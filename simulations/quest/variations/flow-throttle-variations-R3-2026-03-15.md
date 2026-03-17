# flow-throttle Skill Variations — Round 3 (v3 Rubric)

---

## Variation Summary

| # | Axis | Hypothesis |
|---|------|-----------|
| V-01 | Role sequence — Expert-first source anchoring | Running the domain expert before the architect locks the evidence base before any claim is made, eliminating retroactive citation at the root |
| V-02 | Output format — Table-centric throughout | Structuring every section as a table makes coverage gaps visually obvious as empty cells, improving C-03/C-04 compliance without additional instructions |
| V-03 | Lifecycle emphasis — Hard phase gates with abort conditions | Making Phase 0 a non-skippable gate (abort if no source register) prevents C-13 from being treated as aspirational rather than structural |
| V-04 | Phrasing register — Interrogative/conversational | Framing analysis as questions to answer ("For each tier: what does the user see?") produces more naturalistic UX descriptions and forces per-tier reasoning |
| V-05 | Combined — Expert-first × tables × hard gates | Each axis addresses a distinct failure mode; combining all three collapses the three most common paths to rubric failure simultaneously |

---

## V-01 — Role Sequence: Expert-First Source Anchoring

**Axis**: Role sequence  
**Hypothesis**: Running the Throughput Domain Expert first — to commit the source register and tier inventory — before the architect traces propagation eliminates retroactive citation. Every number the architect uses was locked before the analysis began.

---

You are running a throughput simulation for a Power Automate / Connector scenario.

**Roles run in this order:**
1. **Throughput Domain Expert** — commits source register and tier inventory first; no propagation analysis may begin until this step is complete
2. **Flow Architect** — traces backpressure and burst paths using only tiers the Expert established
3. **UX Advocate** — translates every tier from the Expert's inventory into user-visible experience; no tier may be omitted

---

### Role 1 — Throughput Domain Expert

Your output from this role must appear before any tier analysis, propagation trace, or numeric claim.

**Source Register**

List every document you will draw from. Every numeric threshold in the body must cite a register entry. Tiers with no documented limit must be marked `[undocumented]` — you may not substitute an inferred value.

```
[S1] <document name or URL>
[S2] <document name or URL>
[S3] ...
```

If you cannot identify at least two named sources, state that explicitly and flag all tiers as `[undocumented]`.

**Tier Inventory**

After closing the source register, enumerate the distinct rate-limit tiers applicable to this scenario. Minimum 2 tiers.

For each tier state:
- **Tier ID** (T1, T2, …)
- **Name** — what this tier is called (e.g., per-connection limit, tenant throttle, connector daily cap)
- **Enforcing component** — the system component that applies this limit (e.g., Power Automate runtime, connector gateway, Azure API Management, SharePoint Online)
- **Scope** — what unit the limit applies to (per user, per flow, per tenant, per 24-hour window, etc.)
- **Limit value** — cite source register entry in brackets (e.g., `100 req/min [S1]`); if undocumented write `[undocumented]`, never an inferred number
- **Binding?** — exactly one tier may be marked Y; all others are N

**Binding Constraint Exclusivity**

State which tier is the primary binding constraint and explain the causal mechanism that makes it fail before all others under the described load pattern.

Then, for at least one non-binding tier, explain the specific mechanism that prevents it from being the first failure point. Name the limit value and the load pattern property that means the primary tier is reached first (e.g., "T2's 500 req/min limit is not reached before T1's 100 connections limit because parallel branch fan-out saturates the connection tier before aggregate request volume reaches T2's threshold").

---

### Role 2 — Flow Architect

Work only from the tier inventory the Expert established. Do not introduce new tiers or numeric claims without a source register entry.

**Backpressure Propagation Trace**

Starting at the binding tier, trace throttle pressure for at least 2 hops. For each hop name:
- The source component emitting backpressure
- The target component receiving it
- The mechanism (queue depth increase, connection hold, retry accumulation, timeout cascade, worker starvation, etc.)
- The observable effect at the target component

**Unprotected Burst Paths**

