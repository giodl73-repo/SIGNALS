# draft-spec Variate — Round 18

Rubric version: v17 · Formula: (E/5×60) + (R/3×30) + (A/39×85) · No new criteria from R17.

Single-axis variations (V-01..V-03), then combinations (V-04..V-05).

**Axes explored:**
- **V-01**: Role sequence — Architect-first scaffolding (Architect names section scaffold before PM assigns R-IDs)
- **V-02**: Output format — table-dominant (pre-printed column stubs for every structural block; minimal directive prose)
- **V-03**: Phrasing register — second-person transitional frame with actor-directive preservation (C-42 target)
- **V-04**: Lifecycle emphasis + Inertia framing — STATUS-QUO-SNAPSHOT as first-class block; Phase 2 expanded with C-36/C-37/C-45/C-46
- **V-05**: Role sequence + ENTER/EXIT ceremony + Phase 1.5 — full five-cluster extension targeting 175/175

**Predicted scores:**

| Variation | A-pass | A-fail | A-N/A | Composite |
|-----------|--------|--------|-------|-----------|
| V-01 | 27 | 4 | 8 | **148.85** |
| V-02 | 27 | 4 | 8 | **148.85** |
| V-03 | 28 | 3 | 8 | **151.03** |
| V-04 | 31 | 4 | 4 | **157.56** |
| V-05 | 39 | 0 | 0 | **175.00** |

Aspirational N/A breakdown:
- V-01/V-02/V-03: C-36, C-37, C-38, C-39, C-40, C-45, C-46, C-47 (no STATUS-QUO, no Phase 1.5)
- V-04: C-38, C-39, C-40, C-47 (no Phase 1.5; STATUS-QUO cluster active)
- V-05: none (all five extension clusters active)

Aspirational fails (non-N/A):
- V-01/V-02: C-41, C-42, C-43, C-44 (no ceremony, no second-person, no ROLE markers)
- V-03: C-41, C-43, C-44 (adds C-42 via second-person; no ceremony, no ROLE markers)
- V-04: C-41, C-42, C-43, C-44 (STATUS-QUO cluster only; no ceremony)
- V-05: none

---

## V-01 — Architect-First Role Sequence | Axis: Role Sequence | No extension clusters

**Hypothesis**: Starting with Architect declaring the section scaffold before PM assigns
R-IDs tests whether the architecture-first ordering changes any rubric outcomes. Expected
result: all essential + recommended pass; aspirational pass rate identical to any
non-extension baseline (27/39) because C-41/C-42/C-43/C-44 require structural elements
absent from this variation and N/A cluster is unchanged. Score: **148.85**.

```
You are running /draft:spec. Active roles: Architect (spec structure owner), PM
(requirements traceability owner). Architect scaffolds the section structure first;
PM then assigns coverage.

---

PHASE 0 — SCOUT ARTIFACT DISCOVERY

Architect: Scan the workspace for scout artifacts related to the topic. Populate
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

Evaluate table. Execute the first matching branch:

  Branch A — ALL NOT FOUND:
  > VERBATIM RESPONSE: "No scout artifacts found for this topic. To proceed, provide
  > a 3–5 sentence product description and I will extract requirements inline.
  > Alternatively, run /scout:requirements first."

  Branch B-1 — scout-requirements N/A, at least one other artifact LOADED:
  > VERBATIM RESPONSE: "scout-requirements not found. Requirements will be extracted
  > inline from your product description. Other loaded artifacts provide context.
  > Proceed with a 3–5 sentence description."

  Branch B-2 — scout-feasibility N/A, scout-requirements LOADED:
  > VERBATIM RESPONSE: "scout-feasibility not found. Feasibility constraints will be
  > noted as open questions in Phase 3 Section 5. Spec proceeds without feasibility
  > scoring."

  Branch B-3 — scout-compliance N/A, scout-requirements LOADED:
  > VERBATIM RESPONSE: "scout-compliance not found. Compliance requirements will be
  > flagged as open questions in Phase 3 Section 5. Spec proceeds without compliance
  > gating."

  Branch B-catch — any other partial configuration:
  > VERBATIM RESPONSE: "Partial scout coverage detected. Available artifacts are in
  > use. Sections drawing from missing artifact types carry an [N/A — artifact
  > missing] marker."

---

PHASE 1 — PM PRE-ASSIGNMENT [GATE: PM-CONTRACT-SEAL]

Architect: Before PM assigns R-IDs, declare the planned spec section scaffold — the
named sections you will author in Phase 3. Each section must be named:

  Planned sections:
  1. Purpose
  2. Requirements
  3. Design
  4. Constraints
  5. Open Questions

PM: scan `scout-requirements` → extract all R-IDs and Priority levels → assign each
R-ID to one or more planned sections → populate [PM-COVERAGE-TABLE]:

  [PM-COVERAGE-TABLE]
  R-ID | Requirement Summary | Priority | Assigned Section | Waiver Status
  -----|---------------------|----------|-----------------|---------------
  (one row per R-ID; Waiver Status = COVERED or C-03 WAIVER)

  Waiver Status values:
    COVERED    — R-ID maps to a named planned section
    C-03 WAIVER — scout-requirements absent or R-ID has no traceable section
  C-03 WAIVER rows propagate to [IG-REGISTER] as:
    Elimination Path = "R-ID WAIVED (no requirements artifact)"

CASCADE TO: [IG-REGISTER] in Phase 2 (R-IDs carried forward as inertia gap inputs);
  cross-namespace signal row in Phase 3 Purpose section (location 2 of 2).

Cross-namespace signal (location 1 of 2):
  Signal: scout-requirements artifact confirmed for R-ID traceability.
  Source: {file path if LOADED, or INLINE}

→ EMIT [PM-CONTRACT-SEAL] WHEN [PM-COVERAGE-TABLE] is fully populated with all R-IDs
  assigned and Waiver Status declared for every row.

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
  Partial-population structural fail: a cell in which one sub-slot is populated while
  the other is blank is a structural fail, not a content gap.

  Standard Elimination Path format: R-ID: [R-XX from [PM-COVERAGE-TABLE]]
  C-03 WAIVER rows: R-ID WAIVED (no requirements artifact)

Architect: Add resolved inertia decisions to [ID-REGISTER]:

  [ID-REGISTER]
  ID-ID | Decision | Rationale | IG-ID Resolved
  ------|----------|-----------|---------------

[INERTIA-ANALYZED]
  Condition 1: INVALID IF [IG-REGISTER] or [ID-REGISTER] is absent, or any required
    row is unpopulated.
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

→ BLOCKED: Phase 3 requires [PM-CONTRACT-SEAL] AND [INERTIA-ANALYZED].

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
     State what the feature accomplishes from user and system perspectives. Connect
     to inertia decisions in Phase 2 where the spec resolves a named inertia gap.

  2. REQUIREMENTS
     List all R-IDs from [PM-COVERAGE-TABLE] with Waiver Status = COVERED, grouped
     by Priority (P0 first). Flag C-03 WAIVER rows: "[R-XX] — WAIVED: {reason}"

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

PM: List at minimum 2 amendments. Each amendment names the target section.

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
  Scan 6 — Waiver chain: C-03 WAIVER rows traceable through R-ID WAIVED to Condition 2 exemption.

  Finding ID | Type               | Description | R-ID / OQ-ID | Resolution
  -----------|--------------------|-------------|--------------|----------
             | coverage gap       |             |              |
             | contradiction      |             |              |
             | complexity hotspot |             |              |
             | OQ register        |             |              |
```

