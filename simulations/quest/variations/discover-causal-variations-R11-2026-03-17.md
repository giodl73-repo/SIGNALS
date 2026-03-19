Written to `simulations/quest/variations/discover-causal-variations-R11-2026-03-17.md`.

---

## R11 Variations Summary

**Base:** R10 V-05 (215/215 under v11)
**New criteria targeted:** C-32 and C-33

| # | Label | Axis | Single change | Expected |
|---|-------|------|---------------|----------|
| V-01 | C-32 stripped | Lifecycle emphasis | Phase 6 C-32 integration rule removed; C-31 + C-33 intact | ~210 |
| V-02 | C-32 softened | Phrasing register | Phase 6 names C-31 requirement positively -- no "does not pass" for Phase 3-only case | ~210 |
| V-03 | C-33 stripped | Lifecycle emphasis | `phase3_anchor_update_prohibited_form` removed from ARTIFACT; C-31 + C-32 intact | ~210 |
| V-04 | C-33 body-placement | Lifecycle emphasis | Field moved from frontmatter to artifact prose body; `anchor_updated_from_phase1` stays in frontmatter | ~210 |
| V-05 | Full ceiling + v12 scout | Combination | R10 V-05 intact + `phase1_anchor_prohibition_stated: true \| false \| n/a` added to ARTIFACT | 215 |

**Four isolation questions:**
1. **V-01** -- Is C-32 independently required, or do C-29 + C-30 stale-anchor rule together cover C-31 enforcement at Phase 6?
2. **V-02** -- Does C-32 require explicit "does not pass" for the Phase 3-positive-instruction-only case (by the C-22/C-24/C-27 precedent), or does a positive structural description suffice?
3. **V-03** -- Is the ARTIFACT field independently required for C-33, or does narrative enforcement (C-31 + C-32) substitute?
4. **V-04** -- Does C-33 require frontmatter placement specifically, or does a prose body note satisfy the machine-readability requirement?

**V-05 v12 signal:** `phase1_anchor_prohibition_stated` completes the ARTIFACT audit table -- `preliminary_anchor_declared` (C-26), `phase1_anchor_prohibition_stated` (C-27), `anchor_updated_from_phase1` (C-30), `phase3_anchor_update_prohibited_form` (C-33) -- one field per enforcement chain criterion, four positions covered.
-positive-instruction-only case, or does naming the C-31 structural requirement positively ("the Phase 3 PROHIBITED FORM is required alongside the update record") satisfy C-32? Parallel to C-22/C-20, C-24/C-18, C-27/C-26 patterns: positive rules without failure-mode naming are not self-enforcing.
3. **V-03** -- Is the `phase3_anchor_update_prohibited_form` ARTIFACT field independently required for C-33, or does the combination of the Phase 3 PROHIBITED FORM (C-31) and the Phase 6 C-32 integration rule provide sufficient machine-readable tracking without the ARTIFACT field?
4. **V-04** -- Does C-33 require the `phase3_anchor_update_prohibited_form` field specifically in the YAML frontmatter, or does including it as a named note in the artifact prose body satisfy the criterion? Parallel to C-30's ARTIFACT field requirement: "frontmatter" is the specified location; body placement is the omission variant.

**V-05 v12 signals:** `phase1_anchor_prohibition_stated: true | false | n/a` added to ARTIFACT frontmatter. Currently ARTIFACT tracks `preliminary_anchor_declared: true | false` (C-26 compliance -- was the Phase 1 anchor produced?) but has no machine-readable field for C-27 compliance (was "does not pass" language present at Phase 1 for the preliminary anchor requirement?). By the same symmetry that led C-33 to add `phase3_anchor_update_prohibited_form` alongside `anchor_updated_from_phase1`, a v12 criterion could add `phase1_anchor_prohibition_stated` alongside `preliminary_anchor_declared`. The complete ARTIFACT audit table would then cover all four enforcement chain positions:

