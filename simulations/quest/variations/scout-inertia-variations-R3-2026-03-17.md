Written to `simulations/quest/variations/scout-inertia-variations-R3-2026-03-17.md`.

---

## scout-inertia — Prompt Variations R3

### Variation Map

| ID | Axis | Target | Predicted Score |
|----|------|--------|----------------|
| V-01 | Prose-level `Trigger:` / `Impact:` bullet format (R2 V-01 base) | C-15 | ~97 |
| V-02 | Impact column added to failure mode table (R2 V-02 base) | C-15 | ~96 |
| V-03 | Required section heading list in synthesis output (R2 V-03 base) | C-14 | ~96 |
| V-04 | Impact column + section label compliance note in phase structure | C-14 + C-15 | ~99 |
| V-05 | R2 V-05 scaffold + Impact column + section label reinforcement | C-14 + C-15 | **100** |

---

### Design rationale

**R2 V-05 on rubric v3 needs one change.** It already satisfies C-14 (Sections A-F in STEP 2 are descriptive; heading-scan finds all components). The only failing criterion is C-15: Section C's failure mode table has `Trigger` as a column but merges the failure name and its effect into the `Failure Mode` cell. Adding a dedicated `Impact` column closes that gap.

**Two C-15 mechanisms are tested.** V-01 uses a prose-level labeled bullet format (`Trigger:` / `Impact:` / `Severity:` per entry). V-02 uses a table column split. The column approach (V-02) makes non-compliance visibly malformed — a blank Impact cell is structurally obvious. The prose approach (V-01) admits partial compliance. The predicted scores are similar, but the reliability of the enforcement differs; that difference is the signal.

**C-14 isolation in V-03.** R2 V-03's synthesis step leaves heading structure undefined — the model may produce role labels or continuous prose. The single change is a required heading list prescribing 7 descriptive section names for the synthesized artifact. C-15 is intentionally not targeted (keeping the axis clean).

**V-04 carries both mechanisms in the phase structure.** Phase 3 gains the Impact column; a section label compliance note formalizes C-14. C-13 (replication fidelity) remains absent from V-04's base — hence the ~99 prediction rather than 100.

**V-05 converges.** R2 needed three new mechanisms for 100/100 on v2. R3 needs one. The delta narrowing each round is the expected shape of a converging quest.
gger cell. Prose-level enforcement (V-01)
depends on format-matching within a sentence block. This distinction is the signal:
which compliance mechanism produces more reliable C-15 behavior?

**V-03 is strict single-axis for C-14.** R2 V-03's two-role adversarial structure
produces role labels (ADVOCATE BRIEF, ANALYST VERDICT) and numbered step labels
as instructions -- but the synthesized output heading structure is undefined. The model
may produce role-based headings, analytical headings, or continuous prose. V-03 adds
an explicit required heading list to the synthesis step, converting an emergent
property into a structural requirement. The adversarial role machinery and anchored
rebuttal sequence are unchanged.

**V-04 combines both new criteria inside the phase structure** (R2 V-04 base). The
phase structure already satisfies C-14 informally (Phase 1-4 with sub-parts A/B/C are
descriptive); V-04 formalizes it with a section label compliance note. V-04 also adds
an Impact column to the Phase 3 failure mode table. Both changes slot into the existing
scaffold without restructuring.

**V-05 is R2 V-05 with the minimum changes for rubric v3 coverage.** The two-pass
advocate/analyst scaffold with Replication Fidelity Standard, Verification Command
column, and anchored rebuttal sequence is preserved exactly. The single failing
criterion on v3 (C-15) is fixed by adding an Impact column to Section C. An explicit
section label compliance note is added to reinforce C-14, which the existing A-F
section structure already satisfies structurally.

**Key principle preserved from R2:** format constraints eliminate structural loopholes
better than instructions alone. Both C-15 mechanisms (V-01 format, V-02 column) and
the C-14 mechanism (V-03 heading list) follow this principle -- each converts a
named requirement into a pattern that is visibly malformed when violated.

---

## V-01 -- Axis: Prose-Level Trigger/Impact Format Constraint (C-15 target)

