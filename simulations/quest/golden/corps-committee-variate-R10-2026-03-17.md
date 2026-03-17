---
skill: quest-variate
skill_target: corps-committee
date: 2026-03-17
round: 10
rubric_version: 10
---

# corps-committee -- Prompt Variations R10

## Variation Summary

| ID   | Axis                                                                                        | Hypothesis |
|------|---------------------------------------------------------------------------------------------|------------|
| V-01 | Per-block COMMIT seals (C-31) — single axis                                                | Emitting an explicit B1/B2/B3/B4 COMMIT seal after every pre-execution block's content is complete — before any downstream block or phase begins — makes the "this block is sealed and available for citation" boundary explicit rather than implied by ordering. A downstream block cannot cite a token from an upstream block that has not yet emitted its COMMIT seal. The test: can any downstream block cite a B3 token before B3-COMMIT appears? If yes, availability is ambiguous. Sealing each block makes that ambiguous window structurally impossible. |
| V-02 | TOKEN TRACE CONFIRMATION in Phase 2 (C-32) — single axis                                  | Adding a named, structured TOKEN TRACE CONFIRMATION table as a required Phase 2 output element — re-validating each inertia token's presence in Phase 2 pre-mortem and dissent rows by explicit label citation — closes C-32: the TRACE GATE at Phase 1→2 ensures tokens enter Phase 2 with a committed chain, but the CONFIRMATION ensures they survive to Phase 2 output. A token that cleared the gate but dropped out before the dissent row is only detectable with an active re-validation step inside Phase 2. |
| V-03 | AMEND-AFFECTED SITES notation (C-33) — single axis                                        | Emitting an AMEND-AFFECTED SITES block listing every output element rendered stale by the amendment — by structural reference and affected token — before re-execution begins closes C-33: amendment impact is visible at the artifact layer (which elements are stale) rather than only at the execution-routing layer (which blocks must re-run). A reviewer scanning the stale manifest can verify the amendment was correctly scoped before a single phase re-executes. |
| V-04 | Combination: C-31 + C-32 (sealed blocks + Phase 2 token confirmation as linked chain)    | Combining explicit per-block COMMIT seals with Phase 2 TOKEN TRACE CONFIRMATION creates a complete availability-through-consumption audit chain: each COMMIT seal closes a block's output before downstream citation is permitted; the Phase 2 CONFIRMATION table then re-validates that every sealed token reached final output without dropout. The two mechanisms close different windows in the same audit chain — COMMIT seals close the pre-execution availability window; CONFIRMATION closes the Phase 2 output survival window. Neither mechanism alone is sufficient. |
| V-05 | Full integration: C-31 + C-32 + C-33 + best of R9 architecture                           | Integrating per-block COMMIT seals (C-31), Phase 2 TOKEN TRACE CONFIRMATION (C-32), and AMEND-AFFECTED SITES notation (C-33) into the best R9 architecture — BLOCK DEPENDENCY MAP (C-28), TOKEN TRACE MANIFEST at Phase 1→2 gate (C-29), AMEND block routing table (C-30), vocabulary contract (C-24), tier-sequenced voice with production constraint (C-25), per-tier column grammar (C-26), inertia token anchoring in dissent (C-27), standalone Challenger block (C-23) — produces a fully integrated skill where every block is explicitly sealed, every token is traceable end-to-end including Phase 2 re-validation, and every amendment emits a staleness manifest before re-execution. |

---

## V-01 -- Per-Block COMMIT Seals

**Axis:** Per-block COMMIT seals (C-31)
**Hypothesis:** Emitting explicit B1/B2/B3/B4 COMMIT seals after each pre-execution block's
content is generated — before any downstream block or phase begins — makes block output
availability explicit rather than implied by ordering. A downstream consumer cannot begin
until the upstream block has emitted its COMMIT seal. This closes C-31 by creating sealed
output boundaries rather than relying on positional ordering to imply a clean handoff.

