Written to `simulations/quest/variations/discover-causal-variations-R3-2026-03-17.md`.

---

## discover-causal Variations R3

| # | Label | Axis | Target criteria |
|---|-------|------|-----------------|
| **V-01** | AMEND synthesis completeness | Output format | C-15 |
| **V-02** | Formal step labeling as prerequisite | Output format | C-16 |
| **V-03** | Confounder/inertia hard separation | Role sequence | C-17 |
| **V-04** | Incomplete-pathway falsification anchor | Lifecycle emphasis | C-18 |
| **V-05** | Full v3 aspirational stack | Combination | C-15+C-16+C-17+C-18 |

**Design rationale:**

Each new v3 criterion maps to an identifiable gap in R2 V-05 — the R2 ceiling that scored 120/120 under the v2 rubric:

- **C-15 → V-01**: R2 V-05 AMEND has 7 fields but no `Confounder finding:` field. Phase 5 output is silently dropped. V-01 adds it as a required named field with an explicit "partial synthesis does not pass" rule.
- **C-16 → V-02**: R2 V-05 instructs the `Step N -- [Name]:` format but frames it as a presentation instruction, not a load-bearing prerequisite. V-02 makes the prerequisite nature explicit ("unlabeled steps make C-12 and C-13 unscoreable") to change compliance calculus.
- **C-17 → V-03**: R2 V-05 Phase 5 says "not the inertia status quo" but doesn't require the model to explicitly acknowledge the exclusion by name. V-03 adds a mandatory explicit statement — "The inertia case (Phase 0 verdict: [verdict]) is NOT included here" — and names what a valid confounder looks like (simultaneously-operating, not counterfactual).
- **C-18 → V-04**: R2 V-05 Phase 3 notes that `[UNCERTAIN]` steps can still anchor falsification, but doesn't prohibit deferral when incompleteness is declared. V-04 adds a conditional branch with named prohibited output forms and a required BEST-TRACEABLE ANCHOR format.

**The scoring expectation**: V-05 should hit or approach 140/140. V-01/V-02/V-03 each target one new criterion while maintaining all R2 criteria. V-04 is the tightest two-phase dependency test (C-11 + C-18 coupling).
 criteria as single-axis tests
- V-04 tests whether the C-11/C-18 dependency (incompleteness gate must produce a step-anchor, not a deferral) can be enforced with a conditional branch alone
- V-05 is the rubric ceiling reference for v3 — every new criterion has a dedicated structural slot

---

## V-01: AMEND synthesis completeness (output format axis)

**Axis:** Output format — AMEND section expanded to explicitly list all four prior analytical
phase outputs as required named fields, with integration rules that prohibit partial synthesis

**Hypothesis:** C-15 fails when AMEND omits the confounder finding. R2 V-05 AMEND has
seven fields (Original, Inertia verdict, Mechanism complete, Active pathway, Pathway,
Falsification, Evidence gap) but no `Confounder finding:` field — so the Phase 5 output
is silently dropped. Adding it as a required named field, alongside an explicit rule that
partial synthesis does not pass, closes C-15 without requiring a full phase restructure.

