## flow-lifecycle — Skill Body Variations V-01 through V-05 (Rubric v12)

---

## V-01 — Axis: Role Sequence
**Hypothesis:** Establishing the role registry as the zero-step schema anchor — before phases, states, or decisions — forces domain qualification to propagate forward into every downstream section rather than being retrofitted after gaps are found.

---

```markdown
You are simulating a multi-step business document lifecycle.

Lifecycle: {{lifecycle_name}}
Default if unspecified: Lead-to-Order (L2O)

---

## STEP 0A — Lifecycle Entry Inventory (Pre-Schema)

Write this block before any schema section. Enumerate ≥3 lifecycle entry triggers.
Each trigger must name:
- LT-ID (LT-01, LT-02, ...)
- Trigger Description
- Trigger Source: system event | role action | time condition
- Initial State activated
- Initial Phase activated

| LT-ID | Trigger Description | Trigger Source | Initial State | Initial Phase |
|-------|---------------------|----------------|---------------|---------------|

This block is the traceability anchor for Sections 1 and 2. Every role must trace to
a LT-ID. Every phase entry trigger must trace to a LT-ID.

---

## STEP 0B — Orthogonal Failure Surface Taxonomy (Pre-Schema)

Before authoring any schema section, enumerate ≥3 orthogonal structural failure
surfaces — one per distinct gate domain in this schema. For each:

| FS-ID | Failure Surface Name | Defect Category | Criterion / Gate That Closes It |
|-------|---------------------|-----------------|--------------------------------|

Failure surfaces must correspond to distinct gate domains (e.g., schema-entry defects,
lifecycle-structure defects, decision-quality defects). A failure surface that restates
another's category is a structural duplicate and does not count.

---

## SECTION 1 — Role Registry

Author this section FIRST, before any state name, phase name, or decision name is
written. Every piece of downstream content must use R-IDs drawn from this registry.

Column rules (enforced at point of use):

**Role Title:** Mandatory domain-qualified title. "Approver", "Owner", "Reviewer"
without domain context does not count and is a structural fail for C-05.

**LT-ID Trace:** Each role must trace to ≥1 LT-ID from Step 0A or carry
SECONDARY:rationale naming why this role is not present at any lifecycle entry point.

**Exception Handler Y/N:** Mandatory. Blank is a structural fail. Only roles
designated Y may be assigned as Handler R-IDs in the Exception Catalog (Section 5).

| R-ID | Role Title (domain-qualified; generic label without domain is a fail) | Dept | LT-ID Trace or SECONDARY:rationale | Exception Handler Y/N |
|------|----------------------------------------------------------------------|------|-------------------------------------|----------------------|

Include ≥3 roles. At least one concrete domain-title example must anchor vocabulary
for downstream sections (e.g., "Senior Credit Analyst" not "Credit Analyst").

> **GATE 1 — Role Registry Complete**
> Do not proceed to Section 2 until:
> — ≥3 R-IDs present, each with domain-qualified title
> — Every R-ID has a valid LT-ID trace or SECONDARY:rationale
> — Every R-ID has Exception Handler Y/N populated
> Blocked by: C-05, C-11, C-23.
> Gate violation: Producing downstream sections before Gate 1 clears creates an
> unanchored schema where states and exceptions may reference non-existent or
> generic roles. The artifact must be discarded and rebuilt from Section 1.

---

## SECTION 2 — Phase Index

Write the phase index after Section 1. Each phase must aggregate ≥2 states — a phase
that is 1:1 with a single state is a state rename and does not count as a phase
(structural fail for C-16).

Column rules:

**Entry Trigger / LT-ID Trace:** Phase entry trigger must trace to a named LT-ID
from Step 0A, or carry DERIVED:rationale if the phase is entered only via a prior
phase's completion event.

**Exit Gate (Blocked by: C-ID):** Mandatory structured field. Name the criterion-ID(s)
the gate enforces. Blank criterion-ID is a structural fail for C-39.

| Phase | Entry Trigger | LT-ID Trace or DERIVED:rationale | States Included | Completion Condition | SLA Envelope | SLA Risk | Exit Gate (Blocked by: C-ID) |
|-------|---------------|----------------------------------|-----------------|---------------------|--------------|----------|------------------------------|

Include ≥3 phases. Annotate ≥1 phase with SLA risk naming a causal bottleneck.

> **GATE 2 — Phase Index Complete**
> Do not proceed to Section 3 until:
> — All phase rows contain LT-ID traces or DERIVED:rationale
> — All phase rows contain Exit Gate criterion references (no blanks)
> — ≥1 phase annotated with SLA risk + causal bottleneck
> Blocked by: C-16, C-39.

---

## SECTION 3 — State Transition Trace

Write ≥6 named states. Each state must draw its Owner R-ID from the Section 1
registry (no R-IDs invented here).

Column rules:

**Entry Trigger / Exit Trigger:** Must be explicit conditions. "Then X happens" or
"X leads to Y" language without a named triggering condition does not count and is
a structural fail for C-01.

| State-ID | State Name | Entry Trigger (explicit condition required) | Exit Trigger (explicit condition required) | Owner R-ID | Phase |
|----------|------------|--------------------------------------------|--------------------------------------------|------------|-------|

> **GATE 3 — State Trace Complete**
> Do not proceed to Section 4 until ≥6 state rows present, each with explicit
> entry and exit triggers and valid Phase and R-ID references.
> Blocked by: C-01.

---

## SECTION 4 — Decision Table

Write ≥3 named decision points. Owner R-IDs must be drawn from Section 1.

Column rules:

**Decision Condition (threshold type: dollar amount | day count | retry count —
e.g., `"Order value > $25,000"`):** Conditions must be operationally testable
without further interpretation. Qualifying threshold types: dollar amount, day count,
retry count. Example of a passing value: `"Invoice age > 30 days"`. Qualitative
conditions ("large", "significant", "urgent") without a quantified threshold do not
count and are a structural fail for C-17. Both the category taxonomy (dollar amount,
day count, retry count) and a quoted example with comparison operator and unit are
required — taxonomy without example leaves format ambiguous; example without taxonomy
leaves category-boundary ambiguous.

**Fallback Branch:** Names the holding state or escalation path when the decision
mechanism is impaired (role unavailable, system down, config missing). Mechanism
impairment is distinct from process exceptions and must be treated as its own branch.

| D-ID | Decision Name | Decision Condition (threshold type: dollar amount \| day count \| retry count — e.g., `"Order value > $25,000"`) | Owner R-ID | Branch A (condition met) | Branch B (condition not met) | Fallback Branch (mechanism impaired) |
|------|---------------|------------------------------------------------------------------------------------------------------------------|------------|--------------------------|------------------------------|--------------------------------------|

---

## SECTION 5 — Exception Catalog

> **GATE 4 — Exception Catalog Upstream Boundary**
> Do not author exception flows until Section 3 (State Trace) and Section 4
> (Decision Table) are complete and their gates cleared.
> Blocked by: C-30, C-32.
> Gate violation: Exception flows authored before the state trace is stable will
> reference states and decisions that may shift, producing misaligned exception paths.
> The artifact must be discarded and rebuilt from Section 3.

Write ≥3 exception flows. Each must name a domain-qualified handler drawn from the
Section 1 registry.

Column rules:

**Handler R-ID (Mandatory — must trace to Exception Handler = Y in Section 1 Role
Registry; blank or uncertified handler is a structural fail for C-21 and C-23):**
This column enforces backward pre-certification. Before assigning a Handler R-ID,
verify the role carries Exception Handler = Y in Section 1. A Handler R-ID pointing
to a role with Exception Handler = N is an uncertified handler defect.

| EX-ID | Triggering Condition | Divergence Phase / Step | Handler R-ID (Mandatory; must trace to Exception Handler = Y in Role Registry; blank or uncertified is a fail) | Recovery Path or Terminal State |
|-------|---------------------|------------------------|----------------------------------------------------------------------------------------------------------------|--------------------------------|

> **GATE 5 — Exception Catalog Downstream Boundary**
> Do not proceed to Section 6 until all exception flows have a certified Handler R-ID
> (traceable to Exception Handler = Y in Section 1) and a named recovery path or
> terminal state.
> Blocked by: C-30, C-32.

---

## SECTION 6 — Terminal States and Check V

List all terminal states. Include ≥1 SUCCESS terminal and ≥1 FAILURE/CANCEL terminal.

| Terminal State | Type (SUCCESS / FAILURE / CANCEL) | Paths That Reach This Terminal |
|----------------|-----------------------------------|-------------------------------|

**Check V — Per-Path Terminal Confirmation:**
For each traced path (happy path + each exception path EX-01, EX-02, ...),
confirm which terminal state it reaches. This is a per-path structural check,
not a count. Every row must show CLOSED before the artifact may be written.

| Path ID | Path Description | Terminal Reached | Check V Status |
|---------|-----------------|-----------------|----------------|

All Check V rows must show CLOSED before proceeding to the Production Gate.

---

## SECTION 7 — Parallel Paths

Describe ≥1 parallel path. Name the concurrent states, join condition, and join
owner R-ID. If no parallel paths exist, declare: "No parallel paths. Rationale: [reason]."

---

## SECTION 8 — Bottlenecks and Gaps

Bottlenecks (≥2): each names cause and impact.
Process Gaps (≥1): each names the missing step and consequence.

---

## SECTION 9 — Edge Cases

Write ≥2 edge cases distinct from Section 5 exception flows. Each names: scenario,
gap reason, consequence.

---

## SECTION 10 — Cross-Lifecycle Dependencies

Write ≥1 cross-lifecycle handoff. Name direction, partner lifecycle, and coupling state.

---

## SECTION 11 — SLA Annotation

Annotate ≥3 states with timing. Flag ≥1 state as AT-RISK with a causal bottleneck
cross-reference to Section 8.

---

## PRODUCTION GATE

This artifact may not be written until BOTH of the following conditions are met:
1. Coverage Scan shows PASS for AC-01 through AC-N (all scan rows show CLOSED with
   distinct, non-shared evidence), AND
2. Check V (Section 6) shows CLOSED for every traced path.

Failure consequence: Any artifact produced before both conditions are met is a
structural fail. The artifact contains an incomplete lifecycle trace — at minimum,
one traced path lacks a verified terminal state or one gate-backed criterion has
no independent scan evidence. The violating artifact must be discarded and rerun
from the scan step.

---

## COVERAGE SCAN

### Pre-Schema Structural Blocks

| AC-ID | Check | Evidence (cite section + row) | Status |
|-------|-------|-------------------------------|--------|
| AC-01 | Step 0A: ≥3 LT-IDs with trigger source, initial state, initial phase | | |
| AC-02 | Step 0B: ≥3 orthogonal failure surfaces with criterion/gate mapping | | |
| AC-03 | Section 1: ≥3 R-IDs with domain-qualified titles and LT-ID traces | | |
| AC-04 | Section 1: Exception Handler Y/N present for all R-IDs | | |
| AC-05 | Step 0 cascade: LT-ID trace columns in Section 1 and Section 2 | | |

### Gate-Backed Aspirational Criteria

**Mandate: Each row must be verified by distinct schema evidence. No cell may share
the same coverage claim across these rows.**

| AC-ID | Criterion | Evidence (distinct citation required) | Defect Type if Fail | Detected By | Status |
|-------|-----------|--------------------------------------|---------------------|-------------|--------|
| AC-06 | C-13: ≥1 sequential gate with criterion-ID reference | | unterminated gate | C-13, C-20 | |
| AC-07 | C-16: Phase table with entry trigger, completion condition, SLA, exit gate | | missing phase structure | C-16 | |
| AC-08 | C-17: ≥3 measurable threshold conditions with units | | qualitative-only decision | C-17, C-29 | |
| AC-09 | C-19: Artifact-level production gate present | | no production gate | C-19 | |
| AC-10 | C-20: ≥3 gates distributed across distinct schema boundaries | | gate concentration defect | C-20 | |
| AC-11 | C-21: All exception flows have certified Handler R-ID | | uncertified exception handler | C-21, C-23 | |
| AC-12 | C-22: Production gate contains inline failure declaration | | gate missing fail-language | C-22 | |
| AC-13 | C-23: Role registry pre-certifies exception handler authority (Y/N column) | | handler authority not pre-certified | C-23 | |
| AC-14 | C-24: Remediation action named inline in gate text | | no remediation action in gate | C-24 | |
| AC-15 | C-25: Causal mechanism named inline in gate text | | no causal mechanism in gate | C-25 | |
| AC-16 | C-26: Backward-trace authority rule in Handler column header | | authority rule not at point of use | C-26, C-28 | |
| AC-17 | C-27: Scan table with ≥3 named defect categories and gate-reference column | | scan table missing or incomplete | C-27 | |
| AC-18 | C-28: Handler column header co-locates fail-declaration with authority rule | | fail language not co-located in header | C-28 | |
| AC-19 | C-29/C-31: Decision Condition header has ≥2 threshold-type categories AND quoted example | | taxonomy-only or example-only (single mechanism) | C-29, C-31 | |
| AC-20 | C-30: ≥1 gate at an exception-catalog boundary | | exception catalog ungated at both ends | C-30 | |
| AC-21 | C-32: Both exception-catalog boundaries gated (upstream + downstream) | | single-boundary gate only | C-32 | |
| AC-22 | C-33: Step 0 lifecycle inventory present before any schema section | | no pre-schema entry inventory | C-33 | |
| AC-23 | C-34: Pre-schema failure surface taxonomy with ≥3 domains | | no failure surface taxonomy | C-34 | |
| AC-24 | C-35: Non-overlapping evidence mandate stated in scan table header | | cross-row sharing not prohibited | C-35 | |
| AC-25 | C-36: Step 0 traces cascade into ≥3 downstream sections | | Step 0 is standalone | C-36 | |
| AC-26 | C-37: Defect taxonomy includes both single-mechanism failure variants for dual-mechanism criteria | | one variant missing for dual-mechanism criterion | C-37 | |
| AC-27 | C-38: Detected By column present in defect taxonomy; no blank rows | | defect types not backward-traced to gates | C-38 | |
| AC-28 | C-39: Every phase exit gate has Blocked by: C-ID field; no blanks | | phase exit gate criterion field blank | C-39 | |
| AC-29 | C-40: Check V named as secondary closure condition alongside scan-PASS in production gate | | terminal check absent from gate text | C-40 | |
| AC-30 | C-41: Coverage scan has ≥2 named semantic group headers | | flat undifferentiated scan list | C-41 | |
```

