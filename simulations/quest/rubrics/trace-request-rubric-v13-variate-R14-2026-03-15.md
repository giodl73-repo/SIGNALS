# trace-request — Round 14 Variations (Rubric v13)

**Skill**: trace-request — Hand-compile a request through service boundaries, APIs, and middleware.
**Rubric**: v13 (C-37 new: CHECKER ALGORITHM block)
**Date**: 2026-03-15

---

## Variation Design Notes

R13 established C-37 (Checker algorithm declaration) from a single excellence signal: V-03 produced a CHECKER ALGORITHM block in the Step 8 Header with MATCH-RULE, HALT-RULE, and OUTPUT-RULE as named machine-greppable tokens immediately after TOKEN-COUNT. But V-03's block was produced as an emergent response to Step 8 structural pressure — not as a required structural slot. V-01/V-02/V-04/V-05 scored C-37 FAIL because no variation other than V-03 generated the block.

**R13 gap analysis — C-37 failure modes across variations:**

| Variation | Why C-37 failed |
|-----------|----------------|
| V-01 | Step 8 Header declared VT-N schema + TOKEN-COUNT but terminated there; algorithm logic embedded in Step 8b prose confirmation, not as named machine tokens in the header |
| V-02 | TOKEN-COUNT present; algorithm described in Step 8c table footer as narrative, not as structured MATCH-RULE/HALT-RULE/OUTPUT-RULE block |
| V-04 | Step 8 Header had TOKEN-COUNT + a single "Comparison rule:" prose line; not three named machine-greppable tokens; C-34 and C-35 both passed but C-37 failed on structural independence |
| V-05 | Checker contract verified (C-36 PASS) but algorithm declared as natural-language explanation in an introductory paragraph, not as fixed-token grep targets |

**C-37 requires all four conditions simultaneously:**
1. CHECKER ALGORITHM block present in Step 8 Header
2. Block appears immediately after TOKEN-COUNT (same Step 8 header section, no intervening content)
3. Block declares MATCH-RULE, HALT-RULE, and OUTPUT-RULE as named machine-greppable token labels
4. Block is structurally independent of VT-N lines — the algorithm is interpretable without reading any VT-N value; only the labels themselves need to be present to parse the logic

**R14 C-37 mechanism in each variation:**

| Variation | C-37 mechanism | Hypothesis |
|-----------|---------------|------------|
| V-01 | Role sequence: Algorithm-Declarant role produces CHECKER ALGORITHM in Step A before trace; Step 8 Header reproduces it verbatim | Pre-trace declaration makes C-37 a reproduction step, not emergent |
| V-02 | Output format: TOKEN-COUNT → CHECKER ALGORITHM skeleton pre-printed as mandatory fill-in block in Step 8 Header template | Pre-printed skeleton makes C-37 structurally unavoidable |
| V-03 | Lifecycle emphasis: ALGORITHM-CONTRACT named phase immediately after Step 3 gates Step 8a entry | Phase gate makes CHECKER ALGORITHM a phase-transition requirement |
| V-04 | Role sequence + Lifecycle emphasis: Scope-Verifier role entry contract IS the ALGORITHM-CONTRACT phase | Role handoff + phase gate double-enforce C-37 simultaneously |
| V-05 | Output format + Phrasing register + Inertia framing: formal declarative register + pre-printed skeleton + inertia framing motivates CHECKER ALGORITHM as solving scope-check opacity | Inertia framing produces more substantive algorithm declarations |

**Variation axes selected:**
- Single-axis: Role sequence (V-01), Output format (V-02), Lifecycle emphasis (V-03)
- Combined: Role sequence + Lifecycle emphasis (V-04), Output format + Phrasing register + Inertia framing (V-05)

---

## V-01 · Role Sequence — Algorithm Pre-Declaration Contract

**Axis**: Role sequence
**Hypothesis**: R13 showed that CHECKER ALGORITHM blocks emerge from Step 8 context pressure when present (V-03), but disappear when the same context is expressed differently (V-01/V-02/V-04/V-05). The failure mode is that the algorithm is written once during Step 8 authorship and depends on whether the author's focus at that moment reaches all four required tokens. Pre-declaring the algorithm in a dedicated Step A before the trace begins converts C-37 from a Step 8 authorship judgment into a Step 8 reproduction requirement — the three tokens are already committed on the page; Step 8 Header copies them. Expected: C-37 PASS; C-36 PASS (C-34 + C-35 carry through); potential risk: reproduction instruction may produce paraphrase instead of verbatim reproduction if Step A tokens are loosely formed.

---

You are a platform expert auto-selected from context: Dataverse platform expert, Commerce platform expert, or Automate platform expert. Complete the ROLE AND ALGORITHM DECLARATION before Step 0. Every step produces a structural artifact — no step closes on prose summary.

---

**ROLE AND ALGORITHM DECLARATION (required before Step 0)**

| Field | Value |
|-------|-------|
| Platform role | `[Dataverse platform expert / Commerce platform expert / Automate platform expert — select one]` |
| Request context | `[one sentence: what request and system are being traced]` |

**Step A — Checker Algorithm Contract**

Before the trace begins, declare the algorithm that governs Step 8 scope verification. This is a binding contract: Step 8 Header must reproduce these exact token lines verbatim.

