Good. R5 all-100 confirms all 24 prior criteria encode as baseline. The four new v6 criteria (C-25/C-26/C-27/C-28) all surfaced but only V-05 hit C-27 and C-28 simultaneously. Round 6 variations need to implement all four new criteria in every variation, differentiated by *how* each is implemented — not whether.

**Axis selection:**
- V-01 single: Role sequence (expert owns all contamination control — Phase 0 + challenge)
- V-02 single: Output format (three named artifacts: manifest → skeleton → filled table)
- V-03 single: Lifecycle emphasis (Phase 1B as standalone phase with own gate + frontmatter key)
- V-04 combined: Inertia framing + amendment type taxonomy (C-23/C-28 as interdependent axes)
- V-05 combined: Full integration (6-key frontmatter, all four new criteria, challenge phase keyed)

---

## trace-contract Skill Body Variations — Round 6

---

## V-01

**Variation axis:** Role sequence — Connectors contract expert owns both contamination control steps (Phase 0 scope enumeration and Phase 1 challenge); Automate executes all production phases

**Hypothesis:** Assigning both anti-contamination responsibilities to a single expert role (scope definition and challenge review) creates a coherent single-owner contamination watchdog, reducing coordination overhead and making the two-reader attestation (C-27) semantically clear: the expert who defined scope is the same expert who challenges derivation

---

```yaml
---
skill: trace-contract
topic: [TOPIC]
spec_version: [SPEC VERSION]
date: [DATE]
gate0_scope_confirmed: false
gate1_isolation_confirmed: false
gate2_actual_complete: false
gate3_diff_complete: false
gate4b_calibration_confirmed: false
---
```

**Roles:**
- **Connectors contract expert** — Phase 0 (scope enumeration) and Phase 1 challenge (contamination review). Owns both anti-contamination steps. Does not execute production phases.
- **Automate** — Phase 1A (skeleton + value derivation), Phase 2, Phase 3, Phase 4B, Phase 4, Phase 5. Does not define scope or review contamination.

---

### PHASE 0 — Scope Enumeration (Connectors contract expert)

Read the spec. Produce the SCOPE MANIFEST: a numbered list of every in-scope element, grouped by domain element type.

Domain element types: `schema-field` | `auth-handshake` | `action-payload` | `trigger-payload` | `error-shape` | `metadata`

For each element: Element Name | Domain Element Type | Spec Clause

This is the prior commitment. Phase 1A completeness is verifiable against this manifest by any reader independent of Phase 1A construction. Automate may not add elements during Phase 1A; only fill values for committed rows.

**GATE 0** (Connectors contract expert signs):
- [ ] Every spec-named element appears in the SCOPE MANIFEST
- [ ] No element omitted because its expected value is uncertain or low-confidence
- [ ] Every row has a Domain Element Type from the fixed vocabulary
- [ ] Every row has a Spec Clause citation
- [ ] SCOPE MANIFEST written in full before Automate begins Phase 1A
- [ ] `gate0_scope_confirmed: true` written to frontmatter

---

### PHASE 1A — Expected Output (Automate, from SCOPE MANIFEST only)

Receive the SCOPE MANIFEST from Phase 0. Proceed in two steps.

**Step 1 — Skeleton:** Build EXPECTED-SKELETON from the manifest. Columns: `Element Name | Domain Element Type | Spec Clause | Expected Value`. Populate Name, Type, Spec Clause from manifest rows. Expected Value: blank for all rows. Commit the skeleton before Step 2. Record row count: "SKELETON COMMITTED — N rows."

**Step 2 — Value derivation:** Fill Expected Value for each pre-committed skeleton row. Source: spec clauses only.
- Blank Expected Value in a committed row = omission finding. Record it; do not remove the row.
- Do not add rows not in the SCOPE MANIFEST.
- Do not reference actual output.
- Do not reference what you know the connector currently does.

Mark Phase 1A complete: "PHASE 1A COMPLETE — [N] values derived, [M] omissions."

---

### PHASE 1 CHALLENGE — Contamination Review (Connectors contract expert)

Review every Phase 1A Expected Value for contamination. Two contamination paths:
1. **Actual output leakage** — value reflects known actual output rather than spec
2. **Inertia anchoring** — value reflects current connector runtime behavior rather than spec

**Challenge Log:**

| Row | Element Name | Expected Value | Path 1 Signal | Path 2 Signal | Disposition |
|-----|--------------|---------------|---------------|---------------|-------------|
| | | | None / Present | None / Present | clean / revised / flagged |

- `revised`: state the corrected value
- `flagged`: cannot resolve — Automate marks as omission finding and removes from expected table

**GATE 1** (Connectors contract expert attests):
- [ ] Actual output not consulted during Phase 1A — not just ordered after, but not consulted at all — `[CONFIRMED / NOT CONFIRMED]`
- [ ] Expert runtime knowledge of connector behavior not used to constrain any expected value — not just ordered after, but excluded entirely — `[CONFIRMED / NOT CONFIRMED]`
- [ ] No Spec Clause cells blank in expected table
- [ ] No Expected Value cells blank except recorded omission findings
- [ ] Challenge log reviewed — no contamination signals carried into final table
- [ ] `gate1_isolation_confirmed: true` written to frontmatter

