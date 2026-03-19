## discover-causal Round 2 Scorecard

**Rankings:**

| Rank | Variation | Score /120 | Interpretation |
|------|-----------|-----------|----------------|
| 1 | V-05: Full aspirational stack | **120** | Golden (>= 110) |
| 2 | V-02: Evidence quality scale | **105** | Acceptable |
| 3 | V-04: Incompleteness gate + step-anchored | **98** | Acceptable |
| 4 | V-01: Confounder section | **95** | Acceptable |
| 5 | V-03: Competing pathways | **95** | Acceptable |

All five pass all essential criteria. V-05 hits the ceiling (120/120).

---

**Key scoring decisions:**

- **V-01 C-07: PASS** — The dedicated ALTERNATIVE CAUSES section (distinguished from inertia, requiring both an alternative pathway and a confounding variable) fully closes the R1 universal failure. This is V-01's design purpose and it delivers.

- **V-02 C-09: PASS, C-12/C-13: PARTIAL** — The T1/T2/T3 scale fully covers C-09. But steps are positional (not formally labeled), so falsification can only reference "step 2" not "Step 2 -- User acts on prompt." C-13 only derives gap coverage indirectly — models can satisfy the evidence section without listing ungapped steps.

- **V-03 C-14: PASS** — The only single-axis variation to fully pass C-14: "Amended: bounded by the inertia finding" is explicit required language in the AMEND field.

- **V-04 C-14: PARTIAL** — Inertia status is a required AMEND field (always documented), but inertia-conditioned framing in the amended claim is only required when status is Competing/Unclear. Not-competing verdicts can produce amendments that ignore inertia.

---

**4 new patterns found:**

1. **Phase-ordered structure enables AMEND synthesis** — naming each phase output as a required AMEND field makes integration criteria mechanically enforceable
2. **Labeled step format is a prerequisite, not aesthetics** — C-12 and C-13 require a labeled referent; positional steps partially cover this, prose steps do not
3. **Confounder/inertia separation must be explicit** — shared sections produce C-03/C-07 conflation; separate phases with "is not the inertia status quo" close it
4. **C-11 and C-12 are coupled when step labeling is present** — incompleteness gate + labeled steps + step-anchored falsification form a dependency chain
t forms. |
| C-09 | Evidence quality rated | FAIL | 0 | Not asked. No evidence tier scale. |
| C-10 | Multiple causal pathways considered | FAIL | 0 | Not asked. |
| C-11 | Mechanism incompleteness acknowledged | PASS | 5 | "If you cannot trace 3 observable steps with current knowledge, say so explicitly ('mechanism not fully traceable at step N') rather than generating thin steps." Clear self-disclosure instruction. |
| C-12 | Falsification break anchored to named step | FAIL | 0 | Pathway section has no step labels or numbers. Falsification uses "step N" notation but steps are prose bullet format — there is no labeled referent to anchor to. The step reference is a template placeholder, not a structural tie. |
| C-13 | Evidence gap localized to pathway steps | FAIL | 0 | Evidence section asks about "the mechanism holds and the named alternatives are not the actual cause" — aggregate verdict, not per-step accounting. No step gap enumeration. |
| C-14 | AMEND conditioned on inertia finding | FAIL | 0 | AMEND structure has `Key alternative` field but no `Inertia` field. Amended claim is conditioned on alternative causes, not on the inertia finding. The inertia check result is not required to appear in AMEND. |
| **Total** | | | **95** | All essential: PASS |

---

### V-02: Evidence quality scale

