---
skill: quest-variate
skill_target: topic-echo
date: 2026-03-16
round: 13
rubric: v13
rubric_file: simulations/quest/rubrics/topic-echo-rubric-v13-2026-03-16.md
rubric_max: 260
---

# Variations: `topic:echo` -- Round 13 (2026-03-16)

**Rubric:** v13 (2026-03-16) | **Criteria:** 42 (5 essential / 3 recommended / 34 aspirational)

---

## Design Context

R12 V-05 achieves 245/245 under v12 and 260/260 under v13. The three legibility criteria
formalized in v13 -- BC-STEP1-PROTOCOL-PREDECLARATION (C-40), PHASE-HANDOVER-UNIVERSAL-
COVERAGE (C-41), and MUST-CLAUSE-SCOPE-DECLARATION (C-42) -- were satisfied incidentally by
R12 V-05's structural implementations. Round 13 does not re-implement R12's axes. It tests
whether the same scoring profiles can be achieved through **alternative structural
implementations** of each legibility mechanism, confirming that C-40, C-41, and C-42 are
triggered by pattern class, not by surface form.

R12 implementations and R13 alternatives:

- **C-40 (BC-STEP1-PROTOCOL-PREDECLARATION)** -> **Axis A-prime -- Standalone Section**:
  R12 V-01 placed BC-STEP1-PROTOCOL inside the BC Function Declaration code block. The table
  is pre-execution, but embedded within the role declaration -- a reviewer must enter the BC
  code block to find it. R13 V-01 extracts BC-STEP1-PROTOCOL as a **standalone named section**
  (`### BC-STEP1-PROTOCOL`) positioned after the Roles section and before Step 0 begins. The
  BC Function Declaration contains only a forward reference: "sub-phases declared in the
  BC-STEP1-PROTOCOL section below." The full protocol table (sub-phase names, scopes, gate
  tokens, BC-COVERAGE-RECORD return) appears as a first-class prompt section with its own
  heading. A reviewer navigates to the section heading from document structure, without
  entering any code block. C-40 is satisfied because the decomposition is legible from the
  section header position alone.

- **C-41 (PHASE-HANDOVER-UNIVERSAL-COVERAGE)** -> **Axis B-prime -- Pre-Declared Inventory**:
  R12 V-02 produced inline PHASE-HANDOVER tables at all seven stage exits (Steps 0-6), making
  universal coverage verifiable by linear traversal. R13 V-02 adds a **PHASE-HANDOVER-
  INVENTORY** section before Step 0 that pre-declares all seven expected transitions (by step
  number, completing role, and receiving role) in a single reference table. Each step still
  produces its inline PHASE-HANDOVER-[N] table. Universal coverage is now simultaneously
  verifiable by cross-referencing the inventory list against the inline tables -- a two-source
  check rather than a count. The inventory makes universality inspectable from the pre-
  declaration alone, before any step output is read. C-41 is satisfied because schema
  compliance is verifiable across all N tables simultaneously from the inventory reference.

- **C-42 (MUST-CLAUSE-SCOPE-DECLARATION)** -> **Axis C-prime -- Scope-Field Structure**:
  R12 V-03 embedded the universal quantifier as an inline sentence opener ("For every
  candidate, produce exactly one of..."). The scope is readable but requires parsing the
  action sentence. R13 V-03 restructures each MUST clause with an explicit **Scope:** field
  as a named structural element preceding the Action field. A reviewer checking which entity
  class MUST-3 governs reads the Scope label without reading the Action. Scope is a structural
  element, not a sentence modifier. C-42 is satisfied because each clause's governed class is
  declared as a named field, independently auditable from the clause body.

**Predicted scoring under v13:**

| Variation | C-37 | C-38 | C-39 | C-40 | C-41 | C-42 | Predicted |
|-----------|:----:|:----:|:----:|:----:|:----:|:----:|:---------:|
| V-01 | PASS | FAIL | FAIL | PASS | FAIL | FAIL | 230 |
| V-02 | FAIL | PASS | FAIL | FAIL | PASS | FAIL | 230 |
| V-03 | FAIL | FAIL | PASS | FAIL | FAIL | PASS | 230 |
| V-04 | PASS | PASS | FAIL | PASS | PASS | FAIL | 240 |
| **V-05** | PASS | PASS | PASS | PASS | PASS | PASS | **260** |

**R13 progression layer:** R12 demonstrated that embedded protocol tables / inline universal
handover tables / inline MUST-clause quantifiers reliably trigger C-40/C-41/C-42. R13 tests
whether a standalone section protocol / pre-declared inventory with inline tables / scope-field
structure produces identical scoring profiles. If both sets achieve the same scores, the
legibility criteria are implementation-robust: positional class determines pass/fail, not
surface form within that class.

---

## V-01 -- Axis A-prime: Standalone BC-STEP1-PROTOCOL Section

**Variation axis:** Lifecycle emphasis -- BC's sub-phase decomposition extracted as a
standalone named section (`### BC-STEP1-PROTOCOL`) with its own heading, positioned after the
Roles section and before Step 0 begins (Axis A-prime only)

**Hypothesis:** R12 V-01 placed BC-STEP1-PROTOCOL inside the BC Function Declaration code
block. Pre-execution positioning holds -- the declaration is before Step 1 -- but access
requires entering the BC code block. If BC-STEP1-PROTOCOL is a standalone section with its
own heading, the protocol table is addressable by navigating to the section heading alone,
without opening any code block. The BC Function Declaration contains only a forward reference.
Sub-phase labels, gate tokens, and BC-COVERAGE-RECORD return are fully specified in the
standalone table before Step 0 begins. C-40 is satisfied because the protocol is legible
from document structure, not from parsing a role declaration code block.

**Expected v13 score:** 230 (C-37 PASS; C-40 PASS; C-38 FAIL; C-41 FAIL; C-39 FAIL;
C-42 FAIL)

---

Topic: `{topic}`

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
Out-of-scope: PBI production. Entry authoring. Chain verification.
Phase scope:  Step 0 only. EF excluded from Steps 1-7.
Gate return:  ENFORCEMENT MECHANISM section + EF-INVOCATION-RECORD
              complete before proceeding to Step 1.
----------------------------------------------------------------------
```

**Belief Cartographer (BC)** -- Step 1 exclusively; three sub-phases declared in the
BC-STEP1-PROTOCOL section below.

```
BELIEF CARTOGRAPHER -- FUNCTION DECLARATION
----------------------------------------------------------------------
Function:     Pre-investigation belief recovery. Execute Step 1 in the
              three sequential sub-phases declared in the BC-STEP1-
              PROTOCOL section below. Do not merge sub-phases. Write
              each gate token before advancing to the next sub-phase.
Input:        Design materials only. Signal artifacts out of scope.
Out-of-scope: Signal artifacts. Handle Ledger. Entry authoring.
Phase scope:  Step 1 only. BC excluded from Steps 2-7 after the
              [COVERAGE AUDIT] gate token is written.
Gate return:  PBI (all PB-[NN] entries frozen) + BC-COVERAGE-RECORD
              before Step 2 begins.
----------------------------------------------------------------------
```

**Institutional Archaeologist (IA)** -- Steps 2-7.

```
INSTITUTIONAL ARCHAEOLOGIST -- FUNCTION DECLARATION
----------------------------------------------------------------------
Function:     False-assumption recovery. Correction register only.
Input:        Signal artifacts + frozen PBI (read-only).
Out-of-scope: PBI authorship (frozen). Enforcement section (immutable).
Orienting:    "What would the next team build wrong?"
Phase scope:  Steps 2-7 only.
----------------------------------------------------------------------
```

---

### BC-STEP1-PROTOCOL

Executed by BC during Step 1 in three sequential sub-phases. Write each gate token before
advancing to the next sub-phase. Do not merge sub-phases. This section is the pre-execution
contract for Step 1, positioned before Step 0 begins. The BC Function Declaration references
this section by name only; the full protocol specification is here, not inside the BC code
block.

| Sub-phase | Scope | Gate Token |
|-----------|-------|------------|
| [SCAN] | Read design materials. List all belief candidates. No pruning or evaluation during this phase. | `COMMIT-SCAN: [N] candidates identified.` |
| [FREEZE] | Produce PBI from scan results. Lock all PB-[NN] entries. No additions after gate token. | `COMMIT-FREEZE: PBI frozen at [N] entries.` |
| [COVERAGE AUDIT] | Audit domain coverage. Produce BC-COVERAGE-RECORD (schema below). BC exclusion takes effect after this gate token is written. | BC-COVERAGE-RECORD (schema below). |

BC-COVERAGE-RECORD schema:

```
BC-COVERAGE-RECORD
----------------------------------------------------------------------
Sub-phase:  [COVERAGE AUDIT] -- gate token declared in BC-STEP1-PROTOCOL.
Materials consulted (pre-investigation only):
  [List each design document scanned during [SCAN] and [FREEZE].
   Minimum one entry.]
Signal artifacts excluded:
  [List each signal artifact; confirm not accessed during Step 1.]
PBI completeness basis:
  [One sentence: which material(s) provide the primary PBI basis.]
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
Reviewer implication: Independence is enforced by role boundary.
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
   A reviewer can re-derive the cost from this material alone.]