**Hypothesis**: Adding a labeled bullet format (Trigger: / Impact: / Severity:) to the
failure modes section -- without introducing a new table -- forces C-15 by making
trigger and impact appear as separate named statements. A failure mode reading "silently
drops events under load" fails the label check on inspection. This is R2 V-01 with
exactly one change: the failure modes section instruction. All other sections are
unchanged from R2 V-01.

```
Auto-detect the feature from repo context. Do not prompt unless context is absent.

## Competitor Zero: Status Quo / Do Nothing

Before any named competitor, analyze the primary competitor: the option to do nothing
and keep the current workaround.

Treat inertia as a named competitor. Profile it fully:

**1. What the workaround looks like today -- Replication Fidelity Standard**

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
  team member would not have -- undocumented conventions, tribal context, shared
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

Distinct from switching costs. Failure modes = what goes wrong if you stay.
Identify 2+ specific ways the workaround breaks down.

For each failure mode, record trigger and impact as separate labeled statements.
Do not merge them into one sentence.

Required format per failure mode:
- **Trigger**: [the observable event or threshold that causes the failure -- must be
  detectable by the team]
- **Impact**: [what happens when the trigger fires, and to whom -- must name an effect
  and an affected party]
- **Severity**: HIGH (data loss or compliance risk) / MED (incorrect results) / LOW
  (inefficiency only)

Examples that pass:
- Trigger: Queue depth exceeds 500 messages. Impact: Events are silently dropped with
  no error surfaced to the caller; data inconsistency accumulates until manually
  audited. Severity: HIGH.
- Trigger: New team member runs the deployment Makefile target without prior
  onboarding. Impact: The undocumented environment variable is absent; the
  misconfiguration ships to production silently. Severity: HIGH.

Examples that fail:
- "Silently drops events under load" -- trigger and impact merged; neither named
  specifically.
- "Causes data issues when team grows" -- trigger too vague; impact too vague.
- "The workaround has limitations at scale" -- neither trigger nor impact present.

Fail condition: Trigger or Impact label absent from any entry; both merged into one
undifferentiated sentence.

**6. Forward-Looking Risk**

What happens to teams that stay on the workaround for the next 6-12 months? Name a
specific compounding cost, accumulating debt, or divergence risk with a time horizon.

**7. The Case for Staying (Steelman)**

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

## V-02 -- Axis: Impact Column in Failure Mode Table (C-15 target)

**Hypothesis**: Adding a dedicated "Impact" column to the existing failure mode table --
separate from the "Failure Mode" name column and the existing "Trigger" column -- forces
C-15 by structural constraint. A model filling four columns (Failure Mode / Trigger /
Impact / Severity) cannot merge trigger and impact without leaving the Impact cell blank,
which is visibly malformed. This is R2 V-02 with exactly one change: the failure mode
table structure and its column constraints. All other sections unchanged.

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

Two or more conditions. Each must be falsifiable -- a team could verify it against
their situation.

| # | Condition | Observable Threshold | Verification Command |
|---|-----------|---------------------|---------------------|
| 1 | [condition] | [measurable trigger] | [see format below] |
| 2 | [condition] | [measurable trigger] | [see format below] |

**Verification Command format**: `[Tool or artifact]: [what you open or run] ->
[what the result looks like when the threshold applies]`

Examples that pass:
- "Jira: open the active sprint board -> count rows where Status = Active. If >= 4,
  condition applies."
- "GitHub: run `gh pr list --state open | wc -l` -> if output >= 10, threshold met."

Examples that fail:
- "You can check project count"
- "Review your sprint board"
- "Look at the metrics dashboard"

The Verification Command must name a specific tool and specify a concrete action.
A reader must be able to follow it without asking a follow-up question.

**Section 5 -- Workaround Failure Modes**

Distinct from switching costs. Failure modes = what goes wrong if you stay.
Minimum 2 rows required.

| # | Failure Mode | Trigger | Impact | Severity |
|---|-------------|---------|--------|---------|
| 1 | [short name] | [observable event or threshold] | [what happens to whom] | HIGH / MED / LOW |
| 2 | [short name] | [observable event or threshold] | [what happens to whom] | HIGH / MED / LOW |

Column constraints:
- **Failure Mode**: a short label for the failure (e.g., "silent event drop", "audit
  gap"). Not a full description -- that goes in Impact.
- **Trigger**: the observable condition that causes the failure. Must be detectable.
  "Breaks under load" does not pass. "Queue depth exceeds 500 messages" does pass.
- **Impact**: what happens when the trigger fires, and to whom. "Fails" does not pass.
  "Events silently dropped; caller receives no error; data inconsistency accumulates
  until manually audited" does pass. The Impact column must stand alone -- interpretable
  without reading the Trigger column.
- **Severity**: HIGH (data loss, compliance risk), MED (incorrect results), LOW
  (inefficiency only).

Fail condition: Trigger and Impact merged into one cell. A blank Impact cell is an
automatic fail for that row.

**Section 6 -- Long-Term Risk of Staying**

One paragraph. What happens over the next 6-12 months for teams that keep the
workaround? Name at least one compounding cost or accumulating risk with a
time horizon.

**Section 7 -- Steelman and Rebuttal** *(optional but scored)*

The strongest argument for staying. Then the specific rebuttal.

Write artifact to: simulations/scout/inertia/{topic}-inertia-{date}.md
```

