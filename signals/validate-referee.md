You are running /validate-referee for: {{topic}}

Simulate journal-specific hostile peer review. validate-design uses generic disciplines — this skill knows the difference between a PNAS reviewer demanding effect sizes and a JCS reviewer wanting phenomenological grounding.

---

## PHASE 1 -- SIGNAL ACQUISITION

Glob: signals/**/{topic}-*
Read the paper or draft artifact. Extract: the central claim, the method, the key results, the target journal.

If no journal specified: infer from content style and ask for confirmation before proceeding.

---

## PHASE 2 -- REFEREE ASSIGNMENT

Based on the target journal, assign 3 referees with journal-specific archetypes:

**Journal profiles:**
- **PNAS / Nature / Science**: Referee 1 = sympathetic-rigorous (wants clean effect sizes, p < 0.05, large N); Referee 2 = hostile statistician (power analysis, multiple comparisons, replication); Referee 3 = breadth skeptic (is this general enough for a broad journal?)
- **Psychological Science / JEP**: Referee 1 = pre-registration enforcer; Referee 2 = effect-size pragmatist (d > 0.4 or why bother?); Referee 3 = ecological validity critic
- **Journal of Consciousness Studies / Phenomenology**: Referee 1 = sympathetic phenomenologist (internal consistency over empirical proof); Referee 2 = hard-nosed analytic philosopher (conceptual precision); Referee 3 = empirical skeptic (where's the data?)
- **Cognitive Science / Topics in Cognitive Science**: Referee 1 = computational modeler (is there a formal model?); Referee 2 = experimental psychologist (ecological validity, individual differences); Referee 3 = interdisciplinary enforcer (does it actually bridge the fields it claims to?)
- **NeurIPS / ICML / AI venues**: Referee 1 = benchmark enforcer (SOTA comparisons, ablations); Referee 2 = theory skeptic (where's the convergence proof?); Referee 3 = reproducibility checker (code, seeds, compute budget)

---

## PHASE 3 -- THREE REFEREE REPORTS

For each referee, produce a report in the journal's actual format:

```
REFEREE [N] — [archetype]
Recommendation: Accept / Major Revision / Minor Revision / Reject

SUMMARY:
[2-3 sentences: what the paper does and the referee's overall reaction]

MAJOR CONCERNS:
1. [Specific, citable concern — name the gap, the missing analysis, the logical flaw]
2. [...]
3. [...]

MINOR CONCERNS:
1. [Presentation, framing, missing citations]
2. [...]

SPECIFIC COMMENTS:
Line X: [exact issue]
[...]
```

Enforce journal standards ruthlessly:
- PNAS: "Effect size d = X is not reported. Without this, the practical significance of the finding cannot be assessed."
- JCS: "The phenomenological analysis in §3 conflates first-person and third-person descriptions without acknowledging this move."
- Cognitive Science: "The computational model in Figure 2 is described but never formally specified. What are the free parameters?"

---

## PHASE 4 -- VERDICT

```
Journal: [name]
Likely decision: ACCEPT / MAJOR REVISION / MINOR REVISION / REJECT
Confidence: HIGH / MEDIUM (depends on referee 2's weight at this journal)

P1 blockers (reject conditions):
  [What would cause outright rejection — must fix before resubmission]

P2 conditions (major revision requirements):
  [What all 3 referees flagged — consensus issues are hardest to dismiss]

Strongest referee: Referee [N] — their objections carry most weight because [reason]
```

---

## PHASE 5 -- AMEND

Three targeted pre-submission fixes ordered by blocking severity:
1. [Fix that addresses the most likely reject condition]
2. [Fix that addresses the consensus P2 across referees]
3. [Fix that addresses the journal's specific formatting/evidence standard]

Write artifact to: signals/validate/referee/{{topic}}-referee-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: validate-referee, topic: {{topic}}, date: {{date}}, journal: [journal name], verdict: likely-accept|major-revision|reject
