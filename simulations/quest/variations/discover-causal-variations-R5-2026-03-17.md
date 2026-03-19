**discover-causal Variations R5** written to `simulations/quest/variations/discover-causal-variations-R5-2026-03-17.md`.

---

## Summary

| # | Label | Axis | Target | Base |
|---|-------|------|--------|------|
| V-01 | Null-gap counterexample as instantiated proof | Output format | C-21 only | R4 V-01 |
| V-02 | Named prohibition of conditional inertia form | Phrasing register | C-22 only | R4 V-03 |
| V-03 | Mechanism completeness as standalone AMEND field | Lifecycle emphasis | C-23 only | R4 V-04 |
| V-04 | Null-gap proof + named prohibition | Output format + phrasing register | C-21+C-22 | R4 V-04 |
| V-05 | Full v5 aspirational stack | Combination | C-21+C-22+C-23+all | R4 V-05 |

---

### Three single-axis changes explained

**V-01 → C-21:** R4 V-01 *described* orthogonality ("a pathway with no gap steps still carries tier T1") but didn't *demonstrate* it. C-21's load-bearing element is the instantiated null-gap case as a named output example: `Evidence gap: none / Evidence tier: T1` shown as a concrete working state, with the explanation that omitting the tier when gap is empty is the specific category error. Description → demonstration.

**V-02 → C-22:** R4 V-03 had the unconditional CARRY-FORWARD structure with correct Not-competing language, but never named the prohibited escape hatch by form. The model can follow "always incorporate inertia" and still produce the conditional form while believing it complies. V-02 adds the PROHIBITED FORM block in INERTIA CHECK ("conditioning on Competing or Unclear does not pass") and repeats the prohibition verbatim in AMEND's integration rules — twice, at production point and synthesis point.

**V-03 → C-23:** R4 V-04 had mechanism completeness embedded in the amended clause as a modifier ("note if pathway incompleteness limits the claim's certainty scope"). V-03 extracts it as a standalone named AMEND field `Mechanism completeness: {complete / incomplete at Step N / partial}` with an explicit rule: "a mechanism qualifier embedded within the Amended clause text does not satisfy this field."

**V-05 expected ceiling: 165/165.** All three changes are structurally independent and apply to different sections of the R4 V-05 prompt without conflict.
med AMEND field):**

R4 V-04 and V-05 both had mechanism completeness accessible — V-04 through "Mechanism complete:
{yes / no / partial}" in AMEND, V-05 through "Mechanism completeness: {complete / incomplete /
partial}" in Phase 6. The v5 requirement is that this appear as a *standalone named entry*
separate from the amended clause text. R4 V-04's amended clause said "note if pathway
incompleteness limits the claim's certainty scope" — embedding the mechanism qualifier in the
clause body rather than as a named field. R4 V-05 had the named field. V-03 targets the V-04
pattern: base is R4 V-04, change is extracting mechanism completeness into its own AMEND field
rather than leaving it as a clause-embedded note.

**V-05 expected score: 165/165.** Base is R4 V-05 (150/150 on v4 rubric). Three surgical
additions: Phase 4 gains a NULL-GAP COUNTEREXAMPLE block (C-21); Phase 0 and Phase 6 gain the
explicit conditional-form prohibition (C-22); Phase 6 AMEND gains mechanism completeness as a
standalone named field separate from the amended clause (C-23).

---

## V-01: Null-gap counterexample as instantiated proof (output format axis)

**Axis:** Output format — the FIELD SEPARATION NOTE in CONTEXT EVIDENCE gains a
NULL-GAP COUNTEREXAMPLE block that instantiates the null-gap state as a concrete named
output ("gap: none, tier: T1"), proving field orthogonality by example rather than by
description

