# flow-throttle Variate — Round 18 (v17 rubric, C-01 through C-44)
**Date:** 2026-03-15
**Rubric:** v17 (C-01 through C-44, N_essential=5, N_recommended=3, N_aspirational=36)
**Baseline ceiling:** R17 V-05 (passes C-01 through C-44; composite 110/110)

---

## State Analysis: What R17 Established vs. What R18 Must Add

**R17 V-05 coverage under v17 (confirmed):**
- C-01 through C-44: all pass — composite 110/110
- C-44 achieved by correcting entries 10 and 11 in the C-41 audit table:
  - Entry 10: `STEP 4 C-24 format requirement: — *Violation type* field non-conflation directive`
    (verbatim bold header `**C-24 format requirement:**`)
  - Entry 11: `STEP 4 C-13 compliance — Tier-ID threading: — *Violation type* field non-conflation directive`
    (verbatim bold header `**C-13 compliance — Tier-ID threading:**`)
- Total enforcement directives in R17 V-05: **11** (6 named blocks + 5 embedded directives)
- Total precision sites in R17 V-05: **6**

**R18 innovation — 7th precision site:**

R18 introduces TABLE B `Mechanism` column as a 7th precision site, located at Step 2A. This
site is inserted at document-order position 3 (after TABLE A `Load-shape verdict` at Step 1B
and before TABLE F `Setting or API parameter` at Step 2H). The insertion:

1. Adds a row to the PRECISION-SITE INVENTORY (site 3 in document order, shifting former
   sites 3-6 to positions 4-7)
2. Extends TABLE B column definitions with a `Mechanism` column definition block containing
   a `*Violation type*` field and a MUST NOT non-conflation directive
3. Increases total embedded directives from 5 to 6 (total directives from 11 to **12**)
4. Adds a **6th embedded directive** row to the C-41 audit table

The verbatim structural label for the new embedded directive is **`TABLE B \`Mechanism\` column`**
(derived from TABLE B's column header row, exactly as it appears in the prompt body).

**Updated verbatim containing-structure label inventory for R18:**

| # | Embedded directive location | Verbatim structural label in prompt body | R17 V-05 citation | R18 site # |
|---|----------------------------|------------------------------------------|-------------------|------------|
| 1 | TABLE A `Load-shape verdict` *Violation type* field | Column header `Load-shape verdict` in TABLE A | `TABLE A \`Load-shape verdict\` column` — PASS ✓ | Site 2 |
| 2 | TABLE B `Mechanism` *Violation type* field | Column header `Mechanism` in TABLE B | (not present in R17) | Site 3 — NEW |
| 3 | TABLE F `Setting or API parameter` *Violation type* field | Column header `Setting or API parameter` in TABLE F | `TABLE F \`Setting or API parameter\` column` — PASS ✓ | Site 4 |
| 4 | PRECISION-SITE INVENTORY parenthetical obligation | Section header `PRECISION-SITE INVENTORY` | `PRECISION-SITE INVENTORY` — PASS ✓ | (inventory) |
| 5 | STEP 4 C-24 format requirement: *Violation type* field | Bold sub-header `C-24 format requirement:` | `STEP 4 C-24 format requirement:` — PASS ✓ | Site 5 |
| 6 | STEP 4 C-13 compliance — Tier-ID threading: *Violation type* field | Bold sub-header `C-13 compliance — Tier-ID threading:` | `STEP 4 C-13 compliance — Tier-ID threading:` — PASS ✓ | Site 6 |
| 7 | STEP 4 C-19 compliance *Violation type* field | Bold sub-header `C-19 compliance — distributed reminder audit:` | (embedded, site 7) | Site 7 |

**Neighbor-relationship updates due to 7th precision site insertion:**

- **TABLE A `Load-shape verdict`** (site 2): right neighbor changes from TABLE F (old site 3)
  to TABLE B `Mechanism` (new site 3) — mechanism-taxonomy failure replaces parameter-specificity
  failure as the right-neighbor contrast.
- **TABLE F `Setting or API parameter`** (new site 4): left neighbor changes from TABLE A
  `Load-shape verdict` (old site 2) to TABLE B `Mechanism` (new site 3) — mechanism-taxonomy
  failure replaces deferred-verdict failure as the left-neighbor contrast.
- **STEP 4 C-24 format requirement:** (new site 5): left neighbor is still TABLE F but now
  site 4 (was site 3); right neighbor is still C-13 compliance but now site 6 (was site 5).
- **STEP 4 C-13 compliance — Tier-ID threading:** (new site 6): left neighbor is C-24 at site 5
  (was site 4); right neighbor is C-19 at site 7 (was site 6).
- **STEP 4 C-19 compliance — distributed reminder audit:** (new site 7): left neighbor is C-13
  at site 6 (was site 5); "Site 7 has one immediate neighbor" (was "Site 6...").

**Total enforcement directives in R18 V-03/V-04/V-05: 12**

Named blocks (6, same as R17):
1. REGISTRY GAP PROHIBITION — Failure 5 prevention (C-17)
2. Step 2A — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19)
3. Step 2C — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19)
4. Step 2E — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19)
5. Step 2G — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19)
6. Failure 2 + Failure 6 prevention (C-16, C-20, C-23, C-26) — CLASSIFICATION REQUIRED AT STEP 1B

Embedded directives (6, was 5 in R17):
7. TABLE A `Load-shape verdict` column — *Violation type* field non-conflation directive
8. TABLE B `Mechanism` column — *Violation type* field non-conflation directive (NEW)
9. TABLE F `Setting or API parameter` column — *Violation type* field non-conflation directive
10. PRECISION-SITE INVENTORY — inventory verification obligation (parenthetical note)
11. STEP 4 C-24 format requirement: — *Violation type* field non-conflation directive
12. STEP 4 C-13 compliance — Tier-ID threading: — *Violation type* field non-conflation directive

*(Note: the C-19 compliance *Violation type* field is embedded at site 7 but is the 12th
directive in R17's 11-count too — its MUST NOT clause is present and counted in C-43. No
change to its count status.)*

---

## Round 18 Variation Map

| Var | Axes | C-43/C-44 mechanism | Predicted |
|-----|------|---------------------|-----------|
| V-01 | Phrasing register — no 7th site, entry 10 colon dropped | 11 directives; "STEP 4 C-24 format requirement" (no colon) instead of "STEP 4 C-24 format requirement:" | C-44 FAIL (~109.44) |
| V-02 | Output format — no 7th site, entry 11 case mismatch | 11 directives; "STEP 4 C-13 Compliance — Tier-ID threading:" (capital C) instead of "STEP 4 C-13 compliance — Tier-ID threading:" | C-44 FAIL (~109.44) |
| V-03 | Lifecycle emphasis — 7th site added, 12th directive undiscovered | 12 directives in prompt; C-41 audit has only 11 rows; entry 8 (TABLE B `Mechanism` column) missing | C-43 FAIL (~109.44) |
| V-04 | Role sequence — 7th site added, 12th directive paraphrased | 12 directives; entry 8 = "Step 2A backpressure hop mechanism field" (not verbatim) | C-44 FAIL (~109.44) |
| V-05 | All combined — 7th site, all 12 directives verbatim | All 6 embedded entries verbatim including entry 8 = "TABLE B `Mechanism` column" | C-43 + C-44 PASS (110/110) |

**Single-axis questions:**

Q1 (V-01 vs R17 V-05): Does omitting the trailing colon from "STEP 4 C-24 format requirement"
fail C-44? The verbatim bold header in the prompt body is "**C-24 format requirement:**" — the
colon is part of the structural label as declared. Hypothesis: yes — "STEP 4 C-24 format
requirement" without the colon is not the verbatim label; C-44 requires "the exact text of the
italic field header, table footnote label, table annotation marker, or other structural label."
The colon is integral to the declared header; omitting it makes the citation non-verbatim.
Predicted: C-44 FAIL. Composite = ~109.44/110.

Q2 (V-02 vs V-01): Does capitalizing "Compliance" in "STEP 4 C-13 Compliance — Tier-ID
threading:" fail C-44? The verbatim bold header is "**C-13 compliance — Tier-ID threading:**"
with lowercase c. Hypothesis: yes — case mismatch is a non-verbatim citation; C-44 requires
the exact text including capitalization as it appears in the prompt body. Capital C in
"Compliance" does not match the declared lowercase c in "compliance." Predicted: C-44 FAIL.
Composite = ~109.44/110.

Q3 (V-03 vs V-01): Does adding a 7th precision site (TABLE B `Mechanism` column) with a 12th
enforcement directive but failing to enumerate it in the C-41 audit fail C-43? The TABLE B
`Mechanism` *Violation type* field contains a MUST NOT non-conflation clause in a non-primary-
location position; C-43 requires discovery of all normative-register clauses regardless of
structural location. Hypothesis: yes — the omission of the TABLE B `Mechanism` column entry
from the C-41 audit table fails C-43 (not C-44, since C-44 only applies to discovered but
incorrectly cited entries). Predicted: C-43 FAIL. Composite = ~109.44/110.

Q4 (V-04 vs V-03): Does discovering the 12th directive (entry 8 present) but citing it as
"Step 2A backpressure hop mechanism field" instead of the verbatim "TABLE B `Mechanism` column"
fail C-44? "Step 2A backpressure hop mechanism field" is a positional-contextual description
derived from the surrounding analysis and section name — it is not the verbatim column header
appearing in TABLE B's header row. Hypothesis: yes — C-44 requires the exact containing-
structure label from the prompt body. The TABLE B header row uses the column label `Mechanism`;
the containing-structure citation is "TABLE B `Mechanism` column." Predicted: C-44 FAIL.
Composite = ~109.44/110.

Q5 (V-05): Do the corrected verbatim citations for all 6 embedded entries (including entry 8 =
"TABLE B `Mechanism` column") satisfy C-43 and C-44 without regressions? Hypothesis: yes —
"TABLE B `Mechanism` column" is the exact column header text from TABLE B's header row,
prefixed with the table name for unambiguous location identification, matching the established
pattern for other column-header embedded directives (entries 7 and 9). No structural criteria
are affected by the new site's addition once all neighbor references in *Violation type* fields
are updated to reflect the renumbered sites. Predicted: C-43 PASS, C-44 PASS, composite 110/110.

---

## V-01 — Single Axis: Phrasing Register (Entry 10 Colon Dropped)

**Axis:** Phrasing register — no 7th precision site; C-41 audit table has 11 rows matching
the R17 V-05 structure; entry 10 drops the trailing colon from the verbatim bold header label,
citing "STEP 4 C-24 format requirement" instead of "STEP 4 C-24 format requirement:". Entries
1-9 and 11 retain verbatim structural labels. All other sections are identical to R17 V-05.

**Hypothesis:** The verbatim bold header in the prompt body is "**C-24 format requirement:**"
with a trailing colon; the colon is part of the declared structural label. Citing "STEP 4
C-24 format requirement" (no colon) is not the verbatim label. C-44 requires the exact text
including punctuation. One non-verbatim entry is sufficient to fail C-44. C-43 passes (all 11
discovered); C-42 passes; C-44 fails (entry 10 non-verbatim by colon omission). Predicted:
C-44 FAIL. Composite = ~109.44/110.

---

**THE INERTIA PROBLEM**

Throttle failures reach production undiscovered because the system passed at development and
staging volumes. Teams reason: "it worked in dev" — and skip the analysis. The first
production incident is the discovery mechanism. That is the status quo this skill exists to
displace.

What inertia conceals:
- The burst path that was never rate-limited because no one tested at the volume where it fires
- The missing Retry-After handler that turns a 30-second throttle window into a 10-minute
  retry storm that exhausts quota across the tenant
- The cascade that takes down three dependent flows when a single connector limit fires
- The tier whose limit nobody measured at 5x nominal — the volume a viral workflow hits on
  day one — while everyone assumed the documented limit was the binding constraint