```
You are running /corps-committee.

Simulate the committee meeting before it happens. Types: ROB (product/service review),
shiproom (go/no-go), arch-board (architecture decision review). Read participant charters
from .craft/roles/. Output: mock meeting minutes with decisions, action items, dissenting
opinions.

---

## BEFORE YOU START

Type-specific primary obligations and fail conditions:

ROB: Produce a readiness verdict backed by metric evidence.
  FAIL: No metric in output = you have not done a ROB.

SHIPROOM: Produce a binary GO / NO-GO decision with a stated blocking condition if NO-GO.
  FAIL: No GO or NO-GO decision line = you have not done a shiproom.

ARCH-BOARD: Produce an ADR with named architectural trade-offs and a selected alternative.
  FAIL: No named trade-offs = you have not done an arch-board.

COMMON FAIL: Any participant speaking from the wrong role (PM raises deployment topology as
primary; SRE leads product vision discussion) = FAIL C-02 before minutes are written.

---

## PRE-EXECUTION ZONE

Execute B1 → B3 → B2 → B4 in order. Each block ends with an explicit COMMIT seal.
No downstream block or phase may begin until all COMMIT seals above it are present.
Downstream citation of a block's tokens before that block's COMMIT seal has been
emitted is a structural violation of C-31.

---

### B1 -- Outcome Vocabulary Contract

State your committee type. Commit the allowed outcome tokens.

Committee Type: [ROB / SHIPROOM / ARCH-BOARD]

Vocabulary:
  ROB:        APPROVED | APPROVED WITH CONDITIONS | BLOCKED | DEFERRED
  SHIPROOM:   GO | NO-GO | HOLD
  ARCH-BOARD: ACCEPTED | REJECTED | DEFERRED

Committed vocabulary for this simulation: [list tokens for declared type only]

All downstream STANCE labels, TALLY rows, and Verdict draw exclusively from this committed
set. Tokens not in this list are not valid in this simulation.

B1-COMMIT: [committee type] vocabulary sealed. Tokens: [committed tokens].
  Downstream blocks and phases may now cite these tokens.
  NOTE: any block that cites a B1 token before this COMMIT line exists has violated C-31.

---

### B3 -- Inertia Inventory (executes before B2; B2 consumes B3 tokens)

Investigate what is already in place and at risk.

INERTIA-FINDING-1: [specific workflow or tool in production this agenda item displaces]
INERTIA-FINDING-2: [specific integration surface at risk; name systems, APIs, or contracts]
INERTIA-FINDING-3: [team whose cognitive habit would break; name the team and the habit]
INERTIA-FINDING-4: [non-obvious switching cost the proposal author did not account for]

GATE: Does INERTIA-FINDING-4 reveal a cost the proposal author would not have anticipated?
IF NO: rewrite all four findings. Retry until YES.

INERTIA RECORD (sealed):
| Token              | One-Phrase Anchor                      |
|--------------------|----------------------------------------|
| INERTIA-FINDING-1  | [anchor]                               |
| INERTIA-FINDING-2  | [anchor]                               |
| INERTIA-FINDING-3  | [anchor]                               |
| INERTIA-FINDING-4  | [anchor]                               |

INERTIA INVARIANT: sealed at B3-COMMIT -- findings may not be added, removed, or modified
  without reopening B3.

B3-COMMIT: Inertia inventory sealed. Tokens INERTIA-FINDING-1 through INERTIA-FINDING-4
  are now available for citation by B2 and B4.
  NOTE: any block that cites an INERTIA-FINDING-N token before this COMMIT line exists
  has violated C-31. B2 and B4 must verify this seal is present before citing any token.

---

### B2 -- Tier Pre-Assignment (consumes B1 vocabulary; consumes B3 tokens)

Entry check: B1-COMMIT present? [YES / NO -- HALT if NO]
Entry check: B3-COMMIT present? [YES / NO -- HALT if NO]

Assign each participant a voice tier before roster construction.

Tier 1 -- Challenger: voices concern against the dominant position; speaks first.
  Required fields: STANCE-from-B1 token + Inertia Citation (must be a B3 token)
Tier 2 -- Conditional: conditional support contingent on stated conditions; speaks second.
  Required fields: STANCE-from-B1 token + explicit stated condition
Tier 3 -- Advocate: supports proposal; responds to prior concerns; speaks last.
  Required fields: STANCE-from-B1 token + RESPONDS-TO pointer

| Participant | Role | Tier | STANCE-from-B1 | Inertia Citation (T1 only) | Key Obligation |
|-------------|------|------|----------------|---------------------------|----------------|
| [name]      | [role] | T1 | [B1 token]   | [INERTIA-FINDING-N]       | [what this role challenges] |
| [name]      | [role] | T2 | [B1 token]   | --                        | [stated condition] |
| [name]      | [role] | T3 | [B1 token]   | --                        | RESPONDS-TO: [T1/T2 entry] |

ORDERING CONSTRAINT (structural, not stylistic): All T1 voices are generated before any
T2 voice begins. All T2 voices are generated before any T3 voice begins. A T3 voice
appearing before a T1 Challenger concern exists is a structural violation -- FAIL C-25.

B2-COMMIT: Tier assignments sealed. B1 vocabulary consumed. B3 tokens cited.
  Ordering constraint committed.
  NOTE: any block that cites a tier assignment before this COMMIT line exists has violated C-31.
  Phase 0 roster must verify this seal before constructing the attendee list.

---

### B4 -- Designated Inertia Challenger (consumes B2 tier assignments; consumes B3 tokens)

Entry check: B2-COMMIT present? [YES / NO -- HALT if NO]
Entry check: B3-COMMIT present? [YES / NO -- HALT if NO]

Designate one participant as Inertia Challenger before Phase 0 begins.
This block renders as a standalone structural element before Phase 0 -- not embedded
in roster construction.

DESIGNATED INERTIA CHALLENGER:
  Role: [role name]
  Tier: [must be T1 -- verified against B2 roster; FAIL if mismatch]
  Outside-in rationale: [why this frame is least likely to reflect normalized assumptions;
    must be specific, not generic]
  NORM label obligation: [INERTIA-FINDING-N from B3 -- this token is their required
    Phase 1 citation; must exist in B3 INERTIA RECORD]

If no qualifying participant exists: inject an Inertia-Advocate candidate:
  [Note: [role] is a candidate Inertia Challenger -- confirmed or replaced in Phase 2]

B4-COMMIT: Challenger designated. B2 tier confirmed. B3 NORM obligation assigned.
  Phase 0 may now begin.
  NOTE: any phase that generates simulation content before this COMMIT line exists has
  violated C-31. Phase 0 entry check must verify B4-COMMIT is present.

---

## PHASE 0 -- Roster and Charter Preconditions

Entry check: B1-COMMIT present? [YES] B2-COMMIT? [YES] B3-COMMIT? [YES] B4-COMMIT? [YES]
IF any missing: halt. Emit the missing block before proceeding.

Charter constraints (declared as entry preconditions, not post-hoc):

| Constraint     | Charter Requirement               | Status |
|----------------|-----------------------------------|--------|
| Quorum         | [N members required / N present]  | MET / UNMET |
| Scope          | [what is in-scope / out-of-scope] | DECLARED |
| Veto holders   | [role(s) with veto authority]     | IDENTIFIED |
| Escalation     | [path if no consensus reached]    | COMMITTED |

Attendee List (derived from B2 tier assignments; B4 Challenger first):

| # | Participant | Role | Tier | Charter Status | Provisional? |
|---|-------------|------|------|----------------|--------------|
| 1 | [B4 Challenger] | [role] | T1 | [function] | [Note if candidate] |
| 2 | [other T1] | [role] | T1 | [function] | No |
| 3 | [T2] | [role] | T2 | [function] | No |
| 4 | [T3] | [role] | T3 | [function] | No |

PHASE-0-COMMIT: Roster locked. Charter constraints declared. All block COMMITs verified.
  | ENFORCE: terminal position -- NO PHASE 0 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 1 -- Discussion Simulation

Entry check: PHASE-0-COMMIT present? [YES / NO -- HALT if NO]

VOICE PRODUCTION RULE (structural constraint): Generate ALL T1 entries completely before
writing any T2 entry. Generate ALL T2 entries completely before writing any T3 entry.
Do not interleave tiers. Violation of this ordering = FAIL C-25.

Discussion grid (one row per voice, in tier order):

| Tier | Participant | Role | STANCE | Inertia Finding (T1: required; T2/T3: RESPONDS-TO) | Key Position |
|------|-------------|------|--------|-----------------------------------------------------|--------------|
| T1   | [Challenger] | [role] | [B1 token] | [INERTIA-FINDING-N -- required non-None]  | [concern] |
| T2   | [name] | [role] | [B1 token] | Condition: [explicit stated condition]         | [conditional position] |
| T3   | [name] | [role] | [B1 token] | RESPONDS-TO: [T1/T2 concern]; CITE: [source] | [endorsement] |

Voice completeness check (per tier):

| Tier | Required Fields | Complete? |
|------|----------------|-----------|
| T1 -- Challenger | STANCE + named INERTIA-FINDING-N citation | [YES / FAIL] |
| T2 -- Conditional | STANCE + explicit stated condition | [YES / FAIL] |
| T3 -- Advocate | STANCE + CITE reference + RESPONDS-TO pointer | [YES / FAIL] |

Any FAIL: block progression to PRE-MORTEM CHAIN CHECK. Fix before proceeding.

PRE-MORTEM CHAIN CHECK:

  CHAIN-1 -- Challenger identified: [name/role] -- Status: [CONFIRMED / HALT]
  CHAIN-2 -- Outside-in basis stated: [basis -- must not derive from internal normalized knowledge]
             Circularity check: [does this repeat an organizational assumption? YES = FAIL -- rephrase]
             Status: [CONFIRMED / FAIL]
  CHAIN-3 -- Risk draft connected to inertia: Risk: [draft] -- Connected to: [INERTIA-FINDING-N]
             Status: [CONFIRMED / HALT]

TRACE GATE: Phase 2 may not begin until CHAIN-1, CHAIN-2, CHAIN-3 are all CONFIRMED.
Phase 2 must expand the CHAIN-3 draft -- inconsistency between CHAIN-3 and Phase 2
pre-mortem is a FAIL.

PHASE-1-COMMIT: Discussion complete. CHAIN-CHECK all CONFIRMED. Tier ordering confirmed.
  | ENFORCE: terminal position -- NO PHASE 1 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 2 -- Meeting Minutes

Entry check: PHASE-1-COMMIT present? [YES / NO -- HALT if NO]

### Header
Committee: [type from B1]
Date: [date]
Attendees: [from Phase 0 roster -- flag provisional annotations]
Quorum: MET / NOT MET

### Agenda Items
[Agenda items as structured in Phase 0]

### Discussion Summary
[Prose summary, 2-4 sentences per agenda item. No new positions introduced here.]

### Decisions

Each decision must use a vocabulary token from B1-COMMIT. No other tokens permitted.

| # | Decision | Outcome Token (from B1) | Conditions | Decided By |
|---|----------|------------------------|------------|------------|
| 1 | [statement] | [B1 token] | [conditions or None] | [role] |

### Action Items

Owner column is required and non-empty for every row. Missing owner = missing cell = FAIL C-04/C-21.

| # | Action | Owner (named role) | Due | Linked Decision |
|---|--------|-------------------|-----|-----------------|
| 1 | [action] | [named owner -- required] | [date/TBD] | [#] |

### Dissenting Opinions

Per-participant rows. Missing row = FAIL C-05/C-22.

| Participant | Role | Dissent or Position | Inertia Token | Inertia Linkage Justification |
|-------------|------|---------------------|---------------|-------------------------------|
| [name] | [role] | [dissent / No dissent] | [INERTIA-FINDING-N or "resolved"] | [why this concern persists or was resolved] |

No-dissent entries must still carry the inertia token and justification. Absent = FAIL C-27.

### Pre-Mortem Risk

(Expands CHAIN-3 draft from Phase 1)
Risk: [expanded from CHAIN-3]
Inertia basis: [INERTIA-FINDING-N label]
Challenger: [name/role]
Why the real committee will miss this: [specific organizational normalization]

### Next Steps
[Follow-up meetings, escalations, or dependencies]

PHASE-2-COMMIT: Decisions, action items, dissent, pre-mortem written. Phase 2 closed.
  | ENFORCE: terminal position -- NO PHASE 2 CONTENT MAY FOLLOW THIS LINE.

---

## AMEND Handling

When AMEND is invoked:

Step 1 -- Classify the amendment and identify invalidated blocks:

| Amendment Type | Blocks Invalidated | Phases Affected |
|---------------|-------------------|-----------------|
| Participant composition change | B2 (tiers), B4 (Challenger) | Phase 0 roster, Phase 1 grid |
| Committee type change | B1 (vocabulary), B2 (STANCE tokens) | All phases |
| Scope change | Phase 0 charter constraints | Phase 1 grid |
| New agenda item | Phase 1 only | Phase 1, Phase 2 |

Step 2 -- Re-run only invalidated blocks. Emit updated COMMIT seals.
Step 3 -- Resume phases from first affected phase.
```

---

## V-02 -- TOKEN TRACE CONFIRMATION in Phase 2

**Axis:** TOKEN TRACE CONFIRMATION in Phase 2 (C-32)
**Hypothesis:** Adding a named, structured TOKEN TRACE CONFIRMATION section as a required
Phase 2 output element -- re-validating each inertia token against its consumption sites
in Phase 2 output -- closes C-32. The TRACE GATE at Phase 1→2 ensures tokens enter Phase 2
with a committed chain. The CONFIRMATION ensures they survive to Phase 2 final output.
A token that cleared the gate but dropped before the dissent table is only detectable
with an active re-validation inside Phase 2 itself -- not by checking the gate.

