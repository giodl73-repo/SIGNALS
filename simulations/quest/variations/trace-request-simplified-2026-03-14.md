Now I have everything I need. The full file contains 5 experimental variations (V-01 through V-05) plus meta-commentary. V-05 is the "candidate ceiling variation" designed for maximum coverage (both C-44 and C-45 pass). The minimal golden prompt = V-05 stripped of all research scaffolding.

---

## Simplified Prompt Body

```
You are running a trace-request signal for: {{topic}}

---

### EXECUTION ROLES

**ROLE 1 — ALGORITHM-DECLARANT:** Runs Phase 0B only. Declares the full four-rule CHECKER ALGORITHM before the Platform Expert gathers any boundary evidence.

**ROLE 2 — PLATFORM EXPERT:** Runs Phase 0A and Steps 0–12. Auto-selected from {{topic}} context:
- **Dataverse Platform Engineer** — Dataverse Web API, OData, plugin pipeline, entity operations, FLS/RLS, Entra auth
- **Commerce Service Unit (CSU) Engineer** — CSU APIs, catalog, pricing, order management, checkout, cart
- **Power Automate Backend Engineer** — flow execution, connector calls, action invocations, trigger evaluation

State Platform Expert selection before Phase 0A.

---

### PHASE 0A — TRACE CONTRACT (Platform Expert)

​```
TRACE CONTRACT:
HALT-EXPECTED-BOUNDARY: "[BC-N -- label]"
HALT-EXPECTED-CONDITION: "Step 8b prose asserts coherence for [BC-N label] AND Step 8c Match? = N for [BC-N label] row"
​```

---

### PHASE 0B — CHECKER ALGORITHM (Algorithm-Declarant)

​```
CHECKER ALGORITHM:
MATCH-RULE: Step 8b prose coherence assertion aligns with Step 8c Match? = Y; mismatch fires when Step 8b asserts coherence AND Match? = N simultaneously
HALT-RULE: halt fires when Step 8b prose asserts coherence for HALT-EXPECTED-BOUNDARY AND Step 8c Match? = N for HALT-EXPECTED-BOUNDARY row
OUTPUT-RULE: Row-Verdict = HALT when HALT-RULE conditions simultaneously hold; Row-Verdict = PASS otherwise
CONSISTENCY-RULE: matches HALT-EXPECTED-BOUNDARY: yes → TRACE CONTRACT validation → "Contract prediction confirmed" | matches HALT-EXPECTED-BOUNDARY: no → TRACE CONTRACT validation → "falsified -- actual halt boundary was [BC-N label]"
​```

Reproduce CHECKER ALGORITHM verbatim at Step 8 Header — all four rules.

---

### STEP 0 — BOUNDARY MAP (Platform Expert)

| BC-N | Boundary Name | Entry Side | Exit Side |
|------|--------------|-----------|----------|

Every boundary from entry to data layer and back. BC-N labels in crossing order.

---

### STEPS 1–7 — LAYER TRACE

Each layer produces a structured field block:

​```
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
​```

---

### STEP 8 HEADER

​```
TOKEN-COUNT: [N]
VT-1: "[scope string for BC-1]"
VT-2: "[scope string for BC-2]"
... (one VT-N line per boundary in Step 0 — machine-parseable via ^VT-[0-9]+: ".*"$)
​```

[Reproduce CHECKER ALGORITHM verbatim — all four rules as declared in Phase 0B]

---

### STEP 8A — SCOPE STRING COLLECTION

| BC-N | Boundary Name | Scope String | Source Step | Gap? |
|------|--------------|-------------|------------|------|

---

### STEP 8B — COHERENCE EVENTS

Three sub-steps per Gap? = Y boundary. Sub-steps must not be collapsed.

**Sub-step 8b-i — Arm collection:**

​```
BOUNDARY: BC-N -- [label]
ARM-1 (Step3-Auth): [scope string]
ARM-2 (Step8a-Invoked): [scope string]
ARM-3 (Step11-Params): [param set]
​```

**Sub-step 8b-ii — Coherence assertion:**

​```
COHERENCE-ASSERTION: COHERENT | DIVERGENT
DIVERGENCE-DETAIL: [if DIVERGENT — name arm pair and conflict | if COHERENT — "all three arms align"]
​```

**Sub-step 8b-iii — Contradiction event:**

Execute when sub-step 8b-ii = COHERENT AND Step 8c Match? will be N. Populate before Step 8c is filled.

​```
DECLARE CONTRADICTION: BC-N -- [label] -- arm: [which arm is contradicted]
matches HALT-EXPECTED-BOUNDARY: [yes/no]
VALIDATION-DERIVATION: [yes → "Contract prediction confirmed" | no → "falsified -- actual halt boundary was [BC-N label]"]
​```

Substitution rules:
- All three fields required; a block with any field absent is structurally incomplete
- `matches HALT-EXPECTED-BOUNDARY` = yes iff this BC-N matches the boundary named in TRACE CONTRACT HALT-EXPECTED-BOUNDARY
- VALIDATION-DERIVATION derived from the matches boolean at sub-step 8b-iii emission using CONSISTENCY-RULE from CHECKER ALGORITHM

---

### STEP 8C — COHERENCE TABLE

| BC-N | Boundary | Step3-Auth | Step8a-Invoked | Step11-Params | Match? | Row-Verdict |
|------|---------|-----------|--------------|-------------|--------|------------|

Match? = Y iff all three arms consistent. Row-Verdict = HALT iff Match? = N for HALT-EXPECTED-BOUNDARY row.

​```
CHECK RESULT: [PASS/FAIL -- N rows, M HALT rows]
TRACE CONTRACT validation: [apply CONSISTENCY-RULE — confirm or falsify HALT-EXPECTED-BOUNDARY prediction]
​```

---

### STEP 9 — ERROR PATH

​```
ERROR-PATH:
  SOURCE: BC-N -- [label]
  PROPAGATION:
    - HOP: BC-N → BC-M | TRANSFORM: [error transformation at this hop]
  CALLER-RECEIVES:
    HTTP-STATUS: [code]
    ERROR-BODY: [structure]
    CORRELATION-ID: [present/absent]
  LATENCY-IMPACT: [added ms] | CONTRIBUTOR: [which hop]
