Written to `simulations/quest/variations/flow-resilience-variations-R1-2026-03-14.md`.

---

## Summary

Five complete variations, all runnable as skill body prompts:

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| **V-01** | Output format — table per scenario | Table headers act as a mandatory four-field checklist (C-02); fields cannot be buried in prose |
| **V-02** | Role sequence — Ops SME leads, Dev validates | Operational ground truth first → richer commerce domain grounding (C-05) before technical filtering trims it |
| **V-03** | Lifecycle emphasis — Amend loop required | Re-simulation after findings forces recovery paths to be concrete enough to verify, not aspirational (C-07) |
| **V-04** | Phrasing register — Conversational walkthrough | "Walk me through" framing produces richer failure narratives and edge-case workarounds that formal mode suppresses (C-03, C-05) |
| **V-05** | **Combined** — table + ops-first + mandatory gap section | Structurally blocks the three rubric fast-path failures: pure prose, domain-agnostic, and missing gap types |

**Design rationale for V-05**: the three combined axes each target a different fast-path failure condition. The table blocks prose escape. The ops-first role blocks domain-agnostic analysis. The mandatory three-subsection closing (GAP / DCV / MRF) with numbered finding IDs blocks the "all three gap types must appear" failure even if the model would otherwise blend them together.
appear
as a table with exactly these four rows:

```
| Field        | Content |
|--------------|---------|
| State        | What state is the system in when this failure occurs? |
| Capability   | What can the user (cashier / customer / operator) still do? |
| Data at risk | What data may be lost, stale, or inconsistent? |
| Recovery     | Step-by-step: who acts, what happens, in what order? |
```

**Class A — Offline / network disconnection**
Simulate the system losing connectivity entirely for a sustained period (e.g., 30–60 minutes)
during active commerce operations. The scenario must specify: detection latency, which operations
continue locally, which fail immediately, and what is queued vs discarded.

**Class B — Partial service failure**
Simulate one downstream dependency becoming unavailable (e.g., pricing service 503, loyalty
service timeout, inventory service returning stale data). The system is partially operational.
Identify which commerce flows degrade gracefully and which fail hard.

**Class C — Eventual consistency conflict**
Simulate a state conflict that emerges when two writes to the same record occur in different
partitions during a split or offline window (e.g., refund processed at Store A while Store B
processes the same transaction offline). Specify the conflict resolution strategy in use
(last-write-wins / merge / manual-reconcile / reject-stale) and judge whether it is adequate
for this data type.

---

### Step 3 — Severity and blast radius

After each scenario table, add a one-line annotation:

```
Severity: [degraded | impaired | down]  |  Blast radius: [who / how many are affected]
```

---

### Step 4 — Gap identification

Produce a **Findings** section with three labeled subsections:

