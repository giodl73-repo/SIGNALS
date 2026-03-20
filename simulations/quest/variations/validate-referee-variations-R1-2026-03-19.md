Here are the 5 variations written to `simulations/quest/variations/validate-referee-variations-R1-2026-03-19.md`:

---

## Summary

**Single-axis:**

**V-01 — Role sequence: Verdict-first**
Inserts a *Predictive Verdict* phase before the three reports. The model commits to a predicted outcome (likely decision, P1 blocker, which referee will diverge), then each report must confirm or diverge from that prior. Hypothesis: early commitment forces differentiated referee recommendations (C-07) and produces editorial-grounded rationale (C-09) because the model has to justify when reality diverges from prediction.

**V-02 — Output format: Scored dimension tables**
Replaces prose report preambles with a per-dimension 1-10 scorecard across all three referees before any prose is written. Scores then constrain prose — a dimension scored below 4 must appear as a Major Concern; above 8 cannot. Hypothesis: numeric constraints make differentiation (C-07) and contrarian positions (C-10) structurally visible rather than hidden in prose.

**V-03 — Lifecycle emphasis: Amend-heavy**
Compresses phases 1-2 into a single setup block (including a compact journal archetype table), then expands phase 5 into a full Issue Registry (quoted concerns, severity, ID) plus a per-fix completion criterion and a revision letter seed. Hypothesis: explicit issue IDs and verifiable "done when" criteria make the fix plan actionable (C-08) rather than advisory.

**Combined:**

**V-04 — Role sequence + phrasing register (coaching)**
Verdict-first structure with a conversational coaching register throughout — "think out loud about what this paper will encounter," "at least one referee should sound like someone who reviewed three failed replications last month." Hypothesis: committing early + natural language framing reduces hedging in major concerns (C-04) and makes the strongest-referee rationale feel grounded rather than templated (C-09).