Identify at least one path where burst traffic bypasses or overwhelms throttle controls before they can intercept. Describe:
- The burst trigger scenario (parallel branch fan-out, retry storm, cold-start surge, scheduled batch collision, etc.)
- Why the throttle control does not catch it in time (pre-throttle window, unmetered code path, bypass route)
- The first observable symptom

**Cascading Throttle Failure**

Describe at least one scenario where the primary tier throttling causes a second tier to also throttle, compounding impact. State the chain: Tier A throttles → (mechanism) → Tier B throttles, and the combined user impact that results.

**Retry-After Handling Gaps**

For each caller that receives a throttle response from a named tier, evaluate whether it correctly reads and honors the Retry-After header (or equivalent backoff signal). Verdict per caller: PASS / FAIL / UNKNOWN. For any FAIL, describe the retry storm contribution and the mechanism by which it makes the throttle condition worse.

---

### Role 3 — UX Advocate

For every tier the Expert named in the inventory, describe the user-visible experience during a throttle event. No tier may be skipped.

For each tier state:
- What the user sees (error dialog, spinner, silent drop, degraded response, partial result, timeout message)
- The specific error code or message text if known (e.g., HTTP 429, "Flow run was throttled", "DailyCallLimitExceeded")
- Whether the user receives any indication of when to retry
- The realistic recovery path from the user's perspective (wait, retry manually, contact admin, automatic recovery)

---

### Mitigations and Severity

**Mitigation Recommendations**

For each structural gap identified — burst path, retry-after miss, cascading failure — propose a concrete mitigation and explicitly state the tradeoff it introduces (e.g., adding a queue reduces burst impact but adds latency and requires queue monitoring; exponential backoff reduces retry storms but increases total flow run duration).

Minimum 2 mitigations with explicit tradeoffs.

**Severity Ranking**

Rank all identified throttle risks by user-visible severity. Justify each ranking by referencing impact frequency or blast radius. Minimum 3 risks.

---

### Coverage Self-Verification

Before closing, complete this self-check. If a criterion is missing from both the analysis body and this table, mark it as a gap — do not leave it blank.

| Criterion | Addressed? | Where in output | Gap if not addressed |
|-----------|-----------|-----------------|----------------------|
| Source register committed before first tier | | | |
| Primary bottleneck named with causal reason | | | |
| Binding constraint exclusivity stated with contrastive reasoning | | | |
| ≥ 2 tiers with enforcing component and scope | | | |
| Backpressure propagation traced ≥ 2 hops with mechanism per hop | | | |
| UX described for every named tier | | | |
| Unprotected burst path identified | | | |
| Retry-after handling evaluated per caller | | | |
| Cascading throttle failure scenario described | | | |
| Quantified threshold for primary bottleneck with source citation | | | |
| ≥ 2 mitigations with explicit tradeoffs | | | |
| ≥ 3 risks ranked by severity with justification | | | |

---

## V-02 — Output Format: Table-Centric Throughout

**Axis**: Output format  
**Hypothesis**: When every analysis section is rendered as a structured table, coverage gaps become visually obvious as empty cells. An analyst cannot silently omit a tier's UX description or a hop's mechanism — the empty cell is an immediate flag. This improves C-03 and C-04 compliance without adding explicit coverage rules.

---

You are running a throughput simulation for a Power Automate / Connector scenario. You are acting as a Connectors / Power Automate throughput domain expert.

Produce all output in the table structures defined below. Every section has a required table format. Do not replace tables with prose — prose may accompany a table but may not substitute for it.

---

### Section 1 — Source Register

Complete this table before any tier, threshold, or numeric value appears anywhere in your output.

| Ref | Document Name | URL or Path | Coverage (what tiers/limits it documents) |
|-----|--------------|------------|------------------------------------------|
| S1 | | | |
| S2 | | | |
| S3 (if applicable) | | | |

If a tier has no entry in this table, mark its limit as `[undocumented]` throughout. You may not infer a value for an undocumented tier.

---

### Section 2 — Throttle Tier Inventory

| Tier ID | Tier Name | Enforcing Component | Scope | Limit Value | Source Ref | Binding? |
|---------|-----------|--------------------|----|---|---|---|
| T1 | | | | | | |
| T2 | | | | | | |
| T3 (if applicable) | | | | | | |

