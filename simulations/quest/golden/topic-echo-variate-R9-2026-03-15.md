---
skill: quest-variate
skill_target: topic-echo
date: 2026-03-15
round: 9
rubric: v9
rubric_max: 159
---

# Variations: `topic:echo` -- Round 9

**Rubric:** v9 | **Date:** 2026-03-15

---

## Design Context

R8 differentiating evidence: three structural patterns from R8 V-05 were observable but not
yet formalized as criteria.

1. **R8 V-05 sub-step dimension gap (-> C-32)**: R8 V-05 placed `(epistemic dimension:
   novelty/opposition/specificity)` at each Stage header inside the Gate (Steps 3a-3c). But
   every IA invocation outside the Gate carried only identity+function (`IA:
   false-assumption-recovery`) -- no epistemic dimension inline. A model executing Step 2
   (Prediction Sort) sees the IA name and function shorthand but must infer *why
   historical-recovery is the right epistemic posture for this specific step* without a
   look-back. The Gate stages satisfy C-32 partially (Gatekeeper stages have it); all IA
   steps fail it. C-32 closes this by requiring the three-part annotation -- identity,
   function shorthand, epistemic dimension -- at every named-role invocation across all steps.

2. **R8 V-05 dep-closure traversal gap (-> C-33)**: R8 V-05 embedded the "Dependency closure
   verification" block inside Step 12's chain trace body (between the node list and the
   closing protocol text). A reviewer wanting only to spot-check closure must locate and
   extract it from the trace. C-31 is satisfied -- the graph is readable from the trace.
   But readable and spot-checkable are different properties: C-31 allows the deps to be
   distributed as annotations across nodes; C-33 requires a single terminal artifact after
   the chain trace closes, enumerating every loop in isolation. C-33 closes the gap:
   terminal block, separate from trace, spot-checkable without traversal.

3. **R8 V-05 token rationale asymmetry (-> C-34)**: R8 V-05 added a forward-reader rationale
   at TRACE-CHECK-VERDICT: "A future reader verifies the check ran by locating this token in
   the output -- no session replay required." (Step 10, explicit language). GESTALT-VERDICT
   had: "This verdict is a structural artifact auditable by the same rules as any production
   link." (Step 11). The second formulation tells a reader that the token is auditable but
   does not tell them *how* -- locating the token is the protocol, not just an analogy to
   production links. C-34 closes the gap: each token must carry its own complete forward-
   reader protocol statement so a reader encountering the token in isolation can immediately
   understand how to use it for verification, without reading the other token or re-consulting
   the prompt.

**Variation plan:**

- V-01: C-32 only -- epistemic dimension at every IA invocation (Gatekeeper stages already
  satisfy C-32 in R8 V-05; IA steps do not)
- V-02: C-33 only -- standalone terminal dep enumeration block after chain trace closes
- V-03: C-34 only -- GESTALT-VERDICT gains complete forward-reader protocol; TRACE-CHECK-
  VERDICT extended to match exact language
- V-04: C-32 + C-33 (no C-34) -- combined dep-closure and dimension annotation without token
  rationale parity
- V-05: Full synthesis -- C-32 + C-33 + C-34 on R8 V-05 baseline; gold standard for v9

**Discriminating pairs:**
- V-01 vs V-05: C-33 + C-34 absent vs present; isolates combined dep/token value
- V-02 vs V-05: C-32 + C-34 absent vs present; isolates combined dim/token value
- V-03 vs V-05: C-32 + C-33 absent vs present; isolates combined dim/dep value
- V-04 vs V-05: C-34 absent vs present; direct isolation of token rationale parity value

---

## V-01 -- Single-axis: Epistemic dimension at every IA invocation (C-32)

**Variation axis:** Role annotation depth. Every invocation of a named role (IA or
Gatekeeper) carries the three-part annotation: identity + function shorthand + epistemic
dimension. Gatekeeper stages already carry this in R8 V-05 (the Gate Stage headers have
`epistemic dimension: novelty/opposition/specificity`). This variation extends the
requirement to every IA invocation across all steps outside the Gate.

**Hypothesis:** R8 V-05 satisfied C-32 for the Gatekeeper (Stage headers carry all three
parts) but not for the IA (only identity+function). The Gatekeeper executes a tightly
bounded step (Step 3 only) where the stage header is the natural annotation point. The IA
spans six steps with distinct epistemic work per step: at Step 2 the posture is
historical-recovery of prior beliefs; at Step 5 it is belief-inversion to form the name; at
Step 7 it is failure-projection from false assumptions. Naming the epistemic dimension at
each IA invocation tells a model executing that step why this epistemic posture applies here,
not just what the role does in general. Hypothesis: adding the dimension at IA sub-steps
improves execution fidelity at steps far from the Gate without cluttering the Gate stages.

**Builds on:** R8 V-05 -- all 23 aspirational criteria (C-09..C-31) active.

**C-33 and C-34 status:** Not activated. Dependency closure embedded in chain trace (C-31
satisfied, C-33 not). GESTALT-VERDICT retains R8 V-05 form (C-34 partially satisfied for
TRACE-CHECK-VERDICT, not for GESTALT-VERDICT).

---

### Prompt Body

You are running `/quest:topic echo` for the topic: {topic}.

All essential signals are in hand. Your task: surface the genuine surprises -- findings that
only became visible in retrospect, from cross-signal tension, that no competent practitioner
would have predicted before gathering evidence.

Not a summary. Not a survey of discoveries. An echo: the signal that comes back that you
didn't send.

---

### Roles *(C-25: two distinct named roles; C-30: sub-step identity+function co-activation;
C-32: epistemic dimension at every named-role invocation)*

**Institutional Archaeologist (IA)**
*First invocation: Step 2.*
Function: Recovers false assumptions embedded in current materials -- what a future team
would carry as truth without knowing otherwise. Frames every surprise as a correction to a
false assumption (C-17), not a description of a discovery. Derives consequence by asking
"What would the next team build wrong?" (C-18, C-22). The IA is the author of implication;
the Gatekeeper is the author of rejection.

Sub-step co-activation shorthand *(C-30, C-32)*:
Each IA invocation carries three fields: `IA: false-assumption-recovery; epistemic
dimension: {name}`. The epistemic dimension names why this posture applies at this specific
step. Defined dimensions per step:

| Step | Epistemic Dimension | Why here |
|------|---------------------|----------|
| 2 | prior-frame-recovery | Recovering what beliefs were actually held, not what the spec says |
| 5 | belief-inversion | Inverting the false assumption to derive a correction-encoding name |
| 6 | correction-integrity | Verifying that both name form and failure field faithfully encode the correction |
| 7 | failure-projection | Projecting the concrete mis-design from the false assumption as load-bearing anchor |
| 8 | pattern-emergence | Identifying what only emerges from reading multiple entries together |
| 9 | future-framing | Translating internal findings into actionable guidance for a future builder |

Active: Steps 2, 5, 6, 7, 8, 9.

**Gatekeeper**
*First invocation: Step 3.*
Sub-step co-activation shorthand *(C-30, C-32)*: `Gatekeeper: adversarial-rejection-only;
epistemic dimension: {stage-specific label}` -- see Stage headers in Step 3.

```
GATEKEEPER -- FUNCTION DECLARATION (C-27)
---------------------------------------------------------------------
Function:      Adversarial rejection. Tests each gate-pipeline candidate: (1)
               first-principles predictability -- could a competent practitioner
               have predicted this before any signal gathering? (2) cross-signal
               requirement -- does this finding emerge only when >=2 artifacts
               are read together? Fails either: rejected.

Not-function:  Future-reader framing. The Gatekeeper does not ask what the
               next team would get wrong. That is the IA's domain.

Not-function:  Thematic synthesis or cross-item grouping. The Gatekeeper
               evaluates each candidate in isolation.

Role boundary: Gatekeeper verdicts are final. The IA cannot reverse a rejection.
               The Gatekeeper tests the candidate; the IA frames the implication.
---------------------------------------------------------------------
```

Active: Step 3 only.

---

### Step 1 -- Read Signal Record *(C-10: multi-namespace coverage; C-12: temporal marking)*

Read all signal artifacts in the topic signal folder across all namespaces (scout, draft,
review, flow, trace, prove, listen, program, topic).

Record:
- Namespaces covered -- must reach >=3 distinct namespaces (C-10 floor)
- Total artifacts read
- Date range (earliest -> latest) -- temporal anchor source for C-12 per entry

---

### Step 2 -- Pre-Write Prediction Sort
*(IA: false-assumption-recovery; epistemic dimension: prior-frame-recovery -- recovering
what the team actually believed before investigation, not what the spec states; C-16:
structurally-enforced filter; C-14: downstream routing; C-11: anti-hypothesis guard;
C-09: discard visibility)*

Assign a typed route to every finding. The route is a structural verdict enforced before any
candidate proceeds to the gate *(C-16)*.

Route types:
- `topic-story` -- confirms hypothesis; destination: topic narrative *(C-14)*
- `topic-report` -- restates known constraint; destination: report *(C-14)*
- `gate-pipeline` -- candidate surprise; proceeds to Step 3

Anti-hypothesis guard *(C-11; IA: false-assumption-recovery; epistemic dimension:
prior-frame-recovery)*: "Does this item confirm what the investigation set out to prove?"
YES -> `topic-story`, regardless of apparent novelty.

Pre-expansion co-validation *(C-20 partial; IA: false-assumption-recovery; epistemic
dimension: prior-frame-recovery)*: for each `gate-pipeline` item: "A new team from the spec
alone would not have encountered this." Cannot confirm -> `topic-report`.

Discard log *(C-09; IA: false-assumption-recovery; epistemic dimension: prior-frame-recovery)*:
every item routed to `topic-story` or `topic-report` with route type, reason (1 sentence),
downstream destination *(C-14)*.

Non-empty discard log required. Empty log indicates filter was not applied.

---

### Step 3 -- Multi-Stage Epistemic Gate
*(Gatekeeper: adversarial-rejection-only; C-13: typed skeptic gate; C-15: minimum surprise
floor; C-16: structurally-enforced filter)*

```
GATEKEEPER: adversarial-rejection-only -- active from here through end of Stage 3.
```

**Anti-Pattern Catalog** *(C-13; Gatekeeper: adversarial-rejection-only)*:
- CONFIRMATION: confirms original hypothesis even if unpredicted -> verdict PREDICTABLE
- RESTATEMENT: documents known constraint or spec requirement -> route `topic-report`
- ISOLATED-FINDING: finding complete in one artifact; no cross-signal emergence -> route `topic-report`

**Gate format** *(C-16)*: each candidate receives typed verdict token before expansion.
Format: `VERDICT: SURPRISE | CUT -- {anti-pattern label if CUT}`.

**Three sequential stages. Per-stage commit required. Collapse prohibition: do not write a
combined multi-stage verdict. Each stage result is a written artifact before the next begins.**

---

**Stage 1 -- Prediction Test**
*(Gatekeeper: adversarial-rejection-only; epistemic dimension: novelty -- separating
investigation-emergent findings from outcomes predictable from original design materials)*

