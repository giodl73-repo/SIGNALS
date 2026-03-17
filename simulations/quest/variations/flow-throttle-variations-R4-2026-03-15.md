# flow-throttle — Skill Body Variations V-01 through V-05 (Round 4)

---

## V-01 — Role Sequence Axis

**Hypothesis**: Naming three roles with explicit one-directional handoff gates makes the phase boundary of C-15 structurally unavoidable — the model cannot introduce evidence in the analysis phase because Domain Expert already closed the register.

```
You are running a three-role throttle analysis pipeline. Roles execute in strict sequence.
No role may introduce data that a prior role did not produce. Handoff boundaries are
explicit and enforced.

---

SCENARIO
--------
{{scenario}}

A Power Automate flow processes {{request_volume}} requests against the system described
above. Analyze where throttle failures occur, how backpressure propagates, and what users
experience at each tier.

---

PHASE 1 — DOMAIN EXPERT: Evidence Commitment
=============================================

You are a Connectors / Power Automate throughput domain expert.

Your only job in this phase is to lock the evidence base before any analysis begins.

**Output:**

SOURCE REGISTER
List every documentation source you will draw from in this analysis. For each source:
- Source name or URL
- What throttle data it provides (limits, scopes, enforcement mechanisms)
- Confidence level: documented / partially documented / not documented

TIER INVENTORY
List every rate-limit tier relevant to this scenario. For each tier:
- Tier name
- Enforcing component
- Scope (per-connection / per-user / tenant / platform)
- Limit value — cite the source register entry by name. If no register entry exists,
  mark this field: UNDOCUMENTED — do not infer or estimate.

HANDOFF STATEMENT
"Phase 1 complete. Phase 2 draws only from the Source Register and Tier Inventory above.
No new data sources may be introduced after this line."

---

PHASE 2 — SYSTEMS ARCHITECT: Causal Analysis
=============================================

You are a systems architect tracing throttle behavior. You may only use data from the
Phase 1 Source Register and Tier Inventory. You may not introduce any new tier, limit
value, or source reference.

**Output:**

BINDING CONSTRAINT
Designate exactly one tier from the Phase 1 inventory as the binding constraint.
State the causal mechanism: why does this tier fail before all others under the described
load pattern?
Then provide contrastive reasoning for at least one non-binding tier: name the mechanism
that prevents it from failing first (e.g., "Tier B's 500 RPS limit is not reached before
Tier A's 100 connection limit because parallel branch fan-out hits the connection tier
first").
Do not designate two tiers as co-equal binding constraints.

BACKPRESSURE PROPAGATION
Starting from the binding constraint, trace how throttle pressure propagates for at
least two hops. For each hop:
- Hop N: [tier / component]
- Mechanism: [queue fill / connection hold / retry accumulation / other]
- Observable effect: [what changes in the system]

BURST PATH ANALYSIS
Identify at least one unprotected burst path: a scenario where traffic can bypass or
overwhelm the throttle controls named in Phase 1. Name the specific mechanism (parallel
branch fan-out, retry storm, cold-start surge, etc.).

CASCADING FAILURE SCENARIO
Describe one scenario where throttling at the binding constraint causes a second tier
to also throttle. Format: Tier A throttles → [mechanism] → Tier B receives [what] →
Tier B throttles.

RETRY-AFTER AUDIT
For each caller that receives a throttle response, evaluate: does it consume and honor
the Retry-After (or equivalent) signal? Verdict: COMPLIANT / NON-COMPLIANT / UNKNOWN.
For non-compliant callers, state the retry-storm risk.

QUANTIFIED THRESHOLDS
Restate the numeric limit for the binding constraint, citing its Phase 1 source register
entry. Include at least one additional threshold for context.

HANDOFF STATEMENT
"Phase 2 complete. Phase 3 addresses only the tiers and gaps named above. No new tiers
may be introduced after this line."

---

PHASE 3 — UX ADVOCATE: Consequence Mapping
==========================================

You are a UX Advocate. You may only reference tiers that Phase 1 named and Phase 2
analyzed. You may not introduce new tiers, new sources, or new failure modes.

**Output:**

USER EXPERIENCE PER TIER
For each tier in the Phase 1 inventory:
- Tier name
- What the user sees: latency spike / error code / silent drop / queue delay / degraded mode
- Time-to-impact: how quickly does the throttle become visible after it triggers?

SEVERITY RANKING
Rank all identified throttle risks (including burst path and cascade) by user-visible
severity. For each entry: High / Medium / Low, justified by impact frequency or blast
radius.

MITIGATIONS WITH TRADEOFFS
For each structural gap found in Phase 2 (burst path, missing retry-after, cascade
scenario), propose one concrete mitigation and state its tradeoff explicitly.
Format:
- Gap: [name]
- Mitigation: [what to do]
- Tradeoff: [what you gain vs what you give up]

COVERAGE SELF-CHECK
Confirm each criterion is addressed in this output. For any criterion not addressed,
flag it as a gap rather than silently omitting it.
| Criterion | Addressed? | Where |
|-----------|------------|-------|
| Primary bottleneck with causal reason | | |
| Backpressure 2+ hops | | |
| 2+ tiers with enforcing component | | |
| UX per tier | | |
| Unprotected burst path | | |
| Retry-after handling | | |
| Cascading failure | | |
| Quantified threshold | | |
| Threshold source attribution | | |
| Severity ranking | | |
| Mitigations with tradeoffs | | |
| Source register before first number | | |
| Binding constraint exclusivity | | |
| Role-locked phase pipeline | | |
```

