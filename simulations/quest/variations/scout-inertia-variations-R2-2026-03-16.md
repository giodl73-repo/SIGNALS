**scout-inertia R2 — 5 variations written.**

---

## What changed from R1

R1 V-02 scored ~80 (all essential, est. 2/3 recommended, 0/2 aspirational). The gaps were: R-01 (no team-type column in defeat conditions), R-03 (basis column present but not enforced as a gate), A-01/A-02 (rubric didn't exist yet — but the pattern from V-02 already satisfies them).

R2 closes those gaps across the full variation set:

| Variation | Axis | Key delta |
|-----------|------|-----------|
| **V-01** | Full-stack integration | V-02 skeleton + R-01 team-type column + role precision check + R-03 basis enforcement as self-score criterion |
| **V-02** | Team segmentation | Team type as first-class structural axis (2 passes) — R-01 becomes impossible to miss |
| **V-03** | Grounded-first quantification | Basis-citation is a gatekeeping rule throughout, not just a column — every number needs an anchor before it's accepted |
| **V-04** | Failure-mode-first lifecycle | Inverted lifecycle — start with cracks, reconstruct the workaround from failures; adversarial from sentence one |
| **V-05** | Sparse evidence contract | Five claims, each with one evidence statement; constraint-via-scarcity instead of constraint-via-structure |

Every variation carries A-01 (per-section PASS/FAIL + revision gate) and A-02 (structural constraints — column headers that make vague entries visibly inconsistent). Every variation explicitly wires R-01, R-02, and R-03.
fact is not complete.

Output every section as a table. Score yourself after each section. Use the composite gate in Section 6 before finalizing.

---

### Section 1 — Workaround Profile

| Field | Value |
|-------|-------|
| Workaround name | |
| Tool / file type / process | |
| Data or action handled | |
| Who performs it (role — e.g., "PM", "DevOps engineer", not "teams" or "the person who...") | |
| Frequency | |
| Output artifact | |

**Role precision check**: If the "who performs it" cell contains "teams", "users", "people", or a department name rather than a job role, replace it before continuing. Role-level precision matters for targeted onboarding design.

**Self-score C-01** (Workaround mapped in detail):
- [ ] PASS — Named workaround with specific tool/process, role actor, frequency, and output artifact present
- [ ] FAIL — Generic category or vague actor; return and add specifics before Section 2

---

### Section 2 — Switching Cost Breakdown

| Dimension | Estimate | Unit | Basis / assumption |
|-----------|----------|------|--------------------|
| Time cost to migrate and ramp | | hours or days/user | |
| Training cost | | hours of training per user | |
| Workflow disruption | | sprint-days or people affected | |

**Basis requirement**: At least one row in the Basis column must contain an explicit anchor — an analogy to a comparable migration, a stated assumption, or a source. "~4 hours/user (based on similar CSV-to-tool migrations in last onboarding cycle)" passes. An empty basis cell is acceptable for rows 2 and 3 if row 1 carries a basis, but no row may have a qualitative label ("high") in the Estimate column.

**Self-score C-02** (Switching cost quantified):
- [ ] PASS — At least 2 of 3 rows carry a number or range in the Estimate column
- [ ] FAIL — Qualitative labels present; return and quantify

**Self-score R-03** (At least one cost has cited basis):
- [ ] PASS — At least one Basis cell carries an analogy, comparable, assumption, or source
- [ ] FAIL — All basis cells empty; return and add at least one anchor

---

### Section 3 — Inertia Threat Score

| Field | Value |
|-------|-------|
| Score | HIGH / MEDIUM / LOW |
| Rationale | |
| Mitigating factor (required if not HIGH) | |
| Evidence for mitigation (required if not HIGH) | |

**Default**: HIGH. Reduce only if you can document evidence that the workaround is already being actively abandoned independent of this feature.

**Self-score C-03** (Inertia threat score is HIGH):
- [ ] PASS — Score is HIGH, or mitigation is documented with named evidence
- [ ] FAIL — Score reduced without evidence; restore to HIGH

---

### Section 4 — Workaround Failure Modes

| # | Trigger | What goes wrong | User-visible symptom | Recovery cost |
|---|---------|-----------------|----------------------|---------------|
| FM-01 | | | | |
| FM-02 | | | | |
| FM-03 (optional) | | | | |

**Column contract**: "Trigger" must be a specific input, volume threshold, edge case, or workflow event — not a general category. "User-visible symptom" must be something the user can observe without reading a log. Generic entries ("slow", "doesn't scale") do not qualify.

**Self-score C-05** (Failure modes identified):
- [ ] PASS — At least 2 rows with specific trigger and observable symptom
- [ ] FAIL — Generic pain points only; return and make concrete

---

### Section 5 — Conditions Under Which Inertia Loses

| # | Observable trigger | Team type this applies to | Why workaround fails at this trigger | What teams do instead |
|---|-------------------|-----------------------------|--------------------------------------|-----------------------|
| DC-01 | | | | |
| DC-02 | | | | |
| DC-03 (optional) | | | | |

**Column contract**: "Observable trigger" must be a falsifiable threshold — a third party must be able to observe whether it has been met. "Teams switch when they see value" fails. "Teams switch when FM-01 recurs three times in a sprint" passes.

**Team type column**: At least one row must name a specific team type or role context ("data-heavy PMs", "DevOps teams managing > 3 services", "teams onboarding > 5 new members per quarter"). Universal triggers are weaker — they hide the segmentation that matters for rollout planning.

**Self-score C-04** (Why inertia loses answered):
- [ ] PASS — At least 2 rows with falsifiable trigger
- [ ] FAIL — Vague conditions present; return and add observable thresholds

**Self-score R-01** (Adoption trigger scoped to team type):
- [ ] PASS — At least one DC row names a specific team type or role context
- [ ] FAIL — All conditions stated as universal; return and scope at least one

---

### Section 6 — Composite Self-Score and Revision Gate

| Criterion | Result | Action if FAIL |
|-----------|--------|----------------|
| C-01 Workaround mapped in detail | PASS / FAIL | Return to Section 1 |
| C-02 Switching costs quantified | PASS / FAIL | Return to Section 2 |
| R-03 At least one cost has cited basis | PASS / FAIL | Return to Section 2 |
| C-03 Inertia threat score HIGH | PASS / FAIL | Return to Section 3 |
| C-05 Failure modes identified | PASS / FAIL | Return to Section 4 |
| C-04 Why inertia loses answered | PASS / FAIL | Return to Section 5 |
| R-01 Trigger scoped to team type | PASS / FAIL | Return to Section 5 |
| **All essential pass (C-01..C-05)?** | YES / NO | Revise before finalizing |

**Gate**: If any essential criterion (C-01 through C-05) is FAIL, revise the corresponding section before marking this artifact complete. Recommended criteria (R-01, R-03) failures are advisory — note them for the next iteration.

---

*End V-01*

---

## V-02 — Team-Segmented Analysis: Run twice, once per team type

**Variation axis**: Team segmentation — the analysis is structured as two passes over a shared workaround, each scoped to a distinct team type. R-01 is satisfied structurally (team type is the top-level organizing axis) rather than instructionally.

**Hypothesis**: If team type is a first-class structural element rather than a column in one table, the analyst cannot produce a universal analysis by accident. Segmentation forces both more precise switch conditions (R-01) and more precise role identification (R-02), because each team type has a different primary actor.

---

You are running `scout-inertia`. This analysis is structured in two passes: one for each major team type that uses or would use the feature. A universal analysis obscures the segmentation that drives adoption planning.

**Before you begin**: Name the two team types most relevant to this feature. These are the two populations whose current workaround you will analyze. Write them here:

- **Primary team type**: (e.g., "PMs managing multi-product roadmaps")
- **Secondary team type**: (e.g., "DevOps engineers managing > 3 services")

---

### Shared Workaround (complete once — applies to both team types)

Describe the workaround that both team types currently use. If they use fundamentally different workarounds, treat them as separate analyses.

| Field | Detail |
|-------|--------|
| Workaround name | |
| Tool / file type / process | |
| Data or action handled | |
| Output artifact | |

---

### Pass A — Primary team type: [fill in above]

#### A1 — Primary actor profile

| Field | Value |
|-------|-------|
| Who performs the workaround? (role) | |
| Frequency for this team type | |
| Volume or scale context | |

**Role precision check**: Actor must be a role ("PM", "data analyst"), not a department ("product team") or a vague population ("users"). If not a role, rewrite it.

#### A2 — Switching costs for primary team type

| Dimension | Estimate | Unit | Basis / assumption |
|-----------|----------|------|--------------------|
| Time to migrate and ramp | | hours or days/user | |
| Training cost | | hours per user | |
| Workflow disruption | | sprint-days or people affected | |

At least one basis cell must carry an anchor (analogy, comparable migration, or stated assumption).

#### A3 — Failure modes for primary team type

| # | Trigger | What goes wrong | User-visible symptom |
|---|---------|-----------------|----------------------|
| FM-A01 | | | |
| FM-A02 | | | |

Triggers must be specific. Symptoms must be observable. "Manual is slow" does not qualify.

#### A4 — Defeat conditions for primary team type

| # | Observable trigger | Linked failure mode | Falsifiable? |
|---|-------------------|--------------------:|--------------|
| DC-A01 | Teams switch when... | FM-A__ | YES / NO |
| DC-A02 | Teams switch when... | FM-A__ / External | YES / NO |

All conditions must be YES in the Falsifiable column. If NO, rewrite until a third party could observe whether the condition is met.

---

### Pass B — Secondary team type: [fill in above]

#### B1 — Secondary actor profile

| Field | Value |
|-------|-------|
| Who performs the workaround? (role) | |
| Frequency for this team type | |
| Volume or scale context | |

**Role precision check**: Same rule — role, not department.

#### B2 — Switching costs for secondary team type

| Dimension | Estimate | Unit | Basis / assumption |
|-----------|----------|------|--------------------|
| Time to migrate and ramp | | hours or days/user | |
| Training cost | | hours per user | |
| Workflow disruption | | sprint-days or people affected | |

#### B3 — Failure modes for secondary team type

| # | Trigger | What goes wrong | User-visible symptom |
|---|---------|-----------------|----------------------|
| FM-B01 | | | |
| FM-B02 | | | |

#### B4 — Defeat conditions for secondary team type

| # | Observable trigger | Linked failure mode | Falsifiable? |
|---|-------------------|--------------------:|--------------|
| DC-B01 | Teams switch when... | FM-B__ | YES / NO |
| DC-B02 | Teams switch when... | FM-B__ / External | YES / NO |

---

### Inertia threat score

**Score**: HIGH *(default — reduce only with documented evidence of active abandonment already in progress)*

---

### Cross-segment verdict

Write two to four sentences: why does inertia lose for each team type, and which team type is likely to adopt first and why?

Reference failure modes and defeat conditions by ID. If the two team types have different adoption thresholds, say so explicitly — it determines rollout sequencing.

---

### Self-score

| Criterion | Primary (A) | Secondary (B) |
|-----------|-------------|---------------|
| C-01 Workaround mapped | PASS / FAIL | PASS / FAIL |
| C-02 Costs quantified | PASS / FAIL | PASS / FAIL |
| R-02 Actor is a role | PASS / FAIL | PASS / FAIL |
| R-03 Basis cited for cost | PASS / FAIL | PASS / FAIL |
| C-05 Failure modes concrete | PASS / FAIL | PASS / FAIL |
| C-04 Defeat conditions falsifiable | PASS / FAIL | PASS / FAIL |
| R-01 Team type scoped | YES (structural) | YES (structural) |
| C-03 Inertia threat HIGH | PASS / FAIL | — (shared) |

**Gate**: All essential criteria (C-01..C-05) must pass for both segments. Revise failing sections before finalizing.

---

*End V-02*

---

## V-03 — Grounded-First Quantification: Every number needs an anchor before it is accepted

**Variation axis**: Citation/grounding emphasis — the prompt makes basis-citation a gatekeeping mechanism throughout, not just a recommended column. A number without an anchor is treated as no better than a qualitative label.

**Hypothesis**: In R1, the basis column existed in V-02 but was easy to leave empty. Making basis-first a structural gatekeeping requirement throughout (not just in the cost table) closes R-03, incidentally forces more careful failure mode thresholds, and raises the overall credibility of every quantitative claim in the artifact.

---

You are running `scout-inertia`. This analysis relies on quantified claims. A quantified claim without a stated basis is as weak as a qualitative label — it cannot be challenged, verified, or updated when conditions change.

**The basis rule**: Every number or range in this analysis must be followed immediately by its basis in parentheses. Acceptable bases:
- An analogy: "(similar to last quarter's CSV migration: 3 hours/user)"
- A stated assumption: "(assuming standard tool onboarding; no historical data)"
- A reference: "(per Q3 onboarding report)"
- An acknowledgment of uncertainty with a range: "(unknown; estimating wide: 2-8 hours/user)"

A number with no basis in parentheses is not acceptable. If you cannot produce a basis, write the range wide and acknowledge the uncertainty.

---

### Step 1 — Workaround: what inertia is protecting

Describe the workaround. Name it. Identify the role that performs it, not the department. State how often it happens and what it produces.

Failure check: if your description contains only a category ("manual process", "spreadsheet workflow"), stop and add the specific tool, the specific actor role, and the specific output artifact.

---

### Step 2 — Switching costs: inertia's defenses, grounded

For each dimension, state the estimate and its basis immediately.

**Time cost**: [estimate] ([basis])
Example: "3-5 hours/user (based on analogous data migration onboarding for Tool X in Q4)"

**Training cost**: [estimate] ([basis])
Example: "2 hours of training per user (assuming one async walkthrough session; no prior internal data)"

**Workflow disruption**: [estimate] ([basis])
Example: "1 sprint of partial disruption, 4 people affected (based on handoff complexity observed in similar process migrations)"

Inertia threat score: **HIGH** *(default; reduce only with documented evidence of active abandonment already underway)*

---

### Step 3 — Failure modes: where the workaround's numbers break down

For each failure mode, the description must include an observable trigger and a user-visible symptom. Then state the failure frequency with a basis.

**FM-01**:
- Trigger: [specific input, volume threshold, or workflow event]
- What goes wrong: [specific error, data loss, re-work required]
- User-visible symptom: [what the user sees or experiences]
- Frequency estimate: [estimate] ([basis])

**FM-02**:
- Trigger:
- What goes wrong:
- User-visible symptom:
- Frequency estimate: [estimate] ([basis])

Generic entries ("it's slow when there's a lot of data") do not pass. If you cannot state a specific trigger, you have not found a real failure mode — look harder.

---

### Step 4 — Defeat conditions: when the cost of staying exceeds the cost of switching

For each condition, state the observable threshold and scope it to a team type. Then state what would make you believe the threshold estimate is wrong — this is the falsifiability check.

**DC-01**:
- Condition: Teams switch when [observable trigger — falsifiable by third party]
- Applies to: [specific team type or role context]
- Basis for threshold: [how did you arrive at this threshold — analogy, assumption, observation?]
- What would invalidate this: [what evidence would show this condition is wrong or premature?]

**DC-02**:
- Condition: Teams switch when [observable trigger]
- Applies to: [specific team type or role context]
- Basis for threshold:
- What would invalidate this:

---

### Step 5 — Verdict

Answer directly: why does inertia lose? Reference failure modes and defeat conditions by label. State what the feature must provide that the workaround cannot.

If any of your quantified claims carry no basis, flag them here as confidence gaps — claims the team should verify before committing to the feature timeline.

---

### Self-score

| Criterion | Result |
|-----------|--------|
| C-01 Workaround mapped in detail | PASS / FAIL |
| C-02 Switching costs quantified (numbers present) | PASS / FAIL |
| R-03 At least one cost has cited basis | PASS / FAIL |
| C-03 Inertia threat score HIGH | PASS / FAIL |
| C-05 Failure modes with specific trigger and symptom | PASS / FAIL |
| C-04 Why inertia loses with falsifiable conditions | PASS / FAIL |
| R-01 At least one condition scoped to team type | PASS / FAIL |
| R-02 Workaround actor is a named role | PASS / FAIL |

**Gate**: All C-0x criteria must pass. If any fail, revise the corresponding step before finalizing. Flag R-0x failures as next-iteration improvements.

---

*End V-03*

---

## V-04 — Failure-Mode-First: Inverted lifecycle, start with the cracks

**Variation axis**: Lifecycle inversion — begin with failure mode discovery, then work backward to understand what workaround produces them, then quantify switching costs. The standard lifecycle (workaround → costs → failure modes → conditions) is reversed.

**Hypothesis**: Starting with "describe the workaround" biases the analysis toward the happy-path picture of the workaround that its users hold. Starting with "find where it breaks" forces the analyst to think adversarially from the first sentence. Cracks often reveal workaround details (actor, frequency, volume) that the happy-path description omits — the description that emerges from failure discovery is richer than one written top-down.

---

You are running `scout-inertia`. Start from the cracks. If you can find where the current workaround fails, you can understand it. If you can quantify the failures, you can identify when a team has had enough.

Do not start by describing the workaround. Start by finding where it breaks.

---

### Step 1 — Find the failure modes (begin here)

Think like a tester trying to make the workaround fail. For each failure mode:

| # | What breaks | Specific trigger | User-visible symptom | How often | Recovery cost |
|---|-------------|-----------------|----------------------|-----------|---------------|
| FM-01 | | | | | |
| FM-02 | | | | | |
| FM-03 (optional) | | | | | |

**Column contract**:
- "Specific trigger" must be a concrete input, volume, or event — not a general category
- "User-visible symptom" must be observable without reading a log
- "How often" must be an estimate with a basis in parentheses, or acknowledge uncertainty

If you cannot find at least two failure modes, re-examine the workaround from the perspective of a user who has been burned by it, not one who just learned it.

---

### Step 2 — Reconstruct the workaround from the failures

The failure modes you found reveal what the workaround is. Now describe it.

| Field | What the failure modes reveal |
|-------|-------------------------------|
| What is the workaround? (specific tool/process — emerged from failure analysis) | |
| Who is most affected when it fails? (role — this is likely the primary actor) | |
| At what volume or frequency do failures appear? (this is likely the normal operating frequency) | |
| What does the workaround normally produce? (the artifact that breaks or gets corrupted) | |

**Role precision check**: Actor must be a role ("data analyst", "release manager"), not a department or vague population. The failures point to who is responsible — use that.

**Self-score C-01** (Workaround mapped):
- [ ] PASS — Named workaround with role, frequency, and output artifact present
- [ ] FAIL — Return to Step 1; more specific failure modes will reveal more specific workaround details

---

### Step 3 — Quantify the switching cost (starting from what you now know)

Now that you understand the workaround from its failure modes, you can estimate abandonment costs more precisely.

| Dimension | Estimate | Unit | Basis / assumption |
|-----------|----------|------|--------------------|
| Time to migrate and ramp | | hours or days/user | |
| Training cost | | hours per user | |
| Workflow disruption | | sprint-days or people affected | |

At least one basis cell must contain an anchor (comparable migration, stated assumption, or acknowledged uncertainty range).

**Self-score C-02** (Costs quantified):
- [ ] PASS — At least 2 of 3 rows carry a number or range
- [ ] FAIL — Return and quantify

**Self-score R-03** (Basis cited):
- [ ] PASS — At least one basis cell carries an anchor
- [ ] FAIL — Add at least one anchor

**Inertia threat score**: HIGH *(default — reduce only with documented evidence of active abandonment already underway)*

---

### Step 4 — Map defeat conditions from failure modes

Each failure mode you found is a potential defeat condition. For each one, identify the threshold at which the failure becomes intolerable.

| # | Defeat condition | Source failure mode | Team type this applies to | Falsifiable? |
|---|-----------------|--------------------:|---------------------------|--------------|
| DC-01 | Teams switch when... | FM-__ | | YES / NO |
| DC-02 | Teams switch when... | FM-__ / External | | YES / NO |
| DC-03 (optional) | | | | |

**Columns**:
- "Defeat condition" must be falsifiable — a third party must be able to observe whether the threshold has been crossed
- "Team type" must name a specific team or role context, not a universal population
- All entries in "Falsifiable?" must be YES — rewrite any NO before continuing

Also consider: external forcing functions not tied to a failure mode. Regulation, platform change, key-person departure, competitive event. Add as DC rows with "External" in the source column.

**Self-score C-04** (Why inertia loses):
- [ ] PASS — At least 2 conditions are falsifiable
- [ ] FAIL — Return and rewrite vague conditions

**Self-score C-05** (Failure modes):
- [ ] PASS — At least 2 FM rows with specific trigger and observable symptom
- [ ] FAIL — Return to Step 1

**Self-score R-01** (Team type scoped):
- [ ] PASS — At least one DC row names a specific team type
- [ ] FAIL — Return and scope at least one condition

---

### Step 5 — Verdict

Write two to four sentences: why does inertia lose? Reference failure modes and defeat conditions by ID. State what must be true for the feature to tip each defeat condition. If none of the conditions are met, say so — inertia wins and the feature does not get adopted regardless of its quality.

---

### Composite gate

| Criterion | Result |
|-----------|--------|
| C-01 | PASS / FAIL |
| C-02 | PASS / FAIL |
| R-03 | PASS / FAIL |
| C-03 | PASS / FAIL |
| C-05 | PASS / FAIL |
| C-04 | PASS / FAIL |
| R-01 | PASS / FAIL |
| R-02 | PASS / FAIL |
| **All C-0x pass?** | YES / NO |

If any C-0x criterion fails, revise before finalizing.

---

*End V-04*

---

## V-05 — Sparse Evidence Contract: Five claims, each with a one-sentence evidence statement

**Variation axis**: Compression + constraint-via-sparsity — the entire analysis is expressed as exactly five named claims. Each claim has a one-to-two sentence evidence statement. No tables with many rows. No filler.

**Hypothesis**: Tables with many rows allow analysts to write one strong row and two weak rows and still feel they have satisfied the format. A format that gives exactly one evidence statement per claim forces the analyst to choose the strongest, most specific evidence they have. Constraint-via-scarcity may drive precision as effectively as constraint-via-structure — and produces a more readable artifact for a skeptical PM.

---

You are running `scout-inertia`. The output is five claims. Each claim is a one-sentence assertion. Immediately after each claim, write one to two sentences of evidence that justify it. No tables. No roles. No filler.

The five claims are fixed. Fill them in order.

---

**Claim 1 — The workaround**

*Assertion*: [One sentence naming the specific workaround, actor role, and how often it happens.]

*Evidence*: [One to two sentences describing what the workaround produces and what makes it sticky — why teams chose it and why they stay.]

**Failure check**: If your assertion contains "teams", "users", "a manual process", or "a spreadsheet" without a more specific noun, rewrite it. The assertion must be specific enough that a new hire could identify the workaround from it.

---

**Claim 2 — The switching cost**

*Assertion*: [One sentence stating the total switching cost across the two largest dimensions, with numbers and units.]

*Evidence*: [One to two sentences explaining the basis for the estimates — an analogy, a comparable migration, a stated assumption, or an acknowledged uncertainty range.]

**Failure check**: If the assertion contains "high", "moderate", or "low" without a number, rewrite it. If the evidence does not name a basis, add one. "Estimated based on similar onboarding cycles" passes. "Assumed" alone does not.

---

**Claim 3 — The inertia threat score**

*Assertion*: Inertia threat score: HIGH. [One sentence stating the primary reason the score is HIGH.]

*Evidence*: [One to two sentences stating what mitigating factor would justify reducing the score, and confirming whether that factor is present. If present, document it here.]

**Default rule**: The score is HIGH unless you have documented evidence of active abandonment already underway independent of this feature. "The feature is better" is not a mitigating factor.

---

**Claim 4 — The failure modes**

*Assertion*: [One sentence naming two specific failure modes of the workaround — what breaks and when.]

*Evidence*: [One to two sentences describing the user-visible symptom of each failure mode and an estimate of how often it occurs, with a basis.]

**Failure check**: If the assertion contains "slow", "manual", "doesn't scale" without a specific trigger and symptom, rewrite it. "FM-01: CSV export silently truncates rows over 65,536 — no error; FM-02: pivot table breaks on non-ASCII characters, producing wrong totals" passes.

---

**Claim 5 — Why inertia loses**

*Assertion*: [One sentence stating the specific condition under which a specific team type abandons the workaround, falsifiable by a third party.]

*Evidence*: [One to two sentences explaining what must happen for the feature to tip this condition — what the feature provides that the workaround cannot, and what remains true if the condition is not met.]

**Failure check**: If the assertion contains "when they see the value" or "when they realize" or "when it becomes clear", rewrite it. The condition must name an observable event. "Teams switch when FM-01 recurs twice in one release cycle and causes a missed deadline" passes.

---

### Self-score

After writing all five claims, check:

| Criterion | Check |
|-----------|-------|
| C-01: Claim 1 names specific tool, role actor, frequency | PASS / FAIL |
| C-02: Claim 2 carries a number with a unit | PASS / FAIL |
| R-03: Claim 2 evidence names a basis | PASS / FAIL |
| C-03: Claim 3 states HIGH with rationale | PASS / FAIL |
| C-05: Claim 4 names two specific failure modes with trigger and symptom | PASS / FAIL |
| C-04: Claim 5 states a falsifiable condition | PASS / FAIL |
| R-01: Claim 5 names a specific team type | PASS / FAIL |
| R-02: Claim 1 actor is a role (not department/population) | PASS / FAIL |

**Gate**: All C-0x criteria must pass. If any fail, rewrite the corresponding claim. The format constraint (one assertion, one evidence) must be respected — do not add filler to satisfy a criterion. If you cannot satisfy C-04 in one sentence with one evidence paragraph, you have not found the inertia-breaking condition yet.

---

*End V-05*

---

*End of V-01 through V-05 — scout-inertia R2*

**Coverage summary**:

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 essential | Y | Y | Y | Y | Y |
| C-02 essential | Y | Y | Y | Y | Y |
| C-03 essential | Y | Y | Y | Y | Y |
| C-04 essential | Y | Y | Y | Y | Y |
| C-05 essential | Y | Y | Y | Y | Y |
| R-01 team type | Y | Y (structural) | Y | Y | Y |
| R-02 role precision | Y | Y | Y | Y | Y |
| R-03 cited basis | Y | Y | Y | Y | Y |
| A-01 self-correction | Y | Y | Y | Y | Y |
| A-02 structural constraints | Y | Y | partial | Y | partial |
