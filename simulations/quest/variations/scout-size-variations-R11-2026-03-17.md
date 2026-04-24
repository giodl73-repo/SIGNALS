Now I have everything I need. The key finding: the existing R11 variations file was generated against v11 with 23 criteria, but the current rubric is v11 with **24** criteria (C-32 added). The R10 champion (V-04) introduced the three-column self-check table that C-32 now formalizes. I need to generate R11 variations that all target C-32 compliance.

---

# Scout-Size Prompt Variations — R11

**Skill**: scout-size
**Rubric**: v11 (24 aspirational criteria, C-01 through C-32)
**Date**: 2026-03-17
**R10 champion**: V-04 (24/24 = 100.00) — two/three-phase with three-column self-check for essential/recommended items; passes C-32 by design
**R10 gaps for other variations**: C-32 FAIL (V-01/V-02/V-03 flat self-check or no disqualifying forms); C-30/C-31 FAIL in single-phase V-01–V-03

---

## Context: What R11 Addresses

C-32 was extracted from R10 V-04's excellence signal: the self-check carried a three-column table (ID / What to verify / Failing form) giving each essential/recommended item an exact disqualifying form alongside its pass condition. V-03 passed C-31 with flat pass/fail entries for C-01–C-08 but failed C-32 because no item specified the exact output that would fail it.

R11 variations explore:
1. Whether single-phase designs can carry C-32 without two-phase overhead
2. Whether structural innovations (bookend inertia, prose-lead sections, handoff receipts) add quality while preserving C-32
3. Whether novel role-sequencing (risk-first flow) creates structural C-15 compliance through temporal ordering

**Axes selected:**

| Variation | Axis | Hypothesis |
|---|---|---|
| V-01 | Inertia framing (inertia as structural bookend) | Opening inertia + closing verdict forces cost-comparison coherence across the whole signal; single-axis test against V-04's baseline |
| V-02 | Output format (prose-lead sections before tables) | Requiring a prose reasoning paragraph per section prevents table-cell hiding; tests whether prose + table dual-track satisfies structural criteria |
| V-03 | Lifecycle emphasis (explicit phase handoff receipts) | Handoff summaries between phases create verifiable transfer records; tests whether handoff artifacts improve role boundary enforcement |
| V-04 | Phrasing register + structural encoding (combined) | First-person analyst voice + column-level constraint tags; tests whether narrative register can carry C-32 precision without structural degradation |
| V-05 | Role sequence + inertia framing (combined) | Risk-first hypothesis flow: Risk Assessor declares uncertainty hypothesis before Sizing Analyst fills fields; creates temporal C-15 compliance — negation-of-basis is structurally impossible because the basis didn't exist when the gap was stated |

---

## V-01 — Axis: Inertia framing (Inertia as structural bookend)

**Variation axis**: Inertia framing — inertia check opens the signal AND a closing Inertia Verdict section requires coherence between the cost-direction judgment and the complexity/confidence signals produced
**Hypothesis**: Placing inertia at the opening (cost-of-not-building assessment before any sizing) and the closing (explicit verdict confirming the complexity tier and confidence level cohere with the cost direction) creates a cost-comparison frame that the sizing work must satisfy. A HIGH complexity + LOW confidence signal that concludes "cheaper to build" is internally incoherent; the verdict forces the analyst to surface that tension. Single-phase design with C-28 self-test on the gap field and C-32 three-column self-check.

---

