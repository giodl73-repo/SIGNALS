Written to `simulations/quest/variations/flow-throttle-variations-R3-2026-03-14.md`.

---

## Round 3 Variations — Summary

| V | Axis | Base | Key mechanism |
|---|------|------|---------------|
| **V-01** | C-14 isolation | V-02 R2 (prose, no gates) | Three named conditional gates with explicit "Block: STEP X is blocked" language added to a gate-free imperative base |
| **V-02** | C-15 isolation | V-03 R2 (five tables, C-14/C-16 pass) | One non-deference sentence prepended to Round 2 header — "Do not assume Round 1 was accurate because it was confident. Treat Round 1's accepted construct names as unverified." |
| **V-03** | C-16 isolation | V-04 R2 (role sequence, C-14/C-15 pass) | Explicit scope declaration in ROLE 2.1 naming three construct populations (tier-map, propagation, cascade) with structural justification for why ROLE 1's scope window excluded them |
| **V-04** | C-15 + C-16 | Fresh two-role design | Both independence assertion and scope boundary stated in a single ROLE 2 preamble block |
| **V-05** | Full synthesis | V-05 R2 + all three | Conditional gate language tightened (C-14), non-deference added to PHASE 4.A (C-15), scope inheritance declaration added to PHASE 4.A (C-16) |

**Key discriminators:**
- **V-01** is diagnostic — expected ~101. It confirms C-14 gate syntax works but inherits V-02 R2's C-12 FAIL and C-05 PARTIAL.
- **V-02** and **V-03** are the minimum-mechanism ceiling tests — both predicted **118** by adding one sentence to a base that already passes the other two new criteria.
- **V-04** tests whether C-15 + C-16 co-located in one block score as two criteria (predicted 117, C-12 PARTIAL from prose backpressure).
- **V-05** is ceiling confirmation — expected **118**.
ccepted construct names as unverified." — added to V-03 R2. V-03 R2 already passes C-14 and C-16 as the generating source for those criteria. If V-02 scores C-15 = PASS and reaches 118, the single sentence is sufficient and no structural redesign is required.

- **C-16 scope isolation (V-03):** V-04 R2 already passes C-14 (role-boundary gates as source) and C-15 ("do not assume ROLE 1 was accurate because it was confident"). The one addition is a scope declaration in ROLE 2.1 naming three construct populations and explaining why ROLE 1's scope window excluded them. If V-03 scores C-16 = PASS and reaches 118, the scope naming alone closes the criterion.

- **C-15 + C-16 co-location (V-04):** Both criteria are properties of a well-specified second barrier and should compose naturally. Co-stating them tests whether an evaluator treats them as one criterion or two. Fresh two-role design also removes V-04 R2's (?) flagging convention, which introduced uncertainty-delegation complexity that may have suppressed remediation depth (C-10).

- **Predicted 118:** V-02 and V-03 each add one mechanism to a base that already scores 109 on v2 criteria plus the other two new criteria. Both should hit 118 if the mechanism is sufficient. V-05 full synthesis is the redundant ceiling confirmation.

---

## V-01 — Single-axis: Named Phase Gate Enforcement

**Variation axis:** C-14 mechanism
**Hypothesis:** Three named conditional gates — one at each phase boundary (setup-to-analysis, analysis-to-cascade, cascade-to-quantification) — added to V-02 R2's prose-imperative base satisfy C-14's requirement for an explicit prerequisite and a named blocked section. Tests whether gate syntax satisfies C-14 independently of tabular structure or role separation.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across the rate-limited system described in this scenario.

**Scenario:** [Insert scenario here]

**Domain rule:** All constructs must use exact Power Automate and Connectors terminology. Valid constructs: Power Platform request entitlements, connector throttling policies, flow run concurrency limits, action call limits, premium vs. standard connector tiers, Microsoft 365 service protection limits. Generic HTTP 429 without a PA construct name does not count.

**Core task:** Surface the binding bottleneck, trace how limits cascade, characterize user experience at each tier, and identify hidden burst paths and retry-after gaps. This analysis will inform a go/no-go decision on the flow design.

**The inertia assumption under test:** Most flow developers assume rate limits are independent — that saturating one tier has no effect on others. This scenario may invalidate that assumption. Your bottleneck and cascade sections must either confirm or refute it.

---

### STEP 1 — SCENARIO SETUP

Map all rate-limiting components and their numeric limits:

| Component | PA construct (exact) | Limit (req/unit-time) | Volume contribution |
|-----------|---------------------|-----------------------|---------------------|
| | | | |

Aggregate scenario request volume: **[N req/unit-time]**

---

**GATE 1 — prerequisite:** Every row in the component table has (a) a named PA construct using exact PA/Connectors terminology — not a generic API description, (b) a numeric limit with unit of time, and (c) a volume contribution value. Block: STEP 2 is blocked until this condition is met. If any row is incomplete, complete it now before proceeding.

---

### STEP 2 — BOTTLENECK DECLARATION AND INERTIA SEED

Write exactly:
> "[Specific component name] at [PA construct] is the binding bottleneck. It saturates at [N req/unit-time] under this scenario because [reason this aggregate volume exceeds this tier first]. **[INERTIA-SEED]:** The developer assumption that [name the independence or additive assumption commonly made about these limits] fails here because [one sentence explaining why this scenario's topology or volume invalidates that assumption]."

The `[INERTIA-SEED]` label marks the naive assumption this cascade will resolve. You will reference it by label in STEP 7. An analysis where STEP 7 does not cite [INERTIA-SEED] by name is incomplete.

---

### STEP 3 — RATE LIMIT HIT ORDERING

Present throttle tiers in explicit hit order, with explanation:

