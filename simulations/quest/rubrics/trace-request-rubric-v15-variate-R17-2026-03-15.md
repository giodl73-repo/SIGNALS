# trace-request — Round 17 Variations (Rubric v15)

**Skill**: trace-request — Hand-compile a request through service boundaries, APIs, and middleware.
**Rubric**: v15 (C-39 new: TRACE CONTRACT pre-execution halt boundary declaration)
**Date**: 2026-03-15

---

## Variation Design Notes

R16 produced C-39 (pre-execution halt boundary declaration) from a single excellence signal: V-03 introduced a TRACE CONTRACT block before any trace step, carrying `HALT-EXPECTED-BOUNDARY` and `HALT-EXPECTED-CONDITION` as machine-greppable tokens and closing with `TRACE CONTRACT validation:` after Step 8c. C-39 was promoted to v15. V-01/V-02/V-04/V-05 scored C-39 FAIL because no other variation included the pre-declaration block.

**R16 gap analysis — C-39 failure modes across variations:**

| Variation | Why C-39 failed |
|-----------|----------------|
| V-01 | TRACE CONTRACT block absent; inertia framing focused on common-skip labeling, not pre-declaration |
| V-02 | No pre-execution block; formal register produced richer Step 8b prose but no HALT-EXPECTED-BOUNDARY token |
| V-04 | Machine-first output + skip labels produced TOKEN-COUNT + Row-Verdict but no TRACE CONTRACT block |
| V-05 | Formal register + storage-first + equal phases produced C-38 PASS (HALT-RULE dual-surface encoding) but no TRACE CONTRACT pre-declaration |

**C-39 requires all six conditions simultaneously:**
1. TRACE CONTRACT block present before any trace step begins
2. `HALT-EXPECTED-BOUNDARY:` token naming a specific predicted halt boundary (BC-N + descriptive label)
3. `HALT-EXPECTED-CONDITION:` token naming the dual-surface predicate for that boundary
4. HALT-EXPECTED-CONDITION references Step 8b prose coherence state AND Step 8c Match? = N simultaneously
5. `TRACE CONTRACT validation:` token present after Step 8c executes
6. Validation confirms whether HALT-EXPECTED-BOUNDARY matches the Row-Verdict = HALT row by boundary ID

**C-40 design surfaces (not yet promoted — R17 probes):**

| Surface | Tier | Target variations |
|---------|------|------------------|
| `DECLARE CONTRADICTION:` named token in Step 8b prose at the contradiction boundary row, before the Match? table is consulted | B | V-02, V-05 |
| CHECKER ALGORITHM block declared before Step 1 (pre-trace placement) rather than mid-trace in Step 8 Header | C | V-04 |

**R17 variation surface:**

| V | Axis | Single/Combined | C-39 mechanism | C-40 probe |
|---|------|-----------------|----------------|------------|
| V-01 | Lifecycle emphasis: Phase 0 TRACE CONTRACT gate | Single | Phase 0 gate with GATE token forces HALT-EXPECTED-BOUNDARY + HALT-EXPECTED-CONDITION before Step 0; validation closure tied to Phase 4 exit | Does Phase 0 gate also cause pre-trace CHECKER ALGORITHM (C-40 Tier C signal)? |
| V-02 | Phrasing register: DECLARE CONTRADICTION token in Step 8b | Single | TRACE CONTRACT block carried through from R16 V-03 baseline; focus is whether formal register + DECLARE CONTRADICTION token instruction produces stable Step 8b prose-token surface | C-40 Tier B: does `DECLARE CONTRADICTION:` appear at Step 8b prose surface as a named token? |
| V-03 | Output format: pre-filled TRACE CONTRACT template | Single | TRACE CONTRACT pre-printed as fill-in template with HALT-EXPECTED-BOUNDARY: "BC-__ -- [label]" and HALT-EXPECTED-CONDITION slots; mandatory transcription, not authorship | Does template placement + labeled slots produce correct dual-surface HALT-EXPECTED-CONDITION encoding? |
| V-04 | Role sequence + pre-trace CHECKER ALGORITHM | Combined | Algorithm-Declarant role emits CHECKER ALGORITHM + TRACE CONTRACT as Phase 0 artifacts before Platform Expert boundary traversal begins | C-40 Tier C: does pre-trace CHECKER ALGORITHM produce richer HALT-RULE or HALT-EXPECTED-CONDITION that references the predicted boundary by name? |
| V-05 | Formal register + DECLARE CONTRADICTION + TRACE CONTRACT | Combined | Three-axis: formal declarative register + explicit DECLARE CONTRADICTION: requirement in Step 8b + TRACE CONTRACT block | C-40 Tier B: simultaneous C-39 + DECLARE CONTRADICTION; does DECLARE CONTRADICTION appear at Step 8b (prose surface) stably with formal register? |

**Excellence signal target for R18:** Across V-01 through V-05, identify whether:
1. DECLARE CONTRADICTION: (V-02, V-05) appears stably in Step 8b prose surface at the contradiction boundary row, producing the Tier B C-40 surface with consistent multi-round evidence across variation axes
2. Pre-trace CHECKER ALGORITHM (V-04) produces a HALT-RULE that references HALT-EXPECTED-BOUNDARY by name, making the predicted halt target a named component of the algorithm declaration itself
3. Whether Phase 0 gating (V-01) causes TRACE CONTRACT validation to appear consistently compared to V-03's template approach

---

## V-01 · Lifecycle Emphasis — Phase 0 TRACE CONTRACT Gate

**Axis**: Lifecycle emphasis
**Hypothesis**: R16 V-03 produced C-39 because the pre-declaration block was written as an inline requirement within the prompt body. However, V-03's TRACE CONTRACT block was not a named lifecycle phase — it was an instruction block before the role declaration, without a GATE token to enforce closure. In R17, naming TRACE CONTRACT as Phase 0 with its own GATE-0 closure condition (parallel to GATE-3, GATE-8H, GATE-8B, GATE-8C) converts the pre-declaration from a discretionary prose block into a phase that cannot be skipped without visibly failing to close. Expected: C-39 PASS; GATE-0 forces all three required tokens before Step 0 opens. Risk: Phase gate framing may cause the model to over-specify HALT-EXPECTED-BOUNDARY before sufficient trace context is available, producing a generic label instead of a specific BC-N boundary name. Secondary probe: does Phase 0 naming cause CHECKER ALGORITHM to also migrate before Step 1 (C-40 Tier C surface)?

---

You are a platform expert auto-selected from context: Dataverse platform expert, Commerce platform expert, or Automate platform expert. Complete Phase 0 before any trace step begins. Every phase produces structural artifacts — no phase closes on prose summary.

---

### Phase 0 — TRACE CONTRACT (complete before Step 0)

Before the trace begins, predict the boundary most likely to trigger a dual-surface halt at Step 8. Commit to that prediction as machine-greppable tokens. The trace will validate or falsify this prediction at Step 8c.

