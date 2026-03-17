Written to `simulations/quest/variations/flow-throttle-variations-R5-2026-03-14.md`.

---

## Round 5 Variations — Summary

| V | Axis | Key mechanism | Predicted score |
|---|------|---------------|-----------------|
| **V-01** | C-21 isolation | "SECOND BARRIER — PRE-EVALUATION HEADER (before any construct evaluation begins)" — positional name, no labeled pair | 133 |
| **V-02** | C-22 isolation | "ROLE 2 PREAMBLE" — labeled `Independence:` / `Scope extension:` pair, no positional qualifier in container name | 133 |
| **V-03** | Role sequence | UX MAP before CASCADE; "PRE-EVALUATION PREAMBLE (before Round 2 construct evaluation begins)" with labeled pair | 136 |
| **V-04** | C-21 + C-22 + formal register | "SECOND BARRIER — PRE-EVALUATION PREAMBLE (before any construct evaluation begins)" with labeled pair; formal language | 136 |
| **V-05** | C-21 + C-22 + inertia framing + conversational | "PRE-ANALYSIS ASSERTION (before any Round 2 evaluation begins)" with labeled pair; developer-framed inertia tracked end-to-end | 136 |

---

**Diagnostic design:**

- **V-01** tests C-21 alone. The positional name ("PRE-EVALUATION HEADER (before any construct evaluation begins)") satisfies C-21. Two unlabeled paragraphs inside fail C-22 — no sub-labels, one mechanism block. Score: 133.
- **V-02** tests C-22 alone. "ROLE 2 PREAMBLE" has no positional qualifier — C-21 fails. The `Independence:` / `Scope extension:` sub-labels inside satisfy C-22. Score: 133.
- **V-03** is the role-sequence neutrality test. UX before cascade doesn't touch the pre-barrier block's structural position; C-21 and C-22 carry through. Score: 136.
- **V-04** and **V-05** are ceiling confirmations from opposite register extremes (formal vs. conversational). If both score 136, phrasing register is confirmed orthogonal to C-21/C-22.

The V-01/V-02 mirror design gives a clean 3-point delta signal for each new criterion independently. V-03–V-05 confirm the ceiling is reachable from three structurally different formats.
nce. Predicted 136/136.

---

## V-01 — Single-axis: C-21 Isolation (Positional Container Name, No Labeled Pair)

**Variation axis:** C-21 — pre-barrier container name encodes positional role
**Hypothesis:** "SECOND BARRIER — PRE-EVALUATION HEADER (before any construct evaluation begins)" satisfies C-21 because the container name includes an explicit positional qualifier. The two directives inside the block are unlabeled — an evaluator reads them as one mechanism section, not two independent directives. C-22 fails because the labeled pair is absent. Tests C-21 in isolation. Predicted: 133/136 (+3 C-21, +0 C-22).
**Base:** R4 V-04 table-based structure (confirmed 130/130 under v4 rubric). The pre-barrier block retains the positional name and full independence/scope content; `Independence:` / `Scope extension:` sub-labels are removed.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across the rate-limited system described in this scenario. All comparative, ordered, or enumerated analysis must appear in the pre-printed tables below.

**Scenario:** [Insert scenario here]

**Domain rule:** Every construct name must use exact Power Automate or Connectors terminology. Valid constructs: Power Platform request entitlements, connector throttling policies, flow run concurrency limits, action call limits, premium vs. standard connector tiers, Microsoft 365 service protection limits. Generic HTTP 429 without a PA construct name does not count.

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
> "[Component] at [PA construct] is the binding bottleneck. It saturates at [N req/unit-time] under this scenario. **[INERTIA-SEED]:** The developer assumption that [name the independence or additive assumption commonly made about these limits] fails here because [one sentence linking to cascade mechanism or shared principal pool]."

**PA VALIDATION — ROUND 1 (first barrier):** For each construct in TABLE 1, write one line:
> "[Construct name] — confirmed / corrected to: [X] — because: [one sentence]"

**GATE 1:** All TABLE 1 rows have PA constructs, numeric limits, and Round 1 validation lines. Block: TABLE 2 is blocked until all three conditions are met. If any row is incomplete, complete it now before proceeding.

---

### TABLE 2 — RATE LIMIT HIT ORDERING

| Hit order | Tier | Component | PA construct | Limit | Scenario projected volume | Why this order holds at scenario volume |
|-----------|------|-----------|-------------|-------|--------------------------|------------------------------------------|
| 1 (bottleneck) | | | | | | |
| 2 | | | | | | |

Rule: "Why this order holds" must explain the ordering at aggregate volume — not reproduce limits in ascending order.

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

**Cascade resolution statement (required):** "The cascade above resolves [INERTIA-SEED] because [one sentence showing how the causal chain proves the assumption false — cite [INERTIA-SEED] by label]."