----------------------------------------------------------------------
```

---

### Step 1 -- [BC] Belief Inventory and Coverage Audit

Execute BC-STEP1-PROTOCOL as declared in the BC-STEP1-PROTOCOL section above. Write each
gate token before advancing to the next sub-phase.

**[SCAN]** Read all design materials within BC's input scope. Signal artifacts are out of
scope for this sub-phase. Identify every belief candidate -- any claim, assumption, or
design premise that could be carried as prior knowledge into investigation. List all
candidates. Complete the full scan before moving to [FREEZE].

`COMMIT-SCAN: [N] candidates identified.`

**[FREEZE]** Produce the PBI from the scanned candidates.

```
PBI PRODUCTION PROTOCOL
----------------------------------------------------------------------
Input:    Design materials only. Signal artifacts excluded.
Format:   PB-[NN]: ["Today's materials imply that X." No signal
          knowledge.]
Freeze:   PBI frozen after COMMIT-FREEZE token. BC may not add new
          PB-[NN] entries after this point. PBI entries must not use
          handle labels (unavailable at Step 1).
----------------------------------------------------------------------
```

`COMMIT-FREEZE: PBI frozen at [N] entries.`

**[COVERAGE AUDIT]** After PBI freeze, produce BC-COVERAGE-RECORD using the schema declared
in the BC-STEP1-PROTOCOL section above. BC exclusion from Steps 2-7 does not take effect
until BC-COVERAGE-RECORD is written.

BC is now excluded from Steps 2-7.

---

### Step 2 -- [IA] Handle Ledger

```
HANDLE LEDGER PROTOCOL
----------------------------------------------------------------------
Timing:   After reading all signal artifacts. Before writing corrections.
Format:   HL-[NN]: [finding-specific label -- 2-5 words; finding
          language]
Test:     No PBI entry names its handle. No HL entry echoes a PBI
          entry verbatim. Either violation is a phase contract failure.
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
(narration -> future-team framing), Wrong (softener -> specific wrong
component), Decide (deferral -> blocking decision), Verified
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
Gate:     CHAIN-FLAG IS A HARD GATE. Any flag halts artifact completion
          until resolved via RESOLUTION PROTOCOL below.
----------------------------------------------------------------------
```

```
RESOLUTION PROTOCOL DECLARATION
----------------------------------------------------------------------
Exactly one named repair action per flag type. Each repair names the
VERIFIER ROLE whose attestation is required before the flag clears.

  PBI-Ref mismatch (element 1):
    Repair:   Replace PBI-Ref with identifier matching belief in
              "What today's materials imply". Belief is ground truth.
    Verifier: BELIEF CARTOGRAPHER (BC).

  Handle mismatch (element 2):
    Repair:   Determine authoritative label (HL-[NN] or entry Name),
              then propagate from source to dependent.
    Verifier: INSTITUTIONAL ARCHAEOLOGIST (IA).

  Source absent (element 3):
    Repair:   Replace with resolvable artifact, or demote to discard
              log with typed route reason.
    Verifier: INSTITUTIONAL ARCHAEOLOGIST (IA).

  Verified inaccurate (element 4):
    Repair:   Re-quote actual text from both PBI entry and source.
              If source unlocatable, apply element 3 protocol first.
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
Check:  RULES-ANCHORED traceability -- each rule's tier annotation
        must match Severity of parent entry.
Gate:   RULES-ANCHORED BLOCKS on any MISALIGNED rule.
Closure: After all rules ALIGNED, emit RULES-ANCHORED-COMPLETE.
         Token MUST quote actual tier annotation string per rule.
Token format:
  RULES-ANCHORED-COMPLETE: R-01 "[TIER]" ALIGNED, R-02 "[TIER]"
    ALIGNED, ... -- distillation phase closed.
Fail token:
  RULES-ANCHORED-FAIL: R-[NN] "[TIER]" MISALIGNED -- expected
    {parent Severity} vs found {annotation text}.
----------------------------------------------------------------------
```

| Tier     | Rule (<=20 words)  | Encodes         |
|----------|--------------------|-----------------|
| [HIGH]   | {rule statement}   | {SURPRISE NAME} |
| [MEDIUM] | {rule statement}   | {SURPRISE NAME} |

RULES-ANCHORED check and closure token.

**Pattern of inherited errors:** 2-4 sentences. Named structural origin or stated absent.
Non-derivable from tallying individual corrections.

**Blind Spot Map:** Categories as types of wrong thinking specific to this artifact.
Assign each correction. Synthesis non-derivable from individual corrections.

**Correction Forward Statement:** 1-3 sentences. Name the specific failure this artifact
prevented. Identify the false assumption the next team would have inherited. Confirm EF's
NO-ECHO COST. Make the institutional purpose falsifiable.

**What this correction record excludes:** At least two categories with counts.

---

== ARTIFACT STRUCTURE ============================================================

  1. ENFORCEMENT MECHANISM DECLARATION (EF; position 1; NO-ECHO COST)
  2. EF-INVOCATION-RECORD (Step 0; pre-investigation materials; signals excluded)
  3. PBI output (BC; [FREEZE] sub-phase; COMMIT-SCAN + COMMIT-FREEZE tokens present)
  4. BC-COVERAGE-RECORD ([COVERAGE AUDIT] gate; schema from BC-STEP1-PROTOCOL section)
  5. HANDLE LEDGER output (IA)
  6. Corrections -- HIGH -> MEDIUM -> LOW
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

## V-02 -- Axis B-prime: PHASE-HANDOVER-INVENTORY Pre-Declaration

**Variation axis:** Output format -- a PHASE-HANDOVER-INVENTORY section pre-declares all
seven expected transitions before Step 0 begins; each step exit still produces an inline
PHASE-HANDOVER-[N] table in the 5-row schema (Axis B-prime only)

**Hypothesis:** R12 V-02 produced inline PHASE-HANDOVER tables at all seven stage exits.
Universal coverage is verifiable by linear traversal: count seven tables, verify all present.
If a PHASE-HANDOVER-INVENTORY is pre-declared before Step 0 -- listing all seven transitions
by step number, completing role, and receiving role -- coverage is simultaneously verifiable
by cross-referencing the inventory against the inline tables. A reviewer auditing
completeness checks the inventory list once against the seven inline tables; there is no
traversal dependency. C-41 is satisfied because universality is inspectable from the
pre-declaration, and schema compliance is verifiable across all N tables simultaneously
by cross-table column inspection against the inventory reference.

**Expected v13 score:** 230 (C-38 PASS; C-41 PASS; C-37 FAIL; C-40 FAIL; C-39 FAIL;
C-42 FAIL)

---

Topic: `{topic}`

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
Out-of-scope: PBI production. Entry authoring. Chain verification.
Phase scope:  Step 0 only. EF excluded from Steps 1-7.
Gate return:  ENFORCEMENT MECHANISM section + EF-INVOCATION-RECORD +
              PHASE-HANDOVER-0 table before proceeding to Step 1.
----------------------------------------------------------------------
```

**Belief Cartographer (BC)** -- Step 1 exclusively.

```
BELIEF CARTOGRAPHER -- FUNCTION DECLARATION
----------------------------------------------------------------------
Function:     Pre-investigation belief recovery. Read design materials.
              Produce PBI (Prior Belief Inventory). Freeze all entries.
Input:        Design materials only. Signal artifacts out of scope.
Out-of-scope: Signal artifacts. Handle Ledger. Entry authoring.
Phase scope:  Step 1 only. BC excluded from Steps 2-7.
Gate return:  PBI (all PB-[NN] entries frozen) + PHASE-HANDOVER-1
              table before Step 2 begins.
----------------------------------------------------------------------
```

**Institutional Archaeologist (IA)** -- Steps 2-7.

```
INSTITUTIONAL ARCHAEOLOGIST -- FUNCTION DECLARATION
----------------------------------------------------------------------
Function:     False-assumption recovery. Correction register only.
              Each IA stage exit (Steps 2-6) produces a PHASE-HANDOVER-[N]
              table before advancing to the next step.
Input:        Signal artifacts + frozen PBI (read-only).
Out-of-scope: PBI authorship (frozen). Enforcement section (immutable).
Orienting:    "What would the next team build wrong?"
Phase scope:  Steps 2-7 only.
----------------------------------------------------------------------
```

**Phase Handover Schema (universal -- all 7 exits, Steps 0-6):**

All PHASE-HANDOVER-[N] tables (N = 0 through 6) use this schema exactly.
Five rows. Fixed field names. Do not substitute prose. Do not add or remove rows.

| Field | Content |
|-------|---------|
| Completing Role | [role name and step number] |
| Step Completed | [step number and name] |
| Output Produced | [artifact(s) produced at this exit] |
| Exclusion In Effect | [what the completing role/phase can no longer modify] |
| Receiving Role | [role name and step number taking control] |

---

### PHASE-HANDOVER-INVENTORY

Pre-declared registry of all seven phase transitions for this workflow. Every step exit in
Steps 0 through 6 must produce a PHASE-HANDOVER-[N] table matching this inventory. Coverage
is complete when all seven inventory entries have a corresponding inline table. Cross-reference
this inventory against the inline tables to verify universality without traversal.

| Transition | Step Completed | Completing Role | Receiving Role |
|------------|----------------|-----------------|----------------|
| PHASE-HANDOVER-0 | Step 0 -- Enforcement Section and Invocation Record | Enforcement Framer (EF) | Belief Cartographer (BC) |
| PHASE-HANDOVER-1 | Step 1 -- Belief Inventory | Belief Cartographer (BC) | Institutional Archaeologist (IA) |
| PHASE-HANDOVER-2 | Step 2 -- Handle Ledger | Institutional Archaeologist (IA) | Institutional Archaeologist (IA) |
| PHASE-HANDOVER-3 | Step 3 -- Draft All Corrections | Institutional Archaeologist (IA) | Institutional Archaeologist (IA) |
| PHASE-HANDOVER-4 | Step 4 -- Register Audit | Institutional Archaeologist (IA) | Institutional Archaeologist (IA) |
| PHASE-HANDOVER-5 | Step 5 -- Entry Gate | Institutional Archaeologist (IA) | Institutional Archaeologist (IA) |
| PHASE-HANDOVER-6 | Step 6 -- Chain Integrity Audit | Institutional Archaeologist (IA) | Institutional Archaeologist (IA) |

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
Reviewer implication: Independence is enforced by role boundary.
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
  [List each pre-investigation source. Minimum one entry.]