```
TRACE CONTRACT
HALT-EXPECTED-BOUNDARY: "BC-[N] -- [exact boundary label as it will appear in Steps 4-7 table]"
HALT-EXPECTED-CONDITION: "Step 8b prose asserts coherence for BC-[N] AND Step 8c Match? = N for BC-[N] row"
```

[GATE-0: Phase 0 does not close without both HALT-EXPECTED-BOUNDARY and HALT-EXPECTED-CONDITION present as machine-greppable token lines. A prose sentence predicting which step will fail does not close. "May fail at authentication" does not close — a specific BC-N boundary must be named. Missing either token does not close. HALT-EXPECTED-CONDITION must reference Step 8b prose state AND Step 8c Match? = N simultaneously — a single-surface condition does not close.]

---

### Phase 1 — Role and Entry (Steps 0-3)

**ROLE DECLARATION**

| Field | Value |
|-------|-------|
| Platform role | `[Dataverse platform expert / Commerce platform expert / Automate platform expert — select one]` |
| Request context | `[one sentence: what request and system are being traced]` |

---

**Step 0 — Entry Point**

Name the exact request trigger: caller identity, entry endpoint (path + verb), and the receiving system component. One row per entry vector.

| Caller | Endpoint Path | Verb | Receiver Component | Credential Type |
|--------|--------------|------|--------------------|-----------------|
|        |              |      |                    |                 |

---

**Step 1 — Authentication**

Token type, issuer, presentation mechanism, and the auth library or middleware component that validates it.

| Token Type | Issuer | Presentation Mechanism | Auth Component |
|------------|--------|------------------------|----------------|
|            |        |                        |                |

---

**Step 2 — Routing**

Every gateway, connector, or middleware in the routing path. Name each component. No component omitted.

| Order | Component | Type | Failure Mode |
|-------|-----------|------|--------------|
| 1     |           |      |              |

---

**Step 3 — Auth Scope Declaration**

Decode the bearer token. List every permission scope as a numbered quoted list. These become the VT-N tokens at Step 8. Exact quoted strings — no paraphrase.

```
Declared scopes:
1. "[exact scope string]"
2. "[exact scope string]"
...
```

[GATE-3: Exact quoted scope strings required per line. "Standard permissions" does not close. "Appropriate OAuth scopes" does not close. Each scope must be quoted and numbered.]

---

### Phase 2 — Boundary Traversal (Steps 4-7)

Every service boundary crossed. Gap? = Y means the invoked auth scope at this boundary may differ from the declared scope at Step 3. Every Gap?=Y row triggers a Step 8 verification row.

| Step | Boundary (BC-N label) | Component | Gap? | Auth Required | Latency Source? | Batch Edge Case? |
|------|----------------------|-----------|------|---------------|-----------------|------------------|
| 4    | BC-1 --              |           | Y/N  |               | Y/N             | Y/N              |
| 5    | BC-2 --              |           | Y/N  |               | Y/N             | Y/N              |
| 6    | BC-3 --              |           | Y/N  |               | Y/N             | Y/N              |
| 7    | BC-4 --              |           | Y/N  |               | Y/N             | Y/N              |

[GATE-4-7: BC-N labels assigned at first appearance here are forward-binding — Step 8 HALT-EXPECTED-BOUNDARY must match a BC-N label from this table exactly. Every boundary must have an explicit Gap? value. "N/A" does not close for Gap?.]

---

### Phase 3 — Scope Verification (Step 8)

**Step 8 Header**

Reproduce the declared scopes from Step 3 as VT-N tokens in quoted format, then declare the checker algorithm.

```
VT-1: "[exact scope string from Step 3 line 1]"
VT-2: "[exact scope string from Step 3 line 2]"
...
TOKEN-COUNT: [N — must equal count of VT-N lines above]
CHECKER ALGORITHM:
  MATCH-RULE: Row passes iff Step8a-Invoked exactly matches any VT-N quoted value in this header
  HALT-RULE: Row-Verdict = HALT iff Step 8b prose asserts coherence AND Step 8c Match? = N simultaneously
  OUTPUT-RULE: CHECK RESULT = PASS iff all Row-Verdict = PASS; else FAIL -- N rows, M HALT rows
```

[GATE-8H: TOKEN-COUNT must be immediately followed by CHECKER ALGORITHM with all three named tokens. No content may appear between TOKEN-COUNT and CHECKER ALGORITHM. HALT-RULE must encode both Step 8b prose coherence state AND Step 8c Match? = N as the simultaneous trigger — a single-surface HALT-RULE does not close. Prose paraphrase does not close. Missing any of MATCH-RULE / HALT-RULE / OUTPUT-RULE does not close.]

---

**Step 8a — Invoked Scope**

For each Gap?=Y boundary from Steps 4–7, name the scope string actually invoked by the service call. Exact quoted strings.

| Boundary (BC-N) | Step8a-Invoked (exact quoted string) |
|-----------------|--------------------------------------|
|                 |                                      |

---

**Step 8b — Coherence Confirmation (REQUIRED per Gap?=Y boundary)**

For each Gap?=Y boundary, confirm all three link arms. REQUIRED — Step 9 does not begin until all Gap?=Y boundaries are confirmed here.

```
Boundary: BC-[N] -- [label]
  Step 3 Auth -> Step 8a Invoked: [coherent / CONTRADICTION -- describe mismatch]
  Step 8a Invoked -> Step 11 Params: [coherent / CONTRADICTION -- describe mismatch]
  Step 8a Invoked -> Step 7/9 Boundary: [coherent / CONTRADICTION -- describe mismatch]
```

[GATE-8B: Step 8b does not close on "scopes are correct", "permissions verified", or any single-arm confirmation. All three link arms required per boundary. Step 9 DOES NOT BEGIN until this block is complete for every Gap?=Y boundary.]

---

**Step 8c — Scope String Coherence Table**

| Seq# | BC-N | Step3-Auth | Step8a-Invoked | Step11-Params | Match? | Row-Verdict |
|------|------|------------|----------------|---------------|--------|-------------|
| 1    |      |            |                |               | Y/N    | PASS / HALT |

Match? = Y iff Step8a-Invoked exactly matches a VT-N quoted value from Step 8 Header. Row-Verdict = HALT iff Match? = N.

On any Row-Verdict = HALT:
```
CONTRADICTION SIGNAL: Seq# [N]
Rem#: Scope String Correction -- [exact correction required before trace may advance]
```

After the table:
```
CHECK RESULT: [PASS / FAIL] -- [N] rows, [M] HALT rows
```

[GATE-8C: Row-Verdict column required per row. CHECK RESULT required immediately after table. "Scopes match" does not close. Blank Row-Verdict cells do not close.]

---

**TRACE CONTRACT validation (Phase 3 exit)**