​```

---

### STEP 10 — AUTHORIZATION GAPS

​```
AUTH-GAP:
  BOUNDARY: BC-N -- [label]
  CHECKED: [permission enforced]
  ASSUMED: [permission assumed, not verified]
  EXPLOITABLE-GAP: [what partial credentials enable | "none"]
​```

One AUTH-GAP block per boundary in Step 0.

---

### STEP 11 — PARAM SETS

​```
PARAM-SET:
  BOUNDARY: BC-N -- [label]
  TOKENS: [exact token claims in effect]
  ROLES: [role memberships]
  FILTERS: [FLS/RLS/scope filters applied]
  ENV-TIER: [dev | test | production]
​```

One PARAM-SET block per Gap? = Y boundary from Step 8b.

---

### STEP 12 — FINDINGS

​```
CATEGORY-DEFINITIONS:
AUTH — authentication or identity token failure
BOUNDARY — service boundary enforcement failure
CONTRACT — scope string or parameter contract mismatch
TIMEOUT — latency threshold exceeded or unprotected burst
STATE — precondition violation or state machine bypass
PERMISSION — FLS, RLS, or privilege escalation
​```

| Finding # | Step | BC-N | Failure Mode | FAIL-CATEGORY | Severity |
|-----------|------|------|------------|--------------|---------|

Fill rules:
- FAIL-CATEGORY from closed vocabulary: AUTH · BOUNDARY · CONTRACT · TIMEOUT · STATE · PERMISSION
- Clean trace: Failure Mode = "No failures identified", FAIL-CATEGORY = N/A
- Severity: P1 (security/data loss) · P2 (incorrect behavior) · P3 (performance/latency) · P4 (observability/documentation)
```

---

## Simplification Report

### What was removed and why

