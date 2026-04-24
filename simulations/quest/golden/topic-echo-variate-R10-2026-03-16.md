---
skill: quest-variate
skill_target: topic-echo
date: 2026-03-16
round: 10
rubric: v10
rubric_max: 100
---

# Variations: `topic:echo` -- Round 10

**Rubric:** v10 | **Date:** 2026-03-16

---

## Design Context

R9 V-04/V-05 differential reveals two structural gaps not captured by any prior criterion:

1. **C-16 taxonomy isolation → C-28**: V-04 reached PARTIAL on C-16 — no
   misunderstanding-category taxonomy was declared. V-05 passed C-16 and went further:
   the taxonomy categories propagated from the synthesis section into the Rules of Thumb
   audit pass as a named `{CATEGORY}:` column alongside each surprise label and confidence
   tier. C-16 only tests whether synthesis names the category; C-28 tests whether those
   categories appear as typed fields in downstream audit structures rather than staying
   isolated in the synthesis step.

2. **Synthesis-step budget gap → C-29**: V-04 passed C-20 — every data-collection step
   carried `PHASE:` + `WORD BUDGET:` contract fields. V-05 extended the contract to the
   synthesis step: `One classification line per surprise + synthesis ≤120 words`. C-20
   tests that pipeline phases have scope contracts; C-29 tests that the synthesis/output
   step specifically carries its own formal `WORD BUDGET:` contract field, not merely a
   prose word-count guideline embedded in step description.

**Variation plan:**

- V-01: C-28 only — taxonomy categories propagate from Step 8 synthesis into Step 10
  audit row schema (output format axis)
- V-02: C-29 only — Step 8 gains explicit `WORD BUDGET:` contract header alongside
  existing prose limit (lifecycle emphasis axis)
- V-03: Phrasing register axis only — formal `PHASE:` + `SCOPE:` contract blocks at
  every named pipeline step; neither C-28 nor C-29 activated
- V-04: C-28 + C-29 combined (no formal phase blocks on all steps)
- V-05: Full synthesis — C-28 + C-29 + formal phase contract blocks; gold standard for v10

**Discriminating pairs:**
- V-01 vs V-05: C-29 + register absent vs present; isolates synthesis-budget + phase-contract value
- V-02 vs V-05: C-28 + register absent vs present; isolates taxonomy-propagation + phase-contract value
- V-03 vs V-05: C-28 + C-29 absent vs present; isolates taxonomy-propagation + synthesis-budget value
- V-04 vs V-05: register absent vs present; direct isolation of formal phase-contract value

---

## V-01 -- Single-axis: Category-Field Audit Propagation (C-28)

**Variation axis:** Output format. The misunderstanding-category taxonomy declared in
Step 8 (Cross-Signal Synthesis) propagates as a required typed field `{CATEGORY}:` into
the Rules of Thumb audit rows in Step 10. The audit row schema changes from
`[{tier}] {rule} (encodes: {NAME})` to
`[{tier}] {rule} (encodes: {NAME} → {CATEGORY}: {taxonomy-label})`.
The taxonomy declaration is the upstream source; the audit row schema is the downstream
consumer.

**Hypothesis:** In R9, C-16 PARTIAL failures occurred because models named the synthesis
pattern topically (e.g., "integration surface coupling") rather than by misunderstanding
type (e.g., "integration-surface-blindness"). Even when C-16 was passed with a full
taxonomy declaration (V-05), the categories stayed isolated to the synthesis step — no
downstream consumer required them as typed fields. C-28 closes this by making each audit
row a consumer of the declared taxonomy. A model that produces a taxonomy-less synthesis
cannot propagate categories into audit rows without backfilling them. The field propagation
makes the taxonomy structural, not rhetorical.

**Builds on:** R9 V-05 — all prior criteria active.

**C-29 status:** Not activated. Step 8 carries prose word-limit ("≤120 words") but no
formal `WORD BUDGET:` contract header. This is the discriminator between V-01 and V-05.

---

### Prompt Body

You are running `/quest:topic echo` for the topic: {topic}.

All essential signals are in hand. Your task: surface the genuine surprises — findings that
only became visible in retrospect, from cross-signal tension, that no competent practitioner
would have predicted before gathering evidence.

Not a summary. Not a survey of discoveries. An echo: the signal that comes back that you
didn't send.

---

### Roles

**Institutional Archaeologist (IA)**
*First invocation: Step 2.*
Function: Recovers false assumptions embedded in current materials — what a future team
would carry as truth without knowing otherwise. Frames every surprise as a correction to a
false assumption. Derives consequence by asking "What would the next team build wrong?"
The IA is the author of implication; the Gatekeeper is the author of rejection.

Sub-step co-activation shorthand: each IA invocation carries:
`IA: false-assumption-recovery; epistemic dimension: {name}`

Defined dimensions:

| Step | Epistemic Dimension | Why here |
|------|---------------------|----------|
| 2 | prior-frame-recovery | Recovering what was actually believed, not what spec asserts |
| 5 | belief-inversion | Deriving the correction-encoding name by inverting the false assumption |
| 6 | correction-integrity | Verifying both structural form checks encode the correction |
| 7 | failure-projection | Anchoring entry in the projected mis-design; failure is load-bearing |
| 8 | pattern-emergence | What only emerges when entries are read together; absent from any single |
| 9 | future-framing | Translating institutional memory into actionable guidance for a future builder |

Active: Steps 2, 5, 6, 7, 8, 9.

**Gatekeeper**
*First invocation: Step 3.*
Sub-step shorthand: `Gatekeeper: adversarial-rejection-only; epistemic dimension:
{stage-label}` — see Stage headers.

```
GATEKEEPER -- FUNCTION DECLARATION
---------------------------------------------------------------------
Function:      Adversarial rejection. Tests each gate-pipeline candidate: (1)
               first-principles predictability; (2) cross-signal requirement.
               Fails either: rejected.

Not-function:  Future-reader framing. The Gatekeeper does not ask what the
               next team would get wrong. That is the IA's domain.

Not-function:  Thematic synthesis or cross-item grouping. The Gatekeeper
               evaluates each candidate in isolation.

Role boundary: Gatekeeper verdicts are final. The IA cannot reverse a rejection.
---------------------------------------------------------------------
```

Active: Step 3 only.

---

### Step 1 -- Read Signal Record

Read all signal artifacts across all namespaces (scout, draft, review, flow, trace, prove,
listen, program, topic). Record:
- Namespaces covered -- must reach >=3 distinct namespaces (namespace floor)
- Total artifacts read
- Date range (earliest -> latest)

Record before entry expansion begins. Gap noted if <3 namespaces.

---

### Step 2 -- Pre-Write Prediction Sort
*(IA: false-assumption-recovery; epistemic dimension: prior-frame-recovery -- recovering
what beliefs were actually held before investigation, not what the spec states)*

Assign a typed route to every finding before any candidate proceeds to the gate.

Route types:
- `topic-story` -- confirms hypothesis; destination: topic narrative
- `topic-report` -- restates known constraint; destination: report
- `gate-pipeline` -- candidate surprise; proceeds to Step 3

Anti-hypothesis guard *(IA: false-assumption-recovery; epistemic dimension:
prior-frame-recovery)*: "Does this item confirm what the investigation set out to prove?"
YES -> `topic-story`, regardless of apparent novelty.

Pre-expansion co-validation: for each `gate-pipeline` item: "A new team from the spec
alone would not have encountered this." Cannot confirm -> `topic-report`.

Discard log: every item routed to `topic-story` or `topic-report` with route type, reason
(1 sentence), downstream destination. Non-empty discard log required. Empty log indicates
filter was not applied.

---

### Step 3 -- Multi-Stage Epistemic Gate
*(Gatekeeper: adversarial-rejection-only)*

```
GATEKEEPER: adversarial-rejection-only -- active from here through end of Stage 3.
```

**Anti-Pattern Catalog**:
- CONFIRMATION: confirms original hypothesis even if unpredicted -> PREDICTABLE
- RESTATEMENT: documents known constraint or spec requirement -> route `topic-report`
- ISOLATED-FINDING: finding complete in one artifact; no cross-signal emergence -> route `topic-report`

**Gate format**: `VERDICT: SURPRISE | CUT -- {anti-pattern label if CUT}`

**Three sequential stages. Per-stage commit required. Collapse prohibition: do not write a
combined multi-stage verdict. Each stage result is a written artifact before the next begins.**

---

**Stage 1 -- Prediction Test**
*(Gatekeeper: adversarial-rejection-only; epistemic dimension: novelty -- separating
investigation-emergent findings from outcomes predictable from original design materials)*

"Would a competent practitioner have predicted this from first principles, prior to any
signal gathering?"

`PREDICTABLE` -> route to `topic-story`; discard log
`UNPREDICTABLE` -> Stage 2

**Commit**: `Stage 1: [{item label}] -> [PREDICTABLE | UNPREDICTABLE]`

---

**Stage 2 -- Contradiction Test**
*(Gatekeeper: adversarial-rejection-only; epistemic dimension: opposition -- separating
genuine contradiction of a held belief from findings that are merely notable or unusual)*

"Does this item contradict, complicate, or qualify an assumption from the pre-investigation
frame?"

```
We believed: {falsifiable pre-investigation assumption -- names a specific belief held}
VALID: {case that genuinely falsifies the belief -- names belief and contradiction}
INVALID (absence-of-consideration): {notes absence rather than falsifying a held belief}
INVALID (sentiment-reaction): {expresses surprise without naming the assumption that
   turned out to be false}
INVALID (hedge-uncertainty): {hedges on whether the belief was ever held}
```

If INVALID -> candidate fails Stage 2 -> return to discard log as `topic-report`.

Minimum surprise floor: >=3 candidates must reach CONTRADICTION FOUND. If fewer than 3,
record as floor-miss. Do not suppress it.

`NO CONTRADICTION` -> route to `topic-report`; discard log
`CONTRADICTION FOUND` -> Stage 3

**Commit**: `Stage 2: [{item label}] -> [NO CONTRADICTION | CONTRADICTION FOUND]`

---

**Stage 3 -- Attribution Test**
*(Gatekeeper: adversarial-rejection-only; epistemic dimension: specificity -- separating
traceable cross-signal findings from single-artifact findings that cannot generate an echo)*

"Does this finding emerge only when two or more signal artifacts are read together?"

`SINGLE-ARTIFACT` -> route to `topic-report`; discard log
`CROSS-SIGNAL (cite >=2 source artifacts)` -> verdict SURPRISE

**Commit**: `Stage 3: [{item label}] -> [SINGLE-ARTIFACT | CROSS-SIGNAL] -- sources:
[{artifact1 (namespace/skill)}, {artifact2 (namespace/skill)}]`

---

### Step 4 -- Pre-Write Impact Triage

Assign each SURPRISE candidate a tier comparatively -- evaluate all candidates against
each other before assigning any tier. No tier assigned in isolation.

- **HIGH**: Forces revision to core design decision, assumption, or scope boundary
- **MEDIUM**: Qualifies design principle or adds constraint to existing decision
- **LOW**: Notable; no clear design consequence at present

Failure-first ordering within each tier. Record all assignments before writing any entry.
Write order: HIGH -> MEDIUM -> LOW; within tier: failure-first.

---

### Step 5 -- Naming Scaffold
*(IA: false-assumption-recovery; epistemic dimension: belief-inversion -- the name is
derived by inverting the false assumption; the label encodes what was wrong and where)*

1. State old belief: "The team carried the assumption that ___."
2. State correction: "The signals revealed instead that ___."
3. Derive domain: "This affects the ___ area of the design."
4. Form label: `The {Corrected Belief}: {Domain}`

VALID: "The Silent Veto: Adoption Workflow" -- encodes what was wrong and where.
INVALID: "Surprising Finding About Adoption" -- describes discovery, not corrected belief.

---

### Step 6 -- Pre-Expansion Co-Validation Gate
*(IA: false-assumption-recovery; epistemic dimension: correction-integrity -- verifying
that both name form and failure field structurally encode the correction before any
expansion begins; neither alone suffices)*

Before expanding any entry, co-validate simultaneously. Both must be VALID.
Either failing blocks expansion -- return to Step 5 and revise before proceeding.

- **Name form**: follows `The {Corrected Belief}: {Domain}`? -> VALID / INVALID
- **Failure field**: reads as "If the next team carries the old assumption,
  {specific concrete mis-design}" -- named mis-design, not change-list? -> VALID / INVALID

Gate runs once per candidate. VALID gate is pre-condition for Step 7 expansion.

