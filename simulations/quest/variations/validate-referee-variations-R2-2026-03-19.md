Round 2 variations written to `simulations/quest/variations/validate-referee-variations-R2-2026-03-19.md`.

---

## validate-referee — Round 2 Variations Summary

**Rubric ceiling**: 115 (v1 max 100 + C-11/5 + C-12/5 + C-13/5)

### Single-axis variations

| Variation | Axis | Primary criterion targeted | Key change from R1 |
|-----------|------|---------------------------|-------------------|
| **V-01 R2** | Role sequence | C-11 (+ C-13 for diverger) | Divergence commitment moves to *before* archetype assignment — makes it impossible to assign a panel that neutralizes divergence |
| **V-02 R2** | Lifecycle emphasis | C-12 | Issues labeled with I-NN IDs *as they are written* in Phase 3; verdict and fix plan reference IDs exclusively — eliminates retrospective drift |
| **V-03 R2** | Phrasing register | C-13 | Required 2-3 sentence character brief before *each* referee report (all three, not just the diverger); brief must be audible in concern register |

### Combined variations

| Variation | Axes | Criteria | Hypothesis |
|-----------|------|----------|------------|
| **V-04 R2** | Role sequence + lifecycle emphasis | C-11 + C-12 | Early divergence lock + in-flight registry close both main R1 failure modes (C-07/C-10 unenforced, C-08 prose-only); predicts 110+ |
| **V-05 R2** | All three | C-11 + C-12 + C-13 | All three new criteria are compositionally compatible; the diverger's character brief (C-13) explains the divergence commitment (C-11), which is then captured in a richer registry (C-12); predicts 115/115 |

### Design rationale

- **All variations preserve R1 V-01's divergence enforcement** (explicit rule that at least two recommendation levels must appear) — this is what fixed C-07/C-10 at zero cost in R1, and it should carry through
- **V-01 R2 vs V-01 R1 difference**: The commitment now precedes panel assignment, not just reports — the prediction constrains *which archetypes are selected*, not just how they behave
- **V-02 R2 vs V-03 R1 difference**: Labels appear at write-time in the report body (not as a post-hoc table built from memory) — traceability is structurally enforced
- **V-03 R2 vs V-04 R1 difference**: V-04 R1 had one coaching instruction; V-03 R2 has a per-referee required output block with an explicit quality bar ("if two briefs could be swapped without changing concerns, rewrite")
y eliminate the two biggest gaps in R1 non-winners (C-07/C-10 weak, C-08 prose-only).

