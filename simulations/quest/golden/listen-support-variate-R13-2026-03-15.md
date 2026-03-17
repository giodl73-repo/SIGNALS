# listen-support Round 13 -- Skill Body Prompt Variations

**Date:** 2026-03-15
**Rubric target:** v13 (37 criteria -- C-01 through C-37)
**Base:** V-05 R12 (C-01 through C-35 ceiling; bracket-token + propagation chain + SRE gate all active)

**Variation axes selected** (3 single-axis, then 2 combined):

1. **Checkpoint-Mapped VALIDATION TRACE (C-36 candidate)** -- Expand the VALIDATION TRACE
   block to include a named CHECKPOINT MAP sub-section that echoes each checkpoint label
   (A, B, C) from the PROPAGATION CHAIN verbatim, with a binary YES/NO probe per label.
   Goes beyond C-34 (preamble declares checkpoints) by making the trace echo each label
   back by name. (V-01)

2. **Per-Criterion THRESHOLD CONFIRMATION Sub-Blocks (C-37a candidate)** -- Restructure
   the THRESHOLD CONFIRMATION block so that C-33, C-34, and C-35 each receive their own
   named BLOCK-START / BLOCK-END sub-block with >= 6 verification lines and an explicit
   scan-verifiability YES/NO line, rather than a flat list under a shared section. (V-02)

3. **Cross-Criterion Structural Synergy Declaration (C-37b candidate)** -- Add a
   CROSS-CRITERION SYNERGY DECLARATION sub-block to the THRESHOLD CONFIRMATION that
   names the structural dependency: C-33 bracket-tokens embedded in column headers make
   C-34's declared checkpoints A and B grep-detectable, so the "completeness verifiable
   without traversal" property (C-34 line 6) is answerable YES structurally, not
   aspirationally. The declaration also states what fails if synergy is absent. (V-03)

4. **V-01 + V-02 combined** -- Checkpoint-mapped VALIDATION TRACE + per-criterion
   THRESHOLD CONFIRMATION sub-blocks. Independent mechanisms: trace mapping addresses
   the echo gap in VALIDATION TRACE; per-criterion sub-blocks address granularity in
   THRESHOLD CONFIRMATION. (V-04)

5. **Full synthesis** -- All three axes: checkpoint map + per-criterion sub-blocks +
   cross-criterion synergy declaration. (V-05)

**Axes NOT explored this round (deferred):**
- Role sequence (SRE-first enforced by gate from R12; further sequencing deferred)
- Output format (ticket table format stable)
- Phrasing register (stable at current register from R10)

**R13 criterion hypothesis matrix:**

| Criterion candidate | V-01 | V-02 | V-03 | V-04 | V-05 |
|--------------------|------|------|------|------|------|
| C-01 through C-35 (all prior -- active baseline) | YES | YES | YES | YES | YES |
| C-36 candidate: Checkpoint-Mapped VALIDATION TRACE with per-label YES/NO | YES | -- | -- | YES | YES |
| C-37 candidate: Per-criterion sub-blocks with scan-verifiability YES/NO + cross-criterion synergy | -- | YES | YES | YES | YES |

**Note on C-37 decomposition:** C-37 bundles two mechanisms that appeared together in V-05 R12:
per-criterion sub-blocks (V-02) and cross-criterion synergy (V-03). V-02 tests whether
sub-blocks alone satisfy C-37. V-03 tests whether synergy alone satisfies C-37. V-05
tests both together as the strongest expected satisfier.

**Axes carried from R12 V-05 (active in all R13 variations as baseline):**
- INERTIA COMPETITOR preamble with bracket-variable token declaration (C-31 / C-33)
- PROPAGATION CHAIN sub-block with A/B/C labels pre-declared in preamble (C-34)
- SRE-WRITE-FIRST GATE block at Step 5c -> Step 7 boundary (C-35)
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

## V-01: Single-Axis -- Checkpoint-Mapped VALIDATION TRACE (C-36)

**Axis:** The VALIDATION TRACE block in Step 6 gains a named CHECKPOINT MAP sub-section
that iterates through each checkpoint declared in the preamble PROPAGATION CHAIN (A, B, C)
by label, names its declared location, and probes it with a binary YES/NO. The checkpoint
label is echoed verbatim from the preamble declaration -- "Checkpoint A", "Checkpoint B",
"Checkpoint C" -- not reworded or merged with other lines.

**Probe (C-36 candidate):** C-17 requires a VALIDATION TRACE block to be present. C-34
requires checkpoints to be pre-declared in the preamble. Neither criterion requires the
trace to echo back the declared checkpoint labels by name. A scorer verifying C-34
compliance currently reads the VALIDATION TRACE's "Propagation chain completeness" block
and checks whether each checkpoint appears satisfied -- but the connection between the
label declared in the preamble and the line in the trace is implicit. The CHECKPOINT MAP
closes this gap: it echoes each label verbatim, making the preamble-to-trace connection
explicit and binary. A scorer can answer "are all declared checkpoint labels present in
the trace with individual YES/NO probes?" by scanning for the checkpoint label strings
("Checkpoint A:", "Checkpoint B:", "Checkpoint C:") rather than interpreting whether a
semantically equivalent line exists.

**Hypothesis:** When the CHECKPOINT MAP sub-section echoes checkpoint labels verbatim,
the trace becomes structurally complete relative to the preamble declaration: every
declared label has a corresponding trace line, and the line is binary. C-36 would require
the CHECKPOINT MAP sub-section to be present in VALIDATION TRACE with at least 3 label
echoes (one per declared checkpoint), each with a YES/NO probe, and a final
"All declared checkpoints mapped with YES/NO" confirmation line.

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

---

## STEP 1 -- PHASE-SEVERITY GRADIENT PRIOR

Phase 1 (Day 0-30): P2/P3. Workarounds exist; no committed production data. P0
reserved for activation blockers affecting all users simultaneously.

Phase 2 (Day 31-60): P1/P2. Workarounds have real cost. P0 exceptional: data loss
or workflow corruption under real load only.

Phase 3 (Day 61-90): P0/P1. No fallback at scale. P3 essentially absent.

```
PHASE-SEVERITY PRIOR:
  Phase 1 (Day 0-30):  typical P2/P3; P0 only for activation blockers affecting all users
  Phase 2 (Day 31-60): typical P1/P2; P0 exceptional (data loss or workflow corruption)
  Phase 3 (Day 61-90): typical P0/P1; P3 rare (users have exhausted workarounds)
```

---

## STEP 1b -- PHASE NARRATIVE

**Phase 1 (Day 0-30) -- First contact:**
Users are exploring the feature while keeping [INERTIA COMPETITOR] active as a safety
net. Each step is compared against [INERTIA COMPETITOR] behavior. Trigger event: first
contact with a behavior that diverges from [INERTIA COMPETITOR] -- setup friction,
missing documentation, onboarding gaps. Tickets driven by volume but low severity.

**Phase 2 (Day 31-60) -- Committed trial:**
Users have invested real workflows; some migrated, some still in [INERTIA COMPETITOR].
Trigger event: first time a committed workflow hits a blocking gap -- a config
combination that works in [INERTIA COMPETITOR] but fails here. Partial-migration
friction: no simple revert, but feature coverage incomplete.

**Phase 3 (Day 61-90) -- Operational dependency:**
[INERTIA COMPETITOR] is no longer available for this workflow. Trigger event: blocking
failure under production conditions. Severity escalates -- no fallback exists.

```
PHASE NARRATIVE COMPLETE:
  Phase 1 behavioral driver named ([INERTIA COMPETITOR] referenced): YES / NO
  Phase 2 behavioral driver named ([INERTIA COMPETITOR] referenced): YES / NO
  Phase 3 behavioral driver named ([INERTIA COMPETITOR] referenced): YES / NO
  Trigger events named for all three phases:                         YES / NO
```

---

## STEP 2 -- STATUS QUO ANCHOR

SRE row is listed first. Column 2 uses the INERTIA COMPETITOR name from the preamble.
The bracket-token [INERTIA COMPETITOR] in the column header is Checkpoint A.

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
[INERTIA COMPETITOR] in the column header is Checkpoint B. Cell values must use the
declared name -- no generic substitution.

| # | Persona class | Incumbent [INERTIA COMPETITOR] behavior | Imported expectation | What this feature does instead | Resulting failure mode | Ticket # |
|---|---------------|----------------------------------------|---------------------|-------------------------------|----------------------|----------|

