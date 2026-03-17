# flow-throttle Variate — Round 11

**Date:** 2026-03-16
**Rubric:** v11 (C-01 through C-32, N_essential=5, N_recommended=3, N_aspirational=24)
**Max composite:** 210 | **Baseline ceiling:** R10 V-05 (confirmed passes C-01 through C-28 under v10)

---

## State Analysis: What R10 V-05 Has vs. What R11 Must Add

**R10 V-05 coverage under v11 (assessed):**
- C-01 through C-28: all pass (verified through R10)
- C-32: passes — R10 V-05 TYPE SCAN GATE carries an explicit escape-route demolisher
  labeled "Escape route for C-26 — 'the gate Purpose annotation is redundant because C-22
  already explains why type coverage matters'" and rebuts it: the reasoning conflates the
  structural requirement (C-22 defines what the output must contain) with the enforcement
  mechanism (the gate makes completeness a construction-time block). C-32's pass condition
  is an explicit rebuttal of the C-22-redundancy argument; R10 V-05 satisfies it.

**C-29 gap in R10 V-05:**
R10 V-05's Section B inertia annotation names the implicit-complement inference ("the
complement of Section A's prose-permitted list is implicitly structured output") and
explains why it reintroduces content-inspection classification. The content is present.
The form is not: the annotation is an unstructured prose paragraph. C-29 requires the
annotation to apply C-18/C-26 framing — the labeled-field structure used by PROHIBITED
annotations (C-18) and the TYPE SCAN GATE purpose annotation (C-26): named fields such
as "Failure mode prevented" and "Gap above C-25" that make each component independently
scannable. R10 V-05's prose paragraph does not use labeled fields. C-29 fails.

**C-30 gap in R10 V-05:**
C-30 requires the C-29 annotation (the labeled-field block) to name a specific element
type not in the register and state the ambiguity it would create. R10 V-05 does name
examples in its prose paragraph ("compound gate variant, a load-shape verdict label, a
phase-entry condition banner") and states the ambiguity ("must classify it by interpreting
whether its content constitutes an affirmative statement, a blocking condition, or a
narrative element"). The content is present but is not anchored to a C-29-compliant
labeled annotation — because C-29 itself fails. C-30 requires that the C-29 annotation
contain the example; there is no C-29 annotation form to contain it. C-30 fails as a
structural dependency of C-29.

**C-31 gap in R10 V-05:**
R10 V-05's TYPE SCAN GATE audit test carries two labeled sub-fields (gate-present audit
method / gate-absent signature) — satisfying C-28's two-path labeled form. The paths use
general scan language: "Scan for a named gate step between TABLE E and TABLE F"; "Confirm
three per-category Y/N verdicts are present"; "TABLE F opens immediately after TABLE E
with no intervening named gate step." C-31 requires each path to name specific observables
by artifact identifier and structural position. "Between TABLE E and TABLE F" is a
structural position but does not identify the artifact by name. "A named gate step" is
a general reference, not a named artifact identifier. "Confirm...Y/N verdicts are present"
is a scan instruction, not a named observable with a structural anchor. C-31 fails.

**Summary:**

| Criterion | R10 V-05 status under v11 | Gap |
|-----------|--------------------------|-----|
| C-29 | FAIL | Inertia annotation is prose, not labeled-field |
| C-30 | FAIL | Depends on C-29 labeled form; no C-29 annotation to contain example |
| C-31 | FAIL | Audit paths use general scan instructions, not artifact-ID observables |
| C-32 | PASS | Escape-route demolisher present and rebuts the specific argument |

**R10 V-05 under v11 composite:** 195/210 (missing C-29 + C-30 + C-31 = 3 × 5 pts)

---

## Round 11 Variation Map

| Variation | Axes | C-29 | C-30 | C-31 | C-32 | Predicted composite |
|-----------|------|------|------|------|------|---------------------|
| V-01 | Inertia framing: C-29 FAIL isolation (prose annotation, R10 V-05 baseline carry) | FAIL | FAIL | FAIL | PASS | 195/210 |
| V-02 | Inertia framing: C-29 minimal labeled (two fields, no example) | PASS | FAIL | FAIL | PASS | 200/210 |
| V-03 | Lifecycle emphasis: C-31 named-observable audit paths (prose inertia baseline) | FAIL | FAIL | PASS | PASS | 200/210 |
| V-04 | Inertia framing + Lifecycle emphasis: three-field labeled annotation + named-observable audit paths | PASS | PASS | PASS | PASS | 210/210 |
| V-05 | Role sequence + all axes: three-role pipeline + three-field C-29 annotation + named-observable C-31 audit paths | PASS | PASS | PASS | PASS | 210/210 |

