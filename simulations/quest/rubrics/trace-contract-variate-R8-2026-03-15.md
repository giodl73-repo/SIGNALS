# trace-contract — Round 8 Variations (v8 Rubric, C-01–C-32, formula A/24×10)

**New criteria targeted:** C-31 (GATE 1 inertia clause uses two-clause confirmable form) and C-32 (Phase 1B challenge gate owned by different named role than Phase 1A author).

**Single-axis variations (V-01 to V-03):** Role Sequence, Output Format, Lifecycle Emphasis.
**Combination variations (V-04 to V-05):** Inertia Framing (single axis, depth play on C-31), Combined Full Integration.

---

## V-01 — Role Sequence

**Variation axis:** Role sequence — which named role owns each phase and gate, in what order, with explicit handoff instructions between them.

**Hypothesis:** When Phase 1A (expected construction) is owned by Expert and GATE 1B (challenge certification) is owned by Automate, neither role can self-certify both phases. C-32 emerges as a structural property of the template: role separation is enforced by ownership assignment, not by describing what a second reader might do. C-31 follows naturally — the inertia clause in GATE 1 adopts the same two-clause confirmable form as the actual-output isolation check, because both contamination paths are first-class gate items for the Expert-owned phase.

---

You are running **trace-contract** for Topic: `{Topic}`.

**Role assignment for this run:**

| Role | Identity | Phases Owned |
|------|----------|-------------|
| Expert | Connectors contract expert | Phase 0, Phase 1A, Phase 2, Phase 4, Phase 4B, Phase 5 |
| Automate | Connector automation specialist | Phase 1B, Phase 3 |

Role ownership is a structural constraint: the same role that builds a phase cannot certify the gate that validates it where role separation is listed.

**Frontmatter** — write at artifact top, update keys as each gate passes:

```yaml
---
topic: {Topic}
signal: contract
date: {date}
phase1a_author: Expert
gate1b_owner: Automate
gate0_scope_confirmed: false
gate1_isolation_confirmed: false
gate1b_challenge_confirmed: false
gate2_actual_complete: false
gate3_diff_complete: false
gate4b_calibration_confirmed: false
---
```

---

### Phase 0 — Scope Enumeration (Expert)

Enumerate all in-scope connector contract elements as a committed SCOPE MANIFEST before Phase 1A begins. Derive scope from the spec only — not from what you know the connector currently does. An expert who anchors element names to current connector behavior poisons the scope list before Phase 1A starts.

Required columns — no blank cells:

| # | Element Name | Element Type | Spec Clause Key |
|---|--------------|--------------|-----------------|
| | | schema-field \| auth-handshake \| action-payload \| trigger-payload \| error-shape \| metadata | |

**GATE 0** (Expert):
- [ ] SCOPE MANIFEST complete — `{N}` elements enumerated
- [ ] Element Type populated for every row — no blank cells
- [ ] Spec Clause Key populated for every row — no blank cells
- [ ] Scope derived from spec — current connector behavior excluded from element selection, not merely deprioritized — [CONFIRMED / NOT CONFIRMED]

Set `gate0_scope_confirmed: true`. **Phase 1A cannot begin until gate0_scope_confirmed = true.**

---

### Phase 1A — Expected Output: Skeleton then Values (Expert)

**Step 1 — Commit skeleton** (element names, types, spec clause keys — Expected Value column blank):

| Element | Element Type | Spec Clause | Expected Value |
|---------|--------------|-------------|----------------|
| (one row per Phase 0 element) | | | ← blank |

Record: `SKELETON COMMITTED — {N} rows`

**Step 2 — Fill expected values.** For each committed skeleton row, derive the Expected Value from spec only. Do not reference actual output. Do not reference what you know the connector currently does.

**GATE 1** (Expert signs off before handoff to Automate):
- [ ] All Expected Value cells filled — {N}/{N} rows complete
- [ ] No Spec Clause cells blank in expected table rows
- [ ] Actual output was not consulted during Phase 1A — not just ordered after, but not consulted at all — [CONFIRMED / NOT CONFIRMED]
- [ ] Expert runtime knowledge of current connector behavior was not used to constrain Expected Values — not just deprioritized, but excluded entirely — [CONFIRMED / NOT CONFIRMED]

Set `gate1_isolation_confirmed: true`. **Phase 1B cannot begin until gate1_isolation_confirmed = true.**

> **HANDOFF TO AUTOMATE.** Expert has signed off on Phase 1A and GATE 1. Automate owns Phase 1B and GATE 1B. Expert cannot certify GATE 1B.

---

### Phase 1B — Challenge Review (Automate)

Automate reviews each Phase 1A row for contamination signals. The question for each row: does the Expected Value appear to reflect what the connector currently returns, rather than what the spec defines?

CHALLENGE LOG:

| Row | Element | Contamination Signal? (Yes/No) | Basis | Disposition |
|-----|---------|-------------------------------|-------|-------------|

**GATE 1B** (Automate certifies — Expert cannot certify this gate):
- [ ] All `{N}` Phase 1A rows reviewed — no rows skipped
- [ ] Challenge log records Contamination Signal and Disposition for every row
- [ ] No unresolved contamination signals remain in the final expected table — [CONFIRMED / NOT CONFIRMED]

Set `gate1b_challenge_confirmed: true`. **Phase 2 cannot begin until gate1b_challenge_confirmed = true.**

> **HANDOFF TO EXPERT.** Automate has signed off on Phase 1B and GATE 1B. Expert owns Phase 2.

---

### Phase 2 — Actual Output (Expert)

Run the connector operation or observe actual connector behavior. Record actual output for each scope element. Add an Actual Value column to the Phase 1A table. Do not modify any Expected Value cell.

**GATE 2** (Expert):
- [ ] Actual Value recorded for all `{N}` scope elements — no blank cells
- [ ] No Expected Value cells modified during Phase 2

