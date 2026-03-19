`discover-causal-rubric-v12-2026-03-17.md` written.

---

## What changed: v11 -> v12

**1 new criterion: C-34** from R11 excellence signals E-01 and E-02.

**C-34: `phase1_anchor_prohibition_stated: true | false | n/a` ARTIFACT field** -- tracks C-27 compliance machine-readably, completing the four-position symmetric ARTIFACT audit table.

| Production point | Criterion | ARTIFACT field | Tracked by |
|-----------------|-----------|----------------|------------|
| Phase 1 | C-26 (preliminary anchor) | `preliminary_anchor_declared` | C-26 |
| Phase 1 | C-27 (prohibition phrase) | `phase1_anchor_prohibition_stated` | **C-34** (new) |
| Phase 3 | C-31 (prohibited form) | `phase3_anchor_update_prohibited_form` | C-33 |
| Phase 6 | C-30 (stale-anchor rule) | `anchor_updated_from_phase1` | C-30 |

**E-02 gradeability rule** embedded in C-34: when C-27 fails (prohibition phrase absent), the correct field value is `false` not absent. Absence of the field fails C-34 separately from the C-27 fail. Three states: (a) C-27 PASS + field `true` -- fully compliant; (b) C-27 FAIL + field `false` -- behavioral fail, correct audit (C-34 PASS); (c) C-27 FAIL + field absent -- behavioral fail, missing audit (C-34 FAIL).

**Scoring:** 26 aspirational x 5 = 130 pts | Total **220 pts** | Golden **>= 210** | Acceptable **195-209** | Passing **180-194**

**R11 retro-scores under v12:** V-01..V-04 score 210 (Golden floor, all fail C-34); V-05 scores 220 (ceiling, passes C-34).
 | C-30 |

**Scoring update:**
- Aspirational: 125 -> 130 pts (26 criteria x 5 pts)
- Total: 215 -> **220 pts**
- Golden **>= 210** | Acceptable **195-209** | Passing **180-194**
- Previous ceiling (215) = new Golden floor

**R11 scores under v12:**

| Variation | v11 score | C-34 | v12 score | Tier |
|-----------|-----------|------|-----------|------|
| V-01 (C-32 stripped) | 210 | FAIL | **210** | Golden (floor) |
| V-02 (C-32 softened) | 210 | FAIL | **210** | Golden (floor) |
| V-03 (C-33 stripped) | 210 | FAIL | **210** | Golden (floor) |
| V-04 (C-33 body-placement) | 210 | FAIL | **210** | Golden (floor) |
| V-05 (full ceiling) | 215 | PASS | **220** | Golden (ceiling) |

C-34 FAIL for V-01 through V-04: none carry the `phase1_anchor_prohibition_stated` ARTIFACT field. C-34 is gradeable in all five variations (C-26 PASS in all -- inherited from R10 V-05 base).

---

## Criteria summary

| Tier | IDs | Pts |
|------|-----|-----|
| Essential | C-01 through C-05 | 60 |
| Recommended | C-06 through C-08 | 30 |
| Aspirational | C-09 through C-34 | 130 |

**C-21 through C-34 relationship to earlier criteria:** These fourteen criteria do not replace C-12, C-15, C-18, C-19, C-20, or C-26 -- they capture the stricter pass conditions those criteria require at full depth. A response can pass C-26 (anchor at Phase 1) while failing C-27 (no prohibition named at Phase 1), C-28 (Phase 3 does not back-reference it), C-29 (no Phase 6 integration rule), C-30 (Phase 6 carries stale Phase 1 anchor instead of Phase 3 updated anchor), or C-31 (Phase 3 update point carries no prohibited form). A response can pass C-31 while failing C-32: Phase 3 carries the self-referential prohibited form, but Phase 6 never names that structural requirement at synthesis. A response can pass C-30 while failing C-33: anchor provenance is tracked in the ARTIFACT frontmatter, but the Phase 3 prohibited form status is not. A response can pass C-27 while failing C-34: the Phase 1 prohibition phrase is present in the response, but the `phase1_anchor_prohibition_stated` ARTIFACT field is absent.

---

## Essential Criteria (60 pts total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-01 | **Mechanism traced as pathway** | structure | essential | Response traces a causal pathway from X to Y as a sequence of observable intermediate steps -- not a summary claim, not a single leap. Each step identifies what changes, who acts, and what the observable indicator is. A response that confirms "X causes Y" without tracing the mechanism does not pass. |
| C-02 | **Falsification is mechanism break** | precision | essential | The falsification condition names a specific point in the causal pathway where the mechanism would fail -- "the mechanism fails if [step] does not occur" -- not a metric threshold ("if retention does not improve") or outcome negation. The break must reference the mechanism, not the result. |
| C-03 | **Inertia check performed** | coverage | essential | Response checks whether Y would occur anyway without X -- whether the status quo, through existing trends or momentum, already produces the outcome. A response that does not address inertia does not pass. An explicit "not competing" verdict passes; silence does not. |
| C-04 | **Causal claim narrowed in AMEND** | correctness | essential | The AMEND section produces a narrowed causal claim -- scoped to a more specific condition, user segment, mechanism qualifier, or population than the input hypothesis. Restating the original does not pass. Broadening does not pass. |
| C-05 | **Context evidence assessed** | correctness | essential | Response evaluates whether evidence that the mechanism holds exists in the feature's specific context (team, product, users). "We do not have evidence yet" is a valid answer; silence is not. |

---

## Recommended Criteria (30 pts total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-06 | **Mechanism pathway is testable** | depth | recommended | The described pathway is specific enough that a team could design an observation or test to confirm or deny it. Vague pathways ("X leads to better outcomes") do not pass; named measurable steps do. |
| C-07 | **At least one confounder or alternative cause identified** | depth | recommended | Response names at least one plausible alternative explanation for Y that does not involve X, or a confounding variable that could create the appearance of X causing Y. |
| C-08 | **AMEND output is actionable** | behavior | recommended | The narrowed claim in AMEND is concrete enough to act on -- includes a bounded scope (user segment, condition, timeframe) or a mechanism qualifier. Generic narrowings ("add more evidence") do not pass. |

---

