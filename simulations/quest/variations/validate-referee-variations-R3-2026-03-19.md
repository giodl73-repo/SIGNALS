**validate-referee R3 variations written** to `simulations/quest/variations/validate-referee-variations-R3-2026-03-19.md`.

---

## Summary

**Ceiling**: 125 (v2 115 + C-14/5 + C-15/5)

**R2 baseline gap**: V-05 R2 hit 115/115, but C-14 and C-15 were advisory, not structural. Two failure modes:
- C-14: "make the sketch the foundation" can be satisfied by writing C-11 and C-13 independently
- C-15: "if the character brief illuminates why" makes persona-grounded rationale opt-in; policy form is the fluent default

### Variation map

| ID | Axis | Mechanism | Target |
|----|------|-----------|--------|
| **V-01 R3** | Role sequence | `Brief anchor:` output field in Phase 2 — Phase 4 must open diverger's brief with it verbatim | C-14 |
| **V-02 R3** | Lifecycle emphasis | Forbidden/required template in Phase 5 — policy form labeled DO NOT USE, persona form labeled REQUIRED | C-15 |
| **V-03 R3** | Phrasing register | SEED/EXPAND two-part format for diverger's brief — SEED quotes Phase 2 sketch; EXPAND must derive from SEED | C-14 |
| **V-04 R3** | Role seq + lifecycle | V-01 + V-02 combined — Brief anchor (C-14) + forbidden template (C-15) | C-14 + C-15 |
| **V-05 R3** | All three | V-01 + V-02 + V-03 — full chain: sketch → Brief anchor → SEED → EXPAND → persona rationale | C-14 + C-15 |

**Key design decision**: V-05 R3's SEED/EXPAND format is stronger than V-01 R3's Brief anchor alone because EXPAND's dependency on SEED is itself enforced ("remove SEED; if EXPAND still makes full sense on its own, rewrite EXPAND"). The chain is checkable at every link.
---------|------------|
| **V-04 R3** | Role sequence + lifecycle emphasis | C-14 + C-15 | Brief-anchor quotation (C-14) and forbidden-policy template (C-15) target different phases and different failure modes — composing them adds no structural tension; predicts 122+/125 |
| **V-05 R3** | All three | C-14 + C-15 + phrasing register | SEED/EXPAND format (phrasing) makes the Phase 2 quote visible in the output (role sequence), which flows forward to anchor the persona-specific rationale in Phase 5 (lifecycle); the three mechanisms form a causal chain through the artifact; predicts 125/125 |

### Design rationale

- **All variations inherit V-05 R2 in full** — C-01 through C-13 are already at ceiling; the only open points are C-14 (5) and C-15 (5)
- **C-14 failure mode in V-05 R2**: "make the Phase 2 sketch the foundation" is an aspiration, not an enforcement rule; a model can write C-11 and C-13 independently and still comply with the letter of the instruction
- **C-15 failure mode in V-05 R2**: "if the character brief illuminates why" makes brief-grounded rationale opt-in; abstract policy language ("PNAS editors desk-reject") is easier to generate and will dominate when the "if" is not triggered
- **V-01 R3 vs V-05 R2**: Adds a `Brief anchor:` output field to Phase 2 — a quoted string the model writes once — then requires Phase 4 to open the diverger's brief with that quoted string; the quote is checkable against the Phase 2 block
- **V-02 R3 vs V-05 R2**: Replaces the advisory "if" in Phase 5 with a two-column anti-pattern table: policy form shown and labeled FORBIDDEN, persona form shown and labeled REQUIRED — gives the model a concrete negative example to avoid
- **V-03 R3 vs V-05 R2**: Diverger's character brief changes from free-form (with "foundation" advisory) to mandatory two-part: SEED must be verbatim from Phase 2; EXPAND must derive the brief from SEED — the structure itself enforces the linkage

---

## V-01 R3 — Role Sequence: Brief-Anchor Quotation

