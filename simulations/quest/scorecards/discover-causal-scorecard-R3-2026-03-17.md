## discover-causal R3 Scorecard

**Rankings (v3 rubric, 140 pts max):**

| Rank | Variation | Score | Interpretation |
|------|-----------|-------|----------------|
| 1 | V-05: Full v3 aspirational stack | **140/140** | Golden — ceiling |
| 2 | V-04: Incomplete-pathway falsification anchor | **131/140** | Golden |
| 3 | V-01: AMEND synthesis completeness | **127/140** | Acceptable |
| 4 | V-02: Formal step labeling as prerequisite | **126/140** | Acceptable |
| 5 | V-03: Confounder/inertia hard separation | **123/140** | Acceptable |

All five pass all essential criteria. V-05 hits the ceiling. **V-04 achieves Golden as a single-axis variation** — the BEST-TRACEABLE ANCHOR branch is worth 5 pts and sufficient to cross the 130 threshold without needing to close C-14 or C-15.

**Key scoring decisions:**

- **V-01 C-15: PASS** — Design purpose confirmed. Adding `Confounder finding:` as a required AMEND field with the integration rule "including only some is not sufficient" closes C-15.
- **V-04 C-18: PASS** — Design purpose confirmed. CONDITIONAL BRANCH with named prohibited forms + mandatory BEST-TRACEABLE ANCHOR format closes C-18.
- **V-04 C-14/C-15: PARTIAL** — C-14 fails because the inertia conditional is "if Competing/Unclear" not universal. C-15 fails because AMEND has evidence gap (step labels) but not evidence tier (T1/T2/T3 rating) — these are different fields.
- **V-01/V-02/V-03 C-18: FAIL** — None have the conditional branch prohibiting deferral when incompleteness is declared.
- **C-18 gradeability:** All five have C-11 PASS + C-12 PASS, so C-18 is scored (not N/A) for all.

**4 new patterns:**

1. C-18 BEST-TRACEABLE ANCHOR is the highest-value single v3 addition — achieves Golden alone
2. Evidence gap ≠ evidence tier — C-15 requires the T1/T2/T3 aggregate rating as a named AMEND field, not just the list of gap steps
3. C-14 full pass requires universal incorporation rule, not conditional ("if Competing/Unclear")
4. All four v3 criteria layer on the R2 V-05 phase structure without conflict — ceiling achievable in one combined variation