Ticket #: LEAVE BLANK -- assigned in Step 6b. Complete at least 1 row.

```
ASSUMPTION AUDIT COMPLETE:
  Rows documented:                                         [N]
  SRE row present:                                         YES / NO
  All 5 non-ID columns populated:                          YES / NO
  Column 2 cells reference [INERTIA COMPETITOR] by name:   YES / NO -> Checkpoint B
  Ticket IDs pending at Step 6b:                           [N] rows
```

---

## STEP 4 -- PHASE DISTRIBUTION TARGET

Declare the binding target consistent with the Phase Narrative from Step 1b.

```
PHASE DISTRIBUTION TARGET:
  Phase 1 (Day 0-30):  [N] tickets   -- first contact, [INERTIA COMPETITOR] comparison
  Phase 2 (Day 31-60): [N] tickets   -- committed trial, migration edge cases
  Phase 3 (Day 61-90): [N] tickets   -- operational dependency, no fallback
  Total:               [N] tickets
```

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

```
REGISTRY GATE:
  Per-category commitment honored:  YES / NO -> must be YES
  Floor guarantee sum > 3:          PASS / FAIL
  Dual-category coverage:           PASS / FAIL
  Registry applied during Step 7:   CONFIRMED
```

Do not write any ticket body until REGISTRY GATE shows all conditions met.

---

## STEP 5c -- SRE-WRITE-FIRST GATE

This gate is the binding boundary between the PERSONA VOICE TABLE and ticket body
writing. Do not write any ticket body until this gate shows PASS.

```
SRE-WRITE-FIRST GATE:
  SRE row position in PERSONA VOICE TABLE (Step 5): row [N] of [total rows]
  SRE is the first row in PERSONA VOICE TABLE:       YES / NO  -> PASS / FAIL
  SRE body will be the first body written in Step 7: CONFIRMED
  Gate verdict:                                      PASS / FAIL
```

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

```
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

  CHECKPOINT MAP (C-36 candidate):
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
```

Do not proceed to Step 6b with VALIDATION TRACE showing FAIL.

---

## STEP 6b -- FORWARD-LINK

Go back to Step 3. For every assumption audit row, fill in the Ticket # column.

```
FORWARD-LINK GATE:
  Assumption audit rows total: [N] | Rows with Ticket # assigned: [N] -> PASS / FAIL
  All Ticket # values exist in table: YES / NO -> PASS / FAIL | Overall: PASS / FAIL
```

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

```
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
```

---

## STEP 8 -- MARKER FORMAT AUDIT

```
MARKER FORMAT AUDIT:
  Total bodies: [N] | Bodies with >= 2 diff prefixes: [N]
  Flat-list (R-01): [N]->0 | Same-dim (R-02): [N]->0 | Registry-violating: [N]->0
  Coverage (>= 60%): [N]% -> PASS / FAIL | Overall: PASS / FAIL
```

---

## STEP 9 -- POST-GENERATION PHASE CONFIRMATION

```
PHASE CONFIRMATION:
  Ph1: [gen]/[tgt] | Ph2: [gen]/[tgt] | Ph3: [gen]/[tgt] | Total: [gen]/[tgt]
  -> MATCH / MISMATCH each
```

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

```
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
  [INERTIA COMPETITOR] in Step 2 column header:        YES/NO -> PASS / FAIL
  [INERTIA COMPETITOR] in Step 3 column header:        YES/NO -> PASS / FAIL
  [INERTIA COMPETITOR] in Step 7 instruction clause:   YES/NO -> PASS / FAIL
  [INERTIA COMPETITOR] in Step 10 column header:       YES/NO -> PASS / FAIL
  >= 2 distinct table-header bracket-token locations:  YES/NO -> PASS / FAIL
  Detectable by bracket-scan (no prose interpretation): YES/NO -> PASS / FAIL

C-34 | Propagation Chain Pre-Declaration
  PROPAGATION CHAIN block in preamble before Step 1:            YES/NO -> PASS / FAIL
  All three checkpoints A/B/C named with locations:             YES/NO -> PASS / FAIL
  Checkpoint A satisfied (Step 2 header has bracket-token):     YES/NO -> PASS / FAIL
  Checkpoint B satisfied (Step 3 header has bracket-token):     YES/NO -> PASS / FAIL
  Checkpoint C satisfied (>= 50% linked body coverage):         YES/NO -> PASS / FAIL
  Completeness verifiable from preamble (no traversal needed):  YES/NO -> PASS / FAIL

C-35 | SRE-Write-First Enforcement Gate
  SRE-WRITE-FIRST GATE block present at Step 5c:           YES/NO -> PASS / FAIL
  Gate produces explicit PASS/FAIL verdict:                YES/NO -> PASS / FAIL
  Gate has "do not proceed" halt instruction:              YES/NO -> PASS / FAIL
  Gate was invoked before any body was written:            YES/NO -> PASS / FAIL
  Gate verdict in this output:                             PASS / FAIL

C-36 candidate | Checkpoint-Mapped VALIDATION TRACE
  CHECKPOINT MAP sub-section present in VALIDATION TRACE: YES/NO -> PASS / FAIL
  Checkpoint A echoed by label name with YES/NO probe:    YES/NO -> PASS / FAIL
  Checkpoint B echoed by label name with YES/NO probe:    YES/NO -> PASS / FAIL
  Checkpoint C echoed by label name with YES/NO probe:    YES/NO -> PASS / FAIL
  "All declared checkpoints mapped with YES/NO" confirmation: YES/NO -> PASS / FAIL
  Each probe is binary (no partial/conditional):          YES/NO -> PASS / FAIL

Summary:
  C-14 / C-16 / C-12:      PASS / FAIL each
  C-31 name propagation:    PASS / FAIL
  C-32 SRE-first:           PASS / FAIL
  C-33 bracket-token:       PASS / FAIL
  C-34 chain pre-decl:      PASS / FAIL
  C-35 enforce gate:        PASS / FAIL
  C-36 cand. checkpoint map: PASS / FAIL
  Overall: PASS (all) / FAIL (one or more)
```

If any threshold shows FAIL, identify the specific entries or bodies causing the
shortfall, revise, and re-run this block before submitting.
```

---

## V-02: Single-Axis -- Per-Criterion THRESHOLD CONFIRMATION Sub-Blocks (C-37a)

**Axis:** The THRESHOLD CONFIRMATION block in Step 11 is restructured so that each new
criterion (C-33, C-34, C-35) receives its own named BLOCK-START / BLOCK-END sub-block
with >= 6 verification lines, including an explicit scan-verifiability YES/NO line as
the final line before BLOCK-END. The sub-block is named by criterion number and title.
Older criteria (C-14, C-16, C-12, C-31, C-32) retain compact inline format.

**Probe (C-37a candidate):** In V-05 R12, C-33/C-34/C-35 share a flat section structure
within THRESHOLD CONFIRMATION. A scorer must read the entire section to determine whether
a specific criterion's verification lines are complete. Per-criterion sub-blocks create
addressable boundaries: a scorer can jump to "C-33 | Bracket-Token Propagation
BLOCK-START" and confirm that all lines within BLOCK-END are present and binary, without
reading adjacent criteria. The scan-verifiability YES/NO line (present in each sub-block)
makes the structural question "is this criterion's self-check scannable?" answerable from
within the sub-block, not inferred from the surrounding context.

**Hypothesis:** When each criterion has its own named sub-block, the scorer's verification
work for any single criterion is O(block) rather than O(section). The scan-verifiability
line within the sub-block is the signal that the criterion's author considered whether the
check is scan-detectable -- it's an explicit structural commitment, not just coverage.
C-37 would require: (a) C-33/C-34/C-35 each in their own named sub-block, (b) each
sub-block contains >= 6 lines, (c) each sub-block ends with a scan-verifiability YES/NO.

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

---

## STEP 1 -- PHASE-SEVERITY GRADIENT PRIOR

Phase 1 (Day 0-30): P2/P3. Workarounds exist; no committed production data. P0
reserved for activation blockers affecting all users simultaneously.

Phase 2 (Day 31-60): P1/P2. Workarounds have real cost. P0 exceptional: data loss
or workflow corruption under real load only.

Phase 3 (Day 61-90): P0/P1. No fallback at scale. P3 essentially absent.

```
PHASE-SEVERITY PRIOR:
  Phase 1 (Day 0-30):  typical P2/P3; P0 only for activation blockers affecting all users
  Phase 2 (Day 31-60): typical P1/P2; P0 exceptional (data loss or workflow corruption)
  Phase 3 (Day 61-90): typical P0/P1; P3 rare (users have exhausted workarounds)
