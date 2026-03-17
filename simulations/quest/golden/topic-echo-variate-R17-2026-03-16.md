---
skill: quest-variate
skill_target: topic-echo
date: 2026-03-16
round: 17
rubric: v17
rubric_file: simulations/quest/rubrics/topic-echo-rubric-v17-2026-03-16.md
rubric_max: 320
---

# Variations: `topic:echo` -- Round 17 (2026-03-16)

**Rubric:** v17 (2026-03-16) | **Criteria:** 54 (5 essential / 3 recommended / 46 aspirational)

---

## Design Context

R16 V-05 achieves 305/305 under v16. The three citation-layer criteria formalized in v17 --
CITATION-COMPLETENESS-MANIFEST-EXHAUSTIVE (C-52), DECLARING-SECTION-CONSUMER-INDEX-POPULATED (C-53),
and CITATION-CHAIN-PBI-GROUNDING-VERIFIED (C-54) -- were demonstrated as structural candidates in
R16 but not yet verified against formal pass conditions. Round 17 does not re-implement R16's axes.
It tightens the prompt language for each axis against the precise v17 pass condition text, then
combines axes in the same single-axis-first pattern as R16.

**What changes from R16 to R17:**

- **C-52 tightening**: R16 V-01 introduced the CITATION-COMPLETENESS-MANIFEST with a
  `MANIFEST-COMPLETE` token. R17 V-01 strengthens the token's required format: the token must
  name per-type counts explicitly (`[N] TYPE-A, [N] TYPE-B, [N] TYPE-C`) and carry the confirmation
  phrase "all RESOLVED" -- both required by the C-52 pass condition ("MANIFEST-COMPLETE token gates
  closure"). A token omitting type counts or the "all RESOLVED" clause does not satisfy C-52.

- **C-53 tightening**: R16 V-02 added Consumer-Ref columns but did not include a cross-table
  completeness gate. C-53's pass condition requires all THREE declaring tables simultaneously
  ("partial Consumer-Ref (one or two declaring tables) fails"). R17 V-02 adds a
  `CONSUMER-INDEX-COMPLETE` gate token that names all three tables and confirms each Consumer-Ref
  column is populated -- making the all-three-simultaneously requirement structurally visible and
  testable from the gate token alone.

- **C-54 tightening**: R16 V-03 specified the Belief-Ref extension and F-BCR-4 rule but did not
  add an explicit chain-grounding gate. C-54's pass condition requires both conditions ("either
  alone fails"). R17 V-03 adds a `CHAIN-GROUNDING-COMPLETE` gate token that confirms BOTH
  conditions are met: extended Belief-Ref cells AND specific-PBI-entry F-BCR-4. A prompt
  satisfying only one of the two C-54 conditions does not emit this token and fails the criterion.

**Predicted scoring under v17:**

| Variation | C-52 | C-53 | C-54 | v17 | delta from R16 v16 |
|-----------|:----:|:----:|:----:|:---:|:------------------:|
| V-01 (Axis A) | PASS | FAIL | FAIL | 310 | +5 |
| V-02 (Axis B) | FAIL | PASS | FAIL | 310 | +5 |
| V-03 (Axis C) | FAIL | FAIL | PASS | 310 | +5 |
| V-04 (A+B) | PASS | PASS | FAIL | 315 | +10 |
| **V-05 (A+B+C)** | PASS | PASS | PASS | **320** | +15 |

All variations inherit the full R16 V-05 structure (C-01 through C-51 all PASS).

---

## V-01 -- Axis A: Citation-Completeness Manifest (C-52 formalized)

**Variation axis:** Lifecycle emphasis -- after artifact write, produce a
CITATION-COMPLETENESS-MANIFEST enumerating every citation point with per-type counts and all-RESOLVED
confirmation in the MANIFEST-COMPLETE token (Axis A only; formal C-52 satisfaction)

**Hypothesis:** R16 V-01 demonstrated that a post-artifact manifest creates a single-table
citation audit. R17 V-01 asks whether tightening the MANIFEST-COMPLETE token format -- requiring
per-type counts and explicit "all RESOLVED" confirmation -- produces an observable formal
distinction from R16: the token is now a self-contained audit closure statement, not merely a
marker. A reviewer reading only the token can confirm citation-type completeness without reading
the manifest table body. This satisfies C-52's pass condition: "MANIFEST-COMPLETE token gates
closure."

**Expected v17 score:** 310 (C-01 through C-51: all PASS; C-52: PASS; C-53: FAIL; C-54: FAIL)

---

Topic: `{topic}`

Synthesize what was unexpected. Three roles at three exclusive phase boundaries. Every structural
commitment is named, formal, and auditable from output. This is not a summary. This is not a list
of findings. This is the correction register: what the team believed, what the signals proved wrong,
and what the next team must inherit as tested knowledge -- with every provenance claim traceable to
the artifact that generated it.

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
Phase scope:  Step 0 only. EF excluded from Steps 1-8.
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
Phase scope:  Step 1 only. BC excluded from Steps 2-8 after the
              [COVERAGE AUDIT] gate token is written.
Gate return:  PBI (all PB-[NN] entries frozen) + BC-COVERAGE-RECORD
              (F-BCR field-IDs in headers) + PHASE-HANDOVER-1 table
              before Step 2 begins.
----------------------------------------------------------------------
```

**Institutional Archaeologist (IA)** -- Steps 2-8.

```
INSTITUTIONAL ARCHAEOLOGIST -- FUNCTION DECLARATION
----------------------------------------------------------------------
Function:     False-assumption recovery. Correction register only.
              Each IA stage exit (Steps 2-6) produces a PHASE-
              HANDOVER-[N] table before advancing. At Step 8, produce
              the CITATION-COMPLETENESS-MANIFEST satisfying C-52:
              CITATION-COMPLETENESS-MANIFEST-EXHAUSTIVE. The
              MANIFEST-COMPLETE token must name per-type citation
              counts and confirm all RESOLVED -- it gates closure.
Input:        Signal artifacts + frozen PBI (read-only).
Out-of-scope: PBI authorship (frozen). Enforcement section (immutable).
Orienting:    "What would the next team build wrong?"
Phase scope:  Steps 2-8 only.
----------------------------------------------------------------------
```

**Phase Handover Schema (universal -- all 7 exits, Steps 0-6):**

All PHASE-HANDOVER-[N] tables use this schema exactly. Six rows. Fixed field names.
Do not substitute prose. Do not add or remove rows. The Registry-Ref row cites the
Transition-ID from the Phase Transition Registry, activating the registry address in
each consuming table.

| Field | Content |
|-------|---------|
| Completing Role | [role name and step number] |
| Step Completed | [step number and name] |
| Output Produced | [artifact(s) produced at this exit] |
| Exclusion In Effect | [what the completing role/phase can no longer modify] |
| Receiving Role | [role name and step number taking control] |
| Registry-Ref | [T-NN -- the Transition-ID from the Phase Transition Registry matching this exit] |

#### Phase Transition Registry

Pre-declared registry of all seven phase transitions. Every step exit in Steps 0 through 6
must produce a PHASE-HANDOVER-[N] table with a Registry-Ref row matching this registry.
Universality verifiable by cross-referencing T-IDs in the registry against Registry-Ref
values in inline tables -- no traversal required.

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
advancing. Do not merge sub-phases. Expressed entirely as markdown tables; no code fences.

| Sub-phase | Scope | Gate Token |
|-----------|-------|------------|
| [SCAN] | Read design materials. List all belief candidates. No pruning or evaluation. | `COMMIT-SCAN: [N] candidates identified.` |
| [FREEZE] | Produce PBI from scan results. Lock all PB-[NN] entries. No additions after gate token. | `COMMIT-FREEZE: PBI frozen at [N] entries.` |
| [COVERAGE AUDIT] | Audit domain coverage. Produce BC-COVERAGE-RECORD using schema below. BC exclusion takes effect after this record is written. | BC-COVERAGE-RECORD (schema below). |

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

**PHASE-HANDOVER-0** (registry entry: T-00):

| Field | Content |
|-------|---------|
| Completing Role | Enforcement Framer (EF) -- Step 0 |
| Step Completed | Step 0 -- Enforcement Section and Invocation Record |
| Output Produced | ENFORCEMENT MECHANISM DECLARATION + EF-INVOCATION-RECORD |
| Exclusion In Effect | EF excluded from Steps 1-8; signal artifacts not accessed at Step 0 |
| Receiving Role | Belief Cartographer (BC) -- Step 1 |
| Registry-Ref | T-00 |

---

### Step 1 -- [BC] Belief Inventory and Coverage Audit

Execute BC-STEP1-PROTOCOL as declared above. Write each gate token before advancing.

**[SCAN]** Read all design materials within BC's input scope. Signal artifacts out of scope.
List all belief candidates before moving to [FREEZE].

`COMMIT-SCAN: [N] candidates identified.`

**[FREEZE]** Produce the PBI from scanned candidates.

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
header (F-BCR-1: Sub-phase / F-BCR-2: Materials consulted / F-BCR-3: Signal artifacts excluded /
F-BCR-4: PBI completeness basis). No code fence.

BC is now excluded from Steps 2-8.

**PHASE-HANDOVER-1** (registry entry: T-01):

| Field | Content |
|-------|---------|
| Completing Role | Belief Cartographer (BC) -- Step 1 |
| Step Completed | Step 1 -- Belief Inventory and Coverage Audit |
| Output Produced | PBI (all PB-[NN] frozen) + BC-COVERAGE-RECORD (F-BCR field-IDs in headers) |
| Exclusion In Effect | BC excluded from Steps 2-8; PBI frozen; no additions after this table |
| Receiving Role | Institutional Archaeologist (IA) -- Step 2 |
| Registry-Ref | T-01 |

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

**PHASE-HANDOVER-2** (registry entry: T-02):

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

**STILL-LIVE FILTER -- TABLE-COLUMN MUST-CLAUSE PROTOCOL**

Apply each MUST-clause to every candidate from the Handle Ledger. Scope and Action are
separate columns. Each MUST-clause carries a stable MUST-ID and a Belief-Ref column naming
the PBI entry that motivated each clause. Each MUST-clause is unconditional.

| MUST-ID | Scope | Action | Constraint | Belief-Ref |
|---------|-------|--------|------------|------------|
| MUST-1 | EVERY CANDIDATE -- no exceptions | Produce exactly one of: `STILL-LIVE-[N]: [name]` OR `DISCARD-[N]: [name]` | No candidate evaluation concludes without one of these tokens. | PB-[NN] -- the belief being tested for survival |
| MUST-2 | EVERY DISCARD-[N] TOKEN -- no exceptions | Immediately write: `DISCARD-[N]-PBI-REF: PB-[NN]` | A DISCARD token without a PBI-Ref token is malformed. | PB-[NN] -- the belief whose falsification makes this routing rule necessary |
| MUST-3 | EVERY DISCARD-[N] TOKEN -- no exceptions | Immediately write: `DISCARD-[N]-ROUTE: [destination]` | A DISCARD token without a ROUTE token is malformed. | PB-[NN] -- the belief whose failure category determines the routing destination |
| MUST-4 | EVERY DISCARD-[N] TOKEN -- no exceptions | Immediately write: `DISCARD-[N]-REASON: [one sentence]` | A DISCARD token without a REASON token is malformed. | PB-[NN] -- the belief whose survival condition this REASON clause states |

Completeness gate: `DISCARD-LOG-COMPLETE: [N] STILL-LIVE, [M] DISCARD -- all four MUST-clauses applied to every candidate; no candidate unresolved.`

**PHASE-HANDOVER-3** (registry entry: T-03):

| Field | Content |
|-------|---------|
| Completing Role | Institutional Archaeologist (IA) -- Step 3 |
| Step Completed | Step 3 -- Draft All Corrections |
| Output Produced | Draft corrections + STILL-LIVE FILTER output (DISCARD-LOG-COMPLETE) |
| Exclusion In Effect | No new entries or DISCARD tokens may be added after Step 4 begins |
| Receiving Role | Institutional Archaeologist (IA) -- Step 4 |
| Registry-Ref | T-03 |

---

### Step 4 -- [IA] Register Audit

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

**PHASE-HANDOVER-4** (registry entry: T-04):

| Field | Content |
|-------|---------|
| Completing Role | Institutional Archaeologist (IA) -- Step 4 |
| Step Completed | Step 4 -- Register Audit |
| Output Produced | Audited correction entries (all fields rewritten per protocol) |
| Exclusion In Effect | Field rewrites locked; no further changes outside Step 5 gate |
| Receiving Role | Institutional Archaeologist (IA) -- Step 5 |
| Registry-Ref | T-04 |

---

### Step 5 -- [IA] Entry Gate

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

**PHASE-HANDOVER-5** (registry entry: T-05):

| Field | Content |
|-------|---------|
| Completing Role | Institutional Archaeologist (IA) -- Step 5 |
| Step Completed | Step 5 -- Entry Gate |
| Output Produced | Per-entry STATUS: CLEARED tokens (all entries) |
| Exclusion In Effect | No field changes permitted after all entries CLEARED |
| Receiving Role | Institutional Archaeologist (IA) -- Step 6 |
| Registry-Ref | T-05 |

---

### Step 6 -- [IA] Chain Integrity Audit

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
    Repair:   Replace PBI-Ref with identifier matching belief in PBI.
    Verifier: BELIEF CARTOGRAPHER (BC).

  Handle mismatch (element 2):
    Repair:   Determine authoritative label; propagate from source.
    Verifier: INSTITUTIONAL ARCHAEOLOGIST (IA).

  Source absent (element 3):
    Repair:   Replace with resolvable artifact, or demote to discard.
    Verifier: INSTITUTIONAL ARCHAEOLOGIST (IA).

  Verified inaccurate (element 4):
    Repair:   Re-quote actual text from both PBI entry and source.
    Verifier: INSTITUTIONAL ARCHAEOLOGIST (IA).
----------------------------------------------------------------------
```

Do not proceed to Step 7 until every entry CHAIN-COMPLETE.

**PHASE-HANDOVER-6** (registry entry: T-06):

| Field | Content |
|-------|---------|
| Completing Role | Institutional Archaeologist (IA) -- Step 6 |
| Step Completed | Step 6 -- Chain Integrity Audit |
| Output Produced | Per-entry CHAIN-COMPLETE tokens; RESOLUTION trace if flagged |
| Exclusion In Effect | No chain repairs permitted after all entries CHAIN-COMPLETE |
| Receiving Role | Institutional Archaeologist (IA) -- Step 7 |
| Registry-Ref | T-06 |

---

### Step 7 -- [IA] Hierarchy, Distillation, and Forward Handover

**Surprise hierarchy:** Ranked by design impact. Argued rationale. Names decision at risk.

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

| Tier | Rule (<=20 words) | Encodes |
|------|-------------------|---------|
| [HIGH] | {rule statement} | {SURPRISE NAME} |
| [MEDIUM] | {rule statement} | {SURPRISE NAME} |

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

### Step 8 -- [IA] Citation-Completeness Manifest [AXIS A -- C-52]

After the artifact is complete at Step 7, produce the CITATION-COMPLETENESS-MANIFEST.
This manifest exhaustively enumerates every citation point in the artifact, confirming
all citations resolve against their declared addresses. A reviewer auditing
citation-completeness reads this table alone -- no document traversal required.

```
CITATION-COMPLETENESS-MANIFEST PROTOCOL (C-52: CITATION-COMPLETENESS-MANIFEST-EXHAUSTIVE)
----------------------------------------------------------------------
Purpose:  Post-artifact citation audit. Every citation point that
          exists in this artifact must appear in this manifest.
Scope:    Three citation types (all must be enumerated):
          TYPE-A: F-BCR field-ID citations (output headers -> schema)
          TYPE-B: T-ID registry citations (Registry-Ref rows -> registry)
          TYPE-C: Belief-Ref citations (MUST-clause column -> PBI)
Status:   RESOLVED -- target address exists and is locatable by ID
          DANGLING -- target address absent or non-locatable
Omission: Any citation point absent from the manifest is itself a
          manifest failure. Completeness is verified by row count
          matching known citation points: 4 TYPE-A, 7 TYPE-B, and
          one TYPE-C per MUST-clause row.
Gate:     Any DANGLING citation halts finalization. Report and resolve
          before emitting the MANIFEST-COMPLETE token.
Token:    MANIFEST-COMPLETE must name per-type counts and confirm
          all RESOLVED -- this token is the closure gate for C-52.
          Required format:
          MANIFEST-COMPLETE: [N] citations total --
            CIT-01..CIT-04 [4] TYPE-A RESOLVED,
            CIT-05..CIT-11 [7] TYPE-B RESOLVED,
            CIT-12..CIT-[N] [M] TYPE-C RESOLVED --
            citation-completeness verified; no document traversal
            required to confirm all addresses resolve.
----------------------------------------------------------------------
```

| Citation-ID | Citation Type | Source Location | Target Address | Status |
|-------------|--------------|-----------------|----------------|--------|
| CIT-01 | TYPE-A | BC-COVERAGE-RECORD output header "F-BCR-1: Sub-phase" | BC-COVERAGE-RECORD Schema row F-BCR-1 | RESOLVED / DANGLING |
| CIT-02 | TYPE-A | BC-COVERAGE-RECORD output header "F-BCR-2: Materials consulted" | BC-COVERAGE-RECORD Schema row F-BCR-2 | RESOLVED / DANGLING |
| CIT-03 | TYPE-A | BC-COVERAGE-RECORD output header "F-BCR-3: Signal artifacts excluded" | BC-COVERAGE-RECORD Schema row F-BCR-3 | RESOLVED / DANGLING |
| CIT-04 | TYPE-A | BC-COVERAGE-RECORD output header "F-BCR-4: PBI completeness basis" | BC-COVERAGE-RECORD Schema row F-BCR-4 | RESOLVED / DANGLING |
| CIT-05 | TYPE-B | PHASE-HANDOVER-0 Registry-Ref row | Phase Transition Registry row T-00 | RESOLVED / DANGLING |
| CIT-06 | TYPE-B | PHASE-HANDOVER-1 Registry-Ref row | Phase Transition Registry row T-01 | RESOLVED / DANGLING |
| CIT-07 | TYPE-B | PHASE-HANDOVER-2 Registry-Ref row | Phase Transition Registry row T-02 | RESOLVED / DANGLING |
| CIT-08 | TYPE-B | PHASE-HANDOVER-3 Registry-Ref row | Phase Transition Registry row T-03 | RESOLVED / DANGLING |
| CIT-09 | TYPE-B | PHASE-HANDOVER-4 Registry-Ref row | Phase Transition Registry row T-04 | RESOLVED / DANGLING |
| CIT-10 | TYPE-B | PHASE-HANDOVER-5 Registry-Ref row | Phase Transition Registry row T-05 | RESOLVED / DANGLING |
| CIT-11 | TYPE-B | PHASE-HANDOVER-6 Registry-Ref row | Phase Transition Registry row T-06 | RESOLVED / DANGLING |
| CIT-[N] | TYPE-C | STILL-LIVE FILTER MUST-[N] Belief-Ref cell | PBI row PB-[NN] | RESOLVED / DANGLING |

`MANIFEST-COMPLETE: [N] citations total -- CIT-01..CIT-04 [4] TYPE-A RESOLVED, CIT-05..CIT-11 [7] TYPE-B RESOLVED, CIT-12..CIT-[N] [M] TYPE-C RESOLVED -- citation-completeness verified; no document traversal required to confirm all addresses resolve.`

== ARTIFACT STRUCTURE ============================================================

  1. ENFORCEMENT MECHANISM DECLARATION (EF; NO-ECHO COST named)
  2. EF-INVOCATION-RECORD (Step 0)
  3. PHASE-HANDOVER-0 table (6-row schema; Registry-Ref: T-00)
  4. PBI output (BC; COMMIT-SCAN + COMMIT-FREEZE tokens present)
  5. BC-COVERAGE-RECORD (F-BCR field-IDs in all headers; no code fence)
  6. PHASE-HANDOVER-1 table (6-row schema; Registry-Ref: T-01)
  7. HANDLE LEDGER output (IA)
  8. PHASE-HANDOVER-2 table (6-row schema; Registry-Ref: T-02)
  9. Corrections -- HIGH -> MEDIUM -> LOW
  10. PHASE-HANDOVER-3 table (6-row schema; Registry-Ref: T-03)
  11. Audited corrections (Register Audit output)
  12. PHASE-HANDOVER-4 table (6-row schema; Registry-Ref: T-04)
  13. Entry Gate blocks (all STATUS: CLEARED)
  14. PHASE-HANDOVER-5 table (6-row schema; Registry-Ref: T-05)
  15. Chain Integrity Audit (all CHAIN-COMPLETE)
  16. PHASE-HANDOVER-6 table (6-row schema; Registry-Ref: T-06)
  17. Rules of Thumb (RULES-ANCHORED-COMPLETE)
  18. Surprise hierarchy (ranked with rationale)
  19. Pattern of inherited errors
  20. Blind Spot Map
  21. Correction Forward Statement
  22. What this correction record excludes
  23. CITATION-COMPLETENESS-MANIFEST (Step 8; MANIFEST-COMPLETE token with per-type counts)

Write to: simulations/topic/echo/{topic}-echo-{YYYY-MM-DD}.md

---

## V-02 -- Axis B: Declaring-Section Consumer Index (C-53 formalized)

**Variation axis:** Output format -- the BC-COVERAGE-RECORD Schema, Phase Transition Registry,
AND STILL-LIVE FILTER tables all gain a final `Consumer-Ref` column simultaneously, with a
`CONSUMER-INDEX-COMPLETE` gate token confirming all three tables populated (Axis B only;
formal C-53 satisfaction)

**Hypothesis:** R16 V-02 demonstrated that Consumer-Ref columns in declaring tables create
bidirectional navigability. R17 V-02 adds a cross-table completeness gate --
`CONSUMER-INDEX-COMPLETE` -- that names all three declaring tables and confirms each
Consumer-Ref column is populated. This token makes the C-53 pass condition testable from a
single location: a reviewer reading the gate token knows all three axes are bidirectionally
navigable without reading the three tables independently. This satisfies C-53's critical
clause: "partial Consumer-Ref (one or two declaring tables) fails."

**Expected v17 score:** 310 (C-01 through C-51: all PASS; C-52: FAIL; C-53: PASS; C-54: FAIL)

---

Topic: `{topic}`

Synthesize what was unexpected. Three roles at three exclusive phase boundaries. Every structural
commitment is named, formal, and auditable from output. This is not a summary. This is not a list
of findings. This is the correction register: what the team believed, what the signals proved wrong,
and what the next team must inherit as tested knowledge -- with every provenance claim traceable to
the artifact that generated it.

---

### Roles

_(EF Step 0 exclusively; BC Step 1 exclusively; IA Steps 2-7. Function declarations identical to
V-01 except IA phase scope is Steps 2-7 and no Step 8 mention -- Axis A not present in V-02.)_

**Phase Handover Schema:** Six rows including Registry-Ref row (C-50 preserved, identical to V-01).

#### Phase Transition Registry [AXIS B -- Consumer-Ref column]

Pre-declared registry of all seven phase transitions. Each T-ID row carries a Consumer-Ref
column naming the inline PHASE-HANDOVER table that cites it -- the registry is bidirectionally
navigable from each declaration row. A reviewer reading T-03 immediately knows that
PHASE-HANDOVER-3's Registry-Ref row is the consuming site, without scanning the artifact.

| T-ID | Transition | Step Completed | Completing Role | Receiving Role | Consumer-Ref |
|------|------------|----------------|-----------------|----------------|--------------|
| T-00 | PHASE-HANDOVER-0 | Step 0 -- Enforcement Section and Invocation Record | Enforcement Framer (EF) | Belief Cartographer (BC) | Consumed-By: PHASE-HANDOVER-0 Registry-Ref row |
| T-01 | PHASE-HANDOVER-1 | Step 1 -- Belief Inventory and Coverage Audit | Belief Cartographer (BC) | Institutional Archaeologist (IA) | Consumed-By: PHASE-HANDOVER-1 Registry-Ref row |
| T-02 | PHASE-HANDOVER-2 | Step 2 -- Handle Ledger | Institutional Archaeologist (IA) | Institutional Archaeologist (IA) | Consumed-By: PHASE-HANDOVER-2 Registry-Ref row |
| T-03 | PHASE-HANDOVER-3 | Step 3 -- Draft All Corrections | Institutional Archaeologist (IA) | Institutional Archaeologist (IA) | Consumed-By: PHASE-HANDOVER-3 Registry-Ref row |
| T-04 | PHASE-HANDOVER-4 | Step 4 -- Register Audit | Institutional Archaeologist (IA) | Institutional Archaeologist (IA) | Consumed-By: PHASE-HANDOVER-4 Registry-Ref row |
| T-05 | PHASE-HANDOVER-5 | Step 5 -- Entry Gate | Institutional Archaeologist (IA) | Institutional Archaeologist (IA) | Consumed-By: PHASE-HANDOVER-5 Registry-Ref row |
| T-06 | PHASE-HANDOVER-6 | Step 6 -- Chain Integrity Audit | Institutional Archaeologist (IA) | Institutional Archaeologist (IA) | Consumed-By: PHASE-HANDOVER-6 Registry-Ref row |

---

### BC-STEP1-PROTOCOL

_(Three sub-phases identical to V-01.)_

#### BC-COVERAGE-RECORD Schema [AXIS B -- Consumer-Ref column]

Each field carries a named field-ID (F-BCR-1 through F-BCR-4). Each F-ID row carries a
Consumer-Ref column naming the output step where the field is cited -- the schema is
bidirectionally navigable from each field declaration row without scanning the artifact.

| F-ID | Field | Content | Constraint | Consumer-Ref |
|------|-------|---------|------------|--------------|
| F-BCR-1 | Sub-phase | [COVERAGE AUDIT] -- gate declared in BC-STEP1-PROTOCOL. | Fixed; do not substitute. | Consumed-By: [COVERAGE AUDIT] output header in Step 1; PHASE-HANDOVER-1 Output Produced field |
| F-BCR-2 | Materials consulted | [List each design document scanned during [SCAN] and [FREEZE]. Minimum one entry.] | Pre-investigation only. Signal artifacts excluded. | Consumed-By: [COVERAGE AUDIT] output header in Step 1 |
| F-BCR-3 | Signal artifacts excluded | [List each signal artifact by name; confirm not accessed during Step 1.] | Enumerated by name. "none" not acceptable if signals exist. | Consumed-By: [COVERAGE AUDIT] output header in Step 1 |
| F-BCR-4 | PBI completeness basis | [One sentence: which material(s) provide the primary PBI basis.] | Single sentence. Reviewable from this field alone. | Consumed-By: [COVERAGE AUDIT] output header in Step 1 |

---

### Steps 0-6

_(Identical to V-01 for all steps. All PHASE-HANDOVER tables carry Registry-Ref rows with
T-ID citations. Step 3 STILL-LIVE FILTER includes Axis B Consumer-Ref column as shown below.)_

### Step 3 Extension -- STILL-LIVE FILTER with Consumer-Ref [AXIS B]

**STILL-LIVE FILTER -- TABLE-COLUMN MUST-CLAUSE PROTOCOL**

Each MUST-clause carries a stable MUST-ID (C-48 preserved), a Belief-Ref column naming the
PBI entry that motivated each clause (C-51 preserved), and a Consumer-Ref column naming the
enforcement site where each clause is applied (Axis B). The STILL-LIVE FILTER table is
bidirectionally navigable: from declaring clause to consuming token, not only from consuming
token to declaring clause.

| MUST-ID | Scope | Action | Constraint | Belief-Ref | Consumer-Ref |
|---------|-------|--------|------------|------------|--------------|
| MUST-1 | EVERY CANDIDATE -- no exceptions | Produce exactly one of: `STILL-LIVE-[N]: [name]` OR `DISCARD-[N]: [name]` | No candidate evaluation concludes without one of these tokens. | PB-[NN] -- belief tested for survival | Consumed-By: per-candidate evaluation token in Step 3 |
| MUST-2 | EVERY DISCARD-[N] TOKEN -- no exceptions | Immediately write: `DISCARD-[N]-PBI-REF: PB-[NN]` | A DISCARD token without a PBI-Ref token is malformed. | PB-[NN] -- belief whose falsification makes routing necessary | Consumed-By: DISCARD-[N]-PBI-REF token in Step 3 |
| MUST-3 | EVERY DISCARD-[N] TOKEN -- no exceptions | Immediately write: `DISCARD-[N]-ROUTE: [destination]` | A DISCARD token without a ROUTE token is malformed. | PB-[NN] -- belief whose failure category determines routing | Consumed-By: DISCARD-[N]-ROUTE token in Step 3 |
| MUST-4 | EVERY DISCARD-[N] TOKEN -- no exceptions | Immediately write: `DISCARD-[N]-REASON: [one sentence]` | A DISCARD token without a REASON token is malformed. | PB-[NN] -- belief whose survival condition this REASON states | Consumed-By: DISCARD-[N]-REASON token in Step 3 |

Completeness gate: `DISCARD-LOG-COMPLETE: [N] STILL-LIVE, [M] DISCARD -- all four MUST-clauses applied to every candidate; no candidate unresolved.`

### Step 7 Extension -- Consumer-Index Completeness Gate [AXIS B -- C-53]

After all artifact content is written at Step 7, emit the cross-table consumer-index
completeness gate confirming all three declaring tables carry populated Consumer-Ref columns.
This gate satisfies C-53: DECLARING-SECTION-CONSUMER-INDEX-POPULATED.

```
CONSUMER-INDEX-COMPLETE PROTOCOL (C-53: DECLARING-SECTION-CONSUMER-INDEX-POPULATED)
----------------------------------------------------------------------
Purpose:  Post-content verification that Consumer-Ref columns are
          populated in all three declaring tables simultaneously.
          Partial population (one or two tables) is a gate failure.
Tables:   BC-COVERAGE-RECORD Schema (F-BCR-1..4 Consumer-Ref)
          Phase Transition Registry (T-00..T-06 Consumer-Ref)
          STILL-LIVE FILTER (MUST-1..MUST-4 Consumer-Ref)
Gate:     All three tables must pass. Any table with absent or empty
          Consumer-Ref cells fails. Report before emitting token.
Token:    Required format:
          CONSUMER-INDEX-COMPLETE: BC-COVERAGE-RECORD Schema
            F-BCR-1..F-BCR-4 Consumer-Ref POPULATED,
            Phase Transition Registry T-00..T-06 Consumer-Ref POPULATED,
            STILL-LIVE FILTER MUST-1..MUST-4 Consumer-Ref POPULATED --
            bidirectional navigability complete across all three axes.
----------------------------------------------------------------------
```

`CONSUMER-INDEX-COMPLETE: BC-COVERAGE-RECORD Schema F-BCR-1..F-BCR-4 Consumer-Ref POPULATED, Phase Transition Registry T-00..T-06 Consumer-Ref POPULATED, STILL-LIVE FILTER MUST-1..MUST-4 Consumer-Ref POPULATED -- bidirectional navigability complete across all three axes.`

== ARTIFACT STRUCTURE ============================================================

  1-22. (Same as V-01 items 1-22)
  Note: Phase Transition Registry carries Consumer-Ref column (Axis B)
  Note: BC-COVERAGE-RECORD Schema carries Consumer-Ref column (Axis B)
  Note: STILL-LIVE FILTER carries Consumer-Ref column (Axis B)
  Note: CONSUMER-INDEX-COMPLETE gate token at Step 7 close (C-53)
  No item 23 -- Axis A manifest not present in V-02.

Write to: simulations/topic/echo/{topic}-echo-{YYYY-MM-DD}.md

---

## V-03 -- Axis C: PBI-Grounded Citation Chain (C-54 formalized)

**Variation axis:** Lifecycle emphasis -- each Belief-Ref cell in the STILL-LIVE FILTER
extends to `PB-[NN] (confirmed false by: [artifact name, namespace, date])`; F-BCR-4 output
names specific PBI entries; a `CHAIN-GROUNDING-COMPLETE` gate token confirms BOTH conditions
met (Axis C only; formal C-54 satisfaction)

**Hypothesis:** R16 V-03 demonstrated the extended Belief-Ref cell format and the specific-PBI
F-BCR-4 rule. R17 V-03 adds a `CHAIN-GROUNDING-COMPLETE` gate token that explicitly names
both C-54 conditions and confirms both are present. This makes the "either alone fails"
requirement structurally visible: a reviewer reading only the gate token knows both conditions
are satisfied. Without this token, a prompt might satisfy one condition and silently fail the
other -- the token makes the joint requirement non-defeatable.

**Expected v17 score:** 310 (C-01 through C-51: all PASS; C-52: FAIL; C-53: FAIL; C-54: PASS)

---

Topic: `{topic}`

Synthesize what was unexpected. Three roles at three exclusive phase boundaries. Every structural
commitment is named, formal, and auditable from output. This is not a summary. This is not a list
of findings. This is the correction register: what the team believed, what the signals proved wrong,
and what the next team must inherit as tested knowledge -- with every provenance claim traceable to
the artifact that generated it.

---

### Roles

_(EF Step 0 exclusively; BC Step 1 exclusively; IA Steps 2-7. Function declarations identical to
V-01 except IA phase scope is Steps 2-7 and no Step 8 mention -- Axis A not present in V-03.)_

**Phase Handover Schema:** Six rows including Registry-Ref row (C-50 preserved, identical to V-01).

**Phase Transition Registry:** T-ID column present (C-50 preserved, identical to V-01). No
Consumer-Ref column -- Axis B not present in V-03.

---

### BC-STEP1-PROTOCOL

_(Three sub-phases identical to V-01.)_

#### BC-COVERAGE-RECORD Schema [AXIS C -- F-BCR-4 extension]

Each field carries a named field-ID (F-BCR-1 through F-BCR-4). No Consumer-Ref column --
Axis B not present in V-03.

**F-BCR-4 Axis C requirement**: When producing the BC-COVERAGE-RECORD output, the F-BCR-4
field (PBI completeness basis) must explicitly name the PB-[NN] entries constituting the
coverage basis. Generic summary sentences fail C-54. Required format:

`F-BCR-4: PBI completeness basis -- PB-[NN1] through PB-[NNk] (from [material name]).`

A reviewer can confirm the coverage claim by reading the named PBI entries directly, rather
than accepting an ungrounded summary. This is one of the two required C-54 conditions.

| F-ID | Field | Content | Constraint |
|------|-------|---------|------------|
| F-BCR-1 | Sub-phase | [COVERAGE AUDIT] -- gate declared in BC-STEP1-PROTOCOL. | Fixed; do not substitute. |
| F-BCR-2 | Materials consulted | [List each design document scanned during [SCAN] and [FREEZE]. Minimum one entry.] | Pre-investigation only. Signal artifacts excluded. |
| F-BCR-3 | Signal artifacts excluded | [List each signal artifact by name; confirm not accessed during Step 1.] | Enumerated by name. "none" not acceptable if signals exist. |
| F-BCR-4 | PBI completeness basis | [Name specific PBI entries: "PB-NN through PB-NN (from material name)." Generic sentence fails.] | Names specific PB-[NN] entries. Reviewable against PBI directly. C-54 condition. |

---

### Steps 0-6

_(Identical to V-01 for all steps except Step 3 STILL-LIVE FILTER as shown below.)_

### Step 3 Extension -- STILL-LIVE FILTER with PBI-Grounded Belief-Ref [AXIS C]

**STILL-LIVE FILTER -- TABLE-COLUMN MUST-CLAUSE PROTOCOL**

Each MUST-clause carries a stable MUST-ID (C-48 preserved) and a Belief-Ref column (C-51
preserved). The Belief-Ref cell extends the citation chain one level deeper: it names the PBI
entry AND the signal artifact that confirmed that belief false. This is the second required
C-54 condition. A reviewer reading any MUST-clause can walk to its PBI entry and then to the
signal that confirmed that belief false -- from the table cell alone, without consulting prose
in any section.

**Belief-Ref format rule (C-54 condition):** Each cell must contain:
`PB-[NN] (confirmed false by: [artifact name, namespace, date])`

A Belief-Ref cell containing only `PB-[NN]` without the confirming artifact is incomplete and
must be revised before Step 4 begins. The confirming artifact attribution is required; it is
not optional annotation.

| MUST-ID | Scope | Action | Constraint | Belief-Ref |
|---------|-------|--------|------------|------------|
| MUST-1 | EVERY CANDIDATE -- no exceptions | Produce exactly one of: `STILL-LIVE-[N]: [name]` OR `DISCARD-[N]: [name]` | No candidate evaluation concludes without one of these tokens. | PB-[NN] (confirmed false by: [artifact name, namespace, date]) |
| MUST-2 | EVERY DISCARD-[N] TOKEN -- no exceptions | Immediately write: `DISCARD-[N]-PBI-REF: PB-[NN]` | A DISCARD token without a PBI-Ref token is malformed. | PB-[NN] (confirmed false by: [artifact name, namespace, date]) |
| MUST-3 | EVERY DISCARD-[N] TOKEN -- no exceptions | Immediately write: `DISCARD-[N]-ROUTE: [destination]` | A DISCARD token without a ROUTE token is malformed. | PB-[NN] (confirmed false by: [artifact name, namespace, date]) |
| MUST-4 | EVERY DISCARD-[N] TOKEN -- no exceptions | Immediately write: `DISCARD-[N]-REASON: [one sentence]` | A DISCARD token without a REASON token is malformed. | PB-[NN] (confirmed false by: [artifact name, namespace, date]) |

Completeness gate: `DISCARD-LOG-COMPLETE: [N] STILL-LIVE, [M] DISCARD -- all four MUST-clauses applied to every candidate; no candidate unresolved.`

### Step 7 Extension -- Chain-Grounding Completeness Gate [AXIS C -- C-54]

After all artifact content is written at Step 7, emit the chain-grounding completeness gate
confirming BOTH C-54 conditions are present. Either condition alone is insufficient -- the gate
must confirm both or it does not close.

```
CHAIN-GROUNDING-COMPLETE PROTOCOL (C-54: CITATION-CHAIN-PBI-GROUNDING-VERIFIED)
----------------------------------------------------------------------
Purpose:  Post-content verification that BOTH C-54 conditions are
          satisfied. Either condition alone fails C-54.
Condition 1: STILL-LIVE FILTER Belief-Ref cells carry extended format
             "PB-[NN] (confirmed false by: [artifact, namespace, date])"
             for all MUST-clause rows. No bare "PB-[NN]" cells present.
Condition 2: BC-COVERAGE-RECORD F-BCR-4 output names specific PBI entries
             in format "PB-[NN] through PB-[NN] (from [material name])".
             Generic summary sentence is absent.
Gate:     Both conditions must confirm. If either is absent, report
          and revise before emitting the token.
Token:    Required format:
          CHAIN-GROUNDING-COMPLETE: Belief-Ref cells EXTENDED
            (all MUST-[N] carry confirming artifact reference),
            F-BCR-4 SPECIFIC (names PB-[NN] through PB-[NN]) --
            citation chain verified to evidence without document
            traversal; C-54 both conditions satisfied.
----------------------------------------------------------------------
```

`CHAIN-GROUNDING-COMPLETE: Belief-Ref cells EXTENDED (all MUST-[N] carry confirming artifact reference), F-BCR-4 SPECIFIC (names PB-[NN] through PB-[NN]) -- citation chain verified to evidence without document traversal; C-54 both conditions satisfied.`

== ARTIFACT STRUCTURE ============================================================

  1-22. (Same as V-01 items 1-22)
  Note: BC-COVERAGE-RECORD F-BCR-4 field names specific PBI entries (Axis C)
  Note: STILL-LIVE FILTER Belief-Ref cells include confirming artifact reference (Axis C)
  Note: CHAIN-GROUNDING-COMPLETE gate token at Step 7 close (C-54)
  No item 23 -- Axis A manifest not present in V-03.

Write to: simulations/topic/echo/{topic}-echo-{YYYY-MM-DD}.md

---

## V-04 -- Axes A+B: Citation-Completeness Manifest + Consumer Index (C-52+C-53)

**Variation axis:** Lifecycle emphasis + output format -- adds Axis A (CITATION-COMPLETENESS-
MANIFEST at Step 8 with per-type MANIFEST-COMPLETE token) and Axis B (Consumer-Ref column in
all three declaring tables with CONSUMER-INDEX-COMPLETE gate token) together; no Axis C

**Hypothesis:** V-01 demonstrated that a post-artifact manifest with an explicit per-type token
satisfies C-52. V-02 demonstrated that Consumer-Ref columns with a cross-table completeness gate
satisfy C-53. V-04 asks whether both structures together reinforce each other structurally: the
Consumer-Ref columns declare which consuming contexts cite each address (Axis B); the manifest
verifies that each expected citation resolves (Axis A). Declaration announces; verification
confirms. The CONSUMER-INDEX-COMPLETE gate pre-populates the manifest's expected citation set,
making the manifest verifiable against the declaring tables without independent enumeration.

**Expected v17 score:** 315 (C-01 through C-51: all PASS; C-52: PASS; C-53: PASS; C-54: FAIL)

---

Topic: `{topic}`

Synthesize what was unexpected. Three roles at three exclusive phase boundaries. Every structural
commitment is named, formal, and auditable from output. This is not a summary. This is not a list
of findings. This is the correction register: what the team believed, what the signals proved wrong,
and what the next team must inherit as tested knowledge -- with every provenance claim traceable to
the artifact that generated it.

---

### Roles

_(EF Step 0 exclusively; BC Step 1 exclusively; IA Steps 2-8. IA function declaration notes
Step 8 produces the CITATION-COMPLETENESS-MANIFEST satisfying C-52, identical to V-01.)_

#### Phase Transition Registry [AXIS B -- Consumer-Ref column]

_(Identical to V-02: Consumer-Ref column present in all seven rows.)_

| T-ID | Transition | Step Completed | Completing Role | Receiving Role | Consumer-Ref |
|------|------------|----------------|-----------------|----------------|--------------|
| T-00 | PHASE-HANDOVER-0 | Step 0 -- Enforcement Section and Invocation Record | Enforcement Framer (EF) | Belief Cartographer (BC) | Consumed-By: PHASE-HANDOVER-0 Registry-Ref row |
| T-01 | PHASE-HANDOVER-1 | Step 1 -- Belief Inventory and Coverage Audit | Belief Cartographer (BC) | Institutional Archaeologist (IA) | Consumed-By: PHASE-HANDOVER-1 Registry-Ref row |
| T-02 | PHASE-HANDOVER-2 | Step 2 -- Handle Ledger | Institutional Archaeologist (IA) | Institutional Archaeologist (IA) | Consumed-By: PHASE-HANDOVER-2 Registry-Ref row |
| T-03 | PHASE-HANDOVER-3 | Step 3 -- Draft All Corrections | Institutional Archaeologist (IA) | Institutional Archaeologist (IA) | Consumed-By: PHASE-HANDOVER-3 Registry-Ref row |
| T-04 | PHASE-HANDOVER-4 | Step 4 -- Register Audit | Institutional Archaeologist (IA) | Institutional Archaeologist (IA) | Consumed-By: PHASE-HANDOVER-4 Registry-Ref row |
| T-05 | PHASE-HANDOVER-5 | Step 5 -- Entry Gate | Institutional Archaeologist (IA) | Institutional Archaeologist (IA) | Consumed-By: PHASE-HANDOVER-5 Registry-Ref row |
| T-06 | PHASE-HANDOVER-6 | Step 6 -- Chain Integrity Audit | Institutional Archaeologist (IA) | Institutional Archaeologist (IA) | Consumed-By: PHASE-HANDOVER-6 Registry-Ref row |

#### BC-COVERAGE-RECORD Schema [AXIS B -- Consumer-Ref column]

_(Identical to V-02: Consumer-Ref column present in all four rows.)_

| F-ID | Field | Content | Constraint | Consumer-Ref |
|------|-------|---------|------------|--------------|
| F-BCR-1 | Sub-phase | [COVERAGE AUDIT] -- gate declared in BC-STEP1-PROTOCOL. | Fixed; do not substitute. | Consumed-By: [COVERAGE AUDIT] output header in Step 1; PHASE-HANDOVER-1 Output Produced field |
| F-BCR-2 | Materials consulted | [List each design document scanned during [SCAN] and [FREEZE]. Minimum one entry.] | Pre-investigation only. Signal artifacts excluded. | Consumed-By: [COVERAGE AUDIT] output header in Step 1 |
| F-BCR-3 | Signal artifacts excluded | [List each signal artifact by name; confirm not accessed during Step 1.] | Enumerated by name. "none" not acceptable if signals exist. | Consumed-By: [COVERAGE AUDIT] output header in Step 1 |
| F-BCR-4 | PBI completeness basis | [One sentence: which material(s) provide the primary PBI basis.] | Single sentence. Reviewable from this field alone. | Consumed-By: [COVERAGE AUDIT] output header in Step 1 |

---

### Steps 0-6

_(Identical to V-01 except Step 3 STILL-LIVE FILTER carries Consumer-Ref column as in V-02.
All steps include standard Belief-Ref cells: PB-[NN] only, no confirming artifact -- Axis C
not present in V-04.)_

### Step 7 Extension -- Consumer-Index Completeness Gate [AXIS B -- C-53]

_(Identical to V-02: CONSUMER-INDEX-COMPLETE gate token emitted after Step 7 artifact content,
naming all three declaring tables and confirming Consumer-Ref columns populated across all three.)_

`CONSUMER-INDEX-COMPLETE: BC-COVERAGE-RECORD Schema F-BCR-1..F-BCR-4 Consumer-Ref POPULATED, Phase Transition Registry T-00..T-06 Consumer-Ref POPULATED, STILL-LIVE FILTER MUST-1..MUST-4 Consumer-Ref POPULATED -- bidirectional navigability complete across all three axes.`

### Step 8 -- [IA] Citation-Completeness Manifest [AXIS A -- C-52]

_(Identical to V-01 Step 8. Manifest enumerates TYPE-A, TYPE-B, TYPE-C citations.
MANIFEST-COMPLETE token names per-type counts and confirms all RESOLVED.
Structural reinforcement with Axis B: the Consumer-Ref column in the Phase Transition Registry
declares that T-[NN] is consumed by PHASE-HANDOVER-[N]'s Registry-Ref row; the manifest
confirms the corresponding CIT-[N] TYPE-B is RESOLVED. Declaration and verification corroborate.)_

`MANIFEST-COMPLETE: [N] citations total -- CIT-01..CIT-04 [4] TYPE-A RESOLVED, CIT-05..CIT-11 [7] TYPE-B RESOLVED, CIT-12..CIT-[N] [M] TYPE-C RESOLVED -- citation-completeness verified; no document traversal required to confirm all addresses resolve.`

== ARTIFACT STRUCTURE ============================================================

  1-22. (Same as V-01 items 1-22)
  Note: Phase Transition Registry carries Consumer-Ref column (Axis B)
  Note: BC-COVERAGE-RECORD Schema carries Consumer-Ref column (Axis B)
  Note: STILL-LIVE FILTER carries Consumer-Ref column (Axis B)
  Note: CONSUMER-INDEX-COMPLETE gate token at Step 7 close (C-53)
  23. CITATION-COMPLETENESS-MANIFEST (Step 8; MANIFEST-COMPLETE with per-type counts) (C-52)

Write to: simulations/topic/echo/{topic}-echo-{YYYY-MM-DD}.md

---

## V-05 -- Axes A+B+C: Full Citation Architecture (C-52+C-53+C-54)

**Variation axis:** Full integration -- Axis A (manifest + MANIFEST-COMPLETE token), Axis B
(Consumer-Ref in all three declaring tables + CONSUMER-INDEX-COMPLETE gate), and Axis C
(extended Belief-Ref cells + specific-PBI F-BCR-4 + CHAIN-GROUNDING-COMPLETE gate) active
simultaneously; TYPE-C manifest entries inline the confirming artifact reference

**Hypothesis:** V-01, V-02, V-03 each demonstrate a single new structural property. V-04
demonstrated that Axis A and Axis B corroborate each other. V-05 asks whether all three
active simultaneously create a property that no single axis or pair produces: a **closed
citation architecture** where any entry point into the citation topology (consuming output
header, PHASE-HANDOVER Registry-Ref row, or STILL-LIVE FILTER MUST-clause) enables traversal
to declaring section (Axis B reverse direction), to manifest completeness confirmation (Axis A),
and to the falsifying evidence (Axis C) -- all from table cells alone, without prose consultation.
The closed architecture is only demonstrable when all three axes are simultaneously active.

**Expected v17 score:** 320 (all 54 criteria: PASS)

---

Topic: `{topic}`

Synthesize what was unexpected. Three roles at three exclusive phase boundaries. Every structural
commitment is named, formal, and auditable from output. This is not a summary. This is not a list
of findings. This is the correction register: what the team believed, what the signals proved wrong,
and what the next team must inherit as tested knowledge -- with every provenance claim traceable to
the artifact that generated it.

---

### Roles

**Enforcement Framer (EF)** -- Step 0 exclusively.
_(Function declaration identical to V-01.)_

**Belief Cartographer (BC)** -- Step 1 exclusively.
_(Function declaration identical to V-01.)_

**Institutional Archaeologist (IA)** -- Steps 2-8.

```
INSTITUTIONAL ARCHAEOLOGIST -- FUNCTION DECLARATION
----------------------------------------------------------------------
Function:     False-assumption recovery. Correction register only.
              Each IA stage exit (Steps 2-6) produces a PHASE-
              HANDOVER-[N] table before advancing. At Step 7, emit
              CONSUMER-INDEX-COMPLETE (C-53) and CHAIN-GROUNDING-
              COMPLETE (C-54) gate tokens. At Step 8, produce the
              CITATION-COMPLETENESS-MANIFEST (C-52) with MANIFEST-
              COMPLETE token naming per-type counts and confirming
              all RESOLVED. All three gate tokens are required; any
              absent token is an incompletion, not an omission.
Input:        Signal artifacts + frozen PBI (read-only).
Out-of-scope: PBI authorship (frozen). Enforcement section (immutable).
Orienting:    "What would the next team build wrong?"
Phase scope:  Steps 2-8 only.
----------------------------------------------------------------------
```

**Phase Handover Schema:** Six rows including Registry-Ref row (identical to V-01).

#### Phase Transition Registry [AXIS B -- Consumer-Ref column]

_(Identical to V-02/V-04: Consumer-Ref column in all seven rows.)_

| T-ID | Transition | Step Completed | Completing Role | Receiving Role | Consumer-Ref |
|------|------------|----------------|-----------------|----------------|--------------|
| T-00 | PHASE-HANDOVER-0 | Step 0 -- Enforcement Section and Invocation Record | Enforcement Framer (EF) | Belief Cartographer (BC) | Consumed-By: PHASE-HANDOVER-0 Registry-Ref row |
| T-01 | PHASE-HANDOVER-1 | Step 1 -- Belief Inventory and Coverage Audit | Belief Cartographer (BC) | Institutional Archaeologist (IA) | Consumed-By: PHASE-HANDOVER-1 Registry-Ref row |
| T-02 | PHASE-HANDOVER-2 | Step 2 -- Handle Ledger | Institutional Archaeologist (IA) | Institutional Archaeologist (IA) | Consumed-By: PHASE-HANDOVER-2 Registry-Ref row |
| T-03 | PHASE-HANDOVER-3 | Step 3 -- Draft All Corrections | Institutional Archaeologist (IA) | Institutional Archaeologist (IA) | Consumed-By: PHASE-HANDOVER-3 Registry-Ref row |
| T-04 | PHASE-HANDOVER-4 | Step 4 -- Register Audit | Institutional Archaeologist (IA) | Institutional Archaeologist (IA) | Consumed-By: PHASE-HANDOVER-4 Registry-Ref row |
| T-05 | PHASE-HANDOVER-5 | Step 5 -- Entry Gate | Institutional Archaeologist (IA) | Institutional Archaeologist (IA) | Consumed-By: PHASE-HANDOVER-5 Registry-Ref row |
| T-06 | PHASE-HANDOVER-6 | Step 6 -- Chain Integrity Audit | Institutional Archaeologist (IA) | Institutional Archaeologist (IA) | Consumed-By: PHASE-HANDOVER-6 Registry-Ref row |

---

### BC-STEP1-PROTOCOL

_(Three sub-phases identical to V-01.)_

#### BC-COVERAGE-RECORD Schema [AXIS B + AXIS C]

Each field carries F-ID (C-49 preserved). Consumer-Ref column present (Axis B). F-BCR-4
requires specific PBI entries in output (Axis C).

| F-ID | Field | Content | Constraint | Consumer-Ref |
|------|-------|---------|------------|--------------|
| F-BCR-1 | Sub-phase | [COVERAGE AUDIT] -- gate declared in BC-STEP1-PROTOCOL. | Fixed; do not substitute. | Consumed-By: [COVERAGE AUDIT] output header in Step 1; PHASE-HANDOVER-1 Output Produced field |
| F-BCR-2 | Materials consulted | [List each design document scanned during [SCAN] and [FREEZE]. Minimum one entry.] | Pre-investigation only. Signal artifacts excluded. | Consumed-By: [COVERAGE AUDIT] output header in Step 1 |
| F-BCR-3 | Signal artifacts excluded | [List each signal artifact by name; confirm not accessed during Step 1.] | Enumerated by name. "none" not acceptable if signals exist. | Consumed-By: [COVERAGE AUDIT] output header in Step 1 |
| F-BCR-4 | PBI completeness basis | [Name specific PBI entries: "PB-NN through PB-NN (from material name)." Generic sentence fails C-54.] | Names specific PB-[NN] entries. C-54 condition. | Consumed-By: [COVERAGE AUDIT] output header in Step 1 |

**F-BCR-4 Axis C requirement:** The F-BCR-4 output must name specific PBI entries in the
format: `F-BCR-4: PBI completeness basis -- PB-[NN1] through PB-[NNk] (from [material name]).`
A generic sentence such as "design spec provided the primary basis" fails C-54 condition 2.

---

### Steps 0-6

_(Identical to V-01 except Step 3 STILL-LIVE FILTER carries both Consumer-Ref column [Axis B]
and extended Belief-Ref cells [Axis C] as shown below.)_

### Step 3 Extension -- STILL-LIVE FILTER with Consumer-Ref + PBI-Grounded Belief-Ref [AXIS B + AXIS C]

**STILL-LIVE FILTER -- TABLE-COLUMN MUST-CLAUSE PROTOCOL**

Each MUST-clause carries a stable MUST-ID (C-48), a Belief-Ref column in extended format
(Axis C), and a Consumer-Ref column (Axis B). The table is bidirectionally navigable (declaring
to consuming via Consumer-Ref) and evidence-grounded (chain terminates at confirming signal via
extended Belief-Ref).

**Belief-Ref format (C-54 condition 1):** `PB-[NN] (confirmed false by: [artifact name, namespace, date])`
**Consumer-Ref format (C-53):** `Consumed-By: [enforcement site and step]`

| MUST-ID | Scope | Action | Constraint | Belief-Ref | Consumer-Ref |
|---------|-------|--------|------------|------------|--------------|
| MUST-1 | EVERY CANDIDATE -- no exceptions | Produce exactly one of: `STILL-LIVE-[N]: [name]` OR `DISCARD-[N]: [name]` | No candidate evaluation concludes without one of these tokens. | PB-[NN] (confirmed false by: [artifact name, namespace, date]) | Consumed-By: per-candidate evaluation token in Step 3 |
| MUST-2 | EVERY DISCARD-[N] TOKEN -- no exceptions | Immediately write: `DISCARD-[N]-PBI-REF: PB-[NN]` | A DISCARD token without a PBI-Ref token is malformed. | PB-[NN] (confirmed false by: [artifact name, namespace, date]) | Consumed-By: DISCARD-[N]-PBI-REF token in Step 3 |
| MUST-3 | EVERY DISCARD-[N] TOKEN -- no exceptions | Immediately write: `DISCARD-[N]-ROUTE: [destination]` | A DISCARD token without a ROUTE token is malformed. | PB-[NN] (confirmed false by: [artifact name, namespace, date]) | Consumed-By: DISCARD-[N]-ROUTE token in Step 3 |
| MUST-4 | EVERY DISCARD-[N] TOKEN -- no exceptions | Immediately write: `DISCARD-[N]-REASON: [one sentence]` | A DISCARD token without a REASON token is malformed. | PB-[NN] (confirmed false by: [artifact name, namespace, date]) | Consumed-By: DISCARD-[N]-REASON token in Step 3 |

Completeness gate: `DISCARD-LOG-COMPLETE: [N] STILL-LIVE, [M] DISCARD -- all four MUST-clauses applied to every candidate; no candidate unresolved.`

---

### Step 7 Extension -- Consumer-Index + Chain-Grounding Gates [AXIS B C-53 + AXIS C C-54]

After all artifact content is written at Step 7, emit both completeness gates. Each gate must
be emitted independently -- a single combined token is not acceptable.

**Gate 1 (C-53):**

`CONSUMER-INDEX-COMPLETE: BC-COVERAGE-RECORD Schema F-BCR-1..F-BCR-4 Consumer-Ref POPULATED, Phase Transition Registry T-00..T-06 Consumer-Ref POPULATED, STILL-LIVE FILTER MUST-1..MUST-4 Consumer-Ref POPULATED -- bidirectional navigability complete across all three axes.`

**Gate 2 (C-54):**

`CHAIN-GROUNDING-COMPLETE: Belief-Ref cells EXTENDED (all MUST-[N] carry confirming artifact reference), F-BCR-4 SPECIFIC (names PB-[NN] through PB-[NN]) -- citation chain verified to evidence without document traversal; C-54 both conditions satisfied.`

---

### Step 8 -- [IA] Citation-Completeness Manifest [AXIS A -- C-52]

After the Step 7 gates are confirmed, produce the CITATION-COMPLETENESS-MANIFEST. In V-05,
TYPE-C manifest entries carry the full Axis C inline: the confirming artifact reference from
the Belief-Ref cell appears in the manifest as an extension of the Target Address column,
making the manifest TYPE-C rows self-contained chain references.

```
CITATION-COMPLETENESS-MANIFEST PROTOCOL (C-52: CITATION-COMPLETENESS-MANIFEST-EXHAUSTIVE)
----------------------------------------------------------------------
(Protocol identical to V-01 except TYPE-C row format extended for Axis C:)

TYPE-C row extended format:
  | CIT-[N] | TYPE-C | STILL-LIVE FILTER MUST-[N] Belief-Ref cell |
    PBI row PB-[NN] + confirming artifact ([artifact, namespace, date]) |
    RESOLVED / DANGLING |

The Target Address for TYPE-C entries includes both the PBI identifier
and the confirming signal artifact -- the manifest TYPE-C rows are
evidence-grounded, not merely PBI-pointing. MANIFEST-COMPLETE token
required with per-type counts.
----------------------------------------------------------------------
```

| Citation-ID | Citation Type | Source Location | Target Address | Status |
|-------------|--------------|-----------------|----------------|--------|
| CIT-01 | TYPE-A | BC-COVERAGE-RECORD output header "F-BCR-1: Sub-phase" | BC-COVERAGE-RECORD Schema row F-BCR-1 | RESOLVED / DANGLING |
| CIT-02 | TYPE-A | BC-COVERAGE-RECORD output header "F-BCR-2: Materials consulted" | BC-COVERAGE-RECORD Schema row F-BCR-2 | RESOLVED / DANGLING |
| CIT-03 | TYPE-A | BC-COVERAGE-RECORD output header "F-BCR-3: Signal artifacts excluded" | BC-COVERAGE-RECORD Schema row F-BCR-3 | RESOLVED / DANGLING |
| CIT-04 | TYPE-A | BC-COVERAGE-RECORD output header "F-BCR-4: PBI completeness basis" | BC-COVERAGE-RECORD Schema row F-BCR-4 | RESOLVED / DANGLING |
| CIT-05 | TYPE-B | PHASE-HANDOVER-0 Registry-Ref row | Phase Transition Registry row T-00 | RESOLVED / DANGLING |
| CIT-06 | TYPE-B | PHASE-HANDOVER-1 Registry-Ref row | Phase Transition Registry row T-01 | RESOLVED / DANGLING |
| CIT-07 | TYPE-B | PHASE-HANDOVER-2 Registry-Ref row | Phase Transition Registry row T-02 | RESOLVED / DANGLING |
| CIT-08 | TYPE-B | PHASE-HANDOVER-3 Registry-Ref row | Phase Transition Registry row T-03 | RESOLVED / DANGLING |
| CIT-09 | TYPE-B | PHASE-HANDOVER-4 Registry-Ref row | Phase Transition Registry row T-04 | RESOLVED / DANGLING |
| CIT-10 | TYPE-B | PHASE-HANDOVER-5 Registry-Ref row | Phase Transition Registry row T-05 | RESOLVED / DANGLING |
| CIT-11 | TYPE-B | PHASE-HANDOVER-6 Registry-Ref row | Phase Transition Registry row T-06 | RESOLVED / DANGLING |
| CIT-[N] | TYPE-C | STILL-LIVE FILTER MUST-[N] Belief-Ref cell | PBI row PB-[NN] + confirming artifact ([artifact name, namespace, date]) | RESOLVED / DANGLING |

`MANIFEST-COMPLETE: [N] citations total -- CIT-01..CIT-04 [4] TYPE-A RESOLVED, CIT-05..CIT-11 [7] TYPE-B RESOLVED, CIT-12..CIT-[N] [M] TYPE-C RESOLVED -- citation-completeness verified; no document traversal required to confirm all addresses resolve.`

== ARTIFACT STRUCTURE ============================================================

  1. ENFORCEMENT MECHANISM DECLARATION (EF; NO-ECHO COST named)
  2. EF-INVOCATION-RECORD (Step 0)
  3. PHASE-HANDOVER-0 table (6-row schema; Registry-Ref: T-00)
  4. PBI output (BC; COMMIT-SCAN + COMMIT-FREEZE tokens present)
  5. BC-COVERAGE-RECORD (F-BCR field-IDs in all headers; F-BCR-4 names specific PBI entries)
  6. PHASE-HANDOVER-1 table (6-row schema; Registry-Ref: T-01)
  7. HANDLE LEDGER output (IA)
  8. PHASE-HANDOVER-2 table (6-row schema; Registry-Ref: T-02)
  9. Corrections -- HIGH -> MEDIUM -> LOW
  10. PHASE-HANDOVER-3 table (6-row schema; Registry-Ref: T-03)
  11. Audited corrections (Register Audit output)
  12. PHASE-HANDOVER-4 table (6-row schema; Registry-Ref: T-04)
  13. Entry Gate blocks (all STATUS: CLEARED)
  14. PHASE-HANDOVER-5 table (6-row schema; Registry-Ref: T-05)
  15. Chain Integrity Audit (all CHAIN-COMPLETE)
  16. PHASE-HANDOVER-6 table (6-row schema; Registry-Ref: T-06)
  17. Rules of Thumb (RULES-ANCHORED-COMPLETE)
  18. Surprise hierarchy (ranked with rationale)
  19. Pattern of inherited errors
  20. Blind Spot Map
  21. Correction Forward Statement
  22. What this correction record excludes
  23. CONSUMER-INDEX-COMPLETE gate token (Step 7 close; C-53)
  24. CHAIN-GROUNDING-COMPLETE gate token (Step 7 close; C-54)
  25. CITATION-COMPLETENESS-MANIFEST (Step 8; MANIFEST-COMPLETE with per-type counts; C-52)
      Note: TYPE-C rows carry confirming artifact inline (Axis C extension to manifest scope)

Write to: simulations/topic/echo/{topic}-echo-{YYYY-MM-DD}.md

---

## Variation Summary

| # | Axis | New Gate Token(s) | C-52 | C-53 | C-54 | v17 |
|---|------|-------------------|:----:|:----:|:----:|:---:|
| V-01 | A only | MANIFEST-COMPLETE (per-type counts) | PASS | FAIL | FAIL | 310 |
| V-02 | B only | CONSUMER-INDEX-COMPLETE (all 3 tables) | FAIL | PASS | FAIL | 310 |
| V-03 | C only | CHAIN-GROUNDING-COMPLETE (both conditions) | FAIL | FAIL | PASS | 310 |
| V-04 | A+B | MANIFEST-COMPLETE + CONSUMER-INDEX-COMPLETE | PASS | PASS | FAIL | 315 |
| **V-05** | **A+B+C** | **All three gate tokens** | **PASS** | **PASS** | **PASS** | **320** |

**R17 structural contribution beyond R16:**

Each new criterion gets its own named gate token that makes the joint/simultaneous pass condition
structurally visible:
- C-52: MANIFEST-COMPLETE now carries per-type counts -- a reviewer reading the token alone confirms
  all three citation types are exhaustively enumerated and RESOLVED, without reading the manifest table.
- C-53: CONSUMER-INDEX-COMPLETE names all three declaring tables in a single token -- a reviewer
  confirms all-three-simultaneously without reading each table's Consumer-Ref column independently.
- C-54: CHAIN-GROUNDING-COMPLETE names both C-54 conditions in a single token -- a reviewer
  confirms neither condition was omitted without reading the Belief-Ref cells or F-BCR-4 output.

The gate tokens are the audit surface for the new criteria. Each token's required format is a
machine-readable contract: presence of the token in the correct format confirms the criterion;
absence or wrong format fails it. R17's structural advance is making each criterion's pass
condition token-visible.
