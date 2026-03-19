Written to `simulations/quest/variations/validate-inertia-variations-R3-2026-03-17.md`.

---

## validate-inertia Variations R3

| # | Label | Axis | Primary targets |
|---|-------|------|-----------------|
| V-11 | Kill barrier temporal persistence gate | Kill barrier qualification | C-14 |
| V-12 | Four-part labeled causal chain | Output format / structural labeling | C-15, C-13 |
| V-13 | Mitigation confirmation signal | Lifecycle emphasis (forward anchor in AMEND) | C-16 |
| V-14 | Competitive displacement + temporal persistence | Combination: inertia framing + temporal | C-11, C-14 |
| V-15 | Full integration | Combination: all aspirational axes | C-09--C-16 |

---

### Variation design rationale

**V-11** — Pure C-14 test. Adds a two-horizon gate to Phase 4 only: the kill barrier must be affirmed at T=0 AND confirmed to persist at T=18mo absent deliberate intervention. A barrier that resolves through product maturity fails the gate and must be reselected. Every other section is left unchanged so the gate's contribution to C-14 is cleanly isolated.

**V-12** — Pure C-15 test. Phase 4 requires exactly four numbered, labeled sub-parts: (1) barrier definition, (2) structural persistence, (3) intervention target, (4) lever efficacy. The prompt explicitly prohibits merging any two. Sub-part (4) also drives C-13 because it must state *why* the lever reaches the structural condition — the causal connection, not the result. Expected C-11 PARTIAL: structural reasoning is required but competitive-displacement framing is not.

**V-13** — Pure C-16 test. Every section is standard except AMEND gets a fourth required subfield: **Confirmation signal at T=6mo** — a named, falsifiable observable condition. The prompt specifies that vague forward hopes fail; the signal must be something that could be observed as absent. C-13 also benefits since the confirmation signal presupposes articulating the causal mechanism.

**V-14** — C-11 + C-14 combination. Rebuilds V-08's competitive inventory (Dimension/Advantage/Durability with the familiarity-disqualifier — the only R2 mechanism that fully closed C-11) and layers the T=0/T=18mo qualification gate on top. V-08 scored 110/130; the temporal gate adds C-14 without disturbing the competitive framing that closes C-11.

**V-15** — Maximum combination. Eight structural mechanisms stacked across seven phases: methodology declaration before personas (C-09), competitive inventory with durability (C-11), named social proof threshold in table (C-12), scores traced to Phase 1 methodology (C-09), four-part kill barrier with temporal gate (C-15 + C-14), adoption timeline grid T=0/T=6mo/T=18mo (C-10), AMEND with four-part chain and confirmation signal (C-13 + C-16). Expected ceiling: 160/160 if all phases execute cleanly.
n top
of that base. Expected coverage: C-11 (full pass via competitive inventory + durability
argument), C-12 (named threshold), C-13 (structural durability reference required in mitigation),
C-14 (temporal gate on competitive advantage). C-09 and C-15 are not targeted.

**V-15 (full integration)** — Maximum combination targeting all eight aspirationals. Phase 1
requires methodology declaration before personas (C-09). Phase 2 maps personas as competitive
inventory with Dimension/Advantage/Durability (C-11). Phase 3 inertia table with named social
proof threshold (C-12). Phase 4 per-persona scores traced to Phase 1 methodology (C-09). Phase 5
kill barrier uses four labeled sub-parts (C-15) with temporal persistence gate (C-14). Phase 6
adoption timeline grid T=0/T=6mo/T=18mo (C-10). AMEND has four-part mitigation chain with
confirmation signal (C-13, C-16). If all phases are structurally enforced, maximum possible
score is 160/160.

---

### V-11: Kill Barrier Temporal Persistence Gate

**Axis:** Kill barrier qualification — temporal persistence
**Hypothesis:** A gated T=0/T=18mo qualification test on the kill barrier will close C-14
without requiring changes to any other section. The gate is structural: a barrier that resolves
by T=18mo through product maturity or organic adoption does not qualify and must be replaced.

