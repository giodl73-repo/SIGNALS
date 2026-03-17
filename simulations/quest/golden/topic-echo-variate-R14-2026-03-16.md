---
skill: quest-variate
skill_target: topic-echo
date: 2026-03-16
round: 14
rubric: v14
rubric_file: simulations/quest/rubrics/topic-echo-rubric-v14-2026-03-16.md
rubric_max: 275
---

# Variations: `topic:echo` -- Round 14 (2026-03-16)

**Rubric:** v14 (2026-03-16) | **Criteria:** 45 (5 essential / 3 recommended / 37 aspirational)

---

## Design Context

R13 V-05 achieves 260/260 under v13. The three navigability criteria formalized in v14 --
PROTOCOL-HEADING-SOVEREIGNTY (C-43), INVENTORY-BEFORE-INSTANCE (C-44), and SCOPE-FIELD-
SEPARATION (C-45) -- were satisfied incidentally by R13's structural implementations. Round
14 does not re-implement R13's axes. It tests whether the same scoring profiles can be
achieved through **alternative structural implementations** of each navigability mechanism,
confirming that C-43, C-44, and C-45 are triggered by pattern class, not by surface form.

R13 implementations and R14 alternatives:

- **C-43 (PROTOCOL-HEADING-SOVEREIGNTY)** -> **Axis A-double: Code-Fence-Free Section**:
  R13 V-01 placed BC-STEP1-PROTOCOL as a `### BC-STEP1-PROTOCOL` heading section, with the
  sub-phase table in plain markdown but the BC-COVERAGE-RECORD schema in a code fence. The
  section heading is navigable, but a reviewer who wants the schema must enter a code block.
  R14 V-01 removes all code fences from the BC-STEP1-PROTOCOL section entirely: the
  sub-phase table and the BC-COVERAGE-RECORD schema are both expressed as markdown tables,
  with the schema under a `#### BC-COVERAGE-RECORD Schema` sub-heading. The full protocol
  specification -- including the schema -- is navigable from heading hierarchy alone without
  entering any code block. C-43 is satisfied because no content within the protocol section
  is gated behind a code fence.

- **C-44 (INVENTORY-BEFORE-INSTANCE)** -> **Axis B-double: Roles-Embedded Registry**:
  R13 V-02 added a standalone `### PHASE-HANDOVER-INVENTORY` section between the Roles
  section and Step 0 -- a separate document-level section whose sole content is the 7-row
  inventory table. R14 V-02 embeds the inventory as a `#### Phase Transition Registry`
  sub-heading at the END of the Roles section, before Step 0 begins. The registry lists all
  seven transitions with the same identity fields (transition name, step completed, completing
  role, receiving role). Universality is still verifiable by cross-reference from the registry
  against inline tables; the registry still appears before any step executes. C-44 tests
  the cross-reference property (inventory pre-declared before execution), not the position
  of the inventory relative to the Roles section boundary.

- **C-45 (SCOPE-FIELD-SEPARATION)** -> **Axis C-double: Table-Column MUST-Clauses**:
  R13 V-03 expressed MUST-clauses as labeled fields within a code fence (Scope: / Action: as
  free-form label-value pairs inside a code block). The Scope field is structurally present
  but requires parsing the code block to reach it. R14 V-03 expresses each MUST-clause as a
  row in a four-column markdown table (MUST-ID | Scope | Action | Constraint). The Scope
  column is independently readable without parsing the Action column -- a reviewer checking
  "which entity class does MUST-3 govern?" reads the Scope cell in the table directly. C-45
  tests the field-separation property (scope auditable from label structure alone), not
  the code-fence vs. table distinction.

**Predicted scoring under v14:**

| Variation | C-43 | C-44 | C-45 | v13 | v14 | delta |
|-----------|:----:|:----:|:----:|:---:|:---:|:-----:|
| V-01 | PASS | FAIL | FAIL | 230 | 235 | +5 |
| V-02 | FAIL | PASS | FAIL | 230 | 235 | +5 |
| V-03 | FAIL | FAIL | PASS | 230 | 235 | +5 |
| V-04 | PASS | PASS | FAIL | 240 | 250 | +10 |
| **V-05** | PASS | PASS | PASS | 260 | **275** | +15 |

