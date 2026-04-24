Written to `simulations/quest/variations/trace-contract-variations-R5-2026-03-14.md`.

---

## Round 5 Variations — Summary

| V | Axis | Key mechanism | Predicted |
|---|------|---------------|-----------|
| **V-01** | Lifecycle — Phase 0 scope | Pre-Phase-1 scope enumeration; GATE 0 fires; completeness verifiable against named commitment | **100** |
| **V-02** | Output format — pre-populated skeleton | Phase 1 begins with committed element list; blank cells = structural incompleteness, not omission | **100** |
| **V-03** | Role sequence — challenge-before-gate | Automate challenges Expert's table before GATE 1 fires; isolation backed by two-reader log | **100** |
| **V-04** | V-01 + V-02 | Phase 0 scope list drives skeleton; dual-enforcement completeness at GATE 0 + GATE 1 | **100** |
| **V-05** | Full synthesis | All three axes + interrogative phrasing + Amendment Type column in CONTRACT DELTA | **100** |

---

## Design decisions

**Baseline encoding (C-21 through C-24 in all five):**
- C-21: Per-element justification table in Phase 4B, group-level justification explicitly named as gate failure
- C-22: `breaking → P1 | degraded → P2 | cosmetic → P3` priority annotation on every CONTRACT DELTA entry
- C-23: "Do not reference what you know the connector currently does" as a named GATE 1 clause
- C-24: Spec Clause enforcement at GATE 1 (4-item gate), not deferred to GATE 3

**Three new R5 axes (R4 axes are now structural defaults):**
- R4 axes (inertia framing, expert-leads-Phase-1, imperative phrasing) baked in everywhere — no longer distinguishing
- R5 axes: lifecycle emphasis, output format, role-sequence challenge variant

**v6 candidate patterns surfaced:**
1. **Phase 0 scope as checkable prior commitment** — Phase 1 completeness verifiable against a named list, not assessed by inspection
2. **Skeleton enforcement** — element omission becomes structurally impossible; blank cells are structural failure, not omission
3. **Challenge log** — converts GATE 1 isolation from self-attestation to two-reader record with flagged/revised tracking
4. **Amendment type taxonomy** (V-05 only) — `add-field | remove-field | change-type | change-enum | change-error-shape | …` as a required CONTRACT DELTA column orthogonal to priority

**Key structural distinction across variations:** V-01/V-04/V-05 have 5 frontmatter keys (adding `gate0_scope_confirmed`), extending C-19 coverage to Phase 0. V-03's challenge log is the only mechanism that makes the C-12/C-14 isolation check verifiable by a second reader's output rather than a self-attested checkbox alone.
ted score:** 100 — all v5 criteria pass; introduces Phase 0 pattern as v6 candidate.

