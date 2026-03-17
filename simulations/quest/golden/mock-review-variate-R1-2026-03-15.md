---
skill: quest-variate
skill_target: mock-review
date: 2026-03-15
round: 1
rubric_version: v1
status: VARIATE
---

# mock-review Variate — Round 1

**Date:** 2026-03-15
**Skill:** mock-review
**Rubric:** v1 (C-01 through C-10; essential C-01–C-05)
**Round:** R1 — single-axis pass (V-01 through V-03), then two-axis combinations (V-04, V-05)

---

## Axis-Assignment Plan

Single-axis variations target criteria most at risk from a neutral baseline:
- C-02 (auto-rule correctness) is most likely to fail when rules are interleaved with role
  evaluation — separation of phases is the fix candidate.
- C-04 (status write-back) fails when it is described as a side-effect rather than a
  dedicated phase — lifecycle emphasis is the fix candidate.
- C-07 (PM/Architect/Strategy shown) fails when the output format collapses evaluation
  into a table cell — output format is the fix candidate.

| Plan | Axis | Source signal | Target criteria | Predicted |
|------|------|---------------|-----------------|-----------|
| V-01 | role-sequence | Auto-rules interleaved with role eval → C-02 failures | C-02, C-08 | Improves C-02 pass rate by making auto-flagging a gated phase before any role speaks |
| V-02 | output-format | Table-cell decisions compress evaluation → C-07 failures | C-07, C-10 | Prose-first format forces fuller reasoning per namespace; C-07 pass rate increases |
| V-03 | lifecycle-emphasis | Write-back treated as side-note → C-04 failures | C-04, C-05 | Dedicated numbered phase for write-back with stop gate prevents skip |
| V-04 | role-sequence + phrasing-register | Combine V-01 auto-gate with strict imperative DO NOT language | C-02, C-03, C-04 | DO NOT gates on forbidden decisions (MOCK-ACCEPTED on evidence-heavy) prevent the most common incorrect outputs |
| V-05 | output-format + inertia-framing | Extend decision table with Skip-Cost column; inertia framing in evaluation prompts | C-05, C-09, C-10 | Skip-cost column makes next-steps prioritization defensible and satisfies C-09 coverage gap synthesis |

---

## V-01 — Role Sequence: Auto-Rules Gate Before Role Evaluation

**axis:** role-sequence
**hypothesis:** Running automatic flagging rules as a named, gated phase that completes
before any PM/Architect/Strategy evaluation begins increases C-02 (automatic rule
correctness) pass rate because the three evaluation roles cannot soften or override a
rule that has already fired. Without the gate, a PM evaluation running in parallel with
rule-checking can produce a MOCK-ACCEPTED that technically overwrites an EVIDENCE-HEAVY
flag. The gate makes the auto-rules non-negotiable before human-role judgment starts.
Failure condition: if C-02 pass rate does not improve relative to a baseline that applies
rules inline, the ordering overhead adds no correctness benefit.

---

You are running /mock:review.

**Input**

Topic: {topic}
Mock artifact: {mock-artifact-path}
Tier: {tier — from --tier flag, TOPICS.md, or default 1}

**Setup**

Read the mock artifact at {mock-artifact-path}.
For each namespace section, extract from the MOCK ARTIFACT header block:
  Namespace, Category (HIGH-STRUCTURE | EVIDENCE-HEAVY | MIXED), current Status

Read TOPICS.md:
  Tier for this topic (overridden by --tier if provided)
  Compliance tags (if any)

State the tier at the top of your output:
  Tier used: {N}  (source: TOPICS.md | --tier flag | default)

**Phase 1 — Automatic Flagging**

Apply all three rules to every namespace. Rules are not role-overridable.

RULE A — EVIDENCE-HEAVY (fires at all tiers):
  If Category == EVIDENCE-HEAVY → REAL-REQUIRED
  Trigger label: EVIDENCE-HEAVY

RULE B — TIER-CRITICAL (fires at Tier 2 and Tier 3 only):
  If tier >= 2 AND namespace in {trace-*, scout-feasibility, listen-*, scout-competitors}
  → REAL-REQUIRED
  Trigger label: TIER-CRITICAL

RULE C — COMPLIANCE (fires when compliance context is active):
  If TOPICS.md compliance tags present OR --compliance flag
  AND namespace in {scout-compliance, trace-permissions}
  → REAL-REQUIRED
  Trigger label: COMPLIANCE

