# draft-spec Variate — Round 19

Rubric version: v17 · Formula: (E/5×60) + (R/3×30) + (A/39×85) · No new criteria from R17.

Single-axis variations (V-01..V-03), then combinations (V-04..V-05).

**Axes explored:**
- **V-01**: Role sequence — post-hoc Architect (PM leads phases 0-2, explicit HANDOFF TO ARCHITECT at Phase 3 boundary, joint Phase 4 + FINDINGS)
- **V-02**: Output format — numbered checklist (hierarchical 1.1.1 notation; every block, gate, and directive expressed as a numbered list item)
- **V-03**: Phrasing register — MUST/SHALL modal (all structural requirements and directives use MUST/SHALL/SHALL NOT; actor→action `→` binding preserved for C-27)
- **V-04**: Lifecycle emphasis + Inertia framing — competition-first Phase 2 framing ([STATUS-QUO-SNAPSHOT] opens Phase 2 as an explicit competitor map before gap analysis begins; STATUS-QUO cluster C-36/C-37/C-45/C-46 active)
- **V-05**: Full five-cluster extension — Compliance Lead Phase 1.5 + [COMPLIANCE-SCOPE-SEAL] (C-38/C-39/C-40/C-47) + ENTER/EXIT ceremony (C-41/C-44) + second-person frame (C-42) + ROLE markers (C-43) + STATUS-QUO cluster (C-36/C-37/C-45/C-46) targeting 175/175

**Predicted scores:**

| Variation | A-pass | A-fail | A-N/A | Composite |
|-----------|--------|--------|-------|-----------|
| V-01 | 27 | 4 | 8 | **148.85** |
| V-02 | 27 | 4 | 8 | **148.85** |
| V-03 | 27 | 4 | 8 | **148.85** |
| V-04 | 31 | 4 | 4 | **157.56** |
| V-05 | 39 | 0 | 0 | **175.00** |

Aspirational N/A breakdown:
- V-01/V-02/V-03: C-36, C-37, C-38, C-39, C-40, C-45, C-46, C-47 (no STATUS-QUO, no Phase 1.5)
- V-04: C-38, C-39, C-40, C-47 (no Phase 1.5; STATUS-QUO cluster active)
- V-05: none (all five extension clusters active)

Aspirational fails (non-N/A):
- V-01/V-02/V-03: C-41, C-42, C-43, C-44 (no ceremony, no second-person, no ROLE markers)
- V-04: C-41, C-42, C-43, C-44 (STATUS-QUO cluster only; no ceremony)
- V-05: none

---

## V-01 — Post-Hoc Architect Role Sequence | Axis: Role Sequence | No extension clusters

**Hypothesis**: Making the PM-to-Architect handoff structurally explicit — PM owns phases 0-2,
a labeled HANDOFF statement opens Phase 3, Architect owns all five sections — tests whether
rubric scoring changes when role boundaries are declared at the phase boundary level rather
than embedded within phases via actor→action directives alone. All essential + recommended
pass. Aspirational pass rate identical to any non-extension baseline (27/39) because no
extension clusters are active and C-41/C-42/C-43/C-44 require structural elements absent
from this variation. Score: **148.85**.