```
---
skill: trace-contract
topic: {{topic}}
date: {{date}}
gate0_scope_confirmed: pending
gate1_isolation_confirmed: pending
gate2_actual_complete: pending
gate3_diff_complete: pending
gate4b_calibration_confirmed: pending
---

# Trace: Contract vs. Actual — {{topic}}

**Roles:**
- **Connectors Contract Expert** — leads Phase 0, Phase 1, Phase 3 domain validation,
  Phase 4B calibration
- **Automate** — leads Phase 2, Phase 4; co-owns Phase 3 diff construction

**Inertia framing:**
- Phase 1 = *committed contract* — what the spec promises must hold
- Phase 2 = *inertia output* — what the connector delivers by default
- Severity = consequence of inertia for the promise:
  - `breaking` — inertia structurally violates the contract
  - `degraded` — inertia weakens the contract; promise partially met
  - `cosmetic` — inertia diverges in form but contract guarantee holds

---

## PHASE 0 — Define the Contract Surface (Connectors Contract Expert)

Before any expected values are written, enumerate the connector elements this run covers.

**In scope:** List every connector element the spec defines that this run will test.
Do not guess what the inertia output will cover. List from the spec only.

| Element Name | Spec Clause | Element Type |
|--------------|-------------|--------------|

Element-type vocabulary:
`schema-field | auth-handshake | action-payload | trigger-payload | error-shape | metadata`

**Out of scope (explicit):** List any spec-defined elements explicitly excluded from this run,
with a one-line reason.

| Element Name | Spec Clause | Exclusion Reason |
|--------------|-------------|-----------------|

### GATE 0 — Scope Completeness

- [ ] In-scope list is derived from the spec — not from knowledge of what the connector
  currently implements or can reach
- [ ] No Element Type cells blank in the in-scope table
- [ ] No Spec Clause cells blank in the in-scope table
- [ ] Out-of-scope exclusions are explicit — nothing silently dropped

Set `gate0_scope_confirmed: true` in frontmatter when all items pass.

**Stop. Phase 1 does not begin until gate0_scope_confirmed is true.**

---

## PHASE 1 — Write the Committed Contract (Connectors Contract Expert)

Connectors Contract Expert: derive expected values from spec only.
The Phase 0 in-scope list defines coverage — Phase 1 must include a row for every
in-scope element. Omitting an in-scope element is a Phase 1 failure.

Do not run the connector. Do not reference what you know the connector currently does.

Element-type vocabulary:
`schema-field | auth-handshake | action-payload | trigger-payload | error-shape | metadata`

| Field / Element | Element Type | Promised Value or Shape | Spec Clause |
|-----------------|-------------|------------------------|-------------|

### GATE 1 — Contract Isolation + Domain Completeness (4 items)

Write CONFIRMED or NOT CONFIRMED after the dash.

1. Contract completeness: every Phase 0 in-scope element has a row — nothing omitted
   — [CONFIRMED / NOT CONFIRMED]
2. Inertia output was not referenced during Phase 1 — not just ordered after, but not
   consulted at all — [CONFIRMED / NOT CONFIRMED]
3. No Element Type cells blank in the committed contract table — [CONFIRMED / NOT CONFIRMED]
4. No Spec Clause cells blank in the committed contract table — [CONFIRMED / NOT CONFIRMED]
   *(Do not reference what you know the connector currently does — spec derivation only.)*

Set `gate1_isolation_confirmed: true` in frontmatter when all items pass.

**Stop. Automate does not activate until gate1_isolation_confirmed is true.**

---

## PHASE 2 — Capture the Inertia Output (Automate)

Automate: run the connector. Record verbatim. Do not patch toward the contract.
Include all fields returned, including unexpected ones not in the spec.

```
[inertia output — verbatim, unmodified]
```

### GATE 2

- [ ] Inertia output is complete and unmodified — [CONFIRMED / NOT CONFIRMED]

Set `gate2_actual_complete: true`. Update frontmatter.

**Stop. Do not write Phase 3 until gate2_actual_complete is true.**

---

## PHASE 3 — Classify Contract Gaps (Both Roles)

Both roles active. Compare Phase 1 against Phase 2 element by element.

**Stop. Do not write root causes here. Root causes go in Phase 4. Not here. Classify only.**

Every mismatch row requires all four required columns. Blank cells in Element Type,
Severity, or Spec Clause are a gate failure condition.

| # | Field / Element | Element Type | Inertia Value or Shape | Severity | Spec Clause |
|---|-----------------|-------------|----------------------|----------|-------------|

Severity vocabulary (inertia framing):
`breaking | degraded | cosmetic`

Element-type vocabulary:
`schema-field | auth-handshake | action-payload | trigger-payload | error-shape | metadata`

### GATE 3 — Gap Classification Completeness (4 items)

Write CONFIRMED or NOT CONFIRMED after the dash.

1. No Severity cells blank on any mismatch row — [CONFIRMED / NOT CONFIRMED]
2. No Spec Clause cells blank on any mismatch row — [CONFIRMED / NOT CONFIRMED]
3. No Element Type cells blank on any mismatch row — [CONFIRMED / NOT CONFIRMED]
4. No root cause hypotheses appear anywhere in Phase 3 — [CONFIRMED / NOT CONFIRMED]

Set `gate3_diff_complete: true`. Update frontmatter.

**Stop. Do not write Phase 4 until gate3_diff_complete is true.**

---

## PHASE 4 — Root Cause Analysis (Both Roles)

For each gap row from Phase 3, write a finding. Carry element type and severity from
Phase 3 — do not reclassify until Phase 4B.

---
**Finding F-[NN] — [Field / Element]**

- Element type: [from Phase 3 — carry forward]
- Severity: [from Phase 3 — carry forward]
- Spec clause: [from Phase 3]
- Observed gap: [specific deviation — not generic]
- Root cause hypothesis: [named connector-domain mechanism — schema version mismatch /
  auth handshake gap / action-payload field rename / trigger-payload envelope mismatch /
  error-shape deviation / metadata field omission; not "unknown" alone]
- Suggested resolution: [specific corrective action — name the spec amendment, schema
  field, API version, or auth flow step; not "investigate further" alone]

---

**Stop. Do not write Phase 4B until all Phase 4 findings are complete.**

---

## PHASE 4B — Severity Calibration (Standalone — Do Not Merge with Phase 4)

Connectors Contract Expert leads. No new findings are written here.
CONTRACT DELTA does not begin until GATE 4B passes.

### Severity Tally Table

| Severity | Count | Finding IDs |
|----------|-------|-------------|
| breaking | | |
| degraded | | |
| cosmetic | | |
| **Total** | | |

### Per-Element Justification

For each finding, justify its severity level individually. Group-level justification
("all breaking because inertia implies full replacement") is a gate failure condition.

| Finding | Assigned Severity | Element-Level Justification |
|---------|------------------|-----------------------------|

### Calibration Assessment

Review the tally. Does the distribution reflect the actual gap between committed
contract and inertia output? Inertia framing is not automatic justification for
uniform severity — each element must be individually justified.

### GATE 4B — Calibration Gate (3 items)

Write CONFIRMED or NOT CONFIRMED after the dash.

1. Severity tally complete — total matches Phase 4 finding count
   — [CONFIRMED / NOT CONFIRMED]
2. Each finding individually justified at its assigned severity level — group-level
   justification ("inertia implies all breaking") is not accepted
   — [CONFIRMED / NOT CONFIRMED]
3. Inertia framing alone was not used as uniform severity justification — if all one
   level, every element has an individual justification — [CONFIRMED / NOT CONFIRMED]

Set `gate4b_calibration_confirmed: true`. Update frontmatter.

**Stop. Do not write CONTRACT DELTA until gate4b_calibration_confirmed is true.**

---

## CONTRACT DELTA

Each entry is a spec amendment required to close the contract gap.

| Finding | Spec Clause | Amendment Summary | Priority |
|---------|-------------|-----------------|----------|

Priority annotation derived from Phase 4B calibrated severity:
`breaking → P1 | degraded → P2 | cosmetic → P3`

*(Each entry traceable to a named finding with calibrated severity from Phase 4B.)*
```

---

## V-02: Single Axis — Output Format

**Axis:** Output format — pre-populated spec skeleton

**Hypothesis:** Starting Phase 1 from a pre-committed spec skeleton — element names and
Spec Clause references derived from a spec index step, pre-populated before any Expected
Value is written — makes element omission structurally impossible rather than
instruction-verifiable. A blank Expected Value cell is a structural incompleteness signal,
not an omission that could slip past a completeness check. The skeleton commits coverage;
the fill step commits values.

**Predicted score:** 100 — all v5 criteria pass; introduces skeleton enforcement pattern as v6 candidate.

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
- **Connectors Contract Expert** — builds spec index, fills Phase 1 skeleton, validates
  element-type taxonomy in Phase 3, leads Phase 4B calibration
- **Automate** — leads Phase 2, Phase 4; co-owns Phase 3 diff construction

**Inertia framing:**
- Phase 1 = *committed contract* — what the spec promises must hold
- Phase 2 = *inertia output* — what the connector delivers by default
- Severity: `breaking | degraded | cosmetic`

---

## PHASE 1 — Write the Committed Contract (Pre-Populated Skeleton Pattern)

**Step 1: Build the spec index.**

Connectors Contract Expert: read the spec for {{topic}} now.
List every element the spec defines — every field, auth mechanism, payload envelope,
error shape, metadata property. One row per element. This is the spec index.

Do not derive from connector behavior. Spec text only.

