# trace-request rubric v11 -- Skill Body Prompt Variations R12
# Generated: 2026-03-15

## Overview

Five complete, runnable skill body prompt variations for the `trace-request` skill,
targeting the v11 rubric (220 pts, C-01 through C-33).

**R11 result**: V-01/V-02 regression tests confirmed C-28 and C-29 individually load-bearing
(-5 + -5 each as predicted). V-03 (CONTRADICTION HALT with named typed label) produced ES-1,
promoted to C-31. V-04 (Step 8 Header scope-token re-affirmation) produced ES-2, promoted to
C-32. V-05 (combined) produced ES-3 (all three C-31 pre-conditions co-present), promoted to
C-33. Top score: 205/205 (V-03, V-04, V-05 on v10 rubric).

**R12 baseline**: R11 V-05 body (VT# at Step 0 + Step 3a D=0 gate + Rem# three-way cross-link
+ Step 8b REQUIRED coherence progression gate + Step 8 Header scope-token re-affirmation +
Step 8c REQUIRED coherence table with CONTRADICTION HALT block + named `CONTRADICTION SIGNAL:
Seq# N` label + `Scope String Correction` Rem# type requirement; all C-01 through C-33).

**R12 variation surface**: Two regression tests confirm C-31 and C-32 are individually
load-bearing (V-01, V-02; C-33 falls with each since it depends on both). Three new-axis
explorations probe the C-34 design surface: structured parseable token schema at Step 8 Header
(V-03), row-level verdict token column in Step 8c (V-04), and combined (V-05).

**C-34 design surface (not yet promoted)**: Live automated checker -- a runnable tool or
schema validator that consumes the Step 8 header VT# list, the Step 8c table cells, and the
halt label token and produces a binary pass/fail without human judgment. Requires C-33 to
produce consistent multi-round evidence that the predicate specification is stable across
variation axes before a tool contract can be reliably frozen. V-03, V-04, V-05 probe whether
the checker inputs and outputs can be expressed in a machine-parseable format within the
prompt structure itself.

---

## Variation Summary Table

| V | Axis | Key change from R11 V-05 baseline | C-31 | C-32 | C-33 | New signal | Predicted |
|---|------|-----------------------------------|------|------|------|------------|-----------|
| V-01 | Regression: C-31 advisory | CONTRADICTION HALT block removed; `CONTRADICTION SIGNAL: Seq# N` label replaced with advisory prose; `Scope String Correction` Rem# type removed from Step 11; Step 8 Header preserved | FAIL | PASS | FAIL | none | 210/220 |
| V-02 | Regression: C-32 advisory | Step 8 Header VT# re-affirmation softened to advisory; REQUIRED label removed; Match? computation anchor on header removed; CONTRADICTION HALT (V-03 property) preserved intact | PASS | FAIL | FAIL | none | 210/220 |
| V-03 | Output format: structured token schema | Step 8 Header requires each VT# token in `VT-N: "exact string"` quoted format plus `TOKEN-COUNT: N` summary; Match? rule explicitly cites header token list as reference schema; Step 8c DISQUALIFIER strengthened to fail if any cell value does not appear in header quoted form | PASS | PASS | PASS | C-34 candidate: Step 8 Header now has a defined parseable schema format that a checker can ingest without prose reading | 220/220 |
| V-04 | Output format: row-level verdict token | Step 8c adds `Row-Verdict` column: `PASS` if Match? = Y (or no "Coherence confirmed" in Step 8b for this row), `HALT` if Step 8b asserted coherence AND Match? = N; CONTRADICTION SIGNAL fires on first Row-Verdict = HALT; post-table CHECK RESULT summary emitted | PASS | PASS | PASS | C-34 candidate: checker can scan Row-Verdict column for HALT without reading Match? column or Step 8b prose; binary check output externalized | 220/220 |
| V-05 | Two-axis combination: V-03 + V-04 | Structured header token schema (V-03) + Row-Verdict column (V-04) + CHECK RESULT block; checker contract fully specified: parse header `VT-N: "..."` lines, scan Row-Verdict for HALT, emit CHECK RESULT | PASS | PASS | PASS | C-34 candidate: strongest structural expression; checker input schema (Step 8 Header) and checker output schema (Row-Verdict + CHECK RESULT) both machine-parseable without prose reading | 220/220 |

---

## Shared Prompt Body (Steps 0-7, 9-11 baseline)

The following steps are identical across all five variations. Each variation section below
shows only the Step 8 block and any Step 11 Rem# type changes. For a complete runnable prompt,
substitute the shared steps around the variation-specific Step 8.

---

## V-01 -- Regression: C-31 advisory

### Axis
CONTRADICTION HALT block removed from Step 8c. The `CONTRADICTION SIGNAL: Seq# N` label is
replaced with advisory guidance: if Step 8b asserted coherence for a boundary AND Step 8c
Match? = N for the same boundary, the trace is advised to review the inconsistency but is not
structurally blocked. The `Scope String Correction` Rem# type is removed from Step 11. The
Step 8 Header scope-token re-affirmation (C-32 property) is preserved exactly as in R11 V-05.
All other R11 V-05 requirements unchanged.

### Hypothesis
Removing the typed halt event while keeping the Step 8 Header (C-32) and both surfaces
REQUIRED (C-28, C-29) isolates C-31 as load-bearing. A response will satisfy C-32 (header
present, Match? self-contained) and C-30 (prose/table divergence structurally detectable) but
will lack the named halt type, machine-greppable label, and required Rem# format output that
C-31 tests. C-33 also fails because pre-condition (b) -- named halt type -- is absent. C-30
still passes because both surfaces are REQUIRED and divergence is format-detectable. Predicted:
210/220 (-5 C-31, -5 C-33).

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
is a vocabulary drift.

---

### Step 8c -- Scope String Coherence Table (REQUIRED BEFORE STEP 9)

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
each row without reading any other section of the trace.

NOTE: If any row shows a "Coherence confirmed" statement in Step 8b AND Match? = N for
the same Seq#, this indicates a scope string inconsistency between the prose gate and
the coherence table. Review all three cell values to determine which differs from the
Step 8 Header token, correct the inconsistent cell, and re-produce the row with updated
values before proceeding to Step 9.

DISQUALIFIER: Step 8c table absent or incomplete fails C-29. Match? non-binary fails
C-29. Any cell value not present in the Step 8 Header VT# list fails C-29. Table
positioned after Step 9 fails C-29.

---

ANTI-PATTERN: Producing a Match? = N cell without reviewing whether this reflects a
transcription error or a genuine inconsistency. The divergence between Step 8b prose and
Step 8c table is structurally visible -- act on it before proceeding.

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
dedicated Rem# entry. The Parameters cell must contain the exact scope string that
closes the gap -- the same VT# token present in the Step 8 Header, confirmed in Step 8b,
and verified as Match? = Y in Step 8c.

DISQUALIFIER: Mechanism type without parameters fails C-14. Inline remediation fails
C-17. "Add error handling" without mechanism type fails C-08. Scope-gap Rem# entry
without exact scope string parameter fails C-26.

---

ANTI-PATTERN: Inline annotations in Step 3 hide parameter omissions.
ANTI-PATTERN: "Add missing scope" without naming the exact VT# scope string from the
Step 8 Header. The string is the parameter.

---

---

## V-02 -- Regression: C-32 advisory

### Axis
Step 8 Header scope-token re-affirmation softened from mandatory to advisory. The REQUIRED
label is removed. The binding commitment statement is removed. The Match? computation anchor
("A reviewer holding only this header and the Step 8c table can verify coherence without
reading Steps 0, 3, or 11") is removed. Step 8a no longer requires Scope/Role Invoked values
to come from the header VT# list. Step 8c Match? computation reverts to: "Y if all three cell
values are byte-identical; N if any differ" (no longer requires matching the Step 8 Header
token). The CONTRADICTION HALT block with `CONTRADICTION SIGNAL: Seq# N` label and
`Scope String Correction` Rem# type (C-31 property) is preserved exactly as in R11 V-05.
All other R11 V-05 requirements unchanged.

### Hypothesis
Removing REQUIRED from the Step 8 Header while keeping the CONTRADICTION HALT intact
isolates C-32 as load-bearing. A response will satisfy C-31 (named halt type with
machine-greppable label + required Rem# format output) but will lack the VT# token list
co-located at the Step 8 boundary that makes Match? computation self-contained. C-33 also
fails because pre-condition (a) -- reference set co-located at Step 8 header -- is absent.
C-30 still passes because both surfaces remain REQUIRED and divergence is format-detectable.
Predicted: 210/220 (-5 C-32, -5 C-33).

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

### Step 8 Header -- Scope-Token Reference (optional)

You may optionally re-state the platform role and the relevant VT# scope strings from
Step 0 before beginning the authorization re-walk. This can help orient the audit but
is not required. If provided, it supplements Step 0 -- it does not replace it as the
vocabulary reference for Step 8 sub-steps.

[This section is advisory.]

---

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
before Step 8c begins.

DISQUALIFIER: Re-walk findings that merely restate Step 3 Auth Check fails C-11.
Gap? = Y rows without a cited Rem# fail C-26. Coherence gate absent or incomplete
fails C-28.

---

ANTI-PATTERN: A re-walk that cites Rem# entries (C-26 PASS) but skips the coherence
confirmation (C-28 FAIL). Both are required.

---

### Step 8c -- Scope String Coherence Table with Contradiction Halt (REQUIRED BEFORE STEP 9)

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

CONTRADICTION HALT (REQUIRED): After producing the table, scan for any row where Step 8b
produced a "Coherence confirmed" statement AND Step 8c Match? = N for the same Seq#. This
is a STRUCTURAL CONTRADICTION -- the prose gate and the table disagree on the same boundary.

If any such contradiction exists, you MUST:
1. Emit: "CONTRADICTION SIGNAL: Seq# [N] -- Step 8b prose asserts coherence; Step 8c
   Match? = N. These surfaces disagree. Step 9 is BLOCKED."
2. Identify which cell among Step3-Auth, Step8a-Invoked, Step11-Params differs from the
   others and why.
3. Correct the inconsistent cell (return to the source step and fix it).
4. Add a Rem# to Step 11 with:
   - Mechanism Type: "Scope String Correction"
   - Parameters: "Cell [Step#-Column], incorrect value: [wrong string], correct VT# scope
     string: [correct string]"
5. Re-produce the Step 8c row with corrected values. Match? must = Y for all rows.
6. Only then may Step 9 proceed.

If no contradiction exists (all rows Match? = Y), emit: "COHERENCE VERIFIED: [N] rows,
all Match? = Y. Step 9 may proceed."

DISQUALIFIER: Step 8c table absent or incomplete fails C-29. Match? non-binary fails
C-29. Table positioned after Step 9 fails C-29. Contradiction detected (Step 8b says
coherent, Match? = N) but trace proceeds without CONTRADICTION SIGNAL and Rem# correction
fails C-30.

---

ANTI-PATTERN: A Match? = N cell alongside a "Coherence confirmed" statement in Step 8b
is a structural contradiction. The divergence does not require reading the scope strings --
it fires from the structural co-presence of the two signals.

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
- Scope String Correction: "Cell [Step#-Column], incorrect value: [wrong string], correct
  VT# scope string: [correct string]" (required when CONTRADICTION SIGNAL was raised at
  Step 8c)

SCOPE-GAP ENTRIES: Every scope gap identified in Step 8a (Gap? = Y) must have a
dedicated Rem# entry. The Parameters cell must contain the exact scope string that closes
the gap -- the same VT# term confirmed in Step 8b and verified as Match? = Y in Step 8c.

DISQUALIFIER: Mechanism type without parameters fails C-14. Inline remediation fails
C-17. "Add error handling" without mechanism type fails C-08. Scope-gap Rem# entry
without exact scope string parameter fails C-26. CONTRADICTION SIGNAL raised at Step 8c
without a corresponding Scope String Correction Rem# entry fails C-30.

---

ANTI-PATTERN: A scope-gap Rem# that says "add missing scope" without naming the exact
VT# scope string. The string is the parameter.
ANTI-PATTERN: A CONTRADICTION SIGNAL at Step 8c with no corresponding Rem# correction
entry in Step 11. Every named halt requires a traceable correction record.

---

---

## V-03 -- Output format: structured token schema in Step 8 Header

### Axis
Step 8 Header is augmented with a structured machine-parseable token schema. Instead of
prose re-affirmation of VT# scope strings, each token must be declared in quoted key-value
format: `VT-N: "exact scope string"` (one per line, quotes required). A `TOKEN-COUNT: N`
summary line is required. The Step 8c Match? rule is extended to explicitly reference
the header schema: "Y if all three cell values are byte-identical AND each cell value
appears verbatim as a quoted value in the Step 8 Header token schema; N otherwise." A new
DISQUALIFIER is added to Step 8c: any cell value not appearing as a quoted string in the
Step 8 Header schema fails C-29. All C-28, C-29, C-30, C-31, C-32, C-33 requirements from
R11 V-05 are otherwise preserved identically.

### Hypothesis
The structured `VT-N: "..."` format in the Step 8 Header makes the token list
machine-parseable without prose reading. A checker can extract the expected scope strings
by scanning for lines matching `^VT-[0-9]+: ".*"$` and the token count by reading
`TOKEN-COUNT: N`. This gives the checker a defined input schema (Step 8 Header parsed
token list) separate from the comparison table (Step 8c cells). The C-34 candidate: the
checker input format is specified structurally, not just by implication. Predicted:
220/220 + C-34 surface signal.

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

### Step 8 Header -- Scope-Token Schema (REQUIRED BEFORE STEP 8a)

Before beginning the authorization re-walk, declare the platform role and emit the scope
token schema that governs this audit in the following REQUIRED format:

1. **Platform role**: the same role declared at Step 0 (e.g., "Dataverse platform expert")
2. **Auth scope token schema**: declare each VT# scope string in quoted key-value format,
   one per line:
   ```
   VT-1: "exact scope string from Step 0"
   VT-2: "exact scope string from Step 0"
   ...
   TOKEN-COUNT: N
   ```
   The quoted value must be byte-identical to the VT# term committed in Step 0 -- same
   string, same casing, same delimiters. TOKEN-COUNT must equal the count of VT-N lines.
3. **Binding commitment**: "All Scope/Role Invoked cells in Step 8a, all scope string
   citations in Step 8b, and all Step3-Auth / Step8a-Invoked / Step11-Params column
   values in Step 8c derive exclusively from the quoted values in the token schema above.
   No paraphrase, abbreviation, or generic substitute is permitted in any Step 8 output."

REQUIRED: This header must appear before Step 8a. The quoted `VT-N: "..."` lines are the
machine-parseable reference schema for Step 8c Match? computation. A checker holding only
this schema block and the Step 8c table can verify coherence by comparing each cell value
against the quoted strings -- no prose reading required, no lookup into Steps 0, 3, or 11.

DISQUALIFIER: Step 8 header absent or missing quoted VT-N lines fails C-32. TOKEN-COUNT
absent or not matching the line count of VT-N entries fails C-32. Any unquoted VT# token
declaration in this header fails C-32 (quoted format is the schema contract).

---

ANTI-PATTERN: Re-stating VT# tokens in prose ("The auth scope is the delegated token
with...") rather than the structured `VT-N: "..."` format. Prose re-affirmation is not
machine-parseable. The schema format is the required form.

---

### Step 8a -- Scope Enumeration Table (REQUIRED)

| Seq# | Boundary | Scope/Role Invoked | Required Scope/Role | Verified? | Gap? |

Rules:
- **Scope/Role Invoked**: must be one of the quoted VT# values from the Step 8 Header
  schema. No value outside that set is permitted.
- **Required Scope/Role**: the minimum the platform requires; name it using VT# terms
- **Verified?**: Y if check occurs at runtime; N if assumed from upstream validation
- **Gap?**: Y if Invoked does not cover Required, or Verified? = N at a dependent
  boundary; N otherwise

Every boundary must have a named Required Scope/Role. Blank = disallowed shortcut.

DISQUALIFIER: Scope enumeration table absent fails C-25. Blank Required Scope/Role
without explanation fails C-25. Invoked value not matching a quoted string in the Step 8
Header schema fails C-25.

### Step 8b -- Re-Walk Findings (REQUIRED PROGRESSION GATE BEFORE STEP 8c)

Based on the Step 8a table:
- Name at least one new gap not in Step 3 Auth Check, OR
- Certify the three highest-risk boundaries are clean.

SCOPE-GAP REM# REQUIREMENT (REQUIRED): For every row in Step 8a where Gap? = Y, cite
the specific Rem# from Step 11 that addresses this gap. The citation must appear in the
Step 8b findings section:
  "Seq# [N] Gap? = Y -> addressed by Rem#[X] (scope: [exact VT# scope string])"

The scope string cited must be the exact quoted value from the Step 8 Header schema.

The corresponding Step 11 Rem# entry must have:
  - Mechanism Type: Permission Fix
  - Parameters: the exact scope string or role name (same quoted value from Step 8 Header)

COHERENCE PROGRESSION GATE (REQUIRED BEFORE STEP 8c): For every Gap? = Y row cited
above, confirm explicitly that the exact VT# scope string is byte-identical across all
three structures. Use this form for each boundary:

  "Coherence confirmed: [VT# scope string from Step 8 Header schema] appears verbatim in:
   - Step 3 Auth Check (Seq# [N]): [exact string as written in Step 3]
   - Step 8a Scope/Role Invoked (Seq# [N]): [exact string as written in Step 8a]
   - Step 11 Rem#[X] Parameters: [exact string as written in Step 11]"

One confirmation per Gap? = Y boundary is REQUIRED. All confirmations must appear
before Step 8c begins. The scope string cited in each confirmation must match a quoted
value in the Step 8 Header schema exactly.

DISQUALIFIER: Re-walk findings that merely restate Step 3 Auth Check fails C-11.
Gap? = Y rows without a cited Rem# fail C-26. Coherence gate absent or incomplete
fails C-28. Scope string not present as a quoted value in Step 8 Header schema fails C-28.

---

ANTI-PATTERN: A coherence confirmation citing a scope string that is not in the Step 8
Header schema quoted form. The schema is the reference. Any drift from the quoted value
will produce Match? = N in Step 8c.

---

### Step 8c -- Scope String Coherence Table with Contradiction Halt (REQUIRED BEFORE STEP 9)

For every boundary where Gap? = Y in Step 8a, produce one row:

| Seq# | Step3-Auth | Step8a-Invoked | Step11-Params | Match? |

Rules:
- **Step3-Auth**: exact scope string as written in Step 3 Auth Check cell for this Seq#
- **Step8a-Invoked**: exact scope string as written in Step 8a Scope/Role Invoked cell
- **Step11-Params**: exact scope string as written in the Step 11 Rem# Parameters cell
  for the Rem# cited in Step 8b for this Seq#
- **Match?**: Y if all three cell values are byte-identical AND each cell value appears
  verbatim as a quoted value in the Step 8 Header schema (i.e., matches `VT-N: "value"`
  for some N); N if any cell differs or any cell value is not in the schema

REQUIRED: Table must be present before Step 9. Every Gap? = Y boundary must have a row.
A checker holding only the Step 8 Header schema block and this table can compute Match?
for each row: extract quoted values from `VT-N: "..."` lines, compare each cell against
the set, emit Y or N per row. No prose reading. No lookup into Steps 0, 3, or 11.

CONTRADICTION HALT (REQUIRED): After producing the table, scan for any row where Step 8b
produced a "Coherence confirmed" statement AND Step 8c Match? = N for the same Seq#. This
is a STRUCTURAL CONTRADICTION.

If any such contradiction exists, you MUST:
1. Emit: "CONTRADICTION SIGNAL: Seq# [N] -- Step 8b prose asserts coherence; Step 8c
   Match? = N. Step 8 Header schema token: [VT# quoted value]. These surfaces disagree.
   Step 9 is BLOCKED."
2. Identify which cell (Step3-Auth, Step8a-Invoked, or Step11-Params) does not match a
   quoted value in the Step 8 Header schema and why.
3. Correct the inconsistent cell (return to the source step and fix it).
4. Add a Rem# to Step 11 with:
   - Mechanism Type: "Scope String Correction"
   - Parameters: "Cell [Step#-Column], incorrect value: [wrong string], correct quoted
     value from Step 8 Header schema: [correct string]"
5. Re-produce the Step 8c row with corrected values. Match? must = Y for all rows.
6. Only then may Step 9 proceed.

If no contradiction exists (all rows Match? = Y), emit: "COHERENCE VERIFIED: [N] rows,
all Match? = Y. Step 8 Header schema confirmed across Step 8b prose and Step 8c table.
Step 9 may proceed."

DISQUALIFIER: Step 8c table absent or incomplete fails C-29. Match? non-binary fails
C-29. Any cell value not present as a quoted string in the Step 8 Header schema fails
C-29. Table positioned after Step 9 fails C-29. Contradiction detected but trace proceeds
without CONTRADICTION SIGNAL and Rem# correction fails C-30.

---

ANTI-PATTERN: A Step 8c cell value that differs in punctuation or casing from the quoted
Step 8 Header schema value. The schema format requires byte-identical matching. A cell
that would pass a human eye check ("close enough") but fails byte-comparison is a
Match? = N and should be treated as a contradiction if Step 8b also asserted coherence.

ANTI-PATTERN: Omitting TOKEN-COUNT from the Step 8 Header. The count makes the schema
block self-validating -- a parser can verify it read all tokens without relying on
positional parsing.

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
- Permission fix: exact scope string or role identity (must match a quoted value in the
  Step 8 Header schema)
- Payload guard: specific field name and validation predicate
- Scope String Correction: "Cell [Step#-Column], incorrect value: [wrong string], correct
  quoted value from Step 8 Header schema: [correct string]" (required when CONTRADICTION
  SIGNAL was raised at Step 8c)

SCOPE-GAP ENTRIES: Every scope gap identified in Step 8a (Gap? = Y) must have a
dedicated Rem# entry. The Parameters cell must contain the exact scope string -- the same
quoted value in the Step 8 Header schema, confirmed in Step 8b, and verified as Match? = Y
in Step 8c.

DISQUALIFIER: Mechanism type without parameters fails C-14. Inline remediation fails
C-17. "Add error handling" without mechanism type fails C-08. Scope-gap Rem# entry
without exact scope string parameter fails C-26. CONTRADICTION SIGNAL raised at Step 8c
without a corresponding Scope String Correction Rem# entry fails C-30.

---

ANTI-PATTERN: A Permission Fix Rem# whose Parameters cite a scope string not present in
the Step 8 Header schema quoted form. The schema is the ground truth for all Step 8
scope string references.

---

---

## V-04 -- Output format: row-level verdict token in Step 8c

### Axis
Step 8c adds a `Row-Verdict` column to the coherence table. Row-Verdict emits `PASS` if
Match? = Y (or if no "Coherence confirmed" statement exists in Step 8b for that Seq#) and
`HALT` if Step 8b produced a "Coherence confirmed" statement for this Seq# AND Match? = N.
The CONTRADICTION SIGNAL block fires on the first Row-Verdict = HALT. After the full table,
a REQUIRED CHECK RESULT line is emitted: "CHECK RESULT: [PASS/FAIL] -- N rows checked,
M HALT rows detected." PASS if M = 0; FAIL if M > 0. The Step 8 Header scope-token
re-affirmation (C-32 property) is preserved exactly as in R11 V-05. All other R11 V-05
requirements unchanged.

### Hypothesis
The Row-Verdict column externalizes the contradiction-detection output as a per-row machine
token. A checker scanning only the Row-Verdict column can identify any HALT row without
reading the Match? column values, the Step 8b prose, or the scope strings themselves. The
CHECK RESULT summary provides a single-line binary output that captures the entire table
result. The C-34 candidate: the checker output format is defined within the prompt structure
-- checker input (Step 8 Header VT# list) and checker output (Row-Verdict + CHECK RESULT)
are both present. A tool only needs to (1) parse the header, (2) scan Row-Verdict, (3) emit
CHECK RESULT. Predicted: 220/220 + C-34 surface signal.

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
reference for Step 8c Match? and Row-Verdict computation. A reviewer holding only this
header and the Step 8c table can verify coherence without reading Steps 0, 3, or 11.

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

### Step 8c -- Scope String Coherence Table with Row-Verdict and Contradiction Halt (REQUIRED BEFORE STEP 9)

For every boundary where Gap? = Y in Step 8a, produce one row:

| Seq# | Step3-Auth | Step8a-Invoked | Step11-Params | Match? | Row-Verdict |

Rules:
- **Step3-Auth**: exact scope string as written in Step 3 Auth Check cell for this Seq#
- **Step8a-Invoked**: exact scope string as written in Step 8a Scope/Role Invoked cell
- **Step11-Params**: exact scope string as written in the Step 11 Rem# Parameters cell
  for the Rem# cited in Step 8b for this Seq#
- **Match?**: Y if all three cell values are byte-identical AND each equals a VT# token
  in the Step 8 Header re-affirmation list; N otherwise
- **Row-Verdict**: HALT if (Step 8b produced a "Coherence confirmed" statement for this
  Seq# AND Match? = N); PASS otherwise

REQUIRED: Table must be present before Step 9. Every Gap? = Y boundary must have a row.
A checker holding only the Step 8 Header VT# list and this table can verify Row-Verdict
without reading Match? cells, Step 8b prose, or scope strings: scan Row-Verdict column
for HALT.

CONTRADICTION HALT (REQUIRED): After producing the table, scan for any row where
Row-Verdict = HALT. This is a STRUCTURAL CONTRADICTION.

If any such row exists, you MUST:
1. Emit: "CONTRADICTION SIGNAL: Seq# [N] -- Step 8b prose asserts coherence; Step 8c
   Match? = N. Row-Verdict = HALT. Step 8 Header token: [VT# string]. Step 9 is BLOCKED."
2. Identify which cell (Step3-Auth, Step8a-Invoked, or Step11-Params) differs from the
   Step 8 Header token and why.
3. Correct the inconsistent cell (return to the source step and fix it).
4. Add a Rem# to Step 11 with:
   - Mechanism Type: "Scope String Correction"
   - Parameters: "Cell [Step#-Column], incorrect value: [wrong string], correct VT#
     token from Step 8 Header: [correct string]"
5. Re-produce the Step 8c row with corrected values. Match? must = Y and Row-Verdict
   must = PASS for all rows.
6. Only then emit the CHECK RESULT and proceed to Step 9.

After all contradiction rows are resolved (or if no HALT rows exist), emit:
"CHECK RESULT: [PASS/FAIL] -- N rows checked, M HALT rows detected."
- PASS if M = 0; FAIL if M > 0 (and list the offending Seq# values).

DISQUALIFIER: Step 8c table absent or incomplete fails C-29. Match? non-binary fails
C-29. Row-Verdict column absent fails C-29. Table positioned after Step 9 fails C-29.
Row-Verdict = HALT row present but trace proceeds without CONTRADICTION SIGNAL and Rem#
correction fails C-30. CHECK RESULT line absent fails C-31 surface requirement.

---

ANTI-PATTERN: Producing a Row-Verdict = HALT cell and proceeding to CHECK RESULT: PASS
without resolving the contradiction. Row-Verdict = HALT is a machine-checkable signal --
no scope string comparison needed to detect the issue.

ANTI-PATTERN: Omitting the CHECK RESULT line. This is the binary output that consumes
the Row-Verdict column and provides the single-line verdict a checker would emit.

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
  VT# token from Step 8 Header: [correct string]" (required when Row-Verdict = HALT was
  detected at Step 8c)

SCOPE-GAP ENTRIES: Every scope gap identified in Step 8a (Gap? = Y) must have a
dedicated Rem# entry. The Parameters cell must contain the exact scope string -- the same
VT# token from the Step 8 Header, confirmed in Step 8b, and verified as Row-Verdict = PASS
in Step 8c.

DISQUALIFIER: Mechanism type without parameters fails C-14. Inline remediation fails
C-17. "Add error handling" without mechanism type fails C-08. Scope-gap Rem# entry
without exact scope string parameter fails C-26. Row-Verdict = HALT detected at Step 8c
without a corresponding Scope String Correction Rem# entry fails C-30.

---

ANTI-PATTERN: A CHECK RESULT: FAIL without a corresponding Scope String Correction Rem#.
Every HALT row in Step 8c requires a traceable correction record in Step 11.

---

---

## V-05 -- Two-axis combination: structured token schema + row-level verdict token

### Axis
Combines V-03 (structured `VT-N: "..."` token schema in Step 8 Header) and V-04 (Row-Verdict
column in Step 8c + CHECK RESULT summary). The structured schema makes the checker input
format machine-parseable. The Row-Verdict column makes the checker output format machine-
parseable. Together they establish the full checker contract: (1) parse `VT-N: "..."` lines
from the Step 8 Header to get the reference token set, (2) scan the Row-Verdict column for
HALT to detect contradictions, (3) emit CHECK RESULT: PASS or FAIL. No prose reading at any
step. The CONTRADICTION SIGNAL block fires on Row-Verdict = HALT, anchoring the halt label
to the structured outputs. All C-28 through C-33 requirements from R11 V-05 are preserved.

### Hypothesis
Combined V-03 + V-04 establishes the full C-34 design surface: a checker implementation
requires only: (1) parse lines matching `^VT-[0-9]+: ".*"$` and `TOKEN-COUNT: N` from the
Step 8 Header, (2) scan Step 8c rows for Row-Verdict = HALT, (3) on HALT: verify
`CONTRADICTION SIGNAL: Seq# N` label exists (grep for fixed token), (4) verify a
`Scope String Correction` Rem# is present in Step 11, (5) emit `CHECK RESULT: PASS/FAIL --
N rows, M HALT rows`. No semantic reading of scope strings, no narrative prose traversal.
Predicted: 220/220 + strongest C-34 surface signal.

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

### Step 8 Header -- Scope-Token Schema (REQUIRED BEFORE STEP 8a)

Before beginning the authorization re-walk, declare the platform role and emit the scope
token schema that governs this audit in the following REQUIRED format:

1. **Platform role**: the same role declared at Step 0 (e.g., "Dataverse platform expert")
2. **Auth scope token schema**: declare each VT# scope string in quoted key-value format,
   one per line:
   ```
   VT-1: "exact scope string from Step 0"
   VT-2: "exact scope string from Step 0"
   ...
   TOKEN-COUNT: N
   ```
   The quoted value must be byte-identical to the VT# term committed in Step 0. TOKEN-COUNT
   must equal the count of VT-N lines above it.
3. **Binding commitment**: "All Scope/Role Invoked cells in Step 8a, all scope string
   citations in Step 8b, and all Step3-Auth / Step8a-Invoked / Step11-Params column
   values in Step 8c derive exclusively from the quoted values in the token schema above.
   No paraphrase, abbreviation, or generic substitute is permitted in any Step 8 output."

REQUIRED: This header must appear before Step 8a. The quoted `VT-N: "..."` lines are the
machine-parseable reference schema for Step 8c Match? and Row-Verdict computation.

A checker holding only this schema block and the Step 8c table can execute the full
automated check:
- Parse `VT-N: "..."` lines to get the expected token set
- For each Step 8c row, compare all three cells against the token set (Match? = Y/N)
- Check Row-Verdict column for HALT
- Emit CHECK RESULT: PASS/FAIL
No prose reading. No lookup into Steps 0, 3, or 11.

DISQUALIFIER: Step 8 header absent or missing quoted VT-N lines fails C-32. TOKEN-COUNT
absent or not matching the VT-N line count fails C-32. Any unquoted VT# token declaration
fails C-32.

---

ANTI-PATTERN: Using prose re-affirmation instead of the `VT-N: "..."` schema format.
Prose is not parseable. The schema format is the required form.

---

### Step 8a -- Scope Enumeration Table (REQUIRED)

| Seq# | Boundary | Scope/Role Invoked | Required Scope/Role | Verified? | Gap? |

Rules:
- **Scope/Role Invoked**: must be one of the quoted VT# values from the Step 8 Header
  schema. No value outside that set is permitted.
- **Required Scope/Role**: the minimum the platform requires; name it using VT# terms
- **Verified?**: Y if check occurs at runtime; N if assumed from upstream validation
- **Gap?**: Y if Invoked does not cover Required, or Verified? = N at a dependent
  boundary; N otherwise

Every boundary must have a named Required Scope/Role. Blank = disallowed shortcut.

DISQUALIFIER: Scope enumeration table absent fails C-25. Blank Required Scope/Role
without explanation fails C-25. Invoked value not matching a quoted value in Step 8
Header schema fails C-25.

### Step 8b -- Re-Walk Findings (REQUIRED PROGRESSION GATE BEFORE STEP 8c)

Based on the Step 8a table:
- Name at least one new gap not in Step 3 Auth Check, OR
- Certify the three highest-risk boundaries are clean.

SCOPE-GAP REM# REQUIREMENT (REQUIRED): For every row in Step 8a where Gap? = Y, cite
the specific Rem# from Step 11 that addresses this gap. The citation must appear in the
Step 8b findings section:
  "Seq# [N] Gap? = Y -> addressed by Rem#[X] (scope: [exact VT# scope string])"

The scope string cited must be the exact quoted value from the Step 8 Header schema.

The corresponding Step 11 Rem# entry must have:
  - Mechanism Type: Permission Fix
  - Parameters: the exact scope string (same quoted value from Step 8 Header schema)

COHERENCE PROGRESSION GATE (REQUIRED BEFORE STEP 8c): For every Gap? = Y row cited
above, confirm explicitly that the exact VT# scope string is byte-identical across all
three structures. Use this form for each boundary:

  "Coherence confirmed: [VT# scope string from Step 8 Header schema] appears verbatim in:
   - Step 3 Auth Check (Seq# [N]): [exact string as written in Step 3]
   - Step 8a Scope/Role Invoked (Seq# [N]): [exact string as written in Step 8a]
   - Step 11 Rem#[X] Parameters: [exact string as written in Step 11]"

One confirmation per Gap? = Y boundary is REQUIRED. All confirmations must appear
before Step 8c begins. The scope string cited must match a quoted value in the Step 8
Header schema exactly.

DISQUALIFIER: Re-walk findings that merely restate Step 3 Auth Check fails C-11.
Gap? = Y rows without a cited Rem# fail C-26. Coherence gate absent or incomplete
fails C-28. Scope string not present as a quoted value in Step 8 Header schema fails C-28.

---

ANTI-PATTERN: A coherence confirmation citing a scope string not in the Step 8 Header
schema quoted form. The schema is the reference. Drift from the quoted value will produce
Row-Verdict = HALT in Step 8c.

---

### Step 8c -- Scope String Coherence Table with Row-Verdict, Contradiction Halt, and Check Result (REQUIRED BEFORE STEP 9)

For every boundary where Gap? = Y in Step 8a, produce one row:

| Seq# | Step3-Auth | Step8a-Invoked | Step11-Params | Match? | Row-Verdict |

Rules:
- **Step3-Auth**: exact scope string as written in Step 3 Auth Check cell for this Seq#
- **Step8a-Invoked**: exact scope string as written in Step 8a Scope/Role Invoked cell
- **Step11-Params**: exact scope string as written in the Step 11 Rem# Parameters cell
  for the Rem# cited in Step 8b for this Seq#
- **Match?**: Y if all three cell values are byte-identical AND each value appears as a
  quoted string in the Step 8 Header schema (`VT-N: "value"` for some N); N otherwise
- **Row-Verdict**: HALT if (Step 8b produced a "Coherence confirmed" statement for this
  Seq# AND Match? = N); PASS otherwise

REQUIRED: Table must be present before Step 9. Every Gap? = Y boundary must have a row.

Automated check execution:
- Input: Step 8 Header schema (`VT-N: "..."` lines + TOKEN-COUNT)
- Input: Step 8c table (Step3-Auth, Step8a-Invoked, Step11-Params, Match?, Row-Verdict)
- Input: CONTRADICTION SIGNAL label pattern (`CONTRADICTION SIGNAL: Seq# N`)
- Rule: for each row, Match? = Y iff all three cells equal a quoted value from the schema
- Rule: Row-Verdict = HALT iff Step 8b "Coherence confirmed" exists for Seq# AND Match? = N
- Output: CHECK RESULT line (see below)
No prose reading required at any step of this check.

CONTRADICTION HALT (REQUIRED): After producing the table, scan Row-Verdict column for
HALT. On first HALT row found:

1. Emit: "CONTRADICTION SIGNAL: Seq# [N] -- Step 8b prose asserts coherence; Step 8c
   Match? = N; Row-Verdict = HALT. Step 8 Header schema token: [VT# quoted value].
   Step 9 is BLOCKED."
2. Identify which cell (Step3-Auth, Step8a-Invoked, or Step11-Params) does not match
   the Step 8 Header schema quoted value and why.
3. Correct the inconsistent cell (return to the source step and fix it).
4. Add a Rem# to Step 11 with:
   - Mechanism Type: "Scope String Correction"
   - Parameters: "Cell [Step#-Column], incorrect value: [wrong string], correct quoted
     value from Step 8 Header schema: [correct string]"
5. Re-produce the Step 8c row with corrected values. Match? = Y and Row-Verdict = PASS
   required for all rows.
6. Repeat scan until no Row-Verdict = HALT rows remain.

After all HALT rows resolved (or if no HALT rows exist), emit REQUIRED CHECK RESULT:
"CHECK RESULT: [PASS/FAIL] -- N rows checked, M HALT rows detected."
- PASS if M = 0 (all rows Row-Verdict = PASS)
- FAIL if M > 0 (list Seq# values with Row-Verdict = HALT)

Only after CHECK RESULT: PASS may Step 9 proceed.

DISQUALIFIER: Step 8c table absent or incomplete fails C-29. Match? non-binary fails
C-29. Row-Verdict column absent fails C-29. CHECK RESULT line absent fails C-29. Table
positioned after Step 9 fails C-29. Row-Verdict = HALT present but trace proceeds without
CONTRADICTION SIGNAL and Rem# correction fails C-30. CHECK RESULT: FAIL with no
resolution fails C-30.

---

ANTI-PATTERN: Emitting CHECK RESULT: PASS while any Row-Verdict = HALT row exists.
Row-Verdict is the machine verdict -- it cannot be overridden by prose assertion.

ANTI-PATTERN: Omitting TOKEN-COUNT from the Step 8 Header. TOKEN-COUNT makes the schema
block self-validating without positional parsing.

ANTI-PATTERN: A Step 8c cell value that differs from a quoted Step 8 Header schema value
in any character, even whitespace. Byte-identical matching is the Match? predicate.

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
- Permission fix: exact scope string or role identity (must match a quoted value in the
  Step 8 Header schema)
- Payload guard: specific field name and validation predicate
- Scope String Correction: "Cell [Step#-Column], incorrect value: [wrong string], correct
  quoted value from Step 8 Header schema: [correct string]" (required when Row-Verdict =
  HALT was detected at Step 8c)

SCOPE-GAP ENTRIES: Every scope gap identified in Step 8a (Gap? = Y) must have a
dedicated Rem# entry. The Parameters cell must contain the exact scope string -- the same
quoted value in the Step 8 Header schema, confirmed in Step 8b, and verified as
Row-Verdict = PASS in Step 8c.

DISQUALIFIER: Mechanism type without parameters fails C-14. Inline remediation fails
C-17. "Add error handling" without mechanism type fails C-08. Scope-gap Rem# entry
without exact scope string parameter fails C-26. Row-Verdict = HALT detected at Step 8c
without a corresponding Scope String Correction Rem# entry fails C-30.

---

ANTI-PATTERN: A Permission Fix Rem# whose Parameters cite a scope string not present
as a quoted value in the Step 8 Header schema. The schema is the ground truth.
ANTI-PATTERN: CHECK RESULT: FAIL with no Scope String Correction Rem# in Step 11.
Every HALT row requires a traceable correction record.

---