**Axis**: Role sequence — Phase 2 divergence commitment produces a `Brief anchor:` output field that Phase 4 must quote verbatim at the start of the diverger's character brief
**Hypothesis**: The Phase 2 sketch is instructional in V-05 R2 ("this sketch will become the core of..."). Making it an output field — a quoted string the model explicitly produces — creates a reference that Phase 4 can and must cite. Verbatim quotation in Phase 4 makes the C-14 causal chain output-checkable, not just intent-checkable.

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
Brief anchor: "[Copy the Experiential sketch sentence here, verbatim, inside quotes. This exact text must appear at the opening of this referee's character brief in Phase 4.]"
```

The Brief anchor field is a structural output, not a note. The character brief in Phase 4 must begin with this sentence. If Phase 4's character brief for the diverger does not open with the Brief anchor verbatim, that is a C-14 failure.

This commitment is locked before Phase 3. At least two distinct recommendation levels must appear across the three reports. If all three converge, that is a simulation failure — explain what overrode the commitment.

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

The character brief is required for all three referees. It answers: who is this person right now, and what recent reviewing experience makes their concerns land in this specific register? If two briefs could be swapped without changing any concerns in the reports below them, they are not distinct enough — rewrite.

**For the diverger specifically**: the character brief must open with the Brief anchor verbatim (copy it from Phase 2, inside quotes), then expand from it. The brief is built from the anchor, not written alongside it.

For each referee, this three-part structure is required:

**Referee [N] — [archetype] — Character Brief**
[For the diverger: begin with the Phase 2 Brief anchor in quotes, then expand in 2-3 additional sentences explaining why that reviewing history makes divergence from the other two referees structurally likely for this paper. For non-divergers: 2-3 sentences of concrete recent reviewing history that anchors their concerns in a specific register.]

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

Divergence check: [Did the locked diverger diverge as predicted? If prediction held, confirm. If divergence was in a different direction than predicted, explain why.]

P1 blockers (reject conditions):
  Issues: I-[NN], I-[NN] — what would cause outright rejection

P2 conditions (major revision requirements):
  Issues: I-[NN], I-[NN] — raised by 2+ referees; consensus issues are hardest to dismiss

Strongest referee: Referee [N] — their objections carry most weight because [cite a specific fact from this referee's character brief — their reviewing history, their stated priors, their recent experience — not abstract journal policy]
```

The "because" clause for Strongest referee must derive from the character brief. A clause that cites only journal policy ("PNAS editors desk-reject on power analysis grounds") without anchoring it in this referee's history does not satisfy C-15.

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

## V-02 R3 — Lifecycle Emphasis: Forbidden/Required Rationale Template

**Axis**: Lifecycle emphasis — Phase 5 "Strongest referee" rationale field uses an explicit forbidden/required template showing the policy form (labeled DO NOT USE) and the persona form (labeled REQUIRED)
**Hypothesis**: V-05 R2's "if the character brief illuminates why" makes brief-grounded rationale opt-in. Abstract policy language is generated more fluently and will dominate when the "if" condition is not consciously triggered. Showing the negative example — the policy form, labeled forbidden — eliminates ambiguity about which form is acceptable and makes C-15 checkable against a concrete anti-pattern.

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

This commitment is locked before Phase 3. At least two distinct recommendation levels must appear across the three reports. If all three converge, that is a simulation failure.

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

The character brief is not optional and not decorative. It answers: who is this person right now, and what recent reviewing experience makes their concerns land in this specific register? If two briefs could be swapped without changing any concerns in the reports below them, they are not distinct enough — rewrite. For the Phase 2 diverger, the brief must explain why they will diverge — make the Phase 2 experiential sketch the foundation of this paragraph.

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

Divergence check: [Did the locked diverger diverge as predicted? If prediction held, confirm. If divergence was in a different direction than predicted, explain why.]

P1 blockers (reject conditions):
  Issues: I-[NN], I-[NN] — what would cause outright rejection

P2 conditions (major revision requirements):
  Issues: I-[NN], I-[NN] — raised by 2+ referees; consensus issues are hardest to dismiss

