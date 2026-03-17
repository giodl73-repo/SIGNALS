# trace-contract — Round 9 Variations (v9 Rubric, C-01–C-34, denominator /26)

**New criteria targeted:** C-32 (per-type conditional verification checklist), C-33 (zero-entry vacuous-pass declaration), C-34 (cascade-path negative route prohibition).

**Single-axis variations (V-01 to V-04):** Phrasing Register, Output Format, Lifecycle Emphasis, Inertia Framing.
**Combination variation (V-05):** Full integration of all four axes.

**R9 Platinum gap note:** V-05 achieves 25/26, missing only C-17. A composite merging V-01's "Ask first: [question]..." interrogative structure (distinct sentence preceding each fill form) with V-05's full gate architecture reaches 26/26.

---

## V-01 — Phrasing Register (Interrogative)

**Variation axis:** Phrasing register — "Ask first: [question]..." sentences appear as a distinct preceding line before every fill form. The interrogative is a complete sentence, not a label or gate item. It precedes the fill form, not the gate.

**Hypothesis:** A distinct interrogative sentence before each fill form forces the model to commit a stated answer before executing the fill operation, satisfying C-17 (interrogative sentence present as a distinct element before the fill form). INERTIA-NN numbering and the GATE 1B-TM ask-first framing deliver C-32 and C-33 without requiring a separate format enforcement layer. Cascade path "Must NOT visit" asks satisfy C-34 through stated prohibition rather than table structure.

---

You are running **trace-contract** for Topic: `{Topic}`.

Stock roles: **Expert** (Connectors contract expert), **Automate** (connector automation specialist). Expert constructs expected output (Phase 1A). Automate reviews for contamination (Phase 1B) and classifies the diff (Phase 3). Role separation is a structural requirement: the same role that builds a phase cannot certify the gate that validates it where role separation is specified.

Ask first: What is the normative source for this contract — which spec section, contract clause, or PRINCIPLES.md rule defines the expected behavior for `{Topic}`?

---

**Frontmatter** — required at artifact top; update gate keys as each gate passes:

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

Ask first: What connector contract elements are defined by the spec for `{Topic}` — not what the connector currently exposes, but what the spec says should be there?

Enumerate all in-scope elements as a SCOPE MANIFEST. Derive scope from spec only. All columns required — blank cells are a gate failure condition.

| # | Element Name | Element Type | Spec Clause Key |
|---|--------------|--------------|-----------------|
| | | schema-field \| auth-handshake \| action-payload \| trigger-payload \| error-shape \| metadata | |

**GATE 0** (Expert):
- [ ] SCOPE MANIFEST complete — `{N}` elements enumerated
- [ ] Element Type populated — no blank cells
- [ ] Spec Clause Key populated — no blank cells
- [ ] Scope derived from spec — current connector behavior excluded from element selection — not just deprioritized, but excluded from scope derivation entirely — [CONFIRMED / NOT CONFIRMED]

Set `gate0_scope_confirmed: true`.

---

### PHASE 1A — Expected Output (Expert)

Ask first: For each scope element, what does the spec say the expected value should be — stated as a spec-derivable claim, not as a description of what the connector currently returns?

**Step 1 — Commit skeleton** (names, types, spec clauses — Expected Value column blank):

| Element | Element Type | Spec Clause | Expected Value |
|---------|--------------|-------------|----------------|
| (one row per SCOPE MANIFEST entry) | | | <- leave blank |

Record: `SKELETON COMMITTED — {N} rows`

**Step 2 — Fill Expected Values** from spec. The spec is the contract. Do not reference actual output. Do not reference what you know the connector currently does.

**GATE 1** (Expert):
- [ ] All Expected Value cells filled — {N}/{N} complete — no blank cells
- [ ] No Spec Clause cells blank in expected table rows
- [ ] Actual output not consulted during Phase 1A — not just ordered after, but not consulted at all — [CONFIRMED / NOT CONFIRMED]
- [ ] Expert runtime knowledge of current connector behavior not applied to Expected Values — not just deprioritized, but excluded entirely from expected value derivation — [CONFIRMED / NOT CONFIRMED]

Set `gate1_isolation_confirmed: true`.

---

### PHASE 1B — Challenge Review (Automate)

Ask first: Which Phase 1A rows show evidence that the Expected Value was derived from what the connector currently does, rather than from what the spec defines?

Owner: Automate. Expert built Phase 1A; Automate must own Phase 1B. The same role that built Phase 1A cannot certify GATE 1B.

Label each flagged entry as INERTIA-NN. Assign a Contamination Type to each: NAME (identifier or naming mismatch), TYPE (schema or data-type mismatch), CLAUSE (condition, rule, or logic mismatch).

CHALLENGE LOG — all columns required:

| ID | Row | Element | Contamination Type | Inertia Signal? | Basis | Disposition |
|----|-----|---------|-------------------|-----------------|-------|-------------|
| INERTIA-01 | | | NAME / TYPE / CLAUSE | Yes / No | | |

Ask first: For each Contamination Type (NAME, TYPE, CLAUSE) — are there zero entries of that type in the CHALLENGE LOG? If zero, declare: *vacuous pass — every INERTIA-NN entry RESOLVED for {TYPE} (zero entries).*

**GATE 1B-TM** — Per-Type Conditional Verification (Automate certifies):

| Contamination Type | Entry Count | Entries | Every Entry RESOLVED? |
|-------------------|-------------|---------|----------------------|
| NAME | {count} | INERTIA-NN, ... | YES — all resolved \| (if 0: vacuous pass — every INERTIA-NN entry RESOLVED for NAME) |
| TYPE | {count} | INERTIA-NN, ... | YES — all resolved \| (if 0: vacuous pass — every INERTIA-NN entry RESOLVED for TYPE) |
| CLAUSE | {count} | INERTIA-NN, ... | YES — all resolved \| (if 0: vacuous pass — every INERTIA-NN entry RESOLVED for CLAUSE) |

**GATE 1B** (Automate certifies — Expert cannot certify this gate):
- [ ] All `{N}` Phase 1A rows reviewed — none skipped
- [ ] Contamination Type assigned for every flagged row — no blank cells
- [ ] GATE 1B-TM complete — count and resolution status for each type populated
- [ ] No unresolved INERTIA-NN entries in the final expected table — [CONFIRMED / NOT CONFIRMED]

Set `gate1b_challenge_confirmed: true`.

---

### PHASE 2 — Actual Output (Expert)

Ask first: Is the connector operation for `{Topic}` runnable in this context? If not, what is the specific blocker?

Run the connector operation. Record actual output for each scope element. Add Actual Value column. Do not modify Expected Values.

