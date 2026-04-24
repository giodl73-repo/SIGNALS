# flow-throttle Variate — Round 15

**Date:** 2026-03-16
**Rubric:** v15 (C-01 through C-40, N_essential=5, N_recommended=3, N_aspirational=32)
**Max composite:** 250 | **Baseline ceiling:** R14 best (235/235 under v14; 235/250 under v15 — C-38, C-39, C-40 FAIL)

---

## State Analysis: What R14 Has vs. What R15 Must Add

**R14 coverage under v15 (assessed):**
- C-01 through C-37: all pass (best R14 variant)
- C-38: FAIL — no annotation count declared at Section C header; completeness requires reading all annotation entries, not a count-scan
- C-39: FAIL — partial closure ("This table is closed. No row is added without revising this contract.") does not include the second canonical sentence: "An annotation not listed here does not exist as a contract requirement."
- C-40: FAIL — no PROHIBITED clause embedded in the annotation inventory itself; V-03's PROHIBITED appears at Section C open as a blanket directive, not as an annotation-inventory-level clause with an inline failure-mode annotation

**C-38 / C-39 / C-40 gap in R14:**

R14's best variants (V-02, V-04) carry the annotation inventory as a table with "Expected row count: 7" and the partial closure. C-38 requires the count to appear in the table header as a declared expectation ("This section declares 7 required annotations") — not in a caption or as a note below the table. The count must be declared *before* enumeration so a reader can verify completeness by count-scan rather than annotation-content inspection.

C-39's canonical closure requires both sentences:
1. "This inventory is closed. An annotation not listed here does not exist as a contract requirement."
2. Bidirectional: what is in the inventory *is* a contract requirement; what is not in it *is not*.

The second sentence is what makes C-39 structurally distinct from the Section B closure (C-27). Section B's closure converts implicit-exempt to explicitly-unclassified. Section C's closure converts annotation-presence from a content-preference to a contract-violation-by-omission — the first sentence prohibits the executor from expanding the inventory; the second sentence prohibits the executor from treating an inventory item as optional.

C-40's PROHIBITED clause must be embedded in the annotation inventory section and must carry an inline annotation (parenthetical or italicized) naming the specific failure mode the clause prevents. V-03's placement (PROHIBITED at Section C open, before the annotation list) does not satisfy C-40 because it is structurally a section-level directive, not an inventory-close clause. C-40 requires a dropout prohibition that is part of the inventory's closure logic — appearing after the annotation table and before FORMAT CONTRACT COMPLETE.

**Single axes to test:**
1. **Output format** — Section C header declares count in explicit sentence form; canonical C-39 closure (both sentences); no PROHIBITED clause. Tests C-38 + C-39 in isolation.
2. **Phrasing register** — Full three additions in Section C: count declaration, canonical closure, PROHIBITED dropout clause with inline failure-mode annotation. Single-step test of all three on a minimal Section C change.
3. **Lifecycle emphasis** — PROHIBITED clause moved to a named sub-block immediately before FORMAT CONTRACT COMPLETE. Count and closure in Section C. Tests whether C-40's "annotation inventory includes" requires co-location in Section C or permits a named sub-block at the FORMAT CONTRACT close.

**Combined axes for V-04 and V-05:**
- V-04: Role sequence + phrasing register — all three (C-38 + C-39 + C-40) in Section C; Role 2 activation conditions add annotation count verification as an observable before Phase 1 opens.
- V-05: All three axes — count + closure + PROHIBITED in Section C; annotation count at Role 2 activation; ANNOTATION SCAN GATE before TABLE F with per-annotation dropout prohibition tokens.

---

## V-01 — Single Axis: Output Format (count declared at header; C-38 + C-39; no C-40)

**Axis:** Section C header adds an explicit count sentence before the annotation table ("This section declares 7 required annotations"). Canonical C-39 closure added with both sentences. No PROHIBITED dropout clause at inventory close. Role architecture and activation conditions unchanged from R14 V-02.