Signal artifacts excluded:
  [List each signal artifact; confirm not accessed at Step 0.]
Cost derivation basis:
  [One sentence: which material grounded the NO-ECHO COST claim.]
----------------------------------------------------------------------
```

**PHASE-HANDOVER-0** (inventory entry: EF -> BC):

| Field | Content |
|-------|---------|
| Completing Role | Enforcement Framer (EF) -- Step 0 |
| Step Completed | Step 0 -- Enforcement Section and Invocation Record |
| Output Produced | ENFORCEMENT MECHANISM DECLARATION + EF-INVOCATION-RECORD |
| Exclusion In Effect | EF excluded from Steps 1-7; signal artifacts not accessed at Step 0 |
| Receiving Role | Belief Cartographer (BC) -- Step 1 |

---

### Step 1 -- [BC] Belief Inventory

```
PBI PRODUCTION PROTOCOL
----------------------------------------------------------------------
Input:    Design materials only. Signal artifacts excluded.
Format:   PB-[NN]: ["Today's materials imply that X." No signal
          knowledge.]
Freeze:   PBI frozen at PHASE-HANDOVER-1. No new PB-[NN] entries after
          PHASE-HANDOVER-1 is written. No handle labels in PBI entries.
----------------------------------------------------------------------
```

**PHASE-HANDOVER-1** (inventory entry: BC -> IA):

| Field | Content |
|-------|---------|
| Completing Role | Belief Cartographer (BC) -- Step 1 |
| Step Completed | Step 1 -- Belief Inventory |
| Output Produced | PBI (all PB-[NN] entries frozen) |
| Exclusion In Effect | BC excluded from Steps 2-7; PBI frozen (no additions after this table) |
| Receiving Role | Institutional Archaeologist (IA) -- Step 2 |

---

### Step 2 -- [IA] Handle Ledger

```
HANDLE LEDGER PROTOCOL
----------------------------------------------------------------------
Timing:   After reading all signal artifacts. Before writing corrections.
Format:   HL-[NN]: [finding-specific label -- 2-5 words; finding
          language]
Test:     No PBI entry names its handle. No HL entry echoes a PBI
          entry verbatim. Either violation is a phase contract failure.
----------------------------------------------------------------------
```

**PHASE-HANDOVER-2** (inventory entry: IA Step 2 -> IA Step 3):

| Field | Content |
|-------|---------|
| Completing Role | Institutional Archaeologist (IA) -- Step 2 |
| Step Completed | Step 2 -- Handle Ledger |
| Output Produced | HANDLE LEDGER (all HL-[NN] entries complete) |
| Exclusion In Effect | No new handles may be coined after Step 3 begins |
| Receiving Role | Institutional Archaeologist (IA) -- Step 3 |

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

**PHASE-HANDOVER-3** (inventory entry: IA Step 3 -> IA Step 4):

| Field | Content |
|-------|---------|
| Completing Role | Institutional Archaeologist (IA) -- Step 3 |
| Step Completed | Step 3 -- Draft All Corrections |
| Output Produced | Draft correction entries (all fields populated; pre-audit) |
| Exclusion In Effect | No new entries may be added after Step 4 begins |
| Receiving Role | Institutional Archaeologist (IA) -- Step 4 |

---

### Step 4 -- Register Audit

```
REGISTER AUDIT PROTOCOL
----------------------------------------------------------------------
Execute field by field before Step 5. Rewrite any field in discovery
register: Source (prose -> namespace:skill:artifact), Implies
(narration -> future-team framing), Wrong (softener -> specific wrong
component), Decide (deferral -> blocking decision), Verified
(identifiers -> quoted actual text of both).
----------------------------------------------------------------------
```

**PHASE-HANDOVER-4** (inventory entry: IA Step 4 -> IA Step 5):

| Field | Content |
|-------|---------|
| Completing Role | Institutional Archaeologist (IA) -- Step 4 |
| Step Completed | Step 4 -- Register Audit |
| Output Produced | Audited correction entries (all fields rewritten per protocol) |
| Exclusion In Effect | Field rewrites locked; no further changes outside Step 5 gate |
| Receiving Role | Institutional Archaeologist (IA) -- Step 5 |

---

### Step 5 -- Entry Gate

```
ENTRY GATE DECLARATION
----------------------------------------------------------------------
Purpose:  Per-entry field validation. Format + framing only.
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

**PHASE-HANDOVER-5** (inventory entry: IA Step 5 -> IA Step 6):

| Field | Content |
|-------|---------|
| Completing Role | Institutional Archaeologist (IA) -- Step 5 |
| Step Completed | Step 5 -- Entry Gate |
| Output Produced | Per-entry STATUS: CLEARED tokens (all entries) |
| Exclusion In Effect | No field changes permitted after all entries CLEARED |
| Receiving Role | Institutional Archaeologist (IA) -- Step 6 |

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
Gate:     CHAIN-FLAG IS A HARD GATE.
----------------------------------------------------------------------
```

```
RESOLUTION PROTOCOL DECLARATION
----------------------------------------------------------------------
  PBI-Ref mismatch (element 1):
    Repair:   Replace PBI-Ref with correct identifier.
    Verifier: BELIEF CARTOGRAPHER (BC).

  Handle mismatch (element 2):
    Repair:   Determine authoritative label; propagate from source.
    Verifier: INSTITUTIONAL ARCHAEOLOGIST (IA).

  Source absent (element 3):
    Repair:   Replace with resolvable artifact, or demote with typed
              route reason.
    Verifier: INSTITUTIONAL ARCHAEOLOGIST (IA).

  Verified inaccurate (element 4):
    Repair:   Re-quote actual text from both PBI entry and source.
    Verifier: INSTITUTIONAL ARCHAEOLOGIST (IA).
----------------------------------------------------------------------
```

Do not proceed to Step 7 until every entry CHAIN-COMPLETE.

**PHASE-HANDOVER-6** (inventory entry: IA Step 6 -> IA Step 7):

| Field | Content |
|-------|---------|
| Completing Role | Institutional Archaeologist (IA) -- Step 6 |
| Step Completed | Step 6 -- Chain Integrity Audit |
| Output Produced | Per-entry CHAIN-COMPLETE tokens; Resolution Protocol trace if flagged |
| Exclusion In Effect | No chain repairs permitted after all entries CHAIN-COMPLETE |
| Receiving Role | Institutional Archaeologist (IA) -- Step 7 |

---

### Step 7 -- [IA] Hierarchy, Distillation, and Forward Handover

**Surprise hierarchy:** Ranked by design impact. Argued rationale. Names decision at risk.

**Rules of Thumb:**

```
RULES OF THUMB DECLARATION
----------------------------------------------------------------------
Scope:  HIGH and MEDIUM entries only. LOW excluded.
Format: [TIER] {Rule -- <=20 words} (encodes: {SURPRISE NAME})
Check:  RULES-ANCHORED -- tier annotation must match parent Severity.
Gate:   RULES-ANCHORED BLOCKS on any MISALIGNED rule.
Closure: RULES-ANCHORED-COMPLETE: R-01 "[TIER]" ALIGNED, ... --
         distillation phase closed.
