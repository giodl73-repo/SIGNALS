Written to `simulations/quest/variations/discover-causal-variations-R7-2026-03-17.md`.

---

## R7 Variations Summary

**New criterion targeted:** C-26 -- falsification anchor co-located with incompleteness declaration (Phase 1, not Phase 3)

**Base:** R6 V-05 (175/175 v6, 175/180 v7 -- fails only C-26)

| # | Label | Axis | C-26 mechanism | Expected |
|---|-------|------|----------------|----------|
| V-01 | Phase 1 structural anchor | Role sequence | SUB-STEP format at Phase 1, no "does not pass" language | ~175/180 |
| V-02 | Phase 3 downstream prohibition | Phrasing register | C-26 PROHIBITED FORM in Phase 3 only, Phase 1 unchanged | ~175/180 |
| V-03 | Phase 1 co-located prohibition | Phrasing register | "does not pass" in Phase 1 inline, no sub-step format | ~180/180 |
| V-04 | Phase 1 structural + prohibition | Role seq + phrasing | Sub-step AND "does not pass" both at Phase 1 | ~180/180 |
| V-05 | Full R7 stack | Combination | V-04 + Phase 3 confirmation + Phase 6 integration rule | 180/180 |

**Three key isolation tests:**

1. **V-01 vs V-03** -- does structural sequencing (SUB-STEP format) or prohibition naming ("does not pass") produce Phase 1 anchors in responses? If both pass, co-location alone is the mechanism. If only V-03 passes, the prohibition language is load-bearing.

2. **V-02 control** -- Phase 3 names the C-26 prohibition but Phase 1 has no anchor requirement. Expected FAIL C-26 -- establishes that downstream naming cannot substitute for co-location at the production point.

3. **V-04 vs V-05** -- Phase-1-only dual enforcement vs. adding Phase 3 confirmation and Phase 6 integration rule. If V-04 already achieves 180/180, the downstream sites add no pass probability.

**C-26 structural note:** Unlike C-24 (which requires the deferral prohibition to be *named*), C-26's pass condition is structural proximity -- the anchor must *appear* in Phase 1. C-26 is more like C-18 (structural result required) than C-24 (prohibited form must be named). V-02's expected failure would confirm this distinction.
s the mechanism.

**V-02 isolation test:** Phase 3 names the C-26 prohibition but Phase 1 still has no anchor requirement. Expected FAIL C-26 -- a model declaring PATHWAY INCOMPLETE in Phase 1 has no anchor cue at that point; the Phase 3 prohibition arrives too late. This would establish that the prohibition must be co-located with the production point, not placed downstream.

**Single-axis:** V-01, V-02, V-03 each vary one mechanism. V-04 combines V-01 + V-03 (both Phase 1). V-05 adds Phase 3 confirmation and Phase 6 integration rule.

---

## V-01: Phase 1 structural anchor requirement (role sequence axis)

**Axis:** Role sequence -- Phase 1 MECHANISM READINESS gains a mandatory PRELIMINARY ANCHOR sub-step that must be produced immediately after the PATHWAY INCOMPLETE declaration, before Phase 2 tracing continues. Phase 3 CONDITIONAL BRANCH is updated to confirm and extend the Phase 1 anchor rather than introducing a fresh one. No explicit "does not pass" language for C-26 at Phase 1 -- the requirement is structural, not prohibition-named.

**Hypothesis:** R6 V-05 places the anchor requirement in Phase 3, meaning a model declaring PATHWAY INCOMPLETE in Phase 1 has no anchor obligation until Phase 3. A structural sub-step at Phase 1 ("produce this before continuing") co-locates the anchor production with the declaration -- closing the deferral window by sequencing, not by prohibition. The hypothesis: a required format at Phase 1 (sub-step structure) is sufficient to produce Phase 1 anchors in responses, satisfying C-26. The PROHIBITED FORM absence tests whether structural enforcement alone passes C-26 or whether the escape-hatch naming is also required. C-24 and C-25 preserved from R6 V-05 baseline.

