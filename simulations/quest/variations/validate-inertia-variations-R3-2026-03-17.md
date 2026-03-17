Written to `simulations/quest/variations/validate-inertia-variations-R3-2026-03-17.md`.

---

## Round 3 Variations — validate-inertia

5 variations across 4 axes targeting the three new R3 criteria (C-13/C-14/C-15):

| # | Label | Axis | Key hypothesis |
|---|-------|------|----------------|
| V-01 | R3 upgraded baseline | R2 V-02 + explicit labels | Add "Lost TAM implication:" label, "Implication:" line in Phase 2, unconditional framing -- becomes the R3 floor |
| V-02 | Type-resolution contract | C-13/C-14 integration | Phase 2 writes "Required mitigation form:"; Phase 4 fulfills it -- C-14 becomes contract fulfillment, not fresh derivation |
| V-03 | Lost TAM standalone section | C-15 isolation | Phase 5 owns the Lost TAM line exclusively -- section heading makes it mandatory by isolation |
| V-04 | Inertia type gate | C-13 procedural gate | "Do not proceed until..." + "Gate passed. Proceeding." -- procedural enforcement vs. phase-header framing |
| V-05 | Compressed R3 complete | Output format | All 15 criteria as required output fields in numbered scaffold -- tests whether compressed format can carry C-13's "dedicated phase" requirement |

**Design logic for R3:** R2 V-02 scored 100 and *generated* C-13/C-14/C-15. R3 takes that structure as the source model and asks: how do we make each of the three new criteria structurally reliable rather than incidental? V-02 answers this for C-14 (moves the branch contract to Phase 2). V-03 answers for C-15 (isolation into Phase 5). V-04 answers for C-13 (gate language). V-01 is the stable baseline. V-05 tests whether format can carry the full set.

**The live design tension:** V-02's "Required mitigation form:" contract may be the most interesting structural innovation -- if the kill barrier is revised in Phase 3, the contract and revision must reconcile. That edge case is worth watching in scoring.
iable, not how to replace it.

**Main new axes:**
- **V-02**: Moves C-14 contract-writing to classification phase -- tests whether deriving mitigation form early produces more specific synthesis than writing the constraint at synthesis time.
- **V-03**: Isolates C-15 into its own required section -- tests whether label isolation prevents conditional drift vs. embedding in synthesis.
- **V-04**: Gate language for C-13 -- tests whether "do not proceed" procedural framing outperforms phase-header framing for classification reliability.

**Design tensions:**
- V-02 vs V-01: Does "Required mitigation form:" in Phase 2 improve C-14, or does it over-constrain synthesis when the kill barrier is revised in Phase 3?
- V-03 vs V-01: Does a standalone Phase 5 improve C-15, or does the added phase create output length pressure that degrades earlier sections?
- V-04 vs V-01: Does "Gate passed. Proceeding." improve C-13 reliability, or is the marker skipped?
- V-05: Can compressed format satisfy C-13's "dedicated pre-persona phase" requirement? A numbered section may read as a section, not a phase.

**Structural choices driving the key rubric risks:**
- C-13 (dedicated pre-persona classification): All 5 variants enforce a pre-persona phase. V-04 uses procedural gate language. V-05 uses numbered section ordering with parenthetical enforcement.
- C-14 (type-conditioned mitigation): All 5 variants include explicit if-structural/if-behavioral branching. V-02 writes the branch contract in Phase 2. V-05 formats it as a conditional required field.
- C-15 (Lost TAM unconditional): All 5 variants include "Lost TAM implication:" as a required output line. V-03 isolates it into Phase 5 with its own header.

---

## V-01: R3 Upgraded Baseline

Axis: R2 V-02 promoted to R3 floor -- explicit C-13/C-14/C-15 labels added while
preserving V-02's winning four-phase structure verbatim

Hypothesis: V-02 already embeds the patterns behind C-13/C-14/C-15 but without the
explicit "Lost TAM implication:" label for C-15 and without a distinct "Implication:"
line in Phase 2. Adding these labels while keeping V-02's type-conditioned branching
and unconditional phase structure produces the reliable R3 floor. Every other R3
variant should exceed this score or fail productively.

