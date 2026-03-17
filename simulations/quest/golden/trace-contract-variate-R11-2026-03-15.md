# trace-contract Variate — Round 11
**Date:** 2026-03-15
**Rubric:** v11 (C-01–C-39, denominator /31)
**Baseline:** R10 V-05 = 27.5/31 (C-35 FAIL, C-36 FAIL; C-17 PASS, C-37 PASS, C-38 PASS, C-39 PASS)
**Target criteria:** C-35 (Phase Dependency Reference Table), C-36 (Named Inertia Correction Route Table)

---

## Round 11 Variation Map

| Variation | Axis | C-35 | C-36 | Notes |
|-----------|------|------|------|-------|
| V-01 | Standalone Phase Dependency Reference Table (C-35) | PASS | FAIL | Single-axis: `## Phase Dependency Reference Table` as distinct section upstream of Phase 0; per-phase headers cross-reference it; inline dependency chain retained as supplementary |
| V-02 | Named Inertia Correction Route Table (C-36) | FAIL | PASS | Single-axis: `## INERTIA CORRECTION ROUTES` as dedicated section before Phase 4; ROUTE-A/ROUTE-B with full arrow-notation paths; CASCADE GATE references routes by name |
| V-03 | Role-Owned Schema Confirmation Gate (C-35 alternative) | PASS | FAIL | Single-axis: Automate certifies `SCHEMA GATE` before Phase 0; Phase Dependency Reference Table is a gated role artifact, not a passive preamble; Expert blocked until SCHEMA GATE closes |
| V-04 | Top-Positioned Route Table (C-36 alternative) | FAIL | PASS | Single-axis: INERTIA CORRECTION ROUTES relocated to top-level position immediately after role table, before all phase content; framed as direct response to three contamination vectors |
| V-05 | Combined (Platinum Target: 31/31) | PASS | PASS | V-01 C-35 mechanism + V-02 C-36 mechanism + full R10 V-05 base architecture; expected 31/31 |

---

## V-01 — Standalone Phase Dependency Reference Table

**Axis:** Lifecycle emphasis — global execution schema upstream of all phase content

**Hypothesis:** R10 V-05 (27.5/31) fails C-35 because it has no standalone reference table mapping every phase to its "Unblocked By" gate prerequisite as a structurally independent section upstream of all phase bodies. The inline phase dependency chain is interleaved with cascade routing rows, mixing two concerns in one table. C-35 requires a standalone, upstream table whose sole purpose is global phase-ordering visibility — a reader consulting it before Phase 0 knows the complete execution schema without entering any phase body. V-01 adds `## Phase Dependency Reference Table` as a dedicated section after the role assignment table, before any phase content. The table lists every phase and gate entry with an "Unblocked By" column populated with the specific prior gate key. A note states the table is the global execution schema; per-phase "CANNOT BEGIN UNTIL" declarations remain as local enforcement and are explicitly complementary (not redundant). Every phase header includes a cross-reference line ("Per Phase Dependency Reference Table: Phase X — Unblocked By: [gate key]") tying the local declaration to the global schema. C-36 is not addressed — CASCADE GATE inline labels remain the sole route reference. Expected: C-35 PASS, C-36 FAIL.

---

You are running **trace-contract** for Topic: `{Topic}`.

**The inertia problem.** The expected table you are about to build is a claim about the spec contract — not about the connector's current runtime behavior. Inertia contamination (anchoring expected values to what the connector currently does) silences the diff and defeats the exercise. Three contamination entry points exist: scope anchoring (Phase 0), value anchoring (Phase 1A), and residual contamination detectable only by a second reader with an INERTIA REGISTER (Phase 1B). Each phase closes one entry point.

**Role assignment:**

| Role | Identity | Phases Owned | May NOT perform |
|------|----------|-------------|-----------------|
| Expert | Connectors contract expert | Phase 0, Phase 1A, Phase 2, Phase 4, CASCADE GATE, Phase 4B, Phase 5 | Phase 1B certification; GATE 1B certification |
| Automate | Connector automation specialist | Phase 1B, GATE 1B-TM, GATE 1B, Phase 3 | Phase 1A derivation; GATE 1 certification |

Role separation is structurally enforced. An agent who owns Phase 1A may not certify GATE 1B.

---

## Phase Dependency Reference Table

This table is the global execution schema. Read it before beginning Phase 0. A reader consulting only this table knows the complete phase ordering before entering any phase body. This table is standalone — it does not substitute for the "CANNOT BEGIN UNTIL:" declarations within each phase section, which enforce the constraint at the moment of execution. Both are required.

| Phase | Name | Unblocked By |
|-------|------|-------------|
| Phase 0 | Scope Enumeration | Start of artifact (no prior gate required) |
| GATE 0 | Scope Gate | Phase 0 enumeration complete |
| Phase 1A | Expected Output | gate0_scope_confirmed = true |
| GATE 1 | Isolation Gate | Phase 1A fill complete |
| Phase 1B | INERTIA REGISTER | gate1_isolation_confirmed = true |
| GATE 1B-TM | Per-Type Verification | Phase 1B CHALLENGE LOG complete for all rows |
| GATE 1B | Challenge Gate | GATE 1B-TM complete — all three type blocks present |
| Phase 2 | Actual Output | gate1b_challenge_confirmed = true |
| GATE 2 | Actual Gate | Phase 2 fill complete |
| Phase 3 | Diff + Classification | gate2_actual_complete = true |
| GATE 3 | Diff Gate | Phase 3 classification complete |
| Phase 4 | Findings | gate3_diff_complete = true |
| CASCADE GATE | Cascade Gate | Phase 4 findings complete |
| Phase 4B | Calibration | Phase 4 complete AND CASCADE GATE complete |
| GATE 4B | Calibration Gate | Phase 4B complete |
| Phase 5 | CONTRACT DELTA | gate4b_calibration_confirmed = true |

---

**Phase dependency chain (with cascade routing):**

| Phase | Name | Owner | Unblocked By | Gate Key Set | Must NOT Visit |
|-------|------|-------|-------------|-------------|----------------|
| 0 | Scope Enumeration | Expert | Start | gate0_scope_confirmed | — |
| GATE 0 | Scope Gate | Expert | Phase 0 complete | — | — |
| 1A | Expected Output | Expert | gate0_scope_confirmed = true | gate1_isolation_confirmed | — |
| GATE 1 | Isolation Gate | Expert | Phase 1A complete | — | — |
| 1B | INERTIA REGISTER | **Automate** | gate1_isolation_confirmed = true | (-> GATE 1B-TM) | — |
| GATE 1B-TM | Per-Type Verification | **Automate** | Phase 1B complete | — | — |
| GATE 1B | Challenge Gate | **Automate** | GATE 1B-TM complete | gate1b_challenge_confirmed | — |
| 2 | Actual Output | Expert | gate1b_challenge_confirmed = true | gate2_actual_complete | — |
| GATE 2 | Actual Gate | Expert | Phase 2 complete | — | — |
| 3 | Diff + Classification | Automate | gate2_actual_complete = true | gate3_diff_complete | — |
| GATE 3 | Diff Gate | Automate | Phase 3 complete | — | — |
| 4 | Findings | Expert | gate3_diff_complete = true | — | — |
| CASCADE GATE | Cascade Gate | Expert | All findings assigned | — | — |
| 4B | Calibration | Expert | Phase 4 + CASCADE GATE | gate4b_calibration_confirmed | — |
| GATE 4B | Calibration Gate | Expert | Phase 4B complete | — | — |
| 5 | CONTRACT DELTA | Expert | gate4b_calibration_confirmed = true | — | — |

**Required frontmatter** — all keys required:

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

**CANNOT BEGIN UNTIL: Start of artifact. (Per Phase Dependency Reference Table: Phase 0 — Unblocked By: Start of artifact.)**

**Inertia risk:** Expert anchors element names to what the connector currently exposes, omitting spec-defined elements the connector has not yet implemented.

Ask first: What connector contract elements does the spec define for `{Topic}` — not what the connector currently exposes, but what the spec says should be there?

Enumerate all in-scope elements as a SCOPE MANIFEST. Derive scope from spec only. All columns required.

| # | Element Name | Element Type | Spec Clause Key |
|---|--------------|--------------|-----------------|
| | | schema-field \| auth-handshake \| action-payload \| trigger-payload \| error-shape \| metadata | |

**STOP. Do not write GATE 0 until Phase 0 enumeration is complete.**

**GATE 0** (Expert):
- [ ] SCOPE MANIFEST complete — `{N}` elements enumerated
- [ ] Element Type populated — no blank cells
- [ ] Spec Clause Key populated — no blank cells
- [ ] Scope derived from spec — current connector behavior excluded — [CONFIRMED / NOT CONFIRMED]

Set `gate0_scope_confirmed: true`.

**STOP. Phase 1A cannot begin until gate0_scope_confirmed = true.**

---

### PHASE 1A — Expected Output (Expert)

**CANNOT BEGIN UNTIL: gate0_scope_confirmed = true. (Per Phase Dependency Reference Table: Phase 1A — Unblocked By: gate0_scope_confirmed = true.)**

**Inertia risk:** Expert anchors Expected Values to what the connector currently returns, writing "expected" values that describe current behavior rather than the spec contract.

Ask first: For each scope element, what does the spec say the expected value should be — stated as a spec-derivable claim, not as a description of what the connector currently returns?

**Step 1 — Commit skeleton** (names, types, spec clauses — Expected Value column blank):

| Element | Element Type | Spec Clause | Expected Value |
|---------|--------------|-------------|----------------|
| (one row per SCOPE MANIFEST entry) | | | <- leave blank |

Record: `SKELETON COMMITTED — {N} rows`

**Step 2 — Fill Expected Values** from spec only. Do not reference actual output. Do not reference what the connector currently does.

**STOP. Do not write GATE 1 until all Expected Values are filled.**

**GATE 1** (Expert):
- [ ] All Expected Value cells filled — {N}/{N} complete — no blank cells
- [ ] No Spec Clause cells blank
- [ ] Actual output not consulted during Phase 1A — [CONFIRMED / NOT CONFIRMED]
- [ ] Expert runtime knowledge of current connector behavior not applied to Expected Values — [CONFIRMED / NOT CONFIRMED]

Set `gate1_isolation_confirmed: true`.

**STOP. Phase 1B cannot begin until gate1_isolation_confirmed = true. Phase 1B owner is Automate — not Expert.**

---

### PHASE 1B — INERTIA REGISTER (Automate)

**CANNOT BEGIN UNTIL: gate1_isolation_confirmed = true. (Per Phase Dependency Reference Table: Phase 1B — Unblocked By: gate1_isolation_confirmed = true.) OWNER: AUTOMATE. Expert cannot run or certify this phase.**

