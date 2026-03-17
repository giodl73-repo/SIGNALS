---
skill: quest-variate
skill_target: topic-echo
date: 2026-03-16
round: 19
rubric: v19
rubric_file: simulations/quest/rubrics/topic-echo-rubric-v19-2026-03-16.md
rubric_max: 350
---

# Variations: `topic:echo` -- Round 19 (2026-03-16)

**Rubric:** v19 (2026-03-16) | **Criteria:** 60 (5 essential / 3 recommended / 52 aspirational)

---

## Design Context

R18 V-05 achieves 335/335 under v18. All three R18 closure-layer patterns -- TOKEN-FORMAT-SELF-CERTIFYING
(C-55), GATE-INDEPENDENCE-ENFORCED (C-56), MANIFEST-ROW-INLINE-EVIDENCE (C-57) -- are present and
formally declared. Under v19, R18 V-05 scores 335 unchanged: 0 delta. The three new criteria (C-58,
C-59, C-60) identify structural gaps in the closure layer that remain open even when C-55/C-56/C-57
are fully satisfied.

**What remains unresolved in R18 V-05:**

- **C-58 gap (GATE-TOKEN-REGISTRY absent):** R18 V-05 produces three gate tokens, all self-certifying
  per C-55. But no registry declares the expected token set before Step 0. Token completeness
  verification requires full-artifact traversal to locate all three tokens and confirm the triad is
  present. A missing token cannot be detected by diff -- only by scan. The C-55 contract (each present
  token is internally consistent) does not guarantee the token set is complete.

- **C-59 gap (MANIFEST-COMPLETE uncertified for C-57):** R18 V-05 TYPE-C manifest rows carry the
  confirming artifact in the STATUS CELL (C-57 PASS). The MANIFEST-COMPLETE token carries per-type
  counts per C-55. But MANIFEST-COMPLETE states "K TYPE-C RESOLVED" without certifying that those K
  rows carry inline evidence. A reviewer reading MANIFEST-COMPLETE can confirm citation accounting
  (C-52) but cannot confirm inline-evidence presence (C-57) from the token alone. The terminal audit
  token does not self-certify the full closure-layer state it claims to close.

- **C-60 gap (cross-layer consistency unchecked):** R18 V-05 STILL-LIVE FILTER Belief-Ref cells
  carry the confirming artifact (C-54). Manifest TYPE-C STATUS cells also carry the confirming
  artifact (C-57). Both cells reference the same physical evidence for the same belief. No prior
  criterion requires them to be verified as naming the same source. They are produced at different
  steps by different roles and can diverge through editorial error -- both presenting as RESOLVED
  while naming different artifacts. No token confirms the two layers agree.

**R19 variation axes:**

- **Axis A (C-58):** Add GATE-TOKEN-REGISTRY block at heading-navigable position before Step 0,
  listing all gate tokens by canonical name, step location, and prerequisite criterion. Token absence
  becomes diff-detectable against the declared registry.

- **Axis B (C-59):** Extend the MANIFEST-COMPLETE token format in TOKEN CONTENT REQUIREMENT to
  carry a C-57 compliance suffix: `[Q] TYPE-C RESOLVED (confirming artifact INLINE in all [Q] rows)`.
  Terminal manifest token self-certifies both citation accounting and inline-evidence presence.

- **Axis C (C-60):** Add Step 9 Cross-Layer Citation Consistency Check after manifest completion.
  Per TYPE-C citation: compare Belief-Ref artifact (STILL-LIVE FILTER) against STATUS CELL artifact
  (manifest). Emit CROSS-CITATION-CONSISTENT token only when all rows MATCH.

**Predicted R19 scoring:**

| Variation | C-58 | C-59 | C-60 | v18 | v19 | delta |
|-----------|:----:|:----:|:----:|:---:|:---:|:-----:|
| V-01 (Axis A) | PASS | FAIL | FAIL | 335 | 340 | +5 |
| V-02 (Axis B) | FAIL | PASS | FAIL | 335 | 340 | +5 |
| V-03 (Axis C) | FAIL | FAIL | PASS | 335 | 340 | +5 |
| V-04 (A+B) | PASS | PASS | FAIL | 335 | 345 | +10 |
| **V-05 (A+B+C)** | PASS | PASS | PASS | 335 | **350** | **+15** |

**Scoring rationale:**

- **V-01**: GATE-TOKEN-REGISTRY present listing GT-01/GT-02/GT-03 before Step 0. C-58 PASS.
  MANIFEST-COMPLETE format unchanged from R18 -- no inline-evidence suffix. C-59 FAIL. No
  cross-layer consistency check. C-60 FAIL. Net: +5.

- **V-02**: No GATE-TOKEN-REGISTRY. C-58 FAIL. MANIFEST-COMPLETE format carries C-57 suffix
  per extended TOKEN CONTENT REQUIREMENT. C-59 PASS -- reviewer confirms inline-evidence
  presence from token alone. No cross-layer consistency check. C-60 FAIL. Net: +5.

- **V-03**: No GATE-TOKEN-REGISTRY. C-58 FAIL. MANIFEST-COMPLETE format unchanged. C-59 FAIL.
  Step 9 cross-layer check present; CROSS-CITATION-CONSISTENT emitted when all rows MATCH.
  C-60 PASS. Net: +5.

- **V-04**: GATE-TOKEN-REGISTRY present (C-58 PASS) and MANIFEST-COMPLETE extended (C-59 PASS).
  No Step 9 consistency check. C-60 FAIL. Net: +10.

- **V-05**: All three axes. GATE-TOKEN-REGISTRY lists GT-01 through GT-04 (including
  CROSS-CITATION-CONSISTENT at Step 9). MANIFEST-COMPLETE extended for C-59. Step 9
  cross-layer check produces CROSS-CITATION-CONSISTENT. C-58/C-59/C-60 all PASS. Net: +15.
  Maximum possible score: 350.

**Gate chain extended:** ... -> R18 token inventory declared, manifest token extended for
inline-evidence, cross-layer citation consistent.

---

## V-01 -- Axis A: Gate-Token Registry Declared (C-58 targeted; C-59 C-60 absent)

**Variation axis:** Output format -- a GATE-TOKEN-REGISTRY block is declared at heading-navigable
position before Step 0, listing all three expected gate tokens (MANIFEST-COMPLETE,
CONSUMER-INDEX-COMPLETE, CHAIN-GROUNDING-COMPLETE) by canonical name with step location and
prerequisite criterion. Token completeness is now diff-detectable. Axis A only; C-59 and C-60
not present.

**Hypothesis:** R18 V-05 produces all three gate tokens and they are self-certifying per C-55.
But no declared baseline makes token absence detectable without full-artifact scan. C-58
requires a GATE-TOKEN-REGISTRY at heading level before Step 0 -- the same traversal-free
completeness contract that C-44 applied to phase transitions. Adding the registry at the correct
structural position satisfies C-58 without modifying any existing token formats. The registry
serves as the audit baseline: a reviewer diffs emitted tokens against GT-01..GT-03 without
scanning the artifact.

**Expected v19 score:** 340 (C-01 through C-57 all PASS as in R18 V-05; C-58: PASS;
C-59: FAIL -- MANIFEST-COMPLETE format unchanged; C-60: FAIL -- no cross-layer check)

---

Topic: `{topic}`

Synthesize what was unexpected. Three roles at three exclusive phase boundaries. Every structural
commitment is named, formal, and auditable from output. This is not a summary. This is not a list
of findings. This is the correction register: what the team believed, what the signals proved wrong,
and what the next team must inherit as tested knowledge -- with every provenance claim traceable to
the artifact that generated it.

---

### GATE-TOKEN-REGISTRY [AXIS A -- C-58]

Expected gate tokens for this artifact. All three tokens must be present at their declared step
locations. Token absence is detectable by diff against this registry without full-artifact
traversal. A token listed here but absent from the artifact is missing -- its absence is not
ambiguous. A token not listed here should not appear as a gate token.

| Token-ID | Canonical Name | Step | Prerequisite Criterion |
|----------|----------------|------|------------------------|
| GT-01 | MANIFEST-COMPLETE | Step 8 | C-52 (citation-completeness manifest exhaustive) |
| GT-02 | CONSUMER-INDEX-COMPLETE | Step 7 | C-53 (declaring-section consumer index populated) |
| GT-03 | CHAIN-GROUNDING-COMPLETE | Step 7 | C-54 (citation chain PBI grounding verified) |