**Hypothesis:** C-38 PASS — count declared in header before enumeration; completeness is count-scan verifiable. C-39 PASS — canonical two-sentence closure present. C-40 FAIL — no PROHIBITED dropout clause in the inventory section. Composite: 235 + 5 + 5 = 245/250 (C-38 + C-39 pass, C-40 fail).

**v15 predicted scoring:** C-38 PASS. C-39 PASS. C-40 FAIL. All prior C-01–C-37 carry. Composite: 245/250.

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

**Inertia annotation for C-27 — why the register must be declared closed — 3 fields:
Failure mode prevented | Gap above C-25 | Concrete example (C-29, C-30):**

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
- **Concrete example (C-30):** A load-shape verdict label — "FLAT-LOAD: within nominal
  band" — matches none of the four registered canonical forms (PROCEED/BLOCKED; "One row
  per [source]..."; "PROHIBITED: [data] — [failure mode]"; "C-NN: PASS / FAIL"). Under
  a closed register, the inference is foreclosed: this element type is unregistered, its
  classifications are explicitly unresolved, and adding it requires a named contract
  revision.

**Section C — ANNOTATION INVENTORY (C-18, C-37)**

This section declares 7 required annotations. Completeness verification: count the rows
in the table below; the expected row count is 7. A row count below 7 indicates a missing
annotation requirement — this section is incomplete and FORMAT CONTRACT COMPLETE may not
be stated.

The following table lists every required annotation by anchor identifier and failure-mode
label. A row absent from this table does not exist as a contract requirement. A row
present in this table whose annotation is absent from its anchor site in the body is a
FORMAT CONTRACT violation detectable by anchor-ID lookup without content scan.

| Annot-ID | Anchor site | Failure-mode label | Prohibited form (example) |
|----------|------------|-------------------|--------------------------|
| Annot-01 | TABLE A — `Limit (number + unit)` column definition | vague-label substitution | "limited" or "throttled" in place of "1,200 req/min" |
| Annot-02 | TABLE A — `Binding?` column definition | assertion-without-causal-reason | Binding? = Y with no mechanism named |
| Annot-03 | TABLE A — `Failure mode` column definition | insufficient-categorical-diversity | Fewer than two distinct values across rows |
| Annot-04 | TABLE B — `Mechanism` column definition | generic-term substitution | "blocked" or "throttled" in place of "queue-fill" |
| Annot-05 | TABLE C — `Error code or signal` column definition | plain-description substitution | "request fails" in place of "HTTP 429" |
| Annot-06 | TABLE E — `Type` column definition | category-absence-undetectable | Risk list without Type column with named taxonomy |
| Annot-07 | TABLE F — `Setting or API parameter` column definition | category-of-action substitution | "add retry logic" in place of `connector.retryPolicy` |

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
  - *Gate-present audit method — 5 observables:* Locate **TYPE SCAN GATE** between
    TABLE E's last R-NN row and TABLE F header. Confirm: (1) `Burst: [Y / N]`, (2)
    `Cascade: [Y / N]`, (3) `RetryAfter: [Y / N]` — all before gate decision. (4)
    `PROCEED` or `BLOCKED` after all three verdict lines. (5) TABLE F header and MR-01
    after gate decision. All 5 confirmed = gate compliance verified.
  - *Gate-absent signature — 1 observable:* No **TYPE SCAN GATE** header in the gap
    between TABLE E's last R-NN and MR-01.

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
`connector.retryPolicy`. A row naming a category cannot be applied without further
research; a row naming an exact parameter can be applied immediately.*

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

## V-02 — Single Axis: Phrasing Register (count + canonical closure + PROHIBITED dropout; all three C-38/39/40)

**Axis:** Section C carries all three additions in a single phrasing-register change: count declaration in the section opening line (C-38), canonical two-sentence closure (C-39), and a PROHIBITED dropout clause at inventory close with an inline failure-mode annotation (C-40). No change to role architecture or activation conditions from V-01.