```markdown
## scout-size

Produce a **sizing signal** — not a project plan. No sprint assignments, owner names, task
breakdowns, or milestone dates anywhere in the output.

**Tier vocabulary — assign exactly one**: LOW / MEDIUM / HIGH / XL. "MODERATE", "medium-high",
"3/5", and all other labels fail. Downstream skills parse these four tokens only.

Work through the steps in order. Complete each step before moving to the next.

---

### Input

**Feature**: {{feature_name}}
**Context**: {{feature_context}}
**Current workaround**: {{workaround_description}}

---

### Step 1: Opening Inertia Check

The first question is not "how hard is it to build?" but "how much does it cost to NOT build?"
Teams routinely undercount the workaround's ongoing burden. Name it. Quantify it. Then make a
directional judgment: is building cheaper, comparable, or more expensive than maintaining the
workaround?

> WRONG: "Teams currently use spreadsheets." — Workaround named; cost direction and key driver
> absent. Fails.
> CORRECT: "Manual CSV export maintained by platform team, updated each quarter when schemas change
> — comparable cost to build: isolated from the main codebase and rarely fails, but each schema
> update consumes approximately two engineer-days of platform time."

| Workaround Name [required — "none" only if zero recurring cost] | Ongoing Cost [maintenance burden, error rate, user friction, accumulating debt — name at least one] | Cost Direction [exactly one: cheaper to build / comparable cost / more expensive to build] | Key Driver [one sentence on what drives the comparison] |
|---|---|---|---|
| | | | |

---

### Step 2: Surface Area

> WRONG: "Several API endpoints and some database tables." — No named points; no count. Fails.
> CORRECT: "POST /features endpoint, auth service hook, event-bus subscription (order.placed),
> orders DB schema migration — 4 integration points."

List each integration point individually. State the total count.

| Integration Point Name [name each individually — no generic descriptions] | Type [API / event / hook / UI / data / service / other] | Notes |
|---|---|---|
| | | |
| **Total integration points [numeric count required]** | | |

---

### Step 3: Complexity Tier + Primary Driver

> WRONG tier: "MODERATE" / "medium-high" / "3 out of 5" — Off-vocabulary. Fails.
> WRONG driver: "The feature has a lot of moving parts." — Names no causal factor. Fails.
> CORRECT: Tier: HIGH | Driver: "Cross-service transaction boundary — three services must agree
> on rollback semantics without a distributed transaction coordinator, requiring explicit
> saga-pattern orchestration."

Assign exactly one tier: LOW / MEDIUM / HIGH / XL. Name 1–2 specific drivers.

| Complexity Tier [exactly one: LOW / MEDIUM / HIGH / XL] | Primary Complexity Driver [name 1–2 specific causal factors — "it's complex" fails] |
|---|---|
| | |

---

### Step 4: Team-Size Signal

> WRONG: "2–3 engineers" — Disciplines not named. Fails.
> CORRECT: "1 backend engineer, 1 platform engineer, 0.5 PM"

Name the specialist disciplines. Headcount alone does not let program-plan route the work.

| Specialist Discipline [name the role or discipline — "engineer" alone fails] | FTE Fraction |
|---|---|
| | |
| **Total FTEs** | |

---

### Step 5: Timeline Signal

> WRONG: "Q3" / "4 sprints" — Calendar reference; point estimate. Both fail.
> CORRECT: "3–5 sprints"

State a sprint range. Both a lower bound and an upper bound are required. A single number
communicates false precision; a range communicates real uncertainty.

| Timeline Signal [N–M sprints — not a calendar date, not a single number] |
|---|
| |

---

### Step 6: Confidence Level + Basis

> WRONG: "Confidence: HIGH." — No basis. Fails.
> CORRECT: "MEDIUM — surface area confirmed at four points with stable contracts; auth hook
> behavior against the legacy layer is established from Q3 migration work."

State what IS known and verified. What is NOT yet known belongs in Step 7 — do not merge them.

| Confidence Level [HIGH / MEDIUM / LOW] | Confidence Basis [name what IS specifically established — bare level with no basis fails] |
|---|---|
| | |

---

### Step 7: Confidence Gap

The gap names the primary source of residual uncertainty — what the sizing has not yet verified.
It must address a **different dimension** than the basis above.

> WRONG gap (negation of basis): Basis: "API contract is stable." Gap: "API contract has not
> been confirmed." — Same dimension, reversed. Derivable from the basis by negation. Fails.
> CORRECT gap (new dimension): Basis: "API contract is stable." Gap: "Webhook delivery ordering
> under concurrent writes is unverified — whether the event bus guarantees at-least-once vs.
> exactly-once delivery affects the error-handling surface and may require an idempotency layer."
> — Names a dimension the basis did not reach. Passes.

**Before finalizing your gap**: Read your Confidence Basis in Step 6. Ask yourself: *Could a
reader derive this gap by negating something I confirmed in the basis — reversing "X is
established" to "X has not been confirmed"?* If yes, it is a restatement, not a gap. Restate to
name a different dimension entirely.

| Confidence Gap [must address a dimension NOT covered by the Confidence Basis above — negation of the basis fails this field] |
|---|
| Gap: [specific named unknown] — [why it matters to the sizing] |

---

### Step 8: Confidence Calibration

| What Would Raise Confidence [one concrete investigation or finding] | What Would Lower Confidence [one concrete investigation or finding] |
|---|---|
| | |

---

### Step 9: Tier Sensitivity

> WRONG tier-up: "Tier rises to HIGH if scope expands." — Not falsifiable; destination matches
> current tier if current tier is already HIGH. Fails on both counts.
> CORRECT tier-up: "Tier rises to XL if offline-sync support is required — confirmable by
> reviewing the PRD offline-sync section with the PM before next sprint planning."
>
> WRONG tier-down: "Tier drops if it turns out to be simpler than expected." — Not named; not
> falsifiable. Fails.
> CORRECT tier-down: "Tier drops to MEDIUM if the auth service exposes a documented event-hook
> API — confirmable by reading the auth team's published API reference."

Each condition: single named scenario, falsifiable (reader can name an action that settles it),
destination tier differs from the currently assigned tier.

| Direction | Single Named Falsifiable Condition | Destination Tier [must differ from current tier — LOW / MEDIUM / HIGH / XL] |
|---|---|---|
| Tier rises to → | | |
| Tier drops to → | | |

---

### Step 10: Closing Inertia Verdict

Now that all sizing signals are produced, return to the cost-direction judgment from Step 1.

A sizing signal is internally coherent when the complexity and confidence levels cohere with the
inertia judgment. Review:
- A "more expensive to build" judgment with LOW complexity is a tension worth naming.
- A "cheaper to build" judgment with XL complexity and LOW confidence may need re-examination.

| Cost Direction from Step 1 | Complexity Tier from Step 3 | Confidence Level from Step 6 | Coherence Verdict [Coherent / Tension — and one sentence of reasoning] |
|---|---|---|---|
| [restate] | [restate] | [restate] | |

---

### Output Compilation

**SIZING SIGNAL — {{feature_name}}**

| Field | Value |
|---|---|
| Surface Area | [named points — N integration points] |
| Complexity Tier | [LOW / MEDIUM / HIGH / XL] |
| Primary Complexity Driver | [1–2 named factors] |
| Team-Size Signal | [specialist disciplines + fractions] |
| Timeline Signal | [N–M sprints] |
| Confidence Level + Basis | [LEVEL — what is established] |
| Confidence Gap | [specific named unknown — different dimension from basis] |
| Inertia Check | [workaround — cost direction — key driver] |
| Tier-Up Sensitivity | Tier rises to [LEVEL] if [single named falsifiable condition] |
| Tier-Down Sensitivity | Tier drops to [LEVEL] if [single named falsifiable condition] |
| Confidence Calibration | [what would raise — what would lower] |
| Inertia Verdict | [Coherent / Tension — one sentence] |

---

### Signal Boundary Self-Check

Verify each item before finalizing. Each row names the exact output form that fails the criterion.

| ID | What to verify | Failing form |
|---|---|---|
| C-01 | Complexity tier is exactly one of: LOW / MEDIUM / HIGH / XL | Any label outside that set: "MODERATE", "medium-high", "3/5", two tiers stated, blank |
| C-02 | Timeline is a sprint range with both lower and upper bound | Single sprint number ("4 sprints"), calendar reference ("Q3"), missing either bound |
| C-03 | Surface area names at least 2 integration points with a total count | Generic description ("several APIs"), named points without count, count without named points |
| C-04 | Inertia check names the workaround AND states at least one cost dimension | Workaround named without cost judgment, cost direction absent, section missing |
| C-05 | Confidence level is present AND at least one sentence explains the basis | Bare level with no basis ("HIGH."), basis present but cites no specific evidence |
| C-06 | Team-size names at least one specialist discipline, not just headcount | "3 engineers" with no discipline or role named |
| C-07 | Complexity tier is accompanied by at least one named primary driver | Tier stated alone, driver is "it's complex" or "many moving parts" |
| C-08 | If AMEND is present, output reflects a substantive change traceable to it | AMEND acknowledged in text but no field values differ from non-amended form |
| — | No sprint assignments, owner names, task breakdowns, or milestone dates | Any such content anywhere in the output |
| — | Confidence gap addresses a dimension not covered by confidence basis | Gap = negation of basis |
| — | Tier sensitivity destination differs from current complexity tier | Destination = current tier |
| — | Inertia verdict is present and cites tier and confidence level | Verdict missing or does not reference Step 3 and Step 6 values |
```

---

## V-02 — Axis: Output format (Prose-lead sections before confirmation tables)

**Variation axis**: Output format — each section leads with a mandatory prose reasoning paragraph before the confirmation table; the table is the formal record, the prose is the analyst's reasoning chain
**Hypothesis**: Table-only sections allow constraint evasion by filling cells with minimal content that technically passes field validation but carries no useful signal. Requiring a prose paragraph first — which must name specific factors before the table is populated — forces substantive reasoning up front. The table then confirms the prose. The self-check (C-32) is still a three-column table at the end. Tests whether prose-lead format produces richer signals while maintaining structural compliance on all criteria including the new C-32.

---

