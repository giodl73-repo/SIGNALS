# flow-throttle Variate — Round 14

**Date:** 2026-03-16
**Rubric:** v14 (C-01 through C-37, N_essential=5, N_recommended=3, N_aspirational=29)
**Max composite:** 235 | **Baseline ceiling:** R13 V-04 (230/230 under v13; 230/235 under v14 — C-37 FAIL)

---

## State Analysis: What R13 V-04 Has vs. What R14 Must Add

**R13 V-04 coverage under v14 (assessed):**
- C-01 through C-36: all pass
- C-37: FAIL — no annotation-inventory block in FORMAT CONTRACT; C-18 annotations appear only
  at their anchor sites in the body; dropout detectable only by post-assembly rubric scan, not
  at the handoff boundary

**C-37 gap in R13 V-04:**
The three-role pipeline carries annotations intact (all C-18 annotations present at their anchor
sites in Phase 1B and Phase 2), which is why C-18 passes. But the FORMAT CONTRACT contains only
Section A (prose-permitted contexts) and Section B (structured-output register). There is no
Section C listing each C-18 annotation by anchor identifier and failure-mode label. An executor
who drops an annotation during role execution produces a C-18 violation detectable only by
scanning the full body — the FORMAT CONTRACT provides no inventory to check at the handoff
boundary. C-37 requires that the inventory be sealed before FORMAT CONTRACT COMPLETE, converting
annotation dropout from a content gap into a contract violation.

**Single axes to test:**
1. **Lifecycle emphasis** — Section C added to FORMAT CONTRACT as a prose-list (V-01).
2. **Output format** — Section C as a table with Annot-ID column, enabling count-scan (V-02).
3. **Phrasing register** — Section C with SHALL/PROHIBITED enforcement and explicit annotation-dropout prohibition (V-03).

**Combined axes for V-04 and V-05:**
- V-04: Role sequence + lifecycle emphasis — Role 2 ACTIVATION CONDITIONS reference the annotation inventory count declared in Section C.
- V-05: All three — table-form inventory + SHALL register + count at Role 2 activation boundary + ANNOTATION SCAN GATE before TABLE F.

---

## V-01 — Single Axis: Lifecycle Emphasis (Section C as prose list in FORMAT CONTRACT)

**Axis:** Annotation inventory added to FORMAT CONTRACT as Section C, prose-list form. Each
C-18 annotation listed by anchor identifier (Annot-01 through Annot-07) and failure-mode label.
Sealed under FORMAT CONTRACT COMPLETE before Role 2 activates. No change to role-activation
conditions (Role 2 ACTIVATION CONDITIONS remain identical to R13 V-04). No table format in
Section C.

**Hypothesis:** C-37 PASS — the inventory is a FORMAT CONTRACT deliverable sealed before domain
execution begins; annotation dropout becomes a handoff-boundary violation detectable by checking
anchor presence against the seven registered identifiers. C-37 does not require a table or
count-declared activation conditions — the criterion requires the inventory to be sealed in
FORMAT CONTRACT COMPLETE, which this structure satisfies.

**v14 predicted scoring:** C-37 PASS. C-35 PASS. C-36 PASS. All prior C-01–C-36 carry from R13
V-04 baseline. Composite: 235/235.

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
  contract revision.

**Section C — ANNOTATION INVENTORY (C-18, C-37)**

The following annotations are required at the named anchor sites in the prompt body.
Each annotation is identified by anchor identifier and failure-mode label. An annotation
absent from its anchor site is a contract violation detectable at this inventory without
scanning the body.

- **Annot-01** | Anchor: TABLE A, `Limit (number + unit)` column definition |
  Failure-mode label: vague-label substitution — a label such as "limited" or
  "throttled" appears in the Limit cell in place of a specific number with unit.
- **Annot-02** | Anchor: TABLE A, `Binding?` column definition |
  Failure-mode label: assertion-without-causal-reason — a Binding? = Y designation
  appears without the causal mechanism explaining why this tier fails first.
- **Annot-03** | Anchor: TABLE A, `Failure mode` column definition |
  Failure-mode label: insufficient-categorical-diversity — fewer than two distinct
  failure mode values across TABLE A rows.
- **Annot-04** | Anchor: TABLE B, `Mechanism` column definition |
  Failure-mode label: generic-term substitution — a term such as "blocked" or
  "throttled" appears in place of a named mechanism from the permitted set.
- **Annot-05** | Anchor: TABLE C, `Error code or signal` column definition |
  Failure-mode label: plain-description substitution — a narrative phrase such as
  "request fails" appears in place of a specific HTTP status code or platform signal.
- **Annot-06** | Anchor: TABLE E, `Type` column definition |
  Failure-mode label: category-absence-undetectable — the Type column is absent or
  unnamed, making a missing risk category undetectable by count alone.
- **Annot-07** | Anchor: TABLE F, `Setting or API parameter` column definition |
  Failure-mode label: category-of-action substitution — a phrase such as "add retry
  logic" appears in place of a specific parameter identifier such as
  `connector.retryPolicy`.

This inventory is closed. An annotation not listed here does not exist as a contract
requirement. An annotation listed here that is absent from its anchor site in the body
is a FORMAT CONTRACT violation.

FORMAT CONTRACT COMPLETE

---

**ROLE 2 — DOMAIN EXPERT**

You are a Connectors / Power Automate throughput domain expert. The OUTPUT FORMAT
CONTRACT from Role 1 governs all output you produce. You are bound by Section A,
Section B, and Section C and may not modify the contract.

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
  failure condition: an informal synonym in place of T-NN fails tier-ID threading.
- `Limit (number + unit)` — a specific number with a unit (e.g., "1,200 req/min",
  "500 connections"). *Violation type (Annot-01): vague-label substitution — a label
  such as "limited" or "throttled" in place of a specific number with unit fails
  precision.*
- `STATUS Nx` — OK / HIT / SAT. Must shift between at least two bands.
- `Binding?` — exactly one Y. *Violation type (Annot-02): assertion-without-causal-reason
  — a Binding? = Y designation without the causal mechanism explaining why this tier
  fails first.*
- `Failure mode` — hard rejection / queue saturation / silent drop / degraded throughput /
  timeout. *Violation type (Annot-03): insufficient-categorical-diversity — fewer than
  two distinct values across rows.*

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
downstream content.

**TABLE B — BACKPRESSURE PROPAGATION TRACE**

*(Source: TABLE A. Two hops minimum. T-NNs must reference TABLE A entries.)*

| Hop | From (Tier-ID) | To component | Mechanism | Observable effect |
|-----|----------------|--------------|-----------|-------------------|
| 1 | | | | |
| 2 | | | | |
| ... | | | | |

Mechanism values: queue-fill, connection-hold, retry-amplification, dependency-stall,
timeout-cascade. *Violation type (Annot-04): generic-term substitution — a term such as
"blocked" or "throttled" in place of a named mechanism from the permitted set fails
precision.*

**TABLE C — USER EXPERIENCE CATALOG**

*(Source: TABLE A. One row per TABLE A Tier-ID. No tier may be omitted.)*

| Tier-ID | Error code or signal | Retry-After present? (Y/N) | Retry-After surfaced to caller? (Y/N) | Visible in run history? (Y/N/SILENT) | Failure if Retry-After ignored |
|---------|---------------------|---------------------------|--------------------------------------|--------------------------------------|-------------------------------|
| T-01 | | | | | |
| T-02 | | | | | |

`Error code or signal` — Record the specific HTTP status code or platform signal
identifier (e.g., "HTTP 429", "HTTP 503", "TL-0001"). *Violation type (Annot-05):
plain-description substitution — a phrase such as "request fails" in place of a
specific HTTP status code or platform signal fails precision.*

**TABLE D — UNPROTECTED BURST PATHS**

*(Source: TABLE A. At least one row. If no gap: name >=2 controls as evidence that
every entry point is protected.)*

| Path-ID | Entry component | Tier-IDs involved | Gap reason or named controls | Consequence at burst volume |
|---------|----------------|-------------------|-----------------------------|-----------------------------|
| P-01 | | | | |

**TABLE E — RISK TAXONOMY**

*(Source: TABLE A + TABLE B + TABLE D. Per-type minimum: >=1 Burst, >=1 Cascade,
>=1 RetryAfter.)*