| ID | Criterion | Verdict | Pts | Evidence Note |
|----|-----------|---------|-----|---------------|
| C-01 | Mechanism traced as pathway | PASS | 12 | Three-part per-step instruction + minimum 3 steps + incompleteness declaration instruction. |
| C-02 | Falsification is mechanism break | PASS | 12 | "Describe the specific step in the pathway above where mechanism failure would be visible" + required format "The mechanism fails if [step N does not occur], observable as [indicator]." |
| C-03 | Inertia check performed | PASS | 12 | Dedicated INERTIA CHECK section with Competing / Not competing / Unclear verdict format. |
| C-04 | Causal claim narrowed in AMEND | PASS | 12 | AMEND structure includes `Evidence quality`, `Pathway`, `Falsification`, and `Amended` fields. Amended qualified by evidence tier and mechanism condition. |
| C-05 | Context evidence assessed | PASS | 12 | Per-piece evidence naming + explicit null case ("No context-specific evidence found. Tier: none."). Strongest C-05 for this tier: "we have evidence" must be typed, not asserted. |
| C-06 | Mechanism pathway is testable | PASS | 10 | Observable indicator per step. |
| C-07 | Confounder or alternative cause | PASS | 10 | Dedicated CONFOUNDER CHECK section at end of prompt: "Name at least one alternative explanation for Y that does not require X. What else could produce this outcome independently?" Full structural enforcement. |
| C-08 | AMEND output is actionable | PASS | 10 | Evidence-tier-conditioned narrowing: "scoped to the evidence tier available; mechanism condition named; or qualified with 'pending T3 evidence for step N' if the break point has no supporting evidence." Concrete, step-anchored constraint form. |
| C-09 | Evidence quality rated | PASS | 5 | T1/T2/T3 scale embedded directly in evidence section with named categories (anecdotal / correlation / controlled), per-piece ratings, and `Aggregate evidence tier` required output. Structural scaffold for C-09 is the axis being tested — PASS. |
| C-10 | Multiple causal pathways considered | FAIL | 0 | Not asked. |
| C-11 | Mechanism incompleteness acknowledged | PASS | 5 | "If fewer than 3 observable intermediate steps can be identified with current knowledge, say so rather than inventing thin steps to fill the requirement." |
| C-12 | Falsification break anchored to named step | PARTIAL | 3 | Falsification says "Reference the step by its label or position in the pathway above" and format uses "step N" placeholder. However, the pathway section requires prose bullet format with no explicit "Step N -- [Name]:" label structure — steps have positions but not formal labels. The anchor is weaker than V-04/V-05. A model can satisfy this by saying "step 2" without a named label, which C-12 requires. |
| C-13 | Evidence gap localized to pathway steps | PARTIAL | 2 | Per-piece evidence names "the pathway step it supports" — so which steps have support is derivable. But the section does not require explicitly listing steps that lack evidence. The null case ("No context-specific evidence found. Tier: none.") is a summary verdict, not a per-step gap enumeration. Models can satisfy C-05 without satisfying C-13. |
| C-14 | AMEND conditioned on inertia finding | FAIL | 0 | AMEND structure has `Evidence quality` and `Pathway` fields but no `Inertia` field. The narrowed claim is conditioned on evidence tier and mechanism, not on the inertia finding. |
| **Total** | | | **105** | All essential: PASS |

---

### V-03: Competing pathways