---

### PHASE 2 — Actual Output (Automate)

Run or retrieve the actual operation output. Record verbatim. No annotation, no analysis.

**GATE 2**: `[ ]` Actual output complete and unedited. Set `gate2_actual_complete: true`.

---

### PHASE 3 — Diff / Classification (Automate — no root causes in this phase)

Row-by-row diff of EXPECTED-SKELETON (filled) vs Phase 2 actual. Classify each row.

**Classification table:** `Element Name | Domain Element Type | Spec Clause | Expected | Actual | Classification | Severity`

- Classification: `Match` | `Mismatch` | `Missing` | `Extra`
- Severity (required on all non-Match rows): `breaking` | `degraded` | `cosmetic`
- Blank Severity cell on non-Match row = gate failure
- Blank Spec Clause cell = gate failure
- Blank Domain Element Type cell = gate failure
- **Stop. Do not write root causes here. Root causes go in Phase 4. Not here.**

**GATE 3**:
- [ ] No Severity cells blank on non-Match rows
- [ ] No Spec Clause cells blank
- [ ] No Domain Element Type cells blank
- [ ] No root cause hypotheses present in classification table
- [ ] `gate3_diff_complete: true` written to frontmatter

---

### PHASE 4B — Severity Calibration (Automate — standalone, do not merge with Phase 4)

Build severity tally before writing any assessment:

| Severity | Count |
|----------|-------|
| breaking | |
| degraded | |
| cosmetic | |

Justify each finding's severity individually. A single rationale covering all findings is a gate failure — each element requires its own justification sentence.

**CONTRACT DELTA does not begin until GATE 4B passes.**

**GATE 4B**:
- [ ] Severity tally populated before assessment written
- [ ] Each finding individually justified at its assigned severity level — group-level justification is not accepted
- [ ] Distribution reviewed: not all one level unless each element individually justified at that level
- [ ] `gate4b_calibration_confirmed: true` written to frontmatter

---

### PHASE 4 — Findings (Automate)

One block per non-Match row:

```
Finding: [Element Name]
Severity: [from Phase 4B calibration — breaking / degraded / cosmetic]
Spec Ref: [spec clause]
Mismatch: [precise description of expected vs actual delta]
Root cause hypothesis: [named connector-contract mechanism —
  field-mapping error / auth-handshake gap / action-payload omission /
  trigger-payload schema deviation / error-shape mismatch /
  metadata-convention violation
  "Unknown" alone does not pass; name the candidate mechanism]
Resolution: [specific action — name the spec clause, field, or flow step;
  "Investigate further" alone does not pass]
```

---

### PHASE 5 — CONTRACT DELTA (Automate writes; Connectors contract expert reviews amendment-type taxonomy)

| Finding | Spec Clause | Amendment Description | Priority | Amendment Type |
|---------|-------------|----------------------|----------|----------------|

- **Priority** (required, derived from Phase 4B calibrated severity): `breaking → P1` | `degraded → P2` | `cosmetic → P3`. Blank = gate failure.
- **Amendment Type** (required, fixed vocabulary): `add-field` | `remove-field` | `change-type` | `change-enum` | `change-error-shape` | `change-auth-flow`. Blank = gate failure.

Connectors contract expert reviews: (1) every Priority traces to a named Phase 4B calibrated severity; (2) every Amendment Type correctly characterizes the field-level change; (3) no blank cells in either column.

---

---

## V-02

**Variation axis:** Output format — three named committed artifacts (SCOPE MANIFEST → EXPECTED-SKELETON → EXPECTED-TABLE) with each artifact boundary explicitly marked

**Hypothesis:** A three-artifact chain makes C-25 and C-26 independently verifiable — SCOPE MANIFEST satisfies C-25 (prior commitment); EXPECTED-SKELETON satisfies C-26 (coverage commitment separated from value derivation); the two can fail independently, and a reader can verify either without reading the other

---

```yaml
---
skill: trace-contract
topic: [TOPIC]
spec_version: [SPEC VERSION]
date: [DATE]
gate0_scope_confirmed: false
gate1_isolation_confirmed: false
gate2_actual_complete: false
gate3_diff_complete: false
gate4b_calibration_confirmed: false
---
```

**Roles:**
- **Automate** — Phases 0, 1 (both steps), 2, 3, 4B, 4, 5 execution
- **Connectors contract expert** — Phase 1 challenge log review; Phase 5 amendment-type taxonomy sign-off

---

### PHASE 0 — SCOPE MANIFEST (Automate derives; Connectors contract expert verifies)

Read the spec. Produce **SCOPE MANIFEST** — a numbered list.

For each element: `[N]. Element Name | Domain Element Type | Spec Clause`

Domain Element Types: `schema-field` | `auth-handshake` | `action-payload` | `trigger-payload` | `error-shape` | `metadata`

Mark boundary: `--- SCOPE MANIFEST END ([N] elements) ---`

Connectors contract expert verifies: every spec-named element present; no element omitted for any reason.

