---
skill: quest-variate
skill_target: topic-echo
date: 2026-03-15
round: 8
rubric: v8
---

# Variations: `topic:echo` — Round 8

**Rubric:** v8 | **Date:** 2026-03-15

---

## Design Context

R7 differentiating evidence: three structural patterns from R7 V-05 were observable but not
formalized as criteria in that round:

1. **R7 V-05 audit verdict gap**: V-05 placed the gestalt audit (C-26) and traceability
   check (C-24) as named chain links in the production chain trace. But neither step
   produced a written verdict token — each ended with an implicit branch ("if YES: revise /
   if NO: proceed"; "correct mismatches before proceeding"). An audit step whose output is
   only an implicit branch cannot be independently audited by C-28's rules: there is no
   structural artifact to locate. A future reader cannot verify that these steps ran without
   re-executing the prompt. C-29 closes this gap by requiring each verification step to
   produce a named verdict token (TRACE-CHECK-VERDICT, GESTALT-VERDICT) that is itself a
   chain node with a structural qualifier, traceable by the same rules as any production link.

2. **R7 V-05 sub-step look-back gap**: V-05 placed the Gatekeeper's FUNCTION DECLARATION
   block at Step 3 (satisfying C-27) and named roles per sub-step (satisfying C-25). But no
   individual sub-step carried both identity and declared function simultaneously. Stage 1
   carried `*(Gatekeeper; epistemic dimension: novelty)*` — identity present, function
   requires a look-back to the Step 3 header. Step 7 carried `*(IA)*` — identity only, no
   function inline. C-30 closes this by requiring co-activation at sub-step granularity: each
   sub-step that invokes a named role carries both name and function shorthand inline, so the
   epistemic posture at every sub-step is self-contained.

3. **R7 V-05 dependency graph incompleteness**: V-05's chain trace included the gestalt audit
   as a named node (partially satisfying C-31) but left other inter-criterion dependencies
   implicit. C-23's triage output feeding C-24's tier check, C-17's naming output feeding
   C-20's co-validation gate, and C-26's verdict feeding C-28's trace were structurally
   present but not traced. A reader can infer these relationships from the prompt structure
   but cannot read them from the chain trace alone. C-31 requires all such inter-criterion
   output-to-input flows to appear as named nodes in the trace — the dependency graph is
   closed when no relationship is discoverable only by reading the prompt.

These three patterns became C-29, C-30, and C-31 in v8. Aspirational criteria grew from 20
(C-09..C-28) to 23 (C-09..C-31), yielding a total rubric score of 60 + 21 + 69 = 150.

**Strategy for R8 variations:**
- V-01: Single-axis — C-29 (verification steps as chain nodes)
- V-02: Single-axis — C-30 (sub-step identity+function co-activation)
- V-03: Single-axis — C-31 (closed dependency graph)
- V-04: Combination — C-29 + C-30 + C-31
- V-05: Full combination — all 23 aspirational criteria (C-09..C-31)

---

## V-01 — Verification Chain Node Axis (C-29)

**Variation axis**: Lifecycle emphasis — verification steps produce named verdict tokens
that appear as first-class chain nodes, not exempt meta-gates outside the production chain.

**Hypothesis**: V-05 placed the gestalt audit and traceability check as named chain links,
but neither produced a written structural artifact. An audit step that concludes with an
implicit branch decision cannot be independently verified — a future reader cannot confirm it
ran without re-executing the prompt. C-29 closes this gap by requiring each verification
step to produce a named verdict token (TRACE-CHECK-VERDICT, GESTALT-VERDICT) before the
chain trace is written. Those tokens appear in the chain trace as named nodes with structural
qualifiers that make the verdict itself independently auditable.

**Builds on**: R7 V-05 — all 20 aspirational criteria (C-09..C-28) active.

**New elements targeting C-29**: Named verdict production at Steps 10 and 11. Both verdict
tokens appear as named chain nodes with structural qualifiers in Step 12.

---

You are running `/quest:topic echo` for the topic: {topic}.

All essential signals are in hand. Your task: surface the genuine surprises — findings that
only became visible in retrospect, from cross-signal tension, that no competent practitioner
would have predicted before gathering evidence.

Not a summary. Not a survey of discoveries. An echo: the signal that comes back that you
didn't send.

---

### Roles *(C-25)*

**Institutional Archaeologist (IA)** — active Steps 2, 5, 7, 8, 9.
Recovers false assumptions. Frames every surprise as a correction to a false assumption, not
a description of a discovery. Asks: "What would the next team build wrong?"

**Gatekeeper** — first invoked Step 3.

```
GATEKEEPER — FUNCTION DECLARATION (C-27)
─────────────────────────────────────────────────────────────────────
Function:      Adversarial rejection. Tests each gate-pipeline candidate
               against: (1) first-principles predictability; (2) cross-signal
               requirement. Fails either criterion: rejected.
Not-function:  Future-reader framing (IA's domain). Synthesis (IA's domain).
Role boundary: Gatekeeper verdicts are final. IA cannot override a rejection.
─────────────────────────────────────────────────────────────────────
```

Role names appear per sub-step throughout.

---

### Step 1 — Read Signal Record *(C-10; C-12)*

Read all signal artifacts across namespaces (scout, draft, review, flow, trace, prove,
listen, program, topic). Record namespaces covered (>=3 required) and date range.

---

### Step 2 — Pre-Write Prediction Sort *(IA; C-16; C-14; C-11; C-09)*

Typed route per finding:
- `topic-story` — confirms hypothesis; destination: topic narrative
- `topic-report` — restates known constraint; destination: report
- `gate-pipeline` — candidate surprise; proceeds to Step 3

Anti-hypothesis guard *(C-11)*: "Confirms what we set out to prove?" -> `topic-story`.
*(IA)* co-validation: "New team from spec alone would not have encountered this."
Discard log *(C-09)*: route type, reason, downstream destination. Non-empty required.

---

### Step 3 — Multi-Stage Epistemic Gate *(Gatekeeper; C-13; C-15; C-16)*

```
GATEKEEPER: active from here through Stage 3.
```

Anti-Pattern Catalog *(C-13)*: CONFIRMATION / RESTATEMENT / ISOLATED-FINDING.
Gate format *(C-16)*: `VERDICT: SURPRISE | CUT — {label if CUT}`
Three stages. Per-stage commit. Collapse prohibition.

**Stage 1 — Prediction Test** *(Gatekeeper)*
"Would a competent practitioner have predicted this from first principles?"
`PREDICTABLE` -> discard | `UNPREDICTABLE` -> Stage 2
Commit: `Stage 1: [{item}] -> [{verdict}]`

**Stage 2 — Contradiction Test** *(Gatekeeper)*
"Does this contradict the pre-investigation frame?"
```
We believed: {falsifiable assumption}
VALID: {genuine falsification}
INVALID (absence-of-consideration): {names absence, not falsified belief}
INVALID (sentiment-reaction): {surprise without named assumption}
INVALID (hedge-uncertainty): {hedges on whether belief was held}
```
Floor *(C-15)*: >=3 must reach CONTRADICTION FOUND. Record floor-miss if fewer.
`NO CONTRADICTION` -> discard | `CONTRADICTION FOUND` -> Stage 3
Commit: `Stage 2: [{item}] -> [{verdict}]`

**Stage 3 — Attribution Test** *(Gatekeeper)*
"Cross-signal emergence or single-artifact?"
`SINGLE-ARTIFACT` -> discard | `CROSS-SIGNAL (cite >=2)` -> SURPRISE
Commit: `Stage 3: [{item}] -> [{verdict}] — sources: [{artifact1 (ns/skill)}, {artifact2}]`

---

### Step 4 — Pre-Write Impact Triage *(C-23; C-22)*

Comparative HIGH/MEDIUM/LOW across all SURPRISE candidates before any expansion.
- HIGH: Forces revision to design decision, assumption, or scope boundary
- MEDIUM: Qualifies principle or adds constraint
- LOW: Notable; no current design consequence

*(C-22)*: Within each tier, failure-first ordering by mis-design severity.
Record triage before writing any entry. Write HIGH -> MEDIUM -> LOW; within tier: failure-first.

---

### Step 5 — Naming Scaffold *(C-17; C-21; IA)*

For each SURPRISE candidate:
1. State old belief: "The team carried the assumption that ___."
2. State correction: "The signals revealed instead that ___."
3. Derive domain: "This affects the ___ area."
4. Form: `The {Corrected Belief}: {Domain}`

VALID: "The Silent Veto: Adoption Workflow" | INVALID: "Surprising Finding About Adoption"

---

### Step 6 — Pre-Expansion Co-Validation Gate *(C-20; IA)*

Co-validate simultaneously before expanding any entry:
- Name form (C-17): `The {Corrected Belief}: {Domain}` -> VALID / INVALID
- Failure field (C-18): "If next team carries old assumption, {concrete mis-design}" -> VALID / INVALID

Both VALID to proceed. Either fails -> revise. Gate runs once per entry.

---

### Step 7 — Write Echo Entries *(IA; triage order; C-04; C-02; C-03; C-08; C-12; C-14; C-18; C-22)*

Entry production *(C-22)*: begin from failure, derive signal, name, impact.

**Begin from failure**: If the next team carries the old assumption about {domain},
they would {specific mis-design}. This is the anchor.

**[SURPRISE NAME: `The {Corrected Belief}: {Domain}`]** — *{HIGH | MEDIUM | LOW}* *(IA)*

Source signal: `{artifact-name} ({namespace}/{skill})`
`[CROSS: {artifact-A} x {artifact-B}]` *(C-08)*
Temporal anchor *(C-12)*: `{round or date}`
We believed: `{falsifiable assumption}`
The surprise: `{what signals revealed}`
If the next team carries the old assumption *(C-18)*: `{specific concrete mis-design}`.
Design impact *(C-03)*: `{decision revisited / assumption struck / scope boundary shifted}`.
Downstream route *(C-14)*: `-> {skill or namespace}`.

---

### Step 8 — Cross-Signal Synthesis *(C-05; IA)*

<=120 words. Name >=2 surprises by label. Explain the cross-entry pattern that only emerges
from reading them together — unreachable from any single entry alone.

---

### Step 9 — Forward Handover Guidance *(C-06; C-19; IA)*

Register menu *(C-19)*:
- T-1 (builder): "If you are about to build {scenario}, know that {constraint} because {source}."
- T-2 (reviewer): "Before approving {decision}, verify {constraint} against {source}."
- T-3 (PM): "Scope the {area} decision against {constraint} found in {source}."
- T-4 (architect): "The {component} design assumes {belief}; {source} shows this is false."

State register. Verify slots. Source must be citable.

---

### Step 10 — Rules of Thumb *(C-07; C-24)*

<=3 rules. HIGH and MEDIUM only.
```
[{HIGH | MEDIUM}] {Rule — <=20 words, quotable standalone}
(encodes: {SURPRISE NAME})
```

Traceability check *(C-24)*: tier matches triage from Step 4; no orphan rules;
one-rule-per-surprise. Correct mismatches before writing verdict.

**Write verdict** *(C-29: traceability check as chain node)*:

```
TRACE-CHECK-VERDICT: [PASS | FAIL]
  -- PASS: all tiers match; no orphan rules; one-rule-per-surprise confirmed
  -- FAIL: {each mismatch: rule label, expected tier, actual tier in entry}
```

This verdict is a structural artifact. A future reader verifies the check ran by locating
this token in the output — no session replay required.

---

### Step 11 — Gestalt Summary Audit *(C-26)*

*Applied to the complete draft output (Steps 7–10) as a single unit.*

"Could this output, read as a whole, be described as a survey of what the investigation found?"

YES/PARTLY YES: identify survey-reading entries; revise or discard; log `gestalt-summary-fail`;
re-run audit.

**Write verdict** *(C-29: gestalt audit as chain node)*:

```
GESTALT-VERDICT: [PASS | FAIL]
  -- PASS: output does not read as survey in aggregate; surprises are retroactively-visible
  -- FAIL: {entries revised or discarded, each with gestalt-summary-fail reason}
```

This verdict is a structural artifact auditable by the same rules as any production link.
PASS: proceed to Step 12.

---

### Step 12 — Production Chain Trace *(C-28; C-29)*

*Named chain links with structural qualifiers. Verification verdicts are chain nodes (C-29),
not exempt meta-gates.*

```
PRODUCTION CHAIN TRACE — VERIFICATION NODES INCLUDED (C-29)
──────────────────────────────────────────────────────────────────────
typed-route prediction sort (with IA co-validation per route, anti-hypothesis
  guard per candidate, typed downstream destination per discard, non-empty
  discard log as structural requirement)
-> staged gate verdict (with per-stage written commits, collapse prohibition,
    falsifiable "We believed:" field + VALID/INVALID contrast per Stage 2,
    cross-signal citation per Stage 3 SURPRISE)
-> comparative triage rank (HIGH/MEDIUM/LOW across all candidates simultaneously,
    failure-first within tier, all tiers recorded before any expansion)
-> echo entry (with name from 4-step derivation scaffold, failure-first production,
    [CROSS: A x B] annotation, failure field as concrete mis-design)
-> TRACE-CHECK-VERDICT (PASS: all tiers match, no orphan rules, one-rule-per-
    surprise; FAIL: listed mismatches -- produced by explicit check in Step 10
    before output written; verified by locating token in output)
-> GESTALT-VERDICT (PASS: does not read as survey in aggregate; FAIL: revised/
    discarded entries logged with gestalt-summary-fail -- produced by artifact-
    level audit question in Step 11; verified by locating token in output)
──────────────────────────────────────────────────────────────────────
Missing link protocol: Name absent links as ABSENT with reason.
Verification node protocol: TRACE-CHECK-VERDICT and GESTALT-VERDICT are chain
nodes, not meta-gates. Both are auditable by the same rules as any production link.
```

---

**Output**: Steps 7–12. Steps 1–6 are execution scaffolding.

Sequence: Echo entries -> Synthesis -> Handover -> Rules of Thumb + TRACE-CHECK-VERDICT ->
GESTALT-VERDICT -> Production chain trace.

Minimum surprise floor *(C-15)*: note floor-miss if fewer than 3 distinct surprises.

---

---

## V-02 — Sub-Step Co-Activation Axis (C-30)

**Variation axis**: Role sequence — every sub-step that invokes a named role carries both
role identity and role function inline, at sub-step granularity, requiring no look-back.

**Hypothesis**: V-05 satisfies C-25 (role names per sub-step) and C-27 (function declaration
at first invocation). But no individual sub-step carries both simultaneously. At Stage 1,
`*(Gatekeeper)*` names identity but requires a look-back to the Step 3 header to recover
function. At Step 7, `*(IA)*` names identity but requires a look-back to the preamble. C-30
closes this gap: each sub-step carries both role name and function shorthand inline, derived
from the FUNCTION DECLARATION. A model executing any individual sub-step sees identity and
function together without look-back to any containing scope.

**Builds on**: R7 V-05 — all 20 aspirational criteria (C-09..C-28) active.

**New element targeting C-30**: Inline function shorthand at every role sub-step invocation.
Format: `*(RoleName: function-shorthand)*`. The FUNCTION DECLARATION block (C-27) remains at
Step 3. Sub-step shorthands are derived from that declaration.

---

You are running `/quest:topic echo` for the topic: {topic}.

All essential signals are in hand. Your task: surface what those signals revealed that no
competent practitioner would have predicted before the investigation began.

Not a summary. Not a survey. An echo: the signal that comes back that you didn't send.

---

### Roles *(C-25; C-30: sub-step identity+function co-activation)*

**Institutional Archaeologist (IA)**
*First invocation: Step 2.*
Function: Recovers false assumptions embedded in current materials. Frames every surprise as
a correction to a false assumption, not a description of a discovery. Asks: "What would the
next team build wrong?"

Sub-step shorthand *(C-30)*: `IA: false-assumption-recovery`
Every sub-step the IA governs carries this shorthand. No sub-step requires a look-back to
recover IA's function.

Active: Steps 2, 5, 7, 8, 9.

**Gatekeeper**
*First invocation: Step 3.*
Sub-step shorthand *(C-30)*: `Gatekeeper: adversarial-rejection-only`
Every Stage header the Gatekeeper governs carries this shorthand.

```
GATEKEEPER — FUNCTION DECLARATION (C-27)
─────────────────────────────────────────────────────────────────────
Function:      Adversarial rejection. Tests: (1) first-principles predictability;
               (2) cross-signal emergence. Fails either: rejected.
Not-function:  Future-reader framing (IA's domain). Synthesis (IA's domain).
Role boundary: Gatekeeper verdicts are final. IA cannot override a rejection.
─────────────────────────────────────────────────────────────────────
```

Active: Step 3 only.

---

### Step 1 — Read Signal Record *(C-10; C-12)*

Read all signal artifacts across namespaces. Record namespaces covered (>=3) and date range.

---

### Step 2 — Pre-Write Prediction Sort
*(IA: false-assumption-recovery; C-16; C-14; C-11; C-09)*

Route every finding *(IA: false-assumption-recovery)*:
- `topic-story` — confirms hypothesis
- `topic-report` — known constraint
- `gate-pipeline` — candidate surprise; proceeds to Step 3

Anti-hypothesis guard *(C-11; IA: false-assumption-recovery)*: "Confirms what we set out to
prove?" -> `topic-story`.

Co-validation *(IA: false-assumption-recovery)*: "New team from spec alone would not have
encountered this." Cannot confirm -> `topic-report`.

Discard log *(C-09; IA: false-assumption-recovery)*: route type, reason, destination.

---

### Step 3 — Multi-Stage Epistemic Gate
*(Gatekeeper: adversarial-rejection-only; C-13; C-15; C-16)*

```
GATEKEEPER: adversarial-rejection-only — active from here through Stage 3.
```

Anti-Pattern Catalog *(C-13; Gatekeeper: adversarial-rejection-only)*:
- CONFIRMATION -> PREDICTABLE | RESTATEMENT -> `topic-report` | ISOLATED-FINDING -> `topic-report`

Gate format *(C-16)*: `VERDICT: SURPRISE | CUT — {label if CUT}`
Three stages. Per-stage commit. Collapse prohibition.

**Stage 1 — Prediction Test** *(Gatekeeper: adversarial-rejection-only)*
"Would a competent practitioner have predicted this from first principles?"
`PREDICTABLE` -> discard | `UNPREDICTABLE` -> Stage 2
Commit: `Stage 1: [{item}] -> [{verdict}]`

**Stage 2 — Contradiction Test** *(Gatekeeper: adversarial-rejection-only)*
"Does this contradict the pre-investigation frame?"
```
We believed: {falsifiable assumption}
VALID: {genuine falsification}
INVALID (absence-of-consideration): {names absence not falsified belief}
INVALID (sentiment-reaction): {surprise without named assumption}
INVALID (hedge-uncertainty): {hedges on whether belief was held}
```
Floor *(C-15)*: >=3 must reach CONTRADICTION FOUND.
`NO CONTRADICTION` -> discard | `CONTRADICTION FOUND` -> Stage 3
Commit: `Stage 2: [{item}] -> [{verdict}]`

**Stage 3 — Attribution Test** *(Gatekeeper: adversarial-rejection-only)*
"Cross-signal or single-artifact?"
`SINGLE-ARTIFACT` -> discard | `CROSS-SIGNAL (cite >=2)` -> SURPRISE
Commit: `Stage 3: [{item}] -> [{verdict}] — sources: [{artifact1 (ns/skill)}, {artifact2}]`

---

### Step 4 — Pre-Write Impact Triage *(C-23; C-22)*

Comparative HIGH/MEDIUM/LOW across all SURPRISE candidates before any expansion.
*(C-22)*: Within tier, failure-first. Record before writing any entry.

---

### Step 5 — Naming Scaffold *(C-17; C-21; IA: false-assumption-recovery)*

For each candidate *(IA: false-assumption-recovery)*:
1. State old belief  2. State correction  3. Derive domain
4. Form: `The {Corrected Belief}: {Domain}`

---

### Step 6 — Pre-Expansion Co-Validation Gate *(C-20; IA: false-assumption-recovery)*

Co-validate *(IA: false-assumption-recovery)*: name form (C-17) and failure field (C-18).
Both VALID to proceed.

---

### Step 7 — Write Echo Entries
*(IA: false-assumption-recovery; triage order; C-04; C-02; C-03; C-08; C-12; C-14; C-18; C-22)*

Begin from failure *(IA: false-assumption-recovery; C-22)*: If next team carries old
assumption about {domain}, they would {specific mis-design}. Anchor.

**[SURPRISE NAME: `The {Corrected Belief}: {Domain}`]** — *{HIGH | MEDIUM | LOW}*
*(IA: false-assumption-recovery)*

Source signal: `{artifact-name} ({namespace}/{skill})`
`[CROSS: {artifact-A} x {artifact-B}]` *(C-08)*
Temporal anchor *(C-12)*: `{date}`
We believed: `{falsifiable assumption}`
The surprise: `{what signals revealed}`
If next team carries old assumption *(C-18)*: `{specific mis-design}`.
Design impact *(C-03)*: `{decision/assumption/scope boundary}`.
Downstream route *(C-14)*: `-> {skill}`.

---

### Step 8 — Cross-Signal Synthesis *(C-05; IA: false-assumption-recovery)*

<=120 words. Name >=2 surprises. Explain cross-entry pattern unreachable from single entry.

---

### Step 9 — Forward Handover Guidance *(C-06; C-19; IA: false-assumption-recovery)*

Register menu *(C-19; IA: false-assumption-recovery)*: T-1/T-2/T-3/T-4.
State register. Verify slots. Source citable.

---

### Step 10 — Rules of Thumb *(C-07; C-24)*

<=3 rules. HIGH and MEDIUM only.
```
[{HIGH | MEDIUM}] {Rule — <=20 words}
(encodes: {SURPRISE NAME})
```
Traceability check *(C-24)*: tier matches triage; no orphans; one-rule-per-surprise.

---

### Step 11 — Gestalt Summary Audit *(C-26)*

"Could this output, read as a whole, be described as a survey of what the investigation found?"
YES/PARTLY YES: revise or discard; log `gestalt-summary-fail`; re-run.
NO: proceed to Step 12.

---

### Step 12 — Production Chain Trace *(C-28)*

```
PRODUCTION CHAIN TRACE
──────────────────────────────────────────────────────────────────────
typed-route prediction sort (IA: false-assumption-recovery; co-validation,
  anti-hypothesis guard, typed destinations, non-empty discard log)
-> staged gate verdict (Gatekeeper: adversarial-rejection-only; per-stage
    commits, collapse prohibition, falsifiable "We believed:" + VALID/INVALID
    contrast, cross-signal citation per SURPRISE)
-> comparative triage rank (HIGH/MEDIUM/LOW simultaneously, failure-first
    within tier, all tiers before expansion)
-> echo entry (IA: false-assumption-recovery; name from derivation scaffold,
    failure-first production, [CROSS: A x B], failure field as mis-design)
-> impact-anchored rule (tier verified by explicit traceability check)
-> gestalt audit (IA: false-assumption-recovery; complete artifact as unit;
    gestalt-summary-fail logged separately)
──────────────────────────────────────────────────────────────────────
Missing link protocol: Name absent links as ABSENT with reason.
```

---

**Output**: Steps 7–12. Steps 1–6 are execution scaffolding.

Sequence: Echo entries -> Synthesis -> Handover -> Rules of Thumb -> Gestalt audit note
(if revisions) -> Production chain trace.

Minimum surprise floor *(C-15)*: note floor-miss if fewer than 3 distinct surprises.

---

---

## V-03 — Closed Dependency Graph Axis (C-31)

**Variation axis**: Output format — production chain trace extended with explicit
inter-criterion dependency annotations. The criterion relationship graph is readable from
the trace alone without reasoning about the prompt structure.

**Hypothesis**: V-05's chain trace satisfies C-28 (structural qualifiers on every link) and
partially satisfies C-31 (gestalt audit as a named node closes one dependency loop). But
other inter-criterion flows remain implicit: C-23 output feeding C-24 tier check, C-17
output feeding C-20 co-validation, C-26 verdict feeding C-28 trace. A reader can infer
these from the prompt but cannot read them from the trace alone. C-31 requires every
inter-criterion output-to-input relationship to appear as a named node in the trace —
explicitly annotated, not inferred.

**Builds on**: R7 V-05 — all 20 aspirational criteria (C-09..C-28) active.

**New element targeting C-31**: Step 12 chain trace extended with explicit `produces:` and
`consumed by:` annotations on each node. All inter-criterion dependencies are named. The
trace is a closed dependency graph.

---

You are running `/quest:topic echo` for the topic: {topic}.

All essential signals are in hand. Surface what those signals revealed that no competent
practitioner would have predicted. Name each surprise, trace it to its source, and assess
its impact on the design direction.

Not a summary. Not a survey. An echo.

---

### Roles *(C-25)*

**Institutional Archaeologist (IA)** — active Steps 2, 5, 7, 8, 9.
Recovers false assumptions. Frames every surprise as a correction, not a discovery.

**Gatekeeper** — first invoked Step 3.

```
GATEKEEPER — FUNCTION DECLARATION (C-27)
─────────────────────────────────────────────────────────────────────
Function:      Adversarial rejection. Tests predictability and cross-signal
               emergence. Fails either: rejected.
Not-function:  Future-reader framing (IA). Synthesis (IA).
Role boundary: Gatekeeper verdicts are final.
─────────────────────────────────────────────────────────────────────
```

Role names appear per sub-step.

---

### Step 1 — Read Signal Record *(C-10; C-12)*

Read all signal artifacts across namespaces. Record namespaces (>=3) and date range.

---

### Step 2 — Pre-Write Prediction Sort *(IA; C-16; C-14; C-11; C-09)*

Route per finding: `topic-story` / `topic-report` / `gate-pipeline`.
Anti-hypothesis guard *(C-11)*. IA co-validation. Discard log *(C-09)*.

---

### Step 3 — Multi-Stage Epistemic Gate *(Gatekeeper; C-13; C-15; C-16)*

Anti-Pattern Catalog *(C-13)*. Gate format *(C-16)*. Three stages, per-stage commit.

**Stage 1 — Prediction Test** *(Gatekeeper)* — `PREDICTABLE` -> discard | `UNPREDICTABLE` -> Stage 2
Commit: `Stage 1: [{item}] -> [{verdict}]`

**Stage 2 — Contradiction Test** *(Gatekeeper)*
```
We believed: {falsifiable assumption}
VALID: {genuine falsification}
INVALID (absence-of-consideration) | INVALID (sentiment-reaction) | INVALID (hedge-uncertainty)
```
Floor *(C-15)*: >=3 CONTRADICTION FOUND required.
Commit: `Stage 2: [{item}] -> [{verdict}]`

**Stage 3 — Attribution Test** *(Gatekeeper)* — cross-signal or single-artifact?
Commit: `Stage 3: [{item}] -> [{verdict}] — sources: [{artifact1}, {artifact2}]`

---

### Step 4 — Pre-Write Impact Triage *(C-23; C-22)*

Comparative HIGH/MEDIUM/LOW. Failure-first within tier *(C-22)*. Record before expansion.

---

### Step 5 — Naming Scaffold *(C-17; C-21; IA)*

1. Old belief  2. Correction  3. Domain  4. `The {Corrected Belief}: {Domain}`

---

### Step 6 — Pre-Expansion Co-Validation Gate *(C-20; IA)*

Name form (C-17) and failure field (C-18) co-validated. Both VALID to expand.

---

### Step 7 — Write Echo Entries *(IA; C-04; C-02; C-03; C-08; C-12; C-14; C-18; C-22)*

Begin from failure *(C-22)*. Derive signal, name, impact.

**[SURPRISE NAME: `The {Corrected Belief}: {Domain}`]** — *{HIGH | MEDIUM | LOW}* *(IA)*

Source: `{artifact-name} ({ns/skill})` | `[CROSS: A x B]` | Temporal: `{date}`
We believed: / The surprise: / If next team *(C-18)*: `{mis-design}`.
Impact *(C-03)*: / Route *(C-14)*: `->`.

---

### Step 8 — Cross-Signal Synthesis *(C-05; IA)*

<=120 words. >=2 named surprises. Cross-entry pattern only visible in combination.

---

### Step 9 — Forward Handover Guidance *(C-06; C-19; IA)*

T-1..T-4 register menu. State register. Verify slots.

---

### Step 10 — Rules of Thumb *(C-07; C-24)*

<=3 rules. HIGH/MEDIUM only.
```
[{HIGH | MEDIUM}] {Rule}
(encodes: {SURPRISE NAME})
```
Traceability check *(C-24)*. Correct mismatches.

---

### Step 11 — Gestalt Summary Audit *(C-26)*

"Could this output, read as a whole, be described as a survey of what the investigation found?"
Revise or discard if YES. Log `gestalt-summary-fail`. Re-run.

---

### Step 12 — Production Chain Trace with Closed Dependency Graph *(C-28; C-31)*

*Named chain links with structural qualifiers AND explicit inter-criterion dependency
annotations. The dependency graph is closed: no relationship is discoverable only by
reading the prompt (C-31).*

```
PRODUCTION CHAIN TRACE — DEPENDENCY GRAPH CLOSED (C-31)
══════════════════════════════════════════════════════════════════════

[NODE 1] typed-route prediction sort
  structural qualifier: IA co-validation per route, anti-hypothesis guard per
    candidate, typed downstream destination per discard, non-empty discard log
  produces: typed route decisions (C-16), discard log with destinations (C-09+C-14)
  consumed by: NODE 2 (receives gate-pipeline candidates)

-> [NODE 2] staged gate verdict
  structural qualifier: per-stage written commit tokens, collapse prohibition,
    falsifiable "We believed:" + VALID/INVALID contrast per Stage 2, cross-signal
    citation per Stage 3 SURPRISE
  produces: SURPRISE verdicts (C-13/C-16), floor count (C-15)
  consumed by: NODE 3 (confirmed SURPRISE candidates for triage)

-> [NODE 3] comparative triage rank
  structural qualifier: all candidates evaluated simultaneously, failure-first
    within tier, all tiers recorded before any expansion
  produces: HIGH/MEDIUM/LOW triage assignments (C-23), within-tier order (C-22)
  consumed by: NODE 4 entry headers (C-07: tier labels require C-23 output)
               NODE 7 rules (C-24: tier-match check requires C-23 output)

-> [NODE 4] echo entry
  structural qualifier: name from 4-step derivation scaffold (C-17+C-21), failure-
    first production (C-22), [CROSS: A x B] annotation (C-08), failure field as
    concrete mis-design not change-list (C-18), design impact names decision/
    assumption/scope (C-03)
  produces: named surprise labels (C-04), source citations (C-02), design impact
            (C-03), routing tags (C-14)
  consumed by: NODE 5 synthesis (C-05: requires >=2 named surprise labels)
               NODE 6 handover (C-06: requires named scenario from C-14 routing)
               NODE 7 rules (C-24: requires named surprise per rule)

-> [NODE 5] cross-signal synthesis
  structural qualifier: >=2 named labels cited, pattern unreachable from single entry
  produces: synthesized echo paragraph (C-05)
  consumed by: output (terminal)

-> [NODE 6] forward handover guidance
  structural qualifier: register from T-1..T-4 (C-19), slots verified (C-06), citable
  produces: register-anchored handoff (C-06+C-19)
  consumed by: output (terminal)

-> [NODE 7] impact-anchored rule
  structural qualifier: tier verified against NODE 3 triage by explicit check (C-24),
    orphan rule check, one-rule-per-surprise
  produces: verified rules (C-07+C-24)
  consumed by: NODE 8 chain trace (C-28: rules are production links)

-> [NODE 8] gestalt audit
  structural qualifier: applied to complete artifact as unit, gestalt-summary-fail
    discards logged separately from item-level gate-fail (C-26)
  produces: gestalt audit result (C-26 output)
  consumed by: NODE 9 chain trace (C-28+C-31: gestalt verdict is named chain node;
               this is the archetypal C-31 loop: C-26 output -> C-28 node)

-> [NODE 9] production chain trace (this node)
  structural qualifier: all nodes named with structural qualifiers (C-28); all
    inter-criterion dependencies explicitly annotated — graph closed (C-31)
  produces: closed dependency graph readable without prompt re-inspection
  consumed by: output (terminal)

══════════════════════════════════════════════════════════════════════
Missing link protocol: Name absent nodes as ABSENT with reason.
Dependency closure check (C-31): all inter-criterion output-to-input relationships
are represented above. No relationship is discoverable only by reading the prompt.
```

---

**Output**: Steps 7–12. Steps 1–6 are execution scaffolding.

Sequence: Echo entries -> Synthesis -> Handover -> Rules of Thumb -> Gestalt audit note ->
Production chain trace.

Minimum surprise floor *(C-15)*: note floor-miss if fewer than 3 distinct surprises.

---

---

## V-04 — Combination (C-29 + C-30 + C-31)

**Variation axis**: Combination — lifecycle emphasis (C-29: verdict chain nodes) + role
sequence (C-30: sub-step co-activation) + output format (C-31: closed dependency graph).

**Hypothesis**: The three new criteria address distinct gaps at non-conflicting layers.
C-30 activates at execution time (sub-step: identity+function co-activate; no look-back).
C-29 activates at audit-output time (each verification step produces a named verdict token
before the chain trace is written). C-31 activates at trace-write time (all inter-criterion
dependencies are explicitly named; graph is closed). Together they close the audit trail from
sub-step execution through verification verdict through dependency graph — three orthogonal
structural gaps closed by a single combined prompt.

**Builds on**: R7 V-05 (all 20 aspirational criteria). V-01/V-02/V-03 each isolated;
this variation combines all three.

---

You are running `/quest:topic echo` for the topic: {topic}.

All essential signals are in hand. Your task: surface the genuine surprises — findings only
visible in retrospect, from cross-signal tension, that no competent practitioner would have
predicted before gathering evidence.

Not a summary. Not a survey of discoveries. An echo: the signal that comes back that you
didn't send.

---

### Roles *(C-25; C-30: sub-step identity+function co-activation)*

**Institutional Archaeologist (IA)**
*First invocation: Step 2.*
Function: Recovers false assumptions. Frames every surprise as a correction to a false
assumption, not a discovery. Asks: "What would the next team build wrong?"

Sub-step shorthand *(C-30)*: `IA: false-assumption-recovery`
Appears at every sub-step IA governs. No look-back required to recover function.

Active: Steps 2, 5, 7, 8, 9.

**Gatekeeper**
*First invocation: Step 3.*
Sub-step shorthand *(C-30)*: `Gatekeeper: adversarial-rejection-only`

```
GATEKEEPER — FUNCTION DECLARATION (C-27)
─────────────────────────────────────────────────────────────────────
Function:      Adversarial rejection. Tests: (1) first-principles predictability;
               (2) cross-signal emergence. Fails either: rejected.
Not-function:  Future-reader framing (IA's domain). Synthesis (IA's domain).
Role boundary: Gatekeeper verdicts are final. IA cannot override a rejection.
─────────────────────────────────────────────────────────────────────
```

Active: Step 3 only.

---

### Step 1 — Read Signal Record *(C-10; C-12)*

Read all signal artifacts across namespaces (scout, draft, review, flow, trace, prove,
listen, program, topic). Record namespaces covered (>=3) and date range.

---

### Step 2 — Pre-Write Prediction Sort
*(IA: false-assumption-recovery; C-16; C-14; C-11; C-09)*

Route per finding *(IA: false-assumption-recovery)*:
- `topic-story` — confirms hypothesis
- `topic-report` — known constraint
- `gate-pipeline` — candidate surprise; proceeds to Step 3

Anti-hypothesis guard *(C-11; IA: false-assumption-recovery)*: "Confirms what we set out to
prove?" -> `topic-story`.
Co-validation *(IA: false-assumption-recovery)*: "New team from spec alone would not have
encountered this." Cannot confirm -> `topic-report`.
Discard log *(C-09; IA: false-assumption-recovery)*: type, reason, destination. Non-empty.

---

### Step 3 — Multi-Stage Epistemic Gate
*(Gatekeeper: adversarial-rejection-only; C-13; C-15; C-16)*

```
GATEKEEPER: adversarial-rejection-only — active through Stage 3.
```

Anti-Pattern Catalog *(C-13; Gatekeeper: adversarial-rejection-only)*:
CONFIRMATION / RESTATEMENT / ISOLATED-FINDING.

Gate format *(C-16)*: `VERDICT: SURPRISE | CUT — {label if CUT}`
Three stages. Per-stage commit. Collapse prohibition.

**Stage 1 — Prediction Test** *(Gatekeeper: adversarial-rejection-only)*
"Would a competent practitioner have predicted this?"
`PREDICTABLE` -> discard | `UNPREDICTABLE` -> Stage 2
Commit: `Stage 1: [{item}] -> [{verdict}]`

**Stage 2 — Contradiction Test** *(Gatekeeper: adversarial-rejection-only)*
"Contradicts the pre-investigation frame?"
```
We believed: {falsifiable assumption}
VALID: {genuine falsification}
INVALID (absence-of-consideration) | INVALID (sentiment-reaction) | INVALID (hedge-uncertainty)
```
Floor *(C-15)*: >=3 CONTRADICTION FOUND required.
Commit: `Stage 2: [{item}] -> [{verdict}]`

**Stage 3 — Attribution Test** *(Gatekeeper: adversarial-rejection-only)*
"Cross-signal or single-artifact?"
`SINGLE-ARTIFACT` -> discard | `CROSS-SIGNAL (cite >=2)` -> SURPRISE
Commit: `Stage 3: [{item}] -> [{verdict}] — sources: [{artifact1 (ns/skill)}, {artifact2}]`

---

### Step 4 — Pre-Write Impact Triage *(C-23; C-22)*

Comparative HIGH/MEDIUM/LOW. Failure-first within tier *(C-22)*. Record before expansion.
Write HIGH -> MEDIUM -> LOW; within tier: failure-first.

---

### Step 5 — Naming Scaffold *(C-17; C-21; IA: false-assumption-recovery)*

*(IA: false-assumption-recovery)*:
1. Old belief  2. Correction  3. Domain  4. `The {Corrected Belief}: {Domain}`

---

### Step 6 — Pre-Expansion Co-Validation Gate *(C-20; IA: false-assumption-recovery)*

*(IA: false-assumption-recovery)*: Name form (C-17) and failure field (C-18). Both VALID.

---

### Step 7 — Write Echo Entries
*(IA: false-assumption-recovery; C-04; C-02; C-03; C-08; C-12; C-14; C-18; C-22)*

Begin from failure *(IA: false-assumption-recovery; C-22)*: anchor on mis-design.

**[SURPRISE NAME: `The {Corrected Belief}: {Domain}`]** — *{HIGH | MEDIUM | LOW}*
*(IA: false-assumption-recovery)*

Source: `{artifact-name} ({ns/skill})` | `[CROSS: A x B]` *(C-08)* | Temporal *(C-12)*: `{date}`
We believed: / The surprise: / If next team *(C-18)*: `{mis-design}`.
Impact *(C-03)*: / Route *(C-14)*: `->`.

---

### Step 8 — Cross-Signal Synthesis *(C-05; IA: false-assumption-recovery)*

<=120 words. >=2 surprises named. Cross-entry pattern *(IA: false-assumption-recovery)*.

---

### Step 9 — Forward Handover Guidance *(C-06; C-19; IA: false-assumption-recovery)*

T-1..T-4 register *(C-19; IA: false-assumption-recovery)*. State register. Verify slots.

---

### Step 10 — Rules of Thumb *(C-07; C-24)*

<=3 rules. HIGH/MEDIUM only.
```
[{HIGH | MEDIUM}] {Rule — <=20 words}
(encodes: {SURPRISE NAME})
```
Traceability check *(C-24)*: tier matches triage; no orphans; one-rule-per-surprise.

**Write verdict** *(C-29: traceability check as chain node)*:
```
TRACE-CHECK-VERDICT: [PASS | FAIL]
  -- PASS: all tiers match; no orphan rules; one-rule-per-surprise confirmed
  -- FAIL: {rule label, expected tier, actual tier per mismatch}
```

---

### Step 11 — Gestalt Summary Audit *(C-26)*

"Could this output, read as a whole, be described as a survey of what the investigation found?"

YES/PARTLY YES: revise or discard; log `gestalt-summary-fail`; re-run.

**Write verdict** *(C-29: gestalt audit as chain node)*:
```
GESTALT-VERDICT: [PASS | FAIL]
  -- PASS: does not read as survey in aggregate
  -- FAIL: {entries revised/discarded with gestalt-summary-fail reason}
```

PASS: proceed to Step 12.

---

### Step 12 — Production Chain Trace *(C-28; C-29; C-31)*

*Named links with structural qualifiers. Verification verdicts are chain nodes (C-29).
All inter-criterion dependencies explicitly annotated — graph closed (C-31).*

```
PRODUCTION CHAIN TRACE
VERIFICATION NODES INCLUDED (C-29) | DEPENDENCY GRAPH CLOSED (C-31)
══════════════════════════════════════════════════════════════════════

[NODE 1] typed-route prediction sort
  qualifier: IA: false-assumption-recovery co-validation (C-30), anti-hypothesis
    guard (C-11), typed downstream destinations (C-14), non-empty discard log (C-09)
  produces: typed routes (C-16), discard log (C-09+C-14)
  consumed by: NODE 2

-> [NODE 2] staged gate verdict
  qualifier: Gatekeeper: adversarial-rejection-only at each Stage (C-30), per-stage
    commits, collapse prohibition, "We believed:" + VALID/INVALID contrast, cross-
    signal citation per SURPRISE
  produces: SURPRISE verdicts (C-13/C-16), floor count (C-15)
  consumed by: NODE 3

-> [NODE 3] comparative triage rank
  qualifier: all candidates simultaneously (C-23), failure-first within tier (C-22)
  produces: HIGH/MEDIUM/LOW triage (C-23), within-tier order (C-22)
  consumed by: NODE 4 (entry tier headers, C-07)
               NODE 7 (tier-match check, C-24 requires C-23 output)

-> [NODE 4] echo entry
  qualifier: IA: false-assumption-recovery at each sub-step (C-30); name from
    derivation scaffold (C-17+C-21), failure-first production (C-22), [CROSS: A x B]
    (C-08), failure field as mis-design (C-18)
  produces: named surprises (C-04), citations (C-02), impact (C-03), routing (C-14)
  consumed by: NODE 5 (>=2 labels for synthesis, C-05)
               NODE 6 (routing for handover, C-06)
               NODE 7 (named surprise per rule, C-24)

-> [NODE 5] cross-signal synthesis
  qualifier: >=2 labels cited, pattern unreachable from single entry (C-05)
  produces: echo paragraph (C-05)
  consumed by: output (terminal)

-> [NODE 6] forward handover guidance
  qualifier: register from T-1..T-4 (C-19), verified slots (C-06), citable source
  produces: register-anchored handoff (C-06+C-19)
  consumed by: output (terminal)

-> [NODE 7] impact-anchored rule
  qualifier: tier verified against NODE 3 by explicit check (C-24), orphan check,
    one-rule-per-surprise
  produces: verified rules (C-07+C-24)
  consumed by: NODE 8 TRACE-CHECK-VERDICT

-> [NODE 8] TRACE-CHECK-VERDICT [C-29: verification as chain node]
  qualifier: written PASS|FAIL token produced by explicit match-step in Step 10
    before output; verifiable by locating token; records mismatches if FAIL
  produces: traceability audit result (C-24+C-29)
  consumed by: NODE 10 chain trace (C-28+C-31: TRACE-CHECK is named chain node)

-> [NODE 9] gestalt audit
  qualifier: IA: false-assumption-recovery applied to complete artifact (C-30+C-26),
    gestalt-summary-fail logged separately from gate-fail (C-26)
  produces: gestalt result (C-26)
  consumed by: NODE 10 GESTALT-VERDICT

-> [NODE 10] GESTALT-VERDICT [C-29: verification as chain node]
  qualifier: written PASS|FAIL token produced by audit question in Step 11;
    verifiable by locating token; records revised/discarded if FAIL
  produces: gestalt audit result (C-26+C-29)
  consumed by: NODE 11 chain trace (C-28+C-31: closes C-26->C-28 loop)

-> [NODE 11] production chain trace (this node)
  qualifier: all nodes with qualifiers (C-28); verification verdicts are chain
    nodes not meta-gates (C-29); all inter-criterion dependencies named (C-31)
  produces: closed dependency graph
  consumed by: output (terminal)

══════════════════════════════════════════════════════════════════════
Missing link protocol: Name absent nodes as ABSENT with reason.
Dependency closure (C-31): all inter-criterion output-to-input flows are named
above. No relationship is discoverable only by reading the prompt.
```

---

**Output**: Steps 7–12. Steps 1–6 are scaffolding.

Sequence: Echo entries -> Synthesis -> Handover -> Rules + TRACE-CHECK-VERDICT ->
GESTALT-VERDICT -> Production chain trace.

Minimum surprise floor *(C-15)*: note floor-miss if fewer than 3 distinct surprises.

---

---

## V-05 — Full Combination (All 23 Aspirational Criteria: C-09..C-31)

**Variation axis**: Full combination — all 23 aspirational criteria at structurally distinct
moments. No criterion activates at the same structural step as another unless genuinely
co-dependent. Phrasing register tightened at criterion activation boundaries to prevent
ambiguity about which criterion governs each structural unit.

**Hypothesis**: C-29, C-30, and C-31 activate at non-conflicting structural positions — C-30
at every role sub-step (execution time), C-29 at audit-step output (post-audit, before chain
trace), C-31 at chain-trace write (output time). All three coexist with the 20 prior criteria
without structural collisions. Their combination closes the audit trail at three distinct
layers: sub-step epistemic posture (C-30), verification auditability (C-29), and dependency
graph completeness (C-31). The full 23-criterion combination produces an artifact auditable
from sub-step execution through the final dependency graph.

**Builds on**: V-04 (C-29 + C-30 + C-31 verified in combination).

**New over V-04**: Full criterion inventory with explicit activation tags at all 23 activation
points. C-30 shorthands extended to all sub-steps across all steps. C-29 verdict tokens at
Steps 10 and 11. C-31 dependency annotations in Step 12 close all inter-criterion loops.

---

You are running `/quest:topic echo` for the topic: {topic}.

All essential signals are in hand. Your task: surface the genuine surprises — findings that
only became visible in retrospect, from cross-signal tension, that no competent practitioner
would have predicted before gathering evidence.

Not a summary. Not a survey of discoveries. An echo: the signal that comes back that you
didn't send.

---

### Roles *(C-25: two distinct named roles; C-30: sub-step identity+function co-activation)*

**Institutional Archaeologist (IA)**
*First invocation: Step 2.*
Function: Recovers false assumptions embedded in current materials — what a future team
would carry as truth without knowing otherwise. Frames every surprise as a correction to a
false assumption (C-17), not a description of a discovery. Derives consequence by asking
"What would the next team build wrong?" (C-18, C-22). The IA is the author of implication;
the Gatekeeper is the author of rejection.

Sub-step co-activation shorthand *(C-30)*: `IA: false-assumption-recovery`
Appears at every sub-step IA governs — identity and function simultaneously, no look-back.

Active: Steps 2, 5, 7, 8, 9.

**Gatekeeper**
*First invocation: Step 3.*
Sub-step co-activation shorthand *(C-30)*: `Gatekeeper: adversarial-rejection-only`

```
GATEKEEPER — FUNCTION DECLARATION (C-27)
─────────────────────────────────────────────────────────────────────────
Function:      Adversarial rejection. Tests each gate-pipeline candidate: (1)
               first-principles predictability — could a competent practitioner
               have predicted this before any signal gathering? (2) cross-signal
               requirement — does this finding emerge only when >=2 artifacts
               are read together? Fails either: rejected.

Not-function:  Future-reader framing. The Gatekeeper does not ask what the
               next team would get wrong. That is the IA's domain.

Not-function:  Thematic synthesis or cross-item grouping. The Gatekeeper
               evaluates each candidate in isolation.

Role boundary: Gatekeeper verdicts are final. The IA cannot reverse a rejection.
               The Gatekeeper tests the candidate; the IA frames the implication.
─────────────────────────────────────────────────────────────────────────
```

Active: Step 3 only.

---

### Step 1 — Read Signal Record *(C-10: multi-namespace coverage; C-12: temporal marking)*

Read all signal artifacts in the topic signal folder across all namespaces (scout, draft,
review, flow, trace, prove, listen, program, topic).

Record:
- Namespaces covered — must reach >=3 distinct namespaces (C-10 floor)
- Total artifacts read
- Date range (earliest -> latest) — temporal anchor source for C-12 per entry

---

### Step 2 — Pre-Write Prediction Sort
*(IA: false-assumption-recovery; C-16: structurally-enforced filter; C-14: downstream
routing; C-11: anti-hypothesis guard; C-09: discard visibility)*

Assign a typed route to every finding. The route is a structural verdict enforced before any
candidate proceeds to the gate *(C-16)*.

Route types:
- `topic-story` — confirms hypothesis; destination: topic narrative *(C-14)*
- `topic-report` — restates known constraint; destination: report *(C-14)*
- `gate-pipeline` — candidate surprise; proceeds to Step 3

Anti-hypothesis guard *(C-11; IA: false-assumption-recovery)*: "Does this item confirm what
the investigation set out to prove?" YES -> `topic-story`, regardless of apparent novelty.

Pre-expansion co-validation *(C-20 partial; IA: false-assumption-recovery)*: for each
`gate-pipeline` item: "A new team from the spec alone would not have encountered this."
Cannot confirm -> `topic-report`.

Discard log *(C-09; IA: false-assumption-recovery)*: every item routed to `topic-story` or
`topic-report` with route type, reason (1 sentence), downstream destination *(C-14)*.

Non-empty discard log required. Empty log indicates filter was not applied.

---

### Step 3 — Multi-Stage Epistemic Gate
*(Gatekeeper: adversarial-rejection-only; C-13: typed skeptic gate; C-15: minimum surprise
floor; C-16: structurally-enforced filter)*

```
GATEKEEPER: adversarial-rejection-only — active from here through end of Stage 3.
```

**Anti-Pattern Catalog** *(C-13; Gatekeeper: adversarial-rejection-only — per candidate)*:
- CONFIRMATION: confirms original hypothesis even if unpredicted -> verdict PREDICTABLE
- RESTATEMENT: documents known constraint or spec requirement -> route `topic-report`
- ISOLATED-FINDING: finding complete in one artifact; no cross-signal emergence -> route `topic-report`

**Gate format** *(C-16)*: each candidate receives typed verdict token before expansion.
Format: `VERDICT: SURPRISE | CUT — {anti-pattern label if CUT}`.

**Three sequential stages. Per-stage commit required. Collapse prohibition: do not write a
combined multi-stage verdict. Each stage result is a written artifact before the next begins.**

---

**Stage 1 — Prediction Test** *(Gatekeeper: adversarial-rejection-only; epistemic dimension: novelty)*

"Would a competent practitioner have predicted this from first principles, prior to any
signal gathering?"

Anti-hypothesis re-check *(C-11)*: confirms the investigation's starting hypothesis?
-> PREDICTABLE regardless.

`PREDICTABLE` -> route to `topic-story`; discard log
`UNPREDICTABLE` -> Stage 2

**Commit**: `Stage 1: [{item label}] -> [PREDICTABLE | UNPREDICTABLE]`

---

**Stage 2 — Contradiction Test** *(Gatekeeper: adversarial-rejection-only; epistemic dimension: opposition)*

"Does this item contradict, complicate, or qualify an assumption from the pre-investigation
frame?"

```
We believed: {falsifiable pre-investigation assumption — names a specific belief held}
VALID: {case that genuinely falsifies the belief — names belief and contradiction}
INVALID (absence-of-consideration): {notes absence rather than falsifying a held belief}
INVALID (sentiment-reaction): {expresses surprise without naming the assumption that
   turned out to be false}
INVALID (hedge-uncertainty): {hedges on whether the belief was ever held}
```

Minimum surprise floor *(C-15)*: >=3 candidates must reach CONTRADICTION FOUND.
If fewer than 3, record as floor-miss. Do not suppress it.

`NO CONTRADICTION` -> route to `topic-report`; discard log
`CONTRADICTION FOUND` -> Stage 3

**Commit**: `Stage 2: [{item label}] -> [NO CONTRADICTION | CONTRADICTION FOUND]`

---

**Stage 3 — Attribution Test** *(Gatekeeper: adversarial-rejection-only; epistemic dimension: specificity)*

"Does this finding emerge only when two or more signal artifacts are read together, or does
it exist complete in a single artifact in isolation?"

`SINGLE-ARTIFACT` -> route to `topic-report`; discard log
`CROSS-SIGNAL (cite >=2 source artifacts)` -> verdict SURPRISE

**Commit**: `Stage 3: [{item label}] -> [SINGLE-ARTIFACT | CROSS-SIGNAL] — sources:
[{artifact1 (namespace/skill)}, {artifact2 (namespace/skill)}]`

---

### Step 4 — Pre-Write Impact Triage *(C-23: triage as pre-write scaffolding; C-22: failure-first ordering)*

Assign each SURPRISE candidate a tier comparatively — evaluate all candidates against each
other before assigning any tier. No tier assigned in isolation.

- **HIGH**: Forces revision to core design decision, assumption, or scope boundary
- **MEDIUM**: Qualifies design principle or adds constraint to existing decision
- **LOW**: Notable; no clear design consequence at present

*(C-22)*: Within each tier, failure-first ordering — candidate with highest failure-if-wrong
risk goes first. "If we carry the old assumption on this candidate, what is the severity of
the resulting mis-design?" Order by severity (highest first) within tier.

Record all triage assignments before writing any entry.
Write order: HIGH -> MEDIUM -> LOW; within tier: failure-first *(C-22)*.

---

### Step 5 — Naming Scaffold *(C-17: correction-encoding names; C-21: derivation scaffold; IA: false-assumption-recovery)*

For each SURPRISE candidate, work through the scaffold before writing the entry header
*(IA: false-assumption-recovery)*. Do not skip to name formation.

1. State old belief: "The team carried the assumption that ___."
2. State correction: "The signals revealed instead that ___."
3. Derive domain: "This affects the ___ area of the design."
4. Form label: `The {Corrected Belief}: {Domain}`

VALID: "The Silent Veto: Adoption Workflow" — encodes what was wrong and where.
INVALID: "Surprising Finding About Adoption" — describes discovery category, not corrected belief.

Output of step 4 feeds directly into the entry header.

---

### Step 6 — Pre-Expansion Co-Validation Gate *(C-20; IA: false-assumption-recovery)*

Before expanding any entry, co-validate simultaneously *(IA: false-assumption-recovery)*.
Both must be VALID. Either failing blocks expansion — revise before proceeding.

- **Name form** *(C-17)*: does the label follow `The {Corrected Belief}: {Domain}`?
  -> VALID / INVALID

- **Failure field** *(C-18)*: does the failure read as "If the next team carries the old
  assumption, {specific concrete mis-design}" — named mis-design, not change-list?
  -> VALID / INVALID

Gate runs once per candidate. VALID gate is pre-condition for Step 7 expansion.

---

### Step 7 — Write Echo Entries
*(IA: false-assumption-recovery; triage order; failure-first within tier; C-04; C-02; C-03;
C-08; C-12; C-14; C-17; C-18; C-22)*

Entry production sequence *(C-22; IA: false-assumption-recovery)*: begin from failure
scenario, then derive signal tracing, naming, and impact. The failure is load-bearing.

---

**Begin from failure** *(IA: false-assumption-recovery)*: If the next team carries the old
assumption about {domain}, they would {specific mis-design}. Anchor.

**[SURPRISE NAME: `The {Corrected Belief}: {Domain}`]** — *{HIGH | MEDIUM | LOW}*
*(IA: false-assumption-recovery)*

Source signal: `{artifact-name} ({namespace}/{skill})`
*(C-02: cite all sources; precision sufficient to retrieve)*
`[CROSS: {artifact-A} x {artifact-B}]` *(C-08)*

Temporal anchor *(C-12)*: `{round or date of earliest contributing signal}`

We believed: `{falsifiable pre-investigation assumption}`

The surprise: `{what signals revealed that contradicts the prior assumption}`

If the next team carries the old assumption *(C-18)*: `{specific concrete mis-design — the
exact wrong construction that follows from the false assumption}`.

Design impact *(C-03)*: `{one of: decision revisited / assumption struck / scope boundary
shifted — name the specific decision, assumption, or boundary}`.

Downstream route *(C-14)*: `-> {skill or namespace — name the specific consumer}`.

---

### Step 8 — Cross-Signal Synthesis *(C-05; IA: false-assumption-recovery)*

One paragraph, <=120 words.

*(IA: false-assumption-recovery)*: Name >=2 SURPRISE entries by their labels. Explain what
only emerges from reading those entries together — unreachable from any single entry alone.

C-05 definitional line: a finding in one artifact is a finding; a surprise visible only when
two signals are read together is an echo. Do not summarize; synthesize the cross-entry tension.

---

### Step 9 — Forward Handover Guidance *(C-06; C-19; IA: false-assumption-recovery)*

Select one register *(C-19; IA: false-assumption-recovery)*:

- T-1 (builder): "If you are about to build {scenario}, know that {constraint} because {source}."
- T-2 (reviewer): "Before approving {decision}, verify {constraint} against {source}."
- T-3 (PM): "Scope the {area} decision against {constraint} found in {source}."
- T-4 (architect): "The {component} design assumes {belief}; {source} shows this is false."

Select register matching most actionable downstream route from Step 7 entries.
State selected register (T-1/T-2/T-3/T-4). Verify slot assignments before writing.
Both scenario/decision/area/component and constraint must be specific. Source citable.

---

### Step 10 — Rules of Thumb *(C-07: impact magnitude; C-24: traceability closure)*

<=3 rules. HIGH and MEDIUM surprises only. LOW excluded.

```
[{HIGH | MEDIUM}] {Rule — <=20 words, quotable standalone heuristic}
(encodes: {SURPRISE NAME})
```

Traceability check *(C-24)*:
1. Each rule's tier matches named surprise's triage tier from Step 4
2. Each rule traceable to exactly one named surprise (no orphan rules)
3. No surprise generates more than one rule

Correct mismatches before writing verdict.

**Write verdict** *(C-29: traceability check as chain node with written artifact)*:

```
TRACE-CHECK-VERDICT: [PASS | FAIL]
  -- PASS: all tiers match; no orphan rules; one-rule-per-surprise confirmed
  -- FAIL: {each mismatch: rule label, expected tier from Step 4, actual tier in entry}
```

This verdict is a structural artifact. A future reader verifies the check ran by locating
this token in the output — no session replay required.

---

### Step 11 — Gestalt Summary Audit *(C-26)*

*Applied to the complete draft output (Steps 7–10) as a single unit.*

This step tests what item-level screening (Steps 3–6) structurally cannot catch.

**Audit question**: "Could this output — read as a whole, not entry by entry — be described
as a summary or survey of what the investigation found: a comprehensive review of discoveries
organized by theme or signal source?"

An output can have every entry pass item-level tests and still read in aggregate as a survey
of discoveries. The aggregate tone is what this step screens.

If YES or PARTLY YES:
- Identify entries that read as survey items in aggregate (even if they passed item-level tests)
- Revise to surface genuine cross-signal surprise, or discard
- Add to discard log: `gestalt-summary-fail` (distinct from item-level `gate-fail`)
- Re-run audit after each revision pass

**Write verdict** *(C-29: gestalt audit as chain node with written artifact)*:

```
GESTALT-VERDICT: [PASS | FAIL]
  -- PASS: output does not read as survey in aggregate; surprises are retroactively-visible
  -- FAIL: {entries revised or discarded, each with gestalt-summary-fail reason}
```

This verdict is a structural artifact auditable by the same rules as any production link.
PASS: proceed to Step 12.

---

### Step 12 — Production Chain Trace
*(C-28: full-chain with structural qualifiers; C-29: verification steps as chain nodes;
C-31: closed dependency graph)*

*Named chain links with structural qualifiers (C-28). Verification step verdicts are
first-class chain nodes (C-29) — not exempt meta-gates. All inter-criterion
output-to-input dependencies explicitly annotated — no dependency is discoverable only by
reading the prompt (C-31).*

```
PRODUCTION CHAIN TRACE
VERIFICATION NODES INCLUDED (C-29) | DEPENDENCY GRAPH CLOSED (C-31)
══════════════════════════════════════════════════════════════════════

[NODE 1] typed-route prediction sort
  structural qualifier: IA: false-assumption-recovery co-validation per route (C-30),
    anti-hypothesis guard per candidate (C-11), typed downstream destination per
    discard (C-14), non-empty discard log as structural requirement (C-09)
  produces: typed route decisions (C-16), discard log with destinations (C-09+C-14)
  consumed by: NODE 2 (receives gate-pipeline candidates only)

-> [NODE 2] staged gate verdict
  structural qualifier: Gatekeeper: adversarial-rejection-only at each Stage header
    (C-30), per-stage written commit tokens with collapse prohibition (C-13+C-16),
    falsifiable "We believed:" + VALID/INVALID contrast gallery per Stage 2 (C-18
    scaffolding), cross-signal citation per Stage 3 SURPRISE (C-08 prereq), minimum
    floor tracked (C-15)
  produces: SURPRISE verdicts (C-13/C-16), floor count (C-15)
  consumed by: NODE 3 (confirmed SURPRISE candidates for triage)

-> [NODE 3] comparative triage rank
  structural qualifier: all candidates evaluated simultaneously before any single
    tier assigned (C-23), failure-first ordering within tier by mis-design severity
    (C-22), all tiers recorded as written artifact before expansion begins
  produces: HIGH/MEDIUM/LOW triage assignments (C-23), within-tier order (C-22)
  consumed by: NODE 4 entry headers (C-07: tier labels require C-23 output)
               NODE 8 TRACE-CHECK-VERDICT (C-24: tier-match check requires C-23 output)

-> [NODE 4] echo entry
  structural qualifier: IA: false-assumption-recovery at each sub-step (C-30); name
    from 4-step derivation scaffold (C-17+C-21); failure-first production (C-22);
    [CROSS: A x B] annotation (C-08); failure field as concrete mis-design not
    change-list (C-18); design impact names decision/assumption/scope (C-03)
  produces: named surprise labels (C-04), source citations (C-02), design impact
            statements (C-03), routing tags (C-14)
  consumed by: NODE 5 synthesis (C-05: requires >=2 labeled surprises by name)
               NODE 6 handover (C-06: requires named scenario from C-14 routing)
               NODE 7 rules (C-24: requires named surprise per rule)

-> [NODE 5] cross-signal synthesis
  structural qualifier: >=2 named surprise labels cited by exact label, cross-entry
    pattern stated as unreachable from single entry alone (C-05 definitional line)
  produces: synthesized echo paragraph (C-05)
  consumed by: output (terminal)

-> [NODE 6] forward handover guidance
  structural qualifier: register selected from T-1..T-4 menu (C-19), register stated
    before writing, slot assignments verified (C-06), source citable (C-06)
  produces: register-anchored handoff statement (C-06+C-19)
  consumed by: output (terminal)

-> [NODE 7] impact-anchored rule
  structural qualifier: tier verified against NODE 3 triage by explicit check (C-24),
    orphan rule check, one-rule-per-surprise constraint
  produces: verified rules with tier labels (C-07+C-24)
  consumed by: NODE 8 TRACE-CHECK-VERDICT (C-24 requires rules as input for check)

-> [NODE 8] TRACE-CHECK-VERDICT [C-29: traceability check as chain node]
  structural qualifier: written PASS|FAIL token produced by explicit tier-match step
    at end of Step 10, before output written; verifiable by locating token in output
    without session replay; records each mismatch if FAIL
  produces: traceability audit result (C-24+C-29 joint output)
  consumed by: NODE 11 chain trace (C-28+C-31: TRACE-CHECK-VERDICT is named node;
               C-23->C-24->NODE 8 dependency loop is explicitly closed here)

-> [NODE 9] gestalt audit
  structural qualifier: IA: false-assumption-recovery applied to complete artifact as
    unit, not entry-by-entry (C-26+C-30); gestalt-summary-fail discards logged
    separately from item-level gate-fail (C-26)
  produces: gestalt audit result (C-26)
  consumed by: NODE 10 GESTALT-VERDICT (C-29: audit step produces named verdict)

-> [NODE 10] GESTALT-VERDICT [C-29: gestalt audit as chain node]
  structural qualifier: written PASS|FAIL token produced by explicit audit question
    in Step 11; verifiable by locating token in output; records revised/discarded
    entries if FAIL; distinct from NODE 8 verdict (scope: gestalt not traceability)
  produces: gestalt audit result (C-26+C-29 joint output)
  consumed by: NODE 11 chain trace (C-28+C-31: GESTALT-VERDICT is named chain node;
               this closes the archetypal C-31 loop: C-26 output -> C-28 node)

-> [NODE 11] production chain trace (this node)
  structural qualifier: all nodes named with qualifiers verifiable from output alone
    without session access (C-28); verification verdicts are chain nodes not meta-
    gates (C-29); all inter-criterion output-to-input relationships explicitly
    annotated — graph is closed (C-31)
  produces: closed, auditable dependency graph
  consumed by: output (terminal)

══════════════════════════════════════════════════════════════════════
Missing link protocol: Name any absent node as ABSENT with reason. Absent
nodes are auditable facts; omitting them creates a false audit trail.

Structural qualifier protocol (C-28): each parenthetical names a property
verifiable from the output alone, not from session memory.

Verification node protocol (C-29): TRACE-CHECK-VERDICT (NODE 8) and
GESTALT-VERDICT (NODE 10) are chain nodes auditable by the same rules as
any production link.

Dependency closure verification (C-31): the following inter-criterion loops
are explicitly closed in the trace above:
  C-23 output -> C-24 (NODE 3 -> NODE 8): triage rank feeds tier-match check
  C-26 output -> C-28 (NODE 9 -> NODE 10 -> NODE 11): gestalt verdict is chain node
  C-24 output -> C-28 (NODE 8 -> NODE 11): traceability verdict is chain node
  C-14 output -> C-06 (NODE 4 -> NODE 6): routing feeds handover scenario selection
  C-17+C-21 output -> C-20 (Step 5 -> Step 6): naming scaffold feeds co-validation
No inter-criterion dependency is discoverable only by reading the prompt.
```

---

**Output**: Steps 7–12 only. Steps 1–6 are execution scaffolding not included in output.

Final output sequence:
1. Echo entries (triage-ordered, failure-first within tier)
2. Cross-signal synthesis
3. Forward handover guidance (with register selection stated)
4. Rules of Thumb
5. TRACE-CHECK-VERDICT (from Step 10)
6. GESTALT-VERDICT (from Step 11)
7. Production chain trace with dependency graph

Minimum surprise floor check *(C-15)*: if fewer than 3 distinct surprises in the final
output, note the floor-miss before closing. Do not suppress it.
