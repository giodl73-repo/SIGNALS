---
skill: quest-rubric
skill_target: mock-accept
date: 2026-03-16
version: 1
---

# Scoring Rubric: mock-accept (mock-review Step 2)

**Skill description**: Step 2 of mock-first workflow. Read a mock artifact produced by
`mock-all` or `mock-ns`, apply automatic flagging rules, evaluate non-auto namespaces
through Architect / Strategy / PM roles, produce MOCK-ACCEPTED or REAL-REQUIRED decisions
per namespace, write a review artifact, and write Status fields back in-place to the source
mock artifact.

**Composite score formula**:

```
score = (essential_pass / 5 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 2 * 10)
```

**Golden threshold**: ALL essential criteria pass AND composite score >= 80.

---

## Essential Criteria

> All five must pass. An output that fails any essential criterion is not useful.

---

### C-01 — Auto-flag rules fire correctly

| Field | Value |
|-------|-------|
| ID | C-01 |
| Weight | essential |
| Category | correctness |

**Text**: Every EVIDENCE-HEAVY namespace receives REAL-REQUIRED with trigger = EVIDENCE-HEAVY.
At Tier 2+, every namespace in {trace-*, scout-feasibility, listen-*, scout-competitors}
receives REAL-REQUIRED with trigger = TIER-CRITICAL. When compliance tags are present,
scout-compliance and trace-permissions receive REAL-REQUIRED with trigger = COMPLIANCE.
No auto-flagged namespace is passed to role evaluation.

**Pass condition**: All three auto-flag rules fire for qualifying namespaces; auto-flagged
namespaces are absent from role evaluation sections; trigger labels on auto-flagged blocks
match the enumerated values (EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE).

**Fail examples**: prove and listen marked MOCK-ACCEPTED; trace-* passed to Architect
evaluation at Tier 2; trigger = "evidence-only" (paraphrase, not enumerated label).

---

### C-02 — FORBIDDEN OUTPUTS TRIAD honored

| Field | Value |
|-------|-------|
| ID | C-02 |
| Weight | essential |
| Category | correctness |

**Text**: Zero MOCK-ACCEPTED decisions appear for any namespace that qualified for
EVIDENCE-HEAVY, TIER-CRITICAL, or COMPLIANCE auto-flagging. This constraint is
unconditional: high structural quality in the mock, positive role verdicts, or user
override framing does not lift it.

**Pass condition**: Count of MOCK-ACCEPTED decisions on auto-flagged namespaces = 0.
The three triad labels (EVIDENCE-HEAVY, TIER-CRITICAL, COMPLIANCE) are all present
in the output as acknowledged constraints, not silently omitted.

**Fail examples**: listen marked MOCK-ACCEPTED because "structure looks complete";
scout-feasibility accepted at Tier 2 because "only planning stage"; FORBIDDEN OUTPUTS
triad mentioned for only 2 of 3 labels.

---

### C-03 — Status written back in-place with CANARY ASSERTION

| Field | Value |
|-------|-------|
| ID | C-03 |
| Weight | essential |
| Category | behavior |

**Text**: Step 8 (non-skippable) edits the source mock artifact file using the Edit tool.
Each namespace Status field transitions from `Status: MOCK (awaiting review)` to either
`Status: MOCK-ACCEPTED [...]` or `Status: REAL-REQUIRED [...]`. After all edits, the
CANARY ASSERTION is emitted confirming zero Status fields remain as "MOCK (awaiting review)".

**Pass condition**: Edit tool invocation on the source mock artifact path is present.
CANARY ASSERTION appears verbatim: "Count: 0 Status fields remain as MOCK (awaiting review).
Confirmed." (or CANARY SUPPRESSED with count if not all fields were updated). No Status
field in the source artifact retains the generation-time value.

**Fail examples**: Step 8 omitted entirely; review artifact written but source artifact
not edited; CANARY ASSERTION present but some Status fields unchanged (CANARY-FALSE-POSITIVE).

---

### C-04 — Review artifact produced with required structure

| Field | Value |
|-------|-------|
| ID | C-04 |
| Weight | essential |
| Category | format |