```
You are running /validate-inertia for topic: {topic}.

PURPOSE: Map adoption inertia, classify its type, and produce a type-conditioned
mitigation plan. Four phases -- each output gates the next.

--- PHASE 1: KILL BARRIER HYPOTHESIS ---

Read: simulations/scout/**/{topic}-*.md and simulations/discover/**/{topic}-*.md.

Before any analysis, state your kill barrier hypothesis:
  Kill Barrier Hypothesis: {specific mechanism, role, or structural constraint that would
  prevent adoption entirely. Not generic. Not derived from personas -- this is your
  prediction before looking at the data.}

--- PHASE 2: INERTIA LANDSCAPE CLASSIFICATION ---

Before analyzing individual personas, classify the resistance this feature faces.
This classification determines the type of solution required -- complete it before
proceeding to personas.

  Primary inertia type: Structural | Behavioral | Mixed

  Structural = the feature does not yet satisfy a requirement users consider
  non-negotiable. No amount of onboarding or framing overcomes this -- the product
  must change.

  Behavioral = the feature is capable enough, but habits, workflows, and social dynamics
  prevent adoption. The right launch strategy can reach these users.

  Classification: {Structural | Behavioral | Mixed}
  Rationale: {one sentence explaining which type dominates and why}
  Implication: {one sentence -- if Structural: name the product change required before
  any adoption is possible; if Behavioral: name the launch approach that can reach users;
  if Mixed: name the structural blocker and estimate the split (e.g., "60% behavioral,
  40% structural")}

Name the incumbent -- the tool, script, convention, or process users rely on today.
In one sentence: why did users choose it? What job does it do well for them?

--- PHASE 3: PERSONA DISPLACEMENT SCORECARD ---

Identify 3-5 personas from the signals (or construct from first principles). For each
persona, state why they chose the incumbent -- role-grounded, not generic.

Build this table:

| Persona | Why They Use the Incumbent | Workaround Satisfaction (1-5) | Switching Cost (concrete) | Habit at Risk | Social Proof Needed | Learning Curve | Inertia Score | Inertia Type |
|---------|---------------------------|-------------------------------|--------------------------|---------------|---------------------|----------------|---------------|--------------|

Column rules:
- Why They Use the Incumbent: the adoption decision -- "X won this persona because..."
  Not "it works" but WHY it works for this specific person in this role.
- Workaround Satisfaction: 1-5. Flag 4+ as "good enough" -- state the specific reason
  why that score means the workaround feels sufficient for this persona.
- Switching Cost: concrete units only (hours, steps, files, dollars, rollback risk).
  "High" or "significant effort" fails this column.
- Habit at Risk: specific behavioral pattern, not a category. "Runs make check before
  every commit" not "relies on existing tooling."
- Social Proof Needed: specific threshold -- names, numbers, evidence type.
  "Peer validation" fails.
- Learning Curve: time or concept count; comparison anchor if possible ("similar to
  learning X, which took Y days").
- Inertia Score: Low / Medium / High / Critical. Same scale. Required every row.
- Inertia Type: Structural | Behavioral -- classify each persona individually.

After the table: confirm or revise your Phase 1 hypothesis.
  "Kill Barrier (confirmed):" or "Kill Barrier (revised):" -- one sentence.

--- PHASE 4: SYNTHESIS ---

Overall adoption inertia risk: Low / Medium / High / Critical

Inertia asymmetry:
  Structural (will not adopt without product changes): {personas}
  Behavioral (can be overcome with onboarding/framing): {personas}

Lost TAM implication: {one sentence -- name which personas or persona type represent
permanent lost TAM until product changes, vs. which represent delayed adoption reachable
with launch strategy. Write this regardless of evidence confidence.}

Mitigation: one specific action targeting the kill barrier.
  If the kill barrier is structural: name the product change required.
  If the kill barrier is behavioral: name the launch sequence or social proof intervention.
  Do not restate the barrier. Do not propose generic onboarding.

Write artifact to simulations/validate/inertia/{topic}-validate-inertia-{date}.md
with frontmatter: topic, date, persona_count, kill_barrier (one line), overall_risk.
```

---

## V-02: Type-Resolution Contract

Axis: C-13/C-14 integration -- Phase 2 outputs an explicit "Required mitigation form:"
contract; C-14 in Phase 4 becomes fulfillment of that contract, not fresh derivation