| Element | Element Type | Spec Clause | Expected Value | Actual Value |
|---------|--------------|-------------|----------------|--------------|

**GATE 2** (Expert):
- [ ] Actual Value recorded for all `{N}` elements — no blank cells
- [ ] No Expected Value cells modified

Set `gate2_actual_complete: true`.

---

### PHASE 3 — Diff and Classification (Automate)

Ask first: For each element, do the Expected Value and Actual Value match exactly — or is there any deviation, including cosmetic differences in naming, casing, or whitespace?

Classify each row: MATCH | MISMATCH. For MISMATCH rows: assign Severity (breaking | degraded | cosmetic). Root cause hypotheses go in Phase 4 — do not write them here.

| Element | Element Type | Spec Clause | Expected Value | Actual Value | Match? | Severity |
|---------|--------------|-------------|----------------|--------------|--------|----------|

**GATE 3** (Automate):
- [ ] Every row classified MATCH or MISMATCH — no blank Match? cells
- [ ] No Severity cells blank on MISMATCH rows
- [ ] No Spec Clause cells blank on any row
- [ ] No Element Type cells blank on any row
- [ ] No root cause hypotheses in Phase 3 output — [CONFIRMED / NOT CONFIRMED]

Set `gate3_diff_complete: true`.

---

### PHASE 4 — Findings (Expert)

Ask first: For each MISMATCH — what connector-domain mechanism explains the deviation? State a plausible mechanism before writing the scaffold.

For each MISMATCH row, produce a finding scaffold:

```
F-{NN}: {Element Name}
  Severity:    {from Phase 3 — do not reassign here}
  Spec Ref:    {Spec Clause}
  Root Cause:  {connector mechanism — field-mapping-delta | auth-handshake-mismatch | action-payload-drift | trigger-payload-gap | error-shape-change | metadata-convention-gap | inertia-spec-drift — "unknown" alone not accepted}
  Resolution:  {specific investigative step — names what to investigate; "investigate further" alone not accepted}
```

---

### CASCADE PATHS — Routing Gate

Ask first: For each finding, which cascade path applies — is the finding in-boundary (no scope gap) or out-of-boundary (scope gap detected)?

Ask first: For each labeled cascade path, which upstream phase must that path NOT re-open?

| Finding | Cascade Path | Route | Must NOT Visit |
|---------|-------------|-------|----------------|
| F-{NN} | CASCADE-A (in-boundary: no scope gap) | Phase 4B -> Phase 5 | Phase 0 — do not re-open scope enumeration for an in-boundary omission |
| F-{NN} | CASCADE-B (out-of-boundary: scope gap detected) | Phase 0 amendment -> Phase 1A -> resume | Phase 5 — do not proceed to CONTRACT DELTA without Phase 0 amendment |

**CASCADE GATE:**
- [ ] Each finding assigned to CASCADE-A or CASCADE-B — no unassigned findings
- [ ] No CASCADE-A finding initiates a Phase 0 re-open — [CONFIRMED / NOT CONFIRMED]
- [ ] No CASCADE-B finding proceeds to Phase 5 without completing Phase 0 amendment — [CONFIRMED / NOT CONFIRMED]

---

### PHASE 4B — Calibration (Expert — standalone phase; do not merge with Phase 4)

Ask first: Is the severity distribution across findings reasonable — is there at least one non-breaking finding, or are all findings individually justifiable at breaking?

Severity tally (complete before writing any calibration assessment):

| Severity | Count |
|----------|-------|
| breaking | |
| degraded | |
| cosmetic | |

For each finding individually: justify its severity. Group justification ("all breaking because...") = gate failure condition.

**GATE 4B** (Expert):
- [ ] Severity tally completed before assessments
- [ ] Each finding individually justified at its assigned level — [ ] each element individually justified at that level
- [ ] Distribution reasonable — at least two levels represented, or single level individually justified

Set `gate4b_calibration_confirmed: true`.

---

### PHASE 5 — CONTRACT DELTA (Expert)

Ask first: For each finding, does the spec need to be amended, or does the implementation need to be corrected — and are both options considered before choosing one?

| Finding | Spec Clause | Priority | Amendment Type | Required Change |
|---------|-------------|----------|----------------|-----------------|

Priority: breaking->P1, degraded->P2, cosmetic->P3 (from Phase 4B — no priority assignment without Phase 4B completion).
Amendment Type: add-field \| remove-field \| change-type \| change-enum \| change-error-shape \| change-auth-flow. Blank Amendment Type cells not accepted.

---

---

## V-02 — Output Format (GATE 1B-TM Table Architecture)

**Variation axis:** Output format — GATE 1B-TM is a formal verification table with per-type rows, entry counts, and inline vacuous-pass cells. All compliance is enforced as a table-parsing condition rather than prose instruction. The cascade prohibition is a table column, not a prose statement.

**Hypothesis:** Pre-printing the GATE 1B-TM table schema with NAME/TYPE/CLAUSE rows and an "Every Entry RESOLVED?" column makes type-class failures visible as table-row failures (C-32). The "if 0: vacuous pass" text embedded in the table cell eliminates vacuous-pass ambiguity at the moment of writing (C-33). A separate CASCADE REGISTRY table with a "Must NOT Visit" column converts routing prohibition into a column-filling obligation (C-34). No criterion requires prose-only compliance.

---

You are running **trace-contract** for Topic: `{Topic}`.

Stock roles: Expert (Connectors contract expert), Automate (connector automation specialist). Expert constructs expected output (Phase 1A). Automate reviews for contamination (Phase 1B) and classifies the diff (Phase 3).

---

**Required frontmatter** — begin artifact with this block; fill gate key values as each gate passes; do not omit any key:

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

**SCOPE MANIFEST** — Phase 0 output (Expert). All cells required; blank cells are a gate failure condition.

| # | Element Name | Element Type | Spec Clause Key |
|---|--------------|--------------|-----------------|
| | | schema-field \| auth-handshake \| action-payload \| trigger-payload \| error-shape \| metadata | |

GATE 0 — all items required before Phase 1A begins:
- [ ] `{N}` elements enumerated from spec
- [ ] Element Type populated — no blank cells
- [ ] Spec Clause Key populated — no blank cells
- [ ] Scope anchored to spec only — current connector behavior excluded from element selection — not just deprioritized, but excluded entirely — [CONFIRMED / NOT CONFIRMED]

Update `gate0_scope_confirmed: true`.

---

**EXPECTED TABLE** — Phase 1A output (Expert). Two-step construction. All cells required.

Step 1 — skeleton (fill Element Name, Element Type, Spec Clause; leave Expected Value blank):

