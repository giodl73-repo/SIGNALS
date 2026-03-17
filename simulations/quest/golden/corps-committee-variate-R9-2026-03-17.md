---
skill: quest-variate
skill_target: corps-committee
date: 2026-03-17
round: 9
rubric_version: 9
---

# corps-committee -- Prompt Variations R9

## Variation Summary

| ID   | Axis                                                                                   | Hypothesis |
|------|----------------------------------------------------------------------------------------|------------|
| V-01 | Cross-block dependency graph (C-28)                                                   | Declaring explicit inter-block consumption obligations in a BLOCK DEPENDENCY MAP before any block executes — Block 4 Challenger tier must match a Tier 1 entry in Block 2; Block 2 T1 Inertia Citation must reference a token that exists in Block 3; Block 1 vocabulary consumed by Block 2 STANCE labels — closes C-28 structurally: a reviewer can verify each inter-block contract by label without reading prose. |
| V-02 | End-to-end token trace (C-29)                                                         | Adding a TOKEN TRACE MANIFEST at the Phase 1→2 gate that tracks each INERTIA-FINDING-N through every downstream consumption site — T1 Inertia Citation, CHAIN-3 draft, Phase 2 pre-mortem expansion, Dissent Collection Inertia Token, Dissenting Opinions Inertia Token — closes C-29: any link in the chain that drops a token is a missing cell, auditable by label comparison without reading prose. |
| V-03 | AMEND block-level routing (C-30)                                                      | Adding an AMEND ROUTING TABLE that maps each amendment type (participant composition change, committee type change, scope change) to the specific pre-execution blocks that must be re-run before phase re-execution begins, closes C-30: AMEND scope is determined by block dependency, not phase impact. An amendment that changes participants must re-run Block 2 + Block 4 before Phase 0 re-execution; a type change must re-run Block 1 + Block 2. |
| V-04 | Combination: C-28 + C-29 (block graph + token trace as integrated audit system)      | Combining cross-block dependency declarations with end-to-end token trace creates a self-auditing system: Block 3 originates each INERTIA-FINDING-N token; Block 2 declares a consumption obligation that must reference it; Block 4 validates against Block 2; the TOKEN TRACE MANIFEST at the Phase 1→2 gate then tracks each token through all downstream sites. Any broken link is detectable at the block level before simulation begins or at the gate level before Phase 2 begins. |
| V-05 | Full integration: C-28 + C-29 + C-30 + R8 vocabulary/tier/dissent architecture      | Combining the block dependency graph (C-28), end-to-end token trace (C-29), and AMEND block routing (C-30) with the R8 best architecture — vocabulary contract (C-24), tier-sequenced voice (C-25), per-tier column grammar (C-26), inertia token anchoring in dissent (C-27), Designated Challenger block (C-23), table-first structural grammar (C-16/C-21/C-22) — produces a fully integrated skill where every structural obligation is cross-referenced, every token is traceable, and every amendment is routed through the correct block re-execution path. |

---

## V-01 -- Cross-Block Dependency Graph

**Axis:** Cross-block dependency graph (C-28)
**Hypothesis:** Declaring explicit inter-block consumption obligations before any block executes —
each block states which blocks it consumes and what token or commitment it expects from them —
closes C-28 structurally: a reviewer can verify inter-block consistency by label comparison rather
than prose reading. Block 4 Challenger tier must match a Tier 1 entry committed in Block 2; Block
2 T1 Inertia Citation obligation must reference a token that exists in Block 3; Block 1 vocabulary
tokens must appear in Block 2 STANCE labels. The test: can any block begin without its declared
inputs having been committed? If yes, the dependency graph is not enforced.

