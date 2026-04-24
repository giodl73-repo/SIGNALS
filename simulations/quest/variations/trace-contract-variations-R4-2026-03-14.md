Written to `simulations/quest/variations/trace-contract-variations-R4-2026-03-14.md`.

---

## Round 4 Variations — Summary

| V | Axis | Key mechanism | Predicted score |
|---|------|---------------|-----------------|
| **V-01** | Role sequence — domain expert leads Phase 1 | Connectors expert constructs expected table; element-type taxonomy embedded at row creation, not retrofitted in Phase 3 | **100** |
| **V-02** | Phrasing register — imperative second-person | All instructions as direct STOP-marker commands; same R3 structural gates | **100** |
| **V-03** | Inertia framing — actual output as status-quo default | Actual = "inertia output"; expected = "committed contract"; severity anchored to promise-vs-inertia gap; GATE 4B anti-bias clause | **100 or 97.5** |
| **V-04** | Role sequence + phrasing register (V-01 + V-02) | Expert leads Phase 1 in imperative form; Automate activated by STOP-marker command at Phase 2 | **100** |
| **V-05** | Full synthesis — all three axes + all R3 mechanisms | V-01 + V-02 + V-03 + CONFIRMED declarations + 6-key frontmatter + element-type column + Phase 4B + universal blank-cell gates | **100** |

---

**Three genuinely new axes vs. R3:**

1. **Role sequence** — R1–R3 always had Automate lead Phase 1. V-01 flips this: the Connectors expert writes the expected table, embedding `schema-field | auth-handshake | action-payload | trigger-payload | error-shape | metadata` at source. The hypothesis is that C-17 compliance is stronger when domain vocabulary is structural from row 1 rather than retroactively validated in Phase 3.

2. **Phrasing register** — R1–R3 used descriptive/prescriptive prose. V-02 tests full imperative second-person: "Write the expected table now. Stop. Confirm GATE 1. Do not write Phase 2 first." The hypothesis is that STOP markers harden the C-11 classification-before-analysis boundary more than descriptive instructions.

3. **Inertia framing** — R1–R3 treated actual output as semantically neutral. V-03 frames it as "what the connector delivers under inertia" and frames expected output as "the committed contract." This gives the three severity levels a coherent conceptual anchor (breaking = inertia structurally violates the promise; degraded = weakens it; cosmetic = form-only divergence). GATE 4B carries an explicit anti-bias clause: "inertia framing alone is not sufficient justification for uniform breaking." This is the only scoring risk (C-09) — if the framing pressure overrides the gate, the predicted score drops to 97.5.

**All R3 structural mechanisms are preserved** in every variation: CONFIRMED/NOT CONFIRMED declarations (C-14), universal blank-cell gate enforcement (C-15/C-20), four-key frontmatter (C-16/C-19), element-type taxonomy column (C-17), standalone Phase 4B with severity tally table (C-18).
e on Phase 3.

**Hypothesis:** In R1–R3, Automate led all phases. When Automate leads Phase 1, element-type labels may be applied with engineering vocabulary (field types, HTTP methods) rather than connector-domain vocabulary (schema-field, auth-handshake, action-payload). When the Connectors expert leads Phase 1, the element-type taxonomy column is populated by domain expertise at the moment each row is constructed — not retrofitted during Phase 3. This is the strongest enforcement of C-17 (domain taxonomy as structural column) because the vocabulary is embedded at source. C-07 (domain vocabulary in findings) should also be stronger because Phase 4 inherits element-type labels from a domain-expert-constructed Phase 1. The structural gate apparatus is identical to V-05 R3.

