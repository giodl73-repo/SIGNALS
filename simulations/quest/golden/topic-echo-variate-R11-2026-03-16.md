---
skill: quest-variate
skill_target: topic-echo
date: 2026-03-16
round: 11
rubric: v11
rubric_file: simulations/quest/rubrics/topic-echo-rubric-v11-2026-03-16.md
rubric_max: 230
---

# Variations: `topic:echo` -- Round 11 (2026-03-16)

**Rubric:** v11 (2026-03-16) | **Criteria count:** 36 (5 essential / 3 recommended / 28 aspirational)

---

## Design Context

R10 V-05 achieves 215/215 under v10 and 230/230 under v11. The three structural
patterns identified in R10 -- BC-COVERAGE-RECORD (C-34), PHASE-HANDOVER tokens
(C-35), and DISCARD LOG (C-36) -- are now formal rubric criteria. Round 11 does not
re-explore the R10 axes; it tests whether the same scoring profiles can be produced
through distinct **variation-axis implementations** drawn from the standard set.

The three R10 structural elements map cleanly to three variation axes:

- **C-34 (BC-COVERAGE-RECORD)** -> **Lifecycle emphasis**: BC's Step 1 is
  restructured into three explicit sub-phases ([SCAN] / [FREEZE] / [COVERAGE AUDIT]),
  making the coverage record a natural lifecycle milestone rather than an appended
  block. The implementation emphasis is on extending BC's phase boundary work rather
  than adding a parallel EF-INVOCATION-RECORD copy.
- **C-35 (PHASE-HANDOVER tokens)** -> **Output format**: Phase transition tokens use
  a table-based schema instead of code-block format. The handover structure becomes
  visually distinct from protocol declarations -- a different formatting register for
  transition events vs operational instructions.
- **C-36 (DISCARD LOG)** -> **Phrasing register**: STILL-LIVE FILTER documentation
  is written in pure imperative register -- unconditional second-person present
  commands. No conditional "if NO" framing. Every candidate evaluation produces a
  written record; the imperative form removes the optionality that conditional framing
  can imply.

**Three R11 axes:**

- **Axis A -- Lifecycle Emphasis**: BC's Step 1 receives three named sub-phases:
  [SCAN], [FREEZE], [COVERAGE AUDIT]. BC-COVERAGE-RECORD is the gate return for
  [COVERAGE AUDIT]. BC Function Declaration names all three sub-phases and confirms
  coverage record production before BC exclusion takes effect.
- **Axis B -- Output Format**: PHASE-HANDOVER-EF and PHASE-HANDOVER-BC are rendered
  as markdown tables with | Field | Value | structure rather than code blocks. Each
  row names one transition element (completing role, step, output, exclusion,
  receiving role). Function Declarations reference these tables as gate returns.
- **Axis C -- Phrasing Register**: STILL-LIVE FILTER is written in unconditional
  imperative form. For every candidate that fails the filter: "Write DISCARD-[N].
  Name the finding label. State the route. State one sentence reason." No conditional
  branching. After all candidates: "Write DISCARD-LOG-COMPLETE." Commands, not
  conditions.

**Variation plan:**

| Variation | Axis A | Axis B | Axis C | C-34 | C-35 | C-36 | v11 composite |
|-----------|:------:|:------:|:------:|:----:|:----:|:----:|:-------------:|
| V-01 | YES | -- | -- | PASS | FAIL | FAIL | 220 |
| V-02 | -- | YES | -- | FAIL | PASS | FAIL | 220 |
| V-03 | -- | -- | YES | FAIL | FAIL | PASS | 220 |
| V-04 | YES | YES | -- | PASS | PASS | FAIL | 225 |
| **V-05** | YES | YES | YES | PASS | PASS | PASS | **230** |

All five carry C-01 through C-33. V-05 alone reaches the ceiling.

**Round 11 progression layer:** R10 established the three auditability patterns.
R11 tests structural variation in implementation: lifecycle sub-phasing (A), format
register separation (B), and imperative grammar enforcement (C). If these three axis
implementations produce the same scoring profile as R10's structural additions, the
criteria are implementation-robust -- multiple prompt forms can reliably trigger them.

---

## V-01 -- Lifecycle Emphasis Axis

**Variation axis:** Lifecycle emphasis only -- BC's Step 1 structured as three
explicit sub-phases; BC-COVERAGE-RECORD is the [COVERAGE AUDIT] gate return (Axis A)

