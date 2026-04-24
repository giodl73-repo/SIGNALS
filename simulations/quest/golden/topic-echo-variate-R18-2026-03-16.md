---
skill: quest-variate
skill_target: topic-echo
date: 2026-03-16
round: 18
rubric: v18
rubric_file: simulations/quest/rubrics/topic-echo-rubric-v18-2026-03-16.md
rubric_max: 335
---

# Variations: `topic:echo` -- Round 18 (2026-03-16)

**Rubric:** v18 (2026-03-16) | **Criteria:** 57 (5 essential / 3 recommended / 49 aspirational)

---

## Design Context

R17 V-05 achieves 320/320 under v17 and projects to 335/335 under v18. The three gate-layer
patterns formalized in v18 -- TOKEN-FORMAT-SELF-CERTIFYING (C-55), GATE-INDEPENDENCE-ENFORCED
(C-56), MANIFEST-ROW-INLINE-EVIDENCE (C-57) -- were present in R17 V-05 as excellence patterns
but not formally required by the prompt. Round 18 does not re-implement R17's axes. It promotes
each pattern from implicit to explicit, tightens the prompt language against the precise v18
pass condition text, and tests single-axis isolation before combination.

**What changes from R17 to R18:**

- **C-55 tightening (Axis A)**: R17 V-05 tokens carry inline specifics that happen to satisfy
  C-55 as a structural side-effect. The prompt does not formally declare what a self-certifying
  token must contain. R18 V-01 adds a named TOKEN CONTENT REQUIREMENT block specifying the exact
  format each gate token must carry. A token that asserts closure without naming the required
  specifics -- per-type ID ranges for MANIFEST-COMPLETE, individual table names for
  CONSUMER-INDEX-COMPLETE, both condition labels for CHAIN-GROUNDING-COMPLETE -- fails the
  declared requirement. C-55 is satisfied only when all three tokens are present in the
  prescribed self-certifying format.

- **C-56 tightening (Axis B)**: R17 V-05 Step 7 includes the note "each gate must be emitted
  independently -- a single combined token is not acceptable." C-56's pass condition requires
  an explicit artifact statement naming combined tokens as non-conforming, with the constraint
  name (GATE-INDEPENDENCE-ENFORCED) visible in the prohibition text. R18 V-02 elevates the
  per-step note to a named heading-level declaration with the canonical constraint name, makes
  the prohibition explicit and citation-stable, and requires the model to confirm the constraint
  applies at any step boundary where two or more gates close simultaneously.

- **C-57 tightening (Axis C)**: R17 V-05 Step 8 extends TYPE-C manifest rows by placing the
  confirming artifact in the Target Address column:
  `PBI row PB-[NN] + confirming artifact ([artifact, namespace, date])`. C-57 requires the
  confirming artifact in the STATUS CELL, not in Target Address:
  `RESOLVED (confirmed false by: [artifact name, namespace, date])`. R18 V-03 corrects the
  placement. A TYPE-C row with bare RESOLVED in the status cell fails; a row with the confirming
  artifact only in Target Address also fails -- the inline attribution must be in the status cell.

**Predicted R18 scoring under v18:**

| Variation | C-55 | C-56 | C-57 | v18 score | delta from R17 |
|-----------|:----:|:----:|:----:|:---------:|:--------------:|
| V-01 (Axis A) | FAIL | FAIL | FAIL | 310 | 0 |
| V-02 (Axis B) | FAIL | FAIL | FAIL | 310 | 0 |
| V-03 (Axis C) | FAIL | FAIL | FAIL | 310 | 0 |
| V-04 (A+B) | FAIL | FAIL | FAIL | 315 | 0 |
| **V-05 (A+B+C)** | PASS | PASS | PASS | **335** | **+15** |

**Scoring rationale:**

- **V-01** (C-52 present; C-53 C-54 absent): C-55 requires all three tokens to be
  self-certifying. CONSUMER-INDEX-COMPLETE and CHAIN-GROUNDING-COMPLETE do not exist in V-01.
  C-55 pass condition: "all three gate tokens carry inline specifics." One token present out of
  three -- FAIL.
- **V-02** (C-53 present; C-52 C-54 absent): C-56 requires C-53+C-54 both present (the
  Step-7 dual-gate case). CHAIN-GROUNDING-COMPLETE does not exist in V-02. The co-location
  scenario C-56 guards against never arises; the prohibition is declared but untestable.
  C-56 FAIL.
- **V-03** (C-54 present; C-52 C-53 absent): C-57 requires C-52+C-54 both present. No
  CITATION-COMPLETENESS-MANIFEST in V-03 -- no TYPE-C rows to apply the STATUS cell format to.
  C-57 not applicable -- FAIL.
- **V-04** (C-52+C-53 present; C-54 absent): C-55 requires C-52+C-53+C-54 -- C-54 absent --
  FAIL. C-56 requires C-53+C-54 -- C-54 absent -- FAIL. C-57 requires C-52+C-54 -- C-54 absent
  -- FAIL.
- **V-05** (C-52+C-53+C-54 all present): All prerequisites met. C-55 explicit token format
  declarations satisfied. C-56 explicit named prohibition at dual-gate boundary. C-57 STATUS
  cell carries confirming artifact. All three PASS. Score: 335.

---

## V-01 -- Axis A: Token Content Self-Certifying (C-55 targeted; C-56 C-57 absent)

**Variation axis:** Output format -- all gate tokens emitted in this artifact carry inline
specifics in the prescribed format so a reviewer can verify the token's pass condition without
consulting the underlying sections. Named TOKEN CONTENT REQUIREMENT block declares the format
for each token type (Axis A only; C-55 targeted; C-53 and C-54 not present).

**Hypothesis:** R17 V-01 demonstrated that a MANIFEST-COMPLETE token carrying per-type counts
satisfies C-52. C-55 extends this: the token must be fully self-certifying, not merely
count-carrying. R18 V-01 adds a formal TOKEN CONTENT REQUIREMENT block that names the exact
format for MANIFEST-COMPLETE. The block also declares what CONSUMER-INDEX-COMPLETE and
CHAIN-GROUNDING-COMPLETE would need to contain if they were present -- pre-establishing the
format contract for V-05. C-55 fails in V-01 because those two tokens are absent (C-53 and
C-54 not implemented), but the format declaration is complete and verifiable against V-05.

**Expected v18 score:** 310 (C-01 through C-52: all PASS as in R17 V-01; C-53: FAIL; C-54:
FAIL; C-55: FAIL -- only one of three required tokens present; C-56: FAIL; C-57: FAIL)

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
              the CITATION-COMPLETENESS-MANIFEST satisfying C-52.
              The MANIFEST-COMPLETE token must carry inline specifics
              as declared in the TOKEN CONTENT REQUIREMENT block
              below -- it gates closure and is self-certifying.
Input:        Signal artifacts + frozen PBI (read-only).
Out-of-scope: PBI authorship (frozen). Enforcement section (immutable).
Orienting:    "What would the next team build wrong?"
Phase scope:  Steps 2-8 only.
----------------------------------------------------------------------
```

**Phase Handover Schema (universal -- all 7 exits, Steps 0-6):**

All PHASE-HANDOVER-[N] tables use this schema exactly. Six rows. Fixed field names.
Do not substitute prose. Do not add or remove rows. The Registry-Ref row cites the
Transition-ID from the Phase Transition Registry.

| Field | Content |
|-------|---------|
| Completing Role | [role name and step number] |
| Step Completed | [step number and name] |
| Output Produced | [artifact(s) produced at this exit] |
| Exclusion In Effect | [what the completing role/phase can no longer modify] |
| Receiving Role | [role name and step number taking control] |
| Registry-Ref | [T-NN -- the Transition-ID from the Phase Transition Registry] |

#### Phase Transition Registry

Pre-declared registry of all seven phase transitions. T-ID column assigns stable identifiers
(C-50 preserved). No Consumer-Ref column -- Axis B not present in V-01.

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

### TOKEN CONTENT REQUIREMENT [AXIS A -- C-55]

Every gate token emitted in this artifact must carry inline specifics sufficient to verify its
pass condition without consulting the underlying artifact sections. A token that asserts closure
by label alone -- without naming what it confirmed -- is not self-certifying and fails.

**Required format for MANIFEST-COMPLETE:**

```
MANIFEST-COMPLETE: CIT-[N1]..CIT-[N2] [K] TYPE-A RESOLVED,
  CIT-[M1]..CIT-[M2] [L] TYPE-B RESOLVED,
  CIT-[P1]..CIT-[P2] [Q] TYPE-C RESOLVED --
  citation-completeness verified; no document traversal required
  to confirm all addresses resolve.
