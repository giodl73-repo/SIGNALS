# trace-request — Round 18 Variations (Rubric v16)

**Skill**: trace-request — Hand-compile a request through service boundaries, APIs, and middleware.
**Rubric**: v16 (C-40 + C-41 now frozen; C-42 design surfaces under probe)
**Date**: 2026-03-15

---

## Variation Design Notes

R17 produced two frozen criteria in v16:

- **C-40**: `DECLARE CONTRADICTION: BC-[N] -- [label] -- arm: [which arm]` as a named structural token in Step 8b prose at the contradiction boundary row, emitted before Step 8c is populated. Evidence: V-02 (single-axis formal register) and V-05 (three-axis combined) both produced the three-field token form stably.
- **C-41**: CHECKER ALGORITHM block declared pre-trace (before Step 0) with HALT-RULE explicitly naming `HALT-EXPECTED-BOUNDARY` as a structural token within the halt predicate. Evidence: V-04's Algorithm-Declarant role (Phase 0B) emitted HALT-RULE referencing HALT-EXPECTED-BOUNDARY by name.

**R18 C-42 design surfaces under probe:**

| Surface | Tier | Target variations |
|---------|------|------------------|
| Enhanced DECLARE CONTRADICTION with `-- matches HALT-EXPECTED-BOUNDARY: [yes/no]` intertextual cross-reference field | B+ | V-02, V-05 |
| Error path category taxonomy: `FAIL-CATEGORY:` token on each Step 12 Finding row, drawn from named vocabulary AUTH \| BOUNDARY \| CONTRACT \| TIMEOUT \| STATE \| PERMISSION | D (promotability test) | V-03, V-05 |

**C-42 intertextual field design rationale**: When C-39 (HALT-EXPECTED-BOUNDARY in TRACE CONTRACT) AND C-41 (HALT-EXPECTED-BOUNDARY in HALT-RULE) are both present, the Step 8b DECLARE CONTRADICTION event is structurally linkable to the pre-declared prediction without prose reading. Adding `-- matches HALT-EXPECTED-BOUNDARY: [yes/no]` as a fourth field creates a machine-checkable cross-reference: did the contradiction event fire at the predicted boundary? V-05 (R17) produced this field as a V-05-only surface, but only in combined-axis form. R18 targets the field under single-axis C-42 surface 1 isolation to test whether it appears without the combined-axis confound.

**C-42 FAIL-CATEGORY design rationale**: Step 12 Findings currently classifies findings by Severity and Failure Mode (both prose fields). A named machine-greppable FAIL-CATEGORY token would make finding classification checkable without prose reading. R18 tests whether specifying a closed vocabulary (AUTH | BOUNDARY | CONTRACT | TIMEOUT | STATE | PERMISSION) and requiring a FAIL-CATEGORY: token per finding row produces a stable machine-greppable surface. If FAIL-CATEGORY appears reliably with consistent vocabulary draws, the criterion becomes promotable once the vocabulary is frozen.

**Adversary for R18**: Inertia toward the prediction-confirmation assumption — the planner designs all variations assuming the TRACE CONTRACT prediction fires (HALT at predicted boundary), omitting a variation that explicitly structures the falsification path (prediction wrong, HALT fires elsewhere, or no HALT fires). A variation set in which all five variations assume the prediction confirms cannot distinguish structural enforcement of the falsification token path from the confirmation path.

**R18 variation surface:**

| V | Axis | Single/Combined | C-42 probe | Adversary address |
|---|------|-----------------|------------|-------------------|
| V-01 | Baseline: R18 full stack — C-40 + C-41, Algorithm-Declarant Phase 0A/0B | Baseline | None | Confirmation + falsification branches both required at GATE-TC |
| V-02 | C-42 surface 1: 4-field DECLARE CONTRADICTION with HALT-EXPECTED-BOUNDARY match flag | Single | C-42 surface 1 | Falsification branch explicit: `matches HALT-EXPECTED-BOUNDARY: no` path surfaced |
| V-03 | C-42 surface 2: FAIL-CATEGORY taxonomy in Step 12 Findings | Single | C-42 surface 2 | Not primary; GATE-12 clean-trace declaration still required |
| V-04 | Role sequence: C-41 enforcement as Platform Expert role-entry contract (not Algorithm-Declarant phase) | Single | None | Falsification path in TRACE CONTRACT validation remains GATE-TC-POST enforced |
| V-05 | Combined: C-42 surface 1 + C-42 surface 2 | Combined | Both C-42 surfaces | Both `matches HALT-EXPECTED-BOUNDARY:` and `FAIL-CATEGORY:` required; superadditivity test |

---

## Phase 1 — Planning Table

*Prevents: axis drift where later variations co-vary multiple structural elements without combination labeling; primary-effect cells that describe direction rather than naming falsifiable structural properties; predicted-site cells that name no sibling V-ID*

ADVERSARY: Inertia toward the prediction-confirmation assumption — the planner designs all axes assuming the HALT fires at the predicted boundary, omitting variation axes that test the falsification path (HALT fires at a non-predicted boundary, or no HALT fires). An axis that assumes only the confirmation path cannot distinguish structural enforcement of the falsification token from the confirmation token.

DEFEAT CONDITION: At least one planning-table row names a variation axis that explicitly addresses the falsification path — structuring the case where `matches HALT-EXPECTED-BOUNDARY: no` fires or TRACE CONTRACT validation declares falsification.