```
You are running /discover-causal for topic: {topic}.

Hypothesis under review: {hypothesis}
(Claim: X causes Y. Test whether the mechanism is sound and whether the cause is the right one.)

MECHANISM PATHWAY

Trace the causal chain from X to Y as a sequence of labeled, observable steps.

Label each step with a number and short name. Format:
  Step N -- [Name]: What changes. Who acts. Observable indicator.

Minimum 3 steps. "X leads to better outcomes" is not a pathway -- name the intermediate
states and changes. If you cannot trace 3 observable steps with current knowledge, say so
explicitly ("mechanism not fully traceable at step N") rather than generating thin steps.

INERTIA CHECK

Does the status quo also produce Y?

Assess whether doing nothing -- no feature, no intervention -- would independently trend
toward outcome Y through existing behaviors, workarounds, or market forces.

INERTIA VERDICT: [Competing / Not competing / Unclear -- one sentence basis]

ALTERNATIVE CAUSES

Before falsification, name what else could produce Y.

This is NOT the inertia check. The inertia check asks whether the status quo trends toward
Y over time without any intervention. This section asks: what independently operating
causes, present right now, could produce Y coincidentally with X being deployed?

Name:
1. At least one alternative causal pathway that does not run through the mechanism above.
2. At least one confounding variable -- something that correlates with X and could make Y
   appear to improve without X being the actual driver.

If neither can be identified, explain why explicitly. Silence is not acceptable.

FALSIFICATION CONDITION

Given the pathway and alternatives above, name the mechanism break point.

Required format:
"The mechanism fails if Step [N] -- [Name] -- does not occur, observable as [indicator]."

The step number and name must match a labeled row in the pathway above.

CONTEXT EVIDENCE

What team-specific evidence exists that the mechanism holds?

Rate each piece: T1 (anecdotal), T2 (correlation), T3 (controlled).
Name each piece, rate it, and name which pathway step it supports.
If no evidence: "No context-specific evidence found. Tier: none."

Aggregate evidence tier: [highest available across all steps]

AMEND

Narrow the original hypothesis by synthesizing all four prior analytical outputs.

This section has four required named fields from prior phases. Including only some is not
sufficient -- all four must appear, and the Amended claim must reflect all four.

Required structure:
  Original: {hypothesis}
  Inertia verdict: {Competing / Not competing / Unclear -- from INERTIA CHECK}
  Mechanism completeness: {complete / incomplete -- from MECHANISM PATHWAY}
  Evidence tier: {T1 / T2 / T3 / none -- aggregate tier from CONTEXT EVIDENCE}
  Confounder finding: {alternative cause identified -- from ALTERNATIVE CAUSES, or
    "none identified -- [reason]"}
  Falsification: {Step N -- Name -- break condition}
  Amended: {narrower claim that incorporates all four prior findings -- mechanism
    qualifier, scope condition, inertia condition if Competing/Unclear, and notes any
    confounder risk that bounds where the claim holds}

Integration rules:
  - A narrowed claim that ignores any of the four named fields does not pass.
  - Partial synthesis (e.g., evidence tier present, confounder absent) does not pass.
  - Restating or broadening the original does not pass.

Write artifact to simulations/discover/causal/{topic}-causal-{date}.md.
Frontmatter: topic, date, hypothesis, inertia_verdict, mechanism_complete,
evidence_aggregate_tier, confounders_identified (count), falsification_stated (true/false),
context_evidence_found (true/false).
```

---

## V-02: Formal step labeling as prerequisite (output format axis)

**Axis:** Output format — step labeling framed explicitly as a structural prerequisite that
makes falsification and evidence mechanically gradeable, not a presentational preference

**Hypothesis:** C-16 fails when steps are listed as prose bullets or numbered without names.
The failure is not ignorance of the format but a category error: teams treat labeling as
optional styling. Framing it as a load-bearing structural requirement -- with explicit
language that falsification and evidence gap sections reference steps by label and cannot
anchor to unlabeled steps -- changes the compliance calculus. The test: does framing it as
a prerequisite (rather than a format instruction) increase structured labeling adoption?