```json
{"top_score": 140, "all_essential_pass": true, "new_patterns": ["C-18 best-traceable anchor is the highest-value single v3 addition: adding it alone achieves Golden without closing all other v3 gaps", "evidence gap and evidence tier are different AMEND fields -- C-15 full pass requires the T1/T2/T3 aggregate rating as a named AMEND entry, not just the list of gap steps", "C-14 full pass requires universal inertia incorporation rule ('ignoring any of the four fields does not pass'), not a conditional one ('if Competing/Unclear') -- the conditional approach leaves a Not-competing escape hatch", "all four v3 criteria (C-15/C-16/C-17/C-18) layer on the R2 V-05 phase structure without conflict -- the ceiling is achievable in a single combined variation"]}
```
[Name]: What changes. Who acts. Observable indicator." format + minimum 3 steps + incompleteness declaration instruction. |
| C-02 | Falsification is mechanism break | PASS | 12 | Required format: "The mechanism fails if Step [N] -- [Name] -- does not occur, observable as [indicator]." Step number and name must match a labeled row. |
| C-03 | Inertia check performed | PASS | 12 | Dedicated INERTIA CHECK section with INERTIA VERDICT: [Competing / Not competing / Unclear -- one sentence basis]. |
| C-04 | Causal claim narrowed in AMEND | PASS | 12 | AMEND Required structure with Amended field that must incorporate all four prior findings. Integration rules explicitly prohibit restating or broadening. |
| C-05 | Context evidence assessed | PASS | 12 | Rate each piece T1/T2/T3, name each piece, name which pathway step it supports. Aggregate evidence tier required. Explicit null case. |
| C-06 | Mechanism pathway is testable | PASS | 10 | Observable indicator per step. Named agents. |
| C-07 | Confounder or alternative cause | PASS | 10 | Dedicated ALTERNATIVE CAUSES section requiring: (1) alternative causal pathway not through mechanism, (2) confounding variable. Both required, not either. |
| C-08 | AMEND output is actionable | PASS | 10 | Amended must include mechanism qualifier, scope condition, inertia condition if Competing/Unclear, and confounder risk note. Four named constraint dimensions. |
| C-09 | Evidence quality rated | PASS | 5 | T1/T2/T3 scale with category definitions + per-piece rating + Aggregate evidence tier required output. |
| C-10 | Multiple causal pathways considered | FAIL | 0 | Not asked. No instruction to identify alternative pathways from X to Y. |
| C-11 | Mechanism incompleteness acknowledged | PASS | 5 | "If you cannot trace 3 observable steps with current knowledge, say so explicitly ('mechanism not fully traceable at step N') rather than generating thin steps." |
| C-12 | Falsification break anchored to named step | PASS | 5 | Labeled step format ("Step N -- [Name]:") instructed + falsification must reference a labeled row. Steps have stable referents. |
| C-13 | Evidence gap localized to pathway steps | PARTIAL | 2 | Per-piece evidence names which step it supports, so evidence presence is per-step. But no required explicit gap enumeration ("Evidence gap steps:"). Steps lacking evidence are inferable but not mandated as a named output. |
| C-14 | AMEND conditioned on inertia finding | PASS | 5 | Integration rule: "A narrowed claim that ignores any of the four named fields does not pass." Inertia verdict is one of the four — universally required in the amended claim, not conditionally. |
| C-15 | AMEND synthesizes all phase outputs | PASS | 5 | AMEND Required structure has all four: Inertia verdict, Mechanism completeness, Evidence tier, Confounder finding. Integration rule: "Including only some is not sufficient -- all four must appear." Design purpose confirmed. |
| C-16 | Pathway steps formally labeled | PASS | 5 | "Step N -- [Name]: What changes. Who acts. Observable indicator." format instructed. Falsification must match labeled rows. Stable referents established. |
| C-17 | Confounder explicitly distinguished from inertia | PASS | 5 | ALTERNATIVE CAUSES section begins: "This is NOT the inertia check." Explains the distinction: inertia = status quo trends toward Y over time; this section = independently operating causes present right now. Explicit separation in prompt produces explicit separation in output. |
| C-18 | Incomplete pathway still anchors falsification | FAIL | 0 | No conditional branch in FALSIFICATION CONDITION for incomplete pathways. When C-11 triggers, model is not prohibited from deferring or using a metric threshold. No BEST-TRACEABLE ANCHOR format required. |
| **Total** | | | **127** | All essential: PASS |

---

## V-02: Formal step labeling as prerequisite

