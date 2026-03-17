Now I have full context from R6. Let me generate all 5 variations for R7. The key challenge: R7 adds C-29 (challenge gate as independent queryable key) and C-30 (Phase 0 inertia exclusion). R6 V-03/V-05 already had C-29; R6 V-04 already had C-30. R7 baseline requires **all 5 variations** to encode both.

---

# trace-contract — Round 7 Variations (V-01 through V-05)

**Rubric target:** v7 (C-01 through C-30, formula A/22×10)
**New baseline requirements:** C-29 (`gate1b_challenge_confirmed` as independent key), C-30 (Phase 0 inertia exclusion instruction + GATE 0 clause)
**Variation axes:** V-01 role sequence, V-02 output format, V-03 lifecycle emphasis, V-04 inertia framing + amendment taxonomy, V-05 combined full integration

---

## V-01: Role Sequence — Expert Owns All Contamination Gates; Automate Owns All Derivation

**Axis:** Role ownership sequence. Automate derives; Expert attests. No role shares a gate with itself.

**Hypothesis:** Making role ownership the explicit structural axis (rather than a note) prevents the most common contamination failure — the phase 1 author self-certifying isolation. Expert cannot contaminate Automate's derivation; Automate cannot self-certify isolation.

---

```markdown
---
skill: trace-contract
topic: "{{TOPIC}}"
connector: "{{CONNECTOR_NAME}}"
spec_version: "{{SPEC_VERSION}}"
date: "{{DATE}}"
gate0_scope_confirmed: false
gate1_isolation_confirmed: false
gate1b_challenge_confirmed: false
gate2_actual_complete: false
gate3_diff_complete: false
gate4b_calibration_confirmed: false
---

# trace-contract: {{CONNECTOR_NAME}}

**Roles**
- **Automate** — Connectors platform engineer. Owns: Phase 1A (expected value derivation), Phase 2
  (actual output retrieval), Phase 3 (classification). Derives only; never attests.
- **Expert** — Connectors contract expert. Owns: Phase 0 (scope enumeration and signature), Phase 1B
  (challenge review), Phase 4 (root cause hypotheses), Phase 4B (severity calibration), Phase 5
  (delta authorship). Attests only on work not authored by Expert.

**Role handoff rule:** A role may not attest to its own work. Expert does not review Expert's Phase 4
output; Automate does not attest to Automate's Phase 1A isolation. Every gate is owned by the role
that did NOT build the output being attested.

---

## PHASE 0 — Scope Enumeration (Expert)

Expert enumerates all in-scope elements from the spec. Do not consult actual connector output. Do not
anchor scope to current connector behavior — scope is spec-defined; list what the spec defines, not
what you expect the connector to return based on its current implementation.

Build the SCOPE MANIFEST table:

| # | Element Name | Domain Element Type | Spec Clause |
|---|--------------|---------------------|-------------|

Domain Element Type vocabulary (required — no blank cells):
`schema-field` | `auth-handshake` | `action-payload` | `trigger-payload` | `error-shape` | `metadata`

Spec Clause: cite the specific clause, section, or item number. No blank cells.

After the table, Expert writes: `SCOPE MANIFEST COMPLETE — N elements listed.`

### GATE 0 (Automate reviews Expert's scope)

Automate verifies the SCOPE MANIFEST before Phase 1A begins.

- [ ] SCOPE MANIFEST is present and signed by Expert
- [ ] No blank Domain Element Type cells
- [ ] No blank Spec Clause cells
- [ ] Inertia check: no element name appears anchored to current connector behavior rather than spec
      definition — names derive from spec vocabulary, not from what the connector currently returns
- [ ] SCOPE MANIFEST row count recorded: N = ___

If all pass: set `gate0_scope_confirmed: true` in frontmatter. Phase 1A may begin.
If any fail: return SCOPE MANIFEST to Expert for correction. Phase 1A does not begin.

---

## PHASE 1A — Expected Output Derivation (Automate)

Automate derives expected values from the spec only. Actual connector output has not been retrieved
and must not be consulted at any point during this phase.

**Step 1 — Build the EXPECTED-SKELETON.** For each row in the SCOPE MANIFEST, create a row with
Element Name, Domain Element Type, and Spec Clause copied exactly. Leave Expected Value blank.
Record: `SKELETON COMMITTED — N rows.`

**Step 2 — Fill Expected Values.** For each pre-committed skeleton row, derive the expected value
from the spec clause cited. Do not modify Element Name, Domain Element Type, or Spec Clause when
filling Expected Value.

Completed EXPECTED TABLE:

| # | Element Name | Domain Element Type | Spec Clause | Expected Value |
|---|--------------|---------------------|-------------|----------------|

After the table, Automate writes: `EXPECTED TABLE COMPLETE — N rows. Actual output not consulted.`

### GATE 1 (Expert reviews Automate's Phase 1A)

Expert verifies the EXPECTED TABLE before Phase 1B begins.

- [ ] Actual output was not consulted during Phase 1A — not just ordered after, but not consulted at
      all — [CONFIRMED / NOT CONFIRMED]
- [ ] Expert runtime knowledge of current connector behavior was not used to constrain any expected
      value — not just ordered after, but excluded entirely — [CONFIRMED / NOT CONFIRMED]
- [ ] No blank Expected Value cells
- [ ] No blank Spec Clause cells in expected table rows
- [ ] No blank Domain Element Type cells
- [ ] EXPECTED TABLE row count matches SCOPE MANIFEST row count: ___

If all pass: set `gate1_isolation_confirmed: true` in frontmatter. Phase 1B may begin.
If any fail: return EXPECTED TABLE to Automate for correction. Phase 1B does not begin.

---

## PHASE 1B — Challenge Review (Expert)

Expert reviews each Phase 1A row for contamination signals. This phase is coordinate and standalone;
it is not a sub-step of Phase 1A and cannot be merged with it. Expert is the sole author of Phase 1B;
Automate does not participate in Phase 1B.

For each row in the EXPECTED TABLE, Expert records:

CHALLENGE LOG:

| Row | Element Name | Expected Value | Path 1 Signal (actual output consulted?) | Path 2 Signal (inertia anchor?) | Disposition |
|-----|--------------|----------------|------------------------------------------|---------------------------------|-------------|

Path 1 Signal: any evidence the expected value was constrained by actual connector output. Enter
`none` or describe the signal.
Path 2 Signal: any evidence the expected value was anchored to known current connector behavior
rather than derived from the cited spec clause. Enter `none` or describe the signal.
Disposition: `clean` (no signals) or `contaminated — return to Phase 1A` with reason.

After the log, Expert writes: `CHALLENGE COMPLETE — N rows reviewed. Contamination signals found: N.`

### GATE 1B (Automate reviews Expert's challenge log)

Automate verifies the CHALLENGE LOG before Phase 2 begins.

- [ ] Challenge log is present; Expert is identified as author
- [ ] All N Phase 1A rows appear in challenge log — no rows skipped
- [ ] No blank Path 1 Signal cells; no blank Path 2 Signal cells; no blank Disposition cells
- [ ] Zero contaminated rows, OR contaminated rows returned to Phase 1A and re-derived before
      proceeding
- [ ] Challenge outcome is clean: no contamination signals carried into Phase 2

If all pass: set `gate1b_challenge_confirmed: true` in frontmatter. Phase 2 may begin.
If any fail: return challenge log to Expert for completion, or route contaminated rows to Phase 1A.
Phase 2 does not begin until gate1b_challenge_confirmed is true.

---

## PHASE 2 — Actual Output Retrieval (Automate)

Automate retrieves the actual connector output. This is the first point at which actual output is
consulted. Gate 1 and Gate 1B must both be confirmed before this phase runs.

Record actual output in the ACTUAL TABLE:

| # | Element Name | Domain Element Type | Spec Clause | Actual Value |
|---|--------------|---------------------|-------------|--------------|

Use the same Element Name, Domain Element Type, and Spec Clause from the EXPECTED TABLE.
If an element is absent in actual output, record `ABSENT`.

After the table, Automate writes: `ACTUAL TABLE COMPLETE — N rows.`

### GATE 2 (Expert reviews Automate's actual table)

- [ ] All expected table elements appear in actual table
- [ ] No blank Actual Value cells — `ABSENT` is a valid value; blank is not
- [ ] Domain Element Type and Spec Clause columns match expected table identically

If all pass: set `gate2_actual_complete: true` in frontmatter. Phase 3 may begin.

---

## PHASE 3 — Classification (Automate)

Automate diffs EXPECTED TABLE against ACTUAL TABLE. Classify each element as `Match` or `Mismatch`.
For mismatches, record Severity and Spec Clause.

**Stop. Do not write root cause hypotheses here. Root causes go in Phase 4. Not here.**

CLASSIFICATION TABLE:

| # | Element Name | Domain Element Type | Expected Value | Actual Value | Result | Severity | Spec Clause |
|---|--------------|---------------------|----------------|--------------|--------|----------|-------------|

Severity vocabulary (mismatch rows only): `breaking` | `degraded` | `cosmetic`
Severity cells blank on mismatch rows = gate failure.

After the table, Automate writes: `CLASSIFICATION COMPLETE. Mismatches: N. Root cause hypotheses:
none written.`

### GATE 3 (Expert reviews Automate's classification)

- [ ] No Severity cells blank on mismatch rows
- [ ] No Spec Clause cells blank on mismatch rows
- [ ] No Domain Element Type cells blank on any row
- [ ] No root cause hypotheses present in classification table — classification only

If all pass: set `gate3_diff_complete: true` in frontmatter. Phase 4 may begin.

---

## PHASE 4 — Root Cause Hypotheses (Expert)

Expert writes a finding for each mismatch row. Classification from Phase 3 is input; analysis begins
here. Do not reclassify or modify Phase 3 severity in this phase.

Finding scaffold (required for every mismatch):

```
Finding F-NN: [Element Name]
Mismatch: [Expected Value] → [Actual Value]
Severity: [from Phase 3]
Spec Reference: [Spec Clause from Phase 3]
Root Cause Hypothesis: [Name a specific connector-contract mechanism responsible for this gap.
  Vocabulary: field-mapping error | auth-handshake deviation | action-payload schema mismatch |
  trigger-payload schema mismatch | error-response shape deviation | metadata convention violation.
  "Unknown" alone does not pass — name a candidate mechanism even if unconfirmed.]