**Hypothesis:** R10 V-01 added BC-COVERAGE-RECORD as a parallel block appended after
PBI freeze -- structurally equivalent to EF-INVOCATION-RECORD but positioned at the
end of Step 1. This implementation works but positions the coverage record as an
addendum to PBI production rather than as an obligated lifecycle milestone with its
own phase gate. If BC's Step 1 is restructured into three sub-phases -- [SCAN],
[FREEZE], [COVERAGE AUDIT] -- with COVERAGE AUDIT as the final gate return before
BC exclusion, the coverage record becomes as architecturally prominent as PBI freeze
itself. The hypothesis: explicit sub-phase structure makes the BC coverage obligation
harder to omit than an appended block, because omitting it means failing to close a
named lifecycle phase rather than skipping an optional section.

**New structural element (Axis A):** BC Function Declaration names three sub-phases.
Step 1 has three explicit sub-phase headers: [SCAN], [FREEZE], [COVERAGE AUDIT].
BC-COVERAGE-RECORD is the gate return for [COVERAGE AUDIT] -- BC exclusion does not
take effect until this block is complete.

**Expected v11 score:** 220 (C-34 PASS; C-35 FAIL -- no handover tokens; C-36 FAIL
-- no discard log)

**Discriminant from R10 V-01:** Lifecycle sub-phase structure (three named phases
in BC's step) vs. appended block (BC-COVERAGE-RECORD positioned after freeze but
not inside a named phase). All R10 V-01 axes (EF-INVOCATION-RECORD, all C-33 content)
fully present.

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

**Belief Cartographer (BC)** -- Step 1 exclusively; three sub-phases.

```
BELIEF CARTOGRAPHER -- FUNCTION DECLARATION
----------------------------------------------------------------------
Function:     Pre-investigation belief recovery. Three sub-phases:
              [SCAN] Read design materials; identify belief candidates.
              [FREEZE] Produce PBI; freeze all PB-[NN] entries.
              [COVERAGE AUDIT] Produce BC-COVERAGE-RECORD; confirm
              coverage basis before BC exclusion takes effect.
Input:        Design materials only. Same exclusion as EF.
Out-of-scope: Signal artifacts. Handle Ledger. Entry authoring.
Phase scope:  Step 1 only. BC exclusion takes effect after [COVERAGE
              AUDIT] gate return is complete.
Gate return:  PBI (all PB-[NN] entries frozen) + BC-COVERAGE-RECORD
              (materials, exclusions, completeness basis) before Step 2.
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
   during Step 0. If none: "No signal artifacts present at Step 0."]
Cost derivation basis:
  [One sentence: which material above grounded the NO-ECHO COST claim.
   A reviewer can re-derive the cost from this material alone.]
----------------------------------------------------------------------
```

---

### Step 1 -- [BC] Belief Inventory and Coverage Audit

**[SCAN]** Read all design materials within BC's input scope. Signal artifacts are
out of scope for this sub-phase. Identify every belief candidate -- any claim,
assumption, or design premise that could be carried as prior knowledge into
investigation. Complete the full scan before moving to [FREEZE].

**[FREEZE]** Produce the PBI from the scanned materials.

```
PBI PRODUCTION PROTOCOL
----------------------------------------------------------------------
Input:    Design materials only. Signal artifacts excluded.
Format:   PB-[NN]: ["Today's materials imply that X." No signal knowledge.]
Freeze:   PBI frozen at end of [FREEZE] sub-phase. BC may not add new
          PB-[NN] entries after this point.
          PBI entries must not use handle labels (unavailable at Step 1).
----------------------------------------------------------------------
```

**[COVERAGE AUDIT]** After PBI freeze, produce the coverage record. BC exclusion
from Steps 2-7 does not take effect until this block is written.

