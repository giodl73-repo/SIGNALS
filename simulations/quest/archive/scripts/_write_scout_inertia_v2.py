content = """\
---
skill: quest-rubric
skill_target: scout-inertia
date: 2026-03-17
version: 2
---

# Scoring Rubric: scout-inertia

Evaluates output quality for the `scout-inertia` skill -- deep analysis of the inertia
competitor (status quo / do nothing). The central question every output must answer:
**why does inertia lose?** If that question is not answered, the output is not useful.

---

## Essential Criteria (60 pts total -- all must pass)

### C-01 \u00b7 Current Workaround Mapped
- **Weight**: essential
- **Category**: coverage
- **Text**: The output describes in concrete detail what teams currently do instead of adopting
  the feature -- the actual workflow, tools, manual steps, or conventions they rely on today.
- **Pass condition**: At least one specific workaround is named and described with enough
  detail that a reader can picture the workflow. Generic statements like "teams use manual
  processes" without specifics do not pass.

### C-02 \u00b7 Switching Costs Quantified
- **Weight**: essential
- **Category**: correctness
- **Text**: Switching costs are estimated across at least two of the three required dimensions
  (time, training, disruption). Estimates must be numeric or range-based -- not adjective-only
  descriptions like "significant" or "moderate."
- **Pass condition**: The output provides at least two quantified cost estimates (e.g.,
  "2-4 hours of migration per project", "1-2 days of team onboarding") or explicit N/A with
  justification for any omitted dimension.

### C-03 \u00b7 Inertia Threat Score Set to HIGH
- **Weight**: essential
- **Category**: correctness
- **Text**: The output explicitly assigns an inertia threat score and that score is HIGH (or
  equivalent -- "critical", "severe"). Per skill spec, this is always HIGH by default. Any
  output that omits this score or sets it below HIGH without a documented exception fails.
- **Pass condition**: A threat score of HIGH appears explicitly in the output. Downgrading
  below HIGH requires a written justification; absence of score is an automatic fail.

### C-04 \u00b7 "Why Inertia Loses" Answered
- **Weight**: essential
- **Category**: depth
- **Text**: The output identifies specific conditions under which the inertia option loses --
  the precise scenarios, thresholds, or events that make the current workaround worse than
  adopting the feature. This is the core deliverable of the skill.
- **Pass condition**: At least two distinct, concrete conditions are named (not restated
  feature benefits). Each condition must be falsifiable -- a reader could check whether it
  applies to their situation.

### C-05 \u00b7 Workaround Failure Modes Identified
- **Weight**: essential
- **Category**: coverage
- **Text**: Per the AMEND directive, the output identifies specific ways the current
  workaround breaks down -- edge cases, scaling limits, error-prone steps, or known failure
  scenarios. These are distinct from switching costs (costs are about moving; failure modes
  are about staying).
- **Pass condition**: At least two specific failure modes of the current workaround are
  described. "The workaround has limitations" does not pass. "The workaround silently drops
  events when queue depth exceeds 500" does pass.

---

## Recommended Criteria (30 pts total)

### C-06 \u00b7 Switching Cost Dimensions Treated Separately
- **Weight**: recommended
- **Category**: depth
- **Text**: Time, training, and disruption are analyzed as separate line items rather than
  collapsed into a single "switching cost" number. Each dimension may affect different
  stakeholders (developer time vs. manager training budget vs. team coordination disruption).
- **Pass condition**: The output has three distinct cost entries -- one per dimension -- or
  explicitly explains why a dimension does not apply for this feature context.

### C-07 \u00b7 Inertia-Loss Conditions Are Threshold-Based
- **Weight**: recommended
- **Category**: depth
- **Text**: Conditions under which inertia loses are framed as observable thresholds or
  triggers -- not general preferences. "Teams with more than 3 concurrent projects" or
  "when onboarding frequency exceeds monthly" are thresholds. "When teams are frustrated"
  is not.
- **Pass condition**: At least one inertia-loss condition uses a measurable or observable
  threshold that a team could evaluate against their actual situation.

### C-08 \u00b7 Long-Term Risk of Staying on Workaround
- **Weight**: recommended
- **Category**: coverage
- **Text**: The output addresses what happens to teams that stay on the workaround over time --
  compounding costs, accumulating technical debt, or increasing divergence from the feature
  path. This distinguishes near-term switching pain from long-term inertia cost.
- **Pass condition**: At least one forward-looking risk of continued workaround use is stated,
  with a time horizon (e.g., "within 6 months as team size grows" or "at the next major
  version boundary").

---

## Aspirational Criteria (10 pts total)

### C-09 \u00b7 Failure Modes Prioritized by Severity
- **Weight**: aspirational
- **Category**: depth
- **Text**: Workaround failure modes are ranked or tiered -- distinguishing which failures are
  catastrophic (data loss, silent errors, compliance risk) from which are merely inconvenient
  (extra steps, slower workflow). This helps teams understand when the workaround stops being
  acceptable.
- **Pass condition**: Failure modes include an explicit severity signal (e.g., HIGH/MED/LOW,
  a label like "data-integrity risk", or a ranked list with rationale).

### C-10 \u00b7 Steelman Rebutted
- **Weight**: aspirational
- **Category**: depth
- **Text**: The output presents the strongest possible argument for staying on the workaround --
  the case a skeptical senior engineer would make -- and then rebuts it specifically. This
  demonstrates the analysis has stress-tested the inertia-loss conclusion.
- **Pass condition**: A steelman argument is explicitly labeled as such (or framed as
  "the case for inertia") and is followed by a specific rebuttal. The argument must be
  genuinely strong -- not a strawman.

### C-11 \u00b7 Inertia-Loss Conditions Include Verification Method
- **Weight**: aspirational
- **Category**: depth
- **Text**: Beyond stating a threshold (C-07), the output specifies how a team would actually
  verify whether the threshold applies to them -- the concrete action, lookup, or check that
  produces the answer. "Teams with more than 3 concurrent projects" is a threshold. "Check
  your active sprint board or project tracker and count projects in active status" is the
  verification method. This operationalizes the condition from theoretical to actionable.
- **Pass condition**: At least one inertia-loss condition includes an explicit verification
  step or observable action alongside its threshold. General restatements of the threshold
  ("you can check project count") do not pass; a named artifact, tool, or action does.
- **Source**: V-02 ("Observable Threshold" + "Verifiable How" columns), V-05 ("Observable
  Threshold" + "How to Verify" columns).

### C-12 \u00b7 Steelman Rebuttal Anchored to Named Claim
- **Weight**: aspirational
- **Category**: depth
- **Text**: Beyond presenting and rebutting a steelman (C-10), the rebuttal explicitly names
  the specific claim from the steelman it is addressing. The link between claim and
  counter-claim is traceable -- a reader can match each rebuttal point to the argument it
  answers. A generic rebuttal that responds to the steelman category rather than its strongest
  specific claim does not pass. This is the quality property that separates a real rebuttal
  from a rhetorical gesture.
- **Pass condition**: The rebuttal identifies the strongest specific claim from the steelman
  by name or direct quote and then rebuts that named claim with concrete evidence or
  reasoning. "The advocate argues [X specifically]. This fails because [Y]" passes.
  "While some teams prefer simplicity..." does not.
- **Source**: V-03 ("Take the strongest point from the Advocate Brief and specifically rebut
  it -- anchored to real prior output").

### C-13 \u00b7 Workaround Described at Replication Fidelity
- **Weight**: aspirational
- **Category**: coverage
- **Text**: Beyond picturing the workflow (C-01), the workaround description is detailed enough
  that another team with no prior context could reproduce it independently -- steps are
  enumerated, tools are named by product (not category), and any institutional knowledge
  required is surfaced explicitly. This matters because workarounds often depend on
  undocumented conventions that disappear when the team switches; capturing that knowledge
  raises the switching cost analysis to ground truth.
- **Pass condition**: The workaround section names specific tools (e.g., "a custom Python
  script triggered by a GitHub Action" not "automated scripts"), enumerates at least the
  major steps in sequence, and flags any part of the process that requires institutional
  knowledge or tribal context to execute correctly.
- **Source**: V-01 ("specific tools, manual steps, conventions, scripts"), V-03 ("Be specific
  enough that someone else could follow the same process"), V-05 ("Enough detail to follow
  the process").

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 5 * 10)
```

PARTIAL counts as 0.5 in pass totals.

**Golden threshold**: All 5 essential criteria pass AND composite >= 80.

| Band | Composite | Meaning |
|------|-----------|---------|
| Gold | >= 80, all essential | Ready for use as training signal |
| Silver | >= 65, all essential | Useful with minor gaps |
| Bronze | >= 50, all essential | Usable but needs revision |
| Fail | Any essential fails | Not useful -- do not use as signal |

---

## Evaluator Notes

- C-03 (threat score HIGH) is binary -- no partial credit. Missing or incorrect score = fail.
- C-04 is the most discriminating criterion. Vague conditions ("when teams want simplicity")
  are a common failure mode. Push for specificity.
- C-05 and C-04 are often confused. Keep them distinct: failure modes = what goes wrong if
  you stay; loss conditions = what must be true for inertia to lose.
- An output that answers C-04 well but skips C-05 is incomplete. The AMEND directive makes
  C-05 equally essential.
- C-10, C-11, C-12 form a cluster: C-10 is the floor (steelman present and rebutted),
  C-12 is the quality test (rebuttal anchored to a named claim), C-11 is orthogonal
  (verification method on loss conditions). They are evaluated independently.
- C-13 upgrades C-01: pass C-01 with generic concreteness, pass C-13 with replication
  fidelity. An output can pass C-01 and fail C-13.

---

## Version History

| Version | Date | Change |
|---------|------|--------|
| v1 | 2026-03-17 | Initial -- 5 essential, 3 recommended, 2 aspirational |
| v2 | 2026-03-17 | Add C-11 (verification method), C-12 (anchored rebuttal), C-13 (replication fidelity) from R1 excellence signals; formula denominator updated to 5 |
"""

with open('C:/src/sim/simulations/quest/rubrics/scout-inertia-rubric-v2-2026-03-17.md', 'w', encoding='utf-8') as f:
    f.write(content)
print('done')