| ID | Criterion | Verdict | Pts | Evidence Note |
|----|-----------|---------|-----|---------------|
| C-01 | Mechanism traced as pathway | PASS | 12 | STEP LABELING REQUIREMENT section with structural prerequisite framing + "Step N -- [Name]:" format with example + minimum 3 labeled steps. |
| C-02 | Falsification is mechanism break | PASS | 12 | Required format enforced. "'Step 2 fails' without the step name does not pass." Stable label must match pathway exactly. |
| C-03 | Inertia check performed | PASS | 12 | INERTIA CHECK section with INERTIA VERDICT: [Competing / Not competing / Unclear]. |
| C-04 | Causal claim narrowed in AMEND | PASS | 12 | AMEND section with Original/Inertia verdict/Pathway/Falsification/Evidence gap/Confounder finding/Amended fields. |
| C-05 | Context evidence assessed | PASS | 12 | Per-step evidence audit: "For each labeled step in the pathway above, assess evidence." Format: Step N -- [Name]: [evidence] -- [T1/T2/T3/none]. Strongest C-05 of single-axis variations. |
| C-06 | Mechanism pathway is testable | PASS | 10 | Observable indicator per labeled step. |
| C-07 | Confounder or alternative cause | PASS | 10 | CONFOUNDER CHECK: "Name at least one alternative explanation for Y that does not require X and is not the inertia/status-quo case already addressed in INERTIA CHECK." |
| C-08 | AMEND output is actionable | PASS | 10 | Amended "bounded by mechanism qualifier, scope condition, and evidence tier; reference labeled steps where relevant." Three named constraint dimensions. |
| C-09 | Evidence quality rated | PASS | 5 | T1/T2/T3 scale defined (anecdotal/correlation/controlled) + per-step rating + Aggregate tier required output. |
| C-10 | Multiple causal pathways considered | FAIL | 0 | Not asked. |
| C-11 | Mechanism incompleteness acknowledged | PASS | 5 | "Minimum 3 labeled steps. If fewer than 3 can be traced with confidence, say so explicitly ('mechanism not fully traceable') rather than generating thin steps." |
| C-12 | Falsification break anchored to named step | PASS | 5 | Upfront STEP LABELING REQUIREMENT + falsification label must match exactly + explicit failure mode: "'Step 2 fails' without step name does not pass." Strongest C-12 instruction for a single-axis variation. |
| C-13 | Evidence gap localized to pathway steps | PASS | 5 | "For each labeled step in the pathway above, assess evidence." + "Evidence gap steps: [list the Step N -- [Name] labels that have no supporting evidence]" as required named output. Per-step gap enumeration structurally mandated. |
| C-14 | AMEND conditioned on inertia finding | PARTIAL | 3 | Inertia verdict is a required AMEND named field (always documented). However, Amended instruction is "bounded by mechanism qualifier, scope condition, and evidence tier" — no mention of inertia conditioning. The verdict appears in AMEND but need not shape the amended claim text. |
| C-15 | AMEND synthesizes all phase outputs | PARTIAL | 3 | AMEND has Inertia verdict and Confounder finding (2/4 required). Missing: Mechanism completeness as named field. Has Evidence gap (step labels lacking support) but not Evidence tier (T1/T2/T3 aggregate rating) — these are different outputs. Partial synthesis. |
| C-16 | Pathway steps formally labeled | PASS | 5 | Design purpose. "This is not a formatting preference -- it is a structural prerequisite. The falsification condition and evidence gap sections reference steps by their formal label. Unlabeled steps cause falsification anchoring and evidence gap enumeration to fail mechanically." Strongest C-16 framing. |
| C-17 | Confounder explicitly distinguished from inertia | PASS | 5 | CONFOUNDER CHECK explicitly says "is not the inertia/status-quo case already addressed in INERTIA CHECK." Separate section + explicit exclusion language produces distinct outputs. |
| C-18 | Incomplete pathway still anchors falsification | FAIL | 0 | No conditional branch for incomplete pathways in FALSIFICATION CONDITION. C-11 can trigger but falsification section has no BEST-TRACEABLE ANCHOR requirement. |
| **Total** | | | **126** | All essential: PASS |

---

## V-03: Confounder/inertia hard separation