Strongest referee: Referee [N] — their objections carry most weight because [REQUIRED: cite this referee's reviewing history from their character brief — e.g., "this reviewer's recent experience handling three retraction requests for threshold-adjacent p-values makes their statistical objections structurally weighted here"]
```

**Rationale form for Strongest referee:**

DO NOT USE (policy form — fails C-15):
> "Referee 2's objections carry most weight because PNAS editors routinely desk-reject on power analysis grounds."

REQUIRED (persona form — passes C-15):
> "Referee 2's objections carry most weight because, as their character brief notes, they recently reviewed [specific experience from brief] — which means their concern about [specific issue] is not a generic statistical preference but a pattern they have seen fail in exactly this configuration."

The persona form cites the character brief. The policy form cites the journal. Only the persona form is acceptable. A rationale that could have been written without the character briefs existing does not satisfy C-15.

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

## V-03 R3 — Phrasing Register: SEED/EXPAND Character Brief Format

**Axis**: Phrasing register — diverger's character brief in Phase 4 follows a mandatory SEED/EXPAND two-part format; SEED quotes the Phase 2 experiential sketch verbatim; EXPAND derives the full brief from SEED
**Hypothesis**: The advisory "make the Phase 2 sketch the foundation" in V-05 R2 can be satisfied by writing both independently and claiming one is foundational. Making the SEED sentence a required structural label — and requiring that EXPAND builds explicitly from SEED — creates an output marker that makes C-14 pass/fail checkable from the artifact text alone, without needing to interpret intent.

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

This commitment is locked before Phase 3. At least two distinct recommendation levels must appear across the three reports. If all three converge, that is a simulation failure.

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

The character brief is required for all three referees. Briefs must pass the swap test: if two briefs could be exchanged without changing any concerns in the reports below them, they are not distinct enough — rewrite.

**Character brief formats:**

For non-diverger referees:
**Referee [N] — [archetype] — Character Brief**
[2-3 sentences of concrete recent reviewing history that anchors this archetype's concerns in a specific register — not "skeptical of methodology" but an experience that explains why they raise the specific concerns they will raise.]

For the diverger specifically, the brief must use this two-part format:

**Referee [N] — [archetype] — Character Brief**
SEED: [Copy the Phase 2 Experiential sketch verbatim here]
EXPAND: [2-3 sentences that build directly from SEED — explaining how that specific reviewing history translates into the divergence direction committed in Phase 2. EXPAND must derive from SEED; it must not introduce a new premise independent of SEED. If EXPAND could stand alone without SEED, the linkage has failed.]

The SEED/EXPAND format is a structural requirement for the diverger's brief only. Non-divergers use the free-form format above. The purpose of SEED is to make C-14 checkable: if the SEED sentence does not match the Phase 2 Experiential sketch, the linkage has failed.

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

Divergence check: [Did the locked diverger diverge as predicted? If prediction held, confirm. If divergence was in a different direction than predicted, explain why.]

P1 blockers (reject conditions):
  Issues: I-[NN], I-[NN] — what would cause outright rejection

P2 conditions (major revision requirements):
  Issues: I-[NN], I-[NN] — raised by 2+ referees; consensus issues are hardest to dismiss

Strongest referee: Referee [N] — their objections carry most weight because [cite this referee's reviewing history from their character brief — the reason must derive from who this reviewer is, not from what the journal's editors generically prefer]
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

---

## V-04 R3 — Combined: Brief-Anchor Quotation + Forbidden/Required Template (C-14 + C-15)

**Axes**: Role sequence + lifecycle emphasis
**Hypothesis**: V-01 R3's Brief anchor field (C-14) and V-02 R3's forbidden/required template (C-15) target different phases — Phase 2/4 and Phase 5 respectively — and create no structural tension. Together they close both R3 gaps without changing anything about C-01 through C-13. Predicts 122+/125; the 3-point gap would be if the forbidden/required template is followed but the resulting persona form is thin (draws on a weak brief rather than a rich one — C-15 passes structurally but not substantively).

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
Brief anchor: "[Copy the Experiential sketch sentence here, verbatim, inside quotes. This exact text must appear at the opening of this referee's character brief in Phase 4.]"
```

The Brief anchor is a structural output. Phase 4's character brief for the diverger must begin with this sentence. If it does not, that is a C-14 failure. This commitment is locked before Phase 3. At least two distinct recommendation levels must appear across the three reports. If all three converge, that is a simulation failure.

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

The character brief is required for all three referees. If two briefs could be swapped without changing any concerns in the reports below them, they are not distinct enough — rewrite.

**For the diverger specifically**: the character brief must open with the Brief anchor verbatim (copy it from Phase 2, inside quotes), then expand from it in 2-3 sentences. The brief is built from the anchor, not written independently. The anchor must be visible at the start of the brief as a quoted sentence.

For each referee, this three-part structure is required:

**Referee [N] — [archetype] — Character Brief**
[For the diverger: begin with the Phase 2 Brief anchor in quotes, then 2-3 sentences of expansion explaining why that reviewing history makes divergence structurally likely for this paper. For non-divergers: 2-3 sentences of concrete recent reviewing history anchoring their concerns in a specific register.]

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

Divergence check: [Did the locked diverger diverge as predicted? If prediction held, confirm. If divergence was in a different direction than predicted, explain why.]

P1 blockers (reject conditions):
  Issues: I-[NN], I-[NN] — what would cause outright rejection

P2 conditions (major revision requirements):
  Issues: I-[NN], I-[NN] — raised by 2+ referees; consensus issues are hardest to dismiss

Strongest referee: Referee [N] — their objections carry most weight because [REQUIRED: cite this referee's reviewing history from their character brief]
```

**Rationale form for Strongest referee:**

DO NOT USE (policy form — fails C-15):
> "Referee 2's objections carry most weight because PNAS editors routinely desk-reject on power analysis grounds."

REQUIRED (persona form — passes C-15):
> "Referee 2's objections carry most weight because, as their character brief notes, [specific reviewing experience from brief] — their concern about [specific issue] is not a generic preference but a pattern they have seen fail in this configuration."

The persona form cites the character brief. A rationale that could have been written without character briefs existing does not satisfy C-15.

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

## V-05 R3 — Combined: All Three (C-14 + C-15 + SEED/EXPAND Format)

**Axes**: Role sequence + lifecycle emphasis + phrasing register
**Hypothesis**: The three mechanisms form a causal chain through the artifact: Phase 2 writes the experiential sketch once; Phase 4 opens the diverger's brief with SEED (quoting the sketch verbatim) then EXPAND (deriving the brief from SEED); Phase 5 cites EXPAND content for the strongest-referee rationale (persona form, not policy form). Each mechanism makes the previous one's output checkable in the next phase. The full chain — sketch → SEED → EXPAND → rationale — makes C-14 and C-15 structurally impossible to accidentally satisfy or accidentally fail. Predicts 125/125.

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
