## discover-causal R4 Scorecard

**Rankings (v4 rubric, 150 pts max):**

| Rank | Variation | Score | Interpretation |
|------|-----------|-------|----------------|
| 1 | V-05: Full v4 aspirational stack | **150/150** | Golden — ceiling |
| 2 | V-04: Evidence separation + unconditional inertia | **140/150** | Golden |
| 3 | V-01: Evidence field separation | **135/150** | Acceptable |
| 3 | V-02: Unconditional inertia incorporation | **135/150** | Acceptable |
| 5 | V-03: Inertia verdict as load-bearing anchor | **130/150** | Acceptable |

**Key scoring decisions:**

- V-01 C-19 PASS, C-20 FAIL (conditional form preserved by design), C-14/C-15 PARTIAL (Not-competing escape hatch in Amended clause)
- V-02 C-20 PASS, C-19 FAIL (no evidence gap field), C-13/C-18 PARTIAL (no explicit gap enumeration, no CONDITIONAL BRANCH)
- V-03 C-20 PASS, C-15 FAIL (mechanism completeness + evidence tier both absent from AMEND — 2/4 required fields), C-19 FAIL
- V-04 achieves Golden: C-19 PASS + C-20 PASS. C-15 PARTIAL (mechanism completeness not a named AMEND field despite having all other fields), C-18 PARTIAL (no CONDITIONAL BRANCH in FALSIFICATION)
- V-05 ceiling: C-10 from Phase 2 secondary pathway probe, C-18 from Phase 3 CONDITIONAL BRANCH, C-15 from mechanism completeness as named Phase 6 AMEND field

**3 new patterns:**

1. **Null-gap counterexample is load-bearing** — naming two fields is insufficient; the "all T1, gap: none, tier: T1" example is what makes orthogonality concrete and prevents the category error
2. **Prohibited form must be named by form** — "conditioning on Competing or Unclear does not pass" closes the escape hatch; without naming it explicitly, models produce the conditional form and believe they comply
3. **Mechanism completeness requires a named AMEND field** — the mechanism qualifier in the Amended clause does not substitute; V-04 demonstrates this by failing C-15 despite closing C-19 and C-20

```json
{"top_score": 150, "all_essential_pass": true, "new_patterns": ["null-gap counterexample is the load-bearing element of the C-19 fix: naming two fields is not enough -- showing 'a pathway with all T1 evidence has gap: none but tier: T1' makes orthogonality concrete and prevents the category error", "three-case mandatory inertia table requires the prohibited form named explicitly ('conditioning on Competing or Unclear does not pass') -- without naming the escape hatch as a failure mode, models produce the conditional form and believe they comply", "mechanism completeness must be a separate named AMEND field for C-15 full pass: the mechanism qualifier in the Amended clause does not substitute -- V-04 has strong AMEND structure but omits this field and PARTIAL on C-15 despite closing C-19 and C-20"]}
```
50** — Phase structure carries all seven named AMEND fields (including mechanism completeness), Phase 3 CONDITIONAL BRANCH for C-18, Phase 2 multiple pathway probe for C-10, Phase 4 FIELD INDEPENDENCE NOTE for C-19, Phase 6 three-case unconditional inertia with named prohibited form for C-20.
- **C-18 gradeability:** All five have C-11 PASS + C-12 PASS, so C-18 is scored for all.

**3 new patterns:**

1. Null-gap counterexample is the load-bearing element of the C-19 fix — naming two fields is insufficient; showing "a pathway with all T1 evidence has gap: 'none' but still carries tier: T1" is what prevents the category error by making the orthogonality concrete
2. Three-case mandatory inertia table requires the prohibited form to be named explicitly ("conditioning on Competing or Unclear does not pass") — without naming the escape hatch as a failure mode, models produce the conditional form and believe they comply
3. Mechanism completeness must be a separate named AMEND field for C-15 full pass — V-04 has strong AMEND structure (evidence gap + evidence tier + inertia + confounder) but omits mechanism completeness and PARTIAL on C-15; the mechanism qualifier in the Amended clause does not substitute for a named AMEND field