**Text**: A review artifact is written to `simulations/mock/{topic}-review-{date}.md`
containing: (1) a Coverage Review table with columns Namespace | Category | Decision | trigger,
one row per namespace; (2) a next-steps list, priority-ordered (critical REAL-REQUIRED first,
evaluation-driven REAL-REQUIRED second, evidence-heavy / compliance last); (3) a cross-namespace
risk statement naming the highest-risk gap.

**Pass condition**: File written at correct path. Table present with all four columns and one
row per namespace reviewed. Next-steps list present with explicit priority labeling. Risk
statement present.

**Fail examples**: Review written as prose paragraphs without table; table has three columns
(Decision missing); next-steps are unordered; risk statement absent; file written to wrong path.

---

### C-05 — MOCK-ACCEPTED requires positive argument (reason codes + two structural slots)

| Field | Value |
|-------|-------|
| ID | C-05 |
| Weight | essential |
| Category | correctness |

**Text**: Every MOCK-ACCEPTED decision block includes: (a) at least one reason code from the
exact enumeration (STRUCTURAL-COVERAGE-SUFFICIENT | DOMAIN-KNOWLEDGE-CONSISTENT) — no
paraphrase or invented codes; (b) Structural position (Slot 1) naming the specific Tier N
decision this namespace supports — a generic adequacy statement is a SLOT-VIOLATION; (c)
Contrast (Slot 2) naming a contrasting namespace type and the structural factor distinguishing
it — a confirmatory sentence without a named contrasting type is CONTRAST-INCOMPLETE.

**Pass condition**: Each MOCK-ACCEPTED block has all three elements. Reason codes match
enumeration exactly. Slot 1 names a decision (not "adequate for planning"). Slot 2 names
a contrasting namespace (e.g., "Unlike prove-interview, which carries...").

**Fail examples**: reason-code = "coverage is fine"; Slot 1 = "supports current planning needs"
(no named decision); Slot 2 absent; two slots merged into one block (RATIONALE-INCOMPLETE).

---

## Recommended Criteria

> Output is better with these. Failure here does not disqualify the output but lowers score.

---

### C-06 — Entity-naming grammar in role evaluations

| Field | Value |
|-------|-------|
| ID | C-06 |
| Weight | recommended |
| Category | depth |

**Text**: For each non-auto-flagged namespace, Architect sub-questions name a specific
system component, dependency, or interface (not "the structure looks fine"). Strategy
sub-questions name the specific Tier N decision the namespace supports and state whether
the belief formed would be correct or incorrect. PM sub-questions name required sections
and the specific enforcement gate, decision table, or required output structure present.

**Pass condition**: At least 2 of 3 role sub-questions per namespace answer with a named
artifact element, system component, or decision name. Generic yes/no answers or
"structure is present" forms are absent.

**Fail examples**: Architect SQ-1 = "The mock confirms plausibility"; Strategy SQ-2 =
"The team would form a correct belief"; PM SQ-2 = "Yes, enforcement gate is present".

---

### C-07 — Step sequencing and guard compliance explicit

| Field | Value |
|-------|-------|
| ID | C-07 |
| Weight | recommended |
| Category | behavior |

**Text**: The two-list partition from Step 2 is written explicitly before role evaluation
begins (auto-flagged list + remaining list). The Arch-blocked list is recorded after Step 3
before Step 4 proceeds. The Strategy-blocked list is recorded after Step 4 before Step 5
proceeds. No namespace on a blocked list appears in subsequent evaluation steps.

**Pass condition**: Two-list partition present as explicit output. Arch-blocked list present
(may be empty, but must be stated). Strategy-blocked list present (may be empty). No
namespace appearing in both a blocked list and a downstream evaluation section.

**Fail examples**: Role evaluation begins without two-list partition; Arch-blocked list
omitted entirely; a CONTRADICTS-ARCHITECTURE namespace reappears in Strategy evaluation.

---

### C-08 — Evaluation-driven REAL-REQUIRED template complete

| Field | Value |
|-------|-------|
| ID | C-08 |
| Weight | recommended |
| Category | format |