| V-ID | Axis | Primary effect (name one specific structural property whose absence in the actual body would clearly falsify this claim) | Secondary effect (FROM which structural element / TO which structural element risk transfers) | Predicted manifestation site (name at least one sibling V-ID with if-then conditional structure) |
|------|------|---|---|---|
| V-01 | Baseline: R18 full stack — Algorithm-Declarant Phase 0A/0B with C-40 three-field DECLARE CONTRADICTION and C-41 HALT-EXPECTED-BOUNDARY in HALT-RULE; both confirmation and falsification TRACE CONTRACT validation branches required at GATE-TC | `DECLARE CONTRADICTION: BC-[N] -- [label] -- arm: [which arm]` present as a named structural token in Step 8b prose at the contradiction boundary before Step 8c is populated, AND HALT-RULE text contains the exact phrase "HALT-EXPECTED-BOUNDARY" as a named token within the halt predicate clause in Phase 0B; absence of either falsifies the baseline claim | Adding C-41 enforcement (HALT-EXPECTED-BOUNDARY in HALT-RULE) to the Phase 0B constraint transfers FROM single-surface HALT-RULE authorship freedom TO a constrained HALT-RULE template that names the predicted boundary — risk: model produces HALT-RULE with HALT-EXPECTED-BOUNDARY in Phase 0B but drops the reference during verbatim reproduction at Step 8 Header, producing C-41 FAIL at the header surface | if V-01 (full Phase 0B enforcement with GATE-0B requiring HALT-EXPECTED-BOUNDARY reference) produces verbatim reproduction at Step 8 Header with higher fidelity than V-04 (role-entry contract enforcement without Phase 0B phase gate), then the Phase 0B explicit gate adds enforcement value beyond role-entry framing alone; if fidelity is equivalent, the gate is redundant |
| V-02 | C-42 surface 1 (single): 4-field DECLARE CONTRADICTION — adds `-- matches HALT-EXPECTED-BOUNDARY: [yes/no]` as a fourth required field to the C-40 three-field form; GATE-8B updated to require all four fields; falsification path (`matches HALT-EXPECTED-BOUNDARY: no`) explicitly surfaced as a required output variant | `DECLARE CONTRADICTION: BC-[N] -- [label] -- arm: [which arm] -- matches HALT-EXPECTED-BOUNDARY: [yes/no]` present with all four named fields in Step 8b prose; absence of the fourth `matches HALT-EXPECTED-BOUNDARY:` field falsifies the C-42 surface 1 claim regardless of whether the other three fields appear | Adding the 4th field transfers FROM Step 8b DECLARE CONTRADICTION authorship (three-field form only) TO a four-field form that requires cross-referencing the TRACE CONTRACT prediction at the Step 8b prose surface — risk: model produces the 4-field form in the gate instruction but emits only three fields in actual Step 8b execution, producing C-40 PASS but C-42 surface 1 absent; or model copies `[yes/no]` literally without substituting the actual match result | if V-02's 4-field DECLARE CONTRADICTION appears in Step 8b prose and V-05 (combined) also produces it, then the field is addable as single-axis (V-02 evidence) and stable under combination (V-05 evidence); if V-02 fails to produce the 4th field but V-05 succeeds, the cross-reference requires the FAIL-CATEGORY confound to fire; if both fail, the intertextual surface is not elicitable by instruction alone |
| V-03 | C-42 surface 2 (single): FAIL-CATEGORY taxonomy in Step 12 Findings — every finding row must carry a machine-greppable `FAIL-CATEGORY:` token drawn from the closed vocabulary: AUTH \| BOUNDARY \| CONTRACT \| TIMEOUT \| STATE \| PERMISSION; GATE-12 updated to require FAIL-CATEGORY on every finding row | `FAIL-CATEGORY: [AUTH / BOUNDARY / CONTRACT / TIMEOUT / STATE / PERMISSION]` present as a named token on every finding row in Step 12; absence of FAIL-CATEGORY on any finding row falsifies the C-42 surface 2 claim | Adding FAIL-CATEGORY transfers FROM free-form Failure Mode prose classification TO a closed-vocabulary machine-greppable token field per finding row — risk: model treats FAIL-CATEGORY as a prose label and produces values outside the closed vocabulary (e.g., "SECURITY" or "PERFORMANCE") rather than drawing from the named token set, degrading machine-greppability without producing a clean C-42 surface; secondary risk: GATE-12 requirement for FAIL-CATEGORY may suppress finding quantity as model expends tokens on classification overhead | if V-03 produces FAIL-CATEGORY on every finding row with vocabulary draws exclusively from the named set (AUTH / BOUNDARY / CONTRACT / TIMEOUT / STATE / PERMISSION) and V-05 (combined) also produces it, then the vocabulary constraint is stable under combination; if V-03 produces FAIL-CATEGORY but with non-vocabulary values, the token surface exists but the vocabulary is not freezable as specified |
| V-04 | Role sequence (single): C-41 enforcement relocated from Algorithm-Declarant Phase 0B phase gate TO Platform Expert role-entry contract — the Platform Expert role cannot accept handoff until it declares the CHECKER ALGORITHM with HALT-EXPECTED-BOUNDARY in HALT-RULE as a role-entry artifact; no separate Algorithm-Declarant role; TRACE CONTRACT (Phase 0A equivalent) produced by Platform Expert pre-entry | Platform Expert role-entry contract block present containing CHECKER ALGORITHM with HALT-RULE text including "HALT-EXPECTED-BOUNDARY" as a named token; absence of the role-entry contract block or absence of "HALT-EXPECTED-BOUNDARY" in the HALT-RULE within it falsifies V-04's C-41 role-entry enforcement claim | Relocating C-41 enforcement FROM Algorithm-Declarant Phase 0B (dedicated role producing algorithm as phase closure artifact) TO Platform Expert role-entry contract (single-role architecture where entry condition = algorithm declaration) — risk: without a separate Algorithm-Declarant role imposing an external phase gate, the Platform Expert may produce a CHECKER ALGORITHM at role entry that drops HALT-EXPECTED-BOUNDARY from the HALT-RULE, satisfying the entry contract structurally but not token-specifically; secondary risk: role-entry contract framing (vs. phase-closure framing) may cause verbatim reproduction at Step 8 Header to drift because the entry contract is not named as a "carry" artifact | if V-01 (Algorithm-Declarant Phase 0B gate) produces higher HALT-EXPECTED-BOUNDARY reference fidelity in the Step 8 Header HALT-RULE than V-04 (Platform Expert role-entry contract), the dedicated-role phase-gate enforcement adds enforcement value beyond single-role entry-contract framing; if fidelity is equivalent, phase-gate architecture offers no advantage over role-entry contract for C-41 enforcement |
| V-05 | Combined: C-42 surface 1 + C-42 surface 2 — 4-field DECLARE CONTRADICTION (V-02 axis) AND FAIL-CATEGORY taxonomy in Step 12 (V-03 axis); both GATE-8B update and GATE-12 update applied simultaneously | Both `DECLARE CONTRADICTION: BC-[N] -- [label] -- arm: [which arm] -- matches HALT-EXPECTED-BOUNDARY: [yes/no]` in Step 8b AND `FAIL-CATEGORY: [vocabulary token]` on every Step 12 finding row present simultaneously; absence of either surface in the output falsifies the combined claim | Combining both C-42 axes transfers FROM single-axis surface emergence (V-02: Step 8b cross-reference only; V-03: Step 12 classification only) TO dual-axis concurrent enforcement where both structural modifications are required in the same trace execution — risk: token pressure causes one surface to degrade (shorter Step 8b block losing the 4th field; fewer Step 12 findings each with more classification overhead); if degradation is additive (both surfaces degrade proportionally), V-02 and V-03 are independent; if one surface degrades disproportionately, the surfaces interact under token pressure | V-05 is the superadditivity test for V-02 and V-03; if V-05 produces both surfaces at the same fidelity as V-02 and V-03 individually, C-42 surface 1 and surface 2 are independent under combination; if V-05 produces only one surface reliably, the surfaces interact under combination and the failing surface is the weaker single-axis design |

**Phase 1 STOP CONDITION — all four conditions met:**
1. All five rows complete -- no empty cells in any column. CHECK.
2. At least one Primary-effect cell names a specific, observable structural property (exact phrase or named token). CHECK -- V-01: "DECLARE CONTRADICTION: BC-[N] -- [label] -- arm: [which arm]" and "HALT-EXPECTED-BOUNDARY" exact phrase; V-02: "matches HALT-EXPECTED-BOUNDARY: [yes/no]" as fourth field; V-03: "FAIL-CATEGORY: [AUTH / BOUNDARY / CONTRACT / TIMEOUT / STATE / PERMISSION]"; V-04: "HALT-EXPECTED-BOUNDARY" in role-entry contract block; V-05: both tokens simultaneously.
3. At least one Predicted-manifestation-site cell names a specific sibling V-ID in a conditional if-then structure. CHECK -- V-01 names V-04; V-02 names V-05; V-03 names V-05; V-04 names V-01; V-05 names V-02 and V-03.
4. At least one Axis cell explicitly addresses the falsification path (adversary defeat condition). CHECK -- V-02 explicitly targets `matches HALT-EXPECTED-BOUNDARY: no` as a required output variant; V-01 requires both confirmation and falsification branches at GATE-TC.

---

## Phase 2 — Variation Bodies

---

## V-01

**Axis:** Baseline — R18 full stack: all R17 structures retained (Algorithm-Declarant Phase 0A TRACE CONTRACT + Phase 0B CHECKER ALGORITHM with HALT-EXPECTED-BOUNDARY in HALT-RULE), C-40 three-field DECLARE CONTRADICTION enforced at GATE-8B, C-41 HALT-EXPECTED-BOUNDARY reference enforced at GATE-0B and GATE-8H verbatim reproduction. Both confirmation and falsification branches required at GATE-TC.

**Hypothesis:**

| Field | Prediction |
|-------|------------|
| Primary effect | V-01's Phase 0B CHECKER ALGORITHM block will contain the exact phrase "HALT-EXPECTED-BOUNDARY" as a named structural token within the HALT-RULE predicate (not merely adjacent to it), of the form "HALT-RULE: Row-Verdict = HALT iff Step 8b prose asserts coherence for HALT-EXPECTED-BOUNDARY AND Step 8c Match? = N for HALT-EXPECTED-BOUNDARY row simultaneously"; AND V-01's Step 8b prose will contain `DECLARE CONTRADICTION: BC-[N] -- [label] -- arm: [which arm]` with all three named fields before Step 8c is populated; absence of either phrase falsifies the V-01 baseline claim |
| Secondary effect | Dual enforcement at Phase 0B (GATE-0B) and Step 8 Header (GATE-8H verbatim) transfers FROM single-checkpoint C-41 enforcement TO two-checkpoint consistency contract that requires identical HALT-EXPECTED-BOUNDARY reference text at both structural positions — risk that verbatim reproduction from Phase 0B to Step 8 Header drifts when HALT-EXPECTED-BOUNDARY is a named token within the HALT-RULE (more syntactically complex reproduction target than a simple keyword), with drift manifesting as paraphrase at Step 8 Header while Phase 0B is correct |
| Predicted manifestation site | if V-01 (Phase 0B phase-gate with GATE-0B + GATE-8H verbatim reproduction contract) achieves HALT-EXPECTED-BOUNDARY reference fidelity at Step 8 Header at higher rate than V-04 (role-entry contract without Phase 0B phase gate), then the dedicated phase-gate architecture adds enforcement value beyond role-entry framing; if fidelity is equivalent across V-01 and V-04, GATE-0B's phase-closure enforcement does not improve over V-04's entry-contract enforcement for the Step 8 Header reproduction step |

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

Predict the boundary most likely to produce a dual-surface halt at Step 8. Commit the prediction as machine-greppable tokens before any boundary evidence exists.

```
TRACE CONTRACT
HALT-EXPECTED-BOUNDARY: "BC-[N] -- [exact boundary label as it will appear in the Steps 4-7 table]"
HALT-EXPECTED-CONDITION: "Step 8b prose asserts coherence for BC-[N] AND Step 8c Match? = N for BC-[N] row"
```

[GATE-0A: Both tokens required before Step 0. BC-N must name a specific predicted boundary — "may fail at authentication" does not close. HALT-EXPECTED-CONDITION must encode both the Step 8b prose coherence state AND Step 8c Match? = N simultaneously — a single-surface condition does not close. Generic boundary labels do not close.]

---