| ID | Criterion | Verdict | Pts | Evidence Note |
|----|-----------|---------|-----|---------------|
| C-01 | Mechanism traced as pathway | PASS | 12 | PATHWAY A with three-part per-step instruction + minimum 3 steps. "X ships and metric improves is not a pathway." |
| C-02 | Falsification is mechanism break | PASS | 12 | FALSIFICATION CONDITIONS section requires per-pathway break: "Pathway A break: what step fails, observable as what?" Step-level reference to failure point. |
| C-03 | Inertia check performed | PASS | 12 | INERTIA CHECK section with Competing / Not competing / Unclear verdict + "If competing, which pathway does the status quo most resemble?" — ties inertia to pathway analysis. |
| C-04 | Causal claim narrowed in AMEND | PASS | 12 | AMEND has `Active pathway`, `Pathway summary`, `Falsification`, and `Amended` fields. Amended must be "conditioned on the active pathway, bounded by the inertia finding, and specific to the context where evidence is strongest." |
| C-05 | Context evidence assessed | PASS | 12 | Per-pathway evidence: "Name evidence per pathway -- do not combine. Which pathway has stronger contextual support?" |
| C-06 | Mechanism pathway is testable | PASS | 10 | Observable indicator per step in both Pathway A and B. |
| C-07 | Confounder or alternative cause | PARTIAL | 5 | Pathway B can be "a competing mechanism (another factor independently produces Y alongside X)" — but may also be a different X-to-Y chain (same cause, different intermediate). The structure makes alternative causes more likely to surface but does not guarantee it. PATHWAY COMPARISON asks for "Competing (only one correct)" vs "Complementary" — surfaces the distinction. No dedicated confounder instruction. |
| C-08 | AMEND output is actionable | PASS | 10 | "Conditioned on the active pathway, bounded by the inertia finding, and specific to the context where evidence is strongest" — three named constraint dimensions, each concrete. |
| C-09 | Evidence quality rated | FAIL | 0 | Not asked. No evidence tier scale. |
| C-10 | Multiple causal pathways considered | PASS | 5 | Two labeled pathways (A and B) required. PATHWAY COMPARISON section asks: relationship type (Complementary / Competing / Nested / Singular), most likely active, and whether independently falsifiable. Full C-10 coverage. |
| C-11 | Mechanism incompleteness acknowledged | FAIL | 0 | Pathway A section says "Minimum 3 steps" without a self-disclosure gate. No instruction to flag when 3 steps cannot be traced. "If no meaningful second pathway exists, say so" covers Pathway B incompleteness but not the primary pathway. |
| C-12 | Falsification break anchored to named step | FAIL | 0 | Pathway steps use prose format without step numbers or labels. Falsification refers to "Pathway A break: what step fails" — references the pathway but not a labeled step. No structural anchor available. |
| C-13 | Evidence gap localized to pathway steps | FAIL | 0 | Evidence section is pathway-level ("which pathway has stronger support"), not step-level. No per-step gap enumeration. |
| C-14 | AMEND conditioned on inertia finding | PASS | 5 | AMEND `Amended` field must be "bounded by the inertia finding" — explicitly required language. This is the only single-axis variation that fully passes C-14. The AMEND structure requires incorporating the inertia result into the narrowed claim. |
| **Total** | | | **95** | All essential: PASS |

---

### V-04: Incompleteness gate + step-anchored falsification

