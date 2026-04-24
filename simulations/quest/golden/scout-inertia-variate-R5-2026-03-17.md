---
skill: quest-variate
skill_target: scout-inertia
date: 2026-03-17
round: 5
rubric: v5
variations: 5
---

# scout-inertia — Prompt Variations R5

## Context

R4 results: all 5 variations achieved 100/100 on rubric v4. The R4 scaffold
introduced C-16 (dedicated Trigger/Impact columns) and C-17 (synthesis-step section
heading manifest). The rubric notes that V-01 through V-04 all pass C-16 and C-17
but fail C-18 -- "one insertion per table brings any of them into compliance."

Rubric v5 adds one new criterion:
- **C-18**: Each tabular section opens with a per-table column manifest --
  "Required columns for this table: X | Y | Z" immediately before the table.
  This is the column-level analog of C-17 applied locally per table rather than
  globally per document.

**Reliability gradient note**: All R4 variations scored 100. Score and structural
enforcement strength are now independent axes. Once a scaffold reaches 100,
adversarial robustness (detectability of violations without reading cell content)
is the meaningful differentiator. V-01 < V-02 < V-03 < V-04 < V-05 on this axis.

## Variation Map

| ID | Axis | Hypothesis |
|----|------|------------|
| V-01 | Phrasing register: minimal inline C-18 insertion on inertia-framing base | Adding "Required columns for this table:" as a single inline statement before each table in the Competitor Zero prose format satisfies C-18 with the minimum change. Tests whether inline text (vs. block format) achieves the pre-commitment property. |
| V-02 | Output format: C-18 as explicit schema block | Expressing the column manifest as a `> Schema:` block -- visually separated from the table -- creates a stronger structural enforcement signal than inline text. A missing column is visible at the schema line, not only at the table header. Tests block format vs. inline. |
| V-03 | Role sequence: column manifests as analyst-role table-building instruction | Embedding C-18 inside the ANALYST role as an explicit step ("Before writing each table, declare its required columns") makes column manifest generation procedural rather than template-static. Tests whether procedural enforcement produces the same pre-commitment property as template insertion. |
| V-04 | Combined: lifecycle emphasis + output format | In a phase-structured prompt, placing column manifests at the start of each table-producing phase creates phase-level enforcement. Combined with a document-level section heading manifest (C-17), this produces a two-level structural contract: document level and table level. |
| V-05 | Combined: all axes | Full scaffold: Competitor Zero framing + table quantification + adversarial roles + phase structure + Replication Fidelity Standard (C-13) + Verification Command format (C-11) + NAMED CLAIM anchor (C-12) + section heading manifest (C-17) + per-table column manifests (C-18) at every table position. |

---

## V-01 -- Axis: Phrasing Register (Minimal Inline C-18 Insertion)

**Hypothesis**: The per-table column manifest can satisfy C-18 as a single inline
statement -- "Required columns for this table: X | Y | Z" -- immediately before each
table in the Competitor Zero prose format. This is the minimum viable insertion. It
tests whether inline text achieves the pre-commitment property: a missing column is
detectable at the declaration line without scanning the table header row.

This is R4 V-01 with one change per table: the inline column declaration. All other
sections are unchanged.

