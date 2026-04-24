---
skill: quest-variate
skill_target: topic-echo
date: 2026-03-15
round: 7
rubric: v7
---

# Variations: `topic:echo` — Round 7

**Rubric:** v7 | **Date:** 2026-03-15

---

## Design Context

R6 differentiating evidence: three structural patterns from R6 V-05 were observable but not
formalized as criteria in that round:

1. **R6 V-01 item-level gap**: V-01's multi-stage gate passed all individual entry tests but the
   aggregate artifact was retroactively scored as a survey of discoveries rather than a curated
   set of surprises. The item-level filter (C-01) cannot catch summary-in-disguise at the
   artifact level — an output can have every entry pass the prediction test and still read in
   aggregate as "here is what we found." C-26 closes this gap with a dedicated gestalt test
   applied to the complete output as a unit, after all entries are drafted.

2. **R6 V-04 → V-05 function declaration evolution**: V-04 declared the Gatekeeper via identity
   contrast — "(not the Institutional Archaeologist)." This names *identity* but not *function*.
   V-05 improved this in prose, but the function declaration remained in the preamble and was
   not placed at the role's first invocation point. A model executing the prompt knows that
   Gatekeeper and IA are different but not what the Gatekeeper is *for*. C-27 formalizes the
   pattern: a FUNCTION DECLARATION block placed at or near the Gatekeeper's first invocation,
   stating both what it does and what it does not do as a structural constraint — making the
   boundary structurally clear rather than nominally clear.

3. **Traceability chain underspecification**: C-24 (end-to-end traceability closure) names the
   production chain links and verifies triage-to-header alignment. But the links were named
   without structural qualifiers — "typed-route prediction sort → staged gate verdict →
   comparative triage rank → echo entry → impact-anchored rule" names the links but not what
   makes each link independently auditable. A future reader cannot verify any link without
   re-running the session. C-28 requires each link to carry its structural qualifier in
   parentheses, enabling independent verification from the trace statement alone.

These three patterns became C-26, C-27, and C-28 in v7. Aspirational criteria grew from 17
(C-09..C-25) to 20 (C-09..C-28), yielding a total rubric score of 60 + 21 + 60 = 141.

**Strategy for R7 variations:**
- V-01: Single-axis — C-26 (output-level gestalt summary test)
- V-02: Single-axis — C-27 (adversarial function declaration)
- V-03: Single-axis — C-28 (full-chain traceability with structural qualifiers)
- V-04: Combination — C-26 + C-27 + C-28
- V-05: Full combination — all 20 aspirational criteria (C-09..C-28)

---

## V-01 — Gestalt Audit Axis (C-26)

**Variation axis**: Lifecycle emphasis — add a gestalt-level summary audit after all entries
are drafted, before the output is finalized.

**Hypothesis**: Item-level tests (the per-entry prediction gate) cannot catch an output that
reads in aggregate as a survey of discoveries. A dedicated gestalt audit step applied to the
complete draft artifact as a unit catches summary-in-disguise that passes all item screening
and closes the artifact-level gap C-26 targets.

**Builds on**: R6 V-04 style — two roles, routing layer, multi-stage gate, pre-write triage,
entries with failure framing, synthesis, handover, rules of thumb.

**New element targeting C-26**: Step 9 — Gestalt Summary Audit.

---

You are running `/quest:topic echo` for the topic: {topic}.

All essential signals are in hand. Your task is to surface what those signals revealed that
no competent practitioner would have predicted before the investigation began.

This is not a summary. This is not a survey of discoveries. This is an echo: the signal that
only becomes visible in retrospect, from cross-signal tension.

---

### Roles

**Institutional Archaeologist (IA)** — active in Steps 2, 5, 6, 7, 8.
Holds the perspective of a future team approaching this topic fresh. The IA asks: what false
assumptions would that team carry? What would they build wrong because they didn't know what
you now know?

**Gatekeeper** — active in Step 3.
Runs adversarial rejection. The Gatekeeper tests whether each candidate was predictable from
first principles before signal gathering and whether it emerges from cross-signal tension or
from a single artifact in isolation.

---

### Step 1 — Read Signal Record

Read all signal artifacts in the topic's signal folder, spanning all namespaces (scout, draft,
review, flow, trace, prove, listen, program, topic). Record namespace coverage (count of
distinct namespaces reached).

---

### Step 2 — Pre-Write Prediction Sort *(IA perspective; C-16)*

Assign a typed route to every finding before proceeding:

- `topic-story` — confirms a working hypothesis; routes downstream to topic narrative
- `topic-report` — restates a known constraint or documents a requirement; routes to report
- `gate-pipeline` — candidate surprise; not in pre-investigation frame; routes to Step 3

IA co-validation: for each `gate-pipeline` candidate, confirm: "A new team approaching this
topic from the spec alone would not have encountered this finding."

Discard log *(C-09)*: record every finding routed to `topic-story` or `topic-report` with
its route reason. A non-empty discard log is a prerequisite; an empty log indicates the
filter was not applied.

---

### Step 3 — Multi-Stage Epistemic Gate *(Gatekeeper; C-13, C-16)*

Three sequential stages. Write each stage verdict before proceeding to the next. Do not
collapse stages into a combined verdict.

**Anti-Pattern Catalog** — Skeptic applies per candidate:
- CONFIRMATION: item confirms original hypothesis; verdict PREDICTABLE regardless of stage
- RESTATEMENT: item documents a known constraint; route to `topic-report`
- ISOLATED-FINDING: item exists in one artifact; no cross-signal emergence; route to `topic-report`

**Stage 1 — Prediction Test**
Gate question: "Would a competent practitioner have predicted this from first principles,
prior to any signal gathering?"

`PREDICTABLE` → route to `topic-story`; log in discard log
`UNPREDICTABLE` → proceed to Stage 2

Verdict: `Stage 1: [{item}] → [PREDICTABLE | UNPREDICTABLE]`

**Stage 2 — Contradiction Test**

Gate question: "Does this item contradict, complicate, or qualify an assumption from the
pre-investigation frame?"

We believed: `{falsifiable pre-investigation assumption}`
VALID: `{case that genuinely falsifies the belief — names the specific assumption contradicted}`
INVALID (absence-of-consideration): `{notes absence of something rather than falsifying a held belief}`
INVALID (sentiment-reaction): `{expresses surprise without naming the contradicted assumption}`

`NO CONTRADICTION` → route to `topic-report`; log in discard log
`CONTRADICTION FOUND` → proceed to Stage 3

Verdict: `Stage 2: [{item}] → [NO CONTRADICTION | CONTRADICTION FOUND]`

**Stage 3 — Attribution Test**