```

A MANIFEST-COMPLETE token that omits per-type ID ranges, omits per-type counts, or omits
the "no document traversal" confirmation fails the self-certifying requirement.

**Required format for CONSUMER-INDEX-COMPLETE (when emitted):**

```
CONSUMER-INDEX-COMPLETE: [table-1 heading] Consumer-Ref POPULATED,
  [table-2 heading] Consumer-Ref POPULATED,
  [table-3 heading] Consumer-Ref POPULATED --
  bidirectional navigability confirmed across all three axes.
```

A CONSUMER-INDEX-COMPLETE token naming "all three tables" generically without listing each
table by its heading identity fails. Each of the three table headings must be named
individually.

**Required format for CHAIN-GROUNDING-COMPLETE (when emitted):**

```
CHAIN-GROUNDING-COMPLETE: Belief-Ref cells EXTENDED
  (all MUST-[N] carry confirming artifact reference),
  F-BCR-4 SPECIFIC (names PB-[NN] through PB-[NN]) --
  citation chain verified to evidence; both C-54 conditions confirmed.
```

A CHAIN-GROUNDING-COMPLETE token that omits either condition label ("Belief-Ref cells EXTENDED"
or "F-BCR-4 SPECIFIC") fails. Both conditions must be named in the token body.

**Note:** CONSUMER-INDEX-COMPLETE and CHAIN-GROUNDING-COMPLETE are not produced in this
variation (C-53 and C-54 not implemented). The format declarations above are pre-established
for V-05. MANIFEST-COMPLETE is produced at Step 8 and must conform to its format above.

---

### BC-STEP1-PROTOCOL

Executed by BC during Step 1 in three sequential sub-phases. Write each gate token before
advancing. Do not merge sub-phases.

| Sub-phase | Scope | Gate Token |
|-----------|-------|------------|
| [SCAN] | Read design materials. List all belief candidates. No pruning or evaluation. | `COMMIT-SCAN: [N] candidates identified.` |
| [FREEZE] | Produce PBI from scan results. Lock all PB-[NN] entries. No additions after gate token. | `COMMIT-FREEZE: PBI frozen at [N] entries.` |
| [COVERAGE AUDIT] | Audit domain coverage. Produce BC-COVERAGE-RECORD using schema below. BC exclusion takes effect after this record is written. | BC-COVERAGE-RECORD (schema below). |

#### BC-COVERAGE-RECORD Schema

Each field carries a named field-ID (F-BCR-1 through F-BCR-4). When producing the
BC-COVERAGE-RECORD output, prefix each field header with its schema ID (C-49 preserved).
No Consumer-Ref column -- Axis B not present in V-01.

| F-ID | Field | Content | Constraint |
|------|-------|---------|------------|
| F-BCR-1 | Sub-phase | [COVERAGE AUDIT] -- gate declared in BC-STEP1-PROTOCOL. | Fixed; do not substitute. |
| F-BCR-2 | Materials consulted | [List each design document scanned during [SCAN] and [FREEZE]. Minimum one entry.] | Pre-investigation only. Signal artifacts excluded. |
| F-BCR-3 | Signal artifacts excluded | [List each signal artifact by name; confirm not accessed during Step 1.] | Enumerated by name. |
| F-BCR-4 | PBI completeness basis | [One sentence: which material(s) provide the primary PBI basis.] | Single sentence. |

---

### Step 0 -- [EF] Enforcement Section and Invocation Record

```
ENFORCEMENT MECHANISM DECLARATION
----------------------------------------------------------------------
Provenance tier: STRUCTURAL
Distinguishing property: Role-scope exclusion at three phase boundaries.
  EF writes the cost declaration before signals are read. BC writes
  PBI before signals are read. IA writes corrections from signals and
  cannot alter the frozen PBI or enforcement section. No cross-phase
  reasoning is possible; role boundary is the enforcement mechanism.
Reviewer implication: Independence is enforced by role boundary.
NO-ECHO COST: [EF derives from design materials only -- name the
  specific failure class that propagates if this artifact is not
  produced. Named failure class required. Generic statements fail.]
----------------------------------------------------------------------
```

```
EF-INVOCATION-RECORD
----------------------------------------------------------------------
Step:       0 (EF phase; signal-reading phase not yet open)
Materials consulted (pre-investigation only):
  [List each design document, spec, or proposal consulted.
   Minimum one entry.]
Signal artifacts excluded:
  [List each signal artifact by name. Confirm not accessed at Step 0.]
Cost derivation basis:
  [One sentence: which material grounded the NO-ECHO COST claim.]
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

**[COVERAGE AUDIT]** Produce BC-COVERAGE-RECORD with schema field-IDs in each header.

BC is now excluded from Steps 2-8.

**PHASE-HANDOVER-1** (registry entry: T-01):

| Field | Content |
|-------|---------|
| Completing Role | Belief Cartographer (BC) -- Step 1 |
| Step Completed | Step 1 -- Belief Inventory and Coverage Audit |
| Output Produced | PBI (all PB-[NN] frozen) + BC-COVERAGE-RECORD (F-BCR field-IDs in headers) |
| Exclusion In Effect | BC excluded from Steps 2-8; PBI frozen |
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
          entry verbatim.
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
separate columns. Each MUST-clause carries a stable MUST-ID (C-48 preserved) and a
Belief-Ref column (C-51 preserved) with standard format: `PB-[NN]` only -- Axis C not
present in V-01.

| MUST-ID | Scope | Action | Constraint | Belief-Ref |
|---------|-------|--------|------------|------------|
| MUST-1 | EVERY CANDIDATE -- no exceptions | Produce exactly one of: `STILL-LIVE-[N]: [name]` OR `DISCARD-[N]: [name]` | No candidate evaluation concludes without one of these tokens. | PB-[NN] |
| MUST-2 | EVERY DISCARD-[N] TOKEN -- no exceptions | Immediately write: `DISCARD-[N]-PBI-REF: PB-[NN]` | A DISCARD token without a PBI-Ref token is malformed. | PB-[NN] |
| MUST-3 | EVERY DISCARD-[N] TOKEN -- no exceptions | Immediately write: `DISCARD-[N]-ROUTE: [destination]` | A DISCARD token without a ROUTE token is malformed. | PB-[NN] |
| MUST-4 | EVERY DISCARD-[N] TOKEN -- no exceptions | Immediately write: `DISCARD-[N]-REASON: [one sentence]` | A DISCARD token without a REASON token is malformed. | PB-[NN] |

`DISCARD-LOG-COMPLETE: [N] STILL-LIVE, [M] DISCARD -- all four MUST-clauses applied to every candidate; no candidate unresolved.`

**PHASE-HANDOVER-3** (registry entry: T-03):

| Field | Content |
|-------|---------|
| Completing Role | Institutional Archaeologist (IA) -- Step 3 |
| Step Completed | Step 3 -- Draft All Corrections |
| Output Produced | Draft corrections + STILL-LIVE FILTER output (DISCARD-LOG-COMPLETE) |
| Exclusion In Effect | No new entries or DISCARD tokens after Step 4 begins |
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
| Exclusion In Effect | Field rewrites locked after Step 5 gate |
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
Scope:   HIGH and MEDIUM entries only. LOW excluded.
Format:  [TIER] {Rule -- <=20 words} (encodes: {SURPRISE NAME})
Check:   RULES-ANCHORED traceability -- each rule's tier annotation
         must match Severity of parent entry.
Gate:    RULES-ANCHORED BLOCKS on any MISALIGNED rule.
Closure: After all rules ALIGNED, emit RULES-ANCHORED-COMPLETE.
         Token MUST quote actual tier annotation string per rule.
Token format:
  RULES-ANCHORED-COMPLETE: R-01 "[TIER]" ALIGNED, R-02 "[TIER]"
    ALIGNED, ... -- distillation phase closed.
