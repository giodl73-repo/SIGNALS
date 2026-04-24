Written to `simulations/quest/variations/discover-causal-variations-R2-2026-03-17.md`.

---

## Summary

| # | Label | Axis | Hypothesis |
|---|-------|------|------------|
| **V-01** | Confounder section | Role sequence | Promotes confounders to their own required section before falsification — closes the C-07 gap where inertia was the only named alternative |
| **V-02** | Evidence quality scale | Output format | Embeds a T1/T2/T3 evidence tier scale in the evidence section — creates structural scaffolding for C-09 and forces "we have evidence" to be typed, not asserted |
| **V-03** | Competing pathways | Lifecycle emphasis | Requires two labeled pathways before falsification — directly enables C-10 and surfaces confounders naturally (Pathway B is often an alternative cause) |
| **V-04** | Incompleteness gate + step-anchored falsification | Combination (C-11 + C-12) | Readiness gate before tracing + labeled step numbers = reinforcing structure: you cannot anchor falsification to a step you never named |
| **V-05** | Full aspirational stack | Combination (all v2 aspirationals) | Phase 0 inertia gate through Phase 7 artifact — structural slots for C-07, C-09, C-10, C-11, C-12, C-13, C-14 all in one output |

**Key design choices vs R1:**

- R1 tested *whether* new structures helped; R2 tests *which minimum structure* is needed per new criterion
- V-01 through V-03 are single-axis isolations of C-07, C-09, and C-10 respectively
- V-04 is the minimum combination to produce C-11 + C-12 together (they are structurally coupled: the falsification anchor requires a named step, which requires the readiness gate to not have dropped the pathway)
- V-05 is the rubric ceiling reference — every new v2 aspirational criterion has a dedicated phase

**Structural observation:** V-04's C-11/C-12 coupling is the most interesting dependency to watch in scoring. If a model declares incompleteness at Phase 1 and traces only 2 steps, the Phase 3 falsification must anchor to one of those 2 steps — or acknowledge it cannot. This either produces strong C-11 + C-12 compliance or a principled gap declaration, which is itself valuable signal.
er time pressure?
- **V-04 vs V-05**: Can the incompleteness gate (C-11) and step-anchored falsification
  (C-12) be isolated as a clean two-axis combination, or does full C-14 compliance
  (AMEND conditioned on inertia) require the full Phase 0 inertia gate from V-05?

**Structural observation:** V-04 creates a reinforcing dependency between C-11 and C-12:
if a step is not named in the pathway (because incompleteness was declared), it cannot
serve as a falsification anchor. This makes C-12 mechanically dependent on C-11 in the
same output -- which may increase both pass rates together or cause both to fail together.
This dependency is worth watching in scoring.

---

## V-01: Confounder section (role sequence axis)

Axis: Role sequence -- confounders and alternative causes promoted to a named required
section that runs after mechanism pathway and before falsification, independently of
the inertia check

Hypothesis: The C-07 universal failure in R1 occurred because alternative causes were
never explicitly required -- teams could satisfy the inertia check and feel done with
alternatives. Moving confounders to their own required section, positioned before
falsification and explicitly distinguished from the inertia check, prevents the C-03/C-07
conflation where the status quo counts as the only named alternative.