**Phase 0B — CHECKER ALGORITHM Pre-Declaration**

Declare the checker algorithm. This is a binding contract: Step 8 Header must reproduce these exact lines verbatim.

```
CHECKER ALGORITHM:
  MATCH-RULE: Row passes iff Step8a-Invoked exactly matches any VT-N quoted value in Step 8 Header
  HALT-RULE: Row-Verdict = HALT iff Step 8b prose asserts coherence for HALT-EXPECTED-BOUNDARY AND Step 8c Match? = N for HALT-EXPECTED-BOUNDARY row simultaneously
  OUTPUT-RULE: CHECK RESULT = PASS iff all Row-Verdict = PASS; else FAIL -- N rows, M HALT rows
```

[GATE-0B: CHECKER ALGORITHM block required before Step 0. HALT-RULE must reference HALT-EXPECTED-BOUNDARY as a named structural token within the halt predicate — naming HALT-EXPECTED-BOUNDARY is the test: "Row-Verdict = HALT iff Match? = N" does not close; "iff Step 8b prose asserts coherence AND Step 8c Match? = N" without naming HALT-EXPECTED-BOUNDARY does not close. All three tokens (MATCH-RULE / HALT-RULE / OUTPUT-RULE) required. Missing any one token does not close.]

[GATE-0: Phase 0 does not close without Phase 0A (TRACE CONTRACT) and Phase 0B (CHECKER ALGORITHM) both complete. Platform Expert role does not begin until Phase 0 closes.]

---

### Platform Expert Trace (Steps 0–12)

**Step 0 — Entry Point**

Declare the exact request trigger: caller identity, entry endpoint (path + verb), receiving component, credential type.

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

Decode the bearer token. List every permission scope as a numbered quoted string. These become the VT-N tokens at Step 8. Exact quoted strings — no paraphrase.

```
Declared scopes:
1. "[exact scope string]"
2. "[exact scope string]"
...
```

[GATE-3: Exact quoted scope strings required per line. "Standard permissions" does not close. "Appropriate OAuth scopes" does not close. Each scope must be quoted and numbered.]

---

**Steps 4–7 — Boundary Traversal**

Every service boundary crossed. Gap? = Y means the invoked auth scope at this boundary may differ from the Step 3 declared scope. Every Gap?=Y boundary generates a Step 8 verification row.

| Step | Boundary (BC-N label) | Component | Gap? | Auth Required | Latency Source? | Batch Edge Case? |
|------|----------------------|-----------|------|---------------|-----------------|------------------|
| 4    | BC-1 --              |           | Y/N  |               | Y/N             | Y/N              |
| 5    | BC-2 --              |           | Y/N  |               | Y/N             | Y/N              |
| 6    | BC-3 --              |           | Y/N  |               | Y/N             | Y/N              |
| 7    | BC-4 --              |           | Y/N  |               | Y/N             | Y/N              |

[GATE-4-7: BC-N labels assigned at first appearance are forward-binding — Step 8 HALT-EXPECTED-BOUNDARY must match a BC-N label from this table exactly. Every boundary must have an explicit Gap? value. "N/A" does not close for Gap?.]

---

**Step 8 Header**

Reproduce Step 3 declared scopes as VT-N quoted schema. Reproduce Phase 0B CHECKER ALGORITHM verbatim — no paraphrase, no substitution.

```
VT-1: "[exact scope string from Step 3 line 1]"
VT-2: "[exact scope string from Step 3 line 2]"
...
TOKEN-COUNT: [N — must equal count of VT-N lines above]
CHECKER ALGORITHM:
  MATCH-RULE: [reproduce Phase 0B MATCH-RULE verbatim]
  HALT-RULE: [reproduce Phase 0B HALT-RULE verbatim]
  OUTPUT-RULE: [reproduce Phase 0B OUTPUT-RULE verbatim]
```

[GATE-8H: Verbatim reproduction required — paraphrase does not close. HALT-RULE must reference HALT-EXPECTED-BOUNDARY as a named token (inherited from Phase 0B). If Phase 0B was well-formed, verbatim reproduction preserves the reference. A HALT-RULE that drops HALT-EXPECTED-BOUNDARY during reproduction does not close. Missing any of MATCH-RULE / HALT-RULE / OUTPUT-RULE does not close. TOKEN-COUNT must immediately precede CHECKER ALGORITHM.]

---

**Step 8a — Invoked Scope**

For each Gap?=Y boundary from Steps 4–7, name the scope string actually invoked by the service call. Exact quoted strings.

| Boundary (BC-N) | Step8a-Invoked (exact quoted string) |
|-----------------|--------------------------------------|
|                 |                                      |

---

**Step 8b — Coherence Confirmation (REQUIRED per Gap?=Y boundary)**

For each Gap?=Y boundary, confirm all three link arms. If any arm declares CONTRADICTION, emit the DECLARE CONTRADICTION token immediately in the Step 8b prose block for that boundary, before the Step 8c table is populated for that row.

```
Boundary: BC-[N] -- [label]
  Step 3 Auth -> Step 8a Invoked: [coherent / CONTRADICTION -- describe mismatch]
  Step 8a Invoked -> Step 11 Params: [coherent / CONTRADICTION -- describe mismatch]
  Step 8a Invoked -> Step 7/9 Boundary: [coherent / CONTRADICTION -- describe mismatch]
```

If any arm is CONTRADICTION:
```
DECLARE CONTRADICTION: BC-[N] -- [label] -- arm: [Step3-Auth / Step8a-Invoked / Step11-Params — name the specific arm that is contradicted]
```

[GATE-8B: DECLARE CONTRADICTION token required in Step 8b prose at the contradiction boundary, emitted before Step 8c table is populated for that row. Three fields required: BC-N boundary ID, descriptive label, and arm: naming the specific contradicted arm. CONTRADICTION asserted in prose without DECLARE CONTRADICTION token is a structural defect. Two-field form (missing arm:) is a structural defect. All three link arms required per boundary. Step 9 DOES NOT BEGIN until this block is complete for every Gap?=Y boundary.]

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

**TRACE CONTRACT validation**

After Step 8c executes, return to the Phase 0A prediction and confirm or falsify:

```
TRACE CONTRACT validation: [HALT fired at HALT-EXPECTED-BOUNDARY (BC-[N]). Contract prediction confirmed. / HALT fired at BC-[M] -- not the predicted BC-[N]. Contract prediction: falsified -- actual halt boundary was [label]. / No Row-Verdict = HALT. HALT-EXPECTED-BOUNDARY (BC-[N]) did not fire. Contract prediction: falsified.]
```

[GATE-TC: TRACE CONTRACT validation token required immediately after CHECK RESULT. Must reference the HALT-EXPECTED-BOUNDARY boundary ID from Phase 0A by name. All three outcome paths are valid outputs — the validation is not structural confirmation only. Missing validation token does not close Phase 3.]

---

**Step 9 — Downstream Service Call**

Step 9 DOES NOT BEGIN until Step 8b complete for all Gap?=Y boundaries.

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

[GATE-12: FINDINGS does not close on "no issues found", "no concerns", or blank Failure Mode cells. If trace is clean: state "CLEAN TRACE -- confirmed: no auth gaps, no latency sources, no batch edge cases at any boundary" explicitly in the table. GATE-12 does not close unless every finding row carries an explicit Failure Mode value.]

---

**SetCoherenceAuditor Checkpoint — V-01**

| Check | Pass condition | Pass? |
|-------|----------------|-------|
| Complete standalone body | Full prompt text present — no diffs, no forward references | PASS |
| Axis label | Baseline — R18 full stack | PASS |
| Hypothesis label | Present with Primary effect, Secondary effect, Predicted manifestation site | PASS |
| Single-axis isolation | Baseline — no axis changed relative to V-01 (is V-01) | PASS |
| V-ID citation coverage | Planning table names V-04 and V-01 in mutual Predicted-manifestation-site cells | PASS |
| Axis breadth | V-01 = Baseline (will be 4+ distinct axes across all 5 rows at V-05 completion) | PASS (deferred to completion) |

---

## V-02

**Axis:** C-42 surface 1 (single) — 4-field DECLARE CONTRADICTION with `-- matches HALT-EXPECTED-BOUNDARY: [yes/no]` intertextual cross-reference field. Step 8b DECLARE CONTRADICTION gains a fourth named token field. GATE-8B updated to require all four fields. Falsification path explicitly surfaced: `matches HALT-EXPECTED-BOUNDARY: no` is a valid and required output variant when the contradiction fires at a non-predicted boundary.

**Hypothesis:**