----------------------------------------------------------------------
```

| Tier | Rule (<=20 words) | Encodes |
|------|-------------------|---------|
| [HIGH] | {rule statement} | {SURPRISE NAME} |
| [MEDIUM] | {rule statement} | {SURPRISE NAME} |

RULES-ANCHORED check and closure token.

**Pattern of inherited errors:** 2-4 sentences. Named structural origin.

**Blind Spot Map:** Categories as types of wrong thinking. Assign each correction.

**Correction Forward Statement:** 1-3 sentences. Name the specific failure this artifact
prevented. Confirm EF's NO-ECHO COST.

**What this correction record excludes:** At least two categories with counts.

---

### Step 8 -- [IA] Citation-Completeness Manifest [AXIS A -- C-52 + C-55 TOKEN FORMAT]

After the artifact is complete at Step 7, produce the CITATION-COMPLETENESS-MANIFEST. The
MANIFEST-COMPLETE token must conform to the TOKEN CONTENT REQUIREMENT declared above: it must
carry per-type ID ranges, per-type counts, and the "no document traversal" confirmation inline.
A token asserting closure without those specifics fails the self-certifying requirement.

```
CITATION-COMPLETENESS-MANIFEST PROTOCOL (C-52)
----------------------------------------------------------------------
Purpose:  Post-artifact citation audit. Every citation point in this
          artifact must appear in this manifest.
Scope:    TYPE-A: F-BCR field-ID citations (4 citations: CIT-01..04)
          TYPE-B: T-ID registry citations (7 citations: CIT-05..11)
          TYPE-C: Belief-Ref citations (one per MUST-clause row)
Status:   RESOLVED -- target address exists and is locatable by ID
          DANGLING -- target address absent or non-locatable
Gate:     Any DANGLING citation halts finalization.
Token:    MANIFEST-COMPLETE must conform to TOKEN CONTENT REQUIREMENT
          (self-certifying format declared above). A token that omits
          per-type ID ranges or counts fails.
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

Self-certifying closure token (must conform to TOKEN CONTENT REQUIREMENT):

`MANIFEST-COMPLETE: CIT-01..CIT-04 [4] TYPE-A RESOLVED, CIT-05..CIT-11 [7] TYPE-B RESOLVED, CIT-12..CIT-[N] [M] TYPE-C RESOLVED -- citation-completeness verified; no document traversal required to confirm all addresses resolve.`

== ARTIFACT STRUCTURE ============================================================

  1. ENFORCEMENT MECHANISM DECLARATION (EF; NO-ECHO COST named)
  2. EF-INVOCATION-RECORD (Step 0)
  3. PHASE-HANDOVER-0 table (6-row schema; Registry-Ref: T-00)
  4. PBI output (BC; COMMIT-SCAN + COMMIT-FREEZE tokens present)
  5. BC-COVERAGE-RECORD (F-BCR field-IDs in all headers)
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
  18. Surprise hierarchy
  19. Pattern of inherited errors
  20. Blind Spot Map
  21. Correction Forward Statement
  22. What this correction record excludes
  23. CITATION-COMPLETENESS-MANIFEST (Step 8; MANIFEST-COMPLETE self-certifying per TOKEN CONTENT REQUIREMENT [C-52 + C-55 partial])
  Note: C-55 FAILS -- CONSUMER-INDEX-COMPLETE and CHAIN-GROUNDING-COMPLETE absent (C-53 C-54 not present)

Write to: simulations/topic/echo/{topic}-echo-{YYYY-MM-DD}.md

---

## V-02 -- Axis B: Gate Independence Enforced (C-56 targeted; C-55 C-57 absent)

**Variation axis:** Lifecycle emphasis -- a named GATE-INDEPENDENCE-ENFORCED declaration is
promoted from a per-step note to a heading-level structural rule, with the canonical constraint
name visible in the prohibition text. At Step 7, CONSUMER-INDEX-COMPLETE is emitted as the sole
gate token; the prohibition declares that if a second gate token co-located at this boundary
it would require independent emission (Axis B only; C-56 targeted).

**Hypothesis:** R17 V-02 demonstrated that Consumer-Ref columns in all three declaring tables
satisfy C-53. C-56 extends the constraint model: when multiple gates close at the same step
boundary, the prohibition against combined tokens must be an explicit named rule, not a note
within a step instruction. R18 V-02 adds a heading-level GATE-INDEPENDENCE-ENFORCED declaration
with the canonical name. The declaration is pre-active: it governs any step where two gates
might co-locate. C-56 fails in V-02 because the dual-gate scenario (C-53+C-54 co-located at
Step 7) never arises -- only CONSUMER-INDEX-COMPLETE is emitted. But the structural rule is
formalized, ready for V-05.

**Expected v18 score:** 310 (C-01 through C-53: all PASS as in R17 V-02; C-52: FAIL; C-54:
FAIL; C-55: FAIL; C-56: FAIL -- prohibition declared but Step-7 dual-gate scenario absent;
C-57: FAIL)

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

**Institutional Archaeologist (IA)** -- Steps 2-7.

```
INSTITUTIONAL ARCHAEOLOGIST -- FUNCTION DECLARATION
----------------------------------------------------------------------
Function:     False-assumption recovery. Correction register only.
              Each IA stage exit (Steps 2-6) produces a PHASE-
              HANDOVER-[N] table before advancing. At Step 7, emit
              CONSUMER-INDEX-COMPLETE (C-53) confirming all three
              declaring tables carry populated Consumer-Ref columns.
              Each gate token is emitted independently per the
              GATE-INDEPENDENCE-ENFORCED declaration below.
Input:        Signal artifacts + frozen PBI (read-only).
Out-of-scope: PBI authorship (frozen). Enforcement section (immutable).
Orienting:    "What would the next team build wrong?"
Phase scope:  Steps 2-7 only. No Step 8 -- Axis A not present.
----------------------------------------------------------------------
```

**Phase Handover Schema:** Six rows including Registry-Ref row (C-50 preserved, identical to V-01).

#### GATE-INDEPENDENCE-ENFORCED [AXIS B -- C-56]

Combined tokens are non-conforming when multiple gates close at the same step boundary.
Each gate emits a separate token with its own inline certification. This constraint is named
GATE-INDEPENDENCE-ENFORCED so that any violation in this artifact or future variation is
citing a named constraint, not an implicit convention.

**Applicability:** This constraint governs Step 7, where CONSUMER-INDEX-COMPLETE is emitted.
If CHAIN-GROUNDING-COMPLETE were also produced at Step 7 (when C-54 is implemented), it would
be required as a separate independent token. A combined token -- e.g.,
"CONSUMER-INDEX-AND-CHAIN-GROUNDING-COMPLETE: [conditions]" -- is non-conforming regardless
of its content. The prohibition applies at any step boundary where two or more gates close
simultaneously.

**Explicit prohibition statement:** Combined tokens at co-located gate boundaries are
non-conforming. Each gate criterion's token is individually falsifiable. Merging tokens
makes individual satisfiability unverifiable and violates this named constraint.

#### Phase Transition Registry [AXIS B -- Consumer-Ref column]

Pre-declared registry of all seven phase transitions. Each T-ID row carries a Consumer-Ref
column naming the inline PHASE-HANDOVER table that cites it -- bidirectionally navigable.

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

Each field carries a named field-ID (F-BCR-1 through F-BCR-4) and a Consumer-Ref column
naming the output step where the field is cited.

| F-ID | Field | Content | Constraint | Consumer-Ref |
|------|-------|---------|------------|--------------|
| F-BCR-1 | Sub-phase | [COVERAGE AUDIT] -- gate declared in BC-STEP1-PROTOCOL. | Fixed; do not substitute. | Consumed-By: [COVERAGE AUDIT] output header in Step 1; PHASE-HANDOVER-1 Output Produced field |
| F-BCR-2 | Materials consulted | [List each design document scanned during [SCAN] and [FREEZE]. Minimum one entry.] | Pre-investigation only. | Consumed-By: [COVERAGE AUDIT] output header in Step 1 |
| F-BCR-3 | Signal artifacts excluded | [List each signal artifact by name.] | Enumerated by name. | Consumed-By: [COVERAGE AUDIT] output header in Step 1 |
| F-BCR-4 | PBI completeness basis | [One sentence: which material(s) provide the primary PBI basis.] | Single sentence. | Consumed-By: [COVERAGE AUDIT] output header in Step 1 |