**GATE 3:** Steps 1 and 2 must be filled and cascade resolution statement must cite [INERTIA-SEED] by label. Block: USER EXPERIENCE MAP is blocked until this condition is met.

---

### USER EXPERIENCE MAP

For each tier in TABLE 1:
> "Tier [N]: User sees/experiences: [specific description] — UX category: [transparent retry / visible delay / error surfaced to user / silent data loss]"

Rule: Categories must differ across tiers. State what the user sees, not what the system does internally.

---

### RETRY-AFTER GAPS

For each consumer in TABLE 1 where Retry-After is published:
> "Consumer: [name] — Current behavior: [what it does on 429] — Retry-After header read?: [yes / no] — Consequence: [hammering / premature retry / extended outage / none]"

---

### TABLE 6 — QUANTIFIED RISK REGISTER

| Tier | PA construct | Limit | Projected scenario volume | Status (SAFE / MARGINAL / OVER-LIMIT) | Headroom (+) or deficit (-) |
|------|-------------|-------|--------------------------|---------------------------------------|------------------------------|
| | | | | | |

All tiers from TABLE 1 must appear. Status derived from numeric comparison only.

---

### PA-SPECIFIC REMEDIATIONS

At least two. Each must name an exact PA feature or setting. "Add retries" and "reduce load" do not count.

| Finding addressed (cite TABLE/section) | PA feature (exact name) | Configuration | Effect |
|----------------------------------------|------------------------|---------------|--------|
| | | | |
| | | | |

---

**SECOND BARRIER — PRE-EVALUATION HEADER (before any construct evaluation begins)**

Do not assume Round 1 was accurate because constructs appeared to validate without correction. Round 1's confidence is not evidence of Round 1's precision. Treat Round 1's accepted construct names as unverified at the start of this pass. This header section precedes all Round 2 evaluative output — the independence instruction is active before any construct appears in the validation lines below.

Round 2 covers construct categories that Round 1's execution window excluded by construction. Round 1's construct-definition window closed at TABLE 1 validation time. The sections that followed — TABLE 2 through TABLE 5 — introduced construct references not present within Round 1's window: propagation signal types in TABLE 3, cascade mechanism labels in TABLE 5. Those categories could not have been reviewed by Round 1 regardless of how thoroughly Round 1 performed its analysis. The following populations require independent review: (a) propagation signal types and protocol names from TABLE 3 — introduced after Round 1's window closed; (b) cascade mechanism labels and failure-mode constructs from TABLE 5 — introduced after Round 1's window closed.

**PA VALIDATION — ROUND 2**

Review all PA constructs used in this output. Write one line per construct:
> "[Construct] — confirmed / corrected to: [X] — reason: [one sentence]"

Batch confirmation does not count. Each construct requires its own line.

---

## V-02 — Single-axis: C-22 Isolation (Labeled Pair, Neutral Container Name)

**Variation axis:** C-22 — labeled pair co-location in pre-barrier block
**Hypothesis:** "ROLE 2 PREAMBLE" carries no positional qualifier — C-21 fails regardless of how early the block appears before evaluative output. The `Independence:` and `Scope extension:` sub-labels inside the block are structurally load-bearing: an evaluator must parse each as an independent directive, satisfying C-22. Tests C-22 in isolation. Predicted: 133/136 (+0 C-21, +3 C-22).
**Base:** Two-role design (R4 V-03 structure; confirmed 130/130 under v4 rubric). The pre-barrier block retains the labeled pair and full content; the container name is kept neutral ("ROLE 2 PREAMBLE" — no positional qualifier added).

---

Two roles execute this simulation sequentially. ROLE 1 (Connectors throughput expert) builds the technical analysis. ROLE 2 (Power Automate platform expert) validates domain accuracy and produces the platform-specific analysis. ROLE 2 is the second barrier — ROLE 1's construct choices are the first pass; ROLE 2's validation table is the second. Neither role alone is sufficient.

**Scenario:** [Insert scenario here]

**Domain rule:** Every PA construct name must be exact. Valid constructs: Power Platform request entitlements, connector throttling policies, flow run concurrency limits, action call limits, premium vs. standard connector tiers, Microsoft 365 service protection limits. Generic HTTP 429 without a PA construct name does not count.

---

## ROLE 1 — CONNECTORS THROUGHPUT EXPERT

**Domain rule:** All tier names, limits, and constructs must use exact Connectors/PA terminology. Flag any construct you are uncertain about with (?) for ROLE 2 to correct.

### 1.1 — COMPONENT MAP AND RATE LIMIT INVENTORY

| Component | PA construct (exact, or flag with ?) | Limit (req/unit-time) | Volume contribution | Retry-After published? (yes/no/N/A) |
|-----------|---------------------------------------|----------------------|---------------------|--------------------------------------|
| | | | | |