```
---
skill: trace-contract
topic: {{topic}}
date: {{date}}
gate1_isolation_confirmed: pending
gate2_actual_complete: pending
gate3_diff_complete: pending
gate4b_calibration_confirmed: pending
---

# Trace: Contract vs. Actual — {{topic}}

**Roles:**
- **Connectors Contract Expert** — leads Phase 1; validates element-type taxonomy in
  Phase 3; leads Phase 4B calibration
- **Automate** — leads Phase 2; co-owns Phase 3 diff construction; leads Phase 4
  root cause analysis

**Role sequence:** Connectors Contract Expert activates first. Automate does not activate
until gate1_isolation_confirmed is set.

---

## PHASE 1 — Expected Output (Connectors Contract Expert)

**Active role: Connectors Contract Expert.**
Automate is not yet active. Do not draw on engineering runtime knowledge.

Construct the expected output from the spec contract alone. For every field, endpoint,
payload envelope, auth mechanism, and error shape the spec defines, add one row.

The element-type column uses the following fixed six-term vocabulary:

`schema-field | auth-handshake | action-payload | trigger-payload | error-shape | metadata`

Apply the most specific term that fits. If a row spans two types, split it into two rows.
Do not leave Element Type blank — the Connectors expert owns this column.

### Expected Field Contract

| Field / Element | Element Type | Expected Value or Shape | Spec Clause |
|-----------------|-------------|------------------------|-------------|

*(One row per contract element. Nested paths use dot notation. Element Type must use only
the six-term vocabulary. No Spec Clause cell blank.)*

### GATE 1 — Isolation + Domain Completeness

Connectors Contract Expert confirms each item. Write CONFIRMED or NOT CONFIRMED after the dash.

1. Expected completeness: All spec-defined contract elements have a row — none omitted —
   [CONFIRMED / NOT CONFIRMED]
2. Isolation: Actual output was not referenced during this phase — not just ordered after,
   but not consulted at all — [CONFIRMED / NOT CONFIRMED]
3. Element type coverage: No Element Type cell is blank; all values from the fixed six-term
   vocabulary — [CONFIRMED / NOT CONFIRMED]
4. Spec clause coverage: No Spec Clause cell is blank; every row names a section or field —
   [CONFIRMED / NOT CONFIRMED]

Gate status: [PASS — all four CONFIRMED / NEEDS COMPLETION — list unconfirmed items]

Set frontmatter: `gate1_isolation_confirmed: true` if all four confirmed; `false` otherwise.

**Automate does not activate until gate1_isolation_confirmed is set.**

---

## PHASE 2 — Actual Output (Automate)

**Active role: Automate.**

Capture the actual output from API documentation, connector definition, or last known
response. Report what the system produces exactly. Include unexpected fields not in the spec.
Do not adjust any field to match Phase 1. Do not analyze or classify.

### Actual Output

```
[actual output — verbatim, unmodified]
```

### GATE 2 — Actual Completeness

Automate confirms:

1. Completeness: Actual output is captured in full — no truncation, no summarization,
   no inference about what the output "should" be — [CONFIRMED / NOT CONFIRMED]

Gate status: [PASS — CONFIRMED / NEEDS COMPLETION]

Set frontmatter: `gate2_actual_complete: true` if confirmed; `false` otherwise.

**Do not advance to Phase 3 until gate2_actual_complete is set.**

---

## PHASE 3 — Diff and Classification (Both Roles)

**Active roles: both.**
Automate determines match/mismatch. Connectors Contract Expert validates and populates
Element Type — carry forward from Phase 1 wherever possible; apply fixed vocabulary to
any new mismatch rows using the same six-term list.

Compare each expected row (Phase 1) against the actual output (Phase 2).
For rows that match: no row in the mismatch table.
For rows that mismatch: add to the table below.

**Do not write root cause hypotheses in this phase.** Classification only.

**All four required columns must be filled on every mismatch row.**
**Blank cells in Element Type, Severity, or Spec Clause are a gate failure condition.**

### Mismatch Classification Table

| # | Field / Element | Element Type | Actual Value or Shape | Severity | Spec Clause |
|---|-----------------|-------------|----------------------|----------|-------------|

**Severity vocabulary:** `breaking | degraded | cosmetic`
**Element Type vocabulary:** `schema-field | auth-handshake | action-payload | trigger-payload | error-shape | metadata`

### GATE 3 — Classification Completeness

Confirm all four items. Write CONFIRMED or NOT CONFIRMED after the dash.

1. No Severity cells blank on any mismatch row — [CONFIRMED / NOT CONFIRMED]
2. No Spec Clause cells blank on any mismatch row — [CONFIRMED / NOT CONFIRMED]
3. No Element Type cells blank on any mismatch row — [CONFIRMED / NOT CONFIRMED]
4. No root cause hypotheses appear anywhere in Phase 3 — [CONFIRMED / NOT CONFIRMED]

Gate status: [PASS — all four CONFIRMED / NEEDS COMPLETION — list unconfirmed items]

Set frontmatter: `gate3_diff_complete: true` if all four confirmed; `false` otherwise.

**Do not advance to Phase 4 until gate3_diff_complete is set.**

---

## PHASE 4 — Root Cause Analysis (Automate, validated by Connectors Contract Expert)

For each mismatch row from Phase 3, write one finding block.
Fill all six sub-fields. Do not skip any sub-field.
Do not write a severity tally here — Phase 4B handles calibration.

---
**Finding F-[NN] — [Field / Element name]**

- Element type: [from Phase 3]
- Severity: [from Phase 3]
- Spec clause: [from Phase 3]
- Observed deviation: [specific field, shape, or value mismatch — not generic]
- Root cause hypothesis: [named connector-domain mechanism — schema version mismatch,
  auth handshake gap, action-payload field rename, trigger-payload envelope mismatch,
  error-shape deviation, metadata field omission; not "unknown" alone]
- Suggested resolution: [specific action — name the spec clause, schema field, or API
  version to check; not "investigate further" alone]

---

*(Repeat for each mismatch.)*

---

## PHASE 4B — Severity Calibration (Standalone)

**Do not merge Phase 4 and Phase 4B.**
**Active role: Connectors Contract Expert.**
**No new findings are written here. CONTRACT DELTA does not begin until GATE 4B passes.**

Count every finding from Phase 4 by severity level.

### Severity Tally Table

| Severity | Count |
|----------|-------|
| breaking | |
| degraded | |
| cosmetic | |
| **Total** | |

### Calibration Assessment

Review the tally. Is the distribution calibrated? If all findings are at one level, justify
explicitly. If the distribution spans multiple levels, confirm it reflects genuine severity
differences.

[Assessment here]

### GATE 4B — Calibration Gate

Confirm both items. Write CONFIRMED or NOT CONFIRMED after the dash.

1. Severity tally complete — total matches finding count from Phase 4 —
   [CONFIRMED / NOT CONFIRMED]
2. Severity distribution reviewed — not all one level unless explicitly justified —
   [CONFIRMED / NOT CONFIRMED]

Gate status: [PASS — both CONFIRMED / NEEDS COMPLETION]

Set frontmatter: `gate4b_calibration_confirmed: true` if both confirmed; `false` otherwise.

**CONTRACT DELTA does not begin until gate4b_calibration_confirmed is set.**

---

## CONTRACT DELTA

List spec clauses requiring amendment based on Phase 4 findings.
Reference finding IDs. Format for direct input into the finding lifecycle.

| Finding | Spec Clause | Amendment Type | Priority |
|---------|-------------|---------------|----------|

**Amendment types:** `add | remove | revise | clarify`
```

---

## V-02: Phrasing Register — Imperative Second-Person Command Form

**Axis:** Phrasing register — all instructions rewritten as direct second-person commands with mandatory STOP markers at every phase boundary; structural gates and mechanisms identical to V-05 R3.

**Hypothesis:** R1–R3 used descriptive or prescriptive third-person language: "The expected output is the contract"; "The Automate engineer captures..."; "Write the complete expected output." Descriptive language describes what should happen; imperative language commands what to do now and where to stop. The hypothesis: imperative STOP-marker form ("Write the expected table now. Stop. Confirm GATE 1. Do not write Phase 2 until GATE 1 passes.") reduces phase-bleed by converting passive reading into active step execution. This matters most for C-11 (classification-before-analysis gate) — the most common trace-contract failure is writing root causes while building the diff. An explicit "Stop. Do not write root causes. Classify only." is a harder mechanical signal than "No root cause hypotheses in this phase." The structural gates (element-type column, Phase 4B, full frontmatter, CONFIRMED declarations) are unchanged.

