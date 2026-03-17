---
skill: quest-variate
skill_target: topic-echo
date: 2026-03-16
round: 16
rubric: v16
rubric_file: simulations/quest/rubrics/topic-echo-rubric-v16-2026-03-16.md
rubric_max: 305
---

# Variations: `topic:echo` -- Round 16 (2026-03-16)

**Rubric:** v16 (2026-03-16) | **Criteria:** 51 (5 essential / 3 recommended / 43 aspirational)

---

## Design Context

R15 V-05 achieves 305/305 under v16. The three citation-activation criteria formalized in v16 --
BC-COVERAGE-RECORD-SCHEMA-FIELD-ID-CITATION (C-49), PHASE-HANDOVER-REGISTRY-TRANSITION-ID-CITATION
(C-50), and MUST-CLAUSE-BELIEF-REF-CITATION (C-51) -- are satisfied by R15's three-axis
implementations. Round 16 does not re-implement R15's axes. It tests whether adding explicit
**citation-completeness verification, bidirectional navigability, and PBI-grounded chain depth**
to each R15 citation creates observable structural properties that could become v17 criteria.

R15 made each address citation-active: BC-COVERAGE-RECORD output headers carry F-BCR field-IDs
(C-49); each PHASE-HANDOVER table includes a Registry-Ref row citing its T-ID (C-50); each
MUST-clause carries a Belief-Ref column naming its PBI anchor (C-51). Each citation is present --
a reviewer can follow it -- but the citation set's completeness is not explicitly verified anywhere
in the artifact, the declaring sections have no back-reference to their consumers, and the Belief-Ref
chains terminate at PBI entries without grounding those entries in the signal evidence that falsified them.

R16 tests three new structural layers:

- **Axis A (Citation-Completeness Manifest)**: After the artifact is written (Step 7), produce a
  CITATION-COMPLETENESS-MANIFEST -- a table that enumerates every citation point in the artifact
  (all F-BCR headers, all Registry-Ref values, all Belief-Ref cells), with type, source location,
  target address, and resolution status (RESOLVED / DANGLING). Citation-completeness becomes a
  single-table audit rather than a full-document scan. If this produces an observable structural
  property distinct from citations being present (C-49/50/51), it becomes C-52 candidate:
  CITATION-COMPLETENESS-MANIFEST-EXHAUSTIVE.

- **Axis B (Declaring-Section Consumer Index)**: The BC-COVERAGE-RECORD Schema, Phase Transition
  Registry, and STILL-LIVE FILTER tables each gain a final `Consumer-Ref` column listing every
  section that cites each declaration by address ID. The declaring section becomes bidirectionally
  navigable -- from declaring to consuming, not only from consuming to declaring. A reviewer reading
  the schema table immediately sees which output sections cite each F-ID, without scanning the
  artifact for output headers. If this creates an observable property distinct from citations being
  present, it becomes C-53 candidate: DECLARING-SECTION-CONSUMER-INDEX-POPULATED.

- **Axis C (PBI-Grounded Citation Chain)**: Each Belief-Ref entry in the STILL-LIVE FILTER extends
  from "PB-[NN]" to "PB-[NN] (confirmed false by: [artifact name, namespace, date])". The citation
  chain terminates at evidence: MUST-clause -> PBI entry -> confirming signal artifact. F-BCR-4
  output cells name the specific PBI entries constituting the coverage basis. A reviewer can walk
  the chain from enforcement to epistemic grounding to evidence from table cells alone. If this
  creates a new structural property, it becomes C-54 candidate: CITATION-CHAIN-PBI-GROUNDING-VERIFIED.

R15 implementations and R16 depth tests:

- **C-49 -> Axis A + Axis B**: R15 placed F-BCR field-IDs in output headers. R16 Axis A verifies
  all four F-BCR IDs appear in the manifest as RESOLVED. R16 Axis B adds Consumer-Ref to the
  BC-COVERAGE-RECORD Schema: each F-ID row names its consuming step. C-49 preserved; additive.

- **C-50 -> Axis A + Axis B**: R15 added Registry-Ref rows to PHASE-HANDOVER tables. R16 Axis A
  verifies all seven T-IDs appear in the manifest as RESOLVED. R16 Axis B adds Consumer-Ref to
  the Phase Transition Registry: each T-ID row names its consuming PHASE-HANDOVER table. C-50
  preserved; additive.

- **C-51 -> Axis A + Axis C**: R15 added Belief-Ref column to STILL-LIVE FILTER. R16 Axis A
  verifies all MUST-clause Belief-Refs appear in the manifest as RESOLVED. R16 Axis C extends
  each Belief-Ref cell to name the signal artifact that confirmed the PBI entry false. C-51
  preserved; additive.

**R16 progression layer:** R15 demonstrated that citation-activation creates rubric-scorable
structural properties. R16 tests whether citation-completeness verification (Axis A), bidirectional
navigability (Axis B), and PBI-grounded chain depth (Axis C) create a new structural property class.
V-05 (all three combined) demonstrates the full citation-complete artifact in a single runnable prompt.