```
You are running /draft:spec. PM leads phases 0 through 2 (discovery and analysis).
At Phase 3 an explicit handoff transfers ownership to the Architect for spec authoring.
Both roles collaborate on Phase 4 and FINDINGS.

---

PHASE 0 — SCOUT ARTIFACT DISCOVERY

PM: Scan the workspace for scout artifacts related to the topic. Populate
[SCOUT-STATUS-TABLE]:

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

PM: Evaluate table. Execute the first matching branch:

  Branch A — ALL NOT FOUND:
  > VERBATIM RESPONSE: "No scout artifacts found for this topic. Provide a 3-5
  > sentence product description to proceed, or run /scout:requirements first."

  Branch B-1 — scout-requirements N/A, at least one other artifact LOADED:
  > VERBATIM RESPONSE: "scout-requirements not found. Requirements will be
  > extracted inline from your product description. Other loaded artifacts
  > provide context."

  Branch B-2 — scout-feasibility N/A, scout-requirements LOADED:
  > VERBATIM RESPONSE: "scout-feasibility not found. Feasibility constraints
  > will be noted as open questions in Phase 3 Section 5. Spec proceeds
  > without feasibility scoring."

  Branch B-3 — scout-compliance N/A, scout-requirements LOADED:
  > VERBATIM RESPONSE: "scout-compliance not found. Compliance requirements
  > will be flagged as open questions in Phase 3 Section 5. Spec proceeds
  > without compliance gating."

  Branch B-catch — any other partial configuration:
  > VERBATIM RESPONSE: "Partial scout coverage detected. Missing artifact types
  > carry an [N/A - artifact missing] marker in relevant sections."

---

PHASE 1 — PM PRE-ASSIGNMENT [GATE: PM-CONTRACT-SEAL]

PM: scan `scout-requirements` → extract all R-IDs and Priority levels →
  assign each R-ID to a planned spec section → populate [PM-COVERAGE-TABLE]:

  [PM-COVERAGE-TABLE]
  R-ID | Requirement Summary | Priority | Assigned Section | Waiver Status
  -----|---------------------|----------|-----------------|---------------
  (one row per R-ID; Waiver Status = COVERED or C-03 WAIVER)

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

→ EMIT [PM-CONTRACT-SEAL] WHEN [PM-COVERAGE-TABLE] is fully populated with
  all R-IDs assigned and Waiver Status declared for every row.

[PM-CONTRACT-SEAL]
  INVALID IF [PM-COVERAGE-TABLE] is absent.
  INVALID IF no R-IDs are assigned in [PM-COVERAGE-TABLE].
  Both structural dependencies must be satisfied; neither alone is sufficient.

→ BLOCKED: Phase 2 requires [PM-CONTRACT-SEAL].

---

PHASE 2 — INERTIA ANALYSIS [GATE: INERTIA-ANALYZED]

→ BLOCKED: Phase 2 requires [PM-CONTRACT-SEAL].

PM: For each risk that the status quo will persist and this feature will not be
  adopted, add a row to [IG-REGISTER]:

  [IG-REGISTER]
  IG-ID | Inertia Gap Description | AMPLIFIED | Elimination Path
  ------|-------------------------|-----------|------------------

  Minimum 2 IG-ID rows required.

  AMPLIFIED threshold — mark AMPLIFIED = Y when EITHER condition is true:
    Condition A: The gap has a direct parallel in a named competing solution.
    Condition B: The gap blocks more than one P0 requirement from being addressed.

  AMPLIFIED Elimination Path uses dual sub-slot format — both sub-slots required:
    Risk: [risk narrative]
    R-ID: [R-XX from [PM-COVERAGE-TABLE]]
  Partial-population structural fail: a cell in which one sub-slot is populated
  while the other is blank is a structural fail, not a content gap.

  Standard Elimination Path format: R-ID: [R-XX from [PM-COVERAGE-TABLE]]
  C-03 WAIVER rows: R-ID WAIVED (no requirements artifact)

PM: Add resolved inertia decisions to [ID-REGISTER]:

  [ID-REGISTER]
  ID-ID | Decision | Rationale | IG-ID Resolved
  ------|----------|-----------|---------------

[INERTIA-ANALYZED]
  Condition 1: INVALID IF [IG-REGISTER] or [ID-REGISTER] is absent, or any
    required row is unpopulated.
  Condition 2: INVALID IF any [IG-REGISTER] Elimination Path cell is blank
    and not marked "R-ID WAIVED" — per-cell R-ID population required for every
    non-waiver row.
  Meeting Condition 1 without Condition 2 is invalid: structural completeness
  alone does not permit [INERTIA-ANALYZED] to be emitted.
  [INERTIA-ANALYZED] Condition 2 exemption: cells marked "R-ID WAIVED" are
  exempt from the per-cell R-ID check.
  Waiver chain closure — all three nodes named in sequence:
    (1) [PM-COVERAGE-TABLE] C-03 WAIVER source
    (2) "R-ID WAIVED" cell marker in [IG-REGISTER] Elimination Path
    (3) Condition 2 exemption for R-ID WAIVED cells in [INERTIA-ANALYZED]

---

HANDOFF TO ARCHITECT — Phase 3 requires [PM-CONTRACT-SEAL] AND [INERTIA-ANALYZED].
PM has completed discovery and analysis. Architect takes ownership for spec authoring.

---

PHASE 3 — REQUIREMENTS [GATE: SPEC-DRAFT-COMPLETE]

→ BLOCKED: Phase 3 requires [PM-CONTRACT-SEAL] AND [INERTIA-ANALYZED].

P0 coverage count: State the count of P0 requirements carried forward before any
section prose: "P0 requirements carried forward: {n}"

PM: scan `scout-requirements` → scan R-01 through R-{n} → flag contradictions.
Do not confirm "none found" without naming the scan range R-01 through R-{n}.

Cross-namespace signal (location 2 of 2):
  Signal: scout-requirements artifact confirmed for Phase 3 traceability.
  Source: {same path as location 1 of 2}

Architect: Author each section in prescribed order:

  1. PURPOSE
     State what the feature accomplishes from user and system perspectives.
     Connect to inertia decisions in Phase 2 where the spec resolves a named gap.
     [Cross-namespace signal (location 2 of 2) field placed here.]

  2. REQUIREMENTS
     List all R-IDs from [PM-COVERAGE-TABLE] with Waiver Status = COVERED,
     grouped by Priority (P0 first). Flag C-03 WAIVER rows:
     "[R-XX] — WAIVED: {reason}"

  3. DESIGN
     Describe solution architecture, data model, and key operations. Each major
     design element must trace to at least one R-ID.

  4. CONSTRAINTS
     List hard constraints (platform, performance, compliance) with scout artifact
     source. Each constraint names its origin: {scout artifact path or INLINE}.

  5. OPEN QUESTIONS
     List unresolved questions with OQ-IDs. Each OQ names the blocking concern
     and the information needed to resolve it.
     OQ-ID | Question | Blocking Concern | Resolution Path

[SPEC-DRAFT-COMPLETE]
  INVALID IF [PM-CONTRACT-SEAL] is absent.
  INVALID IF [INERTIA-ANALYZED] is absent.
  INVALID IF scout-requirements is LOADED but cross-namespace signal is absent at
    location 1 of 2 (Phase 1) or location 2 of 2 (Phase 3 Purpose section).

---

PHASE 4 — AMENDMENTS

PM + Architect: Jointly list at minimum 2 amendments. Each amendment names the
target section.

  Amendment 1 — Section: [section name]: [trigger and change description]
  Amendment 2 — Section: [section name]: [trigger and change description]

---

FINDINGS

Architect: Run self-review scan. Name what was scanned and what was found.

  Scan 1 — Coverage gaps: P0 R-IDs in [PM-COVERAGE-TABLE] without a spec section.
  Scan 2 — Contradictions: R-01 through R-{n} — any conflicting requirement pairs.
  Scan 3 — Complexity hotspots: sections with disproportionate complexity vs. priority.
  Scan 4 — OQ register: all unresolved OQ-IDs at spec completion.
  Scan 5 — Cross-namespace signal: confirm signal present at Phase 1 and Phase 3.
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

## V-02 — Numbered Checklist Format | Axis: Output Format | No extension clusters

**Hypothesis**: Expressing every block, gate, and directive as a hierarchical numbered
checklist item (1.1.1 depth notation) changes the processing surface without changing
criterion presence. A model filling 4.4.1/4.4.2/4.4.3/4.4.4/4.4.5 labeled section stubs
should satisfy C-05 identically to prose-labeled sections. All essential + recommended
pass; aspirational pass rate identical to non-extension baseline (27/39). Score: **148.85**.

```
You are running /draft:spec. Populate each numbered item below in sequence.
Active roles: PM (requirements traceability), Architect (spec authoring).

---