```
---
skill: trace-contract
topic: {{topic}}
date: {{date}}
gate1_isolation_confirmed: pending
gate2_actual_complete: pending
gate3_diff_complete: pending
gate4b_calibration_confirmed: pending
---

# Trace: Contract vs. Actual — {{topic}}

You are running /trace:contract as Automate, supported by the Connectors Contract Expert.
Execute each phase in order. At each GATE, write CONFIRMED or NOT CONFIRMED for every item.
Do not advance to the next phase until the current GATE is fully confirmed.

---

## PHASE 1 — Write the Expected Output

Open the spec contract for {{topic}} now.
Do not run the connector. Do not look at any actual output. Spec only.

Write every field, endpoint, payload envelope, auth mechanism, and error shape the spec
defines. Use the table below. One row per contract element.

**Element-type vocabulary. Use exactly these terms — no others:**
`schema-field | auth-handshake | action-payload | trigger-payload | error-shape | metadata`

Write the expected field contract now:

| Field / Element | Element Type | Expected Value or Shape | Spec Clause |
|-----------------|-------------|------------------------|-------------|

Do not leave Element Type blank on any row.
Do not leave Spec Clause blank on any row.
When the table is complete, stop writing. Go to GATE 1. Do not write Phase 2 first.

### GATE 1 — Confirm Before Advancing

Write CONFIRMED or NOT CONFIRMED after the dash for each item.

1. Expected output complete — every spec-defined element has a row — nothing omitted —
   [CONFIRMED / NOT CONFIRMED]
2. Isolation: actual output was not referenced during this phase — not just ordered after,
   but not consulted at all — [CONFIRMED / NOT CONFIRMED]
3. No Element Type cell is blank — every row has a value from the fixed vocabulary —
   [CONFIRMED / NOT CONFIRMED]
4. No Spec Clause cell is blank — every row names a section or field — [CONFIRMED / NOT CONFIRMED]

Set: `gate1_isolation_confirmed: true` if all four CONFIRMED; `false` otherwise.
Update frontmatter now.

Stop. Do not write Phase 2 until gate1_isolation_confirmed is set to true.

---

## PHASE 2 — Capture the Actual Output

Run the connector or read the current API response now.
Record the actual output exactly as produced.
Include all fields — including unexpected ones not in the spec.
Do not edit, summarize, adjust, or analyze. Verbatim only.

Write the actual output now:

```
[actual output — verbatim]
```

When the actual output is recorded, stop writing. Go to GATE 2.

### GATE 2 — Confirm Before Advancing

1. Actual output is complete and unmodified — no truncation, no cleanup, no inference —
   [CONFIRMED / NOT CONFIRMED]

Set: `gate2_actual_complete: true` if CONFIRMED; `false` otherwise. Update frontmatter now.

Stop. Do not write Phase 3 until gate2_actual_complete is set to true.

---

## PHASE 3 — Classify Mismatches

Compare the expected table (Phase 1) against the actual output (Phase 2) row by row.
For each expected element, determine: match or mismatch.
For mismatches only, add a row to the classification table.

Stop. Do not write root cause hypotheses anywhere in this phase.
Do not explain why a field differs. Classify only.
Root causes go in Phase 4. Not here.

**Every mismatch row must have all four required columns filled.**
**Blank cells in Element Type, Severity, or Spec Clause are a gate failure condition.**
**Fill every cell before confirming GATE 3.**

Write the mismatch classification table now:

| # | Field / Element | Element Type | Actual Value or Shape | Severity | Spec Clause |
|---|-----------------|-------------|----------------------|----------|-------------|

**Severity vocabulary:** `breaking | degraded | cosmetic`
**Element Type vocabulary:** `schema-field | auth-handshake | action-payload | trigger-payload | error-shape | metadata`

When the table is complete, stop writing. Go to GATE 3. Do not write Phase 4 first.

### GATE 3 — Confirm Before Advancing

Write CONFIRMED or NOT CONFIRMED after the dash for each item.

1. No Severity cells blank on any mismatch row — [CONFIRMED / NOT CONFIRMED]
2. No Spec Clause cells blank on any mismatch row — [CONFIRMED / NOT CONFIRMED]
3. No Element Type cells blank on any mismatch row — [CONFIRMED / NOT CONFIRMED]
4. No root cause hypotheses appear anywhere in Phase 3 — [CONFIRMED / NOT CONFIRMED]

Set: `gate3_diff_complete: true` if all four CONFIRMED; `false` otherwise. Update frontmatter now.

Stop. Do not write Phase 4 until gate3_diff_complete is set to true.

---

## PHASE 4 — Write Findings

For each mismatch row from Phase 3, write one finding.
Fill all six sub-fields for every finding. Do not skip any sub-field.
Do not write a severity tally or calibration notes here — that is Phase 4B.

Write findings now:

---
**Finding F-[NN] — [Field / Element]**

- Element type: [from Phase 3 — carry forward; do not reclassify]
- Severity: [from Phase 3 — carry forward; do not re-rate until Phase 4B]
- Spec clause: [from Phase 3]
- Observed deviation: [what differed — specific, not generic]
- Root cause hypothesis: [name a connector-domain mechanism — schema version, auth
  handshake gap, action-payload field rename, trigger-payload envelope mismatch,
  error-shape deviation, metadata field omission; not "unknown" alone]
- Suggested resolution: [specific next action — name the spec amendment, schema field,
  API version, or auth flow step; not "investigate further" alone]

---

When all findings are written, stop writing. Go to Phase 4B.
Do not write CONTRACT DELTA.

---

## PHASE 4B — Calibrate Severity (Standalone — Do Not Merge with Phase 4)

This phase has one task. Count findings by severity level. Review the distribution.
Nothing else happens here.

Count all findings from Phase 4 now:

| Severity | Count |
|----------|-------|
| breaking | |
| degraded | |
| cosmetic | |
| **Total** | |

Write the calibration assessment now:

[Is the distribution calibrated? If all one level, justify explicitly. If multiple levels,
confirm they reflect genuine severity differences — not uniform assignment.]

When the tally and assessment are complete, stop. Go to GATE 4B.

### GATE 4B — Confirm Before Advancing

Write CONFIRMED or NOT CONFIRMED after the dash for each item.

1. Severity tally complete — total matches Phase 4 finding count — [CONFIRMED / NOT CONFIRMED]
2. Severity distribution reviewed — not all one level unless explicitly justified —
   [CONFIRMED / NOT CONFIRMED]

Set: `gate4b_calibration_confirmed: true` if both CONFIRMED; `false` otherwise.
Update frontmatter now.

Stop. Do not write CONTRACT DELTA until gate4b_calibration_confirmed is set to true.

---

## CONTRACT DELTA

Write spec clauses requiring amendment. Reference finding IDs from Phase 4.

| Finding | Spec Clause | Amendment Type | Priority |
|---------|-------------|---------------|----------|

**Amendment types:** `add | remove | revise | clarify`
```