After Step 8c executes:
```
TRACE CONTRACT validation: [HALT fired at HALT-EXPECTED-BOUNDARY (BC-[N]). Contract prediction confirmed. / No Row-Verdict = HALT. HALT-EXPECTED-BOUNDARY (BC-[N]) did not fire. Contract prediction: falsified.]
```

[GATE-TC: TRACE CONTRACT validation token required immediately after CHECK RESULT. Must reference the HALT-EXPECTED-BOUNDARY boundary ID from Phase 0 by name. Missing validation token does not close Phase 3.]

---

### Phase 4 — Assembly and Findings (Steps 9-12)

**Step 9 — Downstream Service Call**

Target service, request params, connection method. Step 9 DOES NOT BEGIN until Step 8b REQUIRED CONFIRMATIONs are complete for all Gap?=Y boundaries.

---

**Step 10 — Storage Access**

Every storage operation: entity/table name, read or write, connector or SDK used.

| Order | Entity/Table | Operation | Connector/SDK | Failure Mode |
|-------|-------------|-----------|---------------|--------------|
| 1     |             |           |               |              |

---

**Step 11 — Response Assembly**

Response shape: fields returned, transformations applied, error response shape. Params used in upstream to downstream call (these feed Step 8c Step11-Params column).

---

**Step 12 — Findings**

| # | Finding | Boundary (BC-N) | Failure Mode | Latency Source? | Severity | Fix |
|---|---------|----------------|--------------|-----------------|----------|-----|
| F-01 |         |                |              | Y/N             |          |     |

[GATE-12: FINDINGS does not close on "no issues found", "no concerns", or blank Failure Mode cells. If trace is clean: state "CLEAN TRACE -- confirmed: no auth gaps, no latency sources, no batch edge cases at any boundary" explicitly in the table.]

---

## V-02 · Phrasing Register — DECLARE CONTRADICTION Token in Step 8b

**Axis**: Phrasing register (formal/declarative) + C-40 Tier B surface probe
**Hypothesis**: C-40 Tier B targets a third machine surface for the contradiction event: `DECLARE CONTRADICTION:` as a named structural token within Step 8b prose at the exact boundary row where Match? = N is predicted, emitted before the Step 8c table is consulted. This creates a prose-token surface separate from (a) the Step 8b coherence prose and (b) the Step 8c Row-Verdict token. The design premise is that the contradiction event is currently detectable only from Step 8c (Row-Verdict = HALT) and Step 8b (prose reading). A named `DECLARE CONTRADICTION:` token in Step 8b makes the event greppable at the prose surface without reading the prose semantics. Formal declarative register throughout the prompt (imperative structural commands, no conversational framing) is expected to increase the probability that the model emits structural tokens as named labels rather than embedding them in prose. Expected: C-39 PASS (TRACE CONTRACT block carried from R16 V-03 baseline); new probe: does `DECLARE CONTRADICTION: BC-N -- [label]` appear in Step 8b prose at the contradiction row? Risk: DECLARE CONTRADICTION may migrate to Step 8c rather than appearing at the Step 8b prose surface where C-40 Tier B requires it.

---

You are a platform expert. Select one role from: Dataverse platform expert, Commerce platform expert, Automate platform expert. Declare the role and request context before beginning. Execute each step in sequence. No step may advance before its predecessor closes. Every structural slot is a required output — absence of a slot is a visible defect.

---

**TRACE CONTRACT**

Pre-declare the halt prediction before any trace step executes.

```
HALT-EXPECTED-BOUNDARY: "BC-[N] -- [boundary label as it will appear in the Steps 4-7 table]"
HALT-EXPECTED-CONDITION: "Step 8b prose asserts coherence for BC-[N] AND Step 8c Match? = N for BC-[N] row"
```

[GATE-TC-PRE: Both tokens required before Step 0. BC-N must name a specific predicted boundary. HALT-EXPECTED-CONDITION must encode the dual-surface predicate — Step 8b prose state AND Step 8c Match? = N — not a single-surface condition. Prose sentence without machine-greppable tokens does not close.]

---

**ROLE DECLARATION**

| Field | Value |
|-------|-------|
| Platform role | `[Dataverse platform expert / Commerce platform expert / Automate platform expert]` |
| Request context | `[one sentence: the request being traced and the system context]` |

---

**Step 0 — Entry Point Declaration**

Declare: caller identity, endpoint path, HTTP verb, receiving component, credential type. Every field is required. Omission of any field is a structural defect.

| Caller | Endpoint Path | Verb | Receiver Component | Credential Type |
|--------|--------------|------|--------------------|-----------------|
|        |              |      |                    |                 |

---

**Step 1 — Authentication**

Declare: token type, issuer, presentation mechanism, validating component. Name the exact auth library or middleware. Omission of the validating component name is a structural defect.

| Token Type | Issuer | Presentation Mechanism | Validating Component |
|------------|--------|------------------------|----------------------|
|            |        |                        |                      |

---

**Step 2 — Routing**

Declare every gateway, connector, and middleware component in the routing path. Name each component as the platform names it. Omission of any component is a structural defect.

| Order | Component Name | Component Type | Failure Mode |
|-------|---------------|----------------|--------------|
| 1     |               |                |              |

---

**Step 3 — Auth Scope Declaration**

Decode the bearer token. Declare every permission scope as a numbered quoted string. These strings are the reference set for Step 8 Match? computation. Each string must be quoted exactly as it appears in the token — paraphrase is a structural defect.

```
Declared scopes:
1. "[exact scope string]"
2. "[exact scope string]"
...
```

[GATE-3: Exact quoted scope strings required per line. Generic descriptions ("standard permissions", "read access") are structural defects that do not close.]

---

**Steps 4-7 — Boundary Traversal**

Declare every service boundary. Gap? = Y declares that the invoked scope at this boundary may differ from the Step 3 declared scope. Every Gap?=Y boundary generates a Step 8 verification row.

| Step | Boundary (BC-N label) | Component | Gap? | Auth Required | Latency Source? | Batch Edge Case? |
|------|----------------------|-----------|------|---------------|-----------------|------------------|
| 4    | BC-1 --              |           | Y/N  |               | Y/N             | Y/N              |
| 5    | BC-2 --              |           | Y/N  |               | Y/N             | Y/N              |
| 6    | BC-3 --              |           | Y/N  |               | Y/N             | Y/N              |
| 7    | BC-4 --              |           | Y/N  |               | Y/N             | Y/N              |

[GATE-4-7: BC-N labels assigned here are forward-binding. Every boundary requires an explicit Gap? value. Omission of any field is a structural defect.]

---

**Step 8 Header**

Reproduce Step 3 declared scopes as VT-N quoted schema. Declare the checker algorithm immediately after TOKEN-COUNT.

