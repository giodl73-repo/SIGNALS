---
skill: quest-variate
skill_target: campaign-evidence
round: 3
date: 2026-03-16
rubric: simulations/quest/rubrics/campaign-evidence-rubric-v3-2026-03-16.md
---

# Variations — campaign-evidence / Round 3

Five complete, runnable skill body variations. Single-axis first (V-01, V-02, V-03),
then combined (V-04, V-05).

R3 rubric adds C-13 (named rules declared at preamble and invoked by name at point of
use — not just inline prose) and C-14 (hypothesis reordering rationale stated when
C-10 applies). V-05 from R2 partially addressed both. R3 explores three new axes to
push them further and introduces inertia framing, the one axis from the menu not yet
tested in R2.

---

## V-01 — Axis: Named Rule Invocation Discipline (C-13 maximum)

**Hypothesis**: Embedding "[RULE_NAME invoked]" as a required template element at each
stage — not only at synthesis — forces C-13 compliance at every application point. A
model following the template must invoke each rule by name at the step where it applies;
there is no option to declare rules at preamble and then ignore them until the final
output. Per-stage invocation also produces intermediate evidence that the rule was
applied, which is auditable by a scorer independently of synthesis quality.

```
Run the full evidence campaign for: {{topic}}

Produce a complete evidence brief. The rules below govern this campaign. Each rule is
declared here and then invoked by name at every stage where it applies.

---

CALIBRATION RULE
Confidence ratings across all findings must vary. At least two distinct levels
(High / Medium / Low) must appear. Uniform confidence is a calibration failure.

FALSIFICATION RULE
Every hypothesis carries an explicit status (Supported / Refuted / Indeterminate)
with a named evidence basis. A hypothesis without an outcome is a draft.

ATTRIBUTION RULE
Every material claim in synthesis names its source stage. Minimum form:
"[claim] — Stage [N]." Claims without stage attribution are not acceptable.

EVIDENCE RULE
Stage 2 (websearch) requires URLs — no training-data claims. Stage 3 (intelligence)
requires exact file paths.

---

Stage 1 — prove-hypothesis

State the investigation frame before gathering evidence.

Claim: [one sentence — what you believe]
Falsification condition: [what would disprove this — specific enough that evidence
  could satisfy it]
Confidence prior: [High / Medium / Low] — [one-clause reason]
Experiments: [2-3 tests that would test the claim]

[FALSIFICATION RULE invoked: falsification condition must be non-trivial — a condition
  that no possible evidence could disprove is not falsifiable]

Write to: simulations/prove/investigations/{{topic}}-hypothesis-{{date}}.md

---

Stage 2 — prove-websearch

Search the public web for evidence relevant to {{topic}}.

For each source:
- URL (required)
- Direct quote (verbatim)
- Strength: Weak / Moderate / Strong
- Bearing: Supports / Refutes / Neutral

[EVIDENCE RULE invoked: every source requires a URL — claims without URLs are excluded
  from synthesis]
[ATTRIBUTION RULE invoked: label each source with URL now — these become Stage 2
  citations in synthesis]

Write to: simulations/prove/investigations/{{topic}}-websearch-{{date}}.md

---

Stage 3 — prove-intelligence

Search internal sources (repo files, design docs, scenarios, prior signals).

For each source:
- File path (exact)
- Relevant excerpt
- Strength: Weak / Moderate / Strong
- Bearing: Supports / Refutes / Neutral

[EVIDENCE RULE invoked: exact file paths required — "the codebase" without a path
  is rejected]
[ATTRIBUTION RULE invoked: findings here become Stage 3 citations in synthesis]

Write to: simulations/prove/investigations/{{topic}}-intelligence-{{date}}.md

---

Stage 4 — prove-analysis

Analyze patterns across Stages 1-3 evidence.

For each pattern:
- Source: Stage 2 row / Stage 3 file
- Pattern observed
- Causal or correlational? State explicitly — "Causal" requires identified mechanism.
- Confidence: High / Medium / Low — [one-clause reason]

[CALIBRATION RULE invoked: per-pattern confidence ratings established here — variation
  should appear across patterns; if all patterns are the same level, revisit before
  synthesis]

Write to: simulations/prove/investigations/{{topic}}-analysis-{{date}}.md

---

Stage 5 — prove-synthesize

[CALIBRATION RULE invoked: before writing, verify at least two distinct confidence
  levels appear across Stages 1-4. Revise now if uniform.]
[FALSIFICATION RULE invoked: synthesis must carry Supported / Refuted / Indeterminate
  with the specific finding that determined it.]
[ATTRIBUTION RULE invoked: every finding in the brief names its source stage.]

Write the evidence brief:

**Evidence Brief: {{topic}}**
**Investigation date**: {{date}}

**Hypothesis** (Stage 1): [claim]
**Falsification status** [FALSIFICATION RULE]: [Supported / Refuted / Indeterminate]
**Basis**: [Stage N — specific finding or excerpt that determined this outcome]

**Key findings** [ATTRIBUTION RULE — every finding names its source stage]:
1. [finding] — Stage [N] — Confidence: [High / Medium / Low] — [one-clause rationale]
2. [finding] — Stage [N] — Confidence: [High / Medium / Low] — [one-clause rationale]
3. [finding] — Stage [N] — Confidence: [High / Medium / Low] — [one-clause rationale]
4. [finding] — Stage [N] — Confidence: [High / Medium / Low] — [one-clause rationale]
5. [finding] — Stage [N] — Confidence: [High / Medium / Low] — [one-clause rationale]

[CALIBRATION RULE invoked: confirm at least two distinct confidence levels appear above]

**Consensus** (Stage 2 vs Stage 3): [where web and internal sources agreed]
**Divergence** (Stage 2 vs Stage 3): [where they disagreed — and why it matters]

**Counter-evidence**: [the finding most challenging to the hypothesis, with stage cite]

**Open gaps**: [what the campaign did not resolve — enables follow-up to pick up cleanly]

**Decision readiness**: [one sentence — "Ready to proceed" or "Needs more investigation
on [specific named gap] before committing."]

Write to: simulations/prove/investigations/{{topic}}-synthesis-{{date}}.md
```