**R14 progression layer:** R13 demonstrated that a standalone heading section / pre-declared
inventory / scope-field labeled fields reliably trigger C-43/C-44/C-45. R14 tests whether
a code-fence-free heading section / roles-embedded registry / table-column scope fields
produce identical scoring profiles. If both sets achieve the same scores, the navigability
criteria are implementation-robust: the structural property class determines pass/fail, not
the surface encoding within that class.

---

## V-01 -- Axis A-double: Code-Fence-Free BC-STEP1-PROTOCOL Section

**Variation axis:** Lifecycle emphasis -- BC-STEP1-PROTOCOL section is fully code-fence-free;
the sub-phase contract and BC-COVERAGE-RECORD schema are both expressed as markdown tables
under named sub-headings (Axis A-double only)

**Hypothesis:** R13 V-01 placed the sub-phase table in plain markdown but the BC-COVERAGE-RECORD
schema in a code fence. The heading `### BC-STEP1-PROTOCOL` is navigable, but the schema is
only readable by entering the code block. R14 V-01 removes all code fences from the section:
both the sub-phase table and the BC-COVERAGE-RECORD schema are markdown tables, the schema
under `#### BC-COVERAGE-RECORD Schema`. A reviewer can read the complete protocol -- including
the schema field definitions -- using heading navigation alone, without entering any block. C-43
is satisfied because heading sovereignty now applies to the full section content, not only to
the section's entry point. C-40 is also satisfied because the pre-execution declaration exists
and is standalone. C-43 is a strict superset.

**Expected v14 score:** 235 (C-37 PASS; C-40 PASS; C-43 PASS; C-38 FAIL; C-41 FAIL; C-39 FAIL;
C-42 FAIL; C-44 FAIL; C-45 FAIL)

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
this section by name only; the full protocol specification -- including the BC-COVERAGE-RECORD
schema -- is here, expressed entirely as markdown tables with no code fences. A reviewer can
read the complete contract from heading navigation alone.

| Sub-phase | Scope | Gate Token |
|-----------|-------|------------|
| [SCAN] | Read design materials. List all belief candidates. No pruning or evaluation during this phase. | `COMMIT-SCAN: [N] candidates identified.` |
| [FREEZE] | Produce PBI from scan results. Lock all PB-[NN] entries. No additions after gate token. | `COMMIT-FREEZE: PBI frozen at [N] entries.` |
| [COVERAGE AUDIT] | Audit domain coverage. Produce BC-COVERAGE-RECORD using the schema below. BC exclusion takes effect after this record is written. | BC-COVERAGE-RECORD (schema below). |

#### BC-COVERAGE-RECORD Schema

| Field | Content | Constraint |
|-------|---------|------------|
| Sub-phase | [COVERAGE AUDIT] -- gate declared in BC-STEP1-PROTOCOL. | Fixed; do not substitute. |
| Materials consulted | [List each design document scanned during [SCAN] and [FREEZE]. Minimum one entry.] | Pre-investigation only. Signal artifacts excluded. |
| Signal artifacts excluded | [List each signal artifact by name; confirm not accessed during Step 1.] | Enumerated by name; "none" is not acceptable if signals exist. |
| PBI completeness basis | [One sentence: which material(s) provide the primary PBI basis.] | Single sentence. Reviewable from this field alone. |

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
scope for this sub-phase. Identify every belief candidate. List all candidates before moving
to [FREEZE].

`COMMIT-SCAN: [N] candidates identified.`

**[FREEZE]** Produce the PBI from the scanned candidates.

```
PBI PRODUCTION PROTOCOL
----------------------------------------------------------------------
Input:    Design materials only. Signal artifacts excluded.
Format:   PB-[NN]: ["Today's materials imply that X." No signal
          knowledge.]
Freeze:   PBI frozen after COMMIT-FREEZE token. No new PB-[NN] entries
          after this point. PBI entries must not use handle labels
          (unavailable at Step 1).
----------------------------------------------------------------------
```

`COMMIT-FREEZE: PBI frozen at [N] entries.`