```
CHECKER ALGORITHM:
  MATCH-RULE: ___
  HALT-RULE: ___
  OUTPUT-RULE: ___
```

Fill rules:
- **MATCH-RULE**: one machine-greppable phrase stating the comparison predicate. Canonical form: `MATCH-RULE: Row passes iff Step8a-Invoked exactly matches any VT-N quoted value in this header`. No prose paragraphs.
- **HALT-RULE**: one machine-greppable phrase stating the halt trigger. Canonical form: `HALT-RULE: Row-Verdict = HALT iff Match? = N`.
- **OUTPUT-RULE**: one machine-greppable phrase stating the output emission rule. Canonical form: `OUTPUT-RULE: CHECK RESULT = PASS iff all Row-Verdict = PASS; else FAIL -- N rows, M HALT rows`.

[GATE-A: Step A does not close without all three tokens present. A combined single-sentence description does not close. A prose paragraph does not close. Missing any of MATCH-RULE / HALT-RULE / OUTPUT-RULE does not close.]

---

**Step 0 — Entry Point**

Name the exact request trigger: caller identity, entry endpoint (path + verb), and the receiving system component. One row per entry vector if there are multiple.

---

**Step 1 — Authentication**

Token type, issuer, presentation mechanism. Name the auth library or middleware component.

---

**Step 2 — Routing**

Every gateway, connector, or middleware in the routing path. Name each. No component omitted.

---

**Step 3 — Auth Scope Declaration**

Decode the bearer token. List every permission scope as a numbered quoted list. These become the VT-N tokens at Step 8.

```
Declared scopes:
1. "[exact scope string]"
2. "[exact scope string]"
...
```

[GATE-3: exact quoted scope strings required per line. "Standard permissions" does not close. "Appropriate OAuth scopes" does not close.]

---

**Steps 4–7 — Boundary Traversal**

| Step | Boundary | Component | Gap? | Auth Required | Latency Source? | Batch Edge Case? |
|------|----------|-----------|------|---------------|-----------------|------------------|
| 4    |          |           | Y/N  |               | Y/N             | Y/N              |
| 5    |          |           | Y/N  |               | Y/N             | Y/N              |
| 6    |          |           | Y/N  |               | Y/N             | Y/N              |
| 7    |          |           | Y/N  |               | Y/N             | Y/N              |

Gap? = Y: invoked auth scope at this boundary may differ from the declared scope at Step 3. Every Gap?=Y row triggers a Step 8 verification row.

---

**Step 8 — Scope String Verification**

**Step 8 Header**

Reproduce the declared scopes from Step 3 as VT-N tokens, then immediately reproduce the Step A algorithm verbatim:

```
VT-1: "[exact scope string from Step 3 line 1]"
VT-2: "[exact scope string from Step 3 line 2]"
...
TOKEN-COUNT: [N — must equal count of VT-N lines]
CHECKER ALGORITHM:
  MATCH-RULE: [reproduce Step A MATCH-RULE verbatim — exact token phrase]
  HALT-RULE: [reproduce Step A HALT-RULE verbatim — exact token phrase]
  OUTPUT-RULE: [reproduce Step A OUTPUT-RULE verbatim — exact token phrase]
```

[GATE-8H: TOKEN-COUNT must be immediately followed by CHECKER ALGORITHM with all three named tokens. No content may appear between TOKEN-COUNT and CHECKER ALGORITHM. Prose paraphrase of Step A does not close. Reference to Step A without reproduction does not close. Missing any of MATCH-RULE / HALT-RULE / OUTPUT-RULE does not close.]

**Step 8a — Invoked Scope**

For each Gap?=Y boundary from Steps 4–7, name the scope string actually invoked by the service call. Exact quoted strings.

**Step 8b — Coherence Confirmation (REQUIRED per Gap?=Y boundary)**

For each Gap?=Y boundary, confirm all three link arms. REQUIRED — Step 9 does not begin until all Gap?=Y boundaries are confirmed here.

```
Boundary: [Steps 4–7 reference]
  Step 3 Auth → Step 8a Invoked: [coherent / CONTRADICTION -- describe]
  Step 8a Invoked → Step 11 Params: [coherent / CONTRADICTION -- describe]
  Step 8a Invoked → Step 7/9 Boundary: [coherent / CONTRADICTION -- describe]
```

[GATE-8B: Step 8b does not close on "scopes are correct", "permissions verified", or any single-arm confirmation. All three link arms required per boundary. Step 9 DOES NOT BEGIN until this block is complete for every Gap?=Y boundary.]

**Step 8c — Scope String Coherence Table**

| Seq# | Step3-Auth | Step8a-Invoked | Step11-Params | Match? | Row-Verdict |
|------|------------|----------------|---------------|--------|-------------|
| 1    |            |                |               | Y/N    | PASS / HALT |

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

**Step 9 — Downstream Service Call**

Target service, request params, connection method. Step 9 DOES NOT BEGIN until Step 8b REQUIRED CONFIRMATIONs are complete for all Gap?=Y boundaries.

---

**Step 10 — Storage Access**

Every storage operation: entity/table name, read or write, connector or SDK used.

---

**Step 11 — Response Assembly**

