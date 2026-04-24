R5 variations written to `simulations/quest/variations/validate-referee-variations-R5-2026-03-19.md`.

---

## Summary

**Ceiling**: 135 (v4 rubric — unchanged). Round 5 is a production-fitness round. V-05 R4 hit 135/135; no new criteria emerge. The five variations probe whether different structural arrangements of the same enforcement chain maintain compliance.

### Variation map

| ID | Axis | Prediction |
|----|------|------------|
| **V-01 R5** | Compression | 135/135 — mechanisms intact, overhead stripped |
| **V-02 R5** | Front-loaded enforcement preamble | 131–133 — C-17 partial miss: in-situ placement likely load-bearing for Phase 4 and Phase 6 FORBIDDEN vaccination |
| **V-03 R5** | REQUIRED-first ordering (inverts every pair) | 134–135 — ordering is probably not the load-bearing feature; slight risk of C-17 reduction |
| **V-04 R5** | Phase-end INTEGRITY CHECK blocks | 133–135 — C-16 risk if removal-test timing matters; C-17 intact since FORBIDDEN stays in-phase |
| **V-05 R5** | Canonical production form (clean editorial pass of V-05 R4) | 135/135 — deployment candidate |

**Key experimental question**: V-02 is the decisive test. If its C-17 score drops below 5/5, it confirms that FORBIDDEN examples require spatial proximity to the failure-triggering instruction — the label and the location are both necessary, and a front-loaded gallery is not equivalent to in-situ vaccination.
ests and C-17 references collected into per-phase "INTEGRITY CHECK" blocks at the end of each phase, rather than inline with instructions | Tests whether end-of-phase collocation vs inline enforcement differs for C-16 |
| **V-05 R5** | Canonical production form | V-05 R4 with clean editorial pass — consistent FORBIDDEN typography, unified removal-test verb, normalized phase headers, no redundant commentary | Deployment candidate |

**Key design question for R5**: Do the C-17 FORBIDDEN examples require spatial proximity to the failure site (in-situ) to vaccinate effectively, or can front-loading them in a preamble produce equal compliance? V-02 is the critical test: if it scores below 135 on C-17, in-situ placement is the load-bearing feature, not just the presence of the FORBIDDEN label.

---

## V-01 R5 -- Compression: Full Mechanisms, Minimum Overhead

**Axis**: Compression -- V-05 R4 mechanics with minimum prose overhead
**Hypothesis**: The enforcement mechanisms in V-05 R4 are the load-bearing elements; the surrounding commentary is not. Removing phase-level framing prose, explanatory sentences that restate what the instruction already says, and redundant reminders -- while preserving every FORBIDDEN/REQUIRED pair and every removal-form test verbatim -- should produce 135/135 with approximately 30% fewer tokens. Shorter prompts reduce generation overhead without reducing compliance when the mechanisms are intact.

---

You are running /validate-referee for: {{topic}}

Simulate journal-specific hostile peer review. This skill knows PNAS reviewers from JCS reviewers; validate-design uses generic disciplines, this skill does not.

---

### PHASE 1 -- SIGNAL ACQUISITION

Glob: signals/**/{topic}-*
Read the artifact. Extract: central claim, method, key results, target journal.
If no journal specified: infer from content style and confirm before proceeding.

---

### PHASE 2 -- DIVERGENCE COMMITMENT

Lock the structural minority view before naming referees:

```
DIVERGENCE COMMITMENT (locked before Phase 3)
Journal: [name]
Predicted diverger archetype: [from this journal's pool]
Direction: [more hostile / more sympathetic than the other two]
Reason: [one sentence -- what in this paper triggers this archetype specifically]
Experiential sketch: [one sentence -- the reviewing history that primes this archetype to diverge]
Brief anchor: "[Experiential sketch copied verbatim, inside quotes -- this exact sentence becomes SEED in Phase 4]"
```

Brief anchor is a structural output. Phase 4 diverger brief must open with SEED: [this sentence]. If SEED does not match Brief anchor, C-14 fails. At least two distinct recommendation levels required. Convergence is a simulation failure.

---

### PHASE 3 -- REFEREE ASSIGNMENT

Assign 3 referees. Phase 2 archetype must appear as one of the three.

**Journal profiles:**
- **PNAS / Nature / Science**: R1 = sympathetic-rigorous (effect sizes, p < 0.05, large N); R2 = hostile statistician (power analysis, multiple comparisons, replication); R3 = breadth skeptic
- **Psychological Science / JEP**: R1 = pre-registration enforcer; R2 = effect-size pragmatist (d > 0.4 or why bother?); R3 = ecological validity critic
- **Journal of Consciousness Studies**: R1 = sympathetic phenomenologist; R2 = hard-nosed analytic philosopher; R3 = empirical skeptic
- **Cognitive Science / Topics in Cognitive Science**: R1 = computational modeler; R2 = experimental psychologist; R3 = interdisciplinary enforcer
- **NeurIPS / ICML / AI venues**: R1 = benchmark enforcer; R2 = theory skeptic; R3 = reproducibility checker

---

### PHASE 4 -- THREE REFEREE REPORTS

For each referee: write a character brief, then the report with in-flight issue IDs on every Major Concern.

**Non-diverger brief format:**

```
Referee [N] -- [archetype] -- Character Brief
[2-3 sentences: a specific recent event that makes this referee's response to this paper's features predictable. Not a label plus a disposition -- an event.]
```

**FORBIDDEN** (disposition form -- fails C-13):
> "Referee 1 is a pre-registration enforcer who values methodological transparency. They have a long history of flagging papers that lack pre-registered hypotheses and routinely request that authors share their data."