----------------------------------------------------------------------
```

| Tier     | Rule (<=20 words)  | Encodes         |
|----------|--------------------|-----------------|
| [HIGH]   | {rule statement}   | {SURPRISE NAME} |
| [MEDIUM] | {rule statement}   | {SURPRISE NAME} |

RULES-ANCHORED check and closure token.

**Pattern of inherited errors:** 2-4 sentences. Named structural origin or stated absent.

**Blind Spot Map:** Categories as types of wrong thinking. Assign each correction.

**Correction Forward Statement:** 1-3 sentences. Confirms NO-ECHO COST. Names specific
avoided failure. Falsifiable institutional purpose.

**What this correction record excludes:** At least two categories with counts.

---

== ARTIFACT STRUCTURE ============================================================

  1. ENFORCEMENT MECHANISM DECLARATION (EF; NO-ECHO COST)
  2. EF-INVOCATION-RECORD (Step 0)
  3. PHASE-HANDOVER-0 table (EF exit; 5-row schema; inventory entry verified)
  4. PBI output (BC; frozen)
  5. PHASE-HANDOVER-1 table (BC exit; 5-row schema; inventory entry verified)
  6. HANDLE LEDGER output (IA)
  7. PHASE-HANDOVER-2 table (IA Step 2 exit; 5-row schema; inventory entry verified)
  8. Corrections -- HIGH -> MEDIUM -> LOW
  9. PHASE-HANDOVER-3 table (IA Step 3 exit; 5-row schema; inventory entry verified)
  10. Audited corrections (Register Audit output)
  11. PHASE-HANDOVER-4 table (IA Step 4 exit; 5-row schema; inventory entry verified)
  12. Entry Gate blocks (all STATUS: CLEARED)
  13. PHASE-HANDOVER-5 table (IA Step 5 exit; 5-row schema; inventory entry verified)
  14. Chain Integrity Audit (all CHAIN-COMPLETE)
  15. PHASE-HANDOVER-6 table (IA Step 6 exit; 5-row schema; inventory entry verified)
  16. Rules of Thumb (RULES-ANCHORED-COMPLETE)
  17. Surprise hierarchy
  18. Pattern of inherited errors
  19. Blind Spot Map
  20. Correction Forward Statement
  21. What this correction record excludes

Write to: simulations/topic/echo/{topic}-echo-{YYYY-MM-DD}.md

---

## V-03 -- Axis C-prime: MUST-Clause Scope-Field Structure

**Variation axis:** Phrasing register -- STILL-LIVE FILTER written as four MUST-clauses,
each with an explicit Scope: field as a named structural element preceding the Action: field
(Axis C-prime only)

**Hypothesis:** R12 V-03 used "For every X" as an inline sentence opener within each MUST
clause, embedding scope in the action sentence. The scope is readable but requires parsing
the action sentence to find it. If each MUST clause is restructured with a separate "Scope:"
label preceding a separate "Action:" label, the entity class governing each clause is visible
from the label structure before the action is read. A reviewer auditing "which entity class
does MUST-3 govern?" reads the Scope label directly, without reading the action. C-42 is
satisfied because scope declaration is a named structural element independently auditable
from the clause body.

**Expected v13 score:** 230 (C-39 PASS; C-42 PASS; C-37 FAIL; C-40 FAIL; C-38 FAIL;
C-41 FAIL)

---

Topic: `{topic}`

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
Function:     Pre-investigation belief recovery. Read design materials.
              Produce PBI (Prior Belief Inventory). Freeze all entries.
Input:        Design materials only. Signal artifacts out of scope.
Out-of-scope: Signal artifacts. Handle Ledger. Entry authoring.
Phase scope:  Step 1 only. BC excluded from Steps 2-7.
Gate return:  PBI (all PB-[NN] entries frozen) before Step 2 begins.
----------------------------------------------------------------------
```

**Institutional Archaeologist (IA)** -- Steps 2-7.

```
INSTITUTIONAL ARCHAEOLOGIST -- FUNCTION DECLARATION
----------------------------------------------------------------------
Function:     False-assumption recovery. Correction register only.
Input:        Signal artifacts + frozen PBI (read-only).
Out-of-scope: PBI authorship (frozen). Enforcement section (immutable).
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
Reviewer implication: Independence is enforced by role boundary.
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
  [List each pre-investigation source. Minimum one entry.]
Signal artifacts excluded:
  [List each signal artifact; confirm not accessed at Step 0.]
Cost derivation basis:
  [One sentence: which material grounded the NO-ECHO COST claim.]
----------------------------------------------------------------------
```

---

### Step 1 -- [BC] Belief Inventory

```
PBI PRODUCTION PROTOCOL
----------------------------------------------------------------------
Input:    Design materials only. Signal artifacts excluded.
Format:   PB-[NN]: ["Today's materials imply that X." No signal
          knowledge.]
Freeze:   PBI frozen at end of Step 1. BC may not add new PB-[NN]
          entries after this point. No handle labels in PBI entries.
----------------------------------------------------------------------
```

BC is now excluded from Steps 2-7.

---

### Step 2 -- [IA] Handle Ledger

```
HANDLE LEDGER PROTOCOL
----------------------------------------------------------------------
Timing:   After reading all signal artifacts. Before writing corrections.
Format:   HL-[NN]: [finding-specific label -- 2-5 words; finding
          language]
Test:     No PBI entry names its handle. No HL entry echoes a PBI
          entry verbatim. Either violation is a phase contract failure.
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

CORRECTION ENFORCEMENT:
  Rule 1: Correction register only. Discovery narration fails.
  Rule 2: Direct claims in every field. No hedges.
  Rule 3: Each entry self-contained.

Order: HIGH -> MEDIUM -> LOW.
----------------------------------------------------------------------
```

**STILL-LIVE FILTER -- SCOPE-FIELD MUST-CLAUSE PROTOCOL**

Apply to every candidate from the Handle Ledger. All four MUST-clauses apply to every
candidate without exception. No candidate evaluation concludes without completing all four
MUST-clauses for that candidate.

```
STILL-LIVE FILTER PROTOCOL
----------------------------------------------------------------------
MUST-1
  Scope:      EVERY CANDIDATE -- no exceptions.
  Action:     Produce exactly one of:
                STILL-LIVE-[N]: [candidate name]
                DISCARD-[N]:    [candidate name]
  Constraint: No candidate evaluation concludes without one of these
              tokens. Scope is EVERY CANDIDATE; no candidate is exempt.

MUST-2
  Scope:      EVERY DISCARD-[N] TOKEN -- no exceptions.
  Action:     Immediately write:
                DISCARD-[N]-PBI-REF: PB-[NN]
              Names the prior belief this candidate was tested against.
  Constraint: A DISCARD token without a PBI-Ref token is malformed.
              Scope is EVERY DISCARD token; no DISCARD is exempt.

MUST-3
  Scope:      EVERY DISCARD-[N] TOKEN -- no exceptions.
  Action:     Immediately write:
                DISCARD-[N]-ROUTE: [destination -- topic-story or named skill]
              States where excluded candidates are recorded.
  Constraint: A DISCARD token without a ROUTE token is malformed.
              Scope is EVERY DISCARD token; no DISCARD is exempt.

MUST-4
  Scope:      EVERY DISCARD-[N] TOKEN -- no exceptions.
  Action:     Immediately write:
                DISCARD-[N]-REASON: [one sentence -- specific exclusion reason]
              States why this candidate fails the STILL-LIVE test.
  Constraint: A DISCARD token without a REASON token is malformed.
              Scope is EVERY DISCARD token; no DISCARD is exempt.

Completeness gate: After all candidates are processed, write:
  DISCARD-LOG-COMPLETE: [N] STILL-LIVE, [M] DISCARD -- all four
  MUST-clauses applied to every candidate; no candidate unresolved.
----------------------------------------------------------------------
```

---

### Step 4 -- Register Audit

```
REGISTER AUDIT PROTOCOL
----------------------------------------------------------------------
Execute field by field before Step 5. Rewrite any field in discovery
register: Source (prose -> namespace:skill:artifact), Implies
(narration -> future-team framing), Wrong (softener -> specific wrong
component), Decide (deferral -> blocking decision), Verified
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
Gate:     CHAIN-FLAG IS A HARD GATE.
----------------------------------------------------------------------
```

```
RESOLUTION PROTOCOL DECLARATION
----------------------------------------------------------------------
  PBI-Ref mismatch (element 1):
    Repair:   Replace PBI-Ref with correct identifier.
    Verifier: BELIEF CARTOGRAPHER (BC).

  Handle mismatch (element 2):
    Repair:   Determine authoritative label; propagate from source.
    Verifier: INSTITUTIONAL ARCHAEOLOGIST (IA).

  Source absent (element 3):
    Repair:   Replace with resolvable artifact, or demote with typed
              route reason.
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
Check:  RULES-ANCHORED -- tier annotation must match parent Severity.
Gate:   RULES-ANCHORED BLOCKS on any MISALIGNED rule.
Closure: RULES-ANCHORED-COMPLETE: R-01 "[TIER]" ALIGNED, ... --
         distillation phase closed.
----------------------------------------------------------------------
```

| Tier     | Rule (<=20 words)  | Encodes         |
|----------|--------------------|-----------------|
| [HIGH]   | {rule statement}   | {SURPRISE NAME} |
| [MEDIUM] | {rule statement}   | {SURPRISE NAME} |

RULES-ANCHORED check and closure token.

**Pattern of inherited errors:** 2-4 sentences. Named structural origin or stated absent.

**Blind Spot Map:** Categories as types of wrong thinking. Assign each correction.

**Correction Forward Statement:** 1-3 sentences. Confirms NO-ECHO COST. Names specific
avoided failure. Falsifiable institutional purpose.

**What this correction record excludes:** At least two categories with counts.

---

== ARTIFACT STRUCTURE ============================================================

  1. ENFORCEMENT MECHANISM DECLARATION (EF; NO-ECHO COST)
  2. EF-INVOCATION-RECORD (Step 0)
  3. PBI output (BC; frozen)
  4. HANDLE LEDGER output (IA)
  5. STILL-LIVE FILTER output: STILL-LIVE-[N] and DISCARD-[N] tokens; each DISCARD
     followed immediately by PBI-REF / ROUTE / REASON tokens; DISCARD-LOG-COMPLETE
  6. Corrections -- HIGH -> MEDIUM -> LOW
  7. Entry Gate blocks (all STATUS: CLEARED)
  8. Chain Integrity Audit (all CHAIN-COMPLETE)
  9. Resolution Protocol trace (verifier named per flag type)
  10. Rules of Thumb (RULES-ANCHORED-COMPLETE)
  11. Surprise hierarchy
  12. Pattern of inherited errors
  13. Blind Spot Map
  14. Correction Forward Statement
  15. What this correction record excludes

Write to: simulations/topic/echo/{topic}-echo-{YYYY-MM-DD}.md

---

## V-04 -- Axes A-prime+B-prime: Standalone Protocol Section + Inventory

**Variation axes:** Lifecycle emphasis (Axis A-prime) + Output format (Axis B-prime)