```
Auto-detect the feature from repo context. Do not prompt unless context is absent.

## Competitor Zero: Status Quo / Do Nothing

Before any named competitor, analyze the primary competitor: the option to do
nothing and keep the current workaround. Treat inertia as a named competitor.
Profile it fully.

This output must contain the following sections: Workaround Description, Switching
Cost Profile, Inertia Threat Score, Why Inertia Loses, Workaround Failure Modes,
Forward-Looking Risk, Steelman and Rebuttal.

**1. Workaround Description**

Describe the current workflow in concrete operational detail -- the specific tools,
manual steps, conventions, scripts, or habits teams use to accomplish the job this
feature would handle. Name the workaround (e.g., "manual YAML patching",
"Slack-based approval chain", "spreadsheet audit log"). One paragraph minimum.
Generic statements like "manual processes" do not pass -- a reader must be able to
picture the workflow.

**2. Switching Cost Profile**

Three line items, each with a numeric estimate or explicit N/A with justification:
- Time: hours or days to migrate existing setups, per project or per team
- Training: days of onboarding, number of people affected, ramp-up friction
- Disruption: coordination overhead, workflow interruption, dependencies that
  must change

**3. Inertia Threat Score**

Assign: HIGH (default and required). Downgrading below HIGH requires a written
justification with evidence. Absence of a score is an automatic analysis failure.

**4. Why Inertia Loses**

Required columns for this table: # | Condition | Observable Threshold | Verification Command

| # | Condition | Observable Threshold | Verification Command |
|---|-----------|---------------------|---------------------|
| 1 | [condition] | [measurable trigger] | [Tool: Action → Result when threshold applies] |
| 2 | [condition] | [measurable trigger] | [Tool: Action → Result when threshold applies] |

Verification Command format: `[Tool or artifact]: [what to open or run] →
[what the result looks like when threshold applies]`

Fail condition: "you can check" without naming a specific tool and concrete action.

**5. Workaround Failure Modes**

Distinct from switching costs. Failure modes = what goes wrong if you stay. Two or
more required.

Required columns for this table: # | Failure Mode | Trigger | Impact | Severity

| # | Failure Mode | Trigger | Impact | Severity |
|---|-------------|---------|--------|---------|
| 1 | [specific failure] | [what causes it] | [consequence to team] | HIGH |
| 2 | [specific failure] | [what causes it] | [consequence to team] | MED |

Trigger and Impact are separate columns -- do not merge.
Severity: HIGH = data loss or compliance risk; MED = incorrect results; LOW = inefficiency.

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

## V-02 -- Axis: Output Format (C-18 as Explicit Schema Block)

**Hypothesis**: Expressing the column manifest as a `> Schema:` block -- a visually
distinct declaration line above the table -- is structurally stronger than an inline
statement. The block format separates the pre-commitment from the table header:
a reader's eye lands on the Schema line before reaching the table, making a missing
or renamed column visible at the declaration site rather than requiring header-level
inspection. This is R4 V-02 (table-first required output structure) with the Schema
block added before Sections 4 and 5.

```
Auto-detect the feature from repo context. Do not prompt unless context is absent.

Analyze the inertia competitor -- the option to keep the current workaround instead
of adopting this feature. Answer the central question: **why does inertia lose?**
If you cannot answer it, stop and flag.

### Required Output Structure

**Section 1 -- Workaround Description**

One paragraph. Name the workaround. Describe the concrete workflow a team uses
today: tools, manual steps, conventions, scripts, or habits. Enough detail that a
reader can picture the workflow. Do not use "manual processes" without specifics.

**Section 2 -- Switching Cost Table**

| Dimension | Estimate | Basis |
|-----------|----------|-------|
| Time | [X hours/days per project] | [what drives this] |
| Training | [X days, Y people] | [what must be learned] |
| Disruption | [what changes, who is affected] | [coordination cost] |

All three rows required. Use numeric ranges. "Significant" is not an estimate.

**Section 3 -- Inertia Threat Score**

```
Threat: HIGH
```

Downgrade below HIGH only with written justification and evidence. Omitting this
field fails the analysis.

**Section 4 -- Why Inertia Loses**

Two or more conditions. Each must be falsifiable.

> Schema: # | Condition | Observable Threshold | Verification Command

| # | Condition | Observable Threshold | Verification Command |
|---|-----------|---------------------|---------------------|
| 1 | [condition] | [measurable trigger] | [see format below] |
| 2 | [condition] | [measurable trigger] | [see format below] |

**Verification Command format**: `[Tool or artifact]: [what you open or run] →
[what the result looks like when the threshold applies]`

Examples that pass:
- "Jira: open the active sprint board → count rows where Status = Active.
  If >= 4, condition applies."
- "GitHub: run `gh pr list --state open | wc -l` → if output >= 10, threshold met."

Examples that fail: "You can check project count" / "Review your sprint board"

**Section 5 -- Workaround Failure Modes**

Distinct from switching costs. Failure modes = what goes wrong if you stay.
Two or more required.

> Schema: # | Failure Mode | Trigger | Impact | Severity