Set `gate2_actual_complete: true`.

> **HANDOFF TO AUTOMATE.** Expert has signed off on Phase 2. Automate owns Phase 3.

---

### Phase 3 — Diff and Classification (Automate)

Compare Expected Value vs. Actual Value for each row. Classify: MATCH | MISMATCH. For MISMATCH rows, assign Severity.

**Stop. Do not write root cause hypotheses here. Root causes go in Phase 4. Not here. Root cause text appearing in Phase 3 output is a GATE 3 failure condition.**

| Element | Element Type | Spec Clause | Expected Value | Actual Value | Match? | Severity |
|---------|--------------|-------------|----------------|--------------|--------|----------|

Severity values: breaking | degraded | cosmetic. Severity blank on any MISMATCH row = gate failure.

**GATE 3** (Automate):
- [ ] Every row classified MATCH or MISMATCH
- [ ] No Severity cells blank on MISMATCH rows
- [ ] No Spec Clause cells blank on any row
- [ ] No Element Type cells blank on any row
- [ ] No root cause hypotheses appear in Phase 3 output

Set `gate3_diff_complete: true`.

> **HANDOFF TO EXPERT.** Automate has signed off on Phase 3. Expert owns Phase 4, Phase 4B, and Phase 5.

---

### Phase 4 — Findings (Expert)

For each MISMATCH row, produce a finding scaffold:

```
F-{NN}: {Element Name}
  Severity:    {from Phase 3 — do not reassign here}
  Spec Ref:    {Spec Clause from Phase 3}
  Root Cause:  {connector-domain mechanism — field mapping | auth handshake | action payload shape | trigger payload schema | error response shape | metadata convention — "unknown" alone does not pass}
  Resolution:  {specific next step — names what to investigate; "investigate further" alone does not pass}
```

---

### Phase 4B — Calibration (Expert — standalone phase; do not merge with Phase 4)

Phase 4B is a separate phase. Do not write calibration inside Phase 4. A combined Phase 4 + calibration block does not pass GATE 4B.

**Severity tally** (count findings before writing assessments):

| Severity | Count |
|----------|-------|
| breaking | |
| degraded | |
| cosmetic | |

For each finding individually: justify its severity assignment. A single rationale covering all findings is a gate failure condition — group justification ("all breaking because inertia implies full replacement") is explicitly not accepted.

**GATE 4B** (Expert):
- [ ] Severity tally table completed before assessments written
- [ ] Each finding individually justified at its assigned severity level — group justification not accepted: [ ] each element individually justified at that level
- [ ] Distribution reasonable — at least two severity levels represented, or single level individually justified per finding

Set `gate4b_calibration_confirmed: true`. **Phase 5 cannot begin until gate4b_calibration_confirmed = true.**

---

### Phase 5 — CONTRACT DELTA (Expert)

List all spec amendments required. Priority is derived from Phase 4B calibrated severity — do not assign priority without Phase 4B completion.

| Finding | Spec Clause | Priority | Amendment Type | Required Change |
|---------|-------------|----------|----------------|-----------------|

- Priority: breaking→P1, degraded→P2, cosmetic→P3 (from Phase 4B). No blank Priority cells.
- Amendment Type required on every row: add-field \| remove-field \| change-type \| change-enum \| change-error-shape \| change-auth-flow. No blank Amendment Type cells.

---

---

## V-02 — Output Format

**Variation axis:** Output format — pre-specified table schemas, frontmatter key requirements, and confirmable checkpoint forms drive structural compliance; the format itself is the enforcement mechanism.

**Hypothesis:** Pre-printing column headers, a complete frontmatter key schema, and standardized `— [CONFIRMED / NOT CONFIRMED]` attestation slots in all gate items produces compliance as a parsing condition rather than instruction compliance. C-31 is natural: the inertia exclusion clause in GATE 1 gets the same two-clause checkbox form applied to every other gate item. C-32 is visible via the frontmatter `gate1b_owner` field — role separation is machine-readable.

---

You are running **trace-contract** for Topic: `{Topic}`.

Stock roles: Expert (Connectors contract expert), Automate (connector automation specialist). Expert constructs expected output (Phase 1A). Automate reviews for contamination (Phase 1B) and classifies the diff (Phase 3).

---

**Required frontmatter** — begin artifact with this block. Fill in gate key values as each gate passes. Do not omit any key.

```yaml
---
topic: {Topic}
signal: contract
date: {date}
phase1a_author: Expert
gate1b_owner: Automate
gate0_scope_confirmed: false
gate1_isolation_confirmed: false
gate1b_challenge_confirmed: false
gate2_actual_complete: false
gate3_diff_complete: false
gate4b_calibration_confirmed: false
---
```

---

**SCOPE MANIFEST** — Phase 0 output. All cells required; blank cells are a gate failure condition.

| # | Element Name | Element Type | Spec Clause Key |
|---|--------------|--------------|-----------------|
| | | schema-field \| auth-handshake \| action-payload \| trigger-payload \| error-shape \| metadata | |

GATE 0 — all items required before Phase 1A begins:
- [ ] `{N}` elements enumerated
- [ ] Element Type populated — no blank cells
- [ ] Spec Clause Key populated — no blank cells
- [ ] Scope anchored to spec only — current connector behavior was not used to select elements — not just consulted and set aside, but excluded entirely — [CONFIRMED / NOT CONFIRMED]

Update `gate0_scope_confirmed: true`.

---

**EXPECTED TABLE** — Phase 1A output. Two-step construction.

Step 1 — skeleton (fill Element Name, Element Type, Spec Clause; leave Expected Value blank):

| Element | Element Type | Spec Clause | Expected Value |
|---------|--------------|-------------|----------------|
| | schema-field \| auth-handshake \| action-payload \| trigger-payload \| error-shape \| metadata | | ← blank |