> "Tier 1 (bottleneck): [component] — [PA construct] — [limit] — hits first because [reason at scenario volume]"
> "Tier 2: [component] — [PA construct] — [limit] — hits second because [why it saturates after Tier 1 at this volume]"
> (Continue for all tiers.)

Rule: Each tier entry must explain why it hits at that position given the aggregate request volume. A list of limits without ordering rationale does not pass.

---

### STEP 4 — BACKPRESSURE TRACE

Trace how throttling at Tier 1 propagates, hop by hop:
> "Hop 1: [Component A] emits [signal type: error code / header / queue signal] → [Component B] receives it and responds by: [specific behavior]"
> "Hop 2: [Component B] emits [...] → [Component C] responds by: [...]"
> Continue until reaching the caller or terminal state.

---

### STEP 5 — USER EXPERIENCE MAP

For each throttle tier, state what the user sees or experiences — not what the system does internally:

> "Tier 1: User experiences: [specific description] — UX category: [transparent retry / visible delay / error surfaced / silent data loss]"
> "Tier 2: User experiences: [specific description — must differ from Tier 1] — UX category: [must differ from Tier 1 category]"

---

### STEP 6 — BURST PATH AND RETRY-AFTER ASSESSMENT

**Burst paths:**
For each flow construct that can emit an unbounded burst without a rate-limiting guard:
> "Burst: [Construct name] — Location: [in flow] — Peak rate: [N req/unit-time] — Why it bypasses the tier-1 guard: [reason specific to this scenario]"

If none: "No burst paths. Guards in place: [list]."

**Retry-After gaps:**
For each consumer that receives a 429 from a throttled tier:
> "Consumer: [name] — 429 from: [tier/component] — Retry-After header read?: [yes / no / N/A] — Current behavior: [what it does] — Consequence: [hammering / premature retry / extended outage / none]"

---

**GATE 2 — prerequisite:** (a) Bottleneck statement in STEP 2 is complete with the [INERTIA-SEED] sentence present, (b) all Tier entries in STEP 3 include the "hits at this position because" clause, (c) at least one complete hop is traced in STEP 4, (d) at least two throttle tiers are mapped to distinct UX categories in STEP 5. Block: STEP 7 is blocked until all four conditions are met.

---

### STEP 7 — CASCADE FAILURE TRACE (resolves [INERTIA-SEED])

Begin this section with:
> "The [INERTIA-SEED] assumption breaks here: [one sentence showing how the cascade proves the naive assumption false — naming the coupling mechanism between tiers]."

Then trace the cascade:
> "Cascade: [Tier 1 component] throttles → [causal mechanism: retry storm / queue buildup / shared principal pool depletion / other] → [Tier 2 component] exceeds its own limit → Failure mode: [brownout / full stop / partial data] — Load added to Tier 2: [estimate] — Duration: [bound or estimate]"

Rule: This section must reference `[INERTIA-SEED]` by restating the broken assumption from STEP 2. A cascade section that introduces a new independent finding without connecting to the STEP 2 framing does not satisfy this section's requirement. The cascade is the proof that the INERTIA-SEED assumption fails — not a separate observation.

---

**GATE 3 — prerequisite:** The cascade trace in STEP 7 is complete: a causal chain from Tier 1 to Tier 2 is present, a failure mode is named, and `[INERTIA-SEED]` is cited by label with the broken assumption restated. Block: STEP 8 is blocked until this condition is met.

---

### STEP 8 — QUANTIFIED RISK REGISTER

For each tier, compute whether the scenario volume is safe:

| Tier | PA construct | Limit | Projected scenario volume | Status (SAFE / MARGINAL / OVER-LIMIT) | Headroom (+) or deficit (-) |
|------|-------------|-------|--------------------------|---------------------------------------|------------------------------|
| | | | | | |

Status must be derived from the numeric comparison — not estimated qualitatively.

---

### STEP 9 — PA-SPECIFIC REMEDIATIONS

At least two. Each must name an exact PA feature or setting. "Add retries" and "reduce load" do not count.

| Finding addressed (cite STEP) | PA feature (exact name) | How to configure | Expected effect |
|-------------------------------|------------------------|-----------------|-----------------|
| | | | |
| | | | |

**PA construct review:** For each PA construct used in STEPS 1–9, write one line:
> "[Construct name] — confirmed / corrected to: [X] — reason: [one sentence on why this is the correct PA construct]"

One line per construct. Batch confirmation ("all constructs are correct") does not satisfy this step.

---

## V-02 — Single-axis: Validator Independence Assertion

**Variation axis:** C-15 mechanism
**Hypothesis:** A single non-deference imperative prepended to Round 2's validation header — "Do not assume Round 1 was accurate because it was confident. Treat Round 1's accepted construct names as unverified." — satisfies C-15 without any other structural change. Base is V-03 R2 (five tables, GATE 1, Round 1/Round 2 with scope declaration), which already passes C-14 and C-16. Tests whether the minimum instruction is one sentence.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across the rate-limited system described in this scenario. All comparative, ordered, or enumerated analysis must appear in the pre-printed tables below — tables enforce column-level precision that prose cannot.

**Scenario:** [Insert scenario here]

**Domain rule:** Every construct name must be exact Power Automate or Connectors terminology. Valid constructs: Power Platform request entitlements, connector throttling policies, flow run concurrency limits, action call limits, premium vs. standard connector tiers, Microsoft 365 service protection limits. Generic HTTP 429 without a PA construct name does not count.

**Output structure:** Six required analysis tables plus supporting sections. Every pre-printed table row must be completed or explicitly marked "None identified." Partial rows do not pass.

---

### TABLE 1 — THROTTLE TIER MAP