| # | Failure Mode | Trigger | Impact | Severity |
|---|-------------|---------|--------|---------|
| 1 | [specific failure] | [what triggers it] | [consequence to team] | HIGH / MED / LOW |
| 2 | [specific failure] | [what triggers it] | [consequence to team] | HIGH / MED / LOW |

Trigger and Impact are separate columns -- do not merge into a single cell.

**Section 6 -- Long-Term Risk of Staying**

One paragraph. What happens over the next 6-12 months for teams that keep the
workaround? Name at least one compounding cost or accumulating risk with a
time horizon.

**Section 7 -- Steelman and Rebuttal** *(optional but scored)*

The strongest argument for staying. Then the specific rebuttal.

Write artifact to: simulations/scout/inertia/{topic}-inertia-{date}.md
```

---

## V-03 -- Axis: Role Sequence (Column Manifests as Analyst-Role Table-Building Instruction)

**Hypothesis**: Embedding the per-table column manifest inside the ANALYST role as
an explicit procedural step -- "Before writing each table, declare its required
columns" -- produces C-18 through procedural generation rather than template
insertion. The analyst generates the manifest as part of executing the role. This
tests whether procedural enforcement achieves the same pre-commitment property as
static template declarations (V-01, V-02). A role that skips the column declaration
step has visibly failed the role instruction, independently of the resulting table.

This is R4 V-03 (adversarial roles with NAMED CLAIM anchor) with the column manifest
instruction added to steps 3 and 4 of the ANALYST role.

```
Auto-detect the feature from repo context. Do not prompt unless context is absent.

Run two sequential roles. Do not merge their output.

---

### ROLE 1: Inertia Advocate

You are a senior engineer who has used the current workaround for over a year.
You believe it is good enough. Your job is to describe and defend it.

1. **Describe the workaround concretely.** Name it. Describe the exact workflow
   your team uses: tools, commands, conventions, manual steps. Be specific enough
   that someone else could follow the same process.

2. **Make the case for staying.** Why is the workaround acceptable? What does it
   cost to switch vs. what does it gain? Name real friction points in adopting
   the feature.

3. **State your STRONGEST CLAIM.** Write the single argument a skeptical engineer
   would stake their credibility on -- one declarative sentence. This must be the
   best version of the case for inertia, not a summary.
   Label it: **STRONGEST CLAIM: [your claim as a complete sentence]**

4. **Identify the scenarios where the workaround holds.** When does it work well?
   What team sizes, project types, or usage patterns does it serve correctly?

Output labeled: `ADVOCATE BRIEF`

---

### ROLE 2: Inertia Analyst

You have read the Advocate Brief. Your job is to determine whether inertia loses
and under what conditions.

1. **Assign the threat score.** Inertia threat is HIGH by default. Only downgrade
   with written justification. State the score explicitly.

2. **Quantify switching costs across three dimensions.**
   - Time: numeric estimate per project or team
   - Training: days, people affected, ramp friction
   - Disruption: coordination overhead, dependencies changed
   Do not use adjectives alone. Numbers or ranges required.

3. **Build the failure mode table.**
   Before writing the table, write this line:
   Required columns for this table: # | Failure Mode | Trigger | Impact | Severity

   | # | Failure Mode | Trigger | Impact | Severity |
   |---|-------------|---------|--------|---------|
   | 1 | [specific failure] | [what triggers it] | [what happens to team] | HIGH |
   | 2 | [specific failure] | [what triggers it] | [what happens to team] | MED |

   Minimum 2 rows. Trigger and Impact are separate columns. Rank by severity.

4. **Build the inertia-loss table.**
   Before writing the table, write this line:
   Required columns for this table: # | Condition | Observable Threshold | Verification Command

   | # | Condition | Observable Threshold | Verification Command |
   |---|-----------|---------------------|---------------------|
   | 1 | [scenario] | [measurable trigger] | [Tool: Action → Result] |
   | 2 | [scenario] | [measurable trigger] | [Tool: Action → Result] |

   Verification Command format: `[Tool or artifact]: [action] → [result when threshold applies]`
   Fail condition: "you can check" without a named tool and concrete action.

