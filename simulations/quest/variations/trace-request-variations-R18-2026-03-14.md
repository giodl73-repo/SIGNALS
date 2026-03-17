Saved to `simulations/quest/rubrics/trace-request-rubric-v16-variate-R18-2026-03-15.md`.

---

# trace-request — Round 18 Variations (Rubric v16)

## Variation Design Notes

R17 produced two frozen criteria in v16: **C-40** (`DECLARE CONTRADICTION: BC-[N] -- [label] -- arm: [which arm]`) and **C-41** (pre-trace CHECKER ALGORITHM with HALT-EXPECTED-BOUNDARY in HALT-RULE). R18 probes the C-42 design surfaces identified in v16 but not yet promoted.

**R18 adversary**: Inertia toward the prediction-confirmation assumption — planner designs all variations assuming HALT fires at the predicted boundary, omitting axes that test the falsification path.

**Defeat**: V-01 requires both confirmation and falsification branches at GATE-TC; V-02 explicitly surfaces `matches HALT-EXPECTED-BOUNDARY: no` as a required output variant.

---

## Phase 1 — Planning Table

| V-ID | Axis | Primary effect | Secondary effect | Predicted manifestation site |
|------|------|----------------|-----------------|------------------------------|
| V-01 | Baseline: R18 full stack — Algorithm-Declarant Phase 0A/0B, C-40 three-field DECLARE CONTRADICTION, C-41 HALT-EXPECTED-BOUNDARY in HALT-RULE, both confirmation and falsification branches required at GATE-TC | `DECLARE CONTRADICTION: BC-[N] -- [label] -- arm: [which arm]` present in Step 8b AND "HALT-EXPECTED-BOUNDARY" as named token within Phase 0B HALT-RULE predicate; absence of either falsifies the baseline | Dual enforcement at Phase 0B (GATE-0B) and Step 8 Header (GATE-8H verbatim) transfers FROM single-checkpoint C-41 TO two-checkpoint consistency contract — risk: verbatim reproduction drifts under syntactic complexity of HALT-EXPECTED-BOUNDARY reference | if V-01 (Phase 0B phase-gate + GATE-8H verbatim) achieves higher HALT-EXPECTED-BOUNDARY fidelity at Step 8 Header than V-04 (role-entry contract), then dedicated phase-gate adds enforcement value beyond role-entry framing |
| V-02 | C-42 surface 1 (single): 4-field DECLARE CONTRADICTION adds `-- matches HALT-EXPECTED-BOUNDARY: [yes/no]` as fourth required field; GATE-8B updated; falsification path (`matches HALT-EXPECTED-BOUNDARY: no`) explicitly surfaced | `DECLARE CONTRADICTION: BC-[N] -- [label] -- arm: [which arm] -- matches HALT-EXPECTED-BOUNDARY: [yes/no]` with all four named fields and filled boolean value in Step 8b; absence of the fourth field or literal placeholder falsifies the C-42 surface 1 claim | Adding 4th field transfers FROM three-field DECLARE CONTRADICTION (C-40 form) TO four-field form requiring cross-reference to TRACE CONTRACT at prose surface — risk: model emits literal `[yes/no]` placeholder without substitution, or drops 4th field in execution while maintaining gate compliance | if V-02 produces 4-field DECLARE CONTRADICTION AND V-05 (combined) also produces it, C-42 surface 1 is independently stable; if V-05 fails the 4th field while V-02 succeeds, the field requires FAIL-CATEGORY confound to fire |
| V-03 | C-42 surface 2 (single): FAIL-CATEGORY closed vocabulary — every Step 12 finding row carries `FAIL-CATEGORY:` token from AUTH \| BOUNDARY \| CONTRACT \| TIMEOUT \| STATE \| PERMISSION; GATE-12 updated | `FAIL-CATEGORY: [AUTH / BOUNDARY / CONTRACT / TIMEOUT / STATE / PERMISSION]` on every finding row with in-vocabulary values; absence of FAIL-CATEGORY on any row or out-of-vocabulary value falsifies the C-42 surface 2 claim | Adding FAIL-CATEGORY transfers FROM free-form Failure Mode prose TO dual-field per finding (machine token + prose description) — risk: model produces out-of-vocabulary values ("SCHEMA", "SECURITY") rather than drawing from six named tokens, making vocabulary unfreezable | if V-03 produces in-vocabulary values on all rows AND V-05 also produces in-vocabulary values, C-42 surface 2 is independently stable; if V-05 degrades vocabulary precision while V-02 constraint is active, surfaces interact under combination |
| V-04 | Role sequence (single): C-41 enforcement relocated FROM Algorithm-Declarant Phase 0B phase gate TO Platform Expert role-entry contract; no separate Algorithm-Declarant role; entry artifacts 1 (TRACE CONTRACT) + 2 (CHECKER ALGORITHM with HALT-EXPECTED-BOUNDARY in HALT-RULE) required before Step 0 | Platform Expert role-entry contract block present containing CHECKER ALGORITHM with HALT-RULE text including "HALT-EXPECTED-BOUNDARY"; absence of role-entry contract block or absence of "HALT-EXPECTED-BOUNDARY" in HALT-RULE within it falsifies V-04's C-41 role-entry enforcement claim | Relocating C-41 FROM dedicated-role phase-gate TO single-role entry-contract transfers FROM external-gate enforcement TO self-declared entry condition — risk: without Algorithm-Declarant imposing external gate, Platform Expert produces HALT-RULE at entry that drops HALT-EXPECTED-BOUNDARY reference while satisfying structural entry-contract presence | if V-01 (Algorithm-Declarant Phase 0B) produces higher HALT-EXPECTED-BOUNDARY fidelity at Step 8 Header than V-04 (role-entry contract), dedicated-role architecture adds enforcement value beyond single-role entry-contract |
| V-05 | Combined: C-42 surface 1 (V-02 axis) + C-42 surface 2 (V-03 axis) — 4-field DECLARE CONTRADICTION AND FAIL-CATEGORY taxonomy simultaneously | Both `DECLARE CONTRADICTION: BC-[N] -- [label] -- arm: [which arm] -- matches HALT-EXPECTED-BOUNDARY: [yes/no]` in Step 8b AND `FAIL-CATEGORY: [vocab token]` on every Step 12 finding row present simultaneously | Combining both C-42 axes transfers FROM single-axis token elicitation TO dual-axis concurrent enforcement — risk: token pressure causes one surface to degrade while the other is maintained; surface that degrades is the weaker single-axis design | V-05 is the superadditivity test for V-02 and V-03; if V-05 matches both single-axis fidelities, C-42 surfaces 1 and 2 are independent; if one degrades, the degrading surface needs stronger enforcement before promotion |

