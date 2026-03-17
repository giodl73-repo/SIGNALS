# flow-throttle Variate — Round 12

**Date:** 2026-03-16
**Rubric:** v12 (C-01 through C-34, N_essential=5, N_recommended=3, N_aspirational=26)
**Max composite:** 220 | **Baseline ceiling:** R11 V-04/V-05 (confirmed passes C-01 through C-32 under v11)

---

## State Analysis: What R11 V-05 Has vs. What R12 Must Add

**R11 V-05 coverage under v12 (assessed):**
- C-01 through C-32: all pass (verified through R11)

**C-33 gap in R11 V-04/V-05:**
Both R11 variations carry the three-field inertia annotation with fields "Failure mode
prevented," "Gap above C-25," and "Concrete example" — satisfying C-29 and C-30. C-33
requires that when C-29+C-30 co-satisfy a three-field annotation, a header line must
declare the field count and field names so completeness is verifiable by count-scan.
R11 V-04 and V-05 both head the annotation as "Inertia annotation for C-27 — why the
register must be declared closed (C-29, C-30):" — this names the criteria but does not
declare the field count or enumerate field names in the header. An auditor checking C-33
must read the annotation body and count fields by criterion-matching (locating the
C-29-satisfying "Failure mode prevented" label, then the C-30-satisfying "Concrete
example" label) rather than verifying a declared count against a named list. C-33 fails.

**C-34 gap in R11 V-04/V-05:**
Both variations carry the TYPE SCAN GATE audit test with named observables per path.
The gate-present path says "confirm five named observables in sequence" — a count
embedded in description prose. C-34 requires each path to declare its observable count
at the path identifier level, not inside the description: the pattern is "Gate present —
5 observables:" on the italic path-name line, analogous to how the C-27 closed-register
pattern places the field count on the register header rather than inside a cell. R11
V-04/V-05 embed the count in the prose instruction ("confirm five named observables");
an auditor must read the description to find the number. C-34 fails because the count is
not at the path-label level where a count-scan can confirm it without entering the prose.

**Summary:**

| Criterion | R11 V-05 status under v12 | Gap |
|-----------|--------------------------|-----|
| C-33 | FAIL | Annotation header names criteria but not field count or field names |
| C-34 | FAIL | Observable count embedded in description prose, not at path-label level |

**R11 V-05 under v12 composite:** 210/220 (missing C-33 + C-34 = 2 × 5 pts)

---

## Round 12 Variation Map

| Variation | Axes | C-33 | C-34 | Predicted composite |
|-----------|------|------|------|---------------------|
| V-01 | Inertia framing: C-33 FAIL isolation (R11 V-04 baseline carry, no count header) | FAIL | FAIL | 210/220 |
| V-02 | Inertia framing: C-33 PASS (field-count header on annotation, no observable count) | PASS | FAIL | 215/220 |
| V-03 | Lifecycle emphasis: C-34 PASS (observable count at path-label level, no count header) | FAIL | PASS | 215/220 |
| V-04 | Combined axes: C-33 + C-34 both applied, single-role form | PASS | PASS | 220/220 |
| V-05 | Role sequence + all axes: three-role pipeline with C-33 + C-34 | PASS | PASS | 220/220 |

**Single-axis questions:**

Q1 (V-01 vs V-02): Does adding a field-count header to the three-field annotation satisfy
C-33? Hypothesis: yes — C-33 requires a header line declaring both count and field names.
The form "3 fields: Failure mode prevented | Gap above C-25 | Concrete example" places
the count (3) and the three field names on the header line; an auditor counts three
pipe-delimited names against the declared number without entering the annotation body.
V-02 tests whether this header form alone satisfies C-33 while C-34 remains open.

Q2 (V-01 vs V-03): Does elevating the observable count from embedded prose to the
path-label level satisfy C-34 independently of the C-33 change? Hypothesis: yes — C-34
requires the count to appear on the path identifier ("Gate present — 5 observables:") so
it is verifiable by count-scan without reading the description. Changing
"*Gate-present audit method:*" to "*Gate-present audit method — 5 observables:*" and
"*Gate-absent signature:*" to "*Gate-absent signature — 1 observable:*" converts the
observable sets from open enumerations to labeled closed sets. V-03 tests this change in
isolation; Section B annotation carries the R11 V-04 prose header unchanged.

Q3 (V-04 vs V-05): Does the three-role pipeline provide structural enforcement for C-33
and C-34 beyond what single-role instructions produce? Hypothesis: yes — in V-04, the
field-count header and observable count declarations are inline instructions encountered
at execution time; an executor may skip them. In V-05, the Format Analyst must produce
the field-count header as a role deliverable (the contract is closed before Role 2 opens),
and the Consequence Analyst's count-declared observable paths appear at the TYPE SCAN GATE
role boundary as a structural precondition. The count declarations are enforced by role
architecture, not by inline instruction proximity.

---

## V-01 — Single Axis: Inertia Framing (C-33 FAIL — no count header, R11 V-04 baseline)

**Axis:** Section B inertia annotation carries the R11 V-04 three-field labeled form
(Failure mode prevented / Gap above C-25 / Concrete example) with the original header
that names the criteria (C-29, C-30) but does not declare the field count or enumerate
field names. The TYPE SCAN GATE audit paths carry the R11 V-04 artifact-identifier form
with "confirm five named observables in sequence" embedded in description prose — no
per-path count label.

**Hypothesis:** V-01 is the clean baseline isolation for R12. C-29 and C-30 pass (the
three-field labeled annotation is present and the concrete example names a specific
unregistered element type with its classification ambiguity). C-31 passes (five named
observables with artifact-ID and structural-position anchors). C-32 passes. C-33 fails
because the header line identifies the criteria but not the field count or field names —
an auditor cannot perform a count-scan against the annotation; completeness requires
reading the body and matching fields to criterion definitions. C-34 fails because the
count (five) is inside the prose instruction rather than on the path-label line.

**v12 predicted scoring:** C-33 FAIL. C-34 FAIL. Composite: 210/220.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput
across the rate-limited system described in the signal. Treat the stated request volume
as 1x nominal; also analyze at 2x and 5x.

Tables are the primary output. Fill every cell. Produce sections in the order shown.

---

**OUTPUT FORMAT CONTRACT**

**Section A — PROSE-PERMITTED CONTEXTS (C-20)**

Prose is permitted in exactly three contexts. Each context declared with scope and
authorizing criterion:

1. **Binding-tier causal reason** — one paragraph at Phase 1B exit. Scope: explains
   why the Binding? = Y tier fails before all others under 1x nominal load. Authorized
   by C-01.
2. **Binding constraint exclusivity statement** — one sentence at Phase 1B exit. Scope:
   names the mechanism preventing at least one non-binding tier from binding first.
   Authorized by C-14.
3. **Global criterion-coverage verdict notes** — FAIL verdicts only, at the global
   coverage step. Scope: one sentence per failed criterion. Authorized by C-19.

Any prose passage outside these three declared scopes is a format violation detectable
without content review.

**Section B — STRUCTURED OUTPUT REGISTER (C-25, C-27)**

The following element types are structured output. They are NOT prose. They are exempt
from C-23 inline citation requirements. Classification is by element type — content
inspection is not required and is not the correct classification method.

| Element type | Canonical form | Prose? | C-23 tag required? |
|-------------|---------------|--------|-------------------|
| Gate decision lines | PROCEED / BLOCKED | No | No |
| Cross-artifact header lines | "One row per [source]. No [item] may be omitted." | No | No |
| Phase boundary prohibition lines | "PROHIBITED: [data class] — [failure mode]" | No | No |
| Per-criterion verdict lines | "C-NN: PASS / FAIL" | No | No |

No other element types are added to this register without revising this contract.

**Inertia annotation for C-27 — why the register must be declared closed (C-29, C-30):**

- **Failure mode prevented:** Implicit-complement classification — an executor reasoning
  that the complement of Section A's prose-permitted list is implicitly structured output.
  Under an open register, an executor encountering an unlisted element type has no
  classification decision to make by lookup: "it is not prose-permitted (Section A does
  not authorize it), therefore it is structured output, therefore exempt from C-23." The
  executor classifies by content-based inference rather than by register membership. This
  is the content-inspection problem C-25 was designed to eliminate: element types are
  classified by interpreting their content rather than by identifying their registered type.
- **Gap above C-25:** C-25 requires the register to enumerate element types with explicit
  Prose? and C-23-tag classifications. C-25 compliance does not require the register to
  declare itself exhaustive. An open register that satisfies C-25 leaves every unlisted
  element type in implicit-complement territory: the four-row enumeration is correct for
  the listed types, but a fifth element type is classifiable by inference alone. The
  closure declaration converts implicit-exempt to explicitly-unclassified: the registered
  set is declared exhaustive, and any unlisted element type's classification status is
  a detectable contract gap, not an inferred permission. Adding a new type requires an
  explicit revision to this contract, auditable by change history.
- **Concrete example (C-30):** A load-shape verdict label — e.g., a line reading
  "FLAT-LOAD: within nominal band" — does not match any of the four registered canonical
  forms. Gate decision line (PROCEED / BLOCKED — no match). Cross-artifact header
  ("One row per [source]..." — no match). Phase boundary prohibition ("PROHIBITED:
  [data] — [failure mode]" — no match). Per-criterion verdict ("C-NN: PASS / FAIL" —
  no match). Under an open register, the implicit-complement inference resolves the
  ambiguity: not in Section A, therefore implicitly structured output. Under a closed
  register, the inference is foreclosed: this element type is unregistered, its Prose?
  and C-23-tag classifications are explicitly unresolved, and adding it requires a named
  contract revision. The ambiguity created by the unregistered type is independently
  testable: present the label to an executor — if the register is open, the executor
  will classify it as exempt; if the register is closed, the executor will flag it as
  unresolved.

---

**PHASE 1 — EVIDENCE PHASE**

**Step 1A — SOURCE REGISTER (C-13)**

Commit the evidence base before naming any tier. Every numeric threshold cited in Steps
1B and Phase 2 must have a Source-ID entry here. A tier with no register entry receives
UNDOCUMENTED in the Limit column; it is not assigned an inferred value.

| Source-ID | Source name | Type | Numeric values it provides |
|-----------|-------------|------|---------------------------|
| S-01 | | | |
| S-02 | | | |

PROHIBITED: adding a new Source-ID after this line. — *prevents retroactive source
injection; a source entered after claims are built cannot be verified as the basis for
the numeric claim it purports to support — it may be post-hoc attribution assembled to
satisfy C-11 rather than a pre-committed evidence source*

