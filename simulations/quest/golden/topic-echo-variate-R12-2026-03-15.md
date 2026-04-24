---
skill: quest-variate
skill_target: topic-echo
date: 2026-03-15
round: 12
rubric: v12
rubric_max: 180
---

# Variations: `topic:echo` -- Round 12

**Rubric:** v12 | **Date:** 2026-03-15

---

## Design Context

R11 differentiating evidence: V-01 vs V-05 delta yields two structural properties observable
but not yet formalized as criteria.

1. **R11 universal-inline-node gap (-> C-40)**: R11 V-01 satisfies C-37 by declaring
   "FLOOR-VERDICT is NODE 12" inline at Step 13. But Steps 2-12 carry no inline node
   declarations. The node sequence is recoverable only from the terminal chain trace -- a
   model executing Step 2 (prediction sort) in isolation cannot determine it is NODE 1. Steps
   5 (naming scaffold) and 6 (co-validation gate) were not chain nodes at all. C-40 closes
   this: every production, gate, and verification step carries `[NODE N: {role}]` in its
   step header at declaration time. Universal coverage makes the chain self-verifying from
   step headers alone. No step can exist without a declared node identity.

2. **R11 step-time authority gap (-> C-41)**: R11 V-05's universal inline-node declarations
   (the approach C-40 now formalizes) contained no explicit authority rule at the trace
   assembly step. The terminal chain trace (Step 12) assembled and confirmed node assignments,
   but the step's own header made no claim about whether it was canonical or confirmatory. A
   model executing Step 12 could silently renumber or correct step-time assignments without
   a detectable violation. C-41 closes this: the step header is the canonical record; the
   terminal trace is confirmatory only. The trace assembly step must explicitly state it
   cannot define, renumber, or override step-time declarations. The epistemic authority flows
   step-execution -> trace-assembly, never in reverse.

**Variation plan:**

- V-01: C-40 only -- universal `[NODE N: {role}]` at every step header (14 nodes, Steps 5/6
  promoted to chain nodes); C-41 NOT addressed (trace authority implicit but undeclared)
- V-02: C-41 only -- explicit step-time authority declaration at Step 12; C-40 NOT addressed
  (only Step 13 carries inline NODE via C-37; intermediate steps carry no inline identity)
- V-03: C-40 + C-41 with authority-embedded node template; `[NODE N: {role} |
  step-time-canonical]` format; 14 nodes; no AUTHORITY-VERDICT token (C-37 gap for token)
- V-04: C-41 with named BACK-FILL-GUARD anti-pattern + BACK-FILL-VERDICT token; C-40 PARTIAL
  (only FLOOR-VERDICT step carries inline node via C-37; no universal headers)
- V-05: Full synthesis -- 15-node universal headers (C-40) + step-time authority declaration
  + AUTHORITY-VERDICT token as NODE 14 (C-41 + C-37) + dep closure updated with 9 loops

**Discriminating pairs:**
- V-01 vs V-05: C-40 PASS both; C-41 V-01 FAIL (trace has no authority declaration), V-05 PASS
- V-02 vs V-05: C-41 PASS both; C-40 V-02 FAIL (intermediate steps carry no inline node), V-05 PASS
- V-03 vs V-05: C-40/C-41 PASS both; V-03 no AUTHORITY-VERDICT token (C-37 PARTIAL for it);
  V-05 C-37 PASS (AUTHORITY-VERDICT declared inline at governing step)
- V-04 vs V-05: C-41 PASS both (different token forms); V-04 C-40 PARTIAL; V-05 C-40 PASS

---

## V-01 -- Single-axis: Universal chain node declaration at every step (C-40)

**Variation axis:** Step header node identity coverage. Every production, gate, and
verification step carries `[NODE N: {role}]` inline in its header, not only steps that
introduce verification tokens. Steps 5 (naming scaffold) and 6 (co-validation gate) become
chain nodes (NODE 4 and NODE 5) for the first time. Total: 14 nodes.

**Hypothesis:** R11 V-01 satisfies C-37 (Step 13 declares FLOOR-VERDICT = NODE 12 inline)
but Steps 2-12 carry no inline node identity -- a model executing any intermediate step in
isolation cannot determine its position in the chain. Promoting Steps 5 and 6 to named chain
nodes and adding `[NODE N]` to all step headers makes the chain self-verifying from headers
alone. The C-41 authority question is not addressed: Step 12 assembles the trace with no
explicit authority claim, leaving open the theoretical path for back-fill. Predicted: C-40
PASS; C-41 FAIL; all C-09..C-39 inherited.

**Builds on:** R11 V-01 -- all 31 aspirational criteria (C-09..C-39) active.

---

### Prompt Body

You are running `/quest:topic echo` for the topic: {topic}.

All essential signals are in hand. Your task: surface the genuine surprises -- findings
that only became visible in retrospect, from cross-signal tension, that no competent
practitioner would have predicted before gathering evidence.

Not a summary. Not a survey of discoveries. An echo: the signal that comes back that you
didn't send.

---

### Roles *(C-25; C-30; C-32)*

**Institutional Archaeologist (IA)**
*First invocation: Step 2.*
Function: Recovers false assumptions embedded in current materials -- what a future team
would carry as truth without knowing otherwise. Frames every surprise as a correction to a
false assumption (C-17). Derives consequence by asking "What would the next team build
wrong?" (C-18, C-22). The IA is the author of implication; the Gatekeeper is the author
of rejection.

Sub-step co-activation shorthand *(C-30, C-32)*: `IA: false-assumption-recovery;
epistemic dimension: {name}` at every invocation.

| Step | Epistemic Dimension    | Why here                                              |
|------|------------------------|-------------------------------------------------------|
| 2    | prior-frame-recovery   | Recovering what was actually believed, not spec text  |
| 5    | belief-inversion       | Deriving correction-encoding name by inverting belief |
| 6    | correction-integrity   | Verifying both form checks encode the correction      |
| 7    | failure-projection     | Anchoring entry in projected mis-design               |
| 8    | pattern-emergence      | What only emerges when entries are read together      |
| 9    | future-framing         | Translating findings to guidance for future builder   |

Active: Steps 2, 5, 6, 7, 8, 9.

**Gatekeeper**
*First invocation: Step 3.*
Shorthand: `Gatekeeper: adversarial-rejection-only; epistemic dimension: {stage-label}`

```
GATEKEEPER -- FUNCTION DECLARATION (C-27)
---------------------------------------------------------------------
Function:      Adversarial rejection. Tests each candidate: (1) first-principles
               predictability; (2) cross-signal requirement. Fails either: rejected.
Not-function:  Future-reader framing (IA's domain).
Not-function:  Thematic synthesis (evaluates candidates in isolation).
Role boundary: Gatekeeper verdicts are final.
---------------------------------------------------------------------
```

Active: Step 3 only.

---

### Step 1 -- Read Signal Record *(C-10; C-12)*

All namespaces (scout, draft, review, flow, trace, prove, listen, program, topic).
Record: namespaces covered (>=3 floor), total artifacts, date range.
Step 1 is scaffolding; it does not enter the production chain.

---

### Step 2 -- [NODE 1: typed-route prediction sort] *(C-40)*
*(IA: false-assumption-recovery; epistemic dimension: prior-frame-recovery; C-16; C-14;
C-11; C-09)*

Routes: `topic-story` | `topic-report` | `gate-pipeline`
Anti-hypothesis guard *(C-11)*: "Confirms investigation hypothesis?" YES -> `topic-story`.
Discard log *(C-09)*: every non-gate item, route type, reason (1 sentence). Non-empty required.

---

### Step 3 -- [NODE 2: staged gate verdict] *(C-40)*
*(Gatekeeper: adversarial-rejection-only; C-13; C-15; C-16)*

Anti-Pattern Catalog *(C-13)*: CONFIRMATION | RESTATEMENT | ISOLATED-FINDING
Gate format *(C-16)*: `VERDICT: SURPRISE | CUT -- {label}`

**Stage 1 -- Prediction Test** *(epistemic dimension: novelty)*
"Would a competent practitioner have predicted this from first principles?"
`PREDICTABLE` -> `topic-story` | `UNPREDICTABLE` -> Stage 2
Commit: `Stage 1: [{item}] -> [PREDICTABLE | UNPREDICTABLE]`

**Stage 2 -- Contradiction Test** *(epistemic dimension: opposition)*
`We believed:` / VALID / INVALID gallery. Floor *(C-15)*: >=3 CONTRADICTION FOUND.
Commit: `Stage 2: [{item}] -> [NO CONTRADICTION | CONTRADICTION FOUND]`

