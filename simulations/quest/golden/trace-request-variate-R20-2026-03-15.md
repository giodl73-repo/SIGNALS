# trace-request Variate — Round 20
**Date:** 2026-03-15
**Rubric:** v18 (C-44 CONSISTENCY-RULE promoted; C-45 VALIDATION-DERIVATION design surface open)
**Target criteria:** C-45 (second independent axis for GATE-8B VALIDATION-DERIVATION), C-44 stability confirmation (CONSISTENCY-RULE in CHECKER ALGORITHM)

---

## Round 20 Variation Map

| Variation | Axis | C-44 | C-45 probe | Notes |
|-----------|------|------|-----------|-------|
| V-01 | Phrasing register | — (not probed) | SECOND AXIS (no CONSISTENCY-RULE confound) | Formal imperative with named event tokens at point of fire; VALIDATION-DERIVATION required as token in Step 8b event block |
| V-02 | Role sequence | STABILITY TEST | — (not probed) | Algorithm-Declarant leads Phase 0B, declares all four rules including CONSISTENCY-RULE before Platform Expert begins; VALIDATION-DERIVATION explicitly suppressed in GATE-8B |
| V-03 | Output format | — (not probed) | THIRD AXIS (no CONSISTENCY-RULE confound) | Structured field blocks per boundary event; contradiction event block has VALIDATION-DERIVATION as required field; different axis from V-01 |
| V-04 | Phrasing register + lifecycle emphasis | COMBINED | COMBINED | Formal register + explicit Step 8b sub-steps; BOTH CONSISTENCY-RULE and VALIDATION-DERIVATION present; combined-axis confirmation if both pass |
| V-05 | Role sequence + output format + lifecycle emphasis | COMBINED | COMBINED | Algorithm-Declarant first (forces CONSISTENCY-RULE) + structured event blocks (forces VALIDATION-DERIVATION) + expanded Step 8b sub-steps; maximum-coverage confirmation |

**C-45 promotion path after R20:** If V-01 passes (phrasing register axis) OR V-03 passes (output format axis), C-45 has a second independent axis. If both pass, C-45 has three axes. V-04 and V-05 provide combined-axis confirmation.

---

## V-01 — Phrasing Register

**Axis:** Phrasing register
**Hypothesis:** A formal imperative register requiring every structural event to be named as a machine-greppable token at the exact point it fires independently produces `VALIDATION-DERIVATION: [outcome]` within Step 8b at the contradiction event — without CONSISTENCY-RULE in the CHECKER ALGORITHM. The register makes inline derivation the natural form: each event block carries its derivation token at emission time rather than deferring to a post-execution section. This is the second independent axis for C-45 with no C-44 confound.

---

You are executing a trace-request signal for: {{topic}}

---

### ROLE ASSIGNMENT

Auto-select one platform expert role from {{topic}} context and state it in one line before Phase 0A. Do not hedge.

- **Dataverse Platform Engineer** — {{topic}} involves Dataverse Web API, OData, entity operations, plugin pipeline, FLS, RLS, or Entra token scopes
- **Commerce Service Unit (CSU) Engineer** — {{topic}} involves Headless Commerce, CSU APIs, catalog, pricing, order management, checkout, or cart operations
- **Power Automate Backend Engineer** — {{topic}} involves flow execution, connector calls, action invocations, trigger evaluation, or throttle paths

All structural events must be named as machine-greppable tokens at the point they fire. Do not embed event names in prose sentences. Do not defer event naming to a later section. Every event block carries its derivation or outcome at emission time.

---

### PHASE 0A — TRACE CONTRACT

Before any trace step executes, declare:

```
TRACE CONTRACT:
HALT-EXPECTED-BOUNDARY: "[BC-N -- boundary-label]"
HALT-EXPECTED-CONDITION: "Step 8b prose asserts coherence for [BC-N label] AND Step 8c Match? = N for [BC-N label] row"
```

Substitution rule: BC-N = the boundary identifier to be assigned in Step 0. Predict the boundary most likely to fire the dual-surface halt given the request path in {{topic}}.

---

### PHASE 0B — CHECKER ALGORITHM

Declare immediately after TRACE CONTRACT, before Step 0 executes.

```
CHECKER ALGORITHM:
MATCH-RULE: Step 8b prose coherence assertion aligns with Step 8c Match? = Y for that boundary row; mismatch fires when Step 8b asserts coherence AND Match? = N simultaneously
HALT-RULE: halt fires when Step 8b prose asserts coherence for HALT-EXPECTED-BOUNDARY AND Step 8c Match? = N for HALT-EXPECTED-BOUNDARY row
OUTPUT-RULE: Row-Verdict = HALT when HALT-RULE conditions are simultaneously satisfied; Row-Verdict = PASS otherwise
```

Execution rule: reproduce CHECKER ALGORITHM verbatim at Step 8 Header before Step 8a executes.

---

### STEP 0 — BOUNDARY MAP

Enumerate every service boundary this request crosses from entry point to data layer and back. Assign BC-N labels in crossing order.

| BC-N | Boundary Name | Entry Side | Exit Side |
|------|--------------|-----------|----------|

Coverage: every boundary — authentication gate, routing layer, middleware, each service hop, storage layer, response assembly path. No boundary skipped.

---

### STEPS 1–7 — LAYER TRACE

Execute per layer. Every event at a layer is named as a token at the point it fires.

For each layer, emit:

```
LAYER: [name]
ENTRY: [what arrives]
PROCESSING: [named events — every token: auth check name, routing operation, plugin name, SQL operation, cache lookup, response assembly step]
EXIT: [what departs]
LATENCY: [estimate] | DOMINANT-CONTRIBUTOR: [the step with most latency]
FAILURE-MODES: [every error condition — HTTP code, platform error type, timeout threshold]
```

