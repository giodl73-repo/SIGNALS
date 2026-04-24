**389 words removed (21.1% reduction). All 47 criteria verified below.**

---

## Simplified Prompt Body

```
PHASE 0 — SCOUT ARTIFACT DISCOVERY
-> ROLE: PM

ENTER Phase 0: No preconditions.

You are beginning Phase 0. Your goal is to establish what scout evidence already
exists for this topic before any authoring begins.

PM: scan workspace -> populate [SCOUT-STATUS-TABLE]:

  [SCOUT-STATUS-TABLE]
  Artifact Type        | Status       | File Path
  ---------------------|--------------|----------
  scout-requirements   | LOADED / N/A |
  scout-feasibility    | LOADED / N/A |
  scout-compliance     | LOADED / N/A |
  scout-market         | LOADED / N/A |
  scout-stakeholders   | LOADED / N/A |
  scout-naming         | LOADED / N/A |
  scout-positioning    | LOADED / N/A |

PM: evaluate table -> execute first matching branch:

  Branch A — ALL NOT FOUND:
  > VERBATIM RESPONSE: "No scout artifacts found for this topic. Provide a 3-5
  > sentence product description to extract requirements inline, or run
  > /scout:requirements first."

  Branch B-1 — scout-requirements N/A, at least one other LOADED:
  > VERBATIM RESPONSE: "scout-requirements not found. Requirements will be
  > extracted inline from your product description. Other loaded artifacts
  > provide context."

  Branch B-2 — scout-feasibility N/A, scout-requirements LOADED:
  > VERBATIM RESPONSE: "scout-feasibility not found. Feasibility constraints
  > noted as open questions in Phase 3."

  Branch B-3 — scout-compliance N/A, scout-requirements LOADED:
  > VERBATIM RESPONSE: "scout-compliance not found. Compliance items flagged
  > as open questions in Phase 3."

  Branch B-catch — any other partial configuration:
  > VERBATIM RESPONSE: "Partial scout coverage. Missing artifact types carry
  > [N/A - artifact missing] markers in relevant sections."

EXIT Phase 0: [SCOUT-STATUS-TABLE] complete.

---

PHASE 1 — PM PRE-ASSIGNMENT [GATE: PM-CONTRACT-SEAL]
-> ROLE: PM

ENTER Phase 1: [SCOUT-STATUS-TABLE] must be complete from Phase 0 EXIT.

You are now entering Phase 1. Your goal is to anchor every requirement to a
named spec section.

PM: scan `scout-requirements` -> extract all R-IDs and Priority levels ->
  assign each R-ID to a planned section -> populate [PM-COVERAGE-TABLE]:

  [PM-COVERAGE-TABLE]
  R-ID | Requirement Summary | Priority | Assigned Section | Waiver Status
  -----|---------------------|----------|-----------------|---------------

  Waiver Status values:
    COVERED     — R-ID maps to a named planned section.
    C-03 WAIVER — scout-requirements absent or R-ID has no traceable section.
  C-03 WAIVER rows propagate to [IG-REGISTER] as:
    Elimination Path = "R-ID WAIVED (no requirements artifact)"

CASCADE TO: [IG-REGISTER] in Phase 2 (R-IDs carried forward as inertia gap
  inputs); cross-namespace signal row in Phase 3 Purpose section (location 2
  of 2).

Cross-namespace signal (location 1 of 2):
  Signal: scout-requirements artifact confirmed for R-ID traceability.
  Source: {file path if LOADED, or INLINE}

-> EMIT [PM-CONTRACT-SEAL] WHEN [PM-COVERAGE-TABLE] fully populated.

[PM-CONTRACT-SEAL]
  INVALID IF [PM-COVERAGE-TABLE] is absent.
  INVALID IF no R-IDs are assigned in [PM-COVERAGE-TABLE].

EXIT Phase 1: emits [PM-CONTRACT-SEAL]. Cascade: [PM-COVERAGE-TABLE] R-IDs
  -> Phase 2 [IG-REGISTER]; cross-namespace signal at Phase 1.

---

PHASE 1.5 — COMPLIANCE INERTIA SCOPING [GATE: COMPLIANCE-SCOPE-SEAL]
-> ROLE: Compliance Lead

ENTER Phase 1.5: [PM-CONTRACT-SEAL] from Phase 1 must be present.

You are now entering Phase 1.5. Your goal is to evaluate the named alternatives
in [STATUS-QUO-SNAPSHOT] for compliance posture.

Compliance Lead: Review the feature's topic against known compliance domains
  (data handling, access control, audit, regulatory) -> declare the compliance
  scope for this spec:

  Compliance scope declaration:
    Compliance domains in scope: {list domain names or "none identified"}
    Status-quo compliance gaps anticipated: {brief statement or "none identified"}
    Amplification criteria note: {any compliance factor that would trigger AMPLIFIED
      status in Phase 2 [IG-REGISTER]; "none" if no compliance amplifiers apply}

-> EMIT [COMPLIANCE-SCOPE-SEAL] WHEN compliance scope declaration is complete.

[COMPLIANCE-SCOPE-SEAL]
  INVALID IF the compliance scope declaration is absent.
  INVALID IF [STATUS-QUO-SNAPSHOT] is absent from Phase 2 block.
  INVALID IF the structural fail rule — "a row with a named Alternative but a blank
    Gap statement is a structural fail, not a content gap" — is absent from within
    the [STATUS-QUO-SNAPSHOT] block definition.

EXIT Phase 1.5: emits [COMPLIANCE-SCOPE-SEAL].

---

PHASE 2 — INERTIA ANALYSIS [GATE: INERTIA-ANALYZED]
-> ROLE: PM + Compliance Lead

ENTER Phase 2: [PM-CONTRACT-SEAL] AND [COMPLIANCE-SCOPE-SEAL] required.
  -> BLOCKED: Phase 2 requires [PM-CONTRACT-SEAL] AND [COMPLIANCE-SCOPE-SEAL].

You are now entering Phase 2. Your goal is to map the forces that would cause the
status quo to persist.

PM: Populate [STATUS-QUO-SNAPSHOT] — one row per named alternative:

  [STATUS-QUO-SNAPSHOT]
  Alternative               | Gap Statement
  --------------------------|----------------------------------------------------------
  (name the alternative)    | (state what it lacks vs. this feature)

  Structural fail rule:
    A row with a named Alternative but a blank Gap statement is a structural fail,
    not a content gap. Do not leave Gap blank when Alternative is populated.

PM: For each inertia gap, add a row to [IG-REGISTER]:

  [IG-REGISTER]
  IG-ID | Inertia Gap Description | AMPLIFIED | Elimination Path
  ------|-------------------------|-----------|------------------

  Minimum 2 IG-ID rows required.

  AMPLIFIED threshold — mark AMPLIFIED = Y when EITHER:
    Condition A: The gap has a direct parallel in a named alternative from
      [STATUS-QUO-SNAPSHOT].
    Condition B: The gap blocks more than one P0 requirement from being addressed.

  AMPLIFIED Elimination Path dual sub-slot format (both required):
    Risk: [risk narrative]
    R-ID: [R-XX from [PM-COVERAGE-TABLE]]
  Partial-population structural fail: a cell with one sub-slot populated while the
  other is blank is a structural fail, not a content gap.
  Do not leave R-ID: blank when Risk: is populated.

  Standard Elimination Path: R-ID: [R-XX from [PM-COVERAGE-TABLE]]
  C-03 WAIVER rows: R-ID WAIVED (no requirements artifact)

Architect: Add resolved inertia decisions to [ID-REGISTER]:

  [ID-REGISTER]
  ID-ID | Decision | Rationale | IG-ID Resolved
  ------|----------|-----------|---------------

[INERTIA-ANALYZED]
  Condition 1: INVALID IF [STATUS-QUO-SNAPSHOT], [IG-REGISTER], or [ID-REGISTER]
    is absent from this phase block, or any required row is unpopulated.
  Condition 2: INVALID IF any [IG-REGISTER] Elimination Path cell is blank and not
    marked "R-ID WAIVED" — per-cell R-ID population required for every non-waiver row.
  Meeting Condition 1 without Condition 2 is invalid: structural completeness alone
  does not permit [INERTIA-ANALYZED] to be emitted.
  [INERTIA-ANALYZED] Condition 2 exemption: cells marked "R-ID WAIVED" are exempt
  from the per-cell R-ID check.
  Waiver chain closure — all three nodes named in sequence:
    (1) [PM-COVERAGE-TABLE] C-03 WAIVER source
    (2) "R-ID WAIVED" cell marker in [IG-REGISTER] Elimination Path
    (3) Condition 2 exemption for R-ID WAIVED cells in [INERTIA-ANALYZED]

EXIT Phase 2: emits [INERTIA-ANALYZED]. Cascade: [IG-REGISTER] -> Phase 3 Design;
  [STATUS-QUO-SNAPSHOT] Gap Statements -> Phase 3 Purpose.

---

PHASE 3 — REQUIREMENTS [GATE: SPEC-DRAFT-COMPLETE]
-> ROLE: Architect + PM

ENTER Phase 3: -> BLOCKED: Phase 3 requires [PM-CONTRACT-SEAL] AND [INERTIA-ANALYZED].

You are now entering Phase 3. Your goal is to author the specification itself.

P0 coverage count: State count before any section prose:
  "P0 requirements carried forward: {n}"

PM: scan `scout-requirements` -> scan R-01 through R-{n} -> flag contradictions.
Do not confirm "none found" without naming the scan range R-01 through R-{n}.

Cross-namespace signal (location 2 of 2):
  Signal: scout-requirements artifact confirmed for Phase 3 traceability.
  Source: {same path as location 1 of 2}

Architect: Author five sections in prescribed order:

  1. PURPOSE
     State what the feature accomplishes from user and system perspectives.
     [Cross-namespace signal (location 2 of 2) placed here.]

  2. REQUIREMENTS
     List R-IDs from [PM-COVERAGE-TABLE] with Waiver Status = COVERED (P0 first).
     Flag C-03 WAIVER rows: "[R-XX] — WAIVED: {reason}"

  3. DESIGN
     Describe architecture, data model, and key operations. Each major design
     element traces to at least one R-ID.

  4. CONSTRAINTS
     List hard constraints with scout artifact source for each.

  5. OPEN QUESTIONS
     OQ-ID | Question | Blocking Concern | Resolution Path

[SPEC-DRAFT-COMPLETE]
  INVALID IF [PM-CONTRACT-SEAL] is absent.
  INVALID IF [INERTIA-ANALYZED] is absent.
  INVALID IF scout-requirements LOADED but signal absent at location 1 of 2
    (Phase 1) or location 2 of 2 (Phase 3 Purpose section).

EXIT Phase 3: emits [SPEC-DRAFT-COMPLETE]. Cascade: spec -> Phase 4.

---

PHASE 4 — AMENDMENTS
-> ROLE: PM + Architect

ENTER Phase 4: [SPEC-DRAFT-COMPLETE] from Phase 3 must be present.

You are now in Phase 4. Your goal is to name the conditions under which this
spec would need revision.

PM: List at minimum 2 amendments. Each amendment names the target section.

  Amendment 1 — Section: [section name]: [trigger and change description]
  Amendment 2 — Section: [section name]: [trigger and change description]

EXIT Phase 4: amendment list complete.

---

FINDINGS

You have completed the spec draft. Your goal now is to review what you produced
for gaps, conflicts, and open threads.

Architect: Run self-review scan. Name what was scanned and what was found.

  Scan 1 — Coverage gaps: P0 R-IDs in [PM-COVERAGE-TABLE] without a spec section.
  Scan 2 — Contradictions: R-01 through R-{n} — conflicting requirement pairs.
  Scan 3 — Complexity hotspots: sections with disproportionate complexity vs. priority.
  Scan 4 — OQ register: all unresolved OQ-IDs at spec completion.
  Scan 5 — Cross-namespace signal: confirm present at Phase 1 (location 1) and
    Phase 3 (location 2).
  Scan 6 — Waiver chain: C-03 WAIVER rows traceable through R-ID WAIVED to
    Condition 2 exemption.

  Finding ID | Type               | Description | R-ID / OQ-ID | Resolution
  -----------|--------------------|-------------|--------------|----------
             | coverage gap       |             |              |
             | contradiction      |             |              |
             | complexity hotspot |             |              |
             | OQ register        |             |              |
```

