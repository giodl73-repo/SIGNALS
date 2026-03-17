Written to `simulations/quest/rubrics/scout-inertia-rubric-v5-2026-03-17.md`.

---

**Changes from v4 to v5:**

**New criterion added:**

| ID | Criterion | Source |
|----|-----------|--------|
| C-18 | **Each Tabular Section Opens with a Per-Table Column Manifest** -- immediately before each table, an explicit "Required columns for this table:" declaration appears. Column omission is then detectable at the declaration line, not only at the table header row. This is the column-level analog of C-17 applied locally (per table) rather than globally (per document). | R4 pattern: V-05 per-table column declarations before Section C and Section D |

**Formula change:** aspirational denominator updated from 9 to 10, tier max stays at 10 pts.

**Evaluator Notes additions:**
- C-18 relationship to C-16 and C-17: pairwise independent, form a complete three-layer enforcement stack (C-16 = dedicated columns exist; C-17 = headings pre-declared globally; C-18 = columns pre-declared locally at each table).
- Reliability gradient note: R4 all-100 result establishes that score and structural enforcement strength are independent axes -- once a scaffold reaches 100, adversarial robustness (V-01 < V-02 < V-03 < V-04 < V-05) becomes the meaningful differentiator. Flagged as evaluator insight, not a scored criterion.
least two quantified cost estimates (e.g.,
  "2-4 hours of migration per project", "1-2 days of team onboarding") or explicit N/A with
  justification for any omitted dimension.

### C-03 · Inertia Threat Score Set to HIGH
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

### C-16 · Trigger/Impact Decomposition Uses Dedicated Table Columns
- **Weight**: aspirational
- **Category**: structure
- **Text**: Beyond separating trigger from impact in prose (C-15), the failure mode table
  implements this separation as dedicated, named columns -- one column for Trigger, one for
  Impact -- rather than labeled inline fields within a single merged cell. Column-level
  structure makes non-compliance structurally visible: a blank Impact cell is obviously
  malformed and immediately detectable; a partially-compliant prose label nested inside a
  merged cell is not. This is the structural enforcement property that makes C-15 auditable
  at a glance rather than requiring full reading of each cell.
- **Pass condition**: The failure mode table contains at least two separate named columns
  whose labels (or equivalent headings) distinguish trigger from impact. Labeled bullet
  points or inline "Trigger: / Impact:" markers within a single column cell do not pass.
  "When X [Trigger] -- Y happens [Impact]" in one cell does not pass. A Trigger column and
  a separate Impact column do.
- **Source**: R3 excellence pattern -- V-02/V-05 column-level decomposition vs. V-01 labeled
  bullets. V-01's labeled bullets admitted partially-compliant entries that passed the label
  check but failed depth inspection. V-02/V-05's separate Impact column made the same
  non-compliance structurally visible without any inspection of cell content.

### C-17 · Synthesis Step Declares Section Heading Manifest
- **Weight**: aspirational
- **Category**: structure
- **Text**: The synthesis, conclusion, or output-generation step of the prompt explicitly
  declares a manifest of required section headings before the content is rendered. The
  manifest acts as a structural pre-commitment: if a heading listed in the manifest is
  absent from the output, the gap is detectable at the declaration site without scanning
  the entire document. This is a stronger enforcement property than C-14 (which requires
  labeled sections) -- an output can pass C-14 by having correct headings without declaring
  any manifest, but cannot pass C-17 without an explicit pre-commitment.
- **Pass condition**: The output contains an explicit list of required section headings
  (a manifest) before the first section begins -- e.g., "This output must contain the
  following sections: [list]" or equivalent. The manifest must be complete enough that
  a reader could verify section coverage by comparing the manifest against the actual
  headings without reading the body content.
- **Source**: R3 excellence pattern -- V-03 proved that the heading manifest is a synthesis-
  step constraint orthogonal to role structure: C-14 enforcement was added to any
  adversarial role prompt by grafting the heading manifest onto the synthesis step only,
  leaving roles untouched. V-05 inherits this pattern. The key insight: the manifest
  externalizes the structural contract, making omission visible at declaration rather than
  only at scan time.