```
You are running /corps-committee.

Simulate the committee meeting before it happens. Produce mock meeting minutes.

---

## BLOCK DEPENDENCY MAP

Before any block executes, declare the dependency structure. This map is checked at each block
entry. Blocks may not execute until all listed inputs are available.

| Block | Label                     | Consumes From | Required Input |
|-------|---------------------------|---------------|----------------|
| B1    | Vocabulary Contract       | (none)        | (origin block) |
| B2    | Tier Pre-Assignment       | B1            | Outcome vocabulary tokens — STANCE labels in B2 must draw from B1 |
| B2    | Tier Pre-Assignment       | B3            | T1 Inertia Citation obligation — at least one INERTIA-FINDING-* label from B3 must be named as the T1 citation target |
| B3    | Inertia Inventory         | (none)        | (origin block — inventories named before any tier assignment) |
| B4    | Challenger Designation    | B2            | Challenger tier assignment — B4 Challenger must match a Tier 1 entry committed in B2 |
| B4    | Challenger Designation    | B3            | NORM label obligation — B4 Challenger's NORM label must exist in B3 inventory |

FAILS: any block executes before its declared inputs are present -- C-28 fail.
FAILS: Block 4 Challenger tier does not match a Tier 1 entry in Block 2 -- C-28 fail.
FAILS: Block 2 T1 Inertia Citation does not reference a token present in Block 3 -- C-28 fail.
FAILS: Block 1 vocabulary tokens absent from Block 2 STANCE labels -- C-28 partial.

---

## BLOCK 1 -- Vocabulary Contract

State your committee type. Commit its outcome vocabulary. All downstream tokens draw from here.

**ROB (Product Review / Service Review)**
Primary obligation: A readiness verdict backed by metric evidence.
Fail condition: No metric in output = ROB not done.
OUTCOME VOCABULARY: APPROVED | APPROVED WITH CONDITIONS | BLOCKED | DEFERRED

**SHIPROOM (Go / No-Go)**
Primary obligation: A binary GO or NO-GO decision backed by a risk register.
Fail condition: No GO or NO-GO decision line = shiproom not done.
OUTCOME VOCABULARY: GO | NO-GO | HOLD

**ARCH-BOARD (Architecture Decision Review)**
Primary obligation: An ADR with named trade-offs and a selected alternative.
Fail condition: No ADR or no selected winner = arch-board not done.
OUTCOME VOCABULARY: ACCEPTED | REJECTED | DEFERRED

Write now:
> B1-COMMIT: [ROB / SHIPROOM / ARCH-BOARD] | Topic: [topic] | Vocabulary: [committed tokens]

FAILS: B1-COMMIT absent -- C-24 fail.
FAILS: vocabulary committed but not consumed by B2 STANCE labels -- C-28 partial.

---

## BLOCK 3 -- Inertia Inventory

(Block 3 executes before Block 2 because Block 2 consumes Block 3 tokens.)

Investigate what is already in place and at risk. Produce four named findings.

INERTIA-FINDING-1: [specific workflow or tool in production this agenda item displaces]
INERTIA-FINDING-2: [specific integration surface at risk — name systems, APIs, or contracts]
INERTIA-FINDING-3: [team whose cognitive habit would break and the specific habit]
INERTIA-FINDING-4: [non-obvious switching cost the proposal author did not account for]

GATE: Does INERTIA-FINDING-4 reveal a cost the proposal author would not have anticipated?
IF NO: rewrite all four findings. Repeat until YES.

INERTIA RECORD (sealed):
| Token            | One-Phrase Anchor |
|------------------|-------------------|
| INERTIA-FINDING-1 | [anchor]         |
| INERTIA-FINDING-2 | [anchor]         |
| INERTIA-FINDING-3 | [anchor]         |
| INERTIA-FINDING-4 | [anchor]         |

B3-COMMIT: Inventory sealed. Tokens available for B2 and B4 consumption.

FAILS: any INERTIA-FINDING-* token absent from this table -- B2 and B4 have no valid citation target.
FAILS: B3-COMMIT absent -- inventory not sealed; downstream blocks cannot verify inputs.

---

## BLOCK 2 -- Tier Pre-Assignment

(Executes after B1 and B3 are committed. Consumes: B1 vocabulary tokens for STANCE labels;
B3 tokens for T1 Inertia Citation obligation.)

Assign every participant to a voice tier before Phase 0 roster is built.

| Participant | Role | Tier | STANCE-from-B1 | Inertia Citation (T1 only) | Rationale |
|-------------|------|------|-----------------|---------------------------|-----------|
| [name]      | [role] | T1 | [B1 token]    | [INERTIA-FINDING-N from B3] | [why this frame is challenger] |
| [name]      | [role] | T2 | [B1 token]    | --                          | [conditional condition] |
| [name]      | [role] | T3 | [B1 token]    | --                          | [why advocate] |

B2 CROSS-BLOCK CHECK:
- STANCE-from-B1 column: every token drawn from B1-COMMIT vocabulary? [YES / NO]
- T1 Inertia Citation: every T1 entry cites a token present in B3 INERTIA RECORD? [YES / NO]

IF either check NO: halt. Fix the failing cell before continuing.

B2-COMMIT: Tiers assigned. B1 vocabulary consumed. B3 tokens cited. Available for B4 consumption.

FAILS: STANCE-from-B1 column contains tokens not in B1 vocabulary -- C-28 fail, C-24 fail.
FAILS: T1 Inertia Citation cites a token not in B3 INERTIA RECORD -- C-28 fail.
FAILS: B2 cross-block check absent -- C-28 fail.

---

## BLOCK 4 -- Designated Inertia Challenger

(Executes after B2 and B3 are committed. Consumes: B2 Tier 1 entries; B3 inventory tokens.)

Designate one participant as the Inertia Challenger before Phase 0 begins.

CHALLENGER DESIGNATION:
- Role: [role name]
- B2 Tier: [must be Tier 1 — verified against B2 roster]
- Outside-in rationale: [why their frame is least likely to reflect the normalized assumption]
- NORM label obligation: [INERTIA-FINDING-N from B3 — this token is their required Phase 1 citation]

B4 CROSS-BLOCK CHECK:
- Challenger tier matches a Tier 1 entry in B2? [YES / NO]
- NORM label obligation exists in B3 INERTIA RECORD? [YES / NO]

IF either check NO: halt. Fix before continuing.

B4-COMMIT: Challenger designated. B2 tier confirmed. B3 token obligation assigned.

FAILS: B4 Challenger tier does not match a B2 Tier 1 entry -- C-28 fail, C-20 fail.
FAILS: NORM label not present in B3 INERTIA RECORD -- C-28 fail, C-18 fail.
FAILS: B4 cross-block check absent -- C-28 fail.

---

## PHASE 0 -- Roster and Agenda

(Enters after B1, B2, B3, B4 all committed. Roster drawn from B2 tier assignments.)

Participant Roster (ordered by tier from B2):

| Seq | Participant | Role | Tier | Charter Status |
|-----|-------------|------|------|----------------|
| 1   | [B4 Challenger] | [role] | T1 | [Standing / Candidate: function] |
| 2   | [T1 others] | [role] | T1 | [Standing] |
| 3   | [T2 participants] | [role] | T2 | [Standing] |
| 4   | [T3 participants] | [role] | T3 | [Standing] |

Agenda (type-specific):

| # | Agenda Item | Type Gate | Evidence Required |
|---|-------------|-----------|-------------------|
| 1 | [item]      | [pass/fail condition from B1 obligation] | [what must be present] |

Charter Constraints:

| Constraint | Charter Requirement | Must Honor |
|------------|---------------------|------------|
| Quorum     | [from .craft/roles/] | Yes        |
| Veto       | [veto holder]        | Yes        |

PHASE-0-COMMIT: Roster locked from B2. All blocks committed.

---

## PHASE 1 -- Simulation (Tier 1 → Tier 2 → Tier 3)

Render in tier order. TIER BOUNDARY enforced: all T1 voices before any T2; all T2 before any T3.

**[B4 Challenger] ([Role]) -- STANCE: [B1 token] -- INERTIA-CITE: [INERTIA-FINDING-N from B3]**
[Voice from outside-in perspective. Must cite the NORM label assigned in B4.]

[Remaining T1 voices — STANCE + Inertia Citation from B3]

TIER BOUNDARY: No T2 voice before all T1 voices are written.

[T2 voices — STANCE + explicit conditions]

TIER BOUNDARY: No T3 voice before all T2 voices are written.

[T3 voices — STANCE + CITE from B3 + RESPONDS-TO naming a T1 concern]

STANCE MANIFEST (derived from tier grid):

| Participant | Tier | STANCE |
|-------------|------|--------|
| [name]      | T1   | [B1 token] |

Pre-Mortem Risk (B4 Challenger obligation):
[Non-obvious risk from outside-in frame. Must not be predictable by a competent insider.]

PHASE-1-COMMIT: Voices complete in T1→T2→T3 order. B3 tokens cited in T1 cells.
Inertia-to-discussion chain confirmed. Phase 2 may begin.

FAILS: STANCE token not from B1 vocabulary -- C-24 fail.
FAILS: T1 voice absent inertia citation -- C-26 fail.
FAILS: T3 voice appears before T1 voice -- C-25 fail.

---

## PHASE 2 -- Minutes

### Decisions

| # | Decision | Outcome (B1 vocabulary) | Conditions |
|---|----------|------------------------|------------|
| 1 | [text]   | [B1 token]             | [or --]    |

Verdict: **[B1 token] -- [one-sentence rationale]**

FAILS: Outcome uses token not in B1 vocabulary -- C-24 fail.

### Action Items

| # | Action | Owner | Due |
|---|--------|-------|-----|
| 1 | [text] | [Named role] | [milestone] |

FAILS: Owner column empty -- C-04 fail.

### Dissenting Opinions

| Participant | Role | Inertia Token | Objection | Resolution Path |
|-------------|------|---------------|-----------|-----------------|
| [name]      | [role] | [INERTIA-FINDING-N from B3] | [objection] | [path] |

*No dissent -- [which inertia concern was resolved and by what evidence]:* (if applicable)

FAILS: dissent entry absent inertia token citation -- C-27 fail.
FAILS: "No dissent" without inertia resolution justification -- C-27 fail.

PHASE-2-COMMIT: Minutes complete. B3 tokens traced to dissent section. Simulation done.
```

---

## V-02 -- End-to-End Token Trace

**Axis:** End-to-end token trace (C-29)
**Hypothesis:** Inserting a TOKEN TRACE MANIFEST at the Phase 1→2 gate — one row per
INERTIA-FINDING-N, tracking its presence at every required consumption site: T1 Inertia Citation
column, CHAIN-3 risk draft, Phase 2 pre-mortem expansion, Dissent Collection Inertia Token,
Dissenting Opinions Inertia Token — closes C-29 structurally. Any token that drops out at a
consumption site produces a missing cell in the manifest. A reviewer can audit the full chain
by comparing token labels row-by-row without reading prose. A skill that traces tokens only
through the inventory but not through every downstream site leaves silent drop-out points.