**Single-axis questions:**

Q1 (V-01 vs V-02): Is the labeled-field structure (without a concrete example) sufficient
to satisfy C-29's minimum pass condition? Hypothesis: yes — C-29 requires the framing
form (Failure mode prevented / Gap above C-25 labeled fields) and names the implicit-
complement inference; the concrete example is C-30's independent requirement. A two-field
labeled annotation satisfies C-29 while leaving C-30 as the open gap. The delta between
V-01 and V-02 is exactly one structural transformation: prose paragraph to labeled fields.

Q2 (V-01 vs V-03): Does upgrading audit path language to artifact-identifier form satisfy
C-31 independently of the inertia framing change? Hypothesis: yes — C-31 requires each
audit path to name specific observables by artifact identifier and structural position.
The "TYPE SCAN GATE" section header, named per-category Y/N verdict lines, and the MR-01
structural anchor are all artifact identifiers independent of the Section B annotation
form. V-03 tests whether C-31 passes while C-29/C-30 remain open.

Q3 (V-04 vs V-05): Does the three-role pipeline produce structural enforcement that a
single-role prompt cannot? Hypothesis: yes — in a single-role prompt (V-04), the Section B
closure declaration and phase entry conditions are instructions the executor may read but
is not structurally prevented from violating. In V-05's three-role pipeline, Role 1's
"FORMAT CONTRACT COMPLETE" is the structural precondition for Role 2's activation; the
register is closed before the Domain Expert can encounter an unregistered element type.
The enforcement is architectural rather than instructional.

---

## V-01 — Single Axis: Inertia Framing (C-29 FAIL — prose annotation, R10 V-05 baseline)

**Axis:** Section B carries the R10 V-05 prose inertia annotation without structural change.
The annotation names the implicit-complement inference and explains why it reintroduces
content-inspection classification, but does not use labeled fields. The TYPE SCAN GATE
audit test carries the R10 V-05 labeled two-path form with general scan language.
All other elements carry from R10 V-05.

**Hypothesis:** V-01 is the clean baseline isolation. The content required for C-29/C-30
is present in the annotation; the structural form required by C-29 is absent. An auditor
checking C-29 cannot scan for a "Failure mode prevented" field because there is no labeled
structure — the information is embedded in prose and requires reading comprehension rather
than field-presence verification. C-30 cannot pass because the concrete example is in
the same prose paragraph, not anchored to a C-29-compliant labeled annotation. C-31 fails
because the audit paths direct general scans rather than confirming named artifacts at
structural positions.

**v11 predicted scoring:** C-29 FAIL (prose form; no labeled "Failure mode prevented" or
"Gap above C-25" fields). C-30 FAIL (no C-29 annotation to contain the example). C-31
FAIL (general scan instructions). C-32 PASS (escape-route demolisher present). Composite:
195/210.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput
across the rate-limited system described in the signal. Treat the stated request volume
as 1x nominal; also analyze at 2x and 5x.

Tables are the primary output. Fill every cell. Produce sections in the order shown.

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

**Inertia annotation for C-27 — why the register must be declared closed (C-27):**
The temptation is to leave the register open, reasoning that non-prose is the complement
of the prose-permitted list in Section A — anything not enumerated there is implicitly
structured output. This reasoning reintroduces the content-inspection problem that C-25
was designed to eliminate: an executor encountering an element type not in the register
(e.g., a compound gate variant, a load-shape verdict label, a phase-entry condition
banner) must classify it by interpreting whether its content constitutes an affirmative
statement, a blocking condition, or a narrative element. The closure declaration
forecloses content inspection: an unlisted type is explicitly unclassified, not
implicitly exempt. Its unclassified status is a detectable gap — not an implicit
permission — and adding a new type requires an explicit revision to this contract that
is auditable by change history.

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
  Compliance failure condition: a vague label ("limited", "throttled") in place of a
  specific number-with-unit fails this column's precision requirement.
- `STATUS Nx` — OK / HIT / SAT. Must shift between at least two bands. A tier that
  never transitions cannot be the primary bottleneck at any band.
- `Binding?` — exactly one Y. Compliance failure condition: multiple Y entries fail the
  at-most-one binding constraint; a designation without a causal reason is an assertion,
  not an argument.
