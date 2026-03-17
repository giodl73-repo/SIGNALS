# listen-support Round 14 -- Skill Body Prompt Variations

**Date:** 2026-03-15
**Rubric target:** v14 (40 criteria -- C-01 through C-40)
**Base:** V-05 R13 (C-01 through C-37 ceiling; checkpoint map + per-criterion sub-blocks +
cross-criterion synergy declaration all active)

**Variation axes selected** (3 single-axis, then 2 combined):

1. **Two-Layer Synergy Declaration (C-38 candidate)** -- The CROSS-CRITERION SYNERGY NOTE
   in the preamble and the CROSS-CRITERION SYNERGY DECLARATION in Step 11 are each
   explicitly labeled as LAYER 1 of 2 and LAYER 2 of 2. Step 11 gains a
   two-layer-presence check: "LAYER 1 in preamble: YES/NO | LAYER 2 in Step 11: YES/NO".
   A scorer can confirm both layers are present without reading every section. (V-01)

2. **Grep-Closed Declaration-to-Trace Loop (C-39 candidate)** -- A unique grep anchor
   token `[SYNERGY-ANCHOR: C33xC34]` is embedded in both the preamble SYNERGY NOTE and
   the Step 11 SYNERGY DECLARATION. The preamble note explicitly states that a single
   grep for `SYNERGY-ANCHOR` finds both the declaration site and the echo site. Step 11
   adds a grep-closed verification line: "grep for SYNERGY-ANCHOR finds preamble +
   Step 11: YES/NO". (V-02)

3. **Falsifiable Degradation Clause (C-40 candidate)** -- The CROSS-CRITERION SYNERGY
   NOTE (preamble) and CROSS-CRITERION SYNERGY DECLARATION (Step 11) each gain an
   explicit DEGRADATION CLAUSE sub-section stating the synergy as an if/then conditional:
   "IF C-33 bracket-token is absent from a checkpoint header, THEN that checkpoint
   requires prose interpretation, AND C-34's no-traversal property degrades to
   aspirational." The failure condition is named and the clause is marked falsifiable. (V-03)

4. **V-01 + V-02 combined** -- Two-layer labeling + grep-closed anchor. Independent
   mechanisms: LAYER labeling addresses presence verification; grep anchor addresses
   locatability. (V-04)

5. **Full synthesis** -- All three axes: two-layer labeling + grep-closed anchor +
   falsifiable degradation clause. (V-05)

**Axes NOT explored this round (deferred):**
- Role sequence (SRE-first enforced by gate from R12; stable)
- Output format (ticket table format stable)
- Phrasing register (stable from R10)
- Checkpoint-mapped VALIDATION TRACE (C-36 active baseline; not varied)
- Per-criterion sub-blocks (C-37 active baseline; not varied)

**R14 criterion hypothesis matrix:**

| Criterion candidate | V-01 | V-02 | V-03 | V-04 | V-05 |
|--------------------|------|------|------|------|------|
| C-01 through C-37 (all prior -- active baseline) | YES | YES | YES | YES | YES |
| C-38: Two-Layer Synergy Declaration | YES | -- | -- | YES | YES |
| C-39: Grep-Closed Declaration-to-Trace Loop | -- | YES | -- | YES | YES |
| C-40: Falsifiable Degradation Clause | -- | -- | YES | -- | YES |

**Axes carried from R13 V-05 (active in all R14 variations as baseline):**
- INERTIA COMPETITOR preamble with bracket-variable token declaration (C-31 / C-33)
- PROPAGATION CHAIN sub-block with A/B/C labels pre-declared in preamble (C-34)
- SRE-WRITE-FIRST GATE block at Step 5c -> Step 7 boundary (C-35)
- CHECKPOINT MAP sub-section in VALIDATION TRACE with per-label YES/NO (C-36)
- Per-criterion sub-blocks (C-33 / C-34 / C-35) with scan-verifiability line (C-37)
- CROSS-CRITERION SYNERGY DECLARATION in Step 11 (C-37 satisfied)
- CROSS-CRITERION SYNERGY NOTE in preamble (C-37 satisfied)
- SRE-first ordering in STATUS QUO and PERSONA VOICE TABLE (C-32)
- PHASE NARRATIVE behavioral driver block (R10 V-03)
- TIER-SEQUENCING RULE as preamble before verification block (R9 V-01)
- Per-category minimum instruction with arithmetic rationale in Step 5b (R9 V-02)
- TIER ARCHITECTURE SELF-CHECK as scannable table (R9 V-03)
- Floor guarantee computation row in REGISTRY COMPLETENESS CHECK (R8 V-02)
- Named tier headers TIER 1 / TIER 2 (R7 V-03)
- Per-category minimums >= 2 (R7 V-01)
- Total-count floor row naming C-21 floor (R7 V-02)
- Phase-severity gradient prior (R1)
- STATUS QUO anchor / inertia map (R2)
- Assumption audit 6-column chain with Ticket # pending (R2/R3)
- Phase distribution target with phase-labeled constraints (R1)
- Persona voice table as dimension registry (R2)
- Pre-generation VALIDATION TRACE (R2)
- FORWARD-LINK GATE (R3)
- Ticket bodies with "Traces to:" field + comparison framing (R3)
- Per-pair content alignment evidence with inline Gate: PROCEED|REVISE (R6 V-01)
- Block-level REVISION GATE sub-block with OPEN|CLOSED (R6 V-02)
- Dual-category rejection registry (R6 V-03)
- MARKER FORMAT AUDIT
- Post-generation phase confirmation
- Gap analysis classification table (PARITY / NET-NEW)
- THRESHOLD CONFIRMATION block

---

## V-01: Single-Axis -- Two-Layer Synergy Declaration (C-38)

**Axis:** The synergy between C-33 and C-34 must be declared in exactly two locations:
LAYER 1 in the preamble (CROSS-CRITERION SYNERGY NOTE) and LAYER 2 in Step 11
(CROSS-CRITERION SYNERGY DECLARATION). Each location is explicitly labeled with its
layer number. The Step 11 block gains a two-layer-presence check that names both layers
and their locations: a scorer can confirm two-layer compliance by scanning for
"LAYER 1" and "LAYER 2" without reading every section.

**Probe (C-38 candidate):** R13 V-05 placed a SYNERGY NOTE in the preamble and a
SYNERGY DECLARATION in Step 11, but neither was labeled as a "layer." A scorer
verifying synergy coverage must read both sections to confirm both exist. The two-layer
label makes the architectural intent explicit: the synergy is not a single-site claim
but a claim that must be present in two structurally distinct locations. C-38 would
require: (a) preamble note labeled LAYER 1 of 2, (b) Step 11 block labeled LAYER 2
of 2, (c) a two-layer-presence check in Step 11 with YES/NO for each layer.

**Hypothesis:** When both layers are labeled and the Step 11 block contains an explicit
two-layer-presence check, a scorer can answer "is the synergy declaration present in
both required locations?" by scanning for the layer labels rather than reading content.
C-38 would require both layer labels present and the two-layer-presence check to show
YES for both.

---