---

### Step 7 -- Write Echo Entries
*(IA: false-assumption-recovery; epistemic dimension: failure-projection -- entry begins
from the projected mis-design; failure scenario is load-bearing, not derived;
triage order; failure-first within tier)*

Begin from failure *(IA: false-assumption-recovery; epistemic dimension:
failure-projection)*: If the next team carries the old assumption about {domain}, they
would {specific mis-design}. Anchor.

---

**[`The {Corrected Belief}: {Domain}`]** -- *{HIGH | MEDIUM | LOW}*
*(IA: false-assumption-recovery; epistemic dimension: failure-projection)*

Source signal: `{artifact-name} ({namespace}/{skill})`
`[CROSS: {artifact-A} x {artifact-B}]`
Temporal anchor: `{round or date of earliest contributing signal}`
We believed: `{falsifiable pre-investigation assumption}`
The surprise: `{what signals revealed that contradicts the prior assumption}`
If the next team carries the old assumption: `{specific concrete mis-design}`.
Design impact: `{decision revisited / assumption struck / scope boundary shifted}`.
Downstream route: `-> {skill or namespace}`.

---

### Step 8 -- Cross-Signal Synthesis
*(IA: false-assumption-recovery; epistemic dimension: pattern-emergence -- naming what
only becomes visible when entries are read together; unreachable from any single entry alone)*

**Taxonomy declaration (C-16 -> C-28 propagation upstream source):**
Before writing the synthesis paragraph, declare the misunderstanding-category taxonomy
across all SURPRISE entries. Categories are typed by misunderstanding class, not topic.

```
CATEGORY DECLARATION:
  {SURPRISE NAME-A} -> {CATEGORY}: e.g., capability-underestimation |
                       integration-surface-blindness | pricing-model-conflation |
                       scope-assumption-failure | adoption-friction-blindness |
                       lifecycle-phase-conflation
  {SURPRISE NAME-B} -> {CATEGORY}: {taxonomy-label}
  {SURPRISE NAME-C} -> {CATEGORY}: {taxonomy-label}
```

This declaration is the upstream source for the `{CATEGORY}:` field in Step 10 audit rows
(C-28). Do not proceed to synthesis paragraph without completing the declaration.

**Synthesis paragraph:**
<=120 words. Name >=2 SURPRISE entries by their exact labels. Explain what only emerges
from reading those entries together -- unreachable from any single entry alone. State the
independence constraint explicitly in the paragraph. Name the category of shared
misunderstanding across the dominant entries (C-16). PARTIAL if synthesis names a pattern
but does not classify by misunderstanding type.

---

### Step 9 -- Forward Handover Guidance
*(IA: false-assumption-recovery; epistemic dimension: future-framing)*

Select one register:
- T-1 (builder): "If you are about to build {scenario}, know that {constraint} because {source}."
- T-2 (reviewer): "Before approving {decision}, verify {constraint} against {source}."
- T-3 (PM): "Scope the {area} decision against {constraint} found in {source}."
- T-4 (architect): "The {component} design assumes {belief}; {source} shows this is false."

State selected register (T-1/T-2/T-3/T-4). Verify slot assignments before writing.
Both scenario/decision/area/component and constraint must be specific. Source citable.

---

### Step 10 -- Rules of Thumb

<=3 rules. HIGH and MEDIUM surprises only. LOW excluded.

**Audit row schema (C-28: category-field propagation from Step 8 taxonomy declaration):**

```
[{HIGH | MEDIUM}] {Rule -- <=20 words, quotable standalone heuristic}
(encodes: {SURPRISE NAME} -> {CATEGORY}: {taxonomy-label-from-Step-8-declaration})
```

The `{CATEGORY}:` field must reference a label declared in Step 8's CATEGORY DECLARATION
block. If the label is absent from Step 8, return to Step 8 and update before writing
the rule.

Traceability check:
1. Each rule's tier matches named surprise's triage tier from Step 4
2. Each rule traceable to exactly one named surprise (no orphan rules)
3. No surprise generates more than one rule
4. Each rule's `{CATEGORY}:` references a declared taxonomy label from Step 8 (C-28)

Correct all mismatches before writing verdict.

**Write verdict:**

```
TRACE-CHECK-VERDICT: [PASS | FAIL]
  -- PASS: all tiers match; no orphan rules; one-rule-per-surprise confirmed;
           all {CATEGORY}: fields reference declared taxonomy labels
  -- FAIL: {each mismatch: rule label, expected tier, actual tier, or absent {CATEGORY}:}
```

*A future reader verifies this check ran by locating TRACE-CHECK-VERDICT in the output --
no session replay required. TRACE-CHECK-VERDICT: PASS certifies (1) tier match,
(2) no orphan rules, (3) one-rule-per-surprise, and (4) all {CATEGORY}: fields reference
taxonomy labels declared in Step 8 (C-28 field propagation confirmed).*

---

### Step 11 -- Gestalt Summary Audit

*Applied to the complete draft output (Steps 7-10) as a single unit.*

"Could this output -- read as a whole, not entry by entry -- be described as a summary or
survey of what the investigation found?"

If YES or PARTLY YES: revise, add `gestalt-summary-fail` to discard log, re-run.

```
GESTALT-VERDICT: [PASS | FAIL]
  -- PASS: output does not read as survey in aggregate; every entry is a
     retroactively-visible surprise, not a survey item included for coverage
  -- FAIL: {each entry: label, gestalt-summary-fail trigger reason, revision applied}
```

*A future reader verifies this check ran by locating GESTALT-VERDICT in the output --
no session replay required. GESTALT-VERDICT: PASS certifies the complete output, read
as a whole unit, does not pass the summary-or-survey audit question. GESTALT-VERDICT:
FAIL identifies which entries triggered the pattern and records the revision applied.*

---

### Step 12 -- Production Chain Trace

```
PRODUCTION CHAIN TRACE
VERIFICATION NODES INCLUDED | DEPENDENCY GRAPH CLOSED
======================================================================

[NODE 1] typed-route prediction sort
  structural qualifier: IA: false-assumption-recovery; epistemic dimension:
    prior-frame-recovery co-activation per route, anti-hypothesis guard per candidate,
    typed downstream destination per discard, non-empty discard log as structural requirement
  produces: typed route decisions, discard log with destinations
  consumed by: NODE 2 (receives gate-pipeline candidates only)

-> [NODE 2] staged gate verdict
  structural qualifier: Gatekeeper: adversarial-rejection-only; epistemic dimension per
    stage (novelty/opposition/specificity) at each Stage header, per-stage written commit
    tokens with collapse prohibition, falsifiable "We believed:" + VALID/INVALID contrast
    gallery per Stage 2, cross-signal citation per Stage 3 SURPRISE, minimum floor tracked,
    Stage 2 INVALID -> return to discard log (return semantics present)
  produces: SURPRISE verdicts, floor count
  consumed by: NODE 3

-> [NODE 3] comparative triage rank
  structural qualifier: all candidates evaluated simultaneously before any tier assigned,
    failure-first ordering within tier, all tiers recorded before expansion begins
  produces: HIGH/MEDIUM/LOW triage assignments, within-tier order
  consumed by: NODE 4 (entry headers), NODE 8 (TRACE-CHECK-VERDICT tier-match)

-> [NODE 3b] taxonomy declaration [C-16 -> C-28 upstream source]
  structural qualifier: IA: false-assumption-recovery; epistemic dimension: pattern-emergence;
    per-surprise {NAME} -> {CATEGORY}: typed mapping; written before synthesis paragraph;
    categories typed by misunderstanding class, not topic
  produces: category taxonomy for C-16; per-surprise map as C-28 upstream source
  consumed by: NODE 5 (synthesis paragraph names category), NODE 7 ({CATEGORY}: field)

-> [NODE 4] echo entry
  structural qualifier: IA: false-assumption-recovery; epistemic dimension:
    failure-projection per sub-step; 4-step naming scaffold; failure-first production;
    [CROSS: A x B] annotation; failure field as concrete mis-design; named design impact
  produces: named surprise labels, source citations, design impact, routing tags
  consumed by: NODE 5 (synthesis), NODE 6 (handover), NODE 7 (rules)

-> [NODE 5] cross-signal synthesis
  structural qualifier: IA: false-assumption-recovery; epistemic dimension: pattern-emergence;
    >=2 named surprise labels cited by exact label; cross-entry pattern stated as unreachable
    from single entry alone; independence constraint stated explicitly; misunderstanding
    category named (C-16)
  produces: synthesized echo paragraph
  consumed by: output (terminal)

-> [NODE 6] forward handover guidance
  structural qualifier: IA: false-assumption-recovery; epistemic dimension: future-framing;
    register selected from T-1..T-4 menu; register stated before writing; slots verified;
    source citable
  produces: register-anchored handoff statement
  consumed by: output (terminal)

-> [NODE 7] impact-anchored rule with category field [C-28]
  structural qualifier: tier verified against NODE 3 triage; orphan rule check;
    one-rule-per-surprise; {CATEGORY}: field references declared taxonomy from NODE 3b --
    absent category -> return to NODE 3b for update before rule is written
  produces: verified rules with tier labels and {CATEGORY}: fields
  consumed by: NODE 8 (TRACE-CHECK-VERDICT)

-> [NODE 8] TRACE-CHECK-VERDICT
  structural qualifier: written PASS|FAIL token; certifies tier-match, no-orphan,
    one-rule-per-surprise, and {CATEGORY}: field presence (C-28 check); verifiable by
    locating token; records each mismatch if FAIL; forward-reader protocol at token
  produces: traceability audit result including C-28 field check
  consumed by: NODE 11 (chain trace)

-> [NODE 9] gestalt audit
  structural qualifier: IA: false-assumption-recovery applied to complete artifact as
    unit; gestalt-summary-fail discards logged separately from item-level gate-fail
  produces: gestalt audit result
  consumed by: NODE 10

-> [NODE 10] GESTALT-VERDICT
  structural qualifier: written PASS|FAIL token; certifies aggregate non-survey;
    records revision decisions if FAIL; forward-reader protocol at token
  produces: gestalt audit result
  consumed by: NODE 11 (chain trace)

-> [NODE 11] production chain trace (this node)
  structural qualifier: all nodes named with verifiable structural qualifiers;
    NODE 3b (taxonomy) and its C-28 propagation to NODE 7 explicitly named as a
    dependency link; inter-criterion dependencies annotated -- graph is closed
  produces: closed, auditable dependency graph
  consumed by: output (terminal)

======================================================================
Dependency closure:
  NODE 3 -> NODE 8: triage rank feeds tier-match check
  NODE 3b -> NODE 7: taxonomy declaration feeds {CATEGORY}: field in audit rows (C-28)
  NODE 9/10 -> NODE 11: gestalt verdict is named chain node
  NODE 8 -> NODE 11: traceability verdict is named chain node
  NODE 4 -> NODE 6: routing tags feed handover scenario selection
  Step 5 -> Step 6: naming scaffold feeds co-validation gate
```

---

### Dependency Closure Enumeration

*Standalone terminal block. Spot-checkable without traversal.*

```
DEPENDENCY CLOSURE ENUMERATION
================================
NODE 3 output -> NODE 8:
  triage rank (NODE 3) is required input for tier-match check (NODE 8)

NODE 3b output -> NODE 7 (C-28):
  taxonomy declaration (NODE 3b) is required input for {CATEGORY}: field in audit rows;
  NODE 7 cannot produce a C-28-compliant row without NODE 3b output

NODE 9/10 output -> NODE 11:
  gestalt verdict (NODE 10) is a named chain node in NODE 11

NODE 8 output -> NODE 11:
  traceability verdict (NODE 8) is a named chain node in NODE 11

NODE 4 output -> NODE 6:
  routing tags in entries (NODE 4) feed handover scenario selection (NODE 6)

Step 5 output -> Step 6:
  naming scaffold (Step 5) feeds co-validation name-form check (Step 6)
================================
All 6 loops enumerated. Spot-checkable without chain traversal.
```

**Output**: Steps 7-12 + Dependency Closure Enumeration. Steps 1-6 are execution scaffolding.

---

## V-02 -- Single-axis: Synthesis-Step Budget Contract (C-29)

**Variation axis:** Lifecycle emphasis. Step 8 (Cross-Signal Synthesis) gains a formal
`WORD BUDGET:` contract field identical in structure to the `PHASE:` + `WORD BUDGET:`
blocks already present on data-collection steps. The existing prose instruction
"<=120 words" is not removed -- it becomes the value inside the formal contract field.
The structural distinction: prose instructions embedded in step description vs a
named contract field visible at the step header that a pipeline reviewer can verify
without reading the prose body.

