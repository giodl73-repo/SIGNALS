Written to `simulations/quest/variations/prove-hypothesis-variations-R1-2026-03-14.md`.

---

## Round 1 Variations -- prove-hypothesis

Five complete runnable skill body prompts. Here's the design:

### Single-axis (V-01 through V-03)

**V-01: Output Format** -- Pre-printed tables with required columns for falsification conditions (includes "Observable?" column as C-02 gate), experiments (includes falsification-ID mapping column for C-09 and rank column for C-10). Maximum structural coverage of aspirational criteria.

**V-02: Phrasing Register** -- Conversational, question-driven prose. "What do you believe? What would change your mind?" The control variation. Tests how much rubric compliance flows from guided questions without structural enforcement. Expected to score well on essentials (C-01 through C-05), weakly on C-09/C-10.

**V-03: Inertia Framing** -- Status-quo competitor is F-00, the first pre-printed falsification condition in every hypothesis. Confidence must explicitly address "why is doing nothing insufficient?" before stating the numeric value. Targets C-08 quality (prior-evidence rationale) and an underspecified dimension not yet in the rubric: whether the hypothesis is even competing against the right alternative.

### Combination axes (V-04 through V-05)

**V-04: Role Sequence + Output Format** -- Three roles in sequence: Claimant (declares), Skeptic (challenges observability of each condition with a verdict table before confidence is written), Navigator (plans experiments with rank + risk-rationale columns). The Skeptic gate is the strongest structural enforcement of C-02.

**V-05: Lifecycle Emphasis + Inertia Framing** -- Four explicit phases (Setup / Declare / Challenge / Plan) with checklist-style gates between them. PHASE 3 has explicit read-only access to DECLARE -- making the no-goalpost-movement constraint (C-05) a hard gate condition rather than a section-ordering convention. Inertia is interrogated as a *competing hypothesis* in CHALLENGE, not just a falsification condition.

### Key design decision

C-05 (no goalpost movement) is the rubric's behavioral guarantee but it has no structural analog in most prompt formats -- it's usually enforced only by section ordering. V-04 and V-05 make it a checklist gate item, which is testable on live runs. That's the open research question for R2: does gate-enforcement produce materially cleaner C-05 compliance than ordering-enforcement?

alone achieve rubric compliance without structural enforcement. V-03 is the inertia-framing test:
does adding F-00 as a pre-printed falsification condition raise output quality beyond the rubric?

---

## V-01: Output Format (Table-Structured)

**Axis:** Output format -- falsification conditions and experiments each get a pre-printed table
with required columns. Testability is a column in the falsification table (C-02 structural gate).
Experiment-to-falsification mapping is a column in the experiment table (C-09 structural gate).
Risk rank is a sort instruction on the experiment table (C-10 structural gate).

**Hypothesis:** Pre-printed tables with column-level requirements prevent the most common
failure modes: untestable falsification conditions (C-02), generic experiments (C-04), and
missing experiment-to-falsification mapping (C-09). Each column is a mini-gate. The model
cannot skip a column without leaving a visible blank.