**Stage 3 -- Attribution Test** *(epistemic dimension: specificity)*
"Does this finding emerge only when >=2 signal artifacts are read together?"
`SINGLE-ARTIFACT` -> `topic-report` | `CROSS-SIGNAL` -> SURPRISE
Commit: `Stage 3: [{item}] -> [SINGLE-ARTIFACT | CROSS-SIGNAL] -- sources: [{a1}, {a2}]`

---

### Step 4 -- [NODE 3: comparative triage rank] *(C-40)*
*(C-23; C-22)*

Comparative. HIGH | MEDIUM | LOW. Failure-first within tier. All before expansion.

---

### Step 5 -- [NODE 4: naming scaffold] *(C-40)*
*(C-17; C-21; IA: false-assumption-recovery; epistemic dimension: belief-inversion)*

1. Old belief. 2. Correction. 3. Domain. 4. Form: `The {Corrected Belief}: {Domain}`.
VALID: "The Silent Veto: Adoption Workflow". INVALID: "Surprising Finding About Adoption".

---

### Step 6 -- [NODE 5: pre-expansion co-validation gate] *(C-40)*
*(C-20; IA: false-assumption-recovery; epistemic dimension: correction-integrity)*

Both VALID required. Either failing blocks expansion.
- Name form *(C-17)*: `The {Corrected Belief}: {Domain}`? -> VALID / INVALID
- Failure field *(C-18)*: "If next team carries old assumption, {specific mis-design}"? -> VALID / INVALID

---

### Step 7 -- [NODE 6: echo entry] *(C-40)*
*(IA: false-assumption-recovery; epistemic dimension: failure-projection; C-02..C-04;
C-08; C-12; C-14; C-17; C-18; C-22)*

Begin from failure *(C-22)*: anchor the mis-design first.

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

### Step 8 -- [NODE 7: cross-signal synthesis] *(C-40)*
*(C-05; IA: false-assumption-recovery; epistemic dimension: pattern-emergence)*

<=120 words. Name >=2 entries by exact label. Cross-entry pattern only.

---

### Step 9 -- [NODE 8: forward handover guidance] *(C-40)*
*(C-06; C-19; IA: false-assumption-recovery; epistemic dimension: future-framing)*

T-1..T-4 register. State selection. Verify slots. Scenario and constraint specific.

---

### Step 10 -- [NODE 9: impact-anchored rule] + [NODE 10: TRACE-CHECK-VERDICT] *(C-40)*
*(C-07; C-24)*

<=3 rules. HIGH/MEDIUM only. Tier-match, no orphans, one-rule-per-surprise.

```
TRACE-CHECK-VERDICT: [PASS | FAIL]
  -- PASS: all tiers match; no orphan rules; one-rule-per-surprise confirmed
  -- FAIL: {rule label | expected tier from Step 4 | actual tier in entry}
```
*Forward-reader protocol (C-34): verifiable by TRACE-CHECK-VERDICT token location.*

---

### Step 11 -- [NODE 11: gestalt audit] + [NODE 12: GESTALT-VERDICT] *(C-40)*
*(C-26)*

"Could this output be described as a summary or survey?" If YES: revise, log gestalt-summary-fail.

```
GESTALT-VERDICT: [PASS | FAIL]
  -- PASS: output does not read as survey in aggregate
  -- FAIL: {entry label, gestalt-summary-fail trigger, revision applied}
```
*Forward-reader protocol (C-34): verifiable by GESTALT-VERDICT token location.*

---

### Step 12 -- [NODE 13: production chain trace] *(C-40)*
*(C-28; C-29; C-31)*

*(C-41 NOT ADDRESSED: this trace assembles node assignments but carries no explicit
authority rule. Back-fill through trace assembly is structurally undetectable.)*

```
PRODUCTION CHAIN TRACE
VERIFICATION NODES INCLUDED (C-29) | DEPENDENCY GRAPH CLOSED (C-31)
======================================================================

[NODE 1]  typed-route prediction sort
  structural qualifier: IA+prior-frame-recovery (C-30+C-32), anti-hyp guard (C-11),
    typed destinations (C-14), non-empty discard log (C-09)
  consumed by: NODE 2

-> [NODE 2]  staged gate verdict
  structural qualifier: Gatekeeper+dimension per stage (C-30+C-32), commit tokens
    (C-13+C-16), gallery Stage 2 (C-18), cross-signal Stage 3 (C-08 prereq), floor (C-15)
  consumed by: NODE 3, NODE 14 (floor count for C-36)

-> [NODE 3]  comparative triage rank
  structural qualifier: simultaneous comparison (C-23), failure-first (C-22)
  consumed by: NODE 6 (C-07), NODE 10 TRACE-CHECK-VERDICT (C-24)

-> [NODE 4]  naming scaffold [C-40: promoted from untracked]
  structural qualifier: IA+belief-inversion (C-30+C-32); 4-step derivation (C-21); format (C-17)
  consumed by: NODE 5

-> [NODE 5]  pre-expansion co-validation gate [C-40: promoted from untracked]
  structural qualifier: IA+correction-integrity (C-30+C-32); both-VALID (C-20); blocking
  consumed by: NODE 6

-> [NODE 6]  echo entry
  structural qualifier: IA+failure-projection (C-30+C-32); scaffold from NODE 4 (C-17+C-21);
    failure-first (C-22); [CROSS] (C-08); failure field (C-18); impact (C-03)
  consumed by: NODE 7, NODE 8, NODE 9, NODE 14 (final surprise count)

-> [NODE 7]  cross-signal synthesis
  structural qualifier: IA+pattern-emergence (C-30+C-32); >=2 labels; cross-entry (C-05)

-> [NODE 8]  forward handover guidance
  structural qualifier: IA+future-framing (C-30+C-32); T-1..T-4 (C-19); slots (C-06)

-> [NODE 9]  impact-anchored rule
  structural qualifier: tier vs NODE 3 (C-24), orphan check
  consumed by: NODE 10

-> [NODE 10] TRACE-CHECK-VERDICT [C-29: chain node; C-34: forward-reader protocol]

-> [NODE 11] gestalt audit
  structural qualifier: complete artifact as unit (C-26)
  consumed by: NODE 12

-> [NODE 12] GESTALT-VERDICT [C-29: chain node; C-34: forward-reader protocol]

-> [NODE 13] production chain trace (this)
  structural qualifier: all 14 nodes named with qualifiers (C-28); verification tokens
    are chain nodes (C-29); all 7 inter-criterion deps annotated (C-31)

-> [NODE 14] FLOOR-VERDICT [C-29: chain node; C-36: terminal floor check;
  C-34: forward-reader protocol; C-37: inline node declared at Step 13]
  structural qualifier: PASS|FLOOR-MISS; separate from gate-time floor in NODE 2

======================================================================
CLOSURE CLAIM (C-38): No inter-criterion dependency is discoverable only by reading
the prompt. Known dependencies (7):
  C-23 -> C-24 (NODE 3 -> NODE 10)
  C-26 -> C-28 (NODE 11/12 -> NODE 13)
  C-24 -> C-28 (NODE 10 -> NODE 13)
  C-14 -> C-06 (NODE 6 -> NODE 8)
  C-17+C-21 -> C-20 (NODE 4 -> NODE 5)
  C-15 -> C-36 (NODE 2 -> NODE 14)
  C-36 -> C-28 (NODE 14 -> NODE 13)
Attempt to falsify by reading the full prompt.
```

---

### Dependency Closure Enumeration *(C-33)*

```
DEPENDENCY CLOSURE ENUMERATION
================================
CONTRACT HEADER: Any loop in chain trace but absent here is a C-33 violation. (C-39)

C-23 -> C-24 (NODE 3 -> NODE 10): triage rank feeds tier-match check
C-26 -> C-28 (NODE 11/12 -> NODE 13): gestalt verdict is named chain node
C-24 -> C-28 (NODE 10 -> NODE 13): traceability verdict is named chain node
C-14 -> C-06 (NODE 6 -> NODE 8): routing tags feed handover scenario
C-17+C-21 -> C-20 (NODE 4 -> NODE 5): naming scaffold feeds co-validation
C-15 -> C-36 (NODE 2 -> NODE 14): gate-time floor count feeds terminal check
C-36 -> C-28 (NODE 14 -> NODE 13): FLOOR-VERDICT is named chain node
================================
7 loops enumerated.
Any loop absent from this enumeration that appears in the chain trace is a C-33 violation.
(C-39 postamble)
```

---

**Output**: Steps 7-13 + Dependency Closure Enumeration. Steps 1-6 are scaffolding.

Final output sequence *(C-35)*:
1. Echo entries *(C-02; C-04; C-07; C-08; C-12; C-14; C-17; C-18; C-22)*
2. Cross-signal synthesis *(C-05)*
3. Forward handover guidance *(C-06; C-19)*
4. Rules of Thumb *(C-07; C-24)*
5. TRACE-CHECK-VERDICT *(C-24; C-29; C-34)*
6. GESTALT-VERDICT *(C-26; C-29; C-34)*
7. Production chain trace (14 nodes) + REVIEWER CHALLENGE *(C-28; C-29; C-31; C-38)*
8. Dependency Closure Enumeration *(C-33; C-39)*
9. FLOOR-VERDICT *(C-36)*