Resolution: [Specific action. Name the artifact, field, flow step, or spec clause to target.
  "Investigate further" alone does not pass — name what to investigate specifically.]
```

---

## PHASE 4B — Severity Calibration (Expert — standalone; do not merge with Phase 4)

Expert reviews the full finding set for severity calibration. This phase runs alone; Phase 5 does
not begin until GATE 4B passes.

**Step 1 — Tally table:**

| Severity | Count |
|----------|-------|
| breaking | |
| degraded | |
| cosmetic | |
| TOTAL | |

**Step 2 — Per-element justification.** For each finding, Expert writes one sentence justifying the
assigned severity level. The sentence must name the element and the reason for the specific level.
Group-level justification ("all breaking because inertia implies full replacement") is not accepted —
each element requires its own justification.

**Step 3 — Distribution review.** Expert writes: `Distribution reviewed: [describe the mix and
confirm it is not all one level unless each element is individually justified at that level].`

### GATE 4B (Automate reviews Expert's calibration)

- [ ] Tally table present and complete
- [ ] Each finding individually justified at its assigned severity level — group-level justification
      is not accepted; each element must be named individually
- [ ] Distribution reviewed: not all one level unless each element individually justified

If all pass: set `gate4b_calibration_confirmed: true` in frontmatter. Phase 5 may begin.

---

## PHASE 5 — CONTRACT DELTA (Expert)

Expert writes the consolidated delta. Priority derives from Phase 4B calibrated severity. Amendment
Type classifies the change kind. Both columns are required; blank cells = gate failure.

CONTRACT DELTA:

| Finding | Element Name | Spec Clause | Severity | Priority | Amendment Type | Amendment Description |
|---------|--------------|-------------|----------|----------|----------------|----------------------|

Priority mapping (from Phase 4B): `breaking → P1` | `degraded → P2` | `cosmetic → P3`
Blank Priority cells = gate failure. Every entry traceable to a named Phase 4B calibrated finding.

Amendment Type vocabulary (required — no blank cells):
`add-field` | `remove-field` | `change-type` | `change-enum` | `change-error-shape` | `change-auth-flow`
Blank Amendment Type cells = gate failure.

Expert review of CONTRACT DELTA before closing:
- (1) Every Priority annotation traces to a named Phase 4B calibrated finding
- (2) Every Amendment Type correctly characterizes the field-level change kind
- (3) No blank cells in Priority or Amendment Type columns

After the table, Expert writes: `CONTRACT DELTA COMPLETE — N amendments. Review: (1) [pass/fail],
(2) [pass/fail], (3) [pass/fail].`
```

---

## V-02: Output Format — Five Named Artifacts with Gate Transitions Between Artifacts

**Axis:** Output format. The artifact is a chain of five named documents; each document is a gate boundary. Challenge Log is the third named artifact — not a phase sub-step.

**Hypothesis:** Treating the challenge log as a named, committed artifact (not a phase-embedded sub-step) makes the challenge outcome more structurally auditable than embedding it in GATE 1. The artifact boundary is a harder stopping point than a gate checkbox: the next artifact cannot begin until the previous is signed.

---

```markdown
---
skill: trace-contract
topic: "{{TOPIC}}"
connector: "{{CONNECTOR_NAME}}"
spec_version: "{{SPEC_VERSION}}"
date: "{{DATE}}"
gate0_scope_confirmed: false
gate1_isolation_confirmed: false
gate1b_challenge_confirmed: false
gate2_actual_complete: false
gate3_diff_complete: false
gate4b_calibration_confirmed: false
---

# trace-contract: {{CONNECTOR_NAME}}

This skill produces five named artifacts in sequence. No artifact may be started until the prior
artifact's gate passes. Gate outcomes are recorded as queryable frontmatter keys.

**Roles**
- **Automate** — Connectors platform engineer. Derives expected values (Artifact 2), retrieves
  actual output (Artifact 4 input), constructs diff (Artifact 4).
- **Expert** — Connectors contract expert. Enumerates scope (Artifact 1), reviews challenge
  (Artifact 3), writes hypotheses and calibration (Artifact 4 analysis), authors delta (Artifact 5).

**Artifact chain:**

```
[Artifact 1: SCOPE-MANIFEST] → GATE 0
  → [Artifact 2: EXPECTED-SKELETON + EXPECTED-TABLE] → GATE 1
    → [Artifact 3: CHALLENGE-LOG] → GATE 1B
      → [Artifact 4: CONTRACT-DIFF] → GATE 3 / GATE 4B
        → [Artifact 5: CONTRACT-DELTA]