**GATE 0**:
- [ ] Every spec-named element in SCOPE MANIFEST
- [ ] No element omitted because its expected value is uncertain
- [ ] Domain Element Type populated for every row
- [ ] Spec Clause populated for every row
- [ ] SCOPE MANIFEST committed before Phase 1 Step 1 begins
- [ ] `gate0_scope_confirmed: true` written to frontmatter

---

### PHASE 1 — Expected Output (Automate, three-artifact protocol)

#### Artifact 1: EXPECTED-SKELETON

Transform SCOPE MANIFEST into a table. Columns: `Element Name | Domain Element Type | Spec Clause | Expected Value`

Populate Name, Type, Spec Clause from SCOPE MANIFEST rows exactly. Expected Value column: blank for every row. Row count must equal SCOPE MANIFEST count.

Mark boundary: `--- EXPECTED-SKELETON COMMITTED ([N] rows, matching SCOPE MANIFEST [N]) ---`

#### Artifact 2: EXPECTED-TABLE

Fill Expected Value for each pre-committed skeleton row. Source: spec clauses only.

Rules:
- Blank Expected Value in a committed row = omission finding — record `[OMISSION: Element Name — Spec Clause — no expected value derivable]`; do not remove the row
- Do not add rows not in the skeleton
- Do not reference actual output
- Do not reference what you know the connector currently does

Mark boundary: `--- EXPECTED-TABLE COMPLETE ([N] values, [M] omissions) ---`

#### Phase 1 Challenge Log (Connectors contract expert reviews EXPECTED-TABLE)

For each row where Expected Value appears runtime-derived rather than spec-derived:

| Row | Element Name | Signal | Path | Disposition |
|-----|--------------|--------|------|-------------|
| | | | Actual leakage / Inertia anchor | clean / revised [new value] / flagged |

Mark: `--- CHALLENGE LOG COMPLETE ([K] rows reviewed, [J] flagged, [J] resolved) ---`

**GATE 1**:
- [ ] Actual output not consulted during Phase 1 — not just ordered after, but not consulted at all — `[CONFIRMED / NOT CONFIRMED]`
- [ ] Expert runtime knowledge of connector not used to constrain any expected value — `[CONFIRMED / NOT CONFIRMED]`
- [ ] No Spec Clause cells blank in EXPECTED-TABLE
- [ ] No Expected Value cells blank except recorded omission findings
- [ ] Challenge log complete — no contamination signals carried into final table
- [ ] `gate1_isolation_confirmed: true` written to frontmatter

---

### PHASE 2 — Actual Output (Automate)

Run or retrieve actual. Record verbatim. No annotation.

**GATE 2**: `[ ]` Complete and unedited. Set `gate2_actual_complete: true`.

---

### PHASE 3 — Diff / Classification (Automate — no root causes)

Diff EXPECTED-TABLE vs Phase 2 actual. Classification table:

`Element Name | Domain Element Type | Spec Clause | Expected | Actual | Classification | Severity`

- Classification: `Match` | `Mismatch` | `Missing` | `Extra`
- Note: `Missing` = row in EXPECTED-TABLE, absent from actual. Structurally visible because EXPECTED-TABLE committed row exists.
- Severity on non-Match rows: `breaking` | `degraded` | `cosmetic` — blank = gate failure
- Blank Spec Clause = gate failure; blank Domain Element Type = gate failure
- **Stop. Root causes go in Phase 4. Not here.**

**GATE 3**:
- [ ] No Severity cells blank on non-Match rows
- [ ] No Spec Clause cells blank
- [ ] No Domain Element Type cells blank
- [ ] No root cause hypotheses in classification table
- [ ] `gate3_diff_complete: true` written to frontmatter

---

### PHASE 4B — Severity Calibration (standalone)

| Severity | Count |
|----------|-------|
| breaking | |
| degraded | |
| cosmetic | |

Per-element individual justification. Group-level justification is a gate failure.

**GATE 4B**:
- [ ] Tally built before assessment written
- [ ] Per-element individual justification for every non-Match row
- [ ] Distribution reviewed — not monolithic unless each element individually justified
- [ ] `gate4b_calibration_confirmed: true` written to frontmatter

---

### PHASE 4 — Findings (Automate)

```
Finding: [Element Name]
Severity: [Phase 4B calibrated]
Spec Ref: [clause]
Mismatch: [description]
Root cause hypothesis: [named mechanism — field-mapping error / auth-handshake gap /
  action-payload omission / trigger-payload deviation / error-shape mismatch /
  metadata-convention violation — "Unknown" alone does not pass]
Resolution: [specific next step — name what to investigate or fix; not "Investigate further" alone]
```

---

### PHASE 5 — CONTRACT DELTA

| Finding | Spec Clause | Amendment Description | Priority | Amendment Type |
|---------|-------------|----------------------|----------|----------------|

Priority: `P1` (breaking) / `P2` (degraded) / `P3` (cosmetic) — from Phase 4B. Blank = gate failure.

Amendment Type: `add-field` | `remove-field` | `change-type` | `change-enum` | `change-error-shape` | `change-auth-flow` — blank = gate failure.

Connectors contract expert reviews amendment-type taxonomy completeness before sign-off.

---

---

