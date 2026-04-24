---

## QU5 Simplification Report — validate-referee

### Simplified Prompt Body

```
You are running /validate-referee for: {{topic}}

Simulate journal-specific hostile peer review.

---

### PHASE 1 -- SIGNAL ACQUISITION

Glob: signals/**/{topic}-*
Read the artifact. Extract: central claim, method, key results, target journal.
If no journal specified: infer from content style and confirm before proceeding.

---

### PHASE 2 -- REFEREE ASSIGNMENT

Assign 3 referees.

**Journal profiles:**
- **PNAS / Nature / Science**: R1 = sympathetic-rigorous (effect sizes, p < 0.05, large N); R2 = hostile statistician (power analysis, multiple comparisons, replication); R3 = breadth skeptic
- **Psychological Science / JEP**: R1 = pre-registration enforcer; R2 = effect-size pragmatist (d > 0.4 or why bother?); R3 = ecological validity critic
- **Journal of Consciousness Studies / Phenomenology**: R1 = sympathetic phenomenologist; R2 = hard-nosed analytic philosopher; R3 = empirical skeptic
- **Cognitive Science / Topics in Cognitive Science**: R1 = computational modeler; R2 = experimental psychologist; R3 = interdisciplinary enforcer
- **NeurIPS / ICML / AI venues**: R1 = benchmark enforcer; R2 = theory skeptic; R3 = reproducibility checker

---

### PHASE 3 -- THREE REFEREE REPORTS

For each referee, write a report with issue IDs on every Major Concern.

```
REFEREE [N] -- [archetype]
Recommendation: Accept / Major Revision / Minor Revision / Reject

SUMMARY: [2-3 sentences]

MAJOR CONCERNS:
[I-NN] [Specific, citable -- "Effect size d is not reported in Table 2; practical significance cannot be assessed"]
[I-NN] [...]

MINOR CONCERNS:
1. [...]

SPECIFIC COMMENTS:
Line X: [exact issue]
```

IDs continuous across all three reports.

---

### PHASE 4 -- FINAL VERDICT

```
Journal: [name]
Likely decision: ACCEPT / MAJOR REVISION / MINOR REVISION / REJECT
Confidence: HIGH / MEDIUM

P1 blockers: Issues: I-[NN], I-[NN]
P2 conditions: Issues: I-[NN], I-[NN]
Strongest referee: Referee [N] -- [reason]
```

---

Write artifact to: signals/validate/referee/{{topic}}-referee-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Frontmatter: skill: validate-referee, topic: {{topic}}, date: {{date}}, journal: [journal name], verdict: likely-accept|major-revision|reject
```

---

### What Was Removed and Why

The entire 75-point aspirational superstructure — every word was serving a non-essential criterion:

| Removed | Words | Criterion served |
|---------|-------|-----------------|
| PHASE 2 DIVERGENCE COMMITMENT | ~140 | C-09, C-10, C-11, C-14 (all aspirational) |
| FORBIDDEN/REQUIRED brief examples + self-verifications | ~193 | C-13, C-14, C-16, C-17 |
| FORBIDDEN/REQUIRED Phase 5 rationale + self-verification | ~96 | C-15, C-16, C-17 |
| FORBIDDEN/REQUIRED Done When + self-verification | ~121 | C-12, C-16, C-17 |
| Issue Registry table + Fix Plan + Severity | ~110 | C-08, C-12 |
| Journal standards enforced block | ~60 | C-08 |
| Intro meta-clause about validate-design | ~18 | None |
| Various cleanup (labels, redundant clauses) | ~229 | Cosmetic / redundant |

### Essential Criteria Verification: YES

All five essential criteria (C-01 through C-05) pass with the simplified prompt. The journal profiles table is the only non-trivial retained content beyond the bare templates.

---

```json
{"simplified_word_count": 284, "original_word_count": 1251, "all_essential_still_pass": true}
```
