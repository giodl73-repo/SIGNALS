Written to `simulations/quest/variations/discover-causal-variations-R12-2026-03-17.md`.

---

**R12 Variations Summary**

| # | Label | Axis | Change | Expected |
|---|-------|------|--------|----------|
| V-01 | C-34 stripped | Lifecycle emphasis | `phase1_anchor_prohibition_stated` removed from ARTIFACT; C-27 intact | ~215 |
| V-02 | C-34 body-placement | Lifecycle emphasis | Field moved to artifact prose body; C-27 intact | ~215 |
| V-03 | C-27 stripped + C-34 false | Phrasing register | Phase 1 PROHIBITED FORM removed; field `false` in ARTIFACT (E-02 state b) | ~215 |
| V-04 | C-27 stripped + C-34 absent | Phrasing register | Phase 1 PROHIBITED FORM removed; field absent (E-02 state c) | ~210 |
| V-05 | Full ceiling + v13 scout | Combination | R11 V-05 intact + Phase 6 rule naming C-34 requirement (C-35 candidate) | 220 |

**New in R12:** V-03 and V-04 test the E-02 gradeability rule in a way no prior round has -- they strip C-27 and vary only the ARTIFACT field state (`false` vs absent), isolating whether the `false` value itself is the load-bearing element that gives C-34 PASS under behavioral failure. V-03 vs V-04 is the comparison that proves or disproves E-02 state (b) vs state (c).

**V-05 v13 signal:** C-35 -- Phase 6 integration rule naming the C-34 ARTIFACT field requirement with E-02 value semantics. Closes the synthesis-point naming gap for C-34, parallel to how C-29 closed it for C-26 and C-32 closed it for C-31.
ct body satisfy the machine-readability requirement? Parallel to R11 V-04 which tested C-33 body-placement.
3. **V-03** -- When C-27 fails (no prohibition phrase at Phase 1), does field `false` in ARTIFACT give C-34 PASS? Tests E-02 state (b): behavioral fail, correct audit.
4. **V-04** -- When C-27 fails (no prohibition phrase at Phase 1), does field absent fail C-34 separately from the C-27 fail? Tests E-02 state (c): behavioral fail, missing audit.

**V-05 v13 signal:** Phase 6 integration rule explicitly naming the C-34 structural requirement -- that absence of `phase1_anchor_prohibition_stated` from ARTIFACT frontmatter fails C-34 separately from the C-27 fail, and that when C-27 fails the correct field value is `false` not absent. This would be C-35: the synthesis-point naming of C-34, parallel to C-29 (Phase 6 names C-26) and C-32 (Phase 6 names C-31).

**Scores under v12:**

| Variation | Change | C-27 | C-34 | v12 score | Tier |
|-----------|--------|------|------|-----------|------|
| V-01 (C-34 stripped) | Field removed from ARTIFACT | PASS | FAIL | **215** | Golden |
| V-02 (C-34 body-placement) | Field in prose body not frontmatter | PASS | FAIL | **215** | Golden |
| V-03 (C-27 stripped + field false) | No Phase 1 prohibition; field `false` | FAIL | PASS | **215** | Golden |
| V-04 (C-27 stripped + field absent) | No Phase 1 prohibition; field absent | FAIL | FAIL | **210** | Golden (floor) |
| V-05 (full ceiling + v13 scout) | Phase 6 C-35 candidate rule added | PASS | PASS | **220** | Golden (ceiling) |

---

## V-01: C-34 stripped -- phase1_anchor_prohibition_stated absent from ARTIFACT (lifecycle emphasis axis)

**Axis:** Lifecycle emphasis -- `phase1_anchor_prohibition_stated: true | false | n/a` is removed from the ARTIFACT frontmatter entirely. The Phase 1 PROHIBITED FORM (C-27) is preserved intact. The `anchor_updated_from_phase1: true | false | n/a` and `phase3_anchor_update_prohibited_form: true | false | n/a` fields are preserved (C-30 PASS, C-33 PASS). No other changes.

**Hypothesis:** C-34 requires the `phase1_anchor_prohibition_stated` field as an independent requirement -- C-27 compliance does not make the ARTIFACT field redundant. V-01 tests whether machine-readable ARTIFACT tracking of Phase 1 prohibition status is independently required. Expected ~215: C-34 requires the field specifically; human-readable enforcement at Phase 1 does not substitute. Parallel to C-33: C-31 PASS (Phase 3 has the prohibited form) does not make the C-33 ARTIFACT field redundant. C-27 PASS + C-34 FAIL.

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

## V-02: C-34 body-placement -- phase1_anchor_prohibition_stated in artifact prose body (lifecycle emphasis axis)