**Inertia risk:** The Phase 1A author cannot reliably detect their own inertia contamination. Automate reviews each row for residual contamination.

Ask first: For each Phase 1A row, does the Expected Value appear to reflect what the connector currently does rather than what the spec defines — and if so, which contamination type (NAME, TYPE, or CLAUSE) best characterizes the deviation — not based on assumptions about what the connector ought to return, but based on whether the value is derivable from the spec clause cited?

For each Phase 1A row: does the Expected Value appear to reflect current connector behavior rather than spec derivation? Label each flagged entry as INERTIA-NN. Assign Contamination Type: NAME (identifier or naming mismatch), TYPE (schema or data-type mismatch), CLAUSE (condition, rule, or logic mismatch).

INERTIA REGISTER — all columns required:

| ID | Row | Element | Contamination Type | Inertia Signal? (Yes/No) | Basis | Disposition |
|----|-----|---------|-------------------|--------------------------|-------|-------------|
| INERTIA-01 | | | NAME / TYPE / CLAUSE | | | |

**STOP. Do not write GATE 1B-TM until all rows reviewed.**

**GATE 1B-TM** — Per-Type Conditional Verification Table (Automate certifies):

| Contamination Type | Entry Count | Entries (INERTIA-NN list) | Every Entry RESOLVED? |
|-------------------|-------------|--------------------------|----------------------|
| NAME | {count} | {INERTIA-NN, ...} | YES — all resolved \| (if 0: *vacuous pass — every INERTIA-NN entry RESOLVED for NAME*) |
| TYPE | {count} | {INERTIA-NN, ...} | YES — all resolved \| (if 0: *vacuous pass — every INERTIA-NN entry RESOLVED for TYPE*) |
| CLAUSE | {count} | {INERTIA-NN, ...} | YES — all resolved \| (if 0: *vacuous pass — every INERTIA-NN entry RESOLVED for CLAUSE*) |

**Per-Type Verification Checklists:**

*NAME entries only:*
If zero: `vacuous pass — every INERTIA-NN entry RESOLVED for NAME (zero entries).`
- [ ] INERTIA-{NN}: {element} -> RESOLVED

*TYPE entries only:*
If zero: `vacuous pass — every INERTIA-NN entry RESOLVED for TYPE (zero entries).`
- [ ] INERTIA-{NN}: {element} -> RESOLVED

*CLAUSE entries only:*
If zero: `vacuous pass — every INERTIA-NN entry RESOLVED for CLAUSE (zero entries).`
- [ ] INERTIA-{NN}: {element} -> RESOLVED

Each zero-entry type block must still appear with the vacuous-pass declaration.

**STOP. Do not write GATE 1B until GATE 1B-TM is complete.**

**GATE 1B** (Automate certifies — Expert cannot certify this gate):
- [ ] All `{N}` Phase 1A rows reviewed — none skipped
- [ ] Contamination Type assigned for every flagged row
- [ ] GATE 1B-TM complete — all three type rows populated
- [ ] Per-type checklists complete — each non-empty type block fully checked; each zero-entry type block explicitly declares vacuous pass
- [ ] No unresolved INERTIA-NN entries — [CONFIRMED / NOT CONFIRMED]
- [ ] Per Phase Dependency Reference Table: GATE 1B — Unblocked By: GATE 1B-TM complete. This gate does not close until that condition is satisfied — [CONFIRMED / NOT CONFIRMED]

Set `gate1b_challenge_confirmed: true`.

**STOP. Phase 2 cannot begin until gate1b_challenge_confirmed = true.**

---

### PHASE 2 — Actual Output (Expert)

**CANNOT BEGIN UNTIL: gate1b_challenge_confirmed = true. (Per Phase Dependency Reference Table: Phase 2 — Unblocked By: gate1b_challenge_confirmed = true.)**

Ask first: For each scope element, what does the connector actually return in the current environment — captured now, without consulting the Expected Values already committed above to calibrate your observation?

Run the connector operation. Record actual output for each scope element. Add Actual Value column. Do not modify Expected Values.

| Element | Element Type | Spec Clause | Expected Value | Actual Value |
|---------|--------------|-------------|----------------|--------------|

**GATE 2** (Expert):
- [ ] Actual Value recorded for all `{N}` elements — no blank cells
- [ ] No Expected Value cells modified

Set `gate2_actual_complete: true`.

**STOP. Phase 3 cannot begin until gate2_actual_complete = true.**

---

### PHASE 3 — Diff and Classification (Automate)

**CANNOT BEGIN UNTIL: gate2_actual_complete = true. (Per Phase Dependency Reference Table: Phase 3 — Unblocked By: gate2_actual_complete = true.)**

Ask first: For each element, does the actual value match the expected value — not whether it seems reasonable or close, but whether it satisfies the spec contract exactly — and if not, does the deviation affect contract correctness (breaking), integration quality (degraded), or only surface presentation (cosmetic)?

Classify each row: MATCH | MISMATCH. For MISMATCH rows: assign Severity (breaking | degraded | cosmetic).

**STOP. Do not write root cause hypotheses in Phase 3. Root causes are Phase 4. Root cause text in Phase 3 = immediate GATE 3 failure condition.**

| Element | Element Type | Spec Clause | Expected Value | Actual Value | Match? | Severity |
|---------|--------------|-------------|----------------|--------------|--------|----------|

**GATE 3** (Automate):
- [ ] Every row classified MATCH or MISMATCH — no blank Match? cells
- [ ] No Severity cells blank on MISMATCH rows
- [ ] No Spec Clause cells blank on any row
- [ ] No Element Type cells blank on any row
- [ ] No root cause hypotheses in Phase 3 output — [CONFIRMED / NOT CONFIRMED]

Set `gate3_diff_complete: true`.

**STOP. Phase 4 cannot begin until gate3_diff_complete = true.**

---

### PHASE 4 — Findings (Expert)

**CANNOT BEGIN UNTIL: gate3_diff_complete = true. (Per Phase Dependency Reference Table: Phase 4 — Unblocked By: gate3_diff_complete = true.)**

Ask first: For each MISMATCH, what connector-layer mechanism most plausibly explains why the actual value diverges from the expected value — and if the root cause is inertia-spec-drift, what specific downstream consequence persists for which user, flow, or contract guarantee if this finding is never resolved?

For each MISMATCH row, produce a finding scaffold. The "Harm if unresolved:" field is mandatory for all findings where Root Cause includes an inertia classification.

```
F-{NN}: {Element Name}
  Severity:           {from Phase 3 — do not reassign here}
  Spec Ref:           {Spec Clause}
  Root Cause:         {connector mechanism — field-mapping-delta | auth-handshake-mismatch | action-payload-drift | trigger-payload-gap | error-shape-change | metadata-convention-gap | inertia-spec-drift — "unknown" alone not accepted}
  Harm if unresolved: {specific affected user, flow, or contract guarantee} will experience {nature of persistent deviation} — e.g., "Automate flows consuming {element} will receive {wrong-value} until spec clause {X} is patched"
  Resolution:         {specific investigative step — "investigate further" alone not accepted}
```

"Harm if unresolved:" fill rules:
- Required for every finding where Root Cause = inertia-spec-drift.
- Structurally distinct from Root Cause — separate labeled line.
- Must name: (1) specific affected user, consumer, flow, or contract guarantee; (2) nature of persistent deviation if never resolved.
- Generic entries ("spec drift will continue") do not pass.

**Phase 4 gate check:**
- [ ] Every inertia-classified finding has a populated "Harm if unresolved:" field — [CONFIRMED / NOT CONFIRMED]
- [ ] No "Harm if unresolved:" field uses generic language — [CONFIRMED / NOT CONFIRMED]

**STOP. Proceed to CASCADE GATE after all findings written and Phase 4 gate check confirmed.**

---

### CASCADE GATE (Expert)

**CANNOT BEGIN UNTIL: Phase 4 findings complete and Phase 4 gate check confirmed.**

| Finding | Severity | Route | Path | Must NOT Visit |
|---------|----------|-------|------|----------------|
| F-{NN} | | CASCADE-A (in-boundary: no scope gap) | Phase 4B -> Phase 5 | **Phase 0 — must NOT re-open scope enumeration** |
| F-{NN} | | CASCADE-B (out-of-boundary: scope gap) | Phase 0 amendment -> Phase 1A -> resume | **Phase 5 — must NOT proceed without Phase 0 amendment** |

**CASCADE GATE:**
- [ ] Every finding assigned CASCADE-A or CASCADE-B — no unassigned rows
- [ ] Must NOT Visit populated for every row
- [ ] No CASCADE-A finding has re-opened Phase 0 — [CONFIRMED / NOT CONFIRMED]
- [ ] No CASCADE-B finding has proceeded to Phase 5 without completing Phase 0 amendment — [CONFIRMED / NOT CONFIRMED]

**STOP. Phase 4B cannot begin until CASCADE GATE is complete.**

---

### PHASE 4B — Calibration (Expert — standalone phase; do not merge with Phase 4)

**CANNOT BEGIN UNTIL: Phase 4 complete AND CASCADE GATE signed off. (Per Phase Dependency Reference Table: Phase 4B — Unblocked By: Phase 4 complete AND CASCADE GATE complete.)**

Ask first: Is the severity distribution across findings reasonable — is there at least one non-breaking finding, or is every finding individually justifiable at breaking due to a specific contract guarantee it violates?

Severity tally (complete before writing any calibration assessment):

| Severity | Count |
|----------|-------|
| breaking | |
| degraded | |
| cosmetic | |

For each finding individually: justify its severity assignment. Group justification ("all breaking because...") = gate failure condition.

**STOP. Do not write GATE 4B until individual justifications are written for every finding.**

**GATE 4B** (Expert):
- [ ] Severity tally completed before assessments
- [ ] Each finding individually justified at its assigned level
- [ ] Distribution reasonable — at least two levels represented, or single level individually justified

Set `gate4b_calibration_confirmed: true`.

**STOP. Phase 5 cannot begin until gate4b_calibration_confirmed = true.**

---

### PHASE 5 — CONTRACT DELTA (Expert)

**CANNOT BEGIN UNTIL: gate4b_calibration_confirmed = true. (Per Phase Dependency Reference Table: Phase 5 — Unblocked By: gate4b_calibration_confirmed = true.) CASCADE-B findings: Phase 0 amendment must be complete before this phase.**

Ask first: For each finding, does the spec need to be amended because the spec is wrong, or does the implementation need to be corrected because the spec is right — and which amendment type most precisely describes the required change?

| Finding | Spec Clause | Priority | Amendment Type | Required Change |
|---------|-------------|----------|----------------|-----------------|

