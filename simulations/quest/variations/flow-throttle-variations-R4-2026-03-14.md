Here are the Round 4 variations for `flow-throttle`.

---

## Round 4 Variations — Summary

| V | Axis | Key mechanism | Predicted score |
|---|------|---------------|-----------------|
| **V-01** | C-17 isolation | Named `SECOND BARRIER — PRE-EVALUATION HEADER` block placed before the validation table — labels the positional boundary explicitly | ~127 |
| **V-02** | C-18 isolation | Scope extension adds one structural closure sentence: "ROLE 1's definition window closed at section 1.2 completion, before 1.3–1.5 executed" | ~127 |
| **V-03** | C-19 isolation | Both C-15 and C-16 directives co-located in one ROLE 2 preamble, each with a distinct named label (`Independence:` / `Scope extension:`) | **130** |
| **V-04** | C-17 + C-18 + C-19 | Named `SECOND BARRIER — PRE-EVALUATION PREAMBLE` carries labeled pair before any evaluative output, includes closure reason | **130** |
| **V-05** | Full synthesis | R3 V-05 + `PRE-ANALYSIS ASSERTION` header in PHASE 4.A with labeled pair, closure reason, and prose-portable gates | **130** |

**Design logic for the new criteria:**

- **C-17** requires the non-deference sentence to be BEFORE the barrier's first evaluative output. V-01 and V-05 satisfy this via a named section that explicitly announces the positional boundary.
- **C-18** requires a structural REASON why the first barrier's window excluded those categories — not just naming categories. V-02/V-04/V-05 add: `"ROLE 1's definition window closed at section 1.2 completion — before 1.3–1.5 executed."` That sentence names the window boundary as a structural fact, not a preference.
- **C-19** requires distinct labels when two directives co-locate. V-03/V-04/V-05 use `Independence:` and `Scope extension:` as load-bearing labels — the evaluator must parse each as a separate mechanism.
- **C-20** is confirmed by prose portability — all gates carry (a) name, (b) conditional prerequisite, (c) `Block: SECTION is blocked` statement. No tabular structure required.

V-01 and V-02 are minimum-mechanism diagnostics (~127); V-03/V-04/V-05 are ceiling candidates (130). V-05 is the full-synthesis ceiling confirmation.
on sentence closes the criterion. C-17 passes from base placement; C-19 N/A. Predicted ~127.
- **V-03** is C-19 isolation — tests whether labels alone turn one-criterion co-location scoring into two-criterion scoring. C-17/C-18/C-20 all pass from base structure. Predicted **130**.
- **V-04** combination confirms C-17 + C-18 + C-19 compose in a single pre-barrier block. Predicted **130** if all three score independently.
- **V-05** is full-ceiling confirmation — all twenty criteria present at minimum sufficient mechanisms. Predicted **130/130**.

---

## V-01 — Single-axis: Pre-Barrier Independence Instruction Placement (C-17)

**Variation axis:** C-17 — pre-evaluation placement of the non-deference sentence
**Hypothesis:** The non-deference sentence satisfies C-15 when placed anywhere inside the second barrier. It satisfies C-17 only when placed in a labeled section that precedes all evaluative output from that barrier. A named "SECOND BARRIER — PRE-EVALUATION HEADER" label announces the positional boundary; the non-deference sentence inside it is active when the barrier opens, before any construct appears in the validation table below. Tests whether the named label is the minimum structural mechanism for C-17 or whether an unlabeled sentence in the same position would also pass.
**Base:** R3 V-02 (five tables, GATE 1, Round 1/Round 2 two-barrier structure) — passes C-01–C-16, scores 118/118 under v3 rubric.

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

**GATE 1:** All TABLE 1 rows have PA constructs, numeric limits, and Round 1 validation lines. Block: TABLE 2 is blocked until all three conditions are met. This gate catches missing constructs; Round 2 (after TABLE 5) catches imprecise ones.

---

### TABLE 2 — RATE LIMIT HIT ORDERING

| Hit order | Tier | Component | PA construct | Limit | Scenario projected volume | Why this order holds at scenario volume |
|-----------|------|-----------|-------------|-------|--------------------------|------------------------------------------|
| 1 (bottleneck) | | | | | | |
| 2 | | | | | | |

Rule: "Why this order holds" must explain the ordering at aggregate volume — not just reproduce the limits in ascending order.

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

**GATE 3:** Steps 1 and 2 must be filled and the cascade resolution statement present. Block: USER EXPERIENCE MAP is blocked until this condition is met.

---

### USER EXPERIENCE MAP

For each tier in TABLE 1:
> "Tier [N]: User sees/experiences: [specific description] — UX category: [transparent retry / visible delay / error surfaced to user / silent data loss]"

Rule: Categories must differ across tiers.

---

### RETRY-AFTER GAPS

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

**PA VALIDATION — ROUND 2**