```
You are running /discover-causal for topic: {topic}.

Hypothesis under review: {hypothesis}
(Claim: X causes Y. Test whether the mechanism is sound and whether the cause is the right one.)

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

=== PHASE 1: MECHANISM READINESS + PRELIMINARY ANCHOR ===

Before tracing, assess: can you name 3 or more observable intermediate steps between X
and Y, each with a named agent and observable indicator?

If yes: proceed to Phase 2.

If no: complete both sub-steps below before proceeding to Phase 2.

  SUB-STEP 1 -- Incompleteness declaration:
  Write: "PATHWAY INCOMPLETE: mechanism cannot be traced past [step]. Missing knowledge:
  [what evidence or domain knowledge is needed]."
  Then continue tracing in Phase 2 what can be traced, marking unsubstantiated steps
  [UNCERTAIN].

  SUB-STEP 2 -- Preliminary falsification anchor (required immediately after SUB-STEP 1):
  Name the highest-confidence step you can trace as a preliminary falsification anchor.
  Produce it here, before Phase 2 tracing begins.

  Required format:
  "PRELIMINARY ANCHOR: The mechanism most likely fails if Step [N] -- [Name] -- does not
  occur, observable as [indicator]. Chain traceability ends here. Further falsification
  requires establishing [missing knowledge from SUB-STEP 1]."

  Even one traceable step produces one falsifiable break point. An incomplete pathway
  still requires an anchor. Incompleteness changes the confidence annotation; it does not
  remove the requirement to name a step-level anchor here before Phase 2.

Producing three thin or vague steps to clear the readiness gate -- instead of declaring
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

If PATHWAY INCOMPLETE was declared in Phase 1, a PRELIMINARY ANCHOR is already on record
from Phase 1 SUB-STEP 2. This branch confirms and extends it.

Confirm the Phase 1 anchor. If Phase 2 tracing revealed additional labeled steps with
higher confidence than the Phase 1 preliminary anchor, update to the highest-confidence
step now on record.

Required format:
"BEST-TRACEABLE ANCHOR: The mechanism fails if Step [N] -- [Name] -- does not occur,
observable as [indicator]. Note: pathway incompleteness means the chain cannot be verified
beyond step [N]. Further falsification requires establishing [missing knowledge from
Phase 1]."

PROHIBITED FORM: Declaring incompleteness and deferring or omitting step-level
falsification does not pass. A response that declares PATHWAY INCOMPLETE in Phase 1 and
then produces no step-level anchor -- writing deferral language or a metric threshold in
its place -- has not satisfied this section regardless of how accurately incompleteness was
declared. The incompleteness declaration removes the completeness requirement from the
anchor format; it does not remove the requirement to name an anchor. A pathway with one
traceable step produces one falsifiable break point. Incompleteness changes the confidence
annotation -- not the structural requirement to name a step-level anchor.

This branch confirms the Phase 1 anchor. It does not introduce fresh deferral.

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

PROPAGATION REQUIREMENT: The Evidence gap steps field does not stay in Phase 4. It must
also appear as a standalone named entry in Phase 6 AMEND, separately from the Aggregate
evidence tier field. Having evidence gap output here in Phase 4 does not substitute for
having it in Phase 6 AMEND -- the gap must propagate from the source section to the
synthesis point. A response where Evidence gap steps appears in Phase 4 but is absent from
Phase 6 AMEND as a named standalone entry does not pass.

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
  Falsification: {Step N -- Name -- break condition, or BEST-TRACEABLE ANCHOR if incomplete;
    for incomplete pathways, confirm the Phase 1 PRELIMINARY ANCHOR here, updated for any
    additional steps traced in Phase 2}
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
  - Declaring incompleteness and deferring or omitting step-level falsification does not
    pass -- incompleteness changes the confidence annotation, not the structural requirement
    to name a step-level anchor; a PATHWAY INCOMPLETE response still carries a Falsification:
    field with a BEST-TRACEABLE ANCHOR value, not a deferral statement.
  - Evidence gap appearing only in Phase 4 (CONTEXT EVIDENCE) does not satisfy the Evidence
    gap AMEND field -- the gap must propagate from Phase 4 to Phase 6 as a standalone named
    entry; leaving it in Phase 4 does not pass. Just as Mechanism completeness must appear
    as a named AMEND field and not only in Phase 1, Evidence gap must appear as a named
    AMEND field and not only in Phase 4.
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
  preliminary_anchor_declared: true | false
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

---

## V-02: Phase 3 C-26 PROHIBITED FORM -- downstream naming (phrasing register axis)

**Axis:** Phrasing register -- Phase 3 CONDITIONAL BRANCH gains a new PROHIBITED FORM block that explicitly names C-26 as a failure mode: "A response that declares PATHWAY INCOMPLETE in Phase 1 and produces no Phase 1 anchor does not pass -- the preliminary anchor must appear at the Phase 1 declaration point, not first appear here." Phase 1 is unchanged from R6 V-05 (no sub-step structure, no Phase 1 anchor requirement). C-24 and C-25 preserved from R6 V-05.

**Hypothesis:** C-26 names the prohibited form (absent Phase 1 anchor) downstream -- in Phase 3, where Phase 3 is already the anchor production point for R6 V-05. The hypothesis is that naming the prohibition in Phase 3 without restructuring Phase 1 fails C-26 -- a model declaring PATHWAY INCOMPLETE in Phase 1 has no anchor cue at that point; the Phase 3 prohibition arrives too late to change Phase 1 behavior. Comparison to V-01: V-01 adds structural requirement at Phase 1; V-02 adds prohibition naming at Phase 3. If V-01 passes C-26 and V-02 fails, the load-bearing element is co-location (structural proximity), not prohibition naming alone.

```
You are running /discover-causal for topic: {topic}.