---

### Steps 0-6

_(Identical to V-01 for all steps. All PHASE-HANDOVER tables carry Registry-Ref rows with
T-ID citations. Step 3 STILL-LIVE FILTER carries Consumer-Ref column as shown below.)_

### Step 3 Extension -- STILL-LIVE FILTER with Consumer-Ref [AXIS B]

Each MUST-clause carries MUST-ID (C-48), Belief-Ref (C-51), and Consumer-Ref (Axis B).

| MUST-ID | Scope | Action | Constraint | Belief-Ref | Consumer-Ref |
|---------|-------|--------|------------|------------|--------------|
| MUST-1 | EVERY CANDIDATE -- no exceptions | Produce exactly one of: `STILL-LIVE-[N]: [name]` OR `DISCARD-[N]: [name]` | No candidate evaluation concludes without one of these tokens. | PB-[NN] | Consumed-By: per-candidate evaluation token in Step 3 |
| MUST-2 | EVERY DISCARD-[N] TOKEN -- no exceptions | Immediately write: `DISCARD-[N]-PBI-REF: PB-[NN]` | A DISCARD token without a PBI-Ref token is malformed. | PB-[NN] | Consumed-By: DISCARD-[N]-PBI-REF token in Step 3 |
| MUST-3 | EVERY DISCARD-[N] TOKEN -- no exceptions | Immediately write: `DISCARD-[N]-ROUTE: [destination]` | A DISCARD token without a ROUTE token is malformed. | PB-[NN] | Consumed-By: DISCARD-[N]-ROUTE token in Step 3 |
| MUST-4 | EVERY DISCARD-[N] TOKEN -- no exceptions | Immediately write: `DISCARD-[N]-REASON: [one sentence]` | A DISCARD token without a REASON token is malformed. | PB-[NN] | Consumed-By: DISCARD-[N]-REASON token in Step 3 |

`DISCARD-LOG-COMPLETE: [N] STILL-LIVE, [M] DISCARD -- all four MUST-clauses applied to every candidate; no candidate unresolved.`

### Step 7 Extension -- Consumer-Index Completeness Gate [AXIS B -- C-53 + C-56 PROHIBITION ACTIVE]

After all artifact content is written at Step 7, emit CONSUMER-INDEX-COMPLETE as an
independent token per the GATE-INDEPENDENCE-ENFORCED constraint.

```
CONSUMER-INDEX-COMPLETE PROTOCOL (C-53)
----------------------------------------------------------------------
Purpose:  Post-content verification that Consumer-Ref columns are
          populated in all three declaring tables simultaneously.
          Partial population (one or two tables) is a gate failure.
Tables:   BC-COVERAGE-RECORD Schema (F-BCR-1..4 Consumer-Ref)
          Phase Transition Registry (T-00..T-06 Consumer-Ref)
          STILL-LIVE FILTER (MUST-1..MUST-4 Consumer-Ref)
Independence: This token is emitted as an independent token per the
          GATE-INDEPENDENCE-ENFORCED constraint above. No combined
          token with any other gate criterion.
----------------------------------------------------------------------
```

`CONSUMER-INDEX-COMPLETE: BC-COVERAGE-RECORD Schema F-BCR-1..F-BCR-4 Consumer-Ref POPULATED, Phase Transition Registry T-00..T-06 Consumer-Ref POPULATED, STILL-LIVE FILTER MUST-1..MUST-4 Consumer-Ref POPULATED -- bidirectional navigability complete across all three axes.`

Note: CHAIN-GROUNDING-COMPLETE is not produced in V-02 (C-54 not present). The
GATE-INDEPENDENCE-ENFORCED prohibition is declared and active but the dual-gate co-location
scenario (C-53+C-54 at Step 7) does not arise in this variation. C-56 is not evaluable.

== ARTIFACT STRUCTURE ============================================================

  1-16. (Same as V-01 items 1-16)
  Note: Phase Transition Registry carries Consumer-Ref column (Axis B)
  Note: BC-COVERAGE-RECORD Schema carries Consumer-Ref column (Axis B)
  Note: GATE-INDEPENDENCE-ENFORCED declaration at heading level (C-56 partial)
  Note: STILL-LIVE FILTER carries Consumer-Ref column (Axis B)
  17. Rules of Thumb (RULES-ANCHORED-COMPLETE)
  18-22. (Hierarchy, errors, map, forward, exclusions)
  23. CONSUMER-INDEX-COMPLETE gate token (Step 7; independent per GATE-INDEPENDENCE-ENFORCED) (C-53)
  No Step 8 manifest -- Axis A not present in V-02.

Write to: simulations/topic/echo/{topic}-echo-{YYYY-MM-DD}.md

---

## V-03 -- Axis C: Manifest-Row Inline Evidence (C-57 targeted; C-55 C-56 absent)

**Variation axis:** Output format -- TYPE-C rows in the CITATION-COMPLETENESS-MANIFEST carry
the confirming artifact in the STATUS CELL as `RESOLVED (confirmed false by: [artifact name,
namespace, date])`, not in the Target Address column. Named MANIFEST-ROW-INLINE-EVIDENCE
block declares the correct placement (Axis C only; C-57 targeted; C-53 absent; C-54 absent).

**Hypothesis:** R17 V-01 demonstrated the CITATION-COMPLETENESS-MANIFEST with TYPE-C rows.
The R17 V-05 implementation placed the confirming artifact in the Target Address column.
C-57 requires it in the STATUS CELL. The placement distinction matters: Target Address names
the destination of the citation; Status is the evidence record for the belief's falsification.
A manifest whose TYPE-C rows have bare RESOLVED in the status cell fails C-57 regardless
of what appears in Target Address. R18 V-03 corrects the placement and adds a named
MANIFEST-ROW-INLINE-EVIDENCE declaration specifying the exact STATUS CELL format. C-57 fails
in V-03 because C-54 (extended Belief-Ref) is absent -- the prerequisite that links each
MUST-clause to its falsifying artifact is not established before the manifest is written.
But the STATUS cell placement rule is formalized and ready for V-05.

**Expected v18 score:** 310 (C-01 through C-52: all PASS as in R17 V-01 base; C-53: FAIL;
C-54: FAIL; C-55: FAIL; C-56: FAIL; C-57: FAIL -- C-54 prerequisite absent)

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
              HANDOVER-[N] table before advancing. At Step 8, produce
              the CITATION-COMPLETENESS-MANIFEST. TYPE-C rows must
              carry the confirming artifact in the STATUS CELL per
              the MANIFEST-ROW-INLINE-EVIDENCE declaration below.
              TYPE-C rows with bare RESOLVED in the status cell fail.