| ARTIFACT field | Tracks | Criterion |
|----------------|--------|-----------|
| `preliminary_anchor_declared` | Phase 1 anchor co-location | C-26 |
| `phase1_anchor_prohibition_stated` | Phase 1 prohibition phrase | C-27 (v12 candidate) |
| `anchor_updated_from_phase1` | Phase 6 anchor provenance | C-30 |
| `phase3_anchor_update_prohibited_form` | Phase 3 prohibited form | C-33 |

**Single-axis:** V-01 through V-04 each remove or reposition one C-32 or C-33 component and expect to drop from 215 to ~210. V-05 extends R10 V-05 with one additional ARTIFACT field targeting a potential v12 ceiling.

---

## V-01: C-32 stripped -- Phase 6 C-31 naming rule absent (lifecycle emphasis axis)

**Axis:** Lifecycle emphasis -- the Phase 6 integration rule that explicitly names the C-31 structural requirement is removed entirely. The Phase 3 ANCHOR-UPDATE PROHIBITED FORM (C-31) remains exactly as in R10 V-05: self-referential form present, "does not complete the propagation requirement" and "does not close the Phase 6 propagation requirement" language both intact. The C-30 stale-anchor integration rule at Phase 6 is preserved. The C-29 C-26 integrity rule embedded in the Falsification field description is preserved. The `phase3_anchor_update_prohibited_form: true | false | n/a` ARTIFACT field is preserved (C-33 PASS). No other changes.

**Hypothesis:** C-32 requires a Phase 6 integration rule explicitly naming the C-31 structural requirement -- that the Phase 3 CONDITIONAL BRANCH must carry a PROHIBITED FORM (not merely a positive update instruction) for the propagation enforcement to be complete. V-01 tests whether C-29 (Phase 6 detects C-26 first-appearance-at-synthesis violation) and the C-30 stale-anchor integration rule together satisfy C-32, or whether C-32 is independently required. Expected ~210: C-32 requires Phase 6 to name the C-31 structural requirement specifically; the C-29 and C-30 rules address different failure modes; silence on C-31 at Phase 6 leaves the Phase 3 co-location requirement unnamed at the synthesis convergence point. C-31 PASS + C-33 PASS; C-32 FAIL.

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

## V-02: C-32 softened -- names C-31 requirement without failure-mode phrase (phrasing register axis)

**Axis:** Phrasing register -- the Phase 6 C-32 integration rule is present but rewritten in positive-only language. The rule names the C-31 structural requirement (Phase 3 CONDITIONAL BRANCH must carry a PROHIBITED FORM alongside the update record) but does not include explicit "does not pass" language for the Phase 3-positive-instruction-only case. No "does not pass" or "does not close" phrase appears in the C-32 rule. The Phase 3 ANCHOR-UPDATE PROHIBITED FORM (C-31) is preserved intact from R10 V-05. The C-30 stale-anchor integration rule is preserved. The `phase3_anchor_update_prohibited_form: true | false | n/a` ARTIFACT field is preserved (C-33 PASS). No other changes.