| Field | Prediction |
|-------|------------|
| Primary effect | V-02's Step 8b prose will contain `DECLARE CONTRADICTION: BC-[N] -- [label] -- arm: [which arm] -- matches HALT-EXPECTED-BOUNDARY: [yes/no]` with all four named fields; the presence of the fourth field `matches HALT-EXPECTED-BOUNDARY:` with a filled `[yes/no]` value (not a literal placeholder) in Step 8b prose before Step 8c is populated is the positive falsification anchor; absence of the fourth field in Step 8b (three-field form only) falsifies the V-02 C-42 surface 1 claim |
| Secondary effect | Adding the 4th field transfers FROM three-field DECLARE CONTRADICTION (C-40 form) at Step 8b TO a four-field form that requires cross-referencing HALT-EXPECTED-BOUNDARY at the prose surface — risk: model emits the 4th field with a literal `[yes/no]` placeholder rather than substituting the actual match result ("yes" or "no"), satisfying structural presence of the token while leaving the cross-reference semantically empty; secondary risk: GATE-8B complexity increase (4-field requirement vs 3-field) may cause model to abbreviate Step 8b prose to satisfy the gate, dropping the per-arm confirmation narrative while producing only the DECLARE CONTRADICTION token line |
| Predicted manifestation site | if V-02 produces the 4-field DECLARE CONTRADICTION (with filled yes/no value) in Step 8b prose AND V-05 (combined) also produces it, then C-42 surface 1 is addable as single-axis (V-02 evidence) and stable under combination (V-05 evidence); if V-02 fails to produce the 4th field but V-05 succeeds, the cross-reference field requires the FAIL-CATEGORY token pressure of V-03 to activate, which would make C-42 surface 1 a combination-dependent surface not promotable independently |

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

---

**Phase 0B — CHECKER ALGORITHM Pre-Declaration**

Declare the checker algorithm. This declaration is a binding contract: Step 8 Header must reproduce these exact lines verbatim.

```
CHECKER ALGORITHM:
  MATCH-RULE: Row passes iff Step8a-Invoked exactly matches any VT-N quoted value in Step 8 Header
  HALT-RULE: Row-Verdict = HALT iff Step 8b prose asserts coherence for HALT-EXPECTED-BOUNDARY AND Step 8c Match? = N for HALT-EXPECTED-BOUNDARY row simultaneously
  OUTPUT-RULE: CHECK RESULT = PASS iff all Row-Verdict = PASS; else FAIL -- N rows, M HALT rows
```

[GATE-0B: HALT-RULE must reference HALT-EXPECTED-BOUNDARY as a named structural token within the halt predicate. All three tokens required. Missing any token does not close.]

[GATE-0: Phase 0 closes only when Phase 0A and Phase 0B are both complete. Platform Expert does not begin until Phase 0 closes.]

---

### Platform Expert Trace (Steps 0–12)

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

Decode the bearer token. List every permission scope as a numbered quoted string. These become the VT-N tokens at Step 8.

```
Declared scopes:
1. "[exact scope string]"
2. "[exact scope string]"
...
```

[GATE-3: Exact quoted scope strings required. Generic descriptions do not close.]

---

**Steps 4–7 — Boundary Traversal**

| Step | Boundary (BC-N label) | Component | Gap? | Auth Required | Latency Source? | Batch Edge Case? |
|------|----------------------|-----------|------|---------------|-----------------|------------------|
| 4    | BC-1 --              |           | Y/N  |               | Y/N             | Y/N              |
| 5    | BC-2 --              |           | Y/N  |               | Y/N             | Y/N              |
| 6    | BC-3 --              |           | Y/N  |               | Y/N             | Y/N              |
| 7    | BC-4 --              |           | Y/N  |               | Y/N             | Y/N              |

[GATE-4-7: BC-N labels assigned here are forward-binding. HALT-EXPECTED-BOUNDARY must match one of these labels exactly.]

---

**Step 8 Header**

Reproduce Step 3 declared scopes as VT-N quoted schema. Reproduce Phase 0B CHECKER ALGORITHM verbatim.

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

[GATE-8H: Verbatim reproduction required. HALT-RULE must preserve HALT-EXPECTED-BOUNDARY reference from Phase 0B. Paraphrase does not close.]

---

**Step 8a — Invoked Scope**

| Boundary (BC-N) | Step8a-Invoked (exact quoted string) |
|-----------------|--------------------------------------|
|                 |                                      |

---

**Step 8b — Coherence Confirmation (REQUIRED per Gap?=Y boundary)**

For each Gap?=Y boundary, confirm all three link arms. If any arm declares CONTRADICTION, emit the DECLARE CONTRADICTION token with all four required fields immediately in the Step 8b prose block for that boundary, before Step 8c is populated for that row.

```
Boundary: BC-[N] -- [label]
  Step 3 Auth -> Step 8a Invoked: [coherent / CONTRADICTION -- describe mismatch]
  Step 8a Invoked -> Step 11 Params: [coherent / CONTRADICTION -- describe mismatch]
  Step 8a Invoked -> Step 7/9 Boundary: [coherent / CONTRADICTION -- describe mismatch]
```

If any arm is CONTRADICTION:
```
DECLARE CONTRADICTION: BC-[N] -- [label] -- arm: [Step3-Auth / Step8a-Invoked / Step11-Params] -- matches HALT-EXPECTED-BOUNDARY: [yes / no]
```

`matches HALT-EXPECTED-BOUNDARY:` value is:
- `yes` — if this contradiction fires at the boundary named in the TRACE CONTRACT HALT-EXPECTED-BOUNDARY
- `no` — if this contradiction fires at a different boundary from the one predicted in the TRACE CONTRACT

[GATE-8B: DECLARE CONTRADICTION token required in Step 8b prose at the contradiction boundary, emitted before Step 8c is populated for that row. All four fields are required: BC-N boundary ID, descriptive label, arm: naming the specific contradicted arm, and matches HALT-EXPECTED-BOUNDARY: with a filled yes/no value. Three-field form (missing matches HALT-EXPECTED-BOUNDARY:) is a structural defect. Literal "[yes/no]" placeholder without substitution is a structural defect — the value must be either "yes" or "no". All three link arms required per boundary. Step 9 DOES NOT BEGIN until this block is complete for every Gap?=Y boundary.]

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

[GATE-8C: Row-Verdict column required per row. CHECK RESULT required immediately after table.]

---

**TRACE CONTRACT validation**

After Step 8c executes:

```
TRACE CONTRACT validation: [HALT fired at HALT-EXPECTED-BOUNDARY (BC-[N]). Contract prediction confirmed. / HALT fired at BC-[M] -- not the predicted BC-[N]. Contract prediction: falsified -- actual halt boundary was [label]. / No Row-Verdict = HALT. HALT-EXPECTED-BOUNDARY (BC-[N]) did not fire. Contract prediction: falsified.]
```

[GATE-TC: TRACE CONTRACT validation token required immediately after CHECK RESULT. Must reference the HALT-EXPECTED-BOUNDARY boundary ID from Phase 0A by name. All three outcome paths (confirmed / falsified-wrong-boundary / falsified-no-halt) are valid outputs.]

---

**Step 9 — Downstream Service Call**

Step 9 DOES NOT BEGIN until Step 8b complete for all Gap?=Y boundaries.

Declare: target service, request params, connection method.

---

**Step 10 — Storage Access**

| Order | Entity/Table | Operation | Connector/SDK | Failure Mode |
|-------|-------------|-----------|---------------|--------------|
| 1     |             |           |               |              |

---

**Step 11 — Response Assembly**

Declare response shape: fields returned, transformations applied, error response shape. Params feed Step 8c Step11-Params column.

---

**Step 12 — Findings**

| # | Finding | Boundary (BC-N) | Failure Mode | Latency Source? | Severity | Fix |
|---|---------|----------------|--------------|-----------------|----------|-----|
| F-01 |         |                |              | Y/N             |          |     |

[GATE-12: FINDINGS does not close on "no issues found" without explicit clean trace declaration: "CLEAN TRACE -- confirmed: no auth gaps, no latency sources, no batch edge cases at any boundary".]

---

**SetCoherenceAuditor Checkpoint — V-02**

| Check | Pass condition | Pass? |
|-------|----------------|-------|
| Complete standalone body | Full prompt text present — no diffs, no forward references | PASS |
| Axis label | C-42 surface 1 (single) — 4-field DECLARE CONTRADICTION | PASS |
| Hypothesis label | Present with Primary effect, Secondary effect, Predicted manifestation site | PASS |
| Single-axis isolation | Exactly one axis changed vs V-01: DECLARE CONTRADICTION gains 4th field `-- matches HALT-EXPECTED-BOUNDARY: [yes/no]` and GATE-8B updated; all other structural elements (Phase 0A/0B, Step 8 Header, TRACE CONTRACT validation, Steps 0-12) identical to V-01 | PASS |
| V-ID citation coverage | V-02 planning table row names V-05 in Predicted-manifestation-site cell | PASS |
| Axis breadth | V-01 = Baseline; V-02 = C-42 surface 1 (2 distinct axes so far) | PASS |

---

## V-03

**Axis:** C-42 surface 2 (single) — FAIL-CATEGORY taxonomy in Step 12 Findings. Every finding row must carry a machine-greppable `FAIL-CATEGORY:` token drawn from the closed vocabulary: AUTH | BOUNDARY | CONTRACT | TIMEOUT | STATE | PERMISSION. GATE-12 updated to require FAIL-CATEGORY on every finding row. All other structural elements identical to V-01.

