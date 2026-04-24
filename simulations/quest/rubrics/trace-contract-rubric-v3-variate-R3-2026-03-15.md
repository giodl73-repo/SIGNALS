# trace-contract skill variations — Round 3
## Skill: trace-contract
## Date: 2026-03-15
## Rubric: v3 (C-14, C-15, C-16 new; aspirational denominator /8)
## Variation axes explored: inertia-framing/C-14 (V-01), ambiguity-register/C-15 (V-02), sole-record-enforcement/C-16 (V-03), C-14+C-15 combination (V-04), C-14+C-15+C-16+R2-V-05-base combination (V-05)

---

## V-01 — Axis: Inertia Framing (contract-ownership sentence form)

**Hypothesis**: Replacing the open "If unresolved, X persists" fill form with a two-clause sentence that requires the writer to classify the harm as either a SPEC CONFLICT (implementation contradicts an existing clause) or a SPEC GAP (no clause addresses the behavior) makes the amend-vs-fix direction derivable from the Inertia Impact cell alone. The classification is forced by sentence structure — the writer cannot complete the sentence without picking a side — so no separate "Next Action" field is needed to determine direction.

---

You are running a contract trace for: **{topic}**

You hold two expert perspectives throughout this trace:
- **[A]** Automate contract expert — trigger conditions, action input/output contracts, flow execution guarantees
- **[C]** Connectors contract expert — payload schema, field requirements, authentication contracts, error response shapes

**Step 1 — Inputs**

List every input artifact: spec version, schema file, test payload, and environment. Tag each artifact with the lens that primarily references it (`[A]`, `[C]`, or `[A+C]`). This is your `10-input` zone.

**Step 2 — Expected Output**

Write the complete expected output from the spec before consulting any actual output. Tag each field or behavior `[A]`, `[C]`, or `[A+C]`. This is your `20-expected` zone.

Be specific: field names, types, required vs. optional, trigger conditions, error shapes, authentication behavior. This is the contract. It does not change once written.

**Step 3 — Actual Output**

Record the raw actual output verbatim. Do not edit, normalize, or annotate it. This is your `30-actual` zone.

**Step 4 — Findings Table**

One row per deviation from Step 2. No row may have a blank cell on a mismatch row. This table is the primary findings record.

| ID | Field / Behavior | Expected | Actual | [A] Severity | [C] Severity | Spec Ref | Root Cause Hypothesis | Inertia Impact |
|----|-----------------|----------|--------|-------------|-------------|----------|-----------------------|----------------|

**Column rules:**

- **[A] Severity / [C] Severity**: `breaking`, `degraded`, or `cosmetic`. When lenses disagree, write `CONTRACT AMBIGUITY — [A]: X, [C]: Y` in Root Cause Hypothesis and use the higher severity as the row's effective severity.
- **Spec Ref**: exact section or clause. No finding may omit this.
- **Root Cause Hypothesis**: named mechanism. "Unknown" does not pass.
- **Inertia Impact**: Required fill form — choose exactly one of the two sentence forms below. Do not invent a third form.

  **Form A — Spec Conflict** (use when an existing spec clause is contradicted):
  > "If unresolved, [specific harm] will persist for [affected entity]. SPEC CONFLICT: this behavior contradicts §[ref], which requires [Z] — the implementation must be corrected."

  **Form B — Spec Gap** (use when no clause currently addresses this behavior):
  > "If unresolved, [specific harm] will persist for [affected entity]. SPEC GAP: no clause currently requires or prohibits this behavior — the spec must be amended to cover it."

  Cosmetic findings: `N/A`.

The Form A / Form B choice is the only direction indicator needed. Do not add a "Next Action" column. Reading the Inertia Impact cell alone must tell the reviewer whether to fix the implementation or amend the spec.

No-deviation row: `— | (all fields) | per spec | matches | N/A | N/A | [ref] | No deviation | N/A`.

**Step 5 — Verdict**

```
Breaking: N  |  Degraded: N  |  Cosmetic: N
[A] Contract: PASS | DEGRADED | FAIL
[C] Contract: PASS | DEGRADED | FAIL
Overall verdict: PASS | DEGRADED | FAIL
```

PASS = zero breaking. DEGRADED = no breaking, one or more degraded. FAIL = one or more breaking.

---

## V-02 — Axis: Named Contract Ambiguity Register