| Field / Element | Spec Clause | Element Type |
|-----------------|-------------|--------------|

Element-type vocabulary:
`schema-field | auth-handshake | action-payload | trigger-payload | error-shape | metadata`

**Step 2: Fill the committed contract.**

Using the spec index rows above as the skeleton, add the Expected Value or Shape column.
Fill every row. Do not add new rows. Do not remove rows. The skeleton is the complete
coverage commitment — every row is required.

| Field / Element | Spec Clause | Element Type | Expected Value or Shape |
|-----------------|-------------|--------------|------------------------|

Rules:
- No Element Type cell blank — fill from the fixed vocabulary, row by row
- No Spec Clause cell blank — cite section or field
- No Expected Value cell blank — if the spec is ambiguous, note the ambiguity; do not
  silently skip
- Do not reference what you know the connector currently does — spec derivation only

### GATE 1 — Contract Isolation + Skeleton Completeness (4 items)

Write CONFIRMED or NOT CONFIRMED after the dash.

1. Skeleton completeness: every row from the spec index has a filled Expected Value —
   no blank Expected Value cells — [CONFIRMED / NOT CONFIRMED]
2. Inertia output was not referenced during Phase 1 — not just ordered after, but not
   consulted at all — [CONFIRMED / NOT CONFIRMED]
3. No Element Type cells blank in the committed contract table — [CONFIRMED / NOT CONFIRMED]
4. No Spec Clause cells blank in the committed contract table — [CONFIRMED / NOT CONFIRMED]
   *(Do not reference what you know the connector currently does — spec derivation only.)*

Set `gate1_isolation_confirmed: true` in frontmatter when all items pass.

**Stop. Automate does not activate until gate1_isolation_confirmed is true.**

---

## PHASE 2 — Capture the Inertia Output (Automate)

Run the connector. Record verbatim. Do not patch, summarize, or adjust toward the contract.

```
[inertia output — verbatim, unmodified]
```

### GATE 2

- [ ] Inertia output is complete and unmodified — [CONFIRMED / NOT CONFIRMED]

Set `gate2_actual_complete: true`. Update frontmatter.

**Stop. Do not write Phase 3 until gate2_actual_complete is true.**

---

## PHASE 3 — Classify Contract Gaps (Both Roles)

Both roles active. Compare Phase 1 skeleton against Phase 2 inertia output.

**Stop. Do not write root causes here. Root causes go in Phase 4. Not here.**

Carry element type and spec clause forward from Phase 1 skeleton. Blank cells in
Element Type, Severity, or Spec Clause are a gate failure condition.

| # | Field / Element | Element Type | Inertia Value or Shape | Severity | Spec Clause |
|---|-----------------|-------------|----------------------|----------|-------------|

Severity vocabulary: `breaking | degraded | cosmetic`

### GATE 3 — Gap Classification Completeness (4 items)

Write CONFIRMED or NOT CONFIRMED after the dash.

1. No Severity cells blank on any mismatch row — [CONFIRMED / NOT CONFIRMED]
2. No Spec Clause cells blank on any mismatch row — [CONFIRMED / NOT CONFIRMED]
3. No Element Type cells blank on any mismatch row — [CONFIRMED / NOT CONFIRMED]
4. No root cause hypotheses appear in Phase 3 — [CONFIRMED / NOT CONFIRMED]

Set `gate3_diff_complete: true`. Update frontmatter.

**Stop. Do not write Phase 4 until gate3_diff_complete is true.**

---

## PHASE 4 — Root Cause Analysis (Both Roles)

For each gap row from Phase 3, write a finding. Carry element type and severity forward.

---
**Finding F-[NN] — [Field / Element]**

- Element type: [from Phase 3 skeleton row]
- Severity: [from Phase 3 — carry forward]
- Spec clause: [from Phase 3 skeleton row]
- Observed gap: [specific deviation]
- Root cause hypothesis: [named connector-domain mechanism — schema version mismatch /
  auth handshake gap / action-payload field rename / trigger-payload envelope mismatch /
  error-shape deviation / metadata field omission; not "unknown" alone]
- Suggested resolution: [specific corrective action — name the spec amendment, schema
  field, API version, or auth flow step; not "investigate further" alone]

---

**Stop. Go to Phase 4B. Do not write CONTRACT DELTA.**

---

## PHASE 4B — Severity Calibration (Standalone — Do Not Merge with Phase 4)

Connectors Contract Expert leads. No new findings written here.
CONTRACT DELTA does not begin until GATE 4B passes.

### Severity Tally Table

| Severity | Count | Finding IDs |
|----------|-------|-------------|
| breaking | | |
| degraded | | |
| cosmetic | | |
| **Total** | | |

### Per-Element Justification

| Finding | Assigned Severity | Element-Level Justification |
|---------|------------------|-----------------------------|

*(Group-level justification is a gate failure condition.)*

### GATE 4B — Calibration Gate (3 items)

Write CONFIRMED or NOT CONFIRMED after the dash.

1. Severity tally complete — total matches Phase 4 finding count
   — [CONFIRMED / NOT CONFIRMED]
2. Each finding individually justified at its assigned severity level — group-level
   justification is not accepted — [CONFIRMED / NOT CONFIRMED]
3. Inertia framing alone was not used as uniform justification — [CONFIRMED / NOT CONFIRMED]

Set `gate4b_calibration_confirmed: true`. Update frontmatter.

**Stop. Do not write CONTRACT DELTA until gate4b_calibration_confirmed is true.**

---

## CONTRACT DELTA

| Finding | Spec Clause | Amendment Summary | Priority |
|---------|-------------|-----------------|----------|