```
You are running /prove-hypothesis. Fill in this structured template.
All section headers are fixed. Declare the hypothesis BEFORE any evidence discussion.
Do not adjust the claim or falsification conditions after the HYPOTHESIS DECLARED gate.

---

## SETUP: PRIOR SIGNALS
[Search simulations/prove/ for any prior hypothesis, analysis, or synthesis artifacts on this topic.]
Prior signals found: [List files found, or write "None -- starting fresh."]

## HYPOTHESIS DECLARED
[Complete this section before any evidence is discussed. Do not reference scout findings here.]
Claim: [One sentence. State what you believe to be true. Use "is" or "will" -- not "might" or "could".]

## FALSIFICATION CONDITIONS
[Complete this table before writing the confidence value. Two rows minimum. Conditions must be
observable outcomes, not opinions. "The developer says it was unclear" fails -- name the
observable behavior that would be measured.]

| ID | Condition (the hypothesis is false if this occurs) | Observable? (yes/measurable behavior / no/opinion) |
|----|---------------------------------------------------|-----------------------------------------------------|
| F-01 | [State the condition] | [yes: describe the measurable observation / no: rewrite it] |
| F-02 | [State the condition] | [yes: describe the measurable observation / no: rewrite it] |
[Add F-03 and beyond if needed. Every condition must be marked yes before proceeding.]

## CONFIRMATION CONDITIONS
[What would confirm the hypothesis? One row minimum.]

| ID | Condition (the hypothesis is confirmed if this occurs) |
|----|-------------------------------------------------------|
| CF-01 | [State the positive confirmation criterion] |
[Add CF-02 and beyond if needed.]

## CONFIDENCE
Value: [N]/100
Rationale: [2-3 sentences. Cite at least one specific prior signal, trace finding, or known
friction point from this repo. If no prior signals exist, note "No prior signals -- confidence
is prior-free intuition only." Pure intuition without that note fails.]

## EXPERIMENTS
[List experiments in risk-ranked order -- highest likelihood of falsifying the hypothesis first.
Two rows minimum. Each experiment must name a prove sub-skill, not a generic action.
Valid sub-skills: prove:interview, prove:prototype, prove:analysis, prove:websearch,
prove:publish, prove:synthesize, prove:intelligence.]

| Rank | Experiment | prove sub-skill | Falsification conditions tested |
|------|-----------|-----------------|--------------------------------|
| 1 | [Name and describe the experiment] | prove:[sub-skill] | [F-ID, F-ID] |
| 2 | [Name and describe the experiment] | prove:[sub-skill] | [F-ID, F-ID] |
[Add rows as needed. Rank 1 = highest falsification risk.]

---

Write artifact: simulations/prove/hypothesis/{topic}-hypothesis-{date}.md
Frontmatter: skill, topic, date, claim_summary (one sentence), confidence,
             experiment_count, prior_signals_found (true/false).
```

---

## V-02: Phrasing Register (Conversational)

**Axis:** Phrasing register -- descriptive, question-driven prose replaces imperative directives.
The prompt reads like a thinking partner walking through scientific method, not a compliance
checklist. Questions surface intent before asking for output.

**Hypothesis:** A conversational register lowers the PM audience's friction when the skill is
new to them, at the cost of weaker structural enforcement. The rubric's essential criteria
(C-01 through C-05) can still be met if the questions are specific enough. C-09 and C-10
are aspirational; question-driven prompts may not reach them reliably. This is the control
variation: minimum structural overhead, maximum readability.

```
You are running /prove-hypothesis.

Before looking at any evidence, the goal here is to write down what you believe and commit to
it. Once this artifact exists, the claim and falsification conditions are locked. You will not
adjust them after running experiments -- that is what makes this a real hypothesis instead of
a post-hoc explanation.

---

**Step 1: Check what we already know.**

Look in simulations/prove/ for any prior hypothesis, analysis, or synthesis files on this
topic. If you find them, list them here. If you find nothing, note that explicitly -- this
tells the reader whether the confidence below is backed by prior investigation or is prior-free.

Prior investigation signals: [list files or "None found -- confidence below is prior-free."]

---

**Step 2: State the claim.**

What do you believe? Write one sentence that could, in principle, turn out to be false.
Avoid hedged language like "might" or "could" -- if you believe it, say so directly.

Claim: [one sentence stating what you believe is true]

---

**Step 3: What would prove you wrong?**

Name at least two specific conditions that, if observed, would mean the claim is false.
Each condition should describe an observable outcome -- something you could measure or witness,
not something you would feel or guess. If a condition depends on someone's opinion rather than
a measurable behavior, rewrite it until it doesn't.

The claim is false if:
1. [Observable condition -- describe what you would see, hear, measure]
2. [Observable condition -- describe what you would see, hear, measure]
[Add more if needed]

---

**Step 4: What would prove you right?**

Name at least one condition that would confirm the claim if observed.

The claim is confirmed if:
1. [Observable confirmation condition]

---

**Step 5: How confident are you, and why?**

Give a number from 0 to 100. Then explain why in 2-3 sentences. If you have prior signal
artifacts from Step 1, reference at least one specific finding from them. If you have no
prior signals, say so -- a prior-free confidence of 60 means something different than a
prior-backed confidence of 60.

Confidence: [N]/100
Why: [2-3 sentences with at least one specific anchor -- prior finding, trace result, or
     named friction point. If none: "No prior signals -- this confidence is based on [intuition
     / domain knowledge / first-principles reasoning]."]

---

**Step 6: How will you test this?**

List the experiments you will run. Each experiment should name one of the prove sub-skills --
that way the investigation plan is actionable immediately. Valid sub-skills: prove:interview,
prove:prototype, prove:analysis, prove:websearch, prove:publish, prove:synthesize,
prove:intelligence.

Experiments:
1. [What you will do and why it tests the claim] -- prove:[sub-skill]
2. [What you will do and why it tests the claim] -- prove:[sub-skill]
[Add more if needed. Start with the experiment most likely to falsify the claim.]

---

Write artifact: simulations/prove/hypothesis/{topic}-hypothesis-{date}.md
Frontmatter: skill, topic, date, claim_summary, confidence, experiment_count,
             prior_signals_found (true/false).
```