Gate question: "Does this finding emerge from cross-signal reading, or from one artifact alone?"

`SINGLE-ARTIFACT` → route to `topic-report`; log in discard log
`CROSS-SIGNAL (cite ≥2 artifacts)` → verdict SURPRISE

Verdict: `Stage 3: [{item}] → [SINGLE-ARTIFACT | CROSS-SIGNAL] — sources: [{artifact1 (ns/skill)}, {artifact2 (ns/skill)}]`

---

### Step 4 — Pre-Write Impact Triage *(C-23)*

Assign each SURPRISE candidate a tier comparatively — compare all candidates against each
other before assigning any tier. No tier is assigned in isolation.

- **HIGH**: Forces revision to a core design decision, assumption, or scope boundary
- **MEDIUM**: Qualifies a design principle or adds a constraint to an existing decision
- **LOW**: Notable but no clear design consequence at present

Record triage assignments. Write entries HIGH → MEDIUM → LOW.

---

### Step 5 — Naming Scaffold *(C-17, C-21)*

For each SURPRISE candidate, derive the name before writing the entry:

1. State the old belief: "The team carried the assumption that ___."
2. State the correction: "The signals revealed instead that ___."
3. Derive the domain: "This affects the ___ area of the design."
4. Form the label: `The {Corrected Belief}: {Domain}`

VALID: "The Silent Veto: Adoption Workflow"
INVALID: "Surprising Finding About Adoption"

---

### Step 6 — Pre-Expansion Co-Validation Gate *(C-20)*

Before expanding any entry, co-validate two fields simultaneously:

- **Name form** (C-17): does the label follow `The {Corrected Belief}: {Domain}`?
- **Failure field** (C-18): does the failure read as "If the next team carries the old
  assumption, {specific concrete failure}" — a named mis-design, not a change-list?

Both must be VALID. If either fails, revise before expanding. A failed co-validation blocks
entry expansion.

---

### Step 7 — Write Echo Entries *(IA perspective; in triage order)*

For each SURPRISE candidate (HIGH → MEDIUM → LOW):

---

**[SURPRISE NAME]** — *{HIGH | MEDIUM | LOW}*

Source signal: `{artifact-name} ({namespace}/{skill})`
*(If multiple sources: list all; C-08: annotate as `[CROSS: {artifact-A} × {artifact-B}]`)*

Temporal anchor *(C-12)*: `{round or date of earliest source signal}`

We believed: `{falsifiable pre-investigation assumption}`

The surprise: `{what the signals revealed that contradicts or complicates the prior assumption}`

If the next team carries the old assumption *(C-18)*: `{specific concrete failure — the
mis-design that results}`.

Downstream route *(C-14)*: `→ {topic-story | draft-proposal | trace-component | other skill}`

---

### Step 8 — Cross-Signal Synthesis *(C-05)*

One paragraph, ≤120 words.

Name ≥2 SURPRISE entries by their labels and explain why the pattern only emerges from
reading those entries together — it cannot be derived from any single entry alone.

This is the definitional line: a finding that lives in one artifact is a finding; a surprise
that only becomes visible when two signals are read together is an echo.

---

### Step 9 — Forward Handover Guidance *(C-06)*

One handover statement addressed to the next team at the start of their investigation:

"If you are about to build {specific construction scenario}, know that {concrete constraint}
because {artifact-name} ({namespace}/{skill})."

Scenario must be specific; source must be citable.

---

### Step 10 — Rules of Thumb *(C-24)*

≤3 rules. HIGH and MEDIUM surprises only. LOW surprises do not generate rules.

```
[{HIGH | MEDIUM}] {Rule — ≤20 words, quotable as standalone heuristic}
(encodes: {SURPRISE NAME})
```

Traceability check *(C-24)*: verify that each rule's impact tier matches the named surprise's
triage tier assigned in Step 4. If mismatch: correct before proceeding.

---

### Step 11 — Gestalt Summary Audit *(C-26)*

*This step tests the complete draft output (Steps 7–10) as a single unit.*

**Audit question**: "Could this output — read as a whole, not entry by entry — be described
as a survey of what the investigation found?"

This is an artifact-level test. Item-level tests (Steps 3–6) screen individual entries. This
step screens the artifact gestalt. An output that passes all item-level tests can still fail
this test if, in aggregate, the entries read as a comprehensive review of discoveries rather
than a curated set of retroactively-visible surprises.

If YES or PARTLY YES:
- Identify which entries read as survey items (even if they passed item-level tests)
- Revise to surface the genuine cross-signal surprise, or discard
- Record discarded items in the discard log with reason: `gestalt-summary-fail`
- Re-run audit after revision

If NO: proceed to output.

---

**Output**: Steps 7–11 only. Steps 1–6 and the Step 11 result are scaffolding.

Sequence: Echo entries (triage-ordered) → Cross-signal synthesis → Forward handover →
Rules of Thumb → Gestalt audit note (if any items were revised or discarded).

---

---

## V-02 — Adversarial Function Declaration Axis (C-27)

**Variation axis**: Role sequence — Gatekeeper function declaration placed at first
invocation point (Step 3 header), not only in a preamble.

**Hypothesis**: Placing an explicit FUNCTION DECLARATION block at the Gatekeeper's first
invocation — stating both what the role does and what it does not do — prevents role
conflation at execution time. A model executing this prompt knows not just that Gatekeeper
and IA are different identities, but what the Gatekeeper is *for* and what it is explicitly
*not for*, making the boundary structurally enforced rather than nominally noted.

**Builds on**: R6 V-04 style — two roles, routing layer, multi-stage gate, triage, failure
framing, co-validation gate, synthesis, handover, rules of thumb.

**New element targeting C-27**: FUNCTION DECLARATION block at the exact point where the
Gatekeeper is first invoked (Step 3 header), distinct from and in addition to role preamble.

---

You are running `/quest:topic echo` for the topic: {topic}.

All essential signals are in hand. Your task: surface what those signals revealed that no
competent practitioner would have predicted before the investigation began.

This is not a summary. This is an echo: the signal that only becomes visible in retrospect,
from cross-signal tension.

---

### Roles

**Institutional Archaeologist (IA)**: Recovers false assumptions embedded in the current
materials — what a future team would carry without knowing they are false. Frames every
surprise as a correction to a false assumption, not a description of a discovery. Active in
Steps 2, 5, 6, 7, 8.

**Gatekeeper**: Introduced at Step 3. Function declaration at first invocation. See below.

---

### Step 1 — Read Signal Record

Read all signal artifacts across all namespaces. Record namespace coverage.

---

### Step 2 — Pre-Write Prediction Sort *(IA; C-16)*

Typed route for every finding:

- `topic-story` — confirms hypothesis
- `topic-report` — restates known constraint
- `gate-pipeline` — candidate surprise; not in pre-investigation frame

IA co-validation: confirm each `gate-pipeline` item was not derivable from the spec alone.

Discard log *(C-09)*: record all routed items with route reason.

---

### Step 3 — Multi-Stage Epistemic Gate

The Gatekeeper is invoked here for the first time.

```
GATEKEEPER — FUNCTION DECLARATION (C-27)
─────────────────────────────────────────────────────────────────
Function:      Adversarial rejection. Tests each gate-pipeline candidate
               against first-principles predictability and cross-signal
               requirement. A competent practitioner could have predicted
               it? Rejected. It traces to one artifact? Rejected.

Not-function:  Future-reader framing. The Gatekeeper does not ask what a
               future team would get wrong — that is the Institutional
               Archaeologist's domain. The IA's perspective on rejected
               items is not consulted.

Not-function:  Thematic synthesis. The Gatekeeper does not group, relate,
               or narrate findings. It evaluates each candidate in isolation.

Role boundary: Items rejected by the Gatekeeper are not surprises, period.
               The IA cannot reverse a gate rejection. The boundary is
               structural: one role tests plausibility, the other frames
               implication. They do not overlap.
─────────────────────────────────────────────────────────────────
```

*[Gatekeeper]* Three sequential stages. Per-stage commit before proceeding. No collapsed verdicts.

**Anti-Pattern Catalog** *(C-13)*: Gatekeeper applies per candidate —
- CONFIRMATION: confirms original hypothesis → PREDICTABLE regardless of stage
- RESTATEMENT: restates known constraint → route to `topic-report`
- ISOLATED-FINDING: exists in one artifact → route to `topic-report`

**Stage 1 — Prediction Test** *(Gatekeeper)*
"Would a competent practitioner have predicted this from first principles?"
`PREDICTABLE` → discard | `UNPREDICTABLE` → Stage 2
Commit: `Stage 1: [{item}] → [{verdict}]`

**Stage 2 — Contradiction Test** *(Gatekeeper)*
"Does this contradict or complicate the pre-investigation frame?"
We believed: `{falsifiable assumption}`
VALID: `{genuine falsification}` | INVALID: `{not a falsification — describe type}`
`NO CONTRADICTION` → discard | `CONTRADICTION FOUND` → Stage 3
Commit: `Stage 2: [{item}] → [{verdict}]`

**Stage 3 — Attribution Test** *(Gatekeeper)*
"Does this emerge from cross-signal reading or from one artifact alone?"
`SINGLE-ARTIFACT` → discard | `CROSS-SIGNAL (cite ≥2)` → verdict SURPRISE
Commit: `Stage 3: [{item}] → [{verdict}] — sources: [{artifact1}, {artifact2}]`

---

### Step 4 — Pre-Write Impact Triage *(C-23)*

Comparative HIGH/MEDIUM/LOW across all SURPRISE candidates before writing any entry.

- HIGH: Forces revision to design decision, assumption, or scope boundary
- MEDIUM: Qualifies principle or adds constraint
- LOW: Notable; no clear design consequence

Write entries HIGH → MEDIUM → LOW.

---

### Step 5 — Naming Scaffold *(C-17, C-21)*

For each candidate:
1. State the old belief
2. State the correction
3. Derive the domain
4. Form: `The {Corrected Belief}: {Domain}`

---

### Step 6 — Pre-Expansion Co-Validation Gate *(C-20)*

Co-validate *simultaneously* before expanding any entry:
- Name form passes `The {Corrected Belief}: {Domain}` template (C-17)
- Failure field reads as "If the next team carries the old assumption, {specific mis-design}" (C-18)

Both VALID to proceed. Either fails → revise, not skip.

---

### Step 7 — Write Echo Entries *(IA perspective; triage order)*

**[SURPRISE NAME]** — *{HIGH | MEDIUM | LOW}* *(IA)*

Source signal: `{artifact-name} ({namespace}/{skill})`
`[CROSS: {artifact-A} × {artifact-B}]` *(C-08 if cross-signal)*
Temporal anchor *(C-12)*: `{round or date of source signal}`

We believed: `{falsifiable pre-investigation assumption}`

The surprise: `{what signals revealed}`

If the next team carries the old assumption *(C-18)*: `{specific mis-design that results}`.

Downstream route *(C-14)*: `→ {skill or namespace}`

---

### Step 8 — Cross-Signal Synthesis *(C-05; IA)*

≤120 words. Name ≥2 SURPRISE entries. Explain why the pattern only emerges from reading
them together, not from any single entry alone.

---

### Step 9 — Forward Handover Guidance *(C-06; IA)*

"If you are about to build {specific scenario}, know that {concrete constraint}
because {artifact-name} ({namespace}/{skill})."

---

### Step 10 — Rules of Thumb *(C-24)*

≤3 rules. HIGH and MEDIUM only.

```
[{HIGH | MEDIUM}] {Rule — ≤20 words}
(encodes: {SURPRISE NAME})
```

Traceability check: each rule's tier must match its named surprise's triage tier. Correct
any mismatch before output.

---

**Output**: Steps 7–10 only.

---

---

## V-03 — Production Chain Trace Axis (C-28)

**Variation axis**: Output format — add a production chain trace with structural qualifiers
as the final verification step, after all other output is complete.

**Hypothesis**: Naming each link in the production chain with its structural qualifier in
parentheses makes each link independently auditable by a future reader without access to the
session that produced the artifact. This closes the gap where traceability is claimed by
naming links but not verifiable without re-inspecting each step.

**Builds on**: All 17 prior-round criteria active (C-09..C-25, analogous to R6 V-05 level).

**New element targeting C-28**: Step 11 — Production Chain Trace.

---

You are running `/quest:topic echo` for the topic: {topic}.

All essential signals are in hand. Surface what those signals revealed that no competent
practitioner would have predicted. Name each surprise, trace it to its source, and assess
its impact on the design direction.

Not a summary. Not a survey. An echo: the signal that comes back that you didn't send.

---

### Roles *(C-25)*

**Institutional Archaeologist (IA)** — active Steps 2, 5, 7, 8, 9.
Recovers false assumptions. Frames every surprise as a correction, not a discovery. The IA
asks: what would the next team build wrong?

**Gatekeeper** — active Step 3.
Adversarial rejection. Tests predictability from first principles and cross-signal emergence.
Function: rejection. Not-function: future-reader framing, synthesis.

Role names appear per sub-step throughout.

---

### Step 1 — Read Signal Record *(C-10, C-12)*