```
You are running /discover-causal for topic: {topic}.

Hypothesis under review: {hypothesis}

--- STEP LABELING REQUIREMENT ---

Before producing the mechanism pathway, read this structural rule:

Every step in the pathway must carry a persistent formal label:
  Step N -- [Name]: What changes. Who acts. Observable indicator.

Example: "Step 2 -- User encounters prompt: The system surfaces an inline suggestion.
Agent: platform. Observable: prompt impression logged in telemetry."

This is not a formatting preference -- it is a structural prerequisite. The falsification
condition and evidence gap sections in this output reference steps by their formal label.
A step labeled only by position ("the second step"), or listed as a prose bullet without a
persistent name, does not give downstream sections a stable referent. Unlabeled steps
cause falsification anchoring and evidence gap enumeration to fail mechanically, because
there is no name to anchor to.

Use the "Step N -- [Name]:" format throughout. Keep labels short and stable -- the same
name must appear in the pathway, in falsification, and in evidence gap sections.

--- INERTIA CHECK ---

Before mechanism work: does the status quo produce Y without any new feature?

INERTIA VERDICT: [Competing / Not competing / Unclear -- one sentence basis]

--- MECHANISM PATHWAY ---

Trace the causal chain from X to Y using the labeling rule above.

Minimum 3 labeled steps. If fewer than 3 can be traced with confidence, say so explicitly
("mechanism not fully traceable") rather than generating thin steps.

--- FALSIFICATION CONDITION ---

Name the mechanism break point. Reference the step by its formal label from the pathway above.

Required format:
"The mechanism fails if Step [N] -- [Name] -- does not occur, observable as [indicator]."

The label must match the step label in the pathway exactly. "Step 2 fails" without the
step name does not pass -- there is no stable referent. "If usage declines" does not pass
-- that is an outcome check, not a mechanism break.

--- CONTEXT EVIDENCE ---

For each labeled step in the pathway above, assess evidence.

Use this format (matching the pathway labels exactly):
  Step N -- [Name]: [evidence name or "no evidence"] -- [T1 / T2 / T3 / none]
    T1 = anecdotal / observational / team intuition
    T2 = correlation / A-B / usage analytics / survey
    T3 = controlled / causal-inference-grade experiment

Required outputs:
  Evidence gap steps: [list the Step N -- [Name] labels that have no supporting evidence]
  Aggregate tier: [highest tier across all steps -- T1/T2/T3/none]

List gap steps by their full label from the pathway (Step N -- Name), not by position.

--- CONFOUNDER CHECK ---

Name at least one alternative explanation for Y that does not require X and is not the
inertia/status-quo case already addressed in INERTIA CHECK.

What independently operates right now and could produce Y coincidentally with X?

--- AMEND ---

Original: {hypothesis}
Inertia verdict: {from INERTIA CHECK}
Pathway: {1-sentence mechanism summary using step labels where relevant}
Falsification: {Step N -- Name -- break condition}
Evidence gap: {step labels lacking support, from CONTEXT EVIDENCE}
Confounder finding: {alternative cause identified, or "none identified -- [reason]"}
Amended: {narrower claim -- bounded by mechanism qualifier, scope condition, and
  evidence tier; reference labeled steps where relevant}

Write artifact to simulations/discover/causal/{topic}-causal-{date}.md.
Frontmatter: topic, date, hypothesis, mechanism_complete (true/false),
pathway_steps (count), break_point_step (step label), evidence_gap_steps (list of labels),
evidence_aggregate_tier (T1/T2/T3/none), inertia_verdict,
confounders_identified (count), falsification_stated (true/false).
```

---

## V-03: Confounder/inertia hard separation (role sequence axis)

**Axis:** Role sequence — inertia check runs before the confounder section with an explicit
boundary: the confounder section excludes the inertia case by name and requires a
simultaneously-operating cause, not a "without the feature" counterfactual

**Hypothesis:** C-17 fails when confounder analysis reuses the inertia finding as its answer.
The root cause is not that teams skip confounders -- it is that the section boundary between
"does nothing also cause Y?" and "what else causes Y right now?" is unclear, so models
satisfy both with the same answer. Making the exclusion explicit ("the inertia case is NOT
included here") and naming what a valid confounder looks like (simultaneously-operating,
present during deployment) closes the conflation structurally.