```
BC-COVERAGE-RECORD
----------------------------------------------------------------------
Sub-phase:  [COVERAGE AUDIT] (final BC sub-phase before exclusion)
Materials consulted (pre-investigation only):
  [List each design document, spec, proposal, or other pre-investigation
   source scanned during [SCAN] and [FREEZE] sub-phases. File name or
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

BC is now excluded from Steps 2-7.

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
  3. PBI PRODUCTION PROTOCOL output (BC; [FREEZE] sub-phase)
  4. BC-COVERAGE-RECORD (Step 1 [COVERAGE AUDIT]; design materials scanned;
     signals excluded; completeness basis)
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

## V-02 -- Output Format Axis

**Variation axis:** Output format only -- phase handover tokens rendered as markdown
tables instead of code-block protocol declarations (Axis B)

**Hypothesis:** R10 V-02 added PHASE-HANDOVER-EF and PHASE-HANDOVER-BC as code-block
protocol declarations -- the same visual register as ENFORCEMENT MECHANISM DECLARATION
and EF-INVOCATION-RECORD. This formats transition events identically to operational
instructions, making it harder to visually distinguish "something is happening here"
from "here is how to operate." If phase handover tokens use a different output format
-- a markdown table with | Field | Value | rows -- they occupy a separate format
register from code-block declarations. The visual distinction signals that these are
event records (status of a transition) rather than operational protocols (instructions
for a role). The hypothesis: format-register separation makes the handover tokens more
legible as transition artifacts and less likely to be treated as optional prose sections.

**New structural element (Axis B):** PHASE-HANDOVER-EF is a markdown table at end of
Step 0. PHASE-HANDOVER-BC is a markdown table at end of Step 1. Each table has five
rows: Completing Role, Step Completed, Output Produced, Exclusion In Effect, Receiving
Role. EF and BC Function Declarations name these tables as gate returns.

**Expected v11 score:** 220 (C-34 FAIL -- no BC coverage record; C-35 PASS; C-36 FAIL
-- no discard log)

**Discriminant from R10 V-02:** Table-format handover tokens vs. code-block tokens.
Same fields, different format register. All R10 V-02 axes (EF-INVOCATION-RECORD,
all C-33 content) fully present. No BC-COVERAGE-RECORD.

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
              before any signal reading begins. At end of Step 0,
              complete the PHASE-HANDOVER-EF transition table before
              handing over to BC.
Input:        Design materials only. Signal artifacts out of scope.
              EF-INVOCATION-RECORD must name every pre-investigation
              source consulted and list all signal artifacts as excluded.
Out-of-scope: PBI production. Entry authoring. Chain verification.
Phase scope:  Step 0 only. EF excluded from Steps 1-7.
Gate return:  ENFORCEMENT MECHANISM + EF-INVOCATION-RECORD +
              PHASE-HANDOVER-EF table all complete before Step 1.
----------------------------------------------------------------------
```

**Belief Cartographer (BC)** -- Step 1 exclusively.

```
BELIEF CARTOGRAPHER -- FUNCTION DECLARATION
----------------------------------------------------------------------
Function:     Pre-investigation belief recovery. PBI production.
              At end of Step 1, after PBI freeze, complete the
              PHASE-HANDOVER-BC transition table before IA begins.
Input:        Design materials only. Same exclusion as EF.
Out-of-scope: Signal artifacts. Handle Ledger. Entry authoring.
Phase scope:  Step 1 only. PBI frozen at end of Step 1. BC excluded
              from Steps 2-7.
Gate return:  PBI (all PB-[NN] entries) + PHASE-HANDOVER-BC table
              complete before Step 2.
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
  [One sentence: which material above grounded the NO-ECHO COST claim.
   A reviewer can re-derive the cost from this material alone.]
----------------------------------------------------------------------
```

At end of Step 0, complete the transition record before proceeding to Step 1:

| Field | Value |
|-------|-------|
| **Completing Role** | ENFORCEMENT FRAMER (EF) |
| **Step Completed** | 0 |
| **Output Produced** | ENFORCEMENT MECHANISM DECLARATION + NO-ECHO COST + EF-INVOCATION-RECORD |
| **Exclusion In Effect** | EF excluded from Steps 1-7: no signal artifact access, no PBI authorship, no chain verification |
| **Receiving Role** | BELIEF CARTOGRAPHER (BC) -- Step 1 |

*Label this table: PHASE-HANDOVER-EF*

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

After PBI freeze, complete the transition record before proceeding to Step 2:

| Field | Value |
|-------|-------|
| **Completing Role** | BELIEF CARTOGRAPHER (BC) |
| **Step Completed** | 1 |
| **Output Produced** | PBI -- [N] entries: PB-01 through PB-[NN]. PBI is now frozen; no entries may be added or altered. |
| **Exclusion In Effect** | BC excluded from Steps 2-7: no signal artifact access, no HL authorship, no correction drafting. Exception: BC is VERIFIER for PBI-Ref mismatch repairs per RESOLUTION PROTOCOL. |
| **Receiving Role** | INSTITUTIONAL ARCHAEOLOGIST (IA) -- Steps 2-7 |