Read all signal artifacts across namespaces (scout, draft, review, flow, trace, prove,
listen, program, topic). Record:
- Namespaces covered (≥3 required for C-10)
- Date range of artifacts (earliest → latest) for temporal marking

---

### Step 2 — Pre-Write Prediction Sort *(IA; C-16, C-14)*

Typed route per finding:

- `topic-story` — confirms hypothesis → downstream to topic narrative
- `topic-report` — known constraint → downstream to report
- `gate-pipeline` — candidate surprise → proceeds to Step 3

*(IA)* Co-validation per `gate-pipeline` item: "A new team from the spec alone would not
have encountered this."

Anti-hypothesis guard *(C-11)*: explicit check — "Does this confirm what we set out to
prove?" Confirmed hypotheses route to `topic-story` regardless of apparent novelty.

Discard log *(C-09)*: record all routed items with typed route reason.

---

### Step 3 — Multi-Stage Epistemic Gate *(Gatekeeper; C-13)*

```
GATEKEEPER — FUNCTION DECLARATION
Function:     Adversarial rejection of predictable or single-artifact items.
Not-function: Future-reader framing (IA's domain). Synthesis (IA's domain).
```

Three stages. Per-stage commit. Collapse prohibition: do not write a combined verdict.

**Anti-Pattern Catalog** *(Gatekeeper, C-13)*:
- CONFIRMATION / RESTATEMENT / ISOLATED-FINDING → see catalog; apply per candidate

**Stage 1 — Prediction Test** *(Gatekeeper; epistemic dimension: novelty)*
"Would a competent practitioner have predicted this?"
`PREDICTABLE` → discard | `UNPREDICTABLE` → Stage 2
Commit: `Stage 1: [{item}] → [{verdict}]`

**Stage 2 — Contradiction Test** *(Gatekeeper; epistemic dimension: opposition)*
"Does this contradict or complicate the pre-investigation frame?"

We believed: `{falsifiable assumption}`
VALID example: `{genuine falsification}`
INVALID (absence-of-consideration): `{names absence, not a falsified belief}`
INVALID (sentiment-reaction): `{expresses surprise without naming assumption}`
INVALID (hedge-uncertainty): `{hedges on whether belief was ever held}`

`NO CONTRADICTION` → discard | `CONTRADICTION FOUND` → Stage 3
Commit: `Stage 2: [{item}] → [{verdict}]`

**Stage 3 — Attribution Test** *(Gatekeeper; epistemic dimension: specificity)*
"Cross-signal emergence or single-artifact?"
`SINGLE-ARTIFACT` → discard | `CROSS-SIGNAL (cite ≥2)` → SURPRISE
Commit: `Stage 3: [{item}] → [{verdict}] — sources: [{artifact1 (ns/skill)}, {artifact2}]`

---

### Step 4 — Pre-Write Impact Triage *(C-23)*

Assign HIGH/MEDIUM/LOW comparatively across all SURPRISE candidates before any expansion.

- HIGH: Forces revision to design decision, assumption, or scope boundary
- MEDIUM: Qualifies principle or adds constraint to existing decision
- LOW: Notable; no current design consequence

Within each tier: failure-first ordering *(C-22)* — the entry with highest failure-if-wrong
risk goes first within its tier.

Write entries HIGH → MEDIUM → LOW (within-tier: failure-first).

---

### Step 5 — Naming Scaffold *(C-17, C-21)*

For each candidate:
1. State the old belief: "The team carried the assumption that ___."
2. State the correction: "The signals revealed instead that ___."
3. Derive the domain: "This affects the ___ area."
4. Form: `The {Corrected Belief}: {Domain}`

---

### Step 6 — Pre-Expansion Co-Validation Gate *(C-20)*

Co-validate before expanding any entry:
- Name form passes `The {Corrected Belief}: {Domain}` (C-17) → VALID / INVALID
- Failure field is "If the next team carries the old assumption, {specific mis-design}" (C-18) → VALID / INVALID

Both VALID to proceed. Either fails → revise. Gate runs once per entry.

---

### Step 7 — Write Echo Entries *(IA; failure-first from C-22; triage order)*

Entry production sequence per candidate *(C-22)*: begin from the failure scenario, then
derive signal, name, and impact from that failure anchor.

**Start here**: If the next team carries the old assumption, {specific mis-design that
results} — then derive:

**[SURPRISE NAME: `The {Corrected Belief}: {Domain}`]** — *{HIGH | MEDIUM | LOW}* *(IA)*

Source signal: `{artifact-name} ({namespace}/{skill})`
`[CROSS: {artifact-A} × {artifact-B}]` *(C-08)*
Temporal anchor *(C-12)*: `{round or date}`

We believed: `{falsifiable pre-investigation assumption}`

The surprise: `{what signals revealed}`

If the next team carries the old assumption *(C-18)*: `{specific concrete mis-design}`.

Downstream route *(C-14)*: `→ {skill or namespace}`

---

### Step 8 — Cross-Signal Synthesis *(C-05; IA)*

≤120 words. Name ≥2 SURPRISE entries by label. Explain why the pattern only emerges from
reading them together, not from either one alone.

*(IA)* How do the current materials — collectively — create a misleading picture for a
future team arriving without context?

---

### Step 9 — Forward Handover Guidance *(C-06; C-19; IA)*

Select register from menu:
- T-1 (builder): "If you are about to build {scenario}, know that {constraint} because {source}."
- T-2 (reviewer): "Before approving {decision}, verify {constraint} against {source}."
- T-3 (PM): "Scope the {area} decision against {constraint} found in {source}."
- T-4 (architect): "The {component} design assumes {belief}; {source} shows this is false."

Select the register that matches the most actionable route from Step 7 entry downstream
routing. Verify slot assignments before writing final statement.

---

### Step 10 — Rules of Thumb *(C-24)*

≤3 rules. HIGH and MEDIUM surprises only. LOW excluded.

```
[{HIGH | MEDIUM}] {Rule — ≤20 words, quotable standalone}
(encodes: {SURPRISE NAME})
```

Traceability check *(C-24)*: for each rule, confirm tier matches the named surprise's triage
tier from Step 4. Mismatch → correct before proceeding.

---

### Step 11 — Production Chain Trace *(C-28)*

*Named chain links with structural qualifiers — independently auditable.*

Write the production chain as a verifiable record. Each link must carry its structural
qualifier in parentheses — the property that makes the link verifiable from this statement
alone, without access to the session that produced the artifact.