Aggregate scenario request volume: **[N req/unit-time]**

**GATE 1:** All rows have a named PA construct (or ? flag), numeric limit, and volume contribution. Block: ROLE 1.2 is blocked until this condition is met.

### 1.2 — BOTTLENECK DECLARATION AND INERTIA SEED

> "[Specific component name] saturates first at [N req/unit-time] under this scenario because [reason this aggregate volume exceeds this tier first]. **[INERTIA-SEED]:** The developer assumption that [name the independence or additive assumption] fails here because [one sentence on why this scenario's topology or volume breaks it]."

| Hit order | Tier | Component | PA construct | Limit | Why this order holds at scenario volume |
|-----------|------|-----------|-------------|-------|-----------------------------------------|
| 1 (bottleneck) | | | | | |
| 2 | | | | | |

Rule: "Why this order holds" must explain the ordering at aggregate volume — not reproduce limits in ascending order.

### 1.3 — BACKPRESSURE PROPAGATION

| Hop | From component | Signal emitted | Signal type (error code / retry-after header / queue depth / other) | To component | Response behavior |
|-----|---------------|----------------|---------------------------------------------------------------------|--------------|-------------------|
| 1 | | | | | |
| 2 | | | | | |

Continue until terminal state.

### 1.4 — UNPROTECTED BURST PATHS

| Path | PA flow construct (exact) | Location in flow | Estimated peak rate (req/unit-time) | Why it bypasses tier-1 guard |
|------|--------------------------|-----------------|--------------------------------------|------------------------------|
| | | | | |

If none: "No burst paths. Guards in place: [list]."

### 1.5 — CASCADE FAILURE TRACE (resolves [INERTIA-SEED])

> "The [INERTIA-SEED] assumption breaks: [one sentence showing the causal link — naming the mechanism that couples the tiers]."

| Cascade step | Component | Action | Causal mechanism | Load added to next tier | Failure mode | Duration |
|-------------|-----------|--------|-----------------|-------------------------|--------------|----------|
| 1 | | throttles | | | brownout / full stop / partial data | |
| 2 | | throttles (cascade) | | | | |

Rule: This section must cite [INERTIA-SEED] by label and show how the cascade proves the assumption false.

---

## ROLE 2 — POWER AUTOMATE PLATFORM EXPERT

You are reviewing ROLE 1's output for PA construct accuracy and producing the platform-specific analysis. Your validation table is the **second barrier**.

**ROLE 2 PREAMBLE**

**Independence:** Treat all ROLE 1 construct names as unverified at the start of this role. Do not assume ROLE 1 was accurate because it produced output with no flagged uncertainties. Confidence in ROLE 1's output is not evidence of ROLE 1's precision — a construct can be plausible in the Connectors domain yet imprecise from a PA runtime platform perspective. Your validation is independent of ROLE 1's self-assessment. This directive is active before any construct appears in section 2.1 below.

**Scope extension:** This validation covers construct categories that ROLE 1's execution window excluded by construction. ROLE 1's construct-definition window closed at section 1.2 completion. Sections 1.3, 1.4, and 1.5 then introduced new construct references after that window had closed — propagation signal types and protocol names (1.3), burst construct names (1.4), cascade mechanism labels (1.5). Those categories were not present at ROLE 1's definition-window boundary and could not have been reviewed by ROLE 1 regardless of thoroughness. Three populations require coverage: (a) tier-map and hit-ordering constructs from sections 1.1–1.2, re-validated independently of ROLE 1's confidence; (b) propagation signal types from section 1.3 — structurally outside ROLE 1's window; (c) cascade mechanism labels from section 1.5 — structurally outside ROLE 1's window.

### 2.1 — PA CONSTRUCT VALIDATION (second barrier)

Review every construct from ROLE 1 sections 1.1–1.5. Per-construct review required. Do not batch-confirm.

| ROLE 1 construct name (as written) | Source (section) | Confirmed or corrected | Exact PA construct name | Why this is correct in PA runtime context |
|-------------------------------------|-----------------|----------------------|-------------------------|-------------------------------------------|
| | | confirmed / corrected to: | | |

### 2.2 — USER EXPERIENCE PER THROTTLE TIER

| Tier | PA runtime behavior on throttle | User-visible experience (specific) | UX category |
|------|--------------------------------|------------------------------------|-------------|
| Tier 1 | | | transparent retry / visible delay / error surfaced / silent data loss |
| Tier 2 | | | (must differ from Tier 1) |

Rule: Categories must differ across tiers. State what the user sees, not what the system does internally.

### 2.3 — RETRY-AFTER GAP ASSESSMENT