## Aspirational Criteria (130 pts total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-09 | **Evidence quality rated** | depth | aspirational | Response distinguishes between evidence types (anecdotal, observed correlation, controlled measurement) and rates the current strength of causal evidence, not just its presence or absence. |
| C-10 | **Multiple causal pathways considered** | depth | aspirational | Response identifies more than one possible causal pathway from X to Y and notes whether they are complementary, competing, or independently falsifiable. |
| C-11 | **Mechanism incompleteness acknowledged** | honesty | aspirational | When the response cannot name 3 or more observable intermediate steps, it explicitly says so rather than fabricating a weak or vague pathway to appear complete. Self-disclosure ("mechanism not fully traceable") passes; a thin 3-step pathway that papers over the gap does not. |
| C-12 | **Falsification break anchored to named step** | precision | aspirational | The mechanism-break statement names the specific step number or label from the causal pathway (e.g., "Step 2 -- user sees the prompt -- does not occur"), not just a generic break description. Requires a pathway with named steps to be gradeable. |
| C-13 | **Evidence gap localized to pathway steps** | precision | aspirational | The context evidence section identifies which specific steps in the mechanism lack supporting evidence, not just whether evidence exists in aggregate. Output must name at least one step with missing evidence or confirm all steps have support -- a per-step accounting, not a summary verdict. |
| C-14 | **AMEND conditioned on inertia finding** | integration | aspirational | The narrowed causal claim in AMEND explicitly incorporates the inertia check result -- e.g., scopes the claim to contexts where the status quo does not already produce Y, or flags the claim as invalid if the inertia check shows the feature is redundant. A narrowed claim that ignores the inertia finding does not pass. |
| C-15 | **AMEND synthesizes all phase outputs** | integration | aspirational | The AMEND section explicitly names and incorporates the outputs of every prior analytical phase -- inertia verdict, mechanism completeness status, evidence tier, and confounder finding -- rather than summarizing in aggregate or selectively ignoring phases. An AMEND that references only some phase outputs does not pass. Partial integration (e.g., evidence tier present, inertia absent) does not pass. |
| C-16 | **Pathway steps formally labeled** | precision | aspirational | Each step in the causal pathway carries a persistent formal label (e.g., "Step N -- [Name]:") that the falsification and evidence sections can reference by name. Positional references only ("the second step") and prose bullet lists without persistent labels do not pass. Formal labeling is the prerequisite that makes C-12 and C-13 mechanically gradeable -- this criterion rewards having that prerequisite in place. |
| C-17 | **Confounder explicitly distinguished from inertia** | coverage | aspirational | When naming alternative explanations for Y, the response explicitly excludes the inertia/status-quo case from the confounder analysis -- treating "does nothing also cause Y?" and "what else independently causes Y?" as separate analytical questions. A response where the only named alternative is the inertia case, or where confounder and inertia analysis are merged in a single section without explicit separation, does not pass. |
| C-18 | **Incomplete pathway still anchors falsification** | honesty | aspirational | When mechanism incompleteness is declared (per C-11), the falsification break is still anchored to the highest-confidence labeled step traced rather than deferred, omitted, or replaced with a metric threshold. An incomplete pathway that names a specific step-anchored failure point passes; one that declares incompleteness and then offers no step-level falsification does not. Requires C-11 PASS and C-12 PASS to be gradeable -- if either fails, this criterion is not scored. |
| C-19 | **AMEND evidence gap and evidence tier are separate fields** | integration | aspirational | The AMEND section produces two distinct named outputs: (1) the evidence gap -- the list of pathway step labels that lack supporting evidence -- and (2) the evidence tier -- the T1/T2/T3 aggregate quality rating for all evidence evaluated. A response where these appear merged into a single entry, or where one is present and the other omitted, does not pass. The distinction matters: a pathway where all steps have T1 evidence has no gap steps but still carries an evidence tier; a pathway with gap steps may still carry a tier rating for the steps that do have evidence. |
| C-20 | **AMEND inertia incorporation is unconditional** | integration | aspirational | The amended causal claim in AMEND incorporates the inertia verdict regardless of verdict value -- not only when the verdict is Competing or Unclear. Even when the verdict is Not competing, the amended claim must explicitly reference the inertia finding (e.g., confirming that the feature adds causal effect beyond what the status quo already produces). A response where inertia incorporation is conditioned on the verdict being Competing or Unclear leaves a Not-competing escape hatch and does not pass. |
| C-21 | **Evidence gap orthogonality proven by null-gap counterexample** | precision | aspirational | The response demonstrates that evidence gap and evidence tier are orthogonal fields by including the null-gap counterexample: explicitly showing (or instantiating) a case where a pathway with all T1 evidence has gap: none but still carries evidence tier T1. Asserting that the fields are separate without demonstrating the null-gap case does not pass -- the counterexample is the load-bearing element that prevents the category error ("no gaps means no tier needed"). |
| C-22 | **Inertia conditional form excluded by explicit prohibition** | integration | aspirational | The unconditional inertia rule (C-20) is not self-enforcing by positive statement alone. The response must explicitly name the prohibited conditional form as a failure mode -- e.g., "conditioning inertia incorporation on the verdict being Competing or Unclear does not pass" or equivalent language that closes the escape hatch by name. A response that states the positive rule ("inertia is always incorporated") without naming the conditional form as prohibited does not pass. |
| C-23 | **Mechanism completeness is a named AMEND field** | integration | aspirational | The AMEND section includes mechanism completeness status as a distinct named field (e.g., "Mechanism completeness: complete" or "Mechanism completeness: incomplete at Step N") separate from the amended clause text. A mechanism qualifier embedded within the amended claim sentence -- even a precise one -- does not substitute for a standalone named field. Requires C-15 PASS to be meaningful: C-23 captures the strictest form of the C-15 mechanism completeness requirement. |
| C-24 | **Falsification deferral form excluded by explicit prohibition** | precision | aspirational | The step-anchored falsification rule (C-18) is not self-enforcing by structural requirement alone. The response must explicitly name the deferral form as a failure mode -- e.g., "declaring incompleteness and deferring or omitting step-level falsification does not pass" or equivalent language that closes the deferral escape hatch by name. A response that structurally prevents deferral (by requiring a step anchor format in all cases) without naming the deferral form as prohibited does not pass. Parallel to C-22: the positive rule alone is not sufficient -- the prohibited form must be named. Requires C-18 PASS to be meaningful. |
| C-25 | **Evidence gap is a standalone named AMEND field** | integration | aspirational | The AMEND section includes evidence gap as a distinct named field (e.g., "Evidence gap: none -- all steps supported" or "Evidence gap: Step 2 -- [Name], Step 4 -- [Name]") separate from the evidence tier field. Presence of an evidence gap output in the CONTEXT EVIDENCE section does not substitute -- the gap must also propagate into AMEND as a named standalone field. A response where evidence gap appears only in CONTEXT EVIDENCE (or not at all in AMEND) does not pass. Requires C-19 PASS to be meaningful: C-25 captures the strictest integration requirement for evidence gap, parallel to how C-23 captures the strictest integration requirement for mechanism completeness. |
| C-26 | **Falsification anchor co-located with incompleteness declaration** | honesty | aspirational | When PATHWAY INCOMPLETE is declared in Phase 1 (per C-11), the response immediately produces a named step-anchored falsification entry (preliminary anchor) at the Phase 1 declaration point -- before mechanism tracing continues into later phases. Phase 3 then extends or confirms the Phase 1 preliminary anchor rather than serving as the first and only falsification point. A response that declares PATHWAY INCOMPLETE in Phase 1 and defers all anchor work to Phase 3 does not pass -- even if Phase 3 produces a valid step-anchored break. The load-bearing requirement is structural proximity: the anchor must be produced at the moment incompleteness is declared, not at a downstream phase. Requires C-11 PASS and C-18 PASS to be gradeable. |
| C-27 | **C-26 prohibition co-located with Phase 1 anchor requirement** | honesty | aspirational | When PATHWAY INCOMPLETE is declared in Phase 1, the prohibition for omitting the preliminary anchor must be named at Phase 1 -- not deferred to Phase 3 or later. The "does not pass" language is the load-bearing element; a `PROHIBITED FORM:` block label is not required -- inline "does not pass" in the sub-step header (e.g., "required here before Phase 2; proceeding to Phase 2 without producing this anchor does not pass") satisfies the criterion. A response where the Phase 1 anchor requirement is present but no "does not pass" language appears at Phase 1 -- whether inline or in a block -- does not pass. Structural sequence alone (sub-step ordering) without the explicit prohibition phrase does not close the escape hatch. Parallel to C-24 (which requires the deferral prohibition for C-18 to be named explicitly): C-27 requires the prohibition for C-26 (missing Phase 1 anchor) to be co-located with the Phase 1 anchor requirement. Requires C-26 PASS to be gradeable. |
| C-28 | **Phase 3 frames anchor as confirmation of Phase 1 preliminary anchor** | honesty | aspirational | When a Phase 1 preliminary anchor exists (per C-26), Phase 3 must explicitly reference the Phase 1 anchor as prior record -- using language such as "already on record from Phase 1 SUB-STEP 2" or equivalent explicit prior-record acknowledgment -- and frame its falsification work as confirmation and extension of that record. Instruction-to-confirm language alone ("confirm and extend the preliminary anchor from Phase 1") without explicit prior-record acknowledgment does not pass: it reads as production instruction rather than confirmation, preserving the re-origination pattern. The back-reference phrase ("already on record" or equivalent) is the load-bearing element that distinguishes confirmation framing from origination framing. A response where Phase 3 produces an anchor without referencing the Phase 1 anchor as prior record does not pass regardless of how Phase 3 labels its output. Requires C-26 PASS to be gradeable. |
| C-29 | **C-26 cross-phase integrity rule named at synthesis** | honesty | aspirational | The synthesis/AMEND phase includes an integration rule that explicitly detects the C-26 cross-phase violation: naming that a Falsification field first appearing at synthesis without a corresponding Phase 1 preliminary anchor does not pass. Any Phase 6 position satisfies this criterion -- a single entry in the integration rules list is sufficient; the rule does not need to appear in both the integration rules list and the Falsification field description. This creates a third enforcement site (after Phase 1 structural requirement and Phase 3 confirmation framing) that tests the full causal chain at the synthesis point -- where a model might produce a falsification for the first time while prior phases appeared compliant. A response that satisfies C-26, C-27, and C-28 but includes no such synthesis-phase integrity rule does not pass. Requires C-26 PASS to be gradeable. |
| C-30 | **Phase 6 Falsification tracks Phase 3 anchor update** | integration | aspirational | When Phase 3 updates the preliminary Phase 1 anchor to a higher-confidence step (anchor update path), Phase 6 must carry the Phase 3 updated step as its Falsification break -- not the Phase 1 preliminary anchor verbatim. A response where Phase 6 Falsification references the Phase 1 anchor step even after Phase 3 has updated it commits a stale-anchor propagation failure: the synthesis point carries outdated anchor provenance. The response must include an explicit integration rule naming the stale-anchor failure mode and, where applicable, an `anchor_updated_from_phase1: true | false | n/a` ARTIFACT field to make the propagation status machine-readable. A response with no Phase 3 anchor update (Phase 3 confirms verbatim) carries C-30 as N/A. Requires C-26 PASS and C-28 PASS to be gradeable: C-26 ensures the Phase 1 preliminary anchor exists; C-28 ensures Phase 3 frames its work as confirmation/extension, establishing the update path that C-30 checks. |
| C-31 | **Phase 3 CONDITIONAL BRANCH carries stale-anchor prohibited form** | honesty | aspirational | When Phase 3 updates the preliminary Phase 1 anchor to a higher-confidence step, the Phase 3 CONDITIONAL BRANCH must also carry a PROHIBITED FORM explicitly naming that correctly recording the anchor update at Phase 3 does not close the Phase 6 propagation requirement -- e.g., "recording the updated BEST-TRACEABLE ANCHOR here does not complete the propagation requirement; Phase 6 Falsification must also carry the updated step -- correctly recording the update here does not close the Phase 6 propagation requirement." A Phase 3 CONDITIONAL BRANCH that names only the positive update instruction ("carry the Phase 3 step forward to Phase 6") without naming that doing so at Phase 3 is insufficient to satisfy Phase 6 does not pass. This is the dual-site enforcement parallel to C-26/C-27: C-30 requires the stale-anchor check at the Phase 6 synthesis point; C-31 requires the prohibited form at the Phase 3 update point. A response can pass C-30 while failing C-31 -- Phase 6 names the stale-anchor failure mode, but Phase 3 never states that its own update record does not satisfy that requirement. Requires C-30 PASS to be gradeable; N/A when Phase 3 confirms verbatim (same condition as C-30 N/A). |
| C-32 | **C-31 structural requirement named at Phase 6 synthesis** | integration | aspirational | The synthesis/AMEND phase includes an integration rule explicitly naming the C-31 structural requirement -- that the Phase 3 CONDITIONAL BRANCH must carry a PROHIBITED FORM stating that correctly recording the anchor update at Phase 3 does not close the Phase 6 propagation requirement. A response that satisfies C-31 (Phase 3 carries the self-referential prohibited form) but includes no Phase 6 integration rule naming that structural requirement does not pass. Parallel to C-29: C-29 requires Phase 6 to name the C-26 cross-phase integrity rule (first-appearance-at-synthesis); C-32 requires Phase 6 to name the C-31 structural requirement (Phase 3 update does not close Phase 6). Any Phase 6 position satisfies this criterion -- a single entry in the integration rules list is sufficient. This creates a fourth enforcement site for the anchor update chain at the synthesis point, closing the gap where a response satisfies C-31 at Phase 3 but omits the matching validation at Phase 6. Requires C-31 PASS to be gradeable; N/A when C-31 is N/A (Phase 3 confirms verbatim). |
| C-33 | **Phase 3 prohibited-form status tracked as ARTIFACT field** | integration | aspirational | The ARTIFACT frontmatter includes a `phase3_anchor_update_prohibited_form: true | false | n/a` field that makes the Phase 3 prohibited form status machine-readable, parallel to the `anchor_updated_from_phase1: true | false | n/a` ARTIFACT field required by C-30. `true` when Phase 3 CONDITIONAL BRANCH carries the required self-referential prohibited form (C-31 pass condition met); `false` when Phase 3 carries only a positive update instruction, a softened qualifier ("necessary but not sufficient"), or a forward-looking prohibited form (C-31 fail cases); `n/a` when Phase 3 confirms the anchor verbatim without updating to a higher-confidence step (same N/A condition as C-30 and C-31). A response that satisfies C-30 (anchor provenance tracked in ARTIFACT) but omits this field leaves the Phase 3 co-location status machine-unreadable. Requires C-30 PASS to be gradeable (same N/A condition). |
| C-34 | **Phase 1 prohibition status tracked as ARTIFACT field** | integration | aspirational | The ARTIFACT frontmatter includes a `phase1_anchor_prohibition_stated: true | false | n/a` field that makes the Phase 1 prohibition-stated status (C-27) machine-readable, completing the symmetric ARTIFACT audit table. `true` when Phase 1 includes the required "does not pass" language at the preliminary anchor requirement (C-27 pass condition met); `false` when Phase 1 carries the anchor requirement without the prohibition phrase -- whether inline or block, any position -- (C-27 fail case); `n/a` when the pathway is complete and Phase 1 incompleteness is not declared (same N/A condition as C-26 and C-27). A response that satisfies C-27 but omits this field leaves the Phase 1 prohibition status machine-unreadable. Per the E-02 field gradeability design principle: when C-27 fails (prohibition phrase absent at Phase 1), the correct field value is `false`, not absent -- absence of the field fails C-34 separately from the C-27 fail; presence with `false` reflects behavioral failure with correct audit. Requires C-26 PASS to be gradeable (same N/A condition as C-26 and C-27). |

