Written to `simulations/quest/variations/discover-causal-variations-R10-2026-03-17.md`.

---

## R10 Variations Summary

**Base:** R9 V-05 (205/205 under v10)  
**New criterion targeted:** C-31 (Phase 3 CONDITIONAL BRANCH carries stale-anchor prohibited form)

| # | Label | Axis | Change from base | Expected |
|---|-------|------|-----------------|----------|
| V-01 | C-31 stripped -- positive instruction only | Phrasing register | ANCHOR-UPDATE PROHIBITED FORM replaced with positive ANCHOR-UPDATE INSTRUCTION; no "does not complete" language at Phase 3 | ~200 |
| V-02 | C-31 softened -- no "does not pass" language | Phrasing register | PROHIBITED FORM block present but rewritten as "necessary but not sufficient" -- no explicit failure mode phrase | ~200 |
| V-03 | C-31 deferred to Phase 6 (not co-located at Phase 3) | Lifecycle emphasis | Phase 3 has positive instruction only; self-referential rule moved to Phase 6 integration rules | ~200 |
| V-04 | C-31 forward-looking only -- names Phase 6 failure without self-referential form | Phrasing register (boundary) | Phase 3 PROHIBITED FORM names Phase 6 stale-anchor as "does not pass" but does NOT state "recording here does not close Phase 6" | ~200 |
| V-05 | Full ceiling + Phase 6 C-31 symmetry rule + ARTIFACT field | Combination + v11 scout | R9 V-05 intact + Phase 6 integration rule naming C-31 structural requirement + `phase3_anchor_update_prohibited_form: true\|false\|n/a` in ARTIFACT | 205 |

---

**Four isolation tests:**

1. **V-01** -- Is the Phase 3 PROHIBITED FORM independently required for C-31, or does the Phase 6 C-30 enforcement alone cover propagation?
2. **V-02** -- Does C-31 require explicit "does not complete" / "does not pass" language, or does "necessary but not sufficient" satisfy it? Parallel to the C-22/C-20 pattern.
3. **V-03** -- Does C-31 require co-location at Phase 3 specifically, or does an equivalent rule placed in Phase 6 integration rules satisfy it? Parallel to C-29 requiring the C-26 integrity check at Phase 6.
4. **V-04** -- Is the self-referential form ("recording here does not close Phase 6") the load-bearing phrase, distinct from a forward-looking form that names only the Phase 6 violation?

**V-05 v11 signals:** Phase 6 integration rule naming C-31's structural requirement (analogous to C-29 for C-26) + `phase3_anchor_update_prohibited_form` ARTIFACT field (analogous to `anchor_updated_from_phase1` for C-30).
 6 placement satisfies C-30 but not C-31 -- parallel to how C-29 requires the C-26 integrity rule at Phase 6, not wherever convenient.
4. **V-04** -- Does C-31 require the self-referential form ("recording here does not close Phase 6") specifically, or does a forward-looking form ("Phase 6 must carry the update; failing to do so does not pass") also satisfy C-31? Expected ~200: C-31 requires "recording the updated BEST-TRACEABLE ANCHOR here does not complete the propagation requirement" -- naming the Phase 6 failure from Phase 3 is necessary but the self-referential form ("here does not close") is the load-bearing phrase that closes the self-termination escape hatch.

**V-05 potential v11 signals:**

1. **Phase 6 C-31 symmetry rule**: C-30 requires an integration rule at Phase 6 naming the stale-anchor failure mode. By the same co-location logic (parallel to C-29 for C-26), a v11 criterion could require Phase 6 to also explicitly name the C-31 requirement -- that Phase 3's PROHIBITED FORM is required, and that a Phase 3 positive instruction only (without the prohibited form) does not pass C-31 even when Phase 6 carries the update correctly. V-05 adds this as a Phase 6 integration rule.

2. **ARTIFACT field**: C-30 required `anchor_updated_from_phase1: true | false | n/a` to make the anchor propagation status machine-readable. By symmetry, a v11 criterion could require `phase3_anchor_update_prohibited_form: true | false | n/a` to make the Phase 3 co-location compliance machine-readable. V-05 adds this field to Phase 7 ARTIFACT.

