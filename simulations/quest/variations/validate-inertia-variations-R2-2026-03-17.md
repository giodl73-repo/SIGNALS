Written to `simulations/quest/variations/validate-inertia-variations-R2-2026-03-17.md`.

---

## validate-inertia Variations R2

| # | Label | Axis | Primary target |
|---|-------|------|----------------|
| V-06 | Scoring methodology first | Role sequence | C-09 |
| V-07 | Timeline-indexed inertia | Output format | C-10 |
| V-08 | Competitive displacement with durability argument | Inertia framing | C-11 |
| V-09 | Social proof ladder | Lifecycle emphasis | C-12 |
| V-10 | Root cause mitigation chain | Combination | C-10, C-12, C-13 |

---

### What each variation does and why

**V-06 (methodology first)** — Role sequence axis. Inverts the standard order: Phase 1 requires the model to declare dimension weights and score thresholds *before* it sees any persona. This prevents post-hoc rationalization of scores, which is why C-09 fails in all R1 variations — methodology is always an afterthought there. A declared weighting framework also anchors C-02 quantification: once the model has committed "switching cost is weighted 2x because it's the primary reversibility constraint," the per-persona switching cost fields must be concrete enough to actually apply that threshold.

**V-07 (timeline-indexed inertia)** — Output format axis. Replaces the static snapshot with a temporal grid (T=0, T=6mo, T=18mo). C-10 fails across all R1 variations because "time-dependent" is not a natural output of a static format — you can fill every field without ever asking how inertia evolves. The grid forces it structurally: T=6mo and T=18mo cannot be copied from T=0. The kill-barrier qualification test (must persist across the full window) separates structural blockers from addressable friction.

**V-08 (competitive displacement with durability)** — Inertia framing axis. V-03 and V-05 in R1 named the winning dimension but rarely explained why that advantage is *structurally durable*. This variation requires, per strength: Dimension / Advantage / Durability — where Durability must reference a structural constraint ("300+ downstream scripts reference the output format") rather than a preference ("users are comfortable with it"). Familiarity is explicitly called out as not qualifying. This directly closes C-11.

**V-09 (social proof ladder)** — Lifecycle emphasis axis. Replaces binary Y/N social proof with a four-rung ladder (Not watching → Watching → Evaluating → Adopting). Rung 3 must be a named condition: count, role, use case, or organizational trigger. Binary answers without a named threshold structurally fail the rung. This is the minimum structural change needed to close C-12, which fails universally in R1 because the social proof field accepts "needs peers" as complete.

**V-10 (root cause mitigation chain)** — Combination. Targets C-10 + C-12 + C-13 without structural conflict. The four-part causal chain in AMEND (root cause → persistence property → lever → mechanism) closes C-13 by requiring the model to trace *why* the intervention neutralizes the specific structural constraint — not just what it does. The timeline step (Step 5) closes C-10. Named social proof thresholds throughout close C-12. The three axes appear in different sections and do not compete.
rst (role sequence axis)

**Axis:** Role sequence -- the scoring methodology is declared as Phase 1 before any persona is named or scored. The model commits to which dimensions it will weight most heavily and what dimension combinations produce each score tier. Scores must demonstrably follow from the declared methodology.

**Hypothesis:** C-09 (inertia score methodology explained) fails in R1 because methodology is positioned as an afterthought -- the model produces scores and then reverse-engineers a justification. When methodology is required as a Phase 1 prerequisite with an explicit "scores must follow from this" check, the model cannot float scores freely. The declared weighting framework also improves C-02 and C-03 consistency: once the model has stated "switching cost is weighted 2x because it is the primary reversibility constraint for this feature class," per-persona scores will follow that logic with measurable anchors rather than impressionistic labels.