- The integration test suite reporting green because it mocks the connector layer

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
the rate-limited system described in the signal. Treat the stated request volume as 1x
nominal; also analyze at 2x and 5x.

The tables below are the primary output — each carries a distinct finding category that prose
cannot represent with the same auditability. Every cell SHALL be filled. Produce sections in
the order shown.

---

**PRECISION-SITE INVENTORY**

*(Required before any table is defined — C-33 + C-35 + C-37 + C-39. Every precision-requiring
site in this prompt is enumerated below in document order. The `Violation type` column states
the specific failure at each site, matching the domain-specific text that SHALL appear at each
definition site. The `C-27 hierarchy` column uses the C-31 parenthetical labeling format —
`primary (C-27):` for the first site and `extension (C-27 extension):` for all subsequent
sites — making the C-31 labeling structure auditable from this inventory without opening each
definition block.)*

| # | Site | C-27 hierarchy | Required precision | Violation type |
|---|------|----------------|--------------------|----------------|
| 1 | TABLE A `Limit (number + unit)` (Step 1A) | `primary (C-27):` | Numeric rate with unit (e.g., "1,000 req/min") | Vague label substituted for numeric value (e.g., "limited" in place of "1,200 req/min") |
| 2 | TABLE A `Load-shape verdict` (Step 1B) | `extension (C-27 extension):` | SHAPE-NEUTRAL or SHAPE-SENSITIVE recorded at Step 1B | Deferred verdict token — entry routes classification to Step 2G rather than recording verdict at Step 1B |
| 3 | TABLE F `Setting or API parameter` (Step 2H) | `extension (C-27 extension):` | Specific connector setting, policy parameter, or API attribute name | Category of action substituted for named parameter identifier (e.g., "add retry logic" instead of `connector.retryPolicy`) |
| 4 | STEP 4 C-24 finding schema | `extension (C-27 extension):` | All three slots populated: INFORMAL-NAME, SECTION:LOCATION, T-NN | Missing slot identifier — one or more named slot positions absent or collapsed into prose |
| 5 | STEP 4 C-13 audit FAIL entries | `extension (C-27 extension):` | Per-finding identification with specific informal references | Binary FAIL flag without enumeration of the specific informal references found |
| 6 | STEP 4 C-19 audit FAIL entries | `extension (C-27 extension):` | Per-step inline verdict before aggregate | Aggregate verdict without per-step inline verdict sequence |

*(Six precision-requiring sites. Violation types SHALL match the domain-specific text at each
downstream definition site — enabling inventory-vs-definition verification. An executor SHALL
verify that the label at each definition block matches the `C-27 hierarchy` value in this row
before producing that definition block — the inventory value is a compliance target, not a
record.)*

---

**STEP 1 — TIER REGISTRY**

*(What inertia conceals here: the tier whose per-second limit was never measured at 2x or 5x
nominal — the volume nobody tested.)*

Step 1 has two sub-steps. An executor SHALL complete Step 1A and Step 1B in order before
opening any Step 2 section. The registry SHALL be closed only after Step 1B gate is cleared.

**REGISTRY GAP PROHIBITION — Failure 5 prevention (C-17):** Tiers discovered during Step 2
are scope violations — evidence that the enumeration phase was incomplete. PROHIBITED:
assigning a new T-NN during Step 2 as a fill-in step. An executor SHALL return to TABLE A,
register the tier with all columns filled, and SHALL restart from the point of discovery.
This prohibition SHALL be restated at each Step 2 section where mid-phase discovery could
occur.

---

**Step 1A — VOLUME ANALYST: TIER IDENTIFICATION AND LIMITS**

**PHASE ENTRY CONDITION:** Step 1A SHALL be entered after the signal input has been read in
full.

*(Volume analyst role: identify every rate-limiting component; record numeric limit, scope,
volume-band status, binding band, failure visibility window, and recovery time. Leave
`Load-shape verdict` as placeholder — assign at Step 1B.)*

**TABLE A — THROTTLE TIER INVENTORY ACROSS VOLUME BANDS**

| Tier-ID | Component | Limit (number + unit) | Scope | STATUS 1x | STATUS 2x | STATUS 5x | Binding at band | Load-shape verdict | Failure visibility window | Recovery time |
|---------|-----------|----------------------|-------|-----------|-----------|-----------|-----------------|-------------------|--------------------------|---------------|
| T-01    |           |                      |       |           |           |           |                 | [Step 1B]         |                          |               |
| T-02    |           |                      |       |           |           |           |                 | [Step 1B]         |                          |               |
| ...     |           |                      |       |           |           |           |                 | [Step 1B]         |                          |               |

Column definitions:
- `Tier-ID` — Assign T-01, T-02, ... and SHALL be used verbatim in every downstream section.
- `Limit (number + unit)` — a specific number with a unit (e.g., "1,000 req/min").
  - *Violation type: vague label substituted for numeric value (e.g., "limited", "throttled"
    in place of "1,200 req/min"). Site 1 has one immediate right neighbor (site 2:
    Load-shape verdict). Single-adjacency — C-36 and C-38 SHALL NOT apply.*
  - Compliance failure condition `primary (C-27):` An entry using a vague label instead of a
    specific number-with-unit fails this column's precision requirement.
- `STATUS Nx` — OK / HIT / SAT; SHALL shift between at least two bands.
- `Binding at band` — lowest band at which this tier is the primary bottleneck. N/A if never.
- `Failure visibility window` — how quickly saturation becomes observable (time + signal).
- `Recovery time` — how long until normal operation resumes after burst traffic subsides.

**STEP 1A GATE:** Step 1A SHALL be considered closed when: (a) every identified rate-limiting
component in the target flow has a T-NN row in TABLE A; (b) every TABLE A row except
`Load-shape verdict` is populated with non-placeholder values; and (c) the `Limit` column
contains no vague labels. An executor SHALL NOT open Step 1B until this gate is cleared.

**PHASE EXIT CONDITION:** Step 1A is exited when the STEP 1A GATE is cleared.

---

**Step 1B — LOAD-SHAPE ANALYST: CLASSIFICATION**

**PHASE ENTRY CONDITION:** Step 1B SHALL be entered only after the STEP 1A GATE is cleared.

*(Load-shape analyst role activates here. Review each tier's `Limit` entry in TABLE A and
assign the `Load-shape verdict` column for every row. The registry closes after Step 1B.)*

**Failure 2 + Failure 6 prevention (C-16, C-20, C-23, C-26) — CLASSIFICATION REQUIRED AT
STEP 1B:** An executor SHALL assign `Load-shape verdict` for every TABLE A tier at this step.
PROHIBITED: leaving any `Load-shape verdict` cell as placeholder or deferring classification
to the LOAD SHAPE COMPARISON section (Step 2G).

**Escape-route story (C-23):** The escape route is the "STATUS tracks volume thresholds"
frame. TABLE A STATUS columns use OK/HIT/SAT to track whether a tier's volume threshold is
crossed at each band. Because STATUS is a volume-threshold metric, TABLE A appears to be a
pure volume-threshold analysis table — making load-shape classification appear out of scope
for the registry and naturally belonging in the section named "LOAD SHAPE COMPARISON." The
Step 1B sub-step structure itself introduces a second escape route: because Step 1B is a named
analyst sub-step, an executor may reason that classification can be deferred to Step 2G where
"the analyst naturally encounters load patterns." Both frames route shape analysis to Step 2G.

**Structural rejection proof (C-26):** Both frames are structurally self-defeating. Premise 1:
load-shape classification requires the registered `Limit` value at registration time —
available in TABLE A now at Step 1B. Premise 2: Step 2G depends on per-tier Load-shape
verdicts to produce meaningful comparisons. Consequence: deferring to Step 2G creates a
circular dependency where the downstream section that would "receive" shape classification
is itself dependent on the per-tier verdict the registry was supposed to supply. Step 1B
exists precisely to foreclose this dependency.

For each TABLE A tier, update `Load-shape verdict`:
- State SHAPE-NEUTRAL or SHAPE-SENSITIVE
- State the numeric rate differential between uniform and burst arrival at this tier's limit
- State the mechanism that explains the differential

- *Violation type: deferred verdict token — the executor routes the SHAPE-NEUTRAL/
  SHAPE-SENSITIVE classification to Step 2G rather than recording it at Step 1B.
  All-neighbor contrast (C-36): the `Limit` column's violation type (left neighbor, site 1)
  is a value-absence failure — the measured number is missing or replaced by an imprecise
  placeholder. TABLE F `Setting or API parameter`'s violation type (right neighbor, site 3)
  is a parameter-specificity failure — a task category is named where a deployable parameter
  identifier is required. This column's violation type is neither: the value is not absent
  and the failure is not about parameter identity; the failure is purely temporal — the act
  of recording the verdict is deferred to a section that structurally depends on it. Three
  distinct failures at the same registry level, three different corrections: supply the number
  (Limit), move the classification act to Step 1B (this column), name the parameter (TABLE F).
  An executor MUST NOT conflate these 2 failure modes.*
- Compliance failure condition `extension (C-27 extension):` A Load-shape verdict entry left
  blank or deferred ("see Step 2G", "analyzed below") at the end of Step 1B fails the
  registration-time classification requirement and invalidates Step 2G's numeric comparison.

**STEP 1B GATE:** Step 1B SHALL be considered closed when every TABLE A row has a populated
`Load-shape verdict` cell containing a SHAPE-NEUTRAL or SHAPE-SENSITIVE verdict with numeric
differential and mechanism. No placeholder SHALL remain. The registry is closed at this point.

**PHASE EXIT CONDITION:** Step 1B is exited when the STEP 1B GATE is cleared. An executor
SHALL NOT begin STEP 2 until this phase exit condition is met.

---

**STEP 2 — ANALYSIS PHASES**

**PHASE ENTRY CONDITION:** Step 2 SHALL be entered only after the STEP 1B GATE is cleared.
The tier registry is closed. An executor SHALL use T-NN identifiers from TABLE A throughout
all sections below.

---

**Step 2A — BACKPRESSURE PROPAGATION TRACE (TABLE B)**

**PHASE ENTRY CONDITION:** Step 2A SHALL be entered only after TABLE A is closed.

*(What inertia conceals here: the missing Retry-After handler that turns a 30-second throttle
window into a 10-minute retry storm — invisible where the connector layer is mocked.)*

**Step 2A — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19):** Tiers
appearing in backpressure analysis that are not in TABLE A are scope violations. An executor
SHALL NOT assign a new T-NN here. An executor SHALL return to TABLE A (complete Step 1A +
Step 1B), register the tier with all required columns, then continue.

| Hop | From (Tier-ID) | To component | Mechanism | Observable effect |
|-----|----------------|--------------|-----------|-------------------|
| 1   |                |              |           |                   |
| 2   |                |              |           |                   |
| ... |                |              |           |                   |

A minimum of two hops SHALL be present. `Mechanism` SHALL be specific: queue-fill,
connection-hold, retry-amplification, dependency-stall, timeout-cascade.

**PHASE EXIT CONDITION:** Step 2A SHALL be considered closed when at least two hops are
documented with T-NN identifiers and specific mechanisms.

---

**Step 2B — USER EXPERIENCE CATALOG (TABLE C)**

**PHASE ENTRY CONDITION:** Step 2B SHALL be entered after Step 2A PHASE EXIT CONDITION
is cleared. One row per TABLE A Tier-ID. No tier SHALL be omitted.

| Tier-ID | Error code or signal | Retry-After present? (Y/N) | Retry-After surfaced to caller? (Y/N) | Visible in run history? (Y/N/SILENT) | Failure if Retry-After ignored |
|---------|---------------------|---------------------------|--------------------------------------|--------------------------------------|-------------------------------|
| T-01    |                     |                           |                                      |                                      |                               |
| T-02    |                     |                           |                                      |                                      |                               |

---

**Step 2C — UNPROTECTED BURST PATHS (TABLE D)**

**PHASE ENTRY CONDITION:** Step 2C SHALL be entered after Step 2B is closed.