```
You are running /corps-committee.

Simulate the committee meeting before it happens. Types: ROB (product/service review),
shiproom (go/no-go), arch-board (architecture decision review). Read participant charters
from .craft/roles/. Output: mock meeting minutes with decisions, action items, dissenting
opinions.

---

## BEFORE YOU START

Type obligations:

ROB: Readiness verdict backed by metric evidence.
  FAIL: No metric = ROB not done.

SHIPROOM: Binary GO / NO-GO with blocking condition if NO-GO.
  FAIL: No GO/NO-GO decision line = shiproom not done.

ARCH-BOARD: ADR with named trade-offs and selected alternative.
  FAIL: No named trade-offs = arch-board not done.

---

## PRE-EXECUTION BLOCKS

### B1 -- Vocabulary Contract

Committee type: [ROB / SHIPROOM / ARCH-BOARD]

Committed vocabulary (type-specific):
  ROB:        APPROVED | APPROVED WITH CONDITIONS | BLOCKED | DEFERRED
  SHIPROOM:   GO | NO-GO | HOLD
  ARCH-BOARD: ACCEPTED | REJECTED | DEFERRED

Active tokens for this simulation: [list for declared type]

B1-COMMIT: Vocabulary sealed. Type: [type]. Tokens: [committed tokens]. Available for
  downstream consumption.

---

### B3 -- Inertia Inventory

(Runs before B2 because B2 cites B3 tokens.)

INERTIA-FINDING-1: [workflow / tool displaced]
INERTIA-FINDING-2: [integration surface at risk; name systems or contracts]
INERTIA-FINDING-3: [team whose cognitive habit breaks; name team and habit]
INERTIA-FINDING-4: [non-obvious switching cost author did not account for]

Gate: Does INERTIA-FINDING-4 reveal a cost the author would not have anticipated?
IF NO: rewrite all four. Retry until YES.

INERTIA RECORD:
| Token              | Anchor                                 |
|--------------------|----------------------------------------|
| INERTIA-FINDING-1  | [anchor]                               |
| INERTIA-FINDING-2  | [anchor]                               |
| INERTIA-FINDING-3  | [anchor]                               |
| INERTIA-FINDING-4  | [anchor]                               |

B3-COMMIT: Inventory sealed. INERTIA-FINDING-1 through INERTIA-FINDING-4 available for citation.

---

### B2 -- Tier Pre-Assignment (consumes B1 vocabulary; consumes B3 tokens)

| Participant | Role | Tier | STANCE-from-B1 | Inertia Citation (T1 only) |
|-------------|------|------|----------------|---------------------------|
| [name] | [role] | T1 | [B1 token] | [INERTIA-FINDING-N] |
| [name] | [role] | T2 | [B1 token] | -- |
| [name] | [role] | T3 | [B1 token] | -- |

Ordering constraint: ALL T1 voices before ANY T2; ALL T2 before ANY T3.

B2-COMMIT: Tier assignments sealed. Ordering constraint committed.

---

### B4 -- Designated Inertia Challenger (standalone block, before Phase 0)

(Renders as a structurally isolated block before Phase 0 roster construction.)

DESIGNATED INERTIA CHALLENGER:
  Role: [role name]
  Tier: T1 (verified against B2)
  Outside-in rationale: [specific, non-generic rationale]
  NORM label obligation: [INERTIA-FINDING-N from B3]

B4-COMMIT: Challenger designated. Phase 0 may begin.

---

## PHASE 0 -- Roster and Agenda

Entry: B1-COMMIT, B2-COMMIT, B3-COMMIT, B4-COMMIT all present.

Charter constraints (phase entry preconditions):
  Quorum: [requirement / met?]
  Scope: [in-scope / out-of-scope]
  Veto: [veto holders]
  Escalation: [path if no consensus]

Attendee List:
| # | Participant | Role | Tier | Provisional? |
|---|-------------|------|------|--------------|
| 1 | [B4 Challenger] | [role] | T1 | [Note if candidate] |
| ... | | | | |

PHASE-0-COMMIT: Roster locked. Charter constraints declared.
  | ENFORCE: terminal position -- NO PHASE 0 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 1 -- Discussion

VOICE ORDERING (structural): Generate all T1 voices before any T2. All T2 before any T3.

Discussion grid:
| Tier | Participant | Role | STANCE | Inertia Citation / RESPONDS-TO | Key Position |
|------|-------------|------|--------|-------------------------------|--------------|
| T1 | [Challenger] | [role] | [B1 token] | [INERTIA-FINDING-N -- required] | [concern] |
| T2 | [name] | [role] | [B1 token] | Condition: [explicit condition] | [position] |
| T3 | [name] | [role] | [B1 token] | RESPONDS-TO: [T1/T2]; CITE: [source] | [endorsement] |

Voice completeness check:
| Tier | Required | Complete? |
|------|----------|-----------|
| T1 | STANCE + INERTIA-FINDING-N citation | [YES/FAIL] |
| T2 | STANCE + explicit stated condition | [YES/FAIL] |
| T3 | STANCE + CITE + RESPONDS-TO | [YES/FAIL] |

PRE-MORTEM CHAIN CHECK:

  CHAIN-1: Challenger: [name/role] -- Status: CONFIRMED / HALT
  CHAIN-2: Outside-in basis: [basis] -- Non-circular: [YES/FAIL] -- Status: CONFIRMED / FAIL
  CHAIN-3: Risk draft: [statement] -- Connected to: [INERTIA-FINDING-N] -- Status: CONFIRMED / HALT

TOKEN TRACE MANIFEST (Phase 1→2 gate):
Tracks each inertia token from B3 through every Phase 2 consumption site.

| Token              | T1 Grid Row? | CHAIN-3 Draft? | Phase 2 Pre-Mortem? | Phase 2 Dissent Row? | GATE STATUS |
|--------------------|-------------|----------------|---------------------|----------------------|-------------|
| INERTIA-FINDING-1  | [row ref]   | [YES/NO]       | [SCHEDULED]         | [SCHEDULED]          | PENDING |
| INERTIA-FINDING-2  | [row ref]   | [YES/NO]       | [SCHEDULED]         | [SCHEDULED]          | PENDING |
| INERTIA-FINDING-3  | [row ref]   | [YES/NO]       | [SCHEDULED]         | [SCHEDULED]          | PENDING |
| INERTIA-FINDING-4  | [row ref]   | [YES/NO]       | [SCHEDULED]         | [SCHEDULED]          | PENDING |

TRACE GATE: All chains confirmed? If NO -- halt and fix before Phase 2.

PHASE-1-COMMIT: Discussion complete. TOKEN TRACE MANIFEST populated for Phase 2 consumption.
  Phase 2 will re-validate each token at output. Phase 1 closed.
  | ENFORCE: terminal position -- NO PHASE 1 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 2 -- Meeting Minutes

Entry: PHASE-1-COMMIT present and all CHAIN-CHECKs CONFIRMED.

### Header
Committee: [type]  Date: [date]  Quorum: [MET/NOT MET]

### Decisions

| # | Decision | Outcome Token (from B1) | Conditions | Decided By |
|---|----------|------------------------|------------|------------|
| 1 | [statement] | [B1 token] | [conditions or None] | [role] |

### Action Items (Owner is a required column -- missing = FAIL C-04/C-21)

| # | Action | Owner | Due | Linked Decision |
|---|--------|-------|-----|-----------------|
| 1 | [action] | [named owner] | [date/TBD] | [#] |

### Dissenting Opinions (per-participant rows -- missing row = FAIL C-05/C-22)

| Participant | Role | Dissent | Inertia Token | Justification |
|-------------|------|---------|---------------|---------------|
| [name] | [role] | [dissent or No dissent] | [INERTIA-FINDING-N or resolved] | [why persists or resolved] |

### Pre-Mortem Risk (expands CHAIN-3 draft)

Risk: [expanded from CHAIN-3]
Inertia basis: [INERTIA-FINDING-N]
Challenger: [name/role]
Why the real committee will miss this: [specific organizational normalization -- not generic]

---

### TOKEN TRACE CONFIRMATION

Re-validate each inertia token against its Phase 2 consumption sites. This is an active
re-validation inside Phase 2 output, not a consequence of the Phase 1 TRACE GATE.

The TRACE GATE ensures tokens entered Phase 2 with a committed chain.
This CONFIRMATION ensures they survived to Phase 2 final output.

| Token              | Phase 2 Pre-Mortem (expanded?) | Phase 2 Dissent Row (cited?) | Phase 2 Decision (referenced?) | STATUS |
|--------------------|-------------------------------|------------------------------|--------------------------------|--------|
| INERTIA-FINDING-1  | [YES -- specific ref / NO]    | [YES -- row ref / NO]        | [YES / NO / N/A]               | CONFIRMED / DROPOUT |
| INERTIA-FINDING-2  | [YES / NO]                    | [YES / NO]                   | [YES / NO / N/A]               | CONFIRMED / DROPOUT |
| INERTIA-FINDING-3  | [YES / NO]                    | [YES / NO]                   | [YES / NO / N/A]               | CONFIRMED / DROPOUT |
| INERTIA-FINDING-4  | [YES / NO]                    | [YES / NO]                   | [YES / NO / N/A]               | CONFIRMED / DROPOUT |

DROPOUT REPAIR: Any row showing DROPOUT = Phase 2 output is incomplete.
  Return to the dropout site (pre-mortem or dissent row) and add the missing citation before
  delivering minutes. Do not deliver Phase 2 output with a DROPOUT in this table.

CONFIRMATION NOTE: Tokens confirmed here must match the TOKEN TRACE MANIFEST from Phase 1.
  Any token that was PENDING in Phase 1 and is DROPOUT here represents a gate-cleared token
  that failed to reach output -- the most insidious form of token dropout.

### Next Steps
[Follow-up, escalations, dependencies]

PHASE-2-COMMIT: Decisions, action items, dissent, pre-mortem, TOKEN TRACE CONFIRMATION all
  present. All tokens CONFIRMED in CONFIRMATION table. Simulation complete.
  | ENFORCE: terminal position -- NO PHASE 2 CONTENT MAY FOLLOW THIS LINE.

---

## AMEND Handling

When AMEND is invoked, re-run only the blocks and phases invalidated by the amendment.
Emit updated COMMIT seals for re-run blocks.
TOKEN TRACE CONFIRMATION in Phase 2 must be re-executed when any inertia token or
dissent row is affected by the amendment.
```

---

## V-03 -- AMEND-AFFECTED SITES Notation

**Axis:** AMEND-AFFECTED SITES notation (C-33)
**Hypothesis:** When AMEND is invoked, emitting an AMEND-AFFECTED SITES block that lists
every output element rendered stale by the amendment -- by structural reference and
affected token -- before any re-execution begins closes C-33. Amendment impact becomes
visible at the artifact layer (which elements are stale and why) rather than only at the
execution-routing layer (which blocks must re-run). A reviewer scanning the stale manifest
can verify the amendment was correctly scoped without reading any re-executed output.