*(Priority: `breaking → P1 | degraded → P2 | cosmetic → P3` from Phase 4B calibration.)*
```

---

## V-03: Single Axis — Role Sequence (Challenge-Before-Gate)

**Axis:** Role sequence — Automate challenges Expert's expected table before GATE 1 fires

**Hypothesis:** The existing isolation check in GATE 1 is self-attested by the Expert who
wrote the expected table. Adding a challenge step — where Automate reviews each row for
contamination signals before the gate fires — converts isolation from sole self-attestation
to a two-reader record. The challenge log names which rows were challenged, what the
contamination signal was, and whether revision was required. GATE 1 cannot fire until the
challenge log is complete. This strengthens C-12/C-14 beyond their current form: the
negative-constraint check is now backed by an external review record, not only a confirmable
checkbox.

**Predicted score:** 100 — all v5 criteria pass; introduces challenge-log pattern as v6 candidate.

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
- **Connectors Contract Expert** — constructs Phase 1 expected table; leads Phase 3
  domain validation; leads Phase 4B calibration
- **Automate** — runs Phase 1 challenge review; leads Phase 2; co-owns Phase 3 diff;
  leads Phase 4 root cause analysis

**Role sequence:** Expert constructs. Automate challenges. Gate fires. Automate then activates
for Phase 2. This order is not optional.

**Inertia framing:**
- Phase 1 = *committed contract* — spec-derived, inertia-independent
- Phase 2 = *inertia output* — default connector behavior
- Severity: `breaking | degraded | cosmetic`

---

## PHASE 1 — Write the Committed Contract (Connectors Contract Expert)

Expert writes the expected output table. Derive every value from the spec text.
Do not reference what you know the connector currently does.

Element-type vocabulary:
`schema-field | auth-handshake | action-payload | trigger-payload | error-shape | metadata`

| Field / Element | Element Type | Promised Value or Shape | Spec Clause |
|-----------------|-------------|------------------------|-------------|

When the table is complete: do not run GATE 1. Hand off to Automate for the challenge
review. Automate challenges first; GATE 1 fires only when the challenge log is complete.

---

## PHASE 1 CHALLENGE — Automate Reviews for Contamination

Automate: review the Expert's expected table row by row. For each row, assess:

- Is the Promised Value or Shape derivable from the Spec Clause cited?
- Does any value appear to be anchored to known connector behavior rather than spec text?
- Does any Spec Clause citation appear imprecise or missing?

For each row, record the challenge result:

| Field / Element | Challenge Result | Contamination Signal (if any) | Revision Required |
|-----------------|-----------------|------------------------------|-------------------|

Challenge results vocabulary:
- `clean` — value is traceable to spec clause; no contamination signal
- `flagged` — value appears anchored to connector knowledge or spec citation is imprecise
- `revised` — Expert revised the row after challenge; original value recorded below

For any row marked `flagged`: Expert revises the Expected Value before the gate fires.
Record the original and revised values:

| Field / Element | Original Value | Revised Value | Revision Reason |
|-----------------|----------------|---------------|-----------------|

When challenge log is complete and all flagged rows have been revised, proceed to GATE 1.

### GATE 1 — Contract Isolation + Challenge Complete (4 items)

Write CONFIRMED or NOT CONFIRMED after the dash.

1. Contract completeness: every spec-defined element has a row — nothing omitted
   — [CONFIRMED / NOT CONFIRMED]
2. Inertia output was not referenced during Phase 1 construction — not just ordered
   after, but not consulted at all; challenge log confirms no contamination signals
   carried into final table — [CONFIRMED / NOT CONFIRMED]
3. No Element Type cells blank in the committed contract table — [CONFIRMED / NOT CONFIRMED]
4. No Spec Clause cells blank in the committed contract table — [CONFIRMED / NOT CONFIRMED]
   *(Do not reference what you know the connector currently does — spec derivation only.)*

Set `gate1_isolation_confirmed: true` in frontmatter when all items pass.

**Stop. Automate does not activate for Phase 2 until gate1_isolation_confirmed is true.**

---

## PHASE 2 — Capture the Inertia Output (Automate)

Run the connector. Record verbatim. Do not patch toward the contract.

```
[inertia output — verbatim, unmodified]
```

### GATE 2

- [ ] Inertia output complete and unmodified — [CONFIRMED / NOT CONFIRMED]

Set `gate2_actual_complete: true`. Update frontmatter.

**Stop. Do not write Phase 3 until gate2_actual_complete is true.**

---

## PHASE 3 — Classify Contract Gaps (Both Roles)

Both roles active. Compare Phase 1 committed contract against Phase 2 inertia output.

**Stop. Do not write root causes here. Root causes go in Phase 4. Not here.**

Blank cells in Element Type, Severity, or Spec Clause are a gate failure condition.

| # | Field / Element | Element Type | Inertia Value or Shape | Severity | Spec Clause |
|---|-----------------|-------------|----------------------|----------|-------------|

Severity vocabulary: `breaking | degraded | cosmetic`

### GATE 3 — Gap Classification Completeness (4 items)

Write CONFIRMED or NOT CONFIRMED after the dash.

1. No Severity cells blank on any mismatch row — [CONFIRMED / NOT CONFIRMED]
2. No Spec Clause cells blank on any mismatch row — [CONFIRMED / NOT CONFIRMED]
3. No Element Type cells blank on any mismatch row — [CONFIRMED / NOT CONFIRMED]
4. No root cause hypotheses appear in Phase 3 — [CONFIRMED / NOT CONFIRMED]

Set `gate3_diff_complete: true`. Update frontmatter.

**Stop. Do not write Phase 4 until gate3_diff_complete is true.**

---

## PHASE 4 — Root Cause Analysis (Both Roles)

For each gap row from Phase 3, write a finding.

---
**Finding F-[NN] — [Field / Element]**

- Element type: [from Phase 3]
- Severity: [from Phase 3 — carry forward]
- Spec clause: [from Phase 3]
- Observed gap: [specific deviation]
- Root cause hypothesis: [named connector-domain mechanism — schema version mismatch /
  auth handshake gap / action-payload field rename / trigger-payload envelope mismatch /
  error-shape deviation / metadata field omission; not "unknown" alone]
- Suggested resolution: [specific corrective action — name the spec amendment, schema
  field, API version, or auth flow step; not "investigate further" alone]

---

**Stop. Go to Phase 4B. Do not write CONTRACT DELTA.**

---

## PHASE 4B — Severity Calibration (Standalone — Do Not Merge with Phase 4)

Connectors Contract Expert leads. CONTRACT DELTA does not begin until GATE 4B passes.

### Severity Tally Table

| Severity | Count | Finding IDs |
|----------|-------|-------------|
| breaking | | |
| degraded | | |
| cosmetic | | |
| **Total** | | |

### Per-Element Justification

| Finding | Assigned Severity | Element-Level Justification |
|---------|------------------|-----------------------------|

*(Group-level justification is a gate failure condition.)*

### GATE 4B — Calibration Gate (3 items)

Write CONFIRMED or NOT CONFIRMED after the dash.

1. Severity tally complete — total matches Phase 4 finding count
   — [CONFIRMED / NOT CONFIRMED]
2. Each finding individually justified at its assigned severity level — group-level
   justification ("inertia implies all breaking") is not accepted
   — [CONFIRMED / NOT CONFIRMED]
3. Inertia framing alone was not used as uniform justification — [CONFIRMED / NOT CONFIRMED]

Set `gate4b_calibration_confirmed: true`. Update frontmatter.

**Stop. Do not write CONTRACT DELTA until gate4b_calibration_confirmed is true.**

---

## CONTRACT DELTA

| Finding | Spec Clause | Amendment Summary | Priority |
|---------|-------------|-----------------|----------|

*(Priority: `breaking → P1 | degraded → P2 | cosmetic → P3` from Phase 4B calibration.)*
```

