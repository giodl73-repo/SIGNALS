## discover-causal R6 Scorecard

**v6 rubric: 175 pts max | Golden >= 165**

| Variation | Total | Tier | C-24 | C-25 |
|-----------|-------|------|------|------|
| V-01 | 170 | Golden | PASS (dual-site Ph3+6) | FAIL |
| V-02 | 170 | Golden | FAIL | PASS (dual-site Ph4+6) |
| V-03 | 170 | Golden | PASS (co-located Ph1+3) | FAIL |
| V-04 | **175** | Golden | PASS (single-site Ph3) | PASS (single-site Ph4) |
| V-05 | **175** | Golden | PASS (dual-site Ph3+6) | PASS (dual-site Ph4+6) |

All variants Golden. C-24 and C-25 are the only differentiators.

**Key findings:**

- **V-04 = V-05 at 175**: Single-site placement satisfies C-24 and C-25 -- dual-site adds operational redundancy but doesn't raise the score. The criteria require "explicitly name the prohibited form," not "name it twice."

- **V-03 exposes an alternative C-24 path**: Co-locating "deferring or omitting this preliminary anchor does not pass" at the Phase 1 incompleteness declaration achieves C-24 without a Phase 3 PROHIBITED FORM block. The load-bearing element is naming the prohibited form, not where it appears.

- **Perfect orthogonality**: V-01 passes C-24, fails C-25. V-02 fails C-24, passes C-25. V-03 passes C-24 (via co-location), fails C-25. Zero interaction effects -- each criterion is independently diagnosable.

