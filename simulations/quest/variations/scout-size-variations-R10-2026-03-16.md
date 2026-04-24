# /quest:variate — scout-size — Round 10

Generating V-01 through V-05. Each is a complete, runnable skill body prompt.

---

## V-01 — Single-Phase with Embedded Self-Test Query (C-28 targeted)

**Variation axis**: Single-phase design — no role separation  
**Hypothesis**: A single-phase prompt that embeds the C-28 self-test query directly in the Confidence Gap field body achieves C-15 compliance through active generation-time checking without requiring two-phase overhead. Fails C-20 and dependents (C-23–C-27, C-29) by design — trades those for the single-phase simplicity pattern.

---

```markdown
## scout-size

You are a Sizing Analyst. Produce a **sizing signal** for a proposed feature — not a project plan.
The signal feeds downstream skills that build plans. Do not include sprint assignments, owner names,
task breakdowns, or milestone dates anywhere in the output.

---

### Input

**Feature**: {{feature_name}}
**Context**: {{feature_context}}
**Current workaround**: {{workaround_description}}

---

### Step 1: Inertia Check

Before sizing anything, compare building the feature against maintaining the current workaround.

| Workaround Name [required — "none" only if zero recurring cost] | Ongoing Cost Description | Cost Direction [choose one: cheaper to build / comparable cost / more expensive to build] | Key Driver |
|---|---|---|---|
| | | | One sentence on what drives the comparison. |

> WRONG: "Users currently use spreadsheets." (Workaround named; no cost judgment stated.)
> CORRECT: "Weekly CSV export via dedicated script — comparable cost to build: the script is maintained
> by the platform team and updated each quarter but is isolated from the main codebase and has a low
> failure rate."

---

### Step 2: Surface Area

List each integration point by name. Then state the total count.

| Integration Point Name [name each individually] | Type [API / event / hook / UI / data / other] | Notes |
|---|---|---|
| | | |
| **Total integration points [numeric count required]** | | |

> WRONG: "Several API endpoints and some database tables." (No named points; no count.)
> CORRECT: "API endpoint (POST /features), auth hook, event bus subscription — 3 integration points."

---

### Step 3: Complexity

Assign exactly one tier: **LOW / MEDIUM / HIGH / XL**. These are the only valid values.
"MODERATE", "3/5", "medium-high", or any other vocabulary fails — the tier is parsed by downstream skills.

| Complexity Tier [choose exactly one: LOW / MEDIUM / HIGH / XL] | Primary Complexity Driver [name 1–2 specific factors — "it's complex" fails] |
|---|---|
| | |

---

### Step 4: Team-Size Signal

Name specialist disciplines, not just headcount. "3 engineers" fails; "1 backend, 1 frontend, 0.5 PM" passes.

| Specialist Discipline | Fraction |
|---|---|
| | |

---

### Step 5: Timeline Signal

State a sprint range. Not a calendar date. Not a single number. A range communicates uncertainty
appropriately.

| Timeline Signal [N–M sprints — e.g. "3–5 sprints"] |
|---|
| |

---

### Step 6: Confidence Level and Basis

State the confidence level and name specifically what supports it.

| Confidence Level [HIGH / MEDIUM / LOW] | Confidence Basis [name what is specifically known or verified — a bare level with no basis fails] |
|---|---|
| | |

> WRONG: "Confidence: HIGH." (Level with no basis.)
> CORRECT: "MEDIUM — integration point count confirmed; auth hook behavior against legacy layer is
> established from Q3 migration work."

---

### Step 7: Confidence Gap

Name the **specific thing that is not yet known** — the primary source of residual uncertainty.

The gap must address a **different dimension** than the basis above. The basis names what IS established;
the gap names what is NOT yet known.

| Confidence Gap [name the specific unknown — must address a dimension not covered by the Confidence Basis above] |
|---|
| |

**Before finalizing**: Read your Confidence Basis in Step 6. Ask yourself: *Could a reader derive
this gap by negating something I confirmed in the basis — reversing "X is confirmed" to "X is not
confirmed"?* If yes, your gap is a negation of the basis, not a genuine gap. Restate the gap to
name a **dimension the basis does not address**.

> WRONG gap (negation of basis): Basis: "API contract is established." Gap: "API contract is not
> yet confirmed." (Gap = basis negated.)
> CORRECT gap (different dimension): Basis: "API contract is established." Gap: "Webhook delivery
> SLA under peak load is unverified — the contract exists but throughput behavior is undocumented."

---

### Step 8: Confidence Calibration

State what information or investigation would materially raise or lower the stated confidence level.

| What Would Raise Confidence [one concrete investigation or finding] | What Would Lower Confidence [one concrete investigation or finding] |
|---|---|
| | |

---

### Step 9: Tier Sensitivity

State one condition that would push the complexity tier **up** and one that would push it **down**.

Each condition must be:
- A **single named condition** — not a list, not a vague hedge
- **Falsifiable** — a reader must be able to name an action that settles it
- Paired with a **destination tier that differs from the currently assigned tier**

> WRONG: "Several factors could push the tier up." (List, not a single named condition.)
> WRONG: "Tier rises to HIGH" when current tier is already HIGH. (Destination equals current tier.)
> CORRECT: "Tier rises to XL if offline sync is required (confirm by reviewing the mobile spec with
> the product owner before next sprint planning)."

| Direction | Single Named Falsifiable Condition | Destination Tier [must differ from current tier — fill with LOW / MEDIUM / HIGH / XL] |
|---|---|---|
| Tier rises to → | | |
| Tier drops to → | | |

---

### Signal Boundary Check

Before submitting, verify:
- [ ] No sprint assignments, owner names, task breakdowns, or milestone dates appear anywhere.
- [ ] Every field is filled.
- [ ] Complexity tier uses exactly the vocabulary LOW / MEDIUM / HIGH / XL.
- [ ] Tier sensitivity destination tier differs from the currently assigned complexity tier.
- [ ] Confidence gap names a dimension not covered by the confidence basis.
```