"Would a competent practitioner have predicted this from first principles, prior to any
signal gathering?"

Anti-hypothesis re-check *(C-11)*: confirms the investigation's starting hypothesis?
-> PREDICTABLE regardless.

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

Minimum surprise floor *(C-15)*: >=3 candidates must reach CONTRADICTION FOUND.
If fewer than 3, record as floor-miss. Do not suppress it.

`NO CONTRADICTION` -> route to `topic-report`; discard log
`CONTRADICTION FOUND` -> Stage 3

**Commit**: `Stage 2: [{item label}] -> [NO CONTRADICTION | CONTRADICTION FOUND]`

---

**Stage 3 -- Attribution Test**
*(Gatekeeper: adversarial-rejection-only; epistemic dimension: specificity -- separating
traceable cross-signal findings from single-artifact findings that cannot generate an echo)*

"Does this finding emerge only when two or more signal artifacts are read together, or does
it exist complete in a single artifact in isolation?"

`SINGLE-ARTIFACT` -> route to `topic-report`; discard log
`CROSS-SIGNAL (cite >=2 source artifacts)` -> verdict SURPRISE

**Commit**: `Stage 3: [{item label}] -> [SINGLE-ARTIFACT | CROSS-SIGNAL] -- sources:
[{artifact1 (namespace/skill)}, {artifact2 (namespace/skill)}]`

---

### Step 4 -- Pre-Write Impact Triage *(C-23: triage as pre-write scaffolding; C-22: failure-first ordering)*

Assign each SURPRISE candidate a tier comparatively -- evaluate all candidates against each
other before assigning any tier. No tier assigned in isolation.

- **HIGH**: Forces revision to core design decision, assumption, or scope boundary
- **MEDIUM**: Qualifies design principle or adds constraint to existing decision
- **LOW**: Notable; no clear design consequence at present

*(C-22)*: Within each tier, failure-first ordering -- candidate with highest failure-if-wrong
risk goes first. Order by severity (highest first) within tier.

Record all triage assignments before writing any entry.
Write order: HIGH -> MEDIUM -> LOW; within tier: failure-first *(C-22)*.

---

### Step 5 -- Naming Scaffold
*(C-17: correction-encoding names; C-21: derivation scaffold; IA: false-assumption-recovery;
epistemic dimension: belief-inversion -- the name is derived by inverting the false
assumption; the inversion is not a description of the discovery but an encoding of what
was wrong)*

For each SURPRISE candidate, work through the scaffold before writing the entry header.
Do not skip to name formation.

1. State old belief: "The team carried the assumption that ___."
2. State correction: "The signals revealed instead that ___."
3. Derive domain: "This affects the ___ area of the design."
4. Form label: `The {Corrected Belief}: {Domain}`

VALID: "The Silent Veto: Adoption Workflow" -- encodes what was wrong and where.
INVALID: "Surprising Finding About Adoption" -- describes discovery category, not corrected belief.

Output of step 4 feeds directly into the entry header.

---

### Step 6 -- Pre-Expansion Co-Validation Gate
*(C-20; IA: false-assumption-recovery; epistemic dimension: correction-integrity --
verifying that both name form and failure field structurally encode the correction before any
expansion begins; neither name form alone nor failure field alone suffices)*

Before expanding any entry, co-validate simultaneously. Both must be VALID. Either failing
blocks expansion -- revise before proceeding.

- **Name form** *(C-17)*: does the label follow `The {Corrected Belief}: {Domain}`?
  -> VALID / INVALID

- **Failure field** *(C-18)*: does the failure read as "If the next team carries the old
  assumption, {specific concrete mis-design}" -- named mis-design, not change-list?
  -> VALID / INVALID

Gate runs once per candidate. VALID gate is pre-condition for Step 7 expansion.

---

### Step 7 -- Write Echo Entries
*(IA: false-assumption-recovery; epistemic dimension: failure-projection -- the entry is
produced by projecting the specific mis-design that follows from the false assumption; the
failure scenario is load-bearing, not derived; triage order; failure-first within tier;
C-04; C-02; C-03; C-08; C-12; C-14; C-17; C-18; C-22)*

Entry production sequence *(C-22)*: begin from failure scenario, then derive signal tracing,
naming, and impact. The failure is load-bearing.

---

**Begin from failure** *(IA: false-assumption-recovery; epistemic dimension:
failure-projection)*: If the next team carries the old assumption about {domain}, they would
{specific mis-design}. Anchor.

**[SURPRISE NAME: `The {Corrected Belief}: {Domain}`]** -- *{HIGH | MEDIUM | LOW}*

Source signal: `{artifact-name} ({namespace}/{skill})`
`[CROSS: {artifact-A} x {artifact-B}]` *(C-08)*

Temporal anchor *(C-12)*: `{round or date of earliest contributing signal}`

We believed: `{falsifiable pre-investigation assumption}`

The surprise: `{what signals revealed that contradicts the prior assumption}`

If the next team carries the old assumption *(C-18)*: `{specific concrete mis-design}`.

Design impact *(C-03)*: `{decision revisited / assumption struck / scope boundary shifted}`.

Downstream route *(C-14)*: `-> {skill or namespace}`.

---

### Step 8 -- Cross-Signal Synthesis
*(C-05; IA: false-assumption-recovery; epistemic dimension: pattern-emergence -- naming what
only becomes visible when two or more entries are read together; unreachable from any single
entry in isolation)*

One paragraph, <=120 words.

Name >=2 SURPRISE entries by their labels. Explain what only emerges from reading those
entries together -- unreachable from any single entry alone.

C-05 definitional line: a finding in one artifact is a finding; a surprise visible only when
two signals are read together is an echo. Do not summarize; synthesize the cross-entry tension.

---

### Step 9 -- Forward Handover Guidance *(C-06; C-19; IA: false-assumption-recovery;
epistemic dimension: future-framing -- translating institutional memory into a directive for
a future builder who did not participate in this investigation)*

Select one register *(C-19)*:

- T-1 (builder): "If you are about to build {scenario}, know that {constraint} because {source}."
- T-2 (reviewer): "Before approving {decision}, verify {constraint} against {source}."
- T-3 (PM): "Scope the {area} decision against {constraint} found in {source}."
- T-4 (architect): "The {component} design assumes {belief}; {source} shows this is false."

Select register matching most actionable downstream route from Step 7 entries.
State selected register (T-1/T-2/T-3/T-4). Verify slot assignments before writing.
Both scenario/decision/area/component and constraint must be specific. Source citable.

---

### Step 10 -- Rules of Thumb *(C-07: impact magnitude; C-24: traceability closure)*

<=3 rules. HIGH and MEDIUM surprises only. LOW excluded.

```
[{HIGH | MEDIUM}] {Rule -- <=20 words, quotable standalone heuristic}
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
this token in the output -- no session replay required.

---

### Step 11 -- Gestalt Summary Audit *(C-26)*

*Applied to the complete draft output (Steps 7-10) as a single unit.*

**Audit question**: "Could this output -- read as a whole, not entry by entry -- be described
as a summary or survey of what the investigation found?"

If YES or PARTLY YES:
- Identify entries that read as survey items in aggregate
- Revise to surface genuine cross-signal surprise, or discard
- Add to discard log: `gestalt-summary-fail`
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

### Step 12 -- Production Chain Trace
*(C-28: full-chain with structural qualifiers; C-29: verification steps as chain nodes;
C-31: closed dependency graph)*

```
PRODUCTION CHAIN TRACE
VERIFICATION NODES INCLUDED (C-29) | DEPENDENCY GRAPH CLOSED (C-31)
======================================================================

[NODE 1] typed-route prediction sort
  structural qualifier: IA: false-assumption-recovery; epistemic dimension:
    prior-frame-recovery co-activation per route (C-30+C-32), anti-hypothesis
    guard per candidate (C-11), typed downstream destination per discard (C-14),
    non-empty discard log as structural requirement (C-09)
  produces: typed route decisions (C-16), discard log with destinations (C-09+C-14)
  consumed by: NODE 2 (receives gate-pipeline candidates only)

-> [NODE 2] staged gate verdict
  structural qualifier: Gatekeeper: adversarial-rejection-only; epistemic dimension per
    stage (novelty/opposition/specificity) at each Stage header (C-30+C-32), per-stage
    written commit tokens with collapse prohibition (C-13+C-16), falsifiable "We believed:"
    + VALID/INVALID contrast gallery per Stage 2 (C-18 scaffolding), cross-signal citation
    per Stage 3 SURPRISE (C-08 prereq), minimum floor tracked (C-15)
  produces: SURPRISE verdicts (C-13/C-16), floor count (C-15)
  consumed by: NODE 3 (confirmed SURPRISE candidates for triage)

-> [NODE 3] comparative triage rank
  structural qualifier: all candidates evaluated simultaneously before any single tier
    assigned (C-23), failure-first ordering within tier by mis-design severity (C-22),
    all tiers recorded as written artifact before expansion begins
  produces: HIGH/MEDIUM/LOW triage assignments (C-23), within-tier order (C-22)
  consumed by: NODE 4 entry headers (C-07: tier labels require C-23 output)
               NODE 8 TRACE-CHECK-VERDICT (C-24: tier-match check requires C-23 output)

-> [NODE 4] echo entry
  structural qualifier: IA: false-assumption-recovery; epistemic dimension:
    failure-projection at each sub-step (C-30+C-32); name from 4-step derivation scaffold
    (C-17+C-21); failure-first production (C-22); [CROSS: A x B] annotation (C-08);
    failure field as concrete mis-design not change-list (C-18); design impact names
    decision/assumption/scope (C-03)
  produces: named surprise labels (C-04), source citations (C-02), design impact (C-03),
            routing tags (C-14)
  consumed by: NODE 5 synthesis (C-05: requires >=2 labeled surprises by name)
               NODE 6 handover (C-06: requires named scenario from C-14 routing)
               NODE 7 rules (C-24: requires named surprise per rule)

-> [NODE 5] cross-signal synthesis
  structural qualifier: IA: false-assumption-recovery; epistemic dimension:
    pattern-emergence; >=2 named surprise labels cited by exact label, cross-entry pattern
    stated as unreachable from single entry alone (C-05 definitional line)
  produces: synthesized echo paragraph (C-05)
  consumed by: output (terminal)

-> [NODE 6] forward handover guidance
  structural qualifier: IA: false-assumption-recovery; epistemic dimension:
    future-framing; register selected from T-1..T-4 menu (C-19), register stated before
    writing, slot assignments verified (C-06), source citable (C-06)
  produces: register-anchored handoff statement (C-06+C-19)
  consumed by: output (terminal)

-> [NODE 7] impact-anchored rule
  structural qualifier: tier verified against NODE 3 triage by explicit check (C-24),
    orphan rule check, one-rule-per-surprise constraint
  produces: verified rules with tier labels (C-07+C-24)
  consumed by: NODE 8 TRACE-CHECK-VERDICT

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
  consumed by: NODE 10 GESTALT-VERDICT