```

---

## STEP 1b -- PHASE NARRATIVE

**Phase 1 (Day 0-30) -- First contact:**
Users are exploring the feature while keeping [INERTIA COMPETITOR] active as a safety
net. Each step is compared against [INERTIA COMPETITOR] behavior. Trigger event: first
contact with a behavior that diverges from [INERTIA COMPETITOR] -- setup friction,
missing documentation, onboarding gaps. Tickets driven by volume but low severity.

**Phase 2 (Day 31-60) -- Committed trial:**
Users have invested real workflows; some migrated, some still in [INERTIA COMPETITOR].
Trigger event: first time a committed workflow hits a blocking gap -- a config
combination that works in [INERTIA COMPETITOR] but fails here. Partial-migration
friction: no simple revert, but feature coverage incomplete.

**Phase 3 (Day 61-90) -- Operational dependency:**
[INERTIA COMPETITOR] is no longer available for this workflow. Trigger event: blocking
failure under production conditions. Severity escalates -- no fallback exists.

```
PHASE NARRATIVE COMPLETE:
  Phase 1 behavioral driver named ([INERTIA COMPETITOR] referenced): YES / NO
  Phase 2 behavioral driver named ([INERTIA COMPETITOR] referenced): YES / NO
  Phase 3 behavioral driver named ([INERTIA COMPETITOR] referenced): YES / NO
  Trigger events named for all three phases:                         YES / NO
```

---

## STEP 2 -- STATUS QUO ANCHOR

SRE row is listed first. The bracket-token [INERTIA COMPETITOR] in the column header
is Checkpoint A.

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

**Complete the SRE row first.**

Column 2 (Incumbent [INERTIA COMPETITOR] behavior): state the specific behavior of
[INERTIA COMPETITOR] that created the expectation. The bracket-token
[INERTIA COMPETITOR] in the column header is Checkpoint B.

| # | Persona class | Incumbent [INERTIA COMPETITOR] behavior | Imported expectation | What this feature does instead | Resulting failure mode | Ticket # |
|---|---------------|----------------------------------------|---------------------|-------------------------------|----------------------|----------|

Ticket #: LEAVE BLANK -- assigned in Step 6b. Complete at least 1 row.

```
ASSUMPTION AUDIT COMPLETE:
  Rows documented:                                         [N]
  SRE row present:                                         YES / NO
  All 5 non-ID columns populated:                          YES / NO
  Column 2 cells reference [INERTIA COMPETITOR] by name:   YES / NO -> Checkpoint B
  Ticket IDs pending at Step 6b:                           [N] rows
```

---

## STEP 4 -- PHASE DISTRIBUTION TARGET

```
PHASE DISTRIBUTION TARGET:
  Phase 1 (Day 0-30):  [N] tickets   -- first contact, [INERTIA COMPETITOR] comparison
  Phase 2 (Day 31-60): [N] tickets   -- committed trial, migration edge cases
  Phase 3 (Day 61-90): [N] tickets   -- operational dependency, no fallback
  Total:               [N] tickets
```

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

```
REGISTRY GATE:
  Per-category commitment honored:  YES / NO -> must be YES
  Floor guarantee sum > 3:          PASS / FAIL
  Dual-category coverage:           PASS / FAIL
  Registry applied during Step 7:   CONFIRMED
```

---

## STEP 5c -- SRE-WRITE-FIRST GATE

```
SRE-WRITE-FIRST GATE:
  SRE row position in PERSONA VOICE TABLE (Step 5): row [N] of [total rows]
  SRE is the first row in PERSONA VOICE TABLE:       YES / NO  -> PASS / FAIL
  SRE body will be the first body written in Step 7: CONFIRMED
  Gate verdict:                                      PASS / FAIL
```

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

```
VALIDATION TRACE:
  Distinct categories:                    [N] (>= 3)              -> PASS / FAIL
  Distinct personas:                      [N] (>= 2)              -> PASS / FAIL
  P0 count:                               [N] (<= 1)              -> PASS / FAIL
  Low/medium volume entries:              [N] (>= 1)              -> PASS / FAIL
  Total rows:                             [N] (>= 7)              -> PASS / FAIL
  Phase distribution:
    Phase 1: [N] / target [N] | Phase 2: [N] / target [N] | Phase 3: [N] / target [N]
    -> MATCH / MISMATCH each
  All personas in voice table:            YES / NO                -> PASS / FAIL
  >= 1 ticket linked to audit row:        YES / NO                -> PASS / FAIL
  Phase-severity consistent:
    Phase 1 (P2/P3): [list] | Phase 2 (P1/P2): [list] | Phase 3 (P0/P1): [list]
    -> PASS / FAIL
  SRE checks:
    SRE first in Step 2: YES/NO | SRE first in Step 5: YES/NO
    SRE-WRITE-FIRST GATE verdict: PASS/FAIL | SRE in audit: YES/NO | SRE ticket: YES/NO
  Bracket-token propagation:
    [INERTIA COMPETITOR] in Step 2 header: YES/NO -> Checkpoint A
    [INERTIA COMPETITOR] in Step 3 header: YES/NO -> Checkpoint B
    [INERTIA COMPETITOR] in Step 7 instruction: YES/NO
    [INERTIA COMPETITOR] in Step 10 header: YES/NO
    >= 2 distinct table-header locations: YES/NO -> PASS / FAIL
  Propagation chain:
    PROPAGATION CHAIN block in preamble: YES/NO
    All A/B/C declared: YES/NO
    Checkpoint A satisfied: YES/NO | B satisfied: YES/NO | C satisfied: YES/NO
  Overall:                                                        -> PASS / FAIL
```

---

## STEP 6b -- FORWARD-LINK

```
FORWARD-LINK GATE:
  Assumption audit rows total: [N] | Rows with Ticket # assigned: [N] -> PASS / FAIL
  All Ticket # values exist in table: YES / NO | Overall: PASS / FAIL
```

---

## STEP 7 -- TICKET BODIES WITH DIMENSION-LABELED MARKER CITATIONS

Write SRE bodies first. Do not open any body with a persona declaration.

For tickets with [A#N] tag: body must reference [INERTIA COMPETITOR] verbatim --
the bracket-token [INERTIA COMPETITOR] in this instruction names the comparison anchor.
This satisfies Checkpoint C of the PROPAGATION CHAIN.

Each body: >= 2 markers from DIFFERENT columns. Clear every marker against REJECTION
REGISTRY before citing.

Format:

### Ticket [N] [Phase N]: [Title from table]
**Traces to:** Assumption #[N]
**Body:** [2-5 sentences in the persona's actual voice]
**Voice markers:** operational=[term] | frustration=[phrase]

---

TIER-SEQUENCING RULE (preamble):
  All TIER 1 gates must show PROCEED before TIER 2 is evaluated.

```
BIDIRECTIONAL LINKAGE VERIFICATION:

  TIER ARCHITECTURE SELF-CHECK:
  | Landmark | Expected location | Present | Result |
  |----------|-----------------|---------|--------|
  | TIER-SEQUENCING RULE | Preamble above block | YES/NO | PASS/FAIL |
  | -- TIER 1: Per-Pair -- | Before per-pair blocks | YES/NO | PASS/FAIL |
  | -- TIER 2: Block-Level -- | Before REVISION GATE | YES/NO | PASS/FAIL |

  Forward: [N]/[N] rows have Ticket # | Backward: [N] bodies have "Traces to:"

  -- TIER 1: Per-Pair Verification --
    Assumption #[N] -> Ticket [N]:
      Audit phrase: "[quote]" | Body evidence: "[quote]"
      Alignment: MATCH/MISMATCH | Gate: PROCEED | REVISE
  All TIER 1 PROCEED: YES/NO -> PASS / FAIL

  -- TIER 2: Block-Level Clearance --
  REVISION GATE: Mismatched: [list/"none"] | Status: OPEN | CLOSED
  Overall: PASS / FAIL
