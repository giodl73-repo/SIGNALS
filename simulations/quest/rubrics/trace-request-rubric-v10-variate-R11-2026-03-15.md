# trace-request rubric v10 -- Skill Body Prompt Variations R11
# Generated: 2026-03-15

## Overview

Five complete, runnable skill body prompt variations for the `trace-request` skill,
targeting the v10 rubric (205 pts, C-01 through C-30).

**R10 result**: V-01/V-02 regression tests confirmed C-26 and C-27 load-bearing (-5 each
as predicted). V-03 (Step 8b coherence check) produced ES-1, promoted to C-28. V-04
(Step 8c coherence audit table) produced ES-2, promoted to C-29. V-05 (combined) produced
ES-3 (dual-surface contradiction detection) promoted to C-30. Top score: 190/190 (V-03,
V-04, V-05 on v9 rubric).

**R11 baseline**: R10 V-05 body (VT# at Step 0 + Step 3a D=0 gate + Rem# three-way
cross-link + Step 8b REQUIRED coherence progression gate + Step 8c REQUIRED coherence
table + dual-surface C-30 enforcement; all C-01 through C-30).

**R11 variation surface**: Two regression tests confirm C-28 and C-29 are individually
load-bearing (V-01, V-02; C-30 falls with each since it depends on both). Three new-axis
explorations probe the C-31 design surface: explicit contradiction halt rule at Step 8c
(V-03), mandatory scope-token re-affirmation block at Step 8 entry (V-04), and combined
(V-05).

**C-31 design surface (not yet promoted)**: Automated consistency enforcement -- a
machine-readable schema or linting rule that computes Match? from Step 8b prose token set
and Step 8c cell values, producing binary pass/fail without human judgment. Requires
multi-round evidence of dual-surface divergence cases (C-30) before the predicate can be
reliably specified. V-03, V-04, V-05 probe whether structural contradiction can be made
formally enumerable.

---

## Variation Summary Table

| V | Axis | Key change from R10 V-05 baseline | C-28 | C-29 | C-30 | New signal | Predicted |
|---|------|-----------------------------------|------|------|------|------------|-----------|
| V-01 | Regression: C-28 advisory | Step 8b progression gate softened to NOTE; REQUIRED removed; no "blocks Step 9" mandate; per-boundary confirmation template removed | FAIL | PASS | FAIL | none | 195/205 |
| V-02 | Regression: C-29 advisory | Step 8c coherence table softened to advisory; REQUIRED removed; Match? binary rule relaxed to descriptive guidance | PASS | FAIL | FAIL | none | 195/205 |
| V-03 | Lifecycle emphasis: contradiction halt | Step 8c adds explicit CONTRADICTION HALT block: if Step 8b prose says coherent AND Step 8c Match? = N, halt with named error before Step 9; correction required to proceed | PASS | PASS | PASS | C-31 candidate: contradiction is a named halt type with Rem# requirement | 205/205 |
| V-04 | Role sequence: Step 8 scope-token re-affirmation | Mandatory Step 8 header re-names platform role and re-lists VT# scope tokens; Step 8b/8c cells must derive from this re-affirmation, not memory; role identity anchors VT# propagation | PASS | PASS | PASS | C-31 candidate: scope-token binding makes Match? computation platform-grounded | 205/205 |
| V-05 | Two-axis combination: V-03 + V-04 | Contradiction halt (V-03) + scope-token re-affirmation at Step 8 entry (V-04); both surfaces locked to Step 0 VT# list via Step 8 re-affirmation; halt is platform-identified | PASS | PASS | PASS | C-31 candidate: strongest structural expression; automated enforcement pre-conditions most established | 205/205 |

---

## V-01 -- Regression: C-28 advisory