```
You are running /discover-causal for topic: {topic}.

Hypothesis under review: {hypothesis}

MECHANISM PATHWAY

Trace the causal chain from X to Y. Label each step:
  Step N -- [Name]: What changes. Who acts. Observable indicator.

Minimum 3 steps. If fewer can be traced with confidence, say so explicitly rather than
generating thin steps to fill the count.

FALSIFICATION CONDITION

Name the step in the pathway above where mechanism failure would be observable.

Required format:
"The mechanism fails if Step [N] -- [Name] -- does not occur, observable as [indicator]."

The step must match a labeled row in the pathway above.

INERTIA CHECK

Does doing nothing also produce Y?

This section asks only about the status quo -- existing behaviors, trends, and workarounds
that produce Y without any new feature or intervention. It does not ask about competitors,
other teams, or simultaneously-running programs.

INERTIA VERDICT: [Competing / Not competing / Unclear -- one sentence basis]

CONFOUNDER CHECK

This section asks a DIFFERENT question from the inertia check above.

The inertia check asked: does the status quo trend toward Y over time, without any action?

This section asks: what else, operating RIGHT NOW alongside X, could independently
produce Y at the same time X is deployed?

The inertia case is EXCLUDED from this analysis.

"The status quo already does this" is the inertia verdict -- it does not count as a
confounder here. If the only alternative you can name is a restatement of the inertia
finding, you have not named a confounder.

What you are looking for -- causes that operate simultaneously, not counterfactually:
  - Competing initiatives: another feature, program, or team effort active at the same time
  - Confounding variables: factors that correlate with X adoption and independently predict
    Y (e.g., teams that adopt X early are already more motivated, so Y improves regardless)
  - Selection effects: the population that uses X differs systematically from those who do not
  - Seasonal or environmental effects: events, market trends, or external factors active
    during the same period as X's deployment

Name at least one. If none can be identified, explain why the mechanism is insulated from
simultaneously-operating confounders for this outcome type.

Explicitly state: "The inertia case (INERTIA VERDICT: [verdict]) is NOT included here as
a confounder -- it was addressed in the Inertia Check section."

CONTEXT EVIDENCE

What team-specific evidence exists that the mechanism holds and that the named confounders
are not the actual driver?

Name each piece specifically. Do not count general research as team-specific evidence.
Rate each: T1 (anecdotal), T2 (correlation), T3 (controlled).
Note which pathway step each piece supports.

If none: "No context-specific evidence found."

AMEND

Narrow the original hypothesis to reflect the mechanism, the inertia verdict, and the
confounder findings.

Original: {hypothesis}
Inertia verdict: {Competing / Not competing / Unclear}
Confounder finding: {most plausible simultaneously-operating cause, or "none identified --
  [reason why mechanism is insulated]"}
Pathway: {1-sentence mechanism summary}
Falsification: {Step N -- Name -- break condition}
Amended: {narrower claim -- bounded by mechanism qualifier and scope condition that
  distinguishes X's effect from the named confounder; incorporates inertia condition if
  status is Competing or Unclear}

Write artifact to simulations/discover/causal/{topic}-causal-{date}.md.
Frontmatter: topic, date, hypothesis, inertia_verdict, mechanism_complete (true/false),
pathway_steps (count), break_point_step (step label), confounders_identified (count),
confounder_inertia_excluded (true/false), falsification_stated (true/false),
context_evidence_found (true/false).
```

---

## V-04: Incomplete-pathway falsification anchor (lifecycle emphasis axis)

**Axis:** Lifecycle emphasis — a conditional BEST-TRACEABLE ANCHOR branch in the
falsification phase explicitly prohibits deferral when incompleteness was declared, requiring
a step-level anchor even for partial pathways

**Hypothesis:** C-18 fails when models declare incompleteness in Phase 1 and then use that
incompleteness as a reason to defer or omit falsification. The declaration that "the pathway
cannot be fully traced" is being treated as a license to skip step-level anchoring. An
explicit conditional branch in the falsification section -- with named prohibited output
forms and a required BEST-TRACEABLE ANCHOR format -- closes this by making incompleteness
change only the confidence annotation, not the structural requirement to anchor to a step.

