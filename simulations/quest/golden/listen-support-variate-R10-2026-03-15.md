# listen-support Round 10 -- Skill Body Prompt Variations

**Date:** 2026-03-15
**Rubric target:** v10 (30 criteria -- C-01 through C-30)
**Base:** V-05 R9 (C-01 through C-30 ceiling; preamble rule + upstream commitment +
table self-check all active)

**Variation axes selected** (3 single-axis, then 2 combined):

1. **INERTIA COMPETITOR declared as labeled preamble before all analysis (C-31 candidate)**
   -- Add a labeled `INERTIA COMPETITOR:` block as the very first element of the prompt,
   before the Phase-Severity Prior. All subsequent steps reference the competitor by the
   exact declared name. The VALIDATION TRACE gains a propagation check. Hypothesis: When
   the competitor first appears inside Step 2's multi-column table, models may use generic
   labels ("the incumbent", "the prior tool") in ticket bodies and verification steps. An
   upfront declaration anchors the name before any analysis, making every later reference
   grep-checkable and preventing label drift across 11 steps. (V-01)

2. **SRE-first ordering in STATUS QUO table and PERSONA VOICE TABLE (C-32 candidate)**
   -- Reorder Step 2's STATUS QUO ANCHOR and Step 5's PERSONA VOICE TABLE so SRE appears
   as the first row, before Support and PM/UX. Add an explicit instruction to Step 3's
   ASSUMPTION AUDIT: "Complete the SRE row first -- SRE tickets determine the severity
   ceiling; the entire ticket set's character depends on SRE failure-mode coverage."
   Hypothesis: When Support or PM/UX appear first, SRE may receive fewer assumption-audit
   rows by end of generation. SRE-first ordering seeds the severity ceiling with
   operational precedent before lower-severity personas are analyzed. (V-02)

3. **PHASE NARRATIVE block inserted between severity prior and STATUS QUO (C-33 candidate)**
   -- Add a PHASE NARRATIVE section after Step 1 and before Step 2, naming the behavioral
   driver for each phase: what users are doing, what event triggers ticket filing, how the
   tool relationship evolves. Hypothesis: Without a behavioral narrative, models fill phase
   distributions proportionally without reasoning about WHY ticket character changes. The
   narrative forces explicit adoption-curve reasoning, producing more accurate severity
   distributions and ticket bodies that reflect phase-appropriate user contexts rather than
   generic slot-filling. (V-03)

4. **V-01 + V-02 combined** -- Inertia competitor preamble + SRE-first ordering. Both
   mechanisms are independent: the preamble is a positional anchor before all steps; the
   SRE ordering is a sequence commitment inside Step 2, 3, and 5. Neither shares state
   with the other. (V-04)

5. **Full synthesis** -- All three axes: inertia preamble + SRE-first + phase narrative.
   (V-05)

**Axes carried from R9 (active in all R10 variations as baseline):**
- TIER-SEQUENCING RULE as preamble before block header -- R9 V-01 (C-28)
- Per-category minimum instruction with arithmetic rationale in Step 5b setup -- R9 V-02 (C-29)
- TIER ARCHITECTURE SELF-CHECK as scannable table -- R9 V-03 (C-26 / C-30)
- Floor guarantee computation row in REGISTRY COMPLETENESS CHECK -- R8 V-02
- Named tier headers (TIER 1 / TIER 2) -- R7 V-03
- Per-category minimums >= 2 -- R7 V-01
- Total-count floor row naming C-21 floor -- R7 V-02
- Phase-severity gradient prior -- R1
- STATUS QUO anchor / inertia map -- R2
- Assumption audit 6-column chain with Ticket # pending -- R2 / R3
- Phase distribution target with phase-labeled constraints -- R1
- Persona voice table as dimension registry -- R2
- Pre-generation VALIDATION TRACE -- R2
- FORWARD-LINK GATE -- R3
- Ticket bodies with "Traces to:" field + comparison framing -- R3
- Per-pair content alignment evidence with inline Gate: PROCEED|REVISE -- R6 V-01
- Block-level REVISION GATE sub-block with OPEN|CLOSED -- R6 V-02
- Dual-category rejection registry -- R6 V-03
- MARKER FORMAT AUDIT
- Post-generation phase confirmation
- Gap analysis classification table (PARITY / NET-NEW)
- THRESHOLD CONFIRMATION block (C-14, C-16, C-12)

**New in R10:**
- C-31 candidate: INERTIA COMPETITOR named as labeled preamble before Step 1 -- V-01, V-04, V-05
- C-32 candidate: SRE-first ordering in STATUS QUO and VOICE TABLE -- V-02, V-04, V-05
- C-33 candidate: PHASE NARRATIVE behavioral driver block -- V-03, V-05

---

## V-01: Single-Axis -- INERTIA COMPETITOR as Labeled Preamble Before All Analysis (C-31)

