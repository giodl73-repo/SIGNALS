Golden document written to `simulations/quest/golden/discover-causal-golden-2026-03-17.md`.

**What was produced:**

- **Frontmatter:** `rubric_final: v14` (corrected from the v13 typo in the instructions -- v14 is the final rubric that produced the 230/230 score)
- **Prompt body:** Simplified V-05 with all 20 excision sites applied (3,226 → ~2,203 words). Every criterion-tested phrase preserved verbatim including both C-35 and C-36 two-element requirements at Phase 6
- **What made it golden:** 5 patterns -- symmetric ARTIFACT audit chain, Phase 6 naming chain closed, dual-site enforcement, unconditional requirements enforced by named prohibited forms, evidence gap orthogonality demonstrated not asserted
- **Rubric summary:** All 36 criteria with scoring bands and gradeability cascade
se 6 synthesis-point naming chain, fully closed**
Every ARTIFACT field has a corresponding Phase 6 integration rule naming the field-absence
failure mode and E-02 gradeability distinction:
- C-29 names C-26 cross-phase integrity rule
- C-32 names C-31 Phase 3 co-location requirement
- C-35 names C-34 `phase1_anchor_prohibition_stated` structural requirement
- C-36 names C-33 `phase3_anchor_update_prohibited_form` structural requirement
Each rule names both elements: (1) field absence fails the criterion independently of the
behavioral fail; (2) `false` vs absent is the E-02 gradeability distinction. No partial
naming (V-01/V-02), wrong-location placement (V-03), or paraphrase (V-04) passes.

**3. Dual-site enforcement at every escape hatch**
Each enforcement chain operates at two sites: the production point (where the model acts)
and the synthesis point (Phase 6, where all chains converge). C-26/C-27 pair at Phase 1.
C-30/C-31 pair across Phase 3 and Phase 6. C-33/C-36 and C-34/C-35 complete the ARTIFACT
audit loop. A response that satisfies the production site but omits the synthesis-site
naming fails the corresponding Phase 6 criterion.

**4. Unconditional requirements enforced by named prohibited forms**
Every unconditional rule is closed by naming the conditional escape hatch explicitly.
Phase 0 inertia incorporation: "Not competing -- no adjustment needed" is named as the
form that fails. Phase 1 anchor: deferral to Phase 3 is named as the form that fails.
Phase 3 deferral form for C-18 (C-24). Phase 6 stale-anchor rule for C-30 (C-31).
Positive-rule-only framing does not pass; the prohibited conditional form must be named.

**5. Evidence gap and evidence tier orthogonality demonstrated, not asserted**
The null-gap counterexample (`gap: none, tier: T1`) is required to prove the fields are
independent -- asserting they are separate without instantiating the null-gap state leaves
the category error open. The AMEND structure carries both fields as separate named entries
with propagation from Phase 4 enforced by an explicit integration rule.

---

## Golden Prompt Body

