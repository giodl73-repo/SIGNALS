# flow-throttle Variate — Round 13

**Date:** 2026-03-16
**Rubric:** v13 (C-01 through C-36, N_essential=5, N_recommended=3, N_aspirational=28)
**Max composite:** 230 | **Baseline ceiling:** R12 V-04/V-05 (220/220 under v12; 220/230 and 225/230 under v13)

---

## State Analysis: What R12 V-04/V-05 Have vs. What R13 Must Add

**R12 V-04 coverage under v13 (assessed):**
- C-01 through C-34: all pass
- C-35: FAIL — single-role form; no FORMAT CONTRACT COMPLETE at any role-handoff boundary
- C-36: FAIL — count declarations present as path labels inside the gate body; no consequence-phase role with activation conditions

**R12 V-05 coverage under v13 (assessed):**
- C-01 through C-34: all pass
- C-35: PASS — Format Analyst produces the contract and states FORMAT CONTRACT COMPLETE before Role 2 activates
- C-36: FAIL — count declarations ("5 observables", "1 observable") appear as path identifier labels inside the TYPE SCAN GATE body; Role 3 activation says "You activate only after PROCEED is stated" but does not declare the observable counts at the activation boundary

**C-35 gap in R12 V-04:**
V-04 carries the field-count header on the inertia annotation ("3 fields: Failure mode prevented | Gap above C-25 | Concrete example") and count-declared path labels ("5 observables", "1 observable") in the gate body. C-35 requires the contract to be produced by a first-phase role and sealed with FORMAT CONTRACT COMPLETE at the handoff boundary before any domain execution begins. A single-role prompt with an inline contract section cannot satisfy C-35 regardless of the contract's content quality — the criterion tests the architectural enforcement mechanism (the contract is a role deliverable, and omitting FORMAT CONTRACT COMPLETE is a handoff violation), not the contract's content.

**C-36 gap in R12 V-04 and V-05:**
Both V-04 and V-05 carry the count declarations in the TYPE SCAN GATE audit test labels. In V-04 the labels are instructional text inside the gate body. In V-05 the labels are identically positioned — "*Gate-present audit method — 5 observables:*" appears as the path identifier inside the gate's audit test section. Role 3 activates after PROCEED, but the PROCEED/BLOCKED decision depends only on the Y/N verdict lines, not on the count declarations. The count declarations are inside the gate body, not at the role-activation boundary. C-36 requires the counts to appear at the consequence-phase role activation conditions: the activation header must declare "5 observables required" so that a missing count declaration is a role-activation failure (Role 3 cannot start without seeing the declared count at its activation boundary) rather than an audit-format gap (Role 3 starts but its gate body is non-compliant).

**Summary:**

| Criterion | R12 V-04 under v13 | R12 V-05 under v13 | Gap |
|-----------|-------------------|-------------------|-----|
| C-35 | FAIL | PASS | V-04: no role pipeline; V-05: passes |
| C-36 | FAIL | FAIL | Both: counts in gate body, not at activation boundary |

**R12 V-04 under v13 composite:** 220/230
**R12 V-05 under v13 composite:** 225/230

---

## Round 13 Variation Map

| Variation | Axes | C-35 | C-36 | Predicted composite |
|-----------|------|------|------|---------------------|
| V-01 | Role sequence: C-35+C-36 FAIL isolation (V-04 single-role baseline carry) | FAIL | FAIL | 220/230 |
| V-02 | Lifecycle emphasis: C-35 PASS (FORMAT CONTRACT COMPLETE at phase boundary, no consequence role) | PASS | FAIL | 225/230 |
| V-03 | Role sequence: C-36 PASS (consequence-role activation conditions with counts, no format-phase role) | FAIL | PASS | 225/230 |
| V-04 | Combined axes: three-role pipeline, C-35 + C-36 both applied | PASS | PASS | 230/230 |
| V-05 | Combined axes + phrasing register: V-04 structure in imperative/terse register | PASS | PASS | 230/230 |

**Single-axis questions:**

Q1 (V-01 vs V-02): Does FORMAT CONTRACT COMPLETE at a phase boundary satisfy C-35 independently of C-36? Hypothesis: yes — C-35 requires the contract to be sealed with FORMAT CONTRACT COMPLETE before domain execution begins; a two-phase structure that names the first phase "Format Contract" and states FORMAT CONTRACT COMPLETE at its exit creates the handoff boundary C-35 requires, regardless of whether downstream execution is further role-partitioned.

Q2 (V-01 vs V-03): Do count declarations at a consequence-phase activation condition satisfy C-36 independently of C-35? Hypothesis: yes — C-36 requires the observable counts to appear at the activation boundary of the consequence-phase role; a two-role pipeline (Domain Expert + Consequence Analyst) with count-declared activation conditions satisfies C-36 even if no format-phase role exists and C-35 fails.