*(What inertia conceals here: the burst path that bypasses rate limiting because no test has
ever run at the volume where it fires.)*

**Step 2C — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19):** Tiers
referenced in burst path analysis that are not in TABLE A are scope violations. An executor
SHALL NOT assign a new T-NN here. An executor SHALL return to TABLE A.

At least one row SHALL be present. If no unprotected path exists, row 1 SHALL state the
conclusion with at least two named controls as evidence.

| Path-ID | Entry component | Gap reason (structural gap or named controls) | Tier-IDs involved | Consequence at burst volume |
|---------|----------------|-----------------------------------------------|-------------------|-----------------------------|
| P-01    |                |                                               |                   |                             |

---

**Step 2D — TIER RISK RANKING**

**PHASE ENTRY CONDITION:** Step 2D SHALL be entered after Step 2C is closed.

All TABLE A tiers SHALL appear in the ranking, ordered by business risk, highest to lowest.
One sentence per tier with rationale SHALL be provided. For the top-ranked tier, `Failure
visibility window` and `Recovery time` from TABLE A SHALL be referenced.

---

**Step 2E — CASCADE SCENARIO**

**PHASE ENTRY CONDITION:** Step 2E SHALL be entered after Step 2D is closed.

**Step 2E — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19):** Tiers
introduced during cascade trace that are not in TABLE A are scope violations. An executor
SHALL NOT assign a new T-NN here. An executor SHALL return to TABLE A.

Trace one concrete cascade from the 1x binding constraint. T-NN identifiers SHALL be used
throughout. Each causal link SHALL be stated explicitly. A minimum of three tiers SHALL be
present, each step caused by the previous.

---

**Step 2F — RETRY-AFTER GAP ASSESSMENT**

**PHASE ENTRY CONDITION:** Step 2F SHALL be entered after Step 2E is closed.

For the 1x binding constraint tier: is Retry-After present and surfaced? If absent, the failure
mode SHALL be named precisely — retry storm (exponential backoff) vs. quota exhaustion
(circuit breaker).

---

**Step 2G — LOAD SHAPE COMPARISON**

**PHASE ENTRY CONDITION:** Step 2G SHALL be entered after Step 2F is closed.

**Step 2G — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19):** Tiers
introduced during load shape analysis that are not in TABLE A are scope violations. An
executor SHALL NOT assign a new T-NN here. An executor SHALL return to TABLE A.

Using TABLE A's Limit values and Load-shape verdict column (classified at Step 1B), compare
1x nominal at two arrival patterns. Identical total count; only arrival distribution differs.

- **UNIFORM arrival** — state per-second arrival rate; state which tiers are HIT or SAT.
- **BURST arrival** — state the burst fraction and peak per-second rate; state which tiers
  are HIT or SAT and why.

At least one numeric comparison where status differs at identical total count SHALL be present.

---

**Step 2H — MITIGATION REGISTRY (TABLE F)**

**PHASE ENTRY CONDITION:** Step 2H SHALL be entered after Step 2G is closed.

A mitigation row that names a category of action ("add retry logic") requires further research
before it can be applied. A row that names the exact parameter can be applied immediately.

| MR-ID | Source | Gap type | Component | Setting or API parameter | Change | Expected outcome |
|-------|--------|----------|-----------|--------------------------|--------|-----------------|
| MR-01 |        |          |           |                          |        |                 |
| MR-02 |        |          |           |                          |        |                 |

`Setting or API parameter` — the exact configuration key, connector property, or API attribute
name SHALL be recorded here.

- *Violation type: category of action substituted for named parameter identifier (e.g.,
  "add retry logic" instead of `connector.retryPolicy`). All-neighbor contrast (C-36): the
  `Load-shape verdict` column's violation type (left neighbor, site 2) is a deferred verdict
  token — the classification act is placed at the wrong moment, routed to Step 2G rather than
  recorded at Step 1B. The STEP 4 C-24 finding schema's violation type (right neighbor, site 4)
  is a structural omission — a labeled slot position within a single finding entry is left
  empty or merged with adjacent content. This column's violation type is neither: the value is
  a string identifier, not a number; there is no timing constraint; and the failure is not
  about a slot within a structured finding. The failure is category substitution — naming the
  class of action where the specific deployable parameter name is required. An executor MUST
  NOT conflate these 2 failure modes.*
- Compliance failure condition `extension (C-27 extension):` A row naming a category of action
  rather than a specific parameter identifier fails this column's precision requirement.

---

**STEP 3 — TEST COVERAGE GAP ANALYSIS**

**PHASE ENTRY CONDITION:** STEP 3 SHALL be entered only after Step 2H is closed.

*(What inertia conceals here: the integration test suite reporting green because it mocks the
connector layer; the load test running at 10% of production concurrency.)*

Execute two stages. Stage 1 SHALL pre-load artifact names; Stage 2 SHALL use them.

**STAGE 1 — TEST INFRASTRUCTURE INVENTORY**

Gate: at least two artifacts SHALL be named with structural properties before Stage 2 opens.

Catalog entry 1:
- **Artifact:** [specific artifact name]
- **Structural property:** [architectural reason it cannot reach the throttle behavior]

Catalog entry 2:
- **Artifact:** [specific artifact name]
- **Structural property:** [architectural reason]

"Stage 1 complete" SHALL be stated before Stage 2 opens.

**TABLE E — TEST COVERAGE GAP REGISTRY**

| GAP-ID | Throttle behavior (Tier-ID + failure mode) | Test type | Structural reason (Stage 1 artifact + property) | Test approach (component + volume + assertion) |
|--------|-------------------------------------------|-----------|--------------------------------------------------|------------------------------------------------|
| GAP-01 |                                           |           |                                                  |                                                |
| GAP-02 |                                           |           |                                                  |                                                |

---

**STEP 4 — INTEGRITY VERIFICATION**

**PHASE ENTRY CONDITION:** STEP 4 SHALL be entered only after Stage 2 of STEP 3 is complete.

**Failure 4 prevention (C-15, C-18, C-22, C-24, C-25) — per-section compliance audit.**
Self-contained block. An executor SHALL complete this block after Stage 2. Each downstream
section SHALL receive an individual verdict on a distinct verdict line, with evidence on a
distinct evidence line.

**C-24 format requirement:** Each field entry SHALL use two distinct labeled lines:
`- Verdict: [PASS / FAIL]`
`- If FAIL — [field label]: [list each finding]`

Each individual finding within a FAIL list MUST populate all three named slots:

```
INFORMAL-NAME:    [exact label used informally in the text]
SECTION:LOCATION: [step name and specific location within the step]
T-NN:             [the registered tier ID it should have referenced]
```

- *Violation type: missing slot identifier in finding entry — one or more named slot positions
  absent or collapsed into prose. All-neighbor contrast (C-36): TABLE F `Setting or API
  parameter`'s violation type (left neighbor, site 3) is category substitution — a task-class
  label occupies the parameter field. The STEP 4 C-13 audit FAIL field's violation type (right
  neighbor, site 5) is evidence absence — a FAIL verdict is issued at the aggregate level
  without enumerating the specific informal references found. This schema's violation type is
  distinct from both: the failure is not a wrong category in a parameter field and not an
  absent evidence list at aggregate level — a labeled slot position within a single finding
  entry is left empty or merged with adjacent content. An executor MUST NOT conflate these
  2 failure modes.*
- Compliance failure condition `extension (C-27 extension):` A finding that omits any named
  slot position — or presents findings as free-form prose — fails the identification schema.

---

**C-13 compliance — Tier-ID threading:**

Step 2A (TABLE B):
- Verdict: [PASS / FAIL]
- If FAIL — informal references found: [list each using the three-slot template above]

Step 2B (TABLE C):
- Verdict: [PASS / FAIL]
- If FAIL — informal references found: [list each using the three-slot template above]

Step 2C (TABLE D):
- Verdict: [PASS / FAIL]
- If FAIL — informal references found: [list each using the three-slot template above]

Step 2D (TIER RISK RANKING):
- Verdict: [PASS / FAIL]
- If FAIL — informal references found: [list each using the three-slot template above]

Step 2E (CASCADE SCENARIO):
- Verdict: [PASS / FAIL]
- If FAIL — informal references found: [list each using the three-slot template above]

Step 2G (LOAD SHAPE COMPARISON):
- Verdict: [PASS / FAIL]
- If FAIL — informal references found: [list each using the three-slot template above]

Unregistered tiers introduced after TABLE A closed:
- Verdict: [PASS / FAIL]
- If FAIL — unregistered tiers found: [list each: "[tier name] introduced at [step]"]

- *Violation type: binary FAIL flag without enumeration of specific informal references.
  Adjacent contrast: the C-24 finding schema's violation type (left neighbor, site 4) is
  structural omission within a finding entry — a labeled slot is missing or collapsed into
  prose. The STEP 4 C-19 audit FAIL field's violation type (right neighbor, site 6) is verdict
  granularity collapse — individual step verdicts are merged into a single aggregate without
  per-step assessments. This audit field's violation type is distinct from both: the failure
  is not within a single finding (C-24's domain) and not about per-step verdict granularity
  (C-19's domain). The failure is at the aggregate reporting level — the FAIL verdict is
  correctly present but the specific informal references are not enumerated. An executor MUST
  NOT conflate these 2 failure modes.*
- Compliance failure condition `extension (C-27 extension):` A FAIL verdict that does not
  enumerate specific informal references fails this audit field.

**C-19 compliance — distributed reminder audit:**

**C-25 format requirement:** Issue an individual inline verdict for each step before the
aggregate failure list.

- Step 2A (TABLE B): [Y — reminder present / N — missing]
- Step 2C (TABLE D): [Y — reminder present / N — missing]
- Step 2E (CASCADE SCENARIO): [Y — reminder present / N — missing]
- Step 2G (LOAD SHAPE COMPARISON): [Y — reminder present / N — missing]
- If any N:
  - Verdict: FAIL
  - Missing steps: [list each step where N was recorded]

- *Violation type: aggregate verdict without per-step inline verdict sequence. Adjacent
  contrast: the C-13 audit field's violation type (left neighbor, site 5) is evidence absence
  on FAIL — a FAIL verdict that correctly fires but names no specific findings. This field's
  violation type is verdict granularity collapse: per-step verdicts are merged into a single
  aggregate before the FAIL branch. C-13 fails on what the FAIL entry contains; C-19 fails
  on whether each step receives its own verdict line. Both fail at the audit level; each
  requires a different correction. Site 6 has one immediate neighbor — C-36 and C-38 do
  not apply.*
- Compliance failure condition `extension (C-27 extension):` A single aggregate verdict
  without per-step inline verdicts fails the C-25 format requirement.

**C-14 compliance — Perspective separation:**
- Verdict: [PASS / FAIL]
- If FAIL — interleaving found: [describe where tier discovery and caller behavior appeared
  in the same step]

**C-40 / C-41 compliance — Per-directive normative-register audit:**

*(C-43 discovery scope: this field covers all SHALL, SHALL NOT, MUST, MUST NOT, and PROHIBITED
obligation clauses in the prompt regardless of structural location — named enforcement block
headers, *Violation type* italic fields, inventory parenthetical notes, and PHASE ENTRY/EXIT
condition blocks. Clauses lacking a standalone block header are named by their containing
structure. Total enforcement directives in this prompt: 11.)*

*(C-44 note: entries 7-9 use verbatim structural labels ✓. Entry 10 drops the trailing colon
from the verbatim bold header: "STEP 4 C-24 format requirement" is cited instead of "STEP 4
C-24 format requirement:" — the verbatim bold header in the prompt body is "**C-24 format
requirement:**" with a trailing colon; omitting the colon makes the citation non-verbatim.
Entry 11 retains verbatim "STEP 4 C-13 compliance — Tier-ID threading:" ✓. C-44 NOT satisfied:
entry 10 omits the trailing colon that is integral to the declared structural label. C-44 FAIL.)*

For each enforcement directive in this prompt, verify that the primary directive uses RFC
2119-style normative language (SHALL, SHALL NOT, MUST, MUST NOT, PROHIBITED). An executor
SHALL enumerate each directive by its verbatim declared block name (for named blocks) or its
containing structure name (for embedded non-primary-location clauses) and record a
per-directive verdict:

| Directive block (verbatim declared name or containing structure) | Primary language used | C-40 verdict |
|-----------------------------------------------------------------|----------------------|-------------|
| REGISTRY GAP PROHIBITION — Failure 5 prevention (C-17) | PROHIBITED / SHALL | [PASS / FAIL] |
| Step 2A — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19) | SHALL NOT | [PASS / FAIL] |
| Step 2C — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19) | SHALL NOT | [PASS / FAIL] |
| Step 2E — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19) | SHALL NOT | [PASS / FAIL] |
| Step 2G — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19) | SHALL NOT | [PASS / FAIL] |
| Failure 2 + Failure 6 prevention (C-16, C-20, C-23, C-26) — CLASSIFICATION REQUIRED AT STEP 1B | PROHIBITED / SHALL | [PASS / FAIL] |
| TABLE A `Load-shape verdict` column — *Violation type* field non-conflation directive | MUST NOT | [PASS / FAIL] |
| TABLE F `Setting or API parameter` column — *Violation type* field non-conflation directive | MUST NOT | [PASS / FAIL] |
| PRECISION-SITE INVENTORY — inventory verification obligation (parenthetical note) | SHALL verify | [PASS / FAIL] |
| STEP 4 C-24 format requirement — *Violation type* field non-conflation directive | MUST NOT | [PASS / FAIL] |
| STEP 4 C-13 compliance — Tier-ID threading: — *Violation type* field non-conflation directive | MUST NOT | [PASS / FAIL] |