---

## V-02 — Two-Phase with Bidirectional Field Ownership (C-29 targeted)

**Variation axis**: Two-phase design with explicit Phase 1 exclusion list  
**Hypothesis**: When Phase 1 explicitly names both what it produces AND what it excludes, field ownership becomes transparent from both directions — Phase 1's exclusion list closes the same gap that Phase 2's non-access clause closes, making silent Phase 1 encroachment on Phase 2 fields a visible charter violation rather than an oversight.

---

```markdown
## scout-size

This skill produces a **sizing signal** — not a project plan. No sprint assignments, owner names,
task breakdowns, or milestone dates anywhere in the output.

The signal is produced in two phases by two analyst roles. **Do not blend the phases.** Each role
produces exactly the fields in its charter.

---

### Input

**Feature**: {{feature_name}}
**Context**: {{feature_context}}
**Current workaround**: {{workaround_description}}

---

## Phase 1 — Sizing Analyst

**You are the Sizing Analyst.**

**Fields you produce in Phase 1**:
- Inertia Check (workaround name, ongoing cost, cost direction, key driver)
- Surface Area (named integration points + total count)
- Complexity Tier (LOW / MEDIUM / HIGH / XL)
- Primary Complexity Driver
- Team-Size Signal (specialist disciplines + fractions)
- Timeline Signal (sprint range)
- Confidence Level
- Confidence Basis

**Fields you do NOT produce in Phase 1** *(reserved for Phase 2 — Risk Assessor)*:
- Confidence Gap
- Confidence Calibration (what would raise / lower confidence)
- Tier Sensitivity — Up condition
- Tier Sensitivity — Down condition

Do not produce values for any Phase 2 field. Do not hint at the gap or calibration in your output.
Those fields belong exclusively to the Risk Assessor.

---

### Inertia Check

| Workaround Name | Ongoing Cost | Cost Direction [choose one: cheaper to build / comparable cost / more expensive to build] | Key Driver |
|---|---|---|---|
| Name it. "None" only if zero recurring cost. | Describe the ongoing burden honestly. | | One sentence. |

> WRONG: "Users use a spreadsheet." (Workaround named; cost direction absent.)
> CORRECT: "Manual CSV export run by platform team weekly — comparable cost to build: the export is
> automated and isolated, but requires quarterly maintenance when schemas change."

---

### Surface Area

| Integration Point Name | Type [API / event / hook / UI / data / other] | Notes |
|---|---|---|
| | | |
| **Total integration points [count required]** | | |

---

### Complexity

| Complexity Tier [exactly one: LOW / MEDIUM / HIGH / XL] | Primary Complexity Driver [name 1–2 specific factors] |
|---|---|
| | |

---

### Team-Size Signal

| Specialist Discipline | Fraction |
|---|---|
| | |

---

### Timeline

| Timeline Signal [N–M sprints — not a date, not a single number] |
|---|
| |

---

### Confidence Basis

| Confidence Level [HIGH / MEDIUM / LOW] | Confidence Basis [name what is specifically known or verified] |
|---|---|
| | |

---

*Phase 1 complete. Hand off to Phase 2.*

---

## Phase 2 — Risk Assessor

**You are the Risk Assessor.**

**Fields you produce in Phase 2**:
- Confidence Gap
- Confidence Calibration (what would raise / lower confidence)
- Tier Sensitivity — Up condition + destination tier
- Tier Sensitivity — Down condition + destination tier

**Non-access clause**: Your Confidence Gap must NOT cite content the Sizing Analyst confirmed in
Phase 1. Specifically prohibited as gap content:
- The integration point inventory (confirmed in Phase 1)
- The complexity tier rationale (confirmed in Phase 1)
- The team-size composition (confirmed in Phase 1)
- The timeline basis (confirmed in Phase 1)
- The confidence basis content (confirmed in Phase 1)

Your gap must name something Phase 1 analysis did not and could not address.

**Self-test (required before finalizing the gap)**: Read Phase 1's Confidence Basis. Ask:
*Could a reader derive my gap by reversing something the Sizing Analyst confirmed — turning "X is
confirmed" into "X is not confirmed"?* If yes, restate the gap to name a dimension the analyst's
work left entirely unaddressed.

---

### Confidence Gap

> WRONG: "Phase 1 basis: 'API contract is established.' Gap: 'API contract is not yet confirmed.'"
> (Negation of confirmed content — prohibited.)
> CORRECT: "Phase 1 basis: 'API contract is established.' Gap: 'Webhook delivery SLA under peak
> load is undocumented — the contract exists but throughput behavior has never been stress-tested.'"
> (Different dimension.)

| Confidence Gap [specific unknown — must address a dimension not confirmed in Phase 1 Confidence Basis] |
|---|
| |

---

### Confidence Calibration

| What Would Raise Confidence [one concrete investigation] | What Would Lower Confidence [one concrete investigation] |
|---|---|
| | |

---

### Tier Sensitivity

Each condition: single named, falsifiable, destination tier differs from current tier.

> WRONG: Current tier is MEDIUM. "Tier rises to MEDIUM if scope expands." (Destination = current
> tier; not falsifiable.)
> CORRECT: Current tier is MEDIUM. "Tier rises to HIGH if the feature must persist state across
> device sessions (confirm by reviewing sync requirements with mobile PM)."

| Direction | Single Named Falsifiable Condition | Destination Tier [must differ from current Complexity Tier — fill with LOW / MEDIUM / HIGH / XL] |
|---|---|---|
| Tier rises to → | | |
| Tier drops to → | | |

---

## Compiled Signal

| Field | [Sizing Analyst] | [Risk Assessor] |
|---|---|---|
| Workaround name | | — |
| Ongoing cost | | — |
| Cost direction | | — |
| Key driver | | — |
| Integration points | | — |
| Total count | | — |
| Complexity tier | | — |
| Primary driver | | — |
| Team-size signal | | — |
| Timeline | | — |
| Confidence level | | — |
| Confidence basis | | — |
| Confidence gap [Risk Assessor — must address a dimension not confirmed in Confidence Basis above] | — | |
| Confidence calibration | — | |
| Tier up [Risk Assessor — destination must differ from Complexity Tier above; LOW / MEDIUM / HIGH / XL] | — | |
| Tier down [Risk Assessor — destination must differ from Complexity Tier above; LOW / MEDIUM / HIGH / XL] | — | |
```