```
# listen-support: Predict First-90-Day Support Tickets

Work through each step in order. Do not skip steps. Do not combine steps.

---

INERTIA COMPETITOR: [name the specific product the target personas currently use for
this workflow -- one product name, grep-checkable, no generic labels like "legacy tool"
or "the incumbent"]

This name is a constant. It appears below as the literal bracket-variable token
[INERTIA COMPETITOR] embedded in table column headers and step instruction action
clauses. Every occurrence is detectable by scanning for [INERTIA COMPETITOR].

PROPAGATION CHAIN:
  Checkpoint A: STATUS QUO ANCHOR (Step 2) -- column header "Prior [INERTIA COMPETITOR]
    behavior" uses the bracket-token; column 2 cells name this product explicitly
  Checkpoint B: ASSUMPTION AUDIT (Step 3) -- column header "Incumbent [INERTIA COMPETITOR]
    behavior" uses the bracket-token; column 2 cells cite this product by name
  Checkpoint C: Ticket bodies with [A#N] traces (Step 7) -- bodies linked to assumption
    audit rows contain this product name verbatim; coverage >= 50% of linked bodies

Completeness is verifiable from this declaration: (A) grep Step 2 header, (B) grep
Step 3 header, (C) count bodies. All three must be satisfied before submitting.

CROSS-CRITERION SYNERGY NOTE (LAYER 1 of 2):
  C-33 bracket-tokens at Checkpoint A (Step 2 header) and Checkpoint B (Step 3 header)
  make C-34's declared checkpoints grep-detectable. This is what makes C-34's
  "completeness verifiable without traversal" property structural rather than
  aspirational. If C-33 tokens are absent from a checkpoint header, that checkpoint
  requires prose interpretation and C-34's no-traversal property degrades to
  aspirational for that checkpoint. The CROSS-CRITERION SYNERGY DECLARATION (LAYER 2
  of 2) in Step 11 confirms this dependency is satisfied. Two-layer synergy: this note
  is LAYER 1; the Step 11 declaration is LAYER 2. Both must be present.

---

## STEP 1 -- PHASE-SEVERITY GRADIENT PRIOR

Phase 1 (Day 0-30): P2/P3. P0 reserved for activation blockers affecting all users.
Phase 2 (Day 31-60): P1/P2. P0 exceptional: data loss or workflow corruption only.
Phase 3 (Day 61-90): P0/P1. No fallback at scale. P3 essentially absent.

PHASE-SEVERITY PRIOR:
  Phase 1 (Day 0-30):  typical P2/P3; P0 only for activation blockers affecting all users
  Phase 2 (Day 31-60): typical P1/P2; P0 exceptional (data loss or workflow corruption)
  Phase 3 (Day 61-90): typical P0/P1; P3 rare (users have exhausted workarounds)

---

## STEP 1b -- PHASE NARRATIVE

**Phase 1 (Day 0-30) -- First contact:**
Users explore the feature while keeping [INERTIA COMPETITOR] active as a safety net.
Each step is compared against [INERTIA COMPETITOR] behavior. Trigger event: first
contact with a divergence from [INERTIA COMPETITOR] -- setup friction, missing docs,
onboarding gaps. Tickets: high volume, low severity (prior tool fallback available).

**Phase 2 (Day 31-60) -- Committed trial:**
Users have invested real workflows; some migrated, some still in [INERTIA COMPETITOR].
Trigger event: committed workflow hits a blocking gap that works in [INERTIA COMPETITOR]
but fails here. Partial-migration friction: no simple revert, feature coverage incomplete.

**Phase 3 (Day 61-90) -- Operational dependency:**
[INERTIA COMPETITOR] is no longer available for this workflow. Trigger event: blocking
failure under production conditions. Severity escalates -- no fallback exists.

PHASE NARRATIVE COMPLETE:
  Phase 1 behavioral driver named ([INERTIA COMPETITOR] referenced): YES / NO
  Phase 2 behavioral driver named ([INERTIA COMPETITOR] referenced): YES / NO
  Phase 3 behavioral driver named ([INERTIA COMPETITOR] referenced): YES / NO
  Trigger events named for all three phases:                         YES / NO

---

## STEP 2 -- STATUS QUO ANCHOR

SRE row is listed first. Column 2 uses the INERTIA COMPETITOR name from the preamble.
The bracket-token [INERTIA COMPETITOR] in the column header is Checkpoint A of the
PROPAGATION CHAIN.

Column 2 instruction: for each row, name the specific behavior of [INERTIA COMPETITOR]
that taught this persona class to expect X. The bracket-token [INERTIA COMPETITOR] in
the column header anchors this instruction -- cell values must use the declared name.

| Persona class | Prior [INERTIA COMPETITOR] behavior | Key capability expected to carry over | Most likely violated assumption |
|---------------|-------------------------------------|--------------------------------------|----------------------------------|
| SRE | | | |
| Support | | | |
| PM / UX | | | |
| C-01..C-04 (technical early adopters) | | | |
| C-05..C-08 (pragmatic mainstream) | | | |
| C-09..C-12 (enterprise/compliance) | | | |

Column 4 (violated assumption) feeds Step 3.

---

## STEP 3 -- ASSUMPTION AUDIT

**Complete the SRE row first.** SRE tickets determine the severity ceiling.

Column 2 (Incumbent [INERTIA COMPETITOR] behavior): state the specific behavior of
[INERTIA COMPETITOR] that created the expectation. The bracket-token
[INERTIA COMPETITOR] in the column header is Checkpoint B of the PROPAGATION CHAIN.
Cell values must use the declared name -- no generic substitution.

| # | Persona class | Incumbent [INERTIA COMPETITOR] behavior | Imported expectation | What this feature does instead | Resulting failure mode | Ticket # |
|---|---------------|----------------------------------------|---------------------|-------------------------------|----------------------|----------|

Ticket #: LEAVE BLANK -- assigned in Step 6b. Complete at least 1 row.

ASSUMPTION AUDIT COMPLETE:
  Rows documented:                                         [N]
  SRE row present:                                         YES / NO
  All 5 non-ID columns populated:                          YES / NO
  Column 2 cells reference [INERTIA COMPETITOR] by name:   YES / NO -> Checkpoint B
  Ticket IDs pending at Step 6b:                           [N] rows

---

## STEP 4 -- PHASE DISTRIBUTION TARGET

Declare the binding target consistent with the Phase Narrative from Step 1b.

PHASE DISTRIBUTION TARGET:
  Phase 1 (Day 0-30):  [N] tickets   -- first contact, [INERTIA COMPETITOR] comparison
  Phase 2 (Day 31-60): [N] tickets   -- committed trial, migration edge cases
  Phase 3 (Day 61-90): [N] tickets   -- operational dependency, no fallback
  Total:               [N] tickets

Constraints: Phase 1 >= 3. Phase 3 >= 1. Total >= 7. All three phases non-zero.

---

## STEP 5 -- PERSONA VOICE TABLE (DIMENSION REGISTRY)

SRE row is listed first. The order mirrors Step 2. The SRE-WRITE-FIRST GATE in Step 5c
verifies this position before body writing begins.

| Persona | Operational vocabulary | Frustration register | Framing conventions |
|---------|----------------------|---------------------|---------------------|
| SRE | (>= 2 specific terms) | (>= 2 specific phrases) | (>= 2 structural patterns) |
| Support | (>= 2 specific terms) | (>= 2 specific phrases) | (>= 2 structural patterns) |
| [other personas used] | (>= 2 specific terms) | (>= 2 specific phrases) | (>= 2 structural patterns) |

Dimension prefixes: operational= | frustration= | framing=

What disqualifies: role declarations ("As an SRE"), generic verbs ("noticed", "tried"),
bare nouns ("logs", "data", "error").

---

## STEP 5b -- DIMENSION-LABEL REJECTION REGISTRY

**Per-category minimum commitment:**
  Category 1 (Format violations) minimum: 2 entries
  Category 2 (Value violations) minimum:  2 entries

Floor guarantee: 2 + 2 = 4 > 3.

REJECTION REGISTRY:

Category 1: R-01 (flat list), R-02 (same prefix twice), R-03 (count without naming)
Category 2: R-04 (role declarations), R-05 (generic verbs), R-06 (synonym pairs),
            R-07 (bare nouns)

REGISTRY COMPLETENESS CHECK:
  Category 1: [N] (>= 2) | Category 2: [N] (>= 2) | Total: [N] (>= 3) -> PASS / FAIL
  Floor guarantee: [N] + [N] = [sum], required > 3 -> PASS / FAIL

REGISTRY GATE:
  Per-category commitment honored:  YES / NO -> must be YES
  Floor guarantee sum > 3:          PASS / FAIL
  Dual-category coverage:           PASS / FAIL
  Registry applied during Step 7:   CONFIRMED

Do not write any ticket body until REGISTRY GATE shows all conditions met.

---

## STEP 5c -- SRE-WRITE-FIRST GATE

This gate is the binding boundary between the PERSONA VOICE TABLE and ticket body
writing. Do not write any ticket body until this gate shows PASS.

SRE-WRITE-FIRST GATE:
  SRE row position in PERSONA VOICE TABLE (Step 5): row [N] of [total rows]
  SRE is the first row in PERSONA VOICE TABLE:       YES / NO  -> PASS / FAIL
  SRE body will be the first body written in Step 7: CONFIRMED
  Gate verdict:                                      PASS / FAIL

If FAIL: rebuild the PERSONA VOICE TABLE with SRE as row 1. Re-run this gate before
writing any ticket body.

Do not advance to Step 6 with SRE-WRITE-FIRST GATE verdict = FAIL.

---

## STEP 6 -- TICKET SUMMARY TABLE AND VALIDATION TRACE

| # | Phase | Title | Category | Persona | Volume | Severity |
|---|-------|-------|----------|---------|--------|----------|

Allowed values:
- Phase: Phase 1 | Phase 2 | Phase 3
- Category: how-to | bug | feature-request | config | integration
- Persona: Support | SRE | PM | UX | C-01 through C-12
- Volume: high | medium | low
- Severity: P0 | P1 | P2 | P3

After completing the table, run the full validation trace including the CHECKPOINT MAP:

VALIDATION TRACE:
  Distinct categories:                    [N] (>= 3)              -> PASS / FAIL
  Distinct personas:                      [N] (>= 2)              -> PASS / FAIL
  P0 count:                               [N] (<= 1)              -> PASS / FAIL
  Low/medium volume entries:              [N] (>= 1)              -> PASS / FAIL
  Total rows:                             [N] (>= 7)              -> PASS / FAIL
  Phase distribution:
    Phase 1: [N] / target [N]                                     -> MATCH / MISMATCH
    Phase 2: [N] / target [N]                                     -> MATCH / MISMATCH
    Phase 3: [N] / target [N]                                     -> MATCH / MISMATCH
  All personas in voice table:            YES / NO                -> PASS / FAIL
  >= 1 ticket linked to audit row:        YES / NO                -> PASS / FAIL
  Phase-severity consistent:
    Phase 1 (P2/P3): [list] | Phase 2 (P1/P2): [list] | Phase 3 (P0/P1): [list]
    -> PASS / FAIL
  SRE first in Step 2: YES/NO | SRE first in Step 5: YES/NO       -> PASS / FAIL
  SRE-WRITE-FIRST GATE verdict (Step 5c):  PASS / FAIL            -> PASS / FAIL
  SRE in audit: YES/NO | SRE ticket in table: YES/NO              -> PASS / FAIL
  Bracket-token propagation (C-33):
    [INERTIA COMPETITOR] in Step 2 column header: YES / NO        -> PASS / FAIL
    [INERTIA COMPETITOR] in Step 3 column header: YES / NO        -> PASS / FAIL
    [INERTIA COMPETITOR] in Step 7 instruction:   YES / NO        -> PASS / FAIL
    [INERTIA COMPETITOR] in Step 10 col header:   YES / NO        -> PASS / FAIL
    >= 2 distinct table-header bracket-token locations: YES / NO  -> PASS / FAIL

  CHECKPOINT MAP (C-36):
    Checkpoint A declared in preamble -- location: Step 2 column header
      Checkpoint A satisfied (bracket-token present in Step 2 header): YES / NO
    Checkpoint B declared in preamble -- location: Step 3 column header
      Checkpoint B satisfied (bracket-token present in Step 3 header): YES / NO
    Checkpoint C declared in preamble -- location: >= 50% linked body coverage
      Checkpoint C satisfied (body coverage >= 50%):                   YES / NO
    All declared checkpoint labels echoed by name in this trace:       YES / NO
    All three checkpoint probes binary (YES/NO, no partial):           YES / NO
    -> CHECKPOINT MAP: COMPLETE / INCOMPLETE

  Overall:                                                        -> PASS / FAIL

Do not proceed to Step 6b with VALIDATION TRACE showing FAIL.

---

## STEP 6b -- FORWARD-LINK

Go back to Step 3. For every assumption audit row, fill in the Ticket # column.

FORWARD-LINK GATE:
  Assumption audit rows total: [N] | Rows with Ticket # assigned: [N] -> PASS / FAIL
  All Ticket # values exist in table: YES / NO -> PASS / FAIL | Overall: PASS / FAIL

---

## STEP 7 -- TICKET BODIES WITH DIMENSION-LABELED MARKER CITATIONS

Write SRE bodies first (consistent with SRE-WRITE-FIRST GATE). Then Support, PM/UX,
customer personas. Do not open any body with a persona declaration.

For tickets with [A#N] tag: body must reference [INERTIA COMPETITOR] verbatim --
the bracket-token [INERTIA COMPETITOR] in this instruction names the comparison anchor.
This satisfies Checkpoint C of the PROPAGATION CHAIN.

Each body: >= 2 markers from DIFFERENT columns of the persona's voice table row.
Clear every marker against REJECTION REGISTRY before citing.

Format:

### Ticket [N] [Phase N]: [Title from table]
**Traces to:** Assumption #[N]   <- audit-linked only; omit for net-new
**Body:** [2-5 sentences in the persona's actual voice]
**Voice markers:** operational=[term] | frustration=[phrase]

---

After writing all bodies:

TIER-SEQUENCING RULE (preamble):
  All TIER 1 gates must show PROCEED before TIER 2 is evaluated.

BIDIRECTIONAL LINKAGE VERIFICATION:

  TIER ARCHITECTURE SELF-CHECK:
  | Landmark | Expected location | Present | Result |
  |----------|-----------------|---------|--------|
  | TIER-SEQUENCING RULE | Preamble above block | YES/NO | PASS/FAIL |
  | -- TIER 1: Per-Pair -- | Before per-pair blocks | YES/NO | PASS/FAIL |
  | -- TIER 2: Block-Level -- | Before REVISION GATE | YES/NO | PASS/FAIL |
  All three PASS: YES -> proceed | Any FAIL: halt

  Forward: [N]/[N] rows have Ticket # | Backward: [N] bodies have "Traces to:"

  -- TIER 1: Per-Pair Verification --
    Assumption #[N] -> Ticket [N]:
      Audit phrase: "[quote -- min 5 words]"
      Body evidence: "[quote -- min 5 words]"
      Alignment: MATCH / MISMATCH | Gate: PROCEED | REVISE
    [repeat for each pair]
  All TIER 1 PROCEED: YES / NO -> PASS / FAIL

  -- TIER 2: Block-Level Clearance --
  REVISION GATE:
    Mismatched pairs: [list/"none"] | Gate status: OPEN | CLOSED
    Do not advance to Step 8 with Gate status = CLOSED.

  Overall: PASS / FAIL

---

## STEP 8 -- MARKER FORMAT AUDIT

MARKER FORMAT AUDIT:
  Total bodies: [N] | Bodies with >= 2 diff prefixes: [N]
  Flat-list (R-01): [N]->0 | Same-dim (R-02): [N]->0 | Registry-violating: [N]->0
  Coverage (>= 60%): [N]% -> PASS / FAIL | Overall: PASS / FAIL

---

## STEP 9 -- POST-GENERATION PHASE CONFIRMATION

PHASE CONFIRMATION:
  Ph1: [gen]/[tgt] | Ph2: [gen]/[tgt] | Ph3: [gen]/[tgt] | Total: [gen]/[tgt]
  -> MATCH / MISMATCH each

---

## STEP 10 -- GAP ANALYSIS TABLE

Column definitions:
- Gap type: Doc | Design | Operational
- Specific artifact: exact doc section, config field, API endpoint, runbook page, UI element
- Classification: PARITY | NET-NEW
- Incumbent [INERTIA COMPETITOR] status: what [INERTIA COMPETITOR] offers here (or
  "no equivalent") -- bracket-token in column header names the comparison target; use
  the declared product name in each cell
- Phase first surfaces: Phase 1 | Phase 2 | Phase 3

| # | Gap type | Specific artifact | Classification | Incumbent [INERTIA COMPETITOR] status | Phase first surfaces |
|---|----------|------------------|----------------|--------------------------------------|---------------------|

Minimum: 1 Doc row, 1 Design row, 1 Operational row.

---

## STEP 11 -- THRESHOLD CONFIRMATION

THRESHOLD CONFIRMATION:

C-14: [N]/[N] = [N]% (>= 60%) -> PASS / FAIL
C-16: [N]/[N] = [N]% (>= 60%) -> PASS / FAIL
C-12: [N]/[N] = [N]% (>= 60%) -> PASS / FAIL

C-31 | INERTIA COMPETITOR Propagation
  Preamble declaration present before Step 1:     YES / NO  -> PASS / FAIL
  Bodies containing declared name verbatim:       [N] / [N]
  Propagation coverage (>= 50%):                  [N]%      -> PASS / FAIL
  Step 10 Incumbent cells use declared name:      YES / NO  -> PASS / FAIL

C-32 | SRE-First Ordering
  SRE first in Step 2: YES/NO | SRE first in Step 5: YES/NO
  SRE in audit: YES/NO | SRE ticket in table: YES/NO        -> PASS / FAIL

C-33 | Bracket-Token Propagation
BLOCK-START:
  [INERTIA COMPETITOR] in Step 2 column header (Checkpoint A anchor): YES/NO
  [INERTIA COMPETITOR] in Step 3 column header (Checkpoint B anchor): YES/NO
  [INERTIA COMPETITOR] in Step 7 instruction clause:                  YES/NO
  [INERTIA COMPETITOR] in Step 10 column header:                      YES/NO
  >= 2 distinct table-header bracket-token locations:                 YES/NO
  Scan-verifiability (detectable by bracket-scan, not prose):         YES/NO -> PASS/FAIL
BLOCK-END: C-33 PASS / FAIL

C-34 | Propagation Chain Pre-Declaration
BLOCK-START:
  PROPAGATION CHAIN block present in preamble before Step 1:          YES/NO
  All three checkpoints A/B/C named with locations:                   YES/NO
  Checkpoint A satisfied (Step 2 header has bracket-token):           YES/NO
  Checkpoint B satisfied (Step 3 header has bracket-token):           YES/NO
  Checkpoint C satisfied (>= 50% linked body coverage):               YES/NO
  Completeness verifiable from preamble without traversal:            YES/NO -> PASS/FAIL
BLOCK-END: C-34 PASS / FAIL

C-35 | SRE-Write-First Enforcement Gate
BLOCK-START:
  SRE-WRITE-FIRST GATE block present at Step 5c boundary:             YES/NO
  Gate produces explicit PASS/FAIL verdict:                           YES/NO
  Gate carries "do not proceed" halt instruction:                     YES/NO
  Gate was invoked before any body was written:                       YES/NO
  Gate verdict in this output:                                        PASS / FAIL
  Advisory write-first (C-32) upgraded to binding enforcement gate:   YES/NO -> PASS/FAIL
BLOCK-END: C-35 PASS / FAIL

C-36 | Checkpoint-Mapped VALIDATION TRACE
  CHECKPOINT MAP sub-section present in Step 6 VALIDATION TRACE:  YES/NO -> PASS/FAIL
  Checkpoint A echoed by label name with YES/NO probe:             YES/NO -> PASS/FAIL
  Checkpoint B echoed by label name with YES/NO probe:             YES/NO -> PASS/FAIL
  Checkpoint C echoed by label name with YES/NO probe:             YES/NO -> PASS/FAIL
  "All declared checkpoint labels echoed" confirmation line:       YES/NO -> PASS/FAIL
  All three probes are binary (no partial/conditional):            YES/NO -> PASS/FAIL

C-37 | Cross-Criterion Synergy Declaration (per-criterion sub-blocks)
  C-33 block has scan-verifiability YES/NO as final line:           YES/NO -> PASS/FAIL
  C-34 block has scan-verifiability YES/NO as final line:           YES/NO -> PASS/FAIL
  C-35 block has scan-verifiability YES/NO as final line:           YES/NO -> PASS/FAIL

CROSS-CRITERION SYNERGY DECLARATION (LAYER 2 of 2, C-38 candidate):
  Synergy pair declared: C-33 bracket-token placement + C-34 no-traversal verifiability
  C-33 bracket-token present at Checkpoint A header (Step 2):      YES/NO
  C-33 bracket-token present at Checkpoint B header (Step 3):      YES/NO
  Checkpoint A grep-detectable by bracket-scan (not prose):        YES/NO
  Checkpoint B grep-detectable by bracket-scan (not prose):        YES/NO
  C-34 "completeness verifiable without traversal" -- structural basis:
    Answer is YES because bracket-tokens are the mechanism (not assertion): YES/NO
  Degradation declared: if C-33 absent from a header, that checkpoint
    requires prose interpretation; C-34 no-traversal property degrades:     YES/NO
  Two-layer synergy presence check (C-38):
    LAYER 1 present (preamble CROSS-CRITERION SYNERGY NOTE labeled LAYER 1 of 2): YES/NO
    LAYER 2 present (this Step 11 block labeled LAYER 2 of 2):                    YES/NO
    Both layers confirmed:                                                         YES/NO -> PASS/FAIL
  -> CROSS-CRITERION SYNERGY: STRUCTURAL / ABSENT -> PASS/FAIL

Summary:
  C-14 / C-16 / C-12:       PASS / FAIL each
  C-31 name propagation:     PASS / FAIL
  C-32 SRE-first:            PASS / FAIL
  C-33 bracket-token:        PASS / FAIL
  C-34 chain pre-decl:       PASS / FAIL
  C-35 enforce gate:         PASS / FAIL
  C-36 checkpoint map:       PASS / FAIL
  C-37 synergy sub-blocks:   PASS / FAIL
  C-38 cand. two-layer:      PASS / FAIL
  Overall: PASS (all) / FAIL (one or more)

If any threshold shows FAIL, identify the specific entries or bodies causing the
shortfall, revise, and re-run this block before submitting.
```

