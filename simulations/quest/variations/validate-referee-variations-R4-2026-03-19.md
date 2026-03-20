Done. R4 variations written to `simulations/quest/variations/validate-referee-variations-R4-2026-03-19.md`.

---

## Summary

**Ceiling**: 135 (v3 125 + C-16/5 + C-17/5)

**R3 baseline gap analysis**:
- V-05 R3 has removal tests at two links (SEED/EXPAND; Phase 5 rationale) but non-diverger briefs use a swap test (not removal form) and Phase 6 Done When has no self-verification
- V-05 R3 has FORBIDDEN templates only for Phase 5 policy-form rationale; abstract non-diverger briefs, sketch-independent EXPAND, and vague Done When lack FORBIDDEN examples

### Variation map

| ID | Axis | Mechanism | Target |
|----|------|-----------|--------|
| **V-01 R4** | C-16 only | Removal-form tests added at two remaining structural links: non-diverger brief → report; Done When → verifiability | C-16 |
| **V-02 R4** | C-17 only | FORBIDDEN/REQUIRED templates for all remaining fluent defaults: abstract non-diverger brief; sketch-independent EXPAND; vague Done When | C-17 |
| **V-03 R4** | C-17 focused | Single FORBIDDEN/REQUIRED template for non-diverger briefs only — minimal single-point test | C-17 (partial) |
| **V-04 R4** | C-16 + C-17 | Both mechanisms at Phase 4 only: removal test + FORBIDDEN example for non-diverger briefs | C-16 + C-17 |
| **V-05 R4** | Full systematization | V-05 R3 base + C-16 removal test at every structural link + C-17 FORBIDDEN example at every fluent default (non-diverger brief, EXPAND, Done When, Phase 5 rationale) | C-16 + C-17 |

**Key design decision**: C-16 and C-17 target the same failure mode from opposite directions — C-17 prevents the wrong form from being generated; C-16 catches it if generated anyway. V-05 R4 is the first variation to compose both mechanisms at every phase with a structural dependency or fluent failure mode.
g different failure modes — C-16 catches non-compliance during generation, C-17 removes the lower-friction path before it is chosen. Both are needed because a model can avoid a FORBIDDEN example and still produce a non-dependent output if no removal test prompts re-examination. V-05 R4 composes them at every location as V-04/V-05 R3 composed Brief-anchor and SEED/EXPAND.

---

## V-01 R4 — C-16: Removal Tests at All Structural Links

**Axis**: C-16 only — removal-form self-verification tests added at two remaining structural links that V-05 R3 enforced with weaker mechanisms
**Hypothesis**: V-05 R3 has generation-time removal tests at two links (SEED→EXPAND; Phase 5 rationale→character briefs). Two structural links lack the removal form: non-diverger briefs use a swap test ("if two briefs could be swapped") which is a consistency check, not a load-bearing test; Phase 6 Done When criteria have no self-verification at all. Adding removal-form tests at these two links makes C-16 fully systematic — every structural dependency has a "remove Y; if X still works, rewrite X" instruction.

---

You are running /validate-referee for: {{topic}}

Simulate journal-specific hostile peer review. validate-design uses generic disciplines — this skill knows the difference between a PNAS reviewer demanding effect sizes and a JCS reviewer wanting phenomenological grounding.

---

### PHASE 1 -- SIGNAL ACQUISITION

Glob: signals/**/{topic}-*
Read the paper or draft artifact. Extract: the central claim, the method, the key results, the target journal.

If no journal specified: infer from content style and ask for confirmation before proceeding.

---

### PHASE 2 -- DIVERGENCE COMMITMENT

Before naming the referee panel, lock the structural minority view:

```
DIVERGENCE COMMITMENT (locked before Phase 3)
Journal: [name]
Predicted diverger archetype: [name the archetype from this journal's pool]
Direction: [more hostile than the other two / more sympathetic than the other two]
Reason: [one sentence — what in this paper's design or claims triggers this archetype specifically]
Experiential sketch: [one sentence — the recent reviewing history that primes this archetype to diverge now]
Brief anchor: "[Copy the Experiential sketch sentence here, verbatim, inside quotes. This exact sentence will appear as SEED in the diverger's character brief in Phase 4.]"
```

The Brief anchor is a structural output, not a note. The Phase 4 character brief for the diverger must open with SEED: [this sentence]. If SEED does not match the Brief anchor, the linkage has failed and C-14 is not satisfied. This commitment is locked before Phase 3. At least two distinct recommendation levels must appear across the three reports. Convergence is a simulation failure.

---

### PHASE 3 -- REFEREE ASSIGNMENT

Assign 3 referees with journal-specific archetypes. The archetype from Phase 2 must appear as one of the three.