| Tier | Component | PA construct (exact) | Limit (req/unit-time) | Consumer(s) | Retry-After published? |
|------|-----------|---------------------|-----------------------|-------------|------------------------|
| 1 (bottleneck) | | | | | |
| 2 | | | | | |
| 3 (if applicable) | | | | | |

Aggregate scenario request volume: **[N req/unit-time]**

**Bottleneck statement (complete before TABLE 2):**
> "[Component] at [PA construct] is the binding bottleneck. It saturates at [N req/unit-time] under this scenario. The naive assumption that tier limits are independent fails here because [one sentence linking to cascade mechanism or shared principal pool]."

**PA validation — Round 1 (first barrier):** For each construct in TABLE 1, write one line:
> "[Construct name] — confirmed / corrected to: [X] — because: [one sentence]"

**GATE 1:** All TABLE 1 rows have PA constructs, numeric limits, and Round 1 validation lines. Proceed only when satisfied. This gate blocks TABLE 2. This gate catches missing constructs; Round 2 (after TABLE 5) catches imprecise ones.

---

### TABLE 2 — RATE LIMIT HIT ORDERING

| Hit order | Tier | Component | PA construct | Limit | Scenario projected volume | Why this order holds at scenario volume |
|-----------|------|-----------|-------------|-------|--------------------------|------------------------------------------|
| 1 (bottleneck) | | | | | | |
| 2 | | | | | | |

Rule: "Why this order holds" must explain the ordering at aggregate volume — not just reproduce the limits in ascending order. Unordered enumeration does not pass this table.

---

### TABLE 3 — BACKPRESSURE HOP CHAIN

| Hop | From component | Signal emitted | Signal type | To component | Response behavior |
|-----|---------------|----------------|-------------|--------------|-------------------|
| 1 | | | error code / retry-after header / queue depth / other | | |
| 2 | | | | | |

Continue rows until reaching the caller or terminal state.

---

### TABLE 4 — BURST PATH ENUMERATION

| Path | PA flow construct (exact) | Location in flow | Estimated peak rate (req/unit-time) | Why it bypasses or overwhelms the tier-1 guard |
|------|--------------------------|-----------------|--------------------------------------|------------------------------------------------|
| | | | | |

If none: write "None identified. Guards in place:" in the first cell and list guards across the remaining cells.

---

### TABLE 5 — CASCADE SEQUENCE

| Step | Component | Action | Causal mechanism | Load added to next tier (estimate) | Failure mode | Duration |
|------|-----------|--------|-----------------|-------------------------------------|--------------|----------|
| 1 | | throttles | | | brownout / full stop / partial data | |
| 2 | | throttles (cascade) | | | | |

**Cascade resolution statement (required):** "The cascade above resolves the naive assumption from the bottleneck statement because [one sentence showing how the causal chain proves the assumption false]."

**GATE 3:** Steps 1 and 2 must be filled and the cascade resolution statement present before proceeding.

---

### USER EXPERIENCE MAP (section, not table)

For each tier in TABLE 1:
> "Tier [N]: User sees/experiences: [specific description] — UX category: [transparent retry / visible delay / error surfaced to user / silent data loss]"

Rule: Categories must differ across tiers. Repeating the same category does not pass.

---

### RETRY-AFTER GAPS (section)

For each consumer in TABLE 1 where Retry-After is published:
> "Consumer: [name] — Current behavior: [what it does on 429] — Retry-After header read?: [yes / no] — Consequence: [hammering / premature retry / extended outage / none]"

---

### TABLE 6 — QUANTIFIED RISK REGISTER

| Tier | PA construct | Limit | Projected scenario volume | Status (SAFE / MARGINAL / OVER-LIMIT) | Headroom (+) or deficit (-) |
|------|-------------|-------|--------------------------|---------------------------------------|------------------------------|
| | | | | | |

All tiers from TABLE 1 must appear. Status derived from numeric comparison.

---

### PA-SPECIFIC REMEDIATIONS

At least two. Each must name an exact PA feature or setting. "Add retries" and "reduce load" do not count.

| Finding addressed (cite TABLE/section) | PA feature (exact name) | Configuration | Effect |
|----------------------------------------|------------------------|---------------|--------|
| | | | |
| | | | |

---

**PA validation — Round 2 (second barrier — construct precision):** Do not assume Round 1 was accurate because constructs appeared to validate without correction. Round 1's confidence is not evidence of Round 1's precision. Treat Round 1's accepted construct names as unverified at the start of this review.

After completing remediations, review all PA constructs used in this output. Write one line per construct:
> "[Construct] — confirmed / corrected to: [X] — reason: [one sentence]"

This is not optional. Batch confirmation does not count. Round 2 is specifically looking for constructs introduced in the TABLES 3–5 analysis that were not reviewed in Round 1, which only covered TABLE 1 constructs. Those post-tier constructs were introduced after Round 1's execution window and require independent review here.

---

## V-03 — Single-axis: Barrier Scope Inheritance Boundary

**Variation axis:** C-16 mechanism
**Hypothesis:** An explicit scope declaration added to ROLE 2.1 — naming three construct populations new to ROLE 2's scope window and stating the structural reason ROLE 1 could not have covered them — satisfies C-16 without any other change to V-04 R2. Base is V-04 R2, which already passes C-14 (role-boundary gate as source) and C-15 ("do not assume ROLE 1 was accurate because it was confident"). Tests whether scope naming alone closes the criterion when independence assertion is already in place.

---

Two roles execute this simulation sequentially. ROLE 1 (Connectors throughput expert) builds the technical analysis. ROLE 2 (Power Automate platform expert) validates domain accuracy, fills UX and retry-after detail, and produces remediations. ROLE 2 is the second barrier — ROLE 1's construct choices are the first pass; ROLE 2's validation table is the second. Neither role alone is sufficient.