-> [NODE 10] GESTALT-VERDICT [C-29: gestalt audit as chain node]
  structural qualifier: written PASS|FAIL token produced by explicit audit question
    in Step 11; verifiable by locating token in output; records revised/discarded entries
    if FAIL; distinct from NODE 8 verdict (scope: gestalt not traceability)
  produces: gestalt audit result (C-26+C-29 joint output)
  consumed by: NODE 11 chain trace (C-28+C-31: GESTALT-VERDICT is named chain node)

-> [NODE 11] production chain trace (this node)
  structural qualifier: all nodes named with qualifiers verifiable from output alone (C-28);
    verification verdicts are chain nodes not meta-gates (C-29); all inter-criterion
    output-to-input relationships explicitly annotated -- graph is closed (C-31)
  produces: closed, auditable dependency graph
  consumed by: output (terminal)

======================================================================
Dependency closure verification (C-31): the following inter-criterion loops are
explicitly closed in the trace above:
  C-23 output -> C-24 (NODE 3 -> NODE 8): triage rank feeds tier-match check
  C-26 output -> C-28 (NODE 9 -> NODE 10 -> NODE 11): gestalt verdict is chain node
  C-24 output -> C-28 (NODE 8 -> NODE 11): traceability verdict is chain node
  C-14 output -> C-06 (NODE 4 -> NODE 6): routing feeds handover scenario selection
  C-17+C-21 output -> C-20 (Step 5 -> Step 6): naming scaffold feeds co-validation gate
No inter-criterion dependency is discoverable only by reading the prompt.
```

**Output**: Steps 7-12 only. Steps 1-6 are execution scaffolding.

---

## V-02 -- Single-axis: Terminal dependency enumeration block (C-33)

**Variation axis:** Post-chain terminal artifact. A standalone block, separate from and after
the chain trace closes, enumerates all inter-criterion dependency loops in the format
`{source criterion} output -> {consuming criterion} ({chain node reference})`. The chain
trace itself retains the embedded closure text from R8 V-05 (satisfying C-31); the terminal
block is a separate artifact enabling spot-check without traversal (satisfying C-33).

**Hypothesis:** C-31 (readable from chain trace) and C-33 (spot-checkable terminal block)
satisfy the same information requirement at different audit speeds. C-31 allows a careful
reader to reconstruct the dependency graph by reading the trace. C-33 allows a reviewer
doing a quick spot-check to verify closure at a glance. The two criteria are non-redundant:
satisfying C-31 without C-33 means the deps are present but dispersed; satisfying C-33 adds
a single extraction point for the same information. Hypothesis: the terminal block adds a
structural artifact without duplicating chain logic, and a model producing this output is no
more likely to make errors in the chain trace because the terminal block exists separately.

**Builds on:** R8 V-05 -- all 23 aspirational criteria (C-09..C-31) active.

**C-32 and C-34 status:** Not activated. IA invocations carry identity+function only (R8
V-05 baseline). GESTALT-VERDICT retains R8 V-05 partial rationale.

---

### Prompt Body

You are running `/quest:topic echo` for the topic: {topic}.

All essential signals are in hand. Your task: surface the genuine surprises -- findings that
only became visible in retrospect, from cross-signal tension, that no competent practitioner
would have predicted before gathering evidence.

Not a summary. Not a survey of discoveries. An echo: the signal that comes back that you
didn't send.

---

### Roles *(C-25: two distinct named roles; C-30: sub-step identity+function co-activation)*

**Institutional Archaeologist (IA)**
*First invocation: Step 2.*
Function: Recovers false assumptions embedded in current materials -- what a future team
would carry as truth without knowing otherwise. Frames every surprise as a correction to a
false assumption (C-17). The IA is the author of implication; the Gatekeeper is the author
of rejection.

Sub-step co-activation shorthand *(C-30)*: `IA: false-assumption-recovery`
Appears at every sub-step IA governs -- identity and function simultaneously, no look-back.
Active: Steps 2, 5, 6, 7, 8, 9.

**Gatekeeper**
*First invocation: Step 3.*
Sub-step co-activation shorthand *(C-30)*: `Gatekeeper: adversarial-rejection-only`

```
GATEKEEPER -- FUNCTION DECLARATION (C-27)
---------------------------------------------------------------------
Function:      Adversarial rejection. Tests each gate-pipeline candidate: (1)
               first-principles predictability; (2) cross-signal requirement.
               Fails either: rejected.
Not-function:  Future-reader framing (IA domain).
Not-function:  Thematic synthesis or cross-item grouping.
Role boundary: Gatekeeper verdicts are final.
---------------------------------------------------------------------
```

Active: Step 3 only.

---

### Step 1 -- Read Signal Record *(C-10; C-12)*

Read all signal artifacts across all namespaces (scout, draft, review, flow, trace, prove,
listen, program, topic). Record: namespaces covered (>=3 floor), total artifacts, date range.

---

### Step 2 -- Pre-Write Prediction Sort
*(IA: false-assumption-recovery; C-16; C-14; C-11; C-09)*

Route types: `topic-story` | `topic-report` | `gate-pipeline`

Anti-hypothesis guard *(C-11; IA: false-assumption-recovery)*: confirms original hypothesis?
-> `topic-story` regardless.

Discard log *(C-09)*: every non-gate-pipeline item with route type, reason, destination.
Non-empty discard log required.

---

### Step 3 -- Multi-Stage Epistemic Gate
*(Gatekeeper: adversarial-rejection-only; C-13; C-15; C-16)*

**Anti-Pattern Catalog** *(C-13)*: CONFIRMATION | RESTATEMENT | ISOLATED-FINDING

**Gate format** *(C-16)*: `VERDICT: SURPRISE | CUT -- {label}`

**Stage 1 -- Prediction Test** *(Gatekeeper: adversarial-rejection-only; epistemic dimension: novelty)*

"Would a competent practitioner have predicted this from first principles?"
`PREDICTABLE` -> `topic-story` | `UNPREDICTABLE` -> Stage 2
**Commit**: `Stage 1: [{item}] -> [PREDICTABLE | UNPREDICTABLE]`

---

**Stage 2 -- Contradiction Test** *(Gatekeeper: adversarial-rejection-only; epistemic dimension: opposition)*

"Does this item contradict an assumption from the pre-investigation frame?"

```
We believed: {falsifiable assumption}
VALID: {genuine falsification}
INVALID (absence-of-consideration): ...
INVALID (sentiment-reaction): ...
INVALID (hedge-uncertainty): ...
```

Minimum floor *(C-15)*: >=3 must reach CONTRADICTION FOUND.
`NO CONTRADICTION` -> `topic-report` | `CONTRADICTION FOUND` -> Stage 3
**Commit**: `Stage 2: [{item}] -> [NO CONTRADICTION | CONTRADICTION FOUND]`

---

**Stage 3 -- Attribution Test** *(Gatekeeper: adversarial-rejection-only; epistemic dimension: specificity)*

"Does this finding emerge only when >=2 artifacts are read together?"
`SINGLE-ARTIFACT` -> `topic-report` | `CROSS-SIGNAL (cite >=2 artifacts)` -> SURPRISE
**Commit**: `Stage 3: [{item}] -> [SINGLE-ARTIFACT | CROSS-SIGNAL] -- sources: [{a1}, {a2}]`

---

### Step 4 -- Pre-Write Impact Triage *(C-23; C-22)*

Assign tier comparatively. HIGH | MEDIUM | LOW. Failure-first within tier.
Record all assignments before writing any entry.

---

### Step 5 -- Naming Scaffold
*(C-17; C-21; IA: false-assumption-recovery)*

1. State old belief; 2. State correction; 3. Derive domain; 4. Form label: `The {Corrected Belief}: {Domain}`

---

### Step 6 -- Pre-Expansion Co-Validation Gate *(C-20; IA: false-assumption-recovery)*

Co-validate simultaneously. Both VALID before expansion.
- Name form *(C-17)*: follows `The {Corrected Belief}: {Domain}`? -> VALID / INVALID
- Failure field *(C-18)*: reads as "If the next team carries old assumption, {mis-design}"? -> VALID / INVALID

---

### Step 7 -- Write Echo Entries
*(IA: false-assumption-recovery; triage order; failure-first; C-04; C-02; C-03; C-08; C-12;
C-14; C-17; C-18; C-22)*

Begin from failure *(C-22; IA: false-assumption-recovery)*: anchor on mis-design scenario.

**[`The {Corrected Belief}: {Domain}`]** -- *{HIGH | MEDIUM | LOW}* *(IA: false-assumption-recovery)*

Source signal: `{artifact-name} ({namespace/skill})` `[CROSS: {A} x {B}]` *(C-08)*
Temporal anchor *(C-12)*: `{round/date}`
We believed: `{falsifiable assumption}`
The surprise: `{what signals revealed}`
If the next team carries old assumption *(C-18)*: `{specific mis-design}`.
Design impact *(C-03)*: `{decision/assumption/scope}`.
Downstream route *(C-14)*: `-> {skill/namespace}`.

---

### Step 8 -- Cross-Signal Synthesis *(C-05; IA: false-assumption-recovery)*

<=120 words. Name >=2 entries by label. State what only emerges from reading them together.

---

### Step 9 -- Forward Handover Guidance *(C-06; C-19; IA: false-assumption-recovery)*

Register: T-1 (builder) | T-2 (reviewer) | T-3 (PM) | T-4 (architect). State selection.

---

### Step 10 -- Rules of Thumb *(C-07; C-24)*

<=3 rules. HIGH and MEDIUM only.

```
[{HIGH | MEDIUM}] {Rule}
(encodes: {SURPRISE NAME})
```

**Write verdict**:

```
TRACE-CHECK-VERDICT: [PASS | FAIL]
  -- PASS: all tiers match; no orphan rules; one-rule-per-surprise confirmed
  -- FAIL: {mismatch detail}
```

This verdict is a structural artifact. A future reader verifies the check ran by locating
this token in the output -- no session replay required.

---

### Step 11 -- Gestalt Summary Audit *(C-26)*

"Could this output be described as a summary of what the investigation found?"
If YES/PARTLY YES: revise, add `gestalt-summary-fail` to discard log, re-run.

**Write verdict**:

```
GESTALT-VERDICT: [PASS | FAIL]
  -- PASS: output does not read as survey in aggregate
  -- FAIL: {entries revised/discarded with gestalt-summary-fail reason}
```

This verdict is a structural artifact auditable by the same rules as any production link.

---

### Step 12 -- Production Chain Trace *(C-28; C-29; C-31)*

```
PRODUCTION CHAIN TRACE
VERIFICATION NODES INCLUDED (C-29) | DEPENDENCY GRAPH CLOSED (C-31)
======================================================================

[NODE 1] typed-route prediction sort
  structural qualifier: IA: false-assumption-recovery co-activation (C-30), anti-hypothesis
    guard (C-11), typed destinations (C-14), non-empty discard log (C-09)
  produces: route decisions (C-16), discard log (C-09+C-14)
  consumed by: NODE 2

