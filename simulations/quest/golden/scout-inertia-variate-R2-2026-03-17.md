---
skill: quest-variate
skill_target: scout-inertia
date: 2026-03-17
round: 2
rubric: v2
variations: 5
---

# scout-inertia — Prompt Variations R2

## Context

R1 results: all 5 variations achieved Gold band on rubric v1. V-05 scored 100/100.
Rubric v2 adds three aspirational criteria: C-11 (verification method), C-12 (anchored rebuttal),
C-13 (replication fidelity). R1 excellence signals identified partial coverage; R2 targets each
explicitly.

## Variation Map

| ID | Axis | Hypothesis |
|----|------|------------|
| V-01 | Workaround description upgraded to Replication Fidelity Standard (C-13 target) | Adding a three-item checklist to the workaround section — tools named by product, steps enumerated, institutional knowledge flagged — mechanically forces C-13 without restructuring any other section. V-01 is otherwise R1 V-01 with this single change. |
| V-02 | "Verifiable How" column renamed "Verification Command" with explicit format (C-11 target) | The format constraint `[Tool]: [Action] → [What you see when threshold applies]` blocks generic "you can check" text at the structural level. A column name alone is insufficient; the named format makes non-compliance visibly malformed. |
| V-03 | Anchored rebuttal via mandatory STRONGEST CLAIM extraction (C-12 target) | Role 1 must label its best argument as STRONGEST CLAIM. Role 2 must copy it verbatim as NAMED CLAIM before rebutting. The copy step makes the claim→rebuttal link traceable by construction. |
| V-04 | Combined C-11 + C-12 in phase structure | Pairs the Verification Command column with the anchored rebuttal in the lifecycle-phase format (R1 V-04 base). Two new aspirational criteria land within the existing phase scaffold without adding a full adversarial role sequence. |
| V-05 | Full combined: R1 V-05 scaffold + all three new targets (C-11 + C-12 + C-13) | R1 V-05 scored 100/100 on v1 criteria by combining framing, tables, adversarial roles, and phase structure. R2 V-05 adds the three targeted mechanisms to each corresponding section of the proven scaffold without restructuring it. |

---

## V-01 — Axis: Replication Fidelity (C-13 target)

**Hypothesis**: Adding a "Replication Fidelity Standard" requirement to the workaround
description — tools named by product, steps enumerated in sequence, institutional knowledge
flagged — causes C-13 to pass by structural constraint. The rest of the prompt is unchanged
from R1 V-01 to isolate the single-axis effect.

```
Auto-detect the feature from repo context. Do not prompt unless context is absent.

## Competitor Zero: Status Quo / Do Nothing

Before any named competitor, analyze the primary competitor: the option to do nothing
and keep the current workaround.

Treat inertia as a named competitor. Profile it fully:

**1. What the workaround looks like today — Replication Fidelity Standard**

Describe the current workflow in concrete operational detail. This section must meet
the Replication Fidelity Standard: another team with no prior context could reproduce
the workaround from your description alone.

To meet the standard:
- Name each tool by product, not by category. "GitHub Actions" not "CI system."
  "Confluence page" not "doc." "Custom Python script invoked by a Makefile target"
  not "automation script."
- Enumerate the major steps in numbered sequence. What does the team do first,
  second, third?
- Surface institutional knowledge. Flag any step that requires information a new
  team member would not have — undocumented conventions, tribal context, shared
  credentials, or implicit agreements.

Name the workaround (e.g., "manual YAML patching", "Slack-based approval chain",
"spreadsheet audit log").

Fail condition: tools named only by category, steps described in prose without
enumeration, or institutional knowledge gaps left implicit.

**2. Switching cost profile**

Three line items, each with a numeric estimate or explicit N/A with justification:
- Time: hours or days to migrate existing setups, per project or per team
- Training: days of onboarding, number of people affected, ramp-up friction
- Disruption: coordination overhead, workflow interruption, dependencies that
  must change

**3. Inertia Threat Score**

Assign: HIGH (default and required). Downgrading below HIGH requires a written
justification with evidence. Absence of a score is an automatic analysis failure.

**4. Why Inertia Loses**

State 2+ specific conditions under which the do-nothing option loses. Each condition
must be falsifiable: a team could check whether it applies to their actual situation.
Restating feature benefits does not count. "When teams have more than 3 concurrent
projects" counts. "When teams want simplicity" does not.

**5. Workaround Failure Modes**

Distinct from switching costs. Identify 2+ specific ways the workaround breaks down.
For each mode, name what triggers it and its severity (HIGH = data loss or compliance
risk; MED = incorrect results; LOW = inefficiency only).

**6. Forward-Looking Risk**

What happens to teams that stay on the workaround for the next 6-12 months? Name a
specific compounding cost, accumulating debt, or divergence risk with a time horizon.

**7. The Case for Staying (Steelman)**

Write the strongest possible argument a skeptical senior engineer would make for
staying on the workaround. Label it explicitly. Then rebut it specifically. A weak
steelman is worse than none — if you cannot write a strong one, flag it.

---

After profiling Competitor Zero, add:
- Named competitors (3-5): feature overlap, threat level (HIGH/MEDIUM/LOW),
  one-line differentiation
- The whitespace: what no competitor owns
- Table stakes: what any entrant must match

Write artifact to: simulations/scout/inertia/{topic}-inertia-{date}.md
```

