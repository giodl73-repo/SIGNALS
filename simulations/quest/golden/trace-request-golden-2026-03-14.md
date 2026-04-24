Written to `simulations/quest/golden/trace-request-golden-2026-03-14.md`.

Key decisions made in the extraction:

**Winning variation: V-05** — the only variation where both C-44 and C-45 pass simultaneously. The simplified prompt body in the quest run *is* V-05 stripped of research scaffolding.

**Score: 275/275** — scored against v18 rubric (the round's active rubric). Under v19, which promotes C-45 to a formal criterion, the same prompt body scores 280/280.

**What made it golden (5 patterns):**

1. **Two-role architecture** — Algorithm-Declarant / Platform Expert split makes Phase 0B a structural gate, not a prose instruction
2. **CONSISTENCY-RULE as fourth rule** — the axis V-01 and V-03 each deliberately omit; V-05 carries all four, enabling combined-axis coverage
3. **Three-phase Step 8b lifecycle** (8b-i arm collection / 8b-ii coherence assertion / 8b-iii contradiction detection) — makes the sequence machine-verifiable without holistic prose reading
4. **VALIDATION-DERIVATION as a named field** co-located with DECLARE CONTRADICTION before Step 8c — the exact co-location constraint C-45 tests
5. **Typed EVENT vocabulary** (`auth-check | routing | plugin-execution | ...`) — closes the vocabulary so Step 12 FAIL-CATEGORY traces back to typed events in the layer trace
`
TRACE CONTRACT:
HALT-EXPECTED-BOUNDARY: "[BC-N -- label]"
HALT-EXPECTED-CONDITION: "Step 8b prose asserts coherence for [BC-N label] AND Step 8c Match? = N for [BC-N label] row"
```

---

### PHASE 0B -- CHECKER ALGORITHM (Algorithm-Declarant)

```
CHECKER ALGORITHM:
MATCH-RULE: Step 8b prose coherence assertion aligns with Step 8c Match? = Y; mismatch fires when Step 8b asserts coherence AND Match? = N simultaneously
HALT-RULE: halt fires when Step 8b prose asserts coherence for HALT-EXPECTED-BOUNDARY AND Step 8c Match? = N for HALT-EXPECTED-BOUNDARY row
OUTPUT-RULE: Row-Verdict = HALT when HALT-RULE conditions simultaneously hold; Row-Verdict = PASS otherwise
CONSISTENCY-RULE: matches HALT-EXPECTED-BOUNDARY: yes -> TRACE CONTRACT validation -> "Contract prediction confirmed" | matches HALT-EXPECTED-BOUNDARY: no -> TRACE CONTRACT validation -> "falsified -- actual halt boundary was [BC-N label]"
```

Reproduce CHECKER ALGORITHM verbatim at Step 8 Header -- all four rules.

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

Severity: P1 (critical) / P2 (high) / P3 (medium) / P4 (low)

---

## What Made It Golden

**1. Two-role architecture enforces pre-trace algorithm commitment.**
The Algorithm-Declarant / Platform Expert split makes Phase 0B a dedicated pre-trace gate. The Algorithm-Declarant's sole job is the four-rule declaration. This eliminates the structural failure mode where CHECKER ALGORITHM appears mid-trace or is assembled lazily -- the role boundary is the enforcement mechanism, not prose instruction alone.

**2. CONSISTENCY-RULE as fourth rule enables combined-axis coverage.**
V-01 (phrasing register) and V-03 (output format) each achieve C-45 PASS but explicitly omit CONSISTENCY-RULE, producing C-44 FAIL by design. V-05 carries all four rules, allowing C-44 and C-45 to coexist. The two criteria are complementary surfaces: CONSISTENCY-RULE encodes derivation pre-trace in the algorithm block; VALIDATION-DERIVATION surfaces it inline at contradiction-fire point. V-05 is the first variation where both pass simultaneously.

**3. Three-phase Step 8b lifecycle makes the contradiction-detection sequence machine-verifiable.**
Splitting Step 8b into 8b-i (arm collection), 8b-ii (coherence assertion), and 8b-iii (contradiction detection) creates named sub-step boundaries. A checker does not need to read prose holistically -- it can verify that 8b-ii fires before 8b-iii and that DECLARE CONTRADICTION appears only in 8b-iii. The contradiction event block is a structural artifact of the lifecycle, not an embedded parenthetical.

**4. VALIDATION-DERIVATION as a named field in the EVENT: CONTRADICTION block.**
From V-03's output format pattern: VALIDATION-DERIVATION is a required named field co-located with DECLARE CONTRADICTION before Step 8c is populated. This co-location constraint is what C-45 tests -- the derivation path is surfaced at contradiction-fire, not deferred to a summary section.

**5. Structured event blocks with typed EVENT vocabulary across Steps 1-7.**
The TYPE: [auth-check | routing | plugin-execution | sql-operation | cache-op | response-assembly] closed vocabulary forces every processing event into a named category. This enables Step 12 FAIL-CATEGORY alignment: every finding traces back to a typed event in the layer trace. The structured field block pattern makes the gap between Step 8b prose and Step 8c tabular output mechanically auditable.

---

## Final Rubric Criteria Summary (v19)

**Rubric:** trace-request-rubric-v19-2026-03-14.md
**Total:** 280 pts | **Golden threshold:** 224/280 (80%) | **All 4 essential criteria required: PASS**

| Tier | Criteria | Max pts | Notes |
|------|----------|---------|-------|
| Essential | C-01 to C-04 | 60 | Boundary map, layer trace, failure point, remediation+severity |
| Recommended | C-05 to C-07 | 30 | Auth token chain, error path end-to-end, latency analysis |
| Aspirational (inherited) | C-08 to C-20 | 65 | Foundational structure, Step 8 header, VT-N vocabulary |
| Aspirational C-21 to C-43 | 23 criteria x 5 | 115 | Scope-string table, coherence check machinery, structured tokens |
| C-44 CONSISTENCY-RULE | 1 criterion x 5 | 5 | Fourth rule: derivation path encoded pre-trace in algorithm block |
| C-45 VALIDATION-DERIVATION | 1 criterion x 5 | 5 | Inline derivation token co-located with DECLARE CONTRADICTION in Step 8b |
| **Total** | | **280** | |

**C-44:** All four rules (MATCH-RULE / HALT-RULE / OUTPUT-RULE / CONSISTENCY-RULE) must be present in Phase 0B and reproduced verbatim at Step 8 Header. V-02 is the canonical stability axis for C-44.

**C-45:** VALIDATION-DERIVATION must appear as a named structural token in the EVENT: CONTRADICTION block (Step 8b-iii), co-located with DECLARE CONTRADICTION, before Step 8c is populated. Three independent axes confirmed: R19 V-03 (structured field blocks), R20 V-01 (phrasing register), R20 V-03 (output format). V-05 confirms combined-axis (C-44 + C-45 simultaneously).

**C-44 vs C-45 relationship:** Competing surfaces, not redundant. V-02 = C-44 PASS + C-45 suppressed (CONSISTENCY-RULE encodes derivation pre-trace; inline emission routed away by GATE-8B). V-01/V-03 = C-45 PASS + C-44 FAIL (inline derivation present; fourth rule absent by design). V-05 = both PASS (combined axis; Algorithm-Declarant commits four rules; structured block emits inline derivation).