**Single-axis:** V-01 through V-04 each remove or reposition one C-31 component and expect to drop from 205 to ~200. V-05 extends R9 V-05 with two additional enforcement elements targeting a potential v11 ceiling.

---

## V-01: C-31 stripped -- positive instruction only (phrasing register axis)

**Axis:** Phrasing register -- the ANCHOR-UPDATE PROHIBITED FORM is removed from the Phase 3 CONDITIONAL BRANCH entirely. Replaced with an ANCHOR-UPDATE INSTRUCTION stating only the positive requirement: carry the updated step to Phase 6. No "does not complete the propagation requirement" language. No "does not pass" language for the Phase 3 update case. All C-30 structure in Phase 6 (integration rule naming stale-anchor failure mode, `anchor_updated_from_phase1` ARTIFACT field) preserved exactly from R9 V-05.

**Hypothesis:** C-31 requires the prohibited form co-located at Phase 3 -- explicitly naming that recording the update at Phase 3 does not close the Phase 6 propagation requirement. A positive instruction at Phase 3 ("carry to Phase 6") is the exact C-31 fail case per the rubric. V-01 is the cleanest isolation: all other criteria pass; C-31 alone fails because the PROHIBITED FORM at Phase 3 is absent. Expected ~200: C-30 intact (Phase 6 integration rule + ARTIFACT field present); C-31 FAIL (no Phase 3 prohibited form).

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

ANCHOR-UPDATE INSTRUCTION: When this branch updates the preliminary anchor to a
higher-confidence step, carry the updated BEST-TRACEABLE ANCHOR step to Phase 6
Falsification. Phase 6 must reflect the highest-confidence step on record after all
tracing -- not the Phase 1 preliminary anchor verbatim. If this branch confirms the Phase 1
anchor without updating (no higher-confidence step found), Phase 6 carries the Phase 1
anchor as confirmed -- carrying verbatim is correct and passes.

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

## V-02: C-31 softened -- no "does not pass" language (phrasing register axis)

**Axis:** Phrasing register -- the ANCHOR-UPDATE PROHIBITED FORM block is present at Phase 3 CONDITIONAL BRANCH but rewritten with softened language. The phrase "does not complete the propagation requirement" is replaced with "is necessary but not sufficient for the Phase 6 propagation requirement." No "does not pass" language appears in the Phase 3 anchor-update block. The C-24 PROHIBITED FORM (separate block) is preserved unchanged. All C-30 structure in Phase 6 (integration rule naming stale-anchor failure mode, `anchor_updated_from_phase1` ARTIFACT field) preserved from R9 V-05.

**Hypothesis:** C-31 pass condition requires "explicitly naming that correctly recording the anchor update at Phase 3 does not close the Phase 6 propagation requirement." The question is whether "necessary but not sufficient" framing satisfies this requirement, or whether explicit failure-mode language ("does not complete," "does not pass") is the load-bearing phrase. Parallel to the C-22/C-20 and C-24/C-18 patterns: positive rules and softened qualifications are not self-enforcing; the prohibited form must be named. If "necessary but not sufficient" does not constitute naming the failure mode, V-02 fails C-31 and drops to ~200. Expected ~200.

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

ANCHOR-UPDATE NOTE: When this branch updates the preliminary anchor to a higher-confidence
step, recording the updated BEST-TRACEABLE ANCHOR here is necessary but not sufficient for
the Phase 6 propagation requirement. Phase 6 Falsification must independently carry the
updated step -- the Phase 3 update record alone is insufficient to satisfy the Phase 6
Falsification field. Both sites must carry the updated anchor: this branch records it;
Phase 6 must also independently reference it. If this branch confirms the Phase 1 anchor
without updating (no higher-confidence step found), Phase 6 carries the Phase 1 anchor as
confirmed -- carrying verbatim is correct and passes.

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

## V-03: C-31 deferred to Phase 6 -- not co-located at Phase 3 (lifecycle emphasis axis)

