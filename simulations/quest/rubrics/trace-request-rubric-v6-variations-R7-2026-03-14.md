# trace-request rubric v6 -- Skill Body Prompt Variations R7
# Generated: 2026-03-14

## Overview

Five complete, runnable skill body prompt variations for the `trace-request` skill,
targeting the v6 rubric (160 pts). R6 V-05 achieved 160/160 and the exhaustiveness gate
design space was declared closed. R7 therefore holds C-01 through C-21 constant and
explores new axes to surface excellence signals not yet captured by the rubric.

**R6 baseline**: V-05 prompt body (count gate + Adv? per row + DISQUALIFIER blocks).
**R7 variation surface**: phrasing register, role sequence, inertia framing, and two
new computable gate candidates (C-22, C-23).

---

## Variation Summary Table

| V | Axis | Key change from R6 V-05 | C-20 | C-21 | New signal | Predicted |
|---|------|-------------------------|------|------|------------|-----------|
| V-01 | Phrasing register: advisory | All DISQUALIFIERs softened to advisory notes; exhaustiveness gate advisory paragraph, no integer count enforcement, no Adv? per row | FAIL | FAIL | none | 150/160 |
| V-02 | Role sequence: vocabulary commitment | Role step 0 with explicit per-role vocabulary commitment block; downstream steps reference Step 0 terms | PASS | PASS | C-22 candidate: vocabulary coherence | 160/160 |
| V-03 | Inertia framing: anti-pattern per step | Each major step preceded by named anti-pattern block | PASS | PASS | none (qualitative depth) | 160/160 |
| V-04 | Role vocabulary + Step 10->6 gate (two-axis) | Step 0 vocabulary + Step 10 cross-check elevated to blocking gate with three integer counts | PASS | PASS | C-22 candidate: batch-catalog gate | 160/160 |
| V-05 | Combined: all axes + cross-step Rem# (three-axis) | Step 0 vocabulary + anti-patterns + batch-catalog gate + Steps 7/9 must cite Rem# from Register | PASS | PASS | C-22 + C-23 candidates | 160/160 |

---

## Axis rationale

R6 explored **lifecycle** (advisory vs blocking gate) and **output format** (checklist
structure, Adv? field). Both are now resolved -- the blocking gate with integer counts
and per-row Adv? is the canonical form. R7 targets three unused axes:

- **Phrasing register** (V-01): tests whether DISQUALIFIER enforcement pressure is
  load-bearing for C-20/C-21 or whether structural description alone is sufficient.
- **Role sequence** (V-02): tests whether an explicit vocabulary commitment step
  propagates platform-specific terminology across all failure-mode and permission
  columns -- a qualitative dimension not currently tested by any criterion.
- **Inertia framing** (V-03): tests whether naming the naive anti-pattern at each step
  produces richer responses in depth criteria (C-03, C-04, C-11) even when formally PASS.

V-04 and V-05 combine axes and introduce two candidate gates:
- **Batch-catalog cross-check gate** (Step 10 -> Step 6): analogous to exhaustiveness
  gate (Step 6 -> Step 3). New C-22 candidate.
- **Cross-step Rem# citation** (Steps 7/9 must cite Register rows): closes the loop
  between failure analysis and remediation. New C-23 candidate.

---

## V-01 -- Phrasing register: advisory/descriptive

### Variation axis and hypothesis

Single-axis variation. All imperative/DISQUALIFIER enforcement replaced with
advisory/descriptive phrasing. The exhaustiveness check becomes an advisory paragraph
with a suggested per-row review format -- no integer count required, no Adv? field
per row, no blocking gate language.

Hypothesis: loss of structural enforcement at the exhaustiveness gate degrades C-20
and C-21 (same failure mode as R6 V-02, confirming that integer counts and per-row
Adv? fields require explicit DISQUALIFIER pressure). C-01 through C-19 are predicted
PASS: the structural elements are described, and a capable model will likely comply
with format requests even without DISQUALIFIER language. The regression isolates
the exhaustiveness gate as the enforcement-sensitive region.

### Predicted scores table

| Criterion | Verdict | Reason |
|-----------|---------|--------|
| C-01 through C-17 | PASS | Structural elements present in advisory form; model likely complies |
| C-18 | PASS | Advisory paragraph with per-row review format; timing is described before Step 7 |
| C-19 | PASS | Adv? column in catalog table described; model likely marks one Y |
| C-20 | FAIL | No integer count requirement stated; gate summary advisory ("provide a short confirmation") |
| C-21 | FAIL | No Adv? field per checklist row described; model will not add field unprompted |
| **Total** | **150/160** | Gap: -10 pts (C-20 -5, C-21 -5) |

### Complete prompt body

---

You are a platform expert in one of the following roles -- select the most appropriate
based on the topic context provided:

- **Dataverse Platform Engineer**: OData query pipeline, plugin pipeline, Azure SQL
  storage, Dataverse API authentication (service principal, delegated token). Consider
  this role when the topic involves Dataverse tables, custom plugins, or Power Platform
  data operations.
- **Commerce Service Engineer**: CSU (Commerce Scale Unit), Retail Server, channel DB,
  async document framework, HQ sync. Consider this role when the topic involves retail
  operations, POS, storefront, or order management.
- **Power Automate / Connectors Engineer**: flow execution engine, connector runtime,
  action/trigger dispatch, throttling policies, connection references. Consider this
  role when the topic involves flows, connectors, or automation.

Briefly indicate your selected role before beginning Step 1.

---

**Step 1 -- Entry point**

Describe the entry point for this request. Try to include the HTTP method, the full
URL path with resource identifiers, the payload fields by name, and the type of
caller credential in use.

---

**Step 2 -- Nominal path summary**

In a few sentences, describe what triggers this request, which systems handle it, and
what the caller receives on a successful response. This baseline will help identify
where adversarial paths diverge in Step 7.

---

**Step 3 -- Boundary inventory**

List every distinct service boundary the request crosses, in traversal order. Try to
be comprehensive: API gateway, identity provider, routing layers, each downstream
service, storage, cache, async queues, and response assembly. Well-known intermediate
steps like token validation should be included.

Format:
1. [Boundary Name] -- [one-line description]
... (continue until complete)

Note: Step 4 should contain a row for every boundary listed here, in the same order.

---

**Step 4 -- Traversal table**

| Seq# | Boundary Name | Protocol | From->To | Failure Mode(s) | Auth? | Permission | p50 | p99 | Rem# |

For each row:

- **Failure Mode(s)**: Try to name the exact mechanism -- an HTTP status code and
  behavior, a timeout threshold and what happens when it fires, a throttle rate and
  its breach behavior. Vague entries like "may fail" or "could timeout" are less useful.
- **Auth?**: Y or N. If N, try to explain why no auth check occurs at this boundary
  and what risk this creates for downstream boundaries.
- **Permission**: The specific scope, role name, or permission object checked here.
- **p50 / p99**: Latency estimate in milliseconds. Sub-5ms entries can be annotated
  as "< 5ms -- [reason]". Try to identify at least 3 distinct latency sources.
- **Rem#**: A pointer to the remediation register (R-01, R-02, etc.).

---

**Step 5 -- Critical path and latency budget**

Identify the Seq# chain for worst-case response time. Note which segments run serially
and which in parallel. State the critical-path p50 and p99 totals.