**Hypothesis:** V-04 satisfied C-20 (Audit Scope Differentiation) by carrying phase
scope contracts on data-collection steps but left the synthesis step without a formal
budget contract. The synthesis step is the final output gate; an unconstrained output
step is inconsistent with a contract-structured pipeline. A model executing a prompt
where Steps 2-7 have `WORD BUDGET:` headers but Step 8 does not will apply the
contract discipline inconsistently -- the output step is the one place where unbounded
generation is most likely. C-29 closes this by extending the contract schema to the
synthesis step. Hypothesis: adding `WORD BUDGET:` at Step 8's header reduces output
overrun without requiring any other structural change.

**Builds on:** R9 V-05 -- all prior criteria active.

**C-28 status:** Not activated. Step 8 carries NO taxonomy declaration block. Step 10
audit rows use standard format `(encodes: {SURPRISE NAME})` without `{CATEGORY}:` field.
This is the discriminator between V-02 and V-05.

---

### Prompt Body

You are running `/quest:topic echo` for the topic: {topic}.

All essential signals are in hand. Your task: surface the genuine surprises -- findings
that only became visible in retrospect, from cross-signal tension, that no competent
practitioner would have predicted before gathering evidence.

Not a summary. Not a survey of discoveries. An echo: the signal that comes back that you
didn't send.

---

### Roles

**Institutional Archaeologist (IA)**
*First invocation: Step 2.*
Sub-step shorthand: `IA: false-assumption-recovery; epistemic dimension: {name}`
Active: Steps 2, 5, 6, 7, 8, 9.

| Step | Epistemic Dimension | Why here |
|------|---------------------|----------|
| 2 | prior-frame-recovery | Recovering what was actually believed, not what spec asserts |
| 5 | belief-inversion | Deriving the correction-encoding name by inverting the false assumption |
| 6 | correction-integrity | Verifying both structural form checks encode the correction |
| 7 | failure-projection | Anchoring entry in the projected mis-design; failure is load-bearing |
| 8 | pattern-emergence | What only emerges when entries are read together |
| 9 | future-framing | Translating institutional memory into actionable guidance |

**Gatekeeper**
*First invocation: Step 3.* Sub-step shorthand:
`Gatekeeper: adversarial-rejection-only; epistemic dimension: {stage-label}`

```
GATEKEEPER -- FUNCTION DECLARATION
---------------------------------------------------------------------
Function:      Adversarial rejection. Tests predictability and cross-signal emergence.
Not-function:  Future-reader framing (IA domain).
Not-function:  Thematic synthesis or cross-item grouping.
Role boundary: Verdicts final. IA cannot reverse.
---------------------------------------------------------------------
```

Active: Step 3 only.

---

### Step 1 -- Read Signal Record

Namespaces covered (>=3 floor), total artifacts, date range. Record before expansion.
Gap noted if <3 namespaces.

---

### Step 2 -- Pre-Write Prediction Sort
*(IA: false-assumption-recovery; epistemic dimension: prior-frame-recovery)*

Route: `topic-story` | `topic-report` | `gate-pipeline`

Anti-hypothesis guard: "Confirms original hypothesis?" YES -> `topic-story`.
Discard log required, non-empty; route type, reason, destination per item.

---

### Step 3 -- Multi-Stage Epistemic Gate
*(Gatekeeper: adversarial-rejection-only)*

Anti-Pattern Catalog: CONFIRMATION | RESTATEMENT | ISOLATED-FINDING
Gate format: `VERDICT: SURPRISE | CUT -- {label}`

**Stage 1** *(Gatekeeper: adversarial-rejection-only; epistemic dimension: novelty)*
"Predictable from first principles?"
`PREDICTABLE` -> `topic-story` | `UNPREDICTABLE` -> Stage 2
**Commit**: `Stage 1: [{item}] -> [PREDICTABLE | UNPREDICTABLE]`

**Stage 2** *(Gatekeeper: adversarial-rejection-only; epistemic dimension: opposition)*
"Contradicts pre-investigation assumption?"
```
We believed: {falsifiable assumption}
VALID: {genuine falsification -- names belief and contradiction}
INVALID (absence-of-consideration): ...
INVALID (sentiment-reaction): ...
INVALID (hedge-uncertainty): ...
```
INVALID -> return to discard log as `topic-report`.
Floor: >=3 CONTRADICTION FOUND. `NO CONTRADICTION` -> `topic-report` | `CONTRADICTION FOUND` -> Stage 3
**Commit**: `Stage 2: [{item}] -> [NO CONTRADICTION | CONTRADICTION FOUND]`

**Stage 3** *(Gatekeeper: adversarial-rejection-only; epistemic dimension: specificity)*
"Cross-signal or single-artifact?"
`SINGLE-ARTIFACT` -> `topic-report` | `CROSS-SIGNAL (cite >=2 artifacts)` -> SURPRISE
**Commit**: `Stage 3: [{item}] -> [SINGLE-ARTIFACT | CROSS-SIGNAL] -- sources: [{a1}, {a2}]`

---

### Step 4 -- Pre-Write Impact Triage

HIGH | MEDIUM | LOW. Comparative; failure-first within tier. All assignments before expansion.

---

### Step 5 -- Naming Scaffold
*(IA: false-assumption-recovery; epistemic dimension: belief-inversion)*

1. Old belief. 2. Correction. 3. Domain. 4. Label: `The {Corrected Belief}: {Domain}`
VALID: "The Silent Veto: Adoption Workflow". INVALID: "Surprising Finding About Adoption".

---

### Step 6 -- Pre-Expansion Co-Validation Gate
*(IA: false-assumption-recovery; epistemic dimension: correction-integrity)*

Both VALID required. Either failing blocks expansion -- return to Step 5.
- Name form: `The {Corrected Belief}: {Domain}` -> VALID / INVALID
- Failure field: "If next team carries old assumption, {specific mis-design}" -> VALID / INVALID

---

### Step 7 -- Write Echo Entries
*(IA: false-assumption-recovery; epistemic dimension: failure-projection;
triage order; failure-first within tier)*

Begin from failure *(failure-projection)*: anchor on specific mis-design scenario.

**[`The {Corrected Belief}: {Domain}`]** -- *{HIGH | MEDIUM | LOW}*
*(IA: false-assumption-recovery; epistemic dimension: failure-projection)*

Source signal: `{artifact-name} ({namespace}/{skill})` `[CROSS: {A} x {B}]`
Temporal anchor: `{round/date}`
We believed: `{falsifiable assumption}`
The surprise: `{what signals revealed}`
If the next team carries old assumption: `{specific concrete mis-design}`.
Design impact: `{decision/assumption/scope}`.
Downstream route: `-> {skill or namespace}`.

---

### Step 8 -- Cross-Signal Synthesis

```
PHASE:        output
SCOPE:        synthesis only -- no new evidence; no re-expansion of entry fields;
              cross-entry pattern unreachable from single entry alone (state explicitly)
WORD BUDGET:  <=120 words (synthesis paragraph only)
INPUT:        named SURPRISE entries from Step 7 (>=2 required, cited by exact label)
OUTPUT:       synthesized paragraph + independence constraint stated in paragraph body
```

*(IA: false-assumption-recovery; epistemic dimension: pattern-emergence)*

Name >=2 SURPRISE entries by their exact labels. Explain what only emerges from reading
those entries together. State independence constraint explicitly in the paragraph.
Name the category of shared misunderstanding (C-16). <=120 words.

---

### Step 9 -- Forward Handover Guidance
*(IA: false-assumption-recovery; epistemic dimension: future-framing)*

T-1..T-4 register. State selection. Verify slots. Scenario and constraint both specific.

---

### Step 10 -- Rules of Thumb

<=3 rules. HIGH/MEDIUM only.

```
[{HIGH | MEDIUM}] {Rule -- <=20 words}
(encodes: {SURPRISE NAME})
```

Traceability check: tier match, no orphan rules, one-rule-per-surprise. Correct before verdict.

**Write verdict:**

```
TRACE-CHECK-VERDICT: [PASS | FAIL]
  -- PASS: all tiers match; no orphan rules; one-rule-per-surprise confirmed
  -- FAIL: {rule label | expected tier from Step 4 | actual tier in entry}
```

*A future reader verifies this check ran by locating TRACE-CHECK-VERDICT in the output --
no session replay required. PASS certifies tier-match, no-orphan, one-rule-per-surprise.
FAIL records each mismatch by rule label, expected tier, and actual tier.*

---

### Step 11 -- Gestalt Summary Audit

"Could this output be described as a summary of what the investigation found?"
If YES/PARTLY YES: revise, add `gestalt-summary-fail` to discard log, re-run.

```
GESTALT-VERDICT: [PASS | FAIL]
  -- PASS: output does not read as survey in aggregate; every entry is retroactively-
     visible surprise, not a survey item included for coverage
  -- FAIL: {each entry: label, gestalt-summary-fail trigger reason, revision applied}
```

*A future reader verifies this check ran by locating GESTALT-VERDICT in the output --
no session replay required. PASS certifies output as a whole does not pass the
summary-or-survey audit question. FAIL records revision decisions per entry.*

---

### Step 12 -- Production Chain Trace

```
PRODUCTION CHAIN TRACE
VERIFICATION NODES INCLUDED | DEPENDENCY GRAPH CLOSED
======================================================================

[NODE 1] typed-route prediction sort
  structural qualifier: IA: false-assumption-recovery; epistemic dimension:
    prior-frame-recovery co-activation, anti-hypothesis guard, typed destinations,
    non-empty discard log
  produces: route decisions, discard log
  consumed by: NODE 2

-> [NODE 2] staged gate verdict
  structural qualifier: Gatekeeper: adversarial-rejection-only; epistemic dimension per
    stage (novelty/opposition/specificity) at Stage headers, per-stage commits with
    collapse prohibition, VALID/INVALID gallery per Stage 2, cross-signal citation per
    Stage 3, floor tracked, Stage 2 INVALID -> return to discard log
  produces: SURPRISE verdicts, floor count
  consumed by: NODE 3

-> [NODE 3] comparative triage rank
  structural qualifier: simultaneous comparison, failure-first within tier,
    written before expansion
  produces: tier assignments, within-tier order
  consumed by: NODE 4 (headers), NODE 8 (TRACE-CHECK-VERDICT)

-> [NODE 4] echo entry
  structural qualifier: IA: false-assumption-recovery; epistemic dimension:
    failure-projection; 4-step scaffold; failure-first production; [CROSS] annotation;
    failure field as concrete mis-design; named impact
  produces: named labels, citations, impact, routes
  consumed by: NODE 5, NODE 6, NODE 7

-> [NODE 5] cross-signal synthesis [C-29: formal WORD BUDGET: contract at step header]
  structural qualifier: IA: false-assumption-recovery; epistemic dimension: pattern-emergence;
    PHASE+SCOPE+WORD BUDGET contract block at step header (C-29); >=2 named labels;
    cross-entry pattern unreachable from single entry; independence constraint explicit;
    misunderstanding category named (C-16)
  produces: synthesized paragraph with budget-bounded output
  consumed by: output (terminal)

-> [NODE 6] forward handover guidance
  structural qualifier: IA: false-assumption-recovery; epistemic dimension: future-framing;
    T-1..T-4 register; register stated; slots verified; source citable
  produces: handoff statement
  consumed by: output (terminal)

-> [NODE 7] impact-anchored rule
  structural qualifier: tier verified against NODE 3, orphan check, one-rule-per-surprise
  produces: verified rules (standard format; no {CATEGORY}: field -- C-28 not active)
  consumed by: NODE 8

-> [NODE 8] TRACE-CHECK-VERDICT
  structural qualifier: written PASS|FAIL token; certifies tier-match, no-orphan,
    one-rule-per-surprise; verifiable by token location; mismatches recorded if FAIL;
    forward-reader protocol at token
  produces: traceability audit result
  consumed by: NODE 11

-> [NODE 9] gestalt audit
  structural qualifier: IA on complete artifact, gestalt-fail distinct from gate-fail
  produces: gestalt result
  consumed by: NODE 10

-> [NODE 10] GESTALT-VERDICT
  structural qualifier: written PASS|FAIL token; certifies aggregate non-survey;
    revisions recorded if FAIL; forward-reader protocol at token
  produces: gestalt audit result
  consumed by: NODE 11

-> [NODE 11] chain trace (this node)
  structural qualifier: all nodes with verifiable qualifiers; NODE 5 named as C-29
    contract node; verification verdicts are chain nodes; dependencies annotated -- closed
  produces: closed dependency graph
  consumed by: output (terminal)

======================================================================
Dependency closure:
  NODE 3 -> NODE 8: triage rank feeds tier-match check
  NODE 9/10 -> NODE 11: gestalt verdict is named chain node
  NODE 8 -> NODE 11: traceability verdict is named chain node
  NODE 4 -> NODE 6: routing tags feed handover scenario selection
  Step 5 -> Step 6: naming scaffold feeds co-validation gate
  NODE 5 scope: WORD BUDGET <=120 words contract bounded at step header (C-29)
```

