Written. Here is the summary of what changed:

---

## What changed: v6 -> v7

**1 new aspirational criterion: C-26**

| Signal | Pattern | Criterion |
|--------|---------|-----------|
| V-03 achieves C-24 via Phase 1 co-location | When PATHWAY INCOMPLETE is declared, V-03 immediately produces a PRELIMINARY ANCHOR at Phase 1 before any further tracing -- Phase 3 extends/confirms it. All prior variations (including R5 V-05 base) produce the anchor only at Phase 3. | **C-26: Falsification anchor co-located with incompleteness declaration** -- the anchor must appear at the moment of declaration, not at the downstream falsification phase. |

**C-26 gradeability chain:** requires C-11 PASS + C-18 PASS. Does not trigger for complete pathways.

**Distinction from existing criteria:**
- C-18: anchor exists (anywhere)
- C-24: deferral form named as prohibited
- C-26: anchor produced at Phase 1 declaration point -- structural proximity

A response can pass C-18 and C-24 while failing C-26 (anchor in Phase 3, no preliminary anchor in Phase 1).

**Scoring update:**
- Aspirational: 85 → 90 pts (18 criteria x 5 pts)
- Total: 175 → **180 pts**
- Golden **>= 175** | Acceptable **160-174** | Passing **145-159**
- Previous ceiling (175) = new Golden floor
ge appears where incompleteness is produced, not only in a downstream PROHIBITED FORM block. This is an alternative C-24 satisfaction path, not a C-24 replacement.

**Scoring:**
- Aspirational: 85 -> 90 pts (18 criteria x 5 pts)
- Grand total: 175 -> **180 pts**
- Golden **>= 175** | Acceptable **160-174** | Passing **145-159**
- Previous ceiling (175) becomes new Golden floor, same pattern as every prior version

**C-26 relationship to C-18/C-24:**
- C-26 does not replace C-18 -- it adds the co-location requirement on top of C-18 anchor-existence requirement.
- C-26 does not replace C-24 -- C-24 requires naming the deferral prohibition explicitly; C-26 requires the anchor to be produced at the declaration point. Both can be satisfied independently. V-03 achieves C-24 through co-location; a response could achieve C-24 via a Phase 3 PROHIBITED FORM block while failing C-26 (no Phase 1 preliminary anchor).

---

## Criteria summary

| Tier | IDs | Pts |
|------|-----|-----|
| Essential | C-01 through C-05 | 60 |
| Recommended | C-06 through C-08 | 30 |
| Aspirational | C-09 through C-26 | 90 |

**C-21/C-22/C-23/C-24/C-25/C-26 relationship to earlier criteria:** These six criteria do not replace C-12, C-15, C-18, C-19, C-20, or C-24 -- they capture the stricter pass conditions those criteria require at full depth. A response can pass C-18 at full credit while failing C-24 (structural enforcement without named prohibition) or failing C-26 (anchor present in Phase 3 but not co-located with Phase 1 declaration). A response can pass C-24 while failing C-26 (deferral named as prohibited in Phase 3, but no preliminary anchor in Phase 1).

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

## Aspirational Criteria (90 pts total)

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

---

**Design rationale for C-26:**

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
| All essential pass + >= 175 | Golden -- meets bar for production use |
| All essential pass + 160-174 | Acceptable -- useful but shallow on aspirational |
| All essential pass + 145-159 | Passing -- essential + recommended coverage only |
| Any essential fail | Below bar -- output is unreliable regardless of score |
| < 145 | Below bar |

**Maximum: 180 pts** (60 essential + 30 recommended + 90 aspirational)

**Note on C-18 gradeability:** C-18 is only scored when both C-11 (incompleteness acknowledged) and C-12 (falsification step-anchored) pass. If the pathway is complete and C-11 does not trigger, C-18 is marked N/A and excluded from the denominator. Scorecards should document this explicitly.

**Note on C-23 gradeability:** C-23 requires C-15 PASS. If C-15 fails, C-23 is not scored. C-23 represents the strictest interpretation of the mechanism completeness requirement within C-15.

**Note on C-24 gradeability:** C-24 requires C-18 PASS. If C-18 is N/A (complete pathway) or FAIL, C-24 is not scored. C-24 captures the strictest form of the deferral-prohibition requirement that C-18 structurally enforces.

**Note on C-25 gradeability:** C-25 requires C-19 PASS. If C-19 fails, C-25 is not scored. C-25 captures the strictest integration requirement for evidence gap -- field present in CONTEXT EVIDENCE and promoted to AMEND.

**Note on C-26 gradeability:** C-26 requires C-11 PASS and C-18 PASS. If C-11 does not trigger (complete pathway) or C-18 fails, C-26 is not scored. C-26 captures the strictest structural form of the falsification anchor requirement -- anchor present in Phase 3 (C-18) is necessary but not sufficient; the anchor must also be co-located with the Phase 1 incompleteness declaration.

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
