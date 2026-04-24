# trace-request rubric v8 -- Skill Body Prompt Variations R9
# Generated: 2026-03-15

## Overview

Five complete, runnable skill body prompt variations for the `trace-request` skill,
targeting the v8 rubric (180 pts, C-01 through C-25).

**R8 result**: V-01/V-02 regression tests confirmed C-22 and C-23 load-bearing (-5 each
as predicted). V-03 (cross-check table) produced ES-1 -- K integer derivable from a
visible EC# x TRow# table -- promoted to C-24. V-04 (scope enumeration) produced ES-2 --
per-boundary scope vs required scope table with Gap? column -- promoted to C-25. V-05
(combined) produced both. Top score: 170/170 (V-03, V-04, V-05 on v7 rubric); the two
new criteria add 10 pts bringing v8 scale to 180.

**R9 baseline**: R8 V-05 body (cross-check table at Step 10b + scope enumeration table
at Step 8a, both required, plus all prior criteria).

**R9 variation surface**: Two regression tests confirm C-24 and C-25 are load-bearing
(V-01, V-02). Three new-axis explorations target C-26 design space: ES-3 scope-gap
Rem# propagation (V-03), Step 0 vocabulary conformance gate (V-04), and combined (V-05).

---

## Variation Summary Table

| V | Axis | Key change from R8 V-05 baseline | C-24 | C-25 | New signal | Predicted |
|---|------|----------------------------------|------|------|------------|-----------|
| V-01 | Phrasing register: C-24 advisory | Step 10b cross-check table softened to advisory; gate summary remains but derivation from table not required | FAIL | PASS | none | 175/180 |
| V-02 | Phrasing register: C-25 advisory | Step 8a scope enumeration table softened to advisory; re-walk findings remain | PASS | FAIL | none | 175/180 |
| V-03 | Lifecycle emphasis: scope-gap Rem# propagation | Step 8b requires every Gap?=Y row to cite a dedicated Rem# entry in Step 11 with exact scope string parameter | PASS | PASS | C-26 candidate: scope-gap entries traceable to Rem# with scope parameters | 180/180 |
| V-04 | Output format: Step 0 vocabulary conformance gate | New Step 3a after traversal: every Step 0 committed term cited at its first Step 3 cell; any uncited generic term flagged; conformance integer summary | PASS | PASS | C-26 candidate: vocabulary conformance gate computable | 180/180 |
| V-05 | Two-axis combination (V-03 + V-04) | Scope-gap Rem# propagation + vocabulary conformance gate | PASS | PASS | Two C-26 candidates | 180/180 |

---

## V-01 -- Phrasing register: C-24 advisory