**REQUIRED** (event form -- passes C-13):
> "Referee 1 co-authored the 2023 replication of a widely-cited priming study that failed to reproduce -- the original had no pre-registration and the analysis appeared tailored to the significant result. Since then they treat any paper without pre-registration as one where the reported hypotheses may not be the original hypotheses, and they ask for OSF links in every review they write."

Self-verification: drop the brief; if at least one Major Concern below it would be phrased identically without it, the brief is not load-bearing -- rewrite.

**Diverger brief format (SEED/EXPAND required):**

```
Referee [N] -- [archetype] -- Character Brief
SEED: [Phase 2 Brief anchor copied verbatim -- must match exactly]
EXPAND: [2-3 sentences derived from SEED -- how does that history produce the Phase 2 divergence direction?]
```

**FORBIDDEN** (new-premise EXPAND -- fails C-14):
If SEED = "After reviewing three high-profile replication failures at PNAS in 2024, this reviewer treats any N < 200 study as presumptively underpowered until a prospective power analysis appears."
> "This reviewer also brings expertise from clinical trial design, where power analysis is a prerequisite for IRB approval, giving them a practical rather than theoretical objection to underpowered studies."

**REQUIRED** EXPAND:
> "With that track record, this reviewer will read the N=87 in Section 3 as a pattern they have seen before -- their minority position pushes harder on power analysis specifically because they have personally documented this failure mode three times in the past year."

Self-verification: drop SEED; if EXPAND still stands alone, it introduced a new premise -- rewrite EXPAND so it depends on SEED.

```
REFEREE [N] -- [archetype]
Recommendation: Accept / Major Revision / Minor Revision / Reject
Diverges from Phase 2: YES / NO -- [confirm direction or consensus]

SUMMARY: [2-3 sentences -- voice audible from brief; diverger's EXPAND legible in concern framing]

MAJOR CONCERNS:
[I-NN] [Specific, citable -- "Effect size d is not reported in Table 2; practical significance cannot be assessed"]
[I-NN] [...]

MINOR CONCERNS:
1. [...]

SPECIFIC COMMENTS:
Line X: [exact issue]
```

IDs continuous across all three reports. Journal standards:
- PNAS: "Effect size d is not reported. Practical significance cannot be assessed."
- JCS: "Section 3 conflates first-person and third-person descriptions without acknowledging this."
- Cognitive Science: "The computational model is never formally specified. What are the free parameters?"

---

### PHASE 5 -- FINAL VERDICT

```
Journal: [name]
Likely decision: ACCEPT / MAJOR REVISION / MINOR REVISION / REJECT
Confidence: HIGH / MEDIUM

Divergence check: [Did the locked diverger diverge as predicted?]

P1 blockers: Issues: I-[NN], I-[NN]
P2 conditions: Issues: I-[NN], I-[NN]
Strongest referee: Referee [N] -- their objections carry most weight because [cite specific fact from their character brief -- reviewing history, not journal policy]
```

**FORBIDDEN** (policy form -- fails C-15):
> "Referee 2's statistical objections carry most weight because PNAS editors routinely desk-reject on power analysis grounds."

**REQUIRED** (persona form -- passes C-15):
> "Referee 2's objections carry most weight because, as their EXPAND notes, [specific experience from SEED/EXPAND] -- this reviewer's pattern makes them structurally less dismissible than journal policy would suggest."

Self-verification: drop all character briefs; if this rationale is still legible, rewrite it so it depends on a specific fact from the brief.

---

### PHASE 6 -- ISSUE REGISTRY + ORDERED FIX PLAN

**Issue Registry** -- quote exact concern language from Phase 4; do not paraphrase.

| ID | Source | Concern (exact quote) | Severity | Done When |
|----|--------|-----------------------|----------|-----------|
| I-01 | R[N] | "[exact quoted concern]" | P1/P2/P3 | [verifiable criterion] |

Severity: P1 = reject condition; P2 = consensus (2+ referees); P3 = single-referee non-fatal

**FORBIDDEN** (vague Done When -- fails C-12):
> "Done when the authors have addressed the statistical power concern and provided evidence that the sample is adequate."

**REQUIRED** (specific Done When -- passes C-12):
> "Done when Table 2 reports Cohen's d with 95% CI for all three primary effects AND Supplementary S1 contains a prospective power analysis showing N=87 achieves >= 80% power for d >= 0.35 at alpha = 0.05."

Self-verification: drop the specific table number, section identifier, or threshold; if the remaining text is still a complete criterion, rewrite to name at least one specific artifact and one measurable threshold.

**Ordered Fix Plan:**

**Fix 1 -- [P1 blocker title]**
Addresses: I-[NN], I-[NN]
Action: [Specific]
Done when: [Verifiable]

**Fix 2 -- [P2 consensus title]**
Addresses: I-[NN]
Action: [Specific]
Done when: [Verifiable]

**Fix 3 -- [Journal standard]**
Addresses: I-[NN]
Action: [Specific]
Done when: [Verifiable]

Write artifact to: signals/validate/referee/{{topic}}-referee-{{date}}.md
If --output <path> provided: write flat into <path>/
Frontmatter: skill: validate-referee, topic: {{topic}}, date: {{date}}, journal: [journal name], verdict: likely-accept|major-revision|reject

---

## V-02 R5 -- Front-Loaded Enforcement: Unified Structural Integrity Preamble