1. PHASE 0 — SCOUT ARTIFACT DISCOVERY

   1.1 PM: scan workspace → populate [SCOUT-STATUS-TABLE]:

       [SCOUT-STATUS-TABLE]
       1.1.1 scout-requirements   | LOADED / N/A | {file path}
       1.1.2 scout-feasibility    | LOADED / N/A | {file path}
       1.1.3 scout-compliance     | LOADED / N/A | {file path}
       1.1.4 scout-market         | LOADED / N/A | {file path}
       1.1.5 scout-stakeholders   | LOADED / N/A | {file path}
       1.1.6 scout-naming         | LOADED / N/A | {file path}
       1.1.7 scout-positioning    | LOADED / N/A | {file path}

   1.2 PM: evaluate table → execute first matching branch:

       1.2.1 Branch A — ALL NOT FOUND:
             > VERBATIM RESPONSE: "No scout artifacts found for this topic.
             > Provide a 3-5 sentence product description to proceed, or run
             > /scout:requirements first."

       1.2.2 Branch B-1 — scout-requirements N/A, at least one other LOADED:
             > VERBATIM RESPONSE: "scout-requirements not found. Requirements
             > will be extracted inline from your product description. Other
             > loaded artifacts provide context."

       1.2.3 Branch B-2 — scout-feasibility N/A, scout-requirements LOADED:
             > VERBATIM RESPONSE: "scout-feasibility not found. Feasibility
             > constraints will be noted as open questions in Phase 3 Section 5."

       1.2.4 Branch B-3 — scout-compliance N/A, scout-requirements LOADED:
             > VERBATIM RESPONSE: "scout-compliance not found. Compliance items
             > will be flagged as open questions in Phase 3 Section 5."

       1.2.5 Branch B-catch — any other partial configuration:
             > VERBATIM RESPONSE: "Partial scout coverage. Missing artifact types
             > carry [N/A - artifact missing] markers in relevant sections."

---

2. PHASE 1 — PM PRE-ASSIGNMENT [GATE: PM-CONTRACT-SEAL]

   2.1 PM: scan `scout-requirements` → extract R-IDs and Priority levels →
       assign each to a planned section → populate [PM-COVERAGE-TABLE]:

       [PM-COVERAGE-TABLE]
       R-ID | Requirement Summary | Priority | Assigned Section | Waiver Status
       -----|---------------------|----------|-----------------|---------------
       (one row per R-ID)

   2.2 Waiver Status values:
       2.2.1 COVERED     — R-ID maps to a named planned section.
       2.2.2 C-03 WAIVER — scout-requirements absent or R-ID has no traceable section.
       2.2.3 C-03 WAIVER rows → [IG-REGISTER] Elimination Path:
             "R-ID WAIVED (no requirements artifact)"

   2.3 CASCADE TO:
       2.3.1 [IG-REGISTER] in Phase 2 (R-IDs as inertia gap inputs).
       2.3.2 Cross-namespace signal in Phase 3 Purpose section (location 2 of 2).

   2.4 Cross-namespace signal (location 1 of 2):
       Signal: scout-requirements confirmed for R-ID traceability.
       Source: {file path if LOADED, or INLINE}

   2.5 → EMIT [PM-CONTRACT-SEAL] WHEN [PM-COVERAGE-TABLE] fully populated.
       [PM-CONTRACT-SEAL]
       2.5.1 INVALID IF [PM-COVERAGE-TABLE] is absent.
       2.5.2 INVALID IF no R-IDs assigned in [PM-COVERAGE-TABLE].
       2.5.3 Both dependencies must be satisfied; neither alone is sufficient.

   2.6 → BLOCKED: Phase 2 requires [PM-CONTRACT-SEAL].

---

3. PHASE 2 — INERTIA ANALYSIS [GATE: INERTIA-ANALYZED]

   3.0 → BLOCKED: Phase 2 requires [PM-CONTRACT-SEAL].

   3.1 PM: populate [IG-REGISTER] — one row per inertia gap. Minimum 2 IG-ID rows.

       [IG-REGISTER]
       IG-ID | Inertia Gap Description | AMPLIFIED | Elimination Path
       ------|-------------------------|-----------|------------------

   3.2 AMPLIFIED threshold — mark AMPLIFIED = Y when EITHER:
       3.2.1 The gap has a direct parallel in a named competing solution.
       3.2.2 The gap blocks more than one P0 requirement from being addressed.

   3.3 AMPLIFIED Elimination Path — dual sub-slot format (both required):
       3.3.1 Risk: [risk narrative]
       3.3.2 R-ID: [R-XX from [PM-COVERAGE-TABLE]]
       3.3.3 Partial-population structural fail: one sub-slot populated + one blank
             = structural fail, not a content gap.

   3.4 Standard Elimination Path: R-ID: [R-XX from [PM-COVERAGE-TABLE]]
   3.5 C-03 WAIVER rows: R-ID WAIVED (no requirements artifact)

   3.6 Architect: populate [ID-REGISTER]:

       [ID-REGISTER]
       ID-ID | Decision | Rationale | IG-ID Resolved
       ------|----------|-----------|---------------

   3.7 [INERTIA-ANALYZED]
       3.7.1 Condition 1: INVALID IF [IG-REGISTER] or [ID-REGISTER] absent, or any
             required row unpopulated.
       3.7.2 Condition 2: INVALID IF any Elimination Path cell blank and not marked
             "R-ID WAIVED" — per-cell R-ID population required for every non-waiver row.
       3.7.3 Meeting Condition 1 without Condition 2 is invalid.
       3.7.4 Condition 2 exemption: "R-ID WAIVED" cells exempt from per-cell check.
       3.7.5 Waiver chain closure — all three nodes in sequence:
             (1) [PM-COVERAGE-TABLE] C-03 WAIVER source
             (2) "R-ID WAIVED" cell in [IG-REGISTER] Elimination Path
             (3) Condition 2 exemption in [INERTIA-ANALYZED]

   3.8 → BLOCKED: Phase 3 requires [PM-CONTRACT-SEAL] AND [INERTIA-ANALYZED].

---