**Axis:** Lifecycle emphasis -- the Phase 3 CONDITIONAL BRANCH carries only an ANCHOR-UPDATE INSTRUCTION (positive, same as V-01). The stale-anchor propagation rule naming that recording the Phase 3 update does not close the Phase 6 requirement is moved into the Phase 6 integration rules list as an additional bullet. The ANCHOR-UPDATE PROHIBITED FORM block is absent from Phase 3. All other C-30 structure preserved from R9 V-05 (`anchor_updated_from_phase1` ARTIFACT field present; Phase 6 stale-anchor integration rule from R9 V-05 preserved; new equivalent bullet added).

**Hypothesis:** C-31 is a co-location criterion: "When Phase 3 updates the preliminary Phase 1 anchor, the Phase 3 CONDITIONAL BRANCH must also carry a PROHIBITED FORM." The criterion explicitly requires the prohibited form at Phase 3 -- not at Phase 6. V-03 tests whether placing the equivalent rule in Phase 6 integration rules satisfies C-31. Expected ~200: C-31 requires Phase 3 co-location; Phase 6 placement (however accurate) does not satisfy the co-location requirement. Parallel to C-29 requiring the C-26 integrity rule at Phase 6 specifically -- placement elsewhere does not substitute.

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

ANCHOR-UPDATE INSTRUCTION: When this branch updates the preliminary anchor to a
higher-confidence step, carry the updated BEST-TRACEABLE ANCHOR step to Phase 6
Falsification. Phase 6 must reflect the highest-confidence step on record after all
tracing -- not the Phase 1 preliminary anchor verbatim. If this branch confirms the Phase 1
anchor without updating (no higher-confidence step found), Phase 6 carries the Phase 1
anchor as confirmed -- carrying verbatim is correct and passes.

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
  - For incomplete pathways where Phase 3 updated the preliminary anchor, correctly recording
    the update at Phase 3 does not close this Phase 6 propagation requirement. Phase 6
    Falsification must independently carry the updated step -- the Phase 3 update record
    does not substitute for Phase 6 Falsification reflecting the updated anchor. A response
    where Phase 3 records the anchor update and Phase 6 carries the Phase 1 preliminary
    anchor verbatim does not pass -- the stale-anchor propagation failure is a Phase 6
    failure regardless of how correctly Phase 3 performed the update.
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

## V-04: C-31 forward-looking only -- names Phase 6 failure without self-referential form (phrasing register axis)

**Axis:** Phrasing register boundary test -- the Phase 3 CONDITIONAL BRANCH carries an ANCHOR-UPDATE PROHIBITED FORM block, but the block is forward-looking rather than self-referential. It names that Phase 6 must carry the updated step and that a Phase 6 stale-anchor fails ("does not pass"). What it does NOT include is the self-referential form: "recording the updated BEST-TRACEABLE ANCHOR here does not complete the propagation requirement." It names the Phase 6 violation from Phase 3's vantage point but does not state that Phase 3's own record is insufficient to satisfy Phase 6. The block label reads ANCHOR-UPDATE PROHIBITED FORM and uses "does not pass" language -- the language refers to Phase 6's failure, not Phase 3's self-limitation.

**Hypothesis:** C-31 pass condition requires naming "that correctly recording the anchor update at Phase 3 does not close the Phase 6 propagation requirement." This is the self-referential form: Phase 3 must name that its own record is not the terminal requirement. V-04 names the Phase 6 failure mode (carrying the stale Phase 1 anchor in Phase 6 does not pass) without stating the self-limiting qualification (recording here does not close Phase 6). If the self-referential form ("recording here does not close Phase 6") is the load-bearing element of C-31 -- distinct from naming what Phase 6 must do -- V-04 fails C-31 and drops to ~200. Expected ~200.

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

ANCHOR-UPDATE PROHIBITED FORM: When this branch updates the preliminary anchor to a
higher-confidence step, Phase 6 Falsification must also carry the updated step. Carrying
the Phase 1 preliminary anchor verbatim in Phase 6 when this branch recorded a
higher-confidence step does not pass -- Phase 6 must reflect the Phase 3 update. Both
sites must carry the updated anchor: this branch records it; Phase 6 must carry it. If this
branch confirms the Phase 1 anchor without updating (no higher-confidence step found),
Phase 6 carries the Phase 1 anchor as confirmed -- carrying verbatim is correct and passes.

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

## V-05: Full ceiling + Phase 6 C-31 symmetry rule + ARTIFACT field (combination + v11 scout)