---

## V-04: Two-Axis Combination — V-01 + V-02

**Axes combined:** Lifecycle emphasis (Phase 0 scope) + Output format (pre-populated skeleton)

**Hypothesis:** Phase 0 scope enumeration provides the element list; that list becomes the
Phase 1 skeleton. The two mechanisms are load-bearing in sequence: Phase 0 commits what
must be covered; Phase 2 commits the values for what was committed in Phase 0. Completeness
is doubly enforced — a new element cannot appear in Phase 1 that was not in Phase 0, and
a Phase 0 element cannot be silently dropped when filling the skeleton. GATE 0 and GATE 1
together create a two-checkpoint completeness guarantee.

**Predicted score:** 100 — all v5 criteria pass; Phase 0 + skeleton combination surfaces
dual-enforcement completeness pattern as v6 candidate.

```
---
skill: trace-contract
topic: {{topic}}
date: {{date}}
gate0_scope_confirmed: pending
gate1_isolation_confirmed: pending
gate2_actual_complete: pending
gate3_diff_complete: pending
gate4b_calibration_confirmed: pending
---

# Trace: Contract vs. Actual — {{topic}}

**Roles:**
- **Connectors Contract Expert** — leads Phase 0, builds Phase 1 skeleton, leads Phase 3
  domain validation, leads Phase 4B calibration
- **Automate** — leads Phase 2, Phase 4; co-owns Phase 3

**Inertia framing:**
- Phase 1 = *committed contract*; Phase 2 = *inertia output*
- Severity: `breaking | degraded | cosmetic`

---

## PHASE 0 — Define the Contract Surface (Connectors Contract Expert)

Before any Expected Values are written, enumerate the connector elements this run covers.
Derive from spec text only. This list becomes the Phase 1 skeleton.

**In scope:**

| Element Name | Spec Clause | Element Type |
|--------------|-------------|--------------|

Element-type vocabulary:
`schema-field | auth-handshake | action-payload | trigger-payload | error-shape | metadata`

**Out of scope (explicit):**

| Element Name | Spec Clause | Exclusion Reason |
|--------------|-------------|-----------------|

### GATE 0 — Scope Completeness (4 items)

- [ ] In-scope list derived from spec — not from knowledge of connector behavior
- [ ] No Element Type cells blank in the in-scope table
- [ ] No Spec Clause cells blank in the in-scope table
- [ ] Out-of-scope exclusions are explicit — nothing silently dropped

Set `gate0_scope_confirmed: true`. Update frontmatter.

**Stop. Phase 1 does not begin until gate0_scope_confirmed is true.**

---

## PHASE 1 — Write the Committed Contract (Pre-Populated Skeleton from Phase 0)

**The Phase 0 in-scope list is the skeleton. Do not add rows. Do not remove rows.**

Using Phase 0 rows as the skeleton, fill Expected Value or Shape for each element.
Every row is required. Blank Expected Value cells are a structural incompleteness failure.

Do not reference what you know the connector currently does — spec derivation only.

| Field / Element | Spec Clause | Element Type | Expected Value or Shape |
|-----------------|-------------|--------------|------------------------|

*(Element Name, Spec Clause, and Element Type carry forward from Phase 0.
Only Expected Value or Shape is new in this phase.)*

### GATE 1 — Contract Isolation + Skeleton Completeness (4 items)

Write CONFIRMED or NOT CONFIRMED after the dash.

1. Skeleton completeness: every Phase 0 in-scope row has a filled Expected Value —
   no blank Expected Value cells — [CONFIRMED / NOT CONFIRMED]
2. Inertia output was not referenced during Phase 1 — not just ordered after, but not
   consulted at all — [CONFIRMED / NOT CONFIRMED]
3. No Element Type cells blank (carried from Phase 0; any new row must be filled)
   — [CONFIRMED / NOT CONFIRMED]
4. No Spec Clause cells blank (carried from Phase 0; any new row must be cited)
   — [CONFIRMED / NOT CONFIRMED]
   *(Do not reference what you know the connector currently does — spec derivation only.)*

Set `gate1_isolation_confirmed: true`. Update frontmatter.

**Stop. Automate does not activate until gate1_isolation_confirmed is true.**

---

## PHASE 2 — Capture the Inertia Output (Automate)

Run the connector. Record verbatim. Do not patch toward the contract.

```
[inertia output — verbatim, unmodified]
```

### GATE 2

- [ ] Inertia output complete and unmodified — [CONFIRMED / NOT CONFIRMED]

Set `gate2_actual_complete: true`. Update frontmatter.

**Stop. Do not write Phase 3 until gate2_actual_complete is true.**

---

## PHASE 3 — Classify Contract Gaps (Both Roles)

Compare Phase 1 skeleton against Phase 2 inertia output.

**Stop. Do not write root causes here. Root causes go in Phase 4. Not here.**

Blank cells in Element Type, Severity, or Spec Clause are a gate failure condition.

| # | Field / Element | Element Type | Inertia Value or Shape | Severity | Spec Clause |
|---|-----------------|-------------|----------------------|----------|-------------|

### GATE 3 — Gap Classification Completeness (4 items)

Write CONFIRMED or NOT CONFIRMED after the dash.

1. No Severity cells blank on any mismatch row — [CONFIRMED / NOT CONFIRMED]
2. No Spec Clause cells blank on any mismatch row — [CONFIRMED / NOT CONFIRMED]
3. No Element Type cells blank on any mismatch row — [CONFIRMED / NOT CONFIRMED]
4. No root cause hypotheses appear in Phase 3 — [CONFIRMED / NOT CONFIRMED]

Set `gate3_diff_complete: true`. Update frontmatter.

**Stop. Do not write Phase 4 until gate3_diff_complete is true.**

---

## PHASE 4 — Root Cause Analysis (Both Roles)

For each gap row from Phase 3:

---
**Finding F-[NN] — [Field / Element]**

- Element type: [from Phase 3]
- Severity: [from Phase 3]
- Spec clause: [from Phase 3]
- Observed gap: [specific deviation]
- Root cause hypothesis: [named connector-domain mechanism — schema version mismatch /
  auth handshake gap / action-payload field rename / trigger-payload envelope mismatch /
  error-shape deviation / metadata field omission; not "unknown" alone]
- Suggested resolution: [specific corrective action — name the spec amendment, schema
  field, API version, or auth flow step; not "investigate further" alone]

---

**Stop. Go to Phase 4B. Do not write CONTRACT DELTA.**

---

## PHASE 4B — Severity Calibration (Standalone — Do Not Merge with Phase 4)

Connectors Contract Expert leads. CONTRACT DELTA does not begin until GATE 4B passes.

### Severity Tally Table

| Severity | Count | Finding IDs |
|----------|-------|-------------|
| breaking | | |
| degraded | | |
| cosmetic | | |
| **Total** | | |

### Per-Element Justification

| Finding | Assigned Severity | Element-Level Justification |
|---------|------------------|-----------------------------|

*(Group-level justification is a gate failure condition.)*

### GATE 4B — Calibration Gate (3 items)

Write CONFIRMED or NOT CONFIRMED after the dash.

1. Tally complete — total matches Phase 4 finding count — [CONFIRMED / NOT CONFIRMED]
2. Each finding individually justified — group-level justification not accepted
   — [CONFIRMED / NOT CONFIRMED]
3. Inertia framing alone was not used as uniform justification — [CONFIRMED / NOT CONFIRMED]

Set `gate4b_calibration_confirmed: true`. Update frontmatter.

**Stop. Do not write CONTRACT DELTA until gate4b_calibration_confirmed is true.**

---

## CONTRACT DELTA

| Finding | Spec Clause | Amendment Summary | Priority |
|---------|-------------|-----------------|----------|

*(Priority: `breaking → P1 | degraded → P2 | cosmetic → P3` from Phase 4B.)*
```