| Risk-ID | Tier-ID | Type | Risk description | Severity (H/M/L) |
|---------|---------|------|-----------------|-----------------|
| R-01 | | Burst | | |
| R-02 | | Cascade | | |
| R-03 | | RetryAfter | | |

`Type` column — named taxonomy required: Burst / Cascade / RetryAfter. *Violation type
(Annot-06): category-absence-undetectable — a risk list without a Type column with
named taxonomy and per-type minimum-row constraint fails C-22 even if all required
categories happen to appear, because the mechanism that makes category absence
detectable is absent.*

---

**TYPE SCAN GATE**

**Purpose annotation (C-26) — three fields:**

- **Failure mode prevented:** Category elision — a risk type (Burst, Cascade, or
  RetryAfter) is absent from TABLE E but detectable only by full table scan after
  TABLE F is complete. At that point, TABLE F also has no mitigations for the missing
  category — two artifacts are incomplete and both require revision.
- **Gap above C-22:** C-22 ensures the Type column is present and all three categories
  appear in the finished TABLE E. This gate ensures type completeness is verified before
  TABLE F opens. An executor who reasons "C-22 already requires all three types — this
  gate adds process without substance" conflates the structural requirement with the
  enforcement mechanism. C-22 ensures the structure; the gate ensures the
  missing-category failure mode cannot be produced by any valid execution path.
- **Audit test (C-28, C-31):**
  - *Gate-present audit method — 5 observables:* Locate the section titled **TYPE SCAN
    GATE**. Structural position: between TABLE E's last R-NN row and TABLE F section
    header. Confirm 5 observables in sequence: (1) `Burst: [Y / N]` before gate
    decision. (2) `Cascade: [Y / N]` before gate decision. (3) `RetryAfter: [Y / N]`
    before gate decision. (4) `PROCEED` or `BLOCKED` after all three verdict lines.
    (5) TABLE F header and MR-01 after gate decision line. All 5 confirmed = gate
    compliance verified by count-scan and artifact-ID.
  - *Gate-absent signature — 1 observable:* No **TYPE SCAN GATE** section header in
    the structural gap between TABLE E's last R-NN and MR-01. 1 observable: no
    `[Category]: [Y / N]` verdict lines in that gap.

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

ROLE 2 COMPLETE. The Consequence Analyst (Role 3) activates subject to the activation
conditions below.

---

**ROLE 3 — CONSEQUENCE ANALYST**

**ROLE 3 ACTIVATION CONDITIONS (C-36):**

Role 3 activates only after PROCEED is stated at the TYPE SCAN GATE AND the following
observable counts are confirmed at this boundary:

- Gate-present path — 5 observables required before Role 3 opens:
  (1) `Burst: Y` verdict line present
  (2) `Cascade: Y` verdict line present
  (3) `RetryAfter: Y` verdict line present
  (4) `PROCEED` gate decision line present
  (5) TABLE F section header and MR-01 not yet produced
  Confirming all 5 observables by count-scan at this boundary is a Role 3 entry
  condition. Role 3 cannot activate if any of the 5 observables is missing.

- Gate-absent path — 1 observable confirms non-activation:
  (1) No `[Category]: [Y / N]` verdict lines in the structural gap between TABLE E's
  last R-NN and this activation boundary.
  If this 1 observable is confirmed, the gate is absent and Role 3 cannot activate —
  return to Role 2, complete the TYPE SCAN GATE, re-confirm activation conditions.

You are the Consequence Analyst. Your scope is TABLE F (mitigation registry) and the
global criterion-coverage step. You are bound by the OUTPUT FORMAT CONTRACT above.

**TABLE F — MITIGATION REGISTRY**

*(Source: TABLE E. One row per TABLE E risk. No risk may be omitted.)*

| MR-ID | Source (Risk-ID) | Gap type | Component | Setting or API parameter | Change | Expected outcome | Tradeoff |
|-------|-----------------|----------|-----------|--------------------------|--------|-----------------|---------|
| MR-01 | | | | | | | |
| MR-02 | | | | | | | |

`Setting or API parameter` — the exact configuration key, connector property, or API
attribute name. *Violation type (Annot-07): category-of-action substitution — a phrase
such as "add retry logic" in place of a specific parameter identifier such as
`connector.retryPolicy` fails precision. A row naming a category cannot be applied
without further research; a row naming an exact parameter can be applied immediately.*

PROHIBITED: adding rows to TABLE E after TABLE F has opened. — *prevents retroactive
risk injection; return to Role 2, complete TABLE E, re-run the TYPE SCAN GATE,
re-confirm activation conditions, re-open TABLE F*

---

**GLOBAL CRITERION-COVERAGE STEP**

Named dedicated step. Not embedded prose. Reports per-criterion PASS/FAIL.

- C-01 (Primary bottleneck with causal reason): [binding-tier causal reason present and
  names specific causal mechanism? PASS / FAIL]
- C-02 (Backpressure propagation >=2 hops with mechanism): [TABLE B >=2 rows with T-NN
  identifiers and specific mechanisms from the permitted set? PASS / FAIL]
- C-03 (>=2 tiers with enforcing component and scope): [TABLE A >=2 rows with Component
  and Scope filled, each with specific numeric Limit? PASS / FAIL]
- C-04 (UX at each throttle tier): [TABLE C one row per TABLE A Tier-ID, no tier
  omitted? PASS / FAIL]
- C-05 (Unprotected burst path): [TABLE D >=1 row with gap reason, or >=1 row with >=2
  named controls? PASS / FAIL]

[prose: item 3 — global criterion-coverage verdict notes] State FAIL rationale for any
criterion above that did not pass.

ROLE 3 COMPLETE.

---

---

## V-02 — Single Axis: Output Format (Section C as table with Annot-ID column)

**Axis:** Section C in FORMAT CONTRACT is a TABLE rather than a prose list. Columns:
Annot-ID | Anchor site | Failure-mode label | Prohibited form. Table form enables
count-scan verification: expected row count = 7; a missing row is a count discrepancy
detectable without reading annotation text. Role architecture and activation conditions
unchanged from V-01.

**Hypothesis:** C-37 PASS — table form additionally satisfies the count-verifiability
intent of C-37: annotation dropout is detectable by row-count discrepancy (expected 7
rows, fewer present = gap) without scanning annotation content. The annotation inventory
in V-01 requires identifying each bullet by anchor label; the table form reduces that to
a count-scan. Whether C-37 distinguishes between these forms will be determined by the
scorecard.

**v14 predicted scoring:** C-37 PASS. C-35 PASS. C-36 PASS. Composite: 235/235.

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

**Section C — ANNOTATION INVENTORY (C-18, C-37)**

The following table lists every required annotation by anchor identifier and
failure-mode label. Expected row count: 7. A row absent from this table does not exist
as a contract requirement. A row present in this table whose annotation is absent from
its anchor site in the body is a FORMAT CONTRACT violation detectable by anchor-ID
lookup without content scan.

| Annot-ID | Anchor site | Failure-mode label | Prohibited form (example) |
|----------|------------|-------------------|--------------------------|
| Annot-01 | TABLE A — `Limit (number + unit)` column definition | vague-label substitution | "limited" or "throttled" in place of "1,200 req/min" |
| Annot-02 | TABLE A — `Binding?` column definition | assertion-without-causal-reason | Binding? = Y with no mechanism named |
| Annot-03 | TABLE A — `Failure mode` column definition | insufficient-categorical-diversity | Fewer than two distinct values across rows |
| Annot-04 | TABLE B — `Mechanism` column definition | generic-term substitution | "blocked" or "throttled" in place of "queue-fill" |
| Annot-05 | TABLE C — `Error code or signal` column definition | plain-description substitution | "request fails" in place of "HTTP 429" |
| Annot-06 | TABLE E — `Type` column definition | category-absence-undetectable | Risk list without Type column with named taxonomy |
| Annot-07 | TABLE F — `Setting or API parameter` column definition | category-of-action substitution | "add retry logic" in place of `connector.retryPolicy` |

This table is closed. No row is added without revising this contract.

FORMAT CONTRACT COMPLETE

---

**ROLE 2 — DOMAIN EXPERT**