**Hypothesis:**

| Field | Prediction |
|-------|------------|
| Primary effect | V-03's Step 12 Findings table will contain `FAIL-CATEGORY: [AUTH / BOUNDARY / CONTRACT / TIMEOUT / STATE / PERMISSION]` on every finding row, with the value drawn exclusively from the named closed vocabulary; the presence of FAIL-CATEGORY token lines on every finding row with values from the specified six-item vocabulary (not outside it) is the positive falsification anchor; absence of FAIL-CATEGORY on any finding row, or presence of a value outside the vocabulary, falsifies the V-03 C-42 surface 2 claim |
| Secondary effect | Requiring FAIL-CATEGORY on every finding row transfers FROM unclassified Failure Mode prose (free-form description only) TO a dual-field pattern per finding: machine-greppable FAIL-CATEGORY token + Failure Mode prose description — risk: model treats FAIL-CATEGORY as a semantic category label and produces values outside the closed vocabulary ("SCHEMA" for a contract mismatch, "SECURITY" for an auth gap) rather than drawing from the six named tokens; if out-of-vocabulary values appear consistently, the vocabulary cannot be frozen as specified and C-42 surface 2 remains in Tier D |
| Predicted manifestation site | if V-03 produces FAIL-CATEGORY on every finding row with only in-vocabulary values AND V-05 (combined) also produces FAIL-CATEGORY with in-vocabulary values under the added C-42 surface 1 constraint, then C-42 surface 2 is independently stable and addable without surface interaction; if V-05 produces out-of-vocabulary FAIL-CATEGORY values while V-03 produces in-vocabulary values, the C-42 surface 1 token pressure degrades FAIL-CATEGORY vocabulary precision under combination |

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

Predict the boundary most likely to produce a dual-surface halt at Step 8.

```
TRACE CONTRACT
HALT-EXPECTED-BOUNDARY: "BC-[N] -- [exact boundary label as it will appear in the Steps 4-7 table]"
HALT-EXPECTED-CONDITION: "Step 8b prose asserts coherence for BC-[N] AND Step 8c Match? = N for BC-[N] row"
```

[GATE-0A: Both tokens required before Step 0. BC-N must name a specific predicted boundary. HALT-EXPECTED-CONDITION must encode both Step 8b prose state AND Step 8c Match? = N simultaneously.]

---

**Phase 0B — CHECKER ALGORITHM Pre-Declaration**

```
CHECKER ALGORITHM:
  MATCH-RULE: Row passes iff Step8a-Invoked exactly matches any VT-N quoted value in Step 8 Header
  HALT-RULE: Row-Verdict = HALT iff Step 8b prose asserts coherence for HALT-EXPECTED-BOUNDARY AND Step 8c Match? = N for HALT-EXPECTED-BOUNDARY row simultaneously
  OUTPUT-RULE: CHECK RESULT = PASS iff all Row-Verdict = PASS; else FAIL -- N rows, M HALT rows
```

[GATE-0B: HALT-RULE must reference HALT-EXPECTED-BOUNDARY as a named token within the halt predicate. All three tokens required.]

[GATE-0: Phase 0 closes only when Phase 0A and Phase 0B are both complete.]

---

### Platform Expert Trace (Steps 0–12)

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

**Steps 4–7 — Boundary Traversal**

| Step | Boundary (BC-N label) | Component | Gap? | Auth Required | Latency Source? | Batch Edge Case? |
|------|----------------------|-----------|------|---------------|-----------------|------------------|
| 4    | BC-1 --              |           | Y/N  |               | Y/N             | Y/N              |
| 5    | BC-2 --              |           | Y/N  |               | Y/N             | Y/N              |
| 6    | BC-3 --              |           | Y/N  |               | Y/N             | Y/N              |
| 7    | BC-4 --              |           | Y/N  |               | Y/N             | Y/N              |

[GATE-4-7: BC-N labels forward-binding. Every boundary must have an explicit Gap? value.]

---

**Step 8 Header**

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

[GATE-8H: Verbatim reproduction required. HALT-RULE must preserve HALT-EXPECTED-BOUNDARY reference from Phase 0B.]

---

**Step 8a — Invoked Scope**

| Boundary (BC-N) | Step8a-Invoked (exact quoted string) |
|-----------------|--------------------------------------|
|                 |                                      |

---

**Step 8b — Coherence Confirmation (REQUIRED per Gap?=Y boundary)**

For each Gap?=Y boundary, confirm all three link arms. If any arm declares CONTRADICTION, emit the DECLARE CONTRADICTION token immediately in Step 8b prose before Step 8c is populated for that row.

```
Boundary: BC-[N] -- [label]
  Step 3 Auth -> Step 8a Invoked: [coherent / CONTRADICTION -- describe mismatch]
  Step 8a Invoked -> Step 11 Params: [coherent / CONTRADICTION -- describe mismatch]
  Step 8a Invoked -> Step 7/9 Boundary: [coherent / CONTRADICTION -- describe mismatch]
```

If any arm is CONTRADICTION:
```
DECLARE CONTRADICTION: BC-[N] -- [label] -- arm: [Step3-Auth / Step8a-Invoked / Step11-Params]
```

[GATE-8B: DECLARE CONTRADICTION token required in Step 8b prose at the contradiction boundary before Step 8c is populated. Three fields required: BC-N, label, arm: naming the contradicted arm. All three link arms required per boundary. Step 9 DOES NOT BEGIN until complete for all Gap?=Y boundaries.]

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

[GATE-8C: Row-Verdict column required per row. CHECK RESULT required immediately after table.]

---

**TRACE CONTRACT validation**

```
TRACE CONTRACT validation: [HALT fired at HALT-EXPECTED-BOUNDARY (BC-[N]). Contract prediction confirmed. / HALT fired at BC-[M] -- not the predicted BC-[N]. Contract prediction: falsified. / No Row-Verdict = HALT. HALT-EXPECTED-BOUNDARY (BC-[N]) did not fire. Contract prediction: falsified.]
```

[GATE-TC: Required immediately after CHECK RESULT. Must reference HALT-EXPECTED-BOUNDARY boundary ID by name.]

---

**Step 9 — Downstream Service Call**

Step 9 DOES NOT BEGIN until Step 8b complete for all Gap?=Y boundaries.

Declare: target service, request params, connection method.

---

**Step 10 — Storage Access**

| Order | Entity/Table | Operation | Connector/SDK | Failure Mode |
|-------|-------------|-----------|---------------|--------------|
| 1     |             |           |               |              |

---

**Step 11 — Response Assembly**

Declare response shape: fields returned, transformations applied, error response shape. Params feed Step 8c Step11-Params column.

---

**Step 12 — Findings**

Every finding row must carry a `FAIL-CATEGORY:` token. Assign each finding to exactly one category from the closed vocabulary: AUTH | BOUNDARY | CONTRACT | TIMEOUT | STATE | PERMISSION.

```
Category definitions:
  AUTH     -- authentication or authorization gap (missing scope, privilege escalation, token validation)
  BOUNDARY -- failure mode at a specific service boundary crossing (HTTP error, connection refused, timeout at boundary)
  CONTRACT -- schema mismatch, type coercion, or API contract violation between producer and consumer
  TIMEOUT  -- latency source causing request duration to exceed platform thresholds
  STATE    -- state machine violation, concurrency hazard, or invalid state transition
  PERMISSION -- field-level or record-level permission enforcement gap (FLS, RLS, row-level access)
```

| # | Finding | Boundary (BC-N) | FAIL-CATEGORY | Failure Mode | Latency Source? | Severity | Fix |
|---|---------|----------------|---------------|--------------|-----------------|----------|-----|
| F-01 |         |                | [AUTH / BOUNDARY / CONTRACT / TIMEOUT / STATE / PERMISSION] |              | Y/N             |          |     |

[GATE-12: FAIL-CATEGORY required on every finding row. Values must be drawn from the closed vocabulary: AUTH, BOUNDARY, CONTRACT, TIMEOUT, STATE, PERMISSION. Values outside this vocabulary (e.g., "SECURITY", "PERFORMANCE", "SCHEMA") are structural defects that do not close. FINDINGS does not close on "no issues found" without explicit clean trace declaration: "CLEAN TRACE -- confirmed: no auth gaps, no latency sources, no batch edge cases at any boundary". Clean trace still carries FAIL-CATEGORY: N/A on the clean trace row.]

---

**SetCoherenceAuditor Checkpoint — V-03**