Registry declared before Step 0. Diff this table against emitted tokens to verify completeness.

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
              HANDOVER-[N] table before advancing. At Step 7, emit
              CONSUMER-INDEX-COMPLETE (GT-02) and CHAIN-GROUNDING-
              COMPLETE (GT-03) as INDEPENDENT tokens per the
              GATE-INDEPENDENCE-ENFORCED constraint. Each token must
              be self-certifying per the TOKEN CONTENT REQUIREMENT.
              At Step 8, produce the CITATION-COMPLETENESS-MANIFEST
              (GT-01) with a self-certifying MANIFEST-COMPLETE token;
              TYPE-C rows carry the confirming artifact in the STATUS
              CELL per MANIFEST-ROW-INLINE-EVIDENCE. Three gate tokens
              required (see GATE-TOKEN-REGISTRY); any absent or
              non-self-certifying token is an incompletion.
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

---

#### TOKEN CONTENT REQUIREMENT [C-55]

Every gate token emitted in this artifact must carry inline specifics sufficient to verify its
pass condition without consulting the underlying artifact sections. This requirement applies to
all three gate tokens declared in the GATE-TOKEN-REGISTRY.

**Required format for MANIFEST-COMPLETE (GT-01):**

```
MANIFEST-COMPLETE: CIT-[N1]..CIT-[N2] [K] TYPE-A RESOLVED,
  CIT-[M1]..CIT-[M2] [L] TYPE-B RESOLVED,
  CIT-[P1]..CIT-[P2] [Q] TYPE-C RESOLVED --
  citation-completeness verified; no document traversal required
  to confirm all addresses resolve.
```

A token omitting per-type ID ranges, counts, or traversal confirmation fails.

**Required format for CONSUMER-INDEX-COMPLETE (GT-02):**

```
CONSUMER-INDEX-COMPLETE: BC-COVERAGE-RECORD Schema [F-BCR-1..F-BCR-4]
  Consumer-Ref POPULATED, Phase Transition Registry [T-00..T-06]
  Consumer-Ref POPULATED, STILL-LIVE FILTER [MUST-1..MUST-4]
  Consumer-Ref POPULATED -- bidirectional navigability confirmed
  across all three axes.
```

Each of the three table headings must be named individually with their ID ranges.

**Required format for CHAIN-GROUNDING-COMPLETE (GT-03):**

```
CHAIN-GROUNDING-COMPLETE: Belief-Ref cells EXTENDED
  (all MUST-[N] carry confirming artifact reference),
  F-BCR-4 SPECIFIC (names PB-[NN] through PB-[NN]) --
  citation chain verified to evidence; both C-54 conditions confirmed.
```

Both condition labels must be present. A token missing either label fails.

---

#### GATE-INDEPENDENCE-ENFORCED [C-56]

Combined tokens are non-conforming when multiple gates close at the same step boundary.
This constraint is named GATE-INDEPENDENCE-ENFORCED so that any violation cites a named
constraint. Each gate criterion's token is individually falsifiable; merging tokens makes
individual satisfiability unverifiable and violates this constraint.

**Step 7 application:** CONSUMER-INDEX-COMPLETE (GT-02) and CHAIN-GROUNDING-COMPLETE (GT-03)
both close at Step 7. They must be emitted as separate independent tokens. A combined token
is non-conforming regardless of content.

**Explicit prohibition statement:** At any step boundary where two or more gate criteria close
simultaneously, combined tokens are non-conforming. Each gate emits a separate token with its
own inline certification per TOKEN CONTENT REQUIREMENT.

---

#### MANIFEST-ROW-INLINE-EVIDENCE [C-57]

TYPE-C rows in the CITATION-COMPLETENESS-MANIFEST carry the confirming artifact in the STATUS
CELL:

```
RESOLVED (confirmed false by: [artifact name, namespace, date])
```

A TYPE-C row with bare RESOLVED in the status cell fails. A TYPE-C row placing the confirming
artifact in Target Address but using bare RESOLVED in the status cell also fails. TYPE-A and
TYPE-B rows use bare RESOLVED.

---

#### Phase Transition Registry [C-50 -- Consumer-Ref column]

Pre-declared registry of all seven phase transitions. T-ID column assigns stable identifiers.
Consumer-Ref column names the consuming inline table for bidirectional navigability.

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

Three sequential sub-phases. Do not merge. Write each sub-phase gate token before advancing.

**[SCAN]** -- Enumerate all design materials available pre-investigation. List each by name.
Signal artifacts are out of scope; note each by name and exclude.
Gate: `COMMIT-SCAN: [N] design materials identified, [M] signal artifacts excluded by name.`

**[FREEZE]** -- Convert design materials into prior belief assertions. Each PBI entry:
`PB-[NN]: We expected [specific claim]. Source: [material name]. Category: [domain].`
Gate: `COMMIT-FREEZE: [K] PBI entries written; PBI closed.`

**[COVERAGE AUDIT]** -- Confirm coverage completeness. Produce BC-COVERAGE-RECORD using the
schema below. Write F-BCR field-IDs as column prefixes in output headers.
Gate: Write BC-COVERAGE-RECORD output and advance to PHASE-HANDOVER-1.

#### BC-COVERAGE-RECORD Schema [C-46/C-49 -- field-IDs + Consumer-Ref]

| F-ID | Field | Content | Constraint | Consumer-Ref |
|------|-------|---------|------------|--------------|
| F-BCR-1 | Sub-phase | [COVERAGE AUDIT] | Fixed; do not substitute. | Consumed-By: [COVERAGE AUDIT] output header; PHASE-HANDOVER-1 Output Produced field |
| F-BCR-2 | Materials consulted | [List each design document scanned during [SCAN] and [FREEZE].] | Pre-investigation only. | Consumed-By: [COVERAGE AUDIT] output header |
| F-BCR-3 | Signal artifacts excluded | [List each signal artifact by name.] | Enumerated by name. | Consumed-By: [COVERAGE AUDIT] output header |
| F-BCR-4 | PBI completeness basis | [Name specific PBI entries: "PB-NN through PB-NN (from material name)." Generic sentence fails C-54.] | Names specific PB-[NN] entries. C-54 condition 2. | Consumed-By: [COVERAGE AUDIT] output header |

**F-BCR-4 format requirement (C-54 condition 2):**
`F-BCR-4: PBI completeness basis -- PB-[NN1] through PB-[NNk] (from [material name]).`
A generic sentence such as "the design spec provided the primary basis" fails.

---

### Step 0 -- [EF] Enforcement Section

Produce ENFORCEMENT MECHANISM section at artifact head position. Enforce from design materials
only. Declare:
- **Enforcement mechanism** and its strength classification (structural / procedural / attestation-only).
- **NO-ECHO COST**: the concrete institutional loss if this artifact is skipped.
- **EF-INVOCATION-RECORD**: discrete block recording what EF saw at Step 0 (topic, signal set size,
  declared mechanism, NO-ECHO COST output).

The ENFORCEMENT MECHANISM DECLARATION section must be at position 1 of the artifact -- before
all surprise entries, before the PBI, before the Handle Ledger.

PHASE-HANDOVER-0 (registry entry: T-00) before proceeding to Step 1.

---

### Step 1 -- [BC] Belief Inventory

Execute BC-STEP1-PROTOCOL: [SCAN] -> [FREEZE] -> [COVERAGE AUDIT]. Write each sub-phase gate
token before advancing. Produce frozen PBI, BC-COVERAGE-RECORD (F-BCR field-IDs in headers),
and PHASE-HANDOVER-1.

PHASE-HANDOVER-1 (registry entry: T-01) before proceeding to Step 2.

---

### Step 2 -- [IA] Handle Ledger

Produce one named Handle per candidate surprise. Format: `HL-[N]: [HANDLE-NAME]` (2-5 words,
all-caps, unique, specific to this investigation). No belief language in handles -- finding
language only. Handles serve as stable citation keys.

PHASE-HANDOVER-2 (registry entry: T-02) before proceeding to Step 3.

---

### Step 3 -- [IA] Draft All Corrections

For each STILL-LIVE candidate: draft the full correction entry in discovery register format.
Apply STILL-LIVE FILTER to all candidates. Write DISCARD-LOG-COMPLETE when all candidates
are resolved.

**Discovery register entry format:**