**SECOND BARRIER — PRE-EVALUATION HEADER (before any construct evaluation begins):**
Do not assume Round 1 was accurate because constructs appeared to validate without correction. Round 1's confidence is not evidence of Round 1's precision. Treat Round 1's accepted construct names as unverified at the start of this review. This header precedes all evaluative output from Round 2 — the independence instruction is active before any construct is examined in the table below.

Scope: Round 2 covers construct categories introduced after Round 1's execution window had closed. Round 1 only reviewed TABLE 1 constructs — those present when Round 1 executed at TABLE 1 time. The following categories were introduced after Round 1's scope window closed and require independent review here: (a) propagation signal types and protocol names from TABLE 3 — introduced after Round 1's execution; (b) cascade mechanism labels and failure-mode constructs from TABLE 5 — introduced after Round 1's execution. Round 1 could not have covered these because they did not exist within Round 1's execution scope.

After the pre-evaluation header above, review all PA constructs used in this output. Write one line per construct:
> "[Construct] — confirmed / corrected to: [X] — reason: [one sentence]"

Batch confirmation does not count. Each construct requires its own line.

---

## V-02 — Single-axis: Structural Closure Reason for Scope Extension (C-18)

**Variation axis:** C-18 — structural closure reason in scope declaration
**Hypothesis:** A scope declaration that names three construct populations satisfies C-16. It satisfies C-18 only when it also names the structural reason why the first barrier's execution window excluded those categories — not just that they are being covered now. Tests whether a single structural closure sentence naming the window boundary ("ROLE 1's construct-definition window closed at section 1.2 completion, before sections 1.3–1.5 executed") is the minimum mechanism for C-18, independently of C-16. The closure reason transforms a scope preference into a structural argument.
**Base:** Modified R3 V-03 (two-role design, GATE 1, ROLE 1 (?) flagging, C-14/C-15 pass) with scope declaration that names populations but uses a preference framing ("Round 1 did not cover these"). V-02 adds one structural closure sentence. Expected: the addition moves C-18 from FAIL to PASS, scoring ~127.

---

Two roles execute this simulation sequentially. ROLE 1 (Connectors throughput expert) builds the technical analysis. ROLE 2 (Power Automate platform expert) validates domain accuracy, fills UX and retry-after detail, and produces remediations. ROLE 2 is the second barrier — ROLE 1's construct choices are the first pass; ROLE 2's validation table is the second. Neither role alone is sufficient.

**Scenario:** [Insert scenario here]

---

## ROLE 1 — CONNECTORS THROUGHPUT EXPERT

**Domain rule:** All tier names, limits, and constructs must use exact Connectors/PA terminology. Flag any construct you are uncertain about with (?) for ROLE 2 to correct.

### 1.1 — SCENARIO SETUP

| Component | Tier | PA construct (exact, or flag with ?) | Limit (req/unit-time) | Volume contribution |
|-----------|------|---------------------------------------|----------------------|---------------------|
| | | | | |

Aggregate scenario request volume: **[N req/unit-time]**

**GATE 1:** All rows have a named PA construct (or ? flag), numeric limit, and volume contribution. Block: ROLE 1.2 is blocked until this condition is met.

### 1.2 — BOTTLENECK DECLARATION AND INERTIA SEED

> "[Specific component name] saturates first at [N req/unit-time] under this scenario because [reason this aggregate volume exceeds this tier first]. **[INERTIA-SEED]:** The developer assumption that [name the independence or additive assumption] fails here because [one sentence on why this scenario's topology or volume breaks it]."

| Hit order | Tier | Component | PA construct | Limit | Why this order holds at scenario volume |
|-----------|------|-----------|-------------|-------|-----------------------------------------|
| 1 (bottleneck) | | | | | |
| 2 | | | | | |

### 1.3 — BACKPRESSURE PROPAGATION

Trace hop by hop from Tier 1 to terminal state:
> "Hop 1: [Component A] emits [signal type] → [Component B] responds by: [specific behavior]"
> Continue until terminal state.

### 1.4 — UNPROTECTED BURST PATHS

| Path | PA construct (exact) | Location | Peak rate | Why it bypasses tier-1 guard |
|------|---------------------|---------|-----------|------------------------------|
| | | | | |

If none: "No burst paths. Guards in place: [list]."

### 1.5 — CASCADE FAILURE TRACE (resolves [INERTIA-SEED])

> "The [INERTIA-SEED] assumption breaks: [one sentence showing the causal link — naming the mechanism that couples the tiers]."

| Cascade step | Component | Action | Causal mechanism | Load added to next tier | Failure mode | Duration |
|-------------|-----------|--------|-----------------|-------------------------|--------------|----------|
| 1 | | throttles | | | | |
| 2 | | throttles (cascade) | | | | |

Rule: This section must restate the [INERTIA-SEED] assumption from 1.2 and show how the cascade proves it false.

---

## ROLE 2 — POWER AUTOMATE PLATFORM EXPERT

You are reviewing ROLE 1's output for PA construct accuracy and producing the platform-specific analysis. Your validation table is the **second barrier**.