---

## V-02 — Axis: Verification Command Column (C-11 target)

**Hypothesis**: Renaming "Verifiable How" to "Verification Command" and requiring
the format `[Tool/artifact]: [Action] → [What you see if threshold applies]` makes
non-compliance structurally visible. A cell reading "you can check project count"
fails the format check on inspection, where it might pass an instruction-only
enforcement. This is otherwise R1 V-02 with the single column change.

```
Auto-detect the feature from repo context. Do not prompt unless context is absent.

Analyze the inertia competitor — the option to keep the current workaround instead
of adopting this feature. Answer the central question: **why does inertia lose?**
If you cannot answer it, stop and flag.

### Required Output Structure

**Section 1 — Workaround Description**

One paragraph. Name the workaround. Describe the concrete workflow a team uses
today: tools, manual steps, conventions, scripts, or habits. Enough detail that a
reader can picture the workflow. Do not use "manual processes" without specifics.

**Section 2 — Switching Cost Table**

| Dimension | Estimate | Basis |
|-----------|----------|-------|
| Time | [X hours/days per project] | [what drives this] |
| Training | [X days, Y people] | [what must be learned] |
| Disruption | [what changes, who is affected] | [coordination cost] |

All three rows required. Use numeric ranges. "Significant" is not an estimate.

**Section 3 — Inertia Threat Score**

```
Threat: HIGH
```

Downgrade below HIGH only with written justification and evidence. Omitting this
field fails the analysis.

**Section 4 — Why Inertia Loses**

Two or more conditions. Each must be falsifiable — a team could verify it against
their situation.

| # | Condition | Observable Threshold | Verification Command |
|---|-----------|---------------------|---------------------|
| 1 | [condition] | [measurable trigger] | [see format below] |
| 2 | [condition] | [measurable trigger] | [see format below] |

**Verification Command format**: `[Tool or artifact]: [what you open or run] →
[what the result looks like when the threshold applies]`

Examples that pass:
- "Jira: open the active sprint board → count rows where Status = Active. If ≥ 4,
  condition applies."
- "GitHub: run `gh pr list --state open | wc -l` → if output ≥ 10, threshold met."

Examples that fail:
- "You can check project count"
- "Review your sprint board"
- "Look at the metrics dashboard"

The Verification Command must name a specific tool and specify a concrete action.
A reader must be able to follow it without asking a follow-up question.

**Section 5 — Workaround Failure Modes**

Distinct from switching costs. Failure modes = what goes wrong if you stay.
Two or more required.

| # | Failure Mode | Trigger / Edge Case | Severity |
|---|-------------|---------------------|---------|
| 1 | [specific failure] | [what triggers it] | HIGH / MED / LOW |
| 2 | [specific failure] | [what triggers it] | HIGH / MED / LOW |

**Section 6 — Long-Term Risk of Staying**

One paragraph. What happens over the next 6-12 months for teams that keep the
workaround? Name at least one compounding cost or accumulating risk with a
time horizon.

**Section 7 — Steelman and Rebuttal** *(optional but scored)*

The strongest argument for staying. Then the specific rebuttal.

Write artifact to: simulations/scout/inertia/{topic}-inertia-{date}.md
```

---

## V-03 — Axis: Anchored Rebuttal Sequence (C-12 target)

**Hypothesis**: Adding a mandatory STRONGEST CLAIM labeling step in Role 1 and
a verbatim NAMED CLAIM copy-before-rebut constraint in Role 2 forces the traceable
claim→rebuttal link that C-12 requires. Without the copy step, Role 2 may rebut a
paraphrase or a weaker version of the claim. This is R1 V-03 with the two-step
rebuttal sequence added to Role 2 Step 6.

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
   would stake their credibility on — one declarative sentence. This must be the
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