-> [NODE 2] staged gate verdict
  structural qualifier: Gatekeeper: adversarial-rejection-only per Stage (C-30), per-stage
    commits with collapse prohibition (C-13+C-16), "We believed:" + VALID/INVALID gallery
    (C-18 scaffolding), cross-signal citation (C-08 prereq), floor tracked (C-15)
  produces: SURPRISE verdicts (C-13/C-16), floor count (C-15)
  consumed by: NODE 3

-> [NODE 3] comparative triage rank
  structural qualifier: simultaneous comparison (C-23), failure-first within tier (C-22),
    written before expansion
  produces: tier assignments (C-23), within-tier order (C-22)
  consumed by: NODE 4 headers, NODE 8 TRACE-CHECK-VERDICT

-> [NODE 4] echo entry
  structural qualifier: IA: false-assumption-recovery per sub-step (C-30), 4-step naming
    scaffold (C-17+C-21), failure-first production (C-22), [CROSS] annotation (C-08),
    failure field as concrete mis-design (C-18), named impact (C-03)
  produces: named labels (C-04), citations (C-02), impact (C-03), routes (C-14)
  consumed by: NODE 5, NODE 6, NODE 7

-> [NODE 5] cross-signal synthesis
  structural qualifier: IA: false-assumption-recovery, >=2 named labels, cross-entry
    pattern unreachable from single entry (C-05)
  produces: synthesized paragraph (C-05)
  consumed by: output (terminal)

-> [NODE 6] forward handover guidance
  structural qualifier: IA: false-assumption-recovery, T-1..T-4 register menu (C-19),
    register stated before writing, slots verified (C-06)
  produces: register-anchored handoff (C-06+C-19)
  consumed by: output (terminal)

-> [NODE 7] impact-anchored rule
  structural qualifier: tier checked against NODE 3, orphan check, one-rule-per-surprise
  produces: verified rules (C-07+C-24)
  consumed by: NODE 8

-> [NODE 8] TRACE-CHECK-VERDICT [C-29: chain node]
  structural qualifier: written PASS|FAIL token, verifiable by token location, mismatches
    recorded if FAIL
  produces: traceability audit result (C-24+C-29)
  consumed by: NODE 11 (C-28+C-31: closes C-23->C-24->NODE 8 loop)

-> [NODE 9] gestalt audit
  structural qualifier: IA: false-assumption-recovery on complete artifact (C-26+C-30),
    gestalt-summary-fail distinct from gate-fail (C-26)
  produces: gestalt result (C-26)
  consumed by: NODE 10

-> [NODE 10] GESTALT-VERDICT [C-29: chain node]
  structural qualifier: written PASS|FAIL token, verifiable by location, revisions
    recorded if FAIL
  produces: gestalt audit result (C-26+C-29)
  consumed by: NODE 11

-> [NODE 11] production chain trace (this node)
  structural qualifier: all nodes with verifiable qualifiers (C-28), verification nodes
    included (C-29), all dependencies annotated (C-31)
  produces: closed dependency graph
  consumed by: output (terminal)

======================================================================
Dependency closure verification (C-31): inter-criterion loops explicitly closed:
  C-23 output -> C-24 (NODE 3 -> NODE 8)
  C-26 output -> C-28 (NODE 9 -> NODE 10 -> NODE 11)
  C-24 output -> C-28 (NODE 8 -> NODE 11)
  C-14 output -> C-06 (NODE 4 -> NODE 6)
  C-17+C-21 output -> C-20 (Step 5 -> Step 6)
```

---

### Dependency Closure Enumeration (C-33)

*Standalone terminal block. Separate from chain trace. Spot-checkable without traversal.
Format: `{source criterion} output -> {consuming criterion} ({chain node reference})`.*

```
DEPENDENCY CLOSURE ENUMERATION
================================
C-23 output -> C-24 (NODE 3 -> NODE 8):
  triage rank (NODE 3) is required input for tier-match check (NODE 8);
  NODE 8 cannot verify tiers without NODE 3 triage assignments

C-26 output -> C-28 (NODE 9/10 -> NODE 11):
  gestalt audit verdict (NODE 10) is a named chain node in NODE 11;
  NODE 11 structural qualifier must name NODE 10 as a chain link to satisfy C-28

C-24 output -> C-28 (NODE 8 -> NODE 11):
  traceability verdict (NODE 8) is a named chain node in NODE 11;
  NODE 11 structural qualifier must name NODE 8 to satisfy C-28

C-14 output -> C-06 (NODE 4 -> NODE 6):
  routing tags in entries (NODE 4) are input for handover scenario selection (NODE 6);
  register slot {scenario} requires a named downstream route from NODE 4

C-17+C-21 output -> C-20 (Step 5 -> Step 6):
  name derivation scaffold output (Step 5) is the input to co-validation name-form check
  (Step 6); Step 6 gate cannot run until Step 5 scaffold completes
================================
All 5 loops enumerated. A reviewer can spot-check closure by reading this block
without traversing the chain trace. Any loop absent from this enumeration that
appears in the chain trace is a C-33 violation.
```

**Output**: Steps 7-12 + Dependency Closure Enumeration. Steps 1-6 are scaffolding.

---

## V-03 -- Single-axis: Complete forward-reader rationale at verification tokens (C-34)

**Variation axis:** Token auditability protocol. Each verification verdict token carries an
inline explanation of how a future reader can use the token for audit without session replay.
TRACE-CHECK-VERDICT in R8 V-05 has this: "A future reader verifies the check ran by locating
this token in the output -- no session replay required." GESTALT-VERDICT in R8 V-05 has:
"This verdict is a structural artifact auditable by the same rules as any production link."
This variation makes both tokens carry the same complete protocol statement, and extends each
to declare what the token certifies specifically (not just that it is auditable).

**Hypothesis:** A reader encountering GESTALT-VERDICT: PASS in an output artifact needs to
know (1) how to verify the check ran (locate the token), (2) what PASS certifies (that the
output as a whole does not read as a survey), and (3) what FAIL would contain (entry labels
and gestalt-summary-fail reasons). R8 V-05's GESTALT-VERDICT carries (2) implicitly ("does
not read as survey in aggregate") but not (1) or (3) explicitly. C-34 adds all three.
Hypothesis: explicit protocol at each token enables a reader encountering the token in
isolation to fully audit the step without referring to any other section.

**Builds on:** R8 V-05 -- all 23 aspirational criteria (C-09..C-31) active.

**C-32 and C-33 status:** Not activated. IA invocations carry identity+function only.
No standalone dep enumeration block (chain trace closure satisfies C-31 only).

---

### Prompt Body

You are running `/quest:topic echo` for the topic: {topic}.

All essential signals are in hand. Surface genuine surprises -- retroactively-visible,
cross-signal, contradicting prior assumptions. Not a summary. An echo.

---

### Roles *(C-25; C-30)*

**Institutional Archaeologist (IA)**
Sub-step shorthand: `IA: false-assumption-recovery`. Active: Steps 2, 5, 6, 7, 8, 9.
Function: recovers false assumptions; frames surprises as corrections to false beliefs.

**Gatekeeper**
Sub-step shorthand: `Gatekeeper: adversarial-rejection-only`. Active: Step 3 only.

```
GATEKEEPER -- FUNCTION DECLARATION (C-27)
---------------------------------------------------------------------
Function: Adversarial rejection. Tests predictability and cross-signal emergence.
Not-function: Future-reader framing. Not-function: Thematic synthesis.
Role boundary: Verdicts final. IA cannot reverse.
---------------------------------------------------------------------
```

---

### Step 1 -- Read Signal Record *(C-10; C-12)*

Namespaces covered (>=3), total artifacts, date range.

---

### Step 2 -- Pre-Write Prediction Sort *(IA: false-assumption-recovery; C-16; C-14; C-11; C-09)*

Route: `topic-story` | `topic-report` | `gate-pipeline`. Discard log required, non-empty.

---

### Step 3 -- Multi-Stage Epistemic Gate *(Gatekeeper: adversarial-rejection-only; C-13; C-15; C-16)*

Anti-Pattern Catalog *(C-13)*: CONFIRMATION | RESTATEMENT | ISOLATED-FINDING
Gate format *(C-16)*: `VERDICT: SURPRISE | CUT -- {label}`

**Stage 1** *(Gatekeeper: adversarial-rejection-only; epistemic dimension: novelty)*
"Predictable from first principles?" `PREDICTABLE` -> story | `UNPREDICTABLE` -> Stage 2
**Commit**: `Stage 1: [{item}] -> [PREDICTABLE | UNPREDICTABLE]`

**Stage 2** *(Gatekeeper: adversarial-rejection-only; epistemic dimension: opposition)*
"Contradicts pre-investigation assumption?"
```
We believed: {falsifiable assumption}
VALID: {genuine falsification}
INVALID (absence-of-consideration/sentiment-reaction/hedge-uncertainty): ...
```
Floor *(C-15)*: >=3 CONTRADICTION FOUND. `NO CONTRADICTION` -> report | `CONTRADICTION FOUND` -> Stage 3
**Commit**: `Stage 2: [{item}] -> [NO CONTRADICTION | CONTRADICTION FOUND]`

**Stage 3** *(Gatekeeper: adversarial-rejection-only; epistemic dimension: specificity)*
"Cross-signal or single-artifact?" `SINGLE-ARTIFACT` -> report | `CROSS-SIGNAL` -> SURPRISE
**Commit**: `Stage 3: [{item}] -> [SINGLE-ARTIFACT | CROSS-SIGNAL] -- sources: [{a1}, {a2}]`

---

### Step 4 -- Pre-Write Impact Triage *(C-23; C-22)*

HIGH | MEDIUM | LOW. Failure-first within tier. All assignments recorded before expansion.

---

### Step 5 -- Naming Scaffold *(C-17; C-21; IA: false-assumption-recovery)*

1. Old belief. 2. Correction. 3. Domain. 4. Label: `The {Corrected Belief}: {Domain}`.

---

### Step 6 -- Co-Validation Gate *(C-20; IA: false-assumption-recovery)*

Name form (C-17) VALID + Failure field (C-18) VALID. Both required. Gate per candidate.

---

### Step 7 -- Write Echo Entries *(IA: false-assumption-recovery; C-02..C-04; C-08; C-12; C-14; C-17; C-18; C-22)*

Begin from failure scenario *(C-22)*. Entry template:

**[`The {Corrected Belief}: {Domain}`]** -- *{HIGH | MEDIUM | LOW}* *(IA: false-assumption-recovery)*
Source: `{artifact} ({ns/skill})` `[CROSS: {A} x {B}]`
Temporal anchor: `{round/date}`
We believed: `{assumption}` | The surprise: `{what was found}` | Mis-design *(C-18)*: `{specific failure}`
Impact *(C-03)*: `{decision/assumption/scope}` | Route *(C-14)*: `-> {consumer}`

---

### Step 8 -- Cross-Signal Synthesis *(C-05; IA: false-assumption-recovery)*

<=120 words. >=2 entries by label. What only emerges from reading them together.

---

### Step 9 -- Forward Handover *(C-06; C-19; IA: false-assumption-recovery)*

T-1..T-4 register. State selection. Verify slots. Scenario and constraint both specific.

---

### Step 10 -- Rules of Thumb *(C-07; C-24)*

<=3 rules. HIGH/MEDIUM only. Format: `[{tier}] {rule} (encodes: {NAME})`

Traceability check: tier match, no orphan rules, one-rule-per-surprise. Correct before verdict.

**Write verdict**:

```
TRACE-CHECK-VERDICT: [PASS | FAIL]
  -- PASS: all tiers match; no orphan rules; one-rule-per-surprise confirmed
  -- FAIL: {rule label | expected tier from Step 4 triage | actual tier in entry}