Input:        Signal artifacts + frozen PBI (read-only).
Out-of-scope: PBI authorship (frozen). Enforcement section (immutable).
Orienting:    "What would the next team build wrong?"
Phase scope:  Steps 2-8 only.
----------------------------------------------------------------------
```

**Phase Handover Schema:** Six rows including Registry-Ref row (C-50 preserved).

**Phase Transition Registry:** T-ID column present (C-50 preserved). No Consumer-Ref column
-- Axis B not present in V-03. Identical to V-01.

---

### MANIFEST-ROW-INLINE-EVIDENCE [AXIS C -- C-57]

TYPE-C rows in the CITATION-COMPLETENESS-MANIFEST carry the confirming artifact in the
STATUS CELL, not in the Target Address column.

**Required STATUS CELL format for TYPE-C rows:**

```
RESOLVED (confirmed false by: [artifact name, namespace, date])
```

A TYPE-C row with bare `RESOLVED` in the status cell fails -- the status cell is the evidence
record, not a resolution flag. A TYPE-C row that places the confirming artifact in Target
Address but uses bare `RESOLVED` in the status cell also fails -- placement in the status cell
is required.

**TYPE-A and TYPE-B rows** use bare `RESOLVED` status. This extension applies to TYPE-C only:
their RESOLVED status reflects belief falsification, and the falsifying artifact must be
inline in that status cell.

**Prerequisite note:** This declaration is effective only when C-54 (extended Belief-Ref
cells in the STILL-LIVE FILTER) is also satisfied. C-54 establishes the confirming artifact
attribution for each MUST-clause; the manifest TYPE-C rows inherit that attribution into the
status cell. Without C-54, there is no confirming artifact to place in the status cell. C-57
fails in this variation because C-54 is absent.

---

### BC-STEP1-PROTOCOL

_(Identical to V-01: three sub-phases, BC-COVERAGE-RECORD Schema without Consumer-Ref.)_

---

### Steps 0-6

_(Identical to V-01. STILL-LIVE FILTER uses standard Belief-Ref cells: `PB-[NN]` only --
Axis C not present in Steps 0-6. No extended format; C-54 not implemented.)_

---

### Step 7

_(Identical to V-01 Step 7: Hierarchy, Distillation, Forward Handover. No gate tokens at
Step 7 -- Axis B not present.)_

---

### Step 8 -- [IA] Citation-Completeness Manifest [AXIS A -- C-52 + C-57 PLACEMENT DECLARED]

After the artifact is complete at Step 7, produce the CITATION-COMPLETENESS-MANIFEST. Apply
the MANIFEST-ROW-INLINE-EVIDENCE declaration: TYPE-C rows carry the confirming artifact in
the STATUS CELL, not in Target Address. MANIFEST-COMPLETE uses standard format (C-52).

```
CITATION-COMPLETENESS-MANIFEST PROTOCOL (C-52 + C-57 PLACEMENT)
----------------------------------------------------------------------
TYPE-A rows:  RESOLVED (bare) -- structural/schema citation.
TYPE-B rows:  RESOLVED (bare) -- registry/handover citation.
TYPE-C rows:  RESOLVED (confirmed false by: [artifact name,
              namespace, date]) -- belief falsification citation.
              Bare RESOLVED in TYPE-C status cell FAILS (C-57).
              Confirming artifact in Target Address only FAILS (C-57).
Note:         C-57 requires C-54 as prerequisite. C-54 not present
              in V-03. C-57 therefore fails despite correct placement
              declaration -- the Belief-Ref cells are not extended
              to carry confirming artifacts, so there is no artifact
              to place in the TYPE-C status cell. This declaration
              is pre-established for V-05.
----------------------------------------------------------------------
```

| Citation-ID | Citation Type | Source Location | Target Address | Status |
|-------------|--------------|-----------------|----------------|--------|
| CIT-01 | TYPE-A | BC-COVERAGE-RECORD output header "F-BCR-1" | BC-COVERAGE-RECORD Schema row F-BCR-1 | RESOLVED |
| CIT-02 | TYPE-A | BC-COVERAGE-RECORD output header "F-BCR-2" | BC-COVERAGE-RECORD Schema row F-BCR-2 | RESOLVED |
| CIT-03 | TYPE-A | BC-COVERAGE-RECORD output header "F-BCR-3" | BC-COVERAGE-RECORD Schema row F-BCR-3 | RESOLVED |
| CIT-04 | TYPE-A | BC-COVERAGE-RECORD output header "F-BCR-4" | BC-COVERAGE-RECORD Schema row F-BCR-4 | RESOLVED |
| CIT-05..11 | TYPE-B | PHASE-HANDOVER-[0..6] Registry-Ref rows | Phase Transition Registry T-00..T-06 | RESOLVED |
| CIT-[N] | TYPE-C | STILL-LIVE FILTER MUST-[N] Belief-Ref cell | PBI row PB-[NN] | RESOLVED (confirmed false by: [artifact name, namespace, date]) |

`MANIFEST-COMPLETE: CIT-01..CIT-04 [4] TYPE-A RESOLVED, CIT-05..CIT-11 [7] TYPE-B RESOLVED, CIT-12..CIT-[N] [M] TYPE-C RESOLVED -- citation-completeness verified.`

== ARTIFACT STRUCTURE ============================================================

  1-22. (Same as V-01 items 1-22)
  Note: MANIFEST-ROW-INLINE-EVIDENCE declaration at heading level (C-57 declared but FAIL)
  Note: TYPE-C STATUS CELL format declared: RESOLVED (confirmed false by: ...)
  23. CITATION-COMPLETENESS-MANIFEST (Step 8; MANIFEST-COMPLETE token; TYPE-C STATUS cell format declared but C-57 FAILS -- C-54 absent)

Write to: simulations/topic/echo/{topic}-echo-{YYYY-MM-DD}.md

---

## V-04 -- Axes A+B: Token Self-Certifying + Gate Independence (C-55+C-56 targeted; C-57 absent)

**Variation axis:** Output format + lifecycle emphasis -- TOKEN CONTENT REQUIREMENT (Axis A)
and GATE-INDEPENDENCE-ENFORCED (Axis B) both active; MANIFEST-COMPLETE and CONSUMER-INDEX-COMPLETE
emitted as independent self-certifying tokens; prohibition explicit at heading level. No Axis C
(C-54 absent; no extended Belief-Ref; no CHAIN-GROUNDING-COMPLETE).

**Hypothesis:** V-01 demonstrated the self-certifying token format for MANIFEST-COMPLETE.
V-02 demonstrated the gate independence prohibition as a heading-level declaration. V-04 asks
whether combining both produces a structural property neither achieves alone: the manifest
token confirms citation-type completeness (Axis A) and the independence prohibition ensures the
two Step-7-area gate tokens are individually falsifiable (Axis B). Without Axis C, the third
token (CHAIN-GROUNDING-COMPLETE) is absent -- C-55 cannot be satisfied (requires all three
tokens), and C-56 cannot be satisfied (requires C-53+C-54 co-location). C-57 also fails
(C-54 absent). V-04 scores the same as R17 V-04 under v18.

**Expected v18 score:** 315 (C-01 through C-52+C-53: all PASS; C-54: FAIL; C-55: FAIL --
CHAIN-GROUNDING-COMPLETE absent, C-55 requires all three tokens; C-56: FAIL -- C-54 absent,
dual-gate co-location does not arise; C-57: FAIL)

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
              CONSUMER-INDEX-COMPLETE independently per the
              GATE-INDEPENDENCE-ENFORCED declaration. At Step 8,
              produce the CITATION-COMPLETENESS-MANIFEST with a
              self-certifying MANIFEST-COMPLETE token per the
              TOKEN CONTENT REQUIREMENT declaration.
Input:        Signal artifacts + frozen PBI (read-only).
Out-of-scope: PBI authorship (frozen). Enforcement section (immutable).
Orienting:    "What would the next team build wrong?"
Phase scope:  Steps 2-8 only.
----------------------------------------------------------------------
```

**Phase Handover Schema:** Six rows including Registry-Ref row (identical to V-01).

#### TOKEN CONTENT REQUIREMENT [AXIS A -- C-55 partial]

_(Full declaration identical to V-01 TOKEN CONTENT REQUIREMENT. All three token formats
pre-declared. MANIFEST-COMPLETE and CONSUMER-INDEX-COMPLETE are produced in V-04 and must
conform. CHAIN-GROUNDING-COMPLETE is not produced -- C-54 absent. C-55 fails because all
three tokens are required to be self-certifying; one is absent.)_

#### GATE-INDEPENDENCE-ENFORCED [AXIS B -- C-56 partial]

_(Full declaration identical to V-02 GATE-INDEPENDENCE-ENFORCED. Combined tokens at
co-located gate boundaries are non-conforming. The prohibition is named and active.
C-56 fails because the dual-gate co-location case requires C-53+C-54 simultaneously;
C-54 is absent in V-04.)_

#### Phase Transition Registry [AXIS B -- Consumer-Ref column]

_(Identical to V-02: Consumer-Ref column present in all seven rows.)_