4. PHASE 3 — REQUIREMENTS [GATE: SPEC-DRAFT-COMPLETE]

   4.0 → BLOCKED: Phase 3 requires [PM-CONTRACT-SEAL] AND [INERTIA-ANALYZED].

   4.1 P0 coverage count (state before any section prose):
       "P0 requirements carried forward: {n}"

   4.2 PM: scan `scout-requirements` → scan R-01 through R-{n} → flag contradictions.
       Do not confirm "none found" without naming the scan range.

   4.3 Cross-namespace signal (location 2 of 2):
       Signal: scout-requirements confirmed for Phase 3 traceability.
       Source: {same path as location 1 of 2}

   4.4 Architect: author five sections in prescribed order:

       4.4.1 PURPOSE
             State what the feature accomplishes from user and system perspectives.
             Connect to Phase 2 inertia decisions where the spec resolves a named gap.
             [Cross-namespace signal (location 2 of 2) placed here.]

       4.4.2 REQUIREMENTS
             List R-IDs from [PM-COVERAGE-TABLE] with Waiver Status = COVERED (P0 first).
             Flag C-03 WAIVER rows: "[R-XX] — WAIVED: {reason}"

       4.4.3 DESIGN
             Describe solution architecture, data model, and key operations. Each
             major design element traces to at least one R-ID.

       4.4.4 CONSTRAINTS
             List hard constraints with scout artifact source for each.

       4.4.5 OPEN QUESTIONS
             OQ-ID | Question | Blocking Concern | Resolution Path

   4.5 [SPEC-DRAFT-COMPLETE]
       4.5.1 INVALID IF [PM-CONTRACT-SEAL] is absent.
       4.5.2 INVALID IF [INERTIA-ANALYZED] is absent.
       4.5.3 INVALID IF scout-requirements LOADED but signal absent at location 1 or 2.

---

5. PHASE 4 — AMENDMENTS

   5.1 List at minimum 2 amendments. Each amendment names the target section:
       5.1.1 Amendment 1 — Section: [section name]: [trigger and change description]
       5.1.2 Amendment 2 — Section: [section name]: [trigger and change description]

---

6. FINDINGS

   6.1 Architect: run self-review scan. Name what was scanned and what was found.
       6.1.1 Coverage gaps: P0 R-IDs in [PM-COVERAGE-TABLE] without a spec section.
       6.1.2 Contradictions: R-01 through R-{n} — conflicting requirement pairs.
       6.1.3 Complexity hotspots: sections with disproportionate complexity vs. priority.
       6.1.4 OQ register: all unresolved OQ-IDs at spec completion.
       6.1.5 Cross-namespace signal: confirm present at Phase 1 and Phase 3.
       6.1.6 Waiver chain: C-03 WAIVER → R-ID WAIVED → Condition 2 exemption.

   6.2 Findings table:
       Finding ID | Type               | Description | R-ID / OQ-ID | Resolution
       -----------|--------------------|-------------|--------------|----------
                  | coverage gap       |             |              |
                  | contradiction      |             |              |
                  | complexity hotspot |             |              |
                  | OQ register        |             |              |
```

---

## V-03 — MUST/SHALL Modal Register | Axis: Phrasing Register | No extension clusters

**Hypothesis**: Replacing imperative prose directives with MUST/SHALL/SHALL NOT modal
language (compliance-style register) while preserving the actor→action `→` binding
(C-27 precondition) tests whether the modal register satisfies or conflicts with rubric
criteria. C-27 passes because "PM: MUST scan `scout-requirements` →" retains the
actor→action→output form with `→` binding. C-42 fails (no second-person framing;
formal modal register is orthogonal to orientation prose). All other non-extension
criteria pass. Score: **148.85**.

```
You are running /draft:spec. All structural requirements and transition conditions
below use MUST/SHALL/SHALL NOT modal language. Actor-action directives retain the
"PM: scan `scout-requirements` ->" form. Active roles: PM (requirements
traceability), Architect (spec authoring).

---

PHASE 0 — SCOUT ARTIFACT DISCOVERY

PM: MUST scan the workspace for scout artifacts related to the topic.
[SCOUT-STATUS-TABLE] MUST contain exactly 7 rows covering the following artifact types:

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

PM: MUST evaluate the table and execute the first matching branch. No branch
SHALL be skipped or merged.

  Branch A — ALL NOT FOUND:
  > VERBATIM RESPONSE: "No scout artifacts found for this topic. You MUST provide
  > a 3-5 sentence product description to proceed, or run /scout:requirements first."

  Branch B-1 — scout-requirements N/A, at least one other artifact LOADED:
  > VERBATIM RESPONSE: "scout-requirements not found. Requirements will be extracted
  > inline from your product description. Other loaded artifacts provide context."

  Branch B-2 — scout-feasibility N/A, scout-requirements LOADED:
  > VERBATIM RESPONSE: "scout-feasibility not found. Feasibility constraints will be
  > noted as open questions in Phase 3 Section 5. Spec SHALL proceed without
  > feasibility scoring."

  Branch B-3 — scout-compliance N/A, scout-requirements LOADED:
  > VERBATIM RESPONSE: "scout-compliance not found. Compliance requirements will be
  > flagged as open questions in Phase 3 Section 5. Spec SHALL proceed without
  > compliance gating."

  Branch B-catch — any other partial configuration:
  > VERBATIM RESPONSE: "Partial scout coverage detected. Missing artifact types SHALL
  > carry an [N/A - artifact missing] marker in all relevant sections."

---

PHASE 1 — PM PRE-ASSIGNMENT [GATE: PM-CONTRACT-SEAL]

PM: MUST scan `scout-requirements` -> extract all R-IDs and Priority levels ->
  assign each R-ID to a planned spec section -> populate [PM-COVERAGE-TABLE].
[PM-COVERAGE-TABLE] MUST include a Waiver Status column with enumerated values:

  [PM-COVERAGE-TABLE]
  R-ID | Requirement Summary | Priority | Assigned Section | Waiver Status
  -----|---------------------|----------|-----------------|---------------
  (one row per R-ID; Waiver Status = COVERED or C-03 WAIVER)

  Waiver Status values:
    COVERED     — R-ID maps to a named planned section.
    C-03 WAIVER — scout-requirements absent or R-ID has no traceable section.
  C-03 WAIVER rows SHALL propagate to [IG-REGISTER] as:
    Elimination Path = "R-ID WAIVED (no requirements artifact)"