The per-boundary p50 values from Step 4 should sum to (or reconcile with) the
critical-path total. If you see a discrepancy, try to resolve it before moving on.

---

**Step 6 -- Threat class catalog**

| # | Threat Class | All Applicable Boundary Seq# | Severity | Example Trigger | Adv? |

For each row:

- Aim for at least 5 rows covering at least 4 distinct threat classes.
- For **All Applicable Boundary Seq#**: list every boundary where this threat class
  can manifest, not just the most prominent one.
- **Severity**: High, Medium, or Low.
- **Example Trigger**: A specific, concrete example -- not "the system fails."
- **Adv?**: Mark exactly one row Y to indicate your adversarial candidate; all
  others N. Try to fill this column as you write each row.

---

**Exhaustiveness check**

Before proceeding to Step 7, review your Step 6 catalog against the Step 3 boundary
inventory. For each catalog row, consider whether any applicable boundary Seq# values
were missed.

You might organize this as a brief per-row review, noting any additions found. Once
you have completed this review, provide a short confirmation that the check is done
and note which catalog row is your adversarial candidate.

---

**Step 7 -- Adversarial scenario**

Using the threat class row you marked Adv? = Y, trace an adversarial path. Before
the trace, note the catalog row number, the threat class name, the full Seq# list
from that row, and the specific boundary where the adversarial condition is injected.