```
You are running /discover-causal for topic: {topic}.

Hypothesis under review: {hypothesis}
(Claim: X causes Y. Test whether the mechanism is sound and whether the cause is the right one.)

MECHANISM PATHWAY

Trace the causal chain from X to Y as a sequence of named, observable steps.

For each step, name:
- What changes or happens
- Who or what drives the change
- What observable indicator would confirm this step occurred

Minimum 3 steps. "X enables better outcomes" is not a pathway -- name the intermediate
states. If you cannot trace 3 observable steps with current knowledge, say so explicitly
("mechanism not fully traceable at step N") rather than generating thin steps.

ALTERNATIVE CAUSES

Before testing falsification, name the competing explanations.

This is not the inertia check. The inertia check asks whether the status quo produces Y
over time. This asks: what else, operating right now, could produce Y without X?

Identify:
1. At least one alternative causal pathway -- a route to Y that does not run through
   the mechanism you traced above (a different feature, a market shift, a behavior change)
2. At least one confounding variable -- something that correlates with X and could create
   the appearance of causation without X being the driver (e.g., teams that adopt X are
   already more motivated, so Y would improve regardless)

If no confounders can be identified, say so explicitly and explain why the mechanism is
not susceptible to the typical alternative causes for this outcome type. Silence is not
acceptable.

FALSIFICATION CONDITION

Given the pathway and the alternatives above, describe what a broken mechanism looks like.

Two outputs:
1. Mechanism break: the specific step in the pathway where failure would be visible --
   not "if outcome Y declines" but "if step N does not occur, observable as [indicator]."
2. Alternative signal: what would indicate Y is being produced by an alternative cause
   rather than by the mechanism? (Distinguishes "mechanism working but outcome moved
   elsewhere" from "mechanism not working.")

INERTIA CHECK

Does the status quo also produce Y?

Assess whether doing nothing -- no feature, no intervention -- would independently trend
toward outcome Y through existing behaviors, workarounds, or market forces.

Required answer: Competing / Not competing / Unclear. One sentence why.

CONTEXT EVIDENCE

What specific evidence exists in this team's context that the mechanism holds and that
the named alternatives are not the actual cause?

Name it specifically. If none: "No context-specific evidence found." General research
is not context evidence -- note it separately if relevant, but do not count it as
team-specific.

AMEND

Narrow the original hypothesis to reflect the mechanism, falsification, and alternative
cause analysis.

Original: {hypothesis}
Pathway: {1-sentence mechanism summary}
Key alternative: {the most plausible competing cause identified above}
Falsification: {mechanism break condition}
Amended: {narrower claim -- bounded by mechanism qualifier, population, or condition that
distinguishes X's effect from the alternative causes}

Write artifact to simulations/discover/causal/{topic}-causal-{date}.md.
Frontmatter: topic, date, hypothesis, pathway_steps (count), confounders_identified (count),
falsification_stated (true/false), inertia_check_performed (true/false),
context_evidence_found (true/false).
```

---

## V-02: Evidence quality scale (output format axis)

Axis: Output format -- evidence section replaced with a typed evidence audit using a named
3-tier quality scale (anecdotal / correlation / controlled) with per-piece ratings

Hypothesis: The C-09 failure in R1 occurred because no variation gave teams a naming
convention for evidence quality -- so all evidence was rated present/absent, never
typed. Embedding a 3-tier scale directly in the evidence section instruction creates a
structural scaffold that makes C-09 producible without extra effort. The scale also
forces precision in C-05: "we have evidence" is no longer acceptable without a tier.

```
You are running /discover-causal for topic: {topic}.

Hypothesis under review: {hypothesis}

MECHANISM PATHWAY

Trace the causal chain from X to Y as a sequence of named, observable steps.

Each step names:
- What changes or happens
- Who or what acts
- How you would observe this step occurring

Minimum 3 steps. If fewer than 3 observable intermediate steps can be identified with
current knowledge, say so rather than inventing thin steps to fill the requirement.

FALSIFICATION CONDITION

Describe the specific step in the pathway above where mechanism failure would be visible
-- not "if outcome Y declines" but where the causal chain itself stops working.

Format: "The mechanism fails if [step N does not occur], observable as [indicator]."

Reference the step by its label or position in the pathway above.

INERTIA CHECK

Does doing nothing also produce Y?

Assess whether the status quo -- no feature, no change -- could independently trend toward
outcome Y. Answer: Competing / Not competing / Unclear, and one sentence why.

CONTEXT EVIDENCE (WITH QUALITY RATING)

Assess the evidence that the mechanism holds in this specific team context.

Use this quality scale for each piece of evidence:

  T1 -- Anecdotal: Individual reports, user quotes, team observations, product intuition.
  Directionally useful but not measurable. Cannot establish mechanism on its own.

  T2 -- Correlation: A/B test results, usage analytics, survey data, behavioral logs.
  Establishes co-occurrence. Can support mechanism hypothesis but does not confirm
  causation.

  T3 -- Controlled: Experiment with controlled conditions, intervention study, or causal
  inference method applied to the relevant steps. Can confirm mechanism if correctly
  targeted.

For each piece of evidence available in this context:
  - Name it specifically (artifact name, data source, observed behavior, team finding)
  - Rate it: T1 / T2 / T3
  - Name the pathway step it supports

If no evidence exists for any step: "No context-specific evidence found. Tier: none."

Aggregate evidence tier: the highest tier available across all named evidence.

Do not substitute general research or analogous product examples for team-specific
evidence -- note them separately if relevant, but do not count them in the tier audit.

CONFOUNDER CHECK

Name at least one alternative explanation for Y that does not require X. What else could
produce this outcome independently?

AMEND

Narrow the original hypothesis to reflect the mechanism and the evidence quality available.

Original: {hypothesis}
Evidence quality: {aggregate tier -- T1 / T2 / T3 / none}
Pathway: {1-sentence mechanism summary}
Falsification: {break condition, step-referenced}
Amended: {narrower claim -- scoped to the evidence tier available; mechanism condition
named; or qualified with "pending T3 evidence for step N" if the break point has no
supporting evidence}

Write artifact to simulations/discover/causal/{topic}-causal-{date}.md.
Frontmatter: topic, date, hypothesis, pathway_steps (count),
evidence_quality_tier (T1/T2/T3/none), falsification_stated (true/false),
inertia_check_performed (true/false), confounders_identified (true/false).
```