3. **Find the failure modes.** Identify 2+ specific failure modes: edge cases,
   scale limits, error-prone steps, silent failure conditions. Rank by severity.

4. **Answer: why does inertia lose?** Write 2+ falsifiable conditions under which
   the workaround becomes worse than adopting the feature. Each condition must be
   checkable against a real team's situation. Do not restate feature benefits.

5. **Long-term risk.** What happens in 6-12 months for teams that stay on the
   workaround?

6. **Anchored Rebuttal.** Follow this sequence exactly — do not compress steps:
   a. Copy the STRONGEST CLAIM from the Advocate Brief word-for-word.
      Label it: `NAMED CLAIM: "[exact text from Advocate Brief]"`
   b. Rebut only that claim. Write one paragraph that addresses specifically why
      that claim fails — with evidence or reasoning tied to the claim's content.
   c. Constraint: do not address a weaker point instead. Do not pivot to feature
      benefits unrelated to the named claim. The rebuttal must be traceable to
      the named claim.

Output labeled: `ANALYST VERDICT`

---

Synthesize both outputs into the final artifact.

Write artifact to: simulations/scout/inertia/{topic}-inertia-{date}.md
```

---

## V-04 — Combined: Verification Command + Anchored Rebuttal (C-11 + C-12)

**Hypothesis**: Pairing the Verification Command column (V-02) with the anchored
rebuttal structure (V-03) inside the lifecycle-phase format (R1 V-04 base) delivers
simultaneous C-11 and C-12 coverage without adding a full adversarial role sequence.
The phase structure provides the fail-condition scaffolding; the new additions slot
cleanly into Phases 4 and the steelman extension.

```
Auto-detect the feature from repo context. Do not prompt unless context absent.

You are running the inertia analysis. This is the most important analysis in the
Signal system. Every feature decision must answer: **why does inertia lose?**
If you cannot answer it, stop.

Work through four phases in order. Each phase has a defined scope. Do not compress
phases together.

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

- **Time** — hours or days of migration work per project or per team
- **Training** — days of learning, number of people affected, ramp-up friction
- **Disruption** — workflow interruption, coordination overhead, dependencies
  that must change

Fail condition: adjectives only ("moderate", "significant") with no numeric basis.

Threat score: **HIGH**. Required. Do not omit. Do not downgrade without a written
justification that includes evidence.

---

### PHASE 3: BREAK THE WORKAROUND

Where does the workaround fail if teams stay on it?

Find 2+ specific failure modes — concrete breakdowns: edge cases the workaround
cannot handle, scale thresholds it hits, steps that produce incorrect results,
silent failure conditions. For each failure mode, name what triggers it.

Rank failure modes by severity: HIGH (data loss, compliance risk), MED (incorrect
results), LOW (inefficiency).

Fail condition: "the workaround has limitations" or "it doesn't scale" without
specifics.

---

### PHASE 4: ANSWER THE QUESTION

**Part A — Why Inertia Loses**

| # | Condition | Observable Threshold | Verification Command |
|---|-----------|---------------------|---------------------|
| 1 | [scenario] | [measurable trigger] | [Tool: Action → Result when threshold applies] |
| 2 | [scenario] | [measurable trigger] | [Tool: Action → Result when threshold applies] |

Verification Command format: `[Tool or artifact]: [what you open or run] → [what
the result looks like when the threshold applies]`

Fail condition for this column: "you can check project count", "review your sprint
board", or any description of what could be done without a named tool and concrete
action.

**Part B — Steelman and Anchored Rebuttal**

Follow three steps in sequence — do not merge them:

1. Write the strongest argument a skeptical senior engineer would make for staying
   on the workaround. Label it: **STEELMAN**

2. Extract the single strongest specific claim from your steelman. Write it as a
   complete declarative sentence. Label it: **NAMED CLAIM: "[exact text]"**

3. Rebut only that named claim. One paragraph. Address specifically why that claim
   fails. Do not pivot to feature benefits unrelated to the claim. Do not address
   a weaker point instead.

**Part C — Long-Term Risk**

What accumulates over 6-12 months for teams that stay? Name a specific compounding
cost or divergence risk with a time horizon.

---