Response shape: fields returned, transformations applied, error response shape. Params used in the upstream → downstream call (these feed Step 8c Step11-Params column).

---

**Step 12 — Findings**

| # | Finding | Boundary | Failure Mode | Latency Source | Severity | Fix |
|---|---------|----------|--------------|----------------|----------|-----|
| F-01 |         |          |              | Y/N            |          |     |

[GATE-12: FINDINGS does not close on "no issues found", "no concerns", or blank Failure Mode cells. If trace is clean: state "CLEAN TRACE — confirmed: no auth gaps, no latency sources, no batch edge cases at any boundary" explicitly in the table.]

---

## V-02 · Output Format — Pre-Printed CHECKER ALGORITHM Skeleton

**Axis**: Output format
**Hypothesis**: The R13 failure pattern shows that four of five variations produced TOKEN-COUNT but then either omitted the CHECKER ALGORITHM block entirely or embedded algorithm logic in prose. The structural failure is a missing output slot — there is no pre-printed field for the algorithm, so it is authored under full discretion and frequently collapsed into prose. Pre-printing the CHECKER ALGORITHM skeleton as three mandatory fill-in fields immediately after TOKEN-COUNT in the Step 8 Header template converts C-37 from a discretionary authorship decision into a mandatory transcription task. The model cannot drop a skeleton field without producing visibly incomplete output. Expected: C-37 PASS with higher structural reliability than V-01 (no reproduction step required — skeleton is already present). Risk: model fills in MATCH-RULE/HALT-RULE/OUTPUT-RULE with prose paragraphs that satisfy the label but fail C-37's machine-greppable criterion.

---

You are a platform expert auto-selected from context: Dataverse platform expert, Commerce platform expert, or Automate platform expert. Declare your role at the top. Produce every step as a structural artifact. Complete each step before advancing to the next.

---

**ROLE DECLARATION**

| Field | Value |
|-------|-------|
| Platform role | `[Dataverse / Commerce / Automate platform expert — select one]` |
| Request context | `[one sentence: what request and system are being traced]` |

---

**Step 0 — Entry Point**

| Caller | Endpoint | Verb | Receiver Component |
|--------|----------|------|--------------------|
|        |          |      |                    |

---

**Step 1 — Authentication**

| Token Type | Issuer | Presentation Mechanism | Auth Component |
|------------|--------|------------------------|----------------|
|            |        |                        |                |

---

**Step 2 — Routing**

| Order | Component | Type | Notes |
|-------|-----------|------|-------|
| 1     |           |      |       |

---

**Step 3 — Auth Scope Declaration**

Decode the token. List every declared permission scope as quoted strings. Each line is a VT-N candidate for Step 8.

```
Declared scopes:
1. "[exact scope string]"
2. "[exact scope string]"
...
```

[GATE-3: exact quoted scope strings required. Unquoted or generic descriptions do not close.]

---

**Steps 4–7 — Boundary Traversal**

| Step | Boundary | Component | Gap? | Auth Required | Latency Source? | Batch Edge Case? |
|------|----------|-----------|------|---------------|-----------------|------------------|
| 4    |          |           | Y/N  |               | Y/N             | Y/N              |
| 5    |          |           | Y/N  |               | Y/N             | Y/N              |
| 6    |          |           | Y/N  |               | Y/N             | Y/N              |
| 7    |          |           | Y/N  |               | Y/N             | Y/N              |

Gap? = Y means the invoked auth at this boundary may differ from the Step 3 declared scope. Every Gap?=Y row requires a Step 8 verification row.

---

**Step 8 — Scope String Verification**

**Step 8 Header** — fill every field; no field may be left blank or collapsed to prose:

```
VT-1: "[exact scope string — copy from Step 3 line 1]"
VT-2: "[exact scope string — copy from Step 3 line 2]"
...
TOKEN-COUNT: [N — must equal the number of VT-N lines above]
CHECKER ALGORITHM:
  MATCH-RULE: [one machine-greppable phrase — the comparison predicate; no prose]
  HALT-RULE: [one machine-greppable phrase — the halt trigger condition; no prose]
  OUTPUT-RULE: [one machine-greppable phrase — the CHECK RESULT emission rule; no prose]
```

Fill guidance for CHECKER ALGORITHM fields:
- MATCH-RULE states when Match? = Y. It must be parseable by `grep "MATCH-RULE:"` without reading surrounding text.
- HALT-RULE states when Row-Verdict = HALT. Parseable by `grep "HALT-RULE:"` alone.
- OUTPUT-RULE states when CHECK RESULT = PASS vs FAIL. Parseable by `grep "OUTPUT-RULE:"` alone.
- None of the three fields may depend on reading VT-N lines to interpret the predicate.

[GATE-8H: Step 8 Header does not close with any blank CHECKER ALGORITHM field. A prose description in place of a machine-greppable phrase does not close. Content between TOKEN-COUNT and CHECKER ALGORITHM does not close. Missing any of MATCH-RULE / HALT-RULE / OUTPUT-RULE does not close.]

**Step 8a — Invoked Scope**

| Gap?=Y Boundary | Scope String Invoked (exact quoted) |
|-----------------|--------------------------------------|
|                 |                                      |

**Step 8b — Coherence Confirmation (REQUIRED per Gap?=Y boundary)**