**[COVERAGE AUDIT]** After PBI freeze, produce BC-COVERAGE-RECORD using the schema declared
in the BC-STEP1-PROTOCOL section above (four-field table format; no code fence).

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
  4. BC-COVERAGE-RECORD (table format; four fields; no code fence)
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

## V-02 -- Axis B-double: Roles-Embedded Phase Transition Registry

**Variation axis:** Output format -- the PHASE-HANDOVER-INVENTORY is embedded as a named
subsection (`#### Phase Transition Registry`) at the end of the Roles section, before Step 0
begins; each step exit still produces an inline PHASE-HANDOVER-[N] table in the 5-row schema
(Axis B-double only)

**Hypothesis:** R13 V-02 placed PHASE-HANDOVER-INVENTORY as a standalone `### PHASE-HANDOVER-
INVENTORY` section between the Roles section and Step 0. The critical C-44 property is that
the inventory pre-declares all expected transitions before any step executes, enabling cross-
reference verification rather than traversal. If the same inventory is embedded as a subsection
under the Roles section heading (before Step 0 begins), the cross-reference property is preserved
unchanged: the registry still lists all seven transitions before execution; inline tables are
still checked against the registry by reference; a missing table is still detectable from the
registry alone. C-44 tests the cross-reference property, not the position of the inventory
relative to the step-heading boundary.

**Expected v14 score:** 235 (C-38 PASS; C-41 PASS; C-44 PASS; C-37 FAIL; C-40 FAIL; C-39 FAIL;
C-42 FAIL; C-43 FAIL; C-45 FAIL)

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

#### Phase Transition Registry

Pre-declared registry of all seven phase transitions for this workflow. Every step exit in
Steps 0 through 6 must produce a PHASE-HANDOVER-[N] table matching this registry. This
registry is declared here, within the Roles section, before Step 0 begins: no step output
has been produced when this registry is read. Coverage is verifiable by cross-referencing
the registry rows against the inline PHASE-HANDOVER-[N] tables without document traversal --
a missing table appears as an unchecked registry row.

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

**PHASE-HANDOVER-0** (registry entry: EF -> BC):

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

**PHASE-HANDOVER-1** (registry entry: BC -> IA):

| Field | Content |
|-------|---------|
| Completing Role | Belief Cartographer (BC) -- Step 1 |
| Step Completed | Step 1 -- Belief Inventory |
| Output Produced | PBI (all PB-[NN] frozen) |
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

**PHASE-HANDOVER-2** (registry entry: IA Step 2 -> IA Step 3):

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

**PHASE-HANDOVER-3** (registry entry: IA Step 3 -> IA Step 4):

| Field | Content |
|-------|---------|
| Completing Role | Institutional Archaeologist (IA) -- Step 3 |
| Step Completed | Step 3 -- Draft All Corrections |
| Output Produced | Draft corrections (all STILL-LIVE candidates) |
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

**PHASE-HANDOVER-4** (registry entry: IA Step 4 -> IA Step 5):

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

**PHASE-HANDOVER-5** (registry entry: IA Step 5 -> IA Step 6):

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

**PHASE-HANDOVER-6** (registry entry: IA Step 6 -> IA Step 7):

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

**Correction Forward Statement:** 1-3 sentences. Name the specific failure this artifact
prevented. Identify the false assumption the next team would have inherited. Confirm EF's
NO-ECHO COST. Make the institutional purpose falsifiable.

**What this correction record excludes:** At least two categories with counts.

---