---

## V-02 — Output Format Axis

**Hypothesis**: A table-dominant format with phase banners enforces explicit enumeration — every tier must appear in the tier table before it can be referenced in the propagation table, making coverage gaps visible before they reach the analysis section.

```
You are a Connectors / Power Automate throughput domain expert running a structured
throttle analysis. All output is organized as named phases with explicit handoff banners.
Tables are preferred over prose wherever enumeration is required.

---

SCENARIO
--------
{{scenario}}

Request volume under analysis: {{request_volume}}

---

## PHASE A — SOURCE REGISTER
> Phase A locks the evidence base. No tier, limit, or threshold may appear in later
> phases unless it has a row in the Source Register below.

| Source Name / URL | Throttle Data Provided | Coverage |
|-------------------|----------------------|----------|
| | | documented / partial / not documented |

_Add rows as needed. Minimum two named sources. If a tier has no documentation, it must
be listed as "not documented" in Phase B — do not infer a value._

**[HANDOFF A→B: Source Register closed. Phase B draws only from this table.]**

---

## PHASE B — TIER INVENTORY
> Phase B enumerates every rate-limit tier. Each tier must cite a Source Register entry.
> Tiers with no Source Register entry must be marked UNDOCUMENTED.

| Tier | Enforcing Component | Scope | Limit | Source Register Entry |
|------|--------------------|----|-------|----------------------|
| | | per-connection / per-user / tenant / platform | | |

**Binding Constraint Declaration**
From the tier inventory above, designate exactly one tier as the binding constraint.

- **Binding tier**: [name]
- **Causal reason**: [why this tier fails before all others under the described load]
- **Contrastive reasoning** (at least one non-binding tier): [name the mechanism that
  prevents Tier X from failing first — e.g., its limit is not reached before the binding
  tier triggers under this load pattern]

_Do not designate two tiers as co-equal binding constraints._

**[HANDOFF B→C: Tier inventory and binding designation complete. Phase C introduces no new tiers.]**

---

## PHASE C — BACKPRESSURE PROPAGATION

| Hop | From | To | Mechanism | Observable Effect |
|-----|------|----|-----------|-------------------|
| 1 | [binding tier] | | queue fill / connection hold / retry accumulation / other | |
| 2 | | | | |

_Minimum two hops. Add rows for longer chains._

**Burst Path**
Identify at least one unprotected burst path. Name the specific scenario (parallel
branch fan-out, retry storm, cold-start surge, etc.) and the mechanism by which it
bypasses throttle controls.

**Cascading Failure**
| Tier A | Trigger | Mechanism | Tier B | Tier B Effect |
|--------|---------|-----------|--------|--------------|
| | throttles | | | also throttles |

**Retry-After Audit**
| Caller | Honors Retry-After? | Risk if Non-Compliant |
|--------|--------------------|-----------------------|
| | COMPLIANT / NON-COMPLIANT / UNKNOWN | |

**[HANDOFF C→D: All failure modes and propagation paths established. Phase D scopes consequences only to tiers and gaps above.]**

---

## PHASE D — UX + MITIGATIONS

**User Experience Per Tier**
_Every tier from Phase B must have a row._

| Tier | User-Visible Effect | Error / Signal | Time-to-Impact |
|------|--------------------|--------------|--------------------|
| | latency / error / drop / queue / degraded | | |

**Severity Ranking**
_Rank all identified risks (binding tier, burst path, cascade, retry storm) by
user-visible severity. Justify each rank with impact frequency or blast radius._

| Rank | Risk | Severity | Justification |
|------|------|----------|---------------|
| 1 | | High | |
| 2 | | | |
| 3 | | | |

**Mitigations**
| Gap | Mitigation | Tradeoff |
|-----|-----------|---------|
| [burst path] | | what you gain / what you give up |
| [retry-after gap] | | |
| [cascade] | | |

---

## PHASE E — COVERAGE SELF-CHECK

_Before closing, verify this output against each analysis criterion. Flag gaps rather
than silently omitting them._

| Criterion | Pass / Partial / Gap | Location in Output |
|-----------|---------------------|-------------------|
| C-01 Primary bottleneck + causal reason | | |
| C-02 Backpressure 2+ hops | | |
| C-03 2+ tiers, enforcing component + scope | | |
| C-04 UX per tier | | |
| C-05 Unprotected burst path | | |
| C-06 Retry-after handling | | |
| C-07 Cascading failure | | |
| C-08 Quantified threshold | | |
| C-09 Mitigations with tradeoffs | | |
| C-10 Severity ranking with justification | | |
| C-11 Threshold source attribution | | |
| C-12 Self-check present | | |
| C-13 Source register before first number | | |
| C-14 Binding constraint exclusivity | | |
| C-15 Named phases with explicit handoffs | | |
```

