Written to `simulations/quest/variations/discover-causal-variations-R4-2026-03-17.md`.

---

## discover-causal Variations R4

| # | Label | Axis | Target |
|---|-------|------|--------|
| V-01 | Evidence field separation | Output format | C-19 only |
| V-02 | Unconditional inertia incorporation | Phrasing register | C-20 only |
| V-03 | Inertia verdict as load-bearing anchor | Inertia framing | C-20 only |
| V-04 | Evidence separation + unconditional inertia | Output format + integration | C-19+C-20 |
| V-05 | Full v4 aspirational stack | Combination | C-19+C-20+all |

---

### Design decisions

**C-19 (evidence gap vs evidence tier are separate fields):**

The failure mode is a category error, not ignorance of T1/T2/T3. Teams conflate "which steps lack evidence" with "how strong is the evidence we have." V-01 and V-04 add a **FIELD SEPARATION NOTE / REQUIRED OUTPUTS block** with:
- Explicit orthogonality statement
- The null-gap counterexample: *"a pathway where all steps have T1 evidence has gap: 'none' but tier: T1"*
- "Do not merge them. Do not omit either."

Both fields appear as separate named entries in AMEND.

**C-20 (inertia incorporation is unconditional):**

The R3 escape hatch was "if Competing or Unclear" — Not-competing cases silently dropped. Three approaches tested:
- **V-02** (phrasing register): INERTIA COMMITMENT paragraph + three-case mandatory table in AMEND Amended + explicit integration rule *"Conditioning inertia incorporation on Competing or Unclear does not pass"*
- **V-03** (inertia framing): CARRY-FORWARD block in the inertia section itself, activated by the AMEND clause — the Not-competing case is given affirmative required language: *"confirm that X is the causal driver and the status quo does not independently produce Y"*
- **V-04/V-05**: Both combined

**V-05 expected score: 150/150.** Base is R3 V-05 (140/140). Two surgical changes: Phase 4 gets FIELD INDEPENDENCE NOTE; Phase 6 AMEND (c) replaces the conditional with a three-case mandatory table plus an integration rule that names the escape hatch by form.
scorecard.

---

## V-01: Evidence field separation (output format axis)

**Axis:** Output format -- CONTEXT EVIDENCE section gains a FIELD SEPARATION NOTE that names
evidence gap and evidence tier as two distinct required outputs with different meanings;
AMEND gains both as separate named fields

**Hypothesis:** C-19 fails when AMEND has evidence gap (step labels) but no evidence tier
field, or when the two fields are merged into one entry. The rubric gap is not unfamiliarity
with the scale -- it is a category error: teams treat "which steps lack evidence" and "what
quality is the evidence we have" as the same question. An explicit separation note with an
example ("a pathway with no gap steps still carries evidence tier T1") and a "do not merge
them" rule changes the output structure. Base: R3 V-04. C-20 gap (conditional inertia)
intentionally preserved for single-axis isolation.

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

These fields are orthogonal. A pathway where all steps have T1 evidence has no gap steps
("none") but still carries evidence tier T1 for the evidence it has. A pathway where step
3 has no evidence and step 1-2 have T2 evidence has gap steps ("Step 3 -- [Name]") and
evidence tier T2. Do not substitute one for the other.

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

## V-02: Unconditional inertia incorporation (phrasing register axis)

**Axis:** Phrasing register -- the INERTIA CHECK section gains an explicit INERTIA COMMITMENT
statement; AMEND gains three-case mandatory language replacing the "if Competing/Unclear"
conditional; integration rules prohibit conditional incorporation by name

**Hypothesis:** C-20 fails because models follow the literal "if Competing or Unclear" form
and correctly produce inertia language -- but only when the verdict is non-trivial. The Not
competing case gets silently dropped, which is precisely the most common verdict in healthy
feature decisions. A three-case mandatory table ("if Competing / if Unclear / if Not competing")
with an explicit prohibition on conditional forms closes the escape hatch. Base: R3 V-01.
C-19 gap (no separate evidence gap field in AMEND) intentionally preserved for single-axis
isolation.

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

INERTIA COMMITMENT: This verdict is not conditional. It must explicitly shape the amended
claim in the AMEND section below, regardless of which verdict value applies. There is no
verdict that makes the inertia finding irrelevant to a causal claim.

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
  Amended: {narrower claim that incorporates all four prior findings, including the inertia
    verdict unconditionally. The Amended claim must explicitly reference the inertia finding
    regardless of its value -- use the appropriate form for the verdict:
      If Competing: scope the claim to contexts where the status quo does not already
        produce Y via [the competing mechanism]; or declare the feature causally redundant
        in contexts where the status quo already delivers Y
      If Not competing: confirm explicitly that X is the causal driver and that the status
        quo does not independently produce Y under the claimed conditions -- the absence of
        inertia competition is a positive finding that bounds where X's causal claim holds
      If Unclear: qualify the causal scope with the condition that status-quo independence
        has not been established -- the claim holds only if inertia is ruled out for this
        context
    The Amended claim must also include: mechanism qualifier, scope condition, and any
    confounder risk that bounds where the claim holds.}