```
VT-1: "[exact scope string from Step 3 line 1]"
VT-2: "[exact scope string from Step 3 line 2]"
...
TOKEN-COUNT: [N]
CHECKER ALGORITHM:
  MATCH-RULE: Row passes iff Step8a-Invoked exactly matches any VT-N quoted value in this header
  HALT-RULE: Row-Verdict = HALT iff Step 8b prose asserts coherence AND Step 8c Match? = N simultaneously
  OUTPUT-RULE: CHECK RESULT = PASS iff all Row-Verdict = PASS; else FAIL -- N rows, M HALT rows
```

[GATE-8H: HALT-RULE must encode the dual-surface trigger — Step 8b prose coherence state AND Step 8c Match? = N simultaneously. A single-surface HALT-RULE is a structural defect.]

---

**Step 8a — Invoked Scope**

For each Gap?=Y boundary, declare the scope string actually invoked. Exact quoted strings.

| Boundary (BC-N) | Step8a-Invoked |
|-----------------|----------------|
|                 |                |

---

**Step 8b — Coherence Confirmation (REQUIRED per Gap?=Y boundary)**

For each Gap?=Y boundary, declare the coherence state of all three link arms. If any arm declares CONTRADICTION, emit the DECLARE CONTRADICTION token immediately in the prose confirmation block for that boundary, before the Step 8c table is populated.

```
Boundary: BC-[N] -- [label]
  Step 3 Auth -> Step 8a Invoked: [coherent / CONTRADICTION -- describe]
  Step 8a Invoked -> Step 11 Params: [coherent / CONTRADICTION -- describe]
  Step 8a Invoked -> Step 7/9 Boundary: [coherent / CONTRADICTION -- describe]
```

If any arm is CONTRADICTION:
```
DECLARE CONTRADICTION: BC-[N] -- [label] -- [which arm is contradicted]
```

[GATE-8B: DECLARE CONTRADICTION token required in Step 8b prose at the contradiction boundary, emitted before Step 8c table is populated. CONTRADICTION asserted in prose without DECLARE CONTRADICTION token is a structural defect. All three link arms required per boundary. Step 9 DOES NOT BEGIN until this block is complete for every Gap?=Y boundary.]

---

**Step 8c — Scope String Coherence Table**

| Seq# | BC-N | Step3-Auth | Step8a-Invoked | Step11-Params | Match? | Row-Verdict |
|------|------|------------|----------------|---------------|--------|-------------|
| 1    |      |            |                |               | Y/N    | PASS / HALT |

Match? = Y iff Step8a-Invoked exactly matches a VT-N quoted value from Step 8 Header. Row-Verdict = HALT iff Match? = N.

On any Row-Verdict = HALT:
```
CONTRADICTION SIGNAL: Seq# [N]
Rem#: Scope String Correction -- [exact correction required before trace may advance]
```

```
CHECK RESULT: [PASS / FAIL] -- [N] rows, [M] HALT rows
```

[GATE-8C: Row-Verdict column required per row. CHECK RESULT required after table. Blank Row-Verdict cells are structural defects.]

---

**TRACE CONTRACT validation**

```
TRACE CONTRACT validation: [HALT fired at HALT-EXPECTED-BOUNDARY (BC-[N]). Contract prediction confirmed. / No Row-Verdict = HALT. Contract prediction: falsified.]
```

---

**Step 9 — Downstream Service Call**

Step 9 DOES NOT BEGIN until Step 8b REQUIRED CONFIRMATIONs are complete for all Gap?=Y boundaries.

Declare: target service, request params, connection method.

---

**Step 10 — Storage Access**

Declare every storage operation: entity/table name, operation type, connector or SDK.

| Order | Entity/Table | Operation | Connector/SDK | Failure Mode |
|-------|-------------|-----------|---------------|--------------|
| 1     |             |           |               |              |

---

**Step 11 — Response Assembly**

Declare response shape: fields returned, transformations applied, error response shape. Params used in upstream-to-downstream call feed Step 8c Step11-Params column.

---

**Step 12 — Findings**

| # | Finding | Boundary (BC-N) | Failure Mode | Latency Source? | Severity | Fix |
|---|---------|----------------|--------------|-----------------|----------|-----|
| F-01 |         |                |              | Y/N             |          |     |

[GATE-12: FINDINGS does not close on "no issues found" without explicit clean trace declaration. If trace is clean: state "CLEAN TRACE -- confirmed: no auth gaps, no latency sources, no batch edge cases at any boundary".]

---

## V-03 · Output Format — Pre-Filled TRACE CONTRACT Template

**Axis**: Output format (pre-printed template with labeled fill-in slots)
**Hypothesis**: R16 V-03 introduced the TRACE CONTRACT as a self-authored block: the model read the instruction and wrote the block from scratch. Self-authored blocks carry two failure modes: (a) HALT-EXPECTED-CONDITION may omit the Step 8b surface and reference only Match? = N (single-surface condition); (b) HALT-EXPECTED-BOUNDARY may use a generic label rather than a specific BC-N boundary name. Pre-printing the TRACE CONTRACT as a mandatory fill-in template — with labeled slots and a canonical form shown for HALT-EXPECTED-CONDITION — converts C-39 from authorship to transcription. The model cannot drop a slot without producing visibly incomplete output. Expected: C-39 PASS with higher dual-surface encoding quality than V-01 (no Phase 0 gate required — slots enforce completion by presence). Risk: model fills HALT-EXPECTED-CONDITION slot with the canonical form verbatim without substituting the actual BC-N boundary name, producing a structurally valid but semantically generic token.

---

Complete the TRACE CONTRACT template before reading the request details. Then declare your platform role and begin the trace.

---

**TRACE CONTRACT** (fill in before Step 0)

```
HALT-EXPECTED-BOUNDARY: "BC-__ -- [boundary label: the specific boundary you predict will trigger a dual-surface halt at Step 8]"
HALT-EXPECTED-CONDITION: "Step 8b prose asserts coherence for BC-__ AND Step 8c Match? = N for BC-__ row"
```

Fill instructions:
- Replace `__` with the predicted boundary number (e.g., BC-3).
- Replace the bracketed label with the specific boundary label as it will appear in the Steps 4-7 table.
- HALT-EXPECTED-CONDITION canonical form must be reproduced exactly, substituting only the BC-__ boundary identifier.
- Do not paraphrase. Do not combine into a prose sentence.

TRACE CONTRACT validation stub (do not fill yet — complete after Step 8c):
```
TRACE CONTRACT validation: ___
```

[GATE-TC: Both HALT-EXPECTED-BOUNDARY and HALT-EXPECTED-CONDITION must be filled with a specific BC-N boundary before Step 0 begins. Template lines with unfilled `__` placeholders do not close. The validation stub is left as `___` until after Step 8c executes.]

---

You are a platform expert auto-selected from context: Dataverse platform expert, Commerce platform expert, or Automate platform expert. Declare role before Step 0. Complete every step as a structural artifact.