---

## V-02 — Axis: Output Format (Table-Dominant, Inline Enforcement)
**Hypothesis:** When every column header in every table carries its own anti-pattern rule and fail language, practitioners encounter quality constraints at point of entry — before they can produce a bad value — eliminating the need for separate preamble instructions.

---

```markdown
You are simulating a multi-step business document lifecycle.
Lifecycle: {{lifecycle_name}} (default: Procure-to-Pay, P2P)

All output is table-first. Every constraint is expressed as a column header rule.
Prose is used only for gate declarations. There are no introductory sections.

---

## TABLE 0A — Lifecycle Entry Triggers (complete before all other tables)

| LT-ID | Entry Trigger (name the external event, role action, or scheduled time condition that starts the lifecycle; vague descriptions like "user initiates" do not count) | Trigger Source (system event \| role action \| time condition) | Initial State (exact state name this trigger activates) | Initial Phase (exact phase name) |
|-------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------|--------------------------------------------------------|----------------------------------|

Minimum 3 rows. This table is the traceability root. Every R-ID in Table 1 and every
phase entry trigger in Table 2 must carry a column tracing to an LT-ID from this table.

---

## TABLE 0B — Failure Surface Taxonomy (complete before all other tables)

| FS-ID | Failure Surface Name (name the category of structural defect; restatements of another row's category are duplicates and do not count) | Defect Type | Schema Gate or Criterion That Closes It |
|-------|--------------------------------------------------------------------------------------------------------------------------------------|-------------|----------------------------------------|

Minimum 3 rows. Rows must correspond to distinct gate domains in this schema.

---

## TABLE 1 — Role Registry

> GATE R: Do not populate any other table until Table 1 has ≥3 rows with all
> required columns filled. Blocked by: C-05, C-11, C-23.

| R-ID | Role Title (domain-qualified full title required; "Approver", "Owner", "Reviewer" without domain context does not count — is a fail for C-05) | Department | LT-ID Trace (cite LT-ID from Table 0A; if role has no lifecycle-entry presence write SECONDARY:rationale) | Exception Handler (Y \| N — Mandatory; blank is a fail; only Y roles may be assigned as Handler R-IDs in Table 5) |
|------|----------------------------------------------------------------------------------------------------------------------------------------------|------------|-----------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|

Minimum 3 roles. At minimum one role title must be specific enough to anchor domain
vocabulary for downstream tables (e.g., "Senior Accounts Payable Specialist").

---

## TABLE 2 — Phase Index

| Phase-ID | Phase Name | Entry Trigger (must trace to an LT-ID from Table 0A or carry DERIVED:rationale if entered from prior phase completion only) | LT-ID or DERIVED:rationale | States Included (list ≥2 State-IDs; a phase that maps to exactly one state is a state rename — does not count, structural fail for C-16) | Completion Condition | SLA Envelope (duration with units) | SLA Risk (name causal bottleneck or write NONE) | Exit Gate (Blocked by: C-ID — Mandatory; blank is a fail for C-39) |
|---------|------------|-----------------------------------------------------------------------------------------------------------------------------|----------------------------|------------------------------------------------------------------------------------------------------------|---------------------|------------------------------------|-------------------------------------------------|-------------------------------------------------------------------|

Minimum 3 phases. At least 1 phase must carry a non-NONE SLA Risk with a named
causal bottleneck cross-referenced to Table 8.

> GATE P: Do not populate Table 3 until all Table 2 rows have valid LT-ID or
> DERIVED:rationale, SLA envelopes, and Exit Gate criterion references.
> Blocked by: C-16, C-39.

---

## TABLE 3 — State Transition Trace

| State-ID | State Name | Entry Trigger (explicit event or condition required; "then X happens" language without a named triggering condition does not count — is a fail for C-01) | Exit Trigger (explicit event or condition required; same rule as Entry Trigger) | Owner R-ID (must be an R-ID from Table 1; invented R-IDs not in Table 1 are a fail) | Phase-ID |
|----------|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|----------|

Minimum 6 rows.

> GATE S: Do not populate Table 4 until ≥6 state rows present, each with explicit
> entry/exit triggers and valid Phase-ID and R-ID references. Blocked by: C-01.

---

## TABLE 4 — Decision Table

| D-ID | Decision Name | Decision Condition (threshold type: dollar amount \| day count \| retry count; example of passing value: `"Invoice age > 30 days"`; qualitative-only conditions without a measurable comparator do not count — are a fail for C-17; taxonomy-only without example is a fail for C-31; example-only without taxonomy is a fail for C-31) | Owner R-ID (from Table 1) | Branch A: Condition Met → next State-ID | Branch B: Condition Not Met → next State-ID | Fallback Branch: Mechanism Impaired (role unavailable \| system down \| config missing → name holding state or escalation path; absence is a fail for C-15) |
|------|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------|----------------------------------------|---------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|

Minimum 3 rows.

---

## TABLE 5 — Exception Catalog

> GATE E-UP: Do not populate Table 5 until Table 3 and Table 4 are complete
> and their gates have cleared. Blocked by: C-30, C-32.
> Gate violation: Exception flows authored before state trace is stable reference
> unstable state IDs. Violating artifact must be discarded and rebuilt from Table 3.

| EX-ID | Triggering Condition | Divergence Phase / Step (name Phase-ID and State-ID where divergence begins) | Handler R-ID (Mandatory — must trace to a role with Exception Handler = Y in Table 1; blank is a fail for C-21; role with Exception Handler = N is an uncertified handler and a fail for C-23) | Recovery Path (name target State-ID or terminal state; unresolvable recovery path is a fail) |
|-------|---------------------|------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|

Minimum 3 rows.

> GATE E-DOWN: Do not populate Table 6 until all Table 5 rows have certified
> Handler R-IDs and named recovery paths or terminal states.
> Blocked by: C-30, C-32.

---

## TABLE 6 — Terminal States

| Terminal-ID | Terminal State Name | Type (SUCCESS \| FAILURE \| CANCEL) | Paths That Reach This Terminal (list Path-IDs from Table 6B) |
|-------------|--------------------|------------------------------------|-------------------------------------------------------------|

Minimum 1 SUCCESS terminal and 1 FAILURE or CANCEL terminal.

**Table 6B — Check V: Per-Path Terminal Confirmation**

| Path-ID | Path Description | Terminal Reached | Check V Status (CLOSED \| OPEN) |
|---------|-----------------|-----------------|--------------------------------|

Every row must show CLOSED before the Production Gate condition can be met.

---

## TABLE 7 — Parallel Paths

| Parallel-ID | Concurrent States (list State-IDs) | Join Condition | Join Owner R-ID |
|-------------|-----------------------------------|---------------|-----------------|

If no parallel paths exist: write one row with Parallel-ID = NONE and a rationale
in Join Condition. Blank table is a fail for C-06.

---

## TABLE 8 — Bottlenecks

| B-ID | Bottleneck Description | Cause | Impact |
|------|----------------------|-------|--------|

Minimum 2 rows.

**Table 8B — Process Gaps**

| G-ID | Missing Step | Consequence |
|------|-------------|-------------|

Minimum 1 row.

---

## TABLE 9 — Edge Cases

| EC-ID | Scenario | Gap Reason (why not handled by existing flows) | Consequence |
|-------|----------|-----------------------------------------------|-------------|

Minimum 2 rows. Rows must describe scenarios distinct from Table 5 exception flows.

---

## TABLE 10 — Cross-Lifecycle Dependencies

| CL-ID | Direction (OUTBOUND \| INBOUND) | Partner Lifecycle | Coupling State (State-ID in this lifecycle that triggers or receives the handoff) |
|-------|-------------------------------|-------------------|-----------------------------------------------------------------------------------|

Minimum 1 row.

---

## TABLE 11 — SLA Annotation

| State-ID | State Name | Typical Duration | Risk Flag (AT-RISK \| NOMINAL) | Causal Bottleneck (if AT-RISK, cite B-ID from Table 8) |
|----------|------------|-----------------|-------------------------------|-------------------------------------------------------|

Minimum 3 rows. At least 1 row must show AT-RISK with a B-ID citation.

---

## PRODUCTION GATE

This artifact may not be written until BOTH conditions are true:
1. Coverage Scan (Table 12) shows PASS — every gate-backed AC row shows CLOSED with
   distinct, non-shared evidence across rows, AND
2. Check V (Table 6B) shows CLOSED for every traced path.

Gate failure consequence: This artifact is a structural fail. The violating artifact
contains an incomplete lifecycle trace — at least one traced path has no verified
terminal state or at least one gate-backed criterion has no independent scan evidence.
The artifact must be discarded and rerun from the scan step.

---

## TABLE 12 — Coverage Scan

### Group A: Pre-Schema Structural Blocks

| AC-ID | Check | Evidence | Status |
|-------|-------|----------|--------|
| AC-01 | Table 0A: ≥3 LT-IDs with all required columns | | |
| AC-02 | Table 0B: ≥3 failure surfaces with distinct gate domains | | |
| AC-03 | Table 1: ≥3 R-IDs, domain-qualified, with LT-ID traces | | |
| AC-04 | Table 1: Exception Handler Y/N populated for all R-IDs | | |
| AC-05 | Tables 1+2: LT-ID trace columns present (Step 0 cascade) | | |

### Group B: Gate-Backed Aspirational Criteria

**Mandate: Each row in this group must cite distinct evidence. A schema element
cited in one row may not be reused as the evidence for a different row in this group.**

| AC-ID | Criterion | Evidence (distinct citation — cite table + row; no cell may share the same coverage claim across rows in this group) | Defect Type if Fail | Detected By | Status |
|-------|-----------|-----------------------------------------------------------------------------------------------------------------------|---------------------|-------------|--------|
| AC-06 | C-13: ≥1 sequential gate with criterion-ID | | unterminated gate | C-13, C-20 | |
| AC-07 | C-16: Phase table with all required columns + per-phase exit gate | | missing phase structure | C-16 | |
| AC-08 | C-17: ≥3 threshold decision conditions with units | | qualitative-only decision | C-17 | |
| AC-09 | C-19: Artifact-level production gate present | | no production gate | C-19 | |
| AC-10 | C-20: ≥3 gates at distinct section boundaries | | gate concentration | C-20 | |
| AC-11 | C-21: All EX rows have certified Handler R-ID | | uncertified exception handler | C-21, C-23 | |
| AC-12 | C-22: Production gate has inline failure declaration | | gate missing fail-language | C-22 | |
| AC-13 | C-23: Table 1 has Exception Handler Y/N column | | handler authority not pre-certified | C-23 | |
| AC-14 | C-24: Remediation action in gate text | | no remediation in gate | C-24 | |
| AC-15 | C-25: Causal mechanism in gate text | | no mechanism in gate | C-25 | |
| AC-16 | C-26: Handler column header carries backward-trace rule | | rule not at point of use | C-26, C-28 | |
| AC-17 | C-27: Scan table with ≥3 defect types + Detected By column | | scan table incomplete | C-27, C-38 | |
| AC-18 | C-28: Handler column header co-locates fail-declaration | | fail-language not co-located | C-28 | |
| AC-19 | C-29/C-31: Decision Condition header has taxonomy + quoted example | | taxonomy-only: category list present, no quoted example with operator and unit; example-only: quoted example present, no category list | C-29, C-31 | |
| AC-20 | C-30: ≥1 exception-catalog boundary gate | | catalog ungated | C-30 | |
| AC-21 | C-32: Both exception-catalog boundaries gated | | single-boundary only | C-32 | |
| AC-22 | C-33: Step 0 entry inventory present before schema | | no pre-schema inventory | C-33 | |
| AC-23 | C-34: Pre-schema failure surface taxonomy | | no failure surface taxonomy | C-34 | |
| AC-24 | C-35: Non-overlapping mandate in scan header | | sharing not prohibited | C-35 | |
| AC-25 | C-36: Step 0 cascade into ≥3 downstream tables | | Step 0 standalone | C-36 | |
| AC-26 | C-37: Taxonomy-only AND example-only defect variants for C-31 | | one variant missing | C-37 | |
| AC-27 | C-38: Detected By column in defect taxonomy, no blanks | | defect rows lack gate pointer | C-38 | |
| AC-28 | C-39: Every phase exit gate has Blocked by: C-ID | | phase gate criterion blank | C-39 | |
| AC-29 | C-40: Check V named as co-equal condition in production gate | | terminal check absent from gate | C-40 | |
| AC-30 | C-41: Scan has ≥2 named group headers | | flat scan list | C-41 | |
```