**Hypothesis:** C-38 PASS + C-39 PASS + C-40 PASS — the PROHIBITED clause at inventory close with parenthetical failure-mode annotation satisfies C-40's requirement that the inventory itself contain the prohibition and name the failure mode it prevents. The count in the opening line satisfies C-38. The canonical two-sentence closure satisfies C-39. Composite: 250/250.

**v15 predicted scoring:** C-38 PASS. C-39 PASS. C-40 PASS. Composite: 250/250.

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

**Inertia annotation for C-27 — why the register must be declared closed — 3 fields:
Failure mode prevented | Gap above C-25 | Concrete example (C-29, C-30):**

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

This section declares 7 required annotations. Count-scan verification: expected rows = 7;
a row count below 7 is a completeness gap detectable without reading annotation content.

| Annot-ID | Anchor site | Failure-mode label | Prohibited form (example) |
|----------|------------|-------------------|--------------------------|
| Annot-01 | TABLE A — `Limit (number + unit)` column definition | vague-label substitution | "limited" or "throttled" in place of "1,200 req/min" |
| Annot-02 | TABLE A — `Binding?` column definition | assertion-without-causal-reason | Binding? = Y with no mechanism named |
| Annot-03 | TABLE A — `Failure mode` column definition | insufficient-categorical-diversity | Fewer than two distinct values across rows |
| Annot-04 | TABLE B — `Mechanism` column definition | generic-term substitution | "blocked" or "throttled" in place of "queue-fill" |
| Annot-05 | TABLE C — `Error code or signal` column definition | plain-description substitution | "request fails" in place of "HTTP 429" |
| Annot-06 | TABLE E — `Type` column definition | category-absence-undetectable | Risk list without Type column with named taxonomy |
| Annot-07 | TABLE F — `Setting or API parameter` column definition | category-of-action substitution | "add retry logic" in place of `connector.retryPolicy` |

This inventory is closed. An annotation not listed here does not exist as a contract
requirement. An annotation listed here that is absent from its anchor site in the body
is a FORMAT CONTRACT violation.

PROHIBITED: annotation dropout at any anchor site listed in this inventory — *prevents
handoff-boundary gap: an annotation absent from its anchor site is detectable only by
full body scan; this clause converts dropout into a FORMAT CONTRACT violation identifiable
by anchor-ID lookup at this inventory without traversing the body*

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
- `Limit (number + unit)` — specific number with unit. *Violation type (Annot-01):
  vague-label substitution — "limited" or "throttled" in place of a specific number
  with unit fails precision.*
- `STATUS Nx` — OK / HIT / SAT. Must shift between at least two bands.
- `Binding?` — exactly one Y. *Violation type (Annot-02): assertion-without-causal-reason
  — Binding? = Y without named causal mechanism.*
- `Failure mode` — hard rejection / queue saturation / silent drop / degraded throughput /
  timeout. *Violation type (Annot-03): insufficient-categorical-diversity — fewer than
  two distinct values across rows.*

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

## V-03 — Single Axis: Lifecycle Emphasis (PROHIBITED clause in named sub-block before FORMAT CONTRACT COMPLETE)

**Axis:** Section C has count declaration (C-38) and canonical two-sentence closure (C-39). The PROHIBITED dropout clause is extracted from Section C and placed in a named sub-block — **ANNOTATION DROPOUT PROHIBITION** — positioned immediately after Section C and before FORMAT CONTRACT COMPLETE. The sub-block carries the inline failure-mode annotation. Tests whether C-40's "annotation inventory includes a PROHIBITED clause" requires physical co-location inside Section C, or permits a named inventory-close block within the FORMAT CONTRACT.

**Hypothesis:** C-38 PASS (count in Section C header). C-39 PASS (canonical closure in Section C). C-40 — contested. If C-40 reads "includes" as "co-located in the inventory table block", this fails. If "includes" means "part of the inventory's closure logic, sealed before FORMAT CONTRACT COMPLETE", this passes. The variation isolates the co-location requirement.