*Label this table: PHASE-HANDOVER-BC*

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
  3. PHASE-HANDOVER-EF table (5-row transition record; EF exit confirmed; BC receiving)
  4. PBI PRODUCTION PROTOCOL output (BC)
  5. PHASE-HANDOVER-BC table (5-row transition record; BC exit confirmed; PBI frozen;
     entry count; IA receiving)
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

## V-03 -- Phrasing Register Axis

**Variation axis:** Phrasing register only -- STILL-LIVE FILTER documentation uses
unconditional imperative commands; every candidate evaluation produces a written record
(Axis C)

**Hypothesis:** R10 V-03 added DISCARD LOG via a conditional branching structure: "YES
-> draft. NO -> write DISCARD entry." This is correct but uses conditional register --
the NO branch is a triggered outcome, not an unconditional requirement. An LLM reading
this could infer that if all candidates pass the filter, no DISCARD entries are needed
and DISCARD-LOG-COMPLETE might be omitted. If the STILL-LIVE FILTER is rewritten in
pure imperative register -- every candidate evaluation statement is an unconditional
command rather than a conditional branch -- the documentation requirement has no
optionality. The phrasing register carries the enforcement. The hypothesis: imperative
grammar reduces omission risk because the command form removes the conditional structure
that can imply an optional path.

**New structural element (Axis C):** STILL-LIVE FILTER is written in four-step
sequence: (1) apply test, (2) for qualifying candidates draft correction entry, (3)
for non-qualifying candidates write DISCARD-[N] entry, (4) after all candidates write
DISCARD-LOG-COMPLETE. The conditional "if/then" structure is replaced with sequential
imperative commands per candidate category.

**Expected v11 score:** 220 (C-34 FAIL -- no BC coverage record; C-35 FAIL -- no
handover tokens; C-36 PASS)

**Discriminant from R10 V-03:** Imperative register throughout STILL-LIVE FILTER vs.
conditional branching structure. Same token requirements (DISCARD-[N], DISCARD-LOG-
COMPLETE); different grammatical form. No BC-COVERAGE-RECORD, no PHASE-HANDOVER tokens.

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

**Institutional Archaeologist (IA)** -- Steps 2-7. Every STILL-LIVE FILTER evaluation
produces a written record. Every candidate that does not enter the correction register
produces a typed discard entry. The filter is fully documented from first candidate to
DISCARD-LOG-COMPLETE.