**Axis**: Front-loaded enforcement -- all FORBIDDEN examples and removal tests extracted to a single preamble block; phases execute without re-stating the rules
**Hypothesis**: V-05 R4 distributes C-16 and C-17 instructions across phases, placing them proximate to each failure site. This variation consolidates all enforcement into a STRUCTURAL INTEGRITY RULES block at the top. Each phase references the relevant rule numbers but does not re-state FORBIDDEN examples or removal tests inline. If C-17 FORBIDDEN vaccination requires spatial proximity to the failure site to activate before the wrong default is generated, front-loading will fail -- abstract briefs and new-premise EXPANDs will appear because the model encounters the instruction before it encounters the FORBIDDEN label. Predicts C-17 partial miss (3/5): Phase 5 rationale FORBIDDEN (well-internalized across rounds) will hold; Phase 4 and Phase 6 locations will be less reliably blocked when their FORBIDDEN examples are not in-situ.

---

You are running /validate-referee for: {{topic}}

Simulate journal-specific hostile peer review. This skill knows PNAS reviewers from JCS reviewers.

---

## STRUCTURAL INTEGRITY RULES

These rules apply throughout. Phases reference them by number.

**RULE 1 -- Non-diverger character briefs (Phase 4)**

FORBIDDEN (disposition form):
> "Referee 1 is a pre-registration enforcer who values methodological transparency. They have a long history of flagging papers that lack pre-registered hypotheses and routinely request that authors share their data."

REQUIRED (event form):
> "Referee 1 co-authored the 2023 replication of a widely-cited priming study that failed to reproduce -- the original had no pre-registration and the analysis appeared tailored to the significant result. Since then they treat any paper without pre-registration as one where the reported hypotheses may not be the original hypotheses, and they ask for OSF links in every review they write."

Removal test: drop the brief; would at least one Major Concern below it be phrased or weighted differently without it? If no, rewrite so the report depends on it.

**RULE 2 -- EXPAND in diverger brief (Phase 4)**

FORBIDDEN (new-premise EXPAND):
If SEED = "After reviewing three high-profile replication failures at PNAS in 2024, this reviewer treats any N < 200 study as presumptively underpowered until a prospective power analysis appears."
> "This reviewer also brings expertise from clinical trial design, where power analysis is a prerequisite for IRB approval."

REQUIRED EXPAND:
> "With that track record, this reviewer will read the N=87 in Section 3 as a pattern they have seen before -- their minority position pushes harder on power analysis specifically because they have personally documented this failure mode three times in the past year."

Removal test: drop SEED; if EXPAND stands alone, it introduced a new premise -- rewrite EXPAND so it depends on SEED.

**RULE 3 -- Done When criteria (Phase 6)**

FORBIDDEN (vague form):
> "Done when the authors have addressed the statistical power concern and provided evidence that the sample is adequate."

REQUIRED (specific form):
> "Done when Table 2 reports Cohen's d with 95% CI for all three primary effects AND Supplementary S1 contains a prospective power analysis showing N=87 achieves >= 80% power for d >= 0.35 at alpha = 0.05."

Removal test: drop the specific table number, section identifier, or threshold; if remaining text is still a complete criterion, rewrite to name at least one specific artifact and one measurable threshold.

**RULE 4 -- Strongest-referee rationale (Phase 5)**

FORBIDDEN (policy form):
> "Referee 2's objections carry most weight because PNAS editors routinely desk-reject on power analysis grounds."

REQUIRED (persona form):
> "Referee 2's objections carry most weight because, as their EXPAND notes, [specific experience from SEED/EXPAND] -- this reviewer's pattern makes them structurally less dismissible than journal policy would suggest."

Removal test: drop all character briefs; if this rationale is still legible, rewrite it so it depends on a specific fact from the brief.

---

### PHASE 1 -- SIGNAL ACQUISITION

Glob: signals/**/{topic}-*
Read the artifact. Extract: central claim, method, key results, target journal.
If no journal specified: infer and confirm.

---

### PHASE 2 -- DIVERGENCE COMMITMENT

```
DIVERGENCE COMMITMENT (locked before Phase 3)
Journal: [name]
Predicted diverger archetype: [from this journal's pool]
Direction: [more hostile / more sympathetic]
Reason: [one sentence]
Experiential sketch: [one sentence -- reviewing history that primes divergence]
Brief anchor: "[Experiential sketch verbatim, inside quotes -- becomes SEED in Phase 4]"
```

Brief anchor is structural. Phase 4 diverger brief must open with SEED: [this sentence]. Two distinct recommendation levels required. Convergence is a simulation failure.

---

### PHASE 3 -- REFEREE ASSIGNMENT

Assign 3 referees. Phase 2 archetype must appear as one of the three.

**Journal profiles:**
- **PNAS / Nature / Science**: R1 = sympathetic-rigorous; R2 = hostile statistician; R3 = breadth skeptic
- **Psychological Science / JEP**: R1 = pre-registration enforcer; R2 = effect-size pragmatist; R3 = ecological validity critic
- **Journal of Consciousness Studies**: R1 = sympathetic phenomenologist; R2 = hard-nosed analytic philosopher; R3 = empirical skeptic
- **Cognitive Science / Topics in Cognitive Science**: R1 = computational modeler; R2 = experimental psychologist; R3 = interdisciplinary enforcer
- **NeurIPS / ICML / AI venues**: R1 = benchmark enforcer; R2 = theory skeptic; R3 = reproducibility checker

---

### PHASE 4 -- THREE REFEREE REPORTS

Apply RULE 1 (non-diverger briefs) and RULE 2 (EXPAND) from STRUCTURAL INTEGRITY RULES above.

For non-diverger referees: write a character brief per RULE 1, then the report.
For the diverger: write a SEED/EXPAND brief per RULE 2, then the report.