5. **Long-term risk.** What happens in 6-12 months for teams that stay on the
   workaround?

6. **Anchored Rebuttal.** Follow this sequence exactly -- do not compress steps:
   a. Copy the STRONGEST CLAIM from the Advocate Brief word-for-word.
      Label it: `NAMED CLAIM: "[exact text from Advocate Brief]"`
   b. Rebut only that claim. One paragraph. Address specifically why that claim
      fails -- with evidence or reasoning tied to the claim's content.
   c. Constraint: do not address a weaker point instead. The rebuttal must be
      traceable to the named claim.

Output labeled: `ANALYST VERDICT`

---

Synthesize both outputs into the final artifact.

Write artifact to: simulations/scout/inertia/{topic}-inertia-{date}.md
```

---

## V-04 -- Combined: Lifecycle Emphasis + Output Format

**Hypothesis**: In a phase-structured prompt, placing the column manifest at the
start of each table-producing phase (before the table definition) creates
phase-level enforcement. When combined with a document-level section heading
manifest (C-17, inherited from R4), the result is a two-level structural contract:
a reader can verify section coverage from the manifest and column coverage from the
per-phase declaration, without reading any table content. The combination makes both
section omission (C-17) and column omission (C-18) structurally visible at their
respective declaration sites.

This is R4 V-04 (phase structure) with column manifests added at the top of Phase 3
and Part A of Phase 4.

```
Auto-detect the feature from repo context. Do not prompt unless context absent.

You are running the inertia analysis. This is the most important analysis in the
Signal system. Every feature decision must answer: **why does inertia lose?**
If you cannot answer it, stop.

This output must contain the following sections:
- Phase 1: Workaround Map
- Phase 2: Switching Cost
- Phase 3: Failure Mode Table
- Phase 4A: Why Inertia Loses
- Phase 4B: Steelman and Anchored Rebuttal
- Phase 4C: Long-Term Risk

Work through four phases in order. Each phase has a defined scope.
Do not compress phases together.

---

### PHASE 1: MAP THE WORKAROUND

What are teams actually doing today instead of using this feature?

Name the workaround. Describe it concretely: the tools involved, the manual steps,
the conventions teams rely on, the scripts or habits that fill the gap. Write enough
that a reader unfamiliar with the codebase can picture the workflow.

Minimum: one named workaround, described in operational detail.
Fail condition: "teams use manual processes" with no specifics.

---

### PHASE 2: COST THE SWITCH

What would it cost a team to abandon the workaround and adopt the feature?

Three dimensions, each with a numeric estimate or an explicit N/A with justification:
- **Time** -- hours or days of migration work per project or per team
- **Training** -- days of learning, number of people affected, ramp-up friction
- **Disruption** -- workflow interruption, coordination overhead, dependencies
  that must change

Fail condition: adjectives only ("moderate", "significant") with no numeric basis.

Threat score: **HIGH**. Required. Do not omit. Do not downgrade without a written
justification that includes evidence.

---

### PHASE 3: BREAK THE WORKAROUND

Where does the workaround fail if teams stay on it?

Required columns for this table: # | Failure Mode | Trigger | Impact | Severity

| # | Failure Mode | Trigger | Impact | Severity |
|---|-------------|---------|--------|---------|
| 1 | [specific failure] | [what triggers it] | [what happens to the team] | HIGH |
| 2 | [specific failure] | [what triggers it] | [what happens to the team] | MED |

Minimum 2 rows. Trigger and Impact are separate columns -- do not merge.
Severity: HIGH = data loss or compliance risk; MED = incorrect results; LOW = inefficiency.
Fail condition: "the workaround has limitations" or "it doesn't scale" without specifics.

---

### PHASE 4: ANSWER THE QUESTION

**Part A -- Why Inertia Loses**

Required columns for this table: # | Condition | Observable Threshold | Verification Command

| # | Condition | Observable Threshold | Verification Command |
|---|-----------|---------------------|---------------------|
| 1 | [scenario] | [measurable trigger] | [Tool: Action → Result] |
| 2 | [scenario] | [measurable trigger] | [Tool: Action → Result] |

