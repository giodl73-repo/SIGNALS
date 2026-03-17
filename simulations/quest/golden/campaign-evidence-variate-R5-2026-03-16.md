---
skill: quest-variate
skill_target: campaign-evidence
round: 5
date: 2026-03-16
rubric: simulations/quest/rubrics/campaign-evidence-rubric-v5-2026-03-16.md
---

# Variations — campaign-evidence / Round 5

Five complete, runnable skill body variations. Single-axis first (V-01, V-02, V-03),
then combined (V-04, V-05).

R5 rubric adds C-17 and C-18. C-17 requires the rule-to-stage coverage map to be
declared *prospectively* — before any evidence stage runs — as a pre-committed contract,
not assembled after execution. C-18 requires all governance rules to occupy *peer tier*
in the preamble — no rule elevated above others via meta-commentary about its own
governance status.

The critical finding going into R5: R4 V-04's SEQUENCING RULE body contains
"This is a declared governance rule — not an unnamed structural convention. Cite it
by identifier at each stage whose position it governs." — meta-commentary absent from
CALIBRATION, FALSIFICATION, and ATTRIBUTION. Under the C-18 test (remove all rule
labels — if resulting prose treats any rule's content differently, parity is absent),
V-04 fails C-18. SEQUENCING RULE is visually present at peer tier, but its prose
is asymmetric.

V-04 R4 had a coverage map before Stage 1, making it prospective — C-17 should pass
via placement. C-17 tests whether explicit "pre-execution commitment" language adds
structural value beyond placement.

---

## V-01 — Axis: C-18 (rule parity via prose-level uniformity)

**Hypothesis**: The minimal change that crosses C-18 is stripping the SEQUENCING RULE
meta-commentary — replacing "This is a declared governance rule — not an unnamed
structural convention. Cite it by identifier at each stage whose position it governs."
with prose that matches the behavioral register of the other three rules. The C-18
test is prose-level: after removing all rule labels, no block should distinguish itself
by making claims about its own governance status. Parity is achieved by what the rule
*says* (a behavioral demand), not by whether it appears visually alongside the others.

Coverage map remains unchanged from R4 V-04 — placed before Stage 1, cells verifiable
against stage output. C-17 passes via placement.

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
anchored before evidence gathering is a bias, not a hypothesis. Invoke by identifier
at each stage this rule governs.

---

RULE COVERAGE MAP

Read before executing Stage 1. At each stage, invoke every rule marked "invoke" before
writing content. A stage that omits a required invocation is a coverage gap.

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
strength (Weak / Moderate / Strong), bearing (Supports / Refutes / Neutral).

[SEQUENCING RULE invoked: Stage 1 runs before hypothesis declaration]
[ATTRIBUTION RULE invoked: every source requires a URL]

Write to: simulations/prove/investigations/{{topic}}-websearch-{{date}}.md

---

Stage 2 — prove-intelligence

Search internal sources (repo files, design docs, scenarios, prior signals).

For each source: exact file path, relevant excerpt, strength, bearing.

[SEQUENCING RULE invoked: Stage 2 runs before hypothesis declaration]
[ATTRIBUTION RULE invoked: exact file paths required]

Write to: simulations/prove/investigations/{{topic}}-intelligence-{{date}}.md

---

Stage 3 — prove-hypothesis [POST-EVIDENCE]

[SEQUENCING RULE invoked: Stage 3 follows Stages 1-2 — claim must reflect what the
  evidence supports, not a prior intuition]
[FALSIFICATION RULE invoked: falsification condition must be specific enough that
  evidence could satisfy or deny it]

Claim: [one sentence — what Stages 1-2 support you believing]
Falsification condition: [what would disprove this — cite Stage 1-2 findings]
Confidence: [High / Medium / Low] — [cite specific Stage 1-2 findings]
Experiments: [2-3 further tests]

Write to: simulations/prove/investigations/{{topic}}-hypothesis-{{date}}.md

---

Stage 4 — prove-analysis

Analyze patterns across Stages 1-3 evidence.

For each pattern: source, pattern observed, causal or correlational (mechanism required
for causal), confidence (High / Medium / Low — reason).

[CALIBRATION RULE invoked: at least two distinct confidence levels must appear by
  synthesis — redistribute now if all patterns carry the same level]

Write to: simulations/prove/investigations/{{topic}}-analysis-{{date}}.md

---

Stage 5 — prove-synthesize

[CALIBRATION RULE invoked: before writing, verify at least two distinct confidence
  levels across Stages 1-4. Revise now if uniform.]
[FALSIFICATION RULE invoked: brief must declare Supported / Refuted / Indeterminate
  and name the finding that determined it.]
[ATTRIBUTION RULE invoked: every finding names its source stage.]
[SEQUENCING RULE invoked: brief records that hypothesis was declared post-evidence —
  a hypothesis anchored before evidence gathering is a bias, not a hypothesis.]

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

**Rubric targeting**: C-01 through C-16 preserved from R4 V-04. C-17: coverage map
placed before Stage 1 — commitment precedes execution, cells verifiable against stage
output. C-18: SEQUENCING RULE stripped of meta-commentary — all four rules now make
behavioral demands in the same prose register; C-18 parity test (remove labels) passes
because no rule block claims special governance status.
**Single axis**: The only change from R4 V-04 is SEQUENCING RULE's body — last two
sentences replaced with "Invoke by identifier at each stage this rule governs."
**Risk**: C-17 passes via placement, not via explicit temporal commitment language —
a model that reads the map after Stage 1 has already run might still satisfy the
criterion structurally while violating the spirit. C-18 parity is structural here, not
declared; a variant with explicit "all rules at peer tier" language might be more
recoverable when models compress prompts.

---

## V-02 — Axis: C-17 (explicit pre-execution temporal lock)

**Hypothesis**: C-17's requirement that a coverage commitment "precede execution" is
satisfied structurally by placement before Stage 1 (V-01), but explicit temporal lock
language — "This map is finalized before Stage 1 begins and cannot be modified after
any stage executes" — makes the prospective intent unmistakable and algorithmically
checkable. The distinction: placement-before-Stage-1 satisfies C-17 structurally;
explicit lock language satisfies it semantically. This variation tests whether the
semantic declaration changes model behavior or is redundant with placement.

SEQUENCING RULE retains R4 V-04 meta-commentary (intentional — isolates C-17 from
C-18; this variation expects C-18 to fail as a control).

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

PRE-EXECUTION RULE COVERAGE COMMITMENT

This map is finalized before Stage 1 begins. It cannot be modified after any stage
executes. A commitment that precedes execution makes gaps structurally unambiguous —
they are cells declared "invoke" but left empty, not gaps concealed by post-hoc
assembly. A coverage audit populated after all stages complete is not a commitment;
it is a record. This is a commitment.

| Rule              | Stage 1 | Stage 2 | Stage 3 | Stage 4 | Stage 5 |
|-------------------|---------|---------|---------|---------|---------|
| CALIBRATION RULE  | —       | —       | —       | invoke  | invoke  |
| FALSIFICATION RULE| —       | —       | invoke  | —       | invoke  |
| ATTRIBUTION RULE  | invoke  | invoke  | —       | —       | invoke  |
| SEQUENCING RULE   | invoke  | invoke  | invoke  | —       | invoke  |

Read this commitment before executing Stage 1. At each stage, invoke every rule
marked "invoke" before writing content. Any deviation from the declared pattern is
a coverage gap.

---

Stage 1 — prove-websearch

Search the public web for evidence relevant to {{topic}}.

For each source: URL (required — no training-data claims), verbatim quote,
strength (Weak / Moderate / Strong), bearing (Supports / Refutes / Neutral).

[SEQUENCING RULE invoked: Stage 1 runs before hypothesis declaration — governed by
  SEQUENCING RULE, not incidental]
[ATTRIBUTION RULE invoked: every source requires a URL; these become Stage 1 citations]

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

[SEQUENCING RULE invoked: Stage 3 runs third because a hypothesis anchored before
  evidence gathering is a bias, not a hypothesis — this ordering is governed by
  SEQUENCING RULE, declared in the preamble as a first-class rule]
[FALSIFICATION RULE invoked: falsification condition must be specific enough that
  evidence could satisfy it — vague conditions are not falsifiable]

Claim: [one sentence — what Stages 1-2 support you believing]
Falsification condition: [what would disprove this — cite Stage 1-2 findings]
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
  levels across Stages 1-4. Revise now if uniform.]
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

