# listen-support Round 12 -- Skill Body Prompt Variations

**Date:** 2026-03-15
**Rubric target:** v12 (35 criteria -- C-01 through C-35)
**Base:** V-05 R10 (C-01 through C-32 ceiling; inertia preamble + SRE-first + phase
narrative all active)

**Variation axes selected** (3 single-axis, then 2 combined):

1. **Bound-Variable Bracket-Token Propagation (C-33 candidate)** -- Embed the
   competitor name as the literal bracket-variable token `[INERTIA COMPETITOR]` in
   table column headers and step instruction action clauses throughout the prompt.
   All propagation points become detectable by bracket-pattern scan rather than prose
   interpretation. VALIDATION TRACE gains a bracket-scan check. (V-01)

2. **Propagation Chain Pre-Declaration (C-34 candidate)** -- Add a PROPAGATION CHAIN
   sub-block to the preamble naming three checkpoint labels (A, B, C) before Step 1
   runs. The preamble declares: what each checkpoint is and where to find it. VALIDATION
   TRACE gains a completeness check comparing declared vs. satisfied checkpoints. (V-02)

3. **SRE-Write-First Enforcement Gate (C-35 candidate)** -- Insert a named
   SRE-WRITE-FIRST GATE block at the PERSONA VOICE TABLE -> ticket body boundary.
   The gate produces a PASS/FAIL verdict and halts forward progress if SRE is not the
   first row in the voice table. Advisory write-first directive (C-32) becomes a
   binding enforcement gate. (V-03)

4. **V-01 + V-02 combined** -- Bracket-token propagation + propagation chain
   pre-declaration. Independent mechanisms: token embedding is a structural change
   to column headers and instructions; chain pre-declaration is a preamble contract
   with a verification check. (V-04)

5. **Full synthesis** -- All three axes: bracket-token + chain pre-declaration +
   SRE-write-first gate. (V-05)

**Axes NOT explored this round (deferred):**
- Phrasing register (formal vs. conversational) -- stable at current register
- Lifecycle emphasis depth -- phase narrative stable from R10 V-03

**R12 criterion hypothesis matrix:**

| Criterion candidate | V-01 | V-02 | V-03 | V-04 | V-05 |
|--------------------|------|------|------|------|------|
| C-01 through C-32 (all prior -- active baseline) | YES | YES | YES | YES | YES |
| C-33 candidate: `[INERTIA COMPETITOR]` bracket-token in column headers + instruction clauses | YES | -- | -- | YES | YES |
| C-34 candidate: PROPAGATION CHAIN sub-block with A/B/C labels pre-declared in preamble | -- | YES | -- | YES | YES |
| C-35 candidate: SRE-WRITE-FIRST GATE block at voice-table -> body boundary | -- | -- | YES | -- | YES |

**Axes carried from R10 V-05 (active in all R12 variations as baseline):**
- INERTIA COMPETITOR preamble declaration (C-31)
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

## V-01: Single-Axis -- Bound-Variable Bracket-Token Propagation (C-33)

**Axis:** The INERTIA COMPETITOR name is embedded as the literal bracket-variable token
`[INERTIA COMPETITOR]` in table column headers and step instruction action clauses
throughout the prompt. Propagation is detectable by bracket-pattern scan (grep for
`\[INERTIA COMPETITOR\]`) rather than by prose interpretation.

**Probe (C-33 candidate):** C-31 requires the competitor name to appear in the preamble
and propagate into ticket bodies (>= 50% verbatim coverage). A common failure mode:
the declared name drifts to "the incumbent" or "the prior tool" in table column 2 or
instruction text -- prose references that a scorer must read and interpret. Embedding
the name as `[INERTIA COMPETITOR]` in column headers and instruction action clauses
creates a structural propagation anchor. Any column 2 cell that writes "the incumbent"
is immediately detectable as a deviation from the column header's bracket-variable.

**Hypothesis:** When the column header itself reads "Prior `[INERTIA COMPETITOR]`
behavior", the model is forced to fill column 2 cells with content anchored to the
declared name -- the column header is the constraint. The same applies to step
instructions: when an action clause reads "name the behavior of `[INERTIA COMPETITOR]`
that taught this expectation", the bracket-variable in the instruction acts as a binding
cite. C-33 would require at least two distinct bracket-token locations (one table column
header, one instruction clause) detectable by bracket-scan.

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
clauses. Every occurrence is detectable by scanning for the bracket pattern
[INERTIA COMPETITOR] -- no prose interpretation required.

---

## STEP 1 -- PHASE-SEVERITY GRADIENT PRIOR

Before declaring targets or generating tickets, state the principled severity prior.
Identical functional problems carry different severity depending on when they surface.

Phase 1 (Day 0-30): P2/P3. Workarounds exist; no committed production data. P0
reserved for activation blockers affecting all users simultaneously -- excludes config
confusion, missing docs, and edge-case bugs.

Phase 2 (Day 31-60): P1/P2. Users have invested real workflows. A blocking gap in a
committed workflow is P1 because workarounds have real cost. P0 exceptional: data loss
or workflow corruption under real load only.

Phase 3 (Day 61-90): P0/P1. Systems run at scale with real business dependencies.
Partial failures cascade. P3 essentially absent.

```
PHASE-SEVERITY PRIOR:
  Phase 1 (Day 0-30):  typical P2/P3; P0 only for activation blockers affecting all users
  Phase 2 (Day 31-60): typical P1/P2; P0 exceptional (data loss or workflow corruption)
  Phase 3 (Day 61-90): typical P0/P1; P3 rare (users have exhausted workarounds)
```

---

## STEP 1b -- PHASE NARRATIVE

State the behavioral driver for each phase. The Phase Distribution Target in Step 4
must be consistent with this narrative. Reference [INERTIA COMPETITOR] where it names
the prior tool the user is transitioning from.

**Phase 1 (Day 0-30) -- First contact:**
Users are exploring the feature while keeping [INERTIA COMPETITOR] active as a safety
net. Each step is compared against [INERTIA COMPETITOR] behavior. Trigger event: first
contact with a feature behavior that diverges from [INERTIA COMPETITOR] -- setup
friction, missing documentation for the first-use path, onboarding gaps. Tickets driven
by volume but low severity (prior tool fallback available).

**Phase 2 (Day 31-60) -- Committed trial:**
Users have invested real workflows; some are migrated, some still run in
[INERTIA COMPETITOR]. Trigger event: first time a committed workflow hits a blocking
gap -- a config combination that works in [INERTIA COMPETITOR] but fails here, or an
integration boundary assumed compatible. Tickets reflect partial-migration friction:
no simple revert available, but feature coverage incomplete.

**Phase 3 (Day 61-90) -- Operational dependency:**
[INERTIA COMPETITOR] is no longer available for this workflow. Trigger event: a
blocking failure under production conditions that doesn't surface in non-production
use. Severity escalates because no fallback exists.

```
PHASE NARRATIVE COMPLETE:
  Phase 1 behavioral driver named:                    YES / NO
  Phase 2 behavioral driver named:                    YES / NO
  Phase 3 behavioral driver named:                    YES / NO
  [INERTIA COMPETITOR] referenced in Phase 1 text:    YES / NO
  [INERTIA COMPETITOR] referenced in Phase 2 text:    YES / NO
  [INERTIA COMPETITOR] referenced in Phase 3 text:    YES / NO
  Trigger events named for all three phases:          YES / NO
```

---

## STEP 2 -- STATUS QUO ANCHOR

Every support ticket in the first 90 days is a transition story. SRE row is listed
first -- SRE failure modes determine the severity ceiling for the entire ticket set.

Column 2 (Prior [INERTIA COMPETITOR] behavior): name the specific behavior of
[INERTIA COMPETITOR] that taught this persona class to expect X. Use the exact product
name declared in the preamble -- the bracket-token [INERTIA COMPETITOR] in the column
header is the propagation anchor for this table.

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

For each violated assumption in Step 2 column 4, trace the full causal chain from
[INERTIA COMPETITOR] behavior to support ticket.

**Complete the SRE row first.** SRE tickets determine the severity ceiling.

Column 2 (Incumbent [INERTIA COMPETITOR] behavior): state the specific behavior of
[INERTIA COMPETITOR] that created the expectation -- name [INERTIA COMPETITOR]
explicitly in each cell. The bracket-token [INERTIA COMPETITOR] in the column header
is the propagation anchor for this table.