Rules:
- Minimum 2 rows
- Exactly 1 row may have Binding? = Y
- Limit Value must reference a source register entry (e.g., `100 req/min [S1]`) or be `[undocumented]`
- Never enter an inferred numeric value without a source reference

---

### Section 3 — Binding Constraint Exclusivity

| Item | Content |
|------|---------|
| Primary binding tier | |
| Causal mechanism (why it fails before others) | |
| Non-binding tier (name at least one) | |
| Mechanism preventing it from failing first | |

---

### Section 4 — Backpressure Propagation Trace

Starting from the binding tier. Minimum 2 hops.

| Hop | From Component | To Component | Mechanism | Observable Effect at Target |
|-----|---------------|-------------|-----------|---------------------------|
| 1 | | | | |
| 2 | | | | |
| 3 (if applicable) | | | | |

---

### Section 5 — User Experience Per Throttle Tier

One row per tier from Section 2. No tier may be omitted.

| Tier ID | UX Signal Type | User-Visible Symptom | Error Code / Message | Retry Guidance Shown? | Recovery Path |
|---------|---------------|---------------------|----------------------|----------------------|---------------|
| T1 | | | | | |
| T2 | | | | | |

---

### Section 6 — Unprotected Burst Paths

| Path ID | Burst Trigger | Why Throttle Doesn't Intercept | First Observable Symptom |
|---------|-------------|-------------------------------|--------------------------|
| B1 | | | |

Minimum 1 row. Describe a concrete burst scenario (parallel branch fan-out, retry storm, cold-start surge, batch collision, etc.).

---

### Section 7 — Retry-After Handling Assessment

| Caller | Throttle Signal Received | Reads Retry-After? | Honors Backoff? | Verdict | Retry Storm Contribution if FAIL |
|--------|------------------------|-------------------|----------------|---------|----------------------------------|
| | | | | PASS/FAIL/UNKNOWN | |

One row per caller that receives a throttle response from a named tier.

---

### Section 8 — Cascading Throttle Failure Scenarios

| Scenario | Tier A (triggers) | Trigger Mechanism | Tier B (cascades to) | Cascade Mechanism | Combined User Impact |
|----------|-------------------|-------------------|----------------------|------------------|----------------------|
| | | | | | |

Minimum 1 scenario. Tier A throttles → mechanism → Tier B throttles.

---

### Section 9 — Mitigation Recommendations

| Gap Addressed | Mitigation | Tradeoff |
|--------------|-----------|---------|
| | | |
| | | |

Minimum 2 rows. Every mitigation must have an explicit tradeoff. A mitigation without a tradeoff and a tradeoff without a mitigation each earn only partial credit.

---

### Section 10 — Severity Ranking

| Rank | Risk Name | Severity (High/Med/Low) | Impact Frequency | Blast Radius | Justification |
|------|-----------|------------------------|-----------------|-------------|---------------|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |

Minimum 3 rows, ordered by severity descending. Justify each rank — unranked lists or rankings without justification are not valid.

---

### Section 11 — Coverage Self-Verification

| Criterion | Table Location | Complete? (Y/N/PARTIAL) | Gap Description |
|-----------|---------------|-------------------------|-----------------|
| Source register before first tier | Section 1 | | |
| Primary bottleneck with causal reason | Sections 2, 3 | | |
| Binding constraint exclusivity with contrastive reasoning | Section 3 | | |
| ≥ 2 tiers with enforcing component and scope | Section 2 | | |
| Backpressure propagation ≥ 2 hops with mechanism | Section 4 | | |
| UX described for every named tier | Section 5 | | |
| Unprotected burst path identified | Section 6 | | |
| Retry-after handling evaluated | Section 7 | | |
| Cascading failure scenario described | Section 8 | | |
| Quantified threshold with source citation | Section 2 | | |
| ≥ 2 mitigations with tradeoffs | Section 9 | | |
| ≥ 3 risks ranked with justification | Section 10 | | |

Self-reported gaps in this table earn partial credit on that criterion. A criterion absent from both the body tables and this table scores FAIL.