**Rubric targeting**: C-01 (five named stages), C-02 (per-finding confidence with
rationale), C-03 (FALSIFICATION RULE + status + basis), C-04 (titled, dated brief),
C-05 (ATTRIBUTION RULE per finding), C-06 (consensus/divergence), C-07 (CALIBRATION
RULE with anti-uniformity), C-08 (open gaps), C-09 (decision readiness), C-11
(CALIBRATION RULE as named guard), C-12 (one-sentence directive), C-13 (named rules
at preamble, invoked by name at EVERY application stage — not only synthesis).
**Misses**: C-10 (standard sequence — hypothesis before evidence), C-14 (no reorder,
so rationale is not applicable).
**Risk**: Per-stage invocations add length but may become boilerplate — a model
reciting "[RULE invoked]" without applying the rule. C-10 and C-14 are structurally
absent; scores cap at 12/14 criteria.

---

## V-02 — Axis: Hypothesis Reordering Rationale (C-14 at three structural positions)

**Hypothesis**: The R2 rubric codified a pattern observed in V-05: when reordering
stages, stating the principle that justifies the reorder makes the decision auditable.
V-05 R2 stated it once at Stage 3. Encoding the principle at three structural positions
— skill intro, Stage 3 header, and synthesis preamble — ensures C-14 passes regardless
of which part of the output a scorer reads, and makes the principle feel like a design
commitment rather than an incidental note. C-10 passes structurally via evidence-first
sequencing; C-14 passes redundantly via triple encoding.