**Axis:** A labeled `INERTIA COMPETITOR:` declaration appears as the first element of
the prompt body, before STEP 1. Every subsequent step uses this exact product name --
not a generic label. The VALIDATION TRACE gains a propagation check that verifies the
declared name appears verbatim in ticket bodies.
**Hypothesis:** In R9's baseline, the competitor name first appears in Step 2's STATUS QUO
table as a column 2 cell. A model may use generic substitutions ("the incumbent", "the
prior tool", "legacy system") in Steps 3, 5, 7, and 10 -- steps that don't redeclare the
name. A preamble declaration before Step 1 makes the name a constant accessible to all
steps, and the propagation check in VALIDATION TRACE makes label drift detectable.

---

```
# listen-support: Predict First-90-Day Support Tickets

Work through each step in order. Do not skip steps. Do not combine steps.

---

INERTIA COMPETITOR: [name the specific product the target personas currently use for
this workflow -- one product name, grep-checkable, no generic labels like "legacy tool"
or "the incumbent"]

This name is a constant. Use it exactly -- no synonyms, no generic substitutions -- in
every step that references the prior tool. Steps 2, 3, 5, 7, and 10 all reference it.

---

## STEP 1 -- PHASE-SEVERITY GRADIENT PRIOR

Before declaring targets or generating tickets, state the principled severity prior.
This prior matters because identical functional problems carry different severity
depending on when they surface -- Phase 1 users have workarounds; Phase 3 users running
production traffic at scale do not.

Phase 1 (Day 0-30): Users are still exploring. Severity is P2/P3 because workarounds
exist and no one has committed irreplaceable data to the feature. P0 in Phase 1 is
reserved for hard activation blockers affecting all users simultaneously -- an extremely
high bar that excludes configuration confusion, missing docs, and edge-case bugs.

Phase 2 (Day 31-60): Users have invested. A config combination that breaks a committed
production workflow is P1 because workarounds have real cost. P0 is possible only for
data loss or workflow corruption under real load -- not for convenience gaps.

Phase 3 (Day 61-90): Systems run at scale with real business dependencies. P0 appears
here because partial failures under load cascade. Missing operational tooling (no health
endpoint, no runbook section) turns a recoverable incident into an extended outage. P3
is essentially absent -- users at scale have no tolerance for easy-workaround issues.

```
PHASE-SEVERITY PRIOR:
  Phase 1 (Day 0-30):  typical P2/P3; P0 only for activation blockers affecting all users
  Phase 2 (Day 31-60): typical P1/P2; P0 exceptional (data loss or workflow corruption)
  Phase 3 (Day 61-90): typical P0/P1; P3 rare (users have exhausted workarounds)
```

---

## STEP 2 -- STATUS QUO ANCHOR

Every support ticket in the first 90 days is a transition story. Name the prior tool
and the violated assumption to make ticket prediction precise.

Column 2 (Prior tool / STATUS QUO behavior): use the INERTIA COMPETITOR name declared
in the preamble -- not "the incumbent", not "legacy tool", not any generic label.

| Persona class | Prior tool / STATUS QUO behavior | Key capability they expect to carry over | Most likely violated assumption |
|---------------|----------------------------------|------------------------------------------|----------------------------------|
| Support | | | |
| SRE | | | |
| PM / UX | | | |
| C-01..C-04 (technical early adopters) | | | |
| C-05..C-08 (pragmatic mainstream) | | | |
| C-09..C-12 (enterprise/compliance) | | | |

This is your inertia map. Column 4 (violated assumption) feeds Step 3.

---

## STEP 3 -- ASSUMPTION AUDIT

For each violated assumption in column 4, trace the full causal chain from incumbent
behavior to support ticket. State the incumbent behavior -- not the category.

| # | Persona class | Incumbent behavior that created assumption | Imported expectation | What this feature does instead | Resulting failure mode | Ticket # |
|---|---------------|------------------------------------------|---------------------|-------------------------------|----------------------|----------|

Column definitions:
- Incumbent behavior: the specific thing the INERTIA COMPETITOR did that taught users
  to expect X. State the behavior using the INERTIA COMPETITOR name where applicable.
- Imported expectation: the exact assumption, as a first-person belief statement.
- What this feature does instead: the specific divergence.
- Resulting failure mode: the symptom -- what the user will type in the ticket.
- Ticket #: LEAVE BLANK -- assigned in Step 6b after the ticket table is generated.

Complete at least 1 row.

```
ASSUMPTION AUDIT COMPLETE:
  Rows documented: [N]
  All 5 non-ID columns populated for each row: YES / NO
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

Build the vocabulary table before writing any bodies. The column headers become the
required dimension prefixes for all marker citations in Step 7.

| Persona | Operational vocabulary | Frustration register | Framing conventions |
|---------|----------------------|---------------------|---------------------|
| Support | (>= 2 specific terms) | (>= 2 specific phrases) | (>= 2 structural patterns) |
| SRE | (>= 2 specific terms) | (>= 2 specific phrases) | (>= 2 structural patterns) |
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
to carry the full load. A per-category minimum of 1 (1 + 1 = 2 < 3) would require the
total row to carry the entire proof; that creates a single point of verification failure.
Set your minimum at 2 per category before writing any entries.

REJECTION REGISTRY:

Category 1 -- Format violations (wrong or absent label structure):
  R-01: Flat list without dimension prefixes
        Example: "Markers: runbook, incident timeline"
        Why it fails: dimension classification is absent; cross-register diversity is
        unverifiable without the scorer reading and classifying each marker themselves
  R-02: Same dimension prefix used twice
        Example: "operational=runbook | operational=runbook entry"
        Why it fails: one dimension cited twice satisfies count but not register diversity
  R-03: Count without naming
        Example: "2 markers deployed" or "operational and framing markers used"
        Why it fails: no specific marker is named; the citation cannot be verified

Category 2 -- Value violations (marker content fails semantic register requirement):
  R-04: Role declarations used as markers
        Example: operational=As an SRE | frustration=Being a PM
        Why it fails: declares the author's role, not professional vocabulary
  R-05: Generic verbs without register specificity
        Example: frustration=noticed | operational=tried | frustration=encountered
        Why it fails: these verbs appear in tickets written by any persona
  R-06: Same-register synonym pairs
        Example: frustration=frustrated | frustration=annoyed
        Why it fails: two words from the same emotional register count as one dimension
  R-07: Bare nouns without context-anchoring
        Example: operational=logs | operational=data | frustration=error
        Why it fails: universality defeats register specificity

REGISTRY COMPLETENESS CHECK:
  Category 1 (Format violations) entries:          [N]  (required: >= 2)   -> PASS / FAIL
  Category 2 (Value violations) entries:           [N]  (required: >= 2)   -> PASS / FAIL
  Total entries (Category 1 + Category 2):         [N]  (required: >= 3)   -> PASS / FAIL
  Floor guarantee: Cat 1 min [N] + Cat 2 min [N] = [sum], required > 3    -> PASS / FAIL
  Dual-category coverage:                                                   -> PASS / FAIL

```
REGISTRY GATE:
  Per-category commitment honored (Cat 1 >= 2, Cat 2 >= 2):    YES / NO -> must be YES
  All 7 rejection entries reviewed:                             YES / NO -> must be YES
  Registry completeness check -- Category 1:                   PASS / FAIL
  Registry completeness check -- Category 2:                   PASS / FAIL
  Total entries >= 3 (C-21 floor):                             PASS / FAIL
  Floor guarantee (sum > 3):                                   PASS / FAIL
  Dual-category coverage:                                      PASS / FAIL
  Registry will be applied during Step 7 citation:             CONFIRMED
```

Do not write any ticket body until REGISTRY GATE shows all conditions met.

---

## STEP 6 -- TICKET SUMMARY TABLE AND VALIDATION TRACE

Generate the ticket table with a Phase column. Assign severity consistent with the
phase-severity prior from Step 1. For tickets that trace to an assumption audit row,
append the audit reference to the title (e.g., "[Title] [A#1]").

| # | Phase | Title | Category | Persona | Volume | Severity |
|---|-------|-------|----------|---------|--------|----------|

Allowed values -- no other values are valid:
- Phase: Phase 1 | Phase 2 | Phase 3
- Category: how-to | bug | feature-request | config | integration
- Persona: Support | SRE | PM | UX | C-01 through C-12
- Volume: high | medium | low
- Severity: P0 | P1 | P2 | P3

After completing the table, run the full validation trace:

```
VALIDATION TRACE:
  Distinct categories:                    [N] (required: >= 3)            -> PASS / FAIL
  Distinct personas:                      [N] (required: >= 2)            -> PASS / FAIL
  P0 count:                               [N] (required: <= 1)            -> PASS / FAIL
  Low/medium volume entries:              [N] (required: >= 1)            -> PASS / FAIL
  Total rows:                             [N] (required: >= 7)            -> PASS / FAIL
  Phase 1 rows:                           [N] (target: [N from Step 4])  -> MATCH / MISMATCH
  Phase 2 rows:                           [N] (target: [N from Step 4])  -> MATCH / MISMATCH
  Phase 3 rows:                           [N] (target: [N from Step 4])  -> MATCH / MISMATCH
  All personas in voice table:            YES / NO                        -> PASS / FAIL
  >= 1 ticket linked to audit row:        YES / NO                        -> PASS / FAIL
  Phase-severity consistent with prior:
    Phase 1 severities (P2/P3 expected):  [list actual values]           -> PASS / FAIL
    Phase 2 severities (P1/P2 expected):  [list actual values]           -> PASS / FAIL
    Phase 3 severities (P0/P1 expected):  [list actual values]           -> PASS / FAIL
  INERTIA COMPETITOR name propagation:
    Preamble declaration present:         YES / NO                        -> PASS / FAIL
    Name appears verbatim in bodies (count / total bodies):
      [N] / [N]  (required: >= 50%)                                      -> PASS / FAIL
  Overall:                                                                -> PASS / FAIL
```

Do not proceed to Step 6b with VALIDATION TRACE showing FAIL.

---

## STEP 6b -- FORWARD-LINK: ASSIGN TICKET IDs TO ASSUMPTION AUDIT

Go back to Step 3. For every assumption audit row, fill in the Ticket # column with
the specific ticket number that captures that failure mode.

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

For each table row, write the ticket body. Write the way that person actually types.
Do not open any body with a persona declaration. Start with the issue.

For tickets with [A#N] tag: the body must contain comparison framing using the exact
INERTIA COMPETITOR name from the preamble. Do not substitute generic labels.

Each body deploys at least 2 markers from DIFFERENT columns of the assigned persona's
voice table row. Verify every marker against the REJECTION REGISTRY before citing.

REQUIRED citation format:
  Voice markers: operational=[specific term] | frustration=[specific phrase]
  Voice markers: operational=[specific term] | framing=[structural pattern]
  Voice markers: frustration=[specific phrase] | framing=[structural pattern]

Format:

### Ticket [N] [Phase N]: [Title from table]
**Traces to:** Assumption #[N]  <- audit-linked only; omit for net-new
**Body:** [2-5 sentences in the persona's actual voice]
**Voice markers:** operational=[term] | frustration=[phrase]

---

After writing all bodies:

TIER-SEQUENCING RULE (preamble -- before opening the verification block):
  All TIER 1 per-pair gates must show PROCEED before TIER 2 is evaluated.
  Any pair showing REVISE: halt -- do not advance to REVISION GATE or Step 8
  until all per-pair gates show PROCEED.

```
BIDIRECTIONAL LINKAGE VERIFICATION:

  TIER ARCHITECTURE SELF-CHECK (complete before per-pair content):

  | Landmark | Expected location | Present | Result |
  |----------|-----------------|---------|--------|
  | TIER-SEQUENCING RULE field | Preamble above block | YES / NO | PASS / FAIL |
  | -- TIER 1: Per-Pair Verification -- header | Before per-pair blocks | YES / NO | PASS / FAIL |
  | -- TIER 2: Block-Level Clearance -- header | Before REVISION GATE | YES / NO | PASS / FAIL |

  All three PASS: YES -> proceed | Any FAIL: halt -- add missing landmark before proceeding

  Forward direction (assumption audit -> ticket):
    Rows with Ticket # assigned: [N] of [N] rows                        -> PASS / FAIL
  Backward direction (ticket body -> assumption):
    Bodies with "Traces to: Assumption #N" field: [N]
    Matches forward-link row count: YES / NO                             -> PASS / FAIL

  -- TIER 1: Per-Pair Verification --
  Content alignment evidence (one block per linked assumption-ticket pair):
    Assumption #[N] -> Ticket [N]:
      Audit phrase (from Step 3 -- minimum 5 words):
        "[direct quote]"
      Body evidence (from ticket body -- minimum 5 words):
        "[direct quote]"
      Alignment: MATCH / MISMATCH
      Gate: PROCEED | REVISE -> incorporate "[audit phrase]" into Ticket [N] body;
            re-run this verification block before advancing to TIER 2
    [repeat for each additional linked pair]
  All TIER 1 pairs PROCEED: YES / NO                                     -> PASS / FAIL

  -- TIER 2: Block-Level Clearance --
  REVISION GATE:
    Mismatched pairs: [list Ticket # values, or "none"]
    Gate status: OPEN | CLOSED
      OPEN  = all TIER 1 gates PROCEED -- advance to Step 8
      CLOSED = one or more TIER 1 pairs MISMATCH -- revisions required before TIER 2
               can be OPEN
    Do not advance to Step 8 with Gate status = CLOSED.

  Overall:                                                               PASS / FAIL
```

---

## STEP 8 -- MARKER FORMAT AUDIT

```
MARKER FORMAT AUDIT:
  Total ticket bodies:                              [N]
  Bodies with "Voice markers:" citation line:       [N]
  Bodies with >= 2 DIFFERENT dimension prefixes:    [N]
  Bodies with flat-list citation (no prefixes):     [N]  -> must be 0 (R-01)
  Bodies with same-dimension duplication:           [N]  -> must be 0 (R-02)
  Bodies with registry-violating marker values:     [N]  -> must be 0
    (R-04: role declaration / R-05: generic verb / R-06: synonym pair / R-07: bare noun)
  Dimension-labeled coverage (2+ diff / total):     [N]%
    (required: >= 60%)                              -> PASS / FAIL
  Overall:                                          PASS / FAIL
```

---

## STEP 9 -- POST-GENERATION PHASE CONFIRMATION

```
PHASE CONFIRMATION:
  Phase 1 bodies generated: [N]   Target: [N]   -> MATCH / MISMATCH
  Phase 2 bodies generated: [N]   Target: [N]   -> MATCH / MISMATCH
  Phase 3 bodies generated: [N]   Target: [N]   -> MATCH / MISMATCH
  Total bodies:             [N]   Target: [N]   -> MATCH / MISMATCH
```

---

## STEP 10 -- GAP ANALYSIS TABLE

Present the gap analysis as a structured table. No Classification cell may be blank.

| # | Gap type | Specific artifact to create or change | Classification | Incumbent status | Phase first surfaces |
|---|----------|--------------------------------------|----------------|-----------------|---------------------|

Column definitions:
- Gap type: Doc | Design | Operational
- Specific artifact: the exact doc section, config field, API endpoint, runbook page,
  or UI element
- Classification: PARITY (incumbent already provides this; closing it is table stakes)
  or NET-NEW (no incumbent equivalent; represents differentiation or feature-promise gap)
- Incumbent status: what [INERTIA COMPETITOR name from preamble] offers here (or "no
  incumbent equivalent") -- use the exact declared name, not a generic label
- Phase first surfaces: Phase 1 | Phase 2 | Phase 3

Minimum: 1 Doc row, 1 Design row, 1 Operational row.

---

## STEP 11 -- THRESHOLD CONFIRMATION

```
THRESHOLD CONFIRMATION:

C-14 | Gap Classification Coverage
  Total gap entries in table:                     [N]
  Entries with PARITY or NET-NEW classification:  [N]
  Coverage:                                       [N]%
    (required: >= 60%)                            -> PASS / FAIL

C-16 | Voice Marker Citation Coverage
  Total ticket bodies:                            [N]
  Bodies with explicit "Voice markers:" citation: [N]
  Coverage:                                       [N]%
    (required: >= 60%)                            -> PASS / FAIL

C-12 | Voice Register Density
  Total ticket bodies:                            [N]
  Bodies with >= 2 markers from DIFFERENT
  register dimensions:                            [N]
  Coverage:                                       [N]%
    (required: >= 60%)                            -> PASS / FAIL

C-31 candidate | INERTIA COMPETITOR Name Propagation
  Preamble declaration present before Step 1:     YES / NO   -> PASS / FAIL
  Bodies containing declared name verbatim:       [N] / [N]
  Propagation coverage:                           [N]%
    (required: >= 50%)                            -> PASS / FAIL
  Step 10 Incumbent status cells use declared
  name (not generic label):                       YES / NO   -> PASS / FAIL

Summary:
  C-14 gap classification:        PASS / FAIL
  C-16 marker citation:           PASS / FAIL
  C-12 voice density:             PASS / FAIL
  C-31 cand. name propagation:    PASS / FAIL
  Overall threshold status: PASS (all four) / FAIL (one or more)
```

If any threshold shows FAIL, identify the specific entries or bodies causing the
shortfall, revise, and re-run this block before submitting.
```

---

## V-02: Single-Axis -- SRE-First Role Ordering in STATUS QUO and PERSONA VOICE TABLE (C-32)

**Axis:** Step 2's STATUS QUO ANCHOR table and Step 5's PERSONA VOICE TABLE are reordered
so SRE appears as the first row. Step 3's ASSUMPTION AUDIT instruction adds an explicit
sequencing directive: "Complete the SRE row first before other persona classes."
**Hypothesis:** In R9's baseline, Support is the first row in both tables. When Support
leads, models tend to generate more Support assumption rows -- the first role anchors the
analytical frame. SRE failure modes set the operational severity ceiling; if SRE rows are
analyzed last (or not at all after earlier rows fill the budget), the ticket set may lack
the P0/P1 operational scenarios that make the support prediction credible. SRE-first
ordering propagates through tables and instruction text as a consistent signal.

---

```
# listen-support: Predict First-90-Day Support Tickets

Work through each step in order. Do not skip steps. Do not combine steps.

---

## STEP 1 -- PHASE-SEVERITY GRADIENT PRIOR

Before declaring targets or generating tickets, state the principled severity prior.

Phase 1 (Day 0-30): P2/P3. Workarounds exist; no committed production data. P0 reserved
for activation blockers affecting all users simultaneously.

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

## STEP 2 -- STATUS QUO ANCHOR

Every support ticket in the first 90 days is a transition story. Name the prior tool
and the violated assumption to make ticket prediction precise.

SRE row is listed first. SRE failure modes determine the severity ceiling for the entire
ticket set. Complete the SRE row with the same depth as all other rows -- do not leave
it sparse because it appears first.

| Persona class | Prior tool / STATUS QUO behavior | Key capability they expect to carry over | Most likely violated assumption |
|---------------|----------------------------------|------------------------------------------|----------------------------------|
| SRE | | | |
| Support | | | |
| PM / UX | | | |
| C-01..C-04 (technical early adopters) | | | |
| C-05..C-08 (pragmatic mainstream) | | | |
| C-09..C-12 (enterprise/compliance) | | | |

This is your inertia map. Column 4 (violated assumption) feeds Step 3.

---

## STEP 3 -- ASSUMPTION AUDIT

Trace the full causal chain from incumbent behavior to support ticket.

**Complete the SRE row first.** SRE tickets determine the severity ceiling; the entire
ticket set's character depends on SRE failure-mode coverage. After SRE, complete Support,
then PM/UX, then customer personas.

| # | Persona class | Incumbent behavior that created assumption | Imported expectation | What this feature does instead | Resulting failure mode | Ticket # |
|---|---------------|------------------------------------------|---------------------|-------------------------------|----------------------|----------|

Ticket #: LEAVE BLANK -- assigned in Step 6b. Complete at least 1 row.

```
ASSUMPTION AUDIT COMPLETE:
  Rows documented: [N]
  SRE row present: YES / NO
  All 5 non-ID columns populated for each row: YES / NO
  Ticket IDs pending at Step 6b: [N] rows
```

---

## STEP 4 -- PHASE DISTRIBUTION TARGET

```
PHASE DISTRIBUTION TARGET:
  Phase 1 (Day 0-30):  [N] tickets
  Phase 2 (Day 31-60): [N] tickets
  Phase 3 (Day 61-90): [N] tickets
  Total:               [N] tickets
```

Constraints: Phase 1 >= 3. Phase 3 >= 1. Total >= 7.

---

## STEP 5 -- PERSONA VOICE TABLE (DIMENSION REGISTRY)

SRE row is listed first. The order here mirrors Step 2 -- SRE leads in both tables,
ensuring the operational register anchors the vocabulary framework before Support or
PM/UX vocabulary is introduced.

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
        Why it fails: dimension classification absent; cross-register diversity unverifiable
  R-02: Same dimension prefix used twice
        Example: "operational=runbook | operational=runbook entry"
        Why it fails: count satisfied but register diversity not demonstrated
  R-03: Count without naming
        Example: "2 markers deployed" or "operational and framing markers used"
        Why it fails: no specific marker named; citation cannot be verified

Category 2 -- Value violations (marker content fails register requirement):
  R-04: Role declarations used as markers
        Example: operational=As an SRE | frustration=Being a PM
        Why it fails: declares author's role, not professional vocabulary
  R-05: Generic verbs without register specificity
        Example: frustration=noticed | operational=tried | frustration=encountered
        Why it fails: universal across all personas
  R-06: Same-register synonym pairs
        Example: frustration=frustrated | frustration=annoyed
        Why it fails: two words from same emotional register count as one dimension
  R-07: Bare nouns without context-anchoring
        Example: operational=logs | operational=data | frustration=error
        Why it fails: universality defeats register specificity

REGISTRY COMPLETENESS CHECK:
  Category 1 entries:        [N]  (required: >= 2)    -> PASS / FAIL
  Category 2 entries:        [N]  (required: >= 2)    -> PASS / FAIL
  Total entries:             [N]  (required: >= 3)    -> PASS / FAIL
  Floor guarantee: Cat 1 min [N] + Cat 2 min [N] = [sum], required > 3 -> PASS / FAIL
  Dual-category coverage:                             -> PASS / FAIL

```
REGISTRY GATE:
  Per-category commitment honored (Cat 1 >= 2, Cat 2 >= 2):  YES / NO -> must be YES
  Floor guarantee sum > 3:                                    PASS / FAIL
  All other conditions met:                                   PASS / FAIL
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
  Distinct categories:              [N] (>= 3)              -> PASS / FAIL
  Distinct personas:                [N] (>= 2)              -> PASS / FAIL
  P0 count:                         [N] (<= 1)              -> PASS / FAIL
  Low/medium volume entries:        [N] (>= 1)              -> PASS / FAIL
  Total rows:                       [N] (>= 7)              -> PASS / FAIL
  Phase distribution:
    Phase 1: [N] / target [N from Step 4]                   -> MATCH / MISMATCH
    Phase 2: [N] / target [N from Step 4]                   -> MATCH / MISMATCH
    Phase 3: [N] / target [N from Step 4]                   -> MATCH / MISMATCH
  All personas in voice table:      YES / NO                -> PASS / FAIL
  >= 1 ticket linked to audit row:  YES / NO                -> PASS / FAIL
  Phase-severity consistent:
    Phase 1 severities (P2/P3):     [list]                  -> PASS / FAIL
    Phase 2 severities (P1/P2):     [list]                  -> PASS / FAIL
    Phase 3 severities (P0/P1):     [list]                  -> PASS / FAIL
  SRE is first row in Step 2 table: YES / NO                -> PASS / FAIL
  SRE is first row in Step 5 table: YES / NO                -> PASS / FAIL
  SRE row present in assumption audit (Step 3): YES / NO    -> PASS / FAIL
  SRE ticket present in this table: YES / NO                -> PASS / FAIL
  Overall:                                                   -> PASS / FAIL
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

For tickets with [A#N] tag: include comparison framing traceable to the audit row.
Each body: >= 2 markers from DIFFERENT columns of the persona's voice table row.
Clear every marker against REJECTION REGISTRY before citing.

Format:
### Ticket [N] [Phase N]: [Title]
**Traces to:** Assumption #[N]
**Body:** [2-5 sentences]
**Voice markers:** operational=[term] | frustration=[phrase]

After writing all bodies:

TIER-SEQUENCING RULE (preamble -- before opening the verification block):
  All TIER 1 per-pair gates must show PROCEED before TIER 2 is evaluated.
  Any pair showing REVISE: halt -- do not advance to REVISION GATE or Step 8
  until all per-pair gates show PROCEED.

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
  Bodies with >= 2 diff dimension prefixes: [N]
  Flat-list (R-01): [N] -> 0 | Same-dimension (R-02): [N] -> 0
  Registry-violating values (R-04--R-07): [N] -> 0
  Coverage: [N]% (>= 60%) -> PASS / FAIL  |  Overall: PASS / FAIL
```

---

## STEP 9 -- POST-GENERATION PHASE CONFIRMATION

```
PHASE CONFIRMATION:
  Ph1: [gen]/[tgt] -> MATCH/MISMATCH
  Ph2: [gen]/[tgt] -> MATCH/MISMATCH
  Ph3: [gen]/[tgt] -> MATCH/MISMATCH
  Total: [gen]/[tgt] -> MATCH/MISMATCH
```

---

## STEP 10 -- GAP ANALYSIS TABLE

| # | Gap type | Specific artifact | Classification | Incumbent status | Phase first surfaces |
|---|----------|------------------|----------------|-----------------|---------------------|

Classification: PARITY | NET-NEW. Minimum: 1 Doc, 1 Design, 1 Operational row.

---

## STEP 11 -- THRESHOLD CONFIRMATION

```
THRESHOLD CONFIRMATION:
  C-14: [N]/[N] = [N]% (>= 60%) -> PASS / FAIL
  C-16: [N]/[N] = [N]% (>= 60%) -> PASS / FAIL
  C-12: [N]/[N] = [N]% (>= 60%) -> PASS / FAIL
  C-32 cand.: SRE first in Step 2: YES/NO | SRE first in Step 5: YES/NO
              SRE in audit: YES/NO | SRE ticket in table: YES/NO -> PASS / FAIL
  Overall: PASS (all four) / FAIL (one or more)
```
```

---

## V-03: Single-Axis -- PHASE NARRATIVE Block for Behavioral Driver (C-33)

**Axis:** A PHASE NARRATIVE block is inserted after STEP 1 (phase-severity prior) and
before STEP 2 (STATUS QUO anchor). Each phase receives 2-3 sentences naming the behavioral
driver: what users are doing in that phase, what event triggers ticket filing, and how
their relationship to the tool evolves. This block is referenced from Step 4's phase
distribution target instructions.
**Hypothesis:** Without a behavioral narrative, the phase distribution in Step 4 is set
by numeric guessing rather than causal reasoning. Models fill the phases proportionally
(e.g., 3/3/2) without asking "what is happening on Day 45 that makes this a ticket?"
The narrative forces a behavioral hypothesis for each phase window before any analysis
begins. When the ticket table is generated, the model can verify each ticket's phase
assignment against the narrative rather than just against the severity prior.

---

```
# listen-support: Predict First-90-Day Support Tickets

Work through each step in order. Do not skip steps. Do not combine steps.

---

## STEP 1 -- PHASE-SEVERITY GRADIENT PRIOR

Before declaring targets or generating tickets, state the principled severity prior.

Phase 1 (Day 0-30): P2/P3. Workarounds exist; no committed production data. P0 reserved
for activation blockers affecting all users simultaneously.

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
This narrative describes WHAT USERS ARE DOING -- not just what severity to expect.
The Phase Distribution Target in Step 4 must be consistent with this narrative.

**Phase 1 (Day 0-30) -- First contact:**
Users are exploring the feature while keeping the prior tool active as a safety net.
They encounter the feature for the first time, attempt initial setup, and compare
each step against prior-tool behavior. The trigger event for Phase 1 tickets is first
contact with a feature behavior that differs from the prior tool -- setup friction,
missing documentation for the first-use path, and onboarding gaps. Tickets are
driven by volume (many users hitting the same first-contact moment) but low severity
(prior tool fallback available).

**Phase 2 (Day 31-60) -- Committed trial:**
Users have invested real workflows into the feature. Some workflows are migrated;
others still run in the prior tool. The trigger event for Phase 2 tickets is the
first time a committed workflow hits a blocking gap -- a config combination that
works in the prior tool but fails here, an integration boundary the user assumed
was compatible, or an edge case that didn't surface in Phase 1 exploration. Tickets
reflect the friction of partial migration: the user can't simply revert, but the
feature doesn't fully cover their committed workflow.

**Phase 3 (Day 61-90) -- Operational dependency:**
Users are running production traffic with real business dependencies on the feature.
The prior tool is no longer available for this workflow. The trigger event for Phase 3
tickets is a blocking failure under operational conditions -- a failure mode that
doesn't surface in non-production use. Severity escalates because no fallback is
available and the business impact is immediate. Tickets are fewer but higher severity:
each one represents a production blocker, not a discovery gap.

```
PHASE NARRATIVE COMPLETE:
  Phase 1 behavioral driver named:   YES / NO
  Phase 2 behavioral driver named:   YES / NO
  Phase 3 behavioral driver named:   YES / NO
  Trigger events named for all three phases: YES / NO
```

---

## STEP 2 -- STATUS QUO ANCHOR

Every support ticket in the first 90 days is a transition story. The Phase Narrative
established the behavioral context; this table names the specific tool and assumption
that create friction within that context.

| Persona class | Prior tool / STATUS QUO behavior | Key capability they expect to carry over | Most likely violated assumption |
|---------------|----------------------------------|------------------------------------------|----------------------------------|
| Support | | | |
| SRE | | | |
| PM / UX | | | |
| C-01..C-04 (technical early adopters) | | | |
| C-05..C-08 (pragmatic mainstream) | | | |
| C-09..C-12 (enterprise/compliance) | | | |

Column 4 (violated assumption) feeds Step 3.

---

## STEP 3 -- ASSUMPTION AUDIT

Trace the full causal chain from incumbent behavior to support ticket. When assigning
rows to phases, verify each failure mode's phase assignment is consistent with the
Phase Narrative in Step 1b: Phase 1 failures surface at first contact; Phase 2 failures
surface after workflow commitment; Phase 3 failures surface under production load.

| # | Persona class | Incumbent behavior that created assumption | Imported expectation | What this feature does instead | Resulting failure mode | Ticket # |
|---|---------------|------------------------------------------|---------------------|-------------------------------|----------------------|----------|

Ticket #: LEAVE BLANK -- assigned in Step 6b. Complete at least 1 row.

```
ASSUMPTION AUDIT COMPLETE:
  Rows documented: [N]
  All 5 non-ID columns populated: YES / NO
  Ticket IDs pending at Step 6b: [N] rows
```

---

## STEP 4 -- PHASE DISTRIBUTION TARGET

Set phase counts consistent with the Phase Narrative in Step 1b. Each count should
reflect the behavioral driver stated there: Phase 1 volume is driven by first-contact
breadth; Phase 3 count is driven by the number of distinct operational failure modes.

```
PHASE DISTRIBUTION TARGET:
  Phase 1 (Day 0-30):  [N] tickets   -- first-contact volume [consistent with Phase 1 narrative]
  Phase 2 (Day 31-60): [N] tickets   -- committed-workflow friction [consistent with Phase 2]
  Phase 3 (Day 61-90): [N] tickets   -- production blocking failures [consistent with Phase 3]
  Total:               [N] tickets
```

Constraints: Phase 1 >= 3. Phase 3 >= 1. Total >= 7.

Phase count rationale (brief): [one sentence per phase explaining why this count follows
from the Phase Narrative -- not just "3 because it meets the minimum"]

---

## STEP 5 -- PERSONA VOICE TABLE (DIMENSION REGISTRY)

| Persona | Operational vocabulary | Frustration register | Framing conventions |
|---------|----------------------|---------------------|---------------------|
| Support | (>= 2 specific terms) | (>= 2 specific phrases) | (>= 2 structural patterns) |
| SRE | (>= 2 specific terms) | (>= 2 specific phrases) | (>= 2 structural patterns) |
| [other personas used] | (>= 2 specific terms) | (>= 2 specific phrases) | (>= 2 structural patterns) |

Prefixes: operational= | frustration= | framing=
Disqualified: role declarations, generic verbs, bare nouns.

---

## STEP 5b -- DIMENSION-LABEL REJECTION REGISTRY

**Per-category minimum commitment (set before writing entries):**
Each category must contain >= 2 entries independently. Commit now:
  Category 1 minimum: 2 entries
  Category 2 minimum: 2 entries

Rationale: 2 + 2 = 4 > 3. Per-category floors of 2 make C-21's total floor (>= 3)
provable from per-category counts alone -- neither category needs the other's entries
to guarantee compliance. Minimum of 1 per category (1 + 1 = 2 < 3) creates a
single-point-of-verification architecture. Commit to >= 2 per category before writing.

REJECTION REGISTRY:

Category 1 -- Format violations:
  R-01: Flat list without dimension prefixes -- dimension classification absent
  R-02: Same dimension prefix used twice -- register diversity not demonstrated
  R-03: Count without naming -- specific marker absent; citation unverifiable

Category 2 -- Value violations:
  R-04: Role declarations used as markers -- role identity, not vocabulary
  R-05: Generic verbs without register specificity -- universal across all personas
  R-06: Same-register synonym pairs -- two words, one register dimension
  R-07: Bare nouns without context-anchoring -- universality defeats specificity

REGISTRY COMPLETENESS CHECK:
  Category 1 entries:        [N]  (required: >= 2)    -> PASS / FAIL
  Category 2 entries:        [N]  (required: >= 2)    -> PASS / FAIL
  Total entries:             [N]  (required: >= 3)    -> PASS / FAIL
  Floor guarantee: Cat 1 min [N] + Cat 2 min [N] = [sum], required > 3 -> PASS / FAIL
  Dual-category coverage:                             -> PASS / FAIL

```
REGISTRY GATE:
  Per-category commitment honored (Cat 1 >= 2, Cat 2 >= 2):  YES / NO -> must be YES
  Floor guarantee sum > 3:                                    PASS / FAIL -> must be PASS
  All other conditions met:                                   PASS / FAIL
  Registry applied during Step 7:  CONFIRMED
```

---

## STEP 6 -- TICKET SUMMARY TABLE AND VALIDATION TRACE

| # | Phase | Title | Category | Persona | Volume | Severity |
|---|-------|-------|----------|---------|--------|----------|

```
VALIDATION TRACE:
  Distinct categories: [N] (>= 3)   -> PASS / FAIL
  Distinct personas:   [N] (>= 2)   -> PASS / FAIL
  P0 count:            [N] (<= 1)   -> PASS / FAIL
  Low/medium volume:   [N] (>= 1)   -> PASS / FAIL
  Total rows:          [N] (>= 7)   -> PASS / FAIL
  Phase distribution:  Ph1 [N]/[tgt] Ph2 [N]/[tgt] Ph3 [N]/[tgt] -> MATCH/MISMATCH
  Phase-severity:      Ph1 [P2/P3] Ph2 [P1/P2] Ph3 [P0/P1]       -> PASS / FAIL
  Phase-narrative consistency:
    Phase 1 tickets reflect first-contact behavioral driver:        YES / NO -> PASS/FAIL
    Phase 2 tickets reflect committed-workflow behavioral driver:   YES / NO -> PASS/FAIL
    Phase 3 tickets reflect production-blocking behavioral driver:  YES / NO -> PASS/FAIL
  Overall:                                                          -> PASS / FAIL
```

---

## STEP 6b -- FORWARD-LINK

```
FORWARD-LINK GATE:
  Rows total / assigned: [N] / [N]  -> PASS / FAIL
  All Ticket # in table: YES / NO   -> PASS / FAIL
  Overall: PASS / FAIL
```

---

## STEP 7 -- TICKET BODIES WITH DIMENSION-LABELED MARKER CITATIONS

Write the way that person actually types. Do not open with a persona declaration.
For audit-linked tickets: include comparison framing traceable to Step 3.
Each body: >= 2 markers from DIFFERENT columns of the persona's voice table row.

Format:
### Ticket [N] [Phase N]: [Title]
**Traces to:** Assumption #[N]
**Body:** [2-5 sentences; reflects the phase behavioral driver from Step 1b]
**Voice markers:** operational=[term] | frustration=[phrase]

After writing all bodies:

TIER-SEQUENCING RULE (preamble -- before opening the verification block):
  All TIER 1 per-pair gates must show PROCEED before TIER 2 is evaluated.
  Any pair showing REVISE: halt -- do not advance to REVISION GATE or Step 8
  until all per-pair gates show PROCEED.

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
  All TIER 1 pairs PROCEED: YES / NO -> PASS / FAIL

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
  Bodies with >= 2 diff dimension prefixes: [N]
  Flat-list (R-01): [N] -> 0 | Same-dimension (R-02): [N] -> 0
  Registry-violating values (R-04--R-07): [N] -> 0
  Coverage: [N]% (>= 60%) -> PASS / FAIL  |  Overall: PASS / FAIL
```

---

## STEP 9 -- POST-GENERATION PHASE CONFIRMATION

```
PHASE CONFIRMATION:
  Ph1: [gen]/[tgt] -> MATCH/MISMATCH
  Ph2: [gen]/[tgt] -> MATCH/MISMATCH
  Ph3: [gen]/[tgt] -> MATCH/MISMATCH
  Total: [gen]/[tgt] -> MATCH/MISMATCH
```

---

## STEP 10 -- GAP ANALYSIS TABLE

| # | Gap type | Specific artifact | Classification | Incumbent status | Phase first surfaces |
|---|----------|------------------|----------------|-----------------|---------------------|

Classification: PARITY | NET-NEW. Minimum: 1 Doc, 1 Design, 1 Operational row.

---

## STEP 11 -- THRESHOLD CONFIRMATION

```
THRESHOLD CONFIRMATION:
  C-14: [N]/[N] = [N]% (>= 60%) -> PASS / FAIL
  C-16: [N]/[N] = [N]% (>= 60%) -> PASS / FAIL
  C-12: [N]/[N] = [N]% (>= 60%) -> PASS / FAIL
  C-33 cand.: Phase narrative block present (Step 1b): YES / NO
              Trigger events named for all 3 phases: YES / NO
              Phase distribution rationale in Step 4: YES / NO
              VALIDATION TRACE phase-narrative rows all PASS: YES / NO  -> PASS / FAIL
  Overall: PASS (all four) / FAIL (one or more)
```
```

---

## V-04: Combined -- INERTIA COMPETITOR Preamble + SRE-First Ordering (V-01 + V-02)

**Axis:** Both V-01 and V-02 axes active simultaneously. The INERTIA COMPETITOR preamble
anchors the competitor name before all analysis; the SRE-first ordering in Step 2, 3, and
5 ensures operational failure modes set the severity ceiling before lower-stakes personas
are analyzed. The two mechanisms are independent: the preamble is a positional constant;
the ordering is a sequence constraint inside three specific steps. Neither mechanism shares
state with the other; removing either leaves the other intact.
**Hypothesis:** V-01 alone ensures name propagation; V-02 alone ensures severity ceiling
seeding. Combined, they close both the label-drift risk (generic competitor references)
and the severity-floor risk (SRE scenarios deprioritized by ordering effects). V-04 is the
minimum sufficient synthesis for C-31 and C-32 simultaneously.

---

```
# listen-support: Predict First-90-Day Support Tickets

Work through each step in order. Do not skip steps. Do not combine steps.

---

INERTIA COMPETITOR: [name the specific product the target personas currently use for
this workflow -- one product name, grep-checkable, no generic labels]

This name is a constant. Use it exactly -- no synonyms, no generic substitutions -- in
every step that references the prior tool.

---

## STEP 1 -- PHASE-SEVERITY GRADIENT PRIOR

Phase 1 (Day 0-30): P2/P3. Workarounds exist; no committed production data. P0 reserved
for activation blockers affecting all users simultaneously.

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

## STEP 2 -- STATUS QUO ANCHOR

SRE row is listed first. SRE failure modes determine the severity ceiling. Complete
the SRE row with the same depth as all other rows. Column 2: use the INERTIA COMPETITOR
name from the preamble, not a generic label.

| Persona class | Prior tool / STATUS QUO behavior | Key capability they expect to carry over | Most likely violated assumption |
|---------------|----------------------------------|------------------------------------------|----------------------------------|
| SRE | | | |
| Support | | | |
| PM / UX | | | |
| C-01..C-04 (technical early adopters) | | | |
| C-05..C-08 (pragmatic mainstream) | | | |
| C-09..C-12 (enterprise/compliance) | | | |

Column 4 (violated assumption) feeds Step 3.

---

## STEP 3 -- ASSUMPTION AUDIT

**Complete the SRE row first.** SRE tickets determine the severity ceiling; all
subsequent persona rows build on the operational precedent SRE establishes. Use the
INERTIA COMPETITOR name -- not a generic label -- in the "Incumbent behavior" column.

| # | Persona class | Incumbent behavior that created assumption | Imported expectation | What this feature does instead | Resulting failure mode | Ticket # |
|---|---------------|------------------------------------------|---------------------|-------------------------------|----------------------|----------|

Ticket #: LEAVE BLANK. Complete at least 1 row.

```
ASSUMPTION AUDIT COMPLETE:
  Rows documented: [N]
  SRE row present: YES / NO
  All 5 non-ID columns populated: YES / NO
  INERTIA COMPETITOR name used (not generic label): YES / NO
  Ticket IDs pending at Step 6b: [N] rows
```

---

## STEP 4 -- PHASE DISTRIBUTION TARGET

```
PHASE DISTRIBUTION TARGET:
  Phase 1 (Day 0-30):  [N] tickets
  Phase 2 (Day 31-60): [N] tickets
  Phase 3 (Day 61-90): [N] tickets
  Total:               [N] tickets
```

Constraints: Phase 1 >= 3. Phase 3 >= 1. Total >= 7.

---

## STEP 5 -- PERSONA VOICE TABLE (DIMENSION REGISTRY)

SRE row is listed first, consistent with Step 2 ordering. Operational register anchors
the vocabulary framework before Support or PM/UX vocabulary is introduced.

| Persona | Operational vocabulary | Frustration register | Framing conventions |
|---------|----------------------|---------------------|---------------------|
| SRE | (>= 2 specific terms) | (>= 2 specific phrases) | (>= 2 structural patterns) |
| Support | (>= 2 specific terms) | (>= 2 specific phrases) | (>= 2 structural patterns) |
| [other personas used] | (>= 2 specific terms) | (>= 2 specific phrases) | (>= 2 structural patterns) |

Prefixes: operational= | frustration= | framing=
Disqualified: role declarations, generic verbs, bare nouns.

---

## STEP 5b -- DIMENSION-LABEL REJECTION REGISTRY

**Per-category minimum commitment (set before writing entries):**
  Category 1 (Format violations) minimum: 2 entries
  Category 2 (Value violations) minimum:  2 entries

Rationale: 2 + 2 = 4 > 3. Per-category floors of 2 make C-21's total floor (>= 3)
provable from per-category counts alone. Commit to >= 2 per category before writing.

REJECTION REGISTRY:

Category 1 -- Format violations:
  R-01: Flat list without dimension prefixes -- dimension classification absent
  R-02: Same dimension prefix used twice -- register diversity not demonstrated
  R-03: Count without naming -- specific marker absent; citation unverifiable

Category 2 -- Value violations:
  R-04: Role declarations used as markers -- role identity, not vocabulary
  R-05: Generic verbs without register specificity -- universal across all personas
  R-06: Same-register synonym pairs -- two words, one register dimension
  R-07: Bare nouns without context-anchoring -- universality defeats specificity

REGISTRY COMPLETENESS CHECK:
  Category 1 entries:        [N]  (required: >= 2)    -> PASS / FAIL
  Category 2 entries:        [N]  (required: >= 2)    -> PASS / FAIL
  Total entries:             [N]  (required: >= 3)    -> PASS / FAIL
  Floor guarantee: Cat 1 min [N] + Cat 2 min [N] = [sum], required > 3 -> PASS / FAIL
  Dual-category coverage:                             -> PASS / FAIL

```
REGISTRY GATE:
  Per-category commitment honored (Cat 1 >= 2, Cat 2 >= 2):  YES / NO -> must be YES
  Floor guarantee sum > 3:                                    PASS / FAIL
  All other conditions met:                                   PASS / FAIL
  Registry applied during Step 7:                             CONFIRMED
```

---

## STEP 6 -- TICKET SUMMARY TABLE AND VALIDATION TRACE

| # | Phase | Title | Category | Persona | Volume | Severity |
|---|-------|-------|----------|---------|--------|----------|

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
  Phase-severity consistent:
    Phase 1 (P2/P3): [list]                                       -> PASS / FAIL
    Phase 2 (P1/P2): [list]                                       -> PASS / FAIL
    Phase 3 (P0/P1): [list]                                       -> PASS / FAIL
  All personas in voice table:            YES / NO                -> PASS / FAIL
  >= 1 ticket linked to audit row:        YES / NO                -> PASS / FAIL
  INERTIA COMPETITOR name propagation:
    Preamble present:                     YES / NO                -> PASS / FAIL
    Name verbatim in bodies: [N]/[N] (>= 50%)                    -> PASS / FAIL
  SRE ordering:
    SRE first in Step 2:                  YES / NO                -> PASS / FAIL
    SRE first in Step 5:                  YES / NO                -> PASS / FAIL
    SRE ticket in table:                  YES / NO                -> PASS / FAIL
  Overall:                                                        -> PASS / FAIL
```

---

## STEP 6b -- FORWARD-LINK

```
FORWARD-LINK GATE:
  Rows total / assigned: [N] / [N]  -> PASS / FAIL
  All Ticket # in table: YES / NO   -> PASS / FAIL
  Overall: PASS / FAIL
```

---

## STEP 7 -- TICKET BODIES WITH DIMENSION-LABELED MARKER CITATIONS

Do not open with a persona declaration. For audit-linked tickets: include comparison
framing using the exact INERTIA COMPETITOR name from the preamble.
Each body: >= 2 markers from DIFFERENT columns. Clear every marker against REJECTION REGISTRY.

Format:
### Ticket [N] [Phase N]: [Title]
**Traces to:** Assumption #[N]
**Body:** [2-5 sentences]
**Voice markers:** operational=[term] | frustration=[phrase]

After writing all bodies:

TIER-SEQUENCING RULE (preamble -- before opening the verification block):
  All TIER 1 per-pair gates must show PROCEED before TIER 2 is evaluated.
  Any pair showing REVISE: halt -- do not advance to REVISION GATE or Step 8
  until all per-pair gates show PROCEED.

```
BIDIRECTIONAL LINKAGE VERIFICATION:

  TIER ARCHITECTURE SELF-CHECK (complete before per-pair content):

  | Landmark | Expected location | Present | Result |
  |----------|-----------------|---------|--------|
  | TIER-SEQUENCING RULE field | Preamble above block | YES / NO | PASS / FAIL |
  | -- TIER 1: Per-Pair Verification -- header | Before per-pair blocks | YES / NO | PASS / FAIL |
  | -- TIER 2: Block-Level Clearance -- header | Before REVISION GATE | YES / NO | PASS / FAIL |

  All three PASS: YES -> proceed | Any FAIL: halt

  Forward direction: [N] of [N] rows assigned                          -> PASS / FAIL
  Backward direction: [N] bodies with "Traces to:"                     -> PASS / FAIL

  -- TIER 1: Per-Pair Verification --
    Assumption #[N] -> Ticket [N]:
      Audit phrase: "[direct quote -- min 5 words]"
      Body evidence: "[direct quote -- min 5 words]"
      Alignment: MATCH / MISMATCH
      Gate: PROCEED | REVISE
  All TIER 1 pairs PROCEED: YES / NO -> PASS / FAIL

  -- TIER 2: Block-Level Clearance --
  REVISION GATE: [mismatched pairs or "none"] | OPEN | CLOSED
  Do not advance to Step 8 with Gate status = CLOSED.

  Overall: PASS / FAIL
```

---

## STEP 8 -- MARKER FORMAT AUDIT

```
MARKER FORMAT AUDIT:
  Bodies with >= 2 diff dimension prefixes: [N]
  Flat-list (R-01): [N] -> 0 | Same-dimension (R-02): [N] -> 0
  Registry-violating (R-04--R-07): [N] -> 0
  Coverage: [N]% (>= 60%) -> PASS / FAIL  |  Overall: PASS / FAIL
```

---

## STEP 9 -- POST-GENERATION PHASE CONFIRMATION

```
PHASE CONFIRMATION:
  Ph1: [gen]/[tgt] | Ph2: [gen]/[tgt] | Ph3: [gen]/[tgt] | Total: [gen]/[tgt]
  All: MATCH / MISMATCH
```

---

## STEP 10 -- GAP ANALYSIS TABLE

| # | Gap type | Specific artifact | Classification | Incumbent status | Phase first surfaces |
|---|----------|------------------|----------------|-----------------|---------------------|

Incumbent status column: use the exact INERTIA COMPETITOR name, not a generic label.
Minimum: 1 Doc, 1 Design, 1 Operational row.

---

## STEP 11 -- THRESHOLD CONFIRMATION

```
THRESHOLD CONFIRMATION:
  C-14: [N]/[N] = [N]% (>= 60%) -> PASS / FAIL
  C-16: [N]/[N] = [N]% (>= 60%) -> PASS / FAIL
  C-12: [N]/[N] = [N]% (>= 60%) -> PASS / FAIL
  C-31 cand.: Preamble present: YES/NO | Bodies w/ name: [N]/[N] [N]%
              (>= 50%) -> PASS/FAIL | Step 10 uses name: YES/NO -> PASS/FAIL
  C-32 cand.: SRE first Step 2: YES/NO | SRE first Step 5: YES/NO
              SRE ticket present: YES/NO -> PASS / FAIL
  Overall: PASS (all five) / FAIL (one or more)
```
```

---

## V-05: Full Synthesis -- INERTIA COMPETITOR Preamble + SRE-First + PHASE NARRATIVE (V-01 + V-02 + V-03)

**Axis:** All three R10 axes active simultaneously. Each mechanism occupies a distinct
structural position: the INERTIA COMPETITOR preamble is pre-Step-1 positional; the SRE
ordering is an intra-step sequence commitment (Steps 2, 3, 5); the PHASE NARRATIVE is an
analytical block (Step 1b) that precedes assumption generation. The three mechanisms are
orthogonal -- removing any one leaves the other two intact and independently verifiable.
**Hypothesis:** V-01 closes label drift; V-02 closes severity-ceiling deprioritization;
V-03 closes behavioral-driver vacuity in phase assignments. V-04 achieves C-31 + C-32
but leaves C-33 unaddressed. V-05 is the only variation satisfying all three simultaneously.
The three mechanisms reinforce without overlapping: the competitor name appears in the
narrative (Step 1b), is anchored by the preamble, is ordered into SRE rows first, and
propagates through all eleven steps.

---

```
# listen-support: Predict First-90-Day Support Tickets

Work through each step in order. Do not skip steps. Do not combine steps.

---

INERTIA COMPETITOR: [name the specific product the target personas currently use for
this workflow -- one product name, grep-checkable, no generic labels]

This name is a constant. Use it exactly in Steps 1b, 2, 3, 7, and 10. No synonyms,
no generic substitutions ("the incumbent", "the prior tool", "legacy system").

---

## STEP 1 -- PHASE-SEVERITY GRADIENT PRIOR

Phase 1 (Day 0-30): P2/P3. Workarounds exist; no committed production data. P0 reserved
for activation blockers affecting all users simultaneously.

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

State the behavioral driver for each phase. Use the INERTIA COMPETITOR name where the
prior tool is referenced. This narrative must be consistent with the severity prior above
and will be referenced in Steps 4 and 6.

**Phase 1 (Day 0-30) -- First contact:**
Users are exploring the feature while keeping [INERTIA COMPETITOR] active as a safety net.
They encounter the feature for the first time, attempt initial setup, and compare each step
against prior behavior in [INERTIA COMPETITOR]. The trigger event for Phase 1 tickets is
the first contact with a feature behavior that differs from [INERTIA COMPETITOR] -- setup
friction, documentation gaps for the first-use path, onboarding friction. Fallback to
[INERTIA COMPETITOR] is available; severity is bounded.

**Phase 2 (Day 31-60) -- Committed trial:**
Users have migrated real workflows out of [INERTIA COMPETITOR]. Some workflows are on the
new feature; others still run in [INERTIA COMPETITOR]. The trigger event for Phase 2 tickets
is the first time a committed workflow hits a blocking gap: a config combination that works
in [INERTIA COMPETITOR] but fails here, an integration boundary assumed compatible, an edge
case that didn't surface during Phase 1 exploration. Switching cost has accumulated; the
user cannot simply revert.

**Phase 3 (Day 61-90) -- Operational dependency:**
Users are running production traffic. [INERTIA COMPETITOR] is no longer available for this
workflow. The trigger event for Phase 3 tickets is a blocking failure under operational
conditions -- a failure mode that doesn't surface in non-production use. Each ticket
represents a production blocker; no fallback available; severity escalates to P0/P1.

```
PHASE NARRATIVE COMPLETE:
  Phase 1 behavioral driver named:             YES / NO
  Phase 2 behavioral driver named:             YES / NO
  Phase 3 behavioral driver named:             YES / NO
  Trigger events named for all three phases:   YES / NO
  INERTIA COMPETITOR name used in narrative:   YES / NO
```

---

## STEP 2 -- STATUS QUO ANCHOR

SRE row is listed first. SRE failure modes determine the severity ceiling; complete
the SRE row with the same depth as all other rows. Column 2: use the exact INERTIA
COMPETITOR name from the preamble.

| Persona class | Prior tool / STATUS QUO behavior | Key capability they expect to carry over | Most likely violated assumption |
|---------------|----------------------------------|------------------------------------------|----------------------------------|
| SRE | | | |
| Support | | | |
| PM / UX | | | |
| C-01..C-04 (technical early adopters) | | | |
| C-05..C-08 (pragmatic mainstream) | | | |
| C-09..C-12 (enterprise/compliance) | | | |

Column 4 (violated assumption) feeds Step 3.

---

## STEP 3 -- ASSUMPTION AUDIT

**Complete the SRE row first.** SRE tickets determine the severity ceiling; all
subsequent persona rows build on the operational precedent SRE establishes.

Use the exact INERTIA COMPETITOR name in the "Incumbent behavior" column -- not
"the incumbent" or "the prior tool". When assigning rows to phases, verify consistency
with the Phase Narrative (Step 1b): Phase 1 failures at first contact; Phase 2 after
commitment; Phase 3 under production load.

| # | Persona class | Incumbent behavior that created assumption | Imported expectation | What this feature does instead | Resulting failure mode | Ticket # |
|---|---------------|------------------------------------------|---------------------|-------------------------------|----------------------|----------|

Ticket #: LEAVE BLANK. Complete at least 1 row.

```
ASSUMPTION AUDIT COMPLETE:
  Rows documented: [N]
  SRE row present (and first): YES / NO
  All 5 non-ID columns populated: YES / NO
  INERTIA COMPETITOR name used (not generic): YES / NO
  Phase assignments consistent with Phase Narrative: YES / NO
  Ticket IDs pending at Step 6b: [N] rows
```

---

## STEP 4 -- PHASE DISTRIBUTION TARGET

Set phase counts consistent with the Phase Narrative in Step 1b.

```
PHASE DISTRIBUTION TARGET:
  Phase 1 (Day 0-30):  [N] tickets   -- first-contact volume [explain from narrative]
  Phase 2 (Day 31-60): [N] tickets   -- committed-workflow friction [explain from narrative]
  Phase 3 (Day 61-90): [N] tickets   -- production blockers [explain from narrative]
  Total:               [N] tickets
```

Constraints: Phase 1 >= 3. Phase 3 >= 1. Total >= 7.

Phase count rationale: [one sentence per phase explaining why this count follows from
Step 1b's behavioral drivers -- not just "meets the minimum"]

---

## STEP 5 -- PERSONA VOICE TABLE (DIMENSION REGISTRY)

SRE row is listed first, consistent with Steps 2 and 3 ordering.

| Persona | Operational vocabulary | Frustration register | Framing conventions |
|---------|----------------------|---------------------|---------------------|
| SRE | (>= 2 specific terms) | (>= 2 specific phrases) | (>= 2 structural patterns) |
| Support | (>= 2 specific terms) | (>= 2 specific phrases) | (>= 2 structural patterns) |
| [other personas used] | (>= 2 specific terms) | (>= 2 specific phrases) | (>= 2 structural patterns) |

Prefixes: operational= | frustration= | framing=
Disqualified: role declarations, generic verbs, bare nouns.

---

## STEP 5b -- DIMENSION-LABEL REJECTION REGISTRY

**Per-category minimum commitment (set before writing entries):**
  Category 1 (Format violations) minimum: 2 entries
  Category 2 (Value violations) minimum:  2 entries

Rationale: 2 + 2 = 4 > 3. Per-category floors of 2 make C-21's total floor (>= 3)
provable from per-category counts alone -- neither category needs the other's entries.
A per-category minimum of 1 (1 + 1 = 2 < 3) creates a single-point-of-verification
architecture. Commit to >= 2 per category before writing any entries.

REJECTION REGISTRY:

Category 1 -- Format violations:
  R-01: Flat list without dimension prefixes -- dimension classification absent
  R-02: Same dimension prefix used twice -- register diversity not demonstrated
  R-03: Count without naming -- specific marker absent; citation unverifiable

Category 2 -- Value violations:
  R-04: Role declarations used as markers -- role identity, not vocabulary
  R-05: Generic verbs without register specificity -- universal across all personas
  R-06: Same-register synonym pairs -- two words, one register dimension
  R-07: Bare nouns without context-anchoring -- universality defeats specificity

REGISTRY COMPLETENESS CHECK:
  Category 1 entries:        [N]  (required: >= 2)    -> PASS / FAIL
  Category 2 entries:        [N]  (required: >= 2)    -> PASS / FAIL
  Total entries:             [N]  (required: >= 3)    -> PASS / FAIL
  Floor guarantee: Cat 1 min [N] + Cat 2 min [N] = [sum], required > 3 -> PASS / FAIL
  Dual-category coverage:                             -> PASS / FAIL

```
REGISTRY GATE:
  Per-category commitment honored (Cat 1 >= 2, Cat 2 >= 2):  YES / NO -> must be YES
  Floor guarantee sum > 3:                                    PASS / FAIL -> must be PASS
  All other conditions met:                                   PASS / FAIL
  Registry applied during Step 7:                             CONFIRMED
```

---

## STEP 6 -- TICKET SUMMARY TABLE AND VALIDATION TRACE

| # | Phase | Title | Category | Persona | Volume | Severity |
|---|-------|-------|----------|---------|--------|----------|

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
  Phase-severity consistent:
    Phase 1 (P2/P3): [list]                                       -> PASS / FAIL
    Phase 2 (P1/P2): [list]                                       -> PASS / FAIL
    Phase 3 (P0/P1): [list]                                       -> PASS / FAIL
  All personas in voice table:            YES / NO                -> PASS / FAIL
  >= 1 ticket linked to audit row:        YES / NO                -> PASS / FAIL
  INERTIA COMPETITOR name propagation:
    Preamble present:                     YES / NO                -> PASS / FAIL
    Narrative uses name (Step 1b):        YES / NO                -> PASS / FAIL
    Bodies w/ declared name: [N]/[N] (>= 50%)                    -> PASS / FAIL
    Step 10 incumbent column uses name:   YES / NO                -> PASS / FAIL
  SRE ordering:
    SRE first in Step 2:                  YES / NO                -> PASS / FAIL
    SRE first in Step 5:                  YES / NO                -> PASS / FAIL
    SRE row in assumption audit:          YES / NO                -> PASS / FAIL
    SRE ticket in table:                  YES / NO                -> PASS / FAIL
  Phase-narrative consistency:
    Ph1 tickets reflect first-contact driver (Step 1b):    YES / NO -> PASS/FAIL
    Ph2 tickets reflect committed-workflow driver (Step 1b): YES / NO -> PASS/FAIL
    Ph3 tickets reflect production-blocking driver (Step 1b): YES / NO -> PASS/FAIL
  Overall:                                                        -> PASS / FAIL
```

---

## STEP 6b -- FORWARD-LINK

```
FORWARD-LINK GATE:
  Rows total / assigned: [N] / [N]  -> PASS / FAIL
  All Ticket # in table: YES / NO   -> PASS / FAIL
  Overall: PASS / FAIL
```

---

## STEP 7 -- TICKET BODIES WITH DIMENSION-LABELED MARKER CITATIONS

Do not open with a persona declaration. Start with the issue.

For audit-linked tickets: include comparison framing using the exact INERTIA COMPETITOR
name from the preamble -- not a generic label. Each body must also reflect the
behavioral driver of its assigned phase (from Step 1b).

Each body: >= 2 markers from DIFFERENT columns. Clear every marker against REJECTION REGISTRY.

Format:
### Ticket [N] [Phase N]: [Title]
**Traces to:** Assumption #[N]
**Body:** [2-5 sentences; reflects the phase behavioral driver from Step 1b]
**Voice markers:** operational=[term] | frustration=[phrase]

After writing all bodies:

TIER-SEQUENCING RULE (preamble -- before opening the verification block):
  All TIER 1 per-pair gates must show PROCEED before TIER 2 is evaluated.
  Any pair showing REVISE: halt -- do not advance to REVISION GATE or Step 8
  until all per-pair gates show PROCEED.

```
BIDIRECTIONAL LINKAGE VERIFICATION:

  TIER ARCHITECTURE SELF-CHECK (complete before per-pair content):

  | Landmark | Expected location | Present | Result |
  |----------|-----------------|---------|--------|
  | TIER-SEQUENCING RULE field | Preamble above block | YES / NO | PASS / FAIL |
  | -- TIER 1: Per-Pair Verification -- header | Before per-pair blocks | YES / NO | PASS / FAIL |
  | -- TIER 2: Block-Level Clearance -- header | Before REVISION GATE | YES / NO | PASS / FAIL |

  All three PASS: YES -> proceed | Any FAIL: halt -- add missing landmark

  Forward direction: [N] of [N] rows assigned                           -> PASS / FAIL
  Backward direction: [N] bodies with "Traces to:"                      -> PASS / FAIL

  -- TIER 1: Per-Pair Verification --
    Assumption #[N] -> Ticket [N]:
      Audit phrase: "[direct quote -- min 5 words]"
      Body evidence: "[direct quote -- min 5 words]"
      Alignment: MATCH / MISMATCH
      Gate: PROCEED | REVISE
    [repeat for each pair]
  All TIER 1 pairs PROCEED: YES / NO -> PASS / FAIL

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
  Bodies with >= 2 diff dimension prefixes: [N]
  Flat-list (R-01): [N] -> 0 | Same-dimension (R-02): [N] -> 0
  Registry-violating (R-04--R-07): [N] -> 0
  Coverage: [N]% (>= 60%) -> PASS / FAIL  |  Overall: PASS / FAIL
```

---

## STEP 9 -- POST-GENERATION PHASE CONFIRMATION

```
PHASE CONFIRMATION:
  Ph1: [gen]/[tgt] -> MATCH/MISMATCH
  Ph2: [gen]/[tgt] -> MATCH/MISMATCH
  Ph3: [gen]/[tgt] -> MATCH/MISMATCH
  Total: [gen]/[tgt] -> MATCH/MISMATCH
```

---

## STEP 10 -- GAP ANALYSIS TABLE

| # | Gap type | Specific artifact | Classification | Incumbent status | Phase first surfaces |
|---|----------|------------------|----------------|-----------------|---------------------|

Incumbent status column: use the exact INERTIA COMPETITOR name, not a generic label.
Classification: PARITY | NET-NEW. Minimum: 1 Doc, 1 Design, 1 Operational row.

---

## STEP 11 -- THRESHOLD CONFIRMATION

```
THRESHOLD CONFIRMATION:

C-14 | Gap Classification Coverage
  Total gap entries: [N] | Classified: [N] | [N]% (>= 60%) -> PASS / FAIL

C-16 | Voice Marker Citation Coverage
  Total bodies: [N] | With citation: [N] | [N]% (>= 60%)  -> PASS / FAIL

C-12 | Voice Register Density
  Total bodies: [N] | With >= 2 diff dims: [N] | [N]% (>= 60%) -> PASS / FAIL

C-31 cand. | INERTIA COMPETITOR Name Propagation
  Preamble declared before Step 1:          YES / NO  -> PASS / FAIL
  Narrative (Step 1b) uses name:            YES / NO  -> PASS / FAIL
  Bodies w/ name verbatim: [N]/[N] [N]% (>= 50%)     -> PASS / FAIL
  Step 10 incumbent column uses name:       YES / NO  -> PASS / FAIL

C-32 cand. | SRE-First Ordering
  SRE first row in Step 2 table:            YES / NO  -> PASS / FAIL
  SRE first row in Step 5 table:            YES / NO  -> PASS / FAIL
  SRE row in assumption audit (Step 3):     YES / NO  -> PASS / FAIL
  SRE ticket in Step 6 table:               YES / NO  -> PASS / FAIL

C-33 cand. | Phase Narrative Behavioral Driver
  Phase narrative block present (Step 1b):  YES / NO  -> PASS / FAIL
  Trigger events named all 3 phases:        YES / NO  -> PASS / FAIL
  Phase count rationale in Step 4:          YES / NO  -> PASS / FAIL
  VALIDATION TRACE Phase-narrative rows all PASS: YES / NO -> PASS / FAIL

Summary:
  C-14:       PASS / FAIL
  C-16:       PASS / FAIL
  C-12:       PASS / FAIL
  C-31 cand.: PASS / FAIL
  C-32 cand.: PASS / FAIL
  C-33 cand.: PASS / FAIL
  Overall: PASS (all six) / FAIL (one or more)
```

If any threshold shows FAIL, identify the specific entries or bodies causing the
shortfall, revise, and re-run this block before submitting.
```

---

## Variation Comparison Summary

| Axis | V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|------|
| INERTIA COMPETITOR preamble before Step 1 | YES | no | no | YES | YES |
| SRE first in Step 2 and Step 5 tables | no | YES | no | YES | YES |
| PHASE NARRATIVE block (Step 1b) | no | no | YES | no | YES |
| TIER-SEQUENCING RULE as preamble (R9 V-01 baseline) | YES | YES | YES | YES | YES |
| Per-category minimum commitment with rationale (R9 V-02 baseline) | YES | YES | YES | YES | YES |
| TIER ARCHITECTURE SELF-CHECK as table (R9 V-03 baseline) | YES | YES | YES | YES | YES |
| SRE ordering instruction in Step 3 ASSUMPTION AUDIT | no | YES | no | YES | YES |
| Competitor name check in VALIDATION TRACE | YES | no | no | YES | YES |
| Phase-narrative consistency check in VALIDATION TRACE | no | no | YES | no | YES |
| C-31 THRESHOLD check (name propagation) | YES | no | no | YES | YES |
| C-32 THRESHOLD check (SRE ordering) | no | YES | no | YES | YES |
| C-33 THRESHOLD check (phase narrative) | no | no | YES | no | YES |

**C-31 candidate mechanism per variation:**
- V-01: Preamble before Step 1 + propagation check in VALIDATION TRACE + Step 10 instruction
- V-02: Not present
- V-03: Not present
- V-04: Same as V-01
- V-05: Same as V-01, plus name required in Phase Narrative (Step 1b) -- additional surface

**C-32 candidate mechanism per variation:**
- V-01: Not present
- V-02: SRE first in Step 2 + Step 3 sequencing directive + SRE first in Step 5 + VALIDATION TRACE rows
- V-03: Not present
- V-04: Same as V-02
- V-05: Same as V-02 (consistent ordering across Step 2, 3, 4, 5)

**C-33 candidate mechanism per variation:**
- V-01: Not present
- V-02: Not present
- V-03: PHASE NARRATIVE block (Step 1b) + Step 4 rationale requirement + VALIDATION TRACE rows
- V-04: Not present
- V-05: Same as V-03, plus competitor name required in narrative (cross-axis reinforcement)

**Predicted strongest:** V-05 -- all three mechanisms active simultaneously, orthogonal.
V-04 is the minimum sufficient synthesis for C-31 + C-32 if the phase narrative (V-03)
proves orthogonal to both (neither axis shares state with the narrative). V-05 adds the
one interaction that V-04 cannot test: whether naming the INERTIA COMPETITOR inside the
Phase Narrative (before the STATUS QUO anchor) further reduces generic-label substitution
in Phase 2 and Phase 3 ticket bodies.