---

## V-03 -- Axis: Required Section Heading List in Synthesis Output (C-14 target)

**Hypothesis**: R2 V-03's two-role adversarial structure produces role labels
(ADVOCATE BRIEF, ANALYST VERDICT) and numbered step labels as instructions -- but the
synthesized artifact heading structure is undefined. Without explicit heading requirements,
the model may produce role-based headings, continuous prose, or an inconsistent mix.
Adding a required heading list to the synthesis step forces C-14 by making the expected
analytical section names explicit and enforceable by label-scan. The adversarial role
machinery, STRONGEST CLAIM labeling, and anchored rebuttal sequence are unchanged --
exactly one structural element is added to the synthesis step.

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

3. **Find the failure modes.** Identify 2+ specific failure modes: edge cases,
   scale limits, error-prone steps, silent failure conditions. Rank by severity.

4. **Answer: why does inertia lose?** Write 2+ falsifiable conditions under which
   the workaround becomes worse than adopting the feature. Each condition must be
   checkable against a real team's situation. Do not restate feature benefits.

5. **Long-term risk.** What happens in 6-12 months for teams that stay on the
   workaround?

6. **Anchored Rebuttal.** Follow this sequence exactly -- do not compress steps:
   a. Copy the STRONGEST CLAIM from the Advocate Brief word-for-word.
      Label it: `NAMED CLAIM: "[exact text from Advocate Brief]"`
   b. Rebut only that claim. Write one paragraph that addresses specifically why
      that claim fails -- with evidence or reasoning tied to the claim's content.
   c. Constraint: do not address a weaker point instead. Do not pivot to feature
      benefits unrelated to the named claim. The rebuttal must be traceable to
      the named claim.

Output labeled: `ANALYST VERDICT`

---

### Synthesis -- Required Section Headings

Synthesize the Advocate Brief and Analyst Verdict into the final artifact.

The synthesized artifact **must use these exact section headings, in this order**:

1. `## Workaround Description`
2. `## Switching Costs`
3. `## Inertia Threat Score`
4. `## Failure Modes`
5. `## Why Inertia Loses`
6. `## Long-Term Risk`
7. `## Steelman and Rebuttal`

Each heading must be present even if the content under it is brief. Do not rename,
merge, or omit any heading. A reader scanning only the headings must be able to
identify every analytical component without reading prose.

Fail condition: role labels ("The Advocate argued...", "The Analyst concluded...")
appearing as section headings instead of the analytical labels above; prose summary
replacing named sections; any two adjacent components merged under one heading.

Write artifact to: simulations/scout/inertia/{topic}-inertia-{date}.md
```

---

## V-04 -- Combined: Impact Column + Section Label Compliance in Phase Structure (C-14 + C-15)

**Hypothesis**: R2 V-04's phase structure already satisfies C-14 informally (Phase 1-4
with sub-parts A/B/C are descriptive labels). Adding (1) a dedicated Impact column to
Phase 3's failure mode table and (2) an explicit section label compliance note at the
end delivers simultaneous C-14 and C-15 coverage within the existing scaffold. The
Verification Command column and anchored rebuttal sequence from R2 V-04 are preserved
unchanged. Both additions slot into the existing phase structure without restructuring.

```
Auto-detect the feature from repo context. Do not prompt unless context absent.