```
Handle:   [HL-N name] (from Handle Ledger)
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
```

**STILL-LIVE FILTER -- TABLE-COLUMN MUST-CLAUSE PROTOCOL**

Apply each MUST-clause to every candidate. Scope and Action are separate columns. Each MUST-clause
carries a stable MUST-ID (C-48), an extended Belief-Ref (C-54 format), and a Consumer-Ref (C-53).

| MUST-ID | Scope | Action | Constraint | Belief-Ref | Consumer-Ref |
|---------|-------|--------|------------|------------|--------------|
| MUST-1 | EVERY CANDIDATE -- no exceptions | Produce exactly one of: `STILL-LIVE-[N]: [name]` OR `DISCARD-[N]: [name]` | No candidate evaluation concludes without one of these tokens. | PB-[NN] (confirmed false by: [artifact name, namespace, date]) | Consumed-By: per-candidate evaluation token in Step 3 |
| MUST-2 | EVERY DISCARD-[N] TOKEN -- no exceptions | Immediately write: `DISCARD-[N]-PBI-REF: PB-[NN]` | A DISCARD token without a PBI-Ref token is malformed. | PB-[NN] (confirmed false by: [artifact name, namespace, date]) | Consumed-By: DISCARD-[N]-PBI-REF token in Step 3 |
| MUST-3 | EVERY DISCARD-[N] TOKEN -- no exceptions | Immediately write: `DISCARD-[N]-ROUTE: [destination]` | A DISCARD token without a ROUTE token is malformed. | PB-[NN] (confirmed false by: [artifact name, namespace, date]) | Consumed-By: DISCARD-[N]-ROUTE token in Step 3 |
| MUST-4 | EVERY DISCARD-[N] TOKEN -- no exceptions | Immediately write: `DISCARD-[N]-REASON: [one sentence]` | A DISCARD token without a REASON token is malformed. | PB-[NN] (confirmed false by: [artifact name, namespace, date]) | Consumed-By: DISCARD-[N]-REASON token in Step 3 |

`DISCARD-LOG-COMPLETE: [N] STILL-LIVE, [M] DISCARD -- all four MUST-clauses applied to every candidate; no candidate unresolved.`

PHASE-HANDOVER-3 (registry entry: T-03) before proceeding to Step 4.

---

### Step 4 -- [IA] Register Audit

```
REGISTER AUDIT PROTOCOL
----------------------------------------------------------------------
Execute field by field before Step 5. Rewrite any field:
  Source: prose -> namespace:skill:artifact
  Implies: narration -> future-team framing
  Wrong: softener -> specific wrong component
  Decide: deferral -> blocking decision
  Verified: identifiers -> quoted actual text of both
----------------------------------------------------------------------
```

PHASE-HANDOVER-4 (registry entry: T-04) before proceeding to Step 5.

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

PHASE-HANDOVER-5 (registry entry: T-05) before proceeding to Step 6.

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
Gate:     CHAIN-FLAG IS A HARD GATE. Any flag halts artifact
          completion until resolved via RESOLUTION PROTOCOL below.
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

PHASE-HANDOVER-6 (registry entry: T-06) before proceeding to Step 7.

---

### Step 7 -- [IA] Hierarchy, Distillation, and Completeness Gates

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

**Pattern of inherited errors:** 2-4 sentences. Named structural origin.

**Blind Spot Map:** Categories as types of wrong thinking. Assign each correction.

**Correction Forward Statement:** 1-3 sentences. Name the specific failure this artifact
prevented. Confirm EF's NO-ECHO COST.

**What this correction record excludes:** At least two categories with counts.

**After artifact content is complete, emit both completeness gates as INDEPENDENT tokens
per GATE-INDEPENDENCE-ENFORCED. Each token self-certifying per TOKEN CONTENT REQUIREMENT:**

Gate 1 (C-53) -- CONSUMER-INDEX-COMPLETE (GT-02):

```
CONSUMER-INDEX-COMPLETE PROTOCOL (C-53)
----------------------------------------------------------------------
Purpose:   Verify Consumer-Ref columns populated in all three
           declaring tables simultaneously.
Tables:    BC-COVERAGE-RECORD Schema (F-BCR-1..4 Consumer-Ref)
           Phase Transition Registry (T-00..T-06 Consumer-Ref)
           STILL-LIVE FILTER (MUST-1..MUST-4 Consumer-Ref)
Independence: Emitted as independent token per GATE-INDEPENDENCE-
           ENFORCED. No combined token with Gate 2.
----------------------------------------------------------------------
```

`CONSUMER-INDEX-COMPLETE: BC-COVERAGE-RECORD Schema F-BCR-1..F-BCR-4 Consumer-Ref POPULATED, Phase Transition Registry T-00..T-06 Consumer-Ref POPULATED, STILL-LIVE FILTER MUST-1..MUST-4 Consumer-Ref POPULATED -- bidirectional navigability confirmed across all three axes.`

Gate 2 (C-54) -- CHAIN-GROUNDING-COMPLETE (GT-03):

```
CHAIN-GROUNDING-COMPLETE PROTOCOL (C-54)
----------------------------------------------------------------------
Purpose:   Verify citation chain grounded at evidence layer.
Condition 1: All MUST-[N] Belief-Ref cells carry confirming artifact
           reference (extended format, not PB-[NN] alone).
Condition 2: F-BCR-4 output names specific PBI entries by ID range
           and source material (not a generic summary sentence).
Independence: Emitted as independent token per GATE-INDEPENDENCE-
           ENFORCED. Not combined with Gate 1.
----------------------------------------------------------------------
```

`CHAIN-GROUNDING-COMPLETE: Belief-Ref cells EXTENDED (all MUST-[N] carry confirming artifact reference), F-BCR-4 SPECIFIC (names PB-[NN] through PB-[NN]) -- citation chain verified to evidence; both C-54 conditions confirmed.`

These two tokens are at the same step boundary. Per GATE-INDEPENDENCE-ENFORCED, they are
emitted as separate tokens. A combined token is non-conforming.

---

### Step 8 -- [IA] Citation-Completeness Manifest [C-52 + C-55 SELF-CERTIFYING + C-57 STATUS CELL]

After Step 7 gates are confirmed, produce the CITATION-COMPLETENESS-MANIFEST.