You are a Connectors / Power Automate throughput domain expert. The OUTPUT FORMAT
CONTRACT from Role 1 governs all output you produce. You are bound by Section A,
Section B, and Section C and may not modify the contract.

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
- `Limit (number + unit)` — a specific number with a unit. *Violation type (Annot-01):
  vague-label substitution — "limited" or "throttled" in place of a specific number
  with unit fails precision.*
- `STATUS Nx` — OK / HIT / SAT. Must shift between at least two bands.
- `Binding?` — exactly one Y. *Violation type (Annot-02): assertion-without-causal-reason
  — Binding? = Y without named causal mechanism.*
- `Failure mode` — hard rejection / queue saturation / silent drop / degraded throughput /
  timeout. *Violation type (Annot-03): insufficient-categorical-diversity — fewer than
  two distinct values across rows.*

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
timeout-cascade. *Violation type (Annot-04): generic-term substitution — "blocked" or
"throttled" in place of a named mechanism from the permitted set.*

**TABLE C — USER EXPERIENCE CATALOG**

*(Source: TABLE A. One row per TABLE A Tier-ID. No tier may be omitted.)*

| Tier-ID | Error code or signal | Retry-After present? (Y/N) | Retry-After surfaced to caller? (Y/N) | Visible in run history? (Y/N/SILENT) | Failure if Retry-After ignored |
|---------|---------------------|---------------------------|--------------------------------------|--------------------------------------|-------------------------------|
| T-01 | | | | | |
| T-02 | | | | | |

*Violation type (Annot-05): plain-description substitution — "request fails" in place
of "HTTP 429" or a named platform signal identifier fails precision.*

**TABLE D — UNPROTECTED BURST PATHS**

*(Source: TABLE A. At least one row. If no gap: >=2 named controls as evidence.)*

| Path-ID | Entry component | Tier-IDs involved | Gap reason or named controls | Consequence at burst volume |
|---------|----------------|-------------------|-----------------------------|-----------------------------|
| P-01 | | | | |

**TABLE E — RISK TAXONOMY**

*(Source: TABLE A + TABLE B + TABLE D. Per-type minimum: >=1 Burst, >=1 Cascade,
>=1 RetryAfter.)*

| Risk-ID | Tier-ID | Type | Risk description | Severity (H/M/L) |
|---------|---------|------|-----------------|-----------------|
| R-01 | | Burst | | |
| R-02 | | Cascade | | |
| R-03 | | RetryAfter | | |

*Violation type (Annot-06): category-absence-undetectable — a risk list without a
Type column with named taxonomy and per-type minimum-row constraint fails C-22 even
if all required categories happen to appear.*

---

**TYPE SCAN GATE**

**Purpose annotation (C-26) — three fields:**

- **Failure mode prevented:** Category elision — a risk type absent from TABLE E
  detectable only by full table scan after TABLE F is complete; both artifacts require
  revision.
- **Gap above C-22:** C-22 defines what the finished output must contain. This gate makes
  an incomplete TABLE E a construction-time blocking condition. An executor who reasons
  "C-22 already requires all three types — this gate adds process without substance"
  conflates the structural requirement with the enforcement mechanism. C-22 ensures the
  structure; the gate ensures the missing-category failure mode cannot be produced by any
  valid execution path.
- **Audit test (C-28, C-31):**
  - *Gate-present audit method — 5 observables:* Locate the section titled **TYPE SCAN
    GATE**. Structural position: between TABLE E's last R-NN row and TABLE F section
    header. Confirm 5 observables in sequence: (1) `Burst: [Y / N]` before gate decision.
    (2) `Cascade: [Y / N]` before gate decision. (3) `RetryAfter: [Y / N]` before gate
    decision. (4) `PROCEED` or `BLOCKED` after all three verdict lines. (5) TABLE F
    header and MR-01 after gate decision line. All 5 confirmed = gate compliance verified.
  - *Gate-absent signature — 1 observable:* No **TYPE SCAN GATE** section header in the
    structural gap between TABLE E's last R-NN and MR-01.

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

ROLE 2 COMPLETE. The Consequence Analyst (Role 3) activates subject to the activation
conditions below.

---

**ROLE 3 — CONSEQUENCE ANALYST**

**ROLE 3 ACTIVATION CONDITIONS (C-36):**

Role 3 activates only after PROCEED is stated at the TYPE SCAN GATE AND the following
observable counts are confirmed at this boundary:

- Gate-present path — 5 observables required before Role 3 opens:
  (1) `Burst: Y` verdict line present
  (2) `Cascade: Y` verdict line present
  (3) `RetryAfter: Y` verdict line present
  (4) `PROCEED` gate decision line present
  (5) TABLE F section header and MR-01 not yet produced
  All 5 confirmed = Role 3 may activate.

- Gate-absent path — 1 observable confirms non-activation:
  (1) No `[Category]: [Y / N]` verdict lines between TABLE E's last R-NN and this
  boundary. Gate absent — return to Role 2, complete TYPE SCAN GATE.

You are the Consequence Analyst. Your scope is TABLE F and the global criterion-coverage
step. You are bound by the OUTPUT FORMAT CONTRACT above.

**TABLE F — MITIGATION REGISTRY**

*(Source: TABLE E. One row per TABLE E risk. No risk may be omitted.)*

| MR-ID | Source (Risk-ID) | Gap type | Component | Setting or API parameter | Change | Expected outcome | Tradeoff |
|-------|-----------------|----------|-----------|--------------------------|--------|-----------------|---------|
| MR-01 | | | | | | | |
| MR-02 | | | | | | | |

*Violation type (Annot-07): category-of-action substitution — "add retry logic" in place
of a specific parameter identifier such as `connector.retryPolicy`. A row naming a
category cannot be applied without further research; a row naming an exact parameter
can be applied immediately.*

PROHIBITED: adding rows to TABLE E after TABLE F has opened. — *prevents retroactive
risk injection*

---

**GLOBAL CRITERION-COVERAGE STEP**

Named dedicated step. Not embedded prose. Reports per-criterion PASS/FAIL.

- C-01 (Primary bottleneck with causal reason): [PASS / FAIL]
- C-02 (Backpressure propagation >=2 hops with mechanism): [PASS / FAIL]
- C-03 (>=2 tiers with enforcing component and scope): [PASS / FAIL]
- C-04 (UX at each throttle tier): [PASS / FAIL]
- C-05 (Unprotected burst path): [PASS / FAIL]

[prose: item 3 — global criterion-coverage verdict notes] State FAIL rationale for any
criterion above that did not pass.

ROLE 3 COMPLETE.

---

---

## V-03 — Single Axis: Phrasing Register (Section C with SHALL enforcement + annotation-dropout PROHIBITED)

**Axis:** Section C in FORMAT CONTRACT uses formal SHALL/MUST/PROHIBITED register for
annotation requirements. Each annotation carries a SHALL appear directive and a
PROHIBITED dropout clause. The section closes with an explicit PROHIBITED: annotation
dropout prohibition listing each anchor identifier. No change to role-activation
conditions from V-01/V-02.

**Hypothesis:** C-37 PASS — the SHALL/PROHIBITED framing tests whether C-37 requires
normative enforcement language (not just an inventory listing) to convert annotation
dropout into a detectable contract violation. The dropout prohibition clause at the
section close converts each annotation from a "listed requirement" to a "listed
prohibition" — the absence of each annotation becomes a named violation rather than
a missing element. Whether the phrasing register affects the C-37 verdict relative to
V-01 will isolate whether normative language is necessary or sufficient for the criterion.

**v14 predicted scoring:** C-37 PASS. C-35 PASS. C-36 PASS. Composite: 235/235.

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
   coverage step. Scope: one sentence per failed criterion. Authorized by C-19.

Any prose passage appearing outside these three declared scopes is a format violation
detectable without content review.

**Section B — STRUCTURED OUTPUT REGISTER (C-25, C-27)**

The following element types are structured output. They are NOT prose. They are exempt
from C-23 inline citation requirements. Classification is by element type.

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
  exhaustive. The closure declaration converts implicit-exempt to explicitly-unclassified.
  Adding a new type requires an explicit revision, auditable by change history.
- **Concrete example (C-30):** A load-shape verdict label — "FLAT-LOAD: within nominal
  band" — matches none of the four registered canonical forms. Under a closed register,
  the inference is foreclosed: this element type is unregistered, its classifications are
  explicitly unresolved, and adding it requires a named contract revision.

