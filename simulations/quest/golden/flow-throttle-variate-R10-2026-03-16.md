# flow-throttle Variate — Round 10

**Date:** 2026-03-16
**Rubric:** v10 (C-01 through C-28, N_essential=5, N_recommended=3, N_aspirational=20)
**Max composite:** 190 | **Baseline ceiling:** R9 V-05 (confirmed passes C-01 through C-26 under v9)

---

## State Analysis: What R9 V-05 Has vs. What R10 Must Add

**R9 V-05 coverage under v10 (confirmed):**
- C-01 through C-24: all pass (verified through R9)
- C-25: passes — STRUCTURED OUTPUT REGISTER as Section B of OUTPUT FORMAT CONTRACT;
  four-row table (Element type / Canonical form / Prose? / C-23 tag required?); gate
  decision lines, cross-artifact header lines, phase boundary prohibition lines, and
  per-criterion verdict lines all classified No/No. Escape-route framing present.
- C-26: passes — TYPE SCAN GATE carries three-field annotation: Failure mode prevented,
  Gap above C-22, Audit test with gate-present and gate-absent instructions.

**C-27 gap in R9 V-05:**
R9 V-05's STRUCTURED OUTPUT REGISTER satisfies C-25: four named element types,
explicit No/No classification, escape-route explanation. The register does not carry a
closure declaration. An executor encountering a new element type — a compound gate
variant, a phase-entry condition banner, a load-shape verdict label — must classify it
by content inspection. The register is open: unlisted types are not unambiguously
unclassified; they are merely unregistered. C-27 requires the register to declare
itself a formally closed set so that any unregistered type is explicitly unclassified,
not implicitly exempt. R9 V-03 added the closure: "No other element types are added to
this register without revising this contract." R9 V-05 included the four-column table
form but did not include the closure declaration, leaving C-27 open.

**C-28 status in R9 V-05:**
R9 V-05's TYPE SCAN GATE annotation carries "Audit test:" as its third labeled field:
"Gate present → verify PROCEED/BLOCKED verdict appears between TABLE E and TABLE F,
and all three type-presence verdicts are explicitly stated. Gate absent → verify type
completeness by scanning TABLE E after TABLE F is complete." This satisfies C-28's
pass condition (named audit test element with compliance-path instruction and gate-absent
failure signature). C-28 passes in R9 V-05.

**C-28 gap in R9 V-01 through V-04:**
R9 V-01, V-02, and V-04 carried C-26 annotations without a named Audit test element.
They named the failure mode and described the gap above C-22 but did not provide
actionable verification instructions for either the compliance path or the absence
signature. Only V-03 and V-05 satisfied C-28. R10 must test C-28 presentation forms
explicitly, including a clean FAIL isolation.

---

## Round 10 Variation Map

| Variation | Axes | C-27 | C-28 | Predicted composite |
|-----------|------|------|------|---------------------|
| V-01 | Output format: C-27 FAIL isolation (no closure declaration) | FAIL | PASS | 185/190 |
| V-02 | Output format: C-27 minimal inline closure | PASS | PASS | 190/190 |
| V-03 | Lifecycle emphasis: C-28 two-path labeled audit test | PASS | PASS | 190/190 |
| V-04 | Role sequence + inertia framing: C-27 closure via Format Analyst role | PASS | PASS | 190/190 |
| V-05 | All three axes: role sequence + C-27 inertia annotation + C-28 comprehensive | PASS | PASS | 190/190 |

**Single-axis questions:**

Q1 (V-01 vs V-02): Is C-27 the only delta between an open register (V-01) and a minimal
closed register (V-02)? Hypothesis: yes — a single closing sentence satisfies C-27's
pass condition without affecting C-25, and all other criteria are unaffected by the
addition of one sentence to Section B.

Q2 (V-02 vs V-03): Does expanding the C-28 audit test from an inline trailing statement
to a named two-path labeled block improve compliance reliability? Hypothesis: both
forms satisfy C-28 (both carry compliance-path instruction and gate-absent signature);
the labeled form is more auditable because each path is independently scannable. The
compliance verdict should be identical; the question is output quality.

Q3 (V-04 vs V-05): Does adding lifecycle emphasis (expanded C-28 labeled audit test)
on top of role-sequence change produce incremental gains? Hypothesis: the role-sequence
change dominates C-27 compliance; the lifecycle expansion dominates C-28 output quality.
V-05 is the strongest candidate for 190/190 because it addresses both criteria from
independent structural angles.

---

## V-01 — Single Axis: Output Format (C-27 FAIL — no closure declaration)