---

## V-03 — Lifecycle Emphasis: Hard Phase Gates with Abort Conditions

**Axis**: Lifecycle emphasis  
**Hypothesis**: Framing the analysis as four distinct phases with explicit abort conditions — where each phase must produce a named artifact before the next may begin — makes source commitment structural rather than aspirational. A model cannot satisfy Phase 0's abort condition by reaching back and adding citations after the analysis is written.

---

You are running a throughput simulation for a Power Automate / Connector scenario. You are acting as a Connectors / Power Automate throughput domain expert.

This analysis has four phases. **Each phase must be completed in full before the next phase begins.** Phase 0 has an abort condition: if the condition is not met, the analysis stops and reports why. Phases 1–3 may not reference tiers, thresholds, or mechanisms that were not established in a prior phase.

---

### Phase 0 — Evidence Lock

**Purpose**: Commit the evidence base before any analytical claim.  
**Abort condition**: If fewer than 2 named documentation sources can be identified, write "ABORT: insufficient documentation baseline — cannot produce a sourced throttle analysis for this scenario" and stop. Do not proceed to Phase 1.

**Deliverables for Phase 0:**

**0A — Source Register**

List every document from which you will draw tier names, limit values, or behavioral descriptions in this analysis.

```
[S1] <document name, section, URL>
[S2] <document name, section, URL>
[S3] ...
```

Every numeric value in Phases 1–3 must cite a register entry in brackets. Any tier without a register entry must appear in Phase 1 as `[undocumented]`.

**0B — Scope Declaration**

State the scenario boundary: which connectors, which flow types (instant, scheduled, automated), which tenant tier (developer, standard, premium, enterprise), and the approximate request volume under analysis. This declaration bounds what counts as relevant in Phase 1.

**0C — Phase 0 Completion Signal**

Write: "PHASE 0 COMPLETE — source register locked, scope declared. Proceeding to Phase 1."

Do not write any tier name, throttle value, or propagation claim before this line.

---

### Phase 1 — Throttle Tier Inventory

**Purpose**: Enumerate the distinct rate-limit tiers within the declared scope.  
**Constraint**: Every tier and numeric value must trace to a Phase 0 source register entry. Tiers without a register entry are marked `[undocumented]`.

**Deliverables for Phase 1:**

**1A — Tier Inventory**

For each tier, state: Tier ID, tier name, enforcing component, scope, limit value (with register citation or `[undocumented]`), and whether this tier is the binding constraint (Y/N). Exactly one tier may be binding.

Minimum 2 tiers.

**1B — Binding Constraint Exclusivity**

Name the primary binding tier. Explain the causal mechanism that makes it fail before all others under the declared scope's load pattern. Then, for at least one non-binding tier, name the specific mechanism that prevents it from being the first failure point under that same load pattern.

**1C — Phase 1 Completion Signal**

Write: "PHASE 1 COMPLETE — [N] tiers inventoried, binding constraint designated. Proceeding to Phase 2."

---

### Phase 2 — Propagation and Impact Analysis

**Purpose**: Trace how throttling spreads from the binding tier and describe what users experience.  
**Constraint**: May only reference tiers established in Phase 1. New tiers discovered in Phase 2 require a Phase 1 amendment (add the tier to the inventory, with a source register entry, before continuing).

**Deliverables for Phase 2:**

**2A — Backpressure Propagation Trace**

Starting at the Phase 1 binding tier, trace throttle pressure for at least 2 hops. For each hop: source component, target component, mechanism (queue fill, connection hold, retry accumulation, timeout cascade, worker thread exhaustion, etc.), and observable effect at the target.

**2B — User Experience Per Tier**

For every tier from Phase 1, describe the user-visible experience during a throttle event: what the user sees, the specific error code or message if known, whether the user receives any retry guidance, and the realistic recovery path.

**2C — Unprotected Burst Paths**

Identify at least one path where burst traffic bypasses or overwhelms throttle controls. Name the burst trigger, explain why the throttle control does not intercept it in time, and describe the first observable symptom.

**2D — Cascading Throttle Failure**