**Axis:** Lifecycle emphasis -- `phase1_anchor_prohibition_stated` is removed from the ARTIFACT YAML frontmatter and instead instructed to appear as a named compliance note in the artifact prose body. The `preliminary_anchor_declared: true | false`, `anchor_updated_from_phase1: true | false | n/a`, and `phase3_anchor_update_prohibited_form: true | false | n/a` fields remain in frontmatter. The Phase 1 PROHIBITED FORM (C-27) is preserved intact. No other changes.

**Hypothesis:** C-34 specifies "The ARTIFACT frontmatter includes a `phase1_anchor_prohibition_stated: true | false | n/a` field." Frontmatter is the location specification. V-02 tests whether prose body placement satisfies C-34 or whether frontmatter is specifically required. Parallel to R11 V-04 (C-33 body-placement): same structure, same expected result. Expected ~215: C-34 requires frontmatter placement; body placement fails machine-readability. C-27 PASS + C-34 FAIL.

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

In the artifact body, include a Phase 1 prohibition compliance note:
  phase1_anchor_prohibition_stated: [true | false | n/a] -- true if Phase 1 SUB-STEP 2
  carries "does not pass" language for the case of proceeding to Phase 2 without producing
  the preliminary anchor; false if Phase 1 produces the anchor requirement without the
  prohibition phrase; n/a if PATHWAY INCOMPLETE was not declared in Phase 1.
