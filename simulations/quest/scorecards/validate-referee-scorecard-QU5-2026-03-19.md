# validate-referee — QU5 Simplification Pass

**Date**: 2026-03-19
**Source**: V-05 R5 (canonical production form, 135/135)
**Task**: Find minimal prompt that passes all essential rubric criteria (C-01 through C-05 = 60 pts)

---

## Essential Criteria

| ID | Criterion | Points |
|----|-----------|--------|
| C-01 | Three referee reports, each with Summary + Major/Minor Concerns + Specific Comments + Recommendation | 25 |
| C-02 | Each referee archetype matches the target journal's built-in profile | 15 |
| C-03 | Final verdict block with all required fields | 10 |
| C-04 | Each Major Concern is specific and citable (not vague) | 5 |
| C-05 | Artifact written to correct path with correct frontmatter | 5 |
| **Total** | | **60** |

---

## Simplification Analysis: What Is Doing No Work for C-01–C-05

### Removed entirely

| Section | Approx words | Criterion served | Why removable |
|---------|-------------|------------------|---------------|
| Intro clause: "This skill knows PNAS reviewers from JCS reviewers; validate-design uses generic disciplines, this skill does not." | 18 | None | Meta-comment about another skill; not operational |
| PHASE 2 — DIVERGENCE COMMITMENT (full block + post-block enforcement) | 140 | C-09, C-10, C-11, C-14 (all aspirational) | Divergence prediction not in essential criteria |
| "The Phase 2 archetype must appear as one of the three." | 11 | C-11 | Consequent of Phase 2; gone with it |
| Non-diverger character brief format box | 23 | C-13 (aspirational) | Character briefs not in C-01 |
| FORBIDDEN brief example + label | 39 | C-13, C-17 (both aspirational) | Not needed for essential output format |
| REQUIRED brief example + label | 68 | C-13, C-17 | Same |
| Self-verification: brief load-bearing test | 35 | C-16 (aspirational) | Removal tests are aspirational |
| Diverger SEED/EXPAND format box | 36 | C-14 (aspirational) | Not in essential criteria |
| FORBIDDEN new-premise EXPAND setup + example | 67 | C-14, C-17 | Aspirational |
| REQUIRED EXPAND example | 52 | C-14, C-17 | Aspirational |
| Self-verification: EXPAND depends on SEED | 21 | C-16 | Aspirational |
| "Diverges from Phase 2: YES / NO" in report template | 6 | C-09/C-10 | Phase 2 removed |
| SUMMARY brief-voice / EXPAND-framing note | 8 | C-13/C-14 | Aspirational |
| Journal standards enforced block (3 lines) | 60 | C-08 (recommended, not essential) | Not in C-01–C-05 |
| "Divergence check" line in Phase 5 template | 16 | C-09/C-10 | Phase 2 removed |
| "(reject conditions)" / "(major revision requirements)" labels | 8 | Cosmetic | Not load-bearing |
| FORBIDDEN rationale (Phase 5) + label | 28 | C-15, C-17 (both aspirational) | Not in essential criteria |
| REQUIRED rationale (Phase 5) + label | 43 | C-15, C-17 | Aspirational |
| Self-verification: Phase 5 rationale grounded in brief | 25 | C-16 | Aspirational |
| FORBIDDEN Done When + label | 34 | C-12, C-17 (both aspirational) | Not in essential criteria |
| REQUIRED Done When + label | 50 | C-12, C-17 | Aspirational |
| Self-verification: Done When threshold | 37 | C-16 | Aspirational |
| Issue Registry table + Severity definitions | 32 | C-12 (aspirational) | Not in C-01–C-05 |
| "or maps to P1 blocker" from severity | 5 | C-12 | Aspirational |
| Ordered Fix Plan (Fix 1/2/3) | 78 | C-08 (recommended) | Not in C-01–C-05 |
| Inline example in Fix 1 Action/Done-when | 39 | C-08, C-12 | Not essential |
| "[Journal-specific formatting or evidence standard]" | 6 | C-08 | Recommended |
| "Include" from "Include frontmatter:" | 1 | Cosmetic | — |

### Simplified (not removed, just compressed)

| Original | Simplified | Words saved |
|----------|------------|-------------|
| "Assign 3 referees with journal-specific archetypes." | "Assign 3 referees." | 4 |
| "Strongest referee: Referee [N] -- their objections carry most weight because [cite a specific fact from their character brief or EXPAND -- reviewing history, not journal policy]" | "Strongest referee: Referee [N] -- [reason]" | 19 |
| Full intro: "Simulate journal-specific hostile peer review. This skill knows PNAS…" | "Simulate journal-specific hostile peer review." | 18 |

**Total removed or simplified: ~967 words**

---

## Simplified Prompt Body

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

## Essential Criteria Verification

| ID | Criterion | Passes? | Evidence in simplified prompt |
|----|-----------|---------|-------------------------------|
| C-01 | Three reports with all required sections | **YES** | Phase 3 template: Recommendation, Summary, Major Concerns (with I-NN IDs), Minor Concerns, Specific Comments |
| C-02 | Journal-specific archetype matching | **YES** | Phase 2 five-journal profile table retained in full |
| C-03 | Final verdict block with required fields | **YES** | Phase 4 template: decision, confidence, P1 blockers, P2 conditions, strongest referee |
| C-04 | Specific, citable Major Concerns | **YES** | Template example: "[Specific, citable -- 'Effect size d is not reported in Table 2; practical significance cannot be assessed']" |
| C-05 | Artifact at correct path with frontmatter | **YES** | Write instruction, exact path, all frontmatter fields named |

**All essential criteria pass: YES**

---

## Word Count

| Version | Words |
|---------|-------|
| V-05 R5 original | 1,251 |
| Simplified (QU5) | 284 |
| Reduction | 77% |

---

## What the Simplified Version Loses

The simplified version passes C-01–C-05 (60 pts) but will score near-zero on all aspirational criteria:

| Lost | Criteria | Points at stake |
|------|----------|-----------------|
| Divergence commitment + minority dissent enforcement | C-09, C-10, C-11 | 10 + 5 = 15 |
| Character brief event-grounding + SEED/EXPAND chain | C-13, C-14 | 5 + 5 = 10 |
| Verifiable Done When in Issue Registry | C-12 | 5 |
| Strongest-referee rationale grounded in brief | C-15 | 5 |
| Self-verification removal tests | C-16 | 5 |
| FORBIDDEN in-situ vaccination examples | C-17 | 5 |
| Journal standards enforced / fix plan ordering | C-06, C-07, C-08 | 30 |
| **Total aspirational lost** | | **75 pts** |

**The full V-05 R5 prompt is the deployment target.** The simplified version is the essential skeleton — 284 words that define the irreducible core. The remaining 967 words in V-05 R5 are the 75-point aspirational superstructure, and every word earns its place.

---

```json
{"simplified_word_count": 284, "original_word_count": 1251, "all_essential_still_pass": true}
```