| T-ID | Transition | Step Completed | Completing Role | Receiving Role | Consumer-Ref |
|------|------------|----------------|-----------------|----------------|--------------|
| T-00 | PHASE-HANDOVER-0 | Step 0 -- Enforcement Section | Enforcement Framer (EF) | Belief Cartographer (BC) | Consumed-By: PHASE-HANDOVER-0 Registry-Ref row |
| T-01 | PHASE-HANDOVER-1 | Step 1 -- Belief Inventory | Belief Cartographer (BC) | Institutional Archaeologist (IA) | Consumed-By: PHASE-HANDOVER-1 Registry-Ref row |
| T-02 | PHASE-HANDOVER-2 | Step 2 -- Handle Ledger | Institutional Archaeologist (IA) | Institutional Archaeologist (IA) | Consumed-By: PHASE-HANDOVER-2 Registry-Ref row |
| T-03 | PHASE-HANDOVER-3 | Step 3 -- Draft All Corrections | Institutional Archaeologist (IA) | Institutional Archaeologist (IA) | Consumed-By: PHASE-HANDOVER-3 Registry-Ref row |
| T-04 | PHASE-HANDOVER-4 | Step 4 -- Register Audit | Institutional Archaeologist (IA) | Institutional Archaeologist (IA) | Consumed-By: PHASE-HANDOVER-4 Registry-Ref row |
| T-05 | PHASE-HANDOVER-5 | Step 5 -- Entry Gate | Institutional Archaeologist (IA) | Institutional Archaeologist (IA) | Consumed-By: PHASE-HANDOVER-5 Registry-Ref row |
| T-06 | PHASE-HANDOVER-6 | Step 6 -- Chain Integrity Audit | Institutional Archaeologist (IA) | Institutional Archaeologist (IA) | Consumed-By: PHASE-HANDOVER-6 Registry-Ref row |

---

### BC-STEP1-PROTOCOL

_(Three sub-phases identical to V-01.)_

#### BC-COVERAGE-RECORD Schema [AXIS B -- Consumer-Ref column]

_(Identical to V-02: Consumer-Ref column present in all four rows. F-BCR-4 uses standard
single-sentence format -- Axis C absent.)_

| F-ID | Field | Content | Constraint | Consumer-Ref |
|------|-------|---------|------------|--------------|
| F-BCR-1 | Sub-phase | [COVERAGE AUDIT] | Fixed. | Consumed-By: [COVERAGE AUDIT] output header; PHASE-HANDOVER-1 Output Produced |
| F-BCR-2 | Materials consulted | [List each design document.] | Pre-investigation only. | Consumed-By: [COVERAGE AUDIT] output header |
| F-BCR-3 | Signal artifacts excluded | [List each signal artifact by name.] | Enumerated by name. | Consumed-By: [COVERAGE AUDIT] output header |
| F-BCR-4 | PBI completeness basis | [One sentence: primary PBI basis.] | Single sentence. | Consumed-By: [COVERAGE AUDIT] output header |

---

### Steps 0-6

_(Identical to V-01 except Step 3 STILL-LIVE FILTER carries Consumer-Ref column [Axis B]
with standard Belief-Ref cells: `PB-[NN]` only -- Axis C not present in V-04.)_

### Step 3 Extension -- STILL-LIVE FILTER with Consumer-Ref [AXIS B]

_(Identical to V-02 Step 3 Extension: MUST-ID + Scope + Action + Constraint + Belief-Ref
(PB-[NN] only) + Consumer-Ref columns.)_

### Step 7 Extension -- Consumer-Index Gate [AXIS B -- C-53 + GATE-INDEPENDENCE-ENFORCED ACTIVE]

After all artifact content is written at Step 7, emit CONSUMER-INDEX-COMPLETE as an
independent token. Per the GATE-INDEPENDENCE-ENFORCED declaration, this token must not
be combined with any other gate token even if a second gate were present at this boundary.

`CONSUMER-INDEX-COMPLETE: BC-COVERAGE-RECORD Schema F-BCR-1..F-BCR-4 Consumer-Ref POPULATED, Phase Transition Registry T-00..T-06 Consumer-Ref POPULATED, STILL-LIVE FILTER MUST-1..MUST-4 Consumer-Ref POPULATED -- bidirectional navigability complete across all three axes.`

Note: CHAIN-GROUNDING-COMPLETE is absent (C-54 not present). The Step-7 dual-gate
co-location case does not arise. GATE-INDEPENDENCE-ENFORCED is declared and active but
C-56 is not evaluable in this variation.

### Step 8 -- [IA] Citation-Completeness Manifest [AXIS A -- C-52 + TOKEN CONTENT REQUIREMENT ACTIVE]

_(Manifest protocol identical to V-01. MANIFEST-COMPLETE token must conform to TOKEN CONTENT
REQUIREMENT: per-type ID ranges, per-type counts, and traversal confirmation inline. TYPE-C
rows use standard Target Address format: `PBI row PB-[NN]` -- Axis C placement not implemented;
MANIFEST-ROW-INLINE-EVIDENCE not present in V-04.)_

`MANIFEST-COMPLETE: CIT-01..CIT-04 [4] TYPE-A RESOLVED, CIT-05..CIT-11 [7] TYPE-B RESOLVED, CIT-12..CIT-[N] [M] TYPE-C RESOLVED -- citation-completeness verified; no document traversal required to confirm all addresses resolve.`

== ARTIFACT STRUCTURE ============================================================

  1-16. (Same as V-01 items 1-16)
  Note: Phase Transition Registry carries Consumer-Ref column (Axis B)
  Note: BC-COVERAGE-RECORD Schema carries Consumer-Ref column (Axis B)
  Note: GATE-INDEPENDENCE-ENFORCED declaration at heading level (Axis B)
  Note: TOKEN CONTENT REQUIREMENT declaration (Axis A)
  Note: STILL-LIVE FILTER carries Consumer-Ref column (Axis B)
  17-22. (Hierarchy, errors, map, forward, exclusions)
  23. CONSUMER-INDEX-COMPLETE token (Step 7; independent; self-certifying format) (C-53)
  24. CITATION-COMPLETENESS-MANIFEST (Step 8; self-certifying MANIFEST-COMPLETE) (C-52)
  Note: C-55 FAILS -- CHAIN-GROUNDING-COMPLETE absent; C-56 FAILS -- C-54 absent; C-57 FAILS -- C-54 absent

Write to: simulations/topic/echo/{topic}-echo-{YYYY-MM-DD}.md

---

## V-05 -- Axes A+B+C: Full Closure-Layer Audit (C-55+C-56+C-57 all targeted)

**Variation axis:** Full integration -- TOKEN CONTENT REQUIREMENT (Axis A for C-55), named
GATE-INDEPENDENCE-ENFORCED at heading level (Axis B for C-56), and MANIFEST-ROW-INLINE-EVIDENCE
in STATUS CELL (Axis C for C-57) all active simultaneously; C-52+C-53+C-54 all present as
prerequisites; Step 7 emits CONSUMER-INDEX-COMPLETE and CHAIN-GROUNDING-COMPLETE as independent
self-certifying tokens; Step 8 TYPE-C rows carry confirming artifact in STATUS CELL.

**Hypothesis:** V-01, V-02, V-03 each isolate one new structural property. V-04 demonstrated
that Axis A and Axis B corroborate each other. V-05 asks whether all three simultaneously
produce a closed closure-layer audit: (1) every gate token is self-certifying -- a reviewer
can verify any token's pass condition from token text alone without section traversal (C-55);
(2) Step 7's two co-located gate tokens are independently falsifiable -- CONSUMER-INDEX-COMPLETE
can pass while CHAIN-GROUNDING-COMPLETE fails, which a combined token would obscure (C-56);
(3) each TYPE-C manifest row is a terminal evidence record -- citation ID, type, belief
reference, status, and falsifying artifact all in a single row without traversal (C-57). The
three properties form a coherent closure-layer contract: tokens certify themselves (C-55),
gates don't collapse into each other (C-56), manifest rows don't defer to other sections (C-57).

**Expected v18 score:** 335 (all 57 criteria: PASS)

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
              COMPLETE (C-54) as INDEPENDENT tokens per the
              GATE-INDEPENDENCE-ENFORCED constraint -- combined
              tokens at this boundary are non-conforming. Each token
              must be self-certifying per the TOKEN CONTENT
              REQUIREMENT declaration. At Step 8, produce the
              CITATION-COMPLETENESS-MANIFEST (C-52) with a self-
              certifying MANIFEST-COMPLETE token; TYPE-C rows carry
              the confirming artifact in the STATUS CELL per
              MANIFEST-ROW-INLINE-EVIDENCE. All three gate tokens
              are required; any absent or non-self-certifying token
              is an incompletion.