You are running the inertia analysis. This is the most important analysis in the
Signal system. Every feature decision must answer: **why does inertia lose?**
If you cannot answer it, stop.

Work through four phases in order. Each phase has a defined scope and a required
section heading. Do not compress phases together. Do not rename phase headings.

---

### PHASE 1: WORKAROUND DESCRIPTION

What are teams actually doing today instead of using this feature?

Name the workaround. Describe it concretely: the tools involved, the manual steps,
the conventions teams rely on, the scripts or habits that fill the gap. Write enough
that a reader unfamiliar with the codebase can picture the workflow.

Minimum: one named workaround, described in operational detail.
Fail condition: "teams use manual processes" with no specifics.

---

### PHASE 2: SWITCHING COSTS AND THREAT SCORE

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

### PHASE 3: FAILURE MODES

Where does the workaround fail if teams stay on it?

Find 2+ specific failure modes. For each mode, record the trigger (what causes it)
and the impact (what happens to whom) as separate columns -- do not merge them.

| # | Failure Mode | Trigger | Impact | Severity |
|---|-------------|---------|--------|---------|
| 1 | [short name] | [observable event or threshold] | [what happens to whom] | HIGH / MED / LOW |
| 2 | [short name] | [observable event or threshold] | [what happens to whom] | HIGH / MED / LOW |

Column constraints:
- **Trigger**: the observable condition that causes the failure. Must be detectable
  by the team. "Breaks under load" does not pass. "Queue depth exceeds 500 messages"
  does pass.
- **Impact**: what happens when the trigger fires, and to whom. "Fails" does not pass.
  "Events silently dropped; caller receives no error; data inconsistency accumulates"
  does pass. The Impact column must be interpretable without reading the Trigger.
- Trigger and Impact are separate columns. A blank Impact cell is a fail for that row.

Rank failure modes by severity: HIGH (data loss, compliance risk), MED (incorrect
results), LOW (inefficiency).

Fail condition for Trigger: vague scale mentions without a named threshold.
Fail condition for Impact: "fails" or "causes problems" without naming what and to whom.

---

### PHASE 4: WHY INERTIA LOSES

**Part A -- Loss Conditions**

| # | Condition | Observable Threshold | Verification Command |
|---|-----------|---------------------|---------------------|
| 1 | [scenario] | [measurable trigger] | [Tool: Action -> Result when threshold applies] |
| 2 | [scenario] | [measurable trigger] | [Tool: Action -> Result when threshold applies] |

Verification Command format: `[Tool or artifact]: [what you open or run] -> [what
the result looks like when the threshold applies]`

Fail condition for this column: "you can check project count", "review your sprint
board", or any description without a named tool and concrete action.

**Part B -- Steelman and Anchored Rebuttal**

Follow three steps in sequence -- do not merge them:

1. Write the strongest argument a skeptical senior engineer would make for staying
   on the workaround. Label it: **STEELMAN**

2. Extract the single strongest specific claim from your steelman. Write it as a
   complete declarative sentence. Label it: **NAMED CLAIM: "[exact text]"**

3. Rebut only that named claim. One paragraph. Address specifically why that claim
   fails. Do not pivot to feature benefits unrelated to the claim. Do not address
   a weaker point instead.

**Part C -- Long-Term Accumulation**

What accumulates over 6-12 months for teams that stay? Name a specific compounding
cost or divergence risk with a time horizon.

---

Section heading compliance: the artifact must use the phase headings above
(PHASE 1: WORKAROUND DESCRIPTION, PHASE 2: SWITCHING COSTS AND THREAT SCORE,
PHASE 3: FAILURE MODES, PHASE 4: WHY INERTIA LOSES) as top-level headings in the
output. A reader scanning only the headings must be able to locate each analytical
component. Merging PHASE 3 and PHASE 4 under one heading is a fail condition.