```json
{"top_score": 150, "all_essential_pass": true, "new_patterns": ["null-gap counterexample is the load-bearing element of the C-19 fix: naming two fields is not enough -- showing 'a pathway with all T1 evidence has gap: none but tier: T1' makes orthogonality concrete and prevents the category error", "three-case mandatory inertia table requires the prohibited form named explicitly ('conditioning on Competing or Unclear does not pass') -- without naming the escape hatch as a failure mode, models produce the conditional form and believe they comply", "mechanism completeness must be a separate named AMEND field for C-15 full pass: the mechanism qualifier in the Amended clause does not substitute -- V-04 has strong AMEND structure but omits this field and PARTIAL on C-15 despite closing C-19 and C-20"]}
```

---

## V-01: Evidence field separation

| ID | Criterion | Verdict | Pts | Evidence Note |
|----|-----------|---------|-----|---------------|
| C-01 | Mechanism traced as pathway | PASS | 12 | MECHANISM PATHWAY with "Step N -- [Name]: What changes. Who acts. Observable indicator." + READINESS GATE before tracing. |
| C-02 | Falsification is mechanism break | PASS | 12 | Required format: "The mechanism fails if Step [N] -- [Name] -- does not occur." CONDITIONAL BRANCH prohibits metric thresholds and deferral; enforces BEST-TRACEABLE ANCHOR for incomplete pathways. |
| C-03 | Inertia check performed | PASS | 12 | INERTIA CHECK section with INERTIA VERDICT: [Competing / Not competing / Unclear -- one sentence basis]. |
| C-04 | Causal claim narrowed in AMEND | PASS | 12 | AMEND section with narrowing requirement. |
| C-05 | Context evidence assessed | PASS | 12 | CONTEXT EVIDENCE with per-step T1/T2/T3 rating + FIELD SEPARATION NOTE producing gap steps and tier as named outputs. |
| C-06 | Mechanism pathway is testable | PASS | 10 | "Named agent and observable indicator" per step. |
| C-07 | Confounder or alternative cause | PASS | 10 | CONFOUNDER CHECK: "Name at least one cause of Y that does not involve X and is not the inertia case." |
| C-08 | AMEND output is actionable | PASS | 10 | Amended must include mechanism qualifier, scope condition. |
| C-09 | Evidence quality rated | PASS | 5 | T1/T2/T3 scale with category definitions; per-step rating; Evidence tier as separate AMEND field. |
| C-10 | Multiple causal pathways considered | FAIL | 0 | Not asked. |
| C-11 | Mechanism incompleteness acknowledged | PASS | 5 | READINESS GATE: "If no: declare incompleteness now. Write: 'PATHWAY INCOMPLETE: mechanism cannot be traced past [step].' Then continue, marking [UNCERTAIN]." + "Producing thin or vague steps to clear this gate -- instead of declaring incompleteness -- fails this section." |
| C-12 | Falsification break anchored to named step | PASS | 5 | Required format + "Step number and name must match a labeled row in the pathway above." CONDITIONAL BRANCH with BEST-TRACEABLE ANCHOR preserves step-level anchor even for incomplete pathways. |
| C-13 | Evidence gap localized to pathway steps | PASS | 5 | FIELD SEPARATION NOTE: "Evidence gap steps: [list of Step N -- [Name] labels that have no supporting evidence; write 'none' if every step has evidence]." Per-step gap enumeration structurally mandated as named output. |
| C-14 | AMEND conditioned on inertia finding | PARTIAL | 2.5 | "Inertia status:" is a named AMEND field (always documented). However Amended clause says "inertia condition if Competing or Unclear" -- Not-competing cases receive no inertia incorporation in the amended text. |
| C-15 | AMEND synthesizes all phase outputs | PARTIAL | 2.5 | AMEND has all four required fields as named entries (Mechanism complete, Inertia status, Evidence tier, Confounder finding). However the Amended clause incorporates inertia conditionally ("if Competing or Unclear"), so not all four are unconditionally reflected in the amended claim text. |
| C-16 | Pathway steps formally labeled | PASS | 5 | "Step N -- [Name]: What changes. Who acts. Observable indicator." format required throughout. Falsification references by label. |
| C-17 | Confounder explicitly distinguished from inertia | PASS | 5 | CONFOUNDER CHECK: "does not involve X and is not the inertia case." Explicit exclusion language separates the two analytical questions. |
| C-18 | Incomplete pathway still anchors falsification | PASS | 5 | CONDITIONAL BRANCH: named prohibited forms ("Cannot falsify until the mechanism is better understood", "Falsification is deferred", "If outcome Y does not improve") + mandatory BEST-TRACEABLE ANCHOR format + "Declaring incompleteness changes the confidence annotation and adds a note, but does not exempt this section from producing a step-level anchor." |
| C-19 | AMEND evidence gap and evidence tier are separate fields | PASS | 5 | Design purpose. FIELD SEPARATION NOTE: explicit orthogonality statement, null-gap counterexample ("a pathway where all steps have T1 evidence has no gap steps ('none') but still carries evidence tier T1"), "Do not merge them. Do not omit either." Both fields appear as separate named AMEND entries. |
| C-20 | AMEND inertia incorporation is unconditional | FAIL | 0 | Amended clause: "inertia condition if Competing or Unclear." Conditional form intentionally preserved for single-axis isolation. Not-competing cases have no inertia incorporation in amended claim text. |
| **Total** | | | **135** | All essential: PASS |