---

## V-03: Inertia Framing — Actual Output as Status-Quo Default

**Axis:** Inertia framing — the actual output is explicitly framed as "what the connector delivers under inertia" (default behavior, no spec-compliance effort); the expected output is framed as "the committed contract" (what was promised). Severity is redefined as the consequence of inertia for the promise. GATE 4B includes an explicit anti-bias clause to prevent inertia framing from producing uniform breaking severity.

**Hypothesis:** In R1–R3, the actual output was semantically neutral — "what was produced." Inertia framing activates a different mental model: the analyst measures the gap between a spec promise and the connector's default behavior. This should improve C-09 (severity calibration) because the three severity levels map naturally to inertia distances: breaking = inertia structurally violates the promise; degraded = inertia weakens it; cosmetic = inertia diverges in form but the guarantee holds. The risk: inertia framing may prime analysts to see all deviations as breaking (if the connector is far from the spec), producing a uniform distribution without justification. GATE 4B addresses this with the clause "inertia framing is not automatic justification for uniform breaking." The structural gates are identical to V-05 R3. Scoring discriminator: does the anti-bias clause preserve C-09, or does framing pressure override it?

```
---
skill: trace-contract
topic: {{topic}}
date: {{date}}
gate1_isolation_confirmed: pending
gate2_actual_complete: pending
gate3_diff_complete: pending
gate4b_calibration_confirmed: pending
---

# Trace: Contract vs. Actual — {{topic}}

**Roles:** Automate · Connectors Contract Expert

**Framing for this trace:**

The spec defines what was *promised* — the committed contract. A connector has two states:
what it delivers when actively maintained against the spec, and what it delivers under
inertia — the default behavior when no spec-compliance effort is applied.

- **Phase 1** captures the *committed contract*: what the spec says must hold.
- **Phase 2** captures the *inertia output*: what the connector delivers by default.
- **Phase 3** classifies the gap between promise and inertia.
- **Severity** measures the consequence of inertia for the contract guarantee:
  - `breaking` — inertia structurally violates the contract; the promise cannot be met as-is
  - `degraded` — inertia partially violates the contract; the promise weakens but is partially met
  - `cosmetic` — inertia diverges in form but the contract guarantee holds

---

## PHASE 1 — The Committed Contract (Expected Output)

Record the contract as the spec defines it. This is the promise. Do not reference the
inertia output. Spec only.

For every field, endpoint, payload, auth mechanism, and error shape the spec defines, add
one row. Element-type vocabulary:

`schema-field | auth-handshake | action-payload | trigger-payload | error-shape | metadata`

### Committed Contract Table

| Field / Element | Element Type | Promised Value or Shape | Spec Clause |
|-----------------|-------------|------------------------|-------------|

*(No Element Type cell blank. No Spec Clause cell blank.)*

### GATE 1 — Contract Isolation Check

Confirm each item. Write CONFIRMED or NOT CONFIRMED after the dash.

1. Contract completeness: every spec-defined element has a row —
   [CONFIRMED / NOT CONFIRMED]
2. Isolation: inertia output was not referenced during this phase — not just ordered
   after, but not consulted at all — [CONFIRMED / NOT CONFIRMED]
3. Element type coverage: no Element Type cell is blank; all values from the fixed
   vocabulary — [CONFIRMED / NOT CONFIRMED]

Set frontmatter: `gate1_isolation_confirmed: true` if all three CONFIRMED; `false` otherwise.

**Do not capture the inertia output until gate1_isolation_confirmed is set.**

---

## PHASE 2 — The Inertia Output (Actual Output)

Capture what the connector delivers under default behavior — no patching, no spec-compliance
configuration, no active enforcement. This is the inertia state.

Record verbatim. Include all fields, including fields absent from the spec.

### Inertia Output

```
[inertia output — verbatim, unmodified]
```

### GATE 2 — Inertia Capture Completeness

1. Inertia output is complete and unmodified — no truncation, no adjustment toward the
   contract — [CONFIRMED / NOT CONFIRMED]

Set frontmatter: `gate2_actual_complete: true` if CONFIRMED; `false` otherwise.

**Do not classify until gate2_actual_complete is set.**

---

## PHASE 3 — Gap Classification: Promise vs. Inertia

Compare the committed contract (Phase 1) against the inertia output (Phase 2) element by
element. For mismatches only, classify the gap. Do not write root causes here.

**Severity applies the inertia-framing definitions:**
- `breaking` — inertia structurally violates the contract element; promise cannot be met
- `degraded` — inertia weakens the element; promise partially met
- `cosmetic` — inertia diverges in form but the contract guarantee holds

**All four required columns must be filled on every mismatch row.**
**Blank cells in Element Type, Severity, or Spec Clause are a gate failure condition.**

### Contract Gap Table

| # | Field / Element | Element Type | Inertia Value or Shape | Severity | Spec Clause |
|---|-----------------|-------------|----------------------|----------|-------------|

**Element Type vocabulary:** `schema-field | auth-handshake | action-payload | trigger-payload | error-shape | metadata`

### GATE 3 — Gap Classification Completeness

Confirm all four items. Write CONFIRMED or NOT CONFIRMED after the dash.

1. No Severity cells blank on any gap row — [CONFIRMED / NOT CONFIRMED]
2. No Spec Clause cells blank on any gap row — [CONFIRMED / NOT CONFIRMED]
3. No Element Type cells blank on any gap row — [CONFIRMED / NOT CONFIRMED]
4. No root cause hypotheses appear in Phase 3 — [CONFIRMED / NOT CONFIRMED]

Set frontmatter: `gate3_diff_complete: true` if all four CONFIRMED; `false` otherwise.

**Do not advance to Phase 4 until gate3_diff_complete is set.**

---

## PHASE 4 — Root Cause Analysis (Why Inertia Misses the Promise)

For each gap row from Phase 3, explain which connector-domain mechanism causes the inertia
gap. Fill all six sub-fields.

---
**Finding F-[NN] — [Field / Element]**

- Element type: [from Phase 3]
- Severity: [from Phase 3]
- Spec clause: [from Phase 3]
- Observed gap: [how inertia deviates from the promise — specific, not generic]
- Root cause hypothesis: [named connector-domain mechanism driving the inertia gap —
  schema version, auth handshake gap, action-payload field rename, trigger-payload envelope
  mismatch, error-shape deviation, metadata omission; not "unknown" alone]
- Suggested resolution: [specific corrective action that closes the inertia-to-contract gap;
  name the spec clause, schema field, or API version; not "investigate further" alone]

---

## PHASE 4B — Severity Calibration (Standalone)

**Do not merge Phase 4 and Phase 4B. This phase runs alone.**
**CONTRACT DELTA does not begin until GATE 4B passes.**

Count findings from Phase 4 by severity level.

### Severity Tally Table

| Severity | Count |
|----------|-------|
| breaking | |
| degraded | |
| cosmetic | |
| **Total** | |

### Inertia Calibration Assessment

Review the tally in the context of the inertia framing. A connector near the contract will
show few breaking findings; one far from it may legitimately show more. Consider: does the
distribution reflect the actual gap between committed contract and inertia output?

**Important:** Inertia framing does not automatically justify all-breaking severity. If all
findings are breaking, justify explicitly why inertia structurally violates every contract
element — do not cite the framing as the reason.

[Calibration assessment here]

### GATE 4B — Calibration Gate

Confirm both items. Write CONFIRMED or NOT CONFIRMED after the dash.

1. Severity tally complete — total matches finding count from Phase 4 —
   [CONFIRMED / NOT CONFIRMED]
2. Severity distribution reviewed — not all one level unless explicitly justified;
   inertia framing alone is not a justification for uniform breaking —
   [CONFIRMED / NOT CONFIRMED]

Set frontmatter: `gate4b_calibration_confirmed: true` if both CONFIRMED; `false` otherwise.

**Do not write CONTRACT DELTA until gate4b_calibration_confirmed is set.**

---

## CONTRACT DELTA

List spec clauses requiring amendment to close the contract-to-inertia gap.
Reference finding IDs from Phase 4.

| Finding | Spec Clause | Amendment Type | Priority |
|---------|-------------|---------------|----------|

**Amendment types:** `add | remove | revise | clarify`
```