| ID | Criterion | Verdict | Pts | Evidence Note |
|----|-----------|---------|-----|---------------|
| C-01 | Mechanism traced as pathway | PASS | 12 | "Step N -- [Name]: What changes. Who acts. Observable indicator." format. Labeled steps required. [UNCERTAIN] tag for unsubstantiated steps. |
| C-02 | Falsification is mechanism break | PASS | 12 | Required format: "The mechanism fails if Step [N] -- [Name] -- does not occur, observable as [specific indicator]." Step number + label must match a labeled row in the pathway. Hard structural gate. |
| C-03 | Inertia check performed | PASS | 12 | === INERTIA CHECK === section with INERTIA STATUS: [Competing / Not competing / Unclear] format. |
| C-04 | Causal claim narrowed in AMEND | PASS | 12 | AMEND structure: `Mechanism complete / Inertia status / Pathway / Falsification / Amended`. "Amended: must include at least one: mechanism qualifier, scope condition, or inertia-conditioned framing." |
| C-05 | Context evidence assessed | PASS | 12 | "Which labeled steps in the pathway have no supporting evidence? List step numbers and names." — per-step gap accounting is explicitly required for C-05 in this variation. Frontmatter `evidence_gap_steps`. |
| C-06 | Mechanism pathway is testable | PASS | 10 | Observable indicator per labeled step. |
| C-07 | Confounder or alternative cause | FAIL | 0 | No dedicated confounder or alternative cause section. No AMEND field for alternative causes. The confounder/alternative axis was intentionally excluded from this two-axis combination (C-11 + C-12 only). |
| C-08 | AMEND output is actionable | PASS | 10 | "Must include at least one: mechanism qualifier, scope condition, or inertia-conditioned framing if status is Competing or Unclear." Named concrete forms. |
| C-09 | Evidence quality rated | FAIL | 0 | Evidence section asks for presence/absence and gap steps but no T1/T2/T3 quality scale. |
| C-10 | Multiple causal pathways considered | FAIL | 0 | Not asked. |
| C-11 | Mechanism incompleteness acknowledged | PASS | 5 | === MECHANISM READINESS CHECK === gate before tracing: "If no: write 'MECHANISM INCOMPLETE: [explain]' then continue with what can be traced, marking any step [UNCERTAIN]." + "A pathway that names 3 thin or vague steps to clear the threshold -- instead of flagging genuine uncertainty -- fails this check." Strongest C-11 structural enforcement of any variation. |
| C-12 | Falsification break anchored to named step | PASS | 5 | Labeled step format in pathway + "The step number and name must match a labeled row in the pathway above" in falsification + frontmatter `break_point_step: {step label}`. Full mechanical enforcement. |
| C-13 | Evidence gap localized to pathway steps | PASS | 5 | "Which labeled steps in the pathway have no supporting evidence? List step numbers and names." + frontmatter `evidence_gap_steps: [{step labels}]`. Per-step gap accounting explicitly required. |
| C-14 | AMEND conditioned on inertia finding | PARTIAL | 3 | AMEND includes `Inertia status: {from inertia check}` as a named field (inertia is always documented). Inertia-conditioned framing in the amended claim is required only when status is Competing or Unclear. When status is Not competing, AMEND can narrow without referencing inertia. C-14 does not exempt the "not competing" case — the narrowed claim should still be scoped to contexts where inertia was ruled out. Partial: inertia is documented but not universally incorporated into the amended claim text. |
| **Total** | | | **98** | All essential: PASS |

---

### V-05: Full aspirational stack