**Step 1B — TIER INVENTORY**

**TABLE A — THROTTLE TIER INVENTORY ACROSS VOLUME BANDS**

*(One row per rate-limiting component. Source-ID from register required. Every cell
filled — a blank cell and "not applicable" are identical under scan.)*

| Tier-ID | Component | Limit (number + unit) | Source-ID | Scope | STATUS 1x | STATUS 2x | STATUS 5x | Binding? | Failure mode |
|---------|-----------|----------------------|-----------|-------|-----------|-----------|-----------|----------|-------------|
| T-01 | | | | | | | | | |
| T-02 | | | | | | | | | |
| ... | | | | | | | | | |

Column notes:
- `Tier-ID` — T-01, T-02, ... Use verbatim in every downstream table. Compliance
  failure condition: an informal synonym in place of T-NN fails the tier-ID threading
  requirement and makes cross-section tracing a name-resolution task.
- `Limit` — a specific number with a unit (e.g., "1,200 req/min", "500 connections").
  Compliance failure condition: a vague label ("limited", "throttled") fails precision.
- `STATUS Nx` — OK / HIT / SAT. Must shift between at least two bands. A tier that
  never transitions cannot be the primary bottleneck at any band.
- `Binding?` — exactly one Y. Compliance failure condition: multiple Y entries fail the
  at-most-one binding constraint; a designation without causal reason is an assertion,
  not an argument.
- `Failure mode` — hard rejection / queue saturation / silent drop / degraded throughput /
  timeout. At least two distinct values across rows.

PROHIBITED: introducing a new T-NN in any Phase 2 section. — *prevents scope creep;
tier discovery during claims analysis indicates Phase 1 enumeration was incomplete —
return to Step 1B, complete the registry, restart Phase 2 from the point of discovery*

**[prose: item 1 — binding-tier causal reason]** State why the Binding? = Y tier fails
before all others under 1x nominal load. Name the specific causal mechanism.

**[prose: item 2 — binding constraint exclusivity]** For at least one Binding? = N tier,
name the mechanism that prevents it from binding before the primary tier.

---

**PHASE 2 — CLAIMS PHASE**

PROHIBITED: opening Phase 2 before Phase 1B is complete. — *prevents late evidence
injection; claims built on an incomplete tier inventory produce unverifiable findings*

**For each tier in TABLE A (C-17):** every downstream derived table must include a row
for every T-NN. Coverage verifiable by T-NN count match against TABLE A, not by reading
downstream content. — *prevents coverage elision; a tier absent from a derived table
produces a detectable T-NN count gap*

**TABLE B — BACKPRESSURE PROPAGATION TRACE**

*(Source: TABLE A. Two hops minimum. T-NNs must reference TABLE A entries.)*

| Hop | From (Tier-ID) | To component | Mechanism | Observable effect |
|-----|----------------|--------------|-----------|-------------------|
| 1 | | | | |
| 2 | | | | |
| ... | | | | |

Mechanism values: queue-fill, connection-hold, retry-amplification, dependency-stall,
timeout-cascade. Compliance failure condition: a generic term ("blocked", "throttled")
in place of a named mechanism from the permitted set fails precision.

**TABLE C — USER EXPERIENCE CATALOG**

*(Source: TABLE A. One row per TABLE A Tier-ID. No tier may be omitted.)*

| Tier-ID | Error code or signal | Retry-After present? (Y/N) | Retry-After surfaced to caller? (Y/N) | Visible in run history? (Y/N/SILENT) | Failure if Retry-After ignored |
|---------|---------------------|---------------------------|--------------------------------------|--------------------------------------|-------------------------------|
| T-01 | | | | | |
| T-02 | | | | | |

Compliance failure condition: plain description ("request fails", "throttle error") in
`Error code or signal` in place of a specific HTTP status code or platform signal
identifier fails precision.

**TABLE D — UNPROTECTED BURST PATHS**

*(Source: TABLE A. At least one row. If no unprotected path exists, row 1 names ≥2
controls as evidence that every entry point is protected.)*

| Path-ID | Entry component | Tier-IDs involved | Gap reason or named controls | Consequence at burst volume |
|---------|----------------|-------------------|-----------------------------|-----------------------------|
| P-01 | | | | |

**TABLE E — RISK TAXONOMY**

*(Source: TABLE A + TABLE B + TABLE D. Per-type minimum: ≥1 Burst, ≥1 Cascade,
≥1 RetryAfter. Type column required — a count requirement without type classification
can be satisfied by two rows of the same failure category, leaving an entire category
undetected without a type scan.)*

| Risk-ID | Tier-ID | Type | Risk description | Severity (H/M/L) |
|---------|---------|------|-----------------|-----------------|
| R-01 | | Burst | | |
| R-02 | | Cascade | | |
| R-03 | | RetryAfter | | |

Compliance failure condition: a risk list without a Type column with named taxonomy and
per-type minimum-row constraint fails C-22 even if all required categories happen to
appear, because the mechanism that makes category absence detectable is absent.

---

**TYPE SCAN GATE**

**Purpose annotation (C-26) — three fields:**

- **Failure mode prevented:** Category elision — a risk type (Burst, Cascade, or
  RetryAfter) is absent from TABLE E but detectable only by full table scan after TABLE F
  is complete. At that point, TABLE F also has no mitigations for the missing category —
  two artifacts are incomplete and both require revision.
- **Gap above C-22:** C-22 ensures the Type column is present and all three categories
  appear in the *finished* TABLE E. This gate ensures type completeness is verified
  *before TABLE F opens*. C-22 defines what the finished output must contain; this gate
  makes an incomplete TABLE E a construction-time blocking condition. An executor who
  reasons "C-22 already requires all three types — this gate adds process without
  substance" conflates the structural requirement with the enforcement mechanism. C-22
  ensures the structure; the gate ensures the missing-category failure mode cannot be
  produced by any valid execution path.
- **Audit test (C-28, C-31):**
  - *Gate-present audit method:* Locate the section titled **TYPE SCAN GATE** — artifact
    identifier: the exact section header string. Structural position: it appears between
    TABLE E's last row (the row carrying the highest-numbered R-NN value in the Risk-ID
    column) and the TABLE F section header. Within the TYPE SCAN GATE section, confirm
    five named observables in sequence:
    (1) A verdict line of the form `Burst: [Y / N]` — present before the gate decision line.
    (2) A verdict line of the form `Cascade: [Y / N]` — present before the gate decision line.
    (3) A verdict line of the form `RetryAfter: [Y / N]` — present before the gate decision line.
    (4) A gate decision line reading `PROCEED` or `BLOCKED` — appears after all three
    per-category verdict lines and before the TABLE F section header.
    (5) TABLE F section header and first data row (MR-01) appear after the gate decision
    line; MR-01 is not the first row after TABLE E's last R-NN.
    All five observables confirmed = gate compliance verified by artifact-ID scan.
  - *Gate-absent signature:* The structural position between TABLE E's last R-NN row and
    TABLE F's first data row (MR-01) contains no **TYPE SCAN GATE** section header.
    Named observable for the absent condition: no verdict lines of the form
    `[Category]: [Y / N]` (where Category is one of Burst, Cascade, RetryAfter) appear
    in the structural gap between R-NN and MR-01. Gate-present outputs have three named
    Y/N verdict lines before MR-01; gate-absent outputs have none.

**Escape route for C-26 — "the gate Purpose annotation is redundant because C-22 already
explains why type coverage matters" (C-32):** This reasoning conflates the *purpose of
the type taxonomy* (which C-22 explains) with the *purpose of the gate* (which is to make
type completeness a construction-time blocking condition). C-22's requirement is present
in the TABLE E header; the gate annotation explains why a named structural check is
necessary given that C-22 is already present. Without the annotation, an executor can
reason "the table already requires all three types — the gate is extra process" and skip
it. The annotation makes that reasoning auditable: the gap the gate closes (post-hoc vs.
construction-time detection) is explicitly stated and cannot be dismissed as redundant
without contradicting the stated purpose.

Scan TABLE E for type completeness:
- Burst: [at least one row present? Y / N]
- Cascade: [at least one row present? Y / N]
- RetryAfter: [at least one row present? Y / N]

If all Y: PROCEED
If any N: BLOCKED — return to TABLE E, add the missing type row, re-run this gate.

---

**TABLE F — MITIGATION REGISTRY**

*(Source: TABLE E. One row per TABLE E risk. No risk may be omitted.)*

| MR-ID | Source (Risk-ID) | Gap type | Component | Setting or API parameter | Change | Expected outcome | Tradeoff |
|-------|-----------------|----------|-----------|--------------------------|--------|-----------------|---------|
| MR-01 | | | | | | | |
| MR-02 | | | | | | | |

Compliance failure condition: a category of action ("add retry logic") in `Setting or
API parameter` in place of a specific parameter identifier (e.g., `connector.retryPolicy`)
fails precision. A row naming a category cannot be applied without further research; a
row naming an exact parameter can be applied immediately.

PROHIBITED: adding rows to TABLE E after TABLE F has opened. — *prevents retroactive
risk injection; a risk discovered during mitigation planning requires returning to
TABLE E, completing it, re-running the TYPE SCAN GATE, then re-opening TABLE F*

---

**GLOBAL CRITERION-COVERAGE STEP**

Named dedicated step. Not embedded prose. Maps output content to essential criterion
categories by name. Reports per-criterion PASS/FAIL verdict.

- C-01 (Primary bottleneck with causal reason): [binding-tier causal reason present and
  names the specific causal mechanism? PASS / FAIL]
- C-02 (Backpressure propagation ≥2 hops with mechanism): [TABLE B has ≥2 rows with
  T-NN identifiers from TABLE A and specific mechanisms from the permitted set? PASS / FAIL]
- C-03 (≥2 tiers with enforcing component and scope): [TABLE A has ≥2 rows with Component
  and Scope filled, each with a specific numeric Limit? PASS / FAIL]
- C-04 (UX at each throttle tier): [TABLE C has one row per TABLE A Tier-ID and no tier
  is omitted? PASS / FAIL]
- C-05 (Unprotected burst path): [TABLE D has ≥1 row with gap reason, or ≥1 row with
  ≥2 named controls as evidence of full protection? PASS / FAIL]

[prose: item 3 — global criterion-coverage verdict notes] State FAIL rationale for any
criterion above that did not pass.

---

---

## V-02 — Single Axis: Inertia Framing (C-33 PASS — field-count header on annotation)