Verification Command format: `[Tool or artifact]: [what you open or run] → [what
the result looks like when the threshold applies]`

Fail condition: "you can check project count", "review your sprint board", or any
action without a named tool and concrete output.

**Part B -- Steelman and Anchored Rebuttal**

Follow three steps in sequence -- do not merge them:

1. Write the strongest argument a skeptical senior engineer would make for staying
   on the workaround. Label it: **STEELMAN**

2. Extract the single strongest specific claim from your steelman. Write it as a
   complete declarative sentence. Label it: **NAMED CLAIM: "[exact text]"**

3. Rebut only that named claim. One paragraph. Address specifically why that claim
   fails. Do not pivot to feature benefits unrelated to the claim. Do not address
   a weaker point instead.

**Part C -- Long-Term Risk**

What accumulates over 6-12 months for teams that stay? Name a specific compounding
cost or divergence risk with a time horizon.

---

Write artifact to: simulations/scout/inertia/{topic}-inertia-{date}.md
```

---

## V-05 -- Combined: All Axes

**Hypothesis**: R4 V-05 scored 100/100 on all v4 criteria by combining Competitor
Zero framing, table-enforced quantification, adversarial role sequence, phase
structure, Replication Fidelity Standard (C-13), Verification Command format (C-11),
NAMED CLAIM anchor (C-12), and section heading manifest (C-17). R5 V-05 adds
per-table column manifests (C-18) at every table position -- Section C (Failure Mode
Table) and Section D (Why Inertia Loses) -- without restructuring the proven scaffold.
The column manifests are the only additions from R4 V-05.

```
Auto-detect the feature from repo context. Do not prompt unless context absent.

## Inertia Analysis -- Competitor Zero

The primary competitor is not another product. It is the option to do nothing and
keep the current workaround. This analysis must answer one question: **why does
inertia lose?** If you cannot answer it, stop.

This output must contain the following sections:
- WORKAROUND PROFILE (Advocate)
- A. Switching Cost Table
- B. Threat Score
- C. Workaround Failure Mode Table
- D. Why Inertia Loses
- E. Long-Term Risk of Staying
- F. Anchored Rebuttal

---

### STEP 1 -- ADVOCATE PASS

Take the role of a team member who has used the current workaround for 12+ months
and finds it acceptable.

**Workaround Profile -- Replication Fidelity Standard**

Describe the workaround so that another team with no prior context could reproduce
it independently:
- Name each tool by product, not by category. "GitHub Actions" not "CI system."
  "Confluence page" not "doc." "Custom Python script invoked by a Makefile target"
  not "automation script."
- Enumerate the major steps in numbered sequence.
- Flag institutional knowledge: any step requiring tribal context, undocumented
  conventions, or shared credentials that a new team member would not have.

State why the workaround is good enough: what it handles correctly, for which team
sizes and usage patterns.

**Strongest Objection to Switching**

Write the single strongest argument for staying on the workaround -- the one a
skeptical senior engineer would stake their credibility on. One complete declarative
sentence.

Label it: **STRONGEST CLAIM: [exact text of claim]**

Label this section: `WORKAROUND PROFILE (Advocate)`

---

### STEP 2 -- ANALYST PASS

You have read the Advocate Pass. Produce the full inertia assessment.

**A. Switching Cost Table**

| Dimension | Estimate | What Drives This |
|-----------|----------|-----------------|
| Time | [X hours/days per project] | [migration steps] |
| Training | [X days, Y people] | [what must be learned] |
| Disruption | [coordination impact] | [who and what changes] |

All three rows required. Numeric or range-based estimates required.
"Significant" is not an estimate.

**B. Threat Score**

```
Inertia Threat: HIGH
```

Required. Downgrade below HIGH only with written justification and supporting
evidence. Omitting this field = analysis failure.

**C. Workaround Failure Mode Table**

Failure modes are distinct from switching costs. Failure modes = what goes wrong
if teams stay.

Required columns for this table: # | Failure Mode | Trigger | Impact | Severity