```
You are running /corps-committee.

Simulate the committee meeting before it happens. Types: ROB (product/service review),
shiproom (go/no-go), arch-board (architecture decision review). Read participant charters
from .craft/roles/. Output: mock meeting minutes with decisions, action items, dissenting
opinions.

---

## BEFORE YOU START

Type obligations and fail conditions:

ROB: Readiness verdict backed by metric evidence. FAIL: No metric.
SHIPROOM: Binary GO / NO-GO with blocking condition if NO-GO. FAIL: No GO/NO-GO decision.
ARCH-BOARD: ADR with named trade-offs and selected alternative. FAIL: No named trade-offs.

---

## PRE-EXECUTION BLOCKS

### B1 -- Vocabulary Contract
Committee type: [ROB / SHIPROOM / ARCH-BOARD]
Active vocabulary: [committed tokens for this type]
  ROB: APPROVED | APPROVED WITH CONDITIONS | BLOCKED | DEFERRED
  SHIPROOM: GO | NO-GO | HOLD
  ARCH-BOARD: ACCEPTED | REJECTED | DEFERRED
B1-COMMIT: Type: [type]. Vocabulary: [tokens]. Sealed.

### B3 -- Inertia Inventory (before B2)
INERTIA-FINDING-1: [workflow/tool displaced]
INERTIA-FINDING-2: [integration surface at risk]
INERTIA-FINDING-3: [team habit that breaks]
INERTIA-FINDING-4: [non-obvious switching cost]
Gate: INERTIA-FINDING-4 non-obvious? IF NO: rewrite and retry.
INERTIA RECORD: [table with token and anchor for all four findings]
B3-COMMIT: Inventory sealed. Tokens available.

### B2 -- Tier Pre-Assignment (consumes B1 + B3)
| Participant | Role | Tier | STANCE-from-B1 | Inertia Citation (T1 only) |
|-------------|------|------|----------------|---------------------------|
Ordering constraint: ALL T1 before T2; ALL T2 before T3 (structural, not stylistic).
B2-COMMIT: Tiers sealed. Ordering committed.

### B4 -- Designated Inertia Challenger (standalone, before Phase 0)
DESIGNATED INERTIA CHALLENGER:
  Role: [role] | Tier: T1 (verified vs B2) | Outside-in rationale: [specific]
  NORM label obligation: [INERTIA-FINDING-N from B3]
B4-COMMIT: Challenger designated. Phase 0 may begin.

---

## PHASE 0 -- Roster and Agenda

Entry: B1/B2/B3/B4 COMMITs all present.

Charter constraints (preconditions):
  Quorum: [N required / N present] | Scope: [in / out] | Veto: [holders] | Escalation: [path]

Attendee List (from B2, B4 Challenger first):
| # | Participant | Role | Tier | Provisional? |
PHASE-0-COMMIT: Roster locked. Constraints declared.
  | ENFORCE: NO PHASE 0 CONTENT AFTER THIS LINE.

---

## PHASE 1 -- Discussion

VOICE ORDERING (structural): ALL T1 before T2; ALL T2 before T3.

Discussion grid:
| Tier | Participant | STANCE | Inertia Citation / RESPONDS-TO | Key Position |

Voice completeness check (per tier):
| Tier | Required Fields | Complete? |
| T1 | STANCE + INERTIA-FINDING-N | [YES/FAIL] |
| T2 | STANCE + explicit condition | [YES/FAIL] |
| T3 | STANCE + CITE + RESPONDS-TO | [YES/FAIL] |

PRE-MORTEM CHAIN CHECK:
  CHAIN-1: Challenger: [name] -- CONFIRMED / HALT
  CHAIN-2: Outside-in basis: [basis] -- non-circular: [YES/FAIL]
  CHAIN-3: Risk: [draft] -- Connected to: [INERTIA-FINDING-N] -- CONFIRMED / HALT

TRACE GATE: All chains CONFIRMED before Phase 2 begins.

PHASE-1-COMMIT: Discussion complete. Chain checkpoints all CONFIRMED.
  | ENFORCE: NO PHASE 1 CONTENT AFTER THIS LINE.

---

## PHASE 2 -- Meeting Minutes

### Header / Decisions / Action Items / Dissenting Opinions / Pre-Mortem Risk / Next Steps

[Standard Phase 2 sections -- see full template. All sections present.]

PHASE-2-COMMIT: Minutes complete.
  | ENFORCE: NO PHASE 2 CONTENT AFTER THIS LINE.

---

## AMEND Handling

### AMEND ROUTING TABLE

Maps each amendment type to the blocks it invalidates. Re-execution scope is determined
by block dependency, not by phase impact.

| Amendment Type | Pre-Execution Blocks Invalidated | Re-run Order |
|---------------|----------------------------------|--------------|
| Participant composition change | B2 (tiers), B4 (Challenger designation) | B2 → B4 → Phase 0 → Phase 1 → Phase 2 |
| Committee type change | B1 (vocabulary), B2 (STANCE tokens drawing from B1) | B1 → B2 → all phases |
| Scope change | Phase 0 charter constraints only | Phase 0 → Phase 1 → Phase 2 |
| New agenda item | Phase 1 only (no pre-execution blocks invalidated) | Phase 1 → Phase 2 |
| Challenger removed from roster | B4 (designation) | B4 → Phase 0 → Phase 1 → Phase 2 |

### AMEND-AFFECTED SITES

When AMEND is invoked:

STEP 1 -- Identify the amendment type (from AMEND ROUTING TABLE above).
STEP 2 -- Emit the AMEND-AFFECTED SITES block BEFORE any re-execution begins.

AMEND-AFFECTED SITES block format:

```
AMEND-AFFECTED SITES:
Amendment: [describe the change]
Amendment type: [from routing table]
Blocks invalidated: [B1, B2, B3, B4 -- list only those invalidated]

Stale output elements (by structural reference):
  [block/phase location] -- [element name] -- STALE: [reason] -- [re-run action required]
  [block/phase location] -- [element name] -- STALE: [reason] -- [re-run action required]

Example (composition change -- participant added):
  B2 Tier Assignment for [new participant] -- STALE: composition change; role not yet tiered
  B4 Challenger Designation -- STALE: new T1 candidate may qualify; re-designation required
  Phase 0 Attendee List -- STALE: B2 not yet re-committed; roster shows pre-amendment state
  Phase 1 Discussion Grid -- STALE: new participant voice absent
  Phase 2 Action Items -- STALE: owner table may change with new participant
  Phase 2 Dissenting Opinions -- STALE: new participant row absent

Example (committee type change -- ROB → SHIPROOM):
  B1 Vocabulary Contract -- STALE: type changed; APPROVED/BLOCKED vocabulary no longer valid
  B2 STANCE-from-B1 column -- STALE: B1 tokens changed; all STANCE cells must be re-assigned
  Phase 1 STANCE tokens -- STALE: B2 not yet re-committed; grid shows pre-amendment tokens
  Phase 2 Decisions Outcome Token -- STALE: B1 vocabulary changed; tokens in decision table invalid
```

STEP 3 -- Verify AMEND-AFFECTED SITES is complete before re-execution:
  All stale elements listed? [YES / NO]
  All structural references correct (block ID or phase section name)? [YES / NO]
  All affected tokens named? [YES / NO]
  IF any NO: add missing entries before re-executing.

STEP 4 -- Re-run invalidated blocks in routing order. Emit new COMMIT seals.
STEP 5 -- Resume phases from first affected phase.

RULE: An amendment that re-executes phases without first emitting an AMEND-AFFECTED SITES
block has skipped the staleness manifest step -- FAIL C-33.

RULE: An AMEND-AFFECTED SITES block that lists phases without naming specific elements
(e.g., "Phase 2 is stale" without naming which rows or columns are stale) is an
incomplete staleness manifest -- FAIL C-33.
```

---

## V-04 -- Sealed Blocks + Phase 2 Confirmation (C-31 + C-32 combined)

**Axis:** C-31 + C-32 (per-block COMMIT seals + Phase 2 TOKEN TRACE CONFIRMATION as linked audit chain)
**Hypothesis:** Per-block COMMIT seals and Phase 2 TOKEN TRACE CONFIRMATION close different
windows in the same end-to-end audit chain. COMMIT seals close the pre-execution
availability window: a downstream block cannot cite a token before the upstream block
that produces it has sealed its output. TOKEN TRACE CONFIRMATION closes the Phase 2
output survival window: a token that cleared the TRACE GATE but dropped before the
dissent table is only detectable inside Phase 2. Together they create an unbroken chain:
token minted (B3) → sealed (B3-COMMIT) → cited under seal (B2 under B3-COMMIT) → gate-cleared
(TRACE GATE at Phase 1→2) → confirmed at output (Phase 2 CONFIRMATION table). Any broken
link is visible at the layer where it breaks.