Then trace the path:
1. Nominal path up to the divergence boundary (cite Seq# values)
2. The adversarial condition injected at the divergence Seq#
3. What happens at each subsequent boundary
4. The final outcome: exact HTTP status code, error body, and storage state

---

**Step 8 -- Authorization re-walk audit**

Go back through the Step 3 boundary list and focus on authorization specifically.
Look for privilege escalation paths between adjacent boundaries, missing scope
validations that were assumed rather than verified, and service-to-service calls
with broader permissions than the initiating caller holds.

Try to identify at least one authorization concern not already recorded in Step 4,
or explicitly confirm per boundary for the three highest-risk boundaries that no
new gap exists, with your specific evidence for that conclusion.

---

**Step 9 -- Error path trace**

Trace at least one full error path from the boundary where the error originates
through each intermediate boundary to the final caller response. For each hop, note
what happens to the error (propagated unchanged, wrapped in a new type, swallowed,
retried before propagating, translated to a different status code). End with the
exact status code and error body the caller receives, and whether any partial state
was written to storage.

---

**Step 10 -- Batch and edge cases**

For each batch operation, pagination limit, or concurrent-request edge case relevant
to this request, note the specific limit, the boundary Seq# where it is enforced,
and what happens when the limit is hit.

Also note whether any of these edge cases interact with a threat class row in your
Step 6 catalog. If an interaction exists, name the catalog row and describe the
interaction mechanism.

---

**Step 11 -- Remediation Register**

Provide a Remediation Register table as a dedicated section separate from Step 4:

| Rem# | Failure Reference | Mechanism Type | Parameters |

- **Failure Reference**: The Seq# and failure mode being addressed.
- **Mechanism Type**: The remediation type (retry policy, circuit breaker, permission
  scope addition, payload validation guard, timeout configuration, etc.).
- **Parameters**: Specific operational parameters -- algorithm, delays, and max
  attempts for retries; threshold and reset interval for circuit breakers; exact scope
  string for permissions; field name and validation predicate for payload guards.

---

## V-02 -- Role sequence: role-first with vocabulary commitment

### Variation axis and hypothesis

Single-axis variation. The role selection step is expanded to **Step 0** and requires
an explicit vocabulary commitment block: the model must list the platform-specific
terms it will use for auth mechanisms, failure modes, and permission objects before
any trace work begins. All subsequent steps reference "Step 0 vocabulary" for those
fields.

Hypothesis: vocabulary binding at role-selection time produces platform-specific
terminology throughout C-03 failure modes, C-04 auth gap labels, C-11 re-walk
escalation paths, and C-14 remediation parameters -- a qualitative dimension not
currently tested by any criterion. May surface a new excellence signal: **vocabulary
coherence across steps** (candidate C-22). The 21 existing criteria predict PASS
since all structural elements are preserved.

### Predicted scores table

| Criterion | Verdict | Reason |
|-----------|---------|--------|
| C-01 through C-21 | PASS | All structural requirements inherited from R6 V-05 base |
| New: vocabulary coherence | C-22 candidate | Step 0 vocabulary propagates into C-03, C-04, C-11, C-14 fields with platform-specific terms |
| **Total** | **160/160** | + new excellence signal not yet in rubric |

### Complete prompt body

---

**Step 0 -- Role selection and vocabulary commitment**

Select your role based on the topic context:

- **Dataverse Platform Engineer**: OData query pipeline, plugin pipeline, Azure SQL
  storage, Dataverse API authentication (service principal, delegated token).
- **Commerce Service Engineer**: CSU (Commerce Scale Unit), Retail Server, channel DB,
  async document framework, HQ sync.
- **Power Automate / Connectors Engineer**: flow execution engine, connector runtime,
  action/trigger dispatch, throttling policies, connection references.

After selecting, fill in this vocabulary commitment block before writing Step 1:

```
Role: [selected role name]

Auth mechanism vocabulary (terms you will use for credential types throughout):
- Primary credential: [e.g., service principal with client_id + client_secret]
- Delegated credential: [e.g., OAuth 2.0 delegated token with UPN claim]
- Service-to-service: [e.g., managed identity with resource URI]

Failure mode vocabulary (platform-specific codes and mechanisms):
- Throttle: [e.g., 429 with Retry-After header, Dataverse 6000 req/5-min window]
- Auth rejection: [e.g., 401 with AADSTS error code from AAD token endpoint]
- Timeout: [e.g., plugin execution timeout at 2 min, returns HTTP 500 ISV error]
- Storage error: [e.g., SQL deadlock -> 500 InnerError.code: ResourceConflict]

Permission model vocabulary (terms you will use for scopes and roles):
- API scope: [e.g., https://org.crm.dynamics.com/user_impersonation]
- Object-level permission: [e.g., Dataverse table privileges: Create/Read/Write/Delete]
- Record-level access: [e.g., Business Unit depth: User/BU/ParentBU/Organization]
```

Use this vocabulary throughout your response. When Step 4, Step 6, Step 8, and Step 11
ask for auth types, failure modes, and permissions, draw from this commitment.

DISQUALIFIER: vocabulary block left as placeholder brackets; subsequent steps using
generic terms (e.g., "authentication error," "timeout," "scope") when platform-specific
terms are available from the commitment above.

---

**Step 1 -- Entry point declaration**

Declare the exact entry point using Step 0 vocabulary for credential type:

- HTTP method (GET, POST, PATCH, DELETE -- not "an HTTP request")
- Full URL path with resource identifiers (not "the endpoint")
- Payload: every field by name (not "a JSON body")
- Caller identity: exact credential type from Step 0 vocabulary

DISQUALIFIER: "a POST request" (no path), "a JSON body" (no field names), credential
type not drawn from Step 0 vocabulary commitment.

---

**Step 2 -- Nominal path summary**

2-4 sentences: what triggers this request, which systems touch it, what the caller
receives. Baseline for Step 7 divergence measurement.

---

**Step 3 -- Boundary inventory**

Every distinct service boundary in traversal order. Include: API gateway, identity
provider, routing layer, each downstream service, storage, cache, async queue,
response assembly. Token validation must not be omitted.

Format:
1. [Boundary Name] -- [one-line description]
...

GATE: Step 4 must contain a row for every boundary listed here, in order. No boundary
listed in Step 3 may be absent from Step 4.

---

**Step 4 -- Traversal table**

| Seq# | Boundary Name | Protocol | From->To | Failure Mode(s) | Auth? | Permission | p50 | p99 | Rem# |

**Failure Mode(s)**: Use the failure mode vocabulary from Step 0. Name the exact
platform-specific mechanism from that vocabulary.
DISQUALIFIER: "may fail," "could error," "an exception might be thrown" without a
named mechanism; generic mechanism (e.g., "timeout") when Step 0 vocabulary provides
a platform-specific form.

**Auth?**: Y or N. If N: "AUTH GAP -- [reason, using Step 0 auth vocabulary]."
DISQUALIFIER: "standard auth," "valid token," "handled upstream" without naming the
upstream boundary Seq# where auth is actually checked.

**Permission**: Use the permission model vocabulary from Step 0.

**p50 / p99**: Milliseconds. Sub-5ms: "< 5ms -- [reason]". Minimum 3 distinct sources.

**Rem#**: Pointer to Step 11 Remediation Register.

---

**Step 5 -- Critical path and latency budget**

Seq# chain for worst-case response time. Label serial or parallel. State critical-path
p50 and p99 totals.

SUM CLOSURE GATE: if non-parallel per-boundary p50 sums from Step 4 do not match
critical-path p50 stated here, reconcile the difference before proceeding to Step 6.

---

**Step 6 -- Threat class catalog**

| # | Threat Class | All Applicable Boundary Seq# | Severity | Example Trigger | Adv? |

Construction rules:

- Minimum 5 rows. At least 4 distinct threat classes.
- Threat class names should reflect platform vocabulary from Step 0 where applicable.
- **All Applicable Boundary Seq#**: every boundary where this threat class manifests.
  DISQUALIFIER: single Seq# for a threat known to manifest at multiple boundaries;
  "multiple," "various," "see above."
- **Adv?**: Fill Y or N on each row as you write it. Exactly one row must be Y; all
  others N. Do not change any Adv? value after Step 7 begins.
  DISQUALIFIER: no Adv? column; zero or multiple Y; blank cell; value changed after
  Step 7 begins.

---

**EXHAUSTIVENESS GATE (required before Step 7 may begin)**

For each Step 6 catalog row, re-examine the Step 3 boundary inventory and record your
finding. Each entry must carry the Adv? commitment:

- Row 1 ([Threat Class name]): Adv? = [Y/N]. Boundaries in catalog: [Seq# list]. Additional Seq# found: [Seq# added, or "none"].
- Row 2 ([Threat Class name]): Adv? = [Y/N]. Boundaries in catalog: [Seq# list]. Additional Seq# found: [Seq# added, or "none"].
- Row 3 ([Threat Class name]): Adv? = [Y/N]. Boundaries in catalog: [Seq# list]. Additional Seq# found: [Seq# added, or "none"].
- Row 4 ([Threat Class name]): Adv? = [Y/N]. Boundaries in catalog: [Seq# list]. Additional Seq# found: [Seq# added, or "none"].
- Row 5 ([Threat Class name]): Adv? = [Y/N]. Boundaries in catalog: [Seq# list]. Additional Seq# found: [Seq# added, or "none"].

Gate summary: Exhaustiveness check complete -- [N] rows reviewed against Step 3 inventory, [X] Seq# additions made.
(N = exact integer count of catalog rows reviewed. X = exact integer count of Seq# values added.)

DISQUALIFIER (C-20): gate summary omitting either integer count; hedged language
("all rows reviewed," "no additions found" without X=0); gate placed after Step 7.
DISQUALIFIER (C-21): Adv? field missing from any checklist row; placeholder "[Y/N]"
left unfilled; multiple Y; zero Y; value filled after Step 7 begins.

Step 7 may not begin until all checklist rows carry actual names, actual Seq# findings,
all Adv? fields carry Y or N, and the gate summary states both integers.

---

**Step 7 -- Adversarial scenario**

Mandatory cross-reference block before the trace:

```
Catalog row #: [N -- the row marked Adv? = Y in Step 6]
Threat class: [exact threat class name from that row]
All catalog Seq# for this row: [full Seq# list from the Adv? = Y row]
Selected divergence Seq#: [specific boundary where adversarial condition is injected]
```

DISQUALIFIER: adversarial scenario referencing a row not marked Adv? = Y; cross-
reference block placed after the trace begins; placeholder brackets left unfilled.

Trace:
1. Nominal path to divergence (cite Seq# values)
2. Adversarial condition at selected divergence Seq# -- use Step 0 vocabulary for the
   exact condition (malformed field, expired credential, concurrent mutation, etc.)
3. Per-boundary post-divergence: what it receives, what it does, what it emits
4. Concrete outcome: exact HTTP status code, error body, and storage state

---

**Step 8 -- Authorization re-walk audit**

Second pass through the Step 3 boundary list. Focus exclusively on privilege escalation
paths, missing scope validations, and auth assumed but not verified at this boundary.
Use Step 0 permission model vocabulary throughout.

Requirement: name at least one new gap not recorded in Step 4's Auth? column, OR
explicitly confirm per boundary for the three highest-risk boundaries that no new gap
was found and state the specific evidence (e.g., "Seq# 3: re-checked using Step 0
permission vocabulary -- [specific confirmation]").

DISQUALIFIER: re-walk that restates or copies Step 4's Auth? column entries without
raising new questions or providing new per-boundary evidence.

---

**Step 9 -- Error path trace**

Full error path from origination Seq# to caller. Per-hop: error condition in, boundary
action (propagates, wraps, swallows, retries, translates), error condition out.

Final: exact HTTP status code + error body + partial storage state after error.

DISQUALIFIER: "error returned to caller" or "caller receives a 500" without per-hop
propagation chain.

---

**Step 10 -- Batch and edge cases**

Per case: specific limit (exact value), enforcing boundary Seq#, behavioral consequence.
Cross-check against Step 6 catalog: for each case, name catalog row # and describe the
interaction, or state "No interaction with Step 6 catalog rows identified."

---

**Step 11 -- Remediation Register**

Dedicated table, separate from Step 4:

| Rem# | Failure Reference | Mechanism Type | Parameters |

**Failure Reference**: Seq# from Step 4 + exact failure mode string from that row.

**Mechanism Type**: One of: retry policy, circuit breaker, permission scope addition,
payload validation guard, timeout configuration, or another explicitly named type.
DISQUALIFIER: "add error handling," "add retry logic" without a mechanism type.

**Parameters**: Use Step 0 vocabulary for scope strings and platform-specific forms.
Quantified per type:
- Retry policy: algorithm (linear/exponential/jitter), initial delay (ms), multiplier,
  max-attempts, max-delay cap (ms)
- Circuit breaker: failure threshold (count or %), evaluation window (s), reset
  interval (s), half-open probe count
- Permission scope addition: exact scope string from Step 0 vocabulary
- Payload validation guard: specific field name + validation predicate
- Timeout configuration: value (ms or s), boundary, breach behavior

DISQUALIFIER: mechanism type named without quantified parameters; generic parameter
values where Step 0 vocabulary provides a platform-specific form.

---

## V-03 -- Inertia framing: anti-pattern callout per major step

### Variation axis and hypothesis

Single-axis variation. Each major step is preceded by a named anti-pattern block:
"Anti-pattern to avoid: [weak form] -- [why it fails]." The nominal path summary,
boundary inventory, traversal table, threat catalog, adversarial scenario,
authorization re-walk, and remediation register each have a dedicated anti-pattern
block. All structural enforcement and DISQUALIFIER blocks from R6 V-05 are preserved.

Hypothesis: naming the naive failure mode immediately before execution drives richer
responses in depth criteria -- especially C-03 (failure mode specificity), C-04
(auth gap precision), C-11 (auth re-walk raises new gaps), and C-09 (adversarial
path ground-truthed to catalog). May surface a qualitative excellence signal: responses
that exhibit explicit anti-pattern contrast produce boundary-level analysis qualitatively
richer than PASS/FAIL can distinguish. No new computable criterion expected; this is
a depth-of-execution dimension.

### Predicted scores table

| Criterion | Verdict | Reason |
|-----------|---------|--------|
| C-01 through C-21 | PASS | All structural requirements identical to R6 V-05 |
| New: anti-pattern contrast depth | qualitative signal | Responses exhibit richer failure mode vocabulary and auth gap analysis than rubric criteria test |
| **Total** | **160/160** | + qualitative signal not yet captured by criteria |

### Complete prompt body

---

You are a platform expert in one of the following roles -- select the most appropriate
based on the topic context provided:

- **Dataverse Platform Engineer**: OData query pipeline, plugin pipeline, Azure SQL
  storage, Dataverse API authentication (service principal, delegated token).
- **Commerce Service Engineer**: CSU (Commerce Scale Unit), Retail Server, channel DB,
  async document framework, HQ sync.
- **Power Automate / Connectors Engineer**: flow execution engine, connector runtime,
  action/trigger dispatch, throttling policies, connection references.

State your selected role in one sentence before Step 1.

---

> **Anti-pattern to avoid (Entry Point):** Describing the request as "a POST to the
> API with a JSON body from an authenticated user." This loses the path, the field
> names, and the credential type -- making every downstream failure and authorization
> analysis generic and untestable.

**Step 1 -- Entry point declaration**

Declare the exact entry point:

- HTTP method (GET, POST, PATCH, DELETE -- not "an HTTP request")
- Full URL path with resource identifiers (not "the endpoint")
- Payload: every field by name (not "a JSON body" or "the request payload")
- Caller identity: exact credential type (service principal with client_id, delegated
  OAuth token with UPN, API key with header name -- not "an authenticated user")

DISQUALIFIER: "a POST request" (no path), "a JSON body" (no field names), "an
authenticated user" (no credential type).

---

**Step 2 -- Nominal path summary**

2-4 sentences: what triggers this request, which systems touch it, what the caller
receives. This is the baseline for divergence measurement in Step 7.

---

> **Anti-pattern to avoid (Boundary Inventory):** Listing only the entry API gateway
> and the final storage layer. A surface inventory misses token validation, routing
> dispatch, plugin execution pipeline, async document queues, and cache layers -- each
> of which is an independent failure surface and authorization boundary.

**Step 3 -- Boundary inventory**

Every distinct service boundary in traversal order. Include: API gateway, identity
provider, routing layer, each downstream service, storage, cache, async queue,
response assembly. Token validation must not be omitted.

Format:
1. [Boundary Name] -- [one-line description]
...

GATE: Step 4 must contain a row for every boundary listed here, in order.

---

> **Anti-pattern to avoid (Traversal Table):** Writing "may timeout" in the Failure
> Mode column without a threshold ("2-minute plugin execution timeout returning HTTP
> 500 ISV error" is not the same as "might timeout"). Writing "standard auth" or
> "valid token" in the Auth? column without naming the upstream Seq# where that token
> was actually validated -- this hides an auth gap as a confirmation of security.

**Step 4 -- Traversal table**

| Seq# | Boundary Name | Protocol | From->To | Failure Mode(s) | Auth? | Permission | p50 | p99 | Rem# |

**Failure Mode(s)**: Exact mechanism: HTTP status code + behavior, timeout threshold
+ behavior, throttle rate + breach behavior.
DISQUALIFIER: "may fail," "could error," "an exception might be thrown."

**Auth?**: Y or N. If N: "AUTH GAP -- [reason]."
DISQUALIFIER: "standard auth," "valid token," "handled upstream" without naming the
upstream boundary Seq#.

**Permission**: Exact scope string, role name, or permission object.

**p50 / p99**: Milliseconds. Sub-5ms: "< 5ms -- [reason]". Minimum 3 distinct sources.

**Rem#**: Pointer to Step 11.

---

**Step 5 -- Critical path and latency budget**

Seq# chain for worst-case response time. Label serial or parallel. State critical-path
p50 and p99.

SUM CLOSURE GATE: non-parallel per-boundary p50 sums must match critical-path total.
Reconcile before proceeding to Step 6.

---

> **Anti-pattern to avoid (Threat Catalog):** Building a catalog that lists each
> threat at a single boundary -- "throttling happens at the API gateway." Throttling,
> injection, and privilege escalation threats manifest at multiple boundaries; listing
> only the first or most obvious one produces a catalog that passes row count but
> misses 60-80% of the actual threat surface. Similarly: filling the Adv? column after
> writing Step 7 is not a pre-commitment -- it is backward rationalization. The Adv?
> column is a forward pointer that locks in your adversarial selection before the
> adversarial analysis begins.

**Step 6 -- Threat class catalog**

| # | Threat Class | All Applicable Boundary Seq# | Severity | Example Trigger | Adv? |

Construction rules:

- Minimum 5 rows. At least 4 distinct threat classes.
- **All Applicable Boundary Seq#**: every boundary where this threat manifests.
  DISQUALIFIER: single Seq# for a multi-boundary threat; "multiple," "various," "see above."
- **Adv?**: Fill Y or N as you write each row. Exactly one row must be Y; all others
  N. Do not fill or change any Adv? value after Step 7 begins.
  DISQUALIFIER: no Adv? column; zero or multiple Y; blank cell; value changed after Step 7.

---

**EXHAUSTIVENESS GATE (required before Step 7 may begin)**

For each Step 6 catalog row, re-examine the Step 3 boundary inventory and record your
finding. Each entry must carry the Adv? commitment:

- Row 1 ([Threat Class name]): Adv? = [Y/N]. Boundaries in catalog: [Seq# list]. Additional Seq# found: [Seq# added, or "none"].
- Row 2 ([Threat Class name]): Adv? = [Y/N]. Boundaries in catalog: [Seq# list]. Additional Seq# found: [Seq# added, or "none"].
- Row 3 ([Threat Class name]): Adv? = [Y/N]. Boundaries in catalog: [Seq# list]. Additional Seq# found: [Seq# added, or "none"].
- Row 4 ([Threat Class name]): Adv? = [Y/N]. Boundaries in catalog: [Seq# list]. Additional Seq# found: [Seq# added, or "none"].
- Row 5 ([Threat Class name]): Adv? = [Y/N]. Boundaries in catalog: [Seq# list]. Additional Seq# found: [Seq# added, or "none"].

Gate summary: Exhaustiveness check complete -- [N] rows reviewed against Step 3 inventory, [X] Seq# additions made.

DISQUALIFIER (C-20): gate summary omitting either integer count; hedged language
("all rows," "no additions found" without X=0); gate placed after Step 7 begins.
DISQUALIFIER (C-21): Adv? field missing from any checklist row; placeholder not filled;
multiple Y; zero Y; value filled after Step 7 begins.

Step 7 may not begin until all checklist rows are filled with actual names and Seq#
findings, all Adv? carry Y or N, and the gate summary states both integers.

---

> **Anti-pattern to avoid (Adversarial Scenario):** Inventing an adversarial scenario
> not grounded in the threat catalog. An ad-hoc adversarial trace cannot be verified
> against the systematic threat analysis in Step 6. The adversarial scenario must test
> a threat class you cataloged -- the Adv? = Y row is the contract that makes the
> adversarial section auditable.

**Step 7 -- Adversarial scenario**

Mandatory cross-reference block before the trace:

```
Catalog row #: [the row marked Adv? = Y in Step 6]
Threat class: [exact threat class name]
All catalog Seq# for this row: [full Seq# list from the Adv? = Y row]
Selected divergence Seq#: [boundary where adversarial condition is injected]
```

DISQUALIFIER: scenario referencing a row not marked Adv? = Y; block after trace begins;
placeholder brackets left unfilled.

Trace:
1. Nominal path to divergence (cite Seq# values)
2. Adversarial condition at selected divergence Seq# (exact condition: malformed field,
   expired credential, concurrent mutation, payload size, missing required field)
3. Per-boundary post-divergence: what received, what done, what emitted
4. Concrete outcome: exact HTTP status code, error body, storage state

---

> **Anti-pattern to avoid (Authorization Re-walk):** Restating the Auth? column from
> Step 4 verbatim. The re-walk must find something new, or explicitly certify per
> boundary -- for the three highest-risk boundaries -- that no new gap exists, with
> the specific evidence for that certification. A copy of Step 4 is not an audit.

**Step 8 -- Authorization re-walk audit**

Second pass through the Step 3 boundary list. Focus: privilege escalation paths,
missing scope validations, assumed-but-unverified auth, service-to-service calls with
broader permissions than the initiating caller holds.

Requirement: name at least one new gap not in Step 4's Auth? column, OR explicitly
confirm per boundary for the three highest-risk boundaries with specific evidence.

DISQUALIFIER: re-walk restating Step 4 Auth? column without new questions or evidence.

---

**Step 9 -- Error path trace**

Full error path from origination Seq# to caller. Per-hop: error condition in, boundary
action, error condition out.

Final: exact status code + error body + partial storage state.

DISQUALIFIER: "error returned to caller" without per-hop propagation chain.

---

**Step 10 -- Batch and edge cases**

Per case: specific limit (exact value), enforcing boundary Seq#, behavioral consequence.
Cross-check against Step 6 catalog: name catalog row # and interaction mechanism, or
state "No interaction with Step 6 catalog rows identified."

---

> **Anti-pattern to avoid (Remediation Register):** Embedding remediations as inline
> annotations in Step 4 ("Rem: add retry"), or writing parameters like "increase retry
> count" without specifying algorithm, initial delay, multiplier, and max-attempts. A
> separate table makes blank Parameter cells visible as structural gaps; inline
> annotations hide omissions inside populated rows.

**Step 11 -- Remediation Register**

Dedicated table, separate from Step 4:

| Rem# | Failure Reference | Mechanism Type | Parameters |

**Failure Reference**: Seq# from Step 4 + exact failure mode string.
DISQUALIFIER: "add error handling," "add retry logic" without mechanism type.

**Parameters**: Quantified per type:
- Retry policy: algorithm (linear/exponential/jitter), initial delay (ms), multiplier,
  max-attempts, max-delay cap (ms)
- Circuit breaker: failure threshold, evaluation window (s), reset interval (s),
  half-open probe count
- Permission scope addition: exact scope string or role name
- Payload validation guard: specific field + validation predicate
- Timeout configuration: value (ms/s), boundary, breach behavior

DISQUALIFIER: mechanism type named without quantified parameters.

---

## V-04 -- Role vocabulary + Step 10->6 gate (two-axis combination)

### Variation axis and hypothesis

Two-axis combination: (1) Step 0 vocabulary commitment from V-02; (2) the Step 10
batch-edge-case cross-check with the Step 6 threat catalog is elevated from a
cross-check request to a **blocking gate** with a computable three-integer summary.

Hypothesis: the Step 10->6 gate produces a new computable audit artifact: "N edge cases
cross-referenced against M catalog rows, K interactions found." This is independently
testable (three integers required, gate must precede Step 11, per-case entries must be
filled) and does not overlap with C-18/C-20 (which gate the threat catalog against the
boundary inventory). Candidate C-22: **batch-catalog cross-check gate includes
computable summary**. The vocabulary commitment (C-22 sub-candidate) improves response
quality but does not produce a distinct computable artifact.

### Predicted scores table

| Criterion | Verdict | Reason |
|-----------|---------|--------|
| C-01 through C-21 | PASS | All structural requirements from R6 V-05 preserved |
| New: batch-catalog gate | C-22 candidate | Three-integer gate summary (N cases, M rows, K interactions) is independently testable |
| New: vocabulary coherence | qualitative signal | Platform-specific terms from Step 0 propagate throughout |
| **Total** | **160/160** | + C-22 candidate signal |

### Complete prompt body

---

**Step 0 -- Role selection and vocabulary commitment**

Select your role based on topic context:

- **Dataverse Platform Engineer**: OData pipeline, plugin pipeline, Azure SQL,
  Dataverse API auth (service principal, delegated token).
- **Commerce Service Engineer**: CSU, Retail Server, channel DB, async document
  framework, HQ sync.
- **Power Automate / Connectors Engineer**: flow execution engine, connector runtime,
  action/trigger dispatch, throttling, connection references.

Fill in the vocabulary commitment block:

```
Role: [selected role name]

Auth mechanism vocabulary:
- Primary credential: [exact type, e.g., service principal client_id + client_secret]
- Delegated credential: [exact type, e.g., OAuth 2.0 delegated token with UPN claim]
- Service-to-service: [exact type, e.g., managed identity with resource URI]

Failure mode vocabulary:
- Throttle: [platform-specific throttle mechanism + exact threshold]
- Auth rejection: [platform-specific auth rejection code + source]
- Timeout: [platform-specific timeout mechanism + threshold]
- Storage error: [platform-specific storage error type + InnerError code]

Permission model vocabulary:
- API scope: [exact scope string format for this platform]
- Object-level: [exact object permission model name]
- Record-level: [exact record access depth model]
```

DISQUALIFIER: vocabulary block left as placeholder brackets; subsequent steps using
generic terms where platform-specific vocabulary is available.

---

**Step 1 -- Entry point declaration**

Using Step 0 vocabulary for credential type:

- HTTP method + full URL path with resource identifiers
- Payload: every field by name
- Caller identity: credential type from Step 0 vocabulary

DISQUALIFIER: "a POST request" (no path); "a JSON body" (no fields); credential type
not drawn from Step 0 commitment.

---

**Step 2 -- Nominal path summary**

2-4 sentences: trigger, systems touched, caller outcome. Baseline for Step 7 divergence.

---

**Step 3 -- Boundary inventory**

Every distinct boundary in traversal order. Token validation must be included.

Format:
1. [Boundary Name] -- [description]
...

GATE: Step 4 must contain a row for every boundary here, in order.

---

**Step 4 -- Traversal table**

| Seq# | Boundary Name | Protocol | From->To | Failure Mode(s) | Auth? | Permission | p50 | p99 | Rem# |

**Failure Mode(s)**: Use Step 0 failure mode vocabulary.
DISQUALIFIER: "may fail," "could error"; generic mechanism when Step 0 provides a
platform-specific form.

**Auth?**: Y or N. If N: "AUTH GAP -- [reason using Step 0 auth vocabulary]."
DISQUALIFIER: "standard auth," "valid token," "handled upstream" without naming Seq#.

**Permission**: Step 0 permission vocabulary.

**p50 / p99**: ms. Sub-5ms: "< 5ms -- [reason]". 3+ distinct sources.

**Rem#**: Step 11 pointer.

---

**Step 5 -- Critical path and latency budget**

Seq# chain, serial/parallel labels, critical-path p50 and p99.

SUM CLOSURE GATE: non-parallel sums must match. Reconcile before proceeding.

---

**Step 6 -- Threat class catalog**

| # | Threat Class | All Applicable Boundary Seq# | Severity | Example Trigger | Adv? |

- Minimum 5 rows, 4+ threat classes.
- All Applicable Boundary Seq#: every boundary.
  DISQUALIFIER: single Seq# for multi-boundary threat; "multiple," "various."
- Adv?: exactly one Y during construction. Do not change after Step 7.
  DISQUALIFIER: no column; zero or multiple Y; blank; post-Step-7 change.

---

**EXHAUSTIVENESS GATE (required before Step 7 may begin)**

- Row 1 ([Threat Class name]): Adv? = [Y/N]. Boundaries in catalog: [Seq#]. Additional Seq# found: [added or "none"].
- Row 2 ([Threat Class name]): Adv? = [Y/N]. Boundaries in catalog: [Seq#]. Additional Seq# found: [added or "none"].
- Row 3 ([Threat Class name]): Adv? = [Y/N]. Boundaries in catalog: [Seq#]. Additional Seq# found: [added or "none"].
- Row 4 ([Threat Class name]): Adv? = [Y/N]. Boundaries in catalog: [Seq#]. Additional Seq# found: [added or "none"].
- Row 5 ([Threat Class name]): Adv? = [Y/N]. Boundaries in catalog: [Seq#]. Additional Seq# found: [added or "none"].

Gate summary: Exhaustiveness check complete -- [N] rows reviewed against Step 3 inventory, [X] Seq# additions made.

DISQUALIFIER (C-20): no integer counts; hedged language; gate after Step 7.
DISQUALIFIER (C-21): missing Adv? per row; placeholder; multiple Y; post-Step-7 fill.

Step 7 may not begin until all entries are filled and gate summary states both integers.

---

**Step 7 -- Adversarial scenario**

Mandatory cross-reference block:

```
Catalog row #: [Adv? = Y row]
Threat class: [exact name]
All catalog Seq# for this row: [full list]
Selected divergence Seq#: [injection point]
```

DISQUALIFIER: row not Adv? = Y; block after trace; placeholders unfilled.

Trace (use Step 0 vocabulary for condition and permission terms):
1. Nominal to divergence (cite Seq# values)
2. Adversarial condition at selected Seq# (exact condition)
3. Per-boundary post-divergence: received, done, emitted
4. Concrete outcome: status code, error body, storage state

---

**Step 8 -- Authorization re-walk audit**

Full boundary second pass. Privilege escalation, missing scopes, assumed auth. Use
Step 0 permission vocabulary.

Requirement: at least one new gap not in Step 4, OR per-boundary certification for
three highest-risk with specific evidence.

DISQUALIFIER: restating Step 4.

---

**Step 9 -- Error path trace**

Full path from origination Seq# to caller. Per-hop: error in, action, error out.

Final: status code + error body + storage state.

DISQUALIFIER: "error returned to caller" without propagation chain.

---

**Step 10 -- Batch and edge cases**

For each batch operation, pagination limit, or concurrent-request edge case: specific
limit (exact value), enforcing boundary Seq#, behavioral consequence.

**BATCH-CATALOG CROSS-CHECK GATE (required before Step 11 may begin)**

For each batch/edge case identified above, examine every row in your Step 6 catalog
and record the finding:

- Case 1 ([limit name at Seq# N]): Catalog rows examined: [all row #s]. Interactions found: [row # + interaction mechanism, or "none"].
- Case 2 ([limit name at Seq# N]): Catalog rows examined: [all row #s]. Interactions found: [row # + mechanism, or "none"].
- Case 3 ([limit name at Seq# N]): Catalog rows examined: [all row #s]. Interactions found: [row # + mechanism, or "none"].

Gate summary: Batch-catalog cross-check complete -- [N] edge cases cross-referenced against [M] catalog rows, [K] interactions found.
(N = exact integer count of edge cases. M = exact integer count of catalog rows. K = exact integer count of interactions found. K=0 is valid if no interactions exist.)

DISQUALIFIER (C-22 candidate): gate summary omitting any of the three integers; hedged
language ("all cases," "most rows," "some interactions"); gate placed after Step 11
begins; per-case entries left as placeholder brackets; cases listed but Step 6 rows
not named.

Step 11 may not begin until all per-case entries are filled with actual limit names,
actual Seq# values, and actual catalog row examinations, and the gate summary states
all three integers.

---

**Step 11 -- Remediation Register**

Dedicated table, separate from Step 4:

| Rem# | Failure Reference | Mechanism Type | Parameters |

Use Step 0 vocabulary for scope strings and platform-specific mechanism forms.

Parameters quantified per type:
- Retry policy: algorithm, initial delay (ms), multiplier, max-attempts, max-delay cap (ms)
- Circuit breaker: failure threshold, evaluation window (s), reset interval (s), half-open probe count
- Permission scope addition: exact scope string from Step 0 vocabulary
- Payload validation guard: specific field + validation predicate
- Timeout configuration: value (ms/s), boundary, breach behavior

DISQUALIFIER: mechanism without quantified parameters; generic terms where Step 0
provides a platform-specific form.

---

## V-05 -- Combined: role vocabulary + anti-patterns + batch-catalog gate + cross-step Rem# citations

### Variation axis and hypothesis

Three-axis combination:
1. **Role-first vocabulary commitment** (Step 0, from V-02/V-04)
2. **Anti-pattern callouts** per major step (from V-03)
3. **Batch-catalog cross-check gate** with three-integer summary (from V-04)
4. New: **Cross-step Rem# citation** -- Steps 7 (adversarial) and Step 9 (error path)
   must each cite applicable Rem# entries from the Step 11 Register, closing the
   feedback loop between failure analysis and remediation.

Hypothesis: the combination produces responses with (1) platform-specific vocabulary
throughout (vocabulary coherence), (2) anti-pattern contrast in depth criteria,
(3) computable batch-catalog gate artifact (C-22 candidate), and (4) closed-loop Rem#
citations from the adversarial and error path sections (C-23 candidate). C-23 is
independently testable: does the adversarial trace cite at least one Rem# at or after
the divergence boundary? Is that Rem# present in the Register? The same for the error
path trace.

### Predicted scores table

| Criterion | Verdict | Reason |
|-----------|---------|--------|
| C-01 through C-21 | PASS | All R6 V-05 structural requirements preserved |
| New: batch-catalog gate | C-22 candidate | Three-integer gate (N cases, M rows, K interactions) -- independently testable |
| New: cross-step Rem# citation | C-23 candidate | Adversarial + error path must cite Rem# from Register; absence or mismatch is independently testable |
| **Total** | **160/160** | + C-22 and C-23 candidate signals |

### Complete prompt body

---

**Step 0 -- Role selection and vocabulary commitment**

Select your role based on topic context:

- **Dataverse Platform Engineer**: OData pipeline, plugin pipeline, Azure SQL,
  Dataverse API auth (service principal, delegated token).
- **Commerce Service Engineer**: CSU, Retail Server, channel DB, async document
  framework, HQ sync.
- **Power Automate / Connectors Engineer**: flow execution engine, connector runtime,
  action/trigger dispatch, throttling, connection references.

Fill in the vocabulary commitment:

```
Role: [selected role name]

Auth mechanism vocabulary:
- Primary credential: [exact type]
- Delegated credential: [exact type]
- Service-to-service: [exact type]

Failure mode vocabulary:
- Throttle: [platform throttle mechanism + exact threshold]
- Auth rejection: [platform auth rejection code + source]
- Timeout: [platform timeout mechanism + threshold]
- Storage error: [platform storage error type + InnerError code]

Permission model vocabulary:
- API scope: [exact scope string format]
- Object-level: [exact object permission model]
- Record-level: [exact record access depth model]
```

DISQUALIFIER: vocabulary block left as placeholder brackets; subsequent steps using
generic terms where platform-specific vocabulary is available.

---

> **Anti-pattern to avoid (Entry Point):** "A POST with a JSON body from an
> authenticated user." Loses the path, the field names, and the credential type --
> every downstream failure and auth analysis becomes generic and untestable.

**Step 1 -- Entry point declaration**

Using Step 0 vocabulary for credential type:

- HTTP method + full URL path with resource identifiers
- Payload: every field by name
- Caller identity: from Step 0 auth mechanism vocabulary

DISQUALIFIER: "a POST request" (no path); "a JSON body" (no fields); credential type
not drawn from Step 0.

---

**Step 2 -- Nominal path summary**

2-4 sentences: trigger, systems touched, caller outcome. Baseline for Step 7 divergence.

---

> **Anti-pattern to avoid (Boundary Inventory):** Entry gateway and final storage only.
> Token validation, routing dispatch, plugin pipeline, async queues, and cache layers
> are each an independent failure and authorization surface; their omission produces a
> structurally complete-looking trace that misses most of the actual attack and
> failure surface.

**Step 3 -- Boundary inventory**

Every distinct boundary in traversal order. Token validation must be included.

Format:
1. [Boundary Name] -- [description]
...

GATE: Step 4 must contain a row for every boundary here, in order.

---

> **Anti-pattern to avoid (Traversal Table):** "May fail," "standard auth," "valid
> token." These are placeholders, not mechanisms. A traversal table filled with generic
> phrases cannot be used to design mitigations or identify the specific authorization
> gaps that would allow privilege escalation.

**Step 4 -- Traversal table**

| Seq# | Boundary Name | Protocol | From->To | Failure Mode(s) | Auth? | Permission | p50 | p99 | Rem# |

**Failure Mode(s)**: Step 0 failure mode vocabulary. Exact mechanism.
DISQUALIFIER: "may fail," "could error"; generic mechanism when Step 0 provides
platform-specific form.

**Auth?**: Y or N. If N: "AUTH GAP -- [reason using Step 0 auth vocabulary]."
DISQUALIFIER: "standard auth," "valid token," "handled upstream" without upstream Seq#.

**Permission**: Step 0 permission vocabulary.

**p50 / p99**: ms. Sub-5ms: "< 5ms -- [reason]". 3+ distinct sources.

**Rem#**: Step 11 pointer.

---

**Step 5 -- Critical path and latency budget**

Seq# chain, serial/parallel, critical-path p50 and p99.

SUM CLOSURE GATE: non-parallel sums from Step 4 must match. Reconcile before Step 6.

---

> **Anti-pattern to avoid (Threat Catalog):** Single Seq# per threat row. Post-hoc
> Adv? fill after Step 7 is written. Threat classes named without platform vocabulary
> from Step 0. The Adv? column is a forward pointer locked before adversarial analysis
> begins -- not a retrospective label.

**Step 6 -- Threat class catalog**

| # | Threat Class | All Applicable Boundary Seq# | Severity | Example Trigger | Adv? |

- Minimum 5 rows, 4+ distinct threat classes.
- Threat class names should use Step 0 vocabulary where applicable.
- All Applicable Boundary Seq#: every boundary.
  DISQUALIFIER: single Seq# for multi-boundary threat; "multiple," "various."
- Adv?: exactly one Y during construction. Do not change after Step 7.
  DISQUALIFIER: no column; zero or multiple Y; blank; post-Step-7 change.

---

**EXHAUSTIVENESS GATE (required before Step 7 may begin)**

- Row 1 ([Threat Class name]): Adv? = [Y/N]. Boundaries in catalog: [Seq#]. Additional Seq# found: [added or "none"].
- Row 2 ([Threat Class name]): Adv? = [Y/N]. Boundaries in catalog: [Seq#]. Additional Seq# found: [added or "none"].
- Row 3 ([Threat Class name]): Adv? = [Y/N]. Boundaries in catalog: [Seq#]. Additional Seq# found: [added or "none"].
- Row 4 ([Threat Class name]): Adv? = [Y/N]. Boundaries in catalog: [Seq#]. Additional Seq# found: [added or "none"].
- Row 5 ([Threat Class name]): Adv? = [Y/N]. Boundaries in catalog: [Seq#]. Additional Seq# found: [added or "none"].

Gate summary: Exhaustiveness check complete -- [N] rows reviewed against Step 3 inventory, [X] Seq# additions made.

DISQUALIFIER (C-20): no integer counts; hedged language; gate after Step 7.
DISQUALIFIER (C-21): missing Adv? per row; placeholder; multiple Y; post-Step-7 fill.

Step 7 may not begin until all entries are filled, Adv? fields carry Y or N, and gate
summary states both integers.

---

> **Anti-pattern to avoid (Adversarial Scenario):** Inventing an off-catalog threat.
> Tracing the adversarial path without referencing the remediation that addresses it.
> The adversarial section should close the loop: it shows where the boundary fails AND
> cites the Rem# that mitigates the condition.

**Step 7 -- Adversarial scenario**

Mandatory cross-reference block:

```
Catalog row #: [Adv? = Y row]
Threat class: [exact name]
All catalog Seq# for this row: [full list]
Selected divergence Seq#: [injection point]
Applicable Rem#: [one or more Rem# from Step 11 Register that address this threat class]
```

DISQUALIFIER: row not Adv? = Y; block after trace; placeholders unfilled; Applicable
Rem# field absent; Rem# listed not present in Step 11 Register.

Trace:
1. Nominal path to divergence (cite Seq# values, use Step 0 vocabulary)
2. Adversarial condition at selected Seq# (exact condition: malformed field, expired
   credential, concurrent mutation, payload size, missing required field)
3. Per-boundary post-divergence: what received, what done, what emitted
4. Concrete outcome: exact status code, error body, storage state
5. Remediation close-out: for the divergence boundary and each subsequent affected
   boundary, cite the applicable Rem# from the Register and state which parameter
   addresses the adversarial condition

DISQUALIFIER (C-23 candidate): adversarial trace with no Rem# citation at or after
the divergence boundary when applicable Rem# entries exist in the Register; Rem#
citation referencing a row not in Step 11 Register.

---

> **Anti-pattern to avoid (Authorization Re-walk):** Copying Step 4's Auth? column
> verbatim. The re-walk exists to find privilege escalation paths that the initial
> table-filling pass missed -- it must produce new findings or explicit per-boundary
> certification, not a restatement.

**Step 8 -- Authorization re-walk audit**

Full boundary second pass. Privilege escalation, missing scopes, assumed-but-unverified
auth. Step 0 permission vocabulary.

Requirement: at least one new gap not in Step 4, OR per-boundary certification for
three highest-risk with specific evidence.

DISQUALIFIER: restating Step 4.

---

**Step 9 -- Error path trace**

Full path from origination Seq# to caller. Per-hop: error condition in, boundary
action, error condition out.

Final: exact status code + error body + storage state.

Remediation close-out: for each boundary in the error path where an applicable Rem#
exists in the Register, cite it and state whether it would have prevented the error,
mitigated it, or is not applicable to this specific error type (with brief reason).

DISQUALIFIER (C-23 candidate): error path trace with no Rem# citation when applicable
Register entries exist; Rem# citation not traceable to a Register row.
DISQUALIFIER: "error returned to caller" without per-hop propagation chain.

---

**Step 10 -- Batch and edge cases**

Per case: specific limit (exact value), enforcing boundary Seq#, behavioral consequence.

**BATCH-CATALOG CROSS-CHECK GATE (required before Step 11 may begin)**

For each batch/edge case, examine every Step 6 catalog row and record the finding:

- Case 1 ([limit name at Seq# N]): Catalog rows examined: [all row #s]. Interactions found: [row # + mechanism, or "none"].
- Case 2 ([limit name at Seq# N]): Catalog rows examined: [all row #s]. Interactions found: [row # + mechanism, or "none"].
- Case 3 ([limit name at Seq# N]): Catalog rows examined: [all row #s]. Interactions found: [row # + mechanism, or "none"].

Gate summary: Batch-catalog cross-check complete -- [N] edge cases cross-referenced against [M] catalog rows, [K] interactions found.

DISQUALIFIER (C-22 candidate): any integer omitted from gate summary; hedged language
("all cases," "most rows," "some interactions found"); gate placed after Step 11 begins;
per-case entries as placeholder brackets; catalog rows not named by row number.

Step 11 may not begin until all per-case entries are filled and gate summary states
all three integers.

---

> **Anti-pattern to avoid (Remediation Register):** Embedding items in Step 4.
> Writing "add retry logic" or "increase throttle threshold" without specifying the
> exact algorithm, delay values, or scope string. The Register is a separate,
> dedicated structure so that blank Parameter cells are structurally visible -- not
> hidden inside populated traversal rows.

**Step 11 -- Remediation Register**

Dedicated table, separate from Step 4:

| Rem# | Failure Reference | Mechanism Type | Parameters |

Use Step 0 vocabulary for scope strings and platform-specific mechanism forms.

Parameters quantified per type:
- Retry policy: algorithm (linear/exponential/jitter), initial delay (ms), multiplier,
  max-attempts, max-delay cap (ms)
- Circuit breaker: failure threshold (count or %), evaluation window (s), reset
  interval (s), half-open probe count
- Permission scope addition: exact scope string from Step 0 vocabulary
- Payload validation guard: specific field + validation predicate
- Timeout configuration: value (ms/s), boundary, breach behavior

DISQUALIFIER: mechanism without quantified parameters; generic terms where Step 0
provides a platform-specific form.

---

## Variation summary and new patterns assessment

### Score ladder

| Rank | Variation | Score | Gap | All Essential |
|------|-----------|-------|-----|---------------|
| 1 | V-02 (vocabulary commitment) | **160/160** | -- | PASS |
| 1 | V-03 (anti-pattern framing) | **160/160** | -- | PASS |
| 1 | V-04 (vocabulary + batch-catalog gate) | **160/160** | -- | PASS |
| 1 | V-05 (combined: all axes) | **160/160** | -- | PASS |
| 5 | V-01 (advisory phrasing) | **150/160** | -5 C-20, -5 C-21 | PASS |

V-01 confirms that DISQUALIFIER enforcement is load-bearing for C-20 and C-21:
descriptive phrasing that requests but does not require integer counts produces the
same failure mode as R6 V-02. The rubric criterion is stable.

### New candidate signals

**C-22 candidate: Batch-catalog cross-check gate includes computable summary**

V-04 and V-05 introduce a blocking gate at Step 10 requiring three integers: N edge
cases examined, M catalog rows examined, K interactions found. This is independently
testable and does not overlap with C-20 (which gates Step 6 rows against Step 3
inventory). A response can complete C-20 (PASS) while omitting the Step 10->6 gate
entirely (C-22 FAIL). Pass condition: gate summary present before Step 11 begins,
states all three integers as exact values, per-case entries name actual limit names and
catalog row numbers.

**C-23 candidate: Adversarial and error path sections cite applicable Rem# entries**

V-05 requires Steps 7 and 9 to cite Rem# entries from the Step 11 Register at the
divergence/origination boundary and downstream affected boundaries. This is
independently testable: does the adversarial trace include at least one Rem# citation
traceable to a Register row? Does the error path do the same? This closes the
feedback loop between failure identification (Step 4) and remediation design (Step 11)
-- a loop that the current rubric does not test. C-08 through C-17 test that
remediations exist and are quantified; C-23 tests that the adversarial and error
analyses reference those remediations at the point of failure.

### Why C-22 and C-23 don't overlap

- **C-22 vs C-20**: C-20 gates the threat catalog against the boundary inventory.
  C-22 gates the batch/edge case list against the threat catalog. Different source
  (Step 10 vs Step 6) and different target (Step 6 vs Step 3). A response can pass
  C-20 (threat catalog exhaustiveness confirmed) without any Step 10 cross-check
  (C-22 FAIL).

- **C-23 vs C-08/C-14/C-17**: C-08 requires remediations to exist. C-14 requires
  parameters to be quantified. C-17 requires a dedicated separate table. C-23 requires
  the adversarial and error path sections to reference those remediations by Rem# at
  the point of failure. A response can have a complete Register (C-08, C-14, C-17 all
  PASS) with no back-reference from Steps 7 or 9 (C-23 FAIL).

### Dependency candidates

- C-22 depends on C-07 (batch/edge cases must exist before cross-check applies) and
  C-13 (threat catalog must exist to cross-check against)
- C-23 depends on C-08 (remediations must exist) and C-09 (adversarial path must
  exist for C-23 to gate the adversarial section) and C-06 (error path must exist)

---

```json
{"top_score": 160, "all_essential_pass": true, "new_patterns": ["C-22: batch-catalog gate computable summary", "C-23: cross-step Rem# citation in adversarial and error path"]}
```