```
CITATION-COMPLETENESS-MANIFEST PROTOCOL
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

Self-certifying closure token (TOKEN CONTENT REQUIREMENT satisfied; C-57 STATUS CELL format):

`MANIFEST-COMPLETE: CIT-01..CIT-04 [4] TYPE-A RESOLVED, CIT-05..CIT-11 [7] TYPE-B RESOLVED, CIT-12..CIT-[N] [M] TYPE-C RESOLVED -- citation-completeness verified; no document traversal required to confirm all addresses resolve.`

== ARTIFACT STRUCTURE ============================================================

  1. ENFORCEMENT MECHANISM DECLARATION (EF; NO-ECHO COST named; C-26)
  2. EF-INVOCATION-RECORD (Step 0; C-33)
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
  23. CONSUMER-INDEX-COMPLETE gate token (Step 7; GT-02; independent; self-certifying) (C-53+C-55)
  24. CHAIN-GROUNDING-COMPLETE gate token (Step 7; GT-03; independent; self-certifying) (C-54+C-55)
      Note: Gates 23 and 24 independent per GATE-INDEPENDENCE-ENFORCED (C-56)
  25. CITATION-COMPLETENESS-MANIFEST (Step 8; GT-01; self-certifying MANIFEST-COMPLETE;
      TYPE-C STATUS CELL carries confirming artifact) (C-52+C-55+C-57)
  Note: GATE-TOKEN-REGISTRY at heading level before Step 0 [AXIS A C-58] -- items 1-25 diff against GT-01..GT-03

Write to: simulations/topic/echo/{topic}-echo-{YYYY-MM-DD}.md

---

## V-02 -- Axis B: Manifest-Token Extended for Inline-Evidence (C-59 targeted; C-58 C-60 absent)

**Variation axis:** Output format -- MANIFEST-COMPLETE token format in TOKEN CONTENT REQUIREMENT
is extended to carry a C-57 compliance suffix: `[Q] TYPE-C RESOLVED (confirming artifact INLINE
in all [Q] rows)`. Named MANIFEST-TOKEN-INLINE-EVIDENCE-SUFFIX block declares the extension.
Axis B only; C-58 and C-60 not present.

**Hypothesis:** R18 V-05 TYPE-C manifest rows carry the confirming artifact in the STATUS CELL
(C-57 PASS). MANIFEST-COMPLETE carries per-type counts (C-55 PASS). But MANIFEST-COMPLETE states
"Q TYPE-C RESOLVED" without asserting that those Q rows carry inline evidence. A reviewer reading
MANIFEST-COMPLETE can confirm citation accounting but cannot confirm inline-evidence presence from
the token alone -- the terminal audit token is not self-certifying with respect to C-57. C-59
requires the TYPE-C count field to carry the suffix `(confirming artifact INLINE in all [Q] rows)`.
V-02 adds a named heading-level declaration (MANIFEST-TOKEN-INLINE-EVIDENCE-SUFFIX) that extends
the TOKEN CONTENT REQUIREMENT's MANIFEST-COMPLETE format. C-58 and C-60 are absent; only the
manifest token extension is targeted.

**Expected v19 score:** 340 (C-01 through C-57 all PASS as in R18 V-05; C-58: FAIL -- no
GATE-TOKEN-REGISTRY; C-59: PASS -- MANIFEST-COMPLETE carries C-57 suffix; C-60: FAIL -- no
cross-layer check)

---

Topic: `{topic}`

_(Intro paragraph identical to V-01.)_

---

_(GATE-TOKEN-REGISTRY section ABSENT -- Axis A not present in V-02.)_

### Roles

_(EF and BC function declarations identical to V-01.)_

**Institutional Archaeologist (IA)** -- Steps 2-8.

```
INSTITUTIONAL ARCHAEOLOGIST -- FUNCTION DECLARATION
----------------------------------------------------------------------
Function:     False-assumption recovery. Correction register only.
              Each IA stage exit (Steps 2-6) produces a PHASE-
              HANDOVER-[N] table before advancing. At Step 7, emit
              CONSUMER-INDEX-COMPLETE and CHAIN-GROUNDING-COMPLETE as
              INDEPENDENT tokens per GATE-INDEPENDENCE-ENFORCED. Each
              token self-certifying per TOKEN CONTENT REQUIREMENT. At
              Step 8, produce the CITATION-COMPLETENESS-MANIFEST with
              a MANIFEST-COMPLETE token that is self-certifying for
              BOTH citation accounting (C-52) and inline-evidence
              presence (C-57) per the MANIFEST-TOKEN-INLINE-EVIDENCE-
              SUFFIX declaration below. TYPE-C STATUS CELL format per
              MANIFEST-ROW-INLINE-EVIDENCE.
Input:        Signal artifacts + frozen PBI (read-only).
Out-of-scope: PBI authorship (frozen). Enforcement section (immutable).
Orienting:    "What would the next team build wrong?"
Phase scope:  Steps 2-8 only.
----------------------------------------------------------------------
```

_(Phase Handover Schema, GATE-INDEPENDENCE-ENFORCED, MANIFEST-ROW-INLINE-EVIDENCE,
Phase Transition Registry, BC-STEP1-PROTOCOL, BC-COVERAGE-RECORD Schema,
and Steps 0-6 identical to V-01.)_

---

#### TOKEN CONTENT REQUIREMENT [C-55 + C-59 MANIFEST-COMPLETE EXTENSION]

Every gate token emitted in this artifact must carry inline specifics sufficient to verify its
pass condition without consulting the underlying artifact sections.

**Required format for MANIFEST-COMPLETE (extended for C-59):**

```
MANIFEST-COMPLETE: CIT-[N1]..CIT-[N2] [K] TYPE-A RESOLVED,
  CIT-[M1]..CIT-[M2] [L] TYPE-B RESOLVED,
  CIT-[P1]..CIT-[P2] [Q] TYPE-C RESOLVED
    (confirming artifact INLINE in all [Q] rows) --
  citation-completeness and inline-evidence presence verified;
  no document traversal required to confirm all addresses resolve
  or that all TYPE-C rows carry confirming artifacts.
```

The suffix `(confirming artifact INLINE in all [Q] rows)` is required. A MANIFEST-COMPLETE token
whose TYPE-C count is stated as bare `[Q] TYPE-C RESOLVED` without the suffix fails C-59. The
suffix count [Q] must match the actual number of TYPE-C rows in the manifest table. A suffix
naming a different count fails.

_(CONSUMER-INDEX-COMPLETE and CHAIN-GROUNDING-COMPLETE formats identical to V-01.)_

---

#### MANIFEST-TOKEN-INLINE-EVIDENCE-SUFFIX [AXIS B -- C-59]

MANIFEST-COMPLETE is the terminal audit token for the citation layer. After this variation,
MANIFEST-COMPLETE is self-certifying with respect to two independent closure conditions:

1. **Citation accounting (C-52 via C-55):** Per-type ID ranges and counts confirm all citations
   are accounted for. A reviewer reading the token knows how many citations of each type are
   RESOLVED without consulting the manifest table.

2. **Inline-evidence presence (C-57 via C-59):** The TYPE-C count suffix
   `(confirming artifact INLINE in all [Q] rows)` confirms that all Q TYPE-C rows carry the
   confirming artifact in the STATUS CELL. A reviewer reading the token knows inline evidence is
   present for every TYPE-C citation without consulting the manifest rows.

**Verification contract:** A reviewer reading MANIFEST-COMPLETE in this artifact can verify
both conditions from token text alone. Consulting the manifest table is optional for confirmation,
not required for verification. The absence of the inline-evidence suffix in MANIFEST-COMPLETE
is detectable from the token text alone -- it is a falsifiable format requirement, not an
assertion.

**Placement:** This declaration appears at heading level in the Roles/Declarations section,
making it navigable without entering any step section. It supplements TOKEN CONTENT REQUIREMENT
without replacing it: MANIFEST-COMPLETE must satisfy both the base C-55 format and the C-59
extension.

---

_(Steps 0-7 identical to V-01, including all PHASE-HANDOVER tables and Step 7 dual-gate emission.
Step 8 manifest uses the extended MANIFEST-COMPLETE format declared above.)_

### Step 8 -- [IA] Citation-Completeness Manifest [C-52 + C-55 + C-57 + C-59 EXTENDED TOKEN]

_(Manifest protocol identical to V-01. TYPE-C rows carry confirming artifact in STATUS CELL.
MANIFEST-COMPLETE token carries C-59 suffix as declared in MANIFEST-TOKEN-INLINE-EVIDENCE-SUFFIX
and TOKEN CONTENT REQUIREMENT above.)_

`MANIFEST-COMPLETE: CIT-01..CIT-04 [4] TYPE-A RESOLVED, CIT-05..CIT-11 [7] TYPE-B RESOLVED, CIT-12..CIT-[N] [M] TYPE-C RESOLVED (confirming artifact INLINE in all [M] rows) -- citation-completeness and inline-evidence presence verified; no document traversal required to confirm all addresses resolve or that all TYPE-C rows carry confirming artifacts.`

== ARTIFACT STRUCTURE ============================================================

  1-22. Same as V-01 items 1-22
  Note: No GATE-TOKEN-REGISTRY -- Axis A absent
  Note: TOKEN CONTENT REQUIREMENT extends MANIFEST-COMPLETE format for C-59
  Note: MANIFEST-TOKEN-INLINE-EVIDENCE-SUFFIX declaration at heading level (Axis B)
  23. CONSUMER-INDEX-COMPLETE gate token (Step 7; independent; self-certifying) (C-53+C-55)
  24. CHAIN-GROUNDING-COMPLETE gate token (Step 7; independent; self-certifying) (C-54+C-55)
  25. CITATION-COMPLETENESS-MANIFEST (Step 8; MANIFEST-COMPLETE with C-59 suffix) (C-52+C-55+C-57+C-59)

Write to: simulations/topic/echo/{topic}-echo-{YYYY-MM-DD}.md

---

## V-03 -- Axis C: Cross-Layer Citation Consistency (C-60 targeted; C-58 C-59 absent)

**Variation axis:** Output format -- a Step 9 Cross-Layer Citation Consistency Check is added
after the CITATION-COMPLETENESS-MANIFEST. For each TYPE-C citation, the check compares the
Belief-Ref artifact (from STILL-LIVE FILTER) against the STATUS CELL artifact (from manifest).
CROSS-CITATION-CONSISTENT token emitted only when all rows MATCH. Axis C only; C-58 and C-59
not present.

**Hypothesis:** R18 V-05 populates Belief-Ref cells with the confirming artifact (C-54) and
manifest TYPE-C STATUS cells with the confirming artifact (C-57). For any given belief, both
cells reference the same physical evidence -- but they are produced at different steps by the
same role under different editorial pressures. No prior criterion requires them to be verified
as naming the same source. C-60 closes this gap. V-03 adds a dedicated Step 9 protocol that
enumerates each TYPE-C citation as a three-field row (Citation-ID, Belief-Ref-artifact,
Status-Cell-artifact) with a per-row MATCH/MISMATCH verdict. CROSS-CITATION-CONSISTENT is
emitted only when every row shows MATCH. A MISMATCH blocks token emission and halts artifact
production until resolved. C-58 and C-59 are absent; only the cross-layer consistency check
is targeted.

**Expected v19 score:** 340 (C-01 through C-57 all PASS as in R18 V-05; C-58: FAIL -- no
GATE-TOKEN-REGISTRY; C-59: FAIL -- MANIFEST-COMPLETE format unchanged; C-60: PASS -- Step 9
cross-layer check present and CROSS-CITATION-CONSISTENT emitted)

---

Topic: `{topic}`

_(Intro paragraph identical to V-01.)_

---

_(GATE-TOKEN-REGISTRY section ABSENT -- Axis A not present in V-03.)_

### Roles

_(EF and BC function declarations identical to V-01.)_

**Institutional Archaeologist (IA)** -- Steps 2-9.

```
INSTITUTIONAL ARCHAEOLOGIST -- FUNCTION DECLARATION
----------------------------------------------------------------------
Function:     False-assumption recovery. Correction register only.
              Each IA stage exit (Steps 2-6) produces a PHASE-
              HANDOVER-[N] table before advancing. At Step 7, emit
              CONSUMER-INDEX-COMPLETE and CHAIN-GROUNDING-COMPLETE
              as INDEPENDENT tokens per GATE-INDEPENDENCE-ENFORCED.
              At Step 8, produce the CITATION-COMPLETENESS-MANIFEST
              with self-certifying MANIFEST-COMPLETE; TYPE-C rows
              carry the confirming artifact in STATUS CELL per
              MANIFEST-ROW-INLINE-EVIDENCE. At Step 9, execute the
              CROSS-LAYER CITATION CONSISTENCY CHECK: compare each
              TYPE-C citation's Belief-Ref artifact against its
              STATUS CELL artifact. Emit CROSS-CITATION-CONSISTENT
              only when all rows MATCH. A MISMATCH blocks token
              emission and halts artifact production.