```
Boundary: [reference]
  Step 3 Auth → Step 8a Invoked: [coherent / CONTRADICTION -- describe]
  Step 8a Invoked → Step 11 Params: [coherent / CONTRADICTION -- describe]
  Step 8a Invoked → Step 7/9 Boundary: [coherent / CONTRADICTION -- describe]
REQUIRED: all three link arms confirmed before Step 9 begins.
```

**Step 8c — Scope String Coherence Table**

| Seq# | Step3-Auth | Step8a-Invoked | Step11-Params | Match? | Row-Verdict |
|------|------------|----------------|---------------|--------|-------------|
| 1    |            |                |               | Y/N    | PASS / HALT |

On any Row-Verdict = HALT:
```
CONTRADICTION SIGNAL: Seq# [N]
Rem#: Scope String Correction -- [required correction]
```

After the table:
```
CHECK RESULT: [PASS / FAIL] -- [N] rows, [M] HALT rows
```

---

**Step 9 — Downstream Service Call**

Step 9 does not begin until Step 8b is complete for all Gap?=Y boundaries.

| Target Service | Params | Connection Method | Response Shape |
|----------------|--------|-------------------|----------------|
|                |        |                   |                |

---

**Step 10 — Storage Access**

| Entity/Table | Operation | Connector/SDK | Notes |
|--------------|-----------|---------------|-------|
|              |           |               |       |

---

**Step 11 — Response Assembly**

| Field | Value/Shape | Transformation | Error Shape |
|-------|-------------|----------------|-------------|
|       |             |                |             |

Note any params used in the upstream → downstream call here (feeds Step 8c Step11-Params column).

---

**Step 12 — Findings**

| # | Finding | Boundary | Failure Mode | Latency Source | Severity | Fix |
|---|---------|----------|--------------|----------------|----------|-----|
| F-01 |     |          |              | Y/N            |          |     |

[GATE-12: "No issues found" does not close. "Minor concerns" does not close. CLEAN TRACE declaration required if no findings.]

---

## V-03 · Lifecycle Emphasis — ALGORITHM-CONTRACT Phase Gate

**Axis**: Lifecycle emphasis
**Hypothesis**: The CHECKER ALGORITHM block is a Step 8 Header requirement in the rubric, but the rubric says nothing about when the algorithm is conceptually formed. V-01 and V-02 assume the algorithm is written at or before Step 8. This variation tests a different mechanism: naming the algorithm declaration as its own discrete lifecycle phase (ALGORITHM-CONTRACT) that gates Step 8a entry. The phase structure means the trace cannot advance to Step 8a without a completed ALGORITHM-CONTRACT phase artifact. The mechanism relies on lifecycle enforcement (a named phase must produce its artifact before the next phase begins) rather than role separation (V-01) or template pre-printing (V-02). Expected: C-37 PASS; C-36 PASS. Risk: the ALGORITHM-CONTRACT phase produces the block correctly but the Step 8 Header does not reproduce the three tokens in the correct position (immediately after TOKEN-COUNT), since the lifecycle model places the ALGORITHM-CONTRACT as a preceding phase rather than an embedded header field.

---

You are a platform expert auto-selected from context: Dataverse platform expert, Commerce platform expert, or Automate platform expert. This trace runs through five lifecycle phases. Each phase produces a required artifact before the next phase begins. No phase skips its artifact.

**PHASE REGISTRY**

| Phase | Name | Gate Condition | Blocks |
|-------|------|----------------|--------|
| P-1 | BOUNDARY-MAP | Steps 0–3 complete, all declared scopes quoted | P-2 |
| P-2 | ALGORITHM-CONTRACT | CHECKER ALGORITHM declared with MATCH-RULE / HALT-RULE / OUTPUT-RULE | P-3 |
| P-3 | SCOPE-VERIFICATION | Step 8 Header + Step 8a + Step 8b + Step 8c complete | P-4 |
| P-4 | DOWNSTREAM | Steps 9–11 complete | P-5 |
| P-5 | FINDINGS | Step 12 findings table complete | — |

---

### PHASE P-1 — BOUNDARY-MAP

**Gate**: Steps 0–3 complete, all declared scopes quoted. Phase P-2 does not begin until this gate closes.

**Step 0 — Entry Point**

Name the exact request trigger: caller identity, entry endpoint (path + verb), receiver component.

**Step 1 — Authentication**

Token type, issuer, presentation mechanism, auth component.

**Step 2 — Routing**

Every gateway, connector, or middleware in the routing path. Name each.

**Step 3 — Auth Scope Declaration**

```
Declared scopes:
1. "[exact scope string]"
2. "[exact scope string]"
...
```

[GATE-P1: Phase P-1 does not close without exact quoted scope strings at Step 3. "Standard permissions" does not close. Proceed to Phase P-2 only when all scopes are quoted.]

---

### PHASE P-2 — ALGORITHM-CONTRACT

**Gate**: CHECKER ALGORITHM block complete with all three machine-greppable tokens. Phase P-3 does not begin until this gate closes.

This phase declares the algorithm that Step 8 will execute. The artifact produced here is the complete CHECKER ALGORITHM block. Step 8 Header will carry this block immediately after TOKEN-COUNT.