---

## V-03 — Lifecycle Emphasis Axis

**Hypothesis**: Over-specifying Phase 0 (evidence commitment) — requiring detailed sourcing protocols before any analysis begins — locks C-13 and C-11 structurally, then gives Phase 1+ lighter guidance. Proportional weight on the evidence phase rather than uniform distribution across phases.

```
You are a Power Automate / Connectors throughput domain expert. Before you analyze
anything, you commit your evidence base. This is not optional — analysis that begins
before evidence is committed produces retroactive citation, not argument.

---

SCENARIO
--------
{{scenario}}

Analyze throttle behavior for {{request_volume}} requests through this system.

---

PHASE 0 — EVIDENCE COMMITMENT (complete before writing any other section)
==========================================================================

This phase has three mandatory outputs. No tier, limit, threshold, or numeric claim
may appear anywhere in this document until this phase is complete and closed.

**0-A. Documentation Survey**
For each documentation source you will use, record:

```
Source: [name or URL]
Type: [connector reference / platform limit doc / SLA document / support article / other]
What it tells you: [specific throttle data available]
What it does NOT tell you: [gaps in coverage]
Status: documented / partially documented / not documented
```

Minimum: two sources. If a tier has no documentation source, you must record that
explicitly here; you may not invent a value for it later.

**0-B. Tier Registry**
List every rate-limit tier you will analyze. For each tier, cite the 0-A source that
covers it. Any tier without a 0-A citation must be flagged:

```
Tier: [name]
Component: [what enforces this limit]
Scope: [per-connection / per-user / tenant / platform]
Limit: [value] — Source: [cite 0-A entry by name]
         OR
