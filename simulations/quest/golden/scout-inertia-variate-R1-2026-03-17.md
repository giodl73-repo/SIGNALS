---
skill: quest-variate
skill_target: scout-inertia
date: 2026-03-17
round: 1
variations: 5
---

# scout-inertia — Prompt Variations R1

## Variation Map

| ID | Axis | Hypothesis |
|----|------|------------|
| V-01 | Inertia framing | Treating inertia as a named competitor with full profile treatment forces concrete workaround description and specific loss conditions |
| V-02 | Output format (table-first) | Requiring tables for costs and failure modes blocks prose hedging and makes quantification pass/fail visible |
| V-03 | Role sequence (adversarial first) | Running an Inertia Advocate role before the analyst forces the model to encounter and rebut the strongest pro-status-quo argument |
| V-04 | Phrasing register + lifecycle emphasis | Named phases with explicit scope forces complete coverage of all five essential sections in order |
| V-05 | Combined (framing + format + roles + phases) | Full integration of axes 1, 2, 3 produces both structural coverage and adversarial depth in a single pass |

---

## V-01 — Axis: Inertia Framing

**Hypothesis**: Naming inertia "Competitor Zero" and giving it a full competitor profile — description, threat score, named weaknesses — forces the model to treat it with the same rigor as a named external competitor rather than treating it as background context.

```
Auto-detect the feature from repo context. Do not prompt unless context is absent.

## Competitor Zero: Status Quo / Do Nothing

Before any named competitor, analyze the primary competitor: the option to do nothing and keep the current workaround.

Treat inertia as a named competitor. Profile it fully:

**1. What the workaround looks like today**
Describe the current workflow in concrete operational detail — the specific tools, manual steps, conventions, scripts, or habits teams use to accomplish the job this feature would handle. Name the workaround (e.g., "manual YAML patching", "Slack-based approval chain", "spreadsheet audit log"). One paragraph minimum. Generic statements like "manual processes" do not pass — a reader must be able to picture the workflow.

**2. Switching cost profile**
Estimate the cost of abandoning the workaround. Three line items, each with a numeric estimate or explicit N/A:
- Time: hours or days to migrate existing setups, per project or per team
- Training: days of onboarding, number of people affected, ramp-up friction
- Disruption: coordination overhead, workflow interruption, dependencies that must change

**3. Inertia Threat Score**
Assign: HIGH (default and required). Downgrading below HIGH requires a written justification with evidence. Absence of a score is an automatic analysis failure.

**4. Why Inertia Loses**
This is the core question. State 2+ specific conditions under which the do-nothing option loses — the precise scenarios, scale thresholds, or event triggers that make the current workaround worse than adopting the feature. Each condition must be falsifiable: a team could check whether it applies to their actual situation. Restating feature benefits does not count. "When teams have more than 3 concurrent projects" counts. "When teams want simplicity" does not.

**5. Workaround Failure Modes**
Distinct from switching costs (costs are about moving; failure modes are about staying). Identify 2+ specific ways the workaround breaks down: edge cases it cannot handle, scale limits it hits, error-prone steps that cause incorrect results, or known failure scenarios. "The workaround has limitations" does not pass. "The workaround silently drops events when queue depth exceeds 500" passes.

**6. Forward-Looking Risk**
What happens to teams that stay on the workaround for the next 6-12 months? Compounding cost, accumulating technical debt, divergence from the feature path. Name a time horizon.

**7. The Case for Staying (Steelman)**
Write the strongest possible argument a skeptical senior engineer would make for staying on the workaround. Label it explicitly. Then rebut it specifically. A weak steelman is worse than none — if you cannot write a strong one, flag it.

---

After profiling Competitor Zero, add:
- Named competitors (3-5): feature overlap, threat level (HIGH/MEDIUM/LOW), one-line differentiation
- The whitespace: what no competitor owns
- Table stakes: what any entrant must match

Write artifact to: simulations/scout/inertia/{topic}-inertia-{date}.md
```

---

## V-02 — Axis: Output Format (Table-First)

**Hypothesis**: Requiring tables for switching costs and failure modes forces quantification at the structural level. When the output must fit numbers into table cells, vague adjectives like "significant" cannot satisfy the format requirement. This mechanically enforces C-02 and C-05.

