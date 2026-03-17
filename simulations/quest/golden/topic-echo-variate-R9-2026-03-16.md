---
skill: quest-variate
skill_target: topic-echo
date: 2026-03-16
round: 9
rubric: v9
rubric_file: simulations/quest/rubrics/topic-echo-rubric-v9-2026-03-16.md
rubric_max: 200
---

# Variations: `topic:echo` -- Round 9 (2026-03-16)

**Rubric:** v9 (2026-03-16) | **Criteria count:** 30 (5 essential / 3 recommended / 22 aspirational)

---

## Design Context

R8 V-05 achieves 200/200 under v9 -- the rubric ceiling. Round 9 begins at full
convergence on all 30 criteria. The purpose of R9 variations is therefore not to
maximize v9 score (the base already does) but to explore whether structural patterns
exist that the v9 rubric does not yet capture. Three such gaps are visible when the
R8 V-05 prompt is examined against the question: "Which structural commitments does
this prompt enforce but not make auditable from output alone?"

**Gap identification:**

The v9 rubric's progression -- visibility -> navigability -> primacy -> repairability /
stakes / verifiability -> auditable closure / visual sovereignty / structural provenance
-- reveals a recurring meta-pattern: each round takes an "instruction exists" criterion
and converts it into an "output is auditable without re-running the instruction" criterion.
Three such conversions remain available:

1. **RESOLUTION PROTOCOL accountability gap.** C-25/C-29 require the repair-per-flag-type
   protocol to exist and be visually sovereign. Neither requires the repair to name who
   confirms the fix succeeded. Two reviewers who each follow the PBI-Ref mismatch repair
   may each clear the flag without the same person confirming the same thing. Naming a
   VERIFIER ROLE per repair type makes clearing deterministic at the role level, not just
   at the action level: only the named role can certify resolution.

2. **RULES-ANCHORED-COMPLETE evidentiary gap.** C-28 requires a closure token when all
   rules confirm ALIGNED. The token is declarative: "alignment confirmed." C-18 established
   that attestations must quote actual text, not just identifiers -- because a reviewer
   cannot confirm correct content was checked without seeing the content. The same gap
   exists in the RULES-ANCHORED-COMPLETE token: it asserts alignment without showing what
   tier annotation text was checked per rule. Quoting the tier annotation string for each
   rule converts closure from declarative to evidentiary.

3. **EF invocation traceability gap.** C-30 requires EF role-boundary protection. The
   artifact shows EF ran (ENFORCEMENT MECHANISM section exists with NO-ECHO COST). But
   which pre-investigation materials EF consulted is invisible. A reviewer auditing
   structural provenance must re-derive from scratch. If EF produces a visible
   EF-INVOCATION-RECORD naming exact materials consulted, the structural provenance claim
   becomes independently auditable from output -- the same "here is what was read"
   property that C-18 provides for per-entry attestations.

**Three R9 axes:**

- **Axis A -- RESOLUTION PROTOCOL accountability:** Named VERIFIER ROLE per repair action
- **Axis B -- RULES-ANCHORED-COMPLETE evidentiary quotation:** Closure token quotes actual
  tier annotation text per rule
- **Axis C -- EF invocation trace record:** Step 0 produces visible EF-INVOCATION-RECORD
  naming pre-investigation materials consulted

**Variation plan:**

- V-01: Axis A only
- V-02: Axis B only
- V-03: Axis C only
- V-04: Axis A + Axis B
- V-05: Axis A + Axis B + Axis C (full integration)

All five carry C-01 through C-30. Predicted v9 score: 200/200 for all. The new axes
are v10 candidates -- they do not affect v9 scoring.

---

## V-01 -- RESOLUTION PROTOCOL Accountability Axis

**Variation axis:** Named verifier role per repair action in RESOLUTION PROTOCOL (Axis A only)

**Hypothesis:** C-25 names one repair action per CHAIN-FLAG type. C-29 makes the protocol
visually sovereign. Neither specifies who confirms the repair succeeded before the gate
clears. A VERIFIER ROLE named per flag type makes gate-clearing deterministic at the role
level: only the named role can certify resolution. This tests whether role accountability
in the repair protocol produces a structurally stronger repair guarantee than prescription
alone -- and whether this gap deserves its own criterion in v10. Discriminant between V-01
and R8 V-05: V-01 adds Verifier field to each RESOLUTION PROTOCOL entry; all other
structure is identical to R8 V-05.

**New structural element:** Each RESOLUTION PROTOCOL entry adds a `Verifier:` field
naming the role whose attestation is required to clear the flag.

**Expected v9 score:** 200/200 (all C-01 through C-30 pass; Axis A is v10-only)

---

Topic: {topic}

Synthesize what was unexpected. Three roles at three exclusive phase boundaries. Every
structural constraint is a named formal protocol. This is not a summary. This is not a
list of findings. This is the correction register: what the team believed, what the
signals proved wrong, and what the next team must inherit as tested knowledge.

---

### Roles

**Enforcement Framer (EF)** -- Step 0 exclusively.

```
ENFORCEMENT FRAMER -- FUNCTION DECLARATION
----------------------------------------------------------------------
Function:     Produce the ENFORCEMENT MECHANISM section at artifact
              head position. Derive NO-ECHO COST from pre-investigation
              materials only -- before any signal reading begins.
Input:        Design materials only. Signal artifacts out of scope.
Out-of-scope: PBI production. Entry authoring. Chain verification.
Phase scope:  Step 0 only. EF excluded from Steps 1-7.
Gate return:  ENFORCEMENT MECHANISM section complete with provenance
              tier, distinguishing property, reviewer implication, and
              NO-ECHO COST before proceeding to Step 1.
----------------------------------------------------------------------
```

**Belief Cartographer (BC)** -- Step 1 exclusively.

```
BELIEF CARTOGRAPHER -- FUNCTION DECLARATION
----------------------------------------------------------------------
Function:     Pre-investigation belief recovery. PBI production.
Input:        Design materials only. Same exclusion as EF.
Out-of-scope: Signal artifacts. Handle Ledger. Entry authoring.
Phase scope:  Step 1 only. PBI frozen at end of Step 1. BC excluded
              from Steps 2-7.
Gate return:  PBI complete with all PB-[NN] entries.
----------------------------------------------------------------------
```

**Institutional Archaeologist (IA)** -- Steps 2-7.

```
INSTITUTIONAL ARCHAEOLOGIST -- FUNCTION DECLARATION
----------------------------------------------------------------------
Function:     False-assumption recovery. Correction register only.
Input:        Signal artifacts + frozen PBI (read-only).
Out-of-scope: PBI authorship (frozen). Enforcement section (EF; immutable).
Orienting:    "What would the next team build wrong?"
Phase scope:  Steps 2-7 only.
----------------------------------------------------------------------
```

---

### Step 0 -- [EF] Enforcement Section

```
ENFORCEMENT MECHANISM DECLARATION
----------------------------------------------------------------------
Provenance tier: STRUCTURAL
Distinguishing property: Role-scope exclusion at three phase boundaries.
  EF writes the cost declaration before signals are read -- cost claim
  is prospective, not constructed from entry content. BC writes PBI
  before signals are read -- PBI entries cannot be contaminated by HL
  labels. IA writes corrections from signals and cannot alter the
  frozen PBI or enforcement section. No cross-phase reasoning is
  possible; role boundary is the enforcement mechanism.
Reviewer implication: Independence is enforced by role boundary. C-13
  content analysis is confirmatory rather than probative.
NO-ECHO COST: [EF derives from design materials -- name the specific
  failure class that propagates if this artifact is not produced.
  Which beliefs in today's materials would the next team inherit as
  validated design knowledge? What category of design error follows?
  Named failure class required. Generic statements fail.]
----------------------------------------------------------------------
```

---

### Step 1 -- [BC] PBI

```
PBI PRODUCTION PROTOCOL
----------------------------------------------------------------------
Input:    Design materials only. Signal artifacts excluded.
Format:   PB-[NN]: ["Today's materials imply that X." No signal knowledge.]
Freeze:   PBI frozen at end of Step 1. BC excluded from Steps 2-7.
          PBI entries must not use handle labels (unavailable at Step 1).
----------------------------------------------------------------------
```

---

### Step 2 -- [IA] Handle Ledger

```
HANDLE LEDGER PROTOCOL
----------------------------------------------------------------------
Timing:   After reading all signal artifacts. Before writing corrections.
Format:   HL-[NN]: [finding-specific label -- 2-5 words; finding language]
Test:     No PBI entry names its handle. No HL entry echoes a PBI entry
          verbatim. Either violation is a phase contract failure.
----------------------------------------------------------------------
```

---

### Step 3 -- [IA] Draft All Corrections

