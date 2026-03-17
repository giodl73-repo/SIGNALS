---
skill: quest-variate
skill_target: topic-echo
date: 2026-03-15
round: 11
rubric: v11
rubric_max: 174
---

# Variations: `topic:echo` -- Round 11

**Rubric:** v11 | **Date:** 2026-03-15

---

## Design Context

R10 differentiating evidence: three structural patterns from R10 V-05 were observable but
not yet formalized as criteria.

1. **R10 V-05 inline-node gap (-> C-37)**: R10 V-05 added NODE 12 (FLOOR-VERDICT) to the
   production chain trace in Step 12. But Step 13 -- the governing step that introduces
   and defines FLOOR-VERDICT -- carried no inline node assignment. A model executing
   Step 13 in isolation sees the token but not its chain-node identity. The NODE assignment
   appeared only when the terminal chain trace was assembled, leaving a step-local gap.
   C-37 closes this: any named verification token introduced by a governing step is assigned
   its chain-node number inline at the point of introduction, not back-filled at trace time.

2. **R10 V-04 closure-claim gap (-> C-38)**: R10 V-04 enumerated 5 inter-criterion loops in
   the dependency closure section but made no completeness assertion. R10 V-05 extended to 7
   loops and added: "No inter-criterion dependency is discoverable only by reading the
   prompt." That line converts the dep graph from a list into an audit target -- a reviewer
   can attempt to falsify the claim by finding a missing dependency. C-38 formalizes this:
   the chain trace must close with a machine-checkable completeness claim that invites
   falsification.

3. **R10 V-04 enumeration-guard gap (-> C-39)**: R10 V-04's dep enumeration listed 5 loops
   with no mechanism to detect its own incompleteness. R10 V-05 appended: "Any loop absent
   from this enumeration that appears in the chain trace is a C-33 violation." C-39
   formalizes this: the terminal enumeration block carries its own self-referential gap-
   detection guard, enabling a reviewer to audit the enumeration in isolation.

**Variation plan:**

- V-01: C-37 only -- inline NODE 12 declaration in Step 13; C-38/C-39 at R10 V-05 state
- V-02: C-38 only -- challenge-prefix closure claim; C-37/C-39 at R10 V-05 state
- V-03: C-39 only -- bidirectional guard (preamble + postamble); C-37/C-38 at R10 V-05 state
- V-04: C-38 + C-39 in conversational register + inertia framing; C-37 PARTIAL (no inline node)
- V-05: Full synthesis -- C-37 generalized to all steps (universal inline-node declaration) +
  challenge-format C-38 + bidirectional C-39; complete closure of all three gaps

**Discriminating pairs:**
- V-01 vs V-05: C-37 both PASS; C-38/C-39 both PASS; V-05 generalizes C-37 universally
- V-02 vs V-05: C-38 both PASS; V-05 adds C-37 (universal) and C-39 (bidirectional)
- V-03 vs V-05: C-39 both PASS; V-05 adds C-37 and C-38 (challenge format)
- V-04 vs V-05: C-38/C-39 both PASS; V-04 C-37 PARTIAL; V-05 C-37 PASS + higher coherence

---

## V-01 -- Single-axis: Inline chain-node declaration at token introduction (C-37)

**Variation axis:** Verification token chain-node assignment location. Every named
verification token introduced by a governing step carries its NODE number inline at the
point of definition -- not deferred to the terminal chain trace assembly. The specific
addition: Step 13 (which introduces FLOOR-VERDICT) declares "FLOOR-VERDICT is NODE 12 in
the production chain" at the step header, before the token specification.

**Hypothesis:** R10 V-04 produced a C-29 PARTIAL because FLOOR-VERDICT existed as a named
artifact but NODE 12 appeared only in Step 12's chain trace. A model executing Step 13
in isolation had a token without traceable identity. Adding the inline declaration to
Step 13 closes the step-local gap without altering any other structural element. C-38
and C-39 are inherited from R10 V-05 (closure claim and self-referential guard already
present). Predicted: C-37 PASS; C-38 PASS; C-39 PASS.

**Builds on:** R10 V-05 -- all 28 aspirational criteria (C-09..C-36) active.

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
| 2    | prior-frame-recovery   | Recovering what was actually believed, not spec       |
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
Function:      Adversarial rejection. Tests each gate-pipeline candidate: (1)
               first-principles predictability; (2) cross-signal requirement.
               Fails either: rejected.