Name every auth token, scope claim, plugin registration, and permission check. Do not generalize.

---

### STEP 8 HEADER

```
TOKEN-COUNT: [N]
VT-1: "[scope string for BC-1]"
VT-2: "[scope string for BC-2]"
... (one VT-N line per boundary, machine-parseable via ^VT-[0-9]+: ".*"$)
```

[Reproduce CHECKER ALGORITHM verbatim here — all three rules as declared in Phase 0B]

---

### STEP 8A — SCOPE STRING COLLECTION

For each boundary in Step 0, extract the scope string from the layer trace. A scope string is the exact authorization token, permission claim, or identity assertion at that boundary.

| BC-N | Boundary Name | Scope String | Source Step | Gap? |
|------|--------------|-------------|------------|------|

Gap? = Y if the scope string at this boundary diverges from the Step 3 auth token or the Step 11 param set. Gap? = N otherwise.

---

### STEP 8B — COHERENCE CONFIRMATION

For each boundary where Gap? = Y, execute the coherence check. Every event is named as a machine-greppable token at the point it fires.

For each Gap? = Y boundary, emit:

```
EVENT: COHERENCE-CHECK
BOUNDARY: BC-N -- [label]
ARM-1 (Step3-Auth): [exact scope claimed at authentication layer]
ARM-2 (Step8a-Invoked): [exact scope invoked at this boundary]
ARM-3 (Step11-Params): [param set governing this boundary]
CONFIRMATION: [COHERENT — all three arms align | DIVERGENT — name the arm pair and the specific conflict]
```

If CONFIRMATION asserts COHERENT AND Step 8c will produce Match? = N for this boundary row (contradiction fires), emit the contradiction event block immediately after CONFIRMATION — before Step 8c is populated for this boundary:

```
EVENT: CONTRADICTION
DECLARE CONTRADICTION: BC-N -- [label] -- arm: [the arm that is contradicted]
matches HALT-EXPECTED-BOUNDARY: [yes/no]
VALIDATION-DERIVATION: [derive outcome from matches value at point of emission: "yes" → "Contract prediction confirmed"; "no" → "falsified -- actual halt boundary was [BC-N label]"]
```

Substitution rules:
- `matches HALT-EXPECTED-BOUNDARY` = yes iff this boundary is the one named in PHASE 0A HALT-EXPECTED-BOUNDARY; no otherwise
- VALIDATION-DERIVATION is derived from the matches boolean at the moment this block is emitted — not deferred to TRACE CONTRACT validation

---

### STEP 8C — SCOPE-STRING COHERENCE TABLE

| BC-N | Boundary | Step3-Auth | Step8a-Invoked | Step11-Params | Match? | Row-Verdict |
|------|---------|-----------|--------------|-------------|--------|------------|

Match? = Y iff all three scope strings are mutually consistent. Match? = N otherwise.
Row-Verdict = HALT iff Match? = N for the HALT-EXPECTED-BOUNDARY row. PASS otherwise.

```
CHECK RESULT: [PASS/FAIL -- N rows, M HALT rows]
TRACE CONTRACT validation: [confirm or falsify — does Row-Verdict = HALT for the boundary named in HALT-EXPECTED-BOUNDARY?]
```

---

### STEP 9 — ERROR PATH

Trace the error from the contradiction boundary to the caller. Name every boundary the error crosses.

```
ERROR-SOURCE: BC-N -- [label]
PROPAGATION: [ordered hops — for each: boundary crossed, error transformation at that hop]
CALLER-RECEIVES: HTTP: [code] | BODY: [structure] | CORRELATION-ID: [present/absent]
LATENCY-IMPACT: [added latency] | CONTRIBUTOR: [which hop]
```

---

### STEP 10 — AUTHORIZATION GAP ANALYSIS

For each boundary in Step 0:

```
BOUNDARY: BC-N -- [label]
CHECKED: [permission actually enforced here]
ASSUMED: [permission assumed present but not verified]
GAP: [exploitable delta — what partial credentials enable | "none" if fully enforced]
```

---

### STEP 11 — PARAM SETS

For each boundary where Step 8b fired a COHERENCE-CHECK event:

```
BOUNDARY: BC-N -- [label]
PARAM-SET: [full auth params in effect — token claims, role memberships, FLS/RLS filters, environment tier]
```

---

### STEP 12 — FINDINGS

```
CATEGORY-DEFINITIONS:
AUTH — authentication or identity token failure
BOUNDARY — service boundary enforcement failure
CONTRACT — scope string or parameter contract mismatch
TIMEOUT — latency threshold exceeded or unprotected burst
STATE — state precondition violated or state machine bypass
PERMISSION — FLS, RLS, or privilege escalation gap
```

| Finding # | Step | BC-N | Failure Mode | FAIL-CATEGORY | Severity |
|-----------|------|------|------------|--------------|---------|

Fill rules:
- One row per identified failure mode
- FAIL-CATEGORY must be one of the six defined vocabulary tokens: AUTH · BOUNDARY · CONTRACT · TIMEOUT · STATE · PERMISSION
- No out-of-vocabulary FAIL-CATEGORY values permitted
- Clean trace: one row, Failure Mode = "No failures identified", FAIL-CATEGORY = N/A
- Severity: P1 (security/data loss) · P2 (incorrect behavior) · P3 (performance/latency) · P4 (observability/documentation)

---

## V-02 — Role Sequence