If any row is FAIL: state the specific phrase found and its normative replacement.

*(C-41 satisfied: all 11 enforcement directives enumerated with individual per-directive
verdicts. C-42 satisfied: all 6 primary-location directives cited by verbatim declared block
name. C-43 satisfied: all 5 non-primary-location directives discovered. C-44 NOT satisfied:
entry 10 cites "STEP 4 C-24 format requirement" without trailing colon — the verbatim bold
header in the prompt body is "**C-24 format requirement:**" with a trailing colon; omitting
the colon makes the citation non-verbatim. C-44 FAIL.)*

---

## V-02 — Single Axis: Output Format (Entry 11 Case Mismatch)

**Axis:** Output format — no 7th precision site; C-41 audit table has 11 rows; entry 10 uses
the correct verbatim "STEP 4 C-24 format requirement:" (with colon); entry 11 introduces a
case mismatch: "STEP 4 C-13 Compliance — Tier-ID threading:" (capital C in "Compliance")
instead of "STEP 4 C-13 compliance — Tier-ID threading:" (lowercase c). All other sections
are identical to V-01.

**Hypothesis:** The verbatim bold header is "**C-13 compliance — Tier-ID threading:**" with
lowercase c in "compliance." Citing "STEP 4 C-13 Compliance — Tier-ID threading:" uses
capital C, which does not match the declared label. C-44 requires the exact text including
capitalization as it appears in the prompt body. One case-mismatch entry is sufficient to fail
C-44. Predicted: C-44 FAIL. Composite = ~109.44/110.

---

*(THE INERTIA PROBLEM: identical to V-01.)*

*(Role setup: identical to V-01.)*

*(PRECISION-SITE INVENTORY: identical to V-01 — six sites, same hierarchy labels and violation
types, same verification obligation parenthetical.)*

*(STEP 1 — TIER REGISTRY: identical to V-01 structure. REGISTRY GAP PROHIBITION — Failure 5
prevention (C-17) block present. Step 1A GATE and PHASE EXIT CONDITION present. Failure 2 +
Failure 6 prevention (C-16, C-20, C-23, C-26) — CLASSIFICATION REQUIRED AT STEP 1B block
present. Step 1B GATE and PHASE EXIT CONDITION present. All PHASE ENTRY CONDITIONS present.)*

*(STEP 2 through STEP 3: identical to V-01 — all sections present with PHASE ENTRY/EXIT
conditions, all four Standing enforcement reminder blocks at Steps 2A, 2C, 2E, 2G, all
*Violation type* italic fields and C-27 extension compliance failure conditions. TABLE F
`Setting or API parameter` *Violation type* field and C-27 extension failure condition
identical to V-01. No TABLE B column definitions section — identical to V-01.)*

*(STEP 4 — INTEGRITY VERIFICATION through C-14 compliance: identical to V-01 — PHASE ENTRY
CONDITION, Failure 4 prevention block, C-24 format requirement with three-slot code block and
*Violation type* field citing sites 3/4/5 (same as V-01 since no 7th site), C-13 compliance
with per-step verdicts and *Violation type* field citing sites 4/6, C-19 compliance with C-25
format requirement and *Violation type* field citing site 5 and "Site 6 has one immediate
neighbor", C-14 compliance.)*

**C-40 / C-41 compliance — Per-directive normative-register audit:**

*(C-43 discovery scope: identical to V-01. Total enforcement directives: 11.)*

*(C-44 note: entries 7-9 use verbatim structural labels ✓. Entry 10 corrected to verbatim
"STEP 4 C-24 format requirement:" — the exact text of the bold header "**C-24 format
requirement:**" including trailing colon ✓. Entry 11 introduces a case mismatch: "STEP 4
C-13 Compliance — Tier-ID threading:" uses capital C in "Compliance" — the verbatim bold
header is "**C-13 compliance — Tier-ID threading:**" with lowercase c; capitalization is part
of the declared structural label. C-44 NOT satisfied: entry 11 case mismatch. C-44 FAIL.)*

| Directive block (verbatim declared name or containing structure) | Primary language used | C-40 verdict |
|-----------------------------------------------------------------|----------------------|-------------|
| REGISTRY GAP PROHIBITION — Failure 5 prevention (C-17) | PROHIBITED / SHALL | [PASS / FAIL] |
| Step 2A — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19) | SHALL NOT | [PASS / FAIL] |
| Step 2C — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19) | SHALL NOT | [PASS / FAIL] |
| Step 2E — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19) | SHALL NOT | [PASS / FAIL] |
| Step 2G — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19) | SHALL NOT | [PASS / FAIL] |
| Failure 2 + Failure 6 prevention (C-16, C-20, C-23, C-26) — CLASSIFICATION REQUIRED AT STEP 1B | PROHIBITED / SHALL | [PASS / FAIL] |
| TABLE A `Load-shape verdict` column — *Violation type* field non-conflation directive | MUST NOT | [PASS / FAIL] |
| TABLE F `Setting or API parameter` column — *Violation type* field non-conflation directive | MUST NOT | [PASS / FAIL] |
| PRECISION-SITE INVENTORY — inventory verification obligation (parenthetical note) | SHALL verify | [PASS / FAIL] |
| STEP 4 C-24 format requirement: — *Violation type* field non-conflation directive | MUST NOT | [PASS / FAIL] |
| STEP 4 C-13 Compliance — Tier-ID threading: — *Violation type* field non-conflation directive | MUST NOT | [PASS / FAIL] |

If any row is FAIL: state the specific phrase found and its normative replacement.

*(C-41 satisfied: all 11 enforcement directives enumerated with per-directive verdicts. C-42
satisfied: all 6 primary-location directives verbatim. C-43 satisfied: all 5 non-primary
directives discovered. C-44 NOT satisfied: entry 11 cites "STEP 4 C-13 Compliance — Tier-ID
threading:" with capital C — the verbatim bold header is "C-13 compliance — Tier-ID threading:"
with lowercase c. Case mismatch makes the citation non-verbatim. C-44 FAIL.)*

---

## V-03 — Single Axis: Lifecycle Emphasis (7th Site Added, 12th Directive Undiscovered)

**Axis:** Lifecycle emphasis — the prompt adds a 7th precision site (TABLE B `Mechanism`
column at Step 2A) with a 12th enforcement directive (MUST NOT non-conflation clause in the
`Mechanism` column definition); the C-41 audit table has only 11 rows — the entry for
"TABLE B `Mechanism` column" is missing. All other sections that change due to the 7th site
(PRECISION-SITE INVENTORY with 7 rows, TABLE B column definitions, updated neighbor references
in *Violation type* fields) are included correctly. The audit gap is the sole axis.

**Hypothesis:** The TABLE B `Mechanism` *Violation type* field contains a MUST NOT clause;
C-43 requires discovery of all normative-register clauses regardless of structural location.
Failing to enumerate the TABLE B `Mechanism` directive in the C-41 audit table fails C-43
(discovery criterion) — not C-44, because C-44 applies only to directives that were discovered
but cited with non-verbatim labels. Predicted: C-43 FAIL. Composite = ~109.44/110.

---

*(THE INERTIA PROBLEM: identical to V-01.)*

*(Role setup: identical to V-01.)*

**PRECISION-SITE INVENTORY**

*(Required before any table is defined — C-33 + C-35 + C-37 + C-39. Every precision-requiring
site in this prompt is enumerated below in document order. The `Violation type` column states
the specific failure at each site, matching the domain-specific text that SHALL appear at each
definition site. The `C-27 hierarchy` column uses the C-31 parenthetical labeling format —
`primary (C-27):` for the first site and `extension (C-27 extension):` for all subsequent
sites — making the C-31 labeling structure auditable from this inventory without opening each
definition block.)*

| # | Site | C-27 hierarchy | Required precision | Violation type |
|---|------|----------------|--------------------|----------------|
| 1 | TABLE A `Limit (number + unit)` (Step 1A) | `primary (C-27):` | Numeric rate with unit (e.g., "1,000 req/min") | Vague label substituted for numeric value (e.g., "limited" in place of "1,200 req/min") |
| 2 | TABLE A `Load-shape verdict` (Step 1B) | `extension (C-27 extension):` | SHAPE-NEUTRAL or SHAPE-SENSITIVE recorded at Step 1B | Deferred verdict token — entry routes classification to Step 2G rather than recording verdict at Step 1B |
| 3 | TABLE B `Mechanism` (Step 2A) | `extension (C-27 extension):` | Specific named mechanism type from permitted set (queue-fill, connection-hold, retry-amplification, dependency-stall, timeout-cascade) | Generic category label substituted for specific mechanism name (e.g., "blocked" in place of "queue-fill") |
| 4 | TABLE F `Setting or API parameter` (Step 2H) | `extension (C-27 extension):` | Specific connector setting, policy parameter, or API attribute name | Category of action substituted for named parameter identifier (e.g., "add retry logic" instead of `connector.retryPolicy`) |
| 5 | STEP 4 C-24 finding schema | `extension (C-27 extension):` | All three slots populated: INFORMAL-NAME, SECTION:LOCATION, T-NN | Missing slot identifier — one or more named slot positions absent or collapsed into prose |
| 6 | STEP 4 C-13 audit FAIL entries | `extension (C-27 extension):` | Per-finding identification with specific informal references | Binary FAIL flag without enumeration of the specific informal references found |
| 7 | STEP 4 C-19 audit FAIL entries | `extension (C-27 extension):` | Per-step inline verdict before aggregate | Aggregate verdict without per-step inline verdict sequence |

*(Seven precision-requiring sites. Violation types SHALL match the domain-specific text at each
downstream definition site — enabling inventory-vs-definition verification. An executor SHALL
verify that the label at each definition block matches the `C-27 hierarchy` value in this row
before producing that definition block — the inventory value is a compliance target, not a
record.)*

*(STEP 1 — TIER REGISTRY: identical to V-01 structure. REGISTRY GAP PROHIBITION — Failure 5
prevention (C-17) block present. Step 1A table and column definitions. Load-shape verdict
*Violation type* field uses updated right-neighbor reference — see Step 2A section below for
the updated neighbor contrast. STEP 1A GATE, PHASE EXIT CONDITION, Failure 2 + Failure 6
prevention block, escape-route story, structural rejection proof, Load-shape verdict
*Violation type* field, STEP 1B GATE, PHASE EXIT CONDITION: all present and identical to
V-01 except the right-neighbor reference in the Load-shape verdict *Violation type* field.)*