Integration rules:
  - A narrowed claim that ignores any of the four named fields does not pass.
  - Conditioning inertia incorporation on the verdict being Competing or Unclear does not
    pass -- all three verdict values require explicit incorporation in the amended claim.
  - "Inertia: Not competing -- no adjustment needed" is not explicit incorporation. The Not
    competing verdict must shape the amended claim text, not be noted and then dropped.
  - Partial synthesis (e.g., evidence tier present, confounder absent) does not pass.
  - Restating or broadening the original does not pass.

Write artifact to simulations/discover/causal/{topic}-causal-{date}.md.
Frontmatter: topic, date, hypothesis, inertia_verdict, mechanism_complete,
evidence_aggregate_tier, confounders_identified (count), falsification_stated (true/false),
context_evidence_found (true/false).
```

---

## V-03: Inertia verdict as load-bearing anchor (inertia framing axis)

**Axis:** Inertia framing -- the inertia section produces a CARRY-FORWARD commitment with
verdict-specific language; AMEND explicitly references and activates the commitment for all
three verdict values; the framing positions inertia as a gate, not a check

**Hypothesis:** C-20 fails not because the prompt omits inertia from AMEND but because the
model treats inertia as a negative-only finding -- "if not competing, nothing to add."
Structural reframing: the inertia section produces a named CARRY-FORWARD block that the AMEND
section must activate regardless of verdict. Making the Not competing case have explicit
required language ("confirm that X is the causal driver and that the status quo does not
independently produce Y") removes the implicit assumption that a clean inertia check requires
no amended text. Base: R3 V-03 (confounder/inertia hard separation). C-19 gap intentionally
preserved.

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

CARRY-FORWARD: Regardless of which verdict applies above, the amended claim in AMEND must
explicitly incorporate this finding. All three verdict values are load-bearing -- there is
no verdict that makes inertia irrelevant to the causal claim. Use the form appropriate to
the verdict:

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

Omitting the inertia verdict from the amended claim, or treating it as relevant only when
Competing or Unclear, does not pass. Reference the CARRY-FORWARD form above in AMEND.

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

Write artifact to simulations/discover/causal/{topic}-causal-{date}.md.
Frontmatter: topic, date, hypothesis, inertia_verdict, mechanism_complete (true/false),
pathway_steps (count), break_point_step (step label), confounders_identified (count),
confounder_inertia_excluded (true/false), falsification_stated (true/false),
context_evidence_found (true/false), inertia_incorporated_unconditionally (true/false).
```

---

## V-04: Evidence separation + unconditional inertia (combined: C-19+C-20)

**Axes:** Output format (evidence field separation) + integration (unconditional inertia
incorporation) -- both C-19 and C-20 targeted simultaneously in a clean non-phase structure
based on R3 V-02 (formal step labeling)

**Hypothesis:** C-19 and C-20 are independent structural gaps -- adding them together in a
single clean prompt without the full 7-phase stack tests whether the two fixes are
complementary and non-conflicting. C-19 is closed by the REQUIRED OUTPUTS block in CONTEXT
EVIDENCE and two separate AMEND fields. C-20 is closed by an unconditional inertia note in
INERTIA CHECK and a three-case mandatory AMEND clause with explicit prohibition on the
conditional form. Expected: both C-19 and C-20 pass while C-10 (multiple pathways) remains
unaddressed.

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

These fields are orthogonal. A pathway where all steps have T1 evidence has gap: "none"
but tier: T1. A pathway where step 2 lacks evidence and step 1 has T3 evidence has gap:
"Step 2 -- [Name]" and tier: T3. One does not substitute for the other.

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
    pass -- all three verdict values require explicit reference in the amended claim.
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

## V-05: Full v4 aspirational stack (combination)

**Axes:** All v4 axes combined -- FIELD INDEPENDENCE NOTE in Phase 4 for C-19; fully
unconditional three-case inertia in Phase 6 AMEND for C-20; all prior v3 criteria maintained
from R3 V-05 (140/140 baseline)

**Hypothesis:** All v4 criteria can be produced in a single output by adding (a) a FIELD
INDEPENDENCE NOTE in Phase 4 that names evidence gap and evidence tier as orthogonal fields
with an explicit prohibition on merging and an example of the null-gap case, and (b) replacing
the Phase 6 AMEND (c) clause from "if Competing or Unclear" to a three-case mandatory table
with an explicit "no verdict value makes inertia incorporation optional" integration rule.
Both changes are compatible with the R3 V-05 phase structure. Expected ceiling: 150/150.

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
    missing; a pathway where all steps have T1 evidence has gap steps: "none" but still
    carries aggregate evidence tier: T1; produce both fields in every output]

These fields are orthogonal: gap steps names which steps lack evidence; aggregate tier
rates the quality of the evidence that is present. One does not substitute for the other.
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
  Mechanism completeness: {complete / incomplete / partial -- from Phase 1}
  Evidence tier: {aggregate tier from Phase 4 -- T1/T2/T3/none}
  Evidence gap: {step labels lacking support from Phase 4 -- or "none"; this is a separate
    field from Evidence tier -- having one does not satisfy the other; a pathway with no
    gap steps still requires this field}
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
  - A narrowed claim that ignores the inertia verdict does not pass -- no verdict value
    makes inertia incorporation optional; conditioning it on Competing or Unclear does not
    pass.
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