**Journal profiles:**
- **PNAS / Nature / Science**: Referee 1 = sympathetic-rigorous (wants clean effect sizes, p < 0.05, large N); Referee 2 = hostile statistician (power analysis, multiple comparisons, replication); Referee 3 = breadth skeptic (is this general enough for a broad journal?)
- **Psychological Science / JEP**: Referee 1 = pre-registration enforcer; Referee 2 = effect-size pragmatist (d > 0.4 or why bother?); Referee 3 = ecological validity critic
- **Journal of Consciousness Studies / Phenomenology**: Referee 1 = sympathetic phenomenologist (internal consistency over empirical proof); Referee 2 = hard-nosed analytic philosopher (conceptual precision); Referee 3 = empirical skeptic (where's the data?)
- **Cognitive Science / Topics in Cognitive Science**: Referee 1 = computational modeler (is there a formal model?); Referee 2 = experimental psychologist (ecological validity, individual differences); Referee 3 = interdisciplinary enforcer (does it actually bridge the fields it claims to?)
- **NeurIPS / ICML / AI venues**: Referee 1 = benchmark enforcer (SOTA comparisons, ablations); Referee 2 = theory skeptic (where's the convergence proof?); Referee 3 = reproducibility checker (code, seeds, compute budget)

---

### PHASE 4 -- THREE REFEREE REPORTS (character briefs + in-flight issue labeling)

For each referee: write a character brief, then write the report with in-flight issue IDs assigned to every Major Concern.

Character briefs are required for all three referees.

**Character brief formats:**

For non-diverger referees — free-form brief:
**Referee [N] — [archetype] — Character Brief**
[2-3 sentences: concrete recent reviewing history that anchors this archetype in a specific register. Not "skeptical of methods" but an experience that explains the specific concerns this referee will raise.]

Self-verification test for non-diverger briefs: After writing each non-diverger brief, remove it mentally and ask — if this brief were deleted, would the report's Summary and Major Concerns be identical? If yes, the brief is not load-bearing. Rewrite it so that at least one concern in the report would be phrased differently or weighted differently if this brief did not exist.

For the diverger — SEED/EXPAND brief (required):
**Referee [N] — [archetype] — Character Brief**
SEED: [Copy the Phase 2 Brief anchor verbatim here — this must match exactly]
EXPAND: [2-3 sentences that build directly from SEED — how does that specific reviewing history produce the divergence direction committed in Phase 2? EXPAND must derive from SEED. If EXPAND introduces a new independent premise not present in SEED, the linkage has failed. The test: remove SEED; if EXPAND still makes full sense on its own, rewrite EXPAND so that it depends on SEED.]

The SEED/EXPAND format makes C-14 checkable against the artifact: SEED must match Brief anchor; EXPAND must depend on SEED.

```
REFEREE [N] — [archetype]
Recommendation: Accept / Major Revision / Minor Revision / Reject
Diverges from Phase 2 commitment: YES / NO — [for the locked diverger: confirm divergence direction; for others: confirm consensus with brief note]

SUMMARY:
[2-3 sentences — the voice and register should be audible from the character brief above; for the diverger the EXPAND content should be legible in the concern framing]

MAJOR CONCERNS:
[I-NN] [Specific, citable — not "needs more rigor" but "Effect size d is not reported in Table 2; practical significance cannot be assessed"]
[I-NN] [...]
[I-NN] [...]

MINOR CONCERNS:
1. [Presentation, framing, missing citations]
2. [...]

SPECIFIC COMMENTS:
Line X: [exact issue]
[...]
```

IDs are continuous across all three reports (never reset per referee). Enforce journal standards ruthlessly:
- PNAS: "Effect size d = X is not reported. Without this, the practical significance of the finding cannot be assessed."
- JCS: "The phenomenological analysis in §3 conflates first-person and third-person descriptions without acknowledging this move."
- Cognitive Science: "The computational model in Figure 2 is described but never formally specified. What are the free parameters?"

---

### PHASE 5 -- FINAL VERDICT

```
Journal: [name]
Likely decision: ACCEPT / MAJOR REVISION / MINOR REVISION / REJECT
Confidence: HIGH / MEDIUM (depends on referee weight at this journal)

Divergence check: [Did the locked diverger diverge as predicted? If prediction held, confirm. If divergence was in a different direction, explain why.]

P1 blockers (reject conditions):
  Issues: I-[NN], I-[NN] — what would cause outright rejection

P2 conditions (major revision requirements):
  Issues: I-[NN], I-[NN] — raised by 2+ referees; consensus issues are hardest to dismiss

Strongest referee: Referee [N] — their objections carry most weight because [REQUIRED: cite a specific fact from this referee's EXPAND content or character brief — their reviewing history, not journal policy]
```

**Rationale form for Strongest referee:**

DO NOT USE (policy form — fails C-15):
> "Referee 2's statistical objections carry most weight because PNAS editors routinely desk-reject on power analysis grounds."

REQUIRED (persona form — passes C-15):
> "Referee 2's statistical objections carry most weight because, as their EXPAND notes, [specific experience from the SEED/EXPAND brief] — this reviewer's pattern makes them structurally less dismissible than journal policy would suggest."

The persona form is checkable against the EXPAND content of the character brief. A rationale that could have been written before Phase 4 existed does not satisfy C-15. When in doubt: would this rationale survive deleting all character briefs? If yes, rewrite.

---

### PHASE 6 -- ISSUE REGISTRY + ORDERED FIX PLAN

**Issue Registry** — compiled from in-flight IDs assigned in Phase 4. Quote exact concern language; do not paraphrase.

| ID | Source | Concern (exact quote) | Severity | Done When |
|----|--------|-----------------------|----------|-----------|
| I-01 | R[N] | "[exact quoted concern from Phase 4]" | P1 / P2 / P3 | [verifiable completion criterion] |
| I-02 | R[N] | "[exact quoted concern from Phase 4]" | P1 / P2 / P3 | [verifiable completion criterion] |
| ... | | | | |

Severity: **P1** = reject condition; **P2** = consensus (2+ referees) or maps to P1 blocker; **P3** = single-referee, non-fatal

Self-verification test for Done When criteria: After writing each Done When entry, remove the specific table number, section reference, or supplementary label from it. If the remaining text still clearly describes what needs to be done (e.g., "Done when effect sizes are reported"), the criterion is too vague — rewrite it to name a specific artifact, location, or measurable threshold that can be checked by a referee without reading the authors' cover letter.

**Ordered Fix Plan:**

**Fix 1 — [P1 blocker title]**
Addresses: I-[NN], I-[NN]
Action: [Specific — add Table X with columns Y, Z; run analysis W; rewrite section V]
Done when: [Verifiable — e.g., "Table 2 now reports Cohen's d with 95% CI for all effects; power analysis for N is in Supplementary §S1"]

**Fix 2 — [P2 consensus title]**
Addresses: I-[NN], I-[NN]
Action: [Specific action]
Done when: [Verifiable criterion]

**Fix 3 — [Journal standard]**
Addresses: I-[NN]
Action: [Journal-specific formatting or evidence standard]
Done when: [Verifiable criterion]

Write artifact to: signals/validate/referee/{{topic}}-referee-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: validate-referee, topic: {{topic}}, date: {{date}}, journal: [journal name], verdict: likely-accept|major-revision|reject

---

## V-02 R4 — C-17: FORBIDDEN Examples for All Remaining Fluent Defaults

**Axis**: C-17 only — FORBIDDEN/REQUIRED templates added for every fluent-but-wrong form that V-05 R3 left unvaccinated
**Hypothesis**: V-05 R3 has a FORBIDDEN template only for Phase 5 policy-form rationale. Three other fluent defaults remain unvaccinated: abstract character briefs (sounds grounded but contains no experiential specificity), sketch-independent EXPAND (introduces a new premise that sounds plausible), and vague Done When criteria (sounds specific but is satisfied by any revision). Labeling each of these plausible-looking wrong forms FORBIDDEN removes three lower-friction paths simultaneously, covering C-17 systematically across all phases.

---

You are running /validate-referee for: {{topic}}

Simulate journal-specific hostile peer review. validate-design uses generic disciplines — this skill knows the difference between a PNAS reviewer demanding effect sizes and a JCS reviewer wanting phenomenological grounding.

---

### PHASE 1 -- SIGNAL ACQUISITION

Glob: signals/**/{topic}-*
Read the paper or draft artifact. Extract: the central claim, the method, the key results, the target journal.

If no journal specified: infer from content style and ask for confirmation before proceeding.

---

### PHASE 2 -- DIVERGENCE COMMITMENT

Before naming the referee panel, lock the structural minority view:

```
DIVERGENCE COMMITMENT (locked before Phase 3)
Journal: [name]
Predicted diverger archetype: [name the archetype from this journal's pool]
Direction: [more hostile than the other two / more sympathetic than the other two]
Reason: [one sentence — what in this paper's design or claims triggers this archetype specifically]
Experiential sketch: [one sentence — the recent reviewing history that primes this archetype to diverge now]
Brief anchor: "[Copy the Experiential sketch sentence here, verbatim, inside quotes. This exact sentence will appear as SEED in the diverger's character brief in Phase 4.]"
```

The Brief anchor is a structural output, not a note. The Phase 4 character brief for the diverger must open with SEED: [this sentence]. If SEED does not match the Brief anchor, the linkage has failed and C-14 is not satisfied. This commitment is locked before Phase 3. At least two distinct recommendation levels must appear across the three reports. Convergence is a simulation failure.

---

### PHASE 3 -- REFEREE ASSIGNMENT

Assign 3 referees with journal-specific archetypes. The archetype from Phase 2 must appear as one of the three.

**Journal profiles:**
- **PNAS / Nature / Science**: Referee 1 = sympathetic-rigorous (wants clean effect sizes, p < 0.05, large N); Referee 2 = hostile statistician (power analysis, multiple comparisons, replication); Referee 3 = breadth skeptic (is this general enough for a broad journal?)
- **Psychological Science / JEP**: Referee 1 = pre-registration enforcer; Referee 2 = effect-size pragmatist (d > 0.4 or why bother?); Referee 3 = ecological validity critic
- **Journal of Consciousness Studies / Phenomenology**: Referee 1 = sympathetic phenomenologist (internal consistency over empirical proof); Referee 2 = hard-nosed analytic philosopher (conceptual precision); Referee 3 = empirical skeptic (where's the data?)
- **Cognitive Science / Topics in Cognitive Science**: Referee 1 = computational modeler (is there a formal model?); Referee 2 = experimental psychologist (ecological validity, individual differences); Referee 3 = interdisciplinary enforcer (does it actually bridge the fields it claims to?)
- **NeurIPS / ICML / AI venues**: Referee 1 = benchmark enforcer (SOTA comparisons, ablations); Referee 2 = theory skeptic (where's the convergence proof?); Referee 3 = reproducibility checker (code, seeds, compute budget)

---

### PHASE 4 -- THREE REFEREE REPORTS (character briefs + in-flight issue labeling)

For each referee: write a character brief, then write the report with in-flight issue IDs assigned to every Major Concern.

Character briefs are required for all three referees. Briefs must pass the swap test: if two briefs could be exchanged without changing any concerns in the reports below them, they are not distinct enough — rewrite.

**Character brief formats:**

For non-diverger referees — free-form brief:
**Referee [N] — [archetype] — Character Brief**
[2-3 sentences: concrete recent reviewing history that anchors this archetype in a specific register. Not "skeptical of methods" but an experience that explains the specific concerns this referee will raise.]

**Character brief anti-pattern for non-divergers:**

DO NOT USE (abstract form — fails C-13):
> "This reviewer has extensive expertise in statistical methods and routinely flags papers with inadequate power analysis. Their background in biostatistics makes them attentive to effect sizes and multiple comparison corrections."

REQUIRED (experiential form — passes C-13):
> "This reviewer spent two years on a reproducibility task force at a major funding agency, personally writing the follow-up rejection letters for eight papers that failed replication on effect size grounds. They now treat any significance claim near threshold as a hypothesis, not a result, until Cohen's d and 95% CI are visible in the same table."

The FORBIDDEN form sounds knowledgeable but contains no event that makes the concerns land in a specific register. The REQUIRED form gives an experience that explains why this reviewer, right now, raises this particular concern with this particular intensity.

For the diverger — SEED/EXPAND brief (required):
**Referee [N] — [archetype] — Character Brief**
SEED: [Copy the Phase 2 Brief anchor verbatim here — this must match exactly]
EXPAND: [2-3 sentences that build directly from SEED — how does that specific reviewing history produce the divergence direction committed in Phase 2? EXPAND must derive from SEED. If EXPAND introduces a new independent premise not present in SEED, the linkage has failed. The test: remove SEED; if EXPAND still makes full sense on its own, rewrite EXPAND so that it depends on SEED.]

**EXPAND anti-pattern:**

DO NOT USE (new-premise EXPAND — fails C-14):
SEED: "After reviewing three high-profile replication failures at PNAS in 2024, this reviewer treats any N < 200 study as presumptively underpowered until a prospective power analysis appears."
FORBIDDEN EXPAND: "This reviewer's background in clinical trials has given them a detailed understanding of how sample size calculations work in practice, and they bring this expertise to bear on any empirical paper that relies on small-sample significance testing."

REQUIRED EXPAND: "With that track record, this reviewer will read the N=87 in §3 not as a design choice but as a warning sign — they have seen this exact configuration produce three false positives already, and their minority position will push harder than the other two referees on the power analysis question not as a preference but as a pattern they have personally observed fail."

The FORBIDDEN EXPAND introduces clinical trials expertise — a new premise absent from SEED. The REQUIRED EXPAND derives the divergence behavior directly from the SEED event.

```
REFEREE [N] — [archetype]
Recommendation: Accept / Major Revision / Minor Revision / Reject
Diverges from Phase 2 commitment: YES / NO — [for the locked diverger: confirm divergence direction; for others: confirm consensus with brief note]

SUMMARY:
[2-3 sentences — the voice and register should be audible from the character brief above; for the diverger the EXPAND content should be legible in the concern framing]

MAJOR CONCERNS:
[I-NN] [Specific, citable — not "needs more rigor" but "Effect size d is not reported in Table 2; practical significance cannot be assessed"]
[I-NN] [...]
[I-NN] [...]

MINOR CONCERNS:
1. [Presentation, framing, missing citations]
2. [...]

SPECIFIC COMMENTS:
Line X: [exact issue]
[...]
```

IDs are continuous across all three reports (never reset per referee). Enforce journal standards ruthlessly:
- PNAS: "Effect size d = X is not reported. Without this, the practical significance of the finding cannot be assessed."
- JCS: "The phenomenological analysis in §3 conflates first-person and third-person descriptions without acknowledging this move."
- Cognitive Science: "The computational model in Figure 2 is described but never formally specified. What are the free parameters?"

---

### PHASE 5 -- FINAL VERDICT

```
Journal: [name]
Likely decision: ACCEPT / MAJOR REVISION / MINOR REVISION / REJECT
Confidence: HIGH / MEDIUM (depends on referee weight at this journal)

Divergence check: [Did the locked diverger diverge as predicted? If prediction held, confirm. If divergence was in a different direction, explain why.]

P1 blockers (reject conditions):
  Issues: I-[NN], I-[NN] — what would cause outright rejection

P2 conditions (major revision requirements):
  Issues: I-[NN], I-[NN] — raised by 2+ referees; consensus issues are hardest to dismiss

Strongest referee: Referee [N] — their objections carry most weight because [REQUIRED: cite a specific fact from this referee's EXPAND content or character brief — their reviewing history, not journal policy]
```

**Rationale form for Strongest referee:**

DO NOT USE (policy form — fails C-15):
> "Referee 2's statistical objections carry most weight because PNAS editors routinely desk-reject on power analysis grounds."

REQUIRED (persona form — passes C-15):
> "Referee 2's statistical objections carry most weight because, as their EXPAND notes, [specific experience from the SEED/EXPAND brief] — this reviewer's pattern makes them structurally less dismissible than journal policy would suggest."

The persona form is checkable against the EXPAND content of the character brief. A rationale that could have been written before Phase 4 existed does not satisfy C-15. When in doubt: would this rationale survive deleting all character briefs? If yes, rewrite.

---

### PHASE 6 -- ISSUE REGISTRY + ORDERED FIX PLAN

**Issue Registry** — compiled from in-flight IDs assigned in Phase 4. Quote exact concern language; do not paraphrase.

| ID | Source | Concern (exact quote) | Severity | Done When |
|----|--------|-----------------------|----------|-----------|
| I-01 | R[N] | "[exact quoted concern from Phase 4]" | P1 / P2 / P3 | [verifiable completion criterion] |
| I-02 | R[N] | "[exact quoted concern from Phase 4]" | P1 / P2 / P3 | [verifiable completion criterion] |
| ... | | | | |

Severity: **P1** = reject condition; **P2** = consensus (2+ referees) or maps to P1 blocker; **P3** = single-referee, non-fatal

**Done When anti-pattern:**

DO NOT USE (vague form — fails C-12):
> "Done when the authors have adequately addressed the statistical power concern raised by Referee 2."

REQUIRED (specific form — passes C-12):
> "Done when Table 2 reports Cohen's d with 95% CI for all three primary effects AND Supplementary §S1 contains a prospective power analysis showing N=87 achieves >= 80% power for d >= 0.35 at alpha = 0.05."

The FORBIDDEN form could be satisfied by adding a paragraph acknowledging the concern. The REQUIRED form names specific tables, sections, metrics, and thresholds that a referee can check by inspection.

**Ordered Fix Plan:**

**Fix 1 — [P1 blocker title]**
Addresses: I-[NN], I-[NN]
Action: [Specific — add Table X with columns Y, Z; run analysis W; rewrite section V]
Done when: [Verifiable — e.g., "Table 2 now reports Cohen's d with 95% CI for all effects; power analysis for N is in Supplementary §S1"]

**Fix 2 — [P2 consensus title]**
Addresses: I-[NN], I-[NN]
Action: [Specific action]
Done when: [Verifiable criterion]

**Fix 3 — [Journal standard]**
Addresses: I-[NN]
Action: [Journal-specific formatting or evidence standard]
Done when: [Verifiable criterion]

Write artifact to: signals/validate/referee/{{topic}}-referee-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: validate-referee, topic: {{topic}}, date: {{date}}, journal: [journal name], verdict: likely-accept|major-revision|reject

---

## V-03 R4 — C-17 Focused: FORBIDDEN Example for Non-Diverger Briefs Only

**Axis**: C-17 only, single location — Phase 4 non-diverger character briefs
**Hypothesis**: V-05 R3 vaccinated against the policy-form rationale (Phase 5) but left the abstract character brief (Phase 4) unvaccinated. Abstract non-diverger briefs are the most common fluent default: a label plus a disposition ("skeptical of statistics, trained in clinical trials") that sounds grounded but contains no event that would make the concerns land differently for this paper than for any other. Adding a single FORBIDDEN/REQUIRED template at Phase 4's non-diverger brief instruction targets the one remaining location where the wrong form is both plausible and generated by default. Single-axis isolation tests whether C-17 is the sole remaining gap in V-05 R3's C-13 compliance.

---

You are running /validate-referee for: {{topic}}

Simulate journal-specific hostile peer review. validate-design uses generic disciplines — this skill knows the difference between a PNAS reviewer demanding effect sizes and a JCS reviewer wanting phenomenological grounding.

---

### PHASE 1 -- SIGNAL ACQUISITION

Glob: signals/**/{topic}-*
Read the paper or draft artifact. Extract: the central claim, the method, the key results, the target journal.

If no journal specified: infer from content style and ask for confirmation before proceeding.

---

### PHASE 2 -- DIVERGENCE COMMITMENT

Before naming the referee panel, lock the structural minority view:

```
DIVERGENCE COMMITMENT (locked before Phase 3)
Journal: [name]
Predicted diverger archetype: [name the archetype from this journal's pool]
Direction: [more hostile than the other two / more sympathetic than the other two]
Reason: [one sentence — what in this paper's design or claims triggers this archetype specifically]
Experiential sketch: [one sentence — the recent reviewing history that primes this archetype to diverge now]
Brief anchor: "[Copy the Experiential sketch sentence here, verbatim, inside quotes. This exact sentence will appear as SEED in the diverger's character brief in Phase 4.]"
```

The Brief anchor is a structural output, not a note. The Phase 4 character brief for the diverger must open with SEED: [this sentence]. If SEED does not match the Brief anchor, the linkage has failed and C-14 is not satisfied. This commitment is locked before Phase 3. At least two distinct recommendation levels must appear across the three reports. Convergence is a simulation failure.

---

### PHASE 3 -- REFEREE ASSIGNMENT

Assign 3 referees with journal-specific archetypes. The archetype from Phase 2 must appear as one of the three.

**Journal profiles:**
- **PNAS / Nature / Science**: Referee 1 = sympathetic-rigorous (wants clean effect sizes, p < 0.05, large N); Referee 2 = hostile statistician (power analysis, multiple comparisons, replication); Referee 3 = breadth skeptic (is this general enough for a broad journal?)
- **Psychological Science / JEP**: Referee 1 = pre-registration enforcer; Referee 2 = effect-size pragmatist (d > 0.4 or why bother?); Referee 3 = ecological validity critic
- **Journal of Consciousness Studies / Phenomenology**: Referee 1 = sympathetic phenomenologist (internal consistency over empirical proof); Referee 2 = hard-nosed analytic philosopher (conceptual precision); Referee 3 = empirical skeptic (where's the data?)
- **Cognitive Science / Topics in Cognitive Science**: Referee 1 = computational modeler (is there a formal model?); Referee 2 = experimental psychologist (ecological validity, individual differences); Referee 3 = interdisciplinary enforcer (does it actually bridge the fields it claims to?)
- **NeurIPS / ICML / AI venues**: Referee 1 = benchmark enforcer (SOTA comparisons, ablations); Referee 2 = theory skeptic (where's the convergence proof?); Referee 3 = reproducibility checker (code, seeds, compute budget)

---

### PHASE 4 -- THREE REFEREE REPORTS (character briefs + in-flight issue labeling)

For each referee: write a character brief, then write the report with in-flight issue IDs assigned to every Major Concern.

Character briefs are required for all three referees. Briefs must pass the swap test: if two briefs could be exchanged without changing any concerns in the reports below them, they are not distinct enough — rewrite.

**Character brief formats:**

For non-diverger referees — free-form brief:
**Referee [N] — [archetype] — Character Brief**
[2-3 sentences: concrete recent reviewing history that anchors this archetype in a specific register — not a label and a disposition, but an event that explains why these concerns land in this register for this paper.]

**Non-diverger brief anti-pattern:**

DO NOT USE (disposition form — fails C-13):
> "Referee 1 is a sympathetic reviewer who values clear statistical reporting. Trained in quantitative psychology, they have a long history of reviewing work at PNAS and appreciate papers that report effect sizes alongside significance tests."

REQUIRED (event form — passes C-13):
> "Referee 1 recently championed a paper at PNAS that was initially desk-rejected for missing effect sizes; they rewrote the desk-rejection notice themselves to give the authors a revision path and were vindicated when the revised version was cited 40 times in the first year. They now approach papers with missing effect sizes as potentially saveable, not automatically weak — but only if the underlying data is there to compute them."

The FORBIDDEN form says what kind of reviewer they are. The REQUIRED form says what happened to them recently that makes their response to this paper's specific features predictable. A brief that could have been written by reading the archetype label alone does not pass C-13.

For the diverger — SEED/EXPAND brief (required):
**Referee [N] — [archetype] — Character Brief**
SEED: [Copy the Phase 2 Brief anchor verbatim here — this must match exactly]
EXPAND: [2-3 sentences that build directly from SEED — how does that specific reviewing history produce the divergence direction committed in Phase 2? EXPAND must derive from SEED. If EXPAND introduces a new independent premise not present in SEED, the linkage has failed. The test: remove SEED; if EXPAND still makes full sense on its own, rewrite EXPAND so that it depends on SEED.]

```
REFEREE [N] — [archetype]
Recommendation: Accept / Major Revision / Minor Revision / Reject
Diverges from Phase 2 commitment: YES / NO — [for the locked diverger: confirm divergence direction; for others: confirm consensus with brief note]

SUMMARY:
[2-3 sentences — the voice and register should be audible from the character brief above; for the diverger the EXPAND content should be legible in the concern framing]

MAJOR CONCERNS:
[I-NN] [Specific, citable — not "needs more rigor" but "Effect size d is not reported in Table 2; practical significance cannot be assessed"]
[I-NN] [...]
[I-NN] [...]

MINOR CONCERNS:
1. [Presentation, framing, missing citations]
2. [...]

SPECIFIC COMMENTS:
Line X: [exact issue]
[...]
```

IDs are continuous across all three reports (never reset per referee). Enforce journal standards ruthlessly:
- PNAS: "Effect size d = X is not reported. Without this, the practical significance of the finding cannot be assessed."
- JCS: "The phenomenological analysis in §3 conflates first-person and third-person descriptions without acknowledging this move."
- Cognitive Science: "The computational model in Figure 2 is described but never formally specified. What are the free parameters?"

---

### PHASE 5 -- FINAL VERDICT

```
Journal: [name]
Likely decision: ACCEPT / MAJOR REVISION / MINOR REVISION / REJECT
Confidence: HIGH / MEDIUM (depends on referee weight at this journal)

Divergence check: [Did the locked diverger diverge as predicted? If prediction held, confirm. If divergence was in a different direction, explain why.]

P1 blockers (reject conditions):
  Issues: I-[NN], I-[NN] — what would cause outright rejection

P2 conditions (major revision requirements):
  Issues: I-[NN], I-[NN] — raised by 2+ referees; consensus issues are hardest to dismiss

Strongest referee: Referee [N] — their objections carry most weight because [REQUIRED: cite a specific fact from this referee's EXPAND content or character brief — their reviewing history, not journal policy]
```

**Rationale form for Strongest referee:**

DO NOT USE (policy form — fails C-15):
> "Referee 2's statistical objections carry most weight because PNAS editors routinely desk-reject on power analysis grounds."

REQUIRED (persona form — passes C-15):
> "Referee 2's statistical objections carry most weight because, as their EXPAND notes, [specific experience from the SEED/EXPAND brief] — this reviewer's pattern makes them structurally less dismissible than journal policy would suggest."

The persona form is checkable against the EXPAND content of the character brief. A rationale that could have been written before Phase 4 existed does not satisfy C-15. When in doubt: would this rationale survive deleting all character briefs? If yes, rewrite.

---

### PHASE 6 -- ISSUE REGISTRY + ORDERED FIX PLAN

**Issue Registry** — compiled from in-flight IDs assigned in Phase 4. Quote exact concern language; do not paraphrase.

| ID | Source | Concern (exact quote) | Severity | Done When |
|----|--------|-----------------------|----------|-----------|
| I-01 | R[N] | "[exact quoted concern from Phase 4]" | P1 / P2 / P3 | [verifiable completion criterion] |
| I-02 | R[N] | "[exact quoted concern from Phase 4]" | P1 / P2 / P3 | [verifiable completion criterion] |
| ... | | | | |

Severity: **P1** = reject condition; **P2** = consensus (2+ referees) or maps to P1 blocker; **P3** = single-referee, non-fatal

**Ordered Fix Plan:**

**Fix 1 — [P1 blocker title]**
Addresses: I-[NN], I-[NN]
Action: [Specific — add Table X with columns Y, Z; run analysis W; rewrite section V]
Done when: [Verifiable — e.g., "Table 2 now reports Cohen's d with 95% CI for all effects; power analysis for N is in Supplementary §S1"]

**Fix 2 — [P2 consensus title]**
Addresses: I-[NN], I-[NN]
Action: [Specific action]
Done when: [Verifiable criterion]

**Fix 3 — [Journal standard]**
Addresses: I-[NN]
Action: [Journal-specific formatting or evidence standard]
Done when: [Verifiable criterion]

Write artifact to: signals/validate/referee/{{topic}}-referee-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: validate-referee, topic: {{topic}}, date: {{date}}, journal: [journal name], verdict: likely-accept|major-revision|reject

---

## V-04 R4 — Combined: C-16 + C-17 for Phase 4 Character Briefs

**Axes**: C-16 + C-17, both applied to Phase 4 only
**Hypothesis**: Phase 4 is the location where the remaining C-16/C-17 gaps co-occur: non-diverger briefs lack the removal-form self-verification test (C-16 gap) and the FORBIDDEN abstract-brief template (C-17 gap). Applying both mechanisms to Phase 4 — a removal test that catches non-load-bearing briefs at generation time, plus a FORBIDDEN example that removes the disposition form as a lower-friction option — targets the two gaps simultaneously at the phase where they originate. The mechanisms do not interfere: the FORBIDDEN example prevents the wrong form from being chosen; the removal test catches it if chosen anyway. Predicts 133+/135; the 2-point gap would be if EXPAND's C-17 vaccination (sketch-independent form) is not addressed.

---

You are running /validate-referee for: {{topic}}

Simulate journal-specific hostile peer review. validate-design uses generic disciplines — this skill knows the difference between a PNAS reviewer demanding effect sizes and a JCS reviewer wanting phenomenological grounding.

---

### PHASE 1 -- SIGNAL ACQUISITION

Glob: signals/**/{topic}-*
Read the paper or draft artifact. Extract: the central claim, the method, the key results, the target journal.

If no journal specified: infer from content style and ask for confirmation before proceeding.

---

### PHASE 2 -- DIVERGENCE COMMITMENT

Before naming the referee panel, lock the structural minority view:

```
DIVERGENCE COMMITMENT (locked before Phase 3)
Journal: [name]
Predicted diverger archetype: [name the archetype from this journal's pool]
Direction: [more hostile than the other two / more sympathetic than the other two]
Reason: [one sentence — what in this paper's design or claims triggers this archetype specifically]
Experiential sketch: [one sentence — the recent reviewing history that primes this archetype to diverge now]
Brief anchor: "[Copy the Experiential sketch sentence here, verbatim, inside quotes. This exact sentence will appear as SEED in the diverger's character brief in Phase 4.]"
```

The Brief anchor is a structural output, not a note. The Phase 4 character brief for the diverger must open with SEED: [this sentence]. If SEED does not match the Brief anchor, the linkage has failed and C-14 is not satisfied. This commitment is locked before Phase 3. At least two distinct recommendation levels must appear across the three reports. Convergence is a simulation failure.

---

### PHASE 3 -- REFEREE ASSIGNMENT

Assign 3 referees with journal-specific archetypes. The archetype from Phase 2 must appear as one of the three.

**Journal profiles:**
- **PNAS / Nature / Science**: Referee 1 = sympathetic-rigorous (wants clean effect sizes, p < 0.05, large N); Referee 2 = hostile statistician (power analysis, multiple comparisons, replication); Referee 3 = breadth skeptic (is this general enough for a broad journal?)
- **Psychological Science / JEP**: Referee 1 = pre-registration enforcer; Referee 2 = effect-size pragmatist (d > 0.4 or why bother?); Referee 3 = ecological validity critic
- **Journal of Consciousness Studies / Phenomenology**: Referee 1 = sympathetic phenomenologist (internal consistency over empirical proof); Referee 2 = hard-nosed analytic philosopher (conceptual precision); Referee 3 = empirical skeptic (where's the data?)
- **Cognitive Science / Topics in Cognitive Science**: Referee 1 = computational modeler (is there a formal model?); Referee 2 = experimental psychologist (ecological validity, individual differences); Referee 3 = interdisciplinary enforcer (does it actually bridge the fields it claims to?)
- **NeurIPS / ICML / AI venues**: Referee 1 = benchmark enforcer (SOTA comparisons, ablations); Referee 2 = theory skeptic (where's the convergence proof?); Referee 3 = reproducibility checker (code, seeds, compute budget)

---

### PHASE 4 -- THREE REFEREE REPORTS (character briefs + in-flight issue labeling)

For each referee: write a character brief, then write the report with in-flight issue IDs assigned to every Major Concern.

Character briefs are required for all three referees.

**Character brief formats:**

For non-diverger referees — free-form brief:
**Referee [N] — [archetype] — Character Brief**
[2-3 sentences: concrete recent reviewing history that anchors this archetype in a specific register. Not a label plus a disposition, but an event that explains why these concerns land here for this paper.]

**Non-diverger brief anti-pattern:**

DO NOT USE (disposition form — fails C-13):
> "Referee 3 is a breadth skeptic who has spent years reviewing interdisciplinary work. They are well-known for asking whether a paper's claims generalize beyond the narrow experimental context in which they were tested."

REQUIRED (event form — passes C-13):
> "Referee 3 was the dissenting reviewer on a high-profile PNAS paper that was later cited as a cautionary example of overclaiming scope from a limited population sample. They had written in that review 'the sample is N=94 undergraduates; the abstract claims to describe human memory' — a line that later appeared in three editorials about replication. They now treat scope claims as the first thing to read, not the last."

The FORBIDDEN form describes a type. The REQUIRED form describes an event that makes the upcoming concerns predictable in their specific register.

Self-verification for non-diverger briefs: After writing each non-diverger brief, remove it and ask — would the report's Summary and at least one Major Concern be phrased differently if this brief existed? If not, the brief is not load-bearing. Rewrite it so that the report demonstrably depends on it.

For the diverger — SEED/EXPAND brief (required):
**Referee [N] — [archetype] — Character Brief**
SEED: [Copy the Phase 2 Brief anchor verbatim here — this must match exactly]
EXPAND: [2-3 sentences that build directly from SEED — how does that specific reviewing history produce the divergence direction committed in Phase 2? EXPAND must derive from SEED. If EXPAND introduces a new independent premise not present in SEED, the linkage has failed. The test: remove SEED; if EXPAND still makes full sense on its own, rewrite EXPAND so that it depends on SEED.]

The SEED/EXPAND format makes C-14 checkable against the artifact: SEED must match Brief anchor; EXPAND must depend on SEED.

```
REFEREE [N] — [archetype]
Recommendation: Accept / Major Revision / Minor Revision / Reject
Diverges from Phase 2 commitment: YES / NO — [for the locked diverger: confirm divergence direction; for others: confirm consensus with brief note]

SUMMARY:
[2-3 sentences — the voice and register should be audible from the character brief above; for the diverger the EXPAND content should be legible in the concern framing]

MAJOR CONCERNS:
[I-NN] [Specific, citable — not "needs more rigor" but "Effect size d is not reported in Table 2; practical significance cannot be assessed"]
[I-NN] [...]
[I-NN] [...]

MINOR CONCERNS:
1. [Presentation, framing, missing citations]
2. [...]

SPECIFIC COMMENTS:
Line X: [exact issue]
[...]
```

IDs are continuous across all three reports (never reset per referee). Enforce journal standards ruthlessly:
- PNAS: "Effect size d = X is not reported. Without this, the practical significance of the finding cannot be assessed."
- JCS: "The phenomenological analysis in §3 conflates first-person and third-person descriptions without acknowledging this move."
- Cognitive Science: "The computational model in Figure 2 is described but never formally specified. What are the free parameters?"

---

### PHASE 5 -- FINAL VERDICT

```
Journal: [name]
Likely decision: ACCEPT / MAJOR REVISION / MINOR REVISION / REJECT
Confidence: HIGH / MEDIUM (depends on referee weight at this journal)

Divergence check: [Did the locked diverger diverge as predicted? If prediction held, confirm. If divergence was in a different direction, explain why.]

P1 blockers (reject conditions):
  Issues: I-[NN], I-[NN] — what would cause outright rejection

P2 conditions (major revision requirements):
  Issues: I-[NN], I-[NN] — raised by 2+ referees; consensus issues are hardest to dismiss

Strongest referee: Referee [N] — their objections carry most weight because [REQUIRED: cite a specific fact from this referee's EXPAND content or character brief — their reviewing history, not journal policy]
```

**Rationale form for Strongest referee:**

DO NOT USE (policy form — fails C-15):
> "Referee 2's statistical objections carry most weight because PNAS editors routinely desk-reject on power analysis grounds."

REQUIRED (persona form — passes C-15):
> "Referee 2's statistical objections carry most weight because, as their EXPAND notes, [specific experience from the SEED/EXPAND brief] — this reviewer's pattern makes them structurally less dismissible than journal policy would suggest."

The persona form is checkable against the EXPAND content of the character brief. A rationale that could have been written before Phase 4 existed does not satisfy C-15. When in doubt: would this rationale survive deleting all character briefs? If yes, rewrite.

---

### PHASE 6 -- ISSUE REGISTRY + ORDERED FIX PLAN

**Issue Registry** — compiled from in-flight IDs assigned in Phase 4. Quote exact concern language; do not paraphrase.

| ID | Source | Concern (exact quote) | Severity | Done When |
|----|--------|-----------------------|----------|-----------|
| I-01 | R[N] | "[exact quoted concern from Phase 4]" | P1 / P2 / P3 | [verifiable completion criterion] |
| I-02 | R[N] | "[exact quoted concern from Phase 4]" | P1 / P2 / P3 | [verifiable completion criterion] |
| ... | | | | |

Severity: **P1** = reject condition; **P2** = consensus (2+ referees) or maps to P1 blocker; **P3** = single-referee, non-fatal

**Ordered Fix Plan:**

**Fix 1 — [P1 blocker title]**
Addresses: I-[NN], I-[NN]
Action: [Specific — add Table X with columns Y, Z; run analysis W; rewrite section V]
Done when: [Verifiable — e.g., "Table 2 now reports Cohen's d with 95% CI for all effects; power analysis for N is in Supplementary §S1"]

**Fix 2 — [P2 consensus title]**
Addresses: I-[NN], I-[NN]
Action: [Specific action]
Done when: [Verifiable criterion]

**Fix 3 — [Journal standard]**
Addresses: I-[NN]
Action: [Journal-specific formatting or evidence standard]
Done when: [Verifiable criterion]

Write artifact to: signals/validate/referee/{{topic}}-referee-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: validate-referee, topic: {{topic}}, date: {{date}}, journal: [journal name], verdict: likely-accept|major-revision|reject

---

## V-05 R4 — Full Systematization: C-16 + C-17 at Every Phase

**Axes**: All — C-16 self-verification at every structural link + C-17 FORBIDDEN examples for every remaining fluent default
**Hypothesis**: V-05 R3 applied C-16 and C-17 to the two hardest links in the artifact chain (SEED/EXPAND and Phase 5 rationale). Three locations remain: non-diverger briefs (lack removal test + lack FORBIDDEN example), EXPAND anti-pattern (has removal test but no FORBIDDEN example), Phase 6 Done When (lacks both). Full systematization gives every structural dependency a generation-time removal test and every fluent failure mode a plausible FORBIDDEN label. The three mechanisms form an unbroken enforcement chain — FORBIDDEN prevents the wrong choice; removal test catches it anyway; the chain is checkable at every link. Predicts 135/135.

---

You are running /validate-referee for: {{topic}}

Simulate journal-specific hostile peer review. validate-design uses generic disciplines — this skill knows the difference between a PNAS reviewer demanding effect sizes and a JCS reviewer wanting phenomenological grounding.

---

### PHASE 1 -- SIGNAL ACQUISITION

Glob: signals/**/{topic}-*
Read the paper or draft artifact. Extract: the central claim, the method, the key results, the target journal.

If no journal specified: infer from content style and ask for confirmation before proceeding.

---

### PHASE 2 -- DIVERGENCE COMMITMENT

Before naming the referee panel, lock the structural minority view:

```
DIVERGENCE COMMITMENT (locked before Phase 3)
Journal: [name]
Predicted diverger archetype: [name the archetype from this journal's pool]
Direction: [more hostile than the other two / more sympathetic than the other two]
Reason: [one sentence — what in this paper's design or claims triggers this archetype specifically]
Experiential sketch: [one sentence — the recent reviewing history that primes this archetype to diverge now]
Brief anchor: "[Copy the Experiential sketch sentence here, verbatim, inside quotes. This exact sentence will appear as SEED in the diverger's character brief in Phase 4.]"
```

The Brief anchor is a structural output, not a note. The Phase 4 character brief for the diverger must open with SEED: [this sentence]. If SEED does not match the Brief anchor, the linkage has failed and C-14 is not satisfied. This commitment is locked before Phase 3. At least two distinct recommendation levels must appear across the three reports. Convergence is a simulation failure.

---

### PHASE 3 -- REFEREE ASSIGNMENT

Assign 3 referees with journal-specific archetypes. The archetype from Phase 2 must appear as one of the three.

**Journal profiles:**
- **PNAS / Nature / Science**: Referee 1 = sympathetic-rigorous (wants clean effect sizes, p < 0.05, large N); Referee 2 = hostile statistician (power analysis, multiple comparisons, replication); Referee 3 = breadth skeptic (is this general enough for a broad journal?)
- **Psychological Science / JEP**: Referee 1 = pre-registration enforcer; Referee 2 = effect-size pragmatist (d > 0.4 or why bother?); Referee 3 = ecological validity critic
- **Journal of Consciousness Studies / Phenomenology**: Referee 1 = sympathetic phenomenologist (internal consistency over empirical proof); Referee 2 = hard-nosed analytic philosopher (conceptual precision); Referee 3 = empirical skeptic (where's the data?)
- **Cognitive Science / Topics in Cognitive Science**: Referee 1 = computational modeler (is there a formal model?); Referee 2 = experimental psychologist (ecological validity, individual differences); Referee 3 = interdisciplinary enforcer (does it actually bridge the fields it claims to?)
- **NeurIPS / ICML / AI venues**: Referee 1 = benchmark enforcer (SOTA comparisons, ablations); Referee 2 = theory skeptic (where's the convergence proof?); Referee 3 = reproducibility checker (code, seeds, compute budget)

---

### PHASE 4 -- THREE REFEREE REPORTS (character briefs + in-flight issue labeling)

For each referee: write a character brief, then write the report with in-flight issue IDs assigned to every Major Concern.

Character briefs are required for all three referees.

**Character brief formats:**

For non-diverger referees — free-form brief:
**Referee [N] — [archetype] — Character Brief**
[2-3 sentences: a specific recent reviewing event that anchors this archetype's concerns in a register — not a label plus a disposition, but something that happened to this person that makes their response to this paper's specific features predictable.]

**Non-diverger brief anti-pattern:**

DO NOT USE (disposition form — fails C-13):
> "Referee 1 is a pre-registration enforcer who values methodological transparency. They have a long history of flagging papers that lack pre-registered hypotheses and routinely request that authors share their data."

REQUIRED (event form — passes C-13):
> "Referee 1 co-authored the 2023 replication of a widely-cited priming study that failed to reproduce — the original paper had no pre-registration and the analysis appeared tailored to the significant result. Since then they have treated any paper without pre-registration as a paper where the reported hypotheses may not be the original hypotheses, and they ask for OSF links in every review they write."

The FORBIDDEN form describes a type. The REQUIRED form names an event that makes the reviewer's specific reaction to this paper's specific features predictable. A brief that could have been generated by reading the archetype label alone does not pass.

Self-verification for non-diverger briefs: After writing each non-diverger brief, remove it and ask — if this brief did not exist, would at least one Major Concern in the report below it be phrased or weighted differently? If the concerns would be identical either way, the brief is not load-bearing — rewrite it so that the report depends on it.

For the diverger — SEED/EXPAND brief (required):
**Referee [N] — [archetype] — Character Brief**
SEED: [Copy the Phase 2 Brief anchor verbatim here — this must match exactly]
EXPAND: [2-3 sentences that build directly from SEED — how does that specific reviewing history produce the divergence direction committed in Phase 2? EXPAND must derive from SEED.]

**EXPAND anti-pattern:**

DO NOT USE (new-premise EXPAND — fails C-14):
If SEED = "After reviewing three high-profile replication failures at PNAS in 2024, this reviewer treats any N < 200 study as presumptively underpowered until a prospective power analysis appears."
FORBIDDEN EXPAND: "This reviewer also brings expertise from clinical trial design, where power analysis is a prerequisite for IRB approval, giving them a practical rather than theoretical objection to underpowered studies."

REQUIRED EXPAND: "With that track record of watching N < 200 studies fail, this reviewer will read the N=87 in §3 as a pattern they have seen before, not a design choice to evaluate fresh — their minority position will push harder on the power analysis question specifically because they have personally documented this failure mode three times in the past year."

The FORBIDDEN EXPAND introduces clinical trial expertise — a premise absent from SEED. The REQUIRED EXPAND derives the divergence behavior from the SEED event directly. Test: remove SEED; if EXPAND still makes full sense on its own, it introduced a new premise — rewrite EXPAND so that it depends on SEED.

```
REFEREE [N] — [archetype]
Recommendation: Accept / Major Revision / Minor Revision / Reject
Diverges from Phase 2 commitment: YES / NO — [for the locked diverger: confirm divergence direction; for others: confirm consensus with brief note]

SUMMARY:
[2-3 sentences — the voice and register should be audible from the character brief above; for the diverger the EXPAND content should be legible in the concern framing]

MAJOR CONCERNS:
[I-NN] [Specific, citable — not "needs more rigor" but "Effect size d is not reported in Table 2; practical significance cannot be assessed"]
[I-NN] [...]
[I-NN] [...]

MINOR CONCERNS:
1. [Presentation, framing, missing citations]
2. [...]

SPECIFIC COMMENTS:
Line X: [exact issue]
[...]
```

IDs are continuous across all three reports (never reset per referee). Enforce journal standards ruthlessly:
- PNAS: "Effect size d = X is not reported. Without this, the practical significance of the finding cannot be assessed."
- JCS: "The phenomenological analysis in §3 conflates first-person and third-person descriptions without acknowledging this move."
- Cognitive Science: "The computational model in Figure 2 is described but never formally specified. What are the free parameters?"

---

### PHASE 5 -- FINAL VERDICT

```
Journal: [name]
Likely decision: ACCEPT / MAJOR REVISION / MINOR REVISION / REJECT
Confidence: HIGH / MEDIUM (depends on referee weight at this journal)

Divergence check: [Did the locked diverger diverge as predicted? If prediction held, confirm. If divergence was in a different direction, explain why.]

P1 blockers (reject conditions):
  Issues: I-[NN], I-[NN] — what would cause outright rejection

P2 conditions (major revision requirements):
  Issues: I-[NN], I-[NN] — raised by 2+ referees; consensus issues are hardest to dismiss

Strongest referee: Referee [N] — their objections carry most weight because [REQUIRED: cite a specific fact from this referee's EXPAND content or character brief — their reviewing history, not journal policy]
```

**Rationale form for Strongest referee:**

DO NOT USE (policy form — fails C-15):
> "Referee 2's statistical objections carry most weight because PNAS editors routinely desk-reject on power analysis grounds."

REQUIRED (persona form — passes C-15):
> "Referee 2's statistical objections carry most weight because, as their EXPAND notes, [specific experience from the SEED/EXPAND brief] — this reviewer's pattern makes them structurally less dismissible than journal policy would suggest."

The persona form is checkable against the EXPAND content of the character brief. A rationale that could have been written before Phase 4 existed does not satisfy C-15. When in doubt: remove all character briefs from the artifact; if this rationale is still legible, rewrite it so it depends on the brief.

---

### PHASE 6 -- ISSUE REGISTRY + ORDERED FIX PLAN

**Issue Registry** — compiled from in-flight IDs assigned in Phase 4. Quote exact concern language; do not paraphrase.

| ID | Source | Concern (exact quote) | Severity | Done When |
|----|--------|-----------------------|----------|-----------|
| I-01 | R[N] | "[exact quoted concern from Phase 4]" | P1 / P2 / P3 | [verifiable completion criterion] |
| I-02 | R[N] | "[exact quoted concern from Phase 4]" | P1 / P2 / P3 | [verifiable completion criterion] |
| ... | | | | |

Severity: **P1** = reject condition; **P2** = consensus (2+ referees) or maps to P1 blocker; **P3** = single-referee, non-fatal

**Done When anti-pattern:**

DO NOT USE (vague form — fails C-12):
> "Done when the authors have addressed the statistical power concern and provided evidence that the sample is adequate for the claims made."

REQUIRED (specific form — passes C-12):
> "Done when Table 2 reports Cohen's d with 95% CI for all three primary effects AND Supplementary §S1 contains a prospective power analysis demonstrating that N=87 achieves >= 80% power for d >= 0.35 at alpha = 0.05."

The FORBIDDEN form is satisfied by any revision that acknowledges the concern. The REQUIRED form names a table, a section, a metric, and a threshold that a referee can verify by inspection without reading the cover letter.

Self-verification for Done When criteria: After writing each Done When entry, remove the specific table number, section identifier, or threshold value from it. If the remaining text still reads as a complete action criterion, the entry is too vague — rewrite it to name at least one specific artifact (Table N, Supplementary §SN, Figure N panel) and at least one measurable threshold.

**Ordered Fix Plan:**

**Fix 1 — [P1 blocker title]**
Addresses: I-[NN], I-[NN]
Action: [Specific — add Table X with columns Y, Z; run analysis W; rewrite section V]
Done when: [Verifiable — e.g., "Table 2 now reports Cohen's d with 95% CI for all effects; power analysis for N is in Supplementary §S1"]

**Fix 2 — [P2 consensus title]**
Addresses: I-[NN], I-[NN]
Action: [Specific action]
Done when: [Verifiable criterion]

**Fix 3 — [Journal standard]**
Addresses: I-[NN]
Action: [Journal-specific formatting or evidence standard]
Done when: [Verifiable criterion]

Write artifact to: signals/validate/referee/{{topic}}-referee-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: validate-referee, topic: {{topic}}, date: {{date}}, journal: [journal name], verdict: likely-accept|major-revision|reject