---

## V-02: Single-Axis -- Grep-Closed Declaration-to-Trace Loop (C-39)

**Axis:** A unique grep anchor token `[SYNERGY-ANCHOR: C33xC34]` is embedded verbatim
in both the preamble CROSS-CRITERION SYNERGY NOTE and the Step 11 CROSS-CRITERION
SYNERGY DECLARATION. The preamble note states explicitly that a single grep for
`SYNERGY-ANCHOR` finds both the declaration site and the echo site. Step 11 gains a
grep-closed verification line confirming both sites are reachable by that grep.

**Probe (C-39 candidate):** R13 V-05 placed a synergy note in the preamble and a
synergy declaration in Step 11, but a scorer verifying that both sites exist must
navigate to each location independently. A unique anchor token that appears in both
sites closes the loop: a scorer can grep for `SYNERGY-ANCHOR: C33xC34` and confirm
the grep returns exactly two matches (preamble + Step 11) without navigating manually.
C-39 would require: (a) anchor token embedded in preamble note, (b) same token embedded
in Step 11 declaration, (c) preamble note states the grep route explicitly, (d) Step 11
adds a grep-closed confirmation line: "grep for SYNERGY-ANCHOR finds preamble + Step 11:
YES/NO".

**Hypothesis:** When the anchor token appears in both sites and the preamble note
explains the grep route, the scorer's verification path from declaration to echo is
single-step (one grep command). C-39 would require the anchor token to be present at
both sites and the grep-closed confirmation to show YES.

---

```
# listen-support: Predict First-90-Day Support Tickets

Work through each step in order. Do not skip steps. Do not combine steps.

---

INERTIA COMPETITOR: [name the specific product the target personas currently use for
this workflow -- one product name, grep-checkable, no generic labels like "legacy tool"
or "the incumbent"]

This name is a constant. It appears below as the literal bracket-variable token
[INERTIA COMPETITOR] embedded in table column headers and step instruction action
clauses. Every occurrence is detectable by scanning for [INERTIA COMPETITOR].

PROPAGATION CHAIN:
  Checkpoint A: STATUS QUO ANCHOR (Step 2) -- column header "Prior [INERTIA COMPETITOR]
    behavior" uses the bracket-token; column 2 cells name this product explicitly
  Checkpoint B: ASSUMPTION AUDIT (Step 3) -- column header "Incumbent [INERTIA COMPETITOR]
    behavior" uses the bracket-token; column 2 cells cite this product by name
  Checkpoint C: Ticket bodies with [A#N] traces (Step 7) -- bodies linked to assumption
    audit rows contain this product name verbatim; coverage >= 50% of linked bodies

Completeness is verifiable from this declaration: (A) grep Step 2 header, (B) grep
Step 3 header, (C) count bodies. All three must be satisfied before submitting.

CROSS-CRITERION SYNERGY NOTE [SYNERGY-ANCHOR: C33xC34]:
  C-33 bracket-tokens at Checkpoint A (Step 2 header) and Checkpoint B (Step 3 header)
  make C-34's declared checkpoints grep-detectable. This is what makes C-34's
  "completeness verifiable without traversal" property structural rather than
  aspirational. If C-33 tokens are absent from a checkpoint header, that checkpoint
  requires prose interpretation and C-34's no-traversal property degrades to
  aspirational for that checkpoint. The CROSS-CRITERION SYNERGY DECLARATION in
  Step 11 confirms this dependency is satisfied.
  Grep route: search for [SYNERGY-ANCHOR: C33xC34] to find this declaration site
  (preamble) and its echo site (Step 11 THRESHOLD CONFIRMATION). Two matches expected.

---

## STEP 1 -- PHASE-SEVERITY GRADIENT PRIOR

Phase 1 (Day 0-30): P2/P3. P0 reserved for activation blockers affecting all users.
Phase 2 (Day 31-60): P1/P2. P0 exceptional: data loss or workflow corruption only.
Phase 3 (Day 61-90): P0/P1. No fallback at scale. P3 essentially absent.

PHASE-SEVERITY PRIOR:
  Phase 1 (Day 0-30):  typical P2/P3; P0 only for activation blockers affecting all users
  Phase 2 (Day 31-60): typical P1/P2; P0 exceptional (data loss or workflow corruption)
  Phase 3 (Day 61-90): typical P0/P1; P3 rare (users have exhausted workarounds)

---

## STEP 1b -- PHASE NARRATIVE

**Phase 1 (Day 0-30) -- First contact:**
Users explore the feature while keeping [INERTIA COMPETITOR] active as a safety net.
Each step is compared against [INERTIA COMPETITOR] behavior. Trigger event: first
contact with a divergence from [INERTIA COMPETITOR] -- setup friction, missing docs,
onboarding gaps. Tickets: high volume, low severity (prior tool fallback available).

**Phase 2 (Day 31-60) -- Committed trial:**
Users have invested real workflows; some migrated, some still in [INERTIA COMPETITOR].
Trigger event: committed workflow hits a blocking gap that works in [INERTIA COMPETITOR]
but fails here. Partial-migration friction: no simple revert, feature coverage incomplete.

**Phase 3 (Day 61-90) -- Operational dependency:**
[INERTIA COMPETITOR] is no longer available for this workflow. Trigger event: blocking
failure under production conditions. Severity escalates -- no fallback exists.

PHASE NARRATIVE COMPLETE:
  Phase 1 behavioral driver named ([INERTIA COMPETITOR] referenced): YES / NO
  Phase 2 behavioral driver named ([INERTIA COMPETITOR] referenced): YES / NO
  Phase 3 behavioral driver named ([INERTIA COMPETITOR] referenced): YES / NO
  Trigger events named for all three phases:                         YES / NO

---

## STEP 2 -- STATUS QUO ANCHOR

SRE row is listed first. The bracket-token [INERTIA COMPETITOR] in the column header
is Checkpoint A of the PROPAGATION CHAIN.

| Persona class | Prior [INERTIA COMPETITOR] behavior | Key capability expected to carry over | Most likely violated assumption |
|---------------|-------------------------------------|--------------------------------------|----------------------------------|
| SRE | | | |
| Support | | | |
| PM / UX | | | |
| C-01..C-04 (technical early adopters) | | | |
| C-05..C-08 (pragmatic mainstream) | | | |
| C-09..C-12 (enterprise/compliance) | | | |

Column 4 (violated assumption) feeds Step 3.

---

## STEP 3 -- ASSUMPTION AUDIT

**Complete the SRE row first.** SRE tickets determine the severity ceiling.

Column 2 (Incumbent [INERTIA COMPETITOR] behavior): state the specific behavior of
[INERTIA COMPETITOR] that created the expectation. The bracket-token
[INERTIA COMPETITOR] in the column header is Checkpoint B of the PROPAGATION CHAIN.
Cell values must use the declared name -- no generic substitution.

| # | Persona class | Incumbent [INERTIA COMPETITOR] behavior | Imported expectation | What this feature does instead | Resulting failure mode | Ticket # |
|---|---------------|----------------------------------------|---------------------|-------------------------------|----------------------|----------|

Ticket #: LEAVE BLANK -- assigned in Step 6b. Complete at least 1 row.

ASSUMPTION AUDIT COMPLETE:
  Rows documented:                                         [N]
  SRE row present:                                         YES / NO
  All 5 non-ID columns populated:                          YES / NO
  Column 2 cells reference [INERTIA COMPETITOR] by name:   YES / NO -> Checkpoint B
  Ticket IDs pending at Step 6b:                           [N] rows

---

## STEP 4 -- PHASE DISTRIBUTION TARGET

PHASE DISTRIBUTION TARGET:
  Phase 1 (Day 0-30):  [N] tickets   -- first contact, [INERTIA COMPETITOR] comparison
  Phase 2 (Day 31-60): [N] tickets   -- committed trial, migration edge cases
  Phase 3 (Day 61-90): [N] tickets   -- operational dependency, no fallback
  Total:               [N] tickets

Constraints: Phase 1 >= 3. Phase 3 >= 1. Total >= 7. All three phases non-zero.

---

## STEP 5 -- PERSONA VOICE TABLE (DIMENSION REGISTRY)

SRE row is listed first. The SRE-WRITE-FIRST GATE in Step 5c verifies this position.

| Persona | Operational vocabulary | Frustration register | Framing conventions |
|---------|----------------------|---------------------|---------------------|
| SRE | (>= 2 specific terms) | (>= 2 specific phrases) | (>= 2 structural patterns) |
| Support | (>= 2 specific terms) | (>= 2 specific phrases) | (>= 2 structural patterns) |
| [other personas used] | (>= 2 specific terms) | (>= 2 specific phrases) | (>= 2 structural patterns) |

Dimension prefixes: operational= | frustration= | framing=

What disqualifies: role declarations ("As an SRE"), generic verbs ("noticed", "tried"),
bare nouns ("logs", "data", "error").

---

## STEP 5b -- DIMENSION-LABEL REJECTION REGISTRY

**Per-category minimum commitment:**
  Category 1 (Format violations) minimum: 2 entries
  Category 2 (Value violations) minimum:  2 entries

Floor guarantee: 2 + 2 = 4 > 3.

REJECTION REGISTRY:

Category 1: R-01 (flat list), R-02 (same prefix twice), R-03 (count without naming)
Category 2: R-04 (role declarations), R-05 (generic verbs), R-06 (synonym pairs),
            R-07 (bare nouns)

REGISTRY COMPLETENESS CHECK:
  Category 1: [N] (>= 2) | Category 2: [N] (>= 2) | Total: [N] (>= 3) -> PASS / FAIL
  Floor guarantee: [N] + [N] = [sum], required > 3 -> PASS / FAIL

REGISTRY GATE:
  Per-category commitment honored:  YES / NO -> must be YES
  Floor guarantee sum > 3:          PASS / FAIL
  Dual-category coverage:           PASS / FAIL
  Registry applied during Step 7:   CONFIRMED

Do not write any ticket body until REGISTRY GATE shows all conditions met.

---

## STEP 5c -- SRE-WRITE-FIRST GATE

SRE-WRITE-FIRST GATE:
  SRE row position in PERSONA VOICE TABLE (Step 5): row [N] of [total rows]
  SRE is the first row in PERSONA VOICE TABLE:       YES / NO  -> PASS / FAIL
  SRE body will be the first body written in Step 7: CONFIRMED
  Gate verdict:                                      PASS / FAIL

If FAIL: rebuild the PERSONA VOICE TABLE with SRE as row 1. Re-run this gate before
writing any ticket body.

---

## STEP 6 -- TICKET SUMMARY TABLE AND VALIDATION TRACE

| # | Phase | Title | Category | Persona | Volume | Severity |
|---|-------|-------|----------|---------|--------|----------|

Allowed values:
- Phase: Phase 1 | Phase 2 | Phase 3
- Category: how-to | bug | feature-request | config | integration
- Persona: Support | SRE | PM | UX | C-01 through C-12
- Volume: high | medium | low
- Severity: P0 | P1 | P2 | P3

VALIDATION TRACE:
  Distinct categories:                    [N] (>= 3)              -> PASS / FAIL
  Distinct personas:                      [N] (>= 2)              -> PASS / FAIL
  P0 count:                               [N] (<= 1)              -> PASS / FAIL
  Low/medium volume entries:              [N] (>= 1)              -> PASS / FAIL
  Total rows:                             [N] (>= 7)              -> PASS / FAIL
  Phase distribution:
    Phase 1: [N] / target [N]                                     -> MATCH / MISMATCH
    Phase 2: [N] / target [N]                                     -> MATCH / MISMATCH
    Phase 3: [N] / target [N]                                     -> MATCH / MISMATCH
  All personas in voice table:            YES / NO                -> PASS / FAIL
  >= 1 ticket linked to audit row:        YES / NO                -> PASS / FAIL
  Phase-severity consistent:
    Phase 1 (P2/P3): [list] | Phase 2 (P1/P2): [list] | Phase 3 (P0/P1): [list]
    -> PASS / FAIL
  SRE first in Step 2: YES/NO | SRE first in Step 5: YES/NO       -> PASS / FAIL
  SRE-WRITE-FIRST GATE verdict (Step 5c):  PASS / FAIL            -> PASS / FAIL
  Bracket-token propagation (C-33):
    [INERTIA COMPETITOR] in Step 2 column header: YES / NO        -> PASS / FAIL
    [INERTIA COMPETITOR] in Step 3 column header: YES / NO        -> PASS / FAIL
    [INERTIA COMPETITOR] in Step 7 instruction:   YES / NO        -> PASS / FAIL
    [INERTIA COMPETITOR] in Step 10 col header:   YES / NO        -> PASS / FAIL

  CHECKPOINT MAP (C-36):
    Checkpoint A declared in preamble -- location: Step 2 column header
      Checkpoint A satisfied (bracket-token present in Step 2 header): YES / NO
    Checkpoint B declared in preamble -- location: Step 3 column header
      Checkpoint B satisfied (bracket-token present in Step 3 header): YES / NO
    Checkpoint C declared in preamble -- location: >= 50% linked body coverage
      Checkpoint C satisfied (body coverage >= 50%):                   YES / NO
    All declared checkpoint labels echoed by name in this trace:       YES / NO
    All three checkpoint probes binary (YES/NO, no partial):           YES / NO
    -> CHECKPOINT MAP: COMPLETE / INCOMPLETE

  Overall:                                                        -> PASS / FAIL

---

## STEP 6b -- FORWARD-LINK

FORWARD-LINK GATE:
  Assumption audit rows total: [N] | Rows with Ticket # assigned: [N] -> PASS / FAIL
  All Ticket # values exist in table: YES / NO -> PASS / FAIL | Overall: PASS / FAIL

---

## STEP 7 -- TICKET BODIES WITH DIMENSION-LABELED MARKER CITATIONS

Write SRE bodies first. Then Support, PM/UX, customer personas.

For tickets with [A#N] tag: body must reference [INERTIA COMPETITOR] verbatim.
Each body: >= 2 markers from DIFFERENT columns of the persona's voice table row.
Clear every marker against REJECTION REGISTRY before citing.

### Ticket [N] [Phase N]: [Title from table]
**Traces to:** Assumption #[N]
**Body:** [2-5 sentences in the persona's actual voice]
**Voice markers:** operational=[term] | frustration=[phrase]

---

TIER-SEQUENCING RULE (preamble):
  All TIER 1 gates must show PROCEED before TIER 2 is evaluated.

BIDIRECTIONAL LINKAGE VERIFICATION:

  TIER ARCHITECTURE SELF-CHECK:
  | Landmark | Expected location | Present | Result |
  |----------|-----------------|---------|--------|
  | TIER-SEQUENCING RULE | Preamble above block | YES/NO | PASS/FAIL |
  | -- TIER 1: Per-Pair -- | Before per-pair blocks | YES/NO | PASS/FAIL |
  | -- TIER 2: Block-Level -- | Before REVISION GATE | YES/NO | PASS/FAIL |

  -- TIER 1: Per-Pair Verification --
    Assumption #[N] -> Ticket [N]:
      Audit phrase: "[quote -- min 5 words]"
      Body evidence: "[quote -- min 5 words]"
      Alignment: MATCH / MISMATCH | Gate: PROCEED | REVISE
  All TIER 1 PROCEED: YES / NO -> PASS / FAIL

  -- TIER 2: Block-Level Clearance --
  REVISION GATE:
    Mismatched pairs: [list/"none"] | Gate status: OPEN | CLOSED

  Overall: PASS / FAIL

---

## STEP 8 -- MARKER FORMAT AUDIT

MARKER FORMAT AUDIT:
  Total bodies: [N] | Bodies with >= 2 diff prefixes: [N]
  Flat-list (R-01): [N]->0 | Same-dim (R-02): [N]->0 | Registry-violating: [N]->0
  Coverage (>= 60%): [N]% -> PASS / FAIL | Overall: PASS / FAIL

---

## STEP 9 -- POST-GENERATION PHASE CONFIRMATION

PHASE CONFIRMATION:
  Ph1: [gen]/[tgt] | Ph2: [gen]/[tgt] | Ph3: [gen]/[tgt] | Total: [gen]/[tgt]
  -> MATCH / MISMATCH each

---

## STEP 10 -- GAP ANALYSIS TABLE

| # | Gap type | Specific artifact | Classification | Incumbent [INERTIA COMPETITOR] status | Phase first surfaces |
|---|----------|------------------|----------------|--------------------------------------|---------------------|

Minimum: 1 Doc row, 1 Design row, 1 Operational row.

---

## STEP 11 -- THRESHOLD CONFIRMATION

THRESHOLD CONFIRMATION:

C-14: [N]/[N] = [N]% (>= 60%) -> PASS / FAIL
C-16: [N]/[N] = [N]% (>= 60%) -> PASS / FAIL
C-12: [N]/[N] = [N]% (>= 60%) -> PASS / FAIL

C-31 | INERTIA COMPETITOR Propagation
  Preamble declaration present:                   YES / NO  -> PASS / FAIL
  Bodies containing declared name verbatim:       [N] / [N]
  Propagation coverage (>= 50%):                  [N]%      -> PASS / FAIL
  Step 10 Incumbent cells use declared name:      YES / NO  -> PASS / FAIL

C-32 | SRE-First Ordering
  SRE first in Step 2: YES/NO | SRE first in Step 5: YES/NO  -> PASS / FAIL

C-33 | Bracket-Token Propagation
BLOCK-START:
  [INERTIA COMPETITOR] in Step 2 column header:               YES/NO
  [INERTIA COMPETITOR] in Step 3 column header:               YES/NO
  [INERTIA COMPETITOR] in Step 7 instruction clause:          YES/NO
  [INERTIA COMPETITOR] in Step 10 column header:              YES/NO
  >= 2 distinct table-header bracket-token locations:         YES/NO
  Scan-verifiability (detectable by bracket-scan, not prose): YES/NO -> PASS/FAIL
BLOCK-END: C-33 PASS / FAIL

C-34 | Propagation Chain Pre-Declaration
BLOCK-START:
  PROPAGATION CHAIN block present in preamble before Step 1:          YES/NO
  All three checkpoints A/B/C named with locations:                   YES/NO
  Checkpoint A satisfied (Step 2 header has bracket-token):           YES/NO
  Checkpoint B satisfied (Step 3 header has bracket-token):           YES/NO
  Checkpoint C satisfied (>= 50% linked body coverage):               YES/NO
  Completeness verifiable from preamble without traversal:            YES/NO -> PASS/FAIL
BLOCK-END: C-34 PASS / FAIL

C-35 | SRE-Write-First Enforcement Gate
BLOCK-START:
  SRE-WRITE-FIRST GATE block present at Step 5c boundary:             YES/NO
  Gate produces explicit PASS/FAIL verdict:                           YES/NO
  Gate carries "do not proceed" halt instruction:                     YES/NO
  Gate was invoked before any body was written:                       YES/NO
  Gate verdict in this output:                                        PASS / FAIL
  Advisory write-first upgraded to binding enforcement gate:          YES/NO -> PASS/FAIL
BLOCK-END: C-35 PASS / FAIL

C-36 | Checkpoint-Mapped VALIDATION TRACE
  CHECKPOINT MAP sub-section present in Step 6:            YES/NO -> PASS/FAIL
  Checkpoint A echoed by label name with YES/NO probe:     YES/NO -> PASS/FAIL
  Checkpoint B echoed by label name with YES/NO probe:     YES/NO -> PASS/FAIL
  Checkpoint C echoed by label name with YES/NO probe:     YES/NO -> PASS/FAIL
  All three probes are binary (no partial/conditional):    YES/NO -> PASS/FAIL

C-37 | Cross-Criterion Synergy Sub-Blocks
  C-33 block has scan-verifiability line:                  YES/NO -> PASS/FAIL
  C-34 block has scan-verifiability line:                  YES/NO -> PASS/FAIL
  C-35 block has scan-verifiability line:                  YES/NO -> PASS/FAIL

CROSS-CRITERION SYNERGY DECLARATION [SYNERGY-ANCHOR: C33xC34] (C-39 candidate):
  Synergy pair declared: C-33 bracket-token placement + C-34 no-traversal verifiability
  C-33 bracket-token present at Checkpoint A header (Step 2):      YES/NO
  C-33 bracket-token present at Checkpoint B header (Step 3):      YES/NO
  Checkpoint A grep-detectable by bracket-scan (not prose):        YES/NO
  Checkpoint B grep-detectable by bracket-scan (not prose):        YES/NO
  C-34 "completeness verifiable without traversal" -- structural:  YES/NO
  Degradation declared: if C-33 absent, that checkpoint degrades:  YES/NO
  Grep-closed loop (C-39):
    [SYNERGY-ANCHOR: C33xC34] present in preamble SYNERGY NOTE:        YES/NO
    [SYNERGY-ANCHOR: C33xC34] present in this Step 11 declaration:     YES/NO
    Single grep for SYNERGY-ANCHOR finds both declaration + echo site: YES/NO -> PASS/FAIL
  -> CROSS-CRITERION SYNERGY: STRUCTURAL / ABSENT -> PASS/FAIL

Summary:
  C-14 / C-16 / C-12:       PASS / FAIL each
  C-31 through C-37:         PASS / FAIL each
  C-39 cand. grep-closed:    PASS / FAIL
  Overall: PASS (all) / FAIL (one or more)

If any threshold shows FAIL, revise and re-run before submitting.
```