## V-03

**Variation axis:** Lifecycle emphasis — Phase 1B is a named standalone phase with its own gate (GATE 1B) and independent frontmatter key (`gate1b_challenge_complete`); GATE 1 does not fire until GATE 1B passes

**Hypothesis:** Giving the challenge log its own phase gate and frontmatter key makes C-27 independently machine-verifiable — downstream automation can confirm the two-reader record completed without parsing the GATE 1 attestation prose, satisfying C-19 extension to the challenge phase

---

```yaml
---
skill: trace-contract
topic: [TOPIC]
spec_version: [SPEC VERSION]
date: [DATE]
gate0_scope_confirmed: false
gate1b_challenge_complete: false
gate1_isolation_confirmed: false
gate2_actual_complete: false
gate3_diff_complete: false
gate4b_calibration_confirmed: false
---
```

**Roles:**
- **Automate** — Phase 0, Phase 1A, Phase 2, Phase 3, Phase 4B, Phase 4, Phase 5
- **Connectors contract expert** — Phase 1B (challenge log), Phase 5 taxonomy review

---

### PHASE 0 — Scope Enumeration (Automate)

Read spec. Enumerate all in-scope elements. Format: `Element Name | Domain Element Type | Spec Clause`

Domain types: `schema-field` | `auth-handshake` | `action-payload` | `trigger-payload` | `error-shape` | `metadata`

**GATE 0**:
- [ ] All spec elements present — no omissions for any reason
- [ ] Every row has Domain Element Type from fixed vocabulary
- [ ] Every row has Spec Clause
- [ ] List committed before Phase 1A begins
- [ ] `gate0_scope_confirmed: true` written to frontmatter

---

### PHASE 1A — Expected Output (Automate)

**Step 1 — Skeleton:** Build index from Phase 0 list. Columns: `Element Name | Domain Element Type | Spec Clause | Expected Value`. Expected Value: blank. Commit before Step 2: `SKELETON COMMITTED — [N] rows`.

**Step 2 — Derivation:** Fill Expected Value from spec only.
- Blank in committed row = omission finding (record; do not remove row)
- Do not reference actual output
- Do not reference current connector runtime behavior

Phase 1A complete: `PHASE 1A COMPLETE — [N] values, [M] omissions`

---

### PHASE 1B — Contamination Review (Connectors contract expert — standalone phase)

This phase produces the **Challenge Log** as a named output artifact. GATE 1 does not fire until this phase is complete and GATE 1B passes.

Review every Phase 1A Expected Value row. Two contamination paths:
1. Actual output leakage
2. Inertia anchoring (connector runtime knowledge rather than spec)

**Challenge Log:**

| Row | Element Name | Expected Value | Path 1 | Path 2 | Disposition | Revised Value |
|-----|--------------|---------------|--------|--------|-------------|---------------|
| | | | None/Present | None/Present | clean/revised/flagged | |

- `revised`: new value entered in Revised Value column; Phase 1A table updated
- `flagged`: unresolvable — demote to omission finding, remove from expected table

Phase 1B complete: `PHASE 1B COMPLETE — [K] rows reviewed, [J] revised, [L] flagged`

**GATE 1B** (Connectors contract expert signs):
- [ ] Challenge log covers every Phase 1A row — no rows skipped
- [ ] No flagged rows remain in expected table (all demoted to omission findings)
- [ ] Challenge log committed as named Phase 1B output
- [ ] `gate1b_challenge_complete: true` written to frontmatter

---

### GATE 1 (Automate attests — fires only after GATE 1B passes)

- [ ] Actual output not consulted during Phase 1A — not just ordered after, but not consulted at all — `[CONFIRMED / NOT CONFIRMED]`
- [ ] Expert runtime knowledge not used to constrain any expected value — `[CONFIRMED / NOT CONFIRMED]`
- [ ] No Spec Clause cells blank in expected table
- [ ] No Expected Value cells blank except recorded omission findings
- [ ] Phase 1B challenge log complete — references `gate1b_challenge_complete: true`
- [ ] `gate1_isolation_confirmed: true` written to frontmatter

---

### PHASE 2 — Actual Output (Automate)

Run or retrieve actual. Verbatim. No annotation.

**GATE 2**: `[ ]` Complete and unedited. Set `gate2_actual_complete: true`.

---

### PHASE 3 — Diff / Classification (Automate — no root causes)

`Element Name | Domain Element Type | Spec Clause | Expected | Actual | Classification | Severity`

Severity on non-Match rows: `breaking` | `degraded` | `cosmetic` — blank = gate failure. Spec Clause blank = gate failure. Domain Element Type blank = gate failure. **No root causes.**

**GATE 3**:
- [ ] No Severity cells blank on non-Match rows
- [ ] No Spec Clause cells blank
- [ ] No Domain Element Type cells blank
- [ ] No root cause hypotheses in classification table
- [ ] `gate3_diff_complete: true` written to frontmatter

---

### PHASE 4B — Severity Calibration (standalone)

| Severity | Count |
|----------|-------|
| breaking | |
| degraded | |
| cosmetic | |

Per-element individual justification. Group-level justification is a gate failure.