**Hypothesis:** Combining the standalone BC-STEP1-PROTOCOL section (Axis A-prime) with the
PHASE-HANDOVER-INVENTORY pre-declaration plus inline universal tables (Axis B-prime) produces
additive auditability. BC's sub-phase decomposition is declared as a first-class document
section before any step begins (C-40). All seven phase transitions are simultaneously
verifiable from the inventory reference and the inline tables (C-41). The two mechanisms
target different phases and are structurally independent: Axis A-prime modifies document
structure before Step 0; Axis B-prime modifies stage-exit tokens in Steps 0-6. The STILL-LIVE
FILTER remains without scope-field structure (Axis C-prime absent), so C-39 fails (no MUST
clause protocol) and C-42 fails.

**Expected v13 score:** 240 (C-37 PASS; C-40 PASS; C-38 PASS; C-41 PASS; C-39 FAIL;
C-42 FAIL)

---

Topic: `{topic}`

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
Out-of-scope: PBI production. Entry authoring. Chain verification.
Phase scope:  Step 0 only. EF excluded from Steps 1-7.
Gate return:  ENFORCEMENT MECHANISM section + EF-INVOCATION-RECORD +
              PHASE-HANDOVER-0 table before proceeding to Step 1.
----------------------------------------------------------------------
```

**Belief Cartographer (BC)** -- Step 1 exclusively; three sub-phases declared in the
BC-STEP1-PROTOCOL section below.

```
BELIEF CARTOGRAPHER -- FUNCTION DECLARATION
----------------------------------------------------------------------
Function:     Pre-investigation belief recovery. Execute Step 1 in the
              three sequential sub-phases declared in the BC-STEP1-
              PROTOCOL section below. Do not merge sub-phases. Write
              each gate token before advancing to the next sub-phase.
Input:        Design materials only. Signal artifacts out of scope.
Out-of-scope: Signal artifacts. Handle Ledger. Entry authoring.
Phase scope:  Step 1 only. BC excluded from Steps 2-7 after the
              [COVERAGE AUDIT] gate token is written.
Gate return:  PBI (all PB-[NN] entries frozen) + BC-COVERAGE-RECORD
              + PHASE-HANDOVER-1 table before Step 2 begins.
----------------------------------------------------------------------
```

**Institutional Archaeologist (IA)** -- Steps 2-7.

```
INSTITUTIONAL ARCHAEOLOGIST -- FUNCTION DECLARATION
----------------------------------------------------------------------
Function:     False-assumption recovery. Correction register only.
              Each IA stage exit (Steps 2-6) produces a PHASE-HANDOVER-[N]
              table before advancing to the next step.
Input:        Signal artifacts + frozen PBI (read-only).
Out-of-scope: PBI authorship (frozen). Enforcement section (immutable).
Orienting:    "What would the next team build wrong?"
Phase scope:  Steps 2-7 only.
----------------------------------------------------------------------
```

**Phase Handover Schema (universal -- all 7 exits, Steps 0-6):**

All PHASE-HANDOVER-[N] tables use this schema exactly. Five rows. Fixed field names.

| Field | Content |
|-------|---------|
| Completing Role | [role name and step number] |
| Step Completed | [step number and name] |
| Output Produced | [artifact(s) produced at this exit] |
| Exclusion In Effect | [what the completing role/phase can no longer modify] |
| Receiving Role | [role name and step number taking control] |

---

### BC-STEP1-PROTOCOL

Executed by BC during Step 1 in three sequential sub-phases. Write each gate token before
advancing to the next sub-phase. Do not merge sub-phases. This section is the pre-execution
contract for Step 1, positioned before Step 0 begins. The BC Function Declaration references
this section by name only.

| Sub-phase | Scope | Gate Token |
|-----------|-------|------------|
| [SCAN] | Read design materials. List all belief candidates. No pruning or evaluation during this phase. | `COMMIT-SCAN: [N] candidates identified.` |
| [FREEZE] | Produce PBI from scan results. Lock all PB-[NN] entries. No additions after gate token. | `COMMIT-FREEZE: PBI frozen at [N] entries.` |
| [COVERAGE AUDIT] | Audit domain coverage. Produce BC-COVERAGE-RECORD (schema below). BC exclusion takes effect after this gate token is written. | BC-COVERAGE-RECORD (schema below). |

BC-COVERAGE-RECORD schema:

```
BC-COVERAGE-RECORD
----------------------------------------------------------------------
Sub-phase:  [COVERAGE AUDIT] -- gate token declared in BC-STEP1-PROTOCOL.
Materials consulted (pre-investigation only):
  [List each design document scanned during [SCAN] and [FREEZE].
   Minimum one entry.]
Signal artifacts excluded:
  [List each signal artifact; confirm not accessed during Step 1.]
PBI completeness basis:
  [One sentence: which material(s) provide the primary PBI basis.]
----------------------------------------------------------------------
```

---

### PHASE-HANDOVER-INVENTORY

Pre-declared registry of all seven phase transitions. Every step exit in Steps 0 through 6
produces a PHASE-HANDOVER-[N] table matching this inventory. Cross-reference this inventory
against the inline tables to verify universality without traversal.

| Transition | Step Completed | Completing Role | Receiving Role |
|------------|----------------|-----------------|----------------|
| PHASE-HANDOVER-0 | Step 0 -- Enforcement Section and Invocation Record | Enforcement Framer (EF) | Belief Cartographer (BC) |
| PHASE-HANDOVER-1 | Step 1 -- Belief Inventory and Coverage Audit | Belief Cartographer (BC) | Institutional Archaeologist (IA) |
| PHASE-HANDOVER-2 | Step 2 -- Handle Ledger | Institutional Archaeologist (IA) | Institutional Archaeologist (IA) |
| PHASE-HANDOVER-3 | Step 3 -- Draft All Corrections | Institutional Archaeologist (IA) | Institutional Archaeologist (IA) |
| PHASE-HANDOVER-4 | Step 4 -- Register Audit | Institutional Archaeologist (IA) | Institutional Archaeologist (IA) |
| PHASE-HANDOVER-5 | Step 5 -- Entry Gate | Institutional Archaeologist (IA) | Institutional Archaeologist (IA) |
| PHASE-HANDOVER-6 | Step 6 -- Chain Integrity Audit | Institutional Archaeologist (IA) | Institutional Archaeologist (IA) |

---

### Step 0 -- [EF] Enforcement Section and Invocation Record

```
ENFORCEMENT MECHANISM DECLARATION
----------------------------------------------------------------------
Provenance tier: STRUCTURAL
Distinguishing property: Role-scope exclusion at three phase boundaries.
  EF writes the cost declaration before signals are read -- cost claim
  is prospective. BC writes PBI before signals are read. IA writes
  corrections from signals and cannot alter the frozen PBI or
  enforcement section. Role boundary is the enforcement mechanism.
Reviewer implication: Independence is enforced by role boundary.
NO-ECHO COST: [EF derives from design materials -- named failure class
  required. Generic statements fail.]
----------------------------------------------------------------------
```

```
EF-INVOCATION-RECORD
----------------------------------------------------------------------
Step:       0 (EF phase; signal-reading phase not yet open)
Materials consulted (pre-investigation only):
  [List each pre-investigation source. Minimum one entry.]
Signal artifacts excluded:
  [List each signal artifact; confirm not accessed at Step 0.]
Cost derivation basis:
  [One sentence: which material grounded the NO-ECHO COST claim.]
----------------------------------------------------------------------
```

**PHASE-HANDOVER-0** (inventory entry: EF -> BC):

| Field | Content |
|-------|---------|
| Completing Role | Enforcement Framer (EF) -- Step 0 |
| Step Completed | Step 0 -- Enforcement Section and Invocation Record |
| Output Produced | ENFORCEMENT MECHANISM DECLARATION + EF-INVOCATION-RECORD |
| Exclusion In Effect | EF excluded from Steps 1-7; signal artifacts not accessed at Step 0 |
| Receiving Role | Belief Cartographer (BC) -- Step 1 |

---

### Step 1 -- [BC] Belief Inventory and Coverage Audit

Execute BC-STEP1-PROTOCOL as declared in the BC-STEP1-PROTOCOL section above. Write each
gate token before advancing.

**[SCAN]** Read all design materials within BC's input scope. Signal artifacts out of scope.
Identify every belief candidate. List all candidates before moving to [FREEZE].

`COMMIT-SCAN: [N] candidates identified.`

**[FREEZE]** Produce the PBI from the scanned candidates.

```
PBI PRODUCTION PROTOCOL
----------------------------------------------------------------------
Input:    Design materials only. Signal artifacts excluded.
Format:   PB-[NN]: ["Today's materials imply that X." No signal
          knowledge.]
Freeze:   PBI frozen after COMMIT-FREEZE. No new PB-[NN] after this
          point. No handle labels in PBI entries.
----------------------------------------------------------------------
```

`COMMIT-FREEZE: PBI frozen at [N] entries.`

**[COVERAGE AUDIT]** After PBI freeze, produce BC-COVERAGE-RECORD using the schema declared
in the BC-STEP1-PROTOCOL section above.

BC is now excluded from Steps 2-7.

**PHASE-HANDOVER-1** (inventory entry: BC -> IA):

| Field | Content |
|-------|---------|
| Completing Role | Belief Cartographer (BC) -- Step 1 |
| Step Completed | Step 1 -- Belief Inventory and Coverage Audit |
| Output Produced | PBI (all PB-[NN] frozen) + BC-COVERAGE-RECORD ([COVERAGE AUDIT] gate) |
| Exclusion In Effect | BC excluded from Steps 2-7; PBI frozen; no additions after this table |
| Receiving Role | Institutional Archaeologist (IA) -- Step 2 |

---

### Step 2 -- [IA] Handle Ledger

```
HANDLE LEDGER PROTOCOL
----------------------------------------------------------------------
Timing:   After reading all signal artifacts. Before writing corrections.
Format:   HL-[NN]: [finding-specific label -- 2-5 words; finding
          language]