---

## V-03: Competing pathways (lifecycle emphasis axis)

Axis: Lifecycle emphasis -- mechanism section expanded to require two labeled causal
pathways before falsification, with an explicit pathway comparison step

Hypothesis: C-10 (multiple causal pathways considered) never fired in R1 because no
variation asked for more than one mechanism. Requiring two named pathways up front
forces the team to test whether the mechanism is unique -- or whether there are two
routes to Y requiring different evidence to distinguish. The falsification condition
becomes richer: it must either break both pathways or name which pathway it tests.
This also surfaces confounders more naturally (Pathway B is often an alternative cause).

```
You are running /discover-causal for topic: {topic}.

Hypothesis under review: {hypothesis}

PATHWAY A -- PRIMARY MECHANISM

Trace the most direct causal chain from X to Y. Name each step:
- What changes at this step
- Who or what drives it
- Observable indicator

Minimum 3 steps. "X ships and metric improves" is not a pathway.

PATHWAY B -- SECONDARY MECHANISM OR ALTERNATIVE

Now trace a second route -- either a different mechanism from X to Y, or a competing
path where something other than X produces Y.

This may be:
  - A different causal chain via a different intermediate (X causes Z causes Y, vs
    X causes W causes Y)
  - A contribution model (X enables Z, which separately causes Y)
  - A competing mechanism (another factor independently produces Y alongside X)

Why this matters: if both pathways produce Y, you need to know which is operating in
your context. If they falsify differently, the active one determines what you instrument.

Label and trace Pathway B with the same structure: step, agent, observable indicator.

If no meaningful second pathway exists, say so explicitly and explain why the mechanism
is singular. "I can only identify one pathway" is acceptable -- silence is not.

PATHWAY COMPARISON

Compare Pathways A and B:
  - Relationship: Complementary (both active) / Competing (only one correct) /
    Nested (B is a special case of A) / Singular (only A exists)
  - Most likely active in this context: A / B / both / unclear -- and why
  - Independently falsifiable: Yes / No -- and what that means for instrumentation

FALSIFICATION CONDITIONS

For each active pathway:
  Pathway A break: what step fails, observable as what?
  Pathway B break: what step fails, observable as what? (or "not applicable")

If they share a break point, name it once and explain why.

INERTIA CHECK

Does the status quo produce Y via either pathway? Answer: Competing / Not competing /
Unclear. If competing, which pathway does the status quo most resemble?

CONTEXT EVIDENCE

What team-specific evidence exists for each pathway?

Name evidence per pathway -- do not combine. Which pathway has stronger contextual support?

AMEND

Original: {hypothesis}
Active pathway: {A / B / both -- and basis for selection}
Pathway summary: {1-sentence mechanism for the active pathway}
Falsification: {break condition for the active pathway}
Amended: {narrower claim -- conditioned on the active pathway, bounded by the inertia
finding, and specific to the context where evidence is strongest}

Write artifact to simulations/discover/causal/{topic}-causal-{date}.md.
Frontmatter: topic, date, hypothesis, pathway_a_steps (count),
pathway_b_identified (true/false),
pathway_relationship (complementary/competing/nested/singular),
active_pathway (A/B/both/unclear), falsification_stated (true/false),
inertia_check_performed (true/false), context_evidence_found (true/false).
```

---

## V-04: Incompleteness gate + step-anchored falsification (combination)

Axes: Lifecycle emphasis (explicit readiness gate before mechanism tracing, enabling C-11)
+ Output format (step-labeled pathway with numbered and named steps, enabling C-12)

Hypothesis: C-11 fails when models fabricate thin pathways rather than admit
incompleteness. A lifecycle gate that asks "can you trace 3 observable steps?" before
mechanism tracing begins -- and requires self-disclosure if not -- makes incompleteness
acknowledgment structurally required rather than optional. Combining this with labeled
step names creates a reinforcing structure: the falsification condition (C-12) must
anchor to a specific step by number and name, which is impossible if a step was never
labeled. The two criteria are structurally mutually reinforcing in this combination.