```
CORRECTION RECORD SCHEMA
----------------------------------------------------------------------
Fields (all required):
  Name:     HL-[NN] label.
  PBI-Ref:  PB-[NN].
  Source:   namespace:skill:artifact.
  Implies:  "Today's materials imply that..." Degree variants fail.
  Showed:   Direct claim. No hedges.
  Wrong:    Specific component/flow/decision. No softeners.
  Decide:   Specific blocking decision. No deferrals.
  Verified: Actual text of PB-[NN] AND key sentence from source.
            Identifiers alone fail.
  Severity: HIGH / MEDIUM / LOW.

STILL-LIVE FILTER: "Would a new team carry this as a false assumption?"
  YES -> draft. NO -> exclude; route to topic-story.

CORRECTION ENFORCEMENT:
  Rule 1: Correction register only. Discovery narration fails.
  Rule 2: Direct claims in every field. No hedges.
  Rule 3: Each entry self-contained.

Order: HIGH -> MEDIUM -> LOW.
----------------------------------------------------------------------
```

---

### Step 4 -- Register Audit

```
REGISTER AUDIT PROTOCOL
----------------------------------------------------------------------
Execute field by field before Step 5. Rewrite any field in discovery
register: Source (prose -> namespace:skill:artifact), Implies
(narration -> future-team framing), Wrong (softener -> specific
wrong component), Decide (deferral -> blocking decision), Verified
(identifiers -> quoted actual text of both).
----------------------------------------------------------------------
```

---

### Step 5 -- Entry Gate

```
ENTRY GATE DECLARATION
----------------------------------------------------------------------
Purpose:  Per-entry field validation. Format + framing only. Does
          not verify chain consistency (Step 6).
Fields:   PBI-Ref / Source / Implies / Showed / Wrong / Decide /
          Verified
Result:   PASS: {confirmed} / FAIL: {problem description}
Status:   STATUS: CLEARED / STATUS: NOT CLEARED
Gate:     NOT CLEARED halts progression. Rewrite FAIL fields; re-run.
----------------------------------------------------------------------
```

  GATE: [entry Name]
    PBI-Ref / Source / Implies / Showed / Wrong / Decide / Verified
    [PASS / FAIL for each]
  STATUS: CLEARED / NOT CLEARED

Do not proceed to Step 6 until every entry CLEARED.

---

### Step 6 -- Chain Integrity Audit

```
CHAIN INTEGRITY AUDIT DECLARATION
----------------------------------------------------------------------
Purpose:  Post-gate chain consistency verification. Distinct from
          ENTRY GATE (register) -- confirms four chain elements are
          internally consistent.
Elements: [1] PBI-Ref -> correct belief (quote PBI text)
          [2] Handle matches HL (quote HL title)
          [3] Source resolvable in this signal set
          [4] Verified quotation is actual text, not paraphrase
Token:    CHAIN-COMPLETE / CHAIN-FLAG per entry
Gate:     CHAIN-FLAG IS A HARD GATE. Any flag halts artifact
          completion until resolved via RESOLUTION PROTOCOL below.
----------------------------------------------------------------------
```

```
RESOLUTION PROTOCOL DECLARATION
----------------------------------------------------------------------
Exactly one named repair action per flag type. Each repair names the
VERIFIER ROLE whose attestation is required before the flag clears.
A flag is not cleared by completing the repair alone -- it is cleared
when the named VERIFIER ROLE confirms the repair outcome.

  PBI-Ref mismatch (element 1):
    Repair:   Replace PBI-Ref with identifier matching belief in
              "What today's materials imply". Belief statement is
              ground truth; do not alter it.
    Verifier: BELIEF CARTOGRAPHER (BC). BC confirms the corrected
              PBI-Ref maps to the stated belief at that identifier.
              IA may not self-certify PBI-Ref repairs.

  Handle mismatch (element 2):
    Repair:   Determine authoritative label (HL-[NN] or entry Name),
              then propagate from source to dependent. Do not update
              both independently.
    Verifier: INSTITUTIONAL ARCHAEOLOGIST (IA). IA confirms the
              propagated label is consistent across entry and HL.

  Source absent (element 3):
    Repair:   Replace with resolvable artifact, or demote to discard
              log with typed route reason.
    Verifier: INSTITUTIONAL ARCHAEOLOGIST (IA). IA confirms the
              replacement artifact is present in this signal set.

  Verified inaccurate (element 4):
    Repair:   Re-quote actual text from both PBI entry and source.
              If source unlocatable, apply element 3 protocol first.
    Verifier: INSTITUTIONAL ARCHAEOLOGIST (IA). IA confirms both
              quoted texts appear verbatim in their respective sources.
----------------------------------------------------------------------
```

Do not proceed to Step 7 until every entry CHAIN-COMPLETE.

---

### Step 7 -- [IA] Hierarchy, Distillation, and Forward Handover

**Surprise hierarchy:** Ranked by design impact. Argued rationale. Names decision at risk.

**Rules of Thumb:**

```
RULES OF THUMB DECLARATION
----------------------------------------------------------------------
Scope:  HIGH and MEDIUM entries only. LOW excluded.
Format: [TIER] {Rule -- <=20 words} (encodes: {SURPRISE NAME})
Check:  RULES-ANCHORED traceability -- each rule's tier annotation
        must match Severity of parent entry.
Gate:   RULES-ANCHORED BLOCKS on any MISALIGNED rule. Correct tier
        annotation before proceeding to Pattern of Inherited Errors.
Token:  After all rules ALIGNED:
          RULES-ANCHORED-COMPLETE -- distillation phase closed;
            tier alignment confirmed
          RULES-ANCHORED-FAIL: [rule] -- {mismatch description}
----------------------------------------------------------------------
```

| Tier     | Rule (<=20 words)  | Encodes         |
|----------|--------------------|-----------------|
| [HIGH]   | {rule statement}   | {SURPRISE NAME} |
| [MEDIUM] | {rule statement}   | {SURPRISE NAME} |

RULES-ANCHORED check: "[rule] -> ALIGNED / MISALIGNED" per rule.
Emit: RULES-ANCHORED-COMPLETE or RULES-ANCHORED-FAIL.

**Pattern of inherited errors:** 2-4 sentences. Named structural origin or stated absent.
Non-derivable from tallying individual corrections.

**Blind Spot Map:** Categories as types of wrong thinking specific to this artifact.
Assign each correction. Synthesis: non-derivable from individual corrections.

**Correction Forward Statement:**

1-3 sentences. Name the specific failure this artifact prevented. Identify the false
assumption the next team would have inherited and the investigation path it would have
misdirected. Confirm EF's NO-ECHO COST. Make the institutional purpose falsifiable.

PASS: "This echo prevented the next team from inheriting [specific assumption], which
would have directed [specific investigation] toward [Y]; signals showed [Z] instead."
FAIL: advisory framing; summary of findings; avoided-failure absent.

**What this correction record excludes:** At least two categories with counts.

---

== ARTIFACT STRUCTURE ============================================================

  1. ENFORCEMENT MECHANISM DECLARATION (EF; position 1; NO-ECHO COST)
  2. PBI PRODUCTION PROTOCOL output (BC)
  3. HANDLE LEDGER PROTOCOL output (IA)
  4. Corrections -- HIGH -> MEDIUM -> LOW (CORRECTION RECORD SCHEMA)
  5. Entry Gate blocks (ENTRY GATE DECLARATION; all STATUS: CLEARED)
  6. Chain Integrity Audit (CHAIN INTEGRITY AUDIT DECLARATION; all CHAIN-COMPLETE)
  7. Resolution Protocol trace (RESOLUTION PROTOCOL DECLARATION; verifier named per flag)
  8. Rules of Thumb (RULES OF THUMB DECLARATION; RULES-ANCHORED-COMPLETE token)
  9. Surprise hierarchy (ranked with rationale)
  10. Pattern of inherited errors
  11. Blind Spot Map
  12. Correction Forward Statement (confirms NO-ECHO COST; names specific avoided failure)
  13. What this correction record excludes

Write to: simulations/topic/echo/{topic}-echo-{YYYY-MM-DD}.md

---

## V-02 -- RULES-ANCHORED-COMPLETE Evidentiary Quotation Axis

**Variation axis:** Per-rule tier annotation quotation in RULES-ANCHORED-COMPLETE token
(Axis B only)

**Hypothesis:** C-28 requires a RULES-ANCHORED-COMPLETE token when all rules confirm
ALIGNED. The token's current form is declarative: it asserts alignment without quoting
what was aligned. C-18 established that attestations must quote actual text rather than
identifiers alone, because identifiers without quoted content require the reviewer to
navigate to the source to confirm the right content was checked. The same gap exists in
the closure token: it asserts alignment without showing the tier annotation string for
each rule. Adding per-rule tier quotation converts distillation-phase closure from
declarative to evidentiary: a reviewer can confirm the right tier annotation was checked
for each rule without re-running the RULES-ANCHORED check. This tests whether C-18's
evidentiary principle should extend to phase-close tokens, not just entry-level
attestations -- a parallel to how C-19 extended C-18's per-entry verification to the
chain audit layer.

**New structural element:** The RULES-ANCHORED-COMPLETE token quotes the actual tier
annotation string (`[HIGH]` or `[MEDIUM]`) for each rule by position, before asserting
alignment. Format: `RULES-ANCHORED-COMPLETE: R-01 "[HIGH]" ALIGNED, R-02 "[MEDIUM]"
ALIGNED, ... -- distillation phase closed; tier annotations confirmed evidentiary.`