Write artifact to: simulations/scout/inertia/{topic}-inertia-{date}.md
```

---

## V-05 -- Full Combined: R2 V-05 Scaffold + C-14 + C-15

**Hypothesis**: R2 V-05 scored 100/100 on rubric v2 by integrating Replication Fidelity
Standard (C-13), Verification Command column (C-11), and NAMED CLAIM copy-before-rebut
(C-12) into the two-pass advocate/analyst scaffold. On rubric v3, it likely passes C-14
already (Sections A-F in STEP 2 are descriptive) and fails C-15 (Section C's failure
mode table has a Trigger column but no Impact column, leaving impact implicit in the
Failure Mode cell). Adding a dedicated Impact column to Section C, plus a section label
compliance note to reinforce C-14, produces simultaneous passes on all 15 rubric criteria
without restructuring the scaffold that scored 100/100.

```
Auto-detect the feature from repo context. Do not prompt unless context absent.

## Inertia Analysis -- Competitor Zero

The primary competitor is not another product. It is the option to do nothing and
keep the current workaround. This analysis must answer one question: **why does
inertia lose?** If you cannot answer it, stop.

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

The following sections must appear with these exact headings in the final artifact.
A reader scanning only the headings must be able to locate every analytical component
without reading prose. Do not rename, merge, or omit any section heading.

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

**C. Failure Mode Table**

Failure modes are distinct from switching costs. Failure modes = what goes wrong
if teams stay.

| # | Failure Mode | Trigger | Impact | Severity |
|---|-------------|---------|--------|---------|
| 1 | [short name] | [observable event or threshold] | [what happens to whom] | HIGH |
| 2 | [short name] | [observable event or threshold] | [what happens to whom] | MED |
| + | ... | | | |