---

## V-02 — Table-Dominant Format | Axis: Output Format | No extension clusters

**Hypothesis**: Pre-printing explicit column-header stubs for every structural block
removes format ambiguity — the LLM fills rows rather than interpreting field
descriptions. Rubric score is unchanged from V-01 (format does not affect criterion
presence/absence), but table-dominant prompts may improve per-cell traceability
compliance for C-09, C-32, C-33. Score: **148.85**.

```
You are running /draft:spec. Produce the spec by filling the pre-printed structural
blocks below. Do not paraphrase block definitions; populate the named columns.
Active roles: PM (requirements traceability), Architect (spec authoring).

---

PHASE 0 — SCOUT ARTIFACT DISCOVERY

PM: Fill [SCOUT-STATUS-TABLE]. Status = LOADED if file found, N/A otherwise.

  [SCOUT-STATUS-TABLE]
  | Artifact Type      | Status       | File Path |
  |--------------------|--------------|-----------|
  | scout-requirements | LOADED / N/A |           |
  | scout-feasibility  | LOADED / N/A |           |
  | scout-compliance   | LOADED / N/A |           |
  | scout-market       | LOADED / N/A |           |
  | scout-stakeholders | LOADED / N/A |           |
  | scout-naming       | LOADED / N/A |           |
  | scout-positioning  | LOADED / N/A |           |

Fallback decision table — match the first true row:

  | Condition                                              | Branch   |
  |--------------------------------------------------------|----------|
  | All 7 rows = N/A                                       | Branch A |
  | scout-requirements = N/A, ≥1 other = LOADED           | B-1      |
  | scout-feasibility = N/A, scout-requirements = LOADED  | B-2      |
  | scout-compliance = N/A, scout-requirements = LOADED   | B-3      |
  | Any other partial configuration                        | B-catch  |

  Branch A:
  > VERBATIM RESPONSE: "No scout artifacts found. Provide a 3–5 sentence product
  > description to proceed, or run /scout:requirements first."

  Branch B-1:
  > VERBATIM RESPONSE: "scout-requirements not found. Extracting requirements inline
  > from your description. Other loaded artifacts provide context."

  Branch B-2:
  > VERBATIM RESPONSE: "scout-feasibility not found. Feasibility constraints flagged
  > as open questions in Phase 3. Spec proceeds without feasibility scoring."

  Branch B-3:
  > VERBATIM RESPONSE: "scout-compliance not found. Compliance items flagged as open
  > questions in Phase 3. Spec proceeds without compliance gating."

  Branch B-catch:
  > VERBATIM RESPONSE: "Partial scout coverage. Missing artifact types carry
  > [N/A — artifact missing] markers in relevant sections."

---

PHASE 1 — PM PRE-ASSIGNMENT [GATE: PM-CONTRACT-SEAL]

PM: scan `scout-requirements` → fill [PM-COVERAGE-TABLE]. One row per R-ID.

  [PM-COVERAGE-TABLE]
  | R-ID | Requirement Summary | Priority | Assigned Section     | Waiver Status  |
  |------|---------------------|----------|----------------------|----------------|
  |      |                     |          | Purpose /            | COVERED /      |
  |      |                     |          | Requirements /       | C-03 WAIVER    |
  |      |                     |          | Design /             |                |
  |      |                     |          | Constraints /        |                |
  |      |                     |          | Open Questions       |                |

  Waiver Status column values:
    COVERED    — R-ID maps to a named section in Phase 3.
    C-03 WAIVER — scout-requirements absent or R-ID has no traceable section.
  C-03 WAIVER rows → Elimination Path in [IG-REGISTER] = "R-ID WAIVED (no requirements artifact)"

CASCADE TO annotation:
  → [IG-REGISTER] Phase 2: R-IDs carried as inertia gap inputs.
  → Phase 3 Purpose section cross-namespace signal row (location 2 of 2).

Cross-namespace signal (location 1 of 2):
  | Signal field | Value                                                     |
  |--------------|-----------------------------------------------------------|
  | Artifact     | scout-requirements (LOADED path or INLINE)                |
  | Purpose      | R-ID traceability source for [PM-COVERAGE-TABLE]          |
  | Location     | 1 of 2 (Phase 1); paired at Phase 3 Purpose (location 2)  |

→ EMIT [PM-CONTRACT-SEAL] WHEN all rows populated with Waiver Status declared.

  [PM-CONTRACT-SEAL] invalidity table:
  | INVALID IF condition                          | Dependency     |
  |-----------------------------------------------|----------------|
  | [PM-COVERAGE-TABLE] is absent                 | Structural (1) |
  | No R-IDs assigned in [PM-COVERAGE-TABLE]      | Structural (2) |
  Both dependencies must be satisfied; neither alone is sufficient.

→ BLOCKED: Phase 2 requires [PM-CONTRACT-SEAL].

---

PHASE 2 — INERTIA ANALYSIS [GATE: INERTIA-ANALYZED]

→ BLOCKED: Phase 2 requires [PM-CONTRACT-SEAL].

PM: Fill [IG-REGISTER]. Minimum 2 IG-ID rows.

  [IG-REGISTER]
  | IG-ID | Inertia Gap Description | AMPLIFIED | Elimination Path          |
  |-------|-------------------------|-----------|---------------------------|
  |       |                         | Y / N     | R-ID: [R-XX from          |
  |       |                         |           | [PM-COVERAGE-TABLE]]      |
  |       |                         |           | — or —                    |
  |       |                         |           | R-ID WAIVED (no req art.) |

  AMPLIFIED = Y when EITHER:
    A. Gap has direct parallel in a named competing solution.
    B. Gap blocks >1 P0 requirement.

  AMPLIFIED Elimination Path sub-slots (pre-printed; both required):
  | Sub-slot | Content                             |
  |----------|-------------------------------------|
  | Risk:    | [risk narrative]                    |
  | R-ID:    | [R-XX from [PM-COVERAGE-TABLE]]     |
  Partial-population structural fail: one sub-slot populated + one blank = structural fail.

Architect: Fill [ID-REGISTER].

  [ID-REGISTER]
  | ID-ID | Decision | Rationale | IG-ID Resolved |
  |-------|----------|-----------|----------------|

  [INERTIA-ANALYZED] invalidity table:
  | Condition   | INVALID IF                                                          |
  |-------------|---------------------------------------------------------------------|
  | Condition 1 | [IG-REGISTER] or [ID-REGISTER] absent, or any required row missing  |
  | Condition 2 | Any Elimination Path cell blank and not marked "R-ID WAIVED"        |
  | Combined    | Condition 1 satisfied without Condition 2 = invalid state           |

  Condition 2 exemption: "R-ID WAIVED" cells exempt from per-cell R-ID check.

  Waiver chain closure table — all three nodes required in sequence:
  | Node | Location                                                      |
  |------|---------------------------------------------------------------|
  | (1)  | [PM-COVERAGE-TABLE] C-03 WAIVER source row                    |
  | (2)  | "R-ID WAIVED" Elimination Path cell in [IG-REGISTER]          |
  | (3)  | Condition 2 exemption in [INERTIA-ANALYZED] token definition  |

→ BLOCKED: Phase 3 requires [PM-CONTRACT-SEAL] AND [INERTIA-ANALYZED].

---

PHASE 3 — REQUIREMENTS [GATE: SPEC-DRAFT-COMPLETE]

→ BLOCKED: Phase 3 requires [PM-CONTRACT-SEAL] AND [INERTIA-ANALYZED].

P0 coverage count: | P0 requirements carried forward: {n} |
(State count before any section prose.)

PM: scan `scout-requirements` R-01 through R-{n} → contradiction scan.
Do not confirm "none found" without naming the scan range.

Cross-namespace signal (location 2 of 2):
  | Signal field | Value                                               |
  |--------------|-----------------------------------------------------|
  | Artifact     | scout-requirements (same path as location 1 of 2)   |
  | Purpose      | Phase 3 traceability confirmation                   |
  | Location     | 2 of 2 (Phase 3 Purpose section)                    |

Architect: Author five sections in prescribed order:

  1. PURPOSE
     Describe what the feature accomplishes and why it is being built.
     Connect to Phase 2 inertia decisions where the spec resolves a named gap.
     [Include cross-namespace signal (location 2 of 2) field here.]

  2. REQUIREMENTS
     | R-ID | Requirement Summary | Priority | Status       |
     |------|---------------------|----------|--------------|
     (COVERED rows only; P0 first; flag WAIVER rows: "[R-XX] — WAIVED: {reason}")

  3. DESIGN
     Describe architecture, data model, and key operations. Each major design
     element traces to at least one R-ID.

  4. CONSTRAINTS
     | Constraint | Source Artifact | Priority |
     |------------|----------------|----------|
     (hard constraints: platform, performance, compliance; name scout artifact origin)

  5. OPEN QUESTIONS
     | OQ-ID | Question | Blocking Concern | Resolution Path |
     |-------|----------|-----------------|-----------------|

  [SPEC-DRAFT-COMPLETE] invalidity table:
  | INVALID IF condition                                                    |
  |-------------------------------------------------------------------------|
  | [PM-CONTRACT-SEAL] is absent                                            |
  | [INERTIA-ANALYZED] is absent                                            |
  | scout-requirements LOADED but signal absent at location 1 or location 2 |

---

PHASE 4 — AMENDMENTS

  | # | Section         | Amendment Trigger and Change Description |
  |---|-----------------|------------------------------------------|
  | 1 |                 |                                          |
  | 2 |                 |                                          |
  (minimum 2 rows; Section column must name the target section)

---

FINDINGS

Self-review scan table — name what was scanned and what was found:

  | Scan # | Scan Target                         | Range / Scope        | Findings |
  |--------|-------------------------------------|----------------------|----------|
  | 1      | Coverage gaps                       | P0 R-IDs             |          |
  | 2      | Contradictions                      | R-01 through R-{n}   |          |
  | 3      | Complexity hotspots                 | All sections         |          |
  | 4      | OQ register                         | OQ-01 through OQ-{n} |          |
  | 5      | Cross-namespace signal placement    | Phase 1 + Phase 3    |          |
  | 6      | Waiver chain completeness           | C-03 WAIVER rows     |          |

  Findings table:
  | Finding ID | Type               | Description | R-ID / OQ-ID | Resolution |
  |------------|--------------------|-------------|--------------|------------|
  |            | coverage gap       |             |              |            |
  |            | contradiction      |             |              |            |
  |            | complexity hotspot |             |              |            |
  |            | OQ register        |             |              |            |
```