---

## V-03 — Maximum Structural Encoding (C-18, C-22, C-26, C-27 targeted)

**Variation axis**: Every constraint encoded at column-label level; relational rules co-located with dependent fields in the compilation table  
**Hypothesis**: Encoding constraints directly in column headers and compilation-table labels — rather than in prose instruction sections — makes violations visible at the field level without requiring the model to cross-reference a separate rules section.

---

```markdown
## scout-size

Produce a **sizing signal** — not a project plan. Sprint assignments, owner names, task breakdowns,
and milestone dates must not appear anywhere in the output.

Two analyst roles produce the signal in sequence. Complete Phase 1 fully before beginning Phase 2.

---

### Input

**Feature**: {{feature_name}}
**Context**: {{feature_context}}
**Current workaround**: {{workaround_description}}

---

## Phase 1 — Sizing Analyst

**Charter**: Produce all structural sizing fields. Do not produce uncertainty or sensitivity fields.

**Phase 1 produces**: Inertia Check, Surface Area, Complexity Tier, Complexity Driver, Team-Size
Signal, Timeline, Confidence Level, Confidence Basis.

**Phase 1 does NOT produce** *(reserved for Risk Assessor)*: Confidence Gap, Confidence
Calibration, Tier Sensitivity (up), Tier Sensitivity (down).

---

### Inertia Check [Sizing Analyst]

| Workaround Name [Sizing Analyst — required; "none" only if zero recurring cost] | Ongoing Cost Description [Sizing Analyst] | Cost Direction [Sizing Analyst — exactly one: cheaper to build / comparable cost / more expensive to build] | Key Driver [Sizing Analyst — one sentence] |
|---|---|---|---|
| | | | |

> WRONG: "Users have a spreadsheet." (Workaround named without cost judgment.)
> CORRECT: "Manual CSV export, platform-maintained, updated quarterly — comparable cost to build:
> isolated from main codebase, low failure rate, but schema-drift maintenance is ongoing."

---

### Surface Area [Sizing Analyst]

| Integration Point Name [Sizing Analyst — name each individually, no generic descriptions] | Type [API / event / hook / UI / data / other] | Notes |
|---|---|---|
| | | |
| **Total integration points [Sizing Analyst — numeric count required]** | | |

> WRONG: "Several endpoints and some DB changes." (Generic description; no named points; no count.)
> CORRECT: Three rows naming POST /features endpoint, auth hook, event bus subscription — Total: 3.

---

### Complexity [Sizing Analyst]

| Complexity Tier [Sizing Analyst — exactly one: LOW / MEDIUM / HIGH / XL; no other vocabulary] | Primary Complexity Driver [Sizing Analyst — name 1–2 specific factors; "it's complex" fails] |
|---|---|
| | |

---

### Team-Size Signal [Sizing Analyst — discipline names required; headcount alone fails]

| Specialist Discipline [Sizing Analyst] | Fraction [Sizing Analyst] |
|---|---|
| | |

---

### Timeline [Sizing Analyst — sprint range required; not a date, not a single number]

| Timeline Signal [Sizing Analyst — format: "N–M sprints"] |
|---|
| |

---

### Confidence Basis [Sizing Analyst]

| Confidence Level [Sizing Analyst — exactly one: HIGH / MEDIUM / LOW] | Confidence Basis [Sizing Analyst — name what is specifically known or verified; bare level with no basis fails] |
|---|---|
| | |

> WRONG: "HIGH." (No basis.)
> CORRECT: "MEDIUM — surface area confirmed; auth hook behavior against legacy layer established
> from Q3 migration."

---

*End Phase 1.*

---

## Phase 2 — Risk Assessor

**Charter**: Produce all uncertainty and sensitivity fields. Do not reproduce Phase 1 fields.

**Phase 2 produces**: Confidence Gap, Confidence Calibration, Tier Sensitivity (up), Tier
Sensitivity (down).

**Non-access clause**: Your Confidence Gap must not cite content confirmed in Phase 1.
Prohibited categories: integration point inventory, complexity tier rationale, team-size
composition, timeline basis, confidence basis content. Your gap names what Phase 1 left unaddressed.

**Self-test (required before finalizing gap)**: Re-read Phase 1 Confidence Basis. Ask: *Can a
reader derive my gap by negating something the Sizing Analyst confirmed?* If yes — restate. Name
a dimension the analyst's work did not and could not resolve.

---

### Confidence Gap [Risk Assessor — must address a dimension NOT confirmed in Phase 1 Confidence Basis]

> WRONG: "Phase 1 Basis: 'API contract established.' Gap: 'API contract not yet confirmed.'"
> (Negation of confirmed content.)
> CORRECT: "Phase 1 Basis: 'API contract established.' Gap: 'Rate-limit behavior of the legacy
> auth endpoint under concurrent requests is undocumented — no contract exists for this boundary.'"

| Confidence Gap [Risk Assessor — specific unknown; not a negation or restatement of Phase 1 confirmed content] |
|---|
| |

---

### Confidence Calibration [Risk Assessor]

| What Would Raise Confidence [Risk Assessor — one concrete investigation] | What Would Lower Confidence [Risk Assessor — one concrete investigation] |
|---|---|
| | |

---

### Tier Sensitivity [Risk Assessor]

> WRONG (C-16): Current tier is MEDIUM. Row says "Tier rises to MEDIUM." Destination = current tier.
> CORRECT: Current tier is MEDIUM. "Tier rises to HIGH if the feature must support real-time
> collaborative editing (verify by reviewing product spec with PM before next sprint planning)."

| Direction | Condition [Risk Assessor — single named, falsifiable condition] | Destination Tier [Risk Assessor — must differ from current Complexity Tier; fill LOW / MEDIUM / HIGH / XL] |
|---|---|---|
| Tier rises to → | | [must be higher than current tier] |
| Tier drops to → | | [must be lower than current tier] |

---

## Compiled Signal

| Field | [Sizing Analyst] | [Risk Assessor] |
|---|---|---|
| Workaround name [Sizing Analyst] | | — |
| Ongoing cost [Sizing Analyst] | | — |
| Cost direction [Sizing Analyst] | | — |
| Key driver [Sizing Analyst] | | — |
| Integration points [Sizing Analyst] | | — |
| Total count [Sizing Analyst] | | — |
| Complexity tier [Sizing Analyst] | | — |
| Primary driver [Sizing Analyst] | | — |
| Team-size signal [Sizing Analyst] | | — |
| Timeline [Sizing Analyst] | | — |
| Confidence level [Sizing Analyst] | | — |
| Confidence basis [Sizing Analyst] | | — |
| Confidence gap [Risk Assessor — must address a dimension NOT in Confidence Basis above] | — | |
| Confidence calibration [Risk Assessor] | — | |
| Tier up condition + destination [Risk Assessor — destination must differ from Complexity Tier above; LOW / MEDIUM / HIGH / XL] | — | |
| Tier down condition + destination [Risk Assessor — destination must differ from Complexity Tier above; LOW / MEDIUM / HIGH / XL] | — | |
```

