Written to `simulations/quest/rubrics/scout-inertia-rubric-v3-2026-03-17.md`.

---

**Two new aspirational criteria extracted from R2 excellence signals:**

| ID | Criterion | Source |
|----|-----------|--------|
| C-14 | **Output Organized into Labeled Analytical Sections** — the output maps 1:1 to analytical components via explicit headings/phases, enabling coverage verification by label-scan rather than prose-read. Opaque labels ("Part 1") fail; descriptive labels ("Failure Modes", "Why Inertia Loses") pass. | V-04 Phase Structure (Phase 1-4, sub-parts A/B/C) |
| C-15 | **Failure Mode Entries Decompose Trigger from Impact** — beyond naming a specific failure (C-05) and its severity (C-09), each entry distinguishes what causes it (trigger) from what happens when it does (impact). "Breaks under load" fails. "When queue depth exceeds 500 [trigger] — events silently dropped [impact]" passes. | V-02 failure mode table (trigger + severity as separate columns); V-04 Phase 3 ("name what triggers it" as a distinct structural element) |

**Formula change:** aspirational denominator updated from 5 to 7, keeping tier max at 10 pts.

**Design notes added to Evaluator Notes:**
- C-14 is structural: evaluated by heading-scan, not content depth. A correct continuous-prose output fails C-14.
- C-15 upgrades C-05: an output can pass C-05 + C-09 while failing C-15 if trigger and impact are merged.
- C-14 and C-15 are independent — each can fail while the other passes.
 Threat Score Set to HIGH
- **Weight**: essential
- **Category**: correctness
- **Text**: The output explicitly assigns an inertia threat score and that score is HIGH (or
  equivalent -- "critical", "severe"). Per skill spec, this is always HIGH by default. Any
  output that omits this score or sets it below HIGH without a documented exception fails.
- **Pass condition**: A threat score of HIGH appears explicitly in the output. Downgrading
  below HIGH requires a written justification; absence of score is an automatic fail.

### C-04 · "Why Inertia Loses" Answered
- **Weight**: essential
- **Category**: depth
- **Text**: The output identifies specific conditions under which the inertia option loses --
  the precise scenarios, thresholds, or events that make the current workaround worse than
  adopting the feature. This is the core deliverable of the skill.
- **Pass condition**: At least two distinct, concrete conditions are named (not restated
  feature benefits). Each condition must be falsifiable -- a reader could check whether it
  applies to their situation.

### C-05 · Workaround Failure Modes Identified
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

### C-06 · Switching Cost Dimensions Treated Separately
- **Weight**: recommended
- **Category**: depth
- **Text**: Time, training, and disruption are analyzed as separate line items rather than
  collapsed into a single "switching cost" number. Each dimension may affect different
  stakeholders (developer time vs. manager training budget vs. team coordination disruption).
- **Pass condition**: The output has three distinct cost entries -- one per dimension -- or
  explicitly explains why a dimension does not apply for this feature context.

### C-07 · Inertia-Loss Conditions Are Threshold-Based
- **Weight**: recommended
- **Category**: depth
- **Text**: Conditions under which inertia loses are framed as observable thresholds or
  triggers -- not general preferences. "Teams with more than 3 concurrent projects" or
  "when onboarding frequency exceeds monthly" are thresholds. "When teams are frustrated"
  is not.
- **Pass condition**: At least one inertia-loss condition uses a measurable or observable
  threshold that a team could evaluate against their actual situation.

### C-08 · Long-Term Risk of Staying on Workaround
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

### C-09 · Failure Modes Prioritized by Severity
- **Weight**: aspirational
- **Category**: depth
- **Text**: Workaround failure modes are ranked or tiered -- distinguishing which failures are
  catastrophic (data loss, silent errors, compliance risk) from which are merely inconvenient
  (extra steps, slower workflow). This helps teams understand when the workaround stops being
  acceptable.
- **Pass condition**: Failure modes include an explicit severity signal (e.g., HIGH/MED/LOW,
  a label like "data-integrity risk", or a ranked list with rationale).

### C-10 · Steelman Rebutted
- **Weight**: aspirational
- **Category**: depth
- **Text**: The output presents the strongest possible argument for staying on the workaround --
  the case a skeptical senior engineer would make -- and then rebuts it specifically. This
  demonstrates the analysis has stress-tested the inertia-loss conclusion.