Hypothesis: When Phase 2 writes a "Required mitigation form:" field that names what
category of mitigation is valid given the classification, C-14 in synthesis is constrained
by the model's own prior output. The model reads the contract it wrote and fills it in.
This is structurally narrower than "if structural / if behavioral" branching at synthesis
time because the valid answer space is defined before persona analysis begins. Risk: if
the kill barrier is revised in Phase 3, the Phase 2 contract may be misaligned; the
prompt must handle graceful revision.

```
You are running /validate-inertia for topic: {topic}.

PURPOSE: Map adoption inertia, classify its type, and produce a mitigation logically
derived from that classification. The type determines the solution category. Four phases.
Phase 2 writes a contract; Phase 4 fulfills it.

--- PHASE 1: KILL BARRIER HYPOTHESIS ---

Read: simulations/scout/**/{topic}-*.md and simulations/discover/**/{topic}-*.md.

Kill Barrier Hypothesis: {specific mechanism -- not generic, not derived from personas.
Your prediction before the analysis. You will confirm or revise it in Phase 3.}

--- PHASE 2: INERTIA LANDSCAPE CLASSIFICATION ---

Answer this question before any persona analysis. Your answer determines what form
your Phase 4 mitigation must take.

  Primary inertia type: Structural | Behavioral | Mixed

  Structural = the feature has a product gap users consider non-negotiable. No launch
  strategy overcomes this -- the product must change first.

  Behavioral = the feature is capable; habits, social dynamics, and workflow rituals
  prevent adoption. A targeted launch strategy can reach these users.

  Mixed = both types present. Name the structural blocker. Estimate the split.

  Classification: {Structural | Behavioral | Mixed}
  Rationale: {one sentence}
  Implication: {one sentence -- what this type means for adoption before any persona
  has been analyzed}

  Required mitigation form (write this now; Phase 4 must fulfill it):
    Structural: "Phase 4 mitigation must name a specific product change that removes
      the non-negotiable gap. Generic onboarding, tutorials, and framing do not qualify."
    Behavioral: "Phase 4 mitigation must name a specific launch sequence, social proof
      seeding strategy, or framing intervention. Generic onboarding does not qualify."
    Mixed: "Phase 4 mitigation must name a structural product change AND a behavioral
      launch sequence. Both are required."

Name the incumbent: {tool, script, convention, or process users rely on today}
Why users chose it: {one sentence -- the adoption story, the job it does well}

--- PHASE 3: PERSONA DISPLACEMENT SCORECARD ---

Identify 3-5 personas. For each, state why they chose the incumbent -- role-grounded.

| Persona | Why They Use the Incumbent | Workaround Satisfaction (1-5) | Switching Cost (concrete) | Habit at Risk | Social Proof Needed | Learning Curve | Inertia Score | Inertia Type |
|---------|---------------------------|-------------------------------|--------------------------|---------------|---------------------|----------------|---------------|--------------|

Column rules:
- Why They Use the Incumbent: "X won this persona because their role requires..."
- Workaround Satisfaction: 1-5. Flag 4+ as "good enough" -- state the specific reason.
- Switching Cost: concrete units (hours, steps, files, dollars, rollback risk). Vague fails.
- Habit at Risk: specific behavior that fires automatically. Not a category.
- Social Proof Needed: specific threshold -- number, name, or evidence type.
- Learning Curve: time or concept count; comparison anchor preferred.
- Inertia Score: Low / Medium / High / Critical. Same scale. Required every row.
- Inertia Type: Structural | Behavioral per persona.

Kill Barrier (confirmed or revised): {one sentence}
Note: if revised, state whether the Phase 2 classification still holds or also requires
update. If updated, revise the Required mitigation form accordingly.

--- PHASE 4: SYNTHESIS ---

Overall adoption inertia risk: Low / Medium / High / Critical

Mitigation: fulfill the contract you wrote in Phase 2. Use the "Required mitigation form"
you specified. Name the specific product change, launch sequence, or social proof strategy
that directly removes the kill barrier. Name the owner.
Do not restate the barrier. Do not propose generic onboarding.

Inertia asymmetry:
  Structural personas (product must change before they can adopt): {list}
  Behavioral personas (launch strategy can reach them): {list}

Lost TAM implication: {one sentence -- name which personas represent permanent lost TAM
until product changes, vs. which represent delayed adoption reachable with launch strategy.
Required. Write this regardless of evidence confidence.}

Write artifact to simulations/validate/inertia/{topic}-validate-inertia-{date}.md
with frontmatter: topic, date, persona_count, kill_barrier (one line), overall_risk.
```