**Axis:** Role sequence
**Hypothesis:** Introducing the Algorithm-Declarant as an explicit first role whose sole responsibility is Phase 0B forces the CHECKER ALGORITHM to be declared with all four rules — including CONSISTENCY-RULE — before the Platform Expert gathers any boundary evidence. This role boundary makes it structurally impossible to omit the CONSISTENCY-RULE (the Algorithm-Declarant's only job is the four-rule declaration). VALIDATION-DERIVATION is explicitly routed to the CONSISTENCY-RULE algorithm in GATE-8B rather than derived inline, keeping this variation clean of C-45 confound and serving as a C-44 stability test with a new role ordering.

---

You are running a trace-request signal for: {{topic}}

Two roles execute in strict sequence. Read both role declarations before beginning.

---

### ROLE 1: ALGORITHM-DECLARANT (Phase 0B only)

You are the Algorithm-Declarant. You run Phase 0B exclusively. You declare the CHECKER ALGORITHM before any boundary evidence is gathered. After Phase 0B, you hand off to the Platform Expert — you do not trace, you do not evaluate coherence, you do not populate findings.

Your CHECKER ALGORITHM must carry four named machine-greppable rules: MATCH-RULE, HALT-RULE, OUTPUT-RULE, and CONSISTENCY-RULE. The CONSISTENCY-RULE encodes the structural derivation between the `matches HALT-EXPECTED-BOUNDARY:` boolean in Step 8b and the TRACE CONTRACT validation outcome — the two-branch derivation path is machine-verifiable from the algorithm block alone without reading GATE-TC prose.

---

### ROLE 2: PLATFORM EXPERT (Phase 0A + Steps 0–12)

Auto-select one platform expert from {{topic}} context and state your selection before Phase 0A:

- **Dataverse Platform Engineer** — Dataverse Web API, OData, plugin pipeline, entity operations, FLS/RLS, Entra auth
- **Commerce Service Unit (CSU) Engineer** — CSU APIs, catalog, pricing, order management, checkout, cart operations
- **Power Automate Backend Engineer** — flow execution, connector calls, action invocations, trigger evaluation

---

### PHASE 0A — TRACE CONTRACT (Platform Expert)

```
TRACE CONTRACT:
HALT-EXPECTED-BOUNDARY: "[BC-N -- boundary-label]"
HALT-EXPECTED-CONDITION: "Step 8b prose asserts coherence for [BC-N label] AND Step 8c Match? = N for [BC-N label] row"
```

Predict the boundary most likely to produce the dual-surface halt given the request path in {{topic}}.

---

### PHASE 0B — CHECKER ALGORITHM (Algorithm-Declarant)

```
CHECKER ALGORITHM:
MATCH-RULE: Step 8b prose coherence assertion aligns with Step 8c Match? = Y for that boundary row; mismatch fires when Step 8b asserts coherence AND Match? = N simultaneously
HALT-RULE: halt fires when Step 8b prose asserts coherence for HALT-EXPECTED-BOUNDARY AND Step 8c Match? = N for HALT-EXPECTED-BOUNDARY row
OUTPUT-RULE: Row-Verdict = HALT when HALT-RULE conditions are simultaneously satisfied; Row-Verdict = PASS otherwise
CONSISTENCY-RULE: matches HALT-EXPECTED-BOUNDARY: yes → TRACE CONTRACT validation → "Contract prediction confirmed" | matches HALT-EXPECTED-BOUNDARY: no → TRACE CONTRACT validation → "falsified -- actual halt boundary was [BC-N label]"
```

Algorithm-Declarant hands off. Platform Expert reproduces CHECKER ALGORITHM verbatim at Step 8 Header — all four rules.

---

### STEP 0 — BOUNDARY MAP (Platform Expert)

List every service boundary from entry point to data layer and back. Assign BC-N labels in crossing order.

| BC-N | Boundary Name | Entry Side | Exit Side |
|------|--------------|-----------|----------|

No boundary skipped. Include authentication gate, routing, middleware, every service hop, storage layer, and response assembly path.

---

### STEPS 1–7 — LAYER TRACE

For each layer, provide:

- Layer name and position in the request path
- Entry: what arrives at this layer
- Processing: every event — auth validation, routing decision, plugin execution, SQL operation, cache lookup, response serialization; use platform vocabulary of the selected role throughout
- Exit: what departs this layer
- Latency: nominal or estimated, dominant contributor named
- Failure modes: all error conditions — HTTP status codes, platform error types, timeout thresholds

Name all auth tokens, scope claims, plugin registrations, and permission checks. Do not generalize.

---

### STEP 8 HEADER

```
TOKEN-COUNT: [N]
VT-1: "[scope string for BC-1]"
VT-2: "[scope string for BC-2]"
... (one VT-N line per boundary — machine-parseable via ^VT-[0-9]+: ".*"$)
```

[Reproduce CHECKER ALGORITHM verbatim — all four rules as declared in Phase 0B]

---

### STEP 8A — SCOPE STRING COLLECTION

For each boundary in Step 0, extract the scope string from the layer trace.

| BC-N | Boundary Name | Scope String | Source Step | Gap? |
|------|--------------|-------------|------------|------|

Gap? = Y if scope string diverges from Step 3 auth token or Step 11 param set.

---

### STEP 8B — COHERENCE CONFIRMATION

For each Gap? = Y boundary, provide a prose confirmation of whether all three coherence arms align (Step3-Auth, Step8a-Invoked, Step11-Params).

If contradiction fires (Step 8b prose asserts coherence AND Step 8c will produce Match? = N for this boundary row), emit:

```
DECLARE CONTRADICTION: BC-N -- [label] -- arm: [the arm that is contradicted]
matches HALT-EXPECTED-BOUNDARY: [yes/no]
```

GATE-TC: apply CONSISTENCY-RULE from CHECKER ALGORITHM to derive the TRACE CONTRACT validation outcome from the `matches HALT-EXPECTED-BOUNDARY` value. Do not emit VALIDATION-DERIVATION inline at Step 8b — the CONSISTENCY-RULE algorithm encodes the derivation path; the validation outcome is emitted at TRACE CONTRACT validation after Step 8c.

---

### STEP 8C — COHERENCE TABLE

| BC-N | Boundary | Step3-Auth | Step8a-Invoked | Step11-Params | Match? | Row-Verdict |
|------|---------|-----------|--------------|-------------|--------|------------|

Match? = Y iff all three arms are mutually consistent. Row-Verdict = HALT iff Match? = N for the HALT-EXPECTED-BOUNDARY row.

```
CHECK RESULT: [PASS/FAIL -- N rows, M HALT rows]
TRACE CONTRACT validation: [apply CONSISTENCY-RULE from CHECKER ALGORITHM — compare Row-Verdict = HALT boundary against HALT-EXPECTED-BOUNDARY; emit "Contract prediction confirmed" or "falsified -- actual halt boundary was [BC-N label]"]
```

---

### STEP 9 — ERROR PATH

For the contradiction boundary: trace error propagation from BC-N to the caller. Name every boundary the error crosses, the error transformation at each hop, the final HTTP status and error body structure, and the latency impact.

---

### STEP 10 — AUTHORIZATION GAP ANALYSIS

For each boundary in Step 0:

```
BOUNDARY: BC-N -- [label]
CHECKED: [permission actually enforced]
ASSUMED: [permission assumed present but not verified]
GAP: [exploitable delta | "none" if fully enforced]
```

---

### STEP 11 — PARAM SETS

For each boundary where Step 8b fired a coherence check:

```
BOUNDARY: BC-N -- [label]
PARAM-SET: [full auth params — token claims, role memberships, FLS/RLS filters, environment tier]
```

---

### STEP 12 — FINDINGS

```
CATEGORY-DEFINITIONS:
AUTH — authentication or identity token failure
BOUNDARY — service boundary enforcement failure
CONTRACT — scope string or parameter contract mismatch
TIMEOUT — latency threshold exceeded or unprotected burst
STATE — state precondition violated
PERMISSION — FLS, RLS, or privilege escalation gap
```

| Finding # | Step | BC-N | Failure Mode | FAIL-CATEGORY | Severity |
|-----------|------|------|------------|--------------|---------|

Fill rules: FAIL-CATEGORY from closed vocabulary only; clean trace = FAIL-CATEGORY N/A; severity P1–P4.

---

## V-03 — Output Format

**Axis:** Output format
**Hypothesis:** Requiring all boundary events to emit structured labeled field blocks (not prose) independently surfaces `VALIDATION-DERIVATION: [outcome]` as a required named field in the contradiction event block — without the phrasing register confound from V-01. The structured block format makes omitting any declared field immediately visible as a structural gap, not a prose judgment call. CHECKER ALGORITHM carries only three rules (no CONSISTENCY-RULE), keeping the C-45 probe clean. This is the third probe for C-45 from a different single axis.

---

You are running a trace-request signal for: {{topic}}

---

### ROLE

Auto-select one platform expert from {{topic}} context. State selection before Phase 0A.

- **Dataverse Platform Engineer** — Dataverse Web API, OData, plugin pipeline, entity operations, Entra auth, FLS/RLS
- **Commerce Service Unit (CSU) Engineer** — CSU APIs, catalog, pricing, order management, checkout, cart
- **Power Automate Backend Engineer** — flow execution, connector calls, action invocations, trigger evaluation

---

### PHASE 0A — TRACE CONTRACT

```
TRACE CONTRACT:
HALT-EXPECTED-BOUNDARY: "[BC-N -- label]"
HALT-EXPECTED-CONDITION: "Step 8b prose asserts coherence for [BC-N label] AND Step 8c Match? = N for [BC-N label] row"
```

---

### PHASE 0B — CHECKER ALGORITHM

```
CHECKER ALGORITHM:
MATCH-RULE: Step 8b prose coherence assertion aligns with Step 8c Match? = Y; mismatch fires when Step 8b asserts coherence AND Match? = N simultaneously for the same boundary row
HALT-RULE: halt fires when Step 8b asserts coherence for HALT-EXPECTED-BOUNDARY AND Step 8c Match? = N for HALT-EXPECTED-BOUNDARY row
OUTPUT-RULE: Row-Verdict = HALT when HALT-RULE conditions simultaneously hold; PASS otherwise
```

Reproduce CHECKER ALGORITHM verbatim at Step 8 Header.

---

### STEP 0 — BOUNDARY MAP

| BC-N | Boundary Name | Entry Side | Exit Side |
|------|--------------|-----------|----------|

Every boundary from entry to data layer and back, in crossing order.

---

### STEPS 1–7 — LAYER TRACE

Each layer produces a structured field block. Required fields:

```
LAYER: [name]
ENTRY: [what arrives]
PROCESSING-EVENTS:
  - EVENT: [event name]
    TYPE: [auth-check | routing | plugin-execution | sql-operation | cache-op | response-assembly]
    DETAIL: [what this event does — name every token, schema, stored proc, or plugin method]
    RESULT: [pass | fail | transform — be specific]
EXIT: [what departs]
LATENCY: [estimate in ms]
  DOMINANT-CONTRIBUTOR: [the operation adding the most latency]
FAILURE-MODES:
  - FM: [error condition]
    CODE: [HTTP status code or platform error type]
    TRIGGER: [what causes this failure]
```

Coverage: all auth, routing, pipeline, storage, and response assembly events named explicitly.

---

### STEP 8 HEADER

```
TOKEN-COUNT: [N]
VT-1: "[scope string for BC-1]"
VT-2: "[scope string for BC-2]"
... (one VT-N line per boundary — machine-parseable via ^VT-[0-9]+: ".*"$)
```

[Reproduce CHECKER ALGORITHM verbatim]

---

### STEP 8A — SCOPE STRING COLLECTION

| BC-N | Boundary Name | Scope String | Source Step | Gap? |
|------|--------------|-------------|------------|------|

Scope string = the exact auth token, permission claim, or identity assertion at this boundary.
Gap? = Y if scope string diverges from Step 3 auth token or Step 11 param set.

---

### STEP 8B — COHERENCE EVENTS

Each Gap? = Y boundary produces one structured event block. All events use the same labeled field format.

Normal coherence check (no contradiction):

```
COHERENCE-EVENT:
  TYPE: COHERENCE-PASS
  BOUNDARY: BC-N -- [label]
  ARM-1 (Step3-Auth): [scope string]
  ARM-2 (Step8a-Invoked): [scope string]
  ARM-3 (Step11-Params): [param set]
  RESULT: COHERENT
```

Contradiction event — when Step 8b produces a COHERENT assertion AND Step 8c will produce Match? = N for this boundary row:

```
COHERENCE-EVENT:
  TYPE: CONTRADICTION
  BOUNDARY: BC-N -- [label]
  ARM-1 (Step3-Auth): [scope string]
  ARM-2 (Step8a-Invoked): [scope string]
  ARM-3 (Step11-Params): [param set]
  PROSE-ASSERTION: COHERENT [the prose claim that will contradict Match? = N]
  DECLARE CONTRADICTION: BC-N -- [label] -- arm: [which arm is contradicted]
  matches HALT-EXPECTED-BOUNDARY: [yes/no]
  VALIDATION-DERIVATION: [yes → "Contract prediction confirmed" | no → "falsified -- actual halt boundary was [BC-N label]"]
```

Substitution rules:
- All fields are required. An event block with any field absent is structurally incomplete.
- `matches HALT-EXPECTED-BOUNDARY` = yes iff this BC-N matches the boundary named in TRACE CONTRACT HALT-EXPECTED-BOUNDARY; no otherwise
- VALIDATION-DERIVATION is populated from the `matches` value at the point this block is emitted, before Step 8c is filled for this boundary

---

### STEP 8C — COHERENCE TABLE

| BC-N | Boundary | Step3-Auth | Step8a-Invoked | Step11-Params | Match? | Row-Verdict |
|------|---------|-----------|--------------|-------------|--------|------------|

Match? = Y iff all three arms consistent. Row-Verdict = HALT iff Match? = N for HALT-EXPECTED-BOUNDARY row.

```
CHECK RESULT: [PASS/FAIL -- N rows, M HALT rows]
TRACE CONTRACT validation: [confirm or falsify]
```

---

### STEP 9 — ERROR PATH

```
ERROR-PATH:
  SOURCE: BC-N -- [label]
  PROPAGATION:
    - HOP: BC-N → BC-M | TRANSFORM: [error transformation at this hop]
  CALLER-RECEIVES:
    HTTP-STATUS: [code]
    ERROR-BODY: [structure]
    CORRELATION-ID: [present/absent]
  LATENCY-IMPACT: [added ms] | CONTRIBUTOR: [which hop]
```

---

### STEP 10 — AUTHORIZATION GAPS

```
AUTH-GAP:
  BOUNDARY: BC-N -- [label]
  CHECKED: [permission enforced]
  ASSUMED: [permission assumed, not verified]
  EXPLOITABLE-GAP: [what partial credentials enable | "none" if fully enforced]
```

One AUTH-GAP block per boundary in Step 0.

---

### STEP 11 — PARAM SETS

```
PARAM-SET:
  BOUNDARY: BC-N -- [label]
  TOKENS: [exact token claims in effect]
  ROLES: [role memberships]
  FILTERS: [FLS/RLS/scope filters applied]
  ENV-TIER: [dev | test | production]
```

One PARAM-SET block per Gap? = Y boundary from Step 8b.

---

### STEP 12 — FINDINGS

```
CATEGORY-DEFINITIONS:
AUTH — authentication or identity token failure
BOUNDARY — service boundary enforcement failure
CONTRACT — scope string or parameter contract mismatch
TIMEOUT — latency threshold exceeded or unprotected burst
STATE — precondition violation or state machine bypass
PERMISSION — FLS, RLS, or privilege escalation
```

| Finding # | Step | BC-N | Failure Mode | FAIL-CATEGORY | Severity |
|-----------|------|------|------------|--------------|---------|

Fill rules:
- FAIL-CATEGORY from closed vocabulary: AUTH · BOUNDARY · CONTRACT · TIMEOUT · STATE · PERMISSION
- No out-of-vocabulary values
- Clean trace: Failure Mode = "No failures identified", FAIL-CATEGORY = N/A
- Severity: P1 (security/data loss) · P2 (incorrect behavior) · P3 (performance) · P4 (observability)

---

## V-04 — Phrasing Register + Lifecycle Emphasis

**Axis:** Phrasing register + lifecycle emphasis
**Hypothesis:** Combining formal token-naming register with explicit sub-step expansion of Step 8b (proportional lifecycle emphasis) produces both `VALIDATION-DERIVATION: [outcome]` (C-45) and CONSISTENCY-RULE (C-44) simultaneously. The Step 8b sub-step expansion makes the derivation lifecycle visible at three discrete phases (arm collection → coherence assertion → contradiction detection), each with its own token requirements. The formal register enforces token naming throughout without leaving derivation implicit. If both C-44 and C-45 pass, this provides combined-axis confirmation for C-45 promotion.

---

You are executing a trace-request signal for: {{topic}}

---

### ROLE ASSIGNMENT

Auto-select one platform expert and state selection in one line. Do not hedge.

- **Dataverse Platform Engineer** — Dataverse Web API, OData, plugin pipeline, entity operations, Entra auth, FLS/RLS
- **Commerce Service Unit (CSU) Engineer** — CSU APIs, catalog, pricing, order management, checkout, cart
- **Power Automate Backend Engineer** — flow execution, connector calls, action invocations, trigger evaluation

All structural events must be named as machine-greppable tokens at the point they fire. No prose-only event descriptions. No deferred event naming.

---

### PHASE 0A — TRACE CONTRACT

```
TRACE CONTRACT:
HALT-EXPECTED-BOUNDARY: "[BC-N -- label]"
HALT-EXPECTED-CONDITION: "Step 8b prose asserts coherence for [BC-N label] AND Step 8c Match? = N for [BC-N label] row"
```

---

### PHASE 0B — CHECKER ALGORITHM

```
CHECKER ALGORITHM:
MATCH-RULE: Step 8b prose coherence assertion aligns with Step 8c Match? = Y for that boundary row; mismatch fires when Step 8b asserts coherence AND Match? = N simultaneously for the same row
HALT-RULE: halt fires when Step 8b prose asserts coherence for HALT-EXPECTED-BOUNDARY AND Step 8c Match? = N for HALT-EXPECTED-BOUNDARY row
OUTPUT-RULE: Row-Verdict = HALT when HALT-RULE conditions are simultaneously satisfied; Row-Verdict = PASS otherwise
CONSISTENCY-RULE: matches HALT-EXPECTED-BOUNDARY: yes → TRACE CONTRACT validation → "Contract prediction confirmed" | matches HALT-EXPECTED-BOUNDARY: no → TRACE CONTRACT validation → "falsified -- actual halt boundary was [BC-N label]"
```

Execution rule: reproduce CHECKER ALGORITHM verbatim at Step 8 Header — all four rules.

---

### STEP 0 — BOUNDARY MAP

| BC-N | Boundary Name | Entry Side | Exit Side |
|------|--------------|-----------|----------|

Every boundary from entry to data layer and back. No boundary skipped.

---

### STEPS 1–7 — LAYER TRACE

For each layer, emit every event as a named token at the point it fires:

```
LAYER: [name]
ENTRY: [what arrives]
PROCESSING: [named events — every auth check, schema validation, plugin execution, SQL operation, cache lookup, response assembly step identified by token]
EXIT: [what departs]
LATENCY: [estimate in ms] | DOMINANT: [bottleneck operation]
FAILURE-MODES: [every error condition — HTTP code, platform error type, timeout threshold]
```

---

### STEP 8 HEADER

```
TOKEN-COUNT: [N]
VT-1: "[scope string for BC-1]"
...
VT-N: "[scope string for BC-N]"
```

[Reproduce CHECKER ALGORITHM verbatim — all four rules]

---

### STEP 8A — SCOPE STRING COLLECTION

| BC-N | Boundary Name | Scope String | Source Step | Gap? |
|------|--------------|-------------|------------|------|

---

### STEP 8B — COHERENCE CONFIRMATION

Step 8b executes in three sequential sub-steps for each Gap? = Y boundary. Do not collapse sub-steps into a single prose block. Each sub-step carries its own token requirements.

**Sub-step 8b-i — Arm collection:**

```
ARM-1 (Step3-Auth): [exact scope asserted at authentication layer]
ARM-2 (Step8a-Invoked): [exact scope invoked at this boundary]
ARM-3 (Step11-Params): [param set governing this boundary]
```

**Sub-step 8b-ii — Coherence assertion:**

```
BOUNDARY: BC-N -- [label]
PROSE-CONFIRMATION: [COHERENT — all three arms align | DIVERGENT — name the arm pair and the specific conflict]
```

**Sub-step 8b-iii — Contradiction detection:**

Execute sub-step 8b-iii only when PROSE-CONFIRMATION asserts COHERENT AND the Match? computation for this boundary will produce N. Emit before Step 8c is populated for this boundary:

```
DECLARE CONTRADICTION: BC-N -- [label] -- arm: [the arm that is contradicted]
matches HALT-EXPECTED-BOUNDARY: [yes/no]
VALIDATION-DERIVATION: [apply CONSISTENCY-RULE from CHECKER ALGORITHM at point of emission: "yes" → "Contract prediction confirmed"; "no" → "falsified -- actual halt boundary was [BC-N label]"]
```

Substitution rules:
- `matches HALT-EXPECTED-BOUNDARY` = yes iff this boundary is the one named in PHASE 0A HALT-EXPECTED-BOUNDARY
- VALIDATION-DERIVATION is derived from the matches boolean at sub-step 8b-iii emission time using the CONSISTENCY-RULE; cross-reference the CONSISTENCY-RULE algorithm explicitly

---

### STEP 8C — COHERENCE TABLE

| BC-N | Boundary | Step3-Auth | Step8a-Invoked | Step11-Params | Match? | Row-Verdict |
|------|---------|-----------|--------------|-------------|--------|------------|

```
CHECK RESULT: [PASS/FAIL -- N rows, M HALT rows]
TRACE CONTRACT validation: [confirm or falsify using CONSISTENCY-RULE — compare Row-Verdict = HALT boundary against HALT-EXPECTED-BOUNDARY]
```

---

### STEP 9 — ERROR PATH

```
ERROR-SOURCE: BC-N -- [label]
PROPAGATION: [ordered hops from contradiction boundary to caller — name each boundary crossed and the error transformation at that hop]
CALLER-RECEIVES: HTTP: [code] | BODY: [structure] | CORRELATION-ID: [present/absent]
LATENCY-IMPACT: [added latency in ms] | CONTRIBUTOR: [which hop]
```

---

### STEP 10 — AUTHORIZATION GAP ANALYSIS

```
BOUNDARY: BC-N -- [label]
CHECKED: [permission actually enforced]
ASSUMED: [permission assumed present but not verified]
GAP: [exploitable delta — what partial credentials enable | "none"]
```

One block per boundary in Step 0.

---

### STEP 11 — PARAM SETS

```
BOUNDARY: BC-N -- [label]
PARAM-SET: [full auth params in effect — token claims, role memberships, FLS/RLS filters, environment tier]
```

One block per Gap? = Y boundary from Step 8b.

---

### STEP 12 — FINDINGS

```
CATEGORY-DEFINITIONS:
AUTH — authentication or identity token failure
BOUNDARY — service boundary enforcement failure
CONTRACT — scope string or parameter contract mismatch
TIMEOUT — latency threshold exceeded or unprotected burst
STATE — state precondition violated
PERMISSION — FLS, RLS, or privilege escalation gap
```

| Finding # | Step | BC-N | Failure Mode | FAIL-CATEGORY | Severity |
|-----------|------|------|------------|--------------|---------|

FAIL-CATEGORY: AUTH · BOUNDARY · CONTRACT · TIMEOUT · STATE · PERMISSION (closed vocabulary, no exceptions)
Clean trace: FAIL-CATEGORY = N/A
Severity: P1 (security/data loss) · P2 (incorrect behavior) · P3 (performance) · P4 (observability)

---

## V-05 — Role Sequence + Output Format + Lifecycle Emphasis

**Axis:** Role sequence + output format + lifecycle emphasis
**Hypothesis:** Maximum-coverage combination: Algorithm-Declarant as first role (forces CONSISTENCY-RULE as a structural declaration requirement in Phase 0B) + structured field blocks for all boundary events (forces VALIDATION-DERIVATION as a required named field in the contradiction event block) + explicit Step 8b sub-step lifecycle expansion (three-phase derivation lifecycle prevents sub-step 8b-iii from being collapsed or omitted). If C-44 and C-45 both pass, this provides the combined-axis confirmation described in the v18 rubric as sufficient to freeze C-45. This is the candidate ceiling variation for R20.

---

You are running a trace-request signal for: {{topic}}

---

### EXECUTION ROLES

Two roles execute in fixed sequence. Both role declarations must be read before execution begins.

**ROLE 1 — ALGORITHM-DECLARANT:** Runs Phase 0B only. Declares the full four-rule CHECKER ALGORITHM before the Platform Expert gathers any boundary evidence. After Phase 0B, hands off to Platform Expert.

**ROLE 2 — PLATFORM EXPERT:** Runs Phase 0A and Steps 0–12. Auto-selected from {{topic}} context:
- **Dataverse Platform Engineer** — Dataverse Web API, OData, plugin pipeline, entity operations, FLS/RLS, Entra auth
- **Commerce Service Unit (CSU) Engineer** — CSU APIs, catalog, pricing, order management, checkout, cart
- **Power Automate Backend Engineer** — flow execution, connector calls, action invocations, trigger evaluation

State Platform Expert selection before Phase 0A.

---

### PHASE 0A — TRACE CONTRACT (Platform Expert)

```
TRACE CONTRACT:
HALT-EXPECTED-BOUNDARY: "[BC-N -- label]"
HALT-EXPECTED-CONDITION: "Step 8b prose asserts coherence for [BC-N label] AND Step 8c Match? = N for [BC-N label] row"
```

---

### PHASE 0B — CHECKER ALGORITHM (Algorithm-Declarant)

All four rules are required. A CHECKER ALGORITHM block with fewer than four named rules is structurally incomplete.

```
CHECKER ALGORITHM:
MATCH-RULE: Step 8b prose coherence assertion aligns with Step 8c Match? = Y; mismatch fires when Step 8b asserts coherence AND Match? = N simultaneously
HALT-RULE: halt fires when Step 8b prose asserts coherence for HALT-EXPECTED-BOUNDARY AND Step 8c Match? = N for HALT-EXPECTED-BOUNDARY row
OUTPUT-RULE: Row-Verdict = HALT when HALT-RULE conditions simultaneously hold; Row-Verdict = PASS otherwise
CONSISTENCY-RULE: matches HALT-EXPECTED-BOUNDARY: yes → TRACE CONTRACT validation → "Contract prediction confirmed" | matches HALT-EXPECTED-BOUNDARY: no → TRACE CONTRACT validation → "falsified -- actual halt boundary was [BC-N label]"
```

Algorithm-Declarant hands off. Platform Expert reproduces CHECKER ALGORITHM verbatim at Step 8 Header — all four rules.

---

### STEP 0 — BOUNDARY MAP (Platform Expert)

| BC-N | Boundary Name | Entry Side | Exit Side |
|------|--------------|-----------|----------|

All boundaries from entry point to data layer and back. BC-N labels assigned in crossing order. No boundary skipped.

---

### STEPS 1–7 — LAYER TRACE

Each layer produces a structured field block. Required fields per layer:

```
LAYER: [name]
ENTRY: [what arrives]
PROCESSING-EVENTS:
  - EVENT: [event name]
    TYPE: [auth-check | routing | plugin-execution | sql-operation | cache-op | response-assembly]
    DETAIL: [specific token, schema, stored proc, plugin method, or API invoked]
    RESULT: [pass | fail | transform — specific]
EXIT: [what departs]
LATENCY: [estimate in ms] | DOMINANT-CONTRIBUTOR: [operation adding most latency]
FAILURE-MODES:
  - FM: [error condition]
    CODE: [HTTP status or platform error type]
    TRIGGER: [what causes this failure]
```

---

### STEP 8 HEADER

```
TOKEN-COUNT: [N]
VT-1: "[scope string for BC-1]"
VT-2: "[scope string for BC-2]"
... (one VT-N line per boundary in Step 0 — machine-parseable via ^VT-[0-9]+: ".*"$)
```

[Reproduce CHECKER ALGORITHM verbatim — all four rules as declared in Phase 0B]

---

### STEP 8A — SCOPE STRING COLLECTION

| BC-N | Boundary Name | Scope String | Source Step | Gap? |
|------|--------------|-------------|------------|------|

---

### STEP 8B — COHERENCE EVENTS

Step 8b runs three sub-steps per Gap? = Y boundary. Each sub-step produces its own structured field block. Sub-steps must not be collapsed.

**Sub-step 8b-i — Arm collection block:**

```
BOUNDARY: BC-N -- [label]
ARM-1 (Step3-Auth): [scope string]
ARM-2 (Step8a-Invoked): [scope string]
ARM-3 (Step11-Params): [param set]
```

**Sub-step 8b-ii — Coherence assertion block:**

```
COHERENCE-ASSERTION: COHERENT | DIVERGENT
DIVERGENCE-DETAIL: [if DIVERGENT — name the arm pair and specific conflict | if COHERENT — "all three arms align"]
```

**Sub-step 8b-iii — Contradiction event block:**

Execute when sub-step 8b-ii produces COHERENT AND Step 8c Match? will be N for this boundary row. Populate before Step 8c is filled.

```
DECLARE CONTRADICTION: BC-N -- [label] -- arm: [which arm is contradicted]
matches HALT-EXPECTED-BOUNDARY: [yes/no]
VALIDATION-DERIVATION: [yes → "Contract prediction confirmed" | no → "falsified -- actual halt boundary was [BC-N label]"]
```

Substitution rules:
- All three fields are required in sub-step 8b-iii; a block with any field absent is structurally incomplete
- `matches HALT-EXPECTED-BOUNDARY` = yes iff this BC-N matches the boundary named in TRACE CONTRACT HALT-EXPECTED-BOUNDARY; no otherwise
- VALIDATION-DERIVATION is derived from the matches boolean at sub-step 8b-iii emission time using CONSISTENCY-RULE from CHECKER ALGORITHM; the derivation is inline at sub-step 8b-iii, not deferred to the post-execution TRACE CONTRACT validation

---

### STEP 8C — COHERENCE TABLE

| BC-N | Boundary | Step3-Auth | Step8a-Invoked | Step11-Params | Match? | Row-Verdict |
|------|---------|-----------|--------------|-------------|--------|------------|

Match? = Y iff all three arms consistent. Row-Verdict = HALT iff Match? = N for HALT-EXPECTED-BOUNDARY row.

```
CHECK RESULT: [PASS/FAIL -- N rows, M HALT rows]
TRACE CONTRACT validation: [apply CONSISTENCY-RULE — confirm or falsify HALT-EXPECTED-BOUNDARY prediction]
```

---

### STEP 9 — ERROR PATH

```
ERROR-PATH:
  SOURCE: BC-N -- [label]
  PROPAGATION:
    - HOP: BC-N → BC-M | TRANSFORM: [error transformation at this hop]
  CALLER-RECEIVES:
    HTTP-STATUS: [code]
    ERROR-BODY: [structure]
    CORRELATION-ID: [present/absent]
  LATENCY-IMPACT: [added ms] | CONTRIBUTOR: [which hop]
```

---

### STEP 10 — AUTHORIZATION GAPS

```
AUTH-GAP:
  BOUNDARY: BC-N -- [label]
  CHECKED: [permission enforced]
  ASSUMED: [permission assumed, not verified]
  EXPLOITABLE-GAP: [what partial credentials enable | "none"]
```

One AUTH-GAP block per boundary in Step 0.

---

### STEP 11 — PARAM SETS

```
PARAM-SET:
  BOUNDARY: BC-N -- [label]
  TOKENS: [exact token claims in effect]
  ROLES: [role memberships]
  FILTERS: [FLS/RLS/scope filters applied]
  ENV-TIER: [dev | test | production]
```

One PARAM-SET block per Gap? = Y boundary from Step 8b.

---

### STEP 12 — FINDINGS

```
CATEGORY-DEFINITIONS:
AUTH — authentication or identity token failure
BOUNDARY — service boundary enforcement failure
CONTRACT — scope string or parameter contract mismatch
TIMEOUT — latency threshold exceeded or unprotected burst
STATE — precondition violation or state machine bypass
PERMISSION — FLS, RLS, or privilege escalation
```

| Finding # | Step | BC-N | Failure Mode | FAIL-CATEGORY | Severity |
|-----------|------|------|------------|--------------|---------|

Fill rules:
- FAIL-CATEGORY from closed vocabulary: AUTH · BOUNDARY · CONTRACT · TIMEOUT · STATE · PERMISSION
- No out-of-vocabulary values permitted
- Clean trace: Failure Mode = "No failures identified", FAIL-CATEGORY = N/A
- Severity: P1 (security/data loss) · P2 (incorrect behavior) · P3 (performance/latency) · P4 (observability/documentation)