| Removed | Words | Why |
|---------|-------|-----|
| V-05 axis + hypothesis block | ~115 | Research scaffolding explaining WHY this variation was designed; no execution instruction |
| V-01 through V-04 complete variations | ~3,935 | The "complete golden prompt" contains 5 experimental variations; V-05 is the ceiling variation that passes both C-44 and C-45. The minimal prompt is one executable version. |
| Meta header (Round 20 variation map) | ~200 | Research notes on C-45 promotion path; nothing executable |
| "Two roles execute in fixed sequence. Both role declarations must be read before execution begins." | 15 | Redundant — the ROLE 1/ROLE 2 declarations make this obvious |
| "After Phase 0B, hands off to Platform Expert." | 8 | Redundant — ROLE 2 already states it runs Phase 0A and Steps 0–12 |
| "All four rules are required. A CHECKER ALGORITHM block with fewer than four named rules is structurally incomplete." | 18 | The 4-rule code block is the instruction; this meta-note is structural commentary that doesn't change what the executor produces |
| "Algorithm-Declarant hands off. Platform Expert reproduces..." → "Reproduce..." | 5 | "Algorithm-Declarant hands off." has no execution effect once we reach this line |
| "All boundaries from entry point... No boundary skipped." → "Every boundary... in crossing order." | 5 | "No boundary skipped" is covered by "Every boundary"; "in crossing order" already implies assignment order |
| "Required fields per layer:" | 4 | Implied by the following code block being the template |
| "Step 8b runs three sub-steps... Each sub-step produces its own structured field block." → "Three sub-steps..." | 14 | "Each sub-step produces its own structured field block" is shown by the blocks themselves |
| "block:" suffix on sub-step names ×3 | 3 | "Sub-step 8b-i — Arm collection" is unambiguous without "block:" |
| Execute condition wordiness | 6 | "produces COHERENT AND... for this boundary row" → "= COHERENT AND... will be N" |
| "are required in sub-step 8b-iii" | 4 | "All three fields required" is equivalent |
| "; no otherwise" | 2 | Implied negation already covered by "yes iff" |
| Substitution rule 3 tail: "the derivation is inline at sub-step 8b-iii, not deferred to the post-execution TRACE CONTRACT validation" | 17 | The sub-step structure already enforces inline placement; this is explanatory meta-commentary |
| "specific conflict" → "conflict" | 1 | One word shorter, same meaning |
| "No out-of-vocabulary values permitted" | 5 | Already covered by "closed vocabulary" in the same rule |

### Essential criteria check (YES — all pass)

| Criterion | Preserved? | Where |
|-----------|-----------|-------|
| C-01 Request path trace | YES | Steps 0–7 enumerate every boundary |
| C-02 Authorization gap analysis | YES | STEP 10 AUTH-GAP blocks |
| C-03 Failure point identification | YES | STEP 12 FINDINGS table |
| C-04 Error propagation path | YES | STEP 9 ERROR-PATH block |
| C-37 CHECKER ALGORITHM | YES | Phase 0B code block |
| C-38 HALT-RULE dual-surface encoding | YES | "Step 8b asserts coherence AND Step 8c Match? = N" |
| C-39 Pre-execution halt boundary | YES | Phase 0A TRACE CONTRACT |
| C-40 DECLARE CONTRADICTION prose token | YES | Sub-step 8b-iii block |
| C-41 Pre-trace CHECKER ALGORITHM + HALT-EXPECTED-BOUNDARY | YES | Phase 0B before Step 0 |
| C-42 matches HALT-EXPECTED-BOUNDARY field | YES | Sub-step 8b-iii DECLARE CONTRADICTION block |
| C-43 FAIL-CATEGORY closed vocabulary | YES | STEP 12 CATEGORY-DEFINITIONS + Fill rules |
| C-44 CONSISTENCY-RULE | YES | Fourth rule in CHECKER ALGORITHM |
| C-45 VALIDATION-DERIVATION inline | YES | Sub-step 8b-iii, before Step 8c |
| C-34 VT-N schema input | YES | TOKEN-COUNT + VT-N lines in STEP 8 HEADER |
| C-35 Row-level verdict token | YES | Row-Verdict column in STEP 8C |

### Word count comparison

**Comparison 1 (full file → single minimal prompt):**
- Original: ~5,230 words (5 variations + meta header + hypothesis blocks)
- Simplified: ~870 words
- Reduction: **83%** — the 5-variation research artifact is distilled to one executable prompt

**Comparison 2 (V-05 section only → simplified V-05):**
- Original V-05 (including hypothesis block, lines 834–1053): ~1,092 words
- Simplified: ~870 words
- Reduction: **20%** — within the 20–40% target

The 20-40% goal is meaningful at the V-05 level (one variation → minimal version of that variation). The full-file reduction exceeds the target because the original is a 5-way experimental file, not a single prompt.

```json
{"simplified_word_count": 870, "original_word_count": 5230, "all_essential_still_pass": true}
```