Record: `SKELETON COMMITTED — {N} rows`

Step 2 — fill Expected Value for each committed row from spec.

GATE 1 — all items required before Phase 1B begins:
- [ ] All Expected Value cells filled — {N}/{N} complete — no blank cells
- [ ] No Spec Clause cells blank in expected table rows
- [ ] Actual output not consulted — not just ordered after, but not consulted at all — [CONFIRMED / NOT CONFIRMED]
- [ ] Expert runtime knowledge of current connector behavior not applied — not just deprioritized, but excluded entirely — [CONFIRMED / NOT CONFIRMED]

Update `gate1_isolation_confirmed: true`.

---

**CHALLENGE LOG** — Phase 1B output. Owner: Automate (see frontmatter `gate1b_owner`). All columns required.

| Row | Element | Contamination Signal? (Yes/No) | Basis | Disposition |
|-----|---------|-------------------------------|-------|-------------|

GATE 1B — all items required before Phase 2 begins:
- [ ] All `{N}` rows reviewed — none skipped
- [ ] Contamination Signal and Disposition populated for every row — no blank cells
- [ ] No unresolved contamination signals in final expected table — [CONFIRMED / NOT CONFIRMED]

Update `gate1b_challenge_confirmed: true`.

---

**ACTUAL TABLE** — Phase 2 output. Add Actual Value column; do not modify Expected Values.

| Element | Element Type | Spec Clause | Expected Value | Actual Value |
|---------|--------------|-------------|----------------|--------------|

GATE 2:
- [ ] Actual Value populated for all `{N}` elements — no blank cells
- [ ] No Expected Value cells modified

Update `gate2_actual_complete: true`.

---

**DIFF TABLE** — Phase 3 output. Classification only — no root cause hypotheses. All columns required.

| Element | Element Type | Spec Clause | Expected Value | Actual Value | Match? | Severity |
|---------|--------------|-------------|----------------|--------------|--------|----------|

Match?: MATCH \| MISMATCH. Severity: breaking \| degraded \| cosmetic (MISMATCH rows only; blank = gate failure).

GATE 3:
- [ ] Every row classified MATCH or MISMATCH — no blank Match? cells
- [ ] No Severity cells blank on MISMATCH rows
- [ ] No Spec Clause cells blank on any row
- [ ] No Element Type cells blank on any row
- [ ] No root cause hypotheses in Phase 3 output — confirmed absent — [CONFIRMED / NOT CONFIRMED]

Update `gate3_diff_complete: true`.

---

**FINDING SCAFFOLDS** — Phase 4 output. One scaffold per MISMATCH row.

```
F-{NN}: {Element Name}
  Severity:    {from Phase 3 diff table — do not re-assign}
  Spec Ref:    {Spec Clause}
  Root Cause:  {domain mechanism — one of: field-mapping-delta | auth-handshake-mismatch | action-payload-drift | trigger-payload-gap | error-shape-change | metadata-convention-gap — "unknown" alone not accepted}
  Resolution:  {specific investigative step — not "investigate further" alone}
```

---

**CALIBRATION PHASE** — Phase 4B output. Separate section — do not merge with Phase 4 findings.

Severity tally table (required before calibration assessments):

| Severity | Count | Gate: Each Finding Individually Justified |
|----------|-------|------------------------------------------|
| breaking | | [ ] each finding individually justified at breaking |
| degraded | | [ ] each finding individually justified at degraded |
| cosmetic | | [ ] each finding individually justified at cosmetic |

Group justification ("all breaking because...") = gate failure. Each row in the tally requires an individual justification confirmation.

GATE 4B:
- [ ] Tally table populated — counts confirmed
- [ ] Individual justification box checked for each severity level present
- [ ] Distribution reasonable — at least two levels or single level individually justified

Update `gate4b_calibration_confirmed: true`.

---

**CONTRACT DELTA** — Phase 5 output. All columns required; blank Priority or Amendment Type cells are a gate failure condition.

| Finding | Spec Clause | Priority | Amendment Type | Required Change |
|---------|-------------|----------|----------------|-----------------|

Priority schema (from Phase 4B severity): breaking→P1, degraded→P2, cosmetic→P3.
Amendment Type vocabulary: add-field \| remove-field \| change-type \| change-enum \| change-error-shape \| change-auth-flow.

---

---

## V-03 — Lifecycle Emphasis

**Variation axis:** Lifecycle emphasis — sequential phase gates with blocking conditions; no phase can begin until the prior gate fires; STOP markers are structurally conspicuous.

**Hypothesis:** When every phase transition carries an explicit blocking guard ("STOP — cannot proceed until gate fires"), phase separation becomes a structural constraint rather than a formatting suggestion. C-31 is a gate checkpoint on the lifecycle spine — the inertia exclusion clause gets the same blocking authority as the actual-output isolation check because both appear as gate items on the same GATE 1 lifecycle node. C-32 appears as a lifecycle handoff rule at the Phase 1A → Phase 1B boundary.

---

You are running **trace-contract** for Topic: `{Topic}`.

Stock roles: Expert (Connectors contract expert), Automate (connector automation specialist).

**Phase dependency chain** — read before beginning. No phase begins until the gate before it fires.

| Phase | Name | Owner | Unblocked By |
|-------|------|-------|-------------|
| 0 | Scope Enumeration | Expert | Start of artifact |
| GATE 0 | Scope Gate | Expert | Phase 0 complete |
| 1A | Expected: Skeleton + Values | Expert | gate0_scope_confirmed = true |
| GATE 1 | Isolation Gate | Expert | Phase 1A complete |
| 1B | Challenge Review | **Automate** | gate1_isolation_confirmed = true |
| GATE 1B | Challenge Gate | **Automate** | Phase 1B complete |
| 2 | Actual Output | Expert | gate1b_challenge_confirmed = true |
| GATE 2 | Actual Gate | Expert | Phase 2 complete |
| 3 | Diff + Classification | Automate | gate2_actual_complete = true |
| GATE 3 | Diff Gate | Automate | Phase 3 complete |
| 4 | Findings | Expert | gate3_diff_complete = true |
| 4B | Calibration (standalone) | Expert | Phase 4 complete |
| GATE 4B | Calibration Gate | Expert | Phase 4B complete |
| 5 | CONTRACT DELTA | Expert | gate4b_calibration_confirmed = true |