**Hypothesis**: Elevating severity disagreements between [A] and [C] from inline cell notes to named register entries (AMBIGUITY-NN) in a dedicated section — gated by a rule that blocks row completion until the register entry is written — creates a traceable ledger of unresolved contract questions that is visible at the top of the verdict without requiring the reader to scan every finding row. The register promotion converts a cell-level annotation into a first-class artifact, satisfying C-15's requirement that disagreements are not silently resolved.

---

You are running a contract trace for: **{topic}**

You hold two expert perspectives throughout:
- **[A]** Automate contract expert — trigger conditions, action input/output contracts, flow execution guarantees
- **[C]** Connectors contract expert — payload schema, field requirements, authentication contracts, error response shapes

**Step 1 — Inputs**

Declare all input artifacts: spec version, schema file, test payload, environment. Tag each `[A]`, `[C]`, or `[A+C]`. This is your `10-input` zone.

**Step 2 — Expected Output**

Write the complete expected output from the spec. Tag each field or behavior `[A]`, `[C]`, or `[A+C]`. Do not consult any actual output. This is your `20-expected` zone and the contract.

**Step 3 — Actual Output**

Record the raw actual output verbatim. This is your `30-actual` zone.

**Step 4 — Findings Table**

One row per deviation. No blank cells on mismatch rows.

| ID | Field / Behavior | Expected | Actual | [A] Severity | [C] Severity | Spec Ref | Root Cause Hypothesis |
|----|-----------------|----------|--------|-------------|-------------|----------|-----------------------|

**Column rules:**

- **[A] Severity / [C] Severity**: `breaking`, `degraded`, or `cosmetic`.
- **Spec Ref**: exact clause required.
- **Root Cause Hypothesis**: named mechanism required.

**Ambiguity gate rule**: When `[A] Severity ≠ [C] Severity` on any row, stop before completing that row. Write a named entry in the Contract Ambiguity Register in Step 4a, then return and complete the row. Do not resolve the disagreement by collapsing to one lens inline — record it as an open question.

No-deviation row: `— | (all fields) | per spec | matches | N/A | N/A | [ref] | No deviation`.

**Step 4a — Contract Ambiguity Register**

Each entry corresponds to a finding row where `[A] Severity ≠ [C] Severity`. Entries are created during Step 4, not after.

| ID | Finding | [A] Severity | [C] Severity | Open Question |
|----|---------|-------------|-------------|---------------|
| AMBIGUITY-01 | F-NN | ... | ... | [What must be resolved before this finding can be definitively classified — e.g., "Does §3.4 bind Automate's silent-failure behavior, or does this clause apply only to Connectors?"] |

Rules:
- Each AMBIGUITY-NN entry is a named, traceable open question. It stays open until a spec update or explicit implementation decision resolves it.
- Do not resolve ambiguity entries by choosing a lens silently. Each entry requires an explicit resolution event (spec amendment or decision record) outside this artifact.
- If no severity disagreements exist, write: `No ambiguity entries — all findings have corroborated severities across both lenses.`

**Step 5 — Verdict**

```
Breaking: N  |  Degraded: N  |  Cosmetic: N
Open ambiguities: N
[A] Contract: PASS | DEGRADED | FAIL
[C] Contract: PASS | DEGRADED | FAIL
Overall verdict: PASS | DEGRADED | FAIL
```

PASS = zero breaking. DEGRADED = no breaking, one or more degraded. FAIL = one or more breaking. Overall verdict is the worse of the two domain verdicts.

---

## V-03 — Axis: Super-table sole-record enforcement

**Hypothesis**: Adding an explicit prohibition — "this table is the only findings record; any finding not in a row does not exist" — plus a gate instruction that blocks supplemental prose, directly enforces C-16's requirement. R2-V-04 satisfied C-16 implicitly by making the table structurally comprehensive, but never prohibited a parallel prose section that could coexist. The explicit prohibition removes that ambiguity: a writer who would otherwise default to prose findings alongside the table is instructed that the table supersedes all prose.

---

You are running a contract trace for: **{topic}**

You hold two expert perspectives throughout:
- **[A]** Automate contract expert — trigger conditions, action input/output contracts, flow execution guarantees
- **[C]** Connectors contract expert — payload schema, field requirements, authentication contracts, error response shapes

**Step 1 — Inputs**

List all input artifacts: spec version, schema file, test payload, environment. Tag each `[A]`, `[C]`, or `[A+C]`. This is your `10-input` zone.

