---
skill: quest-variate
skill_target: topic-echo
date: 2026-03-16
round: 12
rubric: v12
rubric_file: simulations/quest/rubrics/topic-echo-rubric-v12-2026-03-16.md
rubric_max: 245
---

# Variations: `topic:echo` -- Round 12 (2026-03-16)

**Rubric:** v12 (2026-03-16) | **Criteria:** 39 (5 essential / 3 recommended / 31 aspirational)

---

## Design Context

R11 V-05 achieves 230/230 under v11 and 245/245 under v12. The three enforcement-layer
criteria formalized in v12 -- BC-STEP1-SUBPHASE-DECOMPOSITION (C-37), PHASE-HANDOVER-TABLE-
SCHEMA (C-38), and FILTER-IMPERATIVE-FORM (C-39) -- were satisfied incidentally by R11 V-05's
structural implementations. Round 12 does not re-implement R11's axes. It tests whether the
same scoring profiles can be achieved through **alternative structural implementations** of
each enforcement mechanism, confirming that C-37, C-38, and C-39 are triggered by pattern
class, not by surface form.

R11 implementations and R12 alternatives:

- **C-37 (BC sub-phase decomposition)** -> **Axis A -- Lifecycle emphasis**:
  R11 V-01 embedded sub-phase structure as narrative headers (`[SCAN]` / `[FREEZE]` /
  `[COVERAGE AUDIT]`) inside Step 1 prose. R12 V-01 uses a **BC-STEP1-PROTOCOL declaration
  table** inside BC's Function Declaration -- a pre-execution schema naming sub-phase, scope,
  and gate token before Step 1 begins. BC-COVERAGE-RECORD is named as the [COVERAGE AUDIT]
  gate token inside the protocol table. The decomposition is declared, not emergent. Omitting
  [COVERAGE AUDIT] means failing to close a named protocol table entry, not skipping prose.

- **C-38 (handover table schema)** -> **Axis B -- Output format**:
  R11 V-02 placed 5-row handover tables at two role-boundary exits only (EF exit, BC exit).
  R12 V-02 extends the 5-row schema to **all seven stage exits (PHASE-HANDOVER-0 through
  PHASE-HANDOVER-6)**. Every stage transition is schema-comparable by inspection. Universal
  application makes C-38 non-defeatable by selective omission: no "non-role-boundary"
  exception path exists.