**Predicted scoring under v16 (all 5 variations inherit R15 V-05's full structure):**

| Variation | C-49 | C-50 | C-51 | v16 | v17 (projected) | delta |
|-----------|:----:|:----:|:----:|:---:|:---------------:|:-----:|
| V-01 (Axis A) | PASS | PASS | PASS | 305 | 310 | +5 |
| V-02 (Axis B) | PASS | PASS | PASS | 305 | 310 | +5 |
| V-03 (Axis C) | PASS | PASS | PASS | 305 | 310 | +5 |
| V-04 (A+B) | PASS | PASS | PASS | 305 | 315 | +10 |
| **V-05 (A+B+C)** | PASS | PASS | PASS | 305 | **320** | +15 |

**C-52 scoring basis (V-01, V-04, V-05 -- Axis A):** Variations adding Axis A produce a
CITATION-COMPLETENESS-MANIFEST table at Step 8. The manifest has a row for every citation point --
all four F-BCR header citations (TYPE-A), all seven Registry-Ref rows (TYPE-B), all MUST Belief-Ref
column entries (TYPE-C) -- each with Citation-ID, Citation Type, Source Location, Target Address,
and Status. A reviewer auditing citation-completeness reads the manifest table alone; no document
traversal required. V-02 and V-03 carry no Axis A implementation; V-04 and V-05 include the
identical manifest.

**C-53 scoring basis (V-02, V-04, V-05 -- Axis B):** Variations adding Axis B add a Consumer-Ref
column to the BC-COVERAGE-RECORD Schema, Phase Transition Registry, and STILL-LIVE FILTER. Each
Consumer-Ref cell names the section(s) where the address is cited. A reviewer reading a schema
field declaration can immediately locate all consuming contexts from the declaring table row --
without scanning the artifact. V-01 and V-03 carry no Axis B implementation; V-04 and V-05
include the identical Consumer-Ref columns.

**C-54 scoring basis (V-03, V-05 -- Axis C):** Variations adding Axis C extend each MUST Belief-Ref
cell from "PB-[NN]" to "PB-[NN] (confirmed false by: [artifact name, namespace, date])". The chain
terminates at evidence: a reviewer reading MUST-3 walks to PB-03 (Belief-Ref) then to the signal
artifact -- from the MUST table cell alone. V-01 uses standard Belief-Ref cells; V-02 uses the same;
V-04 (A+B only) carries no Axis C implementation.

---

## V-01 -- Axis A: Citation-Completeness Manifest

**Variation axis:** Lifecycle emphasis -- after artifact write, produce a
CITATION-COMPLETENESS-MANIFEST enumerating every citation point and confirming each resolves
against its declared address (Axis A only)

**Hypothesis:** C-49/50/51 make addresses citation-active at their consuming contexts. The
citations exist and are present. But no single location confirms that *all* citations are present --
a reviewer verifying completeness must scan the full document. R16 Axis A asks whether adding an
explicit CITATION-COMPLETENESS-MANIFEST table creates a new structural property: citation-
completeness is auditable from one table, not a full-document scan. If this produces an observable
property distinct from citations being present (C-49/50/51), it becomes C-52 candidate:
CITATION-COMPLETENESS-MANIFEST-EXHAUSTIVE.

**Expected v16 score:** 305 (C-01 through C-51: all PASS -- inherits full R15 V-05 structure)
**Projected v17 excellence signal:** Post-artifact citation manifest; candidate criterion: artifact
carries a CITATION-COMPLETENESS-MANIFEST table enumerating all citation points with
RESOLVED/DANGLING status, auditable without document traversal.

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
              the CITATION-COMPLETENESS-MANIFEST.
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

### Step 8 -- [IA] Citation-Completeness Manifest [AXIS A]

After the artifact is written at Step 7, produce a CITATION-COMPLETENESS-MANIFEST. This
manifest is an explicit post-artifact audit of every citation point, confirming all citations
resolve against their declared addresses. A reviewer auditing citation-completeness reads this
table alone -- no document traversal required.

```
CITATION-COMPLETENESS-MANIFEST PROTOCOL
----------------------------------------------------------------------
Purpose:  Post-artifact citation audit. Every citation point that
          exists in this artifact must appear in the manifest.
Scope:    Three citation types:
          TYPE-A: F-BCR field-ID citations (output headers -> schema)
          TYPE-B: T-ID registry citations (Registry-Ref rows -> registry)
          TYPE-C: Belief-Ref citations (MUST-clause column -> PBI)
Status:   RESOLVED -- target address exists and is locatable by ID
          DANGLING -- target address absent or non-locatable
Gate:     Any DANGLING citation is a manifest failure. Report before
          finalizing; do not suppress DANGLING entries.
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

`MANIFEST-COMPLETE: [N] citations -- [N] TYPE-A, [N] TYPE-B, [N] TYPE-C -- all RESOLVED.`

== ARTIFACT STRUCTURE ============================================================

  1. ENFORCEMENT MECHANISM DECLARATION (EF; NO-ECHO COST)
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
  23. CITATION-COMPLETENESS-MANIFEST (Step 8; MANIFEST-COMPLETE token)

Write to: simulations/topic/echo/{topic}-echo-{YYYY-MM-DD}.md

---

## V-02 -- Axis B: Declaring-Section Consumer Index

**Variation axis:** Output format -- the BC-COVERAGE-RECORD Schema, Phase Transition Registry,
and STILL-LIVE FILTER tables each gain a final `Consumer-Ref` column listing every section
that cites each address by ID (Axis B only)

**Hypothesis:** C-49 activates the BC-COVERAGE-RECORD Schema from output headers; C-50 activates
the Phase Transition Registry from Registry-Ref rows; C-51 activates MUST-clauses from Belief-Ref
cells. Each activation is from consuming context to declaring context: a reviewer follows citations
forward. R16 Axis B asks whether the reverse direction -- from declaring context to consuming
context -- creates an independent structural property. A reviewer reading the schema declaration
for F-BCR-2 immediately sees which step's output cites it, without scanning for output headers.
If this creates an observable property distinct from citations being present, it becomes C-53
candidate: DECLARING-SECTION-CONSUMER-INDEX-POPULATED.

**Expected v16 score:** 305 (C-01 through C-51: all PASS -- inherits full R15 V-05 structure)
**Projected v17 excellence signal:** Consumer-Ref columns in declaring tables; candidate criterion:
BC-COVERAGE-RECORD Schema, Phase Transition Registry, and STILL-LIVE FILTER each carry a
Consumer-Ref column naming every consuming section, enabling bidirectional navigation from
declaring table row without document traversal.

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
              (F-BCR field-IDs in headers) + PHASE-HANDOVER-1 table
              before Step 2 begins.
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
Each T-ID row carries a Consumer-Ref column naming the inline PHASE-HANDOVER table that
cites it -- the registry is bidirectionally navigable from each declaration row.

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

Executed by BC during Step 1 in three sequential sub-phases. Write each gate token before
advancing. Do not merge sub-phases. Expressed entirely as markdown tables; no code fences.

| Sub-phase | Scope | Gate Token |
|-----------|-------|------------|
| [SCAN] | Read design materials. List all belief candidates. No pruning or evaluation. | `COMMIT-SCAN: [N] candidates identified.` |
| [FREEZE] | Produce PBI from scan results. Lock all PB-[NN] entries. No additions after gate token. | `COMMIT-FREEZE: PBI frozen at [N] entries.` |
| [COVERAGE AUDIT] | Audit domain coverage. Produce BC-COVERAGE-RECORD using schema below. BC exclusion takes effect after this record is written. | BC-COVERAGE-RECORD (schema below). |

#### BC-COVERAGE-RECORD Schema

Each field carries a named field-ID (F-BCR-1 through F-BCR-4). When producing the
BC-COVERAGE-RECORD output, prefix each field header with its schema ID. Each F-ID row
carries a Consumer-Ref column naming the output step where the field is cited -- the
schema is bidirectionally navigable from each field declaration row.

| F-ID | Field | Content | Constraint | Consumer-Ref |
|------|-------|---------|------------|--------------|
| F-BCR-1 | Sub-phase | [COVERAGE AUDIT] -- gate declared in BC-STEP1-PROTOCOL. | Fixed; do not substitute. | Consumed-By: [COVERAGE AUDIT] output header in Step 1; PHASE-HANDOVER-1 Output Produced field |
| F-BCR-2 | Materials consulted | [List each design document scanned during [SCAN] and [FREEZE]. Minimum one entry.] | Pre-investigation only. Signal artifacts excluded. | Consumed-By: [COVERAGE AUDIT] output header in Step 1 |
| F-BCR-3 | Signal artifacts excluded | [List each signal artifact by name; confirm not accessed during Step 1.] | Enumerated by name. "none" not acceptable if signals exist. | Consumed-By: [COVERAGE AUDIT] output header in Step 1 |
| F-BCR-4 | PBI completeness basis | [One sentence: which material(s) provide the primary PBI basis.] | Single sentence. Reviewable from this field alone. | Consumed-By: [COVERAGE AUDIT] output header in Step 1 |

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
| Exclusion In Effect | EF excluded from Steps 1-7; signal artifacts not accessed at Step 0 |
| Receiving Role | Belief Cartographer (BC) -- Step 1 |
| Registry-Ref | T-00 |

---

### Step 1 -- [BC] Belief Inventory and Coverage Audit

Execute BC-STEP1-PROTOCOL as declared above. Write each gate token before advancing.

**[SCAN]** `COMMIT-SCAN: [N] candidates identified.`

**[FREEZE]**

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

**[COVERAGE AUDIT]** Produce BC-COVERAGE-RECORD with schema field-IDs in each header
(F-BCR-1 / F-BCR-2 / F-BCR-3 / F-BCR-4). No code fence.

BC is now excluded from Steps 2-7.

**PHASE-HANDOVER-1** (registry entry: T-01):

| Field | Content |
|-------|---------|
| Completing Role | Belief Cartographer (BC) -- Step 1 |
| Step Completed | Step 1 -- Belief Inventory and Coverage Audit |
| Output Produced | PBI (all PB-[NN] frozen) + BC-COVERAGE-RECORD (F-BCR field-IDs in headers) |
| Exclusion In Effect | BC excluded from Steps 2-7; PBI frozen; no additions after this table |
| Receiving Role | Institutional Archaeologist (IA) -- Step 2 |
| Registry-Ref | T-01 |

---

### Steps 2-7

_(Steps 2-6 identical to V-01 above; Steps 0-6 PHASE-HANDOVER tables each carry Registry-Ref
rows with T-ID citation as shown in V-01. Step 7 Hierarchy, Distillation, and Forward Handover
section identical to V-01. No Step 8 -- Axis A not present in V-02.)_

**STILL-LIVE FILTER** -- Each MUST-clause carries a Belief-Ref column (C-51 preserved) AND a
Consumer-Ref column naming the enforcement site where each clause is applied (Axis B extension
of C-51). The STILL-LIVE FILTER table is bidirectionally navigable: from declaring clause to
consuming token, not only from consuming token to declaring clause.

| MUST-ID | Scope | Action | Constraint | Belief-Ref | Consumer-Ref |
|---------|-------|--------|------------|------------|--------------|
| MUST-1 | EVERY CANDIDATE -- no exceptions | Produce exactly one of: `STILL-LIVE-[N]: [name]` OR `DISCARD-[N]: [name]` | No candidate evaluation concludes without one of these tokens. | PB-[NN] -- belief tested for survival | Consumed-By: per-candidate evaluation in Step 3 |
| MUST-2 | EVERY DISCARD-[N] TOKEN -- no exceptions | Immediately write: `DISCARD-[N]-PBI-REF: PB-[NN]` | A DISCARD token without a PBI-Ref token is malformed. | PB-[NN] -- belief whose falsification makes routing necessary | Consumed-By: DISCARD-[N]-PBI-REF token in Step 3 |
| MUST-3 | EVERY DISCARD-[N] TOKEN -- no exceptions | Immediately write: `DISCARD-[N]-ROUTE: [destination]` | A DISCARD token without a ROUTE token is malformed. | PB-[NN] -- belief whose failure category determines routing | Consumed-By: DISCARD-[N]-ROUTE token in Step 3 |
| MUST-4 | EVERY DISCARD-[N] TOKEN -- no exceptions | Immediately write: `DISCARD-[N]-REASON: [one sentence]` | A DISCARD token without a REASON token is malformed. | PB-[NN] -- belief whose survival condition this REASON states | Consumed-By: DISCARD-[N]-REASON token in Step 3 |

== ARTIFACT STRUCTURE ============================================================

  (Same as V-01 items 1-22; no item 23 -- Axis A manifest not present)

Write to: simulations/topic/echo/{topic}-echo-{YYYY-MM-DD}.md

---

## V-03 -- Axis C: PBI-Grounded Citation Chain

**Variation axis:** Lifecycle emphasis -- each Belief-Ref cell extends from "PB-[NN]" to
"PB-[NN] (confirmed false by: [artifact name, namespace, date])"; F-BCR-4 output names specific
PBI entries constituting the coverage basis (Axis C only)

**Hypothesis:** C-51 links each MUST-clause to its PBI anchor via a Belief-Ref cell. This is a
one-step citation: MUST-clause -> PBI entry. The chain is navigable but terminates at the PBI
declaration, not at the evidence that confirmed the belief false. R16 Axis C asks whether
extending the chain one level deeper -- each Belief-Ref names the signal artifact that confirmed
the PBI entry false -- creates a distinct structural property: the chain terminates at evidence,
not at assertion. A reviewer reading MUST-3 walks to PB-03, then to the signal that confirmed
PB-03 false -- from the MUST table cell alone, without consulting prose in any section. If this
creates a new observable structural property, it becomes C-54 candidate:
CITATION-CHAIN-PBI-GROUNDING-VERIFIED.

**Expected v16 score:** 305 (C-01 through C-51: all PASS -- inherits full R15 V-05 structure)
**Projected v17 excellence signal:** PBI-grounded Belief-Ref cells; candidate criterion: each
MUST-clause Belief-Ref cell names both the PBI entry and the signal artifact that confirmed it
false, grounding the enforcement chain in evidence from the cell alone.

---

Topic: `{topic}`

Synthesize what was unexpected. Three roles at three exclusive phase boundaries. Every structural
commitment is named, formal, and auditable from output. This is not a summary. This is not a list
of findings. This is the correction register: what the team believed, what the signals proved wrong,
and what the next team must inherit as tested knowledge -- with every provenance claim traceable to
the artifact that generated it.

---

### Roles

_(Role declarations identical to V-01: EF Step 0 exclusively, BC Step 1 exclusively, IA Steps 2-7.)_

**Phase Handover Schema:** Six rows including Registry-Ref row (C-50 preserved, identical to V-01).

**Phase Transition Registry:** T-ID column present (C-50 preserved, identical to V-01). No
Consumer-Ref column -- Axis B not present in V-03.

**BC-STEP1-PROTOCOL:** Three sub-phases identical to V-01.

**BC-COVERAGE-RECORD Schema:** F-ID column present (C-49 preserved, identical to V-01). No
Consumer-Ref column -- Axis B not present in V-03.

F-BCR-4 Axis C extension: when producing the BC-COVERAGE-RECORD output, the F-BCR-4 field
(PBI completeness basis) must explicitly name the PB-[NN] entries constituting the coverage
basis. Format: "F-BCR-4: PBI completeness basis -- PB-01 through PB-[N] (from [material name])."
This grounds the coverage claim in specific PBI entries: a reviewer can confirm the coverage
assertion by reading named entries rather than accepting a summary sentence.

---

### Steps 0-6

_(Identical to V-01 -- all PHASE-HANDOVER tables carry Registry-Ref rows with T-ID citation.)_

---

### Step 3 Extension -- STILL-LIVE FILTER with PBI-Grounded Belief-Ref [AXIS C]

**STILL-LIVE FILTER -- TABLE-COLUMN MUST-CLAUSE PROTOCOL**

Each MUST-clause carries a stable MUST-ID (C-48 preserved) and a Belief-Ref column (C-51
preserved). The Belief-Ref cell extends the citation chain one level deeper: it names the PBI
entry AND the signal artifact that confirmed that belief false. Format for each Belief-Ref cell:
"PB-[NN] (confirmed false by: [artifact name, namespace, date])". The chain terminates at
evidence: a reviewer reading any MUST-clause can walk to its PBI entry and then to the signal
that confirmed that belief false -- from the table cell alone, without consulting prose in any
section.

| MUST-ID | Scope | Action | Constraint | Belief-Ref |
|---------|-------|--------|------------|------------|
| MUST-1 | EVERY CANDIDATE -- no exceptions | Produce exactly one of: `STILL-LIVE-[N]: [name]` OR `DISCARD-[N]: [name]` | No candidate evaluation concludes without one of these tokens. | PB-[NN] (confirmed false by: [artifact name, namespace, date]) |
| MUST-2 | EVERY DISCARD-[N] TOKEN -- no exceptions | Immediately write: `DISCARD-[N]-PBI-REF: PB-[NN]` | A DISCARD token without a PBI-Ref token is malformed. | PB-[NN] (confirmed false by: [artifact name, namespace, date]) |
| MUST-3 | EVERY DISCARD-[N] TOKEN -- no exceptions | Immediately write: `DISCARD-[N]-ROUTE: [destination]` | A DISCARD token without a ROUTE token is malformed. | PB-[NN] (confirmed false by: [artifact name, namespace, date]) |
| MUST-4 | EVERY DISCARD-[N] TOKEN -- no exceptions | Immediately write: `DISCARD-[N]-REASON: [one sentence]` | A DISCARD token without a REASON token is malformed. | PB-[NN] (confirmed false by: [artifact name, namespace, date]) |

Belief-Ref format rule: each cell must contain both the PBI identifier (PB-[NN]) and the
confirming signal artifact in parentheses. A Belief-Ref cell containing only "PB-[NN]"
without the confirming artifact is incomplete and must be revised before Step 4 begins.

Completeness gate: `DISCARD-LOG-COMPLETE: [N] STILL-LIVE, [M] DISCARD -- all four MUST-clauses applied to every candidate; no candidate unresolved.`

---

### Step 7

_(Identical to V-01.)_

== ARTIFACT STRUCTURE ============================================================

  (Same as V-01 items 1-22; no item 23 -- Axis A manifest not present)
  Note: BC-COVERAGE-RECORD F-BCR-4 field names specific PBI entries (Axis C extension).
  Note: STILL-LIVE FILTER Belief-Ref cells include confirming artifact reference (Axis C).

Write to: simulations/topic/echo/{topic}-echo-{YYYY-MM-DD}.md

---

## V-04 -- Axes A+B: Citation-Completeness Manifest + Consumer Index

**Variation axis:** Lifecycle emphasis + output format -- adds Axis A (CITATION-COMPLETENESS-
MANIFEST at Step 8) and Axis B (Consumer-Ref column in declaring tables) together; no Axis C

**Hypothesis:** V-01 demonstrated that a post-artifact citation manifest creates a single-table
audit location. V-02 demonstrated that Consumer-Ref columns in declaring tables create
bidirectional navigability. V-04 asks whether both properties together create a structural
reinforcement: the manifest confirms citation-completeness exhaustively (Axis A), and the
declaring tables pre-populate the expected citation set that the manifest verifies (Axis B).
The Consumer-Ref column in the Phase Transition Registry declares that T-02 is consumed by
PHASE-HANDOVER-2's Registry-Ref row; the manifest confirms CIT-07 (TYPE-B) is RESOLVED. The
two structures corroborate each other without redundancy -- declaration announces, manifest verifies.

**Expected v16 score:** 305 (C-01 through C-51: all PASS -- inherits full R15 V-05 structure)
**Projected v17 excellence signal:** Axes A+B together; candidate criteria: CITATION-COMPLETENESS-
MANIFEST-EXHAUSTIVE (C-52) + DECLARING-SECTION-CONSUMER-INDEX-POPULATED (C-53).

---

Topic: `{topic}`

Synthesize what was unexpected. Three roles at three exclusive phase boundaries. Every structural
commitment is named, formal, and auditable from output. This is not a summary. This is not a list
of findings. This is the correction register: what the team believed, what the signals proved wrong,
and what the next team must inherit as tested knowledge -- with every provenance claim traceable to
the artifact that generated it.

---

### Roles

_(EF, BC, IA function declarations identical to V-01.)_

**Phase Handover Schema:** Six rows including Registry-Ref row (C-50 preserved, identical to V-01).

**Phase Transition Registry** -- with T-ID column (C-50) and Consumer-Ref column (Axis B):

| T-ID | Transition | Step Completed | Completing Role | Receiving Role | Consumer-Ref |
|------|------------|----------------|-----------------|----------------|--------------|
| T-00 | PHASE-HANDOVER-0 | Step 0 -- Enforcement Section and Invocation Record | Enforcement Framer (EF) | Belief Cartographer (BC) | Consumed-By: PHASE-HANDOVER-0 Registry-Ref row |
| T-01 | PHASE-HANDOVER-1 | Step 1 -- Belief Inventory and Coverage Audit | Belief Cartographer (BC) | Institutional Archaeologist (IA) | Consumed-By: PHASE-HANDOVER-1 Registry-Ref row |
| T-02 | PHASE-HANDOVER-2 | Step 2 -- Handle Ledger | Institutional Archaeologist (IA) | Institutional Archaeologist (IA) | Consumed-By: PHASE-HANDOVER-2 Registry-Ref row |
| T-03 | PHASE-HANDOVER-3 | Step 3 -- Draft All Corrections | Institutional Archaeologist (IA) | Institutional Archaeologist (IA) | Consumed-By: PHASE-HANDOVER-3 Registry-Ref row |
| T-04 | PHASE-HANDOVER-4 | Step 4 -- Register Audit | Institutional Archaeologist (IA) | Institutional Archaeologist (IA) | Consumed-By: PHASE-HANDOVER-4 Registry-Ref row |
| T-05 | PHASE-HANDOVER-5 | Step 5 -- Entry Gate | Institutional Archaeologist (IA) | Institutional Archaeologist (IA) | Consumed-By: PHASE-HANDOVER-5 Registry-Ref row |
| T-06 | PHASE-HANDOVER-6 | Step 6 -- Chain Integrity Audit | Institutional Archaeologist (IA) | Institutional Archaeologist (IA) | Consumed-By: PHASE-HANDOVER-6 Registry-Ref row |

**BC-STEP1-PROTOCOL:** Identical to V-01.

**BC-COVERAGE-RECORD Schema** -- with F-ID column (C-49) and Consumer-Ref column (Axis B):

| F-ID | Field | Content | Constraint | Consumer-Ref |
|------|-------|---------|------------|--------------|
| F-BCR-1 | Sub-phase | [COVERAGE AUDIT] -- gate declared in BC-STEP1-PROTOCOL. | Fixed; do not substitute. | Consumed-By: [COVERAGE AUDIT] output header (Step 1); PHASE-HANDOVER-1 Output Produced |
| F-BCR-2 | Materials consulted | [List each design document scanned during [SCAN] and [FREEZE]. Minimum one entry.] | Pre-investigation only. Signal artifacts excluded. | Consumed-By: [COVERAGE AUDIT] output header (Step 1) |
| F-BCR-3 | Signal artifacts excluded | [List each signal artifact by name; confirm not accessed during Step 1.] | Enumerated by name. "none" not acceptable if signals exist. | Consumed-By: [COVERAGE AUDIT] output header (Step 1) |
| F-BCR-4 | PBI completeness basis | [One sentence: which material(s) provide the primary PBI basis.] | Single sentence. Reviewable from this field alone. | Consumed-By: [COVERAGE AUDIT] output header (Step 1) |

---

### Steps 0-6

_(All PHASE-HANDOVER tables carry 6-row schema with Registry-Ref rows; T-ID citations match
the Phase Transition Registry. Identical to V-01 for Steps 0-6.)_

**STILL-LIVE FILTER** -- Each MUST-clause carries a Belief-Ref column (C-51) AND a Consumer-Ref
column (Axis B) identical to V-02. No Axis C extension -- Belief-Ref cells contain "PB-[NN]"
without confirming artifact reference.

---

### Step 7

_(Identical to V-01.)_

---

### Step 8 -- [IA] Citation-Completeness Manifest [AXIS A]

_(Identical to V-01 Step 8 -- CITATION-COMPLETENESS-MANIFEST table with all TYPE-A, TYPE-B,
and TYPE-C citations enumerated; MANIFEST-COMPLETE token required.)_

== ARTIFACT STRUCTURE ============================================================

  1-22: Same as V-01
  23. CITATION-COMPLETENESS-MANIFEST (Step 8; MANIFEST-COMPLETE token)
  Note: Phase Transition Registry carries Consumer-Ref column (Axis B).
  Note: BC-COVERAGE-RECORD Schema carries Consumer-Ref column (Axis B).
  Note: STILL-LIVE FILTER carries Consumer-Ref column (Axis B); no Axis C.

Write to: simulations/topic/echo/{topic}-echo-{YYYY-MM-DD}.md

---

## V-05 -- Axes A+B+C: Full R16 Citation Architecture

**Variation axis:** Full integration -- Axis A (Citation-Completeness Manifest) + Axis B
(Consumer-Ref columns in declaring tables) + Axis C (PBI-Grounded Citation Chain) combined

**Hypothesis:** V-01 tested whether a post-artifact manifest makes citation-completeness
auditable from one table. V-02 tested whether Consumer-Ref columns make declaring sections
bidirectionally navigable. V-03 tested whether PBI-grounded Belief-Ref cells terminate the
enforcement chain at evidence. V-05 asks whether all three together create a fully closed
citation architecture: every citation is manifest-verified (Axis A), every declaring section
knows its consumers (Axis B), and every enforcement-to-belief chain terminates at the signal
that confirmed the belief false (Axis C). The architecture is closed when: a reviewer can
enter at any point -- consuming output, declaring table, or enforcement clause -- and traverse
the full citation topology from that entry point alone, without consulting prose in any section.

**Expected v16 score:** 305 (C-01 through C-51: all PASS -- inherits full R15 V-05 structure)
**Projected v17 excellence signal:** Full citation architecture; all three axes active together;
candidate criteria: C-52 (manifest), C-53 (consumer index), C-54 (PBI-grounded chain).

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
              the CITATION-COMPLETENESS-MANIFEST.
Input:        Signal artifacts + frozen PBI (read-only).
Out-of-scope: PBI authorship (frozen). Enforcement section (immutable).
Orienting:    "What would the next team build wrong?"
Phase scope:  Steps 2-8 only.
----------------------------------------------------------------------
```

**Phase Handover Schema (universal -- all 7 exits, Steps 0-6):**

All PHASE-HANDOVER-[N] tables use this schema exactly. Six rows. Fixed field names.
Do not substitute prose. Do not add or remove rows.

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
Each T-ID row carries a Consumer-Ref column (Axis B) naming the consuming PHASE-HANDOVER table.
Universality verifiable by cross-referencing T-IDs against Registry-Ref values -- no traversal.

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

Executed by BC during Step 1 in three sequential sub-phases. Write each gate token before
advancing. Do not merge sub-phases. Expressed entirely as markdown tables; no code fences.

| Sub-phase | Scope | Gate Token |
|-----------|-------|------------|
| [SCAN] | Read design materials. List all belief candidates. No pruning or evaluation. | `COMMIT-SCAN: [N] candidates identified.` |
| [FREEZE] | Produce PBI from scan results. Lock all PB-[NN] entries. No additions after gate token. | `COMMIT-FREEZE: PBI frozen at [N] entries.` |
| [COVERAGE AUDIT] | Audit domain coverage. Produce BC-COVERAGE-RECORD using schema below. BC exclusion takes effect after this record is written. | BC-COVERAGE-RECORD (schema below). |

#### BC-COVERAGE-RECORD Schema

Each field carries a named field-ID (F-BCR-1 through F-BCR-4). When producing the
BC-COVERAGE-RECORD output, prefix each field header with its schema ID. Each F-ID row
carries a Consumer-Ref column (Axis B) naming the output step where the field is cited.
F-BCR-4 Axis C extension: the output cell for F-BCR-4 explicitly names the PB-[NN] entries
constituting the coverage basis -- "PB-01 through PB-[N] (from [material name])" -- grounding
the coverage claim in specific PBI entries rather than a summary sentence.

| F-ID | Field | Content | Constraint | Consumer-Ref |
|------|-------|---------|------------|--------------|
| F-BCR-1 | Sub-phase | [COVERAGE AUDIT] -- gate declared in BC-STEP1-PROTOCOL. | Fixed; do not substitute. | Consumed-By: [COVERAGE AUDIT] output header (Step 1); PHASE-HANDOVER-1 Output Produced |
| F-BCR-2 | Materials consulted | [List each design document scanned during [SCAN] and [FREEZE]. Minimum one entry.] | Pre-investigation only. Signal artifacts excluded. | Consumed-By: [COVERAGE AUDIT] output header (Step 1) |
| F-BCR-3 | Signal artifacts excluded | [List each signal artifact by name; confirm not accessed during Step 1.] | Enumerated by name. "none" not acceptable if signals exist. | Consumed-By: [COVERAGE AUDIT] output header (Step 1) |
| F-BCR-4 | PBI completeness basis | [Output: name specific PB-[NN] entries -- "PB-01 through PB-[N] (from [material name])".] | Names PBI entries; not a summary sentence. Axis C extension. | Consumed-By: [COVERAGE AUDIT] output header (Step 1) |

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

**[SCAN]** `COMMIT-SCAN: [N] candidates identified.`

**[FREEZE]**

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

**[COVERAGE AUDIT]** Produce BC-COVERAGE-RECORD with schema field-IDs in each header. The
F-BCR-4 field output names specific PBI entries (Axis C): "F-BCR-4: PBI completeness basis --
PB-01 through PB-[N] (from [material name])." No code fence.

BC is now excluded from Steps 2-8.

**PHASE-HANDOVER-1** (registry entry: T-01):

| Field | Content |
|-------|---------|
| Completing Role | Belief Cartographer (BC) -- Step 1 |
| Step Completed | Step 1 -- Belief Inventory and Coverage Audit |
| Output Produced | PBI (all PB-[NN] frozen) + BC-COVERAGE-RECORD (F-BCR field-IDs in headers; F-BCR-4 names PBI entries) |
| Exclusion In Effect | BC excluded from Steps 2-8; PBI frozen; no additions after this table |
| Receiving Role | Institutional Archaeologist (IA) -- Step 2 |
| Registry-Ref | T-01 |

---

### Step 2 -- [IA] Handle Ledger

_(Identical to V-01.)_

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

_(CORRECTION RECORD SCHEMA identical to V-01.)_

**STILL-LIVE FILTER -- TABLE-COLUMN MUST-CLAUSE PROTOCOL [AXES B + C]**

Each MUST-clause carries: a stable MUST-ID (C-48), a Belief-Ref column with PBI-grounded
citation chain (C-51 + Axis C), and a Consumer-Ref column naming the enforcement site (Axis B).

Belief-Ref format rule (Axis C): each Belief-Ref cell must contain the PBI identifier and the
confirming signal artifact in parentheses: "PB-[NN] (confirmed false by: [artifact name,
namespace, date])". A Belief-Ref cell containing only "PB-[NN]" is incomplete and must be
revised before Step 4 begins.