After applying all three rules, output two lists before proceeding:

  Auto-flagged (REAL-REQUIRED):
  - {namespace}: trigger = {EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE}

  Remaining (awaiting Phase 2 review):
  - {namespace}: Category = {HIGH-STRUCTURE | MIXED}

Every namespace must appear in exactly one list.
Do not begin Phase 2 until both lists are complete and every namespace is placed.

**Phase 2 — Three-Role Review (non-auto namespaces only)**

For each namespace in the "remaining" list from Phase 1, run three evaluations:

PM — Structural completeness:
  Are required sections present? Are gates present? Are tables well-formed?
  Verdict: Structurally adequate | Structurally incomplete

Architect — Technical plausibility:
  Does the mock content contradict known architectural facts about {topic}?
  Verdict: Plausible | Contradicts known facts

Strategy — Coverage adequacy for Tier {tier}:
  Is this namespace sufficiently covered for decisions at the current tier?
  Verdict: Adequate | Insufficient for Tier {tier}

Record decision:
  If PM = adequate AND Architect = plausible AND Strategy = adequate:
    MOCK-ACCEPTED with at least one reason code from:
      STRUCTURAL-COVERAGE-SUFFICIENT
      DOMAIN-KNOWLEDGE-CONSISTENT
    Use both codes when both conditions hold.
  Otherwise:
    REAL-REQUIRED with the evaluation verdict that drove the decision.

Valid reason codes are exactly as written above. No paraphrase.

**Phase 3 — Write Review Artifact**

Write simulations/mock/{topic}-review-{date}.md:

1. Header: Topic | Tier used | Date
2. Coverage Review table:
   | Namespace | Category | Decision | Trigger / Reason Code |
   (one row per namespace; all namespaces from both Phase 1 lists)
3. Next Steps (numbered, priority order):
   Priority 1 — REAL-REQUIRED critical namespaces: trace, then scout-feasibility, then listen
   Priority 2 — REAL-REQUIRED non-critical namespaces
   Priority 3 — REAL-REQUIRED evidence-heavy namespaces
   Format each entry: /{skill} {topic} — {one-line reason}

**Phase 4 — Write Status Back to Source Artifact (mandatory)**

This is the defining action of /mock:review. It is required.

For every namespace in {mock-artifact-path}, use Edit to replace the Status line in-place:

  Replace: Status: MOCK (awaiting review)
  With:    Status: MOCK-ACCEPTED [STRUCTURAL-COVERAGE-SUFFICIENT | DOMAIN-KNOWLEDGE-CONSISTENT]
  Or:      Status: REAL-REQUIRED [{trigger or evaluation reason}]

Edit the Status line only. Do not rewrite any other content in the source artifact.
This is the only permitted in-place edit in Signal.

Confirm:
  "Annotations updated in: {mock-artifact-path}"
  "Review written: simulations/mock/{topic}-review-{date}.md"

Zero Status fields may remain as MOCK (awaiting review) after Phase 4 completes.

---

## V-02 — Output Format: Prose Evaluation Then Summary Table

**axis:** output-format
**hypothesis:** A prose-first evaluation format — PM/Architect/Strategy as running
narrative paragraphs per namespace before any table — increases C-07 (three-role
evaluation shown) and C-10 (namespace-specific MOCK-ACCEPTED rationale) pass rates
because prose format affords reasoning that a table cell does not. When evaluation
is expressed as a two-word table cell ("Good structure"), the three-role requirement
is technically present but evidentially empty. Prose evaluation forces at least one
substantive sentence per role, which is what C-07 requires.
Failure condition: if C-07 and C-10 scores do not improve relative to a table-primary
format, the prose overhead does not justify the additional length.

---

You are running /mock:review.

**Input**

Topic: {topic}
Mock artifact: {mock-artifact-path}
Tier: {tier — from --tier flag, TOPICS.md, or default 1}

**Setup**

Read {mock-artifact-path}. Parse each namespace's MOCK ARTIFACT header block.
Read TOPICS.md for tier and compliance tags.
State at the top of your output: "Tier: {N} (source: ...)"

**Automatic Rules**

Apply before any review. These fire independently and cannot be overridden by role
evaluation.