- `Failure mode` — hard rejection / queue saturation / silent drop / degraded throughput /
  timeout. At least two distinct values across rows.

PROHIBITED: introducing a new T-NN in any Phase 2 section. — *prevents scope creep;
evidence that Phase 1 enumeration was incomplete is not a fill-in opportunity — it
requires returning to Step 1B, completing the registry, and restarting Phase 2 from
the point of discovery*

**[prose: item 1 — binding-tier causal reason]** State why the Binding? = Y tier fails
before all others under 1x nominal load. Name the specific causal mechanism.

**[prose: item 2 — binding constraint exclusivity]** For at least one Binding? = N tier,
name the mechanism that prevents it from binding before the primary tier.

---

**PHASE 2 — CLAIMS PHASE**

PROHIBITED: opening Phase 2 before Phase 1B is complete. — *prevents late evidence
injection; claims built on an incomplete tier inventory produce unverifiable findings*

**For each tier in TABLE A (C-17):** every downstream derived table must include a row
for every T-NN. Coverage is verifiable by T-NN count match against TABLE A, not by
reading downstream content. — *prevents coverage elision; a tier absent from a derived
table produces a detectable T-NN count gap*

**TABLE B — BACKPRESSURE PROPAGATION TRACE**

*(Source: TABLE A. Two hops minimum. T-NNs must reference TABLE A entries.)*

| Hop | From (Tier-ID) | To component | Mechanism | Observable effect |
|-----|----------------|--------------|-----------|-------------------|
| 1 | | | | |
| 2 | | | | |
| ... | | | | |

Mechanism values: queue-fill, connection-hold, retry-amplification, dependency-stall,
timeout-cascade. Compliance failure condition: a generic term ("blocked", "throttled")
in place of a named mechanism from the permitted set fails this column's precision
requirement.

**TABLE C — USER EXPERIENCE CATALOG**

*(Source: TABLE A. One row per TABLE A Tier-ID. No tier may be omitted.)*

| Tier-ID | Error code or signal | Retry-After present? (Y/N) | Retry-After surfaced to caller? (Y/N) | Visible in run history? (Y/N/SILENT) | Failure if Retry-After ignored |
|---------|---------------------|---------------------------|--------------------------------------|--------------------------------------|-------------------------------|
| T-01 | | | | | |
| T-02 | | | | | |

Compliance failure condition: a plain description ("request fails", "throttle error") in
`Error code or signal` in place of a specific HTTP status code or platform signal
identifier fails this column's precision requirement.

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
  RetryAfter) is absent from TABLE E but the absence is detectable only by a full table
  scan after TABLE F is complete. At that point, TABLE F also has no mitigations for
  that category — two artifacts are incomplete and both must be revised.
- **Gap above C-22:** C-22 ensures the Type column is present and all three categories
  appear in the *finished* TABLE E. This gate ensures type completeness is verified
  *before TABLE F opens*. The distinction: C-22 defines what the finished output must
  contain; this gate makes an incomplete TABLE E a construction-time blocking condition.
  An executor who reasons "C-22 already requires all three types — this gate adds process
  without adding substance" conflates the structural requirement with the enforcement
  mechanism. C-22 ensures the structure; the gate ensures the missing-category failure
  mode cannot be produced by any valid execution path.
- **Audit test (C-28):**
  - *Gate-present audit method:* Confirm the gate step appears between TABLE E and TABLE F.
    Confirm three per-category Y/N verdicts are present — one for Burst, one for Cascade,
    one for RetryAfter. Confirm PROCEED or BLOCKED decision is stated before TABLE F opens.
  - *Gate-absent signature:* TABLE F opens immediately after TABLE E with no intervening
    gate step. Type completeness is verifiable only by scanning TABLE E after TABLE F is
    complete — a post-hoc scan task, not a construction-time blocking condition.

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
fails this column's precision requirement.

PROHIBITED: adding rows to TABLE E after TABLE F has opened. — *prevents retroactive
risk injection; a risk discovered during mitigation planning is evidence TABLE E was
incomplete — return to TABLE E, complete it, re-run the TYPE SCAN GATE, then re-open
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

---

---

## V-02 — Single Axis: Inertia Framing (C-29 minimal — two-field labeled annotation, no example)

**Axis:** Section B carries a labeled two-field inertia annotation in the C-18/C-26
structural form: "Failure mode prevented" and "Gap above C-25" as named fields. The
annotation names the implicit-complement inference and explains the gap above C-25 using
the same labeled-field structure as the TYPE SCAN GATE purpose annotation. No concrete
unregistered-element example is included — the annotation identifies the class of failure
without naming a specific element type. All other elements carry from V-01, including
the R10 V-05 general-language audit paths in the TYPE SCAN GATE.