**Axis:** Section B inertia annotation header is restructured to declare the field count
and enumerate field names: "3 fields: Failure mode prevented | Gap above C-25 | Concrete
example (C-29, C-30)". The three fields carry unchanged from V-01. The TYPE SCAN GATE
audit paths carry the V-01 form with the observable count embedded in prose ("confirm
five named observables in sequence") — C-34 remains open.

**Hypothesis:** The field-count header satisfies C-33. C-33 requires a header line
declaring count and field names; the pipe-delimited form "3 fields: Failure mode prevented
| Gap above C-25 | Concrete example" provides the count (3) and all three field names in
one scannable line. An auditor counts three names against the declared "3" without reading
the annotation body. C-34 fails because the observable count is still in the description
prose. The compliance delta between V-01 and V-02 is exactly one structural transformation:
the annotation header gains a count declaration.

**v12 predicted scoring:** C-33 PASS (field-count header present: "3 fields: Failure mode
prevented | Gap above C-25 | Concrete example"). C-34 FAIL (observable count in prose).
Composite: 215/220.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput
across the rate-limited system described in the signal. Treat the stated request volume
as 1x nominal; also analyze at 2x and 5x.

Tables are the primary output. Fill every cell. Produce sections in the order shown.

---

**OUTPUT FORMAT CONTRACT**

**Section A — PROSE-PERMITTED CONTEXTS (C-20)**

Prose is permitted in exactly three contexts. Each context declared with scope and
authorizing criterion:

1. **Binding-tier causal reason** — one paragraph at Phase 1B exit. Scope: explains
   why the Binding? = Y tier fails before all others under 1x nominal load. Authorized
   by C-01.
2. **Binding constraint exclusivity statement** — one sentence at Phase 1B exit. Scope:
   names the mechanism preventing at least one non-binding tier from binding first.
   Authorized by C-14.
3. **Global criterion-coverage verdict notes** — FAIL verdicts only, at the global
   coverage step. Scope: one sentence per failed criterion. Authorized by C-19.

Any prose passage outside these three declared scopes is a format violation detectable
without content review.

**Section B — STRUCTURED OUTPUT REGISTER (C-25, C-27)**

The following element types are structured output. They are NOT prose. They are exempt
from C-23 inline citation requirements. Classification is by element type — content
inspection is not required and is not the correct classification method.

| Element type | Canonical form | Prose? | C-23 tag required? |
|-------------|---------------|--------|-------------------|
| Gate decision lines | PROCEED / BLOCKED | No | No |
| Cross-artifact header lines | "One row per [source]. No [item] may be omitted." | No | No |
| Phase boundary prohibition lines | "PROHIBITED: [data class] — [failure mode]" | No | No |
| Per-criterion verdict lines | "C-NN: PASS / FAIL" | No | No |

No other element types are added to this register without revising this contract.

**Inertia annotation for C-27 — why the register must be declared closed — 3 fields: Failure mode prevented | Gap above C-25 | Concrete example (C-29, C-30):**

- **Failure mode prevented:** Implicit-complement classification — an executor reasoning
  that the complement of Section A's prose-permitted list is implicitly structured output.
  Under an open register, an executor encountering an unlisted element type has no
  classification decision to make by lookup: "it is not prose-permitted (Section A does
  not authorize it), therefore it is structured output, therefore exempt from C-23." The
  executor classifies by content-based inference rather than by register membership. This
  is the content-inspection problem C-25 was designed to eliminate: element types are
  classified by interpreting their content rather than by identifying their registered type.
- **Gap above C-25:** C-25 requires the register to enumerate element types with explicit
  Prose? and C-23-tag classifications. C-25 compliance does not require the register to
  declare itself exhaustive. An open register that satisfies C-25 leaves every unlisted
  element type in implicit-complement territory: the four-row enumeration is correct for
  the listed types, but a fifth element type is classifiable by inference alone. The
  closure declaration converts implicit-exempt to explicitly-unclassified: the registered
  set is declared exhaustive, and any unlisted element type's classification status is
  a detectable contract gap, not an inferred permission. Adding a new type requires an
  explicit revision to this contract, auditable by change history.
- **Concrete example (C-30):** A load-shape verdict label — e.g., a line reading
  "FLAT-LOAD: within nominal band" — does not match any of the four registered canonical
  forms. Gate decision line (PROCEED / BLOCKED — no match). Cross-artifact header
  ("One row per [source]..." — no match). Phase boundary prohibition ("PROHIBITED:
  [data] — [failure mode]" — no match). Per-criterion verdict ("C-NN: PASS / FAIL" —
  no match). Under an open register, the implicit-complement inference resolves the
  ambiguity: not in Section A, therefore implicitly structured output. Under a closed
  register, the inference is foreclosed: this element type is unregistered, its Prose?
  and C-23-tag classifications are explicitly unresolved, and adding it requires a named
  contract revision.

---

**PHASE 1 — EVIDENCE PHASE**

**Step 1A — SOURCE REGISTER (C-13)**

Commit the evidence base before naming any tier. Every numeric threshold cited in Steps
1B and Phase 2 must have a Source-ID entry here. A tier with no register entry receives
UNDOCUMENTED in the Limit column; it is not assigned an inferred value.

| Source-ID | Source name | Type | Numeric values it provides |
|-----------|-------------|------|---------------------------|
| S-01 | | | |
| S-02 | | | |

PROHIBITED: adding a new Source-ID after this line. — *prevents retroactive source
injection; a source entered after claims are built cannot be verified as the basis for
the numeric claim it purports to support*

**Step 1B — TIER INVENTORY**

**TABLE A — THROTTLE TIER INVENTORY ACROSS VOLUME BANDS**

*(One row per rate-limiting component. Source-ID from register required. Every cell
filled — a blank cell and "not applicable" are identical under scan.)*

| Tier-ID | Component | Limit (number + unit) | Source-ID | Scope | STATUS 1x | STATUS 2x | STATUS 5x | Binding? | Failure mode |
|---------|-----------|----------------------|-----------|-------|-----------|-----------|-----------|----------|-------------|
| T-01 | | | | | | | | | |
| T-02 | | | | | | | | | |
| ... | | | | | | | | | |

Column notes:
- `Tier-ID` — T-01, T-02, ... Use verbatim in every downstream table. Compliance
  failure condition: informal synonym fails T-NN threading requirement.
- `Limit` — specific number with unit. Compliance failure condition: vague label fails
  precision.
- `STATUS Nx` — OK / HIT / SAT. Must shift between at least two bands.
- `Binding?` — exactly one Y. Compliance failure condition: multiple Y or no Y fails
  at-most-one constraint. Designation without causal reason is an assertion, not an
  argument.
- `Failure mode` — hard rejection / queue saturation / silent drop / degraded throughput /
  timeout. At least two distinct values.

PROHIBITED: introducing a new T-NN in any Phase 2 section. — *prevents scope creep;
tier discovery during claims analysis indicates Phase 1 enumeration was incomplete*

**[prose: item 1 — binding-tier causal reason]** State why the Binding? = Y tier fails
before all others under 1x nominal load. Name the specific causal mechanism.

**[prose: item 2 — binding constraint exclusivity]** For at least one Binding? = N tier,
name the mechanism that prevents it from binding before the primary tier.

---

**PHASE 2 — CLAIMS PHASE**

PROHIBITED: opening Phase 2 before Phase 1B is complete. — *prevents late evidence
injection*

**For each tier in TABLE A (C-17):** every downstream derived table must include a row
for every T-NN. Coverage verifiable by T-NN count match against TABLE A. — *prevents
coverage elision*

**TABLE B — BACKPRESSURE PROPAGATION TRACE**

*(Source: TABLE A. Two hops minimum. T-NNs must reference TABLE A entries.)*

| Hop | From (Tier-ID) | To component | Mechanism | Observable effect |
|-----|----------------|--------------|-----------|-------------------|
| 1 | | | | |
| 2 | | | | |
| ... | | | | |

Mechanism values: queue-fill, connection-hold, retry-amplification, dependency-stall,
timeout-cascade. Compliance failure condition: generic term fails precision.

**TABLE C — USER EXPERIENCE CATALOG**

*(Source: TABLE A. One row per TABLE A Tier-ID. No tier may be omitted.)*

| Tier-ID | Error code or signal | Retry-After present? (Y/N) | Retry-After surfaced to caller? (Y/N) | Visible in run history? (Y/N/SILENT) | Failure if Retry-After ignored |
|---------|---------------------|---------------------------|--------------------------------------|--------------------------------------|-------------------------------|
| T-01 | | | | | |
| T-02 | | | | | |

Compliance failure condition: plain description in `Error code or signal` fails precision.

**TABLE D — UNPROTECTED BURST PATHS**

*(Source: TABLE A. At least one row. If no gap: ≥2 named controls as evidence.)*

| Path-ID | Entry component | Tier-IDs involved | Gap reason or named controls | Consequence at burst volume |
|---------|----------------|-------------------|-----------------------------|-----------------------------|
| P-01 | | | | |

**TABLE E — RISK TAXONOMY**

*(Source: TABLE A + TABLE B + TABLE D. Per-type minimum: ≥1 Burst, ≥1 Cascade,
≥1 RetryAfter. Type column required — count alone cannot detect category absence.)*

| Risk-ID | Tier-ID | Type | Risk description | Severity (H/M/L) |
|---------|---------|------|-----------------|-----------------|
| R-01 | | Burst | | |
| R-02 | | Cascade | | |
| R-03 | | RetryAfter | | |

Compliance failure condition: risk list without Type column with named taxonomy and
per-type minimum-row constraint fails C-22 even if all categories happen to appear.

---

**TYPE SCAN GATE**

**Purpose annotation (C-26) — three fields:**

- **Failure mode prevented:** Category elision — a risk type absent from TABLE E is
  detectable only by full table scan after TABLE F is complete; both artifacts require
  revision but TABLE F appears complete.
- **Gap above C-22:** C-22 defines what the finished output must contain. This gate makes
  an incomplete TABLE E a construction-time blocking condition before TABLE F opens. An
  executor who reasons "C-22 already requires all three types — this gate adds process
  without substance" conflates the structural requirement with the enforcement mechanism.
  C-22 ensures the structure; the gate ensures the missing-category failure mode cannot
  be produced by any valid execution path.
- **Audit test (C-28, C-31):**
  - *Gate-present audit method:* Locate the section titled **TYPE SCAN GATE** — artifact
    identifier: the exact section header string. Structural position: it appears between
    TABLE E's last row (the row carrying the highest-numbered R-NN value in the Risk-ID
    column) and the TABLE F section header. Within the TYPE SCAN GATE section, confirm
    five named observables in sequence:
    (1) A verdict line of the form `Burst: [Y / N]` — present before the gate decision line.
    (2) A verdict line of the form `Cascade: [Y / N]` — present before the gate decision line.
    (3) A verdict line of the form `RetryAfter: [Y / N]` — present before the gate decision line.
    (4) A gate decision line reading `PROCEED` or `BLOCKED` — appears after all three
    per-category verdict lines and before the TABLE F section header.
    (5) TABLE F section header and first data row (MR-01) appear after the gate decision
    line; MR-01 is not the first row after TABLE E's last R-NN.
    All five observables confirmed = gate compliance verified by artifact-ID scan.
  - *Gate-absent signature:* The structural position between TABLE E's last R-NN row and
    TABLE F's first data row (MR-01) contains no **TYPE SCAN GATE** section header.
    Named observable for the absent condition: no verdict lines of the form
    `[Category]: [Y / N]` (where Category is one of Burst, Cascade, RetryAfter) appear
    in the structural gap between R-NN and MR-01. Gate-present outputs have three named
    Y/N verdict lines before MR-01; gate-absent outputs have none.