1. EVIDENCE-HEAVY at any tier → REAL-REQUIRED (trigger: EVIDENCE-HEAVY)
2. Tier 2+ and namespace in {trace-*, scout-feasibility, listen-*, scout-competitors}
   → REAL-REQUIRED (trigger: TIER-CRITICAL)
3. Compliance tags active and namespace in {scout-compliance, trace-permissions}
   → REAL-REQUIRED (trigger: COMPLIANCE)

**Per-Namespace Review**

For each namespace, write a structured prose entry using this format:

---

### {Namespace}

Category: {HIGH-STRUCTURE | EVIDENCE-HEAVY | MIXED}

[If auto-flagged by any rule above:]
Decision: REAL-REQUIRED
Trigger: {EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE}
[Skip evaluation sections. Proceed to next namespace.]

[If not auto-flagged:]

**PM assessment:** [One to three sentences. Assess structural completeness. Are required
sections present? Are enforcement gates present and well-formed? Are comparison tables
or required output structures present and correctly formed? Name specific sections or
mechanisms that are present or absent.]

**Architect assessment:** [One to three sentences. Assess technical plausibility for
{topic}. Does the mock content contradict known system architecture, known dependencies,
or known constraints of {topic}? Name the specific element that confirms or contradicts
plausibility.]

**Strategy assessment:** [One to three sentences. Assess coverage adequacy for Tier
{tier}. Would a team making a Tier {tier} decision be misled or blocked by accepting
this namespace as MOCK-ACCEPTED rather than running a real skill? Name the specific
decision the team is making at this tier.]

Decision: MOCK-ACCEPTED [STRUCTURAL-COVERAGE-SUFFICIENT | DOMAIN-KNOWLEDGE-CONSISTENT]
       or REAL-REQUIRED [name the evaluation failure]

[For MOCK-ACCEPTED: use STRUCTURAL-COVERAGE-SUFFICIENT when structural completeness drove
the verdict; use DOMAIN-KNOWLEDGE-CONSISTENT when content plausibility drove the verdict;
use both when both apply. Use exact codes only.]

---

After all namespace prose entries, write the consolidated summary:

**Coverage Summary Table**

| Namespace | Category | Decision | Trigger / Reason Code |
|-----------|----------|----------|-----------------------|

**Next Steps**

Number the real skill runs in priority order:
1. Critical namespace REAL-REQUIRED runs: trace first, then scout-feasibility, then listen
2. Non-critical REAL-REQUIRED runs
3. Evidence-heavy REAL-REQUIRED runs

Each entry: skill command + one-line reason derived from the evaluation above.

**Write Status Back**

Edit {mock-artifact-path}. For each namespace, replace the Status line only:
  Status: MOCK (awaiting review)
  → Status: MOCK-ACCEPTED [STRUCTURAL-COVERAGE-SUFFICIENT | DOMAIN-KNOWLEDGE-CONSISTENT]
  → Status: REAL-REQUIRED [{trigger or evaluation reason}]

One Status line per namespace. In-place edit. No other content changed.
Confirm: "Annotations updated in: {mock-artifact-path}"

---

## V-03 — Lifecycle Emphasis: Named Phases with Stop Gates

**axis:** lifecycle-emphasis
**hypothesis:** Structuring the skill as five explicitly named, numbered phases — each
with a STOP gate before the next phase begins — increases C-04 (status write-back)
and C-05 (next-steps in priority order) pass rates because the write-back is a required
Phase 5 rather than a closing note that can be omitted when the review narrative is
already satisfying. Without a named phase, write-back is the most commonly skipped
action because the review artifact itself feels like completion. The stop gate after
Phase 4 (write review artifact) forces the model to treat Phase 5 as a continuation,
not an optional epilogue.
Failure condition: if C-04 pass rate does not improve relative to a flat-instruction
baseline, the phase scaffolding does not prevent write-back omission.

---

You are running /mock:review.

Input:
  Topic:         {topic}
  Mock artifact: {mock-artifact-path}
  Tier:          {1|2|3} (--tier flag, or read from TOPICS.md, or default 1)

---

### PHASE 1 — READ AND CLASSIFY

- Read {mock-artifact-path}
- For each namespace section, extract: namespace name, Category, current Status
- Read TOPICS.md: tier for {topic}, compliance tags
- State the tier: "Tier: {N} (source: TOPICS.md | --tier | default)"