Priority: breaking->P1, degraded->P2, cosmetic->P3. Blank Priority cells not accepted.
Amendment Type: add-field \| remove-field \| change-type \| change-enum \| change-error-shape \| change-auth-flow. Blank Amendment Type cells not accepted.

**CONTRACT VERDICT:**
- breaking: {N}, degraded: {N}, cosmetic: {N}
- Verdict: PASS (zero breaking) \| DEGRADED (no breaking, some degraded) \| FAIL (one or more breaking)

**Phase 5 does not close until every CASCADE-B finding has a completed Phase 0 amendment on record.**

---

## V-02 — Named Inertia Correction Route Table

**Axis:** Inertia framing — consolidating all correction paths into a standalone auditable reference

**Hypothesis:** R10 V-05 (27.5/31) fails C-36 because inertia correction paths are encoded only as inline CASCADE-A / CASCADE-B labels within the CASCADE GATE — a per-finding routing table. C-36 requires a standalone named-route section that consolidates all correction paths into a single auditable reference before the CASCADE GATE executes routing per finding. The structural distinction: the CASCADE GATE answers "which route does this finding take?" (execution); the INERTIA CORRECTION ROUTES section answers "what does each route consist of?" (reference). V-02 adds `## INERTIA CORRECTION ROUTES` as a dedicated section before Phase 4, with ROUTE-A and ROUTE-B each carrying: (1) triggering condition; (2) complete step sequence in arrow notation; (3) explicit upstream anchor for ROUTE-B; (4) Must NOT Visit prohibition. The CASCADE GATE is retained as the per-finding execution tracker and references routes by name. Phase 4's CANNOT BEGIN UNTIL says "Consult INERTIA CORRECTION ROUTES before assigning cascade paths." C-35 is not addressed — no standalone pre-phase dependency table is added. Expected: C-36 PASS, C-35 FAIL.

---

You are running **trace-contract** for Topic: `{Topic}`.

**The inertia problem.** The expected table you are about to build is a claim about the spec contract — not about the connector's current runtime behavior. Inertia contamination (anchoring expected values to what the connector currently does) silences the diff and defeats the exercise. Three contamination entry points exist: scope anchoring (Phase 0), value anchoring (Phase 1A), and residual contamination detectable only by a second reader with an INERTIA REGISTER (Phase 1B). Each phase closes one entry point.

**Role assignment:**

| Role | Identity | Phases Owned | May NOT perform |
|------|----------|-------------|-----------------|
| Expert | Connectors contract expert | Phase 0, Phase 1A, Phase 2, Phase 4, CASCADE GATE, Phase 4B, Phase 5 | Phase 1B certification; GATE 1B certification |
| Automate | Connector automation specialist | Phase 1B, GATE 1B-TM, GATE 1B, Phase 3 | Phase 1A derivation; GATE 1 certification |

**Phase dependency chain:**

| Phase | Name | Owner | Unblocked By | Gate Key Set | Must NOT Visit |
|-------|------|-------|-------------|-------------|----------------|
| 0 | Scope Enumeration | Expert | Start | gate0_scope_confirmed | — |
| GATE 0 | Scope Gate | Expert | Phase 0 complete | — | — |
| 1A | Expected Output | Expert | gate0_scope_confirmed = true | gate1_isolation_confirmed | — |
| GATE 1 | Isolation Gate | Expert | Phase 1A complete | — | — |
| 1B | INERTIA REGISTER | **Automate** | gate1_isolation_confirmed = true | (-> GATE 1B-TM) | — |
| GATE 1B-TM | Per-Type Verification | **Automate** | Phase 1B complete | — | — |
| GATE 1B | Challenge Gate | **Automate** | GATE 1B-TM complete | gate1b_challenge_confirmed | — |
| 2 | Actual Output | Expert | gate1b_challenge_confirmed = true | gate2_actual_complete | — |
| GATE 2 | Actual Gate | Expert | Phase 2 complete | — | — |
| 3 | Diff + Classification | Automate | gate2_actual_complete = true | gate3_diff_complete | — |
| GATE 3 | Diff Gate | Automate | Phase 3 complete | — | — |
| 4 | Findings | Expert | gate3_diff_complete = true | — | — |
| CASCADE GATE | Cascade Gate | Expert | All findings assigned | — | — |
| 4B | Calibration | Expert | Phase 4 + CASCADE GATE | gate4b_calibration_confirmed | — |
| GATE 4B | Calibration Gate | Expert | Phase 4B complete | — | — |
| 5 | CONTRACT DELTA | Expert | gate4b_calibration_confirmed = true | — | — |

**Required frontmatter:**

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

**CANNOT BEGIN UNTIL: Start of artifact.**

**Inertia risk:** Expert anchors element names to what the connector currently exposes, omitting spec-defined elements the connector has not yet implemented.

Ask first: What connector contract elements does the spec define for `{Topic}` — not what the connector currently exposes, but what the spec says should be there?

Enumerate all in-scope elements as a SCOPE MANIFEST. Derive scope from spec only.

| # | Element Name | Element Type | Spec Clause Key |
|---|--------------|--------------|-----------------|
| | | schema-field \| auth-handshake \| action-payload \| trigger-payload \| error-shape \| metadata | |

**STOP. Do not write GATE 0 until Phase 0 enumeration is complete.**

**GATE 0** (Expert):
- [ ] SCOPE MANIFEST complete — `{N}` elements enumerated
- [ ] Element Type populated — no blank cells
- [ ] Spec Clause Key populated — no blank cells
- [ ] Scope derived from spec — current connector behavior excluded — [CONFIRMED / NOT CONFIRMED]

Set `gate0_scope_confirmed: true`.

**STOP. Phase 1A cannot begin until gate0_scope_confirmed = true.**

---

### PHASE 1A — Expected Output (Expert)

**CANNOT BEGIN UNTIL: gate0_scope_confirmed = true.**

**Inertia risk:** Expert anchors Expected Values to what the connector currently returns.

Ask first: For each scope element, what does the spec say the expected value should be — stated as a spec-derivable claim, not as a description of what the connector currently returns?

**Step 1 — Commit skeleton:**

| Element | Element Type | Spec Clause | Expected Value |
|---------|--------------|-------------|----------------|
| (one row per SCOPE MANIFEST entry) | | | <- leave blank |

Record: `SKELETON COMMITTED — {N} rows`

**Step 2 — Fill Expected Values** from spec only.

**STOP. Do not write GATE 1 until all Expected Values are filled.**

**GATE 1** (Expert):
- [ ] All Expected Value cells filled — no blank cells
- [ ] No Spec Clause cells blank
- [ ] Actual output not consulted during Phase 1A — [CONFIRMED / NOT CONFIRMED]
- [ ] Expert runtime knowledge of current connector behavior not applied — [CONFIRMED / NOT CONFIRMED]

Set `gate1_isolation_confirmed: true`.

**STOP. Phase 1B cannot begin until gate1_isolation_confirmed = true. Phase 1B owner is Automate.**

---

### PHASE 1B — INERTIA REGISTER (Automate)

**CANNOT BEGIN UNTIL: gate1_isolation_confirmed = true. OWNER: AUTOMATE.**

Ask first: For each Phase 1A row, does the Expected Value appear to reflect what the connector currently does rather than what the spec defines — and if so, which contamination type (NAME, TYPE, or CLAUSE) best characterizes the deviation — not based on assumptions about the connector's implementation, but based on whether the value is derivable from the spec clause cited?

For each Phase 1A row: label each flagged entry as INERTIA-NN. Assign Contamination Type: NAME | TYPE | CLAUSE.

| ID | Row | Element | Contamination Type | Inertia Signal? (Yes/No) | Basis | Disposition |
|----|-----|---------|-------------------|--------------------------|-------|-------------|

**STOP. Do not write GATE 1B-TM until all rows reviewed.**

**GATE 1B-TM** — Per-Type Conditional Verification Table:

| Contamination Type | Entry Count | Entries | Every Entry RESOLVED? |
|-------------------|-------------|---------|----------------------|
| NAME | {count} | | YES \| (if 0: *vacuous pass*) |
| TYPE | {count} | | YES \| (if 0: *vacuous pass*) |
| CLAUSE | {count} | | YES \| (if 0: *vacuous pass*) |

Per-Type Checklists (all three blocks required, including zero-entry):

*NAME:* If zero: `vacuous pass — zero entries.`
- [ ] INERTIA-{NN} -> RESOLVED

*TYPE:* If zero: `vacuous pass — zero entries.`
- [ ] INERTIA-{NN} -> RESOLVED

*CLAUSE:* If zero: `vacuous pass — zero entries.`
- [ ] INERTIA-{NN} -> RESOLVED

**STOP. Do not write GATE 1B until GATE 1B-TM is complete.**

**GATE 1B** (Automate):
- [ ] All rows reviewed — none skipped
- [ ] Contamination Type assigned for every flagged row
- [ ] GATE 1B-TM complete — all three type rows and per-type checklists present
- [ ] No unresolved INERTIA-NN entries — [CONFIRMED / NOT CONFIRMED]

Set `gate1b_challenge_confirmed: true`.

**STOP. Phase 2 cannot begin until gate1b_challenge_confirmed = true.**

---

### PHASE 2 — Actual Output (Expert)

**CANNOT BEGIN UNTIL: gate1b_challenge_confirmed = true.**

Ask first: For each scope element, what does the connector actually return in the current environment — captured now, without consulting the Expected Values already committed above to calibrate your observation?

| Element | Element Type | Spec Clause | Expected Value | Actual Value |
|---------|--------------|-------------|----------------|--------------|

**GATE 2:**
- [ ] Actual Value recorded for all elements — no blank cells
- [ ] No Expected Value cells modified

Set `gate2_actual_complete: true`.

**STOP. Phase 3 cannot begin until gate2_actual_complete = true.**

---

### PHASE 3 — Diff and Classification (Automate)

**CANNOT BEGIN UNTIL: gate2_actual_complete = true.**

Ask first: For each element, does the actual value match the expected value — not whether it seems reasonable or close, but whether it satisfies the spec contract exactly — and if not, which severity class applies?

STOP. Do not write root cause hypotheses in Phase 3.

| Element | Element Type | Spec Clause | Expected Value | Actual Value | Match? | Severity |
|---------|--------------|-------------|----------------|--------------|--------|----------|

**GATE 3:**
- [ ] Every row classified MATCH or MISMATCH
- [ ] No Severity cells blank on MISMATCH rows
- [ ] No root cause hypotheses in Phase 3 output — [CONFIRMED / NOT CONFIRMED]

Set `gate3_diff_complete: true`.

**STOP. Phase 4 cannot begin until gate3_diff_complete = true.**

---

## INERTIA CORRECTION ROUTES

Consult this section before assigning any finding to a cascade path in the CASCADE GATE. This reference consolidates all inertia correction paths into one auditable location. The CASCADE GATE is the per-finding execution tracker that references these routes by name — do not redefine routes within the CASCADE GATE.