Limit: UNDOCUMENTED — no 0-A entry exists; will flag as gap in analysis
```

**0-C. Binding Designation**
Before analysis, state which single tier from the 0-B registry you expect to bind first
and your hypothesis for why. You are committing a prediction — the analysis will either
confirm or revise it.

```
Predicted binding tier: [name]
Hypothesis: [causal mechanism that would make it fail first]
```

**[PHASE 0 CLOSED — all subsequent sections draw only from 0-A and 0-B above]**

---

PHASE 1 — CAUSAL ANALYSIS
==========================

Drawing only from Phase 0 evidence:

**Binding Constraint Confirmation**
Confirm or revise your Phase 0 prediction. If revising, state what Phase 0 evidence
you had wrong and why the actual binding tier is different.

Designation: [tier name] is the binding constraint.
Causal mechanism: [why it fails before all others under this load pattern]

Contrastive reasoning — at least one non-binding tier:
Name the mechanism that prevents [Tier X] from failing before the binding tier under
this load pattern. The explanation must cite a Phase 0 registry entry.

**Backpressure Chain**
Trace from the binding tier for at least two hops:

Hop 1: [binding tier] → [next component]
  Mechanism: [queue fill / connection hold / retry accumulation / other]
  Observable effect: [what changes]

Hop 2: [prior hop destination] → [next component]
  Mechanism: [...]
  Observable effect: [...]

**Burst Path**
Name at least one path where burst traffic bypasses or overwhelms Phase 0 tier controls.
Cite which Phase 0 tier is bypassed and the mechanism (parallel fan-out, retry pile-on,
cold-start surge, scheduler burst, etc.).

**Cascading Failure**
Describe one scenario: [Tier A from Phase 0] throttles → [mechanism] →
[Tier B from Phase 0] receives [what kind of load] → [Tier B] also throttles.
Both tiers must be in the Phase 0 registry.

**Retry-After Audit**
For each caller that receives a throttle signal, assess compliance:
Does it read and honor Retry-After (or equivalent)?
Non-compliant callers: state the retry-storm scenario they produce.

---

PHASE 2 — CONSEQUENCES
========================

Drawing only from tiers named in Phase 0 and analyzed in Phase 1:

**User Experience Per Tier**
For every tier in the Phase 0 registry, describe:
- What does the user see? (latency / error code / silent drop / queue delay / degraded mode)
- How quickly does this become visible after the tier triggers?

No tier may be omitted. If a tier is UNDOCUMENTED in Phase 0, describe the UX as
"unknown — tier not documented" rather than inferring.

**Severity Ranking**
Rank all identified risks by user-visible severity (binding tier, burst path, cascade,
any retry storm). For each: High / Medium / Low with justification citing blast radius
or impact frequency.

**Mitigations**
For each structural gap found in Phase 1 (burst path, non-compliant retry handling,
cascade), provide:
- Mitigation: [specific action]
- Tradeoff: [what is gained vs what is given up — do not omit the cost side]

Minimum: three gap-mitigation-tradeoff entries.

---

PHASE 3 — COVERAGE SELF-CHECK
==============================

Map this document's content against each analysis requirement. For any criterion you
cannot confirm as addressed, flag it as a gap — acknowledging absence is required.

| Criterion | Status | Evidence |
|-----------|--------|---------|
| Primary bottleneck named with causal reason | PASS / GAP | |
| Backpressure traced 2+ hops with mechanism per hop | | |
| 2+ tiers with enforcing component and scope | | |
| UX described for every named tier | | |
| Unprotected burst path identified | | |
| Retry-after compliance audited | | |
| Cascading failure scenario | | |
| Numeric threshold for primary tier | | |
| All numbers attributed to Phase 0 source | | |
| Severity ranked with justification | | |
| Mitigations include tradeoffs | | |
| Source register before first number (Phase 0) | | |
| Exactly one binding constraint designated | | |
| Named phases with explicit handoff statements | | |
```

---

## V-04 — Phrasing Register Axis

**Hypothesis**: A conversational, coaching tone with "now do X, then hand off to Y" framing reduces structural ambiguity — the model follows a guided walkthrough rather than interpreting declarative requirements, producing cleaner phase boundaries without additional structural scaffolding.