| ID | Criterion | Verdict | Pts | Evidence Note |
|----|-----------|---------|-----|---------------|
| C-01 | Mechanism traced as pathway | PASS | 12 | "Step N -- [Name]: What changes. Who acts. Observable indicator." + minimum 3 steps + incompleteness instruction. |
| C-02 | Falsification is mechanism break | PASS | 12 | Required format: "The mechanism fails if Step [N] -- [Name] -- does not occur, observable as [indicator]." Must match labeled row. |
| C-03 | Inertia check performed | PASS | 12 | INERTIA CHECK section with INERTIA VERDICT: [Competing / Not competing / Unclear]. Scoped specifically to status quo: "existing behaviors, trends, and workarounds that produce Y without any new feature." |
| C-04 | Causal claim narrowed in AMEND | PASS | 12 | AMEND with Original/Inertia verdict/Confounder finding/Pathway/Falsification/Amended fields. |
| C-05 | Context evidence assessed | PASS | 12 | "Name each piece specifically. Rate each: T1/T2/T3. Note which pathway step each piece supports. If none: 'No context-specific evidence found.'" |
| C-06 | Mechanism pathway is testable | PASS | 10 | Observable indicator per labeled step. |
| C-07 | Confounder or alternative cause | PASS | 10 | CONFOUNDER CHECK: "Name at least one. If none can be identified, explain why the mechanism is insulated." Lists four confounder types: competing initiatives, confounding variables, selection effects, seasonal/environmental effects. |
| C-08 | AMEND output is actionable | PASS | 10 | Amended "bounded by mechanism qualifier and scope condition that distinguishes X's effect from the named confounder; incorporates inertia condition if status is Competing or Unclear." |
| C-09 | Evidence quality rated | PASS | 5 | T1/T2/T3 per-piece rating required. Pass condition met: response distinguishes evidence types. (Aggregate tier not required as named output but per-piece rating satisfies C-09.) |
| C-10 | Multiple causal pathways considered | FAIL | 0 | Not asked. |
| C-11 | Mechanism incompleteness acknowledged | PASS | 5 | "If fewer can be traced with confidence, say so explicitly rather than generating thin steps to fill the count." |
| C-12 | Falsification break anchored to named step | PASS | 5 | Labeled step format + falsification must match labeled row. |
| C-13 | Evidence gap localized to pathway steps | PARTIAL | 2 | Per-piece evidence names which step it supports. But no required gap enumeration ("Evidence gap steps:"). Same gap as V-01: inferable but not mandated. |
| C-14 | AMEND conditioned on inertia finding | PARTIAL | 3 | Inertia verdict is a named AMEND field (always documented). Amended instruction: "incorporates inertia condition if status is Competing or Unclear." When Not competing, amended claim need not incorporate inertia verdict. Same conditional gap as V-04 in R2. |
| C-15 | AMEND synthesizes all phase outputs | PARTIAL | 3 | AMEND has Inertia verdict and Confounder finding. Missing: Mechanism completeness and Evidence tier as named AMEND fields. Two of four required C-15 fields present. |
| C-16 | Pathway steps formally labeled | PASS | 5 | "Step N -- [Name]:" format instructed. Falsification references labeled step. Not framed as structural prerequisite but the format instruction produces labeled outputs. |
| C-17 | Confounder explicitly distinguished from inertia | PASS | 5 | Design purpose. CONFOUNDER CHECK: "This section asks a DIFFERENT question from the inertia check above." + "The inertia case is EXCLUDED from this analysis." + Required output: "Explicitly state: 'The inertia case (INERTIA VERDICT: [verdict]) is NOT included here as a confounder -- it was addressed in the Inertia Check section.'" Strongest C-17 structural enforcement. |
| C-18 | Incomplete pathway still anchors falsification | FAIL | 0 | No conditional branch for incomplete pathways in FALSIFICATION CONDITION. C-11 can trigger but no prohibition on deferral. |
| **Total** | | | **123** | All essential: PASS |

---

## V-04: Incomplete-pathway falsification anchor