```

*Forward-reader protocol (C-34): A future reader verifies this check ran by locating the
TRACE-CHECK-VERDICT token above in the output -- no session replay required.
TRACE-CHECK-VERDICT: PASS certifies that (1) every rule's tier matches the triage assignment
from Step 4, (2) no rule is an orphan (every rule traces to exactly one named surprise), and
(3) no surprise generated more than one rule.
TRACE-CHECK-VERDICT: FAIL records each mismatch by rule label, expected tier, and actual
tier so a reader can verify the specific failure without re-executing the prompt.*

---

### Step 11 -- Gestalt Summary Audit *(C-26)*

"Could this output be described as a summary of what the investigation found?"
If YES/PARTLY YES: revise entries, add `gestalt-summary-fail` to discard log, re-run.

**Write verdict**:

```
GESTALT-VERDICT: [PASS | FAIL]
  -- PASS: output does not read as survey in aggregate; every entry is a
     retroactively-visible surprise, not a survey item included for coverage
  -- FAIL: {each revised or discarded entry with its gestalt-summary-fail trigger reason}
```

*Forward-reader protocol (C-34): A future reader verifies this check ran by locating the
GESTALT-VERDICT token above in the output -- no session replay required.
GESTALT-VERDICT: PASS certifies that the complete output, read as a whole unit and not
entry-by-entry, does not pass the summary-or-survey test from Step 11's audit question.
GESTALT-VERDICT: FAIL identifies which entries triggered the gestalt-summary-fail pattern
and what revision was applied to each, enabling a reader to audit the revision without
access to the pre-revision draft.*

---

### Step 12 -- Production Chain Trace *(C-28; C-29; C-31)*

```
PRODUCTION CHAIN TRACE
======================================================================

[NODE 1] typed-route prediction sort
  structural qualifier: IA: false-assumption-recovery (C-30), anti-hypothesis guard (C-11),
    typed destinations (C-14), non-empty discard log (C-09)
  produces: route decisions, discard log
  consumed by: NODE 2

-> [NODE 2] staged gate verdict
  structural qualifier: Gatekeeper: adversarial-rejection-only per Stage (C-30), commits
    with collapse prohibition (C-13+C-16), VALID/INVALID gallery (C-18), cross-signal
    citation (C-08 prereq), floor tracked (C-15)
  produces: SURPRISE verdicts, floor count
  consumed by: NODE 3

-> [NODE 3] comparative triage rank
  structural qualifier: simultaneous comparison (C-23), failure-first (C-22), written first
  produces: tier assignments, order
  consumed by: NODE 4, NODE 8

-> [NODE 4] echo entry
  structural qualifier: IA: false-assumption-recovery (C-30), 4-step scaffold (C-17+C-21),
    failure-first production (C-22), [CROSS] (C-08), failure field (C-18), named impact (C-03)
  produces: named labels, citations, impact, routes
  consumed by: NODEs 5, 6, 7

-> [NODE 5] synthesis
  structural qualifier: >=2 named labels, cross-entry pattern unreachable from single entry (C-05)
  produces: echo paragraph | consumed by: output

-> [NODE 6] handover
  structural qualifier: T-1..T-4 register (C-19), slots verified (C-06)
  produces: handoff statement | consumed by: output

-> [NODE 7] rules
  structural qualifier: tier vs NODE 3, orphan check, one-rule-per-surprise
  produces: verified rules (C-07+C-24) | consumed by: NODE 8

-> [NODE 8] TRACE-CHECK-VERDICT [C-29: chain node with forward-reader rationale (C-34)]
  structural qualifier: PASS|FAIL token; forward-reader protocol at token definition;
    certifies tier-match, no-orphan, one-rule-per-surprise
  produces: traceability result (C-24+C-29+C-34)
  consumed by: NODE 11

-> [NODE 9] gestalt audit
  structural qualifier: applied to complete artifact (C-26), gestalt-fail separate (C-26)
  produces: gestalt result | consumed by: NODE 10

-> [NODE 10] GESTALT-VERDICT [C-29: chain node with forward-reader rationale (C-34)]
  structural qualifier: PASS|FAIL token; forward-reader protocol at token definition;
    certifies output-level non-survey; FAIL records revision reasons
  produces: gestalt result (C-26+C-29+C-34)
  consumed by: NODE 11

-> [NODE 11] chain trace (this node)
  structural qualifier: all nodes with verifiable qualifiers (C-28), verification nodes
    included (C-29), dependencies annotated -- closed (C-31)
  produces: auditable dependency graph | consumed by: output

======================================================================
Dependency closure verification (C-31):
  C-23 output -> C-24 (NODE 3 -> NODE 8)
  C-26 output -> C-28 (NODEs 9/10 -> NODE 11)
  C-24 output -> C-28 (NODE 8 -> NODE 11)
  C-14 output -> C-06 (NODE 4 -> NODE 6)
  C-17+C-21 output -> C-20 (Step 5 -> Step 6)
```

**Output**: Steps 7-12. Steps 1-6 are scaffolding.

---

## V-04 -- Combined: C-32 + C-33, no C-34

**Variation axis:** Epistemic dimension at every IA invocation (C-32) + standalone terminal
dependency enumeration (C-33). Token forward-reader rationale not extended (C-34 absent --
GESTALT-VERDICT retains R8 V-05 form).

**Hypothesis:** C-32 and C-33 operate at different structural positions -- C-32 governs
role-invocation annotation granularity (execution time), C-33 governs post-chain output
structure (output time). Together they extend the annotation system and the closure artifact
without touching the token definitions. If V-04 scores lower than V-05, the delta is C-34
alone -- the value of symmetric forward-reader rationale at both tokens.

**Builds on:** V-01 (C-32 mechanism) + V-02 (C-33 mechanism). C-34 not present.

---

### Prompt Body

You are running `/quest:topic echo` for the topic: {topic}.

All essential signals are in hand. Surface genuine surprises -- retroactively-visible,
cross-signal, contradicting prior assumptions. Not a summary. An echo.

---

### Roles *(C-25; C-30; C-32: epistemic dimension at every role invocation)*

**Institutional Archaeologist (IA)**
Sub-step shorthand: `IA: false-assumption-recovery; epistemic dimension: {step-specific}`
Active: Steps 2, 5, 6, 7, 8, 9.

Epistemic dimensions per IA step:

| Step | Epistemic Dimension | Why here |
|------|---------------------|----------|
| 2 | prior-frame-recovery | Recovering what was actually believed before investigation |
| 5 | belief-inversion | Deriving the correction-encoding name from the inverted assumption |
| 6 | correction-integrity | Verifying both name form and failure field structurally encode the correction |
| 7 | failure-projection | Anchoring entry production in the projected mis-design scenario |
| 8 | pattern-emergence | Identifying what only becomes visible when entries are read together |
| 9 | future-framing | Translating institutional memory into actionable builder guidance |

**Gatekeeper**
Sub-step shorthand: `Gatekeeper: adversarial-rejection-only; epistemic dimension:
{stage-specific}` -- see Stage headers. Active: Step 3 only.

```
GATEKEEPER -- FUNCTION DECLARATION (C-27)
---------------------------------------------------------------------
Function: Adversarial rejection. Tests predictability and cross-signal emergence.
Not-function: Future-reader framing (IA domain). Not-function: Thematic synthesis.
Role boundary: Verdicts final. IA cannot reverse.
---------------------------------------------------------------------
```

---

### Step 1 -- Read Signal Record *(C-10; C-12)*

Namespaces covered (>=3), total artifacts, date range.

---

### Step 2 -- Pre-Write Prediction Sort
*(IA: false-assumption-recovery; epistemic dimension: prior-frame-recovery -- recovering
what beliefs were actually held, not what the spec asserts; C-16; C-14; C-11; C-09)*

Route: `topic-story` | `topic-report` | `gate-pipeline`

Anti-hypothesis guard *(C-11; IA: false-assumption-recovery; epistemic dimension:
prior-frame-recovery)*: confirms original hypothesis? -> `topic-story`.

Discard log *(C-09)*: non-empty, every routed item with type, reason, destination.

---

### Step 3 -- Multi-Stage Epistemic Gate *(Gatekeeper: adversarial-rejection-only; C-13; C-15; C-16)*

Anti-Pattern Catalog *(C-13)*: CONFIRMATION | RESTATEMENT | ISOLATED-FINDING
Gate format *(C-16)*: `VERDICT: SURPRISE | CUT -- {label}`

**Stage 1** *(Gatekeeper: adversarial-rejection-only; epistemic dimension: novelty --
separating investigation-emergent from predictable-from-materials)*
"Predictable?" `PREDICTABLE` -> story | `UNPREDICTABLE` -> Stage 2
**Commit**: `Stage 1: [{item}] -> [PREDICTABLE | UNPREDICTABLE]`

**Stage 2** *(Gatekeeper: adversarial-rejection-only; epistemic dimension: opposition --
separating genuine contradiction of a held belief from mere notability)*
"Contradicts pre-investigation assumption?"
```
We believed: {falsifiable assumption}
VALID: {genuine falsification -- names belief and contradiction}
INVALID (absence-of-consideration): ...
INVALID (sentiment-reaction): ...
INVALID (hedge-uncertainty): ...
```
Floor *(C-15)*: >=3 CONTRADICTION FOUND.
**Commit**: `Stage 2: [{item}] -> [NO CONTRADICTION | CONTRADICTION FOUND]`

**Stage 3** *(Gatekeeper: adversarial-rejection-only; epistemic dimension: specificity --
separating traceable cross-signal findings from single-artifact findings)*
"Cross-signal?" `SINGLE-ARTIFACT` -> report | `CROSS-SIGNAL` -> SURPRISE
**Commit**: `Stage 3: [{item}] -> [SINGLE-ARTIFACT | CROSS-SIGNAL] -- sources: [{a1}, {a2}]`

---

### Step 4 -- Pre-Write Impact Triage *(C-23; C-22)*

HIGH | MEDIUM | LOW. Failure-first within tier. All assignments before expansion.

---

### Step 5 -- Naming Scaffold
*(C-17; C-21; IA: false-assumption-recovery; epistemic dimension: belief-inversion --
the name is derived by inverting the false assumption, encoding what was wrong and where)*

1. Old belief. 2. Correction. 3. Domain. 4. Label: `The {Corrected Belief}: {Domain}`.
VALID: "The Silent Veto: Adoption Workflow". INVALID: "Surprising Finding About Adoption".

---

### Step 6 -- Co-Validation Gate
*(C-20; IA: false-assumption-recovery; epistemic dimension: correction-integrity --
verifying both structural form checks pass simultaneously before expansion)*

Name form (C-17) VALID + Failure field (C-18) VALID. Both required per candidate.

---

### Step 7 -- Write Echo Entries
*(IA: false-assumption-recovery; epistemic dimension: failure-projection -- entry begins
from projected mis-design; the failure is load-bearing; C-02..C-04; C-08; C-12; C-14;
C-17; C-18; C-22)*

Begin from failure *(C-22; IA: false-assumption-recovery; epistemic dimension:
failure-projection)*: anchor on specific mis-design if old assumption is carried.

**[`The {Corrected Belief}: {Domain}`]** -- *{HIGH | MEDIUM | LOW}* *(IA: false-assumption-recovery; epistemic dimension: failure-projection)*

Source: `{artifact} ({ns/skill})` `[CROSS: {A} x {B}]`
Temporal anchor: `{round/date}`
We believed: `{assumption}` | The surprise: `{what was found}` | Mis-design *(C-18)*: `{specific}`
Impact *(C-03)*: `{decision/assumption/scope}` | Route *(C-14)*: `-> {consumer}`

---

### Step 8 -- Cross-Signal Synthesis
*(C-05; IA: false-assumption-recovery; epistemic dimension: pattern-emergence -- naming
what only becomes visible when entries are read together; absent from any single entry)*

<=120 words. >=2 entries by label. Cross-entry pattern.

---

### Step 9 -- Forward Handover
*(C-06; C-19; IA: false-assumption-recovery; epistemic dimension: future-framing --
translating institutional memory into a directive for a future builder)*

T-1..T-4 register. State selection before writing. Slots specific and citable.

---

### Step 10 -- Rules of Thumb *(C-07; C-24)*

<=3 rules. HIGH/MEDIUM only. `[{tier}] {rule} (encodes: {NAME})`

Tier-match check before verdict.

```
TRACE-CHECK-VERDICT: [PASS | FAIL]
  -- PASS: all tiers match; no orphan rules; one-rule-per-surprise confirmed
  -- FAIL: {mismatch detail}
