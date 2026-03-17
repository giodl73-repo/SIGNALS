# flow-throttle Rubric v6 — Variations V-01 through V-05

---

## V-01

**Variation axis**: Role sequence — three-role pipeline with explicit phase-close prohibition statements.
**Hypothesis**: Locking Domain Expert → Architect → UX Advocate with named prohibition statements at each phase boundary makes retroactive source injection structurally detectable, raising C-11/C-13/C-15/C-16/C-17.

---

You are executing a flow-throttle simulation. Three roles operate in strict sequence. Each role may only draw from artifacts produced in prior phases. A role may not introduce new evidence after its phase closes.

**Inputs**
Topic: {{topic}}
Scenario: {{scenario}}

---

### Phase 1 — Domain Expert

#### 1.1 Source Register

Before stating any limit value, list every source you will draw from in this analysis. For each entry:
- Source name (document title, reference page, or artifact name)
- What tier or behavior it documents

After the list, write:

> Source Register closed. Phase 2 draws only from these sources. No new source reference may appear after this line. — Prevents retroactive source injection.

#### 1.2 Tier Inventory

Enumerate every rate-limit tier relevant to the scenario.

| Tier | Enforcing Component | Scope | Threshold | Source | Binding? |
|------|--------------------|----|-----------|--------|---------|

Rules:
- Threshold must be a number from the Source Register, or "not documented."
- At most one tier may be Binding? = Y.
- For the binding tier: state the causal reason it fails before all others (one paragraph below the table).
- For at least one Binding? = N tier: state the mechanism that prevents it from failing first under this load pattern.

After the table, write:

> Tier Inventory closed. Phase 2 may not introduce any new tier, limit value, or source reference. Phase 3 will enumerate exactly the tiers in this table. — Prevents scope creep into consequence phase.

---

### Phase 2 — Architect

Draw only from Phase 1. No new tiers, thresholds, or sources permitted.

#### 2.1 Primary Bottleneck

Name the binding tier from Phase 1. Restate its causal reason.

#### 2.2 Backpressure Propagation (minimum 2 hops)

Starting from the primary bottleneck, trace how throttle pressure propagates. For each hop:
- Component reached
- Mechanism: queue fill / connection hold / retry accumulation / timeout cascade
- Observable effect at this hop

Minimum two hops. Continue until the chain is absorbed or exhausted.

#### 2.3 Unprotected Burst Path

Name at least one path where burst traffic bypasses or overwhelms throttle controls. Identify the burst vector and explain why the path is unprotected.

#### 2.4 Cascading Throttle Failure

Describe one scenario: Tier A throttles → load transfer mechanism → Tier B throttles. Name both tiers and the compounding effect on users.

After Phase 2, write:

> Phase 2 closed. Phase 3 will enumerate tiers from the Phase 1 Tier Inventory — no others. — Prevents coverage elision: a missing tier produces a detectable gap against the inventory.

---

### Phase 3 — UX Advocate

For each tier in the Phase 1 Tier Inventory — in the same order, all tiers, no additions:

| Tier | User-Visible Effect | Retry-After Compliance | Severity |
|------|--------------------|-----------------------|---------|

- User-Visible Effect: specific — error code returned, latency spike magnitude, silent drop, queue delay, degraded mode.
- Retry-After Compliance: Pass / Fail / N/A — if Fail, state the downstream consequence.
- Severity: High / Medium / Low with one-line justification.

---

### Phase 4 — Mitigations and Risk Ranking

**Mitigations**: For each gap identified in Phase 2 (burst path, retry-after failure, cascade):
- Mitigation: concrete action
- Tradeoff: what it costs or constrains

**Severity ranking**: Rank all identified risks. For each: rank, risk name, severity (H/M/L), justification by frequency or blast radius.

---

### Phase 5 — Global Self-Verification

Map this output against each essential criterion by category ID.

| ID | Criterion | Content Location (cite phase and section) | Verdict |
|----|-----------|------------------------------------------|--------|
| C-01 | Primary bottleneck with causal reason | | PASS/FAIL |
| C-02 | Backpressure propagation ≥ 2 hops with mechanism per hop | | PASS/FAIL |
| C-03 | ≥ 2 throttle tiers with enforcing component | | PASS/FAIL |
| C-04 | UX described at every named tier | | PASS/FAIL |
| C-05 | Unprotected burst path identified | | PASS/FAIL |

If any criterion maps to no content, mark FAIL and describe the gap explicitly.

---

## V-02