**Hypothesis:** Two labeled fields satisfy C-29's minimum pass condition. C-29 requires
the annotation to apply C-18/C-26 framing and name the implicit-complement inference the
closure forecloses. A two-field annotation that names the failure mode (implicit-complement
classification) and the gap above the prior criterion (C-25 requires enumeration but not
closure) satisfies both requirements without the concrete example C-30 independently
requires. The delta from V-01 is exactly one structural transformation: prose paragraph
to labeled fields. The compliance question is whether the form change alone satisfies
C-29 when the content was already present.

**v11 predicted scoring:** C-29 PASS (labeled "Failure mode prevented" and "Gap above
C-25" fields present; names the implicit-complement inference). C-30 FAIL (C-29 annotation
does not include a concrete unregistered-element example). C-31 FAIL (general audit
paths carry from V-01). C-32 PASS. Composite: 200/210.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput
across the rate-limited system described in the signal. Treat the stated request volume
as 1x nominal; also analyze at 2x and 5x.

Tables are the primary output. Fill every cell. Produce sections in the order shown.

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

**Inertia annotation for C-27 — why the register must be declared closed (C-29):**

- **Failure mode prevented:** Implicit-complement classification — an executor reasoning
  that the complement of Section A's prose-permitted list is implicitly structured output.
  Under an open register, an executor encountering an unlisted element type has no
  classification decision to make: the type is not prose (Section A does not permit it),
  therefore it must be structured output and exempt from C-23 requirements. Classification
  is by content inference rather than register membership. This is the content-inspection
  problem C-25 was designed to eliminate.
- **Gap above C-25:** C-25 requires the register to enumerate element types with explicit
  Prose? and C-23-tag classifications. C-25 compliance does not require the register to
  declare itself closed. An open register that satisfies C-25 leaves every unlisted element
  type in implicit-complement territory: the four-row enumeration is present and correct,
  but a fifth element type encountered by an executor is classifiable by inference alone.
  The closure declaration converts the implicit inference into an explicit gap: an unlisted
  element type is not exempt by implication — it is unclassified, and its unclassified
  status is auditable. Adding a new type requires a revision to this contract.

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
- `Limit` — number + unit. Compliance failure condition: vague label fails precision.
- `STATUS Nx` — OK / HIT / SAT. Must shift between at least two bands.
- `Binding?` — exactly one Y. Compliance failure condition: multiple Y entries or no Y
  fails the at-most-one binding constraint.
- `Failure mode` — hard rejection / queue saturation / silent drop / degraded throughput /
  timeout. At least two distinct values across rows.

PROHIBITED: introducing a new T-NN in any Phase 2 section. — *prevents scope creep;
tier discovery during claims analysis indicates Phase 1 enumeration was incomplete*

**[prose: item 1 — binding-tier causal reason]** State why the Binding? = Y tier fails
before all others under 1x nominal load. Name the specific causal mechanism.

**[prose: item 2 — binding constraint exclusivity]** For at least one Binding? = N tier,
name the mechanism that prevents it from binding before the primary tier.

---

**PHASE 2 — CLAIMS PHASE**

PROHIBITED: opening Phase 2 before Phase 1B is complete. — *prevents late evidence
injection; claims built on an incomplete tier inventory produce unverifiable findings*

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
  detectable only by full table scan after TABLE F is complete; the entire category has
  no mitigations but TABLE F appears complete.
- **Gap above C-22:** C-22 ensures the Type column and per-type minimums are present in
  the finished TABLE E. This gate ensures type completeness is verified before TABLE F
  opens. C-22 defines what the finished output must contain; this gate makes an incomplete
  TABLE E a construction-time block rather than a post-hoc finding.
- **Audit test (C-28):**
  - *Gate-present audit method:* Confirm the gate step appears between TABLE E and TABLE F.
    Confirm three per-category Y/N verdicts are present — one for Burst, one for Cascade,
    one for RetryAfter. Confirm PROCEED or BLOCKED decision is stated before TABLE F opens.
  - *Gate-absent signature:* TABLE F opens immediately after TABLE E with no intervening
    gate step. Type completeness is verifiable only by scanning TABLE E after TABLE F is
    complete — construction-time blocking is absent.

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