---

## V-03: Inertia Framing (Status-Quo as F-00)

**Axis:** Inertia framing -- the status-quo is named as F-00, the first falsification
condition in every hypothesis. Before listing any domain-specific falsification conditions,
the skill asks: could the team get equivalent value by doing nothing or continuing current
practice? The confidence value is explicitly calibrated against the status-quo competitor.

**Hypothesis:** The most underspecified element in most hypotheses is the do-nothing
alternative. By pre-printing F-00 as a named, required falsification condition that covers
status-quo sufficiency, the skill forces the PM to compare the claim against inertia rather
than only against a null outcome. This raises the quality of confidence rationale (C-08) and
experiment selection (C-04) because experiments must now include a path that tests whether
the status quo is already sufficient.

```
You are running /prove-hypothesis. Fill in this structured template.
Declare the hypothesis BEFORE any evidence discussion.
The status-quo competitor (F-00) is always the first falsification condition.

---

## SETUP: PRIOR SIGNALS
[Search simulations/prove/ for any prior hypothesis, analysis, or synthesis artifacts on this topic.]
Prior signals found: [List files found, or write "None -- starting fresh."]

## HYPOTHESIS DECLARED
[Write the claim here before any evidence is introduced. No scout findings, no trace references.]
Claim: [One sentence. Use "is" or "will". No hedging.]

## FALSIFICATION CONDITIONS
[F-00 is always the status-quo competitor. Complete it first. Then add domain-specific conditions.]

F-00 (Status-quo competitor): The hypothesis is false if the team can get equivalent value
by continuing what they are already doing -- without this feature, workflow, or artifact.
Observable test: [Describe a specific experiment or observation that would reveal whether
the status quo is sufficient. What would "equivalent value from current practice" look like?]

| ID | Condition (the hypothesis is false if this occurs) | Observable test |
|----|---------------------------------------------------|-----------------|
| F-00 | Status quo is sufficient (see above) | [Described above] |
| F-01 | [Domain-specific falsification condition] | [Observable behavior or measurement] |
| F-02 | [Domain-specific falsification condition] | [Observable behavior or measurement] |
[Add F-03 and beyond if needed.]

## CONFIRMATION CONDITIONS
[What would confirm this -- beyond simply "not false"?]

| ID | Condition (confirmed if this occurs) |
|----|--------------------------------------|
| CF-01 | [Positive confirmation criterion] |

## CONFIDENCE
Value: [N]/100
Rationale: [2-3 sentences. Address two sub-questions:
  (1) Why do you believe the status-quo competitor (F-00) does NOT already satisfy the need?
  (2) What prior signal, trace finding, or friction point anchors the numeric value?
  If no prior signals: "No prior signals. Status-quo calibration based on [reason]."
  Do not omit the F-00 calibration statement.]

## EXPERIMENTS
[List experiments in order: highest falsification risk first. The F-00 test -- whether status
quo is sufficient -- should appear early if the answer is uncertain. Name the prove sub-skill
for each. Valid sub-skills: prove:interview, prove:prototype, prove:analysis, prove:websearch,
prove:publish, prove:synthesize, prove:intelligence.]

| Rank | Experiment | prove sub-skill | Falsification conditions tested |
|------|-----------|-----------------|--------------------------------|
| 1 | [Describe experiment -- why does it carry the most falsification risk?] | prove:[sub-skill] | [F-ID, F-ID] |
| 2 | [Describe experiment] | prove:[sub-skill] | [F-ID, F-ID] |
[Add rows as needed. Include at least one experiment that tests F-00 if F-00 risk is nonzero.]

---

Write artifact: simulations/prove/hypothesis/{topic}-hypothesis-{date}.md
Frontmatter: skill, topic, date, claim_summary, confidence, experiment_count,
             prior_signals_found (true/false), status_quo_risk (HIGH/MEDIUM/LOW -- based on F-00).
```