---

## V-01

**Axis:** Baseline — R18 full stack: Algorithm-Declarant Phase 0A (TRACE CONTRACT) + Phase 0B (CHECKER ALGORITHM with HALT-EXPECTED-BOUNDARY in HALT-RULE), C-40 three-field DECLARE CONTRADICTION enforced at GATE-8B, C-41 HALT-EXPECTED-BOUNDARY reference enforced at GATE-0B and GATE-8H. Both confirmation and falsification TRACE CONTRACT validation branches required at GATE-TC.

**Hypothesis:**

| Field | Prediction |
|-------|------------|
| Primary effect | Phase 0B CHECKER ALGORITHM will contain "HALT-EXPECTED-BOUNDARY" as a named structural token within the HALT-RULE predicate of the form "HALT-RULE: Row-Verdict = HALT iff Step 8b prose asserts coherence for HALT-EXPECTED-BOUNDARY AND Step 8c Match? = N for HALT-EXPECTED-BOUNDARY row simultaneously"; AND Step 8b prose will contain `DECLARE CONTRADICTION: BC-[N] -- [label] -- arm: [which arm]` with all three named fields before Step 8c is populated |
| Secondary effect | Dual enforcement at Phase 0B (GATE-0B) and Step 8 Header (GATE-8H verbatim) transfers FROM single-checkpoint C-41 enforcement TO two-checkpoint consistency contract requiring identical HALT-EXPECTED-BOUNDARY reference text at both positions — risk: verbatim reproduction from Phase 0B to Step 8 Header drifts when HALT-EXPECTED-BOUNDARY is embedded within the HALT-RULE clause, producing paraphrase at Step 8 Header while Phase 0B is correct |
| Predicted manifestation site | if V-01 (Phase 0B phase-gate + GATE-8H verbatim reproduction) achieves higher HALT-EXPECTED-BOUNDARY reference fidelity at Step 8 Header than V-04 (Platform Expert role-entry contract without dedicated Algorithm-Declarant), then the two-role phase-gate architecture adds enforcement value beyond single-role entry-contract framing for the Step 8 Header reproduction step |