**Expected v9 score:** 200/200 (all C-01 through C-30 pass; Axis B is v10-only)

---

Topic: {topic}

Synthesize what was unexpected. Three roles at three exclusive phase boundaries. Every
structural constraint is a named formal protocol. This is not a summary. This is not a
list of findings. This is the correction register: what the team believed, what the
signals proved wrong, and what the next team must inherit as tested knowledge.

---

### Roles

**Enforcement Framer (EF)** -- Step 0 exclusively.

```
ENFORCEMENT FRAMER -- FUNCTION DECLARATION
----------------------------------------------------------------------
Function:     Produce the ENFORCEMENT MECHANISM section at artifact
              head position. Derive NO-ECHO COST from pre-investigation
              materials only -- before any signal reading begins.
Input:        Design materials only. Signal artifacts out of scope.
Out-of-scope: PBI production. Entry authoring. Chain verification.
Phase scope:  Step 0 only. EF excluded from Steps 1-7.
Gate return:  ENFORCEMENT MECHANISM section complete with provenance
              tier, distinguishing property, reviewer implication, and
              NO-ECHO COST before proceeding to Step 1.
----------------------------------------------------------------------
```

**Belief Cartographer (BC)** -- Step 1 exclusively.

```
BELIEF CARTOGRAPHER -- FUNCTION DECLARATION
----------------------------------------------------------------------
Function:     Pre-investigation belief recovery. PBI production.
Input:        Design materials only. Same exclusion as EF.
Out-of-scope: Signal artifacts. Handle Ledger. Entry authoring.
Phase scope:  Step 1 only. PBI frozen at end of Step 1. BC excluded
              from Steps 2-7.
Gate return:  PBI complete with all PB-[NN] entries.
----------------------------------------------------------------------
```

**Institutional Archaeologist (IA)** -- Steps 2-7.

```
INSTITUTIONAL ARCHAEOLOGIST -- FUNCTION DECLARATION
----------------------------------------------------------------------
Function:     False-assumption recovery. Correction register only.
Input:        Signal artifacts + frozen PBI (read-only).
Out-of-scope: PBI authorship (frozen). Enforcement section (EF; immutable).
Orienting:    "What would the next team build wrong?"
Phase scope:  Steps 2-7 only.
----------------------------------------------------------------------
```

---

### Step 0 -- [EF] Enforcement Section

```
ENFORCEMENT MECHANISM DECLARATION
----------------------------------------------------------------------
Provenance tier: STRUCTURAL
Distinguishing property: Role-scope exclusion at three phase boundaries.
  EF writes the cost declaration before signals are read -- cost claim
  is prospective, not constructed from entry content. BC writes PBI
  before signals are read -- PBI entries cannot be contaminated by HL
  labels. IA writes corrections from signals and cannot alter the
  frozen PBI or enforcement section. No cross-phase reasoning is
  possible; role boundary is the enforcement mechanism.
Reviewer implication: Independence is enforced by role boundary. C-13
  content analysis is confirmatory rather than probative.
NO-ECHO COST: [EF derives from design materials -- name the specific
  failure class that propagates if this artifact is not produced.
  Named failure class required. Generic statements fail.]
----------------------------------------------------------------------
```

---

### Step 1 -- [BC] PBI

```
PBI PRODUCTION PROTOCOL
----------------------------------------------------------------------
Input:    Design materials only. Signal artifacts excluded.
Format:   PB-[NN]: ["Today's materials imply that X." No signal knowledge.]
Freeze:   PBI frozen at end of Step 1. BC excluded from Steps 2-7.
          PBI entries must not use handle labels (unavailable at Step 1).
----------------------------------------------------------------------
```

---

### Step 2 -- [IA] Handle Ledger

```
HANDLE LEDGER PROTOCOL
----------------------------------------------------------------------
Timing:   After reading all signal artifacts. Before writing corrections.
Format:   HL-[NN]: [finding-specific label -- 2-5 words; finding language]
Test:     No PBI entry names its handle. No HL entry echoes a PBI entry
          verbatim. Either violation is a phase contract failure.
----------------------------------------------------------------------
```

---

### Step 3 -- [IA] Draft All Corrections

```
CORRECTION RECORD SCHEMA
----------------------------------------------------------------------
Fields (all required):
  Name:     HL-[NN] label.
  PBI-Ref:  PB-[NN].
  Source:   namespace:skill:artifact.
  Implies:  "Today's materials imply that..." Degree variants fail.
  Showed:   Direct claim. No hedges.
  Wrong:    Specific component/flow/decision. No softeners.
  Decide:   Specific blocking decision. No deferrals.
  Verified: Actual text of PB-[NN] AND key sentence from source.
            Identifiers alone fail.
  Severity: HIGH / MEDIUM / LOW.

STILL-LIVE FILTER: "Would a new team carry this as a false assumption?"
  YES -> draft. NO -> exclude; route to topic-story.

CORRECTION ENFORCEMENT:
  Rule 1: Correction register only. Discovery narration fails.
  Rule 2: Direct claims in every field. No hedges.
  Rule 3: Each entry self-contained.

Order: HIGH -> MEDIUM -> LOW.
----------------------------------------------------------------------
```

---

### Step 4 -- Register Audit

```
REGISTER AUDIT PROTOCOL
----------------------------------------------------------------------
Execute field by field before Step 5. Rewrite any field in discovery
register: Source (prose -> namespace:skill:artifact), Implies
(narration -> future-team framing), Wrong (softener -> specific
wrong component), Decide (deferral -> blocking decision), Verified
(identifiers -> quoted actual text of both).
----------------------------------------------------------------------
```

---

### Step 5 -- Entry Gate

```
ENTRY GATE DECLARATION
----------------------------------------------------------------------
Purpose:  Per-entry field validation. Format + framing only. Does
          not verify chain consistency (Step 6).
Fields:   PBI-Ref / Source / Implies / Showed / Wrong / Decide /
          Verified
Result:   PASS: {confirmed} / FAIL: {problem description}
Status:   STATUS: CLEARED / STATUS: NOT CLEARED
Gate:     NOT CLEARED halts progression. Rewrite FAIL fields; re-run.
----------------------------------------------------------------------
```

  GATE: [entry Name]
    PBI-Ref / Source / Implies / Showed / Wrong / Decide / Verified
    [PASS / FAIL for each]
  STATUS: CLEARED / NOT CLEARED

Do not proceed to Step 6 until every entry CLEARED.

---

### Step 6 -- Chain Integrity Audit

```
CHAIN INTEGRITY AUDIT DECLARATION
----------------------------------------------------------------------
Purpose:  Post-gate chain consistency verification.
Elements: [1] PBI-Ref -> correct belief (quote PBI text)
          [2] Handle matches HL (quote HL title)
          [3] Source resolvable in this signal set
          [4] Verified quotation is actual text, not paraphrase
Token:    CHAIN-COMPLETE / CHAIN-FLAG per entry
Gate:     CHAIN-FLAG IS A HARD GATE. Any flag halts artifact
          completion until resolved via RESOLUTION PROTOCOL below.
----------------------------------------------------------------------
```

```
RESOLUTION PROTOCOL DECLARATION
----------------------------------------------------------------------
Exactly one named repair action per flag type:

  PBI-Ref mismatch (element 1): replace PBI-Ref with identifier
    matching belief in "What today's materials imply". Belief
    statement is ground truth; do not alter it.

  Handle mismatch (element 2): determine authoritative label
    (HL-[NN] or entry Name), then propagate from source to dependent.
    Do not update both independently.

  Source absent (element 3): replace with resolvable artifact, or
    demote to discard log with typed route reason.

  Verified inaccurate (element 4): re-quote actual text from both
    PBI entry and source. If source unlocatable, apply element 3
    protocol first.
----------------------------------------------------------------------
```

Do not proceed to Step 7 until every entry CHAIN-COMPLETE.

---

### Step 7 -- [IA] Hierarchy, Distillation, and Forward Handover

**Surprise hierarchy:** Ranked by design impact. Argued rationale. Names decision at risk.

**Rules of Thumb:**

```
RULES OF THUMB DECLARATION
----------------------------------------------------------------------
Scope:  HIGH and MEDIUM entries only. LOW excluded.
Format: [TIER] {Rule -- <=20 words} (encodes: {SURPRISE NAME})
Check:  RULES-ANCHORED traceability -- each rule's tier annotation
        must match Severity of parent entry.
Gate:   RULES-ANCHORED BLOCKS on any MISALIGNED rule. Correct tier
        annotation before proceeding to Pattern of Inherited Errors.
Closure: After all rules ALIGNED, emit RULES-ANCHORED-COMPLETE.
        The token MUST quote the actual tier annotation string for each
        rule by position before asserting alignment. A token that
        asserts "all rules aligned" without quoting the annotation text
        fails the evidentiary standard: the reviewer cannot confirm the
        right tier was checked without re-running the check.
Token format:
  RULES-ANCHORED-COMPLETE: R-01 "[TIER]" ALIGNED, R-02 "[TIER]"
    ALIGNED, ... -- distillation phase closed; tier annotations
    confirmed evidentiary.
Fail token:
  RULES-ANCHORED-FAIL: R-[NN] "[TIER]" MISALIGNED -- expected
    {parent Severity} vs found {annotation text}.
----------------------------------------------------------------------
```