```markdown
## scout-size

Produce a **sizing signal** for the feature below — not a project plan. No sprint assignments,
owner names, task breakdowns, or milestone dates anywhere in the output.

**Tier vocabulary — assign exactly one**: LOW / MEDIUM / HIGH / XL. Only these four. Downstream
skills parse this field — "MODERATE", "medium-high", and numeric scales will break them.

Each section below has two parts: (1) a reasoning paragraph you write before filling any table,
and (2) the confirmation table. Both are required. A blank or perfunctory reasoning paragraph
fails.

---

### Input

**Feature**: {{feature_name}}
**Context**: {{feature_context}}
**Current workaround**: {{workaround_description}}

---

### Section 1: Inertia Check

**Reasoning** — write this paragraph before filling the table:
Before any sizing work, describe the current workaround and characterize its actual cost to the
team or users. Name at least one concrete cost dimension (maintenance burden, error rate, user
friction, accumulating technical debt). Then state your directional verdict: is building this
feature cheaper, comparable, or more expensive than maintaining the workaround? Name the single
factor that most drives that comparison.

*[Analyst writes reasoning paragraph here — must name the workaround, at least one cost
dimension, and the directional verdict before filling the table below]*

**Confirmation table:**

| Workaround Name | Ongoing Cost [at least one cost dimension named in reasoning above] | Cost Direction [cheaper to build / comparable cost / more expensive to build] | Key Driver |
|---|---|---|---|
| | | | |

> WRONG reasoning: "Users have a spreadsheet they use for tracking." — Workaround named; no cost
> dimension characterized; no directional verdict. Paragraph fails.
> CORRECT reasoning: "The platform team maintains a weekly CSV export script that requires a
> schema-update pass whenever upstream models change — approximately two engineer-days per
> release cycle. This overhead scales with the team count. Building the feature is comparable in
> upfront cost but eliminates the recurring maintenance; the key driver is the compounding schema
> drift burden, which makes the workaround increasingly expensive relative to building."

---

### Section 2: Surface Area

**Reasoning** — write this paragraph before filling the table:
Enumerate every place this feature will touch the system. Name each integration point by type
and specific identifier. Do not use general categories ("several APIs") — name the specific
endpoint, hook, topic, schema, or surface. Then state the total count.

*[Analyst writes reasoning paragraph here — must name each integration point before table]*

**Confirmation table:**

| Integration Point Name [name each individually — "several endpoints" is not a name] | Type [API / event / hook / UI / data / service / other] | Notes |
|---|---|---|
| | | |
| **Total integration points [numeric count required]** | | |

> WRONG reasoning: "The feature will require API and database changes." — Generic; no named
> points; no count. Fails.
> CORRECT reasoning: "Three integration points: (1) POST /features REST endpoint in the features
> service, which creates the feature record; (2) an auth-service hook that must validate feature
> scoping rules at creation time; (3) the event-bus subscription on feature.created that the
> notification service consumes. Total: 3."

---

### Section 3: Complexity Tier + Primary Driver

**Reasoning** — write this paragraph before filling the table:
Assign exactly one complexity tier from: LOW / MEDIUM / HIGH / XL. Name the 1–2 specific
factors that most drove this assignment. The factor must be causal — it must name what makes the
feature complex, not restate that it is complex.

*[Analyst writes reasoning paragraph here — must name the tier and primary driver(s) before table]*

**Confirmation table:**

| Complexity Tier [exactly one: LOW / MEDIUM / HIGH / XL — reasoning paragraph must already name this] | Primary Complexity Driver [1–2 causal factors — must match reasoning paragraph above] |
|---|---|
| | |

> WRONG reasoning: "This is a HIGH complexity feature because it is complex and has many
> dependencies." — Circular; "it's complex" is not a driver. Fails.
> CORRECT reasoning: "HIGH complexity. The primary driver is the distributed transaction
> boundary: three services must agree on rollback behavior when feature creation fails mid-saga,
> and none of them currently implement saga-pattern coordination. A secondary driver is the
> auth-scoping rule, which requires a schema migration with a dual-write window."

---

### Section 4: Team-Size Signal

**Reasoning** — write this paragraph before filling the table:
Name the specialist disciplines this feature requires. Headcount alone ("3 engineers") does not
let program-plan source the right people. Name the roles.

*[Analyst writes reasoning paragraph here — must name disciplines before table]*

**Confirmation table:**

| Specialist Discipline [name the role — "engineer" alone fails] | FTE Fraction |
|---|---|
| | |
| **Total FTEs** | |

---

### Section 5: Timeline Signal

**Reasoning** — write this paragraph before filling the table:
Estimate the sprint range. Give both a lower bound (optimistic path with no blockers) and an
upper bound (realistic path with normal uncertainty). A single number falsely implies precision
you do not have. A calendar date conflates sizing with scheduling.

*[Analyst writes reasoning paragraph here — must state the range and the logic behind each bound]*

**Confirmation table:**

| Timeline Signal [N–M sprints — not a calendar date, not a single number; both bounds required] |
|---|
| |

---

### Section 6: Confidence Level + Basis

**Reasoning** — write this paragraph before filling the table:
State your confidence level (HIGH / MEDIUM / LOW) and name specifically what IS known or
verified that supports it. Do not include what is NOT known here — that belongs in Section 7.

*[Analyst writes reasoning paragraph here — must name specific evidence before table]*

**Confirmation table:**

| Confidence Level [HIGH / MEDIUM / LOW] | Confidence Basis [name what IS specifically established — bare level with no basis fails] |
|---|---|
| | |

> WRONG reasoning: "I have MEDIUM confidence because we know some things but not everything."
> — Vague; no specific evidence named. Fails.
> CORRECT reasoning: "MEDIUM confidence. The surface area is confirmed at three named points.
> The auth hook's behavior against the legacy layer is established from the Q3 migration work.
> The feature service's event-publication contract is documented and stable."

---

### Section 7: Confidence Gap

**Reasoning** — write this before filling the table:
Name the primary source of residual uncertainty — the dimension this sizing has NOT yet
verified. This must address a different dimension than the basis in Section 6.

**Stop. Before writing the gap reasoning**: Read your Section 6 Confidence Basis. Ask yourself:
*If I negated something I just confirmed in Section 6 — reversed "X is established" to "X has
not been confirmed" — would I get the gap I am about to write?* If yes, that is a basis-negation
and fails. Name a dimension your Section 6 reasoning did not reach.

*[Analyst writes gap reasoning here — must name a different dimension from Section 6]*

**Confirmation table:**

| Confidence Gap [must address a dimension NOT covered by Section 6 Confidence Basis — negation of the basis fails this field] |
|---|
| Gap: [specific named unknown] — [why it matters to the sizing] |

> WRONG gap reasoning: "I am uncertain about the auth API contract because it has not been
> confirmed." — Section 6 basis confirmed the auth hook behavior. This gap negates that. Fails.
> CORRECT gap reasoning: "What is not yet known is the event-bus delivery guarantee under peak
> concurrent load. Section 6 confirmed the event-publication contract is documented, but that
> contract is silent on at-least-once vs. exactly-once delivery semantics under burst conditions.
> If the guarantee is weak, an idempotency layer becomes a required integration point, expanding
> the surface area beyond the current three-point count."

---

### Section 8: Confidence Calibration

| What Would Raise Confidence [one concrete investigation or finding] | What Would Lower Confidence [one concrete investigation or finding] |
|---|---|
| | |

---

### Section 9: Tier Sensitivity

**Reasoning** — write this before filling the table:
For each direction, name one specific, falsifiable condition that would push the complexity tier
up or down from its current assignment. Each condition must name what would be confirmed or
discovered, and the destination tier must differ from the currently assigned tier.

*[Analyst writes reasoning here — must name both conditions with their destination tiers]*

**Confirmation table:**

| Direction | Single Named Falsifiable Condition [one scenario — name the specific trigger and what settles it] | Destination Tier [must differ from current complexity tier — LOW / MEDIUM / HIGH / XL] |
|---|---|---|
| Tier rises to → | | |
| Tier drops to → | | |

---

### Signal Self-Check

Verify each essential and recommended item. The Failing form column names the exact output
pattern that would fail that criterion.

| ID | What to verify | Failing form |
|---|---|---|
| C-01 | Complexity tier is exactly one of: LOW / MEDIUM / HIGH / XL | Any label not in the set: "MODERATE", "medium-high", "3/5", two tiers, blank |
| C-02 | Timeline is a sprint range with both lower and upper bound stated | Single sprint number, calendar date, missing either bound |
| C-03 | Surface area names at least 2 integration points with a total count | "Several APIs" or similar generic, named points without count, count without named points |
| C-04 | Inertia check names the workaround AND at least one cost dimension | Workaround named without cost judgment, cost direction absent, section missing |
| C-05 | Confidence level is present AND at least one sentence names specific supporting evidence | Bare level ("HIGH."), vague basis without specific named evidence |
| C-06 | Team-size names at least one specialist discipline or role, not just headcount | "3 engineers" or headcount with no discipline named |
| C-07 | Complexity tier is accompanied by at least one named primary causal driver | Tier alone, driver is "it's complex" or "many dependencies" |
| C-08 | If AMEND is present, output reflects a substantive change traceable to the amendment | AMEND acknowledged but field values unchanged from non-amended form |
| — | Reasoning paragraphs are not blank or perfunctory (each names specific factors) | Generic placeholder text or single-sentence non-answer |
| — | No sprint assignments, owner names, task breakdowns, or milestone dates | Any such content present |
| — | Confidence gap addresses a different dimension from the confidence basis | Gap = negation or restatement of basis |
| — | Tier sensitivity destination differs from current tier in both rows | Destination = current tier in either row |
```

---

## V-03 — Axis: Lifecycle emphasis (Explicit phase handoff receipts)

**Variation axis**: Lifecycle emphasis — each phase transition includes an explicit handoff receipt that summarizes what was produced and what is strictly reserved for the next phase; the receiving phase must acknowledge what it received before producing its fields
**Hypothesis**: Phase boundary violations (Phase 2 reproducing Phase 1 fields, or Phase 1 anticipating Phase 2 fields) are prevented not by charter exclusion lists alone but by explicit receipts that make the hand-off auditable. A receiving phase that must confirm "I received: [list of Phase 1 fields]" before proceeding is structurally blocked from claiming those fields as its own output. The receipt also strengthens C-29 compliance by making Phase 1's exclusion list a visible artifact at the boundary rather than a prose instruction only the model has read.

---