**Rubric targeting**: C-01 through C-16 preserved from R4 V-04. C-17: explicit
"finalized before Stage 1 begins / cannot be modified after any stage executes"
language — temporal commitment is declared, not merely implied by placement.
**Intentional miss**: C-18 — SEQUENCING RULE retains meta-commentary; parity test
(remove labels) fails because SEQUENCING RULE's prose claims governance status that
other rules do not.
**Diagnostic value**: If V-02 scores close to V-01, explicit temporal lock language
does not materially change C-17 compliance — placement is sufficient. If V-02 is
significantly stronger, explicit language is load-bearing for C-17.

---

## V-03 — Axis: C-17 via inline coverage annotations (alternative mechanism)

**Hypothesis**: Stage applicability embedded directly in each rule's annotation
— "CALIBRATION RULE [invoked at: Stage 4, Stage 5]" — satisfies C-17 via a different
mechanism than a separate map block. The commitment is inseparable from the rule
declaration: a reader cannot read CALIBRATION RULE without also reading that it applies
at Stages 4 and 5. This is a stronger form of prospective commitment than a separate
map block (which can be skipped by jumping to Stage 1) because it co-locates the
obligation with the rule that creates it.

Inline annotations also address C-18 structurally: all four rules receive identical
annotation formatting — no rule is elevated by having a map row vs. being embedded
as a prose note.