```
You are running /corps-committee.

Simulate the committee meeting before it happens. Produce mock meeting minutes.

---

## BEFORE YOU START

### Committee Type and Obligation

Identify your committee type. State its primary obligation and fail condition.

**ROB:** Obligation — readiness verdict backed by metric evidence.
  Fail condition: No metric = ROB not done. (C-01 fail)
  Vocabulary: APPROVED | APPROVED WITH CONDITIONS | BLOCKED | DEFERRED

**SHIPROOM:** Obligation — binary GO or NO-GO backed by risk register.
  Fail condition: No GO/NO-GO = shiproom not done. (C-01 fail, C-03 fail)
  Vocabulary: GO | NO-GO | HOLD

**ARCH-BOARD:** Obligation — ADR with named trade-offs and selected alternative.
  Fail condition: No ADR or no selected winner = arch-board not done. (C-01 fail)
  Vocabulary: ACCEPTED | REJECTED | DEFERRED

Write: VOCABULARY-LOCK: [type] | Tokens: [committed vocabulary]

### Designated Inertia Challenger

Before Phase 0, designate one participant as the Inertia Challenger.

CHALLENGER: [role name] | Outside-in basis: [why least likely to hold the normalized view]
NORM obligation: [INERTIA-FINDING-N — this token is their required Phase 1 citation]

The outside-in basis must be stated and non-circular. A basis that derives from internal
knowledge or general reasoning explicitly fails.

FAILS: Challenger absent before Phase 0 -- C-23 fail.
FAILS: outside-in basis circular (derives from internal knowledge) -- C-19 fail (CHAIN-2).

### Inertia Inventory

Produce four named findings before Phase 0.

INERTIA-FINDING-1: [workflow or tool displaced]
INERTIA-FINDING-2: [integration surface at risk]
INERTIA-FINDING-3: [team habit that breaks]
INERTIA-FINDING-4: [non-obvious switching cost]

GATE: INERTIA-FINDING-4 reveals a cost the author did not anticipate? [YES / NO]
IF NO: rewrite all four. Repeat until YES.

INERTIA RECORD:
| Token             | One-Phrase Anchor | Available for citation |
|-------------------|-------------------|------------------------|
| INERTIA-FINDING-1 | [anchor]          | Yes                    |
| INERTIA-FINDING-2 | [anchor]          | Yes                    |
| INERTIA-FINDING-3 | [anchor]          | Yes                    |
| INERTIA-FINDING-4 | [anchor]          | Yes                    |

---

## PHASE 0 -- Setup

Participant roster (ordered Tier 1 → Tier 2 → Tier 3, Challenger first in T1):

| Seq | Participant | Role | Tier | Charter Status |
|-----|-------------|------|------|----------------|
| 1   | [Challenger] | [role] | T1 | [Standing / Candidate: function] |

Agenda items (type-specific gates from vocabulary):

| # | Agenda Item | Gate | Evidence Required |
|---|-------------|------|-------------------|
| 1 | [item]      | [pass/fail from obligation] | [what must be present] |

Charter constraints:

| Constraint | Requirement | Must Honor |
|------------|-------------|------------|
| Quorum     | [charter]   | Yes        |
| Veto       | [holder]    | Yes        |

PHASE-0-COMMIT: Setup complete.

---

## PHASE 1 -- Simulation

Voices in tier order (T1 → T2 → T3).

**[Challenger] ([Role]) -- STANCE: [vocab token]**
INERTIA-CITE: [INERTIA-FINDING-N from INERTIA RECORD]
[Voice from outside-in perspective. References normalized assumption explicitly.]
CHAIN-3 DRAFT: Risk from this citation — [one-sentence risk draft from the cited token,
connecting the inertia finding to a concrete failure scenario for Phase 2 expansion]

[Remaining T1 voices — STANCE + INERTIA-CITE]

TIER BOUNDARY: No T2 before all T1 complete.

[T2 voices — STANCE + explicit conditions + RESPONDS-TO a T1 entry]

TIER BOUNDARY: No T3 before all T2 complete.

[T3 voices — STANCE + CITE from INERTIA RECORD + RESPONDS-TO naming a T1 concern]

STANCE MANIFEST:
| Participant | Tier | STANCE |
|-------------|------|--------|
| [name]      | [tier] | [token] |

---

## TOKEN TRACE MANIFEST (Phase 1→2 Gate)

Complete this table before Phase 2 begins. For each INERTIA-FINDING-N, verify its presence
at every required downstream consumption site. A missing cell means the token was dropped.

| Token             | T1 Inertia Citation | CHAIN-3 Draft | Dissent Collection | Dissenting Opinions |
|-------------------|--------------------:|:-------------:|:------------------:|:-------------------:|
| INERTIA-FINDING-1 | [cited by whom]     | [yes/absent]  | [yes/absent]       | [yes/absent]        |
| INERTIA-FINDING-2 | [cited by whom]     | [yes/absent]  | [yes/absent]       | [yes/absent]        |
| INERTIA-FINDING-3 | [cited by whom]     | [yes/absent]  | [yes/absent]       | [yes/absent]        |
| INERTIA-FINDING-4 | [cited by whom]     | [yes/absent]  | [yes/absent]       | [yes/absent]        |

TRACE GATE: Any cell marked "absent"?
IF YES: halt. Return to the phase where the token was dropped. Rewrite to include the citation.
  Phase 2 may not begin until all cells across rows of cited tokens are populated.
IF NO: Phase 2 cleared.

FAILS: TOKEN TRACE MANIFEST absent -- C-29 fail.
FAILS: any T1 Inertia Citation cell empty for a cited token -- C-29 fail.
FAILS: CHAIN-3 Draft cell absent for Challenger's cited token -- C-29 fail (CHAIN-3 link broken).
FAILS: Dissent Collection cell absent for any CONDITION or BLOCK token -- C-29 fail.
FAILS: Dissenting Opinions cell absent when dissent was collected -- C-29 fail.
FAILS: Phase 2 begins with "absent" cells in the manifest -- C-29 fail.

---

## PHASE 2 -- Minutes

*Entry: TOKEN TRACE MANIFEST confirms no absent cells for cited tokens.*

Pre-Mortem Expansion (from CHAIN-3 Drafts above):

For each CHAIN-3 draft committed in Phase 1, expand into a concrete risk scenario.

| INERTIA-FINDING-N | CHAIN-3 Draft | Pre-Mortem Expansion |
|-------------------|---------------|----------------------|
| [token]           | [draft]       | [expanded risk scenario — what breaks, when, who notices] |

FAILS: pre-mortem expansion absent for Challenger's CHAIN-3 draft -- C-09 fail.
FAILS: expansion not traceable to its CHAIN-3 draft by token label -- C-29 fail.

### Decisions

| # | Decision | Outcome (vocab token) | Conditions |
|---|----------|-----------------------|------------|
| 1 | [text]   | [committed token]     | [or --]    |

**Verdict: [token] -- [rationale]**

### Action Items

| # | Action | Owner | Due |
|---|--------|-------|-----|
| 1 | [text] | [Named role] | [milestone] |

FAILS: Owner column empty -- C-04 fail.

### Dissent Collection

| Participant | Tier | INERTIA-FINDING-N | STANCE | Dissent Statement |
|-------------|------|-------------------|--------|-------------------|
| [name]      | T1   | [token from INERTIA RECORD] | [BLOCK/CONDITION] | [objection] |

### Dissenting Opinions (formal record)

| Participant | Role | Inertia Token | Objection | Resolution Path | Authority |
|-------------|------|---------------|-----------|-----------------|-----------|
| [name]      | [role] | [token]     | [objection] | [path]         | [named]   |

*No dissent -- [which inertia concern resolved and by what evidence]:* (if applicable)

TOKEN TRACE CONFIRMATION:
- Dissent Collection Inertia Token column populated from INERTIA RECORD? [YES / NO]
- Dissenting Opinions Inertia Token column matches Dissent Collection entries? [YES / NO]
- All cited tokens traceable back to Phase 1 CHAIN-3 drafts? [YES / NO]

FAILS: token trace confirmation any NO -- C-29 fail.
FAILS: dissent entry absent inertia token -- C-27 fail.

PHASE-2-COMMIT: Token trace confirmed end-to-end. Simulation complete.
```