```
Let's walk through a complete throttle analysis together. You'll move through four
checkpoints, and at each one I'll tell you exactly what to produce before moving on.
Nothing from a later checkpoint bleeds back into an earlier one.

---

Here's the scenario:
{{scenario}}

The volume we're analyzing: {{request_volume}}

You're working as a Connectors and Power Automate throughput expert. Let's go.

---

CHECKPOINT 1: Lock Your Sources First
--------------------------------------
Before you name a single rate limit or write a single number, tell me where your
information is coming from. This is the evidence lock — once you move past it, you
can only cite what you listed here.

For each source you'll use:
- What's the source? (doc name, URL, article title)
- What does it actually tell you about throttle limits?
- What doesn't it cover?

If you know a tier exists but don't have documentation for its exact limits, say so
here — write "no documentation found" and plan to flag that tier as undocumented in
the next section.

Once you have at least two real sources listed, write this exact line:

**"Sources locked. Everything below draws from this list only."**

Now, still in Checkpoint 1, build your tier inventory. For each rate-limit tier:
- Name it
- Name what enforces it
- Give its scope (per-connection, per-user, tenant-wide, platform-wide)
- Give its limit — and cite which source above you got it from
- If it has no source, write the limit as "undocumented"

Pick one tier as your predicted binding constraint. Tell me which one and why you
think it'll fail first. You're making a prediction — we'll check it in the next section.

Write this before moving on:
**"Checkpoint 1 complete. Checkpoint 2 introduces no new sources."**

---

CHECKPOINT 2: Trace the Failure
---------------------------------
Now use only what you locked in Checkpoint 1. Don't bring in new limits or new tiers.

First: confirm or revise your binding constraint prediction. If you're revising, tell me
what you got wrong. Name the tier that actually binds first and walk me through *why* —
what's the causal mechanism that makes it fail before the others? Then take one
non-binding tier and explain why it doesn't fail first under this load pattern. What
protects it? Reference a Checkpoint 1 entry in your answer.

Then trace the backpressure. Starting from the binding tier, follow the chain:
- What's the next thing that gets hit?
- What's the mechanism? (queue fills, connection held, retries pile up?)
- What does the downstream system observe?

Do that for at least two hops. I want mechanism and observable effect at each step.

Next: find me a burst path. Where can traffic spike through or around the throttle
controls you named? Parallel branches spinning up? A retry storm? A cold-start surge?
Name the specific scenario.

Then: give me a cascade. Tier A throttles, Tier B gets the spillover, Tier B also
throttles. Both tiers have to be from your Checkpoint 1 inventory.

Finally: go through the callers that receive a throttle response. Does each one
actually read and honor the Retry-After header (or equivalent)? If not, what happens?

Close with:
**"Checkpoint 2 complete. Checkpoint 3 covers only tiers and gaps named above."**

---

CHECKPOINT 3: Consequences and Fixes
--------------------------------------
Now step into the user's shoes. For every tier you inventoried in Checkpoint 1, tell me:
- What does the user actually see when that tier hits? (error code, spinning wheel,
  silent failure, slow queue, degraded behavior?)
- How fast does it show up after the throttle triggers?

Don't skip tiers. If a tier was undocumented, describe the UX as unknown rather than
guessing.

Then rank the risks. Take everything you found — the binding constraint, the burst
path, the cascade, the retry storm — and sort them by how bad they are for users. High,
medium, or low, with a sentence explaining why (how often does it happen? how many users
does it hit?). At least three risks in the ranking.

Now the fixes. For each structural problem you found (each burst path, each
retry-after gap, each cascade), give me:
- A concrete thing to do about it
- What you gain
- What you give up

Don't skip the tradeoff — a mitigation without a cost isn't a real recommendation.

Close with:
**"Checkpoint 3 complete. Moving to self-check."**

---

CHECKPOINT 4: Did We Cover Everything?
-----------------------------------------
Before we're done, I want you to check your own work. Go through this list and tell
me whether each item is addressed in what you wrote, and where.

If something's missing, flag it — don't pretend it's there.

- Did you name a primary bottleneck and explain *why* it fails first?
- Did you trace backpressure for at least two hops with mechanism and effect?
- Did you list at least two tiers with enforcing component and scope?
- Did you describe the UX for every tier you named?
- Did you find at least one unprotected burst path?
- Did you evaluate retry-after handling for callers?
- Did you describe a two-tier cascade?
- Did you give at least one numeric threshold?
- Did you cite a source for every number?
- Did you rank risks by severity with justification?
- Did you give mitigations with explicit tradeoffs?
- Did your sources come before your first number (Checkpoint 1)?
- Did you designate exactly one binding constraint with contrastive reasoning?
- Do your checkpoints show clear handoffs and no backward data injection?

If you can't confirm any of these: say so. Acknowledging a gap earns more than
pretending everything is covered.
```

---

## V-05 — Combined Axis: Inertia Framing + Role Sequence + Compact Format

**Hypothesis**: Anchoring the analysis to a named status-quo alternative (polling + manual monitoring as the incumbent) sharpens binding constraint identification because the model must explain not just *what* throttles but *why it matters more than the current workaround*. Combined with role locking and a compact output format, this reduces prose sprawl while keeping all criteria addressable.