**Axis:** The STRUCTURED OUTPUT REGISTER in Section B names four element types as
exempt from C-23 tagging (satisfying C-25) but does not include a closure declaration.
The register is an open enumeration: an executor encountering an unregistered element
type must classify it by content inspection rather than by register membership. All
other elements carry from the R9 V-05 baseline, including the C-28 Audit test in the
TYPE SCAN GATE annotation.

**Hypothesis:** V-01 is the clean C-27 isolation failure. The register is present and
element types are named and classified; the open/closed status of the register is the
only delta. An executor reading Section B sees four named types but has no statement
that the set is exhaustive — encountering a fifth type requires content inspection. All
other criteria pass at the R9 V-05 level. The Audit test (C-28) is fully present in the
TYPE SCAN GATE annotation.

**v10 predicted scoring:** C-27 FAIL (no closure declaration; register is open, unregistered
types are implicitly unclassified rather than explicitly unresolved). C-28 PASS (Audit test
present with compliance path and gate-absent signature). All other aspirationals pass.
Composite: 185/190.

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
3. **Global criterion-coverage verdict notes** — FAIL verdicts only, at the global
   coverage step. Authorized by C-19.

Any prose passage outside these three contexts is a format violation detectable without
content review.

**Section B — STRUCTURED OUTPUT REGISTER (C-25)**

The following element types are structured output. They are NOT prose. They are exempt
from C-23 inline citation requirements. Classification is by element type, not by content.

| Element type | Canonical form | Prose? | C-23 tag required? |
|-------------|---------------|--------|-------------------|
| Gate decision lines | PROCEED / BLOCKED | No | No |
| Cross-artifact header lines | "One row per [source]. No [item] may be omitted." | No | No |
| Phase boundary prohibition lines | "PROHIBITED: [data class] — [failure mode]" | No | No |
| Per-criterion verdict lines | "C-NN: PASS / FAIL" | No | No |

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
- `STATUS Nx` — OK / HIT / SAT. Must shift between at least two bands.
- `Binding?` — exactly one Y. Compliance failure condition: multiple Y entries or no Y
  entry fails the at-most-one binding constraint; a designation without causal reason
  is an assertion, not an argument.
- `Failure mode` — hard rejection / queue saturation / silent drop / degraded throughput /
  timeout. At least two distinct values across rows.

PROHIBITED: introducing a new T-NN in any Phase 2 section. — *prevents scope creep;
tier discovery during claims analysis indicates Phase 1 enumeration was incomplete and
is not a fill-in opportunity*

**[prose: item 1 — binding-tier causal reason]** State why the Binding? = Y tier fails
before all others under 1x nominal load. Name the specific causal mechanism.

**[prose: item 2 — binding constraint exclusivity]** For at least one Binding? = N tier,
name the mechanism that prevents it from binding before the primary tier.

---

**PHASE 2 — CLAIMS PHASE**

PROHIBITED: opening Phase 2 before Phase 1B is complete. — *prevents late evidence
injection; claims built on an incomplete tier inventory are unverifiable against C-11*

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

*(Source: TABLE A + TABLE B + TABLE D. Per-type minimum: ≥1 Burst, ≥1 Cascade, ≥1
RetryAfter. Type column required — a count-only list can be satisfied by two rows of
the same category, leaving an entire category undetected.)*

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

**Purpose — prevents category elision above C-22 (C-26):** C-22 ensures the Type column
is present and all three categories appear in the finished TABLE E. This gate ensures
type completeness is verified before TABLE F opens. Without this gate, an executor can
complete TABLE F (all TABLE E rows have mitigation entries) and discover a missing
Cascade row afterward — at which point TABLE F also has no Cascade mitigations. The
gate makes a missing category a blocking condition before TABLE F opens.

**Escape route for C-26 — "C-22 makes this gate redundant":** This reasoning conflates
the structural requirement (C-22 ensures the finished output is correctly typed) with
the construction-time enforcement mechanism (the gate ensures completeness before
downstream work proceeds). An output that satisfies C-22 by inspection may have been
produced through an execution path where TABLE F was completed before the type gap was
detected. The gate forecloses that path.

**Audit test (C-28):** Gate present — verify PROCEED/BLOCKED verdict appears between
TABLE E and TABLE F and all three type-presence verdicts are explicitly stated. Gate
absent — verify type completeness by scanning TABLE E after TABLE F is complete; the
gate is the only mechanism that makes type completeness a construction-time blocking
condition rather than a post-hoc scan result.

Scan TABLE E:
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
fails this column's precision requirement. A row naming a category cannot be applied
without further research; a row naming an exact parameter can be applied immediately.