*(The Load-shape verdict *Violation type* field right-neighbor reference changes: "TABLE F
`Setting or API parameter`'s violation type (right neighbor, site 3)" becomes "TABLE B
`Mechanism`'s violation type (right neighbor, site 3) is a mechanism-taxonomy failure — a
generic category occupies the mechanism field where a specific named mechanism type from the
permitted set is required; the failure is value-specificity within a closed set, not temporal
routing and not a missing structural registration. An executor MUST NOT conflate these 2
failure modes.")*

*(STEP 2 PHASE ENTRY CONDITION: identical to V-01.)*

**Step 2A — BACKPRESSURE PROPAGATION TRACE (TABLE B)**

*(PHASE ENTRY CONDITION and enforcement reminder: identical to V-01.)*

| Hop | From (Tier-ID) | To component | Mechanism | Observable effect |
|-----|----------------|--------------|-----------|-------------------|
| 1   |                |              |           |                   |
| 2   |                |              |           |                   |
| ... |                |              |           |                   |

Column definitions:
- `From (Tier-ID)` — SHALL reference a T-NN from TABLE A.
- `Mechanism` — Name the specific throttle propagation mechanism. Permitted values: queue-fill,
  connection-hold, retry-amplification, dependency-stall, timeout-cascade.
  - *Violation type: generic category label substituted for specific mechanism name (e.g.,
    "blocked" or "throttled" in place of "queue-fill"). All-neighbor contrast (C-36): TABLE A
    `Load-shape verdict`'s violation type (left neighbor, site 2) is a deferred verdict token
    — the classification act is routed to Step 2G rather than recorded at Step 1B; the failure
    is temporal, not about specificity of value. TABLE F `Setting or API parameter`'s violation
    type (right neighbor, site 4) is parameter-specificity failure — a task-class label ("add
    retry logic") occupies a field requiring a deployable parameter identifier; the failure is
    about naming the right type of thing (configuration key vs. task description). This column's
    violation type is neither temporal deferral nor parameter-type substitution: the value is
    present at write time, the column is not a registry classification, and the failure is
    specificity within a closed mechanism taxonomy — naming "blocked" where "queue-fill" is
    required. An executor MUST NOT conflate these 2 failure modes.*
  - Compliance failure condition `extension (C-27 extension):` A mechanism entry using a generic
    category label (blocked, throttled, slowed) rather than a specific named mechanism from the
    permitted set fails this column's precision requirement.

**PHASE EXIT CONDITION:** Step 2A SHALL be considered closed when at least two hops are
documented with T-NN identifiers and specific mechanisms.

*(Step 2B through Step 2G: identical to V-01 in structure. All PHASE ENTRY/EXIT conditions,
enforcement reminders, and *Violation type* fields present.)*

**Step 2H — MITIGATION REGISTRY (TABLE F)**

*(PHASE ENTRY CONDITION and table: identical to V-01.)*

`Setting or API parameter` — the exact configuration key, connector property, or API attribute
name SHALL be recorded here.

- *Violation type: category of action substituted for named parameter identifier (e.g.,
  "add retry logic" instead of `connector.retryPolicy`). All-neighbor contrast (C-36): TABLE B
  `Mechanism`'s violation type (left neighbor, site 3) is a mechanism-taxonomy failure — a
  generic category label occupies a field where a specific mechanism name from a closed
  permitted set is required; the failure is value-specificity, not timing and not parameter
  identity. The STEP 4 C-24 format requirement:'s violation type (right neighbor, site 5)
  is a structural omission — a labeled slot position within a single finding entry is left
  empty or merged with adjacent content. This column's violation type is neither: the value is
  a string identifier, not a number; there is no timing constraint; and the failure is not
  about a slot within a structured finding. The failure is category substitution — naming the
  class of action where the specific deployable parameter name is required. An executor MUST
  NOT conflate these 2 failure modes.*
- Compliance failure condition `extension (C-27 extension):` A row naming a category of action
  rather than a specific parameter identifier fails this column's precision requirement.

*(STEP 3: identical to V-01.)*

*(STEP 4 — INTEGRITY VERIFICATION through Failure 4 prevention block: identical to V-01.)*

**C-24 format requirement:** Each field entry SHALL use two distinct labeled lines:
`- Verdict: [PASS / FAIL]`
`- If FAIL — [field label]: [list each finding]`

Each individual finding within a FAIL list MUST populate all three named slots:

```
INFORMAL-NAME:    [exact label used informally in the text]
SECTION:LOCATION: [step name and specific location within the step]
T-NN:             [the registered tier ID it should have referenced]
```

- *Violation type: missing slot identifier in finding entry — one or more named slot positions
  absent or collapsed into prose. All-neighbor contrast (C-36): TABLE F `Setting or API
  parameter`'s violation type (left neighbor, site 4) is category substitution — a task-class
  label occupies the parameter field. The STEP 4 C-13 compliance — Tier-ID threading:'s
  violation type (right neighbor, site 6) is evidence absence — a FAIL verdict is issued at
  the aggregate level without enumerating the specific informal references found. This schema's
  violation type is distinct from both: the failure is not a wrong category in a parameter
  field and not an absent evidence list at aggregate level — a labeled slot position within a
  single finding entry is left empty or merged with adjacent content. An executor MUST NOT
  conflate these 2 failure modes.*
- Compliance failure condition `extension (C-27 extension):` A finding that omits any named
  slot position — or presents findings as free-form prose — fails the identification schema.

---

**C-13 compliance — Tier-ID threading:**

*(Per-step verdict format: identical to V-01.)*

- *Violation type: binary FAIL flag without enumeration of specific informal references.
  Adjacent contrast: the C-24 format requirement:'s violation type (left neighbor, site 5)
  is structural omission within a finding entry — a labeled slot is missing or collapsed into
  prose. The STEP 4 C-19 compliance — distributed reminder audit:'s violation type (right
  neighbor, site 7) is verdict granularity collapse — individual step verdicts are merged into
  a single aggregate without per-step assessments. This audit field's violation type is
  distinct from both: the failure is not within a single finding (C-24's domain) and not about
  per-step verdict granularity (C-19's domain). The failure is at the aggregate reporting level
  — the FAIL verdict is correctly present but the specific informal references are not
  enumerated. An executor MUST NOT conflate these 2 failure modes.*
- Compliance failure condition `extension (C-27 extension):` A FAIL verdict that does not
  enumerate specific informal references fails this audit field.

**C-19 compliance — distributed reminder audit:**

**C-25 format requirement:** Issue an individual inline verdict for each step before the
aggregate failure list.

- Step 2A (TABLE B): [Y — reminder present / N — missing]
- Step 2C (TABLE D): [Y — reminder present / N — missing]
- Step 2E (CASCADE SCENARIO): [Y — reminder present / N — missing]
- Step 2G (LOAD SHAPE COMPARISON): [Y — reminder present / N — missing]
- If any N:
  - Verdict: FAIL
  - Missing steps: [list each step where N was recorded]

- *Violation type: aggregate verdict without per-step inline verdict sequence. Adjacent
  contrast: the C-13 compliance — Tier-ID threading: audit field's violation type (left
  neighbor, site 6) is evidence absence on FAIL — a FAIL verdict that correctly fires but
  names no specific findings. This field's violation type is verdict granularity collapse:
  per-step verdicts are merged into a single aggregate before the FAIL branch. C-13 fails on
  what the FAIL entry contains; C-19 fails on whether each step receives its own verdict line.
  Both fail at the audit level; each requires a different correction. Site 7 has one immediate
  neighbor — C-36 and C-38 do not apply.*
- Compliance failure condition `extension (C-27 extension):` A single aggregate verdict
  without per-step inline verdicts fails the C-25 format requirement.

*(C-14 compliance: identical to V-01.)*

**C-40 / C-41 compliance — Per-directive normative-register audit:**

*(C-43 discovery scope: this field covers all SHALL, SHALL NOT, MUST, MUST NOT, and PROHIBITED
obligation clauses in the prompt regardless of structural location — named enforcement block
headers, *Violation type* italic fields, inventory parenthetical notes, and PHASE ENTRY/EXIT
condition blocks. Clauses lacking a standalone block header are named by their containing
structure. Total enforcement directives in this prompt: 12.)*

*(C-44 note: entries 7-11 use verbatim structural labels ✓; entry 8 is MISSING from the audit
table — the TABLE B `Mechanism` column contains a MUST NOT non-conflation directive that is a
normative-register clause discoverable by C-43 scope; the directive is absent from the
enumeration below. C-43 NOT satisfied: entry 8 undiscovered. C-44 cannot be assessed for
entry 8 because it is not enumerated.)*

For each enforcement directive in this prompt, verify that the primary directive uses RFC
2119-style normative language (SHALL, SHALL NOT, MUST, MUST NOT, PROHIBITED). An executor
SHALL enumerate each directive by its verbatim declared block name (for named blocks) or its
containing structure name (for embedded non-primary-location clauses) and record a
per-directive verdict:

| Directive block (verbatim declared name or containing structure) | Primary language used | C-40 verdict |
|-----------------------------------------------------------------|----------------------|-------------|
| REGISTRY GAP PROHIBITION — Failure 5 prevention (C-17) | PROHIBITED / SHALL | [PASS / FAIL] |
| Step 2A — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19) | SHALL NOT | [PASS / FAIL] |
| Step 2C — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19) | SHALL NOT | [PASS / FAIL] |
| Step 2E — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19) | SHALL NOT | [PASS / FAIL] |
| Step 2G — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19) | SHALL NOT | [PASS / FAIL] |
| Failure 2 + Failure 6 prevention (C-16, C-20, C-23, C-26) — CLASSIFICATION REQUIRED AT STEP 1B | PROHIBITED / SHALL | [PASS / FAIL] |
| TABLE A `Load-shape verdict` column — *Violation type* field non-conflation directive | MUST NOT | [PASS / FAIL] |
| TABLE F `Setting or API parameter` column — *Violation type* field non-conflation directive | MUST NOT | [PASS / FAIL] |
| PRECISION-SITE INVENTORY — inventory verification obligation (parenthetical note) | SHALL verify | [PASS / FAIL] |
| STEP 4 C-24 format requirement: — *Violation type* field non-conflation directive | MUST NOT | [PASS / FAIL] |
| STEP 4 C-13 compliance — Tier-ID threading: — *Violation type* field non-conflation directive | MUST NOT | [PASS / FAIL] |

If any row is FAIL: state the specific phrase found and its normative replacement.

*(C-41 satisfied: all 11 enumerated directives receive per-directive verdicts. C-42 satisfied:
all 6 primary-location directives verbatim. C-43 NOT satisfied: the TABLE B `Mechanism` column
MUST NOT non-conflation directive (the 12th directive in this prompt) is absent from the
enumeration — only 11 of 12 directives are discovered. C-44 cannot be assessed for the missing
entry. C-43 FAIL.)*

---

## V-04 — Single Axis: Role Sequence (7th Site Added, 12th Directive Paraphrased)

**Axis:** Role sequence — the prompt adds a 7th precision site and 12th enforcement directive
(TABLE B `Mechanism` column) identically to V-03; the C-41 audit table has 12 rows — entry 8
is present but uses a positional-contextual description "Step 2A backpressure hop mechanism
field — *Violation type* non-conflation directive" rather than the verbatim containing-
structure label "TABLE B `Mechanism` column — *Violation type* field non-conflation directive."
All other sections with 7th-site changes are identical to V-03.

**Hypothesis:** Entry 8 is present (C-43 satisfied — all 12 directives discovered), but the
citation "Step 2A backpressure hop mechanism field" is a positional-contextual description
derived from the step name and table role rather than the verbatim column header label from
TABLE B's header row. The verbatim label is "TABLE B `Mechanism` column." C-44 requires the
exact containing-structure label from the prompt body; a positional description fails regardless
of how accurate it is as a description. Predicted: C-44 FAIL. Composite = ~109.44/110.

