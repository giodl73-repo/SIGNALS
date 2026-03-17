---
skill: quest-variate
skill_target: topic-echo
date: 2026-03-16
round: 10
rubric: v10
rubric_file: simulations/quest/rubrics/topic-echo-rubric-v10-2026-03-16.md
rubric_max: 215
---

# Variations: `topic:echo` -- Round 10 (2026-03-16)

**Rubric:** v10 (2026-03-16) | **Criteria count:** 33 (5 essential / 3 recommended / 25 aspirational)

---

## Design Context

R9 V-05 achieves 215/215 under v10 -- the rubric ceiling. Round 10 begins at full
convergence on all 33 criteria. The purpose of R10 variations is not to maximize v10
score (the base already does) but to identify structural patterns the v10 rubric does
not yet capture.

The v10 rubric's meta-pattern: each round takes a structural commitment enforced by
specification and converts it into something observable from output alone. The R9 layer
produced: C-31 (visible repair routing -> role-accountable clearing), C-32 (closure
token asserts alignment -> token quotes what was aligned), C-33 (EF role boundary ->
EF names materials consulted). Three such conversions remain visible when R9 V-05 is
examined against "which commitments does this prompt enforce but not make auditable?"

**Gap identification:**

1. **BC Coverage Record gap.** C-33 gave EF an EF-INVOCATION-RECORD: EF names which
   pre-investigation materials were consulted and which signals were excluded, making
   the EF role-boundary claim independently auditable. BC operates under the identical
   exclusion contract (design materials only; signal artifacts out of scope) and its
   PBI output is equally weight-bearing -- every correction entry references a PBI
   identifier. But BC produces no parallel record. A reviewer auditing PBI completeness
   cannot verify whether BC scanned all relevant design materials without re-running
   Step 1 from scratch. A BC-COVERAGE-RECORD (parallel to EF-INVOCATION-RECORD) naming
   exact materials consulted, signals excluded, and PBI completeness basis makes BC's
   provenance claim independently auditable. C-33's principle generalizes: any role
   that makes a material-scope exclusion claim should produce a visible invocation record.

2. **Phase Handover Token gap.** The ENFORCEMENT MECHANISM DECLARATION asserts
   "role-scope exclusion at three phase boundaries" as the core provenance claim. But
   no element of the artifact confirms that transitions occurred. EF ran -- the section
   exists. BC ran -- PBI exists. Whether EF was excluded from Step 1 onward, and
   whether BC was excluded from Step 2 onward, is not observable from output: a reviewer
   must infer it from the absence of wrong-phase content. A PHASE-HANDOVER token at end
   of Step 0 (EF->BC) and Step 1 (BC->IA) would name the completing role, list its
   output, and declare the exclusion taking effect. The enforcement mechanism's core
   claim -- that cross-phase reasoning is structurally blocked -- becomes observable,
   not merely declared.

3. **Discard Log observability gap.** The STILL-LIVE FILTER makes a routing decision
   per candidate: YES -> correction register; NO -> topic-story. Accepted candidates
   are visible as correction entries. Rejected candidates are completely invisible. A
   reviewer cannot audit the filter's selectivity without re-running the full signal
   sweep. If IA writes a typed DISCARD entry for each NO decision -- naming the finding
   label, route, and specific reason it would not be carried as a false assumption --
   and emits a DISCARD-LOG-COMPLETE token summarizing the sweep's full scope, the
   filter's composition decisions become auditable. The same "here is what was read
   and why" principle that C-33 applied to EF's material selection applies to IA's
   candidate selection.

**Three R10 axes:**

- **Axis A -- BC Coverage Record:** BC produces BC-COVERAGE-RECORD after PBI freeze,
  naming design documents scanned, signals excluded, and PBI completeness basis
- **Axis B -- Phase Handover Tokens:** PHASE-HANDOVER-EF at end of Step 0 and
  PHASE-HANDOVER-BC at end of Step 1 confirm role exit, output produced, and handover
- **Axis C -- Discard Log:** STILL-LIVE FILTER NO decisions produce typed DISCARD
  entries; DISCARD-LOG-COMPLETE summarizes candidates considered / accepted / discarded

**Variation plan:**

- V-01: Axis A only (BC Coverage Record)
- V-02: Axis B only (Phase Handover Tokens)
- V-03: Axis C only (Discard Log)
- V-04: Axis A + Axis B
- V-05: Axis A + Axis B + Axis C (full integration)

All five carry C-01 through C-33. Predicted v10 score: 215/215 for all. The new axes
are v11 candidates -- they do not affect v10 scoring.

**Round 10 progression layer:** auditable record -> symmetric provenance. R9 converted
structural commitments to auditable records (EF invocation, repair routing, closure
token). R10 asks whether every role that makes a provenance claim should produce the
same class of record -- and whether process decisions (filter selectivity, phase
transitions) warrant the same "visible from output" treatment as content decisions.

---

## V-01 -- BC Coverage Record Axis

**Variation axis:** BC produces BC-COVERAGE-RECORD after PBI freeze (Axis A only)

**Hypothesis:** C-33 applied the principle "role-boundary provenance should be visible,
not just structurally enforced" to EF: the EF-INVOCATION-RECORD names what EF read and
what it excluded. BC operates under the identical exclusion contract and produces a
PBI of equivalent institutional weight. C-33's principle is not specific to EF -- it
follows from the meta-rule that any role-boundary claim should produce an observable
record. A BC-COVERAGE-RECORD testing whether the same standard applies to BC: does a
reviewer auditing PBI completeness need to re-run Step 1, or can the artifact answer
"what did BC scan?" directly? If BC's material scope is opaque while EF's is transparent,
structural provenance is asymmetric across roles that make equivalent claims.

**New structural element:** BC produces a BC-COVERAGE-RECORD block after PBI freeze,
listing: pre-investigation materials consulted (with identifiers), signal artifacts
excluded by name, and a one-sentence PBI completeness basis naming which materials
grounded the entry set.