```
Referee [N] -- [archetype] -- Character Brief
[Brief per applicable rule]

REFEREE [N] -- [archetype]
Recommendation: Accept / Major Revision / Minor Revision / Reject
Diverges from Phase 2: YES / NO

SUMMARY: [2-3 sentences]

MAJOR CONCERNS:
[I-NN] [Specific, citable]
[I-NN] [...]

MINOR CONCERNS:
1. [...]

SPECIFIC COMMENTS:
Line X: [exact issue]
```

IDs continuous across all three reports. Journal standards:
- PNAS: "Effect size d is not reported. Practical significance cannot be assessed."
- JCS: "Section 3 conflates first-person and third-person descriptions."
- Cognitive Science: "The computational model is never formally specified. What are the free parameters?"

---

### PHASE 5 -- FINAL VERDICT

Apply RULE 4 from STRUCTURAL INTEGRITY RULES.

```
Journal: [name]
Likely decision: ACCEPT / MAJOR REVISION / MINOR REVISION / REJECT
Confidence: HIGH / MEDIUM

Divergence check: [Did the locked diverger diverge as predicted?]

P1 blockers: Issues: I-[NN], I-[NN]
P2 conditions: Issues: I-[NN], I-[NN]
Strongest referee: Referee [N] -- their objections carry most weight because [persona form per RULE 4]
```

---

### PHASE 6 -- ISSUE REGISTRY + ORDERED FIX PLAN

Apply RULE 3 (Done When) from STRUCTURAL INTEGRITY RULES.

**Issue Registry:**

| ID | Source | Concern (exact quote) | Severity | Done When |
|----|--------|-----------------------|----------|-----------|
| I-01 | R[N] | "[exact quoted concern]" | P1/P2/P3 | [specific criterion per RULE 3] |

Severity: P1 = reject; P2 = consensus; P3 = single-referee non-fatal

**Ordered Fix Plan:**

**Fix 1 -- [P1 blocker title]**
Addresses: I-[NN]
Action: [Specific]
Done when: [Verifiable per RULE 3]

**Fix 2 -- [P2 consensus title]**
Addresses: I-[NN]
Action: [Specific]
Done when: [Verifiable]

**Fix 3 -- [Journal standard]**
Addresses: I-[NN]
Action: [Specific]
Done when: [Verifiable]

Write artifact to: signals/validate/referee/{{topic}}-referee-{{date}}.md
Frontmatter: skill: validate-referee, topic: {{topic}}, date: {{date}}, journal: [journal name], verdict: likely-accept|major-revision|reject

---

## V-03 R5 -- REQUIRED-First Ordering: Correct Form Shown Before FORBIDDEN

**Axis**: Ordering inversion -- every FORBIDDEN/REQUIRED pair inverted so REQUIRED appears first, FORBIDDEN labeled "NOT THIS" after
**Hypothesis**: V-05 R4 consistently shows the wrong form first (FORBIDDEN), then the right form (REQUIRED). The standard intuition: labeling the wrong form first focuses attention on what to avoid, removing the lower-friction path before the right path is presented. The alternative: showing the correct form first programs the target more reliably, and the NOT THIS example reinforces it from behind. Predicts 135/135 if ordering is not the load-bearing feature of C-17. Predicts slight C-17 reduction (4/5) if the model is less likely to self-identify the wrong form when it is presented as a contrast to an already-processed REQUIRED form rather than as an actively-labeled dangerous path that must be avoided before reaching the correct instruction.

---

You are running /validate-referee for: {{topic}}

Simulate journal-specific hostile peer review. This skill knows PNAS reviewers from JCS reviewers; validate-design uses generic disciplines, this skill does not.

---

### PHASE 1 -- SIGNAL ACQUISITION

Glob: signals/**/{topic}-*
Read the artifact. Extract: central claim, method, key results, target journal.
If no journal specified: infer and confirm before proceeding.

---

### PHASE 2 -- DIVERGENCE COMMITMENT

Lock the structural minority view before naming referees:

```
DIVERGENCE COMMITMENT (locked before Phase 3)
Journal: [name]
Predicted diverger archetype: [from this journal's pool]
Direction: [more hostile / more sympathetic than the other two]
Reason: [one sentence -- what in this paper triggers this archetype]
Experiential sketch: [one sentence -- reviewing history that primes this archetype to diverge]
Brief anchor: "[Experiential sketch copied verbatim, inside quotes -- becomes SEED in Phase 4]"
```

Brief anchor is structural. Phase 4 diverger brief must open with SEED: [this sentence]. Two distinct recommendation levels required. Convergence is a simulation failure.

---

### PHASE 3 -- REFEREE ASSIGNMENT

Assign 3 referees. Phase 2 archetype must appear as one of the three.

**Journal profiles:**
- **PNAS / Nature / Science**: R1 = sympathetic-rigorous (effect sizes, p < 0.05, large N); R2 = hostile statistician (power analysis, multiple comparisons); R3 = breadth skeptic
- **Psychological Science / JEP**: R1 = pre-registration enforcer; R2 = effect-size pragmatist; R3 = ecological validity critic
- **Journal of Consciousness Studies**: R1 = sympathetic phenomenologist; R2 = hard-nosed analytic philosopher; R3 = empirical skeptic
- **Cognitive Science / Topics in Cognitive Science**: R1 = computational modeler; R2 = experimental psychologist; R3 = interdisciplinary enforcer
- **NeurIPS / ICML / AI venues**: R1 = benchmark enforcer; R2 = theory skeptic; R3 = reproducibility checker

---

### PHASE 4 -- THREE REFEREE REPORTS

For each referee: write a character brief, then the report with in-flight issue IDs on every Major Concern.

**Non-diverger brief -- REQUIRED form:**