Describe at least one scenario where the binding tier throttling causes a second Phase 1 tier to also throttle. State the two-tier chain and the compounded user impact.

**2E — Phase 2 Completion Signal**

Write: "PHASE 2 COMPLETE — propagation traced [N] hops, UX described for [N] tiers, [N] burst paths identified. Proceeding to Phase 3."

---

### Phase 3 — Gap Analysis and Synthesis

**Purpose**: Identify handling failures, propose mitigations, rank risks, and verify coverage.  
**Constraint**: Must address every tier and gap surfaced in Phases 1–2.

**Deliverables for Phase 3:**

**3A — Retry-After Handling Assessment**

For each caller that receives a throttle response from a Phase 1 tier, evaluate whether it correctly reads and honors the Retry-After header (or equivalent backoff signal). Verdict: PASS / FAIL / UNKNOWN. For FAIL, describe the retry storm contribution.

**3B — Mitigation Recommendations**

For each structural gap — burst path from 2C, any retry-after FAIL from 3A, cascade from 2D — propose a concrete mitigation and state the explicit tradeoff. Minimum 2 mitigations. A mitigation without a tradeoff is incomplete.

**3C — Severity Ranking**

Rank all identified throttle risks by user-visible severity (high/medium/low or ordered list). Justify each ranking by referencing impact frequency or blast radius. Minimum 3 risks.

**3D — Coverage Self-Verification**

Complete the following check. A criterion missing from both the analysis body and this check is a gap.

| Criterion | Phase Location | Status | Gap Description |
|-----------|---------------|--------|-----------------|
| Source register before first tier | Phase 0 | | |
| Primary bottleneck with causal reason | Phase 1A, 1B | | |
| Binding exclusivity with contrastive reasoning | Phase 1B | | |
| ≥ 2 tiers with enforcing component and scope | Phase 1A | | |
| Backpressure propagation ≥ 2 hops | Phase 2A | | |
| UX for every named tier | Phase 2B | | |
| Unprotected burst path | Phase 2C | | |
| Cascading failure scenario | Phase 2D | | |
| Retry-after evaluated per caller | Phase 3A | | |
| Quantified threshold with source citation | Phase 1A | | |
| ≥ 2 mitigations with tradeoffs | Phase 3B | | |
| ≥ 3 risks ranked with justification | Phase 3C | | |

**3E — Phase 3 Completion Signal**

Write: "PHASE 3 COMPLETE — analysis closed. Composite coverage: [N]/12 criteria fully addressed, [N] partial, [N] gap."

---

## V-04 — Phrasing Register: Interrogative/Conversational

**Axis**: Phrasing register  
**Hypothesis**: Framing the analysis as a series of questions to answer — rather than imperatives to execute — produces more naturalistic per-tier reasoning. An analyst forced to answer "what does the user see at this tier?" is less likely to copy a generic UX description across all tiers than one told "describe UX for each tier."

---

You are an expert in Power Automate throughput, rate limiting, and connector behavior. A team has asked you to walk them through the throttle landscape for a specific scenario. Think of this as a conversation with a technically curious engineer who wants to understand *why* things fail, not just *that* they fail.

Work through the following questions in order. For each question, reason through it before giving your answer — the reasoning is as important as the conclusion.

---

**Before you start: What are you drawing from?**

Before answering any question about limits or tiers, list the documentation sources you'll rely on. Think of this as your evidence ledger — if a number appears later in your answer, it should trace back to something here.

- Source 1: …
- Source 2: …
- (add more if needed)

If you find yourself about to cite a number with no entry in this list, stop and either add the source or mark the claim as undocumented. Never invent a threshold value.

---

**Question 1: Where will the system break first?**

Given the load pattern in this scenario, which rate-limit tier will be hit first? Don't list all the tiers yet — focus on naming the one that runs out of headroom before everything else, and explain the *mechanism* that makes it the first failure point.

What is it about this specific tier — its scope, its enforcer, its limit value — that means requests pile up here before they pile up anywhere else?

Then: pick at least one other tier that might *seem* like the binding constraint but isn't. Why doesn't it fail first? What property of the load pattern or the tier's limit means it still has headroom when the primary tier is already throttling?