Test:     No PBI entry names its handle. No HL entry echoes a PBI
          entry verbatim. Either violation is a phase contract failure.
----------------------------------------------------------------------
```

**PHASE-HANDOVER-2** (inventory entry: IA Step 2 -> IA Step 3):

| Field | Content |
|-------|---------|
| Completing Role | Institutional Archaeologist (IA) -- Step 2 |
| Step Completed | Step 2 -- Handle Ledger |
| Output Produced | HANDLE LEDGER (all HL-[NN] entries complete) |
| Exclusion In Effect | No new handles may be coined after Step 3 begins |
| Receiving Role | Institutional Archaeologist (IA) -- Step 3 |

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

**PHASE-HANDOVER-3** (inventory entry: IA Step 3 -> IA Step 4):

| Field | Content |
|-------|---------|
| Completing Role | Institutional Archaeologist (IA) -- Step 3 |
| Step Completed | Step 3 -- Draft All Corrections |
| Output Produced | Draft correction entries (all fields populated; pre-audit) |
| Exclusion In Effect | No new entries may be added after Step 4 begins |
| Receiving Role | Institutional Archaeologist (IA) -- Step 4 |

---

### Step 4 -- Register Audit

```
REGISTER AUDIT PROTOCOL
----------------------------------------------------------------------
Execute field by field before Step 5. Rewrite any field in discovery
register: Source (prose -> namespace:skill:artifact), Implies
(narration -> future-team framing), Wrong (softener -> specific wrong
component), Decide (deferral -> blocking decision), Verified
(identifiers -> quoted actual text of both).
----------------------------------------------------------------------
```

**PHASE-HANDOVER-4** (inventory entry: IA Step 4 -> IA Step 5):

| Field | Content |
|-------|---------|
| Completing Role | Institutional Archaeologist (IA) -- Step 4 |
| Step Completed | Step 4 -- Register Audit |
| Output Produced | Audited correction entries (all fields rewritten per protocol) |
| Exclusion In Effect | Field rewrites locked; no further changes outside Step 5 gate |
| Receiving Role | Institutional Archaeologist (IA) -- Step 5 |

---

### Step 5 -- Entry Gate

```
ENTRY GATE DECLARATION
----------------------------------------------------------------------
Purpose:  Per-entry field validation. Format + framing only.
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

**PHASE-HANDOVER-5** (inventory entry: IA Step 5 -> IA Step 6):

| Field | Content |
|-------|---------|
| Completing Role | Institutional Archaeologist (IA) -- Step 5 |
| Step Completed | Step 5 -- Entry Gate |
| Output Produced | Per-entry STATUS: CLEARED tokens (all entries) |
| Exclusion In Effect | No field changes permitted after all entries CLEARED |
| Receiving Role | Institutional Archaeologist (IA) -- Step 6 |

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
Gate:     CHAIN-FLAG IS A HARD GATE.
----------------------------------------------------------------------
```

```
RESOLUTION PROTOCOL DECLARATION
----------------------------------------------------------------------
  PBI-Ref mismatch (element 1):
    Repair:   Replace PBI-Ref with correct identifier.
    Verifier: BELIEF CARTOGRAPHER (BC).

  Handle mismatch (element 2):
    Repair:   Determine authoritative label; propagate from source.
    Verifier: INSTITUTIONAL ARCHAEOLOGIST (IA).

  Source absent (element 3):
    Repair:   Replace with resolvable artifact, or demote with typed
              route reason.
    Verifier: INSTITUTIONAL ARCHAEOLOGIST (IA).

  Verified inaccurate (element 4):
    Repair:   Re-quote actual text from both PBI entry and source.
    Verifier: INSTITUTIONAL ARCHAEOLOGIST (IA).
----------------------------------------------------------------------
```

Do not proceed to Step 7 until every entry CHAIN-COMPLETE.

**PHASE-HANDOVER-6** (inventory entry: IA Step 6 -> IA Step 7):

| Field | Content |
|-------|---------|
| Completing Role | Institutional Archaeologist (IA) -- Step 6 |
| Step Completed | Step 6 -- Chain Integrity Audit |
| Output Produced | Per-entry CHAIN-COMPLETE tokens; Resolution Protocol trace if flagged |
| Exclusion In Effect | No chain repairs permitted after all entries CHAIN-COMPLETE |
| Receiving Role | Institutional Archaeologist (IA) -- Step 7 |

---

### Step 7 -- [IA] Hierarchy, Distillation, and Forward Handover

**Surprise hierarchy:** Ranked by design impact. Argued rationale. Names decision at risk.

**Rules of Thumb:**

```
RULES OF THUMB DECLARATION
----------------------------------------------------------------------
Scope:  HIGH and MEDIUM entries only. LOW excluded.
Format: [TIER] {Rule -- <=20 words} (encodes: {SURPRISE NAME})
Check:  RULES-ANCHORED -- tier annotation must match parent Severity.
Gate:   RULES-ANCHORED BLOCKS on any MISALIGNED rule.
Closure: RULES-ANCHORED-COMPLETE: R-01 "[TIER]" ALIGNED, ... --
         distillation phase closed.
----------------------------------------------------------------------
```

| Tier     | Rule (<=20 words)  | Encodes         |
|----------|--------------------|-----------------|
| [HIGH]   | {rule statement}   | {SURPRISE NAME} |
| [MEDIUM] | {rule statement}   | {SURPRISE NAME} |

RULES-ANCHORED check and closure token.

**Pattern of inherited errors:** 2-4 sentences. Named structural origin or stated absent.

**Blind Spot Map:** Categories as types of wrong thinking. Assign each correction.

**Correction Forward Statement:** 1-3 sentences. Confirms NO-ECHO COST. Falsifiable.

**What this correction record excludes:** At least two categories with counts.

---

== ARTIFACT STRUCTURE ============================================================

  1. ENFORCEMENT MECHANISM DECLARATION (EF; NO-ECHO COST)
  2. EF-INVOCATION-RECORD (Step 0)
  3. PHASE-HANDOVER-0 table (EF exit; 5-row schema; inventory entry verified)
  4. PBI output (BC; COMMIT-SCAN + COMMIT-FREEZE tokens)
  5. BC-COVERAGE-RECORD ([COVERAGE AUDIT] gate; schema from BC-STEP1-PROTOCOL section)
  6. PHASE-HANDOVER-1 table (BC exit; 5-row schema; inventory entry verified)
  7. HANDLE LEDGER output (IA)
  8. PHASE-HANDOVER-2 table (IA Step 2 exit; 5-row schema; inventory entry verified)
  9. Corrections -- HIGH -> MEDIUM -> LOW
  10. PHASE-HANDOVER-3 table (IA Step 3 exit; 5-row schema; inventory entry verified)
  11. Audited corrections (Register Audit output)
  12. PHASE-HANDOVER-4 table (IA Step 4 exit; 5-row schema; inventory entry verified)
  13. Entry Gate blocks (all STATUS: CLEARED)
  14. PHASE-HANDOVER-5 table (IA Step 5 exit; 5-row schema; inventory entry verified)
  15. Chain Integrity Audit (all CHAIN-COMPLETE)
  16. PHASE-HANDOVER-6 table (IA Step 6 exit; 5-row schema; inventory entry verified)
  17. Rules of Thumb (RULES-ANCHORED-COMPLETE)
  18. Surprise hierarchy
  19. Pattern of inherited errors
  20. Blind Spot Map
  21. Correction Forward Statement
  22. What this correction record excludes

Write to: simulations/topic/echo/{topic}-echo-{YYYY-MM-DD}.md

---

## V-05 -- Axes A-prime+B-prime+C-prime: Full Alternative Combination

**Variation axes:** Lifecycle emphasis (Axis A-prime) + Output format (Axis B-prime) +
Phrasing register (Axis C-prime)

**Hypothesis:** Combining all three R13 axes produces the maximum-scoring variant through
alternative structural implementations. The standalone BC-STEP1-PROTOCOL section (Axis
A-prime) satisfies C-37 (sub-phase decomposition present) and C-40 (positionally legible
from section header -- no code block entry required). The PHASE-HANDOVER-INVENTORY plus
inline universal tables (Axis B-prime) satisfies C-38 (5-row schema format) and C-41
(universality simultaneously verifiable by cross-referencing inventory against inline tables).
The scope-field MUST-clause protocol (Axis C-prime) satisfies C-39 (unconditional imperatives)
and C-42 (scope declared as a named structural field, readable from label without parsing
the action sentence). All three mechanisms target different phases and are structurally
independent. V-05 is the only R13 variation predicted to achieve 260/260 under v13.

**Expected v13 score:** 260 (C-37 PASS; C-38 PASS; C-39 PASS; C-40 PASS; C-41 PASS;
C-42 PASS)

---

Topic: `{topic}`

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
Out-of-scope: PBI production. Entry authoring. Chain verification.
Phase scope:  Step 0 only. EF excluded from Steps 1-7.
Gate return:  ENFORCEMENT MECHANISM section + EF-INVOCATION-RECORD +
              PHASE-HANDOVER-0 table before proceeding to Step 1.
----------------------------------------------------------------------
```

**Belief Cartographer (BC)** -- Step 1 exclusively; three sub-phases declared in the
BC-STEP1-PROTOCOL section below.