### Step 13 -- [NODE 14: FLOOR-VERDICT] *(C-40)*

*(C-37: FLOOR-VERDICT is NODE 14 in the production chain. This inline declaration satisfies
C-37 for this verification token.)*

Count distinct surprises in final output (Item 1 entries). Compare to floor (3).

```
FLOOR-VERDICT: [PASS | FLOOR-MISS]
  -- PASS: distinct surprise count >= 3 confirmed in final output
  -- FLOOR-MISS: {count} surprises present; floor shortfall: {3 - count} required
```

*Forward-reader protocol (C-34): verifiable by FLOOR-VERDICT token location.*
*(C-36: Separate from gate-time floor check in Step 3 Stage 2.)*

---

## V-02 -- Single-axis: Step-time node authority with confirmatory trace (C-41)

**Variation axis:** Trace assembly authority. The chain trace assembly step (Step 12)
carries an explicit step-time authority declaration: step headers are canonical; this trace
is confirmatory only. The declaration prohibits renumbering, back-filling, and override.
C-40 is NOT addressed: only Step 13 carries an inline node declaration (via C-37); all
intermediate steps are anonymous at execution time.

**Hypothesis:** R11 V-01 left the trace assembly step without an authority claim. A model
executing Step 12 sees a list of nodes to assemble but no constraint on whether it is
defining or confirming those assignments. Adding an explicit authority declaration converts
the trace from "assembly" to "confirmation record." C-40 is deliberately absent: intermediate
steps carry no inline identity, creating the discriminating contrast with V-01 and V-05.
Predicted: C-40 FAIL; C-41 PASS; all C-09..C-39 inherited.

**Builds on:** R11 V-01 -- all 31 aspirational criteria (C-09..C-39) active.

---

### Prompt Body

You are running `/quest:topic echo` for the topic: {topic}.

All essential signals are in hand. Surface the genuine surprises -- findings only visible
in retrospect, from cross-signal tension, unpredictable before evidence gathering.

Not a summary. An echo: the signal that comes back that you didn't send.

---

### Roles *(C-25; C-30; C-32)*

**Institutional Archaeologist (IA)** -- *First invocation: Step 2.*
Function: Recovers false assumptions. Frames surprises as corrections (C-17). Derives
consequence: "What would the next team build wrong?" (C-18, C-22).
Sub-step shorthand: `IA: false-assumption-recovery; epistemic dimension: {name}`

| Step | Epistemic Dimension    |
|------|------------------------|
| 2    | prior-frame-recovery   |
| 5    | belief-inversion       |
| 6    | correction-integrity   |
| 7    | failure-projection     |
| 8    | pattern-emergence      |
| 9    | future-framing         |

**Gatekeeper** -- *First invocation: Step 3.*

```
GATEKEEPER -- FUNCTION DECLARATION (C-27)
Function:      Adversarial rejection -- predictability test + cross-signal requirement.
Not-function:  Future-reader framing (IA). Not-function: Thematic synthesis.
Role boundary: Verdicts final.
```

Shorthand: `Gatekeeper: adversarial-rejection-only; epistemic dimension: {stage-label}`

---

### Step 1 *(C-10; C-12)* -- All namespaces. >=3. Record.

### Step 2 *(IA: prior-frame-recovery; C-16; C-14; C-11; C-09)* -- Routes. Discard log.

### Step 3 *(Gatekeeper; C-13; C-15; C-16)*
Anti-Pattern Catalog: CONFIRMATION | RESTATEMENT | ISOLATED-FINDING
Gate format: `VERDICT: SURPRISE | CUT -- {label}`
Stage 1 *(novelty)*: Commit predictability. Stage 2 *(opposition)*: `We believed:` gallery;
floor >=3. Stage 3 *(specificity)*: cross-signal attribution.

### Step 4 *(C-23; C-22)* -- Triage. Failure-first. All before expansion.

### Step 5 *(C-17; C-21; IA: belief-inversion)* -- 4-step naming scaffold.

### Step 6 *(C-20; IA: correction-integrity)* -- Co-validation. Both VALID required.

### Step 7 *(IA: failure-projection; C-02..C-04; C-08; C-12; C-14; C-17; C-18; C-22)*
Begin from failure. Name, source, [CROSS], temporal, belief, surprise, mis-design, impact, route.

### Step 8 *(C-05; IA: pattern-emergence)* -- <=120 words. >=2 named labels. Cross-entry only.

### Step 9 *(C-06; C-19; IA: future-framing)* -- T-1..T-4. State selection. Verify slots.

### Step 10 *(C-07; C-24)*

```
TRACE-CHECK-VERDICT: [PASS | FAIL]
  -- PASS: tiers match; no orphans; one-rule-per-surprise
  -- FAIL: {label | expected | actual}
```
*Forward-reader protocol (C-34): verifiable by token location.*

### Step 11 *(C-26)*

```
GESTALT-VERDICT: [PASS | FAIL]
  -- PASS: not survey in aggregate
  -- FAIL: {entry, reason, revision}
```
*Forward-reader protocol (C-34): verifiable by token location.*

---

### Step 12 -- Production Chain Trace *(C-28; C-29; C-31)*

*(C-41: STEP-TIME AUTHORITY DECLARATION)*

```
STEP-TIME AUTHORITY RULE (C-41)
---------------------------------------------------------------------
This trace assembly step is CONFIRMATORY ONLY.

The canonical record for each node's chain position and role assignment is the step
header at which that node was declared during execution. This trace step confirms
what those declarations already established.

This step MUST NOT:
  - Define a node assignment not already in a step header
  - Renumber any node from its step-time assignment
  - Override, correct, or refine a step-header node declaration
  - Back-fill chain positions for steps that executed without inline node identity

If this trace disagrees with any step header, the step header governs.
Authority: step-execution time -> trace assembly time. Irreversible.
---------------------------------------------------------------------
```

```
PRODUCTION CHAIN TRACE
======================================================================

[NODE 1]  prediction sort -- IA+prior-frame-recovery (C-30+C-32), anti-hyp (C-11),
            destinations (C-14), discard log (C-09)
-> [NODE 2]  gate verdict -- Gatekeeper+dimension per stage (C-30+C-32), commits
               (C-13+C-16), gallery (C-18), cross-signal (C-08), floor (C-15)
-> [NODE 3]  triage -- simultaneous (C-23), failure-first (C-22)
-> [NODE 4]  echo entry -- IA+failure-projection (C-30+C-32); scaffold (C-17+C-21);
               failure-first (C-22); [CROSS] (C-08); failure field (C-18); impact (C-03)
-> [NODE 5]  synthesis -- IA+pattern-emergence (C-30+C-32); C-05
-> [NODE 6]  handover -- IA+future-framing (C-30+C-32); T-1..T-4 (C-19)
-> [NODE 7]  rules -- tier vs NODE 3 (C-24), orphan check
-> [NODE 8]  TRACE-CHECK-VERDICT [C-29; C-34]
-> [NODE 9]  gestalt audit -- complete artifact (C-26)
-> [NODE 10] GESTALT-VERDICT [C-29; C-34]
-> [NODE 11] chain trace (this) + C-41 authority declaration
-> [NODE 12] FLOOR-VERDICT [C-29; C-36; C-34; C-37: inline at Step 13]

======================================================================
CLOSURE CLAIM (C-38): No inter-criterion dependency is discoverable only by reading
the prompt. Known dependencies (7):
  C-23 -> C-24 (NODE 3 -> NODE 8)
  C-26 -> C-28 (NODE 9/10 -> NODE 11)
  C-24 -> C-28 (NODE 8 -> NODE 11)
  C-14 -> C-06 (NODE 4 -> NODE 6)
  C-17+C-21 -> C-20 (Step 5 -> Step 6)
  C-15 -> C-36 (NODE 2 -> NODE 12)
  C-36 -> C-28 (NODE 12 -> NODE 11)
```

---

### Dependency Closure Enumeration *(C-33)*

```
DEPENDENCY CLOSURE ENUMERATION
================================
CONTRACT HEADER: Any loop in chain trace but absent here is a C-33 violation. (C-39)

C-23 -> C-24 (NODE 3 -> NODE 8): triage rank feeds tier-match check
C-26 -> C-28 (NODE 9/10 -> NODE 11): gestalt verdict is named chain node
C-24 -> C-28 (NODE 8 -> NODE 11): traceability verdict is named chain node
C-14 -> C-06 (NODE 4 -> NODE 6): routing tags feed handover scenario
C-17+C-21 -> C-20 (Step 5 -> Step 6): naming scaffold feeds co-validation
C-15 -> C-36 (NODE 2 -> NODE 12): gate-time floor count feeds terminal check
C-36 -> C-28 (NODE 12 -> NODE 11): FLOOR-VERDICT is named chain node
================================
7 loops enumerated.
Any loop absent from this enumeration that appears in the chain trace is a C-33 violation.
(C-39 postamble)
```