| Consumer | PA retry mechanism in use | 429 from which tier | Retry-After header read? | Gap identified | Consequence |
|----------|--------------------------|---------------------|--------------------------|----------------|-------------|
| | | | yes / no / N/A | | hammering / premature retry / extended outage / none |

### 2.4 — QUANTIFIED RISK REGISTER

| Tier | PA construct (validated) | Limit | Projected scenario volume | Status (SAFE / MARGINAL / OVER-LIMIT) | Headroom (+) or deficit (-) |
|------|-------------------------|-------|--------------------------|---------------------------------------|------------------------------|
| | | | | | |

Status must be derived from numeric comparison — not estimated qualitatively.

### 2.5 — PA-SPECIFIC REMEDIATIONS

At least two. Each must name an exact PA feature or setting. "Add retries" and "reduce load" do not count.

| Finding addressed (cite ROLE 1 section) | PA feature (exact name) | Configuration detail | Effect on finding |
|------------------------------------------|------------------------|----------------------|-------------------|
| | | | |
| | | | |

---

## V-03 — Single-axis: Role Sequence (UX Before Cascade, C-21+C-22 Intact)

**Variation axis:** Role sequence / lifecycle emphasis — USER EXPERIENCE MAP placed before CASCADE SEQUENCE
**Hypothesis:** The pre-barrier container and its labeled pair are properties of the second-barrier opening block, not of analysis section order. Moving USER EXPERIENCE MAP before CASCADE SEQUENCE changes the lifecycle phase ordering but leaves the structural position of the pre-barrier block unchanged — it still precedes all Round 2 evaluative output. Both C-21 (positional name) and C-22 (labeled pair) should score identically to the R4 ceiling. Lifecycle reorder is a content-neutral axis. Predicted: 136/136.
**Base:** Table-based single-LLM structure. Section order: TABLE 1 → BOTTLENECK → ROUND 1 → TABLE 2 → TABLE 3 → TABLE 4 → USER EXPERIENCE MAP → TABLE 5 CASCADE → RETRY-AFTER → TABLE 6 → REMEDIATIONS → PRE-BARRIER → ROUND 2.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across the rate-limited system described in this scenario. All comparative, ordered, or enumerated analysis must appear in the pre-printed tables below.

**Scenario:** [Insert scenario here]

**Domain rule:** Every construct name must use exact Power Automate or Connectors terminology. Valid constructs: Power Platform request entitlements, connector throttling policies, flow run concurrency limits, action call limits, premium vs. standard connector tiers, Microsoft 365 service protection limits. Generic HTTP 429 without a PA construct name does not count.

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
> "[Component] at [PA construct] is the binding bottleneck. It saturates at [N req/unit-time] under this scenario. **[INERTIA-SEED]:** The developer assumption that [name the naive assumption commonly made about these limits] fails here because [one sentence linking to cascade mechanism or shared principal pool]."

**PA VALIDATION — ROUND 1 (first barrier):** For each construct in TABLE 1, write one line:
> "[Construct name] — confirmed / corrected to: [X] — because: [one sentence]"

**GATE 1:** All TABLE 1 rows have PA constructs, numeric limits, and Round 1 validation lines. Block: TABLE 2 is blocked until all three conditions are met.

---

### TABLE 2 — RATE LIMIT HIT ORDERING

| Hit order | Tier | Component | PA construct | Limit | Scenario projected volume | Why this order holds at scenario volume |
|-----------|------|-----------|-------------|-------|--------------------------|------------------------------------------|
| 1 (bottleneck) | | | | | | |
| 2 | | | | | | |

Rule: "Why this order holds" must explain the ordering at aggregate volume — not reproduce limits in ascending order.

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

### USER EXPERIENCE MAP

*Placed before cascade analysis: per-tier UX is determined by the throttle tier structure in TABLE 1 and TABLE 2. Cascade analysis that follows may intensify UX effects but does not change per-tier UX category.*

For each tier in TABLE 1:
> "Tier [N]: User sees/experiences: [specific description] — UX category: [transparent retry / visible delay / error surfaced to user / silent data loss]"

Rule: Categories must differ across tiers. State what the user sees, not what the system does internally.

---

### TABLE 5 — CASCADE SEQUENCE

| Step | Component | Action | Causal mechanism | Load added to next tier (estimate) | Failure mode | Duration |
|------|-----------|--------|-----------------|-------------------------------------|--------------|----------|
| 1 | | throttles | | | brownout / full stop / partial data | |
| 2 | | throttles (cascade) | | | | |

**Cascade resolution statement (required):** "The cascade above resolves [INERTIA-SEED] because [one sentence showing how the causal chain proves the assumption false — cite [INERTIA-SEED] by label]."