---

## V-03 — Second-Person Transitional Frame | Axis: Phrasing Register | C-42 target

**Hypothesis**: Second-person framing in phase purpose statements and transitional
preambles across ≥3 phases satisfies C-42 independently of C-41 (no ENTER/EXIT
ceremony required). Actor→action directives preserve "PM: scan →" form throughout
(C-27 precondition for C-42). C-43/C-44 still fail (no ROLE markers, no chained
ENTER/EXIT). Score adds C-42 to baseline: 28/39 → **151.03**.

```
You are running /draft:spec. You will move through five phases to produce a
technical specification. Your goal at each phase is named in its preamble.
Active roles: PM (requirements traceability), Architect (spec authoring).

---

PHASE 0 — SCOUT ARTIFACT DISCOVERY

You are beginning Phase 0. Your goal is to establish what scout evidence already
exists for this topic before any authoring begins.

PM: scan `scout-requirements` → populate [SCOUT-STATUS-TABLE]:

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

Evaluate the table. Execute the first matching branch:

  Branch A — ALL NOT FOUND:
  > VERBATIM RESPONSE: "No scout artifacts found for this topic. Provide a 3–5
  > sentence product description to extract requirements inline, or run
  > /scout:requirements first."

  Branch B-1 — scout-requirements N/A, ≥1 other LOADED:
  > VERBATIM RESPONSE: "scout-requirements not found. Requirements will be extracted
  > inline from your product description. Other loaded artifacts provide context."

  Branch B-2 — scout-feasibility N/A, scout-requirements LOADED:
  > VERBATIM RESPONSE: "scout-feasibility not found. Feasibility constraints will be
  > noted as open questions in Phase 3 Section 5."

  Branch B-3 — scout-compliance N/A, scout-requirements LOADED:
  > VERBATIM RESPONSE: "scout-compliance not found. Compliance items will be flagged
  > as open questions in Phase 3 Section 5."

  Branch B-catch — any other partial configuration:
  > VERBATIM RESPONSE: "Partial scout coverage detected. Missing artifact types carry
  > [N/A — artifact missing] markers in relevant sections."

---

PHASE 1 — PM PRE-ASSIGNMENT [GATE: PM-CONTRACT-SEAL]

You are now entering Phase 1. Your goal is to anchor every requirement to a named
spec section before any design work begins. This prevents scope from drifting during
authoring — the assignment table is your contract with Phase 3.

PM: scan `scout-requirements` → extract R-IDs → assign each to a planned section
→ populate [PM-COVERAGE-TABLE]:

  [PM-COVERAGE-TABLE]
  R-ID | Requirement Summary | Priority | Assigned Section | Waiver Status
  -----|---------------------|----------|-----------------|---------------
  (one row per R-ID; Waiver Status = COVERED or C-03 WAIVER)

  Waiver Status values:
    COVERED    — R-ID maps to a named planned section.
    C-03 WAIVER — scout-requirements absent or R-ID has no traceable section.
  C-03 WAIVER rows propagate to [IG-REGISTER] as:
    Elimination Path = "R-ID WAIVED (no requirements artifact)"

CASCADE TO: [IG-REGISTER] in Phase 2 (R-IDs as inertia gap inputs);
  cross-namespace signal row in Phase 3 Purpose section (location 2 of 2).

Cross-namespace signal (location 1 of 2):
  Signal: scout-requirements artifact confirmed for R-ID traceability.
  Source: {file path if LOADED, or INLINE}

→ EMIT [PM-CONTRACT-SEAL] WHEN [PM-COVERAGE-TABLE] is fully populated.

[PM-CONTRACT-SEAL]
  INVALID IF [PM-COVERAGE-TABLE] is absent.
  INVALID IF no R-IDs are assigned in [PM-COVERAGE-TABLE].
  Both structural dependencies must be satisfied; neither alone is sufficient.

→ BLOCKED: Phase 2 requires [PM-CONTRACT-SEAL].

---

PHASE 2 — INERTIA ANALYSIS [GATE: INERTIA-ANALYZED]

You are now entering Phase 2. Your goal is to surface the forces that would cause
this feature to fail in the field even if it is technically correct. You are not
writing the spec yet — you are mapping the resistance the spec must overcome.

→ BLOCKED: Phase 2 requires [PM-CONTRACT-SEAL].

PM: For each inertia gap — a risk that the status quo wins by default — add a row
to [IG-REGISTER]:

  [IG-REGISTER]
  IG-ID | Inertia Gap Description | AMPLIFIED | Elimination Path
  ------|-------------------------|-----------|------------------

  Minimum 2 IG-ID rows required.

  AMPLIFIED threshold — mark AMPLIFIED = Y when EITHER:
    Condition A: The gap has a direct parallel in a named competing solution.
    Condition B: The gap blocks more than one P0 requirement from being addressed.
  AMPLIFIED Elimination Path dual sub-slot format (both required):
    Risk: [risk narrative]
    R-ID: [R-XX from [PM-COVERAGE-TABLE]]
  Partial-population structural fail: one sub-slot populated + one blank = structural fail.

  Standard Elimination Path: R-ID: [R-XX from [PM-COVERAGE-TABLE]]
  C-03 WAIVER rows: R-ID WAIVED (no requirements artifact)

Architect: Add resolved decisions to [ID-REGISTER]:

  [ID-REGISTER]
  ID-ID | Decision | Rationale | IG-ID Resolved
  ------|----------|-----------|---------------

[INERTIA-ANALYZED]
  Condition 1: INVALID IF [IG-REGISTER] or [ID-REGISTER] is absent, or any required
    row is unpopulated.
  Condition 2: INVALID IF any Elimination Path cell is blank and not marked
    "R-ID WAIVED" — per-cell R-ID population required for every non-waiver row.
  Meeting Condition 1 without Condition 2 is invalid.
  Condition 2 exemption: "R-ID WAIVED" cells are exempt from per-cell R-ID check.
  Waiver chain closure — all three nodes named in sequence:
    (1) [PM-COVERAGE-TABLE] C-03 WAIVER source
    (2) "R-ID WAIVED" cell in [IG-REGISTER] Elimination Path
    (3) Condition 2 exemption in [INERTIA-ANALYZED]

→ BLOCKED: Phase 3 requires [PM-CONTRACT-SEAL] AND [INERTIA-ANALYZED].

---

PHASE 3 — REQUIREMENTS [GATE: SPEC-DRAFT-COMPLETE]

You are now entering Phase 3. Your goal is to author the specification itself.
Everything you write here must be traceable to what you established in Phases 1
and 2 — this is where the assignment table and inertia decisions become a design.

→ BLOCKED: Phase 3 requires [PM-CONTRACT-SEAL] AND [INERTIA-ANALYZED].

P0 coverage count: State count before any prose: "P0 requirements carried forward: {n}"

PM: scan `scout-requirements` R-01 through R-{n} → flag contradictions.
Do not confirm "none found" without naming the scan range.

Cross-namespace signal (location 2 of 2):
  Signal: scout-requirements artifact confirmed for Phase 3 traceability.
  Source: {same path as location 1 of 2}

Architect: Author five sections in prescribed order:

  1. PURPOSE
     State what the feature accomplishes. Connect to Phase 2 inertia decisions.
     [Cross-namespace signal (location 2 of 2) field placed here.]

  2. REQUIREMENTS
     List R-IDs from [PM-COVERAGE-TABLE] with Waiver Status = COVERED (P0 first).
     Flag C-03 WAIVER rows: "[R-XX] — WAIVED: {reason}"

  3. DESIGN
     Describe solution architecture, data model, and operations. Each design
     element traces to at least one R-ID.

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

You are now in Phase 4. Your goal is to name the conditions under which this spec
would need revision — not to revise it now, but to make future amendment paths explicit.

PM: List at minimum 2 amendments with named target sections.

  Amendment 1 — Section: [section name]: [trigger and change description]
  Amendment 2 — Section: [section name]: [trigger and change description]

---

FINDINGS

You have completed the spec draft. Your goal now is to review what you produced
for gaps, conflicts, and open threads before handing off.

Architect: Run self-review scan. Name what was scanned and what was found.

  Scan 1 — Coverage gaps: P0 R-IDs in [PM-COVERAGE-TABLE] without a spec section.
  Scan 2 — Contradictions: R-01 through R-{n} — conflicting requirement pairs.
  Scan 3 — Complexity hotspots: sections with disproportionate complexity vs. priority.
  Scan 4 — OQ register: all unresolved OQ-IDs at spec completion.
  Scan 5 — Cross-namespace signal: confirm at Phase 1 (location 1) and Phase 3 (location 2).
  Scan 6 — Waiver chain: C-03 WAIVER rows traceable through R-ID WAIVED to Condition 2.

  Finding ID | Type               | Description | R-ID / OQ-ID | Resolution
  -----------|--------------------|-------------|--------------|----------
             | coverage gap       |             |              |
             | contradiction      |             |              |
             | complexity hotspot |             |              |
             | OQ register        |             |              |
```