---

**Output**: Steps 7-12 + Dependency Closure Enumeration + Step 13.

Final output sequence *(C-35)*:
1. Echo entries *(C-02; C-04; C-07; C-08; C-12; C-14; C-17; C-18; C-22)*
2. Cross-signal synthesis *(C-05)*
3. Forward handover guidance *(C-06; C-19)*
4. Rules of Thumb *(C-07; C-24)*
5. TRACE-CHECK-VERDICT *(C-24; C-29; C-34)*
6. GESTALT-VERDICT *(C-26; C-29; C-34)*
7. Chain trace (12 nodes) + C-41 authority declaration + REVIEWER CHALLENGE
   *(C-28; C-29; C-31; C-38; C-41)*
8. Dependency Closure Enumeration *(C-33; C-39)*
9. FLOOR-VERDICT *(C-36)*

### Step 13 -- Terminal Minimum Surprise Floor Check *(C-36)*

*(C-37: FLOOR-VERDICT is NODE 12. Inline declaration satisfies C-37.)*

```
FLOOR-VERDICT: [PASS | FLOOR-MISS]
  -- PASS: distinct surprise count >= 3 confirmed
  -- FLOOR-MISS: {count} surprises; shortfall: {3 - count}
```
*Forward-reader protocol (C-34): verifiable by FLOOR-VERDICT token location.*
*(C-36: Separate from gate-time floor check in Step 3 Stage 2.)*

---

## V-03 -- Combination: C-40 + C-41 with authority-embedded node template

**Variation axis:** Node declaration format that embeds step-time authority marker. Every
step header carries `[NODE N: {role} | step-time-canonical]`, making the authority claim
part of the declaration syntax. Steps 5 and 6 promoted to chain nodes (NODE 4, NODE 5).
14 nodes total. No dedicated AUTHORITY-VERDICT token (C-37 gap for this token).

**Hypothesis:** Embedding `| step-time-canonical` in the node declaration template is the
most compact C-41 form: the authority claim is visible at declaration time without a
separate preamble block at Step 12. This tests whether in-template markers satisfy C-41
structurally or whether a verifiable token is also required. C-41 compliance is not
verifiable by token location -- a reviewer must read chain trace entries to confirm no
override occurred. Predicted: C-40 PASS; C-41 PASS; C-37 PARTIAL (no dedicated
AUTHORITY-VERDICT token).

**Builds on:** R11 V-01 -- all 31 aspirational criteria (C-09..C-39) active.

---

### Prompt Body

You are running `/quest:topic echo` for the topic: {topic}.

All essential signals are in hand. Surface the genuine surprises -- findings only visible
in retrospect, from cross-signal tension, unpredictable before evidence gathering.

Not a summary. An echo: the signal that comes back that you didn't send.

---

**Node declaration format (C-40 + C-41 co-enforcement):**
Every step header carries: `[NODE N: {role} | step-time-canonical]`
The `| step-time-canonical` marker declares this step's node assignment authoritative as of
execution time. The terminal chain trace (Step 12) confirms; it does not define or override.

---

### Roles *(C-25; C-30; C-32)*

**Institutional Archaeologist (IA)** -- *First invocation: Step 2.*
Function: Recovers false assumptions. Frames surprises as corrections (C-17). Author of
implication. Sub-step shorthand: `IA: false-assumption-recovery; epistemic dimension: {name}`

| Step | Epistemic Dimension  |
|------|----------------------|
| 2    | prior-frame-recovery |
| 5    | belief-inversion     |
| 6    | correction-integrity |
| 7    | failure-projection   |
| 8    | pattern-emergence    |
| 9    | future-framing       |

**Gatekeeper** -- *First invocation: Step 3.*

```
GATEKEEPER -- FUNCTION DECLARATION (C-27)
Function:      Adversarial rejection -- predictability test + cross-signal requirement.
Not-function:  Future-reader framing (IA). Not-function: Thematic synthesis.
Role boundary: Verdicts final.
```

Shorthand: `Gatekeeper: adversarial-rejection-only; epistemic dimension: {label}`

---

### Step 1 *(C-10; C-12)* -- All namespaces. >=3. (Scaffolding -- not a chain node.)

### Step 2 -- [NODE 1: prediction sort | step-time-canonical]
*(IA: prior-frame-recovery; C-16; C-14; C-11; C-09)* -- Routes. Anti-hyp guard. Discard log.

### Step 3 -- [NODE 2: staged gate verdict | step-time-canonical]
*(Gatekeeper; C-13; C-15; C-16)*
Anti-Pattern Catalog: CONFIRMATION | RESTATEMENT | ISOLATED-FINDING
Gate: `VERDICT: SURPRISE | CUT -- {label}`
Stage 1 *(novelty)*. Stage 2 *(opposition)*: `We believed:` gallery; floor >=3.
Stage 3 *(specificity)*: cross-signal attribution.

### Step 4 -- [NODE 3: comparative triage rank | step-time-canonical]
*(C-23; C-22)* -- Comparative. HIGH | MEDIUM | LOW. Failure-first. All before expansion.

### Step 5 -- [NODE 4: naming scaffold | step-time-canonical]
*(C-17; C-21; IA: belief-inversion)* -- 1. Old belief. 2. Correction. 3. Domain. 4. Label.

### Step 6 -- [NODE 5: pre-expansion co-validation gate | step-time-canonical]
*(C-20; IA: correction-integrity)* -- Both VALID required. Blocking gate.

### Step 7 -- [NODE 6: echo entry | step-time-canonical]
*(IA: failure-projection; C-02..C-04; C-08; C-12; C-14; C-17; C-18; C-22)*
Begin from failure. Name, source, [CROSS], temporal, belief, surprise, mis-design, impact, route.

### Step 8 -- [NODE 7: cross-signal synthesis | step-time-canonical]
*(C-05; IA: pattern-emergence)* -- <=120 words. >=2 named labels. Cross-entry only.

### Step 9 -- [NODE 8: forward handover guidance | step-time-canonical]
*(C-06; C-19; IA: future-framing)* -- T-1..T-4. State selection. Verify slots.

### Step 10 -- [NODE 9: rules | step-time-canonical] + [NODE 10: TRACE-CHECK-VERDICT | step-time-canonical]
*(C-07; C-24)*

```
TRACE-CHECK-VERDICT: [PASS | FAIL]
  -- PASS: tiers match; no orphans; one-rule-per-surprise
  -- FAIL: {label | expected | actual}
```
*Forward-reader protocol (C-34): verifiable by token location.*

### Step 11 -- [NODE 11: gestalt audit | step-time-canonical] + [NODE 12: GESTALT-VERDICT | step-time-canonical]
*(C-26)*

```
GESTALT-VERDICT: [PASS | FAIL]
  -- PASS: not survey in aggregate
  -- FAIL: {entry, trigger, revision}
```
*Forward-reader protocol (C-34): verifiable by token location.*

---

### Step 12 -- [NODE 13: chain trace | step-time-canonical]
*(C-28; C-29; C-31)*

*(C-41 constraint: This trace confirms step-time declarations. The `| step-time-canonical`
marker in each header is authoritative. This step may not renumber, override, or back-fill.)*