**Expected v10 score:** 215/215

**Discriminant from R9 V-05:** BC-COVERAGE-RECORD absent in R9 V-05 (no BC parallel
to EF-INVOCATION-RECORD). All R9 axes (C-31/C-32/C-33) fully present.

---

Topic: {topic}

Synthesize what was unexpected. Three roles at three exclusive phase boundaries. Every
structural commitment is named, formal, and auditable from output. This is not a
summary. This is not a list of findings. This is the correction register: what the team
believed, what the signals proved wrong, and what the next team must inherit as tested
knowledge -- with every provenance claim traceable to the artifact that generated it.

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
              EF-INVOCATION-RECORD must name every pre-investigation
              source consulted and list all signal artifacts as excluded.
Out-of-scope: PBI production. Entry authoring. Chain verification.
Phase scope:  Step 0 only. EF excluded from Steps 1-7.
Gate return:  ENFORCEMENT MECHANISM section + EF-INVOCATION-RECORD
              complete before proceeding to Step 1.
----------------------------------------------------------------------
```

**Belief Cartographer (BC)** -- Step 1 exclusively.

```
BELIEF CARTOGRAPHER -- FUNCTION DECLARATION
----------------------------------------------------------------------
Function:     Pre-investigation belief recovery. PBI production.
              After PBI freeze, produce BC-COVERAGE-RECORD.
Input:        Design materials only. Same exclusion as EF.
Out-of-scope: Signal artifacts. Handle Ledger. Entry authoring.
Phase scope:  Step 1 only. PBI frozen at end of Step 1. BC excluded
              from Steps 2-7.
Gate return:  PBI complete with all PB-[NN] entries + BC-COVERAGE-RECORD
              naming materials consulted and signals excluded.
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
   A reviewer can re-derive the cost from this material alone.]
----------------------------------------------------------------------
```

---

### Step 1 -- [BC] PBI and Coverage Record

```
PBI PRODUCTION PROTOCOL
----------------------------------------------------------------------
Input:    Design materials only. Signal artifacts excluded.
Format:   PB-[NN]: ["Today's materials imply that X." No signal knowledge.]
Freeze:   PBI frozen at end of Step 1. BC excluded from Steps 2-7.
          PBI entries must not use handle labels (unavailable at Step 1).
----------------------------------------------------------------------
```

After PBI freeze, produce:

```
BC-COVERAGE-RECORD
----------------------------------------------------------------------
Step:       1 (BC phase; signal-reading phase not yet open)
Materials consulted (pre-investigation only):
  [List each design document, spec, proposal, or other pre-investigation
   source scanned to recover beliefs for PBI production. File name or
   artifact identifier per entry. Minimum one entry. Same exclusion
   scope as EF -- no signal artifacts.]
Signal artifacts excluded:
  [List each signal artifact by name and confirm it was not accessed
   during Step 1. A reviewer auditing PBI completeness uses this list
   to determine whether additional design materials exist that BC did
   not consult.]
PBI completeness basis:
  [One sentence: which material(s) above provide the primary basis for
   the PBI entry set. A reviewer can re-run BC against these materials
   to verify entry completeness without re-running the full investigation.]
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
              "What today's materials imply". Belief is ground truth.
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
        Token MUST quote the actual tier annotation string per rule.
        Declarative "all aligned" without quoted tier text fails.
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
per rule. Emit RULES-ANCHORED-COMPLETE with per-rule tier quotation, or RULES-ANCHORED-FAIL.

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
  2. EF-INVOCATION-RECORD (Step 0; pre-investigation materials; signals excluded)
  3. PBI PRODUCTION PROTOCOL output (BC)
  4. BC-COVERAGE-RECORD (Step 1; design materials scanned; signals excluded;
     completeness basis)
  5. HANDLE LEDGER PROTOCOL output (IA)
  6. Corrections -- HIGH -> MEDIUM -> LOW (CORRECTION RECORD SCHEMA)
  7. Entry Gate blocks (all STATUS: CLEARED)
  8. Chain Integrity Audit (all CHAIN-COMPLETE)
  9. Resolution Protocol trace (verifier named per flag type)
  10. Rules of Thumb (RULES-ANCHORED-COMPLETE with per-rule tier quotation)
  11. Surprise hierarchy (ranked with rationale)
  12. Pattern of inherited errors
  13. Blind Spot Map
  14. Correction Forward Statement (confirms NO-ECHO COST; names specific avoided failure)
  15. What this correction record excludes

Write to: simulations/topic/echo/{topic}-echo-{YYYY-MM-DD}.md

---

## V-02 -- Phase Handover Token Axis

**Variation axis:** PHASE-HANDOVER tokens at end of Steps 0 and 1 (Axis B only)

**Hypothesis:** The ENFORCEMENT MECHANISM DECLARATION asserts "role-scope exclusion at
three phase boundaries" as the provenance mechanism. But no visible token confirms
that transitions happened. A reviewer must infer phase compliance from the absence of
wrong-phase content. A PHASE-HANDOVER token at end of Step 0 and Step 1 makes each
transition observable: which role completed, what it produced (with output identifiers),
and that it is now excluded. The enforcement mechanism's core claim -- cross-phase
reasoning is structurally blocked by role scope -- becomes observable from output, not
merely asserted by specification. This tests whether the phase-boundary claim requires
the same "auditable from output" treatment that C-33 gave to EF's material-scope claim.
Discriminant: only the phase handover tokens change; all other R9 V-05 structure is
preserved, including EF-INVOCATION-RECORD, RESOLUTION PROTOCOL verifier fields, and
RULES-ANCHORED-COMPLETE per-rule quotation.

**New structural element:** PHASE-HANDOVER-EF token emitted at end of Step 0;
PHASE-HANDOVER-BC token emitted at end of Step 1, each naming: completing role, step
completed, output produced, exclusion taking effect, and receiving role.