### 2.1 — PA CONSTRUCT VALIDATION (Second barrier)

**Independence requirement:** Do not assume ROLE 1 was accurate because it was confident. If ROLE 1 had zero (?) flags, confirm each construct explicitly and explain why it is correct. The second barrier is independent of ROLE 1's confidence.

**Scope declaration:** Your validation covers three construct populations that ROLE 1 did not review: (a) tier-map and hit-ordering constructs from sections 1.1–1.2, re-validated independently of ROLE 1's confidence; (b) propagation signal types and protocol names introduced in section 1.3; (c) cascade mechanism labels and failure-mode constructs introduced in section 1.5. The structural reason these categories were outside ROLE 1's scope: ROLE 1's construct-definition window closed at section 1.2 completion — at that point ROLE 1 had finished defining tier-map constructs and hit-ordering constructs. Sections 1.3, 1.4, and 1.5 then executed after that window had closed, introducing construct references (propagation signal types, burst construct names, cascade mechanism labels) that were not present within ROLE 1's execution window by construction. Those references could not have been reviewed by ROLE 1 regardless of how thoroughly ROLE 1 performed its analysis. Do not treat populations (b) and (c) as reviewed by ROLE 1 — they were structurally outside ROLE 1's scope.

Review every construct named in ROLE 1. Do not batch-confirm.

| ROLE 1 construct name (as written) | Source (section) | Confirmed or corrected | Exact PA construct name | Why this is correct in PA runtime context |
|-------------------------------------|-----------------|----------------------|-------------------------|-------------------------------------------|
| | | confirmed / corrected to: | | |

### 2.2 — USER EXPERIENCE PER THROTTLE TIER

| Tier | PA runtime behavior on throttle | User-visible experience (specific) | UX category |
|------|--------------------------------|------------------------------------|-------------|
| Tier 1 | | | transparent retry / visible delay / error surfaced / silent data loss |
| Tier 2 | | | (must differ from Tier 1) |

### 2.3 — RETRY-AFTER GAP ASSESSMENT

| Consumer | PA retry mechanism in use | 429 from which tier | Retry-After header read? | Gap identified | Consequence |
|----------|--------------------------|---------------------|--------------------------|----------------|-------------|
| | | | yes / no / N/A | | hammering / premature retry / extended outage / none |

### 2.4 — QUANTIFIED RISK REGISTER

| Tier | PA construct (validated) | Limit | Projected scenario volume | Status (SAFE / MARGINAL / OVER-LIMIT) | Headroom (+) or deficit (-) |
|------|-------------------------|-------|--------------------------|---------------------------------------|------------------------------|
| | | | | | |

### 2.5 — PA-SPECIFIC REMEDIATIONS

At least two. Each must name an exact PA feature or setting. "Add retries" and "reduce load" do not count.

| Finding addressed (cite ROLE 1 section) | PA feature (exact name) | Configuration detail | Effect on finding |
|------------------------------------------|------------------------|----------------------|-------------------|
| | | | |
| | | | |

**Autonomy note:** ROLE 2 may identify additional remediations from PA-platform-specific controls not visible in a Connectors-domain view: per-connection entitlements, environment-level request allocation, service principal pooling, premium connector tier upgrades, M365 service protection exemption requests.

---

## V-03 — Single-axis: Label-Enforced Co-location Independence (C-19)

**Variation axis:** C-19 — distinct named labels when two independent directives occupy the same block
**Hypothesis:** When the independence assertion (C-15) and scope declaration (C-16) are co-located in a single ROLE 2 preamble block without labels, an evaluator treats them as one mechanism and both criteria collapse to one score. Adding distinct named labels — "Independence:" and "Scope extension:" — forces the evaluator to parse each as a separate requirement, and both score independently. Tests whether labels alone are the structurally load-bearing element for C-19 when all other content is identical.
**Base:** Fresh two-role design with both directives in a single ROLE 2 preamble block. Both directives contain the full C-15 and C-16 content. Both are labeled. The pre-barrier position satisfies C-17; the closure reason satisfies C-18; the labels satisfy C-19; the GATE syntax satisfies C-20.

---

Two roles execute this analysis sequentially.

**ROLE 1** (Connectors throughput analyst): builds the technical analysis — tier map, bottleneck, propagation chain, burst paths, cascade failure.
**ROLE 2** (Power Automate platform expert): independently validates all PA domain accuracy and produces platform-grounded UX, retry-after assessment, risk quantification, and remediations.

**Scenario:** [Insert scenario here]

**Domain rule:** Every PA construct name must be exact. Valid constructs: Power Platform request entitlements, connector throttling policies, flow run concurrency limits, action call limits, premium vs. standard connector tiers, Microsoft 365 service protection limits. Generic HTTP 429 without a PA construct name does not count.

---

## ROLE 1 — CONNECTORS THROUGHPUT ANALYST