```
CHAIN TRACE -- CONFIRMS STEP-TIME DECLARATIONS (C-41)
======================================================================
[NODE 1: prediction sort | step-time-canonical]
  confirms: IA+prior-frame-recovery (C-30+C-32), anti-hyp (C-11), destinations (C-14)

-> [NODE 2: gate verdict | step-time-canonical]
  confirms: Gatekeeper+dimension per stage (C-30+C-32), commits (C-13+C-16), floor (C-15)

-> [NODE 3: triage | step-time-canonical]
  confirms: simultaneous (C-23), failure-first (C-22)

-> [NODE 4: naming scaffold | step-time-canonical]
  confirms: IA+belief-inversion (C-30+C-32), 4-step (C-21), format (C-17)

-> [NODE 5: co-validation gate | step-time-canonical]
  confirms: IA+correction-integrity (C-30+C-32), both-VALID (C-20)

-> [NODE 6: echo entry | step-time-canonical]
  confirms: IA+failure-projection (C-30+C-32), failure-first (C-22), [CROSS] (C-08),
    failure field (C-18), impact (C-03)

-> [NODE 7: synthesis | step-time-canonical]
  confirms: IA+pattern-emergence (C-30+C-32), >=2 labels, cross-entry (C-05)

-> [NODE 8: handover | step-time-canonical]
  confirms: IA+future-framing (C-30+C-32), T-1..T-4 (C-19), slots (C-06)

-> [NODE 9: rules | step-time-canonical]
  confirms: tier vs NODE 3 (C-24), orphan check

-> [NODE 10: TRACE-CHECK-VERDICT | step-time-canonical]
  confirms: PASS|FAIL token with forward-reader protocol (C-34)

-> [NODE 11: gestalt audit | step-time-canonical]
  confirms: complete artifact (C-26)

-> [NODE 12: GESTALT-VERDICT | step-time-canonical]
  confirms: PASS|FAIL token with forward-reader protocol (C-34)

-> [NODE 13: chain trace (this) | step-time-canonical]
  confirms: 14 nodes (C-28), verification nodes (C-29), deps (C-31), C-41 constraint

-> [NODE 14: FLOOR-VERDICT | step-time-canonical]
  confirms: PASS|FLOOR-MISS; separate (C-36); forward-reader (C-34)

======================================================================
CLOSURE CLAIM (C-38): No inter-criterion dependency is discoverable only by reading
the prompt. Known dependencies (7):
  C-23 -> C-24 (NODE 3 -> NODE 10)
  C-26 -> C-28 (NODE 11/12 -> NODE 13)
  C-24 -> C-28 (NODE 10 -> NODE 13)
  C-14 -> C-06 (NODE 6 -> NODE 8)
  C-17+C-21 -> C-20 (NODE 4 -> NODE 5)
  C-15 -> C-36 (NODE 2 -> NODE 14)
  C-36 -> C-28 (NODE 14 -> NODE 13)
```

---

### Dependency Closure Enumeration *(C-33)*

```
DEPENDENCY CLOSURE ENUMERATION
================================
CONTRACT HEADER: Any loop in chain trace but absent here is a C-33 violation. (C-39)

C-23 -> C-24 (NODE 3 -> NODE 10): triage rank feeds tier-match check
C-26 -> C-28 (NODE 11/12 -> NODE 13): gestalt verdict is named chain node
C-24 -> C-28 (NODE 10 -> NODE 13): traceability verdict is named chain node
C-14 -> C-06 (NODE 6 -> NODE 8): routing tags feed handover scenario
C-17+C-21 -> C-20 (NODE 4 -> NODE 5): naming scaffold feeds co-validation
C-15 -> C-36 (NODE 2 -> NODE 14): gate-time floor count feeds terminal check
C-36 -> C-28 (NODE 14 -> NODE 13): FLOOR-VERDICT is named chain node
================================
7 loops enumerated.
Any loop absent from this enumeration that appears in the chain trace is a C-33 violation.
(C-39 postamble)
```

---

**Output**: Steps 7-12 + Dependency Closure Enumeration + Step 13.

Final output sequence *(C-35)*:
1. Echo entries *(C-02; C-04; C-07; C-08; C-12; C-14; C-17; C-18; C-22)*
2. Cross-signal synthesis *(C-05)*
3. Forward handover guidance *(C-06; C-19)*
4. Rules of Thumb *(C-07; C-24)*
5. TRACE-CHECK-VERDICT *(C-24; C-29; C-34)*
6. GESTALT-VERDICT *(C-26; C-29; C-34)*
7. Chain trace (14 nodes, C-41 constraint) *(C-28; C-29; C-31; C-38; C-40; C-41)*
8. Dependency Closure Enumeration *(C-33; C-39)*
9. FLOOR-VERDICT *(C-36)*

### Step 13 -- [NODE 14: FLOOR-VERDICT | step-time-canonical]

*(C-37: FLOOR-VERDICT is NODE 14. Inline declaration satisfies C-37.)*

```
FLOOR-VERDICT: [PASS | FLOOR-MISS]
  -- PASS: distinct surprise count >= 3 confirmed
  -- FLOOR-MISS: {count} surprises; shortfall: {3 - count}
```
*Forward-reader protocol (C-34): verifiable by FLOOR-VERDICT token location.*
*(C-36: Separate from gate-time floor check in Step 3 Stage 2.)*

---

## V-04 -- C-41 with named BACK-FILL-GUARD and BACK-FILL-VERDICT token

**Variation axis:** Anti-pattern naming + dedicated verification token for back-fill
detection. The back-fill failure mode is named explicitly at the trace assembly step with
its own detection protocol and BACK-FILL-VERDICT token. C-40 is NOT addressed (only Step
13 carries inline NODE via C-37; no universal headers on intermediate steps).

**Hypothesis:** Naming "back-fill" as a specific, detectable anti-pattern with a VERDICT
token makes C-41 violations auditable by token location without session replay -- parallel
to how FLOOR-VERDICT makes floor violations detectable. The key question: does a
detection-oriented approach (BACK-FILL-VERDICT verifies no violation) satisfy C-41 as well
as a prohibition-oriented approach? C-40 is absent: universal headers would prevent back-fill
architecturally; the BACK-FILL-GUARD detects it epistemically. Predicted: C-40 FAIL; C-41
PASS; C-37 PARTIAL (BACK-FILL-VERDICT introduced but no inline NODE declaration at its
governing sub-step per C-37).

**Builds on:** R11 V-01 -- all 31 aspirational criteria (C-09..C-39) active.

---

### Prompt Body

You are running `/quest:topic echo` for the topic: {topic}.

All essential signals are in hand. Surface the genuine surprises -- findings only visible
in retrospect, from cross-signal tension, unpredictable before evidence gathering.

Not a summary. An echo: the signal that comes back that you didn't send.

---

**THE BACK-FILL ANTI-PATTERN (C-41)**

Back-fill: the trace assembly step defines or renumbers node assignments that should have
been canonical in step headers. Back-fill converts step-time declarations into anticipatory
drafts -- the terminal trace becomes definitional rather than confirmatory. Back-fill is
structurally invisible: a well-formed trace looks identical whether nodes were declared at
step-time or assigned retroactively. The BACK-FILL-GUARD below closes this gap.

---

### Roles *(C-25; C-30; C-32)*

**Institutional Archaeologist (IA)** -- *First invocation: Step 2.*
Function: Recovers false assumptions. Frames surprises as corrections (C-17). Author of
implication. Sub-step shorthand: `IA: false-assumption-recovery; epistemic dimension: {name}`

| Step | Epistemic Dimension  |
|------|----------------------|
| 2    | prior-frame-recovery |
| 5    | belief-inversion     |
| 6    | correction-integrity |
| 7    | failure-projection   |
| 8    | pattern-emergence    |
| 9    | future-framing       |

**Gatekeeper** -- *First invocation: Step 3.*

```
GATEKEEPER -- FUNCTION DECLARATION (C-27)
Function:      Adversarial rejection -- predictability test + cross-signal requirement.
Not-function:  Future-reader framing (IA). Not-function: Thematic synthesis.
Role boundary: Verdicts final.
```

Shorthand: `Gatekeeper: adversarial-rejection-only; epistemic dimension: {label}`

---

### Step 1 *(C-10; C-12)* -- All namespaces. >=3. Record.

### Step 2 *(IA: prior-frame-recovery; C-16; C-14; C-11; C-09)* -- Routes. Discard log.

### Step 3 *(Gatekeeper; C-13; C-15; C-16)*
Anti-Pattern Catalog: CONFIRMATION | RESTATEMENT | ISOLATED-FINDING
Gate: `VERDICT: SURPRISE | CUT -- {label}`
Stage 1 *(novelty)*. Stage 2 *(opposition)*: floor >=3. Stage 3 *(specificity)*: attribution.

### Step 4 *(C-23; C-22)* -- Triage. Failure-first. All before expansion.

### Step 5 *(C-17; C-21; IA: belief-inversion)* -- 4-step naming scaffold.

### Step 6 *(C-20; IA: correction-integrity)* -- Co-validation. Both VALID required.

### Step 7 *(IA: failure-projection; C-02..C-04; C-08; C-12; C-14; C-17; C-18; C-22)*
Begin from failure. Name, source, [CROSS], temporal, belief, surprise, mis-design, impact, route.

### Step 8 *(C-05; IA: pattern-emergence)* -- <=120 words. >=2 named labels.

### Step 9 *(C-06; C-19; IA: future-framing)* -- T-1..T-4. State selection. Verify.

### Step 10 *(C-07; C-24)*

```
TRACE-CHECK-VERDICT: [PASS | FAIL]
  -- PASS: tiers match; no orphans; one-rule-per-surprise
  -- FAIL: {label | expected | actual}
```
*Forward-reader protocol (C-34): verifiable by token location.*

### Step 11 *(C-26)*

```
GESTALT-VERDICT: [PASS | FAIL]
  -- PASS: not survey in aggregate
  -- FAIL: {entry, trigger, revision}
```
*Forward-reader protocol (C-34): verifiable by token location.*