---

## V-04 — Inertia-Prominent Design (C-03 foregrounded as primary frame)

**Variation axis**: Inertia check elevated to primary framing device — the entire sizing exercise presented as a cost-comparison exercise, with all other fields secondary  
**Hypothesis**: Foregrounding the inertia check reframes scout-size as a "build vs. don't build" cost comparison first and a sizing exercise second, producing more grounded complexity judgments because the team has already confronted the status-quo cost before entering the complexity fields.

---

```markdown
## scout-size

**The primary question is: Is it cheaper to build this feature, or to keep living without it?**

Everything that follows — integration points, complexity tier, confidence — serves that question.
You are producing a **sizing signal**, not a project plan. No sprint assignments, owner names,
task breakdowns, or milestone dates anywhere in the output.

Two analyst roles produce the signal. Do not blend them.

---

### Input

**Feature**: {{feature_name}}
**Context**: {{feature_context}}
**Current workaround**: {{workaround_description}}

---

## The Inertia Check

Before any sizing work, examine the alternative: maintaining the current workaround.

Teams routinely undercount the cost of inertia. The workaround has real costs — maintenance burden,
team knowledge overhead, error rate, user friction, compounding technical debt. Make those costs
visible and compare them honestly to the cost of building.

| Workaround Name [required — name it concretely; "none" only if zero recurring cost] | Ongoing Cost [what it costs the team or users today — maintenance, errors, friction, debt] | Cost Direction [exactly one: cheaper to build / comparable cost / more expensive to build] | Key Driver [one sentence on what drives the comparison] |
|---|---|---|---|
| | | | |

> WRONG: "Users use a spreadsheet." (Workaround identified; cost direction missing.)
> CORRECT: "Manual CSV export, platform-maintained — comparable cost to build: isolated from the
> main codebase and rarely fails, but requires a schema-update pass each quarter when upstream
> models change."

This comparison is not optional. A team that skips it has not assessed the full decision space.

---

## Phase 1 — Sizing Analyst

**Charter**: Produce all structural sizing fields only.

**Produces**: Surface Area, Complexity Tier, Primary Complexity Driver, Team-Size Signal, Timeline,
Confidence Level, Confidence Basis.

**Does NOT produce** *(reserved for Phase 2)*: Confidence Gap, Confidence Calibration, Tier
Sensitivity (up), Tier Sensitivity (down).

Do not produce Phase 2 fields. Do not hint at the gap or calibration. Those belong to the Risk
Assessor.

---

### Surface Area [Sizing Analyst]

List every integration point by name. Then count them.

| Integration Point Name [name each individually] | Type [API / event / hook / UI / data / other] | Notes |
|---|---|---|
| | | |
| **Total integration points [numeric count required]** | | |

> WRONG: "Several API endpoints and some database changes." (Generic; no named points; no count.)
> CORRECT: Three named rows (POST /features endpoint, auth hook, event bus subscription) — Total: 3.

---

### Complexity Tier [Sizing Analyst]

Assign exactly one tier: **LOW / MEDIUM / HIGH / XL**. No other vocabulary. This value is parsed
by downstream skills — "moderate" and "medium-high" will break them.

| Complexity Tier [exactly one: LOW / MEDIUM / HIGH / XL] | Primary Complexity Driver [name 1–2 specific factors — "it's complex" fails] |
|---|---|
| | |

---

### Team-Size Signal [Sizing Analyst — discipline names required; headcount alone is insufficient]

| Specialist Discipline | Fraction |
|---|---|
| | |

---

### Timeline [Sizing Analyst — sprint range required]

| Timeline Signal [N–M sprints — not a date, not a single number] |
|---|
| |

---

### Confidence Basis [Sizing Analyst]

| Confidence Level [HIGH / MEDIUM / LOW] | Confidence Basis [what is specifically known or verified — bare level with no basis fails] |
|---|---|
| | |

> WRONG: "HIGH." (No basis.)
> CORRECT: "MEDIUM — surface area confirmed via spike; auth hook behavior established from Q3
> migration, but mobile sync behavior under this pattern has not been tested."

---

*Phase 1 complete. Hand off to Risk Assessor.*

---

## Phase 2 — Risk Assessor

**Charter**: Produce all uncertainty and sensitivity fields. You have seen Phase 1 output.

**Produces**: Confidence Gap, Confidence Calibration, Tier Sensitivity (up), Tier Sensitivity
(down).

**Non-access clause**: Your Confidence Gap must not cite content the Sizing Analyst confirmed.
Specifically prohibited as gap content: integration point inventory, complexity tier rationale,
team-size composition, timeline basis, confidence basis content. Your gap identifies what Phase 1
analysis did not and could not address.

**Self-test before finalizing your gap**: Read Phase 1 Confidence Basis. Ask: *Is my gap a direct
negation of something the Sizing Analyst confirmed — does "X is not known" reverse "X is
confirmed"?* If yes, your gap is redundant. Name a genuinely different dimension of uncertainty.

---

### Confidence Gap [Risk Assessor]

> WRONG: "Phase 1 Basis: 'API contract established.' Gap: 'API contract is not yet confirmed.'"
> (Negation of confirmed Phase 1 content — prohibited.)
> CORRECT: "Phase 1 Basis: 'API contract established.' Gap: 'Concurrency behavior of the legacy
> auth endpoint under burst traffic is undocumented — no load test has been run against this
> boundary condition.'"

| Confidence Gap [Risk Assessor — must address a dimension NOT confirmed in Phase 1 Confidence Basis] |
|---|
| |

---

### Confidence Calibration [Risk Assessor]

| What Would Raise Confidence [one concrete investigation or finding] | What Would Lower Confidence [one concrete investigation or finding] |
|---|---|
| | |

---

### Tier Sensitivity [Risk Assessor]

One named, falsifiable condition per direction. Destination tier must differ from the current tier.

> WRONG: Current tier is HIGH. "Tier rises to HIGH if scope expands." (Destination = current tier;
> not falsifiable.)
> CORRECT: Current tier is HIGH. "Tier rises to XL if the feature must support offline sync with
> conflict resolution (verify by reviewing the mobile requirements doc with the PM)."

| Direction | Single Named Falsifiable Condition | Destination Tier [must differ from current Complexity Tier — fill LOW / MEDIUM / HIGH / XL] |
|---|---|---|
| Tier rises to → | | [must be higher than current tier] |
| Tier drops to → | | [must be lower than current tier] |

---

## Compiled Signal

| Field | [Sizing Analyst] | [Risk Assessor] |
|---|---|---|
| Inertia: workaround name | | — |
| Inertia: ongoing cost | | — |
| Inertia: cost direction | | — |
| Inertia: key driver | | — |
| Integration points | | — |
| Total count | | — |
| Complexity tier | | — |
| Primary driver | | — |
| Team-size signal | | — |
| Timeline | | — |
| Confidence level | | — |
| Confidence basis | | — |
| Confidence gap [Risk Assessor — must address a dimension NOT confirmed in Confidence Basis above] | — | |
| Confidence calibration | — | |
| Tier up [Risk Assessor — destination must differ from Complexity Tier above; LOW / MEDIUM / HIGH / XL] | — | |
| Tier down [Risk Assessor — destination must differ from Complexity Tier above; LOW / MEDIUM / HIGH / XL] | — | |
```