**Frontmatter** — required at artifact top:

```yaml
---
topic: {Topic}
signal: contract
date: {date}
gate0_scope_confirmed: false
gate1_isolation_confirmed: false
gate1b_challenge_confirmed: false
gate2_actual_complete: false
gate3_diff_complete: false
gate4b_calibration_confirmed: false
---
```

---

### PHASE 0 — Scope Enumeration (Expert)

**CANNOT BEGIN UNTIL:** Start of artifact.

Enumerate all in-scope connector contract elements as a SCOPE MANIFEST. Derive scope from the spec — not from what you know the connector currently does.

| # | Element Name | Element Type | Spec Clause Key |
|---|--------------|--------------|-----------------|
| | | schema-field \| auth-handshake \| action-payload \| trigger-payload \| error-shape \| metadata | |

**━━━ STOP. Do not write GATE 0 until Phase 0 enumeration is complete. ━━━**

**GATE 0** (Expert):
- [ ] SCOPE MANIFEST complete — `{N}` elements committed
- [ ] Element Type populated — no blank cells
- [ ] Spec Clause Key populated — no blank cells
- [ ] Scope anchored to spec only — current connector behavior excluded from element selection — [CONFIRMED / NOT CONFIRMED]

Set `gate0_scope_confirmed: true`.

**━━━ STOP. Phase 1A cannot begin until gate0_scope_confirmed = true. ━━━**

---

### PHASE 1A — Expected Output (Expert)

**CANNOT BEGIN UNTIL:** gate0_scope_confirmed = true.

**Step 1 — Skeleton** (names, types, spec clauses; Expected Value column blank):

| Element | Element Type | Spec Clause | Expected Value |
|---------|--------------|-------------|----------------|
| (one row per Phase 0 SCOPE MANIFEST entry) | | | ← leave blank |

Record: `SKELETON COMMITTED — {N} rows`

**Step 2 — Fill Expected Values.** Derive each value from spec. Do not reference actual output. Do not reference what you know the connector currently does.

**━━━ STOP. Do not write GATE 1 until all Expected Values are filled. ━━━**

**GATE 1** (Expert):
- [ ] All Expected Value cells filled — {N}/{N} complete
- [ ] No Spec Clause cells blank in expected table rows
- [ ] Actual output not consulted during Phase 1A — not just ordered after, but not consulted at all — [CONFIRMED / NOT CONFIRMED]
- [ ] Expert runtime knowledge of current connector behavior not applied to expected values — not just deprioritized, but excluded entirely — [CONFIRMED / NOT CONFIRMED]

Set `gate1_isolation_confirmed: true`.

**━━━ STOP. Phase 1B cannot begin until gate1_isolation_confirmed = true. Phase 1B owner is Automate — not Expert. The same role that built Phase 1A cannot certify Phase 1B. ━━━**

---

### PHASE 1B — Challenge Review (Automate)

**CANNOT BEGIN UNTIL:** gate1_isolation_confirmed = true. **Owner: Automate.** Expert built Phase 1A; Automate must own Phase 1B. This role separation is a structural requirement, not a suggestion.

Review each Phase 1A row. For each row: does the Expected Value appear anchored to current connector behavior rather than to spec derivation?

CHALLENGE LOG:

| Row | Element | Contamination Signal? (Yes/No) | Basis | Disposition |
|-----|---------|-------------------------------|-------|-------------|

**━━━ STOP. Do not write GATE 1B until all rows reviewed. ━━━**

**GATE 1B** (Automate certifies — Expert cannot certify this gate):
- [ ] All `{N}` Phase 1A rows reviewed — none skipped
- [ ] Disposition recorded for every row
- [ ] No unresolved contamination signals in the final expected table — [CONFIRMED / NOT CONFIRMED]

Set `gate1b_challenge_confirmed: true`.

**━━━ STOP. Phase 2 cannot begin until gate1b_challenge_confirmed = true. ━━━**

---

### PHASE 2 — Actual Output (Expert)

**CANNOT BEGIN UNTIL:** gate1b_challenge_confirmed = true.

Run the connector operation. Record actual output for each scope element. Add Actual Value column. Do not modify Expected Values.

**GATE 2** (Expert):
- [ ] Actual Value recorded for all `{N}` elements — no blank cells
- [ ] No Expected Value cells modified

Set `gate2_actual_complete: true`.

**━━━ STOP. Phase 3 cannot begin until gate2_actual_complete = true. ━━━**

---

### PHASE 3 — Diff and Classification (Automate)

**CANNOT BEGIN UNTIL:** gate2_actual_complete = true.

Classify each row: MATCH | MISMATCH. For MISMATCH rows: assign Severity (breaking | degraded | cosmetic).

**━━━ STOP. Do not write root cause hypotheses in Phase 3. Root causes are Phase 4. Root cause text in Phase 3 output = immediate GATE 3 failure. ━━━**

| Element | Element Type | Spec Clause | Expected Value | Actual Value | Match? | Severity |
|---------|--------------|-------------|----------------|--------------|--------|----------|

**GATE 3** (Automate):
- [ ] Every row classified MATCH or MISMATCH
- [ ] No Severity cells blank on MISMATCH rows
- [ ] No Spec Clause cells blank on any row
- [ ] No Element Type cells blank on any row
- [ ] No root cause hypotheses in Phase 3 output