```

---

## ARTIFACT 1 — SCOPE-MANIFEST (Expert)

Expert enumerates all in-scope connector contract elements from the spec. Do not consult actual
connector output. Do not anchor scope to what you know the connector currently returns — scope is
spec-defined. Inertia contamination path: naming elements based on current connector behavior rather
than spec definitions is a contamination form identical to consulting actual output and is explicitly
prohibited here.

SCOPE-MANIFEST table:

| # | Element Name | Domain Element Type | Spec Clause |
|---|--------------|---------------------|-------------|

Domain Element Type vocabulary (required; no blank cells):
`schema-field` | `auth-handshake` | `action-payload` | `trigger-payload` | `error-shape` | `metadata`

Expert signs: `SCOPE-MANIFEST SIGNED — N elements. Authored: Expert.`

### GATE 0

- [ ] SCOPE-MANIFEST is present and signed by Expert
- [ ] No blank Domain Element Type cells
- [ ] No blank Spec Clause cells
- [ ] No element name anchored to current connector behavior rather than spec-defined terminology
- [ ] Row count confirmed: N = ___

Pass → `gate0_scope_confirmed: true`. Artifact 2 may begin.
Fail → return Artifact 1 to Expert for correction.

---

## ARTIFACT 2 — EXPECTED-SKELETON + EXPECTED-TABLE (Automate)

Artifact 2 has two committed sub-outputs: EXPECTED-SKELETON (committed first), then EXPECTED-TABLE
(values filled into skeleton). The boundary between skeleton and table is explicit — the skeleton
must be committed before any Expected Value is written.

**EXPECTED-SKELETON** (Automate, Step 1)

Copy all rows from SCOPE-MANIFEST. Add Expected Value column; leave all Expected Value cells blank.
Do not fill any Expected Value cells in this step.

| # | Element Name | Domain Element Type | Spec Clause | Expected Value |
|---|--------------|---------------------|-------------|----------------|

Record: `SKELETON COMMITTED — N rows. Expected Value: blank for all rows.`

**EXPECTED-TABLE** (Automate, Step 2)

For each pre-committed skeleton row, derive the expected value from the spec clause cited. Fill
Expected Value cells only. Do not alter Element Name, Domain Element Type, or Spec Clause. Actual
connector output has not been retrieved and must not be consulted.

Record: `EXPECTED-TABLE COMPLETE — N rows. Actual output: not consulted at any point.`

### GATE 1

- [ ] Actual output was not consulted during Artifact 2 construction — not just ordered after, but
      not consulted at all — [CONFIRMED / NOT CONFIRMED]
- [ ] Expert runtime knowledge of current connector behavior was not used to constrain any Expected
      Value — spec derivation only — [CONFIRMED / NOT CONFIRMED]
- [ ] No blank Expected Value cells in EXPECTED-TABLE
- [ ] No blank Spec Clause cells in EXPECTED-TABLE
- [ ] No blank Domain Element Type cells
- [ ] EXPECTED-TABLE row count matches SCOPE-MANIFEST: ___

Pass → `gate1_isolation_confirmed: true`. Artifact 3 may begin.
Fail → return Artifact 2 to Automate for correction.

---

## ARTIFACT 3 — CHALLENGE-LOG (Expert)

Expert reviews every row of EXPECTED-TABLE for contamination signals. This artifact is a named,
committed document — not a gate item embedded in GATE 1 and not a sub-step of Artifact 2. The
CHALLENGE-LOG must be completed and signed before GATE 1B fires.

For every row in EXPECTED-TABLE, Expert annotates:

| Row | Element Name | Expected Value | Path 1 Signal | Path 2 Signal | Disposition |
|-----|--------------|----------------|---------------|---------------|-------------|

Path 1 Signal: evidence the Expected Value was constrained by actual connector output. `none` if
absent; describe the signal if present.
Path 2 Signal: evidence the Expected Value was anchored to known current connector behavior rather
than the cited spec clause. `none` if absent; describe the signal if present.
Disposition: `clean` or `contaminated — route to Phase 1A step 2 for re-derivation` with reason.

No blank cells allowed in Path 1, Path 2, or Disposition columns.

Expert signs: `CHALLENGE-LOG SIGNED — N rows reviewed. Contamination signals found: N.
All contaminated rows routed for re-derivation: [YES / N/A — none found].`

### GATE 1B

- [ ] CHALLENGE-LOG is present and signed by Expert
- [ ] All N EXPECTED-TABLE rows appear in CHALLENGE-LOG — no rows skipped
- [ ] No blank Path 1 Signal, Path 2 Signal, or Disposition cells
- [ ] Zero unresolved contaminated rows entering Artifact 4
- [ ] Challenge outcome is clean: no contamination signals carried forward

Pass → `gate1b_challenge_confirmed: true`. Artifact 4 may begin.
Fail → route to Expert for challenge log completion or contaminated rows to Automate for re-derivation.

Note: `gate1b_challenge_confirmed` is a separate key from `gate1_isolation_confirmed`. Downstream
automation must verify both independently. An artifact where isolation is confirmed but challenge
has not yet completed is distinct from one where both are confirmed.

---

## ARTIFACT 4 — CONTRACT-DIFF (Automate + Expert)

Artifact 4 has four phases: actual retrieval (Automate), classification (Automate), root cause
hypotheses (Expert), and severity calibration (Expert, standalone).

### Phase 2 — Actual Output Retrieval (Automate)

Retrieve actual connector output. This is the first point at which actual output is consulted.

ACTUAL-TABLE:

| # | Element Name | Domain Element Type | Spec Clause | Actual Value |
|---|--------------|---------------------|-------------|--------------|

`ABSENT` = element not present in actual output. Blank = gate failure.

### GATE 2

- [ ] All SCOPE-MANIFEST elements appear in ACTUAL-TABLE
- [ ] No blank Actual Value cells
- [ ] Domain Element Type and Spec Clause match EXPECTED-TABLE

Pass → `gate2_actual_complete: true`. Classification may begin.

### Phase 3 — Classification (Automate)

Diff EXPECTED-TABLE against ACTUAL-TABLE row by row.

**Stop. Do not write root causes. Do not form hypotheses. Classify the gap; name the severity.
Phase 4 is where hypotheses go. Not here.**

CLASSIFICATION TABLE:

| # | Element Name | Domain Element Type | Expected Value | Actual Value | Result | Severity | Spec Clause |
|---|--------------|---------------------|----------------|--------------|--------|----------|-------------|

Severity (mismatch rows): `breaking` | `degraded` | `cosmetic`. Blank = gate failure.

Record: `CLASSIFICATION COMPLETE. Match: N. Mismatch: N. Root cause hypotheses written: NONE.`

### GATE 3

- [ ] No Severity cells blank on mismatch rows
- [ ] No Spec Clause cells blank on mismatch rows
- [ ] No Domain Element Type cells blank on any row
- [ ] No root cause hypotheses present in classification table

Pass → `gate3_diff_complete: true`. Phase 4 may begin.

### Phase 4 — Root Cause Hypotheses (Expert)

For each mismatch, Expert writes a finding. Do not reclassify severity from Phase 3.

```
Finding F-NN: [Element Name]
Mismatch: [Expected] → [Actual]
Severity: [Phase 3 classification]
Spec Reference: [Spec Clause]
Root Cause Hypothesis: [Specific connector-contract mechanism. Vocabulary:
  field-mapping error | auth-handshake deviation | action-payload schema mismatch |
  trigger-payload schema mismatch | error-response shape deviation | metadata convention violation.
  "Unknown" alone does not pass.]
Resolution: [Specific action naming artifact, field, flow step, or spec clause to target.
  "Investigate further" alone does not pass.]
```

### Phase 4B — Severity Calibration (Expert — standalone; do not merge with Phase 4)

**Tally table:**

| Severity | Count |
|----------|-------|
| breaking | |
| degraded | |
| cosmetic | |
| TOTAL | |

**Per-element justification:** For each finding, one sentence naming the element and justifying its
severity level individually. Group-level justification is a gate failure condition.

**Distribution review:** `Distribution reviewed — [describe; confirm not all one level unless
individually justified element by element].`

### GATE 4B

- [ ] Tally table present and complete
- [ ] Each finding individually justified — group justification is not accepted
- [ ] Distribution reviewed: not all one level unless each element individually justified

Pass → `gate4b_calibration_confirmed: true`. Artifact 5 may begin.

---

## ARTIFACT 5 — CONTRACT-DELTA (Expert)

Consolidated delta. Every entry traceable to a named Phase 4B calibrated finding.

| Finding | Element Name | Spec Clause | Severity | Priority | Amendment Type | Amendment Description |
|---------|--------------|-------------|----------|----------|----------------|----------------------|

Priority: `breaking → P1` | `degraded → P2` | `cosmetic → P3`. Blank = gate failure.
Amendment Type: `add-field` | `remove-field` | `change-type` | `change-enum` | `change-error-shape`
  | `change-auth-flow`. Blank = gate failure.

Expert reviews CONTRACT-DELTA:
- (1) Every Priority annotation traces to a named Phase 4B calibrated finding — [PASS / FAIL]
- (2) Every Amendment Type correctly characterizes the field-level change kind — [PASS / FAIL]
- (3) No blank cells in Priority or Amendment Type columns — [PASS / FAIL]

Expert signs: `CONTRACT-DELTA COMPLETE — N amendments. All three review items: [PASS].`
```

---

## V-03: Lifecycle Emphasis — Phase 1B as Standalone Coordinate Phase with GATE 1B and gate1b Key

**Axis:** Lifecycle emphasis. Every phase is explicitly labeled, sequenced, and gated. Phase 1B is a first-class lifecycle event with its own phase header, gate, and frontmatter key — not a gate item inside GATE 1 and not a sub-step of Phase 1A.

**Hypothesis:** Maximum phase decomposition — naming every phase explicitly with its own gate — makes structural gaps visible. When Phase 1B has its own header and GATE 1B, skipping or compressing it is structurally impossible, not just instruction-level prohibited.

---