**Escape route for C-26 — "the gate Purpose annotation is redundant because C-22 already
explains why type coverage matters" (C-32):** This reasoning conflates the *purpose of
the type taxonomy* (which C-22 explains) with the *purpose of the gate* (which is to make
type completeness a construction-time blocking condition). Without the annotation, an
executor can reason "the table already requires all three types — the gate is extra process"
and skip it. The annotation makes that reasoning auditable: the gap the gate closes
(post-hoc vs. construction-time detection) is explicitly stated and cannot be dismissed
as redundant without contradicting the stated purpose.

Scan TABLE E for type completeness:
- Burst: [at least one row present? Y / N]
- Cascade: [at least one row present? Y / N]
- RetryAfter: [at least one row present? Y / N]

If all Y: PROCEED
If any N: BLOCKED — return to TABLE E, add the missing type row, re-run this gate.

---

**TABLE F — MITIGATION REGISTRY**

*(Source: TABLE E. One row per TABLE E risk. No risk may be omitted.)*

| MR-ID | Source (Risk-ID) | Gap type | Component | Setting or API parameter | Change | Expected outcome | Tradeoff |
|-------|-----------------|----------|-----------|--------------------------|--------|-----------------|---------|
| MR-01 | | | | | | | |
| MR-02 | | | | | | | |

Compliance failure condition: category of action in `Setting or API parameter` fails
precision requirement.

PROHIBITED: adding rows to TABLE E after TABLE F has opened. — *prevents retroactive
risk injection*

---

**GLOBAL CRITERION-COVERAGE STEP**

Named dedicated step. Not embedded prose. Reports per-criterion PASS/FAIL.

- C-01 (Primary bottleneck with causal reason): [binding-tier causal reason present and
  names specific causal mechanism? PASS / FAIL]
- C-02 (Backpressure propagation ≥2 hops with mechanism): [TABLE B ≥2 rows with T-NN
  identifiers and specific mechanisms from the permitted set? PASS / FAIL]
- C-03 (≥2 tiers with enforcing component and scope): [TABLE A ≥2 rows with Component
  and Scope filled, each with specific numeric Limit? PASS / FAIL]
- C-04 (UX at each throttle tier): [TABLE C one row per TABLE A Tier-ID, no tier
  omitted? PASS / FAIL]
- C-05 (Unprotected burst path): [TABLE D ≥1 row with gap reason, or ≥1 row with ≥2
  named controls? PASS / FAIL]

[prose: item 3 — global criterion-coverage verdict notes] State FAIL rationale for any
criterion above that did not pass.

---

---

## V-03 — Single Axis: Lifecycle Emphasis (C-34 PASS — observable count at path-label level)

**Axis:** The TYPE SCAN GATE audit test path identifiers are restructured to declare
observable counts before enumeration: "*Gate-present audit method — 5 observables:*"
and "*Gate-absent signature — 1 observable:*". The observable content carries unchanged
from V-01. Section B inertia annotation carries the V-01 header without field-count
declaration — C-33 remains open.

**Hypothesis:** Elevating the observable count from embedded prose to the path-label
level satisfies C-34 independently of the C-33 change. C-34 requires the count to appear
at the path identifier, not inside the description. The form "*Gate-present audit method
— 5 observables:*" places the count (5) before the first observable, making list
completeness verifiable by count-scan: an auditor sees "5 observables", counts five items
in the numbered list, and verifies completeness without reading each observable's content.
The analogous form for the absent path: "*Gate-absent signature — 1 observable:*"
declares a closed set of one item. The compliance delta from V-01 is confined to the two
path-identifier lines in the TYPE SCAN GATE audit test.

**v12 predicted scoring:** C-33 FAIL (annotation header carries from V-01; no count
declaration). C-34 PASS (per-path count labels present: "5 observables" and "1
observable"). Composite: 215/220.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput
across the rate-limited system described in the signal. Treat the stated request volume
as 1x nominal; also analyze at 2x and 5x.

Tables are the primary output. Fill every cell. Produce sections in the order shown.

---

**OUTPUT FORMAT CONTRACT**

**Section A — PROSE-PERMITTED CONTEXTS (C-20)**

Prose is permitted in exactly three contexts. Each context declared with scope and
authorizing criterion:

1. **Binding-tier causal reason** — one paragraph at Phase 1B exit. Scope: explains
   why the Binding? = Y tier fails before all others under 1x nominal load. Authorized
   by C-01.
2. **Binding constraint exclusivity statement** — one sentence at Phase 1B exit. Scope:
   names the mechanism preventing at least one non-binding tier from binding first.
   Authorized by C-14.
3. **Global criterion-coverage verdict notes** — FAIL verdicts only, at the global
   coverage step. Scope: one sentence per failed criterion. Authorized by C-19.

Any prose passage outside these three declared scopes is a format violation detectable
without content review.

**Section B — STRUCTURED OUTPUT REGISTER (C-25, C-27)**

The following element types are structured output. They are NOT prose. They are exempt
from C-23 inline citation requirements. Classification is by element type — content
inspection is not required and is not the correct classification method.

| Element type | Canonical form | Prose? | C-23 tag required? |
|-------------|---------------|--------|-------------------|
| Gate decision lines | PROCEED / BLOCKED | No | No |
| Cross-artifact header lines | "One row per [source]. No [item] may be omitted." | No | No |
| Phase boundary prohibition lines | "PROHIBITED: [data class] — [failure mode]" | No | No |
| Per-criterion verdict lines | "C-NN: PASS / FAIL" | No | No |

No other element types are added to this register without revising this contract.

**Inertia annotation for C-27 — why the register must be declared closed (C-29, C-30):**

- **Failure mode prevented:** Implicit-complement classification — an executor reasoning
  that the complement of Section A's prose-permitted list is implicitly structured output.
  Under an open register, an executor encountering an unlisted element type has no
  classification decision to make by lookup: "it is not prose-permitted (Section A does
  not authorize it), therefore it is structured output, therefore exempt from C-23." The
  executor classifies by content-based inference rather than by register membership. This
  is the content-inspection problem C-25 was designed to eliminate.
- **Gap above C-25:** C-25 requires the register to enumerate element types with explicit
  Prose? and C-23-tag classifications. C-25 compliance does not require the register to
  declare itself exhaustive. An open register that satisfies C-25 leaves every unlisted
  element type in implicit-complement territory. The closure declaration converts
  implicit-exempt to explicitly-unclassified: the registered set is declared exhaustive,
  and any unlisted element type's classification status is a detectable contract gap,
  not an inferred permission. Adding a new type requires an explicit revision to this
  contract, auditable by change history.
- **Concrete example (C-30):** A load-shape verdict label — e.g., a line reading
  "FLAT-LOAD: within nominal band" — does not match any of the four registered canonical
  forms. Gate decision line (PROCEED / BLOCKED — no match). Cross-artifact header
  ("One row per [source]..." — no match). Phase boundary prohibition ("PROHIBITED:
  [data] — [failure mode]" — no match). Per-criterion verdict ("C-NN: PASS / FAIL" —
  no match). Under an open register, the implicit-complement inference resolves the
  ambiguity. Under a closed register, the inference is foreclosed: this element type is
  unregistered, its Prose? and C-23-tag classifications are explicitly unresolved, and
  adding it requires a named contract revision.

---

**PHASE 1 — EVIDENCE PHASE**

**Step 1A — SOURCE REGISTER (C-13)**

Commit the evidence base before naming any tier. Every numeric threshold cited in Steps
1B and Phase 2 must have a Source-ID entry here. A tier with no register entry receives
UNDOCUMENTED in the Limit column; it is not assigned an inferred value.

| Source-ID | Source name | Type | Numeric values it provides |
|-----------|-------------|------|---------------------------|
| S-01 | | | |
| S-02 | | | |

PROHIBITED: adding a new Source-ID after this line. — *prevents retroactive source
injection; a source entered after claims are built cannot be verified as the basis for
the numeric claim it purports to support*

**Step 1B — TIER INVENTORY**

**TABLE A — THROTTLE TIER INVENTORY ACROSS VOLUME BANDS**

*(One row per rate-limiting component. Source-ID from register required. Every cell
filled — a blank cell and "not applicable" are identical under scan.)*

| Tier-ID | Component | Limit (number + unit) | Source-ID | Scope | STATUS 1x | STATUS 2x | STATUS 5x | Binding? | Failure mode |
|---------|-----------|----------------------|-----------|-------|-----------|-----------|-----------|----------|-------------|
| T-01 | | | | | | | | | |
| T-02 | | | | | | | | | |
| ... | | | | | | | | | |

Column notes:
- `Tier-ID` — T-01, T-02, ... Use verbatim in every downstream table. Compliance
  failure condition: informal synonym fails T-NN threading requirement.
- `Limit` — specific number with unit. Compliance failure condition: vague label fails
  precision.
- `STATUS Nx` — OK / HIT / SAT. Must shift between at least two bands.
- `Binding?` — exactly one Y. Compliance failure condition: multiple Y or no Y fails
  at-most-one constraint.
- `Failure mode` — hard rejection / queue saturation / silent drop / degraded throughput /
  timeout. At least two distinct values.

PROHIBITED: introducing a new T-NN in any Phase 2 section. — *prevents scope creep;
tier discovery during claims analysis indicates Phase 1 enumeration was incomplete*

**[prose: item 1 — binding-tier causal reason]** State why the Binding? = Y tier fails
before all others under 1x nominal load. Name the specific causal mechanism.

**[prose: item 2 — binding constraint exclusivity]** For at least one Binding? = N tier,
name the mechanism that prevents it from binding before the primary tier.