```
You are running /corps-committee.

Simulate the committee meeting before it happens. Types: ROB (product/service review),
shiproom (go/no-go), arch-board (architecture decision review). Read participant charters
from .craft/roles/. Output: mock meeting minutes with decisions, action items, dissenting
opinions.

---

## BEFORE YOU START

Type obligations and fail conditions:

ROB: Readiness verdict backed by metric evidence. FAIL: No metric = ROB not done.
SHIPROOM: Binary GO / NO-GO with blocking condition if NO-GO. FAIL: No GO/NO-GO.
ARCH-BOARD: ADR with named trade-offs and selected alternative. FAIL: No trade-offs.

Common FAIL: Participant speaking from wrong role = FAIL C-02.

---

## BLOCK DEPENDENCY MAP (declared before any block executes)

Blocks form an interdependent system. Each block declares its inputs before executing.

| Block | Label                     | Inputs Required Before Execution |
|-------|---------------------------|----------------------------------|
| B1    | Vocabulary Contract       | (origin -- no upstream dependencies) |
| B3    | Inertia Inventory         | (origin -- runs before B2 to supply tokens) |
| B2    | Tier Pre-Assignment       | B1-COMMIT (vocabulary tokens) + B3-COMMIT (inertia tokens) |
| B4    | Challenger Designation    | B2-COMMIT (tier assignments) + B3-COMMIT (NORM token) |
| Phase 0 | Roster Construction    | B1-COMMIT + B2-COMMIT + B3-COMMIT + B4-COMMIT (all four) |

DEPENDENCY RULE: A block may not execute until all listed inputs are present as COMMIT seals.
Citation of a token from an upstream block before that block's COMMIT seal = violation C-31.

---

### B1 -- Vocabulary Contract

Committee type: [ROB / SHIPROOM / ARCH-BOARD]

Type-keyed vocabulary:
  ROB:        APPROVED | APPROVED WITH CONDITIONS | BLOCKED | DEFERRED
  SHIPROOM:   GO | NO-GO | HOLD
  ARCH-BOARD: ACCEPTED | REJECTED | DEFERRED

Active tokens: [tokens for declared type only]

Downstream consumption obligations:
  B2: STANCE-from-B1 column must draw from this set
  Phase 1: all STANCE labels must draw from this set
  Phase 2: all Outcome Tokens must draw from this set

B1-COMMIT: Type: [type] | Vocabulary: [tokens] | Sealed.
  Downstream blocks may now cite B1 tokens. No citation permitted before this line.

---

### B3 -- Inertia Inventory

INERTIA-FINDING-1: [workflow/tool displaced]
INERTIA-FINDING-2: [integration surface at risk; name systems/APIs/contracts]
INERTIA-FINDING-3: [team cognitive habit that breaks; name team and habit]
INERTIA-FINDING-4: [non-obvious switching cost author did not account for]

Gate: Is INERTIA-FINDING-4 non-obvious to the proposal author? IF NO: rewrite and retry.

INERTIA RECORD:
| Token              | Anchor                                    |
|--------------------|-------------------------------------------|
| INERTIA-FINDING-1  | [anchor]                                  |
| INERTIA-FINDING-2  | [anchor]                                  |
| INERTIA-FINDING-3  | [anchor]                                  |
| INERTIA-FINDING-4  | [anchor]                                  |

INERTIA INVARIANT: sealed at B3-COMMIT -- findings may not be modified without reopening B3.

Downstream consumption obligations:
  B2: T1 Inertia Citation column must cite tokens from this record
  B4: NORM label obligation must cite a token from this record
  Phase 1: Tier 1 Inertia Finding column must cite tokens from this record
  Phase 1 CHAIN-3: risk draft must connect to a token from this record
  Phase 2 pre-mortem: must expand CHAIN-3; inertia basis cites a token from this record
  Phase 2 dissent: inertia token column cites tokens from this record

B3-COMMIT: Inertia inventory sealed. Tokens INERTIA-FINDING-1 through INERTIA-FINDING-4
  available for downstream citation.
  No block or phase may cite an INERTIA-FINDING-N token without this COMMIT having appeared.

---

### B2 -- Tier Pre-Assignment

Entry: B1-COMMIT present? [YES / HALT]  B3-COMMIT present? [YES / HALT]

Assign each participant to a voice tier.

| Participant | Role | Tier | STANCE-from-B1 | Inertia Citation (T1 only) | Obligation |
|-------------|------|------|----------------|---------------------------|------------|
| [name] | [role] | T1 | [B1 token] | [INERTIA-FINDING-N from B3] | [what this frame challenges] |
| [name] | [role] | T2 | [B1 token] | -- | Condition: [explicit] |
| [name] | [role] | T3 | [B1 token] | -- | RESPONDS-TO: [T1/T2]; CITE: [source] |

B2 cross-block integrity check:
- STANCE-from-B1: all tokens from B1 committed vocabulary? [YES / NO -- fix if NO]
- T1 Inertia Citation: all tokens present in B3 INERTIA RECORD? [YES / NO -- fix if NO]

Ordering constraint (structural): ALL T1 voices generated before ANY T2.
  ALL T2 voices generated before ANY T3.
  A T3 voice before a T1 concern exists = structural violation FAIL C-25.

B2-COMMIT: Tier assignments sealed. B1 consumed. B3 tokens cited.
  No block or phase may cite a tier assignment without this COMMIT having appeared.

---

### B4 -- Designated Inertia Challenger (standalone structural element, before Phase 0)

Entry: B2-COMMIT present? [YES / HALT]  B3-COMMIT present? [YES / HALT]

This block is rendered as a structurally isolated element before Phase 0.
It is not embedded in Phase 0 roster construction.

DESIGNATED INERTIA CHALLENGER:
  Role: [role name]
  Tier (from B2): [must be T1 -- verify against B2; FAIL if mismatch]
  Outside-in rationale: [why this frame is least normalized; specific, not generic]
  NORM label obligation: [INERTIA-FINDING-N from B3; must exist in INERTIA RECORD]
  Confirmation: B2 Tier 1 match? [YES / FAIL]  B3 token exists? [YES / FAIL]

If no qualifying participant: inject Inertia-Advocate candidate:
  [Note: [role] is a candidate Inertia Challenger -- confirmed or replaced in Phase 2]

B4-COMMIT: Challenger designated. B2 tier confirmed. B3 obligation assigned.
  Phase 0 may begin. No phase may generate simulation content before this COMMIT.

---

## PHASE 0 -- Roster and Agenda

Entry: ALL four COMMIT seals present (B1, B2, B3, B4). HALT if any missing.

Charter constraints (phase entry preconditions, not post-hoc):

| Constraint   | Requirement                              | Status |
|--------------|------------------------------------------|--------|
| Quorum       | [N required / N present]                 | MET / UNMET |
| Scope        | [in-scope items / out-of-scope boundary] | DECLARED |
| Veto holders | [roles with veto authority]              | IDENTIFIED |
| Escalation   | [path if no consensus]                   | COMMITTED |

Attendee List (derived from B2; B4 Challenger listed first):

| # | Participant | Role | Tier | Charter Status | Provisional? |
|---|-------------|------|------|----------------|--------------|
| 1 | [B4 Challenger] | [role] | T1 | [function] | [Note if candidate] |
| 2 | [T1 others] | [role] | T1 | [function] | No |
| 3 | [T2] | [role] | T2 | [function] | No |
| 4 | [T3] | [role] | T3 | [function] | No |

PHASE-0-COMMIT: Roster locked from B2. Charter constraints declared as preconditions.
  | ENFORCE: terminal position -- NO PHASE 0 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 1 -- Discussion

Entry: PHASE-0-COMMIT present? [YES / HALT]

VOICE PRODUCTION RULE (structural): Generate ALL T1 entries before writing any T2 entry.
Generate ALL T2 entries before writing any T3 entry. This is a production constraint,
not a style preference. Violation = FAIL C-25.

Discussion grid (in tier order):

| Tier | Participant | Role | STANCE | Inertia Finding (T1 req) / Condition (T2 req) / RESPONDS-TO (T3 req) | Position |
|------|-------------|------|--------|-----------------------------------------------------------------------|----------|
| T1   | [Challenger] | [role] | [B1 token] | INERTIA-FINDING-N: [label] | [concern] |
| T2   | [name] | [role] | [B1 token] | Condition: [explicit stated condition] | [position] |
| T3   | [name] | [role] | [B1 token] | RESPONDS-TO: [T1/T2 entry]; CITE: [source] | [endorsement] |

Voice completeness check:

| Tier | Required Fields | Complete? |
|------|----------------|-----------|
| T1 | STANCE (B1 token) + INERTIA-FINDING-N citation (non-None) | [YES / FAIL] |
| T2 | STANCE (B1 token) + explicit stated condition | [YES / FAIL] |
| T3 | STANCE (B1 token) + CITE reference + RESPONDS-TO pointer | [YES / FAIL] |

FAIL in any row: block progression to PRE-MORTEM CHAIN CHECK until fixed.

PRE-MORTEM CHAIN CHECK:

  CHAIN-1: Challenger: [name/role]
    Status: CONFIRMED / HALT (None = halt, do not proceed to Phase 2)

  CHAIN-2: Outside-in basis: [state the basis]
    Non-circular check: [does this basis derive from internal normalized knowledge?
      IF YES: restate basis using genuine outside-in perspective; internal knowledge fails]
    Status: CONFIRMED / FAIL

  CHAIN-3: Risk draft: [statement]
    Connected to: [INERTIA-FINDING-N -- must be a B3 token]
    Status: CONFIRMED / HALT

TOKEN TRACE MANIFEST (Phase 1→2 gate status):

| Token              | T1 Grid (row?) | CHAIN-3 Draft? | Phase 2 Pre-Mortem (scheduled) | Phase 2 Dissent (scheduled) | GATE STATUS |
|--------------------|---------------|----------------|-------------------------------|----------------------------|-------------|
| INERTIA-FINDING-1  | [row ref]     | [YES/NO]       | PENDING                        | PENDING                    | GATE-CLEARED / NOT-CLEARED |
| INERTIA-FINDING-2  | [row ref]     | [YES/NO]       | PENDING                        | PENDING                    | GATE-CLEARED / NOT-CLEARED |
| INERTIA-FINDING-3  | [row ref]     | [YES/NO]       | PENDING                        | PENDING                    | GATE-CLEARED / NOT-CLEARED |
| INERTIA-FINDING-4  | [row ref]     | [YES/NO]       | PENDING                        | PENDING                    | GATE-CLEARED / NOT-CLEARED |

TRACE GATE: All tokens GATE-CLEARED? [YES / NO -- HALT if NO]
Phase 2 content must expand CHAIN-3 draft; inconsistency = FAIL.

PHASE-1-COMMIT: Voices complete. All chain checkpoints CONFIRMED. TOKEN TRACE MANIFEST
  populated. Gate cleared. Phase 1 closed.
  | ENFORCE: terminal position -- NO PHASE 1 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 2 -- Meeting Minutes

Entry: PHASE-1-COMMIT present? All CHAIN checkpoints CONFIRMED? [YES / HALT]

### Header
Committee: [B1 type]  Date: [date]  Quorum: [MET / NOT MET]
Attendees: [from Phase 0 roster; flag any provisional annotations]

### Agenda Items
[From Phase 0 agenda, with type-gate evidence noted]

### Discussion Summary
[Prose, 2-4 sentences per agenda item; no new positions not in Phase 1 grid]

### Decisions

Outcome tokens must draw from B1 committed vocabulary. No other tokens permitted.

| # | Decision | Outcome Token (from B1) | Conditions | Decided By |
|---|----------|------------------------|------------|------------|
| 1 | [statement] | [B1 token] | [conditions or None] | [role] |

### Action Items

Owner is a structurally required column. Missing Owner = missing cell = FAIL C-04/C-21.

| # | Action | Owner (named role -- required) | Due | Linked Decision |
|---|--------|-------------------------------|-----|-----------------|
| 1 | [action] | [named owner] | [date/TBD] | [#] |

### Dissenting Opinions

Per-participant rows required. Missing row = FAIL C-05/C-22.
Each dissent entry must cite an inertia token. No-dissent entries must state why the
inertia concern was resolved. Absent justification = FAIL C-27.

| Participant | Role | Dissent | Inertia Token | Justification |
|-------------|------|---------|---------------|---------------|
| [name] | [role] | [dissent / No dissent] | [INERTIA-FINDING-N or resolved] | [persists because... / resolved by...] |

### Pre-Mortem Risk

(Must expand CHAIN-3 draft from Phase 1. Inconsistency between CHAIN-3 and this
section = FAIL.)

Risk: [expanded from CHAIN-3 draft]
Inertia basis: [INERTIA-FINDING-N label]
Challenger: [name/role]
Why the real committee will miss this: [specific organizational normalization, not generic concern]

---

### TOKEN TRACE CONFIRMATION

This section actively re-validates each inertia token at Phase 2 output.
This is distinct from the Phase 1 TRACE GATE (which ensures tokens entered Phase 2).
This CONFIRMATION ensures tokens survived to Phase 2 final output.

| Token              | Pre-Mortem Entry? | Dissent Row Cited? | Decision Ref? | CONFIRMATION STATUS |
|--------------------|------------------|--------------------|---------------|---------------------|
| INERTIA-FINDING-1  | [YES + ref / NO] | [YES + row / NO]  | [YES/NO/N/A]  | CONFIRMED / DROPOUT |
| INERTIA-FINDING-2  | [YES + ref / NO] | [YES + row / NO]  | [YES/NO/N/A]  | CONFIRMED / DROPOUT |
| INERTIA-FINDING-3  | [YES + ref / NO] | [YES + row / NO]  | [YES/NO/N/A]  | CONFIRMED / DROPOUT |
| INERTIA-FINDING-4  | [YES + ref / NO] | [YES + row / NO]  | [YES/NO/N/A]  | CONFIRMED / DROPOUT |

Cross-reference with Phase 1 TOKEN TRACE MANIFEST:
  Tokens that were GATE-CLEARED in Phase 1 and are DROPOUT here = gate-cleared dropout.
  This is the most critical failure mode -- the token survived the gate but dropped
  before reaching Phase 2 output. Must be repaired before delivering minutes.

DROPOUT REPAIR RULE: Any DROPOUT = return to the dropout site and add the missing citation.
Do not deliver Phase 2 output with any DROPOUT row in this table.

### Next Steps
[Follow-up meetings, escalations, dependencies]

PHASE-2-COMMIT: All sections present. TOKEN TRACE CONFIRMATION complete with no DROPOUT.
  Simulation complete.
  | ENFORCE: terminal position -- NO PHASE 2 CONTENT MAY FOLLOW THIS LINE.

---

## AMEND Handling

Classify the amendment → identify blocks invalidated → emit AMEND-AFFECTED SITES block
before re-execution → re-run invalidated blocks → emit new COMMIT seals → resume phases.

Block re-execution routing:
  Composition change: B2 → B4 → Phase 0+
  Type change: B1 → B2 → all phases
  Scope change: Phase 0 charter constraints → Phase 0+
  Agenda item addition: Phase 1+

TOKEN TRACE CONFIRMATION must be re-executed in Phase 2 whenever inertia tokens or
dissent rows are affected by the amendment.
```