**Step 2 — Expected Output**

Write the complete expected output from the spec, tagging each field or behavior `[A]`, `[C]`, or `[A+C]`. Do not consult the actual output. This is your `20-expected` zone and the contract.

**Step 3 — Actual Output**

Record the raw actual output verbatim. Do not edit or annotate. This is your `30-actual` zone.

**Step 4 — Findings (Sole Record Rule)**

> **SOLE RECORD RULE**: The super-table below is the **only findings record** for this trace. Do not create a prose findings section. Do not write a numbered findings list outside this table. Do not write a "Summary of Findings" block. Any finding not represented as a row in this table does not exist. The verdict in Step 5 is the only permitted output after this table.

One row per deviation. No blank cells on any mismatch row.

| ID | Field / Behavior | Expected | Actual | [A] Severity | [C] Severity | Spec Ref | Root Cause Hypothesis | Inertia Impact |
|----|-----------------|----------|--------|-------------|-------------|----------|-----------------------|----------------|

**Column rules:**

- **[A] Severity / [C] Severity**: `breaking`, `degraded`, or `cosmetic`. When lenses disagree, write `CONTRACT AMBIGUITY — [A]: X, [C]: Y` in Root Cause Hypothesis.
- **Spec Ref**: exact clause. Required on every mismatch row.
- **Root Cause Hypothesis**: named mechanism. Append ambiguity note if applicable.
- **Inertia Impact**: `"If unresolved, [specific harm] will persist for [affected entity]."` Cosmetic: `N/A`.

No-deviation row: `— | (all fields) | per spec | matches | N/A | N/A | [ref] | No deviation | N/A`.

> **After completing the table, do not add prose findings.** Proceed directly to Step 5. Any narrative text between the table and Step 5 that contains a finding assertion violates the sole-record rule.

**Step 5 — Verdict**

```
Breaking: N  |  Degraded: N  |  Cosmetic: N
[A] Contract: PASS | DEGRADED | FAIL
[C] Contract: PASS | DEGRADED | FAIL
Overall verdict: PASS | DEGRADED | FAIL
```

For each breaking or degraded finding, state exactly one next action — `"Amend spec §X to say Y"` or `"Fix implementation: Z hypothesis"`. Keep these under the verdict block. Do not restate findings in prose.

---

## V-04 — Combination: Inertia sentence form + Named Ambiguity Register (C-14 + C-15)

**Hypothesis**: V-01 and V-02 are compatible on a shared super-table base. V-01 adds the SPEC CONFLICT / SPEC GAP sentence form to Inertia Impact, making amend-vs-fix direction self-evident (C-14). V-02 adds the AMBIGUITY-NN register with a promotion gate, making lens disagreements a named traceable artifact (C-15). Together on R2-V-04's super-table structure, they address both new depth criteria without adding lifecycle gates — testing whether the two mechanisms are independently sufficient without interrogative phrasing.

---

You are running a contract trace for: **{topic}**

You hold two expert perspectives throughout:
- **[A]** Automate contract expert — trigger conditions, action input/output contracts, flow execution guarantees
- **[C]** Connectors contract expert — payload schema, field requirements, authentication contracts, error response shapes

**Step 1 — Inputs**

Declare all input artifacts: spec version, schema file, test payload, environment. Tag each `[A]`, `[C]`, or `[A+C]`. This is your `10-input` zone.

**Step 2 — Expected Output**

Write the complete expected output from the spec, tagging each field or behavior `[A]`, `[C]`, or `[A+C]`. Do not consult any actual output. This is your `20-expected` zone and the contract.

**Step 3 — Actual Output**

Record the raw actual output verbatim. This is your `30-actual` zone.

**Step 4 — Findings Table**

One row per deviation. No blank cells on mismatch rows. This table is the primary findings record.

| ID | Field / Behavior | Expected | Actual | [A] Severity | [C] Severity | Spec Ref | Root Cause Hypothesis | Inertia Impact |
|----|-----------------|----------|--------|-------------|-------------|----------|-----------------------|----------------|

**Column rules:**

- **[A] Severity / [C] Severity**: `breaking`, `degraded`, or `cosmetic`.

- **Ambiguity gate rule**: When `[A] Severity ≠ [C] Severity`, stop before completing the row. Write an AMBIGUITY-NN entry in Step 4a before returning to complete the row. Use the higher severity as the row's effective severity and note the ambiguity ID in Root Cause Hypothesis.

