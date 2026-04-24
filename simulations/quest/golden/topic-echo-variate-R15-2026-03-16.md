---
skill: quest-variate
skill_target: topic-echo
date: 2026-03-16
round: 15
rubric: v15
rubric_file: simulations/quest/rubrics/topic-echo-rubric-v15-2026-03-16.md
rubric_max: 290
---

# Variations: `topic:echo` -- Round 15 (2026-03-16)

**Rubric:** v15 (2026-03-16) | **Criteria:** 48 (5 essential / 3 recommended / 40 aspirational)

---

## Design Context

R14 V-05 achieves 290/290 under v15. The three addressability criteria formalized in v15 --
BC-COVERAGE-RECORD-SCHEMA-HEADING-SOVEREIGNTY (C-46), INVENTORY-GOVERNANCE-COLLOCATION (C-47),
and MUST-CLAUSE-ID-ADDRESSABILITY (C-48) -- are satisfied by R14's alternative structural
implementations. Round 15 does not re-implement R14's axes. It tests whether adding explicit
**citation activation** to each R14 address creates observable structural properties that could
become v16 criteria.

R14 made sub-elements independently addressable: the schema within BC-STEP1-PROTOCOL gets a
sub-heading (C-46); the inventory is co-located with governance (C-47); each MUST-clause
carries a stable MUST-ID (C-48). Each address is passive -- it exists and is navigable, but
is not explicitly cited by the artifact sections that consume it.

R15 tests the **citation layer**: addresses exist (R14). Do addresses become active when their
consuming contexts cite them by ID (R15)? Three axes, one per R14 address type:

- **Axis A (Schema field-ID citation)**: BC-COVERAGE-RECORD Schema fields (C-46 sub-heading)
  carry named field-IDs (F-BCR-1 through F-BCR-4). The BC-COVERAGE-RECORD output table headers
  prefix each field with its schema ID. The schema address is activated in the output that
  consumes it: a reviewer can confirm "F-BCR-2: Materials consulted" in the output matches the
  F-BCR-2 declaration in the schema -- without reading surrounding prose in either location.

- **Axis B (Transition-ID registry citation)**: The Phase Transition Registry (inside Roles
  per C-47) assigns a Transition-ID (T-00 through T-06) to each row. Each inline PHASE-
  HANDOVER-[N] table includes a 6th row `Registry-Ref` citing its T-ID. The inventory address
  is activated in each table that checks against it: a reviewer can confirm "Registry-Ref: T-02"
  in an inline table matches "T-02 | PHASE-HANDOVER-2 | ..." in the registry -- without
  traversing the document to find the corresponding row.

- **Axis C (MUST-clause belief-ref citation)**: Each MUST-clause in the STILL-LIVE FILTER
  table (MUST-ID per C-48) carries a 5th column `Belief-Ref` (PB-[NN]) naming the prior
  belief that motivated this enforcement clause. The MUST-ID address is activated by its
  epistemic anchor: a reviewer reading MUST-3 can immediately look up which PBI entry this
  clause enforces, and a reviewer reading PB-03 can find which MUST-clause enforces it --
  from table cells alone, without consulting surrounding prose.

R14 implementations and R15 citation activations:

- **C-46 (BC-COVERAGE-RECORD-SCHEMA-HEADING-SOVEREIGNTY)** -> **Axis A: Schema field-ID
  citation**: R14 V-01 placed `#### BC-COVERAGE-RECORD Schema` as a navigable sub-heading
  under `### BC-STEP1-PROTOCOL`, with field definitions in a markdown table. The sub-heading
  exists and is navigable. R15 V-01 adds named field-IDs (F-BCR-1..F-BCR-4) as the first
  column of the schema table, and instructs BC to prefix each field header in the BC-COVERAGE-
  RECORD output with its schema ID. The schema now has two structural layers: sub-heading
  navigability (C-46, from R14) and field-ID citation (Axis A, R15). C-46 is preserved; the
  field-ID citation layer is additive.

- **C-47 (INVENTORY-GOVERNANCE-COLLOCATION)** -> **Axis B: Transition-ID registry citation**:
  R14 V-02 embedded the Phase Transition Registry as `#### Phase Transition Registry` inside
  the Roles section -- inventory and governance co-located. The registry lists seven transitions
  by identity. R15 V-02 adds a Transition-ID column (T-00..T-06) to the registry, and adds a
  6th row `Registry-Ref` to the Phase Handover Schema. Each inline PHASE-HANDOVER-[N] table
  cites its T-ID in the Registry-Ref row. C-47 is preserved; the citation activation layer is
  additive.

- **C-48 (MUST-CLAUSE-ID-ADDRESSABILITY)** -> **Axis C: MUST-clause belief-ref citation**:
  R14 V-03 expressed MUST-clauses as a 4-column table (MUST-ID | Scope | Action | Constraint),
  each clause citable by MUST-ID without reading any field. R15 V-03 adds a 5th column
  Belief-Ref (PB-[NN]) naming the prior belief that motivated each clause. C-48 is preserved;
  the belief-ref column is additive and enables bidirectional lookup between beliefs and the
  enforcement clauses that guard them.

**R15 progression layer:** R14 demonstrated that stable addresses (sub-headings, registry rows,
MUST-IDs) reliably trigger C-46/C-47/C-48. R15 tests whether citation activation -- consuming
contexts explicitly citing addresses by ID -- creates a new structural property class. If it
does, the three axes become three candidate criteria for v16, and V-05 (all three combined)
demonstrates the full citation-activated artifact in a single runnable prompt.