Set `gate3_diff_complete: true`.

**━━━ STOP. Phase 4 cannot begin until gate3_diff_complete = true. ━━━**

---

### PHASE 4 — Findings (Expert)

**CANNOT BEGIN UNTIL:** gate3_diff_complete = true.

For each MISMATCH, produce a finding scaffold:

```
F-{NN}: {Element Name}
  Severity:    {from Phase 3}
  Spec Ref:    {Spec Clause}
  Root Cause:  {connector mechanism — field-mapping | auth-handshake | action-payload | trigger-payload | error-shape | metadata — "unknown" alone not accepted}
  Resolution:  {specific next step — names what to investigate}
```

**━━━ STOP. Phase 4B is a separate, standalone phase. Do not begin calibration inside Phase 4. Do not proceed to Phase 4B until all Phase 4 findings are written. ━━━**

---

### PHASE 4B — Calibration (Expert — standalone phase; do not merge with Phase 4)

**CANNOT BEGIN UNTIL:** Phase 4 findings complete. **CONTRACT DELTA cannot begin until GATE 4B fires.**

Severity tally (count before assessing):

| Severity | Count |
|----------|-------|
| breaking | |
| degraded | |
| cosmetic | |

For each finding individually: justify its severity. A group rationale covering all findings is a gate failure condition.

**━━━ STOP. Do not write GATE 4B until individual justifications are written for every finding. ━━━**

**GATE 4B** (Expert):
- [ ] Severity tally table completed before assessments
- [ ] Each finding individually justified at its assigned level — [ ] each element individually justified at that level
- [ ] Distribution is reasonable — not all one level unless individually justified

Set `gate4b_calibration_confirmed: true`.

**━━━ STOP. Phase 5 cannot begin until gate4b_calibration_confirmed = true. ━━━**

---

### PHASE 5 — CONTRACT DELTA (Expert)

**CANNOT BEGIN UNTIL:** gate4b_calibration_confirmed = true.

| Finding | Spec Clause | Priority | Amendment Type | Required Change |
|---------|-------------|----------|----------------|-----------------|

Priority derived from Phase 4B calibrated severity: breaking→P1, degraded→P2, cosmetic→P3. Blank Priority cells not accepted.
Amendment Type required: add-field \| remove-field \| change-type \| change-enum \| change-error-shape \| change-auth-flow. Blank Amendment Type cells not accepted.

---

---

## V-04 — Inertia Framing

**Variation axis:** Inertia framing — the status-quo competitor is named at the top, and every contamination barrier is explained in terms of the specific inertia risk it closes.

**Hypothesis:** Fronting the skill body with the inertia framing ("what the connector currently does is the real alternative") makes the contamination barriers explanatorily coherent — the reader understands WHY each isolation check exists. C-31 is the primary target: the inertia exclusion clause in GATE 1 adopts the full two-clause confirmable form because inertia contamination is the conceptual center of the prompt, not a footnote. C-30 (Phase 0 inertia exclusion) and C-23 (GATE 1 inertia clause) are prominent; C-31 upgrades C-23 to the confirmable form naturally.

---

You are running **trace-contract** for Topic: `{Topic}`.

**The inertia problem.** The expected table you are about to build is a claim that the spec — not the connector's current runtime behavior — defines what the connector should do. This claim is only valid if the expected values are derived from the spec alone. The connector's current behavior is the inertia competitor: it is already deployed, already integrated, and it pulls expected-value derivation toward what-is rather than what-should-be. There are two distinct entry points where inertia can contaminate the expected table:

1. **Scope anchoring** (Phase 0): An expert anchors the scope to elements the connector currently exposes, omitting spec-defined elements the connector does not yet implement.
2. **Value anchoring** (Phase 1A): An expert anchors expected values to what the connector currently returns, writing "expected" values that match actual output and silencing the diff.

A third contamination path exists even when both anchoring paths are closed:
3. **Residual contamination** (Phase 1B): Contamination that the author cannot detect in their own work. A second-reader challenge log closes this path.

Each phase below explicitly closes one contamination entry point. The inertia framing inside each gate is not decorative — it names the specific risk each check targets.

Stock roles: Expert (Connectors contract expert), Automate (connector automation specialist). Automate owns Phase 1B and GATE 1B to enforce second-reader independence.

**Frontmatter:**

```yaml
---
topic: {Topic}
signal: contract
date: {date}
inertia_framing: true
phase1a_author: Expert
gate1b_owner: Automate
gate0_scope_confirmed: false
gate1_isolation_confirmed: false
gate1b_challenge_confirmed: false
gate2_actual_complete: false
gate3_diff_complete: false
gate4b_calibration_confirmed: false
---
```

---

### Phase 0 — Scope Enumeration (Inertia layer: scope anchoring)

**Inertia risk:** An expert who has worked with this connector will instinctively enumerate elements by what the connector currently exposes. Spec-defined elements that the connector does not yet implement are invisible from a runtime perspective but are in scope from a contract perspective. Anchor scope to the spec — not to the connector.

Enumerate all in-scope elements as a SCOPE MANIFEST:

| # | Element Name | Element Type | Spec Clause Key |
|---|--------------|--------------|-----------------|
| | | schema-field \| auth-handshake \| action-payload \| trigger-payload \| error-shape \| metadata | |

**GATE 0** — Inertia closure at scope layer:
- [ ] SCOPE MANIFEST complete — `{N}` elements enumerated from spec
- [ ] Element Type populated — no blank cells
- [ ] Spec Clause Key populated — no blank cells
- [ ] Scope derived from spec — current connector behavior was not used to anchor element names or select elements — not just consulted and discarded, but excluded from scope derivation entirely — [CONFIRMED / NOT CONFIRMED]

Set `gate0_scope_confirmed: true`.

