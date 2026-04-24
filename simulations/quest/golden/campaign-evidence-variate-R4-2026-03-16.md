---
skill: quest-variate
skill_target: campaign-evidence
round: 4
date: 2026-03-16
rubric: simulations/quest/rubrics/campaign-evidence-rubric-v4-2026-03-16.md
---

# Variations — campaign-evidence / Round 4

Five complete, runnable skill body variations. Single-axis first (V-01, V-02, V-03),
then combined (V-04, V-05).

R4 rubric adds C-15 and C-16. C-15 requires the sequencing decision to be declared
as a named rule — not an unnamed convention or a narrative principle. The SEQUENCING
RULE must appear in the preamble rule block at the same tier as CALIBRATION, FALSIFICATION,
and ATTRIBUTION, and be referenceable by identifier at each stage it governs. C-16
requires zero-gap invocation: every declared rule is invoked by name at every stage
where it applies, with full coverage across ATTRIBUTION (evidence-gathering stages),
CALIBRATION (analysis and synthesis), FALSIFICATION (hypothesis declaration and
synthesis), and SEQUENCING (all stages whose ordering the rule governs).

R3's V-04 came closest on both criteria: it declared SEQUENCING RULE in the preamble
and invoked it at Stages 1, 2, 3, and 5. But C-15 and C-16 were not yet rubric
criteria, so the enforcement was aspirational. R4 tests three distinct mechanisms for
satisfying these criteria and then combines them.

---

## V-01 — Axis: C-15 (SEQUENCING elevated to formal named rule)

**Hypothesis**: Placing SEQUENCING RULE in the preamble rule block — same visual tier,
same identifier format as CALIBRATION RULE, FALSIFICATION RULE, ATTRIBUTION RULE —
makes it a first-class governance rule rather than an unnamed structural convention or
a narrative principle. C-15 is not satisfied by evidence-first ordering alone, nor by
a "SEQUENCING PRINCIPLE" outside the rule block. The criterion requires that the
sequencing decision be promotable to a rule that any reader can cite by name. A
variation that changes only this — from structural label to declared, referenceable
rule — tests whether C-15 is a naming and placement decision or a behavioral one.

```
Run the full evidence campaign for: {{topic}}

Produce a complete evidence brief. Evidence-first sequencing: web search and internal
search complete before the hypothesis is declared.

---

CALIBRATION RULE
Confidence ratings must vary. At least two distinct levels (High / Medium / Low) must
appear across all findings. Uniform confidence is a calibration failure. At synthesis,
check the confidence column before submitting — if every row carries the same level,
calibration has not occurred.

FALSIFICATION RULE
Every hypothesis carries an explicit status (Supported / Refuted / Indeterminate) with
a named evidence basis. A hypothesis without a falsification outcome is a draft, not
a finding.

ATTRIBUTION RULE
Every material claim in synthesis names its source stage: "[claim] — Stage [N]."
Claims without stage attribution are not acceptable. Websearch claims require URLs;
intelligence claims require exact file paths.

SEQUENCING RULE
Web search and internal search complete before hypothesis declaration. A hypothesis
anchored before evidence gathering is a bias, not a hypothesis. This rule governs the
ordering of Stages 1, 2, and 3 — it is a declared governance rule, not an unnamed
structural convention. Cite it by identifier at each stage it governs.

---

Stage 1 — prove-websearch

Search the public web for evidence relevant to {{topic}}.

For each source: URL (required — no training-data claims), verbatim quote,
strength (Weak / Moderate / Strong), bearing (Supports / Refutes / Neutral).

[SEQUENCING RULE invoked: Stage 1 runs before hypothesis declaration — this ordering
  is a named governance decision, not incidental]
[ATTRIBUTION RULE invoked: every source requires a URL; these become Stage 1 citations
  in synthesis]

Write to: simulations/prove/investigations/{{topic}}-websearch-{{date}}.md

---

Stage 2 — prove-intelligence

Search internal sources (repo files, design docs, scenarios, prior signals).

For each source: exact file path, relevant excerpt, strength, bearing.

[SEQUENCING RULE invoked: Stage 2 runs before hypothesis declaration by SEQUENCING RULE]
[ATTRIBUTION RULE invoked: exact file paths required — these become Stage 2 citations]

Write to: simulations/prove/investigations/{{topic}}-intelligence-{{date}}.md

---

Stage 3 — prove-hypothesis [POST-EVIDENCE]

[SEQUENCING RULE invoked: this stage runs third because a hypothesis anchored before
  evidence gathering is a bias, not a hypothesis. The claim below must reflect what
  Stages 1 and 2 support you believing — not a prior intuition.]

Claim: [one sentence — what the evidence from Stages 1-2 supports you believing]
Falsification condition: [what would disprove this — cite Stage 1-2 findings that
  shaped this choice]
Confidence: [High / Medium / Low] — [cite specific Stage 1-2 findings that drive
  this rating]
Experiments: [2-3 further tests]

[FALSIFICATION RULE invoked: falsification condition must be specific enough that
  evidence could satisfy it — a condition no evidence could disprove is not falsifiable]

Write to: simulations/prove/investigations/{{topic}}-hypothesis-{{date}}.md

---

Stage 4 — prove-analysis

Analyze patterns across the evidence from Stages 1-3.

For each pattern: source (Stage 2 row / Stage 3 file), pattern observed, causal or
correlational (mechanism required for causal), confidence (High / Medium / Low — reason).

[CALIBRATION RULE invoked: confidence ratings across patterns start here — at least two
  distinct levels should appear; uniform ratings at Stage 4 will produce uniform ratings
  in synthesis — revise now if all patterns carry the same level]

Write to: simulations/prove/investigations/{{topic}}-analysis-{{date}}.md

---

Stage 5 — prove-synthesize

[CALIBRATION RULE invoked: before writing, verify at least two distinct confidence
  levels appear across Stages 1-4. Revise now if uniform.]
[FALSIFICATION RULE invoked: synthesis must declare Supported / Refuted / Indeterminate
  and name the specific finding that determined the outcome.]
[ATTRIBUTION RULE invoked: every finding in the brief names its source stage.]
[SEQUENCING RULE invoked: the brief records that hypothesis was declared post-evidence
  and states why — the sequencing choice is a named governance rule, auditable by any
  reader who can cite SEQUENCING RULE by identifier.]

Write the evidence brief:

**Evidence Brief: {{topic}}**
**Investigation date**: {{date}}

**Sequencing** [SEQUENCING RULE]: Evidence-first — hypothesis declared post-evidence
(Stage 3 follows Stages 1-2). A hypothesis anchored before evidence gathering is a
bias, not a hypothesis.

**Hypothesis** (declared post-evidence, Stage 3): [claim]
**Falsification status** [FALSIFICATION RULE]: [Supported / Refuted / Indeterminate]
**Basis**: [Stage N — specific finding that determined this outcome]

**Key findings** [ATTRIBUTION RULE — every finding names its source stage]:
1. [finding] — Stage [N] — Confidence: [High / Medium / Low] — [one-clause rationale]
2. [finding] — Stage [N] — Confidence: [High / Medium / Low] — [one-clause rationale]
3. [finding] — Stage [N] — Confidence: [High / Medium / Low] — [one-clause rationale]
4. [finding] — Stage [N] — Confidence: [High / Medium / Low] — [one-clause rationale]
5. [finding] — Stage [N] — Confidence: [High / Medium / Low] — [one-clause rationale]

[CALIBRATION RULE invoked: two distinct confidence levels present above?]

**Consensus** (Stage 1 vs Stage 2): [where web and internal sources agreed]
**Divergence** (Stage 1 vs Stage 2): [where they disagreed — and why it matters]

**Counter-evidence**: [finding most challenging to the hypothesis, with stage cite]

**Open gaps**: [what the campaign did not resolve]

**Decision readiness**: [one sentence — "Ready to proceed" or "Needs more investigation
on [specific named gap] before committing."]

Write to: simulations/prove/investigations/{{topic}}-synthesis-{{date}}.md
```