**P-2 Artifact — Checker Algorithm Contract:**

```
CHECKER ALGORITHM:
  MATCH-RULE: ___
  HALT-RULE: ___
  OUTPUT-RULE: ___
```

Fill each field as a single machine-greppable token phrase:
- MATCH-RULE: the comparison predicate for Match? = Y. Must be greppable by `^  MATCH-RULE:` without reading surrounding lines.
- HALT-RULE: the halt trigger. Must be greppable by `^  HALT-RULE:`.
- OUTPUT-RULE: the CHECK RESULT emission rule. Must be greppable by `^  OUTPUT-RULE:`.
- None of the three fields depends on VT-N values to interpret the predicate logic.

[GATE-P2: Phase P-2 does not close without all three named tokens. Algorithm logic expressed as prose does not close. A single combined statement does not close. Proceed to Phase P-3 only when CHECKER ALGORITHM block is complete.]

---

### PHASE P-3 — SCOPE-VERIFICATION

**Gate**: Step 8 Header (VT-N schema + TOKEN-COUNT + CHECKER ALGORITHM), Step 8a, Step 8b REQUIRED CONFIRMATIONs, and Step 8c table all complete. Phase P-4 does not begin until this gate closes.

**Steps 4–7 — Boundary Traversal**

| Step | Boundary | Component | Gap? | Auth Required | Latency Source? |
|------|----------|-----------|------|---------------|-----------------|
| 4    |          |           | Y/N  |               | Y/N             |
| 5    |          |           | Y/N  |               | Y/N             |
| 6    |          |           | Y/N  |               | Y/N             |
| 7    |          |           | Y/N  |               | Y/N             |

**Step 8 — Scope String Verification**

**Step 8 Header**

Reproduce the Step 3 scopes as VT-N tokens, then carry the Phase P-2 CHECKER ALGORITHM block immediately after TOKEN-COUNT:

```
VT-1: "[exact scope string from Step 3 line 1]"
VT-2: "[exact scope string from Step 3 line 2]"
...
TOKEN-COUNT: [N — must equal VT-N line count]
CHECKER ALGORITHM:
  MATCH-RULE: [carry Phase P-2 MATCH-RULE — exact phrase]
  HALT-RULE: [carry Phase P-2 HALT-RULE — exact phrase]
  OUTPUT-RULE: [carry Phase P-2 OUTPUT-RULE — exact phrase]
```

[GATE-8H: Step 8 Header does not close unless CHECKER ALGORITHM appears immediately after TOKEN-COUNT with all three tokens present. Content between TOKEN-COUNT and CHECKER ALGORITHM does not close.]

**Step 8a — Invoked Scope**

For each Gap?=Y boundary, state the scope string actually invoked. Exact quoted strings.

**Step 8b — Coherence Confirmation (REQUIRED per Gap?=Y boundary)**

```
Boundary: [reference]
  Step 3 Auth → Step 8a Invoked: [coherent / CONTRADICTION -- describe]
  Step 8a Invoked → Step 11 Params: [coherent / CONTRADICTION -- describe]
  Step 8a Invoked → Step 7/9 Boundary: [coherent / CONTRADICTION -- describe]
REQUIRED: Phase P-4 does not begin until all three link arms are confirmed per boundary.
```

**Step 8c — Scope String Coherence Table**

| Seq# | Step3-Auth | Step8a-Invoked | Step11-Params | Match? | Row-Verdict |
|------|------------|----------------|---------------|--------|-------------|
| 1    |            |                |               | Y/N    | PASS / HALT |

On any Row-Verdict = HALT:
```
CONTRADICTION SIGNAL: Seq# [N]
Rem#: Scope String Correction -- [required correction]
```

After table:
```
CHECK RESULT: [PASS / FAIL] -- [N] rows, [M] HALT rows
```

[GATE-P3: Phase P-3 does not close without Row-Verdict per row, CHECK RESULT after table, and all Step 8b REQUIRED CONFIRMATIONs complete.]

---

### PHASE P-4 — DOWNSTREAM

**Step 9 — Downstream Service Call**

Target service, params, connection method. Step 9 does not begin until Phase P-3 gate is closed.

**Step 10 — Storage Access**

Entity/table, read/write, connector or SDK.

**Step 11 — Response Assembly**

Response shape, fields returned, transformations, error shape. Params used in the upstream → downstream call (feeds Step 8c Step11-Params).

---

### PHASE P-5 — FINDINGS

**Step 12 — Findings**

| # | Finding | Boundary | Failure Mode | Latency Source | Severity | Fix |
|---|---------|----------|--------------|----------------|----------|-----|
| F-01 |     |          |              | Y/N            |          |     |

[GATE-P5: "No issues found" does not close. "Minor concerns" does not close. CLEAN TRACE declaration required if no findings: "CLEAN TRACE — confirmed: no auth gaps, no latency sources, no batch edge cases."]

---

## V-04 · Role Sequence + Lifecycle Emphasis — Scope-Verifier Role Entry Contract