```
You are running /validate:inertia for topic: {topic}.

Feature under adoption stress-test: {feature}

This skill stress-tests the adoption case. The goal is not to evaluate feature quality --
assume it works perfectly. The question is: why would the right users still not switch?

Before you assess any persona, you will declare your scoring methodology. Your inertia scores
must demonstrably follow from that methodology. This prevents post-hoc rationalization.

=== PHASE 1: SCORING METHODOLOGY ===

Declare how you will score inertia for this specific feature and user population. Address all
five inertia dimensions and set the thresholds that will determine each score tier.

Dimension weights (complete all five):

  Workaround satisfaction
    Weight: [High / Medium / Low relative to the other four dimensions for this feature]
    Reason: [one sentence -- why this dimension matters more or less for this specific feature
      class; reference a property of the feature or its user population]

  Switching cost
    Weight: [High / Medium / Low]
    Reason: [one sentence]

  Habit lock-in
    Weight: [High / Medium / Low]
    Reason: [one sentence]

  Social proof requirement
    Weight: [High / Medium / Low]
    Reason: [one sentence]

  Learning curve
    Weight: [High / Medium / Low]
    Reason: [one sentence]

Score thresholds (define what dimension combinations produce each tier):

  Low inertia: [the combination of dimension levels that would produce this verdict --
    e.g., "requires Low or Medium on all five dimensions, including switching cost below 4/10"]

  Medium inertia: [the minimum qualifying combination -- at least one dimension that triggers
    Medium or High, with the others not compensating]

  High inertia: [what must be true -- e.g., "at least two high-weight dimensions rated High,
    or one Critical-equivalent (e.g., workaround satisfaction = H AND switching cost >= 6/10)"]

  Critical inertia: [the adoption-blocking threshold -- what combination makes this persona
    unlikely to switch absent a structural change]

This methodology applies to all personas. If a persona's score deviates from what the
methodology would predict, flag the deviation and explain it.

=== PHASE 2: PERSONA IDENTIFICATION ===

Name 2-4 user personas who are plausible adopters of this feature. For each:
  (a) Name and brief role (one sentence)
  (b) The outcome they currently achieve without this feature
  (c) The named current workaround -- the specific tool, workflow, or process they use today

Every persona must have a named current workaround. A persona entry without one is incomplete.

=== PHASE 3: INERTIA FACTOR ANALYSIS ===

For each persona, assess all five dimensions. Apply the methodology declared in Phase 1.

  Workaround satisfaction: H / M / L -- how well the current workaround meets this persona's
    need. One phrase: why any satisfaction (even L) creates resistance to switching.

  Switching cost: [quantified] -- the cost to migrate from the current workaround to this
    feature. Required formats:
    - Time: "~X hours migration + Y days ramp"
    - Steps: "N discrete steps, M of which require manual verification"
    - Effort rating: "X/10 compared to [a comparable task this persona has performed]"
    - Relative: "Nx the setup cost of [specific action this persona takes regularly]"
    Qualitative descriptions alone ("significant effort," "it's hard") do not pass.

  Habit lock-in: the specific behavioral pattern that resists change. Name the concrete habit,
    not the category. Not "uses keyboard shortcuts" but "runs 3 fixed terminal commands from
    muscle memory 30+ times daily."

  Social proof requirement: does this persona adopt individually or wait for peer signals?
    Characterize as: solo adopter / needs peer proof / unclear. One sentence basis.

  Learning curve: Low / Medium / High + the specific knowledge delta required.

=== PHASE 4: PER-PERSONA INERTIA SCORES ===

Assign each persona an inertia score. Apply the Phase 1 thresholds.

Format per persona:
  [Persona name]: [Score: Low / Medium / High / Critical]
  Dimension ratings: [list each dimension at its assessed level, e.g., "Satisfaction: H,
    Switching cost: 7/10, Habit lock-in: High, Social proof: needs peers, Learning: Medium"]
  Methodology application: [one sentence -- confirm which Phase 1 threshold this persona
    falls into, or explain any deviation from the declared methodology]
  Primary driver: [the single dimension most responsible for this score]

Every Phase 2 persona must be scored. A shared blanket score for multiple personas does not
pass; the Phase 1 methodology differentiates personas by dimension profile.

=== PHASE 5: KILL-BARRIER IDENTIFICATION ===

Do not proceed to Phase 6 until this phase produces a single named adoption killer.

Review Phase 3 assessments and Phase 4 scores. Identify the one barrier that would survive
even if: switching cost were halved by a migration tool, the learning curve were flattened by
guided onboarding, and early adopters publicly demonstrated success.

ADOPTION KILLER: [barrier name]
Affected persona(s): [names]
Methodology anchor: [which Phase 1 dimension or weight explains why this barrier is irreducible
  -- reference your declared methodology; not "it's the highest rated" but why the specific
  weighting you established in Phase 1 makes this barrier structurally dominant]
Why product improvements won't close it: [the structural property that persists after typical
  product or onboarding improvements are applied]

Only one adoption killer. If two are plausible, select the one that is least addressable
through a change that does not require redesigning the feature's core interaction model.

=== PHASE 6: OVERALL VERDICT ===

OVERALL RISK: [Low / Medium / High / Critical]
Score distribution: [count per tier, e.g., "1 Critical, 2 High, 1 Low"]
Rationale: [1-2 sentences -- connects the Phase 4 score distribution, Phase 1 methodology
  weights, and Phase 5 kill barrier to the overall risk verdict]

=== PHASE 7: AMEND ===

Narrow to the highest Phase 4 inertia persona.

  Persona: [name]
  Switching cost (quantified): [the concrete value from Phase 3 -- must include a unit]
  Kill barrier: [must match the Phase 5 adoption killer]
  Scenario: [one sentence -- the specific moment where this persona encounters the kill barrier
    and decides not to adopt, even though the feature works correctly]
  Mitigation: [one concrete intervention -- feature change, migration tool, pricing lever,
    onboarding redesign, or social proof mechanism -- and why it addresses the structural
    reason the kill barrier persists, not just what it does]

Write artifact to simulations/validate/inertia/{topic}-inertia-{date}.md.
Frontmatter: topic, date, feature, personas (list), persona_count,
scoring_methodology_declared (true/false), kill_barrier, overall_risk,
inertia_scores (map of persona name to Low/Medium/High/Critical).
```