```
INSTITUTIONAL ARCHAEOLOGIST -- FUNCTION DECLARATION
----------------------------------------------------------------------
Function:     False-assumption recovery. Correction register only.
              Every STILL-LIVE FILTER evaluation produces a written
              record -- either a correction entry or a DISCARD-[N]
              entry. After all candidates, write DISCARD-LOG-COMPLETE.
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
  [One sentence: which material above grounded the NO-ECHO COST claim.
   A reviewer can re-derive the cost from this material alone.]
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

### Step 3 -- [IA] Draft All Corrections with Documented Filter

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

STILL-LIVE FILTER -- DOCUMENTED EVALUATION:

For each candidate identified in the signal sweep:

  1. Apply the test: "Would a new team carry this as a false assumption
     going into their next investigation?"

  2. For each candidate that qualifies: draft a correction entry per
     the schema above.

  3. For each candidate that does not qualify: write a DISCARD entry
     immediately -- before moving to the next candidate:

       DISCARD-[N]: [finding label -- HL-[NN] or 3-5 word description]
       Route:  topic-story
       Reason: [One sentence. Name the specific claim or component that
                makes this a confirmed finding rather than a false
                assumption. State why a new team would not carry this
                as wrong prior knowledge. "Not relevant" fails.]

  4. After all candidates are evaluated (every candidate either has
     a correction entry or a DISCARD-[N] entry): write the closure:

       DISCARD-LOG-COMPLETE
       ----------------------------------------------------------------
       Candidates considered:   [total count -- integer]
       Accepted (correction):   [count with correction entries]
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
  3. PBI PRODUCTION PROTOCOL output (BC)
  4. HANDLE LEDGER PROTOCOL output (IA)
  5. Corrections -- HIGH -> MEDIUM -> LOW (CORRECTION RECORD SCHEMA)
  6. DISCARD-[N] entries (one per non-qualifying candidate; inline with evaluation)
  7. DISCARD-LOG-COMPLETE (after all candidates evaluated; candidates / accepted /
     discarded counts)
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

## V-04 -- Lifecycle Emphasis + Output Format Axes

**Variation axis:** Axis A (BC three sub-phases + BC-COVERAGE-RECORD) + Axis B
(table-format phase handover tokens); Axis C absent

**Hypothesis:** V-01 and V-02 establish that Axis A and Axis B each independently
produce their target criteria. V-04 tests whether combining them -- BC's expanded
lifecycle sub-phases with table-format phase transition records -- creates interference
or whether the axes are genuinely compositional. The structural zones are distinct:
Axis A operates inside Step 1 (BC sub-phase structure); Axis B operates at step
boundaries (transition tables between Steps 0/1 and 1/2). These zones do not overlap.
The expected result is additive: C-34 satisfied by [COVERAGE AUDIT] gate, C-35 by
table-format PHASE-HANDOVER tokens, C-36 absent (no discard log).

**Expected v11 score:** 225 (C-34 PASS; C-35 PASS; C-36 FAIL)

**Discriminant from V-01 and V-02:** Adds table-format handover tokens (Axis B) to
V-01's lifecycle sub-phase structure (Axis A). DISCARD LOG absent; C-36 FAIL.

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
              before any signal reading begins. At end of Step 0,
              complete the PHASE-HANDOVER-EF transition table before
              handing over to BC.
Input:        Design materials only. Signal artifacts out of scope.
              EF-INVOCATION-RECORD must name every pre-investigation
              source consulted and list all signal artifacts as excluded.
Out-of-scope: PBI production. Entry authoring. Chain verification.
Phase scope:  Step 0 only. EF excluded from Steps 1-7.
Gate return:  ENFORCEMENT MECHANISM + EF-INVOCATION-RECORD +
              PHASE-HANDOVER-EF table all complete before Step 1.
----------------------------------------------------------------------
```

**Belief Cartographer (BC)** -- Step 1 exclusively; three sub-phases.

```
BELIEF CARTOGRAPHER -- FUNCTION DECLARATION
----------------------------------------------------------------------
Function:     Pre-investigation belief recovery. Three sub-phases:
              [SCAN] Read design materials; identify belief candidates.
              [FREEZE] Produce PBI; freeze all PB-[NN] entries.
              [COVERAGE AUDIT] Produce BC-COVERAGE-RECORD; confirm
              coverage basis. Complete PHASE-HANDOVER-BC table before
              BC exclusion takes effect.
Input:        Design materials only. Same exclusion as EF.
Out-of-scope: Signal artifacts. Handle Ledger. Entry authoring.
Phase scope:  Step 1 only. BC exclusion takes effect after [COVERAGE
              AUDIT] gate return and PHASE-HANDOVER-BC table are complete.
Gate return:  PBI (all PB-[NN] entries) + BC-COVERAGE-RECORD +
              PHASE-HANDOVER-BC table all complete before Step 2.
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
  [One sentence: which material above grounded the NO-ECHO COST claim.
   A reviewer can re-derive the cost from this material alone.]
----------------------------------------------------------------------
```

At end of Step 0, complete the transition record before proceeding to Step 1:

| Field | Value |
|-------|-------|
| **Completing Role** | ENFORCEMENT FRAMER (EF) |
| **Step Completed** | 0 |
| **Output Produced** | ENFORCEMENT MECHANISM DECLARATION + NO-ECHO COST + EF-INVOCATION-RECORD |
| **Exclusion In Effect** | EF excluded from Steps 1-7: no signal artifact access, no PBI authorship, no chain verification |
| **Receiving Role** | BELIEF CARTOGRAPHER (BC) -- Step 1 |

*Label this table: PHASE-HANDOVER-EF*

---

### Step 1 -- [BC] Belief Inventory, Coverage Audit, and Phase Handover

**[SCAN]** Read all design materials within BC's input scope. Signal artifacts are
out of scope. Identify every belief candidate -- any claim, assumption, or design
premise that could be carried as prior knowledge. Complete the full scan before [FREEZE].

**[FREEZE]** Produce the PBI from the scanned materials.