---

## V-05: Full Synthesis — All Three R5 Axes + Interrogative Phrasing + Full v5 Baseline

**Axes combined:** Lifecycle emphasis (Phase 0) + Output format (pre-populated skeleton) +
Role sequence (challenge-before-gate) + Phrasing register (interrogative at contamination
checkpoints)

**Hypothesis:** The three R5 mechanisms are load-bearing in sequence and address
orthogonal failure modes:
- **Phase 0** prevents scope drift — coverage commitment before any value is written
- **Skeleton** prevents element omission — structural incompleteness, not omission
- **Challenge step** converts isolation from self-attestation to two-reader record
- **Interrogative phrasing** at key gates surfaces contamination reasoning explicitly
  ("What is the source of this value? Spec text, or memory?")

Layered on top of the full v5 baseline (C-21 through C-24 as defaults), this combination
should surface at least three v6 candidate patterns:
1. Phase 0 scope as checkable commitment upstream of Phase 1 completeness
2. Challenge log as verifiable isolation record (not purely self-attested)
3. Amendment type taxonomy in CONTRACT DELTA as a required structural column

**Predicted score:** 100 — all v5 criteria pass; expected to surface 3+ v6 candidates.

```
---
skill: trace-contract
topic: {{topic}}
date: {{date}}
gate0_scope_confirmed: pending
gate1_isolation_confirmed: pending
gate2_actual_complete: pending
gate3_diff_complete: pending
gate4b_calibration_confirmed: pending
---

# Trace: Contract vs. Actual — {{topic}}

**Roles:**
- **Connectors Contract Expert** — leads Phase 0, constructs Phase 1 expected table,
  revises flagged rows during Phase 1 challenge, leads Phase 3 domain validation,
  leads Phase 4B calibration
- **Automate** — runs Phase 1 challenge review; leads Phase 2; co-owns Phase 3 diff;
  leads Phase 4 root cause analysis

**Role sequence:** Expert defines scope (Phase 0) → Expert builds skeleton → Expert
fills contract → Automate challenges → GATE 1 fires → Automate captures inertia output.
This order is not optional.

**Inertia framing:**
- Phase 1 = *committed contract* — what the spec promises must hold
- Phase 2 = *inertia output* — what the connector delivers by default
- Severity = consequence of inertia for the promise:
  - `breaking` — inertia structurally violates the contract; promise cannot be met
  - `degraded` — inertia weakens the contract; promise partially met
  - `cosmetic` — inertia diverges in form but contract guarantee holds

---

## PHASE 0 — Define the Contract Surface (Connectors Contract Expert)

Before any Expected Values are written, define what this run covers.

*What does the spec cover for {{topic}}? List every element — fields, auth mechanisms,
payload envelopes, error shapes, metadata properties. Do not list what you expect the
connector to return. List what the spec defines.*

**In scope:**

| Element Name | Spec Clause | Element Type |
|--------------|-------------|--------------|

Element-type vocabulary:
`schema-field | auth-handshake | action-payload | trigger-payload | error-shape | metadata`

**Out of scope (explicit):**

| Element Name | Spec Clause | Exclusion Reason |
|--------------|-------------|-----------------|

### GATE 0 — Scope Completeness (4 items)

- [ ] In-scope list derived from spec text only — not from knowledge of what the connector
  currently implements or can reach
- [ ] No Element Type cells blank in the in-scope table
- [ ] No Spec Clause cells blank in the in-scope table
- [ ] Out-of-scope exclusions are explicit and named — nothing silently omitted

Set `gate0_scope_confirmed: true`. Update frontmatter.

**Stop. Phase 1 does not begin until gate0_scope_confirmed is true.**

---

## PHASE 1 — Write the Committed Contract (Expert Constructs from Phase 0 Skeleton)

**The Phase 0 in-scope list is the skeleton. Do not add rows. Do not remove rows.**

*For each row in the Phase 0 skeleton: what does the spec say this element's value or
shape must be? Write only that. Not what you know the connector currently returns.*

Fill Expected Value or Shape for every skeleton row. Blank cells are structural
incompleteness — record ambiguity explicitly rather than leaving blank.

Do not reference what you know the connector currently does — spec derivation only.

| Field / Element | Spec Clause | Element Type | Expected Value or Shape |
|-----------------|-------------|--------------|------------------------|

When the table is complete: stop. Do not run GATE 1. Hand off to Automate for the
challenge review. Automate challenges first; GATE 1 fires only when the challenge
log is complete.

---

## PHASE 1 CHALLENGE — Automate Reviews for Contamination

Automate: review every row of the Expert's committed contract table.

*For each row: Is this value derivable from the spec clause cited? Or does it appear to
be anchored to what you know the connector currently does? Ask: if someone had never
seen this connector run, would they derive this exact value from the spec text alone?*

Record the challenge result for each row:

| Field / Element | Challenge Result | Contamination Signal (if any) | Revision Required |
|-----------------|-----------------|------------------------------|-------------------|

Challenge results vocabulary:
- `clean` — value traceable to spec clause; no contamination signal detected
- `flagged` — value appears anchored to connector knowledge, or spec citation is
  imprecise; Expert must revise before GATE 1 fires
- `revised` — Expert revised after flagging; original and revised values recorded below

For any `flagged` row, Expert revises and records:

| Field / Element | Original Value | Revised Value | Revision Reason |
|-----------------|----------------|---------------|-----------------|

When challenge log is complete and all flagged rows revised: proceed to GATE 1.

### GATE 1 — Contract Isolation + Skeleton Completeness + Challenge Complete (4 items)

Write CONFIRMED or NOT CONFIRMED after the dash.

1. Skeleton completeness: every Phase 0 in-scope row has a filled Expected Value —
   no blank Expected Value cells — [CONFIRMED / NOT CONFIRMED]
2. Inertia output was not referenced during Phase 1 — not just ordered after, but not
   consulted at all; challenge log records no contamination signals carried into the
   final table — [CONFIRMED / NOT CONFIRMED]
   *(Do not reference what you know the connector currently does — spec derivation only.)*
3. No Element Type cells blank in the final committed contract table
   — [CONFIRMED / NOT CONFIRMED]
4. No Spec Clause cells blank in the final committed contract table
   — [CONFIRMED / NOT CONFIRMED]

Set `gate1_isolation_confirmed: true`. Update frontmatter.

**Stop. Automate does not activate for Phase 2 until gate1_isolation_confirmed is true.**

---

## PHASE 2 — Capture the Inertia Output (Automate)

Run the connector. Record verbatim. Do not patch, summarize, or adjust toward the contract.

*What does the connector return, exactly? Do not edit. Do not truncate. Do not move
values closer to what the spec says. Record the inertia output as-is.*

```
[inertia output — verbatim, unmodified]
```

### GATE 2

- [ ] Inertia output is complete and unmodified — no truncation, no adjustment —
  [CONFIRMED / NOT CONFIRMED]

Set `gate2_actual_complete: true`. Update frontmatter.

**Stop. Do not write Phase 3 until gate2_actual_complete is true.**

---

## PHASE 3 — Classify Contract Gaps (Both Roles)

Both roles active. Compare Phase 1 committed contract against Phase 2 inertia output.

**Stop. Do not write root causes here. Root causes go in Phase 4. Not here.
Classify the gap. Name the severity. Do not explain why. That is Phase 4.**

Carry element type and spec clause forward from Phase 1. Add rows only for elements
where the inertia output diverges from the committed contract.

Blank cells in Element Type, Severity, or Spec Clause are a gate failure condition.

| # | Field / Element | Element Type | Inertia Value or Shape | Severity | Spec Clause |
|---|-----------------|-------------|----------------------|----------|-------------|

Severity vocabulary (inertia framing):
- `breaking` — inertia structurally violates the contract; promise cannot be met
- `degraded` — inertia weakens the contract; promise partially met
- `cosmetic` — inertia diverges in form but contract guarantee holds

Element-type vocabulary:
`schema-field | auth-handshake | action-payload | trigger-payload | error-shape | metadata`

### GATE 3 — Gap Classification Completeness (4 items)

Write CONFIRMED or NOT CONFIRMED after the dash.

1. No Severity cells blank on any mismatch row — [CONFIRMED / NOT CONFIRMED]
2. No Spec Clause cells blank on any mismatch row — [CONFIRMED / NOT CONFIRMED]
3. No Element Type cells blank on any mismatch row — [CONFIRMED / NOT CONFIRMED]
4. No root cause hypotheses appear anywhere in Phase 3 — [CONFIRMED / NOT CONFIRMED]

Set `gate3_diff_complete: true`. Update frontmatter.

**Stop. Do not write Phase 4 until gate3_diff_complete is true.**

---

## PHASE 4 — Root Cause Analysis (Both Roles)

For each gap row from Phase 3, explain why inertia misses the promise. Carry element
type and severity forward — do not reclassify until Phase 4B.

*For each gap: which connector-domain mechanism is responsible? Name it specifically.
Not "unknown" — name the candidate mechanism even if not yet confirmed.*

---
**Finding F-[NN] — [Field / Element]**

- Element type: [from Phase 3 — carry forward]
- Severity: [from Phase 3 — carry forward]
- Spec clause: [from Phase 3]
- Observed gap: [specific deviation — not generic; name the field, the value, the shape]
- Root cause hypothesis: [named connector-domain mechanism — schema version mismatch /
  auth handshake gap / action-payload field rename / trigger-payload envelope mismatch /
  error-shape deviation / metadata field omission; not "unknown" alone]
- Suggested resolution: [specific corrective action — name the spec amendment, schema
  field, API version, or auth flow step; not "investigate further" alone]

---

**Stop. All findings written. Go to Phase 4B. Do not write CONTRACT DELTA.**

---

## PHASE 4B — Severity Calibration (Standalone — Do Not Merge with Phase 4)

**Connectors Contract Expert leads. This phase runs alone.**
**No new findings are written here. CONTRACT DELTA does not begin until GATE 4B passes.**

*How many findings at each level? Count before writing any assessment.*

### Severity Tally Table

| Severity | Count | Finding IDs |
|----------|-------|-------------|
| breaking | | |
| degraded | | |
| cosmetic | | |
| **Total** | | |

### Per-Element Justification

*For each finding: why is this finding at this severity level specifically? Not as a
group — individually. What about this element's gap makes it breaking, degraded, or
cosmetic?*

| Finding | Assigned Severity | Element-Level Justification |
|---------|------------------|-----------------------------|

*(Group-level justification — "all breaking because inertia implies full replacement" —
is a gate failure condition. Inertia framing is not automatic justification for uniform
severity.)*

### Calibration Assessment

Review the tally. Is the distribution coherent? Does it reflect the actual severity of
each element's gap — not the framing, not the expectation, but the gap itself?

If all findings are at one severity level: explicitly justify each element at that level.
A group statement does not pass. State what about each element individually meets the
threshold.

### GATE 4B — Calibration Gate (3 items)

Write CONFIRMED or NOT CONFIRMED after the dash.

1. Severity tally complete — total matches Phase 4 finding count
   — [CONFIRMED / NOT CONFIRMED]
2. Each finding individually justified at its assigned severity level — group-level
   justification ("inertia implies all breaking") is not accepted; if all one level,
   every finding has an element-level justification — [CONFIRMED / NOT CONFIRMED]
3. Inertia framing alone was not used as uniform justification — per-element reasoning
   is present for every finding — [CONFIRMED / NOT CONFIRMED]

Set `gate4b_calibration_confirmed: true`. Update frontmatter.

**Stop. Do not write CONTRACT DELTA until gate4b_calibration_confirmed is true.**

---

## CONTRACT DELTA

Each entry is a spec amendment required to close the contract-to-inertia gap.
Priority is derived from Phase 4B calibrated severity. Amendment type classifies
the kind of spec change required.

| Finding | Spec Clause | Amendment Summary | Amendment Type | Priority |
|---------|-------------|-----------------|----------------|----------|

**Amendment type vocabulary:** `add-field | remove-field | change-type | change-enum |
change-error-shape | change-auth-flow | add-constraint | remove-constraint`

**Priority mapping:** `breaking → P1 | degraded → P2 | cosmetic → P3`
*(Priority reflects calibrated severity from Phase 4B. Each entry traceable to a named
finding with an individually justified severity level.)*
```