```
You are running /discover-causal for topic: {topic}.

Hypothesis under review: {hypothesis}

=== READINESS GATE ===

Before tracing the mechanism: can you name 3 or more observable intermediate steps between
X and Y, each with a named agent and observable indicator?

If yes: proceed to MECHANISM PATHWAY.
If no: declare incompleteness now.
  Write: "PATHWAY INCOMPLETE: mechanism cannot be traced past [step description].
  Missing knowledge: [what evidence or domain knowledge is needed to complete the chain]."
  Then continue tracing what can be traced, marking unsubstantiated steps [UNCERTAIN].

Producing thin or vague steps to clear this gate -- instead of declaring incompleteness --
fails this section. Accurate self-report is the required output.

=== MECHANISM PATHWAY ===

Trace the causal chain from X to Y. Label each step:
  Step N -- [Name]: What changes. Who acts. Observable indicator.

Mark any step you cannot substantiate with [UNCERTAIN].

=== FALSIFICATION CONDITION ===

Name the mechanism break point. Reference a labeled step from the pathway above.

Required format:
"The mechanism fails if Step [N] -- [Name] -- does not occur, observable as [indicator]."

The step number and name must match a labeled row in the pathway above.

-- CONDITIONAL BRANCH: incomplete pathway --

If PATHWAY INCOMPLETE was declared in READINESS GATE, this branch applies.

You must still produce a step-anchored falsification. Do NOT write any of the following:
  - "Cannot falsify until the mechanism is better understood."
  - "Falsification is deferred pending mechanism completion."
  - "If outcome Y does not improve..." (a metric threshold, not a mechanism break)

Instead: identify the highest-confidence step that was traced -- even if only one step was
traced -- and anchor falsification there.

Required format for incomplete pathways:
"BEST-TRACEABLE ANCHOR: The mechanism fails if Step [N] -- [Name] -- does not occur,
observable as [indicator]. Note: pathway incompleteness means the chain cannot be verified
beyond step [N]. Falsification of later steps requires establishing [missing knowledge
from READINESS GATE]."

This is still a mechanism break statement -- not a deferral. Declaring incompleteness
changes the confidence annotation and adds a note, but does not exempt this section from
producing a step-level anchor. A pathway with one traceable step still produces one
falsifiable break point.

-- END CONDITIONAL BRANCH --

=== INERTIA CHECK ===

INERTIA VERDICT: [Competing / Not competing / Unclear -- one sentence basis]

=== CONFOUNDER CHECK ===

Name at least one cause of Y that does not involve X and is not the inertia case.

The inertia case was addressed above. This section names something else that could
independently produce Y right now -- a simultaneously-operating cause, not a counterfactual.

If none can be identified, explain why.

=== CONTEXT EVIDENCE ===

What team-specific evidence exists that the mechanism holds?

Name it specifically. Identify which labeled steps in the pathway have no supporting
evidence -- list them by step number and name (Step N -- Name).

Evidence gap steps: [{step labels with no supporting evidence}]
Aggregate evidence tier: T1 / T2 / T3 / none

=== AMEND ===

Original: {hypothesis}
Mechanism complete: {yes / no / partial -- and what is incomplete}
Inertia status: {from INERTIA CHECK}
Pathway: {1-sentence mechanism summary}
Falsification: {Step N -- Name -- break condition; or BEST-TRACEABLE ANCHOR if incomplete}
Evidence gap: {step labels lacking support}
Confounder finding: {alternative cause or "none identified -- [reason]"}
Amended: {narrower claim -- must include mechanism qualifier; scope condition; inertia
  condition if Competing or Unclear; note if pathway incompleteness limits the claim's
  certainty scope}

Write artifact to simulations/discover/causal/{topic}-causal-{date}.md.
Frontmatter:
  topic: {topic}
  date: {date}
  hypothesis: {original hypothesis}
  mechanism_complete: true | false | partial
  incomplete_pathway_declared: true | false
  pathway_steps: {count}
  break_point_step: {step label, or "best-traceable: Step N -- Name"}
  inertia_status: competing | not-competing | unclear
  evidence_gap_steps: [{step labels}]
  evidence_aggregate_tier: T1 | T2 | T3 | none
  confounders_identified: {count}
  falsification_stated: true | false
  context_evidence_found: true | false
```

---

## V-05: Full v3 aspirational stack (combination)

**Axes:** All four v3 axes combined: AMEND synthesis completeness (C-15) + formal step
labeling as prerequisite (C-16) + confounder/inertia hard separation (C-17) +
incomplete-pathway falsification anchor (C-18), integrated into the R2 V-05 phase structure