```
PBI PRODUCTION PROTOCOL
----------------------------------------------------------------------
Input:    Design materials only. Signal artifacts excluded.
Format:   PB-[NN]: ["Today's materials imply that X." No signal knowledge.]
Freeze:   PBI frozen at end of [FREEZE] sub-phase. No new PB-[NN]
          entries after this point.
          PBI entries must not use handle labels (unavailable at Step 1).
----------------------------------------------------------------------
```

**[COVERAGE AUDIT]** After PBI freeze, produce the coverage record. Complete both
BC-COVERAGE-RECORD and PHASE-HANDOVER-BC table before BC exclusion takes effect.

```
BC-COVERAGE-RECORD
----------------------------------------------------------------------
Sub-phase:  [COVERAGE AUDIT] (final BC sub-phase before exclusion)
Materials consulted (pre-investigation only):
  [List each design document, spec, proposal, or other pre-investigation
   source scanned during [SCAN] and [FREEZE] sub-phases. File name or
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

After completing BC-COVERAGE-RECORD, complete the transition record before Step 2:

| Field | Value |
|-------|-------|
| **Completing Role** | BELIEF CARTOGRAPHER (BC) |
| **Step Completed** | 1 |
| **Output Produced** | PBI -- [N] entries: PB-01 through PB-[NN]. BC-COVERAGE-RECORD. PBI is now frozen. |
| **Exclusion In Effect** | BC excluded from Steps 2-7: no signal artifact access, no HL authorship, no correction drafting. Exception: BC is VERIFIER for PBI-Ref mismatch repairs per RESOLUTION PROTOCOL. |
| **Receiving Role** | INSTITUTIONAL ARCHAEOLOGIST (IA) -- Steps 2-7 |

*Label this table: PHASE-HANDOVER-BC*

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
  3. PHASE-HANDOVER-EF table (5-row; EF exit confirmed; BC receiving)
  4. PBI PRODUCTION PROTOCOL output (BC; [FREEZE] sub-phase)
  5. BC-COVERAGE-RECORD (Step 1 [COVERAGE AUDIT]; design materials; exclusions;
     completeness basis)
  6. PHASE-HANDOVER-BC table (5-row; BC exit confirmed; PBI frozen + coverage record
     complete; entry count; IA receiving)
  7. HANDLE LEDGER PROTOCOL output (IA)
  8. Corrections -- HIGH -> MEDIUM -> LOW (CORRECTION RECORD SCHEMA)
  9. Entry Gate blocks (all STATUS: CLEARED)
  10. Chain Integrity Audit (all CHAIN-COMPLETE)
  11. Resolution Protocol trace (verifier named per flag type)
  12. Rules of Thumb (RULES-ANCHORED-COMPLETE with per-rule tier quotation)
  13. Surprise hierarchy (ranked with rationale)
  14. Pattern of inherited errors
  15. Blind Spot Map
  16. Correction Forward Statement (confirms NO-ECHO COST; names specific avoided failure)
  17. What this correction record excludes

Write to: simulations/topic/echo/{topic}-echo-{YYYY-MM-DD}.md

---

## V-05 -- Full Axis Integration (Lifecycle Emphasis + Output Format + Phrasing Register)

**Variation axis:** All three axes -- Axis A (BC sub-phases + BC-COVERAGE-RECORD) +
Axis B (table-format handovers) + Axis C (imperative filter documentation)

**Hypothesis:** V-04 showed Axes A and B are compositional -- distinct structural
zones, no interference. Adding Axis C (phrasing register change in STILL-LIVE FILTER)
to the V-04 base tests whether imperative filter documentation is equally compositional.
The structural zones remain independent: BC sub-phases in Step 1 (Axis A); table
handovers at step boundaries (Axis B); imperative filter commands in Step 3 STILL-LIVE
FILTER (Axis C). All three should compose without interaction. V-05 is the ceiling
variation: 230/230 under v11. If it scores correctly, the three implementation axes
are mutually independent and the ceiling is reachable via multiple structural paths --
the implementation-robustness thesis holds.

**Expected v11 score:** 230 (C-34 PASS; C-35 PASS; C-36 PASS -- ceiling)

**Discriminant from R10 V-05:** Three distinct implementation-axis choices (lifecycle
sub-phasing, table-format tokens, imperative grammar) vs. R10's structural additions
(appended blocks, code-block tokens, conditional branching). Same criteria satisfied;
different prompting strategy across all three axes simultaneously.

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
              before any signal reading begins. At end of Step 0,
              complete the PHASE-HANDOVER-EF transition table before
              handing over to BC.
Input:        Design materials only. Signal artifacts out of scope.
              EF-INVOCATION-RECORD must name every pre-investigation
              source consulted and list all signal artifacts as excluded.
Out-of-scope: PBI production. Entry authoring. Chain verification.
Phase scope:  Step 0 only. EF excluded from Steps 1-7.
Gate return:  ENFORCEMENT MECHANISM + EF-INVOCATION-RECORD +
              PHASE-HANDOVER-EF table all complete before Step 1.
----------------------------------------------------------------------
```