- **Pass condition**: A steelman argument is explicitly labeled as such (or framed as
  "the case for inertia") and is followed by a specific rebuttal. The argument must be
  genuinely strong -- not a strawman.

### C-11 · Inertia-Loss Conditions Include Verification Method
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

### C-12 · Steelman Rebuttal Anchored to Named Claim
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

### C-13 · Workaround Described at Replication Fidelity
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

### C-14 · Output Organized into Labeled Analytical Sections
- **Weight**: aspirational
- **Category**: structure
- **Text**: The output divides its analysis into named, labeled sections or phases that map
  1:1 to distinct analytical components: workaround description, switching costs, failure
  modes, loss conditions, long-term risk, and (if present) steelman. This allows a reader
  or evaluator to locate any component by label without reading linearly and to verify
  coverage by inspection rather than by parsing prose. A single continuous prose block
  fails. Merged unlabeled sections also fail -- e.g., failure modes and loss conditions
  combined into one unlabeled narrative paragraph obscure whether both are present and
  complete.
- **Pass condition**: The output uses explicit section headings or phase labels for at least
  five distinct analytical components. Labels must be descriptive enough that a first-time
  reader knows what each section contains before reading it. Opaque labels ("Part 1",
  "Part 2") do not pass; "Workaround Description", "Failure Modes", "Why Inertia Loses"
  do.
- **Source**: V-04 Phase Structure -- Phase 1 (workaround), Phase 2 (switching costs),
  Phase 3 (failure modes), Phase 4 Part A (loss conditions + verification), Phase 4 Part B
  (steelman), Phase 4 Part C (long-term accumulation). The multi-phase organization proved
  that full analytical depth remains navigable when each component has a dedicated home.

### C-15 · Failure Mode Entries Decompose Trigger from Impact
- **Weight**: aspirational
- **Category**: depth
- **Text**: Beyond identifying specific failure modes (C-05) and ranking them by severity
  (C-09), each failure mode entry explicitly states the trigger -- the observable event or
  threshold that causes the failure -- as a statement distinct from the impact -- what
  happens when it occurs and to whom. Teams use triggers to know when to start worrying
  and impacts to know how urgently to act. Merging the two into one sentence ("this breaks
  under load") removes the signal a team needs to self-assess.
- **Pass condition**: At least two failure mode entries each contain a distinguishable
  trigger statement and a distinguishable impact statement. "The workaround fails
  occasionally" does not pass. "When queue depth exceeds 500 messages [trigger] -- events
  are silently dropped with no error surfaced to the caller [impact]" passes.
- **Source**: V-02 failure mode table requiring named trigger + severity as separate
  columns; V-04 Phase 3 explicit requirement to "name what triggers it" as a structural
  element distinct from the failure mode description itself.

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 7 * 10)
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
- C-14 is structural, not content-based. A perfectly correct output that reads as continuous
  prose fails C-14 regardless of depth. Evaluate by whether a reader could find each
  component by scanning headings alone.
- C-15 upgrades C-05: pass C-05 by naming specific failure scenarios, pass C-15 by
  separating each scenario into a distinguishable trigger and a distinguishable impact. An
  output can pass C-05 and C-09 (severity present) while still failing C-15 if trigger and
  impact are merged into a single narrative sentence.
- C-14 and C-15 are independent: a well-sectioned output (C-14) can still merge trigger and
  impact inside the failure modes section (C-15 fails); a trigger-decomposed failure mode
  section (C-15) can appear inside an otherwise continuous prose output (C-14 fails).

---

## Version History

| Version | Date | Change |
|---------|------|--------|
| v1 | 2026-03-17 | Initial -- 5 essential, 3 recommended, 2 aspirational (C-09, C-10) |
| v2 | 2026-03-17 | Add C-11 (verification method), C-12 (anchored rebuttal), C-13 (replication fidelity) from R1 excellence signals; aspirational denominator updated to 5 |
| v3 | 2026-03-17 | Add C-14 (labeled analytical sections) from V-04 Phase Structure; add C-15 (trigger/impact decomposition) from V-02/V-04 failure mode table pattern; aspirational denominator updated to 7 |