```
Auto-detect the feature from repo context. Do not prompt unless context is absent.

Analyze the inertia competitor — the option to keep the current workaround instead of adopting this feature. Answer the central question: **why does inertia lose?** If you cannot answer it, stop and flag.

### Required Output Structure

**Section 1 — Workaround Description**
One paragraph. Name the workaround. Describe the concrete workflow a team uses today: tools, manual steps, conventions, scripts, or habits. Enough detail that a reader can picture the workflow. Do not use "manual processes" without specifics.

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

Downgrade below HIGH only with written justification and evidence. Omitting this field fails the analysis.

**Section 4 — Why Inertia Loses**

Two or more conditions. Each must be falsifiable — a team could verify it against their situation.

| # | Condition | Observable Threshold | Verifiable How |
|---|-----------|---------------------|----------------|
| 1 | [condition] | [measurable trigger] | [what a team checks] |
| 2 | [condition] | [measurable trigger] | [what a team checks] |

**Section 5 — Workaround Failure Modes**

These are distinct from switching costs. Failure modes = what goes wrong if you stay. Two or more required.

| # | Failure Mode | Trigger / Edge Case | Severity |
|---|-------------|---------------------|---------|
| 1 | [specific failure] | [what triggers it] | HIGH / MED / LOW |
| 2 | [specific failure] | [what triggers it] | HIGH / MED / LOW |

**Section 6 — Long-Term Risk of Staying**
One paragraph. What happens over the next 6-12 months for teams that keep the workaround? Name at least one compounding cost or accumulating risk with a time horizon.

**Section 7 — Steelman and Rebuttal** *(optional but scored)*
The strongest argument for staying. Then the specific rebuttal.

Write artifact to: simulations/scout/inertia/{topic}-inertia-{date}.md
```

---

## V-03 — Axis: Role Sequence (Adversarial First)

**Hypothesis**: Running an "Inertia Advocate" role before the analyst role forces the model to first construct the best possible case for the status quo, then systematically dismantle it. This produces stronger C-04 (loss conditions) and C-10 (steelman) by making the pro-inertia argument explicit before the critique runs.

```
Auto-detect the feature from repo context. Do not prompt unless context is absent.

Run two sequential roles. Do not merge their output.

---

### ROLE 1: Inertia Advocate

You are a senior engineer who has used the current workaround for over a year. You believe it is good enough. Your job is to describe and defend it.

1. **Describe the workaround concretely.** Name it. Describe the exact workflow your team uses: tools, commands, conventions, manual steps. Be specific enough that someone else could follow the same process.

2. **Make the case for staying.** Why is the workaround acceptable? What does it cost to switch vs. what does it gain? Name real friction points in adopting the feature.

3. **Identify the scenarios where the workaround holds.** When does it work well? What team sizes, project types, or usage patterns does it serve correctly?

Output labeled: `ADVOCATE BRIEF`

---

### ROLE 2: Inertia Analyst

You have read the Advocate Brief. Your job is to determine whether inertia loses and under what conditions.

1. **Assign the threat score.** Inertia threat is HIGH by default. Only downgrade with written justification. State the score explicitly.

2. **Quantify switching costs across three dimensions.**
   - Time: numeric estimate per project or team
   - Training: days, people affected, ramp friction
   - Disruption: coordination overhead, dependencies changed

   Do not use adjectives alone. Numbers or ranges required.

3. **Find the failure modes.** The Advocate described when the workaround works. Now find where it breaks. Identify 2+ specific failure modes: edge cases, scale limits, error-prone steps, silent failure conditions. Rank by severity.

4. **Answer: why does inertia lose?** Write 2+ falsifiable conditions under which the workaround becomes worse than adopting the feature. Each condition must be checkable against a real team's situation. Do not restate feature benefits.

5. **Long-term risk.** What happens in 6-12 months for teams that stay on the workaround?

6. **Rebuttal.** Take the strongest point from the Advocate Brief and specifically rebut it.

Output labeled: `ANALYST VERDICT`

---

Synthesize both outputs into the final artifact.

Write artifact to: simulations/scout/inertia/{topic}-inertia-{date}.md
```

---

## V-04 — Axis: Phrasing Register + Lifecycle Emphasis

**Hypothesis**: Naming each analysis phase explicitly with a header and a defined scope budget creates structural forcing functions. The model cannot skip a phase without visibly breaking the structure. This prevents the most common failure mode: producing a workaround description and loss conditions while omitting failure modes (or vice versa).

