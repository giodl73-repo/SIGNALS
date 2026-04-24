---
skill: quest-variate
skill_target: topic-echo
date: 2026-03-15
round: 14
rubric: v14
rubric_max: 204
---

# Variations: `topic:echo` -- Round 14

**Rubric:** v14 | **Date:** 2026-03-15

---

## Design Context

R13 V-05 produced four structural gaps formalized as C-46..C-49.

1. **R13 sequencing-vs-blocking gap (-> C-46)**: NODE 15 (assembly) is ordered after
   BACK-FILL-VERDICT (NODE 14) -- C-44 PASS -- but NODE 15's header names no declared
   dependency on that verdict. A model can proceed through NODE 15 without consulting
   the verdict. C-46 closes this: the assembly step header must name BACK-FILL-VERDICT
   (NODE 14) as a required input, converting sequential constraint into architectural
   blocking.

2. **R13 token-audit-footprint gap (-> C-47)**: AUTHORITY-VERDICT carries a NODE
   assignment (C-37), forward-reader rationale (C-34), and C-45 note. But the introduction
   block names no criteria the token satisfies and carries no explicit non-identity clause.
   A reader cannot reconstruct the token's audit footprint without re-reading each
   criterion. C-47 requires: (1) NODE assignment, (2) forward-reader rationale,
   (3) satisfied-criteria enumeration ("satisfies C-37/C-41/C-43/C-45"), (4) explicit
   non-identity clause ("not a structural marker embedded in C-40's node declaration
   template").

3. **R13 authority-block-isolation gap (-> C-48)**: The authority block states the
   non-vacuity count (C-43) and confirms C-41 but does not open by citing BACK-FILL-
   VERDICT (NODE 14). A model executing the authority step must locate NODE 14 separately
   to verify C-44 compliance. C-48 requires the authority block to open: "BACK-FILL-
   VERDICT (NODE 14): confirmed PASS prior to this step (C-44 satisfied)." This links
   C-43 and C-44 operationally in a single block.

4. **R13 version-scope gap (-> C-49)**: The terminal dependency enumeration closes with
   a count and C-39's guard but no version-aligned closing tag naming the criteria
   introduced in v13 (`[C-42..C-45]`). C-49 requires a closing tag naming all new
   criteria from the current rubric version, machine-checkable against the changelog.

**Variation plan:**

- V-01: C-46 only -- assembly step header declares `requires BACK-FILL-VERDICT (NODE 14):
  PASS`; C-47 absent; C-48 absent; C-49 absent. 17 nodes. 12 deps.
- V-02: C-47 only -- AUTHORITY-VERDICT introduction carries full identity contract
  (NODE + forward-reader + satisfied-criteria + non-identity clause);
  C-46 absent; C-48 absent; C-49 absent. 17 nodes. 12 deps.
- V-03: C-48 only -- authority block opens with BACK-FILL-VERDICT citation before
  non-vacuity count; C-46 absent; C-47 absent; C-49 absent. 17 nodes. 12 deps.
- V-04: C-46 + C-47 -- assembly header dep declaration AND full token identity contract;
  C-48 absent; C-49 absent. 17 nodes. 12 deps.
- V-05: Full synthesis -- C-46 + C-47 + C-48 + C-49; 17 nodes; 13 deps (C-48 adds
  named operational link: BACK-FILL-VERDICT consumed inside authority block).

**Discriminating pairs:**

- V-01 vs V-05: C-46 PASS both; C-47 V-01 FAIL (no satisfied-criteria enumeration,
  no non-identity clause), V-05 PASS
- V-02 vs V-05: C-47 PASS both; C-46 V-02 FAIL (no named dep in assembly header),
  V-05 PASS
- V-03 vs V-05: C-48 PASS both; C-46+C-47 V-03 FAIL, V-05 PASS; C-49 V-03 FAIL
- V-04 vs V-05: C-46+C-47 PASS both; C-48 V-04 FAIL (authority block lacks verdict
  citation at open), V-05 PASS; C-49 V-04 FAIL

---

## V-01 -- Single-axis: Assembly step declares structural dependency (C-46)

**Variation axis:** Assembly step header carries explicit named dependency on detection
verdict. NODE 15 header reads: `*(C-46: requires BACK-FILL-VERDICT (NODE 14): PASS --
assembly is architecturally blocked without this verdict)*`. C-44 enforces that detection
precedes assembly in sequence; C-46 enforces that assembly cannot execute without
consulting the verdict. Without C-46, a model running NODE 15 knows detection ran (from
sequencing) but is not blocked from bypassing the verdict lookup.

**Hypothesis:** C-44 and C-46 address adjacent failure modes. C-44 prevents
detection-after-assembly. C-46 prevents verdict-bypass in sequentially-correct prompts.
V-01 tests C-46 in isolation. C-47 absent -- AUTHORITY-VERDICT carries no satisfied-
criteria enumeration, no non-identity clause. C-48 absent -- authority block does not
open with verdict citation. C-49 absent -- dep enumeration has no version-aligned tag.
Predicted: C-46 PASS; C-47 FAIL; C-48 FAIL; C-49 FAIL; all C-09..C-45 inherited.

**Builds on:** R13 V-05 -- all 37 criteria (C-09..C-45) active. 17 nodes. 12 deps.

---

### Prompt Body

You are running `/quest:topic echo` for the topic: {topic}.

All essential signals are in hand. Your task: surface the genuine surprises -- findings
that only became visible in retrospect, from cross-signal tension, that no competent
practitioner would have predicted before gathering evidence.

Not a summary. Not a survey of discoveries. An echo: the signal that comes back that
you didn't send.

---

### Roles *(C-25; C-30; C-32)*

**Institutional Archaeologist (IA)**
*First invocation: Step 2.*
Function: Recovers false assumptions embedded in current materials. Frames every surprise
as a correction to a false assumption (C-17). Derives consequence: "What would the next
team build wrong?" (C-18, C-22).

Sub-step co-activation: `IA: false-assumption-recovery; epistemic dimension: {name}`

| Step | Epistemic Dimension    | Why here                                              |
|------|------------------------|-------------------------------------------------------|
| 2    | prior-frame-recovery   | Recovering what was actually believed, not spec text  |
| 5    | belief-inversion       | Deriving correction-encoding name by inverting belief |
| 6    | correction-integrity   | Verifying both form checks encode the correction      |
| 7    | failure-projection     | Anchoring entry in projected mis-design               |
| 8    | pattern-emergence      | What only emerges when entries are read together      |
| 9    | future-framing         | Translating findings to guidance for future builder   |

**Gatekeeper**
*First invocation: Step 3.*

```
GATEKEEPER -- FUNCTION DECLARATION (C-27)
---------------------------------------------------------------------
Function:      Adversarial rejection. Tests: (1) first-principles predictability;
               (2) cross-signal requirement. Fails either: rejected.
Not-function:  Future-reader framing (IA's domain).
Role boundary: Gatekeeper verdicts are final.
---------------------------------------------------------------------
```

---

### Step 1 -- Read Signal Record *(C-10; C-12)*

All namespaces (scout, draft, review, flow, trace, prove, listen, program, topic).
Record: namespaces covered (>=3 floor), total artifacts, date range.
Scaffolding -- does not enter the production chain.

---

### Step 2 -- [NODE 1: typed-route prediction sort]
*(IA: false-assumption-recovery; epistemic dimension: prior-frame-recovery; C-16; C-14; C-11; C-09)*

Routes: `topic-story` | `topic-report` | `gate-pipeline`
Anti-hypothesis guard *(C-11)*: "Confirms investigation hypothesis?" YES -> `topic-story`.
Discard log *(C-09)*: every non-gate item, route type, reason (1 sentence). Non-empty.

---

### Step 3 -- [NODE 2: staged gate verdict]
*(Gatekeeper: adversarial-rejection-only; C-13; C-15; C-16)*

Anti-Pattern Catalog *(C-13)*: CONFIRMATION | RESTATEMENT | ISOLATED-FINDING
Gate format *(C-16)*: `VERDICT: SURPRISE | CUT -- {label}`

**Stage 1 -- Prediction Test** *(epistemic dimension: novelty)*
`PREDICTABLE` -> `topic-story` | `UNPREDICTABLE` -> Stage 2
Commit: `Stage 1: [{item}] -> [PREDICTABLE | UNPREDICTABLE]`

**Stage 2 -- Contradiction Test** *(epistemic dimension: opposition)*
`We believed:` / VALID / INVALID gallery. Floor *(C-15)*: >=3 CONTRADICTION FOUND.
Commit: `Stage 2: [{item}] -> [NO CONTRADICTION | CONTRADICTION FOUND]`

**Stage 3 -- Attribution Test** *(epistemic dimension: specificity)*
`SINGLE-ARTIFACT` -> `topic-report` | `CROSS-SIGNAL` -> SURPRISE
Commit: `Stage 3: [{item}] -> [SINGLE-ARTIFACT | CROSS-SIGNAL] -- sources: [{a1}, {a2}]`

---

### Step 4 -- [NODE 3: comparative triage rank] *(C-23; C-22)*

Comparative. HIGH | MEDIUM | LOW. Failure-first within tier. All before expansion.

---

### Step 5 -- [NODE 4: naming scaffold]
*(C-17; C-21; IA: false-assumption-recovery; epistemic dimension: belief-inversion)*

1. Old belief. 2. Correction. 3. Domain. 4. Form: `The {Corrected Belief}: {Domain}`.
VALID: "The Silent Veto: Adoption Workflow". INVALID: "Surprising Finding About Adoption".

---

### Step 6 -- [NODE 5: pre-expansion co-validation gate]
*(C-20; IA: false-assumption-recovery; epistemic dimension: correction-integrity)*

Both VALID required. Either failing blocks expansion.
- Name form *(C-17)*: `The {Corrected Belief}: {Domain}`? -> VALID / INVALID
- Failure field *(C-18)*: "If next team carries old assumption, {specific mis-design}"?
  -> VALID / INVALID

---

### Step 7 -- [NODE 6: echo entry]
*(IA: false-assumption-recovery; epistemic dimension: failure-projection;*
*C-02..C-04; C-08; C-12; C-14; C-17; C-18; C-22)*

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

### Step 8 -- [NODE 7: cross-signal synthesis]
*(C-05; IA: false-assumption-recovery; epistemic dimension: pattern-emergence)*

<=120 words. Name >=2 entries by exact label. Cross-entry pattern only.

---

### Step 9 -- [NODE 8: forward handover guidance]
*(C-06; C-19; IA: false-assumption-recovery; epistemic dimension: future-framing)*

T-1..T-4 register. State selection. Verify slots. Scenario and constraint specific.

---

### Step 10 -- [NODE 9: impact-anchored rules] + [NODE 10: TRACE-CHECK-VERDICT]
*(C-07; C-24)*

*(C-37: TRACE-CHECK-VERDICT is NODE 10.)*

```
TRACE-CHECK-VERDICT: [PASS | FAIL]
  -- PASS: all tiers match; no orphan rules; one-rule-per-surprise confirmed
  -- FAIL: {rule label | expected tier | actual tier}
```
*Forward-reader protocol (C-34): verifiable by TRACE-CHECK-VERDICT token location.*

---

### Step 11 -- [NODE 11: gestalt audit] + [NODE 12: GESTALT-VERDICT]
*(C-26)*

*(C-37: GESTALT-VERDICT is NODE 12.)*

"Could this output be described as a summary or survey?" If YES: revise, log gestalt-summary-fail.

```
GESTALT-VERDICT: [PASS | FAIL]
  -- PASS: output does not read as survey in aggregate
  -- FAIL: {entry label, gestalt-summary-fail trigger, revision applied}
```
*Forward-reader protocol (C-34): verifiable by GESTALT-VERDICT token location.*

---

### Step 12 -- [NODE 13: back-fill guard] + [NODE 14: BACK-FILL-VERDICT]
*(C-44: detection protocol ordered BEFORE trace assembly step NODE 15)*

```
BACK-FILL-GUARD (C-44)
---------------------------------------------------------------------
Ordered BEFORE assembly (NODE 15). Verifies Steps 2-12 each carry an inline
[NODE N: {role}] declaration in the step header.

  Step header carries [NODE N: {role}] -> DECLARED
  Step header lacks inline declaration -> BACK-FILL-RISK
---------------------------------------------------------------------
```

*(C-37: BACK-FILL-VERDICT is NODE 14.)*

```
BACK-FILL-VERDICT: [PASS | FAIL]
  -- PASS: all Steps 2-12 carry inline [NODE N: {role}] declarations; assembly
           (NODE 15) may proceed in confirmatory mode only
  -- FAIL: Step {N} lacks inline node declaration; back-fill risk identified
```
*Forward-reader protocol (C-34): verifiable by BACK-FILL-VERDICT token location.*
*(C-44: NODE 13 ordered before NODE 15; BACK-FILL-VERDICT is NODE 14, consumed
by -- not produced inside -- NODE 15.)*

---

### Step 13 -- [NODE 15: production chain trace]
*(C-28; C-29; C-31; C-38; C-40; C-41)*
*(C-46: requires BACK-FILL-VERDICT (NODE 14): PASS -- assembly is architecturally
blocked without this verdict. Locate BACK-FILL-VERDICT before proceeding.
If BACK-FILL-VERDICT is FAIL: surface the gap; do not proceed.)*

```
STEP-TIME AUTHORITY RULE (C-41) -- WITH NON-VACUITY ASSERTION (C-43)
---------------------------------------------------------------------
This trace assembly step is CONFIRMATORY ONLY.

NON-VACUITY COUNT (C-43): This rule governs [N] step-header node declarations.
N >= 1 confirmed. The rule governs a nonzero population; it is operative.

MUST NOT: define, renumber, back-fill, or override any step-time node assignment.
If this trace disagrees with any step header, the step header governs.
Authority: step-execution time -> trace assembly time. Irreversible.
---------------------------------------------------------------------
```

*(C-37: AUTHORITY-VERDICT is NODE 16.)*

```
AUTHORITY-VERDICT: [CONFIRMATORY | OVERRIDE-DETECTED]
  -- CONFIRMATORY: all 17 entries confirm step-time declarations; no back-fill
  -- OVERRIDE-DETECTED: {NODE N | step header declared X | trace assigns Y}
```
*Forward-reader protocol (C-34): verifiable by AUTHORITY-VERDICT token location.*
*(C-45: AUTHORITY-VERDICT is a dedicated compliance token, not a template marker
embedded in C-40's node declaration format. NODE 16 per C-37.)*
[C-47 ABSENT: no satisfied-criteria enumeration; no explicit non-identity clause
beyond the C-45 note above. Full audit footprint not reconstructible from token block.]

```
PRODUCTION CHAIN TRACE
VERIFICATION NODES INCLUDED (C-29) | DEPENDENCY GRAPH CLOSED (C-31)
C-42 PRECONDITION TYPED | C-43 COUNT ACTIVE | C-44 PRE-ASSEMBLY | C-45 DEDICATED TOKEN
C-46: NODE 15 HEADER DECLARES DEP ON BACK-FILL-VERDICT (NODE 14)
======================================================================

[NODE 1]  typed-route prediction sort
  structural qualifier: IA+prior-frame-recovery (C-30+C-32), anti-hyp guard (C-11),
    typed destinations (C-14), non-empty discard log (C-09)
  consumed by: NODE 2

-> [NODE 2]  staged gate verdict
  structural qualifier: Gatekeeper+dimension per stage (C-30+C-32), commit tokens
    (C-13+C-16), We-believed gallery Stage 2 (C-18), cross-signal Stage 3, floor (C-15)
  consumed by: NODE 3, NODE 17

-> [NODE 3]  comparative triage rank
  structural qualifier: simultaneous comparison (C-23), failure-first (C-22)
  consumed by: NODE 9, NODE 10

-> [NODE 4]  naming scaffold
  structural qualifier: IA+belief-inversion (C-30+C-32); 4-step derivation (C-21); format (C-17)
  consumed by: NODE 5

-> [NODE 5]  pre-expansion co-validation gate
  structural qualifier: IA+correction-integrity (C-30+C-32); both-VALID blocking (C-20)
  consumed by: NODE 6

-> [NODE 6]  echo entry
  structural qualifier: IA+failure-projection (C-30+C-32); failure-first (C-22);
    [CROSS] (C-08); failure field (C-18); impact (C-03)
  consumed by: NODE 7, NODE 8, NODE 9, NODE 17

-> [NODE 7]  cross-signal synthesis
  structural qualifier: IA+pattern-emergence (C-30+C-32); >=2 exact labels (C-05)

-> [NODE 8]  forward handover guidance
  structural qualifier: IA+future-framing (C-30+C-32); T-1..T-4 (C-19); slots (C-06)

-> [NODE 9]  impact-anchored rules
  structural qualifier: tier vs NODE 3 (C-24), orphan check
  consumed by: NODE 10

-> [NODE 10] TRACE-CHECK-VERDICT [C-29; C-34; C-37: NODE 10]

-> [NODE 11] gestalt audit
  structural qualifier: complete artifact as unit (C-26)
  consumed by: NODE 12

-> [NODE 12] GESTALT-VERDICT [C-29; C-34; C-37: NODE 12]

-> [NODE 13] back-fill guard
  structural qualifier: pre-assembly detection (C-44); scans Steps 2-12
  consumed by: NODE 14

-> [NODE 14] BACK-FILL-VERDICT [C-29; C-34; C-37: NODE 14; C-44: pre-assembly]
  consumed by: NODE 15 (C-46: declared dep in step header)

-> [NODE 15] production chain trace (this step)
  structural qualifier: 17 nodes+qualifiers (C-28); verification in chain (C-29);
    C-40->C-41 precondition typed (C-42); C-41+C-43; C-44+C-46 dep declared; C-38 claim
  note: C-48 ABSENT -- authority block states non-vacuity count but does not open
    with BACK-FILL-VERDICT citation

-> [NODE 16] AUTHORITY-VERDICT [C-29; C-34; C-37: NODE 16; C-45: dedicated token]
  note: C-47 ABSENT -- no satisfied-criteria enumeration; no non-identity clause

-> [NODE 17] FLOOR-VERDICT [C-29; C-36; C-34; C-37: NODE 17]

======================================================================
CLOSURE CLAIM (C-38): No inter-criterion dependency discoverable only by reading
the prompt. Known dependencies (12):
  C-23 -> C-24 (NODE 3 -> NODE 10)
  C-26 -> C-28 (NODE 11/12 -> NODE 15)
  C-24 -> C-28 (NODE 10 -> NODE 15)
  C-14 -> C-06 (NODE 6 -> NODE 8)
  C-17+C-21 -> C-20 (NODE 4 -> NODE 5)
  C-15 -> C-36 (NODE 2 -> NODE 17)
  C-36 -> C-28 (NODE 17 -> NODE 15)
  C-40 (structural precondition) -> C-41 (NODE 15) [C-42]
  C-43 -> C-41 (NODE 15) [depends on C-42]
  C-44+C-46: BACK-FILL-GUARD (NODE 13/14) -> assembly (NODE 15); dep declared in header
  C-41 -> C-45 (NODE 15 -> NODE 16) [dedicated token, C-37 inline]
  C-37 -> NODE 14: BACK-FILL-VERDICT inline declaration at governing step
Attempt to falsify by reading the full prompt.
```

---

### Dependency Closure Enumeration *(C-33)*

```
DEPENDENCY CLOSURE ENUMERATION
================================
CONTRACT HEADER: Any loop in chain trace but absent here is a C-33 violation. (C-39)

C-23 -> C-24 (NODE 3 -> NODE 10)
C-26 -> C-28 (NODE 11/12 -> NODE 15)
C-24 -> C-28 (NODE 10 -> NODE 15)
C-14 -> C-06 (NODE 6 -> NODE 8)
C-17+C-21 -> C-20 (NODE 4 -> NODE 5)
C-15 -> C-36 (NODE 2 -> NODE 17)
C-36 -> C-28 (NODE 17 -> NODE 15)
C-40 (structural precondition) -> C-41 (NODE 15) [C-42]
C-43 -> C-41 (NODE 15) [C-43 count derives from C-40 declarations]
C-44+C-46: BACK-FILL-GUARD (NODE 13/14) -> assembly (NODE 15) [C-44+C-46]
C-41 -> C-45 (NODE 15 -> NODE 16) [C-45 dedicated token]
C-37 -> NODE 14: inline declaration at back-fill guard step
================================
12 loops enumerated.
Any loop absent from this enumeration that appears in the chain trace is a
C-33 violation. (C-39 postamble)
[C-49 ABSENT: no version-aligned closing tag for v14 new criteria]
```

---

**Final output sequence** *(C-35)*:
1. Echo entries *(C-02; C-04; C-07; C-08; C-12; C-14; C-17; C-18; C-22)*
2. Cross-signal synthesis *(C-05)*
3. Forward handover guidance *(C-06; C-19)*
4. Rules of Thumb *(C-07; C-24)*
5. TRACE-CHECK-VERDICT *(C-24; C-29; C-34; C-37: NODE 10)*
6. GESTALT-VERDICT *(C-26; C-29; C-34; C-37: NODE 12)*
7. BACK-FILL-VERDICT *(C-44; C-29; C-34; C-37: NODE 14)*
8. Production chain trace -- 17 nodes; C-41+C-43; C-42 precondition; C-44+C-46 dep
   declared in header *(C-28; C-29; C-31; C-38; C-40; C-41; C-42; C-43; C-44; C-46)*
9. AUTHORITY-VERDICT *(C-45; C-29; C-34; C-37: NODE 16)* [C-47 ABSENT]
10. Dependency Closure Enumeration -- 12 loops *(C-33; C-39)* [C-49 ABSENT]
11. FLOOR-VERDICT *(C-36; C-37: NODE 17)*

### Step 14 -- [NODE 17: FLOOR-VERDICT]

*(C-37: FLOOR-VERDICT is NODE 17.)*

```
FLOOR-VERDICT: [PASS | FLOOR-MISS]
  -- PASS: distinct surprise count >= 3 confirmed in final output
  -- FLOOR-MISS: {count} surprises; shortfall: {3 - count}
```
*Forward-reader protocol (C-34): verifiable by FLOOR-VERDICT token location.*
*(C-36: Separate from gate-time floor check in Step 3 Stage 2.)*

---

## V-02 -- Single-axis: Token identity contract (C-47)

**Variation axis:** AUTHORITY-VERDICT introduction block carries full four-part identity
contract: (1) NODE assignment, (2) forward-reader rationale, (3) criteria enumeration
("satisfies C-37/C-41/C-43/C-45"), (4) non-identity clause ("not a structural marker
embedded in C-40's node declaration template"). A reader encountering the token in
isolation can determine exactly what it certifies without re-reading each criterion.

**Hypothesis:** Without C-47, a reader can reconstruct C-41 compliance and the C-45
distinction, but cannot determine from the token block alone whether C-43 and C-37 are
also satisfied, nor whether conflation with a template marker has occurred at C-40's step.
The four-part contract makes the full audit footprint in-band. C-46 absent -- NODE 15
header carries prose condition without naming the verdict as a declared dep. C-48 absent
-- authority block does not open with verdict citation. C-49 absent.
Predicted: C-47 PASS; C-46 FAIL; C-48 FAIL; C-49 FAIL; all C-09..C-45 inherited.

**Builds on:** R13 V-05 -- all 37 criteria (C-09..C-45) active. 17 nodes. 12 deps.

---

### Prompt Body

You are running `/quest:topic echo` for the topic: {topic}.

All essential signals are in hand. Your task: surface the genuine surprises -- findings
that only became visible in retrospect, from cross-signal tension, that no competent
practitioner would have predicted before gathering evidence.

Not a summary. Not a survey of discoveries. An echo: the signal that comes back that
you didn't send.

---

### Roles *(C-25; C-30; C-32)*

**Institutional Archaeologist (IA)**
*First invocation: Step 2.*
Function: Recovers false assumptions embedded in current materials. Frames every surprise
as a correction to a false assumption (C-17). Derives consequence: "What would the next
team build wrong?" (C-18, C-22).

Sub-step co-activation: `IA: false-assumption-recovery; epistemic dimension: {name}`

| Step | Epistemic Dimension    | Why here                                              |
|------|------------------------|-------------------------------------------------------|
| 2    | prior-frame-recovery   | Recovering what was actually believed, not spec text  |
| 5    | belief-inversion       | Deriving correction-encoding name by inverting belief |
| 6    | correction-integrity   | Verifying both form checks encode the correction      |
| 7    | failure-projection     | Anchoring entry in projected mis-design               |
| 8    | pattern-emergence      | What only emerges when entries are read together      |
| 9    | future-framing         | Translating findings to guidance for future builder   |

**Gatekeeper**
*First invocation: Step 3.*

```
GATEKEEPER -- FUNCTION DECLARATION (C-27)
---------------------------------------------------------------------
Function:      Adversarial rejection. Tests: (1) first-principles predictability;
               (2) cross-signal requirement. Fails either: rejected.
Not-function:  Future-reader framing (IA's domain).
Role boundary: Gatekeeper verdicts are final.
---------------------------------------------------------------------
```

---

### Step 1 -- Read Signal Record *(C-10; C-12)*

All namespaces (scout, draft, review, flow, trace, prove, listen, program, topic).
Record: namespaces covered (>=3 floor), total artifacts, date range.
Scaffolding -- does not enter the production chain.

---

### Step 2 -- [NODE 1: typed-route prediction sort]
*(IA: false-assumption-recovery; epistemic dimension: prior-frame-recovery; C-16; C-14; C-11; C-09)*

Routes: `topic-story` | `topic-report` | `gate-pipeline`
Anti-hypothesis guard *(C-11)*: "Confirms investigation hypothesis?" YES -> `topic-story`.
Discard log *(C-09)*: every non-gate item, route type, reason (1 sentence). Non-empty.

---

### Step 3 -- [NODE 2: staged gate verdict]
*(Gatekeeper: adversarial-rejection-only; C-13; C-15; C-16)*

Anti-Pattern Catalog *(C-13)*: CONFIRMATION | RESTATEMENT | ISOLATED-FINDING
Gate format *(C-16)*: `VERDICT: SURPRISE | CUT -- {label}`

**Stage 1 -- Prediction Test** *(epistemic dimension: novelty)*
`PREDICTABLE` -> `topic-story` | `UNPREDICTABLE` -> Stage 2
Commit: `Stage 1: [{item}] -> [PREDICTABLE | UNPREDICTABLE]`

**Stage 2 -- Contradiction Test** *(epistemic dimension: opposition)*
`We believed:` / VALID / INVALID gallery. Floor *(C-15)*: >=3 CONTRADICTION FOUND.
Commit: `Stage 2: [{item}] -> [NO CONTRADICTION | CONTRADICTION FOUND]`

**Stage 3 -- Attribution Test** *(epistemic dimension: specificity)*
`SINGLE-ARTIFACT` -> `topic-report` | `CROSS-SIGNAL` -> SURPRISE
Commit: `Stage 3: [{item}] -> [SINGLE-ARTIFACT | CROSS-SIGNAL] -- sources: [{a1}, {a2}]`

---

### Step 4 -- [NODE 3: comparative triage rank] *(C-23; C-22)*

Comparative. HIGH | MEDIUM | LOW. Failure-first within tier. All before expansion.

---

### Step 5 -- [NODE 4: naming scaffold]
*(C-17; C-21; IA: false-assumption-recovery; epistemic dimension: belief-inversion)*

1. Old belief. 2. Correction. 3. Domain. 4. Form: `The {Corrected Belief}: {Domain}`.
VALID: "The Silent Veto: Adoption Workflow". INVALID: "Surprising Finding About Adoption".

---

### Step 6 -- [NODE 5: pre-expansion co-validation gate]
*(C-20; IA: false-assumption-recovery; epistemic dimension: correction-integrity)*

Both VALID required. Either failing blocks expansion.
- Name form *(C-17)*: `The {Corrected Belief}: {Domain}`? -> VALID / INVALID
- Failure field *(C-18)*: "If next team carries old assumption, {specific mis-design}"?
  -> VALID / INVALID

---

### Step 7 -- [NODE 6: echo entry]
*(IA: false-assumption-recovery; epistemic dimension: failure-projection;*
*C-02..C-04; C-08; C-12; C-14; C-17; C-18; C-22)*

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

### Step 8 -- [NODE 7: cross-signal synthesis]
*(C-05; IA: false-assumption-recovery; epistemic dimension: pattern-emergence)*

<=120 words. Name >=2 entries by exact label. Cross-entry pattern only.

---

### Step 9 -- [NODE 8: forward handover guidance]
*(C-06; C-19; IA: false-assumption-recovery; epistemic dimension: future-framing)*

T-1..T-4 register. State selection. Verify slots. Scenario and constraint specific.

---

### Step 10 -- [NODE 9: impact-anchored rules] + [NODE 10: TRACE-CHECK-VERDICT]
*(C-07; C-24)*

*(C-37: TRACE-CHECK-VERDICT is NODE 10.)*

```
TRACE-CHECK-VERDICT: [PASS | FAIL]
  -- PASS: all tiers match; no orphan rules; one-rule-per-surprise confirmed
  -- FAIL: {rule label | expected tier | actual tier}
```
*Forward-reader protocol (C-34): verifiable by TRACE-CHECK-VERDICT token location.*

---

### Step 11 -- [NODE 11: gestalt audit] + [NODE 12: GESTALT-VERDICT]
*(C-26)*

*(C-37: GESTALT-VERDICT is NODE 12.)*

"Could this output be described as a summary or survey?" If YES: revise.

```
GESTALT-VERDICT: [PASS | FAIL]
  -- PASS: output does not read as survey in aggregate
  -- FAIL: {entry label, gestalt-summary-fail trigger, revision applied}
```
*Forward-reader protocol (C-34): verifiable by GESTALT-VERDICT token location.*

---

### Step 12 -- [NODE 13: back-fill guard] + [NODE 14: BACK-FILL-VERDICT]
*(C-44: detection protocol ordered BEFORE trace assembly step NODE 15)*

```
BACK-FILL-GUARD (C-44)
---------------------------------------------------------------------
Ordered BEFORE assembly (NODE 15). Verifies Steps 2-12 each carry an inline
[NODE N: {role}] declaration in the step header.
---------------------------------------------------------------------
```

*(C-37: BACK-FILL-VERDICT is NODE 14.)*

```
BACK-FILL-VERDICT: [PASS | FAIL]
  -- PASS: all Steps 2-12 carry inline [NODE N: {role}]; assembly may proceed
  -- FAIL: Step {N} lacks inline node declaration
```
*Forward-reader protocol (C-34): verifiable by BACK-FILL-VERDICT token location.*
*(C-44: NODE 13 ordered before NODE 15.)*

---

### Step 13 -- [NODE 15: production chain trace]
*(C-28; C-29; C-31; C-38; C-40; C-41)*

Condition: BACK-FILL-VERDICT (NODE 14) must be PASS before proceeding.
[C-46 ABSENT: condition stated in prose; NODE 15 header does not name BACK-FILL-VERDICT
by token name and NODE number as a declared blocking dependency.]

```
STEP-TIME AUTHORITY RULE (C-41) -- WITH NON-VACUITY ASSERTION (C-43)
---------------------------------------------------------------------
This trace assembly step is CONFIRMATORY ONLY.

NON-VACUITY COUNT (C-43): This rule governs [N] step-header node declarations.
N >= 1 confirmed. The rule is operative, not vacuous.

MUST NOT: define, renumber, back-fill, or override any step-time node assignment.
If this trace disagrees with any step header, the step header governs.
Authority: step-execution time -> trace assembly time. Irreversible.
---------------------------------------------------------------------
```

*(C-37: AUTHORITY-VERDICT is NODE 16.)*

```
AUTHORITY-VERDICT TOKEN IDENTITY CONTRACT (C-47)
---------------------------------------------------------------------
NODE assignment (C-37): AUTHORITY-VERDICT is NODE 16 in the production chain.
  A model executing this step sees NODE 16 identity without consulting the
  terminal chain trace.

Forward-reader rationale (C-34): A future reader verifies C-41 compliance by
  locating AUTHORITY-VERDICT; no session replay required. CONFIRMATORY certifies
  step headers are canonical; OVERRIDE-DETECTED certifies each violation by node
  number, step-header declaration, and trace assignment.

Criteria satisfied by this token:
  C-37 (inline NODE assignment at governing step)
  C-41 (step-time authority compliance verification)
  C-43 (non-vacuity count confirmed operative)
  C-45 (dedicated compliance verdict with own NODE assignment)
  Full audit footprint reconstructible from this block without re-reading each
  criterion individually.

Non-identity clause: AUTHORITY-VERDICT is NOT a structural marker embedded in
  C-40's node declaration template (e.g., `| step-time-canonical` attribute).
  It is a standalone chain node. Node identity (C-40) and authority compliance
  (C-41) are carried by distinct tokens, each independently locatable.
---------------------------------------------------------------------
```

```
AUTHORITY-VERDICT: [CONFIRMATORY | OVERRIDE-DETECTED]
  -- CONFIRMATORY: all 17 entries confirm step-time declarations; no back-fill
  -- OVERRIDE-DETECTED: {NODE N | step header declared X | trace assigns Y}
```

```
PRODUCTION CHAIN TRACE
VERIFICATION NODES INCLUDED (C-29) | DEPENDENCY GRAPH CLOSED (C-31)
C-42 PRECONDITION TYPED | C-43 COUNT ACTIVE | C-44 PRE-ASSEMBLY | C-45 DEDICATED TOKEN
C-47: AUTHORITY-VERDICT (NODE 16) CARRIES FULL IDENTITY CONTRACT
======================================================================

[NODE 1]  typed-route prediction sort
  structural qualifier: IA+prior-frame-recovery (C-30+C-32), anti-hyp guard (C-11),
    typed destinations (C-14), non-empty discard log (C-09)
  consumed by: NODE 2

-> [NODE 2]  staged gate verdict
  structural qualifier: Gatekeeper+dimension per stage (C-30+C-32), commit tokens
    (C-13+C-16), We-believed gallery Stage 2, cross-signal Stage 3, floor (C-15)
  consumed by: NODE 3, NODE 17

-> [NODE 3]  comparative triage rank
  structural qualifier: simultaneous comparison (C-23), failure-first (C-22)
  consumed by: NODE 9, NODE 10

-> [NODE 4]  naming scaffold
  structural qualifier: IA+belief-inversion (C-30+C-32); 4-step (C-21); format (C-17)
  consumed by: NODE 5

-> [NODE 5]  pre-expansion co-validation gate
  structural qualifier: both-VALID blocking (C-20)
  consumed by: NODE 6

-> [NODE 6]  echo entry
  structural qualifier: failure-first (C-22); [CROSS] (C-08); failure field (C-18)
  consumed by: NODE 7, NODE 8, NODE 9, NODE 17

-> [NODE 7]  cross-signal synthesis
  structural qualifier: >=2 exact labels; cross-entry (C-05)

-> [NODE 8]  forward handover guidance
  structural qualifier: T-1..T-4 (C-19); slot verification (C-06)

-> [NODE 9]  impact-anchored rules
  consumed by: NODE 10

-> [NODE 10] TRACE-CHECK-VERDICT [C-29; C-34; C-37: NODE 10]

-> [NODE 11] gestalt audit
  consumed by: NODE 12

-> [NODE 12] GESTALT-VERDICT [C-29; C-34; C-37: NODE 12]

-> [NODE 13] back-fill guard [C-44: pre-assembly]
  consumed by: NODE 14

-> [NODE 14] BACK-FILL-VERDICT [C-29; C-34; C-37: NODE 14; C-44]
  consumed by: NODE 15 (prose condition; C-46 ABSENT -- not declared dep in header)

-> [NODE 15] production chain trace (this step)
  structural qualifier: 17 nodes+qualifiers (C-28); C-42 precondition; C-43+C-41;
    C-44; C-47 identity contract on NODE 16; C-38 claim
  note: C-48 ABSENT -- authority block does not open with BACK-FILL-VERDICT citation

-> [NODE 16] AUTHORITY-VERDICT [C-47: full identity contract (NODE+forward-reader+
             satisfies C-37/C-41/C-43/C-45+non-identity clause); C-45; C-29; C-34; C-37]

-> [NODE 17] FLOOR-VERDICT [C-29; C-36; C-34; C-37: NODE 17]

======================================================================
CLOSURE CLAIM (C-38): No inter-criterion dependency discoverable only by reading
the prompt. Known dependencies (12):
  C-23 -> C-24 (NODE 3 -> NODE 10)
  C-26 -> C-28 (NODE 11/12 -> NODE 15)
  C-24 -> C-28 (NODE 10 -> NODE 15)
  C-14 -> C-06 (NODE 6 -> NODE 8)
  C-17+C-21 -> C-20 (NODE 4 -> NODE 5)
  C-15 -> C-36 (NODE 2 -> NODE 17)
  C-36 -> C-28 (NODE 17 -> NODE 15)
  C-40 (structural precondition) -> C-41 (NODE 15) [C-42]
  C-43 -> C-41 (NODE 15) [C-43 count derives from C-40]
  C-44: BACK-FILL-GUARD (NODE 13/14) -> assembly (NODE 15) [C-44]
  C-41 -> C-45 (NODE 15 -> NODE 16) [C-45 dedicated token]
  C-37 -> NODE 14: inline declaration at governing step
Attempt to falsify by reading the full prompt.
```

---

### Dependency Closure Enumeration *(C-33)*

```
DEPENDENCY CLOSURE ENUMERATION
================================
CONTRACT HEADER: Any loop in chain trace but absent here is a C-33 violation. (C-39)

C-23 -> C-24 (NODE 3 -> NODE 10)
C-26 -> C-28 (NODE 11/12 -> NODE 15)
C-24 -> C-28 (NODE 10 -> NODE 15)
C-14 -> C-06 (NODE 6 -> NODE 8)
C-17+C-21 -> C-20 (NODE 4 -> NODE 5)
C-15 -> C-36 (NODE 2 -> NODE 17)
C-36 -> C-28 (NODE 17 -> NODE 15)
C-40 (structural precondition) -> C-41 (NODE 15) [C-42]
C-43 -> C-41 (NODE 15) [C-43 count derives from C-40 declarations]
C-44: BACK-FILL-GUARD (NODE 13/14) -> assembly (NODE 15) [C-44]
C-41 -> C-45 (NODE 15 -> NODE 16) [C-45 dedicated token]
C-37 -> NODE 14: inline declaration at back-fill guard step
================================
12 loops enumerated.
Any loop absent from this enumeration that appears in the chain trace is a
C-33 violation. (C-39 postamble)
[C-49 ABSENT: no version-aligned closing tag for v14 new criteria]
```

---

**Final output sequence** *(C-35)*:
1. Echo entries *(C-02; C-04; C-07; C-08; C-12; C-14; C-17; C-18; C-22)*
2. Cross-signal synthesis *(C-05)*
3. Forward handover guidance *(C-06; C-19)*
4. Rules of Thumb *(C-07; C-24)*
5. TRACE-CHECK-VERDICT *(C-24; C-29; C-34; C-37: NODE 10)*
6. GESTALT-VERDICT *(C-26; C-29; C-34; C-37: NODE 12)*
7. BACK-FILL-VERDICT *(C-44; C-29; C-34; C-37: NODE 14)*
8. Production chain trace -- 17 nodes; C-41+C-43; C-42 precondition; C-47 identity
   contract on NODE 16 *(C-28; C-29; C-31; C-38; C-40; C-41; C-42; C-43; C-44; C-47)*
   [C-46 ABSENT: NODE 15 header has prose condition, not named dep declaration]
9. AUTHORITY-VERDICT *(C-47: full identity contract; C-45; C-29; C-34; C-37: NODE 16)*
10. Dependency Closure Enumeration -- 12 loops *(C-33; C-39)* [C-49 ABSENT]
11. FLOOR-VERDICT *(C-36; C-37: NODE 17)*

### Step 14 -- [NODE 17: FLOOR-VERDICT]

*(C-37: FLOOR-VERDICT is NODE 17.)*

```
FLOOR-VERDICT: [PASS | FLOOR-MISS]
  -- PASS: distinct surprise count >= 3 confirmed in final output
  -- FLOOR-MISS: {count} surprises; shortfall: {3 - count}
```
*Forward-reader protocol (C-34): verifiable by FLOOR-VERDICT token location.*
*(C-36: Separate from gate-time floor check in Step 3 Stage 2.)*

---

## V-03 -- Single-axis: Authority block cites detection verdict (C-48)

**Variation axis:** The authority block opens by citing BACK-FILL-VERDICT (NODE 14) by
name and NODE number before stating the non-vacuity count: "BACK-FILL-VERDICT (NODE 14):
confirmed PASS prior to this step (C-44 satisfied)." This operationally links C-43
(non-vacuity count) and C-44 (pre-assembly ordering) in one block.

**Hypothesis:** Without C-48, C-43 and C-44 are satisfied in isolation: the authority
block carries a count (C-43 PASS), and the guard precedes assembly (C-44 PASS), but a
model executing the authority block must locate NODE 14 separately to confirm C-44
compliance. C-48 converts two separately-verifiable criteria into a jointly-verifiable
precondition chain. C-46 absent -- NODE 15 header carries no named dep declaration.
C-47 absent -- AUTHORITY-VERDICT has no satisfied-criteria enumeration or non-identity
clause. C-49 absent.
Predicted: C-48 PASS; C-46 FAIL; C-47 FAIL; C-49 FAIL; all C-09..C-45 inherited.

**Builds on:** R13 V-05 -- all 37 criteria (C-09..C-45) active. 17 nodes. 12 deps.

---

### Prompt Body

You are running `/quest:topic echo` for the topic: {topic}.

All essential signals are in hand. Your task: surface the genuine surprises -- findings
that only became visible in retrospect, from cross-signal tension, that no competent
practitioner would have predicted before gathering evidence.

Not a summary. Not a survey of discoveries. An echo: the signal that comes back that
you did not send.

---

### Roles *(C-25; C-30; C-32)*

**Institutional Archaeologist (IA)**
*First invocation: Step 2.*
Function: Recovers false assumptions embedded in current materials. Frames every surprise
as a correction to a false assumption (C-17). Derives consequence: "What would the next
team build wrong?" (C-18, C-22).

Sub-step co-activation: `IA: false-assumption-recovery; epistemic dimension: {name}`

| Step | Epistemic Dimension    | Why here                                              |
|------|------------------------|-------------------------------------------------------|
| 2    | prior-frame-recovery   | Recovering what was actually believed, not spec text  |
| 5    | belief-inversion       | Deriving correction-encoding name by inverting belief |
| 6    | correction-integrity   | Verifying both form checks encode the correction      |
| 7    | failure-projection     | Anchoring entry in projected mis-design               |
| 8    | pattern-emergence      | What only emerges when entries are read together      |
| 9    | future-framing         | Translating findings to guidance for future builder   |

**Gatekeeper** *First invocation: Step 3.*

```
GATEKEEPER -- FUNCTION DECLARATION (C-27)
---------------------------------------------------------------------
Function:      Adversarial rejection. Tests: (1) first-principles predictability;
               (2) cross-signal requirement. Fails either: rejected.
Not-function:  Future-reader framing (IA's domain).
Role boundary: Gatekeeper verdicts are final.
---------------------------------------------------------------------
```

---

### Step 1 -- Read Signal Record *(C-10; C-12)*

All namespaces (scout, draft, review, flow, trace, prove, listen, program, topic).
Record: namespaces covered (>=3 floor), total artifacts, date range.
Scaffolding -- does not enter the production chain.

---

### Step 2 -- [NODE 1: typed-route prediction sort]
*(IA: false-assumption-recovery; epistemic dimension: prior-frame-recovery; C-16; C-14; C-11; C-09)*

Routes: `topic-story` | `topic-report` | `gate-pipeline`
Anti-hypothesis guard (C-11): "Confirms investigation hypothesis?" YES -> `topic-story`.
Discard log (C-09): every non-gate item, route type, reason. Non-empty required.

---

### Step 3 -- [NODE 2: staged gate verdict]
*(Gatekeeper: adversarial-rejection-only; C-13; C-15; C-16)*

Anti-Pattern Catalog (C-13): CONFIRMATION | RESTATEMENT | ISOLATED-FINDING
Gate format (C-16): `VERDICT: SURPRISE | CUT -- {label}`

Stage 1 -- Prediction Test (epistemic: novelty):
  `PREDICTABLE` -> `topic-story` | `UNPREDICTABLE` -> Stage 2

Stage 2 -- Contradiction Test (epistemic: opposition):
  `We believed:` gallery. Floor (C-15): >=3 CONTRADICTION FOUND.

Stage 3 -- Attribution Test (epistemic: specificity):
  `SINGLE-ARTIFACT` -> `topic-report` | `CROSS-SIGNAL` -> SURPRISE

---

### Step 4 -- [NODE 3: comparative triage rank] *(C-23; C-22)*

Comparative. HIGH | MEDIUM | LOW. Failure-first within tier. All before expansion.

---

### Step 5 -- [NODE 4: naming scaffold]
*(C-17; C-21; IA: false-assumption-recovery; epistemic dimension: belief-inversion)*

1. Old belief. 2. Correction. 3. Domain. 4. Form: `The {Corrected Belief}: {Domain}`.
VALID: "The Silent Veto: Adoption Workflow". INVALID: "Surprising Finding About Adoption".

---

### Step 6 -- [NODE 5: pre-expansion co-validation gate]
*(C-20; IA: false-assumption-recovery; epistemic dimension: correction-integrity)*

Both VALID required. Either failing blocks expansion.
- Name form (C-17): `The {Corrected Belief}: {Domain}`? -> VALID / INVALID
- Failure field (C-18): "If next team carries old assumption, {specific mis-design}"?
  -> VALID / INVALID

---

### Step 7 -- [NODE 6: echo entry]
*(IA: false-assumption-recovery; epistemic dimension: failure-projection;*
*C-02..C-04; C-08; C-12; C-14; C-17; C-18; C-22)*

Begin from failure (C-22): anchor the mis-design first.

**[`The {Corrected Belief}: {Domain}`]** -- *{HIGH | MEDIUM | LOW}*

Source signal: `{artifact-name} ({namespace}/{skill})`
`[CROSS: {artifact-A} x {artifact-B}]` (C-08)
Temporal anchor (C-12): `{round or date}`
We believed: `{falsifiable assumption}`
The surprise: `{what signals revealed}`
If the next team carries old assumption (C-18): `{specific concrete mis-design}`.
Design impact (C-03): `{decision revisited / assumption struck / scope boundary shifted}`.
Downstream route (C-14): `-> {skill or namespace}`.

---

### Step 8 -- [NODE 7: cross-signal synthesis]
*(C-05; IA: false-assumption-recovery; epistemic dimension: pattern-emergence)*

<=120 words. Name >=2 entries by exact label. Cross-entry pattern only.

---

### Step 9 -- [NODE 8: forward handover guidance]
*(C-06; C-19; IA: false-assumption-recovery; epistemic dimension: future-framing)*

T-1..T-4 register. State selection. Verify slots. Scenario and constraint specific.

---

### Step 10 -- [NODE 9: impact-anchored rules] + [NODE 10: TRACE-CHECK-VERDICT]
*(C-07; C-24)*

*(C-37: TRACE-CHECK-VERDICT is NODE 10.)*

TRACE-CHECK-VERDICT token: PASS = all tiers match; no orphan rules.
FAIL = {rule label | expected tier | actual tier}.
Forward-reader protocol (C-34): verifiable by token location.

---

### Step 11 -- [NODE 11: gestalt audit] + [NODE 12: GESTALT-VERDICT]
*(C-26)*

*(C-37: GESTALT-VERDICT is NODE 12.)*

"Could this output be described as a summary or survey?" If YES: revise.
GESTALT-VERDICT: PASS | FAIL. Forward-reader protocol (C-34).

---

### Step 12 -- [NODE 13: back-fill guard] + [NODE 14: BACK-FILL-VERDICT]
*(C-44: detection protocol ordered BEFORE trace assembly step NODE 15)*

BACK-FILL-GUARD: verifies Steps 2-12 each carry inline [NODE N: {role}] in step header.
*(C-37: BACK-FILL-VERDICT is NODE 14.)*
BACK-FILL-VERDICT: PASS = all present; FAIL = Step {N} lacks header.
Forward-reader protocol (C-34). (C-44: NODE 13 ordered before NODE 15.)

---

### Step 13 -- [NODE 15: production chain trace]
*(C-28; C-29; C-31; C-38; C-40; C-41)*

Condition: BACK-FILL-VERDICT (NODE 14) must be PASS before proceeding.
[C-46 ABSENT: condition stated in prose; NODE 15 step header carries no named dep
declaration on BACK-FILL-VERDICT by token name and NODE number.]

```
STEP-TIME AUTHORITY RULE (C-41) WITH NON-VACUITY ASSERTION (C-43)
AND DETECTION VERDICT CITATION (C-48)
---------------------------------------------------------------------
BACK-FILL-VERDICT (NODE 14): confirmed PASS prior to this step (C-44 satisfied).
This trace assembly step is CONFIRMATORY ONLY.

NON-VACUITY COUNT (C-43): This rule governs [N] step-header node declarations.
N >= 1 confirmed. The rule is operative, not vacuous.

The opening citation above operationally links C-43 and C-44 in this single block:
a model executing this step verifies both (1) detection ran before assembly (C-44
satisfied, cited above) and (2) governed population is nonzero (C-43 count stated
immediately above) without consulting separate steps.

MUST NOT: define, renumber, back-fill, or override any step-time node assignment.
If this trace disagrees with any step header, the step header governs.
Authority: step-execution time -> trace assembly time. Irreversible.
---------------------------------------------------------------------
```

*(C-37: AUTHORITY-VERDICT is NODE 16.)*

AUTHORITY-VERDICT: CONFIRMATORY = all 17 entries confirm step-time declarations.
OVERRIDE-DETECTED = {NODE N | step header declared X | trace assigns Y}.
Forward-reader protocol (C-34): verifiable by token location.
(C-45: AUTHORITY-VERDICT is dedicated compliance token, not a template marker. NODE 16.)
[C-47 ABSENT: no satisfied-criteria enumeration; no explicit non-identity clause.]

```
PRODUCTION CHAIN TRACE
C-42 PRECONDITION TYPED | C-43+C-48 AUTHORITY BLOCK | C-44 PRE-ASSEMBLY | C-45 TOKEN
======================================================================
NODE 1:  typed-route prediction sort [IA+prior-frame-recovery; C-11; C-14; C-09]
NODE 2:  staged gate verdict [Gatekeeper; C-13+C-16+C-15; C-18; cross-signal]
NODE 3:  comparative triage rank [C-23; C-22]
NODE 4:  naming scaffold [IA+belief-inversion; C-21; C-17]
NODE 5:  pre-expansion co-validation gate [both-VALID blocking; C-20]
NODE 6:  echo entry [IA+failure-projection; failure-first C-22; C-08; C-18; C-03]
NODE 7:  cross-signal synthesis [IA+pattern-emergence; >=2 labels; C-05]
NODE 8:  forward handover guidance [IA+future-framing; T-1..T-4; C-19; C-06]
NODE 9:  impact-anchored rules [tier vs NODE 3; orphan check; C-24]
NODE 10: TRACE-CHECK-VERDICT [C-29; C-34; C-37: NODE 10]
NODE 11: gestalt audit [C-26]
NODE 12: GESTALT-VERDICT [C-29; C-34; C-37: NODE 12]
NODE 13: back-fill guard [C-44: pre-assembly; scans Steps 2-12]
NODE 14: BACK-FILL-VERDICT [C-29; C-34; C-37: NODE 14; C-44]
  consumed by: NODE 15 (prose condition; C-46 ABSENT)
  also consumed by: NODE 15 authority block (C-48: cited at authority block open)
NODE 15: production chain trace -- this step
  [C-48 authority citation; C-42 precondition; C-43 count; C-44; C-38 claim]
  [C-46 ABSENT; C-47 ABSENT on NODE 16]
NODE 16: AUTHORITY-VERDICT [C-29; C-34; C-37: NODE 16; C-45: dedicated] [C-47 ABSENT]
NODE 17: FLOOR-VERDICT [C-29; C-36; C-34; C-37: NODE 17]
======================================================================
CLOSURE CLAIM (C-38): No inter-criterion dependency discoverable only by reading
the prompt. 12 deps (C-48 makes C-44 dep explicit within authority block but does
not add a new inter-criterion graph loop). Attempt to falsify by reading the prompt.
```

---

### Dependency Closure Enumeration *(C-33)*

```
DEPENDENCY CLOSURE ENUMERATION
================================
CONTRACT HEADER: Any loop in chain trace but absent here is a C-33 violation. (C-39)

C-23 -> C-24 (NODE 3 -> NODE 10)
C-26 -> C-28 (NODE 11/12 -> NODE 15)
C-24 -> C-28 (NODE 10 -> NODE 15)
C-14 -> C-06 (NODE 6 -> NODE 8)
C-17+C-21 -> C-20 (NODE 4 -> NODE 5)
C-15 -> C-36 (NODE 2 -> NODE 17)
C-36 -> C-28 (NODE 17 -> NODE 15)
C-40 (structural precondition) -> C-41 (NODE 15) [C-42]
C-43 -> C-41 (NODE 15) [count derives from C-40]
C-44: BACK-FILL-GUARD (NODE 13/14) -> assembly (NODE 15) [C-44]
C-41 -> C-45 (NODE 15 -> NODE 16) [C-45 dedicated token]
C-37 -> NODE 14: inline declaration at governing step
================================
12 loops enumerated.
Any loop absent from this enumeration that appears in the chain trace is a
C-33 violation. (C-39 postamble)
[C-49 ABSENT: no version-aligned closing tag for v14 new criteria]
```

---

**Final output sequence** *(C-35)*:
1-7. Echo entries through BACK-FILL-VERDICT (same as V-01/V-02).
8. Production chain trace -- 17 nodes; C-43+C-48 authority block opens with verdict
   citation; C-42 precondition; C-44 pre-assembly. [C-46 ABSENT; C-47 ABSENT]
9. AUTHORITY-VERDICT (C-45; C-29; C-34; C-37: NODE 16) [C-47 ABSENT]
10. Dependency Closure Enumeration -- 12 loops (C-33; C-39) [C-49 ABSENT]
11. FLOOR-VERDICT (C-36; C-37: NODE 17)

### Step 14 -- [NODE 17: FLOOR-VERDICT]

*(C-37: FLOOR-VERDICT is NODE 17.)*
FLOOR-VERDICT: PASS = distinct surprise count >= 3; FLOOR-MISS = {count}; shortfall {3-count}.
Forward-reader protocol (C-34). (C-36: Separate from gate-time floor check in Step 3.)

---

## V-04 -- Combined: Assembly dep declaration + token identity contract (C-46 + C-47)

**Variation axis:** Two criteria that govern the same token (AUTHORITY-VERDICT / NODE 16)
from different angles are combined. C-46 requires NODE 15's step header to declare
BACK-FILL-VERDICT (NODE 14) as a named blocking dependency. C-47 requires NODE 16's
introduction block to carry a full four-part identity contract. Together they test
whether declaring the dep at the assembly header (C-46) and making the token self-
documenting (C-47) can coexist without structural interference. C-48 absent -- authority
block does not open with verdict citation. C-49 absent.
Predicted: C-46 PASS; C-47 PASS; C-48 FAIL; C-49 FAIL; all C-09..C-45 inherited.

**Builds on:** R13 V-05 -- all 37 criteria (C-09..C-45) active. 17 nodes. 12 deps.

---

### Prompt Body

You are running `/quest:topic echo` for the topic: {topic}.

All essential signals are in hand. Your task: surface the genuine surprises -- findings
that only became visible in retrospect, from cross-signal tension, that no competent
practitioner would have predicted before gathering evidence.

Not a summary. Not a survey of discoveries. An echo: the signal that comes back that
you did not send.

---

### Roles *(C-25; C-30; C-32)*

**Institutional Archaeologist (IA)**
*First invocation: Step 2.*
Function: Recovers false assumptions. Frames surprises as corrections to false assumptions
(C-17). Derives consequence: "What would the next team build wrong?" (C-18, C-22).
Sub-step co-activation: `IA: false-assumption-recovery; epistemic dimension: {name}`

| Step | Epistemic Dimension  | Why here                                              |
|------|----------------------|-------------------------------------------------------|
| 2    | prior-frame-recovery | Recovering what was actually believed, not spec text  |
| 5    | belief-inversion     | Deriving correction-encoding name by inverting belief |
| 6    | correction-integrity | Verifying both form checks encode the correction      |
| 7    | failure-projection   | Anchoring entry in projected mis-design               |
| 8    | pattern-emergence    | What only emerges when entries are read together      |
| 9    | future-framing       | Translating findings to guidance for future builder   |

**Gatekeeper** *First invocation: Step 3.*
Function: Adversarial rejection. Tests predictability and cross-signal requirement.
Not-function: future-reader framing. Verdicts final.

---

### Step 1 -- Read Signal Record *(C-10; C-12)*

All namespaces. Record: namespaces covered (>=3 floor), total artifacts, date range.
Scaffolding -- does not enter the production chain.

---

### Step 2 -- [NODE 1: typed-route prediction sort]
*(IA: false-assumption-recovery; epistemic dimension: prior-frame-recovery; C-16; C-14; C-11; C-09)*

Routes: `topic-story` | `topic-report` | `gate-pipeline`
Anti-hypothesis guard (C-11). Discard log (C-09): non-empty required.

---

### Step 3 -- [NODE 2: staged gate verdict]
*(Gatekeeper: adversarial-rejection-only; C-13; C-15; C-16)*

Stage 1 Prediction Test (novelty): PREDICTABLE -> topic-story | UNPREDICTABLE -> Stage 2
Stage 2 Contradiction Test (opposition): We believed gallery; floor >= 3 CONTRADICTION FOUND
Stage 3 Attribution Test (specificity): SINGLE-ARTIFACT -> topic-report | CROSS-SIGNAL -> SURPRISE

---

### Step 4 -- [NODE 3: comparative triage rank] *(C-23; C-22)*

Comparative. HIGH | MEDIUM | LOW. Failure-first. All before expansion.

---

### Step 5 -- [NODE 4: naming scaffold]
*(C-17; C-21; IA: false-assumption-recovery; epistemic dimension: belief-inversion)*

1. Old belief. 2. Correction. 3. Domain. 4. Form: `The {Corrected Belief}: {Domain}`.

---

### Step 6 -- [NODE 5: pre-expansion co-validation gate]
*(C-20; IA: false-assumption-recovery; epistemic dimension: correction-integrity)*

Both VALID required (name form C-17 + failure field C-18). Either failing blocks expansion.

---

### Step 7 -- [NODE 6: echo entry]
*(IA: false-assumption-recovery; epistemic dimension: failure-projection; C-02..C-04; C-08; C-12; C-14; C-17; C-18; C-22)*

Begin from failure (C-22). Template: source signal, [CROSS], temporal anchor, We believed,
The surprise, If next team carries old assumption (C-18), Design impact (C-03), route (C-14).

---

### Step 8 -- [NODE 7: cross-signal synthesis]
*(C-05; IA: false-assumption-recovery; epistemic dimension: pattern-emergence)*
<=120 words. >=2 exact labels. Cross-entry pattern only.

---

### Step 9 -- [NODE 8: forward handover guidance]
*(C-06; C-19; IA: false-assumption-recovery; epistemic dimension: future-framing)*
T-1..T-4 register. State selection. Verify slots. Scenario and constraint specific.

---

### Step 10 -- [NODE 9: impact-anchored rules] + [NODE 10: TRACE-CHECK-VERDICT]
*(C-07; C-24)*
*(C-37: TRACE-CHECK-VERDICT is NODE 10.)*
TRACE-CHECK-VERDICT: PASS = tiers match, no orphans. FAIL = {label | expected | actual}.
Forward-reader protocol (C-34): verifiable by token location.

---

### Step 11 -- [NODE 11: gestalt audit] + [NODE 12: GESTALT-VERDICT]
*(C-26)*
*(C-37: GESTALT-VERDICT is NODE 12.)*
"Could this output be described as a summary or survey?" If YES: revise.
GESTALT-VERDICT: PASS | FAIL. Forward-reader protocol (C-34).

---

### Step 12 -- [NODE 13: back-fill guard] + [NODE 14: BACK-FILL-VERDICT]
*(C-44: detection ordered BEFORE assembly NODE 15)*
BACK-FILL-GUARD: verifies Steps 2-12 each carry inline [NODE N: {role}] in step header.
*(C-37: BACK-FILL-VERDICT is NODE 14.)*
BACK-FILL-VERDICT: PASS = all present; FAIL = Step {N} lacks header.
Forward-reader protocol (C-34). (C-44: NODE 13 ordered before NODE 15.)

---

### Step 13 -- [NODE 15: production chain trace]
*(C-28; C-29; C-31; C-38; C-40; C-41)*
*(C-46: requires BACK-FILL-VERDICT (NODE 14): PASS -- assembly is architecturally blocked
without this verdict. Locate BACK-FILL-VERDICT before proceeding.
If BACK-FILL-VERDICT is FAIL: surface the gap; do not proceed.)*

```
STEP-TIME AUTHORITY RULE (C-41) -- WITH NON-VACUITY ASSERTION (C-43)
---------------------------------------------------------------------
This trace assembly step is CONFIRMATORY ONLY.

NON-VACUITY COUNT (C-43): This rule governs [N] step-header node declarations.
N >= 1 confirmed. The rule is operative, not vacuous.

MUST NOT: define, renumber, back-fill, or override any step-time node assignment.
If this trace disagrees with any step header, the step header governs.
Authority: step-execution time -> trace assembly time. Irreversible.
---------------------------------------------------------------------
```

[C-48 ABSENT: authority block does not open with BACK-FILL-VERDICT citation.
The non-vacuity count is stated, but C-43 and C-44 are not operationally linked
within this block -- a model must locate NODE 14 separately to verify C-44.]

*(C-37: AUTHORITY-VERDICT is NODE 16.)*

```
AUTHORITY-VERDICT TOKEN IDENTITY CONTRACT (C-47)
---------------------------------------------------------------------
NODE assignment (C-37): AUTHORITY-VERDICT is NODE 16 in the production chain.
  A model executing this step sees NODE 16 identity without consulting the trace.

Forward-reader rationale (C-34): A future reader verifies C-41 compliance by
  locating AUTHORITY-VERDICT; no session replay required. CONFIRMATORY certifies
  step headers are canonical; OVERRIDE-DETECTED certifies each violation.

Criteria satisfied by this token:
  C-37 (inline NODE assignment at governing step)
  C-41 (step-time authority compliance verification)
  C-43 (non-vacuity count confirmed operative)
  C-45 (dedicated compliance verdict with own NODE assignment)
  Full audit footprint reconstructible from this block without re-reading each
  criterion individually.

Non-identity clause: AUTHORITY-VERDICT is NOT a structural marker embedded in
  C-40's node declaration template (e.g., | step-time-canonical attribute).
  It is a standalone chain node. Node identity (C-40) and authority compliance
  (C-41) are carried by distinct tokens, each independently locatable.
---------------------------------------------------------------------
```

AUTHORITY-VERDICT: CONFIRMATORY | OVERRIDE-DETECTED.
Forward-reader protocol (C-34): stated in identity contract above.

```
PRODUCTION CHAIN TRACE
C-42 PRECONDITION TYPED | C-43 COUNT ACTIVE | C-44 PRE-ASSEMBLY | C-45 DEDICATED TOKEN
C-46: NODE 15 HEADER DECLARES DEP ON BACK-FILL-VERDICT (NODE 14)
C-47: AUTHORITY-VERDICT (NODE 16) CARRIES FULL IDENTITY CONTRACT
======================================================================
NODE 1:  typed-route prediction sort [IA+prior-frame-recovery; C-11; C-14; C-09]
NODE 2:  staged gate verdict [Gatekeeper; C-13+C-16+C-15; C-18; cross-signal]
NODE 3:  comparative triage rank [C-23; C-22]
NODE 4:  naming scaffold [IA+belief-inversion; C-21; C-17]
NODE 5:  pre-expansion co-validation gate [both-VALID blocking; C-20]
NODE 6:  echo entry [IA+failure-projection; failure-first C-22; C-08; C-18; C-03]
NODE 7:  cross-signal synthesis [IA+pattern-emergence; >=2 labels; C-05]
NODE 8:  forward handover guidance [IA+future-framing; T-1..T-4; C-19; C-06]
NODE 9:  impact-anchored rules [tier vs NODE 3; orphan check; C-24]
NODE 10: TRACE-CHECK-VERDICT [C-29; C-34; C-37: NODE 10]
NODE 11: gestalt audit [C-26]
NODE 12: GESTALT-VERDICT [C-29; C-34; C-37: NODE 12]
NODE 13: back-fill guard [C-44: pre-assembly]
NODE 14: BACK-FILL-VERDICT [C-29; C-34; C-37: NODE 14; C-44]
  consumed by: NODE 15 (C-46: declared dep in step header)
NODE 15: production chain trace (this step)
  [C-46 dep declared in header; C-42 precondition; C-43+C-41; C-44; C-38 claim]
  [C-48 ABSENT: authority block does not open with verdict citation]
NODE 16: AUTHORITY-VERDICT [C-47: full identity contract (NODE+forward-reader+
         satisfies C-37/C-41/C-43/C-45+non-identity clause); C-45; C-29; C-34; C-37]
NODE 17: FLOOR-VERDICT [C-29; C-36; C-34; C-37: NODE 17]
======================================================================
CLOSURE CLAIM (C-38): 12 deps. Same as R13 V-05.
Attempt to falsify by reading the full prompt.
```

---

### Dependency Closure Enumeration *(C-33)*

```
DEPENDENCY CLOSURE ENUMERATION
================================
CONTRACT HEADER: Any loop in chain trace but absent here is a C-33 violation. (C-39)

C-23 -> C-24 (NODE 3 -> NODE 10)
C-26 -> C-28 (NODE 11/12 -> NODE 15)
C-24 -> C-28 (NODE 10 -> NODE 15)
C-14 -> C-06 (NODE 6 -> NODE 8)
C-17+C-21 -> C-20 (NODE 4 -> NODE 5)
C-15 -> C-36 (NODE 2 -> NODE 17)
C-36 -> C-28 (NODE 17 -> NODE 15)
C-40 (structural precondition) -> C-41 (NODE 15) [C-42]
C-43 -> C-41 (NODE 15) [count derives from C-40]
C-44+C-46: BACK-FILL-GUARD (NODE 13/14) -> assembly (NODE 15) [C-44+C-46 dep declared]
C-41 -> C-45 (NODE 15 -> NODE 16) [C-45 dedicated token]
C-37 -> NODE 14: inline declaration at governing step
================================
12 loops enumerated.
Any loop absent from this enumeration that appears in the chain trace is a
C-33 violation. (C-39 postamble)
[C-49 ABSENT: no version-aligned closing tag for v14 new criteria]
```

---

**Final output sequence** *(C-35)*:
1-7. Echo entries through BACK-FILL-VERDICT.
8. Production chain trace -- 17 nodes; C-46 dep declared in NODE 15 header; C-47 identity
   contract on NODE 16; C-42 precondition; C-43+C-41; C-44 pre-assembly. [C-48 ABSENT]
9. AUTHORITY-VERDICT (C-47: full identity contract; C-45; C-29; C-34; C-37: NODE 16)
10. Dependency Closure Enumeration -- 12 loops (C-33; C-39) [C-49 ABSENT]
11. FLOOR-VERDICT (C-36; C-37: NODE 17)

### Step 14 -- [NODE 17: FLOOR-VERDICT]

*(C-37: FLOOR-VERDICT is NODE 17.)*
FLOOR-VERDICT: PASS = distinct surprise count >= 3; FLOOR-MISS = {count}; shortfall {3-count}.
Forward-reader protocol (C-34). (C-36: Separate from gate-time floor check in Step 3.)

---

## V-05 -- Full synthesis: C-46 + C-47 + C-48 + C-49

**Variation axis:** All four new criteria integrated simultaneously. (1) Assembly step
header declares BACK-FILL-VERDICT (NODE 14) as blocking dep (C-46). (2) AUTHORITY-VERDICT
introduction carries full four-part identity contract (C-47). (3) Authority block opens
with BACK-FILL-VERDICT citation before non-vacuity count (C-48). (4) Terminal enumeration
closes with version-aligned tag [C-46..C-49] (C-49). 17 nodes. 13 deps.

**Hypothesis:** C-46..C-49 address four independent audit-footprint gaps. V-01..V-04 show
each can be satisfied in isolation. V-05 tests whether all four can be simultaneously
satisfied without interaction failures. Key tensions: (a) C-46 (dep declared in header)
and C-48 (dep cited in authority block) both reference BACK-FILL-VERDICT -- can one
token satisfy both without conflation? (b) C-47 requires AUTHORITY-VERDICT to enumerate
satisfied criteria including C-43, while C-48 requires the authority block to cite
BACK-FILL-VERDICT before C-43's count -- can the four-part contract and the opening
citation coexist in the authority block without obscuring each other? (c) C-49 requires
the enumeration to close with a version-scoped tag listing C-46..C-49 -- does this tag
appear coherently after the C-39 guard? 13 deps: adds one named C-48 operational link
(BACK-FILL-VERDICT NODE 14 consumed inside authority block) to the 12 inherited deps.
Predicted: C-46 PASS; C-47 PASS; C-48 PASS; C-49 PASS; all C-09..C-45 inherited.

**Builds on:** R13 V-05 -- all 37 criteria (C-09..C-45) active. 17 nodes. 12 deps.
V-05 adds 1 new dep loop (C-48 authority block citation) -> 13 deps.

---

### Prompt Body

You are running `/quest:topic echo` for the topic: {topic}.

All essential signals are in hand. Your task: surface the genuine surprises -- findings
that only became visible in retrospect, from cross-signal tension, that no competent
practitioner would have predicted before gathering evidence.

Not a summary. Not a survey of discoveries. An echo: the signal that comes back that
you did not send.

---

### Roles *(C-25; C-30; C-32)*

**Institutional Archaeologist (IA)**
*First invocation: Step 2.*
Function: Recovers false assumptions embedded in current materials -- what a future team
would carry as truth without knowing otherwise. Frames every surprise as a correction to
a false assumption (C-17). Derives consequence: "What would the next team build wrong?"
(C-18, C-22). The IA is the author of implication; the Gatekeeper is the author of
rejection.

Sub-step co-activation shorthand (C-30, C-32):
`IA: false-assumption-recovery; epistemic dimension: {name}` at every invocation.

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
Scaffolding -- does not enter the production chain.

---

### Step 2 -- [NODE 1: typed-route prediction sort]
*(IA: false-assumption-recovery; epistemic dimension: prior-frame-recovery; C-16; C-14; C-11; C-09)*

Routes: `topic-story` | `topic-report` | `gate-pipeline`
Anti-hypothesis guard (C-11): "Confirms investigation hypothesis?" YES -> `topic-story`.
Discard log (C-09): every non-gate item, route type, reason (1 sentence). Non-empty.

---

### Step 3 -- [NODE 2: staged gate verdict]
*(Gatekeeper: adversarial-rejection-only; C-13; C-15; C-16)*

Anti-Pattern Catalog (C-13): CONFIRMATION | RESTATEMENT | ISOLATED-FINDING
Gate format (C-16): `VERDICT: SURPRISE | CUT -- {label}`

**Stage 1 -- Prediction Test** *(epistemic dimension: novelty)*
"Would a competent practitioner have predicted this from first principles?"
`PREDICTABLE` -> `topic-story` | `UNPREDICTABLE` -> Stage 2
Commit: `Stage 1: [{item}] -> [PREDICTABLE | UNPREDICTABLE]`

**Stage 2 -- Contradiction Test** *(epistemic dimension: opposition)*
`We believed:` / VALID / INVALID gallery. Floor (C-15): >=3 CONTRADICTION FOUND.
Commit: `Stage 2: [{item}] -> [NO CONTRADICTION | CONTRADICTION FOUND]`

**Stage 3 -- Attribution Test** *(epistemic dimension: specificity)*
"Does this finding emerge only when >=2 signal artifacts are read together?"
`SINGLE-ARTIFACT` -> `topic-report` | `CROSS-SIGNAL` -> SURPRISE
Commit: `Stage 3: [{item}] -> [SINGLE-ARTIFACT | CROSS-SIGNAL] -- sources: [{a1}, {a2}]`

---

### Step 4 -- [NODE 3: comparative triage rank] *(C-23; C-22)*

Comparative. HIGH | MEDIUM | LOW. Failure-first within tier. All before expansion.

---

### Step 5 -- [NODE 4: naming scaffold]
*(C-17; C-21; IA: false-assumption-recovery; epistemic dimension: belief-inversion)*

1. Old belief. 2. Correction. 3. Domain. 4. Form: `The {Corrected Belief}: {Domain}`.
VALID: "The Silent Veto: Adoption Workflow". INVALID: "Surprising Finding About Adoption".

---

### Step 6 -- [NODE 5: pre-expansion co-validation gate]
*(C-20; IA: false-assumption-recovery; epistemic dimension: correction-integrity)*

Both VALID required. Either failing blocks expansion.
- Name form (C-17): `The {Corrected Belief}: {Domain}`? -> VALID / INVALID
- Failure field (C-18): "If next team carries old assumption, {specific mis-design}"?
  -> VALID / INVALID

---

### Step 7 -- [NODE 6: echo entry]
*(IA: false-assumption-recovery; epistemic dimension: failure-projection;*
*C-02..C-04; C-08; C-12; C-14; C-17; C-18; C-22)*

Begin from failure (C-22): anchor the mis-design first.

**[`The {Corrected Belief}: {Domain}`]** -- *{HIGH | MEDIUM | LOW}*
*(IA: false-assumption-recovery; epistemic dimension: failure-projection)*

Source signal: `{artifact-name} ({namespace}/{skill})`
`[CROSS: {artifact-A} x {artifact-B}]` (C-08)
Temporal anchor (C-12): `{round or date}`
We believed: `{falsifiable assumption}`
The surprise: `{what signals revealed}`
If the next team carries old assumption (C-18): `{specific concrete mis-design}`.
Design impact (C-03): `{decision revisited / assumption struck / scope boundary shifted}`.
Downstream route (C-14): `-> {skill or namespace}`.

---

### Step 8 -- [NODE 7: cross-signal synthesis]
*(C-05; IA: false-assumption-recovery; epistemic dimension: pattern-emergence)*

<=120 words. Name >=2 entries by exact label. Cross-entry pattern only.

---

### Step 9 -- [NODE 8: forward handover guidance]
*(C-06; C-19; IA: false-assumption-recovery; epistemic dimension: future-framing)*

T-1..T-4 register. State selection. Verify slots. Scenario and constraint specific.

---

### Step 10 -- [NODE 9: impact-anchored rules] + [NODE 10: TRACE-CHECK-VERDICT]
*(C-07; C-24)*

*(C-37: TRACE-CHECK-VERDICT is NODE 10 in the production chain.)*

TRACE-CHECK-VERDICT: PASS = all tiers match; no orphan rules; one-rule-per-surprise.
FAIL = {rule label | expected tier | actual tier}.
Forward-reader protocol (C-34): A future reader verifies this check ran by locating
TRACE-CHECK-VERDICT; no session replay required.

---

### Step 11 -- [NODE 11: gestalt audit] + [NODE 12: GESTALT-VERDICT]
*(C-26)*

*(C-37: GESTALT-VERDICT is NODE 12 in the production chain.)*

"Could this output be described as a summary or survey?" If YES: revise, log gestalt-summary-fail.
GESTALT-VERDICT: PASS | FAIL. Forward-reader protocol (C-34): verifiable by token location.

---

### Step 12 -- [NODE 13: back-fill guard] + [NODE 14: BACK-FILL-VERDICT]
*(C-44: detection protocol ordered BEFORE trace assembly step NODE 15)*

```
BACK-FILL-GUARD (C-44)
---------------------------------------------------------------------
This step is ordered BEFORE trace assembly (NODE 15). Verifies that every
production, gate, and verification step from Step 2 through Step 12 carries
an inline [NODE N: {role}] declaration in its step header.

  Step header carries [NODE N: {role}] -> DECLARED
  Step header lacks inline declaration -> BACK-FILL-RISK

A trace assembly step operating in confirmatory mode cannot define assignments
for steps that executed without inline headers. This guard confirms no gaps
exist before assembly is permitted to proceed.
---------------------------------------------------------------------
```

*(C-37: BACK-FILL-VERDICT is NODE 14 in the production chain. Inline declaration
satisfies C-37 for this verification token.)*

BACK-FILL-VERDICT: PASS = all Steps 2-12 carry inline [NODE N: {role}]; assembly may
proceed in confirmatory mode. FAIL = Step {N} lacks inline node declaration.
Forward-reader protocol (C-34): A future reader verifies back-fill detection ran by
locating BACK-FILL-VERDICT; no session replay required.
(C-44: BACK-FILL-GUARD is NODE 13, ordered before assembly step NODE 15.
BACK-FILL-VERDICT is NODE 14, consumed by -- not produced inside -- NODE 15.)

---

### Step 13 -- [NODE 15: production chain trace]
*(C-28; C-29; C-31; C-38; C-40; C-41)*
*(C-46: requires BACK-FILL-VERDICT (NODE 14): PASS -- assembly is architecturally blocked
without this verdict. Locate BACK-FILL-VERDICT before proceeding.
If BACK-FILL-VERDICT is FAIL: surface the gap; do not proceed to trace assembly.)*

```
STEP-TIME AUTHORITY RULE (C-41) WITH NON-VACUITY ASSERTION (C-43)
AND DETECTION VERDICT CITATION (C-48)
---------------------------------------------------------------------
BACK-FILL-VERDICT (NODE 14): confirmed PASS prior to this step (C-44 satisfied).
This trace assembly step is CONFIRMATORY ONLY.

NON-VACUITY COUNT (C-43): This rule governs [N] step-header node declarations --
the inline [NODE N: {role}] headers carried by Steps 2-12 in this execution.
N >= 1 confirmed. The rule governs a nonzero population; it is operative.

The opening citation of BACK-FILL-VERDICT (NODE 14) above operationally links
C-43 (non-vacuity count) and C-44 (pre-assembly ordering) in this single block:
a model executing this authority step can verify both (1) detection ran before
assembly (C-44 satisfied, cited above) and (2) governed population is nonzero
(C-43 count stated immediately above) without consulting separate steps.

MUST NOT: define, renumber, back-fill, or override any step-time node assignment.
If this trace disagrees with any step header, the step header governs.
Authority: step-execution time -> trace assembly time. Irreversible.
---------------------------------------------------------------------
```

*(C-37: AUTHORITY-VERDICT is NODE 16 in the production chain. Inline declaration
satisfies C-37 for this verification token.)*

```
AUTHORITY-VERDICT TOKEN IDENTITY CONTRACT (C-47)
---------------------------------------------------------------------
NODE assignment (C-37): AUTHORITY-VERDICT is NODE 16 in the production chain.
  A model executing this step sees NODE 16 identity without consulting the
  terminal chain trace.

Forward-reader rationale (C-34): A future reader verifies C-41 compliance by
  locating AUTHORITY-VERDICT; no session replay required. CONFIRMATORY certifies
  step headers are canonical; OVERRIDE-DETECTED certifies each violation by node
  number, step-header declaration, and trace assignment.

Criteria satisfied by this token:
  C-37 (inline NODE assignment at governing step)
  C-41 (step-time authority compliance verification)
  C-43 (non-vacuity count confirmed operative via N count in authority block)
  C-45 (dedicated compliance verdict token with own NODE assignment)
  Full audit footprint reconstructible from this block without re-reading C-37,
  C-41, C-43, or C-45 individually.

Non-identity clause: AUTHORITY-VERDICT is NOT a structural marker embedded in
  C-40's node declaration template (e.g., | step-time-canonical attribute).
  It is a standalone chain node. Node identity (C-40) and authority compliance
  (C-41) are carried by distinct tokens, each independently locatable.
---------------------------------------------------------------------
```

AUTHORITY-VERDICT: CONFIRMATORY = all 17 entries confirm step-time declarations; no
back-fill. OVERRIDE-DETECTED = {NODE N | step header declared X | trace assigns Y}.
Forward-reader protocol (C-34): stated in identity contract above.

```
PRODUCTION CHAIN TRACE
VERIFICATION NODES INCLUDED (C-29) | DEPENDENCY GRAPH CLOSED (C-31)
C-42 PRECONDITION TYPED | C-43+C-48 AUTHORITY BLOCK | C-44 PRE-ASSEMBLY
C-45 DEDICATED TOKEN | C-46 ASSEMBLY DEP DECLARED | C-47 TOKEN IDENTITY CONTRACT
======================================================================
NODE 1:  typed-route prediction sort
  [IA+prior-frame-recovery (C-30+C-32); anti-hyp guard (C-11); typed dest (C-14); discard (C-09)]
NODE 2:  staged gate verdict
  [Gatekeeper+dimension/stage (C-30+C-32); C-13+C-16+C-15; We-believed (C-18); cross-signal]
  consumed by: NODE 3, NODE 17
NODE 3:  comparative triage rank [C-23; C-22; consumed by NODE 9, NODE 10]
NODE 4:  naming scaffold [IA+belief-inversion (C-30+C-32); C-21; C-17; consumed by NODE 5]
NODE 5:  pre-expansion co-validation gate [both-VALID blocking (C-20); consumed by NODE 6]
NODE 6:  echo entry [IA+failure-projection (C-30+C-32); failure-first C-22; C-08; C-18; C-03]
  consumed by: NODE 7, NODE 8, NODE 9, NODE 17
NODE 7:  cross-signal synthesis [IA+pattern-emergence (C-30+C-32); >=2 exact labels; C-05]
NODE 8:  forward handover guidance [IA+future-framing (C-30+C-32); T-1..T-4; C-19; C-06]
NODE 9:  impact-anchored rules [tier vs NODE 3 (C-24); orphan check; consumed by NODE 10]
NODE 10: TRACE-CHECK-VERDICT [C-29; C-34; C-37: NODE 10]
NODE 11: gestalt audit [C-26; consumed by NODE 12]
NODE 12: GESTALT-VERDICT [C-29; C-34; C-37: NODE 12]
NODE 13: back-fill guard [C-44: pre-assembly detection; scans Steps 2-12]
NODE 14: BACK-FILL-VERDICT [C-29; C-34; C-37: NODE 14; C-44: pre-assembly verdict]
  consumed by: NODE 15 header (C-46: declared blocking dep)
  consumed by: NODE 15 authority block (C-48: cited at authority block open)
NODE 15: production chain trace (this step)
  [17 nodes+qualifiers (C-28); verification in chain (C-29); C-40->C-41 precondition
  typed (C-31+C-42); C-41+C-43 authority with C-48 opening citation; C-44+C-46 dep
  declared in header; C-47 identity contract on NODE 16; C-38 closure claim]
NODE 16: AUTHORITY-VERDICT
  [C-47: full identity contract (NODE+forward-reader+satisfies C-37/C-41/C-43/C-45
  +non-identity clause); C-45: dedicated token; C-29; C-34; C-37: NODE 16]
NODE 17: FLOOR-VERDICT [C-29; C-36; C-34; C-37: NODE 17; separate from NODE 2 floor]
======================================================================
CLOSURE CLAIM (C-38): No inter-criterion dependency discoverable only by reading
the prompt. Known dependencies (13):
  C-23 -> C-24 (NODE 3 -> NODE 10)
  C-26 -> C-28 (NODE 11/12 -> NODE 15)
  C-24 -> C-28 (NODE 10 -> NODE 15)
  C-14 -> C-06 (NODE 6 -> NODE 8)
  C-17+C-21 -> C-20 (NODE 4 -> NODE 5)
  C-15 -> C-36 (NODE 2 -> NODE 17)
  C-36 -> C-28 (NODE 17 -> NODE 15)
  C-40 (structural precondition) -> C-41 (NODE 15) [C-42]
  C-43 -> C-41 (NODE 15) [count derives from C-40; C-43 depends on C-42]
  C-44+C-46: BACK-FILL-GUARD (NODE 13/14) -> assembly (NODE 15) header [C-44+C-46]
  C-48: BACK-FILL-VERDICT (NODE 14) -> authority block within NODE 15 [C-48 citation]
  C-41 -> C-45 (NODE 15 -> NODE 16) [C-45 dedicated token; C-37 inline at NODE 15]
  C-37 -> NODE 14: BACK-FILL-VERDICT inline declaration at governing step
Attempt to falsify by reading the full prompt.
```

---

### Dependency Closure Enumeration *(C-33)*

```
DEPENDENCY CLOSURE ENUMERATION
================================
CONTRACT HEADER: Any loop in chain trace but absent here is a C-33 violation. (C-39)

C-23 -> C-24 (NODE 3 -> NODE 10): triage rank feeds tier-match check
C-26 -> C-28 (NODE 11/12 -> NODE 15): gestalt verdict is named chain node
C-24 -> C-28 (NODE 10 -> NODE 15): traceability verdict is named chain node
C-14 -> C-06 (NODE 6 -> NODE 8): routing tags feed handover scenario
C-17+C-21 -> C-20 (NODE 4 -> NODE 5): naming scaffold feeds co-validation gate
C-15 -> C-36 (NODE 2 -> NODE 17): gate-time floor count feeds terminal check
C-36 -> C-28 (NODE 17 -> NODE 15): FLOOR-VERDICT is named chain node
C-40 (structural precondition) -> C-41 (NODE 15): C-41 governs step-header
  declarations; C-40 is structural precondition for that population [C-42]
C-43 -> C-41 (NODE 15): non-vacuity count in authority block; derives from C-40 [C-43]
C-44+C-46: BACK-FILL-GUARD (NODE 13/14) -> assembly (NODE 15) header: dep declared
  in NODE 15 step header by name and NODE number [C-44+C-46]
C-48: BACK-FILL-VERDICT (NODE 14) -> authority block within NODE 15: verdict cited
  at open of authority block, linking C-43 and C-44 operationally [C-48]
C-41 -> C-45 (NODE 15 -> NODE 16): authority compliance produces dedicated verdict
  token; C-37 inline at NODE 15 [C-45]
C-37 -> NODE 14: BACK-FILL-VERDICT inline node declaration at back-fill guard step
================================
13 loops enumerated.
Any loop absent from this enumeration that appears in the chain trace is a
C-33 violation. (C-39 postamble)
[C-46 assembly dep declared; C-47 token identity contract; C-48 authority cites verdict; C-49 version-aligned tag]
```

---

**Final output sequence** *(C-35)*:
1. Echo entries *(failure-first; C-02; C-04; C-07; C-08; C-12; C-14; C-17; C-18; C-22)*
2. Cross-signal synthesis *(C-05)*
3. Forward handover guidance *(C-06; C-19)*
4. Rules of Thumb *(C-07; C-24)*
5. TRACE-CHECK-VERDICT *(C-24; C-29; C-34; C-37: NODE 10)*
6. GESTALT-VERDICT *(C-26; C-29; C-34; C-37: NODE 12)*
7. BACK-FILL-VERDICT *(C-44: pre-assembly; C-29; C-34; C-37: NODE 14)*
8. Production chain trace -- 17 nodes; C-46 dep in NODE 15 header; C-43+C-48 authority
   block with verdict citation; C-47 identity contract on NODE 16; C-42 precondition
   *(C-28; C-29; C-31; C-38; C-40; C-41; C-42; C-43; C-44; C-45; C-46; C-47; C-48)*
9. AUTHORITY-VERDICT (C-47: full identity contract including satisfies-enumeration and
   non-identity clause; C-45: dedicated token; C-29; C-34; C-37: NODE 16)
10. Dependency Closure Enumeration -- 13 loops *(C-33; C-39; C-49: version-aligned
    closing tag [C-46 assembly dep declared; C-47 token identity contract;
    C-48 authority cites verdict; C-49 version-aligned tag])*
11. FLOOR-VERDICT *(C-36; C-37: NODE 17)*

### Step 14 -- [NODE 17: FLOOR-VERDICT]

*(C-37: FLOOR-VERDICT is NODE 17 in the production chain. Inline declaration satisfies
C-37 for this verification token.)*

FLOOR-VERDICT: PASS = distinct surprise count >= 3 confirmed in final output.
FLOOR-MISS = {count} surprises; shortfall: {3 - count} required.
Forward-reader protocol (C-34): A future reader verifies floor compliance by locating
FLOOR-VERDICT; no session replay required.
(C-36: Separate from gate-time floor check in Step 3 Stage 2.)