---

### Dependency Closure Enumeration

```
DEPENDENCY CLOSURE ENUMERATION
================================
NODE 3 output -> NODE 8:
  triage rank required for tier-match check

NODE 9/10 output -> NODE 11:
  gestalt verdict (NODE 10) is named chain node in NODE 11

NODE 8 output -> NODE 11:
  traceability verdict (NODE 8) is named chain node in NODE 11

NODE 4 output -> NODE 6:
  routing tags in entries feed handover scenario selection

Step 5 output -> Step 6:
  naming scaffold feeds co-validation name-form check

NODE 5 contract (C-29):
  WORD BUDGET: <=120 words declared at step header -- not embedded in prose;
  scoped to NODE 5 specifically, not inherited from global limit
================================
All 5 dependency loops + 1 C-29 contract anchor enumerated.
```

**Output**: Steps 7-12 + Dependency Closure Enumeration. Steps 1-6 are scaffolding.

---

## V-03 -- Single-axis: Formal Phase Contract Blocks at Every Named Step

**Variation axis:** Phrasing register. Every named pipeline step opens with a formal
`PHASE:` + `SCOPE:` contract block (and `WORD BUDGET:` where a word limit applies).
This extends the phase-contract discipline from data-collection steps uniformly across
the full pipeline, including the gate, triage, naming, validation, and audit steps.
The new criteria C-28 and C-29 are NOT activated: Step 8 has no taxonomy declaration
block, and while Step 8's WORD BUDGET appears inside its contract block, there is no
formal `WORD BUDGET:` contract header as a standalone field (C-29 requires the budget
to be a named contract field, not merely listed inside a PHASE block).

**Hypothesis:** R9 V-04 applied `PHASE:` + `WORD BUDGET:` only to data-collection steps.
A model executing the prompt sees a structural discontinuity: data-collection steps are
formally bounded; the gate, triage, naming, and synthesis steps are not. The hypothesis
is that formal phase declarations throughout improve execution discipline uniformly --
a model does not need to infer which steps are bounded -- even without adding C-28 or
C-29 specifically. V-03 vs V-05 isolates the value of C-28+C-29 by holding the
phrasing register constant at its highest level while leaving new criteria absent.

**Builds on:** R9 V-05 -- all prior criteria active.

**C-28 status:** Not activated. Step 8 has no CATEGORY DECLARATION block. Step 10 uses
standard audit row format.
**C-29 status:** Not activated. Step 8's word limit appears inside a PHASE block but
not as a standalone `WORD BUDGET:` contract field. C-29 requires a named contract field
on the synthesis step; having word-limit inside a shared PHASE block is PARTIAL at best.

---

### Prompt Body

You are running `/quest:topic echo` for the topic: {topic}.

All essential signals are in hand. Surface genuine surprises -- findings that only became
visible in retrospect, from cross-signal tension, that no competent practitioner would
have predicted before gathering evidence.

Not a summary. Not a survey. An echo: the signal that comes back that you didn't send.

---

### Roles

**Institutional Archaeologist (IA)**
Sub-step shorthand: `IA: false-assumption-recovery; epistemic dimension: {name}`
Active: Steps 2, 5, 6, 7, 8, 9.

| Step | Epistemic Dimension | Why here |
|------|---------------------|----------|
| 2 | prior-frame-recovery | Recovering what was actually believed, not what spec asserts |
| 5 | belief-inversion | Deriving correction-encoding name by inverting the false assumption |
| 6 | correction-integrity | Verifying both structural form checks encode the correction |
| 7 | failure-projection | Entry anchored in projected mis-design; failure is load-bearing |
| 8 | pattern-emergence | What only emerges when entries are read together |
| 9 | future-framing | Translating institutional memory into actionable guidance |

**Gatekeeper**
Sub-step shorthand: `Gatekeeper: adversarial-rejection-only; epistemic dimension:
{stage-label}` -- see Stage headers.

```
GATEKEEPER -- FUNCTION DECLARATION
---------------------------------------------------------------------
Function:      Adversarial rejection. Tests predictability and cross-signal emergence.
Not-function:  Future-reader framing (IA domain).
Not-function:  Thematic synthesis or cross-item grouping.
Role boundary: Verdicts final. IA cannot reverse.
---------------------------------------------------------------------
```

Active: Step 3 only.

---

### Step 1 -- Read Signal Record

```
PHASE:  intake
SCOPE:  read-only; no filtering or routing; record namespace coverage, artifact count,
        date range; stop before Step 2 begins
```

Read all signal artifacts across all namespaces (scout, draft, review, flow, trace, prove,
listen, program, topic). Record: namespaces covered (>=3 floor), total artifacts, date range.
Gap noted if <3 namespaces.

---

### Step 2 -- Pre-Write Prediction Sort

```
PHASE:  filter
SCOPE:  routing only -- assign route type to every finding; no entry generation;
        no expansion; gate-pipeline candidates pass through; all others to discard log
```

*(IA: false-assumption-recovery; epistemic dimension: prior-frame-recovery)*

Route: `topic-story` | `topic-report` | `gate-pipeline`
Anti-hypothesis guard: "Confirms original hypothesis?" YES -> `topic-story`.
Discard log required, non-empty; route type, reason, destination per item.

---

### Step 3 -- Multi-Stage Epistemic Gate

```
PHASE:  gate
SCOPE:  rejection testing only -- no triage, no expansion, no naming; each candidate
        receives a typed verdict token; stages are sequential artifacts, not combined
```

*(Gatekeeper: adversarial-rejection-only)*

Anti-Pattern Catalog: CONFIRMATION | RESTATEMENT | ISOLATED-FINDING
Gate format: `VERDICT: SURPRISE | CUT -- {label}`

**Stage 1** *(Gatekeeper: adversarial-rejection-only; epistemic dimension: novelty)*
"Predictable?" `PREDICTABLE` -> `topic-story` | `UNPREDICTABLE` -> Stage 2
**Commit**: `Stage 1: [{item}] -> [PREDICTABLE | UNPREDICTABLE]`

**Stage 2** *(Gatekeeper: adversarial-rejection-only; epistemic dimension: opposition)*
```
We believed: {falsifiable assumption}
VALID: {genuine falsification} | INVALID (absence-of-consideration / sentiment-reaction /
hedge-uncertainty): ...
```
INVALID -> return to discard log. Floor: >=3 CONTRADICTION FOUND.
`NO CONTRADICTION` -> `topic-report` | `CONTRADICTION FOUND` -> Stage 3
**Commit**: `Stage 2: [{item}] -> [NO CONTRADICTION | CONTRADICTION FOUND]`

**Stage 3** *(Gatekeeper: adversarial-rejection-only; epistemic dimension: specificity)*
"Cross-signal?" `SINGLE-ARTIFACT` -> `topic-report` | `CROSS-SIGNAL` -> SURPRISE
**Commit**: `Stage 3: [{item}] -> [SINGLE-ARTIFACT | CROSS-SIGNAL] -- sources: [{a1}, {a2}]`

---

### Step 4 -- Pre-Write Impact Triage

```
PHASE:  triage
SCOPE:  tier assignment only -- no entry generation; all candidates evaluated
        simultaneously before any single tier assigned; assignments written as
        artifact before Step 5 begins
```

HIGH | MEDIUM | LOW. Failure-first within tier. Write order: HIGH -> MEDIUM -> LOW.

---

### Step 5 -- Naming Scaffold

```
PHASE:  naming
SCOPE:  scaffold only -- work through 4-step derivation per candidate; no entry
        prose written here; output feeds Step 6 gate and Step 7 entry header
```

*(IA: false-assumption-recovery; epistemic dimension: belief-inversion)*

1. Old belief. 2. Correction. 3. Domain. 4. Label: `The {Corrected Belief}: {Domain}`
VALID: "The Silent Veto: Adoption Workflow". INVALID: "Surprising Finding About Adoption".

---

### Step 6 -- Pre-Expansion Co-Validation Gate

```
PHASE:  co-validation
SCOPE:  gate only -- simultaneous check of name form and failure field; no expansion
        until both VALID; failed candidate returns to Step 5
```

*(IA: false-assumption-recovery; epistemic dimension: correction-integrity)*

- Name form: `The {Corrected Belief}: {Domain}` -> VALID / INVALID
- Failure field: "If next team carries old assumption, {specific mis-design}" -> VALID / INVALID

Both VALID required per candidate. Either failing -> return to Step 5.

---

### Step 7 -- Write Echo Entries

```
PHASE:  entry generation
SCOPE:  one entry per confirmed SURPRISE; triage order with failure-first; begin from
        failure scenario; no new evidence; no triage revisions
WORD BUDGET:  per-entry fields as specified below; no running total
```

*(IA: false-assumption-recovery; epistemic dimension: failure-projection)*

Begin from failure: anchor on specific mis-design if old assumption is carried.

**[`The {Corrected Belief}: {Domain}`]** -- *{HIGH | MEDIUM | LOW}*
*(IA: false-assumption-recovery; epistemic dimension: failure-projection)*

Source signal: `{artifact-name} ({namespace}/{skill})` `[CROSS: {A} x {B}]`
Temporal anchor: `{round/date}`
We believed: `{assumption}` | The surprise: `{what was found}`
If the next team carries old assumption: `{specific concrete mis-design}`.
Design impact: `{decision/assumption/scope}`. Downstream route: `-> {consumer}`.

---

### Step 8 -- Cross-Signal Synthesis

```
PHASE:        output
SCOPE:        synthesis only -- no new evidence; pattern unreachable from single entry
              alone; independence constraint stated explicitly in paragraph body
WORD BUDGET:  <=120 words (synthesis paragraph)
INPUT:        named SURPRISE entries from Step 7 (>=2 required, cited by exact label)
OUTPUT:       synthesized paragraph with independence constraint; misunderstanding
              category named
```

*(IA: false-assumption-recovery; epistemic dimension: pattern-emergence)*

Name >=2 entries by exact label. State what only emerges when entries are read together.
Name the category of shared misunderstanding (C-16). Do not summarize; synthesize tension.

---

### Step 9 -- Forward Handover Guidance

```
PHASE:  handover
SCOPE:  one register selection from T-1..T-4; stated before writing; slots verified;
        no derivation of new evidence
```

*(IA: false-assumption-recovery; epistemic dimension: future-framing)*

T-1 (builder) | T-2 (reviewer) | T-3 (PM) | T-4 (architect). State selection.
Both scenario/decision/area/component and constraint specific. Source citable.

---

### Step 10 -- Rules of Thumb

```
PHASE:  rules
SCOPE:  <=3 rules; HIGH/MEDIUM only; traceability check before verdict; correct before writing
```

```
[{HIGH | MEDIUM}] {Rule -- <=20 words}
(encodes: {SURPRISE NAME})
```

Traceability check: tier match, no orphan rules, one-rule-per-surprise.

```
TRACE-CHECK-VERDICT: [PASS | FAIL]
  -- PASS: all tiers match; no orphan rules; one-rule-per-surprise confirmed
  -- FAIL: {mismatch detail}
```

*Forward-reader protocol: locate TRACE-CHECK-VERDICT token to verify check ran.*

---

### Step 11 -- Gestalt Summary Audit

```
PHASE:  gestalt audit
SCOPE:  applied to complete draft (Steps 7-10) as single unit; not entry-by-entry;
        revise until PASS
```

"Could this output be described as a summary of what the investigation found?"
Revise if YES/PARTLY YES. Add `gestalt-summary-fail` to discard log.

```
GESTALT-VERDICT: [PASS | FAIL]
  -- PASS: output does not read as survey in aggregate
  -- FAIL: {entries revised/discarded with gestalt-summary-fail reason}
```

*Forward-reader protocol: locate GESTALT-VERDICT token to verify check ran.*

---

### Step 12 -- Production Chain Trace

```
PHASE:  chain trace
SCOPE:  full pipeline with structural qualifiers; verification verdicts named as chain
        nodes; dependency graph closed; terminal artifact
```