| Element | Element Type | Spec Clause | Expected Value |
|---------|--------------|-------------|----------------|
| | schema-field \| auth-handshake \| action-payload \| trigger-payload \| error-shape \| metadata | | <- blank |

Record: `SKELETON COMMITTED — {N} rows`

Step 2 — fill Expected Value for each committed row from spec only.

GATE 1 — all items required before Phase 1B begins:
- [ ] All Expected Value cells filled — {N}/{N} complete — no blank cells
- [ ] No Spec Clause cells blank in expected table rows
- [ ] Actual output not consulted — not just ordered after, but not consulted at all — [CONFIRMED / NOT CONFIRMED]
- [ ] Expert runtime knowledge of current connector behavior not applied to Expected Values — not just deprioritized, but excluded entirely — [CONFIRMED / NOT CONFIRMED]

Update `gate1_isolation_confirmed: true`.

---

**CHALLENGE LOG** — Phase 1B output (Owner: Automate — see frontmatter `gate1b_owner`). All columns required. Label each flagged entry as INERTIA-NN.

| ID | Row | Element | Contamination Type | Inertia Signal? (Yes/No) | Basis | Disposition |
|----|-----|---------|-------------------|--------------------------|-------|-------------|
| INERTIA-01 | | | NAME / TYPE / CLAUSE | | | |

---

**GATE 1B-TM** — Per-Type Conditional Verification Table (Automate certifies). One row per Contamination Type. Complete all cells; blank cells are a gate failure condition.

| Contamination Type | Description | Entry Count | Entries (INERTIA-NN list) | Every Entry RESOLVED? |
|-------------------|-------------|-------------|--------------------------|----------------------|
| NAME | Identifier or naming mismatch | {count} | {INERTIA-NN, ...} | YES — all resolved \| (if 0: vacuous pass — every INERTIA-NN entry RESOLVED for NAME) |
| TYPE | Schema or data-type mismatch | {count} | {INERTIA-NN, ...} | YES — all resolved \| (if 0: vacuous pass — every INERTIA-NN entry RESOLVED for TYPE) |
| CLAUSE | Condition, rule, or logic mismatch | {count} | {INERTIA-NN, ...} | YES — all resolved \| (if 0: vacuous pass — every INERTIA-NN entry RESOLVED for CLAUSE) |

**Per-Type Verification Checklists** — one block per Contamination Type, scoped to entries of that type only:

*NAME entries only:*
- [ ] INERTIA-{NN}: {element} -> RESOLVED
- If zero entries: `(vacuous pass — every INERTIA-NN entry RESOLVED for NAME)`

*TYPE entries only:*
- [ ] INERTIA-{NN}: {element} -> RESOLVED
- If zero entries: `(vacuous pass — every INERTIA-NN entry RESOLVED for TYPE)`

*CLAUSE entries only:*
- [ ] INERTIA-{NN}: {element} -> RESOLVED
- If zero entries: `(vacuous pass — every INERTIA-NN entry RESOLVED for CLAUSE)`

GATE 1B — all items required before Phase 2 begins:
- [ ] All `{N}` Phase 1A rows reviewed — none skipped
- [ ] GATE 1B-TM complete — every row populated, no blank cells
- [ ] All per-type checklists present — each non-empty type block fully checked; each zero-entry type block explicitly declares vacuous pass
- [ ] No unresolved INERTIA-NN entries in the final expected table — [CONFIRMED / NOT CONFIRMED]

Update `gate1b_challenge_confirmed: true`.

---

**ACTUAL TABLE** — Phase 2 output (Expert). Add Actual Value column; do not modify Expected Values.

| Element | Element Type | Spec Clause | Expected Value | Actual Value |
|---------|--------------|-------------|----------------|--------------|

GATE 2:
- [ ] Actual Value populated for all `{N}` elements — no blank cells
- [ ] No Expected Value cells modified

Update `gate2_actual_complete: true`.

---

**DIFF TABLE** — Phase 3 output (Automate). Classification only — no root cause hypotheses. All columns required.

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

**FINDING SCAFFOLDS** — Phase 4 output (Expert). One scaffold per MISMATCH row. All fields required.

```
F-{NN}: {Element Name}
  Severity:    {from Phase 3 diff table — do not re-assign}
  Spec Ref:    {Spec Clause}
  Root Cause:  {domain mechanism — field-mapping-delta | auth-handshake-mismatch | action-payload-drift | trigger-payload-gap | error-shape-change | metadata-convention-gap | inertia-spec-drift — "unknown" alone not accepted}
  Resolution:  {specific investigative step — not "investigate further" alone}
```

---

**CASCADE REGISTRY** — Phase 4 routing table (Expert). One row per finding. All columns required; blank Must NOT Visit cells are a gate failure condition.

| Finding | Cascade Path | Route | Must NOT Visit | Status |
|---------|-------------|-------|----------------|--------|
| F-{NN} | CASCADE-A (in-boundary: no scope gap) | Phase 4 -> Phase 4B -> Phase 5 | Phase 0 — must NOT re-open scope enumeration | VALID / VIOLATION |
| F-{NN} | CASCADE-B (out-of-boundary: scope gap) | Phase 4 -> Phase 0 amendment -> Phase 1A | Phase 5 — must NOT proceed to CONTRACT DELTA | VALID / VIOLATION |

CASCADE GATE:
- [ ] Every finding assigned CASCADE-A or CASCADE-B — no unassigned rows
- [ ] Must NOT Visit populated for every row — no blank cells
- [ ] No CASCADE-A finding has Status = VIOLATION (Phase 0 re-opened)
- [ ] No CASCADE-B finding has Status = VIOLATION (Phase 5 entered without Phase 0 amendment)

---

**CALIBRATION PHASE** — Phase 4B output (Expert — separate section; do not merge with Phase 4 findings).

Severity tally table (required before calibration assessments):

| Severity | Count | Gate: Each Finding Individually Justified |
|----------|-------|------------------------------------------|
| breaking | | [ ] each finding individually justified at breaking |
| degraded | | [ ] each finding individually justified at degraded |
| cosmetic | | [ ] each finding individually justified at cosmetic |

Group justification ("all breaking because...") = gate failure condition.

GATE 4B:
- [ ] Tally table populated — counts confirmed
- [ ] Individual justification checkbox checked for each severity level present
- [ ] Distribution reasonable — at least two levels or single level individually justified

Update `gate4b_calibration_confirmed: true`.

---

**CONTRACT DELTA** — Phase 5 output (Expert). All columns required; blank Priority or Amendment Type cells are a gate failure condition.

| Finding | Spec Clause | Priority | Amendment Type | Required Change |
|---------|-------------|----------|----------------|-----------------|