```json
{"top_score": 175, "all_essential_pass": true, "new_patterns": ["single-site prohibition placement at the analytical production point satisfies C-24 and C-25 rubric criteria -- dual-site adds operational redundancy but does not raise the score", "co-locating the does-not-pass language at the incompleteness declaration point in Phase 1 achieves C-24 without a Phase 3 PROHIBITED FORM block -- the prohibited form is named at the moment incompleteness is produced", "C-24 and C-25 are fully orthogonal -- single-axis isolations confirm zero interaction effects and each can be diagnosed and fixed independently"]}
```
on; restating and broadening prohibited. |
| C-05 | Context evidence assessed | PASS | 12 | Phase 4 CONTEXT EVIDENCE: per-step T1/T2/T3 audit; FIELD INDEPENDENCE NOTE; "do not substitute general research for team-specific evidence." |
| C-06 | Mechanism pathway is testable | PASS | 10 | Named agent + observable indicator per step; STEP LABELING REQUIREMENT makes steps observable and referenceable. |
| C-07 | Confounder or alternative cause | PASS | 10 | Phase 5 CONFOUNDER CHECK: explicitly requires alternative cause (a) not involving X and (b) not the inertia case; explicit exclusion acknowledgment required. |
| C-08 | AMEND output is actionable | PASS | 10 | Amended clause requires mechanism qualifier + scope condition + inertia qualifier per verdict form. |
| C-09 | Evidence quality rated | PASS | 5 | T1/T2/T3 scale with definitions; Aggregate evidence tier as separate AMEND field. |
| C-10 | Multiple causal pathways considered | PASS | 5 | Phase 2: "is there more than one plausible causal pathway? If yes: trace primary, name secondary in one sentence. Note whether complementary, competing, or nested." Active pathway named in AMEND. |
| C-11 | Mechanism incompleteness acknowledged | PASS | 5 | Phase 1: "If no: declare incompleteness now. Write: PATHWAY INCOMPLETE: mechanism cannot be traced past [step]." Producing thin steps to clear this gate fails. |
| C-12 | Falsification break anchored to named step | PASS | 5 | Required format includes "Step [N] -- [Name]"; "step number and name must match a labeled row in Phase 2 exactly." BEST-TRACEABLE ANCHOR format for incomplete pathways also requires named step. |
| C-13 | Evidence gap localized to pathway steps | PASS | 5 | FIELD INDEPENDENCE NOTE: "Evidence gap steps: [list Step N -- [Name] labels with no supporting evidence; write 'none' if every step has evidence]" -- per-step accounting required as named output. |
| C-14 | AMEND conditioned on inertia finding | PASS | 5 | Amended clause: three-case required incorporation per verdict value (Competing / Not competing / Unclear); "no verdict makes inertia incorporation optional." |
| C-15 | AMEND synthesizes all phase outputs | PASS | 5 | Phase 6 required structure: Inertia verdict, Mechanism completeness, Evidence tier, Evidence gap, Confounder finding, Active pathway, Falsification -- all named fields; "Omitting any of them does not pass." |
| C-16 | Pathway steps formally labeled | PASS | 5 | STEP LABELING REQUIREMENT: "Step N -- [Name]:" format required; "same label must appear identically in the pathway, in falsification, and in evidence gap sections." Unlabeled steps make falsification anchoring fail mechanically. |
| C-17 | Confounder explicitly distinguished from inertia | PASS | 5 | Phase 5: "The inertia case (Phase 0) is EXCLUDED from this analysis. It does not count as a confounder." Explicit acknowledgment required: "The inertia case (Phase 0 verdict: [verdict]) is not included here." |
| C-18 | Incomplete pathway still anchors falsification | PASS | 5 | CONDITIONAL BRANCH: prohibits deferral and metric threshold; BEST-TRACEABLE ANCHOR required format. PROHIBITED FORM block structural requirement: "The incompleteness declaration removes the completeness requirement from the anchor format; it does not remove the requirement to name an anchor." |
| C-19 | AMEND evidence gap and evidence tier are separate fields | PASS | 5 | FIELD INDEPENDENCE NOTE: orthogonality statement + two separate AMEND fields. NULL-GAP COUNTEREXAMPLE: "Evidence gap steps: none / Aggregate evidence tier: T1" as valid required output state. |
| C-20 | AMEND inertia incorporation is unconditional | PASS | 5 | Phase 0 PROHIBITED FORM: "Conditioning inertia incorporation on the verdict being Competing or Unclear does not pass... 'Not competing -- no adjustment needed' is the conditional form that fails." |
| C-21 | Evidence gap orthogonality proven by null-gap counterexample | PASS | 5 | NULL-GAP COUNTEREXAMPLE block in Phase 4: instantiates "Evidence gap steps: none / Aggregate evidence tier: T1"; names category error ("conflating 'no missing steps' with 'no tier to report'"); "Both are always required. Both always carry a value, even when gap is none." |
| C-22 | Inertia conditional form excluded by explicit prohibition | PASS | 5 | Phase 0 PROHIBITED FORM names conditional form: "'Not competing -- no adjustment needed' is the conditional form that fails." Phase 6 integration rules repeat prohibition. Dual-site. |
| C-23 | Mechanism completeness is a named AMEND field | PASS | 5 | Standalone "Mechanism completeness:" field in AMEND with explicit note: "this is a standalone named field; a mechanism qualifier embedded within the Amended clause text does not satisfy this field." |
| C-24 | Falsification deferral form excluded by explicit prohibition | PASS | 5 | Design purpose. Phase 3 PROHIBITED FORM: "Declaring incompleteness and deferring or omitting step-level falsification does not pass. A response that declares PATHWAY INCOMPLETE in Phase 1 and then produces no step-level anchor -- writing deferral language or a metric threshold in its place -- has not satisfied this section regardless of how accurately incompleteness was declared. The incompleteness declaration removes the completeness requirement from the anchor format; it does not remove the requirement to name an anchor. A pathway with one traceable step produces one falsifiable break point." Phase 6 integration rules: "Declaring incompleteness and deferring or omitting step-level falsification does not pass -- incompleteness changes the confidence annotation, not the structural requirement to name a step-level anchor; a PATHWAY INCOMPLETE response still carries a Falsification: field with a BEST-TRACEABLE ANCHOR value, not a deferral statement." Dual-site following C-22 pattern. |
| C-25 | Evidence gap is a standalone named AMEND field | FAIL | 0 | No PROPAGATION REQUIREMENT in Phase 4. No integration rule in Phase 6 naming the escape hatch "evidence gap appears only in Phase 4 and is absent from AMEND." Evidence gap field IS present in the AMEND structure (satisfying C-19) but the prohibition of the Phase-4-only form is absent. C-25 gap intentionally preserved for single-axis isolation. |
| **Total** | | | **170 / 175** | All essential: PASS. Golden. C-25 gap isolated. |

---

## V-02: Evidence gap propagation requirement

*Base: R5 V-05. Change: Phase 4 FIELD INDEPENDENCE NOTE gains PROPAGATION REQUIREMENT block; Phase 6 integration rules gain the C-25 prohibition. C-24 gap (no named prohibition of deferral form) intentionally preserved.*