---

## V-04: Role Sequence + Output Format (Claimant / Skeptic / Navigator)

**Axes:** Role sequence (three explicit roles with pre-printed phase gates) + output format
(structured tables enforce C-02, C-09, C-10 per-column).

**Hypothesis:** Separating claim authorship (Claimant), falsifiability challenge (Skeptic),
and experiment planning (Navigator) creates internal checks that the single-voice format
lacks. The Skeptic must interrogate each falsification condition for observability before
the confidence value is written, enforcing C-02 without a post-hoc review pass. The Navigator
must rank experiments by falsification risk, enforcing C-10. Role gates make it structurally
impossible to write confidence before falsification is challenged, or experiments before
confidence is declared.

```
You are running /prove-hypothesis. Fill in this structured template.
Three roles execute in sequence. Each role gate must complete before the next begins.
Do not adjust the Claimant's claim or falsification conditions after the Skeptic gate.

---

## CLAIMANT: DECLARE
[No evidence references allowed in this section. Declare before examining.]

Prior signals check: [Search simulations/prove/ for prior hypothesis/analysis/synthesis on this topic.
List files found, or write "None -- starting fresh."]

Claim: [One sentence. State what you believe is true. Use "is" or "will".]

Falsification candidates (draft -- Skeptic will challenge these):
- [Condition 1: what would make this false?]
- [Condition 2: what would make this false?]
[Add more. These are drafts -- Skeptic must clear them before they become final.]

## SKEPTIC: CHALLENGE
[Each falsification candidate from CLAIMANT must pass the Skeptic's observability test.
Conditions that depend on subjective opinion or invisible internal states must be rewritten.]

| Candidate | Skeptic verdict | Rewritten (if needed) |
|-----------|----------------|-----------------------|
| [Condition 1 text] | PASS (observable: [how]) / REWRITE | [Rewritten version if verdict is REWRITE] |
| [Condition 2 text] | PASS (observable: [how]) / REWRITE | [Rewritten version if verdict is REWRITE] |
[All candidates must reach PASS before the confidence value is written.]

## SKEPTIC: CONFIRM
[What would confirm the hypothesis? At least one confirmation condition required.]
| ID | Confirmation condition (hypothesis confirmed if this occurs) |
|----|--------------------------------------------------------------|
| CF-01 | [State the positive confirmation criterion] |

## CLAIMANT: CONFIDENCE
[Written after Skeptic gate. Confidence is calibrated to the falsification conditions above,
not to intuition alone.]

Value: [N]/100
Rationale: [2-3 sentences. Reference at least one specific prior signal, trace finding,
or known friction point from this codebase. If none exist: "No prior signals -- confidence
is prior-free. Calibration based on [reasoning]." Do not omit the prior-evidence note.]

## NAVIGATOR: EXPERIMENTS
[Plan the experiments. Every experiment must name a prove sub-skill. Order by falsification
risk: rank 1 carries the highest probability of proving the hypothesis false. Map each
experiment to the falsification conditions it tests (use IDs from Skeptic table above).]

| Rank | Experiment | prove sub-skill | Falsification conditions tested | Why this risk rank |
|------|-----------|-----------------|--------------------------------|--------------------|
| 1 | [Describe the experiment] | prove:[sub-skill] | [F-ID, F-ID] | [Why highest risk] |
| 2 | [Describe the experiment] | prove:[sub-skill] | [F-ID, F-ID] | [Why second risk] |
[Add rows as needed. Minimum two. Cover all falsification conditions across the experiment set.]

---

Write artifact: simulations/prove/hypothesis/{topic}-hypothesis-{date}.md
Frontmatter: skill, topic, date, claim_summary, confidence, experiment_count,
             prior_signals_found (true/false), skeptic_rewrites (count of rewritten conditions).
```

---

## V-05: Lifecycle Emphasis + Inertia Framing

**Axes:** Lifecycle emphasis (explicit phase gates with named gate conditions) + inertia
framing (status-quo hypothesis interrogated as a competing hypothesis in the CHALLENGE phase,
not just as a falsification condition).

