content = """\
---
skill: quest-rubric
skill_target: mock-accept
date: 2026-03-16
version: 2
changelog: >
  v2 adds C-11, C-12, C-13 from R1 scorecard excellence signals.
  Updates aspirational denominator from 2 to 5 in scoring formula.
---

# Scoring Rubric: mock-accept (mock-review Step 2)

**Skill description**: Step 2 of mock-first workflow. Read a mock artifact produced by
`mock-all` or `mock-ns`, apply automatic flagging rules, evaluate non-auto namespaces
through Architect / Strategy / PM roles, produce MOCK-ACCEPTED or REAL-REQUIRED decisions
per namespace, write a review artifact, and write Status fields back in-place to the source
mock artifact.

**Composite score formula**:

```
score = (essential_pass / 5 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 5 * 10)
```

**Golden threshold**: ALL essential criteria pass AND composite score >= 80.

---

## Essential Criteria

> All five must pass. An output that fails any essential criterion is not useful.

---

### C-01 -- Auto-flag rules fire correctly

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

### C-02 -- FORBIDDEN OUTPUTS TRIAD honored

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

### C-03 -- Status written back in-place with CANARY ASSERTION

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

### C-04 -- Review artifact produced with required structure

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

### C-05 -- MOCK-ACCEPTED requires positive argument (reason codes + two structural slots)

| Field | Value |
|-------|-------|
| ID | C-05 |
| Weight | essential |
| Category | correctness |

**Text**: Every MOCK-ACCEPTED decision block includes: (a) at least one reason code from the
exact enumeration (STRUCTURAL-COVERAGE-SUFFICIENT | DOMAIN-KNOWLEDGE-CONSISTENT) -- no
paraphrase or invented codes; (b) Structural position (Slot 1) naming the specific Tier N
decision this namespace supports -- a generic adequacy statement is a SLOT-VIOLATION; (c)
Contrast (Slot 2) naming a contrasting namespace type and the structural factor distinguishing
it -- a confirmatory sentence without a named contrasting type is CONTRAST-INCOMPLETE.

**Pass condition**: Each MOCK-ACCEPTED block has all three elements. Reason codes match
enumeration exactly. Slot 1 names a decision (not "adequate for planning"). Slot 2 names
a contrasting namespace (e.g., "Unlike prove-interview, which carries...").

**Fail examples**: reason-code = "coverage is fine"; Slot 1 = "supports current planning needs"
(no named decision); Slot 2 absent; two slots merged into one block (RATIONALE-INCOMPLETE).

---

## Recommended Criteria

> Output is better with these. Failure here does not disqualify the output but lowers score.

---

### C-06 -- Entity-naming grammar in role evaluations

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

### C-07 -- Step sequencing and guard compliance explicit

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

### C-08 -- Evaluation-driven REAL-REQUIRED template complete

| Field | Value |
|-------|-------|
| ID | C-08 |
| Weight | recommended |
| Category | format |

**Text**: Every REAL-REQUIRED decision driven by role evaluation (not auto-flagged) uses
the full evaluation-driven template: trigger field (STRATEGY-INADEQUATE | ARCH-IMPLAUSIBLE |
PM-INCOMPLETE), Failing evaluation (role name), Failing verdict (full verdict string),
SQ answer driving verdict (present-tense, artifact as grammatical subject -- not role as
subject), and Artifact state (present-tense, artifact as subject, propagated to next-steps).

**Pass condition**: All five template fields present for each evaluation-driven REAL-REQUIRED
block. No VERDICT-ECHO violations (role as subject in SQ answer field). Artifact state
matches the corresponding next-steps entry.

**Fail examples**: trigger field absent; SQ answer = "The Architect found no gate"
(VERDICT-ECHO -- role as subject); Artifact state missing; next-steps entry does not
match artifact state from the decision block.

---

## Aspirational Criteria

> Raise the bar once essential and recommended criteria are stable.

---

### C-09 -- Cross-namespace risk statement names specific decision with urgency grouping

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

**Fail examples**: "Highest-risk gap: trace -- important for implementation"; urgency
absent; grouping commentary absent when five namespaces are flagged REAL-REQUIRED.

---

### C-10 -- Tier sourcing explicit and consistent throughout

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

### C-11 -- Named guard-bypass error codes on each role-transition gate

| Field | Value |
|-------|-------|
| ID | C-11 |
| Weight | aspirational |
| Category | behavior |
| Source | R1 scorecard: V-02 full pass vs V-04 partial on C-07 |

**Text**: When recording the blocked-list output after each role evaluation, the step names
a specific error code for the violation case rather than using soft language ("set aside").
Each role-transition gate has its own named error: ARCH-GUARD-BYPASS (namespace enters
Strategy when Architecture verdict is not CONSISTENT), STRATEGY-TO-PM-GUARD-BYPASS
(namespace enters PM when Strategy verdict is not ADEQUATE), and GUARD-BYPASS CONTAMINATION
(any downstream role evaluates a namespace whose upstream role issued a blocking verdict).

**Pass condition**: Each of the three inter-role guard gates names its specific bypass
error code in the blocked-list recording section. Soft "set aside" or "does not proceed"
phrasing without a named error code is a partial pass only.

**Fail examples**: "These namespaces are set aside and will not be evaluated by Strategy"
(no named error code); GUARD-BYPASS CONTAMINATION not named anywhere; only one of three
gate error codes present.

**Why this matters**: V-04 received PARTIAL on C-07 because soft framing reduced enforcement
signal at step-transition guards. V-02's named error codes make the constraint checkable
rather than interpretive.

---

### C-12 -- Contrast slot (Slot 2) ordered before structural position (Slot 1) in MOCK-ACCEPTED blocks

| Field | Value |
|-------|-------|
| ID | C-12 |
| Weight | aspirational |
| Category | correctness |
| Source | R1 scorecard: V-01 "SLOT 2 placed before SLOT 1 -- strongest CONTRAST-INCOMPLETE prevention" |

**Text**: In each MOCK-ACCEPTED decision block, the Contrast entry (Slot 2) appears as
the first named slot, before the Structural position entry (Slot 1). This ordering
prevents the most common MOCK-ACCEPTED failure: writing a plausible Slot 1 and then
omitting Slot 2 because the block already reads complete.

**Pass condition**: In every MOCK-ACCEPTED block, the line or label for Slot 2 (Contrast)
precedes the line or label for Slot 1 (Structural position). Both slots are structurally
separate (not merged into a single paragraph).

**Fail examples**: Slot 1 written first, Slot 2 omitted (CONTRAST-INCOMPLETE); Slot 1
written first with Slot 2 as a trailing clause inside the same sentence (RATIONALE-INCOMPLETE);
slots in canonical 1-then-2 order with no structural defense against Slot 2 omission.

**Why this matters**: C-05 requires both slots to be present. C-12 adds the ordering
constraint V-01 demonstrated as the strongest enforcement mechanism: Slot 2 first means
it cannot be dropped by omission after Slot 1 reads sufficient.

---

### C-13 -- Auto-rule contamination enforced through output structure (SKIP cells)

| Field | Value |
|-------|-------|
| ID | C-13 |
| Weight | aspirational |
| Category | behavior |
| Source | R1 scorecard: V-03 "SKIP cells prevent downstream contamination structurally" |

**Text**: When the output format is table-first, auto-flagged namespaces receive explicit
SKIP values in the Arch, Strategy, and PM columns of the evaluation table. The label
AUTO-RULE CONTAMINATION is referenced in the table header or column rules so that any
non-SKIP cell in an auto-flagged row constitutes a visible, checkable violation. SKIP
must appear in all three role columns simultaneously -- partial SKIP (e.g., only Arch = SKIP)
is itself an AUTO-RULE CONTAMINATION error.

**Pass condition**: Auto-flagged namespaces have Arch = SKIP, Strategy = SKIP, and PM = SKIP
in the evaluation table. Column rules or table header reference AUTO-RULE CONTAMINATION as
the reason. A non-SKIP value in any role column for an auto-flagged row is a structural
violation detectable by inspection. (N/A for prose-only output formats.)

**Fail examples**: Auto-flagged namespace has Arch = SKIP but Strategy and PM columns blank
(ambiguous, not explicit SKIP); AUTO-RULE CONTAMINATION not named in table rules; SKIP
applied to only one role column for an auto-flagged namespace.

**Why this matters**: V-03's table-first format made contamination violations immediately
visible without requiring prose enforcement language -- a zero-extra-cost structural check.
Prose-only outputs rely on DO-NOT gates (C-01/C-02); table outputs have a stronger,
structurally self-evident invariant available.

---

## Scoring Reference

| Tier | Criteria | Count | Weight |
|------|----------|-------|--------|
| Essential | C-01, C-02, C-03, C-04, C-05 | 5 | 60 pts |
| Recommended | C-06, C-07, C-08 | 3 | 30 pts |
| Aspirational | C-09, C-10, C-11, C-12, C-13 | 5 | 10 pts |

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
| RATIONALE-INCOMPLETE | MOCK-ACCEPTED Slot 1 and Slot 2 merged into one block | C-05 |
| SLOT-ORDER-INVERSION | MOCK-ACCEPTED Slot 1 written before Slot 2 (Contrast omission risk) | C-12 |
| AUTO-RULE CONTAMINATION | Role evaluation applied to auto-flagged namespace | C-01, C-02, C-13 |
| GUARD-BYPASS CONTAMINATION | Blocked namespace evaluated by downstream role | C-07, C-11 |
| ARCH-GUARD-BYPASS | Namespace enters Strategy without Arch CONSISTENT verdict | C-11 |
| STRATEGY-TO-PM-GUARD-BYPASS | Namespace enters PM without Strategy ADEQUATE verdict | C-11 |
| TRIAD-INCOMPLETE | FORBIDDEN OUTPUTS only 2 of 3 labels acknowledged | C-02 |
"""

with open("C:/src/sim/simulations/quest/rubrics/mock-accept-rubric-v2-2026-03-16.md", "w", encoding="utf-8") as f:
    f.write(content)
print("Written.")