---

## V-07: Timeline-indexed inertia (output format axis)

**Axis:** Output format -- inertia is expressed as a temporal grid rather than a static snapshot. Each persona's inertia is scored at three time horizons (T=0 launch, T=6mo, T=18mo), surfacing how inertia evolves as the feature matures, social proof accumulates, and current workarounds age.

**Hypothesis:** C-10 (adoption timeline sensitivity) fails in all five R1 variations because the prompt treats inertia as a fixed property. In practice, inertia is time-dependent: workaround satisfaction can erode as the workaround ages or becomes unsupported; habit lock-in can deepen as users continue investing in the current workflow; social proof barriers fall as early adopters become visible. A temporal grid format makes time-dependency structurally required -- the T=6mo and T=18mo columns cannot be filled by copying T=0, because the prompt asks explicitly "how has inertia changed and why?" The kill-barrier qualification test (must persist across the full T=0--T=18mo window) distinguishes structural barriers from addressable friction.

```
You are running /validate:inertia for topic: {topic}.

Feature under adoption stress-test: {feature}

Inertia is not a fixed property. A user who will not switch today may switch in six months,
or may be more entrenched in eighteen months. This skill maps inertia across three time
horizons: at launch (T=0), at six months post-launch (T=6mo), and at eighteen months (T=18mo).

PERSONA IDENTIFICATION

Name 2-4 user personas who are plausible adopters of this feature. For each:
  (a) Name and brief role (one sentence)
  (b) The outcome they currently achieve without this feature
  (c) The named current workaround -- the specific tool, workflow, or process they use today

INERTIA FACTOR BASELINE (T=0)

At the moment of launch, assess each persona on the five inertia dimensions.

| Persona | Workaround satisfaction | Switching cost (quantified) | Habit lock-in | Social proof req. | Learning curve |
|---------|------------------------|----------------------------|---------------|-------------------|----------------|

Column requirements:

  Workaround satisfaction: H (fully or near-fully meets the need) / M (partial) / L (unreliable
    or painful). One qualifying phrase per cell.

  Switching cost: must be a concrete measurable value. Accepted formats:
    - Time: "~6 hours migration + 2 days ramp"
    - Steps: "5-step reconfiguration, 2 require manual data verification"
    - Effort rating: "7/10 compared to the team's last toolchain migration"
    - Relative: "3x the setup cost of renewing their current annual license"
    Qualitative descriptions alone ("it's hard," "high effort") do not pass.

  Social proof req.: name the specific threshold or condition, not binary Y/N. Examples:
    "needs 2+ colleagues on the same tool before committing," "will adopt solo if it
    eliminates her Friday reporting task," "requires manager endorsement in team standup."

  Habit lock-in and Learning curve: H/M/L with one qualifying phrase.

PER-PERSONA INERTIA SCORES AT T=0

| Persona | Inertia score (T=0) | Primary driver |
|---------|---------------------|----------------|

Scale: Low / Medium / High / Critical (standard definitions apply).
Primary driver: the single dimension from the baseline table that most explains the T=0 score.

INERTIA TRAJECTORY: T=6mo AND T=18mo

For each persona, project how their inertia score changes at six months and eighteen months
post-launch. For each horizon, name the direction and the driver of change.

Factors to consider:
  - Feature maturity: does improving UX, adding migration tooling, or fixing early bugs reduce
    switching cost or learning curve over time?
  - Workaround aging: does the current workaround become harder to maintain, less supported,
    or more expensive as the feature gains adoption?
  - Social proof accumulation: as early adopters become visible within teams and communities,
    does the social proof requirement fall -- and for which personas does it fall fastest?
  - Habit entrenchment: does continued use of the current workflow over six months deepen
    lock-in, particularly for muscle-memory or toolchain-integrated behaviors?
  - Organizational momentum: do team or management signals shift the adoption calculus?

| Persona | Score (T=0) | Score (T=6mo) | Score (T=18mo) | Trajectory | Key driver of change |
|---------|-------------|---------------|----------------|------------|----------------------|

Trajectory: Rising (inertia growing) / Falling (inertia decreasing) / Flat (stable).
Key driver: the single factor most responsible for the trajectory from T=0 to T=18mo.

Requirements:
  - At least one persona must show a non-flat trajectory. If all personas are flat, explain
    why the inertia picture is genuinely time-invariant for this feature.
  - For any persona with a Rising trajectory, explain what is compounding the lock-in.
  - For any persona with a Falling trajectory, name the mechanism (improved tooling, social
    proof threshold met, workaround becoming unsupported, etc.).

KILL-BARRIER IDENTIFICATION

A kill barrier must persist across the full T=0--T=18mo window to qualify. A barrier that
resolves naturally by T=6mo is addressable friction, not a structural adoption killer.

Qualification test: review the trajectory table. The kill barrier must appear as the primary
driver for at least one persona at T=0 and remain unresolved or only partially resolved at T=18mo.

ADOPTION KILLER: [barrier name]
Affected persona(s): [names]
Why time does not resolve it: [the structural property that makes this barrier persist even
  as the feature matures, social proof accumulates, and switching costs fall through tooling
  improvements -- reference the T=18mo trajectory for affected personas]
Earliest resolution window: [the earliest time horizon or condition under which this barrier
  could plausibly be addressed, e.g., "never without a pricing change," "only after >30% of
  the team adopts," "T=18mo if a migration wizard ships at T=6mo"]

OVERALL ADOPTION INERTIA RISK

OVERALL RISK: [Low / Medium / High / Critical -- based on T=0 scores]
Trajectory: [Improving / Worsening / Stable -- the direction of the overall picture at T=18mo
  if no mitigation is applied]
Rationale: [1-2 sentences -- connects T=0 score distribution, overall trajectory, and
  the time-persistent kill barrier]

AMEND

Focus on the persona with the highest T=0 inertia score.

  Persona: [name]
  Switching cost (quantified): [concrete value from the T=0 baseline table]
  Kill barrier: [must match the KILL-BARRIER IDENTIFICATION adoption killer]
  Scenario: [one sentence -- the specific moment at launch (T=0) where this persona
    encounters the kill barrier and decides not to adopt, despite the feature working correctly]
  Mitigation: [the one intervention most likely to shift this persona's T=6mo score downward;
    explain why this lever addresses the structural reason the barrier persists at T=0 and
    what evidence at T=6mo would confirm the mitigation is working]

Write artifact to simulations/validate/inertia/{topic}-inertia-{date}.md.
Frontmatter: topic, date, feature, personas (list), persona_count,
timeline_horizons (["T=0","T=6mo","T=18mo"]), kill_barrier,
kill_barrier_time_persistent (true/false), overall_risk, overall_trajectory,
inertia_scores (map: persona -> {t0: score, t6: score, t18: score}).
```