**Belief Cartographer (BC)** -- Step 1 exclusively; three sub-phases.

```
BELIEF CARTOGRAPHER -- FUNCTION DECLARATION
----------------------------------------------------------------------
Function:     Pre-investigation belief recovery. Three sub-phases:
              [SCAN] Read design materials; identify belief candidates.
              [FREEZE] Produce PBI; freeze all PB-[NN] entries.
              [COVERAGE AUDIT] Produce BC-COVERAGE-RECORD; complete
              PHASE-HANDOVER-BC table. BC exclusion takes effect after
              both are written.
Input:        Design materials only. Same exclusion as EF.
Out-of-scope: Signal artifacts. Handle Ledger. Entry authoring.
Phase scope:  Step 1 only. BC exclusion takes effect after [COVERAGE
              AUDIT] gate return and PHASE-HANDOVER-BC table are complete.
Gate return:  PBI (all PB-[NN] entries) + BC-COVERAGE-RECORD +
              PHASE-HANDOVER-BC table all complete before Step 2.
----------------------------------------------------------------------
```

**Institutional Archaeologist (IA)** -- Steps 2-7. Every STILL-LIVE FILTER evaluation
produces a written record. Every candidate that does not enter the correction register
produces a typed discard entry. The filter is fully documented from first candidate to
DISCARD-LOG-COMPLETE.

```
INSTITUTIONAL ARCHAEOLOGIST -- FUNCTION DECLARATION
----------------------------------------------------------------------
Function:     False-assumption recovery. Correction register only.
              Every STILL-LIVE FILTER evaluation produces a written
              record -- either a correction entry or a DISCARD-[N]
              entry. After all candidates, write DISCARD-LOG-COMPLETE.
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
   A reviewer can re-derive the cost from this material alone.]
----------------------------------------------------------------------
```

At end of Step 0, complete the transition record before proceeding to Step 1:

| Field | Value |
|-------|-------|
| **Completing Role** | ENFORCEMENT FRAMER (EF) |
| **Step Completed** | 0 |
| **Output Produced** | ENFORCEMENT MECHANISM DECLARATION + NO-ECHO COST + EF-INVOCATION-RECORD |
| **Exclusion In Effect** | EF excluded from Steps 1-7: no signal artifact access, no PBI authorship, no chain verification |
| **Receiving Role** | BELIEF CARTOGRAPHER (BC) -- Step 1 |

*Label this table: PHASE-HANDOVER-EF*

---

### Step 1 -- [BC] Belief Inventory, Coverage Audit, and Phase Handover

**[SCAN]** Read all design materials within BC's input scope. Signal artifacts are
out of scope. Identify every belief candidate -- any claim, assumption, or design
premise that could be carried as prior knowledge. Complete the full scan before [FREEZE].

**[FREEZE]** Produce the PBI from the scanned materials.

```
PBI PRODUCTION PROTOCOL
----------------------------------------------------------------------
Input:    Design materials only. Signal artifacts excluded.
Format:   PB-[NN]: ["Today's materials imply that X." No signal knowledge.]
Freeze:   PBI frozen at end of [FREEZE] sub-phase. No new PB-[NN]
          entries after this point.
          PBI entries must not use handle labels (unavailable at Step 1).
----------------------------------------------------------------------
```

**[COVERAGE AUDIT]** After PBI freeze, produce the coverage record and the transition
table. BC exclusion does not take effect until both are written.