```
PRODUCTION CHAIN TRACE
VERIFICATION NODES INCLUDED | DEPENDENCY GRAPH CLOSED
======================================================================

[NODE 1] typed-route prediction sort
  [PHASE: filter] structural qualifier: IA: false-assumption-recovery; epistemic
    dimension: prior-frame-recovery; anti-hypothesis guard; typed destinations;
    non-empty discard log
  produces: route decisions, discard log | consumed by: NODE 2

-> [NODE 2] staged gate verdict
  [PHASE: gate] structural qualifier: Gatekeeper: adversarial-rejection-only; per-stage
    epistemic dimensions; per-stage commits; VALID/INVALID gallery; floor tracked;
    Stage 2 INVALID -> return to discard log
  produces: SURPRISE verdicts, floor count | consumed by: NODE 3

-> [NODE 3] comparative triage rank
  [PHASE: triage] structural qualifier: simultaneous; failure-first; written before expansion
  produces: tier assignments, order
  consumed by: NODE 4 (headers), NODE 8 (TRACE-CHECK-VERDICT)

-> [NODE 4] echo entry
  [PHASE: entry generation] structural qualifier: IA: false-assumption-recovery;
    epistemic dimension: failure-projection; 4-step scaffold; failure-first; [CROSS];
    failure field; named impact
  produces: labels, citations, impact, routes
  consumed by: NODE 5, NODE 6, NODE 7

-> [NODE 5] cross-signal synthesis
  [PHASE: output] structural qualifier: IA: false-assumption-recovery; epistemic
    dimension: pattern-emergence; WORD BUDGET <=120 words in PHASE block;
    >=2 named labels; cross-entry pattern; independence constraint explicit; C-16 named
  produces: synthesized paragraph (word-bounded via PHASE block, not standalone contract)
  consumed by: output (terminal)

-> [NODE 6] forward handover guidance
  [PHASE: handover] structural qualifier: T-1..T-4 register; stated before writing;
    slots verified; source citable
  produces: handoff statement | consumed by: output (terminal)

-> [NODE 7] impact-anchored rule
  [PHASE: rules] structural qualifier: tier vs NODE 3; orphan check; one-rule-per-surprise
  produces: verified rules | consumed by: NODE 8

-> [NODE 8] TRACE-CHECK-VERDICT
  structural qualifier: PASS|FAIL token; certifies tier-match, no-orphan,
    one-rule-per-surprise; forward-reader protocol at token
  produces: traceability result | consumed by: NODE 11

-> [NODE 9] gestalt audit
  [PHASE: gestalt audit] structural qualifier: IA on complete artifact; gestalt-fail distinct
  produces: gestalt result | consumed by: NODE 10

-> [NODE 10] GESTALT-VERDICT
  structural qualifier: PASS|FAIL token; certifies aggregate non-survey;
    revisions recorded; forward-reader protocol
  produces: gestalt result | consumed by: NODE 11

-> [NODE 11] chain trace (this node)
  [PHASE: chain trace] structural qualifier: all nodes with phase labels; verification
    verdicts as chain nodes; dependencies annotated -- graph closed
  produces: closed dependency graph | consumed by: output (terminal)

======================================================================
Dependency closure:
  NODE 3 -> NODE 8: triage rank feeds tier-match check
  NODE 9/10 -> NODE 11: gestalt verdict is named chain node
  NODE 8 -> NODE 11: traceability verdict is named chain node
  NODE 4 -> NODE 6: routing tags feed handover scenario selection
  Step 5 -> Step 6: naming scaffold feeds co-validation gate
```

---

### Dependency Closure Enumeration

```
DEPENDENCY CLOSURE ENUMERATION
================================
NODE 3 -> NODE 8: triage rank feeds tier-match check
NODE 9/10 -> NODE 11: gestalt verdict is named chain node
NODE 8 -> NODE 11: traceability verdict is named chain node
NODE 4 -> NODE 6: routing tags feed handover scenario selection
Step 5 -> Step 6: naming scaffold feeds co-validation gate
================================
All 5 loops enumerated.
```

**Output**: Steps 7-12 + Dependency Closure Enumeration. Steps 1-6 are scaffolding.

---

## V-04 -- Combined: C-28 + C-29, no formal phase blocks

**Variation axis:** C-28 (category-field audit propagation) + C-29 (synthesis-step budget
contract). Taxonomy declaration block present in Step 8; `{CATEGORY}:` field in Step 10
audit rows; formal `WORD BUDGET:` contract header on Step 8. Formal `PHASE:` + `SCOPE:`
blocks NOT extended to all other steps -- they remain in their R9 V-05 form.

**Hypothesis:** C-28 and C-29 activate at non-overlapping positions: C-28 at the synthesis
output step and its downstream audit consumer (Step 8 declaration -> Step 10 rows);
C-29 at the synthesis step's header as a standalone contract field. Together they close
the two R9 gaps identified in the differential. The phrasing register axis (V-03) is a
separate concern about uniform step formatting. V-04 tests whether the two new criteria
together are sufficient for a high score on v10 without the V-03 phase-block extension.
If V-04 scores lower than V-05, the delta is the phrasing register axis alone.

**Builds on:** V-01 (C-28 mechanism) + V-02 (C-29 mechanism). Phase block extension
from V-03 not present.

---

### Prompt Body

You are running `/quest:topic echo` for the topic: {topic}.

All essential signals are in hand. Your task: surface the genuine surprises -- findings that
only became visible in retrospect, from cross-signal tension, that no competent practitioner
would have predicted before gathering evidence.

Not a summary. Not a survey of discoveries. An echo: the signal that comes back that you
didn't send.

---

### Roles

**Institutional Archaeologist (IA)**
*First invocation: Step 2.*
Sub-step shorthand: `IA: false-assumption-recovery; epistemic dimension: {name}`
Active: Steps 2, 5, 6, 7, 8, 9.

| Step | Epistemic Dimension | Why here |
|------|---------------------|----------|
| 2 | prior-frame-recovery | Recovering what was actually believed, not what spec asserts |
| 5 | belief-inversion | Deriving correction-encoding name by inverting the false assumption |
| 6 | correction-integrity | Verifying both structural form checks encode the correction |
| 7 | failure-projection | Entry anchored in projected mis-design; failure is load-bearing |
| 8 | pattern-emergence | What only emerges when entries are read together |
| 9 | future-framing | Translating institutional memory into actionable guidance |

**Gatekeeper**
*First invocation: Step 3.*
Sub-step shorthand: `Gatekeeper: adversarial-rejection-only; epistemic dimension:
{stage-label}` -- see Stage headers.

```
GATEKEEPER -- FUNCTION DECLARATION
---------------------------------------------------------------------
Function:      Adversarial rejection. Tests predictability and cross-signal emergence.
Not-function:  Future-reader framing (IA domain).
Not-function:  Thematic synthesis or cross-item grouping.
Role boundary: Verdicts final. IA cannot reverse.
---------------------------------------------------------------------
```

Active: Step 3 only.

---

### Step 1 -- Read Signal Record

Read all signal artifacts across all namespaces (scout, draft, review, flow, trace, prove,
listen, program, topic). Record: namespaces covered (>=3 floor), total artifacts, date range.
Gap noted if <3 namespaces.

---

### Step 2 -- Pre-Write Prediction Sort
*(IA: false-assumption-recovery; epistemic dimension: prior-frame-recovery -- recovering
what beliefs were actually held before investigation, not what the spec states)*

Route: `topic-story` | `topic-report` | `gate-pipeline`

Anti-hypothesis guard *(IA: false-assumption-recovery; epistemic dimension:
prior-frame-recovery)*: "Confirms original hypothesis?" YES -> `topic-story`.

Discard log: every non-gate item with route type, reason (1 sentence), destination.
Non-empty required.

---

### Step 3 -- Multi-Stage Epistemic Gate
*(Gatekeeper: adversarial-rejection-only)*

Anti-Pattern Catalog: CONFIRMATION | RESTATEMENT | ISOLATED-FINDING
Gate format: `VERDICT: SURPRISE | CUT -- {label}`

**Stage 1** *(Gatekeeper: adversarial-rejection-only; epistemic dimension: novelty --
separating investigation-emergent from predictable-from-materials)*
"Predictable?" `PREDICTABLE` -> `topic-story` | `UNPREDICTABLE` -> Stage 2
**Commit**: `Stage 1: [{item}] -> [PREDICTABLE | UNPREDICTABLE]`

**Stage 2** *(Gatekeeper: adversarial-rejection-only; epistemic dimension: opposition --
separating genuine contradiction of a held belief from mere notability)*
"Contradicts pre-investigation assumption?"
```
We believed: {falsifiable assumption -- names specific held belief}
VALID: {genuine falsification -- names belief and contradiction}
INVALID (absence-of-consideration): ...
INVALID (sentiment-reaction): ...
INVALID (hedge-uncertainty): ...
```
INVALID -> return to discard log as `topic-report`.
Floor: >=3 CONTRADICTION FOUND.
**Commit**: `Stage 2: [{item}] -> [NO CONTRADICTION | CONTRADICTION FOUND]`

**Stage 3** *(Gatekeeper: adversarial-rejection-only; epistemic dimension: specificity --
separating traceable cross-signal findings from single-artifact findings)*
"Cross-signal?" `SINGLE-ARTIFACT` -> `topic-report` | `CROSS-SIGNAL` -> SURPRISE
**Commit**: `Stage 3: [{item}] -> [SINGLE-ARTIFACT | CROSS-SIGNAL] -- sources: [{a1}, {a2}]`

---

### Step 4 -- Pre-Write Impact Triage

Assign comparatively. HIGH | MEDIUM | LOW. Failure-first within tier.
All assignments written before any expansion begins.

---

### Step 5 -- Naming Scaffold
*(IA: false-assumption-recovery; epistemic dimension: belief-inversion -- the name is
derived by inverting the false assumption; encodes what was wrong and where)*

1. Old belief. 2. Correction. 3. Domain. 4. Label: `The {Corrected Belief}: {Domain}`
VALID: "The Silent Veto: Adoption Workflow". INVALID: "Surprising Finding About Adoption".

---

### Step 6 -- Pre-Expansion Co-Validation Gate
*(IA: false-assumption-recovery; epistemic dimension: correction-integrity)*

Both VALID required. Either failing blocks expansion -- return to Step 5.
- Name form: `The {Corrected Belief}: {Domain}` -> VALID / INVALID
- Failure field: "If next team carries old assumption, {specific mis-design}" -> VALID / INVALID

---

### Step 7 -- Write Echo Entries
*(IA: false-assumption-recovery; epistemic dimension: failure-projection;
triage order; failure-first within tier)*

Begin from failure *(failure-projection)*: If next team carries old assumption about
{domain}, they would {specific mis-design}. Anchor.

**[`The {Corrected Belief}: {Domain}`]** -- *{HIGH | MEDIUM | LOW}*
*(IA: false-assumption-recovery; epistemic dimension: failure-projection)*

Source signal: `{artifact-name} ({namespace}/{skill})`
`[CROSS: {artifact-A} x {artifact-B}]`
Temporal anchor: `{round or date}`
We believed: `{falsifiable assumption}`
The surprise: `{what signals revealed}`
If the next team carries old assumption: `{specific concrete mis-design}`.
Design impact: `{decision revisited / assumption struck / scope boundary shifted}`.
Downstream route: `-> {skill or namespace}`.

---

### Step 8 -- Cross-Signal Synthesis

```
PHASE:        output
SCOPE:        synthesis only -- no new evidence; no re-expansion of entry fields;
              cross-entry pattern unreachable from single entry alone
WORD BUDGET:  <=120 words (synthesis paragraph; taxonomy declaration lines not counted)
INPUT:        named SURPRISE entries from Step 7 (>=2 required, cited by exact label)
OUTPUT:       taxonomy declaration + synthesized paragraph with independence constraint
```

*(IA: false-assumption-recovery; epistemic dimension: pattern-emergence -- naming what
only becomes visible when entries are read together; unreachable from any single entry
alone)*

**Taxonomy declaration (C-16 -> C-28 propagation upstream source):**
Before writing the synthesis paragraph, declare the misunderstanding-category taxonomy.
Categories typed by misunderstanding class, not topic.

```
CATEGORY DECLARATION:
  {SURPRISE NAME-A} -> {CATEGORY}: capability-underestimation |
                       integration-surface-blindness | pricing-model-conflation |
                       scope-assumption-failure | adoption-friction-blindness |
                       lifecycle-phase-conflation
  {SURPRISE NAME-B} -> {CATEGORY}: {taxonomy-label}
  {SURPRISE NAME-C} -> {CATEGORY}: {taxonomy-label}
```