**Scenario:** [Insert scenario here]

---

## ROLE 1 — CONNECTORS THROUGHPUT EXPERT

**Domain rule:** All tier names, limits, and constructs must use exact Connectors/PA terminology. Flag any construct you are uncertain about with (?) for ROLE 2 to correct. ROLE 2 will validate every construct you produce — do not rely on it to catch everything; flag your uncertainties explicitly.

### 1.1 — SCENARIO SETUP

Map all rate-limiting components. Identify aggregate scenario request volume.

| Component | Tier | PA construct (exact, or flag with ?) | Limit (req/unit-time) | Volume contribution |
|-----------|------|---------------------------------------|----------------------|---------------------|
| | | | | |

Aggregate scenario request volume: **[N req/unit-time]**

**GATE 1:** All rows have a named PA construct (or ? flag), numeric limit, and volume contribution. ROLE 1.2 is blocked until this condition is met.

### 1.2 — BOTTLENECK DECLARATION AND INERTIA SEED

Write the bottleneck statement:
> "[Specific component name] saturates first at [N req/unit-time] under this scenario. It is the binding constraint because [one sentence on why this aggregate volume exceeds this tier first]. **[INERTIA-SEED]:** The developer assumption that [name the independence or additive assumption commonly made] fails here because [one sentence on why this scenario's topology or volume breaks that assumption]."

Then order the tiers:
> "Tier 1 (bottleneck): [component] — [PA construct] — limit: [N] — saturates first because [reason at scenario volume]"
> "Tier 2: [component] — [PA construct] — limit: [N] — hits second because [reason]"
> (Continue for all tiers.)

| Hit order | Tier | Component | PA construct | Limit | Why this order holds at scenario volume |
|-----------|------|-----------|-------------|-------|-----------------------------------------|
| 1 (bottleneck) | | | | | |
| 2 | | | | | |

### 1.3 — BACKPRESSURE PROPAGATION

Trace from Tier 1 outward, hop by hop:
> "Hop 1: [Bottleneck component] emits [signal type: error code / header / queue signal] → [Receiving component] responds by: [specific behavior]"
> Continue until terminal state.

### 1.4 — UNPROTECTED BURST PATHS

For each flow construct that emits a burst without a guard:
> "Burst: [Construct name] — Location: [in flow] — Peak rate: [N req/unit-time] — Why it bypasses the tier-1 guard: [reason specific to this scenario]"

| Path | PA construct (exact) | Location | Peak rate | Why it bypasses tier-1 guard |
|------|---------------------|---------|-----------|------------------------------|
| | | | | |

If none: "No burst paths. Guards in place: [list]."

### 1.5 — CASCADE FAILURE TRACE (resolves [INERTIA-SEED])

Begin:
> "The [INERTIA-SEED] assumption breaks: [one sentence showing the causal link between bottleneck and cascade — naming the mechanism that couples the tiers]."

Then trace the cascade:

| Cascade step | Component | Action | Causal mechanism | Load added to next tier | Failure mode | Duration |
|-------------|-----------|--------|-----------------|-------------------------|--------------|----------|
| 1 | | throttles | | | | |
| 2 | | throttles (cascade) | | | | |

Cascade narrative:
> "Cascade: [Tier 1 component] throttles → [causal mechanism] → [Tier 2 component] exceeds its own limit → Failure mode: [brownout / full stop / partial data] — Duration: [bound]."

Rule: This section must restate the [INERTIA-SEED] assumption from 1.2 and show how the cascade proves it false. A cascade section that does not reference [INERTIA-SEED] by label is incomplete.

---

## ROLE 2 — POWER AUTOMATE PLATFORM EXPERT

You are reviewing ROLE 1's output for PA construct accuracy and producing the platform-specific analysis. Your validation table is the **second barrier**: ROLE 1's self-reporting (including (?) flags) is the first. A construct may be present and plausible in ROLE 1 but imprecise from a PA platform perspective — your job is to catch that.

### 2.1 — PA CONSTRUCT VALIDATION (Second barrier)

**Independence requirement:** If ROLE 1 had zero (?) flags, confirm each construct explicitly and explain why it is correct — do not assume ROLE 1 was accurate because it was confident. The second barrier is independent of ROLE 1's confidence.

**Scope declaration:** Your validation covers three construct populations that ROLE 1 could not fully validate. ROLE 1's constructs were defined in two phases: tier-mapping (section 1.1) and bottleneck ordering (section 1.2). Those phases closed before ROLE 1 executed propagation (1.3), burst-path (1.4), and cascade (1.5) analysis, which introduced new construct references — propagation signal types, burst construct names, and cascade mechanism labels — after ROLE 1's construct-definition window had already closed. This review covers: (a) tier-map and hit-ordering constructs from sections 1.1–1.2 — re-validate independently of ROLE 1's confidence, (b) propagation signal types and protocol names introduced in section 1.3 — outside ROLE 1's definition scope, and (c) cascade mechanism labels and failure-mode constructs introduced in section 1.5 — also outside ROLE 1's definition scope. Do not treat populations (b) and (c) as reviewed by ROLE 1 — they were not present within ROLE 1's scope window.

Review every construct named in ROLE 1. Do not batch-confirm. For each:

| ROLE 1 construct name (as written) | Source (section) | Confirmed or corrected | Exact PA construct name | Why this is correct in PA runtime context |
|-------------------------------------|-----------------|----------------------|-------------------------|-------------------------------------------|
| | | confirmed / corrected to: | | |

### 2.2 — USER EXPERIENCE PER THROTTLE TIER

From the PA runtime perspective:

| Tier | PA runtime behavior on throttle | User-visible experience (specific) | UX category |
|------|--------------------------------|------------------------------------|-------------|
| Tier 1 | | | transparent retry / visible delay / error surfaced / silent data loss |
| Tier 2 | | | (must differ from Tier 1) |

### 2.3 — RETRY-AFTER GAP ASSESSMENT

For each consumer that receives a 429 from any throttled tier:

| Consumer | PA retry mechanism in use | 429 from which tier | Retry-After header read? | Gap identified | Consequence |
|----------|--------------------------|---------------------|--------------------------|----------------|-------------|
| | | | yes / no / N/A | | hammering / premature retry / extended outage / none |

### 2.4 — QUANTIFIED RISK REGISTER

Use validated construct names from 2.1:

| Tier | PA construct (validated) | Limit | Projected scenario volume | Status (SAFE / MARGINAL / OVER-LIMIT) | Headroom (+) or deficit (-) |
|------|-------------------------|-------|--------------------------|---------------------------------------|------------------------------|
| | | | | | |

### 2.5 — PA-SPECIFIC REMEDIATIONS

At least two. Each must name an exact PA feature or setting. "Add retries" and "reduce load" do not count.

| Finding addressed (cite ROLE 1 section) | PA feature (exact name) | Configuration detail | Effect on finding |
|------------------------------------------|------------------------|----------------------|-------------------|
| | | | |
| | | | |

**Autonomy note:** ROLE 2 may identify additional remediations beyond what ROLE 1 surfaced, particularly from PA-platform-specific controls not visible in a Connectors-domain view: per-connection entitlements, environment-level request allocation, service principal pooling, premium connector tier upgrades, or M365 service protection exemption requests. If identified, add rows.

---

## V-04 — Combination: C-15 + C-16 (Validator Independence + Scope Inheritance)

**Variation axis:** C-15 + C-16 together in a two-role second-barrier preamble
**Hypothesis:** C-15 and C-16 are complementary properties of a well-specified second barrier and compose naturally in a single preamble block. Stating them together tests whether co-location causes an evaluator to treat them as one criterion or two. A fresh two-role design (no (?) flagging convention) also removes V-04 R2's uncertainty-delegation complexity that may have suppressed remediation depth. A named GATE 1 satisfies C-14.

---

Two roles execute this analysis sequentially.

**ROLE 1** (Connectors throughput analyst): builds the technical analysis — tier map, bottleneck, propagation chain, burst paths, cascade failure.
**ROLE 2** (Power Automate platform expert): independently validates all PA domain accuracy and produces platform-grounded UX, retry-after assessment, risk quantification, and remediations.

**Scenario:** [Insert scenario here]

**Domain rule:** Every PA construct name must be exact. Valid constructs: Power Platform request entitlements, connector throttling policies, flow run concurrency limits, action call limits, premium vs. standard connector tiers, Microsoft 365 service protection limits. Generic HTTP 429 without a PA construct name does not count.

---

## ROLE 1 — CONNECTORS THROUGHPUT ANALYST

### 1.1 — COMPONENT MAP AND RATE LIMIT INVENTORY

Identify all rate-limiting components. State aggregate scenario request volume.

| Component | PA construct (exact) | Limit (req/unit-time) | Volume contribution | Retry-After published? (yes/no/N/A) |
|-----------|---------------------|-----------------------|---------------------|--------------------------------------|
| | | | | |

Aggregate scenario request volume: **[N req/unit-time]**

**GATE 1:** All rows have a named PA construct, a numeric limit with unit, and a volume contribution. Proceed to ROLE 1.2 only when this condition is met. ROLE 1.2 is blocked until GATE 1 is satisfied.

### 1.2 — BOTTLENECK DECLARATION AND INERTIA SEED

Write the bottleneck statement:
> "[Specific component name] at [PA construct] is the binding bottleneck. It saturates at [N req/unit-time] under this scenario because [reason the aggregate volume exceeds this tier first]. **[INERTIA-SEED]:** The developer assumption that [name the naive independence or additive assumption] fails here because [one sentence on why this topology or volume invalidates it]."

Order all tiers in hit sequence:

| Hit order | Tier | Component | PA construct | Limit | Why this order holds at scenario volume |
|-----------|------|-----------|-------------|-------|-----------------------------------------|
| 1 (bottleneck) | | | | | |
| 2 | | | | | |

Rule: "Why this order holds" must explain the ordering at aggregate volume — not simply reproduce limits in ascending order.

### 1.3 — BACKPRESSURE PROPAGATION CHAIN

Trace from Tier 1 to caller or terminal state, hop by hop:

| Hop | From component | Signal emitted | Signal type (error code / retry-after header / queue depth / other) | To component | Response behavior |
|-----|---------------|----------------|---------------------------------------------------------------------|--------------|-------------------|
| 1 | | | | | |
| 2 | | | | | |

### 1.4 — BURST PATH IDENTIFICATION

For each flow construct that can emit a burst without a rate-limiting guard:

| Path | PA flow construct (exact) | Location in flow | Estimated peak rate (req/unit-time) | Why it bypasses or overwhelms the tier-1 guard |
|------|--------------------------|-----------------|--------------------------------------|------------------------------------------------|
| | | | | |

If none: write "None identified" in the first cell; list guards in effect in the remaining cells.

### 1.5 — CASCADE FAILURE TRACE (resolves [INERTIA-SEED])

Open this section with:
> "The [INERTIA-SEED] assumption breaks here: [one sentence showing how this cascade proves the naive assumption false — naming the mechanism that couples the tiers]."

Trace the cascade:

| Cascade step | Component | Action | Causal mechanism | Load added to next tier (estimate) | Failure mode | Duration |
|-------------|-----------|--------|-----------------|-------------------------------------|--------------|----------|
| 1 | | throttles | | | brownout / full stop / partial data | |
| 2 | | throttles (cascade) | | | | |

