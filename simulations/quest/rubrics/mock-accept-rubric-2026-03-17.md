# Rubric — mock-accept v2
*Updated from R1 scorecard: four new aspirational criteria (C-11 to C-14) derived from excellence signals.*

---

## Rubric Summary — mock-accept v2

**5 Essential** (must all pass — 60 pts):

| ID | What it tests |
|----|---------------|
| C-01 | Every namespace has exactly one decision (no omissions, no doubles) |
| C-02 | Auto-flag rules are never violated — EVIDENCE-HEAVY/TIER-CRITICAL/COMPLIANCE always REAL-REQUIRED |
| C-03 | Reason codes on MOCK-ACCEPTED use exact enumeration only (`STRUCTURAL-COVERAGE-SUFFICIENT` / `DOMAIN-KNOWLEDGE-CONSISTENT`) |
| C-04 | Source mock artifact Status fields all edited in-place; Canary assertion issued correctly |
| C-05 | MOCK-ACCEPTED decisions have both structural slots: SQ-1 tier-decision anchor (Slot 1) + named contrasting namespace (Slot 2) |

**3 Recommended** (30 pts): named role verdicts per namespace (C-06), review artifact at canonical path with Coverage Review table (C-07), next-steps in `/skill {topic}` invocation format (C-08).

**6 Aspirational** (10 pts): artifact-as-subject SQ grammar — no VERDICT-ECHO (C-09), single highest-risk gap with urgency label (C-10), inline completeness gate (C-11), reason-code enforcement at point of use (C-12), phase exit assertions (C-13), blank-line failure signal (C-14).

**Golden threshold**: all 5 essential pass + composite >= 80.

The dominant failure modes are C-02 (auto-flag bypass by a persuasive mock) and C-05 (SLOT-VIOLATION on the Structural position field — generic adequacy instead of a named tier decision).

---

## Essential Criteria (60 pts total)

*All five must pass. One fail = not golden, regardless of composite.*

| ID | Text | Weight | Category | Pass Condition |
|----|------|--------|----------|----------------|
| C-01 | Every namespace has exactly one decision | essential | completeness | The output contains exactly one decision entry per namespace (9 namespaces in the standard mock artifact). A namespace with no decision (omission) or two conflicting decisions (double) both fail. |
| C-02 | Auto-flag rules are never violated | essential | correctness | Every namespace classified as EVIDENCE-HEAVY (prove, listen), TIER-CRITICAL (flow, trace), or COMPLIANCE (program) receives REAL-REQUIRED regardless of mock quality or evaluation outcome. An EVIDENCE-HEAVY/TIER-CRITICAL/COMPLIANCE namespace that receives MOCK-ACCEPTED after a strong mock evaluation is a hard fail. |
| C-03 | Exact reason codes on MOCK-ACCEPTED | essential | format | Every MOCK-ACCEPTED decision carries at least one reason code from the exact enumeration: `STRUCTURAL-COVERAGE-SUFFICIENT` or `DOMAIN-KNOWLEDGE-CONSISTENT`. Paraphrased codes, invented codes, and codes embedded only in prose (not in the labeled reason-code field) all fail. |
| C-04 | Source mock artifact Status fields all updated -- Canary issued | essential | behavior | The skill edits the source mock artifact in-place using the Edit tool, replacing every "Status: MOCK (awaiting review)" with the final decision value. After edits, the Canary assertion is written verbatim: "Count: 0 Status fields remain as MOCK (awaiting review). Confirmed." If any Status field is unchanged, the Canary is suppressed and the output names the remaining fields. False positive Canary (emitted before verifying) is a hard fail. |
| C-05 | MOCK-ACCEPTED decisions have both structural slots populated | essential | format | Every MOCK-ACCEPTED block contains (a) a Structural position field with the SQ-1 Strategy anchor naming the specific tier decision the namespace supports, and (b) a Contrast field naming a contrasting namespace type and the structural factor that distinguishes it. A generic adequacy statement in Slot 1 without a named tier decision (SLOT-VIOLATION) or a confirmatory statement in Slot 2 without a named contrasting namespace type (CONTRAST-INCOMPLETE) both fail. |

---

## Recommended Criteria (30 pts total)

*Output is meaningfully better with these.*

| ID | Text | Weight | Category | Pass Condition |
|----|------|--------|----------|----------------|
| C-06 | Evaluation pipeline produces explicit named verdicts | recommended | depth | For each non-auto-flagged namespace, the output contains at minimum one explicitly named role verdict (Architect, Strategy, or PM) with the full verdict string (e.g., CONSISTENT-WITH-ARCHITECTURE, ADEQUATE FOR TIER 1, STRUCTURALLY ADEQUATE). A decision produced without any traceable role verdict is a fail for that namespace. |
| C-07 | Review artifact written at canonical path with Coverage Review table | recommended | format | The skill writes simulations/mock/{topic}-review-{date}.md and that file contains a Coverage Review table with columns: Namespace, Category, Decision, trigger. Ordering rule is stated. Cross-namespace risk statement with urgency level is present. |
| C-08 | Next-steps list uses /skill {topic} invocation format | recommended | format | The next-steps or priority list entries follow the format "/{skill-id} {topic} -- {Artifact state}". Entries that name a namespace without a skill invocation, or that list topics without skill IDs, fail. At least one entry from each applicable priority group (Critical REAL-REQUIRED, non-critical evaluation-driven) must be present. |

---

## Aspirational Criteria (10 pts total)

*Raise the bar once essential and recommended are stable.*