---

**PHASE 2 — CLAIMS PHASE**

PROHIBITED: opening Phase 2 before Phase 1B is complete. — *prevents late evidence
injection*

**For each tier in TABLE A (C-17):** every downstream derived table must include a row
for every T-NN. Coverage verifiable by T-NN count match against TABLE A. — *prevents
coverage elision*

**TABLE B — BACKPRESSURE PROPAGATION TRACE**

*(Source: TABLE A. Two hops minimum. T-NNs must reference TABLE A entries.)*

| Hop | From (Tier-ID) | To component | Mechanism | Observable effect |
|-----|----------------|--------------|-----------|-------------------|
| 1 | | | | |
| 2 | | | | |
| ... | | | | |

Mechanism values: queue-fill, connection-hold, retry-amplification, dependency-stall,
timeout-cascade. Compliance failure condition: generic term fails precision.

**TABLE C — USER EXPERIENCE CATALOG**

*(Source: TABLE A. One row per TABLE A Tier-ID. No tier may be omitted.)*

| Tier-ID | Error code or signal | Retry-After present? (Y/N) | Retry-After surfaced to caller? (Y/N) | Visible in run history? (Y/N/SILENT) | Failure if Retry-After ignored |
|---------|---------------------|---------------------------|--------------------------------------|--------------------------------------|-------------------------------|
| T-01 | | | | | |
| T-02 | | | | | |

Compliance failure condition: plain description in `Error code or signal` fails precision.

**TABLE D — UNPROTECTED BURST PATHS**

*(Source: TABLE A. At least one row. If no gap: ≥2 named controls as evidence.)*

| Path-ID | Entry component | Tier-IDs involved | Gap reason or named controls | Consequence at burst volume |
|---------|----------------|-------------------|-----------------------------|-----------------------------|
| P-01 | | | | |

**TABLE E — RISK TAXONOMY**

*(Source: TABLE A + TABLE B + TABLE D. Per-type minimum: ≥1 Burst, ≥1 Cascade,
≥1 RetryAfter. Type column required — count alone cannot detect category absence.)*

| Risk-ID | Tier-ID | Type | Risk description | Severity (H/M/L) |
|---------|---------|------|-----------------|-----------------|
| R-01 | | Burst | | |
| R-02 | | Cascade | | |
| R-03 | | RetryAfter | | |

Compliance failure condition: risk list without Type column with named taxonomy and
per-type minimum-row constraint fails C-22 even if all categories happen to appear.

---

**TYPE SCAN GATE**

**Purpose annotation (C-26) — three fields:**

- **Failure mode prevented:** Category elision — a risk type absent from TABLE E is
  detectable only by full table scan after TABLE F is complete; both artifacts require
  revision but TABLE F appears complete.
- **Gap above C-22:** C-22 defines what the finished output must contain. This gate makes
  an incomplete TABLE E a construction-time blocking condition before TABLE F opens. An
  executor who reasons "C-22 already requires all three types — this gate adds process
  without substance" conflates the structural requirement with the enforcement mechanism.
  C-22 ensures the structure; the gate ensures the missing-category failure mode cannot
  be produced by any valid execution path.
- **Audit test (C-28, C-31):**
  - *Gate-present audit method — 5 observables:* Locate the section titled **TYPE SCAN
    GATE** — artifact identifier: the exact section header string. Structural position:
    it appears between TABLE E's last row (the row carrying the highest-numbered R-NN
    value in the Risk-ID column) and the TABLE F section header. Confirm the following
    5 observables in sequence:
    (1) A verdict line of the form `Burst: [Y / N]` — present before the gate decision line.
    (2) A verdict line of the form `Cascade: [Y / N]` — present before the gate decision line.
    (3) A verdict line of the form `RetryAfter: [Y / N]` — present before the gate decision line.
    (4) A gate decision line reading `PROCEED` or `BLOCKED` — appears after all three
    per-category verdict lines and before the TABLE F section header.
    (5) TABLE F section header and first data row (MR-01) appear after the gate decision
    line; MR-01 is not the first row after TABLE E's last R-NN.
    All 5 observables confirmed = gate compliance verified by count-scan and artifact-ID.
  - *Gate-absent signature — 1 observable:* The structural position between TABLE E's
    last R-NN row and TABLE F's first data row (MR-01) contains no **TYPE SCAN GATE**
    section header. Confirm the following 1 observable: no verdict lines of the form
    `[Category]: [Y / N]` (where Category is one of Burst, Cascade, RetryAfter) appear
    in the structural gap between R-NN and MR-01. Gate-present outputs have 3 named Y/N
    verdict lines before MR-01; gate-absent outputs have none. This single observable
    separates the two structural conditions.

**Escape route for C-26 — "the gate Purpose annotation is redundant because C-22 already
explains why type coverage matters" (C-32):** This reasoning conflates the *purpose of
the type taxonomy* (which C-22 explains) with the *purpose of the gate* (which is to make
type completeness a construction-time blocking condition). Without the annotation, an
executor can reason "the table already requires all three types — the gate is extra process"
and skip it. The annotation makes that reasoning auditable: the gap the gate closes
(post-hoc vs. construction-time detection) is explicitly stated and cannot be dismissed
as redundant without contradicting the stated purpose.

Scan TABLE E for type completeness:
- Burst: [at least one row present? Y / N]
- Cascade: [at least one row present? Y / N]
- RetryAfter: [at least one row present? Y / N]

If all Y: PROCEED
If any N: BLOCKED — return to TABLE E, add the missing type row, re-run this gate.

---

**TABLE F — MITIGATION REGISTRY**

*(Source: TABLE E. One row per TABLE E risk. No risk may be omitted.)*

| MR-ID | Source (Risk-ID) | Gap type | Component | Setting or API parameter | Change | Expected outcome | Tradeoff |
|-------|-----------------|----------|-----------|--------------------------|--------|-----------------|---------|
| MR-01 | | | | | | | |
| MR-02 | | | | | | | |

Compliance failure condition: category of action in `Setting or API parameter` fails
precision requirement.

PROHIBITED: adding rows to TABLE E after TABLE F has opened. — *prevents retroactive
risk injection*

---

**GLOBAL CRITERION-COVERAGE STEP**

Named dedicated step. Not embedded prose. Reports per-criterion PASS/FAIL.

- C-01 (Primary bottleneck with causal reason): [binding-tier causal reason present and
  names specific causal mechanism? PASS / FAIL]
- C-02 (Backpressure propagation ≥2 hops with mechanism): [TABLE B ≥2 rows with T-NN
  identifiers and specific mechanisms from the permitted set? PASS / FAIL]
- C-03 (≥2 tiers with enforcing component and scope): [TABLE A ≥2 rows with Component
  and Scope filled, each with specific numeric Limit? PASS / FAIL]
- C-04 (UX at each throttle tier): [TABLE C one row per TABLE A Tier-ID, no tier
  omitted? PASS / FAIL]
- C-05 (Unprotected burst path): [TABLE D ≥1 row with gap reason, or ≥1 row with ≥2
  named controls? PASS / FAIL]

[prose: item 3 — global criterion-coverage verdict notes] State FAIL rationale for any
criterion above that did not pass.

---

---

## V-04 — Combined Axes: C-33 + C-34 (both changes, single-role form)

**Axes:** (1) Inertia framing — Section B annotation header declares field count and
names: "3 fields: Failure mode prevented | Gap above C-25 | Concrete example (C-29,
C-30)". (2) Lifecycle emphasis — TYPE SCAN GATE audit path identifiers declare observable
counts: "*Gate-present audit method — 5 observables:*" and "*Gate-absent signature — 1
observable:*". Both changes applied in a single-role prompt; the delta from V-02 is the
observable count addition; the delta from V-03 is the field-count header addition; the
delta from V-01 is both changes simultaneously.

**Hypothesis:** C-33 and C-34 are orthogonal requirements in the same prompt. The
field-count header on the annotation satisfies C-33 without affecting the TYPE SCAN GATE.
The per-path count labels on the audit test satisfy C-34 without affecting Section B.
V-04 tests whether combining the two single-axis changes produces 220/220, confirming
orthogonality and that neither change interferes with the other's compliance condition.
The enforcement remains inline instruction-based; V-05 tests the role-pipeline alternative.

**v12 predicted scoring:** C-33 PASS (field-count header present). C-34 PASS (per-path
count labels present). All prior C-01 through C-32 carry from R11 V-04 baseline.
Composite: 220/220.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput
across the rate-limited system described in the signal. Treat the stated request volume
as 1x nominal; also analyze at 2x and 5x.

Tables are the primary output. Fill every cell. Produce sections in the order shown.

---

**OUTPUT FORMAT CONTRACT**

**Section A — PROSE-PERMITTED CONTEXTS (C-20)**

Prose is permitted in exactly three contexts. Each context declared with scope and
authorizing criterion:

1. **Binding-tier causal reason** — one paragraph at Phase 1B exit. Scope: explains
   why the Binding? = Y tier fails before all others under 1x nominal load. Authorized
   by C-01.
2. **Binding constraint exclusivity statement** — one sentence at Phase 1B exit. Scope:
   names the mechanism preventing at least one non-binding tier from binding first.
   Authorized by C-14.
3. **Global criterion-coverage verdict notes** — FAIL verdicts only, at the global
   coverage step. Scope: one sentence per failed criterion explaining the coverage gap.
   Authorized by C-19.

Any prose passage appearing outside these three declared scopes is a format violation
detectable without content review.

**Section B — STRUCTURED OUTPUT REGISTER (C-25, C-27)**

The following element types are structured output. They are NOT prose. They are exempt
from C-23 inline citation requirements. Classification is by element type — content
inspection is not required and is not the correct classification method.

| Element type | Canonical form | Prose? | C-23 tag required? |
|-------------|---------------|--------|-------------------|
| Gate decision lines | PROCEED / BLOCKED | No | No |
| Cross-artifact header lines | "One row per [source]. No [item] may be omitted." | No | No |
| Phase boundary prohibition lines | "PROHIBITED: [data class] — [failure mode]" | No | No |
| Per-criterion verdict lines | "C-NN: PASS / FAIL" | No | No |

No other element types are added to this register without revising this contract.

**Inertia annotation for C-27 — why the register must be declared closed — 3 fields: Failure mode prevented | Gap above C-25 | Concrete example (C-29, C-30):**