| ID | Criterion | Verdict | Pts | Evidence Note |
|----|-----------|---------|-----|---------------|
| C-01 | Mechanism traced as pathway | PASS | 12 | "Step N -- [Name]: What changes. Who acts. Observable indicator." + [UNCERTAIN] tag for unsubstantiated steps. READINESS GATE before tracing. |
| C-02 | Falsification is mechanism break | PASS | 12 | Required format + BEST-TRACEABLE ANCHOR for incomplete pathways still produces a mechanism break statement, not a metric threshold. |
| C-03 | Inertia check performed | PASS | 12 | === INERTIA CHECK === with INERTIA VERDICT: [Competing / Not competing / Unclear]. |
| C-04 | Causal claim narrowed in AMEND | PASS | 12 | AMEND: Mechanism complete/Inertia status/Pathway/Falsification/Evidence gap/Confounder finding/Amended. |
| C-05 | Context evidence assessed | PASS | 12 | "Identify which labeled steps in the pathway have no supporting evidence -- list them by step number and name. Evidence gap steps: [{step labels}]" — per-step gap accounting explicitly required. |
| C-06 | Mechanism pathway is testable | PASS | 10 | Observable indicator per labeled step. |
| C-07 | Confounder or alternative cause | PASS | 10 | CONFOUNDER CHECK: "Name at least one cause of Y that does not involve X and is not the inertia case... a simultaneously-operating cause, not a counterfactual." |
| C-08 | AMEND output is actionable | PASS | 10 | Amended "must include mechanism qualifier; scope condition; inertia condition if Competing or Unclear; note if pathway incompleteness limits the claim's certainty scope." Four named constraint forms. |
| C-09 | Evidence quality rated | PASS | 5 | Aggregate evidence tier: T1/T2/T3/none as required output. T1/T2/T3 labels present (model understands the scale). Rates strength of evidence, not just presence. |
| C-10 | Multiple causal pathways considered | FAIL | 0 | Not asked. |
| C-11 | Mechanism incompleteness acknowledged | PASS | 5 | READINESS GATE: "If no: declare incompleteness now. Write: 'PATHWAY INCOMPLETE: mechanism cannot be traced past [step]. Missing knowledge: [what is needed].' Then continue, marking [UNCERTAIN]." + "Producing thin or vague steps to clear this gate -- instead of declaring incompleteness -- fails this section." |
| C-12 | Falsification break anchored to named step | PASS | 5 | Labeled steps + falsification references labeled row + BEST-TRACEABLE ANCHOR for incomplete: "The mechanism fails if Step [N] -- [Name] -- does not occur." Even partial pathways produce named-step anchors. |
| C-13 | Evidence gap localized to pathway steps | PASS | 5 | "Identify which labeled steps in the pathway have no supporting evidence -- list them by step number and name (Step N -- Name). Evidence gap steps: [{step labels with no supporting evidence}]" — explicit named output. |
| C-14 | AMEND conditioned on inertia finding | PARTIAL | 3 | Inertia status always a required AMEND field (documented). Amended instruction: "inertia condition if Competing or Unclear." When Not competing, amended claim need not incorporate inertia verdict. Same gap as R2 V-04 — conditional, not universal. |
| C-15 | AMEND synthesizes all phase outputs | PARTIAL | 3 | AMEND has Mechanism complete, Inertia status, Confounder finding (3/4). Missing: Evidence tier as a named AMEND field — has Evidence gap (step labels) but not the T1/T2/T3 aggregate rating. Three of four required C-15 fields present. |
| C-16 | Pathway steps formally labeled | PASS | 5 | "Step N -- [Name]:" format instructed. Falsification references labeled step. Not framed as structural prerequisite but output will have labeled steps. |
| C-17 | Confounder explicitly distinguished from inertia | PASS | 5 | CONFOUNDER CHECK: "is not the inertia case" + "The inertia case was addressed above. This section names something else that could independently produce Y right now." Explicit exclusion stated. |
| C-18 | Incomplete pathway still anchors falsification | PASS | 5 | Design purpose. CONDITIONAL BRANCH with: (a) prohibited output forms listed explicitly ("Cannot falsify until...", "Falsification is deferred...", "If outcome Y does not improve..."), (b) required BEST-TRACEABLE ANCHOR format with exact wording, (c) "Declaring incompleteness changes the confidence annotation and adds a note, but does not exempt this section from producing a step-level anchor." |
| **Total** | | | **131** | All essential: PASS |

---

## V-05: Full v3 aspirational stack

