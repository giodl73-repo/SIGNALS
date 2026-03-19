You are a request tracing expert. Hand-compile a request through every service boundary,
API, and middleware layer from entry point to data layer and back. Declare the checker
algorithm before tracing. Work through every step in order.

---

### PHASE 0B -- CHECKER ALGORITHM (Algorithm-Declarant)

Declare this algorithm completely before proceeding to STEP 0.

```
CHECKER ALGORITHM:
MATCH-RULE: Step 8b prose coherence assertion aligns with Step 8c Match? = Y; mismatch fires when Step 8b asserts coherence AND Match? = N simultaneously
HALT-RULE: halt fires when Step 8b prose asserts coherence for HALT-EXPECTED-BOUNDARY AND Step 8c Match? = N for HALT-EXPECTED-BOUNDARY row
OUTPUT-RULE: Row-Verdict = HALT when HALT-RULE conditions simultaneously hold; Row-Verdict = PASS otherwise
CONSISTENCY-RULE: matches HALT-EXPECTED-BOUNDARY: yes -> TRACE CONTRACT validation -> "Contract prediction confirmed" | matches HALT-EXPECTED-BOUNDARY: no -> TRACE CONTRACT validation -> "falsified -- actual halt boundary was [BC-N label]"
```

```
TRACE CONTRACT:
HALT-EXPECTED-BOUNDARY: "[BC-N -- label]"
HALT-EXPECTED-CONDITION: "Step 8b prose asserts coherence for [BC-N label] AND Step 8c Match? = N for [BC-N label] row"
```

---

### STEP 0 -- BOUNDARY MAP (Platform Expert)

| BC-N | Boundary Name | Entry Side | Exit Side |
|------|--------------|-----------|----------|

Every boundary from entry to data layer and back. BC-N labels in crossing order.

---

### STEPS 1-7 -- LAYER TRACE

Each layer produces a structured field block:

```
LAYER: [name]
ENTRY: [what arrives]
PROCESSING-EVENTS:
  - EVENT: [event name]
    TYPE: [auth-check | routing | plugin-execution | sql-operation | cache-op | response-assembly]
    DETAIL: [specific token, schema, stored proc, plugin method, or API invoked]
    RESULT: [pass | fail | transform -- specific]
EXIT: [what departs]
LATENCY: [estimate in ms] | DOMINANT-CONTRIBUTOR: [operation adding most latency]
FAILURE-MODES:
  - FM: [error condition]
    CODE: [HTTP status or platform error type]
    TRIGGER: [what causes this failure]
```

---

### STEP 8 HEADER

Reproduce CHECKER ALGORITHM verbatim -- all four rules -- before the Step 8a table.

```
CHECKER ALGORITHM:
MATCH-RULE: ...
HALT-RULE: ...
OUTPUT-RULE: ...
CONSISTENCY-RULE: ...
TOKEN-COUNT: [N]
VT-1: "[scope string for BC-1]"
VT-2: "[scope string for BC-2]"
...
```

---

### STEP 8a -- SCOPE-STRING TABLE

| BC-N | Boundary Name | Scope String | Source Step | Gap? |
|------|--------------|--------------|-------------|------|

---

### STEP 8b -- COHERENCE CHECK (three-phase lifecycle)

For each Gap?=Y boundary, execute three explicit sub-steps:

**8b-i -- ARM COLLECTION:** Collect the three coherence arms for this boundary:
- ARM-1 (Step3-Auth): [auth token / scope claim from Step 3]
- ARM-2 (Step8a-Invoked): [scope string from Step 8a table]
- ARM-3 (Step11-Params): [param-set from Step 11]

**8b-ii -- COHERENCE ASSERTION:** State whether the three arms are coherent. Prose assertion required.

**8b-iii -- CONTRADICTION DETECTION:** If assertion is coherent AND Step 8c will produce Match? = N, fire:

```
EVENT: CONTRADICTION
DECLARE CONTRADICTION: [BC-N] -- [label] -- arm: [ARM that diverges]
matches HALT-EXPECTED-BOUNDARY: [yes/no]
VALIDATION-DERIVATION: [derive outcome from matches value at point of emission: "yes" -> "Contract prediction confirmed"; "no" -> "falsified -- actual halt boundary was [BC-N label]"]
```

---

### STEP 8c -- COHERENCE TABLE

| BC-N | Step3-Auth | Step8a-Invoked | Step11-Params | Match? | Row-Verdict |
|------|-----------|---------------|---------------|--------|-------------|

CHECK RESULT: [HALT / PASS -- with boundary label if HALT]
TRACE CONTRACT validation: [Contract prediction confirmed / falsified -- actual halt boundary was [BC-N label]]

---

### STEP 9 -- ERROR PATH

```
ERROR-SOURCE: [BC-N -- label]
PROPAGATION: [layer sequence]
CALLER-RECEIVES: [HTTP status + body]
LATENCY-IMPACT: [added ms]
```

---

### STEP 10 -- LATENCY SUMMARY

| Layer | Latency (ms) | Dominant Contributor |
|-------|-------------|---------------------|

---

### STEP 11 -- PARAM-SET BLOCKS

One PARAM-SET block per Gap?=Y boundary:

```
PARAM-SET: [BC-N -- label]
REQUIRED: [param list]
OPTIONAL: [param list]
MISSING: [what the caller omitted]
```

---

### STEP 12 -- FINDINGS TABLE

```
CATEGORY-DEFINITIONS:
AUTH-GAP: missing or mismatched auth token / scope claim
SCHEMA-MISMATCH: entity shape divergence between layers
PLUGIN-FAULT: plugin pre/post execution failure
PARAM-MISSING: required parameter absent from call
ROUTING-ERROR: request dispatched to wrong endpoint or service
LATENCY-RISK: operation exceeds SLA threshold
```

| # | Layer | Finding | Severity | FAIL-CATEGORY | Remediation |
|---|-------|---------|----------|---------------|-------------|

Severity: P1 (critical) / P2 (high) / P3 (medium) / P4 (low)

Write artifact to: signals/simulate/request/{{topic}}-request-{{date}}.md
If --output <path> provided: write to <path>/{topic}-{skill}-{date}.md (flat, no namespace prefix).
Include frontmatter: skill: simulate-request, topic: {{topic}}, date: {{date}}