| MUST-ID | Scope | Action | Constraint | Belief-Ref | Consumer-Ref |
|---------|-------|--------|------------|------------|--------------|
| MUST-1 | EVERY CANDIDATE -- no exceptions | Produce exactly one of: `STILL-LIVE-[N]: [name]` OR `DISCARD-[N]: [name]` | No candidate evaluation concludes without one of these tokens. | PB-[NN] (confirmed false by: [artifact, namespace, date]) | Consumed-By: per-candidate evaluation tokens in Step 3 |
| MUST-2 | EVERY DISCARD-[N] TOKEN -- no exceptions | Immediately write: `DISCARD-[N]-PBI-REF: PB-[NN]` | A DISCARD token without a PBI-Ref token is malformed. | PB-[NN] (confirmed false by: [artifact, namespace, date]) | Consumed-By: DISCARD-[N]-PBI-REF token in Step 3 |
| MUST-3 | EVERY DISCARD-[N] TOKEN -- no exceptions | Immediately write: `DISCARD-[N]-ROUTE: [destination]` | A DISCARD token without a ROUTE token is malformed. | PB-[NN] (confirmed false by: [artifact, namespace, date]) | Consumed-By: DISCARD-[N]-ROUTE token in Step 3 |
| MUST-4 | EVERY DISCARD-[N] TOKEN -- no exceptions | Immediately write: `DISCARD-[N]-REASON: [one sentence]` | A DISCARD token without a REASON token is malformed. | PB-[NN] (confirmed false by: [artifact, namespace, date]) | Consumed-By: DISCARD-[N]-REASON token in Step 3 |