### Axis
Step 8b coherence progression gate softened from mandatory to advisory NOTE. The REQUIRED
label is removed. The per-boundary confirmation template ("Coherence confirmed: [VT# string]
appears verbatim in Step 3 Auth Check (Seq# N), Step 8a Invoked (Seq# N), and Step 11
Rem#[X] Parameters") is removed. Step 9 is no longer structurally blocked by a required
gate output. C-26 Rem# cross-link requirement is preserved identically. C-29 Step 8c table
is preserved as REQUIRED. All other R10 V-05 requirements are unchanged.

### Hypothesis
Removing REQUIRED from the progression gate while keeping Step 8c table REQUIRED isolates
C-28 as load-bearing. A response will satisfy C-26 (Rem# entries exist and are cited) and
C-29 (Step 8c table present) but will lack the per-boundary prose confirmation that names
all three link arms before Step 9. C-30 also fails because it requires both C-28 and C-29
surfaces to be REQUIRED for contradiction to be format-detectable. Predicted: 195/205
(-5 C-28, -5 C-30).

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
ANTI-PATTERN: "valid token" -- the exact VT# scope string must appear in Auth Check.

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

SCOPE-GAP REM# REQUIREMENT (REQUIRED): For every row in Step 8a where Gap? = Y, cite
the specific Rem# from Step 11 that addresses this gap. The citation must appear in the
Step 8b findings section:
  "Seq# [N] Gap? = Y -> addressed by Rem#[X] (scope: [exact VT# scope string])"

The corresponding Step 11 Rem# entry must have:
  - Mechanism Type: Permission Fix
  - Parameters: the exact scope string or role name that closes the gap (same VT# term)

NOTE: For coherence, the VT# scope string in the Rem# citation above should match the
exact string appearing in the Step 3 Auth Check cell and Step 11 Parameters cell for
this boundary. Confirming this match is good practice before proceeding to Step 9.

DISQUALIFIER: Re-walk findings that merely restate Step 3 Auth Check fails C-11.
Gap? = Y rows without a cited Rem# with exact scope parameter fail C-26.

---

ANTI-PATTERN: A re-walk that identifies scope gaps without tracing them to a Rem# entry
with an exact scope string. A gap without a Rem# citation is half an audit.

---

### Step 8c -- Scope String Coherence Table (REQUIRED BEFORE STEP 9)

For every boundary where Gap? = Y in Step 8a, produce one row in the following table:

| Seq# | Step3-Auth | Step8a-Invoked | Step11-Params | Match? |

Rules:
- **Step3-Auth**: the exact scope string as written in the Step 3 Auth Check cell for
  this Seq#
- **Step8a-Invoked**: the exact scope string as written in the Step 8a Scope/Role
  Invoked cell for this Seq#
- **Step11-Params**: the exact scope string as written in the Step 11 Rem# Parameters
  cell for the Rem# cited in Step 8b for this Seq#
- **Match?**: Y if all three cell values are byte-identical; N if any differ

REQUIRED: This table must be present before Step 9 begins. Every Gap? = Y boundary
must have exactly one row. The VT# scope string committed in Step 0 must appear
verbatim as the value in each of the three cells; it may not be paraphrased.

Note: a Match? = N cell indicates a scope string inconsistency. Consider whether this
reflects a genuine inconsistency or a transcription error before proceeding.

DISQUALIFIER: Step 8c table absent or incomplete (missing a Gap? = Y row) fails C-29.
Table present but Match? column is non-binary (not Y or N) fails C-29. Table positioned
after Step 9 rather than before fails C-29.

---

ANTI-PATTERN: Omitting Step 8c because the Step 8b prose already described the coherence.
The table is a separate required output. Prose in Step 8b and the Step 8c table are two
distinct surfaces. Both are required.

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
string that closes the gap -- the same VT# term cited in Step 8b findings. The string
must be byte-identical to the value in the Step 8c Step11-Params cell for this Seq#.

DISQUALIFIER: Mechanism type without parameters fails C-14. Inline remediation fails
C-17. "Add error handling" without mechanism type fails C-08. Scope-gap Rem# entry
without exact scope string parameter fails C-26.

---

ANTI-PATTERN: Inline annotations in Step 3 hide parameter omissions.
ANTI-PATTERN: "Add missing scope" without naming the exact VT# scope string.

---

---

## V-02 -- Regression: C-29 advisory

### Axis
Step 8c coherence table softened from mandatory to advisory. The REQUIRED label is
removed. The binary Match? column rule is relaxed to descriptive guidance ("you may
note whether the strings appear consistent"). The "must be present before Step 9 begins"
gate is removed. Step 8b REQUIRED coherence progression gate is preserved exactly as in
R10 V-05, including the per-boundary "Coherence confirmed: [VT# string]" statement with
all three link arms named and REQUIRED before Step 9. All other R10 V-05 requirements
are unchanged.

### Hypothesis
Removing REQUIRED from Step 8c while keeping Step 8b REQUIRED isolates C-29 as
load-bearing. A response will satisfy C-26 (Rem# entries cited) and C-28 (per-boundary
prose confirmation present and naming all three link arms) but will lack the separate
tabular surface required for C-29. C-30 also fails because it requires both surfaces
to be REQUIRED. Predicted: 195/205 (-5 C-29, -5 C-30).

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
ANTI-PATTERN: "valid token" -- the exact VT# scope string must appear in Auth Check.

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
- **Verified?**: Y if check occurs at runtime; N if assumed from upstream validation
- **Gap?**: Y if Invoked does not cover Required, or Verified? = N at a dependent
  boundary; N otherwise

Every boundary must have a named Required Scope/Role. Blank = disallowed shortcut.

DISQUALIFIER: Scope enumeration table absent fails C-25. Blank Required Scope/Role
without explanation fails C-25.

### Step 8b -- Re-Walk Findings (REQUIRED PROGRESSION GATE BEFORE STEP 9)

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

COHERENCE PROGRESSION GATE (REQUIRED BEFORE STEP 9): For every Gap? = Y row cited
above, confirm explicitly that the exact VT# scope string is byte-identical across all
three structures. Use this form for each boundary:

  "Coherence confirmed: [VT# scope string] appears verbatim in:
   - Step 3 Auth Check (Seq# [N]): [exact string as written in Step 3]
   - Step 8a Scope/Role Invoked (Seq# [N]): [exact string as written in Step 8a]
   - Step 11 Rem#[X] Parameters: [exact string as written in Step 11]"

One confirmation per Gap? = Y boundary is REQUIRED. This block must appear in Step 8b
before Step 9 begins. Step 9 may not start until all Gap? = Y boundaries have a
confirmation statement.

DISQUALIFIER: Re-walk findings that merely restate Step 3 Auth Check fails C-11.
Gap? = Y rows without a cited Rem# fail C-26. Coherence progression gate absent or
with any Gap? = Y boundary unconfirmed fails C-28.

---

ANTI-PATTERN: A re-walk that cites Rem# entries but never produces the explicit per-
boundary coherence confirmation naming all three structures. Rem# cited (C-26 PASS) with
coherence gate absent (C-28 FAIL) is a predictable failure mode.

---

### Step 8c -- Scope String Coherence Table (optional check)

After producing the Step 8b coherence gate output, you may optionally tabulate the three-
way scope string comparison in a structured table for reference:

| Seq# | Step3-Auth | Step8a-Invoked | Step11-Params | Match? |

If you produce this table, Match? should indicate whether all three cell values are
identical (Y) or differ (N). This table supplements the Step 8b prose gate but does not
replace it.

[This section is advisory. The table is not required. Step 9 may proceed once the
Step 8b coherence gate confirms all Gap? = Y boundaries.]

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
string that closes the gap -- the same VT# term cited in Step 8b findings and confirmed
in the Step 8b coherence gate.

DISQUALIFIER: Mechanism type without parameters fails C-14. Inline remediation fails
C-17. "Add error handling" without mechanism type fails C-08. Scope-gap Rem# entry
without exact scope string parameter fails C-26.

---

ANTI-PATTERN: Inline annotations in Step 3 hide parameter omissions.
ANTI-PATTERN: "Add missing scope" without naming the exact VT# scope string.

---

---

## V-03 -- Lifecycle emphasis: contradiction halt

### Axis
Step 8c augmented with an explicit CONTRADICTION HALT block. In V-01/V-02 baseline, a
Match? = N cell in Step 8c is possible without a defined consequence. V-03 adds a
required post-table rule: if Step 8b prose confirms coherent for a boundary (produced
a "Coherence confirmed" statement) AND the corresponding Step 8c Match? cell for that
boundary = N, this is a STRUCTURAL CONTRADICTION and must be named, halted, and resolved
before Step 9. The halt is not advisory -- it is a DISQUALIFIER for proceeding. The
contradiction must produce a named Rem# correction entry before the trace may continue.

### Hypothesis
The contradiction halt makes the C-30 dual-surface divergence signal formally enumerable
as a named error type rather than an implicit detection. A response that produces both
Step 8b coherence confirmation and Step 8c Match? = N for the same boundary cannot
silently proceed. The halt produces a Rem# entry specifically scoped to "scope string
inconsistency between prose gate and coherence table" -- the C-31 candidate. Predicted:
205/205 + C-31 surface signal.

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
ANTI-PATTERN: "valid token" -- the exact VT# scope string must appear in Auth Check.

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
- **Verified?**: Y if check occurs at runtime; N if assumed from upstream validation
- **Gap?**: Y if Invoked does not cover Required, or Verified? = N at a dependent
  boundary; N otherwise

Every boundary must have a named Required Scope/Role. Blank = disallowed shortcut.

DISQUALIFIER: Scope enumeration table absent fails C-25. Blank Required Scope/Role
without explanation fails C-25.

### Step 8b -- Re-Walk Findings (REQUIRED PROGRESSION GATE BEFORE STEP 8c)

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

COHERENCE PROGRESSION GATE (REQUIRED BEFORE STEP 8c): For every Gap? = Y row cited
above, confirm explicitly that the exact VT# scope string is byte-identical across all
three structures. Use this form for each boundary:

  "Coherence confirmed: [VT# scope string] appears verbatim in:
   - Step 3 Auth Check (Seq# [N]): [exact string as written in Step 3]
   - Step 8a Scope/Role Invoked (Seq# [N]): [exact string as written in Step 8a]
   - Step 11 Rem#[X] Parameters: [exact string as written in Step 11]"

One confirmation per Gap? = Y boundary is REQUIRED. All confirmations must appear
before Step 8c begins. Step 8c will independently verify these claims in table form.

DISQUALIFIER: Re-walk findings that merely restate Step 3 Auth Check fails C-11.
Gap? = Y rows without a cited Rem# fail C-26. Coherence progression gate absent or
with any Gap? = Y boundary unconfirmed fails C-28.

---

ANTI-PATTERN: A re-walk that produces Rem# citations (C-26 PASS) and coherence prose
(C-28 PASS) but skips any boundary. Every Gap? = Y boundary must have its own line.

---

### Step 8c -- Scope String Coherence Table (REQUIRED BEFORE STEP 9)

For every boundary where Gap? = Y in Step 8a, produce one row:

| Seq# | Step3-Auth | Step8a-Invoked | Step11-Params | Match? |

Rules:
- **Step3-Auth**: exact scope string as written in Step 3 Auth Check cell for this Seq#
- **Step8a-Invoked**: exact scope string as written in Step 8a Scope/Role Invoked cell
- **Step11-Params**: exact scope string as written in the Step 11 Rem# Parameters cell
  for the Rem# cited in Step 8b for this Seq#
- **Match?**: Y if all three cell values are byte-identical; N if any differ

REQUIRED: Table must be present before Step 9. Every Gap? = Y boundary must have a row.
VT# scope strings committed in Step 0 must appear verbatim; no paraphrase permitted.

CONTRADICTION HALT (REQUIRED): After producing the table, check for any row where
Step 8b produced a "Coherence confirmed" statement AND Step 8c Match? = N. This is a
STRUCTURAL CONTRADICTION -- the prose gate and the table disagree on the same boundary.

If any such contradiction exists, you MUST:
1. Emit: "CONTRADICTION SIGNAL: Seq# [N] -- Step 8b prose asserts coherence; Step 8c
   Match? = N. These surfaces disagree. Step 9 is BLOCKED."
2. Identify which cell among Step3-Auth, Step8a-Invoked, Step11-Params differs from the
   others and why.
3. Correct the inconsistent cell (return to the source step and fix it).
4. Add a Rem# to Step 11 with Mechanism Type: "Scope String Correction" and Parameters
   identifying the cell, the incorrect value, and the correct VT# scope string.
5. Re-produce the Step 8c row with corrected values. Match? must = Y for all rows.
6. Only then may Step 9 proceed.

DISQUALIFIER: Step 8c table absent or incomplete fails C-29. Match? non-binary fails
C-29. Contradiction detected (Step 8b says coherent, Match? = N) but trace proceeds to
Step 9 without a CONTRADICTION SIGNAL and Rem# correction fails C-30.

---

ANTI-PATTERN: Producing a Match? = N cell and proceeding to Step 9 without a named
CONTRADICTION SIGNAL. The divergence between prose gate and table is self-evidencing --
it does not require semantic reading of the scope strings to detect. A Match? = N cell
alongside a "Coherence confirmed" statement in Step 8b is by definition a structural
contradiction and must be halted.

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
- Scope String Correction: cell identity (Step#-Column), incorrect value, correct VT#
  scope string (used when a CONTRADICTION SIGNAL was raised at Step 8c)

SCOPE-GAP ENTRIES: Every scope gap identified in Step 8a (Gap? = Y) must have a
dedicated Rem# entry. The Parameters cell must contain the exact scope string that
closes the gap -- the same VT# term confirmed in Step 8b and verified as Match? = Y
in Step 8c.

DISQUALIFIER: Mechanism type without parameters fails C-14. Inline remediation fails
C-17. "Add error handling" without mechanism type fails C-08. Scope-gap Rem# entry
without exact scope string parameter fails C-26.

---

ANTI-PATTERN: A scope-gap Rem# entry that says "add missing scope" without naming the
exact VT# scope string. The string is the parameter.

---

---

## V-04 -- Role sequence: Step 8 scope-token re-affirmation

### Axis
A mandatory Step 8 header block is added before Step 8a. The header requires the
platform expert to: (1) re-name the platform role adopted in Step 0, (2) re-list the
VT# scope tokens from Step 0 that are relevant to authorization at the boundaries about
to be audited, and (3) commit that all Step 8a Scope/Role Invoked cells, Step 8b
coherence confirmations, and Step 8c table column values must derive from this
re-affirmation, not from memory. This creates a platform-grounded anchor for the VT#
propagation that Step 8b and Step 8c require. All C-28 and C-29 requirements from R10
V-05 are preserved identically. The new content is the Step 8 entry header only.

### Hypothesis
Late role re-affirmation at the Step 8 transition ensures that VT# scope strings are
explicitly re-confirmed at the moment of the authorization audit rather than assumed
from Step 0 memory. A model that drifts from the VT# vocabulary between Steps 0 and 8
(generic substitutes creeping back in) will be caught at the re-affirmation gate before
they appear in Step 8c cells. This makes Match? = N in Step 8c more likely to reflect
a true coherence failure rather than a notation drift. The C-31 candidate: role-grounded
scope token binding makes Match? computation independently verifiable by a machine
that holds only the Step 8 re-affirmation header and the Step 8c table. Predicted:
205/205 + C-31 surface signal.

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
ANTI-PATTERN: "valid token" -- the exact VT# scope string must appear in Auth Check.

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

### Step 8 Header -- Scope-Token Re-Affirmation (REQUIRED BEFORE STEP 8a)

Before beginning the authorization re-walk, re-affirm the platform role and the scope
token vocabulary that governs this audit. State:

1. **Platform role**: the same role declared at Step 0 (e.g., "Dataverse platform expert")
2. **Auth scope tokens under audit**: re-list each VT# scope string from Step 0 that
   applies to authorization checks at service boundaries. Use the exact form committed
   in Step 0 -- same string, same casing, same delimiters.
3. **Binding commitment**: "All Scope/Role Invoked cells in Step 8a, all scope string
   citations in Step 8b, and all Step3-Auth / Step8a-Invoked / Step11-Params column
   values in Step 8c derive exclusively from the VT# tokens listed above. No paraphrase,
   abbreviation, or generic substitute is permitted in any Step 8 output."

REQUIRED: This header must appear before Step 8a. Its VT# token list is the reference
set against which the Step 8c Match? column is computed. A reviewer holding only this
header and the Step 8c table can verify coherence without reading Steps 3 or 11.

DISQUALIFIER: Step 8 header absent or missing VT# token re-list fails the C-31 surface
target. All Step 8 sub-step requirements (C-25 through C-30) depend on this header as
the scope token reference.

---

ANTI-PATTERN: Beginning Step 8a without a re-affirmation of which scope token vocabulary
is being audited. The header makes the audit self-contained -- a downstream reviewer
does not need to re-read Step 0 to know what "correct" looks like for the Match? column.

---

### Step 8a -- Scope Enumeration Table (REQUIRED)

| Seq# | Boundary | Scope/Role Invoked | Required Scope/Role | Verified? | Gap? |

Rules:
- **Scope/Role Invoked**: must be one of the VT# scope tokens listed in the Step 8
  Header. No value outside that set is permitted.
- **Required Scope/Role**: the minimum the platform requires; name it using VT# terms
- **Verified?**: Y if check occurs at runtime; N if assumed from upstream validation
- **Gap?**: Y if Invoked does not cover Required, or Verified? = N at a dependent
  boundary; N otherwise

Every boundary must have a named Required Scope/Role. Blank = disallowed shortcut.

DISQUALIFIER: Scope enumeration table absent fails C-25. Blank Required Scope/Role
without explanation fails C-25. Invoked value not in Step 8 Header VT# list fails C-25.

### Step 8b -- Re-Walk Findings (REQUIRED PROGRESSION GATE BEFORE STEP 8c)

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

COHERENCE PROGRESSION GATE (REQUIRED BEFORE STEP 8c): For every Gap? = Y row cited
above, confirm explicitly that the exact VT# scope string is byte-identical across all
three structures. Use this form for each boundary:

  "Coherence confirmed: [VT# scope string from Step 8 Header] appears verbatim in:
   - Step 3 Auth Check (Seq# [N]): [exact string as written in Step 3]
   - Step 8a Scope/Role Invoked (Seq# [N]): [exact string as written in Step 8a]
   - Step 11 Rem#[X] Parameters: [exact string as written in Step 11]"

One confirmation per Gap? = Y boundary is REQUIRED. All confirmations must appear
before Step 8c begins. The VT# scope string cited in each confirmation must appear
verbatim in the Step 8 Header re-affirmation list.

DISQUALIFIER: Re-walk findings that merely restate Step 3 Auth Check fails C-11.
Gap? = Y rows without a cited Rem# fail C-26. Coherence gate absent or incomplete
fails C-28. Scope string not present in Step 8 Header list fails C-28.

---

ANTI-PATTERN: A coherence confirmation that uses a scope string not in the Step 8
Header re-affirmation list. The header is the reference; any string that appears in
Step 8b but not in the header is a vocabulary drift.

---

### Step 8c -- Scope String Coherence Table (REQUIRED BEFORE STEP 9)

For every boundary where Gap? = Y in Step 8a, produce one row:

| Seq# | Step3-Auth | Step8a-Invoked | Step11-Params | Match? |

Rules:
- **Step3-Auth**: exact scope string as written in Step 3 Auth Check cell for this Seq#
- **Step8a-Invoked**: exact scope string as written in Step 8a Scope/Role Invoked cell
- **Step11-Params**: exact scope string as written in the Step 11 Rem# Parameters cell
- **Match?**: Y if all three cell values are byte-identical AND each equals a VT# token
  in the Step 8 Header re-affirmation list; N otherwise

REQUIRED: Table must be present before Step 9. Every Gap? = Y boundary must have a row.
A reviewer holding only the Step 8 Header and this table can verify Match? = Y for each
row without reading any other section of the trace.

DISQUALIFIER: Step 8c table absent or incomplete fails C-29. Match? non-binary fails
C-29. Any cell value not present in the Step 8 Header VT# list fails C-29. Table
positioned after Step 9 fails C-29. A Match? = N row alongside a Step 8b "Coherence
confirmed" statement for the same Seq# without correction fails C-30.

---

ANTI-PATTERN: Populating Step 8c cells with scope strings that were never listed in
the Step 8 Header re-affirmation. The header is the reference set. Any mismatch between
header values and Step 8c cell values is a scope-token drift, not a boundary gap.

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
- Permission fix: exact scope string or role identity (must be a VT# term from Step 0
  and present in Step 8 Header re-affirmation list)
- Payload guard: specific field name and validation predicate

SCOPE-GAP ENTRIES: Every scope gap identified in Step 8a (Gap? = Y) must have a
dedicated Rem# entry. The Parameters cell must contain the exact scope string -- the
same VT# term present in the Step 8 Header list, confirmed in Step 8b, and verified
as Match? = Y in Step 8c.

DISQUALIFIER: Mechanism type without parameters fails C-14. Inline remediation fails
C-17. "Add error handling" without mechanism type fails C-08. Scope-gap Rem# entry
without exact scope string parameter fails C-26.

---

ANTI-PATTERN: A scope-gap Rem# entry that says "add missing scope" without naming the
exact VT# scope string from the Step 8 Header. The string is the parameter.

---

---

## V-05 -- Two-axis combination: contradiction halt + scope-token re-affirmation

### Axis
Combines V-03 (explicit CONTRADICTION HALT at Step 8c) and V-04 (mandatory Step 8
scope-token re-affirmation header). The re-affirmation header makes Match? = Y
independently verifiable from the header alone (V-04 signal). The contradiction halt
rule names any prose/table divergence as a typed error requiring a Rem# correction
entry before Step 9 (V-03 signal). Together they establish the pre-conditions for C-31:
an automated consistency enforcement rule could compute Match? from the Step 8 Header
token list and the Step 8c cell values, and could detect any "Coherence confirmed" /
Match? = N divergence as a named CONTRADICTION SIGNAL error without reading prose.

### Hypothesis
Combined V-03 + V-04 is the strongest structural expression of dual-surface coherence.
The contradiction halt gives C-30 a formal error type with a required Rem# correction.
The re-affirmation header gives a machine-readable reference set for Match? computation.
Together they produce the two properties needed for C-31: (1) the reference set for
automated Match? computation is externalized into the Step 8 Header, and (2) the
contradiction event is a named halt type with a required Rem# entry format. If both
properties appear consistently across multiple rounds, the automated-check predicate
can be reliably specified. Predicted: 205/205 + strongest C-31 surface signal.

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
ANTI-PATTERN: "valid token" -- the exact VT# scope string must appear in Auth Check.

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

### Step 8 Header -- Scope-Token Re-Affirmation (REQUIRED BEFORE STEP 8a)

Before beginning the authorization re-walk, re-affirm the platform role and the scope
token vocabulary that governs this audit. State:

1. **Platform role**: the same role declared at Step 0 (e.g., "Dataverse platform expert")
2. **Auth scope tokens under audit**: re-list each VT# scope string from Step 0 that
   applies to authorization checks at service boundaries. Use the exact form committed
   in Step 0 -- same string, same casing, same delimiters.
3. **Binding commitment**: "All Scope/Role Invoked cells in Step 8a, all scope string
   citations in Step 8b, and all Step3-Auth / Step8a-Invoked / Step11-Params column
   values in Step 8c derive exclusively from the VT# tokens listed above. No paraphrase,
   abbreviation, or generic substitute is permitted in any Step 8 output."

REQUIRED: This header must appear before Step 8a. Its VT# token list is the canonical
reference for Step 8c Match? computation. A reviewer holding only this header and the
Step 8c table can verify coherence without reading Steps 0, 3, or 11.

DISQUALIFIER: Step 8 header absent or missing VT# token re-list causes downstream C-29
and C-30 verification to be unanchored.

---

### Step 8a -- Scope Enumeration Table (REQUIRED)

| Seq# | Boundary | Scope/Role Invoked | Required Scope/Role | Verified? | Gap? |

Rules:
- **Scope/Role Invoked**: must be one of the VT# scope tokens listed in the Step 8
  Header. No value outside that set is permitted.
- **Required Scope/Role**: the minimum the platform requires; name it using VT# terms
- **Verified?**: Y if check occurs at runtime; N if assumed from upstream validation
- **Gap?**: Y if Invoked does not cover Required, or Verified? = N at a dependent
  boundary; N otherwise

Every boundary must have a named Required Scope/Role. Blank = disallowed shortcut.

DISQUALIFIER: Scope enumeration table absent fails C-25. Blank Required Scope/Role
without explanation fails C-25. Invoked value not in Step 8 Header VT# list fails C-25.

### Step 8b -- Re-Walk Findings (REQUIRED PROGRESSION GATE BEFORE STEP 8c)

Based on the Step 8a table:
- Name at least one new gap not in Step 3 Auth Check, OR
- Certify the three highest-risk boundaries are clean.

SCOPE-GAP REM# REQUIREMENT (REQUIRED): For every row in Step 8a where Gap? = Y, cite
the specific Rem# from Step 11 that addresses this gap. The citation must appear in the
Step 8b findings section:
  "Seq# [N] Gap? = Y -> addressed by Rem#[X] (scope: [exact VT# scope string])"

The corresponding Step 11 Rem# entry must have:
  - Mechanism Type: Permission Fix
  - Parameters: the exact scope string or role name that closes the gap (same VT# term
    present in the Step 8 Header re-affirmation list)

COHERENCE PROGRESSION GATE (REQUIRED BEFORE STEP 8c): For every Gap? = Y row cited
above, confirm explicitly that the exact VT# scope string is byte-identical across all
three structures. Use this form for each boundary:

  "Coherence confirmed: [VT# scope string from Step 8 Header] appears verbatim in:
   - Step 3 Auth Check (Seq# [N]): [exact string as written in Step 3]
   - Step 8a Scope/Role Invoked (Seq# [N]): [exact string as written in Step 8a]
   - Step 11 Rem#[X] Parameters: [exact string as written in Step 11]"

One confirmation per Gap? = Y boundary is REQUIRED. All confirmations must appear
before Step 8c begins. The VT# scope string cited in each confirmation must match
a token in the Step 8 Header re-affirmation list exactly.

DISQUALIFIER: Re-walk findings that merely restate Step 3 Auth Check fails C-11.
Gap? = Y rows without a cited Rem# fail C-26. Coherence gate absent or incomplete
fails C-28. Scope string not in Step 8 Header list fails C-28.

---

ANTI-PATTERN: A coherence confirmation that uses a scope string not listed in the Step 8
Header. The header is the reference. Any string in Step 8b but absent from the header
is a vocabulary drift that will produce Match? = N in Step 8c -- and should.

---

### Step 8c -- Scope String Coherence Table with Contradiction Halt (REQUIRED BEFORE STEP 9)

For every boundary where Gap? = Y in Step 8a, produce one row:

| Seq# | Step3-Auth | Step8a-Invoked | Step11-Params | Match? |

Rules:
- **Step3-Auth**: exact scope string as written in Step 3 Auth Check cell for this Seq#
- **Step8a-Invoked**: exact scope string as written in Step 8a Scope/Role Invoked cell
- **Step11-Params**: exact scope string as written in the Step 11 Rem# Parameters cell
  for the Rem# cited in Step 8b for this Seq#
- **Match?**: Y if all three cell values are byte-identical AND each equals a VT# token
  in the Step 8 Header re-affirmation list; N otherwise

REQUIRED: Table must be present before Step 9. Every Gap? = Y boundary must have a row.
A reviewer holding only the Step 8 Header and this table can verify Match? = Y or N for
each row without reading any other section of the trace. This is the C-31 pre-condition:
the reference set (Step 8 Header) and the comparison table (Step 8c) are co-located and
machine-checkable.

CONTRADICTION HALT (REQUIRED): After producing the table, scan for any row where Step 8b
produced a "Coherence confirmed" statement AND Match? = N for the same Seq#. This is a
STRUCTURAL CONTRADICTION -- the prose gate and the table disagree on the same boundary.

If any such contradiction exists, you MUST:
1. Emit: "CONTRADICTION SIGNAL: Seq# [N] -- Step 8b prose asserts coherence; Step 8c
   Match? = N. Step 8 Header token: [VT# string]. These surfaces disagree. Step 9 is
   BLOCKED."
2. Identify which cell (Step3-Auth, Step8a-Invoked, or Step11-Params) differs from the
   Step 8 Header token and why.
3. Correct the inconsistent cell (return to the source step and fix it).
4. Add a Rem# to Step 11 with:
   - Mechanism Type: "Scope String Correction"
   - Parameters: "Cell [Step#-Column], incorrect value: [wrong string], correct VT#
     token from Step 8 Header: [correct string]"
5. Re-produce the Step 8c row with corrected values. Match? must = Y for all rows.
6. Only then may Step 9 proceed.

If no contradiction exists (all rows Match? = Y), emit: "COHERENCE VERIFIED: [N] rows,
all Match? = Y. Step 8 Header tokens confirmed across both Step 8b prose and Step 8c
table. Step 9 may proceed."

DISQUALIFIER: Step 8c table absent or incomplete fails C-29. Match? non-binary fails
C-29. Contradiction detected (Step 8b says coherent, Match? = N) but trace proceeds to
Step 9 without CONTRADICTION SIGNAL and Rem# correction fails C-30. Coherence verified
statement absent when all rows match = minor gap (advisory, not DISQUALIFIER).

---

ANTI-PATTERN: Producing a Match? = N cell and proceeding to Step 9 without a named
CONTRADICTION SIGNAL. The divergence is structurally self-evidencing: a reviewer needs
only to find a Match? = N row and confirm a "Coherence confirmed" statement exists for
that Seq# in Step 8b -- no semantic reading of scope strings required. That structural
check is precisely the C-31 pre-condition for automated enforcement.

ANTI-PATTERN: Emitting "Coherence confirmed" for a boundary whose scope string does not
appear in the Step 8 Header. The header is the ground truth. Any confirmation that names
a string not in the header is ungrounded and should fail even before Step 8c is produced.

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
- Permission fix: exact scope string or role identity (must be a VT# term from Step 0
  and present in Step 8 Header re-affirmation list)
- Payload guard: specific field name and validation predicate
- Scope String Correction: "Cell [Step#-Column], incorrect value: [wrong string], correct
  VT# token from Step 8 Header: [correct string]" (required when CONTRADICTION SIGNAL
  was raised at Step 8c)

SCOPE-GAP ENTRIES: Every scope gap identified in Step 8a (Gap? = Y) must have a
dedicated Rem# entry. The Parameters cell must contain the exact scope string -- the
same VT# token from the Step 8 Header, confirmed in Step 8b, and verified as Match? = Y
in Step 8c.

DISQUALIFIER: Mechanism type without parameters fails C-14. Inline remediation fails
C-17. "Add error handling" without mechanism type fails C-08. Scope-gap Rem# entry
without exact scope string parameter fails C-26. CONTRADICTION SIGNAL raised at Step 8c
without a corresponding Scope String Correction Rem# entry fails C-30.

---

ANTI-PATTERN: A scope-gap Rem# entry that says "add missing scope" without naming the
exact VT# scope string from the Step 8 Header. The string is the parameter.
ANTI-PATTERN: A CONTRADICTION SIGNAL at Step 8c with no corresponding Rem# correction
entry in Step 11. Every named halt requires a traceable correction record.

---