**v15 predicted scoring:** C-38 PASS. C-39 PASS. C-40 contested (likely FAIL if "includes" is co-location-strict). Composite: 245/250 (optimistic) or 245/250 (same as V-01).

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

**Inertia annotation for C-27 — why the register must be declared closed — 3 fields:
Failure mode prevented | Gap above C-25 | Concrete example (C-29, C-30):**

- **Failure mode prevented:** Implicit-complement classification — an executor reasoning
  that the complement of Section A's prose-permitted list is implicitly structured output.
  Under an open register, an executor encountering an unlisted element type classifies by
  content-based inference rather than register membership.
- **Gap above C-25:** C-25 requires the register to enumerate element types with explicit
  Prose? and C-23-tag classifications but does not require the register to declare itself
  exhaustive. The closure declaration converts implicit-exempt to explicitly-unclassified.
  Adding a new type requires an explicit revision, auditable by change history.
- **Concrete example (C-30):** A load-shape verdict label — "FLAT-LOAD: within nominal
  band" — matches none of the four registered canonical forms. Under a closed register,
  the inference is foreclosed: this element type is unregistered, and adding it requires
  a named contract revision.

**Section C — ANNOTATION INVENTORY (C-18, C-37)**

This section declares 7 required annotations. Completeness is count-verifiable: expected
rows = 7.

| Annot-ID | Anchor site | Failure-mode label | Prohibited form (example) |
|----------|------------|-------------------|--------------------------|
| Annot-01 | TABLE A — `Limit (number + unit)` column definition | vague-label substitution | "limited" or "throttled" in place of "1,200 req/min" |
| Annot-02 | TABLE A — `Binding?` column definition | assertion-without-causal-reason | Binding? = Y with no mechanism named |
| Annot-03 | TABLE A — `Failure mode` column definition | insufficient-categorical-diversity | Fewer than two distinct values across rows |
| Annot-04 | TABLE B — `Mechanism` column definition | generic-term substitution | "blocked" or "throttled" in place of "queue-fill" |
| Annot-05 | TABLE C — `Error code or signal` column definition | plain-description substitution | "request fails" in place of "HTTP 429" |
| Annot-06 | TABLE E — `Type` column definition | category-absence-undetectable | Risk list without Type column with named taxonomy |
| Annot-07 | TABLE F — `Setting or API parameter` column definition | category-of-action substitution | "add retry logic" in place of `connector.retryPolicy` |

This inventory is closed. An annotation not listed here does not exist as a contract
requirement. An annotation listed here that is absent from its anchor site in the body
is a FORMAT CONTRACT violation.

**ANNOTATION DROPOUT PROHIBITION**

PROHIBITED: omitting any annotation from the anchor site declared in Section C — *prevents
silent precision-site gap: annotation dropout converts a detectable format violation into
a body-scan-only defect; this prohibition seals the inventory as a closure condition of
the FORMAT CONTRACT — any annotation in Section C that is absent from its declared anchor
site is a dropout violation, discoverable at this boundary without scanning the body*

FORMAT CONTRACT COMPLETE

---

**ROLE 2 — DOMAIN EXPERT**

You are a Connectors / Power Automate throughput domain expert. The OUTPUT FORMAT
CONTRACT from Role 1 governs all output you produce. You are bound by Section A,
Section B, Section C, and the ANNOTATION DROPOUT PROHIBITION and may not modify the
contract.

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

## V-04 — Combined Axes: Role Sequence + Phrasing Register (all three C-38/39/40 in Section C; count at Role 2 activation)

**Axes:** (1) Phrasing register — Section C carries all three: count declaration (C-38), canonical two-sentence closure (C-39), PROHIBITED dropout with inline failure-mode annotation (C-40). (2) Role sequence — Role 2 ACTIVATION CONDITIONS add an annotation count verification observable: before Phase 1 opens, the executor confirms the Section C annotation inventory count matches the declared expectation of 7.