| ID | Criterion | Verdict | Pts | Evidence Note |
|----|-----------|---------|-----|---------------|
| C-01 | Mechanism traced as pathway | PASS | 12 | Phase 2: "Step N -- [Name]: What changes. Who acts. Observable indicator." Labeled format as structural prerequisite. |
| C-02 | Falsification is mechanism break | PASS | 12 | Phase 3: Required format + BEST-TRACEABLE ANCHOR conditional branch. "Do not state falsification as a metric threshold. Name where the mechanism stops working." |
| C-03 | Inertia check performed | PASS | 12 | Phase 0 INERTIA GATE — first phase before any mechanism work. INERTIA VERDICT with one-sentence basis. Assertion alone not acceptable. |
| C-04 | Causal claim narrowed in AMEND | PASS | 12 | Phase 6: 9-field AMEND structure with strict narrowing rules. "Restating is a failure mode. Broadening is a failure mode." |
| C-05 | Context evidence assessed | PASS | 12 | Phase 4: Per-step T1/T2/T3 audit + "Evidence gap steps: [list Step N -- [Name] labels with no supporting evidence]" as required output. |
| C-06 | Mechanism pathway is testable | PASS | 10 | Observable indicator per labeled step in Phase 2. |
| C-07 | Confounder or alternative cause | PASS | 10 | Phase 5: "Name at least one alternative explanation for Y that (a) does not involve X as a cause, AND (b) is not the inertia/status-quo case already addressed in Phase 0." |
| C-08 | AMEND output is actionable | PASS | 10 | Phase 6 Amended: (a) mechanism qualifier, (b) scope condition, (c) inertia condition if Competing/Unclear, (d) confounder note. Four required components. Most constrained AMEND specification. |
| C-09 | Evidence quality rated | PASS | 5 | Phase 4: T1/T2/T3 scale with full definitions + per-step rating + Aggregate evidence tier required output + frontmatter field. |
| C-10 | Multiple causal pathways considered | PASS | 5 | Phase 2: "Is there more than one plausible causal pathway from X to Y?" If yes: trace primary + name secondary + note relationship (complementary/competing/nested). If no: note mechanism is singular. Both outcomes required. |
| C-11 | Mechanism incompleteness acknowledged | PASS | 5 | Phase 1: PATHWAY INCOMPLETE declaration format + "Producing three thin or vague steps to clear this gate -- instead of declaring incompleteness -- fails this phase." |
| C-12 | Falsification break anchored to named step | PASS | 5 | Phase 3: step number + name must match Phase 2 labeled rows + "[UNCERTAIN] steps may still serve as falsification anchors." Even incomplete pathways produce gradeable anchors. |
| C-13 | Evidence gap localized to pathway steps | PASS | 5 | Phase 4: "For each step in Phase 2: Step N -- [Name]: [evidence] -- [T1/T2/T3/none]" + "Evidence gap steps: [list Step N -- [Name] labels with no supporting evidence]" as required named output. |
| C-14 | AMEND conditioned on inertia finding | PASS | 5 | Phase 6: Inertia verdict always named field + Amended requires "(c) inertia condition if Phase 0 is Competing or Unclear" + "A narrowed claim that ignores the inertia verdict does not pass." Universal incorporation enforced. |
| C-15 | AMEND synthesizes all phase outputs | PASS | 5 | Phase 6: All four required fields present — Inertia verdict, Mechanism completeness, Evidence tier, Confounder finding — as named AMEND fields. Integration rules: "Omitting any of them does not pass. Partial synthesis is not synthesis." |
| C-16 | Pathway steps formally labeled | PASS | 5 | Phase 2: "This is not a presentational preference -- it is a structural prerequisite. Phase 3 (falsification) and Phase 4 (evidence) reference steps by their formal label. Unlabeled steps make C-12 and C-13 unscoreable." Explicit prerequisite framing. |
| C-17 | Confounder explicitly distinguished from inertia | PASS | 5 | Phase 5: "The inertia case (Phase 0) is EXCLUDED from this analysis. It does not count as a confounder" + Required: "Explicitly acknowledge the exclusion: 'The inertia case (Phase 0 verdict: [verdict]) is not included here -- it was handled separately in Phase 0.'" Mandatory acknowledgment in output. |
| C-18 | Incomplete pathway still anchors falsification | PASS | 5 | Phase 3 CONDITIONAL BRANCH: named prohibited forms + "BEST-TRACEABLE ANCHOR: The mechanism fails if Step [N] -- [Name]..." + "Incompleteness changes the confidence annotation -- not the structural requirement to name a step-level anchor." |
| **Total** | | | **140** | All essential: PASS — ceiling |

---

## Rankings