**GATE 4B**:
- [ ] Tally built before assessment
- [ ] Per-element individual justification
- [ ] Distribution reviewed
- [ ] `gate4b_calibration_confirmed: true` written to frontmatter

---

### PHASE 4 — Findings (Automate)

```
Finding: [Element Name]
Severity: [Phase 4B calibrated]
Spec Ref: [clause]
Mismatch: [description]
Root cause hypothesis: [named mechanism — not "Unknown" alone]
Resolution: [specific action — not "Investigate further" alone]
```

---

### PHASE 5 — CONTRACT DELTA (Connectors contract expert reviews taxonomy)

| Finding | Spec Clause | Amendment Description | Priority | Amendment Type |
|---------|-------------|----------------------|----------|----------------|

Priority: `P1`/`P2`/`P3` from Phase 4B. Amendment Type: `add-field` | `remove-field` | `change-type` | `change-enum` | `change-error-shape` | `change-auth-flow`. Blank cells in either column = gate failure.

---

---

## V-04

**Variation axes:** Inertia framing + amendment type taxonomy — the connector's current behavior (inertia baseline) is named in Phase 0 as a separate contamination artifact; CONTRACT DELTA characterizes each amendment as a transition from inertia to spec, making amendment types semantically grounded in what kind of inertia is being overcome

**Hypothesis:** When the inertia baseline is a named Phase 0 artifact (parallel to the scope list), C-23 (anti-inertia contamination clause) and C-28 (amendment type taxonomy) become structurally interdependent: the challenge log checks against the named inertia baseline, and amendment types name the kind of inertia-to-spec transition required

---

```yaml
---
skill: trace-contract
topic: [TOPIC]
spec_version: [SPEC VERSION]
date: [DATE]
inertia_baseline_committed: false
gate0_scope_confirmed: false
gate1_isolation_confirmed: false
gate2_actual_complete: false
gate3_diff_complete: false
gate4b_calibration_confirmed: false
---
```

**Roles:**
- **Connectors contract expert** — Phase 0B (inertia baseline), Phase 0 GATE verification, Phase 1 challenge, Phase 5 amendment-type review
- **Automate** — Phase 0A (scope from spec), Phase 1, Phase 2, Phase 3, Phase 4B, Phase 4, Phase 5 execution

---

### PHASE 0 — Scope + Inertia Enumeration

#### Phase 0A — Scope from Spec (Automate)

Read the spec. Enumerate in-scope elements: `Element Name | Domain Element Type | Spec Clause`

Domain types: `schema-field` | `auth-handshake` | `action-payload` | `trigger-payload` | `error-shape` | `metadata`

Mark: `SCOPE LIST COMPLETE — [N] elements`

#### Phase 0B — Inertia Baseline (Connectors contract expert)

Name what the connector currently does for each element. Source: current connector documentation, observed behavior, or known deployed state — **not the spec**.

Format: `Element Name | Inertia Value | Inertia Source (doc / observed / inferred)`

Cover every element in the Phase 0A scope list. If inertia value is unknown, record `unknown`.

Mark: `INERTIA BASELINE COMPLETE — [N] elements`

**Critical:** The inertia baseline is a **contamination artifact** — not the expected output. It exists to be explicitly excluded from Phase 1 derivation. Automate may not reference it during Phase 1.

**GATE 0**:
- [ ] Phase 0A scope list complete — every spec element present
- [ ] Every scope row has Domain Element Type and Spec Clause
- [ ] Phase 0B inertia baseline complete — every scope element covered
- [ ] Inertia baseline marked as contamination-excluded — explicitly off-limits during Phase 1
- [ ] `inertia_baseline_committed: true` written to frontmatter
- [ ] `gate0_scope_confirmed: true` written to frontmatter

---

### PHASE 1 — Expected Output (Automate, spec only — inertia baseline excluded)

**Step 1 — Skeleton:** Build index from Phase 0A scope list. Columns: `Element Name | Domain Element Type | Spec Clause | Expected Value`. Expected Value: blank. Commit: `SKELETON COMMITTED — [N] rows`.

**Step 2 — Derivation:** Fill Expected Value from spec clauses only.
- Blank in committed row = omission finding (record; do not remove)
- Do not reference actual output
- **Do not reference the Phase 0B inertia baseline** — this is the inertia-specific anti-contamination clause; knowing what the connector currently does must not anchor expected values; the inertia baseline is a named contamination path distinct from actual output leakage

Phase 1 complete: `PHASE 1 COMPLETE — [N] values, [M] omissions`

**Phase 1 Challenge** (Connectors contract expert reviews against inertia baseline):

For each row, compare Expected Value against Phase 0B inertia value. Flag if Expected Value matches inertia value rather than spec derivation:

| Row | Element Name | Expected Value | Inertia Value | Signal | Disposition |
|-----|--------------|---------------|---------------|--------|-------------|
| | | | | None / Inertia match | clean / revised / flagged |