== ARTIFACT STRUCTURE ============================================================

  1. ENFORCEMENT MECHANISM DECLARATION (EF; NO-ECHO COST)
  2. EF-INVOCATION-RECORD (Step 0)
  3. PHASE-HANDOVER-0 table (EF exit; 5-row schema; registry entry verified)
  4. PBI output (BC; COMMIT-SCAN not required -- no sub-phase decomposition)
  5. PHASE-HANDOVER-1 table (BC exit; 5-row schema; registry entry verified)
  6. HANDLE LEDGER output (IA)
  7. PHASE-HANDOVER-2 table (IA Step 2 exit; 5-row schema; registry entry verified)
  8. Corrections -- HIGH -> MEDIUM -> LOW
  9. PHASE-HANDOVER-3 table (IA Step 3 exit; 5-row schema; registry entry verified)
  10. Audited corrections (Register Audit output)
  11. PHASE-HANDOVER-4 table (IA Step 4 exit; 5-row schema; registry entry verified)
  12. Entry Gate blocks (all STATUS: CLEARED)
  13. PHASE-HANDOVER-5 table (IA Step 5 exit; 5-row schema; registry entry verified)
  14. Chain Integrity Audit (all CHAIN-COMPLETE)
  15. PHASE-HANDOVER-6 table (IA Step 6 exit; 5-row schema; registry entry verified)
  16. Rules of Thumb (RULES-ANCHORED-COMPLETE with per-rule tier quotation)
  17. Surprise hierarchy (ranked with rationale)
  18. Pattern of inherited errors
  19. Blind Spot Map
  20. Correction Forward Statement (confirms NO-ECHO COST; names specific avoided failure)
  21. What this correction record excludes

Write to: simulations/topic/echo/{topic}-echo-{YYYY-MM-DD}.md

---

## V-03 -- Axis C-double: Table-Column MUST-Clauses

**Variation axis:** Phrasing register -- each MUST-clause in the STILL-LIVE FILTER is a row
in a four-column markdown table (MUST-ID | Scope | Action | Constraint); Scope and Action are
structurally independent columns, not labeled fields embedded in a code block (Axis C-double only)

**Hypothesis:** R13 V-03 expressed MUST-clauses with `Scope:` / `Action:` as labeled fields
within a code fence. The Scope field is structurally present but requires opening the code
block and parsing label-value pairs to locate it. R14 V-03 uses a markdown table where Scope
is a named COLUMN. A reviewer auditing "which entity class does MUST-3 govern?" reads the
Scope cell directly from the table -- the Scope column is addressable by column header without
reading the Action column. This tests whether C-45 (scope auditable from field label without
parsing the action) is triggered by the structural-field property, regardless of whether the
field is a table column vs. a code-fence label.

**Expected v14 score:** 235 (C-39 PASS; C-42 PASS; C-45 PASS; C-37 FAIL; C-38 FAIL; C-40 FAIL;
C-41 FAIL; C-43 FAIL; C-44 FAIL)

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
              NO-ECHO COST from pre-investigation materials only.
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

---

### Step 1 -- [BC] Belief Inventory

```
PBI PRODUCTION PROTOCOL
----------------------------------------------------------------------
Input:    Design materials only. Signal artifacts excluded.
Format:   PB-[NN]: ["Today's materials imply that X." No signal
          knowledge.]
Freeze:   PBI frozen after BC completes Step 1. No new PB-[NN] entries
          after this point. No handle labels in PBI entries.
----------------------------------------------------------------------
```

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