Output of Phase 1 — namespace inventory:
  | Namespace | Category | Current Status |

STOP. Complete the namespace inventory before entering Phase 2.

---

### PHASE 2 — AUTO-FLAGGING

Apply all three rules to every namespace. Each rule is mandatory.

  RULE EVIDENCE-HEAVY: Category == EVIDENCE-HEAVY → REAL-REQUIRED (all tiers)
  RULE TIER-CRITICAL:  Tier >= 2 AND namespace in {trace-*, scout-feasibility,
                       listen-*, scout-competitors} → REAL-REQUIRED
  RULE COMPLIANCE:     Compliance context active AND namespace in
                       {scout-compliance, trace-permissions} → REAL-REQUIRED

Record the trigger rule for each auto-REAL-REQUIRED namespace.

Output of Phase 2:
  Auto-flagged (REAL-REQUIRED):
  - {namespace}: trigger = {EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE}

  Remaining (awaiting Phase 3):
  - {namespace}: Category = {HIGH-STRUCTURE | MIXED}

STOP. Every namespace must appear in exactly one list before entering Phase 3.

---

### PHASE 3 — THREE-ROLE REVIEW

For each namespace in the "Remaining" list from Phase 2:

  PM:        Are required sections present? Are gates and tables well-formed?
  Architect: Does mock content contradict known facts about {topic}?
  Strategy:  Is coverage adequate for Tier {tier} decisions?

  Decision: MOCK-ACCEPTED or REAL-REQUIRED

  MOCK-ACCEPTED requires at least one code from this exact set:
    STRUCTURAL-COVERAGE-SUFFICIENT
    DOMAIN-KNOWLEDGE-CONSISTENT
  No paraphrase. No invented codes.

  REAL-REQUIRED: name which evaluation verdict drove the decision.

Output of Phase 3:
  For each reviewed namespace:
    - PM: [verdict]
    - Architect: [verdict]
    - Strategy: [verdict]
    - Decision: [MOCK-ACCEPTED [code(s)] | REAL-REQUIRED [reason]]

STOP. All remaining namespaces must have decisions before entering Phase 4.

---

### PHASE 4 — WRITE REVIEW ARTIFACT

Write simulations/mock/{topic}-review-{date}.md.

Section 1 — Header: Topic | Tier | Date
Section 2 — Coverage Review table:
  | Namespace | Category | Decision | Trigger / Reason Code |
  One row per namespace. All namespaces from Phases 2 and 3.
Section 3 — Next Steps (numbered, priority order):
  Priority 1: REAL-REQUIRED critical namespaces — trace, then scout-feasibility, then listen
  Priority 2: REAL-REQUIRED non-critical namespaces
  Priority 3: REAL-REQUIRED evidence-heavy namespaces
  Format: /{skill} {topic} — {one-line reason}

STOP. Review artifact must be written before entering Phase 5.

---

### PHASE 5 — WRITE STATUS BACK (mandatory)

This is the defining action of /mock:review. It cannot be skipped.

For every namespace in {mock-artifact-path}, use Edit to update the Status line in-place:

  Replace: Status: MOCK (awaiting review)
  With one of:
    Status: MOCK-ACCEPTED [STRUCTURAL-COVERAGE-SUFFICIENT | DOMAIN-KNOWLEDGE-CONSISTENT]
    Status: REAL-REQUIRED [{trigger or evaluation reason}]

Rules for this edit:
  - Edit the Status line only. No other content in the source artifact changes.
  - This is the only permitted in-place edit in Signal.
  - The decision written into the source artifact must match the review table from Phase 4.

After all edits:
  Confirm: "Annotations updated in: {mock-artifact-path}"
  Confirm: "Review written: simulations/mock/{topic}-review-{date}.md"

Zero Status fields may remain as MOCK (awaiting review) after Phase 5 completes.

---

## V-04 (Combined) — Role Sequence + Phrasing Register: Strict Imperative with Invoked Roles