---

## V-04 — Inertia-Heavy Lifecycle + STATUS-QUO-SNAPSHOT | Axes: Lifecycle Emphasis + Inertia Framing

**Hypothesis**: Foregrounding the status-quo competitor as a named block ([STATUS-QUO-SNAPSHOT])
before [IG-REGISTER] in Phase 2 — with structural fail rule in dual form (C-45) and scope
qualifier on Condition 1 (C-46) — adds the STATUS-QUO cluster (C-36, C-37, C-45, C-46)
without requiring Phase 1.5. Score adds 4 to V-01 baseline: 31/39 → **157.56**.

```
You are running /draft:spec. Phase 2 is the analytical core of this spec: before you
can design a solution, you must prove the status quo is inadequate and that the
inertia gaps are understood. Active roles: PM (requirements + inertia), Architect (design).

---

PHASE 0 — SCOUT ARTIFACT DISCOVERY

PM: scan workspace → populate [SCOUT-STATUS-TABLE]:

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
  > VERBATIM RESPONSE: "No scout artifacts found. Provide a 3–5 sentence product
  > description to proceed, or run /scout:requirements first."

  Branch B-1 — scout-requirements N/A, ≥1 other LOADED:
  > VERBATIM RESPONSE: "scout-requirements not found. Requirements extracted inline
  > from your description. Other loaded artifacts provide context."

  Branch B-2 — scout-feasibility N/A, scout-requirements LOADED:
  > VERBATIM RESPONSE: "scout-feasibility not found. Feasibility constraints noted
  > as open questions in Phase 3."

  Branch B-3 — scout-compliance N/A, scout-requirements LOADED:
  > VERBATIM RESPONSE: "scout-compliance not found. Compliance items flagged as
  > open questions in Phase 3."

  Branch B-catch — any other partial configuration:
  > VERBATIM RESPONSE: "Partial scout coverage. Missing artifact types carry
  > [N/A — artifact missing] markers."

---

PHASE 1 — PM PRE-ASSIGNMENT [GATE: PM-CONTRACT-SEAL]

PM: scan `scout-requirements` → extract R-IDs → assign each to a planned section →
populate [PM-COVERAGE-TABLE]:

  [PM-COVERAGE-TABLE]
  R-ID | Requirement Summary | Priority | Assigned Section | Waiver Status
  -----|---------------------|----------|-----------------|---------------
  (one row per R-ID; Waiver Status = COVERED or C-03 WAIVER)

  C-03 WAIVER rows → [IG-REGISTER] Elimination Path = "R-ID WAIVED (no requirements artifact)"

CASCADE TO: [IG-REGISTER] in Phase 2; cross-namespace signal in Phase 3 Purpose (location 2 of 2).

Cross-namespace signal (location 1 of 2):
  Signal: scout-requirements artifact confirmed for R-ID traceability.
  Source: {file path if LOADED, or INLINE}

→ EMIT [PM-CONTRACT-SEAL] WHEN [PM-COVERAGE-TABLE] fully populated.

[PM-CONTRACT-SEAL]
  INVALID IF [PM-COVERAGE-TABLE] is absent.
  INVALID IF no R-IDs are assigned in [PM-COVERAGE-TABLE].

→ BLOCKED: Phase 2 requires [PM-CONTRACT-SEAL].

---

PHASE 2 — INERTIA ANALYSIS [GATE: INERTIA-ANALYZED]

→ BLOCKED: Phase 2 requires [PM-CONTRACT-SEAL].

Phase 2 has three blocks. Complete them in order: [STATUS-QUO-SNAPSHOT] first, then
[IG-REGISTER], then [ID-REGISTER]. The snapshot establishes what the status quo looks
like today — without it, gap analysis has no baseline.

PM: Populate [STATUS-QUO-SNAPSHOT] — one row per named alternative that the status
quo offers or that users currently rely on instead of this feature:

  [STATUS-QUO-SNAPSHOT]
  Alternative               | Gap Statement
  --------------------------|---------------
  (name the status-quo alt) | (state what capability it lacks vs. this feature)

  Structural fail rule:
    A row with a named Alternative but a blank Gap statement is a structural fail,
    not a content gap. Do not leave Gap blank when Alternative is populated.

PM: For each inertia gap, add a row to [IG-REGISTER]:

  [IG-REGISTER]
  IG-ID | Inertia Gap Description | AMPLIFIED | Elimination Path
  ------|-------------------------|-----------|------------------

  Minimum 2 IG-ID rows required.

  AMPLIFIED threshold — mark AMPLIFIED = Y when EITHER:
    Condition A: The gap has a direct parallel in a named alternative from [STATUS-QUO-SNAPSHOT].
    Condition B: The gap blocks more than one P0 requirement.
  AMPLIFIED Elimination Path dual sub-slot format (both required):
    Risk: [risk narrative]
    R-ID: [R-XX from [PM-COVERAGE-TABLE]]
  Partial-population structural fail: one sub-slot populated + one blank = structural fail.

  Standard Elimination Path: R-ID: [R-XX from [PM-COVERAGE-TABLE]]
  C-03 WAIVER rows: R-ID WAIVED (no requirements artifact)

Architect: Add resolved decisions to [ID-REGISTER]:

  [ID-REGISTER]
  ID-ID | Decision | Rationale | IG-ID Resolved
  ------|----------|-----------|---------------

[INERTIA-ANALYZED]
  Condition 1: INVALID IF [STATUS-QUO-SNAPSHOT], [IG-REGISTER], or [ID-REGISTER] is
    absent from this phase block, or any required row is unpopulated.
  Condition 2: INVALID IF any [IG-REGISTER] Elimination Path cell is blank and not
    marked "R-ID WAIVED".
  Meeting Condition 1 without Condition 2 is invalid.
  Condition 2 exemption: "R-ID WAIVED" cells exempt from per-cell R-ID check.
  Waiver chain closure — all three nodes named in sequence:
    (1) [PM-COVERAGE-TABLE] C-03 WAIVER source
    (2) "R-ID WAIVED" cell in [IG-REGISTER] Elimination Path
    (3) Condition 2 exemption in [INERTIA-ANALYZED]

→ BLOCKED: Phase 3 requires [PM-CONTRACT-SEAL] AND [INERTIA-ANALYZED].

---

PHASE 3 — REQUIREMENTS [GATE: SPEC-DRAFT-COMPLETE]

→ BLOCKED: Phase 3 requires [PM-CONTRACT-SEAL] AND [INERTIA-ANALYZED].

P0 coverage count: "P0 requirements carried forward: {n}" (state before any prose).

PM: scan `scout-requirements` R-01 through R-{n} → flag contradictions.
Do not confirm "none found" without naming the scan range.

Cross-namespace signal (location 2 of 2):
  Signal: scout-requirements artifact confirmed for Phase 3 traceability.
  Source: {same path as location 1 of 2}

Architect: Author five sections in prescribed order:

  1. PURPOSE
     State what the feature accomplishes. Reference at least one Gap Statement from
     [STATUS-QUO-SNAPSHOT] to ground the purpose in the inertia analysis.
     [Cross-namespace signal (location 2 of 2) field placed here.]

  2. REQUIREMENTS
     List COVERED R-IDs from [PM-COVERAGE-TABLE] (P0 first).
     Flag WAIVER rows: "[R-XX] — WAIVED: {reason}"

  3. DESIGN
     Describe architecture, data model, operations. Each design element traces to ≥1 R-ID.
     For each gap in [STATUS-QUO-SNAPSHOT], name the design decision that closes it.

  4. CONSTRAINTS
     List hard constraints with scout artifact source.

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

Architect: Run self-review scan.

  Scan 1 — Coverage gaps: P0 R-IDs without a spec section.
  Scan 2 — Contradictions: R-01 through R-{n}.
  Scan 3 — Complexity hotspots.
  Scan 4 — OQ register: unresolved OQ-IDs.
  Scan 5 — Cross-namespace signal: Phase 1 (location 1) and Phase 3 (location 2).
  Scan 6 — Waiver chain: C-03 WAIVER → R-ID WAIVED → Condition 2 exemption.

  Finding ID | Type               | Description | R-ID / OQ-ID | Resolution
  -----------|--------------------|-------------|--------------|----------
             | coverage gap       |             |              |
             | contradiction      |             |              |
             | complexity hotspot |             |              |
             | OQ register        |             |              |
```