- **Failure mode prevented:** Implicit-complement classification — an executor reasoning
  that the complement of Section A's prose-permitted list is implicitly structured output.
  Under an open register, an executor encountering an unlisted element type has no
  classification decision to make by lookup: "it is not prose-permitted (Section A does
  not authorize it), therefore it is structured output, therefore exempt from C-23." The
  executor classifies by content-based inference rather than by register membership. This
  is the content-inspection problem C-25 was designed to eliminate: element types are
  classified by interpreting their content rather than by identifying their registered type.
- **Gap above C-25:** C-25 requires the register to enumerate element types with explicit
  Prose? and C-23-tag classifications. C-25 compliance does not require the register to
  declare itself exhaustive. An open register that satisfies C-25 leaves every unlisted
  element type in implicit-complement territory: the four-row enumeration is correct for
  the listed types, but a fifth element type encountered by an executor is classifiable by
  inference alone. The closure declaration converts implicit-exempt to explicitly-
  unclassified: the registered set is declared exhaustive, and an unlisted element type's
  classification status is a detectable contract gap, not an inferred permission. Adding
  a new type requires an explicit revision to this contract, auditable by change history.
- **Concrete example (C-30):** A load-shape verdict label — e.g., a line reading
  "FLAT-LOAD: within nominal band" — does not match any of the four registered canonical
  forms. Gate decision line (PROCEED / BLOCKED — no match). Cross-artifact header
  ("One row per [source]..." — no match). Phase boundary prohibition ("PROHIBITED:
  [data] — [failure mode]" — no match). Per-criterion verdict ("C-NN: PASS / FAIL" —
  no match). Under an open register, the implicit-complement inference resolves the
  ambiguity: not in Section A, therefore implicitly structured output. Under a closed
  register, the inference is foreclosed: this element type is unregistered, its Prose?
  and C-23-tag classifications are explicitly unresolved, and adding it requires a named
  contract revision. The ambiguity created by the unregistered type is independently
  testable: present the label to an executor — if the register is open, the executor
  will classify it as exempt; if the register is closed, the executor will flag it as
  unresolved.

---

**PHASE 1 — EVIDENCE PHASE**

**Step 1A — SOURCE REGISTER (C-13)**

Commit the evidence base before naming any tier. Every numeric threshold cited in Steps
1B and Phase 2 must have a Source-ID entry here. A tier with no register entry receives
UNDOCUMENTED in the Limit column; it is not assigned an inferred value.

| Source-ID | Source name | Type | Numeric values it provides |
|-----------|-------------|------|---------------------------|
| S-01 | | | |
| S-02 | | | |

PROHIBITED: adding a new Source-ID after this line. — *prevents retroactive source
injection; a source entered after claims are built cannot be verified as the basis for
the numeric claim it purports to support — it may be post-hoc attribution assembled to
satisfy C-11 rather than a pre-committed evidence source*

**Step 1B — TIER INVENTORY**

**TABLE A — THROTTLE TIER INVENTORY ACROSS VOLUME BANDS**

*(One row per rate-limiting component. Source-ID from register required. Every cell
filled — a blank cell and "not applicable" are identical under scan.)*

| Tier-ID | Component | Limit (number + unit) | Source-ID | Scope | STATUS 1x | STATUS 2x | STATUS 5x | Binding? | Failure mode |
|---------|-----------|----------------------|-----------|-------|-----------|-----------|-----------|----------|-------------|
| T-01 | | | | | | | | | |
| T-02 | | | | | | | | | |
| ... | | | | | | | | | |

Column notes:
- `Tier-ID` — T-01, T-02, ... Use verbatim in every downstream table. Compliance
  failure condition: an informal synonym in place of T-NN fails the tier-ID threading
  requirement and makes cross-section tracing a name-resolution task.
- `Limit` — a specific number with a unit (e.g., "1,200 req/min", "500 connections").
  Compliance failure condition: a vague label ("limited", "throttled") fails precision.
- `STATUS Nx` — OK / HIT / SAT. Must shift between at least two bands. A tier that
  never transitions cannot be the primary bottleneck at any band.
- `Binding?` — exactly one Y. Compliance failure condition: multiple Y entries fail the
  at-most-one binding constraint; a designation without causal reason is an assertion,
  not an argument.
- `Failure mode` — hard rejection / queue saturation / silent drop / degraded throughput /
  timeout. At least two distinct values across rows.

PROHIBITED: introducing a new T-NN in any Phase 2 section. — *prevents scope creep;
tier discovery during claims analysis indicates Phase 1 enumeration was incomplete —
return to Step 1B, complete the registry, restart Phase 2 from the point of discovery*

**[prose: item 1 — binding-tier causal reason]** State why the Binding? = Y tier fails
before all others under 1x nominal load. Name the specific causal mechanism.

**[prose: item 2 — binding constraint exclusivity]** For at least one Binding? = N tier,
name the mechanism that prevents it from binding before the primary tier.

---

**PHASE 2 — CLAIMS PHASE**

PROHIBITED: opening Phase 2 before Phase 1B is complete. — *prevents late evidence
injection; claims built on an incomplete tier inventory produce unverifiable findings*

**For each tier in TABLE A (C-17):** every downstream derived table must include a row
for every T-NN. Coverage verifiable by T-NN count match against TABLE A, not by reading
downstream content. — *prevents coverage elision; a tier absent from a derived table
produces a detectable T-NN count gap*

**TABLE B — BACKPRESSURE PROPAGATION TRACE**

*(Source: TABLE A. Two hops minimum. T-NNs must reference TABLE A entries.)*

| Hop | From (Tier-ID) | To component | Mechanism | Observable effect |
|-----|----------------|--------------|-----------|-------------------|
| 1 | | | | |
| 2 | | | | |
| ... | | | | |

Mechanism values: queue-fill, connection-hold, retry-amplification, dependency-stall,
timeout-cascade. Compliance failure condition: a generic term ("blocked", "throttled")
in place of a named mechanism from the permitted set fails precision.

**TABLE C — USER EXPERIENCE CATALOG**

*(Source: TABLE A. One row per TABLE A Tier-ID. No tier may be omitted.)*

| Tier-ID | Error code or signal | Retry-After present? (Y/N) | Retry-After surfaced to caller? (Y/N) | Visible in run history? (Y/N/SILENT) | Failure if Retry-After ignored |
|---------|---------------------|---------------------------|--------------------------------------|--------------------------------------|-------------------------------|
| T-01 | | | | | |
| T-02 | | | | | |

Compliance failure condition: plain description ("request fails", "throttle error") in
`Error code or signal` in place of a specific HTTP status code or platform signal
identifier fails precision.

**TABLE D — UNPROTECTED BURST PATHS**

*(Source: TABLE A. At least one row. If no unprotected path exists, row 1 names ≥2
controls as evidence that every entry point is protected.)*

| Path-ID | Entry component | Tier-IDs involved | Gap reason or named controls | Consequence at burst volume |
|---------|----------------|-------------------|-----------------------------|-----------------------------|
| P-01 | | | | |

**TABLE E — RISK TAXONOMY**

*(Source: TABLE A + TABLE B + TABLE D. Per-type minimum: ≥1 Burst, ≥1 Cascade,
≥1 RetryAfter. Type column required — a count requirement without type classification
can be satisfied by two rows of the same failure category, leaving an entire category
undetected without a type scan.)*

| Risk-ID | Tier-ID | Type | Risk description | Severity (H/M/L) |
|---------|---------|------|-----------------|-----------------|
| R-01 | | Burst | | |
| R-02 | | Cascade | | |
| R-03 | | RetryAfter | | |

Compliance failure condition: a risk list without a Type column with named taxonomy and
per-type minimum-row constraint fails C-22 even if all required categories happen to
appear, because the mechanism that makes category absence detectable is absent.

---

**TYPE SCAN GATE**

**Purpose annotation (C-26) — three fields:**

- **Failure mode prevented:** Category elision — a risk type (Burst, Cascade, or
  RetryAfter) is absent from TABLE E but detectable only by full table scan after TABLE F
  is complete. At that point, TABLE F also has no mitigations for the missing category —
  two artifacts are incomplete and both require revision.
- **Gap above C-22:** C-22 ensures the Type column is present and all three categories
  appear in the *finished* TABLE E. This gate ensures type completeness is verified
  *before TABLE F opens*. C-22 defines what the finished output must contain; this gate
  makes an incomplete TABLE E a construction-time blocking condition. An executor who
  reasons "C-22 already requires all three types — this gate adds process without
  substance" conflates the structural requirement with the enforcement mechanism. C-22
  ensures the structure; the gate ensures the missing-category failure mode cannot be
  produced by any valid execution path.
- **Audit test (C-28, C-31):**
  - *Gate-present audit method — 5 observables:* Locate the section titled **TYPE SCAN
    GATE** — artifact identifier: the exact section header string. Structural position:
    it appears between TABLE E's last row (the row carrying the highest-numbered R-NN
    value in the Risk-ID column) and the TABLE F section header. Confirm the following
    5 observables in sequence:
    (1) A verdict line of the form `Burst: [Y / N]` — present before the gate decision line.
    (2) A verdict line of the form `Cascade: [Y / N]` — present before the gate decision line.
    (3) A verdict line of the form `RetryAfter: [Y / N]` — present before the gate decision line.
    (4) A gate decision line reading `PROCEED` or `BLOCKED` — appears after all three
    per-category verdict lines and before the TABLE F section header.
    (5) TABLE F section header and first data row (MR-01) appear after the gate decision
    line; MR-01 is not the first row after TABLE E's last R-NN.
    All 5 observables confirmed = gate compliance verified by count-scan and artifact-ID.
  - *Gate-absent signature — 1 observable:* The structural position between TABLE E's
    last R-NN row and TABLE F's first data row (MR-01) contains no **TYPE SCAN GATE**
    section header. Confirm the following 1 observable: no verdict lines of the form
    `[Category]: [Y / N]` (where Category is one of Burst, Cascade, RetryAfter) appear
    in the structural gap between R-NN and MR-01. Gate-present outputs have 3 named Y/N
    verdict lines before MR-01; gate-absent outputs have none. This single observable
    separates the two structural conditions.

**Escape route for C-26 — "the gate Purpose annotation is redundant because C-22 already
explains why type coverage matters" (C-32):** This reasoning conflates the *purpose of
the type taxonomy* (which C-22 explains) with the *purpose of the gate* (which is to make
type completeness a construction-time blocking condition). C-22's requirement is present
in the TABLE E header; the gate annotation explains why a named structural check is
necessary given that C-22 is already present. Without the annotation, an executor can
reason "the table already requires all three types — the gate is extra process" and skip
it. The annotation makes that reasoning auditable: the gap the gate closes (post-hoc vs.
construction-time detection) is explicitly stated and cannot be dismissed as redundant
without contradicting the stated purpose.