**Section C — ANNOTATION INVENTORY (C-18, C-37)**

The annotations below SHALL appear at the named anchor sites in the prompt body. Each
annotation is identified by anchor identifier and failure-mode label. An executor SHALL
NOT omit an annotation from its anchor site. Annotation dropout is a FORMAT CONTRACT
violation — the presence of each annotation is a contract requirement sealed here, not
a content preference detectable only by rubric scan.

PROHIBITED: omitting any of the following annotations from its declared anchor site —
*prevents annotation dropout; a missing annotation at its anchor site converts a
detectable precision-site failure mode into a silent gap not recoverable at the handoff
boundary*

- **Annot-01 SHALL appear at:** TABLE A, `Limit (number + unit)` column definition.
  Failure-mode label: vague-label substitution. Required form: a *Violation type*
  annotation naming "vague-label substitution" and citing the prohibited pattern ("limited"
  or "throttled" in place of a specific number with unit).

- **Annot-02 SHALL appear at:** TABLE A, `Binding?` column definition.
  Failure-mode label: assertion-without-causal-reason. Required form: a *Violation type*
  annotation naming "assertion-without-causal-reason" and citing the prohibited pattern
  (Binding? = Y with no mechanism named).

- **Annot-03 SHALL appear at:** TABLE A, `Failure mode` column definition.
  Failure-mode label: insufficient-categorical-diversity. Required form: a *Violation
  type* annotation naming "insufficient-categorical-diversity" and citing the prohibited
  pattern (fewer than two distinct values across rows).

- **Annot-04 SHALL appear at:** TABLE B, `Mechanism` column definition.
  Failure-mode label: generic-term substitution. Required form: a *Violation type*
  annotation naming "generic-term substitution" and citing the prohibited pattern
  ("blocked" or "throttled" in place of a named mechanism from the permitted set).

- **Annot-05 SHALL appear at:** TABLE C, `Error code or signal` column definition.
  Failure-mode label: plain-description substitution. Required form: a *Violation type*
  annotation naming "plain-description substitution" and citing the prohibited pattern
  ("request fails" in place of "HTTP 429").

- **Annot-06 SHALL appear at:** TABLE E, `Type` column definition.
  Failure-mode label: category-absence-undetectable. Required form: a *Violation type*
  annotation naming "category-absence-undetectable" and citing the prohibited pattern
  (risk list without Type column with named taxonomy and per-type minimum-row constraint).

- **Annot-07 SHALL appear at:** TABLE F, `Setting or API parameter` column definition.
  Failure-mode label: category-of-action substitution. Required form: a *Violation type*
  annotation naming "category-of-action substitution" and citing the prohibited pattern
  ("add retry logic" in place of `connector.retryPolicy`).

This inventory is closed. No annotation is added without revising this contract.

FORMAT CONTRACT COMPLETE

---

**ROLE 2 — DOMAIN EXPERT**

You are a Connectors / Power Automate throughput domain expert. The OUTPUT FORMAT
CONTRACT from Role 1 governs all output you produce. You are bound by Section A,
Section B, and Section C. Section C SHALL requirements apply to every column definition
annotated in the inventory.

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
injection*

**Step 1B — TIER INVENTORY**

**TABLE A — THROTTLE TIER INVENTORY ACROSS VOLUME BANDS**

*(One row per rate-limiting component. Source-ID from register required. Every cell
filled.)*

| Tier-ID | Component | Limit (number + unit) | Source-ID | Scope | STATUS 1x | STATUS 2x | STATUS 5x | Binding? | Failure mode |
|---------|-----------|----------------------|-----------|-------|-----------|-----------|-----------|----------|-------------|
| T-01 | | | | | | | | | |
| T-02 | | | | | | | | | |
| ... | | | | | | | | | |

Column notes:
- `Tier-ID` — T-01, T-02, ... Use verbatim in every downstream table.
- `Limit (number + unit)` — specific number with unit. *Violation type (Annot-01):
  vague-label substitution — "limited" or "throttled" in place of a specific number
  with unit fails precision.*
- `STATUS Nx` — OK / HIT / SAT. Must shift between at least two bands.
- `Binding?` — exactly one Y. *Violation type (Annot-02): assertion-without-causal-reason
  — Binding? = Y without named causal mechanism.*
- `Failure mode` — hard rejection / queue saturation / silent drop / degraded throughput /
  timeout. *Violation type (Annot-03): insufficient-categorical-diversity — fewer than
  two distinct values across rows.*

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
timeout-cascade. *Violation type (Annot-04): generic-term substitution — "blocked" or
"throttled" in place of a named mechanism from the permitted set.*

**TABLE C — USER EXPERIENCE CATALOG**

*(Source: TABLE A. One row per TABLE A Tier-ID. No tier may be omitted.)*

| Tier-ID | Error code or signal | Retry-After present? (Y/N) | Retry-After surfaced to caller? (Y/N) | Visible in run history? (Y/N/SILENT) | Failure if Retry-After ignored |
|---------|---------------------|---------------------------|--------------------------------------|--------------------------------------|-------------------------------|
| T-01 | | | | | |
| T-02 | | | | | |

*Violation type (Annot-05): plain-description substitution — "request fails" in place
of "HTTP 429" or named platform signal fails precision.*

**TABLE D — UNPROTECTED BURST PATHS**

*(Source: TABLE A. At least one row. If no gap: >=2 named controls as evidence.)*

| Path-ID | Entry component | Tier-IDs involved | Gap reason or named controls | Consequence at burst volume |
|---------|----------------|-------------------|-----------------------------|-----------------------------|
| P-01 | | | | |

**TABLE E — RISK TAXONOMY**

*(Source: TABLE A + TABLE B + TABLE D. Per-type minimum: >=1 Burst, >=1 Cascade,
>=1 RetryAfter.)*

| Risk-ID | Tier-ID | Type | Risk description | Severity (H/M/L) |
|---------|---------|------|-----------------|-----------------|
| R-01 | | Burst | | |
| R-02 | | Cascade | | |
| R-03 | | RetryAfter | | |

*Violation type (Annot-06): category-absence-undetectable — risk list without Type
column with named taxonomy and per-type minimum-row constraint fails C-22 even if all
required categories happen to appear.*

---

**TYPE SCAN GATE**

**Purpose annotation (C-26) — three fields:**

- **Failure mode prevented:** Category elision — a risk type absent from TABLE E
  detectable only by full table scan after TABLE F is complete.
- **Gap above C-22:** C-22 defines what the finished output must contain. This gate
  makes an incomplete TABLE E a construction-time blocking condition. C-22 ensures the
  structure; the gate ensures the missing-category failure mode cannot be produced by any
  valid execution path.
- **Audit test (C-28, C-31):**
  - *Gate-present audit method — 5 observables:* Locate **TYPE SCAN GATE** between
    TABLE E's last R-NN row and TABLE F header. Confirm: (1) `Burst: [Y / N]`, (2)
    `Cascade: [Y / N]`, (3) `RetryAfter: [Y / N]` — all before gate decision. (4)
    `PROCEED` or `BLOCKED` after all three. (5) TABLE F header and MR-01 after gate
    decision. All 5 confirmed = gate compliance verified.
  - *Gate-absent signature — 1 observable:* No **TYPE SCAN GATE** header in the gap
    between TABLE E's last R-NN and MR-01.

**Escape route for C-26 — "the gate Purpose annotation is redundant because C-22 already
explains why type coverage matters" (C-32):** This reasoning conflates the purpose of
the type taxonomy (C-22) with the purpose of the gate (construction-time blocking).

Scan TABLE E for type completeness:
- Burst: [at least one row present? Y / N]
- Cascade: [at least one row present? Y / N]
- RetryAfter: [at least one row present? Y / N]

If all Y: PROCEED
If any N: BLOCKED — return to TABLE E, add the missing type row, re-run this gate.

ROLE 2 COMPLETE. The Consequence Analyst (Role 3) activates subject to the activation
conditions below.

---

**ROLE 3 — CONSEQUENCE ANALYST**

**ROLE 3 ACTIVATION CONDITIONS (C-36):**

Role 3 activates only after PROCEED is stated at the TYPE SCAN GATE AND the following
observable counts are confirmed:

- Gate-present path — 5 observables required:
  (1) `Burst: Y` verdict line present
  (2) `Cascade: Y` verdict line present
  (3) `RetryAfter: Y` verdict line present
  (4) `PROCEED` gate decision line present
  (5) TABLE F section header and MR-01 not yet produced

- Gate-absent path — 1 observable confirms non-activation:
  (1) No `[Category]: [Y / N]` verdict lines between TABLE E's last R-NN and this
  boundary. Gate absent — return to Role 2.

You are the Consequence Analyst. Your scope is TABLE F and the global criterion-coverage
step. You are bound by the OUTPUT FORMAT CONTRACT including Section C SHALL requirements.

**TABLE F — MITIGATION REGISTRY**

*(Source: TABLE E. One row per TABLE E risk. No risk may be omitted.)*

| MR-ID | Source (Risk-ID) | Gap type | Component | Setting or API parameter | Change | Expected outcome | Tradeoff |
|-------|-----------------|----------|-----------|--------------------------|--------|-----------------|---------|
| MR-01 | | | | | | | |
| MR-02 | | | | | | | |

*Violation type (Annot-07): category-of-action substitution — "add retry logic" in place
of a specific parameter identifier such as `connector.retryPolicy`. A row naming a
category cannot be applied without further research; a row naming an exact parameter
can be applied immediately.*

PROHIBITED: adding rows to TABLE E after TABLE F has opened. — *prevents retroactive
risk injection*

---

**GLOBAL CRITERION-COVERAGE STEP**

Named dedicated step. Not embedded prose. Reports per-criterion PASS/FAIL.

- C-01 (Primary bottleneck with causal reason): [PASS / FAIL]
- C-02 (Backpressure propagation >=2 hops with mechanism): [PASS / FAIL]
- C-03 (>=2 tiers with enforcing component and scope): [PASS / FAIL]
- C-04 (UX at each throttle tier): [PASS / FAIL]
- C-05 (Unprotected burst path): [PASS / FAIL]

[prose: item 3 — global criterion-coverage verdict notes] State FAIL rationale for any
criterion above that did not pass.

ROLE 3 COMPLETE.

---

---

## V-04 — Combined Axes: Role Sequence + Lifecycle Emphasis (Role 2 activation references annotation inventory count)

**Axes:** (1) Lifecycle emphasis — Section C as table in FORMAT CONTRACT (per V-02).
(2) Role sequence — Role 2 ACTIVATION CONDITIONS declare the annotation-inventory count
at the role boundary: "Confirm Section C annotation inventory: 7 annotations registered.
Confirm all 7 Annot-IDs appear at their anchor sites before proceeding." Missing
annotation = Role 2 entry condition failure, not a rubric-scan gap.

**Hypothesis:** C-37 PASS with stronger enforcement than V-01/V-02 — the annotation
inventory is both sealed in the FORMAT CONTRACT (satisfying the contract-lock mechanism)
AND wired to Role 2 activation as a count-declared condition. Annotation dropout is now
detectable at two boundaries: the FORMAT CONTRACT handoff (where the inventory exists as
a table) and the Role 2 activation check (where the count is confirmed before any analysis
begins). The combined check converts annotation dropout from a contract violation (detected
at handoff) into a role-activation failure (detected before the role body opens).

**v14 predicted scoring:** C-37 PASS. C-35 PASS. C-36 PASS. Composite: 235/235.

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
   coverage step. Scope: one sentence per failed criterion. Authorized by C-19.

Any prose passage outside these three declared scopes is a format violation detectable
without content review.

**Section B — STRUCTURED OUTPUT REGISTER (C-25, C-27)**

| Element type | Canonical form | Prose? | C-23 tag required? |
|-------------|---------------|--------|-------------------|
| Gate decision lines | PROCEED / BLOCKED | No | No |
| Cross-artifact header lines | "One row per [source]. No [item] may be omitted." | No | No |
| Phase boundary prohibition lines | "PROHIBITED: [data class] — [failure mode]" | No | No |
| Per-criterion verdict lines | "C-NN: PASS / FAIL" | No | No |

No other element types are added to this register without revising this contract.

**Inertia annotation for C-27 — why the register must be declared closed — 3 fields: Failure mode prevented | Gap above C-25 | Concrete example (C-29, C-30):**

- **Failure mode prevented:** Implicit-complement classification — an executor reasoning
  that the complement of Section A is implicitly structured output. Under an open
  register, classification is by content-based inference rather than register membership.
  This is the content-inspection problem C-25 was designed to eliminate.
- **Gap above C-25:** C-25 requires enumeration with explicit Prose? and C-23-tag
  classifications but does not require the register to declare itself exhaustive. The
  closure declaration converts implicit-exempt to explicitly-unclassified. Adding a new
  type requires a named revision, auditable by change history.
- **Concrete example (C-30):** A load-shape verdict label — "FLAT-LOAD: within nominal
  band" — matches none of the four registered canonical forms. Under a closed register,
  this element type is unregistered, its classifications explicitly unresolved, and
  adding it requires a named contract revision.

**Section C — ANNOTATION INVENTORY (C-18, C-37)**

Expected row count: 7. This table is the annotation-inventory required by C-37. An
annotation absent from its anchor site in the body is a FORMAT CONTRACT violation
detectable by anchor-ID lookup at this table. Role 2 SHALL confirm all 7 Annot-IDs
are present at their anchor sites before opening Phase 1.

| Annot-ID | Anchor site | Failure-mode label | Prohibited form (example) |
|----------|------------|-------------------|--------------------------|
| Annot-01 | TABLE A — `Limit (number + unit)` column definition | vague-label substitution | "limited" or "throttled" in place of "1,200 req/min" |
| Annot-02 | TABLE A — `Binding?` column definition | assertion-without-causal-reason | Binding? = Y with no mechanism named |
| Annot-03 | TABLE A — `Failure mode` column definition | insufficient-categorical-diversity | Fewer than two distinct values across rows |
| Annot-04 | TABLE B — `Mechanism` column definition | generic-term substitution | "blocked" or "throttled" in place of "queue-fill" |
| Annot-05 | TABLE C — `Error code or signal` column definition | plain-description substitution | "request fails" in place of "HTTP 429" |
| Annot-06 | TABLE E — `Type` column definition | category-absence-undetectable | Risk list without Type column with named taxonomy |
| Annot-07 | TABLE F — `Setting or API parameter` column definition | category-of-action substitution | "add retry logic" in place of `connector.retryPolicy` |

This table is closed. No row is added without revising this contract.

FORMAT CONTRACT COMPLETE

---

**ROLE 2 — DOMAIN EXPERT**

**ROLE 2 ACTIVATION CONDITIONS (C-37 enforcement — annotation inventory confirmation):**

Role 2 activates only after FORMAT CONTRACT COMPLETE is stated AND the following
annotation-inventory confirmation is completed at this boundary:

- Annotation inventory count — 7 annotations registered in Section C. Confirm all 7
  Annot-IDs are present at their anchor sites before Phase 1 opens:
  (1) Annot-01 present at TABLE A `Limit (number + unit)` column definition
  (2) Annot-02 present at TABLE A `Binding?` column definition
  (3) Annot-03 present at TABLE A `Failure mode` column definition
  (4) Annot-04 present at TABLE B `Mechanism` column definition
  (5) Annot-05 present at TABLE C `Error code or signal` column definition
  (6) Annot-06 present at TABLE E `Type` column definition
  (7) Annot-07 present at TABLE F `Setting or API parameter` column definition
  All 7 confirmed = Role 2 may open Phase 1.
  Any Annot-ID absent from its anchor site = Role 2 activation blocked. Restore the
  missing annotation at its anchor site before re-confirming.

You are a Connectors / Power Automate throughput domain expert. The OUTPUT FORMAT
CONTRACT from Role 1 governs all output you produce.

Simulate throughput across the rate-limited system described in the signal. Treat the
stated request volume as 1x nominal; also analyze at 2x and 5x.

**PHASE 1 ENTRY CONDITION:** Phase 1 opens only after Role 2 activation conditions are
confirmed.

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
filled.)*

| Tier-ID | Component | Limit (number + unit) | Source-ID | Scope | STATUS 1x | STATUS 2x | STATUS 5x | Binding? | Failure mode |
|---------|-----------|----------------------|-----------|-------|-----------|-----------|-----------|----------|-------------|
| T-01 | | | | | | | | | |
| T-02 | | | | | | | | | |
| ... | | | | | | | | | |

