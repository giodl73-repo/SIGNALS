**scout-inertia R3 — 5 variations written.**

---

## What changed from R2

| Variation | Axis | Key delta |
|-----------|------|-----------|
| **V-01** | Question-primed tables (phrasing register) | Each section opens with a direct prose question; analyst writes one-sentence answer before transcribing to table — two-pass attention catches vague entries before they solidify into cells |
| **V-02** | Team segmentation + mandatory synthesis | R2 V-02 repair — same two-pass structure, but adds a synthesis section with its own C-04 self-score gate; synthesis must reference DC-A and DC-B IDs and produce at least two team-scoped falsifiable conditions |
| **V-03** | Failure-first + explicit C-01 gate | R2 V-04 repair — same inverted lifecycle, but the workaround reconstruction step now has an explicit C-01 self-score that quotes all four pass conditions; FAIL redirects back to Step 1 to find more specific failures |
| **V-04** | Adversarial advocate / rebuttal | New axis — write the strongest honest case for inertia winning (with quantified switching costs), then write rebuttals that must address each argument by name; defeat conditions emerge from the rebuttal table |
| **V-05** | Progressive commitment chain | New axis — declares ACTOR-01, WA-01, FM-01/FM-02 as named identifiers in early steps; subsequent steps must reference by ID; a defeat condition without an FM citation is a structural type error, not just a quality gap |

All five carry **A-01** (per-section gate), **A-02** (column constraints), **A-03** (composite gate with back-pointers), and **A-04** (role precision as continuation gate). The v3 rubric's new aspirational criteria are satisfied structurally in every variation, not just instructionally.

The two R2 non-golden variations (V-02, V-04) are directly repaired. R2 V-05's scarcity problem is replaced by a different constraint paradigm (commitment chain) that preserves precision without conflicting with multi-dimensional coverage requirements.
tion gate).

---

## V-01 — Question-Primed Tables: Prose answer before table entry

**Variation axis**: Phrasing register — each section opens with a direct question the analyst
answers in one sentence of prose before transcribing into the structured table.