```
BELIEF CARTOGRAPHER -- FUNCTION DECLARATION
----------------------------------------------------------------------
Function:     Pre-investigation belief recovery. Execute Step 1 in the
              three sequential sub-phases declared in the BC-STEP1-
              PROTOCOL section below. Do not merge sub-phases. Write
              each gate token before advancing to the next sub-phase.
Input:        Design materials only. Signal artifacts out of scope.
Out-of-scope: Signal artifacts. Handle Ledger. Entry authoring.
Phase scope:  Step 1 only. BC excluded from Steps 2-7 after the
              [COVERAGE AUDIT] gate token is written.
Gate return:  PBI (all PB-[NN] entries frozen) + BC-COVERAGE-RECORD
              + PHASE-HANDOVER-1 table before Step 2 begins.
----------------------------------------------------------------------
```

**Institutional Archaeologist (IA)** -- Steps 2-7.

```
INSTITUTIONAL ARCHAEOLOGIST -- FUNCTION DECLARATION
----------------------------------------------------------------------
Function:     False-assumption recovery. Correction register only.
              Each IA stage exit (Steps 2-6) produces a PHASE-HANDOVER-[N]
              table before advancing to the next step.
Input:        Signal artifacts + frozen PBI (read-only).
Out-of-scope: PBI authorship (frozen). Enforcement section (immutable).
Orienting:    "What would the next team build wrong?"
Phase scope:  Steps 2-7 only.
----------------------------------------------------------------------
```

**Phase Handover Schema (universal -- all 7 exits, Steps 0-6):**

All PHASE-HANDOVER-[N] tables use this schema exactly. Five rows. Fixed field names.
Do not substitute prose. Do not add or remove rows.

| Field | Content |
|-------|---------|
| Completing Role | [role name and step number] |
| Step Completed | [step number and name] |
| Output Produced | [artifact(s) produced at this exit] |
| Exclusion In Effect | [what the completing role/phase can no longer modify] |
| Receiving Role | [role name and step number taking control] |

---

### BC-STEP1-PROTOCOL

Executed by BC during Step 1 in three sequential sub-phases. Write each gate token before
advancing to the next sub-phase. Do not merge sub-phases. This section is the pre-execution
contract for Step 1. It is positioned before Step 0 begins -- Step 1 executes against this
declaration. The BC Function Declaration references this section by name only; the full
protocol specification is here, not inside the BC code block.

| Sub-phase | Scope | Gate Token |
|-----------|-------|------------|
| [SCAN] | Read design materials. List all belief candidates. No pruning or evaluation during this phase. | `COMMIT-SCAN: [N] candidates identified.` |
| [FREEZE] | Produce PBI from scan results. Lock all PB-[NN] entries. No additions after gate token. | `COMMIT-FREEZE: PBI frozen at [N] entries.` |
| [COVERAGE AUDIT] | Audit domain coverage. Produce BC-COVERAGE-RECORD (schema below). BC exclusion takes effect after this gate token is written. | BC-COVERAGE-RECORD (schema below). |

BC-COVERAGE-RECORD schema:

```
BC-COVERAGE-RECORD
----------------------------------------------------------------------
Sub-phase:  [COVERAGE AUDIT] -- gate token declared in BC-STEP1-PROTOCOL.
Materials consulted (pre-investigation only):
  [List each design document scanned during [SCAN] and [FREEZE].
   Minimum one entry.]
Signal artifacts excluded:
  [List each signal artifact; confirm not accessed during Step 1.]
PBI completeness basis:
  [One sentence: which material(s) provide the primary PBI basis.]
----------------------------------------------------------------------
```

---

### PHASE-HANDOVER-INVENTORY

Pre-declared registry of all seven phase transitions. Every step exit in Steps 0 through 6
produces a PHASE-HANDOVER-[N] table matching this inventory. Cross-reference this inventory
against the inline tables to verify universality simultaneously, without document traversal.

| Transition | Step Completed | Completing Role | Receiving Role |
|------------|----------------|-----------------|----------------|
| PHASE-HANDOVER-0 | Step 0 -- Enforcement Section and Invocation Record | Enforcement Framer (EF) | Belief Cartographer (BC) |
| PHASE-HANDOVER-1 | Step 1 -- Belief Inventory and Coverage Audit | Belief Cartographer (BC) | Institutional Archaeologist (IA) |
| PHASE-HANDOVER-2 | Step 2 -- Handle Ledger | Institutional Archaeologist (IA) | Institutional Archaeologist (IA) |
| PHASE-HANDOVER-3 | Step 3 -- Draft All Corrections | Institutional Archaeologist (IA) | Institutional Archaeologist (IA) |
| PHASE-HANDOVER-4 | Step 4 -- Register Audit | Institutional Archaeologist (IA) | Institutional Archaeologist (IA) |
| PHASE-HANDOVER-5 | Step 5 -- Entry Gate | Institutional Archaeologist (IA) | Institutional Archaeologist (IA) |
| PHASE-HANDOVER-6 | Step 6 -- Chain Integrity Audit | Institutional Archaeologist (IA) | Institutional Archaeologist (IA) |

---

### Step 0 -- [EF] Enforcement Section and Invocation Record

```
ENFORCEMENT MECHANISM DECLARATION
----------------------------------------------------------------------
Provenance tier: STRUCTURAL
Distinguishing property: Role-scope exclusion at three phase boundaries.
  EF writes the cost declaration before signals are read -- cost claim
  is prospective. BC writes PBI before signals are read. IA writes
  corrections from signals and cannot alter the frozen PBI or
  enforcement section. Role boundary is the enforcement mechanism.
Reviewer implication: Independence is enforced by role boundary.
NO-ECHO COST: [EF derives from design materials -- named failure class
  required. Generic statements fail.]
----------------------------------------------------------------------
```

```
EF-INVOCATION-RECORD
----------------------------------------------------------------------
Step:       0 (EF phase; signal-reading phase not yet open)
Materials consulted (pre-investigation only):
  [List each pre-investigation source. Minimum one entry.]
Signal artifacts excluded:
  [List each signal artifact; confirm not accessed at Step 0.]
Cost derivation basis:
  [One sentence: which material grounded the NO-ECHO COST claim.]
----------------------------------------------------------------------
```

**PHASE-HANDOVER-0** (inventory entry: EF -> BC):

| Field | Content |
|-------|---------|
| Completing Role | Enforcement Framer (EF) -- Step 0 |
| Step Completed | Step 0 -- Enforcement Section and Invocation Record |
| Output Produced | ENFORCEMENT MECHANISM DECLARATION + EF-INVOCATION-RECORD |
| Exclusion In Effect | EF excluded from Steps 1-7; signal artifacts not accessed at Step 0 |
| Receiving Role | Belief Cartographer (BC) -- Step 1 |

---

### Step 1 -- [BC] Belief Inventory and Coverage Audit

Execute BC-STEP1-PROTOCOL as declared in the BC-STEP1-PROTOCOL section above. Write each
gate token before advancing.

**[SCAN]** Read all design materials within BC's input scope. Signal artifacts out of scope.
Identify every belief candidate. List all candidates before moving to [FREEZE].

`COMMIT-SCAN: [N] candidates identified.`

**[FREEZE]** Produce the PBI from the scanned candidates.

```
PBI PRODUCTION PROTOCOL
----------------------------------------------------------------------
Input:    Design materials only. Signal artifacts excluded.
Format:   PB-[NN]: ["Today's materials imply that X." No signal
          knowledge.]
Freeze:   PBI frozen after COMMIT-FREEZE. No new PB-[NN] after this
          point. No handle labels in PBI entries.
----------------------------------------------------------------------
```

`COMMIT-FREEZE: PBI frozen at [N] entries.`

**[COVERAGE AUDIT]** After PBI freeze, produce BC-COVERAGE-RECORD using the schema declared
in the BC-STEP1-PROTOCOL section above.

BC is now excluded from Steps 2-7.

**PHASE-HANDOVER-1** (inventory entry: BC -> IA):

| Field | Content |
|-------|---------|
| Completing Role | Belief Cartographer (BC) -- Step 1 |
| Step Completed | Step 1 -- Belief Inventory and Coverage Audit |
| Output Produced | PBI (all PB-[NN] frozen) + BC-COVERAGE-RECORD ([COVERAGE AUDIT] gate) |
| Exclusion In Effect | BC excluded from Steps 2-7; PBI frozen; no additions after this table |
| Receiving Role | Institutional Archaeologist (IA) -- Step 2 |

---

### Step 2 -- [IA] Handle Ledger

```
HANDLE LEDGER PROTOCOL
----------------------------------------------------------------------
Timing:   After reading all signal artifacts. Before writing corrections.
Format:   HL-[NN]: [finding-specific label -- 2-5 words; finding
          language]
Test:     No PBI entry names its handle. No HL entry echoes a PBI
          entry verbatim. Either violation is a phase contract failure.
----------------------------------------------------------------------
```

**PHASE-HANDOVER-2** (inventory entry: IA Step 2 -> IA Step 3):

| Field | Content |
|-------|---------|
| Completing Role | Institutional Archaeologist (IA) -- Step 2 |
| Step Completed | Step 2 -- Handle Ledger |
| Output Produced | HANDLE LEDGER (all HL-[NN] entries complete) |
| Exclusion In Effect | No new handles may be coined after Step 3 begins |
| Receiving Role | Institutional Archaeologist (IA) -- Step 3 |

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

CORRECTION ENFORCEMENT:
  Rule 1: Correction register only. Discovery narration fails.
  Rule 2: Direct claims in every field. No hedges.
  Rule 3: Each entry self-contained.