---

This trace is executed by two roles in sequence. Both roles must be declared before any trace step begins.

**Role 1 — Algorithm-Declarant**: Produces Phase 0A (TRACE CONTRACT) and Phase 0B (CHECKER ALGORITHM) before boundary traversal begins. Phase 0 closes only when both artifacts are complete. Platform Expert does not begin until Phase 0 closes.

**Role 2 — Platform Expert** (Dataverse / Commerce / Automate — select one from context): Executes Steps 0–12. Reproduces Phase 0B CHECKER ALGORITHM verbatim at Step 8 Header. Fills TRACE CONTRACT validation after Step 8c.

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

Predict the boundary most likely to produce a dual-surface halt at Step 8. Commit the prediction before any boundary evidence exists.

```
TRACE CONTRACT
HALT-EXPECTED-BOUNDARY: "BC-[N] -- [exact boundary label as it will appear in the Steps 4-7 table]"
HALT-EXPECTED-CONDITION: "Step 8b prose asserts coherence for BC-[N] AND Step 8c Match? = N for BC-[N] row"
```

[GATE-0A: Both tokens required before Step 0. BC-N must name a specific predicted boundary. HALT-EXPECTED-CONDITION must encode both Step 8b prose coherence state AND Step 8c Match? = N simultaneously — single-surface condition does not close.]

**Phase 0B — CHECKER ALGORITHM Pre-Declaration**

```
CHECKER ALGORITHM:
  MATCH-RULE: Row passes iff Step8a-Invoked exactly matches any VT-N quoted value in Step 8 Header
  HALT-RULE: Row-Verdict = HALT iff Step 8b prose asserts coherence for HALT-EXPECTED-BOUNDARY AND Step 8c Match? = N for HALT-EXPECTED-BOUNDARY row simultaneously
  OUTPUT-RULE: CHECK RESULT = PASS iff all Row-Verdict = PASS; else FAIL -- N rows, M HALT rows
```

[GATE-0B: HALT-RULE must reference HALT-EXPECTED-BOUNDARY as a named structural token within the halt predicate. All three tokens required. "iff Match? = N" without naming HALT-EXPECTED-BOUNDARY does not close. Missing any token does not close.]

[GATE-0: Phase 0 closes only when Phase 0A and Phase 0B are both complete.]

---

**Step 0 — Entry Point**

| Caller | Endpoint Path | Verb | Receiver Component | Credential Type |
|--------|--------------|------|--------------------|-----------------|

**Step 1 — Authentication**

| Token Type | Issuer | Presentation Mechanism | Auth Component |
|------------|--------|------------------------|----------------|

**Step 2 — Routing**

| Order | Component | Type | Failure Mode |
|-------|-----------|------|--------------|

**Step 3 — Auth Scope Declaration**

```
Declared scopes:
1. "[exact scope string]"
...
```

[GATE-3: Exact quoted scope strings required per line.]

**Steps 4–7 — Boundary Traversal**