Column notes:
- `Tier-ID` — T-01, T-02, ... Use verbatim in every downstream table.
- `Limit (number + unit)` — specific number with unit. *Violation type (Annot-01):
  vague-label substitution — "limited" or "throttled" in place of a specific number
  with unit fails precision.*
- `STATUS Nx` — OK / HIT / SAT. Must shift between at least two bands.
- `Binding?` — exactly one Y. *Violation type (Annot-02): assertion-without-causal-reason
  — Binding? = Y without named causal mechanism.*
- `Failure mode` — hard rejection / queue saturation / silent drop / degraded throughput /
  timeout. *Violation type (Annot-03): insufficient-categorical-diversity — fewer than
  two distinct values across rows.*

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
for every T-NN. Coverage verifiable by T-NN count match.

**TABLE B — BACKPRESSURE PROPAGATION TRACE**

*(Source: TABLE A. Two hops minimum.)*

| Hop | From (Tier-ID) | To component | Mechanism | Observable effect |
|-----|----------------|--------------|-----------|-------------------|
| 1 | | | | |
| 2 | | | | |
| ... | | | | |

Mechanism values: queue-fill, connection-hold, retry-amplification, dependency-stall,
timeout-cascade. *Violation type (Annot-04): generic-term substitution — "blocked" or
"throttled" in place of a named mechanism from the permitted set.*

**TABLE C — USER EXPERIENCE CATALOG**

*(Source: TABLE A. One row per TABLE A Tier-ID. No tier may be omitted.)*

| Tier-ID | Error code or signal | Retry-After present? (Y/N) | Retry-After surfaced to caller? (Y/N) | Visible in run history? (Y/N/SILENT) | Failure if Retry-After ignored |
|---------|---------------------|---------------------------|--------------------------------------|--------------------------------------|-------------------------------|
| T-01 | | | | | |
| T-02 | | | | | |

*Violation type (Annot-05): plain-description substitution — "request fails" in place
of "HTTP 429" or named platform signal identifier fails precision.*

**TABLE D — UNPROTECTED BURST PATHS**

*(Source: TABLE A. At least one row. If no gap: >=2 named controls as evidence.)*

| Path-ID | Entry component | Tier-IDs involved | Gap reason or named controls | Consequence at burst volume |
|---------|----------------|-------------------|-----------------------------|-----------------------------|
| P-01 | | | | |

**TABLE E — RISK TAXONOMY**

*(Source: TABLE A + TABLE B + TABLE D. Per-type minimum: >=1 Burst, >=1 Cascade,
>=1 RetryAfter.)*

| Risk-ID | Tier-ID | Type | Risk description | Severity (H/M/L) |
|---------|---------|------|-----------------|-----------------|
| R-01 | | Burst | | |
| R-02 | | Cascade | | |
| R-03 | | RetryAfter | | |

*Violation type (Annot-06): category-absence-undetectable — risk list without Type
column with named taxonomy and per-type minimum-row constraint fails C-22 even if all
categories happen to appear.*

---

**TYPE SCAN GATE**

**Purpose annotation (C-26) — three fields:**

- **Failure mode prevented:** Category elision — a risk type absent from TABLE E
  detectable only by full table scan after TABLE F is complete.
- **Gap above C-22:** C-22 defines what the finished output must contain. This gate
  makes an incomplete TABLE E a construction-time blocking condition. C-22 ensures the
  structure; the gate ensures the missing-category failure mode cannot be produced by
  any valid execution path.
- **Audit test (C-28, C-31):**
  - *Gate-present audit method — 5 observables:* Locate **TYPE SCAN GATE** between
    TABLE E's last R-NN and TABLE F header. Confirm: (1) `Burst: [Y / N]`, (2)
    `Cascade: [Y / N]`, (3) `RetryAfter: [Y / N]` before gate decision. (4) `PROCEED`
    or `BLOCKED` after all three. (5) TABLE F header and MR-01 after gate decision.
    All 5 confirmed = gate compliance verified.
  - *Gate-absent signature — 1 observable:* No **TYPE SCAN GATE** header in the gap
    between TABLE E's last R-NN and MR-01.

**Escape route for C-26 — "the gate Purpose annotation is redundant because C-22 already
explains why type coverage matters" (C-32):** This reasoning conflates the purpose of
the type taxonomy (C-22) with the purpose of the gate (construction-time blocking).

Scan TABLE E for type completeness:
- Burst: [at least one row present? Y / N]
- Cascade: [at least one row present? Y / N]
- RetryAfter: [at least one row present? Y / N]

If all Y: PROCEED
If any N: BLOCKED — return to TABLE E, add the missing type row, re-run this gate.

ROLE 2 COMPLETE. The Consequence Analyst (Role 3) activates subject to the activation
conditions below.

---

**ROLE 3 — CONSEQUENCE ANALYST**

**ROLE 3 ACTIVATION CONDITIONS (C-36):**

Role 3 activates only after PROCEED is stated at the TYPE SCAN GATE AND the following
observable counts are confirmed at this boundary:

- Gate-present path — 5 observables required before Role 3 opens:
  (1) `Burst: Y` verdict line present
  (2) `Cascade: Y` verdict line present
  (3) `RetryAfter: Y` verdict line present
  (4) `PROCEED` gate decision line present
  (5) TABLE F section header and MR-01 not yet produced
  All 5 confirmed = Role 3 may activate.

- Gate-absent path — 1 observable confirms non-activation:
  (1) No `[Category]: [Y / N]` verdict lines between TABLE E's last R-NN and this
  boundary. Gate absent — return to Role 2, complete TYPE SCAN GATE.

You are the Consequence Analyst. Your scope is TABLE F and the global criterion-coverage
step. You are bound by the OUTPUT FORMAT CONTRACT above.

**TABLE F — MITIGATION REGISTRY**

*(Source: TABLE E. One row per TABLE E risk. No risk may be omitted.)*

| MR-ID | Source (Risk-ID) | Gap type | Component | Setting or API parameter | Change | Expected outcome | Tradeoff |
|-------|-----------------|----------|-----------|--------------------------|--------|-----------------|---------|
| MR-01 | | | | | | | |
| MR-02 | | | | | | | |

*Violation type (Annot-07): category-of-action substitution — "add retry logic" in place
of a specific parameter identifier such as `connector.retryPolicy`. A row naming a
category cannot be applied without further research; a row naming an exact parameter
can be applied immediately.*

PROHIBITED: adding rows to TABLE E after TABLE F has opened. — *prevents retroactive
risk injection*

---

**GLOBAL CRITERION-COVERAGE STEP**

Named dedicated step. Not embedded prose. Reports per-criterion PASS/FAIL.

- C-01 (Primary bottleneck with causal reason): [PASS / FAIL]
- C-02 (Backpressure propagation >=2 hops with mechanism): [PASS / FAIL]
- C-03 (>=2 tiers with enforcing component and scope): [PASS / FAIL]
- C-04 (UX at each throttle tier): [PASS / FAIL]
- C-05 (Unprotected burst path): [PASS / FAIL]

[prose: item 3 — global criterion-coverage verdict notes] State FAIL rationale for any
criterion above that did not pass.

ROLE 3 COMPLETE.

---

---

## V-05 — Combined Axes: All Three (Table inventory + SHALL register + activation count + ANNOTATION SCAN GATE)

**Axes:** (1) Output format — Section C as table (per V-02). (2) Phrasing register —
SHALL/PROHIBITED in Section C (per V-03). (3) Role sequence — Role 2 activation confirms
annotation inventory count (per V-04). Addition: ANNOTATION SCAN GATE between TABLE A
and Phase 2, mirroring the TYPE SCAN GATE pattern — confirms all 7 Annot-IDs are present
at their anchor sites before claims analysis opens.