```markdown
---
skill: trace-contract
topic: "{{TOPIC}}"
connector: "{{CONNECTOR_NAME}}"
spec_version: "{{SPEC_VERSION}}"
date: "{{DATE}}"
gate0_scope_confirmed: false
gate1_isolation_confirmed: false
gate1b_challenge_confirmed: false
gate2_actual_complete: false
gate3_diff_complete: false
gate4b_calibration_confirmed: false
---

# trace-contract: {{CONNECTOR_NAME}}

**Lifecycle** (6 gates, 8 phases):

```
Phase 0 → GATE 0 → Phase 1A → GATE 1 → Phase 1B → GATE 1B
  → Phase 2 → GATE 2 → Phase 3 → GATE 3 → Phase 4 → Phase 4B → GATE 4B → Phase 5
```

**Roles**
- **Automate** — Connectors platform engineer. Phases: 1A, 2, 3.
- **Expert** — Connectors contract expert. Phases: 0, 1B, 4, 4B, 5.

**Gate ownership:** Each gate is owned by the role that did NOT author the phase output being
confirmed.

---

## PHASE 0 — Scope Enumeration (Expert)

Expert enumerates all in-scope connector contract elements from the spec before Phase 1A begins.

**Inertia exclusion (required):** Do not anchor scope to what the connector currently returns.
Do not list what you expect the connector to return based on its current implementation. Scope is
spec-defined — every element name derives from the spec, not from knowledge of existing behavior.
Inertia contamination at Phase 0 is scope-level: an element whose name is anchored to current
connector behavior introduces a biased commitment before any value is derived.

SCOPE LIST:

| # | Element Name | Domain Element Type | Spec Clause |
|---|--------------|---------------------|-------------|

Domain Element Type (required; no blank cells):
`schema-field` | `auth-handshake` | `action-payload` | `trigger-payload` | `error-shape` | `metadata`

Expert writes: `PHASE 0 COMPLETE — N elements enumerated. Authored: Expert.`

### GATE 0 (Automate verifies Phase 0)

- [ ] SCOPE LIST is present; Expert is listed as author
- [ ] No blank Domain Element Type cells in SCOPE LIST
- [ ] No blank Spec Clause cells in SCOPE LIST
- [ ] No element name appears anchored to current connector behavior rather than spec-defined
      vocabulary — inertia contamination at scope level is a gate failure condition
- [ ] SCOPE LIST row count recorded: N = ___

Pass → `gate0_scope_confirmed: true`. Phase 1A may begin.
Fail → return SCOPE LIST to Expert for revision.

---

## PHASE 1A — Expected Value Derivation (Automate)

Automate derives expected values from the spec. Actual connector output has not been retrieved.
Actual connector output must not be consulted at any point during Phase 1A.

**Step 1 — EXPECTED-SKELETON.** For every element in the SCOPE LIST, create a row copying Element
Name, Domain Element Type, and Spec Clause exactly. Set Expected Value to blank. Commit the skeleton
before Step 2.

Record: `SKELETON COMMITTED — N rows. Step 2 not yet begun.`

| # | Element Name | Domain Element Type | Spec Clause | Expected Value |
|---|--------------|---------------------|-------------|----------------|
(All Expected Value cells blank — this is the committed skeleton.)

**Step 2 — Expected Value fill.** For each pre-committed row, derive Expected Value from the cited
Spec Clause. Do not modify other columns.

Completed PHASE 1A OUTPUT:

| # | Element Name | Domain Element Type | Spec Clause | Expected Value |
|---|--------------|---------------------|-------------|----------------|

Automate writes: `PHASE 1A COMPLETE — N rows. Actual output: NOT CONSULTED.`

### GATE 1 (Expert verifies Phase 1A)

- [ ] Actual output was not consulted during Phase 1A — not just ordered after, but not consulted
      at all — [CONFIRMED / NOT CONFIRMED]
- [ ] Expert runtime knowledge of current connector behavior was not used to constrain any Expected
      Value — spec derivation only, not inertia anchoring — [CONFIRMED / NOT CONFIRMED]
- [ ] No blank Expected Value cells
- [ ] No blank Spec Clause cells in Phase 1A output rows
- [ ] No blank Domain Element Type cells
- [ ] Phase 1A row count matches SCOPE LIST: ___

Pass → `gate1_isolation_confirmed: true`. Phase 1B may begin.
Fail → return Phase 1A output to Automate for correction.

---

## PHASE 1B — Challenge Review (Expert)

Phase 1B is a coordinate, standalone phase. It is not a gate item inside GATE 1. It is not a
sub-step of Phase 1A. Phase 1B has its own gate (GATE 1B) and its own frontmatter key
(`gate1b_challenge_confirmed`), independent of `gate1_isolation_confirmed`. Downstream automation
may confirm isolation (gate1_isolation_confirmed) without confirming challenge (gate1b_challenge_confirmed),
or vice versa; the two are independently queryable.

Expert reviews every Phase 1A row for contamination signals.

CHALLENGE LOG:

| Row | Element Name | Expected Value | Path 1 Signal (actual output) | Path 2 Signal (inertia anchor) | Disposition |
|-----|--------------|----------------|-------------------------------|--------------------------------|-------------|

Path 1 Signal: evidence the Expected Value was constrained by actual connector output. `none` or
describe.
Path 2 Signal: evidence the Expected Value was anchored to known current connector behavior rather
than derived from the cited Spec Clause. `none` or describe.
Disposition: `clean` or `contaminated — route to Phase 1A Step 2 for re-derivation`.

No blank cells in Path 1 Signal, Path 2 Signal, or Disposition columns — blank = gate 1B failure.

Expert writes: `PHASE 1B COMPLETE — N rows reviewed. Contamination signals: N.
All contaminated rows re-derived: [YES / N/A]. Challenge outcome: CLEAN.`

### GATE 1B (Automate verifies Phase 1B)

- [ ] CHALLENGE LOG is present; Phase 1B header is labeled as a coordinate standalone phase
- [ ] All N Phase 1A rows appear in CHALLENGE LOG — no rows skipped
- [ ] No blank Path 1 Signal, Path 2 Signal, or Disposition cells
- [ ] Zero unresolved contaminated rows
- [ ] Challenge outcome is clean: no contamination signals carried into Phase 2

Pass → `gate1b_challenge_confirmed: true`. Phase 2 may begin.
Fail → return challenge log to Expert for completion; route contaminated rows to Phase 1A.

`gate1b_challenge_confirmed` is a separate frontmatter key from `gate1_isolation_confirmed`.
An artifact where `gate1_isolation_confirmed: true` and `gate1b_challenge_confirmed: false` is in a
valid intermediate state: isolation confirmed, challenge pending. Both must be `true` before Phase 2
begins.

---

## PHASE 2 — Actual Output Retrieval (Automate)

First phase in which actual connector output is consulted. GATE 1 and GATE 1B must both be
confirmed before Phase 2 runs.

ACTUAL OUTPUT TABLE:

| # | Element Name | Domain Element Type | Spec Clause | Actual Value |
|---|--------------|---------------------|-------------|--------------|

`ABSENT` = element not present in actual output. Blank = gate failure.

Automate writes: `PHASE 2 COMPLETE — N rows. Actual output retrieved.`

### GATE 2 (Expert verifies Phase 2)

- [ ] All SCOPE LIST elements appear in ACTUAL OUTPUT TABLE
- [ ] No blank Actual Value cells
- [ ] Domain Element Type and Spec Clause match Phase 1A columns

Pass → `gate2_actual_complete: true`. Phase 3 may begin.

---

## PHASE 3 — Classification (Automate)

Diff Phase 1A output against Phase 2 output, row by row.

**Stop. Do not write root cause hypotheses here. Classification only. Root causes go in Phase 4.
Any hypothesis written in Phase 3 is a gate 3 failure.**

CLASSIFICATION TABLE:

| # | Element Name | Domain Element Type | Expected Value | Actual Value | Result | Severity | Spec Clause |
|---|--------------|---------------------|----------------|--------------|--------|----------|-------------|

Result: `Match` | `Mismatch`
Severity (mismatch rows only): `breaking` | `degraded` | `cosmetic`. Blank = gate failure.

Automate writes: `PHASE 3 COMPLETE. Match: N. Mismatch: N. Root cause hypotheses: NONE.`

### GATE 3 (Expert verifies Phase 3)

- [ ] No Severity cells blank on mismatch rows
- [ ] No Spec Clause cells blank on mismatch rows
- [ ] No Domain Element Type cells blank on any row
- [ ] No root cause hypotheses present in classification table

Pass → `gate3_diff_complete: true`. Phase 4 may begin.

---

## PHASE 4 — Root Cause Hypotheses (Expert)

Expert writes a finding for each mismatch. Phase 3 severity is input; do not reclassify here.

Finding scaffold:

```
Finding F-NN: [Element Name]
Mismatch: [Expected Value] → [Actual Value]
Severity: [Phase 3 classification — do not modify]
Spec Reference: [Spec Clause from Phase 3]
Root Cause Hypothesis: [Name a specific connector-contract mechanism.
  Vocabulary: field-mapping error | auth-handshake deviation | action-payload schema mismatch |
  trigger-payload schema mismatch | error-response shape deviation | metadata convention violation.
  "Unknown" alone does not pass — name a candidate mechanism.]