| Route | Trigger Condition | Complete Path | Upstream Anchor | Must NOT Visit |
|-------|------------------|--------------|-----------------|----------------|
| ROUTE-A | In-boundary finding: element is present in the SCOPE MANIFEST; deviation originates in expected-value derivation or implementation divergence — no scope amendment required | Phase 4 -> CASCADE GATE (ROUTE-A) -> Phase 4B -> GATE 4B -> Phase 5 | Phase 4 (correction is within already-scoped elements) | **Phase 0 — must NOT re-open scope enumeration. ROUTE-A findings do not require scope amendment.** |
| ROUTE-B | Out-of-boundary discovery: element is absent from the SCOPE MANIFEST; spec defines an element Phase 0 missed — scope amendment required before Phase 5 | Phase 4 -> CASCADE GATE (ROUTE-B) -> Phase 0 amendment -> GATE 0 (re-confirm) -> Phase 1A (re-fill affected rows) -> GATE 1 (re-confirm) -> Phase 1B (re-review added rows) -> GATE 1B -> resume Phase 4 -> Phase 4B -> GATE 4B -> Phase 5 | Phase 0 (GATE 0 must be re-confirmed after scope amendment before proceeding downstream) | **Phase 5 — must NOT proceed to CONTRACT DELTA until Phase 0 amendment complete and GATE 0 re-confirmed.** |

---

### PHASE 4 — Findings (Expert)

**CANNOT BEGIN UNTIL: gate3_diff_complete = true. Consult INERTIA CORRECTION ROUTES above before assigning cascade paths.**

Ask first: For each MISMATCH, what connector-layer mechanism most plausibly explains why the actual value diverges from the expected value — and if the root cause is inertia-spec-drift, what specific downstream consequence persists for which user, flow, or contract guarantee if this finding is never resolved?

```
F-{NN}: {Element Name}
  Severity:           {from Phase 3}
  Spec Ref:           {Spec Clause}
  Root Cause:         {field-mapping-delta | auth-handshake-mismatch | action-payload-drift | trigger-payload-gap | error-shape-change | metadata-convention-gap | inertia-spec-drift}
  Harm if unresolved: {specific affected entity} will experience {nature of persistent deviation}
  Resolution:         {specific investigative step}
```

**Phase 4 gate check:**
- [ ] Every inertia-classified finding has a populated "Harm if unresolved:" field — [CONFIRMED / NOT CONFIRMED]
- [ ] No generic language in "Harm if unresolved:" fields — [CONFIRMED / NOT CONFIRMED]

**STOP. Proceed to CASCADE GATE after findings complete.**

---

### CASCADE GATE (Expert)

**CANNOT BEGIN UNTIL: Phase 4 complete. Select route per finding from INERTIA CORRECTION ROUTES table above.**

| Finding | Severity | Route | Path | Must NOT Visit |
|---------|----------|-------|------|----------------|
| F-{NN} | | ROUTE-A (in-boundary) | Phase 4B -> Phase 5 | **Phase 0** |
| F-{NN} | | ROUTE-B (out-of-boundary) | Phase 0 amendment -> resume | **Phase 5 without amendment** |

- [ ] Every finding assigned ROUTE-A or ROUTE-B per INERTIA CORRECTION ROUTES table
- [ ] Must NOT Visit populated for every row
- [ ] No ROUTE-A finding has re-opened Phase 0 — [CONFIRMED / NOT CONFIRMED]
- [ ] No ROUTE-B finding has proceeded to Phase 5 without Phase 0 amendment — [CONFIRMED / NOT CONFIRMED]

**STOP. Phase 4B cannot begin until CASCADE GATE is complete.**

---

### PHASE 4B — Calibration (Expert — standalone; do not merge with Phase 4)

**CANNOT BEGIN UNTIL: Phase 4 complete AND CASCADE GATE signed off.**

Ask first: Is the severity distribution across findings reasonable — is there at least one non-breaking finding, or is every finding individually justifiable at breaking due to a specific contract guarantee it violates?

| Severity | Count |
|----------|-------|
| breaking | |
| degraded | |
| cosmetic | |

For each finding individually: justify its severity assignment.

**GATE 4B:**
- [ ] Severity tally completed before assessments
- [ ] Each finding individually justified
- [ ] Distribution reasonable

Set `gate4b_calibration_confirmed: true`.

**STOP. Phase 5 cannot begin until gate4b_calibration_confirmed = true.**

---

### PHASE 5 — CONTRACT DELTA (Expert)

**CANNOT BEGIN UNTIL: gate4b_calibration_confirmed = true. ROUTE-B findings: Phase 0 amendment must be complete.**

Ask first: For each finding, does the spec need to be amended because the spec is wrong, or does the implementation need to be corrected because the spec is right — and which amendment type most precisely describes the required change?

| Finding | Spec Clause | Priority | Amendment Type | Required Change |
|---------|-------------|----------|----------------|-----------------|

Priority: breaking->P1, degraded->P2, cosmetic->P3.
Amendment Type: add-field \| remove-field \| change-type \| change-enum \| change-error-shape \| change-auth-flow.

**CONTRACT VERDICT:** breaking: {N}, degraded: {N}, cosmetic: {N} — PASS \| DEGRADED \| FAIL

---

## V-03 — Role-Owned Schema Confirmation Gate (C-35 alternative)

**Axis:** Role sequence — Automate certifies the execution schema before Expert begins Phase 0

**Hypothesis:** V-01 adds a standalone Phase Dependency Reference Table as a passive preamble — it is present upstream but not enforced. A writer could skip it and still begin Phase 0 without consequence. V-03 makes the Phase Dependency Reference Table a role-owned artifact with a gate that blocks Expert from beginning Phase 0. A new `SCHEMA GATE` is added before Phase 0: Automate populates the Phase Dependency Reference Table by reading the phase definitions, confirms all Unblocked By entries are consistent with the phase dependency chain, and certifies the table. Expert may not begin Phase 0 until `gate_schema_confirmed = true`. This turns the table from static front matter into an active gate artifact: its presence is enforced by role separation and gate key state, not just placement. The table produced by the SCHEMA GATE satisfies C-35 because it is standalone, upstream of all phase bodies, populated by a distinct role, and gated. C-36 is not addressed. Expected: C-35 PASS, C-36 FAIL.

---

You are running **trace-contract** for Topic: `{Topic}`.

**The inertia problem.** The expected table you are about to build is a claim about the spec contract — not about the connector's current runtime behavior. Inertia contamination silences the diff. Three entry points: scope anchoring (Phase 0), value anchoring (Phase 1A), residual contamination (Phase 1B).

**Role assignment:**

| Role | Identity | Phases Owned | May NOT perform |
|------|----------|-------------|-----------------|
| Expert | Connectors contract expert | Phase 0, Phase 1A, Phase 2, Phase 4, CASCADE GATE, Phase 4B, Phase 5 | Phase 1B certification; GATE 1B certification; SCHEMA GATE certification |
| Automate | Connector automation specialist | SCHEMA GATE, Phase 1B, GATE 1B-TM, GATE 1B, Phase 3 | Phase 1A derivation; GATE 1 certification; Phase 0 enumeration |

Role separation is structurally enforced. Expert may not certify SCHEMA GATE. Expert may not begin Phase 0 until gate_schema_confirmed = true.

**Required frontmatter:**

```yaml
---
topic: {Topic}
signal: contract
date: {date}
inertia_framing: true
phase1a_author: Expert
gate1b_owner: Automate
gate_schema_confirmed: false
gate0_scope_confirmed: false
gate1_isolation_confirmed: false
gate1b_challenge_confirmed: false
gate2_actual_complete: false
gate3_diff_complete: false
gate4b_calibration_confirmed: false
---
```

---

### SCHEMA GATE — Phase Dependency Confirmation (Automate)

**CANNOT BEGIN UNTIL: Start of artifact. OWNER: AUTOMATE. Expert cannot certify or bypass this gate.**

Ask first: Reading the phase definitions in this prompt, what is the complete ordered sequence of phases and gates — and for each, what is the specific gate key or prior phase that must be confirmed before it can begin — not a general statement about ordering, but the specific key as it appears in the prompt?

Automate reads the phase definitions and produces the following reference table. All rows required — blank cells are a SCHEMA GATE failure condition.

## Phase Dependency Reference Table

| Phase | Name | Owner | Unblocked By |
|-------|------|-------|-------------|
| SCHEMA GATE | Schema Confirmation | Automate | Start of artifact |
| Phase 0 | Scope Enumeration | Expert | gate_schema_confirmed = true |
| GATE 0 | Scope Gate | Expert | Phase 0 enumeration complete |
| Phase 1A | Expected Output | Expert | gate0_scope_confirmed = true |
| GATE 1 | Isolation Gate | Expert | Phase 1A fill complete |
| Phase 1B | INERTIA REGISTER | Automate | gate1_isolation_confirmed = true |
| GATE 1B-TM | Per-Type Verification | Automate | Phase 1B complete |
| GATE 1B | Challenge Gate | Automate | GATE 1B-TM complete |
| Phase 2 | Actual Output | Expert | gate1b_challenge_confirmed = true |
| GATE 2 | Actual Gate | Expert | Phase 2 complete |
| Phase 3 | Diff + Classification | Automate | gate2_actual_complete = true |
| GATE 3 | Diff Gate | Automate | Phase 3 complete |
| Phase 4 | Findings | Expert | gate3_diff_complete = true |
| CASCADE GATE | Cascade Gate | Expert | Phase 4 complete |
| Phase 4B | Calibration | Expert | Phase 4 + CASCADE GATE complete |
| GATE 4B | Calibration Gate | Expert | Phase 4B complete |
| Phase 5 | CONTRACT DELTA | Expert | gate4b_calibration_confirmed = true |

**SCHEMA GATE** (Automate certifies — Expert cannot certify):
- [ ] All phases listed — no phase omitted — {N} rows
- [ ] Owner column populated for every row — no blank cells
- [ ] Unblocked By column populated for every row with the specific gate key or prior phase condition — no blank cells
- [ ] Table is produced upstream of Phase 0 — [CONFIRMED / NOT CONFIRMED]

Set `gate_schema_confirmed: true`.

**STOP. Phase 0 cannot begin until gate_schema_confirmed = true.**

---

### PHASE 0 — Scope Enumeration (Expert)

**CANNOT BEGIN UNTIL: gate_schema_confirmed = true. (Per Phase Dependency Reference Table, certified by Automate at SCHEMA GATE.)**

**Inertia risk:** Expert anchors element names to what the connector currently exposes.

Ask first: What connector contract elements does the spec define for `{Topic}` — not what the connector currently exposes, but what the spec says should be there?