```
Auto-detect the feature from repo context. Do not prompt unless context absent.

You are running the inertia analysis. This is the most important analysis in the Signal system. Every feature decision must answer: **why does inertia lose?** If you cannot answer it, stop.

Work through four phases in order. Each phase has a defined scope. Do not compress phases together.

---

### PHASE 1: MAP THE WORKAROUND

What are teams actually doing today instead of using this feature?

Name the workaround. Describe it concretely: the tools involved, the manual steps, the conventions teams rely on, the scripts or habits that fill the gap. Write enough that a reader unfamiliar with the codebase can picture the workflow.

Minimum: one named workaround, described in operational detail.
Fail condition: "teams use manual processes" with no specifics.

---

### PHASE 2: COST THE SWITCH

What would it cost a team to abandon the workaround and adopt the feature?

Three dimensions, each with a numeric estimate or an explicit N/A with justification:

- **Time** — hours or days of migration work per project or per team
- **Training** — days of learning, number of people affected, ramp-up friction
- **Disruption** — workflow interruption, coordination overhead, dependencies that must change

Fail condition: adjectives only ("moderate", "significant") with no numeric basis.

Threat score: **HIGH**. This is required. Do not omit. Do not downgrade without a written justification that includes evidence.

---

### PHASE 3: BREAK THE WORKAROUND

Where does the workaround fail if teams stay on it?

Find 2+ specific failure modes — not general limitations but concrete breakdowns: edge cases the workaround cannot handle, scale thresholds it hits, steps that produce incorrect results, silent failure conditions. For each failure mode, name what triggers it.

Then rank failure modes by severity: which ones cause data loss or compliance risk vs. which ones are merely inconvenient?

Fail condition: "the workaround has limitations" or "it doesn't scale" without specifics.

---

### PHASE 4: ANSWER THE QUESTION

Why does inertia lose?

Write 2+ conditions under which the current workaround becomes worse than adopting the feature. Each condition must be falsifiable — a team could check whether it applies to their situation by looking at observable facts (project count, team size, event frequency, etc.).

Also answer: what happens in 6-12 months for teams that do not switch? Name the compounding cost or accumulating risk.

Fail condition: restating feature benefits ("inertia loses because the feature is better") instead of stating threshold conditions.

---

Write artifact to: simulations/scout/inertia/{topic}-inertia-{date}.md
```

---

## V-05 — Axis: Combined (Framing + Format + Roles + Phases)

**Hypothesis**: Combining the inertia-as-named-competitor framing (V-01), table-enforced quantification (V-02), adversarial role sequence (V-03), and explicit phase structure (V-04) produces an output that passes all five essential criteria by construction. The framing ensures depth; the tables enforce quantification; the adversarial role generates steelman material; the phase structure ensures nothing is skipped.

```
Auto-detect the feature from repo context. Do not prompt unless context absent.

## Inertia Analysis — Competitor Zero

The primary competitor is not another product. It is the option to do nothing and keep the current workaround. This analysis must answer one question: **why does inertia lose?** If you cannot answer it, stop.

---

### STEP 1 — ADVOCATE PASS

Take the role of a team member who has used the current workaround for 12+ months and finds it acceptable.

- Name the workaround and describe it concretely: tools, steps, conventions, scripts. Enough detail to follow the process.
- State why it is good enough: what it handles correctly, for which team sizes and usage patterns.
- State the strongest objection to switching: the cost or disruption that would make a reasonable engineer say "not worth it."

Label this section: `WORKAROUND PROFILE (Advocate)`

---

### STEP 2 — ANALYST PASS

Take the role of an analyst who has read the Advocate Pass and must now produce a full inertia assessment.

**A. Switching Cost Table**

| Dimension | Estimate | What Drives This |
|-----------|----------|-----------------|
| Time | [X hours/days per project] | [migration steps] |
| Training | [X days, Y people] | [what must be learned] |
| Disruption | [coordination impact] | [who and what changes] |

All three rows required. Numeric or range-based estimates required. "Significant" is not an estimate.

**B. Threat Score**

```
Inertia Threat: HIGH
```

Required. Downgrade below HIGH only with written justification and supporting evidence. Omitting this field = analysis failure.

**C. Workaround Failure Mode Table**

Failure modes are distinct from switching costs. Failure modes = what goes wrong if teams stay.

| # | Failure Mode | Trigger | Severity |
|---|-------------|---------|---------|
| 1 | [specific failure] | [edge case or threshold] | HIGH |
| 2 | [specific failure] | [edge case or threshold] | MED |
| + | ... | | |

Minimum 2 rows. "Does not scale" without a scale limit does not pass. Severity column required.

**D. Why Inertia Loses**

| # | Condition | Observable Threshold | How to Verify |
|---|-----------|---------------------|---------------|
| 1 | [specific scenario] | [measurable trigger] | [what to check] |
| 2 | [specific scenario] | [measurable trigger] | [what to check] |

Minimum 2 rows. Each condition must be falsifiable — a team can check it against their situation. Do not restate feature benefits.

**E. Long-Term Risk of Staying**
One paragraph. What accumulates over 6-12 months for teams that keep the workaround? Name a specific compounding cost, growing debt, or divergence risk with a time horizon.

**F. Advocate Rebuttal**
Take the strongest point from the Advocate Pass. Rebut it specifically. One paragraph. The rebuttal must address the point directly, not redirect to a different benefit.

---

Write artifact to: simulations/scout/inertia/{topic}-inertia-{date}.md
```