**axes:** role-sequence + phrasing-register
**hypothesis:** Combining (a) the role-sequence gate from V-01 with (b) strict imperative
phrasing — DO NOT, MUST, NEVER — applied at every decision point increases C-02
(automatic rule correctness), C-03 (exact reason codes), and C-04 (write-back) pass
rates simultaneously. The mechanism: DO NOT gates name the exact forbidden output pattern
("DO NOT mark any EVIDENCE-HEAVY namespace MOCK-ACCEPTED regardless of mock quality"),
which reduces false MOCK-ACCEPTED decisions more effectively than positive guidance
("mark EVIDENCE-HEAVY as REAL-REQUIRED"). The positive form tells the model what to do
in the normal case; the negative form blocks the failure case directly.
Failure condition: if DO NOT gates do not improve error rates relative to V-01 positive
framing, the imperative register adds friction without reducing failures.

---

You are running /mock:review.

INPUTS:
  topic:         {topic}
  mock-artifact: {mock-artifact-path}
  tier:          {1|2|3} — read from TOPICS.md if not specified; default 1

---

STEP 1 — READ

Read {mock-artifact-path}.
Extract from each namespace section: namespace name, Category field, current Status field.
Read TOPICS.md. Record: tier for {topic}, compliance tags.

WRITE at the top of your output: "Tier: {N} (source: TOPICS.md | --tier | default)"
DO NOT proceed until all namespace header fields are extracted and listed.

---

STEP 2 — AUTO-FLAG

Apply these three rules in order. Each is mandatory. None is optional.

RULE 1 — EVIDENCE-HEAVY (all tiers):
  IF Category == EVIDENCE-HEAVY THEN: REAL-REQUIRED, trigger = EVIDENCE-HEAVY
  DO NOT mark any EVIDENCE-HEAVY namespace MOCK-ACCEPTED regardless of mock quality.

RULE 2 — TIER-CRITICAL (Tier 2 and Tier 3 only):
  IF tier >= 2 AND namespace in {trace-*, scout-feasibility, listen-*, scout-competitors}
  THEN: REAL-REQUIRED, trigger = TIER-CRITICAL
  DO NOT mark any Tier 2+ critical namespace MOCK-ACCEPTED.

RULE 3 — COMPLIANCE (when compliance context is active):
  IF compliance tags in TOPICS.md OR --compliance flag
  AND namespace in {scout-compliance, trace-permissions}
  THEN: REAL-REQUIRED, trigger = COMPLIANCE

DO NOT apply PM/Architect/Strategy evaluation to any auto-flagged namespace.

Output two lists before proceeding:
  Auto-flagged (REAL-REQUIRED):
  - {namespace}: trigger = {rule label}

  Remaining (awaiting Step 3 evaluation):
  - {namespace}: Category = {HIGH-STRUCTURE | MIXED}

DO NOT proceed until every namespace is placed in exactly one list.

---

STEP 3 — PM REVIEW (non-auto namespaces only)

PM MUST assess structural completeness for each remaining namespace:
  - Are all required sections present?
  - Are enforcement gates present and well-formed?
  - Are tables or required output structures present and correctly formed?
  Verdict per namespace: STRUCTURALLY ADEQUATE or STRUCTURALLY INCOMPLETE

Complete PM review for ALL remaining namespaces before proceeding to Step 4.

---

STEP 4 — ARCHITECT REVIEW (non-auto namespaces only)

Architect MUST assess technical plausibility for each remaining namespace:
  - Does the mock content contradict known architectural facts about {topic}?
  - Are dependencies, interfaces, or system constraints plausible?
  Verdict per namespace: PLAUSIBLE or CONTRADICTS KNOWN FACTS

Complete Architect review for ALL remaining namespaces before proceeding to Step 5.

---

STEP 5 — STRATEGY REVIEW (non-auto namespaces only)

Strategy MUST assess coverage adequacy for Tier {tier} for each remaining namespace:
  - Is this namespace covered sufficiently for Tier {tier} decisions?
  - Would the team be blocked or misled by accepting this as MOCK-ACCEPTED at Tier {tier}?
  Verdict per namespace: ADEQUATE or INSUFFICIENT FOR TIER {tier}

---

STEP 6 — DECIDE

For each remaining namespace, combine the three verdicts into a decision:

  IF PM = adequate AND Architect = plausible AND Strategy = adequate:
    Decision: MOCK-ACCEPTED
    MUST include at least one reason code from this exact list:
      STRUCTURAL-COVERAGE-SUFFICIENT  (when structural completeness drove the verdict)
      DOMAIN-KNOWLEDGE-CONSISTENT     (when content plausibility drove the verdict)
    NEVER use any other reason code. NEVER paraphrase these codes.

  OTHERWISE:
    Decision: REAL-REQUIRED
    Name the specific evaluation that failed and why.