---

## V-02: Unconditional inertia incorporation

| ID | Criterion | Verdict | Pts | Evidence Note |
|----|-----------|---------|-----|---------------|
| C-01 | Mechanism traced as pathway | PASS | 12 | MECHANISM PATHWAY: "Label each step with a number and short name. Format: Step N -- [Name]: What changes. Who acts. Observable indicator." Minimum 3 steps. |
| C-02 | Falsification is mechanism break | PASS | 12 | Required format: "The mechanism fails if Step [N] -- [Name] -- does not occur." Step number and name must match labeled row. |
| C-03 | Inertia check performed | PASS | 12 | INERTIA CHECK with INERTIA VERDICT + INERTIA COMMITMENT paragraph. |
| C-04 | Causal claim narrowed in AMEND | PASS | 12 | AMEND Required structure with Amended clause + integration rules prohibiting restating and broadening. |
| C-05 | Context evidence assessed | PASS | 12 | CONTEXT EVIDENCE: "Name each piece, rate it, and name which pathway step it supports." Aggregate evidence tier required. |
| C-06 | Mechanism pathway is testable | PASS | 10 | Observable indicator per labeled step. |
| C-07 | Confounder or alternative cause | PASS | 10 | ALTERNATIVE CAUSES section: requires (1) alternative causal pathway not through mechanism, (2) confounding variable. Both required; silence not acceptable. |
| C-08 | AMEND output is actionable | PASS | 10 | Amended clause specifies mechanism qualifier, scope condition, inertia verdict incorporation for all three cases. |
| C-09 | Evidence quality rated | PASS | 5 | T1/T2/T3 scale with definitions. "Aggregate evidence tier: [highest available across all steps]" as required output. |
| C-10 | Multiple causal pathways considered | FAIL | 0 | Not asked. |
| C-11 | Mechanism incompleteness acknowledged | PASS | 5 | "If you cannot trace 3 observable steps with current knowledge, say so explicitly ('mechanism not fully traceable at step N') rather than generating thin steps." |
| C-12 | Falsification break anchored to named step | PASS | 5 | Required format + step number and name must match labeled row. Labeled step format instructed throughout. |
| C-13 | Evidence gap localized to pathway steps | PARTIAL | 2.5 | Per-piece evidence names which pathway step it supports. However, no required "Evidence gap steps:" output -- which specific steps lack evidence is inferable but not mandated as a named output field. |
| C-14 | AMEND conditioned on inertia finding | PASS | 5 | Three-case mandatory table in Amended clause covers all three verdict values. INERTIA COMMITMENT: "This verdict is not conditional. It must explicitly shape the amended claim regardless of which verdict value applies." Integration rule: "Conditioning inertia incorporation on the verdict being Competing or Unclear does not pass." |
| C-15 | AMEND synthesizes all phase outputs | PASS | 5 | Required structure: Original, Inertia verdict, Mechanism completeness, Evidence tier, Confounder finding, Falsification, Amended. All four C-15 required fields present. Amended "incorporates all four prior findings, including the inertia verdict unconditionally." Integration rule: "A narrowed claim that ignores any of the four named fields does not pass." |
| C-16 | Pathway steps formally labeled | PASS | 5 | "Label each step with a number and short name. Format: Step N -- [Name]:" instructed. Falsification must reference labeled row. |
| C-17 | Confounder explicitly distinguished from inertia | PASS | 5 | ALTERNATIVE CAUSES: "This is NOT the inertia check. The inertia check asks whether the status quo trends toward Y over time without any intervention. This section asks: what independently operating causes, present right now, could produce Y coincidentally with X being deployed?" Explicit distinction with mechanistic separation. |
| C-18 | Incomplete pathway still anchors falsification | PARTIAL | 2.5 | No CONDITIONAL BRANCH in FALSIFICATION CONDITION. The required format always demands a named step anchor, which structurally enforces C-18 -- but no explicit prohibition on deferral forms ("cannot falsify until...") and no BEST-TRACEABLE ANCHOR format for incomplete pathways. |
| C-19 | AMEND evidence gap and evidence tier are separate fields | FAIL | 0 | CONTEXT EVIDENCE produces aggregate evidence tier but no "Evidence gap steps:" named output. AMEND Required structure has Evidence tier but no Evidence gap field. Category error not addressed. |
| C-20 | AMEND inertia incorporation is unconditional | PASS | 5 | Design purpose. INERTIA COMMITMENT paragraph + three-case mandatory table (Competing / Not competing / Unclear) in Amended clause + explicit integration rule: "Conditioning inertia incorporation on the verdict being Competing or Unclear does not pass -- all three verdict values require explicit incorporation in the amended claim." |
| **Total** | | | **135** | All essential: PASS |