---

## Simplification Report

### What was removed and why

| Category | Words removed | Criteria affected | Rationale |
|----------|--------------|-------------------|-----------|
| Opening preamble (skill invocation, phase-count prose, active roles legend) | ~70 | none | Orientational prose; phases are self-labeling; roles established by → ROLE: markers (C-43) |
| Phase 0 ENTER trailer: "Phase 0 begins at invocation." | ~5 | none | ENTER already declares "No preconditions" — redundant |
| Phase 1 goal elaboration: "The assignment table is your contract with Phase 3 — scope that is not in the table will not be in the spec." | ~22 | none | No criterion requires motivational framing in the goal sentence |
| Phase 1 table parenthetical: "(one row per R-ID; Waiver Status = COVERED or C-03 WAIVER)" | ~14 | none | C-03 enumeration is fully satisfied by the Waiver Status values block immediately below |
| Phase 1 seal emphasis: "Both structural dependencies must be satisfied; neither alone is sufficient." | ~10 | none | C-17 is satisfied by the two INVALID IF lines; C-12 is about [INERTIA-ANALYZED], not [PM-CONTRACT-SEAL] |
| Phase 1.5 goal elaboration: "(which will be populated in Phase 2) … establishing which alternatives … Phase 2 cannot begin until this scope is sealed." | ~31 | none | No criterion requires this; C-42 is satisfied by "You are now entering Phase 1.5. Your goal is to evaluate…" |
| Phase 1.5 EXIT cascade: "Cascade: compliance scope flows to Phase 2…" | ~14 | none | C-41 explicitly excludes fractional sub-phases; cascade not required in Phase 1.5 EXIT |
| Phase 2 orientation: "You will work in three blocks: snapshot the alternatives first, then log the gaps, then record the decisions." | ~19 | none | Pure navigational prose; no criterion |
| Phase 2 STATUS-QUO PM description: "Each row names the alternative and states the gap that makes it inadequate:" | ~13 | none | Table headers + structural fail rule make this redundant; C-27 actor→action form preserved |
| Phase 2 compliance note: "Compliance note: apply [COMPLIANCE-SCOPE-SEAL] amplification criteria when evaluating Condition A…" | ~24 | none | C-40 is satisfied by [COMPLIANCE-SCOPE-SEAL]'s INVALID IF rule; this Phase 2 body note is supplementary |
| Phase 2 ENTER condensation: "from Phase 1 AND [COMPLIANCE-SCOPE-SEAL] from Phase 1.5 must both be present" → "AND [COMPLIANCE-SCOPE-SEAL] required" | ~8 | none | C-47 requires both tokens named in ENTER block (satisfied); from-phase provenance redundant with EXIT block labeling |
| Phase 3 ENTER condensation: two-line form → single BLOCKED line | ~10 | none | C-19 (blocked statement) and C-44 (chain: names [INERTIA-ANALYZED]) both satisfied by the single BLOCKED line; no C-47 dependency at Phase 3 |
| Phase 3 goal elaboration: "Everything you write here must trace back to what was established in Phases 1 and 2 — the assignment table and inertia decisions become a design." | ~27 | none | No criterion |
| Phase 3 PURPOSE section instruction: "Connect to inertia decisions in Phase 2 and name at least one status-quo alternative…" | ~22 | none | C-22 is satisfied by "[Cross-namespace signal (location 2 of 2) placed here.]"; no criterion requires PURPOSE body instructions beyond signal placement |
| Phase 3 DESIGN section instruction: "Name the design decision that closes each AMPLIFIED gap in [IG-REGISTER]." | ~13 | none | No criterion |
| Phase 3 CONSTRAINTS section instruction: "Flag any constraint surfaced by [COMPLIANCE-SCOPE-SEAL] compliance scope declaration." | ~10 | none | No criterion |
| Phase 3/4 EXIT cascade verbosity: verbose → arrow notation | ~12 | none | C-41 satisfied by token names; cascade descriptions trimmed not eliminated |
| Phase 4 goal elaboration: "not to revise it now, but to make future amendment paths explicit." | ~12 | none | C-42 satisfied by "Your goal is to name the conditions…" alone |
| Phase 4 EXIT trailer: "Spec artifact ready for FINDINGS review." | ~6 | none | C-44 terminal artifact requirement satisfied by "amendment list complete" |
| FINDINGS Scan 7 (compliance scope coverage) | ~14 | none | C-29 minimum 6 satisfied by scans 1–6; scan 7 was above minimum |
| FINDINGS Scan 8 (status-quo displacement) | ~14 | none | Same — above the C-29 minimum; scan 8 is supplementary |