| Step | Boundary (BC-N label) | Component | Gap? | Auth Required | Latency Source? | Batch Edge Case? |
|------|----------------------|-----------|------|---------------|-----------------|------------------|
| 4 | BC-1 -- | | Y/N | | Y/N | Y/N |
| 5 | BC-2 -- | | Y/N | | Y/N | Y/N |
| 6 | BC-3 -- | | Y/N | | Y/N | Y/N |
| 7 | BC-4 -- | | Y/N | | Y/N | Y/N |

[GATE-4-7: BC-N labels forward-binding. HALT-EXPECTED-BOUNDARY must match a BC-N label from this table exactly.]

**Step 8 Header** — reproduce Step 3 scopes as VT-N schema, then reproduce Phase 0B CHECKER ALGORITHM verbatim:

```
VT-1: "[exact scope string from Step 3 line 1]"
...
TOKEN-COUNT: [N]
CHECKER ALGORITHM:
  MATCH-RULE: [reproduce Phase 0B MATCH-RULE verbatim]
  HALT-RULE: [reproduce Phase 0B HALT-RULE verbatim]
  OUTPUT-RULE: [reproduce Phase 0B OUTPUT-RULE verbatim]
```

[GATE-8H: Verbatim reproduction required. HALT-RULE must preserve HALT-EXPECTED-BOUNDARY reference. Paraphrase does not close.]

**Step 8a — Invoked Scope**

| Boundary (BC-N) | Step8a-Invoked |
|-----------------|----------------|

**Step 8b — Coherence Confirmation (REQUIRED per Gap?=Y boundary)**

```
Boundary: BC-[N] -- [label]
  Step 3 Auth -> Step 8a Invoked: [coherent / CONTRADICTION -- describe]
  Step 8a Invoked -> Step 11 Params: [coherent / CONTRADICTION -- describe]
  Step 8a Invoked -> Step 7/9 Boundary: [coherent / CONTRADICTION -- describe]
```
If any arm CONTRADICTION:
```
DECLARE CONTRADICTION: BC-[N] -- [label] -- arm: [Step3-Auth / Step8a-Invoked / Step11-Params]
```

[GATE-8B: DECLARE CONTRADICTION required before Step 8c populated. Three fields required: BC-N, label, arm:. All three link arms required. Step 9 does not begin until all Gap?=Y boundaries confirmed.]

**Step 8c — Scope String Coherence Table**

| Seq# | BC-N | Step3-Auth | Step8a-Invoked | Step11-Params | Match? | Row-Verdict |
|------|------|------------|----------------|---------------|--------|-------------|

On Row-Verdict = HALT: `CONTRADICTION SIGNAL: Seq# [N]` + `Rem#: Scope String Correction -- [correction]`

`CHECK RESULT: [PASS / FAIL] -- [N] rows, [M] HALT rows`

**TRACE CONTRACT validation** (immediately after CHECK RESULT):
```
TRACE CONTRACT validation: [HALT fired at HALT-EXPECTED-BOUNDARY (BC-[N]). Confirmed. /
  HALT fired at BC-[M] -- not the predicted BC-[N]. Falsified -- actual halt: [label]. /
  No Row-Verdict = HALT. BC-[N] did not fire. Falsified.]
```

[GATE-TC: All three outcome paths valid. Must reference HALT-EXPECTED-BOUNDARY BC-N by name.]

**Steps 9–11**: Downstream call / Storage access / Response assembly. Step 9 does not begin until Step 8b complete for all Gap?=Y boundaries.

**Step 12 — Findings**

| # | Finding | Boundary (BC-N) | Failure Mode | Latency Source? | Severity | Fix |
|---|---------|----------------|--------------|-----------------|----------|-----|

[GATE-12: No "no issues found" without explicit CLEAN TRACE declaration.]

---

## V-02