Write artifact to: simulations/scout/inertia/{topic}-inertia-{date}.md
```

---

## V-05 — Full Combined: R1 V-05 Scaffold + C-11 + C-12 + C-13

**Hypothesis**: R1 V-05 scored 100/100 on v1 criteria by integrating four mechanisms:
inertia-as-named-competitor framing, table-enforced quantification, adversarial role
sequence, and explicit phase structure. Adding the three targeted mechanisms to the
corresponding sections of that proven scaffold — (1) Replication Fidelity Standard
to STEP 1 workaround description, (2) Verification Command column and format to
the Why Inertia Loses table, (3) NAMED CLAIM copy-before-rebut to Section F —
produces simultaneous passes on all 13 rubric criteria without restructuring the
scaffold that scored 100/100.

```
Auto-detect the feature from repo context. Do not prompt unless context absent.

## Inertia Analysis — Competitor Zero

The primary competitor is not another product. It is the option to do nothing and
keep the current workaround. This analysis must answer one question: **why does
inertia lose?** If you cannot answer it, stop.

---

### STEP 1 — ADVOCATE PASS

Take the role of a team member who has used the current workaround for 12+ months
and finds it acceptable.

**Workaround Profile — Replication Fidelity Standard**

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

Write the single strongest argument for staying on the workaround — the one a
skeptical senior engineer would stake their credibility on. One complete declarative
sentence.

Label it: **STRONGEST CLAIM: [exact text of claim]**

Label this section: `WORKAROUND PROFILE (Advocate)`

---

### STEP 2 — ANALYST PASS

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

| # | Failure Mode | Trigger | Severity |
|---|-------------|---------|---------|
| 1 | [specific failure] | [edge case or threshold] | HIGH |
| 2 | [specific failure] | [edge case or threshold] | MED |
| + | ... | | |

Minimum 2 rows. "Does not scale" without a scale limit does not pass. Severity
column required.

**D. Why Inertia Loses**

| # | Condition | Observable Threshold | Verification Command |
|---|-----------|---------------------|---------------------|
| 1 | [specific scenario] | [measurable trigger] | [see format] |
| 2 | [specific scenario] | [measurable trigger] | [see format] |

Minimum 2 rows. Each condition must be falsifiable — a team can check it against
their actual situation.

**Verification Command format**: `[Tool or artifact]: [what you open or run] →
[what the result looks like when the threshold applies]`

Examples that pass:
- "Jira: open the active sprint board → count rows where Status = Active.
  If ≥ 4, condition applies."
- "GitHub: run `gh pr list --state open | wc -l` → if output ≥ 10, threshold met."

Examples that fail:
- "You can check project count"
- "Review your sprint board"

The column must name a specific tool and specify a concrete action a team member
could follow without a follow-up question.

**E. Long-Term Risk of Staying**

One paragraph. What accumulates over 6-12 months for teams that keep the
workaround? Name a specific compounding cost, growing debt, or divergence risk
with a time horizon.

**F. Anchored Rebuttal**

Three-step sequence — execute in order, do not merge:

1. Copy the STRONGEST CLAIM from the Advocate Pass word-for-word.
   Label it: `NAMED CLAIM: "[exact text from Advocate Pass]"`

2. Rebut only that named claim. One paragraph. State specifically why it fails —
   with evidence or reasoning tied to the claim's content.

3. Constraint: do not redirect to a different benefit. Do not address a weaker
   claim instead. The rebuttal must be traceable to the named claim — a reader
   must be able to match the rebuttal to the specific claim above it.

---

Write artifact to: simulations/scout/inertia/{topic}-inertia-{date}.md
```

---

## Predicted R2 Scores (rubric v2)

Rubric v2 scoring: `(essential_pass/5 × 60) + (recommended_pass/3 × 30) + (aspirational_pass/5 × 10)`

| Variation | C-11 | C-12 | C-13 | All v1 criteria | Predicted total |
|-----------|------|------|------|-----------------|----------------|
| V-01 | FAIL (no change) | PARTIAL (no anchor) | PASS (checklist) | All pass | ~94 |
| V-02 | PASS (format constraint) | PARTIAL (no anchor) | FAIL (no upgrade) | All pass | ~94 |
| V-03 | FAIL (no column) | PASS (NAMED CLAIM copy) | PASS (role 1 fidelity) | All pass | ~96 |
| V-04 | PASS (column + format) | PASS (3-step anchor) | FAIL (no upgrade) | All pass | ~96 |
| V-05 | PASS (column + format) | PASS (3-step anchor) | PASS (checklist) | All pass | ~100 |

**R2 design goal**: V-05 to achieve Gold on all 13 criteria simultaneously.
Single-axis variations (V-01, V-02, V-03) isolate each new criterion for signal isolation.
V-04 tests C-11+C-12 combination without C-13 to confirm independence of axes.