**Hypothesis:** C-32 pass condition requires "an integration rule explicitly naming the C-31 structural requirement." The question is whether naming the requirement positively ("the Phase 3 CONDITIONAL BRANCH must carry both the update record and the PROHIBITED FORM -- a positive instruction satisfies the update requirement but not the co-located enforcement requirement") satisfies C-32, or whether explicit failure-mode language ("a Phase 3 CONDITIONAL BRANCH with only a positive instruction does not pass C-31") is the load-bearing element. Parallel to C-22/C-20, C-24/C-18, and C-27/C-26: each of those criteria established that positive rules are not self-enforcing -- the prohibited form must be named as a failure mode. Expected ~210: C-32 by the same pattern requires the explicit failure-mode phrase for the Phase 3-positive-instruction-only case; a positive description of what must be present does not close the escape hatch at the synthesis point.

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
  - The Phase 3 CONDITIONAL BRANCH must carry both the BEST-TRACEABLE ANCHOR update and
    a PROHIBITED FORM naming that recording the update at Phase 3 is not sufficient to
    close the Phase 6 propagation requirement. A Phase 3 CONDITIONAL BRANCH that carries
    the positive update instruction satisfies the recording requirement; the additional
    PROHIBITED FORM is the mechanism that closes the self-termination escape hatch. When
    Phase 3 carries only the positive instruction, the stale-anchor propagation failure at
    Phase 6 remains unnamed at its production point. Both elements are required for complete
    dual-site enforcement: Phase 3 records the update; Phase 3 also names that the record
    alone is insufficient; Phase 6 independently carries the updated step and names the
    stale-anchor failure mode. A positive Phase 3 instruction satisfies the recording
    requirement but not the co-located enforcement requirement.
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

## V-03: C-33 stripped -- phase3_anchor_update_prohibited_form absent from ARTIFACT (lifecycle emphasis axis)

**Axis:** Lifecycle emphasis -- `phase3_anchor_update_prohibited_form: true | false | n/a` is removed from the ARTIFACT frontmatter entirely. The `anchor_updated_from_phase1: true | false | n/a` field is preserved (C-30 PASS). The Phase 3 ANCHOR-UPDATE PROHIBITED FORM (C-31) is preserved intact. The Phase 6 C-32 integration rule is preserved intact. No other changes.

**Hypothesis:** C-33 requires the `phase3_anchor_update_prohibited_form: true | false | n/a` field as an independent requirement -- the combination of C-31 (PROHIBITED FORM at Phase 3) and C-32 (Phase 6 names the C-31 requirement) does not substitute for machine-readable ARTIFACT tracking of Phase 3 co-location compliance. V-03 tests whether the ARTIFACT field is independently required or whether the narrative enforcement at Phase 3 and Phase 6 together satisfy C-33 without machine-readable tracking. Expected ~210: C-33 requires the ARTIFACT field specifically; human-readable enforcement at Phase 3 and Phase 6 does not provide the machine-readable audit that C-33 captures. Parallel to C-30's `anchor_updated_from_phase1` requirement: C-30 requires the integration rule AND the ARTIFACT field; neither alone satisfies both requirements. C-31 PASS + C-32 PASS; C-33 FAIL.

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
```

---

## V-04: C-33 body-placement -- field moved from ARTIFACT frontmatter to artifact prose (lifecycle emphasis axis)

**Axis:** Lifecycle emphasis -- `phase3_anchor_update_prohibited_form` is removed from the ARTIFACT YAML frontmatter and instead instructed to appear as a named note in the artifact prose body. The `anchor_updated_from_phase1: true | false | n/a` field remains in frontmatter (C-30 PASS). The Phase 3 ANCHOR-UPDATE PROHIBITED FORM (C-31) and the Phase 6 C-32 integration rule are preserved intact. No other changes.

**Hypothesis:** C-33 specifies "The ARTIFACT frontmatter includes a `phase3_anchor_update_prohibited_form: true | false | n/a` field." The word "frontmatter" is the location specification -- not merely "the artifact contains." V-04 tests whether body placement (a named note in the artifact prose) satisfies C-33, or whether frontmatter placement is specifically required for machine-readability. The design rationale for C-33 explicitly parallels C-30's `anchor_updated_from_phase1` ARTIFACT field requirement -- and C-30's requirement is frontmatter-specific ("make the propagation status machine-readable"). Machine-readability depends on frontmatter structure; prose body notes are not machine-parseable in the same way. Expected ~210: C-33 requires frontmatter placement specifically; body placement fails the machine-readability requirement that motivates the criterion. C-31 PASS + C-32 PASS; C-33 FAIL.

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

In the artifact body, include a Phase 3 compliance note:
  phase3_anchor_update_prohibited_form: [true | false | n/a] -- true if the Phase 3
  CONDITIONAL BRANCH carried the self-referential ANCHOR-UPDATE PROHIBITED FORM; false
  if Phase 3 carried only a positive update instruction; n/a if Phase 3 confirmed the
  Phase 1 anchor verbatim without updating to a higher-confidence step.
```