---

## V-08: Competitive displacement with durability argument (inertia framing axis)

**Axis:** Inertia framing -- for each persona, the current workaround is treated as a named competitor that holds a structural advantage on at least one specific dimension. The analysis must name the winning dimension AND explain why that advantage is structurally durable -- what property of the current solution makes it resistant to displacement, not just that users prefer it today.

**Hypothesis:** C-11 (status-quo framed as named competitor with durable advantage) receives partial credit in R1 V-03 and V-05 because the winning dimension is often named but the durability argument is absent or surface-level ("users are comfortable with it"). The structural durability of a competitive advantage is qualitatively different from familiarity bias: a tool whose output format is referenced by 200+ downstream automations has a durable advantage that is not eroded by "better UX." A prompt that requires an explicit durability explanation -- what would have to change in the feature, the market, or the user's environment for this advantage to erode -- forces kill-barrier reasoning that is actionable for product strategy, not just for user empathy.

```
You are running /validate:inertia for topic: {topic}.

Feature under adoption stress-test: {feature}

The obstacle to adoption is not abstract inertia -- it is the user's current solution, which
already wins on at least one dimension that matters enough to keep users from switching. This
skill maps that competitive position: what does each persona's current solution do well, why
is that advantage structurally durable, and which advantage is most likely to persist even
after this feature is polished, proven, and actively promoted?

COMPETITIVE INVENTORY

Name 2-4 user personas who are plausible adopters of this feature. For each persona, identify
their current solution and its competitive standing.

For each persona:

  Persona: [name and brief role -- one sentence]
  Current solution: [the specific tool, workflow, or process they use today -- not a category]
  Outcome achieved: [what this persona accomplishes using their current solution]

  Competitive strengths of the current solution:

    For each strength, provide all three fields:

    Dimension: [the named axis on which the current solution wins -- e.g., "integration
      depth with existing CI pipeline," "keyboard-first interaction model," "zero-config
      deployment," "output format compatibility with downstream tools"]
    Advantage: [what the current solution does on this dimension that this feature cannot
      yet replicate -- be specific about what capability or property is missing or weaker]
    Durability: [why this advantage persists even if the new feature improves -- what would
      have to change in the feature, the market, or the user's environment for this advantage
      to erode? Examples: "requires protocol-level API support that represents 18+ months of
      build time," "locked in by 300+ existing scripts that reference the output filename
      format," "requires retraining 12-person team on a new mental model at non-trivial
      cost," "advantage is tied to vendor pricing that the new feature cannot match without
      a different business model"]

    A strength that is purely habitual ("users are comfortable with it") without a named
    structural basis does not qualify. Familiarity is not durability.

    Name at least one durable advantage per persona. Name up to three.

INERTIA FACTOR ANALYSIS

For each persona, assess all five inertia dimensions, grounded in the competitive inventory.

  Workaround satisfaction: H / M / L -- how well the current solution serves this persona.
    Basis: one phrase referencing a named competitive strength from the inventory.

  Switching cost: [quantified] -- the cost to move from the current solution to this feature.
    Required: time ("~X hours"), steps (count), effort rating (X/10 vs. a comparable task),
    or relative ("Nx the cost of [specific recurring action this persona takes]"). Qualitative
    descriptions alone do not pass.

  Habit lock-in: the specific behavioral pattern that reflects the current solution's
    competitive advantage. Name the concrete habit that is difficult to displace, not the
    abstract category. Connect it to a named dimension from the competitive inventory.

  Social proof requirement: name the specific threshold or condition. Not Y/N. Examples:
    "will not switch until the team lead publicly models it," "needs 3 peers with the same
    workflow to confirm time savings," "solo adopter -- will trial if switching cost drops
    below 4 hours."

  Learning curve: Low / Medium / High + the specific knowledge or mental model gap.

PER-PERSONA INERTIA SCORES

For each persona, assign an inertia score that reflects how competitive their current
solution is given the full dimension analysis.

  Low = current solution is weak; the persona would switch with minimal incentive
  Medium = current solution has genuine strengths; switching requires meaningful incentive
    or switching cost reduction
  High = current solution is strong; switching requires both incentive AND reduced switching
    cost; at least one durable competitive advantage remains intact
  Critical = current solution is entrenched; adoption requires a structural change beyond
    product improvement (migration tooling, pricing disruption, organizational mandate, or
    the current solution becoming unavailable)

For each persona:
  [Persona name]: [Score]
  Competitive driver: [the named dimension from the competitive inventory that most explains
    this score -- not a generic inertia dimension like "switching cost" but the specific
    dimension on which the current solution wins]
  Score rationale: [one sentence connecting the durable competitive advantage to the score]

KILL-BARRIER IDENTIFICATION

The kill barrier is the competitive advantage held by the current solution that is most
durable across the persona set -- the advantage most likely to persist even after this
feature improves, switching cost falls through tooling, and social proof accumulates.

Review the competitive inventories and inertia scores. Select the one winning dimension
that has the highest structural durability.

ADOPTION KILLER: [expressed as the competitive dimension the current solution wins on --
  not a generic inertia label like "switching cost" but the specific advantage dimension]
Why the current solution wins on this dimension: [the specific property from the Durability
  field in the competitive inventory -- reference it by name]
Why product improvements alone won't close the gap: [what would have to change in the
  feature's fundamental design, business model, or market position for this advantage to erode]
Affected persona(s): [names of the personas for whom this dimension is a primary driver]

OVERALL ADOPTION INERTIA RISK

OVERALL RISK: [Low / Medium / High / Critical]
Competitive summary: [one sentence characterizing the overall competitive strength of current
  solutions across the persona set -- how entrenched are the current solutions as a group?]
Rationale: [one sentence -- anchors the verdict in the kill barrier's durability and the
  per-persona score distribution]

AMEND

Focus on the persona for whom the current solution's competitive position is most entrenched.

  Persona: [name]
  Current solution: [the specific tool or workflow]
  Winning dimension: [the named competitive advantage from the inventory that drives the
    highest inertia for this persona]
  Switching cost (quantified): [the concrete value from the inertia factor analysis]
  Kill barrier: [must match the ADOPTION KILLER -- use the same competitive dimension label]
  Why the advantage is structurally durable: [the specific Durability property from the
    competitive inventory -- one sentence; must reference a structural constraint, not a
    preference or habit]
  Adoption unlock: [what would have to change -- in the feature, in the current solution's
    market position, or in the user's environment -- for the durable advantage to erode
    enough for this persona to switch]
  Mitigation: [one concrete intervention; explain why it directly addresses the structural
    durability property named above, not just what the intervention does]

Write artifact to simulations/validate/inertia/{topic}-inertia-{date}.md.
Frontmatter: topic, date, feature, personas (list), persona_count,
competitive_inventory_completed (true/false), kill_barrier, kill_barrier_durable (true/false),
overall_risk, inertia_scores (map of persona name to Low/Medium/High/Critical).
```