Input:        Signal artifacts + frozen PBI (read-only).
Out-of-scope: PBI authorship (frozen). Enforcement section (immutable).
Orienting:    "What would the next team build wrong?"
Phase scope:  Steps 2-9 only.
----------------------------------------------------------------------
```

_(Phase Handover Schema, TOKEN CONTENT REQUIREMENT, GATE-INDEPENDENCE-ENFORCED,
MANIFEST-ROW-INLINE-EVIDENCE, Phase Transition Registry, BC-STEP1-PROTOCOL,
BC-COVERAGE-RECORD Schema, and Steps 0-8 identical to V-01. TOKEN CONTENT REQUIREMENT
does NOT include the C-59 extension -- Axis B absent.)_

---

### Step 9 -- [IA] Cross-Layer Citation Consistency Check [AXIS C -- C-60]

After MANIFEST-COMPLETE is emitted at Step 8, execute the cross-layer citation consistency
check. This step is mandatory when TYPE-C citations exist. Its purpose is to verify that the
confirming artifact named in each Belief-Ref cell (STILL-LIVE FILTER, Step 3) is identical to
the confirming artifact named in the corresponding STATUS CELL (CITATION-COMPLETENESS-MANIFEST,
Step 8). The two references are produced independently at different steps; editorial divergence
is possible and undetected without this check.

```
CROSS-LAYER CITATION CONSISTENCY PROTOCOL (C-60)
----------------------------------------------------------------------
Scope:    All TYPE-C citations in the CITATION-COMPLETENESS-MANIFEST.
          TYPE-A and TYPE-B citations are not evaluated.
Source 1: STILL-LIVE FILTER -- Belief-Ref cell for each MUST-[N]
          row whose STILL-LIVE-[N] candidate corresponds to a
          TYPE-C citation.
Source 2: CITATION-COMPLETENESS-MANIFEST -- STATUS column for each
          TYPE-C row.
Check:    For each TYPE-C citation: extract artifact name from
          Belief-Ref cell; extract artifact name from STATUS cell.
          Compare exactly. Record MATCH or MISMATCH.
Token:    CROSS-CITATION-CONSISTENT -- emitted only when ALL rows
          show MATCH. MISMATCH on any row blocks token emission.
Gate:     MISMATCH IS A HARD GATE. Artifact production halts until
          the discrepancy is resolved: correct one or both cells
          to name the same artifact, then re-run the check.
----------------------------------------------------------------------
```

**Per-citation consistency table:**

| Citation-ID | Belief-Ref-artifact (STILL-LIVE FILTER) | Status-Cell-artifact (manifest STATUS) | Verdict |
|-------------|----------------------------------------|----------------------------------------|---------|
| CIT-[N] | [artifact name from Belief-Ref cell] | [artifact name from STATUS cell] | MATCH / MISMATCH |

If all rows show MATCH:

`CROSS-CITATION-CONSISTENT: [K] TYPE-C citations checked; Belief-Ref artifacts and STATUS CELL artifacts verified identical per pair; all [K] rows MATCH -- cross-layer citation consistency confirmed.`

If any row shows MISMATCH: do not emit CROSS-CITATION-CONSISTENT. Identify the discrepancy,
correct the source cell at the appropriate step, and re-run the check from that point.

**Note on token format:** The CROSS-CITATION-CONSISTENT token must name the count of citations
checked and assert per-pair identity. A token stating "all consistent" without naming the count
fails. A token emitted when any row is MISMATCH fails the hard gate condition.

== ARTIFACT STRUCTURE ============================================================

  1-22. Same as V-01 items 1-22
  Note: No GATE-TOKEN-REGISTRY -- Axis A absent
  Note: TOKEN CONTENT REQUIREMENT unchanged from R18 (C-55 only, no C-59 extension)
  Note: CROSS-LAYER CITATION CONSISTENCY PROTOCOL declaration in Step 9 (Axis C)
  23. CONSUMER-INDEX-COMPLETE gate token (Step 7; independent; self-certifying) (C-53+C-55)
  24. CHAIN-GROUNDING-COMPLETE gate token (Step 7; independent; self-certifying) (C-54+C-55)
  25. CITATION-COMPLETENESS-MANIFEST (Step 8; self-certifying MANIFEST-COMPLETE; TYPE-C STATUS CELL) (C-52+C-55+C-57)
  26. CROSS-CITATION-CONSISTENT token (Step 9; all TYPE-C pairs checked; all MATCH) (C-60)

Write to: simulations/topic/echo/{topic}-echo-{YYYY-MM-DD}.md

---

## V-04 -- Axes A+B: Registry Declared + Manifest Token Extended (C-58+C-59 targeted; C-60 absent)

**Variation axis:** GATE-TOKEN-REGISTRY before Step 0 (Axis A for C-58) combined with extended
MANIFEST-COMPLETE token format with C-57 suffix (Axis B for C-59). Both declarations active
simultaneously. No Step 9 cross-layer check -- C-60 not present.

**Hypothesis:** V-01 and V-02 each isolate one new structural property. V-04 tests whether Axis
A and Axis B are mutually reinforcing: the registry (C-58) declares MANIFEST-COMPLETE as GT-01
with its step location and prerequisite; the extended token format (C-59) makes GT-01's emitted
text self-certifying for inline-evidence presence as well as citation accounting. Together they
close the registry-to-token verification path: a reviewer diffs the registry to confirm GT-01
was emitted (C-58), then reads the token to confirm both C-52 and C-57 compliance (C-59). C-60
remains open -- the two confirming artifact references in Belief-Ref and STATUS cells are
individually verified (C-54, C-57) but not cross-verified for identity (C-60 requires a
post-manifest pairwise check).

**Expected v19 score:** 345 (C-01 through C-57 all PASS as in R18 V-05; C-58: PASS; C-59: PASS;
C-60: FAIL -- no Step 9 cross-layer check)

---

Topic: `{topic}`

_(Intro paragraph identical to V-01.)_

---

### GATE-TOKEN-REGISTRY [AXIS A -- C-58]

_(Identical to V-01 GATE-TOKEN-REGISTRY. GT-01 through GT-03 declared before Step 0.)_

| Token-ID | Canonical Name | Step | Prerequisite Criterion |
|----------|----------------|------|------------------------|
| GT-01 | MANIFEST-COMPLETE | Step 8 | C-52 (citation-completeness manifest exhaustive) |
| GT-02 | CONSUMER-INDEX-COMPLETE | Step 7 | C-53 (declaring-section consumer index populated) |
| GT-03 | CHAIN-GROUNDING-COMPLETE | Step 7 | C-54 (citation chain PBI grounding verified) |

Registry declared before Step 0. Diff this table against emitted tokens to verify completeness.

---

### Roles

_(EF and BC function declarations identical to V-01.)_

**Institutional Archaeologist (IA)** -- Steps 2-8.

```
INSTITUTIONAL ARCHAEOLOGIST -- FUNCTION DECLARATION
----------------------------------------------------------------------
Function:     False-assumption recovery. Correction register only.
              Each IA stage exit (Steps 2-6) produces a PHASE-
              HANDOVER-[N] table before advancing. At Step 7, emit
              CONSUMER-INDEX-COMPLETE (GT-02) and CHAIN-GROUNDING-
              COMPLETE (GT-03) as INDEPENDENT tokens per
              GATE-INDEPENDENCE-ENFORCED. At Step 8, produce the
              CITATION-COMPLETENESS-MANIFEST with MANIFEST-COMPLETE
              (GT-01) that is self-certifying for BOTH citation
              accounting (C-52) and inline-evidence presence (C-57)
              per the MANIFEST-TOKEN-INLINE-EVIDENCE-SUFFIX and TOKEN
              CONTENT REQUIREMENT declarations. TYPE-C STATUS CELL
              format per MANIFEST-ROW-INLINE-EVIDENCE.