```

This verdict is a structural artifact. A future reader verifies the check ran by locating
this token in the output -- no session replay required.

---

### Step 11 -- Gestalt Summary Audit *(C-26)*

"Could this output be described as a summary of what the investigation found?"
Revise if YES/PARTLY YES. Add `gestalt-summary-fail` to discard log.

```
GESTALT-VERDICT: [PASS | FAIL]
  -- PASS: output does not read as survey in aggregate
  -- FAIL: {revised/discarded entries with gestalt-summary-fail reason}
```

This verdict is a structural artifact auditable by the same rules as any production link.

---

### Step 12 -- Production Chain Trace *(C-28; C-29; C-31)*

```
PRODUCTION CHAIN TRACE
VERIFICATION NODES INCLUDED (C-29) | DEPENDENCY GRAPH CLOSED (C-31)
======================================================================

[NODE 1] typed-route prediction sort
  structural qualifier: IA: false-assumption-recovery; epistemic dimension:
    prior-frame-recovery (C-30+C-32), anti-hypothesis guard (C-11), typed destinations
    (C-14), non-empty discard log (C-09)
  produces: route decisions (C-16), discard log (C-09+C-14)
  consumed by: NODE 2

-> [NODE 2] staged gate verdict
  structural qualifier: Gatekeeper: adversarial-rejection-only; epistemic dimension per
    stage (novelty/opposition/specificity) at Stage headers (C-30+C-32), per-stage commits
    with collapse prohibition (C-13+C-16), VALID/INVALID gallery (C-18 scaffolding),
    cross-signal citation (C-08 prereq), floor tracked (C-15)
  produces: SURPRISE verdicts (C-13/C-16), floor count (C-15)
  consumed by: NODE 3

-> [NODE 3] comparative triage rank
  structural qualifier: simultaneous (C-23), failure-first (C-22), written before expansion
  produces: tier assignments (C-23), order (C-22)
  consumed by: NODE 4, NODE 8

-> [NODE 4] echo entry
  structural qualifier: IA: false-assumption-recovery; epistemic dimension:
    failure-projection per sub-step (C-30+C-32); 4-step scaffold (C-17+C-21); failure-first
    production (C-22); [CROSS] (C-08); failure field (C-18); named impact (C-03)
  produces: labels (C-04), citations (C-02), impact (C-03), routes (C-14)
  consumed by: NODEs 5, 6, 7

-> [NODE 5] synthesis
  structural qualifier: IA: false-assumption-recovery; epistemic dimension: pattern-emergence
    (C-30+C-32); >=2 named labels; cross-entry pattern unreachable from single entry (C-05)
  produces: echo paragraph | consumed by: output

-> [NODE 6] handover
  structural qualifier: IA: false-assumption-recovery; epistemic dimension: future-framing
    (C-30+C-32); T-1..T-4 register (C-19); slots verified (C-06)
  produces: handoff statement | consumed by: output

-> [NODE 7] rules
  structural qualifier: tier vs NODE 3, orphan check, one-rule-per-surprise
  produces: verified rules (C-07+C-24) | consumed by: NODE 8

-> [NODE 8] TRACE-CHECK-VERDICT [C-29: chain node]
  structural qualifier: PASS|FAIL token; verifiable by locating token; mismatches recorded
  produces: traceability result (C-24+C-29) | consumed by: NODE 11

-> [NODE 9] gestalt audit
  structural qualifier: IA on complete artifact (C-26+C-30), gestalt-fail distinct (C-26)
  produces: gestalt result | consumed by: NODE 10

-> [NODE 10] GESTALT-VERDICT [C-29: chain node]
  structural qualifier: PASS|FAIL token; verifiable by location; revisions recorded if FAIL
  produces: gestalt result (C-26+C-29) | consumed by: NODE 11

-> [NODE 11] chain trace (this node)
  structural qualifier: all nodes with verifiable qualifiers (C-28), verification nodes
    included (C-29), all dependencies annotated (C-31)
  produces: closed dependency graph | consumed by: output

======================================================================
Dependency closure verification (C-31):
  C-23 output -> C-24 (NODE 3 -> NODE 8)
  C-26 output -> C-28 (NODEs 9/10 -> NODE 11)
  C-24 output -> C-28 (NODE 8 -> NODE 11)
  C-14 output -> C-06 (NODE 4 -> NODE 6)
  C-17+C-21 output -> C-20 (Step 5 -> Step 6)
```

---

### Dependency Closure Enumeration (C-33)

*Standalone terminal block. Separate from chain trace. Spot-checkable without traversal.*

```
DEPENDENCY CLOSURE ENUMERATION
================================
C-23 output -> C-24 (NODE 3 -> NODE 8):
  triage rank (NODE 3) required for tier-match check (NODE 8)

C-26 output -> C-28 (NODEs 9/10 -> NODE 11):
  gestalt verdict (NODE 10) is named chain node in NODE 11 (C-28 requires it)

C-24 output -> C-28 (NODE 8 -> NODE 11):
  traceability verdict (NODE 8) is named chain node in NODE 11

C-14 output -> C-06 (NODE 4 -> NODE 6):
  routing tags in entries (NODE 4) feed handover scenario selection (NODE 6)

C-17+C-21 output -> C-20 (Step 5 -> Step 6):
  naming scaffold (Step 5) feeds co-validation name-form check (Step 6)
================================
All 5 loops. Reviewer can spot-check without chain traversal.
```

**Output**: Steps 7-12 + Dependency Closure Enumeration. Steps 1-6 are scaffolding.

---

## V-05 -- Full Synthesis: All 26 Aspirational Criteria (C-09..C-34)

**Variation axis:** Full combination -- C-32 (epistemic dimension at every named-role
invocation), C-33 (standalone terminal dep enumeration), and C-34 (complete forward-reader
protocol at both verification tokens) all active simultaneously, composing with the 23 prior
criteria from R8 V-05.

**Hypothesis:** C-32, C-33, and C-34 activate at three non-overlapping structural positions:
C-32 at every role sub-step invocation (execution-time annotation), C-33 in a standalone
terminal block after the chain trace closes (output-time extraction artifact), C-34 at each
verdict token definition (self-describing audit protocol). None overlap with each other or
with C-09..C-31. Together they close three distinct gaps in R8 V-05: (1) IA invocations
outside the Gate carried only identity+function, requiring a model to infer the epistemic
posture without an inline name; (2) dependency closure required traversal of the chain trace
to reconstruct; (3) GESTALT-VERDICT lacked the complete forward-reader protocol that
TRACE-CHECK-VERDICT had. The full combination produces an artifact where any reader can
verify: why each epistemic posture was applied (C-32), the complete dependency graph without
traversal (C-33), and how each audit token certifies its check (C-34). V-05 is designed to
become the new baseline for v10 development.

**Builds on:** R8 V-05 (all 23 aspirational criteria C-09..C-31) + V-01 (C-32) +
V-02 (C-33) + V-03 (C-34).

---

### Prompt Body

You are running `/quest:topic echo` for the topic: {topic}.

All essential signals are in hand. Your task: surface the genuine surprises -- findings that
only became visible in retrospect, from cross-signal tension, that no competent practitioner
would have predicted before gathering evidence.

Not a summary. Not a survey of discoveries. An echo: the signal that comes back that you
didn't send.

---

### Roles *(C-25: two distinct named roles; C-30: sub-step identity+function co-activation;
C-32: epistemic dimension at every named-role invocation completing the three-part
annotation: who + what operationally + why here)*

**Institutional Archaeologist (IA)**
*First invocation: Step 2.*
Function: Recovers false assumptions embedded in current materials -- what a future team
would carry as truth without knowing otherwise. Frames every surprise as a correction to a
false assumption (C-17). Derives consequence by asking "What would the next team build
wrong?" (C-18, C-22). The IA is the author of implication; the Gatekeeper is the author of
rejection.

Sub-step co-activation shorthand *(C-30, C-32)*: each IA invocation carries:
`IA: false-assumption-recovery; epistemic dimension: {name}`
The epistemic dimension names why this posture applies at this specific step.

Defined dimensions:

| Step | Epistemic Dimension | Why here |
|------|---------------------|----------|
| 2 | prior-frame-recovery | Recovering what was actually believed, not what spec asserts |
| 5 | belief-inversion | Deriving the correction-encoding name by inverting the false assumption |
| 6 | correction-integrity | Verifying both structural form checks encode the correction |
| 7 | failure-projection | Anchoring entry in the projected mis-design; failure is load-bearing |
| 8 | pattern-emergence | What only emerges when entries are read together; absent from any single |
| 9 | future-framing | Translating internal findings into actionable guidance for a future builder |

Active: Steps 2, 5, 6, 7, 8, 9.

**Gatekeeper**
*First invocation: Step 3.*
Sub-step shorthand *(C-30, C-32)*: `Gatekeeper: adversarial-rejection-only; epistemic
dimension: {stage-label}` -- see Stage headers.

```
GATEKEEPER -- FUNCTION DECLARATION (C-27)
---------------------------------------------------------------------
Function:      Adversarial rejection. Tests each gate-pipeline candidate: (1)
               first-principles predictability; (2) cross-signal requirement.
               Fails either: rejected.