---

## Within-Variation Structural Distinctions

| Signal | V-01 | V-02 | V-03 | V-04 | V-05 |
|--------|------|------|------|------|------|
| Phase 0 scope enumeration | **YES** | no | no | **YES** | **YES** |
| Pre-populated skeleton | no | **YES** | no | **YES** | **YES** |
| Challenge-before-gate step | no | no | **YES** | no | **YES** |
| Challenge revision log | no | no | **YES** | no | **YES** |
| Interrogative phrasing at gates | no | no | no | no | **YES** |
| Amendment type column in CONTRACT DELTA | no | no | no | no | **YES** |
| Frontmatter gate key count | 5 | 4 | 4 | 5 | 5 |
| GATE 0 present | **YES** | no | no | **YES** | **YES** |

---

## v6 Candidate Patterns

**Pattern 1 — Phase 0 scope as checkable commitment (V-01/V-04/V-05)**

Phase 0 defines the contract surface before any Expected Values are written. Phase 1
completeness is then verifiable against a named prior commitment (the Phase 0 in-scope
list), not assessed by inspection. GATE 0 fires before Phase 1. This is strictly stronger
than GATE 1 item 1 ("every spec-defined element has a row"), because the in-scope list
exists as a distinct artifact that Phase 1 must match, not an assertion the same author
makes about their own work. Candidate criterion: Phase 0 scope commitment makes Phase 1
completeness checkable against a prior named list.