### C-18 · Each Tabular Section Opens with a Per-Table Column Manifest
- **Weight**: aspirational
- **Category**: structure
- **Text**: Beyond declaring a section heading manifest before output begins (C-17), each
  tabular section opens with an explicit pre-committed list of required columns for that
  specific table -- placed immediately before the table itself. This per-table column
  declaration converts the column requirement into an execution-site pre-commitment: a
  missing or renamed column is detectable at the declaration line, not only by inspecting
  the table header row. This is the column-level analog of C-17 applied locally to each
  table rather than globally to the document.
- **Pass condition**: At least one tabular section in the output includes an explicit column
  manifest immediately before the table (e.g., "Required columns for this table: Failure
  Mode | Trigger | Impact | Severity"). The manifest must be complete enough that a reader
  could verify table structure by comparing it against the actual column headers without
  scanning cell content. A table-level section heading alone (C-16) does not pass; an
  explicit pre-committed column declaration does.
- **Source**: R4 excellence pattern -- V-05 adds "Required columns for this table:"
  immediately before Section C (Failure Mode Table) and Section D (Inertia-Loss Conditions).
  This is the column-level analog of C-17: declaration appears at the execution site
  (immediately before the table), making column omission detectable at the declaration line.
  Neither C-16 (dedicated columns exist) nor C-17 (document-level section manifest) captures
  this property. V-01 through V-04 all pass C-16 and C-17 but fail C-18 -- one insertion
  per table brings any of them into compliance.

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 10 * 10)
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
- C-16 upgrades C-15: pass C-15 with labeled inline prose, fail C-16 without separate
  columns. The structural enforcement property is the key difference -- column-level
  separation makes blank/malformed cells visually obvious; inline labels do not. An output
  can pass C-15 and fail C-16.
- C-17 upgrades C-14: pass C-14 by having correct descriptive headings, pass C-17 only if
  a heading manifest is declared before content begins. C-17 is the pre-commitment form of
  C-14. An output can pass C-14 and fail C-17.
- C-16 and C-17 are independent: a table with dedicated columns (C-16) can appear in an
  output with no heading manifest (C-17 fails); a heading manifest (C-17) can precede
  sections that use prose-merged trigger/impact cells (C-16 fails).
- C-18 upgrades C-17 locally: C-17 pre-commits to section headings at the document level;
  C-18 pre-commits to column structure at each table's execution site. An output can pass
  C-17 (global section manifest present) and fail C-18 (no per-table column manifest). An
  output can also pass C-16 (dedicated Trigger/Impact columns exist in the rendered table)
  and fail C-18 (no pre-committed column declaration before that table).
- C-16, C-17, and C-18 are pairwise independent: any combination of pass/fail across all
  three is structurally possible. The three together form a complete structural enforcement
  stack: C-16 = dedicated columns exist; C-17 = section headings are pre-declared globally;
  C-18 = column structure is pre-declared locally at each table.
- **Reliability gradient (evaluator insight, not a scored criterion)**: All five R4
  variations scored 100 against rubric v4. The differentiator is adversarial robustness --
  how hard it is to violate a structural property without detection. Ranked V-01 < V-02 <
  V-03 < V-04 < V-05 by violation detectability. Score and structural enforcement strength
  are independent axes: once a scaffold reaches 100, reliability tiers matter more than
  score tiers. C-18 captures the strongest form of this property.

---

## Version History

| Version | Date | Change |
|---------|------|--------|
| v1 | 2026-03-17 | Initial -- 5 essential, 3 recommended, 2 aspirational (C-09, C-10) |
| v2 | 2026-03-17 | Add C-11 (verification method), C-12 (anchored rebuttal), C-13 (replication fidelity) from R1 excellence signals; aspirational denominator updated to 5 |
| v3 | 2026-03-17 | Add C-14 (labeled analytical sections) from V-04 Phase Structure; add C-15 (trigger/impact decomposition) from V-02/V-04 failure mode table pattern; aspirational denominator updated to 7 |
| v4 | 2026-03-17 | Add C-16 (dedicated trigger/impact columns) from R3 pattern: column-level enforcement structurally stronger than labeled bullets; add C-17 (synthesis heading manifest) from R3 pattern: manifest orthogonal to role structure, detects omission at declaration site; aspirational denominator updated to 9 |
| v5 | 2026-03-17 | Add C-18 (per-table inline column manifest) from R4 excellence pattern: V-05 column-level analog of C-17, places "Required columns:" declaration at each table's execution site; aspirational denominator updated to 10; add reliability gradient evaluator note: score and structural enforcement strength are independent axes |