```
Run the full evidence campaign for: {{topic}}

Produce a complete evidence brief. Evidence-first sequencing: web search and internal
search complete before the hypothesis is declared.

---

CALIBRATION RULE [invoked at: Stage 4, Stage 5]
Confidence ratings must vary. At least two distinct levels (High / Medium / Low) must
appear across all findings. Uniform confidence is a calibration failure. At synthesis,
check the confidence column — if every row carries the same level, recalibrate before
submitting.

FALSIFICATION RULE [invoked at: Stage 3, Stage 5]
Every hypothesis carries Supported / Refuted / Indeterminate with a named evidence basis.
A hypothesis without an outcome is a draft, not a finding. No outcome without a finding
citation.

ATTRIBUTION RULE [invoked at: Stage 1, Stage 2, Stage 5]
Every material claim in synthesis names its source stage: "[claim] — Stage [N]."
Websearch claims require URLs; intelligence claims require exact file paths. A claim
without stage attribution is not acceptable.

SEQUENCING RULE [invoked at: Stage 1, Stage 2, Stage 3, Stage 5]
Web search and internal search complete before hypothesis declaration. A hypothesis
anchored before evidence gathering is a bias, not a hypothesis. Invoke by identifier
at each stage this rule governs.

The stage applicability above is declared before Stage 1 begins. At each stage,
explicitly invoke every rule annotated for that stage before writing content.

---

Stage 1 — prove-websearch

Search the public web for evidence relevant to {{topic}}.

For each source: URL (required — no training-data claims), verbatim quote,
strength (Weak / Moderate / Strong), bearing (Supports / Refutes / Neutral).

[SEQUENCING RULE invoked: Stage 1 runs before hypothesis declaration — governed by
  SEQUENCING RULE, annotated as applicable at this stage]
[ATTRIBUTION RULE invoked: every source requires a URL]

Write to: simulations/prove/investigations/{{topic}}-websearch-{{date}}.md

---

Stage 2 — prove-intelligence

Search internal sources (repo files, design docs, scenarios, prior signals).

For each source: exact file path, relevant excerpt, strength, bearing.

[SEQUENCING RULE invoked: Stage 2 runs before hypothesis declaration — governed by
  SEQUENCING RULE]
[ATTRIBUTION RULE invoked: exact file paths required]

Write to: simulations/prove/investigations/{{topic}}-intelligence-{{date}}.md

---

Stage 3 — prove-hypothesis [POST-EVIDENCE]

[SEQUENCING RULE invoked: Stage 3 follows Stages 1-2 — claim must reflect what the
  evidence supports, not a prior intuition; governed by SEQUENCING RULE]
[FALSIFICATION RULE invoked: falsification condition must be specific enough that
  evidence could satisfy or deny it]

Claim: [one sentence — what Stages 1-2 support you believing]
Falsification condition: [what would disprove this — cite Stage 1-2 findings]
Confidence: [High / Medium / Low] — [cite specific Stage 1-2 findings]
Experiments: [2-3 further tests]

Write to: simulations/prove/investigations/{{topic}}-hypothesis-{{date}}.md

---

Stage 4 — prove-analysis

Analyze patterns across Stages 1-3 evidence.

For each pattern: source, pattern observed, causal or correlational (mechanism required
for causal), confidence (High / Medium / Low — reason).

[CALIBRATION RULE invoked: per-pattern confidence ratings start here — at least two
  distinct levels must appear by synthesis; redistribute now if all patterns carry the
  same level]

Write to: simulations/prove/investigations/{{topic}}-analysis-{{date}}.md

---

Stage 5 — prove-synthesize

[CALIBRATION RULE invoked: before writing, verify at least two distinct confidence
  levels across Stages 1-4. Revise now if uniform.]
[FALSIFICATION RULE invoked: brief must declare Supported / Refuted / Indeterminate
  and name the finding that determined it.]
[ATTRIBUTION RULE invoked: every finding names its source stage.]
[SEQUENCING RULE invoked: brief records that hypothesis was declared post-evidence —
  a hypothesis anchored before evidence gathering is a bias, not a hypothesis.]

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

**Rubric targeting**: C-01 through C-16 from R4 V-04 (evidence-first, all rules in
preamble, per-stage invocations, coverage tracking). C-17: inline annotations declare
stage applicability as part of each rule before Stage 1 — commitment co-located with
the rule that creates the obligation; equivalent structure satisfying "declared at
brief's outset." C-18: all four rules receive identical annotation format "[invoked
at: Stage X, Stage Y]" — prose bodies are behavioral demands without meta-commentary;
parity test passes.
**Diagnostic value**: If V-03 scores with V-01, inline annotations are equivalent to
a separate map for C-17/C-18. If V-03 underperforms V-01, the map's visual separation
from the rule bodies is important for C-16 (zero-gap invocation checking). If V-03
outperforms V-01, co-locating obligation with rule creates stronger model compliance.

---

## V-04 — Combined: C-18 parity (V-01) + C-17 explicit lock (V-02) + full V-04 stack

**Hypothesis**: V-01 passes C-18 via prose uniformity; V-02 passes C-17 via explicit
temporal lock. The combination makes both criteria structurally unambiguous: the
coverage map is declared as a pre-execution commitment (C-17 semantic), and all four
rules make behavioral demands without any rule claiming special governance status
(C-18 prose parity). This is the cleanest full-stack design — no redundant mechanism
(no retrospective audit), no coverage format change (separate map, not inline).

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
anchored before evidence gathering is a bias, not a hypothesis. Invoke by identifier
at each stage this rule governs.

---

PRE-EXECUTION RULE COVERAGE COMMITMENT

This map is declared and finalized before Stage 1 begins. It cannot be modified after
any stage executes. A commitment that precedes execution makes gaps structurally
unambiguous — they are cells declared "invoke" but left empty, not gaps concealed by
post-hoc assembly.

| Rule              | Stage 1 | Stage 2 | Stage 3 | Stage 4 | Stage 5 |
|-------------------|---------|---------|---------|---------|---------|
| CALIBRATION RULE  | —       | —       | —       | invoke  | invoke  |
| FALSIFICATION RULE| —       | —       | invoke  | —       | invoke  |
| ATTRIBUTION RULE  | invoke  | invoke  | —       | —       | invoke  |
| SEQUENCING RULE   | invoke  | invoke  | invoke  | —       | invoke  |

Read this commitment before executing Stage 1. At each stage, invoke every rule
marked "invoke" before writing content.

---

Stage 1 — prove-websearch

Search the public web for evidence relevant to {{topic}}.

For each source: URL (required — no training-data claims), verbatim quote,
strength (Weak / Moderate / Strong), bearing (Supports / Refutes / Neutral).

[SEQUENCING RULE invoked: Stage 1 runs before hypothesis declaration]
[ATTRIBUTION RULE invoked: every source requires a URL]

Write to: simulations/prove/investigations/{{topic}}-websearch-{{date}}.md

---

Stage 2 — prove-intelligence

Search internal sources (repo files, design docs, scenarios, prior signals).

For each source: exact file path, relevant excerpt, strength, bearing.

[SEQUENCING RULE invoked: Stage 2 runs before hypothesis declaration]
[ATTRIBUTION RULE invoked: exact file paths required]

Write to: simulations/prove/investigations/{{topic}}-intelligence-{{date}}.md

---

Stage 3 — prove-hypothesis [POST-EVIDENCE]

[SEQUENCING RULE invoked: Stage 3 follows Stages 1-2 — a hypothesis anchored before
  evidence gathering is a bias, not a hypothesis; this ordering is governed by
  SEQUENCING RULE, declared in the preamble]
[FALSIFICATION RULE invoked: falsification condition must be specific enough that
  evidence could satisfy or deny it]

Claim: [one sentence — what Stages 1-2 support you believing]
Falsification condition: [what would disprove this — cite Stage 1-2 findings]
Confidence: [High / Medium / Low] — [cite specific Stage 1-2 findings]
Experiments: [2-3 further tests]

Write to: simulations/prove/investigations/{{topic}}-hypothesis-{{date}}.md

---

Stage 4 — prove-analysis

Analyze patterns across Stages 1-3 evidence.

For each pattern: source, pattern observed, causal or correlational (mechanism required
for causal), confidence (High / Medium / Low — reason).

[CALIBRATION RULE invoked: per-pattern confidence ratings start here — at least two
  distinct levels must appear by synthesis; redistribute now if all patterns carry the
  same level]

Write to: simulations/prove/investigations/{{topic}}-analysis-{{date}}.md

---

Stage 5 — prove-synthesize

[CALIBRATION RULE invoked: before writing, verify at least two distinct confidence
  levels across Stages 1-4. Revise now if uniform.]
[FALSIFICATION RULE invoked: brief must declare Supported / Refuted / Indeterminate
  and name the finding that determined it.]
[ATTRIBUTION RULE invoked: every finding names its source stage.]
[SEQUENCING RULE invoked: brief records that hypothesis was declared post-evidence —
  a hypothesis anchored before evidence gathering is a bias, not a hypothesis.]

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

**Rubric targeting**: C-01 through C-16 from R4 V-04 (evidence-first, all four rules
in preamble, coverage map, per-stage invocations, C-14 rationale at Stage 3 and
synthesis). C-17: explicit pre-execution lock — "declared and finalized before Stage 1
begins / cannot be modified after any stage executes." C-18: SEQUENCING RULE body is
uniform prose with no meta-commentary; all four rules make behavioral demands in the
same register; parity test (remove labels) passes.
**Risk**: Preventive only — no retrospective audit loop. A model that executes stages
without reading the pre-execution commitment produces the same output as V-01/V-03.
The explicit lock language is a stronger semantic signal but does not make violation
mechanically impossible.

---

## V-05 — Full stack: inline annotations (C-17 + C-18) + dual enforcement + inertia

**Combined axes**: C-17 (inline coverage co-located with rule declarations) + C-18
(uniform annotation format, no meta-commentary) + dual enforcement (prospective
inline commitment + retrospective audit table) + evidence-first (C-10) + reordering
rationale (C-14) + SEQUENCING RULE (C-15) + inertia framing

**Hypothesis**: Inline stage applicability annotations on each rule satisfy C-17 by
making the prospective commitment inseparable from reading the preamble — a model
cannot encounter SEQUENCING RULE without also reading it applies at Stages 1, 2, 3,
and 5. This is a mechanically stronger form of C-17 than a separate map block, which
can be skipped. Combined with the retrospective audit table (from R4 V-05), both the
obligation and its verification are structurally enforced. Inertia framing adds
decision-trajectory depth above the criteria ceiling.

```
Run the full evidence campaign for: {{topic}}