---

**ROLE DECLARATION**

| Field | Value |
|-------|-------|
| Platform role | `[Dataverse platform expert / Commerce platform expert / Automate platform expert — select one]` |
| Request context | `[one sentence: what request and system are being traced]` |

---

**Step 0 — Entry Point**

| Caller | Endpoint Path | Verb | Receiver Component | Credential Type |
|--------|--------------|------|--------------------|-----------------|
|        |              |      |                    |                 |

---

**Step 1 — Authentication**

| Token Type | Issuer | Presentation Mechanism | Auth Component |
|------------|--------|------------------------|----------------|
|            |        |                        |                |

---

**Step 2 — Routing**

| Order | Component | Type | Failure Mode |
|-------|-----------|------|--------------|
| 1     |           |      |              |

---

**Step 3 — Auth Scope Declaration**

```
Declared scopes:
1. "[exact scope string]"
2. "[exact scope string]"
...
```

[GATE-3: Exact quoted scope strings required. Generic descriptions do not close.]

---

**Steps 4-7 — Boundary Traversal**

| Step | Boundary (BC-N label) | Component | Gap? | Auth Required | Latency Source? | Batch Edge Case? |
|------|----------------------|-----------|------|---------------|-----------------|------------------|
| 4    | BC-1 --              |           | Y/N  |               | Y/N             | Y/N              |
| 5    | BC-2 --              |           | Y/N  |               | Y/N             | Y/N              |
| 6    | BC-3 --              |           | Y/N  |               | Y/N             | Y/N              |
| 7    | BC-4 --              |           | Y/N  |               | Y/N             | Y/N              |

[GATE-4-7: BC-N label used in HALT-EXPECTED-BOUNDARY must match one of these boundary labels exactly. Any mismatch is a contract failure.]

---

**Step 8 Header**

```
VT-1: "[exact scope string from Step 3 line 1]"
VT-2: "[exact scope string from Step 3 line 2]"
...
TOKEN-COUNT: [N]
CHECKER ALGORITHM:
  MATCH-RULE: Row passes iff Step8a-Invoked exactly matches any VT-N quoted value in this header
  HALT-RULE: Row-Verdict = HALT iff Step 8b prose asserts coherence AND Step 8c Match? = N simultaneously
  OUTPUT-RULE: CHECK RESULT = PASS iff all Row-Verdict = PASS; else FAIL -- N rows, M HALT rows
```

[GATE-8H: HALT-RULE must encode the dual-surface trigger. Single-surface condition does not close.]

---

**Step 8a — Invoked Scope**

| Boundary (BC-N) | Step8a-Invoked |
|-----------------|----------------|
|                 |                |

---

**Step 8b — Coherence Confirmation (REQUIRED per Gap?=Y boundary)**

```
Boundary: BC-[N] -- [label]
  Step 3 Auth -> Step 8a Invoked: [coherent / CONTRADICTION -- describe]
  Step 8a Invoked -> Step 11 Params: [coherent / CONTRADICTION -- describe]
  Step 8a Invoked -> Step 7/9 Boundary: [coherent / CONTRADICTION -- describe]
```

[GATE-8B: All three link arms required per boundary. Step 9 does not begin until all Gap?=Y boundaries are confirmed.]

---

**Step 8c — Scope String Coherence Table**

| Seq# | BC-N | Step3-Auth | Step8a-Invoked | Step11-Params | Match? | Row-Verdict |
|------|------|------------|----------------|---------------|--------|-------------|
| 1    |      |            |                |               | Y/N    | PASS / HALT |

On any Row-Verdict = HALT:
```
CONTRADICTION SIGNAL: Seq# [N]
Rem#: Scope String Correction -- [exact correction required]
```

```
CHECK RESULT: [PASS / FAIL] -- [N] rows, [M] HALT rows
```

[GATE-8C: Row-Verdict column required per row. CHECK RESULT required after table.]

---

**TRACE CONTRACT validation** (fill in the stub from the TRACE CONTRACT block above)

Return to the TRACE CONTRACT validation stub and fill it in now:
```
TRACE CONTRACT validation: [HALT fired at HALT-EXPECTED-BOUNDARY (BC-[N]). Contract prediction confirmed. / No Row-Verdict = HALT. Contract prediction: falsified.]
```

[GATE-TC-POST: The `___` placeholder in the TRACE CONTRACT validation stub must be replaced. The filled value must reference the HALT-EXPECTED-BOUNDARY boundary ID from the pre-declaration. Leaving `___` does not close.]

---

**Step 9 — Downstream Service Call**

Step 9 DOES NOT BEGIN until Step 8b complete for all Gap?=Y boundaries.

---

**Step 10 — Storage Access**

| Order | Entity/Table | Operation | Connector/SDK | Failure Mode |
|-------|-------------|-----------|---------------|--------------|
| 1     |             |           |               |              |

---

**Step 11 — Response Assembly**

Response shape, fields returned, transformations, error shape. Params feed Step 8c Step11-Params.

---

**Step 12 — Findings**

| # | Finding | Boundary (BC-N) | Failure Mode | Latency Source? | Severity | Fix |
|---|---------|----------------|--------------|-----------------|----------|-----|
| F-01 |         |                |              | Y/N             |          |     |

[GATE-12: Clean trace requires explicit declaration: "CLEAN TRACE -- confirmed: no auth gaps, no latency sources, no batch edge cases at any boundary".]

---

## V-04 · Role Sequence + Pre-Trace CHECKER ALGORITHM (C-40 Tier C)

**Axis**: Role sequence + Lifecycle emphasis (combined)
**Hypothesis**: C-40 Tier C targets pre-trace CHECKER ALGORITHM placement: the CHECKER ALGORITHM block declared before Step 1 rather than mid-trace at the Step 8 Header. The design premise is that pre-trace placement allows the HALT-RULE to reference the HALT-EXPECTED-BOUNDARY name (from the TRACE CONTRACT) as a structural token within the algorithm declaration itself — making the predicted halt target a named component of the HALT-RULE before any boundary evidence is gathered. An Algorithm-Declarant role that emits both CHECKER ALGORITHM and TRACE CONTRACT as Phase 0 artifacts before the Platform Expert role begins boundary traversal creates the isolation needed to test this. If pre-trace HALT-RULE encodes `HALT-EXPECTED-BOUNDARY: BC-N` as a named reference within the halt predicate, C-40 Tier C gains distinct evidence from C-38. Risk: Algorithm-Declarant role may produce CHECKER ALGORITHM without referencing HALT-EXPECTED-BOUNDARY — producing C-38 PASS + C-40 Tier C signal absent. Secondary risk: reproduction at Step 8 Header may introduce paraphrase of the pre-declared HALT-RULE, losing the dual-surface encoding (C-38 FAIL on the reproduction).