```markdown
## scout-size

Produce a **sizing signal** — not a project plan. No sprint assignments, owner names, task
breakdowns, or milestone dates anywhere in the output.

**Tier vocabulary — assign exactly one**: LOW / MEDIUM / HIGH / XL. No other vocabulary.
Downstream skills parse these four tokens. "MODERATE", "medium-high", and numeric scales fail.

This signal is produced in two phases. At each phase boundary, complete a handoff receipt
before proceeding. Receipts are part of the output.

---

### Input

**Feature**: {{feature_name}}
**Context**: {{feature_context}}
**Current workaround**: {{workaround_description}}

---

## Phase 1 — Sizing Analyst

**Charter — you produce these fields:**
- Inertia Check (workaround name, ongoing cost, cost direction, key driver)
- Surface Area (named integration points + total count)
- Complexity Tier (LOW / MEDIUM / HIGH / XL) + Primary Complexity Driver
- Team-Size Signal (specialist disciplines + fractions)
- Timeline Signal (sprint range N–M)
- Confidence Level + Confidence Basis
- Tier-Up Sensitivity (single named falsifiable condition + destination tier)
- Tier-Down Sensitivity (single named falsifiable condition + destination tier)
- Confidence Calibration (what would raise / lower)

**Charter — you do NOT produce (reserved for Phase 2):**
- Confidence Gap

Do not produce the Confidence Gap. Do not hint at, anticipate, or reference what the gap will be.
The Confidence Gap belongs exclusively to the Risk Assessor in Phase 2.

---

### Inertia Check [Sizing Analyst]

> WRONG: "The team currently uses a spreadsheet." — Cost direction absent. Fails.
> CORRECT: "Manual CSV export, platform-maintained, updated each quarter — comparable cost to
> build: the export is isolated from the main codebase and rarely fails, but schema drift
> consumes approximately two engineer-days per release cycle."

| Workaround Name [required — "none" only if zero recurring cost] | Ongoing Cost [name at least one cost dimension] | Cost Direction [exactly one: cheaper to build / comparable cost / more expensive to build] | Key Driver [one sentence] |
|---|---|---|---|
| | | | |

---

### Surface Area [Sizing Analyst]

> WRONG: "Several endpoints and some database changes." — No named points; no count. Fails.
> CORRECT: "POST /features endpoint, auth hook, event-bus subscription (order.placed),
> orders DB migration — 4 integration points."

| Integration Point Name [Sizing Analyst — name each individually] | Type [API / event / hook / UI / data / service / other] | Notes |
|---|---|---|
| | | |
| **Total integration points [Sizing Analyst — numeric count required]** | | |

---

### Complexity Tier + Primary Driver [Sizing Analyst]

> WRONG tier: "MODERATE" / "medium-high" — Off-vocabulary. Fails.
> WRONG driver: "The feature is complex." — Not a causal factor. Fails.
> CORRECT: Tier: HIGH | Driver: "Distributed saga boundary — three services must coordinate
> rollback without a transaction coordinator, requiring explicit compensating transactions."

| Complexity Tier [Sizing Analyst — exactly one: LOW / MEDIUM / HIGH / XL] | Primary Driver [Sizing Analyst — name 1–2 specific causal factors] |
|---|---|
| | |

---

### Team-Size Signal [Sizing Analyst]

> WRONG: "2 engineers" — Disciplines not named. Fails.
> CORRECT: "1 backend engineer, 1 platform engineer, 0.5 PM"

| Specialist Discipline [Sizing Analyst] | FTE Fraction |
|---|---|
| | |
| **Total FTEs** | |

---

### Timeline Signal [Sizing Analyst]

> WRONG: "Q3" / "4 sprints" — Calendar reference; point estimate. Both fail.
> CORRECT: "3–5 sprints"

| Timeline Signal [Sizing Analyst — N–M sprints; both lower and upper bound required] |
|---|
| |

---

### Confidence Level + Basis [Sizing Analyst]

> WRONG: "HIGH confidence." — No basis named. Fails.
> CORRECT: "MEDIUM — surface area is confirmed at four named integration points; auth hook
> behavior against the legacy layer is established from Q3 migration work."

Name only what IS established. What is NOT yet known goes to Phase 2.

| Confidence Level [Sizing Analyst — HIGH / MEDIUM / LOW] | Confidence Basis [Sizing Analyst — name what IS specifically established — bare level fails] |
|---|---|
| | |

---

### Tier-Up Sensitivity [Sizing Analyst]

> WRONG: "Tier rises if scope expands." — Not falsifiable; no specific condition or tier named.
> CORRECT: "Tier rises to XL if offline-sync support is required — confirm by reviewing the PRD
> offline-sync section with the PM before next sprint planning."

| Single Named Falsifiable Condition [Sizing Analyst — one scenario — name what settles it] | Destination Tier [Sizing Analyst — must be higher than current tier: HIGH or XL] |
|---|---|
| | Tier rises to [ ] |

---

### Tier-Down Sensitivity [Sizing Analyst]

> WRONG: "Tier drops if it's simpler than expected." — Not named; not falsifiable. Fails.
> CORRECT: "Tier drops to MEDIUM if the auth service exposes a documented webhook API —
> confirm by reading the auth team's published API reference this sprint."

| Single Named Falsifiable Condition [Sizing Analyst — one scenario — name what settles it] | Destination Tier [Sizing Analyst — must be lower than current tier: LOW or MEDIUM] |
|---|---|
| | Tier drops to [ ] |

---

### Confidence Calibration [Sizing Analyst]

| What Would Raise Confidence [one concrete investigation or finding] | What Would Lower Confidence [one concrete investigation or finding] |
|---|---|
| | |

---

## Phase 1 → Phase 2 Handoff Receipt

**[Sizing Analyst completes this receipt before handing off to Risk Assessor]**

I have produced the following Phase 1 fields. The Risk Assessor receives these as confirmed
Phase 1 output and must not reproduce them as gap content:

| Field | Status |
|---|---|
| Inertia Check | Produced — [restate cost direction in one phrase] |
| Surface Area | Produced — [restate total count] |
| Complexity Tier | Produced — [restate tier] |
| Primary Complexity Driver | Produced — [restate in 3–5 words] |
| Team-Size Signal | Produced — [restate disciplines] |
| Timeline Signal | Produced — [restate range] |
| Confidence Level + Basis | Produced — [restate level and one phrase from basis] |
| Tier-Up Sensitivity | Produced |
| Tier-Down Sensitivity | Produced |
| Confidence Calibration | Produced |
| **Confidence Gap** | **Reserved — NOT produced. Belongs to Phase 2.** |

*Phase 1 complete. Proceeding to Phase 2.*

---

## Phase 2 — Risk Assessor

**[Risk Assessor acknowledges receipt before producing fields]**

I have received Phase 1 output. The following are confirmed Phase 1 fields — I must not cite
any of them as the primary content of the Confidence Gap:

- The integration points the Sizing Analyst enumerated
- The complexity tier rationale the Sizing Analyst named
- The auth/API contract status the Sizing Analyst confirmed as established
- The team-size and timeline estimates the Sizing Analyst produced
- The confidence basis the Sizing Analyst named

My Confidence Gap must identify a dimension that Phase 1 analysis did not and could not address.

**Charter — I produce exactly one field: Confidence Gap.**

**Non-access constraint**: My gap must not cite any category confirmed in Phase 1. It must name
something the Sizing Analyst's work left entirely unaddressed.

**Self-test — required before writing the gap**: Read the Phase 1 Confidence Basis. Ask: *Could
a reader look only at Phase 1 output and derive my gap by negating something the Sizing Analyst
confirmed — reversing "X is established" to "X has not been confirmed"?* If yes, it is a
restatement and a charter violation. Name a genuinely different dimension.

---

> WRONG gap (charter violation — basis negation):
> Phase 1 basis: "Auth hook behavior established from Q3 migration."
> Gap: "Auth hook behavior has not been confirmed." — Same dimension, negated. Directly
> derivable from Phase 1 by negation. Charter violation.

> CORRECT gap (new dimension Phase 1 did not address):
> Phase 1 basis: "Auth hook behavior established from Q3 migration."
> Gap: "Auth hook rate-limiting under burst load from the new feature's event volume is
> undocumented — the Q3 migration validated the hook's correctness under normal load, but
> concurrent event delivery under peak volume has never been stress-tested. If the hook applies
> per-event rate limits, the feature may require backpressure logic, adding an integration point."

| Confidence Gap [Phase 2: Risk Assessor — PROHIBITED: integration points Analyst named, complexity rationale Analyst stated, contracts Analyst confirmed, team/timeline signals Analyst produced — must name a dimension Phase 1 did not reach — verify it is NOT derivable from Phase 1 by negation] |
|---|
| Gap: [specific named unknown] — [why it matters to the sizing] |

**Before finalizing**: Run the self-test one more time. If your gap negates anything in the
Phase 1 Confidence Basis, it is a charter violation. Restate to name a genuinely different
dimension of uncertainty.

---

## Phase 2 → Output Handoff Receipt

**[Risk Assessor completes this receipt before compilation]**

| Field | Status |
|---|---|
| Confidence Gap | Produced — [restate gap topic in 3–5 words] |
| All Phase 1 fields | Carried forward unchanged from Phase 1 |

*Phase 2 complete. Proceeding to output compilation.*

---

## Compiled Signal

**SIZING SIGNAL — {{feature_name}}**

| Field | Phase | Value |
|---|---|---|
| Inertia Check | 1 | [workaround — cost direction — key driver] |
| Surface Area | 1 | [named points — N integration points] |
| Complexity Tier | 1 | [LOW / MEDIUM / HIGH / XL] |
| Primary Complexity Driver | 1 | [1–2 named factors] |
| Team-Size Signal | 1 | [disciplines + fractions] |
| Timeline Signal | 1 | [N–M sprints] |
| Confidence Level + Basis | 1 | [LEVEL — what is established] |
| Confidence Gap [must address a dimension NOT in Phase 1 Confidence Basis — verify: not derivable from Phase 1 by negation] | 2 | [specific named unknown — why it matters] |
| Tier-Up Sensitivity | 1 | Tier rises to [LEVEL] if [single named falsifiable condition] |
| Tier-Down Sensitivity | 1 | Tier drops to [LEVEL] if [single named falsifiable condition] |
| Confidence Calibration | 1 | [what would raise — what would lower] |

---

### Signal Boundary Self-Check

Verify each essential and recommended item. The Failing form column names the exact output that
disqualifies the criterion.

| ID | What to verify | Failing form |
|---|---|---|
| C-01 | Complexity tier is exactly one of: LOW / MEDIUM / HIGH / XL | Any label outside the set: "MODERATE", "medium-high", "3/5", two tiers stated, blank |
| C-02 | Timeline is a sprint range with both lower and upper bound | Single sprint number ("4 sprints"), calendar date, missing either bound |
| C-03 | Surface area names at least 2 integration points with a total count | Generic description, named points without count, count without named points |
| C-04 | Inertia check names the workaround AND states at least one cost dimension | Workaround named without cost judgment, cost direction absent, section missing |
| C-05 | Confidence level is present AND at least one sentence names specific supporting evidence | Bare level with no basis, vague basis without specific named evidence |
| C-06 | Team-size names at least one specialist discipline or role | Bare headcount with no discipline named |
| C-07 | Complexity tier is accompanied by at least one named primary causal driver | Tier alone, driver is "it's complex" or non-causal |
| C-08 | If AMEND is present, output reflects a substantive change traceable to it | AMEND noted but field values unchanged from non-amended form |
| — | Phase handoff receipts are complete and present | Missing receipt at either phase boundary |
| — | No sprint assignments, owner names, task breakdowns, or milestone dates | Any such content present |
| — | Confidence gap names a dimension not covered by the confidence basis | Gap = negation or restatement of basis |
| — | Tier sensitivity destination differs from current tier in both rows | Destination = current tier |
```