---

## V-03: Single-Axis -- Falsifiable Degradation Clause (C-40)

**Axis:** Both the preamble CROSS-CRITERION SYNERGY NOTE and the Step 11 CROSS-CRITERION
SYNERGY DECLARATION gain an explicit DEGRADATION CLAUSE sub-section. The clause is
written as an if/then conditional with three parts: (a) the trigger condition (C-33
bracket-token absent from a checkpoint header), (b) the immediate consequence (that
checkpoint requires prose interpretation to verify), (c) the cascading effect on C-34
(the no-traversal property degrades to aspirational). The clause is labeled "falsifiable"
because the failure condition is specific enough to be tested rather than assumed.

**Probe (C-40 candidate):** R13 V-05 included "Degradation declared: if C-33 absent
from a header..." as a single YES/NO line in the Step 11 synergy block. That line
confirmed presence but did not expose the logical structure of the degradation. A
DEGRADATION CLAUSE sub-section with explicit if/then wording makes the failure
condition testable: a scorer can ask "is the trigger condition specific?" (YES: a named
absence), "is the consequence specific?" (YES: prose interpretation required), "is the
C-34 effect named?" (YES: no-traversal degrades). C-40 would require: (a) the clause
is present in both preamble and Step 11, (b) the if/then structure is explicit,
(c) the failure state is named, (d) the clause is labeled "falsifiable."

**Hypothesis:** When the degradation clause is written as a testable conditional rather
than a single-line declaration, it becomes auditable as a logical claim rather than an
assertion. C-40 would require the clause to contain: trigger condition (if), immediate
consequence (then), C-34 cascade (and), and falsifiability label.

---