---

STEP 7 — WRITE REVIEW ARTIFACT

Write simulations/mock/{topic}-review-{date}.md:

  Header: Topic | Tier used | Date
  Coverage Review table:
    | Namespace | Category | Decision | Trigger / Reason Code |
    One row per namespace; all namespaces from Steps 2 and 6.
  Next Steps (numbered, strict priority):
    Priority 1: REAL-REQUIRED critical namespaces in this order:
      trace-* first, then scout-feasibility, then listen-*
    Priority 2: REAL-REQUIRED non-critical namespaces
    Priority 3: REAL-REQUIRED evidence-heavy namespaces
    Format: /{skill-id} {topic} — {one-line reason}

---

STEP 8 — WRITE STATUS BACK (mandatory, non-skippable)

MUST update every Status line in {mock-artifact-path}.
Use Edit tool. In-place replacement only. Do not rewrite any other content.

For each namespace:
  REPLACE: Status: MOCK (awaiting review)
  WITH:    Status: MOCK-ACCEPTED [STRUCTURAL-COVERAGE-SUFFICIENT | DOMAIN-KNOWLEDGE-CONSISTENT]
  OR:      Status: REAL-REQUIRED [{trigger or evaluation reason}]

MUST confirm: "Annotations updated in: {mock-artifact-path}"
MUST confirm: "Review written: simulations/mock/{topic}-review-{date}.md"

NEVER leave any Status field as MOCK (awaiting review) after this step.
This is the defining action of /mock:review. It is not optional.

---

## V-05 (Combined) — Output Format + Inertia Framing: Decision Grid with Skip-Cost Column

**axes:** output-format + inertia-framing
**hypothesis:** Extending the decision table with a "Skip cost" column — answering "what
evidence is lost if this namespace stays at MOCK rather than running a real skill?" —
increases C-05 (next-steps in priority order), C-09 (coverage gap synthesis), and C-10
(namespace-specific MOCK-ACCEPTED rationale) pass rates. The inertia framing mechanism:
when the evaluation explicitly asks the team to name the cost of doing nothing, C-09's
cross-namespace risk statement is produced as a natural byproduct of filling the column
rather than requiring a separate synthesis step. The Skip Cost column makes the inertia
competitor — the team that skips real runs — visible in the output rather than leaving
it implicit. Failure condition: if C-09 and C-10 pass rates do not improve, the skip-cost
column adds table width without producing the synthesis the rubric requires.

---

You are running /mock:review.

Input:
  Topic:         {topic}
  Mock artifact: {mock-artifact-path}
  Tier:          {tier — from --tier flag, TOPICS.md, or default 1}

**Setup**

Read {mock-artifact-path}. For each namespace section, parse: namespace, Category, Status.
Read TOPICS.md: tier for {topic}, compliance tags.

State at the top of your output:
  "Tier used: {N} | Source: TOPICS.md | --tier | default"

**Automatic Rules**

Apply before any role evaluation. Not subject to override by evaluation roles.

  EVIDENCE-HEAVY (any tier) → REAL-REQUIRED (trigger: EVIDENCE-HEAVY)
  Critical namespace at Tier 2+: trace-*, scout-feasibility, listen-*, scout-competitors
    → REAL-REQUIRED (trigger: TIER-CRITICAL)
  Compliance context active, namespace in {scout-compliance, trace-permissions}
    → REAL-REQUIRED (trigger: COMPLIANCE)

**Role Evaluation (non-auto namespaces)**

The primary competitor to running a real skill is inertia — the team that accepts MOCK
as coverage without testing whether the fabricated content could mislead a real decision.
The three-role evaluation tests this directly.

For each non-auto namespace, evaluate:

PM: Is the mock artifact structurally complete for a Tier {tier} decision? Would a PM
  accept this artifact as coverage without a real run? Which specific sections or
  enforcement mechanisms confirm this?

Architect: Is the content technically plausible? Could a developer act on this content
  without encountering contradictions in the actual {topic} system? Name the specific
  structural element that confirms or challenges plausibility.

Strategy: What is the cost of not running the real skill? What Tier {tier} decision
  would be made incorrectly if this mock were treated as evidence rather than structure?
  If the cost is low, name why. If the cost is high, name what is at risk.