PROHIBITED: adding rows to TABLE E after TABLE F has opened. — *prevents retroactive
risk injection; a risk discovered during mitigation planning indicates TABLE E was
incomplete and requires returning to the risk phase*

---

**GLOBAL CRITERION-COVERAGE STEP**

Named dedicated step. Not embedded prose. Maps output content to essential criterion
categories by name. Reports per-criterion PASS/FAIL.

- C-01 (Primary bottleneck with causal reason): [binding-tier causal reason present and
  names specific causal mechanism? PASS / FAIL]
- C-02 (Backpressure propagation ≥2 hops with mechanism): [TABLE B has ≥2 rows with T-NN
  identifiers and specific mechanisms from the permitted set? PASS / FAIL]
- C-03 (≥2 tiers with enforcing component and scope): [TABLE A has ≥2 rows with Component
  and Scope filled, each with a specific numeric Limit? PASS / FAIL]
- C-04 (UX at each throttle tier): [TABLE C has one row per TABLE A Tier-ID, no tier
  omitted? PASS / FAIL]
- C-05 (Unprotected burst path): [TABLE D has ≥1 row with gap reason, or ≥1 row with ≥2
  named controls? PASS / FAIL]

[prose: item 3 — global criterion-coverage verdict notes] State FAIL rationale for any
criterion above that did not pass.

---

---

## V-02 — Single Axis: Output Format (C-27 minimal inline closure)

**Axis:** The STRUCTURED OUTPUT REGISTER in Section B is identical to V-01 except for
one closing sentence appended after the table: "No other element types are added to this
register without revising this contract." This converts the open enumeration into a
formally closed set. An executor encountering an unregistered element type can no longer
treat it as implicitly exempt — the closure statement makes its classification status
explicitly unresolved. All other elements carry unchanged from V-01.

**Hypothesis:** A single closing sentence is sufficient to satisfy C-27's pass condition.
C-27 requires a closure declaration "within or immediately following the C-25 exemption
clause, stating that the register is exhaustive and that additions require explicit
contract revision." A sentence that states exactly that, placed immediately after the
exemption table, satisfies the form requirement without requiring structural expansion.
The minimal form tests whether the criterion is a presence check or a quality check.

**v10 predicted scoring:** C-27 PASS (closure declaration present and states exhaustiveness
and revision requirement). C-28 PASS (Audit test carries from V-01). All other criteria
pass. Composite: 190/190.

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
3. **Global criterion-coverage verdict notes** — FAIL verdicts only, at the global
   coverage step. Authorized by C-19.

Any prose passage outside these three contexts is a format violation detectable without
content review.

**Section B — STRUCTURED OUTPUT REGISTER (C-25, C-27)**

The following element types are structured output. They are NOT prose. They are exempt
from C-23 inline citation requirements. Classification is by element type, not by content.

| Element type | Canonical form | Prose? | C-23 tag required? |
|-------------|---------------|--------|-------------------|
| Gate decision lines | PROCEED / BLOCKED | No | No |
| Cross-artifact header lines | "One row per [source]. No [item] may be omitted." | No | No |
| Phase boundary prohibition lines | "PROHIBITED: [data class] — [failure mode]" | No | No |
| Per-criterion verdict lines | "C-NN: PASS / FAIL" | No | No |

No other element types are added to this register without revising this contract.

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
injection; a source entered after claims are built cannot be verified as a prior
commitment*

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
  failure condition: informal synonym fails the tier-ID threading requirement.
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
injection; claims built on an incomplete tier inventory are unverifiable*

**For each tier in TABLE A (C-17):** every downstream derived table must include a row
for every T-NN. Coverage is verifiable by T-NN count match against TABLE A, not by
reading downstream content. — *prevents coverage elision*

**TABLE B — BACKPRESSURE PROPAGATION TRACE**

*(Source: TABLE A. Two hops minimum. T-NNs must reference TABLE A entries.)*

| Hop | From (Tier-ID) | To component | Mechanism | Observable effect |
|-----|----------------|--------------|-----------|-------------------|
| 1 | | | | |
| 2 | | | | |
| ... | | | | |

Mechanism values: queue-fill, connection-hold, retry-amplification, dependency-stall,
timeout-cascade. Compliance failure condition: generic term fails precision requirement.

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

**Purpose — prevents category elision above C-22 (C-26):** C-22 ensures the Type column
is present and all three categories appear in the finished TABLE E. This gate ensures
type completeness is verified before TABLE F opens. Without this gate, an executor can
complete TABLE F and discover a missing Cascade row afterward — at which point TABLE F
also has no Cascade mitigations. The gate makes a missing category a blocking condition.