---

## V-03: Inertia verdict as load-bearing anchor

| ID | Criterion | Verdict | Pts | Evidence Note |
|----|-----------|---------|-----|---------------|
| C-01 | Mechanism traced as pathway | PASS | 12 | MECHANISM PATHWAY with "Step N -- [Name]: What changes. Who acts. Observable indicator." + incompleteness declaration instruction. |
| C-02 | Falsification is mechanism break | PASS | 12 | Required format: "The mechanism fails if Step [N] -- [Name] -- does not occur." Must match labeled row. |
| C-03 | Inertia check performed | PASS | 12 | INERTIA CHECK with INERTIA VERDICT + CARRY-FORWARD block covering all three verdict values. |
| C-04 | Causal claim narrowed in AMEND | PASS | 12 | AMEND section with narrowing requirement and CARRY-FORWARD activation for all three inertia verdict values. |
| C-05 | Context evidence assessed | PASS | 12 | CONTEXT EVIDENCE: "Name each piece specifically. Rate each: T1/T2/T3. Note which pathway step each piece supports." |
| C-06 | Mechanism pathway is testable | PASS | 10 | Observable indicator per labeled step. |
| C-07 | Confounder or alternative cause | PASS | 10 | CONFOUNDER CHECK: four confounder types listed; "Name at least one. If none can be identified, explain why." |
| C-08 | AMEND output is actionable | PASS | 10 | Amended requires (a) mechanism qualifier, (b) scope condition, (c) inertia incorporation for all three cases, (d) confounder note. |
| C-09 | Evidence quality rated | PASS | 5 | T1/T2/T3 per-piece rating required. Per-piece rating satisfies distinction between evidence types. |
| C-10 | Multiple causal pathways considered | FAIL | 0 | Not asked. |
| C-11 | Mechanism incompleteness acknowledged | PASS | 5 | "If fewer can be traced with confidence, say so explicitly rather than generating thin steps to fill the count." |
| C-12 | Falsification break anchored to named step | PASS | 5 | Required format; must match labeled row. Labeled step format instructed. |
| C-13 | Evidence gap localized to pathway steps | PARTIAL | 2.5 | "Note which pathway step each piece supports." Per-piece evidence localized to steps but no required explicit "Evidence gap steps:" enumeration. Gap is inferable, not mandated. |
| C-14 | AMEND conditioned on inertia finding | PASS | 5 | CARRY-FORWARD covers all three cases with specific required language. AMEND (c) activates CARRY-FORWARD unconditionally: "required regardless of verdict value." |
| C-15 | AMEND synthesizes all phase outputs | FAIL | 0 | AMEND structure: Original, Inertia verdict, Confounder finding, Pathway, Falsification, Amended. Missing: Mechanism completeness and Evidence tier as named fields. Two of four required C-15 fields absent. |
| C-16 | Pathway steps formally labeled | PASS | 5 | "Step N -- [Name]: What changes. Who acts. Observable indicator." instructed. Falsification references labeled step. |
| C-17 | Confounder explicitly distinguished from inertia | PASS | 5 | CONFOUNDER CHECK: "This section asks a DIFFERENT question from the inertia check above." + "The inertia case is EXCLUDED from this analysis." + Required output: "Explicitly state: 'The inertia case (INERTIA VERDICT: [verdict]) is NOT included here as a confounder -- it was addressed in the Inertia Check section.'" Strongest C-17 structural enforcement in R4. |
| C-18 | Incomplete pathway still anchors falsification | PARTIAL | 2.5 | No CONDITIONAL BRANCH in FALSIFICATION CONDITION. The required format demands a named step anchor but no explicit prohibition on deferral or BEST-TRACEABLE ANCHOR format for the incomplete case. |
| C-19 | AMEND evidence gap and evidence tier are separate fields | FAIL | 0 | No FIELD SEPARATION NOTE. No evidence gap output in CONTEXT EVIDENCE. No evidence gap field in AMEND. Category error not addressed. |
| C-20 | AMEND inertia incorporation is unconditional | PASS | 5 | CARRY-FORWARD in INERTIA CHECK provides verdict-specific required language for all three cases. AMEND (c) says "required regardless of verdict value; activate the CARRY-FORWARD language from INERTIA CHECK appropriate to the verdict" with explicit forms for Competing, Not competing, and Unclear. |
| **Total** | | | **130** | All essential: PASS |