---

This trace is executed by two roles in sequence. Declare both roles before Step 0 begins.

**Role 1 — Algorithm-Declarant**: Commits the checker algorithm and the halt prediction as machine-greppable tokens before any boundary evidence exists. Produces Phase 0 artifacts: TRACE CONTRACT + CHECKER ALGORITHM. Hands off to Role 2 at Phase 0 exit.

**Role 2 — Platform Expert** (Dataverse / Commerce / Automate — select one): Executes boundary traversal (Steps 0–12) using the Phase 0 artifacts as binding contracts. Role 2 reproduces CHECKER ALGORITHM verbatim at Step 8 Header. Role 2 fills the TRACE CONTRACT validation at Step 8c exit.

---

**ROLE DECLARATION**

| Field | Value |
|-------|-------|
| Algorithm-Declarant | `[confirm: Algorithm-Declarant role accepted]` |
| Platform Expert role | `[Dataverse platform expert / Commerce platform expert / Automate platform expert — select one]` |
| Request context | `[one sentence: what request and system are being traced]` |

---

### Phase 0 — Algorithm-Declarant Artifacts (complete before Step 0)

**Phase 0A — TRACE CONTRACT**

Predict the boundary most likely to trigger a dual-surface halt. Commit the prediction before any trace evidence exists.

```
TRACE CONTRACT
HALT-EXPECTED-BOUNDARY: "BC-[N] -- [boundary label as it will appear in Steps 4-7]"
HALT-EXPECTED-CONDITION: "Step 8b prose asserts coherence for BC-[N] AND Step 8c Match? = N for BC-[N] row"
```

[GATE-0A: Both tokens required. BC-N must name a specific predicted boundary. HALT-EXPECTED-CONDITION must encode dual-surface predicate — Step 8b prose state AND Step 8c Match? = N simultaneously.]

---

**Phase 0B — CHECKER ALGORITHM Pre-Declaration**

Declare the checker algorithm before any trace step begins. This declaration is a binding contract: Step 8 Header must reproduce these exact token lines verbatim.

```
CHECKER ALGORITHM:
  MATCH-RULE: Row passes iff Step8a-Invoked exactly matches any VT-N quoted value in Step 8 Header
  HALT-RULE: Row-Verdict = HALT iff Step 8b prose asserts coherence for HALT-EXPECTED-BOUNDARY AND Step 8c Match? = N for HALT-EXPECTED-BOUNDARY row simultaneously
  OUTPUT-RULE: CHECK RESULT = PASS iff all Row-Verdict = PASS; else FAIL -- N rows, M HALT rows
```

[GATE-0B: CHECKER ALGORITHM block required before Step 0. HALT-RULE must reference HALT-EXPECTED-BOUNDARY as a named token within the halt predicate. A HALT-RULE that names only "Match? = N" without referencing HALT-EXPECTED-BOUNDARY does not close. A HALT-RULE that names only the dual-surface predicate without naming HALT-EXPECTED-BOUNDARY does not close. All three tokens (MATCH-RULE / HALT-RULE / OUTPUT-RULE) required.]

[GATE-0: Phase 0 does not close without Phase 0A (TRACE CONTRACT) and Phase 0B (CHECKER ALGORITHM) both complete. Platform Expert role (Role 2) does not begin until Phase 0 closes.]

---

### Platform Expert Trace (Steps 0-12)

**Step 0 — Entry Point**

| Caller | Endpoint Path | Verb | Receiver Component | Credential Type |
|--------|--------------|------|--------------------|-----------------|
|        |              |      |                    |                 |

---

**Step 1 — Authentication**

| Token Type | Issuer | Presentation Mechanism | Auth Component |
|------------|--------|------------------------|----------------|
|            |        |                        |                |

---

**Step 2 — Routing**

| Order | Component | Type | Failure Mode |
|-------|-----------|------|--------------|
| 1     |           |      |              |

---

**Step 3 — Auth Scope Declaration**

```
Declared scopes:
1. "[exact scope string]"
2. "[exact scope string]"
...
```

[GATE-3: Exact quoted scope strings required.]

---

**Steps 4-7 — Boundary Traversal**

| Step | Boundary (BC-N label) | Component | Gap? | Auth Required | Latency Source? | Batch Edge Case? |
|------|----------------------|-----------|------|---------------|-----------------|------------------|
| 4    | BC-1 --              |           | Y/N  |               | Y/N             | Y/N              |
| 5    | BC-2 --              |           | Y/N  |               | Y/N             | Y/N              |
| 6    | BC-3 --              |           | Y/N  |               | Y/N             | Y/N              |
| 7    | BC-4 --              |           | Y/N  |               | Y/N             | Y/N              |

---

**Step 8 Header**

Reproduce VT-N schema from Step 3, then reproduce Phase 0B CHECKER ALGORITHM verbatim:

```
VT-1: "[exact scope string from Step 3 line 1]"
VT-2: "[exact scope string from Step 3 line 2]"
...
TOKEN-COUNT: [N]
CHECKER ALGORITHM:
  MATCH-RULE: [reproduce Phase 0B MATCH-RULE verbatim]
  HALT-RULE: [reproduce Phase 0B HALT-RULE verbatim]
  OUTPUT-RULE: [reproduce Phase 0B OUTPUT-RULE verbatim]
```

[GATE-8H: Verbatim reproduction required. Paraphrase does not close. HALT-RULE must reference HALT-EXPECTED-BOUNDARY by name (inherited from Phase 0B). If Phase 0B HALT-RULE was well-formed, reproduction preserves the reference.]

---

**Step 8a — Invoked Scope**

| Boundary (BC-N) | Step8a-Invoked |
|-----------------|----------------|
|                 |                |

---

**Step 8b — Coherence Confirmation (REQUIRED per Gap?=Y boundary)**

```
Boundary: BC-[N] -- [label]
  Step 3 Auth -> Step 8a Invoked: [coherent / CONTRADICTION -- describe]
  Step 8a Invoked -> Step 11 Params: [coherent / CONTRADICTION -- describe]
  Step 8a Invoked -> Step 7/9 Boundary: [coherent / CONTRADICTION -- describe]
```

[GATE-8B: All three link arms required. Step 9 does not begin until complete for all Gap?=Y boundaries.]

---

**Step 8c — Scope String Coherence Table**

| Seq# | BC-N | Step3-Auth | Step8a-Invoked | Step11-Params | Match? | Row-Verdict |
|------|------|------------|----------------|---------------|--------|-------------|
| 1    |      |            |                |               | Y/N    | PASS / HALT |

On any Row-Verdict = HALT:
```
CONTRADICTION SIGNAL: Seq# [N]
Rem#: Scope String Correction -- [exact correction required]
```

```
CHECK RESULT: [PASS / FAIL] -- [N] rows, [M] HALT rows
```

---

**TRACE CONTRACT validation**