**Hypothesis:** C-38 PASS + C-39 PASS + C-40 PASS. Additionally, the annotation count appears at the Role 2 activation boundary as the 6th observable — tests whether this strengthens C-36 (role-activation completeness) without breaking it. The count-verification at activation converts annotation dropout from a contract violation (detected at FORMAT CONTRACT handoff) into a role-activation failure (detected before the role body opens).

**v15 predicted scoring:** C-38 PASS. C-39 PASS. C-40 PASS. C-36 PASS (6th observable at activation, count-verifiable). Composite: 250/250.

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

**Inertia annotation for C-27 — why the register must be declared closed — 3 fields:
Failure mode prevented | Gap above C-25 | Concrete example (C-29, C-30):**

- **Failure mode prevented:** Implicit-complement classification — an executor reasoning
  that the complement of Section A's prose-permitted list is implicitly structured output.
  Under an open register, an executor encountering an unlisted element type classifies by
  content-based inference rather than by register membership.
- **Gap above C-25:** C-25 requires the register to enumerate element types with explicit
  Prose? and C-23-tag classifications but does not require the register to declare itself
  exhaustive. The closure declaration converts implicit-exempt to explicitly-unclassified.
  Adding a new type requires an explicit revision, auditable by change history.
- **Concrete example (C-30):** A load-shape verdict label — "FLAT-LOAD: within nominal
  band" — matches none of the four registered canonical forms. Under a closed register,
  this element type is unregistered, its classifications are explicitly unresolved, and
  adding it requires a named contract revision.

**Section C — ANNOTATION INVENTORY (C-18, C-37)**

This section declares 7 required annotations. Count-scan verification: expected rows = 7;
a row count below 7 is a completeness gap detectable without reading annotation content.
Role 2 activation confirms this count before Phase 1 opens.

| Annot-ID | Anchor site | Failure-mode label | Prohibited form (example) |
|----------|------------|-------------------|--------------------------|
| Annot-01 | TABLE A — `Limit (number + unit)` column definition | vague-label substitution | "limited" or "throttled" in place of "1,200 req/min" |
| Annot-02 | TABLE A — `Binding?` column definition | assertion-without-causal-reason | Binding? = Y with no mechanism named |
| Annot-03 | TABLE A — `Failure mode` column definition | insufficient-categorical-diversity | Fewer than two distinct values across rows |
| Annot-04 | TABLE B — `Mechanism` column definition | generic-term substitution | "blocked" or "throttled" in place of "queue-fill" |
| Annot-05 | TABLE C — `Error code or signal` column definition | plain-description substitution | "request fails" in place of "HTTP 429" |
| Annot-06 | TABLE E — `Type` column definition | category-absence-undetectable | Risk list without Type column with named taxonomy |
| Annot-07 | TABLE F — `Setting or API parameter` column definition | category-of-action substitution | "add retry logic" in place of `connector.retryPolicy` |

This inventory is closed. An annotation not listed here does not exist as a contract
requirement. An annotation listed here that is absent from its anchor site in the body
is a FORMAT CONTRACT violation.

PROHIBITED: annotation dropout at any anchor site listed in this inventory — *prevents
handoff-boundary gap: an annotation absent from its anchor site is detectable only by
full body scan; this clause converts dropout into a FORMAT CONTRACT violation identifiable
by anchor-ID lookup at this inventory without traversing the body*

FORMAT CONTRACT COMPLETE

---

**ROLE 2 — DOMAIN EXPERT**

You are a Connectors / Power Automate throughput domain expert. The OUTPUT FORMAT
CONTRACT from Role 1 governs all output you produce. You are bound by Section A,
Section B, and Section C and may not modify the contract.

Simulate throughput across the rate-limited system described in the signal. Treat the
stated request volume as 1x nominal; also analyze at 2x and 5x.

**PHASE 1 ENTRY CONDITION:** Phase 1 opens only after FORMAT CONTRACT COMPLETE is stated
AND the following pre-Phase 1 annotation check is confirmed:

Annotation inventory count check — confirm Section C row count = 7 before Phase 1 opens:
- Section C annotation inventory rows present: [count them; expected = 7]
- If count = 7: annotation inventory complete — proceed to Phase 1.
- If count < 7: annotation inventory incomplete — FORMAT CONTRACT COMPLETE was stated
  prematurely; return to Role 1, complete Section C, re-state FORMAT CONTRACT COMPLETE.

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
- `Limit (number + unit)` — specific number with unit. *Violation type (Annot-01):
  vague-label substitution — "limited" or "throttled" in place of a specific number
  with unit fails precision.*
- `STATUS Nx` — OK / HIT / SAT. Must shift between at least two bands.
- `Binding?` — exactly one Y. *Violation type (Annot-02): assertion-without-causal-reason
  — Binding? = Y without named causal mechanism.*
- `Failure mode` — hard rejection / queue saturation / silent drop / degraded throughput /
  timeout. *Violation type (Annot-03): insufficient-categorical-diversity — fewer than
  two distinct values across rows.*

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

## V-05 — Combined Axes: All Three (count + closure + PROHIBITED in Section C; count at activation; ANNOTATION SCAN GATE before TABLE F)

**Axes:** (1) Output format — Section C table with count declared and per-row Dropout-prohibited? column (C-38 at maximum structural completeness). (2) Phrasing register — canonical two-sentence closure (C-39) + PROHIBITED dropout with per-annotation inline failure-mode annotations (C-40 at maximum specificity). (3) Role sequence — Role 2 activation confirms annotation count from Section C. (4) Lifecycle emphasis — ANNOTATION SCAN GATE added before TABLE F: scans each Section C annotation against its anchor site before the mitigation registry opens, parallel to the TYPE SCAN GATE structure.

**Hypothesis:** C-38 PASS + C-39 PASS + C-40 PASS at maximum structural depth. The ANNOTATION SCAN GATE makes annotation dropout a construction-time blocking condition (parallel to TYPE SCAN GATE for category elision), adding a second enforcement layer. If the scorecard reveals that C-40 requires per-annotation dropout tokens rather than a single inventory-level PROHIBITED clause, this variation covers that. The per-row Dropout-prohibited? column converts each row into a named contract commitment rather than an inventory entry.

**v15 predicted scoring:** C-38 PASS. C-39 PASS. C-40 PASS. Composite: 250/250. Excellence candidate for discovering C-41 (if annotation-scan gate is a new observable that the scorecard rewards).

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

**Inertia annotation for C-27 — why the register must be declared closed — 3 fields:
Failure mode prevented | Gap above C-25 | Concrete example (C-29, C-30):**

- **Failure mode prevented:** Implicit-complement classification — an executor reasoning
  that the complement of Section A's prose-permitted list is implicitly structured output.
  Under an open register, an executor encountering an unlisted element type classifies by
  content-based inference rather than by register membership.
- **Gap above C-25:** C-25 requires the register to enumerate element types with explicit
  Prose? and C-23-tag classifications but does not require the register to declare itself
  exhaustive. The closure declaration converts implicit-exempt to explicitly-unclassified.
  Adding a new type requires an explicit revision, auditable by change history.
- **Concrete example (C-30):** A load-shape verdict label — "FLAT-LOAD: within nominal
  band" — matches none of the four registered canonical forms. Under a closed register,
  this element type is unregistered, its classifications are explicitly unresolved, and
  adding it requires a named contract revision.

**Section C — ANNOTATION INVENTORY (C-18, C-37)**

This section declares 7 required annotations. Count-scan verification: expected rows = 7.
A row count below 7 is a completeness gap detectable without reading annotation content.
Role 2 activation confirms this count at the role boundary before Phase 1 opens.

PROHIBITED: annotation dropout at any anchor site in this inventory — *prevents
handoff-boundary gap: an annotation absent from its anchor site converts a detectable
FORMAT CONTRACT violation into a body-scan-only defect; dropout is non-recoverable at
the handoff boundary without this prohibition*

