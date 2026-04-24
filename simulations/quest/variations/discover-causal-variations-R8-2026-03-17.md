Written to `simulations/quest/variations/discover-causal-variations-R8-2026-03-17.md`.

---

## R8 Variations Summary

**Base:** R7 V-05 (195/195 under v8 -- ceiling)  
**New criteria targeted:** C-27, C-28, C-29

| # | Label | Axis | Change | Expected |
|---|-------|------|--------|----------|
| V-01 | C-27 inline prohibition | Phrasing register | PROHIBITED FORM block removed; "does not pass" embedded inline in SUB-STEP 2 header | 195 |
| V-02 | C-28 back-reference stripped | Phrasing register | Phase 3 drops "already on record" + standalone framing; "confirm and extend" kept | ~190 |
| V-03 | C-29 field-level stripped | Lifecycle emphasis | C-29 rule removed from Falsification field description; kept only in integration rules list | 195 |
| V-04 | V-01 + V-02 combined | Combination | Inline C-27 AND stripped C-28 back-reference together | ~190 |
| V-05 | Full ceiling + anchor-update signal | Combination + v9 scout | R7 V-05 intact + explicit anchor-update propagation integration rule; ARTIFACT gains `anchor_updated_from_phase1` | 195 |

**Three isolation tests:**

1. **V-01**: Does the `PROHIBITED FORM:` block label matter for C-27, or is inline "does not pass" in the header sufficient? Expects 195 -- the phrase is load-bearing, not the block structure.

2. **V-02 control**: Is "already on record from Phase 1 SUB-STEP 2" load-bearing for C-28, or does "confirm and extend" alone pass? Expects ~190 -- the explicit back-reference is the mechanism that distinguishes confirmation from origination.

3. **V-03**: Does C-29 pass when its rule lives only in the integration rules list (not also in the Falsification field description)? Expects 195 -- any Phase 6 position satisfies the criterion.

**V-05 potential v9 signal:** When Phase 3 updates the preliminary anchor to a higher-confidence step, does Phase 6 carry the updated step or freeze at the Phase 1 anchor verbatim? The new integration rule closes this stale-anchor propagation gap and adds an `anchor_updated_from_phase1` frontmatter field to make the behavior observable in scorecards.
 while V-05 stays at 195, this confirms the back-reference is load-bearing for C-28 at the prompt level.

**Single-axis:** V-01 and V-03 test one mechanism each and expect to hold at 195. V-02 tests one mechanism and expects to drop (establishing the load-bearing element for C-28). V-04 combines V-01 + V-02. V-05 extends R7 V-05 with a new signal.

---

## V-01: C-27 inline prohibition (phrasing register axis)

**Axis:** Phrasing register -- Phase 1 PROHIBITED FORM block for SUB-STEP 2 is removed. The "does not pass" language is embedded inline within the SUB-STEP 2 header itself: "Preliminary falsification anchor (required here before Phase 2; proceeding without this anchor does not pass):" All other Phase 1 structure preserved -- SUB-STEP 1, SUB-STEP 2, required format, and the explanatory paragraph about incompleteness annotation. Phase 3 confirmation framing and Phase 6 integration rules preserved from R7 V-05.

**Hypothesis:** C-27 requires the prohibition for omitting the Phase 1 anchor to be "named at Phase 1 -- not deferred to Phase 3 or later." The R7 V-05 mechanism uses a distinct PROHIBITED FORM block with that label. This variation embeds the same "does not pass" language inline in the sub-step header -- a parenthetical at the production point. If C-27 requires the phrase "does not pass" at Phase 1 but not a labeled block, V-01 passes C-27. If the labeled PROHIBITED FORM structure is required, V-01 fails. The block heading is the variable being isolated.

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

  SUB-STEP 2 -- Preliminary falsification anchor (required here before Phase 2;
  proceeding to Phase 2 without producing this anchor does not pass):
  Name the highest-confidence step you can trace as a preliminary falsification anchor.
  Produce it here, before Phase 2 tracing begins. Phase 3 will confirm and extend it.
  Deferring this anchor to Phase 3 does not pass. Incompleteness changes the confidence
  annotation; it does not remove the requirement to name a step-level anchor here. Even
  one traceable step produces one falsifiable break point.

  Required format:
  "PRELIMINARY ANCHOR: The mechanism most likely fails if Step [N] -- [Name] -- does not
  occur, observable as [indicator]. Chain traceability ends here. Further falsification
  requires establishing [missing knowledge from SUB-STEP 1]."

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

## V-02: C-28 back-reference stripped (phrasing register axis)