---

**Design rationale for C-34:**

C-34 closes the ARTIFACT audit gap exposed by V-05 R11's `phase1_anchor_prohibition_stated` field addition. The E-01 pattern ("Symmetric ARTIFACT audit: for every enforcement chain criterion, pair with a machine-readable frontmatter field tracking compliance at that production point") identifies four enforcement chain criteria (C-26, C-27, C-30, C-31) and maps each to an ARTIFACT field. Before v12, three of the four fields existed:

- `anchor_updated_from_phase1` tracks C-30 (required by C-30 itself)
- `phase3_anchor_update_prohibited_form` tracks C-31 (required by C-33)
- `preliminary_anchor_declared` tracks C-26 (structural, implicit in C-26 requirement)

The missing fourth field, `phase1_anchor_prohibition_stated` tracking C-27, is what C-34 requires. A response that satisfies C-27 (Phase 1 includes the prohibition phrase) but omits this ARTIFACT field has made the prohibition behavior observable in the response text but not machine-readable in the frontmatter. C-34 closes this gap.

The parallel to C-33 is exact:
- C-33: `phase3_anchor_update_prohibited_form` tracks C-31 (Phase 3 prohibited form) -- requires C-30 PASS, gradeable even when C-31 FAIL (field value `false`)
- C-34: `phase1_anchor_prohibition_stated` tracks C-27 (Phase 1 prohibition phrase) -- requires C-26 PASS, gradeable even when C-27 FAIL (field value `false`)