**Hypothesis:** All four v3 criteria can be produced in a single output by: (a) adding
`Confounder finding:` as a required AMEND field and making partial synthesis explicitly
fail, (b) framing step labeling as a load-bearing structural prerequisite rather than a
format instruction, (c) strengthening Phase 5's inertia exclusion with explicit acknowledgment
language, and (d) adding a BEST-TRACEABLE ANCHOR branch to Phase 3 that prohibits deferral
when incompleteness was declared. The expected cost is increased prompt length; the expected
gain is a 140-point output that closes all four v3 gaps simultaneously.

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

If Competing: the mechanism analysis in Phase 2 must explain what X produces that the
status quo does not. A mechanism that merely also produces Y alongside the status quo is
not a causal claim for X.

=== PHASE 1: MECHANISM READINESS ===

Before tracing, assess: can you name 3 or more observable intermediate steps between X
and Y, each with a named agent and observable indicator?

If yes: proceed.
If no: declare incompleteness now.
  Write: "PATHWAY INCOMPLETE: mechanism cannot be traced past [step]. Missing knowledge:
  [what evidence or domain knowledge is needed]."
  Then continue with what can be traced, marking unsubstantiated steps [UNCERTAIN].

Producing three thin or vague steps to clear this gate -- instead of declaring
incompleteness -- fails this phase. Accurate self-report is the required output.

=== PHASE 2: MECHANISM PATHWAY ===

Trace the causal pathway from X to Y.

STEP LABELING REQUIREMENT: Each step must carry a persistent formal label:
  Step N -- [Name]: What changes. Who acts. Observable indicator.

This is not a presentational preference -- it is a structural prerequisite. Phase 3
(falsification) and Phase 4 (evidence) reference steps by their formal label. A step listed
as a prose bullet or numbered without a persistent name has no stable referent for later
phases. Unlabeled steps make C-12 and C-13 unscoreable -- there is no name to anchor to.
Use this format throughout. The same label must appear identically in the pathway, in
falsification, and in evidence gap sections.

If inertia status from Phase 0 is Competing: at least one step must describe what X
produces that the status quo does not.

Also: is there more than one plausible causal pathway from X to Y?
  - If yes: trace the primary pathway above and name the secondary pathway in one sentence.
    Note whether the two pathways are complementary, competing, or nested.
  - If no: note that the mechanism is singular.

=== PHASE 3: FALSIFICATION ===

Name the most likely mechanism break point. Reference the step by its Phase 2 label.

Required format:
"The mechanism fails if Step [N] -- [Name] -- does not occur, observable as [indicator]."

Step number and name must match a labeled row in Phase 2 exactly. If a step is marked
[UNCERTAIN], it may still serve as a falsification anchor -- note the uncertainty in the
indicator description.

-- CONDITIONAL BRANCH: incomplete pathway --

If PATHWAY INCOMPLETE was declared in Phase 1, this branch applies.

Do NOT defer falsification. Do NOT write:
  - "Cannot falsify until the mechanism is better understood."
  - "Falsification depends on completing the pathway."
  - A metric threshold ("if Y does not improve").

Instead: identify the highest-confidence labeled step traced and anchor falsification there.

Required format:
"BEST-TRACEABLE ANCHOR: The mechanism fails if Step [N] -- [Name] -- does not occur,
observable as [indicator]. Note: pathway incompleteness means the chain cannot be verified
beyond step [N]. Further falsification requires establishing [missing knowledge from
Phase 1]."

Incompleteness changes the confidence annotation -- not the structural requirement to name
a step-level anchor. A partial pathway still produces at least one falsifiable break point.

-- END CONDITIONAL BRANCH --

Do not state falsification as a metric threshold. A metric shortfall is an outcome check.
Name where the mechanism stops working.

=== PHASE 4: CONTEXT EVIDENCE ===

Assess evidence per pathway step using the formal labels from Phase 2.

For each step:
  Step N -- [Name]: [evidence name, artifact, or "no evidence"] -- [T1 / T2 / T3 / none]
    T1 = anecdotal / observational / team intuition
    T2 = correlation / A-B / usage analytics / survey
    T3 = controlled / causal-inference-grade experiment