---

*(THE INERTIA PROBLEM: identical to V-01.)*

*(Role setup: identical to V-01.)*

*(PRECISION-SITE INVENTORY: identical to V-03 — seven sites including TABLE B `Mechanism` at
site 3, with updated hierarchy labels and violation type for site 3.)*

*(STEP 1 — TIER REGISTRY: identical to V-03 — includes updated Load-shape verdict *Violation
type* right-neighbor reference to TABLE B `Mechanism` (site 3).)*

*(STEP 2 PHASE ENTRY CONDITION: identical to V-01.)*

*(Step 2A — BACKPRESSURE PROPAGATION TRACE (TABLE B): identical to V-03 — includes TABLE B
column definitions with `Mechanism` *Violation type* field and C-27 extension compliance
failure condition.)*

*(Step 2B through Step 2G: identical to V-03.)*

*(Step 2H — MITIGATION REGISTRY (TABLE F): identical to V-03 — includes updated left-neighbor
reference to TABLE B `Mechanism` (site 3) and updated right-neighbor reference to C-24 format
requirement: (site 5).)*

*(STEP 3: identical to V-01.)*

*(STEP 4 through C-14 compliance: identical to V-03 — includes updated site numbers in all
*Violation type* fields (C-24 at site 5, C-13 at site 6, C-19 at site 7; "Site 7 has one
immediate neighbor").)*

**C-40 / C-41 compliance — Per-directive normative-register audit:**

*(C-43 discovery scope: identical to V-03. Total enforcement directives in this prompt: 12.)*

*(C-44 note: entries 7, 9-12 use verbatim structural labels ✓. Entry 8 is present (C-43
satisfied) but uses a positional descriptor: "Step 2A backpressure hop mechanism field" is
derived from the step name and the table's functional role — it is not the verbatim column
header label "TABLE B `Mechanism` column" as it appears in TABLE B's header row. C-44
requires the exact containing-structure label from the prompt body; "Step 2A backpressure hop
mechanism field" does not appear as a structural label anywhere in the prompt. C-44 NOT
satisfied: entry 8 non-verbatim by positional paraphrase. C-44 FAIL.)*

For each enforcement directive in this prompt, verify that the primary directive uses RFC
2119-style normative language (SHALL, SHALL NOT, MUST, MUST NOT, PROHIBITED). An executor
SHALL enumerate each directive by its verbatim declared block name (for named blocks) or its
containing structure name (for embedded non-primary-location clauses) and record a
per-directive verdict:

| Directive block (verbatim declared name or containing structure) | Primary language used | C-40 verdict |
|-----------------------------------------------------------------|----------------------|-------------|
| REGISTRY GAP PROHIBITION — Failure 5 prevention (C-17) | PROHIBITED / SHALL | [PASS / FAIL] |
| Step 2A — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19) | SHALL NOT | [PASS / FAIL] |
| Step 2C — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19) | SHALL NOT | [PASS / FAIL] |
| Step 2E — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19) | SHALL NOT | [PASS / FAIL] |
| Step 2G — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19) | SHALL NOT | [PASS / FAIL] |
| Failure 2 + Failure 6 prevention (C-16, C-20, C-23, C-26) — CLASSIFICATION REQUIRED AT STEP 1B | PROHIBITED / SHALL | [PASS / FAIL] |
| TABLE A `Load-shape verdict` column — *Violation type* field non-conflation directive | MUST NOT | [PASS / FAIL] |
| Step 2A backpressure hop mechanism field — *Violation type* non-conflation directive | MUST NOT | [PASS / FAIL] |
| TABLE F `Setting or API parameter` column — *Violation type* field non-conflation directive | MUST NOT | [PASS / FAIL] |
| PRECISION-SITE INVENTORY — inventory verification obligation (parenthetical note) | SHALL verify | [PASS / FAIL] |
| STEP 4 C-24 format requirement: — *Violation type* field non-conflation directive | MUST NOT | [PASS / FAIL] |
| STEP 4 C-13 compliance — Tier-ID threading: — *Violation type* field non-conflation directive | MUST NOT | [PASS / FAIL] |

If any row is FAIL: state the specific phrase found and its normative replacement.

*(C-41 satisfied: all 12 enforcement directives enumerated with individual per-directive
verdicts. C-42 satisfied: all 6 primary-location directives verbatim. C-43 satisfied: all 6
non-primary-location directives discovered — 12 total directives, 12 total rows. C-44 NOT
satisfied: entry 8 cites "Step 2A backpressure hop mechanism field" — a positional-contextual
description that does not appear as a structural label in the prompt body; the verbatim TABLE B
column header is `Mechanism` and the containing-structure citation is "TABLE B `Mechanism`
column." C-44 FAIL.)*

---

## V-05 — All Axes Combined (C-43 + C-44 Full Compliance, 7th Precision Site)

**Axis:** Full combination — 7th precision site (TABLE B `Mechanism` column) added with
complete column definitions and MUST NOT non-conflation directive; all neighbor references in
*Violation type* fields updated to reflect renumbered sites (sites 1-7); C-41 audit table has
12 rows with all 6 embedded-directive entries citing verbatim structural labels from the prompt
body, including entry 8 = "TABLE B `Mechanism` column — *Violation type* field non-conflation
directive" (verbatim TABLE B column header, matching the established pattern for entries 7
and 9).

**Hypothesis:** All 6 embedded-directive entries now cite verbatim structural labels from the
prompt body. The new entry 8 uses "TABLE B `Mechanism` column" — the exact column header text
from TABLE B's header row, following the same pattern as "TABLE A `Load-shape verdict` column"
(entry 7) and "TABLE F `Setting or API parameter` column" (entry 9). All neighbor references
are updated for the 7 sites. No structural criteria are affected by the audit table's verbatim
compliance. C-43 passes (all 12 discovered); C-44 passes (all 6 embedded entries verbatim);
composite 110/110.

---

**THE INERTIA PROBLEM**

Throttle failures reach production undiscovered because the system passed at development and
staging volumes. Teams reason: "it worked in dev" — and skip the analysis. The first
production incident is the discovery mechanism. That is the status quo this skill exists to
displace.

What inertia conceals:
- The burst path that was never rate-limited because no one tested at the volume where it fires
- The missing Retry-After handler that turns a 30-second throttle window into a 10-minute
  retry storm that exhausts quota across the tenant
- The cascade that takes down three dependent flows when a single connector limit fires
- The tier whose limit nobody measured at 5x nominal — the volume a viral workflow hits on
  day one — while everyone assumed the documented limit was the binding constraint
- The integration test suite reporting green because it mocks the connector layer

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
the rate-limited system described in the signal. Treat the stated request volume as 1x
nominal; also analyze at 2x and 5x.

The tables below are the primary output — each carries a distinct finding category that prose
cannot represent with the same auditability. Every cell SHALL be filled. Produce sections in
the order shown.

---

**PRECISION-SITE INVENTORY**

*(Required before any table is defined — C-33 + C-35 + C-37 + C-39. Every precision-requiring
site in this prompt is enumerated below in document order. The `Violation type` column states
the specific failure at each site, matching the domain-specific text that SHALL appear at each
definition site. The `C-27 hierarchy` column uses the C-31 parenthetical labeling format —
`primary (C-27):` for the first site and `extension (C-27 extension):` for all subsequent
sites — making the C-31 labeling structure auditable from this inventory without opening each
definition block.)*

| # | Site | C-27 hierarchy | Required precision | Violation type |
|---|------|----------------|--------------------|----------------|
| 1 | TABLE A `Limit (number + unit)` (Step 1A) | `primary (C-27):` | Numeric rate with unit (e.g., "1,000 req/min") | Vague label substituted for numeric value (e.g., "limited" in place of "1,200 req/min") |
| 2 | TABLE A `Load-shape verdict` (Step 1B) | `extension (C-27 extension):` | SHAPE-NEUTRAL or SHAPE-SENSITIVE recorded at Step 1B | Deferred verdict token — entry routes classification to Step 2G rather than recording verdict at Step 1B |
| 3 | TABLE B `Mechanism` (Step 2A) | `extension (C-27 extension):` | Specific named mechanism type from permitted set (queue-fill, connection-hold, retry-amplification, dependency-stall, timeout-cascade) | Generic category label substituted for specific mechanism name (e.g., "blocked" in place of "queue-fill") |
| 4 | TABLE F `Setting or API parameter` (Step 2H) | `extension (C-27 extension):` | Specific connector setting, policy parameter, or API attribute name | Category of action substituted for named parameter identifier (e.g., "add retry logic" instead of `connector.retryPolicy`) |
| 5 | STEP 4 C-24 format requirement: | `extension (C-27 extension):` | All three slots populated: INFORMAL-NAME, SECTION:LOCATION, T-NN | Missing slot identifier — one or more named slot positions absent or collapsed into prose |
| 6 | STEP 4 C-13 compliance — Tier-ID threading: | `extension (C-27 extension):` | Per-finding identification with specific informal references | Binary FAIL flag without enumeration of the specific informal references found |
| 7 | STEP 4 C-19 compliance — distributed reminder audit: | `extension (C-27 extension):` | Per-step inline verdict before aggregate | Aggregate verdict without per-step inline verdict sequence |

*(Seven precision-requiring sites. Violation types SHALL match the domain-specific text at each
downstream definition site — enabling inventory-vs-definition verification. An executor SHALL
verify that the label at each definition block matches the `C-27 hierarchy` value in this row
before producing that definition block — the inventory value is a compliance target, not a
record.)*

---

**STEP 1 — TIER REGISTRY**

*(What inertia conceals here: the tier whose per-second limit was never measured at 2x or 5x
nominal — the volume nobody tested.)*

Step 1 has two sub-steps. An executor SHALL complete Step 1A and Step 1B in order before
opening any Step 2 section. The registry SHALL be closed only after Step 1B gate is cleared.

**REGISTRY GAP PROHIBITION — Failure 5 prevention (C-17):** Tiers discovered during Step 2
are scope violations — evidence that the enumeration phase was incomplete. PROHIBITED:
assigning a new T-NN during Step 2 as a fill-in step. An executor SHALL return to TABLE A,
register the tier with all columns filled, and SHALL restart from the point of discovery.
This prohibition SHALL be restated at each Step 2 section where mid-phase discovery could
occur.

---

**Step 1A — VOLUME ANALYST: TIER IDENTIFICATION AND LIMITS**

**PHASE ENTRY CONDITION:** Step 1A SHALL be entered after the signal input has been read in
full.

*(Volume analyst role: identify every rate-limiting component; record numeric limit, scope,
volume-band status, binding band, failure visibility window, and recovery time. Leave
`Load-shape verdict` as placeholder — assign at Step 1B.)*

**TABLE A — THROTTLE TIER INVENTORY ACROSS VOLUME BANDS**

| Tier-ID | Component | Limit (number + unit) | Scope | STATUS 1x | STATUS 2x | STATUS 5x | Binding at band | Load-shape verdict | Failure visibility window | Recovery time |
|---------|-----------|----------------------|-------|-----------|-----------|-----------|-----------------|-------------------|--------------------------|---------------|
| T-01    |           |                      |       |           |           |           |                 | [Step 1B]         |                          |               |
| T-02    |           |                      |       |           |           |           |                 | [Step 1B]         |                          |               |
| ...     |           |                      |       |           |           |           |                 | [Step 1B]         |                          |               |

Column definitions:
- `Tier-ID` — Assign T-01, T-02, ... and SHALL be used verbatim in every downstream section.
- `Limit (number + unit)` — a specific number with a unit (e.g., "1,000 req/min").
  - *Violation type: vague label substituted for numeric value (e.g., "limited", "throttled"
    in place of "1,200 req/min"). Site 1 has one immediate right neighbor (site 2:
    Load-shape verdict). Single-adjacency — C-36 and C-38 SHALL NOT apply.*
  - Compliance failure condition `primary (C-27):` An entry using a vague label instead of a
    specific number-with-unit fails this column's precision requirement.