Compliance failure condition: category of action in `Setting or API parameter` fails
precision requirement.

PROHIBITED: adding rows to TABLE E after TABLE F has opened. — *prevents retroactive
risk injection*

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

---

---

## V-03 — Single Axis: Lifecycle Emphasis (C-31 named-observable audit paths)

**Axis:** The TYPE SCAN GATE audit test is restructured so each path names specific
observables by artifact identifier and structural position. Gate-present method: names
the "TYPE SCAN GATE" section header as the artifact identifier, anchors it to the
structural position between TABLE E's last R-NN row and TABLE F's MR-01 row, and lists
five named observables to confirm. Gate-absent signature: names the structural position
between R-NN and MR-01 and defines the named observable for the absent condition (no
per-category Y/N verdict lines in that gap). Section B carries the R10 V-05 prose inertia
annotation unchanged — C-29 and C-30 remain open.

**Hypothesis:** Artifact-identifier anchoring satisfies C-31 independently of the inertia
framing change. The audit paths' compliance failure is that they direct general scans
("scan for a named gate step") rather than identifying specific artifacts at specific
positions. Replacing general scan instructions with artifact identifiers (the "TYPE SCAN
GATE" section header, the R-NN anchor for TABLE E's last row, the MR-01 anchor for
TABLE F's first row) and named observables (the three per-category Y/N verdict lines with
their exact form) gives an auditor five discrete confirmation targets. The compliance
verdict for C-31 should be identical between V-03 and V-04; V-03 isolates the C-31
change from the C-29/C-30 inertia framing change.

**v11 predicted scoring:** C-29 FAIL (prose inertia annotation carries from V-01). C-30
FAIL (same). C-31 PASS (artifact-identifier anchoring: section header, R-NN anchor,
MR-01 anchor, five named observables). C-32 PASS. Composite: 200/210.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput
across the rate-limited system described in the signal. Treat the stated request volume
as 1x nominal; also analyze at 2x and 5x.

Tables are the primary output. Fill every cell. Produce sections in the order shown.

---

**OUTPUT FORMAT CONTRACT**

**Section A — PROSE-PERMITTED CONTEXTS (C-20)**

Prose is permitted in exactly three contexts:

1. **Binding-tier causal reason** — one paragraph at Phase 1B exit. Authorized by C-01.
2. **Binding constraint exclusivity statement** — one sentence at Phase 1B exit. Authorized
   by C-14.
3. **Global criterion-coverage verdict notes** — FAIL verdicts only. Authorized by C-19.

Any prose passage outside these three contexts is a format violation detectable without
content review.

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

**Inertia annotation for C-27 — why the register must be declared closed (C-27):**
The temptation is to leave the register open, reasoning that non-prose is the complement
of the prose-permitted list in Section A — anything not enumerated there is implicitly
structured output. This reasoning reintroduces the content-inspection problem that C-25
was designed to eliminate: an executor encountering an element type not in the register
(e.g., a compound gate variant, a load-shape verdict label, a phase-entry condition
banner) must classify it by interpreting whether its content constitutes an affirmative
statement, a blocking condition, or a narrative element. The closure declaration
forecloses content inspection: an unlisted type is explicitly unclassified, not
implicitly exempt. Its unclassified status is a detectable gap — not an implicit
permission — and adding a new type requires an explicit revision to this contract.

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
injection*

**Step 1B — TIER INVENTORY**

**TABLE A — THROTTLE TIER INVENTORY ACROSS VOLUME BANDS**

*(One row per rate-limiting component. Source-ID from register required. Every cell filled.)*

| Tier-ID | Component | Limit (number + unit) | Source-ID | Scope | STATUS 1x | STATUS 2x | STATUS 5x | Binding? | Failure mode |
|---------|-----------|----------------------|-----------|-------|-----------|-----------|-----------|----------|-------------|
| T-01 | | | | | | | | | |
| T-02 | | | | | | | | | |
| ... | | | | | | | | | |

Column notes:
- `Tier-ID` — T-01, T-02, ... verbatim downstream. Informal synonym fails T-NN threading.
- `Limit` — number + unit. Vague label fails precision.
- `STATUS Nx` — OK / HIT / SAT. Must shift across at least two bands.
- `Binding?` — exactly one Y. Multiple Y or no Y fails constraint. Designation without
  causal reason is an assertion, not an argument.
- `Failure mode` — hard rejection / queue saturation / silent drop / degraded throughput /
  timeout. At least two distinct values.