| # | Failure Mode | Trigger | Impact | Severity |
|---|-------------|---------|--------|---------|
| 1 | [specific failure] | [edge case or threshold] | [what happens, to whom] | HIGH |
| 2 | [specific failure] | [edge case or threshold] | [what happens, to whom] | MED |
| + | ... | | | |

Minimum 2 rows. Trigger and Impact are separate columns -- do not merge.
"Does not scale" without a scale limit does not pass. Severity column required.

**D. Why Inertia Loses**

Required columns for this table: # | Condition | Observable Threshold | Verification Command

| # | Condition | Observable Threshold | Verification Command |
|---|-----------|---------------------|---------------------|
| 1 | [specific scenario] | [measurable trigger] | [see format] |
| 2 | [specific scenario] | [measurable trigger] | [see format] |

Minimum 2 rows. Each condition must be falsifiable -- a team can check it against
their actual situation.

**Verification Command format**: `[Tool or artifact]: [what you open or run] →
[what the result looks like when the threshold applies]`

Examples that pass:
- "Jira: open the active sprint board → count rows where Status = Active.
  If >= 4, condition applies."
- "GitHub: run `gh pr list --state open | wc -l` → if output >= 10, threshold met."

Examples that fail:
- "You can check project count"
- "Review your sprint board"

The column must name a specific tool and a concrete action a team member could
follow without a follow-up question.

**E. Long-Term Risk of Staying**

One paragraph. What accumulates over 6-12 months for teams that keep the
workaround? Name a specific compounding cost, growing debt, or divergence risk
with a time horizon.

**F. Anchored Rebuttal**

Three-step sequence -- execute in order, do not merge:

1. Copy the STRONGEST CLAIM from the Advocate Pass word-for-word.
   Label it: `NAMED CLAIM: "[exact text from Advocate Pass]"`

2. Rebut only that named claim. One paragraph. State specifically why it fails --
   with evidence or reasoning tied to the claim's content.

3. Constraint: do not redirect to a different benefit. Do not address a weaker
   claim instead. The rebuttal must be traceable to the named claim -- a reader
   must be able to match the rebuttal to the specific claim above it.

---

Write artifact to: simulations/scout/inertia/{topic}-inertia-{date}.md
```

---

## Predicted R5 Scores (rubric v5)

Rubric v5 scoring: `(essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/10 * 10)`

| Variation | C-18 | C-16 | C-17 | All C-01--C-17 carried | Predicted total |
|-----------|------|------|------|------------------------|----------------|
| V-01 | PASS (inline "Required columns:" before each table) | PASS (carried) | PASS (carried) | All pass | 100 |
| V-02 | PASS (Schema block before each table) | PASS (carried) | PASS (carried) | All pass | 100 |
| V-03 | PASS (analyst-role "before writing, declare columns" instruction) | PASS (carried) | PASS (carried) | All pass | 100 |
| V-04 | PASS (column manifest at start of Phase 3 and Phase 4A) | PASS (carried) | PASS (section manifest at top) | All pass | 100 |
| V-05 | PASS (column manifest before Section C and Section D) | PASS (separate columns) | PASS (heading manifest at top) | All pass | 100 |

**R5 design goal**: All 5 variations achieve 100/100 on rubric v5.
Single-axis variations (V-01, V-02, V-03) isolate the C-18 expression form for
reliability gradient analysis. V-04 tests C-18 combined with phase structure.
V-05 confirms the full scaffold with C-18 at all table positions simultaneously.

## Reliability Gradient Analysis

Once all variations score 100, adversarial robustness is the differentiator:

| Variation | C-18 form | Violation detectability |
|-----------|-----------|------------------------|
| V-01 | Inline text: "Required columns for this table: X | Y | Z" | Lowest -- inline text can be omitted without breaking visual structure |
| V-02 | Schema block: `> Schema: X | Y | Z` on its own line | Higher -- block-level element creates visual gap when missing |
| V-03 | Procedural instruction: "Before writing each table, write this line" | Higher -- role step violation is structurally visible in role output |
| V-04 | Phase-level declaration: column manifest as first element of phase | Highest among single-axis -- phase boundary enforces declaration order |
| V-05 | All three forms simultaneously: phase, inline, and template | Highest -- triple enforcement; requires three independent omissions to fail |