---

### Step 12 -- Production Chain Trace + BACK-FILL-GUARD *(C-28; C-29; C-31; C-41)*

```
PRODUCTION CHAIN TRACE
======================================================================

[NODE 1]  prediction sort -- IA+prior-frame-recovery (C-30+C-32), anti-hyp (C-11),
            destinations (C-14), discard log (C-09)
-> [NODE 2]  gate verdict -- Gatekeeper+dimension per stage (C-30+C-32), commits
               (C-13+C-16), gallery (C-18), cross-signal (C-08), floor (C-15)
-> [NODE 3]  triage -- simultaneous (C-23), failure-first (C-22)
-> [NODE 4]  echo entry -- IA+failure-projection (C-30+C-32); scaffold (C-17+C-21);
               failure-first (C-22); [CROSS] (C-08); failure field (C-18); impact (C-03)
-> [NODE 5]  synthesis -- IA+pattern-emergence (C-30+C-32); C-05
-> [NODE 6]  handover -- IA+future-framing (C-30+C-32); T-1..T-4 (C-19)
-> [NODE 7]  rules -- tier vs NODE 3 (C-24), orphan check
-> [NODE 8]  TRACE-CHECK-VERDICT [C-29; C-34]
-> [NODE 9]  gestalt audit -- complete artifact (C-26)
-> [NODE 10] GESTALT-VERDICT [C-29; C-34]
-> [NODE 11] chain trace (this)
-> [NODE 12] FLOOR-VERDICT [C-29; C-36; C-34; C-37: inline at Step 13]

======================================================================
CLOSURE CLAIM (C-38): No inter-criterion dependency is discoverable only by reading
the prompt. Known dependencies (7):
  C-23 -> C-24 (NODE 3 -> NODE 8)
  C-26 -> C-28 (NODE 9/10 -> NODE 11)
  C-24 -> C-28 (NODE 8 -> NODE 11)
  C-14 -> C-06 (NODE 4 -> NODE 6)
  C-17+C-21 -> C-20 (Step 5 -> Step 6)
  C-15 -> C-36 (NODE 2 -> NODE 12)
  C-36 -> C-28 (NODE 12 -> NODE 11)
```

**BACK-FILL-GUARD (C-41)**

*Review each NODE entry. For every node, verify the role assignment in the trace was
declared in a step header during execution -- not assigned for the first time here.*

```
BACK-FILL-VERDICT: [CLEAN | BACK-FILL-DETECTED]
  -- CLEAN: all trace entries confirm step-time declarations; no node back-filled,
     renumbered, or role-assigned for the first time at trace assembly; step headers
     are canonical; this trace is the confirmation record
  -- BACK-FILL-DETECTED: {NODE N: step header declared role X (or: no declaration);
     trace assigns role Y; back-fill confirmed; C-41 violation}
```

*Forward-reader protocol (C-34): A future reader verifies C-41 compliance by locating the
BACK-FILL-VERDICT token -- no session replay required. CLEAN certifies all trace entries are
confirmatory only.*

---

### Dependency Closure Enumeration *(C-33)*

```
DEPENDENCY CLOSURE ENUMERATION
================================
CONTRACT HEADER: Any loop in chain trace but absent here is a C-33 violation. (C-39)

C-23 -> C-24 (NODE 3 -> NODE 8): triage rank feeds tier-match check
C-26 -> C-28 (NODE 9/10 -> NODE 11): gestalt verdict is named chain node
C-24 -> C-28 (NODE 8 -> NODE 11): traceability verdict is named chain node
C-14 -> C-06 (NODE 4 -> NODE 6): routing tags feed handover scenario
C-17+C-21 -> C-20 (Step 5 -> Step 6): naming scaffold feeds co-validation
C-15 -> C-36 (NODE 2 -> NODE 12): gate-time floor count feeds terminal check
C-36 -> C-28 (NODE 12 -> NODE 11): FLOOR-VERDICT is named chain node
================================
7 loops enumerated.
Any loop absent from this enumeration that appears in the chain trace is a C-33 violation.
(C-39 postamble)
```

---

**Output**: Steps 7-12 + Dependency Closure Enumeration + Step 13.

Final output sequence *(C-35)*:
1. Echo entries *(C-02; C-04; C-07; C-08; C-12; C-14; C-17; C-18; C-22)*
2. Cross-signal synthesis *(C-05)*
3. Forward handover guidance *(C-06; C-19)*
4. Rules of Thumb *(C-07; C-24)*
5. TRACE-CHECK-VERDICT *(C-24; C-29; C-34)*
6. GESTALT-VERDICT *(C-26; C-29; C-34)*
7. Chain trace (12 nodes) + BACK-FILL-VERDICT + REVIEWER CHALLENGE
   *(C-28; C-29; C-31; C-38; C-41)*
8. Dependency Closure Enumeration *(C-33; C-39)*
9. FLOOR-VERDICT *(C-36)*

### Step 13 -- Terminal Minimum Surprise Floor Check *(C-36)*

*(C-37: FLOOR-VERDICT is NODE 12. Inline declaration satisfies C-37.)*

```
FLOOR-VERDICT: [PASS | FLOOR-MISS]
  -- PASS: distinct surprise count >= 3 confirmed
  -- FLOOR-MISS: {count} surprises; shortfall: {3 - count}
```
*Forward-reader protocol (C-34): verifiable by FLOOR-VERDICT token location.*
*(C-36: Separate from gate-time floor check in Step 3 Stage 2.)*

---

## V-05 -- Full synthesis: C-40 + C-41 + AUTHORITY-VERDICT + 9-loop dep closure

**Variation axis:** Complete integration of C-40 and C-41 with maximum structural
verifiability. Universal `[NODE N: {role}]` at every step header (C-40). Explicit step-time
authority declaration at trace assembly step with AUTHORITY-VERDICT as NODE 14 (C-41 + C-37
for this token). Steps 5 and 6 promoted to chain nodes. 15 nodes total. Dep closure updated
with 9 loops: 7 inherited from R11 + C-40->C-41 + C-41->C-28.

**Hypothesis:** The V-01 vs V-05 delta from R11 repeats here at the C-40/C-41 level. V-01
satisfies C-40 architecturally but leaves C-41 open. V-02 declares C-41 but without
universal headers to protect. V-03 embeds the authority marker but lacks a verifiable token.
V-04 provides the token but lacks universal coverage. V-05 closes all four gaps: universal
headers make back-fill architecturally impossible (C-40); the authority declaration makes
it epistemically prohibited (C-41); the AUTHORITY-VERDICT token makes compliance verifiable
by location (C-41+C-34); and its inline NODE declaration at the governing sub-step closes
the C-37 gap for this new token. Dep closure update makes the C-40->C-41 structural
dependency auditable (C-31+C-33). Predicted: C-40 PASS; C-41 PASS; C-37 PASS for
AUTHORITY-VERDICT; all C-09..C-41.

**Builds on:** R11 V-01 -- all 31 aspirational criteria (C-09..C-39) active. Extends to C-41.

---

### Prompt Body

You are running `/quest:topic echo` for the topic: {topic}.

All essential signals are in hand. Your task: surface the genuine surprises -- findings
that only became visible in retrospect, from cross-signal tension, that no competent
practitioner would have predicted before gathering evidence.

Not a summary. Not a survey of discoveries. An echo: the signal that comes back that you
didn't send.

---

### Roles *(C-25; C-30; C-32)*

**Institutional Archaeologist (IA)**
*First invocation: Step 2.*
Function: Recovers false assumptions embedded in current materials -- what a future team
would carry as truth without knowing otherwise. Frames every surprise as a correction to a
false assumption (C-17). Derives consequence by asking "What would the next team build
wrong?" (C-18, C-22). The IA is the author of implication; the Gatekeeper is the author
of rejection.

Sub-step co-activation shorthand *(C-30, C-32)*: `IA: false-assumption-recovery;
epistemic dimension: {name}` at every invocation.

| Step | Epistemic Dimension    | Why here                                              |
|------|------------------------|-------------------------------------------------------|
| 2    | prior-frame-recovery   | Recovering what was actually believed, not spec text  |
| 5    | belief-inversion       | Deriving correction-encoding name by inverting belief |
| 6    | correction-integrity   | Verifying both form checks encode the correction      |
| 7    | failure-projection     | Anchoring entry in projected mis-design               |
| 8    | pattern-emergence      | What only emerges when entries are read together      |
| 9    | future-framing         | Translating findings to guidance for future builder   |

Active: Steps 2, 5, 6, 7, 8, 9.

**Gatekeeper**
*First invocation: Step 3.*
Shorthand: `Gatekeeper: adversarial-rejection-only; epistemic dimension: {stage-label}`