CASCADE TO: [IG-REGISTER] in Phase 2 (R-IDs MUST be carried forward as inertia
  gap inputs); cross-namespace signal row in Phase 3 Purpose section (location
  2 of 2).

Cross-namespace signal (location 1 of 2):
  Signal: scout-requirements artifact confirmed for R-ID traceability.
  Source: {file path if LOADED, or INLINE}

[PM-CONTRACT-SEAL] SHALL be emitted WHEN [PM-COVERAGE-TABLE] is fully populated
  with all R-IDs assigned and Waiver Status declared for every row.

[PM-CONTRACT-SEAL]
  INVALID IF [PM-COVERAGE-TABLE] is absent.
  INVALID IF no R-IDs are assigned in [PM-COVERAGE-TABLE].
  Both structural dependencies MUST be satisfied; neither alone is sufficient.

Phase 2 SHALL NOT begin until [PM-CONTRACT-SEAL] is present.

---

PHASE 2 — INERTIA ANALYSIS [GATE: INERTIA-ANALYZED]

Phase 2 SHALL NOT begin until [PM-CONTRACT-SEAL] is present.

PM: MUST add a row to [IG-REGISTER] for each risk that the status quo will persist
  and this feature will not be adopted. [IG-REGISTER] MUST contain minimum 2 IG-ID rows.

  [IG-REGISTER]
  IG-ID | Inertia Gap Description | AMPLIFIED | Elimination Path
  ------|-------------------------|-----------|------------------

  AMPLIFIED SHALL be set to Y when EITHER condition is satisfied:
    Condition A: The gap has a direct parallel in a named competing solution.
    Condition B: The gap blocks more than one P0 requirement from being addressed.

  AMPLIFIED Elimination Path MUST use dual sub-slot format — both sub-slots required:
    Risk: [risk narrative]
    R-ID: [R-XX from [PM-COVERAGE-TABLE]]
  Partial-population SHALL constitute a structural fail: a cell with one sub-slot
  populated while the other is blank is a structural fail, not a content gap.

  Standard Elimination Path format: R-ID: [R-XX from [PM-COVERAGE-TABLE]]
  C-03 WAIVER rows SHALL use: R-ID WAIVED (no requirements artifact)

Architect: MUST add resolved inertia decisions to [ID-REGISTER]:

  [ID-REGISTER]
  ID-ID | Decision | Rationale | IG-ID Resolved
  ------|----------|-----------|---------------

[INERTIA-ANALYZED]
  Condition 1: INVALID IF [IG-REGISTER] or [ID-REGISTER] is absent, or any required
    row is unpopulated.
  Condition 2: INVALID IF any [IG-REGISTER] Elimination Path cell is blank and not
    marked "R-ID WAIVED" — per-cell R-ID population MUST be satisfied for every
    non-waiver row.
  Condition 1 satisfied WITHOUT Condition 2 SHALL constitute an invalid state:
    structural completeness alone SHALL NOT permit [INERTIA-ANALYZED] to be emitted.
  [INERTIA-ANALYZED] Condition 2 exemption: cells marked "R-ID WAIVED" are exempt
  from the per-cell R-ID check.
  Waiver chain closure — all three nodes MUST be named in sequence:
    (1) [PM-COVERAGE-TABLE] C-03 WAIVER source
    (2) "R-ID WAIVED" cell marker in [IG-REGISTER] Elimination Path
    (3) Condition 2 exemption for R-ID WAIVED cells in [INERTIA-ANALYZED]

Phase 3 SHALL NOT begin until [PM-CONTRACT-SEAL] AND [INERTIA-ANALYZED] are both present.

---

PHASE 3 — REQUIREMENTS [GATE: SPEC-DRAFT-COMPLETE]

Phase 3 SHALL NOT begin until [PM-CONTRACT-SEAL] AND [INERTIA-ANALYZED] are both present.

PM: MUST state the P0 coverage count before any narrative prose:
  "P0 requirements carried forward: {n}"

PM: MUST scan `scout-requirements` -> scan R-01 through R-{n} -> flag contradictions.
  SHALL NOT confirm "none found" without naming the scan range R-01 through R-{n}.

Cross-namespace signal (location 2 of 2):
  Signal: scout-requirements artifact confirmed for Phase 3 traceability.
  Source: {same path as location 1 of 2}

Architect: MUST author each of the following five sections in prescribed order:

  1. PURPOSE
     State what the feature accomplishes from user and system perspectives.
     MUST connect to inertia decisions in Phase 2 where the spec resolves a named gap.
     [Cross-namespace signal (location 2 of 2) field placed here.]

  2. REQUIREMENTS
     MUST list all R-IDs from [PM-COVERAGE-TABLE] with Waiver Status = COVERED,
     grouped by Priority (P0 first). C-03 WAIVER rows MUST be flagged:
     "[R-XX] — WAIVED: {reason}"

  3. DESIGN
     Describe solution architecture, data model, and key operations. Each major
     design element MUST trace to at least one R-ID.

  4. CONSTRAINTS
     List hard constraints (platform, performance, compliance). Each constraint
     MUST name its source: {scout artifact path or INLINE}.

  5. OPEN QUESTIONS
     List unresolved questions with OQ-IDs. Each OQ MUST name the blocking concern
     and the information needed to resolve it.
     OQ-ID | Question | Blocking Concern | Resolution Path

[SPEC-DRAFT-COMPLETE]
  INVALID IF [PM-CONTRACT-SEAL] is absent.
  INVALID IF [INERTIA-ANALYZED] is absent.
  INVALID IF scout-requirements is LOADED but cross-namespace signal is absent at
    location 1 of 2 (Phase 1) or location 2 of 2 (Phase 3 Purpose section).

---

PHASE 4 — AMENDMENTS

PM: MUST list at minimum 2 amendments. Each amendment SHALL name the target section.

  Amendment 1 — Section: [section name]: [trigger and change description]
  Amendment 2 — Section: [section name]: [trigger and change description]

---

FINDINGS