Rule: This section must cite [INERTIA-SEED] by label and restate the broken assumption from 1.2. A cascade section that introduces an independent finding without connecting to [INERTIA-SEED] is incomplete.

---

## ROLE 2 — POWER AUTOMATE PLATFORM EXPERT

**Second-barrier preamble:**

**Independence (C-15):** Treat all ROLE 1 construct names as unverified at the start of this role. Do not assume ROLE 1 was accurate because it named constructs without flagging uncertainty. ROLE 1's confidence is not evidence of ROLE 1's precision — a construct can be plausible in the Connectors domain yet imprecise from a PA runtime platform perspective. Your validation is independent of ROLE 1's self-assessment.

**Scope extension (C-16):** Your validation scope covers construct categories that ROLE 1 could not have reviewed. ROLE 1's constructs were established during two phases: the tier-map phase (section 1.1) and the bottleneck/hit-ordering phase (section 1.2). These phases closed before ROLE 1 performed propagation (1.3), burst-path (1.4), or cascade (1.5) analysis, which introduced new construct references — propagation signal types, burst construct names, cascade mechanism labels — that fall outside ROLE 1's construct-definition window by construction. This role covers all three populations: (a) tier-map and hit-ordering constructs from sections 1.1–1.2 — re-validate independently of ROLE 1's confidence, (b) propagation signal types and protocol names introduced in section 1.3 — not in scope for ROLE 1, and (c) cascade mechanism labels introduced in section 1.5 — also not in scope for ROLE 1. Do not treat populations (b) and (c) as reviewed — they were not.

### 2.1 — PA CONSTRUCT VALIDATION (Second barrier)

Review all constructs from ROLE 1 sections 1.1–1.5. Per-construct review required. Do not batch-confirm.

| ROLE 1 construct name (as written) | Source (section) | Confirmed or corrected | Exact PA construct name | Why this is correct in PA runtime context |
|-------------------------------------|-----------------|----------------------|-------------------------|-------------------------------------------|
| | | confirmed / corrected to: | | |

### 2.2 — USER EXPERIENCE PER THROTTLE TIER

| Tier | PA runtime behavior on throttle | User-visible experience (specific) | UX category |
|------|--------------------------------|------------------------------------|-------------|
| Tier 1 | | | transparent retry / visible delay / error surfaced / silent data loss |
| Tier 2 | | | (must differ from Tier 1) |

### 2.3 — RETRY-AFTER GAP ASSESSMENT

For each consumer that receives a 429:

| Consumer | PA retry mechanism in use | 429 from which tier | Retry-After header read? | Gap identified | Consequence |
|----------|--------------------------|---------------------|--------------------------|----------------|-------------|
| | | | yes / no / N/A | | hammering / premature retry / extended outage / none |

### 2.4 — QUANTIFIED RISK REGISTER

Use validated construct names from 2.1:

| Tier | PA construct (validated) | Limit | Projected scenario volume | Status (SAFE / MARGINAL / OVER-LIMIT) | Headroom (+) or deficit (-) |
|------|-------------------------|-------|--------------------------|---------------------------------------|------------------------------|
| | | | | | |

Status must be derived from the numeric comparison — not estimated qualitatively.

### 2.5 — PA-SPECIFIC REMEDIATIONS

At least two. Each must name an exact PA feature or setting. "Add retries" and "reduce load" do not count.

| Finding addressed (cite ROLE 1 section) | PA feature (exact name) | Configuration detail | Effect on finding |
|------------------------------------------|------------------------|----------------------|-------------------|
| | | | |
| | | | |

**Platform controls:** Beyond ROLE 1 findings, identify PA-platform-specific controls not surfaced from a Connectors-domain view: per-connection request entitlements, environment-level request allocation, service principal pooling, premium connector tier upgrades, M365 service protection exemption requests. If relevant, add rows.

---

## V-05 — Full Synthesis: All Three New Criteria Explicitly Embedded

**Variation axis:** V-05 R2 base + explicit C-14 conditional block language + C-15 non-deference in PHASE 4.A + C-16 scope inheritance declaration in PHASE 4.A
**Hypothesis:** All six structural criteria (C-11 through C-16) can be embedded in a single coherent prompt. The three additions to R2 V-05: (1) each GATE gains an explicit "Block: PHASE X is blocked" sentence, (2) PHASE 4.A opens with a non-deference imperative ("Do not assume GATE 1 was accurate because constructs passed presence check"), (3) PHASE 4.A names the construct categories introduced in PHASES 2–3 that GATE 1 could not have covered. Expected: 118/118.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across the rate-limited system described in this scenario. This simulation must surface: the binding bottleneck, ordered throttle tiers, backpressure propagation chain, user experience per tier, unprotected burst paths, retry-after gaps, cascade failure sequence, quantified risk register, and PA-specific remediations.

**Scenario:** [Insert scenario here]

**Structural requirements (all six must be satisfied):**
- **Two-barrier PA validation (C-11):** GATE 1 is the first barrier — it checks that PA constructs are present. PHASE 4.A is the second barrier — it checks that they are precise. Both must fire. An output that fires only one barrier does not satisfy C-11.
- **Five pre-printed analysis tables (C-12):** TABLE 1 (tier ordering), TABLE 2 (backpressure hops), TABLE 3 (burst paths), TABLE 4 (cascade sequence), TABLE 5 (risk register). Each table has columns that structurally enforce the hardest pass condition for its criterion.
- **Inertia-to-cascade causal thread (C-13):** PHASE 2.A requires a named `[INERTIA-SEED]` sentence. PHASE 3.C must cite `[INERTIA-SEED]` by label and resolve the broken assumption. C-01 and C-08 are logically connected by design.
- **Named phase gate enforcement (C-14):** Each GATE explicitly states a prerequisite condition and names the section it blocks. Section headings alone do not constitute gates.
- **Validator independence assertion (C-15):** PHASE 4.A opens with an explicit non-deference instruction directed at the evaluating agent. GATE 1's completeness is not evidence of precision.
- **Barrier scope inheritance boundary (C-16):** PHASE 4.A explicitly names which construct categories are new to its scope window that GATE 1 could not have covered, with the structural reason.