---

## V-05 -- Full Integration (C-31 + C-32 + C-33 + best of R9)

**Axis:** Full integration of C-31, C-32, C-33 plus the complete R9 best architecture
**Hypothesis:** Per-block COMMIT seals (C-31), Phase 2 TOKEN TRACE CONFIRMATION (C-32),
and AMEND-AFFECTED SITES notation (C-33) each address a distinct structural gap in the
end-to-end audit chain. When integrated with the R9 best architecture -- BLOCK DEPENDENCY MAP
(C-28), TOKEN TRACE MANIFEST at the Phase 1→2 gate (C-29), AMEND block routing table
(C-30), vocabulary contract (C-24), tier-sequenced voice production (C-25), per-tier
column grammar (C-26), inertia token anchoring in dissent (C-27), standalone Challenger
block (C-23) -- the result is a complete skill where: every block's output is explicitly
sealed before citation (C-31), every token's survival to Phase 2 output is actively
re-validated (C-32), every amendment's impact is visible as a staleness manifest before
re-execution (C-33), and all upstream R9 structural guarantees remain intact. No single
criterion is satisfied by relying on another; each mechanism closes its own window.

```
You are running /corps-committee.

Simulate the committee meeting before it happens. Types: ROB (product/service review),
shiproom (go/no-go), arch-board (architecture decision review). Read participant charters
from .craft/roles/. Output: mock meeting minutes with decisions, action items, dissenting
opinions. AMEND: add attendees, change scope.

---

## BEFORE YOU START

Type-specific primary obligations. These are fail conditions, not style preferences.

ROB -- Product or Service Review:
  Obligation: Readiness verdict backed by specific metric evidence.
  FAIL: No metric in output = you have not done a ROB.
  FAIL: Generic approval without metric evidence = C-07 partial.

SHIPROOM -- Go / No-Go:
  Obligation: Binary GO / NO-GO decision with a risk register and blocking condition.
  FAIL: No GO or NO-GO decision line = you have not done a shiproom.
  FAIL: GO without a risk register = C-07 partial.

ARCH-BOARD -- Architecture Decision Review:
  Obligation: Named architectural trade-offs with a selected alternative and stated consequence.
  FAIL: No named trade-offs = you have not done an arch-board.
  FAIL: Single option presented = C-07 partial.

COMMON FAIL: Any participant speaking from the wrong role (PM raises deployment topology
as primary; SRE leads product vision) = FAIL C-02. Check role assignments before proceeding.

---

## BLOCK DEPENDENCY MAP

Declares inter-block consumption obligations before any block executes.
Blocks form an interdependent system -- not an independent checklist.

| Block | Label                  | Consumes From | Required Input                                   |
|-------|------------------------|---------------|--------------------------------------------------|
| B1    | Vocabulary Contract    | (origin)      | (none)                                           |
| B3    | Inertia Inventory      | (origin)      | (none -- runs before B2 to supply tokens)        |
| B2    | Tier Pre-Assignment    | B1            | Vocabulary tokens -- STANCE labels draw from B1  |
| B2    | Tier Pre-Assignment    | B3            | T1 Inertia Citation -- must name a B3 token      |
| B4    | Challenger Designation | B2            | Tier 1 assignment -- must match a B2 T1 entry    |
| B4    | Challenger Designation | B3            | NORM label obligation -- must be a B3 token      |

Cross-block consistency obligations:
  B4 Challenger tier must match a Tier 1 entry committed in B2. FAIL if mismatch.
  B2 T1 Inertia Citation must reference a token that exists in B3. FAIL if absent from B3.
  B1 vocabulary tokens must be consumed by B2 STANCE labels. FAIL if B2 uses unlisted tokens.

DEPENDENCY RULE: No block may execute until all upstream COMMIT seals are present.
Citation of a block's tokens before that block's COMMIT seal is emitted = FAIL C-31.

---

### B1 -- Vocabulary Contract

State the committee type. Commit the outcome vocabulary for this type.

Committee Type: [ROB / SHIPROOM / ARCH-BOARD]

Vocabulary table:
  ROB:        APPROVED | APPROVED WITH CONDITIONS | BLOCKED | DEFERRED
  SHIPROOM:   GO | NO-GO | HOLD
  ARCH-BOARD: ACCEPTED | REJECTED | DEFERRED

Active tokens for this simulation: [list for declared type only]

Downstream consumption obligations:
  B2 STANCE-from-B1 column: must draw from this set.
  Phase 1 discussion grid STANCE column: must draw from this set.
  Phase 2 Decisions Outcome Token column: must draw from this set.

B1-COMMIT: Type: [type] | Vocabulary: [committed tokens] | Sealed.
  B2 and all phases may now cite B1 tokens.
  Citation of B1 tokens before this COMMIT = FAIL C-31.

---

### B3 -- Inertia Inventory (executes before B2; B2 consumes B3 tokens)

State the inertia hypothesis: What will the real committee rubber-stamp without challenge?

Then decompose into four named findings -- not category headings. Each finding names
an observable organizational behavior or prior decision.

INERTIA-FINDING-1: [specific workflow or tool in production that this agenda item displaces]
INERTIA-FINDING-2: [specific integration surface at risk; name systems, APIs, or contracts]
INERTIA-FINDING-3: [team whose cognitive habit would break; name the team and the habit]
INERTIA-FINDING-4: [non-obvious switching cost the proposal author did not account for]

Gate: Does INERTIA-FINDING-4 reveal a non-obvious cost the proposal author would not
have anticipated?
IF NO: rewrite all four findings. Retry until YES.

INERTIA RECORD (sealed):
| Token              | One-Phrase Anchor                         |
|--------------------|-------------------------------------------|
| INERTIA-FINDING-1  | [anchor]                                  |
| INERTIA-FINDING-2  | [anchor]                                  |
| INERTIA-FINDING-3  | [anchor]                                  |
| INERTIA-FINDING-4  | [anchor]                                  |

INERTIA INVARIANT: sealed at B3-COMMIT -- findings may not be added, removed, or modified
  without reopening B3. Modifications to INERTIA RECORD require updating B3-COMMIT;
  modifications to B3-COMMIT require updating INERTIA RECORD. Bilateral contract.

Downstream consumption obligations:
  B2: T1 Inertia Citation column cites B3 tokens.
  B4: NORM label obligation cites a B3 token.
  Phase 1 T1 voice entries: Inertia Finding cell cites B3 tokens.
  Phase 1 CHAIN-3: risk draft connects to a B3 token.
  Phase 2 pre-mortem: Inertia basis cites a B3 token.
  Phase 2 dissent: Inertia Token column cites B3 tokens.
  Phase 2 TOKEN TRACE CONFIRMATION: re-validates each B3 token.

B3-COMMIT: Inventory sealed. INERTIA-FINDING-1 through INERTIA-FINDING-4 available.
  B2 and B4 may now cite these tokens.
  Citation of B3 tokens before this COMMIT = FAIL C-31.

---

### B2 -- Tier Pre-Assignment (consumes B1 + B3)

Entry check: B1-COMMIT present? [YES / HALT]  B3-COMMIT present? [YES / HALT]

Assign each participant a voice tier.

Tier 1 -- Challenger: voices concern against dominant position; outside-in obligation.
  Required fields: STANCE-from-B1 token + Inertia Citation (must be a B3 token, non-None)
Tier 2 -- Conditional: conditional support on stated conditions.
  Required fields: STANCE-from-B1 token + explicit stated condition (not "address concerns")
Tier 3 -- Advocate: supports proposal; responds to prior concerns.
  Required fields: STANCE-from-B1 token + RESPONDS-TO pointer + CITE reference

| Participant | Role | Tier | STANCE-from-B1 | Inertia Citation (T1 only) | Obligation / Condition |
|-------------|------|------|----------------|---------------------------|------------------------|
| [name] | [role] | T1 | [B1 token] | [INERTIA-FINDING-N from B3] | [what this frame challenges] |
| [name] | [role] | T2 | [B1 token] | -- | Condition: [explicit] |
| [name] | [role] | T3 | [B1 token] | -- | RESPONDS-TO: [T1/T2]; CITE: [source] |

B2 cross-block integrity check:
  STANCE-from-B1 tokens all from B1 committed vocabulary? [YES / NO -- fix if NO]
  T1 Inertia Citations all present in B3 INERTIA RECORD? [YES / NO -- fix if NO]

Ordering constraint (structural production rule, not style preference):
  All Tier 1 voices are generated before any Tier 2 voice is written.
  All Tier 2 voices are generated before any Tier 3 voice is written.
  A T3 Advocate appearing before a T1 Challenger concern exists = FAIL C-25.

B2-COMMIT: Tier assignments sealed. B1 consumed. B3 tokens cited.
  Ordering constraint committed.
  B4 and Phase 0 may now cite tier assignments.
  Citation of tier assignments before this COMMIT = FAIL C-31.

---

### B4 -- Designated Inertia Challenger

This block renders as a structurally isolated, standalone element before Phase 0.
It is NOT embedded in Phase 0 roster construction.
The Challenger identity is visible to the reader before roster construction begins.

Entry check: B2-COMMIT present? [YES / HALT]  B3-COMMIT present? [YES / HALT]

Designate one participant as the Inertia Challenger. Choose the participant whose
perspective is LEAST likely to reflect the normalized organizational assumptions.

DESIGNATED INERTIA CHALLENGER:
  Role: [role name]
  Tier: [T1 -- verified against B2; if not T1 in B2, HALT and fix B2 before proceeding]
  B2 Tier 1 match: [YES / FAIL -- must be YES]
  Outside-in rationale: [why this specific frame is least normalized; must be specific,
    not generic ("experienced in X" is generic; "their client base operates outside our
    stack and evaluates from switching-cost exposure" is specific)]
  NORM label obligation: [INERTIA-FINDING-N from B3 -- must exist in B3 INERTIA RECORD]
  B3 token exists: [YES / FAIL -- must be YES]

If no qualifying participant exists:
  [Note: [role] is a candidate Inertia Challenger -- confirmed or replaced in Phase 2]

B4-COMMIT: Challenger designated. B2 Tier 1 confirmed. B3 NORM obligation assigned.
  Phase 0 may now begin.
  Simulation content generated before this COMMIT = FAIL C-31.

---

## PHASE 0 -- Roster and Charter Preconditions

Entry: B1-COMMIT present? [YES]  B2-COMMIT? [YES]  B3-COMMIT? [YES]  B4-COMMIT? [YES]
Any missing: HALT. Return to the missing block. Do not proceed.

Charter constraints (phase entry preconditions -- declared before simulation begins):

| Constraint   | Charter Requirement                      | Status       |
|--------------|------------------------------------------|--------------|
| Quorum       | [N roles required / N present]           | MET / UNMET  |
| Scope        | [what is in-scope / what is out-of-scope] | DECLARED     |
| Veto holders | [role(s) with veto authority]            | IDENTIFIED   |
| Escalation   | [path if consensus is not reached]       | COMMITTED    |

Test: can Phase 1 simulation begin without these constraints having been stated?
IF YES: this criterion is not met. Declare constraints before proceeding.

Attendee List (derived from B2 tier assignments; B4 Challenger listed first):

| # | Participant | Role | Tier | Charter Function | Provisional? |
|---|-------------|------|------|------------------|--------------|
| 1 | [B4 Challenger] | [role] | T1 | [function in committee] | [Note if candidate: role is a candidate participant -- confirmed or replaced in Phase 2] |
| 2 | [other T1 if any] | [role] | T1 | [function] | No |
| 3 | [T2] | [role] | T2 | [function] | No |
| 4 | [T3] | [role] | T3 | [function] | No |

PHASE-0-COMMIT: Roster locked from B2. Charter constraints declared as entry preconditions.
  All block COMMITs (B1, B2, B3, B4) verified present.
  | ENFORCE: terminal position -- NO PHASE 0 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 1 -- Discussion Simulation

Entry: PHASE-0-COMMIT present? [YES / HALT]

VOICE PRODUCTION RULE (structural constraint, not style preference):
Generate ALL Tier 1 entries completely before writing any Tier 2 entry.
Generate ALL Tier 2 entries completely before writing any Tier 3 entry.
A T3 voice appearing before a T1 Challenger concern has been stated in the grid = FAIL C-25.

Discussion grid (in tier order -- T1 complete, then T2 complete, then T3):

| Tier | Participant | Role | STANCE | Inertia Finding (T1) / Condition (T2) / RESPONDS-TO (T3) | Key Position |
|------|-------------|------|--------|------------------------------------------------------------|--------------|
| T1   | [Challenger] | [role] | [B1 token] | [INERTIA-FINDING-N -- required; None = structural gap] | [specific concern] |
| T1   | [other T1]  | [role] | [B1 token] | [INERTIA-FINDING-N or N/A if non-Challenger T1] | [concern] |
| T2   | [name] | [role] | [B1 token] | Condition: [explicit stated condition -- "address concerns" fails] | [conditional position] |
| T3   | [name] | [role] | [B1 token] | RESPONDS-TO: [T1/T2 entry by name]; CITE: [source or prior concern] | [endorsement] |

Voice completeness check (per tier -- not per discussion):

| Tier | Required Fields | Complete? |
|------|----------------|-----------|
| T1 -- Challenger | STANCE (B1 token) + INERTIA-FINDING-N citation (non-None) | [YES / FAIL] |
| T2 -- Conditional | STANCE (B1 token) + explicit stated condition | [YES / FAIL] |
| T3 -- Advocate | STANCE (B1 token) + CITE reference + RESPONDS-TO pointer | [YES / FAIL] |

FAIL in any row: block progression to PRE-MORTEM CHAIN CHECK. Fix the failing cell first.

PRE-MORTEM CHAIN CHECK:

  CHAIN-1 -- Challenger identified:
    Challenger: [name/role]
    Status: CONFIRMED / HALT (if None, halt -- do not proceed to Phase 2)

  CHAIN-2 -- Outside-in basis stated:
    Basis: [specific outside-in framing]
    Non-circular check: does this basis derive from internal normalized knowledge?
      [If YES: restate using genuine outside perspective; circular basis fails]
    Status: CONFIRMED / FAIL

  CHAIN-3 -- Risk draft connected to inertia assumption:
    Risk: [draft risk statement]
    Connected to: [INERTIA-FINDING-N -- must be a token from B3 INERTIA RECORD]
    Status: CONFIRMED / HALT (if no B3 token, halt)

TOKEN TRACE MANIFEST (Phase 1→2 gate):
Tracks each inertia token from B3 through Phase 2 consumption sites.
Phase 2 must consume each token; TOKEN TRACE CONFIRMATION in Phase 2 will re-validate.

| Token              | T1 Grid Row? | CHAIN-3? | Phase 2 Pre-Mortem (scheduled) | Phase 2 Dissent (scheduled) | GATE STATUS |
|--------------------|-------------|----------|-------------------------------|----------------------------|-------------|
| INERTIA-FINDING-1  | [row ref]   | [YES/NO] | PENDING                        | PENDING                    | GATE-CLEARED / NOT-CLEARED |
| INERTIA-FINDING-2  | [row ref]   | [YES/NO] | PENDING                        | PENDING                    | GATE-CLEARED / NOT-CLEARED |
| INERTIA-FINDING-3  | [row ref]   | [YES/NO] | PENDING                        | PENDING                    | GATE-CLEARED / NOT-CLEARED |
| INERTIA-FINDING-4  | [row ref]   | [YES/NO] | PENDING                        | PENDING                    | GATE-CLEARED / NOT-CLEARED |

TRACE GATE: All CHAIN checkpoints CONFIRMED AND all tokens GATE-CLEARED?
[YES -- proceed to Phase 2 / NO -- halt and fix before proceeding]
Phase 2 pre-mortem must expand the CHAIN-3 draft.
Inconsistency between CHAIN-3 risk and Phase 2 pre-mortem expansion = FAIL.

PHASE-1-COMMIT: Discussion complete. Chain checkpoints all CONFIRMED. TOKEN TRACE MANIFEST
  populated and gate cleared. Phase 1 closed.
  | ENFORCE: terminal position -- NO PHASE 1 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 2 -- Meeting Minutes

Entry: PHASE-1-COMMIT present? All CHAIN checkpoints CONFIRMED? All tokens GATE-CLEARED?
[YES / HALT if any NO]

### Header
Committee: [B1 type]
Date: [date]
Attendees: [from Phase 0 roster -- note any provisional annotations]
Quorum: [MET / NOT MET -- if UNMET, note impact on decision validity]

### Agenda Items
[Agenda items from Phase 0; note type-gate evidence status for each item]

### Discussion Summary
[Prose summary, 2-4 sentences per agenda item. No new positions introduced here.
All positions derive from Phase 1 discussion grid.]

### Decisions

Outcome tokens must draw from B1 committed vocabulary. Tokens not in B1 = FAIL C-01/C-24.

| # | Decision | Outcome Token (from B1) | Conditions (if any) | Decided By |
|---|----------|------------------------|---------------------|------------|
| 1 | [decision statement] | [B1 token] | [specific conditions or None] | [role] |

Verdict: [matching the tally from Phase 1 stances]

### Action Items

Owner is a structurally required column. Missing Owner = missing cell = FAIL C-04/C-21.
Action items without owners are not valid. Vague conditions are not valid.

| # | Action | Owner (named role -- required, not a team) | Due | Linked Decision # |
|---|--------|-------------------------------------------|-----|-------------------|
| 1 | [specific action] | [named role] | [date or TBD] | [#] |

### Dissenting Opinions

Per-participant rows required for any participant who could plausibly dissent.
Missing row = FAIL C-05/C-22.
Each dissent entry must cite an inertia token by label = FAIL C-27 if absent.
No-dissent entries must state the inertia concern and explain how it was resolved.

| Participant | Role | Dissent or Position | Inertia Token (INERTIA-FINDING-N or resolved) | Inertia Linkage Justification |
|-------------|------|---------------------|-----------------------------------------------|-------------------------------|
| [name] | [role] | [dissent stated / No dissent] | [INERTIA-FINDING-N or "resolved: INERTIA-FINDING-N"] | [why this concern persists or how it was resolved] |

### Pre-Mortem Risk

(Must expand CHAIN-3 draft from Phase 1. If this section contradicts CHAIN-3, that is a FAIL.)

Risk: [expanded from CHAIN-3]
Inertia basis: [INERTIA-FINDING-N label from B3]
Challenger: [name/role]
Why the real committee will miss this: [specific organizational normalization -- the reason
  this concern has been made invisible by prior decisions or standing assumptions; not a
  generic forward-looking concern]

### TOKEN TRACE CONFIRMATION

This section actively re-validates each inertia token's presence in Phase 2 output.
This is NOT a consequence of the Phase 1 TRACE GATE; it is a Phase 2 output-layer assertion.

The TRACE GATE ensures each token entered Phase 2 with a committed chain (C-19/C-29).
This CONFIRMATION ensures each token survived to Phase 2 final output (C-32).
A token that was GATE-CLEARED in Phase 1 and is DROPOUT here has cleared the gate
but failed to reach output -- the most critical failure mode this section exists to detect.

| Token              | Phase 2 Pre-Mortem (cited?) | Phase 2 Dissent Row (cited?) | Phase 2 Decision (referenced?) | CONFIRMATION STATUS |
|--------------------|----------------------------|-----------------------------|--------------------------------|---------------------|
| INERTIA-FINDING-1  | [YES + specific ref / NO]  | [YES + row participant / NO] | [YES / NO / N/A]               | CONFIRMED / DROPOUT |
| INERTIA-FINDING-2  | [YES + ref / NO]           | [YES + row / NO]            | [YES / NO / N/A]               | CONFIRMED / DROPOUT |
| INERTIA-FINDING-3  | [YES + ref / NO]           | [YES + row / NO]            | [YES / NO / N/A]               | CONFIRMED / DROPOUT |
| INERTIA-FINDING-4  | [YES + ref / NO]           | [YES + row / NO]            | [YES / NO / N/A]               | CONFIRMED / DROPOUT |

Cross-reference: compare this table against Phase 1 TOKEN TRACE MANIFEST.
  Any token GATE-CLEARED in Phase 1 and DROPOUT here = gate-cleared dropout = highest severity.
  Any token NOT GATE-CLEARED in Phase 1 and present here = unexpected token = verify label.

DROPOUT REPAIR: Any DROPOUT row = Phase 2 output is incomplete.
Return to the dropout site (pre-mortem or dissent row), add the missing token citation,
then re-run this CONFIRMATION table. Do not deliver minutes with any DROPOUT row.

### Next Steps
[Follow-up meetings, escalations, or dependencies. Include re-entry triggers if verdict is not APPROVED/GO/ACCEPTED.]

PHASE-2-COMMIT: All sections present. TOKEN TRACE CONFIRMATION complete with all tokens
  CONFIRMED. Simulation complete.
  | ENFORCE: terminal position -- NO PHASE 2 CONTENT MAY FOLLOW THIS LINE.

---

## AMEND Handling

AMEND triggers a three-step process. Re-execution does not begin until all three steps
are complete.

### AMEND ROUTING TABLE

Amendment scope is determined by which pre-execution blocks the amendment touches,
not by which phases are affected.

| Amendment Type | Pre-Execution Blocks Invalidated | Re-run Order |
|---------------|----------------------------------|--------------|
| Participant composition change | B2 (tier assignments), B4 (Challenger designation) | B2 → B4 → Phase 0 → Phase 1 → Phase 2 |
| Committee type change | B1 (vocabulary contract), B2 (STANCE tokens) | B1 → B2 → all phases |
| Scope change | Phase 0 charter constraints | Phase 0 charter section → Phase 1 → Phase 2 |
| New agenda item | Phase 1 only | Phase 1 → Phase 2 |
| Challenger role removed | B4 only | B4 → Phase 0 roster → Phase 1 → Phase 2 |
| Inertia finding correction | B3 (inventory) | B3 → B2 (if T1 citation changes) → B4 (if NORM changes) → all phases |

### AMEND-AFFECTED SITES (emit BEFORE any re-execution begins)

List every output element rendered stale by the amendment, by structural reference
and the token or assignment affected. This makes amendment impact visible at the
artifact layer before a single phase re-executes.

Format:
```
AMEND-AFFECTED SITES:
Amendment: [describe the change precisely]
Amendment type: [from AMEND ROUTING TABLE]
Blocks invalidated: [B1 / B2 / B3 / B4 -- list only those invalidated]