**Escape route for C-26 — "C-22 makes this gate redundant":** C-22 ensures the finished
output has the correct type structure; this gate ensures the structure is correct before
downstream construction begins. An output that satisfies C-22 by inspection may have
been produced through a path where TABLE F was completed before the type gap was
detected. The gate forecloses that path.

**Audit test (C-28):** Gate present — verify PROCEED/BLOCKED verdict appears between
TABLE E and TABLE F and all three type-presence verdicts are explicitly stated. Gate
absent — verify type completeness by scanning TABLE E after TABLE F is complete; the
gate is the only mechanism that makes type completeness a construction-time blocking
condition rather than a post-hoc scan result.

Scan TABLE E:
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
precision requirement. A row naming a category cannot be applied without further
research; a row naming an exact parameter can be applied immediately.

PROHIBITED: adding rows to TABLE E after TABLE F has opened. — *prevents retroactive
risk injection*

---

**GLOBAL CRITERION-COVERAGE STEP**

Named dedicated step. Not embedded prose. Maps output content to essential criterion
categories by name. Reports per-criterion PASS/FAIL.

- C-01 (Primary bottleneck with causal reason): [PASS / FAIL]
- C-02 (Backpressure propagation ≥2 hops with mechanism): [PASS / FAIL]
- C-03 (≥2 tiers with enforcing component and scope): [PASS / FAIL]
- C-04 (UX at each throttle tier): [PASS / FAIL]
- C-05 (Unprotected burst path): [PASS / FAIL]

[prose: item 3 — global criterion-coverage verdict notes] State FAIL rationale for any
criterion above that did not pass.

---

---

## V-03 — Single Axis: Lifecycle Emphasis (C-28 two-path labeled audit test)

**Axis:** The TYPE SCAN GATE annotation block is structurally expanded. C-28's Audit
test element is split into two labeled sub-instructions — "Gate-present audit method"
and "Gate-absent signature" — each with a named observable and the specific mechanism
it confirms. C-27 is present (closure declaration from V-02 carried). The single-axis
change from V-02 is the structural expansion of the Audit test from an inline trailing
statement into a named two-path verification block.

**Hypothesis:** The labeled two-path form is more auditable than the inline trailing
form. V-02's Audit test reads as a single sentence with two clauses: an executor must
parse the two paths from a compound statement. V-03's labeled sub-fields make each
path independently scannable: an auditor verifying C-28 compliance can confirm both
paths are present without parsing compound sentences. The compliance verdict is
identical; the structural form is more reliable under adversarial conditions where
the annotation is skimmed rather than read.

**v10 predicted scoring:** C-27 PASS (closure declaration present). C-28 PASS (two-path
labeled sub-fields, each with named observable). Composite: 190/190.

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

Any prose passage outside these three declared contexts is a format violation detectable
without content review.

**Section B — STRUCTURED OUTPUT REGISTER (C-25, C-27)**

The following element types are structured output, not prose. They are exempt from C-23
inline citation requirements. Classification is by element type — content inspection is
not required and is not the correct classification method.

| Element type | Canonical form | Prose? | C-23 tag required? |
|-------------|---------------|--------|-------------------|
| Gate decision lines | PROCEED / BLOCKED | No | No |
| Cross-artifact header lines | "One row per [source]. No [item] may be omitted." | No | No |
| Phase boundary prohibition lines | "PROHIBITED: [data class] — [failure mode]" | No | No |
| Per-criterion verdict lines | "C-NN: PASS / FAIL" | No | No |

No other element types are added to this register without revising this contract.

---

**PHASE 1 — EVIDENCE PHASE**

**Step 1A — SOURCE REGISTER (C-13)**

Commit the evidence base before naming any tier. A tier with no register entry receives
UNDOCUMENTED in the Limit column; it is not assigned an inferred value.

| Source-ID | Source name | Type | Numeric values it provides |
|-----------|-------------|------|---------------------------|
| S-01 | | | |
| S-02 | | | |

PROHIBITED: adding a new Source-ID after this line. — *prevents retroactive source
injection; sources entered after claims are built cannot be verified as prior commitments*

**Step 1B — TIER INVENTORY**

**TABLE A — THROTTLE TIER INVENTORY ACROSS VOLUME BANDS**

*(One row per rate-limiting component. Source-ID from register required.)*

| Tier-ID | Component | Limit (number + unit) | Source-ID | Scope | STATUS 1x | STATUS 2x | STATUS 5x | Binding? | Failure mode |
|---------|-----------|----------------------|-----------|-------|-----------|-----------|-----------|----------|-------------|
| T-01 | | | | | | | | | |
| T-02 | | | | | | | | | |
| ... | | | | | | | | | |