**Variation axis**: Output format — table-dominant structure where every analytical artifact is a numbered table.
**Hypothesis**: Tables enforce coverage completeness through blank-cell visibility, raise C-03/C-04/C-08 compliance, and make cross-referencing between phases mechanical.

---

You are a Power Automate throughput domain expert running a flow-throttle analysis. Deliver all outputs as structured tables. Prose is permitted only for the binding-tier causal reason, burst path narrative, and individual self-verification verdict notes.

**Inputs**
Topic: {{topic}}
Scenario: {{scenario}}

---

### Table 1 — Source Register

Before stating any number, commit your evidence base.

| # | Source Name | URL or Reference | Tiers / Behaviors Documented |
|---|------------|-----------------|------------------------------|

Complete this table before proceeding. Every number in the analysis must cite a row from this table by row number, or be labeled "not documented."

---

### Table 2 — Tier Inventory

| Tier | Enforcing Component | Scope | Threshold | T1 Row | Binding? | Notes |
|------|--------------------|----|-----------|--------|---------|-------|

- Threshold: numeric value traced to Table 1 row, or "not documented."
- T1 Row: the Table 1 row number that provides the threshold.
- Binding? = Y for exactly one tier.
- Notes: for the binding tier, write the causal reason. For at least one non-binding tier, write the mechanism that prevents it from binding first.

---

### Table 3 — Backpressure Propagation

| Hop | From Component | To Component | Mechanism | Observable Effect |
|-----|---------------|-------------|-----------|------------------|

Starting hop is the binding tier from Table 2. Minimum two hops. Mechanism must be one of: queue fill / connection hold / retry accumulation / timeout cascade / other (specify).

---

### Table 4 — UX Consequence Map

One row per tier from Table 2. No tier may be omitted. No tier may be added.

| Tier | User-Visible Effect | Error Signal | Retry-After Honored? | Severity |
|------|--------------------|--------------------|---------------------|---------|

- User-Visible Effect: specific — "run halts with HTTP 429," "20-second queue delay before next trigger," "silent retry with no user notification."
- Retry-After Honored? Pass / Fail / N/A — if Fail, add cascade risk to Table 5.
- Severity: High / Medium / Low.

---

### Table 5 — Risk Register

| ID | Risk Name | Type | Path or Scenario | Why Unprotected or Compounding | Severity |
|----|-----------|------|-----------------|-------------------------------|---------|

Required rows:
- At least one Type = Burst (unprotected burst path)
- At least one Type = Cascade (two-tier compounding failure)
- At least one Type = RetryAfter (caller ignoring Retry-After)

---

### Table 6 — Mitigation Register

| Risk ID (from T5) | Mitigation | Tradeoff |
|-------------------|-----------|---------|

Every row in Table 5 must have a corresponding row here.

---

### Table 7 — Severity Ranking

| Rank | Risk ID (from T5) | Risk Name | Severity | Justification |
|------|------------------|-----------|---------|--------------|

Rank all rows from Table 5. Justification must reference frequency, blast radius, or both.

---

### Table 8 — Global Criterion Coverage

| ID | Criterion | Table(s) Where Satisfied | Verdict |
|----|-----------|------------------------|--------|
| C-01 | Primary bottleneck with causal reason | T2, T2 Notes | PASS/FAIL |
| C-02 | Backpressure propagation ≥ 2 hops | T3 | PASS/FAIL |
| C-03 | ≥ 2 tiers with enforcing component | T2 | PASS/FAIL |
| C-04 | UX at every named tier | T4 | PASS/FAIL |
| C-05 | Unprotected burst path | T5 | PASS/FAIL |
| C-06 | Retry-after compliance evaluated | T4, T5 | PASS/FAIL |
| C-07 | Cascading throttle scenario | T5 | PASS/FAIL |
| C-08 | Quantified thresholds with source | T2 | PASS/FAIL |

Flag any FAIL with the specific missing content.

---

## V-03

**Variation axis**: Lifecycle emphasis — each phase opens with a formal declaration, executes bounded work, and closes with an auditable data-lock statement before the next phase may begin.
**Hypothesis**: High-ceremony boundary language with explicit data-class prohibitions makes phase compliance verifiable by inspection and raises C-15/C-16/C-17 scores.

---

You are running a flow-throttle analysis in four phases. Each phase opens with a declaration, executes a scoped task, and closes with an auditable statement. Do not begin a phase before its predecessor has closed. Do not import data across a phase boundary in the reverse direction.

**Inputs**
Topic: {{topic}}
Scenario: {{scenario}}

---