Resolution: [Name the specific artifact, field, flow step, or spec clause to target.
  "Investigate further" alone does not pass.]
```

---

## PHASE 4B — Severity Calibration (Expert — standalone phase; do not merge with Phase 4)

Phase 4B is a dedicated, named phase. It is not a gate item at the end of Phase 4. CONTRACT DELTA
(Phase 5) does not begin until GATE 4B passes.

**Step 1 — Tally table:**

| Severity | Count |
|----------|-------|
| breaking | |
| degraded | |
| cosmetic | |
| TOTAL | |

**Step 2 — Per-element justification.** For each finding, one sentence justifying the assigned
severity individually. The sentence must name the element. Group justification is a gate failure
condition — "all breaking because inertia implies full replacement" is not per-element justification.

**Step 3 — Distribution review.** Expert writes: `Distribution reviewed — [describe mix; confirm
not all one level unless every element is individually justified at that level].`

### GATE 4B (Automate verifies Phase 4B)

- [ ] Tally table present and complete
- [ ] Each finding individually justified at its assigned severity — group-level justification
      not accepted; gate failure condition
- [ ] Distribution reviewed and confirmed calibrated

Pass → `gate4b_calibration_confirmed: true`. Phase 5 may begin.

---

## PHASE 5 — CONTRACT DELTA (Expert)

| Finding | Element Name | Spec Clause | Severity | Priority | Amendment Type | Amendment Description |
|---------|--------------|-------------|----------|----------|----------------|----------------------|

Priority (from Phase 4B): `breaking → P1` | `degraded → P2` | `cosmetic → P3`. Blank = gate failure.
Every Priority annotation traceable to a named, individually calibrated Phase 4B finding.

Amendment Type: `add-field` | `remove-field` | `change-type` | `change-enum` | `change-error-shape`
  | `change-auth-flow`. Blank = gate failure.
Column is orthogonal to Priority — amendment batching by change kind is independent of urgency.

Expert review:
- (1) Every Priority traces to a named Phase 4B finding: [PASS / FAIL]
- (2) Every Amendment Type correctly characterizes the change kind: [PASS / FAIL]
- (3) No blank cells in either column: [PASS / FAIL]

Expert writes: `PHASE 5 COMPLETE — N amendments. Review items (1)(2)(3): ALL PASS.`
```

---

## V-04: Inertia Framing + Amendment Taxonomy as Interdependent Axes

**Axes:** Inertia framing (primary) + amendment type taxonomy (secondary). C-30 is the primary structural extension: inertia exclusion closes at both Phase 0 (scope) and GATE 1 (value derivation). The amendment type vocabulary is aligned to inertia-resolution change kinds, creating a causal chain: inertia path named → contamination blocked at two gates → resolution classified by change kind.

**Hypothesis:** When inertia framing is the primary axis, making the Phase 0 inertia instruction and GATE 0 inertia clause structurally parallel to the GATE 1 inertia clause shows the two-gate exclusion pattern most clearly. The amendment type vocabulary then names the resolution for each inertia-induced change kind.

---