**Hypothesis:** C-37 PASS with maximum enforcement. The ANNOTATION SCAN GATE converts
annotation dropout from a role-activation concern into a construction-time blocking
condition: a missing annotation at its anchor site blocks Phase 2 from opening, exactly
as a missing risk type blocks TABLE F from opening at the TYPE SCAN GATE. The gate's
purpose annotation (three-field C-26 format) explains: failure mode prevented =
annotation dropout creating silent precision gaps in claims output; gap above C-37 =
C-37 requires the inventory to be sealed in FORMAT CONTRACT but does not require a
construction-time enforcement gate; the ANNOTATION SCAN GATE adds the blocking mechanism
that C-37 alone cannot provide. This is the strongest structural enforcement available
for annotation completeness.

**v14 predicted scoring:** C-37 PASS. C-35 PASS. C-36 PASS. Composite: 235/235.

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
   coverage step. Scope: one sentence per failed criterion. Authorized by C-19.

Any prose passage outside these three declared scopes is a format violation detectable
without content review.

**Section B — STRUCTURED OUTPUT REGISTER (C-25, C-27)**

| Element type | Canonical form | Prose? | C-23 tag required? |
|-------------|---------------|--------|-------------------|
| Gate decision lines | PROCEED / BLOCKED | No | No |
| Cross-artifact header lines | "One row per [source]. No [item] may be omitted." | No | No |
| Phase boundary prohibition lines | "PROHIBITED: [data class] — [failure mode]" | No | No |
| Per-criterion verdict lines | "C-NN: PASS / FAIL" | No | No |

No other element types are added to this register without revising this contract.

**Inertia annotation for C-27 — why the register must be declared closed — 3 fields: Failure mode prevented | Gap above C-25 | Concrete example (C-29, C-30):**

- **Failure mode prevented:** Implicit-complement classification — an executor reasoning
  that the complement of Section A is implicitly structured output. Under an open
  register, classification is by content-based inference rather than register membership.
  This is the content-inspection problem C-25 was designed to eliminate.
- **Gap above C-25:** C-25 requires enumeration with explicit Prose? and C-23-tag
  classifications but does not require the register to declare itself exhaustive. The
  closure declaration converts implicit-exempt to explicitly-unclassified. Adding a new
  type requires a named revision, auditable by change history.
- **Concrete example (C-30):** A load-shape verdict label — "FLAT-LOAD: within nominal
  band" — matches none of the four registered canonical forms. Under a closed register,
  this element type is unregistered, its classifications explicitly unresolved, and
  adding it requires a named contract revision.

**Section C — ANNOTATION INVENTORY (C-18, C-37)**

The annotations below SHALL appear at the named anchor sites in the prompt body.
PROHIBITED: omitting any annotation from its declared anchor site — *prevents annotation
dropout; a missing annotation converts a detectable precision-site failure mode into a
silent gap; dropout is a FORMAT CONTRACT violation detectable at this inventory without
body scan*.

Expected row count: 7. Role 2 SHALL confirm all 7 Annot-IDs at their anchor sites via
the ANNOTATION SCAN GATE before Phase 2 opens. Annotation dropout at any anchor site
blocks Phase 2.

| Annot-ID | Anchor site | Failure-mode label | Prohibited form (example) |
|----------|------------|-------------------|--------------------------|
| Annot-01 | TABLE A — `Limit (number + unit)` column definition | vague-label substitution | "limited" or "throttled" in place of "1,200 req/min" |
| Annot-02 | TABLE A — `Binding?` column definition | assertion-without-causal-reason | Binding? = Y with no mechanism named |
| Annot-03 | TABLE A — `Failure mode` column definition | insufficient-categorical-diversity | Fewer than two distinct values across rows |
| Annot-04 | TABLE B — `Mechanism` column definition | generic-term substitution | "blocked" or "throttled" in place of "queue-fill" |
| Annot-05 | TABLE C — `Error code or signal` column definition | plain-description substitution | "request fails" in place of "HTTP 429" |
| Annot-06 | TABLE E — `Type` column definition | category-absence-undetectable | Risk list without Type column with named taxonomy |
| Annot-07 | TABLE F — `Setting or API parameter` column definition | category-of-action substitution | "add retry logic" in place of `connector.retryPolicy` |

This table is closed. No row is added without revising this contract.

FORMAT CONTRACT COMPLETE

---

**ROLE 2 — DOMAIN EXPERT**

**ROLE 2 ACTIVATION CONDITIONS (C-37 enforcement — annotation inventory pre-confirmation):**

Role 2 activates only after FORMAT CONTRACT COMPLETE is stated AND the following
annotation-inventory pre-confirmation is completed at this boundary. This is a pre-Phase-1
check — not a Phase 1 step. Confirm that the prompt body contains all 7 Annot-IDs at
their anchor sites as declared in Section C:

- Pre-confirm annotation inventory — 7 annotations required:
  (1) Annot-01 at TABLE A `Limit (number + unit)` column definition
  (2) Annot-02 at TABLE A `Binding?` column definition
  (3) Annot-03 at TABLE A `Failure mode` column definition
  (4) Annot-04 at TABLE B `Mechanism` column definition
  (5) Annot-05 at TABLE C `Error code or signal` column definition
  (6) Annot-06 at TABLE E `Type` column definition
  (7) Annot-07 at TABLE F `Setting or API parameter` column definition
  All 7 pre-confirmed = Role 2 may proceed to Phase 1.
  Any Annot-ID absent = Role 2 activation blocked. Restore the missing annotation
  at its anchor site, re-confirm all 7, then proceed.

You are a Connectors / Power Automate throughput domain expert. The OUTPUT FORMAT
CONTRACT from Role 1 governs all output you produce.

Simulate throughput across the rate-limited system described in the signal. Treat the
stated request volume as 1x nominal; also analyze at 2x and 5x.

**PHASE 1 ENTRY CONDITION:** Phase 1 opens only after Role 2 activation conditions are
confirmed.

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
filled.)*

| Tier-ID | Component | Limit (number + unit) | Source-ID | Scope | STATUS 1x | STATUS 2x | STATUS 5x | Binding? | Failure mode |
|---------|-----------|----------------------|-----------|-------|-----------|-----------|-----------|----------|-------------|
| T-01 | | | | | | | | | |
| T-02 | | | | | | | | | |
| ... | | | | | | | | | |

Column notes:
- `Tier-ID` — T-01, T-02, ... Use verbatim in every downstream table.
- `Limit (number + unit)` — specific number with unit. *Violation type (Annot-01):
  vague-label substitution — "limited" or "throttled" in place of a specific number
  with unit fails precision.*
- `STATUS Nx` — OK / HIT / SAT. Must shift between at least two bands.
- `Binding?` — exactly one Y. *Violation type (Annot-02): assertion-without-causal-reason
  — Binding? = Y without named causal mechanism.*
- `Failure mode` — hard rejection / queue saturation / silent drop / degraded throughput /
  timeout. *Violation type (Annot-03): insufficient-categorical-diversity — fewer than
  two distinct values across rows.*

PROHIBITED: introducing a new T-NN in any Phase 2 section. — *prevents scope creep*

**[prose: item 1 — binding-tier causal reason]** State why the Binding? = Y tier fails
before all others under 1x nominal load. Name the specific causal mechanism.

**[prose: item 2 — binding constraint exclusivity]** For at least one Binding? = N tier,
name the mechanism that prevents it from binding before the primary tier.

---

**ANNOTATION SCAN GATE**

**Purpose annotation (C-26 format — three fields):**

- **Failure mode prevented:** Annotation dropout — a precision-site annotation (Annot-01
  through Annot-07) is absent from its anchor site in the body but detectable only by
  full body scan after Phase 2 is complete. At that point, the downstream analysis
  contains precision violations with no inline detection signal — the failure mode
  propagated silently through all tables. Two artifacts require revision: the annotation
  anchor site and every downstream table that referenced the precision-failing column.
- **Gap above C-37:** C-37 requires the annotation inventory to be sealed in FORMAT
  CONTRACT before execution begins. C-37 compliance does not require a construction-time
  enforcement gate. An executor who reasons "C-37 already seals the inventory — this
  gate is extra process" conflates the contract-lock mechanism (inventory sealed before
  execution) with the enforcement mechanism (annotation dropout blocked at construction
  time). C-37 ensures the inventory exists; this gate ensures annotation dropout cannot
  be produced by any valid execution path.