Minimum 2 rows. Column constraints:
- **Failure Mode**: a short label for the failure (e.g., "silent event drop", "audit
  gap"). Not a full description -- the effect belongs in Impact.
- **Trigger**: the observable event or condition that causes the failure. Must be
  detectable by the team. "Breaks under load" does not pass. "Queue depth exceeds
  500 messages" does pass.
- **Impact**: what happens when the trigger fires, and to whom. "Fails" does not
  pass. "Events silently dropped with no error surfaced to caller; data
  inconsistency accumulates until manually discovered" does pass. The Impact
  column must be interpretable without reading the Trigger column.
- Trigger and Impact are separate columns. Do not merge them. A blank Impact cell
  is an automatic fail for that row.

Severity column required. HIGH = data loss or compliance risk; MED = incorrect
results; LOW = inefficiency only.

**D. Why Inertia Loses**

| # | Condition | Observable Threshold | Verification Command |
|---|-----------|---------------------|---------------------|
| 1 | [specific scenario] | [measurable trigger] | [see format] |
| 2 | [specific scenario] | [measurable trigger] | [see format] |

Minimum 2 rows. Each condition must be falsifiable -- a team can check it against
their actual situation.

**Verification Command format**: `[Tool or artifact]: [what you open or run] ->
[what the result looks like when the threshold applies]`

Examples that pass:
- "Jira: open the active sprint board -> count rows where Status = Active.
  If >= 4, condition applies."
- "GitHub: run `gh pr list --state open | wc -l` -> if output >= 10, threshold met."

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

## Predicted R3 Scores (rubric v3)

Rubric v3 scoring: `(essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/7 * 10)`

Aspirational criteria (7): C-09, C-10, C-11, C-12, C-13, C-14, C-15.

### V-01 Prediction

Base is R2 V-01: scored 96/100 on v2 (C-11 FAIL, C-12 FAIL, C-13 PASS). V-01 adds
C-15 mechanism only.

| ID | Criterion | Predicted | Evidence |
|----|-----------|-----------|---------|
| C-09 | Severity ranked | PASS | Section 5: Severity: HIGH/MED/LOW per entry |
| C-10 | Steelman rebutted | PASS | Section 7: labeled steelman + specific rebuttal |
| C-11 | Verification method | FAIL | No Verification Command column; unchanged from R2 V-01 |
| C-12 | Anchored rebuttal | FAIL | No STRONGEST CLAIM / NAMED CLAIM mechanism |
| C-13 | Replication fidelity | PASS | Replication Fidelity Standard intact from R2 V-01 |
| C-14 | Labeled sections | PASS | Sections 1-7 with descriptive titles; heading-scan reveals all components |
| C-15 | Trigger/Impact decomposed | PASS | Labeled bullet format Trigger: / Impact: per entry; merge fails label check |

Aspirational: 5/7 * 10 = 7.14
**Predicted score**: 60 + 30 + 7.14 = **97**

---

### V-02 Prediction

Base is R2 V-02: scored 95/100 on v2 (C-10 PARTIAL, C-12 FAIL, C-13 FAIL). V-02 adds
Impact column only.

| ID | Criterion | Predicted | Evidence |
|----|-----------|-----------|---------|
| C-09 | Severity ranked | PASS | Severity column in failure mode table |
| C-10 | Steelman rebutted | PARTIAL | Section 7 "(optional but scored)" -- structural unreliability preserved from R2 V-02 |
| C-11 | Verification method | PASS | Verification Command column with format and examples; unchanged |
| C-12 | Anchored rebuttal | FAIL | No STRONGEST CLAIM / NAMED CLAIM mechanism |
| C-13 | Replication fidelity | FAIL | Workaround at "reader can picture" level; unchanged from R2 V-02 |
| C-14 | Labeled sections | PASS | Section 1-7 headings are descriptive; heading-scan reveals all components |
| C-15 | Trigger/Impact decomposed | PASS | Dedicated Impact column; blank Impact cell is visibly malformed |

Aspirational: (1 + 0.5 + 1 + 0 + 0 + 1 + 1) = 4.5/7 * 10 = 6.43
**Predicted score**: 60 + 30 + 6.43 = **96**

---

### V-03 Prediction

Base is R2 V-03: scored 97/100 on v2 (C-11 FAIL, C-13 PARTIAL). V-03 adds required
heading list only.

| ID | Criterion | Predicted | Evidence |
|----|-----------|-----------|---------|
| C-09 | Severity ranked | PASS | Role 2 Step 3: "Rank by severity" with HIGH/MED/LOW |
| C-10 | Steelman rebutted | PASS | Full adversarial sequence; Role 1 writes advocate case independently |
| C-11 | Verification method | FAIL | No Verification Command column; unchanged from R2 V-03 |
| C-12 | Anchored rebuttal | PASS | STRONGEST CLAIM in Role 1 -> NAMED CLAIM verbatim copy in Role 2 |
| C-13 | Replication fidelity | PARTIAL | "specific enough that someone else could follow" -- step enumeration implied but institutional knowledge flagging not explicit |
| C-14 | Labeled sections | PASS | Required heading list mandates 7 descriptive headings; fail condition defined |
| C-15 | Trigger/Impact decomposed | FAIL | Role 2 Step 3 identifies trigger but Impact not structurally separated |

Aspirational: (1 + 1 + 0 + 1 + 0.5 + 1 + 0) = 4.5/7 * 10 = 6.43
**Predicted score**: 60 + 30 + 6.43 = **96**

---

### V-04 Prediction

Base is R2 V-04: scored 98/100 on v2 (C-13 FAIL). V-04 adds Impact column + section
label note.

| ID | Criterion | Predicted | Evidence |
|----|-----------|-----------|---------|
| C-09 | Severity ranked | PASS | Phase 3: "Rank failure modes by severity: HIGH / MED / LOW" |
| C-10 | Steelman rebutted | PASS | Phase 4 Part B: STEELMAN -> NAMED CLAIM -> anchored rebuttal |
| C-11 | Verification method | PASS | Phase 4 Part A: Verification Command column with format and fail conditions |
| C-12 | Anchored rebuttal | PASS | Three-step STEELMAN -> NAMED CLAIM: "[exact text]" -> rebuttal-of-named-claim |
| C-13 | Replication fidelity | FAIL | Phase 1 stays at "reader can picture" level; no Replication Fidelity Standard |
| C-14 | Labeled sections | PASS | Phase headings enforced by section label compliance note at end of prompt |
| C-15 | Trigger/Impact decomposed | PASS | Phase 3 Impact column; column constraints with pass/fail examples |

Aspirational: (1 + 1 + 1 + 1 + 0 + 1 + 1) = 6/7 * 10 = 8.57
**Predicted score**: 60 + 30 + 8.57 = **99**

---

### V-05 Prediction

Base is R2 V-05: scored 100/100 on v2. V-05 adds Impact column to Section C + section
label compliance note.

| ID | Criterion | Predicted | Evidence |
|----|-----------|-----------|---------|
| C-09 | Severity ranked | PASS | Section C severity column; unchanged from R2 V-05 |
| C-10 | Steelman rebutted | PASS | Two-pass structure; Section F anchored rebuttal; unchanged |
| C-11 | Verification method | PASS | Section D Verification Command column; unchanged |
| C-12 | Anchored rebuttal | PASS | STRONGEST CLAIM -> NAMED CLAIM verbatim copy -> traceable rebuttal; unchanged |
| C-13 | Replication fidelity | PASS | Replication Fidelity Standard in STEP 1; unchanged |
| C-14 | Labeled sections | PASS | Sections A-F descriptive + compliance note: "do not rename, merge, or omit any section heading" |
| C-15 | Trigger/Impact decomposed | PASS | Section C Impact column; "blank Impact cell = automatic fail for that row" |

Aspirational: 7/7 * 10 = 10
**Predicted score**: 60 + 30 + 10 = **100**

---

## Variation Rankings

| Rank | Variation | Predicted Score | Band | C-14 | C-15 | Key gap vs 100 |
|------|-----------|----------------|------|------|------|----------------|
| 1 | V-05 | 100 | Gold | PASS | PASS | none |
| 2 | V-04 | ~99 | Gold | PASS | PASS | C-13 (replication fidelity) |
| 3 | V-01 | ~97 | Gold | PASS | PASS | C-11, C-12 |
| 4 | V-02 | ~96 | Gold | PASS | PASS | C-10 partial, C-12, C-13 |
| 4 | V-03 | ~96 | Gold | PASS | FAIL | C-11, C-15 |

All five variations predict all essential criteria pass. All predict Gold band.

---

## Excellence Signals from R3 Design

**Signal 1 -- Column-level split is more structurally reliable than prose-level format constraint**

V-01 (Trigger: / Impact: bullet labels) and V-02 (Trigger | Impact columns) both target
C-15. Column-level enforcement (V-02) makes non-compliance visibly malformed: a blank
Impact cell in a required column is an obvious structural defect. Prose-level enforcement
(V-01) admits partially compliant entries ("Trigger: high load. Impact: causes problems")
that pass the label check but fail the depth check. The mechanism difference does not
change the predicted C-15 pass/fail outcome here -- both should pass -- but it changes
the reliability of that pass under adversarial prompting. Column-level > prose-level for
structural enforcement is the generalizable principle.

**Signal 2 -- Section label mandate is a synthesis constraint, independent of role structure**

V-03 shows that C-14 can be enforced by prescribing analytical headings for the synthesis
output, decoupled from the roles that generate the content. The roles run independently;
the heading mandate applies only to the artifact. This means C-14 can be added to any
role-based prompt as a synthesis step without modifying the roles themselves.

**Signal 3 -- V-05 is one column from 100/100 on v3**

R2 V-05 needed three targeted mechanisms to reach 100/100 on rubric v2 (C-11, C-12,
C-13 all required new machinery). R3 V-05 needs one (Impact column for C-15; C-14 is
already satisfied by the existing A-F section structure). The delta narrows each round.
This is the expected shape of a converging quest: the gap between the current best and
100/100 on the updated rubric should shrink as the scaffold matures.

---

```json
{"top_score_predicted": 100, "all_essential_pass": true, "new_patterns": ["Column-level decomposition (separate Impact column) is structurally more reliable than prose-level format constraint for C-15 -- blank column cell is visibly malformed; partially-compliant prose entry is not", "Section label mandate is a synthesis constraint independent of role structure -- C-14 enforcement can be added to any adversarial role prompt without modifying roles, only the synthesis step", "V-05 is one column from 100/100 on v3 confirming scaffold maturity -- R2 three-mechanism delta reduced to R3 one-mechanism delta as expected in a converging quest"]}
```