```
GATEKEEPER -- FUNCTION DECLARATION (C-27)
---------------------------------------------------------------------
Function:      Adversarial rejection. Tests each candidate: (1) first-principles
               predictability; (2) cross-signal requirement. Fails either: rejected.
Not-function:  Future-reader framing (IA's domain).
Not-function:  Thematic synthesis (evaluates candidates in isolation).
Role boundary: Gatekeeper verdicts are final.
---------------------------------------------------------------------
```

Active: Step 3 only.

---

### Step 1 -- Read Signal Record *(C-10; C-12)*

All namespaces (scout, draft, review, flow, trace, prove, listen, program, topic).
Record: namespaces covered (>=3 floor), total artifacts, date range.
Step 1 is scaffolding; it does not enter the production chain.

---

### Step 2 -- [NODE 1: typed-route prediction sort] *(C-40)*
*(IA: false-assumption-recovery; epistemic dimension: prior-frame-recovery; C-16; C-14;
C-11; C-09)*

Routes: `topic-story` | `topic-report` | `gate-pipeline`
Anti-hypothesis guard *(C-11)*: "Confirms investigation hypothesis?" YES -> `topic-story`.
Discard log *(C-09)*: every non-gate item, route type, reason (1 sentence). Non-empty required.

---

### Step 3 -- [NODE 2: staged gate verdict] *(C-40)*
*(Gatekeeper: adversarial-rejection-only; C-13; C-15; C-16)*

Anti-Pattern Catalog *(C-13)*: CONFIRMATION | RESTATEMENT | ISOLATED-FINDING
Gate format *(C-16)*: `VERDICT: SURPRISE | CUT -- {label}`

**Stage 1 -- Prediction Test** *(epistemic dimension: novelty)*
"Would a competent practitioner have predicted this from first principles?"
`PREDICTABLE` -> `topic-story` | `UNPREDICTABLE` -> Stage 2
Commit: `Stage 1: [{item}] -> [PREDICTABLE | UNPREDICTABLE]`

**Stage 2 -- Contradiction Test** *(epistemic dimension: opposition)*
```
We believed: {falsifiable assumption}
VALID: {genuine falsification}
INVALID (absence-of-consideration) | INVALID (sentiment-reaction) | INVALID (hedge-uncertainty)
```
Floor *(C-15)*: >=3 CONTRADICTION FOUND.
Commit: `Stage 2: [{item}] -> [NO CONTRADICTION | CONTRADICTION FOUND]`

**Stage 3 -- Attribution Test** *(epistemic dimension: specificity)*
"Does this finding emerge only when >=2 signal artifacts are read together?"
`SINGLE-ARTIFACT` -> `topic-report` | `CROSS-SIGNAL` -> SURPRISE
Commit: `Stage 3: [{item}] -> [SINGLE-ARTIFACT | CROSS-SIGNAL] -- sources: [{a1}, {a2}]`

---

### Step 4 -- [NODE 3: comparative triage rank] *(C-40)*
*(C-23; C-22)*

Comparative. HIGH | MEDIUM | LOW. Failure-first within tier. All before expansion.

---

### Step 5 -- [NODE 4: naming scaffold] *(C-40)*
*(C-17; C-21; IA: false-assumption-recovery; epistemic dimension: belief-inversion)*

1. Old belief. 2. Correction. 3. Domain. 4. Form: `The {Corrected Belief}: {Domain}`.
VALID: "The Silent Veto: Adoption Workflow". INVALID: "Surprising Finding About Adoption".

---

### Step 6 -- [NODE 5: pre-expansion co-validation gate] *(C-40)*
*(C-20; IA: false-assumption-recovery; epistemic dimension: correction-integrity)*

Both VALID required. Either failing blocks expansion.
- Name form *(C-17)*: `The {Corrected Belief}: {Domain}`? -> VALID / INVALID
- Failure field *(C-18)*: "If next team carries old assumption, {specific mis-design}"? -> VALID / INVALID

---

### Step 7 -- [NODE 6: echo entry] *(C-40)*
*(IA: false-assumption-recovery; epistemic dimension: failure-projection; C-02..C-04;
C-08; C-12; C-14; C-17; C-18; C-22)*

Begin from failure *(C-22)*: anchor the mis-design first.

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

### Step 8 -- [NODE 7: cross-signal synthesis] *(C-40)*
*(C-05; IA: false-assumption-recovery; epistemic dimension: pattern-emergence)*

<=120 words. Name >=2 entries by exact label. Cross-entry pattern only.

---

### Step 9 -- [NODE 8: forward handover guidance] *(C-40)*
*(C-06; C-19; IA: false-assumption-recovery; epistemic dimension: future-framing)*

T-1..T-4 register. State selection. Verify slots. Scenario and constraint specific.

---

### Step 10 -- [NODE 9: impact-anchored rule] + [NODE 10: TRACE-CHECK-VERDICT] *(C-40)*
*(C-07; C-24)*

<=3 rules. HIGH/MEDIUM only. Tier-match, no orphans, one-rule-per-surprise.

```
TRACE-CHECK-VERDICT: [PASS | FAIL]
  -- PASS: all tiers match; no orphan rules; one-rule-per-surprise confirmed
  -- FAIL: {rule label | expected tier from Step 4 | actual tier in entry}
```
*Forward-reader protocol (C-34): verifiable by TRACE-CHECK-VERDICT token location.*

---

### Step 11 -- [NODE 11: gestalt audit] + [NODE 12: GESTALT-VERDICT] *(C-40)*
*(C-26)*

"Could this output be described as a summary or survey?" If YES: revise, log gestalt-summary-fail.

```
GESTALT-VERDICT: [PASS | FAIL]
  -- PASS: output does not read as survey in aggregate; every entry retroactively-visible
  -- FAIL: {entry label, gestalt-summary-fail trigger, revision applied}
```
*Forward-reader protocol (C-34): verifiable by GESTALT-VERDICT token location.*

---

### Step 12 -- [NODE 13: production chain trace] *(C-40)*
*(C-28; C-29; C-31)*

*(C-37: AUTHORITY-VERDICT is NODE 14 in the production chain. A model executing this step
in isolation sees AUTHORITY-VERDICT's node identity without consulting the terminal chain
trace. This inline declaration satisfies C-37 for AUTHORITY-VERDICT.)*

*(C-41: STEP-TIME AUTHORITY DECLARATION. This trace assembly step is CONFIRMATORY ONLY.
The step header at which each node was declared during execution is the canonical record.
This step confirms those declarations. This step MUST NOT define, renumber, back-fill, or
override any step-time node assignment. If this trace disagrees with any step header, the
step header governs. Authority: step-execution time -> trace assembly time. Irreversible.)*