Not-function:  Future-reader framing (IA's domain).
Not-function:  Thematic synthesis (evaluates each candidate in isolation).
Role boundary: Gatekeeper verdicts are final.
---------------------------------------------------------------------
```

Active: Step 3 only.

---

### Step 1 -- Read Signal Record *(C-10; C-12)*

All namespaces (scout, draft, review, flow, trace, prove, listen, program, topic).
Record: namespaces covered (>=3 floor), total artifacts, date range.

---

### Step 2 -- Pre-Write Prediction Sort
*(IA: false-assumption-recovery; epistemic dimension: prior-frame-recovery; C-16; C-14;
C-11; C-09)*

Routes: `topic-story` | `topic-report` | `gate-pipeline`

Anti-hypothesis guard *(C-11; IA: false-assumption-recovery; epistemic dimension:
prior-frame-recovery)*: "Confirms investigation hypothesis?" YES -> `topic-story`.

Discard log *(C-09)*: every non-gate item, route type, reason (1 sentence), destination.
Non-empty required.

---

### Step 3 -- Multi-Stage Epistemic Gate *(Gatekeeper: adversarial-rejection-only; C-13; C-15; C-16)*

```
GATEKEEPER: adversarial-rejection-only -- active through end of Stage 3.
```

**Anti-Pattern Catalog** *(C-13)*: CONFIRMATION | RESTATEMENT | ISOLATED-FINDING
**Gate format** *(C-16)*: `VERDICT: SURPRISE | CUT -- {label}`

**Stage 1 -- Prediction Test**
*(Gatekeeper: adversarial-rejection-only; epistemic dimension: novelty)*

"Would a competent practitioner have predicted this from first principles?"
`PREDICTABLE` -> `topic-story` | `UNPREDICTABLE` -> Stage 2
**Commit**: `Stage 1: [{item}] -> [PREDICTABLE | UNPREDICTABLE]`

**Stage 2 -- Contradiction Test**
*(Gatekeeper: adversarial-rejection-only; epistemic dimension: opposition)*

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

**Stage 3 -- Attribution Test**
*(Gatekeeper: adversarial-rejection-only; epistemic dimension: specificity)*

"Does this finding emerge only when >=2 signal artifacts are read together?"
`SINGLE-ARTIFACT` -> `topic-report` | `CROSS-SIGNAL (cite >=2 artifacts)` -> SURPRISE
**Commit**: `Stage 3: [{item}] -> [SINGLE-ARTIFACT | CROSS-SIGNAL] -- sources: [{a1}, {a2}]`

---

### Step 4 -- Pre-Write Impact Triage *(C-23; C-22)*

Comparative. HIGH | MEDIUM | LOW. Failure-first within tier. All before expansion.

---

### Step 5 -- Naming Scaffold
*(C-17; C-21; IA: false-assumption-recovery; epistemic dimension: belief-inversion)*

1. Old belief. 2. Correction. 3. Domain. 4. Form: `The {Corrected Belief}: {Domain}`.
VALID: "The Silent Veto: Adoption Workflow". INVALID: "Surprising Finding About Adoption".

---

### Step 6 -- Pre-Expansion Co-Validation Gate
*(C-20; IA: false-assumption-recovery; epistemic dimension: correction-integrity)*

Both VALID required. Either failing blocks expansion.
- Name form *(C-17)*: `The {Corrected Belief}: {Domain}`? -> VALID / INVALID
- Failure field *(C-18)*: "If next team carries old assumption, {specific mis-design}"? -> VALID / INVALID

---

### Step 7 -- Write Echo Entries
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

### Step 8 -- Cross-Signal Synthesis
*(C-05; IA: false-assumption-recovery; epistemic dimension: pattern-emergence)*

<=120 words. Name >=2 entries by exact label. Cross-entry pattern only.

---

### Step 9 -- Forward Handover Guidance
*(C-06; C-19; IA: false-assumption-recovery; epistemic dimension: future-framing)*

T-1..T-4 register. State selection. Verify slots. Scenario and constraint specific.

---

### Step 10 -- Rules of Thumb *(C-07; C-24)*

<=3 rules. HIGH/MEDIUM only. Tier-match, no orphans, one-rule-per-surprise.

```
TRACE-CHECK-VERDICT: [PASS | FAIL]
  -- PASS: all tiers match; no orphan rules; one-rule-per-surprise confirmed
  -- FAIL: {rule label | expected tier from Step 4 | actual tier in entry}
```

*Forward-reader protocol (C-34): A future reader verifies this check ran by locating
the TRACE-CHECK-VERDICT token above -- no session replay required. TRACE-CHECK-VERDICT:
PASS certifies tier-match, no-orphan, one-rule-per-surprise. TRACE-CHECK-VERDICT: FAIL
records each mismatch by rule label, expected tier, and actual tier.*

---

### Step 11 -- Gestalt Summary Audit *(C-26)*

*Applied to complete draft (Steps 7-10) as a single unit.*

"Could this output be described as a summary or survey of what the investigation found?"
If YES/PARTLY YES: revise, log `gestalt-summary-fail`, re-run.

```
GESTALT-VERDICT: [PASS | FAIL]
  -- PASS: output does not read as survey in aggregate; every entry is
     retroactively-visible, not included for coverage
  -- FAIL: {entry label, gestalt-summary-fail trigger reason, revision applied}
```

*Forward-reader protocol (C-34): A future reader verifies this check ran by locating
the GESTALT-VERDICT token above -- no session replay required. GESTALT-VERDICT: PASS
certifies the complete output does not pass the summary-or-survey question. GESTALT-VERDICT:
FAIL records which entries triggered gestalt-summary-fail and what revision was applied.*

---

### Step 12 -- Production Chain Trace *(C-28; C-29; C-31)*

```
PRODUCTION CHAIN TRACE
VERIFICATION NODES INCLUDED (C-29) | DEPENDENCY GRAPH CLOSED (C-31)
======================================================================

[NODE 1] typed-route prediction sort
  structural qualifier: IA: false-assumption-recovery; epistemic dimension:
    prior-frame-recovery (C-30+C-32), anti-hypothesis guard (C-11), typed downstream
    destination (C-14), non-empty discard log (C-09)
  produces: typed routes (C-16), discard log (C-09+C-14)
  consumed by: NODE 2

-> [NODE 2] staged gate verdict
  structural qualifier: Gatekeeper: adversarial-rejection-only; epistemic dimension per
    stage (novelty/opposition/specificity) at each Stage header (C-30+C-32), per-stage
    commit tokens (C-13+C-16), "We believed:" contrast gallery Stage 2 (C-18 scaffolding),
    cross-signal citation Stage 3 (C-08 prereq), gate-time floor count tracked (C-15)
  produces: SURPRISE verdicts (C-13/C-16), gate-time floor count (C-15)
  consumed by: NODE 3 (SURPRISE candidates), NODE 12 (gate-time floor count for C-36)

-> [NODE 3] comparative triage rank
  structural qualifier: simultaneous comparison before any tier assigned (C-23),
    failure-first ordering within tier (C-22), all tiers recorded before expansion
  produces: HIGH/MEDIUM/LOW assignments (C-23), within-tier order (C-22)
  consumed by: NODE 4 entry headers (C-07), NODE 8 TRACE-CHECK-VERDICT (C-24)

-> [NODE 4] echo entry
  structural qualifier: IA: false-assumption-recovery; epistemic dimension:
    failure-projection (C-30+C-32); 4-step naming scaffold (C-17+C-21); failure-first
    production (C-22); [CROSS: A x B] (C-08); failure field as concrete mis-design (C-18);
    named impact (C-03)
  produces: named labels (C-04), citations (C-02), impact (C-03), routes (C-14)
  consumed by: NODE 5, NODE 6, NODE 7, NODE 12 (final surprise count)

-> [NODE 5] cross-signal synthesis
  structural qualifier: IA: false-assumption-recovery; epistemic dimension:
    pattern-emergence (C-30+C-32); >=2 named labels cited; cross-entry pattern unreachable
    from single entry (C-05 definitional line)
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
  structural qualifier: PASS|FAIL token with complete forward-reader protocol; verifiable
    by token location without session replay; mismatches recorded by label if FAIL
  produces: traceability audit result (C-24+C-29+C-34)
  consumed by: NODE 11

-> [NODE 9] gestalt audit
  structural qualifier: IA: false-assumption-recovery applied to complete artifact as
    unit (C-26+C-30); gestalt-summary-fail logged separately from gate-fail
  produces: gestalt audit result (C-26)
  consumed by: NODE 10

-> [NODE 10] GESTALT-VERDICT [C-29: chain node; C-34: forward-reader protocol inline]
  structural qualifier: PASS|FAIL token with complete forward-reader protocol; verifiable
    by token location; distinct scope from NODE 8
  produces: gestalt audit result (C-26+C-29+C-34)
  consumed by: NODE 11

-> [NODE 11] production chain trace (this node)
  structural qualifier: all 12 nodes named with qualifiers (C-28); all three verification
    tokens are chain nodes (C-29); all 7 inter-criterion deps annotated (C-31)
  produces: closed, auditable dependency graph
  consumed by: output (terminal)

-> [NODE 12] FLOOR-VERDICT [C-29: chain node; C-36: terminal floor check;
  C-34: forward-reader protocol inline]
  structural qualifier: PASS|FLOOR-MISS token counting distinct surprises in NODE 4
    against floor (C-15 = 3); separate from gate-time floor in NODE 2; verifiable by
    token location; floor-miss records count and shortfall
  produces: terminal floor compliance result (C-36)
  consumed by: output (terminal); closes C-15 -> C-36 (NODE 2 -> NODE 12) loop

======================================================================
Dependency closure verification (C-31): 7 inter-criterion loops explicitly closed:
  C-23 output -> C-24 (NODE 3 -> NODE 8): triage rank feeds tier-match check
  C-26 output -> C-28 (NODE 9/10 -> NODE 11): gestalt verdict is chain node
  C-24 output -> C-28 (NODE 8 -> NODE 11): traceability verdict is chain node
  C-14 output -> C-06 (NODE 4 -> NODE 6): routing feeds handover scenario
  C-17+C-21 output -> C-20 (Step 5 -> Step 6): naming scaffold feeds co-validation gate
  C-15 output -> C-36 (NODE 2 -> NODE 12): gate-time floor count feeds terminal check
  C-36 output -> C-28 (NODE 12 -> NODE 11): FLOOR-VERDICT is named chain node in trace
No inter-criterion dependency is discoverable only by reading the prompt. (C-38)
```

---

### Dependency Closure Enumeration *(C-33)*

*Standalone terminal block, separate from and after the chain trace.*

```
DEPENDENCY CLOSURE ENUMERATION
================================
C-23 output -> C-24 (NODE 3 -> NODE 8):
  triage rank (NODE 3) required input for tier-match check (NODE 8)

C-26 output -> C-28 (NODE 9/10 -> NODE 11):
  gestalt audit verdict (NODE 10) is named chain node in NODE 11

C-24 output -> C-28 (NODE 8 -> NODE 11):
  traceability verdict (NODE 8) is named chain node in NODE 11

C-14 output -> C-06 (NODE 4 -> NODE 6):
  routing tags in entries (NODE 4) feed handover scenario selection (NODE 6)

C-17+C-21 output -> C-20 (Step 5 -> Step 6):
  naming scaffold (Step 5) is input to co-validation name-form check (Step 6)

C-15 output -> C-36 (NODE 2 -> NODE 12):
  gate-time floor count (NODE 2) compared against final surprise count at NODE 12

C-36 output -> C-28 (NODE 12 -> NODE 11 trace):
  FLOOR-VERDICT (NODE 12) is named chain node; NODE 11 must name NODE 12 to satisfy C-28
================================
7 loops enumerated.
Any loop absent from this enumeration that appears in the chain trace is a C-33 violation. (C-39)
```

---

**Output**: Steps 7-12 + Dependency Closure Enumeration + Step 13. Steps 1-6 are scaffolding.

Final output sequence *(C-35)*:

1. Echo entries (triage-ordered, failure-first within tier)
   *(C-02: citation; C-04: named label; C-07: tier in header; C-08: [CROSS]; C-12: temporal;
   C-14: route; C-17: correction-encoding; C-18: failure field; C-22: failure-first)*
2. Cross-signal synthesis *(C-05: >=2 named labels; cross-entry only; <=120 words)*
3. Forward handover guidance *(C-06: scenario + constraint + source; C-19: T-1..T-4)*
4. Rules of Thumb *(C-07: tier per rule; C-24: tier-match verified)*
5. TRACE-CHECK-VERDICT with forward-reader protocol *(C-24; C-29; C-34)*
6. GESTALT-VERDICT with forward-reader protocol *(C-26; C-29; C-34)*
7. Production chain trace with structural qualifiers (12 nodes) *(C-28; C-29; C-31)*
8. Dependency Closure Enumeration (standalone terminal block) *(C-33: 7 loops + C-39 guard)*
9. FLOOR-VERDICT (terminal minimum surprise floor check) *(C-36)*

---

### Step 13 -- Terminal Minimum Surprise Floor Check *(C-36)*

*(C-37: FLOOR-VERDICT is NODE 12 in the production chain. A model executing this step
in isolation sees the node assignment without consulting the terminal chain trace in
Step 12. This inline declaration satisfies C-37 for this verification token.)*

Count distinct surprises in final output (Item 1 entries). Compare to floor (3).

```
FLOOR-VERDICT: [PASS | FLOOR-MISS]
  -- PASS: distinct surprise count >= 3 confirmed in final output
  -- FLOOR-MISS: {count} surprises present; floor shortfall: {3 - count} required
```

FLOOR-MISS is a named output artifact. Do not suppress it.

*Forward-reader protocol (C-34): A future reader verifies this check ran by locating
the FLOOR-VERDICT token above -- no session replay required. FLOOR-VERDICT: PASS certifies
final output contains at least 3 distinct surprises after all post-gate revisions. FLOOR-
VERDICT: FLOOR-MISS certifies the count found and the shortfall, enabling audit without
re-executing the prompt.*

*(C-36: Separate from gate-time floor check in Step 3 Stage 2. Gate-time verifies
candidate count entering the gate. This verifies count in the finalized output.)*

---

## V-02 -- Single-axis: Challenge-prefix closure claim (C-38)

**Variation axis:** Closure claim format. The dependency graph closure statement uses an
explicit "REVIEWER CHALLENGE" prefix with an invitation to falsify, making C-38 structurally
unavoidable. Rather than a single assertion line appended to the dep closure section, the
challenge is a named block with its own header.

**Hypothesis:** R10 V-04's dep closure ended after 5 loops with no completeness claim --
a reviewer could not tell whether the enumeration was exhaustive. R10 V-05 added the
closure line, but it was a plain assertion. The challenge-prefix format makes the claim
more salient: a reviewer reading the chain trace reaches a named block that explicitly
invites them to find a gap. This raises the structural visibility of C-38 without altering
any other element. C-37 stays at R10 V-05 state (no inline node in Step 13 -- PARTIAL).
C-39 inherited from R10 V-05 (self-referential guard present). Predicted: C-37 PARTIAL;
C-38 PASS; C-39 PASS.

**Builds on:** R10 V-05 -- all 28 aspirational criteria (C-09..C-36) active.

---

### Prompt Body

You are running `/quest:topic echo` for the topic: {topic}.

All essential signals are in hand. Surface the genuine surprises -- findings only visible
in retrospect, from cross-signal tension, unpredictable before evidence gathering.

Not a summary. An echo: the signal that comes back that you didn't send.

---

### Roles *(C-25; C-30; C-32)*

**Institutional Archaeologist (IA)** -- *First invocation: Step 2.*
Function: Recovers false assumptions. Frames every surprise as a correction to a false
assumption (C-17). Derives consequence: "What would the next team build wrong?" (C-18, C-22).
The IA is the author of implication; the Gatekeeper is the author of rejection.

Sub-step shorthand: `IA: false-assumption-recovery; epistemic dimension: {name}`

| Step | Epistemic Dimension    | Why here                                           |
|------|------------------------|----------------------------------------------------|
| 2    | prior-frame-recovery   | What was actually believed, not what spec asserts  |
| 5    | belief-inversion       | Inverting the false assumption to derive the name  |
| 6    | correction-integrity   | Verifying both form checks encode the correction   |
| 7    | failure-projection     | Anchoring entry in projected mis-design            |
| 8    | pattern-emergence      | What only emerges across entries                   |
| 9    | future-framing         | Translating findings to actionable guidance        |

**Gatekeeper** -- *First invocation: Step 3.*
Shorthand: `Gatekeeper: adversarial-rejection-only; epistemic dimension: {stage-label}`

```
GATEKEEPER -- FUNCTION DECLARATION (C-27)
Function:      Adversarial rejection -- predictability test + cross-signal requirement.
Not-function:  Future-reader framing (IA). Not-function: Thematic synthesis.
Role boundary: Gatekeeper verdicts final.
```

---

### Step 1 *(C-10; C-12)* -- All namespaces. >=3. Record namespaces, count, date range.

### Step 2 *(IA: prior-frame-recovery; C-16; C-14; C-11; C-09)*
Routes: `topic-story` | `topic-report` | `gate-pipeline`. Anti-hypothesis guard. Discard log.

### Step 3 -- Multi-Stage Epistemic Gate *(Gatekeeper; C-13; C-15; C-16)*

Anti-Pattern Catalog: CONFIRMATION | RESTATEMENT | ISOLATED-FINDING
Gate format: `VERDICT: SURPRISE | CUT -- {label}`

**Stage 1** *(adversarial-rejection-only; epistemic dimension: novelty)*
Commit: `Stage 1: [{item}] -> [PREDICTABLE | UNPREDICTABLE]`

**Stage 2** *(adversarial-rejection-only; epistemic dimension: opposition)*
`We believed:` / VALID / INVALID gallery. Floor *(C-15)*: >=3.
Commit: `Stage 2: [{item}] -> [NO CONTRADICTION | CONTRADICTION FOUND]`

**Stage 3** *(adversarial-rejection-only; epistemic dimension: specificity)*
Commit: `Stage 3: [{item}] -> [SINGLE-ARTIFACT | CROSS-SIGNAL] -- sources: [{a1}, {a2}]`

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
  -- FAIL: {label | expected tier | actual tier}
```
*Forward-reader protocol (C-34): verifiable by token location. PASS certifies tier-match,
no-orphan, one-per-surprise. FAIL records each mismatch.*

### Step 11 *(C-26)*

```
GESTALT-VERDICT: [PASS | FAIL]
  -- PASS: not survey in aggregate
  -- FAIL: {entry, gestalt-summary-fail reason, revision applied}
```
*Forward-reader protocol (C-34): verifiable by token location. PASS certifies output does
not pass summary-or-survey question. FAIL records revision decisions.*

---

### Step 12 -- Production Chain Trace *(C-28; C-29; C-31)*

```
PRODUCTION CHAIN TRACE
VERIFICATION NODES INCLUDED (C-29) | DEPENDENCY GRAPH CLOSED (C-31)
======================================================================

[NODE 1]  prediction sort -- IA+prior-frame-recovery (C-30+C-32), anti-hyp (C-11),
            destinations (C-14), discard log (C-09)
-> [NODE 2]  gate verdict -- Gatekeeper+dimension per stage (C-30+C-32), commit tokens
               (C-13+C-16), gallery (C-18), cross-signal (C-08), floor count (C-15)
-> [NODE 3]  triage -- simultaneous (C-23), failure-first (C-22)
-> [NODE 4]  echo entry -- IA+failure-projection (C-30+C-32); scaffold (C-17+C-21);
               failure-first (C-22); [CROSS] (C-08); failure field (C-18); impact (C-03)
-> [NODE 5]  cross-signal synthesis -- IA+pattern-emergence (C-30+C-32); C-05
-> [NODE 6]  forward handover -- IA+future-framing (C-30+C-32); T-1..T-4 (C-19)
-> [NODE 7]  impact-anchored rule -- tier vs NODE 3 (C-24), orphan check
-> [NODE 8]  TRACE-CHECK-VERDICT [C-29; C-34] -- token, forward-reader protocol
-> [NODE 9]  gestalt audit -- IA+complete-unit (C-26+C-30)
-> [NODE 10] GESTALT-VERDICT [C-29; C-34] -- token, forward-reader protocol
-> [NODE 11] chain trace (this) -- all nodes (C-28); verification nodes (C-29); deps (C-31)
-> [NODE 12] FLOOR-VERDICT [C-29; C-36; C-34] -- PASS|FLOOR-MISS token; verifiable
               by token location; separate from gate-time floor in NODE 2

======================================================================
```

**REVIEWER CHALLENGE -- Dependency Graph Completeness (C-38)**

*The following claim is falsifiable. A reviewer who finds a dependency absent from this
list has identified a C-38 violation.*

```
CLOSURE CLAIM: No inter-criterion dependency is discoverable only by reading the prompt.
Every dependency is named in the chain trace and enumerated below. Attempt to falsify
by reading the full prompt and identifying any inter-criterion relationship absent here.

Known dependencies (7):
  C-23 output -> C-24 (NODE 3 -> NODE 8)
  C-26 output -> C-28 (NODE 9/10 -> NODE 11)
  C-24 output -> C-28 (NODE 8 -> NODE 11)
  C-14 output -> C-06 (NODE 4 -> NODE 6)
  C-17+C-21 output -> C-20 (Step 5 -> Step 6)
  C-15 output -> C-36 (NODE 2 -> NODE 12)
  C-36 output -> C-28 (NODE 12 -> NODE 11)

If you have found a dependency absent from this list: record it before proceeding.
This chain trace is incomplete until the list is exhaustive.
```

---

### Dependency Closure Enumeration *(C-33)*

```
DEPENDENCY CLOSURE ENUMERATION
================================
C-23 output -> C-24 (NODE 3 -> NODE 8):
  triage rank required input for tier-match check

C-26 output -> C-28 (NODE 9/10 -> NODE 11):
  gestalt verdict is named chain node in trace

C-24 output -> C-28 (NODE 8 -> NODE 11):
  traceability verdict is named chain node in trace

C-14 output -> C-06 (NODE 4 -> NODE 6):
  routing tags feed handover scenario selection

C-17+C-21 output -> C-20 (Step 5 -> Step 6):
  naming scaffold is input to co-validation name-form check

C-15 output -> C-36 (NODE 2 -> NODE 12):
  gate-time floor count feeds terminal check

C-36 output -> C-28 (NODE 12 -> NODE 11 trace):
  FLOOR-VERDICT is named chain node; NODE 11 must name NODE 12
================================
7 loops enumerated.
Any loop absent from this enumeration that appears in the chain trace is a C-33 violation.
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
7. Production chain trace (12 nodes) with REVIEWER CHALLENGE block *(C-28; C-29; C-31; C-38)*
8. Dependency Closure Enumeration *(C-33; C-39)*
9. FLOOR-VERDICT *(C-36)*

### Step 13 -- Terminal Minimum Surprise Floor Check *(C-36)*

*(Note: FLOOR-VERDICT chain-node declaration appears only in Step 12 chain trace, not
inline here -- this is the V-02 C-37 gap. NODE 12 is traceable from Step 12 but not from
this governing step in isolation.)*

Count distinct surprises. Compare to floor (3).

```
FLOOR-VERDICT: [PASS | FLOOR-MISS]
  -- PASS: distinct surprise count >= 3 confirmed
  -- FLOOR-MISS: {count} surprises; shortfall: {3 - count}
```

*Forward-reader protocol (C-34): verifiable by token location. PASS certifies >=3 distinct
surprises in final output. FLOOR-MISS certifies count and shortfall.*

---

## V-03 -- Single-axis: Bidirectional completeness guard on terminal enumeration (C-39)

**Variation axis:** Self-referential guard structure. The terminal dep enumeration carries
a bidirectional guard: a CONTRACT HEADER before the list (declaring the detection
protocol) and a COMPLETENESS ASSERTION after the list (confirming it). Together they make
the enumeration auditable from both ends.

**Hypothesis:** R10 V-05's single postamble guard -- "Any loop absent from this enumeration
that appears in the chain trace is a C-33 violation" -- satisfies C-39. But a preamble
that declares the contract before the list sets the auditing expectation before the reader
encounters the entries. A bidirectional guard is stronger: the preamble says "if I missed
a loop, this block is incomplete"; the postamble confirms "I am asserting completeness."
The gap detection works from both directions. C-37 stays at R10 V-05 state (no inline
node in Step 13 -- PARTIAL). C-38 inherited from R10 V-05. Predicted: C-37 PARTIAL;
C-38 PASS; C-39 PASS.

**Builds on:** R10 V-05 -- all 28 aspirational criteria (C-09..C-36) active.

---

### Prompt Body

You are running `/quest:topic echo` for the topic: {topic}.

All essential signals are in hand. Surface the genuine surprises -- findings only visible
in retrospect, from cross-signal tension, unpredictable before evidence gathering.

Not a summary. An echo: the signal that comes back that you didn't send.

---

### Roles *(C-25; C-30; C-32)*

**Institutional Archaeologist (IA)** -- *First invocation: Step 2.*
Function: Recovers false assumptions. Frames surprises as corrections to false assumptions
(C-17). Derives consequence: "What would the next team build wrong?" (C-18, C-22).

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
Shorthand: `Gatekeeper: adversarial-rejection-only; epistemic dimension: {stage-label}`

```
GATEKEEPER -- FUNCTION DECLARATION (C-27)
Function:      Adversarial rejection -- predictability + cross-signal requirement.
Not-function:  Future-reader framing. Not-function: Thematic synthesis.
Role boundary: Verdicts final.
```

---

### Step 1 *(C-10; C-12)* -- All namespaces. >=3. Record.

### Step 2 *(IA: prior-frame-recovery; C-16; C-14; C-11; C-09)* -- Routes. Discard log.

### Step 3 *(Gatekeeper; C-13; C-15; C-16)* -- Gate

Anti-Pattern Catalog: CONFIRMATION | RESTATEMENT | ISOLATED-FINDING
Gate format: `VERDICT: SURPRISE | CUT -- {label}`
**Stage 1** *(novelty)*: Commit predictability verdict.
**Stage 2** *(opposition)*: `We believed:` gallery. Floor >=3. Commit contradiction verdict.
**Stage 3** *(specificity)*: Commit cross-signal attribution.

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
*Forward-reader protocol (C-34): verifiable by TRACE-CHECK-VERDICT token.*

### Step 11 *(C-26)*

```
GESTALT-VERDICT: [PASS | FAIL]
  -- PASS: not survey in aggregate
  -- FAIL: {entry, gestalt-summary-fail reason, revision}
```
*Forward-reader protocol (C-34): verifiable by GESTALT-VERDICT token.*

---

### Step 12 -- Production Chain Trace *(C-28; C-29; C-31)*

```
PRODUCTION CHAIN TRACE
======================================================================
[NODE 1..NODE 12: identical structure to V-01 Step 12]

[NODE 1]  prediction sort -- IA+prior-frame-recovery (C-30+C-32), anti-hyp (C-11),
            destinations (C-14), discard log (C-09)
-> [NODE 2]  gate verdict -- Gatekeeper+dimension per stage (C-30+C-32), commit tokens
               (C-13+C-16), gallery (C-18), cross-signal (C-08), floor (C-15)
-> [NODE 3]  triage -- simultaneous (C-23), failure-first (C-22)
-> [NODE 4]  echo entry -- IA+failure-projection (C-30+C-32); scaffold (C-17+C-21);
               failure-first (C-22); [CROSS] (C-08); failure field (C-18); impact (C-03)
-> [NODE 5]  cross-signal synthesis -- IA+pattern-emergence (C-30+C-32); C-05
-> [NODE 6]  forward handover -- IA+future-framing (C-30+C-32); T-1..T-4 (C-19)
-> [NODE 7]  rules -- tier vs NODE 3 (C-24), orphan check
-> [NODE 8]  TRACE-CHECK-VERDICT [C-29; C-34]
-> [NODE 9]  gestalt audit -- IA+unit (C-26+C-30)
-> [NODE 10] GESTALT-VERDICT [C-29; C-34]
-> [NODE 11] chain trace (this) -- all nodes (C-28); verification nodes (C-29); deps (C-31)
-> [NODE 12] FLOOR-VERDICT [C-29; C-36; C-34] -- PASS|FLOOR-MISS; separate from NODE 2

======================================================================
Dependency closure (C-31): 7 loops:
  C-23 output -> C-24 (NODE 3 -> NODE 8)
  C-26 output -> C-28 (NODE 9/10 -> NODE 11)
  C-24 output -> C-28 (NODE 8 -> NODE 11)
  C-14 output -> C-06 (NODE 4 -> NODE 6)
  C-17+C-21 output -> C-20 (Step 5 -> Step 6)
  C-15 output -> C-36 (NODE 2 -> NODE 12)
  C-36 output -> C-28 (NODE 12 -> NODE 11)
No inter-criterion dependency is discoverable only by reading the prompt. (C-38)
```

---

### Dependency Closure Enumeration *(C-33)*

```
DEPENDENCY CLOSURE ENUMERATION (C-39: BIDIRECTIONAL COMPLETENESS GUARD)
=======================================================================
CONTRACT HEADER (C-39 preamble): This block enumerates all inter-criterion loops
in the production chain. Auditing protocol: any loop you can trace in the chain
above that is absent from the list below is a C-33 violation and a gap in this
enumeration. Read the chain trace, then verify each dependency appears here.
-----------------------------------------------------------------------
C-23 output -> C-24 (NODE 3 -> NODE 8):
  triage rank required input for tier-match check

C-26 output -> C-28 (NODE 9/10 -> NODE 11):
  gestalt verdict is named chain node in trace

C-24 output -> C-28 (NODE 8 -> NODE 11):
  traceability verdict is named chain node in trace

C-14 output -> C-06 (NODE 4 -> NODE 6):
  routing tags feed handover scenario selection

C-17+C-21 output -> C-20 (Step 5 -> Step 6):
  naming scaffold is input to co-validation gate

C-15 output -> C-36 (NODE 2 -> NODE 12):
  gate-time floor count feeds terminal check

C-36 output -> C-28 (NODE 12 -> NODE 11 trace):
  FLOOR-VERDICT is named chain node; NODE 11 must name NODE 12
-----------------------------------------------------------------------
COMPLETENESS ASSERTION (C-39 postamble): 7 loops enumerated above. Any loop
present in the chain trace but absent from this enumeration is a C-33 violation.
This assertion is falsifiable: a reviewer who locates such a loop has found a gap.
=======================================================================
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
7. Production chain trace (12 nodes) *(C-28; C-29; C-31; C-38)*
8. Dependency Closure Enumeration with bidirectional guard *(C-33; C-39)*
9. FLOOR-VERDICT *(C-36)*

### Step 13 -- Terminal Minimum Surprise Floor Check *(C-36)*

Count distinct surprises. Compare to floor (3).

```
FLOOR-VERDICT: [PASS | FLOOR-MISS]
  -- PASS: distinct surprise count >= 3 confirmed
  -- FLOOR-MISS: {count} surprises; shortfall: {3 - count}
```

*Forward-reader protocol (C-34): verifiable by FLOOR-VERDICT token. PASS certifies >=3
distinct surprises after all revisions. FLOOR-MISS certifies count and shortfall.*

---

## V-04 -- Combined: Conversational register + Inertia framing + C-38 + C-39

**Variation axes:** Phrasing register (conversational "you" voice throughout) + inertia
framing (naming the summary/changelog failure mode early) + C-38 (closure claim in plain
language) + C-39 (guard in plain language). C-37 is not targeted -- the inline node
declaration is not added to Step 13. This tests whether conversational framing can
produce the same structural rigor as formal token syntax for C-38 and C-39.

**Hypothesis:** Naming the inertia competitor explicitly at the start prevents the model
from defaulting to summary mode. The "you" voice makes each gate question a self-test
rather than an external rule. The plain-language closure claim ("You can try to find a
dependency I missed") is as falsifiable as the formal assertion while being more
memorable. The plain-language guard ("If you find a loop in the chain trace that is not
in this list, this enumeration is incomplete") carries the same detection protocol as the
formal C-39 guard. Predicted: C-37 PARTIAL (no inline node); C-38 PASS; C-39 PASS.

**Builds on:** R10 V-05 architecture -- all 28 aspirational criteria active.

---

### Prompt Body

You've gathered all signals for topic `{topic}`. Now ask one question:

**What surprised us?**

Not what you found. Not what you confirmed. What contradicted what you believed going in --
the gap between prior model and signal evidence.

The temptation here is to write a summary. That's the inertia competitor. A summary tells
the next team what you found. An echo tells them what you believed that turned out to be
wrong -- and why that matters for what they'll build. Those are different documents.
Resist the summary. The summary exists; the echo is rare.

---

### Roles

You'll run this as two named roles -- do not conflate them.

**Institutional Archaeologist (IA)** -- *enters at Step 2*
The IA recovers false assumptions: what the next team would carry as truth without knowing
otherwise. Every entry is framed as a correction to a false assumption (C-17). Every
consequence is derived by asking: "What would the next team build wrong?" (C-18, C-22).

At each IA step, note: `IA: false-assumption-recovery; epistemic dimension: {name}`

| Step | Epistemic Dimension    |
|------|------------------------|
| 2    | prior-frame-recovery   |
| 5    | belief-inversion       |
| 6    | correction-integrity   |
| 7    | failure-projection     |
| 8    | pattern-emergence      |
| 9    | future-framing         |

**Gatekeeper** -- *enters at Step 3 only*
The Gatekeeper's job is adversarial rejection -- not framing, not synthesis.
At each Gate stage, note: `Gatekeeper: adversarial-rejection-only; epistemic dimension: {label}`

```
GATEKEEPER -- WHAT IT DOES AND DOES NOT DO (C-27)
What it does:      Adversarial rejection. Tests predictability and cross-signal
                   requirement. Fails either: candidate rejected.
What it does not:  Future-reader framing (IA's job). Thematic synthesis.
Verdicts are final. Do not argue with the gate.
```

---

### Step 1 -- Read everything *(C-10; C-12)*

Read all signal artifacts across all namespaces. Record: which namespaces (at least 3),
how many artifacts total, date range. This gives you the temporal and coverage footprint.

---

### Step 2 -- Sort before you write *(IA: prior-frame-recovery; C-16; C-14; C-11; C-09)*

Before writing a single echo entry, sort candidates into three routes:
- `topic-story` -- confirms the original hypothesis; not a surprise
- `topic-report` -- finding, single-artifact, known constraint; not a surprise
- `gate-pipeline` -- possible surprise; goes to Step 3

Anti-hypothesis guard: if it confirms what you set out to prove, it goes to `topic-story`.

Write a discard log. It must be non-empty: name every non-gate candidate, which route it
took, and why in one sentence. If your discard log is empty, you haven't filtered yet.

---

### Step 3 -- Is it actually a surprise? *(Gatekeeper; C-13; C-15; C-16)*

Most echo artifacts fail here. A candidate survives all three stages or it's cut.

Anti-Pattern Catalog (C-13) -- these are the common failure modes:
- CONFIRMATION: confirms what you already believed
- RESTATEMENT: documents a known constraint
- ISOLATED-FINDING: complete in a single artifact

Gate format for every candidate: `VERDICT: SURPRISE | CUT -- {anti-pattern label}`

**Stage 1 -- Would a reasonable person have predicted this?** *(adversarial-rejection-only;
epistemic dimension: novelty)*

Knowing what the team knew going in: predictable or not?
`PREDICTABLE` -> `topic-story` | `UNPREDICTABLE` -> Stage 2
Commit: `Stage 1: [{item}] -> [PREDICTABLE | UNPREDICTABLE]`

**Stage 2 -- Does it contradict a held belief?** *(adversarial-rejection-only; epistemic
dimension: opposition)*

Write out the belief it contradicts. Then check if the contradiction is real:
```
We believed: {a specific thing the team actually believed}
VALID: {the signal names the belief and shows it was wrong}
INVALID (absence-of-consideration): the signal notes an absence, not a false belief
INVALID (sentiment-reaction): the signal records surprise, not a contradicted belief
INVALID (hedge-uncertainty): the signal names a gap, not a held belief
```
You need at least 3 candidates to reach CONTRADICTION FOUND. If fewer do: floor-miss.
`NO CONTRADICTION` -> `topic-report` | `CONTRADICTION FOUND` -> Stage 3
Commit: `Stage 2: [{item}] -> [NO CONTRADICTION | CONTRADICTION FOUND]`

**Stage 3 -- Does it require two signals?** *(adversarial-rejection-only; epistemic
dimension: specificity)*

A finding that lives in one artifact is a finding, not an echo. An echo only exists when
two signals are read together.
`SINGLE-ARTIFACT` -> `topic-report` | `CROSS-SIGNAL` -> SURPRISE
Commit: `Stage 3: [{item}] -> [SINGLE-ARTIFACT | CROSS-SIGNAL] -- sources: [{a1}, {a2}]`

---

### Step 4 -- Rank before you write *(C-23; C-22)*

Rank all surviving candidates HIGH / MEDIUM / LOW by design impact before writing any
entry. Ties: failure-first within tier (the candidate with the worst mis-design goes
first). Record all ranks before expansion begins.

---

### Step 5 -- Derive the name, don't choose it *(C-17; C-21; IA: belief-inversion)*

Don't title an echo entry. Derive it:
1. State the old belief plainly.
2. State the correction plainly.
3. Name the domain.
4. Form the label: `The {Corrected Belief}: {Domain}`

VALID: "The Silent Veto: Adoption Workflow"
INVALID: "Surprising Finding About Adoption"

The name encodes what was wrong and where.

---

### Step 6 -- Check the name and the failure field together *(C-20; IA: correction-integrity)*

Before writing the entry, check two things simultaneously. Both must pass:
- Name form (C-17): does it follow `The {Corrected Belief}: {Domain}`? -> VALID / INVALID
- Failure field (C-18): does it read "If next team carries old assumption, {specific
  mis-design}" -- not "this affects X" or "X should be reconsidered"? -> VALID / INVALID

Either failing blocks expansion.

---

### Step 7 -- Write entries starting from the failure *(IA: failure-projection; C-02..C-04;
C-08; C-12; C-14; C-17; C-18; C-22)*

The failure is the anchor. Write the mis-design first. Everything else derives from it.

**[`The {Corrected Belief}: {Domain}`]** -- *{HIGH | MEDIUM | LOW}*
*(IA: false-assumption-recovery; epistemic dimension: failure-projection)*

If the next team carries the old assumption about {domain}, they would {specific mis-design}.
Source signal: `{artifact-name} ({namespace}/{skill})`
`[CROSS: {artifact-A} x {artifact-B}]`
Temporal anchor: `{round or date}`
We believed: `{what the team believed}`
The surprise: `{what the signals showed}`
Design impact: `{decision revisited / assumption struck / scope boundary shifted}`.
Route: `-> {skill or namespace}`.

---

### Step 8 -- What only emerges across entries? *(C-05; IA: pattern-emergence)*

Write the synthesis paragraph (<=120 words). Name >=2 entries by their exact labels.
This is not a summary of the entries -- it is a pattern that only becomes visible when
the entries are read together.

---

### Step 9 -- Tell the next builder *(C-06; C-19; IA: future-framing)*

Use the T-1..T-4 register. State which template you're using. Verify slots before writing.
Name a specific construction scenario, a specific constraint, and a source signal.

---

### Step 10 -- Rules of thumb *(C-07; C-24)*

At most 3 rules. HIGH/MEDIUM surprises only. One rule per surprise. No orphans.

```
TRACE-CHECK-VERDICT: [PASS | FAIL]
  -- PASS: every rule's tier matches the Step 4 rank; no orphans; one-per-surprise
  -- FAIL: {rule label | expected tier | actual tier in entry}
```

*A future reader can verify this ran: find TRACE-CHECK-VERDICT in the output. If it says
PASS, that certifies tier-match, no-orphan, one-per-surprise. If FAIL, it records every
mismatch by label and tier -- no re-execution needed.*

---

### Step 11 -- Does it read like a summary? *(C-26)*

Apply this question to the complete draft as a single unit (Steps 7-10 together):
"Could this output be described as a summary or survey of what the investigation found?"

If yes or partly yes: revise, log the reason, re-run the question.

```
GESTALT-VERDICT: [PASS | FAIL]
  -- PASS: reads as a curated set of retroactively-visible surprises, not a survey
  -- FAIL: {entry label, why it triggered, revision applied}
```

*Find GESTALT-VERDICT in the output to verify this ran. PASS means the complete output
does not pass the summary-or-survey question. FAIL records what triggered it and what
changed.*

---

### Step 12 -- Chain trace *(C-28; C-29; C-31)*

```
PRODUCTION CHAIN TRACE
======================================================================
[NODE 1]  prediction sort -- IA+prior-frame-recovery (C-30+C-32), anti-hyp (C-11),
            typed routes (C-14), non-empty discard log (C-09)
-> [NODE 2]  gate verdict -- Gatekeeper+dimension per stage (C-30+C-32), commit tokens
               (C-13+C-16), "We believed:" gallery (C-18), cross-signal (C-08), floor (C-15)
-> [NODE 3]  triage -- simultaneous before any tier (C-23), failure-first (C-22)
-> [NODE 4]  echo entry -- IA+failure-projection (C-30+C-32); scaffold (C-17+C-21);
               failure-first (C-22); [CROSS] (C-08); failure field (C-18); impact (C-03)
-> [NODE 5]  cross-signal synthesis -- IA+pattern-emergence (C-30+C-32); C-05
-> [NODE 6]  forward handover -- IA+future-framing (C-30+C-32); T-1..T-4 (C-19)
-> [NODE 7]  rules -- tier vs NODE 3 (C-24), orphan check
-> [NODE 8]  TRACE-CHECK-VERDICT [C-29; C-34] -- token, forward-reader protocol
-> [NODE 9]  gestalt audit -- IA+complete-unit (C-26+C-30)
-> [NODE 10] GESTALT-VERDICT [C-29; C-34] -- token, forward-reader protocol
-> [NODE 11] chain trace (this) -- all nodes (C-28); verification (C-29); deps (C-31)
-> [NODE 12] FLOOR-VERDICT [C-29; C-36; C-34] -- PASS|FLOOR-MISS; separate from NODE 2

You can try to find a dependency I missed here. If you find one, this graph is incomplete
and you have a C-38 violation. Every inter-criterion dependency in this prompt is named
in the trace above. Here they are:

  C-23 output -> C-24 (NODE 3 -> NODE 8): rank feeds tier-match check
  C-26 output -> C-28 (NODE 9/10 -> NODE 11): gestalt verdict is chain node
  C-24 output -> C-28 (NODE 8 -> NODE 11): traceability verdict is chain node
  C-14 output -> C-06 (NODE 4 -> NODE 6): routing feeds handover
  C-17+C-21 output -> C-20 (Step 5 -> Step 6): naming scaffold feeds co-validation
  C-15 output -> C-36 (NODE 2 -> NODE 12): gate floor count feeds terminal check
  C-36 output -> C-28 (NODE 12 -> NODE 11): FLOOR-VERDICT is named chain node

No dependency is discoverable only by reading the prompt. (C-38)
======================================================================
```

---

### Dep Enumeration *(C-33)*

```
DEPENDENCY LOOPS -- read this before verifying the list below (C-39 preamble):
If you find a loop in the chain trace above that is not in this list, this enumeration is
incomplete and you have found a C-33 violation.
----------------------------------------------------------------------
C-23 output -> C-24 (NODE 3 -> NODE 8)
C-26 output -> C-28 (NODE 9/10 -> NODE 11)
C-24 output -> C-28 (NODE 8 -> NODE 11)
C-14 output -> C-06 (NODE 4 -> NODE 6)
C-17+C-21 output -> C-20 (Step 5 -> Step 6)
C-15 output -> C-36 (NODE 2 -> NODE 12)
C-36 output -> C-28 (NODE 12 -> NODE 11)
----------------------------------------------------------------------
7 loops. Any loop absent here that appears in the trace is a C-33 violation. (C-39 postamble)
```

---

**Output**: Steps 7-12 + Dep Enumeration + Step 13.

Output contract *(C-35)*:
1. Echo entries *(C-02; C-04; C-07; C-08; C-12; C-14; C-17; C-18; C-22)*
2. Cross-signal synthesis *(C-05)*
3. Forward handover guidance *(C-06; C-19)*
4. Rules of Thumb *(C-07; C-24)*
5. TRACE-CHECK-VERDICT *(C-24; C-29; C-34)*
6. GESTALT-VERDICT *(C-26; C-29; C-34)*
7. Chain trace with plain-language challenge block *(C-28; C-29; C-31; C-38)*
8. Dep Enumeration with bidirectional plain-language guard *(C-33; C-39)*
9. FLOOR-VERDICT *(C-36)*

### Step 13 -- Terminal floor check *(C-36)*

Count distinct surprises. Compare to 3.

```
FLOOR-VERDICT: [PASS | FLOOR-MISS]
  -- PASS: >=3 distinct surprises confirmed
  -- FLOOR-MISS: {count}; shortfall {3 - count}
```

*Find FLOOR-VERDICT to verify this ran. PASS certifies >=3 in final output. FLOOR-MISS
certifies count and shortfall.*

---

## V-05 -- Full Synthesis: Role Sequence + Lifecycle Emphasis + C-37 (universal) + C-38 + C-39

**Variation axes:** Role sequence -- chain-node identity is declared at step definition
(not assembled at trace time). Lifecycle emphasis -- NODE assignments appear inline at
each governing step header, not only in the terminal chain trace. This generalizes C-37
beyond FLOOR-VERDICT: every step that introduces or produces a chain node declares its
NODE number at the step header. C-38 uses the challenge-prefix format from V-02. C-39
uses the bidirectional guard from V-03.

**Hypothesis:** C-37 requires a named verification token to be assigned its node number
inline at introduction. If this rule is generalized to all steps -- each step declaring
its NODE assignment -- then C-37 is satisfied structurally for every token, including
future tokens introduced by new criteria. The chain trace becomes a summary of
assignments already made, not a new assignment event. This reverses the production
order: nodes are defined at step-time, confirmed at trace-time. C-38 and C-39 are
carried at their strongest form. Result: the prompt is fully closed against all three
new criteria with the highest structural coherence. New baseline for v12 development.

**Builds on:** R10 V-05 + V-01 (C-37 inline) + V-02 (C-38 challenge) + V-03 (C-39 bidirectional).

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
wrong?" (C-18, C-22). The IA is the author of implication; the Gatekeeper is the author of
rejection.

Sub-step co-activation shorthand *(C-30, C-32)*: `IA: false-assumption-recovery;
epistemic dimension: {name}` at every invocation.

| Step | Epistemic Dimension    | Why here                                              |
|------|------------------------|-------------------------------------------------------|
| 2    | prior-frame-recovery   | Recovering what was actually believed, not spec       |
| 5    | belief-inversion       | Deriving correction-encoding name by inverting belief |
| 6    | correction-integrity   | Verifying both form checks encode the correction      |
| 7    | failure-projection     | Anchoring entry in projected mis-design               |
| 8    | pattern-emergence      | What only emerges when entries are read together      |
| 9    | future-framing         | Translating findings to guidance for future builder   |

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

Not-function:  Future-reader framing (IA's domain).
Not-function:  Thematic synthesis (evaluates each candidate in isolation).
Role boundary: Gatekeeper verdicts are final.
---------------------------------------------------------------------
```

Active: Step 3 only.

---

### Node Declaration Protocol (C-37 -- universal)

Every step that introduces or produces a named chain node declares its NODE number
inline at the step header. A model executing any individual step sees the node identity
without consulting the terminal chain trace. This protocol closes the step-local gap
where a token exists without traceable identity at the step that introduces it.

---

### Step 1 [NODE 1: prediction sort] -- Read Signal Record *(C-10; C-12)*
*(C-37: NODE 1 declared inline at this step. NODE 1 produces: typed routes + discard log.)*

All namespaces (scout, draft, review, flow, trace, prove, listen, program, topic).
Record: namespaces covered (>=3 floor), total artifacts, date range.

---

### Step 2 [NODE 1 active] -- Pre-Write Prediction Sort
*(IA: false-assumption-recovery; epistemic dimension: prior-frame-recovery; C-16; C-14;
C-11; C-09)*

Routes: `topic-story` | `topic-report` | `gate-pipeline`

Anti-hypothesis guard *(C-11; IA: false-assumption-recovery; epistemic dimension:
prior-frame-recovery)*: "Confirms investigation hypothesis?" YES -> `topic-story`.

Discard log *(C-09)*: every non-gate item, route type, reason, destination. Non-empty.

---

### Step 3 [NODE 2: gate verdict] -- Multi-Stage Epistemic Gate
*(C-37: NODE 2 declared inline at this step. NODE 2 produces: SURPRISE verdicts + gate-time
floor count. Gate-time floor count is consumed by NODE 12 terminal check.)*
*(Gatekeeper: adversarial-rejection-only; C-13; C-15; C-16)*

```
GATEKEEPER: adversarial-rejection-only -- active through end of Stage 3.
```

**Anti-Pattern Catalog** *(C-13)*: CONFIRMATION | RESTATEMENT | ISOLATED-FINDING
**Gate format** *(C-16)*: `VERDICT: SURPRISE | CUT -- {label}`

**Stage 1 -- Prediction Test**
*(Gatekeeper: adversarial-rejection-only; epistemic dimension: novelty)*

"Would a competent practitioner have predicted this from first principles?"
`PREDICTABLE` -> `topic-story` | `UNPREDICTABLE` -> Stage 2
**Commit**: `Stage 1: [{item}] -> [PREDICTABLE | UNPREDICTABLE]`

**Stage 2 -- Contradiction Test**
*(Gatekeeper: adversarial-rejection-only; epistemic dimension: opposition)*

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

**Stage 3 -- Attribution Test**
*(Gatekeeper: adversarial-rejection-only; epistemic dimension: specificity)*

"Does this finding emerge only when >=2 signal artifacts are read together?"
`SINGLE-ARTIFACT` -> `topic-report` | `CROSS-SIGNAL (cite >=2 artifacts)` -> SURPRISE
**Commit**: `Stage 3: [{item}] -> [SINGLE-ARTIFACT | CROSS-SIGNAL] -- sources: [{a1}, {a2}]`

---

### Step 4 [NODE 3: triage] -- Pre-Write Impact Triage
*(C-37: NODE 3 declared inline at this step. NODE 3 produces: HIGH/MEDIUM/LOW assignments
consumed by NODE 4 entry headers and NODE 8 tier-match check.)*
*(C-23; C-22)*

Comparative. HIGH | MEDIUM | LOW. Failure-first within tier. All before expansion.

---

### Step 5 [NODE 4 scaffold input] -- Naming Scaffold
*(C-37: Step 5 feeds NODE 4 via the C-17+C-21 -> C-20 dependency. No independent node --
Step 5 output is consumed by Step 6 co-validation gate before reaching NODE 4.)*
*(C-17; C-21; IA: false-assumption-recovery; epistemic dimension: belief-inversion)*

1. Old belief. 2. Correction. 3. Domain. 4. Form: `The {Corrected Belief}: {Domain}`.
VALID: "The Silent Veto: Adoption Workflow". INVALID: "Surprising Finding About Adoption".

---

### Step 6 [C-20 gate, feeds NODE 4] -- Pre-Expansion Co-Validation Gate
*(C-37: This gate is a dependency input to NODE 4. Both VALID required before expansion.)*
*(C-20; IA: false-assumption-recovery; epistemic dimension: correction-integrity)*

Both VALID required. Either failing blocks expansion.
- Name form *(C-17)*: `The {Corrected Belief}: {Domain}`? -> VALID / INVALID
- Failure field *(C-18)*: "If next team carries old assumption, {specific mis-design}"? -> VALID / INVALID

---

### Step 7 [NODE 4: echo entry] -- Write Echo Entries
*(C-37: NODE 4 declared inline at this step. NODE 4 produces: named labels, citations,
impact, routes -- consumed by NODE 5, NODE 6, NODE 7, and NODE 12 final surprise count.)*
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

### Step 8 [NODE 5: cross-signal synthesis] -- Cross-Signal Synthesis
*(C-37: NODE 5 declared inline. NODE 5 produces: synthesized echo paragraph consumed by output.)*
*(C-05; IA: false-assumption-recovery; epistemic dimension: pattern-emergence)*

<=120 words. Name >=2 entries by exact label. Cross-entry pattern only.

---

### Step 9 [NODE 6: forward handover] -- Forward Handover Guidance
*(C-37: NODE 6 declared inline. NODE 6 produces: register-anchored handoff consumed by output.)*
*(C-06; C-19; IA: false-assumption-recovery; epistemic dimension: future-framing)*

T-1..T-4 register. State selection. Verify slots. Scenario and constraint specific.

---

### Step 10 [NODE 7 + NODE 8] -- Rules of Thumb
*(C-37: NODE 7 (rules) and NODE 8 (TRACE-CHECK-VERDICT) declared inline at this step.
NODE 7 produces verified rules consumed by NODE 8. NODE 8 is TRACE-CHECK-VERDICT: a named
verification token. NODE 8 = TRACE-CHECK-VERDICT is NODE 8 in the production chain.)*
*(C-07; C-24)*

<=3 rules. HIGH/MEDIUM only. Tier-match, no orphans, one-rule-per-surprise.

```
TRACE-CHECK-VERDICT: [PASS | FAIL]
  -- PASS: all tiers match; no orphan rules; one-rule-per-surprise confirmed
  -- FAIL: {rule label | expected tier from Step 4 | actual tier in entry}
```

*Forward-reader protocol (C-34): A future reader verifies this check ran by locating
the TRACE-CHECK-VERDICT token above -- no session replay required. TRACE-CHECK-VERDICT:
PASS certifies tier-match, no-orphan, one-rule-per-surprise. TRACE-CHECK-VERDICT: FAIL
records each mismatch by rule label, expected tier, and actual tier.*

---

### Step 11 [NODE 9 + NODE 10] -- Gestalt Summary Audit
*(C-37: NODE 9 (gestalt audit) and NODE 10 (GESTALT-VERDICT) declared inline.
NODE 10 = GESTALT-VERDICT is NODE 10 in the production chain.)*
*(C-26)*

*Applied to complete draft (Steps 7-10) as a single unit.*

"Could this output be described as a summary or survey of what the investigation found?"
If YES/PARTLY YES: revise, log `gestalt-summary-fail`, re-run.

```
GESTALT-VERDICT: [PASS | FAIL]
  -- PASS: output does not read as survey in aggregate; every entry is
     retroactively-visible, not included for coverage
  -- FAIL: {entry label, gestalt-summary-fail trigger reason, revision applied}
```

*Forward-reader protocol (C-34): A future reader verifies this check ran by locating
the GESTALT-VERDICT token above -- no session replay required. GESTALT-VERDICT: PASS
certifies the complete output does not pass the summary-or-survey question. GESTALT-VERDICT:
FAIL records which entries triggered gestalt-summary-fail and what revision was applied.*

---

### Step 12 [NODE 11: chain trace] -- Production Chain Trace
*(C-37: NODE 11 declared inline. NODE 11 is the chain trace itself, confirming all prior
node declarations. Nodes were declared inline at their governing steps; this trace
assembles and verifies them.)*
*(C-28; C-29; C-31)*

```
PRODUCTION CHAIN TRACE
VERIFICATION NODES INCLUDED (C-29) | DEPENDENCY GRAPH CLOSED (C-31)
NODE DECLARATIONS CONFIRMED (C-37: each node was declared at its governing step)
======================================================================

[NODE 1] typed-route prediction sort (declared: Step 1/2)
  structural qualifier: IA: false-assumption-recovery; epistemic dimension:
    prior-frame-recovery (C-30+C-32), anti-hypothesis guard (C-11), typed downstream
    destination (C-14), non-empty discard log (C-09)
  produces: typed routes (C-16), discard log (C-09+C-14)
  consumed by: NODE 2

-> [NODE 2] staged gate verdict (declared: Step 3)
  structural qualifier: Gatekeeper: adversarial-rejection-only; epistemic dimension per
    stage (novelty/opposition/specificity) at each Stage header (C-30+C-32), per-stage
    commit tokens (C-13+C-16), "We believed:" contrast gallery Stage 2 (C-18 scaffolding),
    cross-signal citation Stage 3 (C-08 prereq), gate-time floor count tracked (C-15)
  produces: SURPRISE verdicts (C-13/C-16), gate-time floor count (C-15)
  consumed by: NODE 3 (SURPRISE candidates), NODE 12 (gate-time floor count for C-36)

-> [NODE 3] comparative triage rank (declared: Step 4)
  structural qualifier: simultaneous comparison before any tier assigned (C-23),
    failure-first ordering within tier (C-22), all tiers recorded before expansion
  produces: HIGH/MEDIUM/LOW assignments (C-23), within-tier order (C-22)
  consumed by: NODE 4 entry headers (C-07), NODE 8 TRACE-CHECK-VERDICT (C-24)

-> [NODE 4] echo entry (declared: Step 7)
  structural qualifier: IA: false-assumption-recovery; epistemic dimension:
    failure-projection (C-30+C-32); 4-step naming scaffold (C-17+C-21); failure-first
    production (C-22); [CROSS: A x B] (C-08); failure field as concrete mis-design (C-18);
    named impact (C-03)
  produces: named labels (C-04), citations (C-02), impact (C-03), routes (C-14)
  consumed by: NODE 5, NODE 6, NODE 7, NODE 12 (final surprise count)

-> [NODE 5] cross-signal synthesis (declared: Step 8)
  structural qualifier: IA: false-assumption-recovery; epistemic dimension:
    pattern-emergence (C-30+C-32); >=2 named labels cited; cross-entry pattern unreachable
    from single entry (C-05 definitional line)
  produces: synthesized echo paragraph (C-05)
  consumed by: output (terminal)

-> [NODE 6] forward handover guidance (declared: Step 9)
  structural qualifier: IA: false-assumption-recovery; epistemic dimension:
    future-framing (C-30+C-32); T-1..T-4 register (C-19); slots verified (C-06)
  produces: register-anchored handoff (C-06+C-19)
  consumed by: output (terminal)

-> [NODE 7] impact-anchored rule (declared: Step 10)
  structural qualifier: tier verified against NODE 3 triage (C-24), orphan check,
    one-rule-per-surprise
  produces: verified rules (C-07+C-24)
  consumed by: NODE 8

-> [NODE 8] TRACE-CHECK-VERDICT (declared: Step 10) [C-29: chain node; C-34: forward-reader]
  structural qualifier: PASS|FAIL token with complete forward-reader protocol (C-34)
    certifying tier-match (from NODE 3), no-orphan, one-rule-per-surprise; verifiable by
    token location without session replay; mismatches recorded by label if FAIL
  produces: traceability audit result (C-24+C-29+C-34)
  consumed by: NODE 11

-> [NODE 9] gestalt audit (declared: Step 11)
  structural qualifier: IA: false-assumption-recovery applied to complete artifact as
    unit (C-26+C-30); gestalt-summary-fail logged separately from gate-fail
  produces: gestalt audit result (C-26)
  consumed by: NODE 10

-> [NODE 10] GESTALT-VERDICT (declared: Step 11) [C-29: chain node; C-34: forward-reader]
  structural qualifier: PASS|FAIL token with complete forward-reader protocol (C-34)
    certifying output-level non-survey and recording revision reasons if FAIL; verifiable
    by token location; distinct scope from NODE 8
  produces: gestalt audit result (C-26+C-29+C-34)
  consumed by: NODE 11

-> [NODE 11] production chain trace (this node, declared: Step 12)
  structural qualifier: all 12 nodes named with qualifiers (C-28); all three verification
    tokens are chain nodes (C-29); all 7 inter-criterion deps annotated (C-31); all node
    declarations confirmed against inline step declarations (C-37 universal)
  produces: closed, auditable dependency graph
  consumed by: output (terminal)

-> [NODE 12] FLOOR-VERDICT (declared: Step 13) [C-29: chain node; C-36: terminal floor;
  C-34: forward-reader; C-37: inline declaration at Step 13]
  structural qualifier: PASS|FLOOR-MISS token counting distinct surprises in NODE 4
    against floor (C-15 = 3); runs at output-close separate from gate-time check in
    NODE 2; verifiable by token location without session replay
  produces: terminal floor compliance result (C-36)
  consumed by: output (terminal); closes C-15 -> C-36 (NODE 2 -> NODE 12) loop

======================================================================
```

**REVIEWER CHALLENGE -- Dependency Graph Completeness (C-38)**

```
CLOSURE CLAIM: No inter-criterion dependency is discoverable only by reading the prompt.
Every dependency is named in this chain trace and enumerated below.
Challenge: attempt to identify any inter-criterion dependency present in this prompt that
does not appear as a named node in the trace above. The 7 dependencies below are
exhaustive -- a reviewer who finds an 8th identifies a gap in this graph.

Known dependencies (7):
  C-23 output -> C-24 (NODE 3 -> NODE 8): triage rank feeds tier-match check
  C-26 output -> C-28 (NODE 9/10 -> NODE 11): gestalt verdict is chain node
  C-24 output -> C-28 (NODE 8 -> NODE 11): traceability verdict is chain node
  C-14 output -> C-06 (NODE 4 -> NODE 6): routing feeds handover scenario
  C-17+C-21 output -> C-20 (Step 5 -> Step 6): naming scaffold feeds co-validation gate
  C-15 output -> C-36 (NODE 2 -> NODE 12): gate-time floor count feeds terminal check
  C-36 output -> C-28 (NODE 12 -> NODE 11): FLOOR-VERDICT is named chain node in trace
```

---

### Dependency Closure Enumeration *(C-33)*

*Standalone terminal block, separate from and after the chain trace.*

```
DEPENDENCY CLOSURE ENUMERATION (C-39: BIDIRECTIONAL GUARD)
=======================================================================
CONTRACT HEADER (C-39 preamble): This block enumerates all inter-criterion loops
in the production chain. Any loop chain-traceable but absent from this list is a
C-33 violation and an incompleteness in this enumeration. A reviewer verifies
completeness by reading the chain trace and checking each dependency appears here.
-----------------------------------------------------------------------
C-23 output -> C-24 (NODE 3 -> NODE 8):
  triage rank (NODE 3) required input for tier-match check (NODE 8)

C-26 output -> C-28 (NODE 9/10 -> NODE 11):
  gestalt audit verdict (NODE 10) is named chain node in NODE 11

C-24 output -> C-28 (NODE 8 -> NODE 11):
  traceability verdict (NODE 8) is named chain node in NODE 11

C-14 output -> C-06 (NODE 4 -> NODE 6):
  routing tags in entries (NODE 4) feed handover scenario selection (NODE 6)

C-17+C-21 output -> C-20 (Step 5 -> Step 6):
  naming scaffold (Step 5) is input to co-validation name-form check (Step 6)

C-15 output -> C-36 (NODE 2 -> NODE 12):
  gate-time floor count (NODE 2) compared against final surprise count at NODE 12;
  NODE 12 cannot run terminal check without gate-time baseline from NODE 2

C-36 output -> C-28 (NODE 12 -> NODE 11 trace):
  FLOOR-VERDICT (NODE 12) is named chain node; NODE 11 must name NODE 12 to satisfy C-28
-----------------------------------------------------------------------
COMPLETENESS ASSERTION (C-39 postamble): 7 loops enumerated. Any loop absent from this
enumeration that appears in the chain trace is a C-33 violation. This assertion is
falsifiable: a reviewer who locates such a loop has found a gap. This enumeration is
auditable in isolation without traversing the full chain trace.
=======================================================================
```

---

**Output**: Steps 7-12 + Dependency Closure Enumeration + Step 13. Steps 1-6 are scaffolding.

Final output sequence *(C-35: output contract -- each item carries structural label tied to
governing criterion; completeness spot-checkable without re-reading prompt body)*:

1. Echo entries (triage-ordered, failure-first within tier)
   *(satisfies C-02: source citation {name} ({namespace/skill}); C-04: named label The
   {Corrected Belief}: {Domain}; C-07: impact tier HIGH/MEDIUM/LOW in header from Step 4;
   C-08: [CROSS: A x B] annotation on every cross-signal entry; C-12: temporal anchor;
   C-14: downstream route -> {skill}; C-17: correction-encoding name; C-18: failure field
   "If next team carries old assumption, {mis-design}"; C-22: failure written first)*
2. Cross-signal synthesis
   *(satisfies C-05: >=2 named labels cited; cross-entry pattern unreachable from single
   entry; <=120 words)*
3. Forward handover guidance (register stated, slots verified)
   *(satisfies C-06: names specific scenario, constraint, source; C-19: T-1..T-4 stated)*
4. Rules of Thumb
   *(satisfies C-07: tier per rule; C-24: tier-match verified against Step 4 triage;
   no orphans; no surprise generates more than one rule; <=3 rules)*
5. TRACE-CHECK-VERDICT with forward-reader protocol
   *(satisfies C-24: traceability closure; C-29: verification chain node (NODE 8, declared
   Step 10); C-34: forward-reader rationale inline; C-37: NODE declared at governing step)*
6. GESTALT-VERDICT with forward-reader protocol
   *(satisfies C-26: gestalt audit result; C-29: verification chain node (NODE 10, declared
   Step 11); C-34: forward-reader rationale inline; C-37: NODE declared at governing step)*
7. Production chain trace with structural qualifiers (12 nodes) + REVIEWER CHALLENGE
   *(satisfies C-28: every link named with qualifier; C-29: all three verification tokens
   are chain nodes; C-31: all 7 inter-criterion deps annotated; C-37: all inline node
   declarations confirmed; C-38: falsifiable closure claim with challenge prefix)*
8. Dependency Closure Enumeration with bidirectional guard (standalone terminal block)
   *(satisfies C-33: separate from chain trace; 7 loops; spot-checkable; C-39: preamble +
   postamble guard making enumeration self-auditing in isolation)*
9. FLOOR-VERDICT (terminal minimum surprise floor check)
   *(satisfies C-36: separate from gate-time check; named PASS|FLOOR-MISS artifact;
   C-29: verification chain node (NODE 12, declared Step 13); C-37: NODE declared inline)*

---

### Step 13 [NODE 12: FLOOR-VERDICT] -- Terminal Minimum Surprise Floor Check
*(C-37: FLOOR-VERDICT is NODE 12 in the production chain. This inline declaration at the
governing step means a model executing Step 13 in isolation sees the node assignment
without consulting the terminal chain trace in Step 12. The inline declaration at Step 12
(where NODE 12 appears in the chain trace) confirms this assignment; it does not create it.)*
*(C-36)*

Count distinct surprises in final output (Item 1 entries). Compare to floor (3).

```
FLOOR-VERDICT: [PASS | FLOOR-MISS]
  -- PASS: distinct surprise count >= 3 confirmed in final output
  -- FLOOR-MISS: {count} surprises present; floor shortfall: {3 - count} required
```

FLOOR-MISS is a named output artifact. Do not suppress it.

*Forward-reader protocol (C-34): A future reader verifies this check ran by locating
the FLOOR-VERDICT token above in the output -- no session replay required. FLOOR-VERDICT:
PASS certifies that the final output contains at least 3 distinct surprises after all
post-gate revisions are complete. FLOOR-VERDICT: FLOOR-MISS certifies the count found
and the shortfall, enabling a reader to determine the sub-floor state without re-executing
the prompt.*

*(C-36: This check is separate from and after the gate-time floor check in Step 3 Stage 2.
Gate-time verifies >=3 candidates reach CONTRADICTION FOUND. This terminal check verifies
>=3 distinct surprises present in the finalized output after gestalt audit and revisions.)*

---

## Predicted Scores (v11 rubric)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|:----:|:----:|:----:|:----:|:----:|
| C-01..C-36 | PASS | PASS | PASS | PASS | PASS |
| C-37 | PASS | PARTIAL | PARTIAL | PARTIAL | PASS |
| C-38 | PASS | PASS | PASS | PASS | PASS |
| C-39 | PASS | PASS | PASS | PASS | PASS |

Notes:
- V-01: C-37 PASS via single inline declaration in Step 13; C-38/C-39 inherited from R10 V-05.
- V-02: C-37 PARTIAL -- NODE 12 appears only in chain trace, not inline at Step 13; C-38
  PASS via challenge-prefix block; C-39 PASS inherited.
- V-03: C-37 PARTIAL -- same gap as V-02; C-38 PASS inherited; C-39 PASS via bidirectional guard.
- V-04: C-37 PARTIAL -- no inline node declaration; C-38 PASS (conversational challenge);
  C-39 PASS (conversational bidirectional guard).
- V-05: C-37 PASS universally -- every step declares its NODE inline; C-38 PASS
  (challenge-prefix); C-39 PASS (bidirectional). All three new criteria satisfied.

**Discriminating pairs:**
- V-01 vs V-02: C-37 PASS vs PARTIAL; isolates inline-node-at-step-13 value
- V-02 vs V-03: C-38 challenge vs inherited; C-39 bidirectional vs inherited; isolates format
- V-04 vs V-02: register (conversational vs formal); C-38/C-39 both PASS; isolates register effect
- V-05 vs V-01: C-37 universal vs point-fix; C-38 challenge vs assertion; C-39 bidirectional vs single