---

## V-03: Lost TAM Standalone Section

Axis: C-15 isolation -- "Lost TAM implication" extracted into its own required Phase 5,
physically separate from inertia asymmetry and synthesis

Hypothesis: In V-01 and most R2 variants, C-15 is embedded within the synthesis section.
When the model writes a busy synthesis block, the Lost TAM line can collapse into
asymmetry bullets or become conditional by proximity to surrounding "if" language. A
standalone Phase 5 with its own header, its own required template, and explicit "Write
this regardless of evidence confidence." instruction isolates the output slot -- the model
cannot write the artifact line without completing Phase 5. Risk: the added phase creates
output length pressure that degrades earlier sections.

```
You are running /validate-inertia for topic: {topic}.

PURPOSE: Map why users will not adopt this feature even when it works. Produce per-persona
inertia scores, a type-conditioned mitigation, and a Lost TAM estimate. Five phases.

--- PHASE 1: KILL BARRIER HYPOTHESIS ---

Read: simulations/scout/**/{topic}-*.md and simulations/discover/**/{topic}-*.md.

Kill Barrier Hypothesis: {the single mechanism most likely to block adoption entirely.
Feature-specific. Not derived from personas -- your prediction before the evidence.}

--- PHASE 2: INERTIA LANDSCAPE ---

Classify the inertia this feature faces before analyzing any persona. This classification
determines what category of mitigation is valid.

  Type: Structural | Behavioral | Mixed

  Structural = users will not adopt without a product change. Onboarding and framing
  cannot close this gap.

  Behavioral = the feature is capable; habits, workflow rituals, and social dynamics
  prevent adoption. The right launch strategy can reach these users.

  Mixed = both types present. Name the structural blocker. Estimate the split.

  Classification: {Structural | Behavioral | Mixed}
  Rationale: {one sentence}
  Implication: {one sentence -- what this type means for adoption strategy; if Structural,
  name the change that unlocks adoption; if Behavioral, name the launch approach;
  if Mixed, name the structural blocker}

Name the incumbent: {tool, script, convention, or process users rely on today}
Adoption story: "Users adopted {incumbent} because ___." (role-grounded, at least one
persona -- why they chose it, not just what it is)

--- PHASE 3: PERSONA SCORECARD ---

3-5 personas. For each, analyze the displacement challenge.

| Persona | Why They Chose the Incumbent | Workaround Satisfaction (1-5) | Switching Cost (concrete) | Habit at Risk | Social Proof Needed | Learning Curve | Inertia Score | Inertia Type |
|---------|------------------------------|-------------------------------|--------------------------|---------------|---------------------|----------------|---------------|--------------|

Column rules:
- Why They Chose the Incumbent: adoption decision -- "X won this persona because..."
- Workaround Satisfaction: 1-5. Flag 4+ as "good enough" and state the specific reason.
- Switching Cost: concrete units (hours, steps, files, dollars, rollback risk). Vague fails.
- Habit at Risk: specific behavior that fires before they think about it. Not a category.
- Social Proof Needed: specific threshold -- number, name type, evidence form.
- Learning Curve: time estimate or concept count; comparison anchor if possible.
- Inertia Score: Low / Medium / High / Critical. Same scale. Required every row.
- Inertia Type: Structural | Behavioral per persona.

Kill Barrier (confirmed or revised): {one sentence}

--- PHASE 4: ADOPTION RISK + MITIGATION ---

Overall adoption inertia risk: Low / Medium / High / Critical

Inertia asymmetry:
  Structural personas (will not adopt without product changes): {list or "none"}
  Behavioral personas (can be reached with launch strategy): {list}

Mitigation targeting the kill barrier:
  If the kill barrier is structural: name the specific product change required. Not
    "improve the feature" -- name the gap and the fix, specific enough to assign to
    an owner.
  If the kill barrier is behavioral: name the specific launch sequence or social proof
    seeding strategy. Not "improve onboarding" -- name the sequence and the owner.

--- PHASE 5: LOST TAM IMPLICATION ---

This section is required. Write it regardless of evidence confidence.

Lost TAM implication: {one sentence -- name which personas (or persona type) represent
permanent lost TAM until product changes, and which represent delayed adoption reachable
with launch strategy. Both sides of the statement are required. Use "permanent lost TAM"
and "delayed adoption" as anchoring terms.}

Write artifact to simulations/validate/inertia/{topic}-validate-inertia-{date}.md
with frontmatter: topic, date, persona_count, kill_barrier (one line), overall_risk.
```