**Offline Experience Gaps** — Operations that fail during Class A with no graceful fallback.
Name each gap specifically (e.g., "loyalty point redemption has no offline fallback, cashier
must manually calculate equivalent discount with no audit trail").

**Data Consistency Violations** — Records that can be in an incorrect state after any of the
three failure classes. Name the record type, the inconsistency, and whether it is detectable
before or only after the fact.

**Missing Recovery Flows** — Recovery sequences that are absent, incomplete, or require manual
intervention that should be automated. Name the missing flow and the risk if it stays missing.

---

### Step 5 — Write artifact

Write the completed analysis to:
`simulations/flow/resilience/{topic}-resilience-{date}.md`

Use today's date for `{date}`. Return the file path when done.

---

## V-02 — Role Sequence (Operations SME leads, Dev validates)

**Axis**: Role sequence
**Hypothesis**: Leading with the Store Operations SME before the Commerce Developer surfaces
operational/physical reality first (cashier behavior, customer expectations, shift constraints),
which grounds findings in commerce domain (C-05) before technical filtering (C-04) trims
what is or is not achievable.

---

You are running a two-role resilience simulation for `{topic}`.

**Input**
- `{topic}` — the system or flow under analysis
- `{signal}` — read any existing signal artifacts for `{topic}` to load context

**Roles (run in this order)**

1. **Store Operations SME** — knows the physical workflow: what cashiers actually do when the
   system fails, what customers tolerate, what the shift manager's options are, what the store's
   SLA with HQ looks like. Describes failure scenarios from the floor, not from the code.

2. **Commerce Developer** — knows the system: what is actually implemented, what the offline
   capability profile is, what conflict resolution the platform provides, what the upload queue
   behavior is. Validates or corrects the SME's description against technical reality.

---

### Phase 1 — SME walkthrough (operational perspective)

The Store Operations SME describes what happens during each of three degradation scenarios from
the perspective of someone on the floor:

**Scenario 1 — Full network loss**
Tell the story of a 45-minute network outage during peak hours. What does the cashier see?
What workarounds does the shift manager reach for? What do customers experience? What data is
being written to a notebook or receipt tape because the system cannot capture it? Where does
the SME say "this is where we always have a problem"?

**Scenario 2 — Dependent service unavailable**
A pricing service or loyalty service goes down mid-shift. From the floor: does the cashier know
something is wrong, or does it fail silently? What do they do? What do they tell customers?
What gets escalated to the call center?

**Scenario 3 — Post-reconnect conflict**
After the network comes back, transactions start uploading. The SME describes what the shift
manager sees on the reconciliation screen. What does a conflict look like to a non-technical
operator? What is the escalation path if the shift manager cannot resolve it?

---

### Phase 2 — Developer validation (technical perspective)

The Commerce Developer reviews each SME scenario and provides:

- **Correction or confirmation** of what the system actually does in this state
- **Four-field technical trace** for each scenario:
  - State: system state at failure time
  - Capability: operations still functional (with technical basis)
  - Data at risk: what records, why, and whether the risk is detectable
  - Recovery: exact sequence with actor labels (client / server / operator / user)
- **Conflict resolution judgment** for Scenario 3: what strategy is in use, and is it adequate
  given the data type and commerce context?

---

### Phase 3 — Gap synthesis

Both roles contribute to a joint **Findings** section:

- **Offline experience gaps** (SME perspective: what the floor needs that the system does not
  provide; Developer perspective: why it is not provided and what it would take)
- **Data consistency violations** (Developer identifies; SME judges operational impact)
- **Missing recovery flows** (SME identifies what is done manually; Developer labels what could
  be automated and the risk if it is not)

---

### Output

Write the artifact to:
`simulations/flow/resilience/{topic}-resilience-{date}.md`

The artifact must preserve the two-voice structure: SME observations are clearly attributed,
Developer technical traces are clearly attributed, and the gap synthesis is labeled as joint.

---

## V-03 — Lifecycle Emphasis (Amend phase — re-simulation after findings)

**Axis**: Lifecycle emphasis
**Hypothesis**: Requiring a re-simulation after findings forces recovery paths to be concrete
enough to verify, not hypothetical. The amend loop catches whether a proposed fix actually
resolves the gap or just moves it — driving C-07 recovery path specificity and C-08 conflict
resolution adequacy.

---

You are a **Commerce / Distributed Systems domain expert** running a resilience simulation with
an amend loop.

**Input**
- `{topic}` — the system or flow under analysis
- `{signal}` — read any existing signal artifacts for `{topic}` to load context

The simulation runs in four phases: **Setup → Execute → Findings → Amend**. Do not skip Amend.

---

### Phase 1 — Setup

Identify the system boundary: what is in scope for `{topic}`, what is a downstream dependency,
and what is out of scope entirely. Load the offline capability profile: list every operation
that the system supports offline and every operation that requires connectivity. This list is
the baseline for gap identification.

Define three degradation scenarios that cover:
- Full connectivity loss (offline)
- Single dependent service unavailable (partial failure)
- Concurrent writes across a partition boundary (eventual consistency)

For each scenario, state the hypothesis before simulation: what do you expect the system to do?

---

### Phase 2 — Execute

Simulate each scenario as a timeline. For each time step, state what the system does and what
the user (cashier / customer / operator) experiences. Mark moments where the system behavior
diverges from the hypothesis with a `[DELTA]` tag.

End each timeline with a four-field snapshot:
- **State**: what state is the system in at the point of maximum degradation?
- **Capability**: what can users still do, with what limitations?
- **Data at risk**: what records are in an unknown or inconsistent state?
- **Recovery**: the sequence of events that returns the system to a healthy state, with actor
  labels (client initiates retry / server detects conflict / operator approves resolution / user
  confirms re-submission)

---

### Phase 3 — Findings

From the Execute phase, produce labeled findings:

**Offline experience gaps** — operations in the offline capability profile that fail without
a graceful fallback. For each gap: name the operation, describe the failure mode, describe the
cashier or customer impact, and state whether the gap is known/documented or newly identified.

**Data consistency violations** — records that can be in an incorrect or inconsistent state
after any scenario. For each violation: name the record, describe how the inconsistency arises,
state whether it is detectable before customer impact occurs, and rate the severity
(silent data corruption / detectable with reconciliation / surfaced immediately).

**Missing recovery flows** — sequences that require manual steps that could or should be
automated. For each: name the missing flow, describe the manual workaround currently in use,
and estimate the risk if it remains manual (frequency × impact).

---

### Phase 4 — Amend

For each finding, the Commerce Developer proposes a resolution and re-simulates:

1. State the proposed resolution (code change, operational workaround, or configuration change).
2. Re-run the relevant scenario timeline with the resolution applied.
3. Confirm whether the finding is resolved, partially resolved, or transferred to a new finding.
4. If the resolution introduces a new risk, document it as a new finding and repeat.

The Amend phase ends when no finding is `unresolved` or when the developer explicitly accepts
a remaining gap as a known limitation with a documented rationale.

---

### Output

Write the artifact to:
`simulations/flow/resilience/{topic}-resilience-{date}.md`

The artifact must include all four phases. Findings must be in the labeled three-section format.
The Amend phase must show before/after for each finding it addresses.

---

## V-04 — Phrasing Register (Conversational walkthrough)

**Axis**: Phrasing register
**Hypothesis**: Conversational, imperative "walk me through" framing produces richer failure
scenario narratives — the model elaborates on edge cases it would summarize in formal mode —
and surfaces cashier workarounds and customer experience details that structured formats
suppress. This raises commerce domain grounding (C-05) and gap specificity (C-03).

---

You are a seasoned Commerce and distributed systems expert. I need you to walk me through what
happens to `{topic}` when things go wrong.

Before you start, read `{signal}` if it exists — I want you to know what signals we've already
gathered for this topic.

---

**Walk me through three situations.**

---

**Situation 1: The network goes down.**

The store's connectivity drops. Just gone. It happens in the middle of a busy lunch rush. Walk
me through the next 45 minutes, minute by minute if something interesting happens, summarized
otherwise. I want to know:

- What does the cashier see? When do they notice?
- What can they still ring up? What do they have to turn away?
- What is being written somewhere locally that might not make it back to HQ?
- When the network comes back, what happens? Does it just work? Does someone have to do
  something? What if two things conflict?

Don't give me the happy path unless the happy path is actually what happens. Tell me where it
gets complicated.

---

**Situation 2: A service the system depends on goes down.**

Pick the dependency that would hurt the most if it were unavailable — pricing, loyalty, inventory,
payment gateway, whatever makes the most sense for `{topic}`. Now that dependency is returning
503s. Walk me through:

- Does the system know immediately, or does it find out slowly?
- What does the user experience? Does the UI tell them something is wrong, or does it just
  behave strangely?
- What commerce operations are now broken, and which ones limp along?
- What does a cashier actually do when this happens? What do they tell the customer?
- What data is in a bad state after this resolves?

---

**Situation 3: Two things wrote to the same record at the same time.**

This one happens during recovery, usually. A refund was processed at one store while the same
transaction was still open in an offline queue at another store. Or a price was updated centrally
while the POS had a cached version. Walk me through:

- What does the conflict look like in the data?
- Who finds out, and when?
- What does the conflict resolution strategy do — and is that the right call for this type of data?
- What is the blast radius: one transaction, one customer, one store, or wider?
- What does the operator see? Can they resolve it themselves?

---

**Now tell me what's missing.**

After walking through those three situations, give me three lists:

1. **Offline gaps** — things users needed to do during Situation 1 that the system simply could
   not support. Be specific. "Loyalty redemption" is not enough — tell me what the cashier
   actually did instead and whether that workaround creates a downstream problem.

2. **Consistency problems** — data that ended up wrong or unknown after any of these three
   situations. Tell me whether the system knows it's wrong or whether someone will discover it
   later.

3. **Recovery flows that don't exist yet** — steps that a human is currently doing by hand
   that the system should handle automatically. What is the risk of keeping it manual?

---

Write the analysis to:
`simulations/flow/resilience/{topic}-resilience-{date}.md`

---

## V-05 — Combined (Table format + Ops-first role sequence + Explicit gap closing)

**Axis**: Combined — output format (table) + role sequence (ops-first) + lifecycle emphasis
(mandatory gap-identification closing section with all three types labeled and actionable)
**Hypothesis**: The combination eliminates the three most common failure modes identified in
the rubric: pure prose output (blocked by table requirement), domain-agnostic analysis (blocked
by ops-first role), and missing gap types (blocked by mandatory three-section closing). This
should pass all five essential criteria and drive recommended criteria through structural pressure.

---

You are running a two-role resilience simulation for `{topic}`.

**Input**
- `{topic}` — the system or flow under analysis
- `{signal}` — read any existing signal artifacts for `{topic}` before starting

**Roles**

Run roles in this order. Each role contributes to the same output sections — do not produce
separate documents per role.

1. **Store Operations SME** — speaks first in every scenario. Describes what the cashier,
   shift manager, and customer experience from the floor. Does not speculate about system
   internals. Does identify operational workarounds, manual steps, and human impact.

2. **Commerce Developer** — speaks second in every scenario. Validates or corrects the SME
   account, adds technical detail, and fills in the four-field structure.

---

### Section 1 — Offline / Network Loss Scenario

**SME account** (1–3 short paragraphs):
What does the floor experience? What does the cashier do? What do customers see?
What operations stop? What workarounds appear?

**Developer four-field trace**:

| Field        | Content |
|--------------|---------|
| State        | |
| Capability   | |
| Data at risk | |
| Recovery     | [actor-labeled steps: client → server → operator → user] |

**Classification**:
```
Severity: [degraded | impaired | down]  |  Blast radius: [scope and population]
```

---

### Section 2 — Partial Service Failure Scenario

Choose the dependency most critical to `{topic}`'s commerce operations (pricing service, loyalty
service, inventory service, payment gateway). That service is now returning 503s or timing out.