---

## V-03 -- AMEND Block-Level Routing

**Axis:** AMEND block-level routing (C-30)
**Hypothesis:** Adding an AMEND ROUTING TABLE that explicitly maps each amendment type to the
specific pre-execution blocks that must be re-run — before any phase re-execution — closes C-30
structurally. A participant composition change must invalidate Block 2 (tier pre-assignment) and
Block 4 (Challenger designation) before Phase 0 re-execution; a committee type change must
invalidate Block 1 (vocabulary contract) and Block 2 (tier assignments that reference type-specific
tokens). The block re-execution boundary must be stated explicitly. A skill that restarts from
Phase 0 on AMEND without specifying which blocks are invalidated leaves the block dependency
graph in an inconsistent state.

```
You are running /corps-committee.

Simulate the committee meeting before it happens. Produce mock meeting minutes.

---

## BEFORE YOU START

### Committee Type

Identify your committee type. State its obligation and fail condition.

**ROB:** Obligation — readiness verdict backed by metric evidence. Fail: no metric.
  Vocabulary: APPROVED | APPROVED WITH CONDITIONS | BLOCKED | DEFERRED

**SHIPROOM:** Obligation — GO or NO-GO backed by risk register. Fail: no GO/NO-GO.
  Vocabulary: GO | NO-GO | HOLD

**ARCH-BOARD:** Obligation — ADR with trade-offs and selected winner. Fail: no ADR.
  Vocabulary: ACCEPTED | REJECTED | DEFERRED

B1-COMMIT: [type] | Topic: [topic] | Vocabulary: [tokens]

### Designated Inertia Challenger

CHALLENGER: [role] | Rationale: [outside-in basis] | NORM obligation: [INERTIA-FINDING-N]

The outside-in basis must not derive from internal knowledge. A circular basis fails.

B4-COMMIT: Challenger designated. Tier: 1. NORM obligation declared.

### Inertia Inventory

INERTIA-FINDING-1: [workflow displaced]
INERTIA-FINDING-2: [integration at risk]
INERTIA-FINDING-3: [team habit broken]
INERTIA-FINDING-4: [non-obvious cost]

GATE: INERTIA-FINDING-4 non-obvious? YES / NO. IF NO: rewrite until YES.

INERTIA RECORD:
| Token             | Anchor   |
|-------------------|----------|
| INERTIA-FINDING-1 | [anchor] |
| INERTIA-FINDING-2 | [anchor] |
| INERTIA-FINDING-3 | [anchor] |
| INERTIA-FINDING-4 | [anchor] |

B3-COMMIT: Inventory sealed.

### Tier Pre-Assignment

Assign every participant to a tier before Phase 0. Challenger is Tier 1.

| Participant | Role | Tier | STANCE-pool | Inertia Citation (T1) | Rationale |
|-------------|------|------|-------------|----------------------|-----------|
| [Challenger] | [role] | T1 | [B1 tokens] | [INERTIA-FINDING-N] | [outside-in frame] |
| [name]      | [role] | T2 | [B1 tokens] | --                  | [conditional basis] |
| [name]      | [role] | T3 | [B1 tokens] | --                  | [advocacy basis] |

B2-COMMIT: Tiers assigned. B1 vocabulary consumed. B3 tokens cited.

---

## AMEND ROUTING TABLE

When AMEND is invoked, determine re-execution scope here before touching any phase content.

Do not re-run phases until this table is completed for the amendment type.

| Amendment Type                  | Blocks Invalidated     | Re-run Order Before Phase 0 | Reason |
|---------------------------------|------------------------|-----------------------------|--------|
| Participant composition change  | B2, B4                 | B2 → B4                     | Tier pre-assignment depends on participant set; Challenger designation depends on tier roster |
| Committee type change           | B1, B2                 | B1 → B2                     | Vocabulary tokens change; tier STANCE-pool references type-specific tokens from B1 |
| Scope / agenda change           | B3 (partial), B2 (if findings change) | B3 → B2 (if T1 citation targets change) | Inertia inventory may change; T1 citations must reference tokens in the new inventory |
| Challenger role change          | B4                     | B4                          | Challenger designation draws from B2 tier roster — tier roster unchanged, only designation re-run |

### On AMEND Invocation

1. Identify the amendment type from the table above.
2. State which blocks are invalidated: AMEND-BLOCKS-INVALIDATED: [B1 / B2 / B3 / B4]
3. Re-run each invalidated block in the listed order.
4. Write each block's new COMMIT line with suffix: (AMENDED)
5. Verify inter-block cross-checks pass for all re-run blocks.
6. Only then proceed to Phase 0 re-execution.

Example — participant composition change:
> Amendment: Add [new participant] as Tier 1 Challenger (replaces [old participant]).
> AMEND-BLOCKS-INVALIDATED: B2, B4
> Re-running B2 with new participant set... B2-COMMIT: (AMENDED)
> Re-running B4 with new B2 roster... B4-COMMIT: (AMENDED)
> Proceeding to Phase 0 (AMENDED).

FAILS: AMEND invoked but AMEND-BLOCKS-INVALIDATED not stated -- C-30 fail.
FAILS: participant change re-runs Phase 0 without re-running B2 and B4 first -- C-30 fail.
FAILS: type change re-runs phases without re-running B1 and B2 first -- C-30 fail.
FAILS: AMEND-BLOCKS-INVALIDATED stated but invalidated block outputs still carry pre-amendment values -- C-30 fail.
FAILS: AMEND not invoked = vacuously satisfied.

---

## PHASE 0 -- Setup

(Enters after all blocks committed or re-committed after AMEND.)

Participant roster (ordered by tier from B2):

| Seq | Participant | Role | Tier | Charter Status |
|-----|-------------|------|------|----------------|
| 1   | [Challenger] | [role] | T1 | [Standing] |

Agenda:

| # | Agenda Item | Gate | Evidence Required |
|---|-------------|------|-------------------|

Charter constraints:

| Constraint | Requirement | Honored |
|------------|-------------|---------|
| Quorum     | [charter]   | Yes     |
| Veto       | [holder]    | Yes     |

PHASE-0-COMMIT: Roster locked from B2 (or B2 AMENDED).

---

## PHASE 1 -- Simulation

Voices in T1 → T2 → T3 order. TIER BOUNDARY enforced.

**[Challenger] -- STANCE: [B1 token] -- INERTIA-CITE: [INERTIA-FINDING-N from B3]**
[Outside-in voice. Pre-mortem risk from non-obvious frame.]

[T1, T2, T3 voices following tier ordering]

STANCE MANIFEST:
| Participant | Tier | STANCE |
|-------------|------|--------|

PHASE-1-COMMIT: All voices complete. B3 tokens cited in T1 cells.

---

## PHASE 2 -- Minutes

### Decisions

| # | Decision | Outcome (B1 token) | Conditions |
|---|----------|--------------------|------------|

**Verdict: [B1 token]**

### Action Items

| # | Action | Owner | Due |
|---|--------|-------|-----|

FAILS: Owner absent -- C-04 fail.

### Dissenting Opinions

| Participant | Role | Inertia Token | Objection | Resolution Path |
|-------------|------|---------------|-----------|-----------------|

*No dissent -- [inertia concern resolved and evidence]:* (if applicable)

FAILS: dissent absent inertia token -- C-27 fail.

PHASE-2-COMMIT: Minutes complete. Simulation done.
```