The E-02 field gradeability design principle is embedded in both C-33 and C-34: absence of the field is the failure mode that C-33/C-34 test; presence with `false` when the underlying criterion fails is the correct machine-readable state. This enables scorecards to distinguish three states: (a) criterion PASS + field `true` -- fully compliant; (b) criterion FAIL + field `false` -- behavioral failure with correct audit; (c) criterion FAIL + field absent -- behavioral failure with missing audit (C-34 fail). Only (c) fails C-34.

Without C-34, a response can satisfy C-27 at Phase 1 without any ARTIFACT entry confirming that the prohibition status is machine-readable. The symmetric ARTIFACT audit is now closed: every enforcement chain criterion in the anchor-provenance chain has a corresponding machine-readable field.

---

**Design rationale for C-32 (carried from v11):**

C-32 closes the ceiling gap exposed by V-05 R10's Phase 6 integration rule addition: when the dual-site enforcement chain (C-30 at Phase 6, C-31 at Phase 3) is complete, a fourth enforcement site at synthesis names the C-31 structural requirement explicitly. V-01 through V-04 in R10 all pass C-30 but fail C-31 -- they have the Phase 6 stale-anchor integration rule but not the Phase 3 co-located prohibited form. V-05 R10 adds both the Phase 3 prohibited form (C-31) and a Phase 6 integration rule naming that the Phase 3 CONDITIONAL BRANCH must carry it (C-32).