Column notes:
- `Tier-ID` — T-01, T-02, ... Use verbatim downstream. Compliance failure condition:
  informal synonym fails T-NN threading.
- `Limit` — number + unit. Compliance failure condition: vague label fails precision.
- `STATUS Nx` — OK / HIT / SAT. Must shift across at least two bands.
- `Binding?` — exactly one Y. Compliance failure condition: multiple Y entries or no Y
  fails the at-most-one binding constraint; a designation without causal reason is an
  assertion, not an argument.
- `Failure mode` — hard rejection / queue saturation / silent drop / degraded throughput /
  timeout. At least two distinct values.

PROHIBITED: introducing a new T-NN in any Phase 2 section. — *prevents scope creep;
tier discovery during claims analysis indicates Phase 1 enumeration was incomplete*

**[prose: item 1 — binding-tier causal reason]** State why the Binding? = Y tier fails
before all others at 1x nominal. Name the specific causal mechanism.

**[prose: item 2 — binding constraint exclusivity]** For at least one Binding? = N tier,
name the mechanism that prevents it from binding before the primary tier.

---

**PHASE 2 — CLAIMS PHASE**

PROHIBITED: opening Phase 2 before Phase 1B is complete. — *prevents late evidence
injection; claims built on an incomplete tier inventory produce unverifiable findings*

**For each tier in TABLE A (C-17):** every downstream derived table must include a row
for every T-NN. Coverage verifiable by T-NN count match against TABLE A. — *prevents
coverage elision; a tier absent from a derived table produces a detectable T-NN count gap*

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

- **Failure mode prevented:** Category elision — a risk type (Burst, Cascade, or
  RetryAfter) is absent from TABLE E but detectable only by a full table scan after
  TABLE F is complete, at which point that entire risk category also has no mitigations.
- **Gap above C-22:** C-22 ensures the Type column is present and all three categories
  appear in the *finished* TABLE E. This gate ensures type completeness is verified
  *before TABLE F opens*. C-22 is a finished-output structural requirement; this gate
  is a construction-time blocking check. An executor who reasons "C-22 already requires
  all three types — the gate adds no substance" confuses a structural requirement with an
  enforcement mechanism. C-22 ensures what the output must contain; this gate ensures
  the missing-category failure mode cannot be produced by any valid execution path.
- **Audit test (C-28):**
  - *Gate-present audit method:* Confirm the gate step appears between TABLE E and
    TABLE F. Confirm three per-category Y/N verdicts are present: one for Burst, one
    for Cascade, one for RetryAfter. Confirm PROCEED or BLOCKED decision is stated
    before TABLE F opens.
  - *Gate-absent signature:* TABLE F opens immediately after TABLE E with no intervening
    gate step. Type completeness is verifiable only by scanning TABLE E after TABLE F is
    complete — a post-hoc scan task, not a construction-time blocking condition.

Scan TABLE E:
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

Named dedicated step. Not embedded prose. Maps output content to essential criterion
categories by name. Reports per-criterion PASS/FAIL.

- C-01 (Primary bottleneck with causal reason): [PASS / FAIL]
- C-02 (Backpressure propagation ≥2 hops with mechanism): [PASS / FAIL]
- C-03 (≥2 tiers with enforcing component and scope): [PASS / FAIL]
- C-04 (UX at each throttle tier): [PASS / FAIL]
- C-05 (Unprotected burst path): [PASS / FAIL]

[prose: item 3 — global criterion-coverage verdict notes] State FAIL rationale for any
criterion above that did not pass.

---

---

## V-04 — Combined: Role Sequence + Inertia Framing (C-27 closure via Format Analyst role output)

**Axes:** (1) Role sequence — a Format Analyst role activates before the Domain Expert
and produces the complete OUTPUT FORMAT CONTRACT, including Section B with the closure
declaration. The Domain Expert is bound by this contract and may not modify it. The
Format Analyst making the contract a role output makes the closure declaration a
precondition for Domain Expert activation. (2) Inertia framing — Section B's closure
declaration carries an explicit inertia annotation naming the failure mode that an open
register reintroduces: content-inspection classification for any element type not in the
register, which is the exact problem C-25 was designed to eliminate.