Q3 (V-04 vs V-05): Is the C-35/C-36 compliance architecture register-independent? Hypothesis: yes — FORMAT CONTRACT COMPLETE and count-declared activation conditions are structural facts about position in the prompt; phrasing register (formal vs. imperative/terse) affects token economy but not structural position, so V-04 and V-05 should score identically.

---

## V-01 — Single Axis: Role Sequence (C-35 FAIL, C-36 FAIL — V-04 single-role baseline carry)

**Axis:** Single-role form identical to R12 V-04. No role pipeline. No FORMAT CONTRACT COMPLETE at any handoff boundary. Count declarations present as path labels inside the gate body: "*Gate-present audit method — 5 observables:*" and "*Gate-absent signature — 1 observable:*". The inertia annotation carries the R12 V-04 field-count header: "3 fields: Failure mode prevented | Gap above C-25 | Concrete example (C-29, C-30)".

**Hypothesis:** C-35 fails because there is no first-phase role and no FORMAT CONTRACT COMPLETE statement — the format contract is an inline section, not a role deliverable sealed at a handoff boundary. C-36 fails because the count declarations are inside the gate body's audit test labels, not at a consequence-phase role activation boundary — the gate runs inline, and TABLE F follows in the same execution context with no named role-activation condition. C-01 through C-34 all pass (carry from R12 V-04 baseline). The compliance delta between V-01 and V-02 is exactly one structural addition: FORMAT CONTRACT COMPLETE at a phase-exit boundary. The compliance delta between V-01 and V-03 is exactly one structural addition: a consequence-phase role with count-declared activation conditions.

**v13 predicted scoring:** C-35 FAIL. C-36 FAIL. Composite: 220/230.

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
  the listed types, but a fifth element type encountered by an executor is classifiable
  by inference alone. The closure declaration converts implicit-exempt to explicitly-
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

## V-02 — Single Axis: Lifecycle Emphasis (C-35 PASS, C-36 FAIL — FORMAT CONTRACT COMPLETE at phase boundary, no consequence role)

**Axis:** Two-phase structure. Phase 0 = named Format Contract phase that produces
Section A and Section B (including the field-count header on the inertia annotation)
and terminates with FORMAT CONTRACT COMPLETE before Phase 1 opens. Phase 1 + Phase 2 +
TYPE SCAN GATE + TABLE F + GLOBAL CRITERION-COVERAGE STEP run as a single merged
execution context. The TYPE SCAN GATE audit test carries count-declared path labels
identical to V-01 ("5 observables" / "1 observable") inside the gate body — no separate
Consequence Analyst role, no count declarations at a role-activation boundary.

**Hypothesis:** FORMAT CONTRACT COMPLETE at the phase-exit boundary satisfies C-35. C-35
requires the contract to be sealed with FORMAT CONTRACT COMPLETE before domain execution
begins; naming the format section a phase and terminating it with FORMAT CONTRACT COMPLETE
creates the handoff boundary the criterion requires — the contract becomes a phase
deliverable sealed before Phase 1 opens. C-36 fails because the count declarations are
inside the gate body's path identifier labels, not at a named consequence-phase role
activation boundary. The gate runs inline within the merged execution context; no role
activation condition is declared. The compliance delta from V-01 is exactly one
structural addition: the FORMAT CONTRACT COMPLETE statement at a named phase boundary.
The compliance delta from V-04 is the absence of a separate Consequence Analyst role
with count-declared activation conditions.

**v13 predicted scoring:** C-35 PASS (FORMAT CONTRACT COMPLETE at phase boundary before
Phase 1 opens). C-36 FAIL (count declarations inside gate body, not at role-activation
boundary). Composite: 225/230.

---

**PHASE 0 — FORMAT CONTRACT PHASE**

This phase produces the complete OUTPUT FORMAT CONTRACT. Domain execution (Phase 1 and
Phase 2) does not open until FORMAT CONTRACT COMPLETE is stated at the end of this phase.

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
  element type in implicit-complement territory. The closure declaration converts
  implicit-exempt to explicitly-unclassified: the registered set is declared exhaustive,
  and an unlisted element type's classification status is a detectable contract gap, not
  an inferred permission. Adding a new type requires an explicit revision to this
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

FORMAT CONTRACT COMPLETE

---

**PHASE 1 — EVIDENCE PHASE**

**PHASE 1 ENTRY CONDITION:** Phase 1 opens only after FORMAT CONTRACT COMPLETE is stated.

You are a Connectors / Power Automate throughput domain expert. Simulate throughput
across the rate-limited system described in the signal. The OUTPUT FORMAT CONTRACT from
Phase 0 governs all output. Treat the stated request volume as 1x nominal; also analyze
at 2x and 5x.

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
  requirement.
- `Limit` — a specific number with a unit. Compliance failure condition: a vague label
  fails precision.