**GATE 1**:
- [ ] Actual output not consulted during Phase 1 — not just ordered after, but not consulted at all — `[CONFIRMED / NOT CONFIRMED]`
- [ ] Inertia baseline not referenced during Phase 1 derivation — inertia-specific anti-contamination confirmed — `[CONFIRMED / NOT CONFIRMED]`
- [ ] No Spec Clause cells blank in expected table
- [ ] No Expected Value cells blank except recorded omission findings
- [ ] Challenge log complete — no inertia-contamination signals carried into final table
- [ ] `gate1_isolation_confirmed: true` written to frontmatter

---

### PHASE 2 — Actual Output (Automate)

Record verbatim. No annotation.

**GATE 2**: `[ ]` Complete and unedited. Note where actual matches inertia baseline rather than expected — mark as `spec-inertia delta` in Notes. Set `gate2_actual_complete: true`.

---

### PHASE 3 — Diff / Classification (Automate — no root causes)

`Element Name | Domain Element Type | Spec Clause | Expected | Actual | Inertia Value | Classification | Severity | Notes`

- Inertia Value: carry from Phase 0B
- Notes: flag `spec-inertia delta` where Actual = Inertia ≠ Expected (connector is implementing its own inertia rather than the spec)
- Severity on non-Match rows: `breaking` | `degraded` | `cosmetic` — blank = gate failure
- **No root causes**

**GATE 3**:
- [ ] No Severity cells blank on non-Match rows
- [ ] No Spec Clause cells blank
- [ ] No Domain Element Type cells blank
- [ ] Inertia Value column populated for all rows
- [ ] No root cause hypotheses
- [ ] `gate3_diff_complete: true` written to frontmatter

---

### PHASE 4B — Calibration (standalone)

| Severity | Count |
|----------|-------|
| breaking | |
| degraded | |
| cosmetic | |

Per-element individual justification. Note: `spec-inertia delta` findings may warrant `breaking` (full replacement of inertia behavior required) — justify individually; do not apply as a group rule.

**GATE 4B**:
- [ ] Tally built before assessment
- [ ] Per-element individual justification (including inertia-delta findings)
- [ ] Distribution reviewed
- [ ] `gate4b_calibration_confirmed: true` written to frontmatter

---

### PHASE 4 — Findings (Automate)

```
Finding: [Element Name]
Severity: [Phase 4B calibrated]
Spec Ref: [clause]
Inertia Value: [from Phase 0B]
Mismatch: [description — note if actual matches inertia baseline]
Root cause hypothesis: [named mechanism — inertia persistence /
  field-mapping error / auth-handshake gap / action-payload omission /
  trigger-payload deviation / error-shape mismatch /
  metadata-convention violation — "Unknown" alone does not pass]
Resolution: [specific action]
```

---

### PHASE 5 — CONTRACT DELTA (inertia-to-spec transition map)

Each entry names the transition from inertia baseline to spec. The amendment type characterizes what kind of change that transition requires.

| Finding | Spec Clause | Inertia Value | Spec Value | Amendment Description | Priority | Amendment Type |
|---------|-------------|--------------|------------|----------------------|----------|----------------|

- **Priority**: `P1`/`P2`/`P3` from Phase 4B. Blank = gate failure.
- **Amendment Type** (characterizes the inertia-to-spec transition — fixed vocabulary required):
  - `add-field` — spec requires a field absent from the inertia baseline
  - `remove-field` — spec removes a field present in the inertia baseline
  - `change-type` — spec changes the type of an existing field
  - `change-enum` — spec changes allowed enum values
  - `change-error-shape` — spec changes error response structure
  - `change-auth-flow` — spec changes the auth handshake
  - Blank = gate failure

Connectors contract expert reviews: (1) every Amendment Type correctly characterizes the inertia-to-spec transition for that element; (2) no blank cells in Priority or Amendment Type.

---

---

## V-05

**Variation axes:** Full v6 integration — C-25 (Phase 0 prior commitment), C-26 (pre-populated skeleton), C-27 (Phase 1B as standalone phase with own gate + frontmatter key), C-28 (amendment type taxonomy) unified into a coherent 6-gate artifact with complete frontmatter coverage

**Hypothesis:** A 6-key frontmatter manifest (`gate0_scope_confirmed`, `gate1b_challenge_complete`, `gate1_isolation_confirmed`, `gate2_actual_complete`, `gate3_diff_complete`, `gate4b_calibration_confirmed`) extends C-19 to cover the challenge phase as an independently queryable gate — downstream automation can verify the two-reader record completed without inspecting GATE 1 prose, producing the highest-fidelity machine-verifiable audit trail

---

```yaml
---
skill: trace-contract
topic: [TOPIC]
spec_version: [SPEC VERSION]
date: [DATE]
gate0_scope_confirmed: false
gate1b_challenge_complete: false
gate1_isolation_confirmed: false
gate2_actual_complete: false
gate3_diff_complete: false
gate4b_calibration_confirmed: false
---
```

**Roles:**
- **Connectors contract expert** — Phase 0 (scope enumeration), Phase 1B (contamination review), Phase 5 taxonomy sign-off
- **Automate** — Phase 1A (skeleton + derivation), Phase 2, Phase 3, Phase 4B, Phase 4, Phase 5 execution

---

### PHASE 0 — Scope Enumeration (Connectors contract expert)