Order: HIGH -> MEDIUM -> LOW.
----------------------------------------------------------------------
```

**STILL-LIVE FILTER -- TABLE-COLUMN MUST-CLAUSE PROTOCOL**

Apply each MUST-clause to every candidate from the Handle Ledger. The table format separates
Scope from Action structurally: a reviewer auditing which entity class a MUST-clause governs
reads the Scope column directly without parsing the Action column. Each MUST-clause is
unconditional -- no candidate evaluation concludes without completing all four MUST-clauses
for that candidate.

| MUST-ID | Scope | Action | Constraint |
|---------|-------|--------|------------|
| MUST-1 | EVERY CANDIDATE -- no exceptions | Produce exactly one of: `STILL-LIVE-[N]: [candidate name]` OR `DISCARD-[N]: [candidate name]` | No candidate evaluation concludes without one of these tokens. Scope is EVERY CANDIDATE; no candidate is exempt. |
| MUST-2 | EVERY DISCARD-[N] TOKEN -- no exceptions | Immediately write: `DISCARD-[N]-PBI-REF: PB-[NN]` -- names the prior belief this candidate was tested against | A DISCARD token without a PBI-Ref token is malformed. Scope is EVERY DISCARD token; no DISCARD is exempt. |
| MUST-3 | EVERY DISCARD-[N] TOKEN -- no exceptions | Immediately write: `DISCARD-[N]-ROUTE: [destination -- topic-story or named skill]` -- states where excluded candidates are recorded | A DISCARD token without a ROUTE token is malformed. Scope is EVERY DISCARD token; no DISCARD is exempt. |
| MUST-4 | EVERY DISCARD-[N] TOKEN -- no exceptions | Immediately write: `DISCARD-[N]-REASON: [one sentence -- specific exclusion reason]` -- states why this candidate fails the STILL-LIVE test | A DISCARD token without a REASON token is malformed. Scope is EVERY DISCARD token; no DISCARD is exempt. |

Completeness gate: After all candidates are processed, write:
`DISCARD-LOG-COMPLETE: [N] STILL-LIVE, [M] DISCARD -- all four MUST-clauses applied to every candidate; no candidate unresolved.`

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

**Correction Forward Statement:** 1-3 sentences. Name the specific failure this artifact
prevented. Identify the false assumption the next team would have inherited. Confirm EF's
NO-ECHO COST. Make the institutional purpose falsifiable.

**What this correction record excludes:** At least two categories with counts.

---

== ARTIFACT STRUCTURE ============================================================

  1. ENFORCEMENT MECHANISM DECLARATION (EF; NO-ECHO COST)
  2. EF-INVOCATION-RECORD (Step 0)
  3. PBI output (BC)
  4. HANDLE LEDGER output (IA)
  5. STILL-LIVE FILTER table output: STILL-LIVE-[N] and DISCARD-[N] tokens; each DISCARD
     followed immediately by PBI-REF / ROUTE / REASON tokens; DISCARD-LOG-COMPLETE
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

## V-04 -- Axes A-double+B-double: Code-Fence-Free Protocol + Roles-Embedded Registry

**Variation axes:** Lifecycle emphasis (Axis A-double) + Output format (Axis B-double)

**Hypothesis:** Combining the code-fence-free BC-STEP1-PROTOCOL section (C-43-prime) with the
roles-embedded phase transition registry (C-44-prime) produces a variation that satisfies C-37
(BC sub-phase decomposition) + C-40 (pre-execution standalone declaration) + C-43 (heading-
sovereign, no code-fence entry required) + C-38 (universal 5-row schema at all exits) + C-41
(universality simultaneously verifiable by inventory cross-reference) + C-44 (inventory pre-
declared before Step 0 within Roles section). The two mechanisms target different phases (BC's
Step 1 vs. IA's handover exits) and are structurally independent. V-04 fails C-39/C-42/C-45
because the STILL-LIVE FILTER uses a conditional branching form without scope-field separation.

**Expected v14 score:** 250 (C-37 PASS; C-38 PASS; C-40 PASS; C-41 PASS; C-43 PASS; C-44 PASS;
C-39 FAIL; C-42 FAIL; C-45 FAIL)

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
              NO-ECHO COST from pre-investigation materials only.
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

#### Phase Transition Registry

Pre-declared registry of all seven phase transitions. Every step exit in Steps 0 through 6
must produce a PHASE-HANDOVER-[N] table matching this registry. This registry is declared
within the Roles section, before Step 0 begins. Universality is verifiable by cross-referencing
the registry rows against the inline PHASE-HANDOVER-[N] tables -- no document traversal needed.

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

### BC-STEP1-PROTOCOL

Executed by BC during Step 1 in three sequential sub-phases. Write each gate token before
advancing to the next sub-phase. Do not merge sub-phases. This section is the pre-execution
contract for Step 1. It is positioned before Step 0 begins. The BC Function Declaration
references this section by name; the full protocol -- including the BC-COVERAGE-RECORD
schema -- is expressed here entirely as markdown tables with no code fences.

| Sub-phase | Scope | Gate Token |
|-----------|-------|------------|
| [SCAN] | Read design materials. List all belief candidates. No pruning or evaluation during this phase. | `COMMIT-SCAN: [N] candidates identified.` |
| [FREEZE] | Produce PBI from scan results. Lock all PB-[NN] entries. No additions after gate token. | `COMMIT-FREEZE: PBI frozen at [N] entries.` |
| [COVERAGE AUDIT] | Audit domain coverage. Produce BC-COVERAGE-RECORD using the schema below. BC exclusion takes effect after this record is written. | BC-COVERAGE-RECORD (schema below). |

#### BC-COVERAGE-RECORD Schema

| Field | Content | Constraint |
|-------|---------|------------|
| Sub-phase | [COVERAGE AUDIT] -- gate declared in BC-STEP1-PROTOCOL. | Fixed; do not substitute. |
| Materials consulted | [List each design document scanned during [SCAN] and [FREEZE]. Minimum one entry.] | Pre-investigation only. Signal artifacts excluded. |
| Signal artifacts excluded | [List each signal artifact by name; confirm not accessed during Step 1.] | Enumerated by name. |
| PBI completeness basis | [One sentence: which material(s) provide the primary PBI basis.] | Single sentence. |

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

**PHASE-HANDOVER-0** (registry entry: EF -> BC):

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
gate token before advancing to the next sub-phase.

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
in the BC-STEP1-PROTOCOL section above (four-field table; no code fence).

BC is now excluded from Steps 2-7.

**PHASE-HANDOVER-1** (registry entry: BC -> IA):

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

**PHASE-HANDOVER-2** (registry entry: IA Step 2 -> IA Step 3):

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

**PHASE-HANDOVER-3** (registry entry: IA Step 3 -> IA Step 4):

| Field | Content |
|-------|---------|
| Completing Role | Institutional Archaeologist (IA) -- Step 3 |
| Step Completed | Step 3 -- Draft All Corrections |
| Output Produced | Draft corrections (all STILL-LIVE candidates) |
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

**PHASE-HANDOVER-4** (registry entry: IA Step 4 -> IA Step 5):

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

**PHASE-HANDOVER-5** (registry entry: IA Step 5 -> IA Step 6):

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

**PHASE-HANDOVER-6** (registry entry: IA Step 6 -> IA Step 7):

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
avoided failure. Makes institutional purpose falsifiable.

**What this correction record excludes:** At least two categories with counts.

---

== ARTIFACT STRUCTURE ============================================================

  1. ENFORCEMENT MECHANISM DECLARATION (EF; NO-ECHO COST)
  2. EF-INVOCATION-RECORD (Step 0)
  3. PHASE-HANDOVER-0 table (EF exit; 5-row schema; registry entry verified)
  4. PBI output (BC; COMMIT-SCAN + COMMIT-FREEZE tokens)
  5. BC-COVERAGE-RECORD (table format; four fields; no code fence)
  6. PHASE-HANDOVER-1 table (BC exit; 5-row schema; registry entry verified)
  7. HANDLE LEDGER output (IA)
  8. PHASE-HANDOVER-2 table (IA Step 2 exit; 5-row schema; registry entry verified)
  9. Corrections -- HIGH -> MEDIUM -> LOW
  10. PHASE-HANDOVER-3 table (IA Step 3 exit; 5-row schema; registry entry verified)
  11. Audited corrections (Register Audit output)
  12. PHASE-HANDOVER-4 table (IA Step 4 exit; 5-row schema; registry entry verified)
  13. Entry Gate blocks (all STATUS: CLEARED)
  14. PHASE-HANDOVER-5 table (IA Step 5 exit; 5-row schema; registry entry verified)
  15. Chain Integrity Audit (all CHAIN-COMPLETE)
  16. PHASE-HANDOVER-6 table (IA Step 6 exit; 5-row schema; registry entry verified)
  17. Rules of Thumb (RULES-ANCHORED-COMPLETE with per-rule tier quotation)
  18. Surprise hierarchy (ranked with rationale)
  19. Pattern of inherited errors
  20. Blind Spot Map
  21. Correction Forward Statement (confirms NO-ECHO COST; names specific avoided failure)
  22. What this correction record excludes

Write to: simulations/topic/echo/{topic}-echo-{YYYY-MM-DD}.md

---

## V-05 -- Axes A-double+B-double+C-double: Full Alternative Combination

**Variation axes:** Lifecycle emphasis (Axis A-double) + Output format (Axis B-double) +
Phrasing register (Axis C-double)

**Hypothesis:** Combining all three R14 axes produces the maximum-scoring variant through
alternative structural implementations. The code-fence-free BC-STEP1-PROTOCOL section
(Axis A-double) satisfies C-37 (sub-phase decomposition) and C-40 (pre-execution standalone
declaration) and C-43 (heading-sovereign, no code-fence entry required for full protocol
content). The roles-embedded phase transition registry (Axis B-double) satisfies C-38
(5-row schema at all exits) and C-41 (universality simultaneously verifiable by inventory
cross-reference) and C-44 (inventory pre-declared before Step 0 within Roles section). The
table-column MUST-clauses (Axis C-double) satisfy C-39 (unconditional imperatives -- no
conditional branching) and C-42 (scope declared per clause body) and C-45 (Scope is a named
column structurally independent from Action -- scope auditable from column header without
parsing the action cell). All three mechanisms target different phases and are structurally
independent. V-05 is the only R14 variation predicted to achieve 275/275 under v14.

**Expected v14 score:** 275 (C-37 PASS; C-38 PASS; C-39 PASS; C-40 PASS; C-41 PASS; C-42 PASS;
C-43 PASS; C-44 PASS; C-45 PASS)

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

#### Phase Transition Registry

Pre-declared registry of all seven phase transitions. Every step exit in Steps 0 through 6
must produce a PHASE-HANDOVER-[N] table matching this registry. This registry is declared
within the Roles section, before Step 0 begins. Universality is verifiable by cross-referencing
the registry rows against the inline PHASE-HANDOVER-[N] tables -- no document traversal needed.
A missing table is detectable as an unchecked registry row.

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

### BC-STEP1-PROTOCOL

Executed by BC during Step 1 in three sequential sub-phases. Write each gate token before
advancing to the next sub-phase. Do not merge sub-phases. This section is the pre-execution
contract for Step 1, positioned before Step 0 begins. The BC Function Declaration references
this section by name; the full protocol -- including the BC-COVERAGE-RECORD schema -- is
expressed here entirely as markdown tables with no code fences. A reviewer reads the complete
protocol specification from heading navigation alone.

| Sub-phase | Scope | Gate Token |
|-----------|-------|------------|
| [SCAN] | Read design materials. List all belief candidates. No pruning or evaluation during this phase. | `COMMIT-SCAN: [N] candidates identified.` |
| [FREEZE] | Produce PBI from scan results. Lock all PB-[NN] entries. No additions after gate token. | `COMMIT-FREEZE: PBI frozen at [N] entries.` |
| [COVERAGE AUDIT] | Audit domain coverage. Produce BC-COVERAGE-RECORD using the schema below. BC exclusion takes effect after this record is written. | BC-COVERAGE-RECORD (schema below). |

#### BC-COVERAGE-RECORD Schema

| Field | Content | Constraint |
|-------|---------|------------|
| Sub-phase | [COVERAGE AUDIT] -- gate declared in BC-STEP1-PROTOCOL. | Fixed; do not substitute. |
| Materials consulted | [List each design document scanned during [SCAN] and [FREEZE]. Minimum one entry.] | Pre-investigation only. Signal artifacts excluded. |
| Signal artifacts excluded | [List each signal artifact by name; confirm not accessed during Step 1.] | Enumerated by name. |
| PBI completeness basis | [One sentence: which material(s) provide the primary PBI basis.] | Single sentence. |

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

**PHASE-HANDOVER-0** (registry entry: EF -> BC):

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
gate token before advancing to the next sub-phase.

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
in the BC-STEP1-PROTOCOL section above (four-field table; no code fence).

BC is now excluded from Steps 2-7.

**PHASE-HANDOVER-1** (registry entry: BC -> IA):

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

**PHASE-HANDOVER-2** (registry entry: IA Step 2 -> IA Step 3):

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

Order: HIGH -> MEDIUM -> LOW.
----------------------------------------------------------------------
```