Scan TABLE E for type completeness:
- Burst: [at least one row present? Y / N]
- Cascade: [at least one row present? Y / N]
- RetryAfter: [at least one row present? Y / N]

If all Y: PROCEED
If any N: BLOCKED — return to TABLE E, add the missing type row, re-run this gate.

---

**TABLE F — MITIGATION REGISTRY**

*(Source: TABLE E. One row per TABLE E risk. No risk may be omitted.)*

| MR-ID | Source (Risk-ID) | Gap type | Component | Setting or API parameter | Change | Expected outcome | Tradeoff |
|-------|-----------------|----------|-----------|--------------------------|--------|-----------------|---------|
| MR-01 | | | | | | | |
| MR-02 | | | | | | | |

Compliance failure condition: a category of action ("add retry logic") in `Setting or
API parameter` in place of a specific parameter identifier (e.g., `connector.retryPolicy`)
fails precision. A row naming a category cannot be applied without further research; a
row naming an exact parameter can be applied immediately.

PROHIBITED: adding rows to TABLE E after TABLE F has opened. — *prevents retroactive
risk injection; a risk discovered during mitigation planning requires returning to
TABLE E, completing it, re-running the TYPE SCAN GATE, then re-opening TABLE F*

---

**GLOBAL CRITERION-COVERAGE STEP**

Named dedicated step. Not embedded prose. Maps output content to essential criterion
categories by name. Reports per-criterion PASS/FAIL verdict.

- C-01 (Primary bottleneck with causal reason): [binding-tier causal reason present and
  names the specific causal mechanism? PASS / FAIL]
- C-02 (Backpressure propagation ≥2 hops with mechanism): [TABLE B has ≥2 rows with
  T-NN identifiers from TABLE A and specific mechanisms from the permitted set? PASS / FAIL]
- C-03 (≥2 tiers with enforcing component and scope): [TABLE A has ≥2 rows with Component
  and Scope filled, each with a specific numeric Limit? PASS / FAIL]
- C-04 (UX at each throttle tier): [TABLE C has one row per TABLE A Tier-ID and no tier
  is omitted? PASS / FAIL]
- C-05 (Unprotected burst path): [TABLE D has ≥1 row with gap reason, or ≥1 row with
  ≥2 named controls as evidence of full protection? PASS / FAIL]

[prose: item 3 — global criterion-coverage verdict notes] State FAIL rationale for any
criterion above that did not pass.

---

---

## V-05 — Role Sequence + All Axes: Three-Role Pipeline with C-33 + C-34

**Axes:** (1) Role sequence — three-role pipeline: Format Analyst produces the complete
OUTPUT FORMAT CONTRACT including the field-count header on the inertia annotation; Domain
Expert produces evidence and claims through TABLE E; Consequence Analyst activates only
after the TYPE SCAN GATE is cleared and produces TABLE F with count-declared observable
audit paths and the global coverage step. (2) Inertia framing — Format Analyst's Section B
annotation carries the field-count header: "3 fields: Failure mode prevented | Gap above
C-25 | Concrete example (C-29, C-30)". (3) Lifecycle emphasis — Consequence Analyst's
TYPE SCAN GATE carries count-declared path identifiers: "5 observables" and "1 observable".

**Hypothesis:** The three-role pipeline provides structural enforcement for C-33 and C-34
beyond V-04's inline instructions. The Format Analyst must produce the field-count header
as a role deliverable — the contract is declared COMPLETE before Role 2 opens, so the
field count is locked before any element type classification question arises. The
Consequence Analyst's TYPE SCAN GATE with count-declared observable paths is Role 3's
entry point — the count declarations appear at the structural boundary where the gate
result determines Role 3 activation, not as inline notes an executor may skip. The
enforcement for C-33 is architectural (the annotation is a FORMAT CONTRACT deliverable)
and the enforcement for C-34 is role-boundary (the count labels are part of the gate
that triggers Role 3). The delta from V-04 is the role pipeline structure alone; all
textual content for C-33 and C-34 is identical.

**v12 predicted scoring:** C-33 PASS (Format Analyst produces field-count header as
contract deliverable). C-34 PASS (Consequence Analyst TYPE SCAN GATE has per-path count
labels at the role boundary). All prior C-01 through C-32 carry from R11 V-05 baseline.
Composite: 220/220.

---

**ROLE 1 — FORMAT ANALYST**

You are the Format Analyst. Your output is the complete OUTPUT FORMAT CONTRACT below.
The Domain Expert (Role 2) and Consequence Analyst (Role 3) are bound by this contract
and may not modify it. Produce the contract by filling every section, then state
"FORMAT CONTRACT COMPLETE" before Role 2 activates.

---

**OUTPUT FORMAT CONTRACT**

**Section A — PROSE-PERMITTED CONTEXTS (C-20)**

Prose is permitted in exactly three contexts. Each context is declared with scope and
authorizing criterion:

1. **Binding-tier causal reason** — one paragraph at Phase 1B exit. Scope: explains
   why the Binding? = Y tier fails before all others under 1x nominal load. Authorized
   by C-01.
2. **Binding constraint exclusivity statement** — one sentence at Phase 1B exit. Scope:
   names the mechanism that prevents at least one non-binding tier from binding before
   the primary tier. Authorized by C-14.
3. **Global criterion-coverage verdict notes** — FAIL verdicts only, at the global
   coverage step. Scope: one sentence per failed criterion explaining the coverage gap.
   Authorized by C-19.

Any prose passage appearing outside these three declared scopes is a format violation
detectable without content review — the element appears in narrative position and matches
none of the three declared scopes.

**Section B — STRUCTURED OUTPUT REGISTER (C-25, C-27)**

The following element types are structured output. They are NOT prose. They are exempt
from C-23 inline citation requirements. Classification is by element type — content
inspection is not required and is not the correct classification method.

| Element type | Canonical form | Prose? | C-23 tag required? |
|-------------|---------------|--------|-------------------|
| Gate decision lines | PROCEED / BLOCKED | No | No |
| Cross-artifact header lines | "One row per [source]. No [item] may be omitted." | No | No |
| Phase boundary prohibition lines | "PROHIBITED: [data class] — [failure mode]" | No | No |
| Per-criterion verdict lines | "C-NN: PASS / FAIL" | No | No |

No other element types are added to this register without revising this contract.

**Inertia annotation for C-27 — why the register must be declared closed — 3 fields: Failure mode prevented | Gap above C-25 | Concrete example (C-29, C-30):**

- **Failure mode prevented:** Implicit-complement classification — an executor reasoning
  that the complement of Section A's prose-permitted list is implicitly structured output.
  Under an open register, an executor encountering an unlisted element type has no
  classification decision to make by lookup: "it is not prose-permitted (Section A does
  not authorize it), therefore it is structured output, therefore exempt from C-23." The
  executor classifies by content-based inference rather than by register membership. This
  is the content-inspection problem C-25 was designed to eliminate: element types are
  classified by interpreting their content rather than by identifying their registered type.
- **Gap above C-25:** C-25 requires the register to enumerate element types with explicit
  Prose? and C-23-tag classifications. C-25 compliance does not require the register to
  declare itself exhaustive. An open register that satisfies C-25 leaves every unlisted
  element type in implicit-complement territory: the four-row enumeration is correct for
  the listed types, but a fifth element type is classifiable by inference alone. The
  closure declaration converts implicit-exempt to explicitly-unclassified: the registered
  set is declared exhaustive, and any unlisted element type's classification status is
  a detectable contract gap, not an inferred permission. Adding a new type requires an
  explicit revision to this contract, auditable by change history.
- **Concrete example (C-30):** A load-shape verdict label — e.g., a line reading
  "FLAT-LOAD: within nominal band" — does not match any of the four registered canonical
  forms. Gate decision line (PROCEED / BLOCKED — no match). Cross-artifact header
  ("One row per [source]..." — no match). Phase boundary prohibition ("PROHIBITED:
  [data] — [failure mode]" — no match). Per-criterion verdict ("C-NN: PASS / FAIL" —
  no match). Under an open register, the implicit-complement inference resolves the
  ambiguity: not in Section A, therefore implicitly structured output. Under a closed
  register, the inference is foreclosed: this element type is unregistered, its Prose?
  and C-23-tag classifications are explicitly unresolved, and adding it requires a named
  contract revision. The ambiguity created by the unregistered type is independently
  testable: present the label to an executor — if the register is open, the executor
  will classify it as exempt; if the register is closed, the executor will flag it as
  unresolved.

FORMAT CONTRACT COMPLETE

---

**ROLE 2 — DOMAIN EXPERT**

You are a Connectors / Power Automate throughput domain expert. The OUTPUT FORMAT
CONTRACT from Role 1 governs all output you produce. You are bound by Section A and
Section B and may not modify the contract.

Simulate throughput across the rate-limited system described in the signal. Treat the
stated request volume as 1x nominal; also analyze at 2x and 5x.

---

**PHASE 1 — EVIDENCE PHASE**

**PHASE 1 ENTRY CONDITION:** Phase 1 opens only after FORMAT CONTRACT COMPLETE is stated.

**Step 1A — SOURCE REGISTER (C-13)**

Commit the evidence base before naming any tier. Every numeric threshold cited in Steps
1B and Phase 2 must have a Source-ID entry here. A tier with no register entry receives
UNDOCUMENTED in the Limit column; it is not assigned an inferred value.

| Source-ID | Source name | Type | Numeric values it provides |
|-----------|-------------|------|---------------------------|
| S-01 | | | |
| S-02 | | | |

PROHIBITED: adding a new Source-ID after this line. — *prevents retroactive source
injection; a source entered after claims are built cannot be verified as the basis for
the numeric claim it purports to support — it may be post-hoc attribution assembled to
satisfy C-11 rather than a pre-committed evidence source*

**Step 1B — TIER INVENTORY**

**TABLE A — THROTTLE TIER INVENTORY ACROSS VOLUME BANDS**

*(One row per rate-limiting component. Source-ID from register required. Every cell
filled — a blank cell and "not applicable" are identical under scan.)*

| Tier-ID | Component | Limit (number + unit) | Source-ID | Scope | STATUS 1x | STATUS 2x | STATUS 5x | Binding? | Failure mode |
|---------|-----------|----------------------|-----------|-------|-----------|-----------|-----------|----------|-------------|
| T-01 | | | | | | | | | |
| T-02 | | | | | | | | | |
| ... | | | | | | | | | |

Column notes:
- `Tier-ID` — T-01, T-02, ... Use verbatim in every downstream table. Compliance
  failure condition: an informal synonym in place of T-NN fails the tier-ID threading
  requirement and makes cross-section tracing a name-resolution task.