---

### Phase 1A — Expected Output (Inertia layer: value anchoring)

**Inertia risk:** Even with a clean scope, an expert may anchor Expected Values to what the connector currently returns — writing "expected" values that describe current behavior rather than the spec contract. This is the most dangerous contamination form: it is invisible in the expected table but silences the diff entirely for affected elements.

**Step 1 — Commit skeleton** (names, types, spec clauses — Expected Value blank):

| Element | Element Type | Spec Clause | Expected Value |
|---------|--------------|-------------|----------------|
| (one row per Phase 0 SCOPE MANIFEST entry) | | | ← blank |

Record: `SKELETON COMMITTED — {N} rows`

**Step 2 — Fill Expected Values** from spec. The spec is the contract. The connector's current behavior is not evidence for expected value derivation.

**GATE 1** — Inertia closure at value layer. Two contamination paths; each uses two-clause confirmable form:
- [ ] All Expected Value cells filled — {N}/{N} complete
- [ ] No Spec Clause cells blank in expected table rows
- [ ] Actual output not consulted — not just ordered after, but not consulted at all — [CONFIRMED / NOT CONFIRMED]
- [ ] Expert runtime knowledge of current connector behavior not used to constrain Expected Values — not just deprioritized after consideration, but excluded entirely from expected value derivation — [CONFIRMED / NOT CONFIRMED]

Set `gate1_isolation_confirmed: true`.

---

### Phase 1B — Challenge Review (Inertia layer: residual contamination; owner: Automate)

**Inertia risk:** The Phase 1A author cannot reliably detect their own inertia contamination — the contamination is invisible to the person who introduced it. A second reader who did not build Phase 1A reviews each row with the contamination question in mind: does this Expected Value appear to describe what the connector currently does, rather than what the spec defines?

Owner: Automate. Expert owns Phase 1A; Automate owns Phase 1B. The same role cannot certify both phases.

CHALLENGE LOG:

| Row | Element | Inertia Signal? (Yes/No) | Basis | Disposition |
|-----|---------|--------------------------|-------|-------------|

**GATE 1B** (Automate certifies — Expert cannot certify this gate):
- [ ] All `{N}` Phase 1A rows reviewed
- [ ] Inertia Signal and Disposition recorded for every row
- [ ] No residual inertia contamination in the final expected table — [CONFIRMED / NOT CONFIRMED]

Set `gate1b_challenge_confirmed: true`.

---

### Phase 2 — Actual Output

Run the connector operation. Record actual output for each scope element. Add Actual Value column. Do not modify Expected Values.

**GATE 2:**
- [ ] Actual Value recorded for all `{N}` elements
- [ ] No Expected Value cells modified

Set `gate2_actual_complete: true`.

---

### Phase 3 — Diff and Classification

Compare Expected vs. Actual. Classify: MATCH | MISMATCH. For MISMATCH rows: assign Severity (breaking | degraded | cosmetic).

**Inertia note on diff results:** If the inertia barriers worked, you will see mismatches where the spec evolved but the connector did not follow. These are often breaking. Resist the impulse to relabel them as "cosmetic" because the connector is widely deployed — severity is a spec-contract assessment, not a deployment impact assessment. Severity re-assessment belongs in Phase 4B calibration.

Do not write root cause hypotheses in Phase 3. Classification only.

| Element | Element Type | Spec Clause | Expected Value | Actual Value | Match? | Severity |
|---------|--------------|-------------|----------------|--------------|--------|----------|

**GATE 3:**
- [ ] Every row classified MATCH or MISMATCH
- [ ] No Severity cells blank on MISMATCH rows
- [ ] No Spec Clause cells blank
- [ ] No Element Type cells blank
- [ ] No root cause hypotheses in Phase 3 output

Set `gate3_diff_complete: true`.

---

### Phase 4 — Findings

For each MISMATCH, produce a finding scaffold:

```
F-{NN}: {Element Name}
  Severity:    {from Phase 3}
  Spec Ref:    {Spec Clause}
  Root Cause:  {connector mechanism — field-mapping-delta | auth-protocol-mismatch | action-payload-drift | trigger-payload-gap | error-shape-change | metadata-convention-gap | inertia-spec-drift (connector not updated to follow spec change)}
  Resolution:  {specific next step — names clause, version, or integration point to investigate}
```

"Inertia-spec-drift" is a valid root cause when the connector was not updated to follow a known spec change. Name the specific spec clause and the connector version where the gap was introduced.

---

### Phase 4B — Calibration (standalone — do not merge with Phase 4)

**Inertia note on calibration:** Breaking mismatches driven by inertia-spec-drift are correctly assigned breaking severity — but each must be individually justified by its specific spec clause gap, not by a group claim ("all breaking because inertia implies full replacement"). Different spec elements may have different severity even when all are caused by inertia.

Severity tally:

| Severity | Count |
|----------|-------|
| breaking | |
| degraded | |
| cosmetic | |

For each finding individually: justify its severity. Group justification = gate failure condition.

**GATE 4B:**
- [ ] Severity tally completed
- [ ] Each finding individually justified — not grouped by root-cause category — [ ] each element individually justified at that level
- [ ] Distribution reasonable

Set `gate4b_calibration_confirmed: true`.

---

### Phase 5 — CONTRACT DELTA

| Finding | Spec Clause | Priority | Amendment Type | Required Change |
|---------|-------------|----------|----------------|-----------------|

Priority from Phase 4B: breaking→P1, degraded→P2, cosmetic→P3. Blank Priority cells not accepted.
Amendment Type required: add-field \| remove-field \| change-type \| change-enum \| change-error-shape \| change-auth-flow.

**Inertia pattern in delta:** Amendments that correct inertia-spec-drift (usually breaking, P1) should be grouped together — these represent spec evolution the connector has not followed, and they form a coherent remediation batch distinct from schema-only corrections.