| Tier     | Rule (<=20 words)  | Encodes         |
|----------|--------------------|-----------------|
| [HIGH]   | {rule statement}   | {SURPRISE NAME} |
| [MEDIUM] | {rule statement}   | {SURPRISE NAME} |

RULES-ANCHORED check: "R-[NN] [TIER] -> ALIGNED / MISALIGNED (parent Severity: [TIER])"
per rule. Emit: RULES-ANCHORED-COMPLETE with per-rule tier quotation, or RULES-ANCHORED-FAIL.

**Pattern of inherited errors:** 2-4 sentences. Named structural origin or stated absent.
Non-derivable from tallying individual corrections.

**Blind Spot Map:** Assign each correction to a category of wrong thinking.

**Correction Forward Statement:** Name the specific failure this artifact prevented.
Confirm EF's NO-ECHO COST. Make the institutional purpose falsifiable.

**What this correction record excludes:** At least two categories with counts.

---

== ARTIFACT STRUCTURE ============================================================

  1. ENFORCEMENT MECHANISM DECLARATION (EF; position 1; NO-ECHO COST)
  2. PBI PRODUCTION PROTOCOL output (BC)
  3. HANDLE LEDGER PROTOCOL output (IA)
  4. Corrections -- HIGH -> MEDIUM -> LOW (CORRECTION RECORD SCHEMA)
  5. Entry Gate blocks (all STATUS: CLEARED)
  6. Chain Integrity Audit (all CHAIN-COMPLETE)
  7. Resolution Protocol trace (flags resolved)
  8. Rules of Thumb (RULES-ANCHORED-COMPLETE with per-rule tier quotation)
  9. Surprise hierarchy (ranked with rationale)
  10. Pattern of inherited errors
  11. Blind Spot Map
  12. Correction Forward Statement (confirms NO-ECHO COST; names specific avoided failure)
  13. What this correction record excludes

Write to: simulations/topic/echo/{topic}-echo-{YYYY-MM-DD}.md

---

## V-03 -- EF Invocation Trace Record Axis

**Variation axis:** Visible EF-INVOCATION-RECORD naming pre-investigation materials
consulted at Step 0 (Axis C only)

**Hypothesis:** C-30 requires EF role-boundary protection: the NO-ECHO COST must be
derived by a role scoped to pre-investigation materials. The artifact shows EF ran --
the ENFORCEMENT MECHANISM section with NO-ECHO COST exists. But which materials EF
consulted is invisible from output. A reviewer auditing the structural provenance claim
must re-run Step 0 from scratch with only pre-investigation materials and compare.
If EF produces a visible EF-INVOCATION-RECORD naming the exact materials consulted,
the structural provenance claim becomes independently auditable: the reviewer reads the
record and knows what the role-boundary exclusion was enforcing against -- the same
"here is what was read" property that C-18 provides for per-entry attestations. This
tests whether the "here is what was checked" principle should extend to the enforcement
mechanism's own provenance claim, not just to entry-level attestations and distillation
phase tokens.

**New structural element:** Step 0 produces an EF-INVOCATION-RECORD block placed
immediately after the ENFORCEMENT MECHANISM DECLARATION. Lists exact pre-investigation
materials consulted. Explicitly excludes signal artifacts by name.

**Expected v9 score:** 200/200 (all C-01 through C-30 pass; Axis C is v10-only)

---

Topic: {topic}

Synthesize what was unexpected. Three roles at three exclusive phase boundaries. Every
structural constraint is a named formal protocol. This is not a summary. This is not a
list of findings. This is the correction register: what the team believed, what the
signals proved wrong, and what the next team must inherit as tested knowledge.

---

### Roles

**Enforcement Framer (EF)** -- Step 0 exclusively.

```
ENFORCEMENT FRAMER -- FUNCTION DECLARATION
----------------------------------------------------------------------
Function:     Produce the ENFORCEMENT MECHANISM section and the
              EF-INVOCATION-RECORD at artifact head position. Derive
              NO-ECHO COST from pre-investigation materials only --
              before any signal reading begins.
Input:        Design materials only. Signal artifacts out of scope.
              The EF-INVOCATION-RECORD must name every pre-investigation
              source consulted and explicitly exclude all signal artifacts.
Out-of-scope: PBI production. Entry authoring. Chain verification.
Phase scope:  Step 0 only. EF excluded from Steps 1-7.
Gate return:  ENFORCEMENT MECHANISM section + EF-INVOCATION-RECORD
              both complete before proceeding to Step 1.
----------------------------------------------------------------------
```

**Belief Cartographer (BC)** -- Step 1 exclusively.

```
BELIEF CARTOGRAPHER -- FUNCTION DECLARATION
----------------------------------------------------------------------
Function:     Pre-investigation belief recovery. PBI production.
Input:        Design materials only. Same exclusion as EF.
Out-of-scope: Signal artifacts. Handle Ledger. Entry authoring.
Phase scope:  Step 1 only. PBI frozen at end of Step 1. BC excluded
              from Steps 2-7.
Gate return:  PBI complete with all PB-[NN] entries.
----------------------------------------------------------------------
```

**Institutional Archaeologist (IA)** -- Steps 2-7.

```
INSTITUTIONAL ARCHAEOLOGIST -- FUNCTION DECLARATION
----------------------------------------------------------------------
Function:     False-assumption recovery. Correction register only.
Input:        Signal artifacts + frozen PBI (read-only).
Out-of-scope: PBI authorship (frozen). Enforcement section (EF; immutable).
Orienting:    "What would the next team build wrong?"
Phase scope:  Steps 2-7 only.
----------------------------------------------------------------------
```

---

### Step 0 -- [EF] Enforcement Section and Invocation Record

```
ENFORCEMENT MECHANISM DECLARATION
----------------------------------------------------------------------
Provenance tier: STRUCTURAL
Distinguishing property: Role-scope exclusion at three phase boundaries.
  EF writes the cost declaration before signals are read -- cost claim
  is prospective, not constructed from entry content. BC writes PBI
  before signals are read -- PBI entries cannot be contaminated by HL
  labels. IA writes corrections from signals and cannot alter the
  frozen PBI or enforcement section. No cross-phase reasoning is
  possible; role boundary is the enforcement mechanism.
Reviewer implication: Independence is enforced by role boundary. C-13
  content analysis is confirmatory rather than probative.
NO-ECHO COST: [EF derives from design materials -- name the specific
  failure class that propagates if this artifact is not produced.
  Named failure class required. Generic statements fail.]
----------------------------------------------------------------------
```

```
EF-INVOCATION-RECORD
----------------------------------------------------------------------
Step:       0 (EF phase; signal-reading phase not yet open)
Materials consulted (pre-investigation only):
  [List each design document, spec, proposal, or other pre-
   investigation source consulted to derive the NO-ECHO COST.
   File name or artifact identifier per entry. Minimum one entry.]
Signal artifacts excluded:
  [List each signal artifact by name and confirm it was not accessed
   during Step 0. If no signal artifacts exist yet: "No signal
   artifacts present at Step 0."]
Cost derivation basis:
  [One sentence: which material above grounded the NO-ECHO COST claim.
   A reviewer can re-derive the cost from this material alone to
   confirm the claim is prospective, not retrospective.]
----------------------------------------------------------------------
```

---

### Step 1 -- [BC] PBI

```
PBI PRODUCTION PROTOCOL
----------------------------------------------------------------------
Input:    Design materials only. Signal artifacts excluded.
Format:   PB-[NN]: ["Today's materials imply that X." No signal knowledge.]
Freeze:   PBI frozen at end of Step 1. BC excluded from Steps 2-7.
          PBI entries must not use handle labels (unavailable at Step 1).
----------------------------------------------------------------------
```

---

### Step 2 -- [IA] Handle Ledger

```
HANDLE LEDGER PROTOCOL
----------------------------------------------------------------------
Timing:   After reading all signal artifacts. Before writing corrections.
Format:   HL-[NN]: [finding-specific label -- 2-5 words; finding language]
Test:     No PBI entry names its handle. No HL entry echoes a PBI entry
          verbatim. Either violation is a phase contract failure.
----------------------------------------------------------------------
```

---

### Step 3 -- [IA] Draft All Corrections