---

You are running **validate-inertia** for: {{topic}}

Stress-test adoption inertia. Why would users NOT adopt this feature even if it works perfectly?

---

## Phase 1 — Persona Identification

Name 2--4 user personas. Each must have:

- **Name and role** — specific job title or function, not a category
- **Current workaround** — the specific tool or method they use today (not "ad hoc" — name what
  they actually do)
- **Outcome they optimize for** — what job the current workaround successfully does for them

A persona without a named current workaround does not qualify. Do not proceed to Phase 2 until
all personas are listed.

---

## Phase 2 — Inertia Dimension Analysis

For each persona, assess:

| Persona | Workaround satisfaction (H/M/L) | Basis | Switching cost (quantified) | Habit lock-in (named behavior) | Social proof req. (named threshold) | Learning curve |
|---------|--------------------------------|-------|----------------------------|-------------------------------|-------------------------------------|---------------|

Column rules:

- **Workaround satisfaction:** Rate H/M/L with one phrase saying why that level of satisfaction
  creates inertia — even L satisfaction must explain why any satisfaction is sticky.
- **Switching cost:** Required as a measurable value — time estimate, step count, effort rating
  (1--10), or relative ratio. Qualitative-only ("it's hard") fails.
- **Habit lock-in:** Name the specific behavior that has become automatic (keyboard shortcuts,
  naming conventions, mental models). "General familiarity" is not a named behavior.
- **Social proof req.:** Name the specific threshold or condition — not binary Y/N. Examples:
  "needs 2+ teammates on the same tool before committing," "will adopt solo if manager mandates
  it." Binary answers fail.

---

## Phase 3 — Per-Persona Inertia Scores

Assign each persona an inertia score: **Low / Medium / High / Critical**.

For each score, provide one sentence naming the primary inertia driver.

Every Phase 1 persona must be scored. A single shared score for multiple personas does not pass.

---

## Phase 4 — Kill Barrier Identification

Identify the single adoption killer — the one factor that would block adoption even if all other
inertia were resolved.

**Initial identification:**

- **Kill barrier:** [name it precisely]
- **Why it survives all other mitigations:** [the structural reason — not just that it exists,
  but what property makes it persist]
- **Persona most exposed:** [which persona faces this barrier most acutely]

**Temporal persistence test** — the barrier must pass both horizons to qualify as the kill
barrier:

> **T=0 qualification:** Does this barrier exist today for the most exposed persona? [YES / NO]
>
> If NO: this factor does not currently block adoption — reselect a barrier that exists now.

> **T=18mo qualification:** Does this barrier remain unresolved at 18 months — assuming the
> feature ships, matures, and accumulates organic adoption effects — absent a deliberate
> structural intervention? [YES / NO]
>
> If NO: this is adoption friction that time and product maturity will erode — it is not a kill
> barrier. Reselect a barrier that persists structurally.

Both qualifications must be YES. Label the confirmed result **KILL BARRIER** before proceeding.

Do not proceed to Phase 5 until the kill barrier passes the temporal persistence test.

---

## Phase 5 — Overall Adoption Inertia Risk

Produce an aggregate verdict: **Low / Medium / High / Critical**.

Include:

- Score distribution across personas (e.g., "2 High, 1 Medium, 1 Critical")
- Trajectory direction (Stable / Worsening / Resolving over 18 months)
- 1--2 sentence rationale connecting score distribution, trajectory, and confirmed kill barrier

---

## AMEND

Focus the analysis. Identify the single persona most exposed to the confirmed kill barrier.

- **Focus persona:** [name]
- **Switching cost (refined):** [sharpen the quantified value from Phase 2 — be as specific as
  possible]
- **Kill barrier restated:** [one crisp sentence naming the barrier and why it persists for this
  persona specifically]