---

## V-05: Full ceiling + Phase 1 prohibition ARTIFACT field (combination + v12 scout)

**Axes:** All R10 V-05 enforcement sites preserved intact (C-31 ANCHOR-UPDATE PROHIBITED FORM at Phase 3 with self-referential form; C-32 Phase 6 integration rule naming C-31 structural requirement; C-33 `phase3_anchor_update_prohibited_form: true | false | n/a` in ARTIFACT). One new element added:

**Phase 1 prohibition ARTIFACT field:** `phase1_anchor_prohibition_stated: true | false | n/a` added to ARTIFACT frontmatter. This field tracks C-27 compliance -- whether "does not pass" language was present at Phase 1 for the preliminary anchor requirement. Currently ARTIFACT has `preliminary_anchor_declared: true | false` (tracking C-26: was the anchor produced at Phase 1?) but no field for C-27 (was the prohibition phrase present at Phase 1?). The new field completes the ARTIFACT audit for the Phase 1 enforcement chain: `preliminary_anchor_declared` tracks C-26 compliance; `phase1_anchor_prohibition_stated` tracks C-27 compliance.

Value semantics: `true` when Phase 1 SUB-STEP 2 carries "does not pass" language for the case of proceeding to Phase 2 without producing the preliminary anchor (C-27 pass condition met); `false` when Phase 1 produces the preliminary anchor (C-26 pass) but no "does not pass" phrase appears at Phase 1 (C-27 fail case); `n/a` when PATHWAY INCOMPLETE was not declared in Phase 1 -- no preliminary anchor is required, so C-27 has no referent (same N/A condition as C-26 and C-27).