**Pattern 2 — Pre-populated skeleton makes element omission structural (V-02/V-04/V-05)**

Phase 1 begins with a pre-committed element list (from spec index or Phase 0). Blank
Expected Value cells are structural incompleteness, not omissions that pass a completeness
declaration. No variation before R5 pre-committed the element set before deriving values.
Candidate criterion: Phase 1 uses a pre-populated skeleton, making completeness a structural
property rather than an instruction-compliance property.

**Pattern 3 — Challenge log converts isolation to two-reader record (V-03/V-05)**

The existing isolation check (C-12/C-14) is self-attested. A challenge step — where a
second role reviews each row for contamination signals before the gate fires — produces
a challenge log that records which rows were flagged, whether revision was required, and
what the contamination signal was. The GATE 1 isolation confirmation is then backed by an
external review record, not only a checkbox. Candidate criterion: Phase 1 isolation
includes a challenge log from a second role, making isolation verifiable by output, not
solely by self-attestation.

**Pattern 4 — Amendment type taxonomy as required structural column (V-05)**

The CONTRACT DELTA in V-05 adds an Amendment Type column with a fixed vocabulary
(`add-field | remove-field | change-type | change-enum | change-error-shape |
change-auth-flow | add-constraint | remove-constraint`). Prior rounds only classify
by priority (from Phase 4B severity). Amendment type classifies what kind of spec
change is needed — orthogonal to urgency. This creates a second taxonomy on the delta
that enables amendment batching (all add-field amendments across multiple findings can
be grouped for a single schema update). Candidate criterion: CONTRACT DELTA includes an
amendment type column from a fixed vocabulary, enabling amendment batching independent
of priority.