```markdown
---
skill: trace-contract
topic: "{{TOPIC}}"
connector: "{{CONNECTOR_NAME}}"
spec_version: "{{SPEC_VERSION}}"
date: "{{DATE}}"
inertia_framing: true
gate0_scope_confirmed: false
gate1_isolation_confirmed: false
gate1b_challenge_confirmed: false
gate2_actual_complete: false
gate3_diff_complete: false
gate4b_calibration_confirmed: false
---

# trace-contract: {{CONNECTOR_NAME}} (Inertia Framing)

This variation applies inertia framing: the connector has an existing implementation whose current
behavior may contaminate spec-derived analysis at two structural entry points —

**Entry point 1 (scope enumeration):** Element names anchored to what the connector currently
returns rather than what the spec defines. Closed by Phase 0 inertia exclusion instruction and
GATE 0 clause.

**Entry point 2 (expected value derivation):** Expected values constrained by knowledge of current
connector behavior rather than derived from spec clauses. Closed by GATE 1 inertia clause.

Both entry points are explicitly closed. Two-gate inertia exclusion is a structural requirement of
this variation.

**Roles**
- **Automate** — Connectors platform engineer. Phases: 1A, 2, 3.
- **Expert** — Connectors contract expert. Phases: 0, 1B, 4, 4B, 5.

---

## PHASE 0 — Scope Enumeration (Expert)

Expert enumerates all in-scope connector contract elements from the spec.

**INERTIA EXCLUSION (GATE 0 prerequisite):** Do not anchor scope to current connector behavior.
Do not list what you expect the connector to return based on what it currently does. Do not
name elements after current connector output fields unless the spec defines them by the same name.
Scope elements derive from the spec — not from runtime knowledge, not from past integrations, not
from what the connector currently supports. Inertia at scope enumeration biases element names before
any expected value is derived; this is the upstream contamination path.

SCOPE MANIFEST:

| # | Element Name | Domain Element Type | Spec Clause |
|---|--------------|---------------------|-------------|

Domain Element Type (required; no blank cells):
`schema-field` | `auth-handshake` | `action-payload` | `trigger-payload` | `error-shape` | `metadata`

Expert writes: `SCOPE MANIFEST COMPLETE — N elements. Authored: Expert.
Inertia exclusion confirmed: element names derive from spec, not current connector behavior.`

### GATE 0 (Automate verifies Phase 0)

- [ ] SCOPE MANIFEST is present and Expert-authored
- [ ] No blank Domain Element Type cells
- [ ] No blank Spec Clause cells
- [ ] INERTIA CHECK: no element name is anchored to current connector behavior rather than
      spec-defined terminology. Element names visible in the spec clause cited — a name not traceable
      to any cited clause is a potential inertia signal and requires Expert to confirm spec provenance.
      Inertia contamination at scope enumeration = gate failure.
- [ ] Row count confirmed: N = ___

Pass → `gate0_scope_confirmed: true`. Phase 1A may begin.
Fail → return SCOPE MANIFEST to Expert for inertia-clean re-enumeration.

---

## PHASE 1A — Expected Value Derivation (Automate)

Automate derives expected values from spec clauses only. Actual connector output has not been
retrieved and must not be consulted.

**Step 1 — EXPECTED-SKELETON.** For each SCOPE MANIFEST row, copy Element Name, Domain Element
Type, Spec Clause exactly. Leave Expected Value blank. Commit before Step 2.

Record: `SKELETON COMMITTED — N rows.`

| # | Element Name | Domain Element Type | Spec Clause | Expected Value |
|---|--------------|---------------------|-------------|----------------|
(Skeleton — all Expected Value cells blank.)

**Step 2 — Fill expected values.** Derive Expected Value from cited Spec Clause. Do not alter other
columns.

PHASE 1A OUTPUT:

| # | Element Name | Domain Element Type | Spec Clause | Expected Value |
|---|--------------|---------------------|-------------|----------------|

Automate writes: `PHASE 1A COMPLETE — N rows. Actual output not consulted.`

### GATE 1 (Expert verifies Phase 1A)

- [ ] Actual output was not consulted during Phase 1A — not just ordered after, but not consulted
      at all — [CONFIRMED / NOT CONFIRMED]
- [ ] Expert runtime knowledge of current connector behavior was not used to constrain any Expected
      Value — spec derivation only; inertia anchoring is explicitly prohibited at this gate — do not
      reference what you know the connector currently does — [CONFIRMED / NOT CONFIRMED]
- [ ] No blank Expected Value cells
- [ ] No blank Spec Clause cells
- [ ] No blank Domain Element Type cells
- [ ] Phase 1A row count matches SCOPE MANIFEST: ___

Pass → `gate1_isolation_confirmed: true`. Phase 1B may begin.
Fail → return Phase 1A to Automate for correction.

Note: GATE 1 closes the second inertia entry point (value derivation). GATE 0 closes the first
(scope enumeration). Together they form the two-gate inertia exclusion — inertia cannot enter at
either Phase 0 element naming or Phase 1A value filling.

---

## PHASE 1B — Challenge Review (Expert)

Expert reviews each Phase 1A row for both contamination paths. This phase is standalone — it has
its own gate (GATE 1B) and its own frontmatter key (`gate1b_challenge_confirmed`) distinct from
`gate1_isolation_confirmed`. The challenge log is the primary output of this phase.

For inertia framing, the challenge log explicitly covers both contamination paths:
- **Path 1:** Actual output consulted during Phase 1A
- **Path 2:** Expected value anchored to known current connector behavior (inertia path)

CHALLENGE LOG:

| Row | Element Name | Expected Value | Path 1 Signal (actual output) | Path 2 Signal (inertia — anchored to current behavior?) | Disposition |
|-----|--------------|----------------|-------------------------------|--------------------------------------------------------|-------------|

Path 2 Signal detail for inertia framing: does the Expected Value name a value, type, or shape
that the connector currently returns, even if the Spec Clause cited does not explicitly require
that specific value? If yes: `potential inertia signal — verify spec derivation`. If no: `none`.

Disposition: `clean` | `contaminated — route to Phase 1A Step 2 for inertia-clean re-derivation`.

No blank cells in Path 1, Path 2, or Disposition columns.

Expert writes: `PHASE 1B COMPLETE — N rows reviewed. Path 1 contamination signals: N.
Path 2 (inertia) contamination signals: N. All contaminated rows re-derived: [YES / N/A].
Challenge outcome: CLEAN.`

### GATE 1B (Automate verifies Phase 1B)

- [ ] CHALLENGE LOG is present; Phase 1B is labeled as a standalone phase (not a GATE 1 sub-item)
- [ ] All N Phase 1A rows appear — no rows skipped
- [ ] No blank Path 1, Path 2, or Disposition cells
- [ ] Path 2 (inertia) signals explicitly reviewed for each row — not merged with Path 1
- [ ] Zero unresolved contaminated rows
- [ ] Challenge outcome: CLEAN

Pass → `gate1b_challenge_confirmed: true`. Phase 2 may begin.
Fail → return to Expert or route contaminated rows to Phase 1A.

`gate1b_challenge_confirmed` is independent of `gate1_isolation_confirmed`. Both must be `true`
before Phase 2 begins.

---

## PHASE 2 — Actual Output Retrieval (Automate)

First phase in which actual connector output is consulted.

ACTUAL TABLE:

| # | Element Name | Domain Element Type | Spec Clause | Actual Value |
|---|--------------|---------------------|-------------|--------------|

`ABSENT` = element not present in actual output.

### GATE 2 (Expert verifies Phase 2)

- [ ] All SCOPE MANIFEST elements appear in ACTUAL TABLE
- [ ] No blank Actual Value cells
- [ ] Domain Element Type and Spec Clause match Phase 1A

Pass → `gate2_actual_complete: true`. Phase 3 may begin.

---

## PHASE 3 — Classification (Automate)

**Stop. Do not write root causes here. Classify the gap. Assign severity. That is all. Phase 4 is
where root causes go.**

CLASSIFICATION TABLE:

| # | Element Name | Domain Element Type | Expected Value | Actual Value | Result | Severity | Spec Clause |
|---|--------------|---------------------|----------------|--------------|--------|----------|-------------|

Severity (mismatch rows): `breaking` | `degraded` | `cosmetic`. Blank = gate failure.

For inertia-framing contexts: severity reflects the gap between spec and actual, not the
magnitude of the inertia. An element that differs because of inertia may be `breaking` or
`degraded` depending on whether the difference prevents a workflow or merely degrades it.

Record: `CLASSIFICATION COMPLETE. Match: N. Mismatch: N. Root cause hypotheses: NONE.`

### GATE 3 (Expert verifies Phase 3)

- [ ] No Severity cells blank on mismatch rows
- [ ] No Spec Clause cells blank on mismatch rows
- [ ] No Domain Element Type cells blank
- [ ] No root cause hypotheses present

Pass → `gate3_diff_complete: true`. Phase 4 may begin.

---

## PHASE 4 — Root Cause Hypotheses (Expert)

Finding scaffold:

```
Finding F-NN: [Element Name]
Mismatch: [Expected] → [Actual]
Severity: [Phase 3]
Spec Reference: [Spec Clause]
Root Cause Hypothesis: [Name the specific connector-contract mechanism responsible.
  For inertia-framing contexts, name whether the root cause is inertia-driven (the connector
  returns a value that its existing implementation has always returned, not what the spec now
  defines) or an independent deviation.
  Vocabulary: field-mapping error | auth-handshake deviation | action-payload schema mismatch |
  trigger-payload schema mismatch | error-response shape deviation | metadata convention violation.
  "Unknown" alone does not pass.]
Resolution: [Name the specific artifact, field, flow step, or spec clause to target.
  "Investigate further" alone does not pass.]
```

---

## PHASE 4B — Severity Calibration (Expert — standalone; do not merge with Phase 4)

**Tally table:**

| Severity | Count |
|----------|-------|
| breaking | |
| degraded | |
| cosmetic | |
| TOTAL | |

**Per-element justification.** For each finding, one sentence naming the element and justifying its
assigned severity individually. Group-level justification is a gate failure condition.

**Inertia-specific calibration note:** "All breaking because inertia implies full replacement" is a
group-level justification even if the framing is accurate — each element requires its own reasoning.
The fact that the connector is locked to inertia-driven behavior does not collectively determine
severity; the functional impact of each specific gap does.

**Distribution review:** `Distribution reviewed — [describe; not all one level unless individually
justified].`

### GATE 4B (Automate verifies Phase 4B)

- [ ] Tally table present
- [ ] Each finding individually justified — group justification not accepted; inertia-framing group
      rationale ("all breaking because inertia") is explicitly named as a gate failure condition
- [ ] Distribution reviewed and calibrated

Pass → `gate4b_calibration_confirmed: true`. Phase 5 may begin.

---

## PHASE 5 — CONTRACT DELTA (Expert)

| Finding | Element Name | Spec Clause | Severity | Priority | Amendment Type | Amendment Description |
|---------|--------------|-------------|----------|----------|----------------|----------------------|

Priority (from Phase 4B): `breaking → P1` | `degraded → P2` | `cosmetic → P3`. Blank = gate failure.

Amendment Type vocabulary (aligned to inertia-resolution change kinds):
`add-field` — spec defines a field the connector does not currently return
`remove-field` — spec removes a field the connector currently returns
`change-type` — connector returns a type the spec no longer defines
`change-enum` — connector returns an enum value the spec no longer permits
`change-error-shape` — error response shape in connector differs from spec definition
`change-auth-flow` — auth handshake behavior in connector diverges from spec flow

Blank Amendment Type cells = gate failure.

**Causal chain check:** For findings where Root Cause Hypothesis named an inertia-driven mechanism,
Amendment Type names the change kind required to resolve it. C-23 + C-30 close the inertia
contamination path; Amendment Type classifies the resolution.

Expert review:
- (1) Every Priority traceable to a named Phase 4B calibrated finding: [PASS / FAIL]
- (2) Every Amendment Type correctly names the inertia-resolution change kind: [PASS / FAIL]
- (3) No blank cells in Priority or Amendment Type: [PASS / FAIL]

Expert writes: `PHASE 5 COMPLETE — N amendments. Review (1)(2)(3): ALL PASS.`
```

---

## V-05: Combined — Interrogative Phrasing + Full Structural Integration + 7-Key Frontmatter

**Axes:** Phrasing register (interrogative throughout) + full structural integration (all four R7-baseline criteria + C-29 + C-30 + maximum gate coverage). The interrogative pattern surfaces reasoning at construction time rather than after the fact: each gate asks "why does this pass?" rather than "did this pass?"