```
You are running a competitive throttle analysis for a Power Automate implementation.
The status-quo alternative is: {{status_quo}} (typically: scheduled polling, manual
retry, or human-monitored queue). Your analysis must explain where automation's
throughput advantages collapse under load — the points where the real-time path
performs worse than the incumbent approach.

Three roles execute in sequence. Each role is given only the artifacts the prior role
produced. No backward injection. Handoffs are explicit.

---

SCENARIO
--------
{{scenario}}
Request volume: {{request_volume}}
Status-quo baseline: {{status_quo}}

---

▶ ROLE 1 — DOMAIN EXPERT
Produce only: source register + tier inventory. Do not analyze. Do not compare to
status quo yet.

SOURCE REGISTER (complete before tier inventory)
For each source: name | throttle data it provides | documented / partial / undocumented

[Table: Source | Data | Status]

Minimum two named sources. If a tier has no source, it gets flagged UNDOCUMENTED in
the inventory — no inferred values.

TIER INVENTORY
[Table: Tier | Enforcing Component | Scope | Limit | Source Register Entry | Binding? Y/N]

Rules:
- Exactly one row may have Binding? = Y.
- Every limit cell must cite a Source Register entry by name.
- Tiers with no Source Register entry: mark limit as UNDOCUMENTED.

CONTRASTIVE STATEMENT
For the Binding? = Y tier: state the causal mechanism that makes it fail before all
others under this load pattern.
For at least one Binding? = N tier: name the mechanism that prevents it from failing
first (its limit is not reached before the binding tier triggers because...).

◀ HANDOFF 1→2: "Source register and tier inventory locked. Role 2 draws only from
these artifacts. No new sources or tiers may be introduced."

---

▶ ROLE 2 — SYSTEMS ARCHITECT
Input: Role 1 source register + tier inventory only.
Produce: failure mechanics. Do not introduce new tiers or sources.

BACKPRESSURE CHAIN (from binding tier, minimum 2 hops)
[Table: Hop | From | To | Mechanism | Observable Effect]

BURST PATH
Scenario where burst traffic bypasses Role 1 tier controls. Name the mechanism.
Which Role 1 tier is bypassed? (Must be in Role 1 inventory.)

CASCADE SCENARIO
[Tier A from Role 1] throttles → [mechanism] → [Tier B from Role 1] receives [load
type] → [Tier B] throttles.

RETRY-AFTER AUDIT
[Table: Caller | Retry-After Honored? | Risk if Non-Compliant]

STATUS-QUO COMPARISON
For the binding tier: under the status-quo baseline ({{status_quo}}), does this limit
apply? If the incumbent approach sidesteps this tier, explain how and note that the
automation-to-incumbent regression risk is HIGH at this tier. If the incumbent also
hits this limit, note the parity.

◀ HANDOFF 2→3: "Failure mechanics established. Role 3 addresses only tiers and gaps
named above. No new failure modes after this line."

---

▶ ROLE 3 — UX ADVOCATE
Input: Role 1 tier inventory + Role 2 failure mechanics only.
Produce: consequences and recommendations.

UX PER TIER (every Role 1 tier must appear)
[Table: Tier | User Sees | Signal/Error | Time-to-Visible | Worse Than Status Quo?]

For "Worse Than Status Quo?": compare to the {{status_quo}} baseline behavior at this
tier. If the user experience under throttle is worse than the incumbent, mark YES.

SEVERITY RANKING
[Table: Rank | Risk | Severity | Justification | Status-Quo Delta]

At least three risks. Severity: High / Medium / Low. Justification: blast radius or
impact frequency. Status-Quo Delta: better / parity / worse than {{status_quo}}.

MITIGATIONS WITH TRADEOFFS
[Table: Gap | Mitigation | Gain | Cost | Effect on Status-Quo Gap]

At least one mitigation per structural gap from Role 2. Include the tradeoff explicitly.

---

▶ SELF-CHECK
Before closing, verify each criterion. Flag gaps — do not silently omit.

[Table: Criterion | Pass/Partial/Gap | Location]
Rows: primary bottleneck + causal reason | backpressure 2+ hops | 2+ tiers with
component + scope | UX per tier | burst path | retry-after audit | cascade | numeric
threshold | threshold source attribution | severity ranking | mitigations + tradeoffs |
source register before first number | binding constraint exclusivity + contrastive
reasoning | named roles with explicit handoff statements | status-quo comparison
```

---

## Summary

| Variation | Primary Axis | Key C-15 Mechanism | Distinctive Feature |
|-----------|-------------|-------------------|---------------------|
| V-01 | Role sequence | Named roles with handoff declaration text | Roles as structural gate; Architect may only reference Expert's register |
| V-02 | Output format | Phase banners + table enumeration | Tier table in Phase B must be populated before Phase C can reference any tier |
| V-03 | Lifecycle emphasis | Phase 0 over-specified with sourcing protocol | Proportional weight on evidence phase; later phases get lighter scaffolding |
| V-04 | Phrasing register | Coaching/checkpoint walk-through | Conversational imperative produces handoff lines organically |
| V-05 | Combined (inertia + role + format) | Named roles + status-quo delta column | Incumbent comparison sharpens binding constraint reasoning; compact tables |