| Rank | Variation | Score /140 | All Essential | Interpretation | Notes |
|------|-----------|-----------|---------------|----------------|-------|
| 1 | **V-05: Full v3 aspirational stack** | **140** | YES | Golden | Ceiling. All 10 aspirational criteria pass. |
| 2 | **V-04: Incomplete-pathway falsification anchor** | **131** | YES | Golden | C-18 alone achieves Golden; partial on C-14/C-15 |
| 3 | **V-01: AMEND synthesis completeness** | **127** | YES | Acceptable | C-15 + C-14 full pass; C-18 gap |
| 4 | **V-02: Formal step labeling as prerequisite** | **126** | YES | Acceptable | C-16 full pass; C-14/C-15 partial; C-18 gap |
| 5 | **V-03: Confounder/inertia hard separation** | **123** | YES | Acceptable | C-17 strongest; C-14/C-15 partial; C-18 gap |

---

## Score Deltas vs R2

R2 variations are different prompts; the R3 V-01 through V-05 are new variations targeting
the v3 criteria. Direct comparison is against the R2 rubric applied to the new prompts:

| Variation | v3 Score /140 | v2 Equivalent /120 | v3 Gain | Primary driver |
|-----------|--------------|-------------------|---------|----------------|
| V-04 | 131 | ~108 (remove C-18) | +23 | C-18 BEST-TRACEABLE ANCHOR adds 5; C-07/C-09 now present vs R2 V-04 |
| V-01 | 127 | ~122 (remove C-15/C-16/C-17/C-18) | +5 | C-15 design purpose + C-16/C-17 pass |
| V-02 | 126 | ~121 | +5 | C-16 design purpose; C-15 partial |
| V-03 | 123 | ~118 | +5 | C-17 design purpose; C-15 partial |
| V-05 | 140 | 120 | +20 | All four v3 criteria pass on top of R2 ceiling |

---

## Excellence Signals from Top-Scoring Variations

**What made V-05 the ceiling and V-04 the second Golden:**

1. **C-18 is the highest-value single v3 addition** — V-04 achieves Golden with C-18 alone
   (131 despite PARTIAL on C-14/C-15). The BEST-TRACEABLE ANCHOR branch is load-bearing:
   5 pts that require no other criteria to change. A targeted single-axis addition can be
   worth more than a broad integration improvement.

2. **C-15 full pass requires all four named AMEND fields including evidence tier** — Evidence
   gap (which steps lack evidence) is not equivalent to evidence tier (T1/T2/T3 aggregate
   rating). V-04 has three of four C-15 fields but misses evidence tier in AMEND. V-01 gets
   full pass because it adds all four as named AMEND entries. The lesson: AMEND synthesis
   requires each phase's specific OUTPUT TYPE, not a related field from the same phase.

3. **C-14 full pass requires universal incorporation, not conditional** — V-01's integration
   rule "A narrowed claim that ignores any of the four named fields does not pass" achieves
   C-14 full pass by making inertia incorporation unconditional. V-03/V-04's "if Competing
   or Unclear" conditional leaves a Not-competing escape hatch that fails C-14. The stronger
   rule is: all four fields must appear in the amended claim regardless of their verdict.

4. **All four v3 criteria can be layered on the R2 V-05 phase structure without conflict** —
   V-05 confirms no structural tension between C-15, C-16, C-17, and C-18. Phase-ordered
   structure with named outputs makes all four mechanically enforceable simultaneously. The
   v3 rubric ceiling is achievable in a single combined variation.

---

```json
{"top_score": 140, "all_essential_pass": true, "new_patterns": ["C-18 best-traceable anchor is the highest-value single v3 addition: adding it alone achieves Golden without closing all other v3 gaps", "evidence gap and evidence tier are different AMEND fields -- C-15 full pass requires the T1/T2/T3 aggregate rating as a named AMEND entry, not just the list of gap steps", "C-14 full pass requires universal inertia incorporation rule ('ignoring any of the four fields does not pass'), not a conditional one ('if Competing/Unclear') -- the conditional approach leaves a Not-competing escape hatch", "all four v3 criteria (C-15/C-16/C-17/C-18) layer on the R2 V-05 phase structure without conflict -- the ceiling is achievable in a single combined variation"]}
```
