# listen-support Round 3 -- Skill Body Prompt Variations

**Date:** 2026-03-15
**Rubric target:** v3 (16 criteria -- C-01 through C-16; C-14/C-15/C-16 added as aspirational)
**Base:** V-05 R2 (C-01 through C-13 at ceiling; C-14/C-15/C-16 unscored -- targets for this round)

**Variation axes selected** (3 single-axis, then 2 combined):
1. **Gap classification table format** -- gap analysis section restructured as a table with a dedicated PARITY/NET-NEW classification column, replacing inline text tags; makes per-entry coverage mechanically auditable (V-01)
2. **Violated-assumption audit step** -- named analytical step between inertia map and ticket generation; produces a structured chain: incumbent behavior -> user expectation -> feature behavior -> failure mode -> ticket; makes the C-15 reasoning mechanism visible and reproducible (V-02)
3. **Column-attributed marker citation** -- extends the "Markers deployed: X / Y" format to "operational=X | frustration=Y | framing=Z"; attributes each cited marker to its voice-table column; makes cross-dimension density auditable by inspection (V-03)
4. **V-01 + V-02 combined** -- gap classification table + violated-assumption audit step (V-04)
5. **Full synthesis** -- all three R3 axes + full R2 baseline (phase-severity prior, phase distribution, voice table, validation trace, post-generation confirmation) (V-05)

**Axes carried from R2 (still active in all variations):**
- Persona voice table with operational/frustration/framing columns (V-03/R2)
- Inertia map with violated-assumption column (V-02/R2)
- Inline validation trace before bodies (V-05/R2)
- Phase-severity semantic binding with explicit prior (V-05/R2)
- Phase distribution target with post-generation confirmation (V-05/R2)
- Marker citation after each body (V-03/R2)
- PARITY/NET-NEW gap annotation (V-02/R2 -- promoted to table column in V-01/R3)

**New axes introduced this round:**
- Gap classification table format (V-01, V-04, V-05) -- direct C-14 mechanism
- Violated-assumption audit step (V-02, V-04, V-05) -- direct C-15 mechanism
- Column-attributed marker citation (V-03, V-05) -- direct C-16 mechanism

**R3 criterion hypothesis matrix:**

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 through C-13 (all prior -- 100 pt ceiling) | YES | YES | YES | YES | YES |
| C-14: Competitive Gap Classification (table column) | YES | -- | -- | YES | YES |
| C-15: Violated-Assumption Anchor (named step) | -- | YES | -- | YES | YES |
| C-16: Voice Marker Citation (column-attributed) | -- | -- | YES | -- | YES |

---

## V-01: Single-Axis -- Gap Classification Table Format

**Axis:** Output format -- the gap analysis section is restructured from prose entries with
inline PARITY/NET-NEW text tags to a unified table with a dedicated Classification column.
All other R2 V-05 mechanisms are preserved unchanged.

**Probe (C-14 targeting):** C-14 requires at least 60% of gap entries to carry an explicit
per-entry parity/net-new classification. Inline text tags in prose sections are the highest-risk
format for this criterion: the model populates the artifact field (satisfying C-08) and may
write the tag for the first one or two entries but omit it for later entries without noticing.
A table column cannot be partially populated -- a missing cell is visible as a blank. The
Classification column also surfaces the aggregate split at a glance (count PARITY rows vs.
NET-NEW rows), making the strategic framing that C-14 rewards legible to a PM scanning the
output.

**Hypothesis:** A dedicated Classification column produces 100% per-entry coverage rather
than the 60-80% range that inline tags achieve. The table format also adds a "Incumbent
status" column that provides the competitive context that gives PARITY/NET-NEW labels meaning
("Incumbent has /health endpoint; this feature does not" is more actionable than "PARITY").

---

```
# listen-support: Predict First-90-Day Support Tickets

Work through each step in order. Do not skip steps. Do not combine steps.

---

## STEP 1 -- PHASE-SEVERITY GRADIENT PRIOR

Before declaring targets or generating tickets, state the principled severity prior for
each phase. Use this to calibrate severity assignments in Step 4.

Phase 1 (Day 0-30): first-impressions and setup friction. Users have not yet invested
deeply. Typical severity P2/P3. P0 requires a hard activation blocker affecting all users
simultaneously -- rare because the feature has not yet reached production load.

Phase 2 (Day 31-60): adoption edge cases. Users succeeded at the happy path and are
committing real data and workflows. Severity rises to P1/P2. A workflow broken after
investment is harder to accept with a workaround.

Phase 3 (Day 61-90): operational steady-state. Systems run at scale, integrations are live.
P0 tickets appear because partial failures under load have real business impact and missing
operational tooling turns a recoverable incident into an extended outage.

State your prior:

```
PHASE-SEVERITY PRIOR:
  Phase 1 (Day 0-30):  typical P2/P3; P0 only for activation blockers affecting all users
  Phase 2 (Day 31-60): typical P1/P2; P0 exceptional (data loss or workflow corruption)
  Phase 3 (Day 61-90): typical P0/P1; P3 rare (users have exhausted workarounds)
```

---

## STEP 2 -- STATUS QUO ANCHOR

Every support ticket in the first 90 days is a transition story. Name where each persona
class came from before generating any tickets.

| Persona class | Prior tool / STATUS QUO behavior | Key capability they expect to carry over | Most likely violated assumption |
|---------------|----------------------------------|------------------------------------------|----------------------------------|
| Support | | | |
| SRE | | | |
| PM / UX | | | |
| C-01..C-04 (technical early adopters) | | | |
| C-05..C-08 (pragmatic mainstream) | | | |
| C-09..C-12 (enterprise/compliance) | | | |

This is your inertia map. Reference column 4 when writing ticket bodies -- at least one
ticket must surface a violated assumption that a happy-path spec review would miss.

---

## STEP 3 -- PHASE DISTRIBUTION TARGET

Declare the binding ticket count per phase before generating any tickets.

```
PHASE DISTRIBUTION TARGET:
  Phase 1 (Day 0-30):  [N] tickets   -- setup friction, first-impression errors
  Phase 2 (Day 31-60): [N] tickets   -- adoption edge cases, workflow friction
  Phase 3 (Day 61-90): [N] tickets   -- operational steady-state, integration issues
  Total:               [N] tickets