```
CORRECTION RECORD SCHEMA
----------------------------------------------------------------------
Fields (all required):
  Name:     HL-[NN] label.
  PBI-Ref:  PB-[NN].
  Source:   namespace:skill:artifact.
  Implies:  "Today's materials imply that..." Degree variants fail.
  Showed:   Direct claim. No hedges.
  Wrong:    Specific component/flow/decision. No softeners.
  Decide:   Specific blocking decision. No deferrals.
  Verified: Actual text of PB-[NN] AND key sentence from source.
            Identifiers alone fail.
  Severity: HIGH / MEDIUM / LOW.

STILL-LIVE FILTER: "Would a new team carry this as a false assumption?"
  YES -> draft. NO -> exclude; route to topic-story.

CORRECTION ENFORCEMENT:
  Rule 1: Correction register only. Discovery narration fails.
  Rule 2: Direct claims in every field. No hedges.
  Rule 3: Each entry self-contained.

Order: HIGH -> MEDIUM -> LOW.
----------------------------------------------------------------------
```

---

### Step 4 -- Register Audit

```
REGISTER AUDIT PROTOCOL
----------------------------------------------------------------------
Execute field by field before Step 5. Rewrite any field in discovery
register: Source (prose -> namespace:skill:artifact), Implies
(narration -> future-team framing), Wrong (softener -> specific
wrong component), Decide (deferral -> blocking decision), Verified
(identifiers -> quoted actual text of both).
----------------------------------------------------------------------
```

---

### Step 5 -- Entry Gate

```
ENTRY GATE DECLARATION
----------------------------------------------------------------------
Purpose:  Per-entry field validation. Format + framing only.
Fields:   PBI-Ref / Source / Implies / Showed / Wrong / Decide /
          Verified
Status:   STATUS: CLEARED / STATUS: NOT CLEARED
Gate:     NOT CLEARED halts progression. Rewrite FAIL fields; re-run.
----------------------------------------------------------------------
```

Do not proceed to Step 6 until every entry CLEARED.

---

### Step 6 -- Chain Integrity Audit

```
CHAIN INTEGRITY AUDIT DECLARATION
----------------------------------------------------------------------
Elements: [1] PBI-Ref -> correct belief (quote PBI text)
          [2] Handle matches HL (quote HL title)
          [3] Source resolvable in this signal set
          [4] Verified quotation is actual text, not paraphrase
Token:    CHAIN-COMPLETE / CHAIN-FLAG per entry
Gate:     CHAIN-FLAG IS A HARD GATE. Any flag halts artifact
          completion until resolved via RESOLUTION PROTOCOL below.
----------------------------------------------------------------------
```

```
RESOLUTION PROTOCOL DECLARATION
----------------------------------------------------------------------
Exactly one named repair action per flag type:

  PBI-Ref mismatch (element 1): replace PBI-Ref with identifier
    matching belief in "What today's materials imply". Belief
    statement is ground truth; do not alter it.

  Handle mismatch (element 2): determine authoritative label
    (HL-[NN] or entry Name), then propagate from source to dependent.
    Do not update both independently.

  Source absent (element 3): replace with resolvable artifact, or
    demote to discard log with typed route reason.

  Verified inaccurate (element 4): re-quote actual text from both
    PBI entry and source. If source unlocatable, apply element 3
    protocol first.
----------------------------------------------------------------------
```

Do not proceed to Step 7 until every entry CHAIN-COMPLETE.

---

### Step 7 -- [IA] Hierarchy, Distillation, and Forward Handover

**Surprise hierarchy:** Ranked by design impact. Argued rationale. Names decision at risk.

**Rules of Thumb:**

```
RULES OF THUMB DECLARATION
----------------------------------------------------------------------
Scope:  HIGH and MEDIUM entries only. LOW excluded.
Format: [TIER] {Rule -- <=20 words} (encodes: {SURPRISE NAME})
Check:  RULES-ANCHORED traceability -- each rule's tier annotation
        must match Severity of parent entry.
Gate:   RULES-ANCHORED BLOCKS on any MISALIGNED rule. Correct before
        proceeding to Pattern of Inherited Errors.
Token:  After all rules ALIGNED:
          RULES-ANCHORED-COMPLETE -- distillation phase closed;
            tier alignment confirmed
          RULES-ANCHORED-FAIL: [rule] -- {mismatch description}
----------------------------------------------------------------------
```

| Tier     | Rule (<=20 words)  | Encodes         |
|----------|--------------------|-----------------|
| [HIGH]   | {rule statement}   | {SURPRISE NAME} |
| [MEDIUM] | {rule statement}   | {SURPRISE NAME} |

RULES-ANCHORED check: "[rule] -> ALIGNED / MISALIGNED" per rule.
Emit: RULES-ANCHORED-COMPLETE or RULES-ANCHORED-FAIL.

**Pattern of inherited errors:** 2-4 sentences. Named structural origin or stated absent.

**Blind Spot Map:** Assign each correction to a category of wrong thinking.

**Correction Forward Statement:** Name the specific failure this artifact prevented.
Confirm EF's NO-ECHO COST. Make the institutional purpose falsifiable.

**What this correction record excludes:** At least two categories with counts.

---

== ARTIFACT STRUCTURE ============================================================

  1. ENFORCEMENT MECHANISM DECLARATION (EF; position 1; NO-ECHO COST)
  2. EF-INVOCATION-RECORD (Step 0; pre-investigation materials listed; signals excluded)
  3. PBI PRODUCTION PROTOCOL output (BC)
  4. HANDLE LEDGER PROTOCOL output (IA)
  5. Corrections -- HIGH -> MEDIUM -> LOW (CORRECTION RECORD SCHEMA)
  6. Entry Gate blocks (all STATUS: CLEARED)
  7. Chain Integrity Audit (all CHAIN-COMPLETE)
  8. Resolution Protocol trace (flags resolved)
  9. Rules of Thumb (RULES-ANCHORED-COMPLETE token)
  10. Surprise hierarchy (ranked with rationale)
  11. Pattern of inherited errors
  12. Blind Spot Map
  13. Correction Forward Statement (confirms NO-ECHO COST; names specific avoided failure)
  14. What this correction record excludes

Write to: simulations/topic/echo/{topic}-echo-{YYYY-MM-DD}.md

---

## V-04 -- Axis A + Axis B: Accountable Repair and Evidentiary Distillation Closure

**Variation axis:** Combination -- RESOLUTION PROTOCOL accountability (V-01) +
RULES-ANCHORED-COMPLETE evidentiary quotation (V-02)

**Hypothesis:** V-01 makes repair routing accountable (who certifies the fix); V-02 makes
distillation closure evidentiary (what tier text was checked per rule). Each axis
independently converts a currently declarative commitment into one that is auditable from
output. V-04 tests whether the two axes are additive, neutral, or interfering when
combined. The combination targets the two audit phases symmetrically: chain audit repair
routing gets role accountability, distillation audit closure gets evidentiary quotation.
If both axes hold under composition without score loss, the v10 rubric gains C-31 and
C-32 as independent parallel criteria. If combination interferes, the score differential
between V-04 and V-01 or V-02 identifies the conflicting pair.

**New structural elements:**
1. RESOLUTION PROTOCOL entries each carry a `Verifier:` field (Axis A)
2. RULES-ANCHORED-COMPLETE token quotes per-rule tier annotation strings (Axis B)

**Expected v9 score:** 200/200

---

Topic: {topic}

Synthesize what was unexpected. Three roles at three exclusive phase boundaries. Every
structural constraint is a named formal protocol. This is not a summary. This is not a
list of findings. This is the correction register: what the team believed, what the
signals proved wrong, and what the next team must inherit as tested knowledge.

---

### Roles

**Enforcement Framer (EF)** -- Step 0 exclusively.

```
ENFORCEMENT FRAMER -- FUNCTION DECLARATION
----------------------------------------------------------------------
Function:     Produce the ENFORCEMENT MECHANISM section at artifact
              head position. Derive NO-ECHO COST from pre-investigation
              materials only -- before any signal reading begins.
Input:        Design materials only. Signal artifacts out of scope.
Out-of-scope: PBI production. Entry authoring. Chain verification.
Phase scope:  Step 0 only. EF excluded from Steps 1-7.
Gate return:  ENFORCEMENT MECHANISM section complete with provenance
              tier, distinguishing property, reviewer implication, and
              NO-ECHO COST before proceeding to Step 1.
----------------------------------------------------------------------
```

**Belief Cartographer (BC)** -- Step 1 exclusively.

```
BELIEF CARTOGRAPHER -- FUNCTION DECLARATION
----------------------------------------------------------------------
Function:     Pre-investigation belief recovery. PBI production.
Input:        Design materials only. Same exclusion as EF.
Out-of-scope: Signal artifacts. Handle Ledger. Entry authoring.
Phase scope:  Step 1 only. PBI frozen at end of Step 1. BC excluded
              from Steps 2-7.
Gate return:  PBI complete with all PB-[NN] entries.
----------------------------------------------------------------------
```

**Institutional Archaeologist (IA)** -- Steps 2-7.

```
INSTITUTIONAL ARCHAEOLOGIST -- FUNCTION DECLARATION
----------------------------------------------------------------------
Function:     False-assumption recovery. Correction register only.
Input:        Signal artifacts + frozen PBI (read-only).
Out-of-scope: PBI authorship (frozen). Enforcement section (EF; immutable).
Orienting:    "What would the next team build wrong?"
Phase scope:  Steps 2-7 only.
----------------------------------------------------------------------
```