**Predicted scoring under v15 (all 5 variations inherit R14 V-05's full structure):**

| Variation | C-46 | C-47 | C-48 | v15 | v16 (projected) | delta |
|-----------|:----:|:----:|:----:|:---:|:---------------:|:-----:|
| V-01 (Axis A) | PASS | PASS | PASS | 290 | 295 | +5 |
| V-02 (Axis B) | PASS | PASS | PASS | 290 | 295 | +5 |
| V-03 (Axis C) | PASS | PASS | PASS | 290 | 295 | +5 |
| V-04 (A+B) | PASS | PASS | PASS | 290 | 300 | +10 |
| **V-05 (A+B+C)** | PASS | PASS | PASS | 290 | **305** | +15 |

**Excellence signals under v15:** All five variations score 290/290. The differentiating
signals are the citation-activation structures -- schema F-IDs in output headers (Axis A),
T-IDs in PHASE-HANDOVER Registry-Ref rows (Axis B), MUST Belief-Ref column (Axis C) -- which
produce observable structural differences the current rubric cannot score but a reviewer can
identify as candidate C-49/C-50/C-51 patterns.

---

## V-01 -- Axis A: Schema Field-ID Citation

**Variation axis:** Lifecycle emphasis -- BC-COVERAGE-RECORD Schema fields carry named
field-IDs (F-BCR-1 through F-BCR-4); BC-COVERAGE-RECORD output headers cite these IDs;
schema addresses are activated in the consuming output (Axis A only)

**Hypothesis:** R14's C-46 made the schema navigable via sub-heading: a reviewer can jump to
`#### BC-COVERAGE-RECORD Schema` without reading the protocol table. The schema exists and
is findable. R15 V-01 asks whether the schema should also be *citable from its output*: when
BC produces a BC-COVERAGE-RECORD, each output field header carries its schema ID (e.g.,
"F-BCR-2: Materials consulted"). A reviewer confirming a BC-COVERAGE-RECORD entry can verify
against the schema without consulting surrounding prose in either section -- the ID in the
output points to the ID in the schema directly. This tests whether schema-address activation
in the consuming output is a distinct observable structural property from schema-address
navigability in the declaring section.

**Expected v15 score:** 290 (C-01 through C-48: all PASS -- inherits full R14 V-05 structure)
**Projected v16 excellence signal:** Axis A activates schema field addresses from output;
candidate criterion: BC-COVERAGE-RECORD output headers cite schema field-IDs from the C-46
sub-heading, enabling schema-to-output address verification without traversal.

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
              Each IA stage exit (Steps 2-6) produces a PHASE-
              HANDOVER-[N] table before advancing to the next step.
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

Each field carries a named field-ID (F-BCR-1 through F-BCR-4). When producing the
BC-COVERAGE-RECORD output, prefix each field header with its schema ID -- for example,
write "F-BCR-2: Materials consulted" rather than "Materials consulted". This activates
the schema address in the output: a reviewer can match any BC-COVERAGE-RECORD field to
its schema declaration by field-ID alone, without reading surrounding prose in either section.

| F-ID | Field | Content | Constraint |
|------|-------|---------|------------|
| F-BCR-1 | Sub-phase | [COVERAGE AUDIT] -- gate declared in BC-STEP1-PROTOCOL. | Fixed; do not substitute. |
| F-BCR-2 | Materials consulted | [List each design document scanned during [SCAN] and [FREEZE]. Minimum one entry.] | Pre-investigation only. Signal artifacts excluded. |
| F-BCR-3 | Signal artifacts excluded | [List each signal artifact by name; confirm not accessed during Step 1.] | Enumerated by name. "none" not acceptable if signals exist. |
| F-BCR-4 | PBI completeness basis | [One sentence: which material(s) provide the primary PBI basis.] | Single sentence. Reviewable from this field alone. |

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
in the BC-STEP1-PROTOCOL section above. Format the output table with schema field-IDs in each
header (F-BCR-1: Sub-phase / F-BCR-2: Materials consulted / F-BCR-3: Signal artifacts excluded
/ F-BCR-4: PBI completeness basis). No code fence.

BC is now excluded from Steps 2-7.

**PHASE-HANDOVER-1** (registry entry: BC -> IA):

| Field | Content |
|-------|---------|
| Completing Role | Belief Cartographer (BC) -- Step 1 |
| Step Completed | Step 1 -- Belief Inventory and Coverage Audit |
| Output Produced | PBI (all PB-[NN] frozen) + BC-COVERAGE-RECORD (F-BCR field-IDs in headers) |
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

Apply each MUST-clause to every candidate from the Handle Ledger. Scope and Action are
separate columns: the entity class governed by each clause is readable from the Scope
column without parsing the Action column. Each MUST-clause is unconditional -- no candidate
evaluation concludes without all four MUST-clauses applied.

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

  1. ENFORCEMENT MECHANISM DECLARATION (EF; NO-ECHO COST)
  2. EF-INVOCATION-RECORD (Step 0)
  3. PHASE-HANDOVER-0 table (EF exit; 5-row schema; registry entry verified)
  4. PBI output (BC; COMMIT-SCAN + COMMIT-FREEZE tokens present)
  5. BC-COVERAGE-RECORD (F-BCR field-IDs in all headers; table format; no code fence)
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

## V-02 -- Axis B: Transition-ID Registry Citation

**Variation axis:** Output format -- the Phase Transition Registry (inside Roles per C-47)
assigns Transition-IDs (T-00 through T-06) to each row; each inline PHASE-HANDOVER-[N]
table includes a 6th row Registry-Ref citing its T-ID (Axis B only)

**Hypothesis:** R14's C-47 made the Phase Transition Registry co-located with governance:
both role-scope declarations and the expected transition set are in a single navigable unit
inside the Roles section. The registry lists all seven transitions before execution. R15 V-02
asks whether the registry should also be *activated by inline citation*: when a PHASE-HANDOVER-
[N] table is produced, it cites its T-ID in a Registry-Ref row, creating a bidirectional link.
A reviewer verifying coverage can check: the registry declares T-02 = PHASE-HANDOVER-2; the
inline PHASE-HANDOVER-2 table cites T-02 in its Registry-Ref row. The match is verifiable
from cell values alone, without traversal. This tests whether registry-address activation
in each consuming table is distinct from registry collocation with governance (C-47).

**Expected v15 score:** 290 (C-01 through C-48: all PASS -- inherits full R14 V-05 structure)
**Projected v16 excellence signal:** Axis B activates registry transition addresses from
inline tables; candidate criterion: each PHASE-HANDOVER-[N] table cites its Transition-ID
from the C-47 Phase Transition Registry, enabling cross-reference verification from cell
values alone.

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
              Each IA stage exit (Steps 2-6) produces a PHASE-
              HANDOVER-[N] table before advancing to the next step.
Input:        Signal artifacts + frozen PBI (read-only).
Out-of-scope: PBI authorship (frozen). Enforcement section (immutable).
Orienting:    "What would the next team build wrong?"
Phase scope:  Steps 2-7 only.
----------------------------------------------------------------------
```

**Phase Handover Schema (universal -- all 7 exits, Steps 0-6):**

All PHASE-HANDOVER-[N] tables use this schema exactly. Six rows. Fixed field names.
Do not substitute prose. Do not add or remove rows. The Registry-Ref row cites the
Transition-ID from the Phase Transition Registry below, activating the registry address
in each consuming table.

| Field | Content |
|-------|---------|
| Completing Role | [role name and step number] |
| Step Completed | [step number and name] |
| Output Produced | [artifact(s) produced at this exit] |
| Exclusion In Effect | [what the completing role/phase can no longer modify] |
| Receiving Role | [role name and step number taking control] |
| Registry-Ref | [T-NN -- the Transition-ID from the Phase Transition Registry that matches this table] |

#### Phase Transition Registry

Pre-declared registry of all seven phase transitions. Every step exit in Steps 0 through 6
must produce a PHASE-HANDOVER-[N] table matching this registry. This registry is declared
within the Roles section, before Step 0 begins. Each row carries a Transition-ID (T-NN):
the inline PHASE-HANDOVER-[N] table for that exit cites the T-NN in its Registry-Ref row,
creating a cell-level link between the registry declaration and each consuming table.
Universality is verifiable by cross-referencing T-IDs in the registry against Registry-Ref
values in the inline tables -- no traversal required.

| T-ID | Transition | Step Completed | Completing Role | Receiving Role |
|------|------------|----------------|-----------------|----------------|
| T-00 | PHASE-HANDOVER-0 | Step 0 -- Enforcement Section and Invocation Record | Enforcement Framer (EF) | Belief Cartographer (BC) |
| T-01 | PHASE-HANDOVER-1 | Step 1 -- Belief Inventory and Coverage Audit | Belief Cartographer (BC) | Institutional Archaeologist (IA) |
| T-02 | PHASE-HANDOVER-2 | Step 2 -- Handle Ledger | Institutional Archaeologist (IA) | Institutional Archaeologist (IA) |
| T-03 | PHASE-HANDOVER-3 | Step 3 -- Draft All Corrections | Institutional Archaeologist (IA) | Institutional Archaeologist (IA) |
| T-04 | PHASE-HANDOVER-4 | Step 4 -- Register Audit | Institutional Archaeologist (IA) | Institutional Archaeologist (IA) |
| T-05 | PHASE-HANDOVER-5 | Step 5 -- Entry Gate | Institutional Archaeologist (IA) | Institutional Archaeologist (IA) |
| T-06 | PHASE-HANDOVER-6 | Step 6 -- Chain Integrity Audit | Institutional Archaeologist (IA) | Institutional Archaeologist (IA) |

---

### BC-STEP1-PROTOCOL

Executed by BC during Step 1 in three sequential sub-phases. Write each gate token before
advancing to the next sub-phase. Do not merge sub-phases. This section is the pre-execution
contract for Step 1, positioned before Step 0 begins. Expressed entirely as markdown tables
with no code fences. A reviewer reads the complete protocol from heading navigation alone.

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
  Named failure class required. Generic statements fail.]
----------------------------------------------------------------------
```

```
EF-INVOCATION-RECORD
----------------------------------------------------------------------
Step:       0 (EF phase; signal-reading phase not yet open)
Materials consulted (pre-investigation only):
  [List each design document consulted. Minimum one entry.]
Signal artifacts excluded:
  [List each signal artifact by name; confirm not accessed at Step 0.]
Cost derivation basis:
  [One sentence: which material grounded the NO-ECHO COST claim.]
----------------------------------------------------------------------
```

**PHASE-HANDOVER-0** (registry entry T-00: EF -> BC):

| Field | Content |
|-------|---------|
| Completing Role | Enforcement Framer (EF) -- Step 0 |
| Step Completed | Step 0 -- Enforcement Section and Invocation Record |
| Output Produced | ENFORCEMENT MECHANISM DECLARATION + EF-INVOCATION-RECORD |
| Exclusion In Effect | EF excluded from Steps 1-7; signal artifacts not accessed at Step 0 |
| Receiving Role | Belief Cartographer (BC) -- Step 1 |
| Registry-Ref | T-00 |

---

### Step 1 -- [BC] Belief Inventory and Coverage Audit

Execute BC-STEP1-PROTOCOL as declared in the BC-STEP1-PROTOCOL section above.

**[SCAN]** Read all design materials within BC's input scope. Signal artifacts out of scope.
Identify every belief candidate.

`COMMIT-SCAN: [N] candidates identified.`

**[FREEZE]** Produce the PBI from the scanned candidates.

```
PBI PRODUCTION PROTOCOL
----------------------------------------------------------------------
Input:    Design materials only. Signal artifacts excluded.
Format:   PB-[NN]: ["Today's materials imply that X."]
Freeze:   PBI frozen after COMMIT-FREEZE. No new PB-[NN] after this
          point. No handle labels in PBI entries.
----------------------------------------------------------------------
```

`COMMIT-FREEZE: PBI frozen at [N] entries.`

**[COVERAGE AUDIT]** Produce BC-COVERAGE-RECORD (four-field table; no code fence).

BC is now excluded from Steps 2-7.

**PHASE-HANDOVER-1** (registry entry T-01: BC -> IA):

| Field | Content |
|-------|---------|
| Completing Role | Belief Cartographer (BC) -- Step 1 |
| Step Completed | Step 1 -- Belief Inventory and Coverage Audit |
| Output Produced | PBI (all PB-[NN] frozen) + BC-COVERAGE-RECORD ([COVERAGE AUDIT] gate) |
| Exclusion In Effect | BC excluded from Steps 2-7; PBI frozen; no additions after this table |
| Receiving Role | Institutional Archaeologist (IA) -- Step 2 |
| Registry-Ref | T-01 |

---

### Step 2 -- [IA] Handle Ledger

```
HANDLE LEDGER PROTOCOL
----------------------------------------------------------------------
Timing:   After reading all signal artifacts. Before writing corrections.
Format:   HL-[NN]: [finding-specific label -- 2-5 words; finding language]
Test:     No PBI entry names its handle. No HL entry echoes a PBI
          entry verbatim. Either violation is a phase contract failure.
----------------------------------------------------------------------
```

**PHASE-HANDOVER-2** (registry entry T-02: IA Step 2 -> IA Step 3):

| Field | Content |
|-------|---------|
| Completing Role | Institutional Archaeologist (IA) -- Step 2 |
| Step Completed | Step 2 -- Handle Ledger |
| Output Produced | HANDLE LEDGER (all HL-[NN] entries complete) |
| Exclusion In Effect | No new handles may be coined after Step 3 begins |
| Receiving Role | Institutional Archaeologist (IA) -- Step 3 |
| Registry-Ref | T-02 |

---

### Step 3 -- [IA] Draft All Corrections

```
CORRECTION RECORD SCHEMA
----------------------------------------------------------------------
Fields (all required):
  Name / PBI-Ref / Source / Implies / Showed / Wrong / Decide /
  Verified / Severity (HIGH / MEDIUM / LOW)
Order: HIGH -> MEDIUM -> LOW.
----------------------------------------------------------------------
```

**STILL-LIVE FILTER -- TABLE-COLUMN MUST-CLAUSE PROTOCOL**

| MUST-ID | Scope | Action | Constraint |
|---------|-------|--------|------------|
| MUST-1 | EVERY CANDIDATE -- no exceptions | Produce exactly one of: `STILL-LIVE-[N]: [candidate name]` OR `DISCARD-[N]: [candidate name]` | No candidate evaluation concludes without one of these tokens. No candidate is exempt. |
| MUST-2 | EVERY DISCARD-[N] TOKEN -- no exceptions | Immediately write: `DISCARD-[N]-PBI-REF: PB-[NN]` | A DISCARD token without a PBI-Ref token is malformed. |
| MUST-3 | EVERY DISCARD-[N] TOKEN -- no exceptions | Immediately write: `DISCARD-[N]-ROUTE: [destination]` | A DISCARD token without a ROUTE token is malformed. |
| MUST-4 | EVERY DISCARD-[N] TOKEN -- no exceptions | Immediately write: `DISCARD-[N]-REASON: [one sentence]` | A DISCARD token without a REASON token is malformed. |

`DISCARD-LOG-COMPLETE: [N] STILL-LIVE, [M] DISCARD -- all four MUST-clauses applied to every candidate; no candidate unresolved.`

**PHASE-HANDOVER-3** (registry entry T-03: IA Step 3 -> IA Step 4):

| Field | Content |
|-------|---------|
| Completing Role | Institutional Archaeologist (IA) -- Step 3 |
| Step Completed | Step 3 -- Draft All Corrections |
| Output Produced | Draft corrections + STILL-LIVE FILTER output (DISCARD-LOG-COMPLETE) |
| Exclusion In Effect | No new entries or DISCARD tokens may be added after Step 4 begins |
| Receiving Role | Institutional Archaeologist (IA) -- Step 4 |
| Registry-Ref | T-03 |

---

### Step 4 -- Register Audit

```
REGISTER AUDIT PROTOCOL
----------------------------------------------------------------------
Execute field by field before Step 5. Rewrite any field in discovery
register: Source / Implies / Wrong / Decide / Verified.
----------------------------------------------------------------------
```

**PHASE-HANDOVER-4** (registry entry T-04: IA Step 4 -> IA Step 5):

| Field | Content |
|-------|---------|
| Completing Role | Institutional Archaeologist (IA) -- Step 4 |
| Step Completed | Step 4 -- Register Audit |
| Output Produced | Audited correction entries (all fields rewritten per protocol) |
| Exclusion In Effect | Field rewrites locked; no further changes outside Step 5 gate |
| Receiving Role | Institutional Archaeologist (IA) -- Step 5 |
| Registry-Ref | T-04 |

---

### Step 5 -- Entry Gate

```
ENTRY GATE DECLARATION
----------------------------------------------------------------------
Fields:   PBI-Ref / Source / Implies / Showed / Wrong / Decide / Verified
Result:   PASS / FAIL per field
Status:   STATUS: CLEARED / STATUS: NOT CLEARED
Gate:     NOT CLEARED halts progression.
----------------------------------------------------------------------
```

Do not proceed to Step 6 until every entry CLEARED.

**PHASE-HANDOVER-5** (registry entry T-05: IA Step 5 -> IA Step 6):

| Field | Content |
|-------|---------|
| Completing Role | Institutional Archaeologist (IA) -- Step 5 |
| Step Completed | Step 5 -- Entry Gate |
| Output Produced | Per-entry STATUS: CLEARED tokens (all entries) |
| Exclusion In Effect | No field changes permitted after all entries CLEARED |
| Receiving Role | Institutional Archaeologist (IA) -- Step 6 |
| Registry-Ref | T-05 |

---

### Step 6 -- Chain Integrity Audit

```
CHAIN INTEGRITY AUDIT DECLARATION
----------------------------------------------------------------------
Elements: [1] PBI-Ref correct (quote PBI text)
          [2] Handle matches HL (quote HL title)
          [3] Source resolvable
          [4] Verified quotation is actual text
Token:    CHAIN-COMPLETE / CHAIN-FLAG per entry
Gate:     CHAIN-FLAG IS A HARD GATE.
----------------------------------------------------------------------
```

```
RESOLUTION PROTOCOL DECLARATION
----------------------------------------------------------------------
  PBI-Ref mismatch: Repair + BC Verifier.
  Handle mismatch: Repair + IA Verifier.
  Source absent: Repair + IA Verifier.
  Verified inaccurate: Repair + IA Verifier.
----------------------------------------------------------------------
```

Do not proceed to Step 7 until every entry CHAIN-COMPLETE.

**PHASE-HANDOVER-6** (registry entry T-06: IA Step 6 -> IA Step 7):

| Field | Content |
|-------|---------|
| Completing Role | Institutional Archaeologist (IA) -- Step 6 |
| Step Completed | Step 6 -- Chain Integrity Audit |
| Output Produced | Per-entry CHAIN-COMPLETE tokens; Resolution Protocol trace if flagged |
| Exclusion In Effect | No chain repairs permitted after all entries CHAIN-COMPLETE |
| Receiving Role | Institutional Archaeologist (IA) -- Step 7 |
| Registry-Ref | T-06 |

---

### Step 7 -- [IA] Hierarchy, Distillation, and Forward Handover

**Surprise hierarchy:** Ranked by design impact. Argued rationale.

**Rules of Thumb:**

```
RULES OF THUMB DECLARATION
----------------------------------------------------------------------
Scope:  HIGH and MEDIUM only. Format: [TIER] {Rule <=20 words} (encodes: name)
Check:  RULES-ANCHORED -- tier must match parent Severity.
Gate:   BLOCKS on MISALIGNED.
Closure: RULES-ANCHORED-COMPLETE: R-01 "[TIER]" ALIGNED, ... -- closed.
----------------------------------------------------------------------
```

RULES-ANCHORED check and closure token.

**Pattern of inherited errors / Blind Spot Map / Correction Forward Statement /
What this correction record excludes** -- as specified above.

---

== ARTIFACT STRUCTURE ============================================================

  1-2. ENFORCEMENT MECHANISM + EF-INVOCATION-RECORD
  3. PHASE-HANDOVER-0 (6-row; Registry-Ref: T-00)
  4-5. PBI + BC-COVERAGE-RECORD
  6. PHASE-HANDOVER-1 (6-row; Registry-Ref: T-01)
  7. HANDLE LEDGER
  8. PHASE-HANDOVER-2 (6-row; Registry-Ref: T-02)
  9. Corrections HIGH -> MEDIUM -> LOW
  10. PHASE-HANDOVER-3 (6-row; Registry-Ref: T-03)
  11. Audited corrections
  12. PHASE-HANDOVER-4 (6-row; Registry-Ref: T-04)
  13. Entry Gate blocks (all CLEARED)
  14. PHASE-HANDOVER-5 (6-row; Registry-Ref: T-05)
  15. Chain Integrity Audit (all CHAIN-COMPLETE)
  16. PHASE-HANDOVER-6 (6-row; Registry-Ref: T-06)
  17-22. Rules of Thumb / Hierarchy / Pattern / Blind Spot / Forward Statement / Exclusions

Write to: simulations/topic/echo/{topic}-echo-{YYYY-MM-DD}.md

---

## V-03 -- Axis C: MUST-Clause Belief-Ref Citation

**Variation axis:** Phrasing register -- STILL-LIVE FILTER table adds a 5th column
Belief-Ref (PB-[NN]) to each MUST-clause, naming the prior belief the clause enforces;
MUST-ID addresses are activated by their epistemic anchor (Axis C only)

**Hypothesis:** R14's C-48 made MUST-clauses identifiable by MUST-ID: a future artifact can
cite "MUST-3" without reading Scope or Action. The ID enables forward lookup (find the clause).
R15 V-03 asks whether MUST-clauses should also declare their epistemic motivation: a Belief-Ref
column (PB-[NN]) names which prior belief each clause is guarding. This enables backward lookup
(find the belief) and bidirectional lookup (which MUST-clauses enforce B-03? which belief
motivates MUST-2?). A reviewer reading the STILL-LIVE FILTER table can answer both questions
from column cells alone. This tests whether belief-ref citation in enforcement clauses is a
distinct observable property from MUST-ID addressability (C-48).

**Expected v15 score:** 290 (C-01 through C-48: all PASS -- inherits full R14 V-05 structure)
**Projected v16 excellence signal:** Axis C activates MUST-ID addresses with belief anchors;
candidate criterion: each MUST-clause in the STILL-LIVE FILTER carries a Belief-Ref column
naming the PB-[NN] it enforces, enabling bidirectional belief-to-clause lookup from table cells.

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
Phase scope:  Step 0 only. EF excluded from Steps 1-7.
Gate return:  ENFORCEMENT MECHANISM + EF-INVOCATION-RECORD +
              PHASE-HANDOVER-0 before Step 1.
----------------------------------------------------------------------
```

**Belief Cartographer (BC)** -- Step 1 exclusively.

```
BELIEF CARTOGRAPHER -- FUNCTION DECLARATION
----------------------------------------------------------------------
Function:     Pre-investigation belief recovery. Three sub-phases per
              BC-STEP1-PROTOCOL section below. Write gate token before
              advancing each sub-phase.
Input:        Design materials only. Signal artifacts out of scope.
Phase scope:  Step 1 only. BC excluded from Steps 2-7 after [COVERAGE
              AUDIT] gate token.
Gate return:  PBI frozen + BC-COVERAGE-RECORD + PHASE-HANDOVER-1.
----------------------------------------------------------------------
```

**Institutional Archaeologist (IA)** -- Steps 2-7.

```
INSTITUTIONAL ARCHAEOLOGIST -- FUNCTION DECLARATION
----------------------------------------------------------------------
Function:     False-assumption recovery. Correction register only.
              Each stage exit (Steps 2-6) produces PHASE-HANDOVER-[N].
Input:        Signal artifacts + frozen PBI (read-only).
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

#### Phase Transition Registry

Pre-declared registry of all seven phase transitions, inside the Roles section before Step 0.
Universality verifiable by cross-referencing registry rows against inline PHASE-HANDOVER-[N]
tables. A missing table is detectable as an unchecked registry row.

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

Executed by BC during Step 1 in three sequential sub-phases. Pre-execution contract declared
before Step 0. Expressed as markdown tables with no code fences; readable from heading
navigation alone.

| Sub-phase | Scope | Gate Token |
|-----------|-------|------------|
| [SCAN] | Read design materials. List belief candidates. No pruning. | `COMMIT-SCAN: [N] candidates identified.` |
| [FREEZE] | Produce PBI. Lock all PB-[NN] entries. | `COMMIT-FREEZE: PBI frozen at [N] entries.` |
| [COVERAGE AUDIT] | Audit coverage. Produce BC-COVERAGE-RECORD. BC exclusion takes effect. | BC-COVERAGE-RECORD (schema below). |

#### BC-COVERAGE-RECORD Schema

| Field | Content | Constraint |
|-------|---------|------------|
| Sub-phase | [COVERAGE AUDIT] | Fixed. |
| Materials consulted | [List design documents. Minimum one.] | Pre-investigation only. |
| Signal artifacts excluded | [List by name; confirm not accessed.] | Enumerated by name. |
| PBI completeness basis | [One sentence: primary PBI basis.] | Single sentence. |

---

### Step 0 -- [EF] Enforcement Section and Invocation Record

```
ENFORCEMENT MECHANISM DECLARATION
----------------------------------------------------------------------
Provenance tier: STRUCTURAL
Distinguishing property: Role-scope exclusion at three phase boundaries.
Reviewer implication: Independence enforced by role boundary.
NO-ECHO COST: [Named failure class from design materials. Generic fails.]
----------------------------------------------------------------------
```

```
EF-INVOCATION-RECORD
----------------------------------------------------------------------
Step:       0
Materials consulted: [pre-investigation sources; minimum one]
Signal artifacts excluded: [by name; confirm not accessed at Step 0]
Cost derivation basis: [one sentence; reviewable from this field alone]
----------------------------------------------------------------------
```

**PHASE-HANDOVER-0** (registry entry: EF -> BC):

| Field | Content |
|-------|---------|
| Completing Role | Enforcement Framer (EF) -- Step 0 |
| Step Completed | Step 0 -- Enforcement Section and Invocation Record |
| Output Produced | ENFORCEMENT MECHANISM DECLARATION + EF-INVOCATION-RECORD |
| Exclusion In Effect | EF excluded from Steps 1-7 |
| Receiving Role | Belief Cartographer (BC) -- Step 1 |

---

### Step 1 -- [BC] Belief Inventory and Coverage Audit

**[SCAN]** `COMMIT-SCAN: [N] candidates identified.`

**[FREEZE]**

```
PBI PRODUCTION PROTOCOL
----------------------------------------------------------------------
Format: PB-[NN]: ["Today's materials imply that X."]
Freeze: after COMMIT-FREEZE. No handle labels.
----------------------------------------------------------------------
```

`COMMIT-FREEZE: PBI frozen at [N] entries.`

**[COVERAGE AUDIT]** Produce BC-COVERAGE-RECORD (four-field table; no code fence).

**PHASE-HANDOVER-1** (registry entry: BC -> IA):

| Field | Content |
|-------|---------|
| Completing Role | Belief Cartographer (BC) -- Step 1 |
| Step Completed | Step 1 -- Belief Inventory and Coverage Audit |
| Output Produced | PBI (all PB-[NN] frozen) + BC-COVERAGE-RECORD |
| Exclusion In Effect | BC excluded from Steps 2-7; PBI frozen |
| Receiving Role | Institutional Archaeologist (IA) -- Step 2 |

---

### Step 2 -- [IA] Handle Ledger

```
HANDLE LEDGER PROTOCOL
----------------------------------------------------------------------
Format: HL-[NN]: [2-5 words; finding language]
Test:   No PBI entry names its handle. No HL echoes PBI verbatim.
----------------------------------------------------------------------
```

**PHASE-HANDOVER-2** (registry entry: IA Step 2 -> IA Step 3):

| Field | Content |
|-------|---------|
| Completing Role | Institutional Archaeologist (IA) -- Step 2 |
| Step Completed | Step 2 -- Handle Ledger |
| Output Produced | HANDLE LEDGER (all HL-[NN] complete) |
| Exclusion In Effect | No new handles after Step 3 begins |
| Receiving Role | Institutional Archaeologist (IA) -- Step 3 |

---

### Step 3 -- [IA] Draft All Corrections

```
CORRECTION RECORD SCHEMA
----------------------------------------------------------------------
Fields: Name / PBI-Ref / Source / Implies / Showed / Wrong / Decide /
        Verified / Severity (HIGH / MEDIUM / LOW)
Order: HIGH -> MEDIUM -> LOW.
----------------------------------------------------------------------
```

**STILL-LIVE FILTER -- BELIEF-REF MUST-CLAUSE PROTOCOL**

Apply each MUST-clause to every candidate from the Handle Ledger. Scope and Action are
separate columns. The Belief-Ref column names which prior belief (PB-[NN]) each clause
enforces, enabling bidirectional lookup: which clause enforces PB-03? which belief motivates
MUST-2? Both questions are answerable from column cells alone, without reading surrounding
prose. Each MUST-clause is unconditional -- no candidate evaluation skips any clause.

| MUST-ID | Scope | Action | Constraint | Belief-Ref |
|---------|-------|--------|------------|------------|
| MUST-1 | EVERY CANDIDATE -- no exceptions | Produce exactly one of: `STILL-LIVE-[N]: [name]` OR `DISCARD-[N]: [name]` | No candidate concludes without one token. | [PB-NN: the belief whose revision this clause tests for] |
| MUST-2 | EVERY DISCARD-[N] TOKEN -- no exceptions | Write: `DISCARD-[N]-PBI-REF: PB-[NN]` | Malformed without PBI-Ref. | [PB-NN: same as the belief cited in the DISCARD token] |
| MUST-3 | EVERY DISCARD-[N] TOKEN -- no exceptions | Write: `DISCARD-[N]-ROUTE: [destination]` | Malformed without ROUTE. | [PB-NN: belief whose failure to revise triggers this routing] |
| MUST-4 | EVERY DISCARD-[N] TOKEN -- no exceptions | Write: `DISCARD-[N]-REASON: [one sentence]` | Malformed without REASON. | [PB-NN: belief the candidate failed to contradict sufficiently] |

`DISCARD-LOG-COMPLETE: [N] STILL-LIVE, [M] DISCARD -- all four MUST-clauses applied; no candidate unresolved.`

**PHASE-HANDOVER-3** (registry entry: IA Step 3 -> IA Step 4):

| Field | Content |
|-------|---------|
| Completing Role | Institutional Archaeologist (IA) -- Step 3 |
| Step Completed | Step 3 -- Draft All Corrections |
| Output Produced | Draft corrections + STILL-LIVE FILTER output (DISCARD-LOG-COMPLETE) |
| Exclusion In Effect | No new entries after Step 4 begins |
| Receiving Role | Institutional Archaeologist (IA) -- Step 4 |

---

### Step 4 -- Register Audit

```
REGISTER AUDIT PROTOCOL: Source / Implies / Wrong / Decide / Verified -- rewrite per protocol.
```

**PHASE-HANDOVER-4** (registry entry: IA Step 4 -> IA Step 5):

| Field | Content |
|-------|---------|
| Completing Role | Institutional Archaeologist (IA) -- Step 4 |
| Step Completed | Step 4 -- Register Audit |
| Output Produced | Audited corrections (all fields rewritten) |
| Exclusion In Effect | Field rewrites locked |
| Receiving Role | Institutional Archaeologist (IA) -- Step 5 |

---

### Step 5 -- Entry Gate

```
ENTRY GATE: PBI-Ref / Source / Implies / Showed / Wrong / Decide / Verified
  PASS / FAIL per field. STATUS: CLEARED / NOT CLEARED. NOT CLEARED halts.
```

**PHASE-HANDOVER-5** (registry entry: IA Step 5 -> IA Step 6):

| Field | Content |
|-------|---------|
| Completing Role | Institutional Archaeologist (IA) -- Step 5 |
| Step Completed | Step 5 -- Entry Gate |
| Output Produced | Per-entry STATUS: CLEARED tokens |
| Exclusion In Effect | No field changes after CLEARED |
| Receiving Role | Institutional Archaeologist (IA) -- Step 6 |

---

### Step 6 -- Chain Integrity Audit

```
CHAIN INTEGRITY AUDIT: [1] PBI-Ref correct [2] Handle matches HL [3] Source resolvable
  [4] Verified is actual text. Token: CHAIN-COMPLETE / CHAIN-FLAG. CHAIN-FLAG IS HARD GATE.
RESOLUTION PROTOCOL: PBI-Ref/Verifier BC; Handle/Source/Verified Verifier IA.
```

Do not proceed to Step 7 until every entry CHAIN-COMPLETE.

**PHASE-HANDOVER-6** (registry entry: IA Step 6 -> IA Step 7):

| Field | Content |
|-------|---------|
| Completing Role | Institutional Archaeologist (IA) -- Step 6 |
| Step Completed | Step 6 -- Chain Integrity Audit |
| Output Produced | Per-entry CHAIN-COMPLETE tokens; Resolution Protocol trace if flagged |
| Exclusion In Effect | No chain repairs after CHAIN-COMPLETE |
| Receiving Role | Institutional Archaeologist (IA) -- Step 7 |

---

### Step 7 -- [IA] Hierarchy, Distillation, and Forward Handover

**Surprise hierarchy / Rules of Thumb (RULES-ANCHORED-COMPLETE) / Pattern of inherited
errors / Blind Spot Map / Correction Forward Statement / What this correction record excludes**
-- as specified in V-01 Step 7.

---

== ARTIFACT STRUCTURE ============================================================

  1-2. ENFORCEMENT MECHANISM + EF-INVOCATION-RECORD
  3. PHASE-HANDOVER-0 (5-row schema)
  4-5. PBI + BC-COVERAGE-RECORD (standard 4-field headers)
  6. PHASE-HANDOVER-1 (5-row schema)
  7. HANDLE LEDGER
  8. PHASE-HANDOVER-2 (5-row schema)
  9. Corrections HIGH -> MEDIUM -> LOW
  10. PHASE-HANDOVER-3 (5-row schema)
  11. Audited corrections
  12. PHASE-HANDOVER-4 (5-row schema)
  13. Entry Gate blocks (all CLEARED)
  14. PHASE-HANDOVER-5 (5-row schema)
  15. Chain Integrity Audit (all CHAIN-COMPLETE)
  16. PHASE-HANDOVER-6 (5-row schema)
  17-22. Rules / Hierarchy / Pattern / Blind Spot / Forward Statement / Exclusions
  Note: STILL-LIVE FILTER is a 5-column table (MUST-ID | Scope | Action | Constraint | Belief-Ref)

Write to: simulations/topic/echo/{topic}-echo-{YYYY-MM-DD}.md

---

## V-04 -- Axes A+B: Schema Field-ID Citation + Transition-ID Registry Citation

**Variation axes:** Lifecycle emphasis (Axis A) + Output format (Axis B)

**Hypothesis:** Axes A and B target different structural layers -- Axis A activates schema
addresses in the BC-COVERAGE-RECORD output; Axis B activates registry addresses in each
PHASE-HANDOVER table. They are structurally independent: Axis A affects the BC-STEP1-PROTOCOL
section and Step 1 output; Axis B affects the Roles section registry and all seven PHASE-
HANDOVER tables. Combining them tests whether citation activation accumulates additively
across independent structural layers, as R14 observed that navigability criteria (C-43/C-44/
C-45) accumulated additively. V-04 predicts +10 projected delta under v16.

**Expected v15 score:** 290 (all C-01 through C-48 PASS)

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
Function:     ENFORCEMENT MECHANISM + EF-INVOCATION-RECORD + PHASE-
              HANDOVER-0 before Step 1. NO-ECHO COST from pre-
              investigation materials only.
Input:        Design materials only. Signal artifacts out of scope.
Phase scope:  Step 0 only.
----------------------------------------------------------------------
```

**Belief Cartographer (BC)** -- Step 1 exclusively; three sub-phases per BC-STEP1-PROTOCOL.

```
BELIEF CARTOGRAPHER -- FUNCTION DECLARATION
----------------------------------------------------------------------
Function:     Three sub-phases per BC-STEP1-PROTOCOL. Gate token before
              each sub-phase advance. Gate return: PBI frozen +
              BC-COVERAGE-RECORD (with F-BCR field-IDs) + PHASE-
              HANDOVER-1.
Input:        Design materials only. Signal artifacts out of scope.
Phase scope:  Step 1 only. BC excluded from Steps 2-7.
----------------------------------------------------------------------
```

**Institutional Archaeologist (IA)** -- Steps 2-7.

```
INSTITUTIONAL ARCHAEOLOGIST -- FUNCTION DECLARATION
----------------------------------------------------------------------
Function:     False-assumption recovery. PHASE-HANDOVER-[N] at each
              stage exit (Steps 2-6). Each table cites its T-ID from
              the Phase Transition Registry in a Registry-Ref row.
Input:        Signal artifacts + frozen PBI.
Phase scope:  Steps 2-7 only.
----------------------------------------------------------------------
```

**Phase Handover Schema (universal -- all 7 exits, Steps 0-6):**

Six rows. Fixed field names. The Registry-Ref row cites the Transition-ID (T-NN) from the
Phase Transition Registry, activating the registry address in each consuming table.

| Field | Content |
|-------|---------|
| Completing Role | [role name and step number] |
| Step Completed | [step number and name] |
| Output Produced | [artifact(s) produced at this exit] |
| Exclusion In Effect | [what the completing role/phase can no longer modify] |
| Receiving Role | [role name and step number taking control] |
| Registry-Ref | [T-NN -- Transition-ID from Phase Transition Registry] |

#### Phase Transition Registry

Declared inside the Roles section before Step 0. Each row has a Transition-ID (T-NN).
Inline PHASE-HANDOVER-[N] tables cite T-NN in their Registry-Ref row. Universality is
verifiable by matching T-IDs in registry rows against Registry-Ref values in inline tables.

| T-ID | Transition | Step Completed | Completing Role | Receiving Role |
|------|------------|----------------|-----------------|----------------|
| T-00 | PHASE-HANDOVER-0 | Step 0 -- Enforcement Section and Invocation Record | Enforcement Framer (EF) | Belief Cartographer (BC) |
| T-01 | PHASE-HANDOVER-1 | Step 1 -- Belief Inventory and Coverage Audit | Belief Cartographer (BC) | Institutional Archaeologist (IA) |
| T-02 | PHASE-HANDOVER-2 | Step 2 -- Handle Ledger | Institutional Archaeologist (IA) | Institutional Archaeologist (IA) |
| T-03 | PHASE-HANDOVER-3 | Step 3 -- Draft All Corrections | Institutional Archaeologist (IA) | Institutional Archaeologist (IA) |
| T-04 | PHASE-HANDOVER-4 | Step 4 -- Register Audit | Institutional Archaeologist (IA) | Institutional Archaeologist (IA) |
| T-05 | PHASE-HANDOVER-5 | Step 5 -- Entry Gate | Institutional Archaeologist (IA) | Institutional Archaeologist (IA) |
| T-06 | PHASE-HANDOVER-6 | Step 6 -- Chain Integrity Audit | Institutional Archaeologist (IA) | Institutional Archaeologist (IA) |

---

### BC-STEP1-PROTOCOL

Pre-execution contract for Step 1. Markdown tables; no code fences; heading-navigable.

| Sub-phase | Scope | Gate Token |
|-----------|-------|------------|
| [SCAN] | Read design materials. List belief candidates. | `COMMIT-SCAN: [N] candidates identified.` |
| [FREEZE] | Produce PBI. Lock PB-[NN] entries. | `COMMIT-FREEZE: PBI frozen at [N] entries.` |
| [COVERAGE AUDIT] | Produce BC-COVERAGE-RECORD with F-BCR field-IDs. BC exclusion takes effect. | BC-COVERAGE-RECORD (schema below). |

#### BC-COVERAGE-RECORD Schema

Each field carries a named field-ID. BC-COVERAGE-RECORD output headers cite these IDs
(e.g., "F-BCR-2: Materials consulted"). Schema address is activated in the consuming output.

| F-ID | Field | Content | Constraint |
|------|-------|---------|------------|
| F-BCR-1 | Sub-phase | [COVERAGE AUDIT] -- gate declared in BC-STEP1-PROTOCOL. | Fixed. |
| F-BCR-2 | Materials consulted | [List design documents. Minimum one entry.] | Pre-investigation only. |
| F-BCR-3 | Signal artifacts excluded | [List by name; confirm not accessed.] | Enumerated by name. |
| F-BCR-4 | PBI completeness basis | [One sentence: primary PBI basis.] | Single sentence. |

---

### Step 0 -- [EF] Enforcement Section and Invocation Record

```
ENFORCEMENT MECHANISM DECLARATION
----------------------------------------------------------------------
Provenance tier: STRUCTURAL
Distinguishing property: Role-scope exclusion at three phase boundaries.
Reviewer implication: Independence enforced by role boundary.
NO-ECHO COST: [Named failure class. Generic fails.]
----------------------------------------------------------------------
```

```
EF-INVOCATION-RECORD
----------------------------------------------------------------------
Step: 0 | Materials consulted: [pre-investigation; min one] |
Signal artifacts excluded: [by name] | Cost derivation basis: [one sentence]
----------------------------------------------------------------------
```

**PHASE-HANDOVER-0** (registry entry T-00: EF -> BC):

| Field | Content |
|-------|---------|
| Completing Role | Enforcement Framer (EF) -- Step 0 |
| Step Completed | Step 0 -- Enforcement Section and Invocation Record |
| Output Produced | ENFORCEMENT MECHANISM DECLARATION + EF-INVOCATION-RECORD |
| Exclusion In Effect | EF excluded from Steps 1-7 |
| Receiving Role | Belief Cartographer (BC) -- Step 1 |
| Registry-Ref | T-00 |

---

### Step 1 -- [BC] Belief Inventory and Coverage Audit

**[SCAN]** `COMMIT-SCAN: [N] candidates identified.`

**[FREEZE]** PBI -- format PB-[NN]: ["Today's materials imply that X."]

`COMMIT-FREEZE: PBI frozen at [N] entries.`

**[COVERAGE AUDIT]** Produce BC-COVERAGE-RECORD. Prefix each field header with its F-ID from
the BC-COVERAGE-RECORD Schema (F-BCR-1: Sub-phase / F-BCR-2: Materials consulted / etc.).
No code fence.

BC excluded from Steps 2-7.

**PHASE-HANDOVER-1** (registry entry T-01: BC -> IA):

| Field | Content |
|-------|---------|
| Completing Role | Belief Cartographer (BC) -- Step 1 |
| Step Completed | Step 1 -- Belief Inventory and Coverage Audit |
| Output Produced | PBI frozen + BC-COVERAGE-RECORD (F-BCR field-IDs in all headers) |
| Exclusion In Effect | BC excluded; PBI frozen |
| Receiving Role | Institutional Archaeologist (IA) -- Step 2 |
| Registry-Ref | T-01 |

---

### Step 2 -- [IA] Handle Ledger

HL-[NN]: [2-5 words; finding language]. No PBI echoes. No handle labels in PBI entries.

**PHASE-HANDOVER-2** (registry entry T-02):

| Field | Content |
|-------|---------|
| Completing Role | Institutional Archaeologist (IA) -- Step 2 |
| Step Completed | Step 2 -- Handle Ledger |
| Output Produced | HANDLE LEDGER (all HL-[NN] complete) |
| Exclusion In Effect | No new handles after Step 3 |
| Receiving Role | Institutional Archaeologist (IA) -- Step 3 |
| Registry-Ref | T-02 |

---

### Step 3 -- [IA] Draft All Corrections

Correction Record Schema: Name / PBI-Ref / Source / Implies / Showed / Wrong / Decide /
Verified / Severity. Order: HIGH -> MEDIUM -> LOW.

**STILL-LIVE FILTER -- TABLE-COLUMN MUST-CLAUSE PROTOCOL**

| MUST-ID | Scope | Action | Constraint |
|---------|-------|--------|------------|
| MUST-1 | EVERY CANDIDATE -- no exceptions | `STILL-LIVE-[N]` OR `DISCARD-[N]` | No candidate exempt. |
| MUST-2 | EVERY DISCARD-[N] -- no exceptions | `DISCARD-[N]-PBI-REF: PB-[NN]` | Malformed without. |
| MUST-3 | EVERY DISCARD-[N] -- no exceptions | `DISCARD-[N]-ROUTE: [destination]` | Malformed without. |
| MUST-4 | EVERY DISCARD-[N] -- no exceptions | `DISCARD-[N]-REASON: [one sentence]` | Malformed without. |

`DISCARD-LOG-COMPLETE: [N] STILL-LIVE, [M] DISCARD -- all MUST-clauses applied; no candidate unresolved.`

**PHASE-HANDOVER-3** (registry entry T-03):

| Field | Content |
|-------|---------|
| Completing Role | Institutional Archaeologist (IA) -- Step 3 |
| Step Completed | Step 3 -- Draft All Corrections |
| Output Produced | Draft corrections + DISCARD-LOG-COMPLETE |
| Exclusion In Effect | No new entries after Step 4 |
| Receiving Role | Institutional Archaeologist (IA) -- Step 4 |
| Registry-Ref | T-03 |

---

### Step 4 -- Register Audit

Rewrite per protocol: Source / Implies / Wrong / Decide / Verified.

**PHASE-HANDOVER-4** (registry entry T-04):

| Field | Content |
|-------|---------|
| Completing Role | Institutional Archaeologist (IA) -- Step 4 |
| Step Completed | Step 4 -- Register Audit |
| Output Produced | Audited corrections (all fields rewritten) |
| Exclusion In Effect | Field rewrites locked |
| Receiving Role | Institutional Archaeologist (IA) -- Step 5 |
| Registry-Ref | T-04 |

---

### Step 5 -- Entry Gate

PASS/FAIL per field. STATUS: CLEARED / NOT CLEARED. NOT CLEARED halts.

**PHASE-HANDOVER-5** (registry entry T-05):

| Field | Content |
|-------|---------|
| Completing Role | Institutional Archaeologist (IA) -- Step 5 |
| Step Completed | Step 5 -- Entry Gate |
| Output Produced | Per-entry STATUS: CLEARED tokens |
| Exclusion In Effect | No field changes after CLEARED |
| Receiving Role | Institutional Archaeologist (IA) -- Step 6 |
| Registry-Ref | T-05 |

---

### Step 6 -- Chain Integrity Audit

Elements [1]-[4]. CHAIN-COMPLETE / CHAIN-FLAG. CHAIN-FLAG IS HARD GATE.
Resolution Protocol: one repair + named verifier per flag type.

Do not proceed to Step 7 until every entry CHAIN-COMPLETE.

**PHASE-HANDOVER-6** (registry entry T-06):

| Field | Content |
|-------|---------|
| Completing Role | Institutional Archaeologist (IA) -- Step 6 |
| Step Completed | Step 6 -- Chain Integrity Audit |
| Output Produced | Per-entry CHAIN-COMPLETE tokens; Resolution Protocol trace if flagged |
| Exclusion In Effect | No chain repairs after CHAIN-COMPLETE |
| Receiving Role | Institutional Archaeologist (IA) -- Step 7 |
| Registry-Ref | T-06 |

---

### Step 7 -- [IA] Hierarchy, Distillation, and Forward Handover

Surprise hierarchy / Rules of Thumb (RULES-ANCHORED-COMPLETE with per-rule tier quotation) /
Pattern of inherited errors / Blind Spot Map / Correction Forward Statement (confirms NO-ECHO
COST; names specific avoided failure) / What this correction record excludes.

---

== ARTIFACT STRUCTURE ============================================================

  1-2. ENFORCEMENT MECHANISM + EF-INVOCATION-RECORD
  3. PHASE-HANDOVER-0 (6-row; Registry-Ref: T-00)
  4-5. PBI + BC-COVERAGE-RECORD (F-BCR field-IDs in all headers)
  6. PHASE-HANDOVER-1 (6-row; Registry-Ref: T-01)
  7. HANDLE LEDGER
  8. PHASE-HANDOVER-2 (6-row; Registry-Ref: T-02)
  9. Corrections HIGH -> MEDIUM -> LOW
  10. PHASE-HANDOVER-3 (6-row; Registry-Ref: T-03)
  11. Audited corrections
  12. PHASE-HANDOVER-4 (6-row; Registry-Ref: T-04)
  13. Entry Gate blocks (all CLEARED)
  14. PHASE-HANDOVER-5 (6-row; Registry-Ref: T-05)
  15. Chain Integrity Audit (all CHAIN-COMPLETE)
  16. PHASE-HANDOVER-6 (6-row; Registry-Ref: T-06)
  17-22. Rules / Hierarchy / Pattern / Blind Spot / Forward Statement / Exclusions

Write to: simulations/topic/echo/{topic}-echo-{YYYY-MM-DD}.md

---

## V-05 -- Axes A+B+C: Schema Field-ID Citation + Transition-ID Registry Citation + MUST Belief-Ref Citation

**Variation axes:** Lifecycle emphasis (Axis A) + Output format (Axis B) + Phrasing register
(Axis C)

**Hypothesis:** All three citation-activation axes target structurally independent elements --
BC-COVERAGE-RECORD Schema fields (Axis A), Phase Transition Registry rows (Axis B), and
STILL-LIVE FILTER MUST-clauses (Axis C). All three can be satisfied simultaneously without
conflict. If each axis independently contributes an excellence signal under v15, V-05 is the
only R15 variation predicted to show all three, producing the maximum projected delta under
v16 (+15: three new candidate criteria at +5 each). The R15 thesis is confirmed if:
(1) V-01/V-02/V-03 each show their single axis's excellence signal while the others are absent,
(2) V-04 shows Axis A and Axis B but not Axis C,
(3) V-05 shows all three.

**Expected v15 score:** 290 (all C-01 through C-48 PASS)
**Projected v16 score:** 305 (C-49 PASS + C-50 PASS + C-51 PASS: +15)

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
Function:     ENFORCEMENT MECHANISM + EF-INVOCATION-RECORD + PHASE-
              HANDOVER-0 before Step 1. NO-ECHO COST from pre-
              investigation materials only.
Input:        Design materials only. Signal artifacts out of scope.
Phase scope:  Step 0 only. EF excluded from Steps 1-7.
----------------------------------------------------------------------
```

**Belief Cartographer (BC)** -- Step 1 exclusively; three sub-phases per BC-STEP1-PROTOCOL.

```
BELIEF CARTOGRAPHER -- FUNCTION DECLARATION
----------------------------------------------------------------------
Function:     Three sub-phases per BC-STEP1-PROTOCOL. Gate return: PBI
              frozen + BC-COVERAGE-RECORD (F-BCR field-IDs in headers)
              + PHASE-HANDOVER-1 (Registry-Ref: T-01).
Input:        Design materials only. Signal artifacts out of scope.
Phase scope:  Step 1 only. BC excluded from Steps 2-7.
----------------------------------------------------------------------
```

**Institutional Archaeologist (IA)** -- Steps 2-7.

```
INSTITUTIONAL ARCHAEOLOGIST -- FUNCTION DECLARATION
----------------------------------------------------------------------
Function:     False-assumption recovery. Correction register only.
              PHASE-HANDOVER-[N] at each stage exit (Steps 2-6); each
              table cites its T-ID in a Registry-Ref row.
              STILL-LIVE FILTER is a 5-column table with Belief-Ref.
Input:        Signal artifacts + frozen PBI (read-only).
Orienting:    "What would the next team build wrong?"
Phase scope:  Steps 2-7 only.
----------------------------------------------------------------------
```

**Phase Handover Schema (universal -- all 7 exits, Steps 0-6):**

Six rows. Fixed field names. Registry-Ref cites the Transition-ID from the Phase Transition
Registry, activating the registry address in each consuming table. Do not add or remove rows.

| Field | Content |
|-------|---------|
| Completing Role | [role name and step number] |
| Step Completed | [step number and name] |
| Output Produced | [artifact(s) produced at this exit] |
| Exclusion In Effect | [what the completing role/phase can no longer modify] |
| Receiving Role | [role name and step number taking control] |
| Registry-Ref | [T-NN -- Transition-ID from Phase Transition Registry] |

#### Phase Transition Registry

Declared inside the Roles section before Step 0. Each row has a Transition-ID (T-NN). Inline
PHASE-HANDOVER-[N] tables cite T-NN in their Registry-Ref row. Universality verifiable by
matching T-IDs in registry rows against Registry-Ref values in inline tables -- no traversal.

| T-ID | Transition | Step Completed | Completing Role | Receiving Role |
|------|------------|----------------|-----------------|----------------|
| T-00 | PHASE-HANDOVER-0 | Step 0 -- Enforcement Section and Invocation Record | Enforcement Framer (EF) | Belief Cartographer (BC) |
| T-01 | PHASE-HANDOVER-1 | Step 1 -- Belief Inventory and Coverage Audit | Belief Cartographer (BC) | Institutional Archaeologist (IA) |
| T-02 | PHASE-HANDOVER-2 | Step 2 -- Handle Ledger | Institutional Archaeologist (IA) | Institutional Archaeologist (IA) |
| T-03 | PHASE-HANDOVER-3 | Step 3 -- Draft All Corrections | Institutional Archaeologist (IA) | Institutional Archaeologist (IA) |
| T-04 | PHASE-HANDOVER-4 | Step 4 -- Register Audit | Institutional Archaeologist (IA) | Institutional Archaeologist (IA) |
| T-05 | PHASE-HANDOVER-5 | Step 5 -- Entry Gate | Institutional Archaeologist (IA) | Institutional Archaeologist (IA) |
| T-06 | PHASE-HANDOVER-6 | Step 6 -- Chain Integrity Audit | Institutional Archaeologist (IA) | Institutional Archaeologist (IA) |

---

### BC-STEP1-PROTOCOL

Pre-execution contract for Step 1. Heading-sovereign. Markdown tables; no code fences.

| Sub-phase | Scope | Gate Token |
|-----------|-------|------------|
| [SCAN] | Read design materials. List belief candidates. No pruning. | `COMMIT-SCAN: [N] candidates identified.` |
| [FREEZE] | Produce PBI. Lock all PB-[NN] entries. | `COMMIT-FREEZE: PBI frozen at [N] entries.` |
| [COVERAGE AUDIT] | Produce BC-COVERAGE-RECORD with F-BCR field-IDs in headers. BC exclusion takes effect. | BC-COVERAGE-RECORD (schema below). |

#### BC-COVERAGE-RECORD Schema

Each field carries a named F-ID. When producing BC-COVERAGE-RECORD output, prefix each
field header with its F-ID (e.g., "F-BCR-2: Materials consulted"). This activates the schema
address in the output: match any output field to its schema declaration by F-ID alone.

| F-ID | Field | Content | Constraint |
|------|-------|---------|------------|
| F-BCR-1 | Sub-phase | [COVERAGE AUDIT] -- gate declared in BC-STEP1-PROTOCOL. | Fixed. |
| F-BCR-2 | Materials consulted | [List design documents scanned during [SCAN] and [FREEZE]. Minimum one.] | Pre-investigation only. Signal artifacts excluded. |
| F-BCR-3 | Signal artifacts excluded | [List each signal artifact by name; confirm not accessed during Step 1.] | Enumerated by name. "none" not acceptable if signals exist. |
| F-BCR-4 | PBI completeness basis | [One sentence: which material provides the primary PBI basis.] | Single sentence. |

---

### Step 0 -- [EF] Enforcement Section and Invocation Record

```
ENFORCEMENT MECHANISM DECLARATION
----------------------------------------------------------------------
Provenance tier: STRUCTURAL
Distinguishing property: Role-scope exclusion at three phase boundaries.
  EF produces cost claim before signal reading -- cost is prospective.
  BC produces PBI before signal reading -- PBI cannot inherit HL labels.
  IA produces corrections from signals and cannot alter frozen PBI.
  Role boundary is the enforcement mechanism; no cross-phase reasoning.
Reviewer implication: Independence is enforced by role boundary.
NO-ECHO COST: [EF derives from pre-investigation materials. Name the
  specific failure class that propagates if this artifact is absent.
  Which beliefs in today's materials would the next team inherit as
  validated design knowledge? Named failure class required.]
----------------------------------------------------------------------
```

```
EF-INVOCATION-RECORD
----------------------------------------------------------------------
Step:       0 (EF phase; signal-reading phase not yet open)
Materials consulted (pre-investigation only):
  [Design documents, specs, proposals consulted. Minimum one entry.]
Signal artifacts excluded:
  [Each signal artifact by name; confirm not accessed at Step 0.]
Cost derivation basis:
  [One sentence: which material grounded the NO-ECHO COST claim.]
----------------------------------------------------------------------
```

**PHASE-HANDOVER-0** (registry entry T-00: EF -> BC):

| Field | Content |
|-------|---------|
| Completing Role | Enforcement Framer (EF) -- Step 0 |
| Step Completed | Step 0 -- Enforcement Section and Invocation Record |
| Output Produced | ENFORCEMENT MECHANISM DECLARATION + EF-INVOCATION-RECORD |
| Exclusion In Effect | EF excluded from Steps 1-7; signal artifacts not accessed at Step 0 |
| Receiving Role | Belief Cartographer (BC) -- Step 1 |
| Registry-Ref | T-00 |

---

### Step 1 -- [BC] Belief Inventory and Coverage Audit

Execute BC-STEP1-PROTOCOL as declared in the BC-STEP1-PROTOCOL section above.

**[SCAN]** Read all design materials. Signal artifacts out of scope. List every belief
candidate before advancing.

`COMMIT-SCAN: [N] candidates identified.`

**[FREEZE]** Produce the PBI.

```
PBI PRODUCTION PROTOCOL
----------------------------------------------------------------------
Input:    Design materials only. Signal artifacts excluded.
Format:   PB-[NN]: ["Today's materials imply that X." No signal
          knowledge. No handle labels.]
Freeze:   PBI frozen after COMMIT-FREEZE. No new PB-[NN] entries
          after this point.
----------------------------------------------------------------------
```

`COMMIT-FREEZE: PBI frozen at [N] entries.`

**[COVERAGE AUDIT]** Produce BC-COVERAGE-RECORD. Format output table with F-BCR field-IDs
in all headers: `F-BCR-1: Sub-phase`, `F-BCR-2: Materials consulted`, `F-BCR-3: Signal
artifacts excluded`, `F-BCR-4: PBI completeness basis`. Table format; no code fence.

BC is now excluded from Steps 2-7.

**PHASE-HANDOVER-1** (registry entry T-01: BC -> IA):

| Field | Content |
|-------|---------|
| Completing Role | Belief Cartographer (BC) -- Step 1 |
| Step Completed | Step 1 -- Belief Inventory and Coverage Audit |
| Output Produced | PBI (all PB-[NN] frozen) + BC-COVERAGE-RECORD (F-BCR field-IDs in all headers) |
| Exclusion In Effect | BC excluded from Steps 2-7; PBI frozen; no additions after this table |
| Receiving Role | Institutional Archaeologist (IA) -- Step 2 |
| Registry-Ref | T-01 |

---

### Step 2 -- [IA] Handle Ledger

```
HANDLE LEDGER PROTOCOL
----------------------------------------------------------------------
Timing:   After reading all signal artifacts. Before writing corrections.
Format:   HL-[NN]: [finding-specific label -- 2-5 words; finding language]
Test:     No PBI entry names its handle. No HL entry echoes PBI verbatim.
----------------------------------------------------------------------
```

**PHASE-HANDOVER-2** (registry entry T-02: IA Step 2 -> IA Step 3):

| Field | Content |
|-------|---------|
| Completing Role | Institutional Archaeologist (IA) -- Step 2 |
| Step Completed | Step 2 -- Handle Ledger |
| Output Produced | HANDLE LEDGER (all HL-[NN] entries complete) |
| Exclusion In Effect | No new handles may be coined after Step 3 begins |
| Receiving Role | Institutional Archaeologist (IA) -- Step 3 |
| Registry-Ref | T-02 |

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

**STILL-LIVE FILTER -- BELIEF-REF TABLE-COLUMN MUST-CLAUSE PROTOCOL**

Apply each MUST-clause to every candidate from the Handle Ledger. Scope and Action are
independent columns. The Belief-Ref column names the PB-[NN] prior belief each clause
enforces, enabling bidirectional lookup: which clause enforces PB-03? which belief motivates
MUST-2? Both questions answerable from table cells alone. Each MUST-clause is unconditional.

| MUST-ID | Scope | Action | Constraint | Belief-Ref |
|---------|-------|--------|------------|------------|
| MUST-1 | EVERY CANDIDATE -- no exceptions | Produce exactly one of: `STILL-LIVE-[N]: [candidate name]` OR `DISCARD-[N]: [candidate name]` | No candidate concludes without one token. No candidate is exempt. | [PB-NN: belief whose revision this candidate's STILL-LIVE status tests] |
| MUST-2 | EVERY DISCARD-[N] TOKEN -- no exceptions | Immediately write: `DISCARD-[N]-PBI-REF: PB-[NN]` -- names the prior belief tested against | Malformed without PBI-Ref token. No DISCARD is exempt. | [PB-NN: same belief cited in the DISCARD-PBI-REF token for this entry] |
| MUST-3 | EVERY DISCARD-[N] TOKEN -- no exceptions | Immediately write: `DISCARD-[N]-ROUTE: [destination -- topic-story or named skill]` | Malformed without ROUTE token. | [PB-NN: belief whose failure to be contradicted triggers this routing] |
| MUST-4 | EVERY DISCARD-[N] TOKEN -- no exceptions | Immediately write: `DISCARD-[N]-REASON: [one sentence -- specific exclusion reason]` | Malformed without REASON token. | [PB-NN: belief the candidate failed to contradict at sufficient specificity] |

Completeness gate:
`DISCARD-LOG-COMPLETE: [N] STILL-LIVE, [M] DISCARD -- all four MUST-clauses applied to every candidate; no candidate unresolved.`

**PHASE-HANDOVER-3** (registry entry T-03: IA Step 3 -> IA Step 4):

| Field | Content |
|-------|---------|
| Completing Role | Institutional Archaeologist (IA) -- Step 3 |
| Step Completed | Step 3 -- Draft All Corrections |
| Output Produced | Draft corrections + STILL-LIVE FILTER output (DISCARD-LOG-COMPLETE) |
| Exclusion In Effect | No new entries or DISCARD tokens after Step 4 begins |
| Receiving Role | Institutional Archaeologist (IA) -- Step 4 |
| Registry-Ref | T-03 |

---

### Step 4 -- Register Audit

```
REGISTER AUDIT PROTOCOL
----------------------------------------------------------------------
Execute field by field before Step 5. Rewrite: Source (prose ->
namespace:skill:artifact), Implies (narration -> future-team framing),
Wrong (softener -> specific wrong component), Decide (deferral ->
blocking decision), Verified (identifiers -> quoted actual text of both).
----------------------------------------------------------------------
```

**PHASE-HANDOVER-4** (registry entry T-04: IA Step 4 -> IA Step 5):

| Field | Content |
|-------|---------|
| Completing Role | Institutional Archaeologist (IA) -- Step 4 |
| Step Completed | Step 4 -- Register Audit |
| Output Produced | Audited correction entries (all fields rewritten per protocol) |
| Exclusion In Effect | Field rewrites locked; no further changes outside Step 5 gate |
| Receiving Role | Institutional Archaeologist (IA) -- Step 5 |
| Registry-Ref | T-04 |

---

### Step 5 -- Entry Gate

```
ENTRY GATE DECLARATION
----------------------------------------------------------------------
Purpose:  Per-entry field validation. Format + framing only.
Fields:   PBI-Ref / Source / Implies / Showed / Wrong / Decide / Verified
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

**PHASE-HANDOVER-5** (registry entry T-05: IA Step 5 -> IA Step 6):

| Field | Content |
|-------|---------|
| Completing Role | Institutional Archaeologist (IA) -- Step 5 |
| Step Completed | Step 5 -- Entry Gate |
| Output Produced | Per-entry STATUS: CLEARED tokens (all entries) |
| Exclusion In Effect | No field changes permitted after all entries CLEARED |
| Receiving Role | Institutional Archaeologist (IA) -- Step 6 |
| Registry-Ref | T-05 |

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
Exactly one named repair action per flag type. Verifier role required.

  PBI-Ref mismatch (element 1):
    Repair:   Replace PBI-Ref with identifier matching correct belief.
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

**PHASE-HANDOVER-6** (registry entry T-06: IA Step 6 -> IA Step 7):

| Field | Content |
|-------|---------|
| Completing Role | Institutional Archaeologist (IA) -- Step 6 |
| Step Completed | Step 6 -- Chain Integrity Audit |
| Output Produced | Per-entry CHAIN-COMPLETE tokens; Resolution Protocol trace if flagged |
| Exclusion In Effect | No chain repairs permitted after all entries CHAIN-COMPLETE |
| Receiving Role | Institutional Archaeologist (IA) -- Step 7 |
| Registry-Ref | T-06 |

---

### Step 7 -- [IA] Hierarchy, Distillation, and Forward Handover

**Surprise hierarchy:** Ranked by design impact. Argued rationale. Names decision at risk.

**Rules of Thumb:**

```
RULES OF THUMB DECLARATION
----------------------------------------------------------------------
Scope:  HIGH and MEDIUM entries only. LOW excluded.
Format: [TIER] {Rule -- <=20 words} (encodes: {SURPRISE NAME})
Check:  RULES-ANCHORED traceability -- tier annotation must match
        Severity of parent entry.
Gate:   RULES-ANCHORED BLOCKS on any MISALIGNED rule.
Closure: RULES-ANCHORED-COMPLETE: R-01 "[TIER]" ALIGNED, R-02 "[TIER]"
         ALIGNED, ... -- distillation phase closed.
Fail token: RULES-ANCHORED-FAIL: R-[NN] "[TIER]" MISALIGNED.
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

  1. ENFORCEMENT MECHANISM DECLARATION (EF; NO-ECHO COST; head position)
  2. EF-INVOCATION-RECORD (Step 0; pre-investigation materials enumerated)
  3. PHASE-HANDOVER-0 (6-row; Registry-Ref: T-00)
  4. PBI output (BC; COMMIT-SCAN + COMMIT-FREEZE tokens)
  5. BC-COVERAGE-RECORD (F-BCR field-IDs in all headers; table format; no code fence)
  6. PHASE-HANDOVER-1 (6-row; Registry-Ref: T-01)
  7. HANDLE LEDGER output (IA)
  8. PHASE-HANDOVER-2 (6-row; Registry-Ref: T-02)
  9. Corrections -- HIGH -> MEDIUM -> LOW
  10. PHASE-HANDOVER-3 (6-row; Registry-Ref: T-03)
  11. Audited corrections (Register Audit output)
  12. PHASE-HANDOVER-4 (6-row; Registry-Ref: T-04)
  13. Entry Gate blocks (all STATUS: CLEARED)
  14. PHASE-HANDOVER-5 (6-row; Registry-Ref: T-05)
  15. Chain Integrity Audit (all CHAIN-COMPLETE)
  16. PHASE-HANDOVER-6 (6-row; Registry-Ref: T-06)
  17. Rules of Thumb (RULES-ANCHORED-COMPLETE with per-rule tier quotation)
  18. Surprise hierarchy (ranked with rationale)
  19. Pattern of inherited errors
  20. Blind Spot Map
  21. Correction Forward Statement (confirms NO-ECHO COST; names specific avoided failure)
  22. What this correction record excludes
  Note: BC-COVERAGE-RECORD Schema has F-ID column (C-46 sub-heading + Axis A F-IDs)
  Note: PHASE-HANDOVER tables are 6-row (5-row schema + Registry-Ref: T-NN)
  Note: STILL-LIVE FILTER is 5-column (MUST-ID | Scope | Action | Constraint | Belief-Ref)

Write to: simulations/topic/echo/{topic}-echo-{YYYY-MM-DD}.md