```
# listen-support: Predict First-90-Day Support Tickets

Work through each step in order. Do not skip steps. Do not combine steps.

---

INERTIA COMPETITOR: [name the specific product the target personas currently use for
this workflow -- one product name, grep-checkable, no generic labels like "legacy tool"
or "the incumbent"]

This name is a constant. It appears below as the literal bracket-variable token
[INERTIA COMPETITOR] embedded in table column headers and step instruction action
clauses. Every occurrence is detectable by scanning for [INERTIA COMPETITOR].

PROPAGATION CHAIN:
  Checkpoint A: STATUS QUO ANCHOR (Step 2) -- column header "Prior [INERTIA COMPETITOR]
    behavior" uses the bracket-token; column 2 cells name this product explicitly
  Checkpoint B: ASSUMPTION AUDIT (Step 3) -- column header "Incumbent [INERTIA COMPETITOR]
    behavior" uses the bracket-token; column 2 cells cite this product by name
  Checkpoint C: Ticket bodies with [A#N] traces (Step 7) -- bodies linked to assumption
    audit rows contain this product name verbatim; coverage >= 50% of linked bodies

Completeness is verifiable from this declaration: (A) grep Step 2 header, (B) grep
Step 3 header, (C) count bodies. All three must be satisfied before submitting.

CROSS-CRITERION SYNERGY NOTE:
  C-33 bracket-tokens at Checkpoint A (Step 2 header) and Checkpoint B (Step 3 header)
  make C-34's declared checkpoints grep-detectable. This is what makes C-34's
  "completeness verifiable without traversal" property structural rather than
  aspirational. The CROSS-CRITERION SYNERGY DECLARATION in Step 11 confirms this
  dependency is satisfied.
  DEGRADATION CLAUSE (falsifiable):
    IF C-33 bracket-token is absent from a checkpoint header,
    THEN that checkpoint requires prose interpretation to verify,
    AND C-34's "completeness verifiable without traversal" property degrades to
      aspirational for that checkpoint.
    Failure state: any checkpoint header missing [INERTIA COMPETITOR] bracket-token
    causes that checkpoint's C-34 no-traversal claim to be unverifiable by grep.
    This clause is falsifiable: the trigger condition (token absent) is binary and
    testable; the consequence (prose interpretation required) is observable.

---

## STEP 1 -- PHASE-SEVERITY GRADIENT PRIOR

Phase 1 (Day 0-30): P2/P3. P0 reserved for activation blockers affecting all users.
Phase 2 (Day 31-60): P1/P2. P0 exceptional: data loss or workflow corruption only.
Phase 3 (Day 61-90): P0/P1. No fallback at scale. P3 essentially absent.

PHASE-SEVERITY PRIOR:
  Phase 1 (Day 0-30):  typical P2/P3; P0 only for activation blockers affecting all users
  Phase 2 (Day 31-60): typical P1/P2; P0 exceptional (data loss or workflow corruption)
  Phase 3 (Day 61-90): typical P0/P1; P3 rare (users have exhausted workarounds)

---

## STEP 1b -- PHASE NARRATIVE

**Phase 1 (Day 0-30) -- First contact:**
Users explore the feature while keeping [INERTIA COMPETITOR] active as a safety net.
Trigger event: first contact with a divergence from [INERTIA COMPETITOR] -- setup
friction, missing docs, onboarding gaps. Tickets: high volume, low severity.

**Phase 2 (Day 31-60) -- Committed trial:**
Users have invested real workflows; some migrated, some still in [INERTIA COMPETITOR].
Trigger event: committed workflow hits a blocking gap that works in [INERTIA COMPETITOR]
but fails here. Partial-migration friction: no simple revert.

**Phase 3 (Day 61-90) -- Operational dependency:**
[INERTIA COMPETITOR] is no longer available. Trigger event: blocking failure under
production conditions. Severity escalates -- no fallback exists.

PHASE NARRATIVE COMPLETE:
  Phase 1 behavioral driver named ([INERTIA COMPETITOR] referenced): YES / NO
  Phase 2 behavioral driver named ([INERTIA COMPETITOR] referenced): YES / NO
  Phase 3 behavioral driver named ([INERTIA COMPETITOR] referenced): YES / NO
  Trigger events named for all three phases:                         YES / NO

---

## STEP 2 -- STATUS QUO ANCHOR

SRE row is listed first. The bracket-token [INERTIA COMPETITOR] in the column header
is Checkpoint A of the PROPAGATION CHAIN.

| Persona class | Prior [INERTIA COMPETITOR] behavior | Key capability expected to carry over | Most likely violated assumption |
|---------------|-------------------------------------|--------------------------------------|----------------------------------|
| SRE | | | |
| Support | | | |
| PM / UX | | | |
| C-01..C-04 (technical early adopters) | | | |
| C-05..C-08 (pragmatic mainstream) | | | |
| C-09..C-12 (enterprise/compliance) | | | |

---

## STEP 3 -- ASSUMPTION AUDIT

**Complete the SRE row first.**

The bracket-token [INERTIA COMPETITOR] in the column header is Checkpoint B.

| # | Persona class | Incumbent [INERTIA COMPETITOR] behavior | Imported expectation | What this feature does instead | Resulting failure mode | Ticket # |
|---|---------------|----------------------------------------|---------------------|-------------------------------|----------------------|----------|

Ticket #: LEAVE BLANK -- assigned in Step 6b.

ASSUMPTION AUDIT COMPLETE:
  Rows documented:                                         [N]
  SRE row present:                                         YES / NO
  All 5 non-ID columns populated:                          YES / NO
  Column 2 cells reference [INERTIA COMPETITOR] by name:   YES / NO -> Checkpoint B
  Ticket IDs pending at Step 6b:                           [N] rows

---

## STEP 4 -- PHASE DISTRIBUTION TARGET

PHASE DISTRIBUTION TARGET:
  Phase 1 (Day 0-30):  [N] tickets
  Phase 2 (Day 31-60): [N] tickets
  Phase 3 (Day 61-90): [N] tickets
  Total:               [N] tickets

Constraints: Phase 1 >= 3. Phase 3 >= 1. Total >= 7.

---

## STEP 5 -- PERSONA VOICE TABLE (DIMENSION REGISTRY)

SRE row is listed first.

| Persona | Operational vocabulary | Frustration register | Framing conventions |
|---------|----------------------|---------------------|---------------------|
| SRE | (>= 2 specific terms) | (>= 2 specific phrases) | (>= 2 structural patterns) |
| Support | (>= 2 specific terms) | (>= 2 specific phrases) | (>= 2 structural patterns) |
| [other personas used] | (>= 2 specific terms) | (>= 2 specific phrases) | (>= 2 structural patterns) |

Dimension prefixes: operational= | frustration= | framing=

What disqualifies: role declarations, generic verbs, bare nouns.

---

## STEP 5b -- DIMENSION-LABEL REJECTION REGISTRY

**Per-category minimum commitment:**
  Category 1 (Format violations) minimum: 2 entries
  Category 2 (Value violations) minimum:  2 entries

Floor guarantee: 2 + 2 = 4 > 3.

REJECTION REGISTRY:

Category 1: R-01 (flat list), R-02 (same prefix twice), R-03 (count without naming)
Category 2: R-04 (role declarations), R-05 (generic verbs), R-06 (synonym pairs),
            R-07 (bare nouns)

REGISTRY COMPLETENESS CHECK:
  Category 1: [N] (>= 2) | Category 2: [N] (>= 2) | Total: [N] (>= 3) -> PASS / FAIL
  Floor guarantee: [N] + [N] = [sum], required > 3 -> PASS / FAIL

REGISTRY GATE:
  Per-category commitment honored:  YES / NO
  Floor guarantee sum > 3:          PASS / FAIL
  Dual-category coverage:           PASS / FAIL
  Registry applied during Step 7:   CONFIRMED

---

## STEP 5c -- SRE-WRITE-FIRST GATE

SRE-WRITE-FIRST GATE:
  SRE row position in PERSONA VOICE TABLE: row [N] of [total rows]
  SRE is the first row:                    YES / NO  -> PASS / FAIL
  SRE body will be written first:          CONFIRMED
  Gate verdict:                            PASS / FAIL

---

## STEP 6 -- TICKET SUMMARY TABLE AND VALIDATION TRACE

| # | Phase | Title | Category | Persona | Volume | Severity |
|---|-------|-------|----------|---------|--------|----------|

VALIDATION TRACE:
  Distinct categories:                    [N] (>= 3)              -> PASS / FAIL
  Distinct personas:                      [N] (>= 2)              -> PASS / FAIL
  P0 count:                               [N] (<= 1)              -> PASS / FAIL
  Low/medium volume entries:              [N] (>= 1)              -> PASS / FAIL
  Total rows:                             [N] (>= 7)              -> PASS / FAIL
  Phase distribution:
    Phase 1: [N] / target [N]                                     -> MATCH / MISMATCH
    Phase 2: [N] / target [N]                                     -> MATCH / MISMATCH
    Phase 3: [N] / target [N]                                     -> MATCH / MISMATCH
  Phase-severity consistent (P2/P3 | P1/P2 | P0/P1):             -> PASS / FAIL
  SRE-WRITE-FIRST GATE verdict:           PASS / FAIL
  Bracket-token in Step 2 header: YES/NO | Step 3 header: YES/NO  -> PASS / FAIL

  CHECKPOINT MAP (C-36):
    Checkpoint A (Step 2 header bracket-token present): YES / NO
    Checkpoint B (Step 3 header bracket-token present): YES / NO
    Checkpoint C (>= 50% linked body coverage):         YES / NO
    All labels echoed by name with binary probe:        YES / NO
    -> CHECKPOINT MAP: COMPLETE / INCOMPLETE

  Overall:                                                        -> PASS / FAIL

---

## STEP 6b -- FORWARD-LINK

FORWARD-LINK GATE:
  Audit rows: [N] | Rows with Ticket #: [N] -> PASS / FAIL
  All Ticket # values exist in table: YES / NO -> PASS / FAIL

---

## STEP 7 -- TICKET BODIES

Write SRE bodies first. For [A#N] tickets: reference [INERTIA COMPETITOR] verbatim.
Each body: >= 2 markers from DIFFERENT persona voice table columns.

### Ticket [N] [Phase N]: [Title]
**Traces to:** Assumption #[N]
**Body:** [2-5 sentences]
**Voice markers:** operational=[term] | frustration=[phrase]

---

TIER-SEQUENCING RULE (preamble): All TIER 1 gates must show PROCEED before TIER 2.

BIDIRECTIONAL LINKAGE VERIFICATION:

  TIER ARCHITECTURE SELF-CHECK:
  | Landmark | Expected location | Present | Result |
  |----------|-----------------|---------|--------|
  | TIER-SEQUENCING RULE | Preamble above block | YES/NO | PASS/FAIL |
  | -- TIER 1: Per-Pair -- | Before per-pair blocks | YES/NO | PASS/FAIL |
  | -- TIER 2: Block-Level -- | Before REVISION GATE | YES/NO | PASS/FAIL |

  -- TIER 1: Per-Pair Verification --
    Assumption #[N] -> Ticket [N]:
      Audit phrase: "[quote]" | Body evidence: "[quote]"
      Alignment: MATCH / MISMATCH | Gate: PROCEED | REVISE
  All TIER 1 PROCEED: YES / NO -> PASS / FAIL

  -- TIER 2: Block-Level Clearance --
  REVISION GATE:
    Mismatched pairs: [list/"none"] | Gate status: OPEN | CLOSED

---

## STEP 8 -- MARKER FORMAT AUDIT

MARKER FORMAT AUDIT:
  Total bodies: [N] | Bodies with >= 2 diff prefixes: [N]
  Coverage (>= 60%): [N]% -> PASS / FAIL | Overall: PASS / FAIL

---

## STEP 9 -- POST-GENERATION PHASE CONFIRMATION

PHASE CONFIRMATION:
  Ph1: [gen]/[tgt] | Ph2: [gen]/[tgt] | Ph3: [gen]/[tgt] -> MATCH / MISMATCH each

---

## STEP 10 -- GAP ANALYSIS TABLE

| # | Gap type | Specific artifact | Classification | Incumbent [INERTIA COMPETITOR] status | Phase first surfaces |
|---|----------|------------------|----------------|--------------------------------------|---------------------|

Minimum: 1 Doc row, 1 Design row, 1 Operational row.

---

## STEP 11 -- THRESHOLD CONFIRMATION

THRESHOLD CONFIRMATION:

C-14: [N]/[N] = [N]% (>= 60%) -> PASS / FAIL
C-16: [N]/[N] = [N]% (>= 60%) -> PASS / FAIL
C-12: [N]/[N] = [N]% (>= 60%) -> PASS / FAIL

C-31 | INERTIA COMPETITOR Propagation
  Preamble declaration present:                   YES / NO  -> PASS / FAIL
  Bodies containing declared name verbatim:       [N] / [N]
  Propagation coverage (>= 50%):                  [N]%      -> PASS / FAIL
  Step 10 cells use declared name:                YES / NO  -> PASS / FAIL

C-32 | SRE-First Ordering
  SRE first in Step 2: YES/NO | SRE first in Step 5: YES/NO  -> PASS / FAIL

C-33 | Bracket-Token Propagation
BLOCK-START:
  [INERTIA COMPETITOR] in Step 2 column header:               YES/NO
  [INERTIA COMPETITOR] in Step 3 column header:               YES/NO
  [INERTIA COMPETITOR] in Step 7 instruction clause:          YES/NO
  [INERTIA COMPETITOR] in Step 10 column header:              YES/NO
  >= 2 distinct table-header locations:                       YES/NO
  Scan-verifiability:                                         YES/NO -> PASS/FAIL
BLOCK-END: C-33 PASS / FAIL

C-34 | Propagation Chain Pre-Declaration
BLOCK-START:
  PROPAGATION CHAIN block present in preamble:                YES/NO
  All three checkpoints A/B/C named with locations:           YES/NO
  Checkpoint A satisfied:                                     YES/NO
  Checkpoint B satisfied:                                     YES/NO
  Checkpoint C satisfied:                                     YES/NO
  Completeness verifiable from preamble without traversal:    YES/NO -> PASS/FAIL
BLOCK-END: C-34 PASS / FAIL

C-35 | SRE-Write-First Enforcement Gate
BLOCK-START:
  SRE-WRITE-FIRST GATE block present at Step 5c:              YES/NO
  Gate produces explicit PASS/FAIL verdict:                   YES/NO
  Gate carries "do not proceed" halt instruction:             YES/NO
  Gate was invoked before any body was written:               YES/NO
  Gate verdict:                                               PASS / FAIL
  Advisory upgraded to binding enforcement gate:              YES/NO -> PASS/FAIL
BLOCK-END: C-35 PASS / FAIL

C-36 | Checkpoint-Mapped VALIDATION TRACE
  CHECKPOINT MAP present in Step 6:                        YES/NO -> PASS/FAIL
  Checkpoint A echoed by label with YES/NO probe:          YES/NO -> PASS/FAIL
  Checkpoint B echoed by label with YES/NO probe:          YES/NO -> PASS/FAIL
  Checkpoint C echoed by label with YES/NO probe:          YES/NO -> PASS/FAIL
  All probes binary:                                       YES/NO -> PASS/FAIL

C-37 | Cross-Criterion Synergy Sub-Blocks
  C-33 block has scan-verifiability line:                  YES/NO -> PASS/FAIL
  C-34 block has scan-verifiability line:                  YES/NO -> PASS/FAIL
  C-35 block has scan-verifiability line:                  YES/NO -> PASS/FAIL

CROSS-CRITERION SYNERGY DECLARATION (C-40 candidate):
  Synergy pair: C-33 bracket-token placement + C-34 no-traversal verifiability
  C-33 token at Checkpoint A (Step 2 header):              YES/NO
  C-33 token at Checkpoint B (Step 3 header):              YES/NO
  Checkpoint A grep-detectable:                            YES/NO
  Checkpoint B grep-detectable:                            YES/NO
  C-34 no-traversal is structural (not assertion):         YES/NO
  DEGRADATION CLAUSE (falsifiable, C-40):
    Trigger condition: C-33 bracket-token absent from a checkpoint header
    Immediate consequence: that checkpoint requires prose interpretation
    C-34 cascade: no-traversal property degrades to aspirational for that checkpoint
    Failure state named (specific, testable):              YES/NO
    If/then structure present (condition + consequence):   YES/NO
    C-34 cascade effect named:                             YES/NO
    Clause labeled falsifiable:                            YES/NO -> PASS/FAIL
  Preamble DEGRADATION CLAUSE also present:                YES/NO -> PASS/FAIL
  -> CROSS-CRITERION SYNERGY: STRUCTURAL / ABSENT -> PASS/FAIL

Summary:
  C-14 / C-16 / C-12:       PASS / FAIL each
  C-31 through C-37:         PASS / FAIL each
  C-40 cand. falsifiable:    PASS / FAIL
  Overall: PASS (all) / FAIL (one or more)
```