```

Constraints: Phase 1 >= 3. Phase 3 >= 1. Total >= 7. All three phases non-zero.

---

## STEP 4 -- PERSONA VOICE TABLE

Generate the vocabulary table before writing any ticket bodies. Populate with specific
words and phrases -- not general categories. Each body in Step 6 must deploy at least
2 markers from different columns for the assigned persona.

| Persona | Operational vocabulary | Frustration register | Framing conventions |
|---------|----------------------|---------------------|---------------------|
| Support | (>= 2 specific terms) | (>= 2 specific phrases) | (>= 2 structural patterns) |
| SRE | (>= 2 specific terms) | (>= 2 specific phrases) | (>= 2 structural patterns) |
| [other personas used] | (>= 2 specific terms) | (>= 2 specific phrases) | (>= 2 structural patterns) |

Column definitions:
- Operational vocabulary: domain-specific nouns and verbs this persona uses professionally
  (examples: escalation queue, runbook entry, SLO budget, change board ticket, config schema)
- Frustration register: first-person incident-voice phrases used when blocked
  (examples: "I've closed 8 of these today", "paged at 02:14 with a blank runbook page")
- Framing conventions: structural or rhetorical patterns this persona uses
  (examples: numbered repro steps / SRE incident timeline / PM user-research citations with counts)

Anti-pattern: Do not populate cells with role labels ("uses technical terms"). The table
must contain actual words and phrases that will appear in body text.

Only include personas that will appear in the ticket set. Minimum 2 distinct personas.

---

## STEP 5 -- TICKET SUMMARY TABLE

Generate the ticket table with a Phase column. Follow the phase distribution target from
Step 3 and assign severity consistent with the phase-severity prior from Step 1.

| # | Phase | Title | Category | Persona | Volume | Severity |
|---|-------|-------|----------|---------|--------|----------|

Allowed values -- no other values are valid:
- Phase: Phase 1 | Phase 2 | Phase 3
- Category: how-to | bug | feature-request | config | integration
- Persona: Support | SRE | PM | UX | C-01 through C-12
- Volume: high | medium | low
- Severity: P0 | P1 | P2 | P3

After completing the table, run the full validation trace before writing any bodies:

```
VALIDATION TRACE:
  Distinct categories:                [N] (required: >= 3)             -> PASS / FAIL
  Distinct personas:                  [N] (required: >= 2)             -> PASS / FAIL
  P0 count:                           [N] (required: <= 1)             -> PASS / FAIL
  Low/medium volume entries:          [N] (required: >= 1)             -> PASS / FAIL
  Total rows:                         [N] (required: >= 7)             -> PASS / FAIL
  Phase 1 rows:                       [N] (target: [N from Step 3])   -> MATCH / MISMATCH
  Phase 2 rows:                       [N] (target: [N from Step 3])   -> MATCH / MISMATCH
  Phase 3 rows:                       [N] (target: [N from Step 3])   -> MATCH / MISMATCH
  All personas in voice table:        YES / NO                        -> PASS / FAIL
  >= 1 ticket from violated assumption (inertia map col 4): YES / NO  -> PASS / FAIL
  Phase-severity consistent with prior:
    Phase 1 severities (P2/P3 expected): [list actual values]         -> PASS / FAIL
    Phase 2 severities (P1/P2 expected): [list actual values]         -> PASS / FAIL
    Phase 3 severities (P0/P1 expected): [list actual values]         -> PASS / FAIL
  Overall:                                                             -> PASS / FAIL
```

Do not write any ticket body until VALIDATION TRACE shows Overall: PASS.

---

## STEP 6 -- TICKET BODIES

For each table row, write the ticket body. Write the way that person actually types.
Do not open any body with a persona declaration. Start with the issue.

Each body must:
1. Deploy at least 2 markers from different columns of the persona's voice table row
2. Not open with a persona declaration
3. Remain consistent with the phase and severity in the table

After each body, cite which markers you deployed:

### Ticket [N] [Phase N]: [Title from table]
**Body:** [2-5 sentences in the persona's actual voice]
**Markers deployed:** [marker 1 (column name)] / [marker 2 (column name)]

---

## STEP 7 -- POST-GENERATION PHASE CONFIRMATION

After writing all bodies, confirm phase distribution:

```
PHASE CONFIRMATION:
  Phase 1 bodies generated: [N]   Target: [N]   -> MATCH / MISMATCH
  Phase 2 bodies generated: [N]   Target: [N]   -> MATCH / MISMATCH
  Phase 3 bodies generated: [N]   Target: [N]   -> MATCH / MISMATCH
  Total bodies:             [N]   Target: [N]   -> MATCH / MISMATCH
```

If any phase shows MISMATCH, revise before proceeding to Step 8.

---

## STEP 8 -- GAP ANALYSIS TABLE

Derive gaps from the ticket set. Present the gap analysis as a structured table rather
than prose sections. Every row must have a non-empty Classification cell -- no cell
may be left blank or marked "TBD".

| # | Gap type | Specific artifact to create or change | Classification | Incumbent status | Phase first surfaces |
|---|----------|--------------------------------------|----------------|-----------------|---------------------|

Column definitions:
- Gap type: Doc | Design | Operational
- Specific artifact: name the exact doc section, config field, API endpoint, runbook page, or UI element
- Classification: PARITY (incumbent already provides this; closing it is table stakes) or NET-NEW (no incumbent equivalent; this is differentiation or a unique expectation from the feature promise)
- Incumbent status: what the incumbent or prior tool offers in this area (or "no incumbent equivalent" for NET-NEW)
- Phase first surfaces: Phase 1 | Phase 2 | Phase 3

Minimum: 1 Doc row, 1 Design row, 1 Operational row.

After completing the table, confirm:

```
GAP CLASSIFICATION COVERAGE:
  Total gap entries:          [N]
  Entries with Classification: [N]
  Coverage:                   [N]% (required: >= 60%)  -> PASS / FAIL
  PARITY entries:             [N]
  NET-NEW entries:            [N]
```
```

---

## V-02: Single-Axis -- Violated-Assumption Audit Step

**Axis:** Lifecycle emphasis -- a new named analytical step (ASSUMPTION AUDIT) is inserted
between the inertia map and ticket generation. The audit step produces a structured chain
for each violated assumption: incumbent behavior that created the expectation -> user's
imported assumption -> what the feature does instead -> the failure mode that results ->
which ticket in the set traces to this chain. This makes the violated-assumption reasoning
visible as a reproducible analytical output.