```
PRODUCTION CHAIN TRACE
──────────────────────────────────────────────────────────────────────
typed-route prediction sort (with IA co-validation per route decision
  and typed downstream destination for each discarded item)
→ staged gate verdict (with per-stage written commits and falsifiable
    "We believed:" field + VALID/INVALID contrast per Stage 2 candidate)
→ comparative triage rank (HIGH/MEDIUM/LOW assigned across all candidates
    simultaneously before any entry expansion begins)
→ echo entry (with correction-encoding name derived from naming scaffold
    and failure-field framed as concrete mis-design; failure-first production)
→ impact-anchored rule (tier verified against triage rank by explicit check
    in Step 10 before output)
──────────────────────────────────────────────────────────────────────
Missing link protocol: If any chain link is absent from this output,
name it as ABSENT here with reason. An absent link is an auditable fact;
omitting it from the trace creates a false audit trail.
```

---

**Output**: Steps 7–11 only. Steps 1–6 are execution scaffolding.

---

---

## V-04 — Combination (C-26 + C-27 + C-28)

**Variation axis**: Combination — lifecycle emphasis (gestalt audit, C-26) + role sequence
(function declaration at first invocation, C-27) + output format (production chain trace
with structural qualifiers, C-28).

**Hypothesis**: The three new criteria address three distinct auditing failures that operate
at different phases. C-26 catches summary-in-disguise at the artifact level (post-draft);
C-27 prevents role conflation at execution time (pre-execution, at role invocation); C-28
makes each production step independently auditable by a future reader (post-output). Together
they close artifact-level, role-level, and chain-level gaps that prior criteria leave open.

**Builds on**: All 17 prior-round criteria active. New: C-26, C-27, C-28 simultaneously.

---

You are running `/quest:topic echo` for the topic: {topic}.

All essential signals are in hand. Your task: synthesize the unexpected — what signal
gathering revealed that no competent practitioner would have predicted before the
investigation began.

Not a summary. Not a survey. An echo.

---

### Roles *(C-25)*

**Institutional Archaeologist (IA)** — active Steps 2, 5, 7, 8, 9.
Function: Recovers false assumptions — what a future team would carry as truth without
knowing otherwise. Frames every surprise as a correction to a false assumption. Asks:
"What would the next team build wrong?"

**Gatekeeper** — first invoked Step 3.

```
GATEKEEPER — FUNCTION DECLARATION (C-27)
─────────────────────────────────────────────────────────────────
Function:      Adversarial rejection. Tests each gate-pipeline candidate:
               (1) Could a competent practitioner have predicted it? If yes,
               rejected. (2) Does it emerge from a single artifact in
               isolation? If yes, rejected.

Not-function:  Future-reader framing (IA's domain, not Gatekeeper's).
               The Gatekeeper does not ask what a future team would get
               wrong — it asks whether this was predictable.

Not-function:  Thematic synthesis or cross-item grouping (IA's domain).
               The Gatekeeper evaluates each candidate in isolation.

Role boundary: Items the Gatekeeper rejects are not surprises. The IA
               cannot override a gate rejection. The boundary is structural.
─────────────────────────────────────────────────────────────────
```

---

### Step 1 — Read Signal Record *(C-10, C-12)*

Read all signal artifacts across namespaces. Record: namespaces covered (≥3), date range.

---

### Step 2 — Pre-Write Prediction Sort *(IA; C-16, C-14, C-11)*

Typed route per finding:
- `topic-story` — confirms hypothesis
- `topic-report` — known constraint
- `gate-pipeline` — candidate surprise

Anti-hypothesis guard *(C-11)*: "Does this confirm what we set out to prove?" → `topic-story`.
*(IA)* Co-validation: "A new team from the spec alone would not have encountered this."
Discard log *(C-09)*: record all routed items with typed route reason.

---

### Step 3 — Multi-Stage Epistemic Gate *(Gatekeeper; C-13)*

**Anti-Pattern Catalog** *(Gatekeeper)*: CONFIRMATION / RESTATEMENT / ISOLATED-FINDING.
Three stages. Per-stage commits. Collapse prohibition.

**Stage 1 — Prediction Test** *(Gatekeeper)*
"Would a competent practitioner have predicted this?"
`PREDICTABLE` → discard | `UNPREDICTABLE` → Stage 2
Commit: `Stage 1: [{item}] → [{verdict}]`

**Stage 2 — Contradiction Test** *(Gatekeeper)*
"Does this contradict the pre-investigation frame?"
We believed: `{falsifiable assumption}`
VALID: `{genuine falsification}`
INVALID (absence-of-consideration): `{absence, not falsification}`
INVALID (sentiment-reaction): `{surprise without named assumption}`
INVALID (hedge-uncertainty): `{hedges on whether belief was held}`
`NO CONTRADICTION` → discard | `CONTRADICTION FOUND` → Stage 3
Commit: `Stage 2: [{item}] → [{verdict}]`

**Stage 3 — Attribution Test** *(Gatekeeper)*
"Cross-signal or single-artifact?"
`SINGLE-ARTIFACT` → discard | `CROSS-SIGNAL (cite ≥2)` → SURPRISE
Commit: `Stage 3: [{item}] → [{verdict}] — sources: [{artifact1 (ns/skill)}, {artifact2}]`

---

### Step 4 — Pre-Write Impact Triage *(C-23)*

Comparative HIGH/MEDIUM/LOW across all candidates before any expansion.
HIGH → MEDIUM → LOW; within tier: failure-first *(C-22)*.

---

### Step 5 — Naming Scaffold *(C-17, C-21)*

1. State old belief  2. State correction  3. Derive domain  4. Form: `The {Corrected Belief}: {Domain}`

---

### Step 6 — Pre-Expansion Co-Validation Gate *(C-20)*

Both simultaneously before expanding any entry:
- Name form valid per C-17?
- Failure field reads as concrete mis-design per C-18?
Both VALID → expand. Either fails → revise.

---

### Step 7 — Write Echo Entries *(IA; failure-first; triage order; C-22)*

Begin from failure scenario (C-22), then derive:

**[SURPRISE NAME: `The {Corrected Belief}: {Domain}`]** — *{HIGH | MEDIUM | LOW}* *(IA)*

Source signal: `{artifact-name} ({namespace}/{skill})`
`[CROSS: {artifact-A} × {artifact-B}]` *(C-08)*
Temporal anchor *(C-12)*: `{round or date}`
We believed: `{falsifiable assumption}`
The surprise: `{what signals revealed}`
If the next team carries the old assumption *(C-18)*: `{specific mis-design}`.
Downstream route *(C-14)*: `→ {skill or namespace}`

---

### Step 8 — Cross-Signal Synthesis *(C-05; IA)*

≤120 words. Name ≥2 surprises. Explain what only emerges from reading them together.
*(IA)*: How do the current materials collectively mislead a future team?

---

### Step 9 — Forward Handover Guidance *(C-06; C-19; IA)*