**Hypothesis:** C-21 fails when the separation note describes orthogonality abstractly but
does not demonstrate the null-gap case. A prompt that says "no gap steps still requires the
Evidence tier field" describes the rule but doesn't anchor it to a concrete output state. A
model following a description can still collapse the tier field when gap is empty — the
null-gap case requires instantiation ("gap: none, tier: T1 — this is a valid output state
meaning all steps have evidence, and T1 is the quality of that evidence") to prevent the
category error. Base: R4 V-01. C-22 gap (no named prohibition) and C-23 gap (no standalone
mechanism completeness field) intentionally preserved for single-axis isolation.

```
You are running /discover-causal for topic: {topic}.

Hypothesis under review: {hypothesis}
(Claim: X causes Y. Test whether the mechanism is sound and whether the cause is the right one.)

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

Declaring incompleteness changes the confidence annotation and adds a note, but does not
exempt this section from producing a step-level anchor. A pathway with one traceable step
still produces one falsifiable break point.

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

For each labeled step in the pathway above, assess evidence:
  Step N -- [Name]: [evidence name or "no evidence"] -- [T1 / T2 / T3 / none]
    T1 = anecdotal / observational / team intuition
    T2 = correlation / A-B / usage analytics / survey
    T3 = controlled / causal-inference-grade experiment

FIELD SEPARATION NOTE: The following two outputs have different meanings. Produce them
as two separate named entries. Do not merge them into a single field. Do not omit either.

  Evidence gap steps: [list of Step N -- [Name] labels that have no supporting evidence;
    write "none" if every step has evidence -- the absence of a gap does not eliminate
    this field; this output answers: which steps lack support?]

  Evidence tier: [T1/T2/T3/none -- aggregate quality rating across all evidence evaluated;
    write the highest tier available across all steps that do have evidence; this output
    answers: how strong is the evidence that exists? -- independent of which steps are
    missing]

These fields are orthogonal. One does not substitute for the other.

NULL-GAP COUNTEREXAMPLE: The following is a valid, required output state:
  Evidence gap steps: none
  Evidence tier: T1
This state means every step in the pathway has supporting evidence, and that evidence is
anecdotal-grade. "Gap: none" does not mean "no Evidence tier field needed" -- it means
every step is covered. The Evidence tier field is still required and still populated: T1.
A response that omits Evidence tier because gap is empty is making a category error -- it
is conflating "no missing steps" with "no evidence quality to report." The null-gap case
proves the fields are separate: gap answers which steps are missing; tier answers what
quality the present evidence has. Both are always required. Both always carry a value.

=== AMEND ===

Original: {hypothesis}
Mechanism complete: {yes / no / partial -- and what is incomplete}
Inertia status: {from INERTIA CHECK}
Pathway: {1-sentence mechanism summary}
Falsification: {Step N -- Name -- break condition; or BEST-TRACEABLE ANCHOR if incomplete}
Evidence gap: {step labels lacking support, from CONTEXT EVIDENCE; or "none -- all steps
  supported"}
Evidence tier: {aggregate T1/T2/T3/none quality rating, from CONTEXT EVIDENCE}
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
  evidence_gap_steps: [{step labels; or "none"}]
  evidence_aggregate_tier: T1 | T2 | T3 | none
  confounders_identified: {count}
  falsification_stated: true | false
  context_evidence_found: true | false
```

---

## V-02: Named prohibition of conditional inertia form (phrasing register axis)

**Axis:** Phrasing register -- the INERTIA CHECK section names the prohibited conditional
form explicitly ("conditioning inertia incorporation on the verdict being Competing or Unclear
does not pass"); AMEND gain the same prohibition in the integration rules; the form is named
at both the production point and the synthesis point

**Hypothesis:** C-22 fails when the prompt states the unconditional rule positively
("inertia is always incorporated") but does not name the conditional form as a failure mode
by its form. A model reading only the positive rule constructs the conditional form and
believes it complies -- "if Not competing, nothing to add" feels consistent with "inertia
is relevant." The escape hatch must be closed by name, at the point where the inertia verdict
is produced (so the model cannot forget it by the time AMEND is reached) and again in AMEND's
integration rules (so synthesis explicitly prohibits it). Base: R4 V-03 (which had
unconditional CARRY-FORWARD language but did not name the conditional form as prohibited).
C-21 gap (no null-gap instantiation) and C-23 gap (no standalone mechanism completeness
field) intentionally preserved for single-axis isolation.

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

CARRY-FORWARD: This verdict must explicitly shape the amended claim in AMEND, regardless
of which value applies. All three verdict values are load-bearing -- there is no verdict
that makes inertia irrelevant to the causal claim.

  Competing: the amended claim must be scoped to contexts where the status quo does not
    already produce Y through [the competing mechanism], or declare the feature causally
    redundant where the status quo already delivers Y.

  Not competing: the amended claim must explicitly confirm that X is the causal driver and
    that the status quo does not independently produce Y -- the absence of inertia
    competition is a positive bounding condition that must appear in the claim, not be
    silently assumed.

  Unclear: the amended claim must qualify its causal scope with the condition that status-
    quo independence has not been established -- the claim holds only if inertia can be
    ruled out for this context and user population.

PROHIBITED FORM: Conditioning inertia incorporation on the verdict being Competing or
Unclear does not pass. A response that incorporates the inertia finding only when the
verdict is Competing or Unclear, and silently drops it when the verdict is Not competing,
has not satisfied the unconditional requirement. "Not competing -- no adjustment needed"
is a conditional form. The Not competing verdict must explicitly shape the amended claim;
it cannot be noted and then treated as having no claim-bounding force.

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
Inertia verdict: {Competing / Not competing / Unclear -- from INERTIA CHECK}
Confounder finding: {most plausible simultaneously-operating cause, or "none identified --
  [reason why mechanism is insulated]"}
Pathway: {1-sentence mechanism summary}
Falsification: {Step N -- Name -- break condition}
Amended: {narrower claim -- must include:
  (a) mechanism qualifier -- what must hold in the causal chain for X to cause Y
  (b) scope condition -- the population, context, or timeframe where the claim holds
  (c) inertia incorporation -- required regardless of verdict value; activate the
      CARRY-FORWARD language from INERTIA CHECK appropriate to the verdict:
        Competing: scope to contexts where status quo does not already produce Y
        Not competing: confirm X is the causal driver and the status quo does not
          independently produce Y under these conditions
        Unclear: qualify scope with the assumption that status-quo independence must hold
  (d) confounder note -- how the named confounder bounds where the claim holds (if
      a confounder was identified)}

Integration rules:
  - A narrowed claim that ignores any of the four named fields does not pass.
  - Conditioning inertia incorporation on the verdict being Competing or Unclear does not
    pass -- all three verdict values require explicit reference in the amended claim.
  - "Inertia: Not competing -- no adjustment needed" is not explicit incorporation. The Not
    competing verdict must shape the amended claim text, not be noted and then dropped.
  - Partial synthesis (e.g., evidence tier present, confounder absent) does not pass.
  - Restating or broadening the original does not pass.

Write artifact to simulations/discover/causal/{topic}-causal-{date}.md.
Frontmatter: topic, date, hypothesis, inertia_verdict, mechanism_complete (true/false),
pathway_steps (count), break_point_step (step label), confounders_identified (count),
confounder_inertia_excluded (true/false), falsification_stated (true/false),
context_evidence_found (true/false), inertia_incorporated_unconditionally (true/false).
```

---

## V-03: Mechanism completeness as standalone AMEND field (lifecycle emphasis axis)

**Axis:** Lifecycle emphasis -- the AMEND required structure gains a standalone
"Mechanism completeness:" named field separate from the amended clause text; the lifecycle
rule that mechanism incompleteness must produce a named field entry (not only a clause
modifier) is stated explicitly

**Hypothesis:** C-23 fails when mechanism completeness appears as a qualifier embedded in
the amended clause ("X causes Y when the mechanism is fully traceable") rather than as a
standalone named AMEND field. The information is present but not in the required form. The
fix is structural: mechanism completeness must be extracted from the amended clause and given
its own field name in the AMEND required structure, parallel to inertia verdict and evidence
tier. An integration rule stating "mechanism completeness embedded in the amended clause
text does not satisfy this field" closes the loophole. Base: R4 V-04 (had all AMEND
fields including inertia, evidence gap, evidence tier, and confounder, but mechanism
completeness was embedded in the amended clause notes rather than named as a standalone
field). C-21 gap (no null-gap instantiation) and C-22 gap (no named prohibition of
conditional inertia form) intentionally preserved for single-axis isolation.

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
condition and evidence sections reference steps by their formal label. A step labeled only
by position ("the second step"), or listed as a prose bullet without a persistent name,
does not give downstream sections a stable referent. Unlabeled steps cause falsification
anchoring and evidence gap enumeration to fail mechanically.

Use the "Step N -- [Name]:" format throughout. Keep labels short and stable -- the same
name must appear in the pathway, in falsification, and in evidence gap sections.

--- INERTIA CHECK ---

Before mechanism work: does the status quo produce Y without any new feature?

Assess existing behaviors, workarounds, and market forces that independently trend toward Y.

INERTIA VERDICT: [Competing / Not competing / Unclear -- one sentence basis]

This verdict must appear explicitly in the AMEND section below regardless of its value.
All three verdict values are meaningful for the causal claim. Not competing is not a neutral
finding -- it is a positive bounding condition that must appear in the amended claim.

--- MECHANISM PATHWAY ---

Trace the causal chain from X to Y using the labeling rule above.

Before producing steps: can you trace 3 or more observable intermediate steps with named
agents and observable indicators?

If yes: proceed.
If no: declare incompleteness now.
  Write: "PATHWAY INCOMPLETE: mechanism cannot be traced past [step]. Missing knowledge:
  [what evidence or domain knowledge is needed]."
  Then trace what can be traced, marking unsubstantiated steps [UNCERTAIN].
  This incompleteness declaration will appear as a named field in AMEND -- it is not
  just a note on the pathway; it shapes the amended claim and must be retrievable.

Producing thin or vague steps to avoid incompleteness declaration fails this section.

--- FALSIFICATION CONDITION ---

Name the mechanism break point. Reference the step by its formal label from the pathway above.

Required format:
"The mechanism fails if Step [N] -- [Name] -- does not occur, observable as [indicator]."

The label must match the step label in the pathway exactly.

-- CONDITIONAL BRANCH: incomplete pathway --

If PATHWAY INCOMPLETE was declared above, this branch applies.

Do NOT defer falsification ("cannot falsify until the mechanism is clearer"). Identify
the highest-confidence labeled step traced and anchor falsification there.

Required format:
"BEST-TRACEABLE ANCHOR: The mechanism fails if Step [N] -- [Name] -- does not occur,
observable as [indicator]. Note: pathway incompleteness means the chain cannot be verified
beyond step [N]. Falsification of later steps requires establishing [missing knowledge]."

-- END CONDITIONAL BRANCH --

--- CONTEXT EVIDENCE ---

For each labeled step in the pathway above, assess evidence.

Use this format (matching the pathway labels exactly):
  Step N -- [Name]: [evidence name or "no evidence"] -- [T1 / T2 / T3 / none]
    T1 = anecdotal / observational / team intuition
    T2 = correlation / A-B / usage analytics / survey
    T3 = controlled / causal-inference-grade experiment

REQUIRED OUTPUTS -- produce both as separate named entries. These are not the same field.
Do not merge them. Do not omit either.

  Evidence gap: [list Step N -- [Name] labels with no supporting evidence; write "none --
    all steps supported" if no gaps exist; this field answers: which steps lack evidence?]

  Evidence tier: [T1/T2/T3/none -- aggregate quality rating across all evidence evaluated;
    this field answers: how strong is the evidence that exists?; write the highest tier
    across all steps that have evidence, regardless of whether gaps exist]

These fields are orthogonal. A pathway where all steps have T1 evidence has gap: "none"
but tier: T1. One does not substitute for the other.

--- CONFOUNDER CHECK ---

Name at least one alternative explanation for Y that does not require X and is not the
inertia/status-quo case already addressed in INERTIA CHECK.

What independently operates right now and could produce Y coincidentally with X?

--- AMEND ---

Produce the narrowed hypothesis by completing all required named fields below. Each field
corresponds to an analytical output from a prior section. Omitting any field does not pass.

Required structure:
  Original: {hypothesis}
  Inertia verdict: {Competing / Not competing / Unclear -- from INERTIA CHECK}
  Mechanism completeness: {complete / incomplete at Step N / partial -- from MECHANISM
    PATHWAY; this is a standalone named field, not a modifier embedded in the amended
    clause text; if PATHWAY INCOMPLETE was declared, write "incomplete at Step N" here;
    if the mechanism was fully traced, write "complete"; a mechanism qualifier in the
    amended clause text does not satisfy this field}
  Evidence gap: {step labels lacking support, from CONTEXT EVIDENCE; or "none -- all
    steps supported"}
  Evidence tier: {T1/T2/T3/none -- aggregate quality rating, from CONTEXT EVIDENCE}
  Confounder finding: {alternative cause identified, or "none identified -- [reason]"}
  Falsification: {Step N -- Name -- break condition}
  Amended: {narrower claim -- required components:
    (a) mechanism qualifier: what must hold in the causal chain for X to cause Y
    (b) scope condition: population, context, or timeframe where the claim holds
    (c) inertia incorporation: reference the inertia verdict explicitly -- required for ALL
        three verdict values, not only when Competing or Unclear:
          Competing: scope the claim to contexts where the status quo does not already
            produce Y via [the competing mechanism]
          Not competing: confirm that X is the causal driver and that the status quo does
            not independently produce Y under the claimed conditions
          Unclear: qualify the causal scope with the condition that status-quo independence
            has not been established for this context
    (d) evidence tier note: qualify the claim's certainty by the aggregate evidence tier}

Integration rules:
  - Evidence gap and Evidence tier are separate AMEND fields -- merging them into a single
    entry does not pass; omitting either does not pass.
  - Mechanism completeness is a named AMEND field -- it must appear as a standalone entry
    labeled "Mechanism completeness:" not as a qualifier embedded in the amended clause text.
    A clause that says "X causes Y when the mechanism is fully traceable" satisfies the
    mechanism qualifier in (a) but does not satisfy the Mechanism completeness: field.
  - A narrowed claim that ignores any required field does not pass.
  - Restating or broadening the original does not pass.

Write artifact to simulations/discover/causal/{topic}-causal-{date}.md.
Frontmatter:
  topic: {topic}
  date: {date}
  hypothesis: {original hypothesis}
  mechanism_complete: true | false | partial
  incomplete_pathway_declared: true | false
  pathway_steps: {count}
  break_point_step: {step label}
  inertia_verdict: competing | not-competing | unclear
  evidence_gap_steps: [{step labels; or "none"}]
  evidence_aggregate_tier: T1 | T2 | T3 | none
  confounders_identified: {count}
  falsification_stated: true | false
  context_evidence_found: true | false
```

---

## V-04: Null-gap proof + named prohibition (output format + phrasing register)

**Axes:** Output format (null-gap counterexample as instantiated proof) + phrasing register
(explicit named prohibition of conditional inertia form) -- C-21 and C-22 targeted
simultaneously; C-23 gap intentionally preserved for clean two-axis test

**Hypothesis:** C-21 and C-22 are independent structural gaps that can be addressed
simultaneously without conflicting. C-21 is closed by adding a NULL-GAP COUNTEREXAMPLE
block to the FIELD SEPARATION NOTE in CONTEXT EVIDENCE. C-22 is closed by adding an explicit
PROHIBITED FORM statement to the INERTIA CHECK section and naming it again in AMEND's
integration rules. Both fixes are compatible with the R4 V-04 phase structure. Expected:
C-21 and C-22 both pass; C-23 fails (mechanism completeness remains embedded in amended
clause text, not extracted as a standalone field). Base: R4 V-04.

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
condition and evidence sections reference steps by their formal label. A step labeled only
by position ("the second step"), or listed as a prose bullet without a persistent name,
does not give downstream sections a stable referent. Unlabeled steps cause falsification
anchoring and evidence gap enumeration to fail mechanically.

Use the "Step N -- [Name]:" format throughout. Keep labels short and stable.

--- INERTIA CHECK ---

Before mechanism work: does the status quo produce Y without any new feature?

Assess existing behaviors, workarounds, and market forces that independently trend toward Y.

INERTIA VERDICT: [Competing / Not competing / Unclear -- one sentence basis]

This verdict must appear explicitly in the AMEND section below regardless of its value.
All three verdict values are meaningful for the causal claim. Not competing is not a neutral
finding -- it is a positive bounding condition that must appear in the amended claim.

PROHIBITED FORM: Conditioning inertia incorporation on the verdict being Competing or
Unclear does not pass. A response that incorporates inertia only when the verdict is
Competing or Unclear, and treats Not competing as requiring no amended-claim adjustment,
has not satisfied the unconditional requirement. All three verdict values must shape the
amended claim explicitly. "Not competing -- no adjustment needed" is the conditional form
that fails.

--- MECHANISM PATHWAY ---

Trace the causal chain from X to Y using the labeling rule above.

Minimum 3 labeled steps. If fewer than 3 can be traced with confidence, say so explicitly
("mechanism not fully traceable") rather than generating thin steps.

--- FALSIFICATION CONDITION ---

Name the mechanism break point. Reference the step by its formal label from the pathway above.

Required format:
"The mechanism fails if Step [N] -- [Name] -- does not occur, observable as [indicator]."

The label must match the step label in the pathway exactly. "Step 2 fails" without the
step name does not pass. A metric threshold ("if usage declines") does not pass -- name
where the mechanism stops working.

--- CONTEXT EVIDENCE ---

For each labeled step in the pathway above, assess evidence.

Use this format (matching the pathway labels exactly):
  Step N -- [Name]: [evidence name or "no evidence"] -- [T1 / T2 / T3 / none]
    T1 = anecdotal / observational / team intuition
    T2 = correlation / A-B / usage analytics / survey
    T3 = controlled / causal-inference-grade experiment

REQUIRED OUTPUTS -- produce both as separate named entries. These are not the same field.
Do not merge them. Do not omit either.

  Evidence gap: [list Step N -- [Name] labels with no supporting evidence; write "none --
    all steps supported" if no gaps exist; this field answers: which steps lack evidence?]

  Evidence tier: [T1/T2/T3/none -- aggregate quality rating across all evidence evaluated;
    this field answers: how strong is the evidence that exists?; write the highest tier
    across all steps that have evidence, regardless of whether gaps exist]

These fields are orthogonal. One does not substitute for the other.

NULL-GAP COUNTEREXAMPLE: The following is a valid, required output state:
  Evidence gap: none -- all steps supported
  Evidence tier: T1
This state means every step in the pathway has evidence, and that evidence is anecdotal-
grade. "Gap: none" does not mean "Evidence tier field is not needed" -- it means every
step is covered, and the tier of that coverage is T1. A response that omits Evidence tier
because no steps are missing is conflating the two fields. The null-gap case proves the
orthogonality is real: even with no missing steps, the tier field carries independent
information (the quality grade of the evidence that is present). Both fields are always
required. Both always carry a value.

--- CONFOUNDER CHECK ---

Name at least one alternative explanation for Y that does not require X and is not the
inertia/status-quo case already addressed in INERTIA CHECK.

What independently operates right now and could produce Y coincidentally with X?

--- AMEND ---

Original: {hypothesis}
Inertia verdict: {from INERTIA CHECK}
Pathway: {1-sentence mechanism summary using step labels where relevant}
Falsification: {Step N -- Name -- break condition}
Evidence gap: {step labels lacking support, from CONTEXT EVIDENCE; or "none -- all
  steps supported"}
Evidence tier: {T1/T2/T3/none -- aggregate quality rating, from CONTEXT EVIDENCE}
Confounder finding: {alternative cause identified, or "none identified -- [reason]"}
Amended: {narrower claim -- required components:
  (a) mechanism qualifier: what must hold in the causal chain for X to cause Y
  (b) scope condition: population, context, or timeframe where the claim holds
  (c) inertia incorporation: reference the inertia verdict explicitly -- required for ALL
      three verdict values, not only when Competing or Unclear:
        Competing: scope the claim to contexts where the status quo does not already
          produce Y via [the competing mechanism]
        Not competing: confirm that X is the causal driver and that the status quo does
          not independently produce Y under the claimed conditions
        Unclear: qualify the causal scope with the condition that status-quo independence
          has not been established for this context
  (d) evidence tier note: qualify the claim's certainty by the aggregate evidence tier}

Integration rules:
  - Evidence gap and Evidence tier are separate AMEND fields -- merging them into a single
    entry does not pass; omitting either does not pass.
  - Conditioning inertia incorporation on the verdict being Competing or Unclear does not
    pass -- all three verdict values require explicit reference in the amended claim. The
    Not competing verdict must shape the amended claim; it cannot be acknowledged and then
    treated as carrying no claim-bounding force.
  - A narrowed claim that ignores any required field does not pass.
  - Restating or broadening the original does not pass.

Write artifact to simulations/discover/causal/{topic}-causal-{date}.md.
Frontmatter:
  topic: {topic}
  date: {date}
  hypothesis: {original hypothesis}
  mechanism_complete: true | false
  pathway_steps: {count}
  break_point_step: {step label}
  inertia_verdict: competing | not-competing | unclear
  evidence_gap_steps: [{step labels; or "none"}]
  evidence_aggregate_tier: T1 | T2 | T3 | none
  confounders_identified: {count}
  falsification_stated: true | false
  context_evidence_found: true | false
```

---

## V-05: Full v5 aspirational stack (combination)

**Axes:** All v5 axes combined -- NULL-GAP COUNTEREXAMPLE in Phase 4 for C-21; PROHIBITED
FORM statement in Phase 0 and Phase 6 integration rules for C-22; standalone "Mechanism
completeness:" field in Phase 6 AMEND for C-23; all prior v4 criteria maintained from R4
V-05 (150/150 baseline)

**Hypothesis:** All three v5 criteria can be added to the R4 V-05 phase structure with
three surgical changes that do not conflict with any prior phase structure:
(a) Phase 4 FIELD INDEPENDENCE NOTE gains a NULL-GAP COUNTEREXAMPLE block that instantiates
"gap: none, tier: T1" as a named concrete case (C-21);
(b) Phase 0 gains a PROHIBITED FORM statement that names "conditioning on Competing or
Unclear does not pass" at the point of verdict production; Phase 6 integration rules repeat
the prohibition by name (C-22);
(c) Phase 6 AMEND required structure gains "Mechanism completeness:" as a standalone named
field entry separate from the amended clause, with an explicit rule that embedding it in
the clause text does not satisfy the field (C-23).
All R4 V-05 structures are preserved. Expected ceiling: 165/165.

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

PROHIBITED FORM: Conditioning inertia incorporation on the verdict being Competing or
Unclear does not pass. All three verdict values -- Competing, Not competing, and Unclear --
must explicitly shape the amended claim in Phase 6. The Not competing verdict is a positive
bounding condition, not a neutral finding. A response that incorporates the inertia verdict
only when it is Competing or Unclear, and drops it when Not competing, has failed the
unconditional requirement regardless of how correctly the Competing and Unclear cases are
handled. "Not competing -- no adjustment needed" is the conditional form that fails.

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
phases. Unlabeled steps make falsification anchoring and evidence gap enumeration fail
mechanically -- there is no name to anchor to. Use this format throughout. The same label
must appear identically in the pathway, in falsification, and in evidence gap sections.

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

FIELD INDEPENDENCE NOTE: The following two outputs measure different things. Produce them
as two separate named entries. Do not merge them into a single entry. Do not omit either.

  Evidence gap steps: [list Step N -- [Name] labels with no supporting evidence; write
    "none" if every step has evidence -- the absence of a gap does not eliminate this
    field; this output answers: which steps lack supporting evidence?]

  Aggregate evidence tier: [highest tier available -- T1/T2/T3/none; this output answers:
    what is the quality of the evidence that exists? -- independent of which steps are
    missing; produce both fields in every output]

These fields are orthogonal: gap steps names which steps lack evidence; aggregate tier
rates the quality of the evidence that is present. One does not substitute for the other.

NULL-GAP COUNTEREXAMPLE: The following is a valid, required output state:
  Evidence gap steps: none
  Aggregate evidence tier: T1
This state means every step in the pathway has supporting evidence, and that evidence is
anecdotal-grade. The Evidence gap steps field still appears; it carries the value "none."
The Aggregate evidence tier field still appears; it carries the value T1. A response that
omits Aggregate evidence tier because all steps are covered is making the category error
that these fields guard against -- it is conflating "no missing steps" with "no tier to
report." The null-gap state proves the fields are independent: gap answers which steps are
missing (here: none); tier answers what quality the present evidence has (here: T1). Both
are always required. Both always carry a value, even when gap is none.

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

Produce a narrowed version of the hypothesis that integrates all prior analytical phases.
This section has required named inputs from each phase. Omitting any of them does not pass.

Required structure:
  Original: {hypothesis}
  Inertia verdict: {from Phase 0 -- Competing / Not competing / Unclear}
  Mechanism completeness: {complete / incomplete at Step N / partial -- from Phase 1;
    this is a standalone named field; a mechanism qualifier embedded within the Amended
    clause text ("X causes Y when the mechanism is fully traceable") does not satisfy this
    field; the completeness status must appear here as a named entry separate from the
    amended clause; write "complete" if Phase 1 found no gaps; write "incomplete at Step N"
    if PATHWAY INCOMPLETE was declared; write "partial" if some steps are [UNCERTAIN]}
  Evidence tier: {aggregate tier from Phase 4 -- T1/T2/T3/none}
  Evidence gap: {step labels lacking support from Phase 4 -- or "none"; this is a separate
    field from Evidence tier -- having one does not satisfy the other; a pathway with no
    gap steps still requires this field, carrying the value "none"}
  Confounder finding: {from Phase 5 -- name the alternative cause identified, or
    "none identified -- [reason why mechanism is insulated]"}
  Active pathway: {primary / secondary / both / singular}
  Falsification: {Step N -- Name -- break condition, or BEST-TRACEABLE ANCHOR if incomplete}
  Amended: {narrower claim -- must include:
    (a) mechanism qualifier (what must be true in the causal chain for X to cause Y),
    (b) scope condition (population, context, or timeframe),
    (c) inertia incorporation -- required regardless of verdict value; no verdict makes
        inertia incorporation optional; use the form appropriate to the verdict:
          Competing: scope to contexts where the status quo does not already produce Y via
            [the competing mechanism]; or declare the feature causally redundant where the
            status quo already delivers Y
          Not competing: confirm explicitly that X is the causal driver and that the status
            quo does not independently produce Y -- this is a positive bounding condition
            that must appear in the amended claim, not be silently assumed
          Unclear: qualify the causal scope with the condition that status-quo independence
            has not been established -- the claim holds only if inertia can be ruled out for
            this context and population
    (d) confounder note if Phase 5 named a plausible alternative cause that bounds where
        the claim holds -- e.g., "provided [confounder] is not the active driver"}

Integration rules:
  - Evidence tier and Evidence gap are separate AMEND fields -- merging them or omitting
    either does not pass.
  - Mechanism completeness is a standalone named AMEND field -- embedding it within the
    amended clause text does not satisfy this field requirement.
  - A narrowed claim that ignores the inertia verdict does not pass -- no verdict value
    makes inertia incorporation optional.
  - Conditioning inertia incorporation on the verdict being Competing or Unclear does not
    pass -- all three verdict values require explicit reference in the amended claim. The
    Not competing case must shape the amended claim text; acknowledging it and then treating
    it as carrying no bounding force is the conditional form that fails.
  - A narrowed claim that ignores mechanism incompleteness does not pass.
  - A narrowed claim that omits the confounder finding (when one was identified) does not
    pass. Partial synthesis is not synthesis -- all fields must be reflected.
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
  evidence_gap_steps: [{step labels with no supporting evidence; or "none"}]
  confounders_identified: {count}
  confounder_inertia_excluded: true | false
  context_evidence_found: true | false
```