Hypothesis under review: {hypothesis}
(Claim: X causes Y. Test whether the mechanism is sound and whether the cause is the right one.)

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

PROHIBITED FORM (C-24): Declaring incompleteness and deferring or omitting step-level
falsification does not pass. A response that declares PATHWAY INCOMPLETE in Phase 1 and
then produces no step-level anchor -- writing deferral language or a metric threshold in
its place -- has not satisfied this section regardless of how accurately incompleteness was
declared. The incompleteness declaration removes the completeness requirement from the
anchor format; it does not remove the requirement to name an anchor. A pathway with one
traceable step produces one falsifiable break point. Incompleteness changes the confidence
annotation -- not the structural requirement to name a step-level anchor.

PROHIBITED FORM (C-26): A response that declares PATHWAY INCOMPLETE in Phase 1 and
produces no preliminary anchor at the Phase 1 declaration point does not pass. The
falsification anchor must appear at the moment of the incompleteness declaration -- in
Phase 1, not first here in Phase 3. A response where Phase 1 has no anchor and Phase 3
introduces the anchor for the first time has deferred the anchor to Phase 3, not co-located
it with the declaration. The requirement is structural proximity: the anchor must be
produced at the declaration point.

Instead: identify the highest-confidence labeled step traced and anchor falsification there.

Required format:
"BEST-TRACEABLE ANCHOR: The mechanism fails if Step [N] -- [Name] -- does not occur,
observable as [indicator]. Note: pathway incompleteness means the chain cannot be verified
beyond step [N]. Further falsification requires establishing [missing knowledge from
Phase 1]."

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