PROHIBITED: introducing a new T-NN in any Phase 2 section. — *prevents scope creep*

**[prose: item 1 — binding-tier causal reason]** State why the Binding? = Y tier fails
before all others at 1x nominal. Name the specific causal mechanism.

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
timeout-cascade. Generic term fails precision.

**TABLE C — USER EXPERIENCE CATALOG**

*(Source: TABLE A. One row per TABLE A Tier-ID. No tier may be omitted.)*

| Tier-ID | Error code or signal | Retry-After present? (Y/N) | Retry-After surfaced to caller? (Y/N) | Visible in run history? (Y/N/SILENT) | Failure if Retry-After ignored |
|---------|---------------------|---------------------------|--------------------------------------|--------------------------------------|-------------------------------|
| T-01 | | | | | |
| T-02 | | | | | |

Plain description in `Error code or signal` fails precision.

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

Risk list without Type column with named taxonomy fails C-22 even if all categories
happen to appear.

---

**TYPE SCAN GATE**

**Purpose annotation (C-26) — three fields:**

- **Failure mode prevented:** Category elision — a risk type absent from TABLE E is
  detectable only by full table scan after TABLE F is complete; both artifacts require
  revision but TABLE F appears complete.
- **Gap above C-22:** C-22 defines what the finished output must contain. This gate makes
  an incomplete TABLE E a construction-time blocking condition before TABLE F opens.
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
    (5) The TABLE F section header and its first data row (MR-01) appear after the gate
    decision line. Structural position: MR-01 is not the first row after TABLE E's R-NN.
    All five observables confirmed = gate compliance verified by artifact-ID scan.
  - *Gate-absent signature:* The structural position between TABLE E's last R-NN row and
    TABLE F's first data row (MR-01) contains no **TYPE SCAN GATE** section header.
    Named observable for the absent condition: no verdict lines of the form
    `[Category]: [Y / N]` (where Category is Burst, Cascade, or RetryAfter) appear in
    the gap between R-NN and MR-01. The distinguishing observable: gate-present outputs
    have three named Y/N verdict lines before MR-01; gate-absent outputs have none.

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

- C-01 (Primary bottleneck with causal reason): [PASS / FAIL]
- C-02 (Backpressure propagation ≥2 hops with mechanism): [PASS / FAIL]
- C-03 (≥2 tiers with enforcing component and scope): [PASS / FAIL]
- C-04 (UX at each throttle tier): [PASS / FAIL]
- C-05 (Unprotected burst path): [PASS / FAIL]

[prose: item 3 — global criterion-coverage verdict notes] State FAIL rationale for any
criterion above that did not pass.

---

---

## V-04 — Combined: Inertia Framing + Lifecycle Emphasis (C-29 + C-30 + C-31)

**Axes:** (1) Inertia framing — Section B inertia annotation restructured as a three-field
labeled block (Failure mode prevented / Gap above C-25 / Concrete example) matching
C-18/C-26 structural form. The concrete example names a specific element type not in the
register and states the ambiguity it would create, making the claim independently testable.
(2) Lifecycle emphasis — TYPE SCAN GATE audit test upgraded to name specific observables
by artifact identifier and structural position. The delta from V-03 is Section B only;
the delta from V-02 is the TYPE SCAN GATE only; V-04 is the first variation where both
axes are simultaneously changed.

**Hypothesis:** C-29, C-30, and C-31 are orthogonal requirements that can be satisfied
independently within the same structural region. The three-field inertia annotation
satisfies C-29 (labeled-field form) and C-30 (concrete example with stated ambiguity)
without affecting the TYPE SCAN GATE. The artifact-identifier audit paths satisfy C-31
without affecting Section B. V-04 tests whether combining the two single-axis changes
produces a 210/210 composite, confirming orthogonality.

**v11 predicted scoring:** C-29 PASS (three-field labeled annotation with "Failure mode
prevented" and "Gap above C-25" fields). C-30 PASS (C-29 annotation's third field names
a load-shape verdict label and states its classification ambiguity under an open register).
C-31 PASS (five named observables with artifact identifiers and structural position anchors).
C-32 PASS. Composite: 210/210.

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

1. **Binding-tier causal reason** — one paragraph at Phase 1B exit. Scope: why the
   Binding? = Y tier fails before all others under 1x nominal load. Authorized by C-01.
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
  Under an open register, an unlisted element type is classified without register lookup:
  the executor infers "not prose-permitted (Section A does not authorize it), therefore
  structured output, therefore exempt from C-23 requirements." Classification is by
  content inference rather than by registered type membership. This is the content-
  inspection problem C-25 was designed to eliminate: element types are classified by
  interpreting what they say rather than by identifying what they are.