**Hypothesis**: Table-format instructions can be satisfied mechanically — a vague department name
fills a cell without resistance. A direct question ("who performs this workaround — name their
role, not their team") forces a formulated answer. The analyst writes the answer in prose first,
then transcribes it. Two-pass attention on precision catches vague entries at the moment of
formation, before they become table cells. This may reduce the "teams" / "users" failure pattern
more effectively than instruction text alone.

---

You are running `scout-inertia`. This analysis answers one question: **why does inertia lose?**

Each section below opens with a direct question. Write a one-sentence prose answer first. Then
transcribe it into the table. The two-pass approach catches vague entries before they settle.

---

### Section 1 — Workaround Profile

**Question**: Who performs this workaround — using what tool, how often, and to produce what?

*Write your one-sentence answer here before filling the table*:

> ___

Now transcribe into the table:

| Field | Value |
|-------|-------|
| Workaround name | |
| Tool / file type / process | |
| Data or action handled | |
| Who performs it [role — not department, not "users": e.g., "PM", "DevOps engineer", "data analyst"] | |
| Frequency [e.g., "weekly before Monday standup", "per release cycle"] | |
| Output artifact [what it produces] | |

**A-04 — Role precision gate** *(pre-condition for Section 2)*:

Read the "Who performs it" cell. If it contains "teams", "users", "people", "the team", or a
department name rather than a role, rewrite it before continuing. Your prose answer should have
named a role — if it did not, revise the answer, then transcribe again. Only continue to Section 2
once the cell names a role.

**Self-score C-01** (Workaround mapped in detail):
- [ ] PASS — Named workaround, specific tool/process, role actor, frequency, and output artifact all present
- [ ] FAIL — Return here and add specifics before continuing to Section 2

---

### Section 2 — Switching Cost Breakdown

**Question**: What would it cost the [role from Section 1] to abandon this workaround — in time,
training, and disruption?

*Write your one-sentence answer here before filling the table*:

> ___

Now transcribe into the table:

| Dimension | Estimate [number or range — "high"/"low" not accepted] | Unit | Basis [analogy, comparable migration, stated assumption, or explicit uncertainty range] |
|-----------|--------------------------------------------------------|------|-----------------------------------------------------------------------------------------|
| Time to migrate and ramp | | hours or days per [role] | |
| Training | | hours per [role] | |
| Workflow disruption | | sprint-days or number of people affected | |

**Inertia threat score**: HIGH *(default — reduce only with documented evidence that the
workaround is being actively abandoned independent of this feature)*

**Self-score C-02** (Switching costs quantified):
- [ ] PASS — At least 2 of 3 Estimate cells carry a number or range
- [ ] FAIL — Return and quantify before Section 3

**Self-score R-03** (At least one cost cited to named role):
- [ ] PASS — At least one Estimate cell names the role from Section 1 alongside the number, and at least one Basis cell carries an anchor
- [ ] FAIL — Add role label and at least one basis anchor

**Self-score C-03** (Inertia threat HIGH):
- [ ] PASS — Score stated as HIGH, or mitigation documented with named evidence
- [ ] FAIL — Restore to HIGH

---

### Section 3 — Failure Modes

**Question**: In what specific situations does this workaround break, lose data, or force re-work?

*Write your one-sentence answer here naming the two most concrete failures*:

> ___

Now transcribe into the table:

| # | Trigger [specific input, volume threshold, or workflow event — not a general category] | What goes wrong | User-visible symptom [observable without reading a log] | Estimated frequency |
|---|----------------------------------------------------------------------------------------|-----------------|--------------------------------------------------------|---------------------|
| FM-01 | | | | |
| FM-02 | | | | |
| FM-03 (optional) | | | | |

**Column contract**: "Trigger" must be specific enough that a developer could write a test for it.
"User-visible symptom" must be something the user sees or experiences, not an internal error state.
"Manual is slow" in any cell does not satisfy either contract.

**Self-score C-05** (Failure modes identified):
- [ ] PASS — At least 2 rows with specific trigger and observable user-visible symptom
- [ ] FAIL — Return and make triggers and symptoms concrete

---

### Section 4 — Conditions Under Which Inertia Loses

**Question**: Under what observable conditions does a [specific team type] stop tolerating the
workaround and adopt the feature instead?

*Write your one-sentence answer here naming the trigger and the team type*:

> ___

Now transcribe into the table:

| # | Observable trigger [falsifiable — a third party can confirm whether this has occurred] | Team type [specific role or team context — not "all users" or "teams"] | Linked failure mode | Consequence if trigger is not reached |
|---|----------------------------------------------------------------------------------------|------------------------------------------------------------------------|---------------------|---------------------------------------|
| DC-01 | Teams switch when... | | FM-__ | |
| DC-02 | Teams switch when... | | FM-__ / External | |
| DC-03 (optional) | | | | |

**Falsifiability check**: For each DC row, ask: "could a third party observe whether this threshold
has been crossed?" If no, rewrite the trigger until yes. "When they see value" fails. "When FM-01
recurs twice in one sprint" passes.

**Self-score C-04** (Why inertia loses):
- [ ] PASS — At least 2 conditions with falsifiable triggers referencing observable events
- [ ] FAIL — Return and add observable thresholds

**Self-score R-01** (Trigger scoped to team type):
- [ ] PASS — At least one condition names a specific team type or role context
- [ ] FAIL — Return and scope at least one condition

**Self-score R-02** (Role-level precision throughout):
- [ ] PASS — Every actor named in Sections 1 and 4 is a role, not a department
- [ ] FAIL — Return to failing section and correct

---

### Section 5 — Composite Gate

| Criterion | Section | Result | Return to if FAIL |
|-----------|---------|--------|-------------------|
| C-01 Workaround mapped in detail | 1 | PASS / FAIL | Section 1 |
| C-02 Switching costs quantified | 2 | PASS / FAIL | Section 2 |
| C-03 Inertia threat HIGH | 2 | PASS / FAIL | Section 2 |
| C-05 Failure modes with specific trigger + symptom | 3 | PASS / FAIL | Section 3 |
| C-04 Why inertia loses — falsifiable conditions | 4 | PASS / FAIL | Section 4 |
| R-01 Trigger scoped to team type | 4 | PASS / FAIL | Section 4 |
| R-02 Role-level precision | 1, 4 | PASS / FAIL | Section 1 or 4 |
| R-03 At least one cost cited to role with basis | 2 | PASS / FAIL | Section 2 |
| **All essential pass (C-01 through C-05)?** | — | YES / NO | Revise before finalizing |

**A-03 — Gate function**: This table is a completion blocker, not an advisory score. If any
essential criterion (C-01 through C-05) shows FAIL, return to the named section and revise before
marking this artifact done. Do not finalize an artifact with an essential FAIL.

---

*End V-01*

---

## V-02 — Team-Segmented with Synthesis (R2 V-02 Repair)

**Variation axis**: Team segmentation as first-class structural axis, with a mandatory synthesis
section that consolidates both passes into a single unified "why inertia loses" answer.

**Hypothesis**: R2 V-02 failed C-04 because the two-pass structure produced defeat conditions
scoped per team type but had no section that synthesized them into a shared falsifiable statement.
A mandatory synthesis section with its own C-04 self-score gate closes the split. The synthesis
section must reference DC rows from both passes by ID, state which team type adopts first and why,
and produce at least two consolidated conditions that a third party could observe across either
segment. The two-pass structure is preserved because it structurally satisfies R-01 (team type is
the organizing axis), but it now feeds into a section that directly answers C-04.

---

You are running `scout-inertia`. This analysis runs in two passes — one per team type — then
synthesizes into a single answer to the central question: **why does inertia lose?**

A universal analysis obscures the segmentation that drives adoption planning. But segmentation
without synthesis fails to answer the question. Do both.

---

### Step 0 — Name the two team types

Before starting, identify the two team types most relevant to this feature. These are the two
populations whose current workaround you will analyze.

- **Primary team type** (the segment with the highest switching friction): ___
- **Secondary team type** (the segment most likely to adopt first): ___

---

### Shared Workaround (complete once — applies to both team types unless they diverge)

| Field | Value |
|-------|-------|
| Workaround name | |
| Tool / file type / process | |
| Data or action handled | |
| Output artifact | |

*If the two team types use fundamentally different workarounds, treat them as separate analyses
with a note explaining the divergence.*

---

### Pass A — Primary team type: [fill from Step 0]

#### A1 — Workaround Actor

| Field | Value |
|-------|-------|
| Who performs the workaround [role — not department, not "users"] | |
| Frequency for this team type | |
| Volume or scale context | |

**A-04 — Role precision gate**: If "Who performs" contains "teams", "users", "people", or a
department name, rewrite it as a role before continuing Pass A. The role named here must appear
in A2 costs and A3 defeat conditions.

**Self-score C-01 (Pass A)**:
- [ ] PASS — Named workaround, role actor, frequency, and output artifact present
- [ ] FAIL — Return to shared workaround or A1 and add specifics

#### A2 — Switching Costs for Primary Team Type

| Dimension | Estimate [number or range] | Unit | Basis / assumption |
|-----------|---------------------------|------|--------------------|
| Time to migrate and ramp | | hours or days per [role from A1] | |
| Training | | hours per [role from A1] | |
| Workflow disruption | | sprint-days or people affected | |

At least one Basis cell must carry an anchor (comparable migration, stated assumption, or explicit
uncertainty range). "~4 hours (based on similar CSV-to-tool onboarding)" passes. Empty basis is
not acceptable when both other cells carry unsupported estimates.

**Self-score C-02 (Pass A)**:
- [ ] PASS — At least 2 of 3 Estimate cells carry a number or range
- [ ] FAIL — Return and quantify

**Self-score R-03 (Pass A)**:
- [ ] PASS — At least one Basis cell carries an anchor
- [ ] FAIL — Add at least one anchor

#### A3 — Failure Modes for Primary Team Type

| # | Trigger [specific input, volume, or workflow event] | What goes wrong | User-visible symptom [observable without a log] | Recovery cost |
|---|------------------------------------------------------|-----------------|------------------------------------------------|---------------|
| FM-A01 | | | | |
| FM-A02 | | | | |

"Specific trigger" means a developer could write a test for it. "User-visible symptom" means the
user sees it without reading an error log. Generic pain points fail both columns.

**Self-score C-05 (Pass A)**:
- [ ] PASS — At least 2 rows with specific trigger and observable symptom
- [ ] FAIL — Return and make concrete

#### A4 — Defeat Conditions for Primary Team Type

| # | Observable trigger [falsifiable] | Linked failure mode | Falsifiable? |
|---|----------------------------------|---------------------|--------------|
| DC-A01 | Teams switch when... | FM-A__ | YES / NO |
| DC-A02 | Teams switch when... | FM-A__ / External | YES / NO |

All entries in "Falsifiable?" must be YES. If NO, rewrite until a third party could observe whether
the threshold has been crossed.

---

### Pass B — Secondary team type: [fill from Step 0]

#### B1 — Workaround Actor

| Field | Value |
|-------|-------|
| Who performs the workaround [role — not department] | |
| Frequency for this team type | |
| Volume or scale context | |

**A-04 — Role precision gate**: Same rule — role, not department. Correct before continuing.

**Self-score C-01 (Pass B)**:
- [ ] PASS — Role actor, frequency, and volume context present
- [ ] FAIL — Return and add specifics

#### B2 — Switching Costs for Secondary Team Type

| Dimension | Estimate [number or range] | Unit | Basis / assumption |
|-----------|---------------------------|------|--------------------|
| Time to migrate and ramp | | hours or days per [role from B1] | |
| Training | | hours per [role from B1] | |
| Workflow disruption | | sprint-days or people affected | |

**Self-score C-02 (Pass B)**:
- [ ] PASS — At least 2 of 3 Estimate cells carry a number or range
- [ ] FAIL — Return and quantify

**Self-score R-03 (Pass B)**:
- [ ] PASS — At least one Basis cell carries an anchor
- [ ] FAIL — Add at least one anchor

#### B3 — Failure Modes for Secondary Team Type

| # | Trigger [specific input, volume, or workflow event] | What goes wrong | User-visible symptom | Recovery cost |
|---|------------------------------------------------------|-----------------|----------------------|---------------|
| FM-B01 | | | | |
| FM-B02 | | | | |

**Self-score C-05 (Pass B)**:
- [ ] PASS — At least 2 rows with specific trigger and observable symptom
- [ ] FAIL — Return and make concrete

#### B4 — Defeat Conditions for Secondary Team Type

| # | Observable trigger [falsifiable] | Linked failure mode | Falsifiable? |
|---|----------------------------------|---------------------|--------------|
| DC-B01 | Teams switch when... | FM-B__ | YES / NO |
| DC-B02 | Teams switch when... | FM-B__ / External | YES / NO |

---

### Inertia Threat Score

**Score**: HIGH *(default — reduce only with documented evidence of active abandonment already
underway independent of this feature)*

| Field | Value |
|-------|-------|
| Score | HIGH |
| Primary reason | |
| Mitigating factor (only complete if not HIGH) | n/a |

**Self-score C-03**:
- [ ] PASS — Score is HIGH, or mitigation is documented with named evidence
- [ ] FAIL — Restore to HIGH

---

### Synthesis — Why Inertia Loses (C-04 gate)

*This section is mandatory. Do not skip it.*

Answer the following in three to five sentences, referencing defeat conditions by ID (DC-A01,
DC-B01, etc.) and failure modes by ID (FM-A01, FM-B01, etc.):

1. Under what condition does the primary team type (Pass A) abandon the workaround? Which defeat
   condition tips them — and what must the feature provide to reach that condition?

2. Under what condition does the secondary team type (Pass B) abandon the workaround? Is their
   adoption threshold lower or higher than the primary team type, and why?

3. Which team type adopts first? State the observable marker that would confirm this prediction.

Your synthesis must produce at least two consolidated, falsifiable conditions — one per team type.
"When they see the value" does not qualify in either sentence.

**Self-score C-04** (Why inertia loses — synthesis):
- [ ] PASS — At least 2 team-type-scoped falsifiable conditions stated in synthesis prose, referencing DC IDs
- [ ] FAIL — Return and rewrite synthesis until conditions are falsifiable and team-scoped

**Self-score R-01** (Trigger scoped to team type):
- [ ] PASS — Synthesis names specific team type for each condition (structurally satisfied by Pass A / Pass B)
- [ ] FAIL — n/a if synthesis references DC-A and DC-B IDs

---

### Composite Gate

| Criterion | Pass A | Pass B | Synthesis | Return to if FAIL |
|-----------|--------|--------|-----------|-------------------|
| C-01 Workaround mapped | PASS/FAIL | PASS/FAIL | — | A1 or B1 |
| C-02 Costs quantified | PASS/FAIL | PASS/FAIL | — | A2 or B2 |
| R-03 Basis cited | PASS/FAIL | PASS/FAIL | — | A2 or B2 |
| C-03 Inertia HIGH | — | — | PASS/FAIL | Inertia score section |
| C-05 Failure modes | PASS/FAIL | PASS/FAIL | — | A3 or B3 |
| C-04 Why inertia loses | — | — | PASS/FAIL | Synthesis section |
| R-01 Team type scoped | YES (structural) | YES (structural) | — | — |
| R-02 Role precision | PASS/FAIL | PASS/FAIL | — | A1 or B1 |
| **All essential pass?** | — | — | YES / NO | Revise before finalizing |

**A-03 — Gate function**: All essential criteria (C-01 through C-05) must pass for both segments
and the synthesis. If any cell shows FAIL, return to the named section. This gate is a completion
blocker. Recommended criteria (R-01, R-02, R-03) failures are advisory.

---

*End V-02*

---

## V-03 — Failure-First with Explicit C-01 Gate (R2 V-04 Repair)

**Variation axis**: Inverted lifecycle — begin with failure mode discovery, work backward to the
workaround, then forward to costs and defeat conditions. Same inversion as R2 V-04, but with an
explicit C-01-quality self-score gate on the workaround reconstruction step.

**Hypothesis**: R2 V-04 failed C-01 because the reconstruction table ("what do the failures
reveal?") was framed as inference rather than declaration. The analyst was asked to describe the
workaround *from* the failure evidence, but the frame was too open-ended — what emerged was a
picture of failure, not a C-01-quality workaround map with role, frequency, and output artifact
declared. Replacing the reconstruction table with a formal declaration step — with an explicit
C-01 self-score that quotes the pass conditions — forces the analyst to produce a complete
workaround profile regardless of the lifecycle order. If they cannot pass C-01 from the failure
evidence, they must return to Step 1 and find more specific failures.

---

You are running `scout-inertia`. Start from the cracks.

If you can find where the current workaround fails, you understand it better than someone who
describes it from the happy path. Start with specific failure modes. Let the failures reveal the
workaround. Then declare it explicitly.

Do not describe the workaround in Step 1. Find where it breaks first.

---

### Step 1 — Find the Failure Modes

Think like a tester trying to make the workaround fail. For each failure mode:

| # | What breaks | Specific trigger [concrete input, volume threshold, or workflow event — not a category] | User-visible symptom [observable without reading a log] | How often [estimate with basis, or acknowledged uncertainty range] | Recovery cost |
|---|-------------|----------------------------------------------------------------------------------------|--------------------------------------------------------|-------------------------------------------------------------------|---------------|
| FM-01 | | | | | |
| FM-02 | | | | | |
| FM-03 (optional) | | | | | |

**Column contract**: "Specific trigger" means a developer could write a test for it. "How often"
must carry an estimate or acknowledge uncertainty ("unknown; estimating wide: monthly to daily").
Generic pain points ("it's slow", "it doesn't scale") do not satisfy either column.

If you cannot find at least two failure modes, examine the workaround from the perspective of a
user who has been burned by it — not one who just learned it. The failures are there; find them.

**Self-score C-05** (Failure modes identified):
- [ ] PASS — At least 2 rows with specific trigger and observable user-visible symptom
- [ ] FAIL — Return here and make triggers and symptoms concrete before Step 2

---

### Step 2 — Declare the Workaround (C-01 gate)

The failure modes you found reveal what the workaround is. Now declare it formally.

| Field | Declare explicitly |
|-------|-------------------|
| Workaround name | |
| Tool / file type / process | |
| Data or action handled | |
| Who performs it [role — not department, not "users"; the failures point to who is responsible] | |
| Frequency [at what interval do the failure modes occur? That is the operating frequency] | |
| Output artifact [what does the workaround normally produce before it fails?] | |

**A-04 — Role precision gate**: Read the "Who performs it" cell. If it contains "teams", "users",
"people", or a department name, rewrite it as a role before continuing. The failures from Step 1
reveal who is responsible — use that to name the role precisely. Only continue to Step 3 once the
cell names a role.

**Self-score C-01** (Workaround mapped in detail):

The pass conditions for C-01 are: (a) specific tool or process named, (b) role actor named,
(c) frequency stated, (d) output artifact named.

- [ ] PASS — All four elements present; the workaround is described with enough specificity that a
  new hire could identify it from this table
- [ ] FAIL — Return to Step 1 and find more specific failure modes; the failures will reveal the
  missing elements (actor role emerges from "who is affected", frequency from "how often FM-01
  occurs", output artifact from "what gets corrupted or lost")

*If FAIL: the reconstruction from failure evidence is incomplete. Either your failure modes are
not specific enough (return to Step 1) or you are inferring from thin evidence (add a third
failure mode with a more concrete trigger).*

---

### Step 3 — Quantify the Switching Cost

Now that the workaround is declared, estimate what it costs a [role from Step 2] to abandon it.

| Dimension | Estimate [number or range — "high"/"low" not accepted] | Unit | Basis / assumption [analogy, comparable, stated assumption, or explicit uncertainty] |
|-----------|--------------------------------------------------------|------|--------------------------------------------------------------------------------------|
| Time to migrate and ramp | | hours or days per [role] | |
| Training | | hours per [role] | |
| Workflow disruption | | sprint-days or number of people affected | |

**Inertia threat score**: HIGH *(default — reduce only with documented evidence that the
workaround is being actively abandoned independent of this feature)*

**Self-score C-02** (Costs quantified):
- [ ] PASS — At least 2 of 3 Estimate cells carry a number or range
- [ ] FAIL — Return and quantify

**Self-score R-03** (At least one cost cited):
- [ ] PASS — At least one Basis cell carries an anchor (analogy, comparable, or stated assumption)
- [ ] FAIL — Add at least one anchor

**Self-score C-03** (Inertia HIGH):
- [ ] PASS — Score stated as HIGH, or mitigation documented
- [ ] FAIL — Restore to HIGH

---

### Step 4 — Map Defeat Conditions from Failure Modes

Each failure mode found in Step 1 is a potential defeat condition. For each, identify the
threshold at which the failure becomes intolerable enough to trigger a switch.

| # | Defeat condition | Source failure mode | Team type this applies to [specific role or context] | Falsifiable? |
|---|------------------|---------------------|------------------------------------------------------|--------------|
| DC-01 | Teams switch when... | FM-__ | | YES / NO |
| DC-02 | Teams switch when... | FM-__ / External | | YES / NO |
| DC-03 (optional) | | | | |

**Column contracts**:
- "Defeat condition" must be falsifiable — a third party can observe whether the threshold was crossed
- "Team type" must name a specific team or role context; universal triggers hide adoption segmentation
- All entries in "Falsifiable?" must be YES — rewrite any NO entry before continuing

**External forcing functions**: Also consider conditions not tied to a failure mode — regulatory
change, platform deprecation, key-person departure, competitive event. Add as DC rows with
"External" in the source column.

**Self-score C-04** (Why inertia loses):
- [ ] PASS — At least 2 conditions with falsifiable triggers
- [ ] FAIL — Return and rewrite vague conditions

**Self-score R-01** (Trigger scoped to team type):
- [ ] PASS — At least one DC row names a specific team type or role context
- [ ] FAIL — Return and scope at least one condition

**Self-score R-02** (Role-level precision):
- [ ] PASS — Every actor in Steps 2 and 4 is a role, not a department
- [ ] FAIL — Return to failing step and correct

---

### Step 5 — Verdict

Write two to four sentences: why does inertia lose? Reference failure modes and defeat conditions
by ID. State what the feature must provide to tip each defeat condition. If none of the conditions
are currently met, say so — inertia wins until they are.

---

### Composite Gate

| Criterion | Step | Result | Return to if FAIL |
|-----------|------|--------|-------------------|
| C-05 Failure modes (specific trigger + symptom) | 1 | PASS / FAIL | Step 1 |
| C-01 Workaround declared (tool, role, frequency, artifact) | 2 | PASS / FAIL | Step 2 → Step 1 if blocked |
| C-02 Costs quantified | 3 | PASS / FAIL | Step 3 |
| R-03 Basis cited | 3 | PASS / FAIL | Step 3 |
| C-03 Inertia HIGH | 3 | PASS / FAIL | Step 3 |
| C-04 Defeat conditions falsifiable | 4 | PASS / FAIL | Step 4 |
| R-01 Team type scoped | 4 | PASS / FAIL | Step 4 |
| R-02 Role precision | 2, 4 | PASS / FAIL | Step 2 or 4 |
| **All essential pass (C-01 through C-05)?** | — | YES / NO | Revise before finalizing |

**A-03 — Gate function**: This table is a completion blocker. If any essential criterion shows
FAIL, return to the named step. Note that C-01 FAIL in Step 2 redirects to Step 1 — the
workaround declaration cannot be completed until the failure modes are specific enough to reveal
its actor, frequency, and output artifact.

---

*End V-03*

---

## V-04 — Adversarial Advocate / Rebuttal

**Variation axis**: Inertia framing — the analysis is structured in two voices. Section 1 writes
the best case for inertia winning. Section 2 rebuts it. Defeat conditions emerge from the
rebuttal, not from a neutral analysis.

**Hypothesis**: Standard inertia analysis frames inertia as the obstacle to defeat, which biases
the analyst toward underestimating it. When asked to argue for inertia winning — to write its
strongest case — the analyst surfaces the workaround's genuine strengths, the real switching costs,
and the conditions under which users would never switch. The rebuttal must address each advocate
argument by name. This adversarial framing produces stronger defeat conditions (C-04) because they
must defeat specific arguments rather than generic inertia, and more precise failure modes (C-05)
because they are the advocate's vulnerabilities. A rebuttal that cannot name what it is rebutting
fails; the advocate case must be specific enough to produce specific rebuttals.

---

You are running `scout-inertia`. This analysis runs in two voices:

**Voice 1 — The Advocate** argues the case for inertia winning. It makes the best, most honest
argument for why teams will never switch. It names the real costs, the real switching friction,
the real reasons the workaround is good enough.

**Voice 2 — The Rebuttal** answers each advocate argument. It names the specific conditions under
which each advocate argument fails. These become the defeat conditions.

A rebuttal that says "but the feature is better" without naming what makes the advocate argument
fail does not pass. A rebuttal must be adversarially stronger than the advocate case — or inertia
wins.

---

### Section 1 — The Advocate Case (argue for inertia winning)

Write the strongest honest case for why teams will keep the workaround.

Complete the workaround profile as part of the advocate case — you are arguing why it is good
enough, so you must name it precisely.

**Workaround identity** (complete as part of arguing its case):

| Field | Value |
|-------|-------|
| Workaround name | |
| Tool / file type / process | |
| Data or action handled | |
| Who performs it [role — not department: "PM", "DevOps engineer"] | |
| Frequency | |
| Output artifact | |

**A-04 — Role precision gate**: If "Who performs it" names a department or vague population,
rewrite it as a role before continuing. A weak advocate names vague actors — a strong advocate
knows exactly who bears the switching cost.

**Advocate arguments** (why inertia wins — be honest and specific):

| # | Advocate argument | What makes it sticky | Quantified switching cost |
|---|------------------|----------------------|---------------------------|
| ARG-01 | [Name the first reason teams stay] | [What makes this reason hard to overcome] | [number + unit + basis] |
| ARG-02 | [Name the second reason teams stay] | [What makes this reason hard to overcome] | [number + unit + basis] |
| ARG-03 (optional) | | | |

**Column contract**: "Advocate argument" must be a specific reason — "the workaround already
integrates with their reporting tool and re-integration would take 2 sprints" passes. "It works"
fails. "Quantified switching cost" must carry a number — "high" does not pass.

**Inertia threat score**: HIGH *(the advocate is winning this section by design)*

**Self-score C-01** (Workaround profile complete):
- [ ] PASS — Named workaround, role actor, frequency, and output artifact all present in the profile
- [ ] FAIL — Return and complete the profile; the advocate cannot argue for a workaround it has not named

**Self-score C-02** (Switching costs quantified via ARG table):
- [ ] PASS — At least 2 ARG rows carry a number in "Quantified switching cost"
- [ ] FAIL — Return and quantify at least 2 arguments

**Self-score C-03** (Inertia HIGH):
- [ ] PASS — Inertia threat stated as HIGH
- [ ] FAIL — Restore to HIGH

---

### Section 2 — The Rebuttal (argue for why inertia loses)

For each advocate argument, write a specific rebuttal. The rebuttal must name the failure mode
or external condition that defeats the advocate's claim. "The feature is better" is not a rebuttal.

**Failure modes** (the cracks the advocate did not name):

| # | Trigger [specific input, volume, or event that the advocate case assumed would not happen] | What goes wrong when it does | User-visible symptom | Link to advocate argument |
|---|-------------------------------------------------------------------------------------------|------------------------------|----------------------|---------------------------|
| FM-01 | | | | ARG-__ |
| FM-02 | | | | ARG-__ |

**Rebuttal table**:

| # | Advocate argument | Rebuttal | Defeat condition (falsifiable) | Team type this applies to |
|---|-----------------|----------|-------------------------------|---------------------------|
| REB-01 | [ARG-01 text] | [Why ARG-01 fails under specific conditions] | Teams switch when [observable threshold] | |
| REB-02 | [ARG-02 text] | [Why ARG-02 fails under specific conditions] | Teams switch when [observable threshold] | |
| REB-03 (optional) | | | | |

**Column contract**: "Defeat condition" must be falsifiable — a third party can observe whether
the threshold has been crossed. "When they realize" fails. "When FM-01 recurs three times in one
release cycle" passes. "Team type" must name a specific type, not "all users".

**Self-score C-05** (Failure modes):
- [ ] PASS — At least 2 FM rows with specific trigger and observable symptom
- [ ] FAIL — Return and make failure modes concrete

**Self-score C-04** (Why inertia loses — rebuttals are falsifiable defeat conditions):
- [ ] PASS — At least 2 REB rows carry falsifiable defeat conditions with team type named
- [ ] FAIL — Return and rewrite vague rebuttals as observable thresholds

**Self-score R-01** (Team type scoped):
- [ ] PASS — At least one REB row names a specific team type or role context
- [ ] FAIL — Return and scope at least one condition

**Self-score R-02** (Role precision):
- [ ] PASS — Actor in Section 1 profile is a role; team types in REB table are specific
- [ ] FAIL — Return to Section 1 profile or REB table and correct

**Self-score R-03** (At least one cost cited):
- [ ] PASS — At least one ARG row Basis field carries an anchor (analogy, comparable, or assumption)
- [ ] FAIL — Return to Section 1 ARG table and add at least one basis anchor

---

### Section 3 — Verdict

Write two to three sentences: state which advocate arguments inertia loses and under what
conditions. Reference REB IDs and FM IDs. State which team type encounters the defeat condition
first, and what makes that prediction falsifiable.

---

### Composite Gate

| Criterion | Section | Result | Return to if FAIL |
|-----------|---------|--------|-------------------|
| C-01 Workaround mapped | 1 | PASS / FAIL | Section 1 profile |
| C-02 Costs quantified | 1 ARG table | PASS / FAIL | Section 1 ARG table |
| R-03 At least one cost cited | 1 ARG table | PASS / FAIL | Section 1 ARG table |
| C-03 Inertia HIGH | 1 | PASS / FAIL | Section 1 inertia score |
| C-05 Failure modes | 2 FM table | PASS / FAIL | Section 2 FM table |
| C-04 Why inertia loses (falsifiable rebuttals) | 2 REB table | PASS / FAIL | Section 2 REB table |
| R-01 Team type scoped | 2 REB table | PASS / FAIL | Section 2 REB table |
| R-02 Role precision | 1, 2 | PASS / FAIL | Section 1 or 2 |
| **All essential pass (C-01 through C-05)?** | — | YES / NO | Revise before finalizing |

**A-03 — Gate function**: If any essential criterion shows FAIL, return to the named section.
The rebuttal case (Section 2) cannot produce strong defeat conditions unless the advocate case
(Section 1) named specific arguments with specific costs. If C-01 or C-02 fail in Section 1,
revise Section 1 first — the quality of Section 2 depends on the quality of Section 1.

---

*End V-04*

---

## V-05 — Progressive Commitment Chain

**Variation axis**: Forward-reference enforcement — each section declares named commitments
(role ID, workaround ID, failure mode IDs) that all subsequent sections must honor by reference.
An entry in Section 4 that does not cite a failure mode ID from Section 3 is structurally
incomplete, not just instructionally vague.

**Hypothesis**: In R2 variations, defeat conditions could be written without reference to specific
failure modes, and costs could be stated without naming the role who pays them. This produced
syntactically valid outputs where the defeat conditions floated free of the failure evidence. A
forward-reference requirement creates a dependency chain: you cannot write DC-01 without citing
FM-01 or FM-02; you cannot write a cost without naming ACTOR-01. Incoherence becomes visible —
an analyst cannot write a generic defeat condition without first going back to find a failure mode
it is derived from. The commitment chain incidentally enforces R-02 (role cited in every cost),
R-03 (cost grounded in role-specific basis), and R-01 (team type carried forward to defeat
conditions by the same ID discipline).

---

You are running `scout-inertia`. This analysis uses a commitment chain.

**How the chain works**: Each section declares named identifiers. Subsequent sections must
reference those identifiers by name. You cannot use "the role" — use ACTOR-01. You cannot use
"a failure" — use FM-01. This makes cross-section coherence visible: a defeat condition that
does not cite a failure mode ID does not yet have an evidence anchor.

---

### Step 1 — Declare the Core Identifiers

Before any analysis, name the primary actors and the workaround. These become the identifiers
all subsequent sections reference.

| ID | Type | Value |
|----|------|-------|
| ACTOR-01 | Role [not department] | |
| ACTOR-02 (optional — secondary role) | Role [not department] | |
| WA-01 | Workaround name | |
| WA-01-tool | Tool / file type / process | |
| WA-01-output | Output artifact | |
| WA-01-freq | How often ACTOR-01 runs WA-01 | |

**A-04 — Role precision gate**: ACTOR-01 must be a role. If it contains "teams", "users",
"people", or a department name, replace it before continuing. Every subsequent section references
ACTOR-01 — a vague actor corrupts the entire chain.

**Self-score C-01** (Workaround mapped — identifiers declared):
- [ ] PASS — WA-01, WA-01-tool, WA-01-output, WA-01-freq, and ACTOR-01 all declared with specific values
- [ ] FAIL — Return and complete the identifier table before Step 2

---

### Step 2 — Quantify the Cost to ACTOR-01

Using ACTOR-01 as the unit of cost:

| Dimension | Estimate for ACTOR-01 [number or range] | Unit | Basis / assumption |
|-----------|----------------------------------------|------|--------------------|
| Time to migrate ACTOR-01 from WA-01 | | hours or days per ACTOR-01 | |
| Training cost per ACTOR-01 | | hours per ACTOR-01 | |
| Workflow disruption | | sprint-days or number of ACTOR-01s affected | |

Every row must name ACTOR-01 in the Unit cell — a floating number with no named actor is a
type error in this chain. If ACTOR-02 bears a different cost profile, add a second row set
labeled ACTOR-02.

**Inertia threat score**: HIGH *(default — reduce only with documented evidence of active
abandonment already underway)*

**Self-score C-02** (Costs quantified):
- [ ] PASS — At least 2 of 3 Estimate cells carry a number or range, each named to ACTOR-01
- [ ] FAIL — Return and quantify; name ACTOR-01 in each unit

**Self-score R-03** (At least one cost cited):
- [ ] PASS — At least one Basis cell carries an anchor (analogy, comparable, or stated assumption)
- [ ] FAIL — Add at least one anchor

**Self-score C-03** (Inertia HIGH):
- [ ] PASS — Score stated as HIGH, or mitigation documented with named evidence
- [ ] FAIL — Restore to HIGH

---

### Step 3 — Declare the Failure Mode Identifiers

Name the specific points where WA-01 breaks. These IDs will be cited in Step 4.

| ID | Trigger [specific input, volume, or workflow event that causes WA-01 to fail] | What goes wrong in WA-01 | User-visible symptom [observable without a log] | Applies to which ACTOR |
|----|------------------------------------------------------------------------------|--------------------------|------------------------------------------------|------------------------|
| FM-01 | | | | ACTOR-01 / ACTOR-02 |
| FM-02 | | | | ACTOR-01 / ACTOR-02 |
| FM-03 (optional) | | | | |

**Column contract**: "Trigger" must be specific enough that a developer could write a test for it.
"User-visible symptom" must be something the user observes without reading an error log.
"Applies to which ACTOR" must reference ACTOR-01 or ACTOR-02 from Step 1 — not "users".

**Self-score C-05** (Failure modes identified):
- [ ] PASS — At least 2 FM rows with specific trigger, observable symptom, and named ACTOR
- [ ] FAIL — Return and make triggers and symptoms concrete

---

### Step 4 — Map Defeat Conditions from FM and ACTOR Identifiers

Each defeat condition must cite at least one FM ID and one team type. A defeat condition with no
FM citation has no evidence anchor — it is a hypothesis without a root cause.

| # | Defeat condition — "ACTOR-0X switches when [falsifiable threshold]" | Source FM IDs | Team type [specific — must name a role context, not "all users"] | External forcing function? |
|---|---------------------------------------------------------------------|---------------|------------------------------------------------------------------|---------------------------|
| DC-01 | ACTOR-__ switches when... | FM-__ | | YES / NO |
| DC-02 | ACTOR-__ switches when... | FM-__ / FM-__ | | YES / NO |
| DC-03 (optional) | | | | |

**Chain validation**: Before marking each row complete, confirm:
1. The ACTOR ID in "Defeat condition" matches a declared ID from Step 1
2. The FM ID(s) in "Source FM IDs" match declared IDs from Step 3
3. The team type is specific — if it's generic, it will not survive rollout planning

**External forcing functions**: If a defeat condition is not derived from a failure mode (e.g.,
regulatory change, platform deprecation, competitive event), mark "External forcing function?" as
YES and describe the external trigger in the defeat condition cell.

**Self-score C-04** (Why inertia loses — citations present):
- [ ] PASS — At least 2 DC rows with falsifiable conditions citing FM IDs
- [ ] FAIL — Return and rewrite conditions that cannot cite a source FM

**Self-score R-01** (Team type scoped):
- [ ] PASS — At least one DC row names a specific team type or role context
- [ ] FAIL — Return and scope at least one condition

**Self-score R-02** (Role precision — chain complete):
- [ ] PASS — Every ACTOR reference in Steps 2, 3, and 4 traces back to a declared ID in Step 1
- [ ] FAIL — Return to the step where the chain broke and correct

---

### Step 5 — Verdict

Write two to three sentences using only declared identifiers. Name the ACTOR IDs, FM IDs, and
DC IDs that answer the central question: why does inertia lose?

Example form: "Inertia loses when [FM-01] or [FM-02] triggers DC-01 for ACTOR-01. The feature
must [specific capability] to reach this threshold. If this threshold is not met, inertia wins."

If no DC condition is currently met, say so. Do not claim inertia loses if you cannot trace the
path from a failure mode ID to a defeat condition ID.

---

### Composite Gate

| Criterion | Step | Result | Return to if FAIL |
|-----------|------|--------|-------------------|
| C-01 Identifiers declared (workaround, actor, frequency, artifact) | 1 | PASS / FAIL | Step 1 |
| C-02 Costs quantified and named to ACTOR-01 | 2 | PASS / FAIL | Step 2 |
| R-03 At least one cost cited with basis | 2 | PASS / FAIL | Step 2 |
| C-03 Inertia HIGH | 2 | PASS / FAIL | Step 2 |
| C-05 Failure modes with trigger, symptom, and ACTOR | 3 | PASS / FAIL | Step 3 |
| C-04 Defeat conditions citing FM IDs (falsifiable) | 4 | PASS / FAIL | Step 4 |
| R-01 Team type scoped | 4 | PASS / FAIL | Step 4 |
| R-02 Role precision — chain traced | 1, 2, 3, 4 | PASS / FAIL | First broken step |
| **All essential pass (C-01 through C-05)?** | — | YES / NO | Revise before finalizing |

**A-03 — Gate function**: If any essential criterion shows FAIL, return to the named step. For
R-02 failures, the chain validation in Step 4 names the exact step where the chain broke.
Note: C-01 failure in Step 1 propagates — all downstream steps depend on the declared identifiers.
Correct Step 1 before any other revision.

---

*End V-05*

---

*End of V-01 through V-05 — scout-inertia R3*

## Coverage Summary

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 essential | Y | Y | Y (gate on reconstruction) | Y | Y |
| C-02 essential | Y | Y | Y | Y | Y (named to ACTOR-ID) |
| C-03 essential | Y | Y | Y | Y | Y |
| C-04 essential | Y | Y (synthesis section) | Y | Y (rebuttal table) | Y (FM citation required) |
| C-05 essential | Y | Y | Y | Y (FM table in rebuttal) | Y |
| R-01 team type | Y | Y (structural) | Y | Y | Y |
| R-02 role precision | Y | Y | Y | Y | Y (chain traced) |
| R-03 cited basis | Y | Y | Y | Y (ARG table basis) | Y |
| A-01 per-section gate | Y | Y | Y | Y | Y |
| A-02 column constraints | Y | Y | Y | Y | Y |
| A-03 composite gate w/ back-pointers | Y | Y | Y | Y | Y |
| A-04 role precision as continuation gate | Y | Y | Y | Y | Y |