```
═══════════════════════════════════════════════════════════
PHASE OPEN — Phase 1: Evidence Commitment
Role: Domain Expert (Power Automate throughput)
Permitted inputs: external documentation, platform references
Outputs: Source Register, Tier Inventory
═══════════════════════════════════════════════════════════
```

**Source Register**

List every document, reference page, or official artifact this analysis draws from. For each: source name, what limits or behaviors it covers. If a threshold cannot be attributed to a named source, it will be labeled "not documented."

**Tier Inventory**

| Tier | Enforcing Component | Scope | Threshold | Source | Binding? |
|------|--------------------|----|-----------|--------|---------|

- At most one Binding? = Y.
- For the binding tier: state the causal mechanism that makes it fail first.
- For at least one non-binding tier: state the mechanism that prevents it from binding first under this load pattern.

```
═══════════════════════════════════════════════════════════
PHASE CLOSE — Phase 1: Evidence Commitment
Source Register and Tier Inventory are now locked.
Permitted carryforward to Phase 2: Source Register rows, Tier Inventory rows.
Prohibited after this line: new tier names, new threshold values, new source references.
═══════════════════════════════════════════════════════════
```

---

```
═══════════════════════════════════════════════════════════
PHASE OPEN — Phase 2: Propagation Analysis
Role: Systems Architect
Permitted inputs: Phase 1 Source Register, Phase 1 Tier Inventory
Outputs: Propagation chain, Burst path, Cascade scenario
═══════════════════════════════════════════════════════════
```

**Primary Bottleneck**: Name the binding tier from Phase 1 and restate its causal reason.

**Backpressure Propagation (minimum 2 hops)**: For each hop from the primary bottleneck:
- Component reached
- Mechanism: queue fill / connection hold / retry accumulation / timeout cascade
- Observable effect at this hop

**Unprotected Burst Path**: Identify one path where burst traffic bypasses or overwhelms throttle controls. Name the burst vector and the protection gap.

**Cascading Throttle Failure**: Describe one scenario — Tier A throttles → load transfer mechanism → Tier B throttles. Name both tiers and the compounding user-visible effect.

```
═══════════════════════════════════════════════════════════
PHASE CLOSE — Phase 2: Propagation Analysis
Propagation chain, burst path, and cascade scenario are locked.
Permitted carryforward to Phase 3: all tiers from Phase 1 Tier Inventory — all of them.
Prohibited after this line: tier names or limit values absent from Phase 1 Tier Inventory.
Phase 3 will enumerate exactly the tiers in the Phase 1 Tier Inventory — no more, no fewer.
═══════════════════════════════════════════════════════════
```

---

```
═══════════════════════════════════════════════════════════
PHASE OPEN — Phase 3: Consequence Mapping
Role: UX Advocate
Permitted inputs: Phase 1 Tier Inventory (complete), Phase 2 findings
Outputs: UX consequence map, retry-after compliance assessment
═══════════════════════════════════════════════════════════
```

For each tier in the Phase 1 Tier Inventory — in order, all tiers, no new entries:

**Tier: [name]**
- User experience: specific — error code returned, latency spike magnitude, silent drop, queue delay, degraded mode
- Retry-after: Pass / Fail / N/A — if Fail, state the downstream consequence
- Severity: High / Medium / Low — one-line justification

```
═══════════════════════════════════════════════════════════
PHASE CLOSE — Phase 3: Consequence Mapping
UX consequence map complete. All tiers from Phase 1 covered.
═══════════════════════════════════════════════════════════
```

---

```
═══════════════════════════════════════════════════════════
PHASE OPEN — Phase 4: Synthesis and Self-Verification
Role: All roles reviewing collectively
═══════════════════════════════════════════════════════════
```

**Mitigations**: For each gap found in Phase 2 — burst path, retry-after failure, cascade:
- Mitigation: concrete action
- Tradeoff: what it costs or constrains

**Severity ranking**: Rank all risks from high to low. For each: rank, risk name, severity (H/M/L), justification by frequency or blast radius.

**Global Criterion Coverage**

| ID | Criterion | Phase Where Satisfied | Verdict |
|----|-----------|----------------------|--------|
| C-01 | Primary bottleneck with causal reason | | PASS/FAIL |
| C-02 | Backpressure propagation ≥ 2 hops | | PASS/FAIL |
| C-03 | ≥ 2 tiers with enforcing component | | PASS/FAIL |
| C-04 | UX at every named tier | | PASS/FAIL |
| C-05 | Unprotected burst path | | PASS/FAIL |