- **C-39 (filter imperative form)** -> **Axis C -- Phrasing register**:
  R11 V-03 used terse single-sentence imperatives ("Write DISCARD-[N]. Name the finding
  label."). R12 V-03 uses **four numbered MUST-clauses** (MUST-1 through MUST-4), each
  beginning with explicit unconditional scope ("For every candidate" / "For every DISCARD
  token"). Each clause is independently auditable without reading surrounding prose. The
  unconditional scope is stated in the clause body, not implied by imperative mood alone.

**Predicted scoring under v12:**

| Variation | C-34 | C-35 | C-36 | C-37 | C-38 | C-39 | Predicted |
|-----------|:----:|:----:|:----:|:----:|:----:|:----:|:---------:|
| V-01 | PASS | FAIL | FAIL | PASS | FAIL | FAIL | 225 |
| V-02 | FAIL | PASS | FAIL | FAIL | PASS | FAIL | 225 |
| V-03 | FAIL | FAIL | PASS | FAIL | FAIL | PASS | 225 |
| V-04 | PASS | PASS | FAIL | PASS | PASS | FAIL | 235 |
| **V-05** | PASS | PASS | PASS | PASS | PASS | PASS | **245** |

**R12 progression layer:** R11 demonstrated that sub-phase headers / selective 5-row tables /
terse imperatives reliably trigger C-37/C-38/C-39. R12 tests whether a declaration-table
sub-phase structure / universal 7-exit schema / MUST-clause protocol produces identical
scoring profiles. If both sets achieve the same scores, the criteria are implementation-robust:
pattern class determines pass/fail, not surface form.

---

## V-01 -- Axis A: BC-STEP1-PROTOCOL Declaration Table

**Variation axis:** Lifecycle emphasis -- BC's Step 1 decomposition declared as a protocol
table inside BC Function Declaration, with gate tokens pre-specified before execution begins
(Axis A only)

**Hypothesis:** R11 V-01 embedded sub-phase structure in narrative headers within Step 1
text, making the BC execution model recoverable only by reading the full Step 1 block. If
the decomposition is declared as a BC-STEP1-PROTOCOL table inside BC's Function Declaration
-- naming sub-phase, scope, and gate token in a structured schema -- the structure is
auditable from the declaration alone, before any execution content is read. BC-COVERAGE-RECORD
is specified as the [COVERAGE AUDIT] gate token in the table. C-37 is satisfied because BC's
internal process is observable at the role boundary, not inside the execution block. Sub-phase
omission is detectable as a protocol-table violation, not a missing prose section.

**Expected v12 score:** 225 (C-34 PASS; C-37 PASS; C-35 FAIL; C-38 FAIL; C-36 FAIL;
C-39 FAIL)

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
              EF-INVOCATION-RECORD must name every pre-investigation
              source consulted and list all signal artifacts as excluded.
Out-of-scope: PBI production. Entry authoring. Chain verification.
Phase scope:  Step 0 only. EF excluded from Steps 1-7.
Gate return:  ENFORCEMENT MECHANISM section + EF-INVOCATION-RECORD
              complete before proceeding to Step 1.
----------------------------------------------------------------------
```

**Belief Cartographer (BC)** -- Step 1 exclusively; three sub-phases declared below.

```
BELIEF CARTOGRAPHER -- FUNCTION DECLARATION
----------------------------------------------------------------------
Function:     Pre-investigation belief recovery. Execute Step 1 in the
              three sequential sub-phases declared in BC-STEP1-PROTOCOL.
              Do not merge sub-phases. Write each gate token before
              advancing to the next sub-phase.

BC-STEP1-PROTOCOL
--------------------------------------------------------------------
Sub-phase      | Scope                           | Gate Token
--------------------------------------------------------------------
[SCAN]         | Read design materials. List all | COMMIT-SCAN:
               | belief candidates. No pruning   | [N] candidates
               | or evaluation during this phase.| identified.
--------------------------------------------------------------------
[FREEZE]       | Produce PBI from scan results.  | COMMIT-FREEZE:
               | Lock all PB-[NN] entries. No    | PBI frozen at
               | additions after gate token.     | [N] entries.
--------------------------------------------------------------------
[COVERAGE      | Audit domain coverage. Produce  | BC-COVERAGE-RECORD
 AUDIT]        | BC-COVERAGE-RECORD (see schema).| (schema below).
               | BC exclusion takes effect after |
               | this gate token is written.     |
--------------------------------------------------------------------

Input:        Design materials only. Same exclusion scope as EF.
Out-of-scope: Signal artifacts. Handle Ledger. Entry authoring.
Phase scope:  Step 1 only. BC excluded from Steps 2-7 after
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

Execute BC-STEP1-PROTOCOL as declared in BC Function Declaration. Write each gate token
before advancing to the next sub-phase.

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

**[COVERAGE AUDIT]** After PBI freeze, produce the coverage record. BC exclusion from
Steps 2-7 does not take effect until BC-COVERAGE-RECORD is written.

```
BC-COVERAGE-RECORD
----------------------------------------------------------------------
Sub-phase:  [COVERAGE AUDIT] -- gate token declared in BC-STEP1-PROTOCOL.
            Produced at the [COVERAGE AUDIT] boundary before BC exclusion
            takes effect.
Materials consulted (pre-investigation only):
  [List each design document, spec, proposal, or other pre-investigation
   source scanned during [SCAN] and [FREEZE] sub-phases. Minimum one
   entry.]
Signal artifacts excluded:
  [List each signal artifact by name and confirm it was not accessed
   during Step 1.]
PBI completeness basis:
  [One sentence: which material(s) provide the primary basis for the
   PBI entry set. A reviewer can re-run BC against these materials to
   verify entry completeness without re-running the full investigation.]
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
  4. BC-COVERAGE-RECORD ([COVERAGE AUDIT] gate; declared in BC-STEP1-PROTOCOL)
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

## V-02 -- Axis B: Universal Phase Handover Schema

**Variation axis:** Output format -- all seven stage exits (Steps 0-6) produce a
PHASE-HANDOVER-[N] table in the 5-row schema (Completing Role / Step Completed / Output
Produced / Exclusion In Effect / Receiving Role), not only the role-boundary exits
(Axis B only)

**Hypothesis:** R11 V-02 placed 5-row handover tables at the two role-boundary exits (EF
exit at Step 0, BC exit at Step 1), satisfying C-38 through selective placement. If the
5-row schema is applied universally to all seven stage exits, every stage transition is
schema-comparable by inspection -- not only the role boundaries. Universal application
removes any "non-role-boundary" exception path. A reviewer auditing handover completeness
checks seven tables against the same schema; there is no stage exit that legitimately omits
a handover record. C-35 and C-38 are satisfied through schema breadth rather than schema
depth at selected transitions.

**Expected v12 score:** 225 (C-35 PASS; C-38 PASS; C-34 FAIL; C-37 FAIL; C-36 FAIL;
C-39 FAIL)

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

**PHASE-HANDOVER-0:**

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

**PHASE-HANDOVER-1:**

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

**PHASE-HANDOVER-2:**

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

**PHASE-HANDOVER-3:**

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

**PHASE-HANDOVER-4:**

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

**PHASE-HANDOVER-5:**

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

**PHASE-HANDOVER-6:**

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
  3. PHASE-HANDOVER-0 table (EF exit; 5-row schema)
  4. PBI output (BC; frozen)
  5. PHASE-HANDOVER-1 table (BC exit; 5-row schema)
  6. HANDLE LEDGER output (IA)
  7. PHASE-HANDOVER-2 table (IA Step 2 exit; 5-row schema)
  8. Corrections -- HIGH -> MEDIUM -> LOW
  9. PHASE-HANDOVER-3 table (IA Step 3 exit; 5-row schema)
  10. Audited corrections (Register Audit output)
  11. PHASE-HANDOVER-4 table (IA Step 4 exit; 5-row schema)
  12. Entry Gate blocks (all STATUS: CLEARED)
  13. PHASE-HANDOVER-5 table (IA Step 5 exit; 5-row schema)
  14. Chain Integrity Audit (all CHAIN-COMPLETE)
  15. PHASE-HANDOVER-6 table (IA Step 6 exit; 5-row schema)
  16. Rules of Thumb (RULES-ANCHORED-COMPLETE)
  17. Surprise hierarchy
  18. Pattern of inherited errors
  19. Blind Spot Map
  20. Correction Forward Statement
  21. What this correction record excludes

Write to: simulations/topic/echo/{topic}-echo-{YYYY-MM-DD}.md

---

## V-03 -- Axis C: MUST-Clause Filter Protocol

**Variation axis:** Phrasing register -- STILL-LIVE FILTER written as four numbered
MUST-clauses, each with explicit unconditional scope in the clause body (Axis C only)

**Hypothesis:** R11 V-03 used terse single-sentence imperatives that implied unconditional
scope through imperative mood ("Write DISCARD-[N]. Name the finding label."). This satisfies
C-39 but compresses four distinct obligations into a reading-order dependency. If the filter
is written as four numbered MUST-clauses where each clause begins with its unconditional
scope ("For every candidate" / "For every DISCARD token"), a reviewer can check any single
MUST clause against the artifact independently -- without reading surrounding clauses. The
MUST form makes the "no conditional branch" property structurally legible per clause.
C-39 is satisfied not just by imperative grammar but by the explicit unconditional scoping
of each of the four commands.

**Expected v12 score:** 225 (C-36 PASS; C-39 PASS; C-34 FAIL; C-37 FAIL; C-35 FAIL;
C-38 FAIL)

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

**STILL-LIVE FILTER -- MUST-CLAUSE PROTOCOL**

Apply to every candidate from the Handle Ledger. All four MUST-clauses apply to every
candidate without exception. No candidate evaluation concludes without completing all
four MUST-clauses for that candidate.

```
STILL-LIVE FILTER PROTOCOL
----------------------------------------------------------------------
MUST-1: For every candidate, produce exactly one of:
          STILL-LIVE-[N]: [candidate name]
          DISCARD-[N]: [candidate name]
        No candidate evaluation concludes without one of these tokens.
        This clause applies to every candidate. No exceptions.

MUST-2: For every DISCARD-[N] token, immediately write:
          DISCARD-[N]-PBI-REF: PB-[NN]
        Names the prior belief this candidate was tested against.
        A DISCARD token without a PBI-Ref token is malformed.
        This clause applies to every DISCARD token. No exceptions.

MUST-3: For every DISCARD-[N] token, immediately write:
          DISCARD-[N]-ROUTE: [destination -- topic-story or named skill]
        States where excluded candidates are recorded.
        A DISCARD token without a ROUTE token is malformed.
        This clause applies to every DISCARD token. No exceptions.

MUST-4: For every DISCARD-[N] token, immediately write:
          DISCARD-[N]-REASON: [one sentence -- specific exclusion reason]
        States why this candidate fails the STILL-LIVE test.
        A DISCARD token without a REASON token is malformed.
        This clause applies to every DISCARD token. No exceptions.

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
  5. STILL-LIVE FILTER output: STILL-LIVE-[N] and DISCARD-[N] tokens, each DISCARD
     followed by PBI-REF / ROUTE / REASON tokens; DISCARD-LOG-COMPLETE at close
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

## V-04 -- Axes A+B: Protocol Table + Universal Handover Schema

**Variation axes:** Lifecycle emphasis (Axis A) + Output format (Axis B)

**Hypothesis:** Combining BC-STEP1-PROTOCOL declaration table (Axis A) with universal
PHASE-HANDOVER-[N] tables at all seven stage exits (Axis B) produces additive auditability.
BC's sub-phase decomposition is declared before execution (C-37). Every stage transition
is schema-comparable (C-38). The two mechanisms are structurally independent: Axis A
modifies the BC Function Declaration and Step 1 execution; Axis B modifies stage exit
tokens in Steps 0-6. Combining them does not compromise either. The STILL-LIVE FILTER
remains conditional (Axis C absent), so C-36 and C-39 fail.

**Expected v12 score:** 235 (C-34 PASS; C-35 PASS; C-37 PASS; C-38 PASS; C-36 FAIL;
C-39 FAIL)

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

**Belief Cartographer (BC)** -- Step 1 exclusively; three sub-phases declared below.

```
BELIEF CARTOGRAPHER -- FUNCTION DECLARATION
----------------------------------------------------------------------
Function:     Pre-investigation belief recovery. Execute Step 1 in the
              three sequential sub-phases declared in BC-STEP1-PROTOCOL.
              Do not merge sub-phases. Write each gate token before
              advancing to the next sub-phase.

BC-STEP1-PROTOCOL
--------------------------------------------------------------------
Sub-phase      | Scope                           | Gate Token
--------------------------------------------------------------------
[SCAN]         | Read design materials. List all | COMMIT-SCAN:
               | belief candidates. No pruning   | [N] candidates
               | or evaluation during this phase.| identified.
--------------------------------------------------------------------
[FREEZE]       | Produce PBI from scan results.  | COMMIT-FREEZE:
               | Lock all PB-[NN] entries. No    | PBI frozen at
               | additions after gate token.     | [N] entries.
--------------------------------------------------------------------
[COVERAGE      | Audit domain coverage. Produce  | BC-COVERAGE-RECORD
 AUDIT]        | BC-COVERAGE-RECORD (see schema).| (schema below).
               | BC exclusion takes effect after |
               | this gate token is written.     |
--------------------------------------------------------------------

Input:        Design materials only. Same exclusion scope as EF.
Out-of-scope: Signal artifacts. Handle Ledger. Entry authoring.
Phase scope:  Step 1 only. BC excluded from Steps 2-7 after
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

**PHASE-HANDOVER-0:**

| Field | Content |
|-------|---------|
| Completing Role | Enforcement Framer (EF) -- Step 0 |
| Step Completed | Step 0 -- Enforcement Section and Invocation Record |
| Output Produced | ENFORCEMENT MECHANISM DECLARATION + EF-INVOCATION-RECORD |
| Exclusion In Effect | EF excluded from Steps 1-7; signal artifacts not accessed at Step 0 |
| Receiving Role | Belief Cartographer (BC) -- Step 1 |

---

### Step 1 -- [BC] Belief Inventory and Coverage Audit

Execute BC-STEP1-PROTOCOL as declared in BC Function Declaration. Write each gate token
before advancing.

**[SCAN]** Read all design materials within BC's input scope. Signal artifacts out of
scope. Identify every belief candidate. List all candidates before moving to [FREEZE].

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

**[COVERAGE AUDIT]** After PBI freeze, produce the coverage record.

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

BC is now excluded from Steps 2-7.

**PHASE-HANDOVER-1:**

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

**PHASE-HANDOVER-2:**

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

**PHASE-HANDOVER-3:**

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

**PHASE-HANDOVER-4:**

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

**PHASE-HANDOVER-5:**

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

**PHASE-HANDOVER-6:**

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
  3. PHASE-HANDOVER-0 table (EF exit; 5-row schema)
  4. PBI output (BC; COMMIT-SCAN + COMMIT-FREEZE tokens)
  5. BC-COVERAGE-RECORD ([COVERAGE AUDIT] gate; declared in BC-STEP1-PROTOCOL)
  6. PHASE-HANDOVER-1 table (BC exit; 5-row schema)
  7. HANDLE LEDGER output (IA)
  8. PHASE-HANDOVER-2 table (IA Step 2 exit; 5-row schema)
  9. Corrections -- HIGH -> MEDIUM -> LOW
  10. PHASE-HANDOVER-3 table (IA Step 3 exit; 5-row schema)
  11. Audited corrections (Register Audit output)
  12. PHASE-HANDOVER-4 table (IA Step 4 exit; 5-row schema)
  13. Entry Gate blocks (all STATUS: CLEARED)
  14. PHASE-HANDOVER-5 table (IA Step 5 exit; 5-row schema)
  15. Chain Integrity Audit (all CHAIN-COMPLETE)
  16. PHASE-HANDOVER-6 table (IA Step 6 exit; 5-row schema)
  17. Rules of Thumb (RULES-ANCHORED-COMPLETE)
  18. Surprise hierarchy
  19. Pattern of inherited errors
  20. Blind Spot Map
  21. Correction Forward Statement
  22. What this correction record excludes

Write to: simulations/topic/echo/{topic}-echo-{YYYY-MM-DD}.md

---

## V-05 -- Axes A+B+C: Full Combination

**Variation axes:** Lifecycle emphasis (Axis A) + Output format (Axis B) + Phrasing
register (Axis C)

**Hypothesis:** Combining all three R12 axes produces the maximum-scoring variant. The
BC-STEP1-PROTOCOL declaration table (Axis A) satisfies C-37: sub-phase decomposition is
declared before execution, observable at the role boundary. Universal PHASE-HANDOVER-[N]
tables at all seven exits (Axis B) satisfy C-38: every transition is schema-comparable.
The MUST-clause STILL-LIVE filter (Axis C) satisfies C-39: four unconditional commands
each with explicit scope, no conditional branch that skips record production. All three
mechanisms target different phases (Step 1 / Steps 0-6 / Step 3) and are structurally
independent. V-05 is the only variation predicted to achieve 245/245 under v12.

**Expected v12 score:** 245 (C-34 PASS; C-35 PASS; C-36 PASS; C-37 PASS; C-38 PASS;
C-39 PASS)

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

**Belief Cartographer (BC)** -- Step 1 exclusively; three sub-phases declared below.

```
BELIEF CARTOGRAPHER -- FUNCTION DECLARATION
----------------------------------------------------------------------
Function:     Pre-investigation belief recovery. Execute Step 1 in the
              three sequential sub-phases declared in BC-STEP1-PROTOCOL.
              Do not merge sub-phases. Write each gate token before
              advancing to the next sub-phase.

BC-STEP1-PROTOCOL
--------------------------------------------------------------------
Sub-phase      | Scope                           | Gate Token
--------------------------------------------------------------------
[SCAN]         | Read design materials. List all | COMMIT-SCAN:
               | belief candidates. No pruning   | [N] candidates
               | or evaluation during this phase.| identified.
--------------------------------------------------------------------
[FREEZE]       | Produce PBI from scan results.  | COMMIT-FREEZE:
               | Lock all PB-[NN] entries. No    | PBI frozen at
               | additions after gate token.     | [N] entries.
--------------------------------------------------------------------
[COVERAGE      | Audit domain coverage. Produce  | BC-COVERAGE-RECORD
 AUDIT]        | BC-COVERAGE-RECORD (see schema).| (schema below).
               | BC exclusion takes effect after |
               | this gate token is written.     |
--------------------------------------------------------------------

Input:        Design materials only. Same exclusion scope as EF.
Out-of-scope: Signal artifacts. Handle Ledger. Entry authoring.
Phase scope:  Step 1 only. BC excluded from Steps 2-7 after
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

**PHASE-HANDOVER-0:**

| Field | Content |
|-------|---------|
| Completing Role | Enforcement Framer (EF) -- Step 0 |
| Step Completed | Step 0 -- Enforcement Section and Invocation Record |
| Output Produced | ENFORCEMENT MECHANISM DECLARATION + EF-INVOCATION-RECORD |
| Exclusion In Effect | EF excluded from Steps 1-7; signal artifacts not accessed at Step 0 |
| Receiving Role | Belief Cartographer (BC) -- Step 1 |

---

### Step 1 -- [BC] Belief Inventory and Coverage Audit

Execute BC-STEP1-PROTOCOL as declared in BC Function Declaration. Write each gate token
before advancing.

**[SCAN]** Read all design materials within BC's input scope. Signal artifacts out of
scope. Identify every belief candidate. List all candidates before moving to [FREEZE].

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

**[COVERAGE AUDIT]** After PBI freeze, produce the coverage record.

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

BC is now excluded from Steps 2-7.

**PHASE-HANDOVER-1:**

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

**PHASE-HANDOVER-2:**

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

**STILL-LIVE FILTER -- MUST-CLAUSE PROTOCOL**

Apply to every candidate from the Handle Ledger. All four MUST-clauses apply to every
candidate without exception. No candidate evaluation concludes without completing all
four MUST-clauses for that candidate.

```
STILL-LIVE FILTER PROTOCOL
----------------------------------------------------------------------
MUST-1: For every candidate, produce exactly one of:
          STILL-LIVE-[N]: [candidate name]
          DISCARD-[N]: [candidate name]
        No candidate evaluation concludes without one of these tokens.
        This clause applies to every candidate. No exceptions.

MUST-2: For every DISCARD-[N] token, immediately write:
          DISCARD-[N]-PBI-REF: PB-[NN]
        Names the prior belief this candidate was tested against.
        A DISCARD token without a PBI-Ref token is malformed.
        This clause applies to every DISCARD token. No exceptions.

MUST-3: For every DISCARD-[N] token, immediately write:
          DISCARD-[N]-ROUTE: [destination -- topic-story or named skill]
        States where excluded candidates are recorded.
        A DISCARD token without a ROUTE token is malformed.
        This clause applies to every DISCARD token. No exceptions.

MUST-4: For every DISCARD-[N] token, immediately write:
          DISCARD-[N]-REASON: [one sentence -- specific exclusion reason]
        States why this candidate fails the STILL-LIVE test.
        A DISCARD token without a REASON token is malformed.
        This clause applies to every DISCARD token. No exceptions.

Completeness gate: After all candidates are processed, write:
  DISCARD-LOG-COMPLETE: [N] STILL-LIVE, [M] DISCARD -- all four
  MUST-clauses applied to every candidate; no candidate unresolved.
----------------------------------------------------------------------
```

**PHASE-HANDOVER-3:**

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

**PHASE-HANDOVER-4:**

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

**PHASE-HANDOVER-5:**

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

**PHASE-HANDOVER-6:**

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
  3. PHASE-HANDOVER-0 table (EF exit; 5-row schema)
  4. PBI output (BC; COMMIT-SCAN + COMMIT-FREEZE tokens)
  5. BC-COVERAGE-RECORD ([COVERAGE AUDIT] gate; declared in BC-STEP1-PROTOCOL)
  6. PHASE-HANDOVER-1 table (BC exit; 5-row schema)
  7. HANDLE LEDGER output (IA)
  8. PHASE-HANDOVER-2 table (IA Step 2 exit; 5-row schema)
  9. STILL-LIVE FILTER output: STILL-LIVE-[N] and DISCARD-[N] tokens, each DISCARD
     followed immediately by PBI-REF / ROUTE / REASON tokens; DISCARD-LOG-COMPLETE
  10. Corrections -- HIGH -> MEDIUM -> LOW
  11. PHASE-HANDOVER-3 table (IA Step 3 exit; 5-row schema)
  12. Audited corrections (Register Audit output)
  13. PHASE-HANDOVER-4 table (IA Step 4 exit; 5-row schema)
  14. Entry Gate blocks (all STATUS: CLEARED)
  15. PHASE-HANDOVER-5 table (IA Step 5 exit; 5-row schema)
  16. Chain Integrity Audit (all CHAIN-COMPLETE)
  17. PHASE-HANDOVER-6 table (IA Step 6 exit; 5-row schema)
  18. Rules of Thumb (RULES-ANCHORED-COMPLETE with per-rule tier quotation)
  19. Surprise hierarchy (ranked with rationale)
  20. Pattern of inherited errors
  21. Blind Spot Map
  22. Correction Forward Statement (confirms NO-ECHO COST; names avoided failure)
  23. What this correction record excludes

Write to: simulations/topic/echo/{topic}-echo-{YYYY-MM-DD}.md