| ID | Criterion | Verdict | Pts | Evidence Note |
|----|-----------|---------|-----|---------------|
| C-01 | Mechanism traced as pathway | PASS | 12 | MECHANISM READINESS + STEP LABELING REQUIREMENT throughout. Inherited from R5 V-05. |
| C-02 | Falsification is mechanism break | PASS | 12 | Required format with labeled step reference; metric threshold prohibited. |
| C-03 | Inertia check performed | PASS | 12 | Phase 0 INERTIA GATE with three-value verdict. |
| C-04 | Causal claim narrowed in AMEND | PASS | 12 | AMEND narrowing requirement; restating and broadening prohibited. |
| C-05 | Context evidence assessed | PASS | 12 | Per-step T1/T2/T3 audit; team-specific evidence requirement. |
| C-06 | Mechanism pathway is testable | PASS | 10 | Named agent + observable indicator per step. |
| C-07 | Confounder or alternative cause | PASS | 10 | Phase 5 CONFOUNDER CHECK with explicit inertia exclusion. |
| C-08 | AMEND output is actionable | PASS | 10 | Mechanism qualifier + scope condition + inertia qualifier per verdict form. |
| C-09 | Evidence quality rated | PASS | 5 | T1/T2/T3 scale; Aggregate evidence tier as AMEND field. |
| C-10 | Multiple causal pathways considered | PASS | 5 | Phase 2 secondary pathway requirement; Active pathway in AMEND. |
| C-11 | Mechanism incompleteness acknowledged | PASS | 5 | Phase 1 PATHWAY INCOMPLETE format with thin-steps failure condition. |
| C-12 | Falsification break anchored to named step | PASS | 5 | Required format; labeled row matching required. BEST-TRACEABLE ANCHOR for incomplete pathways. |
| C-13 | Evidence gap localized to pathway steps | PASS | 5 | FIELD INDEPENDENCE NOTE: Evidence gap steps as named output with per-step accounting. |
| C-14 | AMEND conditioned on inertia finding | PASS | 5 | Three-case mandatory incorporation in Amended clause. |
| C-15 | AMEND synthesizes all phase outputs | PASS | 5 | All named fields present; "Omitting any of them does not pass." |
| C-16 | Pathway steps formally labeled | PASS | 5 | "Step N -- [Name]:" format required with cross-phase label consistency. |
| C-17 | Confounder explicitly distinguished from inertia | PASS | 5 | Phase 5 explicit exclusion with required acknowledgment sentence. |
| C-18 | Incomplete pathway still anchors falsification | PASS | 5 | CONDITIONAL BRANCH: prohibits specific deferral phrases and metric threshold; BEST-TRACEABLE ANCHOR required. Structural enforcement satisfies C-18 (named prohibition is C-24's bar, not C-18's). |
| C-19 | AMEND evidence gap and evidence tier are separate fields | PASS | 5 | FIELD INDEPENDENCE NOTE + NULL-GAP COUNTEREXAMPLE; two separate AMEND fields. |
| C-20 | AMEND inertia incorporation is unconditional | PASS | 5 | Phase 0 PROHIBITED FORM names conditional form. Integration rules repeat. |
| C-21 | Evidence gap orthogonality proven by null-gap counterexample | PASS | 5 | NULL-GAP COUNTEREXAMPLE block; "Both are always required. Both always carry a value, even when gap is none." |
| C-22 | Inertia conditional form excluded by explicit prohibition | PASS | 5 | Phase 0 PROHIBITED FORM + Phase 6 integration rules -- dual-site. |
| C-23 | Mechanism completeness is a named AMEND field | PASS | 5 | Standalone Mechanism completeness field in AMEND. |
| C-24 | Falsification deferral form excluded by explicit prohibition | FAIL | 0 | Phase 3 CONDITIONAL BRANCH prohibits specific deferral phrases and requires BEST-TRACEABLE ANCHOR format -- structural prevention without naming the deferral form as a failure mode. No PROHIBITED FORM block. No Phase 6 integration rule. C-24 gap intentionally preserved for single-axis isolation. |
| C-25 | Evidence gap is a standalone named AMEND field | PASS | 5 | Design purpose. Phase 4 PROPAGATION REQUIREMENT: "The Evidence gap steps field does not stay in Phase 4. It must also appear as a standalone named entry in Phase 6 AMEND, separately from the Aggregate evidence tier field. Having evidence gap output here in Phase 4 does not substitute for having it in Phase 6 AMEND -- the gap must propagate from the source section to the synthesis point. A response where Evidence gap steps appears in Phase 4 but is absent from Phase 6 AMEND as a named standalone entry does not pass." Phase 6 integration rules: "Evidence gap appearing only in Phase 4 (CONTEXT EVIDENCE) does not satisfy the Evidence gap AMEND field -- the gap must propagate from Phase 4 to Phase 6 as a standalone named entry; leaving it in Phase 4 does not pass. Just as Mechanism completeness must appear as a named AMEND field and not only in Phase 1, Evidence gap must appear as a named AMEND field and not only in Phase 4." Dual-site, with explicit C-23 parallel drawn. |
| **Total** | | | **170 / 175** | All essential: PASS. Golden. C-24 gap isolated. |