**GATE 3:** Steps 1 and 2 must be filled and the cascade resolution statement must cite [INERTIA-SEED] by label. Block: RETRY-AFTER GAPS is blocked until this condition is met.

---

### RETRY-AFTER GAPS

For each consumer in TABLE 1 where Retry-After is published:
> "Consumer: [name] — Current behavior: [what it does on 429] — Retry-After header read?: [yes / no] — Consequence: [hammering / premature retry / extended outage / none]"

---

### TABLE 6 — QUANTIFIED RISK REGISTER

| Tier | PA construct | Limit | Projected scenario volume | Status (SAFE / MARGINAL / OVER-LIMIT) | Headroom (+) or deficit (-) |
|------|-------------|-------|--------------------------|---------------------------------------|------------------------------|
| | | | | | |

All tiers from TABLE 1 must appear. Status derived from numeric comparison only.

---

### PA-SPECIFIC REMEDIATIONS

At least two. Each must name an exact PA feature or setting. "Add retries" and "reduce load" do not count.

| Finding addressed (cite TABLE/section) | PA feature (exact name) | Configuration | Effect |
|----------------------------------------|------------------------|---------------|--------|
| | | | |
| | | | |

---

**PRE-EVALUATION PREAMBLE (before Round 2 construct evaluation begins)**

**Independence:** Do not assume Round 1 was accurate because constructs appeared to validate without correction. Round 1's confidence is not evidence of Round 1's precision. Treat all Round 1 construct names as unverified at the start of this pass. This directive is active before any construct appears in the validation lines below.

**Scope extension:** Round 2 covers construct categories that Round 1's execution window excluded by construction. Round 1's construct-definition window closed at TABLE 1 validation time. The sections that followed introduced construct references not present within Round 1's window — propagation signal types in TABLE 3, cascade mechanism labels in TABLE 5 — after Round 1's window had already closed. Those populations could not have been reviewed by Round 1 regardless of how thoroughly Round 1 performed its analysis. Two populations require independent review: (a) propagation signal types and protocol names from TABLE 3 — introduced after Round 1's window closed; (b) cascade mechanism labels and failure-mode constructs from TABLE 5 — introduced after Round 1's window closed.

**PA VALIDATION — ROUND 2**

Review all PA constructs used in this output. Write one line per construct:
> "[Construct] — confirmed / corrected to: [X] — reason: [one sentence]"

Batch confirmation does not count. Each construct requires its own line.

---

## V-04 — Combined: C-21 + C-22 + Formal Register

**Variation axis:** C-21 + C-22 combined; phrasing register = formal/technical
**Hypothesis:** "SECOND BARRIER — PRE-EVALUATION PREAMBLE (before any construct evaluation begins)" with explicit `Independence:` / `Scope extension:` labeled directives in formal technical language satisfies C-21 (positional qualifier in container name) and C-22 (labeled pair in pre-barrier position). Phrasing register is orthogonal to structural criteria — formal language does not suppress or elevate any score. Predicted: 136/136.
**Base:** Table-based single-LLM structure. Full R4 ceiling (130) carried forward. Both new criteria satisfied by the pre-barrier block design.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across the rate-limited system described in this scenario. All comparative, ordered, or enumerated analysis must appear in the pre-printed tables specified below. Column-level structure in tables enforces precision requirements that prose cannot satisfy.

**Scenario:** [Insert scenario here]

**Domain rule:** All construct names must conform to exact Power Automate and Connectors platform terminology. Valid constructs: Power Platform request entitlements, connector throttling policies, flow run concurrency limits, action call limits, premium vs. standard connector tiers, Microsoft 365 service protection limits. A generic HTTP 429 reference without an associated PA construct name does not satisfy domain grounding requirements.

**Output structure:** Six required analysis tables plus supporting sections. Every table row must be populated or explicitly marked "None identified." Partial row completion does not satisfy the row requirement.

---

### TABLE 1 — THROTTLE TIER MAP

| Tier | Component | PA construct (exact) | Limit (req/unit-time) | Consumer(s) | Retry-After published? |
|------|-----------|---------------------|-----------------------|-------------|------------------------|
| 1 (bottleneck) | | | | | |
| 2 | | | | | |
| 3 (if applicable) | | | | | |

Aggregate scenario request volume: **[N req/unit-time]**

**Bottleneck statement:** Construct this statement before proceeding to TABLE 2:
> "The component [name] at [PA construct] constitutes the binding bottleneck. It reaches saturation at [N req/unit-time] under the described scenario because [reason the aggregate volume exceeds this tier before any other]. **[INERTIA-SEED]:** The assumption that [name the independence or additive assumption commonly applied to these rate limits] is invalidated by this scenario because [one sentence identifying the structural property — shared principal pool, coupled tier dependencies, or volume topology — that refutes the assumption]."

