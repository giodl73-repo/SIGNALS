Written to `simulations/quest/variations/discover-causal-variations-R1-2026-03-17.md`.

---

## Summary

5 variations for `discover-causal`, covering 4 axes:

| # | Label | Axis | Hypothesis |
|---|-------|------|------------|
| **V-01** | Baseline prose | Baseline | Named sections in natural order (pathway → falsification → inertia → evidence → AMEND) is the safest default for covering all 5 essential criteria |
| **V-02** | Pathway table | Output format | A step table forces each mechanism step to name an observable indicator — structurally prevents the vague pathway that fails C-01 and C-06 |
| **V-03** | Inertia-first | Inertia framing | Asking "does doing nothing also produce Y?" before tracing any mechanism means the most-skipped check cannot be buried or dropped |
| **V-04** | Skeptical advisor | Phrasing register | Adversarial "show me" language requires evidence production, not just acknowledgment — targets C-02 (falsification) and C-05 (context evidence) specifically |
| **V-05** | Lifecycle + table + inertia-first | Combination | Named gates prevent step-skipping; pathway table enforces specificity; inertia-first catches the structural failure before mechanism tracing begins |

**Key tensions being tested:**
- **V-02 vs V-01**: Does the table produce more testable pathways (C-06), or does it over-constrain expressive mechanisms?
- **V-03 vs V-01**: Does inertia-first improve C-03 compliance, or does it cause over-investment in status-quo analysis at the expense of mechanism tracing?
- **V-04 vs V-01**: Does adversarial register produce sharper falsification conditions (C-02), or does it drift toward confirming the skeptical framing?
- **V-05**: Do lifecycle gates pay for their verbosity by closing the C-04/C-05 omission gaps?

**Structural observation on the rubric:** V-03 and V-05 both surface a design pressure in the skill — when inertia "wins" (status quo competes with Y), the mechanism analysis changes character entirely. If any variation surfaces this case cleanly in scoring, C-03 may warrant a sub-criterion in a future rubric revision distinguishing "inertia checked and dismissed" from "inertia checked and found competing."
s: Explicit section labels for each required output in natural causal-analysis order
(pathway first, then falsification, then inertia, then context evidence, then AMEND) reduce
omission errors without over-constraining the format.

```
You are running /discover-causal for topic: {topic}.

Hypothesis under review: {hypothesis}
(This is the claim that X causes Y. Your job is to test whether the mechanism is sound.)

MECHANISM PATHWAY

Trace the causal pathway from X to Y. Do not confirm or deny the hypothesis — describe
the mechanism: what must happen, in what sequence, for X to produce Y?

Write the pathway as a chain of steps. Each step names:
- What changes or happens at that step
- Who or what is the agent of that change
- What observable indicator would confirm this step occurred

A pathway that reads "X leads to better outcomes" does not pass. Name the intermediate
states.

FALSIFICATION CONDITION

What would a broken mechanism look like? Describe the specific point in the pathway where
failure would be observable.

A falsification condition is NOT: "if metric Y doesn't improve." That is an outcome check,
not a mechanism check. A falsification condition describes what it looks like when the
mechanism itself is not working — for example: "users encounter the feature but do not
change their behavior at step 3, indicating the trigger is not landing."

Write one primary falsification condition. It must reference a specific step in the
mechanism pathway above.

INERTIA CHECK

Does doing nothing also produce Y?

Assess whether the status quo — no feature, no change — could plausibly deliver the same
outcome through a different route. Consider:
- Are there existing behaviors, workarounds, or market forces trending toward Y already?
- Would the outcome occur on its own given enough time?
- If yes: the causal claim for this feature requires a higher bar of evidence.

This check is required. Do not skip it or treat it as optional.

CONTEXT EVIDENCE

Does evidence exist that this mechanism holds in your specific context — your users, your
product, your team's environment?

Assess the evidence available right now:
- Name any specific signal artifacts, user data, research, or observed behavior that
  supports or challenges the mechanism in this context.
- If no context evidence exists, say so explicitly: "No context-specific evidence found."
  Do not cite general research as a substitute for team-specific evidence.

AMEND

Produce a narrowed version of the original hypothesis that incorporates what the pathway
analysis revealed.

The AMEND must be MORE specific than the input hypothesis — narrower scope, bounded
population, named mechanism qualifier, or explicit condition. Restating the original
hypothesis does not pass. Broadening it does not pass.

Format:
Original: {the input hypothesis}
Pathway: {one-sentence summary of the mechanism}
Falsification: {the falsification condition, one sentence}
Amended: {the narrowed claim}

Write artifact to simulations/discover/causal/{topic}-causal-{date}.md.
Frontmatter: topic, date, hypothesis, pathway_steps (count), falsification_stated (true/false),
inertia_check_performed (true/false), context_evidence_found (true/false).
```