```
Referee [N] -- [archetype] -- Character Brief
[2-3 sentences: a specific recent reviewing event that makes this referee's response to this paper's features predictable -- an event, not a label and a disposition]
```

EXAMPLE (passes C-13):
> "Referee 1 co-authored the 2023 replication of a widely-cited priming study that failed to reproduce -- the original had no pre-registration and the analysis appeared tailored to the significant result. Since then they treat any paper without pre-registration as one where the reported hypotheses may not be the original hypotheses, and they ask for OSF links in every review they write."

NOT THIS (disposition form -- fails C-13):
> "Referee 1 is a pre-registration enforcer who values methodological transparency. They have a long history of flagging papers that lack pre-registered hypotheses and routinely request that authors share their data."

Self-verification: drop the brief; would at least one Major Concern below it be phrased or weighted differently without it? If no, the brief is not load-bearing -- rewrite it.

**Diverger brief -- SEED/EXPAND REQUIRED:**

```
Referee [N] -- [archetype] -- Character Brief
SEED: [Phase 2 Brief anchor copied verbatim -- must match exactly]
EXPAND: [2-3 sentences derived from SEED -- the divergence behavior must follow from the SEED event]
```

EXAMPLE (correct EXPAND -- passes C-14):
If SEED = "After reviewing three high-profile replication failures at PNAS in 2024, this reviewer treats any N < 200 study as presumptively underpowered until a prospective power analysis appears."
REQUIRED EXPAND: "With that track record, this reviewer will read the N=87 in Section 3 as a pattern they have seen before -- their minority position pushes harder on power analysis specifically because they have personally documented this failure mode three times in the past year."

NOT THIS (new-premise EXPAND -- fails C-14):
> "This reviewer also brings expertise from clinical trial design, where power analysis is a prerequisite for IRB approval, giving them a practical rather than theoretical objection to underpowered studies."

Self-verification: drop SEED; if EXPAND still stands alone, rewrite EXPAND so it depends on SEED.

```
REFEREE [N] -- [archetype]
Recommendation: Accept / Major Revision / Minor Revision / Reject
Diverges from Phase 2: YES / NO -- [confirm direction or consensus]

SUMMARY: [2-3 sentences -- voice audible from brief; diverger's EXPAND legible in concern framing]

MAJOR CONCERNS:
[I-NN] [Specific, citable -- "Effect size d is not reported in Table 2; practical significance cannot be assessed"]
[I-NN] [...]
[I-NN] [...]

MINOR CONCERNS:
1. [...]
2. [...]

SPECIFIC COMMENTS:
Line X: [exact issue]
```

IDs continuous across all three reports. Journal standards:
- PNAS: "Effect size d is not reported. Practical significance cannot be assessed."
- JCS: "Section 3 conflates first-person and third-person descriptions."
- Cognitive Science: "The computational model is never formally specified. What are the free parameters?"

---

### PHASE 5 -- FINAL VERDICT

```
Journal: [name]
Likely decision: ACCEPT / MAJOR REVISION / MINOR REVISION / REJECT
Confidence: HIGH / MEDIUM

Divergence check: [Did the locked diverger diverge as predicted?]

P1 blockers: Issues: I-[NN], I-[NN]
P2 conditions: Issues: I-[NN], I-[NN]
Strongest referee: Referee [N] -- their objections carry most weight because [cite specific fact from their character brief or EXPAND -- reviewing history, not journal policy]
```

EXAMPLE (persona form -- passes C-15):
> "Referee 2's objections carry most weight because, as their EXPAND notes, [specific experience from SEED/EXPAND] -- this reviewer's pattern makes them structurally less dismissible than journal policy would suggest."

NOT THIS (policy form -- fails C-15):
> "Referee 2's statistical objections carry most weight because PNAS editors routinely desk-reject on power analysis grounds."

Self-verification: drop all character briefs; if the rationale is still legible, rewrite it so it depends on the brief.

---

### PHASE 6 -- ISSUE REGISTRY + ORDERED FIX PLAN

**Issue Registry** -- quote exact concern language from Phase 4.

| ID | Source | Concern (exact quote) | Severity | Done When |
|----|--------|-----------------------|----------|-----------|
| I-01 | R[N] | "[exact concern]" | P1/P2/P3 | [verifiable criterion] |

Severity: P1 = reject; P2 = consensus; P3 = single-referee non-fatal

Done When -- REQUIRED specific form:
> "Done when Table 2 reports Cohen's d with 95% CI for all three primary effects AND Supplementary S1 contains a prospective power analysis showing N=87 achieves >= 80% power for d >= 0.35 at alpha = 0.05."

NOT THIS (vague form -- fails C-12):
> "Done when the authors have addressed the statistical power concern and provided evidence that the sample is adequate."

Self-verification: drop the specific table number, section reference, or threshold; if the remaining text is still a complete criterion, rewrite.

**Ordered Fix Plan:**

**Fix 1 -- [P1 blocker title]**
Addresses: I-[NN]
Action: [Specific]
Done when: [Verifiable]

**Fix 2 -- [P2 consensus title]**
Addresses: I-[NN]
Action: [Specific]
Done when: [Verifiable]

**Fix 3 -- [Journal standard]**
Addresses: I-[NN]
Action: [Specific]
Done when: [Verifiable]

Write artifact to: signals/validate/referee/{{topic}}-referee-{{date}}.md
Frontmatter: skill: validate-referee, topic: {{topic}}, date: {{date}}, journal: [journal name], verdict: likely-accept|major-revision|reject

---

## V-04 R5 -- Phase-End Compliance Blocks: Integrity Checks After Each Phase