Read the spec. Do not list what you expect the connector to return. List what the spec defines. Produce the **SCOPE MANIFEST**.

For each element: `[N]. Element Name | Domain Element Type | Spec Clause`

Domain types: `schema-field` | `auth-handshake` | `action-payload` | `trigger-payload` | `error-shape` | `metadata`

Mark: `--- SCOPE MANIFEST COMMITTED ([N] elements) ---`

This manifest is the prior commitment. Phase 1A completeness is verifiable against it by any reader independent of Phase 1A.

**GATE 0** (Connectors contract expert signs):
- [ ] Every spec-named element in SCOPE MANIFEST — no element omitted for any reason (uncertainty is not grounds for omission)
- [ ] Every row has Domain Element Type from fixed vocabulary — blank = gate failure
- [ ] Every row has Spec Clause — blank = gate failure
- [ ] SCOPE MANIFEST committed before Automate begins Phase 1A
- [ ] `gate0_scope_confirmed: true` written to frontmatter

---

### PHASE 1A — Expected Skeleton (Automate)

Receive SCOPE MANIFEST from Phase 0.

**Step 1 — Skeleton:** Build EXPECTED-SKELETON from manifest rows. Columns: `Element Name | Domain Element Type | Spec Clause | Expected Value`. Populate Name, Type, Spec Clause from manifest. Expected Value: blank for all rows. Row count must match manifest count.

Mark: `--- EXPECTED-SKELETON COMMITTED ([N] rows — matches SCOPE MANIFEST [N]) ---`

**Step 2 — Value derivation:** Fill Expected Value for each committed row from spec only.
- A blank Expected Value in a committed row is a structural omission — record `[OMISSION: Name / Clause]`; the row stays
- Do not reference actual output — which connector-contract mechanism does the spec define? Derive from that
- Do not reference current connector runtime behavior — which spec clause defines this? Not which value the connector returns today

Mark: `--- PHASE 1A COMPLETE ([N] values, [M] omissions) ---`

---

### PHASE 1B — Challenge Log (Connectors contract expert — standalone phase)

Review every Phase 1A Expected Value. This phase produces the **CHALLENGE LOG** as a named output artifact. GATE 1 does not fire until GATE 1B passes.

Two contamination paths per row:
1. **Actual output leakage** — does the expected value reflect what actual output is known to produce?
2. **Inertia anchoring** — does the expected value reflect what the connector currently does rather than what the spec defines?

**CHALLENGE LOG:**

| Row | Element Name | Expected Value | Path 1 | Path 2 | Disposition | Final Value |
|-----|--------------|---------------|--------|--------|-------------|-------------|
| | | | None/Present | None/Present | clean/revised/flagged | |

- `clean` — no signals; value proceeds as written
- `revised` — contamination detected; enter corrected spec-derived value in Final Value
- `flagged` — contamination unresolvable; demote to omission finding; remove row from expected table

Mark: `--- CHALLENGE LOG COMPLETE ([K] rows reviewed, [J] revised, [L] flagged → demoted to omissions) ---`

**GATE 1B** (Connectors contract expert signs):
- [ ] CHALLENGE LOG covers every Phase 1A row — no rows skipped
- [ ] No `flagged` rows remain in expected table — all demoted to omission findings
- [ ] CHALLENGE LOG committed as named Phase 1B output artifact
- [ ] `gate1b_challenge_complete: true` written to frontmatter

---

### GATE 1 (joint — fires only after GATE 1B passes; references `gate1b_challenge_complete`)

- [ ] Actual output not consulted during Phase 1A — not just ordered after, but not consulted at all — `[CONFIRMED / NOT CONFIRMED]`
- [ ] Expert runtime knowledge of connector not used to constrain any expected value — not just ordered after, but excluded entirely — `[CONFIRMED / NOT CONFIRMED]`
- [ ] No Spec Clause cells blank in expected table — gate-level enforcement, not instruction compliance
- [ ] No Expected Value cells blank except recorded omission findings
- [ ] Phase 1B challenge log complete — `gate1b_challenge_complete: true` confirmed before this gate fires
- [ ] `gate1_isolation_confirmed: true` written to frontmatter

---

### PHASE 2 — Actual Output (Automate)

Run or retrieve actual. Record verbatim. No annotation, no analysis.

**GATE 2**: `[ ]` Actual output complete and unedited. Set `gate2_actual_complete: true`.

---

### PHASE 3 — Diff / Classification (Automate — stop; root causes go in Phase 4, not here)

Diff EXPECTED-SKELETON (filled, post-Phase 1B) vs Phase 2 actual. Classify each row.

`Element Name | Domain Element Type | Spec Clause | Expected | Actual | Classification | Severity`

- Classification: `Match` | `Mismatch` | `Missing` | `Extra`
- `Missing` = row committed in EXPECTED-SKELETON but absent from actual — structurally visible because the skeleton row exists
- Severity on non-Match rows: `breaking` | `degraded` | `cosmetic` — blank = gate failure
- Blank Spec Clause = gate failure; blank Domain Element Type = gate failure
- **Stop. Do not write root causes here. Root causes go in Phase 4. Not here. Classify the gap. Name the severity. Do not explain why.**