---

## V-03 — Axis: Lifecycle Emphasis (Phase-First, Deep Phase Analysis)
**Hypothesis:** Anchoring the entire simulation to an explicit phase-by-phase analysis — where each phase is fully characterized before the state machine is drawn — reduces unterminated paths and missing terminal states because every phase's exit conditions are known before any state transition is written.

---

```markdown
You are simulating a multi-step business document lifecycle.
Lifecycle: {{lifecycle_name}} (default: Period Close)

This simulation is organized phase-first. The lifecycle is characterized by its
phases before individual states are enumerated. Every state in Section 3 must
belong to a phase established in Section 2. Every exception flow must name the
phase where it diverges.

---

## STEP 0 — Pre-Schema Foundations

Before any schema section, complete the following two blocks.

**Block 0A — Lifecycle Entry Inventory**

Enumerate every external event, role action, or time condition that can start this
lifecycle (minimum 3). Assign LT-IDs.

| LT-ID | Trigger Description | Trigger Source | Initial Phase Activated | Initial State Activated |
|-------|---------------------|----------------|------------------------|------------------------|

**Block 0B — Failure Surface Map**

Map ≥3 orthogonal structural failure surfaces to the gates that close them.
Each failure surface must correspond to a distinct gate domain.

| FS-ID | Failure Surface | Defect Category | Gate or Criterion |
|-------|----------------|-----------------|-------------------|

---

## STEP 0C — Failure Surface Framing Statement

Before Section 1, write a sentence-level framing of what each gate in this schema
prevents. This framing is authored before the sections it describes. One framing
entry per gate domain (≥3). Format: "Gate [name] prevents [defect type] by [mechanism]."

---

## SECTION 1 — Role Registry

Establish domain-qualified roles with exception-handler designation and Step 0A trace.

| R-ID | Role Title (domain-qualified — generic labels without domain context are a fail) | Dept | LT-ID Trace | Exception Handler Y/N |
|------|---------------------------------------------------------------------------------|------|-------------|----------------------|

≥3 roles. At least one anchors domain vocabulary with a concrete title.

> GATE 1 — Roles complete before phases. Blocked by: C-05, C-11, C-23.

---

## SECTION 2 — Phase Analysis (Primary Framing Layer)

This is the primary structural layer of this simulation. Spend the most space here.
Each phase is analyzed fully before the state trace is written.

For each phase, produce a complete sub-table:

### Phase [N]: [Phase Name]

**Phase Summary Table:**

| Field | Value |
|-------|-------|
| Entry Trigger | [must trace to LT-ID from Block 0A, or DERIVED:rationale] |
| LT-ID Trace | [LT-ID or DERIVED:rationale] |
| Completion Condition | [explicit observable condition] |
| SLA Envelope | [duration with units] |
| SLA Risk | [bottleneck name or NONE] |
| States Included | [list ≥2 State-IDs that this phase will contain] |
| Key Roles | [list R-IDs active in this phase] |
| Critical Decision | [D-ID of the decision point with the highest-impact branch in this phase, or NONE] |
| Exception Surface | [most likely exception type in this phase, to be detailed in Section 5] |
| Exit Gate | Blocked by: [C-ID] |

**Phase Process Narrative:**
In 3–5 sentences, describe what this phase accomplishes, what can go wrong,
and what must be true for the phase to exit cleanly.

---

Produce sub-tables for ≥3 phases. At least 1 phase must be annotated with non-NONE
SLA Risk and a named causal bottleneck.

> GATE 2 — Phase analysis complete before state trace. Blocked by: C-16, C-39.
> Gate violation: Writing state transitions before phase boundaries are established
> creates states that cannot be assigned to phases, producing an unverifiable lifecycle
> trace. The artifact must be discarded and rebuilt from Section 2.

---

## SECTION 3 — State Transition Trace

Now that phase boundaries are established in Section 2, enumerate individual states.
Every state must reference a Phase established above.

| State-ID | State Name | Entry Trigger (explicit event — "then X happens" is a fail for C-01) | Exit Trigger (explicit event — same rule) | Owner R-ID | Phase |
|----------|------------|-----------------------------------------------------------------------|-------------------------------------------|------------|-------|

≥6 states.

> GATE 3 — States complete before decisions. Blocked by: C-01.

---

## SECTION 4 — Decision Table

| D-ID | Decision Name | Decision Condition (qualifying threshold types: dollar amount, day count, retry count; example: `"Invoice age > 30 days"`; qualitative-only is a fail; taxonomy without example is a fail; example without taxonomy is a fail) | Owner R-ID | Branch A | Branch B | Fallback (mechanism impaired → holding state or escalation) |
|------|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|----------|----------|-------------------------------------------------------------|

≥3 decisions. Each condition must be operationally testable.

---

## SECTION 5 — Exception Catalog

> GATE 4-UP — Exception catalog upstream boundary: do not author exception flows
> before Section 3 and Section 4 are complete. Blocked by: C-30, C-32.

For each phase identified in Section 2, address the exception surface named in that
phase's sub-table. Every exception flow must name its divergence phase.

| EX-ID | Phase of Divergence | Triggering Condition | Divergence State | Handler R-ID (must trace to Exception Handler = Y in Section 1; blank or uncertified is a fail) | Recovery Path |
|-------|---------------------|---------------------|------------------|-------------------------------------------------------------------------------------------------|---------------|

≥3 exception flows.

> GATE 4-DOWN — Exception catalog downstream boundary: do not proceed to Section 6
> before all exception flows carry a certified Handler R-ID.
> Blocked by: C-30, C-32.

---

## SECTION 6 — Terminal States

| Terminal-ID | State Name | Type | Reached By (path-IDs) |
|-------------|------------|------|----------------------|

≥1 SUCCESS, ≥1 FAILURE or CANCEL.

**Check V — Per-Path Terminal Confirmation**

Confirm terminal state for each path. All rows must show CLOSED before production gate.

| Path-ID | Path Description | Terminal Reached | Check V Status |
|---------|-----------------|-----------------|----------------|

---

## SECTION 7 — Parallel Paths

Name concurrent states, join condition, join owner R-ID.
Or declare: "No parallel paths. Rationale: [reason]."

---

## SECTION 8 — Bottlenecks (≥2) and Process Gaps (≥1)

Bottlenecks: name cause and impact.
Gaps: name missing step and consequence.

---

## SECTION 9 — Edge Cases (≥2)

Distinct from Section 5. Name scenario, gap reason, consequence.

---

## SECTION 10 — Cross-Lifecycle Dependencies (≥1)

Name direction, partner lifecycle, coupling state.

---

## SECTION 11 — SLA Annotation

Annotate ≥3 states with timing. Flag ≥1 as AT-RISK with bottleneck cross-reference.

---

## PRODUCTION GATE

This artifact may not be written until:
1. Coverage Scan shows PASS (all AC rows CLOSED, distinct evidence per row), AND
2. Check V shows CLOSED for every traced path.

Failure consequence: This artifact is a structural fail. It contains an incomplete
lifecycle trace — at least one path reaches no verified terminal state or at least
one gate-backed criterion has no independent evidence. The artifact must be
discarded and rerun from the scan step.

---

## COVERAGE SCAN

### Pre-Schema Structural Blocks

| AC-ID | Check | Evidence | Status |
|-------|-------|----------|--------|
| AC-01 | Block 0A: ≥3 LT-IDs present | | |
| AC-02 | Block 0B: ≥3 failure surfaces with gate mapping | | |
| AC-03 | Step 0C: Framing statements for each gate domain | | |
| AC-04 | Section 1: ≥3 domain-qualified roles, LT-ID traces, Exception Handler Y/N | | |
| AC-05 | Section 2 phase sub-tables include LT-ID traces (Step 0 cascade) | | |

### Gate-Backed Aspirational Criteria

**Mandate: Each row must cite distinct schema evidence. No cell may share the same
coverage claim across rows in this group.**

| AC-ID | Criterion | Evidence (distinct per row) | Defect Type if Fail | Detected By | Status |
|-------|-----------|------------------------------|---------------------|-------------|--------|
| AC-06 | C-13: ≥1 gate with criterion-ID reference | | unterminated gate | C-13, C-20 | |
| AC-07 | C-16: Full phase sub-tables with entry trigger + SLA + exit gate | | missing phase structure | C-16 | |
| AC-08 | C-17: ≥3 threshold conditions with units | | qualitative-only decision | C-17 | |
| AC-09 | C-19: Production gate present | | no production gate | C-19 | |
| AC-10 | C-20: ≥3 gates at distinct schema boundaries | | gate concentration | C-20 | |
| AC-11 | C-21: All EX flows have certified Handler R-ID | | uncertified handler | C-21, C-23 | |
| AC-12 | C-22: Gate has inline failure declaration | | no fail-language in gate | C-22 | |
| AC-13 | C-23: Role registry has Exception Handler Y/N column | | authority not pre-certified | C-23 | |
| AC-14 | C-24: Remediation action in gate text | | no remediation | C-24 | |
| AC-15 | C-25: Causal mechanism in gate text | | no mechanism | C-25 | |
| AC-16 | C-26: Handler column header has backward-trace rule | | rule not at point of use | C-26, C-28 | |
| AC-17 | C-27: Scan table with ≥3 defect categories | | scan incomplete | C-27 | |
| AC-18 | C-28: Handler header co-locates fail-declaration | | fail-language not co-located | C-28 | |
| AC-19 | C-29/C-31: Decision Condition header: taxonomy + quoted example | | taxonomy-only: category list present, no quoted example; example-only: quoted example present, no category list | C-29, C-31 | |
| AC-20 | C-30: ≥1 exception-catalog boundary gate | | catalog ungated | C-30 | |
| AC-21 | C-32: Both exception-catalog boundaries gated | | single-boundary only | C-32 | |
| AC-22 | C-33: Step 0 entry inventory before schema | | no pre-schema inventory | C-33 | |
| AC-23 | C-34: Failure surface taxonomy present | | no taxonomy | C-34 | |
| AC-24 | C-35: Non-overlapping mandate in scan | | sharing not prohibited | C-35 | |
| AC-25 | C-36: Step 0 traces cascade into ≥3 sections | | Step 0 standalone | C-36 | |
| AC-26 | C-37: Both single-mechanism failure variants for C-31 | | one variant absent | C-37 | |
| AC-27 | C-38: Detected By column in defect taxonomy | | no backward trace | C-38 | |
| AC-28 | C-39: Phase exit gates have Blocked by: C-ID | | gate criterion blank | C-39 | |
| AC-29 | C-40: Check V named in production gate | | terminal check absent | C-40 | |
| AC-30 | C-41: ≥2 named semantic groups in scan | | flat scan list | C-41 | |
```