---

## V-03: Incompleteness-anchored falsification (co-located)

*Base: R5 V-05. Change: Phase 1 restructured into MECHANISM READINESS + PRELIMINARY ANCHOR; PATHWAY INCOMPLETE must be immediately followed by PRELIMINARY ANCHOR in Phase 1 before further tracing; "does not pass" language at incompleteness production point; Phase 3 CONDITIONAL BRANCH becomes confirmation-and-extension step. C-25 gap (no evidence gap propagation rule) intentionally preserved.*

| ID | Criterion | Verdict | Pts | Evidence Note |
|----|-----------|---------|-----|---------------|
| C-01 | Mechanism traced as pathway | PASS | 12 | MECHANISM READINESS gate + STEP LABELING REQUIREMENT in Phase 2. |
| C-02 | Falsification is mechanism break | PASS | 12 | Required format in Phase 3; BEST-TRACEABLE ANCHOR extends/confirms Phase 1 PRELIMINARY ANCHOR. |
| C-03 | Inertia check performed | PASS | 12 | Phase 0 INERTIA GATE with PROHIBITED FORM and three-value verdict. |
| C-04 | Causal claim narrowed in AMEND | PASS | 12 | AMEND narrowing requirement; restating and broadening prohibited. |
| C-05 | Context evidence assessed | PASS | 12 | Per-step T1/T2/T3 audit; team-specific evidence. |
| C-06 | Mechanism pathway is testable | PASS | 10 | Named agent + observable indicator per step. |
| C-07 | Confounder or alternative cause | PASS | 10 | Phase 5 CONFOUNDER CHECK with explicit inertia exclusion. |
| C-08 | AMEND output is actionable | PASS | 10 | Mechanism qualifier + scope condition + inertia qualifier; Falsification field in AMEND confirms Phase 1 PRELIMINARY ANCHOR updated for Phase 2 steps. |
| C-09 | Evidence quality rated | PASS | 5 | T1/T2/T3 scale; Aggregate evidence tier as AMEND field. |
| C-10 | Multiple causal pathways considered | PASS | 5 | Phase 2 secondary pathway requirement; Active pathway in AMEND. |
| C-11 | Mechanism incompleteness acknowledged | PASS | 5 | Phase 1 SUB-STEP 1: PATHWAY INCOMPLETE format. "Producing three thin or vague steps to clear the readiness gate -- instead of declaring incompleteness -- fails this phase." |
| C-12 | Falsification break anchored to named step | PASS | 5 | PRELIMINARY ANCHOR format in Phase 1: "PRELIMINARY ANCHOR: The mechanism most likely fails if Step [N] -- [Name] -- does not occur, observable as [indicator]." Phase 3 confirms with labeled step. |
| C-13 | Evidence gap localized to pathway steps | PASS | 5 | FIELD INDEPENDENCE NOTE: Evidence gap steps as named output with per-step accounting. |
| C-14 | AMEND conditioned on inertia finding | PASS | 5 | Three-case mandatory incorporation in Amended clause. |
| C-15 | AMEND synthesizes all phase outputs | PASS | 5 | All named fields present; Falsification field explicitly updated for incomplete pathways. |
| C-16 | Pathway steps formally labeled | PASS | 5 | "Step N -- [Name]:" format required in STEP LABELING REQUIREMENT and PRELIMINARY ANCHOR format. |
| C-17 | Confounder explicitly distinguished from inertia | PASS | 5 | Phase 5 explicit exclusion with required acknowledgment. |
| C-18 | Incomplete pathway still anchors falsification | PASS | 5 | Co-location mechanism: Phase 1 SUB-STEP 2 requires PRELIMINARY ANCHOR immediately after PATHWAY INCOMPLETE declaration; Phase 3 confirms and extends. "Declaring incompleteness and deferring or omitting this preliminary anchor does not pass." |
| C-19 | AMEND evidence gap and evidence tier are separate fields | PASS | 5 | FIELD INDEPENDENCE NOTE + NULL-GAP COUNTEREXAMPLE; two separate AMEND fields. |
| C-20 | AMEND inertia incorporation is unconditional | PASS | 5 | Phase 0 PROHIBITED FORM: "'Not competing -- no adjustment needed' is the conditional form that fails." |
| C-21 | Evidence gap orthogonality proven by null-gap counterexample | PASS | 5 | NULL-GAP COUNTEREXAMPLE block; "Both fields are always required. Both always carry a value, even when gap is none." |
| C-22 | Inertia conditional form excluded by explicit prohibition | PASS | 5 | Phase 0 PROHIBITED FORM + integration rules -- dual-site. |
| C-23 | Mechanism completeness is a named AMEND field | PASS | 5 | Standalone Mechanism completeness field; embedding in clause text prohibited. |
| C-24 | Falsification deferral form excluded by explicit prohibition | PASS | 5 | Co-location mechanism. Phase 1 SUB-STEP 2: "Declaring incompleteness and deferring or omitting this preliminary anchor does not pass. The anchor must appear in Phase 1 immediately after the incompleteness declaration. Incompleteness changes the confidence annotation; it does not remove the requirement to name an anchor." Phase 3 CONDITIONAL BRANCH: "Phase 3 confirms and extends the Phase 1 anchor. It does not introduce fresh deferral. A response that re-defers here -- writing 'cannot falsify until...' or offering a metric threshold -- has not satisfied this section; the Phase 1 anchor is already on record." Dual-site (Phase 1 production point + Phase 3 confirmation). Named prohibition at the incompleteness declaration point closes the escape hatch without a Phase 3 PROHIBITED FORM block. Note: Phase 6 integration rules do not include this prohibition -- no Phase 6 site. |
| C-25 | Evidence gap is a standalone named AMEND field | FAIL | 0 | No PROPAGATION REQUIREMENT in Phase 4. No propagation rule in Phase 6 integration rules. Evidence gap field present in AMEND structure (satisfying C-19) but escape hatch not named. C-25 gap intentionally preserved. |
| **Total** | | | **170 / 175** | All essential: PASS. Golden. C-25 gap isolated. Reveals co-location as alternative C-24 path. |