- **Gap above C-25:** C-25 requires the register to enumerate element types with explicit
  Prose? and C-23-tag classifications. C-25 compliance does not require the register to
  declare itself exhaustive. An open register that satisfies C-25 leaves every element
  type outside the four-row table in implicit-complement territory: the enumeration is
  correct and complete for the listed types, but a fifth element type encountered by an
  executor is classifiable only by inference. The closure declaration converts implicit-
  exempt to explicitly-unclassified: the registered set is declared exhaustive, and an
  unlisted type's classification status is a detectable contract gap, not an inferred
  permission. Adding a new type requires an explicit revision auditable by change history.
- **Concrete example (C-30):** A load-shape verdict label — e.g., a line reading
  "FLAT-LOAD: within nominal band" — does not match any of the four registered canonical
  forms. An executor must determine: is this a gate decision line (canonical form:
  PROCEED / BLOCKED — no match), a cross-artifact header ("One row per [source]..." —
  no match), a phase boundary prohibition ("PROHIBITED: [data] — [failure mode]" — no
  match), or a per-criterion verdict ("C-NN: PASS / FAIL" — no match)? Under an open
  register, the implicit-complement inference is available: this element is not in
  Section A's prose-permitted list, therefore it is implicitly structured output. Under
  a closed register, the inference is foreclosed: the element type is unregistered,
  therefore its Prose? and C-23-tag status is explicitly unresolved. The classification
  ambiguity is named and requires contract revision to resolve — it cannot be resolved
  by content inspection alone.

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
- `Tier-ID` — T-01, T-02, ... Use verbatim in every downstream table. Informal synonym
  fails T-NN threading; cross-section tracing becomes a name-resolution task.
- `Limit` — specific number with unit. Vague label ("limited", "throttled") fails precision.
- `STATUS Nx` — OK / HIT / SAT. Must shift between at least two bands.
- `Binding?` — exactly one Y. Multiple Y or no Y fails the at-most-one binding constraint.
  Designation without causal reason is an assertion, not an argument.
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
downstream content. — *prevents coverage elision*

**TABLE B — BACKPRESSURE PROPAGATION TRACE**

*(Source: TABLE A. Two hops minimum. T-NNs must reference TABLE A entries.)*

| Hop | From (Tier-ID) | To component | Mechanism | Observable effect |
|-----|----------------|--------------|-----------|-------------------|
| 1 | | | | |
| 2 | | | | |
| ... | | | | |

Mechanism values: queue-fill, connection-hold, retry-amplification, dependency-stall,
timeout-cascade. Generic term ("blocked", "throttled") fails precision requirement.

**TABLE C — USER EXPERIENCE CATALOG**

*(Source: TABLE A. One row per TABLE A Tier-ID. No tier may be omitted.)*

| Tier-ID | Error code or signal | Retry-After present? (Y/N) | Retry-After surfaced to caller? (Y/N) | Visible in run history? (Y/N/SILENT) | Failure if Retry-After ignored |
|---------|---------------------|---------------------------|--------------------------------------|--------------------------------------|-------------------------------|
| T-01 | | | | | |
| T-02 | | | | | |

Plain description in `Error code or signal` fails precision.

**TABLE D — UNPROTECTED BURST PATHS**

*(Source: TABLE A. At least one row. If no gap: ≥2 named controls as evidence.)*

| Path-ID | Entry component | Tier-IDs involved | Gap reason or named controls | Consequence at burst volume |
|---------|----------------|-------------------|-----------------------------|-----------------------------|
| P-01 | | | | |

**TABLE E — RISK TAXONOMY**

*(Source: TABLE A + TABLE B + TABLE D. Per-type minimum: ≥1 Burst, ≥1 Cascade,
≥1 RetryAfter. Type column required — a count requirement without type classification
can be satisfied by two rows of the same category, leaving an entire category undetected.)*

| Risk-ID | Tier-ID | Type | Risk description | Severity (H/M/L) |
|---------|---------|------|-----------------|-----------------|
| R-01 | | Burst | | |
| R-02 | | Cascade | | |
| R-03 | | RetryAfter | | |

Risk list without Type column with named taxonomy and per-type minimum-row constraint
fails C-22 even if all categories happen to appear.

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
    Y/N verdict lines before MR-01; gate-absent outputs have none. This is the
    distinguishing observable between the two conditions.

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