**Axes:** All R9 V-05 enforcement sites preserved intact (C-31 ANCHOR-UPDATE PROHIBITED FORM co-located at Phase 3 with self-referential form present). Two new elements added:

1. **Phase 6 integration rule naming C-31 symmetry:** An additional integration rule bullet explicitly states that a Phase 3 CONDITIONAL BRANCH carrying only a positive update instruction -- without a PROHIBITED FORM naming that the Phase 3 record does not close Phase 6 -- does not pass C-31. This creates a fourth enforcement site: Phase 1 (C-26/C-27), Phase 3 (C-31), Phase 6 stale-anchor rule (C-30), Phase 6 C-31 symmetry rule (v11 candidate). The Phase 6 rule mirrors C-29's role for C-26: just as C-29 requires Phase 6 to detect the first-appearance-at-synthesis violation of C-26, this rule requires Phase 6 to detect the Phase 3 positive-instruction-only violation of C-31.

2. **ARTIFACT field `phase3_anchor_update_prohibited_form`:** A new ARTIFACT frontmatter field making Phase 3 PROHIBITED FORM compliance machine-readable, parallel to `anchor_updated_from_phase1` for C-30. Value `n/a` when Phase 3 confirms verbatim (same N/A condition as C-31).

**Hypothesis:** R9 V-05 achieves 205/205 under v10. V-05 adds two enforcement elements not yet captured as criteria. A v11 rubric targeting either the Phase 6 C-31 symmetry rule or the `phase3_anchor_update_prohibited_form` ARTIFACT field would give V-05 a score above 205 while V-01 through V-04 do not include these elements. The signal to watch: does explicitly naming C-31's structural requirement in Phase 6 integration rules improve model reliability in producing the Phase 3 PROHIBITED FORM? Does the machine-readable ARTIFACT field create accountability for C-31 compliance analogous to how `anchor_updated_from_phase1` creates accountability for C-30 propagation?

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

ANCHOR-UPDATE PROHIBITED FORM: When this branch updates the preliminary anchor to a
higher-confidence step, recording the updated BEST-TRACEABLE ANCHOR here does not complete
the propagation requirement. Phase 6 Falsification must also carry the updated step --
correctly recording the update here does not close the Phase 6 propagation requirement.
Carrying the Phase 1 preliminary anchor verbatim in Phase 6 when this branch recorded a
higher-confidence step does not pass -- the stale-anchor propagation failure occurs at
Phase 6, not here. Both sites must reflect the updated anchor: this branch records it;
Phase 6 must carry it. If this branch confirms the Phase 1 anchor without updating (no
higher-confidence step found), Phase 6 carries the Phase 1 anchor as confirmed -- carrying
verbatim is correct and passes.

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
  - A Phase 3 CONDITIONAL BRANCH that carries only a positive update instruction -- "record
    the updated BEST-TRACEABLE ANCHOR and carry it to Phase 6" -- without a PROHIBITED FORM
    explicitly naming that recording the update at Phase 3 does not close this Phase 6
    propagation requirement does not pass C-31. The Phase 3 update record and the Phase 3
    PROHIBITED FORM are both required; a response that satisfies this Phase 6 stale-anchor
    rule (C-30 PASS) while leaving Phase 3 with a positive instruction only leaves the
    self-termination escape hatch open at Phase 3. A model reading the Phase 3 instruction
    "carry to Phase 6" may treat Phase 3 as the terminal requirement; the Phase 3 PROHIBITED
    FORM closes that escape hatch at the site where it would be taken -- this Phase 6 rule
    detects its absence at the synthesis point where all enforcement converges.
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
  phase3_anchor_update_prohibited_form: true | false | n/a