Order: HIGH -> MEDIUM -> LOW.
----------------------------------------------------------------------
```

**STILL-LIVE FILTER -- SCOPE-FIELD MUST-CLAUSE PROTOCOL**

Apply to every candidate from the Handle Ledger. All four MUST-clauses apply to every
candidate without exception. No candidate evaluation concludes without completing all four
MUST-clauses for that candidate.

```
STILL-LIVE FILTER PROTOCOL
----------------------------------------------------------------------
MUST-1
  Scope:      EVERY CANDIDATE -- no exceptions.
  Action:     Produce exactly one of:
                STILL-LIVE-[N]: [candidate name]
                DISCARD-[N]:    [candidate name]
  Constraint: No candidate evaluation concludes without one of these
              tokens. Scope is EVERY CANDIDATE; no candidate is exempt.

MUST-2
  Scope:      EVERY DISCARD-[N] TOKEN -- no exceptions.
  Action:     Immediately write:
                DISCARD-[N]-PBI-REF: PB-[NN]
              Names the prior belief this candidate was tested against.
  Constraint: A DISCARD token without a PBI-Ref token is malformed.
              Scope is EVERY DISCARD token; no DISCARD is exempt.

MUST-3
  Scope:      EVERY DISCARD-[N] TOKEN -- no exceptions.
  Action:     Immediately write:
                DISCARD-[N]-ROUTE: [destination -- topic-story or named skill]
              States where excluded candidates are recorded.
  Constraint: A DISCARD token without a ROUTE token is malformed.
              Scope is EVERY DISCARD token; no DISCARD is exempt.

MUST-4
  Scope:      EVERY DISCARD-[N] TOKEN -- no exceptions.
  Action:     Immediately write:
                DISCARD-[N]-REASON: [one sentence -- specific exclusion reason]
              States why this candidate fails the STILL-LIVE test.
  Constraint: A DISCARD token without a REASON token is malformed.
              Scope is EVERY DISCARD token; no DISCARD is exempt.

Completeness gate: After all candidates are processed, write:
  DISCARD-LOG-COMPLETE: [N] STILL-LIVE, [M] DISCARD -- all four
  MUST-clauses applied to every candidate; no candidate unresolved.
----------------------------------------------------------------------
```

**PHASE-HANDOVER-3** (inventory entry: IA Step 3 -> IA Step 4):

| Field | Content |
|-------|---------|
| Completing Role | Institutional Archaeologist (IA) -- Step 3 |
| Step Completed | Step 3 -- Draft All Corrections |
| Output Produced | Draft corrections + STILL-LIVE FILTER output (DISCARD-LOG-COMPLETE) |
| Exclusion In Effect | No new entries or DISCARD tokens may be added after Step 4 begins |
| Receiving Role | Institutional Archaeologist (IA) -- Step 4 |

---

### Step 4 -- Register Audit

```
REGISTER AUDIT PROTOCOL
----------------------------------------------------------------------
Execute field by field before Step 5. Rewrite any field in discovery
register: Source (prose -> namespace:skill:artifact), Implies
(narration -> future-team framing), Wrong (softener -> specific wrong
component), Decide (deferral -> blocking decision), Verified
(identifiers -> quoted actual text of both).
----------------------------------------------------------------------
```

**PHASE-HANDOVER-4** (inventory entry: IA Step 4 -> IA Step 5):

| Field | Content |
|-------|---------|
| Completing Role | Institutional Archaeologist (IA) -- Step 4 |
| Step Completed | Step 4 -- Register Audit |
| Output Produced | Audited correction entries (all fields rewritten per protocol) |
| Exclusion In Effect | Field rewrites locked; no further changes outside Step 5 gate |
| Receiving Role | Institutional Archaeologist (IA) -- Step 5 |

---

### Step 5 -- Entry Gate

```
ENTRY GATE DECLARATION
----------------------------------------------------------------------
Purpose:  Per-entry field validation. Format + framing only.
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

**PHASE-HANDOVER-5** (inventory entry: IA Step 5 -> IA Step 6):

| Field | Content |
|-------|---------|
| Completing Role | Institutional Archaeologist (IA) -- Step 5 |
| Step Completed | Step 5 -- Entry Gate |
| Output Produced | Per-entry STATUS: CLEARED tokens (all entries) |
| Exclusion In Effect | No field changes permitted after all entries CLEARED |
| Receiving Role | Institutional Archaeologist (IA) -- Step 6 |

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
Gate:     CHAIN-FLAG IS A HARD GATE.
----------------------------------------------------------------------
```

```
RESOLUTION PROTOCOL DECLARATION
----------------------------------------------------------------------
  PBI-Ref mismatch (element 1):
    Repair:   Replace PBI-Ref with correct identifier.
    Verifier: BELIEF CARTOGRAPHER (BC).

  Handle mismatch (element 2):
    Repair:   Determine authoritative label; propagate from source.
    Verifier: INSTITUTIONAL ARCHAEOLOGIST (IA).

  Source absent (element 3):
    Repair:   Replace with resolvable artifact, or demote with typed
              route reason.
    Verifier: INSTITUTIONAL ARCHAEOLOGIST (IA).

  Verified inaccurate (element 4):
    Repair:   Re-quote actual text from both PBI entry and source.
    Verifier: INSTITUTIONAL ARCHAEOLOGIST (IA).
----------------------------------------------------------------------
```

Do not proceed to Step 7 until every entry CHAIN-COMPLETE.

**PHASE-HANDOVER-6** (inventory entry: IA Step 6 -> IA Step 7):

| Field | Content |
|-------|---------|
| Completing Role | Institutional Archaeologist (IA) -- Step 6 |
| Step Completed | Step 6 -- Chain Integrity Audit |
| Output Produced | Per-entry CHAIN-COMPLETE tokens; Resolution Protocol trace if flagged |
| Exclusion In Effect | No chain repairs permitted after all entries CHAIN-COMPLETE |
| Receiving Role | Institutional Archaeologist (IA) -- Step 7 |

---

### Step 7 -- [IA] Hierarchy, Distillation, and Forward Handover

**Surprise hierarchy:** Ranked by design impact. Argued rationale. Names decision at risk.

**Rules of Thumb:**

```
RULES OF THUMB DECLARATION
----------------------------------------------------------------------
Scope:  HIGH and MEDIUM entries only. LOW excluded.
Format: [TIER] {Rule -- <=20 words} (encodes: {SURPRISE NAME})
Check:  RULES-ANCHORED -- tier annotation must match parent Severity.
Gate:   RULES-ANCHORED BLOCKS on any MISALIGNED rule.
Closure: RULES-ANCHORED-COMPLETE: R-01 "[TIER]" ALIGNED, ... --
         distillation phase closed.
----------------------------------------------------------------------
```

| Tier     | Rule (<=20 words)  | Encodes         |
|----------|--------------------|-----------------|
| [HIGH]   | {rule statement}   | {SURPRISE NAME} |
| [MEDIUM] | {rule statement}   | {SURPRISE NAME} |

RULES-ANCHORED check and closure token.

**Pattern of inherited errors:** 2-4 sentences. Named structural origin or stated absent.
Non-derivable from tallying individual corrections.

**Blind Spot Map:** Categories as types of wrong thinking specific to this artifact.
Assign each correction. Synthesis non-derivable from individual corrections.

**Correction Forward Statement:** 1-3 sentences. Name the specific failure this artifact
prevented. Identify the false assumption the next team would have inherited. Confirm EF's
NO-ECHO COST. Make the institutional purpose falsifiable.

**What this correction record excludes:** At least two categories with counts.

---

== ARTIFACT STRUCTURE ============================================================

  1. ENFORCEMENT MECHANISM DECLARATION (EF; NO-ECHO COST)
  2. EF-INVOCATION-RECORD (Step 0)
  3. PHASE-HANDOVER-0 table (EF exit; 5-row schema; inventory entry verified)
  4. PBI output (BC; COMMIT-SCAN + COMMIT-FREEZE tokens)
  5. BC-COVERAGE-RECORD ([COVERAGE AUDIT] gate; schema from BC-STEP1-PROTOCOL section)
  6. PHASE-HANDOVER-1 table (BC exit; 5-row schema; inventory entry verified)
  7. HANDLE LEDGER output (IA)
  8. PHASE-HANDOVER-2 table (IA Step 2 exit; 5-row schema; inventory entry verified)
  9. STILL-LIVE FILTER output: STILL-LIVE-[N] and DISCARD-[N] tokens; each DISCARD
     followed immediately by PBI-REF / ROUTE / REASON tokens; DISCARD-LOG-COMPLETE
  10. Corrections -- HIGH -> MEDIUM -> LOW
  11. PHASE-HANDOVER-3 table (IA Step 3 exit; 5-row schema; inventory entry verified)
  12. Audited corrections (Register Audit output)
  13. PHASE-HANDOVER-4 table (IA Step 4 exit; 5-row schema; inventory entry verified)
  14. Entry Gate blocks (all STATUS: CLEARED)
  15. PHASE-HANDOVER-5 table (IA Step 5 exit; 5-row schema; inventory entry verified)
  16. Chain Integrity Audit (all CHAIN-COMPLETE)
  17. PHASE-HANDOVER-6 table (IA Step 6 exit; 5-row schema; inventory entry verified)
  18. Rules of Thumb (RULES-ANCHORED-COMPLETE with per-rule tier quotation)
  19. Surprise hierarchy (ranked with rationale)
  20. Pattern of inherited errors
  21. Blind Spot Map
  22. Correction Forward Statement (confirms NO-ECHO COST; names specific avoided failure)
  23. What this correction record excludes

Write to: simulations/topic/echo/{topic}-echo-{YYYY-MM-DD}.md