### 1.1 — COMPONENT MAP AND RATE LIMIT INVENTORY

| Component | PA construct (exact) | Limit (req/unit-time) | Volume contribution | Retry-After published? (yes/no/N/A) |
|-----------|---------------------|-----------------------|---------------------|--------------------------------------|
| | | | | |

Aggregate scenario request volume: **[N req/unit-time]**

**GATE 1:** All rows have a named PA construct, a numeric limit with unit, and a volume contribution. Block: ROLE 1.2 is blocked until this condition is met.

### 1.2 — BOTTLENECK DECLARATION AND INERTIA SEED

> "[Specific component name] at [PA construct] is the binding bottleneck. It saturates at [N req/unit-time] because [reason the aggregate volume exceeds this tier first]. **[INERTIA-SEED]:** The developer assumption that [name the naive assumption] fails here because [one sentence on why this topology or volume invalidates it]."

| Hit order | Tier | Component | PA construct | Limit | Why this order holds at scenario volume |
|-----------|------|-----------|-------------|-------|-----------------------------------------|
| 1 (bottleneck) | | | | | |
| 2 | | | | | |

Rule: "Why this order holds" must explain the ordering at aggregate volume — not reproduce limits in ascending order.

### 1.3 — BACKPRESSURE PROPAGATION CHAIN

| Hop | From component | Signal emitted | Signal type (error code / retry-after header / queue depth / other) | To component | Response behavior |
|-----|---------------|----------------|---------------------------------------------------------------------|--------------|-------------------|
| 1 | | | | | |
| 2 | | | | | |

### 1.4 — BURST PATH IDENTIFICATION

| Path | PA flow construct (exact) | Location in flow | Estimated peak rate (req/unit-time) | Why it bypasses or overwhelms the tier-1 guard |
|------|--------------------------|-----------------|--------------------------------------|------------------------------------------------|
| | | | | |

If none: write "None identified" in the first cell; list guards in the remaining cells.

### 1.5 — CASCADE FAILURE TRACE (resolves [INERTIA-SEED])

Open with:
> "The [INERTIA-SEED] assumption breaks here: [one sentence showing how this cascade proves the naive assumption false — naming the coupling mechanism]."

| Cascade step | Component | Action | Causal mechanism | Load added to next tier (estimate) | Failure mode | Duration |
|-------------|-----------|--------|-----------------|-------------------------------------|--------------|----------|
| 1 | | throttles | | | brownout / full stop / partial data | |
| 2 | | throttles (cascade) | | | | |

Rule: This section must cite [INERTIA-SEED] by label and restate the broken assumption from 1.2.

---

## ROLE 2 — POWER AUTOMATE PLATFORM EXPERT

**Second-barrier preamble (before any construct evaluation begins):**

**Independence:** Treat all ROLE 1 construct names as unverified at the start of this role. Do not assume ROLE 1 was accurate because it named constructs without flagging uncertainty. ROLE 1's confidence is not evidence of ROLE 1's precision — a construct can be plausible in the Connectors domain yet imprecise from a PA runtime platform perspective. Your validation is independent of ROLE 1's self-assessment. This directive is active before any construct appears in section 2.1 below.

**Scope extension:** Your validation covers construct categories that ROLE 1 could not have reviewed within its execution window. ROLE 1's construct-definition window closed at section 1.2 completion — the tier-map and hit-ordering phases. Sections 1.3, 1.4, and 1.5 then executed after that window had closed and introduced new construct references: propagation signal types and protocol names (1.3), burst construct names (1.4), and cascade mechanism labels (1.5). These categories were not present at ROLE 1's definition-window boundary and could not have been reviewed by ROLE 1 regardless of thoroughness. This role covers three populations: (a) tier-map and hit-ordering constructs from sections 1.1–1.2, re-validated independently of ROLE 1's confidence; (b) propagation signal types and protocol names from section 1.3 — structurally outside ROLE 1's window; (c) cascade mechanism labels from section 1.5 — also structurally outside ROLE 1's window. Do not treat populations (b) and (c) as reviewed — they were not present within ROLE 1's execution window.

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

| Consumer | PA retry mechanism in use | 429 from which tier | Retry-After header read? | Gap identified | Consequence |
|----------|--------------------------|---------------------|--------------------------|----------------|-------------|
| | | | yes / no / N/A | | hammering / premature retry / extended outage / none |

### 2.4 — QUANTIFIED RISK REGISTER

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

**Platform controls:** Beyond ROLE 1 findings, identify PA-platform-specific controls not surfaced from a Connectors-domain view: per-connection request entitlements, environment-level request allocation, service principal pooling, premium connector tier upgrades, M365 service protection exemption requests.

---

## V-04 — Combination: C-17 + C-18 + C-19 (Placement + Closure Reason + Labels Together)