| Annot-ID | Anchor site | Failure-mode label | Prohibited form (example) | Dropout-prohibited? |
|----------|------------|-------------------|--------------------------|---------------------|
| Annot-01 | TABLE A — `Limit (number + unit)` column definition | vague-label substitution | "limited" or "throttled" in place of "1,200 req/min" | YES — *omitting this annotation makes vague-label substitution undetectable at TABLE A without body scan* |
| Annot-02 | TABLE A — `Binding?` column definition | assertion-without-causal-reason | Binding? = Y with no mechanism named | YES — *omitting this annotation makes assertion-without-causal-reason undetectable at TABLE A without body scan* |
| Annot-03 | TABLE A — `Failure mode` column definition | insufficient-categorical-diversity | Fewer than two distinct values across rows | YES — *omitting this annotation makes insufficient-categorical-diversity undetectable at TABLE A without body scan* |
| Annot-04 | TABLE B — `Mechanism` column definition | generic-term substitution | "blocked" or "throttled" in place of "queue-fill" | YES — *omitting this annotation makes generic-term substitution undetectable at TABLE B without body scan* |
| Annot-05 | TABLE C — `Error code or signal` column definition | plain-description substitution | "request fails" in place of "HTTP 429" | YES — *omitting this annotation makes plain-description substitution undetectable at TABLE C without body scan* |
| Annot-06 | TABLE E — `Type` column definition | category-absence-undetectable | Risk list without Type column with named taxonomy | YES — *omitting this annotation makes category-absence-undetectable undetectable at TABLE E without body scan* |
| Annot-07 | TABLE F — `Setting or API parameter` column definition | category-of-action substitution | "add retry logic" in place of `connector.retryPolicy` | YES — *omitting this annotation makes category-of-action substitution undetectable at TABLE F without body scan* |

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

**PHASE 1 ENTRY CONDITION:** Phase 1 opens only after FORMAT CONTRACT COMPLETE is stated
AND the following pre-Phase 1 annotation count check is confirmed:

Annotation count check — Section C declares 7 annotations. Confirm before Phase 1 opens:
- Section C annotation inventory rows present: [count; expected = 7]
- If count = 7: PROCEED to Phase 1.
- If count < 7: Section C is incomplete. FORMAT CONTRACT COMPLETE was stated prematurely.
  Return to Role 1, complete Section C to 7 rows, re-state FORMAT CONTRACT COMPLETE.

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
- `Limit (number + unit)` — a specific number with a unit (e.g., "1,200 req/min").
  *Violation type (Annot-01): vague-label substitution — a label such as "limited" or
  "throttled" in place of a specific number with unit fails precision.*
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

*(Source: TABLE A. At least one row. If no gap: name >=2 controls as evidence.)*

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
  - *Gate-present audit method — 5 observables:* Locate **TYPE SCAN GATE** between
    TABLE E's last R-NN row and TABLE F header. Confirm: (1) `Burst: [Y / N]`, (2)
    `Cascade: [Y / N]`, (3) `RetryAfter: [Y / N]` — all before gate decision. (4)
    `PROCEED` or `BLOCKED` after all three verdict lines. (5) TABLE F header and MR-01
    after gate decision. All 5 confirmed = gate compliance verified.
  - *Gate-absent signature — 1 observable:* No **TYPE SCAN GATE** header in the gap
    between TABLE E's last R-NN and MR-01.

**Escape route for C-26 — "the gate Purpose annotation is redundant because C-22 already
explains why type coverage matters" (C-32):** This reasoning conflates the purpose of
the type taxonomy (C-22) with the purpose of the gate (construction-time blocking). The
annotation makes the gate's distinct purpose auditable and non-dismissible.

Scan TABLE E for type completeness:
- Burst: [at least one row present? Y / N]
- Cascade: [at least one row present? Y / N]
- RetryAfter: [at least one row present? Y / N]