---

## V-04: Two-Axis Combination — Role Sequence + Phrasing Register (V-01 + V-02)

**Axes combined:** Role sequence (Connectors expert leads Phase 1) + phrasing register (imperative second-person throughout).

**Hypothesis:** V-01 and V-02 address orthogonal failure modes. V-01 prevents retroactive domain labeling by giving the domain expert ownership of Phase 1 construction. V-02 prevents phase-bleed by replacing descriptive instructions with STOP-marker commands. These axes are non-competing: role sequence determines *who* acts at Phase 1; phrasing register determines *how* instructions are delivered in all phases. Combining them should produce a prompt where element-type vocabulary originates from domain expertise and phase-bleed is minimized by imperative STOP signals. The full R3 gate apparatus is preserved. Predicted score: 100. Key question for scoring: does expert-led Phase 1 in imperative form produce a cleaner element-type column in Phase 3 than Automate-led Phase 1 (V-02) alone?

```
---
skill: trace-contract
topic: {{topic}}
date: {{date}}
gate1_isolation_confirmed: pending
gate2_actual_complete: pending
gate3_diff_complete: pending
gate4b_calibration_confirmed: pending
---

# Trace: Contract vs. Actual — {{topic}}

**Roles:**
- **Connectors Contract Expert** — active in Phase 1; validates element-type taxonomy in Phase 3; leads Phase 4B
- **Automate** — active in Phase 2; co-owns Phase 3; leads Phase 4

**Role sequence:** Connectors Contract Expert activates first.
Automate does not activate until gate1_isolation_confirmed is set.

---

## PHASE 1 — Write the Expected Contract Table (Connectors Contract Expert)

Connectors Contract Expert: open the spec for {{topic}} now.
Do not run the connector. Do not look at actual output. Spec only.

Write every field, payload envelope, auth mechanism, and error shape the spec defines.
Use the element-type vocabulary to classify each row as you construct it:

`schema-field | auth-handshake | action-payload | trigger-payload | error-shape | metadata`

Apply the most specific term. If a row spans two types, split it. Do not leave any
Element Type cell blank — you own this taxonomy.

Write the expected contract table now:

| Field / Element | Element Type | Expected Value or Shape | Spec Clause |
|-----------------|-------------|------------------------|-------------|

Do not leave Element Type blank on any row.
Do not leave Spec Clause blank on any row.
When the table is complete, stop writing. Confirm GATE 1. Do not write Phase 2 first.

### GATE 1 — Isolation + Domain Completeness

Connectors Contract Expert confirms. Write CONFIRMED or NOT CONFIRMED after the dash.

1. Expected table covers all spec-defined elements — nothing omitted —
   [CONFIRMED / NOT CONFIRMED]
2. Actual output was not referenced during this phase — not just ordered after,
   but not consulted at all — [CONFIRMED / NOT CONFIRMED]
3. No Element Type cell is blank — every row has a value from the fixed vocabulary —
   [CONFIRMED / NOT CONFIRMED]
4. No Spec Clause cell is blank — every row names a section or field — [CONFIRMED / NOT CONFIRMED]

Set: `gate1_isolation_confirmed: true` if all four CONFIRMED; `false` otherwise. Update frontmatter.

Stop. Automate does not activate until gate1_isolation_confirmed is true.

---

## PHASE 2 — Capture the Actual Output (Automate)

Automate: run the connector now. Capture what it produces. Record verbatim.
Include all fields — including unexpected ones not in the spec.
Do not edit, summarize, adjust, or classify. Verbatim only.

Write the actual output now:

```
[actual output — verbatim]
```

When recorded, stop writing. Confirm GATE 2. Do not write Phase 3 first.

### GATE 2 — Actual Completeness

1. Actual output is complete and unmodified — no truncation, no inference —
   [CONFIRMED / NOT CONFIRMED]

Set: `gate2_actual_complete: true` if CONFIRMED; `false` otherwise. Update frontmatter.

Stop. Do not write Phase 3 until gate2_actual_complete is true.

---

## PHASE 3 — Classify Mismatches (Both Roles)

Both roles active. Automate determines match/mismatch. Connectors Contract Expert validates
element-type labels — carry forward from Phase 1; apply vocabulary to any new mismatch rows.

Compare Phase 1 against Phase 2 row by row. Add a row to the table for mismatches only.

Stop. Do not write root causes here. Root causes go in Phase 4. Not here. Classify only.

Every mismatch row must have all four required columns filled.
Blank cells in Element Type, Severity, or Spec Clause are a gate failure condition.
Fill every cell before confirming GATE 3.

Write the mismatch classification table now:

| # | Field / Element | Element Type | Actual Value or Shape | Severity | Spec Clause |
|---|-----------------|-------------|----------------------|----------|-------------|

**Severity vocabulary:** `breaking | degraded | cosmetic`
**Element Type vocabulary:** `schema-field | auth-handshake | action-payload | trigger-payload | error-shape | metadata`

When the table is complete, stop writing. Confirm GATE 3. Do not write Phase 4 first.

### GATE 3 — Classification Completeness

Write CONFIRMED or NOT CONFIRMED after the dash for each item.

1. No Severity cells blank on any mismatch row — [CONFIRMED / NOT CONFIRMED]
2. No Spec Clause cells blank on any mismatch row — [CONFIRMED / NOT CONFIRMED]
3. No Element Type cells blank on any mismatch row — [CONFIRMED / NOT CONFIRMED]
4. No root cause hypotheses appear anywhere in Phase 3 — [CONFIRMED / NOT CONFIRMED]

Set: `gate3_diff_complete: true` if all four CONFIRMED; `false` otherwise. Update frontmatter.

Stop. Do not write Phase 4 until gate3_diff_complete is true.

---

## PHASE 4 — Write Findings (Both Roles)

For each mismatch row from Phase 3, write one finding. Fill all six sub-fields.
Do not calibrate severity here — Phase 4B handles that. Do not write CONTRACT DELTA here.

Write findings now:

---
**Finding F-[NN] — [Field / Element]**

- Element type: [from Phase 3]
- Severity: [from Phase 3]
- Spec clause: [from Phase 3]
- Observed deviation: [specific mismatch — not generic]
- Root cause hypothesis: [named connector-domain mechanism — schema version, auth handshake
  gap, action-payload field rename, trigger-payload envelope mismatch, error-shape deviation,
  metadata omission; not "unknown" alone]
- Suggested resolution: [specific action — name the spec clause, schema field, API version,
  or auth flow step; not "investigate further" alone]

---

When all findings are written, stop writing. Go to Phase 4B. Do not write CONTRACT DELTA.

---

## PHASE 4B — Calibrate Severity (Standalone — Do Not Merge with Phase 4)

This phase has one task: verify severity distribution is calibrated. Nothing else.

Count all findings from Phase 4 by severity level now:

| Severity | Count |
|----------|-------|
| breaking | |
| degraded | |
| cosmetic | |
| **Total** | |

Write the calibration assessment now:

[Assessment — if all one level, justify explicitly; if multiple levels, confirm they
reflect genuine severity differences in the connector contract domain]

When tally and assessment are written, stop. Confirm GATE 4B.

### GATE 4B — Calibration Gate

Write CONFIRMED or NOT CONFIRMED after the dash for each item.

1. Severity tally complete — total matches Phase 4 finding count — [CONFIRMED / NOT CONFIRMED]
2. Severity distribution reviewed — not all one level unless explicitly justified —
   [CONFIRMED / NOT CONFIRMED]

Set: `gate4b_calibration_confirmed: true` if both CONFIRMED; `false` otherwise. Update frontmatter.

Stop. Do not write CONTRACT DELTA until gate4b_calibration_confirmed is true.

---

## CONTRACT DELTA

Write spec clauses requiring amendment. Reference finding IDs from Phase 4.

| Finding | Spec Clause | Amendment Type | Priority |
|---------|-------------|---------------|----------|

**Amendment types:** `add | remove | revise | clarify`
```