| ID | Criterion | Verdict | Pts | Evidence Note |
|----|-----------|---------|-----|---------------|
| C-01 | Mechanism traced as pathway | PASS | 12 | Phase 2 with "Step N -- [Name]: What changes. Who acts. Observable indicator." labeled format. |
| C-02 | Falsification is mechanism break | PASS | 12 | Phase 3 required format: "The mechanism fails if Step [N] -- [Name] -- does not occur, observable as [indicator]." Step number + name must match Phase 2. Do not state as metric threshold. |
| C-03 | Inertia check performed | PASS | 12 | Phase 0 INERTIA GATE — first phase before any mechanism work. INERTIA VERDICT required with Competing / Not competing / Unclear + one-sentence basis. "An assertion" is not acceptable. Front-loaded structural position maximizes compliance. |
| C-04 | Causal claim narrowed in AMEND | PASS | 12 | Phase 6 AMEND: `Original / Inertia verdict / Mechanism complete / Active pathway / Pathway / Falsification / Evidence gap / Amended`. "Restating is a failure mode. Broadening is a failure mode." Strongest AMEND instruction. |
| C-05 | Context evidence assessed | PASS | 12 | Phase 4: per-step evidence audit with T1/T2/T3 rating + explicit `Evidence gap steps: [list step numbers/names with no supporting evidence]`. Two required structured outputs. |
| C-06 | Mechanism pathway is testable | PASS | 10 | Observable indicator per labeled step in Phase 2. |
| C-07 | Confounder or alternative cause | PASS | 10 | Phase 5 CONFOUNDER CHECK: "Name at least one alternative explanation for Y that does not involve X and is not the inertia status quo." Explicitly distinguished from both inertia (Phase 0) and mechanism (Phase 2). "If none can be identified, explain why." |
| C-08 | AMEND output is actionable | PASS | 10 | AMEND `Amended` must include: (a) mechanism qualifier, (b) scope condition, (c) inertia condition if Competing or Unclear. Three named required components — the most constrained AMEND specification of all variations. |
| C-09 | Evidence quality rated | PASS | 5 | Phase 4 T1/T2/T3 scale: "T1 = anecdotal / observational / team intuition, T2 = correlation / A-B / usage analytics / survey, T3 = controlled / causal-inference-grade." Per-step rating + `Aggregate evidence tier` required output + frontmatter `evidence_aggregate_tier`. |
| C-10 | Multiple causal pathways considered | PASS | 5 | Phase 2 explicitly asks: "Is there more than one plausible causal pathway from X to Y?" If yes: trace primary + name secondary in one sentence + note relationship (complementary / competing / nested). If no: note mechanism is singular. Both outcomes are required responses. |
| C-11 | Mechanism incompleteness acknowledged | PASS | 5 | Phase 1 MECHANISM READINESS: "If no: declare incompleteness now. Write: 'PATHWAY INCOMPLETE: mechanism cannot be traced past [step]. Missing knowledge: [what is needed].' Then continue marking unsubstantiated steps [UNCERTAIN]." + "Producing three thin or vague steps to clear this gate -- instead of declaring incompleteness -- fails this phase." |
| C-12 | Falsification break anchored to named step | PASS | 5 | Phase 3 requires step number + name matching Phase 2 labeled rows. "[UNCERTAIN] steps may still serve as falsification anchors -- note uncertainty in the indicator." Even incomplete pathways produce gradeable falsification anchors. |
| C-13 | Evidence gap localized to pathway steps | PASS | 5 | Phase 4: "For each step in Phase 2: Step N -- [Name]: [evidence] -- [T1/T2/T3/none]" + "Evidence gap steps: [list step numbers/names with no supporting evidence]" as required output + frontmatter `evidence_gap_steps`. Per-step gap enumeration is structurally mandated. |
| C-14 | AMEND conditioned on inertia finding | PASS | 5 | Phase 6 AMEND `Inertia verdict` field (always documented) + Amended must include "(c) inertia condition if status is Competing or Unclear: 'in contexts where the status quo does not already [produce Y]' or 'invalid if inertia check shows [condition].'" + "A narrowed claim that ignores the inertia verdict does not pass." Combined: inertia is always present in AMEND structure and inertia-conditioned language is required for non-trivial findings. |
| **Total** | | | **120** | All essential: PASS |

---

### Rankings

| Rank | Variation | Score | All Essential Pass | Interpretation | Notes |
|------|-----------|-------|-------------------|----------------|-------|
| 1 | **V-05: Full aspirational stack** | **120** | YES | Golden (>= 110) | Only variation to hit ceiling; all C-07 through C-14 fully pass |
| 2 | **V-02: Evidence quality scale** | **105** | YES | Acceptable (95–109) | C-07 + C-09 + C-11 pass; C-12/C-13 partial due to unlabeled steps |
| 3 | **V-04: Incompleteness gate + step-anchored** | **98** | YES | Acceptable (95–109) | C-11/C-12/C-13 fully pass; C-07/C-09/C-10 out of scope by design |
| 4 | **V-01: Confounder section** | **95** | YES | Acceptable (95–109) | C-07 fully pass; C-11 pass; C-12/C-13/C-14 fail due to unlabeled steps |
| 5 | **V-03: Competing pathways** | **95** | YES | Acceptable (95–109) | C-10/C-14 pass; C-11/C-12/C-13 fail; C-07 partial |

All five variations pass all essential criteria. All five land in Acceptable or Golden range. None fall below bar.

---

### Score Deltas vs R1