| # | Element Name | Element Type | Spec Clause Key |
|---|--------------|--------------|-----------------|
| | | schema-field \| auth-handshake \| action-payload \| trigger-payload \| error-shape \| metadata | |

**STOP. Do not write GATE 0 until Phase 0 enumeration is complete.**

**GATE 0** (Expert):
- [ ] SCOPE MANIFEST complete
- [ ] Element Type and Spec Clause Key populated — no blank cells
- [ ] Scope derived from spec — current connector behavior excluded — [CONFIRMED / NOT CONFIRMED]

Set `gate0_scope_confirmed: true`.

**STOP. Phase 1A cannot begin until gate0_scope_confirmed = true.**

---

### PHASE 1A — Expected Output (Expert)

**CANNOT BEGIN UNTIL: gate0_scope_confirmed = true.**

Ask first: For each scope element, what does the spec say the expected value should be — stated as a spec-derivable claim, not as a description of what the connector currently returns?

**Step 1 — Commit skeleton:**

| Element | Element Type | Spec Clause | Expected Value |
|---------|--------------|-------------|----------------|
| | | | <- leave blank |

`SKELETON COMMITTED — {N} rows`

**Step 2 — Fill Expected Values** from spec only.

**GATE 1:**
- [ ] All Expected Value cells filled
- [ ] Actual output not consulted — [CONFIRMED / NOT CONFIRMED]
- [ ] Expert runtime knowledge not applied — [CONFIRMED / NOT CONFIRMED]

Set `gate1_isolation_confirmed: true`.

**STOP. Phase 1B cannot begin until gate1_isolation_confirmed = true. Owner: Automate.**

---

### PHASE 1B — INERTIA REGISTER (Automate)

**CANNOT BEGIN UNTIL: gate1_isolation_confirmed = true. OWNER: AUTOMATE.**

Ask first: For each Phase 1A row, does the Expected Value appear to reflect what the connector currently does rather than what the spec defines — and if so, which contamination type (NAME, TYPE, or CLAUSE) best characterizes the deviation — not based on assumptions about the connector's implementation, but based on whether the value is derivable from the spec clause cited?

| ID | Row | Element | Contamination Type | Inertia Signal? | Basis | Disposition |
|----|-----|---------|-------------------|-----------------|-------|-------------|

**GATE 1B-TM:**

| Contamination Type | Count | Entries | RESOLVED? |
|---|---|---|---|
| NAME | | | YES \| vacuous pass |
| TYPE | | | YES \| vacuous pass |
| CLAUSE | | | YES \| vacuous pass |

Per-type checklists (all three blocks required):
*NAME:* If zero: `vacuous pass.` | *TYPE:* If zero: `vacuous pass.` | *CLAUSE:* If zero: `vacuous pass.`

**GATE 1B** (Automate):
- [ ] All rows reviewed
- [ ] GATE 1B-TM complete — three type blocks present
- [ ] No unresolved INERTIA-NN entries — [CONFIRMED / NOT CONFIRMED]

Set `gate1b_challenge_confirmed: true`.

**STOP. Phase 2 cannot begin until gate1b_challenge_confirmed = true.**

---

### PHASE 2 — Actual Output (Expert)

**CANNOT BEGIN UNTIL: gate1b_challenge_confirmed = true.**

Ask first: For each scope element, what does the connector actually return — captured now, without consulting Expected Values above to calibrate your observation?

| Element | Element Type | Spec Clause | Expected Value | Actual Value |
|---------|--------------|-------------|----------------|--------------|

**GATE 2:** Actual Values recorded, no Expected Value cells modified. Set `gate2_actual_complete: true`.

**STOP. Phase 3 cannot begin until gate2_actual_complete = true.**

---

### PHASE 3 — Diff and Classification (Automate)

**CANNOT BEGIN UNTIL: gate2_actual_complete = true.**

Ask first: For each element, does the actual value match the expected value — not whether it seems reasonable, but whether it satisfies the spec contract exactly — and if not, which severity class applies?

STOP. No root cause hypotheses in Phase 3.

| Element | Element Type | Spec Clause | Expected Value | Actual Value | Match? | Severity |
|---------|--------------|-------------|----------------|--------------|--------|----------|

**GATE 3:** All rows classified, no root causes. Set `gate3_diff_complete: true`.

**STOP. Phase 4 cannot begin until gate3_diff_complete = true.**

---

### PHASE 4 — Findings (Expert)

**CANNOT BEGIN UNTIL: gate3_diff_complete = true.**

Ask first: For each MISMATCH, what connector-layer mechanism most plausibly explains why the actual value diverges from the expected value — and if the root cause is inertia-spec-drift, what specific downstream consequence persists if this finding is never resolved?

```
F-{NN}: {Element Name}
  Severity:           {from Phase 3}
  Spec Ref:           {Spec Clause}
  Root Cause:         {mechanism}
  Harm if unresolved: {specific affected entity} will experience {persistent deviation}
  Resolution:         {specific investigative step}
```

**Phase 4 gate check:**
- [ ] Every inertia finding has "Harm if unresolved:" — [CONFIRMED / NOT CONFIRMED]
- [ ] No generic language in harm fields — [CONFIRMED / NOT CONFIRMED]

**STOP. Proceed to CASCADE GATE.**

---

### CASCADE GATE (Expert)

| Finding | Severity | Route | Path | Must NOT Visit |
|---------|----------|-------|------|----------------|
| F-{NN} | | CASCADE-A (in-boundary) | Phase 4B -> Phase 5 | **Phase 0** |
| F-{NN} | | CASCADE-B (out-of-boundary) | Phase 0 amendment -> resume | **Phase 5 without amendment** |

**STOP. Phase 4B cannot begin until CASCADE GATE is complete.**

---

### PHASE 4B — Calibration (Expert — standalone)

**CANNOT BEGIN UNTIL: Phase 4 + CASCADE GATE complete.**

Ask first: Is the severity distribution across findings reasonable — is there at least one non-breaking finding, or is every finding individually justifiable at breaking?

| Severity | Count |
|----------|-------|
| breaking | |
| degraded | |
| cosmetic | |

Individual justification per finding. Set `gate4b_calibration_confirmed: true`.

**STOP. Phase 5 cannot begin until gate4b_calibration_confirmed = true.**

---

### PHASE 5 — CONTRACT DELTA (Expert)

**CANNOT BEGIN UNTIL: gate4b_calibration_confirmed = true.**

Ask first: For each finding, does the spec need to be amended because the spec is wrong, or does the implementation need to be corrected because the spec is right — and which amendment type most precisely describes the required change?

| Finding | Spec Clause | Priority | Amendment Type | Required Change |
|---------|-------------|----------|----------------|-----------------|

**CONTRACT VERDICT:** breaking: {N}, degraded: {N}, cosmetic: {N} — PASS \| DEGRADED \| FAIL

---

## V-04 — Top-Positioned Route Table (C-36 alternative)

**Axis:** Inertia framing — route table positioned at top-level with inertia problem statement, before all phases

**Hypothesis:** V-02 places INERTIA CORRECTION ROUTES before Phase 4, after three phases and their gates have already executed. A writer mid-trace must scroll back to consult routes. V-04 positions the route table immediately after the role assignment table — before any phase begins. Framing rationale: the three contamination entry points (scope, value, residual) map directly to the two correction routes (in-boundary vs out-of-boundary). Knowing the repair paths before Phase 0 helps writers recognize an out-of-boundary discovery at the moment it occurs (Phase 4) without consulting a late section. The top-positioned route table satisfies C-36's "standalone reference section" requirement more strongly because it is upstream of all phase content, not just upstream of Phase 4. The CASCADE GATE still executes routing per finding and references the top-level INERTIA CORRECTION ROUTES by name. C-35 is not addressed. Expected: C-36 PASS, C-35 FAIL.

---

You are running **trace-contract** for Topic: `{Topic}`.

**The inertia problem.** The expected table you are about to build is a claim about the spec contract — not about the connector's current runtime behavior. Inertia contamination silences the diff. Three contamination entry points: scope anchoring (Phase 0), value anchoring (Phase 1A), residual contamination (Phase 1B). When a finding surfaces a deviation rooted in inertia, the correction path depends on whether the element was in scope: in-boundary deviations correct within existing phases; out-of-boundary deviations require scope amendment before proceeding. Consult the INERTIA CORRECTION ROUTES table below before beginning any phase.

**Role assignment:**

| Role | Identity | Phases Owned | May NOT perform |
|------|----------|-------------|-----------------|
| Expert | Connectors contract expert | Phase 0, Phase 1A, Phase 2, Phase 4, CASCADE GATE, Phase 4B, Phase 5 | Phase 1B certification; GATE 1B certification |
| Automate | Connector automation specialist | Phase 1B, GATE 1B-TM, GATE 1B, Phase 3 | Phase 1A derivation; GATE 1 certification |

---

## INERTIA CORRECTION ROUTES

Read this section before beginning Phase 0. All inertia correction paths are defined here. The CASCADE GATE references these routes by name — do not redefine routes inline within the CASCADE GATE. This section is the single source of truth for inertia correction routing.

| Route | Trigger Condition | Complete Path | Upstream Anchor | Must NOT Visit |
|-------|------------------|--------------|-----------------|----------------|
| ROUTE-A | In-boundary finding: element is present in SCOPE MANIFEST; deviation is in expected-value derivation or implementation — no scope amendment required | Phase 4 -> CASCADE GATE (ROUTE-A) -> Phase 4B -> GATE 4B -> Phase 5 | Phase 4 | **Phase 0 — must NOT re-open scope for an in-boundary finding** |
| ROUTE-B | Out-of-boundary discovery: element absent from SCOPE MANIFEST; spec defines an element Phase 0 missed — scope amendment required | Phase 4 -> CASCADE GATE (ROUTE-B) -> Phase 0 amendment -> GATE 0 (re-confirm) -> Phase 1A (re-fill affected rows) -> GATE 1 (re-confirm) -> Phase 1B (re-review added rows) -> GATE 1B -> resume Phase 4 -> Phase 4B -> GATE 4B -> Phase 5 | Phase 0 (GATE 0 must re-confirm after amendment) | **Phase 5 — must NOT proceed until Phase 0 amendment complete and GATE 0 re-confirmed** |

---

**Phase dependency chain:**