The parallel to C-29 is exact:
- C-29: Phase 6 names the C-26 cross-phase integrity rule ("Falsification first appearing at synthesis without a Phase 1 anchor does not pass")
- C-32: Phase 6 names the C-31 structural requirement ("Phase 3 CONDITIONAL BRANCH must carry the prohibited form; carrying only a positive update instruction at Phase 3 does not close Phase 6")

Without C-32, a response can satisfy C-31 (Phase 3 carries the prohibited form) without the Phase 6 synthesis point ever naming that the C-31 requirement exists. The synthesis point is the convergence of all analytical outputs -- naming the C-31 requirement there confirms the dual-site enforcement chain is fully visible at the point where graders and models most often check integration.

---

**Design rationale for C-33 (carried from v11):**

C-33 closes the ceiling gap exposed by V-05 R10's ARTIFACT field addition: the ARTIFACT frontmatter should track the Phase 3 prohibited form status with the same machine-readable field pattern already used for anchor provenance (C-30). A response that satisfies C-30 (includes `anchor_updated_from_phase1: true | false | n/a`) has made anchor provenance machine-readable but left Phase 3 co-location status untracked. The two fields form a complete ARTIFACT-level audit of the Phase 3 anchor update path:

- `anchor_updated_from_phase1: true | false | n/a` -- did Phase 3 upgrade the anchor, and did Phase 6 follow the update? (C-30)
- `phase3_anchor_update_prohibited_form: true | false | n/a` -- did Phase 3 carry the self-referential prohibited form at the update point? (C-33)

Gradeability differs from C-31 and C-32: C-33 requires C-30 PASS (not C-31 PASS), because the field tracks Phase 3 co-location status independently of whether the prohibited form was present. A response that passes C-30 but fails C-31 should still include this field with value `false` -- the field is gradeable and the correct value is `false`, reflecting the C-31 fail. This enables scorecards to distinguish C-31 FAIL with correct ARTIFACT reporting (field present, value `false`) from C-33 FAIL (field absent entirely). Only absence of the field fails C-33; presence with value `false` when C-31 fails is the correct machine-readable state.

---

**Design rationale for C-31 (carried from v10):**

C-31 closes the ceiling gap exposed by V-05's Phase 3 co-location pattern: when Phase 3 updates the preliminary anchor, the update point itself must carry a prohibited form that names the Phase 6 propagation requirement as unsatisfied by the Phase 3 record alone. V-01 through V-04 all pass C-30 (in R9 they fail C-30 -- C-31 is the next ceiling above C-30). V-05 adds both the Phase 6 integration rule (C-30) and the Phase 3 ANCHOR-UPDATE PROHIBITED FORM (C-31).

The co-location logic mirrors C-26/C-27 exactly:
- C-26: anchor must be produced at Phase 1 (the declaration point)
- C-27: prohibition for omitting the Phase 1 anchor must be co-located at Phase 1
- C-30: stale-anchor integration rule must appear at Phase 6 (the synthesis point)
- C-31: prohibited form for treating the Phase 3 update as sufficient must be co-located at Phase 3 (the update point)

Without C-31, a response can pass C-30 (Phase 6 correctly names the stale-anchor failure mode) while leaving the Phase 3 CONDITIONAL BRANCH with only a positive instruction -- "carry the updated step to Phase 6" -- which a model may interpret as: the update record at Phase 3 is the terminal requirement. The prohibited form at Phase 3 names explicitly that the update record there is not sufficient. This is the same mechanism by which C-22 closes the C-20 escape hatch, C-24 closes the C-18 escape hatch, and C-27 closes the C-26 escape hatch: positive rules are not self-enforcing; the escape hatch must be named at the site where it would be taken.

---

**Design rationale for C-30 (carried from v9):**

C-30 closes the ceiling gap exposed by V-05's stale-anchor propagation check: when Phase 3 upgrades the preliminary anchor from Phase 1 to a higher-confidence step, Phase 6 must follow that update. V-01 through V-04 all pass C-26, C-27, C-28, and C-29 -- they produce the Phase 1 anchor, name the prohibition, frame Phase 3 as confirmation, and include a Phase 6 integrity rule. But none include a mechanism that tracks whether Phase 6 carries the Phase 3 updated step rather than the Phase 1 original. V-05 adds: (1) a Phase 6 integration rule explicitly naming the stale-anchor failure mode, and (2) `anchor_updated_from_phase1: true | false | n/a` in the ARTIFACT frontmatter. C-30 captures this propagation-tracking requirement as an explicit criterion.

The distinction from C-26, C-28, C-29, C-31, C-32, C-33, and C-34:
- C-26: Phase 1 produces the preliminary anchor at the declaration point
- C-28: Phase 3 acknowledges the Phase 1 anchor as prior record and frames its work as confirmation/extension
- C-29: Phase 6 names the C-26 integrity rule (first-appearance-at-synthesis failure mode)
- C-30: Phase 6 carries the Phase 3 updated step (not Phase 1 verbatim) when Phase 3 upgraded the anchor
- C-31: Phase 3 names that its update record does not close the Phase 6 propagation requirement
- C-32: Phase 6 names the C-31 structural requirement (Phase 3 must carry the prohibited form)
- C-33: ARTIFACT field tracks Phase 3 prohibited form status machine-readably
- C-34: ARTIFACT field tracks Phase 1 prohibition status machine-readably