**Hypothesis:** R10 V-05 achieves 215/215 under v11. V-05 adds one ARTIFACT field not yet captured as a criterion. A v12 rubric targeting `phase1_anchor_prohibition_stated` would give V-05 a score above 215 while V-01 through V-04 do not include this field. The signal to watch: does the ARTIFACT audit of Phase 1 prohibition status (C-27 compliance) create the same machine-readable accountability for the Phase 1 enforcement chain that C-33 creates for the Phase 3 enforcement chain? The symmetry is exact: C-33 pairs with C-31 (Phase 3 prohibited form) as `anchor_updated_from_phase1` pairs with `preliminary_anchor_declared`. A v12 criterion requiring `phase1_anchor_prohibition_stated` would complete the ARTIFACT-layer audit of the full enforcement chain.

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
  phase1_anchor_prohibition_stated: true | false | n/a
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
{"r11_variations": 5, "new_criteria_targeted": ["C-32", "C-33"], "base": "R10 V-05 (215/215 under v11 rubric -- ceiling)", "single_axis": ["V-01: lifecycle emphasis -- Phase 6 C-32 integration rule removed; Phase 3 C-31 PROHIBITED FORM intact; C-33 ARTIFACT field intact; C-29 and C-30 stale-anchor rule preserved unchanged", "V-02: phrasing register -- Phase 6 C-32 integration rule replaced with positive-only description; names C-31 structural requirement without 'does not pass' failure-mode phrase for Phase 3-positive-instruction-only case; C-31 and C-33 intact", "V-03: lifecycle emphasis -- phase3_anchor_update_prohibited_form ARTIFACT field removed; anchor_updated_from_phase1 field intact; C-31 and C-32 intact", "V-04: lifecycle emphasis -- phase3_anchor_update_prohibited_form moved from ARTIFACT frontmatter to artifact body prose note; anchor_updated_from_phase1 stays in frontmatter; C-31 and C-32 intact"], "combined": ["V-05: Full R10 V-05 ceiling (C-31/C-32/C-33 all intact) + phase1_anchor_prohibition_stated: true | false | n/a added to ARTIFACT (tracks C-27 compliance; n/a when Phase 1 incompleteness not declared; v12 scout)"], "isolation_tests": ["V-01: is the Phase 6 C-32 integration rule independently required for C-32, or do C-29 (Phase 6 names C-26 first-appearance-at-synthesis rule) and the C-30 stale-anchor integration rule together cover C-31 enforcement at the synthesis point? Expected ~210: C-32 is a distinct criterion requiring Phase 6 to name the C-31 structural requirement specifically; C-29 addresses C-26 violation; C-30 stale-anchor rule addresses Phase 6 propagation failure; neither names the C-31 Phase 3 co-location requirement.", "V-02: does C-32 require explicit 'does not pass' failure-mode language for the Phase 3-positive-instruction-only case, or does naming the C-31 structural requirement positively ('a positive Phase 3 instruction satisfies the recording requirement but not the co-located enforcement requirement') satisfy C-32? Expected ~210: by the C-22/C-20, C-24/C-18, and C-27/C-26 precedent, positive rules are not self-enforcing -- the failure-mode phrase is the load-bearing element; describing what must be present without naming its absence as a fail leaves the escape hatch open.", "V-03: is the phase3_anchor_update_prohibited_form ARTIFACT field independently required for C-33, or does the narrative enforcement chain (C-31 PROHIBITED FORM at Phase 3 + C-32 integration rule at Phase 6) substitute for machine-readable ARTIFACT tracking? Expected ~210: C-33 is an independent criterion requiring the ARTIFACT field; narrative enforcement at Phase 3 and Phase 6 addresses the prohibited form behavior; ARTIFACT tracking is a separate machine-readability requirement, parallel to how C-30 requires both the integration rule AND anchor_updated_from_phase1.", "V-04: does C-33 require the phase3_anchor_update_prohibited_form field specifically in the ARTIFACT frontmatter, or does including it as a named prose note in the artifact body satisfy C-33? Expected ~210: C-33 specifies 'ARTIFACT frontmatter includes' -- frontmatter placement is the specified location; body placement fails the machine-readability purpose motivating the criterion, parallel to how C-30's anchor_updated_from_phase1 requires frontmatter not body prose."], "potential_v12_signals": ["phase1_anchor_prohibition_stated: true | false | n/a -- tracks C-27 compliance at ARTIFACT level; n/a when Phase 1 incompleteness not declared; pairs with preliminary_anchor_declared (C-26 tracking) as phase3_anchor_update_prohibited_form pairs with anchor_updated_from_phase1; completes the ARTIFACT audit table: preliminary_anchor_declared (C-26), phase1_anchor_prohibition_stated (C-27), anchor_updated_from_phase1 (C-30), phase3_anchor_update_prohibited_form (C-33)."], "expected_scores": {"V-01": "~210 (C-32 FAIL -- Phase 6 has no integration rule naming the C-31 structural requirement; C-31 PASS + C-33 PASS)", "V-02": "~210 (C-32 FAIL if 'does not pass' failure-mode language is required; 215 if positive structural description satisfies -- expected FAIL by C-22/C-24/C-27 precedent; positive statement without failure-mode phrase does not close the escape hatch)", "V-03": "~210 (C-33 FAIL -- ARTIFACT field absent; C-31 PASS + C-32 PASS)", "V-04": "~210 (C-33 FAIL -- field in artifact body not frontmatter; C-31 PASS + C-32 PASS; machine-readability requires frontmatter placement)", "V-05": "215 (full ceiling under v11; v12 signal graded if v12 rubric targets phase1_anchor_prohibition_stated ARTIFACT field)"}}
```