| Phase | Name | Owner | Unblocked By |
|-------|------|-------|-------------|
| 0 | Scope Enumeration | Expert | Start |
| GATE 0 | Scope Gate | Expert | Phase 0 complete |
| 1A | Expected Output | Expert | gate0_scope_confirmed = true |
| GATE 1 | Isolation Gate | Expert | Phase 1A complete |
| 1B | INERTIA REGISTER | Automate | gate1_isolation_confirmed = true |
| GATE 1B-TM | Per-Type Verification | Automate | Phase 1B complete |
| GATE 1B | Challenge Gate | Automate | GATE 1B-TM complete |
| 2 | Actual Output | Expert | gate1b_challenge_confirmed = true |
| GATE 2 | Actual Gate | Expert | Phase 2 complete |
| 3 | Diff + Classification | Automate | gate2_actual_complete = true |
| GATE 3 | Diff Gate | Automate | Phase 3 complete |
| 4 | Findings | Expert | gate3_diff_complete = true |
| CASCADE GATE | Cascade Gate | Expert | Phase 4 complete |
| 4B | Calibration | Expert | Phase 4 + CASCADE GATE complete |
| GATE 4B | Calibration Gate | Expert | Phase 4B complete |
| 5 | CONTRACT DELTA | Expert | gate4b_calibration_confirmed = true |

**Required frontmatter:**

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

**CANNOT BEGIN UNTIL: Start of artifact.**

**Inertia risk (scope anchoring):** Expert anchors element names to what the connector currently exposes, omitting spec-defined elements. If an out-of-boundary discovery is made in Phase 4, ROUTE-B (see INERTIA CORRECTION ROUTES above) requires returning here for scope amendment.

Ask first: What connector contract elements does the spec define for `{Topic}` — not what the connector currently exposes, but what the spec says should be there?

| # | Element Name | Element Type | Spec Clause Key |
|---|--------------|--------------|-----------------|
| | | schema-field \| auth-handshake \| action-payload \| trigger-payload \| error-shape \| metadata | |

**STOP. Do not write GATE 0 until enumeration is complete.**

**GATE 0:**
- [ ] SCOPE MANIFEST complete
- [ ] No blank cells
- [ ] Scope from spec only — current behavior excluded — [CONFIRMED / NOT CONFIRMED]

Set `gate0_scope_confirmed: true`.

**STOP. Phase 1A cannot begin until gate0_scope_confirmed = true.**

---

### PHASE 1A — Expected Output (Expert)

**CANNOT BEGIN UNTIL: gate0_scope_confirmed = true.**

**Inertia risk (value anchoring):** Expert anchors Expected Values to what the connector currently returns.

Ask first: For each scope element, what does the spec say the expected value should be — stated as a spec-derivable claim, not as a description of what the connector currently returns?

**Step 1 — Commit skeleton:**

| Element | Element Type | Spec Clause | Expected Value |
|---------|--------------|-------------|----------------|
| | | | <- leave blank |

`SKELETON COMMITTED — {N} rows`

**Step 2 — Fill Expected Values** from spec only.

**GATE 1:**
- [ ] All Expected Value cells filled
- [ ] Actual output not consulted — [CONFIRMED / NOT CONFIRMED]
- [ ] Runtime knowledge not applied — [CONFIRMED / NOT CONFIRMED]

Set `gate1_isolation_confirmed: true`.

**STOP. Phase 1B owner: Automate.**

---

### PHASE 1B — INERTIA REGISTER (Automate)

**CANNOT BEGIN UNTIL: gate1_isolation_confirmed = true. OWNER: AUTOMATE.**

Ask first: For each Phase 1A row, does the Expected Value appear to reflect what the connector currently does rather than what the spec defines — and if so, which contamination type (NAME, TYPE, or CLAUSE) best characterizes the deviation — not based on assumptions about connector behavior, but based on whether the value is derivable from the spec clause cited?

| ID | Row | Element | Contamination Type | Inertia Signal? | Basis | Disposition |
|----|-----|---------|-------------------|-----------------|-------|-------------|

**GATE 1B-TM:**

| Type | Count | Entries | RESOLVED? |
|------|-------|---------|-----------|
| NAME | | | YES \| vacuous pass |
| TYPE | | | YES \| vacuous pass |
| CLAUSE | | | YES \| vacuous pass |

Per-type checklists (all three required):
*NAME:* vacuous pass if zero. *TYPE:* vacuous pass if zero. *CLAUSE:* vacuous pass if zero.

**GATE 1B:** All rows reviewed, GATE 1B-TM complete, no unresolved entries. Set `gate1b_challenge_confirmed: true`.

**STOP. Phase 2 cannot begin until gate1b_challenge_confirmed = true.**

---

### PHASE 2 — Actual Output (Expert)

**CANNOT BEGIN UNTIL: gate1b_challenge_confirmed = true.**

Ask first: For each scope element, what does the connector actually return — captured now, without consulting Expected Values above to calibrate your observation?

| Element | Element Type | Spec Clause | Expected Value | Actual Value |
|---------|--------------|-------------|----------------|--------------|

**GATE 2:** Actual Values recorded. Set `gate2_actual_complete: true`.

**STOP. Phase 3 cannot begin until gate2_actual_complete = true.**

---

### PHASE 3 — Diff and Classification (Automate)

**CANNOT BEGIN UNTIL: gate2_actual_complete = true.**

Ask first: For each element, does the actual value match the expected value — not whether it seems reasonable, but whether it satisfies the spec contract exactly — and if not, which severity?

STOP. No root cause hypotheses in Phase 3.

| Element | Element Type | Spec Clause | Expected Value | Actual Value | Match? | Severity |
|---------|--------------|-------------|----------------|--------------|--------|----------|

**GATE 3:** All classified. Set `gate3_diff_complete: true`.

**STOP. Phase 4 cannot begin until gate3_diff_complete = true.**

---

### PHASE 4 — Findings (Expert)

**CANNOT BEGIN UNTIL: gate3_diff_complete = true. Consult INERTIA CORRECTION ROUTES at top of document before assigning cascade paths.**

Ask first: For each MISMATCH, what connector-layer mechanism most plausibly explains the deviation — and if root cause is inertia-spec-drift, what specific downstream consequence persists if never resolved?

```
F-{NN}: {Element Name}
  Severity:           {from Phase 3}
  Spec Ref:           {Spec Clause}
  Root Cause:         {mechanism — inertia-spec-drift | field-mapping-delta | auth-handshake-mismatch | action-payload-drift | trigger-payload-gap | error-shape-change | metadata-convention-gap}
  Harm if unresolved: {specific entity} will experience {persistent deviation}
  Resolution:         {specific step}
```

**Phase 4 gate check:**
- [ ] Every inertia finding has "Harm if unresolved:" — [CONFIRMED / NOT CONFIRMED]
- [ ] No generic language — [CONFIRMED / NOT CONFIRMED]

**STOP. Proceed to CASCADE GATE.**

---

### CASCADE GATE (Expert)

**CANNOT BEGIN UNTIL: Phase 4 complete. Reference INERTIA CORRECTION ROUTES (top of document) for route definitions — do not redefine routes here.**

| Finding | Severity | Route | Path | Must NOT Visit |
|---------|----------|-------|------|----------------|
| F-{NN} | | ROUTE-A (in-boundary) | Phase 4B -> Phase 5 | **Phase 0** |
| F-{NN} | | ROUTE-B (out-of-boundary) | Phase 0 amendment -> resume | **Phase 5 without amendment** |

- [ ] Every finding assigned ROUTE-A or ROUTE-B per INERTIA CORRECTION ROUTES
- [ ] Must NOT Visit populated
- [ ] No ROUTE-A finding re-opened Phase 0 — [CONFIRMED / NOT CONFIRMED]
- [ ] No ROUTE-B finding reached Phase 5 without amendment — [CONFIRMED / NOT CONFIRMED]

**STOP. Phase 4B cannot begin until CASCADE GATE is complete.**

---

### PHASE 4B — Calibration (Expert — standalone)

**CANNOT BEGIN UNTIL: Phase 4 + CASCADE GATE complete.**

Ask first: Is the severity distribution reasonable — at least one non-breaking finding, or every finding individually justifiable at breaking?

| Severity | Count |
|----------|-------|
| breaking | |
| degraded | |
| cosmetic | |

Individual justification per finding. Set `gate4b_calibration_confirmed: true`.

**STOP. Phase 5 cannot begin until gate4b_calibration_confirmed = true.**

---

### PHASE 5 — CONTRACT DELTA (Expert)

**CANNOT BEGIN UNTIL: gate4b_calibration_confirmed = true. ROUTE-B findings: Phase 0 amendment must be complete.**

Ask first: For each finding, does the spec need to be amended because the spec is wrong, or does the implementation need to be corrected — and which amendment type most precisely describes the required change?

| Finding | Spec Clause | Priority | Amendment Type | Required Change |
|---------|-------------|----------|----------------|-----------------|

**CONTRACT VERDICT:** breaking: {N}, degraded: {N}, cosmetic: {N} — PASS \| DEGRADED \| FAIL

---

## V-05 — Combined (Platinum Target: 31/31)

**Axes:** Phase Dependency Reference Table (V-01 C-35 mechanism) + Named Inertia Correction Route Table (V-02 C-36 mechanism) + full R10 V-05 base architecture (C-17, C-37, C-38, C-39 mechanisms)

**Hypothesis:** R10 V-05 achieves 27.5/31 — C-17 PASS, C-37 PASS, C-38 PASS, C-39 PASS, C-35 FAIL, C-36 FAIL. V-05 merges the two open gaps: (1) V-01's standalone `## Phase Dependency Reference Table` section (upstream of Phase 0, maps every phase/gate to its Unblocked By key, cross-referenced from every phase header) closes C-35; (2) V-02's standalone `## INERTIA CORRECTION ROUTES` section (before Phase 4, ROUTE-A and ROUTE-B with full arrow-notation paths, CASCADE GATE references by name) closes C-36. All R10 V-05 mechanisms carry forward: "Ask first:" interrogatives with phase-specific negative exclusion clauses (C-17, C-39 PASS), per-finding "Harm if unresolved:" field (C-37 PASS), STOP-gate sequence as execution protocol (C-38 PASS). The two new sections occupy distinct structural slots: dependency table before Phase 0; route table before Phase 4. Neither duplicates existing mechanisms — the reference table complements per-phase STOP declarations; the route table complements the per-finding CASCADE GATE. Expected: 31/31.

---

You are running **trace-contract** for Topic: `{Topic}`.

**The inertia problem.** The expected table you are about to build is a claim about the spec contract — not about the connector's current runtime behavior. Inertia contamination (anchoring expected values to what the connector currently does) silences the diff and defeats the exercise. Three contamination entry points exist: scope anchoring (Phase 0), value anchoring (Phase 1A), and residual contamination detectable only by a second reader with an INERTIA REGISTER (Phase 1B). Each phase closes one entry point. The inertia framing inside each gate is not decorative.

**Role assignment:**