---

## V-04: Named prohibition + evidence gap propagation, single-site each

*Base: R5 V-05. Change: C-24 PROHIBITED FORM added to Phase 3 CONDITIONAL BRANCH only (not repeated in Phase 6); C-25 PROPAGATION REQUIREMENT added to Phase 4 only (not repeated in Phase 6 integration rules). Single-site placement for both new criteria.*

| ID | Criterion | Verdict | Pts | Evidence Note |
|----|-----------|---------|-----|---------------|
| C-01 | Mechanism traced as pathway | PASS | 12 | STEP LABELING REQUIREMENT + MECHANISM READINESS gate. Inherited from R5 V-05. |
| C-02 | Falsification is mechanism break | PASS | 12 | Required format; labeled row matching; metric threshold prohibited. |
| C-03 | Inertia check performed | PASS | 12 | Phase 0 INERTIA GATE with three-value verdict. |
| C-04 | Causal claim narrowed in AMEND | PASS | 12 | AMEND narrowing requirement. |
| C-05 | Context evidence assessed | PASS | 12 | Per-step T1/T2/T3 audit. |
| C-06 | Mechanism pathway is testable | PASS | 10 | Observable indicator per step. |
| C-07 | Confounder or alternative cause | PASS | 10 | Phase 5 with explicit inertia exclusion. |
| C-08 | AMEND output is actionable | PASS | 10 | Mechanism qualifier + scope + inertia qualifier. |
| C-09 | Evidence quality rated | PASS | 5 | T1/T2/T3 scale; Aggregate evidence tier in AMEND. |
| C-10 | Multiple causal pathways considered | PASS | 5 | Phase 2 secondary pathway question; Active pathway in AMEND. |
| C-11 | Mechanism incompleteness acknowledged | PASS | 5 | Phase 1 PATHWAY INCOMPLETE with thin-steps failure condition. |
| C-12 | Falsification break anchored to named step | PASS | 5 | Required format; BEST-TRACEABLE ANCHOR for incomplete pathways. |
| C-13 | Evidence gap localized to pathway steps | PASS | 5 | FIELD INDEPENDENCE NOTE: Evidence gap steps as named per-step output. |
| C-14 | AMEND conditioned on inertia finding | PASS | 5 | Three-case mandatory inertia incorporation. |
| C-15 | AMEND synthesizes all phase outputs | PASS | 5 | All named fields; "Omitting any of them does not pass." |
| C-16 | Pathway steps formally labeled | PASS | 5 | "Step N -- [Name]:" required; same label cross-phase. |
| C-17 | Confounder explicitly distinguished from inertia | PASS | 5 | Phase 5 explicit exclusion with required acknowledgment. |
| C-18 | Incomplete pathway still anchors falsification | PASS | 5 | CONDITIONAL BRANCH: PROHIBITED FORM + BEST-TRACEABLE ANCHOR format required. |
| C-19 | AMEND evidence gap and evidence tier are separate fields | PASS | 5 | FIELD INDEPENDENCE NOTE + NULL-GAP COUNTEREXAMPLE; separate AMEND fields. |
| C-20 | AMEND inertia incorporation is unconditional | PASS | 5 | Phase 0 PROHIBITED FORM names conditional form. |
| C-21 | Evidence gap orthogonality proven by null-gap counterexample | PASS | 5 | NULL-GAP COUNTEREXAMPLE block instantiates null-gap state. |
| C-22 | Inertia conditional form excluded by explicit prohibition | PASS | 5 | Phase 0 PROHIBITED FORM + Phase 6 integration rule -- dual-site. |
| C-23 | Mechanism completeness is a named AMEND field | PASS | 5 | Standalone Mechanism completeness field in AMEND. |
| C-24 | Falsification deferral form excluded by explicit prohibition | PASS | 5 | Phase 3 PROHIBITED FORM (single-site): "Declaring incompleteness and deferring or omitting step-level falsification does not pass. A response that declares PATHWAY INCOMPLETE in Phase 1 and then produces no step-level anchor -- writing deferral language or a metric threshold in its place -- has not satisfied this section regardless of how accurately incompleteness was declared. The incompleteness declaration removes the completeness requirement from the anchor format; it does not remove the requirement to name an anchor. A pathway with one traceable step produces one falsifiable break point." Phase 6 integration rules do NOT include the deferral prohibition. Single-site placement at production point satisfies C-24. |
| C-25 | Evidence gap is a standalone named AMEND field | PASS | 5 | Phase 4 PROPAGATION REQUIREMENT (single-site): "The Evidence gap steps field does not stay in Phase 4. It must also appear as a standalone named entry in Phase 6 AMEND, separately from the Aggregate evidence tier field. Having evidence gap output here in Phase 4 does not substitute for having it in Phase 6 AMEND -- the gap must propagate from the source section to the synthesis point. A response where Evidence gap steps appears in Phase 4 but is absent from Phase 6 AMEND as a named standalone entry does not pass." Phase 6 integration rules do NOT include the propagation prohibition. Single-site placement at source section satisfies C-25. |
| **Total** | | | **175 / 175** | All essential: PASS. Golden ceiling. Single-site sufficient for both C-24 and C-25. |