**Axis**: End-of-phase enforcement collocation -- C-16 removal tests and C-17 FORBIDDEN references collected into per-phase "INTEGRITY CHECK" blocks at the end of each phase, rather than inline with instructions
**Hypothesis**: V-05 R4 places enforcement mechanisms inline -- the FORBIDDEN example appears immediately after the instruction that could trigger the wrong form; the removal test appears immediately after the structural dependency instruction. This variation separates instruction from enforcement: each phase gives clean structural instructions, then ends with an INTEGRITY CHECK that lists the relevant removal test and FORBIDDEN check. FORBIDDEN examples remain proximate to the phase, not front-loaded to a preamble. Predicts 135/135 if the FORBIDDEN example is effective at the phase level regardless of exact placement within it. Predicts partial C-16 miss (4/5) if the removal test needs to immediately follow the dependency instruction to catch non-compliance before the next output is generated -- end-of-phase placement may be too late.

---

You are running /validate-referee for: {{topic}}

Simulate journal-specific hostile peer review. This skill knows PNAS reviewers from JCS reviewers.

---

### PHASE 1 -- SIGNAL ACQUISITION

Glob: signals/**/{topic}-*
Read the artifact. Extract: central claim, method, key results, target journal.
If no journal specified: infer and confirm.

---

### PHASE 2 -- DIVERGENCE COMMITMENT

Lock the structural minority view before naming referees:

```
DIVERGENCE COMMITMENT (locked before Phase 3)
Journal: [name]
Predicted diverger archetype: [from this journal's pool]
Direction: [more hostile / more sympathetic]
Reason: [one sentence]
Experiential sketch: [one sentence -- reviewing history that primes divergence]
Brief anchor: "[Experiential sketch verbatim, inside quotes -- becomes SEED in Phase 4]"
```

Brief anchor is structural. Phase 4 diverger brief must open with SEED: [this sentence]. Two distinct recommendation levels required. Convergence is a simulation failure.

---

### PHASE 3 -- REFEREE ASSIGNMENT

Assign 3 referees. Phase 2 archetype must appear as one of the three.

**Journal profiles:**
- **PNAS / Nature / Science**: R1 = sympathetic-rigorous; R2 = hostile statistician; R3 = breadth skeptic
- **Psychological Science / JEP**: R1 = pre-registration enforcer; R2 = effect-size pragmatist; R3 = ecological validity critic
- **Journal of Consciousness Studies**: R1 = sympathetic phenomenologist; R2 = hard-nosed analytic philosopher; R3 = empirical skeptic
- **Cognitive Science / Topics in Cognitive Science**: R1 = computational modeler; R2 = experimental psychologist; R3 = interdisciplinary enforcer
- **NeurIPS / ICML / AI venues**: R1 = benchmark enforcer; R2 = theory skeptic; R3 = reproducibility checker

---

### PHASE 4 -- THREE REFEREE REPORTS

For each referee: write a character brief (free-form for non-divergers; SEED/EXPAND for the diverger), then the report with in-flight issue IDs on every Major Concern.

Non-diverger briefs: 2-3 sentences of specific reviewing history that anchors this archetype's concerns in an event.
Diverger brief: SEED = Phase 2 Brief anchor verbatim; EXPAND = 2-3 sentences derived from SEED.

```
Referee [N] -- [archetype] -- Character Brief
[Brief]

REFEREE [N] -- [archetype]
Recommendation: Accept / Major Revision / Minor Revision / Reject
Diverges from Phase 2: YES / NO

SUMMARY: [2-3 sentences]

MAJOR CONCERNS:
[I-NN] [Specific, citable]
[I-NN] [...]

MINOR CONCERNS:
1. [...]

SPECIFIC COMMENTS:
Line X: [exact issue]
```

IDs continuous. Journal standards:
- PNAS: "Effect size d is not reported. Practical significance cannot be assessed."
- JCS: "Section 3 conflates first-person and third-person descriptions."
- Cognitive Science: "The computational model is never formally specified. What are the free parameters?"

**PHASE 4 INTEGRITY CHECK:**

[ ] Non-diverger briefs: drop each brief; would at least one Major Concern be phrased or weighted differently without it? If no, rewrite so the report depends on it.

FORBIDDEN non-diverger form (fails C-13):
> "Referee 1 is a pre-registration enforcer who values methodological transparency. They have a long history of flagging papers that lack pre-registered hypotheses."
If your brief describes a type rather than naming an event -- rewrite.

[ ] EXPAND: drop SEED; does EXPAND still stand alone? If yes, it introduced a new premise -- rewrite EXPAND so the divergence behavior follows from SEED.

FORBIDDEN EXPAND form (fails C-14):
> "This reviewer also brings expertise from clinical trial design, where power analysis is a prerequisite for IRB approval."
If your EXPAND introduces a credential or fact absent from SEED -- rewrite.

---

### PHASE 5 -- FINAL VERDICT

```
Journal: [name]
Likely decision: ACCEPT / MAJOR REVISION / MINOR REVISION / REJECT
Confidence: HIGH / MEDIUM

Divergence check: [Did the diverger diverge as predicted?]

P1 blockers: Issues: I-[NN], I-[NN]
P2 conditions: Issues: I-[NN], I-[NN]
Strongest referee: Referee [N] -- their objections carry most weight because [cite specific fact from their character brief -- reviewing history, not journal policy]
```

**PHASE 5 INTEGRITY CHECK:**

[ ] Strongest-referee rationale: drop all character briefs; is the rationale still legible? If yes, rewrite it so it depends on a specific fact from the brief.

FORBIDDEN rationale form (fails C-15):
> "Referee 2's objections carry most weight because PNAS editors routinely desk-reject on power analysis grounds."
If your rationale could have been written without reading Phase 4 -- rewrite.