---

---

## V-05 — Combined Full Integration

**Variation axes:** Role Sequence + Output Format + Lifecycle Emphasis + Inertia Framing — all four axes present.

**Hypothesis:** The cumulative structural coverage of all four single-axis patterns produces a prompt body where every criterion from C-09 to C-32 is either directly enforced by a named gate item or structurally implied by the template design. No criterion requires prose-only compliance or relies on the agent's good faith.

---

You are running **trace-contract** for Topic: `{Topic}`.

**The inertia problem.** The expected table you are about to build is a claim about the spec contract — not about the connector's current runtime behavior. Inertia contamination (anchoring expected values to what the connector currently does) silences the diff and defeats the exercise. Three contamination entry points exist: scope anchoring (Phase 0), value anchoring (Phase 1A), and residual contamination detectable only by a second reader (Phase 1B). Each phase below closes one entry point. The inertia framing inside each gate is not decorative.

**Role assignment:**

| Role | Identity | Phases Owned |
|------|----------|-------------|
| Expert | Connectors contract expert | Phase 0, Phase 1A, Phase 2, Phase 4, Phase 4B, Phase 5 |
| Automate | Connector automation specialist | Phase 1B (GATE 1B), Phase 3 |

Expert cannot certify GATE 1B. Automate cannot certify GATE 1. Role separation is structurally enforced — it is not operationally optional.

**Phase dependency chain** — no phase begins until the gate before it fires:

| Phase | Owner | Unblocked By | Gate Key Set |
|-------|-------|-------------|-------------|
| 0 Scope Enumeration | Expert | Start | gate0_scope_confirmed |
| 1A Expected Output | Expert | gate0_scope_confirmed = true | gate1_isolation_confirmed |
| 1B Challenge Review | **Automate** | gate1_isolation_confirmed = true | gate1b_challenge_confirmed |
| 2 Actual Output | Expert | gate1b_challenge_confirmed = true | gate2_actual_complete |
| 3 Diff + Classification | Automate | gate2_actual_complete = true | gate3_diff_complete |
| 4 Findings | Expert | gate3_diff_complete = true | — |
| 4B Calibration | Expert | Phase 4 complete | gate4b_calibration_confirmed |
| 5 CONTRACT DELTA | Expert | gate4b_calibration_confirmed = true | — |

**Required frontmatter** — all keys required; no keys may be omitted:

```yaml
---
topic: {Topic}
signal: contract
date: {date}
inertia_framing: true
phase1a_author: Expert
gate1b_owner: Automate
gate0_scope_confirmed: false
gate1_isolation_confirmed: false
gate1b_challenge_confirmed: false
gate2_actual_complete: false
gate3_diff_complete: false
gate4b_calibration_confirmed: false
---
```

---

### PHASE 0 — Scope Enumeration (Expert)

**━━━ CANNOT BEGIN UNTIL: Start of artifact. ━━━**

**Inertia risk:** An expert anchors element names to what the connector currently exposes, omitting spec-defined elements the connector has not yet implemented.

Enumerate all in-scope elements as a SCOPE MANIFEST. Derive scope from spec only. All columns required — blank cells are a gate failure condition.

| # | Element Name | Element Type | Spec Clause Key |
|---|--------------|--------------|-----------------|
| | | schema-field \| auth-handshake \| action-payload \| trigger-payload \| error-shape \| metadata | |

**━━━ STOP. Do not write GATE 0 until Phase 0 enumeration is complete. ━━━**

**GATE 0** (Expert):
- [ ] SCOPE MANIFEST complete — `{N}` elements enumerated
- [ ] Element Type populated — no blank cells
- [ ] Spec Clause Key populated — no blank cells
- [ ] Scope derived from spec — current connector behavior excluded from element selection — not just deprioritized, but excluded from scope derivation entirely — [CONFIRMED / NOT CONFIRMED]

Set `gate0_scope_confirmed: true`.

**━━━ STOP. Phase 1A cannot begin until gate0_scope_confirmed = true. ━━━**

---

### PHASE 1A — Expected Output (Expert)

**━━━ CANNOT BEGIN UNTIL: gate0_scope_confirmed = true. ━━━**

**Inertia risk:** Expert anchors Expected Values to what the connector currently returns, writing expected values that describe current behavior rather than the spec contract.

**Step 1 — Commit skeleton** (names, types, spec clauses — Expected Value blank):

| Element | Element Type | Spec Clause | Expected Value |
|---------|--------------|-------------|----------------|
| (one row per SCOPE MANIFEST entry) | | | ← leave blank |

Record: `SKELETON COMMITTED — {N} rows`

**Step 2 — Fill Expected Values** from spec. The spec is the contract. Do not reference actual output. Do not reference what you know the connector currently does.

**━━━ STOP. Do not write GATE 1 until all Expected Values are filled. ━━━**

**GATE 1** (Expert):
- [ ] All Expected Value cells filled — {N}/{N} complete — no blank cells
- [ ] No Spec Clause cells blank in expected table rows
- [ ] Actual output not consulted during Phase 1A — not just ordered after, but not consulted at all — [CONFIRMED / NOT CONFIRMED]
- [ ] Expert runtime knowledge of current connector behavior not applied to Expected Values — not just deprioritized after consideration, but excluded entirely from expected value derivation — [CONFIRMED / NOT CONFIRMED]

Set `gate1_isolation_confirmed: true`.

**━━━ STOP. Phase 1B cannot begin until gate1_isolation_confirmed = true. Phase 1B owner is Automate — not Expert. Role separation is a structural requirement: the same role that built Phase 1A cannot certify GATE 1B. ━━━**

---

### PHASE 1B — Challenge Review (Automate)

**━━━ CANNOT BEGIN UNTIL: gate1_isolation_confirmed = true. OWNER: AUTOMATE. Expert cannot run or certify this phase. ━━━**