**V-05 R2 — All Three New Criteria (C-11 + C-12 + C-13)**
Combines all three: early divergence commitment (C-11), in-flight issue labeling and labeled registry (C-12), character briefs for all three referees (C-13). Hypothesis: all three v2 additions are compositionally compatible and do not degrade C-01 through C-10 essential compliance; the character brief and divergence commitment reinforce each other (the diverger's brief explains why they diverge).

---

## V-01 R2 — Role Sequence: Early Divergence Lock

**Axis**: Role sequence — divergence commitment before archetype assignment (earlier than V-01 R1)
**Hypothesis**: Committing to a diverger archetype and experiential sketch *before* selecting the referee panel prevents the model from unconsciously assigning archetypes that neutralize divergence. V-01 R1 predicted outlier after assignment; this version forces the prediction to constrain assignment.

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

Before naming the referee panel, commit to the structural minority view. Based on the paper content and target journal alone:

```
DIVERGENCE COMMITMENT (locked before Phase 3)
Journal: [name]
Predicted diverger archetype: [name the archetype from this journal's pool — e.g., "hostile statistician"]
Direction: [more hostile than the other two / more sympathetic than the other two]
Reason: [one sentence — what in this paper's design, framing, or results triggers this archetype specifically]
Experiential sketch: [one sentence — what recent reviewing history primes this archetype to diverge now, e.g., "this reviewer recently handled three manuscripts where power analyses looked sufficient until replication failed"]
```

This commitment is locked before Phase 3. The report written for this archetype must visibly differ from the other two in recommendation level or emphasis. If all three reports converge, that is a simulation failure — explain what overrode the commitment.

---

### PHASE 3 -- REFEREE ASSIGNMENT

Assign 3 referees with journal-specific archetypes. The archetype named in Phase 2 must appear as one of the three.

**Journal profiles:**
- **PNAS / Nature / Science**: Referee 1 = sympathetic-rigorous (wants clean effect sizes, p < 0.05, large N); Referee 2 = hostile statistician (power analysis, multiple comparisons, replication); Referee 3 = breadth skeptic (is this general enough for a broad journal?)
- **Psychological Science / JEP**: Referee 1 = pre-registration enforcer; Referee 2 = effect-size pragmatist (d > 0.4 or why bother?); Referee 3 = ecological validity critic
- **Journal of Consciousness Studies / Phenomenology**: Referee 1 = sympathetic phenomenologist (internal consistency over empirical proof); Referee 2 = hard-nosed analytic philosopher (conceptual precision); Referee 3 = empirical skeptic (where's the data?)
- **Cognitive Science / Topics in Cognitive Science**: Referee 1 = computational modeler (is there a formal model?); Referee 2 = experimental psychologist (ecological validity, individual differences); Referee 3 = interdisciplinary enforcer (does it actually bridge the fields it claims to?)
- **NeurIPS / ICML / AI venues**: Referee 1 = benchmark enforcer (SOTA comparisons, ablations); Referee 2 = theory skeptic (where's the convergence proof?); Referee 3 = reproducibility checker (code, seeds, compute budget)

---

### PHASE 4 -- THREE REFEREE REPORTS

Write each report. The locked diverger must produce a report that visibly differs from the other two in recommendation level or emphasis — at least two distinct recommendation levels must appear across the three reports. The diverger's report should reflect the experiential sketch from Phase 2 in the register of their concerns.

For each referee:

```
REFEREE [N] — [archetype]
Recommendation: Accept / Major Revision / Minor Revision / Reject
Diverges from Phase 2 commitment: YES / NO — [if the diverger: confirm or explain deviation; if non-diverger: confirm consensus]

SUMMARY:
[2-3 sentences: what the paper does and this referee's overall reaction]

MAJOR CONCERNS:
1. [Specific, citable — not "needs more rigor" but "Effect size d is not reported in Table 2; practical significance cannot be assessed"]
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

### PHASE 5 -- FINAL VERDICT

Update the Phase 2 prediction with what the reports actually showed:

```
Journal: [name]
Likely decision: ACCEPT / MAJOR REVISION / MINOR REVISION / REJECT
Confidence: HIGH / MEDIUM (depends on referee weight at this journal)

Divergence check: [Did the locked diverger diverge as predicted? If prediction held, say so. If not, explain what in the reports overrode the Phase 2 commitment.]

P1 blockers (reject conditions):
  [What would cause outright rejection — must fix before resubmission]

P2 conditions (major revision requirements):
  [What 2+ referees flagged — consensus issues are hardest to dismiss]

Strongest referee: Referee [N] — their objections carry most weight because [reason grounded in this journal's editorial process]
```

---

### PHASE 6 -- AMEND

Three targeted pre-submission fixes ordered by blocking severity:
1. [Fix that addresses the most likely reject condition]
2. [Fix that addresses the consensus P2 across referees]
3. [Fix that addresses the journal's specific formatting/evidence standard]

Write artifact to: signals/validate/referee/{{topic}}-referee-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: validate-referee, topic: {{topic}}, date: {{date}}, journal: [journal name], verdict: likely-accept|major-revision|reject

---

## V-02 R2 — Lifecycle Emphasis: In-flight Issue Registry

**Axis**: Lifecycle emphasis — Issue Registry built during Phase 3 (concerns labeled as they are written), not retrospectively in Phase 5
**Hypothesis**: Labeling concerns with I-NN IDs at the moment of writing (not afterward) forces every Major Concern to be traceable from report through verdict through fix plan. Retrospective labeling (V-03 R1) allows the fix plan to drift from what the reports actually said. In-flight labeling eliminates that gap.

---

You are running /validate-referee for: {{topic}}

Simulate journal-specific hostile peer review. validate-design uses generic disciplines — this skill knows the difference between a PNAS reviewer demanding effect sizes and a JCS reviewer wanting phenomenological grounding.

---

### PHASE 1 -- SIGNAL ACQUISITION

Glob: signals/**/{topic}-*
Read the paper or draft artifact. Extract: the central claim, the method, the key results, the target journal.

If no journal specified: infer from content style and ask for confirmation before proceeding.

---

### PHASE 2 -- REFEREE ASSIGNMENT + DIVERGENCE PREDICTION

Based on the target journal, assign 3 referees with journal-specific archetypes:

**Journal profiles:**
- **PNAS / Nature / Science**: Referee 1 = sympathetic-rigorous; Referee 2 = hostile statistician; Referee 3 = breadth skeptic
- **Psychological Science / JEP**: Referee 1 = pre-registration enforcer; Referee 2 = effect-size pragmatist; Referee 3 = ecological validity critic
- **Journal of Consciousness Studies / Phenomenology**: Referee 1 = sympathetic phenomenologist; Referee 2 = hard-nosed analytic philosopher; Referee 3 = empirical skeptic
- **Cognitive Science / Topics in Cognitive Science**: Referee 1 = computational modeler; Referee 2 = experimental psychologist; Referee 3 = interdisciplinary enforcer
- **NeurIPS / ICML / AI venues**: Referee 1 = benchmark enforcer; Referee 2 = theory skeptic; Referee 3 = reproducibility checker

Before writing reports, commit: which referee archetype is most likely to diverge from the other two, and why? This commitment is locked — at least one report must visibly differ in recommendation level or emphasis, producing at least two distinct recommendation levels across the three reports.

```
Predicted outlier: Referee [N] — [archetype] — [direction: more hostile / more sympathetic] — [one sentence reason]
```

---

### PHASE 3 -- THREE REFEREE REPORTS (with in-flight issue labeling)

For each referee, produce a report. As you write each Major Concern, assign it a unique issue ID in sequence across all three reports (I-01, I-02, I-03, ... — never reset per referee). These IDs will drive the verdict and fix plan.

```
REFEREE [N] — [archetype]
Recommendation: Accept / Major Revision / Minor Revision / Reject

SUMMARY:
[2-3 sentences: what the paper does and this referee's overall reaction]

MAJOR CONCERNS:
[I-NN] [Specific, citable concern — name the gap, the missing analysis, the logical flaw]
[I-NN] [...]
[I-NN] [...]

MINOR CONCERNS:
1. [Presentation, framing, missing citations]
2. [...]

SPECIFIC COMMENTS:
Line X: [exact issue]
[...]
```

IDs are continuous across all three reports. The same concern raised by two referees gets two different IDs, but both will be flagged P2 in Phase 5.

Enforce journal standards ruthlessly:
- PNAS: "Effect size d = X is not reported. Without this, the practical significance of the finding cannot be assessed."
- JCS: "The phenomenological analysis in §3 conflates first-person and third-person descriptions without acknowledging this move."
- Cognitive Science: "The computational model in Figure 2 is described but never formally specified. What are the free parameters?"

---

### PHASE 4 -- VERDICT

Reference issue IDs from Phase 3 directly:

```
Journal: [name]
Likely decision: ACCEPT / MAJOR REVISION / MINOR REVISION / REJECT
Confidence: HIGH / MEDIUM (depends on referee weight at this journal)

P1 blockers (reject conditions):
  Issues: [I-NN, I-NN] — must fix before resubmission

P2 conditions (major revision requirements):
  Issues: [I-NN, I-NN] — raised by 2+ referees; consensus issues are hardest to dismiss

Strongest referee: Referee [N] — their objections carry most weight because [reason grounded in this journal's editorial process]
```

---

### PHASE 5 -- ISSUE REGISTRY + ORDERED FIX PLAN

Compile all Major Concerns from Phase 3 into a labeled registry. Populate from the I-NN IDs assigned in-flight — do not paraphrase, quote exactly.

**Issue Registry:**

| ID | Source | Concern (exact quote) | Severity | Done When |
|----|--------|-----------------------|----------|-----------|
| I-01 | R[N] | "[exact quoted concern from Phase 3]" | P1 / P2 / P3 | [verifiable completion criterion] |
| I-02 | R[N] | "[exact quoted concern from Phase 3]" | P1 / P2 / P3 | [verifiable completion criterion] |
| ... | | | | |

Severity:
- **P1**: Reject condition — unfixed, the paper gets rejected
- **P2**: Two or more referees raised this (or it maps to a P1 blocker) — editors weight consensus heavily
- **P3**: Single-referee concern — should fix, not fatal

**Ordered Fix Plan:**

**Fix 1 — [P1 blocker title]**
Addresses: I-[NN], I-[NN]
Action: [Specific — add Table X, run analysis Y, rewrite section Z]
Done when: [Verifiable — e.g., "Table 2 now reports Cohen's d with 95% CI for all effects"]

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

## V-03 R2 — Phrasing Register: Character Brief Before Each Report

**Axis**: Phrasing register — required character brief before each referee report grounds all three archetypes in concrete recent experience
**Hypothesis**: Abstract archetype labels ("hostile statistician") permit persona collapse — all three referees end up voicing the same generic skepticism. A required 2-3 sentence character brief, written before each report, prevents this by anchoring each archetype in a specific reviewing history that shapes the register of their concerns.

---

You are running /validate-referee for: {{topic}}

Simulate journal-specific hostile peer review. validate-design uses generic disciplines — this skill knows the difference between a PNAS reviewer demanding effect sizes and a JCS reviewer wanting phenomenological grounding.

---

### PHASE 1 -- SIGNAL ACQUISITION

Glob: signals/**/{topic}-*
Read the paper or draft artifact. Extract: the central claim, the method, the key results, the target journal.

If no journal specified: infer from content style and ask for confirmation before proceeding.

---

### PHASE 2 -- REFEREE ASSIGNMENT + DIVERGENCE PREDICTION

Based on the target journal, assign 3 referees with journal-specific archetypes:

**Journal profiles:**
- **PNAS / Nature / Science**: Referee 1 = sympathetic-rigorous; Referee 2 = hostile statistician; Referee 3 = breadth skeptic
- **Psychological Science / JEP**: Referee 1 = pre-registration enforcer; Referee 2 = effect-size pragmatist; Referee 3 = ecological validity critic
- **Journal of Consciousness Studies / Phenomenology**: Referee 1 = sympathetic phenomenologist; Referee 2 = hard-nosed analytic philosopher; Referee 3 = empirical skeptic
- **Cognitive Science / Topics in Cognitive Science**: Referee 1 = computational modeler; Referee 2 = experimental psychologist; Referee 3 = interdisciplinary enforcer
- **NeurIPS / ICML / AI venues**: Referee 1 = benchmark enforcer; Referee 2 = theory skeptic; Referee 3 = reproducibility checker

Before writing reports, commit: which referee archetype is most likely to diverge from the other two, and why? At least two distinct recommendation levels must appear across the three reports.

```
Predicted outlier: Referee [N] — [archetype] — [direction] — [one sentence reason]
```

---

### PHASE 3 -- THREE REFEREE REPORTS (with character briefs)

Before each referee's report, write a character brief. The brief grounds the archetype in concrete current experience. Abstract labels allow hedging; the brief prevents it.

For each referee, this two-part structure is required:

**Referee [N] — [archetype] — Character Brief**
[2-3 sentences: Who is this person right now? What have they recently reviewed or handled that sharpens their priors for exactly this kind of paper? Be concrete, not categorical — not "skeptical of statistics" but "this reviewer recently handled three retraction requests where significance was achieved via selective outcome reporting, and they have since adopted a personal policy of requiring pre-registration verification for any p < 0.05 near the threshold." The brief must create a distinct voice the report can inhabit — if two character briefs could be swapped without changing any concerns, they are not distinct enough.]

```
REFEREE [N] — [archetype]
Recommendation: Accept / Major Revision / Minor Revision / Reject

SUMMARY:
[2-3 sentences: what the paper does and this referee's overall reaction — the summary voice should reflect the character brief above]

MAJOR CONCERNS:
1. [Specific, citable — not "needs more rigor" but "Effect size d is not reported in Table 2; practical significance cannot be assessed"]
2. [...]
3. [...]

MINOR CONCERNS:
1. [Presentation, framing, missing citations]
2. [...]

SPECIFIC COMMENTS:
Line X: [exact issue]
[...]
```

The character brief must be audible in how the concerns are voiced — a referee whose brief describes recent failed replications should raise power analysis concerns in that register, not in generic statistical language. The brief is not decoration; it determines voice.

Enforce journal standards ruthlessly:
- PNAS: "Effect size d = X is not reported. Without this, the practical significance of the finding cannot be assessed."
- JCS: "The phenomenological analysis in §3 conflates first-person and third-person descriptions without acknowledging this move."
- Cognitive Science: "The computational model in Figure 2 is described but never formally specified. What are the free parameters?"

---

### PHASE 4 -- VERDICT

```
Journal: [name]
Likely decision: ACCEPT / MAJOR REVISION / MINOR REVISION / REJECT
Confidence: HIGH / MEDIUM (depends on referee weight at this journal)

P1 blockers (reject conditions):
  [What would cause outright rejection — must fix before resubmission]

P2 conditions (major revision requirements):
  [What 2+ referees flagged — consensus issues are hardest to dismiss]

Strongest referee: Referee [N] — their objections carry most weight because [reason grounded in this journal's editorial process]
```

---

### PHASE 5 -- AMEND

Three targeted pre-submission fixes ordered by blocking severity:
1. [Fix that addresses the most likely reject condition]
2. [Fix that addresses the consensus P2 across referees]
3. [Fix that addresses the journal's specific formatting/evidence standard]

Write artifact to: signals/validate/referee/{{topic}}-referee-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: validate-referee, topic: {{topic}}, date: {{date}}, journal: [journal name], verdict: likely-accept|major-revision|reject

---

## V-04 R2 — Combined: Early Divergence Lock + In-flight Registry (C-11 + C-12)

**Axes**: Role sequence + lifecycle emphasis
**Hypothesis**: C-11 (divergence committed before panel assignment) and C-12 (issues labeled in-flight, registry with Done-when) are compositionally compatible and do not create structural tension. Together they close the two main gaps from R1 non-winners: C-07/C-10 (divergence not enforced) and C-08 (prose fix list with no verifiable completion criteria). Predicts 110+/115.

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
```

This commitment is locked. The report written for this archetype must visibly differ from the other two in recommendation level or emphasis, producing at least two distinct recommendation levels across the three reports. If all three reports converge, that is a simulation failure — explain what overrode the commitment.

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

### PHASE 4 -- THREE REFEREE REPORTS (with in-flight issue labeling)

Write each report. The locked diverger must produce a report visibly different from the other two. As you write each Major Concern, assign it a unique issue ID in sequence across all three reports (I-01, I-02, ... — never reset per referee). These IDs are live references used in Phase 5 and Phase 6.

```
REFEREE [N] — [archetype]
Recommendation: Accept / Major Revision / Minor Revision / Reject
Diverges from Phase 2 commitment: YES / NO — [for the locked diverger: confirm divergence; for others: confirm consensus]

SUMMARY:
[2-3 sentences: what the paper does and this referee's overall reaction]

MAJOR CONCERNS:
[I-NN] [Specific, citable — not "needs more rigor" but "Effect size d is not reported in Table 2"]
[I-NN] [...]
[I-NN] [...]

MINOR CONCERNS:
1. [Presentation, framing, missing citations]
2. [...]

SPECIFIC COMMENTS:
Line X: [exact issue]
[...]
```

IDs continuous across all three reports. Enforce journal standards ruthlessly:
- PNAS: "Effect size d = X is not reported. Without this, the practical significance of the finding cannot be assessed."
- JCS: "The phenomenological analysis in §3 conflates first-person and third-person descriptions without acknowledging this move."
- Cognitive Science: "The computational model in Figure 2 is described but never formally specified. What are the free parameters?"

---

### PHASE 5 -- FINAL VERDICT

```
Journal: [name]
Likely decision: ACCEPT / MAJOR REVISION / MINOR REVISION / REJECT
Confidence: HIGH / MEDIUM (depends on referee weight at this journal)

Divergence check: [Did the locked diverger diverge as predicted? If prediction held, confirm. If not, explain what overrode the Phase 2 commitment.]

P1 blockers (reject conditions):
  Issues: I-[NN], I-[NN] — what would cause outright rejection

P2 conditions (major revision requirements):
  Issues: I-[NN], I-[NN] — raised by 2+ referees; consensus issues are hardest to dismiss

Strongest referee: Referee [N] — their objections carry most weight because [reason grounded in this journal's editorial process]
```

---

### PHASE 6 -- ISSUE REGISTRY + ORDERED FIX PLAN

**Issue Registry** — compiled from in-flight IDs assigned in Phase 4:

| ID | Source | Concern (exact quote) | Severity | Done When |
|----|--------|-----------------------|----------|-----------|
| I-01 | R[N] | "[exact quoted concern from Phase 4]" | P1 / P2 / P3 | [verifiable completion criterion] |
| I-02 | R[N] | "[exact quoted concern from Phase 4]" | P1 / P2 / P3 | [verifiable completion criterion] |
| ... | | | | |

Severity: **P1** = reject condition; **P2** = consensus (2+ referees or maps to P1 blocker); **P3** = single-referee, non-fatal

**Ordered Fix Plan:**

**Fix 1 — [P1 blocker title]**
Addresses: I-[NN], I-[NN]
Action: [Specific — add Table X, run analysis Y, rewrite section Z]
Done when: [Verifiable — e.g., "Table 2 now reports Cohen's d with 95% CI for all effects in §4"]

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

## V-05 R2 — Combined: All Three New Criteria (C-11 + C-12 + C-13)

**Axes**: Role sequence + lifecycle emphasis + phrasing register
**Hypothesis**: All three v2 additions are compositionally compatible. Character briefs for all three referees (C-13) reinforce the divergence commitment (C-11) — the diverger's brief explains *why* they diverge. The in-flight registry (C-12) then captures concerns voiced in the brief's register, making the issue table richer and more specific than a generic fix list. Predicts 115/115 — mastery-level output.

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
Experiential sketch: [one sentence — the recent reviewing history that primes this archetype to diverge now — this sketch will become the core of that referee's character brief in Phase 4]
```

This commitment is locked before Phase 3. The report written for this archetype must visibly differ from the other two in recommendation level or emphasis, producing at least two distinct recommendation levels across the three reports. If all three reports converge, that is a simulation failure.

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

The character brief is not optional and not decorative. It answers: who is this person right now, and what recent reviewing experience makes their concerns land in this specific register rather than a generic one? If two briefs could be swapped without changing any concerns in the reports below them, the briefs are not distinct enough — rewrite.

For each referee, this three-part structure is required:

**Referee [N] — [archetype] — Character Brief**
[2-3 sentences: concrete recent reviewing history that primes this archetype for exactly this paper. Not "skeptical of statistics" but "this reviewer recently served on an appeals committee for three papers where p-values near 0.05 failed to replicate, and they now treat any threshold-adjacent significance claim as presumptively fragile until effect sizes and confidence intervals are visible." For the Phase 2 diverger, the brief must explain why they will diverge — make the Phase 2 experiential sketch the foundation of this paragraph.]

```
REFEREE [N] — [archetype]
Recommendation: Accept / Major Revision / Minor Revision / Reject
Diverges from Phase 2 commitment: YES / NO — [for the locked diverger: confirm divergence direction; for others: confirm consensus with brief note]

SUMMARY:
[2-3 sentences — the voice and register should be audible from the character brief above]

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

IDs are continuous across all three reports (never reset per referee). The character brief must be audible in the concern language — a reviewer whose brief describes recent retraction experience should voice statistical concerns in that register, not in textbook statistical language.

Enforce journal standards ruthlessly:
- PNAS: "Effect size d = X is not reported. Without this, the practical significance of the finding cannot be assessed."
- JCS: "The phenomenological analysis in §3 conflates first-person and third-person descriptions without acknowledging this move."
- Cognitive Science: "The computational model in Figure 2 is described but never formally specified. What are the free parameters?"

---

### PHASE 5 -- FINAL VERDICT

```
Journal: [name]
Likely decision: ACCEPT / MAJOR REVISION / MINOR REVISION / REJECT
Confidence: HIGH / MEDIUM (depends on referee weight at this journal)

Divergence check: [Did the locked diverger diverge as predicted? If prediction held, confirm. If divergence was in a different direction than predicted, explain why.]

P1 blockers (reject conditions):
  Issues: I-[NN], I-[NN] — what would cause outright rejection

P2 conditions (major revision requirements):
  Issues: I-[NN], I-[NN] — raised by 2+ referees; consensus issues are hardest to dismiss

Strongest referee: Referee [N] — their objections carry most weight because [reason grounded in this journal's editorial process — connect to the archetype's reviewing history if the character brief illuminates why]
```

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