Architect: MUST run self-review scan. MUST name what was scanned and what was found.
Scan items MUST cover all of the following:

  Scan 1 — Coverage gaps: P0 R-IDs in [PM-COVERAGE-TABLE] without a spec section.
  Scan 2 — Contradictions: R-01 through R-{n} — conflicting requirement pairs.
  Scan 3 — Complexity hotspots: sections with disproportionate complexity vs. priority.
  Scan 4 — OQ register: all unresolved OQ-IDs at spec completion.
  Scan 5 — Cross-namespace signal: confirm present at Phase 1 and Phase 3.
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

## V-04 — Competition-First Inertia Framing + STATUS-QUO-SNAPSHOT | Axes: Lifecycle Emphasis + Inertia Framing

**Hypothesis**: Opening Phase 2 with an explicit competitor map framed as "name what the
status quo offers before naming what it lacks" — [STATUS-QUO-SNAPSHOT] as the Phase 2
entry block, with each row naming a named alternative followed by its gap — activates the
STATUS-QUO cluster (C-36, C-37, C-45, C-46) without Phase 1.5. C-37 structural fail rule
declared in dual form (C-45). [INERTIA-ANALYZED] Condition 1 extended to name
[STATUS-QUO-SNAPSHOT] with scope qualifier (C-46). No ENTER/EXIT ceremony, no second-person
frame, no ROLE markers: C-41/C-42/C-43/C-44 still fail. Score adds 4 to non-extension
baseline: 31/39 -> **157.56**.

```
You are running /draft:spec. Phase 2 uses a competition-first inertia pattern:
before logging gaps, map the named alternatives the feature must displace. Each
status-quo alternative is named with the specific gap that makes it inadequate —
this anchors every inertia gap to a real displacement target. Active roles:
PM (requirements traceability + inertia analysis), Architect (spec authoring).

---

PHASE 0 — SCOUT ARTIFACT DISCOVERY

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

  Branch A — ALL NOT FOUND:
  > VERBATIM RESPONSE: "No scout artifacts found for this topic. Provide a 3-5
  > sentence product description to proceed, or run /scout:requirements first."

  Branch B-1 — scout-requirements N/A, at least one other LOADED:
  > VERBATIM RESPONSE: "scout-requirements not found. Requirements will be
  > extracted inline from your product description. Other loaded artifacts
  > provide context."

  Branch B-2 — scout-feasibility N/A, scout-requirements LOADED:
  > VERBATIM RESPONSE: "scout-feasibility not found. Feasibility constraints
  > noted as open questions in Phase 3 Section 5."

  Branch B-3 — scout-compliance N/A, scout-requirements LOADED:
  > VERBATIM RESPONSE: "scout-compliance not found. Compliance items flagged
  > as open questions in Phase 3 Section 5."

  Branch B-catch — any other partial configuration:
  > VERBATIM RESPONSE: "Partial scout coverage. Missing artifact types carry
  > [N/A - artifact missing] markers in relevant sections."

---

PHASE 1 — PM PRE-ASSIGNMENT [GATE: PM-CONTRACT-SEAL]

PM: scan `scout-requirements` -> extract R-IDs and Priority levels ->
  assign each R-ID to a planned section -> populate [PM-COVERAGE-TABLE]:

  [PM-COVERAGE-TABLE]
  R-ID | Requirement Summary | Priority | Assigned Section | Waiver Status
  -----|---------------------|----------|-----------------|---------------
  (one row per R-ID; Waiver Status = COVERED or C-03 WAIVER)

  Waiver Status values:
    COVERED     — R-ID maps to a named planned section.
    C-03 WAIVER — scout-requirements absent or R-ID has no traceable section.
  C-03 WAIVER rows propagate to [IG-REGISTER] as:
    Elimination Path = "R-ID WAIVED (no requirements artifact)"

CASCADE TO: [IG-REGISTER] in Phase 2 (R-IDs as inertia gap inputs);
  cross-namespace signal in Phase 3 Purpose section (location 2 of 2).

Cross-namespace signal (location 1 of 2):
  Signal: scout-requirements artifact confirmed for R-ID traceability.
  Source: {file path if LOADED, or INLINE}

-> EMIT [PM-CONTRACT-SEAL] WHEN [PM-COVERAGE-TABLE] fully populated.

[PM-CONTRACT-SEAL]
  INVALID IF [PM-COVERAGE-TABLE] is absent.
  INVALID IF no R-IDs are assigned in [PM-COVERAGE-TABLE].
  Both structural dependencies must be satisfied; neither alone is sufficient.

-> BLOCKED: Phase 2 requires [PM-CONTRACT-SEAL].

---

PHASE 2 — INERTIA ANALYSIS [GATE: INERTIA-ANALYZED]

-> BLOCKED: Phase 2 requires [PM-CONTRACT-SEAL].

Phase 2 has three blocks. Populate them in order:
  [STATUS-QUO-SNAPSHOT] — name the alternatives first; establish the competitive baseline.
  [IG-REGISTER]         — name the gaps that let the status quo win by default.
  [ID-REGISTER]         — name the decisions that close those gaps.

PM: Populate [STATUS-QUO-SNAPSHOT]. One row per named alternative the feature must
displace — a competing product, a manual workaround, an incumbent workflow, or the
absence of any solution. Each row names the alternative and states what capability gap
makes it inadequate:

  [STATUS-QUO-SNAPSHOT]
  Alternative               | Gap Statement
  --------------------------|----------------------------------------------------------
  (name the alternative)    | (state what it lacks that this feature provides)

  Structural fail rule:
    A row with a named Alternative but a blank Gap statement is a structural fail,
    not a content gap. Do not leave Gap blank when Alternative is populated.

PM: For each inertia gap that would cause the status quo alternative to persist
  despite this feature existing, add a row to [IG-REGISTER]:

  [IG-REGISTER]
  IG-ID | Inertia Gap Description | AMPLIFIED | Elimination Path
  ------|-------------------------|-----------|------------------

  Minimum 2 IG-ID rows required.

  AMPLIFIED threshold — mark AMPLIFIED = Y when EITHER:
    Condition A: The gap has a direct parallel in a named alternative from
      [STATUS-QUO-SNAPSHOT] — the alternative has this capability and this feature
      does not, making the gap a displacement blocker.
    Condition B: The gap blocks more than one P0 requirement from being addressed.

  AMPLIFIED Elimination Path dual sub-slot format (both required):
    Risk: [risk narrative — name the status-quo alternative it keeps in place]
    R-ID: [R-XX from [PM-COVERAGE-TABLE]]
  Partial-population structural fail: a cell with one sub-slot populated while the
  other is blank is a structural fail, not a content gap.

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

-> BLOCKED: Phase 3 requires [PM-CONTRACT-SEAL] AND [INERTIA-ANALYZED].

---

PHASE 3 — REQUIREMENTS [GATE: SPEC-DRAFT-COMPLETE]

-> BLOCKED: Phase 3 requires [PM-CONTRACT-SEAL] AND [INERTIA-ANALYZED].

P0 coverage count: State count before any section prose:
  "P0 requirements carried forward: {n}"

PM: scan `scout-requirements` -> scan R-01 through R-{n} -> flag contradictions.
Do not confirm "none found" without naming the scan range R-01 through R-{n}.

Cross-namespace signal (location 2 of 2):
  Signal: scout-requirements artifact confirmed for Phase 3 traceability.
  Source: {same path as location 1 of 2}

Architect: Author five sections in prescribed order:

  1. PURPOSE
     State what the feature accomplishes. Ground the purpose in the competitive
     displacement: name at least one status-quo alternative from [STATUS-QUO-SNAPSHOT]
     and the gap this feature closes.
     [Cross-namespace signal (location 2 of 2) placed here.]

  2. REQUIREMENTS
     List R-IDs from [PM-COVERAGE-TABLE] with Waiver Status = COVERED (P0 first).
     Flag C-03 WAIVER rows: "[R-XX] — WAIVED: {reason}"

  3. DESIGN
     Describe architecture, data model, and key operations. Each major design element
     traces to at least one R-ID. For each AMPLIFIED gap in [IG-REGISTER], name the
     design decision that closes the displacement risk.

  4. CONSTRAINTS
     List hard constraints with scout artifact source for each.

  5. OPEN QUESTIONS
     OQ-ID | Question | Blocking Concern | Resolution Path

[SPEC-DRAFT-COMPLETE]
  INVALID IF [PM-CONTRACT-SEAL] is absent.
  INVALID IF [INERTIA-ANALYZED] is absent.
  INVALID IF scout-requirements LOADED but signal absent at location 1 or 2.

---

PHASE 4 — AMENDMENTS

PM: List at minimum 2 amendments with named target sections.

  Amendment 1 — Section: [section name]: [trigger and change description]
  Amendment 2 — Section: [section name]: [trigger and change description]

---

FINDINGS

Architect: Run self-review scan. Name what was scanned and what was found.

  Scan 1 — Coverage gaps: P0 R-IDs in [PM-COVERAGE-TABLE] without a spec section.
  Scan 2 — Contradictions: R-01 through R-{n} — conflicting requirement pairs.
  Scan 3 — Complexity hotspots: sections with disproportionate complexity vs. priority.
  Scan 4 — OQ register: all unresolved OQ-IDs at spec completion.
  Scan 5 — Cross-namespace signal: confirm present at Phase 1 and Phase 3.
  Scan 6 — Waiver chain: C-03 WAIVER rows traceable through R-ID WAIVED to
    Condition 2 exemption.
  Scan 7 — Status-quo coverage: every row in [STATUS-QUO-SNAPSHOT] has a named
    alternative and a non-blank Gap Statement; every AMPLIFIED IG-ID names the
    alternative it displaces.

  Finding ID | Type               | Description | R-ID / OQ-ID | Resolution
  -----------|--------------------|-------------|--------------|----------
             | coverage gap       |             |              |
             | contradiction      |             |              |
             | complexity hotspot |             |              |
             | OQ register        |             |              |
```