| Check | Pass condition | Pass? |
|-------|----------------|-------|
| Complete standalone body | Full prompt text present — no diffs, no forward references | PASS |
| Axis label | C-42 surface 2 (single) — FAIL-CATEGORY taxonomy in Step 12 Findings | PASS |
| Hypothesis label | Present with Primary effect, Secondary effect, Predicted manifestation site | PASS |
| Single-axis isolation | Exactly one axis changed vs V-01: Step 12 Findings gains FAIL-CATEGORY column + GATE-12 updated; all other structural elements (Phase 0A/0B, Step 8b DECLARE CONTRADICTION three-field form, TRACE CONTRACT validation, Steps 0-11) identical to V-01 | PASS |
| V-ID citation coverage | V-03 planning table row names V-05 in Predicted-manifestation-site cell | PASS |
| Axis breadth | V-01 = Baseline; V-02 = C-42 surface 1; V-03 = C-42 surface 2 (3 distinct axes) | PASS |

---

## V-04

**Axis:** Role sequence (single) — C-41 enforcement relocated from Algorithm-Declarant Phase 0B phase gate to Platform Expert role-entry contract. No separate Algorithm-Declarant role. The Platform Expert declares TRACE CONTRACT and CHECKER ALGORITHM as role-entry obligations before accepting the trace task. The role-entry contract IS the Phase 0 artifact — the Platform Expert cannot begin Step 0 without producing a role-entry contract block that includes CHECKER ALGORITHM with HALT-EXPECTED-BOUNDARY in the HALT-RULE.

**Hypothesis:**

| Field | Prediction |
|-------|------------|
| Primary effect | V-04's output will contain a Platform Expert role-entry contract block (positioned after ROLE DECLARATION and before Step 0) that includes CHECKER ALGORITHM with HALT-RULE text containing "HALT-EXPECTED-BOUNDARY" as a named token within the halt predicate; the presence of this role-entry contract block with HALT-EXPECTED-BOUNDARY in the HALT-RULE is the positive falsification anchor; absence of the role-entry contract block, or presence of a HALT-RULE that does not name HALT-EXPECTED-BOUNDARY, falsifies the V-04 C-41 role-entry enforcement claim |
| Secondary effect | Relocating C-41 enforcement FROM Algorithm-Declarant Phase 0B dedicated-role phase gate TO Platform Expert role-entry contract (single-role architecture) transfers FROM a two-role handoff structure with external phase-gate enforcement TO a single-role entry contract where the Platform Expert self-declares the algorithm as entry condition — risk: without a separate Algorithm-Declarant imposing an external gate, the Platform Expert may produce the role-entry contract with a CHECKER ALGORITHM that drops HALT-EXPECTED-BOUNDARY from the HALT-RULE (producing a C-38-compliant HALT-RULE that names the dual-surface predicate but not the specific predicted boundary), satisfying structural entry-contract presence while failing C-41 token specificity |
| Predicted manifestation site | if V-01 (Algorithm-Declarant Phase 0B with GATE-0B enforcing HALT-EXPECTED-BOUNDARY reference) produces HALT-EXPECTED-BOUNDARY in the HALT-RULE at Step 8 Header with higher fidelity than V-04 (Platform Expert role-entry contract with GATE-ENTRY enforcing HALT-EXPECTED-BOUNDARY reference), then the dedicated Algorithm-Declarant role adds enforcement value beyond single-role entry-contract framing for preserving the HALT-EXPECTED-BOUNDARY reference through verbatim reproduction at Step 8 Header |

---

You are a platform expert auto-selected from context: Dataverse platform expert, Commerce platform expert, or Automate platform expert. Before accepting the trace task, complete your role-entry contract. The role-entry contract produces the binding pre-trace artifacts. You may not begin Step 0 until your role-entry contract is complete.

---

**ROLE DECLARATION**

| Field | Value |
|-------|-------|
| Platform Expert role | `[Dataverse platform expert / Commerce platform expert / Automate platform expert — select one]` |
| Request context | `[one sentence: what request and system are being traced]` |

---

### Role Entry Contract (complete before Step 0)

**Entry artifact 1 — TRACE CONTRACT**

Before you have seen any boundary evidence, predict the boundary most likely to produce a dual-surface halt at Step 8.

```
TRACE CONTRACT
HALT-EXPECTED-BOUNDARY: "BC-[N] -- [exact boundary label as it will appear in the Steps 4-7 table]"
HALT-EXPECTED-CONDITION: "Step 8b prose asserts coherence for BC-[N] AND Step 8c Match? = N for BC-[N] row"
```

[GATE-ENTRY-A: TRACE CONTRACT required as role-entry artifact 1. BC-N must name a specific predicted boundary. HALT-EXPECTED-CONDITION must encode Step 8b prose state AND Step 8c Match? = N simultaneously. A prose prediction without machine-greppable tokens does not satisfy entry artifact 1. Role Entry Contract does not close without this artifact.]

---

**Entry artifact 2 — CHECKER ALGORITHM**

Declare the algorithm you will use to execute Step 8. This is a binding declaration: your Step 8 Header must reproduce these lines verbatim.

```
CHECKER ALGORITHM:
  MATCH-RULE: Row passes iff Step8a-Invoked exactly matches any VT-N quoted value in Step 8 Header
  HALT-RULE: Row-Verdict = HALT iff Step 8b prose asserts coherence for HALT-EXPECTED-BOUNDARY AND Step 8c Match? = N for HALT-EXPECTED-BOUNDARY row simultaneously
  OUTPUT-RULE: CHECK RESULT = PASS iff all Row-Verdict = PASS; else FAIL -- N rows, M HALT rows
```

[GATE-ENTRY-B: CHECKER ALGORITHM required as role-entry artifact 2. HALT-RULE must name HALT-EXPECTED-BOUNDARY as a structural token within the halt predicate — "Row-Verdict = HALT iff Match? = N" does not close; "iff Step 8b prose asserts coherence AND Match? = N" without naming HALT-EXPECTED-BOUNDARY does not close. All three tokens (MATCH-RULE / HALT-RULE / OUTPUT-RULE) required. Role Entry Contract does not close without this artifact.]

[GATE-ENTRY: Role Entry Contract closes only when both entry artifacts are complete. Step 0 does not begin until Role Entry Contract closes.]

---

### Trace (Steps 0–12)

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

Decode the bearer token. List every permission scope as a numbered quoted string.

```
Declared scopes:
1. "[exact scope string]"
2. "[exact scope string]"
...
```

[GATE-3: Exact quoted scope strings required. Generic descriptions do not close.]

---

**Steps 4–7 — Boundary Traversal**

| Step | Boundary (BC-N label) | Component | Gap? | Auth Required | Latency Source? | Batch Edge Case? |
|------|----------------------|-----------|------|---------------|-----------------|------------------|
| 4    | BC-1 --              |           | Y/N  |               | Y/N             | Y/N              |
| 5    | BC-2 --              |           | Y/N  |               | Y/N             | Y/N              |
| 6    | BC-3 --              |           | Y/N  |               | Y/N             | Y/N              |
| 7    | BC-4 --              |           | Y/N  |               | Y/N             | Y/N              |

[GATE-4-7: BC-N labels assigned here are forward-binding. HALT-EXPECTED-BOUNDARY must match one of these labels exactly.]

---

**Step 8 Header**

Reproduce Step 3 declared scopes as VT-N quoted schema. Reproduce your Role Entry Contract CHECKER ALGORITHM verbatim.

```
VT-1: "[exact scope string from Step 3 line 1]"
VT-2: "[exact scope string from Step 3 line 2]"
...
TOKEN-COUNT: [N]
CHECKER ALGORITHM:
  MATCH-RULE: [reproduce Role Entry Contract MATCH-RULE verbatim]
  HALT-RULE: [reproduce Role Entry Contract HALT-RULE verbatim]
  OUTPUT-RULE: [reproduce Role Entry Contract OUTPUT-RULE verbatim]
```

[GATE-8H: Verbatim reproduction required. HALT-RULE must preserve HALT-EXPECTED-BOUNDARY reference from Role Entry Contract entry artifact 2. Paraphrase does not close.]

---

**Step 8a — Invoked Scope**

| Boundary (BC-N) | Step8a-Invoked (exact quoted string) |
|-----------------|--------------------------------------|
|                 |                                      |

---

**Step 8b — Coherence Confirmation (REQUIRED per Gap?=Y boundary)**

For each Gap?=Y boundary, confirm all three link arms. If any arm declares CONTRADICTION, emit the DECLARE CONTRADICTION token immediately in Step 8b prose before Step 8c is populated for that row.

```
Boundary: BC-[N] -- [label]
  Step 3 Auth -> Step 8a Invoked: [coherent / CONTRADICTION -- describe mismatch]
  Step 8a Invoked -> Step 11 Params: [coherent / CONTRADICTION -- describe mismatch]
  Step 8a Invoked -> Step 7/9 Boundary: [coherent / CONTRADICTION -- describe mismatch]
```

If any arm is CONTRADICTION:
```
DECLARE CONTRADICTION: BC-[N] -- [label] -- arm: [Step3-Auth / Step8a-Invoked / Step11-Params]
```