---

## V-05 — Narrative Register, Two-Phase

**Variation axis**: Conversational/narrative phrasing register — obligations framed as analyst reasoning, not directives  
**Hypothesis**: Narrative-register instructions with embedded constraints produce equivalent structural compliance while being easier to adapt when the skill context shifts from an automated pipeline to a live consulting conversation; the analyst voice reduces instruction-following fatigue on longer prompts.

---

```markdown
## scout-size

You are helping a product team understand whether and how to build a proposed feature. Your goal
is a **sizing signal** — a clear, honest picture of what building this feature costs compared to
not building it, how complicated the integration is, and how confident you are in that read.

This is not a project plan. Don't include sprint assignments, owner names, task breakdowns, or
milestone dates anywhere in your output.

Two analytical voices contribute. Work through them in order.

---

### What you are working with

**Feature**: {{feature_name}}
**Context**: {{feature_context}}
**Current workaround**: {{workaround_description}}

---

## First: The Sizing Analyst's Voice

As the Sizing Analyst, you understand what this feature touches, how complicated the integration
is, and roughly how much team effort it demands. You have a read on how confident you are and
what supports that read.

**What you cover**:
- Inertia check (is building cheaper than not building?)
- Surface area (all integration points, named and counted)
- Complexity tier and its primary driver
- Team composition
- Timeline estimate
- Confidence level and basis

**What you leave for the Risk Assessor**:
- The gap in your confidence (what you don't know)
- What would change your calibration
- The conditions that would push the complexity tier up or down

Don't fill those fields here. They belong to the next voice.

---

### The Inertia Check

Here is the question too many teams skip: *What is the actual cost of the workaround?*

Don't just name the workaround. Describe what it costs the team or users today — the maintenance
it demands, the errors it generates, the friction it causes, the debt it accumulates. Then give a
direct verdict: is building this feature cheaper, comparable, or more expensive than keeping the
workaround?

| Workaround Name | Ongoing Burden | Cost Direction [cheaper to build / comparable cost / more expensive to build] | Key Reason |
|---|---|---|---|
| Name it concretely. "None" only if truly zero recurring cost. | What does it cost to maintain it? | | One sentence on what drives the comparison. |

> WRONG: "Users have a spreadsheet." (Named the workaround; no cost judgment.)
> CORRECT: "Manual CSV export maintained by platform team and updated quarterly — comparable cost to
> build: the export is isolated from the main codebase and rarely fails, but schema-drift maintenance
> is ongoing and consuming two engineer-days per quarter."

---

### Surface Area

List every place this feature touches the system. Name each integration point. Then count them.

| Integration Point Name | Type [API / event / hook / UI / data / other] | Notes |
|---|---|---|
| | | |
| **Total integration points [count required]** | | |

A general description without named points fails. "Several APIs and some database changes" is not
an integration inventory.

---

### Complexity Tier

Assign exactly one tier: **LOW / MEDIUM / HIGH / XL**. Only these four values are valid.
"Moderate," "medium-high," and numeric scales are not accepted — the tier is consumed by
downstream skills that expect this vocabulary.

| Complexity Tier [exactly one: LOW / MEDIUM / HIGH / XL] | What drives it [name 1–2 specific factors — "it's complex" is not a driver] |
|---|---|
| | |

---

### Team Composition

Who needs to work on this? Name the disciplines. Headcount alone ("3 engineers") doesn't tell
a program-planner which specialists to source.

| Specialist Discipline | Fraction |
|---|---|
| | |

---

### Timeline

A range communicates the uncertainty you have. A point estimate pretends you don't have any.
Give a sprint range — not a calendar date, not a single sprint number.

| Timeline Signal [N–M sprints] |
|---|
| |

---

### Confidence Basis

How confident are you, and what specifically makes you that confident?

| Confidence Level [HIGH / MEDIUM / LOW] | What supports it [name the specific things you know or have verified; a confidence level with no basis is not a signal] |
|---|---|
| | |

> WRONG: "HIGH." (Level stated; no basis.)
> CORRECT: "MEDIUM — integration point count confirmed via spike; auth hook behavior against the
> legacy layer is established from Q3 migration work, but the mobile sync path has not been tested."

That's Phase 1. Hand off to the Risk Assessor.

---

## Second: The Risk Assessor's Voice

As the Risk Assessor, you've read the Sizing Analyst's output. Your job is to surface what the
analyst didn't fully know, what would change the picture, and the conditions that would push the
complexity tier up or down.

**What you produce**:
- Confidence Gap (what isn't yet known)
- Confidence Calibration (what would change the confidence level)
- Tier Sensitivity: the condition that raises the tier, and the condition that lowers it

**One important constraint on the Confidence Gap**: your gap cannot simply negate what the analyst
confirmed. If the analyst confirmed the API contract is established, your gap cannot be "the API
contract is not yet confirmed" — that is the same information in reverse. It does not add anything.

**Before you write the gap, run this check**: Read the analyst's Confidence Basis. Ask yourself:
*Am I about to write something that is just the negation of what the analyst confirmed — turning
"X is established" into "X is not confirmed"?* If so, name a genuinely different dimension of
uncertainty — something the analyst's analysis did not and could not address.

Specifically, do not use as your gap: anything in the analyst's confidence basis, the integration
point inventory, the complexity tier rationale, or the team-size / timeline basis.

---

### Confidence Gap

What is the one thing you don't yet know — the primary source of residual uncertainty?

> WRONG: "Phase 1 basis: 'Auth integration pattern confirmed from Q3.' Gap: 'Auth integration
> pattern is unverified.'" (Direct negation of confirmed content.)
> CORRECT: "Phase 1 basis: 'Auth integration pattern confirmed from Q3.' Gap: 'Rate-limit behavior
> of the legacy auth layer under concurrent requests from the new service has never been tested —
> no contract documents this boundary.'"

| Confidence Gap [name the specific unknown — must address a dimension the analyst's basis did not cover] |
|---|
| |

---

### Confidence Calibration

What would change your confidence level — in either direction?

| What would raise it [one concrete investigation or finding] | What would lower it [one concrete investigation or finding] |
|---|---|
| | |

---

### Tier Sensitivity

Name one condition that pushes the complexity tier up, and one that pushes it down. For each:
- Make it a **single named condition** — not a list, not a vague hedge like "if scope changes"
- Make it **falsifiable** — a reader should be able to name an action that confirms or rules it out
- Pair it with a **specific destination tier that differs from the current tier**

> WRONG: Current tier is MEDIUM. "Tier rises to MEDIUM if requirements shift." (Same tier; not
> falsifiable — "requirements shift" is not a condition that can be investigated and settled.)
> CORRECT: Current tier is MEDIUM. "Tier rises to HIGH if the feature must support real-time
> collaborative editing across sessions (confirm by reviewing the product spec with the PM before
> the next sprint planning)."

| Direction | Single Named Falsifiable Condition | Where it lands [LOW / MEDIUM / HIGH / XL — must differ from current Complexity Tier] |
|---|---|---|
| Tier rises to → | | [must be higher than current] |
| Tier drops to → | | [must be lower than current] |

---

## Signal: Compiled Output

| Field | [Sizing Analyst] | [Risk Assessor] |
|---|---|---|
| Workaround name | | — |
| Ongoing burden | | — |
| Cost direction | | — |
| Key reason | | — |
| Integration points | | — |
| Total count | | — |
| Complexity tier | | — |
| Primary driver | | — |
| Team composition | | — |
| Timeline | | — |
| Confidence level | | — |
| Confidence basis | | — |
| Confidence gap [Risk Assessor — must address a dimension NOT confirmed in Confidence Basis above] | — | |
| Confidence calibration | — | |
| Tier up condition + destination [Risk Assessor — destination must differ from current Complexity Tier; LOW / MEDIUM / HIGH / XL] | — | |
| Tier down condition + destination [Risk Assessor — destination must differ from current Complexity Tier; LOW / MEDIUM / HIGH / XL] | — | |
```