Register menu (C-19): T-1 (builder) / T-2 (reviewer) / T-3 (PM) / T-4 (architect).
Select register matching most actionable downstream route. Verify slot assignments.

---

### Step 10 — Rules of Thumb *(C-24)*

≤3 rules. HIGH and MEDIUM only.
```
[{HIGH | MEDIUM}] {Rule — ≤20 words}
(encodes: {SURPRISE NAME})
```
Traceability check *(C-24)*: tier must match named surprise's triage tier. Correct mismatches.

---

### Step 11 — Gestalt Summary Audit *(C-26)*

*Applied to the complete draft output (Steps 7–10) as a single unit.*

**Audit question**: "Could this output, read as a whole, be described as a survey of what
the investigation found?"

This is an artifact-level test. Item screening (Steps 3–6) cannot catch this. An output can
have every entry pass the prediction gate and still read in aggregate as a comprehensive
survey of discoveries.

If YES / PARTLY YES:
- Identify entries that read as survey items despite passing item-level tests
- Revise to surface genuine cross-signal surprise, or discard
- Add to discard log with reason: `gestalt-summary-fail`
- Re-run audit after revision

If NO: proceed to Step 12.

---

### Step 12 — Production Chain Trace *(C-28)*

*Named chain links with structural qualifiers — independently auditable.*

```
PRODUCTION CHAIN TRACE
──────────────────────────────────────────────────────────────────────
typed-route prediction sort (with IA co-validation, anti-hypothesis guard,
  and typed downstream destination per discarded item)
→ staged gate verdict (with per-stage written commits, falsifiable "We
    believed:" field, and VALID/INVALID contrast gallery per Stage 2 item)
→ comparative triage rank (assigned across all candidates simultaneously,
    failure-first ordering within each tier, before any entry expansion)
→ echo entry (with name from derivation scaffold, failure-first production
    sequence, mis-design field, and cross-signal annotation)
→ impact-anchored rule (tier verified against triage rank by explicit
    traceability check before output)
→ gestalt audit (applied to complete artifact as unit; any gestalt-summary-
    fail discards logged separately from item-level discard log)
──────────────────────────────────────────────────────────────────────
Missing link protocol: Name absent links as ABSENT with reason. Structural
qualifier protocol: each parenthetical names a property verifiable from the
output alone, not from session memory.
```

---

**Output**: Steps 7–12. Steps 1–6 are execution scaffolding.

---

---

## V-05 — Full Combination (All 20 Aspirational Criteria: C-09..C-28)

**Variation axis**: Full combination — all 20 aspirational criteria at structurally distinct
moments. No criterion activates at the same structural step as another unless they are
genuinely co-dependent.

**Hypothesis**: C-26, C-27, and C-28 activate at different phases of the production chain
(C-27 at role first-invocation; C-26 post-draft, artifact-level; C-28 post-output,
chain-level) and do not conflict with any prior criterion. All 20 can coexist with
unambiguous activation boundaries, each criterion auditable by name at the step it governs.

**Builds on**: V-04 (all three new criteria verified individually and in combination).

**New over V-04**: Full criterion inventory; C-27 function declaration at role first-invocation
per sub-step (C-25 requirement); C-26 audit structurally separated from C-24 traceability
check; C-28 trace with structural qualifiers that include the C-26 audit link.

---

You are running `/quest:topic echo` for the topic: {topic}.

All essential signals are in hand. Your task: surface the genuine surprises — findings that
only became visible in retrospect, from cross-signal tension, that no competent practitioner
would have predicted before gathering evidence.

Not a summary. Not a survey of discoveries. An echo: the signal that comes back that you
didn't send.

---

### Roles *(C-25: two distinct named roles with per-sub-step labeling)*

**Institutional Archaeologist (IA)**
*First invocation: Step 2.*
Function: Recovers false assumptions embedded in the current materials — what a future team
would carry as truth without knowing otherwise. Frames every surprise as a correction to a
false assumption (C-17), not a description of a discovery. The IA derives consequence by
asking "What would the next team build wrong?" (C-18, C-22). The IA is the author of
implication; the Gatekeeper is the author of rejection.
Active: Steps 2, 5, 7, 8, 9.

**Gatekeeper**
*First invocation: Step 3.*

```
GATEKEEPER — FUNCTION DECLARATION (C-27)
─────────────────────────────────────────────────────────────────────
Function:      Adversarial rejection. Tests each gate-pipeline candidate
               against two criteria: (1) first-principles predictability —
               could a competent practitioner have predicted this before
               any signal gathering? (2) cross-signal requirement — does
               this finding emerge only when ≥2 artifacts are read together,
               or does it exist in one artifact in isolation? Fails either
               criterion: rejected.

Not-function:  Future-reader framing. The Gatekeeper does not ask what the
               next team would get wrong. That is the Institutional
               Archaeologist's domain. The Gatekeeper asks only: could
               anyone have predicted this? Is this cross-signal?

Not-function:  Thematic synthesis, narrative construction, or cross-item
               grouping. The Gatekeeper evaluates each candidate in
               isolation. It does not relate items to each other.

Role boundary: Gatekeeper verdicts are final. The IA cannot reverse a
               rejection. The boundary is structural: the Gatekeeper tests
               the candidate; the IA frames the implication. They do not
               substitute for each other.
─────────────────────────────────────────────────────────────────────
```

Active: Step 3 only. Role name appears at each Stage header.

---

### Step 1 — Read Signal Record *(C-10: multi-namespace coverage; C-12: temporal marking)*

Read all signal artifacts in the topic signal folder across all namespaces (scout, draft,
review, flow, trace, prove, listen, program, topic).

Record:
- Namespaces covered — must reach ≥3 distinct namespaces (C-10 floor)
- Total artifacts read
- Date range (earliest artifact date → latest) — temporal anchor for C-12 per entry

---

### Step 2 — Pre-Write Prediction Sort
*(IA; C-16: structurally-enforced filter; C-14: downstream handoff routing; C-11: anti-hypothesis guard; C-20: pre-expansion co-validation gate; C-09: discard visibility)*

Assign a typed route to every finding in the signal record. The route is a structural
verdict — not a judgment call — enforced before any candidate proceeds to the gate *(C-16)*.

Route types:
- `topic-story` — finding confirms a working hypothesis; destination: topic narrative (C-14)
- `topic-report` — restates known constraint or documents a requirement; destination: report (C-14)
- `gate-pipeline` — candidate surprise; not in pre-investigation frame; proceeds to Step 3

Anti-hypothesis guard *(C-11)*: before assigning `gate-pipeline`, explicit check: "Does this
item confirm what the investigation set out to prove?" If YES → `topic-story`, regardless of
apparent novelty. Confirmation of hypothesis is not a surprise.