**Hypothesis:** Assigning the STRUCTURED OUTPUT REGISTER (including its closure
declaration) to a Format Analyst role enforces C-27 compliance more reliably than a
single-role format declaration. A role output obligation makes the closure a structural
precondition — the Domain Expert cannot activate before the register is both populated
and declared closed. The inertia annotation for C-27 names the escape route ("the
complement of the prose list is implicitly structured") and demolishes it in place. C-28
carries the labeled two-path form from V-03.

**v10 predicted scoring:** C-27 PASS (Format Analyst role produces the closure as a
required output; inertia annotation names the failure mode prevented). C-28 PASS
(two-path labeled audit test). All other criteria pass. Composite: 190/190.

---

**ROLE 1 — FORMAT ANALYST**

You are the Format Analyst. Your output is the complete OUTPUT FORMAT CONTRACT below.
The Domain Expert (Role 2) is bound by this contract and may not modify it. Produce
the contract by filling every section, then state "FORMAT CONTRACT COMPLETE" before
Role 2 activates.

---

**OUTPUT FORMAT CONTRACT**

**Section A — PROSE-PERMITTED CONTEXTS (C-20)**

Prose is permitted in exactly three contexts. Enumerate each with its scope:

1. **Binding-tier causal reason** — one paragraph at Phase 1B exit. Scope: explains why
   the Binding? = Y tier fails before all others. Authorized by C-01.
2. **Binding constraint exclusivity statement** — one sentence at Phase 1B exit. Scope:
   names the mechanism that prevents at least one non-binding tier from failing first.
   Authorized by C-14.
3. **Global criterion-coverage verdict notes** — FAIL verdicts only, at the global
   coverage step. Scope: one sentence per failed criterion. Authorized by C-19.

Any prose passage outside these three declared scopes is a format violation detectable
without content review.

**Section B — STRUCTURED OUTPUT REGISTER (C-25, C-27)**

The following element types are structured output. They are NOT prose. They are exempt
from C-23 inline citation requirements. Classification is by element type — content
inspection is not required.

| Element type | Canonical form | Prose? | C-23 tag required? |
|-------------|---------------|--------|-------------------|
| Gate decision lines | PROCEED / BLOCKED | No | No |
| Cross-artifact header lines | "One row per [source]. No [item] may be omitted." | No | No |
| Phase boundary prohibition lines | "PROHIBITED: [data class] — [failure mode]" | No | No |
| Per-criterion verdict lines | "C-NN: PASS / FAIL" | No | No |

No other element types are added to this register without revising this contract.

**Inertia annotation for C-27 — why the register must be closed:** The temptation is
to leave the register open, reasoning that any element type not in the prose-permitted
list (Section A) is implicitly structured output. This reasoning requires content
inspection to classify boundary elements: a gate verdict line ("PROCEED") appears in a
narrative position, and classifying it as structured vs. prose requires interpreting
whether it is an affirmative statement or a structured decision. The closure declaration
forecloses content inspection: an unlisted element type is explicitly unclassified (not
implicitly exempt), and its classification status becomes a detectable gap rather than
an inference. Adding a new element type requires an explicit revision to this contract.

FORMAT CONTRACT COMPLETE

---

**ROLE 2 — DOMAIN EXPERT**

You are a Connectors / Power Automate throughput domain expert. The OUTPUT FORMAT
CONTRACT from Role 1 governs all output you produce. You are bound by Section A
(prose-restriction declaration) and Section B (structured output register). Simulate
throughput across the rate-limited system described in the signal. Treat the stated
request volume as 1x nominal; also analyze at 2x and 5x.

---

**PHASE 1 — EVIDENCE PHASE**

**Step 1A — SOURCE REGISTER (C-13)**

Commit the evidence base before naming any tier. A tier with no register entry receives
UNDOCUMENTED in the Limit column; it is not assigned an inferred value.

| Source-ID | Source name | Type | Numeric values it provides |
|-----------|-------------|------|---------------------------|
| S-01 | | | |
| S-02 | | | |

PROHIBITED: adding a new Source-ID after this line. — *prevents retroactive source
injection; a source added after tier analysis cannot be verified as a prior commitment*

**Step 1B — TIER INVENTORY**

**TABLE A — THROTTLE TIER INVENTORY ACROSS VOLUME BANDS**

*(One row per rate-limiting component. Source-ID from register required. Every cell
filled — a blank and "not applicable" are identical under scan.)*

| Tier-ID | Component | Limit (number + unit) | Source-ID | Scope | STATUS 1x | STATUS 2x | STATUS 5x | Binding? | Failure mode |
|---------|-----------|----------------------|-----------|-------|-----------|-----------|-----------|----------|-------------|
| T-01 | | | | | | | | | |
| T-02 | | | | | | | | | |
| ... | | | | | | | | | |

Column notes:
- `Tier-ID` — T-01, T-02, ... verbatim downstream. Compliance failure condition:
  informal synonym fails T-NN threading.
- `Limit` — number + unit. Compliance failure condition: vague label fails precision.
- `Binding?` — exactly one Y. Compliance failure condition: multiple Y entries or no Y
  fails the at-most-one binding constraint.
- `Failure mode` — hard rejection / queue saturation / silent drop / degraded throughput /
  timeout. At least two distinct values.

PROHIBITED: introducing a new T-NN in any Phase 2 section. — *prevents scope creep;
evidence that Phase 1 enumeration was incomplete is not a fill-in opportunity*

**[prose: item 1 — binding-tier causal reason]** Why does the Binding? = Y tier fail
before all others at 1x nominal load? Name the specific causal mechanism.

**[prose: item 2 — binding constraint exclusivity]** For at least one Binding? = N tier,
name the mechanism that prevents it from binding before the primary tier.

---

**PHASE 2 — CLAIMS PHASE**

PROHIBITED: opening Phase 2 before Phase 1B is complete. — *prevents late evidence
injection; claims built on an incomplete tier inventory are unverifiable*

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

Compliance failure condition: risk list without Type column with named taxonomy fails C-22.

---

**TYPE SCAN GATE**

**Purpose annotation (C-26) — three fields:**

- **Failure mode prevented:** Category elision — a risk type absent from TABLE E is
  detectable only by full table scan after TABLE F is complete; the entire category has
  no mitigations but TABLE F appears complete.
- **Gap above C-22:** C-22 ensures the Type column and per-type minimums are present in
  the finished TABLE E. This gate ensures type completeness is verified before TABLE F
  opens. The distinction: C-22 defines what the finished output must contain; this gate
  makes an incomplete TABLE E a construction-time block rather than a post-hoc finding.
  An executor who reasons "C-22 already requires all types — this gate is redundant" has
  confused the structural requirement with the enforcement mechanism.
- **Audit test (C-28):**
  - *Gate-present audit method:* Confirm a named gate step appears between TABLE E and
    TABLE F. Confirm per-category Y/N verdicts are present for Burst, Cascade, and
    RetryAfter. Confirm PROCEED or BLOCKED decision is stated before TABLE F opens.
  - *Gate-absent signature:* TABLE F opens immediately after TABLE E with no intervening
    gate step. Type completeness is verifiable only by scanning TABLE E after TABLE F is
    complete — construction-time blocking is absent.

Scan TABLE E:
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

Named dedicated step. Not embedded prose. Maps output content to essential criterion
categories by name. Reports per-criterion PASS/FAIL.

- C-01 (Primary bottleneck with causal reason): [PASS / FAIL]
- C-02 (Backpressure propagation ≥2 hops with mechanism): [PASS / FAIL]
- C-03 (≥2 tiers with enforcing component and scope): [PASS / FAIL]
- C-04 (UX at each throttle tier): [PASS / FAIL]
- C-05 (Unprotected burst path): [PASS / FAIL]

[prose: item 3 — global criterion-coverage verdict notes] State FAIL rationale for any
criterion above that did not pass.

---

---

## V-05 — Combined: Role Sequence + C-27 Inertia Annotation + C-28 Comprehensive

**Axes:** (1) Role sequence — three-role pipeline: Format Analyst produces the output
contract; Domain Expert produces evidence and claims through TABLE E; Consequence
Analyst activates after the TYPE SCAN GATE is cleared and produces TABLE F and the
global coverage step. Each role is blocked until the prior role's exit condition is
met. (2) Inertia framing for C-27 — the closure declaration carries a named annotation
explaining precisely what failure mode an open register produces (content-inspection
classification for unregistered elements) and how that reintroduces the problem C-25
was designed to eliminate. (3) Comprehensive C-28 — the gate annotation carries a
dual-path audit test with named observables, labeled sub-instructions, and a statement
of why the audit test itself is necessary (distinguishes gate-level verification from
table-level scan).

**Hypothesis:** The three-role pipeline enforces phase ordering at the architectural
level — each role's completed output is the structural precondition for the next role's
activation, making out-of-order execution impossible rather than merely discouraged.
The C-27 inertia annotation demolishes the "implicit complement" reasoning in place,
at the point in the contract where an executor would be most likely to rely on it. The
comprehensive C-28 form provides both a positive test (what to confirm when the gate
is present) and a negative test (what to look for when it is absent), making gate
verification a two-step scan rather than a reconstruction task. This variation is the
strongest candidate for 190/190 because it addresses C-27 and C-28 from structural,
framing, and verification angles simultaneously.

**v10 predicted scoring:** C-27 PASS (Format Analyst role produces the closure with
inertia annotation naming the reintroduced failure mode; additions require explicit
contract revision). C-28 PASS (comprehensive dual-path labeled audit test with named
observables and labeled sub-instructions). All other criteria carry from R9 baseline.
Composite: 190/190.

---

**ROLE 1 — FORMAT ANALYST**

You are the Format Analyst. Your output is the complete OUTPUT FORMAT CONTRACT below.
The Domain Expert (Role 2) and Consequence Analyst (Role 3) are bound by this contract
and may not modify it. Produce the contract by filling every section, then state
"ROLE 1 COMPLETE" before Role 2 activates.

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

ROLE 1 COMPLETE

---

**ROLE 2 — DOMAIN EXPERT**

You are a Connectors / Power Automate throughput domain expert. The OUTPUT FORMAT
CONTRACT from Role 1 governs all output you produce. You are bound by Section A and
Section B and may not modify the contract.

Simulate throughput across the rate-limited system described in the signal. Treat the
stated request volume as 1x nominal; also analyze at 2x and 5x.

---

**PHASE 1 — EVIDENCE PHASE**

**PHASE 1 ENTRY CONDITION:** Phase 1 opens only after ROLE 1 COMPLETE is stated.

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

**STEP 1B GATE:** Every TABLE A row has all columns filled with non-placeholder values.
No vague labels in the Limit column. PROHIBITED: opening Phase 2 before this gate is
cleared. — *prevents late evidence injection; claims built on an incomplete tier
inventory produce unverifiable findings*

---

**PHASE 2 — CLAIMS PHASE**

**PHASE 2 ENTRY CONDITION:** Phase 2 opens only after the STEP 1B GATE is cleared.
The tier registry is closed.

**Enumeration anchor — for each tier in TABLE A (C-17):** every downstream derived
table must include a row for every T-NN. Coverage is verifiable by T-NN count match
against TABLE A, not by reading downstream content. — *prevents coverage elision; a
tier absent from a derived table produces a detectable T-NN count gap*

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

ROLE 2 COMPLETE. The Consequence Analyst (Role 3) activates after the TYPE SCAN GATE
below is cleared.

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
  without adding substance" conflates the structural requirement (what the output must
  contain) with the enforcement mechanism (when completeness is verified). C-22 ensures
  the structure; the gate ensures the missing-category failure mode cannot be produced
  by any valid execution path — an executor following the gate cannot open TABLE F
  against an incomplete risk inventory.