Produce a complete, self-contained evidence brief — readable by someone who did not
run the investigation. This campaign uses two structural commitments: evidence-first
sequencing (web search and internal search before hypothesis declaration) and inertia
framing (state the default belief first, then show what the evidence changed).

INERTIA POSITION: [state in 1-2 sentences — what a reasonable team would believe
  about {{topic}} without running this investigation]

The campaign tests, confirms, or displaces the inertia position. Every stage
contributes evidence toward that verdict.

---

CALIBRATION RULE [invoked at: Stage 4, Stage 5]
Confidence ratings must vary. At least two distinct levels (High / Medium / Low) across
all findings. Uniform confidence is a calibration failure. Before finalizing synthesis,
check the confidence column — if every row carries the same level, redistribute.

FALSIFICATION RULE [invoked at: Stage 3, Stage 5]
Every hypothesis carries Supported / Refuted / Indeterminate with a named evidence
basis. A hypothesis without an outcome is a draft, not a finding.

ATTRIBUTION RULE [invoked at: Stage 1, Stage 2, Stage 5]
Every material claim in synthesis names its source stage: "[claim] — Stage [N]."
Websearch claims require URLs; intelligence claims require exact file paths.

SEQUENCING RULE [invoked at: Stage 1, Stage 2, Stage 3, Stage 5]
Web search and internal search complete before hypothesis declaration. A hypothesis
anchored before evidence gathering is a bias, not a hypothesis. Invoke by identifier
at each stage this rule governs.