Input:        Signal artifacts + frozen PBI (read-only).
Out-of-scope: PBI authorship (frozen). Enforcement section (immutable).
Orienting:    "What would the next team build wrong?"
Phase scope:  Steps 2-8 only.
----------------------------------------------------------------------
```

_(Phase Handover Schema, GATE-INDEPENDENCE-ENFORCED, MANIFEST-ROW-INLINE-EVIDENCE,
Phase Transition Registry, BC-STEP1-PROTOCOL, and BC-COVERAGE-RECORD Schema
identical to V-01.)_

---

#### TOKEN CONTENT REQUIREMENT [C-55 + C-59 MANIFEST-COMPLETE EXTENSION]

_(MANIFEST-COMPLETE format extended identical to V-02. CONSUMER-INDEX-COMPLETE and
CHAIN-GROUNDING-COMPLETE formats identical to V-01.)_

**Required format for MANIFEST-COMPLETE (GT-01) -- extended for C-59:**

```
MANIFEST-COMPLETE: CIT-[N1]..CIT-[N2] [K] TYPE-A RESOLVED,
  CIT-[M1]..CIT-[M2] [L] TYPE-B RESOLVED,
  CIT-[P1]..CIT-[P2] [Q] TYPE-C RESOLVED
    (confirming artifact INLINE in all [Q] rows) --
  citation-completeness and inline-evidence presence verified;
  no document traversal required.
```

---

#### MANIFEST-TOKEN-INLINE-EVIDENCE-SUFFIX [AXIS B -- C-59]

_(Identical to V-02 MANIFEST-TOKEN-INLINE-EVIDENCE-SUFFIX declaration. Self-certifying
contract extended to cover both C-52 and C-57 from token text alone.)_

---

_(Steps 0-8 identical to V-01 except Step 8 MANIFEST-COMPLETE token carries C-59 suffix.)_

### Step 8 -- [IA] Citation-Completeness Manifest [C-52 + C-55 + C-57 + C-59 EXTENDED]

_(Manifest protocol identical to V-01. Extended MANIFEST-COMPLETE token:)_

`MANIFEST-COMPLETE: CIT-01..CIT-04 [4] TYPE-A RESOLVED, CIT-05..CIT-11 [7] TYPE-B RESOLVED, CIT-12..CIT-[N] [M] TYPE-C RESOLVED (confirming artifact INLINE in all [M] rows) -- citation-completeness and inline-evidence presence verified; no document traversal required.`

== ARTIFACT STRUCTURE ============================================================

  1-22. Same as V-01 items 1-22
  Note: GATE-TOKEN-REGISTRY listing GT-01..GT-03 before Step 0 (Axis A, C-58)
  Note: TOKEN CONTENT REQUIREMENT extends MANIFEST-COMPLETE format (Axis B, C-59)
  Note: MANIFEST-TOKEN-INLINE-EVIDENCE-SUFFIX declaration at heading level (Axis B)
  23. CONSUMER-INDEX-COMPLETE gate token (Step 7; GT-02; independent; self-certifying) (C-53+C-55)
  24. CHAIN-GROUNDING-COMPLETE gate token (Step 7; GT-03; independent; self-certifying) (C-54+C-55)
  25. CITATION-COMPLETENESS-MANIFEST (Step 8; GT-01; extended MANIFEST-COMPLETE with C-59 suffix) (C-52+C-55+C-57+C-59)
  Note: C-60 FAILS -- no Step 9 cross-layer check

Write to: simulations/topic/echo/{topic}-echo-{YYYY-MM-DD}.md

---

## V-05 -- Axes A+B+C: Full R19 Closure Layer (C-58+C-59+C-60 all targeted)

**Variation axis:** Full integration -- GATE-TOKEN-REGISTRY before Step 0 (Axis A for C-58),
MANIFEST-COMPLETE extended with C-57 suffix (Axis B for C-59), and Step 9 Cross-Layer Citation
Consistency Check (Axis C for C-60) all active simultaneously. GT-04 added to registry for
CROSS-CITATION-CONSISTENT. All R18 V-05 properties preserved: TOKEN CONTENT REQUIREMENT,
GATE-INDEPENDENCE-ENFORCED, MANIFEST-ROW-INLINE-EVIDENCE, extended Belief-Ref cells, Consumer-Ref
columns, F-BCR-4 specific PBI naming.

**Hypothesis:** V-01, V-02, V-03 each isolate one new structural property. V-04 demonstrated
registry-to-token path closure (C-58+C-59 corroborate: the registry declares GT-01 and the
extended token proves GT-01's full content). V-05 asks whether all three simultaneously produce
a closed R19 closure-layer audit:
(1) Token completeness is diff-detectable: the registry lists all gate tokens; any missing token
is identified by registry-vs-emitted diff, not artifact scan. (C-58)
(2) MANIFEST-COMPLETE self-certifies both citation accounting and inline-evidence presence: a
reviewer reading the token knows Q TYPE-C citations are RESOLVED and all Q rows carry inline
evidence -- without consulting the manifest table. (C-59)
(3) The two confirming artifact references are cross-verified: Belief-Ref cell and STATUS CELL
for each TYPE-C citation name the same physical evidence; CROSS-CITATION-CONSISTENT documents
each pair and fails hard on any discrepancy. (C-60)

The three properties form a coherent R19 closure-layer contract: token set auditable by registry
(C-58), terminal manifest token self-certifying for the full closure layer (C-59), cross-layer
evidence references verified per pair (C-60).

**Expected v19 score:** 350 (all 60 criteria: PASS; maximum achievable under v19)

---

Topic: `{topic}`

Synthesize what was unexpected. Three roles at three exclusive phase boundaries. Every structural
commitment is named, formal, and auditable from output. This is not a summary. This is not a list
of findings. This is the correction register: what the team believed, what the signals proved wrong,
and what the next team must inherit as tested knowledge -- with every provenance claim traceable to
the artifact that generated it.

---

### GATE-TOKEN-REGISTRY [AXIS A -- C-58]

Expected gate tokens for this artifact. Token absence is detectable by diff against this registry
without full-artifact traversal. A listed token absent from the artifact is missing. A token not
listed here should not appear as a gate token.

| Token-ID | Canonical Name | Step | Prerequisite Criterion |
|----------|----------------|------|------------------------|
| GT-01 | MANIFEST-COMPLETE | Step 8 | C-52 (citation-completeness manifest exhaustive) |
| GT-02 | CONSUMER-INDEX-COMPLETE | Step 7 | C-53 (declaring-section consumer index populated) |
| GT-03 | CHAIN-GROUNDING-COMPLETE | Step 7 | C-54 (citation chain PBI grounding verified) |
| GT-04 | CROSS-CITATION-CONSISTENT | Step 9 | C-60 (cross-layer citation consistency verified) |

Registry declared before Step 0. Diff GT-01..GT-04 against emitted tokens to verify completeness.

---

### Roles

**Enforcement Framer (EF)** -- Step 0 exclusively.
_(Function declaration identical to V-01.)_

**Belief Cartographer (BC)** -- Step 1 exclusively.
_(Function declaration identical to V-01.)_

**Institutional Archaeologist (IA)** -- Steps 2-9.

```
INSTITUTIONAL ARCHAEOLOGIST -- FUNCTION DECLARATION
----------------------------------------------------------------------
Function:     False-assumption recovery. Correction register only.
              Each IA stage exit (Steps 2-6) produces a PHASE-
              HANDOVER-[N] table before advancing. At Step 7, emit
              CONSUMER-INDEX-COMPLETE (GT-02) and CHAIN-GROUNDING-
              COMPLETE (GT-03) as INDEPENDENT tokens per
              GATE-INDEPENDENCE-ENFORCED -- combined tokens at this
              boundary are non-conforming. Each token self-certifying
              per TOKEN CONTENT REQUIREMENT. At Step 8, produce the
              CITATION-COMPLETENESS-MANIFEST; MANIFEST-COMPLETE (GT-01)
              carries the C-59 inline-evidence suffix -- self-certifying
              for both citation accounting and inline-evidence presence;
              TYPE-C STATUS CELL carries confirming artifact per
              MANIFEST-ROW-INLINE-EVIDENCE. At Step 9, execute the
              Cross-Layer Citation Consistency Check: compare each
              TYPE-C Belief-Ref artifact against its STATUS CELL
              artifact per pair; emit CROSS-CITATION-CONSISTENT (GT-04)
              only when all rows MATCH. Four gate tokens required (see
              GATE-TOKEN-REGISTRY); any absent or non-conforming token
              is an incompletion.