---

### PHASE 1 — SCENARIO SETUP AND FIRST PA BARRIER

**TABLE 0 — COMPONENT MAP**

| Component | PA construct (exact) | Limit (req/unit-time) | Consumer(s) | Retry-After published? (yes/no/N/A) |
|-----------|---------------------|-----------------------|-------------|--------------------------------------|
| | | | | |

Aggregate scenario request volume: **[N req/unit-time]**

**GATE 1 — First PA barrier (construct presence):**
Prerequisite: (a) every row has a named PA construct — not a generic API description, (b) every limit is numeric with unit, (c) every consumer is named.
Block: PHASE 2 is blocked until all three conditions are met. If any row is incomplete, complete it now.

GATE 1 catches **missing** PA constructs. It does not catch imprecise ones — that is PHASE 4.A's job. Do not conflate the two barriers.

---

### PHASE 2 — CORE ANALYSIS

**2.A — Bottleneck Declaration and Inertia Seed**

Write the bottleneck statement:
> "[Specific component name] at [PA construct] is the binding bottleneck. It saturates at [N req/unit-time] under this scenario because [reason the aggregate volume exceeds this tier first]. **[INERTIA-SEED]:** The developer assumption that [name the independence or additive assumption commonly made about these limits] fails here because [one sentence explaining why this scenario's topology or volume invalidates that assumption]."

The `[INERTIA-SEED]` label is required. It will be resolved in PHASE 3.C. An output where PHASE 3.C does not cite this label cannot satisfy C-13.

**TABLE 1 — RATE LIMIT HIT ORDERING**

| Hit order | Tier | Component | PA construct | Limit | Scenario projected volume | Why this order holds at scenario volume |
|-----------|------|-----------|-------------|-------|--------------------------|------------------------------------------|
| 1 (bottleneck) | | | | | | |
| 2 | | | | | | |

Rule: "Why this order holds" must explain the ordering at the scenario's aggregate volume — not simply list limits in ascending order. Unordered enumeration does not pass this table.

**2.B — Backpressure Propagation**

**TABLE 2 — BACKPRESSURE HOP CHAIN**

| Hop | From component | Signal emitted | Signal type (error code / retry-after header / queue depth / other) | To component | Response behavior |
|-----|---------------|----------------|---------------------------------------------------------------------|--------------|-------------------|
| 1 | | | | | |
| 2 | | | | | |

Continue until reaching the caller or terminal state.

**2.C — User Experience per Throttle Tier**

| Tier | What the system does internally | What the user sees or experiences (specific) | UX category |
|------|--------------------------------|---------------------------------------------|-------------|
| Tier 1 | | | transparent retry / visible delay / error surfaced / silent data loss |
| Tier 2 | | | (must differ from Tier 1) |

Rule: UX categories must differ across rows. Repeating the same category for all tiers does not pass.

**GATE 2:**
Prerequisite: (a) bottleneck statement complete with [INERTIA-SEED] sentence, (b) TABLE 1 "Why this order holds" populated for all rows, (c) TABLE 2 has at least one complete hop, (d) UX table has at least two tiers with distinct categories.
Block: PHASE 3 is blocked until all four conditions are met.

---

### PHASE 3 — FAILURE ANALYSIS

**3.A — Unprotected Burst Paths**

**TABLE 3 — BURST PATH ENUMERATION**

| Path | PA flow construct (exact) | Location in flow | Estimated peak rate (req/unit-time) | Why it bypasses or overwhelms the tier-1 guard |
|------|--------------------------|-----------------|--------------------------------------|------------------------------------------------|
| | | | | |

If no burst paths: write "None identified" in the first cell. List guards in the final cell: "Guards in place: [list each guard and the construct it protects]."

**3.B — Missing Retry-After Handling**

| Consumer | Action / connector call | Current retry behavior | Retry-After header read? | Consequence |
|----------|------------------------|------------------------|--------------------------|-------------|
| | | | yes / no / N/A | hammering / premature retry / extended outage / none |

**3.C — Cascading Throttle Failure (resolves [INERTIA-SEED])**

Begin:
> "The [INERTIA-SEED] assumption breaks here: [one sentence showing how the cascade proves the naive assumption false — naming the coupling mechanism that links the tiers]."

**TABLE 4 — CASCADE SEQUENCE**

| Step | Component | Action | Causal mechanism | Load added to next tier (estimate) | Failure mode | Duration |
|------|-----------|--------|-----------------|-------------------------------------|--------------|----------|
| 1 | | throttles | | | brownout / full stop / partial data | |
| 2 | | throttles (cascade) | | | | |

Rule: The cascade section must cite `[INERTIA-SEED]` by restating the broken assumption from PHASE 2.A. A cascade that introduces a new independent finding without connecting to the INERTIA-SEED framing does not satisfy C-13.

**GATE 3:**
Prerequisite: At least one complete cascade chain (Steps 1 and 2 filled, [INERTIA-SEED] cited and broken assumption restated) is present.
Block: PHASE 4 is blocked until this condition is met.

---

### PHASE 4 — QUANTIFICATION AND SECOND PA BARRIER

**4.A — PA Construct Validation (Second barrier — construct precision)**