The stage applicability above is declared before Stage 1 begins and cannot be modified
retroactively. At each stage, invoke every rule annotated for that stage before writing
content. After Stage 5, complete the RULE INVOCATION AUDIT TABLE to confirm coverage.

---

Stage 1 — prove-websearch

Search the public web for evidence relevant to {{topic}}.

For each source: URL (required — no training-data claims), verbatim quote,
strength (Weak / Moderate / Strong), bearing (Supports / Refutes / Neutral). Also
note: does this source support or challenge the inertia position?

[SEQUENCING RULE invoked: Stage 1 runs before hypothesis declaration — governed by
  SEQUENCING RULE, declared in the preamble as applicable at this stage]
[ATTRIBUTION RULE invoked: every source requires a URL; these become Stage 1 citations]

Write to: simulations/prove/investigations/{{topic}}-websearch-{{date}}.md

---

Stage 2 — prove-intelligence

Search internal sources (repo files, design docs, scenarios, prior signals).

For each source: exact file path, relevant excerpt, strength, bearing. Also note:
does this source confirm or challenge the inertia position?

[SEQUENCING RULE invoked: Stage 2 runs before hypothesis declaration — governed by
  SEQUENCING RULE]
[ATTRIBUTION RULE invoked: exact file paths required — these become Stage 2 citations]