---

## V-04: Combined -- Two-Layer Synergy + Grep-Closed Loop (C-38 + C-39)

**Axes:** V-01 two-layer labeling (LAYER 1 / LAYER 2) + V-02 grep anchor token
`[SYNERGY-ANCHOR: C33xC34]`. Independent mechanisms: layer labeling addresses
presence verification (can a scorer confirm both locations exist?); grep anchor
addresses locatability (can a scorer navigate from declaration to echo in one step?).
Both are active simultaneously but test different verifiability properties.

**Hypothesis:** Two-layer labeling alone confirms presence; grep anchor alone confirms
navigability. Together they confirm both: a scorer can (a) scan for LAYER labels to
confirm two-location presence and (b) grep for the anchor to jump between sites.
C-38 + C-39 together would require both mechanisms simultaneously.

---

```
# listen-support: Predict First-90-Day Support Tickets

Work through each step in order. Do not skip steps. Do not combine steps.

---

INERTIA COMPETITOR: [name the specific product the target personas currently use for
this workflow -- one product name, grep-checkable, no generic labels like "legacy tool"
or "the incumbent"]

This name is a constant. It appears below as the literal bracket-variable token
[INERTIA COMPETITOR] embedded in table column headers and step instruction action
clauses. Every occurrence is detectable by scanning for [INERTIA COMPETITOR].

PROPAGATION CHAIN:
  Checkpoint A: STATUS QUO ANCHOR (Step 2) -- column header "Prior [INERTIA COMPETITOR]
    behavior" uses the bracket-token; column 2 cells name this product explicitly
  Checkpoint B: ASSUMPTION AUDIT (Step 3) -- column header "Incumbent [INERTIA COMPETITOR]
    behavior" uses the bracket-token; column 2 cells cite this product by name
  Checkpoint C: Ticket bodies with [A#N] traces (Step 7) -- bodies linked to assumption
    audit rows contain this product name verbatim; coverage >= 50% of linked bodies

Completeness is verifiable from this declaration: (A) grep Step 2 header, (B) grep
Step 3 header, (C) count bodies. All three must be satisfied before submitting.

CROSS-CRITERION SYNERGY NOTE (LAYER 1 of 2) [SYNERGY-ANCHOR: C33xC34]:
  C-33 bracket-tokens at Checkpoint A (Step 2 header) and Checkpoint B (Step 3 header)
  make C-34's declared checkpoints grep-detectable. This is what makes C-34's
  "completeness verifiable without traversal" property structural rather than
  aspirational. If C-33 tokens are absent from a checkpoint header, that checkpoint
  requires prose interpretation and C-34's no-traversal property degrades to
  aspirational for that checkpoint. The CROSS-CRITERION SYNERGY DECLARATION (LAYER 2
  of 2) in Step 11 confirms this dependency is satisfied. Two-layer synergy: this note
  is LAYER 1; the Step 11 declaration is LAYER 2. Both must be present.
  Grep route: search for [SYNERGY-ANCHOR: C33xC34] to find both LAYER 1 (this note)
  and LAYER 2 (Step 11 declaration). Two matches expected; one grep closes the loop.

---

## STEP 1 -- PHASE-SEVERITY GRADIENT PRIOR

Phase 1 (Day 0-30): P2/P3. P0 reserved for activation blockers affecting all users.
Phase 2 (Day 31-60): P1/P2. P0 exceptional: data loss or workflow corruption only.
Phase 3 (Day 61-90): P0/P1. No fallback at scale. P3 essentially absent.

PHASE-SEVERITY PRIOR:
  Phase 1 (Day 0-30):  typical P2/P3; P0 only for activation blockers affecting all users
  Phase 2 (Day 31-60): typical P1/P2; P0 exceptional (data loss or workflow corruption)
  Phase 3 (Day 61-90): typical P0/P1; P3 rare (users have exhausted workarounds)

---

## STEP 1b -- PHASE NARRATIVE

**Phase 1 (Day 0-30) -- First contact:**
Users explore the feature while keeping [INERTIA COMPETITOR] active as a safety net.
Trigger event: first divergence from [INERTIA COMPETITOR] -- setup friction, missing
docs, onboarding gaps. Tickets: high volume, low severity.

**Phase 2 (Day 31-60) -- Committed trial:**
Users have invested real workflows; some migrated, some still in [INERTIA COMPETITOR].
Trigger event: committed workflow hits a blocking gap that works in [INERTIA COMPETITOR]
but fails here.

**Phase 3 (Day 61-90) -- Operational dependency:**
[INERTIA COMPETITOR] no longer available. Trigger event: blocking failure under
production conditions. Severity escalates -- no fallback.

PHASE NARRATIVE COMPLETE:
  Phase 1 behavioral driver named ([INERTIA COMPETITOR] referenced): YES / NO
  Phase 2 behavioral driver named ([INERTIA COMPETITOR] referenced): YES / NO
  Phase 3 behavioral driver named ([INERTIA COMPETITOR] referenced): YES / NO
  Trigger events named for all three phases:                         YES / NO

---

## STEP 2 -- STATUS QUO ANCHOR

SRE row is listed first. Bracket-token [INERTIA COMPETITOR] in column header =
Checkpoint A.

| Persona class | Prior [INERTIA COMPETITOR] behavior | Key capability expected to carry over | Most likely violated assumption |
|---------------|-------------------------------------|--------------------------------------|----------------------------------|
| SRE | | | |
| Support | | | |
| PM / UX | | | |
| C-01..C-04 (technical early adopters) | | | |
| C-05..C-08 (pragmatic mainstream) | | | |
| C-09..C-12 (enterprise/compliance) | | | |

---

## STEP 3 -- ASSUMPTION AUDIT

**Complete the SRE row first.**

Bracket-token [INERTIA COMPETITOR] in column header = Checkpoint B.

| # | Persona class | Incumbent [INERTIA COMPETITOR] behavior | Imported expectation | What this feature does instead | Resulting failure mode | Ticket # |
|---|---------------|----------------------------------------|---------------------|-------------------------------|----------------------|----------|

Ticket #: LEAVE BLANK -- assigned in Step 6b.

ASSUMPTION AUDIT COMPLETE:
  Rows documented:                                         [N]
  SRE row present:                                         YES / NO
  All 5 non-ID columns populated:                          YES / NO
  Column 2 cells reference [INERTIA COMPETITOR] by name:   YES / NO -> Checkpoint B
  Ticket IDs pending at Step 6b:                           [N] rows

---

## STEP 4 -- PHASE DISTRIBUTION TARGET

PHASE DISTRIBUTION TARGET:
  Phase 1 (Day 0-30):  [N] tickets
  Phase 2 (Day 31-60): [N] tickets
  Phase 3 (Day 61-90): [N] tickets
  Total:               [N] tickets

Constraints: Phase 1 >= 3. Phase 3 >= 1. Total >= 7.

---

## STEP 5 -- PERSONA VOICE TABLE (DIMENSION REGISTRY)

SRE row is listed first.

| Persona | Operational vocabulary | Frustration register | Framing conventions |
|---------|----------------------|---------------------|---------------------|
| SRE | (>= 2 specific terms) | (>= 2 specific phrases) | (>= 2 structural patterns) |
| Support | (>= 2 specific terms) | (>= 2 specific phrases) | (>= 2 structural patterns) |
| [other personas used] | (>= 2 specific terms) | (>= 2 specific phrases) | (>= 2 structural patterns) |

Dimension prefixes: operational= | frustration= | framing=

What disqualifies: role declarations, generic verbs, bare nouns.

---

## STEP 5b -- DIMENSION-LABEL REJECTION REGISTRY

**Per-category minimum commitment:**
  Category 1 (Format violations) minimum: 2 entries
  Category 2 (Value violations) minimum:  2 entries

Floor guarantee: 2 + 2 = 4 > 3.

REJECTION REGISTRY:

Category 1: R-01 (flat list), R-02 (same prefix twice), R-03 (count without naming)
Category 2: R-04 (role declarations), R-05 (generic verbs), R-06 (synonym pairs),
            R-07 (bare nouns)

REGISTRY COMPLETENESS CHECK:
  Category 1: [N] (>= 2) | Category 2: [N] (>= 2) | Total: [N] (>= 3) -> PASS / FAIL
  Floor guarantee: [N] + [N] = [sum], required > 3 -> PASS / FAIL

REGISTRY GATE:
  Per-category commitment honored:  YES / NO
  Floor guarantee sum > 3:          PASS / FAIL
  Dual-category coverage:           PASS / FAIL
  Registry applied during Step 7:   CONFIRMED

---

## STEP 5c -- SRE-WRITE-FIRST GATE

SRE-WRITE-FIRST GATE:
  SRE row position: row [N] of [total rows]
  SRE is first row: YES / NO  -> PASS / FAIL
  SRE body written first: CONFIRMED
  Gate verdict: PASS / FAIL

---

## STEP 6 -- TICKET SUMMARY TABLE AND VALIDATION TRACE

| # | Phase | Title | Category | Persona | Volume | Severity |
|---|-------|-------|----------|---------|--------|----------|

VALIDATION TRACE:
  Distinct categories:       [N] (>= 3)   -> PASS / FAIL
  Distinct personas:         [N] (>= 2)   -> PASS / FAIL
  P0 count:                  [N] (<= 1)   -> PASS / FAIL
  Low/medium volume entries: [N] (>= 1)   -> PASS / FAIL
  Total rows:                [N] (>= 7)   -> PASS / FAIL
  Phase distribution:
    Phase 1: [N] / target [N]             -> MATCH / MISMATCH
    Phase 2: [N] / target [N]             -> MATCH / MISMATCH
    Phase 3: [N] / target [N]             -> MATCH / MISMATCH
  Phase-severity consistent:              -> PASS / FAIL
  SRE-WRITE-FIRST GATE verdict:           PASS / FAIL
  Bracket-token: Step 2 YES/NO | Step 3 YES/NO -> PASS / FAIL

  CHECKPOINT MAP (C-36):
    Checkpoint A (Step 2 bracket-token): YES / NO
    Checkpoint B (Step 3 bracket-token): YES / NO
    Checkpoint C (>= 50% body coverage): YES / NO
    All labels echoed by name, binary probe: YES / NO
    -> CHECKPOINT MAP: COMPLETE / INCOMPLETE

  Overall: -> PASS / FAIL

---

## STEP 6b -- FORWARD-LINK

FORWARD-LINK GATE:
  Audit rows: [N] | Rows with Ticket #: [N] -> PASS / FAIL

---

## STEP 7 -- TICKET BODIES

Write SRE bodies first. For [A#N] tickets: reference [INERTIA COMPETITOR] verbatim.
Each body: >= 2 markers from DIFFERENT persona voice table columns.

### Ticket [N] [Phase N]: [Title]
**Traces to:** Assumption #[N]
**Body:** [2-5 sentences]
**Voice markers:** operational=[term] | frustration=[phrase]

---

TIER-SEQUENCING RULE (preamble): All TIER 1 gates must show PROCEED before TIER 2.

BIDIRECTIONAL LINKAGE VERIFICATION:

  TIER ARCHITECTURE SELF-CHECK:
  | Landmark | Expected location | Present | Result |
  |----------|-----------------|---------|--------|
  | TIER-SEQUENCING RULE | Preamble above block | YES/NO | PASS/FAIL |
  | -- TIER 1: Per-Pair -- | Before per-pair blocks | YES/NO | PASS/FAIL |
  | -- TIER 2: Block-Level -- | Before REVISION GATE | YES/NO | PASS/FAIL |

  -- TIER 1: Per-Pair Verification --
    Assumption #[N] -> Ticket [N]:
      Audit phrase: "[quote]" | Body evidence: "[quote]"
      Alignment: MATCH / MISMATCH | Gate: PROCEED | REVISE
  All TIER 1 PROCEED: YES / NO -> PASS / FAIL

  -- TIER 2: Block-Level Clearance --
  REVISION GATE:
    Mismatched pairs: [list/"none"] | Gate status: OPEN | CLOSED

---

## STEP 8 -- MARKER FORMAT AUDIT

MARKER FORMAT AUDIT:
  Total bodies: [N] | Bodies with >= 2 diff prefixes: [N]
  Coverage (>= 60%): [N]% -> PASS / FAIL | Overall: PASS / FAIL

---

## STEP 9 -- POST-GENERATION PHASE CONFIRMATION

PHASE CONFIRMATION:
  Ph1: [gen]/[tgt] | Ph2: [gen]/[tgt] | Ph3: [gen]/[tgt] -> MATCH / MISMATCH each

---

## STEP 10 -- GAP ANALYSIS TABLE

| # | Gap type | Specific artifact | Classification | Incumbent [INERTIA COMPETITOR] status | Phase first surfaces |
|---|----------|------------------|----------------|--------------------------------------|---------------------|

Minimum: 1 Doc row, 1 Design row, 1 Operational row.

---

## STEP 11 -- THRESHOLD CONFIRMATION

THRESHOLD CONFIRMATION:

C-14: [N]/[N] = [N]% (>= 60%) -> PASS / FAIL
C-16: [N]/[N] = [N]% (>= 60%) -> PASS / FAIL
C-12: [N]/[N] = [N]% (>= 60%) -> PASS / FAIL

C-31 | INERTIA COMPETITOR Propagation
  Preamble declaration present:     YES / NO  -> PASS / FAIL
  Propagation coverage (>= 50%):    [N]%      -> PASS / FAIL
  Step 10 cells use declared name:  YES / NO  -> PASS / FAIL

C-32 | SRE-First Ordering
  SRE first in Step 2: YES/NO | SRE first in Step 5: YES/NO  -> PASS / FAIL

C-33 | Bracket-Token Propagation
BLOCK-START:
  [INERTIA COMPETITOR] in Step 2 column header:               YES/NO
  [INERTIA COMPETITOR] in Step 3 column header:               YES/NO
  [INERTIA COMPETITOR] in Step 7 instruction clause:          YES/NO
  [INERTIA COMPETITOR] in Step 10 column header:              YES/NO
  >= 2 distinct table-header locations:                       YES/NO
  Scan-verifiability:                                         YES/NO -> PASS/FAIL
BLOCK-END: C-33 PASS / FAIL

C-34 | Propagation Chain Pre-Declaration
BLOCK-START:
  PROPAGATION CHAIN block in preamble:                        YES/NO
  All three checkpoints A/B/C named:                          YES/NO
  Checkpoint A satisfied:                                     YES/NO
  Checkpoint B satisfied:                                     YES/NO
  Checkpoint C satisfied:                                     YES/NO
  Completeness verifiable without traversal:                  YES/NO -> PASS/FAIL
BLOCK-END: C-34 PASS / FAIL

C-35 | SRE-Write-First Enforcement Gate
BLOCK-START:
  SRE-WRITE-FIRST GATE block present at Step 5c:              YES/NO
  Gate produces explicit PASS/FAIL verdict:                   YES/NO
  Gate carries "do not proceed" halt instruction:             YES/NO
  Gate was invoked before any body:                           YES/NO
  Gate verdict:                                               PASS / FAIL
  Advisory upgraded to binding enforcement gate:              YES/NO -> PASS/FAIL
BLOCK-END: C-35 PASS / FAIL

C-36 | Checkpoint-Mapped VALIDATION TRACE
  CHECKPOINT MAP present in Step 6:            YES/NO -> PASS/FAIL
  Checkpoint A echoed by label, binary probe:  YES/NO -> PASS/FAIL
  Checkpoint B echoed by label, binary probe:  YES/NO -> PASS/FAIL
  Checkpoint C echoed by label, binary probe:  YES/NO -> PASS/FAIL
  All probes binary:                           YES/NO -> PASS/FAIL

C-37 | Cross-Criterion Synergy Sub-Blocks
  C-33 block has scan-verifiability line:      YES/NO -> PASS/FAIL
  C-34 block has scan-verifiability line:      YES/NO -> PASS/FAIL
  C-35 block has scan-verifiability line:      YES/NO -> PASS/FAIL

CROSS-CRITERION SYNERGY DECLARATION (LAYER 2 of 2) [SYNERGY-ANCHOR: C33xC34]
(C-38 + C-39 candidates):
  Synergy pair: C-33 bracket-token placement + C-34 no-traversal verifiability
  C-33 token at Checkpoint A (Step 2):              YES/NO
  C-33 token at Checkpoint B (Step 3):              YES/NO
  Checkpoint A grep-detectable:                     YES/NO
  Checkpoint B grep-detectable:                     YES/NO
  C-34 no-traversal is structural:                  YES/NO
  Degradation declared (absent = prose required):   YES/NO
  Two-layer presence check (C-38):
    LAYER 1 present (preamble, labeled LAYER 1 of 2): YES/NO
    LAYER 2 present (this block, labeled LAYER 2 of 2): YES/NO
    Both layers confirmed:                            YES/NO -> PASS/FAIL
  Grep-closed loop (C-39):
    [SYNERGY-ANCHOR: C33xC34] in preamble LAYER 1:    YES/NO
    [SYNERGY-ANCHOR: C33xC34] in this LAYER 2 block:  YES/NO
    Single grep finds both sites:                     YES/NO -> PASS/FAIL
  -> CROSS-CRITERION SYNERGY: STRUCTURAL / ABSENT -> PASS/FAIL

Summary:
  C-14 / C-16 / C-12:       PASS / FAIL each
  C-31 through C-37:         PASS / FAIL each
  C-38 cand. two-layer:      PASS / FAIL
  C-39 cand. grep-closed:    PASS / FAIL
  Overall: PASS (all) / FAIL (one or more)
```