This declaration is the upstream source for the `{CATEGORY}:` field in Step 10 audit rows.
Do not proceed to synthesis paragraph without completing the declaration.

**Synthesis paragraph:**
Name >=2 entries by exact label. State what only emerges from reading them together.
State the independence constraint explicitly. Name the category of shared misunderstanding.
<=120 words.

---

### Step 9 -- Forward Handover Guidance
*(IA: false-assumption-recovery; epistemic dimension: future-framing)*

T-1..T-4 register. State selection before writing. Verify slot assignments.
Scenario and constraint both specific. Source citable.

---

### Step 10 -- Rules of Thumb

<=3 rules. HIGH/MEDIUM only.

**Audit row schema (C-28: category-field propagation from Step 8 CATEGORY DECLARATION):**

```
[{HIGH | MEDIUM}] {Rule -- <=20 words, quotable standalone heuristic}
(encodes: {SURPRISE NAME} -> {CATEGORY}: {taxonomy-label-from-Step-8-declaration})
```

The `{CATEGORY}:` field must reference a label from the Step 8 CATEGORY DECLARATION block.
Absent category -> return to Step 8 and update before writing the rule.

Traceability check:
1. Each rule's tier matches named surprise's triage tier from Step 4
2. Each rule traceable to exactly one named surprise (no orphan rules)
3. No surprise generates more than one rule
4. Each `{CATEGORY}:` references a declared taxonomy label (C-28 check)

Correct all mismatches before writing verdict.

**Write verdict:**

```
TRACE-CHECK-VERDICT: [PASS | FAIL]
  -- PASS: all tiers match; no orphan rules; one-rule-per-surprise confirmed;
           all {CATEGORY}: fields reference Step 8 taxonomy labels
  -- FAIL: {rule label | expected tier | actual tier | or absent {CATEGORY}: field}
```

*A future reader verifies this check ran by locating TRACE-CHECK-VERDICT in the output --
no session replay required. PASS certifies tier-match, no-orphan, one-rule-per-surprise,
and {CATEGORY}: field propagation from Step 8 taxonomy (C-28 confirmed).*

---

### Step 11 -- Gestalt Summary Audit

*Applied to complete draft (Steps 7-10) as a single unit.*

"Could this output be described as a summary of what the investigation found?"
If YES/PARTLY YES: revise, add `gestalt-summary-fail` to discard log, re-run.

```
GESTALT-VERDICT: [PASS | FAIL]
  -- PASS: output does not read as survey in aggregate; every entry retroactively-visible
  -- FAIL: {each entry: label, gestalt-summary-fail trigger reason, revision applied}
```

*A future reader verifies by locating GESTALT-VERDICT. PASS certifies aggregate non-survey.
FAIL records revision decisions per entry.*

---

### Step 12 -- Production Chain Trace

```
PRODUCTION CHAIN TRACE
VERIFICATION NODES INCLUDED | DEPENDENCY GRAPH CLOSED
======================================================================

[NODE 1] typed-route prediction sort
  structural qualifier: IA: false-assumption-recovery; epistemic dimension:
    prior-frame-recovery co-activation, anti-hypothesis guard, typed destinations,
    non-empty discard log
  produces: route decisions, discard log
  consumed by: NODE 2

-> [NODE 2] staged gate verdict
  structural qualifier: Gatekeeper: adversarial-rejection-only; epistemic dimension per
    stage (novelty/opposition/specificity) at Stage headers, per-stage commits with
    collapse prohibition, VALID/INVALID gallery, cross-signal citation, floor tracked,
    Stage 2 INVALID -> return to discard log
  produces: SURPRISE verdicts, floor count
  consumed by: NODE 3

-> [NODE 3] comparative triage rank
  structural qualifier: simultaneous, failure-first, written before expansion
  produces: tier assignments, within-tier order
  consumed by: NODE 4 (headers), NODE 8 (TRACE-CHECK-VERDICT)

-> [NODE 3b] taxonomy declaration [C-16 -> C-28]
  structural qualifier: IA: false-assumption-recovery; epistemic dimension: pattern-emergence;
    per-surprise {NAME} -> {CATEGORY}: typed mapping declared before synthesis paragraph;
    categories typed by misunderstanding class; C-28 upstream source
  produces: category taxonomy (C-16), per-surprise map (C-28 upstream)
  consumed by: NODE 5 (synthesis names category), NODE 7 ({CATEGORY}: field in audit row)

-> [NODE 4] echo entry
  structural qualifier: IA: false-assumption-recovery; epistemic dimension:
    failure-projection; 4-step scaffold; failure-first; [CROSS] annotation;
    failure field as concrete mis-design; named impact
  produces: named labels, citations, impact, routes
  consumed by: NODE 5, NODE 6, NODE 7

-> [NODE 5] cross-signal synthesis [C-28 + C-29: taxonomy consumer + budget contract]
  structural qualifier: IA: false-assumption-recovery; epistemic dimension: pattern-emergence;
    PHASE+SCOPE+WORD BUDGET contract block at step header (C-29); >=2 named labels;
    cross-entry pattern unreachable from single entry; independence constraint explicit;
    misunderstanding category named from NODE 3b taxonomy (C-16)
  produces: synthesized paragraph (budget-bounded; category-typed)
  consumed by: output (terminal)

-> [NODE 6] forward handover guidance
  structural qualifier: T-1..T-4 register; stated before writing; slots verified; source citable
  produces: handoff statement
  consumed by: output (terminal)

-> [NODE 7] impact-anchored rule with category field [C-28 consumer]
  structural qualifier: tier verified against NODE 3; orphan check; one-rule-per-surprise;
    {CATEGORY}: field references NODE 3b taxonomy -- absent category -> return to NODE 3b
  produces: verified rules with tier labels and {CATEGORY}: fields
  consumed by: NODE 8

-> [NODE 8] TRACE-CHECK-VERDICT
  structural qualifier: written PASS|FAIL token; certifies tier-match, no-orphan,
    one-rule-per-surprise, and {CATEGORY}: field presence (C-28 check); forward-reader
    protocol; records mismatches if FAIL
  produces: traceability audit result including C-28 field check
  consumed by: NODE 11

-> [NODE 9] gestalt audit
  structural qualifier: IA on complete artifact; gestalt-fail distinct from gate-fail
  produces: gestalt result
  consumed by: NODE 10

-> [NODE 10] GESTALT-VERDICT
  structural qualifier: PASS|FAIL token; certifies aggregate non-survey;
    revisions recorded if FAIL; forward-reader protocol
  produces: gestalt audit result
  consumed by: NODE 11

-> [NODE 11] chain trace (this node)
  structural qualifier: all nodes with verifiable qualifiers; NODE 3b (taxonomy,
    C-28 upstream) and its propagation to NODE 5 (synthesis) and NODE 7 (audit rows)
    explicitly named as dependency links; NODE 5 budget contract (C-29) named;
    verification verdicts are chain nodes; dependencies annotated -- graph is closed
  produces: closed dependency graph
  consumed by: output (terminal)

======================================================================
Dependency closure:
  NODE 3 -> NODE 8: triage rank feeds tier-match check
  NODE 3b -> NODE 5: taxonomy feeds synthesis category naming (C-16/C-28)
  NODE 3b -> NODE 7: taxonomy feeds {CATEGORY}: field in audit rows (C-28)
  NODE 9/10 -> NODE 11: gestalt verdict is named chain node
  NODE 8 -> NODE 11: traceability verdict is named chain node
  NODE 4 -> NODE 6: routing tags feed handover scenario selection
  Step 5 -> Step 6: naming scaffold feeds co-validation gate
  NODE 5 scope: WORD BUDGET <=120 words as standalone contract field at step header (C-29)
```

---

### Dependency Closure Enumeration

```
DEPENDENCY CLOSURE ENUMERATION
================================
NODE 3 -> NODE 8:
  triage rank (NODE 3) is required input for tier-match check (NODE 8)

NODE 3b -> NODE 5 (C-16/C-28):
  taxonomy declaration (NODE 3b) is source for synthesis category naming;
  NODE 5 cannot produce C-16-compliant synthesis without NODE 3b output

NODE 3b -> NODE 7 (C-28):
  taxonomy declaration (NODE 3b) is required input for {CATEGORY}: field in audit rows;
  NODE 7 cannot produce a C-28-compliant row without NODE 3b output

NODE 9/10 -> NODE 11:
  gestalt verdict (NODE 10) is named chain node in NODE 11

NODE 8 -> NODE 11:
  traceability verdict (NODE 8) is named chain node in NODE 11

NODE 4 -> NODE 6:
  routing tags in entries (NODE 4) feed handover scenario selection (NODE 6)

Step 5 -> Step 6:
  naming scaffold (Step 5) feeds co-validation name-form check (Step 6)

NODE 5 budget contract (C-29):
  WORD BUDGET: <=120 words is a standalone contract field at NODE 5's step header,
  not embedded in prose; scoped to synthesis step specifically
================================
All 7 loops + 1 C-29 contract anchor enumerated.
```

**Output**: Steps 7-12 + Dependency Closure Enumeration. Steps 1-6 are scaffolding.

---

## V-05 -- Full Synthesis: C-28 + C-29 + Formal Phase Contract Blocks

**Variation axis:** Full combination -- C-28 (category-field audit propagation),
C-29 (synthesis-step budget contract), and the phrasing register axis (formal
`PHASE:` + `SCOPE:` + `WORD BUDGET:` blocks at every named pipeline step) all active
simultaneously, composing with all prior criteria from R9 V-05.

**Hypothesis:** C-28 and C-29 activate at two non-overlapping structural positions:
C-28 at the synthesis step (taxonomy declaration) and its downstream audit consumer
(Step 10 audit rows); C-29 at the synthesis step header as a standalone formal contract
field. The phrasing register axis (V-03) adds formal phase declarations throughout,
closing the structural inconsistency where data-collection steps carry contract blocks
but the gate, triage, naming, and synthesis steps do not. Together the three axes produce
an artifact where: (1) the category taxonomy is structurally required to propagate from
synthesis into audit fields, not optional, (2) the synthesis step's word budget is a
formal contract that any reviewer can verify at a glance without reading the step body,
and (3) every pipeline step has an explicit scope contract that prevents scope-bleed
between phases. V-05 is designed to become the new baseline for v11 development.

**Builds on:** R9 V-05 (all prior criteria) + V-01 (C-28) + V-02 (C-29) + V-03 (phase
contract blocks throughout).

---

### Prompt Body

You are running `/quest:topic echo` for the topic: {topic}.

All essential signals are in hand. Your task: surface the genuine surprises -- findings
that only became visible in retrospect, from cross-signal tension, that no competent
practitioner would have predicted before gathering evidence.

Not a summary. Not a survey of discoveries. An echo: the signal that comes back that you
didn't send.

---

### Roles *(C-28/C-29: taxonomy and budget contract nodes named in chain trace;
phrasing register: formal PHASE+SCOPE blocks at every step)*

**Institutional Archaeologist (IA)**
*First invocation: Step 2.*
Function: Recovers false assumptions embedded in current materials -- what a future team
would carry as truth without knowing otherwise. Frames every surprise as a correction to a
false assumption. Derives consequence by asking "What would the next team build wrong?"
The IA is the author of implication; the Gatekeeper is the author of rejection.

Sub-step co-activation shorthand: each IA invocation carries:
`IA: false-assumption-recovery; epistemic dimension: {name}`
The epistemic dimension names why this posture applies at this specific step.

Defined dimensions:

| Step | Epistemic Dimension | Why here |
|------|---------------------|----------|
| 2 | prior-frame-recovery | Recovering what was actually believed, not what spec asserts |
| 5 | belief-inversion | Deriving correction-encoding name by inverting the false assumption |
| 6 | correction-integrity | Verifying both structural form checks encode the correction |
| 7 | failure-projection | Entry anchored in projected mis-design; failure is load-bearing |
| 8 | pattern-emergence | What only emerges when entries are read together; absent from any single |
| 9 | future-framing | Translating institutional memory into actionable guidance |

Active: Steps 2, 5, 6, 7, 8, 9.

**Gatekeeper**
*First invocation: Step 3.*
Sub-step shorthand: `Gatekeeper: adversarial-rejection-only; epistemic dimension:
{stage-label}` -- see Stage headers.