- **Audit test (C-28):**
  - *Gate-present audit method:* Scan for a named gate step between TABLE E and TABLE F.
    Confirm three per-category Y/N verdicts are present — one for Burst, one for Cascade,
    one for RetryAfter. Confirm a PROCEED or BLOCKED decision is explicitly stated before
    TABLE F opens. If all three are present, gate compliance is confirmed.
  - *Gate-absent signature:* TABLE F opens immediately after TABLE E with no intervening
    named gate step. Type completeness may still be verified by scanning TABLE E after
    TABLE F is complete — but the verification is a post-hoc scan, not a construction-time
    block. The distinction: gate present means a missing category blocks TABLE F from
    opening; gate absent means a missing category is a gap discovered after TABLE F is
    complete.

**Escape route for C-26 — "the gate Purpose annotation is redundant because C-22 already
explains why type coverage matters":** This reasoning conflates the *purpose of the type
taxonomy* (which C-22 explains) with the *purpose of the gate* (which is to make type
completeness a construction-time blocking condition). C-22's requirement is present in
the TABLE E header; the gate annotation explains why a named structural check is
necessary given that C-22 is already present. Without the annotation, an executor can
reason "the table already requires all three types — the gate is extra process" and skip
it. The annotation makes that reasoning auditable: the gap the gate closes (post-hoc
vs. construction-time detection) is explicitly stated and cannot be dismissed as
redundant without contradicting the stated purpose.

Scan TABLE E for type completeness:
- Burst: [at least one row present? Y / N]
- Cascade: [at least one row present? Y / N]
- RetryAfter: [at least one row present? Y / N]

If all Y: PROCEED
If any N: BLOCKED — return to TABLE E, add the missing type row, re-run this gate.

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
fails this column's precision requirement. A row naming a category cannot be applied
without further research; a row naming an exact parameter can be applied immediately.

PROHIBITED: adding rows to TABLE E after TABLE F has opened. — *prevents retroactive
risk injection; a risk discovered during mitigation planning is evidence TABLE E was
incomplete — it requires returning to Role 2, completing TABLE E, re-running the TYPE
SCAN GATE, and re-opening TABLE F*

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