---

## V-05: Full Synthesis — V-01 + V-02 + V-03 + All R3 Mechanisms

**Axes combined:** Role sequence (V-01) + phrasing register (V-02) + inertia framing (V-03), all R3 structural mechanisms preserved intact.

**Hypothesis:** The three R4 behavioral axes address orthogonal failure modes and are non-competing:
- **V-01** prevents retroactive domain labeling — expert vocabulary embedded at Phase 1 source
- **V-02** prevents phase-bleed — imperative STOP markers convert instructions to execution steps
- **V-03** improves severity calibration — inertia framing gives the three severity levels a coherent conceptual anchor; anti-bias clause prevents framing from producing all-breaking results

Layered on top of R3 structural guarantees — CONFIRMED/NOT CONFIRMED declarations (C-14), universal blank-cell gate enforcement (C-15/C-20), six-key frontmatter (C-16/C-19), element-type taxonomy column (C-17), standalone Phase 4B with severity tally (C-18) — V-05 is the ceiling. The only open question is whether V-03's inertia framing interacts with V-01's expert-led Phase 1 in a way that narrows or widens the expected-output scope (experts who think in "what inertia misses" may construct expected tables differently than experts who think in "what the spec says"). GATE 1 anti-contamination clause ("spec only, not what you know the connector does") should prevent this. Predicted score: 100.

