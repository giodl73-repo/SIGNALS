---
skill: quest-variate
skill_target: topic-echo
date: 2026-03-15
round: 10
rubric: v10
rubric_max: 165
---

# Variations: `topic:echo` -- Round 10

**Rubric:** v10 | **Date:** 2026-03-15

---

## Design Context

R9 differentiating evidence: two structural patterns from R9 V-05 were observable but not
yet formalized as criteria.

1. **R9 V-05 output-contract label gap (-> C-35)**: R9 V-05 introduced a numbered final
   output sequence (8 items) that listed production phases in order. But each item named
   only the phase -- no structural label tied to its governing criterion. "Echo entries
   (triage-ordered, failure-first within tier)" tells a reader the shape of the item but
   not which criteria certify its structure. A reviewer cannot spot-check completeness
   without re-reading the prompt body to recall which step governs each output. C-35 closes
   this: each output item carries a per-item criterion label in parentheses, making the
   contract machine-checkable from the output line alone.

2. **R9 V-05 floor-check artifact gap (-> C-36)**: R9 V-05 already added a terminal floor
   check at output-close: "Minimum surprise floor check *(C-15)*: if fewer than 3 distinct
   surprises in final output, note the floor-miss before closing. Do not suppress it." This
   is prose in the output instructions block -- not a named artifact. A floor-miss is
   instructed to be "noted" but the form of that note is unspecified. Post-gate revisions
   that silently drop a surprise produce no verifiable token. C-36 closes this: the
   terminal check produces a named verdict token (FLOOR-VERDICT) with explicit PASS/FLOOR-
   MISS states, verifiable by token location -- same audit protocol as TRACE-CHECK-VERDICT
   and GESTALT-VERDICT.

**Variation plan:**

- V-01: C-35 only -- per-item criterion labels in output contract; C-36 stays at R9 V-05
  prose form (no named artifact)
- V-02: C-36 only -- FLOOR-VERDICT named token replaces prose floor check; output contract
  has no per-item criterion labels
- V-03: C-35 structural variant -- output contract declared as preamble (front-loaded before
  execution steps) rather than postamble; tests whether positional prominence affects
  execution fidelity
- V-04: C-35 + C-36 combined; chain trace and dep enumeration NOT updated (FLOOR-VERDICT
  absent from NODE list and loop enumeration; C-29/C-31/C-33 at PARTIAL)
- V-05: Full synthesis -- C-35 + C-36 + NODE 12 in chain trace (C-29) + 7 dep loops in
  enumeration (C-31/C-33) + FLOOR-VERDICT forward-reader protocol (potential ES for v11)

**Discriminating pairs:**
- V-01 vs V-05: C-36 FAIL vs PASS; isolates floor-verdict token value
- V-02 vs V-05: C-35 FAIL vs PASS; isolates output contract label value
- V-03 vs V-01: C-35 PASS both; position front vs back; isolates contract prominence effect
- V-04 vs V-05: C-29/C-31/C-33 PARTIAL vs PASS; isolates chain closure value for NODE 12

---

## V-01 -- Single-axis: Per-item criterion labels in output contract (C-35)

**Variation axis:** Output contract structure. Every item in the final output sequence
carries a parenthetical structural label naming the governing criterion or criteria. The
label is in the contract declaration itself -- a reviewer spot-checks completeness by
reading the contract alone, without re-reading the prompt body.