Compliance failure condition: category of action in `Setting or API parameter` fails
precision. A row naming a category cannot be applied without further research; a row
naming an exact parameter (e.g., `connector.retryPolicy`) can be applied immediately.

PROHIBITED: adding rows to TABLE E after TABLE F has opened. — *prevents retroactive
risk injection; a risk discovered during mitigation planning requires returning to
TABLE E, completing it, re-running the TYPE SCAN GATE, then re-opening TABLE F*

---

**GLOBAL CRITERION-COVERAGE STEP**

Named dedicated step. Not embedded prose. Maps output content to essential criterion
categories. Reports per-criterion PASS/FAIL.

- C-01 (Primary bottleneck with causal reason): [binding-tier causal reason present and
  names specific causal mechanism? PASS / FAIL]
- C-02 (Backpressure propagation ≥2 hops with mechanism): [TABLE B has ≥2 rows with
  T-NN identifiers and specific mechanisms from the permitted set? PASS / FAIL]
- C-03 (≥2 tiers with enforcing component and scope): [TABLE A has ≥2 rows with Component
  and Scope filled, each with specific numeric Limit? PASS / FAIL]
- C-04 (UX at each throttle tier): [TABLE C has one row per TABLE A Tier-ID, no tier
  omitted? PASS / FAIL]
- C-05 (Unprotected burst path): [TABLE D has ≥1 row with gap reason, or ≥1 row with
  ≥2 named controls? PASS / FAIL]

[prose: item 3 — global criterion-coverage verdict notes] State FAIL rationale for any
criterion above that did not pass.

---

---

## V-05 — Combined: Role Sequence + Inertia Framing + Lifecycle Emphasis (all axes)

**Axes:** (1) Role sequence — three-role pipeline: Format Analyst produces the complete
OUTPUT FORMAT CONTRACT including the three-field labeled Section B inertia annotation;
Domain Expert produces evidence and claims through TABLE E; Consequence Analyst activates
only after the TYPE SCAN GATE is cleared and produces TABLE F and the global coverage
step. Each role's exit condition is a structural precondition for the next role's
activation. (2) Inertia framing for C-29/C-30 — Section B carries the three-field labeled
annotation (Failure mode prevented / Gap above C-25 / Concrete example) as a Format
Analyst output, making the annotation a role obligation rather than an inline declaration.
(3) Lifecycle emphasis for C-31 — Consequence Analyst's TYPE SCAN GATE annotation carries
the artifact-identifier audit paths with named observables and structural position anchors.

**Hypothesis:** The three-role pipeline provides architectural enforcement that V-04's
single-role instructions cannot: Role 1's exit condition ("FORMAT CONTRACT COMPLETE") is
the structural precondition for Role 2's activation, ensuring the register is both
populated and declared closed before the Domain Expert can encounter an element type
classification question. The Format Analyst's production of the three-field inertia
annotation makes it a role deliverable rather than an inline note — the annotation's
presence is verifiable against the Format Analyst's output, not against the executor's
willingness to include it. The Consequence Analyst's C-31-compliant audit paths provide
independent verification of the TYPE SCAN GATE at the role boundary, not embedded in
mid-phase instructions.

**v11 predicted scoring:** C-29 PASS (Format Analyst role produces the three-field labeled
annotation as a required deliverable; "Failure mode prevented" and "Gap above C-25" fields
present). C-30 PASS (third field of C-29 annotation names load-shape verdict label as
unregistered type and states the classification ambiguity). C-31 PASS (Consequence Analyst
TYPE SCAN GATE carries five named observables with artifact-ID and structural-position
anchors). C-32 PASS (escape-route demolisher present in Consequence Analyst output). All
essential and recommended criteria carry from R10 V-05 baseline. Composite: 210/210.

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
    line; MR-01 is not the first row after TABLE E's last R-NN row.
    All five observables confirmed by artifact-ID scan = gate compliance verified.
  - *Gate-absent signature:* The structural position between TABLE E's last R-NN row and
    TABLE F's first data row (MR-01) contains no **TYPE SCAN GATE** section header.
    Named observable for the absent condition: no verdict lines of the form
    `[Category]: [Y / N]` (where Category is one of Burst, Cascade, RetryAfter) appear
    in the structural gap between R-NN and MR-01. Gate-present outputs have three named
    Y/N verdict lines before MR-01; gate-absent outputs have none. This is the
    distinguishing observable between the two structural conditions.

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