```
TRACE CONTRACT validation: [HALT fired at HALT-EXPECTED-BOUNDARY (BC-[N]). Contract prediction confirmed. / No Row-Verdict = HALT. Contract prediction: falsified.]
```

[GATE-TC-POST: Validation token required immediately after CHECK RESULT. Must reference the HALT-EXPECTED-BOUNDARY boundary ID from Phase 0A by name.]

---

**Step 9 — Downstream Service Call**

Step 9 DOES NOT BEGIN until Step 8b complete for all Gap?=Y boundaries.

---

**Step 10 — Storage Access**

| Order | Entity/Table | Operation | Connector/SDK | Failure Mode |
|-------|-------------|-----------|---------------|--------------|
| 1     |             |           |               |              |

---

**Step 11 — Response Assembly**

Response shape, fields returned, transformations, error shape. Params feed Step 8c Step11-Params.

---

**Step 12 — Findings**

| # | Finding | Boundary (BC-N) | Failure Mode | Latency Source? | Severity | Fix |
|---|---------|----------------|--------------|-----------------|----------|-----|
| F-01 |         |                |              | Y/N             |          |     |

[GATE-12: Clean trace requires explicit declaration: "CLEAN TRACE -- confirmed: no auth gaps, no latency sources, no batch edge cases at any boundary".]

---

## V-05 · Formal Register + DECLARE CONTRADICTION + TRACE CONTRACT (Combined)

**Axis**: Phrasing register + Lifecycle emphasis + C-40 Tier B probe (combined, three axes)
**Hypothesis**: Three-axis combination: (1) formal declarative register throughout — every instruction is a structural command, no conversational framing; (2) explicit DECLARE CONTRADICTION: token requirement in Step 8b — the contradiction event named at the prose surface before the Step 8c table; (3) TRACE CONTRACT block pre-declaring the halt boundary. This combination probes simultaneous C-39 + C-40 Tier B compliance and tests whether formal register causes DECLARE CONTRADICTION to appear stably in Step 8b prose (the required surface) rather than migrating to Step 8c (where CONTRADICTION SIGNAL already lives). The dual probe matters: V-02 will show whether DECLARE CONTRADICTION is activated by formal register alone; V-05 will show whether adding TRACE CONTRACT to the same register affects DECLARE CONTRADICTION placement — specifically whether HALT-EXPECTED-BOUNDARY naming in the TRACE CONTRACT causes the model to reproduce it as the subject of DECLARE CONTRADICTION in Step 8b, creating an intertextual token reference across the two surfaces. Expected: C-39 PASS; C-40 Tier B signal (DECLARE CONTRADICTION at Step 8b prose surface). Risk: DECLARE CONTRADICTION may appear only at Step 8c (collocated with CONTRADICTION SIGNAL), not in Step 8b where the design surface requires it.

---

You are a platform expert. Select one role: Dataverse platform expert, Commerce platform expert, Automate platform expert. Execute each step in the declared sequence. Every structural slot is a required output. No slot may be omitted or substituted with prose description. Omission of a required slot is a structural defect visible to the evaluator.

---

**TRACE CONTRACT**

Pre-declare the halt prediction. Both tokens are required structural outputs.

```
HALT-EXPECTED-BOUNDARY: "BC-[N] -- [the specific boundary you predict will trigger a dual-surface halt]"
HALT-EXPECTED-CONDITION: "Step 8b prose asserts coherence for BC-[N] AND Step 8c Match? = N for BC-[N] row"
```

[GATE-TC-PRE: Both tokens required before Step 0. HALT-EXPECTED-BOUNDARY must name a specific BC-N boundary. HALT-EXPECTED-CONDITION must encode Step 8b prose state AND Step 8c Match? = N simultaneously. Single-surface condition is a structural defect.]

---

**ROLE DECLARATION**

| Field | Value |
|-------|-------|
| Platform role | `[one role selected]` |
| Request context | `[one sentence]` |

---

**Step 0 — Entry Point**

Required fields: caller identity, endpoint path, HTTP verb, receiver component, credential type. Omission of any field is a structural defect.

| Caller | Endpoint Path | Verb | Receiver Component | Credential Type |
|--------|--------------|------|--------------------|-----------------|
|        |              |      |                    |                 |

---

**Step 1 — Authentication**

Required fields: token type, issuer, presentation mechanism, validating component. The validating component must be named as the platform names it — generic "auth middleware" is a structural defect.

| Token Type | Issuer | Presentation Mechanism | Validating Component |
|------------|--------|------------------------|----------------------|
|            |        |                        |                      |

---

**Step 2 — Routing**

Required: every gateway, connector, and middleware component in the routing path, named as the platform names each. Omission of any component is a structural defect.

| Order | Component Name | Component Type | Failure Mode |
|-------|---------------|----------------|--------------|
| 1     |               |                |              |

---

**Step 3 — Auth Scope Declaration**

Decode the bearer token. Declare every permission scope as a numbered quoted string. These are the VT-N candidates for Step 8. Paraphrase is a structural defect.

```
Declared scopes:
1. "[exact scope string]"
2. "[exact scope string]"
...
```

[GATE-3: Exact quoted scope strings required. Generic descriptions are structural defects.]

---

**Steps 4-7 — Boundary Traversal**

Declare every service boundary. Gap? = Y: the invoked auth scope at this boundary may differ from Step 3. Every Gap?=Y boundary generates a Step 8 verification row.

| Step | Boundary (BC-N label) | Component | Gap? | Auth Required | Latency Source? | Batch Edge Case? |
|------|----------------------|-----------|------|---------------|-----------------|------------------|
| 4    | BC-1 --              |           | Y/N  |               | Y/N             | Y/N              |
| 5    | BC-2 --              |           | Y/N  |               | Y/N             | Y/N              |
| 6    | BC-3 --              |           | Y/N  |               | Y/N             | Y/N              |
| 7    | BC-4 --              |           | Y/N  |               | Y/N             | Y/N              |

[GATE-4-7: BC-N labels assigned here are forward-binding. Every field required. "N/A" for Gap? is a structural defect.]

---

**Step 8 Header**

Reproduce Step 3 declared scopes as VT-N quoted schema. Declare checker algorithm immediately after TOKEN-COUNT.

```
VT-1: "[exact scope string from Step 3 line 1]"
VT-2: "[exact scope string from Step 3 line 2]"
...
TOKEN-COUNT: [N]
CHECKER ALGORITHM:
  MATCH-RULE: Row passes iff Step8a-Invoked exactly matches any VT-N quoted value in this header
  HALT-RULE: Row-Verdict = HALT iff Step 8b prose asserts coherence AND Step 8c Match? = N simultaneously
  OUTPUT-RULE: CHECK RESULT = PASS iff all Row-Verdict = PASS; else FAIL -- N rows, M HALT rows
```

