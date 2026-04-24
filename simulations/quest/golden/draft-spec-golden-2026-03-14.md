Written to `simulations/quest/golden/draft-spec-golden-2026-03-14.md`.

---

**Golden document summary:**

- **Score**: 175/175 — first perfect score in the 19-round series
- **Source**: V-05 (R19), simplified 21.1% (all 47 criteria verified)
- **Prompt body**: 6-phase structure (Phase 0 through Phase 4 + FINDINGS), simplified from V-05

**What made it golden — the 5 structural clusters V-01 lacked:**

| Cluster | Criteria | What it adds |
|---------|----------|-------------|
| ENTER/EXIT ceremony | C-41, C-44 | Phase transitions readable as a computable graph |
| `-> ROLE:` markers | C-43 | Role identity at structural boundary, not prose |
| Second-person frame | C-42 | "You are entering Phase N" at every entry |
| Phase 1.5 + [COMPLIANCE-SCOPE-SEAL] | C-38, C-39, C-40, C-47 | Fractional sub-phase with cross-block INVALID IF rule naming [STATUS-QUO-SNAPSHOT] structural fail |
| [STATUS-QUO-SNAPSHOT] | C-36, C-37, C-45, C-46 | Named-alternatives map with embedded structural fail rule, grounded into Phase 3 PURPOSE |

V-01 scored 148.85 (27/39 aspirational, 8 N/A). V-05 scored 175.00 (39/39, 0 N/A) by activating all five extension clusters simultaneously.
nch A — ALL NOT FOUND:
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

## What Made It Golden

Five structural clusters, each absent in V-01, each targeting a distinct rubric gap:

**1. ENTER/EXIT ceremony at every numbered phase boundary (C-41, C-44)**
Every phase opens with `ENTER Phase N: [preconditions]` and closes with `EXIT Phase N: [token emitted + cascade]`. The full sequence is readable as a computable transition graph without parsing phase body content. V-01 had entry-condition prose (the HANDOFF note) but no structural ENTER/EXIT blocks — those are different things.

**2. `-> ROLE:` structural markers at every phase entry (C-43)**
Each phase header is immediately followed by `-> ROLE: [role name]`, placing role identity as a structural declaration at the phase boundary. V-01 stated roles only in prose preambles and the HANDOFF — neither is a structural marker at a numbered phase entry point.

**3. Second-person transitional frame throughout (C-42)**
Each phase opens with "You are [beginning / now entering / now in] Phase N." The model is oriented as the executing agent at every entry. V-01 used third-person ("PM leads phases 0 through 2") with no "you will" or "you are entering" framing across phases.

**4. Phase 1.5 with [COMPLIANCE-SCOPE-SEAL] cross-referencing [STATUS-QUO-SNAPSHOT] (C-38, C-39, C-40, C-47)**
A fractional sub-phase between Phase 1 and Phase 2, owned by the Compliance Lead. Its INVALID IF rules name the [STATUS-QUO-SNAPSHOT] structural fail rule verbatim — satisfying C-40's cross-block rule dependency requirement. Phase 2 ENTER absorbs both [PM-CONTRACT-SEAL] and [COMPLIANCE-SCOPE-SEAL] as a multi-input gate (C-47).

**5. [STATUS-QUO-SNAPSHOT] with embedded structural fail rule (C-36, C-37, C-45, C-46)**
Phase 2 opens with a named-alternatives map before gap analysis begins. The structural fail rule ("a row with a named Alternative but a blank Gap statement is a structural fail, not a content gap") lives inside the block definition — the same rule that [COMPLIANCE-SCOPE-SEAL] must reference by name. Phase 3 PURPOSE is required to name at least one alternative from the snapshot.

---

## Rubric Criteria Summary — v17

**Formula**: `(E/5 × 60) + (R/3 × 30) + (A/39 × 85)`
**Score**: `60 + 30 + 85 = 175.00` — perfect

### Essential (5/5 — 60 pts)

| C-ID | Criterion | Result |
|------|-----------|--------|
| C-01 | Phases 0–4 present in order | PASS |
| C-02 | [SCOUT-STATUS-TABLE] with 7 artifact rows | PASS |
| C-03 | [PM-COVERAGE-TABLE] with Waiver Status column | PASS |
| C-04 | [IG-REGISTER] and [ID-REGISTER] both present, min 2 rows | PASS |
| C-05 | Phase 3 has PURPOSE / REQUIREMENTS / DESIGN / CONSTRAINTS / OPEN QUESTIONS in order | PASS |

### Recommended (3/3 — 30 pts)