**Inertia risk:** The Phase 1A author cannot reliably detect their own inertia contamination. Automate reviews each row with the contamination question front of mind.

For each Phase 1A row: does the Expected Value appear to describe current connector behavior rather than spec-derived contract expectations?

CHALLENGE LOG — all columns required:

| Row | Element | Inertia Signal? (Yes/No) | Basis | Disposition |
|-----|---------|--------------------------|-------|-------------|

**━━━ STOP. Do not write GATE 1B until all rows reviewed. ━━━**

**GATE 1B** (Automate certifies — Expert cannot certify this gate):
- [ ] All `{N}` Phase 1A rows reviewed — none skipped
- [ ] Inertia Signal and Disposition recorded for every row — no blank cells
- [ ] No residual inertia contamination in the final expected table — [CONFIRMED / NOT CONFIRMED]

Set `gate1b_challenge_confirmed: true`.

**━━━ STOP. Phase 2 cannot begin until gate1b_challenge_confirmed = true. ━━━**

---

### PHASE 2 — Actual Output (Expert)

**━━━ CANNOT BEGIN UNTIL: gate1b_challenge_confirmed = true. ━━━**

Run the connector operation. Record actual output for each scope element. Add Actual Value column. Do not modify Expected Values.

| Element | Element Type | Spec Clause | Expected Value | Actual Value |
|---------|--------------|-------------|----------------|--------------|

**GATE 2** (Expert):
- [ ] Actual Value recorded for all `{N}` elements — no blank cells
- [ ] No Expected Value cells modified

Set `gate2_actual_complete: true`.

**━━━ STOP. Phase 3 cannot begin until gate2_actual_complete = true. ━━━**

---

### PHASE 3 — Diff and Classification (Automate)

**━━━ CANNOT BEGIN UNTIL: gate2_actual_complete = true. ━━━**

Classify each row: MATCH | MISMATCH. For MISMATCH rows: assign Severity (breaking | degraded | cosmetic).

**━━━ STOP. Do not write root cause hypotheses in Phase 3. Root causes belong in Phase 4. Root cause text in Phase 3 output = immediate GATE 3 failure condition. ━━━**

| Element | Element Type | Spec Clause | Expected Value | Actual Value | Match? | Severity |
|---------|--------------|-------------|----------------|--------------|--------|----------|

**GATE 3** (Automate):
- [ ] Every row classified MATCH or MISMATCH — no blank Match? cells
- [ ] No Severity cells blank on MISMATCH rows
- [ ] No Spec Clause cells blank on any row
- [ ] No Element Type cells blank on any row
- [ ] No root cause hypotheses in Phase 3 output — confirmed absent — [CONFIRMED / NOT CONFIRMED]

Set `gate3_diff_complete: true`.

**━━━ STOP. Phase 4 cannot begin until gate3_diff_complete = true. ━━━**

---

### PHASE 4 — Findings (Expert)

**━━━ CANNOT BEGIN UNTIL: gate3_diff_complete = true. ━━━**

For each MISMATCH row, produce a finding scaffold:

```
F-{NN}: {Element Name}
  Severity:    {from Phase 3 — do not reassign here}
  Spec Ref:    {Spec Clause}
  Root Cause:  {connector mechanism — field-mapping-delta | auth-handshake-mismatch | action-payload-drift | trigger-payload-gap | error-shape-change | metadata-convention-gap | inertia-spec-drift — "unknown" alone not accepted}
  Resolution:  {specific investigative step — names what to investigate; "investigate further" alone not accepted}
```

"Inertia-spec-drift" is a valid root cause when the connector was not updated to follow a known spec change. Name the specific clause and connector version where the gap was introduced.

**━━━ STOP. Phase 4B is a standalone phase separate from Phase 4. Do not merge calibration into Phase 4. Do not begin Phase 4B until all Phase 4 findings are written. ━━━**

---

### PHASE 4B — Calibration (Expert — standalone phase; do not merge with Phase 4)

**━━━ CANNOT BEGIN UNTIL: Phase 4 findings complete. Phase 5 cannot begin until gate4b_calibration_confirmed = true. ━━━**

**Severity tally** (complete before writing any calibration assessment):

| Severity | Count |
|----------|-------|
| breaking | |
| degraded | |
| cosmetic | |

For each finding individually: justify its severity assignment. Group justification ("all breaking because inertia implies full replacement") = gate failure condition. Each element may have a different inertia magnitude; justify each independently.

**GATE 4B** (Expert):
- [ ] Severity tally table completed before assessments
- [ ] Each finding individually justified at its assigned severity level — group justification not accepted: [ ] each element individually justified at that level
- [ ] Distribution reasonable — at least two severity levels represented, or single level individually justified per finding

Set `gate4b_calibration_confirmed: true`.

**━━━ STOP. Phase 5 cannot begin until gate4b_calibration_confirmed = true. ━━━**

---

### PHASE 5 — CONTRACT DELTA (Expert)

**━━━ CANNOT BEGIN UNTIL: gate4b_calibration_confirmed = true. ━━━**

Priority is derived from Phase 4B calibrated severity. Do not assign priority without Phase 4B completion. All columns required — blank Priority or Amendment Type cells are not accepted.

| Finding | Spec Clause | Priority | Amendment Type | Required Change |
|---------|-------------|----------|----------------|-----------------|

- Priority: breaking→P1, degraded→P2, cosmetic→P3
- Amendment Type: add-field \| remove-field \| change-type \| change-enum \| change-error-shape \| change-auth-flow

**Inertia pattern in delta:** Amendments correcting inertia-spec-drift (typically breaking, P1) form a coherent remediation batch. Group them by amendment type within the P1 tier — they represent spec evolution the connector has not followed and are blocked for downstream integrations relying on the contract as specified.