```
PRODUCTION CHAIN TRACE
VERIFICATION NODES INCLUDED (C-29) | DEPENDENCY GRAPH CLOSED (C-31)
======================================================================

[NODE 1]  typed-route prediction sort
  structural qualifier: IA+prior-frame-recovery (C-30+C-32), anti-hyp guard (C-11),
    typed destinations (C-14), non-empty discard log (C-09)
  produces: typed routes, discard log
  consumed by: NODE 2

-> [NODE 2]  staged gate verdict
  structural qualifier: Gatekeeper+dimension per stage (C-30+C-32), commit tokens
    (C-13+C-16), "We believed:" gallery Stage 2 (C-18), cross-signal Stage 3 (C-08 prereq),
    gate-time floor count (C-15)
  produces: SURPRISE verdicts, gate-time floor count
  consumed by: NODE 3, NODE 15 (floor count for C-36)

-> [NODE 3]  comparative triage rank
  structural qualifier: simultaneous comparison (C-23), failure-first (C-22)
  produces: HIGH/MEDIUM/LOW assignments, within-tier order
  consumed by: NODE 6 entry headers (C-07), NODE 10 TRACE-CHECK-VERDICT (C-24)

-> [NODE 4]  naming scaffold [C-40: universal declaration -- promoted]
  structural qualifier: IA+belief-inversion (C-30+C-32); 4-step derivation (C-21);
    correction-encoding format (C-17)
  produces: correction-encoding name (C-17+C-21)
  consumed by: NODE 5

-> [NODE 5]  pre-expansion co-validation gate [C-40: universal declaration -- promoted]
  structural qualifier: IA+correction-integrity (C-30+C-32); both-VALID required (C-20);
    blocking gate
  produces: co-validated name + failure field pair (C-20)
  consumed by: NODE 6

-> [NODE 6]  echo entry
  structural qualifier: IA+failure-projection (C-30+C-32); scaffold from NODE 4 (C-17+C-21);
    failure-first (C-22); [CROSS] (C-08); failure field (C-18); impact (C-03)
  produces: named labels (C-04), citations (C-02), impact (C-03), routes (C-14)
  consumed by: NODE 7, NODE 8, NODE 9, NODE 15 (final surprise count)

-> [NODE 7]  cross-signal synthesis
  structural qualifier: IA+pattern-emergence (C-30+C-32); >=2 labels; cross-entry (C-05)
  produces: synthesized echo paragraph (C-05)

-> [NODE 8]  forward handover guidance
  structural qualifier: IA+future-framing (C-30+C-32); T-1..T-4 (C-19); slots (C-06)
  produces: register-anchored handoff (C-06+C-19)

-> [NODE 9]  impact-anchored rule
  structural qualifier: tier vs NODE 3 (C-24), orphan check, one-rule-per-surprise
  consumed by: NODE 10

-> [NODE 10] TRACE-CHECK-VERDICT [C-29: chain node; C-34: forward-reader protocol inline]
  structural qualifier: PASS|FAIL token; mismatches by label if FAIL
  produces: traceability audit result (C-24+C-29+C-34)
  consumed by: NODE 13

-> [NODE 11] gestalt audit
  structural qualifier: IA+complete artifact as unit (C-26+C-30)
  produces: gestalt audit result (C-26)
  consumed by: NODE 12

-> [NODE 12] GESTALT-VERDICT [C-29: chain node; C-34: forward-reader protocol inline]
  structural qualifier: PASS|FAIL token; distinct scope from NODE 10
  produces: gestalt audit result (C-26+C-29+C-34)
  consumed by: NODE 13

-> [NODE 13] production chain trace (this node)
  structural qualifier: all 15 nodes named with qualifiers (C-28); all verification tokens
    are chain nodes (C-29); all 9 inter-criterion deps annotated (C-31); C-41 authority
    declaration (above); C-40 universal coverage confirmed
  produces: closed, auditable dependency graph

-> [NODE 14] AUTHORITY-VERDICT [C-29: chain node; C-41: step-time authority verification;
  C-34: forward-reader protocol inline; C-37: inline node declared at governing step above]
  structural qualifier: PASS|FAIL token; verifies no back-fill, renumber, or override at
    NODE 13 trace assembly; verifiable by token location; FAIL records each violation
  produces: step-time authority compliance result (C-41+C-29+C-34+C-37)
  consumed by: output; closes C-41 -> C-28 loop (NODE 14 named in NODE 13)

-> [NODE 15] FLOOR-VERDICT [C-29: chain node; C-36: terminal floor check;
  C-34: forward-reader protocol inline; C-37: inline node declared at Step 13]
  structural qualifier: PASS|FLOOR-MISS token; separate from gate-time floor in NODE 2
  produces: terminal floor compliance result (C-36)
  consumed by: output; closes C-15 -> C-36 (NODE 2 -> NODE 15) loop

======================================================================
CLOSURE CLAIM (C-38): No inter-criterion dependency is discoverable only by reading
the prompt. Known dependencies (9):
  C-23 -> C-24 (NODE 3 -> NODE 10)
  C-26 -> C-28 (NODE 11/12 -> NODE 13)
  C-24 -> C-28 (NODE 10 -> NODE 13)
  C-14 -> C-06 (NODE 6 -> NODE 8)
  C-17+C-21 -> C-20 (NODE 4 -> NODE 5)
  C-15 -> C-36 (NODE 2 -> NODE 15)
  C-36 -> C-28 (NODE 15 -> NODE 13)
  C-40 -> C-41 (NODEs 1-15 universal headers -> NODE 14 AUTHORITY-VERDICT):
    universal step-time declarations are the structural precondition for step-time authority;
    AUTHORITY-VERDICT can only verify what step headers declared
  C-41 -> C-28 (NODE 14 -> NODE 13): AUTHORITY-VERDICT is a named chain node; NODE 13
    must name NODE 14 to satisfy C-28 for this verification token
Attempt to falsify by reading the full prompt.
```

---

### AUTHORITY-VERDICT sub-step *(Step 12 continuation)*

*(C-37: AUTHORITY-VERDICT is NODE 14. Declaration at governing step above satisfies C-37.)*

Review each NODE 1-15 entry. Verify the role assignment in the trace confirms what was
declared in that step's header at execution time.

```
AUTHORITY-VERDICT: [CONFIRMATORY | OVERRIDE-DETECTED]
  -- CONFIRMATORY: all 15 trace entries confirm step-time declarations; no node was
     renumbered, back-filled, or role-assigned for the first time at trace assembly;
     step headers are canonical; this trace is the confirmation record only
  -- OVERRIDE-DETECTED: {NODE N: step header declared role X (or: no declaration);
     trace assigns role Y; back-fill or override confirmed; C-41 violation}
```

*Forward-reader protocol (C-34): A future reader verifies C-41 compliance by locating the
AUTHORITY-VERDICT token -- no session replay required. CONFIRMATORY certifies step headers
are canonical and this trace confirms rather than defines. OVERRIDE-DETECTED certifies each
violation by node number, step-header declaration, and trace assignment.*

*(C-41: This token is the verifiable output of the step-time authority declaration. Step
headers govern when disagreement exists; this token cannot correct step headers.)*

---

### Dependency Closure Enumeration *(C-33)*

*Standalone terminal block, separate from and after the chain trace.*

```
DEPENDENCY CLOSURE ENUMERATION
================================
CONTRACT HEADER: Any loop in chain trace but absent here is a C-33 violation. (C-39)

C-23 -> C-24 (NODE 3 -> NODE 10):
  triage rank (NODE 3) required input for tier-match check (NODE 10)

C-26 -> C-28 (NODE 11/12 -> NODE 13):
  gestalt audit verdict (NODE 12) is named chain node in NODE 13

C-24 -> C-28 (NODE 10 -> NODE 13):
  traceability verdict (NODE 10) is named chain node in NODE 13

C-14 -> C-06 (NODE 6 -> NODE 8):
  routing tags in entries (NODE 6) feed handover scenario selection (NODE 8)

C-17+C-21 -> C-20 (NODE 4 -> NODE 5):
  naming scaffold output (NODE 4) is input to co-validation name-form check (NODE 5)

C-15 -> C-36 (NODE 2 -> NODE 15):
  gate-time floor count (NODE 2) compared against final surprise count at NODE 15

C-36 -> C-28 (NODE 15 -> NODE 13):
  FLOOR-VERDICT (NODE 15) is named chain node; NODE 13 must name NODE 15

C-40 -> C-41 (NODEs 1-15 -> NODE 14):
  universal step-header declarations (C-40) are the structural precondition for step-time
  authority (C-41); AUTHORITY-VERDICT (NODE 14) verifies what universal declarations
  established; C-41 is only auditable when C-40 declarations exist to compare against

C-41 -> C-28 (NODE 14 -> NODE 13):
  AUTHORITY-VERDICT (NODE 14) is a named chain node; NODE 13 must name NODE 14 to
  satisfy C-28 for this verification token
================================
9 loops enumerated.
Any loop absent from this enumeration that appears in the chain trace is a C-33 violation.
(C-39 postamble)
```

---

**Output**: Steps 7-12 (including AUTHORITY-VERDICT sub-step) + Dependency Closure
Enumeration + Step 13.

Final output sequence *(C-35)*:
1. Echo entries *(C-02; C-04; C-07; C-08; C-12; C-14; C-17; C-18; C-22)*
2. Cross-signal synthesis *(C-05)*
3. Forward handover guidance *(C-06; C-19)*
4. Rules of Thumb *(C-07; C-24)*
5. TRACE-CHECK-VERDICT *(C-24; C-29; C-34)*
6. GESTALT-VERDICT *(C-26; C-29; C-34)*
7. Production chain trace (15 nodes) + C-41 authority declaration + REVIEWER CHALLENGE
   *(C-28; C-29; C-31; C-38; C-40; C-41)*
8. AUTHORITY-VERDICT with forward-reader protocol *(C-41; C-29; C-34; C-37)*
9. Dependency Closure Enumeration (9 loops) *(C-33; C-39)*
10. FLOOR-VERDICT *(C-36)*

### Step 13 -- [NODE 15: FLOOR-VERDICT] *(C-40)*

*(C-37: FLOOR-VERDICT is NODE 15. Inline declaration satisfies C-37.)*

Count distinct surprises in final output (Item 1 entries). Compare to floor (3).

```
FLOOR-VERDICT: [PASS | FLOOR-MISS]
  -- PASS: distinct surprise count >= 3 confirmed in final output
  -- FLOOR-MISS: {count} surprises present; floor shortfall: {3 - count} required
```

FLOOR-MISS is a named output artifact. Do not suppress it.

*Forward-reader protocol (C-34): verifiable by FLOOR-VERDICT token location. PASS certifies
final output contains >=3 distinct surprises after all post-gate revisions.*

*(C-36: Separate from gate-time floor check in Step 3 Stage 2.)*