```
BC-COVERAGE-RECORD
----------------------------------------------------------------------
Sub-phase:  [COVERAGE AUDIT] (final BC sub-phase before exclusion)
Materials consulted (pre-investigation only):
  [List each design document, spec, proposal, or other pre-investigation
   source scanned during [SCAN] and [FREEZE] sub-phases. File name or
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

After BC-COVERAGE-RECORD is complete, complete the transition record:

| Field | Value |
|-------|-------|
| **Completing Role** | BELIEF CARTOGRAPHER (BC) |
| **Step Completed** | 1 |
| **Output Produced** | PBI -- [N] entries: PB-01 through PB-[NN]. BC-COVERAGE-RECORD. PBI is now frozen. |
| **Exclusion In Effect** | BC excluded from Steps 2-7: no signal artifact access, no HL authorship, no correction drafting. Exception: BC is VERIFIER for PBI-Ref mismatch repairs per RESOLUTION PROTOCOL. |
| **Receiving Role** | INSTITUTIONAL ARCHAEOLOGIST (IA) -- Steps 2-7 |

*Label this table: PHASE-HANDOVER-BC*

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

### Step 3 -- [IA] Draft All Corrections with Documented Filter

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

STILL-LIVE FILTER -- DOCUMENTED EVALUATION:

For each candidate identified in the signal sweep:

  1. Apply the test: "Would a new team carry this as a false assumption
     going into their next investigation?"

  2. For each candidate that qualifies: draft a correction entry per
     the schema above.

  3. For each candidate that does not qualify: write a DISCARD entry
     immediately -- before moving to the next candidate:

       DISCARD-[N]: [finding label -- HL-[NN] or 3-5 word description]
       Route:  topic-story
       Reason: [One sentence. Name the specific claim or component that
                makes this a confirmed finding rather than a false
                assumption. State why a new team would not carry this
                as wrong prior knowledge. "Not relevant" fails.]

  4. After all candidates are evaluated (every candidate either has
     a correction entry or a DISCARD-[N] entry): write the closure:

       DISCARD-LOG-COMPLETE
       ----------------------------------------------------------------
       Candidates considered:   [total count -- integer]
       Accepted (correction):   [count with correction entries]
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
  3. PHASE-HANDOVER-EF table (5-row; EF exit confirmed; BC receiving)
  4. PBI PRODUCTION PROTOCOL output (BC; [FREEZE] sub-phase)
  5. BC-COVERAGE-RECORD (Step 1 [COVERAGE AUDIT]; design materials; exclusions;
     completeness basis)
  6. PHASE-HANDOVER-BC table (5-row; BC exit confirmed; PBI frozen + coverage record
     complete; entry count; IA receiving)
  7. HANDLE LEDGER PROTOCOL output (IA)
  8. Corrections -- HIGH -> MEDIUM -> LOW (CORRECTION RECORD SCHEMA)
  9. DISCARD-[N] entries (one per non-qualifying candidate; inline with evaluation)
  10. DISCARD-LOG-COMPLETE (candidates / accepted / discarded counts)
  11. Entry Gate blocks (all STATUS: CLEARED)
  12. Chain Integrity Audit (all CHAIN-COMPLETE)
  13. Resolution Protocol trace (verifier named per flag type)
  14. Rules of Thumb (RULES-ANCHORED-COMPLETE with per-rule tier quotation)
  15. Surprise hierarchy (ranked with rationale)
  16. Pattern of inherited errors
  17. Blind Spot Map
  18. Correction Forward Statement (confirms NO-ECHO COST; names specific avoided failure)
  19. What this correction record excludes

Write to: simulations/topic/echo/{topic}-echo-{YYYY-MM-DD}.md

---

## Scoring Summary

| Variation | Axis A | Axis B | Axis C | C-34 | C-35 | C-36 | v11 score |
|-----------|--------|--------|--------|:----:|:----:|:----:|:---------:|
| V-01 | Lifecycle Emphasis | -- | -- | PASS | FAIL | FAIL | 220 |
| V-02 | -- | Output Format | -- | FAIL | PASS | FAIL | 220 |
| V-03 | -- | -- | Phrasing Register | FAIL | FAIL | PASS | 220 |
| V-04 | Lifecycle Emphasis | Output Format | -- | PASS | PASS | FAIL | 225 |
| **V-05** | Lifecycle Emphasis | Output Format | Phrasing Register | PASS | PASS | PASS | **230** |

**Implementation-robustness thesis:** If V-05 scores 230/230, then C-34/C-35/C-36
can be satisfied via sub-phase lifecycle structuring (not only appended blocks),
table tokens (not only code-block tokens), and imperative grammar (not only
conditional branching). Multiple prompt strategies converge on the same rubric
ceiling. The criteria are implementation-robust.