**V-05 — Output format (tables) + inertia framing (submission gate)**
Adds an explicit pre-referee Submission Gate table ("the default answer is: not yet") and a post-verdict Readiness Score with thresholds (8-10: submit; 4-5: hold and fix). Hypothesis: making the inertia competitor structurally present at both ends of the skill reduces false-positive "this paper is ready" outputs and frames the fix plan as a genuine submit/hold decision (C-08, C-09).
the fields it claims to?)
- **NeurIPS / ICML / AI venues**: Referee 1 = benchmark enforcer (SOTA comparisons, ablations); Referee 2 = theory skeptic (where's the convergence proof?); Referee 3 = reproducibility checker (code, seeds, compute budget)

---

## PHASE 3 -- PREDICTIVE VERDICT (before reading individual reports)

Before writing any individual referee report, commit to a predicted outcome:

```
PREDICTIVE VERDICT
Journal: [name]
Predicted decision: ACCEPT / MAJOR REVISION / MINOR REVISION / REJECT
Predicted confidence: HIGH / MEDIUM / LOW

Predicted P1 blocker (most likely reject trigger):
  [Single most likely fatal flaw given this journal's known rejection patterns]

Predicted P2 consensus (most likely shared concern across all three referees):
  [The issue that any referee from this journal profile will raise]

Predicted outlier: which referee is most likely to diverge from the other two?
  [Referee archetype + direction of divergence — more positive or more hostile]
```

---

## PHASE 4 -- THREE REFEREE REPORTS

Now write each referee report. Each referee should confirm or diverge from the predictive verdict above — at least one must diverge in recommendation or emphasis.

For each referee, produce a report in the journal's actual format:

```
REFEREE [N] — [archetype]
Recommendation: Accept / Major Revision / Minor Revision / Reject
Diverges from predictive verdict: YES / NO — [if yes, explain why]

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

## PHASE 5 -- FINAL VERDICT

Update the predictive verdict with what the reports actually showed:

```
Journal: [name]
Likely decision: ACCEPT / MAJOR REVISION / MINOR REVISION / REJECT
Confidence: HIGH / MEDIUM (depends on referee 2's weight at this journal)

Prediction accuracy: [Did the predictive verdict hold? What changed?]

P1 blockers (reject conditions):
  [What would cause outright rejection — must fix before resubmission]

P2 conditions (major revision requirements):
  [What all 3 referees flagged — consensus issues are hardest to dismiss]

Strongest referee: Referee [N] — their objections carry most weight because [reason grounded in this journal's editorial process]
```

---

## PHASE 6 -- AMEND

Three targeted pre-submission fixes ordered by blocking severity:
1. [Fix that addresses the most likely reject condition]
2. [Fix that addresses the consensus P2 across referees]
3. [Fix that addresses the journal's specific formatting/evidence standard]

Write artifact to: signals/validate/referee/{{topic}}-referee-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: validate-referee, topic: {{topic}}, date: {{date}}, journal: [journal name], verdict: likely-accept|major-revision|reject

---

## V-02 — Output Format: Scored Dimension Tables

**Axis**: Output format
**Hypothesis**: Replacing prose report preambles with per-dimension numeric scores (1-10) forces explicit differentiation between referees on each axis, making C-07 (differentiated recommendations) and C-10 (contrarian position) structurally visible rather than emergent from prose reading.

---

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

## PHASE 3 -- SCORECARD

Before individual reports, produce a comparative scorecard across all three referees.

Score each dimension 1-10 (1 = fatal flaw, 10 = no concern). Use journal-specific dimensions:

**For PNAS/Nature/Science:**

| Dimension | R1 (sympathetic) | R2 (statistician) | R3 (breadth) | Notes |
|-----------|-----------------|-------------------|--------------|-------|
| Effect size reporting | [1-10] | [1-10] | [1-10] | |
| Statistical power | [1-10] | [1-10] | [1-10] | |
| Sample size / N | [1-10] | [1-10] | [1-10] | |
| Claim scope (is it general?) | [1-10] | [1-10] | [1-10] | |
| Novelty for broad audience | [1-10] | [1-10] | [1-10] | |
| **Overall** | [1-10] | [1-10] | [1-10] | |

**For NeurIPS/ICML/AI venues:**

| Dimension | R1 (benchmark) | R2 (theory) | R3 (repro) | Notes |
|-----------|----------------|-------------|------------|-------|
| SOTA comparisons | [1-10] | [1-10] | [1-10] | |
| Ablation studies | [1-10] | [1-10] | [1-10] | |
| Theoretical grounding | [1-10] | [1-10] | [1-10] | |
| Reproducibility (code/seeds) | [1-10] | [1-10] | [1-10] | |
| Novelty of contribution | [1-10] | [1-10] | [1-10] | |
| **Overall** | [1-10] | [1-10] | [1-10] | |

(Use the appropriate table for the target journal. For other journal profiles, adapt dimensions accordingly.)

Recommendation summary row:

| | R1 | R2 | R3 |
|--|----|----|-----|
| Recommendation | Accept/Minor/Major/Reject | Accept/Minor/Major/Reject | Accept/Minor/Major/Reject |

---

## PHASE 4 -- THREE REFEREE REPORTS

For each referee, produce a full report. The scores in Phase 3 constrain the prose — a dimension scored below 4 must generate a Major Concern; a dimension scored above 8 must not generate a Major Concern.

```
REFEREE [N] — [archetype]
Recommendation: Accept / Major Revision / Minor Revision / Reject
Overall score: [N]/10

SUMMARY:
[2-3 sentences: what the paper does and the referee's overall reaction]

MAJOR CONCERNS: (dimensions scored 1-5)
1. [Specific, citable concern — name the gap, the missing analysis, the logical flaw]
2. [...]

MINOR CONCERNS: (dimensions scored 6-7)
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

## PHASE 5 -- VERDICT

```
Journal: [name]
Likely decision: ACCEPT / MAJOR REVISION / MINOR REVISION / REJECT
Confidence: HIGH / MEDIUM (depends on referee 2's weight at this journal)

P1 blockers (reject conditions):
  [Dimensions scored 1-3 by any referee — must fix before resubmission]

P2 conditions (major revision requirements):
  [Dimensions scored 4-5 by two or more referees — consensus issues]

Strongest referee: Referee [N] — their objections carry most weight because [reason grounded in this journal's editorial process]
```

---

## PHASE 6 -- AMEND

Three targeted pre-submission fixes ordered by blocking severity:
1. [Fix for lowest-scored dimension across all referees — P1 blocker]
2. [Fix for dimension with worst consensus score — P2 condition]
3. [Fix for the journal's specific formatting or evidence standard]

Write artifact to: signals/validate/referee/{{topic}}-referee-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: validate-referee, topic: {{topic}}, date: {{date}}, journal: [journal name], verdict: likely-accept|major-revision|reject

---

## V-03 — Lifecycle Emphasis: Amend-Heavy

**Axis**: Lifecycle emphasis
**Hypothesis**: Compressing phases 1-2 into a single setup block and expanding phase 5 into a structured repair plan with issue-tracking IDs produces more actionable output (C-08) — the amend section becomes a revision checklist an author can hand to a co-author, not a summary paragraph.

---

You are running /validate-referee for: {{topic}}

Simulate journal-specific hostile peer review. validate-design uses generic disciplines — this skill knows the difference between a PNAS reviewer demanding effect sizes and a JCS reviewer wanting phenomenological grounding.

---

## SETUP (Phases 1-2 combined)

Glob: signals/**/{topic}-*
Read the paper or draft. Extract: central claim, method, key results, target journal, submission deadline if present.

If no journal specified: infer from content style and confirm before proceeding.

Assign 3 referees using the journal archetype table:

| Journal family | R1 | R2 | R3 |
|----------------|----|----|-----|
| PNAS / Nature / Science | sympathetic-rigorous | hostile statistician | breadth skeptic |
| Psychological Science / JEP | pre-registration enforcer | effect-size pragmatist | ecological validity critic |
| JCS / Phenomenology | sympathetic phenomenologist | hard-nosed analytic philosopher | empirical skeptic |
| Cognitive Science / Topics | computational modeler | experimental psychologist | interdisciplinary enforcer |
| NeurIPS / ICML / AI | benchmark enforcer | theory skeptic | reproducibility checker |

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

Strongest referee: Referee [N] — their objections carry most weight because [reason grounded in this journal's editorial process]
```

---

## PHASE 5 -- REPAIR PLAN (expanded)

Produce a structured repair plan the author can execute as a checklist.

### Issue Registry

For every Major Concern raised across all three reports, assign an issue ID:

| ID | Source | Concern (quoted) | Severity | Status |
|----|--------|-----------------|----------|--------|
| I-01 | R[N] | "[exact quoted concern]" | P1 / P2 / P3 | OPEN |
| I-02 | R[N] | "[exact quoted concern]" | P1 / P2 / P3 | OPEN |
| ... | | | | |

Severity levels:
- **P1**: Reject condition — unfixed, the paper gets rejected
- **P2**: Consensus concern — two or more referees raised this; editors weight heavily
- **P3**: Single-referee concern — should fix but not fatal

### Ordered Fix Plan

Fixes ordered by blocking severity (P1 first):

**Fix 1 — [P1 blocker title]**
Addresses: I-[NN], I-[NN]
What to do: [Specific action — add Table X, run analysis Y, rewrite paragraph Z]
Done when: [Verifiable completion criterion — "Table 2 now reports Cohen's d with 95% CI"]
Estimated scope: [sentence / paragraph / section / new analysis]

**Fix 2 — [P2 consensus title]**
Addresses: I-[NN], I-[NN]
What to do: [Specific action]
Done when: [Verifiable completion criterion]
Estimated scope: [scope]

**Fix 3 — [Journal standard / P3 title]**
Addresses: I-[NN]
What to do: [Specific action addressing journal formatting or evidence standard]
Done when: [Verifiable completion criterion]
Estimated scope: [scope]

### Revision Letter Seed

One paragraph the author can use as the opening of their revision letter:
> "We thank the referees for their careful reading. We have addressed all major concerns. The primary revision addresses [P1 blocker] by [action]. We additionally [P2 fix] in response to the consensus concern raised by Referees [N] and [N]. Minor concerns have been addressed throughout."

Write artifact to: signals/validate/referee/{{topic}}-referee-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: validate-referee, topic: {{topic}}, date: {{date}}, journal: [journal name], verdict: likely-accept|major-revision|reject

---

## V-04 — Combined: Role Sequence (verdict-first) + Phrasing Register (conversational coaching)

**Axes**: Role sequence + phrasing register
**Hypothesis**: Leading with a predicted outcome AND using a coaching register ("here's what the reviewers will say") reduces hedging in major concerns (C-04) because the model commits to a position early and then defends it — rather than discovering concerns piecemeal. The conversational register also increases the naturalness of the "strongest referee" rationale (C-09).

---

You are running /validate-referee for: {{topic}}

Your job: simulate what hostile peer review will look like before the paper goes out. This is not a generic review — you know how PNAS referees think versus JCS referees versus NeurIPS area chairs. Use that knowledge.

---

## Step 1: Read the paper

Glob: signals/**/{topic}-*
Read the artifact. You need: what is the central claim, what method does it use, what are the main results, and where is this being submitted.

If no journal is specified, make your best inference from the writing style and ask for confirmation. Don't proceed without knowing the journal.

---

## Step 2: Assign your referee panel

Pick three referees based on the journal. These archetypes are what real editorial boards actually look like:

- **PNAS / Nature / Science** — sympathetic-rigorous + hostile statistician + breadth skeptic
- **Psychological Science / JEP** — pre-registration enforcer + effect-size pragmatist + ecological validity critic
- **JCS / Phenomenology** — sympathetic phenomenologist + hard-nosed analytic philosopher + empirical skeptic
- **Cognitive Science / Topics** — computational modeler + experimental psychologist + interdisciplinary enforcer
- **NeurIPS / ICML / AI** — benchmark enforcer + theory skeptic + reproducibility checker

Name each referee and their archetype. This is who will be reading the paper.

---

## Step 3: Make a prediction before you read the reports

Before anyone writes a word, commit to where this is going:

What is the most likely outcome, and why? What's the one thing that could kill this paper at this journal? Which of your three referees is most likely to be the odd one out — more positive or more hostile than the other two, and why?

Write this as a short paragraph, not a template. Think out loud about what this particular paper submitted to this particular journal is likely to encounter.

---

## Step 4: Write the three referee reports

Now let each referee speak. Each one should feel like a different person with a different set of priors — not three variations of the same review.

For each referee:

```
REFEREE [N] — [archetype]
Recommendation: Accept / Major Revision / Minor Revision / Reject

SUMMARY:
[2-3 sentences: what this paper does and your overall reaction]

MAJOR CONCERNS:
1. [Specific, citable — not "needs more rigor" but "Effect size d is not reported in Table 2"]
2. [...]
3. [...]

MINOR CONCERNS:
1. [...]
2. [...]

SPECIFIC COMMENTS:
Line X: [exact issue]
```

Be ruthless with journal-specific standards. If this is going to PNAS, Referee 2 should sound like someone who reviewed the power analysis on three failed replications last month. If this is going to JCS, Referee 1 should care about phenomenological grounding in a way that Referee 2 finds irritating.

At least one referee should take a position that the other two would push back on.

---

## Step 5: The verdict

Now that you've seen what the referees actually said — did your prediction hold?

```
Journal: [name]
Likely decision: ACCEPT / MAJOR REVISION / MINOR REVISION / REJECT
Confidence: HIGH / MEDIUM

Prediction check: [One sentence — what held, what changed]

P1 blockers (reject conditions):
  [What gets this paper rejected outright — must fix before resubmitting]

P2 conditions (what all three flagged):
  [The consensus issue — editors know when all referees agree]

Strongest referee: Referee [N] — [why their objections carry the most weight given how this journal's editorial process actually works]
```

---

## Step 6: Three fixes

What should the author fix before resubmitting? Ordered by urgency:

1. [The thing that addresses the reject condition]
2. [The thing that addresses the consensus issue]
3. [The journal-specific formatting or evidence standard]

Write artifact to: signals/validate/referee/{{topic}}-referee-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: validate-referee, topic: {{topic}}, date: {{date}}, journal: [journal name], verdict: likely-accept|major-revision|reject

---

## V-05 — Combined: Output Format (scored tables) + Inertia Framing (explicit submission gate)

**Axes**: Output format + inertia framing
**Hypothesis**: Adding an explicit "submit or hold?" gate at the start and a submission-readiness score at the end makes the inertia competitor (don't submit yet, wait for more evidence) structurally present throughout the skill — which should reduce false-positive "this paper is ready" outputs and make the fix plan feel like an actual decision, not a formality.

---

You are running /validate-referee for: {{topic}}

Simulate journal-specific hostile peer review. validate-design uses generic disciplines — this skill knows the difference between a PNAS reviewer demanding effect sizes and a JCS reviewer wanting phenomenological grounding.

The default answer for any paper is: **not yet**. Referees reject or request major revisions on most first submissions. The question is not whether this paper is good — it is whether it is ready for this journal right now. Most papers are not.

---

## PHASE 1 -- SIGNAL ACQUISITION

Glob: signals/**/{topic}-*
Read the paper or draft artifact. Extract: the central claim, the method, the key results, the target journal.

If no journal specified: infer from content style and ask for confirmation before proceeding.

---

## PHASE 2 -- SUBMISSION GATE

Before assigning referees, run a quick gate check. The inertia position is always: wait, gather more evidence, fix before submitting. Answer these questions first:

| Gate question | Answer | Gate pass? |
|---------------|--------|------------|
| Does the paper report effect sizes or equivalent? | [yes/no/partial] | [pass/warn/fail] |
| Is the central claim falsifiable as stated? | [yes/no/partial] | [pass/warn/fail] |
| Is the method matched to the journal's expected rigor? | [yes/no/partial] | [pass/warn/fail] |
| Are all major prior works cited? | [yes/no/partial] | [pass/warn/fail] |
| Does the paper match the journal's scope? | [yes/no/partial] | [pass/warn/fail] |

**Gate result**: CLEAR (proceed) / WARN (flag to author before proceeding) / HOLD (author should address before submitting)

Even if gate result is HOLD, continue with the full simulation — the author needs to see what the referees will say.

---

## PHASE 3 -- REFEREE ASSIGNMENT

Based on the target journal, assign 3 referees with journal-specific archetypes:

**Journal profiles:**
- **PNAS / Nature / Science**: Referee 1 = sympathetic-rigorous (wants clean effect sizes, p < 0.05, large N); Referee 2 = hostile statistician (power analysis, multiple comparisons, replication); Referee 3 = breadth skeptic (is this general enough for a broad journal?)
- **Psychological Science / JEP**: Referee 1 = pre-registration enforcer; Referee 2 = effect-size pragmatist (d > 0.4 or why bother?); Referee 3 = ecological validity critic
- **Journal of Consciousness Studies / Phenomenology**: Referee 1 = sympathetic phenomenologist (internal consistency over empirical proof); Referee 2 = hard-nosed analytic philosopher (conceptual precision); Referee 3 = empirical skeptic (where's the data?)
- **Cognitive Science / Topics in Cognitive Science**: Referee 1 = computational modeler (is there a formal model?); Referee 2 = experimental psychologist (ecological validity, individual differences); Referee 3 = interdisciplinary enforcer (does it actually bridge the fields it claims to?)
- **NeurIPS / ICML / AI venues**: Referee 1 = benchmark enforcer (SOTA comparisons, ablations); Referee 2 = theory skeptic (where's the convergence proof?); Referee 3 = reproducibility checker (code, seeds, compute budget)

---

## PHASE 4 -- THREE REFEREE REPORTS

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

## PHASE 5 -- VERDICT AND READINESS SCORE

```
Journal: [name]
Likely decision: ACCEPT / MAJOR REVISION / MINOR REVISION / REJECT
Confidence: HIGH / MEDIUM (depends on referee 2's weight at this journal)

P1 blockers (reject conditions):
  [What would cause outright rejection — must fix before resubmission]

P2 conditions (major revision requirements):
  [What all 3 referees flagged — consensus issues are hardest to dismiss]

Strongest referee: Referee [N] — their objections carry most weight because [reason grounded in this journal's editorial process]
```

**Submission readiness score:**

| Dimension | Score (1-10) | Why |
|-----------|-------------|-----|
| P1 blockers resolved | [1-10] | [one line] |
| P2 consensus gaps | [1-10] | [one line] |
| Journal standard fit | [1-10] | [one line] |
| Scope match | [1-10] | [one line] |
| **Overall readiness** | [average] | |

Readiness thresholds:
- 8-10: Submit now. Referees will still push back but nothing fatal.
- 6-7: Submit with fixes from Phase 6. Don't submit as-is.
- 4-5: Hold. Fix P1 blockers first, then re-run this skill.
- 1-3: Major revision needed before submission is appropriate.

---

## PHASE 6 -- AMEND

Three targeted pre-submission fixes ordered by blocking severity:
1. [Fix that addresses the most likely reject condition — raises P1 score most]
2. [Fix that addresses the consensus P2 across referees — raises consensus score most]
3. [Fix that addresses the journal's specific formatting/evidence standard — raises journal fit most]

**Rerun trigger**: If overall readiness score is below 6, recommend the author fix items 1-2 and rerun /validate-referee before submitting.

Write artifact to: signals/validate/referee/{{topic}}-referee-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: validate-referee, topic: {{topic}}, date: {{date}}, journal: [journal name], verdict: likely-accept|major-revision|reject