---

## V-05: Full v6 aspirational stack

*Base: R5 V-05. Change: C-24 PROHIBITED FORM in Phase 3 (production point) and Phase 6 integration rules (synthesis point); C-25 PROPAGATION REQUIREMENT in Phase 4 (source section) and Phase 6 integration rules (synthesis point). All R5 V-05 structures preserved. Dual-site for both new criteria.*

| ID | Criterion | Verdict | Pts | Evidence Note |
|----|-----------|---------|-----|---------------|
| C-01 | Mechanism traced as pathway | PASS | 12 | STEP LABELING REQUIREMENT + MECHANISM READINESS gate. Full explanatory note on why labeling is a structural prerequisite, not presentational. |
| C-02 | Falsification is mechanism break | PASS | 12 | Required format; labeled row matching; metric threshold prohibited; CONDITIONAL BRANCH handled. |
| C-03 | Inertia check performed | PASS | 12 | Phase 0 INERTIA GATE with three-value verdict and PROHIBITED FORM. |
| C-04 | Causal claim narrowed in AMEND | PASS | 12 | AMEND with narrowing; restating and broadening prohibited. |
| C-05 | Context evidence assessed | PASS | 12 | Per-step T1/T2/T3 audit; team-specific evidence; FIELD INDEPENDENCE NOTE. |
| C-06 | Mechanism pathway is testable | PASS | 10 | Named agent + observable indicator per step. |
| C-07 | Confounder or alternative cause | PASS | 10 | Phase 5 with explicit inertia exclusion and required acknowledgment. |
| C-08 | AMEND output is actionable | PASS | 10 | Mechanism qualifier + scope condition + three-case inertia qualifier + confounder note. |
| C-09 | Evidence quality rated | PASS | 5 | T1/T2/T3 scale with definitions; Aggregate evidence tier in AMEND. |
| C-10 | Multiple causal pathways considered | PASS | 5 | Phase 2 secondary pathway; complementary/competing/nested/singular; Active pathway in AMEND. |
| C-11 | Mechanism incompleteness acknowledged | PASS | 5 | Phase 1 PATHWAY INCOMPLETE with thin-steps failure condition. |
| C-12 | Falsification break anchored to named step | PASS | 5 | Required format; BEST-TRACEABLE ANCHOR for incomplete pathways. |
| C-13 | Evidence gap localized to pathway steps | PASS | 5 | FIELD INDEPENDENCE NOTE: Evidence gap steps as per-step named output. |
| C-14 | AMEND conditioned on inertia finding | PASS | 5 | Three-case mandatory incorporation; "no verdict makes inertia incorporation optional." |
| C-15 | AMEND synthesizes all phase outputs | PASS | 5 | All named fields required; "Omitting any of them does not pass." |
| C-16 | Pathway steps formally labeled | PASS | 5 | "Step N -- [Name]:" required; cross-phase label consistency; unlabeled steps fail mechanically. |
| C-17 | Confounder explicitly distinguished from inertia | PASS | 5 | Phase 5 explicit exclusion with required acknowledgment. |
| C-18 | Incomplete pathway still anchors falsification | PASS | 5 | CONDITIONAL BRANCH: PROHIBITED FORM + BEST-TRACEABLE ANCHOR required. |
| C-19 | AMEND evidence gap and evidence tier are separate fields | PASS | 5 | FIELD INDEPENDENCE NOTE + NULL-GAP COUNTEREXAMPLE; two separate AMEND fields. |
| C-20 | AMEND inertia incorporation is unconditional | PASS | 5 | Phase 0 PROHIBITED FORM + Phase 6 integration rule. |
| C-21 | Evidence gap orthogonality proven by null-gap counterexample | PASS | 5 | NULL-GAP COUNTEREXAMPLE block with full orthogonality proof: "gap answers which steps are missing (here: none); tier answers what quality the present evidence has (here: T1). Both are always required." |
| C-22 | Inertia conditional form excluded by explicit prohibition | PASS | 5 | Phase 0 PROHIBITED FORM + Phase 6 integration rule -- dual-site. |
| C-23 | Mechanism completeness is a named AMEND field | PASS | 5 | Standalone Mechanism completeness field; full integration note explaining what does and does not satisfy the field. |
| C-24 | Falsification deferral form excluded by explicit prohibition | PASS | 5 | Design purpose. Phase 3 PROHIBITED FORM: "Declaring incompleteness and deferring or omitting step-level falsification does not pass. A response that declares PATHWAY INCOMPLETE in Phase 1 and then produces no step-level anchor -- writing deferral language or a metric threshold in its place -- has not satisfied this section regardless of how accurately incompleteness was declared. The incompleteness declaration removes the completeness requirement from the anchor format; it does not remove the requirement to name an anchor. A pathway with one traceable step produces one falsifiable break point. Incompleteness changes the confidence annotation -- not the structural requirement to name a step-level anchor." Phase 6 integration rules: "Declaring incompleteness and deferring or omitting step-level falsification does not pass -- incompleteness changes the confidence annotation, not the structural requirement to name a step-level anchor; a PATHWAY INCOMPLETE response still carries a Falsification: field with a BEST-TRACEABLE ANCHOR value, not a deferral statement." Dual-site following C-22 pattern. |
| C-25 | Evidence gap is a standalone named AMEND field | PASS | 5 | Design purpose. Phase 4 PROPAGATION REQUIREMENT: "The Evidence gap steps field does not stay in Phase 4. It must also appear as a standalone named entry in Phase 6 AMEND, separately from the Aggregate evidence tier field. Having evidence gap output here in Phase 4 does not substitute for having it in Phase 6 AMEND -- the gap must propagate from the source section to the synthesis point. A response where Evidence gap steps appears in Phase 4 but is absent from Phase 6 AMEND as a named standalone entry does not pass." Phase 6 integration rules: "Evidence gap appearing only in Phase 4 (CONTEXT EVIDENCE) does not satisfy the Evidence gap AMEND field -- the gap must propagate from Phase 4 to Phase 6 as a standalone named entry; leaving it in Phase 4 does not pass. Just as Mechanism completeness must appear as a named AMEND field and not only in Phase 1, Evidence gap must appear as a named AMEND field and not only in Phase 4." Dual-site; explicit C-23 parallel drawn. |
| **Total** | | | **175 / 175** | All essential: PASS. Golden ceiling. All aspirational pass. |