---

## V-04: Evidence separation + unconditional inertia

| ID | Criterion | Verdict | Pts | Evidence Note |
|----|-----------|---------|-----|---------------|
| C-01 | Mechanism traced as pathway | PASS | 12 | MECHANISM PATHWAY with STEP LABELING REQUIREMENT as structural prerequisite. "Step N -- [Name]: What changes. Who acts. Observable indicator." |
| C-02 | Falsification is mechanism break | PASS | 12 | Required format: "The mechanism fails if Step [N] -- [Name] -- does not occur." "'Step 2 fails' without the step name does not pass. A metric threshold ('if usage declines') does not pass." |
| C-03 | Inertia check performed | PASS | 12 | INERTIA CHECK with "This verdict must appear explicitly in the AMEND section below regardless of its value." |
| C-04 | Causal claim narrowed in AMEND | PASS | 12 | AMEND with integration rules: restating does not pass, broadening does not pass. |
| C-05 | Context evidence assessed | PASS | 12 | CONTEXT EVIDENCE per-step T1/T2/T3 audit + REQUIRED OUTPUTS block producing evidence gap and evidence tier as separate named outputs. |
| C-06 | Mechanism pathway is testable | PASS | 10 | Observable indicator per labeled step. STEP LABELING REQUIREMENT enforces named agents. |
| C-07 | Confounder or alternative cause | PASS | 10 | CONFOUNDER CHECK: "Name at least one alternative explanation for Y that does not require X and is not the inertia/status-quo case already addressed in INERTIA CHECK." |
| C-08 | AMEND output is actionable | PASS | 10 | Amended (a) mechanism qualifier, (b) scope condition, (c) inertia incorporation three cases, (d) evidence tier note. Four required constraint dimensions. |
| C-09 | Evidence quality rated | PASS | 5 | T1/T2/T3 per-step rating + aggregate tier as required AMEND field. |
| C-10 | Multiple causal pathways considered | FAIL | 0 | Not asked. |
| C-11 | Mechanism incompleteness acknowledged | PASS | 5 | "Minimum 3 labeled steps. If fewer than 3 can be traced with confidence, say so explicitly ('mechanism not fully traceable') rather than generating thin steps." |
| C-12 | Falsification break anchored to named step | PASS | 5 | Required format + "The label must match the step label in the pathway exactly." Explicit failure mode named. |
| C-13 | Evidence gap localized to pathway steps | PASS | 5 | REQUIRED OUTPUTS: "Evidence gap: [list Step N -- [Name] labels with no supporting evidence; write 'none -- all steps supported' if no gaps exist]." Per-step gap enumeration structurally mandated. |
| C-14 | AMEND conditioned on inertia finding | PASS | 5 | "This verdict must appear explicitly in the AMEND section below regardless of its value. All three verdict values are meaningful for the causal claim. Not competing is not a neutral finding -- it is a positive bounding condition." Three-case mandatory Amended (c). |
| C-15 | AMEND synthesizes all phase outputs | PARTIAL | 2.5 | AMEND has: Inertia verdict, Evidence gap, Evidence tier, Confounder finding. Missing: Mechanism completeness as a named AMEND field. The Amended clause has "(a) mechanism qualifier" but mechanism completeness status is not a separate named AMEND entry. Three-and-a-half of four required C-15 fields. |
| C-16 | Pathway steps formally labeled | PASS | 5 | STEP LABELING REQUIREMENT: "This is not a formatting preference -- it is a structural prerequisite. Unlabeled steps cause falsification anchoring and evidence gap enumeration to fail mechanically." Strongest C-16 framing in R4. |
| C-17 | Confounder explicitly distinguished from inertia | PASS | 5 | CONFOUNDER CHECK "does not require X and is not the inertia/status-quo case already addressed in INERTIA CHECK." Explicit exclusion language. |
| C-18 | Incomplete pathway still anchors falsification | PARTIAL | 2.5 | No CONDITIONAL BRANCH in FALSIFICATION CONDITION. "Say so explicitly" instruction in MECHANISM PATHWAY but falsification section has no prohibited-forms list, no BEST-TRACEABLE ANCHOR format, no explicit prohibition on deferral. |
| C-19 | AMEND evidence gap and evidence tier are separate fields | PASS | 5 | Design purpose. REQUIRED OUTPUTS block: explicit orthogonality statement + counterexample ("A pathway where all steps have T1 evidence has gap: 'none' but tier: T1") + "One does not substitute for the other." Both as separate named AMEND fields with integration rule: "merging them into a single entry does not pass; omitting either does not pass." |
| C-20 | AMEND inertia incorporation is unconditional | PASS | 5 | Three-case mandatory Amended (c): "reference the inertia verdict explicitly -- required for ALL three verdict values, not only when Competing or Unclear." Integration rule: "Conditioning inertia incorporation on the verdict being Competing or Unclear does not pass." |
| **Total** | | | **140** | All essential: PASS |