```
You are running /discover-causal for topic: {topic}.

Hypothesis under review: {hypothesis}
(Claim: X causes Y. Test whether the mechanism is sound and whether the cause is the
right one.)

=== PHASE 0: INERTIA GATE ===

Answer this before any mechanism work: does the status quo already produce Y?

Assess whether existing behaviors, market forces, platform trends, or workarounds
independently trend toward outcome Y -- without any new feature.

INERTIA VERDICT: [Competing / Not competing / Unclear]
Basis: [one sentence -- specific observation about the current state of the domain, not
assertion]

If Competing: the mechanism analysis in Phase 2 must explain what X produces that the
status quo does not.

PROHIBITED FORM: Conditioning inertia incorporation on the verdict being Competing or
Unclear does not pass. All three verdict values -- Competing, Not competing, and Unclear --
must explicitly shape the amended claim in Phase 6. "Not competing -- no adjustment needed"
is the conditional form that fails.

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
  declaration point, before Phase 2.

=== PHASE 2: MECHANISM PATHWAY ===

Trace the causal pathway from X to Y.

STEP LABELING REQUIREMENT: Each step must carry a persistent formal label:
  Step N -- [Name]: What changes. Who acts. Observable indicator.

The same label must appear identically in the pathway, in falsification, and in evidence
gap sections.

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
higher-confidence step does not pass.

PROHIBITED FORM (C-24): Declaring incompleteness and deferring or omitting step-level
falsification does not pass.

-- END CONDITIONAL BRANCH --

Do not state falsification as a metric threshold.

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

NULL-GAP COUNTEREXAMPLE: The following is a valid, required output state:
  Evidence gap steps: none
  Aggregate evidence tier: T1

PROPAGATION REQUIREMENT: The Evidence gap steps field does not stay in Phase 4. It must
also appear as a standalone named entry in Phase 6 AMEND, separately from the Aggregate
evidence tier field.

Do not substitute general research for team-specific evidence.

=== PHASE 5: CONFOUNDER CHECK ===

This phase asks a DIFFERENT question from Phase 0.

Phase 0 asked: does the status quo trend toward Y over time, without intervention?
This phase asks: what else, operating RIGHT NOW alongside X, could independently produce Y?

The inertia case (Phase 0) is EXCLUDED from this analysis.

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
    clause text does not satisfy this field; the completeness status must appear here as a
    named entry separate from the amended clause; write "complete" if Phase 1 found no
    gaps; write "incomplete at Step N" if PATHWAY INCOMPLETE was declared; write "partial"
    if some steps are [UNCERTAIN]}
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
    Phase 6 must reflect that update.
  - A Phase 3 CONDITIONAL BRANCH that carries only a positive update instruction -- "record
    the updated BEST-TRACEABLE ANCHOR and carry it to Phase 6" -- without a PROHIBITED FORM
    explicitly naming that recording the update at Phase 3 does not close this Phase 6
    propagation requirement does not pass C-31.
  - Absence of `phase1_anchor_prohibition_stated` from the ARTIFACT frontmatter does not
    pass C-34 -- the Phase 1 prohibition status must be machine-readable regardless of
    whether C-27 passes or fails. When C-27 passes (Phase 1 carries "does not pass"
    language for the missing-anchor case), the correct field value is `true`. When C-27
    fails (no prohibition phrase at Phase 1), the correct field value is `false` -- not
    absent; absence of the field fails C-34 separately from the C-27 fail. The field is
    `n/a` only when PATHWAY INCOMPLETE was not declared in Phase 1 -- same N/A condition
    as C-26, C-27, and C-34.
  - Absence of `phase3_anchor_update_prohibited_form` from the ARTIFACT frontmatter does
    not pass C-33 -- the Phase 3 co-location status must be machine-readable regardless of
    whether C-31 passes or fails. When C-31 passes (Phase 3 CONDITIONAL BRANCH carries the
    self-referential prohibited form), the correct field value is `true`. When C-31 fails
    (no prohibited form at Phase 3 CONDITIONAL BRANCH), the correct field value is `false`
    -- not absent; absence of the field fails C-33 separately from the C-31 fail. The
    field is `n/a` only when PATHWAY INCOMPLETE was not declared in Phase 1 -- same N/A
    condition as all fields in the incomplete-pathway enforcement chain.
  - Evidence gap appearing only in Phase 4 (CONTEXT EVIDENCE) does not satisfy the Evidence
    gap AMEND field -- the gap must propagate from Phase 4 to Phase 6 as a standalone named
    entry; leaving it in Phase 4 does not pass.
  - A narrowed claim that ignores mechanism incompleteness does not pass.
  - A narrowed claim that omits the confounder finding (when one was identified) does not
    pass.
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

## Final Rubric Criteria Summary (v14)

**Scoring:** 230 pts total | Golden >= 225 | Acceptable 210-224 | Passing 195-209

| Tier | IDs | Pts | Weight |
|------|-----|-----|--------|
| Essential | C-01 through C-05 | 60 | 12 pts each |
| Recommended | C-06 through C-08 | 30 | 10 pts each |
| Aspirational | C-09 through C-36 | 140 | 5 pts each |

### Essential (60 pts)

| ID | Criterion | Pass Condition |
|----|-----------|----------------|
| C-01 | Mechanism traced as pathway | Causal pathway traced as sequence of observable intermediate steps -- not a summary claim or single leap |
| C-02 | Falsification is mechanism break | Names specific mechanism break point ("mechanism fails if [step] does not occur") -- not metric threshold or outcome negation |
| C-03 | Inertia check performed | Checks whether Y occurs without X; explicit "not competing" verdict passes; silence does not |
| C-04 | Causal claim narrowed in AMEND | AMEND produces a narrowed causal claim; restating or broadening does not pass |
| C-05 | Context evidence assessed | Evaluates whether mechanism-holds evidence exists in the team's specific context; silence does not pass |

### Recommended (30 pts)

| ID | Criterion | Pass Condition |
|----|-----------|----------------|
| C-06 | Mechanism pathway is testable | Pathway is specific enough to design an observation or test to confirm or deny |
| C-07 | At least one confounder identified | Names at least one plausible alternative explanation for Y that does not involve X |
| C-08 | AMEND output is actionable | Narrowed claim includes bounded scope or mechanism qualifier; generic narrowings do not pass |

### Aspirational (140 pts)

| ID | Criterion | Category |
|----|-----------|----------|
| C-09 | Evidence quality rated | depth |
| C-10 | Multiple causal pathways considered | depth |
| C-11 | Mechanism incompleteness acknowledged | honesty |
| C-12 | Falsification break anchored to named step | precision |
| C-13 | Evidence gap localized to pathway steps | precision |
| C-14 | AMEND conditioned on inertia finding | integration |
| C-15 | AMEND synthesizes all phase outputs | integration |
| C-16 | Pathway steps formally labeled | precision |
| C-17 | Confounder explicitly distinguished from inertia | coverage |
| C-18 | Incomplete pathway still anchors falsification | honesty |
| C-19 | AMEND evidence gap and evidence tier are separate fields | integration |
| C-20 | AMEND inertia incorporation is unconditional | integration |
| C-21 | Evidence gap orthogonality proven by null-gap counterexample | precision |
| C-22 | Inertia conditional form excluded by explicit prohibition | integration |
| C-23 | Mechanism completeness is a named AMEND field | integration |
| C-24 | Falsification deferral form excluded by explicit prohibition | precision |
| C-25 | Evidence gap is a standalone named AMEND field | integration |
| C-26 | Falsification anchor co-located with incompleteness declaration | honesty |
| C-27 | C-26 prohibition co-located with Phase 1 anchor requirement | honesty |
| C-28 | Phase 3 frames anchor as confirmation of Phase 1 preliminary anchor | honesty |
| C-29 | C-26 cross-phase integrity rule named at synthesis | honesty |
| C-30 | Phase 6 Falsification tracks Phase 3 anchor update | integration |
| C-31 | Phase 3 CONDITIONAL BRANCH carries stale-anchor prohibited form | honesty |
| C-32 | C-31 structural requirement named at Phase 6 synthesis | integration |
| C-33 | Phase 3 prohibited-form status tracked as ARTIFACT field | integration |
| C-34 | Phase 1 prohibition status tracked as ARTIFACT field | integration |
| C-35 | C-34 structural requirement named at Phase 6 synthesis | integration |
| C-36 | C-33 structural requirement named at Phase 6 synthesis | integration |

**C-36 closes the symmetric ARTIFACT audit chain:** C-34/C-35 cover
`phase1_anchor_prohibition_stated`; C-33/C-36 cover
`phase3_anchor_update_prohibited_form`. Every enforcement-chain ARTIFACT field now has a
corresponding Phase 6 naming criterion with the same two-element structure: (1) field
absence independently fails the criterion; (2) `false` vs absent is the E-02 gradeability
distinction.

**Gradeability cascade (incomplete-pathway chain):**
C-11 -> C-12 -> C-18 -> C-24 -> C-26 -> C-27/C-28/C-29 -> C-30 -> C-31/C-33 ->
C-32/C-34 -> C-35/C-36. Each criterion is N/A or unscored when its upstream prerequisite
fails or does not trigger.