Priority: breaking->P1, degraded->P2, cosmetic->P3 (from Phase 4B calibration).
Amendment Type: add-field \| remove-field \| change-type \| change-enum \| change-error-shape \| change-auth-flow.

---

---

## V-03 — Lifecycle Emphasis (Cascade Prohibition)

**Variation axis:** Lifecycle emphasis — every phase transition carries a STOP marker and a blocking guard. CASCADE paths are entries in the phase dependency chain table, each with an explicit "Must NOT Visit" prohibition column. Cascade prohibition is a lifecycle constraint, not a routing annotation.

**Hypothesis:** Adding CASCADE-A and CASCADE-B as named entries in the phase dependency chain with "Must NOT Visit" columns filled like gate keys converts routing prohibition from implicit correctness into an active structural constraint that must be satisfied before the next phase begins (C-34). INERTIA-NN numbering in the challenge log and "every INERTIA-NN entry RESOLVED" as the gate closure phrase delivers C-33 through the lifecycle gate language rather than a table cell. GATE 1B-TM appears as a named lifecycle gate with three per-type sub-checks (C-32).

---

You are running **trace-contract** for Topic: `{Topic}`.

Stock roles: Expert (Connectors contract expert), Automate (connector automation specialist).

**Phase dependency chain** — read before beginning. No phase begins until the gate before it fires. CASCADE paths are lifecycle routes with named prohibitions.

| Phase | Name | Owner | Unblocked By | Gate Key Set | Must NOT Visit |
|-------|------|-------|-------------|-------------|----------------|
| 0 | Scope Enumeration | Expert | Start of artifact | gate0_scope_confirmed | — |
| GATE 0 | Scope Gate | Expert | Phase 0 complete | — | — |
| 1A | Expected Output | Expert | gate0_scope_confirmed = true | gate1_isolation_confirmed | — |
| GATE 1 | Isolation Gate | Expert | Phase 1A complete | — | — |
| 1B | Challenge Review | **Automate** | gate1_isolation_confirmed = true | (-> GATE 1B-TM) | — |
| GATE 1B-TM | Per-Type Verification | **Automate** | Phase 1B CHALLENGE LOG complete | — | — |
| GATE 1B | Challenge Gate | **Automate** | GATE 1B-TM complete | gate1b_challenge_confirmed | — |
| 2 | Actual Output | Expert | gate1b_challenge_confirmed = true | gate2_actual_complete | — |
| GATE 2 | Actual Gate | Expert | Phase 2 complete | — | — |
| 3 | Diff + Classification | Automate | gate2_actual_complete = true | gate3_diff_complete | — |
| GATE 3 | Diff Gate | Automate | Phase 3 complete | — | — |
| 4 | Findings | Expert | gate3_diff_complete = true | — | — |
| CASCADE-A | In-boundary route | Expert | F-{NN} assigned CASCADE-A | — | **Phase 0 — must NOT re-open for in-boundary omission** |
| CASCADE-B | Out-of-boundary route | Expert | F-{NN} assigned CASCADE-B | — | **Phase 5 — must NOT proceed to CONTRACT DELTA without Phase 0 amendment** |
| CASCADE GATE | Cascade Gate | Expert | All findings assigned | — | — |
| 4B | Calibration | Expert | Phase 4 complete + CASCADE GATE | gate4b_calibration_confirmed | — |
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

**CANNOT BEGIN UNTIL: gate0_scope_confirmed = true.**

**Step 1 — Commit skeleton** (names, types, spec clauses — Expected Value column blank):

| Element | Element Type | Spec Clause | Expected Value |
|---------|--------------|-------------|----------------|
| (one row per SCOPE MANIFEST entry) | | | <- leave blank |

Record: `SKELETON COMMITTED — {N} rows`

**Step 2 — Fill Expected Values** from spec. Do not reference actual output. Do not reference what you know the connector currently does.

**STOP. Do not write GATE 1 until all Expected Values are filled.**

**GATE 1** (Expert):
- [ ] All Expected Value cells filled — {N}/{N} complete
- [ ] No Spec Clause cells blank in expected table rows
- [ ] Actual output not consulted during Phase 1A — not just ordered after, but not consulted at all — [CONFIRMED / NOT CONFIRMED]
- [ ] Expert runtime knowledge of current connector behavior not applied to Expected Values — not just deprioritized, but excluded entirely — [CONFIRMED / NOT CONFIRMED]

Set `gate1_isolation_confirmed: true`.

**STOP. Phase 1B cannot begin until gate1_isolation_confirmed = true. Phase 1B owner is Automate — not Expert. The same role that built Phase 1A cannot certify Phase 1B.**

---

### PHASE 1B — Challenge Review (Automate)

**CANNOT BEGIN UNTIL: gate1_isolation_confirmed = true. OWNER: AUTOMATE. Expert cannot run or certify this phase.**

For each Phase 1A row: does the Expected Value appear to reflect current connector behavior rather than spec derivation? Label each flagged entry as INERTIA-NN and assign a Contamination Type.

CHALLENGE LOG — all columns required:

| ID | Row | Element | Contamination Type (NAME / TYPE / CLAUSE) | Inertia Signal? (Yes/No) | Basis | Disposition |
|----|-----|---------|------------------------------------------|--------------------------|-------|-------------|
| INERTIA-01 | | | | | | |

**STOP. Do not write GATE 1B-TM until CHALLENGE LOG is complete for all rows.**

**GATE 1B-TM** — Per-Type Conditional Verification. One block per Contamination Type, scoped to entries of that type only.

*NAME entries only:*
- Count: {N}. If zero: `vacuous pass — every INERTIA-NN entry RESOLVED for NAME.`
- [ ] INERTIA-{NN}: {element} -> RESOLVED

*TYPE entries only:*
- Count: {N}. If zero: `vacuous pass — every INERTIA-NN entry RESOLVED for TYPE.`
- [ ] INERTIA-{NN}: {element} -> RESOLVED

*CLAUSE entries only:*
- Count: {N}. If zero: `vacuous pass — every INERTIA-NN entry RESOLVED for CLAUSE.`
- [ ] INERTIA-{NN}: {element} -> RESOLVED

If a type has zero entries, the block must still appear with the vacuous-pass declaration. Omitting a zero-count block is a GATE 1B-TM failure condition.

**STOP. Do not write GATE 1B until GATE 1B-TM is complete for all three types (including zero-entry declarations).**

**GATE 1B** (Automate certifies — Expert cannot certify this gate):
- [ ] All `{N}` Phase 1A rows reviewed — none skipped
- [ ] GATE 1B-TM complete — all three type blocks present, including zero-entry declarations
- [ ] No unresolved INERTIA-NN entries in the final expected table — [CONFIRMED / NOT CONFIRMED]