---

## V-05 — Full Five-Cluster Extension with Compliance Lead Phase 1.5 | Axes: All Five

**Hypothesis**: All five extension clusters active simultaneously — STATUS-QUO-SNAPSHOT
(C-36/C-37/C-45/C-46), Phase 1.5 COMPLIANCE INERTIA SCOPING with Compliance Lead role
emitting [COMPLIANCE-SCOPE-SEAL] (C-38/C-39), [COMPLIANCE-SCOPE-SEAL] invalidity rule
cross-referencing [STATUS-QUO-SNAPSHOT] structural fail rule (C-40), ENTER/EXIT ceremony
at all five numbered phases (C-41/C-44), second-person transitional frame (C-42),
ROLE markers at all phase entries (C-43), Phase 2 multi-input ENTER absorbing both
[PM-CONTRACT-SEAL] and [COMPLIANCE-SCOPE-SEAL] (C-47) — should achieve 175/175.
Using Compliance Lead in Phase 1.5 (vs. Strategy in R18) tests a different fractional
sub-phase role while maintaining the same structural anatomy. Score: **175.00**.

```
You are running /draft:spec. You will move through five numbered phases plus a
Compliance scoping step (Phase 1.5) inserted between Phase 1 and Phase 2. Your
goal at each phase is stated in its preamble. Every phase boundary carries an
ENTER precondition and an EXIT token — the full sequence is readable as a
computable transition graph without parsing phase body content.
Active roles: PM (requirements traceability), Architect (spec authoring),
Compliance Lead (compliance scope + inertia baseline).

---

PHASE 0 — SCOUT ARTIFACT DISCOVERY
-> ROLE: PM

ENTER Phase 0: No preconditions. Phase 0 begins at invocation.

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

EXIT Phase 0: [SCOUT-STATUS-TABLE] complete. Proceed to Phase 1.

---

PHASE 1 — PM PRE-ASSIGNMENT [GATE: PM-CONTRACT-SEAL]
-> ROLE: PM

ENTER Phase 1: [SCOUT-STATUS-TABLE] must be complete from Phase 0 EXIT.

You are now entering Phase 1. Your goal is to anchor every requirement to a
named spec section before any design or analysis work begins. The assignment
table is your contract with Phase 3 — scope that is not in the table will
not be in the spec.

PM: scan `scout-requirements` -> extract all R-IDs and Priority levels ->
  assign each R-ID to a planned section -> populate [PM-COVERAGE-TABLE]:

  [PM-COVERAGE-TABLE]
  R-ID | Requirement Summary | Priority | Assigned Section | Waiver Status
  -----|---------------------|----------|-----------------|---------------
  (one row per R-ID; Waiver Status = COVERED or C-03 WAIVER)

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
  Both structural dependencies must be satisfied; neither alone is sufficient.

EXIT Phase 1: emits [PM-CONTRACT-SEAL]. Cascade: [PM-COVERAGE-TABLE] R-IDs
  flow to Phase 2 [IG-REGISTER]; cross-namespace signal activated at Phase 1.

---

PHASE 1.5 — COMPLIANCE INERTIA SCOPING [GATE: COMPLIANCE-SCOPE-SEAL]
-> ROLE: Compliance Lead

ENTER Phase 1.5: [PM-CONTRACT-SEAL] from Phase 1 must be present.

You are now entering Phase 1.5. Your goal is to evaluate the named alternatives
in [STATUS-QUO-SNAPSHOT] (which will be populated in Phase 2) for compliance
posture — establishing which alternatives have compliance characteristics that
affect the inertia calculus. Phase 2 cannot begin until this scope is sealed.

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

EXIT Phase 1.5: emits [COMPLIANCE-SCOPE-SEAL]. Compliance scope flows to Phase 2
  [STATUS-QUO-SNAPSHOT] and [IG-REGISTER] AMPLIFIED evaluation.

---

PHASE 2 — INERTIA ANALYSIS [GATE: INERTIA-ANALYZED]
-> ROLE: PM + Compliance Lead

ENTER Phase 2: [PM-CONTRACT-SEAL] from Phase 1 AND [COMPLIANCE-SCOPE-SEAL] from
  Phase 1.5 must both be present.
  -> BLOCKED: Phase 2 requires [PM-CONTRACT-SEAL] AND [COMPLIANCE-SCOPE-SEAL].

You are now entering Phase 2. Your goal is to map the forces that would cause the
status quo to persist. You will work in three blocks: snapshot the alternatives
first, then log the gaps, then record the decisions.

PM: Populate [STATUS-QUO-SNAPSHOT] — one row per named alternative the feature
must displace. Each row names the alternative and states the gap that makes it
inadequate:

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
    Compliance note: apply [COMPLIANCE-SCOPE-SEAL] amplification criteria when
      evaluating Condition A — a compliance gap in a named alternative strengthens
      displacement.

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

EXIT Phase 2: emits [INERTIA-ANALYZED]. Cascade: [IG-REGISTER] decisions flow to
  Phase 3 Design section; [STATUS-QUO-SNAPSHOT] Gap Statements available for
  Phase 3 Purpose grounding.

---

PHASE 3 — REQUIREMENTS [GATE: SPEC-DRAFT-COMPLETE]
-> ROLE: Architect + PM

ENTER Phase 3: [PM-CONTRACT-SEAL] from Phase 1 AND [INERTIA-ANALYZED] from Phase 2
  must both be present.
  -> BLOCKED: Phase 3 requires [PM-CONTRACT-SEAL] AND [INERTIA-ANALYZED].

You are now entering Phase 3. Your goal is to author the specification itself.
Everything you write here must trace back to what was established in Phases 1 and 2 —
the assignment table and inertia decisions become a design.

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
     Connect to inertia decisions in Phase 2 and name at least one status-quo
     alternative from [STATUS-QUO-SNAPSHOT] that this feature displaces.
     [Cross-namespace signal (location 2 of 2) placed here.]

  2. REQUIREMENTS
     List R-IDs from [PM-COVERAGE-TABLE] with Waiver Status = COVERED (P0 first).
     Flag C-03 WAIVER rows: "[R-XX] — WAIVED: {reason}"

  3. DESIGN
     Describe architecture, data model, and key operations. Each major design
     element traces to at least one R-ID. Name the design decision that closes
     each AMPLIFIED gap in [IG-REGISTER].

  4. CONSTRAINTS
     List hard constraints with scout artifact source for each. Flag any constraint
     surfaced by [COMPLIANCE-SCOPE-SEAL] compliance scope declaration.

  5. OPEN QUESTIONS
     OQ-ID | Question | Blocking Concern | Resolution Path

[SPEC-DRAFT-COMPLETE]
  INVALID IF [PM-CONTRACT-SEAL] is absent.
  INVALID IF [INERTIA-ANALYZED] is absent.
  INVALID IF scout-requirements LOADED but signal absent at location 1 of 2
    (Phase 1) or location 2 of 2 (Phase 3 Purpose section).

EXIT Phase 3: emits [SPEC-DRAFT-COMPLETE]. Cascade: spec content available for
  Phase 4 amendment review.

---

PHASE 4 — AMENDMENTS
-> ROLE: PM + Architect

ENTER Phase 4: [SPEC-DRAFT-COMPLETE] from Phase 3 must be present.

You are now in Phase 4. Your goal is to name the conditions under which this
spec would need revision — not to revise it now, but to make future amendment
paths explicit.

PM: List at minimum 2 amendments. Each amendment names the target section.

  Amendment 1 — Section: [section name]: [trigger and change description]
  Amendment 2 — Section: [section name]: [trigger and change description]

EXIT Phase 4: amendment list complete. Spec artifact ready for FINDINGS review.

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
  Scan 7 — Compliance scope coverage: [COMPLIANCE-SCOPE-SEAL] domains reflected
    in Constraints section; AMPLIFIED gaps with compliance factors named.
  Scan 8 — Status-quo displacement: every [STATUS-QUO-SNAPSHOT] Alternative has
    a non-blank Gap Statement; Purpose section names at least one alternative.

  Finding ID | Type               | Description | R-ID / OQ-ID | Resolution
  -----------|--------------------|-------------|--------------|----------
             | coverage gap       |             |              |
             | contradiction      |             |              |
             | complexity hotspot |             |              |
             | OQ register        |             |              |
```