Write to: simulations/prove/investigations/{{topic}}-intelligence-{{date}}.md

---

Stage 3 — prove-hypothesis [POST-EVIDENCE]

[SEQUENCING RULE invoked: Stage 3 follows Stages 1-2 because a hypothesis anchored
  before evidence gathering is a bias, not a hypothesis — governed by SEQUENCING RULE,
  declared in the preamble as applicable at this stage]
[FALSIFICATION RULE invoked: falsification condition must be specific enough that
  evidence could satisfy or deny it]

Claim: [one sentence — what Stages 1-2 support you believing; state how this relates
  to the inertia position: accepts, refines, or challenges it]
Falsification condition: [what would disprove this — cite Stage 1-2 findings]
Confidence: [High / Medium / Low] — [cite specific Stage 1-2 findings]
Experiments: [2-3 further tests]

Write to: simulations/prove/investigations/{{topic}}-hypothesis-{{date}}.md

---

Stage 4 — prove-analysis

Analyze patterns across Stages 1-3 evidence.

For each pattern: source, pattern observed, causal or correlational (mechanism required
for causal), confidence (High / Medium / Low — reason). Also: does this pattern confirm
or challenge the inertia position?

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
[ATTRIBUTION RULE invoked: every finding names its source stage.]
[SEQUENCING RULE invoked: brief records that hypothesis was declared post-evidence —
  a hypothesis anchored before evidence gathering is a bias, not a hypothesis;
  governed by SEQUENCING RULE, declared in the preamble as applicable at this stage]

Write the evidence brief:

**Evidence Brief: {{topic}}**
**Investigation date**: {{date}}