A response can pass C-26, C-27, C-28, and C-29 while failing C-30: all cross-phase integrity rules are named, Phase 1 and Phase 3 are correctly sequenced, but Phase 6 silently carries the Phase 1 step when Phase 3 upgraded it. A response can pass C-30 while failing C-31: Phase 6 names the stale-anchor failure mode, but Phase 3 never names that its own update record is insufficient to satisfy Phase 6. A response can pass C-31 while failing C-32: Phase 3 carries the prohibited form, but Phase 6 never names that C-31 structural requirement at synthesis. A response can pass C-30 while failing C-33: anchor provenance ARTIFACT field present, but Phase 3 co-location status field absent. A response can pass C-27 while failing C-34: Phase 1 prohibition phrase present in response text, but `phase1_anchor_prohibition_stated` ARTIFACT field absent.

---

**Design rationale for C-27/C-28/C-29 (updated in v9):**

- **C-27** closes the ceiling gap exposed by V-01 C-26 PARTIAL in v7: V-01 had the Phase 1 sub-step structure and correct anchor sequence but no PROHIBITED FORM at Phase 1 -- C-26 was structurally satisfied (anchor in Phase 1) but the escape hatch was not closed by name at the production point. R8 confirmed the phrase is the load-bearing element, not the block label: V-01 in R8 used an inline parenthetical and passed C-27. The block label is optional presentation; "does not pass" at Phase 1 is mandatory substance.

- **C-28** closes the ceiling gap exposed by the Phase 3 origination vs confirmation distinction: when C-26 is satisfied (Phase 1 produces the anchor), Phase 3 should not re-originate the anchor as if it had never appeared. R8 confirmed the exact boundary: "confirm and extend the preliminary anchor from Phase 1" (instruction-to-confirm without prior-record acknowledgment) does not pass; "a PRELIMINARY ANCHOR is already on record from Phase 1 SUB-STEP 2 -- this branch confirms and extends it" (prior-record acknowledgment + confirmation framing) passes. The "already on record" phrase or equivalent is the load-bearing element.

- **C-29** closes the ceiling gap exposed by V-05's third enforcement site in v7: V-05 added a Phase 6 integration rule naming C-26 explicitly at synthesis. R8 confirmed the minimum bar: a single integration rules list bullet satisfies C-29 -- a second site (Falsification field description annotation) is additional depth, not a requirement. Any Phase 6 position is sufficient.

---

**Design rationale for C-26 (carried from v7):**

C-26 closes the ceiling gap revealed by the R6 co-location pattern: V-03 restructured Phase 1 into MECHANISM READINESS + PRELIMINARY ANCHOR, requiring PATHWAY INCOMPLETE to be immediately followed by a step-anchored preliminary anchor before tracing continues. Phase 3 becomes a confirmation-and-extension step rather than the origination point for falsification. This pattern was absent from all prior variations -- R5 V-05 (the base) produces the anchor only in Phase 3. C-26 captures this structural proximity requirement as an explicit criterion.

The distinction from C-18 and C-24: C-18 requires the anchor to exist in the falsification phase. C-24 requires the deferral prohibition to be named. C-26 requires the anchor to be produced at the declaration point in Phase 1. A response can pass both C-18 and C-24 (valid anchor in Phase 3, deferral explicitly prohibited) while failing C-26 (no preliminary anchor in Phase 1). V-03 demonstrates the pass path: Phase 1 produces the preliminary anchor co-located with "deferring or omitting this preliminary anchor does not pass," Phase 3 extends it.

---

**Design rationale for C-24/C-25 (carried from v6):**

- **C-24** closes the ceiling gap exposed by V-02 C-18 PARTIAL: V-02 structurally enforces step-anchored falsification by requiring a step anchor in all output formats -- this passes C-18 but not C-24, because the structural requirement never names "deferral does not pass" as an explicit failure mode. A model seeing only the structural requirement constructs a format that looks compliant while leaving the deferral mental model intact. Naming the deferral form as prohibited is the mechanism by which models learn to close it. This mirrors exactly how C-22 closes C-20 escape hatch.

- **C-25** closes the ceiling gap exposed by V-02 AMEND structure: V-02 has an aggregate evidence tier in AMEND but no evidence gap field -- the gap is inferable from CONTEXT EVIDENCE but never promoted to a named AMEND entry. C-25 requires the promotion explicitly, parallel to C-23 requirement that mechanism completeness appear as a named AMEND field rather than embedded in the amended clause. Both criteria enforce the same principle: analytical outputs produced earlier in the response must propagate into AMEND as named fields, not be left behind in their source section.

---

**Design rationale for C-21/C-22/C-23 (carried from v5):**

- **C-21** closes the ceiling gap exposed by the R4 null-gap pattern: V-04 passed C-19 by naming two separate fields and including the counterexample, but the criterion as stated did not explicitly require the counterexample -- only that two fields be present. C-21 makes the null-gap demonstration the explicit bar, because without it a response can name two fields while still conflating them when gap is empty.
- **C-22** closes the ceiling gap exposed by V-01 and V-03: both failed C-20 by using the conditional form, which they constructed believing they were compliant. The positive unconditional rule is not enough -- naming the escape hatch as a failure mode is the mechanism by which models learn to avoid it.
- **C-23** closes the ceiling gap exposed by V-04 C-15 partial: V-04 had strong AMEND structure (evidence gap, evidence tier, inertia, confounder all as named fields) but embedded mechanism completeness in the amended clause text rather than as a named AMEND field. The C-15 criterion requires all four fields; C-23 requires mechanism completeness specifically to be a standalone named entry, which is the form V-05 uses and V-04 omits.

---

## Scoring Guide

| Range | Interpretation |
|-------|---------------|
| All essential pass + >= 210 | Golden -- meets bar for production use |
| All essential pass + 195-209 | Acceptable -- useful but shallow on aspirational |
| All essential pass + 180-194 | Passing -- essential + recommended coverage only |
| Any essential fail | Below bar -- output is unreliable regardless of score |
| < 180 | Below bar |

**Maximum: 220 pts** (60 essential + 30 recommended + 130 aspirational)

**Note on C-18 gradeability:** C-18 is only scored when both C-11 (incompleteness acknowledged) and C-12 (falsification step-anchored) pass. If the pathway is complete and C-11 does not trigger, C-18 is marked N/A and excluded from the denominator. Scorecards should document this explicitly.