```
═══════════════════════════════════════════════════════════
PHASE CLOSE — Phase 4: Analysis complete.
═══════════════════════════════════════════════════════════
```

---

## V-04

**Variation axis**: Phrasing register — conversational imperative, as if coaching a practitioner through each step.
**Hypothesis**: Conversational register lowers prompt-following friction and produces more specific, natural UX descriptions in C-04; step-numbered structure produces higher completion rates on C-02 and C-03.

---

You're a Power Automate throughput expert working through a rate-limit analysis step by step. Work through each step in order. Don't skip ahead and don't go back to add evidence once you've moved on.

**Your scenario**
Topic: {{topic}}
What you're analyzing: {{scenario}}

---

### Step 1: Lock down your sources before you say anything else

Before you write a single number, list every source you're drawing from. For each one: what's its name, and what part of the system does it cover?

Once your list is written, add this line:
> Sources locked — everything below draws from this list only.

If you can't name a source for a number, you don't get to state that number. Write "not documented" instead.

---

### Step 2: Map out the throttle tiers

Now that your sources are committed, identify every rate-limit tier in this scenario. For each one, tell me:
- What's the tier called?
- Which component enforces it?
- What's its scope — per-connection, per-user, per-tenant, or platform-wide?
- What's the threshold? (Use your source list, or say "not documented.")

One tier gets to be the binding tier — the one that fails first. For that tier, explain *why* it fails before the others: what's the causal mechanism? For at least one of the others, explain what keeps it from being the bottleneck under this load pattern.

When you're done, write:
> Tier map locked. The UX section covers exactly these tiers — nothing added later.

---

### Step 3: Trace where the pressure goes

Start at your binding tier and follow the pressure. Walk through at least two hops. For each hop, tell me:
- What component did you reach?
- What moved the pressure there — queue fill, connection hold, retries piling up, a timeout cascade?
- What would someone actually observe at this point?

Then find the burst path: where can a traffic spike bypass or overwhelm the throttle controls? Name the path and explain why it's unprotected.

Then show me a cascade: walk through how Tier A throttling causes Tier B to throttle too. Name both, explain the load-transfer mechanism, and describe what it does to users.

---

### Step 4: Describe what users actually see

Go through every tier from Step 2, same order, no additions. For each one:
- What actually happens to the user? Be specific — "the run halts with HTTP 429," "there's a 20-second queue delay before the next trigger fires," "the action silently retries in the background with no notification."
- Does the caller honor Retry-After? If not, what goes wrong downstream?
- How bad is this — High, Medium, or Low? Give one sentence of reasoning.

---

### Step 5: Fix the gaps you found

For each problem you identified — the burst path, the retry-after miss, the cascade — propose a concrete fix and be honest about the tradeoff. Adding a queue buys you what and costs you what? Implementing exponential backoff achieves what and sacrifices what?

---

### Step 6: Rank the risks

List all the risks you've identified, ranked from worst to least bad from the user's perspective. For each one: say why it's at that rank — how often does it happen, and how many users does it hit?

---

### Step 7: Check your own work

Go through each item and confirm you've covered it. Cite where in your output you covered it. If you missed something, say so — don't leave it blank.

- Named the primary bottleneck and explained causally why it fails first? (C-01)
- Traced backpressure for at least two hops, with mechanism and observable effect at each? (C-02)
- Listed at least two distinct throttle tiers with their enforcing component and scope? (C-03)
- Described what users experience at every tier you named? (C-04)
- Identified at least one unprotected burst path? (C-05)

---

## V-05

**Variation axes (combined)**: Inertia framing (C-18) — each constraint annotated with the failure mode it prevents — plus dedicated global self-verification step (C-19) — a named step that maps output against criterion categories by ID.
**Hypothesis**: Annotating every structural constraint with its target failure mode (making prohibitions self-explaining) combined with a dedicated criterion-coverage step produces the highest composite score by simultaneously satisfying C-18 and C-19 while reinforcing auditing compliance with C-15/C-16/C-17.

---

You are executing a flow-throttle simulation with maximum structural rigor. This prompt names the three failure modes that its constraints exist to prevent:

1. **Retroactive source injection** — a number enters the analysis after the evidence phase closes and cannot be traced to a committed source.
2. **Scope creep** — a tier name enters the consequence phase that was absent from the evidence phase and cannot be verified.
3. **Coverage elision** — a tier is omitted from the UX map without a detectable gap in the output.

Each constraint below is annotated with the specific failure mode it guards against.

**Inputs**
Topic: {{topic}}
Scenario: {{scenario}}

---

### Phase 1 — Evidence Commitment (Domain Expert)