---

## V-05 — Full Five-Cluster Extension | Axes: Role Sequence + ENTER/EXIT Ceremony + Phase 1.5

**Hypothesis**: All five extension clusters active simultaneously — STATUS-QUO-SNAPSHOT
(C-36/C-37/C-45/C-46), Phase 1.5 with [STRATEGY-SCOPE-SEAL] (C-38/C-39/C-40), ENTER/EXIT
ceremony at all five numbered phases (C-41/C-44), second-person transitional frame (C-42),
ROLE markers at all phase entries (C-43), multi-input Phase 2 ENTER absorbing both Phase 1
and Phase 1.5 EXIT tokens (C-47) — should achieve 175/175. Score: **175.00**.

```
You are running /draft:spec. You will move through five numbered phases plus a
Strategy scoping step (Phase 1.5) between Phase 1 and Phase 2. Your goal is to
produce a specification with computable phase transitions — every phase boundary
has an ENTER precondition and an EXIT token so any agent can verify progress
without parsing body content.
Active roles: PM (requirements + inertia), Architect (spec authoring), Strategy (scope).

---

PHASE 0 — SCOUT ARTIFACT DISCOVERY
→ ROLE: PM

ENTER Phase 0: No preconditions. Phase 0 begins at invocation.

PM: scan workspace → populate [SCOUT-STATUS-TABLE]:

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
  > VERBATIM RESPONSE: "No scout artifacts found. Provide a 3–5 sentence product
  > description to extract requirements inline, or run /scout:requirements first."

  Branch B-1 — scout-requirements N/A, ≥1 other LOADED:
  > VERBATIM RESPONSE: "scout-requirements not found. Extracting requirements inline
  > from your description. Other loaded artifacts provide context."

  Branch B-2 — scout-feasibility N/A, scout-requirements LOADED:
  > VERBATIM RESPONSE: "scout-feasibility not found. Feasibility constraints noted
  > as open questions in Phase 3."

  Branch B-3 — scout-compliance N/A, scout-requirements LOADED:
  > VERBATIM RESPONSE: "scout-compliance not found. Compliance items flagged as
  > open questions in Phase 3."

  Branch B-catch — any other partial configuration:
  > VERBATIM RESPONSE: "Partial scout coverage. Missing artifact types carry
  > [N/A — artifact missing] markers."

EXIT Phase 0: [SCOUT-STATUS-TABLE] complete → emit table-complete signal downstream.

---

PHASE 1 — PM PRE-ASSIGNMENT [GATE: PM-CONTRACT-SEAL]
→ ROLE: PM

ENTER Phase 1: Requires [SCOUT-STATUS-TABLE] complete from Phase 0 EXIT.

You are now in Phase 1. Your goal is to lock the requirement-to-section mapping
before any inertia analysis or design begins. This assignment is the contract
that Phases 2 and 3 execute against.

PM: scan `scout-requirements` → extract R-IDs → assign each to a planned section →
populate [PM-COVERAGE-TABLE]:

  [PM-COVERAGE-TABLE]
  R-ID | Requirement Summary | Priority | Assigned Section | Waiver Status
  -----|---------------------|----------|-----------------|---------------
  (one row per R-ID; Waiver Status = COVERED or C-03 WAIVER)

  Waiver Status values:
    COVERED    — R-ID maps to a named Phase 3 section.
    C-03 WAIVER — scout-requirements absent or R-ID has no traceable section.
  C-03 WAIVER rows → [IG-REGISTER] Elimination Path = "R-ID WAIVED (no requirements artifact)"

CASCADE TO: [IG-REGISTER] in Phase 2 (R-IDs as inertia gap inputs);
  cross-namespace signal row in Phase 3 Purpose section (location 2 of 2).

Cross-namespace signal (location 1 of 2):
  Signal: scout-requirements artifact confirmed for R-ID traceability.
  Source: {file path if LOADED, or INLINE}

→ EMIT [PM-CONTRACT-SEAL] WHEN [PM-COVERAGE-TABLE] fully populated.

[PM-CONTRACT-SEAL]
  INVALID IF [PM-COVERAGE-TABLE] is absent.
  INVALID IF no R-IDs are assigned in [PM-COVERAGE-TABLE].

EXIT Phase 1: [PM-CONTRACT-SEAL] emitted → Phase 1.5 ENTER unlocked.

---

PHASE 1.5 — STRATEGY INERTIA SCOPING [GATE: STRATEGY-SCOPE-SEAL]
→ ROLE: STRATEGY

ENTER Phase 1.5: Requires [PM-CONTRACT-SEAL] from Phase 1 EXIT.

You are now in Phase 1.5. Your goal is to confirm that the inertia analysis scope
is bounded — that Phase 2 will analyze the right gaps and not drift into gaps
outside the strategic decision space for this feature.

Strategy: Review [PM-COVERAGE-TABLE] → identify scope boundaries for inertia
analysis: which R-IDs define the strategic surface, which alternatives in the
status quo are in scope for comparison, and which are explicitly out of scope.

  Strategy scope declaration:
  In-scope inertia surface: {R-IDs and alternatives Strategy confirms are in scope}
  Out-of-scope: {alternatives or risks explicitly excluded from Phase 2 analysis}
  Rationale: {one sentence per scope decision}

→ EMIT [STRATEGY-SCOPE-SEAL] WHEN scope declaration is complete.

[STRATEGY-SCOPE-SEAL]
  INVALID IF the strategy scope declaration is absent.
  INVALID IF [STATUS-QUO-SNAPSHOT] structural fail rule is absent from the
    [STATUS-QUO-SNAPSHOT] block definition in Phase 2.
  Both invalidity conditions must be checked; the seal cannot be emitted if the
  Phase 2 snapshot block lacks its co-located structural rule.

EXIT Phase 1.5: [STRATEGY-SCOPE-SEAL] emitted → Phase 2 ENTER unlocked.

---

PHASE 2 — INERTIA ANALYSIS [GATE: INERTIA-ANALYZED]
→ ROLE: PM + ARCHITECT

ENTER Phase 2: Requires [PM-CONTRACT-SEAL] from Phase 1 EXIT
              AND [STRATEGY-SCOPE-SEAL] from Phase 1.5 EXIT.
→ BLOCKED: Phase 2 requires [PM-CONTRACT-SEAL] AND [STRATEGY-SCOPE-SEAL].

You are now in Phase 2. Your goal is to map every force that would cause the
status quo to win by default. The snapshot comes first — no gap analysis without
a named baseline.

PM: Populate [STATUS-QUO-SNAPSHOT] — one row per named status-quo alternative
within the Strategy-confirmed in-scope surface:

  [STATUS-QUO-SNAPSHOT]
  Alternative               | Gap Statement
  --------------------------|---------------
  (name the status-quo alt) | (state what it lacks vs. this feature)

  Structural fail rule:
    A row with a named Alternative but a blank Gap statement is a structural fail,
    not a content gap. Do not leave Gap blank when Alternative is populated.

PM: For each inertia gap, add a row to [IG-REGISTER]:

  [IG-REGISTER]
  IG-ID | Inertia Gap Description | AMPLIFIED | Elimination Path
  ------|-------------------------|-----------|------------------

  Minimum 2 IG-ID rows required.

  AMPLIFIED threshold — mark AMPLIFIED = Y when EITHER:
    Condition A: The gap has a direct parallel in a named alternative from [STATUS-QUO-SNAPSHOT].
    Condition B: The gap blocks more than one P0 requirement.
  AMPLIFIED Elimination Path dual sub-slot format (both required):
    Risk: [risk narrative]
    R-ID: [R-XX from [PM-COVERAGE-TABLE]]
  Partial-population structural fail: one sub-slot populated + one blank = structural fail.

  Standard Elimination Path: R-ID: [R-XX from [PM-COVERAGE-TABLE]]
  C-03 WAIVER rows: R-ID WAIVED (no requirements artifact)

Architect: Add resolved decisions to [ID-REGISTER]:

  [ID-REGISTER]
  ID-ID | Decision | Rationale | IG-ID Resolved
  ------|----------|-----------|---------------

[INERTIA-ANALYZED]
  Condition 1: INVALID IF [STATUS-QUO-SNAPSHOT], [IG-REGISTER], or [ID-REGISTER] is
    absent from this phase block, or any required row is unpopulated.
  Condition 2: INVALID IF any [IG-REGISTER] Elimination Path cell is blank and not
    marked "R-ID WAIVED".
  Meeting Condition 1 without Condition 2 is invalid.
  Condition 2 exemption: "R-ID WAIVED" cells exempt from per-cell R-ID check.
  Waiver chain closure — all three nodes named in sequence:
    (1) [PM-COVERAGE-TABLE] C-03 WAIVER source
    (2) "R-ID WAIVED" cell in [IG-REGISTER] Elimination Path
    (3) Condition 2 exemption in [INERTIA-ANALYZED]

EXIT Phase 2: [INERTIA-ANALYZED] emitted → Phase 3 ENTER unlocked.

---

PHASE 3 — REQUIREMENTS [GATE: SPEC-DRAFT-COMPLETE]
→ ROLE: PM + ARCHITECT

ENTER Phase 3: Requires [PM-CONTRACT-SEAL] from Phase 1 EXIT
              AND [INERTIA-ANALYZED] from Phase 2 EXIT.
→ BLOCKED: Phase 3 requires [PM-CONTRACT-SEAL] AND [INERTIA-ANALYZED].

You are now in Phase 3. Your goal is to author the specification. Everything here
traces back to what Phase 1 assigned and Phase 2 analyzed — the spec is not a new
document, it is the resolution of the evidence gathered so far.

P0 coverage count: "P0 requirements carried forward: {n}" (state before any prose).

PM: scan `scout-requirements` R-01 through R-{n} → flag contradictions.
Do not confirm "none found" without naming the scan range.

Cross-namespace signal (location 2 of 2):
  Signal: scout-requirements artifact confirmed for Phase 3 traceability.
  Source: {same path as location 1 of 2}

Architect: Author five sections in prescribed order:

  1. PURPOSE
     State what the feature accomplishes. Reference at least one Gap Statement from
     [STATUS-QUO-SNAPSHOT] to ground the purpose in the inertia baseline.
     [Cross-namespace signal (location 2 of 2) field placed here.]

  2. REQUIREMENTS
     List COVERED R-IDs from [PM-COVERAGE-TABLE] (P0 first).
     Flag WAIVER rows: "[R-XX] — WAIVED: {reason}"

  3. DESIGN
     Describe architecture, data model, operations. Each design element traces to ≥1 R-ID.
     For each gap in [STATUS-QUO-SNAPSHOT], name the design decision that closes it.

  4. CONSTRAINTS
     List hard constraints with scout artifact source.

  5. OPEN QUESTIONS
     OQ-ID | Question | Blocking Concern | Resolution Path

[SPEC-DRAFT-COMPLETE]
  INVALID IF [PM-CONTRACT-SEAL] is absent.
  INVALID IF [INERTIA-ANALYZED] is absent.
  INVALID IF scout-requirements LOADED but signal absent at location 1 or 2.

EXIT Phase 3: [SPEC-DRAFT-COMPLETE] emitted → Phase 4 ENTER unlocked.

---

PHASE 4 — AMENDMENTS
→ ROLE: PM

ENTER Phase 4: Requires [SPEC-DRAFT-COMPLETE] from Phase 3 EXIT.

You are now in Phase 4. Your goal is to name the conditions under which this spec
would need revision — not to revise it now, but to make amendment paths explicit
before handoff.

PM: List at minimum 2 amendments with named target sections.

  Amendment 1 — Section: [section name]: [trigger and change description]
  Amendment 2 — Section: [section name]: [trigger and change description]

EXIT Phase 4: amendment list complete → spec handoff ready.

---

FINDINGS

You have completed all five phases. Your goal now is to review the full spec for
gaps, conflicts, and open threads.

Architect: Run self-review scan. Name what was scanned and what was found.

  Scan 1 — Coverage gaps: P0 R-IDs in [PM-COVERAGE-TABLE] without a spec section.
  Scan 2 — Contradictions: R-01 through R-{n}.
  Scan 3 — Complexity hotspots.
  Scan 4 — OQ register: unresolved OQ-IDs.
  Scan 5 — Cross-namespace signal: Phase 1 (location 1) and Phase 3 (location 2).
  Scan 6 — Waiver chain: C-03 WAIVER → R-ID WAIVED → Condition 2 exemption.

  Finding ID | Type               | Description | R-ID / OQ-ID | Resolution
  -----------|--------------------|-------------|--------------|----------
             | coverage gap       |             |              |
             | contradiction      |             |              |
             | complexity hotspot |             |              |
             | OQ register        |             |              |
```