**Inertia position** (pre-investigation default): [what a team would have concluded
  about {{topic}} without this campaign]

**Sequencing** [SEQUENCING RULE]: Evidence-first — hypothesis declared post-evidence
(Stage 3 follows Stages 1-2). A hypothesis anchored before evidence gathering is a
bias, not a hypothesis.

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

Expected (from rule annotations): CALIBRATION at 4, 5 | FALSIFICATION at 3, 5 |
ATTRIBUTION at 1, 2, 5 | SEQUENCING at 1, 2, 3, 5. Any deviation requires explanation.

Write brief + audit to: simulations/prove/investigations/{{topic}}-synthesis-{{date}}.md
```

**Rubric targeting**: C-01 through C-16 preserved from R4 V-05. C-17: inline
annotations co-locate stage applicability with each rule declaration before Stage 1 —
commitment is inseparable from reading the preamble; the explicit "cannot be modified
retroactively" sentence adds semantic lock. C-18: all four rules receive identical
"[invoked at: ...]" annotation format; behavioral bodies are structurally parallel
with no meta-commentary; parity test (remove labels) passes — each block states a
behavioral demand without claiming its own governance status.
**Risk**: Longest variation. Audit table may be filled performatively. Inertia
framing requires carrying the INERTIA POSITION through all five stages — if a model
forgets it after Stage 1, the inertia verdict and per-finding inertia labels will be
hollow. The four-column finding row is denser than prior variations.

---

## Variation Summary

| ID | Axis | New targets | All 18 criteria | Key risk |
|----|------|-------------|-----------------|----------|
| V-01 | C-18 (prose parity — strip SEQUENCING meta-commentary) | C-17 (via placement), C-18 | 18/18 | C-17 via placement only — no explicit lock language |
| V-02 | C-17 (explicit pre-execution temporal lock) | C-17 | 17/18 (C-18 intentional miss) | Isolates C-17; C-18 fails as control |
| V-03 | C-17 via inline annotations (alternative mechanism) | C-17, C-18 | 18/18 | No separate map — C-16 zero-gap must be verified through in-line annotations alone |
| V-04 | C-18 parity + C-17 explicit lock (combined) | C-17, C-18 | 18/18 | Preventive only — no retrospective loop |
| V-05 | Inline annotations + explicit lock + dual enforcement + inertia | C-17, C-18 + depth | 18/18 | Longest; audit performative risk; inertia carry-through |

### Predicted leaderboard

| Rank | Variation | Score | Band | Key differentiator |
|------|-----------|-------|------|--------------------|
| 1 | V-05 | 100 | GOLD | Dual enforcement + inertia depth; C-17 inseparable from rule reading |
| 2 | V-04 | 100 | GOLD | Cleanest full-18 design — C-17 explicit lock + C-18 parity, no audit overhead |
| 3 | V-03 | 100 | GOLD | Inline annotations — elegant C-17/C-18 mechanism, smaller prompt than V-04 |
| 4 | V-01 | 100 | GOLD | Minimal change from R4 V-04 — tests whether prose parity alone crosses C-18 |
| 5 | V-02 | 99  | GOLD | Intentional C-18 miss — control for C-17 isolation |

**Diagnostic value**: If V-01 and V-02 both score 100-class (V-01 on C-18, V-02 near
it), the two new criteria are independently satisfiable. If V-03 scores with V-04, the
inline mechanism is a genuine architectural alternative to the separate map. The key
diagnostic question: does placement before Stage 1 (V-01) satisfy C-17 equivalently
to explicit temporal lock language (V-02/V-04)? The gap between them on C-17 scoring
will calibrate whether C-17 is a structural criterion (placement sufficient) or a
semantic one (declaration required).

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Rule prose parity is not achieved by visual tier alone — SEQUENCING RULE's meta-commentary about its own governance status ('This is a declared governance rule — not an unnamed structural convention') creates asymmetry that fails the C-18 remove-labels test even when all four rules appear at the same structural level; parity requires uniform behavioral register across all rule bodies", "Inline stage applicability annotations co-locate the prospective coverage commitment with the rule declarations themselves, making C-17 inseparable from reading the preamble; this is a structurally stronger form of prospective commitment than a separate map block, which can be skipped without reading"]}
```