**Axis:** Phrasing register -- Phase 3 CONDITIONAL BRANCH opening is simplified. R7 V-05 says: "If PATHWAY INCOMPLETE was declared in Phase 1, a PRELIMINARY ANCHOR is already on record from Phase 1 SUB-STEP 2. This branch confirms and extends it." V-02 replaces this with: "If PATHWAY INCOMPLETE was declared in Phase 1, confirm and extend the preliminary anchor from Phase 1." The back-reference phrase "is already on record from Phase 1 SUB-STEP 2" and the standalone framing sentence "This branch confirms and extends it." are both removed. "Confirm and extend" language is retained. All Phase 1 structure and Phase 6 integration rules preserved from R7 V-05.

**Hypothesis:** C-28 requires Phase 3 to "explicitly reference the Phase 1 anchor as prior record and frame its falsification work as confirmation and extension -- not as the first origination of the anchor." The "already on record" phrase is the explicit prior-record acknowledgment. This variation tests whether "confirm and extend" without that acknowledgment satisfies C-28's framing requirement, or whether the back-reference is the load-bearing element that distinguishes confirmation from origination. If V-02 fails C-28 but V-01 (which preserves Phase 3 exactly from R7 V-05) passes, the back-reference language is required.

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

If PATHWAY INCOMPLETE was declared in Phase 1, confirm and extend the preliminary anchor
from Phase 1. If Phase 2 tracing revealed additional labeled steps with higher confidence
than the Phase 1 preliminary anchor, update to the highest-confidence step now on record.

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

## V-03: C-29 field-level rule stripped (lifecycle emphasis axis)

**Axis:** Lifecycle emphasis -- Phase 6 Falsification field description removes the C-29 detection sentence. R7 V-05 places the C-29 rule in two positions within Phase 6: (a) inline in the Falsification field description: "a Falsification field that first names the anchor here without a corresponding Phase 1 PRELIMINARY ANCHOR does not pass C-26"; and (b) as a bullet in the integration rules list: "For incomplete pathways, the Falsification field must carry an anchor that was first produced in Phase 1 -- not first introduced here..." V-03 removes site (a) only; site (b) is preserved identically. All Phase 1 and Phase 3 structure preserved from R7 V-05.

**Hypothesis:** C-29 requires "the synthesis/AMEND phase includes an integration rule that explicitly detects the C-26 cross-phase violation." The integration rules list is explicitly part of Phase 6/AMEND. If the integration rules bullet alone satisfies C-29 (without the field-level annotation), V-03 passes C-29 at 195. If both sites are required or if the field-level annotation is independently load-bearing, V-03 drops. The isolation test establishes whether C-29 is satisfied by any Phase 6 site or requires the specific Falsification field-description placement.

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
    for incomplete pathways, this field carries the Phase 1 PRELIMINARY ANCHOR, updated
    for any additional steps traced in Phase 2}
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

## V-04: C-27 inline + C-28 back-reference stripped (combination)

**Axes:** V-01 phrasing register (Phase 1 inline prohibition) + V-02 phrasing register (Phase 3 back-reference stripped). Both C-27 and C-28 are tested at their minimal form simultaneously. C-29 in Phase 6 is preserved from R7 V-05 at both sites (Falsification field description and integration rules). Phase 1 uses the inline "does not pass" header from V-01; Phase 3 CONDITIONAL BRANCH uses the stripped "confirm and extend" from V-02 without "already on record."

**Hypothesis:** V-01 and V-02 test each minimization independently. V-04 combines them to verify whether the two minimal forms are independent (each passes or fails on its own) or whether interaction effects emerge. If V-01 passes C-27 (inline is sufficient) and V-02 fails C-28 (back-reference is required), V-04 scores: C-27 PASS, C-28 FAIL, C-29 PASS -> 190. If both minimal forms also pass their criteria, V-04 = 195 -- a simpler surface producing the same ceiling score. The combined variation is the stress test for the minimal form hypothesis.

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

  SUB-STEP 2 -- Preliminary falsification anchor (required here before Phase 2;
  proceeding to Phase 2 without producing this anchor does not pass):
  Name the highest-confidence step you can trace as a preliminary falsification anchor.
  Produce it here, before Phase 2 tracing begins. Phase 3 will confirm and extend it.
  Deferring this anchor to Phase 3 does not pass. Incompleteness changes the confidence
  annotation; it does not remove the requirement to name a step-level anchor here. Even
  one traceable step produces one falsifiable break point.

  Required format:
  "PRELIMINARY ANCHOR: The mechanism most likely fails if Step [N] -- [Name] -- does not
  occur, observable as [indicator]. Chain traceability ends here. Further falsification
  requires establishing [missing knowledge from SUB-STEP 1]."

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