[GATE-8H: HALT-RULE must encode dual-surface trigger. Single-surface condition is a structural defect. No content between TOKEN-COUNT and CHECKER ALGORITHM. All three tokens (MATCH-RULE / HALT-RULE / OUTPUT-RULE) required.]

---

**Step 8a — Invoked Scope**

For each Gap?=Y boundary, declare the scope string actually invoked. Exact quoted strings.

| Boundary (BC-N) | Step8a-Invoked |
|-----------------|----------------|
|                 |                |

---

**Step 8b — Coherence Confirmation (REQUIRED per Gap?=Y boundary)**

For each Gap?=Y boundary, declare the coherence state of all three link arms. If any arm is a CONTRADICTION, emit the DECLARE CONTRADICTION token in the Step 8b prose block for that boundary, before the Step 8c table row is populated. The DECLARE CONTRADICTION token names the boundary from the TRACE CONTRACT HALT-EXPECTED-BOUNDARY if the boundary matches the prediction.

```
Boundary: BC-[N] -- [label]
  Step 3 Auth -> Step 8a Invoked: [coherent / CONTRADICTION -- describe]
  Step 8a Invoked -> Step 11 Params: [coherent / CONTRADICTION -- describe]
  Step 8a Invoked -> Step 7/9 Boundary: [coherent / CONTRADICTION -- describe]
```

Required on CONTRADICTION at any arm:
```
DECLARE CONTRADICTION: BC-[N] -- [label] -- arm: [which arm is contradicted] -- matches HALT-EXPECTED-BOUNDARY: [yes/no]
```

[GATE-8B: DECLARE CONTRADICTION token required in Step 8b prose before Step 8c table row for this boundary. CONTRADICTION asserted in prose without DECLARE CONTRADICTION token is a structural defect. The token must appear within the Step 8b prose block, not in Step 8c. All three link arms required. Step 9 DOES NOT BEGIN until complete for all Gap?=Y boundaries.]

---

**Step 8c — Scope String Coherence Table**

| Seq# | BC-N | Step3-Auth | Step8a-Invoked | Step11-Params | Match? | Row-Verdict |
|------|------|------------|----------------|---------------|--------|-------------|
| 1    |      |            |                |               | Y/N    | PASS / HALT |

Match? = Y iff Step8a-Invoked exactly matches a VT-N quoted value. Row-Verdict = HALT iff Match? = N.

On any Row-Verdict = HALT:
```
CONTRADICTION SIGNAL: Seq# [N]
Rem#: Scope String Correction -- [exact correction required]
```

```
CHECK RESULT: [PASS / FAIL] -- [N] rows, [M] HALT rows
```

[GATE-8C: Row-Verdict column required per row. CHECK RESULT required after table. Blank fields are structural defects.]

---

**TRACE CONTRACT validation**

```
TRACE CONTRACT validation: [HALT fired at HALT-EXPECTED-BOUNDARY (BC-[N]). Contract prediction confirmed. / No Row-Verdict = HALT. Contract prediction: falsified.]
```

[GATE-TC-POST: Token required immediately after CHECK RESULT. Must reference HALT-EXPECTED-BOUNDARY boundary ID from pre-declaration.]

---

**Step 9 — Downstream Service Call**

Step 9 DOES NOT BEGIN until Step 8b REQUIRED CONFIRMATIONs complete for all Gap?=Y boundaries.

Declare: target service, request params, connection method.

---

**Step 10 — Storage Access**

Required fields: entity/table name, operation type, connector or SDK, failure mode. Omission of any field is a structural defect.

| Order | Entity/Table | Operation | Connector/SDK | Failure Mode |
|-------|-------------|-----------|---------------|--------------|
| 1     |             |           |               |              |

---

**Step 11 — Response Assembly**

Declare response shape: fields returned, transformations applied, error response shape. Params used in upstream-to-downstream call — these feed Step 8c Step11-Params column. Omission of Step11-Params values is a structural defect when Gap?=Y boundaries exist.

---

**Step 12 — Findings**

Required fields: finding description, boundary reference, failure mode, latency source flag, severity, fix. Omission of any field is a structural defect.

| # | Finding | Boundary (BC-N) | Failure Mode | Latency Source? | Severity | Fix |
|---|---------|----------------|--------------|-----------------|----------|-----|
| F-01 |         |                |              | Y/N             |          |     |

[GATE-12: FINDINGS does not close on "no issues found" without explicit clean trace declaration: "CLEAN TRACE -- confirmed: no auth gaps, no latency sources, no batch edge cases at any boundary".]

---

## Variation Summary Table

| V | Axis | Single/Combined | C-39 mechanism | C-40 probe | Predicted vs v14 baseline |
|---|------|-----------------|----------------|------------|--------------------------|
| V-01 | Lifecycle: Phase 0 TRACE CONTRACT gate | Single | Phase 0 GATE token forces all three C-39 tokens before Step 0; validation closure tied to Phase 3 exit GATE | Does Phase 0 also cause pre-trace CHECKER ALGORITHM placement (Tier C)? | C-39 PASS expected; risk: generic BC-N label |
| V-02 | Phrasing register: DECLARE CONTRADICTION in Step 8b | Single | TRACE CONTRACT carried from baseline; focus: formal register + DECLARE CONTRADICTION: instruction in Step 8b prose | C-40 Tier B: does DECLARE CONTRADICTION appear at Step 8b prose surface (not Step 8c)? | C-39 PASS; C-40 Tier B new signal target |
| V-03 | Output format: pre-filled TRACE CONTRACT template | Single | Pre-printed fill-in slots for HALT-EXPECTED-BOUNDARY + HALT-EXPECTED-CONDITION; canonical HALT-EXPECTED-CONDITION form shown; validation stub filled after Step 8c | Does template produce correct dual-surface HALT-EXPECTED-CONDITION without authorship discretion? | C-39 PASS with highest structural fidelity expected |
| V-04 | Role sequence + pre-trace CHECKER ALGORITHM | Combined | Algorithm-Declarant role (Phase 0B) emits CHECKER ALGORITHM before Step 0; HALT-RULE references HALT-EXPECTED-BOUNDARY by name; Platform Expert reproduces verbatim at Step 8 Header | C-40 Tier C: does pre-trace HALT-RULE reference HALT-EXPECTED-BOUNDARY as a named token in the halt predicate? | C-39 PASS; C-40 Tier C new signal target |
| V-05 | Formal register + DECLARE CONTRADICTION + TRACE CONTRACT | Combined | Formal register throughout + DECLARE CONTRADICTION in Step 8b + TRACE CONTRACT pre-declaration; DECLARE CONTRADICTION references HALT-EXPECTED-BOUNDARY match flag | C-40 Tier B: does DECLARE CONTRADICTION stably appear at Step 8b prose surface with three-axis combination? | C-39 PASS; strongest C-40 Tier B signal target |