- **Mitigation:** [one concrete intervention that could reduce or eliminate the kill barrier —
  explain why this specific lever addresses the structural reason the barrier exists, not just
  what the intervention does]

---

### V-12: Four-Part Labeled Causal Chain

**Axis:** Output format / structural labeling in kill barrier section
**Hypothesis:** Requiring exactly four labeled sub-parts in the kill barrier analysis —
explicitly named and ordered — will close C-15 by making the "what" vs "why" separation a
formatting requirement. It also drives C-13: sub-part (4) must state why the lever resolves the
structural root cause, not just what it does.

---

You are running **validate-inertia** for: {{topic}}

Stress-test adoption inertia. Why would users NOT adopt this feature even if it works perfectly?

---

## Step 1 — Persona Mapping

Name 2--4 user personas. Each requires:

- **Name and role** (specific, not categorical)
- **Current workaround** (name the actual tool or method — "ad hoc" is not a named workaround)
- **Primary resistance property** (one phrase capturing why this persona resists change)

---

## Step 2 — Switching Cost and Inertia Dimensions

For each persona:

| Persona | Workaround satisfaction (H/M/L) | Basis | Switching cost (quantified) | Habit lock-in (named behavior) | Social proof threshold (named condition) | Learning curve |
|---------|--------------------------------|-------|----------------------------|-------------------------------|------------------------------------------|---------------|

- **Switching cost:** Quantified — time, steps, effort rating (1--10), or relative measure.
  Required. Qualitative descriptions alone do not pass.
- **Social proof threshold:** Name a specific count, role, or condition — not binary Y/N.
  Examples: "needs 2 colleagues already using it," "will adopt solo if manager endorses in a
  team meeting."
- **Habit lock-in:** Name the specific repeated behavior, not generic familiarity.

---

## Step 3 — Per-Persona Inertia Scores

Assign Low / Medium / High / Critical to each persona.

One sentence per score stating the primary driver.

Every Step 1 persona must appear. A shared blanket score does not pass.

---

## Step 4 — Kill Barrier: Four-Part Causal Analysis

Identify the single adoption killer — the one factor that would block adoption even if all other
inertia were resolved. Analyze it using exactly **four labeled sub-parts**. Each sub-part must be
distinct. Do not merge any two into a single statement.

**KILL BARRIER**

**(1) Barrier definition**
[What the barrier is — the observable adoption friction, stated precisely. Describe the
phenomenon as the user experiences it. Do not include its cause here.]

**(2) Structural persistence**
[Why this barrier structurally persists — the underlying property or condition that prevents it
from self-resolving through product maturity, improved UX, or organic adoption over time. Do not
repeat (1). Name the structural mechanism that keeps the barrier alive even as the feature
matures.]