---

## V-04 — Combined: Phrasing register + structural encoding

**Variation axis**: Phrasing register (first-person analyst voice) combined with structural encoding (column-level constraint tags)
**Hypothesis**: Two-phase designs in R10/R11 used third-person imperative instructions ("The Risk Assessor must..."). First-person framing ("I am the Risk Assessor. I produce...") creates a role-embodiment pattern where the model's identity shifts at phase boundaries, making charter violations feel like self-contradiction rather than rule-breaking. Combined with column-level role tags that encode ownership structurally — not just in charter prose — the design tests whether identity framing + structural precision can achieve the same criterion coverage as directive-imperative framing while producing more grounded outputs.

---

```markdown
## scout-size

This skill produces a **sizing signal** — not a project plan. No sprint assignments, owner
names, task breakdowns, or milestone dates anywhere in the output.

**Tier vocabulary**: LOW / MEDIUM / HIGH / XL — exactly one. This value is parsed by downstream
skills. "MODERATE", "medium-high", and numeric scales will break them.

Two analysts contribute to this signal. Each speaks in first person. Embody each role fully
before proceeding to the next.

---

### Input

**Feature**: {{feature_name}}
**Context**: {{feature_context}}
**Current workaround**: {{workaround_description}}

---

## Phase 1 — I am the Sizing Analyst

I produce all structural sizing fields. I do not produce the Confidence Gap — that is the Risk
Assessor's sole contribution.

**My fields**: Inertia Check, Surface Area, Complexity Tier, Primary Driver, Team-Size Signal,
Timeline Signal, Confidence Level, Confidence Basis, Tier-Up Sensitivity, Tier-Down Sensitivity,
Confidence Calibration.

**Not my fields**: Confidence Gap. I will not produce, hint at, or anticipate it.

---

### Inertia Check [I am the Sizing Analyst — this is my field]

Before I assess complexity, I compare building against not building. I name the workaround,
characterize its real cost to the team, and state whether building is cheaper, comparable, or
more expensive.

> WRONG: "Teams use a spreadsheet today." — I named the workaround but gave no cost judgment. Fails.
> CORRECT: "Manual CSV export, platform-maintained — comparable cost to build: the export is
> isolated and rarely fails, but requires a schema-update pass each quarter that consumes
> approximately two engineer-days."

| Workaround Name [Sizing Analyst — required; "none" only if zero recurring cost] | Ongoing Cost [Sizing Analyst — name at least one cost dimension] | Cost Direction [Sizing Analyst — exactly one: cheaper to build / comparable cost / more expensive to build] | Key Driver [Sizing Analyst — one sentence] |
|---|---|---|---|
| | | | |

---

### Surface Area [I am the Sizing Analyst — this is my field]

I list every integration point this feature will touch, by name. Generic descriptions are not
an integration inventory.

> WRONG: "Several API endpoints and some database changes." — No named points; no count. Fails.
> CORRECT: "POST /features endpoint, auth hook, event-bus subscription (order.placed),
> orders DB migration — 4 integration points."

| Integration Point Name [Sizing Analyst — name each individually] | Type [API / event / hook / UI / data / service / other] | Notes |
|---|---|---|
| | | |
| **Total integration points [Sizing Analyst — numeric count required]** | | |

---

### Complexity Tier + Primary Driver [I am the Sizing Analyst — this is my field]

I assign exactly one tier from the vocabulary. I name what specifically makes this feature
complex — not that it is complex.

> WRONG tier: "MODERATE" / "medium-high" — Off-vocabulary. Breaks downstream parsing. Fails.
> WRONG driver: "The feature has many moving parts." — Not a causal factor. Fails.
> CORRECT: Tier: HIGH | Driver: "Distributed saga boundary — three services must coordinate
> rollback with explicit compensating transactions; no shared transaction coordinator exists."

| Complexity Tier [Sizing Analyst — exactly one: LOW / MEDIUM / HIGH / XL] | Primary Driver [Sizing Analyst — 1–2 specific causal factors — vague descriptions fail] |
|---|---|
| | |

---

### Team-Size Signal [I am the Sizing Analyst — this is my field]

I name the specialist disciplines, not just headcount.

> WRONG: "2 engineers" — No disciplines. Fails.
> CORRECT: "1 backend engineer, 1 platform engineer, 0.5 PM"

| Specialist Discipline [Sizing Analyst] | FTE Fraction [Sizing Analyst] |
|---|---|
| | |
| **Total FTEs [Sizing Analyst]** | |

---

### Timeline Signal [I am the Sizing Analyst — this is my field]

I give a sprint range — both a lower and upper bound. A single number implies certainty I do
not have.

> WRONG: "Q3 delivery" / "4 sprints" — Calendar reference; point estimate. Both fail.
> CORRECT: "3–5 sprints"

| Timeline Signal [Sizing Analyst — N–M sprints; both bounds required; not a date, not a single number] |
|---|
| |

---

### Confidence Level + Basis [I am the Sizing Analyst — this is my field]

I state how confident I am in this sizing and name specifically what IS established. What is NOT
yet known belongs to the Risk Assessor.

> WRONG: "HIGH confidence." — No basis. Fails.
> CORRECT: "MEDIUM — surface area is confirmed at four named points; auth hook behavior against
> the legacy layer is established from Q3 migration work."

| Confidence Level [Sizing Analyst — HIGH / MEDIUM / LOW] | Confidence Basis [Sizing Analyst — name what IS specifically established — bare level fails] |
|---|---|
| | |

---

### Tier Sensitivity [I am the Sizing Analyst — this is my field]

I name one falsifiable condition per direction. Each destination tier must differ from the
currently assigned tier.

> WRONG up: "Tier rises to HIGH if scope expands." — Destination may equal current tier; not
> falsifiable. Fails.
> CORRECT up: "Tier rises to XL if offline-sync support is required — confirm by reviewing
> the PRD offline-sync section with the PM."
>
> WRONG down: "Tier drops if things are simpler than expected." — Not named; not falsifiable. Fails.
> CORRECT down: "Tier drops to MEDIUM if auth service exposes a documented webhook API —
> confirm by reading the auth team's published API reference."

| Direction | Single Named Falsifiable Condition [Sizing Analyst — one scenario — name what settles it] | Destination Tier [Sizing Analyst — must differ from current tier — LOW / MEDIUM / HIGH / XL] |
|---|---|---|
| Tier rises to → | | |
| Tier drops to → | | |

---

### Confidence Calibration [I am the Sizing Analyst — this is my field]

| What Would Raise Confidence [Sizing Analyst — one concrete investigation] | What Would Lower Confidence [Sizing Analyst — one concrete investigation] |
|---|---|
| | |

---

*Phase 1 complete. I hand off to the Risk Assessor.*

---

## Phase 2 — I am the Risk Assessor

I produce exactly one field: the Confidence Gap. Everything else was produced by the Sizing
Analyst. I do not reproduce it, revise it, or extend it. My sole contribution is naming what
Phase 1 did not address.

**My field**: Confidence Gap.

**Not my fields**: Everything else — the Sizing Analyst produced it and it is final.

**Non-access rule — I am explicitly prohibited from citing as the gap**:
- The integration points the Sizing Analyst enumerated
- The API or service contracts the Sizing Analyst confirmed as established
- The complexity tier rationale the Sizing Analyst named
- The team-size composition or timeline range the Sizing Analyst produced
- The confidence basis the Sizing Analyst stated

These are confirmed Phase 1 content. My gap must name a dimension Phase 1 left unaddressed.

**Self-test — I apply this before writing my gap**: I read the Phase 1 Confidence Basis.
I ask myself: *If I negated something the Sizing Analyst confirmed — reversed "X is established"
to "X has not been confirmed" — would I get the gap I am about to write?* If yes, I have written
a basis-negation, not a gap. I will restate to name a genuinely different dimension.

---

> WRONG gap (I would be citing confirmed Phase 1 content — charter violation):
> Phase 1 basis: "Auth hook behavior established from Q3 migration."
> My gap: "Auth hook behavior has not been confirmed." — Same dimension, negative polarity. I
> derived this from Phase 1 by negation. This is a charter violation.

> CORRECT gap (I am naming a dimension Phase 1 did not reach):
> Phase 1 basis: "Auth hook behavior established from Q3 migration."
> My gap: "Auth hook rate-limiting under the new feature's event volume is undocumented — the
> Q3 migration confirmed correctness under normal load, but concurrent peak delivery has never
> been stress-tested. If per-event rate limits apply, backpressure logic becomes a required
> integration point, expanding the surface area count."

| Confidence Gap [Risk Assessor — PROHIBITED: integration points Sizing Analyst named, contracts Analyst confirmed, complexity drivers Analyst stated, team/timeline signals Analyst produced — must name a dimension Phase 1 did not reach — must NOT be derivable from Phase 1 by negation] |
|---|
| Gap: [specific named unknown] — [why it matters to the sizing] |

**Before I finalize**: I run the self-test one more time. If my gap negates anything in Phase 1's
Confidence Basis, it is a charter violation. I restate to name a genuinely different dimension.

---

## Compiled Signal

**SIZING SIGNAL — {{feature_name}}**

| Field | Analyst | Value |
|---|---|---|
| Inertia Check — workaround | Sizing Analyst | |
| Inertia Check — ongoing cost | Sizing Analyst | |
| Inertia Check — cost direction | Sizing Analyst | |
| Inertia Check — key driver | Sizing Analyst | |
| Surface Area — integration points | Sizing Analyst | |
| Surface Area — total count | Sizing Analyst | |
| Complexity Tier [LOW / MEDIUM / HIGH / XL] | Sizing Analyst | |
| Primary Complexity Driver | Sizing Analyst | |
| Team-Size Signal | Sizing Analyst | |
| Timeline Signal [N–M sprints — single number fails] | Sizing Analyst | |
| Confidence Level + Basis | Sizing Analyst | |
| Confidence Gap [Risk Assessor — must address a dimension NOT in Confidence Basis above — NOT derivable from Phase 1 by negation] | Risk Assessor | |
| Tier-Up Sensitivity | Sizing Analyst | |
| Tier-Down Sensitivity | Sizing Analyst | |
| Confidence Calibration | Sizing Analyst | |

---

### Signal Boundary Self-Check

Each essential and recommended criterion is listed with the exact output form that disqualifies it.

| ID | What to verify | Failing form |
|---|---|---|
| C-01 | Complexity Tier row contains exactly one of: LOW / MEDIUM / HIGH / XL | Any label outside the set: "MODERATE", "medium-high", "3/5", blank, two values |
| C-02 | Timeline row contains a sprint range with both lower and upper bound explicitly stated | Single sprint number, calendar date, missing either bound, format other than "N–M sprints" |
| C-03 | Surface area names at least 2 specific integration points with a numeric total count | Generic phrase ("several endpoints"), named points without count, total absent |
| C-04 | Inertia Check names the workaround AND states at least one explicit cost dimension | Workaround named without characterizing its cost, cost direction absent, section missing |
| C-05 | Confidence level is stated AND at least one sentence names specific supporting evidence | Bare level with no supporting sentence, basis present but cites no specific named evidence |
| C-06 | Team-size names at least one specialist role or discipline beyond bare headcount | "3 engineers" or "2 people" with no role or discipline specified |
| C-07 | Complexity tier is accompanied by at least one named specific causal driver | Tier stated without driver, driver is "it's complex", "many moving parts", or other non-causal phrase |
| C-08 | If AMEND directive is present, at least one field value in the output differs substantively from a non-amended response | AMEND acknowledged in text but all field values identical to what would appear without it |
```