---

## V-04 -- Block Graph + Token Trace (C-28 + C-29)

**Axis:** Combination — cross-block dependency graph (C-28) + end-to-end token trace (C-29)
**Hypothesis:** The block dependency graph and the token trace are complementary audit mechanisms:
the block dependency graph ensures that each block's outputs are available before the next block
consumes them (pre-execution consistency); the token trace manifest ensures that tokens
originating in the inventory survive to every downstream consumption site (execution consistency).
Together they form a two-phase self-auditing system: block-level auditable before simulation,
token-level auditable at the Phase 1→2 gate. A skill with only one of these mechanisms has a gap
where the other would catch failures.

```
You are running /corps-committee.

Simulate the committee meeting before it happens. Produce mock meeting minutes.

---

## BLOCK DEPENDENCY MAP AND TOKEN TRACE CONTRACT

### Part 1 -- Block Dependency Map

Before any block executes, declare what each block consumes. Blocks may not execute until
all declared inputs are available.

| Block | Label                  | Consumes From | Required Input (must be present before this block runs) |
|-------|------------------------|---------------|---------------------------------------------------------|
| B1    | Vocabulary Contract    | (origin)      | (none — first block) |
| B3    | Inertia Inventory      | (origin)      | (none — runs before B2 to be available for B2 citation) |
| B2    | Tier Pre-Assignment    | B1            | B1 outcome vocabulary tokens — STANCE-pool column draws from B1 tokens only |
| B2    | Tier Pre-Assignment    | B3            | T1 Inertia Citation — at least one T1 entry must name a token present in B3 INERTIA RECORD |
| B4    | Challenger Designation | B2            | Challenger must match a Tier 1 entry committed in B2 |
| B4    | Challenger Designation | B3            | NORM label obligation — must name a token present in B3 INERTIA RECORD |

### Part 2 -- Token Trace Contract

At the Phase 1→2 gate, a TOKEN TRACE MANIFEST confirms end-to-end token presence.
Required consumption sites per token that appears in the Phase 1 T1 Inertia Citation column:

1. B3 INERTIA RECORD (origin)
2. Phase 1 T1 Inertia Citation column
3. CHAIN-3 Draft (Challenger's cited token requires a risk draft at Phase 1→2 gate)
4. Phase 2 Pre-Mortem Expansion (derives from CHAIN-3 draft)
5. Dissent Collection Inertia Token column
6. Dissenting Opinions Inertia Token column

A token that drops at any site is a missing cell in the manifest.

---

## BLOCK 1 -- Vocabulary Contract

Committee type: [ROB / SHIPROOM / ARCH-BOARD]
Topic: [topic]

**ROB:** Vocabulary — APPROVED | APPROVED WITH CONDITIONS | BLOCKED | DEFERRED
  Fail condition: No metric = ROB not done.
**SHIPROOM:** Vocabulary — GO | NO-GO | HOLD
  Fail condition: No GO/NO-GO = shiproom not done.
**ARCH-BOARD:** Vocabulary — ACCEPTED | REJECTED | DEFERRED
  Fail condition: No ADR = arch-board not done.

B1-COMMIT: [type] | Vocabulary: [tokens]
B1 → B2 availability: vocabulary tokens available for STANCE-pool column.

---

## BLOCK 3 -- Inertia Inventory

(Runs before B2 so B2's T1 Inertia Citation can reference these tokens.)

INERTIA-FINDING-1: [workflow displaced]
INERTIA-FINDING-2: [integration at risk]
INERTIA-FINDING-3: [team habit broken]
INERTIA-FINDING-4: [non-obvious cost — author-unanticipated]

GATE: INERTIA-FINDING-4 non-obvious? YES / NO. IF NO: rewrite until YES.

INERTIA RECORD:
| Token             | Anchor   | Status for B2/B4 citation |
|-------------------|----------|---------------------------|
| INERTIA-FINDING-1 | [anchor] | Available                 |
| INERTIA-FINDING-2 | [anchor] | Available                 |
| INERTIA-FINDING-3 | [anchor] | Available                 |
| INERTIA-FINDING-4 | [anchor] | Available                 |

B3-COMMIT: Inventory sealed. Tokens available for B2 and B4.
B3 → B2 availability: all INERTIA-FINDING-* tokens available for T1 Inertia Citation column.
B3 → B4 availability: all tokens available for NORM label obligation.

---

## BLOCK 4 -- Designated Inertia Challenger

(Runs after B2 and B3.)

CHALLENGER-DESIGNATION:
- Role: [role name]
- Tier (from B2): [must be T1]
- B2 tier match: [YES — this role appears as T1 in B2 / NO — conflict, fix B2]
- Outside-in rationale: [why least likely to hold the normalized assumption]
- NORM obligation: [INERTIA-FINDING-N from B3 INERTIA RECORD — required Phase 1 citation]
- B3 token exists: [YES / NO — if NO, fix B3 or select a different token]

B4 CROSS-BLOCK CHECKS:
- Challenger tier matches B2 T1 entry? [YES / NO]
- NORM obligation token exists in B3 INERTIA RECORD? [YES / NO]
IF any NO: halt and fix before proceeding.

B4-COMMIT: Challenger designated. B2 T1 match confirmed. B3 token obligation assigned.

FAILS: B4 Challenger tier does not match B2 T1 entry -- C-28 fail.
FAILS: NORM obligation token not in B3 -- C-28 fail.

---

## BLOCK 2 -- Tier Pre-Assignment

(Runs after B1 and B3.)

| Participant | Role | Tier | STANCE-pool (from B1) | Inertia Citation T1 (from B3) | Rationale |
|-------------|------|------|-----------------------|-------------------------------|-----------|
| [Challenger] | [role] | T1 | [B1 tokens]         | [INERTIA-FINDING-N]           | [outside-in frame] |
| [name]      | [role] | T2 | [B1 tokens]           | --                            | [conditional basis] |
| [name]      | [role] | T3 | [B1 tokens]           | --                            | [advocacy basis] |

B2 CROSS-BLOCK CHECKS:
- STANCE-pool column uses only B1 vocabulary tokens? [YES / NO]
- T1 Inertia Citation column references tokens present in B3? [YES / NO]
IF any NO: halt and fix.

B2-COMMIT: Tiers assigned. B1 vocabulary consumed. B3 tokens cited.

---

## PHASE 0 -- Setup

(Enters after all blocks committed.)

Participant Roster (ordered by tier from B2):

| Seq | Participant | Role | Tier | Charter Status |
|-----|-------------|------|------|----------------|
| 1   | [B4 Challenger] | [role] | T1 | [Standing / Candidate: function] |

Agenda (type-specific from B1 obligation):

| # | Item | Type Gate | Evidence Required |
|---|------|-----------|-------------------|

Charter Constraints:

| Constraint | Requirement | Honored |
|------------|-------------|---------|
| Quorum     | [charter]   | Yes     |
| Veto       | [holder]    | Yes     |

PHASE-0-COMMIT: Roster locked from B2. Block dependency chain verified.

---

## PHASE 1 -- Simulation (T1 → T2 → T3)

TIER BOUNDARY enforced: all T1 before any T2; all T2 before any T3.

**[B4 Challenger] ([Role]) -- STANCE: [B1 token]**
INERTIA-CITE: [INERTIA-FINDING-N from B3 INERTIA RECORD]
[Outside-in voice. References normalized assumption. Non-circular basis.]
CHAIN-3 DRAFT: [one-sentence risk connecting the cited token to a concrete failure scenario]

[Remaining T1 voices — STANCE + INERTIA-CITE from B3]

TIER BOUNDARY.

[T2 voices — STANCE + conditions + RESPONDS-TO a T1 entry]

TIER BOUNDARY.

[T3 voices — STANCE + CITE from B3 + RESPONDS-TO]

STANCE MANIFEST:
| Participant | Tier | STANCE (B1 token) | Inertia Token Cited |
|-------------|------|-------------------|---------------------|
| [name]      | T1   | [token]           | [INERTIA-FINDING-N] |

PHASE-1-COMMIT: Voices complete T1→T2→T3. B3 tokens cited. CHAIN-3 drafts present.

---

## TOKEN TRACE MANIFEST (Phase 1→2 Gate)

For each cited INERTIA-FINDING-N, track presence at every consumption site.
Phase 2 may not begin until all cited tokens show YES at all required sites.

| Token             | B3 Origin | T1 Cite | CHAIN-3 Draft | Pre-Mortem Expand | Dissent Collect | Dissent Opinions |
|-------------------|-----------|---------|---------------|-------------------|-----------------|------------------|
| INERTIA-FINDING-1 | YES       | [yes/--] | [yes/--]     | [yes/--]          | [yes/--]        | [yes/--]         |
| INERTIA-FINDING-2 | YES       | [yes/--] | [yes/--]     | [yes/--]          | [yes/--]        | [yes/--]         |
| INERTIA-FINDING-3 | YES       | [yes/--] | [yes/--]     | [yes/--]          | [yes/--]        | [yes/--]         |
| INERTIA-FINDING-4 | YES       | [yes/--] | [yes/--]     | [yes/--]          | [yes/--]        | [yes/--]         |

TRACE GATE: Any "--" in a required site for a cited token?
IF YES: halt. Return to the phase where the token was dropped. Fix. Do not proceed.
IF NO: Phase 2 cleared.

FAILS: manifest absent -- C-29 fail.
FAILS: any cited token has "--" at T1 Cite -- C-29 fail.
FAILS: CHAIN-3 Draft absent for Challenger's cited token -- C-19 fail (CHAIN-3 broken).
FAILS: Dissent Opinions column absent for any BLOCK or CONDITION token -- C-29 fail.

---

## PHASE 2 -- Minutes

*Entry: TOKEN TRACE MANIFEST fully populated for all cited tokens.*

Pre-Mortem Expansion:
| INERTIA-FINDING-N | CHAIN-3 Draft | Expanded Risk |
|-------------------|---------------|---------------|
| [token]           | [draft]       | [what breaks, when, who notices — outside-in only] |

### Decisions
| # | Decision | Outcome (B1 token) | Conditions |
|---|----------|--------------------|------------|

**Verdict: [B1 token] -- [rationale]**

### Action Items
| # | Action | Owner | Due |
|---|--------|-------|-----|
FAILS: Owner absent -- C-04 fail.

### Dissent Collection
| Participant | Tier | INERTIA-FINDING-N | STANCE | Dissent Statement |
|-------------|------|-------------------|--------|-------------------|

### Dissenting Opinions
| Participant | Role | Inertia Token | Objection | Resolution Path | Authority |
|-------------|------|---------------|-----------|-----------------|-----------|

*No dissent -- [which inertia concern resolved and by what evidence]:* (if applicable)

TOKEN TRACE FINAL CONFIRMATION:
- Dissent Collection Inertia Token column populated? [YES / NO]
- Dissenting Opinions Inertia Token column matches Dissent Collection? [YES / NO]
- Pre-Mortem Expansion traces back to CHAIN-3 drafts by token label? [YES / NO]

FAILS: any confirmation NO -- C-29 fail.
FAILS: dissent entry absent inertia token -- C-27 fail.

PHASE-2-COMMIT: Token trace confirmed. Simulation complete.
```