---

## V-09: Social proof ladder (lifecycle emphasis axis)

**Axis:** Lifecycle emphasis -- social proof is elevated from a binary yes/no dimension into a four-rung adoption ladder. A dedicated phase maps the specific observable condition at each rung for each persona. Rung 3 (the tipping condition for adoption) must be expressed as a named count, role, or organizational trigger. Binary "needs peers" / "solo adopter" answers without a named threshold structurally fail the rung.

**Hypothesis:** C-12 (named social proof threshold) fails in V-01--V-04 and receives partial credit only in V-05 because social proof is treated as a binary dimension. The real adoption question is more granular: how many peers, in what role, doing what observable thing for how long would move a hesitant persona from watching to committing? Framing this as a ladder with named rung conditions prevents the model from filing the field with "needs peer proof" (C-12 FAIL) and forces an answer like "needs to see 2 teammates use it in production for one sprint" (C-12 PASS). The ladder also surfaces adoption sequencing structure: when one persona's Rung 3 requires prior adoption by a second persona type, a sequencing dependency emerges that is invisible in binary social proof analysis.

```
You are running /validate:inertia for topic: {topic}.

Feature under adoption stress-test: {feature}

Some users adopt tools alone. Others wait and watch. This skill maps the social conditions
under which each persona would switch -- not whether they need peer proof, but exactly how
much, from whom, and in what form.

PERSONA IDENTIFICATION

Name 2-4 user personas who are plausible adopters of this feature. For each:
  (a) Name and brief role (one sentence)
  (b) The named current workaround -- the specific tool, workflow, or process they use today
  (c) One sentence characterizing whether this persona's tool adoption decisions are typically
    individual or socially conditioned -- based on their role and organizational context

INERTIA DIMENSION ANALYSIS

For each persona, assess four inertia dimensions (social proof is handled separately).

  Workaround satisfaction: H / M / L -- how well the current workaround meets this persona's
    need. One phrase: why any satisfaction (even L) creates adoption resistance.

  Switching cost: [quantified] -- time, steps, effort rating, or relative measure. Required.
    Qualitative descriptions alone ("it's high") do not pass.

  Habit lock-in: the specific behavioral pattern that is integrated into this persona's work.
    Name the concrete habit, not the abstract category.

  Learning curve: Low / Medium / High + the specific knowledge or mental model gap.

SOCIAL PROOF ADOPTION LADDER

For each persona, map the social proof conditions that would move them from their current
state to adoption. The ladder has four rungs. Name the condition at each rung.

  Rung 0 -- Not watching: [what would it take for this persona to notice that others are
    adopting? What signal in their environment -- a mention in Slack, a manager comment, a
    blog post from a peer -- would register at all? If this persona actively monitors new
    tools, note why and proceed to Rung 1 directly.]

  Rung 1 -- Watching: [this persona is aware but not acting; what specific observation of
    peers using the feature would move them from passive awareness to active evaluation?
    Name the observation: what role is the peer, what are they using the feature for, and
    in what context does this persona see it?]

  Rung 2 -- Evaluating: [this persona has started looking seriously; what named condition
    would push them to trial? Name the trigger: a peer count, a specific use case being
    demonstrated, an organizational signal, or a visible outcome metric.]

  Rung 3 -- Adopting: [the tipping condition -- the specific, named threshold at which this
    persona commits. This must be a concrete condition, not a sentiment. Examples:
    "2 teammates on the same team have used it for >1 sprint without rollback"
    "team lead endorses it in a retrospective and offers to co-pilot the migration"
    "sees a colleague solve the exact pain point she has, in under 10 minutes, live"
    "pilot completes with no data loss in first 2 weeks and manager flags the time savings"
    Binary answers ("needs to see peers use it") without a named count, role, or condition
    do not pass this rung.]

For personas who adopt solo (no peer proof required): explicitly state why this persona is
a solo adopter and name the internal threshold that replaces social proof. Examples:
  "will adopt in the first week if the feature eliminates her Friday reporting task on trial"
  "will adopt solo if switching cost drops below 3 hours based on a trial run"
  "adopts any tool that passes a personal 30-minute friction audit with zero blockers"
Solo adopter statements require a named condition, not just "doesn't need peers."

At least one persona must have a Rung 3 condition expressed as a concrete named threshold.

PER-PERSONA INERTIA SCORES

For each persona, assign an inertia score that incorporates the social proof ladder position.

  Low = workaround is weak; social proof threshold is individual or easily met (Rung 3 is
    common and observable)
  Medium = workaround has real strengths; social proof threshold is meaningful but reachable
    within a typical team context (Rung 3 is specific but plausible within 6 months)
  High = workaround is strong; social proof Rung 3 threshold is rare, role-specific, or
    requires organizational action
  Critical = workaround is entrenched; Rung 3 threshold is structurally unreachable without
    a change in team composition, organizational policy, or current solution availability

For each persona:
  [Persona name]: [Score]
  Social proof contribution: [one sentence -- how the Rung 3 threshold raises or lowers this
    persona's inertia score; if they are a solo adopter, how their internal threshold
    compares to the workaround quality]
  Primary driver: [the single dimension -- social proof or one of the four inertia dimensions
    -- most responsible for this score]

KILL-BARRIER IDENTIFICATION

Identify exactly one adoption killer: the single barrier that would block adoption even
after switching costs fall, early adopters become visible, and the feature is proven.

ADOPTION KILLER: [barrier name]
Affected persona(s): [names]
Social proof relationship: [if the kill barrier is not social proof, explain why meeting
  the Rung 3 threshold for these personas still would not produce adoption; if social proof
  IS the kill barrier, explain why the Rung 3 condition is structurally unreachable or
  why reaching it is insufficient to overcome the underlying barrier]

OVERALL ADOPTION INERTIA RISK

OVERALL RISK: [Low / Medium / High / Critical]
Social proof sequencing: [one sentence -- does the social proof ladder reveal a sequencing
  dependency across personas? For example, "Persona A's Rung 3 requires prior adoption by
  Persona B, who has a Critical inertia score -- creating a deadlock that organic adoption
  cannot break." If no dependency exists, note that personas can adopt in parallel.]
Rationale: [one sentence -- overall verdict tied to per-persona scores and the kill barrier]

AMEND

Focus on the persona with the highest inertia score.

  Persona: [name]
  Switching cost (quantified): [concrete value from the inertia dimension analysis]
  Social proof threshold (Rung 3): [the named tipping condition from the ladder]
  Kill barrier: [from KILL-BARRIER IDENTIFICATION]
  Scenario: [one sentence -- the specific moment where this persona encounters the kill
    barrier and decides not to adopt, even though the feature works and peers are beginning
    to use it]
  Mitigation: [the one intervention most likely to reduce the kill barrier; if the mitigation
    involves accelerating social proof accumulation, name the specific mechanism -- e.g.,
    "structured pilot cohort that places 2 teammates from the same workflow in the same
    trial group, creating the Rung 3 condition artificially within week 2" -- and explain
    why it produces the Rung 3 condition faster than organic adoption]

Write artifact to simulations/validate/inertia/{topic}-inertia-{date}.md.
Frontmatter: topic, date, feature, personas (list), persona_count,
social_proof_ladders_completed (true/false), kill_barrier, overall_risk,
inertia_scores (map of persona name to Low/Medium/High/Critical),
social_proof_sequencing_dependency (true/false).
```