- **Audit test:**
  - *Gate-present audit method — 7 observables:* Locate the section titled **ANNOTATION
    SCAN GATE**. Structural position: between Phase 1B's last TABLE A row and the Phase 2
    section header. Confirm 7 observables in sequence: (1) `Annot-01: [Y / N]` before
    gate decision. (2) `Annot-02: [Y / N]` before gate decision. (3) `Annot-03: [Y / N]`
    before gate decision. (4) `Annot-04: [Y / N]` before gate decision. (5)
    `Annot-05: [Y / N]` before gate decision. (6) `Annot-06: [Y / N]` before gate
    decision. (7) `Annot-07: [Y / N]` before gate decision. Then: PROCEED or BLOCKED
    after all 7 verdict lines. All 7 confirmed before PROCEED = gate compliance verified
    by count-scan.
  - *Gate-absent signature — 1 observable:* No **ANNOTATION SCAN GATE** header in the
    structural gap between Phase 1B's last TABLE A row and the Phase 2 section header.

Scan prompt body for annotation completeness:
- Annot-01 at TABLE A `Limit (number + unit)` column definition: [present? Y / N]
- Annot-02 at TABLE A `Binding?` column definition: [present? Y / N]
- Annot-03 at TABLE A `Failure mode` column definition: [present? Y / N]
- Annot-04 at TABLE B `Mechanism` column definition: [present? Y / N]
- Annot-05 at TABLE C `Error code or signal` column definition: [present? Y / N]
- Annot-06 at TABLE E `Type` column definition: [present? Y / N]
- Annot-07 at TABLE F `Setting or API parameter` column definition: [present? Y / N]

If all Y: PROCEED
If any N: BLOCKED — restore the missing annotation at its anchor site, re-run this gate.

---

**PHASE 2 — CLAIMS PHASE**

PROHIBITED: opening Phase 2 before Phase 1B is complete AND the ANNOTATION SCAN GATE
returns PROCEED. — *prevents annotation-dropout propagation into claims analysis*

**For each tier in TABLE A (C-17):** every downstream derived table must include a row
for every T-NN. Coverage verifiable by T-NN count match.

**TABLE B — BACKPRESSURE PROPAGATION TRACE**

*(Source: TABLE A. Two hops minimum.)*

| Hop | From (Tier-ID) | To component | Mechanism | Observable effect |
|-----|----------------|--------------|-----------|-------------------|
| 1 | | | | |
| 2 | | | | |
| ... | | | | |

Mechanism values: queue-fill, connection-hold, retry-amplification, dependency-stall,
timeout-cascade. *Violation type (Annot-04): generic-term substitution — "blocked" or
"throttled" in place of a named mechanism from the permitted set.*

**TABLE C — USER EXPERIENCE CATALOG**

*(Source: TABLE A. One row per TABLE A Tier-ID. No tier may be omitted.)*

| Tier-ID | Error code or signal | Retry-After present? (Y/N) | Retry-After surfaced to caller? (Y/N) | Visible in run history? (Y/N/SILENT) | Failure if Retry-After ignored |
|---------|---------------------|---------------------------|--------------------------------------|--------------------------------------|-------------------------------|
| T-01 | | | | | |
| T-02 | | | | | |

*Violation type (Annot-05): plain-description substitution — "request fails" in place
of "HTTP 429" or named platform signal identifier fails precision.*

**TABLE D — UNPROTECTED BURST PATHS**

*(Source: TABLE A. At least one row. If no gap: >=2 named controls as evidence.)*

| Path-ID | Entry component | Tier-IDs involved | Gap reason or named controls | Consequence at burst volume |
|---------|----------------|-------------------|-----------------------------|-----------------------------|
| P-01 | | | | |

**TABLE E — RISK TAXONOMY**

*(Source: TABLE A + TABLE B + TABLE D. Per-type minimum: >=1 Burst, >=1 Cascade,
>=1 RetryAfter.)*

| Risk-ID | Tier-ID | Type | Risk description | Severity (H/M/L) |
|---------|---------|------|-----------------|-----------------|
| R-01 | | Burst | | |
| R-02 | | Cascade | | |
| R-03 | | RetryAfter | | |

*Violation type (Annot-06): category-absence-undetectable — risk list without Type
column with named taxonomy and per-type minimum-row constraint fails C-22 even if all
categories happen to appear.*

---

**TYPE SCAN GATE**

**Purpose annotation (C-26) — three fields:**

- **Failure mode prevented:** Category elision — a risk type absent from TABLE E
  detectable only by full table scan after TABLE F is complete.
- **Gap above C-22:** C-22 defines what the finished output must contain. This gate
  makes an incomplete TABLE E a construction-time blocking condition. C-22 ensures the
  structure; the gate ensures the missing-category failure mode cannot be produced by
  any valid execution path.
- **Audit test (C-28, C-31):**
  - *Gate-present audit method — 5 observables:* Locate **TYPE SCAN GATE** between
    TABLE E's last R-NN and TABLE F header. Confirm: (1) `Burst: [Y / N]`, (2)
    `Cascade: [Y / N]`, (3) `RetryAfter: [Y / N]` before gate decision. (4) `PROCEED`
    or `BLOCKED` after all three. (5) TABLE F header and MR-01 after gate decision.
    All 5 confirmed = gate compliance verified.
  - *Gate-absent signature — 1 observable:* No **TYPE SCAN GATE** header in the gap
    between TABLE E's last R-NN and MR-01.

**Escape route for C-26 — "the gate Purpose annotation is redundant because C-22 already
explains why type coverage matters" (C-32):** This reasoning conflates the purpose of
the type taxonomy (C-22) with the purpose of the gate (construction-time blocking).

Scan TABLE E for type completeness:
- Burst: [at least one row present? Y / N]
- Cascade: [at least one row present? Y / N]
- RetryAfter: [at least one row present? Y / N]

If all Y: PROCEED
If any N: BLOCKED — return to TABLE E, add the missing type row, re-run this gate.

ROLE 2 COMPLETE. The Consequence Analyst (Role 3) activates subject to the activation
conditions below.

---

**ROLE 3 — CONSEQUENCE ANALYST**

**ROLE 3 ACTIVATION CONDITIONS (C-36):**

Role 3 activates only after PROCEED is stated at the TYPE SCAN GATE AND the following
observable counts are confirmed at this boundary:

- Gate-present path — 5 observables required before Role 3 opens:
  (1) `Burst: Y` verdict line present
  (2) `Cascade: Y` verdict line present
  (3) `RetryAfter: Y` verdict line present
  (4) `PROCEED` gate decision line present
  (5) TABLE F section header and MR-01 not yet produced
  All 5 confirmed = Role 3 may activate.

- Gate-absent path — 1 observable confirms non-activation:
  (1) No `[Category]: [Y / N]` verdict lines between TABLE E's last R-NN and this
  boundary. Gate absent — return to Role 2, complete TYPE SCAN GATE.

You are the Consequence Analyst. Your scope is TABLE F and the global criterion-coverage
step. You are bound by the OUTPUT FORMAT CONTRACT above.

**TABLE F — MITIGATION REGISTRY**

*(Source: TABLE E. One row per TABLE E risk. No risk may be omitted.)*

| MR-ID | Source (Risk-ID) | Gap type | Component | Setting or API parameter | Change | Expected outcome | Tradeoff |
|-------|-----------------|----------|-----------|--------------------------|--------|-----------------|---------|
| MR-01 | | | | | | | |
| MR-02 | | | | | | | |

*Violation type (Annot-07): category-of-action substitution — "add retry logic" in place
of a specific parameter identifier such as `connector.retryPolicy`. A row naming a
category cannot be applied without further research; a row naming an exact parameter
can be applied immediately.*

PROHIBITED: adding rows to TABLE E after TABLE F has opened. — *prevents retroactive
risk injection*

---

**GLOBAL CRITERION-COVERAGE STEP**

Named dedicated step. Not embedded prose. Reports per-criterion PASS/FAIL.

- C-01 (Primary bottleneck with causal reason): [PASS / FAIL]
- C-02 (Backpressure propagation >=2 hops with mechanism): [PASS / FAIL]
- C-03 (>=2 tiers with enforcing component and scope): [PASS / FAIL]
- C-04 (UX at each throttle tier): [PASS / FAIL]
- C-05 (Unprotected burst path): [PASS / FAIL]

[prose: item 3 — global criterion-coverage verdict notes] State FAIL rationale for any
criterion above that did not pass.

ROLE 3 COMPLETE.