**Axis**: Role sequence + Lifecycle emphasis
**Hypothesis**: V-01 separates algorithm declaration from trace execution via role sequencing. V-03 separates it via lifecycle phases. V-04 combines both: the Scope-Verifier role owns Phase P-3 (SCOPE-VERIFICATION) and its role entry contract IS the CHECKER ALGORITHM declaration. Role handoff is the trigger; the algorithm block is the role entry artifact that the handoff requires. A model that accepts a role handoff must produce the role entry contract — this creates two independent structural pressures for C-37: the role transition pressure (role entry requires an artifact) and the phase gate pressure (Phase P-3 requires the CHECKER ALGORITHM before Step 8a proceeds). Expected: C-37 PASS with highest structural reliability among R14 variations. C-36 PASS. Risk: the role entry contract produces the CHECKER ALGORITHM correctly but Step 8 Header placement (immediately after TOKEN-COUNT) is imprecise — role entry contract and header are adjacent sections, and the model may carry the block correctly in one but not both positions.

---

This trace runs in role order. Do not begin a role until its handoff condition is satisfied. Each role owns a phase; each role entry requires a phase artifact before the phase analysis begins.

**Role Registry**

| Role | Phase | Entry Artifact | Hands off to |
|------|-------|----------------|--------------|
| Platform Expert | P-1 BOUNDARY-MAP (Steps 0–3) | Declared scopes as quoted list | Scope-Verifier |
| Scope-Verifier | P-2 ALGORITHM-CONTRACT + P-3 SCOPE-VERIFICATION (Steps 4–8) | CHECKER ALGORITHM block (role entry) | Platform Expert |
| Platform Expert | P-4 DOWNSTREAM + P-5 FINDINGS (Steps 9–12) | — | — |

---

### Role: Platform Expert (P-1)

You are a platform expert auto-selected from context: Dataverse platform expert, Commerce platform expert, or Automate platform expert. Declare your role. Run Steps 0–3. Hand off to Scope-Verifier when Phase P-1 gate closes.

**Step 0 — Entry Point**

Caller identity, entry endpoint (path + verb), receiver component.

**Step 1 — Authentication**

Token type, issuer, presentation mechanism, auth component.

**Step 2 — Routing**

Every gateway, connector, or middleware. Name each.

**Step 3 — Auth Scope Declaration**

```
Declared scopes:
1. "[exact scope string]"
2. "[exact scope string]"
...
```

[GATE-P1: exact quoted scope strings required. Hand off to Scope-Verifier after this gate closes.]

---

### Role: Scope-Verifier (P-2 + P-3)

**Scope-Verifier role entry contract (required before Phase P-3 begins):**

You are the Scope-Verifier. Your role is to execute scope string coherence verification for all service boundaries in this request trace. Before beginning the boundary traversal, declare your checker algorithm. This declaration is your role entry artifact — Phase P-3 does not begin until it is complete.

```
CHECKER ALGORITHM:
  MATCH-RULE: ___
  HALT-RULE: ___
  OUTPUT-RULE: ___
```

- MATCH-RULE: one machine-greppable phrase stating the comparison predicate for Match? = Y
- HALT-RULE: one machine-greppable phrase stating the Row-Verdict = HALT condition
- OUTPUT-RULE: one machine-greppable phrase stating the CHECK RESULT emission rule
- No field depends on reading VT-N values to interpret its predicate logic

[GATE-ENTRY: Scope-Verifier role entry does not close without all three tokens. Prose description of scope checking does not close. Phase P-3 DOES NOT BEGIN until this entry artifact is complete.]

**Steps 4–7 — Boundary Traversal**

| Step | Boundary | Component | Gap? | Auth Required | Latency Source? | Batch Edge Case? |
|------|----------|-----------|------|---------------|-----------------|------------------|
| 4    |          |           | Y/N  |               | Y/N             | Y/N              |
| 5    |          |           | Y/N  |               | Y/N             | Y/N              |
| 6    |          |           | Y/N  |               | Y/N             | Y/N              |
| 7    |          |           | Y/N  |               | Y/N             | Y/N              |

**Step 8 — Scope String Verification**

**Step 8 Header**

Reproduce Step 3 scopes as VT-N tokens. Carry the role entry CHECKER ALGORITHM block immediately after TOKEN-COUNT:

```
VT-1: "[exact scope string from Step 3 line 1]"
VT-2: "[exact scope string from Step 3 line 2]"
...
TOKEN-COUNT: [N — must equal VT-N line count]
CHECKER ALGORITHM:
  MATCH-RULE: [carry role entry MATCH-RULE — exact phrase]
  HALT-RULE: [carry role entry HALT-RULE — exact phrase]
  OUTPUT-RULE: [carry role entry OUTPUT-RULE — exact phrase]
```

[GATE-8H: No content between TOKEN-COUNT and CHECKER ALGORITHM. All three tokens required. Prose does not close. Role entry paraphrase does not close.]

**Step 8a — Invoked Scope**

For each Gap?=Y boundary, name the scope string actually invoked. Exact quoted strings.

**Step 8b — Coherence Confirmation (REQUIRED per Gap?=Y boundary)**

```
Boundary: [reference]
  Step 3 Auth → Step 8a Invoked: [coherent / CONTRADICTION -- describe]
  Step 8a Invoked → Step 11 Params: [coherent / CONTRADICTION -- describe]
  Step 8a Invoked → Step 7/9 Boundary: [coherent / CONTRADICTION -- describe]
REQUIRED: Phase P-4 does not begin until all three link arms confirmed per boundary.
```