- `STATUS Nx` — OK / HIT / SAT. Must shift between at least two bands.
- `Binding?` — exactly one Y. A designation without causal reason is an assertion, not
  an argument.
- `Failure mode` — hard rejection / queue saturation / silent drop / degraded throughput /
  timeout. At least two distinct values across rows.

PROHIBITED: introducing a new T-NN in any Phase 2 section. — *prevents scope creep;
return to Step 1B, complete the registry, restart Phase 2 from the point of discovery*

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
  revision.
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
    `[Category]: [Y / N]` appear in the structural gap between R-NN and MR-01. This
    single observable separates the two structural conditions.

**Escape route for C-26 — "the gate Purpose annotation is redundant because C-22 already
explains why type coverage matters" (C-32):** This reasoning conflates the *purpose of
the type taxonomy* (which C-22 explains) with the *purpose of the gate* (which is to make
type completeness a construction-time blocking condition). Without the annotation, an
executor can reason "the table already requires all three types — the gate is extra
process" and skip it. The annotation makes that reasoning auditable: the gap the gate
closes (post-hoc vs. construction-time detection) is explicitly stated and cannot be
dismissed as redundant without contradicting the stated purpose.

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
precision. A row naming a category cannot be applied without further research; a row
naming an exact parameter can be applied immediately.

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

## V-03 — Single Axis: Role Sequence (C-35 FAIL, C-36 PASS — consequence-role activation conditions with counts, no format-phase role)

**Axis:** Two-role pipeline: Role 1 = Domain Expert (runs Phase 1 + Phase 2 through
TABLE E + TYPE SCAN GATE decision, then states ROLE 1 COMPLETE). Role 2 = Consequence
Analyst, whose activation conditions declare the observable counts at the role-activation
boundary before the role body opens. No Format Analyst phase — no FORMAT CONTRACT COMPLETE
at a role-handoff boundary. The inertia annotation carries the R12 V-04 field-count
header. The TYPE SCAN GATE audit test path identifiers carry the count labels inside the
gate body (as in V-01) but Role 2's activation condition block declares: "ROLE 2
ACTIVATION CONDITIONS — gate-present path: 5 observables required; gate-absent path:
1 observable required."

**Hypothesis:** The count declarations at the Role 2 activation boundary satisfy C-36.
C-36 requires the per-path count declarations to appear as role-activation conditions
for the consequence-phase role — the omission of a count declaration must be a
role-activation failure (Role 2 cannot start without seeing the declared count), not an
audit-format gap. Placing the count declarations in the ROLE 2 ACTIVATION CONDITIONS
block achieves this: an executor who reads the activation conditions sees "5 observables
required" before entering Role 2 and must verify that number before proceeding, not
discover it inside the gate body during execution. C-35 fails because there is no
format-phase role — the OUTPUT FORMAT CONTRACT is an inline section at the top of Role 1,
not a role deliverable sealed with FORMAT CONTRACT COMPLETE at a handoff boundary. The
compliance delta from V-01 is the addition of Role 2 with count-declared activation
conditions. The compliance delta from V-04 is the absence of a format-phase role.