---

### PHASE 6 -- ISSUE REGISTRY + ORDERED FIX PLAN

**Issue Registry** -- exact concern quotes from Phase 4.

| ID | Source | Concern (exact quote) | Severity | Done When |
|----|--------|-----------------------|----------|-----------|
| I-01 | R[N] | "[exact concern]" | P1/P2/P3 | [verifiable criterion] |

Severity: P1 = reject; P2 = consensus; P3 = single-referee non-fatal

**Ordered Fix Plan:**

**Fix 1 -- [P1 blocker title]**
Addresses: I-[NN]
Action: [Specific]
Done when: [Verifiable]

**Fix 2 -- [P2 consensus title]**
Addresses: I-[NN]
Action: [Specific]
Done when: [Verifiable]

**Fix 3 -- [Journal standard]**
Addresses: I-[NN]
Action: [Specific]
Done when: [Verifiable]

**PHASE 6 INTEGRITY CHECK:**

[ ] Done When criteria: drop the specific table number, section reference, or threshold from each Done When entry; if the remaining text is still a complete criterion, rewrite to name at least one specific artifact and one measurable threshold.

FORBIDDEN Done When form (fails C-12):
> "Done when the authors have addressed the statistical power concern and provided evidence that the sample is adequate."
REQUIRED Done When form:
> "Done when Table 2 reports Cohen's d with 95% CI for all three primary effects AND Supplementary S1 contains a prospective power analysis showing N=87 achieves >= 80% power for d >= 0.35 at alpha = 0.05."

Write artifact to: signals/validate/referee/{{topic}}-referee-{{date}}.md
Frontmatter: skill: validate-referee, topic: {{topic}}, date: {{date}}, journal: [journal name], verdict: likely-accept|major-revision|reject

---

## V-05 R5 -- Canonical Production Form: Clean Editorial Pass of V-05 R4

**Axis**: Canonical production -- V-05 R4 with editorial pass for consistency, normalized label typography, unified removal-test verb, and no redundant commentary
**Hypothesis**: V-05 R4 achieves 135/135 but accumulated organic complexity across 4 rounds: some phases use "drop" and some use "remove"; FORBIDDEN label typography varies; explanatory commentary after some blocks restates the distinction the examples already make. An editorial pass that (a) normalizes the removal-test verb to a consistent imperative form; (b) makes FORBIDDEN/REQUIRED a consistent bold typographic convention throughout; (c) removes commentary that duplicates what the examples already demonstrate -- should produce 135/135 in a cleaner, maintainable form. This is the deployment candidate.

---

You are running /validate-referee for: {{topic}}

Simulate journal-specific hostile peer review. This skill knows PNAS reviewers from JCS reviewers; validate-design uses generic disciplines, this skill does not.

---

### PHASE 1 -- SIGNAL ACQUISITION

Glob: signals/**/{topic}-*
Read the artifact. Extract: central claim, method, key results, target journal.
If no journal specified: infer from content style and confirm before proceeding.

---

### PHASE 2 -- DIVERGENCE COMMITMENT

Lock the structural minority view before naming referees:

```
DIVERGENCE COMMITMENT (locked before Phase 3)
Journal: [name]
Predicted diverger archetype: [from this journal's pool]
Direction: [more hostile than the other two / more sympathetic than the other two]
Reason: [one sentence -- what in this paper's design or claims triggers this archetype specifically]
Experiential sketch: [one sentence -- the reviewing history that primes this archetype to diverge now]
Brief anchor: "[Experiential sketch copied verbatim, inside quotes -- this exact sentence becomes SEED in Phase 4]"
```

Brief anchor is a structural output. Phase 4 character brief for the diverger must open with SEED: [this sentence]. If SEED does not match Brief anchor, C-14 is not satisfied. This commitment is locked before Phase 3. At least two distinct recommendation levels must appear across the three reports. Convergence is a simulation failure.

---

### PHASE 3 -- REFEREE ASSIGNMENT

Assign 3 referees with journal-specific archetypes. The Phase 2 archetype must appear as one of the three.

**Journal profiles:**
- **PNAS / Nature / Science**: R1 = sympathetic-rigorous (effect sizes, p < 0.05, large N); R2 = hostile statistician (power analysis, multiple comparisons, replication); R3 = breadth skeptic (is this general enough for a broad journal?)
- **Psychological Science / JEP**: R1 = pre-registration enforcer; R2 = effect-size pragmatist (d > 0.4 or why bother?); R3 = ecological validity critic
- **Journal of Consciousness Studies / Phenomenology**: R1 = sympathetic phenomenologist; R2 = hard-nosed analytic philosopher; R3 = empirical skeptic
- **Cognitive Science / Topics in Cognitive Science**: R1 = computational modeler; R2 = experimental psychologist; R3 = interdisciplinary enforcer
- **NeurIPS / ICML / AI venues**: R1 = benchmark enforcer; R2 = theory skeptic; R3 = reproducibility checker

---

### PHASE 4 -- THREE REFEREE REPORTS

For each referee: write a character brief, then the report with in-flight issue IDs on every Major Concern.

**Non-diverger brief format:**

```
Referee [N] -- [archetype] -- Character Brief
[2-3 sentences: a specific recent reviewing event that makes this referee's response to this paper's features predictable]
```

**FORBIDDEN** (disposition form -- fails C-13):
> "Referee 1 is a pre-registration enforcer who values methodological transparency. They have a long history of flagging papers that lack pre-registered hypotheses and routinely request that authors share their data."