Not-function:  Future-reader framing. The Gatekeeper does not ask what the
               next team would get wrong. That is the IA's domain.

Not-function:  Thematic synthesis or cross-item grouping. The Gatekeeper
               evaluates each candidate in isolation.

Role boundary: Gatekeeper verdicts are final. The IA cannot reverse a rejection.
               The Gatekeeper tests the candidate; the IA frames the implication.
---------------------------------------------------------------------
```

Active: Step 3 only.

---

### Step 1 -- Read Signal Record *(C-10: multi-namespace coverage; C-12: temporal marking)*

Read all signal artifacts across all namespaces (scout, draft, review, flow, trace, prove,
listen, program, topic). Record: namespaces covered (>=3 floor), total artifacts, date range.

---

### Step 2 -- Pre-Write Prediction Sort
*(IA: false-assumption-recovery; epistemic dimension: prior-frame-recovery -- recovering
what beliefs were actually held before investigation, not what the spec states; C-16:
structurally-enforced filter; C-14: downstream routing; C-11: anti-hypothesis guard;
C-09: discard visibility)*

Route types:
- `topic-story` -- confirms hypothesis; destination: topic narrative *(C-14)*
- `topic-report` -- restates known constraint; destination: report *(C-14)*
- `gate-pipeline` -- candidate surprise; proceeds to Step 3

Anti-hypothesis guard *(C-11; IA: false-assumption-recovery; epistemic dimension:
prior-frame-recovery)*: "Does this item confirm what the investigation set out to prove?"
YES -> `topic-story`.

Discard log *(C-09; IA: false-assumption-recovery; epistemic dimension:
prior-frame-recovery)*: every non-gate item with route type, reason (1 sentence), destination.
Non-empty required.

---

### Step 3 -- Multi-Stage Epistemic Gate
*(Gatekeeper: adversarial-rejection-only; C-13: typed skeptic gate; C-15: minimum surprise
floor; C-16: structurally-enforced filter)*

```
GATEKEEPER: adversarial-rejection-only -- active from here through end of Stage 3.
```

**Anti-Pattern Catalog** *(C-13)*:
- CONFIRMATION: confirms original hypothesis -> PREDICTABLE
- RESTATEMENT: documents known constraint -> `topic-report`
- ISOLATED-FINDING: complete in one artifact -> `topic-report`

**Gate format** *(C-16)*: `VERDICT: SURPRISE | CUT -- {anti-pattern label}`

**Stage 1 -- Prediction Test**
*(Gatekeeper: adversarial-rejection-only; epistemic dimension: novelty -- separating
investigation-emergent findings from outcomes predictable from original design materials)*

"Would a competent practitioner have predicted this from first principles, prior to any
signal gathering?"
`PREDICTABLE` -> `topic-story` | `UNPREDICTABLE` -> Stage 2
**Commit**: `Stage 1: [{item}] -> [PREDICTABLE | UNPREDICTABLE]`

---

**Stage 2 -- Contradiction Test**
*(Gatekeeper: adversarial-rejection-only; epistemic dimension: opposition -- separating
genuine contradiction of a held belief from findings that are merely notable or unusual)*

"Does this item contradict an assumption from the pre-investigation frame?"

```
We believed: {falsifiable assumption -- names a specific held belief}
VALID: {genuine falsification -- names belief and contradiction}
INVALID (absence-of-consideration): notes absence, not a falsifiable proposition
INVALID (sentiment-reaction): records team response, not a prior belief state
INVALID (hedge-uncertainty): names a gap, not a held belief
```

Floor *(C-15)*: >=3 must reach CONTRADICTION FOUND.
`NO CONTRADICTION` -> `topic-report` | `CONTRADICTION FOUND` -> Stage 3
**Commit**: `Stage 2: [{item}] -> [NO CONTRADICTION | CONTRADICTION FOUND]`

---

**Stage 3 -- Attribution Test**
*(Gatekeeper: adversarial-rejection-only; epistemic dimension: specificity -- separating
traceable cross-signal findings from single-artifact findings that cannot generate an echo)*

"Does this finding emerge only when >=2 signal artifacts are read together?"
`SINGLE-ARTIFACT` -> `topic-report` | `CROSS-SIGNAL (cite >=2 artifacts)` -> SURPRISE
**Commit**: `Stage 3: [{item}] -> [SINGLE-ARTIFACT | CROSS-SIGNAL] -- sources: [{a1}, {a2}]`

---

### Step 4 -- Pre-Write Impact Triage *(C-23: triage as pre-write scaffolding; C-22)*

Assign comparatively. HIGH | MEDIUM | LOW. Failure-first within tier.
All assignments written before any expansion begins.

---

### Step 5 -- Naming Scaffold
*(C-17; C-21; IA: false-assumption-recovery; epistemic dimension: belief-inversion -- the
name is derived by inverting the false assumption; the label encodes what was wrong and
where, not a description of the discovery)*

1. State old belief. 2. State correction. 3. Derive domain. 4. Form: `The {Corrected Belief}: {Domain}`.
VALID: "The Silent Veto: Adoption Workflow". INVALID: "Surprising Finding About Adoption".

---

### Step 6 -- Pre-Expansion Co-Validation Gate
*(C-20; IA: false-assumption-recovery; epistemic dimension: correction-integrity --
verifying that both structural form checks encode the correction before any expansion begins;
neither alone suffices)*

Both VALID required. Either failing blocks expansion.
- Name form *(C-17)*: `The {Corrected Belief}: {Domain}`? -> VALID / INVALID
- Failure field *(C-18)*: "If next team carries old assumption, {specific mis-design}"? -> VALID / INVALID

---

### Step 7 -- Write Echo Entries
*(IA: false-assumption-recovery; epistemic dimension: failure-projection -- entry begins
from the projected mis-design; failure scenario is load-bearing, not derived; triage order;
failure-first within tier; C-02..C-04; C-08; C-12; C-14; C-17; C-18; C-22)*

Begin from failure *(C-22; IA: false-assumption-recovery; epistemic dimension:
failure-projection)*: If the next team carries the old assumption about {domain}, they would
{specific mis-design}. Anchor.

**[`The {Corrected Belief}: {Domain}`]** -- *{HIGH | MEDIUM | LOW}*
*(IA: false-assumption-recovery; epistemic dimension: failure-projection)*

Source signal: `{artifact-name} ({namespace}/{skill})`
`[CROSS: {artifact-A} x {artifact-B}]` *(C-08)*
Temporal anchor *(C-12)*: `{round or date}`
We believed: `{falsifiable assumption}`
The surprise: `{what signals revealed}`
If the next team carries old assumption *(C-18)*: `{specific concrete mis-design}`.
Design impact *(C-03)*: `{decision revisited / assumption struck / scope boundary shifted}`.
Downstream route *(C-14)*: `-> {skill or namespace}`.

---

### Step 8 -- Cross-Signal Synthesis
*(C-05; IA: false-assumption-recovery; epistemic dimension: pattern-emergence -- naming what
only becomes visible when entries are read together; unreachable from any single entry alone)*

<=120 words. Name >=2 entries by label. Cross-entry pattern only.

---

### Step 9 -- Forward Handover Guidance
*(C-06; C-19; IA: false-assumption-recovery; epistemic dimension: future-framing --
translating institutional memory into a directive for a future builder who did not
participate in this investigation)*

T-1..T-4 register. State selection. Verify slots. Scenario and constraint specific.

---

### Step 10 -- Rules of Thumb *(C-07; C-24)*

<=3 rules. HIGH/MEDIUM only. `[{tier}] {rule} (encodes: {NAME})`

Tier-match, no orphans, one-rule-per-surprise. Correct before writing verdict.

**Write verdict**:

```
TRACE-CHECK-VERDICT: [PASS | FAIL]
  -- PASS: all tiers match; no orphan rules; one-rule-per-surprise confirmed
  -- FAIL: {rule label | expected tier from Step 4 | actual tier in entry}
```

*Forward-reader protocol (C-34): A future reader verifies this check ran by locating
the TRACE-CHECK-VERDICT token above in the output -- no session replay required.
TRACE-CHECK-VERDICT: PASS certifies that (1) every rule's tier matches the triage tier from
Step 4, (2) no rule is an orphan without a named surprise source, and (3) no surprise
generated more than one rule. TRACE-CHECK-VERDICT: FAIL records each specific mismatch by
rule label, expected tier, and actual tier, enabling a reader to audit the failure without
re-executing the prompt.*

---

### Step 11 -- Gestalt Summary Audit *(C-26)*

*Applied to complete draft (Steps 7-10) as a single unit.*

"Could this output be described as a summary or survey of what the investigation found?"
If YES/PARTLY YES: revise, add `gestalt-summary-fail` to discard log, re-run.

**Write verdict**:

```
GESTALT-VERDICT: [PASS | FAIL]
  -- PASS: output does not read as survey in aggregate; every entry is a
     retroactively-visible surprise, not a survey item included for coverage
  -- FAIL: {each entry: label, gestalt-summary-fail trigger reason, revision applied}
```

*Forward-reader protocol (C-34): A future reader verifies this check ran by locating
the GESTALT-VERDICT token above in the output -- no session replay required.
GESTALT-VERDICT: PASS certifies that the complete output, read as a whole unit and not
entry-by-entry, does not pass the summary-or-survey audit question from Step 11.
GESTALT-VERDICT: FAIL identifies which specific entries triggered the gestalt-summary-fail
pattern and records what revision was applied to each, enabling a reader to audit the
revision decision without access to the pre-revision draft.*

---

### Step 12 -- Production Chain Trace
*(C-28: full-chain with structural qualifiers; C-29: verification steps as chain nodes;
C-31: closed dependency graph)*

```
PRODUCTION CHAIN TRACE
VERIFICATION NODES INCLUDED (C-29) | DEPENDENCY GRAPH CLOSED (C-31)
======================================================================

[NODE 1] typed-route prediction sort
  structural qualifier: IA: false-assumption-recovery; epistemic dimension:
    prior-frame-recovery co-activation per route (C-30+C-32), anti-hypothesis guard per
    candidate (C-11), typed downstream destination per discard (C-14), non-empty discard
    log as structural requirement (C-09)
  produces: typed route decisions (C-16), discard log with destinations (C-09+C-14)
  consumed by: NODE 2 (receives gate-pipeline candidates only)