Input:        Signal artifacts + frozen PBI (read-only).
Out-of-scope: PBI authorship (frozen). Enforcement section (immutable).
Orienting:    "What would the next team build wrong?"
Phase scope:  Steps 2-8 only.
----------------------------------------------------------------------
```

**Phase Handover Schema:** Six rows including Registry-Ref row (identical to V-01).

#### TOKEN CONTENT REQUIREMENT [AXIS A -- C-55]

Every gate token emitted in this artifact must carry inline specifics sufficient to verify
its pass condition without consulting the underlying sections. This requirement applies to
all three gate tokens: MANIFEST-COMPLETE, CONSUMER-INDEX-COMPLETE, and CHAIN-GROUNDING-COMPLETE.

**Required format for MANIFEST-COMPLETE:**

```
MANIFEST-COMPLETE: CIT-[N1]..CIT-[N2] [K] TYPE-A RESOLVED,
  CIT-[M1]..CIT-[M2] [L] TYPE-B RESOLVED,
  CIT-[P1]..CIT-[P2] [Q] TYPE-C RESOLVED --
  citation-completeness verified; no document traversal required
  to confirm all addresses resolve.
```

A token omitting per-type ID ranges, counts, or traversal confirmation fails.

**Required format for CONSUMER-INDEX-COMPLETE:**

```
CONSUMER-INDEX-COMPLETE: BC-COVERAGE-RECORD Schema [F-BCR-1..F-BCR-4]
  Consumer-Ref POPULATED, Phase Transition Registry [T-00..T-06]
  Consumer-Ref POPULATED, STILL-LIVE FILTER [MUST-1..MUST-4]
  Consumer-Ref POPULATED -- bidirectional navigability confirmed
  across all three axes.
```

Each of the three table headings must be named individually with their ID ranges. A token
naming "all three tables" generically without individual headings fails.

**Required format for CHAIN-GROUNDING-COMPLETE:**

```
CHAIN-GROUNDING-COMPLETE: Belief-Ref cells EXTENDED
  (all MUST-[N] carry confirming artifact reference),
  F-BCR-4 SPECIFIC (names PB-[NN] through PB-[NN]) --
  citation chain verified to evidence; both C-54 conditions confirmed.
```

Both condition labels must be present in the token body. A token missing either label fails.

#### GATE-INDEPENDENCE-ENFORCED [AXIS B -- C-56]

Combined tokens are non-conforming when multiple gates close at the same step boundary.
This constraint is named GATE-INDEPENDENCE-ENFORCED so that any violation is citing a named
constraint. Each gate criterion's token is individually falsifiable; merging tokens makes
individual satisfiability unverifiable and violates this constraint.

**Step 7 application:** CONSUMER-INDEX-COMPLETE and CHAIN-GROUNDING-COMPLETE both close at
Step 7. They must be emitted as separate independent tokens. A combined token -- e.g.,
"CONSUMER-INDEX-AND-CHAIN-GROUNDING-COMPLETE: [conditions]" -- is non-conforming regardless
of its content. This prohibition is stated here explicitly so future variations cannot merge
these tokens for brevity without overriding a named constraint.

**Explicit prohibition statement:** At any step boundary where two or more gate criteria close
simultaneously, combined tokens are non-conforming. Each gate emits a separate token with
its own inline certification per the TOKEN CONTENT REQUIREMENT above.

#### MANIFEST-ROW-INLINE-EVIDENCE [AXIS C -- C-57]

TYPE-C rows in the CITATION-COMPLETENESS-MANIFEST carry the confirming artifact in the
STATUS CELL:

```
RESOLVED (confirmed false by: [artifact name, namespace, date])
```

A TYPE-C row with bare RESOLVED in the status cell fails. A TYPE-C row placing the confirming
artifact in Target Address but using bare RESOLVED in the status cell also fails. The status
cell is the evidence record for belief falsification; the confirming artifact must be inline
in that cell, not deferred to another column. TYPE-A and TYPE-B rows use bare RESOLVED.

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

Each field carries F-ID (C-49), Consumer-Ref column (Axis B), and F-BCR-4 requires specific
PBI entry names in output (Axis C).

| F-ID | Field | Content | Constraint | Consumer-Ref |
|------|-------|---------|------------|--------------|
| F-BCR-1 | Sub-phase | [COVERAGE AUDIT] | Fixed. | Consumed-By: [COVERAGE AUDIT] output header; PHASE-HANDOVER-1 Output Produced |
| F-BCR-2 | Materials consulted | [List each design document.] | Pre-investigation only. | Consumed-By: [COVERAGE AUDIT] output header |
| F-BCR-3 | Signal artifacts excluded | [List each signal artifact by name.] | Enumerated. | Consumed-By: [COVERAGE AUDIT] output header |
| F-BCR-4 | PBI completeness basis | [Name specific PBI entries: "PB-NN through PB-NN (from material name)." Generic sentence fails C-54.] | Names specific PB-[NN] entries. C-54 condition. | Consumed-By: [COVERAGE AUDIT] output header |

**F-BCR-4 Axis C requirement:** The F-BCR-4 output must name specific PBI entries in the
format: `F-BCR-4: PBI completeness basis -- PB-[NN1] through PB-[NNk] (from [material name]).`
A generic sentence such as "design spec provided the primary basis" fails C-54 condition 2.

---

### Steps 0-6

_(Identical to V-01 except Step 3 STILL-LIVE FILTER carries both Consumer-Ref column [Axis B]
and extended Belief-Ref cells [Axis C] as shown below.)_

### Step 3 Extension -- STILL-LIVE FILTER [AXIS B + AXIS C]

Each MUST-clause carries MUST-ID (C-48), extended Belief-Ref (Axis C), and Consumer-Ref
(Axis B).

**Belief-Ref format (C-54 condition 1):** `PB-[NN] (confirmed false by: [artifact name, namespace, date])`
**Consumer-Ref format (C-53):** `Consumed-By: [enforcement site and step]`

| MUST-ID | Scope | Action | Constraint | Belief-Ref | Consumer-Ref |
|---------|-------|--------|------------|------------|--------------|
| MUST-1 | EVERY CANDIDATE -- no exceptions | Produce exactly one of: `STILL-LIVE-[N]: [name]` OR `DISCARD-[N]: [name]` | No candidate evaluation concludes without one of these tokens. | PB-[NN] (confirmed false by: [artifact name, namespace, date]) | Consumed-By: per-candidate evaluation token in Step 3 |
| MUST-2 | EVERY DISCARD-[N] TOKEN -- no exceptions | Immediately write: `DISCARD-[N]-PBI-REF: PB-[NN]` | A DISCARD token without a PBI-Ref token is malformed. | PB-[NN] (confirmed false by: [artifact name, namespace, date]) | Consumed-By: DISCARD-[N]-PBI-REF token in Step 3 |
| MUST-3 | EVERY DISCARD-[N] TOKEN -- no exceptions | Immediately write: `DISCARD-[N]-ROUTE: [destination]` | A DISCARD token without a ROUTE token is malformed. | PB-[NN] (confirmed false by: [artifact name, namespace, date]) | Consumed-By: DISCARD-[N]-ROUTE token in Step 3 |
| MUST-4 | EVERY DISCARD-[N] TOKEN -- no exceptions | Immediately write: `DISCARD-[N]-REASON: [one sentence]` | A DISCARD token without a REASON token is malformed. | PB-[NN] (confirmed false by: [artifact name, namespace, date]) | Consumed-By: DISCARD-[N]-REASON token in Step 3 |

`DISCARD-LOG-COMPLETE: [N] STILL-LIVE, [M] DISCARD -- all four MUST-clauses applied to every candidate; no candidate unresolved.`

---

### Step 7 Extension -- Consumer-Index + Chain-Grounding Gates [C-53 + C-54 + GATE-INDEPENDENCE-ENFORCED + TOKEN CONTENT REQUIREMENT]

After all artifact content is written at Step 7, emit both completeness gates as independent
tokens. Per GATE-INDEPENDENCE-ENFORCED, combined tokens are non-conforming. Per TOKEN CONTENT
REQUIREMENT, each token must be self-certifying. Emit Gate 1 first, then Gate 2 as a separate
independent token.

**Gate 1 (C-53) -- self-certifying, independent:**

`CONSUMER-INDEX-COMPLETE: BC-COVERAGE-RECORD Schema F-BCR-1..F-BCR-4 Consumer-Ref POPULATED, Phase Transition Registry T-00..T-06 Consumer-Ref POPULATED, STILL-LIVE FILTER MUST-1..MUST-4 Consumer-Ref POPULATED -- bidirectional navigability confirmed across all three axes.`

**Gate 2 (C-54) -- self-certifying, independent:**

`CHAIN-GROUNDING-COMPLETE: Belief-Ref cells EXTENDED (all MUST-[N] carry confirming artifact reference), F-BCR-4 SPECIFIC (names PB-[NN] through PB-[NN]) -- citation chain verified to evidence; both C-54 conditions confirmed.`

These two tokens are at the same step boundary. Per GATE-INDEPENDENCE-ENFORCED, they are
emitted as separate tokens. A combined token is non-conforming.

---

### Step 8 -- [IA] Citation-Completeness Manifest [AXIS A -- C-52 + C-55 TOKEN CONTENT + C-57 STATUS CELL]

After the Step 7 gates are confirmed, produce the CITATION-COMPLETENESS-MANIFEST. Apply
both active Axis declarations:
- TOKEN CONTENT REQUIREMENT (Axis A): MANIFEST-COMPLETE token is self-certifying with
  per-type ID ranges, counts, and traversal confirmation.
- MANIFEST-ROW-INLINE-EVIDENCE (Axis C): TYPE-C rows carry confirming artifact in the STATUS
  CELL: `RESOLVED (confirmed false by: [artifact name, namespace, date])`.

```
CITATION-COMPLETENESS-MANIFEST PROTOCOL (C-52 + C-55 SELF-CERTIFYING + C-57 STATUS CELL)
----------------------------------------------------------------------
TYPE-A rows:  RESOLVED (bare) -- schema field-ID citation.
TYPE-B rows:  RESOLVED (bare) -- registry T-ID citation.
TYPE-C rows:  RESOLVED (confirmed false by: [artifact name,
              namespace, date]) -- STATUS CELL carries confirming
              artifact. Bare RESOLVED in TYPE-C status cell FAILS.
              Confirming artifact in Target Address only FAILS.