```

---

## STEP 8 -- MARKER FORMAT AUDIT

```
MARKER FORMAT AUDIT:
  Bodies >= 2 diff prefixes: [N] | Flat-list: [N]->0 | Same-dim: [N]->0
  Registry-violating: [N]->0 | Coverage (>= 60%): [N]% -> PASS/FAIL | Overall: PASS/FAIL
```

---

## STEP 9 -- POST-GENERATION PHASE CONFIRMATION

```
PHASE CONFIRMATION:
  Ph1: [gen]/[tgt] | Ph2: [gen]/[tgt] | Ph3: [gen]/[tgt] | Total: [gen]/[tgt]
```

---

## STEP 10 -- GAP ANALYSIS TABLE

| # | Gap type | Specific artifact | Classification | Incumbent [INERTIA COMPETITOR] status | Phase first surfaces |
|---|----------|------------------|----------------|--------------------------------------|---------------------|

Minimum: 1 Doc, 1 Design, 1 Operational. Classification: PARITY | NET-NEW.
Use the declared product name in each Incumbent cell.

---

## STEP 11 -- THRESHOLD CONFIRMATION

```
THRESHOLD CONFIRMATION:

C-14: [N]/[N] = [N]% (>= 60%) -> PASS / FAIL
C-16: [N]/[N] = [N]% (>= 60%) -> PASS / FAIL
C-12: [N]/[N] = [N]% (>= 60%) -> PASS / FAIL

C-31: Preamble YES/NO | Body >= 50%: [N]% | Step 10 cells YES/NO -> PASS / FAIL
C-32: SRE first Step 2 YES/NO | SRE first Step 5 YES/NO | SRE audit YES/NO -> PASS/FAIL

C-33 | Bracket-Token Propagation
BLOCK-START:
  [INERTIA COMPETITOR] in Step 2 column header (Checkpoint A):   YES/NO
  [INERTIA COMPETITOR] in Step 3 column header (Checkpoint B):   YES/NO
  [INERTIA COMPETITOR] in Step 7 instruction clause:             YES/NO
  [INERTIA COMPETITOR] in Step 10 column header:                 YES/NO
  >= 2 distinct table-header bracket-token locations:            YES/NO
  Scan-verifiability (detectable by bracket-scan, not prose):    YES/NO -> PASS / FAIL
BLOCK-END: C-33 PASS / FAIL

C-34 | Propagation Chain Pre-Declaration
BLOCK-START:
  PROPAGATION CHAIN block present in preamble before Step 1:     YES/NO
  All three checkpoints A/B/C named with locations:              YES/NO
  Checkpoint A satisfied (Step 2 header has bracket-token):      YES/NO
  Checkpoint B satisfied (Step 3 header has bracket-token):      YES/NO
  Checkpoint C satisfied (>= 50% linked body coverage):          YES/NO
  Completeness verifiable from preamble without traversal:       YES/NO -> PASS / FAIL
BLOCK-END: C-34 PASS / FAIL

C-35 | SRE-Write-First Enforcement Gate
BLOCK-START:
  SRE-WRITE-FIRST GATE block present at Step 5c:                 YES/NO
  Gate produces explicit PASS/FAIL verdict:                      YES/NO
  Gate carries "do not proceed" halt instruction:                YES/NO
  Gate was invoked before any body was written:                  YES/NO
  Gate verdict in this output:                                   PASS / FAIL
  Advisory write-first (C-32) upgraded to binding gate (C-35):  YES/NO -> PASS / FAIL
BLOCK-END: C-35 PASS / FAIL

Summary:
  C-14 / C-16 / C-12:      PASS / FAIL each
  C-31 / C-32:              PASS / FAIL each
  C-33 bracket-token:       PASS / FAIL
  C-34 chain pre-decl:      PASS / FAIL
  C-35 enforce gate:        PASS / FAIL
  Overall: PASS (all) / FAIL (one or more)
```
```

---

## V-03: Single-Axis -- Cross-Criterion Structural Synergy Declaration (C-37b)

**Axis:** A named CROSS-CRITERION SYNERGY DECLARATION sub-block is added to THRESHOLD
CONFIRMATION. The block explicitly names the structural dependency: C-33 bracket-tokens
embedded in column headers at Checkpoints A and B make C-34's declared checkpoints
grep-detectable, so C-34's "completeness verifiable without traversal" property is
answerable YES structurally (the bracket-token IS the mechanism of verifiability, not
just an assertion about it). The block also states what degrades when synergy is absent
(e.g., if C-33 fails, C-34 Checkpoint A/B verification requires prose interpretation
instead of bracket-scan).

**Probe (C-37b candidate):** In V-05 R12, C-33 and C-34 are verified in adjacent sections
within THRESHOLD CONFIRMATION, but no block explicitly names their dependency. A scorer
can observe that both criteria are satisfied without understanding how they interact. The
CROSS-CRITERION SYNERGY DECLARATION makes the dependency structurally visible: C-33 is
a prerequisite of C-34's strongest property (no-traversal verifiability). If C-33 fails,
C-34's "completeness verifiable without traversal" line would have to answer NO even if
the checkpoints themselves are satisfied -- because prose references to "the incumbent"
require interpretation. The declaration collapses the two criteria from independent checks
into a co-dependency statement that a scorer can verify in a single block.

**Hypothesis:** When the synergy between C-33 and C-34 is named explicitly, the model
has a structural commitment to satisfy both criteria in concert, not just independently.
The block tests whether the "completeness verifiable without traversal" YES answer is
earned by structural means (bracket-token in header) or asserted without that structural
backing. C-37 (cross-criterion synergy declared) would require this block to be present,
to name at least two criteria in its dependency statement, and to include a "synergy
verdict" line answerable YES/NO.

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

CROSS-CRITERION SYNERGY NOTE (preamble):
  C-33 bracket-tokens at Checkpoint A (Step 2 header) and Checkpoint B (Step 3 header)
  make C-34's checkpoints A and B grep-detectable. This structural linkage is what
  makes C-34's "completeness verifiable without traversal" property answerable YES --
  not an assertion, but a consequence of C-33 token placement. If C-33 tokens are absent
  from any checkpoint header, that checkpoint requires prose interpretation, and C-34's
  no-traversal property degrades to aspirational.

---

## STEP 1 -- PHASE-SEVERITY GRADIENT PRIOR

Phase 1 (Day 0-30): P2/P3. P0 reserved for activation blockers affecting all users.
Phase 2 (Day 31-60): P1/P2. P0 exceptional: data loss or workflow corruption only.
Phase 3 (Day 61-90): P0/P1. No fallback at scale. P3 essentially absent.

```
PHASE-SEVERITY PRIOR:
  Phase 1 (Day 0-30):  typical P2/P3; P0 only for activation blockers affecting all users
  Phase 2 (Day 31-60): typical P1/P2; P0 exceptional (data loss or workflow corruption)
  Phase 3 (Day 61-90): typical P0/P1; P3 rare (users have exhausted workarounds)
```

---

## STEP 1b -- PHASE NARRATIVE

**Phase 1 (Day 0-30) -- First contact:**
Users explore the feature while keeping [INERTIA COMPETITOR] active as a safety net.
Trigger event: first contact with a behavior that diverges from [INERTIA COMPETITOR].
Tickets driven by volume, low severity (prior tool fallback available).

**Phase 2 (Day 31-60) -- Committed trial:**
Users have invested real workflows; some migrated, some still in [INERTIA COMPETITOR].
Trigger event: committed workflow hits a blocking gap that works in [INERTIA COMPETITOR]
but fails here. Partial-migration friction.

**Phase 3 (Day 61-90) -- Operational dependency:**
[INERTIA COMPETITOR] is no longer available. Trigger event: blocking failure under
production conditions. Severity escalates -- no fallback exists.

```
PHASE NARRATIVE COMPLETE:
  Phase 1 behavioral driver named ([INERTIA COMPETITOR] referenced): YES / NO
  Phase 2 behavioral driver named ([INERTIA COMPETITOR] referenced): YES / NO
  Phase 3 behavioral driver named ([INERTIA COMPETITOR] referenced): YES / NO
  Trigger events named for all three phases:                         YES / NO
```

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

Column 2 (Incumbent [INERTIA COMPETITOR] behavior): the bracket-token in the column
header is Checkpoint B of the PROPAGATION CHAIN.

| # | Persona class | Incumbent [INERTIA COMPETITOR] behavior | Imported expectation | What this feature does instead | Resulting failure mode | Ticket # |
|---|---------------|----------------------------------------|---------------------|-------------------------------|----------------------|----------|