**Text**: Every REAL-REQUIRED decision driven by role evaluation (not auto-flagged) uses
the full evaluation-driven template: trigger field (STRATEGY-INADEQUATE | ARCH-IMPLAUSIBLE |
PM-INCOMPLETE), Failing evaluation (role name), Failing verdict (full verdict string),
SQ answer driving verdict (present-tense, artifact as grammatical subject — not role as
subject), and Artifact state (present-tense, artifact as subject, propagated to next-steps).

**Pass condition**: All five template fields present for each evaluation-driven REAL-REQUIRED
block. No VERDICT-ECHO violations (role as subject in SQ answer field). Artifact state
matches the corresponding next-steps entry.

**Fail examples**: trigger field absent; SQ answer = "The Architect found no gate"
(VERDICT-ECHO — role as subject); Artifact state missing; next-steps entry does not
match artifact state from the decision block.

---

## Aspirational Criteria

> Raise the bar once essential and recommended criteria are stable.

---

### C-09 — Cross-namespace risk statement names specific decision with urgency grouping

| Field | Value |
|-------|-------|
| ID | C-09 |
| Weight | aspirational |
| Category | depth |

**Text**: The cross-namespace risk statement names the single highest-risk gap with the
specific Tier N decision at risk (not generic risk language), assigns one of the three
valid urgency labels (BLOCKING | HIGH | MEDIUM), and provides urgency grouping commentary
for each priority group when more than one REAL-REQUIRED namespace exists.

**Pass condition**: Risk statement names a specific decision (e.g., "build feasibility
gate for Tier 2 go/no-go" not "significant risk to the project"). Urgency = one of three
enumerated values. Urgency grouping commentary present for multi-namespace outputs.

**Fail examples**: "Highest-risk gap: trace — important for implementation"; urgency
absent; grouping commentary absent when five namespaces are flagged REAL-REQUIRED.

---

### C-10 — Tier sourcing explicit and consistent throughout

| Field | Value |
|-------|-------|
| ID | C-10 |
| Weight | aspirational |
| Category | correctness |

**Text**: The tier value used in auto-flagging and role evaluation is stated at the
beginning of Step 1 output in the form "Tier: N (source: TOPICS.md | --tier | default)".
All tier-sensitive decisions in Steps 2-5 are consistent with the stated tier. If tier
is derived from TOPICS.md, the topic entry is cited.

**Pass condition**: Tier sourcing statement present with source attribution. All
TIER-CRITICAL auto-flag decisions match the stated tier (e.g., no TIER-CRITICAL
firing at Tier 1, no TIER-CRITICAL suppressed at Tier 2).

**Fail examples**: Tier used in decisions but never stated as a sourced value; tier 2
used for auto-flagging but TOPICS.md shows tier 1 with no --tier override; tier stated
but source not attributed.

---

## Scoring Reference

| Tier | Criteria | Count | Weight |
|------|----------|-------|--------|
| Essential | C-01, C-02, C-03, C-04, C-05 | 5 | 60 pts |
| Recommended | C-06, C-07, C-08 | 3 | 30 pts |
| Aspirational | C-09, C-10 | 2 | 10 pts |

**Golden**: All 5 essential pass + composite >= 80.
**Passing**: All 5 essential pass + composite >= 60.
**Failing**: Any essential criterion fails (regardless of composite).

---

## Known Failure Patterns to Watch

These are the most likely failure modes based on the skill's complexity:

| Code | Pattern | Affected criterion |
|------|---------|-------------------|
| CANARY-FALSE-POSITIVE | Step 8 runs but Status fields not fully updated | C-03 |
| VERDICT-ECHO | Role name as subject in SQ answer ("Architect found...") | C-08 |
| SLOT-VIOLATION | MOCK-ACCEPTED Slot 1 lacks named tier decision | C-05 |
| CONTRAST-INCOMPLETE | MOCK-ACCEPTED Slot 2 absent or no contrasting namespace named | C-05 |
| AUTO-RULE CONTAMINATION | Role evaluation applied to EVIDENCE-HEAVY namespace | C-01, C-02 |
| GUARD-BYPASS CONTAMINATION | CONTRADICTS-ARCHITECTURE namespace evaluated by Strategy | C-07 |
| TRIAD-INCOMPLETE | FORBIDDEN OUTPUTS only 2 of 3 labels acknowledged | C-02 |