*(IA)* Pre-expansion co-validation *(C-20 partial)*: for each `gate-pipeline` item, the IA
confirms: "A new team approaching this topic from the spec alone would not have encountered
this finding." If the IA cannot confirm: route to `topic-report`.

Discard log *(C-09)*: record every item routed to `topic-story` or `topic-report` with:
- Route type
- Route reason (1 sentence)
- Downstream destination (C-14)

A non-empty discard log is required. An empty log indicates the filter was not applied.

---

### Step 3 — Multi-Stage Epistemic Gate
*(Gatekeeper; C-13: typed skeptic gate; C-15: minimum surprise floor; C-16: structurally-enforced filter)*

```
GATEKEEPER: active from here through end of Stage 3.
```

**Anti-Pattern Catalog** *(C-13; Gatekeeper applies per candidate)*:
- CONFIRMATION: item confirms original hypothesis even if not predicted — verdict PREDICTABLE
- RESTATEMENT: item documents a known constraint or spec requirement — route `topic-report`
- ISOLATED-FINDING: finding exists complete in one artifact; no cross-signal emergence — route `topic-report`

**Gate format** *(C-16)*: each candidate receives a typed verdict token before expansion.
Format: `VERDICT: SURPRISE | CUT — {anti-pattern label if CUT}`. Structurally malformed
entries (no valid verdict token) cannot proceed.

**Three sequential stages. Per-stage commit required. Collapse prohibition: do not write a
combined multi-stage verdict. Each stage result is a written artifact before the next begins.**

---

**Stage 1 — Prediction Test** *(Gatekeeper; epistemic dimension: novelty)*

Gate question: "Would a competent practitioner have predicted this finding from first
principles, prior to any signal gathering?"

Anti-hypothesis guard re-check *(C-11)*: if the finding confirms the investigation's own
starting hypothesis, verdict is PREDICTABLE regardless of other signals.

`PREDICTABLE` → route to `topic-story`; add to discard log; stop here
`UNPREDICTABLE` → proceed to Stage 2

**Commit**: write `Stage 1: [{item label}] → [PREDICTABLE | UNPREDICTABLE]` before Stage 2.

---

**Stage 2 — Contradiction Test** *(Gatekeeper; epistemic dimension: opposition)*

Gate question: "Does this item contradict, complicate, or qualify an assumption from the
pre-investigation frame?"

*"We believed:" field template* *(C-18 scaffolding for later entry)*:

```
We believed: {falsifiable pre-investigation assumption — names a specific belief held}
VALID: {case that genuinely falsifies the belief — names the belief and the contradiction}
INVALID (absence-of-consideration): {notes something was absent rather than falsifying
   a held belief — does not name what assumption was wrong}
INVALID (sentiment-reaction): {expresses surprise without naming the assumption that
   turned out to be false — "we didn't expect X" is not falsification}
INVALID (hedge-uncertainty): {hedges on whether the belief was ever held — weakens
   the falsifiability of the claim}
```

Minimum surprise floor *(C-15)*: at least 3 candidates must reach CONTRADICTION FOUND.
If fewer than 3 pass Stage 2 after all candidates are processed, record as floor-miss.
Do not suppress the floor-miss in output; it is an auditable fact.

`NO CONTRADICTION` → route to `topic-report`; discard log
`CONTRADICTION FOUND` → proceed to Stage 3

**Commit**: write `Stage 2: [{item label}] → [NO CONTRADICTION | CONTRADICTION FOUND]`
before Stage 3.

---

**Stage 3 — Attribution Test** *(Gatekeeper; epistemic dimension: specificity)*

Gate question: "Does this finding emerge only when two or more signal artifacts are read
together, or does it exist complete in a single artifact in isolation?"

`SINGLE-ARTIFACT` → route to `topic-report`; discard log
`CROSS-SIGNAL (cite ≥2 source artifacts)` → verdict SURPRISE

**Commit**: write `Stage 3: [{item label}] → [SINGLE-ARTIFACT | CROSS-SIGNAL] — sources:
[{artifact1 (namespace/skill)}, {artifact2 (namespace/skill)}]` before Step 4.

---

### Step 4 — Pre-Write Impact Triage *(C-23: impact triage as pre-write scaffolding; C-22: failure-first production ordering)*

Assign each SURPRISE candidate a tier *comparatively* — evaluate all candidates against each
other before assigning any tier. No tier is assigned in isolation.

- **HIGH**: Forces revision to a core design decision, assumption, or scope boundary
- **MEDIUM**: Qualifies a design principle or adds a constraint to an existing decision
- **LOW**: Notable; no clear design consequence at present

*(C-22)* Within each tier: failure-first ordering — the candidate with the highest
failure-if-wrong risk goes first within its tier. Ask: "If we carry the old assumption on
this candidate, what is the severity of the resulting mis-design?" Order by severity
(highest first) within each tier.

Record all triage assignments before writing any entry. Entry writing order: HIGH → MEDIUM →
LOW; within tier: failure-first *(C-22)*.

---

### Step 5 — Naming Scaffold *(C-17: correction-encoding names; C-21: derivation scaffold)*

For each SURPRISE candidate, work through the scaffold before writing the entry header.
This scaffold produces the name; do not skip to name formation.

1. State the old belief: "The team carried the assumption that ___."
2. State the correction: "The signals revealed instead that ___."
3. Derive the domain: "This affects the ___ area of the design."
4. Form the label: `The {Corrected Belief}: {Domain}`

VALID: "The Silent Veto: Adoption Workflow" — encodes *what was wrong* (there is a silent
veto mechanism) and *where* (adoption workflow).
INVALID: "Surprising Finding About Adoption" — describes the discovery category, not the
corrected belief.

The output of step 4 feeds directly into the entry header.

---

### Step 6 — Pre-Expansion Co-Validation Gate *(C-20: pre-expansion co-validation gate)*

Before expanding any entry, co-validate two fields *simultaneously*. Both must be VALID.
Either failing blocks expansion — revise the failing field before proceeding.

- **Name form** *(C-17)*: does the label follow `The {Corrected Belief}: {Domain}`, encoding
  what was wrong rather than describing the discovery?
  → VALID / INVALID

- **Failure field** *(C-18)*: does the failure read as "If the next team carries the old
  assumption, {specific concrete mis-design}" — grounded in a named mis-design, not a
  change-list or vague consequence?
  → VALID / INVALID

Gate runs once per candidate entry. A VALID gate is the pre-condition for Step 7 expansion.

---

### Step 7 — Write Echo Entries
*(IA; triage order; failure-first within tier; C-04, C-02, C-03, C-08, C-12, C-14, C-17, C-18, C-22)*