---

## Coverage Summary

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|---|---|---|---|---|
| C-01 Surface area named + count | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-02 Complexity tier on-scale | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-03 Inertia check present | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-04 Confidence level + basis | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-05 Signal boundary respected | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-06 Team-size by specialist type | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-07 Sprint range | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-08 Complexity driver named | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-09 Sensitivity up + down | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-10 Confidence calibration | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-11 Confidence gap named | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-12 Single named conditions | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-13 Destination tier explicit | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-14 Conditions falsifiable | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-15 Basis + gap non-overlapping | ✓ (via C-28) | ✓ (via C-25) | ✓ (via C-25) | ✓ (via C-25) | ✓ (via C-25) |
| C-16 Destination ≠ current tier | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-17 Inline failure examples | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-18 Structural encoding | partial | partial | ✓ | partial | partial |
| C-19 Examples precede fields | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-20 Role-separated production | ✗ | ✓ | ✓ | ✓ | ✓ |
| C-21 WRONG + CORRECT both present | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-22 Relational constraints in field def | ✓ (body) | ✓ (body) | ✓ (label) | ✓ (body) | ✓ (body) |
| C-23 All fields chartered | n/a | ✓ | ✓ | ✓ | ✓ |
| C-24 Phase 2 names prohibited categories | n/a | ✓ | ✓ | ✓ | ✓ |
| C-25 Phase 2 self-test query | n/a | ✓ | ✓ | ✓ | ✓ |
| C-26 Role tags in column headers | n/a | ✓ | ✓ | ✓ | ✓ |
| C-27 Compilation table constraints in labels | n/a | ✓ | ✓ | ✓ | ✓ |
| C-28 Single-phase self-test in gap field | ✓ | n/a | n/a | n/a | n/a |
| C-29 Phase 1 exclusion list | n/a | ✓ | ✓ | ✓ | ✓ |

**Key trade-off**: V-01 is the only variation that exercises C-28 — the R9 pattern where single-phase self-check works. V-02 through V-05 are all two-phase and exercise C-29 (Phase 1 exclusion list). V-03 achieves the strongest structural encoding (C-18, C-22 label-level) at the cost of verbosity.