If PATHWAY INCOMPLETE was declared in Phase 1, confirm and extend the preliminary anchor
from Phase 1. If Phase 2 tracing revealed additional labeled steps with higher confidence
than the Phase 1 preliminary anchor, update to the highest-confidence step now on record.

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

## V-05: Full ceiling + anchor-update propagation signal (combination + v9 scout)

**Axes:** All R7 V-05 enforcement sites preserved intact. One new integration rule added to Phase 6: anchor-update propagation -- when Phase 3 updated the preliminary anchor to a higher-confidence step, the Phase 6 Falsification field must carry the updated step, not the Phase 1 preliminary anchor verbatim. ARTIFACT gains a new frontmatter field `anchor_updated_from_phase1` to make this observable in scorecards.

**Hypothesis:** R7 V-05 achieves 195/195 under v8. V-05 adds one enforcement site not yet captured as a criterion: anchor-update propagation. Phase 3 already says "update to the highest-confidence step now on record" but this requirement is not enforced as an integration rule in Phase 6 and not named as a prohibited form. A model could pass C-26 (Phase 1 anchor present), C-27 (prohibition at Phase 1), C-28 (Phase 3 confirmation framing), and C-29 (synthesis integrity rule) while still carrying the Phase 1 preliminary anchor verbatim in Phase 6 when Phase 3 had updated to a higher-confidence step -- a silent stale-anchor propagation failure. V-05 closes this with an explicit named integration rule and the prohibited form. If a v9 rubric targets this, V-05 passes while V-01 through V-04 fail. The signal to watch in scorecards: does the Phase 6 Falsification field track Phase 3's update, or does it freeze at Phase 1?

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
  - For incomplete pathways where Phase 3 updated the preliminary anchor to a higher-
    confidence step, the Falsification field here must carry the updated step -- not the
    Phase 1 preliminary anchor verbatim. The field reflects the best anchor on record after
    all tracing, not the first anchor recorded. A response that carries the Phase 1
    preliminary anchor unchanged when Phase 3 identified and recorded a higher-confidence
    step does not pass -- Phase 3 updating the anchor is part of its confirmatory function;
    Phase 6 must reflect that update. If Phase 3 confirmed the Phase 1 anchor without
    updating (no higher-confidence step was found), Phase 6 carries the Phase 1 anchor as
    confirmed -- carrying the Phase 1 anchor verbatim is correct in that case and passes.
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
  anchor_updated_from_phase1: true | false | n/a
```

---

```json
{"r8_variations": 5, "new_criteria_targeted": ["C-27", "C-28", "C-29"], "base": "R7 V-05 (195/195 under v8 rubric -- ceiling)", "single_axis": ["V-01: C-27 phrasing register -- PROHIBITED FORM block -> inline header; 'does not pass' present but no block label", "V-02: C-28 phrasing register -- Phase 3 drops 'already on record' + 'This branch confirms and extends it'; 'confirm and extend' instruction kept", "V-03: C-29 lifecycle emphasis -- C-29 rule removed from Falsification field description; retained only in integration rules list"], "combined": ["V-04: V-01 + V-02 -- inline C-27 prohibition AND stripped C-28 back-reference combined", "V-05: Full R7 V-05 ceiling + anchor-update propagation integration rule (v9 scout)"], "isolation_tests": ["V-01: does the PROHIBITED FORM block label matter for C-27, or is inline 'does not pass' sufficient? Expected 195 if phrase is load-bearing, not the block structure.", "V-02 control: is 'already on record' load-bearing for C-28, or does 'confirm and extend' alone pass? Expected ~190 if back-reference is required.", "V-03: does C-29 pass when the rule is in integration rules only (not in Falsification field description)? Expected 195 if any Phase 6 position satisfies C-29.", "V-04 vs V-05: minimal C-27+C-28 combined vs. full ceiling + new signal. If V-02 fails C-28, V-04 also fails C-28 -- isolation test confirms independence."], "potential_v9_signal": "anchor-update propagation: when Phase 3 updates the preliminary anchor to a higher-confidence step, Phase 6 Falsification must carry the updated step, not the Phase 1 anchor verbatim. V-05 closes this with an integration rule and prohibited form; ARTIFACT adds 'anchor_updated_from_phase1' frontmatter field. Watch whether models carry stale Phase 1 anchors when Phase 3 identified better steps.", "expected_scores": {"V-01": "195 (C-27 PASS -- inline is sufficient)", "V-02": "~190 (C-28 FAIL -- back-reference is load-bearing)", "V-03": "195 (C-29 PASS -- integration rules position satisfies)", "V-04": "~190 (C-28 FAIL carries through combination)", "V-05": "195 (full ceiling; v9 signal graded if v9 rubric written)"}}
```