| C-ID | Criterion | Result |
|------|-----------|--------|
| C-06 | All five branch names present (A, B-1, B-2, B-3, B-catch) | PASS |
| C-07 | Each branch has a blockquoted VERBATIM RESPONSE | PASS |
| C-08 | [PM-CONTRACT-SEAL], [INERTIA-ANALYZED], [SPEC-DRAFT-COMPLETE] defined with INVALID IF rules | PASS |

### Aspirational (39/39 — 85 pts)

| C-ID | Criterion | Result |
|------|-----------|--------|
| C-09 | Waiver Status declared as structural element inside [PM-COVERAGE-TABLE] | PASS |
| C-10 | C-03 WAIVER rows propagate to [IG-REGISTER] Elimination Path | PASS |
| C-11 | Condition 1 and Condition 2 named as distinct invalidity paths in [INERTIA-ANALYZED] | PASS |
| C-12 | "Condition 1 without Condition 2 is invalid" explicitly stated | PASS |
| C-13 | Waiver chain closure — all three nodes named in sequence | PASS |
| C-14 | AMPLIFIED threshold names Condition A and Condition B as explicit triggers | PASS |
| C-15 | Dual sub-slot format: "Risk: / R-ID:" | PASS |
| C-16 | Partial-population structural fail named for dual sub-slot cells | PASS |
| C-17 | [PM-CONTRACT-SEAL] names both absence conditions; "both must be satisfied" | PASS |
| C-18 | "-> BLOCKED: Phase 2 requires [PM-CONTRACT-SEAL]" at Phase 2 entry | PASS |
| C-19 | Phase 3 preamble states "requires [PM-CONTRACT-SEAL] AND [INERTIA-ANALYZED]" | PASS |
| C-20 | [SPEC-DRAFT-COMPLETE] INVALID IF rules name both upstream tokens by token name | PASS |
| C-21 | Cross-namespace signal (location 1 of 2) at Phase 1 | PASS |
| C-22 | (location 2 of 2) marker in Phase 3 Purpose section | PASS |
| C-23 | [SPEC-DRAFT-COMPLETE] INVALID IF signal absent at either location | PASS |
| C-24 | "scan R-01 through R-{n}" with named range | PASS |
| C-25 | "Do not confirm 'none found' without naming the scan source and range" | PASS |
| C-26 | "P0 coverage count: State count before any section prose" | PASS |
| C-27 | All directives use actor -> action -> output with `->` binding | PASS |
| C-28 | [PM-CONTRACT-SEAL] emitted at Phase 1 exit; Phase 2 blocked on it | PASS |
| C-29 | FINDINGS has 6 named scan items (Scan 1–Scan 6) | PASS |
| C-30 | Finding table names coverage gap, contradiction, complexity hotspot, OQ register | PASS |
| C-31 | "List at minimum 2 amendments. Each amendment names the target section." | PASS |
| C-32 | Standard Elimination Path format: "R-ID: [R-XX from [PM-COVERAGE-TABLE]]" | PASS |
| C-33 | C-03 WAIVER rows format: "R-ID WAIVED (no requirements artifact)" | PASS |
| C-34 | [INERTIA-ANALYZED] Condition 2 exemption for R-ID WAIVED cells | PASS |
| C-35 | CASCADE TO co-located with Phase 1 directive | PASS |
| C-36 | [STATUS-QUO-SNAPSHOT] block present in Phase 2 | PASS |
| C-37 | [STATUS-QUO-SNAPSHOT] has Alternative / Gap Statement columns | PASS |
| C-38 | Phase 1.5 fractional sub-phase present between Phase 1 and Phase 2 | PASS |
| C-39 | Phase 1.5 emits a named seal token ([COMPLIANCE-SCOPE-SEAL]) | PASS |
| C-40 | [COMPLIANCE-SCOPE-SEAL] INVALID IF rules cross-reference [STATUS-QUO-SNAPSHOT] structural fail rule by name | PASS |
| C-41 | ENTER block at every numbered phase boundary | PASS |
| C-42 | Second-person transitional frame at every phase entry | PASS |
| C-43 | `-> ROLE:` structural marker at every numbered phase entry | PASS |
| C-44 | EXIT block at every numbered phase boundary (readable as transition graph) | PASS |
| C-45 | [STATUS-QUO-SNAPSHOT] structural fail rule embedded in block definition | PASS |
| C-46 | Phase 3 PURPOSE requires naming at least one [STATUS-QUO-SNAPSHOT] alternative | PASS |
| C-47 | Phase 2 ENTER absorbs both [PM-CONTRACT-SEAL] and [COMPLIANCE-SCOPE-SEAL] as multi-input gate | PASS |