Entry production sequence *(C-22: failure-first)*: begin from the failure scenario, then
derive signal tracing, naming, and impact from that anchor. The failure is load-bearing; the
name and source are derived from it, not the reverse.

---

**Begin from failure**: If the next team carries the old assumption about {domain},
they would {specific mis-design}. This is the anchor.

**[SURPRISE NAME: `The {Corrected Belief}: {Domain}`]** — *{HIGH | MEDIUM | LOW}* *(IA)*

Source signal: `{artifact-name} ({namespace}/{skill})`
*(C-02: cite all sources that contributed; precision sufficient to retrieve artifact)*
`[CROSS: {artifact-A} × {artifact-B}]` *(C-08: cross-signal annotation — enables
identification without re-tracing sources)*

Temporal anchor *(C-12)*: `{round or date of earliest contributing signal}`

We believed: `{falsifiable pre-investigation assumption — names the specific belief held}`

The surprise: `{what the signals revealed that contradicts or complicates the prior assumption}`

If the next team carries the old assumption *(C-18)*: `{specific concrete mis-design — the
exact wrong construction that follows from the false assumption}`.

Design impact *(C-03)*: `{one of: a decision revisited / an assumption struck / a scope
boundary shifted — name the specific decision, assumption, or boundary}`.

Downstream route *(C-14)*: `→ {skill or namespace — name the specific consumer}`.

---

### Step 8 — Cross-Signal Synthesis *(C-05: synthesis not summary; IA)*

One paragraph, ≤120 words.

*(IA)*: Identify the pattern. Name ≥2 SURPRISE entries by their labels. Explain what only
emerges from reading those entries together — the insight that cannot be derived from any
single entry alone.

C-05 definitional line: a finding that lives in one artifact is a finding; a surprise that
only becomes visible when two signals are read together is an echo. This paragraph is where
the echo becomes visible. Do not summarize the entries; synthesize the cross-entry tension.

---

### Step 9 — Forward Handover Guidance *(C-06: forward-looking handoff; C-19: register-anchored close; IA)*

Select one register from the menu that matches the most actionable downstream route from
the Step 7 entries *(C-19)*:

- T-1 (builder): "If you are about to build {scenario}, know that {constraint} because {source}."
- T-2 (reviewer): "Before approving {decision}, verify {constraint} against {source}."
- T-3 (PM): "Scope the {area} decision against {constraint} found in {source}."
- T-4 (architect): "The {component} design assumes {belief}; {source} shows this is false."

Verify slot assignments before writing the final statement: {scenario/decision/area/component}
and {constraint/fact} must both be specific, not generic. Source must be citable *(C-06)*.

State the selected register (T-1 / T-2 / T-3 / T-4) before writing the statement.

---

### Step 10 — Rules of Thumb *(C-07: impact magnitude; C-24: end-to-end traceability closure)*

≤3 rules. HIGH and MEDIUM surprises only. LOW surprises do not generate rules.

```
[{HIGH | MEDIUM}] {Rule — ≤20 words, quotable as standalone heuristic}
(encodes: {SURPRISE NAME})
```

Traceability check *(C-24)*:
1. Each rule's impact tier matches the named surprise's triage tier from Step 4
2. Each rule is traceable to exactly one named surprise (no orphan rules)
3. No surprise generates more than one rule

If any check fails: correct before proceeding. This step closes the audit chain: triage →
entry header → rule → verification.

---

### Step 11 — Gestalt Summary Audit *(C-26: output-level gestalt summary test)*

*Applied to the complete draft output (Steps 7–10) as a single unit.*

This step tests what item-level screening (Steps 3–6) structurally cannot catch.

**Audit question**: "Could this output — read as a whole, not entry by entry — be described
as a summary or survey of what the investigation found: a comprehensive review of discoveries
organized by theme or signal source?"

Apply the test to the artifact gestalt. An output can have every individual entry pass the
prediction gate, the contradiction test, and the attribution test, and still read in aggregate
as a survey of discoveries rather than a curated set of retroactively-visible surprises.
The aggregate tone is what this step screens.

If YES or PARTLY YES:
- Identify entries that read as survey items in aggregate (even if they passed item-level tests)
- Revise to surface the genuine cross-signal surprise, or discard
- Add to discard log with reason: `gestalt-summary-fail` (distinct from item-level `gate-fail`)
- Re-run the gestalt audit after each revision pass

If NO: proceed to Step 12.

---

### Step 12 — Production Chain Trace *(C-28: full-chain traceability with structural qualifiers)*

*Each link named with structural qualifier — independently auditable by future reader.*

Write the production chain as a verifiable record. Each parenthetical names the structural
requirement that makes that link auditable from this statement alone — a future reader can
verify any link without access to the session that produced the artifact.

```
PRODUCTION CHAIN TRACE
──────────────────────────────────────────────────────────────────────
typed-route prediction sort (with IA co-validation per route, anti-hypothesis
  guard applied per candidate, typed downstream destination per discard, and
  non-empty discard log as structural requirement)
→ staged gate verdict (with per-stage written commit tokens, collapse
    prohibition enforced, falsifiable "We believed:" field with VALID/INVALID
    contrast per Stage 2 candidate, and cross-signal citation per Stage 3 SURPRISE)
→ comparative triage rank (HIGH/MEDIUM/LOW assigned across all candidates
    simultaneously, failure-first ordering within tier, all tiers recorded
    before any entry expansion begins)
→ echo entry (with name from 4-step derivation scaffold, failure-first
    production sequence, cross-signal annotation [CROSS: A × B], and
    failure field framed as concrete mis-design, not change-list)
→ impact-anchored rule (tier verified by explicit traceability check against
    triage rank, orphan rule check, and one-rule-per-surprise constraint)
→ gestalt audit (applied to complete artifact as unit; gestalt-summary-fail
    discards logged separately from item-level gate-fail discards)
──────────────────────────────────────────────────────────────────────
Missing link protocol: Name any absent link as ABSENT with reason. Do not
omit absent links — an absent link is an auditable fact, not an invisible gap.

Structural qualifier protocol: Each parenthetical must name a property
verifiable from the output alone, not from session memory or scaffolding steps.
```

---

**Output**: Steps 7–12 only. Steps 1–6 are execution scaffolding not included in output.

Final output sequence:
1. Echo entries (triage-ordered, failure-first within tier)
2. Cross-signal synthesis
3. Forward handover guidance (with register selection stated)
4. Rules of Thumb
5. Gestalt audit result (if any items revised or discarded: log entry)
6. Production chain trace

Minimum surprise floor check *(C-15)*: if fewer than 3 distinct surprises are present in
the final output, note the floor-miss before closing. Do not suppress it.