#### Source Register

List every document, reference page, or official artifact this analysis draws from. For each:
- Source name
- What limits or behaviors it covers

> **[Constraint — prevents retroactive source injection]**: After this register is complete, no new source reference, URL, or document citation may appear in the analysis. A number that enters after this line closes cannot be traced to a committed source, and the analysis cannot be audited for evidentiary integrity. Every threshold below must cite a row from this register, or be labeled "not documented."

**Phase 1a close**: Source Register locked.

#### Tier Inventory

| Tier | Enforcing Component | Scope | Threshold | Source Row | Binding? |
|------|--------------------|----|-----------|-----------|---------|

- Threshold must trace to a Source Register row by number, or be labeled "not documented."
- Exactly one Binding? = Y.
  - For the binding tier: state the causal reason it fails before all others (one paragraph below the table).
  - For at least one Binding? = N tier: state the mechanism that prevents it from binding first under this load pattern.

> **[Constraint — prevents scope creep into consequence phase]**: After this inventory is complete, no new tier name or limit value may appear in the analysis. Phase 3 will enumerate exactly the tiers in this table. A tier introduced at the consequence stage cannot be verified against the committed evidence base — the analysis cannot confirm whether that tier's limits are documented or inferred.

**Phase 1b close**: Tier Inventory locked.

---

### Phase 2 — Propagation Analysis (Architect)

Draws from Phase 1 only. No new tiers, thresholds, or source references permitted.

#### Primary Bottleneck

Name the binding tier from Phase 1. Restate its causal reason as committed in Phase 1.

#### Backpressure Propagation (minimum 2 hops)

For each hop from the primary bottleneck:
- Component reached
- Mechanism: queue fill / connection hold / retry accumulation / timeout cascade
- Observable effect at this hop

Minimum two hops. Continue until propagation is absorbed or the chain is exhausted.

#### Unprotected Burst Path

Name at least one path where burst traffic bypasses or overwhelms throttle controls. Identify: the burst vector, the bypass mechanism, the protection gap.

#### Cascading Throttle Failure

Describe one scenario: Tier A throttles → load transfer mechanism → Tier B throttles. Name both tiers and the compounding user-visible effect.

> **[Constraint — prevents coverage elision]**: Phase 3 opens with the anchor "For each tier in the Phase 1 Tier Inventory." This anchor makes omission detectable — any tier absent from the UX map can be identified by comparing the consequence phase against the Phase 1 table by name. A consequence phase without an enumeration anchor cannot be audited for coverage without full reconstruction of the output.

**Phase 2 close**: Propagation analysis locked.

---

### Phase 3 — Consequence Mapping (UX Advocate)

**Enumeration anchor**: For each tier in the Phase 1 Tier Inventory — same order, all tiers, no additions, no omissions.

For each tier:

**Tier: [name]**
- User experience: specific — error code returned, latency spike magnitude, silent drop, queue delay, degraded mode. Avoid generic descriptions.
- Retry-After compliance: Pass / Fail / N/A — if Fail, state the downstream cascade consequence.
- Severity: High / Medium / Low — one-line justification referencing frequency or blast radius.

---

### Phase 4 — Mitigations and Risk Ranking

**Mitigations**: For each structural gap identified in Phase 2 — burst path, retry-after failure, cascading failure:
- Mitigation: concrete action
- Tradeoff: what it costs or constrains (latency, complexity, operational overhead)

**Severity ranking**: Rank all identified risks from high to low by user-visible impact. For each: rank, risk name, severity (H/M/L), justification by frequency, blast radius, or both.

---

### ★ GLOBAL SELF-VERIFICATION — Dedicated Step

This is a named, dedicated verification step. It does not perform section-level count-matching ("N tiers named, N UX rows present"). It maps the content of this output against each essential criterion by category ID and confirms the specific content that satisfies each one.

| Criterion ID | Criterion Category | Content That Satisfies It (cite phase and section) | Verdict |
|-------------|-------------------|--------------------------------------------------|--------|
| C-01 | Primary bottleneck with causal reason | | PASS / FAIL |
| C-02 | Backpressure propagation ≥ 2 hops with mechanism per hop | | PASS / FAIL |
| C-03 | ≥ 2 throttle tiers with enforcing component and scope | | PASS / FAIL |
| C-04 | UX described at every named tier | | PASS / FAIL |
| C-05 | Unprotected burst path identified | | PASS / FAIL |

For any FAIL verdict: state the gap explicitly. An acknowledged gap earns partial credit; a silent omission does not.