**Per-Namespace Output**

For each namespace, write a structured entry:

---

### {Namespace}
Category: {HIGH-STRUCTURE | EVIDENCE-HEAVY | MIXED}
Auto-flag: {REAL-REQUIRED (trigger) | none}

[If auto-flagged: skip PM/Architect/Strategy sections]
[If not auto-flagged: include all three]

PM: {one to two sentences on structural completeness}
Architect: {one to two sentences on technical plausibility}
Strategy: {one to two sentences on coverage adequacy for Tier {tier}}

Decision: {MOCK-ACCEPTED [STRUCTURAL-COVERAGE-SUFFICIENT | DOMAIN-KNOWLEDGE-CONSISTENT]
          | REAL-REQUIRED [reason]}

Skip cost: {For MOCK-ACCEPTED: "No evidence lost — structural coverage sufficient at
  Tier {tier}. [Name the specific structural property that supports acceptance.]"
  For REAL-REQUIRED: "Skipping this run leaves [specific evidence gap] unresolved,
  which would [specific consequence] at Tier {tier} decision time."}

---

After all namespace entries, write the consolidated decision grid:

**Coverage Decision Grid**

| Namespace | Category | Decision | Trigger / Reason Code | Skip Cost |
|-----------|----------|----------|-----------------------|-----------|

The Skip Cost column makes the inertia risk visible: namespaces with low skip cost are
candidates for MOCK-ACCEPTED; namespaces with high skip cost are gate-blockers where
inertia causes real harm at commit time.

**Next Steps**

Ordered by skip cost (highest inertia risk first):

Priority 1 — Gate-blockers (critical REAL-REQUIRED namespaces):
  These are Tier 2 gates. Inertia here risks undetectable build constraints or adoption
  blockers at commit time. Run in this order: trace-*, then scout-feasibility, then listen-*

Priority 2 — Non-critical REAL-REQUIRED namespaces:
  Skip cost is moderate. Run after critical namespaces are VERIFIED.

Priority 3 — Evidence-heavy REAL-REQUIRED namespaces:
  Mock content is structurally correct but evidentially zero. No real run means no data.

For each entry: /{skill} {topic} — {skip cost from the grid above}

**Write Status Back**

Edit {mock-artifact-path}. Replace each Status line in-place. No other content changed.
  Status: MOCK (awaiting review)
  → Status: MOCK-ACCEPTED [STRUCTURAL-COVERAGE-SUFFICIENT | DOMAIN-KNOWLEDGE-CONSISTENT]
  → Status: REAL-REQUIRED [{trigger or evaluation reason}]

This step is mandatory. The decision recorded in the review grid must exist in the source
artifact. A Status field left as MOCK (awaiting review) is not coverage — it is unknown.
Confirm: "Annotations updated in: {mock-artifact-path}"

---

## Variation Map Summary

| V | Axes | What Changed | Hypothesis |
|---|------|--------------|------------|
| V-01 | role-sequence | Auto-rules run as a gated Phase 1 that completes before any role evaluation begins | Prevents auto-rule softening by PM/Architect/Strategy; C-02 improves |
| V-02 | output-format | Prose narrative per namespace before summary table; three-role evaluation in full sentences | Forces substantive evaluation visible at C-07; richer MOCK-ACCEPTED rationale at C-10 |
| V-03 | lifecycle-emphasis | Five named phases with explicit STOP gates; write-back is Phase 5, not a closing note | Write-back treated as required phase, not optional epilogue; C-04 improves |
| V-04 | role-sequence + phrasing-register | V-01 auto-gate combined with strict DO NOT / MUST / NEVER imperatives at every decision point | DO NOT gates name the exact failure pattern; C-02, C-03, C-04 error modes blocked directly |
| V-05 | output-format + inertia-framing | Per-namespace Skip Cost field + extended decision table; inertia framing in Strategy evaluation prompt | Skip-cost column produces C-09 coverage gap synthesis as table output; inertia made visible |

**Top combination candidate for Round 2:**
V-01 (auto-gate) + V-03 (named phases) — if V-01 improves C-02 and V-03 improves C-04,
combining the gated auto-flag phase with the full phase scaffold addresses both without
the imperative overhead of V-04. Predict: C-02 + C-04 + C-05 all pass; C-07 depends on
whether phase-3 instructions produce enough per-role detail.