```
Run the full evidence campaign for: {{topic}}

Produce a complete evidence brief. This campaign uses evidence-first sequencing:
web search and intelligence gathering complete before the hypothesis is declared.

SEQUENCING PRINCIPLE: A hypothesis anchored before evidence gathering is a bias,
not a hypothesis. Evidence gathered under a pre-committed framing is filtered
evidence. This principle governs the stage ordering below and is recorded in the
synthesis so readers can evaluate whether falsification decisions were grounded in
what was actually found.

---

CALIBRATION RULE: Confidence ratings must vary — at least two distinct levels across
findings. Uniform confidence is a calibration failure.

FALSIFICATION RULE: Every hypothesis carries Supported / Refuted / Indeterminate
with a named evidence basis.

ATTRIBUTION RULE: Every material claim in synthesis names its source stage.

---

Stage 1 — prove-websearch

Search the public web for evidence relevant to {{topic}}.

For each source: URL (required — no training-data claims), verbatim quote, strength
(Weak / Moderate / Strong), bearing (Supports / Refutes / Neutral).

Write to: simulations/prove/investigations/{{topic}}-websearch-{{date}}.md

---

Stage 2 — prove-intelligence

Search internal sources (repo files, design docs, scenarios, prior signals).

For each source: exact file path, relevant excerpt, strength, bearing.

Write to: simulations/prove/investigations/{{topic}}-intelligence-{{date}}.md

---

Stage 3 — prove-hypothesis [EVIDENCE-INFORMED DECLARATION]

SEQUENCING PRINCIPLE (applied here): This stage runs third. A hypothesis anchored
before evidence gathering is a bias, not a hypothesis. You have now seen what Stages
1 and 2 found. The claim below must reflect what the evidence supports you believing
— not a prior intuition.

Claim: [one sentence — what the evidence supports you believing]
Falsification condition: [what would disprove this — cite Stages 1-2 findings that
  shaped this choice]
Confidence: [High / Medium / Low] — [cite specific Stage 1-2 findings]
Experiments: [2-3 tests that would further test the claim]

Write to: simulations/prove/investigations/{{topic}}-hypothesis-{{date}}.md

---

Stage 4 — prove-analysis

Analyze patterns across Stages 1-3 evidence.

For each pattern: source, pattern observed, causal or correlational (mechanism
required for causal), confidence (High / Medium / Low — reason).

Write to: simulations/prove/investigations/{{topic}}-analysis-{{date}}.md

---

Stage 5 — prove-synthesize

Apply CALIBRATION RULE before writing: verify at least two distinct confidence levels
appear across all stages. Revise if uniform.

Write the evidence brief:

**Evidence Brief: {{topic}}**
**Investigation date**: {{date}}

SEQUENCING PRINCIPLE (recorded here): This brief's hypothesis was declared after the
evidence stages completed — Stages 1 and 2 ran before Stage 3. A hypothesis anchored
before evidence gathering is a bias, not a hypothesis. Falsification decisions below
are grounded in what Stages 1 and 2 actually found, not pre-anchored assumptions.

**Hypothesis** (declared post-evidence, Stage 3): [claim]
**Falsification status** [FALSIFICATION RULE]: [Supported / Refuted / Indeterminate]
**Basis**: [Stage N — specific finding that determined this outcome]

**Key findings** [ATTRIBUTION RULE — every finding names its source stage]:
1. [finding] — Stage [N] — Confidence: [High / Medium / Low] — [one-clause rationale]
2. [finding] — Stage [N] — Confidence: [High / Medium / Low] — [one-clause rationale]
3. [finding] — Stage [N] — Confidence: [High / Medium / Low] — [one-clause rationale]
4. [finding] — Stage [N] — Confidence: [High / Medium / Low] — [one-clause rationale]
5. [finding] — Stage [N] — Confidence: [High / Medium / Low] — [one-clause rationale]

[CALIBRATION RULE: confirm at least two distinct confidence levels appear above]

**Consensus** (Stage 1 vs Stage 2): [where web and internal sources agreed]
**Divergence** (Stage 1 vs Stage 2): [where they disagreed — and why it matters]

**Counter-evidence**: [the finding most challenging to the hypothesis, with stage cite]

**Open gaps**: [what the campaign did not resolve]

**Decision readiness**: [one sentence — ready to proceed or needs more investigation
on [specific named gap]]

Write to: simulations/prove/investigations/{{topic}}-synthesis-{{date}}.md
```

**Rubric targeting**: C-01 (five stages in evidence-first order), C-02 (per-finding
confidence with rationale), C-03 (FALSIFICATION RULE + status + basis), C-04 (titled,
dated, self-contained), C-05 (ATTRIBUTION RULE), C-06 (consensus/divergence), C-07
(CALIBRATION RULE anti-uniformity), C-08 (open gaps), C-09 (decision readiness),
C-10 (evidence-first: Stage 3 follows Stages 1-2), C-11 (CALIBRATION RULE named),
C-12 (one-sentence directive), C-13 (named rules at preamble, invoked by name in
synthesis headers), C-14 (SEQUENCING PRINCIPLE at three positions: intro, Stage 3
header, synthesis preamble).
**Risk**: C-13 relies on synthesis-level invocations only — intermediate stages invoke
the SEQUENCING PRINCIPLE but not CALIBRATION / FALSIFICATION / ATTRIBUTION by name.
A strict reading of C-13 could penalize variations where invocation occurs only once
at synthesis. The triple C-14 encoding makes it the strongest variation on that
criterion but adds prose overhead.

---

## V-03 — Axis: Inertia Framing (status-quo competitor)

**Hypothesis**: Asking the model to name the default belief before gathering evidence
— what a team would conclude without this campaign — adds a structural before/after
frame to the brief. Inertia framing upgrades C-04 (self-contained brief) because a
reader can evaluate not just what was found but what changed. It upgrades C-08 (open
gaps) because gaps become gaps relative to what the inertia position assumed. The
"Inertia verdict" section provides a uniquely legible decision signal: did the campaign
confirm or displace the default?