---

### Step 0 -- [EF] Enforcement Section

```
ENFORCEMENT MECHANISM DECLARATION
----------------------------------------------------------------------
Provenance tier: STRUCTURAL
Distinguishing property: Role-scope exclusion at three phase boundaries.
  EF writes the cost declaration before signals are read -- cost claim
  is prospective, not constructed from entry content. BC writes PBI
  before signals are read -- PBI entries cannot be contaminated by HL
  labels. IA writes corrections from signals and cannot alter the
  frozen PBI or enforcement section. No cross-phase reasoning is
  possible; role boundary is the enforcement mechanism.
Reviewer implication: Independence is enforced by role boundary. C-13
  content analysis is confirmatory rather than probative.
NO-ECHO COST: [EF derives from design materials -- name the specific
  failure class that propagates if this artifact is not produced.
  Named failure class required. Generic statements fail.]
----------------------------------------------------------------------
```

---

### Step 1 -- [BC] PBI

```
PBI PRODUCTION PROTOCOL
----------------------------------------------------------------------
Input:    Design materials only. Signal artifacts excluded.
Format:   PB-[NN]: ["Today's materials imply that X." No signal knowledge.]
Freeze:   PBI frozen at end of Step 1. BC excluded from Steps 2-7.
          PBI entries must not use handle labels (unavailable at Step 1).
----------------------------------------------------------------------
```

---

### Step 2 -- [IA] Handle Ledger

```
HANDLE LEDGER PROTOCOL
----------------------------------------------------------------------
Timing:   After reading all signal artifacts. Before writing corrections.
Format:   HL-[NN]: [finding-specific label -- 2-5 words; finding language]
Test:     No PBI entry names its handle. No HL entry echoes a PBI entry
          verbatim. Either violation is a phase contract failure.
----------------------------------------------------------------------
```

---

### Step 3 -- [IA] Draft All Corrections

```
CORRECTION RECORD SCHEMA
----------------------------------------------------------------------
Fields (all required):
  Name:     HL-[NN] label.
  PBI-Ref:  PB-[NN].
  Source:   namespace:skill:artifact.
  Implies:  "Today's materials imply that..." Degree variants fail.
  Showed:   Direct claim. No hedges.
  Wrong:    Specific component/flow/decision. No softeners.
  Decide:   Specific blocking decision. No deferrals.
  Verified: Actual text of PB-[NN] AND key sentence from source.
            Identifiers alone fail.
  Severity: HIGH / MEDIUM / LOW.

STILL-LIVE FILTER: "Would a new team carry this as a false assumption?"
  YES -> draft. NO -> exclude; route to topic-story.

CORRECTION ENFORCEMENT:
  Rule 1: Correction register only. Discovery narration fails.
  Rule 2: Direct claims in every field. No hedges.
  Rule 3: Each entry self-contained.

Order: HIGH -> MEDIUM -> LOW.
----------------------------------------------------------------------
```

---

### Step 4 -- Register Audit

```
REGISTER AUDIT PROTOCOL
----------------------------------------------------------------------
Execute field by field before Step 5. Rewrite any field in discovery
register.
----------------------------------------------------------------------
```

---

### Step 5 -- Entry Gate

```
ENTRY GATE DECLARATION
----------------------------------------------------------------------
Fields:   PBI-Ref / Source / Implies / Showed / Wrong / Decide /
          Verified
Status:   STATUS: CLEARED / STATUS: NOT CLEARED
Gate:     NOT CLEARED halts progression.
----------------------------------------------------------------------
```

Do not proceed to Step 6 until every entry CLEARED.

---

### Step 6 -- Chain Integrity Audit

```
CHAIN INTEGRITY AUDIT DECLARATION
----------------------------------------------------------------------
Elements: [1] PBI-Ref -> correct belief (quote PBI text)
          [2] Handle matches HL (quote HL title)
          [3] Source resolvable in this signal set
          [4] Verified quotation is actual text, not paraphrase
Token:    CHAIN-COMPLETE / CHAIN-FLAG per entry
Gate:     CHAIN-FLAG IS A HARD GATE. Any flag halts artifact
          completion until resolved via RESOLUTION PROTOCOL below.
----------------------------------------------------------------------
```

```
RESOLUTION PROTOCOL DECLARATION
----------------------------------------------------------------------
Exactly one named repair action per flag type. Each repair names the
VERIFIER ROLE whose attestation is required before the flag clears.
A flag is not cleared by the repair alone -- it clears when the named
VERIFIER ROLE confirms the repair outcome.

  PBI-Ref mismatch (element 1):
    Repair:   Replace PBI-Ref with identifier matching belief in
              "What today's materials imply". Belief statement is
              ground truth; do not alter it.
    Verifier: BELIEF CARTOGRAPHER (BC). BC confirms the corrected
              PBI-Ref maps to the stated belief at that identifier.

  Handle mismatch (element 2):
    Repair:   Determine authoritative label (HL-[NN] or entry Name),
              then propagate from source to dependent.
    Verifier: INSTITUTIONAL ARCHAEOLOGIST (IA). IA confirms label
              is consistent across entry and HL.

  Source absent (element 3):
    Repair:   Replace with resolvable artifact, or demote to discard
              log with typed route reason.
    Verifier: INSTITUTIONAL ARCHAEOLOGIST (IA). IA confirms
              replacement is present in this signal set.

  Verified inaccurate (element 4):
    Repair:   Re-quote actual text from both PBI entry and source.
              If source unlocatable, apply element 3 protocol first.
    Verifier: INSTITUTIONAL ARCHAEOLOGIST (IA). IA confirms both
              quoted texts appear verbatim in their sources.
----------------------------------------------------------------------
```

Do not proceed to Step 7 until every entry CHAIN-COMPLETE.

---

### Step 7 -- [IA] Hierarchy, Distillation, and Forward Handover

**Surprise hierarchy:** Ranked by design impact. Argued rationale. Names decision at risk.

**Rules of Thumb:**

```
RULES OF THUMB DECLARATION
----------------------------------------------------------------------
Scope:  HIGH and MEDIUM entries only. LOW excluded.
Format: [TIER] {Rule -- <=20 words} (encodes: {SURPRISE NAME})
Check:  RULES-ANCHORED traceability -- each rule's tier annotation
        must match Severity of parent entry.
Gate:   RULES-ANCHORED BLOCKS on any MISALIGNED rule. Correct before
        proceeding to Pattern of Inherited Errors.
Closure: After all rules ALIGNED, emit RULES-ANCHORED-COMPLETE.
        The token MUST quote the actual tier annotation string for each
        rule by position before asserting alignment. A declarative
        "all rules aligned" without quoted tier text fails.
Token format:
  RULES-ANCHORED-COMPLETE: R-01 "[TIER]" ALIGNED, R-02 "[TIER]"
    ALIGNED, ... -- distillation phase closed; tier annotations
    confirmed evidentiary.
Fail token: RULES-ANCHORED-FAIL: R-[NN] "[TIER]" MISALIGNED --
    expected {parent Severity} vs found {annotation text}.
----------------------------------------------------------------------
```

| Tier     | Rule (<=20 words)  | Encodes         |
|----------|--------------------|-----------------|
| [HIGH]   | {rule statement}   | {SURPRISE NAME} |
| [MEDIUM] | {rule statement}   | {SURPRISE NAME} |

RULES-ANCHORED check: "R-[NN] [TIER] -> ALIGNED / MISALIGNED (parent Severity: [TIER])"
per rule. Emit: RULES-ANCHORED-COMPLETE with per-rule tier quotation, or RULES-ANCHORED-FAIL.

**Pattern of inherited errors:** 2-4 sentences. Named structural origin or stated absent.

**Blind Spot Map:** Assign each correction to a category of wrong thinking.

**Correction Forward Statement:** Name the specific failure this artifact prevented.
Confirm EF's NO-ECHO COST. Make the institutional purpose falsifiable.

**What this correction record excludes:** At least two categories with counts.

---

== ARTIFACT STRUCTURE ============================================================

  1. ENFORCEMENT MECHANISM DECLARATION (EF; position 1; NO-ECHO COST)
  2. PBI PRODUCTION PROTOCOL output (BC)
  3. HANDLE LEDGER PROTOCOL output (IA)
  4. Corrections -- HIGH -> MEDIUM -> LOW (CORRECTION RECORD SCHEMA)
  5. Entry Gate blocks (all STATUS: CLEARED)
  6. Chain Integrity Audit (all CHAIN-COMPLETE)
  7. Resolution Protocol trace (RESOLUTION PROTOCOL; verifier named per flag type)
  8. Rules of Thumb (RULES-ANCHORED-COMPLETE with per-rule tier quotation)
  9. Surprise hierarchy (ranked with rationale)
  10. Pattern of inherited errors
  11. Blind Spot Map
  12. Correction Forward Statement (confirms NO-ECHO COST; names specific avoided failure)
  13. What this correction record excludes

Write to: simulations/topic/echo/{topic}-echo-{YYYY-MM-DD}.md