**Hypothesis:** Explicit lifecycle phases with hard gate conditions -- not section headers
alone -- enforce the no-goalpost-movement constraint (C-05) most directly. The gate between
DECLARE and CHALLENGE is the structural guarantee: the CHALLENGE phase has read-only access
to the claim and falsification conditions declared in DECLARE. Inertia is framed as a competing
hypothesis (not just a falsification condition) because the skill's real question is often
"do we need to build this at all?" Naming inertia as a competing hypothesis forces the PM to
choose between "X is true" and "doing nothing is equivalent" rather than treating them as
unrelated concerns.

```
You are running /prove-hypothesis.
Four phases execute in order. Each phase gate lists what must be true before the next phase begins.
The DECLARE phase output is LOCKED after the gate. Do not modify claim or conditions in later phases.

---

## PHASE 1: SETUP

Goal: Load context. Establish prior signal state before declaring anything.

Prior signals: [Search simulations/prove/ for any prior hypothesis, analysis, or synthesis
artifacts on this topic. List files found with one-line summaries. Write "None -- starting fresh"
if nothing found.]

Status-quo baseline: [In one sentence, describe what the team or user currently does without
this feature or capability. This is the inertia competitor. It will become the competing
hypothesis in CHALLENGE.]

GATE 1 -- required before DECLARE:
[ ] Prior signal state is declared (found or not found -- not silent)
[ ] Status-quo baseline is written (one sentence minimum)

---

## PHASE 2: DECLARE

Goal: Write the hypothesis. No evidence from SETUP may change the claim structure.
The DECLARE output is locked after GATE 2 -- CHALLENGE and PLAN are read-only on this section.

Claim: [One sentence. Use "is" or "will". No hedging. This is what you believe.]

The claim is false if ANY of:
- F-01: [Falsification condition -- state as an observable outcome, not an opinion]
- F-02: [Falsification condition -- state as an observable outcome, not an opinion]
[Add F-03 and beyond if needed. Each must be observable.]

The claim is confirmed if ANY of:
- CF-01: [Positive confirmation criterion -- what would clearly confirm the claim?]

Confidence: [N]/100
Why: [2-3 sentences. Cite at least one specific anchor from SETUP prior signals or the
     status-quo baseline. If no prior signals: "No prior signals. Confidence prior-free:
     calibrated from [intuition / domain knowledge / status-quo baseline analysis]."
     Do not omit an explicit anchor statement.]

GATE 2 -- required before CHALLENGE:
[ ] Claim is one sentence with no hedging
[ ] At least two falsification conditions present
[ ] Each condition describes an observable outcome (not "they feel confused")
[ ] Confidence value is numeric 0-100 with rationale
[ ] No evidence or findings from future phases referenced here

---

## PHASE 3: CHALLENGE

Goal: Interrogate the hypothesis. Two questions: (1) Is the claim falsifiable as written?
(2) Is the status-quo competitor a plausible alternative hypothesis?

Read-only access to PHASE 2: Do not modify claim or falsification conditions. Record any
observability failures as amendments for after this run -- not retroactive edits.

Falsifiability check:
[For each F-ID from DECLARE, confirm it describes a measurable outcome. If not, flag it.]
| F-ID | Observable? | Note (if flagged) |
|------|-------------|-------------------|
| F-01 | yes / NO -- [reason] | [Suggested rewrite for next run if flagged] |
| F-02 | yes / NO -- [reason] | [Suggested rewrite for next run if flagged] |

Status-quo competing hypothesis:
[The status-quo baseline from SETUP is a competing hypothesis: "The team gets equivalent
value by doing nothing." Address it directly.]
- Is doing nothing a plausible outcome? [yes / no -- and why in one sentence]
- If yes: add as F-00 below and include in experiment plan.
F-00 (if applicable): The hypothesis is false if the team gets equivalent value from current practice -- [describe what "equivalent value from status quo" would look like observably].

GATE 3 -- required before PLAN:
[ ] All F-IDs are observability-checked (flagged conditions noted, not silently removed)
[ ] Status-quo competing hypothesis explicitly addressed

---

## PHASE 4: PLAN

Goal: Assign prove sub-skills to experiments. Order by falsification risk. Map to F-IDs.

[Rank 1 = highest probability of falsifying the hypothesis. Include F-00 if it was added in
CHALLENGE. Valid sub-skills: prove:interview, prove:prototype, prove:analysis, prove:websearch,
prove:publish, prove:synthesize, prove:intelligence.]

| Rank | Experiment | prove sub-skill | Falsification conditions tested | Risk rationale |
|------|-----------|-----------------|--------------------------------|----------------|
| 1 | [Describe experiment] | prove:[sub-skill] | [F-00, F-01, ...] | [Why rank 1?] |
| 2 | [Describe experiment] | prove:[sub-skill] | [F-01, F-02, ...] | [Why rank 2?] |
[Add rows as needed. Every falsification condition must be covered by at least one experiment.]

---

Write artifact: simulations/prove/hypothesis/{topic}-hypothesis-{date}.md
Frontmatter: skill, topic, date, claim_summary, confidence, experiment_count,
             prior_signals_found (true/false), status_quo_risk (HIGH/MEDIUM/LOW),
             falsifiability_flags (count of observability flags from CHALLENGE).
```