Gate:         Any DANGLING citation halts finalization.
Token:        MANIFEST-COMPLETE must be self-certifying per TOKEN
              CONTENT REQUIREMENT: per-type ID ranges, counts, and
              "no document traversal" confirmation inline.
----------------------------------------------------------------------
```

| Citation-ID | Citation Type | Source Location | Target Address | Status |
|-------------|--------------|-----------------|----------------|--------|
| CIT-01 | TYPE-A | BC-COVERAGE-RECORD output header "F-BCR-1: Sub-phase" | BC-COVERAGE-RECORD Schema row F-BCR-1 | RESOLVED |
| CIT-02 | TYPE-A | BC-COVERAGE-RECORD output header "F-BCR-2: Materials consulted" | BC-COVERAGE-RECORD Schema row F-BCR-2 | RESOLVED |
| CIT-03 | TYPE-A | BC-COVERAGE-RECORD output header "F-BCR-3: Signal artifacts excluded" | BC-COVERAGE-RECORD Schema row F-BCR-3 | RESOLVED |
| CIT-04 | TYPE-A | BC-COVERAGE-RECORD output header "F-BCR-4: PBI completeness basis" | BC-COVERAGE-RECORD Schema row F-BCR-4 | RESOLVED |
| CIT-05 | TYPE-B | PHASE-HANDOVER-0 Registry-Ref row | Phase Transition Registry row T-00 | RESOLVED |
| CIT-06 | TYPE-B | PHASE-HANDOVER-1 Registry-Ref row | Phase Transition Registry row T-01 | RESOLVED |
| CIT-07 | TYPE-B | PHASE-HANDOVER-2 Registry-Ref row | Phase Transition Registry row T-02 | RESOLVED |
| CIT-08 | TYPE-B | PHASE-HANDOVER-3 Registry-Ref row | Phase Transition Registry row T-03 | RESOLVED |
| CIT-09 | TYPE-B | PHASE-HANDOVER-4 Registry-Ref row | Phase Transition Registry row T-04 | RESOLVED |
| CIT-10 | TYPE-B | PHASE-HANDOVER-5 Registry-Ref row | Phase Transition Registry row T-05 | RESOLVED |
| CIT-11 | TYPE-B | PHASE-HANDOVER-6 Registry-Ref row | Phase Transition Registry row T-06 | RESOLVED |
| CIT-[N] | TYPE-C | STILL-LIVE FILTER MUST-[N] Belief-Ref cell | PBI row PB-[NN] | RESOLVED (confirmed false by: [artifact name, namespace, date]) |

Self-certifying closure token (TOKEN CONTENT REQUIREMENT + MANIFEST-ROW-INLINE-EVIDENCE both satisfied):

`MANIFEST-COMPLETE: CIT-01..CIT-04 [4] TYPE-A RESOLVED, CIT-05..CIT-11 [7] TYPE-B RESOLVED, CIT-12..CIT-[N] [M] TYPE-C RESOLVED -- citation-completeness verified; no document traversal required to confirm all addresses resolve.`

== ARTIFACT STRUCTURE ============================================================

  1. ENFORCEMENT MECHANISM DECLARATION (EF; NO-ECHO COST named)
  2. EF-INVOCATION-RECORD (Step 0)
  3. PHASE-HANDOVER-0 table (6-row schema; Registry-Ref: T-00)
  4. PBI output (BC; COMMIT-SCAN + COMMIT-FREEZE tokens present)
  5. BC-COVERAGE-RECORD (F-BCR field-IDs in all headers; F-BCR-4 names specific PBI entries [Axis C])
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
  23. CONSUMER-INDEX-COMPLETE gate token (Step 7; independent; self-certifying per TOKEN CONTENT REQUIREMENT) (C-53 + C-55 partial)
  24. CHAIN-GROUNDING-COMPLETE gate token (Step 7; independent; self-certifying per TOKEN CONTENT REQUIREMENT) (C-54 + C-55 partial)
      Note: Gates 23 and 24 are independent per GATE-INDEPENDENCE-ENFORCED (C-56)
  25. CITATION-COMPLETENESS-MANIFEST (Step 8; self-certifying MANIFEST-COMPLETE; TYPE-C STATUS CELL carries confirming artifact) (C-52 + C-55 + C-57)

Write to: simulations/topic/echo/{topic}-echo-{YYYY-MM-DD}.md

---

## Variation Summary

| # | Axis | New R18 Declarations | C-55 | C-56 | C-57 | v18 score |
|---|------|---------------------|:----:|:----:|:----:|:---------:|
| V-01 | A only | TOKEN CONTENT REQUIREMENT | FAIL | FAIL | FAIL | 310 |
| V-02 | B only | GATE-INDEPENDENCE-ENFORCED | FAIL | FAIL | FAIL | 310 |
| V-03 | C only | MANIFEST-ROW-INLINE-EVIDENCE | FAIL | FAIL | FAIL | 310 |
| V-04 | A+B | TOKEN CONTENT REQUIREMENT + GATE-INDEPENDENCE-ENFORCED | FAIL | FAIL | FAIL | 315 |
| **V-05** | **A+B+C** | **All three** | **PASS** | **PASS** | **PASS** | **335** |

**R18 structural contribution beyond R17:**

Each new criterion gets its own named heading-level declaration that makes the format
requirement formally binding and citation-stable:

- C-55: TOKEN CONTENT REQUIREMENT names exact token formats -- a prompt without this block
  cannot be verified as self-certifying from the prompt text alone. The block is the
  structural guarantee that each token's content is specified before execution begins.
- C-56: GATE-INDEPENDENCE-ENFORCED is promoted from a per-step note to a named structural
  constraint. Citation-stable naming means the constraint can be cited by name in future
  variations, rubric criteria, and failure diagnoses without re-reading the step instruction.
- C-57: MANIFEST-ROW-INLINE-EVIDENCE names the STATUS CELL placement rule explicitly.
  The distinction between Target Address and Status is non-obvious; a named declaration
  prevents the Target Address misplacement from recurring in future variations.

The three declarations form a coherent R18 closure-layer contract: tokens certify themselves
(TOKEN CONTENT REQUIREMENT), gates don't collapse (GATE-INDEPENDENCE-ENFORCED), manifest
rows don't defer (MANIFEST-ROW-INLINE-EVIDENCE).