```
Run the full evidence campaign for: {{topic}}

Before gathering evidence, state the inertia position: what would a reasonable team
believe about {{topic}} if they relied only on default assumptions, prior experience,
or conventional wisdom — without running this investigation?

INERTIA POSITION: [state in 1-2 sentences — the default belief this campaign will test]

The purpose of this campaign is to test, confirm, or displace the inertia position.
Every stage contributes evidence toward that verdict.

---

CALIBRATION RULE: Confidence ratings must vary — at least two distinct levels (High /
Medium / Low) across findings. Uniform confidence is a calibration failure.

FALSIFICATION RULE: Every hypothesis carries Supported / Refuted / Indeterminate with
a named evidence basis. No outcome without a finding citation.

ATTRIBUTION RULE: Every material claim in synthesis names its source stage.

---

Stage 1 — prove-hypothesis

Given the inertia position above, state what you believe about {{topic}} and what
would change your mind.

Claim: [one sentence — how this claim relates to the inertia position: accepts it,
  refines it, or challenges it]
Falsification condition: [what would disprove this]
Confidence prior: [High / Medium / Low] — [reason]
Experiments: [2-3 tests]

Write to: simulations/prove/investigations/{{topic}}-hypothesis-{{date}}.md

---

Stage 2 — prove-websearch

Search the public web for evidence relevant to {{topic}}.

For each source: URL (required — no training-data claims), verbatim quote, strength
(Weak / Moderate / Strong), bearing (Supports / Refutes / Neutral). Also note: does
this source support or challenge the inertia position?

Write to: simulations/prove/investigations/{{topic}}-websearch-{{date}}.md

---

Stage 3 — prove-intelligence

Search internal sources (repo files, design docs, scenarios, prior signals).

For each source: exact file path, relevant excerpt, strength, bearing. Also note:
does this source confirm or challenge the inertia position?

Write to: simulations/prove/investigations/{{topic}}-intelligence-{{date}}.md

---

Stage 4 — prove-analysis

Analyze patterns across Stages 1-3. For each pattern: source, pattern, causal or
correlational (mechanism required for causal), confidence (High / Medium / Low — reason).

Also identify: which patterns confirm the inertia position? Which patterns challenge it?

Write to: simulations/prove/investigations/{{topic}}-analysis-{{date}}.md

---

Stage 5 — prove-synthesize

Apply CALIBRATION RULE before writing: verify at least two distinct confidence levels
appear across all stages. Revise if uniform.

Write the evidence brief:

**Evidence Brief: {{topic}}**
**Investigation date**: {{date}}

**Inertia position** (pre-investigation default): [from intro — what a team would
  have concluded without this campaign]

**Hypothesis** (Stage 1): [claim]
**Falsification status** [FALSIFICATION RULE]: [Supported / Refuted / Indeterminate]
**Basis**: [Stage N — specific finding that determined this outcome]

**Key findings** [ATTRIBUTION RULE — every finding names its source stage]:
1. [finding] — Stage [N] — Confidence: [H/M/L] — Inertia: [confirms / challenges]
2. [finding] — Stage [N] — Confidence: [H/M/L] — Inertia: [confirms / challenges]
3. [finding] — Stage [N] — Confidence: [H/M/L] — Inertia: [confirms / challenges]
4. [finding] — Stage [N] — Confidence: [H/M/L] — Inertia: [confirms / challenges]
5. [finding] — Stage [N] — Confidence: [H/M/L] — Inertia: [confirms / challenges]

[CALIBRATION RULE: confirm at least two distinct confidence levels appear above]

**Consensus** (Stage 2 vs Stage 3): [where web and internal sources agreed]
**Divergence** (Stage 2 vs Stage 3): [where they disagreed — and why it matters]

**Inertia verdict**: Did the campaign confirm, partially displace, or fully challenge
the inertia position? [1-2 sentences]

**Counter-evidence**: [the finding most challenging to the hypothesis, with stage cite]

**Open gaps**: [what the campaign did not resolve — specifically, what the inertia
  position assumed that the campaign left unanswered]

**Decision readiness**: [one sentence — ready to proceed or needs more investigation
on [specific named gap]]

Write to: simulations/prove/investigations/{{topic}}-synthesis-{{date}}.md
```