```

---

```json
{"r10_variations": 5, "new_criterion_targeted": "C-31", "base": "R9 V-05 (205/205 under v10 rubric -- ceiling)", "single_axis": ["V-01: phrasing register -- Phase 3 ANCHOR-UPDATE PROHIBITED FORM replaced with positive ANCHOR-UPDATE INSTRUCTION; no failure mode language at Phase 3 update point; C-30 structure (Phase 6 integration rule + ARTIFACT field) intact", "V-02: phrasing register -- ANCHOR-UPDATE NOTE block present at Phase 3 but uses softened language ('necessary but not sufficient'); no 'does not pass' or 'does not complete' phrase; C-30 structure intact", "V-03: lifecycle emphasis -- Phase 3 has positive ANCHOR-UPDATE INSTRUCTION only; stale-anchor self-referential rule ('recording here does not close Phase 6') moved to Phase 6 integration rules as additional bullet; C-30 structure intact plus new Phase 6 bullet", "V-04: phrasing register boundary -- Phase 3 carries ANCHOR-UPDATE PROHIBITED FORM block with 'does not pass' language for Phase 6 stale-anchor failure; does NOT include self-referential form ('recording here does not complete the propagation requirement'); names Phase 6 violation without naming Phase 3 self-limitation"], "combined": ["V-05: Full R9 V-05 ceiling (C-31 PROHIBITED FORM at Phase 3 intact with self-referential form) + Phase 6 C-31 symmetry integration rule (names that Phase 3 positive-instruction-only does not pass C-31) + ARTIFACT field phase3_anchor_update_prohibited_form: true | false | n/a (v11 scout)"], "isolation_tests": ["V-01: is the ANCHOR-UPDATE PROHIBITED FORM at Phase 3 independently required for C-31, or does the Phase 6 C-30 integration rule alone enforce propagation? Expected ~200 -- C-31 requires the prohibited form co-located at Phase 3; absent from Phase 3, C-31 fails regardless of Phase 6 completeness.", "V-02: does C-31 require explicit 'does not pass' / 'does not complete' failure-mode language, or does softened 'necessary but not sufficient' framing satisfy C-31? Expected ~200 -- parallel to C-22/C-20 and C-24/C-18: failure-mode naming is the load-bearing element; softened framing is the prohibited form that fails.", "V-03: does C-31 require the prohibited form at Phase 3 specifically (co-location), or does placing the equivalent rule in Phase 6 integration rules satisfy C-31? Expected ~200 -- C-31 is a co-location criterion requiring the prohibited form at the update point (Phase 3); Phase 6 placement satisfies C-30 not C-31.", "V-04: does C-31 require the self-referential form ('recording here does not close Phase 6') specifically, or does a forward-looking form ('Phase 6 must carry the update; failing to do so does not pass') also satisfy C-31? Expected ~200 -- naming the Phase 6 failure from Phase 3 is necessary but the self-referential form ('here does not close') is the load-bearing phrase that closes the self-termination escape hatch at the Phase 3 update site."], "potential_v11_signals": ["Phase 6 C-31 symmetry rule: analogous to C-29 (Phase 6 must detect C-26 first-appearance-at-synthesis violation), a v11 criterion could require Phase 6 to also detect Phase 3 positive-instruction-only (C-31 violation). V-05 adds this as a Phase 6 integration rule. Watch whether explicit Phase 6 naming of the C-31 structural requirement changes model reliability.", "ARTIFACT field phase3_anchor_update_prohibited_form: analogous to anchor_updated_from_phase1 for C-30, a v11 criterion could require machine-readable tracking of C-31 compliance at Phase 3. V-05 adds this field. n/a when Phase 3 confirms verbatim (same N/A condition as C-31/C-30)."], "expected_scores": {"V-01": "~200 (C-31 FAIL -- Phase 3 has positive instruction only, no PROHIBITED FORM at update point)", "V-02": "~200 (C-31 FAIL if 'does not pass'/'does not complete' language is required; 205 if 'necessary but not sufficient' satisfies -- expected FAIL parallel to C-22 pattern)", "V-03": "~200 (C-31 FAIL -- Phase 6 placement of the self-referential rule does not satisfy the Phase 3 co-location requirement)", "V-04": "~200 (C-31 FAIL if self-referential form 'recording here does not close Phase 6' is the load-bearing element; 205 if forward-looking 'Phase 6 must carry' with 'does not pass' satisfies -- expected FAIL: C-31 rubric specifically requires naming that the Phase 3 update record is insufficient)", "V-05": "205 (full ceiling; v11 signal graded if v11 rubric targets Phase 6 C-31 symmetry rule or phase3_anchor_update_prohibited_form ARTIFACT field)"}}
```