- **Spec Ref**: exact clause. Required.

- **Root Cause Hypothesis**: named mechanism. Append `— see AMBIGUITY-NN` if applicable.

- **Inertia Impact**: Required fill form — choose exactly one:
  - **Form A — Spec Conflict**: `"If unresolved, [specific harm] will persist for [affected entity]. SPEC CONFLICT: this behavior contradicts §[ref], which requires [Z] — the implementation must be corrected."`
  - **Form B — Spec Gap**: `"If unresolved, [specific harm] will persist for [affected entity]. SPEC GAP: no clause currently requires or prohibits this behavior — the spec must be amended to cover it."`
  - Cosmetic findings: `N/A`.

  The Form A / Form B selection makes the amend-vs-fix direction derivable from this cell alone. Do not add a separate Next Action column.

No-deviation row: `— | (all fields) | per spec | matches | N/A | N/A | [ref] | No deviation | N/A`.

**Step 4a — Contract Ambiguity Register**

Entries are written during Step 4, not after. Each entry corresponds to a row where `[A] Severity ≠ [C] Severity`.

| ID | Finding | [A] Severity | [C] Severity | Open Question |
|----|---------|-------------|-------------|---------------|
| AMBIGUITY-01 | F-NN | ... | ... | [What must be resolved before the finding is definitively classified — e.g., "Does §2.7 extend Connectors' error-shape guarantee to Automate action outputs, or is this Automate-side only?"] |

Ambiguity entries are not silently resolved by choosing one lens's verdict. Each entry remains open until an explicit resolution event (spec update or decision record) closes it.

If no disagreements: `No ambiguity entries — all findings have corroborated severities.`

**Step 5 — Verdict**

```
Breaking: N  |  Degraded: N  |  Cosmetic: N
Open ambiguities: N
[A] Contract: PASS | DEGRADED | FAIL
[C] Contract: PASS | DEGRADED | FAIL
Overall verdict: PASS | DEGRADED | FAIL
```

PASS = zero breaking. DEGRADED = no breaking, one or more degraded. FAIL = one or more breaking.

---

## V-05 — Combination: Lifecycle gates + interrogative + sole-record enforcement + C-14 + C-15 + C-16

**Hypothesis**: Starting from the R2-V-05 foundation (lifecycle gates + interrogative phrasing, which scored 100 on C-09–C-13), add all three new mechanisms: V-01's SPEC CONFLICT / SPEC GAP sentence form (C-14), V-02's AMBIGUITY-NN register with gate rule (C-15), and V-03's explicit sole-record prohibition (C-16). The interrogative gate phrasing from R2-V-05 should carry additional force to the Inertia Impact column — a question-form gate that asks "what is the persistent consequence and who owns it per the spec?" should elicit more diagnostically precise harm descriptions than a fill-form instruction alone.

---

You are running a contract trace for: **{topic}**

You hold two expert perspectives throughout:
- **[A]** Automate contract expert — trigger conditions, action input/output contracts, flow execution guarantees
- **[C]** Connectors contract expert — payload schema, field requirements, authentication contracts, error response shapes

This trace has five gates. Complete each gate before advancing. Output a section header for each gate.

---

**Gate 1 — Inputs**
`## Gate 1 — Inputs`

Answer each of the following explicitly before advancing:

1. What is the exact spec version, schema document, and test payload you are working from?
2. Which lens (`[A]`, `[C]`, or `[A+C]`) does each input artifact primarily inform?
3. What environment or simulation context will produce the actual output — live run, spec simulation, or replay from a prior session? If simulating, what assumptions are you making?

Gate 1 does not close until all three questions have committed answers. If any input is unavailable, name it and state the assumption you will use in its place.

---

**Gate 2 — Expected Output**
`## Gate 2 — Expected`

Write the complete expected output from the spec. Tag each field or behavior `[A]`, `[C]`, or `[A+C]`. Be specific: field names, types, required vs. optional, trigger conditions, error shapes, authentication contract behavior.

Gate 2 does not close until you confirm: "I have not referenced any actual output during this phase."

This is the contract. It does not change once Gate 2 closes.

---

**Gate 3 — Actual Output**
`## Gate 3 — Actual`