---

## V-04 — Combined Axis: Role Sequence + Phrasing Register (Formal Imperative)
**Hypothesis:** Formal SHALL / MUST NOT / is a structural fail language, combined with role-first ordering, removes the practitioner's ability to rationalize non-compliance — every constraint is stated as an obligation with a named consequence, not a recommendation.

---

```markdown
You are simulating a multi-step business document lifecycle.
Lifecycle: {{lifecycle_name}} (default: Quote-to-Cash)

This schema is governed by formal obligation language. Every rule is stated as a
SHALL, MUST, or MUST NOT obligation. Every violation carries a named consequence.
Rules are established before the sections they govern. Roles are established before
any state, phase, or decision point is named.

---

## OBLIGATION 0 — Pre-Schema Blocks

The practitioner SHALL complete both pre-schema blocks before writing any section.

**Block 0A — Lifecycle Entry Inventory**

The practitioner SHALL enumerate ≥3 lifecycle entry triggers (LT-01, LT-02, ...).
Each trigger SHALL name its source (system event | role action | time condition),
the initial state it activates, and the initial phase it activates.
Failure to complete Block 0A before Section 1 is a structural fail for C-33.

| LT-ID | Trigger Description | Trigger Source | Initial State | Initial Phase |
|-------|---------------------|----------------|---------------|---------------|

**Block 0B — Failure Surface Taxonomy**

The practitioner SHALL enumerate ≥3 orthogonal structural failure surfaces before
any schema section. Each failure surface SHALL correspond to a distinct gate domain.
A failure surface that restates another row's domain MUST NOT be counted.
Failure to complete Block 0B before Section 1 is a structural fail for C-34.

| FS-ID | Failure Surface Name | Defect Category | Closed By (gate or criterion) |
|-------|---------------------|-----------------|-------------------------------|

---

## SECTION 1 — Role Registry (SHALL be authored before all other sections)

The practitioner SHALL establish the role registry as the first schema section.
No state name, phase name, or decision condition SHALL be written before Section 1
is complete and Gate 1 is cleared.

**Role Title:** MUST be fully domain-qualified. Generic labels ("Approver", "Owner")
without domain context SHALL NOT be used and constitute a structural fail for C-05.
The role registry SHALL include at least one concrete domain-title example that
anchors vocabulary for all downstream content (e.g., "Senior Revenue Accountant").

**LT-ID Trace:** Every role SHALL trace to ≥1 LT-ID from Block 0A, or carry
SECONDARY:rationale. A role with no LT-ID trace and no SECONDARY:rationale is
a structural fail.

**Exception Handler:** MUST be Y or N. Blank is a structural fail for C-23.
Only roles carrying Exception Handler = Y SHALL be assigned as Handler R-IDs
in Section 5. Assignment of a role carrying Exception Handler = N as a Handler
R-ID is a structural fail for C-21 and C-23.

| R-ID | Role Title (domain-qualified; generic label is a structural fail for C-05) | Dept | LT-ID Trace (or SECONDARY:rationale) | Exception Handler (Y \| N — blank is a structural fail) |
|------|---------------------------------------------------------------------------|------|--------------------------------------|--------------------------------------------------------|

Minimum 3 rows.

> **GATE 1 — Role Registry**
> The practitioner MUST NOT proceed to Section 2 until:
> — ≥3 R-IDs are present, each with a domain-qualified title
> — Every R-ID carries a valid LT-ID trace or SECONDARY:rationale
> — Every R-ID carries Exception Handler Y or N (no blanks)
> Blocked by: C-05, C-11, C-23.
> Gate violation consequence: Sections authored before Gate 1 clears contain
> role references that are unanchored, uncertified, or undifferentiated.
> The violating artifact MUST be discarded and rebuilt from Section 1.

---

## SECTION 2 — Phase Index

The phase index SHALL be authored after Section 1 and before Section 3.

**States Included:** Each phase SHALL aggregate ≥2 State-IDs. A phase that
maps to exactly one state is a state rename and SHALL NOT be counted.
This is a structural fail for C-16.

**Entry Trigger / LT-ID Trace:** Each phase entry trigger SHALL trace to a named
LT-ID from Block 0A, or carry DERIVED:rationale.

**Exit Gate:** MUST be populated. The practitioner MUST name the criterion-ID(s)
the gate enforces in the Blocked by: field. A blank criterion-ID is a structural
fail for C-39.

| Phase-ID | Phase Name | Entry Trigger | LT-ID Trace or DERIVED:rationale | States Included (≥2 State-IDs; 1:1 with state is a fail) | Completion Condition | SLA Envelope | SLA Risk (bottleneck name or NONE) | Exit Gate (Blocked by: C-ID — blank is a fail) |
|---------|------------|---------------|----------------------------------|----------------------------------------------------------|---------------------|--------------|------------------------------------|-------------------------------------------------|

Minimum 3 phases. ≥1 phase SHALL carry a non-NONE SLA Risk with a named bottleneck.

> **GATE 2 — Phase Index**
> The practitioner MUST NOT proceed to Section 3 until all phase rows carry:
> — Valid LT-ID trace or DERIVED:rationale
> — SLA envelope
> — Exit gate with criterion-ID (no blanks)
> Blocked by: C-16, C-39.

---

## SECTION 3 — State Transition Trace

States SHALL reference only Phase-IDs established in Section 2 and R-IDs
established in Section 1.

**Entry/Exit Triggers:** SHALL be explicit conditions. "Then X happens" language
without a named triggering event or condition SHALL NOT be used.
This is a structural fail for C-01.

| State-ID | State Name | Entry Trigger (explicit condition — "then X" is a fail) | Exit Trigger (explicit condition — same rule) | Owner R-ID | Phase-ID |
|----------|------------|--------------------------------------------------------|-----------------------------------------------|------------|----------|

Minimum 6 rows.

> **GATE 3 — State Trace**
> MUST NOT proceed to Section 4 until ≥6 rows present with explicit triggers
> and valid Phase-ID and R-ID references. Blocked by: C-01.

---

## SECTION 4 — Decision Table

**Decision Condition:** SHALL be operationally testable without further interpretation.
Qualifying threshold types are: dollar amount, day count, retry count.
The Decision Condition column header SHALL include BOTH:
(1) a named list of qualifying threshold types (dollar amount, day count, retry count)
AND (2) a quoted passing example with comparison operator and unit (e.g., `"Order value > $25,000"`).
Taxonomy without example is a structural fail for C-31.
Example without taxonomy is a structural fail for C-31.
Qualitative-only condition without a measurable comparator is a structural fail for C-17.

**Fallback Branch:** SHALL name the holding state or escalation path when the
decision mechanism is impaired. Mechanism impairment (role unavailable, system down,
config missing) is distinct from normal process branches and SHALL be treated
as its own branch. Absence is a structural fail for C-15.

| D-ID | Decision Name | Decision Condition (qualifying types: dollar amount \| day count \| retry count; passing example: `"Order value > $25,000"`; qualitative-only is a fail; taxonomy-only is a fail; example-only is a fail) | Owner R-ID | Branch A | Branch B | Fallback (mechanism impaired — name holding state or escalation; absence is a fail) |
|------|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|----------|----------|-------------------------------------------------------------------------------------|

Minimum 3 rows.

---

## SECTION 5 — Exception Catalog

> **GATE 4-UP — Exception Catalog Upstream Boundary**
> The practitioner MUST NOT author exception flows until Section 3 and Section 4
> are complete and their gates cleared. Blocked by: C-30, C-32.
> Gate violation consequence: Exception flows referencing unstable state IDs produce
> misaligned divergence paths. The violating artifact MUST be discarded and
> rebuilt from Section 3.

**Handler R-ID:** MUST trace to a role with Exception Handler = Y in Section 1.
Blank Handler R-ID is a structural fail for C-21.
A Handler R-ID pointing to a role with Exception Handler = N is an uncertified
handler and is a structural fail for C-23.
Before assigning any Handler R-ID, the practitioner SHALL verify Exception Handler = Y
in the Section 1 Role Registry. This backward pre-certification is mandatory.

| EX-ID | Triggering Condition | Divergence Phase / State | Handler R-ID (Mandatory — must trace to Exception Handler = Y in Section 1; blank is a fail for C-21; uncertified role is a fail for C-23) | Recovery Path |
|-------|---------------------|------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|---------------|

Minimum 3 rows.

> **GATE 4-DOWN — Exception Catalog Downstream Boundary**
> The practitioner MUST NOT proceed to Section 6 until all EX rows carry a certified
> Handler R-ID and a named recovery path or terminal state.
> Blocked by: C-30, C-32.

---

## SECTION 6 — Terminal States

SHALL include ≥1 SUCCESS terminal and ≥1 FAILURE or CANCEL terminal.

| Terminal-ID | State Name | Type | Paths That Reach It |
|-------------|------------|------|---------------------|

**Check V — Per-Path Terminal Confirmation**
The practitioner SHALL confirm, per-path (not per-count), that every traced path
reaches a named terminal state. All rows MUST show CLOSED.

| Path-ID | Description | Terminal Reached | Check V Status (CLOSED \| OPEN) |
|---------|-------------|-----------------|--------------------------------|

All rows SHALL show CLOSED before the Production Gate condition can be met.

---

## SECTION 7 — Parallel Paths

SHALL name ≥1 parallel path with concurrent states, join condition, and join
owner R-ID. OR declare no parallel paths with explicit rationale.

---

## SECTION 8 — Bottlenecks and Gaps

Bottlenecks (≥2): SHALL name cause and impact.
Process Gaps (≥1): SHALL name missing step and consequence.

---

## SECTION 9 — Edge Cases (≥2)

SHALL be distinct from Section 5 flows. Each SHALL name scenario, gap reason, consequence.

---

## SECTION 10 — Cross-Lifecycle Dependencies (≥1)

SHALL name direction, partner lifecycle, and coupling state.

---

## SECTION 11 — SLA Annotation

SHALL annotate ≥3 states with timing. ≥1 SHALL be flagged AT-RISK with bottleneck
cross-reference from Section 8.

---

## PRODUCTION GATE

The practitioner MUST NOT write the final lifecycle artifact until BOTH of the
following conditions are confirmed:
1. Coverage Scan shows PASS — every gate-backed AC row shows CLOSED with distinct,
   non-shared evidence, AND
2. Check V shows CLOSED for every traced path.

Gate failure consequence: This artifact is a structural fail. It contains an
incomplete lifecycle trace — at least one traced path reaches no verified terminal
state or at least one gate-backed criterion is supported by shared rather than
independent evidence. The violating artifact MUST be discarded and MUST be rerun
from the scan step.

---

## COVERAGE SCAN

### Pre-Schema Structural Blocks

| AC-ID | Check | Evidence | Status |
|-------|-------|----------|--------|
| AC-01 | Block 0A ≥3 LT-IDs: trigger source, initial state, initial phase | | |
| AC-02 | Block 0B ≥3 failure surfaces with criterion/gate mapping | | |
| AC-03 | Section 1: ≥3 domain-qualified roles with LT-ID traces | | |
| AC-04 | Section 1: Exception Handler Y/N in all rows | | |
| AC-05 | Step 0 cascade: LT-ID trace columns present in Section 1 and 2 | | |

### Gate-Backed Aspirational Criteria

**SHALL: Each row in this group cites distinct schema evidence. The same schema
element SHALL NOT be cited as evidence for more than one row in this group.**

| AC-ID | Criterion | Evidence (distinct per row — same element SHALL NOT cover multiple rows) | Defect Type if Fail | Detected By | Status |
|-------|-----------|-------------------------------------------------------------------------|---------------------|-------------|--------|
| AC-06 | C-13: ≥1 sequential gate with criterion-ID | | unterminated gate | C-13, C-20 | |
| AC-07 | C-16: Phase table with all required columns and exit gates | | missing phase structure | C-16 | |
| AC-08 | C-17: ≥3 threshold conditions with measurable units | | qualitative-only decision | C-17 | |
| AC-09 | C-19: Artifact-level production gate | | no production gate | C-19 | |
| AC-10 | C-20: ≥3 gates at distinct section boundaries | | gate concentration | C-20 | |
| AC-11 | C-21: All EX flows have certified Handler R-ID | | uncertified exception handler | C-21, C-23 | |
| AC-12 | C-22: Production gate has inline failure declaration | | no fail-language in gate | C-22 | |
| AC-13 | C-23: Role registry pre-certifies exception handler authority | | authority not pre-certified | C-23 | |
| AC-14 | C-24: Remediation action in gate text | | no remediation | C-24 | |
| AC-15 | C-25: Causal mechanism in gate text | | no mechanism | C-25 | |
| AC-16 | C-26: Handler column header has backward-trace rule | | rule not at point of use | C-26, C-28 | |
| AC-17 | C-27: Scan table with ≥3 named defect categories | | scan table incomplete | C-27 | |
| AC-18 | C-28: Handler header co-locates fail-declaration with authority rule | | not co-located | C-28 | |
| AC-19 | C-29/C-31: Decision Condition header has taxonomy + quoted example both | | taxonomy-only: category list present, no quoted example with operator and unit; example-only: quoted example present, no category list | C-29, C-31 | |
| AC-20 | C-30: ≥1 exception-catalog boundary gate | | catalog ungated | C-30 | |
| AC-21 | C-32: Both catalog boundaries gated | | single-boundary only | C-32 | |
| AC-22 | C-33: Step 0 entry inventory before schema | | no pre-schema inventory | C-33 | |
| AC-23 | C-34: Failure surface taxonomy | | no taxonomy | C-34 | |
| AC-24 | C-35: Non-overlapping mandate in scan | | sharing not prohibited | C-35 | |
| AC-25 | C-36: Step 0 cascade into ≥3 downstream sections | | Step 0 standalone | C-36 | |
| AC-26 | C-37: Both single-mechanism variants for C-31 in defect taxonomy | | one variant absent | C-37 | |
| AC-27 | C-38: Detected By column in defect taxonomy, no blanks | | no backward trace | C-38 | |
| AC-28 | C-39: Every phase exit gate has Blocked by: C-ID | | gate criterion blank | C-39 | |
| AC-29 | C-40: Check V named in production gate as co-equal condition | | terminal check absent from gate | C-40 | |
| AC-30 | C-41: ≥2 named semantic groups in scan | | flat scan | C-41 | |
```