**PA VALIDATION — ROUND 1 (first barrier):** For each construct enumerated in TABLE 1, produce one validation line:
> "[Construct name] — confirmed / corrected to: [X] — rationale: [one sentence identifying why this term is the correct Power Automate platform construct]"

**GATE 1:** All TABLE 1 rows must carry (a) an exact PA construct name, (b) a numeric limit with unit of time, and (c) a corresponding Round 1 validation line. Block: TABLE 2 is blocked until all three conditions are satisfied for every row.

---

### TABLE 2 — RATE LIMIT HIT ORDERING

| Hit order | Tier | Component | PA construct | Limit | Scenario projected volume | Ordering rationale at scenario volume |
|-----------|------|-----------|-------------|-------|--------------------------|----------------------------------------|
| 1 (bottleneck) | | | | | | |
| 2 | | | | | | |

Constraint: The ordering rationale must explain why each tier reaches its limit in the stated sequence given the aggregate request volume. Reproducing limits in ascending order without volumetric justification does not satisfy this constraint.

---

### TABLE 3 — BACKPRESSURE HOP CHAIN

| Hop | Originating component | Signal emitted | Signal classification | Receiving component | Behavioral response |
|-----|-----------------------|----------------|----------------------|---------------------|---------------------|
| 1 | | | error code / retry-after header / queue depth / other | | |
| 2 | | | | | |

Extend rows until the propagation chain reaches the terminal state or caller boundary.

---

### TABLE 4 — BURST PATH ENUMERATION

| Path | PA flow construct (exact) | Location in flow | Estimated peak rate (req/unit-time) | Bypass mechanism |
|------|--------------------------|-----------------|--------------------------------------|------------------|
| | | | | |

If no burst paths are identified: record "None identified. Active guards:" in the path cell and enumerate the active protective controls.

---

### TABLE 5 — CASCADE SEQUENCE

| Step | Component | Action | Causal mechanism | Incremental load on subsequent tier (estimate) | Failure classification | Duration |
|------|-----------|--------|-----------------|------------------------------------------------|------------------------|----------|
| 1 | | throttles | | | brownout / full stop / partial data | |
| 2 | | throttles (cascade) | | | | |

**Cascade resolution statement:** Required; must cite [INERTIA-SEED] by label:
> "The cascade sequence above resolves [INERTIA-SEED] by demonstrating that [one sentence establishing the causal relationship between the identified coupling mechanism and the failure of the stated assumption]."

**GATE 3:** Both cascade steps must be populated and the cascade resolution statement must cite [INERTIA-SEED] by label. Block: USER EXPERIENCE MAP is blocked until this condition is satisfied.

---

### USER EXPERIENCE MAP

For each tier enumerated in TABLE 1, produce one entry:
> "Tier [N]: User-observable condition: [specific description of what the user encounters] — UX classification: [transparent retry / visible delay / error surfaced to user / silent data loss]"

Constraint: UX classifications must be distinct across tiers. Characterize user-observable conditions, not internal system states.

---

### RETRY-AFTER GAP ANALYSIS

For each consumer in TABLE 1 where Retry-After publication status is "yes," produce one entry:
> "Consumer: [name] — Observed behavior on HTTP 429: [description] — Retry-After header consumed?: [yes / no] — Consequence classification: [hammering / premature retry / extended outage / none]"

---

### TABLE 6 — QUANTIFIED RISK REGISTER

| Tier | PA construct | Defined limit | Projected scenario volume | Risk status (SAFE / MARGINAL / OVER-LIMIT) | Margin: headroom (+) or deficit (-) |
|------|-------------|---------------|--------------------------|---------------------------------------------|--------------------------------------|
| | | | | | |

All tiers from TABLE 1 must appear. Risk status must be derived from direct numeric comparison — qualitative estimation is not permitted.

---

### PA-SPECIFIC REMEDIATIONS

Minimum of two entries. Each entry must reference an exact Power Automate feature name or configuration setting. Non-specific recommendations do not satisfy this requirement.

| Finding (cite TABLE or section) | PA feature (exact name) | Configuration specification | Projected effect |
|---------------------------------|------------------------|----------------------------|-----------------|
| | | | |
| | | | |

---

**SECOND BARRIER — PRE-EVALUATION PREAMBLE (before any construct evaluation begins)**

**Independence:** The non-deference directive is active before any construct appears in the Round 2 validation lines that follow. Do not assume that Round 1 validation accuracy is established by Round 1's apparent construct confidence. Round 1's output confidence is not evidence of Round 1's construct precision. All Round 1 construct names are to be treated as unverified at the commencement of this evaluation pass, irrespective of whether Round 1 flagged uncertainty.