---

## V-05: Full Synthesis -- Two-Layer + Grep-Closed + Falsifiable Degradation (C-38 + C-39 + C-40)

**Axes:** All three combined. The LAYER labels (C-38), grep anchor (C-39), and
DEGRADATION CLAUSE (C-40) are all present simultaneously in both the preamble note
and the Step 11 declaration. This is the strongest expected satisfier: a scorer can
confirm two-location presence via LAYER labels, navigate between sites via one grep,
and audit the synergy as a falsifiable logical claim via the if/then clause.

**Hypothesis:** The three mechanisms address three distinct verifiability dimensions:
- C-38 (two-layer): WHERE is the synergy declared? (both locations labeled)
- C-39 (grep-closed): HOW does a scorer find both sites? (one grep, one anchor)
- C-40 (falsifiable): WHAT happens when synergy breaks? (explicit if/then condition)

All three can be satisfied simultaneously without conflict; V-05 is the expected
ceiling for R14 scoring.

---

```
# listen-support: Predict First-90-Day Support Tickets

Work through each step in order. Do not skip steps. Do not combine steps.

---

INERTIA COMPETITOR: [name the specific product the target personas currently use for
this workflow -- one product name, grep-checkable, no generic labels like "legacy tool"
or "the incumbent"]

This name is a constant. It appears below as the literal bracket-variable token
[INERTIA COMPETITOR] embedded in table column headers and step instruction action
clauses. Every occurrence is detectable by scanning for [INERTIA COMPETITOR].

PROPAGATION CHAIN:
  Checkpoint A: STATUS QUO ANCHOR (Step 2) -- column header "Prior [INERTIA COMPETITOR]
    behavior" uses the bracket-token; column 2 cells name this product explicitly
  Checkpoint B: ASSUMPTION AUDIT (Step 3) -- column header "Incumbent [INERTIA COMPETITOR]
    behavior" uses the bracket-token; column 2 cells cite this product by name
  Checkpoint C: Ticket bodies with [A#N] traces (Step 7) -- bodies linked to assumption
    audit rows contain this product name verbatim; coverage >= 50% of linked bodies

Completeness is verifiable from this declaration: (A) grep Step 2 header, (B) grep
Step 3 header, (C) count bodies. All three must be satisfied before submitting.

CROSS-CRITERION SYNERGY NOTE (LAYER 1 of 2) [SYNERGY-ANCHOR: C33xC34]:
  C-33 bracket-tokens at Checkpoint A (Step 2 header) and Checkpoint B (Step 3 header)
  make C-34's declared checkpoints grep-detectable. This is what makes C-34's
  "completeness verifiable without traversal" property structural rather than
  aspirational. The CROSS-CRITERION SYNERGY DECLARATION (LAYER 2 of 2) in Step 11
  confirms this dependency is satisfied. Two-layer synergy: this note is LAYER 1; the
  Step 11 declaration is LAYER 2. Both must be present.
  Grep route: search for [SYNERGY-ANCHOR: C33xC34] to find LAYER 1 (here) and LAYER 2
  (Step 11). One grep closes the declaration-to-trace loop.
  DEGRADATION CLAUSE (falsifiable):
    IF C-33 bracket-token is absent from a checkpoint header,
    THEN that checkpoint requires prose interpretation to verify,
    AND C-34's "completeness verifiable without traversal" property degrades to
      aspirational for that checkpoint.
    Failure state: any checkpoint header missing [INERTIA COMPETITOR] bracket-token
    causes that checkpoint's no-traversal claim to become unverifiable by grep.
    This clause is falsifiable: the trigger (token absent) is binary and testable;
    the consequence (prose required) is observable; the C-34 cascade is named.

---

## STEP 1 -- PHASE-SEVERITY GRADIENT PRIOR

Phase 1 (Day 0-30): P2/P3. P0 reserved for activation blockers affecting all users.
Phase 2 (Day 31-60): P1/P2. P0 exceptional: data loss or workflow corruption only.
Phase 3 (Day 61-90): P0/P1. No fallback at scale. P3 essentially absent.

PHASE-SEVERITY PRIOR:
  Phase 1 (Day 0-30):  typical P2/P3; P0 only for activation blockers affecting all users
  Phase 2 (Day 31-60): typical P1/P2; P0 exceptional (data loss or workflow corruption)
  Phase 3 (Day 61-90): typical P0/P1; P3 rare (users have exhausted workarounds)

---

## STEP 1b -- PHASE NARRATIVE

**Phase 1 (Day 0-30) -- First contact:**
Users explore the feature while keeping [INERTIA COMPETITOR] active as a safety net.
Each step is compared against [INERTIA COMPETITOR] behavior. Trigger event: first
divergence -- setup friction, missing docs, onboarding gaps. Tickets: high volume,
low severity.

**Phase 2 (Day 31-60) -- Committed trial:**
Users have invested real workflows; some migrated, some still in [INERTIA COMPETITOR].
Trigger event: committed workflow hits a blocking gap that works in [INERTIA COMPETITOR]
but fails here. Partial-migration friction: no simple revert.

**Phase 3 (Day 61-90) -- Operational dependency:**
[INERTIA COMPETITOR] is no longer available. Trigger event: blocking failure under
production conditions. Severity escalates -- no fallback exists.

PHASE NARRATIVE COMPLETE:
  Phase 1 behavioral driver named ([INERTIA COMPETITOR] referenced): YES / NO
  Phase 2 behavioral driver named ([INERTIA COMPETITOR] referenced): YES / NO
  Phase 3 behavioral driver named ([INERTIA COMPETITOR] referenced): YES / NO
  Trigger events named for all three phases:                         YES / NO

---

## STEP 2 -- STATUS QUO ANCHOR

SRE row is listed first. Bracket-token [INERTIA COMPETITOR] in column header =
Checkpoint A of PROPAGATION CHAIN.

| Persona class | Prior [INERTIA COMPETITOR] behavior | Key capability expected to carry over | Most likely violated assumption |
|---------------|-------------------------------------|--------------------------------------|----------------------------------|
| SRE | | | |
| Support | | | |
| PM / UX | | | |
| C-01..C-04 (technical early adopters) | | | |
| C-05..C-08 (pragmatic mainstream) | | | |
| C-09..C-12 (enterprise/compliance) | | | |

Column 4 (violated assumption) feeds Step 3.

---

## STEP 3 -- ASSUMPTION AUDIT

**Complete the SRE row first.** SRE tickets determine the severity ceiling.

Bracket-token [INERTIA COMPETITOR] in column header = Checkpoint B of PROPAGATION CHAIN.
Cell values must use the declared name -- no generic substitution.

| # | Persona class | Incumbent [INERTIA COMPETITOR] behavior | Imported expectation | What this feature does instead | Resulting failure mode | Ticket # |
|---|---------------|----------------------------------------|---------------------|-------------------------------|----------------------|----------|

Ticket #: LEAVE BLANK -- assigned in Step 6b. Complete at least 1 row.

ASSUMPTION AUDIT COMPLETE:
  Rows documented:                                         [N]
  SRE row present:                                         YES / NO
  All 5 non-ID columns populated:                          YES / NO
  Column 2 cells reference [INERTIA COMPETITOR] by name:   YES / NO -> Checkpoint B
  Ticket IDs pending at Step 6b:                           [N] rows

---

## STEP 4 -- PHASE DISTRIBUTION TARGET

PHASE DISTRIBUTION TARGET:
  Phase 1 (Day 0-30):  [N] tickets   -- first contact, [INERTIA COMPETITOR] comparison
  Phase 2 (Day 31-60): [N] tickets   -- committed trial, migration edge cases
  Phase 3 (Day 61-90): [N] tickets   -- operational dependency, no fallback
  Total:               [N] tickets

Constraints: Phase 1 >= 3. Phase 3 >= 1. Total >= 7. All three phases non-zero.

---

## STEP 5 -- PERSONA VOICE TABLE (DIMENSION REGISTRY)

SRE row is listed first. The SRE-WRITE-FIRST GATE in Step 5c verifies this position.

| Persona | Operational vocabulary | Frustration register | Framing conventions |
|---------|----------------------|---------------------|---------------------|
| SRE | (>= 2 specific terms) | (>= 2 specific phrases) | (>= 2 structural patterns) |
| Support | (>= 2 specific terms) | (>= 2 specific phrases) | (>= 2 structural patterns) |
| [other personas used] | (>= 2 specific terms) | (>= 2 specific phrases) | (>= 2 structural patterns) |

Dimension prefixes: operational= | frustration= | framing=

What disqualifies: role declarations ("As an SRE"), generic verbs ("noticed", "tried"),
bare nouns ("logs", "data", "error").

---

## STEP 5b -- DIMENSION-LABEL REJECTION REGISTRY

**Per-category minimum commitment:**
  Category 1 (Format violations) minimum: 2 entries
  Category 2 (Value violations) minimum:  2 entries

Floor guarantee: 2 + 2 = 4 > 3.

REJECTION REGISTRY:

Category 1: R-01 (flat list), R-02 (same prefix twice), R-03 (count without naming)
Category 2: R-04 (role declarations), R-05 (generic verbs), R-06 (synonym pairs),
            R-07 (bare nouns)

REGISTRY COMPLETENESS CHECK:
  Category 1: [N] (>= 2) | Category 2: [N] (>= 2) | Total: [N] (>= 3) -> PASS / FAIL
  Floor guarantee: [N] + [N] = [sum], required > 3 -> PASS / FAIL

REGISTRY GATE:
  Per-category commitment honored:  YES / NO -> must be YES
  Floor guarantee sum > 3:          PASS / FAIL
  Dual-category coverage:           PASS / FAIL
  Registry applied during Step 7:   CONFIRMED

Do not write any ticket body until REGISTRY GATE shows all conditions met.

---

## STEP 5c -- SRE-WRITE-FIRST GATE

This gate is the binding boundary between the PERSONA VOICE TABLE and ticket body
writing. Do not write any ticket body until this gate shows PASS.

SRE-WRITE-FIRST GATE:
  SRE row position in PERSONA VOICE TABLE (Step 5): row [N] of [total rows]
  SRE is the first row in PERSONA VOICE TABLE:       YES / NO  -> PASS / FAIL
  SRE body will be the first body written in Step 7: CONFIRMED
  Gate verdict:                                      PASS / FAIL

If FAIL: rebuild the PERSONA VOICE TABLE with SRE as row 1. Re-run this gate.

Do not advance to Step 6 with SRE-WRITE-FIRST GATE verdict = FAIL.

---

## STEP 6 -- TICKET SUMMARY TABLE AND VALIDATION TRACE

| # | Phase | Title | Category | Persona | Volume | Severity |
|---|-------|-------|----------|---------|--------|----------|

Allowed values:
- Phase: Phase 1 | Phase 2 | Phase 3
- Category: how-to | bug | feature-request | config | integration
- Persona: Support | SRE | PM | UX | C-01 through C-12
- Volume: high | medium | low
- Severity: P0 | P1 | P2 | P3

After completing the table, run the full validation trace:

VALIDATION TRACE:
  Distinct categories:                    [N] (>= 3)              -> PASS / FAIL
  Distinct personas:                      [N] (>= 2)              -> PASS / FAIL
  P0 count:                               [N] (<= 1)              -> PASS / FAIL
  Low/medium volume entries:              [N] (>= 1)              -> PASS / FAIL
  Total rows:                             [N] (>= 7)              -> PASS / FAIL
  Phase distribution:
    Phase 1: [N] / target [N]                                     -> MATCH / MISMATCH
    Phase 2: [N] / target [N]                                     -> MATCH / MISMATCH
    Phase 3: [N] / target [N]                                     -> MATCH / MISMATCH
  All personas in voice table:            YES / NO                -> PASS / FAIL
  >= 1 ticket linked to audit row:        YES / NO                -> PASS / FAIL
  Phase-severity consistent:
    Phase 1 (P2/P3): [list] | Phase 2 (P1/P2): [list] | Phase 3 (P0/P1): [list]
    -> PASS / FAIL
  SRE first in Step 2: YES/NO | SRE first in Step 5: YES/NO       -> PASS / FAIL
  SRE-WRITE-FIRST GATE verdict (Step 5c):  PASS / FAIL            -> PASS / FAIL
  SRE in audit: YES/NO | SRE ticket in table: YES/NO              -> PASS / FAIL
  Bracket-token propagation:
    [INERTIA COMPETITOR] in Step 2 header: YES/NO -> PASS / FAIL
    [INERTIA COMPETITOR] in Step 3 header: YES/NO -> PASS / FAIL
    [INERTIA COMPETITOR] in Step 7 instr:  YES/NO -> PASS / FAIL
    [INERTIA COMPETITOR] in Step 10 header:YES/NO -> PASS / FAIL

  CHECKPOINT MAP (C-36):
    Checkpoint A declared in preamble -- location: Step 2 column header
      Checkpoint A satisfied (bracket-token in Step 2 header): YES / NO
    Checkpoint B declared in preamble -- location: Step 3 column header
      Checkpoint B satisfied (bracket-token in Step 3 header): YES / NO
    Checkpoint C declared in preamble -- location: >= 50% linked body coverage
      Checkpoint C satisfied (body coverage >= 50%):           YES / NO
    All declared checkpoint labels echoed by name:             YES / NO
    All three checkpoint probes binary:                        YES / NO
    -> CHECKPOINT MAP: COMPLETE / INCOMPLETE

  Overall:                                                     -> PASS / FAIL

Do not proceed to Step 6b with VALIDATION TRACE showing FAIL.

---

## STEP 6b -- FORWARD-LINK

Go back to Step 3. For every assumption audit row, fill in the Ticket # column.

FORWARD-LINK GATE:
  Assumption audit rows total: [N] | Rows with Ticket # assigned: [N] -> PASS / FAIL
  All Ticket # values exist in table: YES / NO -> PASS / FAIL | Overall: PASS / FAIL

---

## STEP 7 -- TICKET BODIES WITH DIMENSION-LABELED MARKER CITATIONS

Write SRE bodies first. Then Support, PM/UX, customer personas. Do not open any body
with a persona declaration.

For tickets with [A#N] tag: body must reference [INERTIA COMPETITOR] verbatim --
satisfies Checkpoint C of the PROPAGATION CHAIN.

Each body: >= 2 markers from DIFFERENT columns of the persona's voice table row.
Clear every marker against REJECTION REGISTRY before citing.

### Ticket [N] [Phase N]: [Title from table]
**Traces to:** Assumption #[N]   <- audit-linked only; omit for net-new
**Body:** [2-5 sentences in the persona's actual voice]
**Voice markers:** operational=[term] | frustration=[phrase]

---

TIER-SEQUENCING RULE (preamble):
  All TIER 1 gates must show PROCEED before TIER 2 is evaluated.

BIDIRECTIONAL LINKAGE VERIFICATION:

  TIER ARCHITECTURE SELF-CHECK:
  | Landmark | Expected location | Present | Result |
  |----------|-----------------|---------|--------|
  | TIER-SEQUENCING RULE | Preamble above block | YES/NO | PASS/FAIL |
  | -- TIER 1: Per-Pair -- | Before per-pair blocks | YES/NO | PASS/FAIL |
  | -- TIER 2: Block-Level -- | Before REVISION GATE | YES/NO | PASS/FAIL |
  All three PASS: YES -> proceed | Any FAIL: halt

  Forward: [N]/[N] rows have Ticket # | Backward: [N] bodies have "Traces to:"

  -- TIER 1: Per-Pair Verification --
    Assumption #[N] -> Ticket [N]:
      Audit phrase: "[quote -- min 5 words]"
      Body evidence: "[quote -- min 5 words]"
      Alignment: MATCH / MISMATCH | Gate: PROCEED | REVISE
    [repeat for each pair]
  All TIER 1 PROCEED: YES / NO -> PASS / FAIL

  -- TIER 2: Block-Level Clearance --
  REVISION GATE:
    Mismatched pairs: [list/"none"] | Gate status: OPEN | CLOSED
    Do not advance to Step 8 with Gate status = CLOSED.

  Overall: PASS / FAIL

---

## STEP 8 -- MARKER FORMAT AUDIT

MARKER FORMAT AUDIT:
  Total bodies: [N] | Bodies with >= 2 diff prefixes: [N]
  Flat-list (R-01): [N]->0 | Same-dim (R-02): [N]->0 | Registry-violating: [N]->0
  Coverage (>= 60%): [N]% -> PASS / FAIL | Overall: PASS / FAIL

---

## STEP 9 -- POST-GENERATION PHASE CONFIRMATION

PHASE CONFIRMATION:
  Ph1: [gen]/[tgt] | Ph2: [gen]/[tgt] | Ph3: [gen]/[tgt] | Total: [gen]/[tgt]
  -> MATCH / MISMATCH each

---

## STEP 10 -- GAP ANALYSIS TABLE

| # | Gap type | Specific artifact | Classification | Incumbent [INERTIA COMPETITOR] status | Phase first surfaces |
|---|----------|------------------|----------------|--------------------------------------|---------------------|

Minimum: 1 Doc row, 1 Design row, 1 Operational row.

---

## STEP 11 -- THRESHOLD CONFIRMATION

THRESHOLD CONFIRMATION:

C-14: [N]/[N] = [N]% (>= 60%) -> PASS / FAIL
C-16: [N]/[N] = [N]% (>= 60%) -> PASS / FAIL
C-12: [N]/[N] = [N]% (>= 60%) -> PASS / FAIL

C-31 | INERTIA COMPETITOR Propagation
  Preamble declaration present before Step 1:     YES / NO  -> PASS / FAIL
  Bodies containing declared name verbatim:       [N] / [N]
  Propagation coverage (>= 50%):                  [N]%      -> PASS / FAIL
  Step 10 Incumbent cells use declared name:      YES / NO  -> PASS / FAIL

C-32 | SRE-First Ordering
  SRE first in Step 2: YES/NO | SRE first in Step 5: YES/NO
  SRE in audit: YES/NO | SRE ticket in table: YES/NO        -> PASS / FAIL

C-33 | Bracket-Token Propagation
BLOCK-START:
  [INERTIA COMPETITOR] in Step 2 column header (Checkpoint A anchor): YES/NO
  [INERTIA COMPETITOR] in Step 3 column header (Checkpoint B anchor): YES/NO
  [INERTIA COMPETITOR] in Step 7 instruction clause:                  YES/NO
  [INERTIA COMPETITOR] in Step 10 column header:                      YES/NO
  >= 2 distinct table-header bracket-token locations:                 YES/NO
  Scan-verifiability (detectable by bracket-scan, not prose):         YES/NO -> PASS/FAIL
BLOCK-END: C-33 PASS / FAIL

C-34 | Propagation Chain Pre-Declaration
BLOCK-START:
  PROPAGATION CHAIN block present in preamble before Step 1:          YES/NO
  All three checkpoints A/B/C named with locations:                   YES/NO
  Checkpoint A satisfied (Step 2 header has bracket-token):           YES/NO
  Checkpoint B satisfied (Step 3 header has bracket-token):           YES/NO
  Checkpoint C satisfied (>= 50% linked body coverage):               YES/NO
  Completeness verifiable from preamble without traversal:            YES/NO -> PASS/FAIL
BLOCK-END: C-34 PASS / FAIL

C-35 | SRE-Write-First Enforcement Gate
BLOCK-START:
  SRE-WRITE-FIRST GATE block present at Step 5c boundary:             YES/NO
  Gate produces explicit PASS/FAIL verdict:                           YES/NO
  Gate carries "do not proceed" halt instruction:                     YES/NO
  Gate was invoked before any body was written:                       YES/NO
  Gate verdict in this output:                                        PASS / FAIL
  Advisory write-first upgraded to binding enforcement gate:          YES/NO -> PASS/FAIL
BLOCK-END: C-35 PASS / FAIL

C-36 | Checkpoint-Mapped VALIDATION TRACE
  CHECKPOINT MAP sub-section present in Step 6:            YES/NO -> PASS/FAIL
  Checkpoint A echoed by label name with YES/NO probe:     YES/NO -> PASS/FAIL
  Checkpoint B echoed by label name with YES/NO probe:     YES/NO -> PASS/FAIL
  Checkpoint C echoed by label name with YES/NO probe:     YES/NO -> PASS/FAIL
  "All declared checkpoint labels echoed" confirmation:    YES/NO -> PASS/FAIL
  All three probes are binary (no partial/conditional):    YES/NO -> PASS/FAIL

C-37 | Cross-Criterion Synergy Sub-Blocks
  C-33 block has scan-verifiability YES/NO as final line:  YES/NO -> PASS/FAIL
  C-34 block has scan-verifiability YES/NO as final line:  YES/NO -> PASS/FAIL
  C-35 block has scan-verifiability YES/NO as final line:  YES/NO -> PASS/FAIL

CROSS-CRITERION SYNERGY DECLARATION (LAYER 2 of 2) [SYNERGY-ANCHOR: C33xC34]
(C-38 + C-39 + C-40 candidates):
  Synergy pair declared: C-33 bracket-token placement + C-34 no-traversal verifiability
  C-33 bracket-token present at Checkpoint A header (Step 2):          YES/NO
  C-33 bracket-token present at Checkpoint B header (Step 3):          YES/NO
  Checkpoint A grep-detectable by bracket-scan (not prose):            YES/NO
  Checkpoint B grep-detectable by bracket-scan (not prose):            YES/NO
  C-34 "completeness verifiable without traversal" -- structural basis:
    Answer is YES because bracket-tokens are the mechanism (not assertion): YES/NO
  Two-layer presence check (C-38):
    LAYER 1 present (preamble note labeled LAYER 1 of 2):              YES/NO
    LAYER 2 present (this Step 11 block labeled LAYER 2 of 2):         YES/NO
    Both layers confirmed:                                             YES/NO -> PASS/FAIL
  Grep-closed loop (C-39):
    [SYNERGY-ANCHOR: C33xC34] in preamble LAYER 1:                     YES/NO
    [SYNERGY-ANCHOR: C33xC34] in this LAYER 2 block:                   YES/NO
    Single grep for SYNERGY-ANCHOR finds both declaration + echo site: YES/NO -> PASS/FAIL
  DEGRADATION CLAUSE (falsifiable, C-40):
    Trigger condition: C-33 bracket-token absent from a checkpoint header
    Immediate consequence: that checkpoint requires prose interpretation
    C-34 cascade: no-traversal property degrades to aspirational for that checkpoint
    Failure state named (specific, testable):                          YES/NO
    If/then structure present (condition + consequence + cascade):     YES/NO
    Clause labeled falsifiable:                                        YES/NO
    Preamble DEGRADATION CLAUSE also present (LAYER 1 echo):           YES/NO -> PASS/FAIL
  -> CROSS-CRITERION SYNERGY: STRUCTURAL / ABSENT -> PASS/FAIL

Summary:
  C-14 / C-16 / C-12:       PASS / FAIL each
  C-31 name propagation:     PASS / FAIL
  C-32 SRE-first:            PASS / FAIL
  C-33 bracket-token:        PASS / FAIL
  C-34 chain pre-decl:       PASS / FAIL
  C-35 enforce gate:         PASS / FAIL
  C-36 checkpoint map:       PASS / FAIL
  C-37 synergy sub-blocks:   PASS / FAIL
  C-38 cand. two-layer:      PASS / FAIL
  C-39 cand. grep-closed:    PASS / FAIL
  C-40 cand. falsifiable:    PASS / FAIL
  Overall: PASS (all) / FAIL (one or more)

If any threshold shows FAIL, identify the specific shortfall, revise, and re-run
this block before submitting.
```