---

## V-05 — Combined: Role sequence + Inertia framing (Risk-first hypothesis flow)

**Variation axis**: Role sequence (reversed: Risk Assessor states uncertainty hypotheses before Sizing Analyst fills fields) combined with inertia framing (inertia owned by Risk Assessor as cost-of-not-building assessment)
**Hypothesis**: In every previous variation, the Sizing Analyst produces the Confidence Basis before the Risk Assessor produces the Confidence Gap. This creates a structural risk: the Risk Assessor, having read the Basis, can produce a gap that is a negation of it. The fix applied is a self-test prompt. An alternative fix is to reverse the temporal sequence: the Risk Assessor states their uncertainty hypothesis *before* the Sizing Analyst fills any fields. The gap cannot negatively reference the Basis because the Basis does not exist yet when the gap is written. After the Risk Assessor stakes out the gap, the Sizing Analyst fills all sizing fields and the Confidence Basis — which now must explicitly address a *different* dimension from the already-stated gap. C-15 compliance becomes structural rather than heuristic. Inertia is co-framed: the Risk Assessor assesses cost-of-not-building from the risk perspective (what does the team risk by continuing without this feature?), and the Sizing Analyst confirms the cost direction.

---

```markdown
## scout-size

Produce a **sizing signal** — not a project plan. No sprint assignments, owner names, task
breakdowns, or milestone dates anywhere in the output.

**Tier vocabulary — assign exactly one**: LOW / MEDIUM / HIGH / XL. No other vocabulary.

This signal is produced in a reversed sequence: the Risk Assessor stakes out the primary
uncertainty **before** the Sizing Analyst produces the structural fields. This sequence makes
the non-overlap constraint between Confidence Basis and Confidence Gap structurally guaranteed
rather than heuristically enforced — the gap was written before the basis existed.

Read the full instructions for each phase before beginning.

---

### Input

**Feature**: {{feature_name}}
**Context**: {{feature_context}}
**Current workaround**: {{workaround_description}}

---

## Phase 1 — Risk Assessor (Uncertainty First)

**I am the Risk Assessor. I go first.**

Before the Sizing Analyst produces any sizing fields, I state my assessment of:
1. The primary unknown — the confidence gap hypothesis
2. The cost of not building — from the risk perspective (what does the team risk by continuing
   without this feature?)

I do not produce sizing fields. I do not produce: surface area, complexity tier, team-size
signal, timeline signal, confidence level, confidence basis, tier sensitivities, or confidence
calibration. Those are the Sizing Analyst's fields.

**Why I go first**: My Confidence Gap must address a different dimension than the Confidence
Basis. If the Sizing Analyst produced the Basis first, I could accidentally negate it. By
staking out the Gap hypothesis now — before the Basis exists — the non-overlap constraint is
structurally enforced. The Sizing Analyst will then produce a Basis that addresses what IS known,
which must be a different dimension from the gap I have already stated.

---

### Risk Framing: Cost of Not Building [Risk Assessor]

What does the team risk by continuing without this feature? Name the workaround's burden from
the risk perspective: what is growing worse, what is accumulating, what failure modes does the
workaround create?

> WRONG: "Without this feature, users use the current system." — Names the state; names no risk.
> CORRECT: "Without this feature, teams run manual CSV exports that accumulate schema drift debt
> — each release cycle adds a schema-update pass; the risk is that drift compounds faster than
> the team can maintain the export script, eventually requiring a rewrite rather than an update.
> The compounding nature makes delay increasingly expensive."

| Risk of Not Building [Risk Assessor — name the workaround and at least one compounding or growing risk dimension] |
|---|
| [Workaround] — continuing without this feature risks: [specific growing risk] |

---

### Confidence Gap Hypothesis [Risk Assessor — stated before Sizing Analyst produces any fields]

I name the primary source of uncertainty I expect this sizing will carry — the dimension I
believe is most likely to be unresolved when Phase 2 is complete.

**This is a hypothesis, not a confirmed finding.** The Sizing Analyst may confirm or revise it
in Phase 2. But by stating it now, before the Confidence Basis is written, I guarantee the gap
and basis address different dimensions.

> WRONG gap hypothesis: "I expect the surface area to be uncertain." — The surface area is a
> Phase 2 structural field the Sizing Analyst will confirm. This names a Phase 2 output, not an
> uncertainty about a dimension beyond it. Fails.
> CORRECT gap hypothesis: "I expect the primary uncertainty to be behavioral — specifically,
> how the event bus handles concurrent delivery under peak load from the new feature's event
> volume. The surface area count may be confirmed, but the delivery guarantee contract (at-least-
> once vs. exactly-once) is unlikely to be documented, making the error-handling surface
> potentially larger than the integration point count suggests."

| Confidence Gap Hypothesis [Risk Assessor — state before Phase 2 begins — must name a behavioral, operational, or environmental dimension the sizing may leave unresolved — not a Phase 2 structural field] |
|---|
| Hypothesis: [dimension] — [why it is unlikely to be resolved by structural sizing alone] |

---

*Phase 1 complete. Risk Assessor has staked out the gap hypothesis. Sizing Analyst proceeds.*

---

## Phase 2 — Sizing Analyst (Structural Fields)

**I am the Sizing Analyst. I produce all structural sizing fields.**

I have read the Risk Assessor's gap hypothesis. My Confidence Basis must address what IS
specifically established in the structural sizing — and because the Risk Assessor has already
stated the gap dimension, my Basis will naturally address a different dimension without requiring
a self-test check.

**My fields**: Surface Area, Complexity Tier, Primary Driver, Team-Size Signal, Timeline Signal,
Confidence Level, Confidence Basis, Cost Direction Confirmation (inertia), Tier-Up Sensitivity,
Tier-Down Sensitivity, Confidence Calibration, Confidence Gap Confirmation.

**Not my fields**: Risk Framing (Phase 1). The gap hypothesis is the Risk Assessor's. I confirm
or amend it at the end of Phase 2.

---

### Surface Area [Sizing Analyst]

> WRONG: "Several API and database integrations." — No named points; no count. Fails.
> CORRECT: "POST /features endpoint, auth hook, event-bus subscription (order.placed),
> orders DB migration — 4 integration points."

| Integration Point Name [Sizing Analyst — name each individually] | Type [API / event / hook / UI / data / service / other] | Notes |
|---|---|---|
| | | |
| **Total integration points [Sizing Analyst — numeric count required]** | | |

---

### Complexity Tier + Primary Driver [Sizing Analyst]

> WRONG tier: "MODERATE" / "medium-high" — Off-vocabulary. Fails.
> WRONG driver: "It's a complex integration." — Not a causal factor. Fails.
> CORRECT: Tier: HIGH | Driver: "Distributed saga boundary — three services must coordinate
> rollback with explicit compensating transactions and no shared coordinator."

| Complexity Tier [Sizing Analyst — exactly one: LOW / MEDIUM / HIGH / XL] | Primary Driver [Sizing Analyst — 1–2 specific causal factors] |
|---|---|
| | |

---

### Team-Size Signal [Sizing Analyst]

> WRONG: "2 engineers" — Disciplines not named. Fails.
> CORRECT: "1 backend engineer, 1 platform engineer, 0.5 PM"

| Specialist Discipline [Sizing Analyst] | FTE Fraction |
|---|---|
| | |
| **Total FTEs** | |

---

### Timeline Signal [Sizing Analyst]

> WRONG: "Q3" / "4 sprints" — Calendar reference; point estimate. Both fail.
> CORRECT: "3–5 sprints"

| Timeline Signal [Sizing Analyst — N–M sprints; both lower and upper bound required] |
|---|
| |

---

### Confidence Level + Basis [Sizing Analyst]

I name what IS established by the structural sizing. Because the Risk Assessor has already
stated the gap hypothesis, my basis will naturally address what the gap did not — I name what
the sizing DID resolve.

> WRONG: "MEDIUM confidence." — No basis. Fails.
> CORRECT: "MEDIUM — surface area is confirmed at four named integration points; auth hook
> behavior against the legacy layer is established from Q3 migration work; the saga-pattern
> rollback design is documented in the architecture review."

Note: my Confidence Basis should address what IS known from structural sizing. The Risk
Assessor's gap hypothesis addresses what the structural sizing leaves unresolved. These are
different dimensions by construction.

| Confidence Level [Sizing Analyst — HIGH / MEDIUM / LOW] | Confidence Basis [Sizing Analyst — name what IS specifically established — bare level fails] |
|---|---|
| | |

---

### Cost Direction Confirmation [Sizing Analyst — confirms Risk Assessor's risk framing]

The Risk Assessor identified the cost of not building from a risk perspective. I confirm the
directional judgment from the sizing perspective: given the complexity tier and team-size signal,
is building cheaper, comparable, or more expensive than maintaining the workaround?

| Workaround Name | Cost Direction [Sizing Analyst confirms: cheaper to build / comparable cost / more expensive to build] | Key Driver [one sentence] |
|---|---|---|
| [restate from Phase 1] | | |

---

### Tier Sensitivity [Sizing Analyst]

> WRONG up: "Tier rises if scope expands." — Not falsifiable. Fails.
> CORRECT up: "Tier rises to XL if offline-sync support is required — confirm by reviewing
> the PRD offline-sync section with the PM."
>
> WRONG down: "Tier drops if things simplify." — Not named; not falsifiable. Fails.
> CORRECT down: "Tier drops to MEDIUM if the auth service exposes a documented webhook API —
> confirm by reading the auth team's API reference."

| Direction | Single Named Falsifiable Condition [Sizing Analyst — one scenario — name what settles it] | Destination Tier [Sizing Analyst — must differ from current tier — LOW / MEDIUM / HIGH / XL] |
|---|---|---|
| Tier rises to → | | |
| Tier drops to → | | |

---

### Confidence Calibration [Sizing Analyst]

| What Would Raise Confidence [one concrete investigation] | What Would Lower Confidence [one concrete investigation] |
|---|---|
| | |

---

### Confidence Gap Confirmation [Sizing Analyst — confirms or amends the Risk Assessor's hypothesis]

I review the Risk Assessor's gap hypothesis from Phase 1. I confirm it if my structural sizing
left that dimension unresolved, or amend it with a more specific characterization.

| Risk Assessor's Hypothesis [from Phase 1] | Sizing Analyst Confirmation [Confirmed as stated / Amended to: — one sentence] |
|---|---|
| [restate from Phase 1] | |

---

## Compiled Signal

**SIZING SIGNAL — {{feature_name}}**

| Field | Phase | Value |
|---|---|---|
| Risk of Not Building [Risk Assessor] | 1 | [workaround — growing risk dimension] |
| Confidence Gap [Risk Assessor hypothesis, confirmed or amended by Sizing Analyst — addresses a dimension NOT in Confidence Basis by construction] | 1+2 | [specific named unknown — why it matters] |
| Surface Area | 2 | [named points — N integration points] |
| Complexity Tier | 2 | [LOW / MEDIUM / HIGH / XL] |
| Primary Complexity Driver | 2 | [1–2 named factors] |
| Team-Size Signal | 2 | [disciplines + fractions] |
| Timeline Signal | 2 | [N–M sprints] |
| Confidence Level + Basis | 2 | [LEVEL — what IS established — different dimension from gap] |
| Cost Direction | 2 | [workaround — cheaper/comparable/more expensive — key driver] |
| Tier-Up Sensitivity | 2 | Tier rises to [LEVEL] if [single named falsifiable condition] |
| Tier-Down Sensitivity | 2 | Tier drops to [LEVEL] if [single named falsifiable condition] |
| Confidence Calibration | 2 | [what would raise — what would lower] |

---

### Signal Boundary Self-Check

Each essential and recommended item specifies the exact output form that disqualifies it.

| ID | What to verify | Failing form |
|---|---|---|
| C-01 | Complexity tier is exactly one of: LOW / MEDIUM / HIGH / XL | Any label outside the set: "MODERATE", "medium-high", "3/5", two tiers stated, blank |
| C-02 | Timeline is a sprint range with both lower and upper bound | Single sprint number, calendar date, missing either bound |
| C-03 | Surface area names at least 2 integration points with a total count | Generic description, named points without count, count without named points |
| C-04 | Inertia / cost-of-not-building section names the workaround AND at least one risk or cost dimension | Workaround named without cost or risk characterized, section missing |
| C-05 | Confidence level is present AND at least one sentence names specific supporting evidence | Bare level with no basis, vague basis without specific evidence named |
| C-06 | Team-size names at least one specialist discipline or role, not just headcount | "3 engineers" or bare headcount with no role named |
| C-07 | Complexity tier is accompanied by at least one named primary causal driver | Tier stated alone, driver is "it's complex" or non-causal |
| C-08 | If AMEND is present, output reflects a substantive change traceable to it | AMEND acknowledged but no field values changed from non-amended form |
| — | Phase 1 Risk Assessor gap hypothesis is present and states a non-structural dimension | Missing, or hypothesis names a Phase 2 structural field (surface area, tier) rather than a behavioral/operational dimension |
| — | Confidence Basis (Phase 2) and Confidence Gap (Phase 1) address different dimensions | Basis negates or restates gap; gap negates or restates basis |
| — | No sprint assignments, owner names, task breakdowns, or milestone dates | Any such content present |
| — | Tier sensitivity destination differs from current tier in both rows | Destination equals current tier in either row |
```