**v13 predicted scoring:** C-35 FAIL (no format-phase role, no FORMAT CONTRACT COMPLETE
at handoff). C-36 PASS (Role 2 activation conditions declare counts: "5 observables
required" and "1 observable required" at the role boundary). Composite: 225/230.

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
  Under an open register, an executor encountering an unlisted element type classifies by
  content-based inference rather than by register membership. This is the content-
  inspection problem C-25 was designed to eliminate.
- **Gap above C-25:** C-25 requires the register to enumerate element types with explicit
  Prose? and C-23-tag classifications but does not require the register to declare itself
  exhaustive. The closure declaration converts implicit-exempt to explicitly-unclassified:
  any unlisted element type's classification status is a detectable contract gap, not an
  inferred permission. Adding a new type requires an explicit revision, auditable by
  change history.
- **Concrete example (C-30):** A load-shape verdict label — e.g., "FLAT-LOAD: within
  nominal band" — does not match any of the four registered canonical forms (PROCEED/
  BLOCKED; "One row per [source]..."; "PROHIBITED: [data] — [failure mode]"; "C-NN:
  PASS / FAIL"). Under an open register, the implicit-complement inference resolves the
  ambiguity. Under a closed register, the inference is foreclosed: this element type is
  unregistered, its classifications are explicitly unresolved, and adding it requires a
  named contract revision.

---

**ROLE 1 — DOMAIN EXPERT**

You are a Connectors / Power Automate throughput domain expert. The OUTPUT FORMAT
CONTRACT above governs all output you produce. Simulate throughput across the
rate-limited system described in the signal. Treat the stated request volume as 1x
nominal; also analyze at 2x and 5x.

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
injection*

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
- `Tier-ID` — T-01, T-02, ... Use verbatim in every downstream table.
- `Limit` — specific number with unit. Vague label fails precision.
- `STATUS Nx` — OK / HIT / SAT. Must shift between at least two bands.
- `Binding?` — exactly one Y.
- `Failure mode` — hard rejection / queue saturation / silent drop / degraded throughput /
  timeout. At least two distinct values.

PROHIBITED: introducing a new T-NN in any Phase 2 section. — *prevents scope creep*

**[prose: item 1 — binding-tier causal reason]** State why the Binding? = Y tier fails
before all others under 1x nominal load. Name the specific causal mechanism.

**[prose: item 2 — binding constraint exclusivity]** For at least one Binding? = N tier,
name the mechanism that prevents it from binding before the primary tier.

---

**PHASE 2 — CLAIMS PHASE**

PROHIBITED: opening Phase 2 before Phase 1B is complete. — *prevents late evidence
injection*

**For each tier in TABLE A (C-17):** every downstream derived table must include a row
for every T-NN. Coverage verifiable by T-NN count match against TABLE A.

**TABLE B — BACKPRESSURE PROPAGATION TRACE**

*(Source: TABLE A. Two hops minimum. T-NNs must reference TABLE A entries.)*

| Hop | From (Tier-ID) | To component | Mechanism | Observable effect |
|-----|----------------|--------------|-----------|-------------------|
| 1 | | | | |
| 2 | | | | |
| ... | | | | |

Mechanism values: queue-fill, connection-hold, retry-amplification, dependency-stall,
timeout-cascade.

**TABLE C — USER EXPERIENCE CATALOG**

*(Source: TABLE A. One row per TABLE A Tier-ID. No tier may be omitted.)*

| Tier-ID | Error code or signal | Retry-After present? (Y/N) | Retry-After surfaced to caller? (Y/N) | Visible in run history? (Y/N/SILENT) | Failure if Retry-After ignored |
|---------|---------------------|---------------------------|--------------------------------------|--------------------------------------|-------------------------------|
| T-01 | | | | | |
| T-02 | | | | | |

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

**TYPE SCAN GATE**

**Purpose annotation (C-26) — three fields:**

- **Failure mode prevented:** Category elision — a risk type absent from TABLE E is
  detectable only by full table scan after TABLE F is complete; both artifacts require
  revision.
- **Gap above C-22:** C-22 ensures the Type column is present and all three categories
  appear in the *finished* TABLE E. This gate makes an incomplete TABLE E a
  construction-time blocking condition. An executor who reasons "C-22 already requires
  all three types — this gate adds process without substance" conflates the structural
  requirement with the enforcement mechanism. C-22 ensures the structure; the gate
  ensures the missing-category failure mode cannot be produced by any valid execution
  path.
- **Audit test (C-28, C-31):**
  - *Gate-present audit method — 5 observables:* Locate the section titled **TYPE SCAN
    GATE**. Structural position: between TABLE E's last R-NN row and TABLE F section
    header. Confirm 5 observables in sequence: (1) `Burst: [Y / N]` before gate decision.
    (2) `Cascade: [Y / N]` before gate decision. (3) `RetryAfter: [Y / N]` before gate
    decision. (4) `PROCEED` or `BLOCKED` after all three verdict lines. (5) TABLE F
    header and MR-01 after gate decision line. All 5 confirmed = gate compliance verified.
  - *Gate-absent signature — 1 observable:* No **TYPE SCAN GATE** section header in the
    structural gap between TABLE E's last R-NN and MR-01. 1 observable: no `[Category]:
    [Y / N]` verdict lines in that gap.

**Escape route for C-26 — "the gate Purpose annotation is redundant because C-22 already
explains why type coverage matters" (C-32):** This reasoning conflates the purpose of
the type taxonomy (C-22) with the purpose of the gate (construction-time blocking). The
annotation makes the gate's distinct purpose auditable and non-dismissible.

Scan TABLE E for type completeness:
- Burst: [at least one row present? Y / N]
- Cascade: [at least one row present? Y / N]
- RetryAfter: [at least one row present? Y / N]

If all Y: PROCEED
If any N: BLOCKED — return to TABLE E, add the missing type row, re-run this gate.

ROLE 1 COMPLETE. The Consequence Analyst (Role 2) activates subject to the activation
conditions below.

---

**ROLE 2 — CONSEQUENCE ANALYST**

**ROLE 2 ACTIVATION CONDITIONS (C-36):**

Role 2 activates only after PROCEED is stated at the TYPE SCAN GATE AND the following
observable counts are confirmed at this boundary:

- Gate-present path — 5 observables required before Role 2 opens:
  (1) `Burst: Y` verdict line present
  (2) `Cascade: Y` verdict line present
  (3) `RetryAfter: Y` verdict line present
  (4) `PROCEED` gate decision line present
  (5) TABLE F section header and MR-01 not yet produced
  Confirming all 5 observables by count-scan at this boundary is a Role 2 entry
  condition. Role 2 cannot activate if any of the 5 observables is missing.

- Gate-absent path — 1 observable confirms non-activation:
  (1) No `[Category]: [Y / N]` verdict lines in the structural gap between TABLE E's
  last R-NN and this activation boundary.
  If this 1 observable is confirmed, the gate is absent and Role 2 cannot activate —
  return to Role 1, complete the TYPE SCAN GATE, re-confirm activation conditions.

You are the Consequence Analyst. Your scope is TABLE F (mitigation registry) and the
global criterion-coverage step. You are bound by the OUTPUT FORMAT CONTRACT above.

**TABLE F — MITIGATION REGISTRY**

*(Source: TABLE E. One row per TABLE E risk. No risk may be omitted.)*

| MR-ID | Source (Risk-ID) | Gap type | Component | Setting or API parameter | Change | Expected outcome | Tradeoff |
|-------|-----------------|----------|-----------|--------------------------|--------|-----------------|---------|
| MR-01 | | | | | | | |
| MR-02 | | | | | | | |

Compliance failure condition: category of action in `Setting or API parameter` fails
precision. A row naming an exact parameter can be applied immediately; a category name
cannot.

PROHIBITED: adding rows to TABLE E after TABLE F has opened. — *prevents retroactive
risk injection; return to Role 1, complete TABLE E, re-run the TYPE SCAN GATE,
re-confirm activation conditions, re-open TABLE F*

---

**GLOBAL CRITERION-COVERAGE STEP**

Named dedicated step. Not embedded prose. Reports per-criterion PASS/FAIL.

- C-01 (Primary bottleneck with causal reason): [PASS / FAIL]
- C-02 (Backpressure propagation ≥2 hops with mechanism): [PASS / FAIL]
- C-03 (≥2 tiers with enforcing component and scope): [PASS / FAIL]
- C-04 (UX at each throttle tier): [PASS / FAIL]
- C-05 (Unprotected burst path): [PASS / FAIL]

[prose: item 3 — global criterion-coverage verdict notes] State FAIL rationale for any
criterion above that did not pass.

ROLE 2 COMPLETE.

---

---

## V-04 — Combined Axes: Three-Role Pipeline (C-35 PASS, C-36 PASS)

**Axes:** (1) Role sequence — three-role pipeline: Format Analyst (sealed with FORMAT
CONTRACT COMPLETE at Role 1 exit) + Domain Expert + Consequence Analyst. (2) Lifecycle
emphasis — Consequence Analyst activation conditions declare observable counts at the
role boundary: "5 observables required" and "1 observable required". Both C-35 and C-36
applied simultaneously in the minimal combined form: single-role content quality per
R12 V-04, structural architecture upgraded to three-role with phase-lock and activation
conditions.

**Hypothesis:** C-35 passes — the Format Analyst produces the contract and states FORMAT
CONTRACT COMPLETE before Role 2 opens; the contract is a role deliverable sealed at a
handoff boundary, making omission of FORMAT CONTRACT COMPLETE a role-handoff violation
rather than a rubric-scan failure. C-36 passes — the Consequence Analyst's activation
conditions declare the observable counts before the role body opens; a missing count
declaration is a role-activation failure (Role 3 cannot start without the declared count
at its boundary) rather than a gate-body formatting gap. The delta from V-02 is the
addition of Role 3 with count-declared activation conditions. The delta from V-03 is
the addition of Role 1 (Format Analyst with FORMAT CONTRACT COMPLETE). The delta from
V-01 is both changes plus the role pipeline architecture.

**v13 predicted scoring:** C-35 PASS. C-36 PASS. All prior C-01–C-34 carry from R12
V-04/V-05 baseline. Composite: 230/230.

---

**ROLE 1 — FORMAT ANALYST**

You are the Format Analyst. Your output is the complete OUTPUT FORMAT CONTRACT below.
The Domain Expert (Role 2) and Consequence Analyst (Role 3) are bound by this contract
and may not modify it. Produce the contract by filling every section, then state
FORMAT CONTRACT COMPLETE before Role 2 activates.

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

**PHASE 1 ENTRY CONDITION:** Phase 1 opens only after FORMAT CONTRACT COMPLETE is stated.

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

**STEP 1B GATE:** Every TABLE A row has all columns filled with non-placeholder values.
No vague labels in the Limit column.

PROHIBITED: opening Phase 2 before the STEP 1B GATE is cleared. — *prevents late
evidence injection*

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

ROLE 2 COMPLETE. The Consequence Analyst (Role 3) activates subject to the activation
conditions below.

---

**TYPE SCAN GATE**

**Purpose annotation (C-26) — three fields:**

- **Failure mode prevented:** Category elision — a risk type (Burst, Cascade, or
  RetryAfter) is absent from TABLE E but the absence is detectable only by a full table
  scan after TABLE F is complete. At that point, TABLE F also has no mitigations for
  the missing category — two artifacts are incomplete and both must be revised.
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
If any N: BLOCKED — return to Role 2, add the missing type row to TABLE E, re-run
this gate before Role 3 activates.

---

**ROLE 3 — CONSEQUENCE ANALYST**

**ROLE 3 ACTIVATION CONDITIONS (C-36):**

Role 3 activates only after PROCEED is stated at the TYPE SCAN GATE AND the following
observable counts are confirmed at this boundary before the role body opens:

- Gate-present path — 5 observables required:
  (1) `Burst: Y` verdict line confirmed
  (2) `Cascade: Y` verdict line confirmed
  (3) `RetryAfter: Y` verdict line confirmed
  (4) `PROCEED` gate decision line confirmed
  (5) TABLE F section and MR-01 not yet produced
  All 5 observables must be count-verified at this activation boundary. A missing
  observable is a Role 3 activation failure — Role 3 cannot open TABLE F until all
  5 are confirmed.

- Gate-absent path — 1 observable confirms non-activation:
  (1) No `[Category]: [Y / N]` verdict lines in the structural gap between TABLE E's
  last R-NN and this boundary.
  If this 1 observable is confirmed (gate absent), Role 3 cannot activate — return to
  Role 2, complete the TYPE SCAN GATE, re-confirm activation conditions.

You are the Consequence Analyst. You activate only after PROCEED is stated and activation
conditions are confirmed above. Your scope is TABLE F (mitigation registry) and the
global criterion-coverage step. You are bound by the OUTPUT FORMAT CONTRACT from Role 1.

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
incomplete — return to Role 2, complete TABLE E, re-run the TYPE SCAN GATE, re-confirm
Role 3 activation conditions, re-open TABLE F*

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

---

---

## V-05 — Combined Axes + Phrasing Register: Imperative/Terse Register (C-35 PASS, C-36 PASS)

**Axes:** All V-04 axes (three-role pipeline, FORMAT CONTRACT COMPLETE at Role 1 exit,
count-declared Role 3 activation conditions) plus phrasing register variation. V-04 uses
formal/explanatory register with full compliance failure condition sentences throughout.
V-05 uses imperative/terse register: compliance failure conditions are compressed to
one-line "VIOLATION:" flags, role instructions use directive mood, annotation prose is
condensed without omitting logical content. Structural architecture is identical to V-04 —
same role pipeline, same FORMAT CONTRACT COMPLETE, same activation condition structure,
same count values. Tests whether phrasing register is orthogonal to C-35 and C-36
compliance.

**Hypothesis:** C-35 and C-36 compliance is architectural, not register-dependent.
FORMAT CONTRACT COMPLETE at Role 1 exit satisfies C-35 regardless of whether Role 1's
surrounding instructions are formal or imperative. The count declarations at Role 3's
activation boundary satisfy C-36 regardless of whether the surrounding activation
conditions are verbose or terse. If V-04 and V-05 score identically on C-35 and C-36,
phrasing register is confirmed as a non-variable for these criteria. The compliance
delta between V-04 and V-05 is register only — no structural element is added, removed,
or repositioned.

**v13 predicted scoring:** C-35 PASS. C-36 PASS. All prior C-01–C-34 carry. Composite:
230/230.

---

**ROLE 1 — FORMAT ANALYST**

Produce the OUTPUT FORMAT CONTRACT below. Roles 2 and 3 are bound by it and cannot
modify it. State FORMAT CONTRACT COMPLETE when done. Role 2 does not open until
FORMAT CONTRACT COMPLETE is stated.

---

**OUTPUT FORMAT CONTRACT**

**Section A — PROSE-PERMITTED CONTEXTS**

Three prose contexts only. Any prose outside these three is a format violation.

1. **Binding-tier causal reason** — one paragraph, Phase 1B exit. Why the Binding? = Y
   tier fails first at 1x. Authorized by C-01.
2. **Binding constraint exclusivity** — one sentence, Phase 1B exit. Mechanism
   preventing ≥1 non-binding tier from binding first. Authorized by C-14.
3. **Coverage verdict notes** — FAIL verdicts only, global coverage step. One sentence
   per FAIL. Authorized by C-19.

**Section B — STRUCTURED OUTPUT REGISTER**

These four element types are structured output. NOT prose. Exempt from C-23 citation.
Classify by element type. Do not inspect content to classify.

| Element type | Canonical form | Prose? | C-23 tag required? |
|-------------|---------------|--------|-------------------|
| Gate decision lines | PROCEED / BLOCKED | No | No |
| Cross-artifact header lines | "One row per [source]. No [item] may be omitted." | No | No |
| Phase boundary prohibition lines | "PROHIBITED: [data class] — [failure mode]" | No | No |
| Per-criterion verdict lines | "C-NN: PASS / FAIL" | No | No |

No additions without revising this contract.

**Inertia annotation — why the register must be declared closed — 3 fields: Failure mode prevented | Gap above C-25 | Concrete example (C-29, C-30):**

- **Failure mode prevented:** Implicit-complement classification. Open register: an
  executor encountering an unlisted element type infers "not in Section A prose-permitted
  list, therefore structured output, therefore C-23-exempt." Classification by inference,
  not by register lookup — exactly what C-25 prohibits.
- **Gap above C-25:** C-25 requires enumeration with explicit Prose? and C-23-tag
  classifications but does not require the register to declare itself exhaustive. Without
  closure, every unlisted type is implicitly exempt. With closure, every unlisted type
  is explicitly unclassified — a detectable contract gap, not an inferred permission.
  Any new type requires a named contract revision, auditable by change history.
- **Concrete example (C-30):** "FLAT-LOAD: within nominal band" — matches none of the
  four registered forms. Open register: implicitly exempt (not in Section A, therefore
  structured). Closed register: explicitly unclassified — contract gap, not permission.
  Independently testable: give the label to an executor. Open register: classified
  exempt. Closed register: flagged unresolved.

FORMAT CONTRACT COMPLETE

---

**ROLE 2 — DOMAIN EXPERT**

You are a Connectors / Power Automate throughput domain expert. Apply the OUTPUT FORMAT
CONTRACT from Role 1. Do not modify it. Analyze the rate-limited system in the signal
at 1x, 2x, and 5x nominal volume. Tables only — fill every cell.

**PHASE 1 ENTRY CONDITION:** Open only after FORMAT CONTRACT COMPLETE.

**Step 1A — SOURCE REGISTER**

List every source before naming any tier. Tiers with no source entry get UNDOCUMENTED
in the Limit column — no inferred values.

| Source-ID | Source name | Type | Numeric values it provides |
|-----------|-------------|------|---------------------------|
| S-01 | | | |
| S-02 | | | |

PROHIBITED: new Source-ID after this line. — *post-hoc attribution cannot be verified
as pre-committed evidence*

**Step 1B — TABLE A: THROTTLE TIER INVENTORY ACROSS VOLUME BANDS**

One row per rate-limiting component. Source-ID required. Fill every cell.

| Tier-ID | Component | Limit (number + unit) | Source-ID | Scope | STATUS 1x | STATUS 2x | STATUS 5x | Binding? | Failure mode |
|---------|-----------|----------------------|-----------|-------|-----------|-----------|-----------|----------|-------------|
| T-01 | | | | | | | | | |
| T-02 | | | | | | | | | |
| ... | | | | | | | | | |

- `Tier-ID`: T-01, T-02, ... Verbatim in all downstream tables. VIOLATION: informal
  synonym breaks T-NN threading.
- `Limit`: number + unit. VIOLATION: vague label ("limited", "throttled").
- `STATUS Nx`: OK / HIT / SAT. Must shift across at least two bands.
- `Binding?`: exactly one Y. VIOLATION: multiple Y or none.
- `Failure mode`: hard rejection / queue saturation / silent drop / degraded throughput /
  timeout. At least two distinct values.

PROHIBITED: new T-NN in Phase 2. — *return to Step 1B, complete registry, restart Phase 2*

**[prose: item 1]** Why does the Binding? = Y tier fail first at 1x? Name the causal
mechanism.

**[prose: item 2]** For ≥1 Binding? = N tier: what prevents it from binding before the
primary tier?

**STEP 1B GATE:** All TABLE A rows complete, no vague Limit values. PROHIBITED: open
Phase 2 before this gate clears.

---

**Phase 2 opens after STEP 1B GATE clears. Tier registry is closed.**

One row per T-NN in every derived table. Verify T-NN count matches TABLE A before
proceeding to each table.

**TABLE B — BACKPRESSURE PROPAGATION TRACE**

Two hops minimum. Source: TABLE A.

| Hop | From (Tier-ID) | To component | Mechanism | Observable effect |
|-----|----------------|--------------|-----------|-------------------|
| 1 | | | | |
| 2 | | | | |
| ... | | | | |

Mechanism: queue-fill / connection-hold / retry-amplification / dependency-stall /
timeout-cascade. VIOLATION: generic term.

**TABLE C — USER EXPERIENCE CATALOG**

One row per TABLE A Tier-ID. No omissions.

| Tier-ID | Error code or signal | Retry-After present? (Y/N) | Retry-After surfaced to caller? (Y/N) | Visible in run history? (Y/N/SILENT) | Failure if Retry-After ignored |
|---------|---------------------|---------------------------|--------------------------------------|--------------------------------------|-------------------------------|
| T-01 | | | | | |
| T-02 | | | | | |

VIOLATION: plain description in `Error code or signal` — use specific HTTP status code
or platform signal identifier.

**TABLE D — UNPROTECTED BURST PATHS**

At least one row. If all paths protected: row 1 names ≥2 controls.

| Path-ID | Entry component | Tier-IDs involved | Gap reason or named controls | Consequence at burst volume |
|---------|----------------|-------------------|-----------------------------|-----------------------------|
| P-01 | | | | |

**TABLE E — RISK TAXONOMY**

Sources: TABLE A + TABLE B + TABLE D. Per-type minimum: ≥1 Burst, ≥1 Cascade,
≥1 RetryAfter. Type column mandatory — count alone cannot detect a missing category.

| Risk-ID | Tier-ID | Type | Risk description | Severity (H/M/L) |
|---------|---------|------|-----------------|-----------------|
| R-01 | | Burst | | |
| R-02 | | Cascade | | |
| R-03 | | RetryAfter | | |

VIOLATION: risk list without Type column with named taxonomy and per-type minimum fails
C-22 even if all categories appear, because the detection mechanism is absent.

ROLE 2 COMPLETE. Role 3 activates subject to conditions below.

---

**TYPE SCAN GATE**

**Purpose annotation — three fields:**

- **Failure mode prevented:** Category elision — a missing risk type is detectable only
  after TABLE F is complete; at that point two artifacts are incomplete.
- **Gap above C-22:** C-22 defines the finished output requirement. This gate makes an
  incomplete TABLE E a construction-time block before TABLE F opens. An executor who
  skips the gate because "C-22 already covers this" conflates the structural requirement
  with the enforcement timing. C-22 ensures structure; the gate ensures no valid
  execution path can produce an incomplete TABLE E and an open TABLE F simultaneously.
- **Audit test:**
  - *Gate-present — 5 observables:* Section header **TYPE SCAN GATE** between TABLE E's
    last R-NN and TABLE F header. Then in sequence: (1) `Burst: Y/N`, (2) `Cascade: Y/N`,
    (3) `RetryAfter: Y/N`, (4) `PROCEED` or `BLOCKED`, (5) TABLE F header + MR-01 after
    gate decision. Count 5 observables confirmed = gate present and compliant.
  - *Gate-absent — 1 observable:* No **TYPE SCAN GATE** header between last R-NN and
    MR-01. Confirm: no `[Category]: Y/N` lines in that gap. 1 observable = gate absent.

**Escape route for C-32 — "Purpose annotation is redundant; C-22 already explains type
coverage":** Incorrect. C-22 explains the type taxonomy. The Purpose annotation explains
why a named gate is necessary even when C-22 is present. Without the annotation, an
executor can dismiss the gate as redundant. With it, dismissing the gate requires
contradicting the stated purpose.

Scan TABLE E:
- Burst: [Y / N]
- Cascade: [Y / N]
- RetryAfter: [Y / N]

All Y: PROCEED
Any N: BLOCKED — return to Role 2, complete TABLE E, re-run gate.

---

**ROLE 3 — CONSEQUENCE ANALYST**

**ROLE 3 ACTIVATION CONDITIONS:**

Activate only after PROCEED and after confirming these counts at this boundary:

Gate-present — 5 observables required before Role 3 opens:
1. `Burst: Y` present
2. `Cascade: Y` present
3. `RetryAfter: Y` present
4. `PROCEED` present
5. TABLE F and MR-01 not yet produced
VIOLATION: Role 3 opens without all 5 confirmed = activation failure.

Gate-absent — 1 observable blocks activation:
1. No `[Category]: Y/N` lines between last R-NN and this boundary.
If confirmed: gate absent — return to Role 2, complete gate, re-confirm conditions.

Apply the OUTPUT FORMAT CONTRACT from Role 1. Produce TABLE F and the global coverage
step only.

**TABLE F — MITIGATION REGISTRY**

Source: TABLE E. One row per risk. No omissions.

| MR-ID | Source (Risk-ID) | Gap type | Component | Setting or API parameter | Change | Expected outcome | Tradeoff |
|-------|-----------------|----------|-----------|--------------------------|--------|-----------------|---------|
| MR-01 | | | | | | | |
| MR-02 | | | | | | | |

VIOLATION: category of action in `Setting or API parameter` — use exact parameter
identifier (e.g., `connector.retryPolicy`). A category requires research to apply; a
parameter does not.

PROHIBITED: adding rows to TABLE E after TABLE F opens. — *incomplete TABLE E requires
return to Role 2, full TABLE E completion, gate re-run, activation re-confirm*

---

**GLOBAL CRITERION-COVERAGE STEP**

Named step. Not prose. Per-criterion PASS/FAIL.

- C-01 (Primary bottleneck with causal reason): [PASS / FAIL]
- C-02 (Backpressure ≥2 hops with mechanism): [PASS / FAIL]
- C-03 (≥2 tiers, component, scope, numeric limit): [PASS / FAIL]
- C-04 (UX at each tier): [PASS / FAIL]
- C-05 (Unprotected burst path): [PASS / FAIL]

[prose: item 3] FAIL rationale for any criterion above that did not pass.

ROLE 3 COMPLETE.