**STILL-LIVE FILTER -- TABLE-COLUMN MUST-CLAUSE PROTOCOL**

Apply each MUST-clause to every candidate from the Handle Ledger. The table format
declares Scope and Action as separate columns: the entity class governed by each MUST-clause
is readable from the Scope column without parsing the Action column. Each MUST-clause is
unconditional -- no candidate evaluation concludes without all four MUST-clauses applied.

| MUST-ID | Scope | Action | Constraint |
|---------|-------|--------|------------|
| MUST-1 | EVERY CANDIDATE -- no exceptions | Produce exactly one of: `STILL-LIVE-[N]: [candidate name]` OR `DISCARD-[N]: [candidate name]` | No candidate evaluation concludes without one of these tokens. No candidate is exempt. |
| MUST-2 | EVERY DISCARD-[N] TOKEN -- no exceptions | Immediately write: `DISCARD-[N]-PBI-REF: PB-[NN]` -- names the prior belief this candidate was tested against | A DISCARD token without a PBI-Ref token is malformed. No DISCARD is exempt. |
| MUST-3 | EVERY DISCARD-[N] TOKEN -- no exceptions | Immediately write: `DISCARD-[N]-ROUTE: [destination -- topic-story or named skill]` -- states where excluded candidates are recorded | A DISCARD token without a ROUTE token is malformed. No DISCARD is exempt. |
| MUST-4 | EVERY DISCARD-[N] TOKEN -- no exceptions | Immediately write: `DISCARD-[N]-REASON: [one sentence -- specific exclusion reason]` -- states why this candidate fails the STILL-LIVE test | A DISCARD token without a REASON token is malformed. No DISCARD is exempt. |

