---
skill: quest-variate
skill_target: scout-inertia
date: 2026-03-17
round: 6
rubric: v6
variations: 5
---

# scout-inertia -- Prompt Variations R6

## Context

R5 results: all 5 variations predicted 100/100 on rubric v5. R5 scaffold introduced
C-18 (per-table column manifest -- "Required columns for this table:" before each
table). The new rubric v6 adds two criteria:

- **C-19**: Multi-component requirements use a Named Sub-Protocol (e.g., "Replication
  Fidelity Standard:" before 3 numbered sub-requirements). R5 V-05 demonstrates this;
  V-01--V-04 use the same requirements in unnamed prose and produce PARTIAL C-13.
- **C-20**: Requirement statements include inline acceptable/unacceptable counter-example
  pairs (e.g., "'GitHub Actions' not 'CI system'"). R5 V-05 demonstrates this; V-01--V-04
  have fail conditions only (unacceptable example without the paired acceptable form).

**Design goal for R6**: All 5 variations pass C-19 and C-20, plus carry all C-01--C-18
from R5. Single-axis variations explore different mechanisms for C-19 and C-20 compliance.

**Axes available**:
- C-19 scope: minimum (one named sub-protocol) vs. comprehensive (all multi-component
  requirements named)
- C-20 density: minimum (2 pairs at critical requirements) vs. maximum (every
  requirement statement with a fail condition gets a full pair)
- Placement: template position vs. role instruction vs. phase header
- Register: formal/technical vs. imperative

Single-axis choices: C-19 minimum viable (V-01), C-20 maximum density (V-02), C-19
comprehensive via role instructions (V-03). Combined: C-19+C-20 as phase-protocol
headers (V-04), full scaffold with all 5 sub-protocols + saturated C-20 (V-05).

## Variation Map

| ID | Axis | Hypothesis |
|----|------|------------|
| V-01 | Single-axis C-19: minimum viable named sub-protocol on inertia-framing base | Adding "Replication Fidelity Standard" as the one named sub-protocol + 2 inline pairs satisfies C-19 and C-20 with minimum scaffold change. Tests whether the properties hold at low insertion cost. |
| V-02 | Single-axis C-20: maximum counter-example density on schema-block base | Converting every fail condition to a full pass/fail pair (adding the acceptable form to each) saturates C-20 enforcement. Tests whether C-20 density produces more reliable C-13 compliance than the named-protocol label alone. |
| V-03 | Single-axis C-19: comprehensive named sub-protocols for all 5 multi-component requirements, via role instructions | Adding named sub-protocol labels to all five structural requirements (Replication Fidelity Standard, Switching Cost Protocol, Failure Mode Standard, Loss Condition Standard, Anchored Rebuttal Protocol) via role steps makes every multi-component requirement independently addressable by name. |
| V-04 | Combined C-19+C-20: phase headers as named protocols, counter-example pairs per phase | Using phase headers to declare sub-protocol names (C-19) and opening each phase with inline pass/fail pairs (C-20) creates two-level structural enforcement: phases declare the protocol, pairs enforce within the phase. |
| V-05 | Combined all axes: complete named sub-protocols + maximum C-20 density + full C-16/C-17/C-18 stack | R5 V-05 base extended: all 5 multi-component requirements named as sub-protocols (C-19 comprehensive), counter-example pairs at every requirement (C-20 saturated). Eliminates all remaining judgment-dependent requirements. |

---

## V-01 -- Axis: C-19 Minimum Viable (Single Named Sub-Protocol on Inertia-Framing Base)

**Hypothesis**: Adding "Replication Fidelity Standard" as the one named sub-protocol
to the workaround description, plus 2 inline acceptable/unacceptable pairs at the
most critical requirement sites (tool naming and verification commands), satisfies
C-19 and C-20 with the minimum change to the R5 V-01 scaffold. Tests whether the
named-protocol and counter-example properties hold without restructuring the prompt.

This is R5 V-01 (Competitor Zero framing, inline "Required columns" manifests) with
two additions: (1) workaround section becomes a named sub-protocol with numbered
sub-requirements, (2) inline pass/fail pairs at tool naming and verification command
positions.

```
Auto-detect the feature from repo context. Do not prompt unless context is absent.

## Competitor Zero: Status Quo / Do Nothing

Before any named competitor, analyze the primary competitor: the option to do
nothing and keep the current workaround. Treat inertia as a named competitor.
Profile it fully.

This output must contain the following sections: Workaround Description,
Switching Cost Profile, Inertia Threat Score, Why Inertia Loses, Workaround
Failure Modes, Forward-Looking Risk, Steelman and Rebuttal.

**1. Workaround Description -- Replication Fidelity Standard**

Describe the workaround so that another team with no prior context could reproduce
it independently. Apply the Replication Fidelity Standard:

1. Name each tool by product, not by category.
   Pass: "GitHub Actions" / Fail: "CI system"
   Pass: "custom Python script invoked by a Makefile target" / Fail: "automation script"
2. Enumerate the major steps in numbered sequence.
3. Flag institutional knowledge: any step requiring tribal context, undocumented
   conventions, or shared credentials a new team member would not have.

All three sub-requirements of the Replication Fidelity Standard must be satisfied
independently. Name the workaround (e.g., "manual YAML patching", "Slack-based
approval chain"). One paragraph minimum.

**2. Switching Cost Profile**

Three line items, each with a numeric estimate or explicit N/A with justification:
- Time: hours or days to migrate existing setups, per project or per team
- Training: days of onboarding, number of people affected, ramp-up friction
- Disruption: coordination overhead, workflow interruption, dependencies that
  must change

Numeric or range-based estimates required. "Significant" is not an estimate.

**3. Inertia Threat Score**

Assign: HIGH (default and required). Downgrading below HIGH requires a written
justification with evidence. Absence of a score is an automatic analysis failure.

**4. Why Inertia Loses**

Required columns for this table: # | Condition | Observable Threshold | Verification Command

| # | Condition | Observable Threshold | Verification Command |
|---|-----------|---------------------|---------------------|
| 1 | [condition] | [measurable trigger] | [Tool: Action -> Result when threshold applies] |
| 2 | [condition] | [measurable trigger] | [Tool: Action -> Result when threshold applies] |

Verification Command format: `[Tool or artifact]: [what to open or run] ->
[what the result looks like when threshold applies]`

Pass: "Jira: open the active sprint board -> count rows where Status = Active.
If >= 4, condition applies."
Fail: "you can check project count" or "review your sprint board"

**5. Workaround Failure Modes**

Distinct from switching costs. Failure modes = what goes wrong if you stay.
Two or more required.

Required columns for this table: # | Failure Mode | Trigger | Impact | Severity

| # | Failure Mode | Trigger | Impact | Severity |
|---|-------------|---------|--------|---------|
| 1 | [specific failure] | [what causes it] | [consequence to team] | HIGH |
| 2 | [specific failure] | [what causes it] | [consequence to team] | MED |

Trigger and Impact are separate columns -- do not merge.
Severity: HIGH = data loss or compliance risk; MED = incorrect results; LOW = inefficiency.
"Does not scale" without a named scale limit does not pass.

**6. Forward-Looking Risk**

What happens to teams that stay on the workaround for the next 6-12 months? Name a
specific compounding cost, accumulating debt, or divergence risk with a time horizon.

**7. Steelman and Rebuttal**

Write the strongest possible argument a skeptical senior engineer would make for
staying on the workaround. Label it explicitly. Then rebut it specifically. A weak
steelman is worse than none -- if you cannot write a strong one, flag it.

---

After profiling Competitor Zero, add:
- Named competitors (3-5): feature overlap, threat level (HIGH/MEDIUM/LOW),
  one-line differentiation
- The whitespace: what no competitor owns
- Table stakes: what any entrant must match

Write artifact to: simulations/scout/inertia/{topic}-inertia-{date}.md
```

---

## V-02 -- Axis: C-20 Maximum Density (Counter-Example Pairs at Every Requirement)

**Hypothesis**: Converting every fail condition to a full pass/fail pair -- adding
the acceptable form alongside the unacceptable -- saturates C-20 enforcement
throughout the scaffold. Every requirement statement becomes directly testable by
substitution: a reader applies the contrast directly without subjective judgment.
This tests whether C-20 density produces more reliable C-13 compliance than the
Replication Fidelity Standard name alone.

This is R5 V-02 (Schema block format, table-first structure) with three additions:
(1) Replication Fidelity Standard named sub-protocol in Section 1, (2) Pass/Fail
examples added to every requirement statement that previously had fail conditions
only, (3) explicit section heading manifest added at the top.

```
Auto-detect the feature from repo context. Do not prompt unless context is absent.

Analyze the inertia competitor -- the option to keep the current workaround instead
of adopting this feature. Answer the central question: **why does inertia lose?**
If you cannot answer it, stop and flag.

This output must contain the following sections: Workaround Description, Switching
Cost Table, Inertia Threat Score, Why Inertia Loses, Workaround Failure Modes,
Long-Term Risk of Staying, Steelman and Rebuttal.

### Required Output Structure

**Section 1 -- Workaround Description**

**Replication Fidelity Standard:**
1. Tool names: product-level, not category-level.
   Pass: "GitHub Actions" / Fail: "CI system"
   Pass: "Confluence page" / Fail: "doc"
   Pass: "custom Python script invoked by a Makefile target" / Fail: "automation script"
2. Steps: enumerated in numbered sequence, not summarized prose.
   Pass: "1. Engineer opens Confluence template, 2. copies to project page, 3. edits
   four required fields, 4. pings #approvals"
   Fail: "team follows the standard documentation process"
3. Institutional knowledge: any step requiring tribal context flagged explicitly.
   Pass: "requires access to #approvals Slack channel -- not in onboarding docs"
   Fail: [omitting a step that depends on undocumented knowledge]

Name the workaround. Write one paragraph minimum.

**Section 2 -- Switching Cost Table**

| Dimension | Estimate | Basis |
|-----------|----------|-------|
| Time | [X hours/days per project] | [what drives this] |
| Training | [X days, Y people] | [what must be learned] |
| Disruption | [what changes, who is affected] | [coordination cost] |

All three rows required.
Pass: "2-4 hours per project for YAML migration"
Fail: "moderate effort" or "significant time"

**Section 3 -- Inertia Threat Score**

```
Threat: HIGH
```

Downgrade below HIGH only with written justification and evidence.
Pass: explicit "HIGH" label with any qualifier.
Fail: omitting the score or substituting narrative language ("elevated concern",
"real risk") without the explicit severity token.

**Section 4 -- Why Inertia Loses**

Two or more conditions. Each must be falsifiable.

> Schema: # | Condition | Observable Threshold | Verification Command

| # | Condition | Observable Threshold | Verification Command |
|---|-----------|---------------------|---------------------|
| 1 | [condition] | [measurable trigger] | [see format below] |
| 2 | [condition] | [measurable trigger] | [see format below] |

**Verification Command format**: `[Tool or artifact]: [what you open or run] ->
[what the result looks like when the threshold applies]`

Pass: "Jira: open the active sprint board -> count rows where Status = Active.
If >= 4, condition applies."
Pass: "GitHub: run `gh pr list --state open | wc -l` -> if output >= 10, threshold met."
Fail: "You can check project count"
Fail: "Review your sprint board"

The command must name a specific tool and a concrete action without requiring a
follow-up question.

**Section 5 -- Workaround Failure Modes**

Distinct from switching costs. Failure modes = what goes wrong if you stay.
Two or more required.

> Schema: # | Failure Mode | Trigger | Impact | Severity

| # | Failure Mode | Trigger | Impact | Severity |
|---|-------------|---------|--------|---------|
| 1 | [specific failure] | [what triggers it] | [consequence to team] | HIGH / MED / LOW |
| 2 | [specific failure] | [what triggers it] | [consequence to team] | HIGH / MED / LOW |

Trigger and Impact are separate columns -- do not merge into a single cell.
Pass: Trigger = "when queue depth exceeds 500 messages"; Impact = "events silently
dropped with no error surfaced to the caller"
Fail: Trigger+Impact merged = "the workaround fails under load" or "doesn't scale
without further tuning"

Severity:
Pass: "HIGH" with evidence that data loss or compliance is at risk.
Fail: "HIGH" asserted without specifying the data-integrity or compliance exposure.

**Section 6 -- Long-Term Risk of Staying**

One paragraph. What happens over the next 6-12 months for teams that keep the
workaround? Name at least one compounding cost or accumulating risk with a time
horizon.
Pass: "within 6 months, the custom script will need re-porting as the upstream
API changes its response shape, breaking all teams on the workaround simultaneously"
Fail: "the workaround will become harder to maintain over time"

**Section 7 -- Steelman and Rebuttal** *(optional but scored)*

Present the strongest case for staying. Then rebut it specifically.
Pass: steelman names the specific friction point a real senior engineer would resist,
followed by a rebuttal that addresses that specific point.
Fail: "simplicity is valuable" as a steelman (a real skeptic's strongest claim
will name a concrete cost or risk, not a general principle).

Write artifact to: simulations/scout/inertia/{topic}-inertia-{date}.md
```

---

## V-03 -- Axis: C-19 Comprehensive (Five Named Sub-Protocols via Role Instructions)

**Hypothesis**: Adding named sub-protocol labels to all five multi-component
requirements -- via role instructions rather than template positions -- makes every
structural requirement independently addressable by name. The Replication Fidelity
Standard pattern generalizes to: Switching Cost Protocol, Failure Mode Standard,
Loss Condition Standard, and Anchored Rebuttal Protocol. Tests whether full C-19
coverage across all multi-component requirements is achievable through procedural
role instructions, and whether the named-protocol pattern increases C-13 compliance
without relying on template-static declarations.

This is R5 V-03 (adversarial role sequence, NAMED CLAIM anchor) with: (1) all five
multi-component requirements introduced by named sub-protocol labels, (2) minimal
inline counter-example pairs at the two most failure-prone requirement sites,
(3) explicit heading manifest in the synthesis step.

```
Auto-detect the feature from repo context. Do not prompt unless context is absent.

Run two sequential roles. Do not merge their output.

---

### ROLE 1: Inertia Advocate

You are a senior engineer who has used the current workaround for over a year.
You believe it is good enough. Your job is to describe and defend it.

1. **Describe the workaround -- Replication Fidelity Standard.** Name the
   workaround. Apply all three sub-requirements independently:
   a. Product names, not categories: "GitHub Actions" not "CI system";
      "Confluence page" not "doc"; "custom Python script via Makefile" not "script"
   b. Major steps in numbered sequence.
   c. Institutional knowledge flagged: any step requiring tribal context,
      undocumented conventions, or shared credentials a new team member lacks.
   Enough detail that another team with no prior context could reproduce the workflow.

2. **Make the case for staying.** Why is the workaround acceptable? What does it
   cost to switch vs. what does it gain? Name real friction points.

3. **State your STRONGEST CLAIM.** Write the single argument a skeptical engineer
   would stake their credibility on -- one complete declarative sentence.
   Label it: **STRONGEST CLAIM: [exact text of claim]**

4. **Identify the scenarios where the workaround holds.** What team sizes, project
   types, or usage patterns does it serve correctly?

Output labeled: `WORKAROUND PROFILE (Advocate)`

---

### ROLE 2: Inertia Analyst

You have read the Advocate's Workaround Profile. Produce the full inertia assessment.

1. **Assign the threat score.** Inertia threat is HIGH by default. Only downgrade
   with written justification. State the score explicitly.

2. **Apply the Switching Cost Protocol.** Three independently quantified dimensions --
   each must be a numeric estimate, not an adjective:
   - Time: hours or days per project or team.
     Pass: "2-4 hours per project for config migration" / Fail: "moderate effort"
   - Training: days, people affected, ramp friction.
     Pass: "1-2 days for 3-4 engineers covering X and Y" / Fail: "some training required"
   - Disruption: coordination overhead, dependencies changed -- name specific systems
     or teams affected.
     Pass: "CI pipeline paused for a 4-hour migration window, coordinated with ops"
     Fail: "team disruption expected"

3. **Apply the Failure Mode Standard.** What goes wrong if teams stay?
   Before writing the table, write this line:
   Required columns for this table: # | Failure Mode | Trigger | Impact | Severity

   | # | Failure Mode | Trigger | Impact | Severity |
   |---|-------------|---------|--------|---------|
   | 1 | [specific failure] | [what triggers it] | [what happens to team] | HIGH |
   | 2 | [specific failure] | [what triggers it] | [what happens to team] | MED |

   Minimum 2 rows. Trigger and Impact are separate columns.
   Severity: HIGH = data loss or compliance risk; MED = incorrect results;
   LOW = inefficiency.

4. **Apply the Loss Condition Standard.** When does inertia lose?
   Before writing the table, write this line:
   Required columns for this table: # | Condition | Observable Threshold | Verification Command

   | # | Condition | Observable Threshold | Verification Command |
   |---|-----------|---------------------|---------------------|
   | 1 | [scenario] | [measurable trigger] | [Tool: Action -> Result] |
   | 2 | [scenario] | [measurable trigger] | [Tool: Action -> Result] |

   Verification Command format: `[Tool or artifact]: [action] -> [result when threshold applies]`
   Pass: "Jira: open active sprint -> count rows Status=Active -> if >= 4, applies"
   Fail: "you can check" without naming a specific tool and concrete action.

5. **Long-term risk.** What accumulates over 6-12 months for teams that stay?

6. **Apply the Anchored Rebuttal Protocol.** Execute in order -- do not compress:
   a. Copy the STRONGEST CLAIM from the Advocate's Workaround Profile word-for-word.
      Label it: `NAMED CLAIM: "[exact text]"`
   b. Rebut only that claim. One paragraph. Explain specifically why it fails --
      with evidence or reasoning tied to the claim's content.
   c. Constraint: the rebuttal must be traceable to the named claim. Do not address
      a weaker point or redirect to general feature benefits.

Output labeled: `ANALYST VERDICT`

---

Synthesize both outputs into the final artifact. The artifact must contain the
following sections: Workaround Profile, Switching Cost Profile, Inertia Threat Score,
Workaround Failure Modes, Why Inertia Loses, Long-Term Risk, Anchored Rebuttal.

Write artifact to: simulations/scout/inertia/{topic}-inertia-{date}.md
```

---

## V-04 -- Combined: C-19 as Phase-Level Protocol Headers + C-20 Pairs Per Phase

**Hypothesis**: In a phase-structured prompt, using each phase header to declare a
named sub-protocol (C-19) and opening each phase with inline pass/fail pairs for
that phase's requirements (C-20) creates a two-level structural contract: the phase
boundary IS the protocol declaration site, and the pairs enforce within the phase.
This tests whether the phase-structure base (R5 V-04) naturally accommodates C-19
and C-20 by treating each phase as a named enforcement unit -- without adding a
separate role layer.

This is R5 V-04 (phase structure, two-level manifests) with: (1) each phase header
extended to declare its sub-protocol name, (2) inline pass/fail counter-example pairs
added at every requirement statement within each phase.

```
Auto-detect the feature from repo context. Do not prompt unless context absent.

You are running the inertia analysis. This is the most important analysis in the
Signal system. Every feature decision must answer: **why does inertia lose?**
If you cannot answer it, stop.

This output must contain the following sections:
- Phase 1: Workaround Map -- Replication Fidelity Standard
- Phase 2: Switching Cost -- Switching Cost Protocol
- Phase 3: Failure Mode Table -- Failure Mode Standard
- Phase 4A: Why Inertia Loses -- Loss Condition Standard
- Phase 4B: Steelman and Anchored Rebuttal -- Anchored Rebuttal Protocol
- Phase 4C: Long-Term Risk

Work through phases in order. Do not compress phases together.

---

### PHASE 1: MAP THE WORKAROUND -- Replication Fidelity Standard

What are teams actually doing today instead of using this feature?

Apply the Replication Fidelity Standard -- three independently required properties:

1. Tool names: product-level, not category-level.
   Pass: "GitHub Actions" / Fail: "CI system"
   Pass: "custom Python script invoked by a Makefile target" / Fail: "automation script"
2. Steps: enumerated in numbered sequence.
   Pass: "1. engineer runs script, 2. manually edits YAML, 3. commits and pushes"
   Fail: "team follows the deployment process"
3. Institutional knowledge: flagged explicitly.
   Pass: "step 3 requires posting in #deploy with a specific prefix -- not in
   onboarding docs" / Fail: [omitting an undocumented step]

Minimum: one named workaround, all three sub-requirements satisfied independently.

---

### PHASE 2: COST THE SWITCH -- Switching Cost Protocol

What would it cost a team to abandon the workaround and adopt the feature?

Apply the Switching Cost Protocol -- three independently quantified dimensions:

- **Time**: hours or days of migration work per project or per team.
  Pass: "2-4 hours per project for config migration" / Fail: "moderate effort"
- **Training**: days of learning, number of people affected, ramp-up friction.
  Pass: "1-2 days for 3-4 engineers, covering API changes and new config format"
  Fail: "some training required"
- **Disruption**: workflow interruption, coordination overhead, dependencies changed.
  Pass: "CI pipeline paused for 4-hour migration window, coordinated with ops team"
  Fail: "team disruption expected"

Threat score: **HIGH**. Required. Do not omit. Downgrade only with written
justification including evidence. Omitting = analysis failure.

---

### PHASE 3: BREAK THE WORKAROUND -- Failure Mode Standard

Where does the workaround fail if teams stay on it?

Apply the Failure Mode Standard -- two independently required properties per row:

- Trigger: the specific observable event or threshold that causes failure.
  Pass: "when queue depth exceeds 500 messages" / Fail: "under heavy load"
- Impact: what happens to the team when failure occurs.
  Pass: "events silently dropped with no error surfaced to the caller"
  Fail: "the workaround stops working"

Required columns for this table: # | Failure Mode | Trigger | Impact | Severity

| # | Failure Mode | Trigger | Impact | Severity |
|---|-------------|---------|--------|---------|
| 1 | [specific failure] | [what triggers it] | [what happens to the team] | HIGH |
| 2 | [specific failure] | [what triggers it] | [what happens to the team] | MED |

Minimum 2 rows. Trigger and Impact are separate columns -- do not merge.
Severity: HIGH = data loss or compliance risk; MED = incorrect results; LOW = inefficiency.

---

### PHASE 4: ANSWER THE QUESTION

**Part A -- Why Inertia Loses -- Loss Condition Standard**

Apply the Loss Condition Standard -- two independently required properties per row:

- Observable Threshold: measurable enough that a team can check it.
  Pass: "active project count >= 4" / Fail: "when teams get busy"
- Verification Command: names specific tool, concrete action, result when threshold applies.
  Pass: "Jira: open sprint board -> count Status=Active rows -> if >= 4, applies"
  Fail: "you can check project count" / Fail: "review your sprint board"

Required columns for this table: # | Condition | Observable Threshold | Verification Command

| # | Condition | Observable Threshold | Verification Command |
|---|-----------|---------------------|---------------------|
| 1 | [scenario] | [measurable trigger] | [Tool: Action -> Result] |
| 2 | [scenario] | [measurable trigger] | [Tool: Action -> Result] |

**Part B -- Steelman and Anchored Rebuttal -- Anchored Rebuttal Protocol**

Apply the Anchored Rebuttal Protocol -- three steps in sequence, do not merge:

1. Write the strongest argument for staying on the workaround.
   Label it: **STEELMAN**
   Pass: names a specific friction, cost, or risk a real skeptic would actually cite.
   Fail: "simplicity is valuable" (a principle, not a claim a real skeptic would stake
   credibility on).
2. Extract the single strongest specific claim. One declarative sentence.
   Label it: **NAMED CLAIM: "[exact text]"**
3. Rebut only that named claim. State specifically why it fails.
   Pass: rebuttal names what is wrong with the specific claim's logic or premise.
   Fail: "while simplicity matters, the feature offers..." without addressing the claim.

**Part C -- Long-Term Risk**

What accumulates over 6-12 months for teams that stay? Name a specific compounding
cost or divergence risk with a time horizon.

---

Write artifact to: simulations/scout/inertia/{topic}-inertia-{date}.md
```

---

## V-05 -- Combined: All Axes (Complete Named Sub-Protocols + Saturated C-20 + Full Stack)

**Hypothesis**: R5 V-05 demonstrated C-19 at the Replication Fidelity Standard
position and C-20 at the verification command and scale-limit positions. R6 V-05
extends both to full coverage: all five multi-component requirements receive named
sub-protocol labels (C-19 comprehensive), and every requirement statement that
admits a predictable violation receives an inline acceptable/unacceptable pair
(C-20 saturated). Combined with the full C-16/C-17/C-18 enforcement stack, this
eliminates every judgment-dependent requirement by converting it to inspection-based
verification. The reliability gradient prediction: the hardest of all five variations
to produce a violation without detection.

This is R5 V-05 (full scaffold: Competitor Zero framing, advocate/analyst roles,
Replication Fidelity Standard, NAMED CLAIM anchor, per-table column manifests, section
heading manifest) with: (1) four additional named sub-protocol labels beyond
Replication Fidelity Standard, (2) inline pass/fail pairs added to every requirement
in Sections A, C, D, and F.

```
Auto-detect the feature from repo context. Do not prompt unless context absent.

## Inertia Analysis -- Competitor Zero

The primary competitor is not another product. It is the option to do nothing and
keep the current workaround. This analysis must answer one question: **why does
inertia lose?** If you cannot answer it, stop.

This output must contain the following sections:
- WORKAROUND PROFILE (Advocate)
- A. Switching Cost Table -- Switching Cost Protocol
- B. Threat Score
- C. Workaround Failure Mode Table -- Failure Mode Standard
- D. Why Inertia Loses -- Loss Condition Standard
- E. Long-Term Risk of Staying
- F. Anchored Rebuttal -- Anchored Rebuttal Protocol

---

### STEP 1 -- ADVOCATE PASS

Take the role of a team member who has used the current workaround for 12+ months
and finds it acceptable.

**Workaround Profile -- Replication Fidelity Standard**

Describe the workaround so that another team with no prior context could reproduce
it independently. Apply all three sub-requirements:

1. Name each tool by product, not by category.
   Pass: "GitHub Actions" / Fail: "CI system"
   Pass: "Confluence page" / Fail: "doc"
   Pass: "custom Python script invoked by a Makefile target" / Fail: "automation script"
2. Enumerate the major steps in numbered sequence.
   Pass: "1. engineer opens Confluence template, 2. copies to project page, 3. edits
   four required fields, 4. pings #approvals"
   Fail: "team follows the standard documentation process"
3. Flag institutional knowledge: any step requiring tribal context, undocumented
   conventions, or shared credentials a new team member would not have.
   Pass: "step 4 requires posting in #approvals with a specific prefix -- documented
   only in the team wiki, not in company onboarding"
   Fail: [omitting the undocumented step or treating it as common knowledge]

State why the workaround is good enough: what it handles correctly, for which team
sizes and usage patterns.

**Strongest Objection to Switching**

Write the single strongest argument for staying on the workaround -- the one a
skeptical senior engineer would stake their credibility on. One complete declarative
sentence. Label it: **STRONGEST CLAIM: [exact text of claim]**

Label this section: `WORKAROUND PROFILE (Advocate)`

---

### STEP 2 -- ANALYST PASS

You have read the Advocate Pass. Produce the full inertia assessment.

**A. Switching Cost Table -- Switching Cost Protocol**

Three independently quantified dimensions. Apply the Switching Cost Protocol:
Pass: "2-4 hours per project for config migration" / Fail: "moderate effort"
Pass: "1-2 days for 3-4 engineers" / Fail: "some training required"
Pass: "CI pipeline paused for 4-hour window, coordinated with ops" /
Fail: "team disruption"

| Dimension | Estimate | What Drives This |
|-----------|----------|-----------------|
| Time | [X hours/days per project] | [migration steps] |
| Training | [X days, Y people] | [what must be learned] |
| Disruption | [coordination impact] | [who and what changes] |

All three rows required. Numeric or range-based estimates required.

**B. Threat Score**

```
Inertia Threat: HIGH
```

Required. Downgrade below HIGH only with written justification and supporting
evidence. Omitting this field = analysis failure.

**C. Workaround Failure Mode Table -- Failure Mode Standard**

Failure modes are distinct from switching costs. Failure modes = what goes wrong
if teams stay. Apply the Failure Mode Standard -- two independently required
properties per row:

Trigger: Pass: "when queue depth exceeds 500 messages" / Fail: "under heavy load"
Impact: Pass: "events silently dropped with no error surfaced to the caller" /
Fail: "the workaround stops working correctly"

Required columns for this table: # | Failure Mode | Trigger | Impact | Severity

| # | Failure Mode | Trigger | Impact | Severity |
|---|-------------|---------|--------|---------|
| 1 | [specific failure] | [edge case or threshold] | [what happens, to whom] | HIGH |
| 2 | [specific failure] | [edge case or threshold] | [what happens, to whom] | MED |
| + | ... | | | |

Minimum 2 rows. Trigger and Impact are separate columns -- do not merge.
Severity: HIGH = data loss or compliance risk; MED = incorrect results; LOW = inefficiency.
"Does not scale" without a named scale limit does not pass.

**D. Why Inertia Loses -- Loss Condition Standard**

Apply the Loss Condition Standard -- two independently required properties per row:
Observable Threshold: Pass: "active project count >= 4" / Fail: "when teams get busy"
Verification Command:
Pass: "Jira: open active sprint -> count Status=Active rows -> if >= 4, applies"
Pass: "GitHub: run `gh pr list --state open | wc -l` -> if >= 10, threshold met"
Fail: "you can check project count" / Fail: "review your sprint board"

Required columns for this table: # | Condition | Observable Threshold | Verification Command

| # | Condition | Observable Threshold | Verification Command |
|---|-----------|---------------------|---------------------|
| 1 | [specific scenario] | [measurable trigger] | [see format] |
| 2 | [specific scenario] | [measurable trigger] | [see format] |

Minimum 2 rows. Each condition must be falsifiable -- a team can check it against
their actual situation. The Verification Command must name a specific tool and
concrete action a team member could follow without a follow-up question.

**E. Long-Term Risk of Staying**

One paragraph. What accumulates over 6-12 months for teams that keep the
workaround? Name a specific compounding cost, growing debt, or divergence risk
with a time horizon.

**F. Anchored Rebuttal -- Anchored Rebuttal Protocol**

Apply the Anchored Rebuttal Protocol -- three steps in sequence, do not merge:

1. Copy the STRONGEST CLAIM from the Advocate Pass word-for-word.
   Label it: `NAMED CLAIM: "[exact text from Advocate Pass]"`

2. Rebut only that named claim. One paragraph. State specifically why it fails --
   with evidence or reasoning tied to the claim's content.
   Pass: rebuttal names the specific weakness in the claim's premise and ties the
   counter-argument to the claim's content.
   Fail: "while simplicity is valuable, the feature offers..." without addressing
   the claim's specific assertion.

3. Constraint: do not redirect to a different benefit. Do not address a weaker
   claim instead. The rebuttal must be traceable to the named claim -- a reader
   must be able to match the rebuttal to the specific claim above it.

---

Write artifact to: simulations/scout/inertia/{topic}-inertia-{date}.md
```

---

## Predicted R6 Scores (rubric v6)

Rubric v6 formula: `(essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/12 * 10)`

PARTIAL counts as 0.5.

### C-19 and C-20 compliance by variation

| Variation | C-19 mechanism | C-19 prediction | C-20 pairs present | C-20 prediction |
|-----------|---------------|-----------------|-------------------|-----------------|
| V-01 | "Replication Fidelity Standard" with 3 numbered items | PASS | "'GitHub Actions' not 'CI system'"; "Jira:...Pass/Fail" -- 2+ pairs | PASS |
| V-02 | "Replication Fidelity Standard" with 3 numbered items | PASS | Pass/Fail pair in every section (tools, steps, IK, switching cost, severity, threshold, verification, steelman) -- highest density | PASS |
| V-03 | 5 named sub-protocols in role instructions: Replication Fidelity Standard, Switching Cost Protocol, Failure Mode Standard, Loss Condition Standard, Anchored Rebuttal Protocol | PASS (multiple) | "'GitHub Actions' not 'CI system'"; Switching Cost pass/fail; Verification Command pass/fail -- 3+ pairs | PASS |
| V-04 | 5 named sub-protocols as phase headers: same set as V-03 | PASS (multiple) | Pass/Fail pairs at every phase requirement -- 8+ pairs | PASS |
| V-05 | 5 named sub-protocols in analyst pass: same set as V-03, all in template positions | PASS (multiple) | Pass/Fail pairs at every requirement in Sections A, C, D, F -- 10+ pairs, highest alongside V-02 | PASS |

### Full score predictions

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 Essential | PASS | PASS | PASS | PASS | PASS |
| C-02 Essential | PASS | PASS | PASS | PASS | PASS |
| C-03 Essential | PASS | PASS | PASS | PASS | PASS |
| C-04 Essential | PASS | PASS | PASS | PASS | PASS |
| C-05 Essential | PASS | PASS | PASS | PASS | PASS |
| C-06 Recommended | PASS | PASS | PASS | PASS | PASS |
| C-07 Recommended | PASS | PASS | PASS | PASS | PASS |
| C-08 Recommended | PASS | PASS | PASS | PASS | PASS |
| C-09 Aspirational | PASS | PASS | PASS | PASS | PASS |
| C-10 Aspirational | PASS | PASS | PASS | PASS | PASS |
| C-11 Aspirational | PASS | PASS | PASS | PASS | PASS |
| C-12 Aspirational | PARTIAL | PARTIAL | PASS | PASS | PASS |
| C-13 Aspirational | PASS | PASS | PASS | PASS | PASS |
| C-14 Aspirational | PASS | PASS | PASS | PASS | PASS |
| C-15 Aspirational | PASS | PASS | PASS | PASS | PASS |
| C-16 Aspirational | PASS | PASS | PASS | PASS | PASS |
| C-17 Aspirational | PASS | PASS | PASS (synthesis manifest) | PASS | PASS |
| C-18 Aspirational | PASS | PASS (Schema blocks) | PASS (role instruction) | PASS | PASS |
| C-19 Aspirational | PASS | PASS | PASS | PASS | PASS |
| C-20 Aspirational | PASS | PASS | PASS | PASS | PASS |
| **Predicted total** | **99.6** | **99.6** | **100** | **100** | **100** |

**Notes on C-12 PARTIAL for V-01 and V-02:**
Neither scaffold includes the explicit NAMED CLAIM instruction or Anchored Rebuttal
Protocol label. The model may produce an anchored rebuttal from context alone (the
role sequence and "rebut it specifically" instruction), but without the NAMED CLAIM
scaffold the output is unreliable. PARTIAL reflects uncertain compliance rather than
structural enforcement.

### Reliability Gradient Analysis

Once all variations score at or near 100, adversarial robustness is the differentiator:

| Variation | C-19 enforcement | C-20 enforcement | C-12 | Overall robustness |
|-----------|-----------------|-----------------|------|-------------------|
| V-01 | 1 named sub-protocol (Replication Fidelity Standard only) | Minimum 2 pairs | PARTIAL | Lowest -- gaps at C-12 and incomplete C-19 |
| V-02 | 1 named sub-protocol | Maximum density -- every requirement | PARTIAL | Higher on C-20 axis; same C-12 gap |
| V-03 | 5 named sub-protocols via role instructions | 3+ pairs at critical sites | PASS | Higher -- all sub-protocols named, NAMED CLAIM present |
| V-04 | 5 named sub-protocols as phase headers | 8+ pairs throughout phases | PASS | Higher -- phase boundaries + pair density |
| V-05 | 5 named sub-protocols in template positions | 10+ pairs throughout sections | PASS | Highest -- template + role + pairs at every site |

**R6 design conclusion**: C-19 and C-20 are independently satisfiable at minimum
(1 named sub-protocol + 2 pairs as in V-01/V-02) but the reliability gradient favors
comprehensive C-19 (all multi-component requirements named) paired with maximum C-20
density. V-05 assembles both at the highest density.

**C-19 and C-20 relationship (observed across R6)**: V-01 and V-02 demonstrate the
axes are genuinely independent -- V-01 is C-19 minimal / C-20 minimal; V-02 is C-19
minimal / C-20 maximal. V-03 through V-05 show that comprehensive C-19 (naming every
sub-protocol) naturally creates more C-20 anchor sites, since each named sub-protocol's
numbered items invite inline counter-example pairs.