- `STATUS Nx` — OK / HIT / SAT; SHALL shift between at least two bands.
- `Binding at band` — lowest band at which this tier is the primary bottleneck. N/A if never.
- `Failure visibility window` — how quickly saturation becomes observable (time + signal).
- `Recovery time` — how long until normal operation resumes after burst traffic subsides.

**STEP 1A GATE:** Step 1A SHALL be considered closed when: (a) every identified rate-limiting
component in the target flow has a T-NN row in TABLE A; (b) every TABLE A row except
`Load-shape verdict` is populated with non-placeholder values; and (c) the `Limit` column
contains no vague labels. An executor SHALL NOT open Step 1B until this gate is cleared.

**PHASE EXIT CONDITION:** Step 1A is exited when the STEP 1A GATE is cleared.

---

**Step 1B — LOAD-SHAPE ANALYST: CLASSIFICATION**

**PHASE ENTRY CONDITION:** Step 1B SHALL be entered only after the STEP 1A GATE is cleared.

*(Load-shape analyst role activates here. Review each tier's `Limit` entry in TABLE A and
assign the `Load-shape verdict` column for every row. The registry closes after Step 1B.)*

**Failure 2 + Failure 6 prevention (C-16, C-20, C-23, C-26) — CLASSIFICATION REQUIRED AT
STEP 1B:** An executor SHALL assign `Load-shape verdict` for every TABLE A tier at this step.
PROHIBITED: leaving any `Load-shape verdict` cell as placeholder or deferring classification
to the LOAD SHAPE COMPARISON section (Step 2G).

**Escape-route story (C-23):** The escape route is the "STATUS tracks volume thresholds"
frame. TABLE A STATUS columns use OK/HIT/SAT to track whether a tier's volume threshold is
crossed at each band. Because STATUS is a volume-threshold metric, TABLE A appears to be a
pure volume-threshold analysis table — making load-shape classification appear out of scope
for the registry and naturally belonging in the section named "LOAD SHAPE COMPARISON." The
Step 1B sub-step structure itself introduces a second escape route: because Step 1B is a named
analyst sub-step, an executor may reason that classification can be deferred to Step 2G where
"the analyst naturally encounters load patterns." Both frames route shape analysis to Step 2G.

**Structural rejection proof (C-26):** Both frames are structurally self-defeating. Premise 1:
load-shape classification requires the registered `Limit` value at registration time —
available in TABLE A now at Step 1B. Premise 2: Step 2G depends on per-tier Load-shape
verdicts to produce meaningful comparisons. Consequence: deferring to Step 2G creates a
circular dependency where the downstream section that would "receive" shape classification
is itself dependent on the per-tier verdict the registry was supposed to supply. Step 1B
exists precisely to foreclose this dependency.

For each TABLE A tier, update `Load-shape verdict`:
- State SHAPE-NEUTRAL or SHAPE-SENSITIVE
- State the numeric rate differential between uniform and burst arrival at this tier's limit
- State the mechanism that explains the differential

- *Violation type: deferred verdict token — the executor routes the SHAPE-NEUTRAL/
  SHAPE-SENSITIVE classification to Step 2G rather than recording it at Step 1B.
  All-neighbor contrast (C-36): the `Limit` column's violation type (left neighbor, site 1)
  is a value-absence failure — the measured number is missing or replaced by an imprecise
  placeholder. TABLE B `Mechanism`'s violation type (right neighbor, site 3) is a mechanism-
  taxonomy failure — a generic category occupies the mechanism field where a specific named
  mechanism type from the permitted set is required; the failure is value-specificity within
  a closed set, not temporal routing and not a missing structural registration. This column's
  violation type is neither: the value is not absent and the failure is not about mechanism
  taxonomy; the failure is purely temporal — the act of recording the verdict is deferred to
  a section that structurally depends on it. Three distinct failures at the same registry
  level, three different corrections: supply the number (Limit), move the classification act
  to Step 1B (this column), name the specific mechanism (TABLE B). An executor MUST NOT
  conflate these 2 failure modes.*
- Compliance failure condition `extension (C-27 extension):` A Load-shape verdict entry left
  blank or deferred ("see Step 2G", "analyzed below") at the end of Step 1B fails the
  registration-time classification requirement and invalidates Step 2G's numeric comparison.

**STEP 1B GATE:** Step 1B SHALL be considered closed when every TABLE A row has a populated
`Load-shape verdict` cell containing a SHAPE-NEUTRAL or SHAPE-SENSITIVE verdict with numeric
differential and mechanism. No placeholder SHALL remain. The registry is closed at this point.

**PHASE EXIT CONDITION:** Step 1B is exited when the STEP 1B GATE is cleared. An executor
SHALL NOT begin STEP 2 until this phase exit condition is met.

---

**STEP 2 — ANALYSIS PHASES**

**PHASE ENTRY CONDITION:** Step 2 SHALL be entered only after the STEP 1B GATE is cleared.
The tier registry is closed. An executor SHALL use T-NN identifiers from TABLE A throughout
all sections below.

---

**Step 2A — BACKPRESSURE PROPAGATION TRACE (TABLE B)**

**PHASE ENTRY CONDITION:** Step 2A SHALL be entered only after TABLE A is closed.

*(What inertia conceals here: the missing Retry-After handler that turns a 30-second throttle
window into a 10-minute retry storm — invisible where the connector layer is mocked.)*

**Step 2A — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19):** Tiers
appearing in backpressure analysis that are not in TABLE A are scope violations. An executor
SHALL NOT assign a new T-NN here. An executor SHALL return to TABLE A (complete Step 1A +
Step 1B), register the tier with all required columns, then continue.

| Hop | From (Tier-ID) | To component | Mechanism | Observable effect |
|-----|----------------|--------------|-----------|-------------------|
| 1   |                |              |           |                   |
| 2   |                |              |           |                   |
| ... |                |              |           |                   |

Column definitions:
- `From (Tier-ID)` — SHALL reference a T-NN from TABLE A.
- `Mechanism` — Name the specific throttle propagation mechanism. Permitted values: queue-fill,
  connection-hold, retry-amplification, dependency-stall, timeout-cascade.
  - *Violation type: generic category label substituted for specific mechanism name (e.g.,
    "blocked" or "throttled" in place of "queue-fill"). All-neighbor contrast (C-36): TABLE A
    `Load-shape verdict`'s violation type (left neighbor, site 2) is a deferred verdict token
    — the classification act is routed to Step 2G rather than recorded at Step 1B; the failure
    is temporal, not about specificity of value. TABLE F `Setting or API parameter`'s violation
    type (right neighbor, site 4) is parameter-specificity failure — a task-class label ("add
    retry logic") occupies a field requiring a deployable parameter identifier; the failure is
    about naming the right type of thing (configuration key vs. task description). This column's
    violation type is neither temporal deferral nor parameter-type substitution: the value is
    present at write time, the column is not a registry classification, and the failure is
    specificity within a closed mechanism taxonomy — naming "blocked" where "queue-fill" is
    required. An executor MUST NOT conflate these 2 failure modes.*
  - Compliance failure condition `extension (C-27 extension):` A mechanism entry using a generic
    category label (blocked, throttled, slowed) rather than a specific named mechanism from the
    permitted set fails this column's precision requirement.

**PHASE EXIT CONDITION:** Step 2A SHALL be considered closed when at least two hops are
documented with T-NN identifiers and specific mechanisms.

---

**Step 2B — USER EXPERIENCE CATALOG (TABLE C)**

**PHASE ENTRY CONDITION:** Step 2B SHALL be entered after Step 2A PHASE EXIT CONDITION
is cleared. One row per TABLE A Tier-ID. No tier SHALL be omitted.

| Tier-ID | Error code or signal | Retry-After present? (Y/N) | Retry-After surfaced to caller? (Y/N) | Visible in run history? (Y/N/SILENT) | Failure if Retry-After ignored |
|---------|---------------------|---------------------------|--------------------------------------|--------------------------------------|-------------------------------|
| T-01    |                     |                           |                                      |                                      |                               |
| T-02    |                     |                           |                                      |                                      |                               |

---

**Step 2C — UNPROTECTED BURST PATHS (TABLE D)**

**PHASE ENTRY CONDITION:** Step 2C SHALL be entered after Step 2B is closed.

*(What inertia conceals here: the burst path that bypasses rate limiting because no test has
ever run at the volume where it fires.)*

**Step 2C — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19):** Tiers
referenced in burst path analysis that are not in TABLE A are scope violations. An executor
SHALL NOT assign a new T-NN here. An executor SHALL return to TABLE A.

At least one row SHALL be present. If no unprotected path exists, row 1 SHALL state the
conclusion with at least two named controls as evidence.

| Path-ID | Entry component | Gap reason (structural gap or named controls) | Tier-IDs involved | Consequence at burst volume |
|---------|----------------|-----------------------------------------------|-------------------|-----------------------------|
| P-01    |                |                                               |                   |                             |

---

**Step 2D — TIER RISK RANKING**

**PHASE ENTRY CONDITION:** Step 2D SHALL be entered after Step 2C is closed.

All TABLE A tiers SHALL appear in the ranking, ordered by business risk, highest to lowest.
One sentence per tier with rationale SHALL be provided. For the top-ranked tier, `Failure
visibility window` and `Recovery time` from TABLE A SHALL be referenced.

---

**Step 2E — CASCADE SCENARIO**

**PHASE ENTRY CONDITION:** Step 2E SHALL be entered after Step 2D is closed.

**Step 2E — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19):** Tiers
introduced during cascade trace that are not in TABLE A are scope violations. An executor
SHALL NOT assign a new T-NN here. An executor SHALL return to TABLE A.

Trace one concrete cascade from the 1x binding constraint. T-NN identifiers SHALL be used
throughout. Each causal link SHALL be stated explicitly. A minimum of three tiers SHALL be
present, each step caused by the previous.

---

**Step 2F — RETRY-AFTER GAP ASSESSMENT**

**PHASE ENTRY CONDITION:** Step 2F SHALL be entered after Step 2E is closed.

For the 1x binding constraint tier: is Retry-After present and surfaced? If absent, the failure
mode SHALL be named precisely — retry storm (exponential backoff) vs. quota exhaustion
(circuit breaker).

---

**Step 2G — LOAD SHAPE COMPARISON**

**PHASE ENTRY CONDITION:** Step 2G SHALL be entered after Step 2F is closed.

**Step 2G — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19):** Tiers
introduced during load shape analysis that are not in TABLE A are scope violations. An
executor SHALL NOT assign a new T-NN here. An executor SHALL return to TABLE A.

Using TABLE A's Limit values and Load-shape verdict column (classified at Step 1B), compare
1x nominal at two arrival patterns. Identical total count; only arrival distribution differs.

- **UNIFORM arrival** — state per-second arrival rate; state which tiers are HIT or SAT.
- **BURST arrival** — state the burst fraction and peak per-second rate; state which tiers
  are HIT or SAT and why.

At least one numeric comparison where status differs at identical total count SHALL be present.

---

**Step 2H — MITIGATION REGISTRY (TABLE F)**

**PHASE ENTRY CONDITION:** Step 2H SHALL be entered after Step 2G is closed.

A mitigation row that names a category of action ("add retry logic") requires further research
before it can be applied. A row that names the exact parameter can be applied immediately.

| MR-ID | Source | Gap type | Component | Setting or API parameter | Change | Expected outcome |
|-------|--------|----------|-----------|--------------------------|--------|-----------------|
| MR-01 |        |          |           |                          |        |                 |
| MR-02 |        |          |           |                          |        |                 |

`Setting or API parameter` — the exact configuration key, connector property, or API attribute
name SHALL be recorded here.