---

## V-05 -- Full Integration

**Axis:** Full integration — C-28 + C-29 + C-30 + R8 architecture (C-24 vocabulary contract +
C-25 tier-sequenced voice + C-26 per-tier column grammar + C-27 inertia-to-dissent token anchor
+ C-23 pre-Phase-0 Challenger block + C-16/C-21/C-22 table-first structural grammar)
**Hypothesis:** All five structural properties of a converged skill reinforce each other when
combined: the block dependency graph (C-28) ensures inter-block consistency before simulation
begins; the end-to-end token trace (C-29) ensures inertia tokens survive every consumption site;
the AMEND routing table (C-30) ensures amendments invalidate the correct blocks before phase
re-execution; the vocabulary contract (C-24) ensures decision tokens are type-keyed; the
tier-sequenced voice protocol (C-25 + C-26) ensures confrontation before consensus in a
structurally enforced column grammar; and the inertia token anchoring in dissent (C-27) makes
the full chain from normalized assumption to recorded objection auditable by token label alone.
The skill that combines all five has no silent drop-out points: every omission produces a
missing cell or a failed gate.

```
You are running /corps-committee.

Simulate the committee meeting before it happens. Produce mock meeting minutes.

---

## BLOCK DEPENDENCY MAP

Declare inter-block dependencies before any block executes. Each block may only run after
all its declared inputs are committed.

| Block | Label                  | Consumes From     | Required Input |
|-------|------------------------|-------------------|----------------|
| B1    | Vocabulary Contract    | (origin)          | none |
| B3    | Inertia Inventory      | (origin)          | none |
| B2    | Tier Pre-Assignment    | B1, B3            | B1 vocabulary → STANCE-pool; B3 tokens → T1 Inertia Citation |
| B4    | Challenger Designation | B2, B3            | B2 T1 entry → Challenger tier; B3 token → NORM obligation |

AMEND ROUTING TABLE (consult on any AMEND invocation before touching phases):

| Amendment Type                  | Blocks Invalidated | Re-run Order | Before Phase Re-execution |
|---------------------------------|--------------------|--------------|---------------------------|
| Participant composition change  | B2, B4             | B2 → B4      | Yes — both re-committed before Phase 0 |
| Committee type change           | B1, B2             | B1 → B2      | Yes — both re-committed; B3 unchanged unless findings change |
| Scope / agenda change           | B3, B2 (if T1 cites change) | B3 → B2 | Only if inventory changes |
| Challenger role change          | B4 only            | B4           | B4 re-committed; B2 roster unchanged |

On AMEND: write AMEND-BLOCKS-INVALIDATED: [list] before re-running any block.

FAILS: AMEND invoked without AMEND-BLOCKS-INVALIDATED declaration -- C-30 fail.
FAILS: participant change runs Phase 0 without re-running B2 and B4 first -- C-30 fail.
FAILS: type change runs phases without re-running B1 and B2 first -- C-30 fail.

---

## BLOCK 1 -- Vocabulary Contract

Identify committee type. Commit its primary obligation, fail condition, and outcome vocabulary.
All STANCE, TALLY, and Verdict tokens downstream must draw from here only.

**ROB (Product Review / Service Review)**
Primary obligation: A readiness verdict backed by metric evidence.
Fail condition: No metric in output = ROB not done. (C-01 fail)
OUTCOME VOCABULARY: APPROVED | APPROVED WITH CONDITIONS | BLOCKED | DEFERRED

**SHIPROOM (Go / No-Go)**
Primary obligation: A binary GO or NO-GO backed by a risk register.
Fail condition: No GO or NO-GO decision line = shiproom not done. (C-01 fail, C-03 fail)
OUTCOME VOCABULARY: GO | NO-GO | HOLD

**ARCH-BOARD (Architecture Decision Review)**
Primary obligation: An ADR with named trade-offs and a selected alternative.
Fail condition: No ADR or no selected winner = arch-board not done. (C-01 fail)
OUTCOME VOCABULARY: ACCEPTED | REJECTED | DEFERRED

B1-COMMIT: [ROB / SHIPROOM / ARCH-BOARD] | Topic: [topic] | Vocabulary: [committed tokens]
B1 → B2 availability: [committed tokens] available for STANCE-pool column.

FAILS: B1-COMMIT absent -- C-24 fail, C-13 fail.
FAILS: vocabulary committed but downstream STANCE uses foreign tokens -- C-24 fail, C-28 fail.

---

## BLOCK 3 -- Inertia Inventory

(Runs before B2 to be available for B2 T1 Inertia Citation column.)

What will this committee rubber-stamp without challenge? Identify the normalized assumptions
the real committee holds as default. Produce four named findings.

INERTIA-FINDING-1: [specific workflow or tool in production this agenda item displaces — name it]
INERTIA-FINDING-2: [specific integration surface at risk — name system, API, or contract]
INERTIA-FINDING-3: [team whose cognitive habit breaks and the specific habit — name both]
INERTIA-FINDING-4: [non-obvious switching cost the proposal author did not account for]

GATE: INERTIA-FINDING-4 reveals a cost the author would not have anticipated? [YES / NO]
IF NO: rewrite all four findings. Increment attempt. Repeat until YES.
ENFORCE: each attempt labeled INVESTIGATION-ATTEMPT-N.

INERTIA RECORD (sealed at B3-COMMIT):
| Token             | One-Phrase Anchor | Available for B2/B4 |
|-------------------|-------------------|---------------------|
| INERTIA-FINDING-1 | [anchor]          | Yes |
| INERTIA-FINDING-2 | [anchor]          | Yes |
| INERTIA-FINDING-3 | [anchor]          | Yes |
| INERTIA-FINDING-4 | [anchor]          | Yes |

B3-COMMIT: Inventory sealed. Findings locked. B2 and B4 may cite these tokens.
B3 → B2 availability: all INERTIA-FINDING-* tokens available for T1 Inertia Citation column.
B3 → B4 availability: all tokens available for NORM label obligation.

FAILS: any INERTIA-FINDING-* bare label or unfilled placeholder -- C-18 fail.
FAILS: B3-COMMIT absent -- downstream blocks cannot verify citation targets.

---

## BLOCK 4 -- Designated Inertia Challenger

(Runs after B2 and B3. This block is structurally isolated — not a row in the Phase 0 roster.)

Designate one participant as the Inertia Challenger. This designation is committed before
Phase 0 roster construction begins.

CHALLENGER-DESIGNATION:
- Role: [role name]
- Tier (from B2): [T1 — verified]
- Outside-in rationale: [why this frame is least likely to reflect the normalized assumption —
  must be non-circular: basis derived from internal knowledge or general reasoning fails]
- NORM label obligation: [INERTIA-FINDING-N from B3 INERTIA RECORD — required Phase 1 citation]

B4 CROSS-BLOCK CHECKS:
1. Challenger role matches a Tier 1 entry in B2 tier table? [YES / NO]
2. NORM label obligation exists in B3 INERTIA RECORD? [YES / NO]

IF check 1 NO: fix B2 tier table or select a different Challenger.
IF check 2 NO: select a different NORM token from B3 or revise B3.

B4-COMMIT: Challenger designated. B2 T1 match confirmed. B3 NORM obligation assigned.
B4 → Phase 0: Challenger is first participant in Tier 1 roster.

FAILS: B4 Challenger tier does not match B2 T1 entry -- C-28 fail, C-23 fail.
FAILS: NORM obligation not in B3 -- C-28 fail, C-20 fail.
FAILS: outside-in basis is circular -- C-19 fail.
FAILS: B4 cross-block check absent -- C-28 fail.

---

## BLOCK 2 -- Tier Pre-Assignment

(Runs after B1 and B3; B4 Challenger identity used to assign T1 position.)

Pre-assign all participants to voice tiers before Phase 0 roster construction.
ORDERING CONSTRAINT (structural): T1 voices before T2; T2 voices before T3. Not stylistic.

| Participant | Role | Tier | STANCE-pool (B1 tokens only) | Inertia Citation (T1 — from B3) | Rationale |
|-------------|------|------|------------------------------|---------------------------------|-----------|
| [B4 Challenger] | [role] | T1 | [B1 vocabulary] | [INERTIA-FINDING-N] | [outside-in frame per B4] |
| [name]      | [role] | T1 | [B1 vocabulary]              | [INERTIA-FINDING-N or --]       | [challenger basis] |
| [name]      | [role] | T2 | [B1 vocabulary]              | --                              | [conditional basis] |
| [name]      | [role] | T3 | [B1 vocabulary]              | --                              | [advocacy basis] |

B2 CROSS-BLOCK CHECKS:
1. STANCE-pool column: all tokens from B1-COMMIT vocabulary? [YES / NO]
2. T1 Inertia Citation column: all citations reference tokens present in B3 INERTIA RECORD? [YES / NO]
3. SORT-CHECK: Tier 1 and Tier 2 both empty? [YES — reassign / NO — proceed]

IF check 1 or 2 NO: halt and fix.
IF SORT-CHECK YES: reassign at least one participant to T1, state reason, reprint, recheck.

B2-COMMIT: Tiers assigned. B1 vocabulary consumed in STANCE-pool. B3 tokens cited in T1 column.
B2 → Phase 0: roster drawn from this table in T1→T2→T3 order.
B2 → B4: T1 entries available for Challenger tier verification.

FAILS: STANCE-pool uses tokens not in B1 vocabulary -- C-28 fail, C-24 fail.
FAILS: T1 citation references token not in B3 -- C-28 fail, C-26 fail.
FAILS: SORT-CHECK absent -- C-25 fail.

---

## PHASE 0 -- Roster and Agenda

(Enters after B1, B2, B3, B4 all committed. Roster drawn from B2 in T1→T2→T3 order,
B4 Challenger first in T1.)

Participant Roster:

| Seq | Participant | Role | Tier | Primary Concern | Charter Status |
|-----|-------------|------|------|-----------------|----------------|
| 1   | [B4 Challenger] | [role] | T1 | [concern from B4 rationale] | [Standing / Candidate: function] |
| 2   | [T1 next]   | [role] | T1 | [concern]       | [Standing] |
| 3   | [T2]        | [role] | T2 | [concern]       | [Standing] |
| 4   | [T3]        | [role] | T3 | [concern]       | [Standing] |

Agenda (type-specific from B1 obligation):

| # | Agenda Item | Type Gate (from B1 obligation) | Evidence Required |
|---|-------------|-------------------------------|-------------------|
| 1 | [item]      | [pass/fail for this type]     | [what must be present] |
| 2 | [item]      | [pass/fail]                   | [evidence] |

Charter Constraints (at least two, from .craft/roles/):

| Constraint | Charter Requirement | Must Honor in Phase 1 |
|------------|---------------------|----------------------|
| Quorum     | [charter]           | Yes |
| Veto       | [holder + conditions] | Yes |

PHASE-0-COMMIT: Roster locked from B2. Charter constraints declared. Block chain complete.
| ENFORCE: terminal position — NO PHASE 0 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 1 -- Simulation

*Entry: all blocks committed, Phase 0 complete.*
*Constraint: T1 voices before T2; T2 before T3. Not a preference — a structural constraint.*

### Tier 1 Voices (all T1 before any T2)

**Voice format (required columns per tier):**

Tier 1 (Challenger + other T1):
| Participant | STANCE (B1 token) | Inertia Token Cited (from B3) | Voice Content |
|-------------|-------------------|-------------------------------|---------------|

CHAIN-3 DRAFT (B4 Challenger's cited token only):
CHAIN-3: [INERTIA-FINDING-N] → risk draft — [one sentence connecting the inertia finding to
a concrete failure scenario, for Phase 2 expansion]

Basis confirmation (B4 Challenger): outside-in basis non-circular? [YES — basis stated /
NO — basis derives from internal knowledge — rewrite]

TIER BOUNDARY: NO Tier 2 voice before all Tier 1 voices are written.

### Tier 2 Voices (all T2 before any T3)

Tier 2 (Conditional):
| Participant | STANCE (B1 token) | Explicit Conditions | RESPONDS-TO (T1 entry) |
|-------------|-------------------|---------------------|------------------------|

"Address concerns" is not an explicit condition. Name the specific deliverable or change required.

TIER BOUNDARY: NO Tier 3 voice before all Tier 2 voices are written.

### Tier 3 Voices

Tier 3 (Advocate):
| Participant | STANCE (B1 token) | CITE (from B3 INERTIA RECORD) | RESPONDS-TO (T1 or T2 entry) |
|-------------|-------------------|-------------------------------|------------------------------|

STANCE MANIFEST (derived from tier grids — token count source for Phase 2 tally):
| Participant | Tier | STANCE (B1 token) | Inertia Token Cited |
|-------------|------|-------------------|---------------------|
| [name]      | T1   | [token]           | [INERTIA-FINDING-N] |

PHASE-1-COMMIT: Voices complete T1→T2→T3. B3 tokens cited. CHAIN-3 draft present.
All voices rendered. STANCE MANIFEST sealed.
| ENFORCE: terminal position — NO PHASE 1 CONTENT MAY FOLLOW THIS LINE.

---

## TOKEN TRACE MANIFEST (Phase 1→2 Gate)

Complete this table before Phase 2 begins. A missing cell means the token was dropped.
Phase 2 may not begin if any cited token has "--" at a required consumption site.

| Token             | B3 Origin | T1 Cite | CHAIN-3 Draft | Pre-Mortem Expand | Dissent Collect | Dissent Opinions |
|-------------------|-----------|---------|---------------|-------------------|-----------------|------------------|
| INERTIA-FINDING-1 | YES       |         |               |                   |                 |                  |
| INERTIA-FINDING-2 | YES       |         |               |                   |                 |                  |
| INERTIA-FINDING-3 | YES       |         |               |                   |                 |                  |
| INERTIA-FINDING-4 | YES       |         |               |                   |                 |                  |

Fill each cell: YES (present by label), -- (not cited this run, not required), MISSING (required but absent — halt).

TRACE GATE:
- Any cell marked MISSING? → HALT. Return to drop-out phase. Fix. Do not proceed to Phase 2.
- All cited tokens show YES at all required sites? → Phase 2 cleared.

FAILS: manifest absent -- C-29 fail.
FAILS: MISSING in T1 Cite for a token that was the NORM obligation -- C-29 fail, C-19 fail.
FAILS: MISSING in CHAIN-3 Draft for Challenger's cited token -- C-29 fail (CHAIN-3 broken).
FAILS: MISSING in Dissent Opinions for any BLOCK or CONDITION token -- C-29 fail, C-27 fail.

---

## PHASE 2 -- Minutes

*Entry: TOKEN TRACE MANIFEST fully populated (no MISSING cells) for all cited tokens.*

### Pre-Mortem Expansion

For each CHAIN-3 draft from Phase 1, expand into a concrete risk scenario.

| Inertia Token     | CHAIN-3 Draft        | Expanded Risk Scenario |
|-------------------|----------------------|------------------------|
| [INERTIA-FINDING-N] | [draft from Phase 1] | [what breaks, when, who notices, why a competent insider would not have predicted it] |

FAILS: expansion absent for Challenger's CHAIN-3 draft -- C-09 fail.
FAILS: expansion not traceable to its CHAIN-3 source by token label -- C-29 fail.

### Decisions

Outcome column uses only the B1-COMMIT vocabulary tokens.

| # | Decision | Outcome (B1 token) | Conditions (specific deliverables, not "address feedback") |
|---|----------|--------------------|-----------------------------------------------------------|
| 1 | [text]   | [B1 token]         | [or --] |

**Verdict: [B1 token] -- [one-sentence rationale]**

FAILS: Outcome token not from B1 vocabulary -- C-24 fail.
FAILS: Decisions table absent -- C-03 fail.
FAILS: Verdict token not from B1 vocabulary -- C-24 fail.

If verdict is not APPROVED / GO / ACCEPTED:
- Owner: [named role from Phase 0 roster — not a team]
- Trigger: [named artifact + recipient + authority]
FAILS: Owner or Trigger absent when verdict is non-approval -- C-03 partial.

### Action Items

| # | Action (specific, not "address feedback") | Owner (named role) | Due (milestone) |
|---|-------------------------------------------|--------------------|-----------------|
| 1 | [text] | [Name / Role] | [milestone] |

FAILS: Owner column empty for any row -- C-04 fail, C-21 fail.
FAILS: table absent when Phase 1 raised open questions -- C-04 fail.

### Dissent Collection

| Participant | Tier | Inertia Token (B3) | STANCE | Dissent Statement |
|-------------|------|-------------------|--------|-------------------|
| [name]      | T1   | [INERTIA-FINDING-N] | BLOCK  | [objection stating why the inertia finding is not resolved] |
| [name]      | T2   | [INERTIA-FINDING-N] | CONDITION | [condition not yet met] |

FAILS: CONDITION or BLOCK stance participant absent from this table -- C-22 fail.

### Dissenting Opinions (formal record)

| Participant | Role | Inertia Token | Objection | Resolution Path | Named Authority | Trigger |
|-------------|------|---------------|-----------|-----------------|-----------------|---------|
| [name]      | [role] | [INERTIA-FINDING-N from B3] | [objection] | [path] | [authority] | [concrete trigger] |

*No dissent — [which inertia concern was resolved and by what evidence]:* (if applicable)

FAILS: dissent entry absent inertia token citation -- C-27 fail.
FAILS: "No dissent" without inertia resolution justification -- C-27 fail.
FAILS: participant with BLOCK or CONDITION stance absent from this table -- C-05 fail.

### Charter Constraints Honored

| Constraint | Requirement (from Phase 0) | Applied | Evidence |
|------------|---------------------------|---------|----------|
| Quorum     | [charter]                 | Yes / No | [count] |
| Veto       | [holder]                  | Exercised / Waived | [outcome] |

FAILS: fewer than two constraints confirmed -- C-10 partial.

### TOKEN TRACE FINAL CONFIRMATION

| Token             | Pre-Mortem Expand | Dissent Collect | Dissent Opinions | Chain Complete? |
|-------------------|-------------------|-----------------|------------------|-----------------|
| INERTIA-FINDING-N | [YES/--]          | [YES/--]        | [YES/--]         | [YES / BROKEN]  |

FAILS: any row shows BROKEN -- C-29 fail.

PHASE-2-COMMIT: Decisions, action items, dissenting opinions, charter confirmation, and
token trace final confirmation complete. Block dependency graph verified end-to-end.
Simulation complete.
| ENFORCE: terminal position — NO PHASE 2 CONTENT MAY FOLLOW THIS LINE.
```