**Rubric targeting**: C-01 (five named stages, evidence-first), C-02 (per-finding
confidence with rationale), C-03 (FALSIFICATION RULE + status + basis), C-04 (titled,
dated, self-contained), C-05 (ATTRIBUTION RULE per finding), C-06 (consensus/divergence),
C-07 (CALIBRATION RULE anti-uniformity), C-08 (open gaps), C-09 (decision readiness),
C-10 (structural evidence-first), C-11 (CALIBRATION RULE as named anti-uniformity guard),
C-12 (one-sentence directive), C-13 (four named rules at preamble, invoked at point of
use), C-14 (reordering rationale at Stage 3 and synthesis), C-15 (SEQUENCING RULE
declared in the preamble rule block at the same tier as CALIBRATION, FALSIFICATION,
ATTRIBUTION — referenceable by identifier at each governed stage), C-16 (ATTRIBUTION
invoked at Stages 1 and 2; CALIBRATION invoked at Stages 4 and 5; FALSIFICATION invoked
at Stages 3 and 5; SEQUENCING invoked at Stages 1, 2, 3, and 5).
**Risk**: The single axis is naming and placement. A model that already produced R3 V-04
behavior will pass C-15 here; the test is whether the formal declaration changes anything
for a model that doesn't read the preamble carefully. C-16 coverage is complete but
untested with a coverage map — a model could still write the invocation tags without
actually applying the rules.

---

## V-02 — Axis: C-16 (Pre-declared Coverage Matrix, hypothesis-first)

**Hypothesis**: C-16's zero-gap requirement can be satisfied preventively by publishing
a coverage matrix before Stage 1 that maps each declared rule to every stage where it
applies. A model reading the matrix before executing knows what's expected at each step:
"at Stage 2, I must invoke ATTRIBUTION RULE and EVIDENCE RULE." The matrix pre-commits
the model to complete coverage; gaps become visible violations rather than silent
omissions. This variation tests whether preventive scaffolding — a contract declared
before any stage runs — enforces zero-gap invocation more reliably than embedded stage
reminders alone, and does so without evidence-first sequencing (C-10/C-15 intentionally
absent to isolate the C-16 axis).