---

## V-05: Full v4 aspirational stack

| ID | Criterion | Verdict | Pts | Evidence Note |
|----|-----------|---------|-----|---------------|
| C-01 | Mechanism traced as pathway | PASS | 12 | Phase 2: STEP LABELING REQUIREMENT as structural prerequisite + "Step N -- [Name]: What changes. Who acts. Observable indicator." |
| C-02 | Falsification is mechanism break | PASS | 12 | Phase 3: Required format + CONDITIONAL BRANCH with named prohibited forms + BEST-TRACEABLE ANCHOR format. "Do not state falsification as a metric threshold. Name where the mechanism stops working." |
| C-03 | Inertia check performed | PASS | 12 | Phase 0 INERTIA GATE -- first phase before any mechanism work. INERTIA VERDICT with one-sentence basis. Assertion alone not acceptable. |
| C-04 | Causal claim narrowed in AMEND | PASS | 12 | Phase 6: 9-field AMEND structure with strict integration rules. "Restating the original hypothesis does not pass. Broadening it does not pass." |
| C-05 | Context evidence assessed | PASS | 12 | Phase 4: per-step T1/T2/T3 audit using Phase 2 formal labels + FIELD INDEPENDENCE NOTE producing both outputs. "Do not substitute general research for team-specific evidence." |
| C-06 | Mechanism pathway is testable | PASS | 10 | Observable indicator per labeled step in Phase 2. |
| C-07 | Confounder or alternative cause | PASS | 10 | Phase 5: "Name at least one alternative explanation for Y that (a) does not involve X as a cause, AND (b) is not the inertia/status-quo case already addressed in Phase 0." Silence not acceptable. |
| C-08 | AMEND output is actionable | PASS | 10 | Phase 6 Amended: (a) mechanism qualifier, (b) scope condition, (c) inertia incorporation for all three cases, (d) confounder note. Four required constraint dimensions. |
| C-09 | Evidence quality rated | PASS | 5 | Phase 4: T1/T2/T3 scale with full definitions + per-step rating + Aggregate evidence tier as required named output. |
| C-10 | Multiple causal pathways considered | PASS | 5 | Phase 2: "Also: is there more than one plausible causal pathway from X to Y?" If yes: trace primary + name secondary + note relationship (complementary/competing/nested). If no: note mechanism is singular. Both outcomes required. Frontmatter: secondary_pathway_noted, pathway_relationship. |
| C-11 | Mechanism incompleteness acknowledged | PASS | 5 | Phase 1 MECHANISM READINESS: PATHWAY INCOMPLETE declaration format + "Producing three thin or vague steps to clear this gate -- instead of declaring incompleteness -- fails this phase." Accurate self-report required output. |
| C-12 | Falsification break anchored to named step | PASS | 5 | Phase 3: step number + name must match Phase 2 labeled rows. "[UNCERTAIN] steps may still serve as falsification anchors -- note the uncertainty in the indicator description." Step-level anchor preserved even for uncertain steps. |
| C-13 | Evidence gap localized to pathway steps | PASS | 5 | Phase 4 FIELD INDEPENDENCE NOTE: "Evidence gap steps: [list Step N -- [Name] labels with no supporting evidence; write 'none' if every step has evidence]." Per-step gap enumeration structurally mandated as named output. |
| C-14 | AMEND conditioned on inertia finding | PASS | 5 | Phase 6: "required regardless of verdict value; no verdict makes inertia incorporation optional." Three-case forms for Competing, Not competing, Unclear. Inertia verdict always named AMEND field. |
| C-15 | AMEND synthesizes all phase outputs | PASS | 5 | Phase 6: All four required fields present as named entries -- Inertia verdict, Mechanism completeness, Evidence tier, Confounder finding. Integration rules: "Omitting any of them does not pass. Partial synthesis is not synthesis -- all fields must be reflected." |
| C-16 | Pathway steps formally labeled | PASS | 5 | Phase 2: "This is not a presentational preference -- it is a structural prerequisite. Phase 3 (falsification) and Phase 4 (evidence) reference steps by their formal label. Unlabeled steps make falsification anchoring and evidence gap enumeration fail mechanically." |
| C-17 | Confounder explicitly distinguished from inertia | PASS | 5 | Phase 5: "The inertia case (Phase 0) is EXCLUDED from this analysis. It does not count as a confounder." + Required acknowledgment: "Explicitly acknowledge the exclusion: 'The inertia case (Phase 0 verdict: [verdict]) is not included here -- it was handled separately in Phase 0.'" Mandatory acknowledgment in output. |
| C-18 | Incomplete pathway still anchors falsification | PASS | 5 | Phase 3 CONDITIONAL BRANCH: named prohibited forms + mandatory BEST-TRACEABLE ANCHOR format + "Incompleteness changes the confidence annotation -- not the structural requirement to name a step-level anchor. A partial pathway still produces at least one falsifiable break point." |
| C-19 | AMEND evidence gap and evidence tier are separate fields | PASS | 5 | Phase 4 FIELD INDEPENDENCE NOTE: orthogonality statement + null-gap counterexample ("a pathway where all steps have T1 evidence has gap steps: 'none' but still carries aggregate evidence tier: T1; produce both fields in every output") + "One does not substitute for the other." Both as separate named Phase 6 AMEND fields with integration rule: "merging them or omitting either does not pass." |
| C-20 | AMEND inertia incorporation is unconditional | PASS | 5 | Phase 6 AMEND (c): "required regardless of verdict value; no verdict makes inertia incorporation optional" + three-case mandatory forms + integration rule: "conditioning it on Competing or Unclear does not pass." Named escape hatch as failure mode. |
| **Total** | | | **150** | All essential: PASS -- ceiling |