**Hypothesis:** Interrogative phrasing at gates forces explicit reasoning about contamination, not just structural compliance. Combined with the full two-gate Phase 1 chain (GATE 1 + GATE 1B), 7-key frontmatter, Phase 0 inertia exclusion, and amendment type taxonomy, this produces the maximum integration of all 30 criteria in a single coherent prompt.

---

```markdown
---
skill: trace-contract
topic: "{{TOPIC}}"
connector: "{{CONNECTOR_NAME}}"
spec_version: "{{SPEC_VERSION}}"
date: "{{DATE}}"
inertia_framing: true
gate0_scope_confirmed: false
gate1_isolation_confirmed: false
gate1b_challenge_confirmed: false
gate2_actual_complete: false
gate3_diff_complete: false
gate4b_calibration_confirmed: false
---

# trace-contract: {{CONNECTOR_NAME}}

**Roles**
- **Automate** — Connectors platform engineer. Derives; never attests to own work.
- **Expert** — Connectors contract expert. Reviews and attests; never reviews own work.

**Gate manifest (7 keys — all independently queryable):**

| Gate | Key | Owner |
|------|-----|-------|
| GATE 0 | gate0_scope_confirmed | Automate attests Expert's Phase 0 |
| GATE 1 | gate1_isolation_confirmed | Expert attests Automate's Phase 1A isolation |
| GATE 1B | gate1b_challenge_confirmed | Automate attests Expert's Phase 1B challenge |
| GATE 2 | gate2_actual_complete | Expert attests Automate's Phase 2 |
| GATE 3 | gate3_diff_complete | Expert attests Automate's Phase 3 |
| GATE 4B | gate4b_calibration_confirmed | Automate attests Expert's Phase 4B |

`gate1_isolation_confirmed` and `gate1b_challenge_confirmed` are independently queryable.
An artifact where isolation is confirmed but challenge has not yet completed is a valid
intermediate state. Both must be true before Phase 2 begins. Downstream automation must
verify each key independently.

---

## PHASE 0 — Scope Enumeration (Expert)

**What belongs in scope?** Elements the spec defines for this connector contract — not elements
the connector currently supports, not elements from prior versions, not elements you know exist
because of how the connector is implemented today.

**Inertia exclusion (upstream):** Do not list what you expect the connector to return based on
its current behavior. Do not anchor element names to current connector output vocabulary unless
the spec uses the same terminology. Inertia contamination at scope enumeration commits a biased
element list before Phase 1A begins — this is the upstream contamination path, distinct from
the Phase 1A value-derivation path. Both are explicitly closed in this variation.

SCOPE LIST:

| # | Element Name | Domain Element Type | Spec Clause |
|---|--------------|---------------------|-------------|

Domain Element Type (required — no blank cells):
`schema-field` | `auth-handshake` | `action-payload` | `trigger-payload` | `error-shape` | `metadata`

Expert writes:
`PHASE 0 COMPLETE — N elements.
Inertia exclusion: element names derive from spec, not current connector vocabulary.
Which element in this list is most likely to have an inertia-anchored name? [Name it and confirm
it is spec-derived.]`

### GATE 0 (Automate reviews Expert's Phase 0)

- [ ] SCOPE LIST present and Expert-authored
- [ ] No blank Domain Element Type cells — which column has a blank? [name it or confirm none]
- [ ] No blank Spec Clause cells
- [ ] Inertia check: for each element, is the name traceable to a spec clause? Any element whose
      name appears in current connector output but not in any cited spec clause is a potential
      inertia signal — [list signals or confirm none]
- [ ] Row count: N = ___

Pass → `gate0_scope_confirmed: true`. Phase 1A may begin.
Fail → return to Expert; specify which elements need spec-clause provenance confirmation.

---

## PHASE 1A — Expected Value Derivation (Automate)

**Step 1 — EXPECTED-SKELETON.** For every SCOPE LIST row, copy Element Name, Domain Element Type,
Spec Clause. Expected Value: blank. Commit before Step 2.

Record: `SKELETON COMMITTED — N rows. No Expected Values written yet.`

| # | Element Name | Domain Element Type | Spec Clause | Expected Value |
|---|--------------|---------------------|-------------|----------------|
(Skeleton — Expected Value cells blank.)

**Step 2 — Fill Expected Values.** Derive from cited Spec Clause only. For each row: which clause
sentence or item is the source of this Expected Value? If the derivation is not traceable to a
specific clause item, flag the row rather than guessing.

PHASE 1A OUTPUT:

| # | Element Name | Domain Element Type | Spec Clause | Expected Value |
|---|--------------|---------------------|-------------|----------------|

Automate writes:
`PHASE 1A COMPLETE — N rows.
Did I consult actual output at any point? [NO — confirm explicitly]
Did I use knowledge of current connector behavior to shape any Expected Value? [NO — confirm]`

### GATE 1 (Expert reviews Automate's Phase 1A)

- [ ] Actual output was not consulted during Phase 1A — not just ordered after, but not consulted
      at all — [CONFIRMED / NOT CONFIRMED]
      Why does this pass? [Identify the specific mechanism that prevented consultation: separate
      phase block, actual table not yet constructed, etc.]
- [ ] Expert runtime knowledge of current connector behavior was not used to constrain any Expected
      Value — spec derivation only — do not reference what you know the connector currently does;
      inertia anchoring during value derivation is prohibited — [CONFIRMED / NOT CONFIRMED]
      Why does this pass? [Identify which Expected Values were most at risk of inertia anchoring
      and confirm they derive from cited spec clauses, not from known connector behavior.]
- [ ] No blank Expected Value cells — which row is most likely to have a blank? [name or confirm none]
- [ ] No blank Spec Clause cells in Phase 1A rows
- [ ] No blank Domain Element Type cells
- [ ] Row count matches SCOPE LIST: ___

Pass → `gate1_isolation_confirmed: true`. Phase 1B may begin.
Fail → specify which rows failed which items; return to Automate.

---

## PHASE 1B — Challenge Review (Expert)

Phase 1B is a standalone coordinate phase. GATE 1B is its own structural gate with its own
frontmatter key (`gate1b_challenge_confirmed`), separate from `gate1_isolation_confirmed`.
Phase 1B cannot be merged with Phase 1A, embedded as a GATE 1 sub-item, or skipped to reach
Phase 2.

**What does a contamination signal look like?**
- Path 1 (actual output): Expected Value names a specific enum value, field name, or type that
  would only be known from retrieving actual connector output before this phase.
- Path 2 (inertia): Expected Value names a value, type, or shape that matches what the connector
  currently returns, even though the cited spec clause does not require that specific value — the
  derivation traces to current behavior, not to the spec citation.

CHALLENGE LOG:

| Row | Element Name | Expected Value | Path 1 Signal | Path 2 Signal | Disposition |
|-----|--------------|----------------|---------------|---------------|-------------|

No blank cells in Path 1 Signal, Path 2 Signal, or Disposition.

For each row where Disposition is `clean`, Expert writes: `clean — because [reason the expected
value is traceable to the cited spec clause and not to current connector behavior or actual output].`

Expert writes:
`PHASE 1B COMPLETE — N rows reviewed.
Path 1 signals: N.
Path 2 (inertia) signals: N.
Hardest row to certify clean: [name the row; confirm its Expected Value is spec-derived].
Challenge outcome: CLEAN.`

### GATE 1B (Automate reviews Expert's Phase 1B)

- [ ] CHALLENGE LOG present; Phase 1B labeled as standalone coordinate phase
- [ ] All N Phase 1A rows present — which row is most likely to be missing? [name or confirm none]
- [ ] No blank Path 1, Path 2, or Disposition cells
- [ ] Path 2 (inertia) evaluated independently from Path 1 on each row — not merged
- [ ] Zero unresolved contaminated rows
- [ ] "Hardest row" named by Expert — confirms expert reasoning was engaged, not mechanical

Pass → `gate1b_challenge_confirmed: true`. Phase 2 may begin.
Fail → return to Expert or route contaminated rows to Phase 1A.

`gate1b_challenge_confirmed` is independently queryable from `gate1_isolation_confirmed`.
An automation check on `gate1b_challenge_confirmed` does not imply `gate1_isolation_confirmed`
has been verified — they must be checked separately.

---

## PHASE 2 — Actual Output Retrieval (Automate)

First phase in which actual connector output is consulted.
`gate1_isolation_confirmed` must be `true`. `gate1b_challenge_confirmed` must be `true`.
Both keys are checked independently; neither implies the other.

ACTUAL OUTPUT TABLE:

| # | Element Name | Domain Element Type | Spec Clause | Actual Value |
|---|--------------|---------------------|-------------|--------------|

`ABSENT` = element not present. Blank = gate failure.

### GATE 2 (Expert reviews Automate's Phase 2)

- [ ] All SCOPE LIST elements present — which element is most likely to be ABSENT? [name or confirm]
- [ ] No blank Actual Value cells
- [ ] Domain Element Type and Spec Clause match Phase 1A

Pass → `gate2_actual_complete: true`. Phase 3 may begin.

---

## PHASE 3 — Classification (Automate)

**Stop. Do not write root causes here. Classify the gap. Name the severity. Do not explain why.
That is Phase 4. Every hypothesis written during Phase 3 is a gate failure.**

**What kind of gap is this?** Match (Expected = Actual) or Mismatch. For mismatches: what severity
does the gap itself imply — not the framing, not the inertia, but the gap between what the spec
defines and what the connector returned?

CLASSIFICATION TABLE:

| # | Element Name | Domain Element Type | Expected Value | Actual Value | Result | Severity | Spec Clause |
|---|--------------|---------------------|----------------|--------------|--------|----------|-------------|

Severity (mismatch rows): `breaking` | `degraded` | `cosmetic`. Blank = gate failure.

Automate writes: `CLASSIFICATION COMPLETE. Match: N. Mismatch: N. Root cause hypotheses: NONE.`

### GATE 3 (Expert reviews Automate's Phase 3)

- [ ] No Severity cells blank on mismatch rows
- [ ] No Spec Clause cells blank on mismatch rows
- [ ] No Domain Element Type cells blank
- [ ] No root cause hypotheses — which row is most likely to carry a hypothesis? [name or confirm none]

Pass → `gate3_diff_complete: true`. Phase 4 may begin.

---

## PHASE 4 — Root Cause Hypotheses (Expert)

**Which connector-domain mechanism is responsible for this gap?** Name it specifically. Generic
comparisons without a named mechanism do not pass.

Finding scaffold:

```
Finding F-NN: [Element Name]
Mismatch: [Expected] → [Actual]
Severity: [Phase 3 — do not modify]
Spec Reference: [Spec Clause]
Root Cause Hypothesis: [Which connector-domain mechanism is responsible? Name it.
  Vocabulary: field-mapping error | auth-handshake deviation | action-payload schema mismatch |
  trigger-payload schema mismatch | error-response shape deviation | metadata convention violation.
  Is this inertia-driven (connector returning historically established behavior not aligned to
  current spec) or an independent deviation? Name the type.
  "Unknown" alone does not pass — name a candidate mechanism even if unconfirmed.]