**Scope extension:** Round 2 covers three construct populations that were structurally outside Round 1's execution window. Round 1's construct-definition window closed upon completion of TABLE 1 validation. The sections that executed subsequent to that closure — TABLE 2 through TABLE 5 — introduced construct references that were not present within Round 1's execution scope and therefore could not have been evaluated by Round 1 regardless of thoroughness. The three populations requiring independent evaluation in this pass: (a) tier-map and hit-ordering constructs from TABLE 1 and TABLE 2, re-evaluated independently of Round 1's confidence; (b) propagation signal types and protocol references introduced in TABLE 3 — introduced after Round 1's window closed; (c) cascade mechanism labels and failure-mode constructs introduced in TABLE 5 — introduced after Round 1's window closed. Populations (b) and (c) must not be treated as reviewed by Round 1.

**PA VALIDATION — ROUND 2**

For every PA construct referenced in this output, produce one validation entry:
> "[Construct name] — confirmed / corrected to: [X] — rationale: [one sentence establishing correctness in PA runtime context]"

Per-construct entries are required. Batch confirmation does not satisfy this requirement.

---

## V-05 — Combined: C-21 + C-22 + Inertia Framing Prominent + Conversational Register

**Variation axis:** C-21 + C-22 combined; inertia framing prominent throughout; phrasing register = conversational/imperative
**Hypothesis:** Developer-framed inertia assumption named in the opening, tracked through each section with [INERTIA-SEED] label, resolved explicitly in the cascade section — tests whether prominent inertia framing affects any existing criterion while C-21 and C-22 are satisfied via "PRE-ANALYSIS ASSERTION (before any Round 2 evaluation begins)" with labeled pair. Inertia framing and conversational register are content/style axes, not structural axes — both should be orthogonal to all criteria. Predicted: 136/136.
**Base:** Two-role structure (R4 V-05 skeleton). Inertia assumption given visible framing from the opening statement forward.

---

Most flow developers building multi-connector automations assume rate limits are independent — saturating the connector tier has no effect on the platform entitlement tier, and vice versa. This scenario tests that assumption directly. Your task: find where it breaks, trace how the failure propagates, and quantify the damage.

You are a Connectors / Power Automate throughput domain expert. Work through this scenario in two roles sequentially.

**Scenario:** [Insert scenario here]

**Ground rule:** Every construct name must be exact PA or Connectors platform terminology. Valid constructs: Power Platform request entitlements, connector throttling policies, flow run concurrency limits, action call limits, premium vs. standard connector tiers, Microsoft 365 service protection limits. "HTTP 429" alone doesn't count — name the PA construct that produced it.

---

## ROLE 1 — CONNECTORS THROUGHPUT EXPERT

Start by mapping every rate-limiting component. Then find which one breaks first. Then trace the damage.

### 1.1 — MAP THE RATE-LIMITING COMPONENTS

| Component | PA construct (exact, or flag with ?) | Limit (req/unit-time) | Volume share of total scenario requests | Retry-After published? |
|-----------|---------------------------------------|----------------------|-----------------------------------------|------------------------|
| | | | | |

Total scenario request volume: **[N req/unit-time]**

**GATE 1:** Every row needs a named PA construct (or ? flag), a numeric limit, and a volume share. Flag anything uncertain for ROLE 2 to correct. Block: 1.2 is blocked until every row is complete.

### 1.2 — NAME THE BOTTLENECK AND PLANT THE INERTIA SEED

Write this statement — it anchors the cascade analysis in section 1.5:
> "[Component] at [PA construct] hits its limit first. It saturates at [N req/unit-time] because [one sentence on why this tier saturates before the others at this volume]. **[INERTIA-SEED]:** The standard developer assumption — that [name the specific independence or isolation assumption developers make about these limits] — breaks here because [one sentence on the structural property of this scenario that makes the assumption false]."

Then rank every tier in the order it will saturate:

| Hit order | Tier | Component | PA construct | Limit | Why it hits at this position given total volume |
|-----------|------|-----------|-------------|-------|-------------------------------------------------|
| 1 (bottleneck) | | | | | |
| 2 | | | | | |

Don't just list limits in ascending order — explain the ordering given the actual volume.

**PA VALIDATION — ROUND 1 (first barrier):** For each construct in 1.1, one line:
> "[Construct name] — confirmed / corrected to: [X] — because: [one sentence]"

**GATE 1B:** All Round 1 validation lines present. Block: 1.3 is blocked until complete.

### 1.3 — TRACE HOW THE THROTTLE SIGNAL TRAVELS

From the bottleneck outward, hop by hop:

| Hop | From | Signal sent | Signal type | To | What happens |
|-----|------|-------------|-------------|-----|--------------|
| 1 | | | error code / retry-after header / queue depth / other | | |
| 2 | | | | | |

Keep going until you reach the caller or a terminal state.