**Expected v10 score:** 215/215

---

Topic: {topic}

Synthesize what was unexpected. Three roles at three exclusive phase boundaries. Every
structural commitment is named, formal, and auditable from output. This is not a
summary. This is not a list of findings. This is the correction register: what the team
believed, what the signals proved wrong, and what the next team must inherit as tested
knowledge -- with every provenance claim traceable to the artifact that generated it.

---

### Roles

**Enforcement Framer (EF)** -- Step 0 exclusively.

```
ENFORCEMENT FRAMER -- FUNCTION DECLARATION
----------------------------------------------------------------------
Function:     Produce the ENFORCEMENT MECHANISM section and the
              EF-INVOCATION-RECORD at artifact head position. Derive
              NO-ECHO COST from pre-investigation materials only --
              before any signal reading begins. Emit PHASE-HANDOVER-EF
              at end of Step 0 before handing over to BC.
Input:        Design materials only. Signal artifacts out of scope.
              EF-INVOCATION-RECORD must name every pre-investigation
              source consulted and list all signal artifacts as excluded.
Out-of-scope: PBI production. Entry authoring. Chain verification.
Phase scope:  Step 0 only. EF excluded from Steps 1-7.
Gate return:  ENFORCEMENT MECHANISM + EF-INVOCATION-RECORD +
              PHASE-HANDOVER-EF all complete before Step 1.
----------------------------------------------------------------------
```

**Belief Cartographer (BC)** -- Step 1 exclusively.

```
BELIEF CARTOGRAPHER -- FUNCTION DECLARATION
----------------------------------------------------------------------
Function:     Pre-investigation belief recovery. PBI production.
              Emit PHASE-HANDOVER-BC at end of Step 1 before IA begins.
Input:        Design materials only. Same exclusion as EF.
Out-of-scope: Signal artifacts. Handle Ledger. Entry authoring.
Phase scope:  Step 1 only. PBI frozen at end of Step 1. BC excluded
              from Steps 2-7.
Gate return:  PBI complete with all PB-[NN] entries + PHASE-HANDOVER-BC
              emitted before Step 2.
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

### Step 0 -- [EF] Enforcement Section, Invocation Record, and Phase Handover

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
   during Step 0. If none: "No signal artifacts present at Step 0."]
Cost derivation basis:
  [One sentence: which material above grounded the NO-ECHO COST claim.]
----------------------------------------------------------------------
```

At end of Step 0, emit phase handover token before proceeding:

```
PHASE-HANDOVER-EF
----------------------------------------------------------------------
Completing role:   ENFORCEMENT FRAMER (EF)
Step completed:    0
Output produced:   ENFORCEMENT MECHANISM DECLARATION + NO-ECHO COST
                   + EF-INVOCATION-RECORD
EF exclusion:      EF is now excluded from Steps 1-7. EF may not
                   read signal artifacts, produce PBI entries, author
                   corrections, or participate in chain verification.
Receiving role:    BELIEF CARTOGRAPHER (BC) -- Step 1
----------------------------------------------------------------------
```

---

### Step 1 -- [BC] PBI and Phase Handover

```
PBI PRODUCTION PROTOCOL
----------------------------------------------------------------------
Input:    Design materials only. Signal artifacts excluded.
Format:   PB-[NN]: ["Today's materials imply that X." No signal knowledge.]
Freeze:   PBI frozen at end of Step 1. BC excluded from Steps 2-7.
          PBI entries must not use handle labels (unavailable at Step 1).
----------------------------------------------------------------------
```

At end of Step 1, after PBI freeze, emit phase handover token:

```
PHASE-HANDOVER-BC
----------------------------------------------------------------------
Completing role:   BELIEF CARTOGRAPHER (BC)
Step completed:    1
Output produced:   PBI -- [N] entries: PB-01 through PB-[NN].
                   PBI is now frozen. No entries may be added or
                   altered after this token is emitted.
BC exclusion:      BC is now excluded from Steps 2-7. BC may not
                   read signal artifacts, author HL entries, draft
                   corrections, or participate in chain verification.
                   Exception: BC is the designated VERIFIER for
                   PBI-Ref mismatch repairs per RESOLUTION PROTOCOL.
Receiving role:    INSTITUTIONAL ARCHAEOLOGIST (IA) -- Steps 2-7
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
              "What today's materials imply". Belief is ground truth.
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
        Token MUST quote actual tier annotation string per rule.
        Declarative "all aligned" without quoted tier text fails.
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
per rule. Emit RULES-ANCHORED-COMPLETE with per-rule tier quotation, or RULES-ANCHORED-FAIL.

**Pattern of inherited errors:** 2-4 sentences. Named structural origin or stated absent.
Non-derivable from tallying individual corrections.

**Blind Spot Map:** Categories as types of wrong thinking specific to this artifact.
Assign each correction. Synthesis: non-derivable from individual corrections.

**Correction Forward Statement:**

1-3 sentences. Name the specific failure this artifact prevented. Identify the false
assumption the next team would have inherited and the investigation path it would have
misdirected. Confirm EF's NO-ECHO COST. Make the institutional purpose falsifiable.

**What this correction record excludes:** At least two categories with counts.

---

== ARTIFACT STRUCTURE ============================================================

  1. ENFORCEMENT MECHANISM DECLARATION (EF; position 1; NO-ECHO COST)
  2. EF-INVOCATION-RECORD (Step 0; pre-investigation materials; signals excluded)
  3. PHASE-HANDOVER-EF (EF exit confirmed; output listed; BC receiving)
  4. PBI PRODUCTION PROTOCOL output (BC)
  5. PHASE-HANDOVER-BC (BC exit confirmed; PBI frozen; entry count; IA receiving)
  6. HANDLE LEDGER PROTOCOL output (IA)
  7. Corrections -- HIGH -> MEDIUM -> LOW (CORRECTION RECORD SCHEMA)
  8. Entry Gate blocks (all STATUS: CLEARED)
  9. Chain Integrity Audit (all CHAIN-COMPLETE)
  10. Resolution Protocol trace (verifier named per flag type)
  11. Rules of Thumb (RULES-ANCHORED-COMPLETE with per-rule tier quotation)
  12. Surprise hierarchy (ranked with rationale)
  13. Pattern of inherited errors
  14. Blind Spot Map
  15. Correction Forward Statement (confirms NO-ECHO COST; names specific avoided failure)
  16. What this correction record excludes

Write to: simulations/topic/echo/{topic}-echo-{YYYY-MM-DD}.md

---

## V-03 -- Discard Log Axis

**Variation axis:** STILL-LIVE FILTER exclusions produce typed DISCARD entries and
DISCARD-LOG-COMPLETE summary token (Axis C only)

**Hypothesis:** The STILL-LIVE FILTER makes a binary routing decision per candidate:
YES enters the register; NO routes to topic-story. Accepted candidates are visible as
correction entries. Rejected candidates are completely invisible. A reviewer cannot
audit the filter's selectivity -- how many candidates were considered, what made the
register's composition what it is -- without re-running the full signal sweep from
scratch. This is an observability gap: the register's content is transparent; the
filter's decision record is not. If IA writes a typed DISCARD entry for each NO
decision (naming the finding label, route, and specific reason it fails the false-
assumption test) and emits a DISCARD-LOG-COMPLETE token showing total sweep scope,
the filter becomes auditable. The same "make it visible from output" principle that
C-33 applied to EF's material selection applies to IA's candidate selection -- both
are provenance decisions that shaped what ended up in the artifact.

**New structural element:** For each STILL-LIVE FILTER NO decision in Step 3, IA
writes a typed DISCARD entry. At end of Step 3 candidate evaluation, IA emits
DISCARD-LOG-COMPLETE summarizing: total candidates, accepted (correction), discarded.

**Expected v10 score:** 215/215

---

Topic: {topic}

Synthesize what was unexpected. Three roles at three exclusive phase boundaries. Every
structural commitment is named, formal, and auditable from output. This is not a
summary. This is not a list of findings. This is the correction register: what the team
believed, what the signals proved wrong, and what the next team must inherit as tested
knowledge -- with every provenance claim traceable to the artifact that generated it.

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
              EF-INVOCATION-RECORD must name every pre-investigation
              source consulted and list all signal artifacts as excluded.
Out-of-scope: PBI production. Entry authoring. Chain verification.
Phase scope:  Step 0 only. EF excluded from Steps 1-7.
Gate return:  ENFORCEMENT MECHANISM section + EF-INVOCATION-RECORD
              complete before proceeding to Step 1.
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
              For each STILL-LIVE FILTER NO decision in Step 3, produce
              a typed DISCARD entry. Emit DISCARD-LOG-COMPLETE after
              all candidates are evaluated.
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
   during Step 0. If none: "No signal artifacts present at Step 0."]
Cost derivation basis:
  [One sentence: which material above grounded the NO-ECHO COST claim.]
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

### Step 3 -- [IA] Draft All Corrections with Discard Log

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
  YES -> draft correction entry per schema above.
  NO -> write DISCARD entry immediately before continuing:

    DISCARD-[N]: [finding label or 3-5 word description]
    Route:  topic-story
    Reason: [one sentence: why a new team would not carry this as a
             false assumption. Names the specific claim or component
             that makes it non-qualifying. Generic "not relevant" fails.]

  After all candidates evaluated, emit:

    DISCARD-LOG-COMPLETE
    ----------------------------------------------------------------
    Candidates considered:   [total from signal sweep -- integer]
    Accepted (correction):   [count entering correction register]
    Discarded (topic-story): [count with DISCARD-[N] entries]
    ----------------------------------------------------------------

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
              "What today's materials imply". Belief is ground truth.
    Verifier: BELIEF CARTOGRAPHER (BC). BC confirms the corrected
              PBI-Ref maps to the stated belief at that identifier.
              IA may not self-certify PBI-Ref repairs.

  Handle mismatch (element 2):
    Repair:   Determine authoritative label (HL-[NN] or entry Name),
              then propagate from source to dependent.
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
        Token MUST quote actual tier annotation string per rule.
        Declarative "all aligned" without quoted tier text fails.
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
per rule. Emit RULES-ANCHORED-COMPLETE with per-rule tier quotation, or RULES-ANCHORED-FAIL.

**Pattern of inherited errors:** 2-4 sentences. Named structural origin or stated absent.
Non-derivable from tallying individual corrections.

**Blind Spot Map:** Categories as types of wrong thinking specific to this artifact.
Assign each correction. Synthesis: non-derivable from individual corrections.

**Correction Forward Statement:**

1-3 sentences. Name the specific failure this artifact prevented. Identify the false
assumption the next team would have inherited. Confirm EF's NO-ECHO COST.

**What this correction record excludes:** At least two categories with counts.

---

== ARTIFACT STRUCTURE ============================================================

  1. ENFORCEMENT MECHANISM DECLARATION (EF; position 1; NO-ECHO COST)
  2. EF-INVOCATION-RECORD (Step 0; pre-investigation materials; signals excluded)
  3. PBI PRODUCTION PROTOCOL output (BC)
  4. HANDLE LEDGER PROTOCOL output (IA)
  5. Corrections -- HIGH -> MEDIUM -> LOW (CORRECTION RECORD SCHEMA)
  6. DISCARD entries (DISCARD-[N]: for each STILL-LIVE FILTER NO decision)
  7. DISCARD-LOG-COMPLETE (candidates considered / accepted / discarded)
  8. Entry Gate blocks (all STATUS: CLEARED)
  9. Chain Integrity Audit (all CHAIN-COMPLETE)
  10. Resolution Protocol trace (verifier named per flag type)
  11. Rules of Thumb (RULES-ANCHORED-COMPLETE with per-rule tier quotation)
  12. Surprise hierarchy (ranked with rationale)
  13. Pattern of inherited errors
  14. Blind Spot Map
  15. Correction Forward Statement (confirms NO-ECHO COST; names specific avoided failure)
  16. What this correction record excludes

Write to: simulations/topic/echo/{topic}-echo-{YYYY-MM-DD}.md

---

## V-04 -- Axis A + Axis B: BC Coverage Record and Phase Handover Tokens

**Variation axis:** BC Coverage Record (V-01) + Phase Handover Tokens (V-02) combined

**Hypothesis:** V-01 makes BC's material scope auditable (parallel to EF-INVOCATION-
RECORD). V-02 makes role transitions observable (phase handover tokens at Steps 0 and
1). Each axis targets a different property of the pre-IA phases: Axis A answers "what
did BC read?"; Axis B answers "when did each role finish and what did it hand over?"
The two questions are distinct and non-redundant: BC-COVERAGE-RECORD names materials;
PHASE-HANDOVER-BC confirms the transition and freeze. V-04 tests whether these two
provenance claims are additive and compositionally stable without axis interference.
If the combination scores 215/215, both axes are independent and can become parallel
v11 criteria. The discriminant from V-05 isolates whether the Discard Log (Axis C)
is compositionally neutral with the combined pre-IA provenance package.

**New structural elements:**
1. BC-COVERAGE-RECORD after PBI freeze (Axis A)
2. PHASE-HANDOVER-EF at end of Step 0 (Axis B)
3. PHASE-HANDOVER-BC at end of Step 1, reflecting BC-COVERAGE-RECORD in output list (Axis B)

**Expected v10 score:** 215/215

---

Topic: {topic}

Synthesize what was unexpected. Three roles at three exclusive phase boundaries. Every
structural commitment is named, formal, and auditable from output. This is not a
summary. This is not a list of findings. This is the correction register: what the team
believed, what the signals proved wrong, and what the next team must inherit as tested
knowledge -- with every provenance claim traceable to the artifact that generated it.

---

### Roles

**Enforcement Framer (EF)** -- Step 0 exclusively.

```
ENFORCEMENT FRAMER -- FUNCTION DECLARATION
----------------------------------------------------------------------
Function:     Produce the ENFORCEMENT MECHANISM section and the
              EF-INVOCATION-RECORD at artifact head position. Derive
              NO-ECHO COST from pre-investigation materials only.
              Emit PHASE-HANDOVER-EF at end of Step 0.