---

**Question 2: What is the full tier landscape?**

Now enumerate the complete set of rate-limit tiers relevant to this scenario — not just the binding one. For each tier, ask yourself:

- *Who enforces this limit?* (Which system component actually applies it — the Power Automate runtime, the connector gateway, Azure API Management, SharePoint Online, the underlying service?)
- *What unit does this limit apply to?* (Per user, per flow, per tenant, per 24-hour window, per minute?)
- *What is the actual limit value, and where did I find it?* (Cite your source ledger. If you can't find documentation, say so — don't fill in a plausible-sounding number.)

You need at least two distinct tiers. The primary bottleneck you named in Question 1 counts as one.

---

**Question 3: Once the first tier throttles, what happens next?**

Throttling at one tier doesn't stay local. What does it do to the components downstream or upstream from it?

Walk through at least two hops. For each hop, ask:

- *What component is now receiving the backpressure?*
- *Through what mechanism?* (Does a queue start filling? Do connections stay held? Do retries start accumulating? Does a timeout cascade begin?)
- *What becomes observable at that component?*

The goal is a chain, not a list. Each hop should connect causally to the next.

---

**Question 4: What does the user experience at each tier?**

Go through every tier you named in Question 2 — not just the binding one. For each one, ask: *if this tier were the only one being hit right now, what would the user see?*

- Is there an error message? What does it say?
- Is there an HTTP code? Which one?
- Does the user know to wait, or does the system just appear stuck?
- Is there any automatic recovery, or does someone need to act?

Be specific to each tier. A generic "the flow run fails" answer doesn't count — different tiers produce different user experiences.

---

**Question 5: Where can burst traffic sneak through?**

Rate limits are designed for steady-state behavior. Where does this scenario have a path where a burst of requests — triggered by parallel branches, a retry storm, a cold-start event, a scheduled batch colliding with live traffic — can hit the system before the throttle controls can respond?

For at least one such path: name the trigger, explain why the throttle doesn't catch it in time, and describe the first symptom a user or operator would notice.

---

**Question 6: Does the system know how to back off?**

When a caller receives a throttle response, does it correctly read and honor the Retry-After header (or whatever backoff signal this system uses)?

For each caller that will receive a throttle response, ask: *does it actually read that header? Does it wait the right amount of time? Or does it retry immediately and make the problem worse?*

If a caller is ignoring the backoff signal: what does that look like, and how does it compound the throttle condition?

---

**Question 7: Can one tier's throttle cause another to throttle?**

Describe a scenario where the primary tier throttling doesn't just impact the user directly — it causes a *second* tier to also throttle, compounding the problem. What's the chain? Why does the second tier get hit harder after the first fires?

---

**Question 8: What would you change, and what would you give up?**

For each structural problem you've found — the burst path, any caller that ignores Retry-After, the cascade scenario — what's the most practical fix, and what does it cost?

For at least two problems: name the mitigation and be honest about the tradeoff. A queue that absorbs burst traffic also adds latency and requires monitoring. Exponential backoff reduces retry storms but makes total run time longer. What does this specific fix buy, and what does it give up?

---

**Question 9: Which risks matter most?**

Rank the throttle risks you've identified by how bad they are for users — not by technical severity, but by the impact a user actually experiences. Consider: how often does this risk trigger? How many users does it affect when it does?

Give at least three risks, in order, with a brief explanation for each ranking.

---

**Before you close: Did you actually answer everything?**

Go back through your answers. For each item below, check whether you addressed it. If you didn't, say so — a self-reported gap is better than a silent miss.

- Did you name a primary bottleneck with a causal reason?
- Did you commit your source ledger before making any numeric claim?
- Did you explain why the binding tier fails before at least one other tier?
- Did you name at least 2 tiers with their enforcing component and scope?
- Did you trace backpressure for at least 2 hops with a mechanism at each?
- Did you describe the user experience for every tier you named?
- Did you identify at least one unprotected burst path?
- Did you evaluate retry-after handling for callers that receive throttle responses?
- Did you describe a cascading failure scenario?
- Did you cite at least one numeric threshold with a source?
- Did you propose at least 2 mitigations with explicit tradeoffs?
- Did you rank at least 3 risks with justification?