---

## Rankings

| Rank | Variation | Score /150 | All Essential | Interpretation | Notes |
|------|-----------|-----------|---------------|----------------|-------|
| 1 | **V-05: Full v4 aspirational stack** | **150** | YES | Golden | Ceiling. All 12 aspirational criteria pass. |
| 2 | **V-04: Evidence separation + unconditional inertia** | **140** | YES | Golden | C-19+C-20 combined earns 10 new pts; C-15 partial (mechanism completeness field missing) and C-18 partial (no CONDITIONAL BRANCH) cost 10 pts total |
| 3 | **V-01: Evidence field separation** | **135** | YES | Acceptable | C-19 design purpose; C-18 PASS (inherits R3 V-04 CONDITIONAL BRANCH); C-14/C-15 partial; C-20 FAIL |
| 3 | **V-02: Unconditional inertia incorporation** | **135** | YES | Acceptable | C-20 design purpose; C-14/C-15 full pass; C-13/C-18 partial; C-19 FAIL |
| 5 | **V-03: Inertia verdict as load-bearing anchor** | **130** | YES | Acceptable | C-20 PASS + strongest C-17; C-15 FAIL (two of four fields missing); C-19 FAIL; C-13/C-18 partial |

---

## Score Deltas vs R3

| Variation | R4 Score /150 | R3 Baseline /140 | R4 Gain | Primary driver |
|-----------|--------------|-----------------|---------|----------------|
| V-05 | 150 | 140 (R3 V-05) | +10 | C-19 PASS (+5) + C-20 PASS (+5) via FIELD INDEPENDENCE NOTE + three-case mandatory integration rule |
| V-04 | 140 | ~126 (R3 V-02 level) | +14 | C-19 PASS (+5) + C-20 PASS (+5) + C-14/C-15 improvements over R3 V-02; C-18 PARTIAL |
| V-01 | 135 | 131 (R3 V-04) | +4 | C-19 PASS (+5); C-15 PARTIAL improved (evidence tier now in AMEND); C-20 FAIL (0) |
| V-02 | 135 | ~127 (R3 V-01) | +8 | C-20 PASS (+5); C-14 full PASS; C-19 FAIL (0); C-13 still PARTIAL |
| V-03 | 130 | ~123 (R3 V-03) | +7 | C-20 PASS (+5); C-14 full PASS; C-15 still FAIL; C-19 FAIL |