```
You are running /discover-causal for topic: {topic}.

Hypothesis under review: {hypothesis}

=== MECHANISM READINESS CHECK ===

Before tracing the mechanism, assess whether you have sufficient knowledge to trace it.

Question: Can you name 3 or more observable intermediate steps between X and Y -- steps
where you can identify what changes, who acts, and how you would observe it?

If yes: proceed to MECHANISM PATHWAY.
If no: write "MECHANISM INCOMPLETE: [explain which part of the chain cannot be traced
with current knowledge and why]" -- then continue with what can be traced, marking any
step you cannot substantiate with [UNCERTAIN].

This is a honesty gate, not a barrier to continuing. A pathway that names 3 thin or
vague steps to clear the threshold -- instead of flagging genuine uncertainty -- fails
this check. Accurate self-report is the output.

=== MECHANISM PATHWAY ===

Trace the causal pathway from X to Y.

Label each step with a number and a short descriptive name. Format:

  Step 1 -- [Name]: What changes. Who acts. Observable indicator.
  Step 2 -- [Name]: What changes. Who acts. Observable indicator.
  Step 3 -- [Name]: ...

Use labels like "Step 2 -- User acts on prompt" so they can be referenced precisely in
later sections. If a step was flagged [UNCERTAIN] in the readiness check, retain that
flag here.

=== FALSIFICATION CONDITION ===

Name the specific step from the pathway above where mechanism failure would be observable.

Required format:
"The mechanism fails if Step [N] -- [Name] -- does not occur, observable as [specific
indicator]."

Rules:
- The step number and name must match a labeled row in the pathway above.
- If the pathway is incomplete (readiness check triggered), name the earliest step that
  can still be falsified and note the incompleteness.
- A falsification condition that does not reference a specific step by number and name
  does not pass this section.
- Do not state falsification as a metric shortfall ("if Y does not improve") -- that is
  an outcome check, not a mechanism check.

=== INERTIA CHECK ===

Does doing nothing also produce Y?

Assess the status quo as a competing cause -- existing behaviors, workarounds, and domain
trends that independently move toward Y without any new feature.

Required output:
INERTIA STATUS: [Competing / Not competing / Unclear -- one sentence basis]

=== CONTEXT EVIDENCE ===

What team-specific evidence exists that the mechanism holds?

Name it. If none: "No context-specific evidence found."

Also: which labeled steps in the pathway have no supporting evidence? List step numbers
and names. This guides future signal work -- you are not expected to have evidence for
every step, but gaps must be named.

=== AMEND ===

Narrow the original hypothesis using the mechanism and falsification analysis.

Original: {hypothesis}
Mechanism complete: {yes / no / partial -- and what is incomplete}
Inertia status: {from inertia check}
Pathway: {1-sentence mechanism summary}
Falsification: {Step N -- Name -- break condition}
Amended: {narrower claim -- must include at least one: mechanism qualifier, scope
condition, or inertia-conditioned framing if status is Competing or Unclear}

Write artifact to simulations/discover/causal/{topic}-causal-{date}.md.
Frontmatter:
  topic: {topic}
  date: {date}
  hypothesis: {original hypothesis}
  mechanism_complete: true | false | partial
  pathway_steps: {count}
  break_point_step: {step label, e.g. "Step 2 -- Name"}
  inertia_status: competing | not-competing | unclear
  falsification_stated: true | false
  context_evidence_found: true | false
  evidence_gap_steps: [{step labels}]
```

---

## V-05: Full aspirational stack (combination)

Axes: Inertia gate (C-03, C-14) + incompleteness gate (C-11) + step-labeled pathway
table (C-12) + per-step evidence accounting with tier rating (C-09, C-13) + competing
pathways noted (C-10) + inertia-conditioned AMEND (C-14) + confounder check (C-07)

Hypothesis: The v2 aspirational criteria (C-11 through C-14) can all be produced in a
single output if each is given its own structural slot. V-05 tests the ceiling of the
v2 rubric by making every aspirational criterion structurally required -- not recommended
-- and by integrating them so that the AMEND section synthesizes results from all prior
phases. This is the reference target for what a Golden output looks like under the v2
rubric. The expected cost is increased prompt complexity and verbosity.