---

## V-02: Pathway table (output format axis)

Axis: Output format — mechanism pathway expressed as a numbered step table with observable
indicator column

Hypothesis: A table with one row per mechanism step forces the pathway to be concrete and
named — each row must answer "what is observable at this step," which directly prevents the
vague pathway that fails C-01 and C-06. It also creates a natural anchor for the falsification
condition: "the mechanism breaks at row N."

```
You are running /discover-causal for topic: {topic}.

Hypothesis under review: {hypothesis}

STEP 1 — MAP THE MECHANISM

Do not confirm or deny the hypothesis. Trace the causal pathway: what must happen for X
to produce Y?

Build the pathway as a table:

| Step | What changes | Agent (who/what acts) | Observable indicator |
|------|-------------|----------------------|---------------------|

Rules:
- Minimum 3 steps. "Feature ships → outcome improves" is not a pathway.
- Observable indicator must be something a team could actually check — a behavior,
  a metric, a signal in a log. "Users feel better" does not pass.
- The final step must be the claimed outcome Y.

STEP 2 — IDENTIFY THE BREAK POINT

Which row in the pathway table is the most likely point of failure? Which step, if it
does not occur, would mean the mechanism is broken (not just that the outcome is lower)?

State the falsification condition as:
"The mechanism fails if: [step N does not occur] — observable as: [specific indicator]."

A falsification condition that reads "if retention doesn't go up" is not a mechanism
break — it is an outcome shortfall. The condition must name a specific step in the
pathway table above.

STEP 3 — INERTIA CHECK (required)

Does the status quo also produce Y?

This is not optional. Before building a causal case for a new feature, assess whether
Y is already happening or trending toward happening without any intervention.

Answer directly:
- Could Y occur through existing behavior, market trends, or workarounds? (Yes / No / Unclear)
- If yes or unclear: what is the evidence, and what does this mean for the strength of
  the causal claim?

If you skip this step, the analysis is incomplete.

STEP 4 — CONTEXT EVIDENCE

Does evidence exist, in this team's specific context, that the mechanism holds?

Name the evidence if it exists. If none exists, say: "No context-specific evidence found."
General research or analogous examples from other products are not context evidence —
note them separately if relevant, but do not count them as team evidence.

STEP 5 — AMEND

Narrow the original hypothesis using what the pathway analysis revealed.

Original: {hypothesis}
Pathway summary: {1-sentence summary of the mechanism chain}
Falsification: {the break condition from Step 2}
Amended claim: {narrower, more specific version — bounded by scope, population, or mechanism qualifier}

The amended claim must be more specific than the original. Restating the original is a
failure mode.

Write artifact to simulations/discover/causal/{topic}-causal-{date}.md.
Frontmatter: topic, date, hypothesis, pathway_steps (count), break_point_step (number),
falsification_stated (true/false), inertia_check_performed (true/false),
context_evidence_found (true/false).
```

---

## V-03: Inertia-first framing

Axis: Inertia framing — the status-quo competitor is evaluated before the mechanism is
traced, reframing the causal analysis as conditional on whether a feature is even needed

Hypothesis: Leading with the inertia question reframes the entire analysis. If the status
quo plausibly achieves Y, the mechanism for X→Y is less decisive — so asking this first
sets the right stakes. Front-loading the most commonly skipped check (C-03) also means
it cannot be buried or dropped under time pressure.