[GATE-8B: DECLARE CONTRADICTION token required in Step 8b prose at the contradiction boundary before Step 8c is populated. Three fields required: BC-N, label, arm:. All three link arms required per boundary. Step 9 DOES NOT BEGIN until complete for all Gap?=Y boundaries.]

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

[GATE-8C: Row-Verdict column required per row. CHECK RESULT required immediately after table.]

---

**TRACE CONTRACT validation**

```
TRACE CONTRACT validation: [HALT fired at HALT-EXPECTED-BOUNDARY (BC-[N]). Contract prediction confirmed. / HALT fired at BC-[M] -- not the predicted BC-[N]. Contract prediction: falsified. / No Row-Verdict = HALT. HALT-EXPECTED-BOUNDARY (BC-[N]) did not fire. Contract prediction: falsified.]
```

[GATE-TC-POST: Required immediately after CHECK RESULT. Must reference HALT-EXPECTED-BOUNDARY boundary ID from Role Entry Contract by name.]

---

**Step 9 — Downstream Service Call**

Step 9 DOES NOT BEGIN until Step 8b complete for all Gap?=Y boundaries.

Declare: target service, request params, connection method.

---

**Step 10 — Storage Access**

| Order | Entity/Table | Operation | Connector/SDK | Failure Mode |
|-------|-------------|-----------|---------------|--------------|
| 1     |             |           |               |              |

---

**Step 11 — Response Assembly**

Declare response shape: fields returned, transformations applied, error response shape. Params feed Step 8c Step11-Params column.

---

**Step 12 — Findings**

| # | Finding | Boundary (BC-N) | Failure Mode | Latency Source? | Severity | Fix |
|---|---------|----------------|--------------|-----------------|----------|-----|
| F-01 |         |                |              | Y/N             |          |     |

[GATE-12: FINDINGS does not close on "no issues found" without explicit clean trace declaration: "CLEAN TRACE -- confirmed: no auth gaps, no latency sources, no batch edge cases at any boundary".]

---

**SetCoherenceAuditor Checkpoint — V-04**

| Check | Pass condition | Pass? |
|-------|----------------|-------|
| Complete standalone body | Full prompt text present — no diffs, no forward references | PASS |
| Axis label | Role sequence (single) — C-41 enforcement as Platform Expert role-entry contract | PASS |
| Hypothesis label | Present with Primary effect, Secondary effect, Predicted manifestation site | PASS |
| Single-axis isolation | Exactly one axis changed vs V-01: Algorithm-Declarant two-role structure replaced with single Platform Expert role + role-entry contract (GATE-ENTRY-A + GATE-ENTRY-B + GATE-ENTRY instead of GATE-0A + GATE-0B + GATE-0); Step 8 Header verbatim reproduction instruction references "Role Entry Contract" rather than "Phase 0B"; all other structural elements (DECLARE CONTRADICTION three-field form, TRACE CONTRACT validation, Steps 0-12) identical to V-01 | PASS |
| V-ID citation coverage | V-04 planning table row names V-01 in Predicted-manifestation-site cell | PASS |
| Axis breadth | V-01 = Baseline; V-02 = C-42 surface 1; V-03 = C-42 surface 2; V-04 = Role sequence (4 distinct axes) | PASS |

---

## V-05

**Axis:** Combined — C-42 surface 1 + C-42 surface 2: 4-field DECLARE CONTRADICTION with `-- matches HALT-EXPECTED-BOUNDARY: [yes/no]` (V-02 axis) AND FAIL-CATEGORY taxonomy in Step 12 Findings (V-03 axis). Superadditivity test: both GATE-8B and GATE-12 updated simultaneously. All Phase 0A/0B structure from V-01 retained.

**Hypothesis:**

| Field | Prediction |
|-------|------------|
| Primary effect | V-05's output will contain both (a) `DECLARE CONTRADICTION: BC-[N] -- [label] -- arm: [which arm] -- matches HALT-EXPECTED-BOUNDARY: [yes/no]` in Step 8b prose with all four fields and (b) `FAIL-CATEGORY: [vocabulary token]` on every Step 12 finding row with values from the closed vocabulary; the simultaneous presence of both named token surfaces in the same trace output is the positive falsification anchor; absence of either surface (four-field DECLARE CONTRADICTION OR FAIL-CATEGORY on finding rows) falsifies the V-05 combined claim |
| Secondary effect | Combining both C-42 axes transfers FROM single-axis token elicitation (V-02: one new field at one structural position; V-03: one new column at one structural position) TO dual-axis concurrent enforcement where two independent structural modifications are required in the same trace execution — risk: token pressure under dual enforcement causes one surface to degrade while the other is maintained; if Step 8b DECLARE CONTRADICTION degrades (loses 4th field under token pressure while maintaining FAIL-CATEGORY), V-02 surface is the weaker under combination; if FAIL-CATEGORY degrades (out-of-vocabulary values or absent rows under DECLARE CONTRADICTION 4th-field pressure), V-03 surface is the weaker under combination |
| Predicted manifestation site | if V-05 produces both surfaces at equal fidelity to V-02 and V-03 individually (4-field DECLARE CONTRADICTION with filled yes/no AND FAIL-CATEGORY with in-vocabulary values), C-42 surface 1 and surface 2 are independent under combination and both are independently promotable; if V-05 produces one surface degraded relative to its single-axis baseline variation, the degrading surface requires isolation from the other C-42 axis to achieve stable elicitation, and the weaker surface needs a more explicit enforcement mechanism before promotion |

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

Predict the boundary most likely to produce a dual-surface halt at Step 8.

```
TRACE CONTRACT
HALT-EXPECTED-BOUNDARY: "BC-[N] -- [exact boundary label as it will appear in the Steps 4-7 table]"
HALT-EXPECTED-CONDITION: "Step 8b prose asserts coherence for BC-[N] AND Step 8c Match? = N for BC-[N] row"
```

[GATE-0A: Both tokens required before Step 0. BC-N must name a specific predicted boundary. HALT-EXPECTED-CONDITION must encode Step 8b prose state AND Step 8c Match? = N simultaneously.]

---

**Phase 0B — CHECKER ALGORITHM Pre-Declaration**

```
CHECKER ALGORITHM:
  MATCH-RULE: Row passes iff Step8a-Invoked exactly matches any VT-N quoted value in Step 8 Header
  HALT-RULE: Row-Verdict = HALT iff Step 8b prose asserts coherence for HALT-EXPECTED-BOUNDARY AND Step 8c Match? = N for HALT-EXPECTED-BOUNDARY row simultaneously
  OUTPUT-RULE: CHECK RESULT = PASS iff all Row-Verdict = PASS; else FAIL -- N rows, M HALT rows
```

[GATE-0B: HALT-RULE must reference HALT-EXPECTED-BOUNDARY as a named token within the halt predicate. All three tokens required.]

[GATE-0: Phase 0 closes only when Phase 0A and Phase 0B are both complete.]

---

### Platform Expert Trace (Steps 0–12)

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

**Steps 4–7 — Boundary Traversal**

| Step | Boundary (BC-N label) | Component | Gap? | Auth Required | Latency Source? | Batch Edge Case? |
|------|----------------------|-----------|------|---------------|-----------------|------------------|
| 4    | BC-1 --              |           | Y/N  |               | Y/N             | Y/N              |
| 5    | BC-2 --              |           | Y/N  |               | Y/N             | Y/N              |
| 6    | BC-3 --              |           | Y/N  |               | Y/N             | Y/N              |
| 7    | BC-4 --              |           | Y/N  |               | Y/N             | Y/N              |

[GATE-4-7: BC-N labels forward-binding. Every boundary must have an explicit Gap? value.]

---

**Step 8 Header**

Reproduce Step 3 declared scopes as VT-N quoted schema. Reproduce Phase 0B CHECKER ALGORITHM verbatim.

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

[GATE-8H: Verbatim reproduction required. HALT-RULE must preserve HALT-EXPECTED-BOUNDARY reference from Phase 0B.]

---

**Step 8a — Invoked Scope**

| Boundary (BC-N) | Step8a-Invoked (exact quoted string) |
|-----------------|--------------------------------------|
|                 |                                      |

---

**Step 8b — Coherence Confirmation (REQUIRED per Gap?=Y boundary)**

For each Gap?=Y boundary, confirm all three link arms. If any arm declares CONTRADICTION, emit the DECLARE CONTRADICTION token with all four required fields immediately in the Step 8b prose block for that boundary, before Step 8c is populated for that row.

```
Boundary: BC-[N] -- [label]
  Step 3 Auth -> Step 8a Invoked: [coherent / CONTRADICTION -- describe mismatch]
  Step 8a Invoked -> Step 11 Params: [coherent / CONTRADICTION -- describe mismatch]
  Step 8a Invoked -> Step 7/9 Boundary: [coherent / CONTRADICTION -- describe mismatch]
```

If any arm is CONTRADICTION:
```
DECLARE CONTRADICTION: BC-[N] -- [label] -- arm: [Step3-Auth / Step8a-Invoked / Step11-Params] -- matches HALT-EXPECTED-BOUNDARY: [yes / no]
```