---

## Coverage Summary

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|---|---|---|---|---|
| C-01 Complexity tier on-scale | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-02 Timeline range with both bounds | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-03 Surface area named + count | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-04 Inertia check present with cost | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-05 Confidence level + basis | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-06 Team-size by specialist type | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-07 Complexity driver named | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-08 AMEND modifies output | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-09 Sensitivity up + down | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-10 Confidence calibration | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-11 Confidence gap named | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-12 Single named conditions | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-13 Destination tier explicit | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-14 Conditions falsifiable | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-15 Basis + gap non-overlapping | ✓ (C-28) | ✓ (C-28) | ✓ (C-25) | ✓ (C-25) | ✓ (structural) |
| C-16 Destination ≠ current tier | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-17 Inline failure examples | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-18 Structural encoding | partial | partial | ✓ | ✓ | partial |
| C-19 Examples precede fields | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-20 Role-separated production | ✗ (single-phase) | ✗ (single-phase) | ✓ | ✓ | ✓ |
| C-21 WRONG + CORRECT both present | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-22 Relational constraints in field def | ✓ (body) | ✓ (body) | ✓ (label) | ✓ (label) | ✓ (body) |
| C-23 All fields chartered | n/a | n/a | ✓ | ✓ | ✓ |
| C-24 Phase 2 names prohibited categories | n/a | n/a | ✓ | ✓ | ✓ |
| C-25 Phase 2 self-test query | n/a | n/a | ✓ | ✓ | n/a (structural) |
| C-26 Role tags in column headers | n/a | n/a | ✓ | ✓ | partial |
| C-27 Compilation table constraints in labels | partial | partial | ✓ | ✓ | ✓ |
| C-28 Single-phase self-test in gap field | ✓ | ✓ | n/a | n/a | n/a |
| C-29 Phase 1 exclusion list | n/a | n/a | ✓ | ✓ | ✓ |
| C-30 Defense cluster co-located on gap field | ✓ | ✓ | ✓ | ✓ | partial* |
| C-31 Named gate block for in-table gap | ✓ | ✓ | ✓ | ✓ | n/a† |
| C-32 Self-check carries disqualifying forms | ✓ | ✓ | ✓ | ✓ | ✓ |