| # | Persona class | Incumbent [INERTIA COMPETITOR] behavior | Imported expectation | What this feature does instead | Resulting failure mode | Ticket # |
|---|---------------|----------------------------------------|---------------------|-------------------------------|----------------------|----------|

Ticket #: LEAVE BLANK -- assigned in Step 6b. Complete at least 1 row.

```
ASSUMPTION AUDIT COMPLETE:
  Rows documented:                                         [N]
  SRE row present:                                         YES / NO
  All 5 non-ID columns populated for each row:             YES / NO
  Column 2 cells reference [INERTIA COMPETITOR] by name:   YES / NO -> PASS / FAIL
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

SRE row is listed first. The order mirrors Step 2 -- SRE leads in both tables,
ensuring the operational register anchors the vocabulary framework before Support
or PM/UX vocabulary is introduced.

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

**Per-category minimum commitment (set before writing entries):**
This registry requires >= 2 entries per category. Name your commitment now:
  Category 1 (Format violations) minimum: 2 entries
  Category 2 (Value violations) minimum:  2 entries

Why this minimum matters: 2 + 2 = 4 > 3. Per-category minimums of 2 make C-21's floor
(>= 3 total entries) provable from per-category counts alone -- neither category needs
to carry the full load. A per-category minimum of 1 (1 + 1 = 2 < 3) creates a single
point of verification failure. Set your minimum at 2 per category before writing entries.

REJECTION REGISTRY:

Category 1 -- Format violations (wrong or absent label structure):
  R-01: Flat list without dimension prefixes
        Example: "Markers: runbook, incident timeline"
        Why it fails: dimension classification absent; diversity unverifiable
  R-02: Same dimension prefix used twice
        Example: "operational=runbook | operational=runbook entry"
        Why it fails: count satisfied but register diversity not demonstrated
  R-03: Count without naming
        Example: "2 markers deployed"
        Why it fails: no specific marker named; citation cannot be verified

Category 2 -- Value violations (marker content fails register requirement):
  R-04: Role declarations used as markers
        Example: operational=As an SRE | frustration=Being a PM
  R-05: Generic verbs without register specificity
        Example: frustration=noticed | operational=tried
  R-06: Same-register synonym pairs
        Example: frustration=frustrated | frustration=annoyed
  R-07: Bare nouns without context-anchoring
        Example: operational=logs | operational=data

REGISTRY COMPLETENESS CHECK:
  Category 1 entries:        [N]  (required: >= 2)    -> PASS / FAIL
  Category 2 entries:        [N]  (required: >= 2)    -> PASS / FAIL
  Total entries:             [N]  (required: >= 3)    -> PASS / FAIL
  Floor guarantee: Cat 1 [N] + Cat 2 [N] = [sum], required > 3 -> PASS / FAIL
  Dual-category coverage:                                        -> PASS / FAIL

```
REGISTRY GATE:
  Per-category commitment honored (Cat 1 >= 2, Cat 2 >= 2):  YES / NO -> must be YES
  Floor guarantee sum > 3:                                    PASS / FAIL
  Dual-category coverage:                                     PASS / FAIL
  Registry applied during Step 7:                             CONFIRMED
```

Do not write any ticket body until REGISTRY GATE shows all conditions met.

---

## STEP 6 -- TICKET SUMMARY TABLE AND VALIDATION TRACE

Generate the ticket table. Assign severity consistent with the phase-severity prior
from Step 1. For tickets tracing to an assumption audit row, append "[A#N]" to title.

| # | Phase | Title | Category | Persona | Volume | Severity |
|---|-------|-------|----------|---------|--------|----------|

Allowed values:
- Phase: Phase 1 | Phase 2 | Phase 3
- Category: how-to | bug | feature-request | config | integration
- Persona: Support | SRE | PM | UX | C-01 through C-12
- Volume: high | medium | low
- Severity: P0 | P1 | P2 | P3

After completing the table, run the full validation trace:

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
    Phase 1 severities (P2/P3 expected):  [list actual values]   -> PASS / FAIL
    Phase 2 severities (P1/P2 expected):  [list actual values]   -> PASS / FAIL
    Phase 3 severities (P0/P1 expected):  [list actual values]   -> PASS / FAIL
  SRE is first row in Step 2 table:       YES / NO                -> PASS / FAIL
  SRE is first row in Step 5 table:       YES / NO                -> PASS / FAIL
  SRE row present in assumption audit:    YES / NO                -> PASS / FAIL
  SRE ticket present in this table:       YES / NO                -> PASS / FAIL
  Bracket-token propagation check:
    [INERTIA COMPETITOR] in Step 2 column header: YES / NO        -> PASS / FAIL
    [INERTIA COMPETITOR] in Step 3 column header: YES / NO        -> PASS / FAIL
    [INERTIA COMPETITOR] in Step 1b instruction:  YES / NO        -> PASS / FAIL
    >= 2 distinct bracket-token locations found:  YES / NO        -> PASS / FAIL
  Overall:                                                        -> PASS / FAIL
```

Do not proceed to Step 6b with VALIDATION TRACE showing FAIL.

---

## STEP 6b -- FORWARD-LINK

Go back to Step 3. For every assumption audit row, fill in the Ticket # column.

```
FORWARD-LINK GATE:
  Assumption audit rows total:                    [N]
  Rows with Ticket # assigned:                    [N]  -> must equal [N] -> PASS / FAIL
  All assigned Ticket # values exist in table:    YES / NO               -> PASS / FAIL
  Overall:                                        PASS / FAIL
```

Do not write any body with FORWARD-LINK GATE showing FAIL.

---

## STEP 7 -- TICKET BODIES WITH DIMENSION-LABELED MARKER CITATIONS

Write the way that person actually types. Do not open any body with a persona
declaration. Start with the issue.