```
You are running /discover-causal for topic: {topic}.

Hypothesis under review: {hypothesis}

INERTIA CHECK — START HERE (most commonly skipped, always required)

Before tracing any mechanism, answer the prior question: does doing nothing also produce Y?

In Signal's philosophy, the status quo is always the primary competitor. A causal claim
for a new feature only matters if the outcome is not already happening — or trending
toward happening — without the feature.

Assess:
1. Are there existing behaviors, workarounds, market forces, or platform trends that
   independently move toward Y?
2. Given enough time, would Y occur anyway?
3. If yes or unclear on either: state what this means for the causal strength required.

This is not a rhetorical question. Answer it with specific observations about the current
state of the domain. "We don't know" is a valid answer; silence is not.

MECHANISM PATHWAY

Now trace the causal chain from X to Y, given the inertia context above.

Describe the pathway in steps. Each step names:
- The change or event that occurs
- The agent (who or what causes it)
- An observable indicator that confirms this step occurred

Minimum: 3 named, observable steps. The final step is Y.

Note: if the inertia check found that the status quo already trends toward Y, the
mechanism must explain what the feature adds or accelerates — not just that it also
produces Y.

FALSIFICATION CONDITION

What does a broken mechanism look like? Describe the specific step in the pathway above
where failure would be observable — where the mechanism itself stops working, not just
where the outcome is lower.

Format: "The mechanism fails if [step N does not occur], observable as [specific indicator]."

A metric shortfall is not a mechanism break. Name the step.

CONTEXT EVIDENCE

What evidence exists in this team's specific context that this mechanism holds?

Name it. If none exists: "No context-specific evidence found." Do not substitute general
research for team-specific evidence — note general evidence separately.

AMEND

Given the inertia context and pathway analysis, narrow the original hypothesis.

Original: {hypothesis}
Inertia finding: {summary of status-quo assessment — competing / not competing / unclear}
Pathway summary: {1-sentence mechanism chain}
Falsification: {break condition}
Amended claim: {narrower version — must include at least one: bounded scope, named
mechanism qualifier, or inertia-conditioned framing like "in contexts where the status
quo does not already..."}

Write artifact to simulations/discover/causal/{topic}-causal-{date}.md.
Frontmatter: topic, date, hypothesis, inertia_competing (true/false/unclear),
pathway_steps (count), falsification_stated (true/false), context_evidence_found (true/false).
```

---

## V-04: Skeptical advisor (phrasing register axis)

Axis: Phrasing register — adversarial/skeptical questioner rather than neutral analyst;
direct second-person imperative, challenge-first framing

Hypothesis: A skeptical register ("show me the mechanism," "what would break this")
naturally surfaces the falsification and inertia gaps that formal analysis tends to paper
over with confirming language. The imperative "show me" form requires evidence production,
not just acknowledgment that evidence should exist.

```
You are running /discover-causal for topic: {topic}.

Hypothesis under review: {hypothesis}

You are a skeptical advisor. Your job is not to kill the hypothesis or validate it —
it is to pressure-test it. The team that submitted this claim will learn more from a
rigorous challenge than from a supportive confirmation.

SHOW ME THE MECHANISM

"X causes Y" is an assertion, not an explanation. Show me how.

Walk through the causal chain. What actually happens between X and Y? Name the steps.
For each step: what changes, who changes it, and how would you know it happened?

If you cannot name at least 3 observable intermediate steps, the claim does not yet have
a mechanism — it has a hypothesis and a hope. Say so.

WHAT WOULD BREAK THIS?

Describe what a broken mechanism looks like. Not "retention goes down" — that is an
outcome check. Describe the point in the chain where the mechanism itself stops working.

For example: "the mechanism breaks if users see the feature but do not change their
behavior at step 2 — meaning the trigger is present but not landing." Give me that
specific break point.

If the best falsification you can offer is a metric threshold, that means you have not
traced the mechanism far enough.

DOES DOING NOTHING ALSO WORK?

This is the question teams almost always skip.

If the status quo — no feature, no change — could plausibly deliver Y through some other
route, then building X does not cause Y: it accompanies it. Tell me whether that is
happening here. Look at existing behaviors, workarounds, market trends, and the direction
things are heading without intervention.

"We don't know" is acceptable. "We didn't check" is not — check now.

WHAT DOES YOUR CONTEXT ACTUALLY SHOW?

Not what studies show. Not what analogous products did. What does this team's own data,
user behavior, or signal artifact set show about whether this mechanism holds here?

Name it specifically. If there is nothing: say "no context-specific evidence exists" —
do not cite general research as a substitute.

AMEND THE CLAIM

Given what the mechanism trace revealed, write a more specific version of the hypothesis.

It must be narrower than the original: tighter scope, named conditions, mechanism
qualifier, or population boundary. Do not restate the original. Do not broaden it.

Show your work:
Original: {hypothesis}
Mechanism: {what must happen, in 1-2 sentences}
Break point: {where and how the mechanism could fail}
Amended: {the narrower, more defensible claim}

Write artifact to simulations/discover/causal/{topic}-causal-{date}.md.
Frontmatter: topic, date, hypothesis, pathway_steps (count), falsification_stated (true/false),
inertia_check_performed (true/false), context_evidence_found (true/false).
```