---

## V-05 -- Full R9 Integration: Axis A + Axis B + Axis C

**Variation axis:** All three R9 axes -- RESOLUTION PROTOCOL accountability (V-01) +
RULES-ANCHORED-COMPLETE evidentiary quotation (V-02) + EF invocation trace record (V-03)

**Hypothesis:** Each R9 axis makes a structural commitment auditable from output alone:
V-03 makes the EF role-boundary claim traceable (which materials were consulted); V-02
makes distillation-phase closure evidentiary (what tier text was aligned per rule); V-01
makes repair routing accountable (who certifies the fix per flag type). Combined, V-05
tests whether a consistent meta-principle governs all three -- every structural commitment
this artifact makes should be independently auditable from its output, not just
structurally enforced. If V-05 achieves 200/200 without axis interactions degrading
individual criteria, all three axes are independent and the v10 rubric gains three new
parallel criteria (C-31, C-32, C-33). The score differential between V-05 and V-04
(which excludes Axis C) isolates whether the EF-INVOCATION-RECORD is compositionally
stable with the other two axes.

**New structural elements (V-05 = V-01 + V-02 + V-03):**
1. RESOLUTION PROTOCOL entries each carry a `Verifier:` field (Axis A)
2. RULES-ANCHORED-COMPLETE token quotes per-rule tier annotation strings (Axis B)
3. Step 0 produces EF-INVOCATION-RECORD listing pre-investigation materials consulted (Axis C)

**Expected v9 score:** 200/200

---

Topic: {topic}

Synthesize what was unexpected. Three roles at three exclusive phase boundaries. Every
structural commitment is named, formal, and auditable from output. This is not a summary.
This is not a list of findings. This is the correction register: what the team believed,
what the signals proved wrong, and what the next team must inherit as tested knowledge --
with every provenance claim traceable to the artifact that generated it.

---

### Roles

**Enforcement Framer (EF)** -- Step 0 exclusively.

```
ENFORCEMENT FRAMER -- FUNCTION DECLARATION
----------------------------------------------------------------------
Function:     Produce the ENFORCEMENT MECHANISM section and the
              EF-INVOCATION-RECORD at artifact head position. Derive
              NO-ECHO COST from pre-investigation materials only --
              before any signal reading begins.
Input:        Design materials only. Signal artifacts out of scope.
              The EF-INVOCATION-RECORD must name every pre-investigation
              source consulted and explicitly list all signal artifacts
              as excluded.
Out-of-scope: PBI production. Entry authoring. Chain verification.
Phase scope:  Step 0 only. EF excluded from Steps 1-7.
Gate return:  ENFORCEMENT MECHANISM section + EF-INVOCATION-RECORD
              both complete before proceeding to Step 1.
----------------------------------------------------------------------
```

**Belief Cartographer (BC)** -- Step 1 exclusively.

```
BELIEF CARTOGRAPHER -- FUNCTION DECLARATION
----------------------------------------------------------------------
Function:     Pre-investigation belief recovery. PBI production.
Input:        Design materials only. Same exclusion as EF.
Out-of-scope: Signal artifacts. Handle Ledger. Entry authoring.
Phase scope:  Step 1 only. PBI frozen at end of Step 1. BC excluded
              from Steps 2-7.
Gate return:  PBI complete with all PB-[NN] entries.
----------------------------------------------------------------------
```

**Institutional Archaeologist (IA)** -- Steps 2-7.

```
INSTITUTIONAL ARCHAEOLOGIST -- FUNCTION DECLARATION
----------------------------------------------------------------------
Function:     False-assumption recovery. Correction register only.
Input:        Signal artifacts + frozen PBI (read-only).
Out-of-scope: PBI authorship (frozen). Enforcement section (EF; immutable).
Orienting:    "What would the next team build wrong?"
Phase scope:  Steps 2-7 only.
----------------------------------------------------------------------
```

---

### Step 0 -- [EF] Enforcement Section and Invocation Record

```
ENFORCEMENT MECHANISM DECLARATION
----------------------------------------------------------------------
Provenance tier: STRUCTURAL
Distinguishing property: Role-scope exclusion at three phase boundaries.
  EF writes the cost declaration before signals are read -- cost claim
  is prospective, not constructed from entry content. BC writes PBI
  before signals are read -- PBI entries cannot be contaminated by HL
  labels. IA writes corrections from signals and cannot alter the
  frozen PBI or enforcement section. No cross-phase reasoning is
  possible; role boundary is the enforcement mechanism.
Reviewer implication: Independence is enforced by role boundary. C-13
  content analysis is confirmatory rather than probative.
NO-ECHO COST: [EF derives from design materials -- name the specific
  failure class that propagates if this artifact is not produced.
  Which beliefs in today's materials would the next team inherit as
  validated design knowledge? What category of design error follows?
  Named failure class required. Generic statements fail.]
----------------------------------------------------------------------
```

```
EF-INVOCATION-RECORD
----------------------------------------------------------------------
Step:       0 (EF phase; signal-reading phase not yet open)
Materials consulted (pre-investigation only):
  [List each design document, spec, proposal, or other pre-
   investigation source consulted to derive the NO-ECHO COST.
   File name or artifact identifier per entry. Minimum one entry.]
Signal artifacts excluded:
  [List each signal artifact by name and confirm it was not accessed
   during Step 0. If no signal artifacts exist yet: "No signal
   artifacts present at Step 0."]
Cost derivation basis:
  [One sentence: which material above grounded the NO-ECHO COST claim.
   A reviewer can re-derive the cost from this material alone to
   confirm the claim is prospective, not retrospective.]
----------------------------------------------------------------------
```

---

### Step 1 -- [BC] PBI

```
PBI PRODUCTION PROTOCOL
----------------------------------------------------------------------
Input:    Design materials only. Signal artifacts excluded.
Format:   PB-[NN]: ["Today's materials imply that X." No signal knowledge.]
Freeze:   PBI frozen at end of Step 1. BC excluded from Steps 2-7.
          PBI entries must not use handle labels (unavailable at Step 1).
----------------------------------------------------------------------
```

---

### Step 2 -- [IA] Handle Ledger

```
HANDLE LEDGER PROTOCOL
----------------------------------------------------------------------
Timing:   After reading all signal artifacts. Before writing corrections.
Format:   HL-[NN]: [finding-specific label -- 2-5 words; finding language]
Test:     No PBI entry names its handle. No HL entry echoes a PBI entry
          verbatim. Either violation is a phase contract failure.
----------------------------------------------------------------------
```

---

### Step 3 -- [IA] Draft All Corrections

```
CORRECTION RECORD SCHEMA
----------------------------------------------------------------------
Fields (all required):
  Name:     HL-[NN] label.
  PBI-Ref:  PB-[NN].
  Source:   namespace:skill:artifact.
  Implies:  "Today's materials imply that..." Degree variants fail.
  Showed:   Direct claim. No hedges.
  Wrong:    Specific component/flow/decision. No softeners.
  Decide:   Specific blocking decision. No deferrals.
  Verified: Actual text of PB-[NN] AND key sentence from source.
            Identifiers alone fail.
  Severity: HIGH / MEDIUM / LOW.

STILL-LIVE FILTER: "Would a new team carry this as a false assumption?"
  YES -> draft. NO -> exclude; route to topic-story.

CORRECTION ENFORCEMENT:
  Rule 1: Correction register only. Discovery narration fails.
  Rule 2: Direct claims in every field. No hedges.
  Rule 3: Each entry self-contained.

Order: HIGH -> MEDIUM -> LOW.
----------------------------------------------------------------------
```

---

### Step 4 -- Register Audit

```
REGISTER AUDIT PROTOCOL
----------------------------------------------------------------------
Execute field by field before Step 5. Rewrite any field in discovery
register: Source (prose -> namespace:skill:artifact), Implies
(narration -> future-team framing), Wrong (softener -> specific
wrong component), Decide (deferral -> blocking decision), Verified
(identifiers -> quoted actual text of both).
----------------------------------------------------------------------
```

---

### Step 5 -- Entry Gate

```
ENTRY GATE DECLARATION
----------------------------------------------------------------------
Purpose:  Per-entry field validation. Format + framing only. Does
          not verify chain consistency (Step 6).
Fields:   PBI-Ref / Source / Implies / Showed / Wrong / Decide /
          Verified
Result:   PASS: {confirmed} / FAIL: {problem description}
Status:   STATUS: CLEARED / STATUS: NOT CLEARED
Gate:     NOT CLEARED halts progression. Rewrite FAIL fields; re-run.
----------------------------------------------------------------------
```

  GATE: [entry Name]
    PBI-Ref / Source / Implies / Showed / Wrong / Decide / Verified
    [PASS / FAIL for each]
  STATUS: CLEARED / NOT CLEARED

Do not proceed to Step 6 until every entry CLEARED.

---

### Step 6 -- Chain Integrity Audit