### Axis
Step 10b cross-check table (EC# x TRow#) softened from required to advisory. The
three-integer gate summary in Step 10c is still required, satisfying C-22. But the
table from which integers would be derived is only suggested, not mandated. All R8
V-05 requirements preserved for C-01 through C-23 and C-25.

### Hypothesis
Removing the required backing cross-check table from Step 10 while retaining the
three-integer gate causes C-24 FAIL (gate integers present but not table-derivable)
while all other criteria including C-22 and C-25 hold. Predicted: 175/180 (-5 C-24).

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

This vocabulary commitment is forward-binding: all Steps 1-11 must use these terms, not
generic substitutes.

---

ANTI-PATTERN: Declaring a role without committing vocabulary. The vocabulary commitment
is the binding contract that makes C-03, C-04, and C-14 specific.

---

## Step 1 -- Entry Point Declaration

State the precise entry point: the API verb, endpoint path, caller identity, credential
type (from Step 0), and ambient context (tenant, environment, region). If the topic
involves a user action, name the trigger (UI gesture, automation event, webhook payload).

DISQUALIFIER: "A request is made" or "the user calls the API" without the credential type
and endpoint path fails C-01.

---

ANTI-PATTERN: "A POST with a JSON body from an authenticated user." This hides credential
scope, endpoint version, and ambient context.

---

## Step 2 -- Boundary Inventory (GATE)

List every service boundary this request will cross, in traversal order. Use the boundary
names committed in Step 0. Include: API gateway, authentication service, routing layer,
each microservice or platform service, each storage system, any async queue or event bus,
cache layers, and the response assembly path.

GATE: Step 3 must contain a row for every boundary listed here, in order.

DISQUALIFIER: Omitting token validation, plugin pipeline stages, async queues, or cache
layers fails C-02.

---

ANTI-PATTERN: Listing only the primary service and the database. Real requests cross
4-8 boundaries before storage is reached.

---

## Step 3 -- Traversal Table

Produce a boundary traversal table with the following columns for every boundary from
Step 2:

| Seq# | Boundary | Operation | Failure Point | Auth Check | p50 (ms) | p99 (ms) |

Rules:
- **Seq#**: sequential integer, referenced throughout Steps 4-11
- **Failure Point**: name the specific mechanism (e.g., "token expiry -> 401 Unauthorized",
  not "may fail")
- **Auth Check**: name the specific scope string or role check, or mark [AUTH GAP]
- **p50/p99**: estimate in ms; sub-5ms entries annotated "< 5ms -- [reason]"

DISQUALIFIER: "may fail," "could timeout," or blank Failure Point fails C-03. "Valid
token" or "authenticated" without scope string fails C-04. "fast" or blank latency
fails C-05.

---

ANTI-PATTERN: Failure points that say "may timeout" without the threshold and error code.
ANTI-PATTERN: Auth fields that say "valid token" -- this hides a gap as a confirmation.

---

## Step 4 -- Critical Path (SUM CLOSURE GATE)

Identify the critical path: the specific Seq# chain whose cumulative latency determines
worst-case response time. Name each Seq# in the chain. Distinguish parallel or cached
paths that do NOT count toward the critical-path total. Compute critical-path p50 and
p99 by summing per-boundary values from Step 3.

SUM CLOSURE GATE: if the per-boundary sum for the critical path differs from the stated
total by more than 10%, reconcile before proceeding.

DISQUALIFIER: No specific Seq# chain named fails C-10. Total not derivable from rows
fails C-12.

## Step 5 -- Threat Class Catalog

Construct a threat class catalog table:

| Row# | Threat Class | Boundary Seq# (all applicable) | Adv? |

Rules:
- Minimum 5 rows; minimum 4 distinct threat classes
- **Boundary Seq# (all applicable)**: list EVERY Seq# where this threat class manifests
- **Adv?**: exactly one row marked Y; all others N

DISQUALIFIER: Fewer than 4 threat classes fails C-13. Single Seq# for multi-boundary
threat fails C-15. Zero or multiple Y values fails C-19.

---

ANTI-PATTERN: One Seq# per threat row. Real threats manifest at multiple boundaries.

---

## Step 6 -- Exhaustiveness Gate (REQUIRED BEFORE STEP 7)

For every row in the threat catalog from Step 5, produce a checklist entry:
- Row#: [number]
- Threat: [name]
- Seq# checked against Step 2 inventory: [list]
- Any additions to Seq# list: [additions, or "none"]
- Adv?: [Y or N, matching Step 5]

Then produce the gate summary: "N rows reviewed against Step 2 inventory, X Seq#
additions made." N and X must be exact integers.

DISQUALIFIER: Missing integer counts fails C-20. Missing Adv? per row fails C-21.
Bare "confirmed" without naming rows fails C-18.

## Step 7 -- Adversarial Path Comparison

Before writing the adversarial trace, produce a mandatory cross-reference block:

| Field | Value |
|-------|-------|
| Catalog row# | [from Step 5] |
| Threat class | [exact name from Step 5] |
| All catalog Seq# for this row | [from Step 5] |
| Selected divergence Seq# | [where the adversarial path diverges] |

Then write the adversarial trace: starting from entry point, walk the path and name the
specific Seq# where the adversarial condition causes divergence. Show the post-divergence
path and concrete outcome.

REQUIRED: At the exact boundary where divergence occurs, include inline:
"-> Rem#[X] applies" citing the applicable Remediation Register entry. This citation must
appear at the divergence boundary, not in a trailing summary.

DISQUALIFIER: No cross-reference block fails C-16. No inline Rem# at divergence boundary
fails C-23.

---

ANTI-PATTERN: Inventing an adversarial scenario not grounded in the threat catalog.

---

## Step 8 -- Authorization Re-Walk Audit

### Step 8a -- Scope Enumeration Table (REQUIRED BEFORE RE-WALK FINDINGS)

Produce a scope enumeration table covering every boundary from Step 2:

| Seq# | Boundary | Scope/Role Invoked | Required Scope/Role | Verified? | Gap? |

Rules:
- **Scope/Role Invoked**: the exact scope string or role identity actually presented
  (from Step 0 vocabulary and Step 3 Auth Check)
- **Required Scope/Role**: the minimum scope or role the platform requires for the
  operation at this boundary. Name it. Do not leave blank.
- **Verified?**: Y if the traversal confirms the check occurs at runtime; N if assumed
  from upstream validation
- **Gap?**: Y if Invoked does not cover Required, or if Verified? = N at a boundary where
  downstream operations depend on this check; N otherwise

A row where Required Scope/Role = blank and Gap? = N is a disallowed shortcut. Every
boundary must name a Required Scope/Role or explain why none applies.

### Step 8b -- Re-Walk Findings

Based on the Step 8a table, produce re-walk findings:
- Name at least one new gap not surfaced in Step 3 Auth Check, OR
- Explicitly certify, referencing the Step 8a table, that the three highest-risk
  boundaries are clean and state why.

DISQUALIFIER: Re-walk findings that merely restate Step 3 Auth Check without new findings
fails C-11. Step 8a table with blank Required Scope/Role cells (without explanation)
renders the re-walk structurally incomplete, failing C-25.

---

ANTI-PATTERN: A copy of the Step 3 Auth Check column is not an audit. The scope
enumeration table makes gaps structurally visible.

---

## Step 9 -- Error Path Trace

Trace at least one full error path from its origination point to the final caller
response. Show:
- The specific Seq# where the error originates
- How the error transforms or propagates at each subsequent boundary
- Whether the error is swallowed, wrapped, or passed through at each boundary
- The final form of the error as seen by the caller

REQUIRED: At the exact boundary where the error originates, include inline:
"-> Rem#[X] applies" citing the applicable Remediation Register entry. This citation must
appear at the origination boundary, not in a trailing summary.

DISQUALIFIER: "Error returned to caller" without propagation chain fails C-06. No inline
Rem# at origination boundary fails C-23.

## Step 10 -- Batch and Edge-Case Handling

### Step 10a -- Edge-Case Table

For each batch operation, pagination scenario, or concurrent-request edge case:

| EC# | Edge Case | Boundary Seq# | Limit | Behavioral Consequence |

Each EC# is a sequential integer for use in cross-reference.

### Step 10b -- Batch-Catalog Cross-Check (advisory)

Consider producing a cross-check table mapping each edge case against each threat catalog
row (columns = TRow-1, TRow-2, ...). Marking "X" in each cell where the edge case has a
meaningful interaction with that threat class can make the relationship between batch
behavior and threat surface visible. This is suggested but not required.

### Step 10c -- Cross-Check Gate Summary (REQUIRED BEFORE STEP 11)

State the three-integer gate: "N edge cases x M catalog rows -> K interactions found."
N, M, and K must be exact integers. This gate must appear after Step 10a and before
Step 11. Per-case entries in Step 10a should cite catalog row numbers from Step 5 where
a relationship exists.

DISQUALIFIER: Gate absent or missing any one integer fails C-22. A prose assertion
("all edge cases checked") without the three-integer format fails C-22.

## Step 11 -- Remediation Register

Produce a dedicated Remediation Register as a separate table, distinct from the Step 3
traversal:

| Rem# | Failure Ref (Seq#) | Mechanism Type | Parameters |

Rules:
- Every failure point from Step 3 must have a Rem# entry
- **Mechanism Type**: name the type (retry policy, circuit breaker, permission scope
  addition, payload validation guard) -- not "add error handling"
- **Parameters**: quantify the mechanism:
  - Retry: algorithm, initial delay, multiplier, max-attempts
  - Circuit breaker: threshold, reset interval
  - Permission fix: exact scope string or role identity
  - Payload guard: specific field name and validation predicate

DISQUALIFIER: Mechanism type without parameters fails C-14. Inline remediation in
Step 3 fails C-17. "Add error handling" without mechanism type fails C-08.

---

ANTI-PATTERN: Inline annotations in Step 3 hide parameter omissions.

---

---

## V-02 -- Phrasing register: C-25 advisory

### Axis
Step 8a scope enumeration table (Seq#, Boundary, Scope/Role Invoked, Required Scope/Role,
Verified?, Gap?) softened from required to advisory. The Step 8b re-walk findings remain
required (C-11 still enforced). All R8 V-05 requirements preserved for C-01 through C-24.

### Hypothesis
Removing the required scope enumeration table from Step 8 while retaining the re-walk
findings requirement causes C-25 FAIL (re-walk exists, no preceding table) while all
other criteria including C-11 and C-24 hold. Predicted: 175/180 (-5 C-25).

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

---

ANTI-PATTERN: Declaring a role without committing vocabulary. The vocabulary commitment
is the binding contract that makes C-03, C-04, and C-14 specific.

---

## Step 1 -- Entry Point Declaration

State the precise entry point: the API verb, endpoint path, caller identity, credential
type (from Step 0), and ambient context (tenant, environment, region).

DISQUALIFIER: Missing credential type and endpoint path fails C-01.

---

ANTI-PATTERN: "A POST with a JSON body from an authenticated user" hides credential
scope, endpoint version, and ambient context.

---

## Step 2 -- Boundary Inventory (GATE)

List every service boundary in traversal order. Include: API gateway, authentication
service, routing layer, each platform service, each storage system, async queues, cache
layers, and the response assembly path.

GATE: Step 3 must contain a row for every boundary listed here.

DISQUALIFIER: Omitting token validation, plugin pipelines, async queues, or cache layers
fails C-02.

---

ANTI-PATTERN: Listing only the primary service and the database.

---

## Step 3 -- Traversal Table

| Seq# | Boundary | Operation | Failure Point | Auth Check | p50 (ms) | p99 (ms) |

- **Failure Point**: specific mechanism (not "may fail")
- **Auth Check**: specific scope string or [AUTH GAP]
- **p50/p99**: ms; sub-5ms = "< 5ms -- [reason]"

DISQUALIFIER: "may fail" or blank Failure Point fails C-03. "Valid token" without scope
string fails C-04. "fast" or blank latency fails C-05.

---

ANTI-PATTERN: "may timeout" without threshold and error code.
ANTI-PATTERN: "valid token" -- this hides a gap as a confirmation.

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

Mandatory cross-reference block before the trace:

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

Perform a dedicated second-pass authorization audit over the full boundary list from
Step 2, focused on privilege escalation paths, missing scope validations, and
assumed-but-unverified auth.

Before writing findings, consider producing a per-boundary scope summary. Listing the
scope invoked, the required scope, and whether the check is verified at runtime can
help surface gaps that narrative re-walk may miss. [NOTE: This summary is advisory.]

The re-walk must either:
(a) Name at least one new gap not surfaced in Step 3 Auth Check, OR
(b) Explicitly certify, per the three highest-risk boundaries, that scope and role
    checks are clean.

DISQUALIFIER: Re-walk that merely restates Step 3 Auth Check without new findings
fails C-11.

---

ANTI-PATTERN: A copy of the Step 3 Auth Check column is not an audit. Active
interrogation -- asking whether each boundary's check is sufficient, not just whether
one exists -- is required.

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

Produce a cross-check table mapping every edge case (EC# rows) against every threat
catalog row (TRow# columns). Mark "X" in each cell where the edge case has a meaningful
interaction with that threat class. Leave blank if no interaction.

| EC# | TRow-1 | TRow-2 | TRow-3 | TRow-4 | TRow-5 | ... |

The table must include a column for every Row# from Step 5 and a row for every EC#
from Step 10a.

### Step 10c -- Cross-Check Gate Summary (REQUIRED BEFORE STEP 11)

Derive the three-integer gate summary directly from the Step 10b table:
- N = count of EC# rows in the table (must equal count of rows in Step 10a)
- M = count of TRow columns (must equal count of rows in Step 5)
- K = count of "X" cells in the cross-check table

State: "N edge cases x M catalog rows -> K interactions found."

DISQUALIFIER: Gate absent or missing any integer fails C-22. Gate integers not derivable
by counting Step 10b table cells fails C-24.

---

ANTI-PATTERN: Prose cross-check without a backing table. Prose K cannot be cell-verified.

---

## Step 11 -- Remediation Register

| Rem# | Failure Ref (Seq#) | Mechanism Type | Parameters |

Every failure point from Step 3 must have a Rem# entry. Mechanism Type must name the
type. Parameters must be quantified:
- Retry: algorithm, initial delay, multiplier, max-attempts
- Circuit breaker: threshold, reset interval
- Permission fix: exact scope string or role identity
- Payload guard: specific field name and validation predicate

DISQUALIFIER: Mechanism type without parameters fails C-14. Inline remediation fails
C-17. "Add error handling" without mechanism type fails C-08.

---

ANTI-PATTERN: Inline annotations in Step 3 hide parameter omissions.

---

---

## V-03 -- Lifecycle emphasis: scope-gap Rem# propagation (ES-3)

### Axis
Step 8b re-walk findings augmented with a required cross-link: every Gap? = Y row in
the Step 8a scope enumeration table must be cited as a dedicated Rem# entry in Step 11
with the exact scope string or role name as the Parameters value of a Permission Fix
mechanism. This closes the Step 8a -> Step 11 loop for scope gaps.

### Hypothesis
Requiring scope-gap Rem# propagation surfaces a C-26 candidate: scope-gap entries in
the scope enumeration table are traceable to specific Rem# entries in the Remediation
Register with exact scope parameters. A response can complete Step 8a with Gap? = Y
entries and complete Step 11 with remediation items and still fail this criterion if
the scope gaps are not individually cited as Rem# entries with exact scope strings. The
three-way link Step 8a -> Step 11 -> Step 7/9 is the testable condition.

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

---

ANTI-PATTERN: Declaring a role without committing vocabulary. The vocabulary commitment
is the binding contract that makes C-03, C-04, and C-14 specific.

---

## Step 1 -- Entry Point Declaration

State the precise entry point: the API verb, endpoint path, caller identity, credential
type (from Step 0), and ambient context (tenant, environment, region).

DISQUALIFIER: Missing credential type and endpoint path fails C-01.

---

ANTI-PATTERN: "A POST with a JSON body from an authenticated user" hides credential
scope, endpoint version, and ambient context.

---

## Step 2 -- Boundary Inventory (GATE)

List every service boundary in traversal order. Include: API gateway, authentication
service, routing layer, each platform service, each storage system, async queues, cache
layers, and the response assembly path.

GATE: Step 3 must contain a row for every boundary listed here.

DISQUALIFIER: Omitting token validation, plugin pipelines, async queues, or cache layers
fails C-02.

---

ANTI-PATTERN: Listing only the primary service and the database.

---

## Step 3 -- Traversal Table

| Seq# | Boundary | Operation | Failure Point | Auth Check | p50 (ms) | p99 (ms) |

- **Failure Point**: specific mechanism (not "may fail")
- **Auth Check**: specific scope string or [AUTH GAP]
- **p50/p99**: ms; sub-5ms = "< 5ms -- [reason]"

DISQUALIFIER: "may fail" or blank Failure Point fails C-03. "Valid token" without scope
string fails C-04. "fast" or blank latency fails C-05.

---

ANTI-PATTERN: "may timeout" without threshold and error code.
ANTI-PATTERN: "valid token" -- this hides a gap as a confirmation.

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

Mandatory cross-reference block before the trace:

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

Produce a scope enumeration table covering every boundary from Step 2:

| Seq# | Boundary | Scope/Role Invoked | Required Scope/Role | Verified? | Gap? |

Rules:
- **Scope/Role Invoked**: exact scope string or role identity from Step 0 vocabulary
  and Step 3 Auth Check
- **Required Scope/Role**: the minimum the platform requires at this boundary. Name it.
- **Verified?**: Y if the check occurs at runtime; N if assumed from upstream validation
- **Gap?**: Y if Invoked does not cover Required, or Verified? = N at a dependent
  boundary; N otherwise

Every boundary must have a named Required Scope/Role. Blank = disallowed shortcut.

### Step 8b -- Re-Walk Findings

Based on the Step 8a table:
- Name at least one new gap not in Step 3 Auth Check, OR
- Certify, referencing the Step 8a Gap? column, that the three highest-risk boundaries
  are clean and state why.

SCOPE-GAP REM# REQUIREMENT (REQUIRED): For every row in Step 8a where Gap? = Y, cite
the specific Rem# from Step 11 that addresses this gap. The citation must appear in the
Step 8b findings section:
  "Seq# [N] Gap? = Y -> addressed by Rem#[X] (scope: [exact scope string])"
The corresponding Step 11 entry must have:
  - Mechanism Type: Permission Fix (or Scope Elevation)
  - Parameters: the exact scope string or role name that closes the gap

DISQUALIFIER: Re-walk findings that merely restate Step 3 Auth Check fails C-11. Blank
Required Scope/Role cells without explanation fails C-25. Gap? = Y rows without a cited
Rem# in Step 8b findings, or without a corresponding Step 11 entry with exact scope
parameters, is a disallowed omission (C-26 candidate signal).

---

ANTI-PATTERN: A re-walk that identifies scope gaps without tracing them to a remediation
entry with an exact scope string parameter. A gap without a Rem# citation is half an
audit -- it names the problem but does not commit to the fix.

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

Mark "X" where the edge case has a meaningful interaction with that threat class. Every
Row# from Step 5 must appear as a column. Every EC# from Step 10a must appear as a row.

### Step 10c -- Cross-Check Gate Summary (REQUIRED BEFORE STEP 11)

Derive from the Step 10b table:
- N = count of EC# rows (must equal count in Step 10a)
- M = count of TRow columns (must equal count in Step 5)
- K = count of "X" cells

State: "N edge cases x M catalog rows -> K interactions found."

DISQUALIFIER: Gate absent or missing any integer fails C-22. Gate integers not derivable
from table cells fails C-24.

---

ANTI-PATTERN: Prose cross-check without a backing table.

---

## Step 11 -- Remediation Register

| Rem# | Failure Ref (Seq#) | Mechanism Type | Parameters |

Every failure point from Step 3 must have a Rem# entry. Mechanism Type names the type.
Parameters are quantified:
- Retry: algorithm, initial delay, multiplier, max-attempts
- Circuit breaker: threshold, reset interval
- Permission fix: exact scope string or role identity
- Payload guard: specific field name and validation predicate

SCOPE-GAP ENTRIES: Every scope gap identified in Step 8a (Gap? = Y) must have a
dedicated Rem# entry in this Register. The Parameters cell of that entry must contain
the exact scope string or role name that closes the gap -- the same string cited in
Step 8b findings. A scope-gap entry that names a mechanism type but does not specify
the exact scope string in Parameters is incomplete.

DISQUALIFIER: Mechanism type without parameters fails C-14. Inline remediation fails
C-17. "Add error handling" without mechanism type fails C-08. Scope-gap Rem# entry
without exact scope string parameter is the C-26 target: treat as a gap signal.

---

ANTI-PATTERN: Inline annotations in Step 3 hide parameter omissions.
ANTI-PATTERN: A scope-gap Rem# entry that says "add missing scope" without naming the
exact scope string. The exact string (e.g., "user_impersonation" or "prvWriteContact")
is the testable parameter.

---

---

## V-04 -- Output format: Step 0 vocabulary conformance gate

### Axis
A new Step 3a is added after the traversal table and before the critical path: a
vocabulary conformance gate that lists every term committed in Step 0, cites the Step 3
cell(s) where each term appears verbatim, flags any Step 3 cell using a generic substitute
instead of the committed term, and produces an integer conformance summary.

### Hypothesis
Requiring a structured vocabulary conformance gate surfaces a C-26 candidate: vocabulary
conformance -- Step 0 committed terms verifiably propagate to Step 3 cells, with any
generic deviation structurally flagged. A response can declare rich vocabulary in Step 0
and still use generic terms in Step 3 (e.g., "valid token" instead of the committed scope
string); the conformance gate makes this drift structurally visible as a binary integer
(deviation count = 0 or > 0).

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

Assign a VT# (vocabulary term number) to each committed term. Example:
- VT-1: [auth mechanism name with exact scope string]
- VT-2: [primary boundary name as platform names it]
- VT-3: [failure mode vocabulary with specific HTTP code]
- VT-4: [permission model term with specific privilege name]

---

ANTI-PATTERN: Declaring a role without committing vocabulary. The VT# assignment is the
binding contract that makes the Step 3a conformance gate computable.

---

## Step 1 -- Entry Point Declaration

State the precise entry point: API verb, endpoint path, caller identity, credential type
(from Step 0 VT terms), and ambient context.

DISQUALIFIER: Missing credential type and endpoint path fails C-01.

---

ANTI-PATTERN: "A POST with a JSON body from an authenticated user" hides credential
scope, endpoint version, ambient context.

---

## Step 2 -- Boundary Inventory (GATE)

List every service boundary in traversal order. Use the VT# boundary names committed
in Step 0. Include: API gateway, authentication service, routing layer, each platform
service, each storage system, async queues, cache layers, and response assembly path.

GATE: Step 3 must contain a row for every boundary listed here.

DISQUALIFIER: Omitting token validation, plugin pipelines, async queues, or cache layers
fails C-02.

---

ANTI-PATTERN: Listing only the primary service and the database.

---

## Step 3 -- Traversal Table

| Seq# | Boundary | Operation | Failure Point | Auth Check | p50 (ms) | p99 (ms) |

For every cell in the Failure Point and Auth Check columns, use only terms committed
in Step 0. Do not introduce generic substitutes.

- **Failure Point**: specific mechanism from Step 0 failure vocabulary (not "may fail")
- **Auth Check**: specific scope string from Step 0 auth vocabulary or [AUTH GAP]
- **p50/p99**: ms; sub-5ms = "< 5ms -- [reason]"

DISQUALIFIER: "may fail" or blank Failure Point fails C-03. "Valid token" without scope
string fails C-04. "fast" or blank latency fails C-05.

---

ANTI-PATTERN: "may timeout" without the Step 0 failure code.
ANTI-PATTERN: "valid token" -- if Step 0 committed a specific scope string, that string
must appear in every Auth Check cell, not a generic substitute.

---

## Step 3a -- Vocabulary Conformance Gate (REQUIRED BEFORE STEP 4)

Produce a vocabulary conformance table checking every Step 0 committed term against its
Step 3 usage:

| VT# | Term Committed in Step 0 | Step 3 Cells Where Term Appears | Generic Substitute Found? |

Rules:
- **Step 3 Cells Where Term Appears**: list the Seq# and column (e.g., "Seq-3 Auth Check,
  Seq-7 Auth Check") where the exact committed term appears verbatim in Step 3
- **Generic Substitute Found?**: Y if any Step 3 cell in that term's category uses a
  generic form instead of the committed term; N otherwise

After completing the per-term table, produce the conformance gate summary:
"V terms committed, V terms confirmed in Step 3, D deviations found."
V (confirmed), and D (deviations) must be exact integers.

DISQUALIFIER: A vocabulary declaration without a corresponding conformance gate is a
partial commitment. D must be 0 for the gate to be satisfied. D > 0 is a structural
gap: any deviation found in Step 3 must be resolved before proceeding.

If D > 0: return to Step 3 and replace generic terms with the committed terms before
producing Step 3a gate summary.

---

ANTI-PATTERN: Completing the conformance gate with D > 0 and proceeding anyway.
The conformance gate is a correction checkpoint, not a documentation checkpoint.

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

Per-row checklist (Row#, Threat, Seq# checked, additions, Adv? Y/N). Gate summary:
"N rows reviewed against Step 2 inventory, X Seq# additions made." N and X exact integers.

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

Adversarial trace. REQUIRED: Inline at divergence boundary: "-> Rem#[X] applies."

DISQUALIFIER: No cross-reference block fails C-16. No inline Rem# fails C-23.

---

ANTI-PATTERN: Ad-hoc adversarial scenario not grounded in the threat catalog.

---

## Step 8 -- Authorization Re-Walk Audit

### Step 8a -- Scope Enumeration Table (REQUIRED BEFORE RE-WALK FINDINGS)

| Seq# | Boundary | Scope/Role Invoked | Required Scope/Role | Verified? | Gap? |

Every boundary must have a named Required Scope/Role. Blank = disallowed shortcut.
Use VT# terms from Step 0 for Scope/Role Invoked cells.

### Step 8b -- Re-Walk Findings

Name at least one new gap OR certify the three highest-risk boundaries are clean.

DISQUALIFIER: Restating Step 3 Auth Check fails C-11. Blank Required Scope/Role fails
C-25.

---

ANTI-PATTERN: A copy of the Step 3 Auth Check column is not an audit.

---

## Step 9 -- Error Path Trace

Trace one full error path: origination Seq#, propagation, swallowed/wrapped/passed
through, final caller-visible form.

REQUIRED: Inline at origination boundary: "-> Rem#[X] applies."

DISQUALIFIER: "Error returned to caller" without propagation chain fails C-06. No
inline Rem# fails C-23.

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
- Permission fix: exact scope string or role identity (using VT# terms from Step 0)
- Payload guard: specific field name and validation predicate

DISQUALIFIER: Mechanism type without parameters fails C-14. Inline remediation fails
C-17. "Add error handling" without mechanism type fails C-08.

---

ANTI-PATTERN: Inline annotations in Step 3.

---

---

## V-05 -- Two-axis combination: V-03 scope-gap Rem# propagation + V-04 vocabulary conformance gate

### Axes
Lifecycle emphasis (V-03: scope-gap -> Step 11 Rem# citation with exact scope parameter)
PLUS output format (V-04: Step 3a vocabulary conformance gate with integer summary).
All R8 V-05 requirements preserved for C-01 through C-25.

### Hypothesis
Both axes together produce 180/180 and surface two independent C-26 candidates:
(A) scope-gap Rem# propagation -- every Gap?=Y row in Step 8a is traceable to a
dedicated Rem# entry in Step 11 with exact scope string parameter; the three-way
cross-link Step 8a -> Step 11 -> (Step 7/9 Rem# citation) is fully computable;
(B) vocabulary conformance gate -- Step 0 committed terms (VT# assigned) are verifiably
present in Step 3 cells with a structured conformance table and a D=0 gate summary.
A response achieving both new structural properties while maintaining all C-01-C-25
requirements establishes the design surface for v9.

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
- VT-2: [primary boundary name]
- VT-3: [failure mode vocabulary with HTTP code]
- VT-4: [permission model term with specific privilege name]

---

ANTI-PATTERN: Declaring a role without committing vocabulary. The VT# assignment makes
the Step 3a vocabulary conformance gate computable.

---

## Step 1 -- Entry Point Declaration

State the precise entry point: API verb, endpoint path, caller identity, credential type
(from Step 0 VT terms), and ambient context.

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

ANTI-PATTERN: "may timeout" without the Step 0 failure code.
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
before continuing.

DISQUALIFIER: Gate absent fails the conformance check (C-26 target). D > 0 without
correcting Step 3 is a disallowed omission.

---

ANTI-PATTERN: Declaring vocabulary at Step 0 and allowing generic substitutes in Step 3.
The conformance gate is a correction checkpoint: D > 0 means return and fix, not proceed
and note.

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

Adversarial trace. REQUIRED: Inline at divergence boundary: "-> Rem#[X] applies."

DISQUALIFIER: No cross-reference block fails C-16. No inline Rem# fails C-23.

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

### Step 8b -- Re-Walk Findings

Based on the Step 8a table:
- Name at least one new gap not in Step 3 Auth Check, OR
- Certify the three highest-risk boundaries are clean.

SCOPE-GAP REM# REQUIREMENT (REQUIRED): For every row where Gap? = Y, cite the specific
Rem# from Step 11 that addresses this gap:
  "Seq# [N] Gap? = Y -> addressed by Rem#[X] (scope: [exact VT# scope string])"

The corresponding Step 11 Rem# entry must have:
  - Mechanism Type: Permission Fix
  - Parameters: the exact scope string or role name that closes the gap (same as VT#)

DISQUALIFIER: Re-walk that merely restates Step 3 fails C-11. Blank Required Scope/Role
fails C-25. Gap? = Y rows without cited Rem# in Step 8b, or without a corresponding
Step 11 entry with exact scope parameter, is a C-26 target gap signal.

---

ANTI-PATTERN: A re-walk that identifies scope gaps without tracing them to a Rem# entry
with an exact scope string. A gap without a Rem# citation is half an audit.

---

## Step 9 -- Error Path Trace

Trace one full error path: origination Seq#, propagation, swallowed/wrapped/passed
through, final caller-visible form.

REQUIRED: Inline at origination boundary: "-> Rem#[X] applies."

DISQUALIFIER: "Error returned to caller" without propagation chain fails C-06. No
inline Rem# fails C-23.

## Step 10 -- Batch and Edge-Case Handling with Cross-Check Table

### Step 10a -- Edge-Case Table

| EC# | Edge Case | Boundary Seq# | Limit | Behavioral Consequence |

### Step 10b -- Batch-Catalog Cross-Check Table (REQUIRED)

| EC# | TRow-1 | TRow-2 | TRow-3 | TRow-4 | TRow-5 | ... |

Mark "X" where interaction exists. Every Row# from Step 5 = column. Every EC# = row.

### Step 10c -- Cross-Check Gate Summary (REQUIRED BEFORE STEP 11)

N = EC# row count. M = TRow# column count. K = "X" cell count.
State: "N edge cases x M catalog rows -> K interactions found."

DISQUALIFIER: Gate absent or missing any integer fails C-22. Integers not derivable from
table cells fails C-24.

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
entry without an exact scope string parameter is incomplete.

DISQUALIFIER: Mechanism type without parameters fails C-14. Inline remediation fails
C-17. "Add error handling" without mechanism type fails C-08. Scope-gap Rem# entry
without exact scope string parameter is the C-26 target: treat as a gap signal.

---

ANTI-PATTERN: Inline annotations in Step 3 hide parameter omissions.
ANTI-PATTERN: A scope-gap Rem# entry that says "add missing scope" without the exact
scope string (e.g., "user_impersonation" or "prvWriteContact"). The string is the
parameter.

---

---

## Rankings (predicted)

| Rank | Variation | Score | Gap | All Essential | New Signal |
|------|-----------|-------|-----|---------------|------------|
| 1 | V-03 (scope-gap Rem#) | 180/180 | -- | PASS | C-26a candidate: scope-gap entries traceable to Rem# with exact scope parameter |
| 1 | V-04 (vocab conformance) | 180/180 | -- | PASS | C-26b candidate: vocabulary conformance gate computable (D integer = 0 or >0) |
| 1 | V-05 (combined) | 180/180 | -- | PASS | Both C-26 candidates |
| 4 | V-01 (C-24 advisory) | 175/180 | -5 C-24 | PASS | none |
| 4 | V-02 (C-25 advisory) | 175/180 | -5 C-25 | PASS | none |

V-01 and V-02 are regression tests. If they produce the predicted -5 gaps, C-24 and
C-25 are confirmed load-bearing. If either produces a full-score response despite the
softened language, the DISQUALIFIER wording needs hardening in the rubric.

V-03, V-04, V-05 are new-surface explorations. The two candidate axes are independent:
C-26a (scope-gap Rem# propagation) extends the C-23/C-25 cross-link family;
C-26b (vocabulary conformance) extends the C-02 vocabulary binding contract.
If both manifest in V-05, they establish the two criteria for v9.

---

## Excellence Signal Candidates for R9

| Signal | Source | Testable condition | Dependency |
|--------|---------|--------------------|------------|
| ES-1: Scope-gap Rem# propagation | V-03, V-05 | Every Gap?=Y row in Step 8a cites a Rem# in Step 11 with exact scope string parameter; Step 8b findings explicitly cite the Rem# with scope string | C-25 + C-08 + C-14 |
| ES-2: Vocabulary conformance gate | V-04, V-05 | Step 3a table present; every VT# term from Step 0 cited at a Step 3 cell; D deviations integer = 0; gate summary has two exact integers | C-02 |
| ES-3: Scope-gap three-way cross-link | V-05 (speculative) | Gap?=Y row in Step 8a -> Rem# in Step 11 with scope parameter -> Rem# cited in Step 7 or Step 9 at the divergence/origination boundary | C-25 + C-23 + ES-1 |

ES-3 is speculative: it requires V-05 to produce responses where a scope gap from Step
8a propagates to Step 11 AND the resulting Rem# is also the one cited in Steps 7/9 at
a divergence or origination boundary. If achieved, it closes the three-way loop and
makes scope-gap remediation fully auditable end-to-end.

---

```json
{"round": "R9", "rubric": "v8", "scale": 180, "baseline": "R8 V-05", "axes": ["C-24 regression (V-01)", "C-25 regression (V-02)", "scope-gap Rem# propagation (V-03)", "vocab conformance gate (V-04)", "combined (V-05)"], "predicted_top": 180, "predicted_regression_gap": -5, "new_candidates": ["C-26a: scope-gap Rem# propagation", "C-26b: vocabulary conformance gate", "C-27 speculative: scope-gap three-way cross-link"]}
```