**Note on C-23 gradeability:** C-23 requires C-15 PASS. If C-15 fails, C-23 is not scored. C-23 represents the strictest interpretation of the mechanism completeness requirement within C-15.

**Note on C-24 gradeability:** C-24 requires C-18 PASS. If C-18 is N/A (complete pathway) or FAIL, C-24 is not scored. C-24 captures the strictest form of the deferral-prohibition requirement that C-18 structurally enforces.

**Note on C-25 gradeability:** C-25 requires C-19 PASS. If C-19 fails, C-25 is not scored. C-25 captures the strictest integration requirement for evidence gap -- field present in CONTEXT EVIDENCE and promoted to AMEND.

**Note on C-26 gradeability:** C-26 requires C-11 PASS and C-18 PASS. If C-11 does not trigger (complete pathway) or C-18 fails, C-26 is not scored. C-26 captures the strictest structural form of the falsification anchor requirement -- anchor present in Phase 3 (C-18) is necessary but not sufficient; the anchor must also be co-located with the Phase 1 incompleteness declaration.

**Note on C-27 gradeability:** C-27 requires C-26 PASS. If C-26 is N/A or FAIL, C-27 is not scored. C-27 captures the strictest form of the Phase 1 anchor requirement -- anchor present at Phase 1 (C-26) is necessary but not sufficient; the prohibition for omitting that anchor must also be named at Phase 1 (inline phrase or block, any position at Phase 1).

**Note on C-28 gradeability:** C-28 requires C-26 PASS. If C-26 is N/A or FAIL, C-28 is not scored (no Phase 1 anchor exists to be referenced by Phase 3). C-28 captures the confirmation-framing requirement that follows from C-26: once the Phase 1 anchor exists, Phase 3 must acknowledge it as prior record with explicit prior-record language ("already on record" or equivalent).

**Note on C-29 gradeability:** C-29 requires C-26 PASS. If C-26 is N/A or FAIL, C-29 is not scored. C-29 captures the synthesis-phase integrity check -- the third enforcement site that tests the cross-phase structural requirement at the AMEND point. Any Phase 6 position (integration rules list, field description annotation, or other) satisfies the criterion.

**Note on C-30 gradeability:** C-30 requires C-26 PASS and C-28 PASS. If C-26 is N/A or FAIL (no Phase 1 preliminary anchor), C-30 is not scored. If C-28 FAIL (Phase 3 does not acknowledge the Phase 1 anchor as prior record), C-30 is not scored -- the Phase 3 update path is not established. If Phase 3 confirms the anchor verbatim without updating to a higher-confidence step, C-30 is N/A. C-30 captures the propagation requirement: when Phase 3 upgrades the anchor, Phase 6 must carry the upgraded step.

**Note on C-31 gradeability:** C-31 requires C-30 PASS. If C-30 is N/A (Phase 3 confirms verbatim, no update) or FAIL, C-31 is not scored -- there is no Phase 3 anchor update established, so the Phase 3 prohibited form has no referent. C-31 captures the dual-site enforcement requirement: C-30 places the stale-anchor check at Phase 6 (synthesis point); C-31 places the prohibited form at Phase 3 (update point). A response must satisfy C-30 before C-31 is meaningful.

**Note on C-32 gradeability:** C-32 requires C-31 PASS. If C-31 is N/A (Phase 3 confirms verbatim) or FAIL, C-32 is not scored -- there is no Phase 3 prohibited form in place for Phase 6 to name. C-32 captures the synthesis-phase naming requirement for the C-31 structural requirement, parallel to how C-29 captures the synthesis-phase naming requirement for the C-26 structural requirement. Any Phase 6 position satisfies the criterion.

**Note on C-33 gradeability:** C-33 requires C-30 PASS. If C-30 is N/A (Phase 3 confirms verbatim, no update) or FAIL, C-33 is not scored -- the same N/A condition as C-30 and C-31. Unlike C-32 (which requires C-31 PASS), C-33 is gradeable even when C-31 FAIL: a response that passes C-30 but fails C-31 should include `phase3_anchor_update_prohibited_form: false` in the ARTIFACT -- the field is gradeable and absence of the field fails C-33 regardless of whether C-31 passed.

**Note on C-34 gradeability:** C-34 requires C-26 PASS. If C-26 is N/A (complete pathway, incompleteness not declared) or FAIL, C-34 is not scored -- the same N/A condition as C-26 and C-27. Unlike C-27 (which also requires C-26 PASS), C-34 is gradeable even when C-27 FAIL: a response that passes C-26 but fails C-27 should include `phase1_anchor_prohibition_stated: false` in the ARTIFACT -- the field is gradeable and absence of the field fails C-34 regardless of whether C-27 passed. Presence with `false` (C-27 fail, correct audit) is the passing state for C-34; absence of the field is the failing state.

---

## Common Failure Modes