Set `gate1b_challenge_confirmed: true`.

**STOP. Phase 2 cannot begin until gate1b_challenge_confirmed = true.**

---

### PHASE 2 — Actual Output (Expert)

**CANNOT BEGIN UNTIL: gate1b_challenge_confirmed = true.**

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

**CANNOT BEGIN UNTIL: gate2_actual_complete = true.**

Classify each row: MATCH | MISMATCH. For MISMATCH rows: assign Severity (breaking | degraded | cosmetic).

**STOP. Do not write root cause hypotheses in Phase 3. Root causes are Phase 4. Root cause text in Phase 3 output = immediate GATE 3 failure condition.**

| Element | Element Type | Spec Clause | Expected Value | Actual Value | Match? | Severity |
|---------|--------------|-------------|----------------|--------------|--------|----------|

**GATE 3** (Automate):
- [ ] Every row classified MATCH or MISMATCH
- [ ] No Severity cells blank on MISMATCH rows
- [ ] No Spec Clause cells blank on any row
- [ ] No Element Type cells blank on any row
- [ ] No root cause hypotheses in Phase 3 output — confirmed absent — [CONFIRMED / NOT CONFIRMED]

Set `gate3_diff_complete: true`.

**STOP. Phase 4 cannot begin until gate3_diff_complete = true.**

---

### PHASE 4 — Findings (Expert)

**CANNOT BEGIN UNTIL: gate3_diff_complete = true.**

For each MISMATCH, produce a finding scaffold:

```
F-{NN}: {Element Name}
  Severity:    {from Phase 3 — do not reassign here}
  Spec Ref:    {Spec Clause}
  Root Cause:  {connector mechanism — field-mapping-delta | auth-handshake-mismatch | action-payload-drift | trigger-payload-gap | error-shape-change | metadata-convention-gap | inertia-spec-drift — "unknown" alone not accepted}
  Resolution:  {specific next step — names what to investigate; "investigate further" alone not accepted}
```

**STOP. Phase 4B is a standalone phase. Do not begin calibration inside Phase 4. After all findings are written, proceed to CASCADE GATE before Phase 4B.**

---

### CASCADE GATE (Expert)

**CANNOT BEGIN UNTIL: Phase 4 findings complete.**

Assign each finding to a cascade path. Each path prohibits visiting a named upstream phase.

| Finding | Severity | Cascade Path | Route | Must NOT Visit |
|---------|----------|-------------|-------|----------------|
| F-{NN} | | CASCADE-A (in-boundary) | Phase 4B -> Phase 5 | **Phase 0 — must NOT re-open scope enumeration for an in-boundary omission** |
| F-{NN} | | CASCADE-B (out-of-boundary) | Phase 0 -> Phase 1A -> resume | **Phase 5 — must NOT proceed to CONTRACT DELTA without Phase 0 amendment** |

**CASCADE GATE:**
- [ ] Every finding assigned CASCADE-A or CASCADE-B — no unassigned rows
- [ ] No CASCADE-A finding re-opens Phase 0 — [CONFIRMED / NOT CONFIRMED]
- [ ] No CASCADE-B finding proceeds to Phase 5 without a completed Phase 0 amendment — [CONFIRMED / NOT CONFIRMED]

**STOP. Phase 4B cannot begin until CASCADE GATE is complete.**

---

### PHASE 4B — Calibration (Expert — standalone phase; do not merge with Phase 4)

**CANNOT BEGIN UNTIL: Phase 4 findings complete AND CASCADE GATE signed off. Phase 5 cannot begin until gate4b_calibration_confirmed = true.**

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
- [ ] Each finding individually justified at its assigned level — [ ] each element individually justified at that level
- [ ] Distribution reasonable — at least two levels, or single level individually justified

Set `gate4b_calibration_confirmed: true`.

**STOP. Phase 5 cannot begin until gate4b_calibration_confirmed = true.**

---

### PHASE 5 — CONTRACT DELTA (Expert)

**CANNOT BEGIN UNTIL: gate4b_calibration_confirmed = true. CASCADE-B findings: Phase 0 amendment must be complete before this phase.**

| Finding | Spec Clause | Priority | Amendment Type | Required Change |
|---------|-------------|----------|----------------|-----------------|

Priority: breaking->P1, degraded->P2, cosmetic->P3. Blank Priority cells not accepted.
Amendment Type: add-field \| remove-field \| change-type \| change-enum \| change-error-shape \| change-auth-flow. Blank Amendment Type cells not accepted.

---

---

## V-04 — Inertia Framing (INERTIA-NN Registry)

**Variation axis:** Inertia framing — the INERTIA REGISTER is a named block that leads Phase 1B. All contamination entries receive INERTIA-NN labels and a Contamination Type. The gate closure phrase uses universal quantification: "every INERTIA-NN entry RESOLVED." Zero-entry vacuous-pass is a first-class declaration in the register, not a table cell or footnote. Cascade paths are framed as inertia correction routes with explicit prohibitions.

**Hypothesis:** Making the INERTIA REGISTER a named, numbered artifact elevates INERTIA-NN entries to trackable contract items. The universal quantification closure phrase ("every INERTIA-NN entry RESOLVED") makes vacuous-pass explicit by the same mechanism it makes non-empty passes explicit — the same sentence covers both cases (C-33). Per-type breakdown of INERTIA entries (NAME/TYPE/CLAUSE) in the register delivers C-32 as a first-class register dimension rather than a gate footnote. Cascade paths framed as inertia correction routes with explicit "Must NOT visit" prohibitions deliver C-34 in the conceptual register of inertia analysis.

---

You are running **trace-contract** for Topic: `{Topic}`.

**The inertia problem.** The expected table you are about to build is a claim that the spec — not the connector's current runtime behavior — defines what the connector should do. This claim is only valid if the expected values are derived from the spec alone. The connector's current behavior is the inertia competitor: already deployed, already integrated, already pulling expected-value derivation toward what-is rather than what-should-be.

Three contamination entry points exist:
1. **Scope anchoring** (Phase 0): Expert anchors scope to elements the connector currently exposes, omitting spec-defined elements the connector has not yet implemented.
2. **Value anchoring** (Phase 1A): Expert anchors expected values to what the connector currently returns, silencing the diff for affected elements.
3. **Residual contamination** (Phase 1B): Contamination the author cannot detect in their own work — requires a second-reader INERTIA REGISTER.

All contamination entries are logged as INERTIA-NN and classified by type: NAME (identifier or naming mismatch), TYPE (schema or data-type mismatch), CLAUSE (condition, rule, or logic mismatch). The gate closure phrase is: *every INERTIA-NN entry RESOLVED.* If the register is empty for a given type: *vacuous pass — every INERTIA-NN entry RESOLVED for {TYPE} (zero entries).*