**Variation axis:** C-17 + C-18 + C-19 together in a single named pre-barrier block
**Hypothesis:** The three R4 structural placement/labeling criteria are independent mechanisms that compose in one block. C-17 requires the preamble to precede all evaluative output (positional); C-18 requires a closure reason sentence naming the window boundary (content); C-19 requires distinct labels when two directives occupy the same block (structural). A single ROLE 2 "SECOND BARRIER — PRE-EVALUATION PREAMBLE" block that: (a) appears before section 2.1, (b) carries both directives each labeled, and (c) includes the closure reason in the "Scope extension:" subsection — should satisfy all three simultaneously. Tests whether the three criteria compose without interference in one combined pre-barrier design.
**Base:** Fresh two-role design, incorporating all mechanisms from V-01/V-02/V-03 into a single second-barrier opening.

---

Two roles execute this analysis sequentially.

**ROLE 1** (Connectors throughput analyst): builds the technical analysis — tier map, bottleneck, hit ordering, propagation, burst paths, cascade failure.
**ROLE 2** (Power Automate platform expert): independently validates all PA construct accuracy and produces platform-grounded UX, retry-after assessment, risk quantification, and remediations. ROLE 2 is the second barrier.

**Scenario:** [Insert scenario here]

**Domain rule:** Every PA construct name must be exact. Valid constructs: Power Platform request entitlements, connector throttling policies, flow run concurrency limits, action call limits, premium vs. standard connector tiers, Microsoft 365 service protection limits. Generic HTTP 429 without a PA construct name does not count.

---

## ROLE 1 — CONNECTORS THROUGHPUT ANALYST

### 1.1 — COMPONENT MAP

| Component | PA construct (exact) | Limit (req/unit-time) | Volume contribution | Retry-After published? (yes/no/N/A) |
|-----------|---------------------|-----------------------|---------------------|--------------------------------------|
| | | | | |

Aggregate scenario request volume: **[N req/unit-time]**

**GATE 1:** All rows have a named PA construct, a numeric limit with unit, and a volume contribution. Block: ROLE 1.2 is blocked until this condition is met. If any row is incomplete, complete it now before proceeding.

### 1.2 — BOTTLENECK AND INERTIA SEED

> "[Specific component name] at [PA construct] is the binding bottleneck. It saturates at [N req/unit-time] because [reason the aggregate volume exceeds this tier first]. **[INERTIA-SEED]:** The developer assumption that [name the naive assumption] fails here because [one sentence on why this scenario invalidates it]."

| Hit order | Tier | Component | PA construct | Limit | Why this order holds at scenario volume |
|-----------|------|-----------|-------------|-------|-----------------------------------------|
| 1 (bottleneck) | | | | | |
| 2 | | | | | |

### 1.3 — BACKPRESSURE PROPAGATION

| Hop | From component | Signal emitted | Signal type (error code / retry-after header / queue depth / other) | To component | Response behavior |
|-----|---------------|----------------|---------------------------------------------------------------------|--------------|-------------------|
| 1 | | | | | |
| 2 | | | | | |

### 1.4 — BURST PATH IDENTIFICATION

| Path | PA flow construct (exact) | Location in flow | Estimated peak rate (req/unit-time) | Why it bypasses or overwhelms tier-1 guard |
|------|--------------------------|-----------------|--------------------------------------|--------------------------------------------|
| | | | | |

If none: "None identified." List guards in effect in the remaining cells.

### 1.5 — CASCADE FAILURE TRACE (resolves [INERTIA-SEED])

Open with:
> "The [INERTIA-SEED] assumption breaks here: [one sentence on how this cascade proves the naive assumption false — naming the coupling mechanism]."

| Cascade step | Component | Action | Causal mechanism | Load added to next tier (estimate) | Failure mode | Duration |
|-------------|-----------|--------|-----------------|-------------------------------------|--------------|----------|
| 1 | | throttles | | | brownout / full stop / partial data | |
| 2 | | throttles (cascade) | | | | |

Rule: This section must cite [INERTIA-SEED] by label and restate the broken assumption from 1.2.

---

## ROLE 2 — POWER AUTOMATE PLATFORM EXPERT

**SECOND BARRIER — PRE-EVALUATION PREAMBLE (this block precedes all evaluative output from ROLE 2; both directives below are active when the barrier opens, before any construct appears in section 2.1):**

**Independence:** Treat all ROLE 1 construct names as unverified at the start of this role. Do not assume ROLE 1 was accurate because it produced constructs without flagging uncertainty. ROLE 1's confidence is not evidence of ROLE 1's precision — a construct can appear plausible in the Connectors domain while being imprecise from a PA runtime platform perspective. Your validation is independent of ROLE 1's self-assessment. This directive is in effect before any construct is examined in section 2.1 below.