Completeness gate: `DISCARD-LOG-COMPLETE: [N] STILL-LIVE, [M] DISCARD -- all four MUST-clauses applied to every candidate; no candidate unresolved.`

**PHASE-HANDOVER-3** (registry entry: T-03):

| Field | Content |
|-------|---------|
| Completing Role | Institutional Archaeologist (IA) -- Step 3 |
| Step Completed | Step 3 -- Draft All Corrections |
| Output Produced | Draft corrections + STILL-LIVE FILTER output (DISCARD-LOG-COMPLETE; Belief-Ref cells PBI-grounded) |
| Exclusion In Effect | No new entries or DISCARD tokens may be added after Step 4 begins |
| Receiving Role | Institutional Archaeologist (IA) -- Step 4 |
| Registry-Ref | T-03 |

---

### Steps 4-6

_(Register Audit, Entry Gate, Chain Integrity Audit -- identical to V-01. PHASE-HANDOVER-4
through PHASE-HANDOVER-6 each carry Registry-Ref rows matching T-04, T-05, T-06.)_

---

### Step 7 -- [IA] Hierarchy, Distillation, and Forward Handover

_(Identical to V-01.)_

---

### Step 8 -- [IA] Citation-Completeness Manifest [AXIS A]

After the artifact is written at Step 7, produce a CITATION-COMPLETENESS-MANIFEST. Every
citation point in the artifact -- all F-BCR header citations (TYPE-A), all Registry-Ref rows
(TYPE-B), all Belief-Ref cells with confirming artifact references (TYPE-C, Axis C extended) --
must appear in the manifest with resolution status.