**Independence:** Do not assume GATE 1 was accurate because all constructs passed the presence check. GATE 1's completeness is not evidence of precision. A construct that was present at GATE 1 may still be imprecise from a PA runtime perspective. Treat all construct names as unverified at the start of this section.

**Scope:** GATE 1 covered construct categories present at PHASE 1 execution time: tier component names and their initial PA construct assignments. This section covers construct categories introduced in PHASES 2–3 that did not exist within GATE 1's execution scope: (a) propagation signal types and protocol names introduced in TABLE 2 and PHASE 2.B, (b) cascade mechanism labels introduced in TABLE 4 and PHASE 3.C, and (c) construct references in the UX analysis (PHASE 2.C) and retry-after gaps (PHASE 3.B). GATE 1 could not have reviewed these categories because they were not present when GATE 1 executed.

Review every PA construct used in PHASES 1–3:

| PHASE/Section where used | Construct name as written | Confirmed or corrected | Exact PA construct name (if correction) | Why this is correct in PA runtime context |
|--------------------------|--------------------------|----------------------|-----------------------------------------|-------------------------------------------|
| | | confirmed / corrected to: | | |

Batch confirmation ("all constructs are correct") does not satisfy C-11 — each construct requires a per-construct review.

**4.B — User Experience Validation (PA runtime view)**

Review each UX tier from PHASE 2.C using PA platform perspective. Correct if PA runtime behavior differs from the connector-domain view:

| Tier | PHASE 2.C UX (original characterization) | PA runtime behavior (if different) | Revised UX (if applicable) |
|------|------------------------------------------|-------------------------------------|----------------------------|
| Tier 1 | | | |
| Tier 2 | | | |

**4.C — Quantified Risk Register**

**TABLE 5 — RISK REGISTER**

| Tier | PA construct (validated in 4.A) | Limit | Projected scenario volume | Status (SAFE / MARGINAL / OVER-LIMIT) | Headroom (+) or deficit (-) |
|------|--------------------------------|-------|--------------------------|---------------------------------------|------------------------------|
| | | | | | |

All tiers from PHASE 1 must appear. Status must be derived from the numeric comparison — not estimated.

**4.D — PA-Specific Remediations**

At least two. "Add retries" and "reduce load" do not count. Each must name an exact PA feature or setting.

| Finding addressed (cite PHASE/section) | PA feature (exact name) | Configuration detail | Effect on finding |
|----------------------------------------|------------------------|----------------------|-------------------|
| | | | |
| | | | |

**Inertia verdict (required):** In one sentence, state the consequence of not acting: "If the [INERTIA-SEED] assumption is left in place and these remediations are not applied, the result is: [specific outcome with volume threshold or timeline]."

---

## Predicted Scores (v3 rubric, max 118)

| V | C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | C-11 | C-12 | C-13 | C-14 | C-15 | C-16 | Total |
|---|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|-------|
| V-01 | 12 | 7.2 | 12 | 12 | 7.2 | 10 | 10 | 10 | 5 | 5 | 1.5 | 0 | 3 | 3 | 1.5 | 1.5 | **~101** |
| V-02 | 12 | 12 | 12 | 12 | 12 | 10 | 10 | 10 | 5 | 5 | 3 | 3 | 3 | 3 | 3 | 3 | **118** |
| V-03 | 12 | 12 | 12 | 12 | 12 | 10 | 10 | 10 | 5 | 5 | 3 | 3 | 3 | 3 | 3 | 3 | **118** |
| V-04 | 12 | 12 | 12 | 12 | 12 | 10 | 10 | 10 | 5 | 5 | 3 | 2.4 | 3 | 3 | 3 | 3 | **~117** |
| V-05 | 12 | 12 | 12 | 12 | 12 | 10 | 10 | 10 | 5 | 5 | 3 | 3 | 3 | 3 | 3 | 3 | **118** |

**Key bets:**

- **C-14 (V-01):** Three added GATE statements — each naming a conditional prerequisite and a blocked section — satisfy C-14. PASS predicted. V-01 inherits V-02 R2's other structural deficits: C-02 PARTIAL (prose ordering), C-05 PARTIAL (soft trailing PA check), C-11 PARTIAL (soft trailing check as second barrier), C-12 FAIL (only risk register in table form). These persist unchanged — V-01 is a diagnostic, not a production candidate.

- **C-15 (V-02):** One non-deference sentence prepended to Round 2 is the minimum instruction. Predicted PASS — imperative, directed at the evaluating agent ("do not assume Round 1 was accurate"), specific to the prior layer ("Round 1's confidence"), and present before any Round 2 content executes. V-03 R2 already passes C-14 (GATE 1/GATE 3 as source) and C-16 (scope declaration as source) — adding C-15 should produce 118.

- **C-16 (V-03):** Scope inheritance declaration in ROLE 2.1 names three construct populations (tier-map, propagation, cascade) with explicit structural justification ("outside ROLE 1's scope window by construction"). Predicted PASS. V-04 R2 already passes C-14 and C-15 — adding C-16 should produce 118.

- **C-15 + C-16 co-location (V-04):** Co-stating both in one preamble block tests whether an evaluator sees two distinct criteria. Predicted both PASS. C-12 predicted PARTIAL (2.4/3) — backpressure (section 1.3) uses prose, not a table, leaving only four of five eligible criteria in table form.

- **V-05 ceiling confirmation:** All six structural criteria named in "Structural requirements" block and embedded in each relevant section. PHASE 4.A carries both C-15 (non-deference sentence) and C-16 (scope declaration). Expected 118/118. Primary uncertainty: does "GATE 1's completeness is not evidence of precision" satisfy C-15's "specific to the prior layer" requirement when GATE 1 is not a named role?