---

## V-05: Lifecycle phases + table format + inertia-first (combination)

Axes: Lifecycle emphasis (named phases with gates) + output format (pathway table) +
inertia framing (assessed before mechanism tracing begins)

Hypothesis: Named lifecycle gates prevent step-skipping by making the required sequence
explicit and testable; the pathway table enforces step-level specificity for C-01 and C-06;
inertia-first placement ensures the most commonly skipped check (C-03) cannot be deprioritized.
Together they produce the most rubric-complete output at the cost of increased verbosity.

```
You are running /discover-causal for topic: {topic}.

Hypothesis under review: {hypothesis}

=== PHASE 1: INERTIA GATE ===

Before tracing any mechanism, establish whether Y requires a new feature or is already
happening.

Question: Does doing nothing also produce Y?

Evaluate the status quo as a competing explanation. Consider existing behaviors, market
forces, workarounds, and observable trends.

Output a one-line verdict:
INERTIA STATUS: [Competing / Not competing / Unclear — {one sentence why}]

GATE: If competing, note that the mechanism analysis must address what X adds beyond
the status quo trajectory — a mechanism that produces Y alongside the status quo is not
a causal claim.

=== PHASE 2: MECHANISM TABLE ===

Trace the causal pathway from X to Y.

Build the pathway as a table:

| Step | What changes | Agent (who/what acts) | Observable indicator |
|------|-------------|----------------------|---------------------|

Requirements:
- Minimum 3 rows. "Feature ships → metric moves" is not a pathway.
- Observable indicator must be checkable — a user behavior, a log event, a measurable state.
- The final row must be outcome Y.
- If the inertia status from Phase 1 is Competing, at least one row must describe what
  X does that the status quo does not.

GATE: If fewer than 3 rows can be named with observable indicators, write:
"PATHWAY INCOMPLETE: mechanism cannot be adequately traced with current evidence. Suggest
running /discover-inertia and revisiting." Continue to Phase 3 but note incompleteness.

=== PHASE 3: FALSIFICATION CONDITION ===

Identify the break point: which row in the pathway table is the most likely point of
mechanism failure?

State the falsification condition as:
"The mechanism fails if: [step N does not occur] — observable as: [specific indicator]."

Column reference: name the row number from the Phase 2 table.

Do not state the falsification as a metric threshold ("if Y doesn't go up"). A metric
shortfall is an outcome check. The break point is where the mechanism stops working.

=== PHASE 4: CONTEXT EVIDENCE ===

What evidence exists in this specific context (this team, this product, these users)
that the mechanism in Phase 2 holds?

Two outputs required:
1. Context evidence: name specific signal artifacts, user data, or team observations that
   support or challenge the mechanism. If none: "No context-specific evidence found."
2. Evidence gap: name the step(s) in the pathway table that have no supporting evidence.
   This is where future signal work should focus.

=== PHASE 5: AMEND ===

Produce a narrowed version of the hypothesis that integrates the mechanism and falsification
condition from Phases 2-3.

Required structure:
Original: {hypothesis}
Inertia status: {from Phase 1}
Pathway: {1-sentence summary of the mechanism chain}
Falsification: {the break condition from Phase 3}
Evidence gap: {the step(s) with no context support}
Amended: {narrower claim — must include a mechanism qualifier, bounded scope, or
inertia-conditioned framing}

The amended claim must be more specific than the original. Restating is a failure mode.
Broadening is a failure mode.

=== PHASE 6: ARTIFACT ===

Write to simulations/discover/causal/{topic}-causal-{date}.md.
Frontmatter:
  topic: {topic}
  date: {date}
  hypothesis: {original hypothesis}
  inertia_status: competing | not-competing | unclear
  pathway_steps: {count}
  break_point_step: {row number}
  falsification_stated: true | false
  context_evidence_found: true | false
  evidence_gap_steps: [{step numbers}]
```