Input:        Signal artifacts + frozen PBI (read-only).
Out-of-scope: PBI authorship (frozen). Enforcement section (immutable).
Orienting:    "What would the next team build wrong?"
Phase scope:  Steps 2-9 only.
----------------------------------------------------------------------
```

**Phase Handover Schema (universal -- all 7 exits, Steps 0-6):**
_(Identical to V-01: six rows, fixed field names, Registry-Ref row cites T-ID.)_

---

#### TOKEN CONTENT REQUIREMENT [C-55 + C-59 EXTENDED MANIFEST-COMPLETE]

Every gate token emitted in this artifact must carry inline specifics sufficient to verify its
pass condition without consulting the underlying artifact sections. This requirement applies to
all four gate tokens declared in the GATE-TOKEN-REGISTRY.

**Required format for MANIFEST-COMPLETE (GT-01) -- extended for C-59:**

```
MANIFEST-COMPLETE: CIT-[N1]..CIT-[N2] [K] TYPE-A RESOLVED,
  CIT-[M1]..CIT-[M2] [L] TYPE-B RESOLVED,
  CIT-[P1]..CIT-[P2] [Q] TYPE-C RESOLVED
    (confirming artifact INLINE in all [Q] rows) --
  citation-completeness and inline-evidence presence verified;
  no document traversal required to confirm all addresses resolve
  or that all TYPE-C rows carry confirming artifacts.
```

A token whose TYPE-C count omits the inline-evidence suffix fails C-59. The suffix count [Q]
must match the actual TYPE-C row count in the manifest table.

**Required format for CONSUMER-INDEX-COMPLETE (GT-02):**
_(Identical to V-01: three tables named individually with ID ranges.)_

**Required format for CHAIN-GROUNDING-COMPLETE (GT-03):**
_(Identical to V-01: both condition labels present.)_

**Required format for CROSS-CITATION-CONSISTENT (GT-04):**

```
CROSS-CITATION-CONSISTENT: [K] TYPE-C citations checked;
  Belief-Ref artifacts and STATUS CELL artifacts verified identical
  per pair; all [K] rows MATCH -- cross-layer citation consistency
  confirmed.
```

The token must name the count checked and assert per-pair identity. A token stating
"all consistent" without naming the count fails. A token emitted when any row is MISMATCH
fails the hard gate condition.

---

#### GATE-INDEPENDENCE-ENFORCED [C-56]

_(Identical to V-01. Combined tokens non-conforming at co-located gate boundaries. Step 7
application: GT-02 and GT-03 must be separate independent tokens.)_

---

#### MANIFEST-TOKEN-INLINE-EVIDENCE-SUFFIX [AXIS B -- C-59]

_(Identical to V-02. MANIFEST-COMPLETE self-certifies both citation accounting (C-52) and
inline-evidence presence (C-57) from token text alone. Placed at heading level, navigable
without entering any step section. Supplements TOKEN CONTENT REQUIREMENT.)_

---

#### MANIFEST-ROW-INLINE-EVIDENCE [C-57]

_(Identical to V-01. TYPE-C STATUS CELL carries confirming artifact. Bare RESOLVED fails.)_

---

#### Phase Transition Registry [C-50 -- Consumer-Ref column]

_(Identical to V-01: T-00 through T-06 with Consumer-Ref column.)_

---

### BC-STEP1-PROTOCOL

_(Identical to V-01: three sub-phases [SCAN], [FREEZE], [COVERAGE AUDIT].)_

#### BC-COVERAGE-RECORD Schema [C-46/C-49 -- field-IDs + Consumer-Ref; F-BCR-4 specific format]

_(Identical to V-01: F-BCR-1 through F-BCR-4 with Consumer-Ref column. F-BCR-4 names specific
PBI entries by ID range and source material -- generic sentence fails C-54 condition 2.)_

---

### Steps 0-6

_(Identical to V-01. All PHASE-HANDOVER tables carry Registry-Ref rows with T-ID citations.)_

### Step 3 Extension -- STILL-LIVE FILTER [C-51 extended Belief-Ref + C-53 Consumer-Ref]

_(Identical to V-01. MUST-ID + Scope + Action + Constraint + extended Belief-Ref
[`PB-[NN] (confirmed false by: [artifact name, namespace, date])`] + Consumer-Ref columns.)_

---

### Step 7 -- [IA] Hierarchy, Distillation, and Dual-Gate Emission [C-53+C-54+C-55+C-56]

_(Hierarchy, distillation content, and closing elements identical to V-01.)_

**After artifact content is complete, emit both Step 7 completeness gates as INDEPENDENT
self-certifying tokens per GATE-INDEPENDENCE-ENFORCED and TOKEN CONTENT REQUIREMENT:**

Gate 1 (C-53) -- CONSUMER-INDEX-COMPLETE (GT-02):

`CONSUMER-INDEX-COMPLETE: BC-COVERAGE-RECORD Schema F-BCR-1..F-BCR-4 Consumer-Ref POPULATED, Phase Transition Registry T-00..T-06 Consumer-Ref POPULATED, STILL-LIVE FILTER MUST-1..MUST-4 Consumer-Ref POPULATED -- bidirectional navigability confirmed across all three axes.`

Gate 2 (C-54) -- CHAIN-GROUNDING-COMPLETE (GT-03):

`CHAIN-GROUNDING-COMPLETE: Belief-Ref cells EXTENDED (all MUST-[N] carry confirming artifact reference), F-BCR-4 SPECIFIC (names PB-[NN] through PB-[NN]) -- citation chain verified to evidence; both C-54 conditions confirmed.`

These two tokens are at the same step boundary. Per GATE-INDEPENDENCE-ENFORCED, they are
emitted as separate tokens. A combined token is non-conforming.

---

### Step 8 -- [IA] Citation-Completeness Manifest [C-52+C-55+C-57+C-59]

Produce CITATION-COMPLETENESS-MANIFEST. Apply all active declarations:
- TOKEN CONTENT REQUIREMENT + MANIFEST-TOKEN-INLINE-EVIDENCE-SUFFIX: MANIFEST-COMPLETE (GT-01)
  carries C-59 inline-evidence suffix.
- MANIFEST-ROW-INLINE-EVIDENCE: TYPE-C STATUS cells carry confirming artifact.

```
CITATION-COMPLETENESS-MANIFEST PROTOCOL (C-52+C-55+C-57+C-59)
----------------------------------------------------------------------
TYPE-A rows:  RESOLVED (bare) -- schema field-ID citation.
TYPE-B rows:  RESOLVED (bare) -- registry T-ID citation.
TYPE-C rows:  RESOLVED (confirmed false by: [artifact name,
              namespace, date]) -- STATUS CELL carries confirming
              artifact. Bare RESOLVED fails. Confirming artifact
              in Target Address only fails.