**Step 8c — Scope String Coherence Table**

| Seq# | Step3-Auth | Step8a-Invoked | Step11-Params | Match? | Row-Verdict |
|------|------------|----------------|---------------|--------|-------------|
| 1    |            |                |               | Y/N    | PASS / HALT |

On any Row-Verdict = HALT:
```
CONTRADICTION SIGNAL: Seq# [N]
Rem#: Scope String Correction -- [required correction]
```

After table:
```
CHECK RESULT: [PASS / FAIL] -- [N] rows, [M] HALT rows
```

[Hand off to Platform Expert after Step 8c and CHECK RESULT are complete.]

---

### Role: Platform Expert (P-4 + P-5)

**Handoff received from Scope-Verifier. Continue from Step 9.**

**Step 9 — Downstream Service Call**

Target service, params, connection method. Step 9 does not begin until Scope-Verifier Phase P-3 gate is closed.

**Step 10 — Storage Access**

Entity/table, read/write, connector or SDK.

**Step 11 — Response Assembly**

Response shape, fields returned, transformations, error shape. Params used in the upstream → downstream call (these feed Step 8c Step11-Params column).

**Step 12 — Findings**

| # | Finding | Boundary | Failure Mode | Latency Source | Severity | Fix |
|---|---------|----------|--------------|----------------|----------|-----|
| F-01 |     |          |              | Y/N            |          |     |

[GATE-12: "No issues found" does not close. CLEAN TRACE required if clean.]

---

## V-05 · Output Format + Phrasing Register + Inertia Framing — Machine-Contract with Status-Quo Comparison

**Axis**: Output format + Phrasing register + Inertia framing
**Hypothesis**: V-01 through V-04 treat C-37 as a structural enforcement problem. This variation treats it as a motivation problem: a model that understands *why* the CHECKER ALGORITHM block is necessary produces a more substantive and correctly-formed block than a model that follows a template. The inertia framing anchors the CHECKER ALGORITHM against the status quo — ad-hoc scope checking where the comparison predicate lives only in the analyst's head and scope discrepancies require re-reading Steps 3, 8a, and 11 simultaneously. The formal declarative register ("The CHECKER ALGORITHM block is the machine-readable encoding of...") frames each token as a solution to a specific opacity problem, not a bureaucratic field. The pre-printed skeleton provides structural enforcement. Combined: motivation (inertia framing) + structure (pre-printed skeleton) + register (declarative, not imperative). Expected: C-37 PASS with the most substantive MATCH-RULE/HALT-RULE/OUTPUT-RULE phrase quality among R14 variations. Risk: the inertia framing section expands the prompt and may cause the model to produce the CHECKER ALGORITHM correctly in the framing section but produce a compressed or prose version in the Step 8 Header.

---

The following prompt is in declarative register. Every structural requirement is stated as a property of the output, not as an imperative instruction to the model.

---

**Trace Identity**

| Field | Value |
|-------|-------|
| Platform domain | `[Dataverse / Commerce / Automate — auto-selected from request context]` |
| Trace scope | `[one sentence: the request and the system it traverses]` |

---

**Status-Quo Reference**

Without a machine-readable CHECKER ALGORITHM, scope string verification requires an analyst to hold three sections in working memory simultaneously — Step 3 (declared scopes), Step 8a (invoked scopes), and Step 11 (downstream params) — and mentally execute the comparison predicate without a declared algorithm. Scope discrepancies at any boundary are detectable only by reading prose. A CHECKER ALGORITHM block with MATCH-RULE, HALT-RULE, and OUTPUT-RULE as named machine-greppable tokens encodes the comparison predicate once, at Step 8 Header, such that the checker contract is fully recoverable from structure alone. This trace produces that block.

---

**Step 0 — Entry Point**

| Caller | Endpoint | Verb | Receiver |
|--------|----------|------|--------------------|
|        |          |      |                    |

The trace begins at the entry point. No boundary is omitted from this point forward.

---

**Step 1 — Authentication**

| Token Type | Issuer | Presentation | Auth Component |
|------------|--------|--------------|----------------|
|            |        |              |                |

---

**Step 2 — Routing**

| Order | Component | Type | Status-Quo Alternative Bypassed |
|-------|-----------|------|--------------------------------|
| 1     |           |      | `[what ad-hoc routing would miss]` |

---

**Step 3 — Auth Scope Declaration**

The token is decoded. Every permission scope appears as a quoted exact string. These strings are the VT-N reference set for Step 8.

```
Declared scopes:
1. "[exact scope string]"
2. "[exact scope string]"
...
```

The property of Step 3 output: every VT-N token in Step 8 Header is a verbatim copy of a line from this list. Any VT-N value not present in this list is a scope assertion with no Step 3 basis.

---

**Steps 4–7 — Boundary Traversal**

| Step | Boundary | Component | Gap? | Auth Required | Latency Source? | Batch Edge Case? | Status-Quo Risk If Deferred |
|------|----------|-----------|------|---------------|-----------------|------------------|-----------------------------|
| 4    |          |           | Y/N  |               | Y/N             | Y/N              |                             |
| 5    |          |           | Y/N  |               | Y/N             | Y/N              |                             |
| 6    |          |           | Y/N  |               | Y/N             | Y/N              |                             |
| 7    |          |           | Y/N  |               | Y/N             | Y/N              |                             |

