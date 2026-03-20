---
name: validate-referee
description: "Journal-specific hostile peer review. 3 referees drawn from the target journal's archetype pool (PNAS/JCS/CogSci/etc). Continuous I-NN issue IDs. P1/P2 blocking severity in verdict."
allowed-tools: [Read, Write, Glob]
param_set: lean
---
depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure


You are running /validate-referee for: {{topic}}

Simulate journal-specific hostile peer review. Three referees drawn from the target journal's archetype pool. Issue IDs continuous across all three reports.

---

## PHASE 1 -- SIGNAL ACQUISITION

Glob: signals/**/{topic}-*
Read the paper or draft artifact. Extract: the central claim, the method, the key results.
Identify the target journal. If not specified, infer from content style and confirm before proceeding.

---

## PHASE 2 -- REFEREE ASSIGNMENT

Select 3 referee archetypes from the target journal's pool:

- **PNAS / Nature / Science**: R1 = sympathetic-rigorous (effect sizes, large N); R2 = hostile statistician (power analysis, multiple comparisons); R3 = breadth skeptic (too narrow for a broad journal?)
- **Psychological Science / JEP**: R1 = pre-registration enforcer; R2 = effect-size pragmatist (d > 0.4?); R3 = ecological validity critic
- **Journal of Consciousness Studies / Phenomenology**: R1 = sympathetic phenomenologist (internal consistency over proof); R2 = hard-nosed analytic philosopher (conceptual precision); R3 = empirical skeptic
- **Cognitive Science / Topics in Cognitive Science**: R1 = computational modeler (where's the formal model?); R2 = experimental psychologist (ecological validity, N); R3 = interdisciplinary enforcer
- **NeurIPS / ICML / AI venues**: R1 = benchmark enforcer (SOTA, ablations); R2 = theory skeptic (convergence proof?); R3 = reproducibility checker (code, seeds, compute)

Before writing reports: commit which referee is most likely to diverge (recommend Reject while others recommend Revision) and state why.

---

## PHASE 3 -- THREE REFEREE REPORTS

Issue IDs are continuous across all three reports (I-01, I-02, ..., I-N). Do not reset per referee.

For each referee, produce:

```
REFEREE [N] -- [archetype]
Recommendation: Accept / Major Revision / Minor Revision / Reject

SUMMARY: [2-3 sentences: what the paper does and this referee's overall reaction]

MAJOR CONCERNS:
[I-NN] [Specific, citable -- "Effect size d is not reported in Table 2; practical significance cannot be assessed"]
[I-NN] [...]

MINOR CONCERNS:
1. [Presentation, framing, missing citations]

SPECIFIC COMMENTS:
Line X: [exact issue]
```

Enforce journal standards:
- PNAS: FORBIDDEN: "The finding is interesting." REQUIRED: "Effect size d = [value] is not reported; practical significance cannot be assessed."
- JCS: FORBIDDEN: vague appeals to consciousness. REQUIRED: name the specific phenomenological structure being invoked.
- Cognitive Science: FORBIDDEN: informal model description. REQUIRED: "The model is described but not formally specified — free parameters are undefined."

---

## PHASE 4 -- FINAL VERDICT

```
Journal: [name]
Likely decision: ACCEPT / MAJOR REVISION / MINOR REVISION / REJECT
Confidence: HIGH / MEDIUM

P1 blockers (reject conditions): Issues: I-[NN], I-[NN]
P2 conditions (major revision): Issues: I-[NN], I-[NN]
Strongest referee: Referee [N] -- [reason this referee's objections carry most weight at this journal]
```

---

## PHASE 5 -- AMEND

Three targeted pre-submission fixes ordered by blocking severity:
1. [Fix that addresses the most likely reject condition — I-[NN]]
2. [Fix that addresses the consensus P2 across referees]
3. [Fix that addresses the journal's specific formatting or evidence standard]

Write artifact to: signals/validate/referee/{{topic}}-referee-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: validate-referee, topic: {{topic}}, date: {{date}}, journal: [journal name], verdict: likely-accept|major-revision|reject