- **C-01 fail**: Output confirms the claim ("yes, X causes Y") without tracing the mechanism
- **C-02 fail**: Falsification is stated as a metric threshold ("if retention does not go up") rather than a mechanism break
- **C-03 fail**: Inertia check skipped entirely -- most common failure per skill description
- **C-04 fail**: AMEND section restates the original hypothesis or broadens instead of narrows
- **C-05 fail**: Evidence section is generic ("studies show...") without reference to the team actual context
- **C-07 fail** (common): Inertia check surfaces status-quo alternative but no independent confounders named -- easy to satisfy C-03 while missing C-07 entirely
- **C-11 fail**: Model fabricates 3 weak steps to avoid appearing incomplete instead of flagging the gap
- **C-14 fail**: AMEND narrows the claim but does not incorporate what the inertia check found -- the two outputs are not integrated
- **C-15 fail**: AMEND synthesizes some phases but silently drops others -- e.g., narrowed claim incorporates evidence tier but ignores the inertia verdict or confounder finding
- **C-16 fail**: Steps are listed as prose bullets or numbered without names -- "1. User sees the feature" does not give falsification a stable referent to anchor to
- **C-17 fail**: Confounder section names only "the feature is not needed because the status quo already does this" -- that is the inertia case restated, not an independent alternative cause
- **C-18 fail**: Response declares incompleteness in C-11 and then offers a metric-threshold falsification or defers ("cannot falsify until mechanism is clearer") instead of anchoring to the best-traced step
- **C-19 fail**: AMEND has a single combined evidence entry that lists gap steps and assigns a tier in the same field -- or lists gap steps but omits the aggregate tier entirely, or states an aggregate tier without naming which steps are gaps
- **C-20 fail**: Amended claim conditions inertia incorporation on the verdict value -- e.g., scopes to contexts where status quo does not already produce Y only if Competing or Unclear -- leaving Not-competing cases where the inertia finding is silently dropped
- **C-21 fail**: Response names evidence gap and evidence tier as separate fields but does not include the null-gap counterexample -- without demonstrating "gap: none, tier: T1" as a valid state, the field distinction is asserted but not proven concrete
- **C-22 fail**: Response states the unconditional inertia rule positively ("inertia is always incorporated") but does not name "conditioning on Competing or Unclear does not pass" -- models seeing only the positive rule produce the conditional form and believe they comply
- **C-23 fail**: Mechanism completeness appears as a qualifier within the amended clause text ("X causes Y when the mechanism is fully traceable") rather than as a named standalone AMEND field -- the information is present but not in the required named-field form
- **C-24 fail**: Response structurally requires a step anchor in all falsification formats (preventing deferral mechanically) but never names "declaring incompleteness and deferring step-level falsification does not pass" -- the prohibited form exists in the model output space and is not closed by structural constraint alone
- **C-25 fail**: Evidence gap appears as a named output in CONTEXT EVIDENCE (satisfying C-13 and C-19) but does not propagate into AMEND as a standalone named field -- evidence tier is present in AMEND, evidence gap is not -- the gap field is left behind in its source section rather than promoted to the synthesis point
- **C-26 fail**: Response declares PATHWAY INCOMPLETE in Phase 1 and produces a valid step-anchored break in Phase 3 (passing C-18), but Phase 1 contains no preliminary anchor -- the anchor appears only at the falsification phase, not at the moment of declaration. The structural proximity requirement is unmet even though the anchor eventually exists.
- **C-27 fail**: Response includes the Phase 1 anchor requirement and produces the anchor at Phase 1 (satisfying C-26) but includes no "does not pass" language at Phase 1 -- neither inline in the sub-step header nor in a labeled block. Structural sequence present; prohibition phrase absent. Note: the block label alone without the phrase also fails; the phrase alone without the block label passes.
- **C-28 fail**: Response declares PATHWAY INCOMPLETE in Phase 1, produces a preliminary anchor at Phase 1 (satisfying C-26), but Phase 3 either (a) re-originates the anchor without referencing Phase 1 at all, or (b) uses instruction-to-confirm framing ("confirm and extend the preliminary anchor from Phase 1") without explicit prior-record acknowledgment ("already on record from Phase 1 SUB-STEP 2" or equivalent). The prior-record phrase is the load-bearing element -- its absence leaves the re-origination pattern open.
- **C-29 fail**: Response satisfies C-26, C-27, and C-28 but includes no synthesis-phase integration rule that detects C-26 violation at AMEND -- the cross-phase integrity check is absent from the point where all analytical outputs converge. A Falsification field that first appears at synthesis without a Phase 1 anchor would not be flagged.
- **C-30 fail**: Response satisfies C-26, C-27, C-28, and C-29 -- Phase 1 anchor exists, prohibition named, Phase 3 confirms with prior-record acknowledgment, Phase 6 integrity rule present -- but Phase 6 Falsification still carries the Phase 1 preliminary anchor step verbatim even though Phase 3 upgraded the anchor to a higher-confidence step. The stale-anchor propagation failure is invisible to all prior enforcement sites; only C-30 detects it. Absence of `anchor_updated_from_phase1` ARTIFACT field when Phase 3 performed an update also fails.
- **C-31 fail**: Response satisfies C-30 -- Phase 6 names the stale-anchor failure mode, integration rule present, ARTIFACT field present -- but Phase 3 CONDITIONAL BRANCH carries only a positive update instruction ("record the updated BEST-TRACEABLE ANCHOR and carry it to Phase 6") without naming that correctly recording the update at Phase 3 does not close the Phase 6 propagation requirement. The dual-site enforcement is broken: Phase 6 names the failure mode; Phase 3 does not name that its own update record is insufficient to satisfy Phase 6. A model reading the Phase 3 branch sees a positive instruction and may treat the Phase 3 update record as the terminal requirement.
- **C-32 fail**: Response satisfies C-31 -- Phase 3 CONDITIONAL BRANCH carries the self-referential prohibited form -- but Phase 6 integration rules include no statement naming the C-31 structural requirement. The Phase 3 co-location requirement is met at Phase 3 but never validated or named at the synthesis point. A response where Phase 6 integration rules name only the C-26 cross-phase integrity rule (C-29) and the stale-anchor failure mode (C-30) without also naming the C-31 Phase 3 co-location requirement does not pass.
- **C-33 fail**: Response satisfies C-30 -- `anchor_updated_from_phase1: true | false | n/a` ARTIFACT field present -- but ARTIFACT frontmatter does not include `phase3_anchor_update_prohibited_form: true | false | n/a`. The anchor provenance is machine-readable; the Phase 3 co-location status is not. Note: a response that fails C-31 (prohibited form absent at Phase 3) but correctly includes `phase3_anchor_update_prohibited_form: false` passes C-33 -- the field is present and accurately reflects the C-31 fail state. Only absence of the field fails C-33.
- **C-34 fail**: Response satisfies C-27 -- Phase 1 carries the "does not pass" prohibition phrase -- but ARTIFACT frontmatter does not include `phase1_anchor_prohibition_stated: true | false | n/a`. The Phase 1 prohibition behavior is observable in the response text; the machine-readable ARTIFACT record is absent. Note: a response that fails C-27 (prohibition phrase absent at Phase 1) but correctly includes `phase1_anchor_prohibition_stated: false` passes C-34 -- the field is present and accurately reflects the C-27 fail state. Only absence of the field fails C-34. The two failure modes are: (a) C-27 FAIL + field absent -- behavioral failure with missing audit (C-34 FAIL); (b) C-27 FAIL + field `false` -- behavioral failure with correct audit (C-34 PASS).
