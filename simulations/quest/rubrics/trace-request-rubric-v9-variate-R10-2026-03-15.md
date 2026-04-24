# trace-request rubric v9 -- Skill Body Prompt Variations R10
# Generated: 2026-03-15

## Overview

Five complete, runnable skill body prompt variations for the `trace-request` skill,
targeting the v9 rubric (190 pts, C-01 through C-27).

**R9 result**: V-01/V-02 regression tests confirmed C-24 and C-25 load-bearing (-5 each
as predicted). V-03 (scope-gap Rem# propagation) produced ES-1, promoted to C-26. V-04
(vocabulary conformance gate) produced ES-2, promoted to C-27. V-05 (combined) produced
both, plus ES-3 (three-way VT# scope string coherence) as a not-yet-promoted C-28
candidate. Top score: 180/180 (V-03, V-04, V-05 on v8 rubric).

**R10 baseline**: R9 V-05 body (VT# assigned at Step 0 + Step 3a conformance gate with
D=0 + scope-gap Rem# three-way propagation + all prior criteria C-01 through C-25).

**R10 variation surface**: Two regression tests confirm C-26 and C-27 are load-bearing
(V-01, V-02). Three new-axis explorations target the ES-3 / C-28 design surface: VT#
scope string three-way coherence as spine of Step 8b (V-03), dedicated Step 8c coherence
audit table (V-04), and combined (V-05).

---

## Variation Summary Table

| V | Axis | Key change from R9 V-05 baseline | C-26 | C-27 | New signal | Predicted |
|---|------|----------------------------------|------|------|------------|-----------|
| V-01 | Phrasing register: C-26 advisory | Scope-gap Rem# cross-link softened; REQUIRED label removed from Step 8b and Step 11 scope-gap entries; NOTE replaces mandate | FAIL | PASS | none | 185/190 |
| V-02 | Phrasing register: C-27 advisory | Step 3a vocabulary conformance gate softened to advisory; D=0 gate summary and correction cycle not required | PASS | FAIL | none | 185/190 |
| V-03 | Lifecycle emphasis: VT# scope string coherence | Step 8b adds explicit REQUIRED three-way coherence check: exact VT# scope string must match across Step 3 Auth Check / Step 8a Invoked / Step 11 Parameters for each Gap?=Y boundary; coherence confirmation required before Step 9 | PASS | PASS | C-28 candidate: VT# scope string three-way coherence computable as binary | 190/190 |
| V-04 | Output format: dedicated coherence audit table | New Step 8c between Step 8b and Step 9: Scope String Coherence Table (Seq# / Step3-Auth-Check / Step8a-Invoked / Step11-Params / Match?) for every Gap?=Y boundary; Match? = Y required for each row | PASS | PASS | C-28 candidate: coherence computable from Match? column cell count | 190/190 |
| V-05 | Two-axis combination: V-03 + V-04 | Explicit coherence requirement in Step 8b PLUS dedicated Step 8c coherence table, both required | PASS | PASS | C-28 candidate: strongest structural expression of three-way coherence | 190/190 |

---

## V-01 -- Phrasing register: C-26 advisory

### Axis
Step 8b scope-gap Rem# requirement softened from mandatory (REQUIRED with DISQUALIFIER)
to advisory NOTE. Step 11 SCOPE-GAP ENTRIES requirement softened to advisory. All R9 V-05
requirements preserved identically for C-01 through C-25 and C-27 (conformance gate
remains REQUIRED).

### Hypothesis
Removing the REQUIRED label and DISQUALIFIER from the scope-gap -> Rem# three-way
cross-link causes C-26 FAIL while all other criteria including C-27 hold. A response
will complete Step 8a with Gap? = Y rows and Step 11 with remediation items but will not
wire each gap to a Rem# with the exact scope string. Predicted: 185/190 (-5 C-26).

---

### Complete Prompt Body

You are a platform expert (Dataverse / Commerce / Automate -- select the role that matches
the Topic and Signal context). Before beginning, declare your role and commit to the
vocabulary set for this platform in Step 0.

## Step 0 -- Role Declaration and Vocabulary Commitment

Declare: which platform role you are adopting, and commit to the platform-specific
vocabulary that will govern all subsequent steps. List at minimum:
- Auth mechanism name (e.g., "Azure AD delegated token with scope X" not "valid token")
- Primary service boundary names as the platform names them
- Failure mode vocabulary (e.g., "429 TooManyRequests with Retry-After" not "throttled")
- Permission model terms (e.g., "prvReadContact" not "read permission")

This vocabulary commitment is forward-binding: all Steps 1-11 must use these terms.

Assign a VT# (vocabulary term number) to each committed term:
- VT-1: [auth mechanism name with exact scope string]
- VT-2: [primary boundary name as platform names it]
- VT-3: [failure mode vocabulary with specific HTTP code]
- VT-4: [permission model term with specific privilege name]

---

ANTI-PATTERN: Declaring a role without committing vocabulary. The VT# assignment makes
the Step 3a vocabulary conformance gate computable.

---

## Step 1 -- Entry Point Declaration

State the precise entry point: API verb, endpoint path, caller identity, credential type
(from Step 0 VT terms), and ambient context (tenant, environment, region).

DISQUALIFIER: Missing credential type and endpoint path fails C-01.

---

ANTI-PATTERN: "A POST with a JSON body from an authenticated user" hides credential
scope, endpoint version, ambient context.

---

## Step 2 -- Boundary Inventory (GATE)

List every service boundary in traversal order. Use VT# boundary names. Include: API
gateway, authentication service, routing layer, each platform service, each storage
system, async queues, cache layers, response assembly path.

GATE: Step 3 must contain a row for every boundary listed here.

DISQUALIFIER: Omitting token validation, plugin pipelines, async queues, or cache layers
fails C-02.

---

ANTI-PATTERN: Listing only the primary service and the database.

---

## Step 3 -- Traversal Table

| Seq# | Boundary | Operation | Failure Point | Auth Check | p50 (ms) | p99 (ms) |

For Auth Check and Failure Point cells, use only terms committed in Step 0 VT# list.
Do not introduce generic substitutes.

- **Failure Point**: specific mechanism using Step 0 failure vocabulary (not "may fail")
- **Auth Check**: specific scope string from Step 0 VT# list, or [AUTH GAP]
- **p50/p99**: ms; sub-5ms = "< 5ms -- [reason]"

DISQUALIFIER: "may fail" or blank Failure Point fails C-03. "Valid token" without scope
string fails C-04. "fast" or blank latency fails C-05.

---

ANTI-PATTERN: "may timeout" without threshold and error code.
ANTI-PATTERN: "valid token" -- the exact VT# scope string must appear in every Auth
Check cell, not a generic substitute.

---

## Step 3a -- Vocabulary Conformance Gate (REQUIRED BEFORE STEP 4)

Produce a vocabulary conformance table:

| VT# | Term Committed in Step 0 | Step 3 Cells Where Term Appears | Generic Substitute Found? |

Rules:
- **Step 3 Cells Where Term Appears**: list Seq# and column for each verbatim occurrence
- **Generic Substitute Found?**: Y if any Step 3 cell in this term's category uses a
  generic form; N otherwise

Conformance gate summary: "V terms committed, V terms confirmed in Step 3, D deviations
found." D must be an exact integer. If D > 0, return to Step 3 and replace generic terms
before continuing. D = 0 is required to proceed.

DISQUALIFIER: Gate absent or missing integer summary fails C-27. D > 0 without correcting
Step 3 fails C-27.

---

ANTI-PATTERN: Declaring vocabulary at Step 0 and allowing generic substitutes in Step 3.
D > 0 means return and fix -- not proceed and note.

---

## Step 4 -- Critical Path (SUM CLOSURE GATE)

Name the Seq# chain. Distinguish parallel/cached paths. Compute p50/p99 from per-boundary
values. Reconcile if sum differs from total by more than 10%.

DISQUALIFIER: No Seq# chain fails C-10. Non-derivable total fails C-12.

## Step 5 -- Threat Class Catalog

| Row# | Threat Class | Boundary Seq# (all applicable) | Adv? |

- Minimum 5 rows; minimum 4 distinct threat classes
- List ALL Seq# per threat class
- Exactly one row Adv? = Y

DISQUALIFIER: <4 threat classes fails C-13. Single Seq# for multi-boundary threat
fails C-15. Zero or multiple Y values fails C-19.

---

ANTI-PATTERN: One Seq# per threat row. Real threats manifest at multiple boundaries.

---

## Step 6 -- Exhaustiveness Gate (REQUIRED BEFORE STEP 7)

Per-row checklist (Row#, Threat, Seq# checked, additions, Adv? Y/N) for every Step 5
row. Gate summary: "N rows reviewed against Step 2 inventory, X Seq# additions made."
N and X must be exact integers.

DISQUALIFIER: Missing integer counts fails C-20. Missing Adv? per row fails C-21.
Bare "confirmed" fails C-18.

## Step 7 -- Adversarial Path Comparison

Mandatory cross-reference block:

| Field | Value |
|-------|-------|
| Catalog row# | [from Step 5] |
| Threat class | [exact name] |
| All catalog Seq# for this row | [from Step 5] |
| Selected divergence Seq# | [divergence point] |

Adversarial trace naming divergence Seq#, adversarial condition, post-divergence path,
concrete outcome.

REQUIRED: Inline at the divergence boundary: "-> Rem#[X] applies." Not in trailing
summary.

DISQUALIFIER: No cross-reference block fails C-16. No inline Rem# at divergence boundary
fails C-23.

---

ANTI-PATTERN: Ad-hoc adversarial scenario not grounded in the threat catalog.

---

## Step 8 -- Authorization Re-Walk Audit

### Step 8a -- Scope Enumeration Table (REQUIRED BEFORE RE-WALK FINDINGS)

| Seq# | Boundary | Scope/Role Invoked | Required Scope/Role | Verified? | Gap? |

Rules:
- **Scope/Role Invoked**: exact scope string from Step 0 VT# list
- **Required Scope/Role**: the minimum the platform requires; name it
- **Verified?**: Y if check occurs at runtime; N if assumed from upstream validation
- **Gap?**: Y if Invoked does not cover Required, or Verified? = N at a dependent
  boundary; N otherwise

Every boundary must have a named Required Scope/Role. Blank = disallowed shortcut.

DISQUALIFIER: Scope enumeration table absent fails C-25. Blank Required Scope/Role
without explanation fails C-25.

### Step 8b -- Re-Walk Findings

Based on the Step 8a table:
- Name at least one new gap not in Step 3 Auth Check, OR
- Certify the three highest-risk boundaries are clean.

NOTE: Where Gap? = Y rows exist in Step 8a, consider citing the applicable Rem# from
Step 11 that addresses each gap. Including the exact scope string in the Rem# Parameters
field provides traceability between the scope gap and its remediation.

DISQUALIFIER: Re-walk findings that merely restate Step 3 Auth Check fails C-11.

---

ANTI-PATTERN: A copy of the Step 3 Auth Check column is not an audit. The scope
enumeration table makes gaps structurally visible; the re-walk findings interpret them.

---

## Step 9 -- Error Path Trace

Trace one full error path: origination Seq#, propagation at each boundary,
swallowed/wrapped/passed through, final caller-visible form.

REQUIRED: Inline at the origination boundary: "-> Rem#[X] applies." Not in trailing
summary.

DISQUALIFIER: "Error returned to caller" without propagation chain fails C-06. No
inline Rem# at origination boundary fails C-23.

## Step 10 -- Batch and Edge-Case Handling with Cross-Check Table

### Step 10a -- Edge-Case Table

| EC# | Edge Case | Boundary Seq# | Limit | Behavioral Consequence |

### Step 10b -- Batch-Catalog Cross-Check Table (REQUIRED)

| EC# | TRow-1 | TRow-2 | TRow-3 | TRow-4 | TRow-5 | ... |

Mark "X" where interaction exists. Every Row# from Step 5 = column. Every EC# = row.

### Step 10c -- Cross-Check Gate Summary (REQUIRED BEFORE STEP 11)

N = EC# row count. M = TRow# column count. K = "X" cell count.
State: "N edge cases x M catalog rows -> K interactions found."

DISQUALIFIER: Gate absent or missing any integer fails C-22. Integers not derivable
from table cells fails C-24.

---

ANTI-PATTERN: Prose cross-check without a backing table.

---

## Step 11 -- Remediation Register

| Rem# | Failure Ref (Seq#) | Mechanism Type | Parameters |

Every failure point from Step 3 must have a Rem# entry. Parameters quantified:
- Retry: algorithm, initial delay, multiplier, max-attempts
- Circuit breaker: threshold, reset interval
- Permission fix: exact scope string or role identity (must be a VT# term from Step 0)
- Payload guard: specific field name and validation predicate

NOTE: Where scope gaps were identified in Step 8a (Gap? = Y), consider dedicating a
Rem# entry to each gap, with the exact scope string or role name as the Parameters value.
This supports traceability from Step 8a to Step 11.

DISQUALIFIER: Mechanism type without parameters fails C-14. Inline remediation fails
C-17. "Add error handling" without mechanism type fails C-08.

---

ANTI-PATTERN: Inline annotations in Step 3 hide parameter omissions.

---

---

## V-02 -- Phrasing register: C-27 advisory

### Axis
Step 3a vocabulary conformance gate softened from mandatory (REQUIRED BEFORE STEP 4) to
advisory. No D=0 gate summary required. No correction cycle instruction. All R9 V-05
requirements preserved for C-01 through C-26: scope-gap Rem# cross-link is REQUIRED,
Step 8b SCOPE-GAP REM# REQUIREMENT and Step 11 SCOPE-GAP ENTRIES both mandatory.

### Hypothesis
Removing the mandatory D=0 gate and correction cycle from the conformance gate causes
C-27 FAIL while all other criteria including C-26 hold. A response will declare VT#
terms in Step 0 but may skip the per-term conformance table or produce a gate summary
without a D integer. Predicted: 185/190 (-5 C-27).

---

### Complete Prompt Body

You are a platform expert (Dataverse / Commerce / Automate -- select the role that matches
the Topic and Signal context). Before beginning, declare your role and commit to the
vocabulary set for this platform in Step 0.

## Step 0 -- Role Declaration and Vocabulary Commitment

Declare: which platform role you are adopting, and commit to the platform-specific
vocabulary that will govern all subsequent steps. List at minimum:
- Auth mechanism name (e.g., "Azure AD delegated token with scope X" not "valid token")
- Primary service boundary names as the platform names them
- Failure mode vocabulary (e.g., "429 TooManyRequests with Retry-After" not "throttled")
- Permission model terms (e.g., "prvReadContact" not "read permission")

This vocabulary commitment is forward-binding: all Steps 1-11 must use these terms.

Assign a VT# (vocabulary term number) to each committed term:
- VT-1: [auth mechanism name with exact scope string]
- VT-2: [primary boundary name as platform names it]
- VT-3: [failure mode vocabulary with specific HTTP code]
- VT-4: [permission model term with specific privilege name]

---

ANTI-PATTERN: Declaring a role without committing vocabulary. The vocabulary commitment
is the binding contract that makes C-03, C-04, and C-14 specific.

---

## Step 1 -- Entry Point Declaration

State the precise entry point: API verb, endpoint path, caller identity, credential type
(from Step 0 VT terms), and ambient context (tenant, environment, region).

DISQUALIFIER: Missing credential type and endpoint path fails C-01.

---

ANTI-PATTERN: "A POST with a JSON body from an authenticated user" hides credential
scope, endpoint version, ambient context.

---

## Step 2 -- Boundary Inventory (GATE)

List every service boundary in traversal order. Use VT# boundary names. Include: API
gateway, authentication service, routing layer, each platform service, each storage
system, async queues, cache layers, response assembly path.

GATE: Step 3 must contain a row for every boundary listed here.

DISQUALIFIER: Omitting token validation, plugin pipelines, async queues, or cache layers
fails C-02.

---

ANTI-PATTERN: Listing only the primary service and the database.

---

## Step 3 -- Traversal Table

| Seq# | Boundary | Operation | Failure Point | Auth Check | p50 (ms) | p99 (ms) |

For Auth Check and Failure Point cells, use only terms committed in Step 0 VT# list.

- **Failure Point**: specific mechanism using Step 0 failure vocabulary (not "may fail")
- **Auth Check**: specific scope string from Step 0 VT# list, or [AUTH GAP]
- **p50/p99**: ms; sub-5ms = "< 5ms -- [reason]"

DISQUALIFIER: "may fail" or blank Failure Point fails C-03. "Valid token" without scope
string fails C-04. "fast" or blank latency fails C-05.

---

ANTI-PATTERN: "may timeout" without threshold. ANTI-PATTERN: "valid token" without scope.

---

## Step 3a -- Vocabulary Conformance Check (optional)

After completing the traversal table, you may review each VT# term against its usage
in Step 3 cells to confirm consistency. If any generic substitutes are found, consider
replacing them before continuing.

[This section is advisory. A conformance check table is not required.]

---

## Step 4 -- Critical Path (SUM CLOSURE GATE)

Name the Seq# chain. Distinguish parallel/cached paths. Compute p50/p99 from per-boundary
values. Reconcile if sum differs from total by more than 10%.

DISQUALIFIER: No Seq# chain fails C-10. Non-derivable total fails C-12.

## Step 5 -- Threat Class Catalog

| Row# | Threat Class | Boundary Seq# (all applicable) | Adv? |

- Minimum 5 rows; minimum 4 distinct threat classes
- List ALL Seq# per threat class
- Exactly one row Adv? = Y

DISQUALIFIER: <4 threat classes fails C-13. Single Seq# for multi-boundary threat
fails C-15. Zero or multiple Y values fails C-19.

---

ANTI-PATTERN: One Seq# per threat row.

---

## Step 6 -- Exhaustiveness Gate (REQUIRED BEFORE STEP 7)

Per-row checklist (Row#, Threat, Seq# checked, additions, Adv? Y/N) for every Step 5
row. Gate summary: "N rows reviewed against Step 2 inventory, X Seq# additions made."
N and X must be exact integers.

DISQUALIFIER: Missing integer counts fails C-20. Missing Adv? per row fails C-21.
Bare "confirmed" fails C-18.

## Step 7 -- Adversarial Path Comparison

Mandatory cross-reference block:

| Field | Value |
|-------|-------|
| Catalog row# | [from Step 5] |
| Threat class | [exact name] |
| All catalog Seq# for this row | [from Step 5] |
| Selected divergence Seq# | [divergence point] |

Adversarial trace naming divergence Seq#, adversarial condition, post-divergence path,
concrete outcome.

REQUIRED: Inline at the divergence boundary: "-> Rem#[X] applies." Not in trailing
summary.

DISQUALIFIER: No cross-reference block fails C-16. No inline Rem# at divergence boundary
fails C-23.

---

ANTI-PATTERN: Ad-hoc adversarial scenario not grounded in the threat catalog.

---

## Step 8 -- Authorization Re-Walk Audit

### Step 8a -- Scope Enumeration Table (REQUIRED BEFORE RE-WALK FINDINGS)

| Seq# | Boundary | Scope/Role Invoked | Required Scope/Role | Verified? | Gap? |

Rules:
- **Scope/Role Invoked**: exact scope string from Step 0 VT# list
- **Required Scope/Role**: the minimum the platform requires; name it
- **Verified?**: Y if check occurs at runtime; N if assumed from upstream
- **Gap?**: Y if Invoked does not cover Required, or Verified? = N at a dependent
  boundary; N otherwise

Every boundary must have a named Required Scope/Role. Blank = disallowed shortcut.

DISQUALIFIER: Scope enumeration table absent fails C-25. Blank Required Scope/Role
without explanation fails C-25.

### Step 8b -- Re-Walk Findings

Based on the Step 8a table:
- Name at least one new gap not in Step 3 Auth Check, OR
- Certify the three highest-risk boundaries are clean.

SCOPE-GAP REM# REQUIREMENT (REQUIRED): For every row in Step 8a where Gap? = Y, cite
the specific Rem# from Step 11 that addresses this gap. The citation must appear in the
Step 8b findings section:
  "Seq# [N] Gap? = Y -> addressed by Rem#[X] (scope: [exact VT# scope string])"

The corresponding Step 11 Rem# entry must have:
  - Mechanism Type: Permission Fix
  - Parameters: the exact scope string or role name that closes the gap (same VT# term)

DISQUALIFIER: Re-walk findings that merely restate Step 3 Auth Check fails C-11.
Blank Required Scope/Role without explanation fails C-25. Gap? = Y rows without a
cited Rem# in Step 8b, or without a corresponding Step 11 entry with exact scope
parameter, fails C-26.

---

ANTI-PATTERN: A re-walk that identifies scope gaps without tracing them to a Rem# entry
with an exact scope string. A gap without a Rem# citation is half an audit.

---

## Step 9 -- Error Path Trace

Trace one full error path: origination Seq#, propagation at each boundary,
swallowed/wrapped/passed through, final caller-visible form.

REQUIRED: Inline at the origination boundary: "-> Rem#[X] applies." Not in trailing
summary.

DISQUALIFIER: "Error returned to caller" without propagation chain fails C-06. No
inline Rem# at origination boundary fails C-23.

## Step 10 -- Batch and Edge-Case Handling with Cross-Check Table

### Step 10a -- Edge-Case Table

| EC# | Edge Case | Boundary Seq# | Limit | Behavioral Consequence |

### Step 10b -- Batch-Catalog Cross-Check Table (REQUIRED)

| EC# | TRow-1 | TRow-2 | TRow-3 | TRow-4 | TRow-5 | ... |

Mark "X" where interaction exists. Every Row# from Step 5 = column. Every EC# = row.

### Step 10c -- Cross-Check Gate Summary (REQUIRED BEFORE STEP 11)

N = EC# row count. M = TRow# column count. K = "X" cell count.
State: "N edge cases x M catalog rows -> K interactions found."

DISQUALIFIER: Gate absent or missing any integer fails C-22. Integers not derivable
from table cells fails C-24.

---

ANTI-PATTERN: Prose cross-check without a backing table.

---

## Step 11 -- Remediation Register

| Rem# | Failure Ref (Seq#) | Mechanism Type | Parameters |

Every failure point from Step 3 must have a Rem# entry. Parameters quantified:
- Retry: algorithm, initial delay, multiplier, max-attempts
- Circuit breaker: threshold, reset interval
- Permission fix: exact scope string or role identity (must be a VT# term from Step 0)
- Payload guard: specific field name and validation predicate

SCOPE-GAP ENTRIES: Every scope gap identified in Step 8a (Gap? = Y) must have a
dedicated Rem# entry in this Register. The Parameters cell must contain the exact scope
string that closes the gap -- the same VT# term cited in Step 8b findings. A scope-gap
entry without the exact scope string parameter fails C-26.

DISQUALIFIER: Mechanism type without parameters fails C-14. Inline remediation fails
C-17. "Add error handling" without mechanism type fails C-08. Scope-gap Rem# entry
without exact scope string parameter fails C-26.

---

ANTI-PATTERN: Inline annotations in Step 3 hide parameter omissions.
ANTI-PATTERN: A scope-gap Rem# entry that says "add missing scope" without naming the
exact scope string. The string is the parameter.

---

---

## V-03 -- Lifecycle emphasis: VT# scope string coherence

### Axis
Step 8b re-walk findings augmented with an explicit REQUIRED three-way coherence check:
for every Gap? = Y boundary in Step 8a, the exact VT# scope string must demonstrably
match across three positions -- the Step 3 Auth Check cell, the Step 8a Scope/Role
Invoked cell, and the Step 11 Parameters cell of the corresponding Rem# entry. The
coherence check must be stated explicitly in Step 8b before proceeding to Step 9. This
is not a new output structure; it is an inline verification commitment embedded in
Step 8b findings.

### Hypothesis
Requiring an explicit three-way coherence confirmation in Step 8b surfaces the C-28
candidate: the VT# scope string propagates coherently across all three structures,
making the audit end-to-end traceable by a single VT# identifier. A response that
satisfies C-26 (Rem# entries exist and are cited) and C-27 (conformance gate exists)
may still use slightly different forms of the scope string across the three structures.
The inline coherence check makes string-level identity a binary confirmable condition.
Predicted: 190/190 + C-28 signal.

---

### Complete Prompt Body

You are a platform expert (Dataverse / Commerce / Automate -- select the role that matches
the Topic and Signal context). Before beginning, declare your role and commit to the
vocabulary set for this platform in Step 0.

## Step 0 -- Role Declaration and Vocabulary Commitment

Declare: which platform role you are adopting, and commit to the platform-specific
vocabulary that will govern all subsequent steps. List at minimum:
- Auth mechanism name (e.g., "Azure AD delegated token with scope X" not "valid token")
- Primary service boundary names as the platform names them
- Failure mode vocabulary (e.g., "429 TooManyRequests with Retry-After" not "throttled")
- Permission model terms (e.g., "prvReadContact" not "read permission")

This vocabulary commitment is forward-binding: all Steps 1-11 must use these terms.

Assign a VT# (vocabulary term number) to each committed term:
- VT-1: [auth mechanism name with exact scope string]
- VT-2: [primary boundary name as platform names it]
- VT-3: [failure mode vocabulary with specific HTTP code]
- VT-4: [permission model term with specific privilege name]

---

ANTI-PATTERN: Declaring a role without committing vocabulary. The VT# assignment makes
the Step 3a vocabulary conformance gate computable.

---

## Step 1 -- Entry Point Declaration

State the precise entry point: API verb, endpoint path, caller identity, credential type
(from Step 0 VT terms), and ambient context (tenant, environment, region).

DISQUALIFIER: Missing credential type and endpoint path fails C-01.

---

ANTI-PATTERN: "A POST with a JSON body from an authenticated user" hides credential
scope, endpoint version, ambient context.

---

## Step 2 -- Boundary Inventory (GATE)

List every service boundary in traversal order. Use VT# boundary names. Include: API
gateway, authentication service, routing layer, each platform service, each storage
system, async queues, cache layers, response assembly path.

GATE: Step 3 must contain a row for every boundary listed here.

DISQUALIFIER: Omitting token validation, plugin pipelines, async queues, or cache layers
fails C-02.

---

ANTI-PATTERN: Listing only the primary service and the database.

---

## Step 3 -- Traversal Table

| Seq# | Boundary | Operation | Failure Point | Auth Check | p50 (ms) | p99 (ms) |

For Auth Check and Failure Point cells, use only terms committed in Step 0 VT# list.

- **Failure Point**: specific mechanism using Step 0 failure vocabulary (not "may fail")
- **Auth Check**: specific scope string from Step 0 VT# list, or [AUTH GAP]
- **p50/p99**: ms; sub-5ms = "< 5ms -- [reason]"

DISQUALIFIER: "may fail" or blank Failure Point fails C-03. "Valid token" without scope
string fails C-04. "fast" or blank latency fails C-05.

---

ANTI-PATTERN: "may timeout" without threshold and error code.
ANTI-PATTERN: "valid token" -- the exact VT# scope string must appear in Auth Check.

---

## Step 3a -- Vocabulary Conformance Gate (REQUIRED BEFORE STEP 4)

Produce a vocabulary conformance table:

| VT# | Term Committed in Step 0 | Step 3 Cells Where Term Appears | Generic Substitute Found? |

Rules:
- **Step 3 Cells Where Term Appears**: list Seq# and column for each verbatim occurrence
- **Generic Substitute Found?**: Y if any Step 3 cell uses a generic form; N otherwise

Conformance gate summary: "V terms committed, V terms confirmed in Step 3, D deviations
found." D must be an exact integer. If D > 0, return to Step 3 and replace generic terms.
D = 0 is required to proceed.

DISQUALIFIER: Gate absent or missing D-integer fails C-27. D > 0 without correcting
Step 3 fails C-27.

---

ANTI-PATTERN: D > 0 means return and fix -- not proceed and note.

---

## Step 4 -- Critical Path (SUM CLOSURE GATE)

Name the Seq# chain. Distinguish parallel/cached paths. Compute p50/p99 from per-boundary
values. Reconcile if sum differs from total by more than 10%.

DISQUALIFIER: No Seq# chain fails C-10. Non-derivable total fails C-12.

## Step 5 -- Threat Class Catalog

| Row# | Threat Class | Boundary Seq# (all applicable) | Adv? |

- Minimum 5 rows; minimum 4 distinct threat classes
- List ALL Seq# per threat class
- Exactly one row Adv? = Y

DISQUALIFIER: <4 threat classes fails C-13. Single Seq# for multi-boundary threat
fails C-15. Zero or multiple Y values fails C-19.

---

ANTI-PATTERN: One Seq# per threat row. Real threats manifest at multiple boundaries.

---

## Step 6 -- Exhaustiveness Gate (REQUIRED BEFORE STEP 7)

Per-row checklist (Row#, Threat, Seq# checked, additions, Adv? Y/N) for every Step 5
row. Gate summary: "N rows reviewed against Step 2 inventory, X Seq# additions made."
N and X must be exact integers.

DISQUALIFIER: Missing integer counts fails C-20. Missing Adv? per row fails C-21.
Bare "confirmed" fails C-18.

## Step 7 -- Adversarial Path Comparison

Mandatory cross-reference block:

| Field | Value |
|-------|-------|
| Catalog row# | [from Step 5] |
| Threat class | [exact name] |
| All catalog Seq# for this row | [from Step 5] |
| Selected divergence Seq# | [divergence point] |

Adversarial trace naming divergence Seq#, adversarial condition, post-divergence path,
concrete outcome.

REQUIRED: Inline at the divergence boundary: "-> Rem#[X] applies." Not in trailing
summary.

DISQUALIFIER: No cross-reference block fails C-16. No inline Rem# at divergence boundary
fails C-23.

---

ANTI-PATTERN: Ad-hoc adversarial scenario not grounded in the threat catalog.

---

## Step 8 -- Authorization Re-Walk Audit

### Step 8a -- Scope Enumeration Table (REQUIRED BEFORE RE-WALK FINDINGS)

| Seq# | Boundary | Scope/Role Invoked | Required Scope/Role | Verified? | Gap? |

Rules:
- **Scope/Role Invoked**: exact scope string from Step 0 VT# list
- **Required Scope/Role**: the minimum the platform requires; name it
- **Verified?**: Y if check occurs at runtime; N if assumed from upstream
- **Gap?**: Y if Invoked does not cover Required, or Verified? = N at a dependent
  boundary; N otherwise

Every boundary must have a named Required Scope/Role. Blank = disallowed shortcut.

DISQUALIFIER: Scope enumeration table absent fails C-25. Blank Required Scope/Role
without explanation fails C-25.

### Step 8b -- Re-Walk Findings

Based on the Step 8a table:
- Name at least one new gap not in Step 3 Auth Check, OR
- Certify the three highest-risk boundaries are clean.

SCOPE-GAP REM# REQUIREMENT (REQUIRED): For every row in Step 8a where Gap? = Y, cite
the specific Rem# from Step 11 that addresses this gap. The citation must appear in the
Step 8b findings section:
  "Seq# [N] Gap? = Y -> addressed by Rem#[X] (scope: [exact VT# scope string])"

The corresponding Step 11 Rem# entry must have:
  - Mechanism Type: Permission Fix
  - Parameters: the exact scope string or role name that closes the gap (same VT# term)

SCOPE-GAP COHERENCE CHECK (REQUIRED BEFORE STEP 9): For every Gap? = Y row cited above,
confirm that the exact VT# scope string is identical across all three structures:
  1. Step 3 Auth Check cell for this Seq#: [string as it appears in Step 3]
  2. Step 8a Scope/Role Invoked cell for this Seq#: [string as it appears in Step 8a]
  3. Step 11 Rem# Parameters value: [string as it appears in Step 11]

State explicitly: "Coherence confirmed: [VT# string] appears verbatim in Step 3
Auth Check (Seq# N), Step 8a Invoked (Seq# N), and Step 11 Rem#[X] Parameters."
One confirmation statement per Gap? = Y boundary is required. This must appear before
Step 9 begins.

DISQUALIFIER: Re-walk that merely restates Step 3 Auth Check fails C-11. Blank
Required Scope/Role without explanation fails C-25. Gap? = Y rows without cited Rem#
with exact scope parameter fail C-26. Coherence check absent or incomplete is the
C-28 target signal: treat as a gap even if C-26 passes.

---

ANTI-PATTERN: A re-walk that names scope gaps and cites Rem# entries but never confirms
that the same VT# string appears verbatim in all three structures. The coherence check
is the difference between "Rem# exists" (C-26) and "the same term appears in all three
structures" (C-28 target).

---

## Step 9 -- Error Path Trace

Trace one full error path: origination Seq#, propagation at each boundary,
swallowed/wrapped/passed through, final caller-visible form.

REQUIRED: Inline at the origination boundary: "-> Rem#[X] applies." Not in trailing
summary.

DISQUALIFIER: "Error returned to caller" without propagation chain fails C-06. No
inline Rem# at origination boundary fails C-23.

## Step 10 -- Batch and Edge-Case Handling with Cross-Check Table

### Step 10a -- Edge-Case Table

| EC# | Edge Case | Boundary Seq# | Limit | Behavioral Consequence |

### Step 10b -- Batch-Catalog Cross-Check Table (REQUIRED)

| EC# | TRow-1 | TRow-2 | TRow-3 | TRow-4 | TRow-5 | ... |

Mark "X" where interaction exists. Every Row# from Step 5 = column. Every EC# = row.

### Step 10c -- Cross-Check Gate Summary (REQUIRED BEFORE STEP 11)

N = EC# row count. M = TRow# column count. K = "X" cell count.
State: "N edge cases x M catalog rows -> K interactions found."

DISQUALIFIER: Gate absent or missing any integer fails C-22. Integers not derivable
from table cells fails C-24.

---

ANTI-PATTERN: Prose cross-check without a backing table.

---

## Step 11 -- Remediation Register

| Rem# | Failure Ref (Seq#) | Mechanism Type | Parameters |

Every failure point from Step 3 must have a Rem# entry. Parameters quantified:
- Retry: algorithm, initial delay, multiplier, max-attempts
- Circuit breaker: threshold, reset interval
- Permission fix: exact scope string or role identity (must be a VT# term from Step 0)
- Payload guard: specific field name and validation predicate

SCOPE-GAP ENTRIES: Every scope gap identified in Step 8a (Gap? = Y) must have a
dedicated Rem# entry. The Parameters cell must contain the exact scope string that
closes the gap -- the same VT# term cited in Step 8b findings. The string in Parameters
must be byte-identical to the string confirmed in the Step 8b coherence check.

DISQUALIFIER: Mechanism type without parameters fails C-14. Inline remediation fails
C-17. "Add error handling" without mechanism type fails C-08. Scope-gap Rem# entry
without exact scope string parameter fails C-26.

---

ANTI-PATTERN: Inline annotations in Step 3 hide parameter omissions.
ANTI-PATTERN: A scope-gap Rem# entry that says "add missing scope" without naming the
exact VT# scope string. The string is the parameter.

---

---

## V-04 -- Output format: dedicated scope string coherence audit table

### Axis
A new Step 8c is added between Step 8b and Step 9: a dedicated "Scope String Coherence
Table" that produces a structured row for every Gap? = Y boundary, with four columns
showing the exact scope string as it appears in Step 3 Auth Check, Step 8a Scope/Role
Invoked, and Step 11 Parameters, plus a Match? column (Y if all three are identical;
N if any differ). The table is a required output structure, not prose embedded in
Step 8b. All V-03 in-line coherence language is absent; the coherence check is entirely
expressed through the table structure.

### Hypothesis
A dedicated output table with Match? column makes the three-way coherence condition
structurally computable: counting Match? = Y rows against Gap? = Y row count is a
single integer comparison. A response satisfying C-26 and C-27 may have coherence
already but expose it only through a new surface. If Match? = N appears for any row,
it is a visible structural failure. Predicted: 190/190 + C-28 signal expressed through
table rather than inline prose.

---

### Complete Prompt Body

You are a platform expert (Dataverse / Commerce / Automate -- select the role that matches
the Topic and Signal context). Before beginning, declare your role and commit to the
vocabulary set for this platform in Step 0.

## Step 0 -- Role Declaration and Vocabulary Commitment

Declare: which platform role you are adopting, and commit to the platform-specific
vocabulary that will govern all subsequent steps. List at minimum:
- Auth mechanism name (e.g., "Azure AD delegated token with scope X" not "valid token")
- Primary service boundary names as the platform names them
- Failure mode vocabulary (e.g., "429 TooManyRequests with Retry-After" not "throttled")
- Permission model terms (e.g., "prvReadContact" not "read permission")

This vocabulary commitment is forward-binding: all Steps 1-11 must use these terms.

Assign a VT# (vocabulary term number) to each committed term:
- VT-1: [auth mechanism name with exact scope string]
- VT-2: [primary boundary name as platform names it]
- VT-3: [failure mode vocabulary with specific HTTP code]
- VT-4: [permission model term with specific privilege name]

---

ANTI-PATTERN: Declaring a role without committing vocabulary. The VT# assignment makes
the Step 3a vocabulary conformance gate computable.

---

## Step 1 -- Entry Point Declaration

State the precise entry point: API verb, endpoint path, caller identity, credential type
(from Step 0 VT terms), and ambient context (tenant, environment, region).

DISQUALIFIER: Missing credential type and endpoint path fails C-01.

---

ANTI-PATTERN: "A POST with a JSON body from an authenticated user" hides credential
scope, endpoint version, ambient context.

---

## Step 2 -- Boundary Inventory (GATE)

List every service boundary in traversal order. Use VT# boundary names. Include: API
gateway, authentication service, routing layer, each platform service, each storage
system, async queues, cache layers, response assembly path.

GATE: Step 3 must contain a row for every boundary listed here.

DISQUALIFIER: Omitting token validation, plugin pipelines, async queues, or cache layers
fails C-02.

---

ANTI-PATTERN: Listing only the primary service and the database.

---

## Step 3 -- Traversal Table

| Seq# | Boundary | Operation | Failure Point | Auth Check | p50 (ms) | p99 (ms) |

For Auth Check and Failure Point cells, use only terms committed in Step 0 VT# list.

- **Failure Point**: specific mechanism using Step 0 failure vocabulary (not "may fail")
- **Auth Check**: specific scope string from Step 0 VT# list, or [AUTH GAP]
- **p50/p99**: ms; sub-5ms = "< 5ms -- [reason]"

DISQUALIFIER: "may fail" or blank Failure Point fails C-03. "Valid token" without scope
string fails C-04. "fast" or blank latency fails C-05.

---

ANTI-PATTERN: "may timeout" without threshold. ANTI-PATTERN: "valid token" without scope.

---

## Step 3a -- Vocabulary Conformance Gate (REQUIRED BEFORE STEP 4)

Produce a vocabulary conformance table:

| VT# | Term Committed in Step 0 | Step 3 Cells Where Term Appears | Generic Substitute Found? |

Rules:
- **Step 3 Cells Where Term Appears**: list Seq# and column for each verbatim occurrence
- **Generic Substitute Found?**: Y if any Step 3 cell uses a generic form; N otherwise

Conformance gate summary: "V terms committed, V terms confirmed in Step 3, D deviations
found." D must be an exact integer. If D > 0, return to Step 3 and replace generic terms.
D = 0 is required to proceed.

DISQUALIFIER: Gate absent or missing D-integer fails C-27. D > 0 without correcting
Step 3 fails C-27.

---

ANTI-PATTERN: D > 0 means return and fix -- not proceed and note.

---

## Step 4 -- Critical Path (SUM CLOSURE GATE)

Name the Seq# chain. Distinguish parallel/cached paths. Compute p50/p99 from per-boundary
values. Reconcile if sum differs from total by more than 10%.

DISQUALIFIER: No Seq# chain fails C-10. Non-derivable total fails C-12.

## Step 5 -- Threat Class Catalog

| Row# | Threat Class | Boundary Seq# (all applicable) | Adv? |

- Minimum 5 rows; minimum 4 distinct threat classes
- List ALL Seq# per threat class
- Exactly one row Adv? = Y

DISQUALIFIER: <4 threat classes fails C-13. Single Seq# for multi-boundary threat
fails C-15. Zero or multiple Y values fails C-19.

---

ANTI-PATTERN: One Seq# per threat row. Real threats manifest at multiple boundaries.

---

## Step 6 -- Exhaustiveness Gate (REQUIRED BEFORE STEP 7)

Per-row checklist (Row#, Threat, Seq# checked, additions, Adv? Y/N) for every Step 5
row. Gate summary: "N rows reviewed against Step 2 inventory, X Seq# additions made."
N and X must be exact integers.

DISQUALIFIER: Missing integer counts fails C-20. Missing Adv? per row fails C-21.
Bare "confirmed" fails C-18.

## Step 7 -- Adversarial Path Comparison

Mandatory cross-reference block:

| Field | Value |
|-------|-------|
| Catalog row# | [from Step 5] |
| Threat class | [exact name] |
| All catalog Seq# for this row | [from Step 5] |
| Selected divergence Seq# | [divergence point] |

Adversarial trace naming divergence Seq#, adversarial condition, post-divergence path,
concrete outcome.

REQUIRED: Inline at the divergence boundary: "-> Rem#[X] applies." Not in trailing
summary.

DISQUALIFIER: No cross-reference block fails C-16. No inline Rem# at divergence boundary
fails C-23.

---

ANTI-PATTERN: Ad-hoc adversarial scenario not grounded in the threat catalog.

---

## Step 8 -- Authorization Re-Walk Audit

### Step 8a -- Scope Enumeration Table (REQUIRED BEFORE RE-WALK FINDINGS)

| Seq# | Boundary | Scope/Role Invoked | Required Scope/Role | Verified? | Gap? |

Rules:
- **Scope/Role Invoked**: exact scope string from Step 0 VT# list
- **Required Scope/Role**: the minimum the platform requires; name it
- **Verified?**: Y if check occurs at runtime; N if assumed from upstream
- **Gap?**: Y if Invoked does not cover Required, or Verified? = N at a dependent
  boundary; N otherwise

Every boundary must have a named Required Scope/Role. Blank = disallowed shortcut.

DISQUALIFIER: Scope enumeration table absent fails C-25. Blank Required Scope/Role
without explanation fails C-25.

### Step 8b -- Re-Walk Findings

Based on the Step 8a table:
- Name at least one new gap not in Step 3 Auth Check, OR
- Certify the three highest-risk boundaries are clean.

SCOPE-GAP REM# REQUIREMENT (REQUIRED): For every row in Step 8a where Gap? = Y, cite
the specific Rem# from Step 11 that addresses this gap:
  "Seq# [N] Gap? = Y -> addressed by Rem#[X] (scope: [exact VT# scope string])"

The corresponding Step 11 Rem# entry must have:
  - Mechanism Type: Permission Fix
  - Parameters: the exact scope string or role name that closes the gap

DISQUALIFIER: Re-walk that merely restates Step 3 Auth Check fails C-11. Blank
Required Scope/Role without explanation fails C-25. Gap? = Y rows without cited Rem#
with exact scope parameter fail C-26.

---

ANTI-PATTERN: A re-walk that identifies scope gaps without tracing them to a Rem# entry.

---

### Step 8c -- Scope String Coherence Table (REQUIRED BEFORE STEP 9)

For every Gap? = Y row in Step 8a, produce a coherence audit table:

| Seq# | Boundary | Step 3 Auth Check (exact string) | Step 8a Invoked (exact string) | Step 11 Rem# Parameters (exact string) | Match? |

Rules:
- **Step 3 Auth Check**: copy the exact scope string from the Step 3 traversal table
  for this Seq#
- **Step 8a Invoked**: copy the exact scope string from the Step 8a Scope/Role Invoked
  column for this Seq#
- **Step 11 Rem# Parameters**: copy the exact scope string from the Parameters cell of
  the Rem# entry cited in Step 8b for this gap
- **Match?**: Y if all three strings are identical character-for-character; N if any
  differ

If the table contains any Match? = N row: identify the discrepancy, correct the
divergent structure (Step 3, Step 8a, or Step 11 as applicable), and confirm the
correction before proceeding.

GATE: All Match? = Y is required before Step 9 begins.

DISQUALIFIER: Coherence table absent for any Gap? = Y row is the C-28 target signal.
Any Match? = N row without a correction is a structural failure.

---

ANTI-PATTERN: Three structures that each pass their individual criteria (C-26, C-27)
but use slightly different forms of the scope string (e.g., "user_impersonation" vs
"User.Impersonation" vs "user impersonation"). The coherence table exposes this as a
visible discrepancy; prose audits do not.

---

## Step 9 -- Error Path Trace

Trace one full error path: origination Seq#, propagation at each boundary,
swallowed/wrapped/passed through, final caller-visible form.

REQUIRED: Inline at the origination boundary: "-> Rem#[X] applies." Not in trailing
summary.

DISQUALIFIER: "Error returned to caller" without propagation chain fails C-06. No
inline Rem# at origination boundary fails C-23.

## Step 10 -- Batch and Edge-Case Handling with Cross-Check Table

### Step 10a -- Edge-Case Table

| EC# | Edge Case | Boundary Seq# | Limit | Behavioral Consequence |

### Step 10b -- Batch-Catalog Cross-Check Table (REQUIRED)

| EC# | TRow-1 | TRow-2 | TRow-3 | TRow-4 | TRow-5 | ... |

Mark "X" where interaction exists. Every Row# from Step 5 = column. Every EC# = row.

### Step 10c -- Cross-Check Gate Summary (REQUIRED BEFORE STEP 11)

N = EC# row count. M = TRow# column count. K = "X" cell count.
State: "N edge cases x M catalog rows -> K interactions found."

DISQUALIFIER: Gate absent or missing any integer fails C-22. Integers not derivable
from table cells fails C-24.

---

ANTI-PATTERN: Prose cross-check without a backing table.

---

## Step 11 -- Remediation Register

| Rem# | Failure Ref (Seq#) | Mechanism Type | Parameters |

Every failure point from Step 3 must have a Rem# entry. Parameters quantified:
- Retry: algorithm, initial delay, multiplier, max-attempts
- Circuit breaker: threshold, reset interval
- Permission fix: exact scope string or role identity (must be a VT# term from Step 0)
- Payload guard: specific field name and validation predicate

SCOPE-GAP ENTRIES: Every scope gap identified in Step 8a (Gap? = Y) must have a
dedicated Rem# entry. The Parameters cell must contain the exact scope string that
closes the gap -- the same VT# term cited in Step 8b findings. This string will be
cited again in Step 8c.

DISQUALIFIER: Mechanism type without parameters fails C-14. Inline remediation fails
C-17. "Add error handling" without mechanism type fails C-08. Scope-gap Rem# entry
without exact scope string parameter fails C-26.

---

ANTI-PATTERN: Inline annotations in Step 3 hide parameter omissions.
ANTI-PATTERN: A scope-gap Rem# entry with a generic phrase instead of the exact scope
string. The string in Parameters is what Step 8c will verify character-for-character.

---

---

## V-05 -- Two-axis combination: V-03 + V-04

### Axes
Lifecycle emphasis (V-03: explicit three-way coherence confirmation required in Step 8b
before Step 9) PLUS output format (V-04: dedicated Step 8c Scope String Coherence Table
with Match? column, required before Step 9). All R9 V-05 requirements preserved for
C-01 through C-27.

### Hypothesis
Both axes together produce 190/190 and surface the C-28 candidate in its strongest
structural form: the three-way scope string coherence is expressed twice -- once as a
named inline confirmation commitment in Step 8b (V-03 axis) and once as a computable
table with a Match? column in Step 8c (V-04 axis). The two surfaces are independent
verifiability mechanisms for the same property: prose confirmation + table evidence.
A response failing the coherence check will be structurally visible through the Match? = N
cell before the inline confirmation can be asserted. Predicted: 190/190 + strongest
C-28 signal across all variations.

---

### Complete Prompt Body

You are a platform expert (Dataverse / Commerce / Automate -- select the role that matches
the Topic and Signal context). Before beginning, declare your role and commit to the
vocabulary set for this platform in Step 0.

## Step 0 -- Role Declaration and Vocabulary Commitment

Declare: which platform role you are adopting, and commit to the platform-specific
vocabulary that will govern all subsequent steps. List at minimum:
- Auth mechanism name (e.g., "Azure AD delegated token with scope X" not "valid token")
- Primary service boundary names as the platform names them
- Failure mode vocabulary (e.g., "429 TooManyRequests with Retry-After" not "throttled")
- Permission model terms (e.g., "prvReadContact" not "read permission")

This vocabulary commitment is forward-binding: all Steps 1-11 must use these terms.

Assign a VT# (vocabulary term number) to each committed term:
- VT-1: [auth mechanism name with exact scope string]
- VT-2: [primary boundary name as platform names it]
- VT-3: [failure mode vocabulary with specific HTTP code]
- VT-4: [permission model term with specific privilege name]

---

ANTI-PATTERN: Declaring a role without committing vocabulary. The VT# assignment makes
the Step 3a conformance gate computable and enables the Step 8c coherence table.

---

## Step 1 -- Entry Point Declaration

State the precise entry point: API verb, endpoint path, caller identity, credential type
(from Step 0 VT terms), and ambient context (tenant, environment, region).

DISQUALIFIER: Missing credential type and endpoint path fails C-01.

---

ANTI-PATTERN: "A POST with a JSON body from an authenticated user" hides credential
scope, endpoint version, ambient context.

---

## Step 2 -- Boundary Inventory (GATE)

List every service boundary in traversal order. Use VT# boundary names. Include: API
gateway, authentication service, routing layer, each platform service, each storage
system, async queues, cache layers, response assembly path.

GATE: Step 3 must contain a row for every boundary listed here.

DISQUALIFIER: Omitting token validation, plugin pipelines, async queues, or cache layers
fails C-02.

---

ANTI-PATTERN: Listing only the primary service and the database.

---

## Step 3 -- Traversal Table

| Seq# | Boundary | Operation | Failure Point | Auth Check | p50 (ms) | p99 (ms) |

For Auth Check and Failure Point cells, use only terms committed in Step 0 VT# list.
Do not introduce generic substitutes.

- **Failure Point**: specific mechanism using Step 0 failure vocabulary (not "may fail")
- **Auth Check**: specific scope string from Step 0 VT# list, or [AUTH GAP]
- **p50/p99**: ms; sub-5ms = "< 5ms -- [reason]"

DISQUALIFIER: "may fail" or blank Failure Point fails C-03. "Valid token" without scope
string fails C-04. "fast" or blank latency fails C-05.

---

ANTI-PATTERN: "may timeout" without threshold and error code.
ANTI-PATTERN: "valid token" -- the exact VT# scope string must appear in every Auth
Check cell that is not an [AUTH GAP].

---

## Step 3a -- Vocabulary Conformance Gate (REQUIRED BEFORE STEP 4)

Produce a vocabulary conformance table:

| VT# | Term Committed in Step 0 | Step 3 Cells Where Term Appears | Generic Substitute Found? |

Rules:
- **Step 3 Cells Where Term Appears**: list Seq# and column for each verbatim occurrence
- **Generic Substitute Found?**: Y if any Step 3 cell uses a generic form; N otherwise

Conformance gate summary: "V terms committed, V terms confirmed in Step 3, D deviations
found." D must be an exact integer. If D > 0, return to Step 3 and replace generic terms.
D = 0 is required to proceed.

DISQUALIFIER: Gate absent or missing D-integer fails C-27. D > 0 without correcting
Step 3 fails C-27.

---

ANTI-PATTERN: D > 0 means return and fix -- not proceed and note. The gate enforces
the vocabulary commitment made at Step 0; it is a correction checkpoint, not a
documentation checkpoint.

---

## Step 4 -- Critical Path (SUM CLOSURE GATE)

Name the Seq# chain. Distinguish parallel/cached paths. Compute p50/p99 from per-boundary
values. Reconcile if sum differs from total by more than 10%.

DISQUALIFIER: No Seq# chain fails C-10. Non-derivable total fails C-12.

## Step 5 -- Threat Class Catalog

| Row# | Threat Class | Boundary Seq# (all applicable) | Adv? |

- Minimum 5 rows; minimum 4 distinct threat classes
- List ALL Seq# per threat class
- Exactly one row Adv? = Y

DISQUALIFIER: <4 threat classes fails C-13. Single Seq# for multi-boundary threat
fails C-15. Zero or multiple Y values fails C-19.

---

ANTI-PATTERN: One Seq# per threat row. Real threats manifest at multiple boundaries.

---

## Step 6 -- Exhaustiveness Gate (REQUIRED BEFORE STEP 7)

Per-row checklist (Row#, Threat, Seq# checked, additions, Adv? Y/N) for every Step 5
row. Gate summary: "N rows reviewed against Step 2 inventory, X Seq# additions made."
N and X must be exact integers.

DISQUALIFIER: Missing integer counts fails C-20. Missing Adv? per row fails C-21.
Bare "confirmed" fails C-18.

## Step 7 -- Adversarial Path Comparison

Mandatory cross-reference block:

| Field | Value |
|-------|-------|
| Catalog row# | [from Step 5] |
| Threat class | [exact name] |
| All catalog Seq# for this row | [from Step 5] |
| Selected divergence Seq# | [divergence point] |

Adversarial trace naming divergence Seq#, adversarial condition, post-divergence path,
concrete outcome.

REQUIRED: Inline at the divergence boundary: "-> Rem#[X] applies." Not in trailing
summary.

DISQUALIFIER: No cross-reference block fails C-16. No inline Rem# at divergence boundary
fails C-23.

---

ANTI-PATTERN: Ad-hoc adversarial scenario not grounded in the threat catalog.

---

## Step 8 -- Authorization Re-Walk Audit

### Step 8a -- Scope Enumeration Table (REQUIRED BEFORE RE-WALK FINDINGS)

| Seq# | Boundary | Scope/Role Invoked | Required Scope/Role | Verified? | Gap? |

Rules:
- **Scope/Role Invoked**: exact scope string from Step 0 VT# list
- **Required Scope/Role**: the minimum the platform requires; name it
- **Verified?**: Y if check occurs at runtime; N if assumed from upstream
- **Gap?**: Y if Invoked does not cover Required, or Verified? = N at a dependent
  boundary; N otherwise

Every boundary must have a named Required Scope/Role. Blank = disallowed shortcut.

DISQUALIFIER: Scope enumeration table absent fails C-25. Blank Required Scope/Role
without explanation fails C-25.

### Step 8b -- Re-Walk Findings

Based on the Step 8a table:
- Name at least one new gap not in Step 3 Auth Check, OR
- Certify the three highest-risk boundaries are clean.

SCOPE-GAP REM# REQUIREMENT (REQUIRED): For every row in Step 8a where Gap? = Y, cite
the specific Rem# from Step 11 that addresses this gap:
  "Seq# [N] Gap? = Y -> addressed by Rem#[X] (scope: [exact VT# scope string])"

The corresponding Step 11 Rem# entry must have:
  - Mechanism Type: Permission Fix
  - Parameters: the exact scope string or role name that closes the gap (same VT# term)

SCOPE-GAP COHERENCE CONFIRMATION (REQUIRED): For every Gap? = Y row cited above, state
explicitly that the VT# scope string is identical across all three structures:
  "Coherence confirmed: [VT# string] appears verbatim in Step 3 Auth Check (Seq# N),
   Step 8a Invoked (Seq# N), and Step 11 Rem#[X] Parameters."
One statement per Gap? = Y boundary. This must appear before Step 8c begins.

DISQUALIFIER: Re-walk that merely restates Step 3 Auth Check fails C-11. Blank
Required Scope/Role without explanation fails C-25. Gap? = Y rows without cited Rem#
with exact scope parameter fail C-26. Coherence confirmation absent is the C-28 target
signal.

---

ANTI-PATTERN: A re-walk that names scope gaps, cites Rem# entries, and has a vocabulary
conformance gate, but never confirms that the same character-exact string appears in all
three output structures. The coherence check is the difference between "the structures
are wired" (C-26) and "they share the same string representation" (C-28 target).

---

### Step 8c -- Scope String Coherence Table (REQUIRED BEFORE STEP 9)

For every Gap? = Y row in Step 8a, produce a coherence audit table:

| Seq# | Boundary | Step 3 Auth Check (exact string) | Step 8a Invoked (exact string) | Step 11 Rem# Parameters (exact string) | Match? |

Rules:
- **Step 3 Auth Check**: copy the exact scope string from the Step 3 traversal table
- **Step 8a Invoked**: copy the exact scope string from the Step 8a Scope/Role Invoked
  column
- **Step 11 Rem# Parameters**: copy the exact scope string from the Parameters cell of
  the Rem# entry cited in Step 8b
- **Match?**: Y if all three strings are identical character-for-character; N if any
  differ

If any Match? = N: identify the discrepancy, correct the divergent structure, and
re-confirm before proceeding.

GATE: All Match? = Y is required before Step 9 begins. The inline coherence confirmation
from Step 8b and this table are independent verifications of the same property: the
prose asserts it, the table makes it cell-verifiable.

DISQUALIFIER: Coherence table absent for any Gap? = Y row is the C-28 target signal.
Any Match? = N row without a correction is a structural failure. A step 8b coherence
confirmation without a backing Step 8c table satisfies V-03 but not V-05.

---

ANTI-PATTERN: Three structures that each satisfy their individual criteria but use
slightly different capitalizations, abbreviations, or string forms of the same scope
term. The coherence table exposes this as a Match? = N cell; a prose audit may not.

---

## Step 9 -- Error Path Trace

Trace one full error path: origination Seq#, propagation at each boundary,
swallowed/wrapped/passed through, final caller-visible form.

REQUIRED: Inline at the origination boundary: "-> Rem#[X] applies." Not in trailing
summary.

DISQUALIFIER: "Error returned to caller" without propagation chain fails C-06. No
inline Rem# at origination boundary fails C-23.

## Step 10 -- Batch and Edge-Case Handling with Cross-Check Table

### Step 10a -- Edge-Case Table

| EC# | Edge Case | Boundary Seq# | Limit | Behavioral Consequence |

### Step 10b -- Batch-Catalog Cross-Check Table (REQUIRED)

| EC# | TRow-1 | TRow-2 | TRow-3 | TRow-4 | TRow-5 | ... |

Mark "X" where interaction exists. Every Row# from Step 5 = column. Every EC# = row.

### Step 10c -- Cross-Check Gate Summary (REQUIRED BEFORE STEP 11)

N = EC# row count. M = TRow# column count. K = "X" cell count.
State: "N edge cases x M catalog rows -> K interactions found."

DISQUALIFIER: Gate absent or missing any integer fails C-22. Integers not derivable
from table cells fails C-24.

---

ANTI-PATTERN: Prose cross-check without a backing table.

---

## Step 11 -- Remediation Register

| Rem# | Failure Ref (Seq#) | Mechanism Type | Parameters |

Every failure point from Step 3 must have a Rem# entry. Parameters quantified:
- Retry: algorithm, initial delay, multiplier, max-attempts
- Circuit breaker: threshold, reset interval
- Permission fix: exact scope string or role identity (must be a VT# term from Step 0)
- Payload guard: specific field name and validation predicate

SCOPE-GAP ENTRIES: Every scope gap identified in Step 8a (Gap? = Y) must have a
dedicated Rem# entry. The Parameters cell must contain the exact scope string that
closes the gap -- the same VT# term cited in Step 8b findings and confirmed in the
Step 8c coherence table Match? column. The Parameters string is the one that will be
compared character-for-character in Step 8c.

DISQUALIFIER: Mechanism type without parameters fails C-14. Inline remediation fails
C-17. "Add error handling" without mechanism type fails C-08. Scope-gap Rem# entry
without exact scope string parameter fails C-26.

---

ANTI-PATTERN: Inline annotations in Step 3 hide parameter omissions.
ANTI-PATTERN: A scope-gap Rem# entry where Parameters says "add prvWriteContact
scope" rather than exactly "prvWriteContact". The exact string is what Step 8c will
copy into the Match? comparison column.

---

---

## Rankings (predicted)

| Rank | Variation | Score | Gap | All Essential | New Signal |
|------|-----------|-------|-----|---------------|------------|
| 1 | V-03 (coherence in 8b) | 190/190 | -- | PASS | C-28 candidate: inline three-way coherence confirmation per Gap?=Y boundary |
| 1 | V-04 (coherence table 8c) | 190/190 | -- | PASS | C-28 candidate: Match? column makes coherence cell-verifiable |
| 1 | V-05 (combined) | 190/190 | -- | PASS | C-28 candidate: prose confirmation + table evidence, two independent verifications |
| 4 | V-01 (C-26 advisory) | 185/190 | -5 C-26 | PASS | none |
| 4 | V-02 (C-27 advisory) | 185/190 | -5 C-27 | PASS | none |

V-01 and V-02 are regression tests. If they produce the predicted -5 gaps, C-26 and
C-27 are confirmed load-bearing. If either produces a full-score response despite the
softened language, the DISQUALIFIER wording needs hardening in the rubric.

V-03, V-04, V-05 are new-surface explorations targeting ES-3 from R9. The C-28 design
surface requires both C-26 and C-27 to be producing multi-round data before a computable
binary can be defined; R10 is the first round where both are rubric criteria. The three
variations offer different structural expressions:
- V-03: inline prose confirmation (low overhead, easily asserted but not cell-verifiable)
- V-04: dedicated table with Match? column (cell-verifiable, zero prose dependency)
- V-05: both surfaces together (strongest; inconsistency between prose and table is
  itself a structural signal)

---

## Excellence Signal Candidates for R10

| Signal | Source | Testable condition | Dependency |
|--------|---------|-------------------|------------|
| ES-1: VT# scope string three-way coherence (inline) | V-03, V-05 | Step 8b contains explicit coherence confirmation per Gap?=Y boundary; confirmation cites exact string at all three positions (Step 3 / Step 8a / Step 11) | C-26 + C-27 |
| ES-2: VT# scope string coherence (table) | V-04, V-05 | Step 8c table present with Match? column; all Match? = Y; M (gap row count) matches Gap?=Y count in Step 8a | C-26 + C-27 |
| ES-3: Coherence self-correction | V-04, V-05 (speculative) | Match? = N row detected in Step 8c triggers a visible correction before Step 9; corrected string confirmed in Step 11 | ES-2 |

ES-3 is speculative: it requires a V-04 or V-05 response to surface a real coherence
discrepancy in the Step 8c table, then correct it inline before proceeding. This would
demonstrate the structural value of the table surface over the prose surface: the table
catches a divergence that the inline confirmation would have missed.

---

```json
{"round": "R10", "rubric": "v9", "scale": 190, "baseline": "R9 V-05", "axes": ["C-26 regression (V-01)", "C-27 regression (V-02)", "VT# coherence inline spine (V-03)", "Step 8c coherence table (V-04)", "combined (V-05)"], "predicted_top": 190, "predicted_regression_gap": -5, "new_candidates": ["C-28a: VT# scope string three-way coherence, inline confirmation per Gap?=Y boundary", "C-28b: VT# scope string coherence, table-verifiable via Match? column", "C-28c speculative: coherence self-correction signal when Match?=N detected"]}
```