**Scope extension:** Your validation covers construct categories that ROLE 1 could not have reviewed. The structural reason: ROLE 1's construct-definition window closed at section 1.2 completion. At that point ROLE 1 had defined tier-map constructs (1.1) and hit-ordering constructs (1.2). Sections 1.3, 1.4, and 1.5 then executed after ROLE 1's definition window had already closed — those sections introduced construct references (propagation signal types from 1.3, burst construct names from 1.4, cascade mechanism labels from 1.5) that were not present within ROLE 1's execution window by construction. These categories are new scope for this barrier, not optional additions. This role covers three populations: (a) tier-map and hit-ordering constructs from sections 1.1–1.2 — re-validated independently of ROLE 1's confidence; (b) propagation signal types and protocol names from section 1.3 — structurally outside ROLE 1's window; (c) cascade mechanism labels from section 1.5 — also structurally outside ROLE 1's window. Do not treat populations (b) and (c) as reviewed — they were not present at ROLE 1's definition-window boundary.

### 2.1 — PA CONSTRUCT VALIDATION

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

| Consumer | PA retry mechanism in use | 429 from which tier | Retry-After header read? | Gap identified | Consequence |
|----------|--------------------------|---------------------|--------------------------|----------------|-------------|
| | | | yes / no / N/A | | hammering / premature retry / extended outage / none |

### 2.4 — QUANTIFIED RISK REGISTER

| Tier | PA construct (validated) | Limit | Projected scenario volume | Status (SAFE / MARGINAL / OVER-LIMIT) | Headroom (+) or deficit (-) |
|------|-------------------------|-------|--------------------------|---------------------------------------|------------------------------|
| | | | | | |

Status derived from numeric comparison — not estimated qualitatively.

### 2.5 — PA-SPECIFIC REMEDIATIONS

At least two. Each must name an exact PA feature or setting. "Add retries" and "reduce load" do not count.

| Finding addressed (cite ROLE 1 section) | PA feature (exact name) | Configuration detail | Effect on finding |
|------------------------------------------|------------------------|----------------------|-------------------|
| | | | |
| | | | |

**Platform controls:** Identify PA-platform-specific controls not surfaced from a Connectors-domain view: per-connection request entitlements, environment-level request allocation, service principal pooling, premium connector tier upgrades, M365 service protection exemption requests. Add rows if relevant.

---

## V-05 — Full Synthesis: All Twenty Criteria Explicitly Embedded

**Variation axis:** R3 V-05 base + C-17 via named PRE-ANALYSIS ASSERTION block + C-18 via execution-window closure reason in scope extension + C-19 via labeled pair in PRE-ANALYSIS ASSERTION + C-20 via all three prose gate elements present at each gate
**Hypothesis:** All twenty criteria (C-01 through C-20) can be embedded in a single PHASE-structured prompt. The four R4 additions to R3 V-05: (1) PHASE 4.A opens with a named "PRE-ANALYSIS ASSERTION" section before the validation table — C-17 satisfied by structural position; (2) scope extension in PRE-ANALYSIS ASSERTION names the execution-window boundary as a structural fact ("categories introduced in PHASES 2–3, which executed after GATE 1's scope window had already closed") — C-18 satisfied by closure reason; (3) PRE-ANALYSIS ASSERTION carries "Independence:" and "Scope extension:" as two distinct labeled subsections — C-19 satisfied by labels; (4) each GATE carries name/label + explicit conditional prerequisite + "Block: PHASE X is blocked" — C-20 confirmed by prose portability. Expected: **130/130**.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across the rate-limited system described in this scenario. This simulation must surface: the binding bottleneck, ordered throttle tiers, backpressure propagation chain, user experience per tier, unprotected burst paths, retry-after gaps, cascade failure sequence, quantified risk register, and PA-specific remediations.

**Scenario:** [Insert scenario here]

**Structural requirements (all twenty criteria satisfied when the output follows this structure):**
- **C-11 — Two-barrier PA validation:** GATE 1 is the first barrier (construct presence, PHASE 1). PHASE 4.A is the second barrier (construct precision). Both must fire independently. An output that fires only one does not satisfy C-11.
- **C-12 — Five pre-printed tables:** TABLE 1 (tier ordering), TABLE 2 (backpressure hops), TABLE 3 (burst paths), TABLE 4 (cascade sequence), TABLE 5 (risk register). Each table has columns enforcing the hardest pass condition for its criterion.
- **C-13 — Inertia-to-cascade causal thread:** PHASE 2.A requires a named `[INERTIA-SEED]` sentence. PHASE 3.C must cite `[INERTIA-SEED]` by label. Both ends structurally enforced.
- **C-14 — Named phase gate enforcement:** Each GATE states an explicit prerequisite and names the section it blocks. Section headings alone do not constitute gates.
- **C-15 — Validator independence assertion:** PHASE 4.A PRE-ANALYSIS ASSERTION carries an imperative non-deference sentence naming GATE 1 and asserting completeness is not evidence of precision.
- **C-16 — Barrier scope inheritance boundary:** PHASE 4.A PRE-ANALYSIS ASSERTION names which construct categories are new to PHASE 4.A's scope that GATE 1 could not have covered, with structural reason.
- **C-17 — Pre-barrier independence placement:** The C-15 sentence is in the PRE-ANALYSIS ASSERTION block before any construct-by-construct output from PHASE 4.A. Active when the barrier opens.
- **C-18 — Structural closure reason:** The C-16 scope extension names the execution-window closure as structural fact ("GATE 1's scope window had already closed before PHASES 2–3 introduced those categories") — not a preference.
- **C-19 — Label-enforced co-location independence:** PRE-ANALYSIS ASSERTION carries both C-15 and C-16 under distinct labels ("Independence:" and "Scope extension:") so each scores as a separate criterion.
- **C-20 — Gate mechanism prose portability:** Each GATE carries all three elements: (a) name, (b) conditional prerequisite, (c) named block target. Format is decorative; three elements are load-bearing.