### 1.4 — FIND THE UNPROTECTED BURST PATHS

Where can volume spike past the tier-1 guard?

| Path | PA construct (exact) | Where in the flow | Peak burst rate | Why the guard doesn't stop it |
|------|---------------------|-------------------|----------------|-------------------------------|
| | | | | |

If there are none: "No burst paths. Active guards: [list]."

### 1.5 — CASCADE: WHERE [INERTIA-SEED] BREAKS

Saturation at Tier 1 doesn't stay isolated — show how it multiplies through the system. Start by naming what [INERTIA-SEED] gets wrong:
> "The [INERTIA-SEED] assumption fails here because: [one sentence naming the coupling mechanism — shared pool, entitlement bleed, retry amplification, or similar — that connects the tiers]."

| Step | Component | What happens | Why (causal mechanism) | Extra load on next tier | How it manifests | Duration |
|------|-----------|-------------|------------------------|------------------------|-----------------|----------|
| 1 | | throttles | | | brownout / full stop / partial data | |
| 2 | | throttles (cascade) | | | | |

This section must cite [INERTIA-SEED] by label and prove the assumption false from the cascade structure.

---

## ROLE 2 — POWER AUTOMATE PLATFORM EXPERT

You're reviewing ROLE 1's work from a PA platform perspective — not as a Connectors generalist, but as someone who knows the exact PA runtime behavior for every construct ROLE 1 named. Your validation table is the **second barrier** on construct accuracy.

**PRE-ANALYSIS ASSERTION (before any Round 2 evaluation begins)**

**Independence:** Start by treating every construct ROLE 1 named as unverified. ROLE 1 may have expressed no uncertainty — that is not evidence of accuracy from a PA runtime platform perspective. Do not carry ROLE 1's confidence forward into this evaluation. This directive is active before any construct appears in section 2.1 below.

**Scope extension:** This validation pass covers more ground than ROLE 1's execution window could. ROLE 1's construct-definition window closed when section 1.2 completed — the point at which ROLE 1 finished defining tier-map and hit-ordering constructs. Everything after that (sections 1.3, 1.4, 1.5) introduced new construct references after ROLE 1's window had already closed: propagation signal types in 1.3, burst construct names in 1.4, cascade mechanism labels in 1.5. ROLE 1 could not have reviewed those populations regardless of how careful ROLE 1 was — they were not within scope when ROLE 1's definition window was open. Three populations need independent coverage here: (a) tier-map and hit-ordering constructs from 1.1–1.2, re-evaluated without carrying ROLE 1's confidence; (b) propagation signal types and protocol names from 1.3 — introduced after ROLE 1's window closed; (c) cascade mechanism labels and failure-mode constructs from 1.5 — introduced after ROLE 1's window closed.

### 2.1 — VALIDATE EVERY CONSTRUCT ROLE 1 USED (second barrier)

One line per construct — no batch confirmations.

| Construct as ROLE 1 wrote it | Where ROLE 1 used it | Your verdict | Correct PA name | Why this is the right name in PA runtime |
|------------------------------|---------------------|-------------|----------------|------------------------------------------|
| | | confirmed / corrected to: | | |

### 2.2 — MAP THE USER EXPERIENCE AT EACH TIER

What does the user actually see? Not what the system does internally — what the user encounters:

| Tier | What PA does at this throttle | What the user experiences (specific) | UX category |
|------|-------------------------------|--------------------------------------|-------------|
| Tier 1 | | | transparent retry / visible delay / error surfaced / silent data loss |
| Tier 2 | | | (must differ from Tier 1) |

Different tiers must produce different UX categories.

### 2.3 — RETRY-AFTER: IS ANYONE READING IT?

For each tier where Retry-After is published:
> "Tier [N] — What the consumer does on 429: [description] — Reads Retry-After?: [yes / no] — Consequence if no: [hammering / premature retry / extended outage / none]"

### 2.4 — QUANTIFY THE RISK AT EACH TIER

Numbers only — no qualitative estimates:

| Tier | PA construct (your validated name) | Limit | Volume hitting this tier | Status (SAFE / MARGINAL / OVER-LIMIT) | Margin |
|------|------------------------------------|-------|-------------------------|---------------------------------------|--------|
| | | | | | |

### 2.5 — FIX IT: PA-SPECIFIC REMEDIATIONS

Two minimum. Every remediation must name an exact PA feature or setting. "Add retries" and "reduce load" don't count.

| What you're fixing (cite section) | PA feature (exact name) | How to configure it | What it changes |
|-----------------------------------|------------------------|---------------------|-----------------|
| | | | |
| | | | |

**Platform angle:** Go beyond ROLE 1's Connectors view — per-connection request entitlements, environment-level request allocation, service principal pooling, premium connector tier upgrades, M365 service protection exemption paths.