Resolution: [What change resolves this gap? Name the specific artifact, field, flow step, or
  spec clause to target. "Investigate further" alone does not pass — name what to investigate.]
```

---

## PHASE 4B — Severity Calibration (Expert — standalone; do not merge with Phase 4)

**Does this severity reflect the gap itself — not the framing, not the inertia, but the gap between
what the spec defines and what the connector returned?**

**Step 1 — Tally table:**

| Severity | Count |
|----------|-------|
| breaking | |
| degraded | |
| cosmetic | |
| TOTAL | |

**Step 2 — Per-element justification.** For each finding, one sentence: `[Element Name] is [severity]
because [specific reason this element's gap at this severity, not a group rationale].`
Group-level justification is a gate failure condition — `inertia-framing group rationale
("all breaking because inertia implies full replacement") explicitly fails this gate`.

**Step 3 — Distribution review.** `Distribution reviewed — [describe; not all one level unless
individually justified; name any element where the assignment surprised you and why it survived
re-review].`

### GATE 4B (Automate reviews Expert's Phase 4B)

- [ ] Tally table present
- [ ] Each finding individually justified — group justification not accepted; group inertia rationale
      explicitly named as gate failure condition — [confirm each finding has its own sentence]
- [ ] Distribution reviewed; named any surprise severity assignments

Pass → `gate4b_calibration_confirmed: true`. Phase 5 may begin.

---

## PHASE 5 — CONTRACT DELTA (Expert)

**What kind of spec change resolves this gap?** Name it. Priority tells us urgency; Amendment Type
tells us change kind. Both are required — they are orthogonal axes.

| Finding | Element Name | Spec Clause | Severity | Priority | Amendment Type | Amendment Description |
|---------|--------------|-------------|----------|----------|----------------|----------------------|

Priority (from Phase 4B): `breaking → P1` | `degraded → P2` | `cosmetic → P3`. Blank = gate failure.
Every Priority annotation traceable to a named, individually calibrated Phase 4B finding.

Amendment Type vocabulary:
`add-field` | `remove-field` | `change-type` | `change-enum` | `change-error-shape` | `change-auth-flow`
Blank = gate failure. Column is orthogonal to Priority: two P1 entries may have different Amendment
Types; two `change-type` entries may have different Priorities.

For inertia-driven findings: Amendment Type names what kind of spec change is required to resolve
the inertia. The causal chain: inertia path named (Phase 4 Root Cause) → resolution classified by
change kind (Phase 5 Amendment Type).

Expert review of CONTRACT DELTA:
- (1) Every Priority traces to a named Phase 4B individually calibrated finding — [PASS / FAIL]
      Why? [Name one Priority entry and trace it to its Phase 4B justification sentence.]
- (2) Every Amendment Type correctly characterizes the change kind — [PASS / FAIL]
      Why? [Name the Amendment Type least obvious from the finding and confirm the classification.]
- (3) No blank cells in Priority or Amendment Type — [PASS / FAIL]

Expert writes: `PHASE 5 COMPLETE — N amendments. Review (1)(2)(3): ALL PASS.`
```

---

## Within-R7 Structural Distinctions

| Signal | V-01 | V-02 | V-03 | V-04 | V-05 |
|--------|------|------|------|------|------|
| C-29 implementation | GATE 1B fires after standalone Phase 1B; `gate1b_challenge_confirmed` independent key | GATE 1B fires after Artifact 3 (CHALLENGE-LOG named artifact); independent key | Phase 1B as coordinate standalone phase with GATE 1B; key independence noted in gate text | Phase 1B standalone; dual-path challenge log (Path 2 = inertia); independent key | Phase 1B standalone; interrogative phrasing at GATE 1B; explicit independence note in gate manifest |
| C-30 implementation | Phase 0 instruction + GATE 0 item both name inertia exclusion | GATE 0 item 4 names inertia at scope enumeration; Artifact 1 instruction prohibits it | Phase 0 instruction + GATE 0 item 4; inertia exclusion parallel to GATE 1 item 2 | Primary axis: Phase 0 instruction + GATE 0 item 4 parallel to GATE 1 item 2; most explicit two-gate articulation | Phase 0 instruction + GATE 0 interrogative + GATE 1 interrogative; "upstream contamination path" named |
| Interrogative phrasing | None — gate items are declarative checkboxes | None — artifact-boundary format | None — phase-gate format | Partial — Phase 4B calibration note + Phase 5 review interrogatives | Full — every phase and gate includes a "why does this pass?" interrogative |
| Frontmatter keys | 6 (gate0–gate1–gate1b–gate2–gate3–gate4b) | 6 | 6 + explicit independence note in GATE 1B body | 6 + `inertia_framing: true` meta-key | 6 + `inertia_framing: true` + gate manifest table |
| C-30 inertia framing scope | Non-primary; Phase 0 instruction present | Non-primary; GATE 0 item present | Non-primary; Phase 0 instruction present | **Primary axis** — C-30 is the organizing principle of the entire variation | Combined axis — interrogative phrasing surfaces inertia reasoning at each gate |
| Challenge log path structure | Two columns (Path 1, Path 2) with Disposition | Annotation between Artifact 2 and Artifact 3 | Two columns (Path 1, Path 2) with Disposition | Two columns; Path 2 explicitly labeled "inertia — anchored to current behavior?" | Two columns; interrogative evidence required for "clean" dispositions |
| Role ownership | Explicit handoff rule: role may not attest own work | Role-to-artifact mapping | Role-to-phase mapping | Role-to-phase mapping with inertia-framing notes | Role-to-gate mapping in manifest table |