| ID | Text | Weight | Category | Pass Condition |
|----|------|--------|----------|----------------|
| C-09 | SQ answers use artifact-as-subject grammar -- no VERDICT-ECHO | aspirational | correctness | Every SQ answer driving a REAL-REQUIRED verdict is written with the artifact as grammatical subject in present tense ("Section 4 contains no tier-boundary gate" = pass; "Architect found no gate" = VERDICT-ECHO fail). At least one evaluation-driven REAL-REQUIRED decision must be present for this criterion to be scoreable; if none are present mark N/A. |
| C-10 | Cross-namespace risk statement identifies single highest-risk gap with urgency | aspirational | depth | The review artifact contains a cross-namespace risk statement naming exactly one highest-risk gap namespace, the specific tier decision at risk, and an urgency classification (BLOCKING, HIGH, or MEDIUM). A list of risks without a single highest-risk selection, or a statement without urgency, does not pass. |
| C-11 | Inline completeness gate asserts namespace count explicitly | aspirational | format | The skill includes a named checkpoint that asserts the count of namespaces processed equals the expected total — for example "count rows = 9" or "N+M = [total]. Matches working set." Implicit phase coverage without an explicit count or sum assertion does not pass. A skill where a missing namespace would pass through silently fails this criterion. *Source: V-02 count-rows=9 self-check; V-04 N+M=total sum assertion.* |
| C-12 | Reason-code constraint placed at point of use, not only in preamble | aspirational | format | The exact-enumeration constraint for reason codes (STRUCTURAL-COVERAGE-SUFFICIENT / DOMAIN-KNOWLEDGE-CONSISTENT) appears inside the table column rule, checklist checkbox, or labeled field definition — not only in introductory prose. A constraint stated only in preamble that is absent at the decision point does not pass. *Source: V-02 table column rule; V-05 checklist checkbox.* |
| C-13 | Phase exit assertions prevent auto-flag / evaluation interleave | aspirational | behavior | Each major phase boundary (auto-flag phase → evaluation phase) has an explicit exit assertion summarizing its output counts before the next phase begins (e.g., "[N] AUTO-FLAGGED, [M] EVALUATION-ELIGIBLE. Sum = [total]. Phase 1 complete."). A skill that interleaves auto-flag and evaluation logic without explicit phase boundaries or exit counts does not pass. *Source: V-04 Phase 1 exit assertion pattern.* |
| C-14 | Slot and field completeness is structurally visible without prose parsing | aspirational | format | The skill uses a format — checklist, table, or labeled slot block — where an incomplete or missing entry is visible as an empty cell, blank line, or unchecked item. A format that requires prose parsing to detect a missing slot, omitted field, or incomplete entry does not pass. *Source: V-05 blank-line failure signal: checklist item left blank is a structural gap, not a semantic one.* |

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 6 * 10)
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

Notes:
- C-09 is marked N/A (not scored) when no evaluation-driven REAL-REQUIRED decisions appear in the output. In that case the aspirational denominator decreases by 1 (use 5, not 6) and the formula uses `aspirational_pass / 5 * 10`.
- Each aspirational criterion is pass/fail (0 or 1). Partial credit is not awarded at the criterion level.

---

## Common Failure Modes

Derived from skill spec analysis (mock-review.t3/SKILL.md), trace-skill protocol, and R1 scorecard findings:

| Finding | Criterion | Failure Pattern |
|---------|-----------|-----------------|
| MA-01 | C-02 | EVIDENCE-HEAVY namespace (prove, listen) receives MOCK-ACCEPTED after strong mock quality -- auto-flag bypassed by evaluation outcome |
| MA-02 | C-03 | MOCK-ACCEPTED block uses paraphrase ("sufficient structural coverage") instead of exact code STRUCTURAL-COVERAGE-SUFFICIENT |
| MA-03 | C-04 | Edit tool called but Canary assertion omitted or emitted before verifying all fields changed |
| MA-04 | C-04 | CANARY-FALSE-POSITIVE: "Count: 0" written when one or more Status fields were not updated |
| MA-05 | C-05 | Structural position field contains generic statement ("supports tier 1 decision-making") without naming the specific tier-1 decision -- SLOT-VIOLATION |
| MA-06 | C-05 | Contrast field absent or merged with Structural position into single-slot rationale -- RATIONALE-INCOMPLETE |
| MA-07 | C-06 | Decision produced without any traceable role verdict -- output is a conclusion without an argument chain |
| MA-08 | C-09 | VERDICT-ECHO: "Strategy found the namespace adequate" as SQ answer -- role as subject instead of artifact as subject |
| MA-09 | C-11 | No namespace count assertion anywhere in output -- a missing namespace passes through silently (V-01, V-03 failure mode) |
| MA-10 | C-12 | Reason-code constraint stated in preamble only; column rule or checkbox omits the enumeration -- constraint invisible at decision point |
| MA-11 | C-13 | Auto-flag and evaluation steps interleaved in a single pass without exit assertion -- collapse makes C-02 bypass harder to detect |
| MA-12 | C-14 | Structural slots documented in prose paragraphs -- empty slot requires semantic reading rather than visible structural gap |

---

## Version History

| Version | Date | Change |
|---------|------|--------|
| v1 | 2026-03-17 | Initial rubric — 5 essential, 3 recommended, 2 aspirational |
| v2 | 2026-03-17 | R1 scorecard: added C-11 to C-14 (inline completeness gate, reason-code point-of-use, phase exit assertions, blank-line failure signal); aspirational denominator updated to 6; MA-09 to MA-12 added |