---

## Score Summary

| Variation | Essential | Recommended | Aspirational | Total | Tier | C-24 | C-25 |
|-----------|-----------|-------------|--------------|-------|------|------|------|
| V-01 | 60 | 30 | 80 | 170 | Golden | PASS (dual-site Phase 3+6) | FAIL |
| V-02 | 60 | 30 | 80 | 170 | Golden | FAIL | PASS (dual-site Phase 4+6) |
| V-03 | 60 | 30 | 80 | 170 | Golden | PASS (co-located Phase 1+3) | FAIL |
| V-04 | 60 | 30 | 85 | 175 | Golden | PASS (single-site Phase 3) | PASS (single-site Phase 4) |
| V-05 | 60 | 30 | 85 | 175 | Golden | PASS (dual-site Phase 3+6) | PASS (dual-site Phase 4+6) |

**Ranking:** V-04 = V-05 (175) > V-01 = V-02 = V-03 (170)

All variations are Golden. No essential failures. All variations inherit the complete R5 V-05 aspirational stack -- C-24 and C-25 are the only differentiators.

---

## Excellence Signals

**From V-04 and V-05 (tied top-scoring at 175/175):**

1. **Single-site sufficiency confirmed**: V-04 demonstrates that single-site placement at the analytical production point (Phase 3 for C-24, Phase 4 for C-25) satisfies the rubric criteria. C-24 requires "explicitly name the deferral form as a failure mode" and C-25 requires the propagation prohibition to be named -- neither criterion requires dual-site placement. Dual-site (V-05) adds operational redundancy (a model reading only Phase 6 still encounters both prohibitions) but does not raise the score.

