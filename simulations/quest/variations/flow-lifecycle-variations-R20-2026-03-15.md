---

```markdown
---
skill: flow-lifecycle
round: 20
rubric-version: v20
date: 2026-03-16
status: VARIATE
variations: 5
rubric: simulations/quest/rubrics/flow-lifecycle-rubric-v20-2026-03-16.md
floor: flow-lifecycle-variate-R19-2026-03-16.md V-05
---

# flow-lifecycle -- Round 20 Variations (rubric v20: C-57, C-58)

Round 20 holds the R19 V-05 full floor and probes two new aspirational criteria
formalized from Round 19 scoring evidence:

- **C-57 -- Gate Defect D-ID Cross-Reference**: each named defect category in the
  gate text's inline enumeration (satisfying C-55) carries a parenthetical D-ID
  designator -- e.g., "an unterminated path (D-01), an uncertified exception handler
  (D-02), an unresolvable decision owner (D-03)" -- making the gate-to-taxonomy linkage
  row-specific rather than requiring a category-name scan. Source signal: R19 V-01/V-02/
  V-03/V-05 already carry parenthetical D-IDs on every enumerated category (HOLD/PASS);
  R19 V-04 enumerates plain prose names without D-IDs (TARGET).

- **C-58 -- Parenthetical Eligibility Binding Format**: each typed escape code in the
  LT-ID Trace and Entry Trigger column headers uses a code-token + immediately-adjacent
  parenthetical -- "SECONDARY (use only when...)" rather than "write SECONDARY -- but
  only when..." -- so code token and eligibility clause form a single typographic unit
  with no intervening instruction verb or separator. Source signal: R19 V-01/V-02/V-03/
  V-05 already use the parenthetical form (HOLD/PASS); R19 V-04 uses the dash-separator
  imperative form (TARGET).

Denominator: 56 -> 58. Aspirational count: 48 -> 50.

Two new defect types added to all variation taxonomies:
- **D-21**: Gate-defect-D-ID-absent
- **D-22**: Escape-code-non-parenthetical-binding

Two new Coverage Scan rows added to all variations:
- **AC-31**: C-57 check
- **AC-32**: C-58 check

**Variation axes explored:**

- V-01: Role sequence (pre-declaration role registry) -- single axis.
  C-57 HOLD/PASS (D-IDs stable from R19 V-01). C-58 HOLD/PASS (parenthetical form
  stable). Adds AC-31/AC-32 and D-21/D-22 to formalize verification.

- V-02: Output format (SQ Declaration as Column Contract) -- single axis.
  C-57 HOLD/PASS. C-58 HOLD/PASS. Adds AC-31/AC-32 and D-21/D-22.

- V-03: Lifecycle emphasis (phase-first framing + GATE SQ) -- single axis.
  C-57 HOLD/PASS. C-58 HOLD/PASS. Adds AC-31/AC-32 and D-21/D-22.

- V-04: Phrasing register (conversational FM-ID Guidance) + role sequence -- combination.
  C-57 TARGET: gate text updated to add parenthetical D-IDs to every inline category.
  C-58 TARGET: escape code column headers updated from dash-separator imperative form
  to code-token + immediately-adjacent parenthetical form.

- V-05: Full combination floor (R19 V-05 + AC-31/AC-32/D-21/D-22 formalization).
  C-57 HOLD/PASS. C-58 HOLD/PASS. Stability confirmation across all 58 criteria.

---

## V-01 -- Role Sequence: Pre-Declaration Role Registry + D-ID Gate Stability

**Variation axis:** Role sequence -- DOMAIN ROLE REGISTRY precedes all other content.
All R19 V-01 structural properties held. C-57 HOLD: parenthetical D-IDs already present
on every gate-enumerated category from R19 V-01. C-58 HOLD: parenthetical escape code
binding already present in LT-ID Trace and Entry Trigger column headers. Single
structural extension: D-21 and D-22 added to Defect Type Taxonomy; AC-31 and AC-32
added to Coverage Scan Group B; gate text extended with D-21/D-22 entries.

**Hypothesis:** D-ID gate cross-referencing and parenthetical eligibility binding are
axis-independent of role sequencing. The pre-declaration role registry axis positions
domain-qualified roles before any schema section, establishing LT anchor scope before
FM-IDs are defined. This sequencing does not interact with the gate's inline D-ID
enumeration (which appears far downstream) or with column header escape code binding
format (which is a per-column typographic decision). Prediction: C-57 HOLD/PASS
(AC-31 PASS, gate D-ID enumeration stable); C-58 HOLD/PASS (AC-32 PASS, parenthetical
binding stable); full aspirational 50/58 achievable.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document
or process named in the signal. Work through every numbered step in order. Establish the
DOMAIN ROLE REGISTRY first, then read the FM-ID PROTOCOL before filling the STATUS-QUO
PROCESS DECLARATION. Every field cell in the SQ Declaration begins with a compact
enforcement token; read the token before reading the content instruction.

---

### DOMAIN ROLE REGISTRY (Pre-Declaration Pass)

Author this table completely before proceeding to FM-ID PROTOCOL.

| R-ID | Role Name -- domain-qualified functional title (e.g., "Senior Credit Analyst",
"AP Supervisor"); generic labels ("Approver", "Admin", "User", "Finance team") do not
count | Domain -- process function (e.g., Sales Operations, Finance -- AP); org-unit
name without process qualifier does not count | Exception Handler (Y/N) -- Mandatory;
Y = authorized to handle exception flows; N = not authorized; at least one Y required;
blank is a fail | LT-ID Trace -- name the LT-ID(s) whose Initial State or Initial Phase
this role appears in; if role exists outside all LT scopes write
SECONDARY (use only when role has no LT-bound trigger, naming why this role exists
without any LT anchor): [rationale]; generic "N/A" or blank is a fail |
|------|------|------|------|------|
| R-01 | | | | |
| R-02 | | | | |
| R-03 | | | | |

Minimum 3 roles.

> Do not proceed to FM-ID PROTOCOL until every R-ID carries a domain-qualified title
> and an Exception Handler designation (Y/N). Generic placeholder titles are a fail.

---

### FM-ID PROTOCOL

FM-IDs are mandatory structural identifiers. They are defined in the STATUS-QUO PROCESS
DECLARATION below and must appear in every Phase Index Status-Quo Gap cell downstream.

This protocol governs all four fields in the SQ Declaration:

- **Incumbent Process**: must name a specific named process, tool, or workaround -- not
  a department and not a generic "manual" description. A single-word tool name without
  context does not count.
- **FM-01**: must name the specific detection or prevention mechanism the incumbent fails
  to provide. "Error-prone," "inefficient," or "slow" does not count. Assign identifier
  FM-01 inline.
- **FM-02**: must name a second failure mode orthogonal to FM-01. A restatement,
  subcategory, or downstream consequence of FM-01 does not count. Assign identifier
  FM-02 inline.
- **Inertia Driver**: must name the specific organizational, systemic, or economic reason
  the incumbent persists despite FM-01 and FM-02. A reason that would apply to any
  legacy process does not count.

A Phase Index Status-Quo Gap cell with no FM-ID from this block is structurally
unanchored and is a fail. Author the STATUS-QUO PROCESS DECLARATION completely before
proceeding to STEP 0A.

---

### STATUS-QUO PROCESS DECLARATION

| SQ-Field | Content |
|----------|---------|
| does not count; Mandatory -- Incumbent Process: names the specific named process, tool, or workaround being replaced; "manual process" without tool name does not count; naming a department alone does not count | |
| does not count; Mandatory -- FM-01: first failure mode; names the specific detection or prevention mechanism the incumbent fails to provide; "error-prone," "inefficient," or "slow" does not count; assign identifier FM-01 inline | |
| does not count; Mandatory -- FM-02: second failure mode orthogonal to FM-01; a restatement, subcategory, or downstream consequence of FM-01 does not count; assign identifier FM-02 inline | |
| does not count; Mandatory -- Inertia Driver: names the specific organizational, systemic, or economic reason the incumbent persists despite FM-01 and FM-02; a reason equally applicable to any legacy process does not count | |

---

### STEP 0A -- LIFECYCLE TRIGGER INVENTORY

Author this table completely before proceeding to STEP 0B.

| LT-ID | Trigger Description -- names the external event, role action, or time condition
that initiates the lifecycle; "process begins" or "a request is received" does not
count; name the specific initiating signal | Trigger Source (must be exactly:
System Event / Role Action / Time Condition; any other value is a fail) |
Initial State -- first lifecycle state activated; a generic name without lifecycle
qualifier does not count | Initial Phase -- phase boundary this trigger activates;
Mandatory; blank is a structural fail |
|-------|------|------|------|------|
| LT-01 | | | | |
| LT-02 | | | | |
| LT-03 | | | | |

Minimum 3 rows.

> Do not proceed to STEP 0B until STEP 0A is complete and every row carries all four
> fields.

---

### STEP 0B -- ORTHOGONAL FAILURE SURFACE TAXONOMY

| FS-ID | Failure Surface -- structural defect category; two rows naming the same category
are not orthogonal | Gate Domain -- schema section; "general" does not count |
Closed By (C-ID or Gate Label) -- blank is a fail |
|-------|------|------|------|
| FS-01 | | | |
| FS-02 | | | |
| FS-03 | | | |

> Do not proceed to STEP 1 until STEP 0B is complete.

---

**STEP 1 -- DOMAIN ROLE REGISTRY**

> **GATE A**: Do not open the Phase Index until the Role Registry is complete, all roles
> carry domain-qualified titles, every role has an Exception Handler designation, and
> every role has an LT-ID Trace or SECONDARY:rationale.
> Blocked by: C-05, C-11, C-23, C-36

| R-ID | Role Name -- domain-qualified functional title; generic labels do not count |
Domain -- process function | Exception Handler (Y/N) -- Mandatory; at least one Y
required; blank is a fail | LT-ID Trace (LT-ID from STEP 0A; or
SECONDARY (use only when role exists outside all LT scopes, naming why this role
exists without any LT-bound trigger): [rationale]; generic "N/A" or blank is a fail) |
|------|------|------|------|------|
| R-01 | | | | |
| R-02 | | | | |
| R-03 | | | | |

---

**STEP 2 -- PHASE INDEX**

> **GATE B**: Do not open State Trace until Phase Index complete; every Entry Trigger
> carries LT-ID or DERIVED:rationale; every Status-Quo Gap cell names a specific FM-ID.
> Blocked by: C-16, C-36, C-47

| Ph-ID | Phase Name | Entry Trigger (LT-ID from STEP 0A; or
DERIVED (use only when this phase boundary results from multiple LT-IDs combining,
naming which LT-IDs and combination logic produced this boundary): [rationale];
generic "N/A" or blank is a fail) | Status-Quo Gap (mutual-audit pair with Entry
Trigger -- co-designed as a mutual-audit pair; not a coincidence of column placement;
write FM-ID from STATUS-QUO PROCESS DECLARATION; a cell with no FM-ID is structurally
unanchored and is a fail) | Completion Condition | SLA Envelope | SLA Risk |
States Contained |
|-------|------|------|------|------|------|------|------|
| PH-01 | | | | | | | |
| PH-02 | | | | | | | |
| PH-03 | | | | | | | |

Minimum 3 phases; each phase must contain >=2 states.

---

**STEP 3 -- STATE TRACE + DECISION TABLE + PARALLEL PATHS**

Minimum 6 states.

| S-ID | Phase (Ph-ID) | State Name | Entry Condition | Exit Transitions |
Owner (R-ID) | Timing | SLA Status |
|------|------|------|------|------|------|------|------|
| S-01 | | | | | | | |
| S-02 | | | | | | | |
| S-03 | | | | | | | |
| S-04 | | | | | | | |
| S-05 | | | | | | | |
| S-06 | | | | | | | |

**Decision Points** -- minimum 3:

| D-ID | Decision Name | Decision Condition (both mechanisms required:
(1) threshold-type category from -- dollar amount, day count, retry count,
unit quantity -- AND (2) quoted example with comparison operator and unit,
e.g., "Invoice value > $10,000"; category-only is a fail; example-only is a fail) |
Owner (R-ID) | Branch: Condition Met | Branch: Condition Not Met |
Fallback -- mechanism-impairment path; names holding state or escalation target |
|------|------|------|------|------|------|------|
| D-01 | | | | | | |
| D-02 | | | | | | |
| D-03 | | | | | | |

**Parallel Paths:**

```
Fork (S-ID):    [branching state]
Branch A/B:     [concurrent paths]
Join condition: [merge requirement]
Merge owner:    [R-ID]
```

> **GATE C -- Upstream Exception-Catalog Boundary**: Do not open Exception Catalog
> until State Trace and Decision Table are complete. Source: Step 3 --> Target: Step 5.
> Blocked by: C-30, C-32.

---

**STEP 4 -- PHASE EXIT GATES**

```
Phase:          [Ph-ID: Phase Name]
Exit condition: [verifiable output]
SLA envelope:   [duration]
Success:        [Ph-ID or T-ID]
Failure:        [T-ID or exception]
Blocked by:     [C-ID(s) -- Mandatory]
```

---

**STEP 5 -- EXCEPTION CATALOG**

GATE C must be CLOSED. Minimum 3 flows.

| E-ID | Phase (Ph-ID) | Exception Name | Trigger |
Handler (R-ID) -- Must trace to a role with Exception Handler = Y in Step 1;
Mandatory; blank or uncertified role is a structural fail |
Divergence Phase/Step | Recovery State or Terminal |
|------|------|------|------|------|------|------|
| E-01 | | | | | | |
| E-02 | | | | | | |
| E-03 | | | | | | |

> **GATE D -- Downstream Exception-Catalog Boundary**: Do not open Terminal Declaration
> until all exception flows carry a certified Handler R-ID tracing to
> Exception Handler = Y. An uncertified or blank Handler R-ID is a structural fail --
> discard and rerun from Step 5.
> Source: Step 5 --> Target: Step 6. Blocked by: C-32, C-45.

---

**STEP 6 -- TERMINAL DECLARATION**

| T-ID | Terminal Name | Type (success / failure / cancel) | Reached From |
|------|------|------|------|
| T-01 | | | |
| T-02 | | | |

> **Check V** -- Status: [ OPEN / CLOSED ]
> Confirm every path reaches a named T-ID. Unterminated path = D-01. Co-equal with
> Coverage Scan PASS for Production Gate.

---

**STEP 7 -- EDGE CASE CATALOG**

| EC-ID | Edge Case | Phase (Ph-ID) | Gap Reason | Consequence |
|-------|------|------|------|------|
| EC-01 | | | | |
| EC-02 | | | | |

---

**STEP 8 -- SLA ANNOTATION**

| SLA-ID | S-ID or Ph-ID | Target Duration | At-Risk? | Risk Cause |
|--------|------|------|------|------|
| SLA-01 | | | | |
| SLA-02 | | | | |
| SLA-03 | | | | |

---

**STEP 9 -- BOTTLENECK REGISTER**

| B-ID | Phase (Ph-ID) | Bottleneck Name | Cause | Downstream Impact | Breach Link |
|------|------|------|------|------|------|
| B-01 | | | | | |
| B-02 | | | | | |

---

**STEP 10 -- GAP REGISTER**

| G-ID | Phase (Ph-ID) | Missing Step | Why Required | Risk if Absent |
|------|------|------|------|------|
| G-01 | | | | |

---

**STEP 11 -- CROSS-LIFECYCLE HANDOFF**

| Handoff Trigger | Partner Lifecycle | Direction | Fields Passed | Coupling State |
|------|------|------|------|------|
| | | | | |

---

**STEP 12 -- EXCEPTION COVERAGE AUDIT**

| Ph-ID | Phase Name | Handler Exists (Y/N) | Handler R-ID | Risk if Uncovered |
|-------|------|------|------|------|
| PH-01 | | | | |
| PH-02 | | | | |
| PH-03 | | | | |

---

**STEP 13 -- COVERAGE SCAN**

#### Group A -- Pre-Schema Structural Blocks

| AC-ID | Check | Evidence Location | Status | Defect Type if FAIL |
|-------|-------|-----------------|--------|---------------------|
| AC-01 | STEP 0A >=3 LT-IDs; all four fields per row | STEP 0A | | |
| AC-02 | STEP 0B >=3 orthogonal failure surfaces | STEP 0B | | |
| AC-21 | SQ Declaration present before STEP 0A; all four fields; Role Registry precedes SQ Declaration | SQ Declaration | | |
| AC-23 | Every SQ Declaration field cell carries inline anti-pattern token specific to that field | SQ Declaration cells | | |
| AC-24 | FM-ID PROTOCOL present before SQ Declaration; covers all four fields | FM-ID PROTOCOL | | |
| AC-25 | Every SQ Declaration field cell begins with "does not count; Mandatory" as first expression | SQ Declaration cells | | |
| AC-26 | C-52: FM-ID PROTOCOL covers Incumbent Process and Inertia Driver with governance depth equal to FM-01 and FM-02 | FM-ID PROTOCOL | | |
| AC-27 | C-53: Leading-clause token present as first expression in all four SQ Declaration field cells | SQ Declaration cells | | |
| AC-28 | C-54: FM-ID PROTOCOL closes with explicit forward sequencing instruction naming SQ Declaration and STEP 0A | FM-ID PROTOCOL closing | | |

#### Group B -- Gate-Backed Aspirational Criteria

| AC-ID | Check | Evidence Location | Status | Defect Type if FAIL |
|-------|-------|-----------------|--------|---------------------|
| AC-04 | Role Registry domain-qualified titles, Exception Handler Y/N, LT-ID Trace or SECONDARY:rationale | Step 1 | | |
| AC-05 | LT-ID Trace column header defines SECONDARY typed escape code WITH eligibility condition in parenthetical binding: SECONDARY (use only when...) | Step 1 column header | | |
| AC-06 | Entry Trigger column header defines DERIVED typed escape code WITH eligibility condition in parenthetical binding: DERIVED (use only when...) | Step 2 column header | | |
| AC-07 | All exception Handler R-IDs trace to Exception Handler = Y | Step 5 | | |
| AC-08 | Handler column header co-locates backward-trace rule and fail-declaration | Step 5 header | | |
| AC-09 | Gate D uses "certified Handler R-ID" language | Gate D text | | |
| AC-10 | Decision Condition header: category list AND quoted example | Step 3 D-table header | | |
| AC-11 | Phase exit gates: "Blocked by: [C-ID]" present | Step 4 gates | | |
| AC-12 | Gate C and Gate D both present, source and target named | Gate C + D | | |
| AC-13 | Check V present; Production Gate names Check V as co-equal condition | Step 6 + Gate | | |
| AC-22 | Phase Index Status-Quo Gap column header names the mutual-audit design principle | Step 2 header | | |
| AC-29 | C-55: production gate sentence enumerates >=3 named defect category names inline; column pointer alone is D-19 | Production Gate text | | |
| AC-30 | C-56: LT-ID Trace AND Entry Trigger headers each carry typed code format AND qualifying eligibility condition; format-only is D-20 | Step 1 + Step 2 headers | | |
| AC-31 | C-57: each named defect category in gate inline enumeration carries parenthetical D-ID (e.g., "an unterminated path (D-01)"); enumeration without D-IDs is D-21 | Production Gate text | | |
| AC-32 | C-58: LT-ID Trace AND Entry Trigger column headers use code-token + immediately-adjacent parenthetical binding; dash separator or instruction verb between code and qualifier is D-22 | Step 1 + Step 2 headers | | |

#### Group C -- General Schema Integrity

| AC-ID | Check | Evidence | Status | Defect Type if FAIL |
|-------|-------|---------|--------|---------------------|
| AC-14 | >=6 named states; each carries entry condition, exit transitions, and owner R-ID | Step 3 state table | | |
| AC-15 | >=3 exception flows; each carries trigger, certified Handler R-ID, divergence, recovery or terminal | Step 5 table | | |
| AC-16 | >=1 success terminal + >=1 failure/cancel terminal; all traced paths reach a named T-ID | Step 6 + Check V | | |
| AC-17 | >=2 bottlenecks (cause + downstream impact) + >=1 gap (missing step + risk if absent) | Steps 9 + 10 | | |
| AC-18 | >=3 decision points; each carries measurable threshold condition, owner, all branches, and fallback | Step 3 D-table | | |
| AC-19 | >=3 states with timing; >=1 phase annotated AT-RISK with causal bottleneck | Steps 3 + 2 | | |
| AC-20 | >=1 cross-lifecycle handoff with partner lifecycle, direction, fields passed, coupling state | Step 11 | | |

**Defect Type Taxonomy:**

| Defect-ID | Defect Type | Detected By |
|-----------|-------------|-------------|
| D-01 | Unterminated path: at least one traced path has no named T-ID | C-03, C-14, AC-16, Check V |
| D-02 | Uncertified exception handler: Handler R-ID does not trace to Exception Handler = Y | C-21, C-23, AC-07 |
| D-03 | Unresolvable decision owner: D-table Owner R-ID not in Step 1 | C-05, C-07, AC-18 |
| D-04 | Taxonomy-only decision condition: category enumeration present; no quoted example with operator and unit | C-31, AC-10 |
| D-05 | Example-only decision condition: quoted example present; no category enumeration | C-31, AC-10 |
| D-06 | Generic escape code: LT-ID Trace or Entry Trigger uses "N/A" or blank instead of typed SECONDARY/DERIVED code | C-44, AC-04, AC-05, AC-06 |
| D-07 | Missing Initial Phase field: LT record has Initial State column but no Initial Phase column | C-43, AC-01 |
| D-08 | Unlabeled pre-schema blocks: STEP 0A / STEP 0B section headers absent or merged | C-42, AC-02 |
| D-09 | Missing SQ Declaration: no STATUS-QUO PROCESS DECLARATION block present before STEP 0A | C-46, AC-21 |
| D-10 | FM-ID-free failure mode: SQ Declaration present but a failure mode entry carries no FM-ID identifier | C-46, AC-21 |
| D-11 | Unanchored status-quo gap: Phase Index Status-Quo Gap cell contains prose without FM-ID, or cell is blank | C-47, AC-22 |
| D-14 | Per-field anti-pattern gap: SQ Declaration field row carries no inline anti-pattern token | C-48, AC-23 |
| D-15 | Trailing-position enforcement token: SQ Declaration field carries an inline token but token is at end of cell | C-51, AC-25 |
| D-16 | Missing section-entry FM-ID Protocol block: no pre-table named section establishing FM-ID enforcement | C-50, AC-24 |
| D-17 | Partial Protocol block field coverage: Protocol block covers only FM fields; Incumbent Process or Inertia Driver absent | C-52, AC-26 |
| D-18 | Selective leading-clause token distribution: leading tokens on FM fields only; contextual field cells carry trailing tokens | C-53, AC-27 |
| D-19 | Gate-defect-pointer-only: production gate identifies violation by column pointer only without enumerating >=3 named categories inline | C-55, AC-29 |
| D-20 | Escape-code-eligibility-absent: escape code column header carries typed code format without qualifying eligibility condition | C-56, AC-30 |
| D-21 | Gate-defect-D-ID-absent: production gate enumerates defect category names inline but carries no parenthetical D-ID cross-reference on any enumerated category | C-57, AC-31 |
| D-22 | Escape-code-non-parenthetical-binding: escape code column header carries eligibility condition but binds it via instruction verb or dash separator rather than immediately-adjacent parenthetical | C-58, AC-32 |

> **PRODUCTION GATE**: Writing this artifact while any Coverage Scan row shows FAIL is a
> structural fail -- the artifact contains at least one of: an unterminated path (D-01),
> an uncertified exception handler (D-02), an unresolvable decision owner (D-03), a
> missing or partial SQ Declaration (D-09/D-10), an unanchored status-quo gap (D-11),
> a per-field anti-pattern gap (D-14), a trailing-position enforcement token (D-15),
> a missing FM-ID Protocol block (D-16), partial Protocol field coverage (D-17),
> selective leading-clause token distribution (D-18), a gate-defect-pointer-only gate
> sentence (D-19), an escape-code-eligibility-absent column header (D-20), a gate
> enumeration without D-ID cross-references (D-21), or an escape code with
> non-parenthetical eligibility binding (D-22) -- and that artifact must be discarded
> and rerun from the failing step before it is filed or used.
>
> Both conditions must be satisfied before the artifact is written:
> (1) Coverage Scan shows PASS for AC-01 through AC-32.
> (2) Check V shows CLOSED.

---

## V-02 -- Output Format: SQ Declaration as Column Contract + D-ID/Parenthetical Stability

**Variation axis:** Output format -- STATUS-QUO PROCESS DECLARATION uses a two-part
Column Contract + Fill Table format. All R19 V-02 structural properties held. C-57
HOLD: parenthetical D-IDs already present in gate text from R19 V-02. C-58 HOLD:
parenthetical escape code binding already present in LT-ID Trace and Entry Trigger
column headers. Single structural extension: D-21 and D-22 added to Defect Type
Taxonomy; AC-31 and AC-32 added to Coverage Scan Group B; gate text extended with
D-21/D-22.

**Hypothesis:** Column Contract format separates field definition from field execution,
creating structural pre-commitment at the column-specification layer. C-57 and C-58
are column-header-scoped and gate-sentence-scoped respectively -- neither interacts with
the Column Contract's separation of definition from execution. Testing whether the
Column Contract's enforcement architecture (which produces D-14/D-15 coverage via
field-definition rows) is orthogonal to gate D-ID cross-referencing and escape code
parenthetical binding. Prediction: C-57 HOLD/PASS (AC-31 PASS, D-IDs stable in
Column Contract variation); C-58 HOLD/PASS (AC-32 PASS, parenthetical binding stable);
Column Contract format does not interact with either new criterion.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document
or process named in the signal. Work through every numbered step in order. Read the
FM-ID PROTOCOL before filling the STATUS-QUO PROCESS DECLARATION. The SQ Declaration
uses a two-part format: a Column Contract defines each field, followed by a fill table.
Read the Column Contract completely before filling the Content column.

---

### FM-ID PROTOCOL

FM-IDs are mandatory structural identifiers. They are defined in the STATUS-QUO PROCESS
DECLARATION Column Contract below and must appear in every Phase Index Status-Quo Gap
cell downstream.

This protocol governs all four fields in the SQ Declaration:

- **Incumbent Process**: must name a specific named process, tool, or workaround -- not
  a department and not a generic "manual" description. A single-word tool name without
  context does not count.
- **FM-01**: must name the specific detection or prevention mechanism the incumbent fails
  to provide. "Error-prone," "inefficient," or "slow" does not count. Assign identifier
  FM-01 inline.
- **FM-02**: must name a second failure mode orthogonal to FM-01. A restatement,
  subcategory, or downstream consequence of FM-01 does not count. Assign identifier
  FM-02 inline.
- **Inertia Driver**: must name the specific organizational, systemic, or economic reason
  the incumbent persists despite FM-01 and FM-02. A reason that would apply to any
  legacy process does not count.

A Phase Index Status-Quo Gap cell with no FM-ID from this block is structurally
unanchored and is a fail. Author the STATUS-QUO PROCESS DECLARATION completely before
proceeding to STEP 0A.

---

### STATUS-QUO PROCESS DECLARATION -- Column Contract

Read this table completely before filling the Content column below.

| Field | Fill Requirement | Does Not Count |
|-------|-----------------|----------------|
| does not count; Mandatory -- Incumbent Process | names the specific named process, tool, or workaround being replaced; include tool or process name and operational context | "manual process" without tool name; department or team name alone; single-word tool name without context |
| does not count; Mandatory -- FM-01 | names the specific detection or prevention mechanism the incumbent fails to provide; assign identifier FM-01 inline | "error-prone," "inefficient," "slow"; generic quality attribute; category name without naming the specific missing mechanism |
| does not count; Mandatory -- FM-02 | names a second failure mode orthogonal to FM-01; assign identifier FM-02 inline | restatement of FM-01; subcategory; downstream consequence |
| does not count; Mandatory -- Inertia Driver | names the specific organizational, systemic, or economic reason the incumbent persists despite FM-01 and FM-02 | "familiarity"; "it works well enough"; any reason equally applicable to all legacy processes |

### STATUS-QUO PROCESS DECLARATION -- Fill Table

| SQ-Field | Content |
|----------|---------|
| Incumbent Process | |
| FM-01 | |
| FM-02 | |
| Inertia Driver | |

---

### STEP 0A -- LIFECYCLE TRIGGER INVENTORY

Author this table completely before proceeding to STEP 0B.

| LT-ID | Trigger Description -- names the external event, role action, or time condition
that initiates the lifecycle; "process begins" does not count; name the specific
initiating signal | Trigger Source (System Event / Role Action / Time Condition) |
Initial State -- first lifecycle state activated; generic name without lifecycle
qualifier does not count | Initial Phase -- Mandatory; blank is a structural fail |
|-------|------|------|------|------|
| LT-01 | | | | |
| LT-02 | | | | |
| LT-03 | | | | |

> Do not proceed to STEP 0B until STEP 0A is complete and every row carries all four
> fields.

---

### STEP 0B -- ORTHOGONAL FAILURE SURFACE TAXONOMY

| FS-ID | Failure Surface -- structural defect category; two rows naming the same category
are not orthogonal | Gate Domain -- schema section; "general" does not count |
Closed By (C-ID or Gate Label) -- blank is a fail |
|-------|------|------|------|
| FS-01 | | | |
| FS-02 | | | |
| FS-03 | | | |

> Do not proceed to STEP 1 until STEP 0B is complete.

---

**STEP 1 -- DOMAIN ROLE REGISTRY**

> **GATE A**: Do not open the Phase Index until Role Registry is complete, all roles
> carry domain-qualified titles, every role has an Exception Handler designation, and
> every role has an LT-ID Trace or SECONDARY:rationale.
> Blocked by: C-05, C-11, C-23, C-36

| R-ID | Role Name -- domain-qualified functional title; generic labels ("Approver",
"Admin") do not count | Domain -- process function |
Exception Handler (Y/N) -- Mandatory; at least one Y required; blank is a fail |
LT-ID Trace (LT-ID from STEP 0A; or
SECONDARY (use only when role exists outside all LT scopes, naming why this role
exists without any LT-bound trigger): [rationale];
generic "N/A" or blank is a fail) |
|------|------|------|------|------|
| R-01 | | | | |
| R-02 | | | | |
| R-03 | | | | |

---

**STEP 2 -- PHASE INDEX**

> **GATE B**: Do not open State Trace until Phase Index complete; every Entry Trigger
> carries LT-ID or DERIVED:rationale; every Status-Quo Gap names a specific FM-ID.
> Blocked by: C-16, C-36, C-47

| Ph-ID | Phase Name | Entry Trigger (LT-ID from STEP 0A; or
DERIVED (use only when this phase boundary results from multiple LT-IDs combining,
naming which LT-IDs and combination logic produced this boundary): [rationale];
generic "N/A" or blank is a fail) |
Status-Quo Gap (mutual-audit pair with Entry Trigger -- co-designed as a mutual-audit
pair; not a coincidence of column placement; write FM-ID from STATUS-QUO PROCESS
DECLARATION; a cell with no FM-ID is structurally unanchored and is a fail) |
Completion Condition | SLA Envelope | SLA Risk | States Contained |
|-------|------|------|------|------|------|------|------|
| PH-01 | | | | | | | |
| PH-02 | | | | | | | |
| PH-03 | | | | | | | |

Minimum 3 phases; each phase must contain >=2 states.

---

**STEPS 3 through 12** -- same structure as V-01.

---

**STEP 13 -- COVERAGE SCAN**

[Groups A, B, C identical to V-01. Defect Type Taxonomy D-01 through D-22 as in V-01.
Coverage Scan includes AC-31 and AC-32.]

> **PRODUCTION GATE**: Writing this artifact while any Coverage Scan row shows FAIL is a
> structural fail -- the artifact contains at least one of: an unterminated path (D-01),
> an uncertified exception handler (D-02), an unresolvable decision owner (D-03), a
> missing or partial SQ Declaration (D-09/D-10), an unanchored status-quo gap (D-11),
> a per-field anti-pattern gap (D-14), a trailing-position enforcement token (D-15),
> a missing FM-ID Protocol block (D-16), partial Protocol field coverage (D-17),
> selective leading-clause token distribution (D-18), a gate-defect-pointer-only gate
> sentence (D-19), an escape-code-eligibility-absent column header (D-20), a gate
> enumeration without D-ID cross-references (D-21), or an escape code with
> non-parenthetical eligibility binding (D-22) -- and that artifact must be discarded
> and rerun from the failing step before it is filed or used.
>
> Both conditions must be satisfied before the artifact is written:
> (1) Coverage Scan shows PASS for AC-01 through AC-32.
> (2) Check V shows CLOSED.

---

## V-03 -- Lifecycle Emphasis: Phase-First Framing + GATE SQ + D-ID/Parenthetical Stability

**Variation axis:** Lifecycle emphasis -- a LIFECYCLE PHASE FRAMING block precedes the
FM-ID PROTOCOL, establishing the lifecycle type, phase count, and cross-lifecycle
handoffs before the SQ Declaration is authored. Holds R19 V-03's phase-first framing
axis and GATE SQ labeled gate. C-57 HOLD: parenthetical D-IDs already present in gate
text from R19 V-03. C-58 HOLD: parenthetical escape code binding already present in
column headers. Single structural extension: D-21 and D-22 added to taxonomy; AC-31
and AC-32 added to scan Group B; gate text extended with D-21/D-22.

**Hypothesis:** Phase-first framing displaces the FM-ID Protocol from the document's
first structural position but does not interact with gate D-ID cross-referencing or
escape code binding format. Both C-57 and C-58 are structurally downstream of the phase
framing block: C-57 applies to the production gate (end of schema) and C-58 applies to
Step 1 and Step 2 column headers. Phase framing does not modify either location. Testing
whether the GATE SQ label (which appears at the FM-ID Protocol close) and the phase
framing block's pre-schema position are orthogonal to both new criteria. Prediction:
C-57 HOLD/PASS (AC-31 PASS, phase framing does not displace D-ID gate enumeration);
C-58 HOLD/PASS (AC-32 PASS, parenthetical binding stable); GATE SQ label is
compatible with both new criteria.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document
or process named in the signal. Work through every numbered step in order. Establish the
lifecycle's phase structure first, then read the FM-ID PROTOCOL before filling the
STATUS-QUO PROCESS DECLARATION. Every field cell in the SQ Declaration begins with a
compact enforcement token; read the token before reading the content instruction.

---

### LIFECYCLE PHASE FRAMING

Before authoring the SQ Declaration or trigger inventory, establish the lifecycle's phase
structure. This framing determines how FM-IDs are anchored to phases downstream.

```
Lifecycle type:    [L2O / P2P / Period Close / Case Lifecycle / other -- name specifically]
Phase count:       [expected number of phases -- minimum 3]
Phase boundaries:  [name the expected phase transition points]
Cross-lifecycle:   [name any handoff to a partner lifecycle; or "self-contained"]
```

Complete this framing block before proceeding to FM-ID PROTOCOL.

---

### FM-ID PROTOCOL

FM-IDs are mandatory structural identifiers. They are defined in the STATUS-QUO PROCESS
DECLARATION below and must appear in every Phase Index Status-Quo Gap cell downstream.

This protocol governs all four fields in the SQ Declaration:

- **Incumbent Process**: must name a specific named process, tool, or workaround. A
  single-word tool name without context does not count. The Incumbent Process should be
  consistent with the lifecycle type named in the Phase Framing above.
- **FM-01**: must name the specific detection or prevention mechanism the incumbent fails
  to provide. "Error-prone," "inefficient," or "slow" does not count. Assign identifier
  FM-01 inline. FM-01 should map to a gap visible within at least one phase named in the
  Phase Framing.
- **FM-02**: must name a second failure mode orthogonal to FM-01. A restatement,
  subcategory, or downstream consequence of FM-01 does not count. Assign identifier
  FM-02 inline.
- **Inertia Driver**: must name the specific organizational, systemic, or economic reason
  the incumbent persists despite FM-01 and FM-02. "Familiarity" without specificity does
  not count. The Inertia Driver explains why the lifecycle type named in Phase Framing
  continues to operate under the incumbent.

A Phase Index Status-Quo Gap cell with no FM-ID from this block is structurally
unanchored and is a fail.

> **GATE SQ**: Author the STATUS-QUO PROCESS DECLARATION completely before proceeding
> to STEP 0A. A SQ Declaration with any blank Content cell is incomplete and blocks
> GATE SQ. Blocked by: C-52, C-53, C-54.

---

### STATUS-QUO PROCESS DECLARATION

| SQ-Field | Content |
|----------|---------|
| does not count; Mandatory -- Incumbent Process: names the specific named process, tool, or workaround being replaced; "manual process" without naming the specific tool does not count; naming a department or team alone does not count | |
| does not count; Mandatory -- FM-01: first failure mode; names the specific detection or prevention mechanism the incumbent fails to provide; "error-prone," "inefficient," or "slow" does not count; assign identifier FM-01 inline | |
| does not count; Mandatory -- FM-02: second failure mode orthogonal to FM-01; a restatement, subcategory, or downstream consequence of FM-01 does not count; assign identifier FM-02 inline | |
| does not count; Mandatory -- Inertia Driver: names the specific organizational, systemic, or economic reason the incumbent persists despite FM-01 and FM-02; "familiarity" without specificity does not count; a reason that would apply equally to any other legacy process does not count | |

---

### STEP 0A -- LIFECYCLE TRIGGER INVENTORY

Author this table completely before proceeding to STEP 0B.

| LT-ID | Trigger Description -- names the external event, role action, or time condition
that initiates the lifecycle; "process begins" does not count; name the specific
initiating signal | Trigger Source (System Event / Role Action / Time Condition) |
Initial State | Initial Phase -- Mandatory; blank is a structural fail |
|-------|------|------|------|------|
| LT-01 | | | | |
| LT-02 | | | | |
| LT-03 | | | | |

> Do not proceed to STEP 0B until STEP 0A is complete and every row carries all four
> fields.

---

### STEP 0B -- ORTHOGONAL FAILURE SURFACE TAXONOMY

| FS-ID | Failure Surface -- structural defect category; two rows naming the same category
are not orthogonal | Gate Domain -- schema section; "general" does not count |
Closed By (C-ID or Gate Label) -- blank is a fail |
|-------|------|------|------|
| FS-01 | | | |
| FS-02 | | | |
| FS-03 | | | |

> Do not proceed to STEP 1 until STEP 0B is complete.

---

**STEP 1 -- DOMAIN ROLE REGISTRY**

> **GATE A**: Do not open the Phase Index until Role Registry is complete, all roles
> carry domain-qualified titles, every role has an Exception Handler designation, and
> every role has an LT-ID Trace or SECONDARY:rationale.
> Blocked by: C-05, C-11, C-23, C-36

| R-ID | Role Name -- domain-qualified title; generic labels do not count |
Domain -- process function |
Exception Handler (Y/N) -- Mandatory; at least one Y required |
LT-ID Trace (LT-ID from STEP 0A; or
SECONDARY (use only when role exists outside all LT scopes, naming why this role
exists without any LT-bound trigger): [rationale];
generic "N/A" or blank is a fail) |
|------|------|------|------|------|
| R-01 | | | | |
| R-02 | | | | |
| R-03 | | | | |

---

**STEP 2 -- PHASE INDEX**

> **GATE B**: Do not open State Trace until Phase Index complete; every Entry Trigger
> carries LT-ID or DERIVED:rationale; every Status-Quo Gap names an FM-ID.
> Blocked by: C-16, C-36, C-47

| Ph-ID | Phase Name | Entry Trigger (LT-ID from STEP 0A; or
DERIVED (use only when this phase boundary results from multiple LT-IDs combining,
naming which LT-IDs and combination logic produced this boundary): [rationale];
generic "N/A" or blank is a fail) |
Status-Quo Gap (mutual-audit pair with Entry Trigger -- co-designed as a mutual-audit
pair; not a coincidence of column placement; write FM-ID from STATUS-QUO PROCESS
DECLARATION; blank is a fail) |
Completion Condition | SLA Envelope | SLA Risk | States Contained |
|-------|------|------|------|------|------|------|------|
| PH-01 | | | | | | | |
| PH-02 | | | | | | | |
| PH-03 | | | | | | | |

---

**STEPS 3 through 12** -- same structure as V-01.

---

**STEP 13 -- COVERAGE SCAN**

[Groups A, B, C identical to V-01. AC-28 check references GATE SQ label.
Defect Type Taxonomy D-01 through D-22 as in V-01. AC-31 and AC-32 present.]

> **PRODUCTION GATE**: Writing this artifact while any Coverage Scan row shows FAIL is a
> structural fail -- the artifact contains at least one of: an unterminated path (D-01),
> an uncertified exception handler (D-02), an unresolvable decision owner (D-03), a
> missing or partial SQ Declaration (D-09/D-10), an unanchored status-quo gap (D-11),
> a per-field anti-pattern gap (D-14), a trailing-position enforcement token (D-15),
> a missing FM-ID Protocol block (D-16), partial Protocol field coverage (D-17),
> selective leading-clause token distribution (D-18), a gate-defect-pointer-only gate
> sentence (D-19), an escape-code-eligibility-absent column header (D-20), a gate
> enumeration without D-ID cross-references (D-21), or an escape code with
> non-parenthetical eligibility binding (D-22) -- and that artifact must be discarded
> and rerun from the failing step before it is filed or used.
>
> Both conditions must be satisfied before the artifact is written:
> (1) Coverage Scan shows PASS for AC-01 through AC-32.
> (2) Check V shows CLOSED.

---

## V-04 -- Phrasing Register: Conversational D-ID Gate + Parenthetical Escape Binding

**Variation axis:** Phrasing register (conversational) + role sequence -- two axes
combined. The FM-ID Protocol is relabeled FM-ID GUIDANCE and uses plain-language
framing throughout. The DOMAIN ROLE REGISTRY precedes all other content (role-first
axis). Two targeted changes from R19 V-04:
(1) Gate text updated to add parenthetical D-IDs to every inline defect category
(C-57 TARGET): e.g., "an unterminated path (D-01), an uncertified exception handler
(D-02)..." -- R19 V-04 enumerated plain prose names without D-IDs.
(2) Escape code column headers updated from dash-separator imperative form
("write SECONDARY -- but only when...") to code-token + immediately-adjacent
parenthetical form ("SECONDARY (use only when...)") (C-58 TARGET).

**Hypothesis:** Conversational register is compatible with both C-57 and C-58 because
both criteria are about typographic structure at specific locations -- not about
formal/imperative phrasing. C-57 requires parenthetical D-IDs adjacent to category
names in the gate sentence; a conversational gate can carry "(D-01)" parenthetically
without losing plain-language character. C-58 requires the code token to immediately
precede the opening parenthesis; conversational language can adopt this binding format
without reverting to formal notation. R19 V-04 demonstrated that conversational tone
does not prevent C-55 (inline enumeration) or C-56 (eligibility co-location); R20 V-04
tests whether the same register can satisfy the stronger forms. The test: does
conversational phrasing introduce a structural tension with D-ID parenthetical placement
or parenthetical binding format? Prediction: C-57 TARGET (PASS -- D-IDs attach
naturally to inline category names in conversational prose); C-58 TARGET (PASS --
code-before-paren format is register-neutral); AC-31 PASS; AC-32 PASS.

---

You are a business-process simulation expert. Your job is to walk through a complete
business lifecycle end to end. Start by listing the team members who own this process,
then read the FM-ID Guidance section before filling in the status-quo table. Follow
every numbered step in order.

---

### Start Here: Domain Role Registry

Fill in this table before you do anything else. Every role needs a specific job title --
not a generic label like "Approver" or "Finance team." The "Exception Handler?" column
tells you who is authorized to own exception flows later.

| R-ID | Job Title (specific domain title, e.g., "Senior Credit Analyst" or "AP Supervisor";
generic labels like "Approver" or "Admin" do not count) |
Process Area (specific function, e.g., "Sales Operations" or "Finance -- AP";
a department name without a process qualifier does not count) |
Exception Handler? (Y or N -- at least one Y is required; leave blank and the whole
artifact is invalid) |
Which Triggers Start This Role? (write the LT-ID(s) this role first appears in; if
this role has no lifecycle trigger write
SECONDARY (use only when role has no LT-bound trigger at all, naming why this role
exists outside any trigger scope): [rationale]; "N/A" is not acceptable) |
|------|------|------|------|------|
| R-01 | | | | |
| R-02 | | | | |
| R-03 | | | | |

You need at least 3 roles. Do not open the FM-ID Guidance until every row has a specific
job title and an Exception Handler answer.

---

### FM-ID Guidance

FM-IDs label the ways your current process fails. You will use these labels in the Phase
table downstream -- every phase needs to name which FM-ID its entry trigger is
addressing.

Read these four rules before filling in the status-quo table:

- **What is your current process?** Name the specific tool, procedure, or workaround --
  not just "a manual process" or "the finance team." If you can't name it specifically,
  you haven't scoped the problem yet.
- **FM-01 -- First failure:** What specific thing does the current process fail to detect
  or prevent? Saying it's "error-prone" or "slow" is not a failure mode -- name the
  specific mechanism that is absent.
- **FM-02 -- Second failure (orthogonal):** A completely different failure from FM-01.
  If fixing FM-01 would also fix FM-02, they're not orthogonal -- write a genuinely
  different failure.
- **Why does it persist?** What specific organizational, contractual, or systemic reason
  keeps the current process in place despite FM-01 and FM-02? "We're used to it" is not
  an answer -- name the specific lock-in mechanism.

Once you have all four answers, fill in the status-quo table, then move on to Step 0A.

---

### Status-Quo Process Declaration

| Field | Your Answer |
|-------|-------------|
| does not count; Mandatory -- Current Process: name the specific tool or procedure being replaced; "manual process" without naming the tool does not count; a team name alone does not count | |
| does not count; Mandatory -- FM-01: the specific mechanism the current process fails to provide; "error-prone" or "slow" does not count; assign label FM-01 inline | |
| does not count; Mandatory -- FM-02: a second failure orthogonal to FM-01; a restatement or downstream consequence of FM-01 does not count; assign label FM-02 inline | |
| does not count; Mandatory -- Why It Persists (Inertia Driver): the specific organizational or systemic reason the current process stays despite FM-01 and FM-02; "familiarity" without a specific mechanism does not count | |

---

### Step 0A -- What Starts This Lifecycle?

List every external trigger that can kick off this process. "The process starts" is not
a trigger -- name the specific event, action, or condition.

| LT-ID | What triggers this? (name the specific event, role action, or time condition) |
Source type (write exactly one: System Event / Role Action / Time Condition) |
First state this trigger activates |
First phase this trigger activates (required -- blank is a fail) |
|-------|------|------|------|------|
| LT-01 | | | | |
| LT-02 | | | | |
| LT-03 | | | | |

You need at least 3 rows. Do not move on until every row has all four fields.

---

### Step 0B -- Failure Surface Taxonomy

Before building the schema, name the structural ways this lifecycle document can go
wrong. These are schema defects, not process exceptions.

| FS-ID | What can go wrong structurally? (a schema defect category -- two rows naming the
same defect are not orthogonal) |
Which schema section does this affect? ("general" is too vague) |
What criterion or gate prevents this? (required -- blank is a fail) |
|-------|------|------|------|
| FS-01 | | | |
| FS-02 | | | |
| FS-03 | | | |

---

**Step 1 -- Role Registry Verification**

You set up roles at the start. Before opening the Phase Index, confirm they are
complete.

> **Gate A**: Do not open the Phase Index until: every role has a specific job title
> (no generics), every role has an Exception Handler Y/N, every role has a trigger trace
> or SECONDARY:rationale, and at least one role has Exception Handler = Y.
> Blocked by: C-05, C-11, C-23, C-36

---

**Step 2 -- Phase Index**

> **Gate B**: Do not open the State Trace until the Phase Index is complete, every Entry
> Trigger has a trigger ID or DERIVED:rationale, and every Status-Quo Gap names an FM-ID.
> Blocked by: C-16, C-36, C-47

| Ph-ID | Phase Name |
What triggers this phase? (write the LT-ID from Step 0A; or if this phase boundary
comes from combining multiple triggers, write
DERIVED (use only when the phase results from multiple LT-IDs combining, naming which
LT-IDs and how they combine): [rationale]; "N/A" is not valid) |
Which FM-ID does this phase address? (write FM-01 or FM-02 from the Status-Quo table;
this column and the trigger column are co-designed as a mutual-audit pair -- not a
coincidence of column placement -- a vague trigger produces a blank here, making the
gap visible in a single row scan; blank is a structural fail) |
What ends this phase? | How long should this take? | At-risk? |
States (fill after Step 3) |
|-------|------|------|------|------|------|------|------|
| PH-01 | | | | | | | |
| PH-02 | | | | | | | |
| PH-03 | | | | | | | |

---

**Steps 3 through 12** -- same structure as V-01 (conversational column labels
throughout; "Who handles it?" instead of "Handler (R-ID)"; "What if the decision
mechanism breaks?" instead of "Fallback"; etc.).

---

**Step 13 -- Coverage Check**

#### Group A -- Pre-Schema Blocks

| AC-ID | What to verify | Where to look | Result | Defect if fail |
|-------|----------------|--------------|--------|----------------|
| AC-01 | Step 0A has >=3 trigger rows; all four columns filled per row | Step 0A | | |
| AC-02 | Step 0B has >=3 orthogonal failure surfaces; all three columns filled | Step 0B | | |
| AC-03 | Role Registry appears before FM-ID Guidance; roles have job titles and Exception Handler Y/N before Status-Quo table is filled | Role Registry | | |
| AC-21 | Status-Quo table appears before Step 0A; all four fields present | Status-Quo table | | |
| AC-23 | Every Status-Quo field cell carries an inline anti-pattern token for that field | Status-Quo cells | | |
| AC-24 | FM-ID Guidance section appears before Status-Quo table; covers all four fields with "does not count" language | FM-ID Guidance | | |
| AC-25 | Every Status-Quo field cell begins with "does not count; Mandatory" as its first expression | Status-Quo cells | | |
| AC-26 | C-52: FM-ID Guidance covers Current Process and Inertia Driver with same governance depth as FM-01/FM-02 | FM-ID Guidance | | |
| AC-27 | C-53: Leading-clause "does not count; Mandatory" token appears first in all four Status-Quo field cells | Status-Quo cells | | |
| AC-28 | C-54: FM-ID Guidance closes with instruction to complete Status-Quo table before moving to Step 0A | FM-ID Guidance close | | |

#### Group B -- Gate-Backed Criteria

| AC-ID | What to verify | Where | Result | Defect if fail |
|-------|----------------|-------|--------|----------------|
| AC-04 | Role Registry: specific job titles, Exception Handler Y/N, trigger trace or SECONDARY:rationale | Step 1 | | |
| AC-05 | "Which Triggers Start This Role?" column header carries SECONDARY in parenthetical binding format: SECONDARY (use only when role has no LT-bound trigger, naming why this role exists outside any trigger scope): [rationale] -- dash-separator form is D-22 | Step 1 column header | | |
| AC-06 | Phase trigger column header carries DERIVED in parenthetical binding format: DERIVED (use only when phase results from multiple LT-IDs combining, naming which LT-IDs and how they combine): [rationale] -- dash-separator form is D-22 | Step 2 column header | | |
| AC-07 | All exception handlers trace to Exception Handler = Y | Step 5 | | |
| AC-08 | Handler column header co-locates backward-trace rule and fail-declaration | Step 5 header | | |
| AC-09 | Gate D uses "certified" or equivalent handler verification language | Gate D | | |
| AC-10 | Decision condition column carries both threshold-type category list and quoted example | Step 3 | | |
| AC-11 | Phase exit gates all carry "Blocked by: [C-ID]" | Step 4 | | |
| AC-12 | Gate C and Gate D both present with source and target named | Gates C + D | | |
| AC-13 | Check V present; Production Gate names Check V as co-equal condition | Step 6 + Gate | | |
| AC-22 | Phase Index Status-Quo Gap column header names the mutual-audit design principle | Step 2 | | |
| AC-29 | C-55: Production gate names >=3 defect categories inline in the gate sentence itself | Production Gate | | |
| AC-30 | C-56: Trigger-trace column (Step 1) and phase-trigger column (Step 2) each carry both code format and eligibility condition | Steps 1 + 2 headers | | |
| AC-31 | C-57: each named defect category in gate inline enumeration carries parenthetical D-ID; categories without D-IDs are D-21 | Production Gate | | |
| AC-32 | C-58: Step 1 and Step 2 escape code headers use code-token + immediately-adjacent parenthetical; dash-separator or instruction verb between code and qualifier is D-22 | Steps 1 + 2 headers | | |

#### Group C -- Schema Integrity

[Same checks as V-01 Group C: AC-14 through AC-20.]

**Defect Types:** [D-01 through D-22 as in V-01]

> **Production Gate**: Writing this artifact while any Coverage Check row shows FAIL
> means the artifact has at least one structural problem -- an unterminated path (D-01),
> an uncertified exception handler (D-02), an unresolvable decision owner (D-03), a
> missing or partial status-quo declaration (D-09/D-10), an unanchored status-quo gap
> (D-11), a per-field anti-pattern gap (D-14), a trailing-position enforcement token
> (D-15), a missing FM-ID guidance section (D-16), partial guidance coverage (D-17),
> selective leading-clause distribution (D-18), a gate that only points to the defect
> list without naming any defects inline (D-19), an escape code column that carries a
> format code but no eligibility condition (D-20), a gate enumeration that names defect
> categories without D-ID cross-references (D-21), or an escape code binding that uses
> a separator between the code token and its eligibility clause instead of immediate
> parenthetical adjacency (D-22) -- and the artifact must be discarded and rerun from
> the failing step before it is filed or used.
>
> Both conditions must be met:
> (1) Coverage Check shows PASS for AC-01 through AC-32.
> (2) Check V shows CLOSED.

---

## V-05 -- Full Combination: Inertia-First + Column Contract + Pre-Declaration Roles +
GATE SQ + C-57/C-58 Stability Confirmation

**Variation axis:** Inertia framing + output format + role sequence -- three axes
combined. Holds R19 V-05 full floor intact. C-57 HOLD: R19 V-05 production gate
already carries parenthetical D-IDs on every enumerated category (C-57 was satisfied
by the R19 V-05 structure before C-57 was formalized as a criterion). C-58 HOLD: R19
V-05 LT-ID Trace and Entry Trigger column headers already use code-token +
immediately-adjacent parenthetical binding. Single structural extension: D-21 and D-22
added to Defect Type Taxonomy; AC-31 and AC-32 added to Coverage Scan Group B; gate
text extended with D-21/D-22.

**Hypothesis:** The R19 V-05 full floor already satisfies C-57 and C-58 through
structural choices made for other criteria (the verbose production gate was written to
be maximally specific; the parenthetical binding format was adopted to satisfy C-56's
eligibility co-location requirement). Explicitly formalizing AC-31/AC-32 as Coverage
Scan rows and D-21/D-22 as defect taxonomy entries closes the gap between "the artifact
passes these criteria" and "the schema explicitly verifies them as independent named
criteria." V-05 serves as the full-stack stability confirmation across all 58 criteria:
if AC-31 and AC-32 both PASS when evaluated against the existing R19 V-05 structure,
the formalization is score-neutral for V-05 and both criteria are confirmed as
independently satisfiable from the full-floor baseline. Prediction: C-57 HOLD/PASS,
C-58 HOLD/PASS, AC-31 PASS (stable), AC-32 PASS (stable); no structural changes needed;
full aspirational 50/58 achievable from V-05 baseline.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document
or process named in the signal. Work through every numbered step in order. Establish the
DOMAIN ROLE REGISTRY first, then read the FM-ID PROTOCOL before filling the STATUS-QUO
PROCESS DECLARATION Column Contract. Every Column Contract field definition begins with
a compact enforcement token; read the token before reading the content instruction.

---

### DOMAIN ROLE REGISTRY (Pre-Declaration Pass)

Author this table completely before proceeding to FM-ID PROTOCOL.

| R-ID | Role Name -- domain-qualified functional title (e.g., "Senior Credit Analyst",
"AP Supervisor"); generic labels ("Approver", "Admin", "User", "Finance team") do not
count | Domain -- process function (e.g., Sales Operations, Finance -- AP); org-unit
name without process qualifier does not count |
Exception Handler (Y/N) -- Mandatory; Y = authorized to handle exception flows;
N = not authorized; at least one Y required; blank is a fail |
LT-ID Trace -- name the LT-ID(s) whose Initial State or Initial Phase this role appears
in; if role exists outside all LT scopes write
SECONDARY (use only when role has no LT-bound trigger, naming why this role exists
without any LT anchor): [rationale]; generic "N/A" or blank is a fail |
|------|------|------|------|------|
| R-01 | | | | |
| R-02 | | | | |
| R-03 | | | | |

Minimum 3 roles. Domain-qualified titles are mandatory -- the Incumbent Process and
Inertia Driver fields you will fill next should reference the same domain context
anchored here.

> Do not proceed to FM-ID PROTOCOL until every R-ID carries a domain-qualified title
> and an Exception Handler designation (Y/N). Generic placeholder titles block this
> gate.

---

### FM-ID PROTOCOL

FM-IDs are mandatory structural identifiers. They are defined in the STATUS-QUO PROCESS
DECLARATION Column Contract below and must appear in every Phase Index Status-Quo Gap
cell downstream.

This protocol governs all four fields in the SQ Declaration, organized by field type:

**CONTEXTUAL FIELDS** -- establish the organizational setting:

- **Inertia Driver**: does not count if the entry would apply to any legacy process;
  must name the specific organizational, systemic, or economic reason this particular
  incumbent persists despite its failure modes. "Familiarity" or "switching costs"
  alone does not count without naming the specific mechanism (e.g., a named integration
  dependency, a contractual lock-in, a compliance regime that approved the incumbent).
  Assign the Inertia Driver before FM-01 and FM-02 -- the failure modes are symptoms
  of an incumbent that persists for this specific reason.

- **Incumbent Process**: does not count if it names only a department or a generic
  method; must name the specific tool, procedure, or workaround being replaced,
  including enough operational context to understand how it is used. A single-word tool
  name without context does not count. The Incumbent Process should be consistent with
  the Inertia Driver.

**FAILURE MODE FIELDS** -- name what the incumbent fails to provide:

- **FM-01**: does not count if it describes a quality attribute ("error-prone," "slow,"
  "inefficient"); must name the specific detection or prevention mechanism the incumbent
  fails to provide. Assign identifier FM-01 inline.

- **FM-02**: does not count if it is a restatement, subcategory, or downstream
  consequence of FM-01; must name a second orthogonal failure mode. Assign identifier
  FM-02 inline.

A Phase Index Status-Quo Gap cell with no FM-ID from this block is structurally
unanchored and is a fail. The equal governance depth for Contextual Fields and Failure
Mode Fields is intentional -- Incumbent Process and Inertia Driver cells failing their
"does not count" threshold produce the same downstream gap as a failing FM-01 or FM-02
cell.

> **GATE SQ**: Author the STATUS-QUO PROCESS DECLARATION Column Contract completely
> before proceeding to STEP 0A. Every Content cell in the Fill Table must be non-blank.
> A Column Contract with any blank Content cell is incomplete and blocks GATE SQ.
> Blocked by: C-52, C-53, C-54.

---

### STATUS-QUO PROCESS DECLARATION -- Column Contract

Read this table completely before filling the Content column below.

| Field | Fill Requirement | Does Not Count |
|-------|-----------------|----------------|
| does not count; Mandatory -- Inertia Driver | names the specific organizational, systemic, or economic reason this incumbent persists; include the specific lock-in mechanism | "familiarity"; "switching costs" without naming the mechanism; any reason equally applicable to all legacy processes |
| does not count; Mandatory -- Incumbent Process | names the specific tool, procedure, or workaround being replaced; include operational context; consistent with Inertia Driver | department or team name alone; "manual process" without tool name; single-word tool name without context |
| does not count; Mandatory -- FM-01 | names the specific detection or prevention mechanism the incumbent fails to provide; assign identifier FM-01 inline | "error-prone," "inefficient," "slow"; generic quality attribute |
| does not count; Mandatory -- FM-02 | names a second failure mode orthogonal to FM-01; assign identifier FM-02 inline | restatement of FM-01; subcategory; downstream consequence |

### STATUS-QUO PROCESS DECLARATION -- Fill Table

| SQ-Field | Content |
|----------|---------|
| Inertia Driver | |
| Incumbent Process | |
| FM-01 | |
| FM-02 | |

---

### STEP 0A -- LIFECYCLE TRIGGER INVENTORY

Author this table completely before proceeding to STEP 0B.

| LT-ID | Trigger Description -- names the external event, role action, or time condition
that initiates the lifecycle; "process begins" does not count |
Trigger Source (System Event / Role Action / Time Condition) |
Initial State | Initial Phase -- Mandatory; blank is a structural fail |
|-------|------|------|------|------|
| LT-01 | | | | |
| LT-02 | | | | |
| LT-03 | | | | |

> Do not proceed to STEP 0B until STEP 0A is complete.

---

### STEP 0B -- ORTHOGONAL FAILURE SURFACE TAXONOMY

| FS-ID | Failure Surface -- structural defect category; two rows naming the same category
are not orthogonal | Gate Domain -- schema section; "general" does not count |
Closed By (C-ID or Gate Label) -- blank is a fail |
|-------|------|------|------|
| FS-01 | | | |
| FS-02 | | | |
| FS-03 | | | |

> Do not proceed to STEP 1 until STEP 0B is complete.

---

**STEP 1 -- DOMAIN ROLE REGISTRY**

> **GATE A**: Do not open the Phase Index until Role Registry is complete, all roles
> carry domain-qualified titles, every role has an Exception Handler designation, and
> every role has an LT-ID Trace or SECONDARY:rationale.
> Blocked by: C-05, C-11, C-23, C-36

| R-ID | Role Name -- domain-qualified functional title; generic labels do not count |
Domain -- process function |
Exception Handler (Y/N) -- Mandatory; at least one Y required; blank is a fail |
LT-ID Trace (LT-ID from STEP 0A; or
SECONDARY (use only when role exists outside all LT scopes, naming why this role
exists without any LT anchor): [rationale];
generic "N/A" or blank is a fail) |
|------|------|------|------|------|
| R-01 | | | | |
| R-02 | | | | |
| R-03 | | | | |

---

**STEP 2 -- PHASE INDEX**

> **GATE B**: Do not open State Trace until Phase Index complete; every Entry Trigger
> carries LT-ID or DERIVED:rationale; every Status-Quo Gap cell names a specific FM-ID.
> Blocked by: C-16, C-36, C-47

| Ph-ID | Phase Name | Entry Trigger (LT-ID from STEP 0A; or
DERIVED (use only when this phase boundary results from multiple LT-IDs combining,
naming which LT-IDs and combination logic produced this boundary): [rationale];
generic "N/A" or blank is a fail) |
Status-Quo Gap (mutual-audit pair with Entry Trigger -- co-designed as a mutual-audit
pair; design intent of their adjacency is mutual verification; write FM-ID from
STATUS-QUO PROCESS DECLARATION; a cell with no FM-ID is structurally unanchored
and is a fail) |
Completion Condition | SLA Envelope | SLA Risk | States Contained |
|-------|------|------|------|------|------|------|------|
| PH-01 | | | | | | | |
| PH-02 | | | | | | | |
| PH-03 | | | | | | | |

Minimum 3 phases; each phase must contain >=2 states.

---

**STEPS 3 through 12** -- same structure as V-01.

---

**STEP 13 -- COVERAGE SCAN**

#### Group A -- Pre-Schema Structural Blocks

| AC-ID | Check | Evidence Location | Status | Defect Type if FAIL |
|-------|-------|-----------------|--------|---------------------|
| AC-01 | STEP 0A >=3 LT-IDs; all four fields per row | STEP 0A | | |
| AC-02 | STEP 0B >=3 orthogonal failure surfaces | STEP 0B | | |
| AC-21 | SQ Declaration Column Contract present before STEP 0A; Inertia Driver appears before Incumbent Process in Column Contract; Role Registry precedes all content | SQ Column Contract | | |
| AC-23 | Every Column Contract Field cell carries inline anti-pattern token specific to that field | SQ Column Contract Field column | | |
| AC-24 | FM-ID PROTOCOL present before SQ Column Contract; Contextual Fields and Failure Mode Fields organized as named groups with equal governance depth | FM-ID PROTOCOL | | |
| AC-25 | Every SQ Declaration Column Contract Field cell begins with "does not count; Mandatory" as first expression | SQ Column Contract Field cells | | |
| AC-26 | C-52: FM-ID PROTOCOL covers Inertia Driver and Incumbent Process with governance depth equal to FM-01 and FM-02 (Contextual Fields group named explicitly) | FM-ID PROTOCOL | | |
| AC-27 | C-53: Leading-clause token present as first expression in all four Column Contract Field cells | SQ Column Contract Field column | | |
| AC-28 | C-54: GATE SQ present at FM-ID PROTOCOL close; names SQ Declaration and STEP 0A; "Blocked by" field present | GATE SQ text | | |

#### Group B -- Gate-Backed Aspirational Criteria

| AC-ID | Check | Evidence Location | Status | Defect Type if FAIL |
|-------|-------|-----------------|--------|---------------------|
| AC-04 | Role Registry domain-qualified titles, Exception Handler Y/N, LT-ID Trace or SECONDARY:rationale | Step 1 | | |
| AC-05 | LT-ID Trace column header defines SECONDARY in parenthetical binding: SECONDARY (use only when role exists outside all LT scopes, naming why): [rationale]; dash-separator or instruction verb between code and qualifier is D-22 | Step 1 column header | | |
| AC-06 | Entry Trigger column header defines DERIVED in parenthetical binding: DERIVED (use only when phase boundary results from multiple LT-IDs combining, naming which LT-IDs and combination logic): [rationale]; dash-separator form is D-22 | Step 2 column header | | |
| AC-07 | All exception Handler R-IDs trace to Exception Handler = Y | Step 5 | | |
| AC-08 | Handler column header co-locates backward-trace rule and fail-declaration | Step 5 header | | |
| AC-09 | Gate D uses "certified Handler R-ID" language | Gate D text | | |
| AC-10 | Decision Condition header: category list AND quoted example | Step 3 D-table header | | |
| AC-11 | Phase exit gates: "Blocked by: [C-ID]" present | Step 4 gates | | |
| AC-12 | Gate C and Gate D both present, source and target named | Gate C + D | | |
| AC-13 | Check V present; Production Gate names Check V as co-equal condition | Step 6 + Gate | | |
| AC-22 | Phase Index Status-Quo Gap column header names the mutual-audit design principle and design intent of adjacency | Step 2 header | | |
| AC-29 | C-55: production gate enumerates >=3 named defect categories inline; column pointer alone is D-19 | Production Gate text | | |
| AC-30 | C-56: LT-ID Trace AND Entry Trigger headers each carry typed code format AND qualifying eligibility condition; format-only is D-20 | Step 1 + Step 2 headers | | |
| AC-31 | C-57: each named defect category in gate inline enumeration carries parenthetical D-ID cross-reference; categories without D-IDs are D-21 | Production Gate text | | |
| AC-32 | C-58: LT-ID Trace AND Entry Trigger column headers use code-token + immediately-adjacent parenthetical; dash-separator or instruction verb between code and qualifier is D-22 | Step 1 + Step 2 headers | | |

#### Group C -- General Schema Integrity

| AC-ID | Check | Evidence | Status | Defect Type if FAIL |
|-------|-------|---------|--------|---------------------|
| AC-14 | >=6 named states; each carries entry condition, exit transitions, and owner R-ID | Step 3 state table | | |
| AC-15 | >=3 exception flows; each carries trigger, certified Handler R-ID, divergence, recovery or terminal | Step 5 table | | |
| AC-16 | >=1 success terminal + >=1 failure/cancel terminal; all traced paths reach a named T-ID | Step 6 + Check V | | |
| AC-17 | >=2 bottlenecks (cause + downstream impact) + >=1 gap (missing step + risk if absent) | Steps 9 + 10 | | |
| AC-18 | >=3 decision points; each carries measurable threshold condition, owner, all branches, and fallback | Step 3 D-table | | |
| AC-19 | >=3 states with timing; >=1 phase annotated AT-RISK with causal bottleneck | Steps 3 + 2 | | |
| AC-20 | >=1 cross-lifecycle handoff with partner lifecycle, direction, fields passed, coupling state | Step 11 | | |

**Defect Type Taxonomy:**

| Defect-ID | Defect Type | Detected By |
|-----------|-------------|-------------|
| D-01 | Unterminated path: at least one traced path has no named T-ID | C-03, C-14, AC-16, Check V |
| D-02 | Uncertified exception handler: Handler R-ID does not trace to Exception Handler = Y | C-21, C-23, AC-07 |
| D-03 | Unresolvable decision owner: D-table Owner R-ID not in Step 1 | C-05, C-07, AC-18 |
| D-04 | Taxonomy-only decision condition: category enumeration present; no quoted example with operator and unit | C-31, AC-10 |
| D-05 | Example-only decision condition: quoted example present; no category enumeration | C-31, AC-10 |
| D-06 | Generic escape code: LT-ID Trace or Entry Trigger uses "N/A" or blank instead of typed SECONDARY/DERIVED code | C-44, AC-04, AC-05, AC-06 |
| D-07 | Missing Initial Phase field: LT record has Initial State column but no Initial Phase column | C-43, AC-01 |
| D-08 | Unlabeled pre-schema blocks: STEP 0A / STEP 0B section headers absent or merged | C-42, AC-02 |
| D-09 | Missing SQ Declaration: no STATUS-QUO PROCESS DECLARATION block present before STEP 0A | C-46, AC-21 |
| D-10 | FM-ID-free failure mode: SQ Declaration present but a failure mode entry carries no FM-ID identifier | C-46, AC-21 |
| D-11 | Unanchored status-quo gap: Phase Index Status-Quo Gap cell contains prose without FM-ID, or cell is blank | C-47, AC-22 |
| D-14 | Per-field anti-pattern gap: SQ Declaration field row carries no inline anti-pattern token | C-48, AC-23 |
| D-15 | Trailing-position enforcement token: SQ Declaration field carries an inline token but token is at end of cell | C-51, AC-25 |
| D-16 | Missing section-entry FM-ID Protocol block: no pre-table named section establishing FM-ID enforcement | C-50, AC-24 |
| D-17 | Partial Protocol block field coverage: Protocol block covers only FM fields; Incumbent Process or Inertia Driver absent | C-52, AC-26 |
| D-18 | Selective leading-clause token distribution: leading tokens on FM fields only; contextual field cells carry trailing tokens | C-53, AC-27 |
| D-19 | Gate-defect-pointer-only: production gate identifies violation by column pointer only without enumerating >=3 named categories inline | C-55, AC-29 |
| D-20 | Escape-code-eligibility-absent: escape code column header carries typed code format without qualifying eligibility condition | C-56, AC-30 |
| D-21 | Gate-defect-D-ID-absent: production gate enumerates defect category names inline but carries no parenthetical D-ID cross-reference on any enumerated category | C-57, AC-31 |
| D-22 | Escape-code-non-parenthetical-binding: escape code column header carries eligibility condition but binds it via instruction verb or dash separator rather than immediately-adjacent parenthetical | C-58, AC-32 |

> **PRODUCTION GATE**: Writing this artifact while any Coverage Scan row shows FAIL is a
> structural fail -- the artifact contains at least one of: an unterminated path (D-01),
> an uncertified exception handler (D-02), an unresolvable decision owner (D-03), a
> missing or partial SQ Declaration (D-09/D-10), an unanchored status-quo gap (D-11),
> a per-field anti-pattern gap (D-14), a trailing-position enforcement token (D-15),
> a missing FM-ID Protocol block (D-16), partial Protocol field coverage (D-17),
> selective leading-clause token distribution (D-18), a gate-defect-pointer-only gate
> sentence (D-19), an escape-code-eligibility-absent column header (D-20), a gate
> enumeration without D-ID cross-references (D-21), or an escape code with
> non-parenthetical eligibility binding (D-22) -- and that artifact must be discarded
> and rerun from the failing step before it is filed or used.
>
> Both conditions must be satisfied before the artifact is written:
> (1) Coverage Scan shows PASS for AC-01 through AC-32.
> (2) Check V shows CLOSED.
```

---

**Where to save:** `simulations/quest/golden/flow-lifecycle-variate-R20-2026-03-16.md`

**Summary of what changed per variation:**

| | C-57 | C-58 | Key structural change |
|---|---|---|---|
| V-01 | HOLD | HOLD | D-21/D-22 added to taxonomy + gate; AC-31/32 added to scan |
| V-02 | HOLD | HOLD | Same + Column Contract format held |
| V-03 | HOLD | HOLD | Same + Phase Framing block + GATE SQ held |
| V-04 | **TARGET** | **TARGET** | Gate text: D-IDs added to all inline categories; escape code headers: dash-separator → parenthetical binding |
| V-05 | HOLD | HOLD | Same as V-01 + inertia-first Column Contract + pre-declaration roles + GATE SQ |