```
Run the full evidence campaign for: {{topic}}

Produce a complete evidence brief — a single document readable by someone unfamiliar
with the run. Standard sequence: prove-hypothesis, prove-websearch, prove-intelligence,
prove-analysis, prove-synthesize.

---

CALIBRATION RULE
Confidence ratings must vary. At least two distinct levels (High / Medium / Low) must
appear across all findings. Uniform confidence is a calibration failure.

FALSIFICATION RULE
Every hypothesis carries Supported / Refuted / Indeterminate with a named evidence basis.
No outcome without a finding citation.

ATTRIBUTION RULE
Every material claim in synthesis names its source stage. "[claim] — Stage [N]."
Websearch claims require URLs; intelligence claims require exact file paths.

EVIDENCE RULE
Stage 2 (websearch) requires URLs — no training-data claims. Stage 3 (intelligence)
requires exact file paths.

---

RULE COVERAGE MAP

This map declares which rules are invoked at each stage. Every cell marked "invoke"
must carry an explicit [RULE_NAME invoked] tag in the stage output. A stage that
omits a required invocation fails C-16.

| Rule              | Stage 1 | Stage 2 | Stage 3 | Stage 4 | Stage 5 |
|-------------------|---------|---------|---------|---------|---------|
| CALIBRATION RULE  | —       | —       | —       | invoke  | invoke  |
| FALSIFICATION RULE| invoke  | —       | —       | —       | invoke  |
| ATTRIBUTION RULE  | —       | invoke  | invoke  | —       | invoke  |
| EVIDENCE RULE     | —       | invoke  | invoke  | —       | —       |

Read the map before executing Stage 1. At each stage, invoke every rule marked
"invoke" for that stage before writing content.

---

Stage 1 — prove-hypothesis

State the investigation frame.

Claim: [one sentence — what you believe]
Falsification condition: [what would disprove this]
Confidence prior: [High / Medium / Low] — [one-clause reason]
Experiments: [2-3 tests]

[FALSIFICATION RULE invoked: falsification condition declared here — specific enough
  that evidence could satisfy or deny it]

Write to: simulations/prove/investigations/{{topic}}-hypothesis-{{date}}.md

---

Stage 2 — prove-websearch

Search the public web for evidence relevant to {{topic}}.

For each source: URL, verbatim quote, strength (Weak / Moderate / Strong), bearing
(Supports / Refutes / Neutral).

[ATTRIBUTION RULE invoked: every source requires a URL — these become Stage 2 citations]
[EVIDENCE RULE invoked: no training-data claims — URL required per source]

Write to: simulations/prove/investigations/{{topic}}-websearch-{{date}}.md

---

Stage 3 — prove-intelligence

Search internal sources (repo files, design docs, scenarios, prior signals).

For each source: exact file path, relevant excerpt, strength, bearing.

[ATTRIBUTION RULE invoked: exact file paths required — these become Stage 3 citations]
[EVIDENCE RULE invoked: exact file paths required — "the codebase" without a path
  is rejected]

Write to: simulations/prove/investigations/{{topic}}-intelligence-{{date}}.md

---

Stage 4 — prove-analysis

Analyze patterns across Stages 1-3 evidence.

For each pattern: source, pattern observed, causal or correlational (mechanism required
for causal), confidence (High / Medium / Low — reason).

[CALIBRATION RULE invoked: confidence ratings across patterns start here — variation
  must appear; uniform ratings at Stage 4 will produce uniform ratings in synthesis —
  redistribute now if all patterns carry the same level]

Write to: simulations/prove/investigations/{{topic}}-analysis-{{date}}.md

---

Stage 5 — prove-synthesize

[CALIBRATION RULE invoked: before writing, verify at least two distinct confidence
  levels appear across Stages 1-4. Revise now if uniform.]
[FALSIFICATION RULE invoked: synthesis must declare status and name the basis finding.]
[ATTRIBUTION RULE invoked: every finding names its source stage.]

Write the evidence brief:

**Evidence Brief: {{topic}}**
**Investigation date**: {{date}}

**Hypothesis** (Stage 1): [claim]
**Falsification status** [FALSIFICATION RULE]: [Supported / Refuted / Indeterminate]
**Basis**: [Stage N — specific finding that determined this outcome]

**Key findings** [ATTRIBUTION RULE — every finding names its source stage]:
1. [finding] — Stage [N] — Confidence: [High / Medium / Low] — [one-clause rationale]
2. [finding] — Stage [N] — Confidence: [High / Medium / Low] — [one-clause rationale]
3. [finding] — Stage [N] — Confidence: [High / Medium / Low] — [one-clause rationale]
4. [finding] — Stage [N] — Confidence: [High / Medium / Low] — [one-clause rationale]
5. [finding] — Stage [N] — Confidence: [High / Medium / Low] — [one-clause rationale]

[CALIBRATION RULE invoked: two distinct confidence levels present above?]

**Consensus** (Stage 2 vs Stage 3): [where web and internal sources agreed]
**Divergence** (Stage 2 vs Stage 3): [where they disagreed — and why it matters]

**Counter-evidence**: [finding most challenging to the hypothesis, with stage cite]

**Open gaps**: [what the campaign did not resolve]

**Decision readiness**: [one sentence — ready to proceed or needs more investigation
on [specific named gap]]

Write to: simulations/prove/investigations/{{topic}}-synthesis-{{date}}.md
```

**Rubric targeting**: C-01 (five named stages), C-02 (per-finding confidence), C-03
(FALSIFICATION RULE + status + basis), C-04 (titled, dated, self-contained), C-05
(ATTRIBUTION RULE per finding), C-06 (consensus/divergence), C-07 (CALIBRATION RULE
anti-uniformity), C-08 (open gaps), C-09 (decision readiness), C-11 (CALIBRATION RULE
as named anti-uniformity guard), C-12 (one-sentence directive), C-13 (named rules at
preamble, invoked at every applicable stage per coverage map), C-16 (coverage matrix
pre-declared; every "invoke" cell in the map must carry an explicit tag — gaps are
visible violations).
**Intentional misses**: C-10 (hypothesis-first sequence — SEQUENCING RULE not declared),
C-14 (no reordering, no rationale applicable), C-15 (no SEQUENCING RULE declared — this
variation isolates C-16 from C-15).
**Risk**: The coverage map is a pre-commitment, but a model that ignores the map header
and proceeds directly to Stage 1 will produce the same output as any prior variation.
The map's enforcement depends on the model reading and following the contract, not on
a structural mechanism that makes violation impossible. EVIDENCE RULE is declared here
as a fourth rule rather than SEQUENCING RULE — this covers websearch/intelligence
discipline without evidence-first ordering.

---

## V-03 — Axis: Output Format (Post-Brief Invocation Audit Table)