| Role | Identity | Phases Owned | May NOT perform |
|------|----------|-------------|-----------------|
| Expert | Connectors contract expert | Phase 0, Phase 1A, Phase 2, Phase 4, CASCADE GATE, Phase 4B, Phase 5 | Phase 1B certification; GATE 1B certification |
| Automate | Connector automation specialist | Phase 1B, GATE 1B-TM, GATE 1B, Phase 3 | Phase 1A derivation; GATE 1 certification |

Role separation is structurally enforced. An agent who owns Phase 1A may not certify GATE 1B. An agent who owns Phase 1B may not derive expected values.

---

## Phase Dependency Reference Table

Read this table before beginning Phase 0. No phase may begin until its gate prerequisite is satisfied. This table is the global execution schema — a reader consulting only this table before execution knows the complete ordering before entering any phase body. This table is standalone and does not substitute for the "CANNOT BEGIN UNTIL:" declarations within each phase section — both are required. The per-phase declarations enforce the constraint at the moment of execution; this table provides global visibility before execution.

| Phase | Name | Unblocked By |
|-------|------|-------------|
| Phase 0 | Scope Enumeration | Start of artifact (no prior gate required) |
| GATE 0 | Scope Gate | Phase 0 enumeration complete |
| Phase 1A | Expected Output | gate0_scope_confirmed = true |
| GATE 1 | Isolation Gate | Phase 1A fill complete |
| Phase 1B | INERTIA REGISTER | gate1_isolation_confirmed = true |
| GATE 1B-TM | Per-Type Verification | Phase 1B CHALLENGE LOG complete for all rows |
| GATE 1B | Challenge Gate | GATE 1B-TM complete — all three type blocks present |
| Phase 2 | Actual Output | gate1b_challenge_confirmed = true |
| GATE 2 | Actual Gate | Phase 2 fill complete |
| Phase 3 | Diff + Classification | gate2_actual_complete = true |
| GATE 3 | Diff Gate | Phase 3 classification complete |
| Phase 4 | Findings | gate3_diff_complete = true |
| CASCADE GATE | Cascade Gate | Phase 4 findings complete |
| Phase 4B | Calibration | Phase 4 complete AND CASCADE GATE complete |
| GATE 4B | Calibration Gate | Phase 4B complete |
| Phase 5 | CONTRACT DELTA | gate4b_calibration_confirmed = true |

---

**Phase dependency chain (with cascade routing):**

| Phase | Name | Owner | Unblocked By | Gate Key Set | Must NOT Visit |
|-------|------|-------|-------------|-------------|----------------|
| 0 | Scope Enumeration | Expert | Start | gate0_scope_confirmed | — |
| GATE 0 | Scope Gate | Expert | Phase 0 complete | — | — |
| 1A | Expected Output | Expert | gate0_scope_confirmed = true | gate1_isolation_confirmed | — |
| GATE 1 | Isolation Gate | Expert | Phase 1A complete | — | — |
| 1B | INERTIA REGISTER | **Automate** | gate1_isolation_confirmed = true | (-> GATE 1B-TM) | — |
| GATE 1B-TM | Per-Type Verification | **Automate** | Phase 1B complete | — | — |
| GATE 1B | Challenge Gate | **Automate** | GATE 1B-TM complete | gate1b_challenge_confirmed | — |
| 2 | Actual Output | Expert | gate1b_challenge_confirmed = true | gate2_actual_complete | — |
| GATE 2 | Actual Gate | Expert | Phase 2 complete | — | — |
| 3 | Diff + Classification | Automate | gate2_actual_complete = true | gate3_diff_complete | — |
| GATE 3 | Diff Gate | Automate | Phase 3 complete | — | — |
| 4 | Findings | Expert | gate3_diff_complete = true | — | — |
| CASCADE GATE | Cascade Gate | Expert | All findings assigned | — | — |
| 4B | Calibration | Expert | Phase 4 + CASCADE GATE | gate4b_calibration_confirmed | — |
| GATE 4B | Calibration Gate | Expert | Phase 4B complete | — | — |
| 5 | CONTRACT DELTA | Expert | gate4b_calibration_confirmed = true | — | — |

**Required frontmatter** — all keys required:

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

**CANNOT BEGIN UNTIL: Start of artifact. (Per Phase Dependency Reference Table: Phase 0 — Unblocked By: Start of artifact.)**

**Inertia risk:** Expert anchors element names to what the connector currently exposes, omitting spec-defined elements the connector has not yet implemented.

Ask first: What connector contract elements does the spec define for `{Topic}` — not what the connector currently exposes, but what the spec says should be there?

Enumerate all in-scope elements as a SCOPE MANIFEST. Derive scope from spec only. All columns required — blank cells are a gate failure condition.

| # | Element Name | Element Type | Spec Clause Key |
|---|--------------|--------------|-----------------|
| | | schema-field \| auth-handshake \| action-payload \| trigger-payload \| error-shape \| metadata | |

**STOP. Do not write GATE 0 until Phase 0 enumeration is complete.**

**GATE 0** (Expert):
- [ ] SCOPE MANIFEST complete — `{N}` elements enumerated
- [ ] Element Type populated — no blank cells
- [ ] Spec Clause Key populated — no blank cells
- [ ] Scope derived from spec — current connector behavior excluded from element selection — not just deprioritized, but excluded entirely — [CONFIRMED / NOT CONFIRMED]

Set `gate0_scope_confirmed: true`.

**STOP. Phase 1A cannot begin until gate0_scope_confirmed = true.**

---

### PHASE 1A — Expected Output (Expert)

**CANNOT BEGIN UNTIL: gate0_scope_confirmed = true. (Per Phase Dependency Reference Table: Phase 1A — Unblocked By: gate0_scope_confirmed = true.)**

**Inertia risk:** Expert anchors Expected Values to what the connector currently returns, writing "expected" values that describe current behavior rather than the spec contract.

Ask first: For each scope element, what does the spec say the expected value should be — stated as a spec-derivable claim, not as a description of what the connector currently returns?

**Step 1 — Commit skeleton** (names, types, spec clauses — Expected Value column blank):

| Element | Element Type | Spec Clause | Expected Value |
|---------|--------------|-------------|----------------|
| (one row per SCOPE MANIFEST entry) | | | <- leave blank |

Record: `SKELETON COMMITTED — {N} rows`

**Step 2 — Fill Expected Values** from spec. The spec is the contract. Do not reference actual output. Do not reference what the connector currently does.

**STOP. Do not write GATE 1 until all Expected Values are filled.**

**GATE 1** (Expert):
- [ ] All Expected Value cells filled — {N}/{N} complete — no blank cells
- [ ] No Spec Clause cells blank
- [ ] Actual output not consulted during Phase 1A — not just ordered after, but not consulted at all — [CONFIRMED / NOT CONFIRMED]
- [ ] Expert runtime knowledge of current connector behavior not applied to Expected Values — not just deprioritized after consideration, but excluded entirely — [CONFIRMED / NOT CONFIRMED]

Set `gate1_isolation_confirmed: true`.

**STOP. Phase 1B cannot begin until gate1_isolation_confirmed = true. Phase 1B owner is Automate — not Expert. The same role that built Phase 1A cannot certify GATE 1B.**

---

### PHASE 1B — INERTIA REGISTER (Automate)

**CANNOT BEGIN UNTIL: gate1_isolation_confirmed = true. (Per Phase Dependency Reference Table: Phase 1B — Unblocked By: gate1_isolation_confirmed = true.) OWNER: AUTOMATE. Expert cannot run or certify this phase.**

**Inertia risk:** The Phase 1A author cannot reliably detect their own inertia contamination. Automate reviews each row for residual contamination.

Ask first: For each Phase 1A row, does the Expected Value appear to reflect what the connector currently does rather than what the spec defines — and if so, which contamination type (NAME, TYPE, or CLAUSE) best characterizes the deviation — not based on assumptions about what the connector ought to return, but based on whether the value is derivable from the spec clause cited?

For each Phase 1A row: does the Expected Value appear to reflect current connector behavior rather than spec derivation? Label each flagged entry as INERTIA-NN. Assign Contamination Type: NAME (identifier or naming mismatch), TYPE (schema or data-type mismatch), CLAUSE (condition, rule, or logic mismatch).

INERTIA REGISTER — all columns required:

| ID | Row | Element | Contamination Type | Inertia Signal? (Yes/No) | Basis | Disposition |
|----|-----|---------|-------------------|--------------------------|-------|-------------|
| INERTIA-01 | | | NAME / TYPE / CLAUSE | | | |

**STOP. Do not write GATE 1B-TM until all rows reviewed.**

**GATE 1B-TM** — Per-Type Conditional Verification Table (Automate certifies). One row per Contamination Type. All cells required — blank cells are a gate failure condition.

| Contamination Type | Entry Count | Entries (INERTIA-NN list) | Every Entry RESOLVED? |
|-------------------|-------------|--------------------------|----------------------|
| NAME | {count} | {INERTIA-NN, ...} | YES — all resolved \| (if 0: *vacuous pass — every INERTIA-NN entry RESOLVED for NAME*) |
| TYPE | {count} | {INERTIA-NN, ...} | YES — all resolved \| (if 0: *vacuous pass — every INERTIA-NN entry RESOLVED for TYPE*) |
| CLAUSE | {count} | {INERTIA-NN, ...} | YES — all resolved \| (if 0: *vacuous pass — every INERTIA-NN entry RESOLVED for CLAUSE*) |

**Per-Type Verification Checklists** — one block per Contamination Type:

*NAME entries only:*
If zero: `vacuous pass — every INERTIA-NN entry RESOLVED for NAME (zero entries).`
- [ ] INERTIA-{NN}: {element} -> RESOLVED

*TYPE entries only:*
If zero: `vacuous pass — every INERTIA-NN entry RESOLVED for TYPE (zero entries).`
- [ ] INERTIA-{NN}: {element} -> RESOLVED

*CLAUSE entries only:*
If zero: `vacuous pass — every INERTIA-NN entry RESOLVED for CLAUSE (zero entries).`
- [ ] INERTIA-{NN}: {element} -> RESOLVED

Each zero-entry type block must still appear with the vacuous-pass declaration. Omitting a zero-count block is a GATE 1B-TM failure condition.

**STOP. Do not write GATE 1B until GATE 1B-TM is complete — all three type rows populated and all per-type checklists present.**

**GATE 1B** (Automate certifies — Expert cannot certify this gate):
- [ ] All `{N}` Phase 1A rows reviewed — none skipped
- [ ] Contamination Type assigned for every flagged row — no blank cells
- [ ] GATE 1B-TM complete — all three type rows populated, no blank cells
- [ ] Per-type checklists complete — each non-empty type block fully checked; each zero-entry type block explicitly declares vacuous pass
- [ ] No unresolved INERTIA-NN entries in the final expected table — [CONFIRMED / NOT CONFIRMED]
- [ ] Per Phase Dependency Reference Table: GATE 1B — Unblocked By: GATE 1B-TM complete. This gate does not close until that condition is satisfied — [CONFIRMED / NOT CONFIRMED]