- *Violation type: category of action substituted for named parameter identifier (e.g.,
  "add retry logic" instead of `connector.retryPolicy`). All-neighbor contrast (C-36): TABLE B
  `Mechanism`'s violation type (left neighbor, site 3) is a mechanism-taxonomy failure — a
  generic category label occupies a field where a specific mechanism name from a closed
  permitted set is required; the failure is value-specificity, not timing and not parameter
  identity. The STEP 4 C-24 format requirement:'s violation type (right neighbor, site 5)
  is a structural omission — a labeled slot position within a single finding entry is left
  empty or merged with adjacent content. This column's violation type is neither: the value is
  a string identifier, not a number; there is no timing constraint; and the failure is not
  about a slot within a structured finding. The failure is category substitution — naming the
  class of action where the specific deployable parameter name is required. An executor MUST
  NOT conflate these 2 failure modes.*
- Compliance failure condition `extension (C-27 extension):` A row naming a category of action
  rather than a specific parameter identifier fails this column's precision requirement.

---

**STEP 3 — TEST COVERAGE GAP ANALYSIS**

**PHASE ENTRY CONDITION:** STEP 3 SHALL be entered only after Step 2H is closed.

*(What inertia conceals here: the integration test suite reporting green because it mocks the
connector layer; the load test running at 10% of production concurrency.)*

Execute two stages. Stage 1 SHALL pre-load artifact names; Stage 2 SHALL use them.

**STAGE 1 — TEST INFRASTRUCTURE INVENTORY**

Gate: at least two artifacts SHALL be named with structural properties before Stage 2 opens.

Catalog entry 1:
- **Artifact:** [specific artifact name]
- **Structural property:** [architectural reason it cannot reach the throttle behavior]

Catalog entry 2:
- **Artifact:** [specific artifact name]
- **Structural property:** [architectural reason]

"Stage 1 complete" SHALL be stated before Stage 2 opens.

**TABLE E — TEST COVERAGE GAP REGISTRY**

| GAP-ID | Throttle behavior (Tier-ID + failure mode) | Test type | Structural reason (Stage 1 artifact + property) | Test approach (component + volume + assertion) |
|--------|-------------------------------------------|-----------|--------------------------------------------------|------------------------------------------------|
| GAP-01 |                                           |           |                                                  |                                                |
| GAP-02 |                                           |           |                                                  |                                                |

---

**STEP 4 — INTEGRITY VERIFICATION**

**PHASE ENTRY CONDITION:** STEP 4 SHALL be entered only after Stage 2 of STEP 3 is complete.

**Failure 4 prevention (C-15, C-18, C-22, C-24, C-25) — per-section compliance audit.**
Self-contained block. An executor SHALL complete this block after Stage 2. Each downstream
section SHALL receive an individual verdict on a distinct verdict line, with evidence on a
distinct evidence line.

**C-24 format requirement:** Each field entry SHALL use two distinct labeled lines:
`- Verdict: [PASS / FAIL]`
`- If FAIL — [field label]: [list each finding]`

Each individual finding within a FAIL list MUST populate all three named slots:

```
INFORMAL-NAME:    [exact label used informally in the text]
SECTION:LOCATION: [step name and specific location within the step]
T-NN:             [the registered tier ID it should have referenced]
```

- *Violation type: missing slot identifier in finding entry — one or more named slot positions
  absent or collapsed into prose. All-neighbor contrast (C-36): TABLE F `Setting or API
  parameter`'s violation type (left neighbor, site 4) is category substitution — a task-class
  label occupies the parameter field. The STEP 4 C-13 compliance — Tier-ID threading:'s
  violation type (right neighbor, site 6) is evidence absence — a FAIL verdict is issued at
  the aggregate level without enumerating the specific informal references found. This schema's
  violation type is distinct from both: the failure is not a wrong category in a parameter
  field and not an absent evidence list at aggregate level — a labeled slot position within a
  single finding entry is left empty or merged with adjacent content. An executor MUST NOT
  conflate these 2 failure modes.*
- Compliance failure condition `extension (C-27 extension):` A finding that omits any named
  slot position — or presents findings as free-form prose — fails the identification schema.

---

**C-13 compliance — Tier-ID threading:**

Step 2A (TABLE B):
- Verdict: [PASS / FAIL]
- If FAIL — informal references found: [list each using the three-slot template above]

Step 2B (TABLE C):
- Verdict: [PASS / FAIL]
- If FAIL — informal references found: [list each using the three-slot template above]

Step 2C (TABLE D):
- Verdict: [PASS / FAIL]
- If FAIL — informal references found: [list each using the three-slot template above]

Step 2D (TIER RISK RANKING):
- Verdict: [PASS / FAIL]
- If FAIL — informal references found: [list each using the three-slot template above]

Step 2E (CASCADE SCENARIO):
- Verdict: [PASS / FAIL]
- If FAIL — informal references found: [list each using the three-slot template above]

Step 2G (LOAD SHAPE COMPARISON):
- Verdict: [PASS / FAIL]
- If FAIL — informal references found: [list each using the three-slot template above]

Unregistered tiers introduced after TABLE A closed:
- Verdict: [PASS / FAIL]
- If FAIL — unregistered tiers found: [list each: "[tier name] introduced at [step]"]

- *Violation type: binary FAIL flag without enumeration of specific informal references.
  Adjacent contrast: the C-24 format requirement:'s violation type (left neighbor, site 5)
  is structural omission within a finding entry — a labeled slot is missing or collapsed into
  prose. The STEP 4 C-19 compliance — distributed reminder audit:'s violation type (right
  neighbor, site 7) is verdict granularity collapse — individual step verdicts are merged into
  a single aggregate without per-step assessments. This audit field's violation type is
  distinct from both: the failure is not within a single finding (C-24's domain) and not about
  per-step verdict granularity (C-19's domain). The failure is at the aggregate reporting level
  — the FAIL verdict is correctly present but the specific informal references are not
  enumerated. An executor MUST NOT conflate these 2 failure modes.*
- Compliance failure condition `extension (C-27 extension):` A FAIL verdict that does not
  enumerate specific informal references fails this audit field.

**C-19 compliance — distributed reminder audit:**

**C-25 format requirement:** Issue an individual inline verdict for each step before the
aggregate failure list.

- Step 2A (TABLE B): [Y — reminder present / N — missing]
- Step 2C (TABLE D): [Y — reminder present / N — missing]
- Step 2E (CASCADE SCENARIO): [Y — reminder present / N — missing]
- Step 2G (LOAD SHAPE COMPARISON): [Y — reminder present / N — missing]
- If any N:
  - Verdict: FAIL
  - Missing steps: [list each step where N was recorded]

- *Violation type: aggregate verdict without per-step inline verdict sequence. Adjacent
  contrast: the C-13 compliance — Tier-ID threading: audit field's violation type (left
  neighbor, site 6) is evidence absence on FAIL — a FAIL verdict that correctly fires but
  names no specific findings. This field's violation type is verdict granularity collapse:
  per-step verdicts are merged into a single aggregate before the FAIL branch. C-13 fails on
  what the FAIL entry contains; C-19 fails on whether each step receives its own verdict line.
  Both fail at the audit level; each requires a different correction. Site 7 has one immediate
  neighbor — C-36 and C-38 do not apply.*
- Compliance failure condition `extension (C-27 extension):` A single aggregate verdict
  without per-step inline verdicts fails the C-25 format requirement.

**C-14 compliance — Perspective separation:**
- Verdict: [PASS / FAIL]
- If FAIL — interleaving found: [describe where tier discovery and caller behavior appeared
  in the same step]

**C-40 / C-41 compliance — Per-directive normative-register audit:**

*(C-43 discovery scope: this field covers all SHALL, SHALL NOT, MUST, MUST NOT, and PROHIBITED
obligation clauses in the prompt regardless of structural location — named enforcement block
headers, *Violation type* italic fields, inventory parenthetical notes, and PHASE ENTRY/EXIT
condition blocks. Clauses lacking a standalone block header are named by their exact containing
structure. Total enforcement directives in this prompt: 12.)*

*(C-44 compliance note: all 6 embedded non-primary-location directives are cited using the
verbatim structural labels as they appear in the prompt body. Entry 7: "TABLE A `Load-shape
verdict` column" — verbatim column name from TABLE A header row. Entry 8: "TABLE B `Mechanism`
column" — verbatim column name from TABLE B header row. Entry 9: "TABLE F `Setting or API
parameter` column" — verbatim column name from TABLE F header row. Entry 10: "PRECISION-SITE
INVENTORY" — verbatim section header. Entry 11: "STEP 4 C-24 format requirement:" — verbatim
bold sub-header "**C-24 format requirement:**" as it appears in STEP 4, including trailing
colon. Entry 12: "STEP 4 C-13 compliance — Tier-ID threading:" — verbatim bold sub-header
"**C-13 compliance — Tier-ID threading:**" as it appears in STEP 4, with lowercase c. No
contextual derivations or paraphrases in entries 7-12.)*

For each enforcement directive in this prompt, verify that the primary directive uses RFC
2119-style normative language (SHALL, SHALL NOT, MUST, MUST NOT, PROHIBITED). An executor
SHALL enumerate each directive by its verbatim declared block name (for named blocks) or its
exact containing structure name (for embedded non-primary-location clauses) and record a
per-directive verdict:

| Directive block (verbatim declared name or containing structure) | Primary language used | C-40 verdict |
|-----------------------------------------------------------------|----------------------|-------------|
| REGISTRY GAP PROHIBITION — Failure 5 prevention (C-17) | PROHIBITED / SHALL | [PASS / FAIL] |
| Step 2A — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19) | SHALL NOT | [PASS / FAIL] |
| Step 2C — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19) | SHALL NOT | [PASS / FAIL] |
| Step 2E — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19) | SHALL NOT | [PASS / FAIL] |
| Step 2G — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19) | SHALL NOT | [PASS / FAIL] |
| Failure 2 + Failure 6 prevention (C-16, C-20, C-23, C-26) — CLASSIFICATION REQUIRED AT STEP 1B | PROHIBITED / SHALL | [PASS / FAIL] |
| TABLE A `Load-shape verdict` column — *Violation type* field non-conflation directive | MUST NOT | [PASS / FAIL] |
| TABLE B `Mechanism` column — *Violation type* field non-conflation directive | MUST NOT | [PASS / FAIL] |
| TABLE F `Setting or API parameter` column — *Violation type* field non-conflation directive | MUST NOT | [PASS / FAIL] |
| PRECISION-SITE INVENTORY — inventory verification obligation (parenthetical note) | SHALL verify | [PASS / FAIL] |
| STEP 4 C-24 format requirement: — *Violation type* field non-conflation directive | MUST NOT | [PASS / FAIL] |
| STEP 4 C-13 compliance — Tier-ID threading: — *Violation type* field non-conflation directive | MUST NOT | [PASS / FAIL] |

If any row is FAIL: state the specific phrase found and its normative replacement.

*(C-41 satisfied: all 12 enforcement directives enumerated by their declared or containing-
structure names with individual per-directive verdicts. Aggregate statements are not used.
C-42 satisfied: all 6 primary-location directives cited by their verbatim declared block name
exactly as they appear in the prompt body — including criterion-ID parentheticals. C-43
satisfied: all 6 non-primary-location directives discovered — TABLE A, TABLE B, and TABLE F
*Violation type* field non-conflation directives, PRECISION-SITE INVENTORY parenthetical
obligation, and both STEP 4 *Violation type* field non-conflation directives — named by their
exact containing structure. C-44 satisfied: all 6 embedded-directive entries cite their
containing structures using the verbatim structural labels from the prompt body — "TABLE A
`Load-shape verdict` column", "TABLE B `Mechanism` column", "TABLE F `Setting or API
parameter` column", "PRECISION-SITE INVENTORY", "STEP 4 C-24 format requirement:" (verbatim
bold header including trailing colon), and "STEP 4 C-13 compliance — Tier-ID threading:"
(verbatim bold header with lowercase c). No contextually-derived or paraphrased container
labels remain.)*