**SME account** (1–3 short paragraphs):
Does the cashier know? What do they tell customers? What is escalated?

**Developer four-field trace**:

| Field        | Content |
|--------------|---------|
| State        | |
| Capability   | |
| Data at risk | |
| Recovery     | [actor-labeled steps] |

**Classification**:
```
Severity: [degraded | impaired | down]  |  Blast radius: [scope and population]
```

---

### Section 3 — Eventual Consistency Conflict Scenario

Simulate a state conflict: two writes to the same record occurred in different partitions
during the offline or failure window (e.g., cross-store refund, dual-write inventory decrement,
stale price applied to offline transaction).

**SME account** (1–3 short paragraphs):
What does the reconciliation screen look like to the shift manager? What is the escalation path
if they cannot resolve it?

**Developer four-field trace**:

| Field        | Content |
|--------------|---------|
| State        | |
| Capability   | |
| Data at risk | |
| Recovery     | [actor-labeled steps] |

**Conflict resolution**:
State the strategy in use: `last-write-wins | merge | manual-reconcile | reject-stale`.
Assess whether that strategy is adequate for the record type involved. If not adequate, name
the failure mode.

**Classification**:
```
Severity: [degraded | impaired | down]  |  Blast radius: [scope and population]
```

---

### Section 4 — Gap Identification (mandatory — do not omit or merge with scenarios)

This section is separate from the scenarios. Each subsection must name specific, actionable
findings — not generic observations.

**Offline Experience Gaps**

For each gap: name the operation, describe what the user must do instead, and state whether
the workaround creates downstream data problems.

- GAP-01: [name] — [description] — [downstream risk]
- GAP-02: ...

(minimum one; add as many as found)

**Data Consistency Violations**

For each violation: name the record type, describe the inconsistency, state whether it is
detectable before customer impact.

- DCV-01: [record] — [inconsistency] — [detectability]
- DCV-02: ...

(minimum one)

**Missing Recovery Flows**

For each: name the missing automated flow, describe the current manual workaround, estimate
frequency × impact.

- MRF-01: [name] — [manual workaround] — [risk if stays manual]
- MRF-02: ...

(minimum one)

---

### Output

Write the artifact to:
`simulations/flow/resilience/{topic}-resilience-{date}.md`

Return the file path when done.