| Variation | R1 Score (/100) | R2 Score (/120) | Delta | What changed |
|-----------|-----------------|-----------------|-------|-------------|
| V-01 (Confounder section) | 78* | 95 | +17 | C-07 now PASS (dedicated section); C-11 PASS (incompleteness instruction present) |
| V-02 (Evidence quality scale) | 78* | 105 | +27 | C-07 + C-09 + C-11 now pass; C-12/C-13 partial |
| V-03 (Competing pathways) | 79* | 95 | +16 | C-10 + C-14 now pass; C-07 partial; C-11 still fail |
| V-04 (Incompleteness gate) | 84* | 98 | +14 | C-11 + C-12 + C-13 now pass; C-14 partial |
| V-05 (Full aspirational stack) | 82* | 120 | +38 | All new criteria pass; ceiling variation |

*R1 variations are different prompts; comparison is conceptual (R1 best was V-04 at 84/100).

---

### Excellence Signals from V-05

**What made V-05 the ceiling variation:**

1. **Phase-ordered structure enables AMEND synthesis** — Each phase (0 through 5) produces a named output. Phase 6 AMEND explicitly requires incorporating every prior phase output by name. This makes C-14 mechanically enforceable: the inertia verdict cannot be ignored because it is a required AMEND field. The pattern is: structural slots in earlier phases + required-field references in AMEND = reliable integration. This generalizes beyond C-14 to any criterion that requires two outputs to be integrated.

2. **Labeled step format is a prerequisite for two criteria** — "Step N -- [Name]:" is not just a presentation choice; it enables C-12 (step-anchored falsification) and C-13 (per-step evidence gaps) to be gradeable at all. Without labeled steps, both criteria mechanically fail — there is no referent to anchor to. V-02 demonstrates this: evidence quality scale passes C-09 but only partially covers C-12/C-13 because steps are positional, not labeled. The implication: step labeling is a load-bearing structural choice, not an aesthetic one.

3. **Confounder separated from inertia by phase boundary** — Phase 5 CONFOUNDER CHECK explicitly says "does not involve X and is not the inertia status quo" — it carves out the exact space that R1 left uncovered (where inertia was the only named alternative). This design addresses the C-03/C-07 conflation at the prompt level rather than relying on the model to distinguish them.

4. **C-11 and C-12 are structurally coupled when step labeling is present** — Phase 1 (incompleteness gate) + Phase 2 (labeled steps) + Phase 3 (step-anchored falsification) form a dependency chain: if you declare incompleteness in Phase 1, you still label whatever steps you trace, and Phase 3 anchors falsification to one of those labeled steps. The mechanism either produces a named-step falsification or a principled gap statement. Both outcomes satisfy the rubric better than a vague pathway with a metric-threshold falsification.

5. **Per-step evidence accounting closes C-09/C-13 together** — Phase 4's per-step T1/T2/T3 audit with required `Evidence gap steps` output simultaneously satisfies C-09 (quality rated) and C-13 (gaps localized). The two criteria share the same structural requirement. V-02 gets C-09 without C-13 because it lacks the gap enumeration step.

---

```json
{"top_score": 120, "all_essential_pass": true, "new_patterns": ["phase-ordered structure with named phase outputs enables reliable AMEND integration: when each phase produces a named field that AMEND must reference, integration criteria (C-14) become mechanically enforceable rather than aspirational", "labeled step format (Step N -- Name) is a prerequisite for two criteria: C-12 and C-13 require a labeled referent to be gradeable at all -- positional steps (step 2) partially cover this, prose steps do not", "confounder and inertia must be separated by design: when confounders share a section with the inertia check, models satisfy C-03 while never naming a concurrently operating cause -- separate phases with explicit exclusion language ('is not the inertia status quo') closes this conflation", "C-11 and C-12 pass or fail together when step labeling is present: incompleteness gate + labeled steps + step-anchored falsification form a dependency chain where declaring incompleteness still produces a gradeable falsification anchor"]}
```