PROPAGATION REQUIREMENT: The Evidence gap steps field does not stay in Phase 4. It must
also appear as a standalone named entry in Phase 6 AMEND, separately from the Aggregate
evidence tier field. Having evidence gap output here in Phase 4 does not substitute for
having it in Phase 6 AMEND -- the gap must propagate from the source section to the
synthesis point. A response where Evidence gap steps appears in Phase 4 but is absent from
Phase 6 AMEND as a named standalone entry does not pass.

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
  - Declaring incompleteness and deferring or omitting step-level falsification does not
    pass -- incompleteness changes the confidence annotation, not the structural requirement
    to name a step-level anchor; a PATHWAY INCOMPLETE response still carries a Falsification:
    field with a BEST-TRACEABLE ANCHOR value, not a deferral statement.
  - Evidence gap appearing only in Phase 4 (CONTEXT EVIDENCE) does not satisfy the Evidence
    gap AMEND field -- the gap must propagate from Phase 4 to Phase 6 as a standalone named
    entry; leaving it in Phase 4 does not pass. Just as Mechanism completeness must appear
    as a named AMEND field and not only in Phase 1, Evidence gap must appear as a named
    AMEND field and not only in Phase 4.
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

---

## V-03: Phase 1 C-26 PROHIBITED FORM -- co-located naming (phrasing register axis)

**Axis:** Phrasing register -- Phase 1 declaration section gains an explicit PROHIBITED FORM statement naming the absent-anchor case as a failure mode: "Declaring incompleteness and proceeding to Phase 2 without immediately producing a step-anchored preliminary anchor here does not pass." The required format for the preliminary anchor is specified in Phase 1. Phase 1 does NOT use sub-step labeling (contrast with V-01). Phase 3 CONDITIONAL BRANCH is updated to confirm and extend. C-24 and C-25 preserved from R6 V-05.

**Hypothesis:** V-01 uses structural sub-steps to require the anchor at Phase 1; V-03 uses prohibition naming without sub-step restructuring. The hypothesis: naming the absence as a failure mode at Phase 1 (co-located with the production point) is the minimal change sufficient to produce C-26-passing responses. If V-03 passes C-26 while V-01 fails, the load-bearing mechanism is the "does not pass" language. If both pass, co-location (at any level of explicitness) is sufficient. If neither passes without the sub-step format, then structural sequencing is required, not just prohibition naming.