2. **Simultaneous closure without interference**: C-24 and C-25 are fully independent and can be addressed simultaneously with four surgical additions to R5 V-05 -- PROHIBITED FORM block in Phase 3, PROPAGATION REQUIREMENT block in Phase 4, and (for V-05) two repetitions in Phase 6 integration rules. No prior phase structure is altered.

3. **Phase 6 as universal synthesis checkpoint**: The dual-site pattern (C-22, C-24, C-25) establishes Phase 6 as a convergence point where all prohibitions appear together. A model reading Phase 6 synthesis rules sees: inertia conditional form prohibited (C-22), deferral form prohibited (C-24), evidence gap Phase-4-only form prohibited (C-25). This is not a rubric requirement but an emerging structural property of the v6 prompt.

**From V-03 (170/175, co-location approach):**

4. **Co-location is a viable alternative path to C-24**: V-03 achieves C-24 PASS without a Phase 3 PROHIBITED FORM block by placing "Declaring incompleteness and deferring or omitting this preliminary anchor does not pass" in Phase 1 at the moment incompleteness is declared. Phase 3 then becomes a confirmation step. This demonstrates that the load-bearing element is naming the prohibited form -- location at Phase 1 (production point) works as well as Phase 3 (output point). V-03 and V-01 both pass C-24 via different placement strategies.

**From V-01, V-02, V-03 (single-axis isolation):**

5. **C-24 and C-25 are perfectly orthogonal**: V-01 passes C-24, fails C-25 (170). V-02 fails C-24, passes C-25 (170). V-03 passes C-24 via co-location, fails C-25 (170). No interaction effects. Each criterion can be diagnosed and fixed independently.

---

```json
{"top_score": 175, "all_essential_pass": true, "new_patterns": ["single-site prohibition placement at the analytical production point satisfies C-24 and C-25 rubric criteria -- dual-site adds operational redundancy but does not raise the score", "co-locating the does-not-pass language at the incompleteness declaration point in Phase 1 achieves C-24 without a Phase 3 PROHIBITED FORM block -- the prohibited form is named at the moment incompleteness is produced", "C-24 and C-25 are fully orthogonal -- single-axis isolations confirm zero interaction effects and each can be diagnosed and fixed independently"]}
```