- `Limit` — a specific number with a unit (e.g., "1,200 req/min", "500 connections").
  Compliance failure condition: a vague label ("limited", "throttled") fails precision.
- `STATUS Nx` — OK / HIT / SAT. Must shift between at least two bands. A tier that
  never transitions cannot be the primary bottleneck at any band.
- `Binding?` — exactly one Y. Compliance failure condition: multiple Y entries fail the
  at-most-one binding constraint; a designation without causal reason is an assertion,
  not an argument.
- `Failure mode` — hard rejection / queue saturation / silent drop / degraded throughput /
  timeout. At least two distinct values across rows.

PROHIBITED: introducing a new T-NN in any Phase 2 section. — *prevents scope creep;
evidence that Phase 1 enumeration was incomplete is not a fill-in opportunity — return
to Step 1B, complete the registry, restart Phase 2 from the point of discovery*

**[prose: item 1 — binding-tier causal reason]** State why the Binding? = Y tier fails
before all others under 1x nominal load. Name the specific causal mechanism.

**[prose: item 2 — binding constraint exclusivity]** For at least one Binding? = N tier,
name the mechanism that prevents it from binding before the primary tier.

**STEP 1B GATE:** Every TABLE A row has all columns filled with non-placeholder values.
No vague labels in the Limit column.

PROHIBITED: opening Phase 2 before the STEP 1B GATE is cleared. — *prevents late
evidence injection; claims built on an incomplete tier inventory produce unverifiable
findings*

---

**PHASE 2 — CLAIMS PHASE**

**PHASE 2 ENTRY CONDITION:** Phase 2 opens only after the STEP 1B GATE is cleared.
The tier registry is closed.

**Enumeration anchor — for each tier in TABLE A (C-17):** every downstream derived
table must include a row for every T-NN. Coverage verifiable by T-NN count match against
TABLE A, not by reading downstream content. — *prevents coverage elision; a tier absent
from a derived table produces a detectable T-NN count gap*

**TABLE B — BACKPRESSURE PROPAGATION TRACE**

*(Source: TABLE A. Two hops minimum. T-NNs must reference TABLE A entries.)*

| Hop | From (Tier-ID) | To component | Mechanism | Observable effect |
|-----|----------------|--------------|-----------|-------------------|
| 1 | | | | |
| 2 | | | | |
| ... | | | | |

Mechanism values: queue-fill, connection-hold, retry-amplification, dependency-stall,
timeout-cascade. Compliance failure condition: a generic term ("blocked", "throttled")
in place of a named mechanism from the permitted set fails precision.

**TABLE C — USER EXPERIENCE CATALOG**

*(Source: TABLE A. One row per TABLE A Tier-ID. No tier may be omitted.)*

| Tier-ID | Error code or signal | Retry-After present? (Y/N) | Retry-After surfaced to caller? (Y/N) | Visible in run history? (Y/N/SILENT) | Failure if Retry-After ignored |
|---------|---------------------|---------------------------|--------------------------------------|--------------------------------------|-------------------------------|
| T-01 | | | | | |
| T-02 | | | | | |

Compliance failure condition: plain description ("request fails", "throttle error") in
`Error code or signal` in place of a specific HTTP status code or platform signal
identifier fails precision.

**TABLE D — UNPROTECTED BURST PATHS**

*(Source: TABLE A. At least one row. If no unprotected path exists, row 1 names ≥2
controls as evidence that every entry point is protected.)*

| Path-ID | Entry component | Tier-IDs involved | Gap reason or named controls | Consequence at burst volume |
|---------|----------------|-------------------|-----------------------------|-----------------------------|
| P-01 | | | | |

**TABLE E — RISK TAXONOMY**

*(Source: TABLE A + TABLE B + TABLE D. Per-type minimum: ≥1 Burst, ≥1 Cascade,
≥1 RetryAfter. Type column required — a count requirement without type classification
can be satisfied by two rows of the same failure category, leaving an entire category
undetected without a type scan.)*

| Risk-ID | Tier-ID | Type | Risk description | Severity (H/M/L) |
|---------|---------|------|-----------------|-----------------|
| R-01 | | Burst | | |
| R-02 | | Cascade | | |
| R-03 | | RetryAfter | | |

Compliance failure condition: a risk list without a Type column with named taxonomy and
per-type minimum-row constraint fails C-22 even if all required categories happen to
appear, because the mechanism that makes category absence detectable is absent.

ROLE 2 COMPLETE. The Consequence Analyst (Role 3) activates after the TYPE SCAN GATE
below is cleared.

---

**TYPE SCAN GATE**

**Purpose annotation (C-26) — three fields:**

- **Failure mode prevented:** Category elision — a risk type (Burst, Cascade, or
  RetryAfter) is absent from TABLE E but the absence is detectable only by a full table
  scan after TABLE F is complete. At that point, TABLE F also has no mitigations for the
  missing category — two artifacts are incomplete and both must be revised.
- **Gap above C-22:** C-22 ensures the Type column is present and all three categories
  appear in the *finished* TABLE E. This gate ensures type completeness is verified
  *before TABLE F opens*. The distinction: C-22 defines what the finished output must
  contain; this gate makes an incomplete TABLE E a construction-time blocking condition.
  An executor who reasons "C-22 already requires all three types — this gate adds process
  without adding substance" conflates the structural requirement (what the output must
  contain) with the enforcement mechanism (when completeness is verified). C-22 ensures
  the structure; the gate ensures the missing-category failure mode cannot be produced
  by any valid execution path — an executor following the gate cannot open TABLE F
  against an incomplete risk inventory.
- **Audit test (C-28, C-31):**
  - *Gate-present audit method — 5 observables:* Locate the section titled **TYPE SCAN
    GATE** — artifact identifier: the exact section header string. Structural position:
    it appears between TABLE E's last row (the row carrying the highest-numbered R-NN
    value in the Risk-ID column) and the TABLE F section header. Confirm the following
    5 observables in sequence:
    (1) A verdict line of the form `Burst: [Y / N]` — present before the gate decision line.
    (2) A verdict line of the form `Cascade: [Y / N]` — present before the gate decision line.
    (3) A verdict line of the form `RetryAfter: [Y / N]` — present before the gate decision line.
    (4) A gate decision line reading `PROCEED` or `BLOCKED` — appears after all three
    per-category verdict lines and before the TABLE F section header.
    (5) TABLE F section header and first data row (MR-01) appear after the gate decision
    line; MR-01 is not the first row after TABLE E's last R-NN row.
    All 5 observables confirmed by artifact-ID scan = gate compliance verified by
    count-scan.
  - *Gate-absent signature — 1 observable:* The structural position between TABLE E's
    last R-NN row and TABLE F's first data row (MR-01) contains no **TYPE SCAN GATE**
    section header. Confirm the following 1 observable: no verdict lines of the form
    `[Category]: [Y / N]` (where Category is one of Burst, Cascade, RetryAfter) appear
    in the structural gap between R-NN and MR-01. Gate-present outputs have 3 named Y/N
    verdict lines before MR-01; gate-absent outputs have none. This single observable is
    the distinguishing condition between the two structural states.

**Escape route for C-26 — "the gate Purpose annotation is redundant because C-22 already
explains why type coverage matters" (C-32):** This reasoning conflates the *purpose of
the type taxonomy* (which C-22 explains) with the *purpose of the gate* (which is to make
type completeness a construction-time blocking condition). C-22's requirement is present
in the TABLE E header; the gate annotation explains why a named structural check is
necessary given that C-22 is already present. Without the annotation, an executor can
reason "the table already requires all three types — the gate is extra process" and skip
it. The annotation makes that reasoning auditable: the gap the gate closes (post-hoc vs.
construction-time detection) is explicitly stated and cannot be dismissed as redundant
without contradicting the stated purpose.

Scan TABLE E for type completeness:
- Burst: [at least one row present? Y / N]
- Cascade: [at least one row present? Y / N]
- RetryAfter: [at least one row present? Y / N]

If all Y: PROCEED
If any N: BLOCKED — return to Role 2, add the missing type row to TABLE E, re-run this
gate before Role 3 activates.

---

**ROLE 3 — CONSEQUENCE ANALYST**

You are the Consequence Analyst. You activate only after PROCEED is stated at the TYPE
SCAN GATE. Your scope is TABLE F (mitigation registry) and the global criterion-coverage
step. You are bound by the OUTPUT FORMAT CONTRACT from Role 1.

**TABLE F — MITIGATION REGISTRY**

*(Source: TABLE E. One row per TABLE E risk. No risk may be omitted.)*

| MR-ID | Source (Risk-ID) | Gap type | Component | Setting or API parameter | Change | Expected outcome | Tradeoff |
|-------|-----------------|----------|-----------|--------------------------|--------|-----------------|---------|
| MR-01 | | | | | | | |
| MR-02 | | | | | | | |

Compliance failure condition: a category of action ("add retry logic") in `Setting or
API parameter` in place of a specific parameter identifier (e.g., `connector.retryPolicy`)
fails precision. A row naming a category cannot be applied without further research; a
row naming an exact parameter can be applied immediately.

PROHIBITED: adding rows to TABLE E after TABLE F has opened. — *prevents retroactive
risk injection; a risk discovered during mitigation planning is evidence TABLE E was
incomplete — return to Role 2, complete TABLE E, re-run the TYPE SCAN GATE, re-open
TABLE F*

---

**GLOBAL CRITERION-COVERAGE STEP**

Named dedicated step. Not embedded prose. Maps output content to essential criterion
categories by name. Reports per-criterion PASS/FAIL verdict.

- C-01 (Primary bottleneck with causal reason): [binding-tier causal reason present and
  names the specific causal mechanism? PASS / FAIL]
- C-02 (Backpressure propagation ≥2 hops with mechanism): [TABLE B has ≥2 rows with
  T-NN identifiers from TABLE A and specific mechanisms from the permitted set? PASS / FAIL]
- C-03 (≥2 tiers with enforcing component and scope): [TABLE A has ≥2 rows with Component
  and Scope filled, each with a specific numeric Limit? PASS / FAIL]
- C-04 (UX at each throttle tier): [TABLE C has one row per TABLE A Tier-ID and no tier
  is omitted? PASS / FAIL]
- C-05 (Unprotected burst path): [TABLE D has ≥1 row with gap reason, or ≥1 row with
  ≥2 named controls as evidence of full protection? PASS / FAIL]

[prose: item 3 — global criterion-coverage verdict notes] State FAIL rationale for any
criterion above that did not pass.

ROLE 3 COMPLETE.