Cascade paths are inertia correction routes: in-boundary findings follow the path that must NOT revisit scope enumeration; out-of-boundary findings follow the scope-correction path that must NOT proceed to contract delta without scope amendment.

Stock roles: Expert (Connectors contract expert), Automate (connector automation specialist). Expert builds Phase 1A. Automate owns the INERTIA REGISTER (Phase 1B) and diff classification (Phase 3).

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

**Inertia risk:** An expert who has worked with this connector instinctively enumerates elements by what the connector currently exposes. Spec-defined elements the connector has not yet implemented are invisible from a runtime perspective but are in scope from a contract perspective.

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

**Inertia risk:** Even with a clean scope, an expert may anchor Expected Values to what the connector currently returns. This is the most dangerous contamination form: invisible in the expected table but silences the diff entirely for affected elements.

**Step 1 — Commit skeleton** (names, types, spec clauses — Expected Value blank):

| Element | Element Type | Spec Clause | Expected Value |
|---------|--------------|-------------|----------------|
| (one row per SCOPE MANIFEST entry) | | | <- blank |

Record: `SKELETON COMMITTED — {N} rows`

**Step 2 — Fill Expected Values** from spec. The spec is the contract. The connector's current behavior is not evidence for expected value derivation.

**GATE 1** — Inertia closure at value layer. Two contamination paths; each uses two-clause confirmable form:
- [ ] All Expected Value cells filled — {N}/{N} complete
- [ ] No Spec Clause cells blank in expected table rows
- [ ] Actual output not consulted — not just ordered after, but not consulted at all — [CONFIRMED / NOT CONFIRMED]
- [ ] Expert runtime knowledge of current connector behavior not used to constrain Expected Values — not just deprioritized after consideration, but excluded entirely from expected value derivation — [CONFIRMED / NOT CONFIRMED]

Set `gate1_isolation_confirmed: true`.

---

### Phase 1B — INERTIA REGISTER (Inertia layer: residual contamination; owner: Automate)

**Inertia risk:** The Phase 1A author cannot reliably detect their own inertia contamination. Automate reviews each row: does this Expected Value appear to describe what the connector currently does, rather than what the spec defines?

Owner: Automate. Expert owns Phase 1A; Automate owns Phase 1B and GATE 1B. The same role cannot certify both phases.

**INERTIA REGISTER** — assign INERTIA-NN labels to all flagged entries; classify each by Contamination Type:

| ID | Row | Element | Contamination Type | Inertia Signal? (Yes/No) | Basis | Disposition |
|----|-----|---------|-------------------|--------------------------|-------|-------------|
| INERTIA-01 | | | NAME / TYPE / CLAUSE | | | |

**INERTIA REGISTER SUMMARY** — count entries by Contamination Type:

| Contamination Type | Count | Per-Type Closure |
|-------------------|-------|-----------------|
| NAME | {count} | every INERTIA-NN entry RESOLVED for NAME — or: *vacuous pass — every INERTIA-NN entry RESOLVED for NAME (zero entries)* |
| TYPE | {count} | every INERTIA-NN entry RESOLVED for TYPE — or: *vacuous pass — every INERTIA-NN entry RESOLVED for TYPE (zero entries)* |
| CLAUSE | {count} | every INERTIA-NN entry RESOLVED for CLAUSE — or: *vacuous pass — every INERTIA-NN entry RESOLVED for CLAUSE (zero entries)* |

**Per-Type Resolution** — one block per type, scoped to entries of that type only:

*NAME entries:*
If zero: *vacuous pass — every INERTIA-NN entry RESOLVED for NAME (zero entries).*
- [ ] INERTIA-{NN}: {element} -> RESOLVED

*TYPE entries:*
If zero: *vacuous pass — every INERTIA-NN entry RESOLVED for TYPE (zero entries).*
- [ ] INERTIA-{NN}: {element} -> RESOLVED

*CLAUSE entries:*
If zero: *vacuous pass — every INERTIA-NN entry RESOLVED for CLAUSE (zero entries).*
- [ ] INERTIA-{NN}: {element} -> RESOLVED

**GATE 1B** (Automate certifies — Expert cannot certify this gate):
- [ ] All `{N}` Phase 1A rows reviewed — none skipped
- [ ] Every INERTIA-NN entry assigned a Contamination Type — no blank cells
- [ ] INERTIA REGISTER SUMMARY complete — per-type closure declared for all three types (including vacuous-pass declarations for zero-count types)
- [ ] *every INERTIA-NN entry RESOLVED* — or — *vacuous pass — every INERTIA-NN entry RESOLVED (zero entries)* — [CONFIRMED / NOT CONFIRMED]

Set `gate1b_challenge_confirmed: true`.

---

### Phase 2 — Actual Output

Run the connector operation. Record actual output for each scope element. Add Actual Value column. Do not modify Expected Values.

| Element | Element Type | Spec Clause | Expected Value | Actual Value |
|---------|--------------|-------------|----------------|--------------|

**GATE 2:**
- [ ] Actual Value recorded for all `{N}` elements — no blank cells
- [ ] No Expected Value cells modified

Set `gate2_actual_complete: true`.

---

### Phase 3 — Diff and Classification

Compare Expected vs. Actual. Classify: MATCH | MISMATCH. For MISMATCH rows: assign Severity (breaking | degraded | cosmetic). Do not write root cause hypotheses in Phase 3.

| Element | Element Type | Spec Clause | Expected Value | Actual Value | Match? | Severity |
|---------|--------------|-------------|----------------|--------------|--------|----------|

**GATE 3:**
- [ ] Every row classified MATCH or MISMATCH
- [ ] No Severity cells blank on MISMATCH rows
- [ ] No Spec Clause cells blank
- [ ] No Element Type cells blank
- [ ] No root cause hypotheses in Phase 3 output — confirmed absent — [CONFIRMED / NOT CONFIRMED]

Set `gate3_diff_complete: true`.

---

### Phase 4 — Findings

For each MISMATCH, produce a finding scaffold. The `inertia-spec-drift` root cause is available when the connector was not updated to follow a known spec change — name the specific clause and connector version where the gap was introduced.

```
F-{NN}: {Element Name}
  Severity:    {from Phase 3}
  Spec Ref:    {Spec Clause}
  Root Cause:  {connector mechanism — field-mapping-delta | auth-handshake-mismatch | action-payload-drift | trigger-payload-gap | error-shape-change | metadata-convention-gap | inertia-spec-drift — "unknown" alone not accepted}
  Resolution:  {specific next step — names clause, version, or integration point to investigate}
```