```
You are running /discover-causal for topic: {topic}.

Hypothesis under review: {hypothesis}
(Claim: X causes Y. Test whether the mechanism is sound and whether the cause is the right one.)

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

  Immediately after this declaration -- before Phase 2 -- name the highest-confidence step
  you can trace as a preliminary falsification anchor.

  Required format:
  "PRELIMINARY ANCHOR: The mechanism most likely fails if Step [N] -- [Name] -- does not
  occur, observable as [indicator]. Chain traceability ends here. Further falsification
  requires establishing [missing knowledge above]."

  PROHIBITED FORM: Declaring incompleteness and proceeding to Phase 2 without producing
  this preliminary anchor here does not pass. The anchor must appear at this declaration
  point -- not deferred to Phase 3. Phase 3 will confirm and extend it, but Phase 1 must
  produce it first. Incompleteness changes the confidence annotation; it does not remove
  the requirement to name a step-level anchor here. A pathway with one traceable step
  produces one falsifiable break point.

  Then continue tracing in Phase 2 what can be traced, marking unsubstantiated steps
  [UNCERTAIN].

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

If PATHWAY INCOMPLETE was declared in Phase 1, a PRELIMINARY ANCHOR is on record from
Phase 1. Confirm and extend it here.

Confirm the Phase 1 anchor. If Phase 2 tracing revealed additional labeled steps with
higher confidence than the Phase 1 preliminary anchor, update to the highest-confidence
step now on record.

Required format:
"BEST-TRACEABLE ANCHOR: The mechanism fails if Step [N] -- [Name] -- does not occur,
observable as [indicator]. Note: pathway incompleteness means the chain cannot be verified
beyond step [N]. Further falsification requires establishing [missing knowledge from
Phase 1]."

PROHIBITED FORM: Declaring incompleteness and deferring or omitting step-level
falsification does not pass. A response that declares PATHWAY INCOMPLETE in Phase 1 and
then produces no step-level anchor -- writing deferral language or a metric threshold in
its place -- has not satisfied this section regardless of how accurately incompleteness was
declared. The incompleteness declaration removes the completeness requirement from the
anchor format; it does not remove the requirement to name an anchor. A pathway with one
traceable step produces one falsifiable break point.

This branch confirms the Phase 1 anchor. It does not introduce fresh deferral.

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

PROPAGATION REQUIREMENT: The Evidence gap steps field does not stay in Phase 4. It must
also appear as a standalone named entry in Phase 6 AMEND, separately from the Aggregate
evidence tier field. Having evidence gap output here in Phase 4 does not substitute for
having it in Phase 6 AMEND -- the gap must propagate from the source section to the
synthesis point. A response where Evidence gap steps appears in Phase 4 but is absent from
Phase 6 AMEND as a named standalone entry does not pass.

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
  Falsification: {Step N -- Name -- break condition, or BEST-TRACEABLE ANCHOR if incomplete;
    for incomplete pathways, carry the Phase 1 PRELIMINARY ANCHOR here, updated for any
    additional steps traced in Phase 2}
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
  - Declaring incompleteness and deferring or omitting step-level falsification does not
    pass -- incompleteness changes the confidence annotation, not the structural requirement
    to name a step-level anchor; a PATHWAY INCOMPLETE response still carries a Falsification:
    field with a BEST-TRACEABLE ANCHOR value, not a deferral statement.
  - Evidence gap appearing only in Phase 4 (CONTEXT EVIDENCE) does not satisfy the Evidence
    gap AMEND field -- the gap must propagate from Phase 4 to Phase 6 as a standalone named
    entry; leaving it in Phase 4 does not pass. Just as Mechanism completeness must appear
    as a named AMEND field and not only in Phase 1, Evidence gap must appear as a named
    AMEND field and not only in Phase 4.
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
  preliminary_anchor_declared: true | false
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

---

## V-04: Phase 1 structural + Phase 1 PROHIBITED FORM (role sequence + phrasing register combination)

**Axes:** Role sequence (V-01 Phase 1 sub-step structure) + phrasing register (V-03 Phase 1 PROHIBITED FORM). Both C-26 enforcement mechanisms applied at Phase 1: structural sequencing (SUB-STEP 1 + SUB-STEP 2) AND naming the absent-anchor case as a failure mode at the same Phase 1 point. Phase 3 updated to confirmation-and-extension language. C-24 PROHIBITED FORM in Phase 3 retained. C-25 PROPAGATION REQUIREMENT in Phase 4 and Phase 6 retained from R6 V-05.

**Hypothesis:** V-01 tests structural sequencing alone; V-03 tests Phase 1 prohibition naming alone. V-04 combines both at Phase 1 without adding Phase 3 or Phase 6 C-26 language. The dual-site pattern within a single phase (structural requirement + prohibition naming) parallels how C-22 closes C-20 (positive rule + named prohibited form together, both at the same location). The question is whether Phase-1-only dual enforcement is sufficient for C-26, or whether Phase 3 confirmation language and Phase 6 integration rule (V-05) add incremental pass probability.

```
You are running /discover-causal for topic: {topic}.

Hypothesis under review: {hypothesis}
(Claim: X causes Y. Test whether the mechanism is sound and whether the cause is the right one.)

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

=== PHASE 1: MECHANISM READINESS + PRELIMINARY ANCHOR ===

Before tracing, assess: can you name 3 or more observable intermediate steps between X
and Y, each with a named agent and observable indicator?

If yes: proceed to Phase 2.