---

## Round 1 Design Notes

### Variation axis selection

Three single-axis variations chosen from the five candidate axes:

- **Output format** (V-01): Highest structural coverage of aspirational criteria C-09/C-10.
  Pre-printed table columns make mapping and risk-ranking unavoidable. Chosen as the
  "maximum structural enforcement" baseline for single-axis.

- **Phrasing register** (V-02): Control variation. Tests whether question-driven prose
  achieves rubric compliance without structural enforcement. Expected to score well on
  essential criteria (C-01 through C-05) and weakly on aspirational (C-09/C-10). Its
  score reveals how much structural enforcement is actually needed.

- **Inertia framing** (V-03): Addresses the gap not in the rubric but visible in the trace:
  most hypotheses never test whether the status quo is already sufficient. F-00 as a
  pre-printed condition forces the comparison. Expected to raise C-08 quality (confidence
  rationale) and C-04 quality (experiments that include a status-quo validity test).

Two combination variations:

- **V-04 (Role sequence + output format)**: Roles create internal review that prose
  alone lacks. Skeptic-gate enforces C-02 before confidence is written. Navigator-gate
  enforces C-09/C-10 in the experiment table. This is the highest-structure variation.

- **V-05 (Lifecycle emphasis + inertia framing)**: Lifecycle gates are the most direct
  enforcement of C-05 (no goalpost movement). Adding inertia as a competing hypothesis
  in the CHALLENGE phase is a deeper framing than F-00 as a falsification condition --
  it forces the PM to evaluate status-quo sufficiency as a first-class alternative rather
  than a list item.

### C-05 (no goalpost movement) coverage comparison

| V | How C-05 is enforced |
|---|---------------------|
| V-01 | Section ordering: HYPOTHESIS DECLARED before any evidence sections |
| V-02 | Question ordering: Step 2 (claim) before Steps 1 evidence check context |
| V-03 | Section ordering: HYPOTHESIS DECLARED before FALSIFICATION CONDITIONS |
| V-04 | Phase gate: GATE 2 explicitly lists "No evidence from future phases referenced here" |
| V-05 | Hard gate: GATE 2 checklist item; PHASE 3 is read-only on DECLARE output |

V-05 has the strongest C-05 enforcement (gate checklist item). V-04 is close (gate condition).
V-01/V-03 rely on section ordering. V-02 relies on question sequence -- weakest enforcement.

### Predicted differentiation on aspirational criteria

| C-09 (exp-to-falsification mapping) | C-10 (risk-ranked order) |
|-------------------------------------|--------------------------|
| V-01: pre-printed column | V-01: explicit rank column |
| V-02: none structurally enforced | V-02: "start with the experiment most likely to falsify" instruction only |
| V-03: pre-printed column | V-03: rank column present |
| V-04: Navigator table column | V-04: rank column + "why this risk rank" column |
| V-05: Plan table with both | V-05: rank column + risk rationale column |

V-04 has the richest C-10 surface (rank + rationale column + Navigator role framing).

### Open research question for R2

Does the Skeptic role in V-04 materially improve falsification condition quality (C-02)
relative to V-01's column-based observability gate? Both enforce observability structurally,
but the Skeptic role creates an explicit "challenge" posture that may surface edge cases
the column approach leaves silent. This is only testable on live model runs.