**Hypothesis:** R9 V-05 established the numbered output sequence, partially satisfying
C-35 intent. The gap: a reviewer reading item 5 ("TRACE-CHECK-VERDICT with forward-reader
protocol") cannot know without re-reading Step 10 that this item certifies C-24, C-29, and
C-34. Adding per-item criterion labels converts the list from a production checklist into
an auditable contract. Predicted: C-35 PASS; C-36 FAIL (prose check present, no token).

**Builds on:** R9 V-05 -- all 26 aspirational criteria (C-09..C-34) active.

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
false assumption (C-17). Derives consequence by asking "What would the next team build
wrong?" (C-18, C-22). The IA is the author of implication; the Gatekeeper is the author of
rejection.

Sub-step co-activation shorthand *(C-30, C-32)*: `IA: false-assumption-recovery; epistemic
dimension: {name}` at every invocation.

Defined dimensions:

| Step | Epistemic Dimension | Why here |
|------|---------------------|----------|
| 2 | prior-frame-recovery | Recovering what was actually believed, not what spec asserts |
| 5 | belief-inversion | Deriving correction-encoding name by inverting the false assumption |
| 6 | correction-integrity | Verifying both structural form checks encode the correction |
| 7 | failure-projection | Anchoring entry in projected mis-design; failure is load-bearing |
| 8 | pattern-emergence | What only emerges when entries are read together |
| 9 | future-framing | Translating findings into actionable guidance for a future builder |

Active: Steps 2, 5, 6, 7, 8, 9.

**Gatekeeper**
*First invocation: Step 3.*
`Gatekeeper: adversarial-rejection-only; epistemic dimension: {stage-label}` per stage.

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

Discard log *(C-09; IA: false-assumption-recovery; epistemic dimension:
prior-frame-recovery)*: every non-gate item, route type, reason, destination. Non-empty.

---

### Step 3 -- Multi-Stage Epistemic Gate
*(Gatekeeper: adversarial-rejection-only; C-13; C-15; C-16)*

```
GATEKEEPER: adversarial-rejection-only -- active through end of Stage 3.
```

**Anti-Pattern Catalog** *(C-13)*: CONFIRMATION | RESTATEMENT | ISOLATED-FINDING
**Gate format** *(C-16)*: `VERDICT: SURPRISE | CUT -- {label}`

**Stage 1 -- Prediction Test**
*(Gatekeeper: adversarial-rejection-only; epistemic dimension: novelty -- separating
investigation-emergent findings from outcomes predictable from original design materials)*

"Would a competent practitioner have predicted this from first principles?"
`PREDICTABLE` -> `topic-story` | `UNPREDICTABLE` -> Stage 2
**Commit**: `Stage 1: [{item}] -> [PREDICTABLE | UNPREDICTABLE]`

**Stage 2 -- Contradiction Test**
*(Gatekeeper: adversarial-rejection-only; epistemic dimension: opposition -- separating
genuine contradiction of a held belief from findings merely notable or unusual)*

```
We believed: {falsifiable assumption -- names a specific held belief}
VALID: {genuine falsification -- names belief and contradiction}
INVALID (absence-of-consideration): notes absence, not a falsifiable proposition
INVALID (sentiment-reaction): records team response, not a prior belief state
INVALID (hedge-uncertainty): names a gap, not a held belief
```

Floor *(C-15)*: >=3 must reach CONTRADICTION FOUND. If fewer, record floor-miss.
`NO CONTRADICTION` -> `topic-report` | `CONTRADICTION FOUND` -> Stage 3
**Commit**: `Stage 2: [{item}] -> [NO CONTRADICTION | CONTRADICTION FOUND]`

**Stage 3 -- Attribution Test**
*(Gatekeeper: adversarial-rejection-only; epistemic dimension: specificity -- separating
traceable cross-signal findings from single-artifact findings)*

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

Begin from failure *(C-22; IA: false-assumption-recovery; epistemic dimension:
failure-projection)*: anchor mis-design first.

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
the TRACE-CHECK-VERDICT token above in the output -- no session replay required.
TRACE-CHECK-VERDICT: PASS certifies that (1) every rule's tier matches the triage tier from
Step 4, (2) no rule is an orphan without a named surprise source, and (3) no surprise
generated more than one rule. TRACE-CHECK-VERDICT: FAIL records each mismatch by rule label,
expected tier, and actual tier, enabling audit without re-executing the prompt.*

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
certifies the complete output does not pass the summary-or-survey audit question from
Step 11. GESTALT-VERDICT: FAIL records which entries triggered gestalt-summary-fail and
what revision was applied, enabling audit without the pre-revision draft.*

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
    cross-signal citation Stage 3 (C-08 prereq), gate-time floor tracked (C-15)
  produces: SURPRISE verdicts (C-13/C-16), gate-time floor count (C-15)
  consumed by: NODE 3

-> [NODE 3] comparative triage rank
  structural qualifier: simultaneous comparison (C-23), failure-first ordering (C-22),
    all tiers recorded before expansion
  produces: HIGH/MEDIUM/LOW assignments (C-23), within-tier order (C-22)
  consumed by: NODE 4 (entry headers, C-07), NODE 8 (tier-match check, C-24)

-> [NODE 4] echo entry
  structural qualifier: IA: false-assumption-recovery; epistemic dimension:
    failure-projection (C-30+C-32); 4-step naming scaffold (C-17+C-21); failure-first
    production (C-22); [CROSS: A x B] (C-08); failure field as concrete mis-design (C-18);
    named impact (C-03)
  produces: named labels (C-04), citations (C-02), impact (C-03), routes (C-14)
  consumed by: NODE 5, NODE 6, NODE 7

-> [NODE 5] cross-signal synthesis
  structural qualifier: IA: false-assumption-recovery; epistemic dimension:
    pattern-emergence (C-30+C-32); >=2 named labels cited; cross-entry pattern unreachable
    from single entry (C-05 definitional line)
  produces: synthesized echo paragraph (C-05)
  consumed by: output

-> [NODE 6] forward handover guidance
  structural qualifier: IA: false-assumption-recovery; epistemic dimension:
    future-framing (C-30+C-32); T-1..T-4 register (C-19); slots verified (C-06)
  produces: register-anchored handoff (C-06+C-19)
  consumed by: output

-> [NODE 7] impact-anchored rule
  structural qualifier: tier verified against NODE 3 triage (C-24), orphan check,
    one-rule-per-surprise
  produces: verified rules (C-07+C-24)
  consumed by: NODE 8

-> [NODE 8] TRACE-CHECK-VERDICT [C-29; C-34: forward-reader protocol inline]
  structural qualifier: PASS|FAIL token with complete forward-reader protocol; verifiable
    by token location; mismatches recorded by label if FAIL
  produces: traceability audit result (C-24+C-29+C-34)
  consumed by: NODE 11

-> [NODE 9] gestalt audit
  structural qualifier: IA applied to complete artifact as unit (C-26+C-30); gestalt-fail
    logged separately from gate-fail
  produces: gestalt audit result (C-26)
  consumed by: NODE 10

-> [NODE 10] GESTALT-VERDICT [C-29; C-34: forward-reader protocol inline]
  structural qualifier: PASS|FAIL token with complete forward-reader protocol; verifiable
    by token location; distinct scope from NODE 8
  produces: gestalt audit result (C-26+C-29+C-34)
  consumed by: NODE 11

-> [NODE 11] production chain trace (this node)
  structural qualifier: all nodes named with qualifiers (C-28); verification verdicts are
    chain nodes (C-29); all inter-criterion deps annotated (C-31)
  produces: closed, auditable dependency graph
  consumed by: output

======================================================================
Dependency closure (C-31):
  C-23 output -> C-24 (NODE 3 -> NODE 8): triage rank feeds tier-match check
  C-26 output -> C-28 (NODE 9/10 -> NODE 11): gestalt verdict is chain node
  C-24 output -> C-28 (NODE 8 -> NODE 11): traceability verdict is chain node
  C-14 output -> C-06 (NODE 4 -> NODE 6): routing feeds handover scenario
  C-17+C-21 output -> C-20 (Step 5 -> Step 6): naming scaffold feeds co-validation gate
```

---

### Dependency Closure Enumeration (C-33)

```
DEPENDENCY CLOSURE ENUMERATION
================================
C-23 output -> C-24 (NODE 3 -> NODE 8)
C-26 output -> C-28 (NODE 9/10 -> NODE 11)
C-24 output -> C-28 (NODE 8 -> NODE 11)
C-14 output -> C-06 (NODE 4 -> NODE 6)
C-17+C-21 output -> C-20 (Step 5 -> Step 6)
================================
5 loops enumerated.
```

**Output**: Steps 7-12 + Dependency Closure Enumeration. Steps 1-6 are scaffolding.

Final output sequence *(C-35: output contract -- each item carries structural label tied
to governing criterion; completeness spot-checkable without re-reading prompt body)*:

1. Echo entries (triage-ordered, failure-first within tier)
   *(satisfies C-02: source citation {name} ({namespace/skill}); C-04: named label
   The {Corrected Belief}: {Domain}; C-07: impact tier in header from Step 4; C-08: [CROSS]
   annotation; C-12: temporal anchor; C-14: downstream route; C-17: correction-encoding
   name; C-18: failure field as concrete mis-design; C-22: failure-first production)*
2. Cross-signal synthesis
   *(satisfies C-05: >=2 named labels cited; cross-entry pattern; unreachable from single
   entry; <=120 words)*
3. Forward handover guidance (register stated, slots verified)
   *(satisfies C-06: specific scenario + constraint + source; C-19: T-1..T-4 selection)*
4. Rules of Thumb
   *(satisfies C-07: tier per rule; C-24: tier-match verified against Step 4 triage)*
5. TRACE-CHECK-VERDICT with forward-reader protocol
   *(satisfies C-24: traceability closure; C-29: verification chain node; C-34: forward-
   reader rationale inline)*
6. GESTALT-VERDICT with forward-reader protocol
   *(satisfies C-26: gestalt audit result; C-29: verification chain node; C-34: forward-
   reader rationale inline)*
7. Production chain trace with structural qualifiers
   *(satisfies C-28: full-chain; C-29: verification nodes included; C-31: dep graph closed)*
8. Dependency Closure Enumeration (standalone terminal block)
   *(satisfies C-33: spot-checkable dep list, separate from chain trace)*

Minimum surprise floor check *(C-15)*: if fewer than 3 distinct surprises in final output,
note the floor-miss before closing. Do not suppress it.

---

## V-02 -- Single-axis: Named verdict token for terminal floor check (C-36)

**Variation axis:** Floor compliance artifact form. The terminal floor check produces a
named FLOOR-VERDICT token (PASS/FLOOR-MISS) parallel to TRACE-CHECK-VERDICT and GESTALT-
VERDICT. A floor-miss is a named artifact, not an unspecified prose note.

**Hypothesis:** R9 V-05's prose floor check satisfies C-15 at gate time but not C-36 at
output-close. The prose instruction does not specify the form of the note, so a model may
suppress a floor-miss or embed it ambiguously. A named token with explicit states produces
a verifiable artifact. Predicted: C-36 PASS; C-35 FAIL (output list without per-item labels).

**Builds on:** R9 V-05 -- all 26 aspirational criteria (C-09..C-34) active.

---

### Prompt Body

You are running `/quest:topic echo` for the topic: {topic}.

All essential signals are in hand. Your task: surface the genuine surprises -- findings that
only became visible in retrospect, from cross-signal tension, that no competent practitioner
would have predicted before gathering evidence.

Not a summary. Not a survey of discoveries. An echo: the signal that comes back that you
didn't send.

---

### Roles *(C-25; C-30; C-32)*

**Institutional Archaeologist (IA)** -- *First invocation: Step 2.*
Function: Recovers false assumptions -- what a future team would carry as truth. Frames
every surprise as a correction to a false assumption (C-17). Derives consequence: "What
would the next team build wrong?" (C-18, C-22).

Sub-step shorthand: `IA: false-assumption-recovery; epistemic dimension: {name}`

| Step | Epistemic Dimension | Why here |
|------|---------------------|----------|
| 2 | prior-frame-recovery | Recovering what was actually believed |
| 5 | belief-inversion | Inverting the false assumption to derive the name |
| 6 | correction-integrity | Verifying both form checks encode the correction |
| 7 | failure-projection | Anchoring in projected mis-design |
| 8 | pattern-emergence | What only emerges across entries |
| 9 | future-framing | Translating to actionable guidance |

**Gatekeeper** -- *First invocation: Step 3.*
Shorthand: `Gatekeeper: adversarial-rejection-only; epistemic dimension: {stage-label}`

```
GATEKEEPER -- FUNCTION DECLARATION (C-27)
Function:      Adversarial rejection -- predictability test + cross-signal requirement.
Not-function:  Future-reader framing (IA). Not-function: Thematic synthesis.
Role boundary: Gatekeeper verdicts final.
```

---

### Step 1 -- Read Signal Record *(C-10; C-12)*

All namespaces. >=3 floor. Record: namespaces, count, date range.

---

### Step 2 -- Pre-Write Prediction Sort
*(IA: false-assumption-recovery; epistemic dimension: prior-frame-recovery; C-16; C-14;
C-11; C-09)*

Routes: `topic-story` | `topic-report` | `gate-pipeline`
Anti-hypothesis guard *(C-11)*. Discard log *(C-09)* with destinations. Non-empty.

---

### Step 3 -- Multi-Stage Epistemic Gate *(Gatekeeper; C-13; C-15; C-16)*

Anti-Pattern Catalog: CONFIRMATION | RESTATEMENT | ISOLATED-FINDING
Gate format: `VERDICT: SURPRISE | CUT -- {label}`

**Stage 1** *(adversarial-rejection-only; epistemic dimension: novelty)*
`PREDICTABLE` -> `topic-story` | `UNPREDICTABLE` -> Stage 2
**Commit**: `Stage 1: [{item}] -> [PREDICTABLE | UNPREDICTABLE]`

**Stage 2** *(adversarial-rejection-only; epistemic dimension: opposition)*
```
We believed: {falsifiable assumption}
VALID: {genuine falsification}
INVALID (absence-of-consideration) / INVALID (sentiment-reaction) / INVALID (hedge-uncertainty)
```
Floor *(C-15)*: >=3 CONTRADICTION FOUND.
`NO CONTRADICTION` -> `topic-report` | `CONTRADICTION FOUND` -> Stage 3
**Commit**: `Stage 2: [{item}] -> [NO CONTRADICTION | CONTRADICTION FOUND]`

**Stage 3** *(adversarial-rejection-only; epistemic dimension: specificity)*
`SINGLE-ARTIFACT` -> `topic-report` | `CROSS-SIGNAL` -> SURPRISE
**Commit**: `Stage 3: [{item}] -> [SINGLE-ARTIFACT | CROSS-SIGNAL] -- sources: [{a1}, {a2}]`

---

### Step 4 -- Pre-Write Impact Triage *(C-23; C-22)*

Comparative. HIGH | MEDIUM | LOW. Failure-first. All before expansion.

---

### Step 5 -- Naming Scaffold *(C-17; C-21; IA: belief-inversion)*

1. Old belief. 2. Correction. 3. Domain. 4. Label: `The {Corrected Belief}: {Domain}`.

---

### Step 6 -- Pre-Expansion Co-Validation Gate *(C-20; IA: correction-integrity)*

Both VALID required. Either failing blocks expansion.
- Name form *(C-17)*: -> VALID / INVALID
- Failure field *(C-18)*: -> VALID / INVALID

---

### Step 7 -- Write Echo Entries
*(IA: failure-projection; C-02..C-04; C-08; C-12; C-14; C-17; C-18; C-22)*

Begin from failure *(C-22)*. Then: name, source, [CROSS], temporal, belief, surprise,
mis-design *(C-18)*, impact *(C-03)*, route *(C-14)*.

---

### Step 8 -- Cross-Signal Synthesis *(C-05; IA: pattern-emergence)*

<=120 words. >=2 named labels. Cross-entry pattern only.

---

### Step 9 -- Forward Handover *(C-06; C-19; IA: future-framing)*

T-1..T-4. State selection. Verify slots.

---

### Step 10 -- Rules of Thumb *(C-07; C-24)*

<=3. HIGH/MEDIUM only. Tier-match, no orphans, one-per-surprise.

```
TRACE-CHECK-VERDICT: [PASS | FAIL]
  -- PASS: tiers match; no orphans; one-rule-per-surprise confirmed
  -- FAIL: {rule label | expected tier | actual tier}
```

*Forward-reader protocol (C-34): Verifiable by locating TRACE-CHECK-VERDICT token. PASS
certifies tier-match, no-orphan, one-rule-per-surprise. FAIL records each mismatch.*

---

### Step 11 -- Gestalt Summary Audit *(C-26)*

```
GESTALT-VERDICT: [PASS | FAIL]
  -- PASS: output does not read as survey in aggregate
  -- FAIL: {entry, gestalt-summary-fail reason, revision applied}
```

*Forward-reader protocol (C-34): Verifiable by locating GESTALT-VERDICT token. PASS
certifies complete output does not pass the summary-or-survey question. FAIL records
revision decisions.*

---

### Step 12 -- Production Chain Trace *(C-28; C-29; C-31)*

[NODE 1..NODE 11 chain identical to V-01 Step 12]

```
[NODE 1] typed-route prediction sort
  structural qualifier: IA+prior-frame-recovery (C-30+C-32), anti-hypothesis guard (C-11),
    typed destinations (C-14), non-empty discard log (C-09)

-> [NODE 2] staged gate verdict
  structural qualifier: Gatekeeper+dimension per stage (C-30+C-32), commit tokens
    (C-13+C-16), "We believed:" gallery (C-18), cross-signal citation (C-08), floor (C-15)

-> [NODE 3] comparative triage rank
  structural qualifier: simultaneous comparison (C-23), failure-first (C-22)

-> [NODE 4] echo entry
  structural qualifier: IA+failure-projection (C-30+C-32); scaffold (C-17+C-21);
    failure-first (C-22); [CROSS] (C-08); failure field (C-18); impact (C-03)

-> [NODE 5] cross-signal synthesis
  structural qualifier: IA+pattern-emergence (C-30+C-32); >=2 labels; C-05

-> [NODE 6] forward handover
  structural qualifier: IA+future-framing (C-30+C-32); T-1..T-4 (C-19); verified (C-06)

-> [NODE 7] impact-anchored rule
  structural qualifier: tier vs NODE 3 (C-24), orphan check, one-per-surprise

-> [NODE 8] TRACE-CHECK-VERDICT [C-29; C-34]
  structural qualifier: PASS|FAIL with forward-reader protocol; token-verifiable

-> [NODE 9] gestalt audit
  structural qualifier: IA+complete-unit (C-26+C-30); gestalt-fail separate

-> [NODE 10] GESTALT-VERDICT [C-29; C-34]
  structural qualifier: PASS|FAIL with forward-reader protocol; token-verifiable

-> [NODE 11] production chain trace (this node)
  structural qualifier: all nodes named with qualifiers (C-28); verification nodes as
    chain nodes (C-29); all deps annotated (C-31)

Dependency closure (C-31):
  C-23 -> C-24 (NODE 3 -> NODE 8)
  C-26 -> C-28 (NODE 9/10 -> NODE 11)
  C-24 -> C-28 (NODE 8 -> NODE 11)
  C-14 -> C-06 (NODE 4 -> NODE 6)
  C-17+C-21 -> C-20 (Step 5 -> Step 6)
```

---

### Dependency Closure Enumeration (C-33)

```
DEPENDENCY CLOSURE ENUMERATION
================================
C-23 output -> C-24 (NODE 3 -> NODE 8)
C-26 output -> C-28 (NODE 9/10 -> NODE 11)
C-24 output -> C-28 (NODE 8 -> NODE 11)
C-14 output -> C-06 (NODE 4 -> NODE 6)
C-17+C-21 output -> C-20 (Step 5 -> Step 6)
================================
5 loops enumerated.
```

**Output**: Steps 7-12 + Dependency Closure Enumeration. Steps 1-6 are scaffolding.

Final output sequence:
1. Echo entries (triage-ordered, failure-first within tier)
2. Cross-signal synthesis
3. Forward handover guidance (register stated)
4. Rules of Thumb
5. TRACE-CHECK-VERDICT with forward-reader protocol
6. GESTALT-VERDICT with forward-reader protocol
7. Production chain trace
8. Dependency Closure Enumeration (standalone terminal block)

### Step 13 -- Terminal Minimum Surprise Floor Check *(C-36)*

Count distinct surprises in final output. Compare to floor (3).

```
FLOOR-VERDICT: [PASS | FLOOR-MISS]
  -- PASS: distinct surprise count >= 3 confirmed in final output
  -- FLOOR-MISS: {count} surprises present; shortfall: {3 - count} required
```

FLOOR-MISS is a named output artifact. If FLOOR-MISS: note the shortfall. Do not suppress.

*(C-36: This check is separate from and after the gate-time floor check in Step 3 Stage 2.
Gate-time verifies candidate count entering the gate. This verifies count in the finalized
output -- post-gate revisions that drop a surprise are caught here, not at the gate.)*

9. FLOOR-VERDICT (terminal floor compliance)

---

## V-03 -- Structural variant: Output contract as preamble (C-35 position test)

**Variation axis:** Output contract position. The numbered final output sequence with
per-item criterion labels is declared at the TOP of the prompt (before role definitions and
execution steps), rather than after the chain trace. Tests whether front-loading the
contract produces higher execution fidelity.

**Hypothesis:** In R9 V-05, the output contract appears after 12 execution steps and the
dep enumeration block -- by the time a model reaches it, the output is nearly finalized and
the contract becomes a post-hoc checklist rather than a governing spec. If declared first,
the contract acts as a structural constraint shaping execution from step 1: a model writing
echo entries already knows each entry must satisfy C-02/C-04/C-07/C-08/C-12/C-14/C-17/
C-18/C-22. Front-loading may improve completeness adherence at earlier steps. Trade-off:
the reader must hold the contract in memory while reading execution steps.

**Builds on:** R9 V-05 baseline + C-35 front-loaded. C-36 stays at prose form (FAIL).

---

### Prompt Body

You are running `/quest:topic echo` for the topic: {topic}.

---

### Output Contract *(C-35: declared before execution; machine-checkable without re-reading
prompt body; each item carries structural label tied to governing criterion)*

The following is the complete expected output in production order. Verify all items present
at output-close.

**Item 1: Echo entries** (triage-ordered, failure-first within tier)
*(C-02: source citation {name} ({namespace/skill}); C-04: named label The {Corrected
Belief}: {Domain}; C-07: impact tier HIGH/MEDIUM/LOW from Step 4; C-08: [CROSS: A x B]
on every cross-signal entry; C-12: temporal anchor (round or date); C-14: route ->
{skill or namespace}; C-17: correction-encoding name; C-18: failure field "If next team
carries old assumption, {mis-design}"; C-22: failure written first)*

**Item 2: Cross-signal synthesis**
*(C-05: >=2 named labels cited by exact label; cross-entry pattern unreachable from single
entry; <=120 words)*

**Item 3: Forward handover guidance**
*(C-06: names specific scenario, constraint, source; C-19: T-1..T-4 register stated before
writing; slots verified)*

**Item 4: Rules of Thumb**
*(C-07: tier per rule [HIGH|MEDIUM]; C-24: tier matches Step 4 triage; no orphan rules; no
surprise generates more than one rule; <=3 rules; HIGH/MEDIUM only)*

**Item 5: TRACE-CHECK-VERDICT with forward-reader protocol**
*(C-24: traceability closure; C-29: verification chain node; C-34: forward-reader rationale
stating what PASS certifies and what FAIL records)*

**Item 6: GESTALT-VERDICT with forward-reader protocol**
*(C-26: gestalt audit; C-29: verification chain node; C-34: forward-reader rationale)*

**Item 7: Production chain trace with structural qualifiers**
*(C-28: every link named with qualifier; C-29: verification nodes are chain nodes; C-31:
all inter-criterion deps annotated)*

**Item 8: Dependency Closure Enumeration** (standalone terminal block)
*(C-33: separate from chain trace; {source criterion} -> {consuming criterion} ({node});
spot-checkable without traversal)*

---

All execution steps below produce the output items declared above.

Not a summary. Not a survey of discoveries. An echo: the signal that comes back that you
didn't send.

---

### Roles *(C-25; C-30; C-32)*

**Institutional Archaeologist (IA)** -- *First invocation: Step 2.*
Function: Recovers false assumptions. Frames every surprise as a correction to a false
assumption (C-17). Derives consequence: "What would the next team build wrong?" (C-18, C-22).

`IA: false-assumption-recovery; epistemic dimension: {name}` at every invocation.

| Step | Epistemic Dimension | Why here |
|------|---------------------|----------|
| 2 | prior-frame-recovery | What was actually believed, not what spec asserts |
| 5 | belief-inversion | Deriving name by inverting the false assumption |
| 6 | correction-integrity | Verifying both form checks encode the correction |
| 7 | failure-projection | Anchoring in projected mis-design |
| 8 | pattern-emergence | What only emerges across entries |
| 9 | future-framing | Translating to actionable guidance |

**Gatekeeper** -- *First invocation: Step 3.*
`Gatekeeper: adversarial-rejection-only; epistemic dimension: {stage-label}` per stage.

```
GATEKEEPER -- FUNCTION DECLARATION (C-27)
Function:      Adversarial rejection -- predictability + cross-signal requirement.
Not-function:  Future-reader framing (IA). Not-function: Thematic synthesis.
Role boundary: Gatekeeper verdicts final.
```

---

### Step 1 -- Read Signal Record *(C-10; C-12)*

All namespaces. >=3 floor. Namespaces, count, date range.

---

### Step 2 -- Pre-Write Prediction Sort
*(IA: false-assumption-recovery; epistemic dimension: prior-frame-recovery; C-16; C-14;
C-11; C-09)*

Routes: `topic-story` | `topic-report` | `gate-pipeline`
Anti-hypothesis guard *(C-11)*. Discard log *(C-09)* with destinations. Non-empty.

---

### Step 3 -- Multi-Stage Epistemic Gate *(Gatekeeper; C-13; C-15; C-16)*

Anti-Pattern Catalog: CONFIRMATION | RESTATEMENT | ISOLATED-FINDING
Gate format: `VERDICT: SURPRISE | CUT -- {label}`

**Stage 1** *(adversarial-rejection-only; epistemic dimension: novelty)*
Commit: `Stage 1: [{item}] -> [PREDICTABLE | UNPREDICTABLE]`

**Stage 2** *(adversarial-rejection-only; epistemic dimension: opposition)*
`We believed:` / VALID / INVALID gallery. Floor *(C-15)*: >=3 CONTRADICTION FOUND.
Commit: `Stage 2: [{item}] -> [NO CONTRADICTION | CONTRADICTION FOUND]`

**Stage 3** *(adversarial-rejection-only; epistemic dimension: specificity)*
Commit: `Stage 3: [{item}] -> [SINGLE-ARTIFACT | CROSS-SIGNAL] -- sources: [{a1}, {a2}]`

---

### Step 4 -- Pre-Write Impact Triage *(C-23; C-22)*

Comparative. HIGH | MEDIUM | LOW. Failure-first. All before expansion.

---

### Step 5 -- Naming Scaffold *(C-17; C-21; IA: belief-inversion)*

1. Old belief. 2. Correction. 3. Domain. 4. Label.

---

### Step 6 -- Pre-Expansion Co-Validation Gate *(C-20; IA: correction-integrity)*

Name form + failure field both VALID. Blocks expansion if either fails.

---

### Step 7 -- Write Echo Entries
*(IA: failure-projection; satisfies Output Contract Item 1)*

Begin from failure *(C-22)*. Name, source, [CROSS] *(C-08)*, temporal *(C-12)*, belief,
surprise, mis-design *(C-18)*, impact *(C-03)*, route *(C-14)*. See Item 1 criteria.

---

### Step 8 -- Cross-Signal Synthesis *(C-05; IA: pattern-emergence -- satisfies Item 2)*

---

### Step 9 -- Forward Handover *(C-06; C-19; IA: future-framing -- satisfies Item 3)*

---

### Step 10 -- Rules of Thumb *(C-07; C-24 -- satisfies Items 4 and 5)*

```
TRACE-CHECK-VERDICT: [PASS | FAIL]
  -- PASS: tiers match; no orphans; one-rule-per-surprise confirmed
  -- FAIL: {rule label | expected tier | actual tier}
```

*Forward-reader protocol (C-34 -- satisfies Item 5): Verifiable by token location. PASS
certifies tier-match, no-orphan, one-rule-per-surprise. FAIL records each mismatch.*

---

### Step 11 -- Gestalt Summary Audit *(C-26 -- satisfies Item 6)*

```
GESTALT-VERDICT: [PASS | FAIL]
  -- PASS: output does not read as survey in aggregate
  -- FAIL: {entry, gestalt-summary-fail reason, revision applied}
```

*Forward-reader protocol (C-34 -- satisfies Item 6): Verifiable by token location. PASS
certifies complete output does not pass summary-or-survey question. FAIL records revisions.*

---

### Step 12 -- Production Chain Trace *(C-28; C-29; C-31 -- satisfies Item 7)*

[NODE 1..NODE 11, identical structure to V-01 Step 12]

---

### Dependency Closure Enumeration *(C-33 -- satisfies Item 8)*

[5-loop enumeration identical to V-01]

Minimum surprise floor check *(C-15)*: if fewer than 3 distinct surprises in final output,
note the floor-miss before closing. Do not suppress it.

---

## V-04 -- Combined: C-35 + C-36 without chain trace extension

**Variation axes:** C-35 (per-item criterion labels) + C-36 (FLOOR-VERDICT token). Chain
trace retains NODE 1..11 only -- FLOOR-VERDICT is NOT added as NODE 12 and the two new
C-36-related dep loops are absent from the enumeration.

**Hypothesis:** C-35 and C-36 can be added as surface-level additions without extending
the chain. The contract is auditable (C-35 satisfied) and the floor-verdict is a named
artifact (C-36 satisfied). But FLOOR-VERDICT is not a chain node (C-29 PARTIAL) and the
dep enumeration lacks the C-15->C-36 and C-36->C-28 loops (C-31/C-33 PARTIAL). Tests
whether the structural gap is observable in execution or only at scoring time.

**Builds on:** R9 V-05 + C-35 + C-36 added without chain closure.

---

### Prompt Body

You are running `/quest:topic echo` for the topic: {topic}.

All essential signals are in hand. Surface the genuine surprises -- findings only visible in
retrospect, from cross-signal tension, that no competent practitioner would have predicted.

Not a summary. An echo: the signal that comes back that you didn't send.

---

### Roles *(C-25; C-30; C-32)*

**Institutional Archaeologist (IA)** -- *First invocation: Step 2.*
Function: Recovers false assumptions. Frames surprises as corrections (C-17). Derives
consequence: "What would the next team build wrong?" (C-18, C-22).
Shorthand: `IA: false-assumption-recovery; epistemic dimension: {name}`

| Step | Epistemic Dimension |
|------|---------------------|
| 2 | prior-frame-recovery |
| 5 | belief-inversion |
| 6 | correction-integrity |
| 7 | failure-projection |
| 8 | pattern-emergence |
| 9 | future-framing |

**Gatekeeper** -- *First invocation: Step 3.*
Shorthand: `Gatekeeper: adversarial-rejection-only; epistemic dimension: {stage-label}`

```
GATEKEEPER -- FUNCTION DECLARATION (C-27)
Function: Adversarial rejection -- predictability + cross-signal requirement.
Not-function: Future-reader framing. Not-function: Thematic synthesis.
Role boundary: Verdicts final.
```

---

### Step 1 *(C-10; C-12)* -- All namespaces. >=3. Record.

### Step 2 *(IA: prior-frame-recovery; C-16; C-14; C-11; C-09)* -- Sort to routes. Discard log.

### Step 3 *(Gatekeeper; C-13; C-15; C-16)* -- Gate

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

### Step 5 *(C-17; C-21; IA: belief-inversion)* -- Naming scaffold. 4-step derivation.

### Step 6 *(C-20; IA: correction-integrity)* -- Co-validation. Both VALID required.

### Step 7 *(IA: failure-projection; C-02..C-04; C-08; C-12; C-14; C-17; C-18; C-22)*

Begin from failure *(C-22)*. Name, source, [CROSS] *(C-08)*, temporal *(C-12)*, belief,
surprise, mis-design *(C-18)*, impact *(C-03)*, route *(C-14)*.

### Step 8 *(C-05; IA: pattern-emergence)* -- Cross-signal synthesis. <=120 words.

### Step 9 *(C-06; C-19; IA: future-framing)* -- T-1..T-4. State selection.

### Step 10 *(C-07; C-24)*

```
TRACE-CHECK-VERDICT: [PASS | FAIL]
  -- PASS: tiers match; no orphans; one-rule-per-surprise
  -- FAIL: {label | expected | actual}
```

*Forward-reader protocol (C-34): Verifiable by TRACE-CHECK-VERDICT token. PASS certifies
tier-match, no-orphan, one-per-surprise. FAIL records each mismatch by label and tier.*

### Step 11 *(C-26)*

```
GESTALT-VERDICT: [PASS | FAIL]
  -- PASS: not survey in aggregate
  -- FAIL: {entry, gestalt-summary-fail reason, revision}
```

*Forward-reader protocol (C-34): Verifiable by GESTALT-VERDICT token. PASS certifies
complete output does not pass summary-or-survey question. FAIL records revision decisions.*

### Step 12 -- Production Chain Trace *(C-28; C-29; C-31)*

```
PRODUCTION CHAIN TRACE (NODES 1-11)
======================================================================
[NODE 1] prediction sort -- IA+prior-frame-recovery (C-30+C-32), anti-hyp (C-11),
  destinations (C-14), discard log (C-09)
-> [NODE 2] gate verdict -- Gatekeeper+dimension per stage (C-30+C-32), commit tokens
  (C-13+C-16), gallery (C-18), cross-signal (C-08), floor (C-15)
-> [NODE 3] triage -- simultaneous (C-23), failure-first (C-22)
-> [NODE 4] echo entry -- IA+failure-projection (C-30+C-32); scaffold (C-17+C-21);
  failure-first (C-22); [CROSS] (C-08); failure field (C-18); impact (C-03)
-> [NODE 5] cross-signal synthesis -- IA+pattern-emergence (C-30+C-32); C-05
-> [NODE 6] forward handover -- IA+future-framing (C-30+C-32); T-1..T-4 (C-19)
-> [NODE 7] rules -- tier vs NODE 3 (C-24), orphan check
-> [NODE 8] TRACE-CHECK-VERDICT [C-29; C-34] -- PASS|FAIL token, forward-reader protocol
-> [NODE 9] gestalt audit -- IA+unit (C-26+C-30)
-> [NODE 10] GESTALT-VERDICT [C-29; C-34] -- PASS|FAIL token, forward-reader protocol
-> [NODE 11] chain trace (this) -- all nodes (C-28); verification nodes (C-29); deps (C-31)

Dependency closure (C-31):
  C-23 -> C-24 (NODE 3 -> NODE 8)
  C-26 -> C-28 (NODE 9/10 -> NODE 11)
  C-24 -> C-28 (NODE 8 -> NODE 11)
  C-14 -> C-06 (NODE 4 -> NODE 6)
  C-17+C-21 -> C-20 (Step 5 -> Step 6)
======================================================================
```

### Dependency Closure Enumeration (C-33)

```
DEPENDENCY CLOSURE ENUMERATION
================================
C-23 output -> C-24 (NODE 3 -> NODE 8)
C-26 output -> C-28 (NODE 9/10 -> NODE 11)
C-24 output -> C-28 (NODE 8 -> NODE 11)
C-14 output -> C-06 (NODE 4 -> NODE 6)
C-17+C-21 output -> C-20 (Step 5 -> Step 6)
================================
5 loops enumerated.
```

**Output**: Steps 7-12 + Dep Closure Enumeration + Step 13. Steps 1-6 are scaffolding.

Final output sequence *(C-35: per-item criterion labels)*:

1. Echo entries (triage-ordered, failure-first within tier)
   *(C-02: citation; C-04: named label; C-07: tier in header; C-08: [CROSS]; C-12: temporal;
   C-14: route; C-17: correction-encoding; C-18: failure field; C-22: failure-first)*
2. Cross-signal synthesis
   *(C-05: >=2 labels; cross-entry only; unreachable from single entry)*
3. Forward handover guidance (register stated, slots verified)
   *(C-06: scenario + constraint + source; C-19: T-1..T-4)*
4. Rules of Thumb
   *(C-07: tier per rule; C-24: tier-match verified)*
5. TRACE-CHECK-VERDICT with forward-reader protocol
   *(C-24; C-29; C-34)*
6. GESTALT-VERDICT with forward-reader protocol
   *(C-26; C-29; C-34)*
7. Production chain trace (Nodes 1-11)
   *(C-28; C-29; C-31)*
8. Dependency Closure Enumeration
   *(C-33: 5 loops, standalone block)*
9. FLOOR-VERDICT (terminal floor check)
   *(C-36: named artifact; PASS or FLOOR-MISS)*

### Step 13 -- Terminal Minimum Surprise Floor Check *(C-36)*

Count distinct surprises. Compare to floor (3).

```
FLOOR-VERDICT: [PASS | FLOOR-MISS]
  -- PASS: distinct surprise count >= 3 in final output
  -- FLOOR-MISS: {count} surprises; shortfall: {3 - count}
```

FLOOR-MISS is a named artifact. Do not suppress it.

*(C-36: Separate from gate-time check in Step 3 Stage 2.)*

---

## V-05 -- Full Synthesis: All 28 Aspirational Criteria (C-09..C-36)

**Variation axes:** C-35 + C-36 + NODE 12 (FLOOR-VERDICT as chain node, C-29) + dep
enumeration extended to 7 loops (C-31/C-33) + FLOOR-VERDICT forward-reader protocol.

**Hypothesis:** C-35 and C-36 activate at non-overlapping positions: C-35 at output
declaration (machine-checkable contract) and C-36 at output-close (verifiable floor token).
But C-36 introduces a new verification token -- every verification token must be a chain
node (C-29) with a structural qualifier (C-28) and appear in the dep enumeration (C-33).
V-04 shows surface-level combination; V-05 closes the chain. New dep loops: the gate-time
floor count (NODE 2 / C-15) is consumed by the terminal check (NODE 12 / C-36) -- this
loop must appear in the dep enumeration. Additionally: FLOOR-VERDICT should carry a
forward-reader protocol parallel to TRACE-CHECK-VERDICT and GESTALT-VERDICT (potential
ES-1 signal for C-37 in v11). V-05 is the new baseline for v11 development.

**Builds on:** R9 V-05 (C-09..C-34) + V-01 (C-35) + V-02 (C-36) + chain extension.

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
false assumption (C-17). Derives consequence by asking "What would the next team build
wrong?" (C-18, C-22). The IA is the author of implication; the Gatekeeper is the author of
rejection.

Sub-step co-activation shorthand *(C-30, C-32)*: each IA invocation carries:
`IA: false-assumption-recovery; epistemic dimension: {name}`

Defined dimensions:

| Step | Epistemic Dimension | Why here |
|------|---------------------|----------|
| 2 | prior-frame-recovery | Recovering what was actually believed, not what spec asserts |
| 5 | belief-inversion | Deriving correction-encoding name by inverting the false assumption |
| 6 | correction-integrity | Verifying both structural form checks encode the correction |
| 7 | failure-projection | Anchoring entry in projected mis-design; failure is load-bearing |
| 8 | pattern-emergence | What only emerges when entries are read together |
| 9 | future-framing | Translating findings into actionable guidance for a future builder |

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

Discard log *(C-09; IA: false-assumption-recovery; epistemic dimension:
prior-frame-recovery)*: every non-gate item, route type, reason (1 sentence), destination.
Non-empty required.

---

### Step 3 -- Multi-Stage Epistemic Gate
*(Gatekeeper: adversarial-rejection-only; C-13; C-15; C-16)*

```
GATEKEEPER: adversarial-rejection-only -- active through end of Stage 3.
```

**Anti-Pattern Catalog** *(C-13)*:
- CONFIRMATION: confirms original hypothesis -> PREDICTABLE
- RESTATEMENT: documents known constraint -> `topic-report`
- ISOLATED-FINDING: complete in one artifact -> `topic-report`

**Gate format** *(C-16)*: `VERDICT: SURPRISE | CUT -- {anti-pattern label}`

**Stage 1 -- Prediction Test**
*(Gatekeeper: adversarial-rejection-only; epistemic dimension: novelty -- separating
investigation-emergent findings from outcomes predictable from original design materials)*

"Would a competent practitioner have predicted this from first principles?"
`PREDICTABLE` -> `topic-story` | `UNPREDICTABLE` -> Stage 2
**Commit**: `Stage 1: [{item}] -> [PREDICTABLE | UNPREDICTABLE]`

**Stage 2 -- Contradiction Test**
*(Gatekeeper: adversarial-rejection-only; epistemic dimension: opposition -- separating
genuine contradiction of a held belief from findings merely notable or unusual)*

```
We believed: {falsifiable assumption -- names a specific held belief}
VALID: {genuine falsification -- names belief and contradiction}
INVALID (absence-of-consideration): notes absence, not a falsifiable proposition
INVALID (sentiment-reaction): records team response, not a prior belief state
INVALID (hedge-uncertainty): names a gap, not a held belief
```

Floor *(C-15)*: >=3 must reach CONTRADICTION FOUND. If fewer, record floor-miss.
`NO CONTRADICTION` -> `topic-report` | `CONTRADICTION FOUND` -> Stage 3
**Commit**: `Stage 2: [{item}] -> [NO CONTRADICTION | CONTRADICTION FOUND]`

**Stage 3 -- Attribution Test**
*(Gatekeeper: adversarial-rejection-only; epistemic dimension: specificity -- separating
traceable cross-signal findings from single-artifact findings)*

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
If YES/PARTLY YES: revise, log `gestalt-summary-fail`, re-run.

```
GESTALT-VERDICT: [PASS | FAIL]
  -- PASS: output does not read as survey in aggregate; every entry is
     retroactively-visible, not a survey item included for coverage
  -- FAIL: {entry label, gestalt-summary-fail trigger reason, revision applied}
```

*Forward-reader protocol (C-34): A future reader verifies this check ran by locating
the GESTALT-VERDICT token above -- no session replay required. GESTALT-VERDICT: PASS
certifies the complete output does not pass the summary-or-survey audit question from
Step 11. GESTALT-VERDICT: FAIL records which entries triggered gestalt-summary-fail and
what revision was applied, enabling audit without the pre-revision draft.*

---

### Step 12 -- Production Chain Trace
*(C-28; C-29; C-31)*

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
  consumed by: NODE 5, NODE 6, NODE 7, NODE 12 (final surprise count for floor check)

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
  structural qualifier: PASS|FAIL token with complete forward-reader protocol (C-34)
    certifying tier-match (from NODE 3), no-orphan, one-rule-per-surprise; verifiable by
    token location without session replay; mismatches recorded by label if FAIL
  produces: traceability audit result (C-24+C-29+C-34)
  consumed by: NODE 11 (closes C-23->C-24->NODE 8 loop)

-> [NODE 9] gestalt audit
  structural qualifier: IA: false-assumption-recovery applied to complete artifact as
    unit (C-26+C-30); gestalt-summary-fail logged separately from gate-fail
  produces: gestalt audit result (C-26)
  consumed by: NODE 10

-> [NODE 10] GESTALT-VERDICT [C-29: chain node; C-34: forward-reader protocol inline]
  structural qualifier: PASS|FAIL token with complete forward-reader protocol (C-34)
    certifying output-level non-survey and recording revision reasons if FAIL; verifiable
    by token location; distinct scope from NODE 8
  produces: gestalt audit result (C-26+C-29+C-34)
  consumed by: NODE 11 (closes C-26->C-28 loop)

-> [NODE 11] production chain trace (this node)
  structural qualifier: all 12 nodes named with qualifiers verifiable from output (C-28);
    all three verification tokens are chain nodes (C-29); all 7 inter-criterion deps
    annotated (C-31)
  produces: closed, auditable dependency graph
  consumed by: output (terminal)

-> [NODE 12] FLOOR-VERDICT [C-29: chain node; C-36: terminal floor check;
  C-34 candidate: forward-reader protocol inline]
  structural qualifier: written PASS|FLOOR-MISS token produced by counting distinct
    surprises in final output (NODE 4 count) against floor (C-15 floor = 3); runs at
    output-close, separate from gate-time floor count in NODE 2; verifiable by token
    location without session replay; floor-miss records count and shortfall if FAIL
  produces: terminal floor compliance result (C-36)
  consumed by: output (terminal); closes gate-time floor count -> terminal check loop
    (C-15 output -> C-36, NODE 2 -> NODE 12)

======================================================================
Dependency closure verification (C-31): 7 inter-criterion loops explicitly closed:
  C-23 output -> C-24 (NODE 3 -> NODE 8): triage rank feeds tier-match check
  C-26 output -> C-28 (NODE 9/10 -> NODE 11): gestalt verdict is chain node
  C-24 output -> C-28 (NODE 8 -> NODE 11): traceability verdict is chain node
  C-14 output -> C-06 (NODE 4 -> NODE 6): routing feeds handover scenario
  C-17+C-21 output -> C-20 (Step 5 -> Step 6): naming scaffold feeds co-validation gate
  C-15 output -> C-36 (NODE 2 -> NODE 12): gate-time floor count feeds terminal check
  C-36 output -> C-28 (NODE 12 -> NODE 11): FLOOR-VERDICT is named chain node in trace
No inter-criterion dependency is discoverable only by reading the prompt.
```

---

### Dependency Closure Enumeration (C-33)

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
  gate-time floor count (NODE 2) is compared against final surprise count at NODE 12;
  NODE 12 cannot run terminal check without gate-time baseline from NODE 2

C-36 output -> C-28 (NODE 12 -> NODE 11 trace):
  FLOOR-VERDICT (NODE 12) is named chain node; NODE 11 must name NODE 12 to satisfy C-28
================================
7 loops enumerated. Reviewer spot-checks closure by reading this block.
Any loop absent from this enumeration that appears in the chain trace is a C-33 violation.
```

---

**Output**: Steps 7-12 + Dependency Closure Enumeration + Step 13. Steps 1-6 are scaffolding.

Final output sequence *(C-35: output contract -- each item carries structural label tied to
governing criterion; completeness spot-checkable without re-reading prompt body)*:

1. Echo entries (triage-ordered, failure-first within tier)
   *(satisfies C-02: source citation {name} ({namespace/skill}); C-04: named label The
   {Corrected Belief}: {Domain}; C-07: impact tier HIGH/MEDIUM/LOW in header from Step 4;
   C-08: [CROSS: A x B] annotation on every cross-signal entry; C-12: temporal anchor
   (round or date of earliest contributing signal); C-14: downstream route -> {skill};
   C-17: correction-encoding name encoding what was wrong and where; C-18: failure field
   framed as "If next team carries old assumption, {mis-design}"; C-22: failure written
   first; name, source, impact derived after)*
2. Cross-signal synthesis
   *(satisfies C-05: >=2 named labels cited by exact label; cross-entry pattern stated as
   unreachable from any single entry alone; <=120 words)*
3. Forward handover guidance (register stated, slots verified)
   *(satisfies C-06: names specific construction scenario, constraint, and source signal;
   C-19: register selected from T-1..T-4 menu; register stated before writing; slots
   verified before output)*
4. Rules of Thumb
   *(satisfies C-07: impact tier per rule [HIGH|MEDIUM]; C-24: tier matches triage from
   Step 4; no orphan rules; no surprise generates more than one rule; <=3 rules)*
5. TRACE-CHECK-VERDICT with forward-reader protocol
   *(satisfies C-24: traceability closure verdict; C-29: verification node in chain trace;
   C-34: forward-reader rationale stating what PASS certifies and what FAIL records)*
6. GESTALT-VERDICT with forward-reader protocol
   *(satisfies C-26: gestalt summary audit result; C-29: verification node in chain trace;
   C-34: forward-reader rationale stating what PASS certifies and what FAIL records)*
7. Production chain trace with structural qualifiers (12 nodes)
   *(satisfies C-28: every link named with qualifier; C-29: all three verification tokens
   are chain nodes including NODE 12; C-31: all 7 inter-criterion deps annotated)*
8. Dependency Closure Enumeration (standalone terminal block)
   *(satisfies C-33: separate from chain trace; 7 loops in {source} -> {consuming}
   ({node}) format; spot-checkable without traversal)*
9. FLOOR-VERDICT (terminal minimum surprise floor check)
   *(satisfies C-36: separate from gate-time floor check in Step 3 Stage 2; named
   PASS|FLOOR-MISS artifact; floor-miss surfaces count and shortfall as named output)*

### Step 13 -- Terminal Minimum Surprise Floor Check *(C-36)*

Count distinct surprises in final output (Item 1 entries). Compare to floor (3).

```
FLOOR-VERDICT: [PASS | FLOOR-MISS]
  -- PASS: distinct surprise count >= 3 confirmed in final output
  -- FLOOR-MISS: {count} surprises present; floor shortfall: {3 - count} required
```

*Forward-reader protocol (C-34 candidate -- potential ES-1 signal for v11 C-37): A future
reader verifies this check ran by locating the FLOOR-VERDICT token above in the output --
no session replay required. FLOOR-VERDICT: PASS certifies that the final output contains
at least 3 distinct surprises after all post-gate revisions (gestalt audit, traceability
check) are complete. FLOOR-VERDICT: FLOOR-MISS certifies the count found and the shortfall,
enabling a reader to determine whether the output is below the floor and by how much,
without re-executing the prompt or manually counting entries.*

*(C-36: This check is separate from and after the gate-time floor check in Step 3 Stage 2.
The gate-time check verifies >=3 candidates reach CONTRADICTION FOUND in the gate pipeline.
This terminal check verifies >=3 distinct surprises are present in the finalized output
after post-gate composition, gestalt audit (Step 11), and any resulting revisions. These
are different populations: a surprise that passed the gate may be removed during gestalt
audit revision; only the terminal check catches that reduction.)*

---

## Predicted Scores (v10 rubric)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 | PASS | PASS | PASS | PASS | PASS |
| C-02 | PASS | PASS | PASS | PASS | PASS |
| C-03 | PASS | PASS | PASS | PASS | PASS |
| C-04 | PASS | PASS | PASS | PASS | PASS |
| C-05 | PASS | PASS | PASS | PASS | PASS |
| C-06 | PASS | PASS | PASS | PASS | PASS |
| C-07 | PASS | PASS | PASS | PASS | PASS |
| C-08 | PASS | PASS | PASS | PASS | PASS |
| C-09 | PASS | PASS | PASS | PASS | PASS |
| C-10 | PASS | PASS | PASS | PASS | PASS |
| C-11 | PASS | PASS | PASS | PASS | PASS |
| C-12 | PASS | PASS | PASS | PASS | PASS |
| C-13 | PASS | PASS | PASS | PASS | PASS |
| C-14 | PASS | PASS | PASS | PASS | PASS |
| C-15 | PASS | PASS | PASS | PASS | PASS |
| C-16 | PASS | PASS | PASS | PASS | PASS |
| C-17 | PASS | PASS | PASS | PASS | PASS |
| C-18 | PASS | PASS | PASS | PASS | PASS |
| C-19 | PASS | PASS | PASS | PASS | PASS |
| C-20 | PASS | PASS | PASS | PASS | PASS |
| C-21 | PASS | PASS | PASS | PASS | PASS |
| C-22 | PASS | PASS | PASS | PASS | PASS |
| C-23 | PASS | PASS | PASS | PASS | PASS |
| C-24 | PASS | PASS | PASS | PASS | PASS |
| C-25 | PASS | PASS | PASS | PASS | PASS |
| C-26 | PASS | PASS | PASS | PASS | PASS |
| C-27 | PASS | PASS | PASS | PASS | PASS |
| C-28 | PASS | PASS | PASS | PASS | PASS |
| C-29 | PASS | PASS | PASS | PARTIAL | PASS |
| C-30 | PASS | PASS | PASS | PASS | PASS |
| C-31 | PASS | PASS | PASS | PARTIAL | PASS |
| C-32 | PASS | PASS | PASS | PASS | PASS |
| C-33 | PASS | PASS | PASS | PARTIAL | PASS |
| C-34 | PASS | PASS | PASS | PASS | PASS |
| C-35 | PASS | FAIL | PASS | PASS | PASS |
| C-36 | FAIL | PASS | FAIL | PASS | PASS |

*C-29/C-31/C-33 notes (V-04):*
- TRACE-CHECK-VERDICT and GESTALT-VERDICT are chain nodes (satisfying C-29 for those two).
  FLOOR-VERDICT exists and is a named artifact (C-36 satisfied) but is NOT a chain node in
  the V-04 trace (nodes 1..11 only). C-29 scored PARTIAL.
- 5 dep loops closed in chain trace and enumeration; C-15->C-36 and C-36->C-28 absent.
  C-31 scored PARTIAL. C-33 scored PARTIAL (5 of 7 loops enumerated).

*C-35 notes:*
- V-01, V-03, V-04, V-05: Output contract with per-item criterion labels. PASS.
- V-02: Output sequence lists items in order without per-item criterion labels. A reviewer
  cannot spot-check completeness without re-reading the prompt body. FAIL.

*C-36 notes:*
- V-02, V-04, V-05: FLOOR-VERDICT named token with PASS/FLOOR-MISS states present. PASS.
- V-01: Terminal check present as prose instruction only; no named token artifact. FAIL.
- V-03: Same as V-01 -- prose form. FAIL.

**Discriminating pairs:**
- V-01 vs V-05: C-36 FAIL vs PASS; C-29/C-31/C-33 PASS vs PASS (chain depth same since
  V-01 has no FLOOR-VERDICT token to add as a node). Isolates floor-verdict token value.
- V-02 vs V-05: C-35 FAIL vs PASS. Isolates output contract label value against floor-
  verdict-token baseline.
- V-03 vs V-01: C-35 PASS both, C-36 FAIL both; position front vs back. Isolates contract
  position effect without confounding from C-36 delta.
- V-04 vs V-05: C-29/C-31/C-33 PARTIAL vs PASS. Direct isolation of NODE 12 chain closure
  value. C-35 and C-36 held constant between V-04 and V-05.