---

## V-05 — Combined: Expert-First × Table Format × Hard Phase Gates

**Axis**: Role sequence × Output format × Lifecycle emphasis  
**Hypothesis**: Each single-axis variation targets one failure mode: V-01 eliminates retroactive citation, V-02 makes coverage gaps visible, V-03 prevents phase-skip. Combining all three collapses the three most common paths to rubric failure simultaneously. The cost is prompt length; the benefit is that the structural guarantees are additive, not redundant.

---

You are running a throughput simulation for a Power Automate / Connector scenario.

**Role execution order:**
1. **Throughput Domain Expert** — runs Phase 0 and Phase 1 exclusively; output is a locked source register and tier table
2. **Flow Architect** — runs Phase 2; may only reference tiers from the Phase 1 table
3. **UX Advocate** — co-runs Phase 2B; produces one table row per Phase 1 tier, no omissions
4. **Risk Analyst** — runs Phase 3; synthesizes gaps, mitigations, ranking, and self-verification

**Phase gate rule:** Each phase ends with a completion signal line. The next phase may not begin until that line is written. Phases may not be merged or reordered.

---

### PHASE 0 — Evidence Lock (Throughput Domain Expert)

**Abort condition:** If fewer than 2 named documentation sources exist for this scenario, write `ABORT: documentation baseline insufficient` and stop.

**Table 0A — Source Register**

Complete this table before any tier name, limit value, or behavioral claim appears in your output.

| Ref | Document Name | Section / URL | What It Documents |
|-----|--------------|--------------|-------------------|
| S1 | | | |
| S2 | | | |

**Table 0B — Scope Declaration**

| Field | Value |
|-------|-------|
| Connectors in scope | |
| Flow types (instant / scheduled / automated) | |
| Tenant tier | |
| Approximate request volume under analysis | |

`PHASE 0 COMPLETE — source register locked. [N] sources committed. Proceeding to Phase 1.`

---

### PHASE 1 — Throttle Tier Inventory (Throughput Domain Expert)

No tier or threshold may appear here that is not grounded in Table 0A. Tiers without a register entry must appear as `[undocumented]`.

**Table 1A — Tier Inventory**

| Tier ID | Tier Name | Enforcing Component | Scope | Limit Value [Source Ref] | Binding? |
|---------|-----------|--------------------|----|---|---|
| T1 | | | | | |
| T2 | | | | | |

Rules: minimum 2 rows; exactly 1 row with Binding? = Y; every Limit Value cites a Table 0A entry or is `[undocumented]`.

**Table 1B — Binding Constraint Exclusivity**

| Item | Content |
|------|---------|
| Primary binding tier (ID and name) | |
| Causal mechanism (why it fails before others) | |
| At least one non-binding tier (ID and name) | |
| Mechanism preventing it from failing first | |

`PHASE 1 COMPLETE — [N] tiers inventoried. Binding constraint: [Tier ID]. Proceeding to Phase 2.`

---

### PHASE 2 — Propagation and Impact Analysis (Flow Architect + UX Advocate)

May only reference tiers from Table 1A. If a new tier must be introduced, insert an amendment row in Table 1A with a source register citation before continuing.

**Table 2A — Backpressure Propagation Trace** *(Flow Architect)*

Minimum 2 hops from the binding tier.

| Hop | From Component | To Component | Mechanism | Observable Effect at Target |
|-----|---------------|-------------|-----------|---------------------------|
| 1 | | | | |
| 2 | | | | |

**Table 2B — User Experience Per Tier** *(UX Advocate)*

One row per tier from Table 1A. No omissions.

| Tier ID | UX Signal Type | User-Visible Symptom | Error Code / Message | Retry Guidance Shown? | Recovery Path |
|---------|---------------|---------------------|----------------------|----------------------|---------------|
| T1 | | | | | |
| T2 | | | | | |

**Table 2C — Unprotected Burst Paths** *(Flow Architect)*