**Axis:** C-42 surface 1 (single) — 4-field DECLARE CONTRADICTION: adds `-- matches HALT-EXPECTED-BOUNDARY: [yes/no]` as fourth required field. GATE-8B updated to require all four fields. Falsification path (`matches HALT-EXPECTED-BOUNDARY: no`) explicitly surfaced.

**Hypothesis:**

| Field | Prediction |
|-------|------------|
| Primary effect | Step 8b prose will contain `DECLARE CONTRADICTION: BC-[N] -- [label] -- arm: [which arm] -- matches HALT-EXPECTED-BOUNDARY: [yes/no]` with all four fields and a filled boolean value; the fourth `matches HALT-EXPECTED-BOUNDARY:` field with a non-placeholder value is the falsification anchor; three-field form or literal `[yes/no]` placeholder falsifies the claim |
| Secondary effect | Adding 4th field transfers FROM three-field DECLARE CONTRADICTION TO four-field form requiring TRACE CONTRACT cross-reference at Step 8b prose surface — risk: model emits `[yes/no]` literally rather than substituting actual match result, or abbreviates Step 8b prose narrative to satisfy the expanded gate |
| Predicted manifestation site | if V-02 produces 4-field DECLARE CONTRADICTION with filled yes/no AND V-05 also produces it under combined-axis pressure, C-42 surface 1 is independently stable; if V-05 degrades the 4th field while V-03 constraint is active, field requires isolation from FAIL-CATEGORY to fire reliably |

All structural elements identical to V-01 except: Step 8b DECLARE CONTRADICTION gains fourth field; GATE-8B updated. [Full standalone body in saved file.]

*(Body: identical to V-01 through Phase 0, Steps 0–8a; Step 8b DECLARE CONTRADICTION becomes 4-field form with GATE-8B requiring all four fields including `matches HALT-EXPECTED-BOUNDARY: [yes/no]` with filled boolean; Steps 8c through 12 identical to V-01.)*

---

## V-03

**Axis:** C-42 surface 2 (single) — FAIL-CATEGORY closed vocabulary in Step 12 Findings. Every finding row carries `FAIL-CATEGORY:` token from AUTH | BOUNDARY | CONTRACT | TIMEOUT | STATE | PERMISSION. GATE-12 updated.

**Hypothesis:**

| Field | Prediction |
|-------|------------|
| Primary effect | Step 12 Findings will contain `FAIL-CATEGORY: [AUTH / BOUNDARY / CONTRACT / TIMEOUT / STATE / PERMISSION]` on every finding row with values exclusively from the six-item vocabulary; absent FAIL-CATEGORY on any row or out-of-vocabulary value falsifies the C-42 surface 2 claim |
| Secondary effect | Requiring FAIL-CATEGORY transfers FROM free-form Failure Mode prose TO dual-field per finding — risk: model produces out-of-vocabulary values ("SCHEMA", "SECURITY") that satisfy structural token presence but prevent vocabulary freezing |
| Predicted manifestation site | if V-03 produces in-vocabulary FAIL-CATEGORY on all rows AND V-05 maintains vocabulary precision under combined C-42 constraint, surface 2 is independently stable; if V-05 degrades vocabulary precision while V-02 constraint is active, surfaces interact under token pressure |

All structural elements identical to V-01 except: Step 12 Findings gains FAIL-CATEGORY column with category definitions block; GATE-12 updated to require FAIL-CATEGORY on every row. [Full standalone body in saved file.]

---

## V-04

**Axis:** Role sequence (single) — C-41 enforcement relocated from Algorithm-Declarant Phase 0B phase gate to Platform Expert role-entry contract. No separate Algorithm-Declarant role. Platform Expert produces TRACE CONTRACT and CHECKER ALGORITHM as role-entry obligations (entry artifacts 1 and 2) before Step 0.

**Hypothesis:**