Set `gate1b_challenge_confirmed: true`.

**STOP. Phase 2 cannot begin until gate1b_challenge_confirmed = true.**

---

### PHASE 2 — Actual Output (Expert)

**CANNOT BEGIN UNTIL: gate1b_challenge_confirmed = true. (Per Phase Dependency Reference Table: Phase 2 — Unblocked By: gate1b_challenge_confirmed = true.)**

Ask first: For each scope element, what does the connector actually return in the current environment — captured now, without consulting the Expected Values already committed above to calibrate your observation?

Run the connector operation. Record actual output for each scope element. Add Actual Value column. Do not modify Expected Values.

| Element | Element Type | Spec Clause | Expected Value | Actual Value |
|---------|--------------|-------------|----------------|--------------|

**GATE 2** (Expert):
- [ ] Actual Value recorded for all `{N}` elements — no blank cells
- [ ] No Expected Value cells modified

Set `gate2_actual_complete: true`.

**STOP. Phase 3 cannot begin until gate2_actual_complete = true.**

---

### PHASE 3 — Diff and Classification (Automate)

**CANNOT BEGIN UNTIL: gate2_actual_complete = true. (Per Phase Dependency Reference Table: Phase 3 — Unblocked By: gate2_actual_complete = true.)**

Ask first: For each element, does the actual value match the expected value — not whether it seems reasonable or close, but whether it satisfies the spec contract exactly — and if not, does the deviation affect contract correctness (breaking), integration quality (degraded), or only surface presentation (cosmetic)?

Classify each row: MATCH | MISMATCH. For MISMATCH rows: assign Severity (breaking | degraded | cosmetic).

**STOP. Do not write root cause hypotheses in Phase 3. Root causes are Phase 4. Root cause text in Phase 3 output = immediate GATE 3 failure condition.**

| Element | Element Type | Spec Clause | Expected Value | Actual Value | Match? | Severity |
|---------|--------------|-------------|----------------|--------------|--------|----------|

**GATE 3** (Automate):
- [ ] Every row classified MATCH or MISMATCH — no blank Match? cells
- [ ] No Severity cells blank on MISMATCH rows
- [ ] No Spec Clause cells blank on any row
- [ ] No Element Type cells blank on any row
- [ ] No root cause hypotheses in Phase 3 output — confirmed absent — [CONFIRMED / NOT CONFIRMED]

Set `gate3_diff_complete: true`.

**STOP. Phase 4 cannot begin until gate3_diff_complete = true.**

---

## INERTIA CORRECTION ROUTES

Consult this section before assigning any finding to a cascade path in the CASCADE GATE. This reference consolidates all inertia correction paths into one auditable location. The CASCADE GATE is the per-finding execution tracker that references these routes by name — do not redefine routes within the CASCADE GATE. The CASCADE GATE and this section have non-overlapping structural functions: this section defines what each route consists of; the CASCADE GATE records which route each finding takes.

| Route | Trigger Condition | Complete Path | Upstream Anchor | Must NOT Visit |
|-------|------------------|--------------|-----------------|----------------|
| ROUTE-A | In-boundary finding: element is present in the SCOPE MANIFEST; deviation originates in expected-value derivation or implementation divergence — no scope amendment required | Phase 4 -> CASCADE GATE (ROUTE-A) -> Phase 4B -> GATE 4B -> Phase 5 | Phase 4 (correction is within already-scoped elements) | **Phase 0 — must NOT re-open scope enumeration. ROUTE-A findings do not require scope amendment.** |
| ROUTE-B | Out-of-boundary discovery: element is absent from the SCOPE MANIFEST; the spec defines an element Phase 0 missed — scope amendment required before Phase 5 | Phase 4 -> CASCADE GATE (ROUTE-B) -> Phase 0 amendment -> GATE 0 (re-confirm) -> Phase 1A (re-fill affected rows) -> GATE 1 (re-confirm) -> Phase 1B (re-review added rows) -> GATE 1B -> resume Phase 4 -> Phase 4B -> GATE 4B -> Phase 5 | Phase 0 (GATE 0 must be re-confirmed after scope amendment before proceeding downstream) | **Phase 5 — must NOT proceed to CONTRACT DELTA until Phase 0 amendment complete and GATE 0 re-confirmed.** |

---

### PHASE 4 — Findings (Expert)

**CANNOT BEGIN UNTIL: gate3_diff_complete = true. (Per Phase Dependency Reference Table: Phase 4 — Unblocked By: gate3_diff_complete = true.) Consult INERTIA CORRECTION ROUTES above before assigning cascade paths in the CASCADE GATE.**

Ask first: For each MISMATCH, what connector-layer mechanism most plausibly explains why the actual value diverges from the expected value — and if the root cause is inertia-spec-drift, what specific downstream consequence persists for which user, flow, or contract guarantee if this finding is never resolved?

For each MISMATCH row, produce a finding scaffold. The "Harm if unresolved:" field is mandatory for all findings where Root Cause includes an inertia classification.

```
F-{NN}: {Element Name}
  Severity:           {from Phase 3 — do not reassign here}
  Spec Ref:           {Spec Clause}
  Root Cause:         {connector mechanism — field-mapping-delta | auth-handshake-mismatch | action-payload-drift | trigger-payload-gap | error-shape-change | metadata-convention-gap | inertia-spec-drift — "unknown" alone not accepted}
  Harm if unresolved: {specific affected user, flow, or contract guarantee} will experience {nature of persistent deviation} — e.g., "Automate flows consuming {element} will receive {wrong-value} until spec clause {X} is patched in connector version {V}"
  Resolution:         {specific investigative step — names what to investigate; "investigate further" alone not accepted}
```

"Harm if unresolved:" fill rules:
- Required for every finding where Root Cause = inertia-spec-drift.
- Field is structurally distinct from Root Cause — it is a separate labeled line.
- Must name: (1) the specific affected user, consumer, flow, or contract guarantee; (2) the nature of the persistent deviation if the finding is never resolved.
- Generic entries such as "spec drift will continue" or "the bug will remain" do not pass.

**Phase 4 gate check for harm fields:**
- [ ] Every inertia-classified finding has a populated "Harm if unresolved:" field — [CONFIRMED / NOT CONFIRMED]
- [ ] No "Harm if unresolved:" field uses generic language without naming specific affected entity — [CONFIRMED / NOT CONFIRMED]

`inertia-spec-drift` is a valid root cause when the connector was not updated to follow a known spec change. Name the specific clause and the connector version where the gap was introduced.

**STOP. Phase 4B is a standalone phase. After all findings written and Phase 4 gate check confirmed, proceed to CASCADE GATE using INERTIA CORRECTION ROUTES table above. Do not begin calibration inside Phase 4.**

---

### CASCADE GATE (Expert)

**CANNOT BEGIN UNTIL: Phase 4 findings complete and Phase 4 gate check confirmed. Select route per finding from INERTIA CORRECTION ROUTES table above.**

| Finding | Severity | Route | Path | Must NOT Visit |
|---------|----------|-------|------|----------------|
| F-{NN} | | ROUTE-A (in-boundary: no scope gap) | Phase 4B -> Phase 5 | **Phase 0 — must NOT re-open scope enumeration for an in-boundary omission** |
| F-{NN} | | ROUTE-B (out-of-boundary: scope gap) | Phase 0 amendment -> Phase 1A -> resume | **Phase 5 — must NOT proceed to CONTRACT DELTA without Phase 0 amendment** |

**CASCADE GATE:**
- [ ] Every finding assigned ROUTE-A or ROUTE-B per INERTIA CORRECTION ROUTES table — no unassigned rows
- [ ] Must NOT Visit populated for every row — no blank cells
- [ ] No ROUTE-A finding has re-opened Phase 0 — [CONFIRMED / NOT CONFIRMED]
- [ ] No ROUTE-B finding has proceeded to Phase 5 without completing Phase 0 amendment — [CONFIRMED / NOT CONFIRMED]

**STOP. Phase 4B cannot begin until CASCADE GATE is complete.**

---

### PHASE 4B — Calibration (Expert — standalone phase; do not merge with Phase 4)

**CANNOT BEGIN UNTIL: Phase 4 complete AND CASCADE GATE signed off. (Per Phase Dependency Reference Table: Phase 4B — Unblocked By: Phase 4 complete AND CASCADE GATE complete.) Phase 5 cannot begin until gate4b_calibration_confirmed = true.**

Ask first: Is the severity distribution across findings reasonable — is there at least one non-breaking finding, or is every finding individually justifiable at breaking due to a specific contract guarantee it violates?

Severity tally (complete before writing any calibration assessment):

| Severity | Count |
|----------|-------|
| breaking | |
| degraded | |
| cosmetic | |

For each finding individually: justify its severity assignment. Group justification ("all breaking because...") = gate failure condition.

**STOP. Do not write GATE 4B until individual justifications are written for every finding.**

**GATE 4B** (Expert):
- [ ] Severity tally completed before assessments
- [ ] Each finding individually justified at its assigned level
- [ ] Distribution reasonable — at least two levels represented, or single level individually justified

Set `gate4b_calibration_confirmed: true`.

**STOP. Phase 5 cannot begin until gate4b_calibration_confirmed = true.**

---

### PHASE 5 — CONTRACT DELTA (Expert)

**CANNOT BEGIN UNTIL: gate4b_calibration_confirmed = true. (Per Phase Dependency Reference Table: Phase 5 — Unblocked By: gate4b_calibration_confirmed = true.) ROUTE-B findings: Phase 0 amendment must be complete before this phase.**

Ask first: For each finding, does the spec need to be amended because the spec is wrong, or does the implementation need to be corrected because the spec is right — and which amendment type most precisely describes the required change?

| Finding | Spec Clause | Priority | Amendment Type | Required Change |
|---------|-------------|----------|----------------|-----------------|

Priority: breaking->P1, degraded->P2, cosmetic->P3 (from Phase 4B). Blank Priority cells not accepted.
Amendment Type: add-field \| remove-field \| change-type \| change-enum \| change-error-shape \| change-auth-flow. Blank Amendment Type cells not accepted.

**CONTRACT VERDICT:**
- breaking: {N}, degraded: {N}, cosmetic: {N}
- Verdict: PASS (zero breaking) \| DEGRADED (no breaking, some degraded) \| FAIL (one or more breaking)

**Phase 5 does not close until every ROUTE-B finding has a completed Phase 0 amendment on record. This gate does not close until the Phase Dependency Reference Table condition is satisfied — gate4b_calibration_confirmed = true — [CONFIRMED / NOT CONFIRMED]**