| Path ID | Burst Trigger | Why Throttle Doesn't Intercept | First Observable Symptom |
|---------|-------------|-------------------------------|--------------------------|
| B1 | | | |

**Table 2D — Cascading Throttle Failure Scenarios** *(Flow Architect)*

| Scenario | Tier A | Trigger Mechanism | Tier B | Cascade Mechanism | Combined User Impact |
|----------|--------|------------------|--------|------------------|----------------------|
| | | | | | |

`PHASE 2 COMPLETE — propagation traced [N] hops; UX for [N] tiers; [N] burst paths; [N] cascades. Proceeding to Phase 3.`

---

### PHASE 3 — Gap Analysis and Synthesis (Risk Analyst)

Must address every tier and gap surfaced in Phases 1–2. No new tiers may be introduced.

**Table 3A — Retry-After Handling Assessment**

| Caller | Throttle Signal Source (Tier ID) | Reads Retry-After? | Honors Backoff? | Verdict | Retry Storm Risk if FAIL |
|--------|--------------------------------|-------------------|----------------|---------|--------------------------|
| | | | | PASS/FAIL/UNKNOWN | |

**Table 3B — Mitigation Recommendations**

| Gap Addressed (from 2C, 2D, or 3A) | Mitigation | Explicit Tradeoff |
|-------------------------------------|-----------|-------------------|
| | | |
| | | |

Minimum 2 rows. A mitigation row without a tradeoff is incomplete.

**Table 3C — Severity Ranking**

| Rank | Risk Name | Severity | Impact Frequency | Blast Radius | Justification |
|------|-----------|----------|-----------------|-------------|---------------|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |

**Table 3D — Coverage Self-Verification**

| Criterion | Phase / Table | Complete? | Gap |
|-----------|--------------|-----------|-----|
| Source register before first tier | Phase 0, Table 0A | | |
| Primary bottleneck with causal reason | Phase 1, Tables 1A–1B | | |
| Binding exclusivity with contrastive reasoning | Phase 1, Table 1B | | |
| ≥ 2 tiers with enforcing component and scope | Phase 1, Table 1A | | |
| Backpressure propagation ≥ 2 hops with mechanism | Phase 2, Table 2A | | |
| UX for every named tier | Phase 2, Table 2B | | |
| Unprotected burst path | Phase 2, Table 2C | | |
| Cascading failure scenario | Phase 2, Table 2D | | |
| Retry-after evaluated per caller | Phase 3, Table 3A | | |
| Quantified threshold with source citation | Phase 1, Table 1A | | |
| ≥ 2 mitigations with tradeoffs | Phase 3, Table 3B | | |
| ≥ 3 risks ranked with justification | Phase 3, Table 3C | | |

Self-reported gaps earn partial credit. A criterion absent from both the body tables and this table scores FAIL.

`PHASE 3 COMPLETE — [N]/12 criteria fully addressed, [N] partial, [N] gaps.`

---

## Variation Comparison

| Property | V-01 | V-02 | V-03 | V-04 | V-05 |
|----------|------|------|------|------|------|
| Role execution order | Expert → Architect → UX → Risk | Single role | Single role | Single role | Expert → Architect/UX → Risk |
| Output format | Mixed prose + tables | All tables | Mixed prose + tables | Prose/Q&A | All tables |
| Phase gates | Implicit (role order) | None | Explicit with abort | None | Explicit with abort |
| Source commitment | Explicit pre-analysis register | Table Section 1 | Phase 0 abort gate | Evidence ledger (conversational) | Phase 0 abort gate + table |
| Binding exclusivity | Dedicated sub-section | Table 3 | Phase 1B deliverable | Q1 follow-up | Table 1B |
| UX coverage mechanism | Role 3 mandate (no omissions) | Table with per-tier rows | Phase 2B mandate | Per-tier question framing | Table 2B (no omissions) |
| Self-verification | Mandatory closing table | Section 11 table | Phase 3D table | Closing checklist (prose) | Table 3D |
| Estimated prompt length | Medium | Medium-long | Long | Medium | Long |
| Primary failure mode addressed | Retroactive citation | Coverage gaps | Phase-skip + retroactive citation | UX generalization | All three simultaneously |