**Hypothesis**: A retrospective invocation audit table — required at the end of
Stage 5 synthesis — forces C-16 compliance by making every gap a visible blank cell.
The model writes the brief, then completes the audit table by marking where each rule
was invoked. A rule invoked only at synthesis but applicable at earlier stages will
produce a partially-filled row; the gap is auditable. This mechanism differs from the
coverage map (V-02) in causality: the map is preventive (contract before execution),
the audit table is retrospective (verification after execution). Retrospective checking
may surface invocations that were silently applied but not tagged — and force the model
to either go back and add tags or acknowledge the gap.

```
Run the full evidence campaign for: {{topic}}

Produce a complete evidence brief and a rule invocation audit confirming where each
governance rule was applied. The audit table is a required deliverable alongside the
brief — it confirms that no applicable stage was left untagged.

---

CALIBRATION RULE
Confidence ratings must vary. At least two distinct levels (High / Medium / Low) across
all findings. Uniform confidence is a calibration failure.

FALSIFICATION RULE
Every hypothesis carries Supported / Refuted / Indeterminate with a named evidence
basis. No outcome without a finding citation.

ATTRIBUTION RULE
Every material claim in synthesis names its source stage: "[claim] — Stage [N]."
Websearch claims require URLs; intelligence claims require exact file paths.

EVIDENCE RULE
Stage 2 (websearch): URLs required. Stage 3 (intelligence): exact file paths required.

---

Stage 1 — prove-hypothesis

Claim: [one sentence — what you believe]
Falsification condition: [what would disprove this]
Confidence prior: [High / Medium / Low] — [one-clause reason]
Experiments: [2-3 tests]

Apply all rules that govern this stage. Mark applied rules with [RULE_NAME invoked]
in your output.

Write to: simulations/prove/investigations/{{topic}}-hypothesis-{{date}}.md

---

Stage 2 — prove-websearch

Search the public web for evidence relevant to {{topic}}.

For each source: URL (required), verbatim quote, strength (Weak / Moderate / Strong),
bearing (Supports / Refutes / Neutral).

Apply all rules that govern this stage. Mark applied rules with [RULE_NAME invoked].

Write to: simulations/prove/investigations/{{topic}}-websearch-{{date}}.md

---

Stage 3 — prove-intelligence

Search internal sources (repo files, design docs, scenarios, prior signals).

For each source: exact file path, relevant excerpt, strength, bearing.

Apply all rules that govern this stage. Mark applied rules with [RULE_NAME invoked].

Write to: simulations/prove/investigations/{{topic}}-intelligence-{{date}}.md

---

Stage 4 — prove-analysis

Analyze patterns across Stages 1-3 evidence.

For each pattern: source, pattern, causal or correlational (mechanism required for
causal), confidence (High / Medium / Low — reason).

Apply all rules that govern this stage. Mark applied rules with [RULE_NAME invoked].

Write to: simulations/prove/investigations/{{topic}}-analysis-{{date}}.md

---

Stage 5 — prove-synthesize

Apply all rules that govern this stage. Mark applied rules with [RULE_NAME invoked].

Write the evidence brief:

**Evidence Brief: {{topic}}**
**Investigation date**: {{date}}

**Hypothesis** (Stage 1): [claim]
**Falsification status**: [Supported / Refuted / Indeterminate]
**Basis**: [Stage N — specific finding that determined this outcome]

**Key findings** (every finding names its source stage and confidence):
1. [finding] — Stage [N] — Confidence: [High / Medium / Low] — [one-clause rationale]
2. [finding] — Stage [N] — Confidence: [High / Medium / Low] — [one-clause rationale]
3. [finding] — Stage [N] — Confidence: [High / Medium / Low] — [one-clause rationale]
4. [finding] — Stage [N] — Confidence: [High / Medium / Low] — [one-clause rationale]
5. [finding] — Stage [N] — Confidence: [High / Medium / Low] — [one-clause rationale]

**Consensus** (Stage 2 vs Stage 3): [where web and internal sources agreed]
**Divergence** (Stage 2 vs Stage 3): [where they disagreed — and why it matters]

**Counter-evidence**: [finding most challenging to the hypothesis, with stage cite]

**Open gaps**: [what the campaign did not resolve]

**Decision readiness**: [one sentence — ready to proceed or needs more investigation
on [specific named gap]]

---

After completing the brief, fill in the invocation audit table below. For each cell,
write "invoked" if the rule was explicitly tagged in that stage's output, or leave
blank if the rule does not apply to that stage. A blank cell at a stage where the
rule applies is a C-16 violation — go back and add the invocation tag before
submitting.

**RULE INVOCATION AUDIT**

| Rule              | Stage 1 | Stage 2 | Stage 3 | Stage 4 | Stage 5 |
|-------------------|---------|---------|---------|---------|---------|
| CALIBRATION RULE  |         |         |         |         |         |
| FALSIFICATION RULE|         |         |         |         |         |
| ATTRIBUTION RULE  |         |         |         |         |         |
| EVIDENCE RULE     |         |         |         |         |         |

Expected pattern (cells that must be "invoked" for a complete audit):
- CALIBRATION RULE: Stage 4, Stage 5
- FALSIFICATION RULE: Stage 1, Stage 5
- ATTRIBUTION RULE: Stage 2, Stage 3, Stage 5
- EVIDENCE RULE: Stage 2, Stage 3

Any deviation from this expected pattern requires explanation or correction.

Write brief + audit to: simulations/prove/investigations/{{topic}}-synthesis-{{date}}.md
```