```
You are running /discover-causal for topic: {topic}.

Hypothesis under review: {hypothesis}

=== PHASE 0: INERTIA GATE ===

Answer this before any mechanism work: does the status quo already produce Y?

Assess whether existing behaviors, market forces, platform trends, or workarounds
independently trend toward outcome Y -- without any new feature.

INERTIA VERDICT: [Competing / Not competing / Unclear]
Basis: [one sentence -- specific observation about the current state of the domain, not
assertion]

If Competing: the mechanism analysis in Phase 2 must explain what X adds or accelerates
beyond the status quo trajectory. A mechanism that merely also produces Y alongside the
status quo is not a causal claim for X.

=== PHASE 1: MECHANISM READINESS ===

Before tracing, assess: can you name 3 or more observable intermediate steps between X
and Y?

If yes: proceed.
If no: declare incompleteness now.
  Write: "PATHWAY INCOMPLETE: mechanism cannot be traced past [step description].
  Missing knowledge: [what evidence or domain knowledge is needed]."
  Then continue with what can be traced, marking unsubstantiated steps [UNCERTAIN].

Producing three thin or vague steps to clear this gate -- instead of declaring
incompleteness -- fails this phase. Accurate self-report is the required output.

=== PHASE 2: MECHANISM PATHWAY ===

Trace the causal pathway from X to Y.

Label each step. Format:
  Step 1 -- [Name]: What changes. Who acts. Observable indicator.
  Step 2 -- [Name]: ...

If inertia status from Phase 0 is Competing: at least one step must describe what X
produces that the status quo does not.

Also: is there more than one plausible causal pathway from X to Y?
  - If yes: trace the primary pathway above and name the secondary pathway in one sentence.
    Note whether the two pathways are complementary, competing, or nested.
  - If no: note that the mechanism is singular.

=== PHASE 3: FALSIFICATION ===

Name the most likely mechanism break point.

Required format:
"The mechanism fails if Step [N] -- [Name] -- does not occur, observable as [indicator]."

Step number and name must match Phase 2. If a step is marked [UNCERTAIN], that step may
still serve as a falsification anchor -- note the uncertainty in the indicator description.

Do not state the falsification as a metric threshold. A metric shortfall is an outcome
check. Name where the mechanism stops working.

=== PHASE 4: CONTEXT EVIDENCE ===

Assess evidence per pathway step.

For each step in Phase 2:
  Step N -- [Name]: [evidence name, artifact, or "no evidence"] -- [T1 / T2 / T3 / none]
    T1 = anecdotal / observational / team intuition
    T2 = correlation / A-B / usage analytics / survey
    T3 = controlled / causal-inference-grade experiment

Required outputs:
  Evidence gap steps: [list step numbers/names with no supporting evidence]
  Aggregate evidence tier: [highest tier available across all steps -- T1/T2/T3/none]

Do not substitute general research for team-specific evidence. Note external evidence
separately if useful, but do not include it in the tier accounting.

=== PHASE 5: CONFOUNDER CHECK ===

Name at least one alternative explanation for Y that does not involve X and is not the
inertia status quo.

This is an independently operating cause -- something in the environment that could
produce Y coincidentally with X being deployed. If none can be identified, explain why.

=== PHASE 6: AMEND ===

Produce a narrowed version of the hypothesis that integrates all prior phases.

Required structure:
  Original: {hypothesis}
  Inertia verdict: {from Phase 0 -- Competing / Not competing / Unclear}
  Mechanism complete: {yes / no / partial}
  Active pathway: {primary / secondary / both / singular}
  Pathway: {1-sentence mechanism summary}
  Falsification: {Step N -- Name -- break condition}
  Evidence gap: {step(s) lacking support}
  Amended: {narrower claim -- must include:
    (a) a mechanism qualifier (what must be true in the causal chain for X to cause Y),
    (b) a scope condition (population, context, or timeframe),
    (c) inertia condition if status is Competing or Unclear: "in contexts where the
        status quo does not already [produce Y]" or "invalid if inertia check shows
        [condition]"}

A narrowed claim that ignores the inertia verdict does not pass.
A narrowed claim that ignores mechanism incompleteness does not pass.

=== PHASE 7: ARTIFACT ===

Write to simulations/discover/causal/{topic}-causal-{date}.md.
Frontmatter:
  topic: {topic}
  date: {date}
  hypothesis: {original hypothesis}
  inertia_status: competing | not-competing | unclear
  mechanism_complete: true | false | partial
  pathway_steps: {count}
  secondary_pathway_noted: true | false
  pathway_relationship: complementary | competing | nested | singular
  break_point_step: {step label}
  falsification_stated: true | false
  evidence_aggregate_tier: T1 | T2 | T3 | none
  evidence_gap_steps: [{step labels with no supporting evidence}]
  confounders_identified: {count}
  context_evidence_found: true | false
```