```
CHAIN INTEGRITY AUDIT DECLARATION
----------------------------------------------------------------------
Purpose:  Post-gate chain consistency verification. Confirms four
          chain elements are internally consistent.
Elements: [1] PBI-Ref -> correct belief (quote PBI text)
          [2] Handle matches HL (quote HL title)
          [3] Source resolvable in this signal set
          [4] Verified quotation is actual text, not paraphrase
Token:    CHAIN-COMPLETE / CHAIN-FLAG per entry
Gate:     CHAIN-FLAG IS A HARD GATE. Any flag halts artifact
          completion until resolved via RESOLUTION PROTOCOL below.
----------------------------------------------------------------------
```

```
RESOLUTION PROTOCOL DECLARATION
----------------------------------------------------------------------
Exactly one named repair action per flag type. Each repair names the
VERIFIER ROLE whose attestation is required before the flag clears.
A flag is not cleared by completing the repair alone -- it clears when
the named VERIFIER ROLE confirms the repair outcome.

  PBI-Ref mismatch (element 1):
    Repair:   Replace PBI-Ref with identifier matching belief in
              "What today's materials imply". Belief statement is
              ground truth; do not alter it.
    Verifier: BELIEF CARTOGRAPHER (BC). BC confirms the corrected
              PBI-Ref maps to the stated belief at that identifier.
              IA may not self-certify PBI-Ref repairs.

  Handle mismatch (element 2):
    Repair:   Determine authoritative label (HL-[NN] or entry Name),
              then propagate from source to dependent. Do not update
              both independently.
    Verifier: INSTITUTIONAL ARCHAEOLOGIST (IA). IA confirms the
              propagated label is consistent across entry and HL.

  Source absent (element 3):
    Repair:   Replace with resolvable artifact, or demote to discard
              log with typed route reason.
    Verifier: INSTITUTIONAL ARCHAEOLOGIST (IA). IA confirms the
              replacement artifact is present in this signal set.

  Verified inaccurate (element 4):
    Repair:   Re-quote actual text from both PBI entry and source.
              If source unlocatable, apply element 3 protocol first.
    Verifier: INSTITUTIONAL ARCHAEOLOGIST (IA). IA confirms both
              quoted texts appear verbatim in their respective sources.
----------------------------------------------------------------------
```

Do not proceed to Step 7 until every entry CHAIN-COMPLETE.

---

### Step 7 -- [IA] Hierarchy, Distillation, and Forward Handover

**Surprise hierarchy:** Ranked by design impact. Argued rationale. Names decision at risk.

**Rules of Thumb:**

```
RULES OF THUMB DECLARATION
----------------------------------------------------------------------
Scope:  HIGH and MEDIUM entries only. LOW excluded.
Format: [TIER] {Rule -- <=20 words} (encodes: {SURPRISE NAME})
Check:  RULES-ANCHORED traceability -- each rule's tier annotation
        must match Severity of parent entry.
Gate:   RULES-ANCHORED BLOCKS on any MISALIGNED rule. Correct tier
        annotation before proceeding to Pattern of Inherited Errors.
Closure: After all rules ALIGNED, emit RULES-ANCHORED-COMPLETE.
        The token MUST quote the actual tier annotation string for each
        rule by position before asserting alignment. A bare
        RULES-ANCHORED-COMPLETE without per-rule tier quotations fails:
        the reviewer cannot confirm the right annotation was checked
        without re-running the RULES-ANCHORED check.
Token format:
  RULES-ANCHORED-COMPLETE: R-01 "[TIER]" ALIGNED, R-02 "[TIER]"
    ALIGNED, ... -- distillation phase closed; tier annotations
    confirmed evidentiary.
Fail token:
  RULES-ANCHORED-FAIL: R-[NN] "[TIER]" MISALIGNED -- expected
    {parent Severity} vs found {annotation text}.
----------------------------------------------------------------------
```

| Tier     | Rule (<=20 words)  | Encodes         |
|----------|--------------------|-----------------|
| [HIGH]   | {rule statement}   | {SURPRISE NAME} |
| [MEDIUM] | {rule statement}   | {SURPRISE NAME} |

RULES-ANCHORED check: "R-[NN] [TIER] -> ALIGNED / MISALIGNED (parent Severity: [TIER])"
per rule. Emit: RULES-ANCHORED-COMPLETE with per-rule tier quotation, or RULES-ANCHORED-FAIL.

**Pattern of inherited errors:** 2-4 sentences. Named structural origin or stated absent.
Non-derivable from tallying individual corrections.

**Blind Spot Map:** Categories as types of wrong thinking specific to this artifact.
Assign each correction. Synthesis: non-derivable from individual corrections.

**Correction Forward Statement:**

1-3 sentences: "Before you build {topic}, the correction record requires you to know that..."

Name the specific failure this artifact prevented. Identify the false assumption the next
team would have inherited and the investigation path it would have misdirected.

Closes two loops:
  1. Confirms EF's NO-ECHO COST (prospective cost claim -> verified outcome at completion).
  2. Makes the artifact's institutional purpose falsifiable (commitment honored or denied).

PASS: "This echo prevented the next team from inheriting [specific assumption], which
would have directed [specific investigation] toward [Y]; signals showed [Z] instead,
and the [specific wrong design] was thereby avoided."
FAIL: advisory framing; summary of findings; avoided-failure absent.

**What this correction record excludes:** At least two categories with counts.

---

== ARTIFACT STRUCTURE ============================================================

  1. ENFORCEMENT MECHANISM DECLARATION (EF; position 1; NO-ECHO COST)
  2. EF-INVOCATION-RECORD (Step 0; pre-investigation materials listed; signals excluded)
  3. PBI PRODUCTION PROTOCOL output (BC)
  4. HANDLE LEDGER PROTOCOL output (IA)
  5. Corrections -- HIGH -> MEDIUM -> LOW (CORRECTION RECORD SCHEMA)
  6. Entry Gate blocks (ENTRY GATE DECLARATION; all STATUS: CLEARED)
  7. Chain Integrity Audit (CHAIN INTEGRITY AUDIT DECLARATION; all CHAIN-COMPLETE)
  8. Resolution Protocol trace (RESOLUTION PROTOCOL; verifier named per flag type)
  9. Rules of Thumb (RULES OF THUMB DECLARATION; RULES-ANCHORED-COMPLETE with tier quotations)
  10. Surprise hierarchy (ranked with rationale)
  11. Pattern of inherited errors
  12. Blind Spot Map
  13. Correction Forward Statement (confirms NO-ECHO COST; names specific avoided failure)
  14. What this correction record excludes

Write to: simulations/topic/echo/{topic}-echo-{YYYY-MM-DD}.md

---

## Predicted v9 Scores

| Variation | Axis   | New element                                   | v9 composite | C-28 | C-29 | C-30 |
|-----------|--------|-----------------------------------------------|:------------:|:----:|:----:|:----:|
| V-01      | A only | Verifier role per repair action               | 200          | PASS | PASS | PASS |
| V-02      | B only | Tier quotation in RULES-ANCHORED-COMPLETE     | 200          | PASS | PASS | PASS |
| V-03      | C only | EF-INVOCATION-RECORD at Step 0                | 200          | PASS | PASS | PASS |
| V-04      | A + B  | Verifier + tier quotation                     | 200          | PASS | PASS | PASS |
| V-05      | A+B+C  | Verifier + tier quotation + EF record         | 200          | PASS | PASS | PASS |

All five variations carry C-01 through C-30 intact from R8 V-05.
The three new axes are v10 candidates only -- they do not affect v9 scoring.

---

## R9 Isolated Pattern: Structural Traceability

Each R9 axis applies the same meta-principle: every structural commitment this artifact
makes should be independently auditable from output -- not just structurally enforced,
but structurally traceable.

| Existing criterion | What it enforces | R9 axis | What it makes auditable |
|--------------------|------------------|---------|------------------------|
| C-30: EF role-boundary | NO-ECHO COST is prospective (role-scope exclusion) | Axis C (V-03) | WHICH materials EF consulted at Step 0 |
| C-28: RULES-ANCHORED-COMPLETE | Distillation phase closed successfully | Axis B (V-02) | WHAT tier annotation text was checked per rule |
| C-25 + C-29: RESOLUTION PROTOCOL | Repair exists, is visible and peer-level | Axis A (V-01) | WHO certifies the repair before gate clears |

The v9 rubric progression concluded at: **auditable closure / visual sovereignty /
structural provenance**. R9 candidate layer: **structural traceability** -- making
every enforced commitment verifiable from the artifact's own output, not only from
the mechanism that generated it.

Each new layer converts a structural guarantee from:
  "the mechanism exists and its exit state is visible"
to:
  "the mechanism's execution is independently verifiable from the artifact's own output"

**V-01, V-02, V-03** are independent single-axis tests. If all three score identically
to each other and to R8 V-05 on v9, they are ready for v10 rubric integration as three
independent new criteria.

**V-04** tests whether Axis A and Axis B are compositionally stable. Score differential
from V-01 or V-02 identifies any interaction.

**V-05** tests whether all three axes together are compositionally stable -- the question
that V-01 through V-04 together cannot answer without the full combination.