---

### PHASE 1 — SCENARIO SETUP AND FIRST PA BARRIER

**TABLE 0 — COMPONENT MAP**

| Component | PA construct (exact) | Limit (req/unit-time) | Consumer(s) | Retry-After published? (yes/no/N/A) |
|-----------|---------------------|-----------------------|-------------|--------------------------------------|
| | | | | |

Aggregate scenario request volume: **[N req/unit-time]**

**GATE 1 — First PA barrier (construct presence):**
Prerequisite: (a) every row has a named PA construct — not a generic API description; (b) every limit is numeric with unit; (c) every consumer is named.
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

Rule: "Why this order holds" must explain the ordering at the scenario's aggregate volume — not simply list limits in ascending order.

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

Rule: UX categories must differ across rows.

**GATE 2 — Prerequisite:** (a) bottleneck statement complete with [INERTIA-SEED] sentence; (b) TABLE 1 "Why this order holds" populated for all rows; (c) TABLE 2 has at least one complete hop; (d) UX table has at least two tiers with distinct categories.
Block: PHASE 3 is blocked until all four conditions are met.

---

### PHASE 3 — FAILURE ANALYSIS

**3.A — Unprotected Burst Paths**

**TABLE 3 — BURST PATH ENUMERATION**

| Path | PA flow construct (exact) | Location in flow | Estimated peak rate (req/unit-time) | Why it bypasses or overwhelms the tier-1 guard |
|------|--------------------------|-----------------|--------------------------------------|------------------------------------------------|
| | | | | |

If no burst paths: write "None identified" in the first cell; list guards in the final cell: "Guards in place: [list each guard and the construct it protects]."

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

**GATE 3 — Prerequisite:** At least one complete cascade chain — Steps 1 and 2 filled, `[INERTIA-SEED]` cited and broken assumption restated — is present.
Block: PHASE 4 is blocked until this condition is met.

---

### PHASE 4 — QUANTIFICATION AND SECOND PA BARRIER

**4.A — PA Construct Validation (Second barrier — construct precision)**

**PRE-ANALYSIS ASSERTION (before any construct evaluation begins — this section precedes all per-construct output from PHASE 4.A; both directives below are active when this barrier opens):**

**Independence:** Do not assume GATE 1 was accurate because all constructs passed the presence check. GATE 1's completeness is not evidence of precision. A construct that was present and accepted at GATE 1 may still be imprecise from a PA runtime platform perspective. Treat all construct names as unverified at the start of this section. This instruction is in effect before any construct appears in the validation table below.

**Scope extension:** This section covers construct categories that did not exist within GATE 1's execution window and could not have been reviewed by GATE 1 regardless of its thoroughness. The structural reason: GATE 1 executed at PHASE 1 — its scope was bounded by TABLE 0's tier component names at that execution time. PHASES 2 and 3 then ran after GATE 1's scope window had already closed, introducing construct references that were not present at GATE 1 execution: propagation signal types and protocol names from TABLE 2 and PHASE 2.B, cascade mechanism labels and failure-mode constructs from TABLE 4 and PHASE 3.C, and UX and retry-after constructs from PHASE 2.C and PHASE 3.B. These categories are new scope — structurally outside GATE 1's window, not optional additions. This section covers: (a) tier component constructs from TABLE 0 and TABLE 1 — re-validated independently of GATE 1's acceptance; (b) propagation signal types and protocol names from TABLE 2 — not present at GATE 1 execution time; (c) cascade mechanism labels, failure-mode constructs, UX constructs, and retry-after constructs from PHASES 2.C, 3.B, and 3.C — also not present at GATE 1 execution time.

Review every PA construct used in PHASES 1–3:

| PHASE/Section where used | Construct name as written | Confirmed or corrected | Exact PA construct name (if correction) | Why this is correct in PA runtime context |
|--------------------------|--------------------------|----------------------|-----------------------------------------|-------------------------------------------|
| | | confirmed / corrected to: | | |

Batch confirmation ("all constructs are correct") does not satisfy C-11. Each construct requires a per-construct review line.

**4.B — User Experience Validation (PA runtime view)**

Review each UX tier from PHASE 2.C using the PA platform perspective. Correct if PA runtime behavior differs from the connector-domain characterization:

| Tier | PHASE 2.C UX (original characterization) | PA runtime behavior (if different) | Revised UX (if applicable) |
|------|------------------------------------------|-------------------------------------|----------------------------|
| Tier 1 | | | |
| Tier 2 | | | |

**4.C — Quantified Risk Register**

**TABLE 5 — RISK REGISTER**

| Tier | PA construct (validated in 4.A) | Limit | Projected scenario volume | Status (SAFE / MARGINAL / OVER-LIMIT) | Headroom (+) or deficit (-) |
|------|--------------------------------|-------|--------------------------|---------------------------------------|------------------------------|
| | | | | | |

All tiers from PHASE 1 must appear. Status derived from numeric comparison — not estimated.

**4.D — PA-Specific Remediations**

At least two. "Add retries" and "reduce load" do not count. Each must name an exact PA feature or setting.

| Finding addressed (cite PHASE/section) | PA feature (exact name) | Configuration detail | Effect on finding |
|----------------------------------------|------------------------|----------------------|-------------------|
| | | | |
| | | | |

**Inertia verdict (required):** In one sentence, state the consequence of not acting: "If the [INERTIA-SEED] assumption is left in place and these remediations are not applied, the result is: [specific outcome with volume threshold or timeline]."

---

## Predicted Scores (v4 rubric, max 130)

| V | C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | C-11 | C-12 | C-13 | C-14 | C-15 | C-16 | C-17 | C-18 | C-19 | C-20 | Total |
|---|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|-------|
| V-01 | 12 | 12 | 12 | 12 | 12 | 10 | 10 | 10 | 5 | 5 | 3 | 3 | 3 | 3 | 3 | 3 | **3** | 3 | 0 | 3 | **127** |
| V-02 | 12 | 12 | 12 | 12 | 12 | 10 | 10 | 10 | 5 | 5 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | **3** | 0 | 3 | **127** |
| V-03 | 12 | 12 | 12 | 12 | 12 | 10 | 10 | 10 | 5 | 5 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | **3** | 3 | **130** |
| V-04 | 12 | 12 | 12 | 12 | 12 | 10 | 10 | 10 | 5 | 5 | 3 | 3 | 3 | 3 | 3 | 3 | **3** | **3** | **3** | 3 | **130** |
| V-05 | 12 | 12 | 12 | 12 | 12 | 10 | 10 | 10 | 5 | 5 | 3 | 3 | 3 | 3 | 3 | 3 | **3** | **3** | **3** | **3** | **130** |

**Key bets:**

- **C-17 (V-01):** The "SECOND BARRIER — PRE-EVALUATION HEADER" label announces the positional boundary; the non-deference sentence is inside it before the validation table begins. The sentence names Round 1 as the prior layer and asserts confidence-is-not-evidence. Predicted PASS. C-18 predicted PASS from scope text inherited from R3 V-02 ("introduced after Round 1's execution window had closed"). C-19 N/A — only one labeled block in V-01's design.

- **C-18 (V-02):** One structural closure sentence added: "ROLE 1's construct-definition window closed at section 1.2 completion — before sections 1.3–1.5 executed." This names the window boundary as a structural fact (ROLE 1's phases closed before 1.3 executed), not a preference. Predicted PASS. C-17 predicted PASS from base placement (independence sentence precedes evaluation table). C-19 N/A — scope and independence are in sequential blocks, not co-located.

- **C-19 (V-03):** Both directives are in a single ROLE 2 "Second-barrier preamble" block, each under a distinct label. "Independence:" carries the C-15/C-17 content. "Scope extension:" carries the C-16/C-18 content. Labels force independent parsing — evaluator must treat them as two separate mechanisms. C-17 predicted PASS (both labeled blocks appear before 2.1 table). C-18 predicted PASS (closure reason present in "Scope extension:"). Predicted **130** — all four R4 criteria present.

- **C-17 + C-18 + C-19 combination (V-04):** Named "SECOND BARRIER — PRE-EVALUATION PREAMBLE" carries both labeled subsections before any evaluative output. "Independence:" asserting non-deference, "Scope extension:" giving structural closure reason with window boundary named. C-17: pre-evaluation position confirmed by block name. C-18: closure reason present. C-19: labels force independent parsing. C-20: GATE 1 carries name + conditional prerequisite + "Block: ROLE 1.2 is blocked." Predicted **130**.

- **V-05 ceiling confirmation (130/130):** All twenty criteria named in structural requirements header and embedded at point-of-use. PRE-ANALYSIS ASSERTION opens PHASE 4.A with labeled "Independence:" and "Scope extension:" blocks before the validation table (C-17 placement, C-18 closure reason, C-19 labels). Three GATE blocks each carry name + conditional + "Block: PHASE X is blocked" (C-20 confirmed prose portable). Primary uncertainty: does C-19 require the label to be at the START of each directive sentence, or can the label appear as a bold markdown header before the paragraph? Predicted YES — bold markdown headers are labels in this format.