```

---

## V-03: C-27 stripped + C-34 field false -- E-02 state (b) behavioral fail correct audit (phrasing register axis)

**Axis:** Phrasing register -- the Phase 1 PROHIBITED FORM for omitting the preliminary anchor is removed entirely. Phase 1 SUB-STEP 2 retains the required format and instruction to produce the anchor, but carries no "does not pass" language. The `phase1_anchor_prohibition_stated: true | false | n/a` ARTIFACT field is preserved in frontmatter with explicit value semantics instructing `false` when the prohibition phrase was absent. All other elements of R11 V-05 are preserved intact.

**Hypothesis:** C-34's E-02 gradeability rule: when C-27 fails (prohibition phrase absent), field `false` gives C-34 PASS; field absent fails C-34 separately. V-03 tests E-02 state (b): C-27 FAIL + field `false` = C-34 PASS. Expected ~215: C-27 FAIL = -5 pts; C-34 PASS = 0 pts lost; net 215. Confirms C-34 is a distinct criterion from C-27 -- it can pass when C-27 fails, provided the field is present with `false`.

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
    [true when Phase 1 SUB-STEP 2 carried "does not pass" language; false when Phase 1
    produced the anchor requirement without a prohibition phrase -- the prohibition phrase
    is absent in this prompt so record false when the incomplete path was taken; n/a when
    PATHWAY INCOMPLETE was not declared in Phase 1]
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

## V-04: C-27 stripped + C-34 absent -- E-02 state (c) behavioral fail missing audit (phrasing register axis)

**Axis:** Phrasing register -- the Phase 1 PROHIBITED FORM for omitting the preliminary anchor is removed entirely (identical to V-03). The `phase1_anchor_prohibition_stated` field is also removed from the ARTIFACT frontmatter entirely. The `anchor_updated_from_phase1: true | false | n/a` and `phase3_anchor_update_prohibited_form: true | false | n/a` fields are preserved. All other elements of R11 V-05 are preserved intact.

**Hypothesis:** C-34's E-02 gradeability rule: when C-27 fails, field absent fails C-34 separately from the C-27 fail. V-04 tests E-02 state (c): C-27 FAIL + field absent = C-34 FAIL independently. Expected ~210: C-27 FAIL = -5 pts; C-34 FAIL = -5 pts; two independent failure modes. V-03 vs V-04 comparison isolates whether `false` vs absent is the load-bearing distinction for C-34 gradeability under E-02.

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

## V-05: Full ceiling + Phase 6 C-35 candidate rule (combination + v13 scout)

**Axes:** All R11 V-05 enforcement sites preserved intact (C-27 PROHIBITED FORM at Phase 1; C-31 ANCHOR-UPDATE PROHIBITED FORM at Phase 3; C-32 Phase 6 integration rule naming C-31 structural requirement; C-33 `phase3_anchor_update_prohibited_form` in ARTIFACT; C-34 `phase1_anchor_prohibition_stated` in ARTIFACT). One new element added:

**Phase 6 C-35 candidate integration rule:** A new integration rule explicitly naming the C-34 structural requirement -- that absence of `phase1_anchor_prohibition_stated` from the ARTIFACT frontmatter fails C-34 separately from the C-27 fail, and that when C-27 fails the correct field value is `false` not absent. Parallel to C-29 (Phase 6 names C-26 cross-phase integrity rule) and C-32 (Phase 6 names C-31 structural requirement).

**Hypothesis:** V-05 achieves 220/220 under v12. A v13 rubric targeting this Phase 6 rule would give V-05 a score above 220 while V-01 through V-04 do not include this rule. C-35 would close the synthesis-point gap: Phase 6 names the C-34 ARTIFACT field requirement with E-02 value semantics, making the three-state distinction (true / false / absent) explicit at the convergence point.

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
  - Absence of `phase1_anchor_prohibition_stated` from the ARTIFACT frontmatter does not
    pass C-34 -- the Phase 1 prohibition status must be machine-readable regardless of
    whether C-27 passes or fails. When C-27 passes (Phase 1 carries "does not pass"
    language for the missing-anchor case), the correct field value is `true`. When C-27
    fails (no prohibition phrase at Phase 1), the correct field value is `false` -- not
    absent; absence of the field fails C-34 separately from the C-27 fail. A response that
    carries the ARTIFACT field with `false` when C-27 fails satisfies C-34 (behavioral
    failure, correct audit); a response that omits the field when C-27 fails fails C-34
    separately (behavioral failure, missing audit). The field is `n/a` only when PATHWAY
    INCOMPLETE was not declared in Phase 1 -- same N/A condition as C-26, C-27, and C-34.
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
{"r12_variations": 5, "new_criterion_targeted": "C-34", "base": "R11 V-05 (220/220 under v12 -- ceiling)", "single_axis": ["V-01: lifecycle emphasis -- phase1_anchor_prohibition_stated field removed from ARTIFACT frontmatter; Phase 1 PROHIBITED FORM (C-27) intact; anchor_updated_from_phase1 and phase3_anchor_update_prohibited_form fields intact", "V-02: lifecycle emphasis -- phase1_anchor_prohibition_stated moved from ARTIFACT frontmatter to artifact prose body note; Phase 1 PROHIBITED FORM (C-27) intact; anchor_updated_from_phase1 stays in frontmatter", "V-03: phrasing register -- Phase 1 PROHIBITED FORM removed (C-27 FAIL); phase1_anchor_prohibition_stated: true | false | n/a field preserved in ARTIFACT frontmatter with explicit false-value semantics for C-27-fail case (E-02 state b -- C-34 PASS)", "V-04: phrasing register -- Phase 1 PROHIBITED FORM removed (C-27 FAIL); phase1_anchor_prohibition_stated field absent from ARTIFACT entirely (E-02 state c -- C-34 FAIL)"], "combined": ["V-05: Full R11 V-05 ceiling (C-27/C-31/C-32/C-33/C-34 all intact) + Phase 6 integration rule explicitly naming C-34 structural requirement and E-02 value semantics (C-35 candidate)"], "isolation_tests": ["V-01: Is the phase1_anchor_prohibition_stated ARTIFACT field independently required, or does C-27 PASS make the field redundant? Expected ~215: C-27 PASS + C-34 FAIL.", "V-02: Does C-34 require frontmatter placement specifically, or does prose body satisfy machine-readability? Expected ~215: C-27 PASS + C-34 FAIL.", "V-03: E-02 state (b) -- C-27 FAIL + field false = C-34 PASS? Expected ~215: C-27 FAIL -5 pts; C-34 PASS.", "V-04: E-02 state (c) -- C-27 FAIL + field absent = C-34 FAIL separately? Expected ~210: C-27 FAIL -5 pts + C-34 FAIL -5 pts."], "potential_v13_signals": ["C-35: Phase 6 integration rule naming C-34 structural requirement -- that absence of phase1_anchor_prohibition_stated from ARTIFACT frontmatter fails C-34 separately from C-27 fail, and that false vs absent is the gradeability distinction under E-02. Parallel to C-29 (Phase 6 names C-26) and C-32 (Phase 6 names C-31)."], "expected_scores": {"V-01": "~215 (C-27 PASS + C-34 FAIL -- field independently required)", "V-02": "~215 (C-27 PASS + C-34 FAIL -- frontmatter placement specifically required)", "V-03": "~215 (C-27 FAIL -5 + C-34 PASS -- E-02 state b: behavioral fail, correct audit)", "V-04": "~210 (C-27 FAIL -5 + C-34 FAIL -5 -- E-02 state c: behavioral fail, missing audit)", "V-05": "220 under v12 (ceiling unchanged; v13 signal graded if v13 rubric targets Phase 6 C-35 candidate rule)"}}
```