Gate:         Any DANGLING citation halts finalization.
Token:        MANIFEST-COMPLETE (GT-01) carries C-59 suffix:
              [Q] TYPE-C RESOLVED (confirming artifact INLINE
              in all [Q] rows).
----------------------------------------------------------------------
```

_(Manifest table structure identical to V-01.)_

Self-certifying extended closure token:

`MANIFEST-COMPLETE: CIT-01..CIT-04 [4] TYPE-A RESOLVED, CIT-05..CIT-11 [7] TYPE-B RESOLVED, CIT-12..CIT-[N] [M] TYPE-C RESOLVED (confirming artifact INLINE in all [M] rows) -- citation-completeness and inline-evidence presence verified; no document traversal required to confirm all addresses resolve or that all TYPE-C rows carry confirming artifacts.`

---

### Step 9 -- [IA] Cross-Layer Citation Consistency Check [AXIS C -- C-60]

After MANIFEST-COMPLETE is emitted, execute the cross-layer citation consistency check before
declaring the artifact complete. This step closes the gap between C-54 (Belief-Ref layer) and
C-57 (STATUS CELL layer): both cells reference the same physical evidence for the same belief,
but are produced at different steps and may diverge through editorial error.

```
CROSS-LAYER CITATION CONSISTENCY PROTOCOL (C-60)
----------------------------------------------------------------------
Scope:    All TYPE-C citations in the CITATION-COMPLETENESS-MANIFEST.
          TYPE-A and TYPE-B citations not evaluated.
Source 1: STILL-LIVE FILTER Belief-Ref cell for each TYPE-C
          citation's corresponding MUST-[N] row.
Source 2: CITATION-COMPLETENESS-MANIFEST STATUS column for each
          TYPE-C row.
Check:    Extract artifact name from each Belief-Ref cell.
          Extract artifact name from corresponding STATUS cell.
          Compare exactly. Record MATCH or MISMATCH per pair.
Token:    CROSS-CITATION-CONSISTENT (GT-04) -- emitted only when
          ALL rows show MATCH.
Gate:     MISMATCH IS A HARD GATE. Artifact production halts.
          Correct the discrepancy (identify which cell names the
          wrong artifact; re-populate; re-run from Step 9).
----------------------------------------------------------------------
```

**Per-citation consistency table:**

| Citation-ID | Belief-Ref-artifact (STILL-LIVE FILTER) | Status-Cell-artifact (manifest STATUS) | Verdict |
|-------------|----------------------------------------|----------------------------------------|---------|
| CIT-[N] | [artifact name from Belief-Ref cell] | [artifact name from STATUS cell] | MATCH |

If all rows show MATCH, emit CROSS-CITATION-CONSISTENT (GT-04):

`CROSS-CITATION-CONSISTENT: [K] TYPE-C citations checked; Belief-Ref artifacts and STATUS CELL artifacts verified identical per pair; all [K] rows MATCH -- cross-layer citation consistency confirmed.`

If any row shows MISMATCH: do not emit GT-04. Halt artifact production. Identify the discrepancy,
correct the source cell, and re-run the cross-layer check.

**Verification note:** A reviewer can verify CROSS-CITATION-CONSISTENT from the per-citation
table alone: the table enumerates each pair with both artifact names and the MATCH verdict.
No consultation of the STILL-LIVE FILTER or manifest table is required beyond the table rows
in this step.

== ARTIFACT STRUCTURE ============================================================

  1. ENFORCEMENT MECHANISM DECLARATION (EF; NO-ECHO COST named; C-26)
  2. EF-INVOCATION-RECORD (Step 0; C-33)
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
  23. CONSUMER-INDEX-COMPLETE (Step 7; GT-02; independent; self-certifying) (C-53+C-55)
  24. CHAIN-GROUNDING-COMPLETE (Step 7; GT-03; independent; self-certifying) (C-54+C-55)
      Note: Gates 23 and 24 independent per GATE-INDEPENDENCE-ENFORCED (C-56)
  25. CITATION-COMPLETENESS-MANIFEST with extended MANIFEST-COMPLETE (Step 8; GT-01;
      C-59 inline-evidence suffix; TYPE-C STATUS CELL carries confirming artifact)
      (C-52+C-55+C-57+C-59)
  26. CROSS-CITATION-CONSISTENT per-citation table + token (Step 9; GT-04; all pairs MATCH)
      (C-60)
  Note: GATE-TOKEN-REGISTRY lists GT-01..GT-04 before Step 0 [AXIS A C-58]
        Items 23-26 diff against GT-01..GT-04 for completeness verification

Write to: simulations/topic/echo/{topic}-echo-{YYYY-MM-DD}.md

---

## Variation Summary

| # | Axis | New R19 Declarations | C-58 | C-59 | C-60 | v19 score |
|---|------|---------------------|:----:|:----:|:----:|:---------:|
| V-01 | A only | GATE-TOKEN-REGISTRY | PASS | FAIL | FAIL | 340 |
| V-02 | B only | MANIFEST-TOKEN-INLINE-EVIDENCE-SUFFIX | FAIL | PASS | FAIL | 340 |
| V-03 | C only | CROSS-LAYER CITATION CONSISTENCY PROTOCOL (Step 9) | FAIL | FAIL | PASS | 340 |
| V-04 | A+B | GATE-TOKEN-REGISTRY + MANIFEST-TOKEN-INLINE-EVIDENCE-SUFFIX | PASS | PASS | FAIL | 345 |
| **V-05** | **A+B+C** | **All three + GT-04 in registry** | **PASS** | **PASS** | **PASS** | **350** |

**R19 structural contribution beyond R18:**

Each new criterion gets its own named heading-level declaration operating on the token/registry
layer established by R17 and extended by R18:

- **C-58: GATE-TOKEN-REGISTRY** -- converts token completeness from scan-dependent to
  diff-detectable. Parallels C-44 (phase transition inventory) and C-52 (citation manifest):
  all three apply the traversal-free completeness contract to their respective structural layer.
  Registry applies it to the token layer itself.

- **C-59: MANIFEST-TOKEN-INLINE-EVIDENCE-SUFFIX** -- extends MANIFEST-COMPLETE's
  self-certification scope from citation accounting (C-52) to include inline-evidence
  completeness (C-57). The terminal manifest token now proves the full closure-layer state it
  claims to close. Without this extension, MANIFEST-COMPLETE is self-certifying for C-52 only;
  a reviewer wanting C-57 confirmation still needs to consult the manifest table.

- **C-60: CROSS-LAYER CITATION CONSISTENCY PROTOCOL** -- applies the traversal-free,
  token-certified audit contract to the cross-layer dimension. C-54 and C-57 each verify one
  reference direction; C-60 verifies both references name the same source. The per-citation
  table in Step 9 is the audit record; CROSS-CITATION-CONSISTENT is its closure token. A
  discrepancy at any pair fails the gate without requiring section traversal to identify the
  mismatch.

The three declarations form a coherent R19 closure-layer contract: token set auditable by
registry (GATE-TOKEN-REGISTRY), terminal manifest token self-certifying for the full closure
layer (MANIFEST-TOKEN-INLINE-EVIDENCE-SUFFIX), cross-layer evidence references verified per
pair (CROSS-LAYER CITATION CONSISTENCY PROTOCOL).

Gate chain: R10 output auditable -> R11 output non-defeatable -> R12 enforcement legible ->
R13 structure navigable -> R14 element addressable -> R15 address citation-activated ->
R16 citation exhaustively manifested, bidirectionally indexed, and chain-grounded ->
R17 tokens self-certifying, gates independent, manifest rows inline-evidenced ->
R18 token inventory declared, manifest token extended for inline-evidence,
cross-layer citation consistent.