If no: complete both sub-steps below before proceeding to Phase 2.

  SUB-STEP 1 -- Incompleteness declaration:
  Write: "PATHWAY INCOMPLETE: mechanism cannot be traced past [step]. Missing knowledge:
  [what evidence or domain knowledge is needed]."
  Then continue tracing in Phase 2 what can be traced, marking unsubstantiated steps
  [UNCERTAIN].

  SUB-STEP 2 -- Preliminary falsification anchor (required immediately after SUB-STEP 1):
  Name the highest-confidence step you can trace as a preliminary falsification anchor.
  Produce it here, before Phase 2 tracing begins.

  Required format:
  "PRELIMINARY ANCHOR: The mechanism most likely fails if Step [N] -- [Name] -- does not
  occur, observable as [indicator]. Chain traceability ends here. Further falsification
  requires establishing [missing knowledge from SUB-STEP 1]."

  PROHIBITED FORM: Declaring incompleteness and proceeding to Phase 2 without producing
  this preliminary anchor in SUB-STEP 2 does not pass. The anchor must appear here, at the
  declaration point, before Phase 2. Phase 3 will confirm and extend the anchor, but Phase 1
  must produce it first. Deferring the anchor to Phase 3 -- or to any downstream phase --
  does not satisfy this sub-step regardless of how accurately incompleteness was declared.
  Incompleteness changes the confidence annotation; it does not remove the requirement to
  name a step-level anchor here. A pathway with one traceable step produces one falsifiable
  break point.

Producing three thin or vague steps to clear the readiness gate -- instead of declaring
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

If PATHWAY INCOMPLETE was declared in Phase 1, a PRELIMINARY ANCHOR is already on record
from Phase 1 SUB-STEP 2. This branch confirms and extends it.

Confirm the Phase 1 anchor. If Phase 2 tracing revealed additional labeled steps with
higher confidence than the Phase 1 preliminary anchor, update to the highest-confidence
step now on record.

Required format:
"BEST-TRACEABLE ANCHOR: The mechanism fails if Step [N] -- [Name] -- does not occur,
observable as [indicator]. Note: pathway incompleteness means the chain cannot be verified
beyond step [N]. Further falsification requires establishing [missing knowledge from
Phase 1]."

PROHIBITED FORM: Declaring incompleteness and deferring or omitting step-level
falsification does not pass. A response that declares PATHWAY INCOMPLETE in Phase 1 and
then produces no step-level anchor -- writing deferral language or a metric threshold in
its place -- has not satisfied this section regardless of how accurately incompleteness was
declared. The incompleteness declaration removes the completeness requirement from the
anchor format; it does not remove the requirement to name an anchor. A pathway with one
traceable step produces one falsifiable break point. Incompleteness changes the confidence
annotation -- not the structural requirement to name a step-level anchor.

This branch confirms the Phase 1 anchor. It does not introduce fresh deferral.

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

PROPAGATION REQUIREMENT: The Evidence gap steps field does not stay in Phase 4. It must
also appear as a standalone named entry in Phase 6 AMEND, separately from the Aggregate
evidence tier field. Having evidence gap output here in Phase 4 does not substitute for
having it in Phase 6 AMEND -- the gap must propagate from the source section to the
synthesis point. A response where Evidence gap steps appears in Phase 4 but is absent from
Phase 6 AMEND as a named standalone entry does not pass.

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
  Falsification: {Step N -- Name -- break condition, or BEST-TRACEABLE ANCHOR if incomplete;
    for incomplete pathways, confirm the Phase 1 PRELIMINARY ANCHOR here, updated for any
    additional steps traced in Phase 2}
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
  - Declaring incompleteness and deferring or omitting step-level falsification does not
    pass -- incompleteness changes the confidence annotation, not the structural requirement
    to name a step-level anchor; a PATHWAY INCOMPLETE response still carries a Falsification:
    field with a BEST-TRACEABLE ANCHOR value, not a deferral statement.
  - Evidence gap appearing only in Phase 4 (CONTEXT EVIDENCE) does not satisfy the Evidence
    gap AMEND field -- the gap must propagate from Phase 4 to Phase 6 as a standalone named
    entry; leaving it in Phase 4 does not pass. Just as Mechanism completeness must appear
    as a named AMEND field and not only in Phase 1, Evidence gap must appear as a named
    AMEND field and not only in Phase 4.
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
  preliminary_anchor_declared: true | false
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

---

## V-05: Full R7 aspirational stack (combination)