---

## V-05 — Combined Axis: Lifecycle Emphasis + Inertia Framing
**Hypothesis:** Pairing phase-first lifecycle analysis with an explicit status-quo competitor column makes process gaps, bottlenecks, and missing steps visible by contrast — practitioners find what is missing not by abstract inspection but by naming what the manual/legacy process fails to provide at each phase boundary.

---

```markdown
You are simulating a multi-step business document lifecycle.
Lifecycle: {{lifecycle_name}} (default: Case Lifecycle)

This simulation runs two parallel tracks simultaneously:
- Track A: The target lifecycle (fully specified)
- Track B: The status-quo (manual/legacy) competitor at each phase

Track B is not a separate document — it is a named column in each phase analysis
and a named dimension in the bottleneck and gap analysis. Every place Track A has
a gate, state, or decision point, Track B names what the current process does instead
(or fails to do). This contrast surfaces missing steps, implicit assumptions,
and unhandled edge cases faster than abstract inspection alone.

---

## STEP 0A — Lifecycle Entry Inventory

Before all schema sections, enumerate ≥3 lifecycle entry triggers.

| LT-ID | Trigger Description | Trigger Source | Status Quo Equivalent (how does the legacy process currently initiate this path? if absent, write "MISSING in legacy") | Initial State (target) | Initial Phase (target) |
|-------|---------------------|----------------|------------------------------------------------------------------------------------------------------------------------|------------------------|------------------------|

---

## STEP 0B — Failure Surface Taxonomy

Before all schema sections, enumerate ≥3 orthogonal structural failure surfaces.

| FS-ID | Failure Surface | Defect Category | Criterion / Gate | Status Quo Exposure (how does legacy process expose this failure surface?) |
|-------|----------------|-----------------|------------------|---------------------------------------------------------------------------|

---

## SECTION 1 — Role Registry

Establish domain-qualified roles. For each role, name the status-quo equivalent
(who currently fills this function in the manual process, or ABSENT:rationale).

| R-ID | Role Title (domain-qualified — generic label without domain context is a structural fail) | Dept | LT-ID Trace | Exception Handler Y/N | Status Quo Equivalent |
|------|------------------------------------------------------------------------------------------|------|-------------|----------------------|----------------------|

≥3 roles. ≥1 role must anchor domain vocabulary with a concrete title.

> GATE 1 — Role Registry Complete. Blocked by: C-05, C-11, C-23.

---

## SECTION 2 — Phase Analysis (Primary Framing Layer)

Each phase is analyzed with a lifecycle-emphasis sub-table. The status-quo competitor
is named per phase. This contrast makes gaps explicit.

For each phase, produce a sub-table:

### Phase [N]: [Phase Name]

| Field | Target Lifecycle | Status Quo (manual/legacy) |
|-------|-----------------|---------------------------|
| Entry Trigger | [event that starts this phase] | [how legacy process starts this equivalent stage, or MISSING] |
| LT-ID Trace | [LT-ID or DERIVED:rationale] | — |
| Completion Condition | [explicit observable exit] | [how does legacy know this stage is done? or IMPLICIT:description] |
| SLA Envelope | [duration with units] | [typical duration in legacy, or UNMEASURED] |
| SLA Risk | [bottleneck name or NONE] | [is the same bottleneck present in legacy? describe] |
| States Included | [≥2 State-IDs] | — |
| Key Roles | [R-IDs] | [equivalent legacy actors] |
| Gap Surface | [what target lifecycle handles that legacy does not] | — |
| Exit Gate | Blocked by: [C-ID] | [does legacy have any equivalent exit check? describe or NONE] |

**Phase Gap Narrative:**
In 2–3 sentences, name what the target lifecycle gains over the status quo at this
phase boundary, and what risks remain if the target process reverts to manual.

---

Produce sub-tables for ≥3 phases. ≥1 must carry SLA Risk with named bottleneck.
≥1 must name a concrete gap (something target handles that legacy does not).

> GATE 2 — Phase analysis complete before state trace. Blocked by: C-16, C-39.
> Gate violation: Writing state transitions before phase gap analysis is complete
> misses the bottlenecks and edge cases that the contrast reveals. The artifact
> must be discarded and rebuilt from Section 2.

---

## SECTION 3 — State Transition Trace

| State-ID | State Name | Entry Trigger (explicit — "then X" is a fail) | Exit Trigger (explicit — same rule) | Owner R-ID | Phase-ID | Legacy State (equivalent state in status-quo process, or ABSENT:consequence) |
|----------|------------|----------------------------------------------|-------------------------------------|------------|----------|-------------------------------------------------------------------------------|

≥6 states.

> GATE 3 — State trace complete. Blocked by: C-01.

---

## SECTION 4 — Decision Table

| D-ID | Decision Name | Decision Condition (qualifying types: dollar amount \| day count \| retry count; passing example: `"Case age > 14 days"`; qualitative-only is a fail; taxonomy-only is a fail; example-only is a fail) | Owner R-ID | Branch A | Branch B | Fallback (mechanism impaired) | Legacy Decision (how is this decision made in status quo? or DISCRETIONARY:consequence) |
|------|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|----------|----------|-------------------------------|------------------------------------------------------------------------------------------|

≥3 decisions.

---

## SECTION 5 — Exception Catalog

> GATE 4-UP — Upstream exception-catalog boundary.
> Do not author exception flows before Section 3 and Section 4 are stable.
> Blocked by: C-30, C-32.

| EX-ID | Triggering Condition | Divergence Phase / State | Handler R-ID (Mandatory; must trace to Exception Handler = Y in Section 1; blank or uncertified is a fail) | Recovery Path | Legacy Handling (how does status quo handle this exception? or UNHANDLED:consequence) |
|-------|---------------------|------------------------|-----------------------------------------------------------------------------------------------------------|---------------|--------------------------------------------------------------------------------------|

≥3 exception flows.

> GATE 4-DOWN — Downstream exception-catalog boundary.
> Do not proceed to Section 6 until all EX flows have certified Handler R-IDs.
> Blocked by: C-30, C-32.

---

## SECTION 6 — Terminal States and Check V

| Terminal-ID | State Name | Type | Paths That Reach It | Legacy Equivalent (is there a corresponding terminal state in legacy, or ABSENT) |
|-------------|------------|------|---------------------|---------------------------------------------------------------------------------|

≥1 SUCCESS, ≥1 FAILURE or CANCEL.

**Check V — Per-Path Terminal Confirmation:**
All rows must show CLOSED before the Production Gate condition can be met.

| Path-ID | Path Description | Terminal Reached | Check V Status |
|---------|-----------------|-----------------|----------------|

---

## SECTION 7 — Parallel Paths

Name concurrent states, join condition, join owner R-ID — and name whether the
status-quo process runs these concurrently or serially (and the consequence if serial).

---

## SECTION 8 — Bottlenecks and Gaps

**Bottlenecks (≥2):** Each names cause, impact, and whether the same bottleneck
exists in the status-quo process (SAME, WORSE, or ABSENT with description).

**Process Gaps (≥1):** Each names the missing step, consequence, and whether the
gap originated in the status-quo process or was introduced by the target design.

---

## SECTION 9 — Edge Cases (≥2)

Distinct from Section 5. For each edge case, name whether the status-quo process
handles it (HANDLED:method | UNHANDLED:consequence | UNKNOWN).

---

## SECTION 10 — Cross-Lifecycle Dependencies (≥1)

Name direction, partner lifecycle, coupling state. Note whether the coupling
exists in the status-quo process or is new in the target design.

---

## SECTION 11 — SLA Annotation

≥3 states with timing. ≥1 AT-RISK with bottleneck cross-reference.
For AT-RISK states, note whether the legacy process has better or worse timing.

---

## PRODUCTION GATE

This artifact may not be written until BOTH conditions are met:
1. Coverage Scan shows PASS (all AC rows CLOSED, distinct evidence per row), AND
2. Check V shows CLOSED for every traced path.

Failure consequence: This artifact is a structural fail. It contains an incomplete
lifecycle trace — at least one traced path reaches no verified terminal state or at
least one gate-backed criterion carries shared rather than independent evidence.
The artifact must be discarded and rerun from the scan step.

---

## COVERAGE SCAN

### Pre-Schema Structural Blocks

| AC-ID | Check | Evidence | Status |
|-------|-------|----------|--------|
| AC-01 | Step 0A: ≥3 LT-IDs with trigger source, initial state, initial phase | | |
| AC-02 | Step 0B: ≥3 failure surfaces with gate mapping | | |
| AC-03 | Section 1: ≥3 domain-qualified roles with LT-ID traces and Exception Handler Y/N | | |
| AC-04 | Step 0 cascade: LT-ID trace columns in Section 1 (role) and Section 2 (phase) | | |

### Gate-Backed Aspirational Criteria

**Mandate: Each row in this group must cite distinct schema evidence. No cell may
share the same coverage claim across rows in this group.**

| AC-ID | Criterion | Evidence (distinct per row) | Defect Type if Fail | Detected By | Status |
|-------|-----------|------------------------------|---------------------|-------------|--------|
| AC-05 | C-13: ≥1 sequential gate with criterion-ID | | unterminated gate | C-13, C-20 | |
| AC-06 | C-16: Phase sub-tables with entry trigger, SLA, exit gate | | missing phase structure | C-16 | |
| AC-07 | C-17: ≥3 threshold conditions with measurable units | | qualitative-only decision | C-17 | |
| AC-08 | C-19: Production gate present | | no production gate | C-19 | |
| AC-09 | C-20: ≥3 gates at distinct schema boundaries | | gate concentration | C-20 | |
| AC-10 | C-21: All EX rows have certified Handler R-ID | | uncertified handler | C-21, C-23 | |
| AC-11 | C-22: Production gate has inline failure declaration | | no fail-language in gate | C-22 | |
| AC-12 | C-23: Role registry has Exception Handler Y/N column | | authority not pre-certified | C-23 | |
| AC-13 | C-24: Remediation action in gate text | | no remediation | C-24 | |
| AC-14 | C-25: Causal mechanism in gate text | | no mechanism | C-25 | |
| AC-15 | C-26: Handler column header has backward-trace rule | | rule not at point of use | C-26, C-28 | |
| AC-16 | C-27: Scan table with ≥3 named defect categories and Detected By column | | scan table incomplete | C-27, C-38 | |
| AC-17 | C-28: Handler header co-locates fail-declaration with authority rule | | not co-located | C-28 | |
| AC-18 | C-29/C-31: Decision Condition header: taxonomy (dollar amount, day count, retry count) AND quoted example both present | | taxonomy-only: category list present, no quoted example with operator and unit; example-only: quoted example present, no category list | C-29, C-31 | |
| AC-19 | C-30: ≥1 exception-catalog boundary gate | | catalog ungated | C-30 | |
| AC-20 | C-32: Both exception-catalog boundaries gated | | single-boundary only | C-32 | |
| AC-21 | C-33: Step 0 entry inventory before schema | | no pre-schema inventory | C-33 | |
| AC-22 | C-34: Failure surface taxonomy before schema | | no taxonomy | C-34 | |
| AC-23 | C-35: Non-overlapping mandate stated in scan header | | sharing not prohibited | C-35 | |
| AC-24 | C-36: Step 0 cascade into role registry, phase index, ≥1 more section | | Step 0 standalone | C-36 | |
| AC-25 | C-37: Taxonomy-only AND example-only defect variants for C-31 in scan taxonomy | | one mechanism-variant absent | C-37 | |
| AC-26 | C-38: Detected By column present in defect taxonomy, no blank rows | | defect rows lack gate pointer | C-38 | |
| AC-27 | C-39: Every phase exit gate has Blocked by: C-ID, no blanks | | gate criterion blank | C-39 | |
| AC-28 | C-40: Check V named as co-equal condition (alongside scan PASS) in production gate | | terminal check absent from gate | C-40 | |
| AC-29 | C-41: ≥2 named semantic group headers in this scan | | flat scan list | C-41 | |
```

---

## Variation Summary

| Version | Axis | Lifecycle | Key Structural Difference |
|---------|------|-----------|--------------------------|
| V-01 | Role Sequence | L2O | Role registry is zero-step anchor; every section back-references R-IDs |
| V-02 | Output Format (table-dominant) | P2P | All schema expressed as tables; column headers carry enforcement language |
| V-03 | Lifecycle Emphasis (phase-first) | Period Close | Phase sub-tables with full analysis precede state trace |
| V-04 | Role Sequence + Formal Imperative | Quote-to-Cash | SHALL/MUST/MUST NOT throughout; violations name consequences inline |
| V-05 | Lifecycle Emphasis + Inertia Framing | Case Lifecycle | Status-quo competitor column in every table; gap visible by contrast |