**(3) Intervention target**
[What a mitigation must target — the specific lever point that, if addressed, would disrupt the
structural persistence mechanism described in (2). Name the target, not the intervention itself.
"Improve onboarding" is an intervention; "the information asymmetry that makes setup feel
opaque" is a target.]

**(4) Lever efficacy**
[Why addressing the target in (3) resolves the structural root cause in (2). Explain the causal
connection. "It reduces friction" describes a result; explain why this lever reaches the
structural condition named in (2). The explanation must reference (2) by name.]

Label the most exposed persona after the four sub-parts.

---

## Step 5 — Overall Adoption Inertia Risk

Aggregate verdict: Low / Medium / High / Critical.

- Score distribution across personas
- 1--2 sentence rationale tied to the kill barrier and per-persona distribution

---

## AMEND

Focus on the persona most exposed to the kill barrier.

- **Focus persona:** [name]
- **Switching cost (quantified):** [sharpened measurable value]
- **Kill barrier for this persona:** [one sentence restating the barrier in terms of this
  persona's specific situation]
- **Mitigation:** [intervention targeting the lever point from Step 4(3) — explain why it
  resolves the structural root cause from Step 4(2), referencing the structural mechanism by
  name]

---

### V-13: Mitigation Confirmation Signal

**Axis:** Lifecycle emphasis — forward anchor in AMEND
**Hypothesis:** A dedicated "Confirmation signal at T+6mo" subfield in the AMEND section will
close C-16 by requiring a falsifiable leading indicator at a named future time point. The signal
must name what you would observe, not what you hope will happen.

---

You are running **validate-inertia** for: {{topic}}

Map adoption inertia. Why would users not adopt this feature even if it works perfectly?

---

## Phase 1 — Personas

Identify 2--4 named personas. Each must have:

- Name and role (specific, not a category)
- Named current workaround (the actual solution they use today — "ad hoc" is not a named
  workaround)
- Outcome the current workaround successfully delivers for them

---

## Phase 2 — Inertia Dimensions per Persona

| Persona | Workaround satisfaction (H/M/L) | Why that satisfaction is sticky | Switching cost (quantified) | Habit lock-in (named behavior) | Social proof req. (name the threshold) | Learning curve |
|---------|--------------------------------|---------------------------------|----------------------------|-------------------------------|----------------------------------------|---------------|

- Switching cost must be expressed as time, steps, effort rating (1--10), or relative measure.
  Qualitative descriptions ("it's significant") do not pass.
- Social proof: state a named condition — "needs 2 colleagues already using it," "adopts solo
  if manager endorses in a team meeting." Binary Y/N does not pass.

---

## Phase 3 — Per-Persona Inertia Scores

Score each persona: Low / Medium / High / Critical.

One sentence per persona stating the primary inertia driver.

Every Phase 1 persona requires a score. No shared scores.

---

## Phase 4 — Kill Barrier

Name exactly one adoption killer — the single barrier that would block adoption even if
everything else were resolved.

- **Kill barrier:** [name it]
- **Why it survives:** [the structural reason this barrier persists even as the product matures
  and organic adoption accumulates]
- **Most exposed persona:** [name]

---

## Phase 5 — Overall Risk

Verdict: Low / Medium / High / Critical.

Score distribution + trajectory direction (Stable / Worsening / Resolving) + 1--2 sentence
rationale connecting distribution, trajectory, and kill barrier.

---

## AMEND — Per-Persona Focus + Mitigation

Select the persona most exposed to the kill barrier.

**Focus persona:** [name]

**Switching cost (sharpened):** [most precise quantified value you can give for this persona]

**Kill barrier for this persona:** [one sentence restating what it is and why it matters
specifically for them]

**Mitigation:**

> **Intervention:** [what to do — one concrete, specific action]
>
> **Root cause addressed:** [which structural reason from Phase 4 this intervention targets —
> quote or directly reference the "why it survives" language]
>
> **Why this lever works:** [the causal mechanism — explain why this intervention addresses the
> structural root cause, not just what it does. "It reduces friction" is a result, not a
> mechanism. Explain the causal connection to the root cause named in Phase 4.]
>
> **Confirmation signal at T=6mo:** [Name a specific leading indicator or observable condition
> that would confirm the intervention is working at six months. Example: "At T=6mo, the focus
> persona's team shows at least 25% trial rate without a dedicated onboarding champion driving
> adoption." Vague forward hopes ("users will feel more comfortable") do not qualify. The signal
> must be falsifiable — it must be possible to observe it as absent.]

The confirmation signal must name a concrete observable. It is not complete without one.

---

### V-14: Competitive Displacement + Temporal Persistence

**Axis:** Combination — inertia framing (C-11) + temporal qualification (C-14)
**Hypothesis:** Combining V-08's competitive inventory (Dimension/Advantage/Durability with the
familiarity-disqualifier — the only mechanism that fully closed C-11 in R2) with an explicit
T=0/T=18mo qualification gate on the kill barrier will close both C-11 and C-14 in one
variation. V-08 scored 110/130 without C-14; this variation adds the temporal gate to its base.

---

You are running **validate-inertia** for: {{topic}}

The current solution is a competitor. Map why the status quo would win the adoption contest even
if this feature ships and works perfectly.

---

## Phase 1 — Competitive Inventory

Identify 2--4 personas. For each persona, map their current solution as a competitor:

| Persona | Role | Current solution (named) | Outcome it delivers |
|---------|------|--------------------------|---------------------|

For each current solution, record its competitive strengths:

| Dimension | Advantage | Durability |
|-----------|-----------|------------|

- **Dimension:** The specific axis on which the current solution wins (e.g., zero-setup cost,
  output format compatibility, existing keyboard shortcuts, audit trail depth).
- **Advantage:** What the current solution does better on that dimension for this persona.
- **Durability:** Why this advantage is structurally hard to replicate or displace. Must
  reference a structural constraint — a technical property, organizational norm, integration
  dependency, or switching-cost asymmetry. **Familiarity is not durability.** "People are used
  to it" does not qualify. Name the structural constraint that makes the advantage persist even
  after the new feature is available and known.

---

## Phase 2 — Inertia Factor Analysis

For each persona:

| Persona | Workaround satisfaction (H/M/L) | Satisfaction basis (ref. competitive strength) | Switching cost (quantified) | Habit lock-in (named behavior) | Social proof threshold (named condition) |
|---------|--------------------------------|-----------------------------------------------|----------------------------|-------------------------------|------------------------------------------|

- **Satisfaction basis:** Reference a named competitive strength from Phase 1 — not a vague
  sentiment.
- **Switching cost:** Time, steps, effort rating (1--10), or relative measure. Required.
  Qualitative descriptions alone do not pass.
- **Social proof threshold:** Name the specific count, role, or condition. Not binary Y/N.
  Examples: "will adopt if 2 teammates have used it for more than one sprint without rollback,"
  "solo adopter if switching cost drops below 4 hours."

---

## Phase 3 — Per-Persona Inertia Scores

Score each persona: Low / Medium / High / Critical.

One sentence per persona anchored in a named competitive strength from Phase 1.

Every Phase 1 persona must be scored individually.

---

## Phase 4 — Kill Barrier (competitive framing)

Identify the single adoption killer — expressed as the competitive dimension on which the current
solution wins and that this feature cannot displace without a deliberate structural intervention.

**Kill barrier:** [Name the competitive dimension. Example: "The current solution wins on
zero-ramp time — any new tool requires setup investment the current solution never required."]

**Durability argument:** [Explain why this competitive advantage is structurally durable.
Reference the structural constraint from Phase 1. "Users are used to it" fails — name the
property that makes the advantage persist structurally.]

**Temporal persistence test:**

> **T=0 qualification:** Does this competitive advantage exist today? [YES / NO]
>
> If NO: this factor is not a current blocker — reselect.

> **T=18mo qualification:** Does this competitive advantage persist at 18 months — assuming the
> feature ships, matures, and accumulates organic adoption — absent a deliberate structural
> intervention targeting the durability property? [YES / NO]
>
> If NO: this is temporary competitive friction that maturation will erode — it is not a kill
> barrier. Reselect a competitive dimension with structural durability through the full horizon.

Both qualifications must be YES. Label this **CONFIRMED KILL BARRIER**.

**Most exposed persona:** [name]

---

## Phase 5 — Overall Adoption Inertia Risk

Verdict: Low / Medium / High / Critical.

- Competitive summary: name the kill barrier dimension and its structural durability basis
- Score distribution across personas
- 1--2 sentence rationale anchored in kill barrier durability and per-persona score distribution

---

## AMEND

**Focus persona:** [most exposed to the confirmed kill barrier]

**Switching cost (refined):** [sharpest quantified value for this persona]

**Kill barrier restated:** [one sentence: the competitive dimension + structural durability +
why this persona specifically is most exposed]

**Mitigation:** [one concrete intervention — explain why it directly addresses the structural
durability property of the kill barrier, not just what the intervention does. A mitigation that
only reduces familiarity friction without targeting the named structural constraint does not
pass.]

---

### V-15: Full Integration — All Aspirationals

**Axis:** Combination — methodology (C-09) + temporal grid (C-10) + competitive (C-11) +
named social proof (C-12) + root cause chain (C-13) + temporal persistence gate (C-14) +
labeled causal sub-parts (C-15) + confirmation signal (C-16)
**Hypothesis:** Stacking all eight aspirational axes into one structurally-gated variation will
achieve the highest possible score on the v3 rubric. Each phase targets one or more aspirationals
structurally — not as suggestions but as format requirements the output cannot satisfy by
omission.

---

You are running **validate-inertia** for: {{topic}}

Map adoption inertia. Why would users not adopt this feature even if it works perfectly? Complete
each phase in sequence. Each phase gates the next.

---

## Phase 1 — Scoring Methodology Declaration

Before analyzing any persona, declare the inertia scoring framework that will govern per-persona
scores in Phase 4.

**Dimension weights:**

| Dimension | Weight (High / Medium / Low) | Why this weight |
|-----------|------------------------------|-----------------|

Dimensions to weight: Workaround satisfaction / Switching cost / Habit lock-in / Social proof
requirements / Learning curve.

**Score thresholds:** Define the dimension-combination rules that produce each tier:

- **Critical:** [state which dimension combinations produce this tier]
- **High:** [state which combinations produce this tier]
- **Medium:** [state which combinations]
- **Low:** [state which combinations]

Do not proceed to Phase 2 until the methodology is declared. Per-persona scores in Phase 4 must
demonstrably follow from this framework — they cannot be assigned independently.

---

## Phase 2 — Persona and Competitive Inventory

Identify 2--4 named personas. For each persona, treat the current solution as a named
competitor:

**Persona entry:**

- Name and role (specific, not categorical)
- Current solution (named tool or method — "ad hoc" is not a solution; name what they actually
  do)
- Outcome the current solution delivers

**Competitive strength inventory** — for each strength the current solution has:

| Dimension | Advantage | Durability |
|-----------|-----------|------------|

Durability must reference a structural constraint (technical, organizational, integration-based,
or switching-cost-based). **Familiarity is not durability.** A strength listed without a
structural basis does not qualify and must be removed or replaced.

---

## Phase 3 — Inertia Dimension Analysis

For each persona:

| Persona | Workaround satisfaction (H/M/L) | Satisfaction basis (ref. Phase 2 competitive strength) | Switching cost (quantified) | Habit lock-in (named behavior) | Social proof threshold | Learning curve |
|---------|--------------------------------|-------------------------------------------------------|----------------------------|-------------------------------|------------------------|---------------|

- **Switching cost:** Time, steps, effort rating (1--10), or relative measure. Required.
  Qualitative descriptions do not pass.
- **Satisfaction basis:** Reference a named competitive strength from Phase 2 — not a vague
  sentiment.
- **Social proof threshold:** Name a specific count, role, or condition — not binary Y/N.
  Examples: "needs 2 colleagues using it for more than one sprint," "will adopt solo if manager
  endorses at team standup." Binary answers fail.

---

## Phase 4 — Per-Persona Inertia Scores

Score each persona: Low / Medium / High / Critical.

For each persona:

- **Score:** [Low / Medium / High / Critical]
- **Methodology trace:** [one sentence connecting the Phase 3 dimension values to the Phase 1
  threshold that produces this score — show the derivation, do not just assert the tier]

Every Phase 2 persona must be scored individually. A shared blanket score does not pass.

---

## Phase 5 — Kill Barrier: Four-Part Causal Analysis

Identify the single adoption killer — expressed as the competitive dimension on which the
current solution wins. Use exactly **four labeled sub-parts**. Each must be distinct. Do not
merge any two into a single statement.

**KILL BARRIER**

**(1) Barrier definition**
[What the barrier is — the observable adoption friction as the most exposed persona experiences
it. State the competitive dimension. Describe the phenomenon; do not include its cause here.]

**(2) Structural persistence**
[Why this barrier structurally persists — the underlying property from the Phase 2 competitive
inventory that prevents it from self-resolving through product maturity or organic adoption.
Do not repeat (1). Name the structural mechanism and reference the relevant Phase 2 durability
property by name.]

**(3) Intervention target**
[What a mitigation must target — the specific lever point that, if addressed, would disrupt the
structural persistence mechanism described in (2). Name the target, not the intervention.
"Better onboarding" is an intervention; "the information gap that makes migration feel
irreversible" is a target.]

**(4) Lever efficacy**
[Why addressing (3) resolves the structural root cause in (2). Explain the causal connection.
Reference (2) by name. "It reduces friction" states a result; explain why this lever reaches
the structural condition named in (2).]

**Temporal persistence test:**

> **T=0 qualification:** Does this barrier exist today? [YES / NO]
>
> **T=18mo qualification:** Does this barrier persist at 18 months — absent a deliberate
> structural intervention targeting the durability property? [YES / NO]
>
> If either is NO: reselect. Only a barrier that passes both horizons qualifies as the kill
> barrier.

Label the confirmed result **CONFIRMED KILL BARRIER**. Name the most exposed persona.

Do not proceed to Phase 6 until the kill barrier passes both temporal qualifications.

---

## Phase 6 — Adoption Timeline Sensitivity

For the confirmed kill barrier and at least two personas, project inertia across three horizons:

| Persona | T=0 score | T=6mo score | T=18mo score | Trajectory | Driver of change |
|---------|-----------|-------------|--------------|------------|-----------------|

- Trajectory: Resolving / Stable / Worsening
- At least one trajectory must be non-flat. T=6mo and T=18mo values cannot be copied from T=0
  without a stated reason why nothing changes.
- **Kill barrier time-sensitivity verdict:** Resolving / Stable / Worsening — with one sentence
  of structural reasoning tied to the persistence property in Phase 5(2).

---

## Phase 7 — Overall Adoption Inertia Risk

Verdict: Low / Medium / High / Critical.

- Score distribution across personas (e.g., "2 High, 1 Critical, 1 Medium")
- Trajectory direction from Phase 6
- Competitive summary: the kill barrier dimension and its Phase 2 structural durability basis
- 1--2 sentence rationale connecting score distribution, trajectory, and confirmed kill barrier

---

## AMEND — Focus, Quantify, Confirm

Select the persona most exposed to the confirmed kill barrier.

**Focus persona:** [name]

**Switching cost (sharpened):** [most precise quantified value — time, steps, effort rating, or
relative measure]

**Kill barrier for this persona:** [one sentence restating the barrier in terms of this
persona's specific situation — name the competitive dimension and why it is most acute for them]

**Mitigation with full causal chain:**

> **(a) Intervention:** [one concrete, specific action]
>
> **(b) Root cause addressed:** [which structural condition from Phase 5(2) this targets —
> quote or directly reference the persistence property by name]
>
> **(c) Causal mechanism:** [why this lever resolves the structural root cause — the causal
> connection. Reference the intervention target from Phase 5(3). Do not describe what happens;
> explain why this lever reaches the structural condition.]
>
> **(d) Confirmation signal at T=6mo:** [A specific leading indicator or observable condition
> that would confirm the intervention is working at six months. Name what you would measure or
> observe. Example: "At T=6mo, the focus persona's team shows at least 25% trial rate without
> a dedicated onboarding champion, indicating the structural switching cost barrier has been
> reduced to below the spontaneous adoption threshold." Vague forward hopes ("users will feel
> more comfortable") do not qualify. The signal must be falsifiable — it must be possible to
> observe it as absent.]

The confirmation signal must be an observable, not a hope. The AMEND section is not complete
without it.