**Rubric targeting**: C-01 (five stages), C-02 (per-finding confidence), C-03
(FALSIFICATION RULE + status + basis), C-04 (inertia frame makes brief legible to
outsider), C-05 (ATTRIBUTION RULE), C-06 (consensus/divergence), C-07 (CALIBRATION
RULE anti-uniformity), C-08 (open gaps reframed as inertia gaps), C-09 (decision
readiness), C-11 (CALIBRATION RULE named), C-12 (one-sentence directive).
**Misses**: C-10 (standard sequence — hypothesis before evidence), C-13 (rules invoked
in synthesis headers but not at intermediate stages), C-14 (no reordering, so
principle is not applicable).
**Risk**: Inertia framing is additive overhead — a model may produce shallow inertia
labels ("confirms" / "challenges") as checkbox behavior without genuine comparison.
C-10 and C-14 are absent; scores cap at 12/14 criteria. Inertia framing is the only
new structural contribution this variation makes relative to R2 variations.

---

## V-04 — Combined Axes: Evidence-first + Named rule invocation (C-10 + C-13)

**Hypothesis**: Combining structural evidence-first sequencing with systematic named
rule invocations at every application stage — not just synthesis — yields the strongest
possible coverage of C-10 and C-13 simultaneously. Evidence-first prevents hypothesis
pre-anchoring structurally (C-10). Per-stage rule invocations prevent C-13 from being
satisfied only at synthesis (C-13 at maximum enforcement). C-14 is addressed at a
single position (Stage 3) which passes the criterion without triple-encoding.

```
Run the full evidence campaign for: {{topic}}

Produce a complete evidence brief — a single document readable by someone unfamiliar
with the run. Evidence-first sequencing: web search and intelligence stages complete
before the hypothesis is declared.

---

CALIBRATION RULE
Confidence ratings must vary. At least two distinct levels (High / Medium / Low) must
appear in the synthesis. Uniform confidence is a calibration failure.

FALSIFICATION RULE
Every hypothesis carries Supported / Refuted / Indeterminate with a named evidence
basis. A hypothesis without an outcome is a draft.

ATTRIBUTION RULE
Every material claim in synthesis names its source stage. "[claim] — Stage [N]."
Floating claims not traceable to a stage are not acceptable.

SEQUENCING RULE
Web search and internal search complete before hypothesis declaration. A hypothesis
anchored before evidence gathering is a bias, not a hypothesis.

---

Stage 1 — prove-websearch

Search the public web for evidence relevant to {{topic}}.

For each source:
- URL (required — no training-data claims)
- Direct quote (verbatim)
- Strength: Weak / Moderate / Strong
- Bearing: Supports / Refutes / Neutral

[ATTRIBUTION RULE invoked: label each source with URL now — these become Stage 1
  citations in synthesis]
[SEQUENCING RULE invoked: this stage runs before hypothesis declaration by design]

Write to: simulations/prove/investigations/{{topic}}-websearch-{{date}}.md

---

Stage 2 — prove-intelligence

Search internal sources (repo files, design docs, scenarios, prior signals).

For each source:
- File path (exact)
- Relevant excerpt
- Strength: Weak / Moderate / Strong
- Bearing: Supports / Refutes / Neutral

[ATTRIBUTION RULE invoked: exact file paths required — these become Stage 2 citations
  in synthesis]
[SEQUENCING RULE invoked: this stage runs before hypothesis declaration by design]

Write to: simulations/prove/investigations/{{topic}}-intelligence-{{date}}.md

---

Stage 3 — prove-hypothesis [POST-EVIDENCE]

[SEQUENCING RULE invoked: this stage runs after Stages 1 and 2 because a hypothesis
  anchored before evidence gathering is a bias, not a hypothesis. The claim below
  must reflect what the evidence supports you believing.]

Claim: [one sentence — what Stages 1-2 support you believing]
Falsification condition: [what would disprove this — cite Stage 1 or 2 evidence
  that shaped this choice]
Confidence: [High / Medium / Low] — [cite specific findings from Stages 1-2]
Experiments: [2-3 further tests]

[FALSIFICATION RULE invoked: falsification condition must be non-trivial and
  evidence-grounded — vague conditions fail]

Write to: simulations/prove/investigations/{{topic}}-hypothesis-{{date}}.md

---

Stage 4 — prove-analysis

Analyze patterns across Stages 1-3 evidence.

For each pattern: source, pattern, causal or correlational (mechanism required for
causal), confidence (High / Medium / Low — reason).

[CALIBRATION RULE invoked: per-pattern confidence ratings start here — variation
  should appear; if every pattern is the same level, revisit before synthesis]

Write to: simulations/prove/investigations/{{topic}}-analysis-{{date}}.md

---

Stage 5 — prove-synthesize

[CALIBRATION RULE invoked: before writing, verify at least two distinct confidence
  levels across all stages. Revise now if uniform.]
[FALSIFICATION RULE invoked: brief must declare status and name the basis finding.]
[ATTRIBUTION RULE invoked: every finding in the brief names its source stage.]
[SEQUENCING RULE invoked: brief records that hypothesis was declared post-evidence
  and states why — this is auditable design.]

Write the evidence brief:

**Evidence Brief: {{topic}}**
**Investigation date**: {{date}}
**Sequencing**: Evidence-first — hypothesis declared post-evidence (Stage 3 follows
Stages 1-2). A hypothesis anchored before evidence gathering is a bias, not a hypothesis.

**Hypothesis** (declared post-evidence, Stage 3): [claim]
**Falsification status** [FALSIFICATION RULE invoked]: [Supported / Refuted / Indeterminate]
**Basis**: [Stage N — specific finding that determined this outcome]

**Key findings** [ATTRIBUTION RULE invoked — every finding names its source stage]:
1. [finding] — Stage [N] — Confidence: [High / Medium / Low] — [one-clause rationale]
2. [finding] — Stage [N] — Confidence: [High / Medium / Low] — [one-clause rationale]
3. [finding] — Stage [N] — Confidence: [High / Medium / Low] — [one-clause rationale]
4. [finding] — Stage [N] — Confidence: [High / Medium / Low] — [one-clause rationale]
5. [finding] — Stage [N] — Confidence: [High / Medium / Low] — [one-clause rationale]

[CALIBRATION RULE invoked: two distinct confidence levels present above?]

**Consensus** (Stage 1 vs Stage 2): [where web and internal sources agreed]
**Divergence** (Stage 1 vs Stage 2): [where they disagreed — and why it matters]

**Counter-evidence**: [the finding most challenging to the hypothesis, with stage cite]

**Open gaps**: [what the campaign did not resolve — enables follow-up to pick up cleanly]

**Decision readiness**: [one sentence — "Ready to proceed" or "Needs more investigation
on [specific named gap] before committing."]

Write to: simulations/prove/investigations/{{topic}}-synthesis-{{date}}.md
```