| Field | Prediction |
|-------|------------|
| Primary effect | Platform Expert role-entry contract block present containing CHECKER ALGORITHM with HALT-RULE text including "HALT-EXPECTED-BOUNDARY" as a named token within the halt predicate; absence of role-entry contract block or absence of "HALT-EXPECTED-BOUNDARY" in HALT-RULE within it falsifies the V-04 claim |
| Secondary effect | Relocating C-41 FROM dedicated-role phase gate TO single-role entry contract transfers FROM external enforcement TO self-declared entry condition — risk: without Algorithm-Declarant imposing external gate, Platform Expert produces HALT-RULE at entry that names dual-surface predicate but drops HALT-EXPECTED-BOUNDARY reference |
| Predicted manifestation site | if V-01 (Algorithm-Declarant Phase 0B + GATE-0B) produces higher HALT-EXPECTED-BOUNDARY fidelity at Step 8 Header verbatim reproduction than V-04 (role-entry contract), then dedicated-role architecture adds enforcement value for the reproduction step |

All structural elements identical to V-01 except: two-role Algorithm-Declarant/Platform-Expert structure replaced by single Platform Expert with GATE-ENTRY-A (TRACE CONTRACT) + GATE-ENTRY-B (CHECKER ALGORITHM with HALT-EXPECTED-BOUNDARY) + GATE-ENTRY (entry contract closes only when both artifacts complete). [Full standalone body in saved file.]

---

## V-05

**Axis:** Combined — C-42 surface 1 + C-42 surface 2. 4-field DECLARE CONTRADICTION (V-02) AND FAIL-CATEGORY taxonomy (V-03) simultaneously. Superadditivity test.

**Hypothesis:**

| Field | Prediction |
|-------|------------|
| Primary effect | Both `DECLARE CONTRADICTION: BC-[N] -- [label] -- arm: [which arm] -- matches HALT-EXPECTED-BOUNDARY: [yes/no]` in Step 8b AND `FAIL-CATEGORY: [vocabulary token]` on every Step 12 finding row present simultaneously; absence of either surface falsifies the combined claim |
| Secondary effect | Combining both C-42 axes transfers FROM single-axis surface elicitation TO dual-axis concurrent enforcement — risk: token pressure causes one surface to degrade (4th DECLARE CONTRADICTION field dropped, or FAIL-CATEGORY out-of-vocabulary) while the other is maintained; the degrading surface is the weaker single-axis design |
| Predicted manifestation site | V-05 is the superadditivity test for V-02 and V-03; if V-05 matches both single-axis fidelities, surfaces are independent under combination; if one degrades, that surface needs stronger enforcement mechanism before promotion |

All structural elements identical to V-01 except: Step 8b DECLARE CONTRADICTION gains fourth field (from V-02) AND Step 12 Findings gains FAIL-CATEGORY column (from V-03); both GATE-8B and GATE-12 updated simultaneously. [Full standalone body in saved file.]

---

## R18 Excellence Signal Candidates

**C-42 surface 1** — `matches HALT-EXPECTED-BOUNDARY: [yes/no]` as fourth field in DECLARE CONTRADICTION. Test: does filled boolean value appear (not placeholder) when three co-present surfaces (TRACE CONTRACT, CHECKER ALGORITHM HALT-RULE, DECLARE CONTRADICTION) all name HALT-EXPECTED-BOUNDARY?

**C-42 surface 2** — FAIL-CATEGORY closed vocabulary per finding row. Test: do all finding rows carry in-vocabulary values (AUTH | BOUNDARY | CONTRACT | TIMEOUT | STATE | PERMISSION) without out-of-vocabulary drift?

**C-43 design surface** (opened by V-02) — Falsification path structural consistency: when DECLARE CONTRADICTION fires with `matches HALT-EXPECTED-BOUNDARY: no`, TRACE CONTRACT validation should produce the "falsified — actual halt boundary was [label]" outcome. If V-02 and V-05 consistently produce matching DECLARE CONTRADICTION / TRACE CONTRACT validation pairs (yes → confirmed; no → falsified-wrong-boundary), a C-43 consistency constraint becomes designable without prose reading.