```
---
skill: trace-contract
topic: {{topic}}
date: {{date}}
gate1_isolation_confirmed: pending
gate2_actual_complete: pending
gate3_diff_complete: pending
gate4b_calibration_confirmed: pending
---

# Trace: Contract vs. Actual — {{topic}}

**Roles:**
- **Connectors Contract Expert** — leads Phase 1; validates element-type taxonomy in Phase 3; leads Phase 4B calibration
- **Automate** — leads Phase 2; co-owns Phase 3 diff construction; leads Phase 4 root cause analysis

**Role sequence:** Connectors Contract Expert activates first.
Automate does not activate until gate1_isolation_confirmed is set.

**Inertia framing:**
- Phase 1 = *committed contract* — what the spec promises must hold
- Phase 2 = *inertia output* — what the connector delivers by default, without spec-compliance effort
- Severity = consequence of inertia for the promise:
  - `breaking` — inertia structurally violates the contract; promise cannot be met
  - `degraded` — inertia weakens the contract; promise partially met
  - `cosmetic` — inertia diverges in form but contract guarantee holds

---

## PHASE 1 — Write the Committed Contract (Connectors Contract Expert)

Connectors Contract Expert: open the spec for {{topic}} now.
Do not run the connector. Do not reference what you know the connector currently does.
The spec is the only source. Write what the spec promises — not what you expect the
inertia output to be.

Write every field, payload envelope, auth mechanism, and error shape the spec defines.
Classify each row as you construct it using the fixed element-type vocabulary:

`schema-field | auth-handshake | action-payload | trigger-payload | error-shape | metadata`

Apply the most specific term. Split rows that span two types. Do not leave Element Type
blank — you own this column. Do not leave Spec Clause blank.

Write the committed contract table now:

| Field / Element | Element Type | Promised Value or Shape | Spec Clause |
|-----------------|-------------|------------------------|-------------|

When the table is complete, stop writing. Confirm GATE 1. Do not write Phase 2 first.

### GATE 1 — Contract Isolation + Domain Completeness

Connectors Contract Expert confirms. Write CONFIRMED or NOT CONFIRMED after the dash.

1. Contract completeness: every spec-defined element has a row — nothing omitted —
   [CONFIRMED / NOT CONFIRMED]
2. Isolation: inertia output was not referenced during this phase — not just ordered
   after, but not consulted at all — [CONFIRMED / NOT CONFIRMED]
3. No Element Type cell is blank — every row has a value from the fixed vocabulary —
   [CONFIRMED / NOT CONFIRMED]
4. No Spec Clause cell is blank — every row names a section or field — [CONFIRMED / NOT CONFIRMED]

Set: `gate1_isolation_confirmed: true` if all four CONFIRMED; `false` otherwise. Update frontmatter.

Stop. Automate does not activate until gate1_isolation_confirmed is true.

---

## PHASE 2 — Capture the Inertia Output (Automate)

Automate: run the connector now. Record the inertia output — default behavior, no patching.
Include all fields, including unexpected ones not in the spec.
Do not edit, summarize, adjust, or analyze. Verbatim only.

Write the inertia output now:

```
[inertia output — verbatim, unmodified]
```

When recorded, stop writing. Confirm GATE 2. Do not write Phase 3 first.

### GATE 2 — Inertia Capture Completeness

1. Inertia output is complete and unmodified — no truncation, no adjustment toward the
   contract — [CONFIRMED / NOT CONFIRMED]

Set: `gate2_actual_complete: true` if CONFIRMED; `false` otherwise. Update frontmatter.

Stop. Do not write Phase 3 until gate2_actual_complete is true.

---

## PHASE 3 — Classify Contract Gaps (Both Roles)

Both roles active. Automate determines match/mismatch. Connectors Contract Expert validates
element-type labels — carry forward from Phase 1 wherever possible; apply vocabulary to
any new mismatch rows.

Compare Phase 1 against Phase 2 element by element. Add a row for mismatches only.

Stop. Do not write root causes here. Root causes go in Phase 4. Not here.
Classify the gap using the inertia-framing severity definitions only.

Every mismatch row must have all four required columns filled.
Blank cells in Element Type, Severity, or Spec Clause are a gate failure condition.
Fill every cell before confirming GATE 3.

Write the contract gap classification table now:

| # | Field / Element | Element Type | Inertia Value or Shape | Severity | Spec Clause |
|---|-----------------|-------------|----------------------|----------|-------------|

**Severity vocabulary (inertia framing):**
- `breaking` — inertia structurally violates the contract; promise cannot be met
- `degraded` — inertia weakens the contract; promise partially met
- `cosmetic` — inertia diverges in form but contract guarantee holds

**Element Type vocabulary:**
`schema-field | auth-handshake | action-payload | trigger-payload | error-shape | metadata`

When the table is complete, stop writing. Confirm GATE 3. Do not write Phase 4 first.

### GATE 3 — Gap Classification Completeness

Write CONFIRMED or NOT CONFIRMED after the dash for each item.

1. No Severity cells blank on any mismatch row — [CONFIRMED / NOT CONFIRMED]
2. No Spec Clause cells blank on any mismatch row — [CONFIRMED / NOT CONFIRMED]
3. No Element Type cells blank on any mismatch row — [CONFIRMED / NOT CONFIRMED]
4. No root cause hypotheses appear anywhere in Phase 3 — [CONFIRMED / NOT CONFIRMED]

Set: `gate3_diff_complete: true` if all four CONFIRMED; `false` otherwise. Update frontmatter.

Stop. Do not write Phase 4 until gate3_diff_complete is true.

---

## PHASE 4 — Root Cause Analysis: Why Inertia Misses the Promise (Both Roles)

For each gap row from Phase 3, explain which connector-domain mechanism causes the inertia
gap. Fill all six sub-fields. Carry forward element type and severity from Phase 3 —
do not reclassify until Phase 4B.

Write findings now:

---
**Finding F-[NN] — [Field / Element]**

- Element type: [from Phase 3 — carry forward]
- Severity: [from Phase 3 — carry forward; calibration happens in Phase 4B]
- Spec clause: [from Phase 3]
- Observed gap: [how inertia deviates from the promise — specific, not generic]
- Root cause hypothesis: [named connector-domain mechanism driving the inertia gap —
  schema version mismatch, auth handshake gap, action-payload field rename, trigger-payload
  envelope mismatch, error-shape deviation, metadata field omission; not "unknown" alone]
- Suggested resolution: [specific corrective action that closes the inertia-to-contract gap;
  name the spec amendment, schema field, API version, or auth flow step; not "investigate
  further" alone]

---

When all findings are written, stop writing. Go to Phase 4B. Do not write CONTRACT DELTA.

---

## PHASE 4B — Severity Calibration (Standalone — Do Not Merge with Phase 4)

**Connectors Contract Expert leads. This phase runs alone.**
**No new findings are written here. CONTRACT DELTA does not begin until GATE 4B passes.**

Count all findings from Phase 4 by severity level now:

### Severity Tally Table

| Severity | Count |
|----------|-------|
| breaking | |
| degraded | |
| cosmetic | |
| **Total** | |

### Inertia Calibration Assessment

Review the tally in the context of the inertia framing. Consider: does the distribution
reflect the actual gap between the committed contract and the inertia output? A connector
near the contract will show few breaking findings; one far from it may legitimately show
more.

**Critical:** Inertia framing is not automatic justification for uniform breaking severity.
If all findings are breaking, justify explicitly why inertia structurally violates every
single contract element — not because the framing makes violation seem likely, but because
each specific element was verified to fail the breaking threshold.

Write the calibration assessment now:

[Assessment — include specific justification if all one level; confirm genuine severity
differences if multiple levels]

When tally and assessment are written, stop. Confirm GATE 4B.

### GATE 4B — Calibration Gate

Write CONFIRMED or NOT CONFIRMED after the dash for each item.

1. Severity tally complete — total matches Phase 4 finding count — [CONFIRMED / NOT CONFIRMED]
2. Severity distribution reviewed — not all one level unless each element individually
   justified at that level; inertia framing alone is not sufficient justification —
   [CONFIRMED / NOT CONFIRMED]

Set: `gate4b_calibration_confirmed: true` if both CONFIRMED; `false` otherwise. Update frontmatter.

Stop. Do not write CONTRACT DELTA until gate4b_calibration_confirmed is true.

---

## CONTRACT DELTA

List spec clauses requiring amendment to close the contract-to-inertia gap.
Reference finding IDs from Phase 4.

| Finding | Spec Clause | Amendment Type | Priority |
|---------|-------------|---------------|----------|

**Amendment types:** `add | remove | revise | clarify`

*(Priority reflects calibrated severity from Phase 4B: breaking → P1, degraded → P2,
cosmetic → P3, unless Phase 4B assessment explicitly overrides.)*
```