`matches HALT-EXPECTED-BOUNDARY:` value is:
- `yes` — if this contradiction fires at the boundary named in the TRACE CONTRACT HALT-EXPECTED-BOUNDARY
- `no` — if this contradiction fires at a different boundary from the one predicted in the TRACE CONTRACT

[GATE-8B: DECLARE CONTRADICTION token required in Step 8b prose at the contradiction boundary before Step 8c is populated. All four fields are required: BC-N boundary ID, descriptive label, arm: naming the contradicted arm, and matches HALT-EXPECTED-BOUNDARY: with a filled yes/no value (not a placeholder). Three-field form is a structural defect. All three link arms required per boundary. Step 9 DOES NOT BEGIN until complete for all Gap?=Y boundaries.]

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

[GATE-8C: Row-Verdict column required per row. CHECK RESULT required immediately after table.]

---

**TRACE CONTRACT validation**

```
TRACE CONTRACT validation: [HALT fired at HALT-EXPECTED-BOUNDARY (BC-[N]). Contract prediction confirmed. / HALT fired at BC-[M] -- not the predicted BC-[N]. Contract prediction: falsified. / No Row-Verdict = HALT. HALT-EXPECTED-BOUNDARY (BC-[N]) did not fire. Contract prediction: falsified.]
```

[GATE-TC: Required immediately after CHECK RESULT. Must reference HALT-EXPECTED-BOUNDARY boundary ID from Phase 0A by name.]

---

**Step 9 — Downstream Service Call**

Step 9 DOES NOT BEGIN until Step 8b complete for all Gap?=Y boundaries.

Declare: target service, request params, connection method.

---

**Step 10 — Storage Access**

| Order | Entity/Table | Operation | Connector/SDK | Failure Mode |
|-------|-------------|-----------|---------------|--------------|
| 1     |             |           |               |              |

---

**Step 11 — Response Assembly**

Declare response shape: fields returned, transformations applied, error response shape. Params feed Step 8c Step11-Params column.

---

**Step 12 — Findings**

Every finding row must carry a `FAIL-CATEGORY:` token from the closed vocabulary: AUTH | BOUNDARY | CONTRACT | TIMEOUT | STATE | PERMISSION.

```
Category definitions:
  AUTH       -- authentication or authorization gap
  BOUNDARY   -- failure mode at a service boundary crossing
  CONTRACT   -- schema mismatch, type coercion, or API contract violation
  TIMEOUT    -- latency source exceeding platform threshold
  STATE      -- state machine violation or concurrency hazard
  PERMISSION -- field-level or record-level permission enforcement gap
```

| # | Finding | Boundary (BC-N) | FAIL-CATEGORY | Failure Mode | Latency Source? | Severity | Fix |
|---|---------|----------------|---------------|--------------|-----------------|----------|-----|
| F-01 |         |                | [AUTH / BOUNDARY / CONTRACT / TIMEOUT / STATE / PERMISSION] |              | Y/N             |          |     |

[GATE-12: FAIL-CATEGORY required on every finding row. Values must be from the closed vocabulary — out-of-vocabulary values are structural defects. FINDINGS does not close on "no issues found" without explicit clean trace declaration. Clean trace row carries FAIL-CATEGORY: N/A.]

---

**SetCoherenceAuditor Checkpoint — V-05**

| Check | Pass condition | Pass? |
|-------|----------------|-------|
| Complete standalone body | Full prompt text present — no diffs, no forward references | PASS |
| Axis label | Combined — C-42 surface 1 + C-42 surface 2 | PASS |
| Hypothesis label | Present with Primary effect, Secondary effect, Predicted manifestation site | PASS |
| Single-axis isolation | Explicitly labeled as combination pass — two axes combined: (1) DECLARE CONTRADICTION 4th field from V-02, (2) FAIL-CATEGORY from V-03; all other structural elements identical to V-01 | PASS |
| V-ID citation coverage | V-05 planning table row names V-02 and V-03 in Predicted-manifestation-site cell | PASS |
| Axis breadth | V-01 = Baseline; V-02 = C-42 surface 1; V-03 = C-42 surface 2; V-04 = Role sequence; V-05 = Combined (5 rows, 4 distinct single-axis variations + 1 combination) | PASS |

---

## Phase 2 STOP CONDITION — verified before Phase 3

All 5 variations have passed their per-variation checkpoints. No noted-but-unresolved failures.

**Variation Completion Manifest**

| V-ID | Checkpoint status | All variation-level and set-level checks passed? |
|------|------------------|--------------------------------------------------|
| V-01 | Complete | Yes — Baseline R18 full stack; all structural slots present; HALT-EXPECTED-BOUNDARY in Phase 0B HALT-RULE; DECLARE CONTRADICTION three-field form in GATE-8B |
| V-02 | Complete | Yes — Single-axis C-42 surface 1; 4-field DECLARE CONTRADICTION with matches HALT-EXPECTED-BOUNDARY; GATE-8B updated to require 4th field; falsification path (matches HALT-EXPECTED-BOUNDARY: no) surfaced |
| V-03 | Complete | Yes — Single-axis C-42 surface 2; FAIL-CATEGORY closed vocabulary in Step 12; GATE-12 updated; category definitions block present |
| V-04 | Complete | Yes — Single-axis role sequence; Algorithm-Declarant replaced by Platform Expert role-entry contract (GATE-ENTRY-A + GATE-ENTRY-B + GATE-ENTRY); HALT-EXPECTED-BOUNDARY in role-entry HALT-RULE; all other elements identical to V-01 |
| V-05 | Complete | Yes — Combination V-02+V-03 axes; both 4-field DECLARE CONTRADICTION and FAIL-CATEGORY present simultaneously; explicitly labeled as combination pass |

**Manifest STOP CONDITION: All 5 rows filled and confirmed. Phase 3 may begin.**

---

## Phase 3 — Complete Variation Set

*Variations V-01 through V-05 are emitted above in Phase 2 with full bodies. Each variation is a complete standalone runnable skill body. Phase 3 references the bodies as emitted — no scoring, critique, or comparison in this phase.*

---

## R18 Excellence Signal Candidates

**C-42 surface 1 — `matches HALT-EXPECTED-BOUNDARY:` fourth field in DECLARE CONTRADICTION**

The V-02 single-axis design produces `DECLARE CONTRADICTION: BC-[N] -- [label] -- arm: [which arm] -- matches HALT-EXPECTED-BOUNDARY: [yes/no]` with all four fields as a required output when GATE-8B explicitly names the fourth field and specifies the yes/no substitution rule. Key test: does the `matches HALT-EXPECTED-BOUNDARY:` field appear with a filled boolean value rather than a placeholder when (a) TRACE CONTRACT pre-declares HALT-EXPECTED-BOUNDARY (C-39) and (b) the HALT-RULE additionally names HALT-EXPECTED-BOUNDARY within the algorithm (C-41)? The intertextual reference is structurally supported by three co-present surfaces: TRACE CONTRACT (Phase 0A), CHECKER ALGORITHM (Phase 0B), and DECLARE CONTRADICTION (Step 8b) — the fourth field creates a machine-checkable link from the contradiction event to the pre-declared prediction without prose reading.

**C-42 surface 2 — FAIL-CATEGORY closed-vocabulary token per finding row**

The V-03 single-axis design adds `FAIL-CATEGORY: [AUTH / BOUNDARY / CONTRACT / TIMEOUT / STATE / PERMISSION]` to every Step 12 finding row. The promotability gate: do all finding rows carry FAIL-CATEGORY tokens with values drawn exclusively from the six-item vocabulary? If the model produces values outside the vocabulary ("SCHEMA", "SECURITY", "PERFORMANCE") in more than one finding, the vocabulary is not machine-freezable as specified and the criterion remains in Tier D. If in-vocabulary values appear consistently, the criterion advances to Tier C and the vocabulary becomes the freezable token set.

**C-43 design surface (opened by R18 V-02)** — Falsification path as structural token at TRACE CONTRACT validation

V-02's explicit falsification branch (`matches HALT-EXPECTED-BOUNDARY: no`) in DECLARE CONTRADICTION creates a structural linkage: when DECLARE CONTRADICTION fires with `no`, the TRACE CONTRACT validation should produce the "falsified -- actual halt boundary was [label]" variant. The question for C-43: is the TRACE CONTRACT validation outcome structurally determined by the `matches HALT-EXPECTED-BOUNDARY: [yes/no]` value in Step 8b DECLARE CONTRADICTION, creating a machine-verifiable consistency constraint between the Step 8b token and the TRACE CONTRACT validation token? If V-02 and V-05 consistently produce matching DECLARE CONTRADICTION / TRACE CONTRACT validation pairs (yes → confirmed, no → falsified-wrong-boundary), a C-43 criterion becomes designable: the TRACE CONTRACT validation token value is derivable from the DECLARE CONTRADICTION `matches HALT-EXPECTED-BOUNDARY:` field value without prose reading.