---

## V-10: Root cause mitigation chain (combination)

**Axes:** Phrasing register (formal causal reasoning) + mitigation structure (explicit four-part causal chain) + timeline sensitivity + named social proof thresholds

**Hypothesis:** C-13 (mitigation tied to structural root cause) fails when the mitigation is generated independently of the kill-barrier root cause analysis. The most common failure mode: the kill barrier is named correctly, but the mitigation addresses a symptom rather than the structural property that makes the barrier persist. V-05's Phase 6 ("explain why this specific intervention addresses the structural reason named in Phase 4") moved toward C-13 but stops short of requiring the model to articulate the causal mechanism explicitly. This variation requires a four-part causal chain for every mitigation: (a) name the structural root cause, (b) name the persistence property that typical product improvements do not address, (c) name the lever that targets the root cause, and (d) explain why that lever neutralizes the persistence property. Combined with timeline sensitivity (C-10) and named social proof thresholds (C-12) -- three aspirational criteria that stack without structural conflict, each appearing in a different section.

```
You are running /validate:inertia for topic: {topic}.

Feature under adoption stress-test: {feature}

This skill produces an inertia analysis where the mitigation is causally connected to the
kill barrier -- not adjacent to it, not an analogy, but a direct response to the structural
property that makes the barrier persist. The analysis proceeds in seven steps, each grounding
the next. Steps may not be reordered.

=== STEP 1: PERSONA IDENTIFICATION ===

Name 2-4 user personas who are plausible adopters of this feature.

Required per persona:
  (a) Name and brief role (one sentence)
  (b) The specific outcome they currently achieve without this feature
  (c) The named current workaround -- the concrete tool, workflow, or process in use today
  (d) The single property of the current workaround that most creates adoption resistance

Every persona must have a named current workaround and a resistance property before
proceeding to Step 2.

=== STEP 2: INERTIA DIMENSION ANALYSIS ===

For each persona, assess five dimensions.

  Workaround satisfaction: H / M / L -- how well the current workaround meets the need.
    Include: why any satisfaction (at any level) creates resistance to switching.

  Switching cost: [quantified] -- the cost to migrate from the current workaround to this
    feature. Required formats:
    - Time: "~X hours migration + Y days ramp"
    - Steps: "N discrete steps, M of which require manual data verification"
    - Effort rating: "X/10 compared to [a named comparable task this persona has performed]"
    - Relative: "Nx the setup cost of [a specific recurring action this persona takes]"
    Qualitative descriptions alone ("significant effort") do not pass this field.

  Habit lock-in: the specific behavioral pattern that resists change. Name the concrete habit.
    Not "uses keyboard shortcuts" but "runs the same 3-command terminal sequence from
    muscle memory 25+ times per day."

  Social proof requirement: name the specific threshold or condition -- not binary Y/N.
    Name the count, role, use case, or organizational signal that would tip this persona.
    Examples: "needs 2 teammates in the same workflow to adopt first," "will adopt solo if
    it eliminates her highest-friction weekly task on the first trial run," "requires the
    tech lead to publicly endorse it in a sprint retrospective."

  Learning curve: Low / Medium / High + the specific knowledge or mental model gap.

=== STEP 3: PER-PERSONA INERTIA SCORES ===

Assign each persona an inertia score and a primary driver.

Scale:
  Low: minimal resistance; current workaround is weak; switching cost and lock-in are low
  Medium: meaningful resistance; at least one high-friction dimension present
  High: significant resistance; multiple high-friction dimensions OR high workaround satisfaction
  Critical: adoption-blocking; structural change required to unlock adoption

Format per persona:
  [Persona name]: [Score] -- primary driver: [dimension]
  Score basis: [one sentence -- why the primary driver dominates and how it interacts with
    the second-most-significant dimension for this persona]

Every Step 1 persona must be scored. A shared blanket score for multiple personas does not pass.

=== STEP 4: KILL-BARRIER STRUCTURAL ANALYSIS ===

Do not proceed to Step 5 until this step produces both a named adoption killer AND its
structural root cause. Both are required before the aggregate verdict.

Review Step 2 assessments and Step 3 scores.

ADOPTION KILLER: [barrier name]
Affected persona(s): [names]

Structural root cause analysis (answer all four questions):

  (a) Root cause: [the underlying structural condition that produces this barrier -- not the
    surface manifestation but the property that generates it. Example: not "high switching
    cost" but "the persona's current output format is referenced by 200+ downstream scripts,
    making migration non-atomic -- each script must be individually validated after switching."]

  (b) Persistence property: [why typical product improvements -- better UX, faster performance,
    migration tooling, onboarding guides -- do not address this root cause. The persistence
    must reference a property of the user's environment or organizational context, not the
    feature. Example: "migration tooling can automate the format conversion but cannot
    validate the 200+ downstream scripts without running them -- which requires the user
    to own a full regression cycle before committing to the switch."]

  (c) Lever type: [the category of intervention that could address the root cause directly --
    not the symptom. Examples: "a compatibility shim that makes the new output format
    indistinguishable to downstream scripts until each is individually migrated," "a
    migration audit tool that maps all downstream dependencies before the user commits,"
    "a pricing change that makes the cost of staying on the current solution exceed the
    migration cost," "an organizational trigger (team lead mandate) that socializes the
    migration cost across the team rather than placing it on one person."]

  (d) Causal mechanism: [why the lever in (c) neutralizes the persistence property in (b) --
    not what the lever does, but the causal pathway through which it addresses the specific
    structural constraint. Example: "the compatibility shim eliminates the regression cycle
    requirement because downstream scripts see no format change -- the non-atomic migration
    risk disappears, reducing switching cost from 'unknown regression surface' to 'one-time
    shim install.'"]

=== STEP 5: ADOPTION TIMELINE SENSITIVITY ===

Using the kill barrier and root cause from Step 4: how does the inertia picture evolve?

At T=0 (launch): [the current state -- which personas are at which score level; what is the
  dominant inertia driver across the persona set at the moment of launch]

At T=6 months: [how has the picture changed? Name the mechanism for any score change: improved
  tooling, social proof threshold partially met, workaround aging, organizational signals.
  For personas showing a score change, state the direction and the driver.]

At T=18 months: [the longer horizon -- if no mitigation is applied, does the kill barrier
  resolve, worsen, or remain stable? Which personas are most likely to have shifted and why?]

Kill barrier time-sensitivity: [Resolving / Stable / Worsening by T=18mo]
  Reason: [one sentence connecting the Step 4 persistence property to the trajectory --
    why does time help, hurt, or not change the structural constraint identified in Step 4(b)?]

=== STEP 6: AGGREGATE VERDICT ===

OVERALL RISK: [Low / Medium / High / Critical]
Score distribution: [count per tier, e.g., "1 Critical, 2 High, 1 Low"]
Trajectory: [Improving / Worsening / Stable -- the T=18mo direction if no mitigation applied]
Rationale: [1-2 sentences -- connects Step 3 scores, Step 4 root cause, and Step 5 trajectory
  to the overall risk verdict]

=== STEP 7: AMEND ===

Narrow to the highest-inertia persona. Produce a focused mitigation with a full causal chain.

  Persona: [name]
  Switching cost (quantified): [concrete value from Step 2]
  Social proof threshold: [the named condition from Step 2 for this persona -- the specific
    count, role, or trigger that would move them to adoption]
  Kill barrier: [must match the Step 4 adoption killer exactly]
  Scenario: [one sentence -- the specific moment where this persona encounters the kill
    barrier and decides not to adopt, even though the feature works correctly]

  Mitigation (complete all four parts):

    Intervention: [the concrete action -- feature change, migration tool, pricing lever,
      onboarding redesign, or social proof mechanism; name it specifically]

    Root cause addressed: [reference the Step 4(a) root cause by name -- which structural
      property does this intervention modify? Use the same language as Step 4(a).]

    Causal mechanism: [why this specific intervention neutralizes the persistence property
      from Step 4(b) -- not what the intervention does, but why it works on the specific
      structural constraint; follow the logic established in Step 4(d)]

    Expected signal at T=6mo: [the observable change in this persona's behavior or inertia
      score that would confirm the mitigation is working -- name the metric or behavior,
      not just "inertia decreases"]

Write artifact to simulations/validate/inertia/{topic}-inertia-{date}.md.
Frontmatter: topic, date, feature, personas (list), persona_count,
kill_barrier, kill_barrier_root_cause_documented (true/false),
kill_barrier_time_sensitivity, overall_risk, overall_trajectory,
inertia_scores (map of persona name to Low/Medium/High/Critical),
mitigation_causal_chain (true/false), social_proof_thresholds_named (true/false).
```