---

## Round 4 Analysis

### What is new vs. R3

| Axis | What R3 did | What R4 adds |
|------|-------------|--------------|
| Role sequence | Automate led all phases in R1–R3 | Connectors expert leads Phase 1 — domain vocabulary embedded at construction, not retrofitted |
| Phrasing register | Descriptive / prescriptive language | Full imperative second-person with STOP markers between every phase |
| Inertia framing | Actual output was semantically neutral | Actual = "inertia output"; expected = "committed contract"; severity anchored to promise-vs-default gap; GATE 4B anti-bias clause |

### Predicted scoring summary

| V | Key open question | Expected score |
|---|-------------------|----------------|
| V-01 | Does expert-led Phase 1 strengthen C-17/C-07 vs Automate-led baseline? | 100 |
| V-02 | Does imperative STOP form strengthen C-11 vs descriptive baseline? | 100 |
| V-03 | Does inertia framing improve C-09 calibration, or does the anti-bias gate carry all the load? | 100 or 97.5 |
| V-04 | Do V-01 + V-02 compose cleanly — expert domain vocabulary + imperative form? | 100 |
| V-05 | Do all three behavioral axes compose with all four R3 structural mechanisms? | 100 |

### Scoring formula (v4 rubric)

| Tier | Criteria | Max | Weight |
|------|----------|-----|--------|
| Essential | C-01 to C-05 | 5 | 60 pts |
| Recommended | C-06 to C-08 | 3 | 30 pts |
| Aspirational | C-09 to C-20 | 12 | 10 pts |
| **Composite** | | | **(E/5 × 60) + (R/3 × 30) + (A/12 × 10)** |

**Golden:** all essential pass (5/5) AND composite ≥ 80.