```
ASSUMPTION AUDIT COMPLETE:
  Rows: [N] | SRE present: YES/NO | Columns populated: YES/NO
  Checkpoint B (col 2 uses [INERTIA COMPETITOR] name): YES/NO | Ticket # pending: [N]
```

---

## STEP 4 -- PHASE DISTRIBUTION TARGET

```
PHASE DISTRIBUTION TARGET:
  Phase 1 (Day 0-30):  [N] tickets   -- first contact, [INERTIA COMPETITOR] comparison
  Phase 2 (Day 31-60): [N] tickets   -- committed trial, migration edge cases
  Phase 3 (Day 61-90): [N] tickets   -- operational dependency, no fallback
  Total:               [N] tickets
```

Constraints: Phase 1 >= 3. Phase 3 >= 1. Total >= 7.

---

## STEP 5 -- PERSONA VOICE TABLE (DIMENSION REGISTRY)

| Persona | Operational vocabulary | Frustration register | Framing conventions |
|---------|----------------------|---------------------|---------------------|
| SRE | (>= 2 specific terms) | (>= 2 specific phrases) | (>= 2 structural patterns) |
| Support | (>= 2 specific terms) | (>= 2 specific phrases) | (>= 2 structural patterns) |
| [other personas used] | (>= 2 specific terms) | (>= 2 specific phrases) | (>= 2 structural patterns) |

---

## STEP 5b -- DIMENSION-LABEL REJECTION REGISTRY

Category 1 min: 2 | Category 2 min: 2 | Floor guarantee: 2 + 2 = 4 > 3.

REJECTION REGISTRY:
Category 1: R-01 (flat list), R-02 (same prefix twice), R-03 (count without naming)
Category 2: R-04 (role declarations), R-05 (generic verbs), R-06 (synonym pairs),
            R-07 (bare nouns)

```
REGISTRY GATE:
  Category 1: [N]>=2 | Category 2: [N]>=2 | Total: [N]>=3 | Floor sum>[3]: PASS/FAIL
  Registry applied during Step 7: CONFIRMED
```

---

## STEP 5c -- SRE-WRITE-FIRST GATE

```
SRE-WRITE-FIRST GATE:
  SRE row position: row [N] of [N] | SRE first: YES/NO -> PASS/FAIL
  SRE body written first in Step 7: CONFIRMED | Gate verdict: PASS / FAIL
```

---

## STEP 6 -- TICKET SUMMARY TABLE AND VALIDATION TRACE

| # | Phase | Title | Category | Persona | Volume | Severity |
|---|-------|-------|----------|---------|--------|----------|

```
VALIDATION TRACE:
  Distinct categories: [N]>=3 | Distinct personas: [N]>=2 | P0 count: [N]<=1
  Low/medium volume: [N]>=1 | Total rows: [N]>=7
  Phase distribution:
    Phase 1: [N]/[N] | Phase 2: [N]/[N] | Phase 3: [N]/[N] -> MATCH / MISMATCH each
  All personas in voice table: YES/NO | >= 1 linked to audit: YES/NO
  Phase-severity: P1:[list] | P2:[list] | P3:[list] -> PASS/FAIL
  SRE checks: Step2 first YES/NO | Step5 first YES/NO | Gate PASS/FAIL | audit YES/NO
  Bracket-token: Step2 header YES/NO | Step3 header YES/NO | >= 2 locations YES/NO
  Propagation chain: preamble block YES/NO | A/B/C declared YES/NO
    A satisfied YES/NO | B satisfied YES/NO | C satisfied YES/NO
  Overall: -> PASS / FAIL
```

---

## STEP 6b -- FORWARD-LINK

```
FORWARD-LINK GATE:
  Audit rows: [N] | With Ticket #: [N] -> PASS/FAIL | IDs exist: YES/NO | Overall: PASS/FAIL
```

---

## STEP 7 -- TICKET BODIES

Write SRE bodies first. No persona declaration to open.