-> [NODE 2] staged gate verdict
  structural qualifier: Gatekeeper: adversarial-rejection-only; epistemic dimension
    (novelty/opposition/specificity) at each Stage header (C-30+C-32), per-stage written
    commit tokens with collapse prohibition (C-13+C-16), falsifiable "We believed:" +
    VALID/INVALID contrast gallery per Stage 2 (C-18 scaffolding), cross-signal citation per
    Stage 3 SURPRISE (C-08 prereq), minimum floor tracked (C-15)
  produces: SURPRISE verdicts (C-13/C-16), floor count (C-15)
  consumed by: NODE 3

-> [NODE 3] comparative triage rank
  structural qualifier: all candidates evaluated simultaneously before any tier assigned
    (C-23), failure-first ordering within tier (C-22), all tiers recorded before expansion
  produces: HIGH/MEDIUM/LOW assignments (C-23), within-tier order (C-22)
  consumed by: NODE 4 entry headers (C-07), NODE 8 TRACE-CHECK-VERDICT (C-24)

-> [NODE 4] echo entry
  structural qualifier: IA: false-assumption-recovery; epistemic dimension:
    failure-projection at each sub-step (C-30+C-32); 4-step naming scaffold (C-17+C-21);
    failure-first production (C-22); [CROSS: A x B] (C-08); failure field as concrete
    mis-design (C-18); named impact (C-03)
  produces: named labels (C-04), citations (C-02), impact (C-03), routes (C-14)
  consumed by: NODE 5, NODE 6, NODE 7

-> [NODE 5] cross-signal synthesis
  structural qualifier: IA: false-assumption-recovery; epistemic dimension:
    pattern-emergence (C-30+C-32); >=2 named labels cited by exact label; cross-entry
    pattern stated as unreachable from single entry (C-05 definitional line)
  produces: synthesized echo paragraph (C-05)
  consumed by: output (terminal)

-> [NODE 6] forward handover guidance
  structural qualifier: IA: false-assumption-recovery; epistemic dimension:
    future-framing (C-30+C-32); T-1..T-4 register (C-19); slots verified (C-06)
  produces: register-anchored handoff (C-06+C-19)
  consumed by: output (terminal)

-> [NODE 7] impact-anchored rule
  structural qualifier: tier verified against NODE 3 triage (C-24), orphan check,
    one-rule-per-surprise
  produces: verified rules (C-07+C-24)
  consumed by: NODE 8

-> [NODE 8] TRACE-CHECK-VERDICT [C-29: chain node; C-34: forward-reader protocol inline]
  structural qualifier: written PASS|FAIL token with forward-reader protocol (C-34)
    certifying tier-match (from NODE 3), no-orphan, and one-rule-per-surprise; verifiable
    by token location without session replay; mismatches recorded by label if FAIL
  produces: traceability audit result (C-24+C-29+C-34)
  consumed by: NODE 11 (C-28+C-31: TRACE-CHECK-VERDICT is named node; closes
               C-23->C-24->NODE 8 dependency loop)

-> [NODE 9] gestalt audit
  structural qualifier: IA: false-assumption-recovery applied to complete artifact as
    unit (C-26+C-30); gestalt-summary-fail logged separately from gate-fail (C-26)
  produces: gestalt audit result (C-26)
  consumed by: NODE 10

-> [NODE 10] GESTALT-VERDICT [C-29: chain node; C-34: forward-reader protocol inline]
  structural qualifier: written PASS|FAIL token with forward-reader protocol (C-34)
    certifying output-level non-survey and recording revision reasons if FAIL; verifiable
    by token location without session replay; distinct scope from NODE 8
  produces: gestalt audit result (C-26+C-29+C-34)
  consumed by: NODE 11 (C-28+C-31: GESTALT-VERDICT is named chain node; closes
               C-26 output -> C-28 loop)

-> [NODE 11] production chain trace (this node)
  structural qualifier: all nodes named with qualifiers verifiable from output alone
    (C-28); verification verdicts are chain nodes not meta-gates (C-29); all
    inter-criterion output-to-input relationships explicitly annotated (C-31)
  produces: closed, auditable dependency graph
  consumed by: output (terminal)

======================================================================
Dependency closure verification (C-31): inter-criterion loops explicitly closed:
  C-23 output -> C-24 (NODE 3 -> NODE 8): triage rank feeds tier-match check
  C-26 output -> C-28 (NODE 9/10 -> NODE 11): gestalt verdict is chain node
  C-24 output -> C-28 (NODE 8 -> NODE 11): traceability verdict is chain node
  C-14 output -> C-06 (NODE 4 -> NODE 6): routing feeds handover scenario selection
  C-17+C-21 output -> C-20 (Step 5 -> Step 6): naming scaffold feeds co-validation gate
No inter-criterion dependency is discoverable only by reading the prompt.
```

---

### Dependency Closure Enumeration (C-33)

*Standalone terminal block, separate from and after the chain trace. Spot-checkable without
chain traversal. Format: `{source criterion} output -> {consuming criterion} ({chain node})`.*

```
DEPENDENCY CLOSURE ENUMERATION
================================
C-23 output -> C-24 (NODE 3 -> NODE 8):
  triage rank (NODE 3) is required input for tier-match check (NODE 8);
  NODE 8 cannot verify tier agreement without NODE 3 triage assignments as input

C-26 output -> C-28 (NODE 9/10 -> NODE 11):
  gestalt audit verdict (NODE 10) is a named chain node in NODE 11;
  NODE 11 structural qualifier must name NODE 10 to satisfy C-28's full-chain requirement

C-24 output -> C-28 (NODE 8 -> NODE 11):
  traceability verdict (NODE 8) is a named chain node in NODE 11;
  NODE 11 structural qualifier must name NODE 8 to close the traceability audit loop

C-14 output -> C-06 (NODE 4 -> NODE 6):
  routing tags in entries (NODE 4) feed handover scenario selection (NODE 6);
  the {scenario} slot in the T-1..T-4 register requires a named downstream route from NODE 4

C-17+C-21 output -> C-20 (Step 5 -> Step 6):
  naming scaffold output (Step 5) is the input to co-validation name-form check (Step 6);
  the co-validation gate in Step 6 cannot run until Step 5 scaffold produces a candidate name
================================
5 loops enumerated. Reviewer spot-checks closure by reading this block.
Any loop absent from this enumeration that appears in the chain trace is a C-33 violation.
```

**Output**: Steps 7-12 + Dependency Closure Enumeration. Steps 1-6 are scaffolding.

Final output sequence:
1. Echo entries (triage-ordered, failure-first within tier)
2. Cross-signal synthesis
3. Forward handover guidance (register selection stated)
4. Rules of Thumb
5. TRACE-CHECK-VERDICT (from Step 10) with forward-reader protocol
6. GESTALT-VERDICT (from Step 11) with forward-reader protocol
7. Production chain trace with dependency graph
8. Dependency Closure Enumeration (standalone terminal block)

Minimum surprise floor check *(C-15)*: if fewer than 3 distinct surprises in final output,
note the floor-miss before closing. Do not suppress it.

---

## Predicted Scores (v9 rubric)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 (surprise synthesis frame) | PASS | PASS | PASS | PASS | PASS |
| C-02 (named entries) | PASS | PASS | PASS | PASS | PASS |
| C-03 (source signal) | PASS | PASS | PASS | PASS | PASS |
| C-04 (design impact) | PASS | PASS | PASS | PASS | PASS |
| C-05 (synthesis not summary) | PASS | PASS | PASS | PASS | PASS |
| C-06 (forward handoff) | PASS | PASS | PASS | PASS | PASS |
| C-07 (impact magnitude) | PASS | PASS | PASS | PASS | PASS |
| C-08 (cross-signal explicit) | PASS | PASS | PASS | PASS | PASS |
| C-09 (discard visibility) | PASS | PASS | PASS | PASS | PASS |
| C-10 (multi-namespace coverage) | PASS | PASS | PASS | PASS | PASS |
| C-11 (anti-hypothesis guard) | PASS | PASS | PASS | PASS | PASS |
| C-12 (temporal marking) | PASS | PASS | PASS | PASS | PASS |
| C-13 (typed skeptic gate) | PASS | PASS | PASS | PASS | PASS |
| C-14 (downstream handoff routing) | PASS | PASS | PASS | PASS | PASS |
| C-15 (minimum surprise floor) | PASS | PASS | PASS | PASS | PASS |
| C-16 (structurally-enforced filter) | PASS | PASS | PASS | PASS | PASS |
| C-17 (correction-encoding names) | PASS | PASS | PASS | PASS | PASS |
| C-18 (forward-failure framing) | PASS | PASS | PASS | PASS | PASS |
| C-19 (register-anchored close) | PASS | PASS | PASS | PASS | PASS |
| C-20 (pre-expansion co-validation) | PASS | PASS | PASS | PASS | PASS |
| C-21 (derivation scaffold) | PASS | PASS | PASS | PASS | PASS |
| C-22 (failure-first production) | PASS | PASS | PASS | PASS | PASS |
| C-23 (impact triage pre-write) | PASS | PASS | PASS | PASS | PASS |
| C-24 (traceability closure) | PASS | PASS | PASS | PASS | PASS |
| C-25 (two distinct named roles) | PASS | PASS | PASS | PASS | PASS |
| C-26 (gestalt summary test) | PASS | PASS | PASS | PASS | PASS |
| C-27 (adversarial function declaration) | PASS | PASS | PASS | PASS | PASS |
| C-28 (full-chain traceability) | PASS | PASS | PASS | PASS | PASS |
| C-29 (verification steps as chain nodes) | PASS | PASS | PASS | PASS | PASS |
| C-30 (sub-step identity+function) | PASS | PASS | PASS | PASS | PASS |
| C-31 (closed dependency graph) | PASS | PASS | PASS | PASS | PASS |
| C-32 (epistemic dimension at role invocations) | PASS | FAIL | FAIL | PASS | PASS |
| C-33 (terminal dep closure enumeration) | FAIL | PASS | FAIL | PASS | PASS |
| C-34 (forward-reader rationale at tokens) | PARTIAL | PARTIAL | PASS | PARTIAL | PASS |

*C-34 notes:*
- V-01, V-02, V-04: TRACE-CHECK-VERDICT retains R8 V-05 complete forward-reader rationale
  (PASS on that token); GESTALT-VERDICT retains R8 V-05 partial form ("auditable by same
  rules") -- scored PARTIAL. C-34 requires both tokens to carry complete protocol.
- V-03, V-05: Both tokens carry complete forward-reader protocol including what each token
  certifies and what FAIL records -- scored PASS.

**Discriminating pairs:**
- V-01 vs V-05: C-33 FAIL vs PASS, C-34 PARTIAL vs PASS. Isolates dep enumeration + token
  parity value against epistemic-dimension-only baseline.
- V-02 vs V-05: C-32 FAIL vs PASS, C-34 PARTIAL vs PASS. Isolates dimension annotation +
  token parity value against dep-enumeration-only baseline.
- V-03 vs V-05: C-32 FAIL vs PASS, C-33 FAIL vs PASS. Isolates combined dim+dep value
  against token-rationale-only baseline.
- V-04 vs V-05: C-34 PARTIAL vs PASS. Direct isolation of complete token protocol value.
  All other criteria held constant between V-04 and V-05.