**Rubric targeting**: C-01 (five named stages), C-02 (per-finding confidence), C-03
(falsification status + basis in brief), C-04 (titled, dated, self-contained), C-05
(stage attribution per finding), C-06 (consensus/divergence), C-07 (CALIBRATION RULE
anti-uniformity), C-08 (open gaps), C-09 (decision readiness), C-11 (CALIBRATION RULE
as named anti-uniformity guard), C-12 (one-sentence directive), C-13 (named rules at
preamble; stage prompts say "apply all rules that govern this stage"), C-16 (audit
table + expected pattern forces retrospective verification — any gap is a visible blank
cell requiring correction before submission).
**Intentional misses**: C-10 (hypothesis-first), C-14 (no reordering), C-15 (no
SEQUENCING RULE declared).
**Risk**: The audit table is retrospective; a model that did not apply rules during
stages may fill in "invoked" dishonestly rather than going back. The instruction "go
back and add the invocation tag before submitting" creates a correction loop but
depends on the model following it. The stage prompts ("apply all rules that govern
this stage") without a coverage map leave the mapping implicit — a model must infer
which rules apply at which stages rather than reading them from a pre-declared matrix.
This is intentional: the test is whether the audit table as a retrospective mechanism
is sufficient on its own.

---

## V-04 — Combined Axes: C-15 + C-16 (SEQUENCING as Named Rule + Coverage Matrix)

**Hypothesis**: C-15 requires that SEQUENCING be a declared named rule in the preamble
rule block. C-16 requires zero-gap invocation per a coverage map. These two criteria are
naturally additive: C-15 provides the rule identifier that C-16 requires at every
governed stage. Without C-15, there is no SEQUENCING RULE for the coverage map to assign
to Stages 1, 2, 3, and 5. Without a coverage map, SEQUENCING RULE may be declared but
invoked only at synthesis (the weakest C-16 pattern). The combination makes C-15 and
C-16 mutually reinforcing: the formal rule declaration (C-15) feeds the coverage map
(C-16), and the coverage map enforces that SEQUENCING RULE is not merely named but
actually invoked at every applicable stage. C-14 is encoded at Stage 3 and synthesis
via the rationale sentence, making the C-10 + C-14 + C-15 + C-16 stack complete.

```
Run the full evidence campaign for: {{topic}}

Produce a complete evidence brief. Evidence-first sequencing: web search and internal
search complete before the hypothesis is declared.

---

CALIBRATION RULE
Confidence ratings must vary. At least two distinct levels (High / Medium / Low) must
appear across all findings. Uniform confidence is a calibration failure.

FALSIFICATION RULE
Every hypothesis carries Supported / Refuted / Indeterminate with a named evidence basis.
No outcome without a finding citation.

ATTRIBUTION RULE
Every material claim in synthesis names its source stage: "[claim] — Stage [N]."
Websearch claims require URLs; intelligence claims require exact file paths.

SEQUENCING RULE
Web search and internal search complete before hypothesis declaration. A hypothesis
anchored before evidence gathering is a bias, not a hypothesis. This is a declared
governance rule — not an unnamed structural convention. Cite it by identifier at each
stage whose position it governs.

---

RULE COVERAGE MAP

Read before executing Stage 1. At each stage, invoke every rule marked "invoke"
before writing content. A stage that omits a required invocation is a C-16 violation.

| Rule              | Stage 1    | Stage 2    | Stage 3    | Stage 4 | Stage 5 |
|-------------------|------------|------------|------------|---------|---------|
| CALIBRATION RULE  | —          | —          | —          | invoke  | invoke  |
| FALSIFICATION RULE| —          | —          | invoke     | —       | invoke  |
| ATTRIBUTION RULE  | invoke     | invoke     | —          | —       | invoke  |
| SEQUENCING RULE   | invoke     | invoke     | invoke     | —       | invoke  |

---

Stage 1 — prove-websearch

Search the public web for evidence relevant to {{topic}}.

For each source: URL (required — no training-data claims), verbatim quote,
strength (Weak / Moderate / Strong), bearing (Supports / Refutes / Neutral).

[SEQUENCING RULE invoked: Stage 1 runs before hypothesis declaration — this ordering
  is governed by SEQUENCING RULE, not incidental]
[ATTRIBUTION RULE invoked: every source requires a URL; these become Stage 1 citations
  in synthesis]

Write to: simulations/prove/investigations/{{topic}}-websearch-{{date}}.md

---

Stage 2 — prove-intelligence

Search internal sources (repo files, design docs, scenarios, prior signals).

For each source: exact file path, relevant excerpt, strength, bearing.

[SEQUENCING RULE invoked: Stage 2 runs before hypothesis declaration by SEQUENCING RULE]
[ATTRIBUTION RULE invoked: exact file paths required — these become Stage 2 citations]

Write to: simulations/prove/investigations/{{topic}}-intelligence-{{date}}.md

---

Stage 3 — prove-hypothesis [POST-EVIDENCE]

[SEQUENCING RULE invoked: this stage runs third because a hypothesis anchored before
  evidence gathering is a bias, not a hypothesis. The claim below must reflect what
  Stages 1 and 2 support you believing.]
[FALSIFICATION RULE invoked: falsification condition must be specific enough that
  evidence could satisfy it — vague conditions are not falsifiable]

Claim: [one sentence — what Stages 1-2 support you believing]
Falsification condition: [what would disprove this — cite Stage 1-2 findings that
  shaped this choice]
Confidence: [High / Medium / Low] — [cite specific Stage 1-2 findings]
Experiments: [2-3 further tests]

Write to: simulations/prove/investigations/{{topic}}-hypothesis-{{date}}.md

---

Stage 4 — prove-analysis

Analyze patterns across Stages 1-3 evidence.

For each pattern: source, pattern observed, causal or correlational (mechanism required
for causal), confidence (High / Medium / Low — reason).

[CALIBRATION RULE invoked: per-pattern confidence ratings start here — at least two
  distinct levels must appear by synthesis; revise now if all patterns carry the same
  level]

Write to: simulations/prove/investigations/{{topic}}-analysis-{{date}}.md

---

Stage 5 — prove-synthesize

[CALIBRATION RULE invoked: before writing, verify at least two distinct confidence
  levels appear across Stages 1-4. Revise now if uniform.]
[FALSIFICATION RULE invoked: brief must declare Supported / Refuted / Indeterminate
  and name the finding that determined it.]
[ATTRIBUTION RULE invoked: every finding names its source stage.]
[SEQUENCING RULE invoked: brief records that hypothesis was declared post-evidence —
  the sequencing choice is a named governance rule, auditable by any reader who can
  cite SEQUENCING RULE by identifier.]

Write the evidence brief:

**Evidence Brief: {{topic}}**
**Investigation date**: {{date}}

**Sequencing** [SEQUENCING RULE]: Evidence-first — hypothesis declared post-evidence
(Stage 3 follows Stages 1-2). A hypothesis anchored before evidence gathering is a
bias, not a hypothesis. Falsification decisions below are grounded in what Stages 1
and 2 actually found.

**Hypothesis** (declared post-evidence, Stage 3): [claim]
**Falsification status** [FALSIFICATION RULE]: [Supported / Refuted / Indeterminate]
**Basis**: [Stage N — specific finding that determined this outcome]

**Key findings** [ATTRIBUTION RULE — every finding names its source stage]:
1. [finding] — Stage [N] — Confidence: [High / Medium / Low] — [one-clause rationale]
2. [finding] — Stage [N] — Confidence: [High / Medium / Low] — [one-clause rationale]
3. [finding] — Stage [N] — Confidence: [High / Medium / Low] — [one-clause rationale]
4. [finding] — Stage [N] — Confidence: [High / Medium / Low] — [one-clause rationale]
5. [finding] — Stage [N] — Confidence: [High / Medium / Low] — [one-clause rationale]

[CALIBRATION RULE invoked: two distinct confidence levels present above?]

**Consensus** (Stage 1 vs Stage 2): [where web and internal sources agreed]
**Divergence** (Stage 1 vs Stage 2): [where they disagreed — and why it matters]

**Counter-evidence**: [finding most challenging to the hypothesis, with stage cite]

**Open gaps**: [what the campaign did not resolve]

**Decision readiness**: [one sentence — "Ready to proceed" or "Needs more investigation
on [specific named gap] before committing."]

Write to: simulations/prove/investigations/{{topic}}-synthesis-{{date}}.md
```

**Rubric targeting**: C-01 (five stages, evidence-first), C-02 (per-finding confidence),
C-03 (FALSIFICATION RULE + status + basis), C-04 (titled, dated, self-contained), C-05
(ATTRIBUTION RULE per finding), C-06 (consensus/divergence), C-07 (CALIBRATION RULE
anti-uniformity), C-08 (open gaps), C-09 (decision readiness), C-10 (structural evidence-
first), C-11 (CALIBRATION RULE as named anti-uniformity guard), C-12 (one-sentence
directive), C-13 (four named rules at preamble, invoked by name at point of use), C-14
(reordering rationale at Stage 3 and synthesis), C-15 (SEQUENCING RULE in the preamble
rule block — same tier as the other three governance rules — cited by identifier at
Stages 1, 2, 3, 5), C-16 (coverage map pre-declares invocations; ATTRIBUTION at Stages
1, 2, 5; CALIBRATION at Stages 4, 5; FALSIFICATION at Stages 3, 5; SEQUENCING at Stages
1, 2, 3, 5 — every cell in the map fulfilled in the stage prompts).
**Risk**: The coverage map and stage invocations are fully aligned here — but both still
depend on the model reading and executing faithfully. No retrospective audit table (V-03
mechanism) checks for gaps after the fact. The combination is preventive only. If a model
skips a stage invocation, there is no self-correction loop.

---

## V-05 — Full Stack: C-15 + C-16 + Evidence-First + Reordering Rationale + Inertia + Audit Trail

**Combined axes**: C-15 (SEQUENCING as named rule) + C-16 (coverage matrix + audit trail)
+ Role sequence (evidence-first) + Hypothesis reordering rationale (C-14) + Inertia
framing + Post-brief retrospective audit

**Hypothesis**: The full-stack combination targets all 16 criteria simultaneously. C-15
and C-16 are addressed by both preventive (coverage matrix) and retrospective (audit
trail) mechanisms — the map commits the model before execution, the table verifies after.
Evidence-first ordering provides structural enforcement of C-10 and gives SEQUENCING RULE
actual stages to govern. C-14 reordering rationale is encoded at Stage 3 and in the
synthesis preamble. Inertia framing provides independent structural depth for C-04
(self-contained brief with before/after frame) and C-08 (gaps named relative to what the
default assumed). The combination is additive: no axis competes with another; each
contributes independently to a distinct criterion or criterion cluster.

```
Run the full evidence campaign for: {{topic}}

Produce a complete, self-contained evidence brief — readable by someone who did not
run the investigation. This campaign uses two structural commitments: evidence-first
sequencing (web search and internal search before hypothesis declaration) and inertia
framing (state the default belief first, then show what the evidence changed).

INERTIA POSITION: [state in 1-2 sentences — what a reasonable team would believe
  about {{topic}} without running this investigation]

The campaign tests, confirms, or displaces the inertia position. Every stage contributes
evidence toward that verdict.

---

CALIBRATION RULE
Confidence ratings must vary. At least two distinct levels (High / Medium / Low) across
all findings. Uniform confidence is a calibration failure. Before finalizing synthesis,
check the confidence column — if every row carries the same level, redistribute.

FALSIFICATION RULE
Every hypothesis carries Supported / Refuted / Indeterminate with a named evidence basis.
A hypothesis without an outcome is a draft, not a finding.

ATTRIBUTION RULE
Every material claim in synthesis names its source stage: "[claim] — Stage [N]."
Websearch claims require URLs; intelligence claims require exact file paths.

SEQUENCING RULE
Web search and internal search complete before hypothesis declaration. A hypothesis
anchored before evidence gathering is a bias, not a hypothesis. This is a declared
governance rule — not an unnamed structural convention. It governs the positions of
Stages 1, 2, and 3 and is auditable by any reader who can cite SEQUENCING RULE by
identifier.

---

RULE COVERAGE MAP

Read before executing Stage 1. At each stage, invoke every rule marked "invoke"
before writing content. After completing Stage 5, fill in the INVOCATION AUDIT TABLE
to confirm coverage. Any blank cell at a required stage is a C-16 violation.

| Rule              | Stage 1 | Stage 2 | Stage 3 | Stage 4 | Stage 5 |
|-------------------|---------|---------|---------|---------|---------|
| CALIBRATION RULE  | —       | —       | —       | invoke  | invoke  |
| FALSIFICATION RULE| —       | —       | invoke  | —       | invoke  |
| ATTRIBUTION RULE  | invoke  | invoke  | —       | —       | invoke  |
| SEQUENCING RULE   | invoke  | invoke  | invoke  | —       | invoke  |

---

Stage 1 — prove-websearch

Search the public web for evidence relevant to {{topic}}.

For each source: URL (required — no training-data claims), verbatim quote,
strength (Weak / Moderate / Strong), bearing (Supports / Refutes / Neutral). Also
note: does this source support or challenge the inertia position?

[SEQUENCING RULE invoked: Stage 1 runs before hypothesis declaration — governed by
  SEQUENCING RULE, not incidental]
[ATTRIBUTION RULE invoked: every source requires a URL; these become Stage 1 citations
  in synthesis]

Write to: simulations/prove/investigations/{{topic}}-websearch-{{date}}.md

---

Stage 2 — prove-intelligence

Search internal sources (repo files, design docs, scenarios, prior signals).

For each source: exact file path, relevant excerpt, strength, bearing. Also note:
does this source confirm or challenge the inertia position?

[SEQUENCING RULE invoked: Stage 2 runs before hypothesis declaration by SEQUENCING RULE]
[ATTRIBUTION RULE invoked: exact file paths required — these become Stage 2 citations]

Write to: simulations/prove/investigations/{{topic}}-intelligence-{{date}}.md

---

Stage 3 — prove-hypothesis [POST-EVIDENCE]

[SEQUENCING RULE invoked: this stage runs third because a hypothesis anchored before
  evidence gathering is a bias, not a hypothesis. The claim below must reflect what
  Stages 1 and 2 support you believing. This ordering is governed by SEQUENCING RULE —
  a declared governance commitment, not an incidental structural choice.]
[FALSIFICATION RULE invoked: falsification condition must be specific enough that
  evidence could satisfy or deny it]

Claim: [one sentence — what the evidence from Stages 1-2 supports you believing;
  state how this relates to the inertia position: accepts, refines, or challenges it]
Falsification condition: [what would disprove this — cite Stage 1-2 findings that
  shaped this choice]
Confidence: [High / Medium / Low] — [cite specific Stage 1-2 findings]
Experiments: [2-3 further tests]

Write to: simulations/prove/investigations/{{topic}}-hypothesis-{{date}}.md

---

Stage 4 — prove-analysis

Analyze patterns across Stages 1-3 evidence.

For each pattern: source, pattern observed, causal or correlational (mechanism required
for causal), confidence (High / Medium / Low — reason). Also identify: does this pattern
confirm or challenge the inertia position?

[CALIBRATION RULE invoked: per-pattern confidence ratings start here — at least two
  distinct levels must appear by synthesis; if all patterns carry the same level,
  redistribute now]

Write to: simulations/prove/investigations/{{topic}}-analysis-{{date}}.md

---

Stage 5 — prove-synthesize

[CALIBRATION RULE invoked: before writing, verify at least two distinct confidence
  levels across Stages 1-4. Revise now if uniform.]
[FALSIFICATION RULE invoked: brief must declare Supported / Refuted / Indeterminate
  and name the specific finding that determined it.]
[ATTRIBUTION RULE invoked: every finding in the brief names its source stage.]
[SEQUENCING RULE invoked: brief records that hypothesis was declared post-evidence
  and states the governing principle — auditable design, not incidental ordering.]

Write the evidence brief:

**Evidence Brief: {{topic}}**
**Investigation date**: {{date}}

**Inertia position** (pre-investigation default): [from intro — what a team would
  have concluded about {{topic}} without this campaign]

**Sequencing** [SEQUENCING RULE]: Evidence-first — hypothesis declared post-evidence
(Stage 3 follows Stages 1-2). A hypothesis anchored before evidence gathering is a
bias, not a hypothesis. Falsification decisions below are grounded in what Stages 1
and 2 actually found.

**Hypothesis** (declared post-evidence, Stage 3): [claim — how it relates to the
  inertia position]
**Falsification status** [FALSIFICATION RULE]: [Supported / Refuted / Indeterminate]
**Basis**: [Stage N — specific finding that determined this outcome]

**Key findings** [ATTRIBUTION RULE — every finding names its source stage]:
1. [finding] — Stage [N] — Confidence: [H/M/L] — Inertia: [confirms/challenges] — [rationale]
2. [finding] — Stage [N] — Confidence: [H/M/L] — Inertia: [confirms/challenges] — [rationale]
3. [finding] — Stage [N] — Confidence: [H/M/L] — Inertia: [confirms/challenges] — [rationale]
4. [finding] — Stage [N] — Confidence: [H/M/L] — Inertia: [confirms/challenges] — [rationale]
5. [finding] — Stage [N] — Confidence: [H/M/L] — Inertia: [confirms/challenges] — [rationale]

[CALIBRATION RULE invoked: two distinct confidence levels present above?]

**Consensus** (Stage 1 vs Stage 2): [where web and internal sources agreed]
**Divergence** (Stage 1 vs Stage 2): [where they disagreed — and why it matters]

**Inertia verdict**: Did the campaign confirm, partially displace, or fully challenge
the inertia position? [1-2 sentences naming what shifted and what did not]

**Counter-evidence**: [finding most challenging to the hypothesis, with stage cite]

**Open gaps**: [what the campaign did not resolve — specifically, what the inertia
  position assumed that the evidence left unanswered]

**Decision readiness**: [one sentence — "Ready to proceed" or "Needs more investigation
on [specific named gap] before committing."]

---

After writing the brief, complete the invocation audit. For each cell, write "invoked"
if the rule was explicitly tagged in that stage's output. If a required cell is blank,
go back and add the invocation tag before submitting.

**RULE INVOCATION AUDIT**

| Rule              | Stage 1 | Stage 2 | Stage 3 | Stage 4 | Stage 5 |
|-------------------|---------|---------|---------|---------|---------|
| CALIBRATION RULE  |         |         |         |         |         |
| FALSIFICATION RULE|         |         |         |         |         |
| ATTRIBUTION RULE  |         |         |         |         |         |
| SEQUENCING RULE   |         |         |         |         |         |

Expected (from coverage map): CALIBRATION at 4, 5 | FALSIFICATION at 3, 5 |
ATTRIBUTION at 1, 2, 5 | SEQUENCING at 1, 2, 3, 5. Any deviation requires explanation.

Write brief + audit to: simulations/prove/investigations/{{topic}}-synthesis-{{date}}.md
```

**Rubric targeting**: C-01 (five stages, evidence-first), C-02 (per-finding confidence
with rationale), C-03 (FALSIFICATION RULE + status + basis), C-04 (inertia frame makes
brief legible to outsider without context), C-05 (ATTRIBUTION RULE per finding), C-06
(consensus/divergence), C-07 (CALIBRATION RULE anti-uniformity), C-08 (open gaps defined
relative to inertia assumptions), C-09 (decision readiness), C-10 (structural evidence-
first), C-11 (CALIBRATION RULE as named anti-uniformity guard), C-12 (one-sentence
directive), C-13 (four named rules at preamble, invoked by name at point of use),
C-14 (reordering rationale at Stage 3 header and synthesis preamble — "a hypothesis
anchored before evidence gathering is a bias, not a hypothesis"), C-15 (SEQUENCING RULE
declared in the preamble rule block alongside CALIBRATION, FALSIFICATION, ATTRIBUTION —
same tier, same format, referenceable by identifier at Stages 1, 2, 3, 5), C-16
(coverage map pre-commits to invocation pattern; audit table retrospectively verifies
coverage; dual mechanism makes gap detection both preventive and corrective).
**Risk**: This is the longest variation. The dual enforcement mechanism (coverage map +
audit table) adds two structural blocks. A model may fill the audit table with "invoked"
without having actually invoked the rules in the stage outputs — the audit becomes
performative rather than verification. The four-column findings row (finding, stage,
confidence, inertia, rationale) is denser than prior variations; shallow models may
abbreviate content to fit the format. Inertia framing adds a before/after frame that
upgrades C-04 and C-08 but requires the model to carry the inertia position through
every stage — if it forgets the INERTIA POSITION after Stage 1, the inertia verdict
and per-finding inertia labels will be empty.

---

## Variation Summary

| ID | Axes | Primary New Targets | All Criteria Hit | Key Risk |
|----|------|---------------------|-----------------|----------|
| V-01 | C-15 (SEQUENCING as named rule) | C-15, C-16 | 16/16 | Naming/placement only; no coverage map verification |
| V-02 | C-16 (coverage matrix, hypothesis-first) | C-16 | 11/16 | Misses C-10, C-14, C-15; map enforcement still behavioral |
| V-03 | Output format (audit trail, hypothesis-first) | C-16 (retrospective) | 11/16 | Misses C-10, C-14, C-15; audit may be filled dishonestly |
| V-04 | C-15 + C-16 (named rule + coverage matrix) | C-15, C-16 | 16/16 | Preventive only — no retrospective audit loop |
| V-05 | C-15 + C-16 + evidence-first + rationale + inertia + audit | C-15, C-16 + depth | 16/16 | Longest; audit performative risk; inertia carry-through risk |

**Predicted leaderboard going into quest-score**: V-05 > V-04 > V-01 > V-03 > V-02.

V-05 is the only variation combining preventive (coverage map) and retrospective (audit
table) mechanisms for C-16, plus inertia framing and C-14 triple-encoding. V-04 covers
all 16 criteria with the cleanest structure and no verbose audit overhead — likely the
highest-quality output for models that follow templates faithfully. V-01 covers all 16
criteria through the single C-15 naming/placement axis; it is the minimal change from
R3 V-04 that crosses the C-15 threshold and verifies whether the formal declaration in
the rule block produces behavioral change beyond what R3 V-04 already demonstrated.

V-02 and V-03 are intentional isolates: they test C-16 enforcement mechanisms without
the C-15/C-10/C-14 stack. If V-02 scores close to V-04, the coverage map is doing the
work independent of SEQUENCING RULE. If V-03 scores close to V-05, the retrospective
audit is the mechanically dominant intervention and the preventive map is redundant.
The divergence between V-02/V-03 and V-04/V-05 on C-15 scoring will calibrate whether
C-15 is primarily a naming criterion or whether the named SEQUENCING RULE actually
changes model behavior at governed stages.