For [A#N] tickets: reference [INERTIA COMPETITOR] verbatim (Checkpoint C).
Each body: >= 2 markers from DIFFERENT dimensions. Clear against REJECTION REGISTRY.

### Ticket [N] [Phase N]: [Title from table]
**Traces to:** Assumption #[N]
**Body:** [2-5 sentences]
**Voice markers:** operational=[term] | frustration=[phrase]

---

TIER-SEQUENCING RULE: All TIER 1 PROCEED before TIER 2 evaluated.

```
BIDIRECTIONAL LINKAGE VERIFICATION:

  TIER ARCHITECTURE SELF-CHECK:
  | TIER-SEQUENCING RULE | Preamble | YES/NO | PASS/FAIL |
  | -- TIER 1: Per-Pair -- | Before pairs | YES/NO | PASS/FAIL |
  | -- TIER 2: Block-Level -- | Before REVISION GATE | YES/NO | PASS/FAIL |

  -- TIER 1 --
  Assumption #[N] -> Ticket [N]: Audit "[quote]" | Body "[quote]" | MATCH | PROCEED/REVISE
  All TIER 1 PROCEED: YES/NO -> PASS/FAIL

  -- TIER 2 --
  REVISION GATE: Mismatched: [/"none"] | OPEN | CLOSED
  Overall: PASS / FAIL
```

---

## STEP 8 -- MARKER FORMAT AUDIT

```
MARKER FORMAT AUDIT:
  >= 2 diff prefixes: [N] | R-01: [N]->0 | R-02: [N]->0 | R-04..07: [N]->0
  Coverage >= 60%: [N]% | Overall: PASS/FAIL
```

---

## STEP 9 -- PHASE CONFIRMATION

```
PHASE CONFIRMATION:
  Ph1:[gen]/[tgt] | Ph2:[gen]/[tgt] | Ph3:[gen]/[tgt] | Total:[gen]/[tgt]
```

---

## STEP 10 -- GAP ANALYSIS TABLE

| # | Gap type | Specific artifact | Classification | Incumbent [INERTIA COMPETITOR] status | Phase first surfaces |
|---|----------|------------------|----------------|--------------------------------------|---------------------|

Min: 1 Doc, 1 Design, 1 Operational. Classification: PARITY | NET-NEW.

---

## STEP 11 -- THRESHOLD CONFIRMATION

```
THRESHOLD CONFIRMATION:

C-14: [N]/[N]=[N]% | C-16: [N]/[N]=[N]% | C-12: [N]/[N]=[N]% -> PASS/FAIL each
C-31: Preamble YES/NO | Body >= 50%: [N]% | Step 10 YES/NO -> PASS/FAIL
C-32: SRE Step2 YES/NO | SRE Step5 YES/NO | SRE audit YES/NO -> PASS/FAIL

C-33 | Bracket-Token Propagation
  Step 2 header YES/NO | Step 3 header YES/NO | Step 7 instruction YES/NO
  Step 10 header YES/NO | >= 2 distinct locations YES/NO
  Scan-verifiability: YES/NO -> PASS/FAIL

C-34 | Propagation Chain Pre-Declaration
  Preamble block YES/NO | A/B/C declared YES/NO
  A satisfied YES/NO | B satisfied YES/NO | C satisfied YES/NO
  Completeness verifiable without traversal: YES/NO -> PASS/FAIL

C-35 | SRE-Write-First Enforcement Gate
  Gate block at Step 5c: YES/NO | PASS/FAIL verdict: YES/NO | Halt instruction: YES/NO
  Invoked before body writing: YES/NO | Gate verdict: PASS/FAIL

CROSS-CRITERION SYNERGY DECLARATION (C-37b candidate):
  Synergy pair declared: C-33 + C-34
  C-33 bracket-token at Checkpoint A header (Step 2): YES/NO
  C-33 bracket-token at Checkpoint B header (Step 3): YES/NO
  C-34 "completeness verifiable without traversal" -- structural basis:
    Checkpoint A verifiable by bracket-scan (not prose): YES/NO
    Checkpoint B verifiable by bracket-scan (not prose): YES/NO
  Synergy verdict: C-33 token placement IS the mechanism making C-34
    no-traversal verifiability structural rather than aspirational: YES/NO
  Degradation if C-33 absent: Checkpoint A/B require prose interpretation,
    C-34 "no-traversal" property degrades to aspirational:           YES/NO
  -> CROSS-CRITERION SYNERGY: STRUCTURAL / ABSENT

Summary:
  C-14 / C-16 / C-12:      PASS/FAIL each
  C-31 / C-32:              PASS/FAIL each
  C-33 bracket-token:       PASS/FAIL
  C-34 chain pre-decl:      PASS/FAIL
  C-35 enforce gate:        PASS/FAIL
  C-37b cand. synergy decl: STRUCTURAL / ABSENT -> PASS/FAIL
  Overall: PASS (all) / FAIL (one or more)
```
```

---

## V-04: Combined -- Checkpoint Map + Per-Criterion Sub-Blocks (V-01 + V-02)

**Axes combined:** Checkpoint-Mapped VALIDATION TRACE (V-01) + Per-Criterion THRESHOLD
CONFIRMATION Sub-Blocks (V-02). Independent mechanisms: the checkpoint map targets the
echo gap in Step 6 VALIDATION TRACE; the per-criterion sub-blocks target granularity
in Step 11 THRESHOLD CONFIRMATION.

**Combination hypothesis:** V-01 adds structural completeness at the trace level: each
checkpoint label declared in the preamble is echoed back with a binary probe. V-02 adds
structural granularity at the verification level: each criterion's verification lines are
bounded and addressable. The two mechanisms address different steps (Step 6 vs Step 11)
and different structural properties (trace echo completeness vs per-criterion scan
addressability). Neither mechanism requires the other to function. Their combination
closes two gaps simultaneously: (1) the trace does not currently echo checkpoint labels
verbatim; (2) the verification block does not currently bound criteria individually.
C-36 candidate requires V-01; C-37a candidate requires V-02. V-04 is the expected
satisfier of both independently.

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

---

## STEP 1 -- PHASE-SEVERITY GRADIENT PRIOR

Phase 1 (Day 0-30): P2/P3. P0 reserved for activation blockers affecting all users.
Phase 2 (Day 31-60): P1/P2. P0 exceptional: data loss or workflow corruption only.
Phase 3 (Day 61-90): P0/P1. No fallback at scale. P3 essentially absent.

```
PHASE-SEVERITY PRIOR:
  Phase 1: typical P2/P3; P0 only for activation blockers affecting all users
  Phase 2: typical P1/P2; P0 exceptional (data loss or workflow corruption)
  Phase 3: typical P0/P1; P3 rare (users have exhausted workarounds)
```

---

## STEP 1b -- PHASE NARRATIVE

**Phase 1 (Day 0-30) -- First contact:**
Users explore the feature while keeping [INERTIA COMPETITOR] active as a safety net.
Trigger event: divergence from [INERTIA COMPETITOR] behavior -- setup friction, missing
docs, onboarding gaps. Tickets: high volume, low severity (prior tool fallback available).

**Phase 2 (Day 31-60) -- Committed trial:**
Users have real workflows migrated; some still in [INERTIA COMPETITOR]. Trigger event:
committed workflow hits a blocking gap that works in [INERTIA COMPETITOR] but fails here.

**Phase 3 (Day 61-90) -- Operational dependency:**
[INERTIA COMPETITOR] is no longer available. Trigger event: blocking failure under
production conditions. Severity escalates -- no fallback.

```
PHASE NARRATIVE COMPLETE:
  Phase 1 driver named ([INERTIA COMPETITOR] referenced): YES / NO
  Phase 2 driver named ([INERTIA COMPETITOR] referenced): YES / NO
  Phase 3 driver named ([INERTIA COMPETITOR] referenced): YES / NO
  Trigger events named all phases:                        YES / NO
```

---

## STEP 2 -- STATUS QUO ANCHOR

SRE row is listed first. The bracket-token [INERTIA COMPETITOR] in the column header
is Checkpoint A.

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

Column header "Incumbent [INERTIA COMPETITOR] behavior" is Checkpoint B.

| # | Persona class | Incumbent [INERTIA COMPETITOR] behavior | Imported expectation | What this feature does instead | Resulting failure mode | Ticket # |
|---|---------------|----------------------------------------|---------------------|-------------------------------|----------------------|----------|

```
ASSUMPTION AUDIT COMPLETE:
  Rows: [N] | SRE present: YES/NO | Columns populated: YES/NO
  Checkpoint B (col 2 name): YES/NO | Ticket # pending: [N]
```

---

## STEP 4 -- PHASE DISTRIBUTION TARGET

```
PHASE DISTRIBUTION TARGET:
  Phase 1 (Day 0-30):  [N] tickets   -- [INERTIA COMPETITOR] comparison
  Phase 2 (Day 31-60): [N] tickets   -- migration edge cases
  Phase 3 (Day 61-90): [N] tickets   -- operational dependency, no fallback
  Total:               [N] tickets
```

Constraints: Phase 1 >= 3. Phase 3 >= 1. Total >= 7.

---

## STEP 5 -- PERSONA VOICE TABLE (DIMENSION REGISTRY)

| Persona | Operational vocabulary | Frustration register | Framing conventions |
|---------|----------------------|---------------------|---------------------|
| SRE | (>= 2 specific terms) | (>= 2 specific phrases) | (>= 2 structural patterns) |
| Support | (>= 2 specific terms) | (>= 2 specific phrases) | (>= 2 structural patterns) |
| [other personas] | (>= 2 specific terms) | (>= 2 specific phrases) | (>= 2 structural patterns) |

Dimension prefixes: operational= | frustration= | framing=

---

## STEP 5b -- DIMENSION-LABEL REJECTION REGISTRY

Category 1 min: 2 | Category 2 min: 2 | Floor guarantee: 4 > 3.

REJECTION REGISTRY:
Category 1: R-01 (flat list), R-02 (same prefix twice), R-03 (count without naming)
Category 2: R-04 (role declarations), R-05 (generic verbs), R-06 (synonym pairs),
            R-07 (bare nouns)

```
REGISTRY GATE:
  Cat1: [N]>=2 | Cat2: [N]>=2 | Total: [N]>=3 | Floor [N]+[N]>[3]: PASS/FAIL
  Registry applied during Step 7: CONFIRMED
```

---

## STEP 5c -- SRE-WRITE-FIRST GATE

```
SRE-WRITE-FIRST GATE:
  SRE position in voice table: row [N] of [N]
  SRE is first row:            YES / NO -> PASS / FAIL
  SRE body written first:      CONFIRMED
  Gate verdict:                PASS / FAIL
```

Do not advance to Step 6 with gate = FAIL.

---

## STEP 6 -- TICKET SUMMARY TABLE AND VALIDATION TRACE

| # | Phase | Title | Category | Persona | Volume | Severity |
|---|-------|-------|----------|---------|--------|----------|

```
VALIDATION TRACE:
  Distinct categories: [N]>=3 | Distinct personas: [N]>=2 | P0 count: [N]<=1
  Low/medium volume: [N]>=1 | Total rows: [N]>=7
  Phase distribution:
    Phase 1: [N]/[N] | Phase 2: [N]/[N] | Phase 3: [N]/[N] -> MATCH/MISMATCH each
  All personas in voice table: YES/NO | >=1 linked to audit row: YES/NO
  Phase-severity: Ph1(P2/P3):[list] | Ph2(P1/P2):[list] | Ph3(P0/P1):[list] -> PASS/FAIL
  SRE checks: Step2 first YES/NO | Step5 first YES/NO | Gate PASS/FAIL
  Bracket-token:
    Step 2 header: YES/NO -> Checkpoint A | Step 3 header: YES/NO -> Checkpoint B
    Step 7 instruction: YES/NO | Step 10 header: YES/NO
    >= 2 distinct table-header locations: YES/NO -> PASS/FAIL

  CHECKPOINT MAP (C-36 candidate):
    Checkpoint A declared in preamble -- location: Step 2 column header
      Checkpoint A satisfied (bracket-token in Step 2 header): YES / NO
    Checkpoint B declared in preamble -- location: Step 3 column header
      Checkpoint B satisfied (bracket-token in Step 3 header): YES / NO
    Checkpoint C declared in preamble -- location: >=50% linked body coverage
      Checkpoint C satisfied (body coverage >= 50%):           YES / NO
    All declared checkpoint labels echoed by name in this trace: YES / NO
    All three probes are binary (YES/NO, no partial):            YES / NO
    -> CHECKPOINT MAP: COMPLETE / INCOMPLETE

  Overall: -> PASS / FAIL
```

Do not proceed to Step 6b with VALIDATION TRACE = FAIL.

---

## STEP 6b -- FORWARD-LINK

```
FORWARD-LINK GATE:
  Audit rows: [N] | With Ticket #: [N] -> PASS/FAIL
  All IDs exist in table: YES/NO | Overall: PASS/FAIL
```

---

## STEP 7 -- TICKET BODIES

Write SRE bodies first. No persona declaration to open.
[A#N] tickets: reference [INERTIA COMPETITOR] verbatim (Checkpoint C).
Each body: >= 2 markers from DIFFERENT dimensions.

### Ticket [N] [Phase N]: [Title]
**Traces to:** Assumption #[N]
**Body:** [2-5 sentences]
**Voice markers:** operational=[term] | frustration=[phrase]

---

TIER-SEQUENCING RULE: All TIER 1 PROCEED before TIER 2.

```
BIDIRECTIONAL LINKAGE VERIFICATION:

  TIER ARCHITECTURE SELF-CHECK:
  | TIER-SEQUENCING RULE | Preamble | YES/NO | PASS/FAIL |
  | -- TIER 1: Per-Pair -- | Before pairs | YES/NO | PASS/FAIL |
  | -- TIER 2: Block-Level -- | Before REVISION GATE | YES/NO | PASS/FAIL |

  -- TIER 1 --
  Assumption #[N] -> Ticket [N]: "[audit quote]" | "[body quote]" | MATCH | PROCEED/REVISE
  All TIER 1 PROCEED: YES/NO -> PASS/FAIL

  -- TIER 2 --
  REVISION GATE: Mismatched: [/"none"] | OPEN | CLOSED
  Overall: PASS/FAIL
```

---

## STEP 8 -- MARKER FORMAT AUDIT

```
MARKER FORMAT AUDIT:
  >=2 diff prefixes: [N] | R-01: [N]->0 | R-02: [N]->0 | R-04..07: [N]->0
  Coverage >=60%: [N]% | Overall: PASS/FAIL
```

---

## STEP 9 -- PHASE CONFIRMATION

```
PHASE CONFIRMATION:
  Ph1:[gen]/[tgt] | Ph2:[gen]/[tgt] | Ph3:[gen]/[tgt] | Total:[gen]/[tgt]
```

---

## STEP 10 -- GAP ANALYSIS TABLE

| # | Gap type | Specific artifact | Classification | Incumbent [INERTIA COMPETITOR] status | Phase first surfaces |
|---|----------|------------------|----------------|--------------------------------------|---------------------|

Min: 1 Doc, 1 Design, 1 Operational.

---

## STEP 11 -- THRESHOLD CONFIRMATION

```
THRESHOLD CONFIRMATION:

C-14: [N]/[N]=[N]% | C-16: [N]/[N]=[N]% | C-12: [N]/[N]=[N]% -> PASS/FAIL each
C-31: Preamble YES/NO | Body >= 50%: [N]% | Step 10 cells YES/NO -> PASS/FAIL
C-32: SRE Step2 YES/NO | SRE Step5 YES/NO | SRE audit YES/NO -> PASS/FAIL

C-33 | Bracket-Token Propagation
BLOCK-START:
  [INERTIA COMPETITOR] in Step 2 column header (Checkpoint A):   YES/NO
  [INERTIA COMPETITOR] in Step 3 column header (Checkpoint B):   YES/NO
  [INERTIA COMPETITOR] in Step 7 instruction clause:             YES/NO
  [INERTIA COMPETITOR] in Step 10 column header:                 YES/NO
  >= 2 distinct table-header bracket-token locations:            YES/NO
  Scan-verifiability (bracket-scan, not prose interpretation):   YES/NO -> PASS/FAIL
BLOCK-END: C-33 PASS / FAIL

C-34 | Propagation Chain Pre-Declaration
BLOCK-START:
  PROPAGATION CHAIN block present in preamble before Step 1:     YES/NO
  All three checkpoints A/B/C named with locations:              YES/NO
  Checkpoint A satisfied (Step 2 header has bracket-token):      YES/NO
  Checkpoint B satisfied (Step 3 header has bracket-token):      YES/NO
  Checkpoint C satisfied (>= 50% linked body coverage):          YES/NO
  Completeness verifiable from preamble without traversal:       YES/NO -> PASS/FAIL
BLOCK-END: C-34 PASS / FAIL

C-35 | SRE-Write-First Enforcement Gate
BLOCK-START:
  SRE-WRITE-FIRST GATE block present at Step 5c:                 YES/NO
  Gate produces explicit PASS/FAIL verdict:                      YES/NO
  Gate carries "do not proceed" halt instruction:                YES/NO
  Gate was invoked before any body was written:                  YES/NO
  Gate verdict in this output:                                   PASS / FAIL
  Advisory C-32 upgraded to binding enforcement gate:            YES/NO -> PASS/FAIL
BLOCK-END: C-35 PASS / FAIL

C-36 candidate | Checkpoint-Mapped VALIDATION TRACE
  CHECKPOINT MAP sub-section present in Step 6 VALIDATION TRACE: YES/NO -> PASS/FAIL
  Checkpoint A echoed by label name with YES/NO probe:            YES/NO -> PASS/FAIL
  Checkpoint B echoed by label name with YES/NO probe:            YES/NO -> PASS/FAIL
  Checkpoint C echoed by label name with YES/NO probe:            YES/NO -> PASS/FAIL
  "All declared checkpoints mapped" confirmation line present:    YES/NO -> PASS/FAIL
  Each probe is binary (no partial/conditional):                  YES/NO -> PASS/FAIL

Summary:
  C-14 / C-16 / C-12:       PASS/FAIL each
  C-31 / C-32:               PASS/FAIL each
  C-33 bracket-token:        PASS/FAIL
  C-34 chain pre-decl:       PASS/FAIL
  C-35 enforce gate:         PASS/FAIL
  C-36 cand. checkpoint map: PASS/FAIL
  Overall: PASS (all) / FAIL (one or more)
```
```

---

## V-05: Full Synthesis -- Checkpoint Map + Per-Criterion Sub-Blocks + Synergy Declaration (V-01 + V-02 + V-03)

**Axes combined:** All three R13 axes: Checkpoint-Mapped VALIDATION TRACE (V-01) +
Per-Criterion THRESHOLD CONFIRMATION Sub-Blocks (V-02) + Cross-Criterion Structural
Synergy Declaration (V-03).

**Combination hypothesis:** The three axes address three distinct structural gaps:
- V-01: VALIDATION TRACE does not echo checkpoint labels by name -- the CHECKPOINT MAP
  closes this by creating a verbatim-echo sub-section
- V-02: THRESHOLD CONFIRMATION criteria are not individually bounded -- per-criterion
  sub-blocks close this by making each criterion addressable independently
- V-03: C-33 and C-34 have structural dependency not yet declared -- the CROSS-CRITERION
  SYNERGY DECLARATION closes this by naming the mechanism explicitly

Together they form an integrated verification chain: declare checkpoints (PROPAGATION
CHAIN in preamble) -> embed bracket-tokens at declared locations (C-33) -> echo each
checkpoint label in trace with binary probe (C-36, V-01) -> bound each criterion's
verification independently (C-37a, V-02) -> declare that C-33 token placement IS the
mechanism making C-34 no-traversal verifiability structural (C-37b, V-03).

**C-36 + C-37 candidates:** Both apply. V-05 is the strongest expected satisfier of
C-36 and C-37 while maintaining all C-01 through C-35 compliance.

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

CROSS-CRITERION SYNERGY NOTE (preamble):
  C-33 bracket-tokens at Checkpoint A (Step 2 header) and Checkpoint B (Step 3 header)
  make C-34's declared checkpoints grep-detectable. This is what makes C-34's
  "completeness verifiable without traversal" property structural rather than
  aspirational. If C-33 tokens are absent from a checkpoint header, that checkpoint
  requires prose interpretation and C-34's no-traversal property degrades to
  aspirational for that checkpoint. The CROSS-CRITERION SYNERGY DECLARATION in
  Step 11 confirms this dependency is satisfied.

---

## STEP 1 -- PHASE-SEVERITY GRADIENT PRIOR

Phase 1 (Day 0-30): P2/P3. P0 reserved for activation blockers affecting all users.
Phase 2 (Day 31-60): P1/P2. P0 exceptional: data loss or workflow corruption only.
Phase 3 (Day 61-90): P0/P1. No fallback at scale. P3 essentially absent.

```
PHASE-SEVERITY PRIOR:
  Phase 1 (Day 0-30):  typical P2/P3; P0 only for activation blockers affecting all users
  Phase 2 (Day 31-60): typical P1/P2; P0 exceptional (data loss or workflow corruption)
  Phase 3 (Day 61-90): typical P0/P1; P3 rare (users have exhausted workarounds)
```

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

```
PHASE NARRATIVE COMPLETE:
  Phase 1 behavioral driver named ([INERTIA COMPETITOR] referenced): YES / NO
  Phase 2 behavioral driver named ([INERTIA COMPETITOR] referenced): YES / NO
  Phase 3 behavioral driver named ([INERTIA COMPETITOR] referenced): YES / NO
  Trigger events named for all three phases:                         YES / NO
```

---

## STEP 2 -- STATUS QUO ANCHOR

SRE row is listed first. Column 2 uses the INERTIA COMPETITOR name from the preamble.
The bracket-token [INERTIA COMPETITOR] in the column header is Checkpoint A of the
PROPAGATION CHAIN.

Column 2 instruction: for each row, name the specific behavior of [INERTIA COMPETITOR]
that taught this persona class to expect X. The bracket-token [INERTIA COMPETITOR] in
the column header anchors this instruction.

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

```
ASSUMPTION AUDIT COMPLETE:
  Rows documented:                                         [N]
  SRE row present:                                         YES / NO
  All 5 non-ID columns populated:                          YES / NO
  Column 2 cells reference [INERTIA COMPETITOR] by name:   YES / NO -> Checkpoint B
  Ticket IDs pending at Step 6b:                           [N] rows
```

---

## STEP 4 -- PHASE DISTRIBUTION TARGET

Declare the binding target consistent with the Phase Narrative from Step 1b.

```
PHASE DISTRIBUTION TARGET:
  Phase 1 (Day 0-30):  [N] tickets   -- first contact, [INERTIA COMPETITOR] comparison
  Phase 2 (Day 31-60): [N] tickets   -- committed trial, migration edge cases
  Phase 3 (Day 61-90): [N] tickets   -- operational dependency, no fallback
  Total:               [N] tickets
```

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

```
REGISTRY GATE:
  Per-category commitment honored:  YES / NO -> must be YES
  Floor guarantee sum > 3:          PASS / FAIL
  Dual-category coverage:           PASS / FAIL
  Registry applied during Step 7:   CONFIRMED
```

Do not write any ticket body until REGISTRY GATE shows all conditions met.

---

## STEP 5c -- SRE-WRITE-FIRST GATE

This gate is the binding boundary between the PERSONA VOICE TABLE and ticket body
writing. Do not write any ticket body until this gate shows PASS.

```
SRE-WRITE-FIRST GATE:
  SRE row position in PERSONA VOICE TABLE (Step 5): row [N] of [total rows]
  SRE is the first row in PERSONA VOICE TABLE:       YES / NO  -> PASS / FAIL
  SRE body will be the first body written in Step 7: CONFIRMED
  Gate verdict:                                      PASS / FAIL
```

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

```
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
    [INERTIA COMPETITOR] in Step 2 column header: YES / NO        -> Checkpoint A anchor
    [INERTIA COMPETITOR] in Step 3 column header: YES / NO        -> Checkpoint B anchor
    [INERTIA COMPETITOR] in Step 7 instruction:   YES / NO
    [INERTIA COMPETITOR] in Step 10 col header:   YES / NO
    >= 2 distinct table-header bracket-token locations: YES / NO  -> PASS / FAIL

  CHECKPOINT MAP (C-36 candidate):
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
```

Do not proceed to Step 6b with VALIDATION TRACE showing FAIL.

---

## STEP 6b -- FORWARD-LINK

Go back to Step 3. For every assumption audit row, fill in the Ticket # column.

```
FORWARD-LINK GATE:
  Assumption audit rows total: [N] | Rows with Ticket # assigned: [N] -> PASS / FAIL
  All Ticket # values exist in table: YES / NO -> PASS / FAIL | Overall: PASS / FAIL
```

Do not write any body with FORWARD-LINK GATE showing FAIL.

---

## STEP 7 -- TICKET BODIES WITH DIMENSION-LABELED MARKER CITATIONS

Write SRE bodies first (consistent with SRE-WRITE-FIRST GATE). Then Support, PM/UX,
customer personas. Do not open any body with a persona declaration. Start with the issue.

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

```
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
```

---

## STEP 8 -- MARKER FORMAT AUDIT

```
MARKER FORMAT AUDIT:
  Total bodies: [N] | Bodies with >= 2 diff prefixes: [N]
  Flat-list (R-01): [N]->0 | Same-dim (R-02): [N]->0 | Registry-violating: [N]->0
  Coverage (>= 60%): [N]% -> PASS / FAIL | Overall: PASS / FAIL
```

---

## STEP 9 -- POST-GENERATION PHASE CONFIRMATION

```
PHASE CONFIRMATION:
  Phase 1: [gen]/[tgt] -> MATCH/MISMATCH
  Phase 2: [gen]/[tgt] -> MATCH/MISMATCH
  Phase 3: [gen]/[tgt] -> MATCH/MISMATCH
  Total:   [gen]/[tgt] -> MATCH/MISMATCH
```

---

## STEP 10 -- GAP ANALYSIS TABLE

Column definitions:
- Gap type: Doc | Design | Operational
- Specific artifact: exact doc section, config field, API endpoint, runbook page, UI element
- Classification: PARITY | NET-NEW
- Incumbent [INERTIA COMPETITOR] status: what [INERTIA COMPETITOR] offers here (or
  "no equivalent") -- bracket-token in column header; use declared product name in cells
- Phase first surfaces: Phase 1 | Phase 2 | Phase 3

| # | Gap type | Specific artifact | Classification | Incumbent [INERTIA COMPETITOR] status | Phase first surfaces |
|---|----------|------------------|----------------|--------------------------------------|---------------------|

Minimum: 1 Doc row, 1 Design row, 1 Operational row.

---

## STEP 11 -- THRESHOLD CONFIRMATION

```
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

C-36 candidate | Checkpoint-Mapped VALIDATION TRACE
  CHECKPOINT MAP sub-section present in Step 6 VALIDATION TRACE:  YES/NO -> PASS/FAIL
  Checkpoint A echoed by label name with YES/NO probe:             YES/NO -> PASS/FAIL
  Checkpoint B echoed by label name with YES/NO probe:             YES/NO -> PASS/FAIL
  Checkpoint C echoed by label name with YES/NO probe:             YES/NO -> PASS/FAIL
  "All declared checkpoint labels echoed" confirmation line:       YES/NO -> PASS/FAIL
  All three probes are binary (no partial/conditional):            YES/NO -> PASS/FAIL

CROSS-CRITERION SYNERGY DECLARATION (C-37 candidate):
  Synergy pair declared: C-33 bracket-token placement + C-34 no-traversal verifiability
  C-33 bracket-token present at Checkpoint A header (Step 2):      YES/NO
  C-33 bracket-token present at Checkpoint B header (Step 3):      YES/NO
  Checkpoint A grep-detectable by bracket-scan (not prose):        YES/NO
  Checkpoint B grep-detectable by bracket-scan (not prose):        YES/NO
  C-34 "completeness verifiable without traversal" -- structural basis:
    Answer is YES because bracket-tokens are the mechanism (not assertion): YES/NO
  Degradation declared: if C-33 absent from a header, that checkpoint
    requires prose interpretation; C-34 no-traversal property degrades:     YES/NO
  -> CROSS-CRITERION SYNERGY: STRUCTURAL / ABSENT -> PASS/FAIL

Summary:
  C-14 / C-16 / C-12:       PASS / FAIL each
  C-31 name propagation:     PASS / FAIL
  C-32 SRE-first:            PASS / FAIL
  C-33 bracket-token:        PASS / FAIL
  C-34 chain pre-decl:       PASS / FAIL
  C-35 enforce gate:         PASS / FAIL
  C-36 cand. checkpoint map: PASS / FAIL
  C-37 cand. synergy decl:   STRUCTURAL / ABSENT -> PASS / FAIL
  Overall: PASS (all) / FAIL (one or more)
```

If any threshold shows FAIL, identify the specific entries or bodies causing the
shortfall, revise, and re-run this block before submitting.
```