```
GATEKEEPER -- FUNCTION DECLARATION
---------------------------------------------------------------------
Function:      Adversarial rejection. Tests each gate-pipeline candidate: (1)
               first-principles predictability; (2) cross-signal requirement.
               Fails either: rejected.

Not-function:  Future-reader framing. The Gatekeeper does not ask what the
               next team would get wrong. That is the IA's domain.

Not-function:  Thematic synthesis or cross-item grouping. The Gatekeeper
               evaluates each candidate in isolation.

Role boundary: Gatekeeper verdicts are final. The IA cannot reverse a rejection.
---------------------------------------------------------------------
```

Active: Step 3 only.

---

### Step 1 -- Read Signal Record

```
PHASE:  intake
SCOPE:  read-only; no filtering or routing; record namespace coverage, artifact count,
        date range; stop before Step 2 begins
```

Read all signal artifacts across all namespaces (scout, draft, review, flow, trace, prove,
listen, program, topic). Record:
- Namespaces covered -- must reach >=3 distinct namespaces (namespace floor)
- Total artifacts read
- Date range (earliest -> latest)

Gap noted if <3 namespaces. Coverage record visible in output before entry expansion begins.

---

### Step 2 -- Pre-Write Prediction Sort

```
PHASE:  filter
SCOPE:  routing only -- assign route type to every finding; no entry generation;
        no expansion; gate-pipeline candidates pass to Step 3; all others to discard log
```

*(IA: false-assumption-recovery; epistemic dimension: prior-frame-recovery -- recovering
what beliefs were actually held before investigation, not what the spec states)*

Route types:
- `topic-story` -- confirms hypothesis; destination: topic narrative
- `topic-report` -- restates known constraint; destination: report
- `gate-pipeline` -- candidate surprise; proceeds to Step 3

Anti-hypothesis guard *(IA: false-assumption-recovery; epistemic dimension:
prior-frame-recovery)*: "Does this item confirm what the investigation set out to prove?"
YES -> `topic-story`, regardless of apparent novelty.

Pre-expansion co-validation: "A new team from the spec alone would not have encountered
this." Cannot confirm -> `topic-report`.

Discard log: every non-gate item with route type, reason (1 sentence), downstream
destination. Non-empty discard log required. Empty log indicates filter was not applied.

---

### Step 3 -- Multi-Stage Epistemic Gate

```
PHASE:  gate
SCOPE:  rejection testing only -- no triage, no expansion, no naming; each candidate
        receives a typed verdict token before any entry work; stages are sequential
        written artifacts, not combined
```

*(Gatekeeper: adversarial-rejection-only)*

```
GATEKEEPER: adversarial-rejection-only -- active from here through end of Stage 3.
```

**Anti-Pattern Catalog**:
- CONFIRMATION: confirms original hypothesis even if unpredicted -> PREDICTABLE
- RESTATEMENT: documents known constraint or spec requirement -> route `topic-report`
- ISOLATED-FINDING: finding complete in one artifact; no cross-signal emergence -> `topic-report`

**Gate format**: `VERDICT: SURPRISE | CUT -- {anti-pattern label if CUT}`

**Three sequential stages. Per-stage commit required. Collapse prohibition: do not write
a combined multi-stage verdict. Each stage result is a written artifact before the next
begins.**

---

**Stage 1 -- Prediction Test**
*(Gatekeeper: adversarial-rejection-only; epistemic dimension: novelty -- separating
investigation-emergent findings from outcomes predictable from original design materials)*

"Would a competent practitioner have predicted this from first principles, prior to any
signal gathering?"

`PREDICTABLE` -> route to `topic-story`; discard log
`UNPREDICTABLE` -> Stage 2

**Commit**: `Stage 1: [{item label}] -> [PREDICTABLE | UNPREDICTABLE]`

---

**Stage 2 -- Contradiction Test**
*(Gatekeeper: adversarial-rejection-only; epistemic dimension: opposition -- separating
genuine contradiction of a held belief from findings that are merely notable or unusual)*

"Does this item contradict, complicate, or qualify an assumption from the pre-investigation
frame?"

```
We believed: {falsifiable pre-investigation assumption -- names a specific belief held}
VALID: {case that genuinely falsifies the belief -- names belief and contradiction}
INVALID (absence-of-consideration): {notes absence rather than falsifying a held belief}
INVALID (sentiment-reaction): {expresses surprise without naming the assumption that
   turned out to be false}
INVALID (hedge-uncertainty): {hedges on whether the belief was ever held}
```

If INVALID -> candidate fails Stage 2 -> return to discard log as `topic-report`.

Minimum surprise floor: >=3 candidates must reach CONTRADICTION FOUND. If fewer than 3,
record as floor-miss. Do not suppress it.

`NO CONTRADICTION` -> route to `topic-report`; discard log
`CONTRADICTION FOUND` -> Stage 3

**Commit**: `Stage 2: [{item label}] -> [NO CONTRADICTION | CONTRADICTION FOUND]`

---

**Stage 3 -- Attribution Test**
*(Gatekeeper: adversarial-rejection-only; epistemic dimension: specificity -- separating
traceable cross-signal findings from single-artifact findings that cannot generate an echo)*

"Does this finding emerge only when two or more signal artifacts are read together?"

`SINGLE-ARTIFACT` -> route to `topic-report`; discard log
`CROSS-SIGNAL (cite >=2 source artifacts)` -> verdict SURPRISE

**Commit**: `Stage 3: [{item label}] -> [SINGLE-ARTIFACT | CROSS-SIGNAL] -- sources:
[{artifact1 (namespace/skill)}, {artifact2 (namespace/skill)}]`

---

### Step 4 -- Pre-Write Impact Triage

```
PHASE:  triage
SCOPE:  tier assignment only -- no entry generation; all candidates evaluated
        simultaneously before any tier assigned; all assignments written as artifact
        before Step 5 begins
```

- **HIGH**: Forces revision to core design decision, assumption, or scope boundary
- **MEDIUM**: Qualifies design principle or adds constraint to existing decision
- **LOW**: Notable; no clear design consequence at present

Failure-first ordering within each tier. Write order: HIGH -> MEDIUM -> LOW.

---

### Step 5 -- Naming Scaffold

```
PHASE:  naming
SCOPE:  scaffold only -- work through 4-step derivation per candidate; no entry prose
        written here; output is candidate label feeding Step 6 gate and Step 7 header
```

*(IA: false-assumption-recovery; epistemic dimension: belief-inversion -- the name is
derived by inverting the false assumption; encodes what was wrong and where, not a
description of the discovery)*

1. State old belief: "The team carried the assumption that ___."
2. State correction: "The signals revealed instead that ___."
3. Derive domain: "This affects the ___ area of the design."
4. Form label: `The {Corrected Belief}: {Domain}`

VALID: "The Silent Veto: Adoption Workflow" -- encodes what was wrong and where.
INVALID: "Surprising Finding About Adoption" -- describes discovery, not corrected belief.

---

### Step 6 -- Pre-Expansion Co-Validation Gate

```
PHASE:  co-validation
SCOPE:  gate only -- simultaneous check of name form and failure field; no expansion
        until both VALID; failed candidate returns to Step 5 for revision
```

*(IA: false-assumption-recovery; epistemic dimension: correction-integrity -- verifying
that both structural form checks encode the correction before any expansion begins;
neither alone suffices)*

- **Name form**: follows `The {Corrected Belief}: {Domain}`? -> VALID / INVALID
- **Failure field**: reads as "If the next team carries the old assumption,
  {specific concrete mis-design}" -- named mis-design, not change-list? -> VALID / INVALID

Both VALID required. Either failing blocks expansion -- return to Step 5.

---

### Step 7 -- Write Echo Entries

```
PHASE:        entry generation
SCOPE:        one entry per confirmed SURPRISE; triage order with failure-first within
              tier; begin from failure scenario; no new evidence; no triage revisions
WORD BUDGET:  per-entry fields as specified in template; no running word total
INPUT:        confirmed SURPRISE candidates from Step 3 with triage tiers from Step 4
              and validated labels from Step 6
OUTPUT:       one fully populated entry per SURPRISE, failure-first within tier
```

*(IA: false-assumption-recovery; epistemic dimension: failure-projection -- entry begins
from the projected mis-design; failure scenario is load-bearing, not derived)*

Begin from failure *(failure-projection)*: If the next team carries the old assumption
about {domain}, they would {specific mis-design}. Anchor.

---

**[`The {Corrected Belief}: {Domain}`]** -- *{HIGH | MEDIUM | LOW}*
*(IA: false-assumption-recovery; epistemic dimension: failure-projection)*

Source signal: `{artifact-name} ({namespace}/{skill})`
`[CROSS: {artifact-A} x {artifact-B}]`
Temporal anchor: `{round or date of earliest contributing signal}`
We believed: `{falsifiable pre-investigation assumption}`
The surprise: `{what signals revealed that contradicts the prior assumption}`
If the next team carries the old assumption: `{specific concrete mis-design}`.
Design impact: `{decision revisited / assumption struck / scope boundary shifted}`.
Downstream route: `-> {skill or namespace}`.

---

### Step 8 -- Cross-Signal Synthesis

```
PHASE:        output
SCOPE:        synthesis only -- no new evidence; no re-expansion of entry fields;
              cross-entry pattern unreachable from single entry alone; independence
              constraint stated explicitly in paragraph body
WORD BUDGET:  <=120 words (synthesis paragraph; taxonomy declaration lines not counted)
INPUT:        named SURPRISE entries from Step 7 (>=2 required, cited by exact label)
OUTPUT:       taxonomy declaration + synthesized paragraph with independence constraint
              + named misunderstanding category
```

*(IA: false-assumption-recovery; epistemic dimension: pattern-emergence -- naming what
only becomes visible when entries are read together; unreachable from any single entry
alone)*

**Taxonomy declaration (C-16 -> C-28 upstream source):**
Before writing the synthesis paragraph, declare the misunderstanding-category taxonomy
across all SURPRISE entries. Categories are typed by misunderstanding class, not topic.

```
CATEGORY DECLARATION:
  {SURPRISE NAME-A} -> {CATEGORY}: capability-underestimation |
                       integration-surface-blindness | pricing-model-conflation |
                       scope-assumption-failure | adoption-friction-blindness |
                       lifecycle-phase-conflation | [or other typed class]
  {SURPRISE NAME-B} -> {CATEGORY}: {taxonomy-label}
  {SURPRISE NAME-C} -> {CATEGORY}: {taxonomy-label}
```

This CATEGORY DECLARATION is the upstream source for the `{CATEGORY}:` field in Step 10
audit rows (C-28). Do not proceed to synthesis paragraph without completing the declaration.

**Synthesis paragraph:**
Name >=2 SURPRISE entries by their exact labels. Explain what only emerges from reading
those entries together -- unreachable from any single entry alone. State the independence
constraint explicitly in the paragraph: "This pattern is not derivable from either entry
read alone." Name the category of shared misunderstanding across the dominant entries
(C-16). PARTIAL if synthesis names a pattern but does not classify by misunderstanding
type. <=120 words (WORD BUDGET above).

---

### Step 9 -- Forward Handover Guidance

```
PHASE:  handover
SCOPE:  one register selection from T-1..T-4; stated before writing; slots verified
        against entry content; source citable; no new evidence derivation
```

*(IA: false-assumption-recovery; epistemic dimension: future-framing -- translating
institutional memory into a directive for a future builder who did not participate in
this investigation)*

Select one register:
- T-1 (builder): "If you are about to build {scenario}, know that {constraint} because {source}."
- T-2 (reviewer): "Before approving {decision}, verify {constraint} against {source}."
- T-3 (PM): "Scope the {area} decision against {constraint} found in {source}."
- T-4 (architect): "The {component} design assumes {belief}; {source} shows this is false."

State selected register (T-1/T-2/T-3/T-4) before writing. Verify slot assignments.
Both scenario/decision/area/component and constraint must be specific. Source citable.

---

### Step 10 -- Rules of Thumb

```
PHASE:  rules
SCOPE:  <=3 rules; HIGH/MEDIUM only; all traceability checks before verdict written;
        correct mismatches before writing
```

**Audit row schema (C-28: category-field propagation from Step 8 CATEGORY DECLARATION):**

```
[{HIGH | MEDIUM}] {Rule -- <=20 words, quotable standalone heuristic}
(encodes: {SURPRISE NAME} -> {CATEGORY}: {taxonomy-label-from-Step-8-declaration})
```