Completeness gate: After all candidates are processed, write:
`DISCARD-LOG-COMPLETE: [N] STILL-LIVE, [M] DISCARD -- all four MUST-clauses applied to every candidate; no candidate unresolved.`

**PHASE-HANDOVER-3** (registry entry: IA Step 3 -> IA Step 4):

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

**PHASE-HANDOVER-4** (registry entry: IA Step 4 -> IA Step 5):

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

**PHASE-HANDOVER-5** (registry entry: IA Step 5 -> IA Step 6):

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

**PHASE-HANDOVER-6** (registry entry: IA Step 6 -> IA Step 7):

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
  3. PHASE-HANDOVER-0 table (EF exit; 5-row schema; registry entry verified)
  4. PBI output (BC; COMMIT-SCAN + COMMIT-FREEZE tokens present)
  5. BC-COVERAGE-RECORD (table format; four fields; no code fence; [COVERAGE AUDIT] gate)
  6. PHASE-HANDOVER-1 table (BC exit; 5-row schema; registry entry verified)
  7. HANDLE LEDGER output (IA)
  8. PHASE-HANDOVER-2 table (IA Step 2 exit; 5-row schema; registry entry verified)
  9. STILL-LIVE FILTER table output (MUST-ID / Scope / Action / Constraint columns):
     STILL-LIVE-[N] and DISCARD-[N] tokens; each DISCARD followed immediately by
     PBI-REF / ROUTE / REASON tokens; DISCARD-LOG-COMPLETE
  10. Corrections -- HIGH -> MEDIUM -> LOW
  11. PHASE-HANDOVER-3 table (IA Step 3 exit; 5-row schema; registry entry verified)
  12. Audited corrections (Register Audit output)
  13. PHASE-HANDOVER-4 table (IA Step 4 exit; 5-row schema; registry entry verified)
  14. Entry Gate blocks (all STATUS: CLEARED)
  15. PHASE-HANDOVER-5 table (IA Step 5 exit; 5-row schema; registry entry verified)
  16. Chain Integrity Audit (all CHAIN-COMPLETE)
  17. PHASE-HANDOVER-6 table (IA Step 6 exit; 5-row schema; registry entry verified)
  18. Rules of Thumb (RULES-ANCHORED-COMPLETE with per-rule tier quotation)
  19. Surprise hierarchy (ranked with rationale)
  20. Pattern of inherited errors
  21. Blind Spot Map
  22. Correction Forward Statement (confirms NO-ECHO COST; names specific avoided failure)
  23. What this correction record excludes

Write to: simulations/topic/echo/{topic}-echo-{YYYY-MM-DD}.md