### Criteria verification — all 47 pass

**Essential (5/5):** C-01 phases in order ✓ · C-02 7-row SCOUT-STATUS-TABLE ✓ · C-03 Waiver Status with enumerated values ✓ · C-04 [IG-REGISTER]+[ID-REGISTER] min 2 rows ✓ · C-05 five Phase 3 sections in order ✓

**Recommended (3/3):** C-06 all fallback branches ✓ · C-07 VERBATIM blocks in all branches ✓ · C-08 all three named gate tokens with INVALID IF ✓

**Aspirational — extension clusters intact:**
- STATUS-QUO cluster: C-36/C-37/C-45/C-46 ✓ ([STATUS-QUO-SNAPSHOT] structural fail rule dual-form; Condition 1 scoped to "this phase block")
- Phase 1.5 cluster: C-38/C-39/C-40 ✓ (Phase 1.5 header with ordinal+role; [COMPLIANCE-SCOPE-SEAL] cross-referencing structural fail rule by name)
- ENTER/EXIT ceremony: C-41/C-44/C-47 ✓ (five numbered phases; unbroken chain; Phase 2 ENTER names both [PM-CONTRACT-SEAL] AND [COMPLIANCE-SCOPE-SEAL] as distinct line from BLOCKED)
- Style: C-42/C-43 ✓ (second-person in 7 phases; → ROLE: markers at all entries)
- Traceability/governance: C-09–C-35 ✓ (waiver chain, cross-namespace signals, gate dependencies, scan instructions — all structural elements preserved)

```json
{"simplified_word_count": 1452, "original_word_count": 1841, "all_essential_still_pass": true}
```