---

## V-04: Inertia Type Gate

Axis: C-13 procedural gate -- Phase 2 uses "do not proceed" language and a "Gate passed.
Proceeding." marker; classification is a blocking prerequisite, not a phase header

Hypothesis: V-01 frames Phase 2 as a section header ("INERTIA LANDSCAPE CLASSIFICATION").
V-04 frames it as a gate: "Do not proceed to persona analysis until you have answered this
question." The gate language plus an explicit "Gate passed." self-affirmation makes the
classification a procedural prerequisite the model tracks. This should produce the
strongest C-13 guarantee because the constraint is procedural rather than structural.
Risk: the "Gate passed. Proceeding." marker may be skipped or treated as prose.

```
You are running /validate-inertia for topic: {topic}.

FRAME: Before users can adopt this feature, it must displace something they already
trust. Your job is to understand why they will not switch -- even when the feature works
correctly. Run in four phases. Do not start a phase until the previous one is complete.

--- PHASE 1: KILL BARRIER HYPOTHESIS ---

Read: simulations/scout/**/{topic}-*.md and simulations/discover/**/{topic}-*.md.

Before any persona analysis, state your hypothesis:
  Kill Barrier Hypothesis: {the single mechanism most likely to prevent adoption entirely.
  Specific to this feature. Not derived from personas -- this is your prediction.}

--- PHASE 2: INERTIA TYPE GATE ---

Do not proceed to persona analysis until you have classified inertia type.

This classification determines what category of solution can work. Structural inertia
cannot be addressed by launch strategy alone. Behavioral inertia cannot be fixed by
product changes alone. Getting the type wrong produces a useless mitigation.

Answer this question now:

  Inertia type: Structural | Behavioral | Mixed

  Structural inertia: the feature has a product gap users consider non-negotiable. They
  will not adopt until the product changes -- not because of habits or onboarding friction,
  but because the feature does not yet do what they require.

  Behavioral inertia: the feature is capable. Habits, social dynamics, and workflow
  rituals prevent adoption. A targeted launch strategy can reach these users.

  Mixed: both types present. Name the structural blocker explicitly. Estimate the split
  (e.g., "60% behavioral, 40% structural").

  Your classification: {Structural | Behavioral | Mixed}
  Rationale: {one sentence}
  Implication: {one sentence -- if Structural: name the product change that would unlock
  adoption; if Behavioral: name the launch approach that can reach users; if Mixed: name
  the structural blocker}

Name the incumbent: {tool, script, convention, or process users rely on today}
Why users chose it: {one sentence -- the adoption story, not current state}

Gate passed. Proceeding to persona analysis.

--- PHASE 3: PERSONA DISPLACEMENT SCORECARD ---

3-5 personas. For each: why did they choose the incumbent? (Role-grounded.)

| Persona | Why They Use the Incumbent | Workaround Satisfaction (1-5) | Switching Cost (concrete) | Habit at Risk | Social Proof Needed | Learning Curve | Inertia Score | Inertia Type |
|---------|---------------------------|-------------------------------|--------------------------|---------------|---------------------|----------------|---------------|--------------|

Column rules:
- Why They Use the Incumbent: the adoption decision -- "X won this persona because..."
  Not "it works" -- why it works for this specific person in this role.
- Workaround Satisfaction: 1-5. Flag 4+ as "good enough" -- state the specific reason.
- Switching Cost: concrete units (hours, steps, files, dollars, rollback risk). "High" fails.
- Habit at Risk: specific behavioral pattern. Not a category label.
- Social Proof Needed: specific threshold -- numbers, names, evidence type.
- Learning Curve: time or concept count; comparison anchor if possible.
- Inertia Score: Low / Medium / High / Critical. Same scale. Required every row.
- Inertia Type: Structural | Behavioral -- classify each persona individually.

Kill Barrier (confirmed or revised): {one sentence}

--- PHASE 4: SYNTHESIS ---

Overall adoption inertia risk: Low / Medium / High / Critical

Inertia asymmetry:
  Structural (will not adopt without product changes): {personas}
  Behavioral (can be reached with launch strategy): {personas}

Lost TAM implication: {one sentence -- which personas represent permanent lost TAM until
product changes, vs. delayed adoption reachable with launch strategy. Required. Unconditional.}

Mitigation targeting the kill barrier:
  If the kill barrier is structural: name the specific product change required --
    specific enough to assign to an owner and schedule.
  If the kill barrier is behavioral: name the specific launch sequence or social proof
    seeding intervention -- name the sequence and the owner.
  Do not restate the barrier. Do not propose generic onboarding.

Write artifact to simulations/validate/inertia/{topic}-validate-inertia-{date}.md
with frontmatter: topic, date, persona_count, kill_barrier (one line), overall_risk.
```