Input:        Design materials only. Signal artifacts out of scope.
              EF-INVOCATION-RECORD must name every pre-investigation
              source consulted and list all signal artifacts as excluded.
Out-of-scope: PBI production. Entry authoring. Chain verification.
Phase scope:  Step 0 only. EF excluded from Steps 1-7.
Gate return:  ENFORCEMENT MECHANISM + EF-INVOCATION-RECORD +
              PHASE-HANDOVER-EF all complete before Step 1.
----------------------------------------------------------------------
```

**Belief Cartographer (BC)** -- Step 1 exclusively.

```
BELIEF CARTOGRAPHER -- FUNCTION DECLARATION
----------------------------------------------------------------------
Function:     Pre-investigation belief recovery. PBI production.
              After PBI freeze, produce BC-COVERAGE-RECORD.
              Emit PHASE-HANDOVER-BC before Step 2.
Input:        Design materials only. Same exclusion as EF.
Out-of-scope: Signal artifacts. Handle Ledger. Entry authoring.
Phase scope:  Step 1 only. PBI frozen at end of Step 1. BC excluded
              from Steps 2-7.
Gate return:  PBI + BC-COVERAGE-RECORD + PHASE-HANDOVER-BC all
              complete before proceeding to Step 2.
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

### Step 0 -- [EF] Enforcement Section, Invocation Record, and Phase Handover

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
  [List each design document, spec, or proposal consulted. Minimum one.]