---

### INERTIA CORRECTION ROUTES — Cascade Gate

Classify each finding into an inertia correction route. Each route names the upstream phase it must NOT visit.

| Finding | Root Cause Pattern | Correction Route | Must NOT Visit |
|---------|-------------------|-----------------|----------------|
| F-{NN} | In-boundary (no scope gap — correction is spec clause fix or impl fix only) | ROUTE-A: Phase 4B -> Phase 5 | **Phase 0 — must NOT re-open scope enumeration; in-boundary findings do not require scope amendment** |
| F-{NN} | Out-of-boundary (scope gap — spec defines an element Phase 0 missed) | ROUTE-B: Phase 0 amendment -> Phase 1A -> resume | **Phase 5 — must NOT proceed to CONTRACT DELTA until Phase 0 scope amendment is complete** |

**INERTIA CORRECTION GATE:**
- [ ] Every finding assigned ROUTE-A or ROUTE-B
- [ ] No ROUTE-A finding initiates a Phase 0 re-open — [CONFIRMED / NOT CONFIRMED]
- [ ] No ROUTE-B finding proceeds to Phase 5 without Phase 0 amendment — [CONFIRMED / NOT CONFIRMED]

---

### Phase 4B — Calibration (Standalone — do not merge with Phase 4)

**Inertia note on calibration:** Breaking mismatches driven by inertia-spec-drift are correctly assigned breaking severity — but each must be individually justified by its specific spec clause gap, not by a group claim. Different spec elements may have different severity even when all are caused by inertia.

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

Priority from Phase 4B: breaking->P1, degraded->P2, cosmetic->P3. Blank Priority cells not accepted.
Amendment Type: add-field \| remove-field \| change-type \| change-enum \| change-error-shape \| change-auth-flow. Blank Amendment Type cells not accepted.

**Inertia pattern in delta:** Amendments correcting inertia-spec-drift (typically breaking, P1) form a coherent remediation batch — spec evolution the connector has not followed, blocking downstream integrations. Group them within the P1 tier.

---

---

## V-05 — Combined Full Integration

**Variation axes:** Phrasing Register (no ask-first) + Output Format (GATE 1B-TM table) + Lifecycle Emphasis (STOP markers + CASCADE paths in dependency chain) + Inertia Framing (INERTIA REGISTER + INERTIA-NN numbering).

**Hypothesis:** Combining GATE 1B-TM with per-type rows and inline vacuous-pass cells (C-32, C-33), the CASCADE GATE with named "Must NOT Visit" columns in the phase dependency chain (C-34), INERTIA-NN universal-quantification gate closure language (C-33 redundant coverage), and the full role separation and STOP marker architecture achieves 25/26 aspirational criteria. The single missing criterion is C-17 — no "Ask first: [question]..." interrogative sentence precedes any fill form. A composite merging V-01's ask-first structure with this architecture closes the remaining gap at 26/26.

---

You are running **trace-contract** for Topic: `{Topic}`.

**The inertia problem.** The expected table you are about to build is a claim about the spec contract — not about the connector's current runtime behavior. Inertia contamination (anchoring expected values to what the connector currently does) silences the diff and defeats the exercise. Three contamination entry points exist: scope anchoring (Phase 0), value anchoring (Phase 1A), and residual contamination detectable only by a second reader with an INERTIA REGISTER (Phase 1B). Each phase below closes one entry point. The inertia framing inside each gate is not decorative.

**Role assignment:**

| Role | Identity | Phases Owned |
|------|----------|-------------|
| Expert | Connectors contract expert | Phase 0, Phase 1A, Phase 2, Phase 4, CASCADE GATE, Phase 4B, Phase 5 |
| Automate | Connector automation specialist | Phase 1B, GATE 1B-TM, GATE 1B, Phase 3 |

Expert cannot certify GATE 1B. Automate cannot certify GATE 1. Role separation is structurally enforced — it is not operationally optional.

**Phase dependency chain** — no phase begins until the gate before it fires; CASCADE paths are lifecycle entries with named prohibitions:

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
| CASCADE-A | In-boundary route | Expert | F-{NN} assigned | — | **Phase 0 — must NOT re-open for in-boundary omission** |
| CASCADE-B | Out-of-boundary route | Expert | F-{NN} assigned | — | **Phase 5 — must NOT proceed to CONTRACT DELTA without Phase 0 amendment** |
| CASCADE GATE | Cascade Gate | Expert | All findings assigned | — | — |
| 4B | Calibration | Expert | Phase 4 + CASCADE GATE | gate4b_calibration_confirmed | — |
| GATE 4B | Calibration Gate | Expert | Phase 4B complete | — | — |
| 5 | CONTRACT DELTA | Expert | gate4b_calibration_confirmed = true | — | — |

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

**CANNOT BEGIN UNTIL: Start of artifact.**

**Inertia risk:** Expert anchors element names to what the connector currently exposes, omitting spec-defined elements the connector has not yet implemented.

Enumerate all in-scope elements as a SCOPE MANIFEST. Derive scope from spec only. All columns required — blank cells are a gate failure condition.

| # | Element Name | Element Type | Spec Clause Key |
|---|--------------|--------------|-----------------|
| | | schema-field \| auth-handshake \| action-payload \| trigger-payload \| error-shape \| metadata | |

**STOP. Do not write GATE 0 until Phase 0 enumeration is complete.**

**GATE 0** (Expert):
- [ ] SCOPE MANIFEST complete — `{N}` elements enumerated
- [ ] Element Type populated — no blank cells
- [ ] Spec Clause Key populated — no blank cells
- [ ] Scope derived from spec — current connector behavior excluded from element selection — not just deprioritized, but excluded from scope derivation entirely — [CONFIRMED / NOT CONFIRMED]

Set `gate0_scope_confirmed: true`.

**STOP. Phase 1A cannot begin until gate0_scope_confirmed = true.**

---

### PHASE 1A — Expected Output (Expert)

**CANNOT BEGIN UNTIL: gate0_scope_confirmed = true.**

**Inertia risk:** Expert anchors Expected Values to what the connector currently returns, writing "expected" values that describe current behavior rather than the spec contract.

**Step 1 — Commit skeleton** (names, types, spec clauses — Expected Value column blank):

| Element | Element Type | Spec Clause | Expected Value |
|---------|--------------|-------------|----------------|
| (one row per SCOPE MANIFEST entry) | | | <- leave blank |

Record: `SKELETON COMMITTED — {N} rows`

**Step 2 — Fill Expected Values** from spec. The spec is the contract. Do not reference actual output. Do not reference what you know the connector currently does.