```
CITATION-COMPLETENESS-MANIFEST PROTOCOL
----------------------------------------------------------------------
Purpose:  Post-artifact citation audit. Every citation point that
          exists in this artifact must appear in the manifest.
Scope:    Three citation types:
          TYPE-A: F-BCR field-ID citations (output headers -> schema)
          TYPE-B: T-ID registry citations (Registry-Ref rows -> registry)
          TYPE-C: Belief-Ref citations (MUST-clause column -> PBI +
                  confirming signal artifact [Axis C extension])
Status:   RESOLVED -- target address exists and is locatable by ID;
                     for TYPE-C, confirming artifact is named and
                     resolvable in this signal set
          DANGLING -- target address absent, non-locatable, or
                     TYPE-C confirming artifact not in signal set
Gate:     Any DANGLING citation is a manifest failure. Report before
          finalizing; do not suppress DANGLING entries.
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
| CIT-[N] | TYPE-C | STILL-LIVE FILTER MUST-[N] Belief-Ref cell | PBI row PB-[NN] + confirming signal artifact | RESOLVED / DANGLING |

`MANIFEST-COMPLETE: [N] citations -- [N] TYPE-A, [N] TYPE-B, [N] TYPE-C -- all RESOLVED.`

== ARTIFACT STRUCTURE ============================================================

  1. ENFORCEMENT MECHANISM DECLARATION (EF; NO-ECHO COST)
  2. EF-INVOCATION-RECORD (Step 0)
  3. PHASE-HANDOVER-0 table (6-row schema; Registry-Ref: T-00)
  4. PBI output (BC; COMMIT-SCAN + COMMIT-FREEZE tokens present)
  5. BC-COVERAGE-RECORD (F-BCR field-IDs in all headers; F-BCR-4 names PBI entries [Axis C]; no code fence)
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
  23. CITATION-COMPLETENESS-MANIFEST (Step 8; MANIFEST-COMPLETE token) [Axis A]
  Note: Phase Transition Registry carries Consumer-Ref column [Axis B]
  Note: BC-COVERAGE-RECORD Schema carries Consumer-Ref column [Axis B]
  Note: STILL-LIVE FILTER carries Consumer-Ref column [Axis B]
  Note: STILL-LIVE FILTER Belief-Ref cells name confirming signal artifact [Axis C]
  Note: F-BCR-4 output names specific PBI entries [Axis C]

Write to: simulations/topic/echo/{topic}-echo-{YYYY-MM-DD}.md