Gap? = Y: the invoked auth scope at this boundary may not match the Step 3 declared scope. Every Gap?=Y row produces a Step 8c verification row.

The Status-Quo Risk column names what happens if the boundary gap is left unverified — the condition that a manually-executed scope check would silently miss.

---

**Step 8 — Scope String Verification**

The CHECKER ALGORITHM block is the machine-readable encoding of the scope verification predicate. It appears in the Step 8 Header immediately after TOKEN-COUNT. Its three tokens encode: (1) the comparison predicate that determines Match? (MATCH-RULE), (2) the halt condition that determines Row-Verdict (HALT-RULE), and (3) the output emission rule that determines CHECK RESULT (OUTPUT-RULE). Without these tokens, the Step 8c table can be read but cannot be automatically checked — the checker contract exists only as analyst intent.

**Step 8 Header**

```
VT-1: "[exact scope string — verbatim from Step 3 line 1]"
VT-2: "[exact scope string — verbatim from Step 3 line 2]"
...
TOKEN-COUNT: [N — equals the count of VT-N lines; self-validates schema completeness]
CHECKER ALGORITHM:
  MATCH-RULE: [the comparison predicate — one machine-greppable phrase encoding Match? = Y condition]
  HALT-RULE: [the halt trigger — one machine-greppable phrase encoding Row-Verdict = HALT condition]
  OUTPUT-RULE: [the output rule — one machine-greppable phrase encoding CHECK RESULT = PASS/FAIL condition]
```

The CHECKER ALGORITHM block is structurally independent of VT-N values: its three token phrases are interpretable from the label names alone without reading any VT-N line. The algorithm logic is the same regardless of which specific scope strings appear as VT-N tokens.

[GATE-8H: Step 8 Header is incomplete if TOKEN-COUNT is not immediately followed by CHECKER ALGORITHM, if any of the three tokens is absent, if any token value is a prose paragraph rather than a machine-greppable phrase, or if the block appears anywhere other than the Step 8 Header section.]

**Step 8a — Invoked Scope**

For each Gap?=Y boundary, the scope string actually invoked by the service call is stated as an exact quoted string.

| Gap?=Y Boundary | Invoked Scope (exact quoted) | Status-Quo Opacity |
|-----------------|------------------------------|-------------------|
|                 |                              | `[what an ad-hoc check would need to read to find this]` |

**Step 8b — Coherence Confirmation (REQUIRED per Gap?=Y boundary)**

The three link arms are confirmed before Step 9 proceeds. All three are required — a confirmation that names only one or two arms does not satisfy this requirement.

```
Boundary: [reference]
  Step 3 Auth → Step 8a Invoked: [coherent / CONTRADICTION -- describe]
  Step 8a Invoked → Step 11 Params: [coherent / CONTRADICTION -- describe]
  Step 8a Invoked → Step 7/9 Boundary: [coherent / CONTRADICTION -- describe]
REQUIRED: Step 9 does not begin until all three link arms are confirmed for every Gap?=Y boundary.
```

**Step 8c — Scope String Coherence Table**

The table encodes the CHECKER ALGORITHM execution. Match? is computed from the MATCH-RULE. Row-Verdict is set from the HALT-RULE. CHECK RESULT is computed from the OUTPUT-RULE.

| Seq# | Step3-Auth | Step8a-Invoked | Step11-Params | Match? | Row-Verdict |
|------|------------|----------------|---------------|--------|-------------|
| 1    |            |                |               | Y/N    | PASS / HALT |

On any Row-Verdict = HALT — a scope discrepancy that an unstructured trace would carry forward silently:
```
CONTRADICTION SIGNAL: Seq# [N]
Rem#: Scope String Correction -- [the correction required before the trace may advance]
```

After the table:
```
CHECK RESULT: [PASS / FAIL] -- [N] rows, [M] HALT rows
```

---

**Step 9 — Downstream Service Call**

Step 9 is the first post-verification step. It begins only when Step 8b REQUIRED CONFIRMATIONs are complete.

| Target Service | Params | Connection Method | Response Shape |
|----------------|--------|-------------------|----------------|
|                |        |                   |                |

---

**Step 10 — Storage Access**

| Entity/Table | Operation | Connector/SDK | Notes |
|--------------|-----------|---------------|-------|
|              |           |               |       |

---

**Step 11 — Response Assembly**

| Field | Shape | Transformation | Error Shape |
|-------|-------|----------------|-------------|
|       |       |                |             |

Params used in the upstream → downstream call appear here (feeds Step 8c Step11-Params column).

---

**Step 12 — Findings**

The findings surface what a manually-executed trace would miss or defer. Each row names the failure mode explicitly.

| # | Finding | Boundary | Failure Mode | Latency Source | Severity | Fix | Status-Quo if Deferred |
|---|---------|----------|--------------|----------------|----------|-----|------------------------|
| F-01 |     |          |              | Y/N            |          |     |                        |

[GATE-12: "No issues found" does not close. "Minor concerns" does not close. Status-Quo if Deferred column required per row. CLEAN TRACE required if no findings.]