Stale output elements:
  [block ID or phase + section] -- [element name] -- STALE: [reason] -- Re-run: [action]
  [block ID or phase + section] -- [element name] -- STALE: [reason] -- Re-run: [action]
```

Examples:

Composition change (participant added):
  B2 Tier Assignment table -- new participant row absent -- STALE: composition change -- Re-run B2
  B4 Challenger Designation -- STALE: new T1 candidate may qualify; re-designation required -- Re-run B4
  Phase 0 Attendee List -- STALE: B2 not yet re-committed; shows pre-amendment roster -- Re-run Phase 0
  Phase 1 Discussion Grid -- STALE: new participant voice absent -- Re-run Phase 1
  Phase 2 Action Items -- STALE: owner table may change -- Re-run Phase 2
  Phase 2 Dissenting Opinions -- STALE: new participant row absent -- Re-run Phase 2
  Phase 2 TOKEN TRACE CONFIRMATION -- STALE: dissent rows changed -- Re-run CONFIRMATION

Committee type change (ROB → SHIPROOM):
  B1 Vocabulary Contract -- STALE: type changed; APPROVED/BLOCKED no longer valid -- Re-run B1
  B2 STANCE-from-B1 column -- STALE: B1 tokens changed; all STANCE cells invalid -- Re-run B2
  Phase 1 Discussion Grid STANCE column -- STALE: B2 not re-committed -- Re-run Phase 1
  Phase 2 Decisions Outcome Token column -- STALE: B1 vocabulary changed -- Re-run Phase 2

RULE: An AMEND that re-executes without first emitting this block = FAIL C-33.
RULE: An AMEND-AFFECTED SITES block that names phases without naming specific elements
  (e.g., "Phase 2 is stale" without specifying which rows or columns are stale) = incomplete
  staleness manifest = FAIL C-33.

### Re-Execution

After AMEND-AFFECTED SITES is complete:

1. Re-run invalidated pre-execution blocks in routing order.
2. Emit updated COMMIT seals for each re-run block.
3. Resume phases from the first affected phase.
4. Re-run TOKEN TRACE CONFIRMATION in Phase 2 whenever inertia tokens or dissent rows
   are affected.
5. Verify no new DROPOUT rows in the CONFIRMATION table.
```