**Rubric targeting**: C-01 (five stages in evidence-first order), C-02 (per-finding
confidence with rationale), C-03 (FALSIFICATION RULE invoked + status + basis),
C-04 (titled, dated, self-contained), C-05 (ATTRIBUTION RULE per finding), C-06
(consensus/divergence named), C-07 (CALIBRATION RULE anti-uniformity), C-08 (open
gaps), C-09 (decision readiness), C-10 (evidence-first: Stage 3 structurally follows
Stages 1-2), C-11 (CALIBRATION RULE as named anti-uniformity guard), C-12 (one-
sentence directive), C-13 (named rules at preamble, invoked by name at EVERY
intermediate stage AND synthesis), C-14 (reordering rationale stated at Stage 3
header and synthesis preamble).
**Risk**: The SEQUENCING RULE invocation at Stages 1 and 2 ("runs before hypothesis
declaration by design") may feel redundant — the order itself communicates this. C-14
has a single rationale sentence at Stage 3 and one in synthesis; not triple-encoded
like V-02 but still structurally present. Richest C-13 coverage of any variation.

---

## V-05 — Full Stack: Evidence-first + Named rules + Reordering rationale + Inertia framing

**Combined axes**: Role sequence (evidence-first) + Named rule invocation (per-stage)
+ Hypothesis reordering rationale (C-14 at three positions) + Inertia framing

**Hypothesis**: The full-stack combination targets all 14 criteria. Evidence-first
handles C-10 structurally. Named rules with per-stage invocations handle C-13 at
maximum enforcement. Reordering rationale at three structural positions handles C-14
redundantly. Inertia framing — the one axis from the R3 menu not covered in any other
R3 variation — adds independent structural depth to C-04 (self-contained brief with
before/after frame) and C-08 (gaps named relative to what the default assumed). The
combination is additive: no axis competes with another; each contributes independently.

```
Run the full evidence campaign for: {{topic}}

Produce a complete, self-contained evidence brief — readable by someone who did not
run the investigation. This campaign uses evidence-first sequencing and inertia
framing: before gathering evidence, name the default belief; after, show what changed.

INERTIA POSITION: [state in 1-2 sentences — what a reasonable team would believe
  about {{topic}} without running this investigation]

SEQUENCING PRINCIPLE: A hypothesis anchored before evidence gathering is a bias, not
a hypothesis. Evidence gathered under a pre-committed framing is filtered evidence.
The hypothesis is declared after Stages 1 and 2 complete. This principle is recorded
in the synthesis so readers can evaluate whether falsification decisions were grounded
in actual findings.

---

CALIBRATION RULE
Confidence ratings must vary. At least two distinct levels (High / Medium / Low) must
appear across findings. Uniform confidence is a calibration failure.

FALSIFICATION RULE
Every hypothesis carries Supported / Refuted / Indeterminate with a named evidence
basis. No outcome without a finding citation.

ATTRIBUTION RULE
Every material claim in synthesis names its source stage: "[claim] — Stage [N]."
Claims without stage attribution are not acceptable.

INERTIA RULE
The synthesis explicitly compares findings against the inertia position — naming what
the evidence confirmed, displaced, or left unresolved relative to the default belief.

---

Stage 1 — prove-websearch

Search the public web for evidence relevant to {{topic}}.

For each source: URL (required — no training-data claims), verbatim quote, strength
(Weak / Moderate / Strong), bearing (Supports / Refutes / Neutral).

[ATTRIBUTION RULE invoked: label each source with URL now — these become Stage 1
  citations in synthesis]
[INERTIA RULE invoked: note whether each source supports or challenges the inertia
  position — this feeds the inertia verdict in synthesis]

Write to: simulations/prove/investigations/{{topic}}-websearch-{{date}}.md

---

Stage 2 — prove-intelligence

Search internal sources (repo files, design docs, scenarios, prior signals).

For each source: exact file path, relevant excerpt, strength, bearing.

[ATTRIBUTION RULE invoked: exact file paths required — these become Stage 2 citations]
[INERTIA RULE invoked: note whether each source confirms or challenges the inertia
  position]

Write to: simulations/prove/investigations/{{topic}}-intelligence-{{date}}.md

---

Stage 3 — prove-hypothesis [EVIDENCE-INFORMED DECLARATION]

[SEQUENCING PRINCIPLE invoked: this stage runs third. A hypothesis anchored before
  evidence gathering is a bias, not a hypothesis. You have now seen what Stages 1
  and 2 found. The claim below must reflect what the evidence supports you believing
  — not a prior intuition.]

Claim: [one sentence — what the evidence supports you believing]
Falsification condition: [what would disprove this — cite Stages 1-2 findings that
  shaped this choice]
Confidence: [High / Medium / Low] — [cite specific Stage 1-2 findings]
Experiments: [2-3 further tests]

[FALSIFICATION RULE invoked: falsification condition must be specific enough that
  evidence could satisfy it — vague conditions fail]

Write to: simulations/prove/investigations/{{topic}}-hypothesis-{{date}}.md

---

Stage 4 — prove-analysis

Analyze patterns across Stages 1-3 evidence.

For each pattern: source, pattern observed, causal or correlational (mechanism required
for causal), confidence (High / Medium / Low — reason).

[CALIBRATION RULE invoked: per-pattern confidence ratings start here — variation must
  appear; if every pattern is the same level, revisit before synthesis]

Write to: simulations/prove/investigations/{{topic}}-analysis-{{date}}.md

---

Stage 5 — prove-synthesize

[CALIBRATION RULE invoked: before writing, verify at least two distinct confidence
  levels appear across all stages. Revise now if uniform.]
[FALSIFICATION RULE invoked: brief must declare status and name the basis finding.]
[ATTRIBUTION RULE invoked: every finding names its source stage.]
[INERTIA RULE invoked: synthesis compares findings against inertia position explicitly.]
[SEQUENCING PRINCIPLE invoked: brief records evidence-first sequencing and states
  the principle — auditable design, not incidental ordering.]

Write the evidence brief:

**Evidence Brief: {{topic}}**
**Investigation date**: {{date}}

**Inertia position** (pre-investigation default): [what a team would have concluded
  about {{topic}} without this campaign]

**Sequencing**: Evidence-first — hypothesis declared post-evidence (Stage 3 follows
Stages 1-2). A hypothesis anchored before evidence gathering is a bias, not a
hypothesis. Falsification decisions below are grounded in what Stages 1 and 2
actually found.

**Hypothesis** (declared post-evidence, Stage 3): [claim]
**Falsification status** [FALSIFICATION RULE invoked]: [Supported / Refuted / Indeterminate]
**Basis**: [Stage N — specific finding that determined this outcome]

**Key findings** [ATTRIBUTION RULE invoked — every finding names its source stage]:
1. [finding] — Stage [N] — Confidence: [H/M/L] — Inertia: [confirms / challenges] — [rationale]
2. [finding] — Stage [N] — Confidence: [H/M/L] — Inertia: [confirms / challenges] — [rationale]
3. [finding] — Stage [N] — Confidence: [H/M/L] — Inertia: [confirms / challenges] — [rationale]
4. [finding] — Stage [N] — Confidence: [H/M/L] — Inertia: [confirms / challenges] — [rationale]
5. [finding] — Stage [N] — Confidence: [H/M/L] — Inertia: [confirms / challenges] — [rationale]

[CALIBRATION RULE invoked: two distinct confidence levels present above?]

**Consensus** (Stage 1 vs Stage 2): [where web and internal sources agreed]
**Divergence** (Stage 1 vs Stage 2): [where they disagreed — and why it matters]

**Inertia verdict** [INERTIA RULE invoked]: Did the campaign confirm, partially
displace, or fully challenge the inertia position? [1-2 sentences naming what shifted
and what did not]

**Counter-evidence**: [the finding most challenging to the hypothesis, with stage cite]

**Open gaps**: [what the campaign did not resolve — specifically, what the inertia
  position assumed that the evidence left unanswered]

**Decision readiness**: [one sentence — "Ready to proceed" or "Needs more investigation
on [specific named gap] before committing."]

Write to: simulations/prove/investigations/{{topic}}-synthesis-{{date}}.md
```

**Rubric targeting**: C-01 (five stages in evidence-first order), C-02 (per-finding
confidence with rationale), C-03 (FALSIFICATION RULE invoked + status + basis),
C-04 (inertia frame makes brief legible to outsider without context), C-05 (ATTRIBUTION
RULE per finding), C-06 (consensus/divergence named), C-07 (CALIBRATION RULE anti-
uniformity), C-08 (open gaps defined relative to inertia assumptions), C-09 (decision
readiness), C-10 (evidence-first: Stage 3 structurally follows Stages 1-2), C-11
(CALIBRATION RULE as named anti-uniformity guard), C-12 (one-sentence directive),
C-13 (four named rules at preamble, invoked by name at every intermediate stage AND
synthesis), C-14 (SEQUENCING PRINCIPLE at three positions: intro, Stage 3 header,
synthesis preamble — with the full rationale sentence at each).
**Risk**: This is the longest variation. Inertia framing adds a per-finding column
and an inertia verdict section; combined with per-stage rule invocations, a model
following the template may produce verbose but shallow output — every cell filled,
no cell substantive. The four named rules (adding INERTIA RULE to V-04's three) make
the preamble block heavier; a model may read it as boilerplate and skip to the stage
templates.

---

## Variation Summary

| ID | Axes | Primary Rubric Targets | Criteria Covered | Key Risk |
|----|------|----------------------|-----------------|----------|
| V-01 | Named rule invocation (per-stage) | C-01..C-09, C-11..C-13 | 12/14 | Misses C-10, C-14; boilerplate invocations |
| V-02 | Hypothesis reordering rationale (3 positions) | C-01..C-14 | 14/14 | C-13 synthesis-only; weakest per-stage enforcement |
| V-03 | Inertia framing | C-01..C-09, C-11..C-12 + inertia depth | 12/14 | Misses C-10, C-13 (per-stage), C-14; inertia as checkbox |
| V-04 | Evidence-first + Named rule invocation | C-01..C-14 | 14/14 | C-14 single-position; richest C-13 enforcement |
| V-05 | Evidence-first + Named rules + Rationale + Inertia | C-01..C-14 + depth | 14/14 | Most complex; risk of verbose but shallow filling |

**Predicted leaderboard going into quest-score**: V-05 > V-04 > V-02 > V-01 > V-03.

V-05 is the only variation that covers all 14 criteria AND adds inertia framing as
independent structural depth for C-04 and C-08. V-04 covers all 14 with the strictest
C-13 enforcement (per-stage invocations for four named rules) but no inertia framing.
V-02 passes C-14 most robustly (triple-encoded) but has weaker C-13 (invocations at
synthesis only). V-01 has the cleanest C-13 pattern but structurally cannot reach C-10
or C-14. V-03 introduces the inertia axis but does not enforce evidence-first or named
rule invocations at each stage, leaving C-10, C-13, and C-14 at risk.

The main open question for scoring: does C-13 require invocation at every application
stage (favors V-04 and V-05) or is synthesis-level invocation sufficient (levels
V-02 up to match V-04)? The rubric says "at the step where they apply" — which
suggests each step, not only synthesis.