**STOP. Do not write GATE 1 until all Expected Values are filled.**

**GATE 1** (Expert):
- [ ] All Expected Value cells filled — {N}/{N} complete — no blank cells
- [ ] No Spec Clause cells blank in expected table rows
- [ ] Actual output not consulted during Phase 1A — not just ordered after, but not consulted at all — [CONFIRMED / NOT CONFIRMED]
- [ ] Expert runtime knowledge of current connector behavior not applied to Expected Values — not just deprioritized after consideration, but excluded entirely from expected value derivation — [CONFIRMED / NOT CONFIRMED]

Set `gate1_isolation_confirmed: true`.

**STOP. Phase 1B cannot begin until gate1_isolation_confirmed = true. Phase 1B owner is Automate — not Expert. The same role that built Phase 1A cannot certify GATE 1B.**

---

### PHASE 1B — INERTIA REGISTER (Automate)

**CANNOT BEGIN UNTIL: gate1_isolation_confirmed = true. OWNER: AUTOMATE. Expert cannot run or certify this phase.**

**Inertia risk:** The Phase 1A author cannot reliably detect their own inertia contamination. Automate reviews each row for residual contamination.

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

**Per-Type Verification Checklists** — one block per Contamination Type, scoped to entries of that type only:

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

**STOP. Do not write GATE 1B until GATE 1B-TM is complete — all three type rows populated and all per-type checklists present (including zero-entry vacuous-pass declarations).**

**GATE 1B** (Automate certifies — Expert cannot certify this gate):
- [ ] All `{N}` Phase 1A rows reviewed — none skipped
- [ ] Contamination Type assigned for every flagged row — no blank cells
- [ ] GATE 1B-TM complete — all three type rows populated, no blank cells
- [ ] Per-type checklists complete — each non-empty type block fully checked; each zero-entry type block explicitly declares vacuous pass
- [ ] No unresolved INERTIA-NN entries in the final expected table — [CONFIRMED / NOT CONFIRMED]

Set `gate1b_challenge_confirmed: true`.

**STOP. Phase 2 cannot begin until gate1b_challenge_confirmed = true.**

---

### PHASE 2 — Actual Output (Expert)

**CANNOT BEGIN UNTIL: gate1b_challenge_confirmed = true.**

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

**CANNOT BEGIN UNTIL: gate2_actual_complete = true.**

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

### PHASE 4 — Findings (Expert)

**CANNOT BEGIN UNTIL: gate3_diff_complete = true.**

For each MISMATCH row, produce a finding scaffold:

```
F-{NN}: {Element Name}
  Severity:    {from Phase 3 — do not reassign here}
  Spec Ref:    {Spec Clause}
  Root Cause:  {connector mechanism — field-mapping-delta | auth-handshake-mismatch | action-payload-drift | trigger-payload-gap | error-shape-change | metadata-convention-gap | inertia-spec-drift — "unknown" alone not accepted}
  Resolution:  {specific investigative step — names what to investigate; "investigate further" alone not accepted}
```

`inertia-spec-drift` is a valid root cause when the connector was not updated to follow a known spec change. Name the specific clause and the connector version where the gap was introduced.

**STOP. Phase 4B is a standalone phase. Do not begin calibration inside Phase 4. After all findings are written, proceed to CASCADE GATE before Phase 4B.**

---

### CASCADE GATE (Expert)

**CANNOT BEGIN UNTIL: Phase 4 findings complete.**

Assign each finding to a cascade path. Each path has a named upstream phase it must NOT visit.

| Finding | Severity | Cascade Path | Route | Must NOT Visit |
|---------|----------|-------------|-------|----------------|
| F-{NN} | | CASCADE-A (in-boundary: no scope gap) | Phase 4B -> Phase 5 | **Phase 0 — must NOT re-open scope enumeration for an in-boundary omission** |
| F-{NN} | | CASCADE-B (out-of-boundary: scope gap detected) | Phase 0 amendment -> Phase 1A -> resume | **Phase 5 — must NOT proceed to CONTRACT DELTA without Phase 0 amendment** |

**CASCADE GATE:**
- [ ] Every finding assigned CASCADE-A or CASCADE-B — no unassigned rows
- [ ] Must NOT Visit populated for every row — no blank cells
- [ ] No CASCADE-A finding has re-opened Phase 0 — [CONFIRMED / NOT CONFIRMED]
- [ ] No CASCADE-B finding has proceeded to Phase 5 without completing Phase 0 amendment — [CONFIRMED / NOT CONFIRMED]

**STOP. Phase 4B cannot begin until CASCADE GATE is signed off.**

---

### PHASE 4B — Calibration (Expert — standalone phase; do not merge with Phase 4)

**CANNOT BEGIN UNTIL: Phase 4 findings complete AND CASCADE GATE signed off. Phase 5 cannot begin until gate4b_calibration_confirmed = true.**

**Severity tally** (complete before writing any calibration assessment):

| Severity | Count |
|----------|-------|
| breaking | |
| degraded | |
| cosmetic | |

For each finding individually: justify its severity assignment. Group justification ("all breaking because inertia implies full replacement") = gate failure condition. Each element may have a different inertia magnitude; justify each independently.

**STOP. Do not write GATE 4B until individual justifications are written for every finding.**

**GATE 4B** (Expert):
- [ ] Severity tally completed before assessments
- [ ] Each finding individually justified at its assigned severity level — group justification not accepted: [ ] each element individually justified at that level
- [ ] Distribution reasonable — at least two severity levels represented, or single level individually justified per finding

Set `gate4b_calibration_confirmed: true`.

**STOP. Phase 5 cannot begin until gate4b_calibration_confirmed = true. CASCADE-B findings: Phase 0 amendment must also be complete.**

---

### PHASE 5 — CONTRACT DELTA (Expert)

**CANNOT BEGIN UNTIL: gate4b_calibration_confirmed = true AND all CASCADE-B Phase 0 amendments complete.**

Priority is derived from Phase 4B calibrated severity. Do not assign priority without Phase 4B completion. All columns required — blank Priority or Amendment Type cells are not accepted.

| Finding | Spec Clause | Priority | Amendment Type | Required Change |
|---------|-------------|----------|----------------|-----------------|

- Priority: breaking->P1, degraded->P2, cosmetic->P3
- Amendment Type: add-field \| remove-field \| change-type \| change-enum \| change-error-shape \| change-auth-flow

**Inertia pattern in delta:** Amendments correcting inertia-spec-drift (typically breaking, P1) form a coherent remediation batch distinct from schema-only corrections. Group them within the P1 tier — they represent spec evolution the connector has not followed and are blocking downstream integrations that rely on the contract as specified.