**Axes:** All R7 axes combined -- C-26 addressed at four sites: (a) Phase 1 SUB-STEP structure (V-01 pattern); (b) Phase 1 PROHIBITED FORM (V-03/V-04 pattern); (c) Phase 3 confirmation-and-extension with C-24 PROHIBITED FORM; (d) Phase 6 integration rule naming the Phase 1 anchor requirement for incomplete pathways. C-24 dual-site from R6 V-05 retained (Phase 3 + Phase 6). C-25 dual-site from R6 V-05 retained (Phase 4 + Phase 6). All R5 and R6 structures preserved.

**Hypothesis:** R6 V-05 scores 175/175 under v6 and 175/180 under v7 (fails only C-26). V-05 closes C-26 with the maximum possible prompt-level enforcement: structural co-location at Phase 1 (sub-step), named prohibition at Phase 1 (does not pass), Phase 3 becomes confirmation (not origination), and Phase 6 integration rules explicitly reference the Phase 1 preliminary anchor requirement. The cross-site pattern mirrors how C-22/C-24 were closed across their respective versions: a model that skips Phase 1 sees the requirement again at Phase 3; a model that misses Phase 3 sees the integration rule at Phase 6. Expected ceiling: 180/180 Golden.

```
You are running /discover-causal for topic: {topic}.

Hypothesis under review: {hypothesis}
(Claim: X causes Y. Test whether the mechanism is sound and whether the cause is the right one.)

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

=== PHASE 1: MECHANISM READINESS + PRELIMINARY ANCHOR ===

Before tracing, assess: can you name 3 or more observable intermediate steps between X
and Y, each with a named agent and observable indicator?

If yes: proceed to Phase 2.

If no: complete both sub-steps below before proceeding to Phase 2.

  SUB-STEP 1 -- Incompleteness declaration:
  Write: "PATHWAY INCOMPLETE: mechanism cannot be traced past [step]. Missing knowledge:
  [what evidence or domain knowledge is needed]."
  Then continue tracing in Phase 2 what can be traced, marking unsubstantiated steps
  [UNCERTAIN].

  SUB-STEP 2 -- Preliminary falsification anchor (required immediately after SUB-STEP 1):
  Name the highest-confidence step you can trace as a preliminary falsification anchor.
  Produce it here, before Phase 2 tracing begins.

  Required format:
  "PRELIMINARY ANCHOR: The mechanism most likely fails if Step [N] -- [Name] -- does not
  occur, observable as [indicator]. Chain traceability ends here. Further falsification
  requires establishing [missing knowledge from SUB-STEP 1]."

  PROHIBITED FORM: Declaring incompleteness and proceeding to Phase 2 without producing
  this preliminary anchor in SUB-STEP 2 does not pass. The anchor must appear here, at the
  declaration point, before Phase 2. Phase 3 will confirm and extend it, but Phase 1 must
  produce it first. Deferring the anchor to Phase 3 -- writing "will determine in Phase 3"
  or equivalent -- does not satisfy this sub-step regardless of how accurately incompleteness
  was declared. Incompleteness changes the confidence annotation; it does not remove the
  requirement to name a step-level anchor here. Even one traceable step produces one
  falsifiable break point.

Producing three thin or vague steps to clear the readiness gate -- instead of declaring
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

If PATHWAY INCOMPLETE was declared in Phase 1, a PRELIMINARY ANCHOR is already on record
from Phase 1 SUB-STEP 2. This branch confirms and extends it.

Confirm the Phase 1 anchor. If Phase 2 tracing revealed additional labeled steps with
higher confidence than the Phase 1 preliminary anchor, update to the highest-confidence
step now on record.

Required format:
"BEST-TRACEABLE ANCHOR: The mechanism fails if Step [N] -- [Name] -- does not occur,
observable as [indicator]. Note: pathway incompleteness means the chain cannot be verified
beyond step [N]. Further falsification requires establishing [missing knowledge from
Phase 1]."

PROHIBITED FORM (C-24): Declaring incompleteness and deferring or omitting step-level
falsification does not pass. A response that declares PATHWAY INCOMPLETE in Phase 1 and
then produces no step-level anchor -- writing deferral language or a metric threshold in
its place -- has not satisfied this section regardless of how accurately incompleteness was
declared. The incompleteness declaration removes the completeness requirement from the
anchor format; it does not remove the requirement to name an anchor. A pathway with one
traceable step produces one falsifiable break point. Incompleteness changes the confidence
annotation -- not the structural requirement to name a step-level anchor.

This branch confirms the Phase 1 anchor. It does not introduce fresh deferral.

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

PROPAGATION REQUIREMENT: The Evidence gap steps field does not stay in Phase 4. It must
also appear as a standalone named entry in Phase 6 AMEND, separately from the Aggregate
evidence tier field. Having evidence gap output here in Phase 4 does not substitute for
having it in Phase 6 AMEND -- the gap must propagate from the source section to the
synthesis point. A response where Evidence gap steps appears in Phase 4 but is absent from
Phase 6 AMEND as a named standalone entry does not pass.

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
  Falsification: {Step N -- Name -- break condition, or BEST-TRACEABLE ANCHOR if incomplete;
    for incomplete pathways, this field must carry the Phase 1 PRELIMINARY ANCHOR, updated
    for any additional steps traced in Phase 2; a Falsification field that first names the
    anchor here without a corresponding Phase 1 PRELIMINARY ANCHOR does not pass C-26}
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
  - Declaring incompleteness and deferring or omitting step-level falsification does not
    pass -- incompleteness changes the confidence annotation, not the structural requirement
    to name a step-level anchor; a PATHWAY INCOMPLETE response still carries a Falsification:
    field with a BEST-TRACEABLE ANCHOR value, not a deferral statement.
  - For incomplete pathways, the Falsification field must carry an anchor that was first
    produced in Phase 1 -- not first introduced here. A response where Phase 1 contains no
    PRELIMINARY ANCHOR and Phase 6 Falsification carries the first anchor does not pass
    C-26 -- the anchor appeared at the synthesis point, not at the declaration point.
  - Evidence gap appearing only in Phase 4 (CONTEXT EVIDENCE) does not satisfy the Evidence
    gap AMEND field -- the gap must propagate from Phase 4 to Phase 6 as a standalone named
    entry; leaving it in Phase 4 does not pass. Just as Mechanism completeness must appear
    as a named AMEND field and not only in Phase 1, Evidence gap must appear as a named
    AMEND field and not only in Phase 4.
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
  preliminary_anchor_declared: true | false
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

---

```json
{"r7_variations": 5, "new_criterion_targeted": "C-26", "base": "R6 V-05 (175/175 under v6 rubric, 175/180 under v7 rubric)", "single_axis": ["V-01: C-26 role sequence -- Phase 1 structural sub-step, no Phase 1 PROHIBITED FORM", "V-02: C-26 phrasing register -- Phase 3 PROHIBITED FORM naming C-26 absence, no Phase 1 change", "V-03: C-26 phrasing register -- Phase 1 PROHIBITED FORM at declaration point, no sub-step format"], "combined": ["V-04: Phase 1 structural sub-step + Phase 1 PROHIBITED FORM, Phase-1-only dual enforcement", "V-05: Full R7 stack -- Phase 1 sub-step + Phase 1 PROHIBITED FORM + Phase 3 confirmation + Phase 6 integration rule"], "isolation_tests": ["V-01 vs V-03: structural sub-step vs prohibition naming -- which mechanism produces Phase 1 anchor in responses?", "V-02 control: downstream prohibition (Phase 3) without Phase 1 structural change -- expected FAIL C-26", "V-04 vs V-05: Phase-1-only dual enforcement vs full cross-site enforcement -- does Phase 6 rule add incremental pass probability?"], "expected_ceiling": "180/180 (V-04, V-05)", "c26_distinction": "C-26 pass condition is structural proximity in the response (anchor appears at Phase 1), not prohibition naming -- compare to C-24 which requires prohibition naming; C-26 is more like C-18 (structural requirement) than C-24 (prohibited form naming)"}
```