*V-05 C-30 is partial — the three defense mechanisms are distributed across Phase 1 (gap hypothesis) and Phase 2 (self-check + examples), not co-located in one section. This is the testable trade-off of the reversed-sequence design.

†V-05 C-31 is n/a — the gap is written by the Risk Assessor in Phase 1 as a prose field, not a table row, so the named gate block pattern is not applicable. C-19 is satisfied by the prose structure.

**Key trade-off**: V-01 and V-02 are single-phase with inertia bookend and prose-lead innovations respectively; both fail C-20/C-23–C-27/C-29 by design and gain C-28 instead. V-03 and V-04 are two-phase with handoff receipts and first-person register respectively; both gain the full role-separation cluster. V-05 tests the reversed-sequence hypothesis at the cost of C-30 precision — the defense cluster is temporal rather than spatial, which the rubric may or may not credit as equivalent.

**Expected aspirational profiles (v11, 24 criteria):**

| Variation | Design | Expected aspirational | Composite ceiling |
|---|---|---|---|
| V-01 | Single-phase, inertia bookend, C-32 self-check | ~16/24 (fails C-20/C-23–C-27/C-29) | ~96.7 |
| V-02 | Single-phase, prose-lead, C-32 self-check | ~16/24 (fails C-20/C-23–C-27/C-29) | ~96.7 |
| V-03 | Two-phase, handoff receipts, C-32 self-check | ~23/24 (C-30 partial risk) | ~99.6 |
| V-04 | Two-phase, first-person register, column tags, C-32 | ~24/24 | ~100.0 |
| V-05 | Two-phase reversed, inertia co-owned, C-32 | ~22/24 (C-30 partial, C-25 structural) | ~99.2 |