Signal artifacts excluded:
  [List each signal artifact by name. If none: "No signal artifacts
   present at Step 0."]
Cost derivation basis:
  [One sentence: which material grounded the NO-ECHO COST claim.]
----------------------------------------------------------------------
```

```
PHASE-HANDOVER-EF
----------------------------------------------------------------------
Completing role:   ENFORCEMENT FRAMER (EF)
Step completed:    0
Output produced:   ENFORCEMENT MECHANISM DECLARATION + NO-ECHO COST
                   + EF-INVOCATION-RECORD
EF exclusion:      EF is now excluded from Steps 1-7.
Receiving role:    BELIEF CARTOGRAPHER (BC) -- Step 1
----------------------------------------------------------------------
```

---

### Step 1 -- [BC] PBI, Coverage Record, and Phase Handover

```
PBI PRODUCTION PROTOCOL
----------------------------------------------------------------------
Input:    Design materials only. Signal artifacts excluded.
Format:   PB-[NN]: ["Today's materials imply that X." No signal knowledge.]
Freeze:   PBI frozen at end of Step 1. BC excluded from Steps 2-7.
          PBI entries must not use handle labels (unavailable at Step 1).
----------------------------------------------------------------------
```

After PBI freeze, produce:

```
BC-COVERAGE-RECORD
----------------------------------------------------------------------
Step:       1 (BC phase; signal-reading phase not yet open)
Materials consulted (pre-investigation only):
  [List each design document, spec, or proposal scanned for belief
   recovery. File name or artifact identifier per entry. Minimum one.
   Same exclusion scope as EF -- no signal artifacts.]
Signal artifacts excluded:
  [List each signal artifact by name. A reviewer auditing PBI
   completeness uses this list to check for unconsulted materials.]
PBI completeness basis:
  [One sentence: which material(s) ground the PBI entry set. A reviewer
   can re-run BC against these to verify completeness independently.]
----------------------------------------------------------------------
```

Then emit:

```
PHASE-HANDOVER-BC
----------------------------------------------------------------------
Completing role:   BELIEF CARTOGRAPHER (BC)
Step completed:    1
Output produced:   PBI -- [N] entries: PB-01 through PB-[NN].
                   BC-COVERAGE-RECORD -- materials consulted listed.
                   PBI is now frozen.
BC exclusion:      BC is now excluded from Steps 2-7.
                   Exception: BC is the designated VERIFIER for
                   PBI-Ref mismatch repairs per RESOLUTION PROTOCOL.
Receiving role:    INSTITUTIONAL ARCHAEOLOGIST (IA) -- Steps 2-7
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
Elements: [1] PBI-Ref -> correct belief (quote PBI text)
          [2] Handle matches HL (quote HL title)
          [3] Source resolvable in this signal set
          [4] Verified quotation is actual text, not paraphrase
Token:    CHAIN-COMPLETE / CHAIN-FLAG per entry
Gate:     CHAIN-FLAG IS A HARD GATE.
----------------------------------------------------------------------
```

```
RESOLUTION PROTOCOL DECLARATION
----------------------------------------------------------------------
Exactly one named repair action per flag type. Each repair names the
VERIFIER ROLE whose attestation is required before the flag clears.

  PBI-Ref mismatch (element 1):
    Repair:   Replace PBI-Ref with correct identifier.
    Verifier: BELIEF CARTOGRAPHER (BC). IA may not self-certify.

  Handle mismatch (element 2):
    Repair:   Determine authoritative label; propagate from source.
    Verifier: INSTITUTIONAL ARCHAEOLOGIST (IA).

  Source absent (element 3):
    Repair:   Replace with resolvable artifact or demote to discard log.
    Verifier: INSTITUTIONAL ARCHAEOLOGIST (IA).

  Verified inaccurate (element 4):
    Repair:   Re-quote actual text from both PBI entry and source.
    Verifier: INSTITUTIONAL ARCHAEOLOGIST (IA).
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
Check:  RULES-ANCHORED -- each rule's tier must match parent Severity.
Gate:   RULES-ANCHORED BLOCKS on any MISALIGNED rule.
Closure: RULES-ANCHORED-COMPLETE token MUST quote tier annotation
        string per rule before asserting alignment.
Token format:
  RULES-ANCHORED-COMPLETE: R-01 "[TIER]" ALIGNED, R-02 "[TIER]"
    ALIGNED, ... -- distillation phase closed; tier annotations
    confirmed evidentiary.
----------------------------------------------------------------------
```

| Tier     | Rule (<=20 words)  | Encodes         |
|----------|--------------------|-----------------|
| [HIGH]   | {rule statement}   | {SURPRISE NAME} |
| [MEDIUM] | {rule statement}   | {SURPRISE NAME} |

RULES-ANCHORED check per rule. Emit RULES-ANCHORED-COMPLETE with per-rule tier
quotation, or RULES-ANCHORED-FAIL.

**Pattern of inherited errors:** 2-4 sentences. Named structural origin or stated absent.

**Blind Spot Map:** Assign each correction to a category of wrong thinking.

**Correction Forward Statement:** Name the specific failure prevented. Confirm NO-ECHO
COST. Make institutional purpose falsifiable.

**What this correction record excludes:** At least two categories with counts.

---

== ARTIFACT STRUCTURE ============================================================

  1. ENFORCEMENT MECHANISM DECLARATION (EF; position 1; NO-ECHO COST)
  2. EF-INVOCATION-RECORD (Step 0)
  3. PHASE-HANDOVER-EF (EF exit confirmed; BC receiving)
  4. PBI PRODUCTION PROTOCOL output (BC)
  5. BC-COVERAGE-RECORD (Step 1; materials scanned; signals excluded; completeness basis)
  6. PHASE-HANDOVER-BC (BC exit confirmed; PBI frozen + BC-COVERAGE-RECORD listed; IA receiving)
  7. HANDLE LEDGER PROTOCOL output (IA)
  8. Corrections -- HIGH -> MEDIUM -> LOW
  9. Entry Gate blocks (all STATUS: CLEARED)
  10. Chain Integrity Audit (all CHAIN-COMPLETE)
  11. Resolution Protocol trace (verifier named per flag type)
  12. Rules of Thumb (RULES-ANCHORED-COMPLETE with per-rule tier quotation)
  13. Surprise hierarchy (ranked with rationale)
  14. Pattern of inherited errors
  15. Blind Spot Map
  16. Correction Forward Statement
  17. What this correction record excludes

Write to: simulations/topic/echo/{topic}-echo-{YYYY-MM-DD}.md

---

## V-05 -- Full R10 Integration: Axis A + Axis B + Axis C

**Variation axis:** BC Coverage Record (V-01) + Phase Handover Tokens (V-02) + Discard
Log (V-03) -- all three R10 axes

**Hypothesis:** Each R10 axis converts a different class of structural opacity into
an observable record, each targeting a different production decision that currently
leaves no trace in output:
- Axis A: what BC read (PBI provenance)
- Axis B: when each pre-IA role finished and was excluded (phase transition)
- Axis C: what IA discarded and why (filter selectivity)
All three axes follow the same meta-principle established by C-33: role-boundary
provenance and process decisions should be visible from output, not merely enforced
by specification. No axis modifies the same artifact section as another: A targets
Step 1 (BC output), B targets Step 0 and Step 1 transition tokens, C targets Step 3
(IA filter decisions). The combination is structurally non-interfering. V-05 tests
whether all three hold simultaneously at 215/215 -- confirming they are independent
and each is a valid v11 candidate. Score differential between V-04 and V-05 isolates
whether the Discard Log (Axis C) is compositionally neutral with the pre-IA provenance
package.

**New structural elements:**
1. BC-COVERAGE-RECORD after PBI freeze (Axis A)
2. PHASE-HANDOVER-EF at end of Step 0; PHASE-HANDOVER-BC at end of Step 1 (Axis B)
3. Typed DISCARD entries per STILL-LIVE FILTER NO decision + DISCARD-LOG-COMPLETE (Axis C)

**Expected v10 score:** 215/215

---

Topic: {topic}

Synthesize what was unexpected. Three roles at three exclusive phase boundaries. Every
structural commitment is named, formal, and auditable from output. This is not a
summary. This is not a list of findings. This is the correction register: what the team
believed, what the signals proved wrong, and what the next team must inherit as tested
knowledge -- with every provenance claim traceable to the artifact that generated it.

---

### Roles

**Enforcement Framer (EF)** -- Step 0 exclusively.

```
ENFORCEMENT FRAMER -- FUNCTION DECLARATION
----------------------------------------------------------------------
Function:     Produce the ENFORCEMENT MECHANISM section and the
              EF-INVOCATION-RECORD at artifact head position. Derive
              NO-ECHO COST from pre-investigation materials only --
              before any signal reading begins. Emit PHASE-HANDOVER-EF
              at end of Step 0.
Input:        Design materials only. Signal artifacts out of scope.
              EF-INVOCATION-RECORD must name every pre-investigation
              source consulted and list all signal artifacts as excluded.
Out-of-scope: PBI production. Entry authoring. Chain verification.
Phase scope:  Step 0 only. EF excluded from Steps 1-7.
Gate return:  ENFORCEMENT MECHANISM + EF-INVOCATION-RECORD +
              PHASE-HANDOVER-EF all complete before Step 1.
----------------------------------------------------------------------
```

**Belief Cartographer (BC)** -- Step 1 exclusively.

```
BELIEF CARTOGRAPHER -- FUNCTION DECLARATION
----------------------------------------------------------------------
Function:     Pre-investigation belief recovery. PBI production.
              After PBI freeze, produce BC-COVERAGE-RECORD.
              Emit PHASE-HANDOVER-BC before IA begins Step 2.
Input:        Design materials only. Same exclusion as EF.
Out-of-scope: Signal artifacts. Handle Ledger. Entry authoring.
Phase scope:  Step 1 only. PBI frozen at end of Step 1. BC excluded
              from Steps 2-7.
Gate return:  PBI complete with all PB-[NN] entries + BC-COVERAGE-RECORD
              + PHASE-HANDOVER-BC before Step 2.
----------------------------------------------------------------------
```

**Institutional Archaeologist (IA)** -- Steps 2-7.

```
INSTITUTIONAL ARCHAEOLOGIST -- FUNCTION DECLARATION
----------------------------------------------------------------------
Function:     False-assumption recovery. Correction register only.
              For each STILL-LIVE FILTER NO decision in Step 3, produce
              a typed DISCARD entry immediately. After all candidates
              are evaluated in Step 3, emit DISCARD-LOG-COMPLETE.
Input:        Signal artifacts + frozen PBI (read-only).
Out-of-scope: PBI authorship (frozen). Enforcement section (EF; immutable).
Orienting:    "What would the next team build wrong?"
Phase scope:  Steps 2-7 only.
----------------------------------------------------------------------
```

---

### Step 0 -- [EF] Enforcement Section, Invocation Record, and Phase Handover

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
   during Step 0. If none: "No signal artifacts present at Step 0."]
Cost derivation basis:
  [One sentence: which material above grounded the NO-ECHO COST claim.
   A reviewer can re-derive the cost from this material alone to
   confirm the claim is prospective, not retrospective.]
----------------------------------------------------------------------
```

```
PHASE-HANDOVER-EF
----------------------------------------------------------------------
Completing role:   ENFORCEMENT FRAMER (EF)
Step completed:    0
Output produced:   ENFORCEMENT MECHANISM DECLARATION + NO-ECHO COST
                   + EF-INVOCATION-RECORD
EF exclusion:      EF is now excluded from Steps 1-7. EF may not
                   read signal artifacts, produce PBI entries, author
                   corrections, or participate in chain verification.
Receiving role:    BELIEF CARTOGRAPHER (BC) -- Step 1
----------------------------------------------------------------------
```

---

### Step 1 -- [BC] PBI, Coverage Record, and Phase Handover

```
PBI PRODUCTION PROTOCOL
----------------------------------------------------------------------
Input:    Design materials only. Signal artifacts excluded.
Format:   PB-[NN]: ["Today's materials imply that X." No signal knowledge.]
Freeze:   PBI frozen at end of Step 1. BC excluded from Steps 2-7.
          PBI entries must not use handle labels (unavailable at Step 1).
----------------------------------------------------------------------
```

After PBI freeze, produce:

```
BC-COVERAGE-RECORD
----------------------------------------------------------------------
Step:       1 (BC phase; signal-reading phase not yet open)
Materials consulted (pre-investigation only):
  [List each design document, spec, proposal, or other pre-investigation
   source scanned to recover beliefs for PBI production. File name or
   artifact identifier per entry. Minimum one entry. Same exclusion
   scope as EF -- no signal artifacts.]
Signal artifacts excluded:
  [List each signal artifact by name and confirm it was not accessed
   during Step 1. A reviewer auditing PBI completeness uses this list
   to determine whether additional design materials exist that BC did
   not consult.]
PBI completeness basis:
  [One sentence: which material(s) above provide the primary basis for
   the PBI entry set. A reviewer can re-run BC against these materials
   to verify entry completeness without re-running the investigation.]
----------------------------------------------------------------------
```

Then emit phase handover:

```
PHASE-HANDOVER-BC
----------------------------------------------------------------------
Completing role:   BELIEF CARTOGRAPHER (BC)
Step completed:    1
Output produced:   PBI -- [N] entries: PB-01 through PB-[NN].
                   BC-COVERAGE-RECORD -- materials consulted listed.
                   PBI is now frozen. No entries may be added or
                   altered after this token is emitted.
BC exclusion:      BC is now excluded from Steps 2-7. BC may not
                   read signal artifacts, author HL entries, draft
                   corrections, or participate in chain verification.
                   Exception: BC is the designated VERIFIER for
                   PBI-Ref mismatch repairs per RESOLUTION PROTOCOL.
Receiving role:    INSTITUTIONAL ARCHAEOLOGIST (IA) -- Steps 2-7
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

### Step 3 -- [IA] Draft All Corrections with Discard Log

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
  YES -> draft correction entry per schema above.
  NO -> write DISCARD entry immediately before continuing to next candidate:

    DISCARD-[N]: [finding label or 3-5 word description]
    Route:  topic-story
    Reason: [one sentence: why a new team would not carry this as a
             false assumption. Specific claim or component named.
             Generic "not relevant" fails.]

  After all candidates evaluated, emit:

    DISCARD-LOG-COMPLETE
    ----------------------------------------------------------------
    Candidates considered:   [total from signal sweep -- integer]
    Accepted (correction):   [count entering correction register]
    Discarded (topic-story): [count with typed DISCARD-[N] entries]
    ----------------------------------------------------------------

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
          ENTRY GATE -- confirms four chain elements are internally
          consistent.
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
              "What today's materials imply". Belief is ground truth;
              do not alter it.
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
        Token MUST quote the actual tier annotation string per rule
        before asserting alignment. Declarative "all aligned" without
        quoted tier text fails the evidentiary standard.
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
per rule. Emit RULES-ANCHORED-COMPLETE with per-rule tier quotation, or RULES-ANCHORED-FAIL.

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
  2. EF-INVOCATION-RECORD (Step 0; pre-investigation materials; signals excluded)
  3. PHASE-HANDOVER-EF (EF exit confirmed; output listed; BC receiving)
  4. PBI PRODUCTION PROTOCOL output (BC)
  5. BC-COVERAGE-RECORD (Step 1; design materials scanned; signals excluded;
     PBI completeness basis)
  6. PHASE-HANDOVER-BC (BC exit confirmed; PBI frozen; entry count;
     BC-COVERAGE-RECORD listed; IA receiving)
  7. HANDLE LEDGER PROTOCOL output (IA)
  8. Corrections -- HIGH -> MEDIUM -> LOW (CORRECTION RECORD SCHEMA)
  9. DISCARD entries (DISCARD-[N]: for each STILL-LIVE FILTER NO decision)
  10. DISCARD-LOG-COMPLETE (candidates considered / accepted / discarded)
  11. Entry Gate blocks (ENTRY GATE DECLARATION; all STATUS: CLEARED)
  12. Chain Integrity Audit (CHAIN INTEGRITY AUDIT DECLARATION; all CHAIN-COMPLETE)
  13. Resolution Protocol trace (RESOLUTION PROTOCOL DECLARATION; verifier named per flag type)
  14. Rules of Thumb (RULES OF THUMB DECLARATION; RULES-ANCHORED-COMPLETE with per-rule tier quotation)
  15. Surprise hierarchy (ranked with rationale)
  16. Pattern of inherited errors
  17. Blind Spot Map
  18. Correction Forward Statement (confirms NO-ECHO COST; names specific avoided failure)
  19. What this correction record excludes

Write to: simulations/topic/echo/{topic}-echo-{YYYY-MM-DD}.md

---

## Round 10 Summary

| Variation | Axis A | Axis B | Axis C | Predicted v10 |
|-----------|:------:|:------:|:------:|:-------------:|
| V-01 | BC-COVERAGE-RECORD | -- | -- | 215/215 |
| V-02 | -- | PHASE-HANDOVER tokens | -- | 215/215 |
| V-03 | -- | -- | DISCARD LOG | 215/215 |
| V-04 | BC-COVERAGE-RECORD | PHASE-HANDOVER tokens | -- | 215/215 |
| V-05 | BC-COVERAGE-RECORD | PHASE-HANDOVER tokens | DISCARD LOG | 215/215 |

**Meta-principle under test (R10):** symmetric provenance -- every role that makes a
material-scope exclusion claim, every phase transition that implements role exclusion,
and every process decision that shapes artifact composition should be observable from
output, not merely enforced by specification.

**Three structural gaps targeted:**

| Gap | Commitment enforced | Axis | Observable with |
|-----|---------------------|------|-----------------|
| BC provenance | BC reads design materials only | A | BC-COVERAGE-RECORD |
| Phase transitions | Role boundaries are exclusive | B | PHASE-HANDOVER tokens |
| Filter selectivity | STILL-LIVE FILTER routes excluded candidates | C | DISCARD LOG |

**Progression layer (R10 candidate):** auditable record -> symmetric provenance.
R9 established that structural commitments should produce auditable records (EF-INVOCATION-
RECORD, CHAIN-COMPLETE, RULES-ANCHORED-COMPLETE with quotation). R10 asks whether
the same "auditable from output" standard applies symmetrically across all roles,
all phase transitions, and all selection decisions -- not just the ones C-33 targeted.

**Score prediction table under v10:**

| Variation | C-31 | C-32 | C-33 | v10 score | Notes |
|-----------|:----:|:----:|:----:|:---------:|-------|
| V-01 | PASS | PASS | PASS | 215/215 | Adds BC-COVERAGE-RECORD only |
| V-02 | PASS | PASS | PASS | 215/215 | Adds PHASE-HANDOVER tokens only |
| V-03 | PASS | PASS | PASS | 215/215 | Adds DISCARD LOG only |
| V-04 | PASS | PASS | PASS | 215/215 | Adds A+B; no Discard Log |
| V-05 | PASS | PASS | PASS | 215/215 | All three R10 axes |

All five carry C-31 (RESOLUTION PROTOCOL verifier per flag type), C-32 (RULES-ANCHORED-
COMPLETE with per-rule tier quotation), and C-33 (EF-INVOCATION-RECORD). The R10 axes
are v11 candidates that do not affect v10 scoring.