Reference steps by their formal Phase 2 label -- not by position or paraphrase.

Required outputs:
  Evidence gap steps: [list Step N -- [Name] labels with no supporting evidence]
  Aggregate evidence tier: [highest tier available -- T1/T2/T3/none]

Do not substitute general research for team-specific evidence. Note external evidence
separately if useful, but do not include it in the tier accounting.

=== PHASE 5: CONFOUNDER CHECK ===

This phase asks a DIFFERENT question from Phase 0.

Phase 0 asked: does the status quo trend toward Y over time, without intervention?
This phase asks: what else, operating RIGHT NOW alongside X, could independently produce Y?

The inertia case (Phase 0) is EXCLUDED from this analysis. It does not count as a
confounder -- it was answered in its own phase with its own verdict.

What you are looking for -- simultaneously-operating causes, not counterfactuals:
  - Competing initiatives active during the same deployment window
  - Confounding variables that correlate with X adoption and independently predict Y
  - Selection effects: the population using X differs from those who do not
  - Environmental or seasonal effects coinciding with X's deployment period

Name at least one alternative explanation for Y that:
  (a) does not involve X as a cause, AND
  (b) is not the inertia/status-quo case already addressed in Phase 0.

Explicitly acknowledge the exclusion: "The inertia case (Phase 0 verdict: [verdict]) is
not included here -- it was handled separately in Phase 0."

If no independently-operating cause can be identified, explain why the mechanism is
insulated from this type of confounding for this outcome type. Silence is not acceptable.

=== PHASE 6: AMEND ===

Produce a narrowed version of the hypothesis that integrates all four prior analytical
phases. This section has four required named inputs. Omitting any of them does not pass.

Required structure:
  Original: {hypothesis}
  Inertia verdict: {from Phase 0 -- Competing / Not competing / Unclear}
  Mechanism completeness: {complete / incomplete / partial -- from Phase 1}
  Evidence tier: {aggregate tier from Phase 4 -- T1/T2/T3/none}
  Confounder finding: {from Phase 5 -- name the alternative cause identified, or
    "none identified -- [reason why mechanism is insulated]"}
  Active pathway: {primary / secondary / both / singular}
  Falsification: {Step N -- Name -- break condition, or BEST-TRACEABLE ANCHOR if incomplete}
  Evidence gap: {step labels lacking support, from Phase 4}
  Amended: {narrower claim -- must include:
    (a) mechanism qualifier (what must be true in the causal chain for X to cause Y),
    (b) scope condition (population, context, or timeframe),
    (c) inertia condition if Phase 0 is Competing or Unclear: "in contexts where the
        status quo does not already [produce Y]" or "invalid if inertia check shows
        [condition]",
    (d) confounder note if Phase 5 named a plausible alternative cause that bounds
        where the claim holds -- e.g., "provided [confounder] is not the active driver"}

Integration rules:
  - A narrowed claim that ignores the inertia verdict does not pass.
  - A narrowed claim that ignores mechanism incompleteness does not pass.
  - A narrowed claim that omits the confounder finding (when one was identified) does
    not pass. Partial synthesis is not synthesis -- all four fields must be reflected.
  - Restating the original hypothesis does not pass. Broadening it does not pass.

=== PHASE 7: ARTIFACT ===

Write to simulations/discover/causal/{topic}-causal-{date}.md.
Frontmatter:
  topic: {topic}
  date: {date}
  hypothesis: {original hypothesis}
  inertia_status: competing | not-competing | unclear
  mechanism_complete: true | false | partial
  incomplete_pathway_declared: true | false
  pathway_steps: {count}
  secondary_pathway_noted: true | false
  pathway_relationship: complementary | competing | nested | singular
  break_point_step: {step label, or "best-traceable: Step N -- Name"}
  falsification_stated: true | false
  evidence_aggregate_tier: T1 | T2 | T3 | none
  evidence_gap_steps: [{step labels with no supporting evidence}]
  confounders_identified: {count}
  confounder_inertia_excluded: true | false
  context_evidence_found: true | false
```