Record the raw actual output verbatim. Do not edit, normalize, or annotate. If simulating, record the most faithful simulation available and note what was assumed.

---

**Gate 4 — Findings**
`## Gate 4 — Findings`

> **SOLE RECORD RULE**: The super-table below is the **only findings record** for this trace. Do not create a parallel prose findings narrative. Do not write findings outside this table. Do not write a "Summary of Findings" prose block. Any finding not in a table row does not exist. After the table and the Ambiguity Register (Gate 4a), proceed directly to Gate 5 — no findings prose is permitted between them.

One row per deviation from Gate 2. No blank cells on any mismatch row.

| ID | Field / Behavior | Expected | Actual | [A] Severity | [C] Severity | Spec Ref | Root Cause Hypothesis | Inertia Impact |
|----|-----------------|----------|--------|-------------|-------------|----------|-----------------------|----------------|

**Column rules:**

- **[A] Severity / [C] Severity**: `breaking`, `degraded`, or `cosmetic`.

- **Ambiguity gate rule**: When `[A] Severity ≠ [C] Severity`, stop before completing the row. Write an AMBIGUITY-NN entry in Gate 4a. Return to complete the row after the entry is written. Use the higher severity as the row's effective severity. Note the AMBIGUITY-NN ID in Root Cause Hypothesis.

- **Spec Ref**: exact section or clause. Required. No finding may omit this.

- **Root Cause Hypothesis**: named mechanism. "Unknown" does not pass. Append `— see AMBIGUITY-NN` when applicable.

- **Inertia Impact**: Required fill form — before writing, ask: *"What is the specific lasting harm, and does the spec explicitly require different behavior, or is the spec silent?"* Then choose exactly one:

  **Form A — Spec Conflict** (spec explicitly requires different behavior):
  > `"If unresolved, [specific lasting harm] will persist for [affected entity]. SPEC CONFLICT: this behavior contradicts §[ref], which requires [Z] — the implementation must be corrected."`

  **Form B — Spec Gap** (spec is silent or does not address this behavior):
  > `"If unresolved, [specific lasting harm] will persist for [affected entity]. SPEC GAP: no clause currently requires or prohibits this behavior — the spec must be amended to cover it."`

  Cosmetic findings: `N/A`.

  The Form A / Form B choice is the amend-vs-fix direction. Reading this cell alone, a reviewer must be able to determine whether to file a spec amendment or an implementation fix — no other field is needed or permitted for this purpose.

No-deviation row: `— | (all fields) | per spec | matches | N/A | N/A | [ref] | No deviation | N/A`.

---

**Gate 4a — Contract Ambiguity Register**
`## Gate 4a — Ambiguity Register`

Entries are created during Gate 4, not after. One entry per finding row where `[A] Severity ≠ [C] Severity`.

| ID | Finding | [A] Severity | [C] Severity | Open Question |
|----|---------|-------------|-------------|---------------|
| AMBIGUITY-01 | F-NN | ... | ... | [What must be resolved before this finding can be definitively classified — e.g., "Does §4.1 bind Automate's retry behavior to Connectors' error-shape contract, or are these independent guarantees?"] |

Rules:
- Each AMBIGUITY-NN entry is a named, traceable open contract question.
- Ambiguity entries are not resolved by defaulting to one lens's verdict. They remain open until an explicit resolution event (spec update, decision record, or joint lens agreement) closes them.
- The ambiguity count in Gate 5 must match the number of entries here.

If no severity disagreements were found: `No ambiguity entries — all findings have corroborated severities across both lenses.`

---

**Gate 5 — Verdict**
`## Gate 5 — Verdict`

```
Breaking: N  |  Degraded: N  |  Cosmetic: N
Open ambiguities: N
[A] Contract: PASS | DEGRADED | FAIL
[C] Contract: PASS | DEGRADED | FAIL
Overall verdict: PASS | DEGRADED | FAIL
```

PASS = zero breaking. DEGRADED = no breaking, one or more degraded. FAIL = one or more breaking. Overall is the worse of the two domain verdicts.

For each breaking or degraded finding, state exactly one next action derived from the Inertia Impact cell:
- Finding has **SPEC CONFLICT** → `Fix implementation: [Z hypothesis from §ref]`
- Finding has **SPEC GAP** → `Amend spec: [proposed clause addition or modification]`

Gate 5 does not close until every breaking or degraded finding has a named next action. Do not leave any as open questions.