---

## Excellence Signals from V-05

**What the ceiling variation has that Golden V-04 does not:**

1. **C-10 (+5): Phase 2 explicit secondary pathway probe** -- "Is there more than one plausible causal pathway?" is the minimal trigger. Without this explicit question, no variation produces a secondary pathway survey. V-04's clean non-phase structure has no equivalent prompt element. Single-axis variations also do not ask it.

2. **C-18 (+2.5 -> PASS vs PARTIAL): Phase 3 CONDITIONAL BRANCH** -- naming the prohibited forms ("Cannot falsify until the mechanism is better understood", "If Y does not improve") is what closes C-18. V-04's "say so explicitly" in the mechanism section doesn't prevent a model from deferring falsification when incompleteness is declared. The prohibition must appear in the FALSIFICATION section, not just the pathway section.

3. **C-15 (+2.5 -> PASS vs PARTIAL): Mechanism completeness as a named AMEND field** -- Phase 6 explicitly lists "Mechanism completeness: {complete / incomplete / partial -- from Phase 1}" as a named AMEND entry. V-04 achieves all other named fields but omits this one, and fails C-15 as a result. The mechanism qualifier "(a)" in the Amended clause is not an equivalent substitute.

**The core v4 pattern:**
- V-04 proves C-19 and C-20 are compatible and complementary -- adding both in a single clean prompt without the full phase stack works and achieves Golden
- V-05 proves C-19 and C-20 layer onto the full phase structure without conflict at the ceiling
- The gap between V-04 (140) and V-05 (150) is not C-19/C-20 -- those are fully resolved in V-04 -- it is the pre-existing C-10/C-15/C-18 partials that only the phase structure closes

---

```json
{"top_score": 150, "all_essential_pass": true, "new_patterns": ["null-gap counterexample is the load-bearing element of the C-19 fix: naming two fields is not enough -- showing 'a pathway with all T1 evidence has gap: none but tier: T1' makes orthogonality concrete and prevents the category error", "three-case mandatory inertia table requires the prohibited form named explicitly ('conditioning on Competing or Unclear does not pass') -- without naming the escape hatch as a failure mode, models produce the conditional form and believe they comply", "mechanism completeness must be a separate named AMEND field for C-15 full pass: the mechanism qualifier in the Amended clause does not substitute -- V-04 has strong AMEND structure but omits this field and PARTIAL on C-15 despite closing C-19 and C-20"]}
```