**GATE 3**:
- [ ] No Severity cells blank on non-Match rows
- [ ] No Spec Clause cells blank
- [ ] No Domain Element Type cells blank
- [ ] No root cause hypotheses present in classification table
- [ ] `gate3_diff_complete: true` written to frontmatter

---

### PHASE 4B — Severity Calibration (standalone — do not merge with Phase 4)

Count before writing any assessment:

| Severity | Count | % |
|----------|-------|---|
| breaking | | |
| degraded | | |
| cosmetic | | |

What about each element's gap — not the framing, not the expectation, but the gap itself — makes it breaking, degraded, or cosmetic? Answer per element. A single rationale covering all findings is a gate failure.

**CONTRACT DELTA does not begin until GATE 4B passes.**

**GATE 4B**:
- [ ] Severity tally built before any assessment written
- [ ] Each finding individually justified — group-level justification is a gate failure; if all one level, every finding has an element-level justification sentence
- [ ] Distribution reviewed: not monolithic unless each element is individually justified at that level
- [ ] `gate4b_calibration_confirmed: true` written to frontmatter

---

### PHASE 4 — Findings (Automate)

```
Finding: [Element Name]
Severity: [Phase 4B calibrated — breaking / degraded / cosmetic]
Spec Ref: [spec clause]
Mismatch: [precise description of expected vs actual delta]
Root cause hypothesis: [which connector-contract mechanism is responsible?
  Name it specifically: field-mapping error / auth-handshake gap /
  action-payload omission / trigger-payload schema deviation /
  error-shape mismatch / metadata-convention violation
  "Unknown" alone does not pass — name the candidate mechanism even if not yet confirmed]
Resolution: [specific investigation or fix step — name the spec clause, field, or auth flow step;
  "Investigate further" alone does not pass]
```

---

### PHASE 5 — CONTRACT DELTA (Automate writes; Connectors contract expert reviews both columns)

| Finding | Spec Clause | Amendment Description | Priority | Amendment Type |
|---------|-------------|----------------------|----------|----------------|

**Priority** (required — derived from Phase 4B calibrated severity; each entry traceable to a named finding with an individually justified severity level):
- `breaking → P1` | `degraded → P2` | `cosmetic → P3`
- Blank = gate failure

**Amendment Type** (required — fixed vocabulary; orthogonal to Priority; enables amendment grouping by change kind independent of urgency):
- `add-field` — spec requires a field not currently present
- `remove-field` — spec removes a field currently present
- `change-type` — spec changes the type of an existing field
- `change-enum` — spec changes the allowed values of an enum
- `change-error-shape` — spec changes the error response structure
- `change-auth-flow` — spec changes the authentication handshake
- Blank = gate failure

Connectors contract expert reviews: (1) every Priority traces to a named Phase 4B individually justified severity; (2) every Amendment Type correctly characterizes the field-level change kind; (3) no blank cells in either column.

---

### Frontmatter audit (Automate — final step)

Verify all six keys are `true`:

```
gate0_scope_confirmed        ← Phase 0 scope committed before Phase 1A
gate1b_challenge_complete    ← Phase 1B two-reader challenge log complete
gate1_isolation_confirmed    ← Phase 1 isolation confirmed (backed by gate1b)
gate2_actual_complete        ← Phase 2 actual recorded
gate3_diff_complete          ← Phase 3 classification complete
gate4b_calibration_confirmed ← Phase 4B standalone calibration confirmed
```

Any `false` value = artifact incomplete. Do not mark artifact final until all six confirm. Each key is independently queryable — downstream automation may verify any individual gate without treating the artifact as a single pass/fail.

---

## Axis and Hypothesis Summary

| Variation | Axis | Hypothesis | C-25 | C-26 | C-27 | C-28 | Keys |
|-----------|------|-----------|------|------|------|------|------|
| V-01 | Role sequence — expert owns both contamination steps | Single-owner contamination watchdog cleaner than role-swapping | Phase 0 expert-owned | Skeleton in Phase 1A | Challenge in GATE 1 sub-step | Phase 5 | 5 |
| V-02 | Output format — three named committed artifacts | Three-artifact chain makes C-25/C-26 independently verifiable | SCOPE MANIFEST artifact | EXPECTED-SKELETON artifact | Challenge in GATE 1 sub-step | Phase 5 | 5 |
| V-03 | Lifecycle emphasis — Phase 1B as standalone phase with own gate | Phase 1B own gate + key makes C-27 independently machine-verifiable | Phase 0 compact | Skeleton in Phase 1A | Phase 1B + GATE 1B | Phase 5 | 6 |
| V-04 | Inertia framing + amendment type taxonomy | Named inertia baseline makes C-23/C-28 structurally interdependent | Phase 0 scope | Skeleton in Phase 1A | Challenge keyed to inertia baseline | Inertia-to-spec transition taxonomy | 6 |
| V-05 | Full integration — 6-key frontmatter | Challenge phase as independently queryable gate produces highest-fidelity audit trail | Phase 0 expert-owned | Phase 1A two-step | Phase 1B + GATE 1B + own key | Priority + Amendment Type both gated | 6 |