**Probe (C-15 targeting):** C-15 scores whether the violated-assumption framing is present
as a named analytical step, not whether a non-obvious ticket incidentally appears in the
output (that is C-09's job). R2 V-02 introduced the inertia map with a "most likely
violated assumption" column -- this satisfies C-09 reliably (the assumption is named)
but does not fully satisfy C-15 (the mechanism is a table cell, not a named analytical
step with an explicit chain). The ASSUMPTION AUDIT step closes this gap: it requires the
model to reason through the full chain from incumbent behavior to failure mode before
generating any ticket, and to name which ticket in the set captures the failure mode.

**Hypothesis:** When the violated-assumption chain is required to be explicit and
forward-linked to a specific ticket, the model cannot satisfy C-15 by gesture -- it must
complete the reasoning before writing the ticket. The forward link (AUDIT row -> ticket ID)
also creates a verifiable trace: a rubric scorer can confirm that the ticket named in the
AUDIT row exists and surfaces the non-obvious failure mode, independently of reading the
full ticket body.

---

```
# listen-support: Predict First-90-Day Support Tickets

Work through each step in order. Do not skip steps. Do not combine steps.

---

## STEP 1 -- STATUS QUO ANCHOR

Every support ticket in the first 90 days is a transition story. Name where each persona
class came from before generating any tickets.

| Persona class | Prior tool / STATUS QUO behavior | Key capability they expect to carry over | Most likely violated assumption |
|---------------|----------------------------------|------------------------------------------|----------------------------------|
| Support | | | |
| SRE | | | |
| PM / UX | | | |
| C-01..C-04 (technical early adopters) | | | |
| C-05..C-08 (pragmatic mainstream) | | | |
| C-09..C-12 (enterprise/compliance) | | | |

---

## STEP 2 -- ASSUMPTION AUDIT

For each violated assumption in column 4 of the inertia map, complete the full
assumption chain. This is a named analytical step -- not a summary or a restatement
of the inertia map. It produces the structural reasoning that will drive non-obvious
ticket generation in Step 5.

| # | Persona class | Incumbent behavior that created assumption | User's imported expectation | What this feature does instead | Resulting failure mode | Ticket ID (to be assigned in Step 5) |
|---|---------------|-------------------------------------------|---------------------------|-------------------------------|----------------------|--------------------------------------|

Column definitions:
- Incumbent behavior: the specific thing the prior tool did that taught users to expect X
- User's imported expectation: the exact assumption carried over ("I expect Y because in [prior tool] it always worked this way")
- What this feature does instead: the specific behavior that violates the expectation
- Resulting failure mode: what the user experiences -- the concrete symptom, not the root cause
- Ticket ID: leave blank for now; fill in after Step 5 with the ticket that captures this chain

Complete at least 1 row. The resulting failure mode in each row must be non-obvious
from reading the feature spec's happy path -- it must require knowing the prior tool's
behavior to predict.

After completing the audit, state:

```
ASSUMPTION AUDIT COMPLETE:
  Violated assumptions documented: [N]
  Each row has: incumbent behavior, imported expectation, feature behavior, failure mode: YES / NO
  Ticket IDs to be assigned in Step 5: [N] rows pending
```

---

## STEP 3 -- PHASE-SEVERITY GRADIENT PRIOR

Before declaring targets or generating tickets, state the principled severity prior.

Phase 1 (Day 0-30): first-impressions and setup friction. Typical P2/P3. P0 only for
activation blockers affecting all users simultaneously.

Phase 2 (Day 31-60): adoption edge cases after happy-path success. Typical P1/P2.
P0 exceptional (data loss or workflow corruption under real load).

Phase 3 (Day 61-90): operational steady-state at scale. Typical P0/P1. P3 rare because
users at this stage have exhausted easy workarounds.

```
PHASE-SEVERITY PRIOR:
  Phase 1 (Day 0-30):  typical P2/P3; P0 only for activation blockers affecting all users
  Phase 2 (Day 31-60): typical P1/P2; P0 exceptional (data loss or workflow corruption)
  Phase 3 (Day 61-90): typical P0/P1; P3 rare (users have exhausted workarounds)
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

Constraints: Phase 1 >= 3. Phase 3 >= 1. Total >= 7. All three phases non-zero.

---

## STEP 5 -- PERSONA VOICE TABLE

Build the vocabulary table before writing any bodies. Populate with specific words and
phrases -- not categories. Each body in Step 7 must deploy at least 2 markers from
different columns.

| Persona | Operational vocabulary | Frustration register | Framing conventions |
|---------|----------------------|---------------------|---------------------|
| Support | (>= 2 specific terms) | (>= 2 specific phrases) | (>= 2 structural patterns) |
| SRE | (>= 2 specific terms) | (>= 2 specific phrases) | (>= 2 structural patterns) |
| [other personas used] | (>= 2 specific terms) | (>= 2 specific phrases) | (>= 2 structural patterns) |

Anti-pattern: Do not populate cells with role labels. The table must contain actual words
and phrases that will appear in body text. Minimum 2 distinct personas.

---

## STEP 6 -- TICKET SUMMARY TABLE

Generate the ticket table. Include a Phase column. For tickets that trace to an assumption
audit row, note the audit row number in the title or a Trace column.

| # | Phase | Title | Category | Persona | Volume | Severity |
|---|-------|-------|----------|---------|--------|----------|

Allowed values:
- Phase: Phase 1 | Phase 2 | Phase 3
- Category: how-to | bug | feature-request | config | integration
- Persona: Support | SRE | PM | UX | C-01 through C-12
- Volume: high | medium | low
- Severity: P0 | P1 | P2 | P3

After completing the table, update Step 2's ASSUMPTION AUDIT with the assigned Ticket IDs.
Then run the full validation trace:

```
VALIDATION TRACE:
  Distinct categories:                [N] (required: >= 3)             -> PASS / FAIL
  Distinct personas:                  [N] (required: >= 2)             -> PASS / FAIL
  P0 count:                           [N] (required: <= 1)             -> PASS / FAIL
  Low/medium volume entries:          [N] (required: >= 1)             -> PASS / FAIL
  Total rows:                         [N] (required: >= 7)             -> PASS / FAIL
  Phase 1 rows:                       [N] (target: [N from Step 4])   -> MATCH / MISMATCH
  Phase 2 rows:                       [N] (target: [N from Step 4])   -> MATCH / MISMATCH
  Phase 3 rows:                       [N] (target: [N from Step 4])   -> MATCH / MISMATCH
  All personas in voice table:        YES / NO                        -> PASS / FAIL
  Assumption audit rows linked to tickets: [N] of [N] rows assigned   -> PASS / FAIL
  Phase-severity consistent with prior:
    Phase 1 severities (P2/P3 expected): [list actual values]         -> PASS / FAIL
    Phase 2 severities (P1/P2 expected): [list actual values]         -> PASS / FAIL
    Phase 3 severities (P0/P1 expected): [list actual values]         -> PASS / FAIL
  Overall:                                                             -> PASS / FAIL
```

Do not write any body until VALIDATION TRACE shows Overall: PASS.

---

## STEP 7 -- TICKET BODIES

For each table row, write the ticket body. Write the way that person actually types.
Do not open any body with a persona declaration. Start with the issue.

For tickets linked to an assumption audit row: the body must contain the comparison
framing from that row -- what the user expected (based on the incumbent behavior)
and what they found instead. This is the voice signature of an assumption-violation ticket.

For tickets not linked to an assumption audit row: write in pure persona voice without
forced comparison framing.

Each body must deploy at least 2 markers from different columns of the persona's voice
table row. After each body, cite the deployed markers:

### Ticket [N] [Phase N]: [Title from table]
**Assumption trace:** [audit row N, or "net-new friction"]
**Body:** [2-5 sentences in the persona's actual voice]
**Markers deployed:** [marker 1 (column name)] / [marker 2 (column name)]

---

## STEP 8 -- POST-GENERATION PHASE CONFIRMATION

```
PHASE CONFIRMATION:
  Phase 1 bodies generated: [N]   Target: [N]   -> MATCH / MISMATCH
  Phase 2 bodies generated: [N]   Target: [N]   -> MATCH / MISMATCH
  Phase 3 bodies generated: [N]   Target: [N]   -> MATCH / MISMATCH
  Total bodies:             [N]   Target: [N]   -> MATCH / MISMATCH
```

---

## STEP 9 -- GAP ANALYSIS

Three required sections. Each entry names a specific artifact. Tag each entry as
PARITY (incumbent has this) or NET-NEW (no incumbent equivalent).

### Documentation Gaps
[Each entry names a specific doc, section, or reference article.
Tag: PARITY / NET-NEW]

### Design Gaps
[Each entry names a specific UI element, config field, API behavior, or workflow step.
Tag: PARITY / NET-NEW]

### Operational Gaps
[Each entry names a specific runbook page, monitoring endpoint, alert rule, or
deployment checklist item. Tag: PARITY / NET-NEW]

Minimum: 1 entry per section. At least 60% of all entries must carry a classification tag.
```

---

## V-03: Single-Axis -- Column-Attributed Marker Citation

**Axis:** Output format -- the marker citation after each ticket body is extended from
"Markers deployed: X / Y" to "operational=[term] | frustration=[phrase] | framing=[convention]".
Each cited marker is explicitly attributed to its voice-table column. All other R2 V-05
mechanisms are preserved.

**Probe (C-16 targeting):** C-16 requires that per-body citations NAME the specific markers
deployed (not just count them) and make voice density auditable by inspection. R2 V-03's
"Markers deployed: [marker 1 (column name)] / [marker 2 (column name)]" format already
satisfies the naming requirement, but the "(column name)" attribution is appended in
parentheses and can be omitted without the format breaking syntactically.

Column-attributed format makes the attribution structural: the label "operational=" is the
column name, the value after "=" is the marker. A reviewer scanning for C-16 compliance can
check that each body has "operational=", "frustration=", and/or "framing=" prefix labels.
The format also closes a subtle gap in C-12 verification: C-12 requires markers from
DIFFERENT register dimensions. With "Markers: runbook / incident timeline", a reviewer
must know that "runbook" is operational and "incident timeline" is framing. With
"operational=runbook | framing=incident timeline", the cross-dimension claim is explicit
and self-verifying.

**Hypothesis:** Structurally attributed citations prevent single-dimension marker repetition.
A body that deploys "runbook" and "runbook entry" satisfies "2 markers" in the count-based
format but fails C-12's cross-dimension requirement. With column-attributed citations, a
model would have to write "operational=runbook | operational=runbook entry" -- two values
for the same column prefix -- which is visibly wrong and correctable before the output is
accepted. The attribution format makes C-12 failures self-detecting.

---

```
# listen-support: Predict First-90-Day Support Tickets

Work through each step in order. Do not skip steps. Do not combine steps.

---

## STEP 1 -- PHASE-SEVERITY GRADIENT PRIOR

Before declaring targets or generating tickets, state the principled severity prior.

Phase 1 (Day 0-30): first-impressions and setup friction. Typical P2/P3. P0 only for
activation blockers affecting all users simultaneously.

Phase 2 (Day 31-60): adoption edge cases. Typical P1/P2. P0 exceptional.

Phase 3 (Day 61-90): operational steady-state at scale. Typical P0/P1. P3 rare.

```
PHASE-SEVERITY PRIOR:
  Phase 1 (Day 0-30):  typical P2/P3; P0 only for activation blockers affecting all users
  Phase 2 (Day 31-60): typical P1/P2; P0 exceptional (data loss or workflow corruption)
  Phase 3 (Day 61-90): typical P0/P1; P3 rare (users have exhausted workarounds)
```

---

## STEP 2 -- STATUS QUO ANCHOR

Name where each persona class came from before generating any tickets.

| Persona class | Prior tool / STATUS QUO behavior | Key capability they expect to carry over | Most likely violated assumption |
|---------------|----------------------------------|------------------------------------------|----------------------------------|
| Support | | | |
| SRE | | | |
| PM / UX | | | |
| C-01..C-04 (technical early adopters) | | | |
| C-05..C-08 (pragmatic mainstream) | | | |
| C-09..C-12 (enterprise/compliance) | | | |

At least one ticket in Step 6 must surface a violated assumption from column 4.

---

## STEP 3 -- PHASE DISTRIBUTION TARGET

```
PHASE DISTRIBUTION TARGET:
  Phase 1 (Day 0-30):  [N] tickets
  Phase 2 (Day 31-60): [N] tickets
  Phase 3 (Day 61-90): [N] tickets
  Total:               [N] tickets
```

Constraints: Phase 1 >= 3. Phase 3 >= 1. Total >= 7. All three phases non-zero.

---

## STEP 4 -- PERSONA VOICE TABLE

Build the vocabulary table before writing any bodies. Populate with specific words and
phrases -- not categories.

| Persona | Operational vocabulary | Frustration register | Framing conventions |
|---------|----------------------|---------------------|---------------------|
| Support | (>= 2 specific terms) | (>= 2 specific phrases) | (>= 2 structural patterns) |
| SRE | (>= 2 specific terms) | (>= 2 specific phrases) | (>= 2 structural patterns) |
| [other personas used] | (>= 2 specific terms) | (>= 2 specific phrases) | (>= 2 structural patterns) |

Column definitions:
- Operational vocabulary: domain-specific nouns and verbs used professionally
- Frustration register: first-person incident-voice phrases used when blocked
- Framing conventions: structural or rhetorical patterns this persona uses

Anti-pattern: Do not populate cells with role labels. The table must contain actual words
and phrases that will appear in body text. Minimum 2 distinct personas.

Each body in Step 6 must deploy at least 2 markers from DIFFERENT columns. The marker
citation format (Step 6) will show exactly which column each marker came from.

---

## STEP 5 -- TICKET SUMMARY TABLE AND VALIDATION TRACE

Generate the ticket table with a Phase column.

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
  Distinct categories:                [N] (required: >= 3)             -> PASS / FAIL
  Distinct personas:                  [N] (required: >= 2)             -> PASS / FAIL
  P0 count:                           [N] (required: <= 1)             -> PASS / FAIL
  Low/medium volume entries:          [N] (required: >= 1)             -> PASS / FAIL
  Total rows:                         [N] (required: >= 7)             -> PASS / FAIL
  Phase 1 rows:                       [N] (target: [N from Step 3])   -> MATCH / MISMATCH
  Phase 2 rows:                       [N] (target: [N from Step 3])   -> MATCH / MISMATCH
  Phase 3 rows:                       [N] (target: [N from Step 3])   -> MATCH / MISMATCH
  All personas in voice table:        YES / NO                        -> PASS / FAIL
  >= 1 ticket from violated assumption: YES / NO                      -> PASS / FAIL
  Phase-severity consistent with prior:
    Phase 1 severities (P2/P3 expected): [list actual values]         -> PASS / FAIL
    Phase 2 severities (P1/P2 expected): [list actual values]         -> PASS / FAIL
    Phase 3 severities (P0/P1 expected): [list actual values]         -> PASS / FAIL
  Overall:                                                             -> PASS / FAIL
```

Do not write any body until VALIDATION TRACE shows Overall: PASS.

---

## STEP 6 -- TICKET BODIES WITH COLUMN-ATTRIBUTED MARKER CITATIONS

For each table row, write the ticket body. Write the way that person actually types.
Do not open any body with a persona declaration. Start with the issue.

Each body must:
1. Deploy at least 2 markers from DIFFERENT columns of the persona's voice table row
2. Not open with a persona declaration
3. Remain consistent with the phase and severity locked in the table

After each body, cite the markers using column-attributed format:

```
Voice markers: operational=[specific term] | frustration=[specific phrase] | framing=[structural pattern]
```

Every citation must:
- Use the exact column label prefix (operational= / frustration= / framing=)
- Name the specific word or phrase deployed (not a description of it)
- Include at least 2 different column prefixes (operational= | frustration= is 2 columns;
  operational= | operational= is 1 column and fails the cross-dimension requirement)

Format:

### Ticket [N] [Phase N]: [Title from table]
**Body:** [2-5 sentences in the persona's actual voice]
**Voice markers:** operational=[term from voice table] | frustration=[phrase from voice table]
OR: operational=[term] | framing=[pattern]
OR: frustration=[phrase] | framing=[pattern]
(Any 2 different column prefixes satisfies the minimum; 3 columns is aspirational)

Anti-pattern: Do not write "operational=runbook | operational=runbook entry" -- same column
twice fails. Do not write "2 markers deployed" -- count without naming fails C-16.

---

## STEP 7 -- POST-GENERATION PHASE CONFIRMATION

```
PHASE CONFIRMATION:
  Phase 1 bodies generated: [N]   Target: [N]   -> MATCH / MISMATCH
  Phase 2 bodies generated: [N]   Target: [N]   -> MATCH / MISMATCH
  Phase 3 bodies generated: [N]   Target: [N]   -> MATCH / MISMATCH
  Total bodies:             [N]   Target: [N]   -> MATCH / MISMATCH
```

Check that every body has a Voice markers: line with at least 2 different column prefixes:

```
MARKER CITATION AUDIT:
  Bodies with Voice markers citation:   [N] of [N] bodies
  Bodies with 2+ different column prefixes: [N] of [N] bodies
  Coverage:                             [N]% (required: >= 60%)  -> PASS / FAIL
```

---

## STEP 8 -- GAP ANALYSIS

Three required sections. Each entry names a specific artifact. Tag each entry PARITY or NET-NEW.

### Documentation Gaps
[Each entry names a specific doc, section, or reference article. Tag: PARITY / NET-NEW]

### Design Gaps
[Each entry names a specific UI element, config field, API behavior, or workflow step.
Tag: PARITY / NET-NEW]

### Operational Gaps
[Each entry names a specific runbook page, monitoring endpoint, alert rule, or deployment
checklist item. Tag: PARITY / NET-NEW]

Minimum: 1 entry per section. At least 60% of all entries must carry a PARITY or NET-NEW tag.
```

---

## V-04: Combined -- Gap Classification Table + Violated-Assumption Audit (V-01 + V-02)

**Axes combined:** Gap analysis as classification table (V-01, targeting C-14) + explicit
violated-assumption audit step (V-02, targeting C-15).

**Combination hypothesis:** C-14 and C-15 operate in different output zones: C-14 is a
property of the gap section (post-generation); C-15 is a property of the analytical
reasoning step (pre-generation). They do not interact structurally and can be stacked
without tension. The question is whether requiring both creates cognitive sequencing
overhead -- the model must maintain the assumption audit forward-link (Step 2 -> Step 6
ticket IDs) while also producing a well-structured gap classification table at the end.

The combination also tests whether C-15's assumption audit provides forward signal that
improves C-14's classification accuracy. When the model has already reasoned through
"incumbent does X, user expected X, feature does Y, failure mode Z", it has a richer
basis for classifying the corresponding gap as PARITY (the feature lacks what the
incumbent had) vs. NET-NEW (the gap is not an incumbent parity issue but a feature-promise
expectation). The assumed result is that ASSUMPTION AUDIT rows map naturally to PARITY
classifications and net-new friction tickets map to NET-NEW classifications.

---

```
# listen-support: Predict First-90-Day Support Tickets

Work through each step in order. Do not skip steps. Do not combine steps.

---

## STEP 1 -- STATUS QUO ANCHOR

Name where each persona class came from before generating any tickets.

| Persona class | Prior tool / STATUS QUO behavior | Key capability they expect to carry over | Most likely violated assumption |
|---------------|----------------------------------|------------------------------------------|----------------------------------|
| Support | | | |
| SRE | | | |
| PM / UX | | | |
| C-01..C-04 (technical early adopters) | | | |
| C-05..C-08 (pragmatic mainstream) | | | |
| C-09..C-12 (enterprise/compliance) | | | |

---

## STEP 2 -- ASSUMPTION AUDIT

For each violated assumption in column 4 of the inertia map, complete the full chain.

| # | Persona class | Incumbent behavior that created assumption | User's imported expectation | What this feature does instead | Resulting failure mode | Ticket ID |
|---|---------------|-------------------------------------------|---------------------------|-------------------------------|----------------------|-----------|

Minimum 1 row. The failure mode must be non-obvious from the happy-path spec alone.
Leave Ticket ID blank; fill in after Step 6.

```
ASSUMPTION AUDIT COMPLETE:
  Violated assumptions documented: [N]
  Each row complete (all 6 non-ID columns populated): YES / NO
  Ticket IDs pending: [N]
```

---

## STEP 3 -- PHASE-SEVERITY GRADIENT PRIOR

```
PHASE-SEVERITY PRIOR:
  Phase 1 (Day 0-30):  typical P2/P3; P0 only for activation blockers affecting all users
  Phase 2 (Day 31-60): typical P1/P2; P0 exceptional (data loss or workflow corruption)
  Phase 3 (Day 61-90): typical P0/P1; P3 rare (users have exhausted workarounds)
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

Constraints: Phase 1 >= 3. Phase 3 >= 1. Total >= 7. All three phases non-zero.

---

## STEP 5 -- PERSONA VOICE TABLE

Build the vocabulary table before writing any bodies. Minimum 2 distinct personas.

| Persona | Operational vocabulary | Frustration register | Framing conventions |
|---------|----------------------|---------------------|---------------------|
| Support | (>= 2 specific terms) | (>= 2 specific phrases) | (>= 2 structural patterns) |
| SRE | (>= 2 specific terms) | (>= 2 specific phrases) | (>= 2 structural patterns) |
| [other personas used] | (>= 2 specific terms) | (>= 2 specific phrases) | (>= 2 structural patterns) |

Anti-pattern: Do not populate cells with role labels. The table must contain actual words
and phrases that will appear in body text.

---

## STEP 6 -- TICKET SUMMARY TABLE

Generate the ticket table with Phase column. Assign severity consistent with Phase-Severity Prior.

| # | Phase | Title | Category | Persona | Volume | Severity |
|---|-------|-------|----------|---------|--------|----------|

Allowed values:
- Phase: Phase 1 | Phase 2 | Phase 3
- Category: how-to | bug | feature-request | config | integration
- Persona: Support | SRE | PM | UX | C-01 through C-12
- Volume: high | medium | low
- Severity: P0 | P1 | P2 | P3

After completing the table, update Step 2's Ticket ID column for each assumption audit row.
Then run the full validation trace:

```
VALIDATION TRACE:
  Distinct categories:                [N] (required: >= 3)             -> PASS / FAIL
  Distinct personas:                  [N] (required: >= 2)             -> PASS / FAIL
  P0 count:                           [N] (required: <= 1)             -> PASS / FAIL
  Low/medium volume entries:          [N] (required: >= 1)             -> PASS / FAIL
  Total rows:                         [N] (required: >= 7)             -> PASS / FAIL
  Phase 1 rows:                       [N] (target: [N from Step 4])   -> MATCH / MISMATCH
  Phase 2 rows:                       [N] (target: [N from Step 4])   -> MATCH / MISMATCH
  Phase 3 rows:                       [N] (target: [N from Step 4])   -> MATCH / MISMATCH
  All personas in voice table:        YES / NO                        -> PASS / FAIL
  Assumption audit Ticket IDs all assigned: YES / NO                  -> PASS / FAIL
  Phase-severity consistent with prior:
    Phase 1 severities (P2/P3 expected): [list actual values]         -> PASS / FAIL
    Phase 2 severities (P1/P2 expected): [list actual values]         -> PASS / FAIL
    Phase 3 severities (P0/P1 expected): [list actual values]         -> PASS / FAIL
  Overall:                                                             -> PASS / FAIL
```

Do not write any body until VALIDATION TRACE shows Overall: PASS.

---

## STEP 7 -- TICKET BODIES

For each table row, write the ticket body. Write the way that person actually types.
Do not open any body with a persona declaration.

For tickets linked to an assumption audit row: the body must contain the comparison framing
(what the user expected based on incumbent behavior vs. what they found). For all other
tickets: write in pure persona voice.

Each body must deploy at least 2 markers from different columns of the persona's voice
table row. After each body, cite the deployed markers:

### Ticket [N] [Phase N]: [Title from table]
**Assumption trace:** [audit row N, or "net-new friction"]
**Body:** [2-5 sentences in the persona's actual voice]
**Markers deployed:** [marker 1 (column name)] / [marker 2 (column name)]

---

## STEP 8 -- POST-GENERATION PHASE CONFIRMATION

```
PHASE CONFIRMATION:
  Phase 1 bodies generated: [N]   Target: [N]   -> MATCH / MISMATCH
  Phase 2 bodies generated: [N]   Target: [N]   -> MATCH / MISMATCH
  Phase 3 bodies generated: [N]   Target: [N]   -> MATCH / MISMATCH
  Total bodies:             [N]   Target: [N]   -> MATCH / MISMATCH
```

---

## STEP 9 -- GAP ANALYSIS TABLE

Present the gap analysis as a structured table. Every row must have a non-empty
Classification cell. Do not use a preamble note to classify gaps in aggregate.

| # | Gap type | Specific artifact to create or change | Classification | Incumbent status | Phase first surfaces |
|---|----------|--------------------------------------|----------------|-----------------|---------------------|

Column definitions:
- Gap type: Doc | Design | Operational
- Specific artifact: name the exact doc section, config field, API endpoint, runbook page, or UI element
- Classification: PARITY (incumbent already provides this) or NET-NEW (no incumbent equivalent or unique feature promise)
- Incumbent status: what the prior tool offers in this area, or "no incumbent equivalent"
- Phase first surfaces: Phase 1 | Phase 2 | Phase 3

Minimum: 1 Doc row, 1 Design row, 1 Operational row.

For gaps that trace to an assumption audit row: the classification should align with the
audit reasoning -- if the incumbent had the capability, the gap is PARITY; if the gap is
unique to this feature's promise, it is NET-NEW.

After completing the table, confirm:

```
GAP CLASSIFICATION COVERAGE:
  Total gap entries:           [N]
  Entries with Classification: [N]
  Coverage:                    [N]% (required: >= 60%)  -> PASS / FAIL
  PARITY entries:              [N]
  NET-NEW entries:             [N]
  Assumption-audit-sourced gaps classified PARITY: [N] of [N]  -> [check]
```
```

---

## V-05: Full R3 Synthesis -- Gap Classification Table + Assumption Audit + Column-Attributed Marker Citation

**Axes combined:** Gap analysis as classification table (V-01, C-14) + explicit violated-assumption
audit step (V-02, C-15) + column-attributed marker citation (V-03, C-16) + full R2 baseline
(phase-severity prior, phase distribution target, persona voice table, validation trace,
post-generation confirmation, inertia map).

**Combination hypothesis:** The three R3 mechanisms operate at different stages of the
generation sequence with no structural overlap:
- C-15 mechanism (ASSUMPTION AUDIT) runs at Step 2 -- pre-generation reasoning
- C-16 mechanism (column-attributed citations) runs at Step 7 -- during body generation
- C-14 mechanism (gap classification table) runs at Step 9 -- post-generation synthesis

This staging means stacking all three does not create competing constraints in any single
step. The hypothesis is that each mechanism can achieve its criterion independently while
they collectively raise output quality: the assumption audit produces better-grounded
non-obvious tickets (C-09), the column-attributed citations enforce cross-dimension voice
density (C-12), and the gap table produces per-entry competitive framing (C-14).

The full synthesis also tests for ceiling interference: whether nine sequential gates
(assumption audit -> phase prior -> phase target -> voice table -> ticket table ->
validation trace -> bodies with citations -> phase confirmation -> gap table) create
cognitive overload that degrades ticket quality or voice authenticity. The prior rounds
showed that R2 V-05's six gates did not degrade quality; R3 V-05 adds three more gates
across different output zones.

**C-14 + C-15 interaction:** When the ASSUMPTION AUDIT forward-links to specific tickets,
the gap analysis can back-link: each gap that originates from an assumption audit row
is structurally PARITY (the incumbent had the capability). Gaps from net-new friction
tickets are structurally NET-NEW. This forward/backward linkage makes the PARITY/NET-NEW
classifications non-arbitrary -- they derive from the assumption audit reasoning, not
from ad-hoc labeling.

---

```
# listen-support: Predict First-90-Day Support Tickets

Work through each step in order. Do not skip steps. Do not combine steps.

---

## STEP 1 -- STATUS QUO ANCHOR

Name where each persona class came from before generating any tickets. This is the
foundation for both assumption reasoning (Step 2) and gap classification (Step 9).

| Persona class | Prior tool / STATUS QUO behavior | Key capability they expect to carry over | Most likely violated assumption |
|---------------|----------------------------------|------------------------------------------|----------------------------------|
| Support | | | |
| SRE | | | |
| PM / UX | | | |
| C-01..C-04 (technical early adopters) | | | |
| C-05..C-08 (pragmatic mainstream) | | | |
| C-09..C-12 (enterprise/compliance) | | | |

---

## STEP 2 -- ASSUMPTION AUDIT

For each violated assumption in column 4 of the inertia map, complete the full reasoning chain.
This is the named analytical step that produces non-obvious failure modes structurally rather
than incidentally.

| # | Persona class | Incumbent behavior that created assumption | User's imported expectation | What this feature does instead | Resulting failure mode | Ticket ID |
|---|---------------|-------------------------------------------|---------------------------|-------------------------------|----------------------|-----------|

Minimum 1 row. The failure mode must be non-obvious from the happy-path spec alone --
it requires knowing the incumbent's behavior to predict.

Leave Ticket ID blank; fill in after Step 6 when tickets are assigned numbers.

```
ASSUMPTION AUDIT COMPLETE:
  Rows documented: [N]
  Each row complete (all 6 non-ID columns populated): YES / NO
  Ticket IDs pending: [N] (to be assigned in Step 6)
```

---

## STEP 3 -- PHASE-SEVERITY GRADIENT PRIOR

State the principled severity prior before declaring targets or generating tickets.

Phase 1 (Day 0-30): first-impressions and setup friction. Users have not yet invested deeply.
Typical P2/P3. P0 only for activation blockers affecting all users simultaneously.

Phase 2 (Day 31-60): adoption edge cases. Users succeeded at the happy path and are
committing real data and workflows. Typical P1/P2. P0 exceptional (data loss or
workflow corruption).

Phase 3 (Day 61-90): operational steady-state. Systems run at scale. Typical P0/P1.
P3 rare (users have exhausted workarounds).

```
PHASE-SEVERITY PRIOR:
  Phase 1 (Day 0-30):  typical P2/P3; P0 only for activation blockers affecting all users
  Phase 2 (Day 31-60): typical P1/P2; P0 exceptional (data loss or workflow corruption)
  Phase 3 (Day 61-90): typical P0/P1; P3 rare (users have exhausted workarounds)
```

---

## STEP 4 -- PHASE DISTRIBUTION TARGET

Declare the binding ticket count per phase.

```
PHASE DISTRIBUTION TARGET:
  Phase 1 (Day 0-30):  [N] tickets   -- setup friction, first-impression errors, activation issues
  Phase 2 (Day 31-60): [N] tickets   -- adoption edge cases, assumption violations, workflow friction
  Phase 3 (Day 61-90): [N] tickets   -- operational steady-state, integration issues, scale failures
  Total:               [N] tickets
```

Constraints: Phase 1 >= 3. Phase 3 >= 1. Total >= 7. All three phases non-zero.

Note: Assumption-audit tickets (Step 2) most frequently surface in Phase 2 -- the user has
committed to the tool and encountered the violated assumption under real conditions. However,
some violated assumptions surface in Phase 1 (setup-time assumption, e.g., expected default
behavior that differs) or Phase 3 (scale-time assumption, e.g., expected operational tooling).
Assign phase based on when the violation is likely to be experienced.

---

## STEP 5 -- PERSONA VOICE TABLE

Build the vocabulary table before writing any bodies. Populate with specific words and
phrases that will appear verbatim in body text.

| Persona | Operational vocabulary | Frustration register | Framing conventions |
|---------|----------------------|---------------------|---------------------|
| Support | (>= 2 specific terms) | (>= 2 specific phrases) | (>= 2 structural patterns) |
| SRE | (>= 2 specific terms) | (>= 2 specific phrases) | (>= 2 structural patterns) |
| [other personas used] | (>= 2 specific terms) | (>= 2 specific phrases) | (>= 2 structural patterns) |

Column definitions:
- Operational vocabulary: domain-specific nouns and verbs this persona uses professionally
  (examples: escalation queue, runbook entry, SLO budget, change board ticket, config schema)
- Frustration register: first-person incident-voice phrases used when blocked
  (examples: "I've closed 8 of these today", "paged at 02:14 with a blank runbook page",
  "three customer calls cited this gap")
- Framing conventions: structural or rhetorical patterns
  (examples: numbered repro steps / incident timeline with timestamps / user-research
  citation with count / click-path description with label names / config excerpt in
  code block / expected-vs-actual comparison / approval-chain reference)

Anti-pattern: Do not populate cells with role labels. The table must contain actual words
and phrases that will appear in body text. Minimum 2 distinct personas.

Each body in Step 7 must deploy at least 2 markers from DIFFERENT columns. The
column-attributed citation format (Step 7) will verify this cross-dimension requirement.

---

## STEP 6 -- TICKET SUMMARY TABLE

Generate the ticket table with Phase column. Assign severity consistent with the
phase-severity prior from Step 3. At least one ticket must trace to an assumption audit row.

| # | Phase | Title | Category | Persona | Volume | Severity |
|---|-------|-------|----------|---------|--------|----------|

Allowed values -- no other values are valid:
- Phase: Phase 1 | Phase 2 | Phase 3
- Category: how-to | bug | feature-request | config | integration
- Persona: Support | SRE | PM | UX | C-01 through C-12
- Volume: high | medium | low
- Severity: P0 | P1 | P2 | P3

After completing the table, update Step 2's Ticket ID column for each assumption audit row.
Then run the full validation trace:

```
VALIDATION TRACE:
  Distinct categories:                  [N] (required: >= 3)              -> PASS / FAIL
  Distinct personas:                    [N] (required: >= 2)              -> PASS / FAIL
  P0 count:                             [N] (required: <= 1)              -> PASS / FAIL
  Low/medium volume entries:            [N] (required: >= 1)              -> PASS / FAIL
  Total rows:                           [N] (required: >= 7)              -> PASS / FAIL
  Phase 1 rows:                         [N] (target: [N from Step 4])    -> MATCH / MISMATCH
  Phase 2 rows:                         [N] (target: [N from Step 4])    -> MATCH / MISMATCH
  Phase 3 rows:                         [N] (target: [N from Step 4])    -> MATCH / MISMATCH
  All personas in voice table:          YES / NO                         -> PASS / FAIL
  All assumption audit rows linked to ticket IDs: YES / NO               -> PASS / FAIL
  Phase-severity consistent with prior:
    Phase 1 severities (P2/P3 expected): [list actual values]            -> PASS / FAIL
    Phase 2 severities (P1/P2 expected): [list actual values]            -> PASS / FAIL
    Phase 3 severities (P0/P1 expected): [list actual values]            -> PASS / FAIL
  Overall:                                                                -> PASS / FAIL
```

Do not write any ticket body until VALIDATION TRACE shows Overall: PASS.

---

## STEP 7 -- TICKET BODIES WITH COLUMN-ATTRIBUTED MARKER CITATIONS

For each table row, write the ticket body. Write the way that person actually types.

Rules:
1. Do not open any body with a persona declaration ("As an SRE..." or "I am a Support
   agent who..."). Start with the issue. The voice comes from the vocabulary, not the label.
2. Each body must deploy at least 2 markers from DIFFERENT columns of the persona's voice
   table row (operational AND frustration, or operational AND framing, or frustration AND framing).
3. For tickets linked to an assumption audit row: the body must contain the comparison
   framing from that row -- what the user expected (from incumbent behavior) vs. what they found.
4. For tickets not linked to an assumption audit row: write in pure persona voice.

After each body, cite the deployed markers using column-attributed format:

```
Voice markers: operational=[specific term] | frustration=[specific phrase]
```
OR:
```
Voice markers: operational=[specific term] | framing=[structural pattern]
```
OR:
```
Voice markers: frustration=[specific phrase] | framing=[structural pattern]
```
OR (aspirational -- 3 columns):
```
Voice markers: operational=[specific term] | frustration=[specific phrase] | framing=[structural pattern]
```

Rules for Voice markers citation:
- Use the exact column label prefix (operational= / frustration= / framing=)
- Name the specific word or phrase deployed -- not a description or category of it
- Require at least 2 DIFFERENT prefixes per body (same prefix twice fails cross-dimension test)
- "2 markers deployed" without naming fails C-16; "operational=runbook" names the marker correctly

Format:

### Ticket [N] [Phase N]: [Title from table]
**Assumption trace:** [audit row N, or "net-new friction"]
**Body:** [2-5 sentences in the persona's actual voice]
**Voice markers:** operational=[term] | frustration=[phrase]
(or any 2+ different column prefixes from the voice table)

---

## STEP 8 -- POST-GENERATION PHASE AND CITATION CONFIRMATION

Confirm phase distribution:

```
PHASE CONFIRMATION:
  Phase 1 bodies generated: [N]   Target: [N]   -> MATCH / MISMATCH
  Phase 2 bodies generated: [N]   Target: [N]   -> MATCH / MISMATCH
  Phase 3 bodies generated: [N]   Target: [N]   -> MATCH / MISMATCH
  Total bodies:             [N]   Target: [N]   -> MATCH / MISMATCH
```

Confirm marker citation coverage:

```
MARKER CITATION AUDIT:
  Bodies with Voice markers citation:        [N] of [N] bodies
  Bodies with 2+ different column prefixes:  [N] of [N] bodies
  Coverage:                                  [N]% (required: >= 60%)  -> PASS / FAIL
  Bodies with 3 column prefixes (aspirational): [N] of [N] bodies
```

If PHASE CONFIRMATION shows any MISMATCH or MARKER CITATION AUDIT shows FAIL, revise
before proceeding to Step 9.

---

## STEP 9 -- GAP ANALYSIS CLASSIFICATION TABLE

Present the full gap analysis as a structured table. Every row must have a non-empty
Classification cell. Do not use a preamble paragraph to classify gaps in aggregate --
classification is per-entry.

| # | Gap type | Specific artifact to create or change | Classification | Incumbent status | Phase first surfaces |
|---|----------|--------------------------------------|----------------|-----------------|---------------------|

Column definitions:
- Gap type: Doc | Design | Operational
- Specific artifact: name the exact doc section, config field, API endpoint, runbook page, or UI element
  (Anti-pattern: "improve documentation" without naming the artifact fails; "add troubleshooting
  section to getting-started guide covering error code E-4023" passes)
- Classification: PARITY or NET-NEW
  - PARITY: the incumbent or prior tool already provides this capability; closing it is table stakes
  - NET-NEW: no incumbent equivalent; this is a differentiation opportunity or a unique expectation
    from the feature promise
  (Anti-pattern: leaving this cell blank, writing "TBD", or writing "both" fails per-entry test)
- Incumbent status: what the prior tool or incumbent offers in this area; required for PARITY rows
  (example: "Prior tool had /health/ready endpoint returning queue depth"; for NET-NEW: "no incumbent equivalent")
- Phase first surfaces: Phase 1 | Phase 2 | Phase 3

Classification guidance: Gaps that trace to an assumption audit row are presumptively PARITY
(the incumbent had the capability that created the violated assumption). Gaps from net-new
friction tickets are presumptively NET-NEW. Verify each classification against the inertia
map before finalizing.

Minimum: 1 Doc row, 1 Design row, 1 Operational row.

After completing the table, confirm:

```
GAP CLASSIFICATION SUMMARY:
  Total gap entries:                    [N]
  Entries with Classification:          [N]
  Coverage:                             [N]% (required: >= 60%)  -> PASS / FAIL
  PARITY entries:                       [N]
  NET-NEW entries:                      [N]
  Assumption-audit-sourced gaps:        [N] -- expected classification: PARITY
  All assumption-audit gaps classified PARITY: YES / NO
  Net-new-friction gaps:               [N] -- expected classification: NET-NEW
```
```