If all Y: PROCEED to ANNOTATION SCAN GATE.
If any N: BLOCKED — return to TABLE E, add the missing type row, re-run this gate.

---

**ANNOTATION SCAN GATE**

**Purpose annotation — three fields:**

- **Failure mode prevented:** Annotation dropout — a Section C annotation absent from
  its anchor site in the body, detectable only by full body scan after all tables are
  complete. At that point the output is finished and the annotation gap is a silent defect.
- **Gap above Section C PROHIBITED clause:** The PROHIBITED: annotation dropout clause
  in Section C is a contract declaration. This gate is the construction-time enforcement:
  it makes annotation dropout a blocking condition before TABLE F opens, converting a
  post-hoc detectable violation into a pre-TABLE-F blocking failure.
- **Audit test — 7 observables:** Locate the **ANNOTATION SCAN GATE** section. Confirm
  one scan-line per Annot-ID in sequence: (1) `Annot-01: [present? Y / N]`, (2)
  `Annot-02: [Y / N]`, (3) `Annot-03: [Y / N]`, (4) `Annot-04: [Y / N]`, (5)
  `Annot-05: [Y / N]`, (6) `Annot-06: [Y / N]`, (7) `Annot-07: [Y / N]`. Gate
  decision line `PROCEED` or `BLOCKED` after all 7. All 8 observables confirmed = gate
  compliance verified by count-scan.

Scan each Section C annotation against its declared anchor site:
- Annot-01 (TABLE A `Limit` column): [annotation present at anchor? Y / N]
- Annot-02 (TABLE A `Binding?` column): [annotation present at anchor? Y / N]
- Annot-03 (TABLE A `Failure mode` column): [annotation present at anchor? Y / N]
- Annot-04 (TABLE B `Mechanism` column): [annotation present at anchor? Y / N]
- Annot-05 (TABLE C `Error code or signal` column): [annotation present at anchor? Y / N]
- Annot-06 (TABLE E `Type` column): [annotation present at anchor? Y / N]
- Annot-07 (TABLE F `Setting or API parameter` column): [annotation present at anchor? Y / N]

If all Y: PROCEED
If any N: BLOCKED — return to the named anchor site, add the missing annotation, re-run
this gate.

ROLE 2 COMPLETE. The Consequence Analyst (Role 3) activates subject to the activation
conditions below.

---

**ROLE 3 — CONSEQUENCE ANALYST**

**ROLE 3 ACTIVATION CONDITIONS (C-36):**

Role 3 activates only after PROCEED is stated at the TYPE SCAN GATE AND PROCEED is
stated at the ANNOTATION SCAN GATE AND the following observable counts are confirmed:

- Gate-present path — 7 observables required before Role 3 opens:
  (1) `Burst: Y` verdict line present at TYPE SCAN GATE
  (2) `Cascade: Y` verdict line present at TYPE SCAN GATE
  (3) `RetryAfter: Y` verdict line present at TYPE SCAN GATE
  (4) `PROCEED` gate decision line at TYPE SCAN GATE
  (5) `PROCEED` gate decision line at ANNOTATION SCAN GATE
  (6) All 7 Annot-NN scan lines showing Y at ANNOTATION SCAN GATE
  (7) TABLE F section header and MR-01 not yet produced
  Confirming all 7 observables by count-scan is a Role 3 entry condition.

- Gate-absent path — 1 observable confirms non-activation:
  (1) No `Annot-NN: [Y / N]` scan lines between TYPE SCAN GATE and this boundary.
  ANNOTATION SCAN GATE absent — return to Role 2, complete the gate, re-confirm
  activation conditions.

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
`connector.retryPolicy`. A row naming a category cannot be applied without further
research; a row naming an exact parameter can be applied immediately.*

PROHIBITED: adding rows to TABLE E after TABLE F has opened. — *prevents retroactive
risk injection; return to Role 2, complete TABLE E, re-run TYPE SCAN GATE and
ANNOTATION SCAN GATE, re-confirm activation conditions, re-open TABLE F*

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