---

## V-05: Compressed R3 Complete

Axes: Output format (minimal numbered scaffold) + lifecycle emphasis (every line is a
required output specification, no explanatory prose) with R3 additions as required fields

Hypothesis: C-13, C-14, and C-15 can be expressed as required output fields in the
compressed numbered format without explanatory prose. Section 2 carries C-13 via its
"(complete before any persona analysis)" parenthetical and structural position before
Section 3. Section 6's explicit if-Structural/if-Behavioral fields carry C-14 by format.
Section 5's standalone "Lost TAM implication:" required line carries C-15 by isolation.
Risk: Section 2 as a numbered section may not satisfy the rubric's "dedicated pre-persona
phase" requirement -- a numbered section may read as an inline classification.

```
You are running /validate-inertia for topic: {topic}.

Read: simulations/scout/**/{topic}-*.md and simulations/discover/**/{topic}-*.md.

Produce these sections in order. Do not reorder. Every labeled line is a required output.

---

1. KILL BARRIER HYPOTHESIS

Kill Barrier Hypothesis: {specific mechanism -- feature-specific, not generic, stated
before any persona work. Not derived from aggregating personas.}

---

2. INERTIA LANDSCAPE (complete before any persona analysis)

Inertia type: Structural | Behavioral | Mixed
Rationale: {one sentence}
Implication: {Structural: name the product change that unlocks adoption |
  Behavioral: name the launch approach that reaches users |
  Mixed: name the structural blocker and split estimate (e.g., "60% behavioral, 40% structural")}

Incumbent: {tool, script, convention, or process users rely on today}
Why users chose it: "They adopted {incumbent} because ___." (adoption decision, not
current state -- at least one persona; role-grounded)

---

3. PERSONA TABLE (3-5 personas)

| Persona | Why Incumbent Won | Workaround Satisfaction (1-5) | Switching Cost | Habit at Risk | Social Proof Needed | Learning Curve | Inertia Score | Inertia Type |
|---------|-------------------|-------------------------------|----------------|---------------|---------------------|----------------|---------------|--------------|

Column rules:
- Why Incumbent Won: role-grounded. Not "it works."
- Workaround Satisfaction: 1-5. Flag 4+ as "good enough" -- state the specific reason.
- Switching Cost: concrete units (hours, steps, files, dollars, rollback risk). "High" fails.
- Habit at Risk: specific behavior. Not a category.
- Social Proof Needed: specific threshold -- number, name, or evidence type.
- Learning Curve: time or concept count; comparison anchor preferred.
- Inertia Score: Low / Medium / High / Critical. Same scale. Required every row.
- Inertia Type: Structural | Behavioral per persona.

---

4. KILL BARRIER (confirmed or revised)

Kill Barrier (confirmed): {one sentence}  --OR--  Kill Barrier (revised): {one sentence}

---

5. INERTIA ASYMMETRY

Structural personas (product must change before they can adopt): {list or "none"}
Behavioral personas (launch strategy can reach them): {list}
Lost TAM implication: {one sentence -- required, unconditional. Name which personas or
persona type represent permanent lost TAM until product changes vs. delayed adoption
reachable with launch strategy.}

---

6. OVERALL RISK + MITIGATION

Overall risk: Low / Medium / High / Critical

Mitigation (type-conditioned -- derived from Section 2 inertia type):
  If Structural: {name the specific product change required -- the gap and the fix,
    assignable to an owner}
  If Behavioral: {name the specific launch sequence or social proof intervention --
    the sequence and the owner}
  If Mixed: {structural change: [name it] | behavioral sequence: [name it]}

Do not restate the barrier. Do not write "improve onboarding."

---

Write artifact to simulations/validate/inertia/{topic}-validate-inertia-{date}.md
with frontmatter: topic, date, persona_count, kill_barrier (one line), overall_risk.
```