For tickets with [A#N] tag: the body must contain comparison framing that references
[INERTIA COMPETITOR] -- the bracket-token [INERTIA COMPETITOR] in this instruction
names the comparison anchor. Use the specific product name declared in the preamble.

Each body deploys >= 2 markers from DIFFERENT columns of the assigned persona's voice
table row. Clear every marker against REJECTION REGISTRY before citing.

Format:

### Ticket [N] [Phase N]: [Title from table]
**Traces to:** Assumption #[N]   <- audit-linked only; omit for net-new
**Body:** [2-5 sentences in the persona's actual voice]
**Voice markers:** operational=[term] | frustration=[phrase]

---

After writing all bodies:

TIER-SEQUENCING RULE (preamble -- before opening the verification block):
  All TIER 1 per-pair gates must show PROCEED before TIER 2 is evaluated.
  Any pair showing REVISE: halt -- revise before advancing to REVISION GATE or Step 8.

```
BIDIRECTIONAL LINKAGE VERIFICATION:

  TIER ARCHITECTURE SELF-CHECK (complete before per-pair content):

  | Landmark | Expected location | Present | Result |
  |----------|-----------------|---------|--------|
  | TIER-SEQUENCING RULE field | Preamble above block | YES / NO | PASS / FAIL |
  | -- TIER 1: Per-Pair Verification -- header | Before per-pair blocks | YES / NO | PASS / FAIL |
  | -- TIER 2: Block-Level Clearance -- header | Before REVISION GATE | YES / NO | PASS / FAIL |

  All three PASS: YES -> proceed | Any FAIL: halt -- add missing landmark

  Forward direction: [N] of [N] rows have Ticket # assigned              -> PASS / FAIL
  Backward direction: [N] bodies have "Traces to:" field                 -> PASS / FAIL

  -- TIER 1: Per-Pair Verification --
    Assumption #[N] -> Ticket [N]:
      Audit phrase: "[direct quote -- min 5 words]"
      Body evidence: "[direct quote -- min 5 words]"
      Alignment: MATCH / MISMATCH
      Gate: PROCEED | REVISE
    [repeat for each pair]
  All TIER 1 pairs PROCEED: YES / NO                                     -> PASS / FAIL

  -- TIER 2: Block-Level Clearance --
  REVISION GATE:
    Mismatched pairs: [list or "none"]
    Gate status: OPEN | CLOSED
    Do not advance to Step 8 with Gate status = CLOSED.

  Overall: PASS / FAIL
```

---

## STEP 8 -- MARKER FORMAT AUDIT

```
MARKER FORMAT AUDIT:
  Total ticket bodies:                              [N]
  Bodies with >= 2 diff dimension prefixes:         [N]
  Flat-list citations (R-01):                       [N]  -> must be 0
  Same-dimension duplications (R-02):               [N]  -> must be 0
  Registry-violating marker values (R-04..R-07):    [N]  -> must be 0
  Dimension-labeled coverage (>= 60%):              [N]% -> PASS / FAIL
  Overall:                                               PASS / FAIL
```

---

## STEP 9 -- POST-GENERATION PHASE CONFIRMATION

```
PHASE CONFIRMATION:
  Phase 1 bodies: [gen] / [target]  -> MATCH / MISMATCH
  Phase 2 bodies: [gen] / [target]  -> MATCH / MISMATCH
  Phase 3 bodies: [gen] / [target]  -> MATCH / MISMATCH
  Total:          [gen] / [target]  -> MATCH / MISMATCH
```

---

## STEP 10 -- GAP ANALYSIS TABLE

Present the gap analysis as a structured table. No Classification cell may be blank.

Column definitions:
- Gap type: Doc | Design | Operational
- Specific artifact: the exact doc section, config field, API endpoint, runbook page,
  or UI element
- Classification: PARITY (incumbent already provides this; closing it is table stakes)
  or NET-NEW (no incumbent equivalent)
- Incumbent [INERTIA COMPETITOR] status: what [INERTIA COMPETITOR] offers here (or
  "no equivalent") -- the bracket-token [INERTIA COMPETITOR] in this column header
  names the comparison target; use the specific product name in each cell
- Phase first surfaces: Phase 1 | Phase 2 | Phase 3

| # | Gap type | Specific artifact | Classification | Incumbent [INERTIA COMPETITOR] status | Phase first surfaces |
|---|----------|------------------|----------------|--------------------------------------|---------------------|

Minimum: 1 Doc row, 1 Design row, 1 Operational row.

---

## STEP 11 -- THRESHOLD CONFIRMATION

```
THRESHOLD CONFIRMATION:

C-14 | Gap Classification Coverage
  Total gap entries:                              [N]
  Entries with PARITY or NET-NEW classification:  [N]
  Coverage (>= 60%):                              [N]% -> PASS / FAIL

C-16 | Voice Marker Citation Coverage
  Total ticket bodies:                            [N]
  Bodies with explicit "Voice markers:" citation: [N]
  Coverage (>= 60%):                              [N]% -> PASS / FAIL

C-12 | Voice Register Density
  Bodies with >= 2 markers from DIFFERENT dimensions: [N]
  Coverage (>= 60%):                              [N]% -> PASS / FAIL

C-31 | INERTIA COMPETITOR Name Propagation
  Preamble declaration present before Step 1:     YES / NO  -> PASS / FAIL
  Bodies containing declared name verbatim:       [N] / [N]
  Propagation coverage (>= 50%):                  [N]%      -> PASS / FAIL
  Step 10 Incumbent cells use declared name:      YES / NO  -> PASS / FAIL

C-32 | SRE-First Ordering
  SRE first in Step 2 STATUS QUO table:           YES / NO  -> PASS / FAIL
  SRE first in Step 5 PERSONA VOICE TABLE:        YES / NO  -> PASS / FAIL
  SRE row in assumption audit:                    YES / NO  -> PASS / FAIL
  SRE ticket in ticket table:                     YES / NO  -> PASS / FAIL

C-33 candidate | Bracket-Token Propagation
  [INERTIA COMPETITOR] token in Step 2 column header:   YES / NO -> PASS / FAIL
  [INERTIA COMPETITOR] token in Step 3 column header:   YES / NO -> PASS / FAIL
  [INERTIA COMPETITOR] token in Step 7 instruction:     YES / NO -> PASS / FAIL
  [INERTIA COMPETITOR] token in Step 10 column header:  YES / NO -> PASS / FAIL
  >= 2 distinct table-header bracket-token locations:   YES / NO -> PASS / FAIL
  Detectable by bracket-scan (no prose interpretation): YES / NO -> PASS / FAIL

Summary:
  C-14 gap classification:        PASS / FAIL
  C-16 marker citation:           PASS / FAIL
  C-12 voice density:             PASS / FAIL
  C-31 name propagation:          PASS / FAIL
  C-32 SRE-first:                 PASS / FAIL
  C-33 cand. bracket-token:       PASS / FAIL
  Overall: PASS (all) / FAIL (one or more)
```

If any threshold shows FAIL, identify entries or bodies causing the shortfall, revise,
and re-run this block before submitting.
```

---

## V-02: Single-Axis -- Propagation Chain Pre-Declaration (C-34)

**Axis:** A PROPAGATION CHAIN sub-block is added to the preamble, naming three
checkpoint labels (A, B, C) before Step 1 runs. The preamble declares what each
checkpoint is and where it is located. VALIDATION TRACE gains a completeness check
that verifies all three declared checkpoints are satisfied in the output.

**Probe (C-34 candidate):** C-31 requires three propagation checkpoints to exist in
the output but does not require the preamble to enumerate them. A scorer verifies
completeness by traversal -- reading every step to find all three. C-34 requires the
preamble to pre-declare the checkpoint contract so completeness is verifiable by
comparing the preamble declaration against output, not by traversal. Analogous to
C-29's advance over C-27: floor declared before generation, not just detected after.

**Hypothesis:** When the preamble names "Checkpoint A: Step 2 STATUS QUO column 2 uses
[product name]. Checkpoint B: Step 3 ASSUMPTION AUDIT column 2 cites [product name].
Checkpoint C: ticket bodies with [A#N] traces contain [product name] in >= 50%", the
model has a pre-declared contract to honor. A scorer can verify completeness by reading
the preamble declaration, then checking each checkpoint location directly -- no traversal
of all 11 steps needed. The criterion would require the preamble to declare all three
checkpoints by label before Step 1, and the VALIDATION TRACE to report each checkpoint
as satisfied or missing.

---

```
# listen-support: Predict First-90-Day Support Tickets

Work through each step in order. Do not skip steps. Do not combine steps.

---

INERTIA COMPETITOR: [name the specific product the target personas currently use for
this workflow -- one product name, grep-checkable, no generic labels like "legacy tool"
or "the incumbent"]

This name is a constant. Use it exactly in every step that references the prior tool.

PROPAGATION CHAIN:
  Checkpoint A: STATUS QUO ANCHOR (Step 2) -- column 2 uses this product name to
    describe prior behavior; cells must name this product, not a generic label
  Checkpoint B: ASSUMPTION AUDIT (Step 3) -- column 2 ("Incumbent behavior") cites
    this product name; the causal chain is anchored to a named product, not an
    abstraction
  Checkpoint C: Ticket bodies with [A#N] traces (Step 7) -- bodies linked to
    assumption audit rows contain this product name verbatim; propagation coverage
    >= 50% of all linked bodies

All three checkpoints must be satisfied in the output. Completeness is confirmed by
checking: (A) Step 2 column 2 cells, (B) Step 3 column 2 cells, (C) body count.

---

## STEP 1 -- PHASE-SEVERITY GRADIENT PRIOR

Before declaring targets or generating tickets, state the principled severity prior.

Phase 1 (Day 0-30): P2/P3. Workarounds exist; no committed production data. P0
reserved for activation blockers affecting all users simultaneously.

Phase 2 (Day 31-60): P1/P2. Workarounds have real cost. P0 exceptional: data loss or
workflow corruption under real load only.

Phase 3 (Day 61-90): P0/P1. No fallback at scale. P3 essentially absent.

```
PHASE-SEVERITY PRIOR:
  Phase 1 (Day 0-30):  typical P2/P3; P0 only for activation blockers affecting all users
  Phase 2 (Day 31-60): typical P1/P2; P0 exceptional (data loss or workflow corruption)
  Phase 3 (Day 61-90): typical P0/P1; P3 rare (users have exhausted workarounds)
```

---

## STEP 1b -- PHASE NARRATIVE

State the behavioral driver for each phase before any inertia or assumption analysis.
The Phase Distribution Target in Step 4 must be consistent with this narrative.

**Phase 1 (Day 0-30) -- First contact:**
Users are exploring the feature while keeping the prior tool active as a safety net.
Each step is compared against prior-tool behavior. Trigger event: first contact with a
feature behavior that diverges from the prior tool -- setup friction, missing
documentation, onboarding gaps. Tickets driven by volume but low severity (prior tool
fallback available).

**Phase 2 (Day 31-60) -- Committed trial:**
Users have invested real workflows; some are migrated, some still run in the prior
tool. Trigger event: first time a committed workflow hits a blocking gap -- a config
combination that works in the prior tool but fails here, or an integration boundary
assumed compatible. Tickets reflect partial-migration friction.

**Phase 3 (Day 61-90) -- Operational dependency:**
The prior tool is no longer available for this workflow. Trigger event: a blocking
failure under production conditions. Severity escalates because no fallback exists.

```
PHASE NARRATIVE COMPLETE:
  Phase 1 behavioral driver named:    YES / NO
  Phase 2 behavioral driver named:    YES / NO
  Phase 3 behavioral driver named:    YES / NO
  Trigger events named:               YES / NO
```

---

## STEP 2 -- STATUS QUO ANCHOR

Every support ticket in the first 90 days is a transition story. SRE row is listed
first -- SRE failure modes determine the severity ceiling for the entire ticket set.

Column 2 (Prior tool / STATUS QUO behavior): use the INERTIA COMPETITOR name declared
in the preamble -- not "the incumbent", not "legacy tool". This satisfies Checkpoint A
of the PROPAGATION CHAIN declared in the preamble.

| Persona class | Prior tool / STATUS QUO behavior | Key capability expected to carry over | Most likely violated assumption |
|---------------|----------------------------------|--------------------------------------|----------------------------------|
| SRE | | | |
| Support | | | |
| PM / UX | | | |
| C-01..C-04 (technical early adopters) | | | |
| C-05..C-08 (pragmatic mainstream) | | | |
| C-09..C-12 (enterprise/compliance) | | | |

Column 4 (violated assumption) feeds Step 3.

---

## STEP 3 -- ASSUMPTION AUDIT

For each violated assumption in Step 2 column 4, trace the full causal chain from
incumbent behavior to support ticket. **Complete the SRE row first.**

Column 2 (Incumbent behavior that created assumption): state the behavior using the
INERTIA COMPETITOR name declared in the preamble. This satisfies Checkpoint B of the
PROPAGATION CHAIN declared in the preamble.

| # | Persona class | Incumbent behavior that created assumption | Imported expectation | What this feature does instead | Resulting failure mode | Ticket # |
|---|---------------|------------------------------------------|---------------------|-------------------------------|----------------------|----------|

Ticket #: LEAVE BLANK -- assigned in Step 6b. Complete at least 1 row.

```
ASSUMPTION AUDIT COMPLETE:
  Rows documented:                                         [N]
  SRE row present:                                         YES / NO
  All 5 non-ID columns populated for each row:             YES / NO
  Column 2 cells use declared INERTIA COMPETITOR name:     YES / NO -> Checkpoint B
  Ticket IDs pending at Step 6b:                           [N] rows
```

---

## STEP 4 -- PHASE DISTRIBUTION TARGET

```
PHASE DISTRIBUTION TARGET:
  Phase 1 (Day 0-30):  [N] tickets   -- setup friction, first-impression errors
  Phase 2 (Day 31-60): [N] tickets   -- adoption edge cases, workflow friction
  Phase 3 (Day 61-90): [N] tickets   -- operational steady-state, integration issues
  Total:               [N] tickets
```

Constraints: Phase 1 >= 3. Phase 3 >= 1. Total >= 7. All three phases non-zero.

---

## STEP 5 -- PERSONA VOICE TABLE (DIMENSION REGISTRY)

SRE row is listed first. The order mirrors Step 2.

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

**Per-category minimum commitment (set before writing entries):**
  Category 1 (Format violations) minimum: 2 entries
  Category 2 (Value violations) minimum:  2 entries

Floor guarantee: 2 + 2 = 4 > 3. Per-category minimums of 2 make C-21's floor provable
from per-category counts alone.

REJECTION REGISTRY:

Category 1 -- Format violations:
  R-01: Flat list without dimension prefixes
  R-02: Same dimension prefix used twice
  R-03: Count without naming

Category 2 -- Value violations:
  R-04: Role declarations used as markers
  R-05: Generic verbs without register specificity
  R-06: Same-register synonym pairs
  R-07: Bare nouns without context-anchoring

REGISTRY COMPLETENESS CHECK:
  Category 1 entries: [N] (>= 2) -> PASS / FAIL
  Category 2 entries: [N] (>= 2) -> PASS / FAIL
  Total entries:      [N] (>= 3) -> PASS / FAIL
  Floor guarantee: Cat 1 [N] + Cat 2 [N] = [sum], required > 3 -> PASS / FAIL
  Dual-category coverage: -> PASS / FAIL

```
REGISTRY GATE:
  Per-category commitment honored (Cat 1 >= 2, Cat 2 >= 2):  YES / NO -> must be YES
  Floor guarantee sum > 3:                                    PASS / FAIL
  Dual-category coverage:                                     PASS / FAIL
  Registry applied during Step 7:                             CONFIRMED
```

Do not write any ticket body until REGISTRY GATE shows all conditions met.

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
    Phase 1: [N] / target [N]                                     -> MATCH / MISMATCH
    Phase 2: [N] / target [N]                                     -> MATCH / MISMATCH
    Phase 3: [N] / target [N]                                     -> MATCH / MISMATCH
  All personas in voice table:            YES / NO                -> PASS / FAIL
  >= 1 ticket linked to audit row:        YES / NO                -> PASS / FAIL
  Phase-severity consistent:
    Phase 1 severities (P2/P3 expected):  [list]                  -> PASS / FAIL
    Phase 2 severities (P1/P2 expected):  [list]                  -> PASS / FAIL
    Phase 3 severities (P0/P1 expected):  [list]                  -> PASS / FAIL
  SRE is first row in Step 2 table:       YES / NO                -> PASS / FAIL
  SRE is first row in Step 5 table:       YES / NO                -> PASS / FAIL
  SRE row present in assumption audit:    YES / NO                -> PASS / FAIL
  SRE ticket present in this table:       YES / NO                -> PASS / FAIL
  Propagation chain completeness (C-34 candidate):
    PROPAGATION CHAIN block in preamble:            YES / NO      -> PASS / FAIL
    Checkpoint A declared in preamble:              YES / NO      -> PASS / FAIL
    Checkpoint B declared in preamble:              YES / NO      -> PASS / FAIL
    Checkpoint C declared in preamble:              YES / NO      -> PASS / FAIL
    All three checkpoints A/B/C declared:           YES / NO      -> PASS / FAIL
    Checkpoint A satisfied (Step 2 col 2 uses name): YES / NO     -> PASS / FAIL
    Checkpoint B satisfied (Step 3 col 2 uses name): YES / NO     -> PASS / FAIL
    Checkpoint C satisfied (>= 50% body coverage):  YES / NO      -> PASS / FAIL
    All three checkpoints A/B/C satisfied:          YES / NO      -> PASS / FAIL
  Overall:                                                        -> PASS / FAIL
```

Do not proceed to Step 6b with VALIDATION TRACE showing FAIL.

---

## STEP 6b -- FORWARD-LINK

Go back to Step 3. For every assumption audit row, fill in the Ticket # column.

```
FORWARD-LINK GATE:
  Assumption audit rows total:                    [N]
  Rows with Ticket # assigned:                    [N]  -> must equal [N] -> PASS / FAIL
  All assigned Ticket # values exist in table:    YES / NO               -> PASS / FAIL
  Overall:                                        PASS / FAIL
```

---

## STEP 7 -- TICKET BODIES WITH DIMENSION-LABELED MARKER CITATIONS

Write the way that person actually types. Do not open with a persona declaration.

For tickets with [A#N] tag: the body must contain comparison framing using the exact
INERTIA COMPETITOR name from the preamble. This satisfies Checkpoint C of the
PROPAGATION CHAIN -- verbatim name appearance in the linked body.

Each body: >= 2 markers from DIFFERENT columns of the assigned persona's voice table
row. Clear every marker against REJECTION REGISTRY before citing.

Format:

### Ticket [N] [Phase N]: [Title from table]
**Traces to:** Assumption #[N]   <- audit-linked only; omit for net-new
**Body:** [2-5 sentences in the persona's actual voice]
**Voice markers:** operational=[term] | frustration=[phrase]

---

After writing all bodies:

TIER-SEQUENCING RULE (preamble -- before opening the verification block):
  All TIER 1 per-pair gates must show PROCEED before TIER 2 is evaluated.

```
BIDIRECTIONAL LINKAGE VERIFICATION:

  TIER ARCHITECTURE SELF-CHECK:
  | Landmark | Expected location | Present | Result |
  |----------|-----------------|---------|--------|
  | TIER-SEQUENCING RULE field | Preamble above block | YES / NO | PASS / FAIL |
  | -- TIER 1: Per-Pair Verification -- header | Before per-pair blocks | YES / NO | PASS / FAIL |
  | -- TIER 2: Block-Level Clearance -- header | Before REVISION GATE | YES / NO | PASS / FAIL |

  All three PASS: YES -> proceed | Any FAIL: halt -- add missing landmark

  Forward direction: [N] of [N] rows have Ticket # assigned              -> PASS / FAIL
  Backward direction: [N] bodies have "Traces to:" field                 -> PASS / FAIL

  -- TIER 1: Per-Pair Verification --
    Assumption #[N] -> Ticket [N]:
      Audit phrase: "[direct quote -- min 5 words]"
      Body evidence: "[direct quote -- min 5 words]"
      Alignment: MATCH / MISMATCH
      Gate: PROCEED | REVISE
    [repeat for each pair]
  All TIER 1 pairs PROCEED: YES / NO                                     -> PASS / FAIL

  -- TIER 2: Block-Level Clearance --
  REVISION GATE:
    Mismatched pairs: [list or "none"]
    Gate status: OPEN | CLOSED
    Do not advance to Step 8 with Gate status = CLOSED.

  Overall: PASS / FAIL
```

---

## STEP 8 -- MARKER FORMAT AUDIT

```
MARKER FORMAT AUDIT:
  Total bodies:                               [N]
  Bodies with >= 2 diff dimension prefixes:   [N]
  Flat-list (R-01): [N] -> 0 | Same-dim (R-02): [N] -> 0
  Registry-violating (R-04..R-07): [N] -> 0
  Coverage (>= 60%): [N]% -> PASS / FAIL | Overall: PASS / FAIL
```

---

## STEP 9 -- POST-GENERATION PHASE CONFIRMATION

```
PHASE CONFIRMATION:
  Phase 1: [gen] / [target] -> MATCH / MISMATCH
  Phase 2: [gen] / [target] -> MATCH / MISMATCH
  Phase 3: [gen] / [target] -> MATCH / MISMATCH
  Total:   [gen] / [target] -> MATCH / MISMATCH
```

---

## STEP 10 -- GAP ANALYSIS TABLE

| # | Gap type | Specific artifact | Classification | Incumbent status | Phase first surfaces |
|---|----------|------------------|----------------|-----------------|---------------------|

Classification: PARITY | NET-NEW.
Incumbent status: what the INERTIA COMPETITOR name declared in the preamble offers
here (or "no equivalent") -- use the declared name, not a generic label.
Minimum: 1 Doc row, 1 Design row, 1 Operational row.

---

## STEP 11 -- THRESHOLD CONFIRMATION

```
THRESHOLD CONFIRMATION:

C-14: [N]/[N] = [N]% (>= 60%) -> PASS / FAIL
C-16: [N]/[N] = [N]% (>= 60%) -> PASS / FAIL
C-12: [N]/[N] = [N]% (>= 60%) -> PASS / FAIL

C-31 | INERTIA COMPETITOR Propagation
  Preamble declaration present:           YES / NO -> PASS / FAIL
  Body propagation (>= 50%):              [N]%     -> PASS / FAIL
  Step 10 cells use declared name:        YES / NO -> PASS / FAIL

C-32 | SRE-First
  SRE first in Step 2: YES/NO | SRE first in Step 5: YES/NO
  SRE in audit: YES/NO | SRE ticket in table: YES/NO -> PASS / FAIL

C-34 candidate | Propagation Chain Pre-Declaration
  PROPAGATION CHAIN block in preamble:               YES / NO -> PASS / FAIL
  All three checkpoints A/B/C declared in preamble:  YES / NO -> PASS / FAIL
  Checkpoint A satisfied (Step 2 col 2):             YES / NO -> PASS / FAIL
  Checkpoint B satisfied (Step 3 col 2):             YES / NO -> PASS / FAIL
  Checkpoint C satisfied (body coverage >= 50%):     YES / NO -> PASS / FAIL
  Completeness verifiable from preamble declaration
  without traversal of all steps:                    YES / NO -> PASS / FAIL

Summary:
  C-14 / C-16 / C-12 / C-31 / C-32:  PASS / FAIL each
  C-34 cand. chain pre-declaration:   PASS / FAIL
  Overall: PASS (all) / FAIL (one or more)
```
```

---

## V-03: Single-Axis -- SRE-Write-First Enforcement Gate (C-35)

**Axis:** A named SRE-WRITE-FIRST GATE block is inserted at the boundary between the
PERSONA VOICE TABLE (Step 5) and ticket body writing (Step 7). The gate produces a
PASS/FAIL verdict and halts forward progress if SRE is not the first row in the voice
table. C-32's advisory write-first directive becomes a binding enforcement gate.

**Probe (C-35 candidate):** C-32 requires an advisory write-first directive for SRE
and a post-hoc VALIDATION TRACE check. Neither mechanism blocks body writing if the
voice table was assembled wrong. A model that lists Support as the first row in Step 5
can still proceed to Step 7 -- the error is caught at VALIDATION TRACE after bodies
are already written. C-35 requires a named gate block at the exact Step 5 -> Step 7
boundary that halts forward progress until SRE-first position is confirmed.

**Hypothesis:** When the advisory directive appears inside Step 5 prose, models may
acknowledge it (write "SRE is listed first") without actually reordering if Support
is more cognitively accessible. An enforcement gate block with an explicit PASS/FAIL
verdict and a "do not proceed" instruction creates the same structural interrupt that
FORWARD-LINK GATE (Step 6b) creates for assumption linkage: halt, verify, remediate
before advancing. The gate verdict is scannable independently of VALIDATION TRACE.

---

```
# listen-support: Predict First-90-Day Support Tickets

Work through each step in order. Do not skip steps. Do not combine steps.

---

INERTIA COMPETITOR: [name the specific product the target personas currently use for
this workflow -- one product name, grep-checkable, no generic labels like "legacy tool"
or "the incumbent"]

This name is a constant. Use it exactly in every step that references the prior tool.

---

## STEP 1 -- PHASE-SEVERITY GRADIENT PRIOR

Before declaring targets or generating tickets, state the principled severity prior.

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

State the behavioral driver for each phase before any inertia or assumption analysis.
The Phase Distribution Target in Step 4 must be consistent with this narrative.

**Phase 1 (Day 0-30) -- First contact:**
Users are exploring the feature while keeping the prior tool active as a safety net.
Trigger event: first contact with a feature behavior that diverges from prior-tool
behavior -- setup friction, missing documentation, onboarding gaps. Tickets driven by
volume but low severity (prior tool fallback available).

**Phase 2 (Day 31-60) -- Committed trial:**
Users have invested real workflows; some migrated, some still run in the prior tool.
Trigger event: first time a committed workflow hits a blocking gap -- a config
combination that works in the prior tool but fails here. Tickets reflect
partial-migration friction: no simple revert, but feature coverage incomplete.

**Phase 3 (Day 61-90) -- Operational dependency:**
The prior tool is no longer available for this workflow. Trigger event: a blocking
failure under production conditions. Severity escalates because no fallback exists.

```
PHASE NARRATIVE COMPLETE:
  Phase 1 behavioral driver named:    YES / NO
  Phase 2 behavioral driver named:    YES / NO
  Phase 3 behavioral driver named:    YES / NO
  Trigger events named:               YES / NO
```

---

## STEP 2 -- STATUS QUO ANCHOR

Every support ticket in the first 90 days is a transition story. SRE row is listed
first -- SRE failure modes determine the severity ceiling for the entire ticket set.

Column 2 (Prior tool / STATUS QUO behavior): use the INERTIA COMPETITOR name declared
in the preamble -- not "the incumbent", not "legacy tool".

| Persona class | Prior tool / STATUS QUO behavior | Key capability expected to carry over | Most likely violated assumption |
|---------------|----------------------------------|--------------------------------------|----------------------------------|
| SRE | | | |
| Support | | | |
| PM / UX | | | |
| C-01..C-04 (technical early adopters) | | | |
| C-05..C-08 (pragmatic mainstream) | | | |
| C-09..C-12 (enterprise/compliance) | | | |

Column 4 (violated assumption) feeds Step 3.

---

## STEP 3 -- ASSUMPTION AUDIT

For each violated assumption in Step 2 column 4, trace the full causal chain from
incumbent behavior to support ticket. **Complete the SRE row first.**

| # | Persona class | Incumbent behavior that created assumption | Imported expectation | What this feature does instead | Resulting failure mode | Ticket # |
|---|---------------|------------------------------------------|---------------------|-------------------------------|----------------------|----------|

Ticket #: LEAVE BLANK -- assigned in Step 6b. Complete at least 1 row.

```
ASSUMPTION AUDIT COMPLETE:
  Rows documented: [N]
  SRE row present: YES / NO
  All 5 non-ID columns populated: YES / NO
  Ticket IDs pending at Step 6b: [N] rows
```

---

## STEP 4 -- PHASE DISTRIBUTION TARGET

```
PHASE DISTRIBUTION TARGET:
  Phase 1 (Day 0-30):  [N] tickets   -- setup friction, first-impression errors
  Phase 2 (Day 31-60): [N] tickets   -- adoption edge cases, workflow friction
  Phase 3 (Day 61-90): [N] tickets   -- operational steady-state, integration issues
  Total:               [N] tickets
```

Constraints: Phase 1 >= 3. Phase 3 >= 1. Total >= 7. All three phases non-zero.

---

## STEP 5 -- PERSONA VOICE TABLE (DIMENSION REGISTRY)

SRE row is listed first. SRE leads in both this table and Step 2's STATUS QUO table,
ensuring the operational register anchors the vocabulary framework before Support or
PM/UX vocabulary is introduced.

Write SRE first. Do not reorder. The SRE-WRITE-FIRST GATE in Step 5c verifies this.

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

Floor guarantee: 2 + 2 = 4 > 3. Per-category minimums of 2 make C-21's floor provable
from per-category counts alone.

REJECTION REGISTRY:

Category 1 -- Format violations:
  R-01: Flat list without dimension prefixes
  R-02: Same dimension prefix used twice
  R-03: Count without naming

Category 2 -- Value violations:
  R-04: Role declarations used as markers
  R-05: Generic verbs without register specificity
  R-06: Same-register synonym pairs
  R-07: Bare nouns without context-anchoring

REGISTRY COMPLETENESS CHECK:
  Category 1 entries: [N] (>= 2) -> PASS / FAIL
  Category 2 entries: [N] (>= 2) -> PASS / FAIL
  Total entries:      [N] (>= 3) -> PASS / FAIL
  Floor guarantee: Cat 1 [N] + Cat 2 [N] = [sum], required > 3 -> PASS / FAIL
  Dual-category coverage: -> PASS / FAIL

```
REGISTRY GATE:
  Per-category commitment honored (Cat 1 >= 2, Cat 2 >= 2):  YES / NO -> must be YES
  Floor guarantee sum > 3:                                    PASS / FAIL
  Dual-category coverage:                                     PASS / FAIL
  Registry applied during Step 7:                             CONFIRMED
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
writing any ticket body. A FAIL here means Step 6's VALIDATION TRACE will also fail
the SRE-first checks -- fix at this gate, not downstream.

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
    Phase 1: [N] / target [N]                                     -> MATCH / MISMATCH
    Phase 2: [N] / target [N]                                     -> MATCH / MISMATCH
    Phase 3: [N] / target [N]                                     -> MATCH / MISMATCH
  All personas in voice table:            YES / NO                -> PASS / FAIL
  >= 1 ticket linked to audit row:        YES / NO                -> PASS / FAIL
  Phase-severity consistent:
    Phase 1 severities (P2/P3 expected):  [list]                  -> PASS / FAIL
    Phase 2 severities (P1/P2 expected):  [list]                  -> PASS / FAIL
    Phase 3 severities (P0/P1 expected):  [list]                  -> PASS / FAIL
  SRE is first row in Step 2 table:       YES / NO                -> PASS / FAIL
  SRE is first row in Step 5 table:       YES / NO                -> PASS / FAIL
  SRE-WRITE-FIRST GATE verdict (Step 5c): PASS / FAIL             -> PASS / FAIL
  SRE row present in assumption audit:    YES / NO                -> PASS / FAIL
  SRE ticket present in this table:       YES / NO                -> PASS / FAIL
  INERTIA COMPETITOR name propagation:
    Preamble declaration present:         YES / NO                -> PASS / FAIL
    Bodies with name verbatim: [N] / [N] (>= 50%)                -> PASS / FAIL
  Overall:                                                        -> PASS / FAIL
```

Do not proceed to Step 6b with VALIDATION TRACE showing FAIL.

---

## STEP 6b -- FORWARD-LINK

Go back to Step 3. For every assumption audit row, fill in the Ticket # column.

```
FORWARD-LINK GATE:
  Assumption audit rows total:                    [N]
  Rows with Ticket # assigned:                    [N]  -> must equal [N] -> PASS / FAIL
  All assigned Ticket # values exist in table:    YES / NO               -> PASS / FAIL
  Overall:                                        PASS / FAIL
```

---

## STEP 7 -- TICKET BODIES WITH DIMENSION-LABELED MARKER CITATIONS

Write SRE bodies first (if any SRE tickets are in the table). Then Support, PM/UX,
customer personas. This ordering mirrors Step 5's voice table and was confirmed by
the SRE-WRITE-FIRST GATE.

Write the way that person actually types. Do not open with a persona declaration.

For tickets with [A#N] tag: include comparison framing using the INERTIA COMPETITOR
name declared in the preamble.

Each body: >= 2 markers from DIFFERENT columns of the persona's voice table row.
Clear every marker against REJECTION REGISTRY before citing.

Format:

### Ticket [N] [Phase N]: [Title from table]
**Traces to:** Assumption #[N]   <- audit-linked only; omit for net-new
**Body:** [2-5 sentences in the persona's actual voice]
**Voice markers:** operational=[term] | frustration=[phrase]

---

After writing all bodies:

TIER-SEQUENCING RULE (preamble -- before opening the verification block):
  All TIER 1 per-pair gates must show PROCEED before TIER 2 is evaluated.

```
BIDIRECTIONAL LINKAGE VERIFICATION:

  TIER ARCHITECTURE SELF-CHECK:
  | Landmark | Expected location | Present | Result |
  |----------|-----------------|---------|--------|
  | TIER-SEQUENCING RULE field | Preamble above block | YES / NO | PASS / FAIL |
  | -- TIER 1: Per-Pair Verification -- header | Before per-pair blocks | YES / NO | PASS / FAIL |
  | -- TIER 2: Block-Level Clearance -- header | Before REVISION GATE | YES / NO | PASS / FAIL |

  All three PASS: YES -> proceed | Any FAIL: halt

  Forward direction: [N] of [N] rows have Ticket # assigned              -> PASS / FAIL
  Backward direction: [N] bodies have "Traces to:" field                 -> PASS / FAIL

  -- TIER 1: Per-Pair Verification --
    Assumption #[N] -> Ticket [N]:
      Audit phrase: "[direct quote -- min 5 words]"
      Body evidence: "[direct quote -- min 5 words]"
      Alignment: MATCH / MISMATCH
      Gate: PROCEED | REVISE
    [repeat for each pair]
  All TIER 1 pairs PROCEED: YES / NO                                     -> PASS / FAIL

  -- TIER 2: Block-Level Clearance --
  REVISION GATE:
    Mismatched pairs: [list or "none"]
    Gate status: OPEN | CLOSED
    Do not advance to Step 8 with Gate status = CLOSED.

  Overall: PASS / FAIL
```

---

## STEP 8 -- MARKER FORMAT AUDIT

```
MARKER FORMAT AUDIT:
  Total bodies:                               [N]
  Bodies with >= 2 diff dimension prefixes:   [N]
  Flat-list (R-01): [N] -> 0 | Same-dim (R-02): [N] -> 0
  Registry-violating (R-04..R-07): [N] -> 0
  Coverage (>= 60%): [N]% -> PASS / FAIL | Overall: PASS / FAIL
```

---

## STEP 9 -- POST-GENERATION PHASE CONFIRMATION

```
PHASE CONFIRMATION:
  Phase 1: [gen] / [target] -> MATCH / MISMATCH
  Phase 2: [gen] / [target] -> MATCH / MISMATCH
  Phase 3: [gen] / [target] -> MATCH / MISMATCH
  Total:   [gen] / [target] -> MATCH / MISMATCH
```

---

## STEP 10 -- GAP ANALYSIS TABLE

| # | Gap type | Specific artifact | Classification | Incumbent status | Phase first surfaces |
|---|----------|------------------|----------------|-----------------|---------------------|

Classification: PARITY | NET-NEW.
Incumbent status: what the INERTIA COMPETITOR name declared in the preamble offers
here (or "no equivalent") -- use the declared name, not a generic label.
Minimum: 1 Doc row, 1 Design row, 1 Operational row.

---

## STEP 11 -- THRESHOLD CONFIRMATION

```
THRESHOLD CONFIRMATION:

C-14: [N]/[N] = [N]% (>= 60%) -> PASS / FAIL
C-16: [N]/[N] = [N]% (>= 60%) -> PASS / FAIL
C-12: [N]/[N] = [N]% (>= 60%) -> PASS / FAIL

C-31 | INERTIA COMPETITOR Propagation
  Preamble present: YES/NO | Body coverage >= 50%: [N]% | Step 10 cells: YES/NO
  -> PASS / FAIL

C-32 | SRE-First Ordering
  SRE first in Step 2: YES/NO | SRE first in Step 5: YES/NO
  SRE in audit: YES/NO | SRE ticket in table: YES/NO -> PASS / FAIL

C-35 candidate | SRE-Write-First Enforcement Gate
  SRE-WRITE-FIRST GATE block present at Step 5 -> Step 7 boundary: YES / NO -> PASS / FAIL
  Gate produces explicit PASS/FAIL verdict:                        YES / NO -> PASS / FAIL
  Gate has "do not proceed" halt instruction:                      YES / NO -> PASS / FAIL
  Gate was invoked before any body was written:                    YES / NO -> PASS / FAIL
  Gate verdict in output:                                          PASS / FAIL
  Advisory directive (C-32) upgraded to binding gate (C-35):      YES / NO -> PASS / FAIL

Summary:
  C-14 / C-16 / C-12 / C-31 / C-32:  PASS / FAIL each
  C-35 cand. enforcement gate:        PASS / FAIL
  Overall: PASS (all) / FAIL (one or more)
```
```

---

## V-04: Combined -- Bracket-Token Propagation + Propagation Chain Pre-Declaration (V-01 + V-02)

**Axes combined:** `[INERTIA COMPETITOR]` bracket-token in column headers and
instruction clauses (V-01) + PROPAGATION CHAIN sub-block pre-declaring checkpoints
A/B/C in the preamble (V-02).

**Combination hypothesis:** V-01 makes propagation detectable by bracket-pattern
scan; V-02 makes completeness verifiable from the preamble declaration without
traversal. The two mechanisms are additive: V-01 answers "is the token present at
this location?" (grep-checkable), V-02 answers "are all declared checkpoints satisfied?"
(comparison-checkable). A prompt with both allows a scorer to (1) grep for
`[INERTIA COMPETITOR]` to find all propagation points, then (2) compare against the
declared PROPAGATION CHAIN to confirm all three checkpoints are covered. Neither
mechanism conflicts with the other -- the bracket-token is a formatting change to
column headers and instructions; the chain pre-declaration is a preamble contract.

**C-33 + C-34 candidates:** Both apply. V-04 is expected to satisfy C-33 (bracket-token
in >= 2 table column headers) and C-34 (PROPAGATION CHAIN pre-declared with A/B/C
labels) simultaneously while maintaining all C-01 through C-32 compliance.

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
    behavior" uses the bracket-token; column 2 cells name this product
  Checkpoint B: ASSUMPTION AUDIT (Step 3) -- column header "Incumbent [INERTIA COMPETITOR]
    behavior" uses the bracket-token; column 2 cells cite this product
  Checkpoint C: Ticket bodies with [A#N] traces (Step 7) -- bodies linked to assumption
    audit rows contain this product name verbatim; coverage >= 50% of linked bodies

Completeness verification: (A) grep Step 2 column header for bracket-token, (B) grep
Step 3 column header for bracket-token, (C) count bodies with verbatim product name.
All three must be satisfied.

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
net. Trigger event: first contact with a feature behavior that diverges from
[INERTIA COMPETITOR] -- setup friction, missing docs, onboarding gaps.

**Phase 2 (Day 31-60) -- Committed trial:**
Users have invested real workflows; some migrated, some still in [INERTIA COMPETITOR].
Trigger event: first time a committed workflow hits a blocking gap -- a config
combination that works in [INERTIA COMPETITOR] but fails here.

**Phase 3 (Day 61-90) -- Operational dependency:**
[INERTIA COMPETITOR] no longer available for this workflow. Trigger event: blocking
failure under production conditions with no fallback.

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

| Persona class | Prior [INERTIA COMPETITOR] behavior | Key capability expected to carry over | Most likely violated assumption |
|---------------|-------------------------------------|--------------------------------------|----------------------------------|
| SRE | | | |
| Support | | | |
| PM / UX | | | |
| C-01..C-04 (technical early adopters) | | | |
| C-05..C-08 (pragmatic mainstream) | | | |
| C-09..C-12 (enterprise/compliance) | | | |

Column 2 instruction: for each row, name the specific behavior of [INERTIA COMPETITOR]
that taught this persona class to expect X. Column 4 (violated assumption) feeds Step 3.

---

## STEP 3 -- ASSUMPTION AUDIT

**Complete the SRE row first.**

Column 2 (Incumbent [INERTIA COMPETITOR] behavior): state the specific behavior of
[INERTIA COMPETITOR] that created the expectation. The bracket-token
[INERTIA COMPETITOR] in the column header is Checkpoint B of the PROPAGATION CHAIN.

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

SRE row is listed first. The order mirrors Step 2.

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
    Phase 1: [N] / target [N]                                     -> MATCH / MISMATCH
    Phase 2: [N] / target [N]                                     -> MATCH / MISMATCH
    Phase 3: [N] / target [N]                                     -> MATCH / MISMATCH
  All personas in voice table:            YES / NO                -> PASS / FAIL
  >= 1 ticket linked to audit row:        YES / NO                -> PASS / FAIL
  Phase-severity consistent:
    Phase 1 (P2/P3): [list] | Phase 2 (P1/P2): [list] | Phase 3 (P0/P1): [list]
    -> PASS / FAIL
  SRE first in Step 2: YES/NO | SRE first in Step 5: YES/NO
  SRE in audit: YES/NO | SRE ticket in table: YES/NO              -> PASS / FAIL
  Bracket-token propagation (C-33 candidate):
    [INERTIA COMPETITOR] in Step 2 column header: YES / NO        -> Checkpoint A
    [INERTIA COMPETITOR] in Step 3 column header: YES / NO        -> Checkpoint B
    >= 2 distinct bracket-token table-header locations: YES / NO  -> PASS / FAIL
  Propagation chain completeness (C-34 candidate):
    PROPAGATION CHAIN block in preamble:            YES / NO      -> PASS / FAIL
    All checkpoints A/B/C declared:                 YES / NO      -> PASS / FAIL
    Checkpoint A satisfied:                         YES / NO      -> PASS / FAIL
    Checkpoint B satisfied:                         YES / NO      -> PASS / FAIL
    Checkpoint C satisfied (>= 50% body coverage):  YES / NO      -> PASS / FAIL
  Overall:                                                        -> PASS / FAIL
```

---

## STEP 6b -- FORWARD-LINK

```
FORWARD-LINK GATE:
  Assumption audit rows total: [N] | Rows with Ticket # assigned: [N] -> PASS / FAIL
  All Ticket # values exist in table: YES / NO -> PASS / FAIL | Overall: PASS / FAIL
```

---

## STEP 7 -- TICKET BODIES WITH DIMENSION-LABELED MARKER CITATIONS

Write the way that person actually types. Do not open with a persona declaration.

For tickets with [A#N] tag: body must reference [INERTIA COMPETITOR] verbatim. This
satisfies Checkpoint C of the PROPAGATION CHAIN.

Each body: >= 2 markers from DIFFERENT columns of the persona's voice table row.

Format:

### Ticket [N] [Phase N]: [Title from table]
**Traces to:** Assumption #[N]
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

  Forward: [N]/[N] rows have Ticket # | Backward: [N] bodies have "Traces to:"

  -- TIER 1: Per-Pair Verification --
    Assumption #[N] -> Ticket [N]:
      Audit phrase: "[quote]" | Body evidence: "[quote]"
      Alignment: MATCH/MISMATCH | Gate: PROCEED | REVISE
  All TIER 1 PROCEED: YES/NO -> PASS / FAIL

  -- TIER 2: Block-Level Clearance --
  REVISION GATE: Mismatched pairs: [list/"none"] | Status: OPEN | CLOSED
  Overall: PASS / FAIL
```

---

## STEP 8 -- MARKER FORMAT AUDIT

```
MARKER FORMAT AUDIT:
  Bodies with >= 2 diff prefixes: [N] | Flat-list: [N]->0 | Same-dim: [N]->0
  Registry-violating: [N]->0 | Coverage (>= 60%): [N]% -> PASS/FAIL | Overall: PASS/FAIL
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

| # | Gap type | Specific artifact | Classification | Incumbent [INERTIA COMPETITOR] status | Phase first surfaces |
|---|----------|------------------|----------------|--------------------------------------|---------------------|

Column 4 instruction: for each row, name what [INERTIA COMPETITOR] offers here (or
"no equivalent") -- the bracket-token [INERTIA COMPETITOR] in the column header names
the comparison target.
Minimum: 1 Doc, 1 Design, 1 Operational row. Classification: PARITY | NET-NEW.

---

## STEP 11 -- THRESHOLD CONFIRMATION

```
THRESHOLD CONFIRMATION:

C-14: [N]/[N] = [N]% (>= 60%) -> PASS / FAIL
C-16: [N]/[N] = [N]% (>= 60%) -> PASS / FAIL
C-12: [N]/[N] = [N]% (>= 60%) -> PASS / FAIL

C-31: Preamble YES/NO | Body >= 50%: [N]% | Step 10 cells YES/NO -> PASS / FAIL
C-32: SRE first Step 2 YES/NO | SRE first Step 5 YES/NO | SRE audit YES/NO -> PASS/FAIL

C-33 candidate | Bracket-Token Propagation
  [INERTIA COMPETITOR] in Step 2 col header: YES/NO -> Checkpoint A
  [INERTIA COMPETITOR] in Step 3 col header: YES/NO -> Checkpoint B
  [INERTIA COMPETITOR] in Step 10 col header: YES/NO
  [INERTIA COMPETITOR] in Step 7 instruction: YES/NO
  >= 2 distinct table-header locations:       YES/NO -> PASS / FAIL

C-34 candidate | Propagation Chain Pre-Declaration
  PROPAGATION CHAIN block in preamble:               YES/NO -> PASS / FAIL
  All A/B/C declared before Step 1:                  YES/NO -> PASS / FAIL
  Checkpoint A satisfied:                            YES/NO -> PASS / FAIL
  Checkpoint B satisfied:                            YES/NO -> PASS / FAIL
  Checkpoint C satisfied (>= 50% body coverage):     YES/NO -> PASS / FAIL
  Completeness verifiable from preamble declaration: YES/NO -> PASS / FAIL

Summary:
  C-14 / C-16 / C-12 / C-31 / C-32: PASS/FAIL each
  C-33 cand. bracket-token:  PASS / FAIL
  C-34 cand. chain pre-decl: PASS / FAIL
  Overall: PASS (all) / FAIL (one or more)
```
```

---

## V-05: Full Synthesis -- Bracket-Token + Chain Pre-Declaration + SRE Gate (V-01 + V-02 + V-03)

**Axes combined:** All three R12 axes: `[INERTIA COMPETITOR]` bracket-token in column
headers and instruction clauses (V-01) + PROPAGATION CHAIN sub-block with A/B/C labels
pre-declared in preamble (V-02) + SRE-WRITE-FIRST GATE block at Step 5 -> Step 7
boundary (V-03).

**Combination hypothesis:** The three axes address three distinct failure modes:
- V-01: competitor name drifts to generic labels in prose -- caught by bracket-scan
- V-02: propagation completeness is unverifiable without traversal -- caught by preamble
  contract comparison
- V-03: SRE-first ordering is advisory, not enforced -- caught by binding gate verdict

Together they form a pipeline: declare the propagation chain contract (V-02) -> embed
bracket-tokens at declared checkpoints (V-01) -> enforce SRE-first ordering before any
body is written (V-03). Each gate catches a different failure class. The three mechanisms
stack without conflict: chain pre-declaration describes what checkpoints exist; bracket
tokens make each checkpoint grep-detectable; the SRE gate blocks ordering failures
before they propagate into bodies.

**C-33 + C-34 + C-35 candidates:** All three apply. V-05 is the strongest expected
satisfier of all three new criterion candidates while maintaining all C-01 through
C-32 compliance.

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
writing any ticket body. A FAIL here means Step 6's VALIDATION TRACE will also fail
SRE-first checks -- fix at this gate, not downstream.

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
  Bracket-token propagation (C-33 candidate):
    [INERTIA COMPETITOR] in Step 2 column header: YES / NO        -> Checkpoint A
    [INERTIA COMPETITOR] in Step 3 column header: YES / NO        -> Checkpoint B
    [INERTIA COMPETITOR] in Step 7 instruction:   YES / NO
    [INERTIA COMPETITOR] in Step 10 col header:   YES / NO
    >= 2 distinct table-header bracket-token locations: YES / NO  -> PASS / FAIL
  Propagation chain completeness (C-34 candidate):
    PROPAGATION CHAIN block in preamble:            YES / NO      -> PASS / FAIL
    All checkpoints A/B/C declared before Step 1:   YES / NO      -> PASS / FAIL
    Checkpoint A satisfied (Step 2 col header):     YES / NO      -> PASS / FAIL
    Checkpoint B satisfied (Step 3 col header):     YES / NO      -> PASS / FAIL
    Checkpoint C satisfied (>= 50% linked bodies):  YES / NO      -> PASS / FAIL
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

C-33 candidate | Bracket-Token Propagation
  [INERTIA COMPETITOR] in Step 2 column header (Checkpoint A): YES/NO -> PASS / FAIL
  [INERTIA COMPETITOR] in Step 3 column header (Checkpoint B): YES/NO -> PASS / FAIL
  [INERTIA COMPETITOR] in Step 7 instruction clause:           YES/NO -> PASS / FAIL
  [INERTIA COMPETITOR] in Step 10 column header:               YES/NO -> PASS / FAIL
  >= 2 distinct table-header bracket-token locations:          YES/NO -> PASS / FAIL
  Detectable by bracket-scan without prose interpretation:     YES/NO -> PASS / FAIL

C-34 candidate | Propagation Chain Pre-Declaration
  PROPAGATION CHAIN block in preamble before Step 1:            YES/NO -> PASS / FAIL
  All three checkpoints A/B/C named with locations:             YES/NO -> PASS / FAIL
  Checkpoint A satisfied (Step 2 header has bracket-token):     YES/NO -> PASS / FAIL
  Checkpoint B satisfied (Step 3 header has bracket-token):     YES/NO -> PASS / FAIL
  Checkpoint C satisfied (>= 50% linked body coverage):         YES/NO -> PASS / FAIL
  Completeness verifiable from preamble (no traversal needed):  YES/NO -> PASS / FAIL

C-35 candidate | SRE-Write-First Enforcement Gate
  SRE-WRITE-FIRST GATE block present at Step 5 -> Step 7 boundary: YES/NO -> PASS / FAIL
  Gate produces explicit PASS/FAIL verdict:                        YES/NO -> PASS / FAIL
  Gate has "do not proceed" halt instruction:                      YES/NO -> PASS / FAIL
  Gate was invoked before any body was written:                    YES/NO -> PASS / FAIL
  Gate verdict in this output:                                     PASS / FAIL
  Advisory write-first (C-32) upgraded to binding gate (C-35):    YES/NO -> PASS / FAIL

Summary:
  C-14 / C-16 / C-12:     PASS / FAIL each
  C-31 name propagation:   PASS / FAIL
  C-32 SRE-first:          PASS / FAIL
  C-33 cand. bracket-token:    PASS / FAIL
  C-34 cand. chain pre-decl:   PASS / FAIL
  C-35 cand. enforce gate:     PASS / FAIL
  Overall: PASS (all) / FAIL (one or more)
```

If any threshold shows FAIL, identify the specific entries or bodies causing the
shortfall, revise, and re-run this block before submitting.
```