**REQUIRED** (event form -- passes C-13):
> "Referee 1 co-authored the 2023 replication of a widely-cited priming study that failed to reproduce -- the original had no pre-registration and the analysis appeared tailored to the significant result. Since then they treat any paper without pre-registration as one where the reported hypotheses may not be the original hypotheses, and they ask for OSF links in every review they write."

Self-verification: drop the brief; if at least one Major Concern below it would be phrased or weighted identically without it, the brief is not load-bearing -- rewrite it so the report depends on it.

**Diverger brief format (SEED/EXPAND required):**

```
Referee [N] -- [archetype] -- Character Brief
SEED: [Phase 2 Brief anchor copied verbatim -- must match exactly]
EXPAND: [2-3 sentences derived from SEED -- how does that reviewing history produce the Phase 2 divergence direction?]
```

**FORBIDDEN** (new-premise EXPAND -- fails C-14):
If SEED = "After reviewing three high-profile replication failures at PNAS in 2024, this reviewer treats any N < 200 study as presumptively underpowered until a prospective power analysis appears."
> "This reviewer also brings expertise from clinical trial design, where power analysis is a prerequisite for IRB approval, giving them a practical rather than theoretical objection to underpowered studies."

**REQUIRED** EXPAND:
> "With that track record of watching N < 200 studies fail, this reviewer will read the N=87 in Section 3 as a pattern they have seen before -- their minority position pushes harder on power analysis specifically because they have personally documented this failure mode three times in the past year."

Self-verification: drop SEED; if EXPAND still stands alone, it introduced a new premise -- rewrite EXPAND so it depends on SEED.

```
REFEREE [N] -- [archetype]
Recommendation: Accept / Major Revision / Minor Revision / Reject
Diverges from Phase 2: YES / NO -- [confirm direction or consensus]

SUMMARY:
[2-3 sentences -- voice audible from brief; diverger's EXPAND legible in concern framing]

MAJOR CONCERNS:
[I-NN] [Specific, citable -- "Effect size d is not reported in Table 2; practical significance cannot be assessed"]
[I-NN] [...]
[I-NN] [...]

MINOR CONCERNS:
1. [...]
2. [...]

SPECIFIC COMMENTS:
Line X: [exact issue]
```

IDs continuous across all three reports. Journal standards enforced:
- PNAS: "Effect size d is not reported. Without this, practical significance cannot be assessed."
- JCS: "Section 3 conflates first-person and third-person descriptions without acknowledging this move."
- Cognitive Science: "The computational model in Figure 2 is described but never formally specified. What are the free parameters?"

---

### PHASE 5 -- FINAL VERDICT

```
Journal: [name]
Likely decision: ACCEPT / MAJOR REVISION / MINOR REVISION / REJECT
Confidence: HIGH / MEDIUM

Divergence check: [Did the locked diverger diverge as predicted? If yes, confirm. If direction differed, explain.]

P1 blockers (reject conditions):
  Issues: I-[NN], I-[NN]

P2 conditions (major revision requirements):
  Issues: I-[NN], I-[NN]

Strongest referee: Referee [N] -- their objections carry most weight because [cite a specific fact from their character brief or EXPAND -- reviewing history, not journal policy]
```

**FORBIDDEN** (policy form -- fails C-15):
> "Referee 2's statistical objections carry most weight because PNAS editors routinely desk-reject on power analysis grounds."

**REQUIRED** (persona form -- passes C-15):
> "Referee 2's objections carry most weight because, as their EXPAND notes, [specific experience from SEED/EXPAND] -- this reviewer's pattern makes them structurally less dismissible than journal policy would suggest."

Self-verification: drop all character briefs; if this rationale is still legible, rewrite it so it depends on a specific fact from the brief.

---

### PHASE 6 -- ISSUE REGISTRY + ORDERED FIX PLAN

**Issue Registry** -- quote exact concern language from Phase 4; do not paraphrase.

| ID | Source | Concern (exact quote) | Severity | Done When |
|----|--------|-----------------------|----------|-----------|
| I-01 | R[N] | "[exact quoted concern]" | P1/P2/P3 | [verifiable criterion] |
| I-02 | R[N] | "[exact quoted concern]" | P1/P2/P3 | [verifiable criterion] |

Severity: P1 = reject condition; P2 = consensus (2+ referees) or maps to P1 blocker; P3 = single-referee non-fatal

**FORBIDDEN** (vague Done When -- fails C-12):
> "Done when the authors have addressed the statistical power concern and provided evidence that the sample is adequate for the claims made."

**REQUIRED** (specific Done When -- passes C-12):
> "Done when Table 2 reports Cohen's d with 95% CI for all three primary effects AND Supplementary S1 contains a prospective power analysis showing N=87 achieves >= 80% power for d >= 0.35 at alpha = 0.05."

Self-verification: drop the specific table number, section identifier, or threshold from each Done When entry; if the remaining text is still a complete criterion, rewrite to name at least one specific artifact and one measurable threshold.

**Ordered Fix Plan:**

**Fix 1 -- [P1 blocker title]**
Addresses: I-[NN], I-[NN]
Action: [Specific -- add Table X with columns Y, Z; run analysis W; rewrite section V]
Done when: [Verifiable -- e.g., "Table 2 now reports Cohen's d with 95% CI for all effects; power analysis in Supplementary S1"]

**Fix 2 -- [P2 consensus title]**
Addresses: I-[NN], I-[NN]
Action: [Specific]
Done when: [Verifiable]

**Fix 3 -- [Journal standard]**
Addresses: I-[NN]
Action: [Journal-specific formatting or evidence standard]
Done when: [Verifiable]

Write artifact to: signals/validate/referee/{{topic}}-referee-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: validate-referee, topic: {{topic}}, date: {{date}}, journal: [journal name], verdict: likely-accept|major-revision|reject