The `{CATEGORY}:` field must reference a label from the Step 8 CATEGORY DECLARATION block.
If the label is absent from Step 8, return to Step 8 and update the declaration before
writing the rule. This is a structural gate, not a post-hoc annotation.

Traceability check:
1. Each rule's tier matches named surprise's triage tier from Step 4
2. Each rule traceable to exactly one named surprise (no orphan rules)
3. No surprise generates more than one rule
4. Each `{CATEGORY}:` references a declared taxonomy label from Step 8 (C-28 check)

Correct all mismatches before writing verdict.

**Write verdict:**

```
TRACE-CHECK-VERDICT: [PASS | FAIL]
  -- PASS: all tiers match; no orphan rules; one-rule-per-surprise confirmed;
           all {CATEGORY}: fields reference declared taxonomy labels from Step 8
  -- FAIL: {each mismatch: rule label | expected tier from Step 4 | actual tier in entry
           | or absent/undeclared {CATEGORY}: field}
```

*Forward-reader protocol: A future reader verifies this check ran by locating the
TRACE-CHECK-VERDICT token in the output -- no session replay required.
TRACE-CHECK-VERDICT: PASS certifies (1) tier match, (2) no orphan rules,
(3) one-rule-per-surprise, and (4) all {CATEGORY}: fields reference taxonomy labels
declared in Step 8 (C-28 field propagation confirmed).
TRACE-CHECK-VERDICT: FAIL records each specific mismatch by rule label, expected tier,
and actual tier or missing category field, enabling a reader to audit the failure without
re-executing the prompt.*

---

### Step 11 -- Gestalt Summary Audit

```
PHASE:  gestalt audit
SCOPE:  applied to complete draft (Steps 7-10) as single unit; not entry-by-entry;
        revise and re-run until PASS; gestalt-summary-fail distinct from gate-fail
```

*Applied to the complete draft output (Steps 7-10) as a single unit.*

"Could this output -- read as a whole, not entry by entry -- be described as a summary
or survey of what the investigation found?"

If YES or PARTLY YES:
- Identify entries that read as survey items in aggregate
- Revise to surface genuine cross-signal surprise, or discard
- Add to discard log: `gestalt-summary-fail`
- Re-run audit after each revision pass

**Write verdict:**

```
GESTALT-VERDICT: [PASS | FAIL]
  -- PASS: output does not read as survey in aggregate; every entry is a
     retroactively-visible surprise, not a survey item included for coverage
  -- FAIL: {each entry: label, gestalt-summary-fail trigger reason, revision applied}
```

*Forward-reader protocol: A future reader verifies this check ran by locating
GESTALT-VERDICT in the output -- no session replay required.
GESTALT-VERDICT: PASS certifies the complete output, read as a whole unit and not
entry-by-entry, does not pass the summary-or-survey audit question from Step 11.
GESTALT-VERDICT: FAIL identifies which specific entries triggered the gestalt-summary-fail
pattern and records what revision was applied to each, enabling a reader to audit the
revision decision without access to the pre-revision draft.*

---

### Step 12 -- Production Chain Trace

```
PHASE:  chain trace
SCOPE:  terminal artifact -- full pipeline with structural qualifiers; verification
        verdicts named as chain nodes; C-28 taxonomy propagation path named; C-29
        budget contract named; dependency graph explicitly closed
```

```
PRODUCTION CHAIN TRACE
VERIFICATION NODES INCLUDED | DEPENDENCY GRAPH CLOSED
======================================================================

[NODE 1] typed-route prediction sort [PHASE: filter]
  structural qualifier: IA: false-assumption-recovery; epistemic dimension:
    prior-frame-recovery co-activation per route, anti-hypothesis guard per candidate,
    typed downstream destination per discard, non-empty discard log as structural
    requirement, phase scope contract (filter-only)
  produces: typed route decisions, discard log with destinations
  consumed by: NODE 2 (receives gate-pipeline candidates only)

-> [NODE 2] staged gate verdict [PHASE: gate]
  structural qualifier: Gatekeeper: adversarial-rejection-only; epistemic dimension per
    stage (novelty/opposition/specificity) at each Stage header, per-stage written commit
    tokens with collapse prohibition, falsifiable "We believed:" + VALID/INVALID contrast
    gallery per Stage 2, cross-signal citation per Stage 3 SURPRISE, minimum floor tracked,
    Stage 2 INVALID -> return to discard log (return semantics), phase scope contract
    (rejection-testing-only)
  produces: SURPRISE verdicts, floor count
  consumed by: NODE 3

-> [NODE 3] comparative triage rank [PHASE: triage]
  structural qualifier: all candidates evaluated simultaneously before any tier assigned,
    failure-first ordering within tier, all tiers recorded before expansion begins,
    phase scope contract (tier-assignment-only)
  produces: HIGH/MEDIUM/LOW triage assignments, within-tier order
  consumed by: NODE 4 (entry headers), NODE 8 (TRACE-CHECK-VERDICT tier-match)

-> [NODE 3b] taxonomy declaration [C-16 -> C-28 upstream source]
  structural qualifier: IA: false-assumption-recovery; epistemic dimension: pattern-emergence;
    per-surprise {NAME} -> {CATEGORY}: typed mapping declared inside Step 8's PHASE block
    before synthesis paragraph begins; categories typed by misunderstanding class, not topic;
    CATEGORY DECLARATION block is upstream source for NODE 7's {CATEGORY}: field
  produces: category taxonomy (C-16), per-surprise map (C-28 upstream)
  consumed by: NODE 5 (synthesis names category via C-16),
               NODE 7 ({CATEGORY}: field in audit row via C-28)

-> [NODE 4] echo entry [PHASE: entry generation]
  structural qualifier: IA: false-assumption-recovery; epistemic dimension:
    failure-projection per sub-step; 4-step naming scaffold; failure-first production;
    [CROSS: A x B] annotation; failure field as concrete mis-design; named design impact;
    phase scope contract (one-entry-per-SURPRISE, no new evidence, no triage revision)
  produces: named surprise labels, source citations, design impact, routing tags
  consumed by: NODE 5 (synthesis), NODE 6 (handover), NODE 7 (rules)

-> [NODE 5] cross-signal synthesis [C-28 taxonomy consumer + C-29 budget contract]
  structural qualifier: IA: false-assumption-recovery; epistemic dimension: pattern-emergence;
    PHASE+SCOPE+WORD BUDGET contract block at step header (C-29 -- WORD BUDGET: <=120 words
    as standalone field, not embedded prose); taxonomy declaration from NODE 3b feeds
    category naming in synthesis (C-16/C-28 chain); >=2 named labels; cross-entry pattern
    unreachable from single entry; independence constraint stated explicitly in paragraph
  produces: synthesized paragraph with budget-bounded output and typed misunderstanding category
  consumed by: output (terminal)

-> [NODE 6] forward handover guidance [PHASE: handover]
  structural qualifier: IA: false-assumption-recovery; epistemic dimension: future-framing;
    T-1..T-4 register selected from menu; register stated before writing; slots verified;
    source citable; phase scope contract (one-register, no new derivation)
  produces: register-anchored handoff statement
  consumed by: output (terminal)

-> [NODE 7] impact-anchored rule with category field [C-28 consumer; PHASE: rules]
  structural qualifier: tier verified against NODE 3 triage; orphan rule check;
    one-rule-per-surprise; {CATEGORY}: field references CATEGORY DECLARATION from NODE 3b
    -- absent category is a structural gate, not a post-hoc flag; absent category ->
    return to NODE 3b before rule written
  produces: verified rules with tier labels and {CATEGORY}: fields
  consumed by: NODE 8 (TRACE-CHECK-VERDICT)

-> [NODE 8] TRACE-CHECK-VERDICT
  structural qualifier: written PASS|FAIL token; certifies tier-match, no-orphan,
    one-rule-per-surprise, and {CATEGORY}: field presence against NODE 3b taxonomy (C-28);
    forward-reader protocol specifies: locate token, PASS certifies four checks, FAIL
    records each mismatch by rule label + expected tier + actual tier + missing field
  produces: traceability audit result including C-28 category-field check
  consumed by: NODE 11 (chain trace)

-> [NODE 9] gestalt audit [PHASE: gestalt audit]
  structural qualifier: IA: false-assumption-recovery applied to complete artifact as
    unit (not entry-by-entry); gestalt-summary-fail discards logged separately from
    item-level gate-fail; phase scope contract (whole-artifact evaluation, revise until PASS)
  produces: gestalt audit result
  consumed by: NODE 10

-> [NODE 10] GESTALT-VERDICT
  structural qualifier: written PASS|FAIL token; certifies aggregate non-survey;
    PASS certifies output-as-whole fails summary-or-survey audit question; FAIL records
    entry label + trigger reason + revision applied per entry; forward-reader protocol
    specifies: locate token, PASS certifies aggregate non-survey, FAIL records revision
    decisions enabling reader audit without pre-revision draft
  produces: gestalt audit result
  consumed by: NODE 11 (chain trace)

-> [NODE 11] chain trace (this node) [PHASE: chain trace]
  structural qualifier: all nodes named with verifiable structural qualifiers and phase
    labels; NODE 3b (taxonomy, C-28 upstream source) and its propagation to NODE 5
    (synthesis category naming) and NODE 7 (audit row {CATEGORY}: field) explicitly named
    as dependency links; NODE 5 budget contract (C-29 -- WORD BUDGET: as standalone
    contract field) named; verification verdicts (NODEs 8 and 10) are named chain nodes;
    all inter-criterion dependencies annotated -- graph is closed
  produces: closed, auditable dependency graph
  consumed by: output (terminal)

======================================================================
Dependency closure:
  NODE 3 -> NODE 8: triage rank feeds tier-match check
  NODE 3b -> NODE 5 (C-16/C-28): taxonomy feeds synthesis category naming
  NODE 3b -> NODE 7 (C-28): taxonomy feeds {CATEGORY}: field in audit rows
  NODE 9/10 -> NODE 11: gestalt verdict is named chain node
  NODE 8 -> NODE 11: traceability verdict is named chain node
  NODE 4 -> NODE 6: routing tags feed handover scenario selection
  Step 5 -> Step 6: naming scaffold feeds co-validation gate
  NODE 5 contract (C-29): WORD BUDGET: <=120 words is a standalone contract field
    at NODE 5's step header -- not embedded prose; scoped to synthesis step specifically
```

---

### Dependency Closure Enumeration

*Standalone terminal block. Spot-checkable without traversal.*

```
DEPENDENCY CLOSURE ENUMERATION
================================
NODE 3 -> NODE 8:
  triage rank (NODE 3) is required input for tier-match check (NODE 8);
  NODE 8 cannot verify tiers without NODE 3 assignments

NODE 3b -> NODE 5 (C-16/C-28):
  taxonomy declaration (NODE 3b) is source for synthesis category naming;
  NODE 5 cannot produce C-16-compliant synthesis without NODE 3b output;
  this is the C-28 chain leg: taxonomy declared in synthesis step

NODE 3b -> NODE 7 (C-28):
  taxonomy declaration (NODE 3b) is required input for {CATEGORY}: field in audit rows;
  NODE 7 cannot produce a C-28-compliant row without NODE 3b taxonomy output;
  absent category in NODE 7 routes back to NODE 3b (return gate, not annotation)

NODE 9/10 -> NODE 11:
  gestalt verdict (NODE 10) is a named chain node in NODE 11;
  NODE 11 structural qualifier must reference NODE 10 to satisfy chain-closure requirement

NODE 8 -> NODE 11:
  traceability verdict (NODE 8) is a named chain node in NODE 11;
  NODE 11 structural qualifier must reference NODE 8

NODE 4 -> NODE 6:
  routing tags in entries (NODE 4) feed handover scenario selection (NODE 6);
  T-1..T-4 register slot {scenario/decision/area/component} requires named route from NODE 4

Step 5 -> Step 6:
  naming scaffold (Step 5) feeds co-validation name-form check (Step 6);
  Step 6 gate cannot run until Step 5 scaffold completes per candidate

NODE 5 budget contract (C-29):
  WORD BUDGET: <=120 words declared at NODE 5's step header as standalone contract field;
  not embedded in prose; scoped to synthesis step specifically, not inherited from global
  limit; consistent with WORD BUDGET: contract structure on data-collection steps
================================
All 7 dependency loops + 1 C-29 contract anchor enumerated.
A reviewer can spot-check closure by reading this block without traversing chain trace.
Any loop absent from this enumeration that appears in the chain trace is a closure violation.
```

**Output**: Steps 7-12 + Dependency Closure Enumeration. Steps 1-6 are execution scaffolding.
