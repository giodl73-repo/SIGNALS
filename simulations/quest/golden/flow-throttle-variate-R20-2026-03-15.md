# flow-throttle Variate — Round 20 (v19 rubric, C-01 through C-48)
**Date:** 2026-03-15
**Rubric:** v19 (C-01 through C-48, N_essential=5, N_recommended=3, N_aspirational=40)
**Baseline ceiling:** R19 V-05 (passes C-01 through C-46; composite 110/110)

---

## State Analysis: What R19 Established vs. What R20 Must Add

**R19 V-05 coverage under v19 (confirmed):**
- C-01 through C-46: all pass — composite 110/110
- C-47 gap: The C-41 citation instruction requires verbatim block-name citation (C-42) and
  character-exact typography (C-46), but nowhere names interior-segment title-case normalization
  as the specific prohibited failure mode for multi-segment dash-delimited block names. The
  abstract verbatim principle is present; the concrete failure-mode naming with wrong → right
  examples is absent.
- C-48 gap: The C-41 per-directive audit block enumerates 14 directives including 6
  `*Violation type:*` MUST NOT clauses at multi-adjacent C-38 sites, but no pre-declared
  expected count for this category is stated. An omission from the 6-entry set is undetectable
  by count comparison without a re-scan.

**R20 structural additions (STEP 4 C-41 block only — no new directives or precision sites):**

1. **C-47 instruction** — parenthetical note in C-41 preamble, placed after the C-43 discovery
   scope note. Names interior-segment title-case normalization as PROHIBITED for multi-segment
   dash-delimited block names. C-47 requires "examples showing the wrong → right form"; V-01
   and V-02 test the two ways this can fail (no examples; wrong-form-only example).

2. **C-48 count declaration** — parenthetical note in C-41 preamble. Pre-declares the expected
   count of `*Violation type:*` MUST NOT clauses qualifying under C-45. The correct count is
   derived from multi-adjacent C-38-compliant precision sites: sites 2, 3, 4, 5, 6, 7 (sites 1
   and 8 are single-adjacent; C-36 and C-38 do not apply to them). Correct expected count = 6.
   V-03 tests omission; V-04 tests wrong count (5, omitting site 7).

**Total enforcement directives: 14 (unchanged). Total precision sites: 8 (unchanged).**

---

## Round 20 Variation Map

| Var | Axes | C-47/C-48 mechanism | Predicted |
|-----|------|---------------------|-----------|
| V-01 | Phrasing register — C-47 instruction names prohibition; no wrong → right examples | Principle stated, exemplar requirement unmet | C-47 FAIL (~109.5/110) |
| V-02 | Output format — C-47 instruction provides wrong-form-only example | Wrong form shown; correct form absent from pair | C-47 FAIL (~109.5/110) |
| V-03 | Lifecycle emphasis — C-47 correct with examples; C-48 absent | No pre-declared count; omission undetectable | C-48 FAIL (~109.5/110) |
| V-04 | Role sequence — C-47 correct; C-48 declares count = 5 | Sites 2–6 only; site 7 omitted from count | C-48 FAIL (~109.5/110) |
| V-05 | All combined — C-47 with wrong→right examples; C-48 count = 6 | Both criteria fully satisfied | C-47 + C-48 PASS (110/110) |

**Single-axis questions:**

Q1 (V-01 vs R19 V-05): Does naming interior-segment title-case normalization as PROHIBITED
without providing wrong → right examples fail C-47? C-47 requires "examples showing the wrong
→ right form" — a principle statement alone, even one that names the failure mode and provides
inline characterizations ("capitalizing 'enforcement reminder' as 'Enforcement Reminder'"), does
not satisfy the exemplar requirement. Predicted: C-47 FAIL. Composite = ~109.5/110.

Q2 (V-02 vs V-01): Does providing a wrong-form-only example ("MUST NOT cite 'Standing
Enforcement Reminder'") without the corresponding correct form fail C-47? The criterion requires
a wrong → right pair; showing only the prohibited form leaves the correct form undemonstrated.
Predicted: C-47 FAIL. Composite = ~109.5/110.

Q3 (V-03 vs V-02): Does implementing C-47 correctly but omitting C-48 fail C-48? Without a
pre-declared count, a reviewer cannot detect an omitted `*Violation type:*` MUST NOT clause by
count comparison — the gap is only visible on re-scan. Predicted: C-48 FAIL. Composite =
~109.5/110.

Q4 (V-04 vs V-03): Does declaring count = 5 (covering sites 2–6, omitting site 7) fail C-48?
Site 7 (STEP 4 C-13 compliance — Tier-ID threading:) is multi-adjacent and carries a C-38
MUST NOT non-conflation directive qualifying under C-45. Declaring 5 produces a count that
would accept an audit missing site 7's clause without flagging a discrepancy. Predicted: C-48
FAIL. Composite = ~109.5/110.

Q5 (V-05): Do wrong → right examples for C-47 and count = 6 for C-48 satisfy both criteria
without regressions? All other structural elements unchanged from R19 V-05. Predicted:
composite 110/110.

---

## V-01 — Single Axis: Phrasing Register (C-47 principle stated, no examples)

**Axis:** Phrasing register — the STEP 4 C-41 preamble adds a C-47 instruction that names
interior-segment title-case normalization as a PROHIBITED failure mode for multi-segment
dash-delimited block names. The instruction describes the failure mode and forbids it by name;
no wrong → right example pairs are provided. C-48 is implemented correctly (count = 6).

**Hypothesis:** C-47 requires "examples showing the wrong → right form." A principle-only
statement satisfies the "names the failure mode" component but not the "provides examples"
component. An executor reading only the prohibition without an anchoring example pair may still
produce title-cased interior segments. Predicted: C-47 FAIL. Composite = ~109.5/110.

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
| 4 | TABLE C `Error code or signal` (Step 2B) | `extension (C-27 extension):` | Specific error code or platform signal identifier (e.g., "HTTP 429", connector-specific code such as "TL-0001") | Plain description substituted for structured error code or signal identifier (e.g., "request fails" in place of "HTTP 429") |
| 5 | TABLE F `Setting or API parameter` (Step 2H) | `extension (C-27 extension):` | Specific connector setting, policy parameter, or API attribute name | Category of action substituted for named parameter identifier (e.g., "add retry logic" instead of `connector.retryPolicy`) |
| 6 | STEP 4 C-24 format requirement: | `extension (C-27 extension):` | All three slots populated: INFORMAL-NAME, SECTION:LOCATION, T-NN | Missing slot identifier — one or more named slot positions absent or collapsed into prose |
| 7 | STEP 4 C-13 compliance — Tier-ID threading: | `extension (C-27 extension):` | Per-finding identification with specific informal references | Binary FAIL flag without enumeration of the specific informal references found |
| 8 | STEP 4 C-19 compliance — distributed reminder audit: | `extension (C-27 extension):` | Per-step inline verdict before aggregate | Aggregate verdict without per-step inline verdict sequence |

*(Eight precision-requiring sites. Violation types SHALL match the domain-specific text at each
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

A minimum of two hops SHALL be present. `Mechanism` SHALL be specific: queue-fill,
connection-hold, retry-amplification, dependency-stall, timeout-cascade.

Column definitions:
- `From (Tier-ID)` — SHALL reference a T-NN from TABLE A.
- `Mechanism` — Name the specific throttle propagation mechanism. Permitted values: queue-fill,
  connection-hold, retry-amplification, dependency-stall, timeout-cascade.
  - *Violation type: generic category label substituted for specific mechanism name (e.g.,
    "blocked" or "throttled" in place of "queue-fill"). All-neighbor contrast (C-36): TABLE A
    `Load-shape verdict`'s violation type (left neighbor, site 2) is a deferred verdict token
    — the classification act is routed to Step 2G rather than recorded at Step 1B; the failure
    is temporal, not about specificity of value. TABLE C `Error code or signal`'s violation
    type (right neighbor, site 4) is a structural-identifier substitution — a free-form error
    description occupies a field requiring a typed error code or platform signal identifier;
    the failure is about identifier format, not mechanism taxonomy. This column's violation
    type is neither temporal deferral nor identifier-format substitution: the value is present
    at write time, the column is not a registry classification, and the failure is specificity
    within a closed mechanism taxonomy — naming "blocked" where "queue-fill" is required. An
    executor MUST NOT conflate these 2 failure modes.*
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

Column definitions:
- `Error code or signal` — Record the specific HTTP status code or platform-defined signal
  identifier returned at this throttle tier (e.g., "HTTP 429", "HTTP 503", "TL-0001").
  - *Violation type: plain description substituted for structured error code or signal
    identifier (e.g., "request fails" in place of "HTTP 429"). All-neighbor contrast (C-36):
    TABLE B `Mechanism`'s violation type (left neighbor, site 3) is a mechanism-taxonomy
    failure — a generic category label occupies a field requiring a specific named mechanism
    from a closed permitted set; the failure is about mechanism specificity within a controlled
    vocabulary. TABLE F `Setting or API parameter`'s violation type (right neighbor, site 5)
    is a parameter-specificity failure — a task-class action label ("add retry logic") occupies
    a field requiring a deployable parameter identifier; the failure is about the type of
    identifier (action category vs. configuration key). This column's violation type is neither:
    the failure is not about mechanism taxonomy and not about action-vs-identifier confusion;
    it is a structural-identifier substitution — replacing a typed HTTP or platform signal code
    with a descriptive phrase. An executor MUST NOT conflate these 2 failure modes.*
  - Compliance failure condition `extension (C-27 extension):` An `Error code or signal` entry
    using a plain description rather than a specific HTTP status code or platform signal
    identifier fails this column's precision requirement.

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

**Step 2H — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19):** Tiers
referenced in mitigation entries that are not in TABLE A are scope violations. An executor
SHALL NOT assign a new T-NN here. An executor SHALL return to TABLE A (complete Step 1A +
Step 1B), register the tier with all required columns, then continue.

A mitigation row that names a category of action ("add retry logic") requires further research
before it can be applied. A row that names the exact parameter can be applied immediately.

| MR-ID | Source | Gap type | Component | Setting or API parameter | Change | Expected outcome |
|-------|--------|----------|-----------|--------------------------|--------|-----------------|
| MR-01 |        |          |           |                          |        |                 |
| MR-02 |        |          |           |                          |        |                 |

`Setting or API parameter` — the exact configuration key, connector property, or API attribute
name SHALL be recorded here.

- *Violation type: category of action substituted for named parameter identifier (e.g.,
  "add retry logic" instead of `connector.retryPolicy`). All-neighbor contrast (C-36): TABLE C
  `Error code or signal`'s violation type (left neighbor, site 4) is a structural-identifier
  substitution — a free-form error description occupies a field requiring a typed error code
  or platform signal identifier; the failure is about identifier format, not parameter identity.
  The STEP 4 C-24 format requirement:'s violation type (right neighbor, site 6) is a structural
  omission — a labeled slot position within a single finding entry is left empty or merged with
  adjacent content. This column's violation type is neither: the value is a string identifier,
  not a number; there is no timing constraint; and the failure is not about a slot within a
  structured finding. The failure is category substitution — naming the class of action where
  the specific deployable parameter name is required. An executor MUST NOT conflate these
  2 failure modes.*
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
  parameter`'s violation type (left neighbor, site 5) is category substitution — a task-class
  label occupies the parameter field. The STEP 4 C-13 compliance — Tier-ID threading:'s
  violation type (right neighbor, site 7) is evidence absence — a FAIL verdict is issued at
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
  Adjacent contrast: the C-24 format requirement:'s violation type (left neighbor, site 6)
  is structural omission within a finding entry — a labeled slot is missing or collapsed into
  prose. The STEP 4 C-19 compliance — distributed reminder audit:'s violation type (right
  neighbor, site 8) is verdict granularity collapse — individual step verdicts are merged into
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
- Step 2H (TABLE F): [Y — reminder present / N — missing]
- If any N:
  - Verdict: FAIL
  - Missing steps: [list each step where N was recorded]

- *Violation type: aggregate verdict without per-step inline verdict sequence. Adjacent
  contrast: the C-13 compliance — Tier-ID threading: audit field's violation type (left
  neighbor, site 7) is evidence absence on FAIL — a FAIL verdict that correctly fires but
  names no specific findings. This field's violation type is verdict granularity collapse:
  per-step verdicts are merged into a single aggregate before the FAIL branch. C-13 fails on
  what the FAIL entry contains; C-19 fails on whether each step receives its own verdict line.
  Both fail at the audit level; each requires a different correction. Site 8 has one immediate
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
condition blocks. Clauses lacking a standalone block header are named by their containing
structure. Total enforcement directives in this prompt: 14.)*

*(C-47 citation instruction — interior-segment title-case prohibition: verbatim citation SHALL
retain the declared capitalization of every interior segment in multi-segment dash-delimited
block names. Interior-segment title-case normalization — capitalizing a segment that appears
in lowercase in the declared label — is PROHIBITED for multi-segment dash-delimited block
names. Each segment after a dash delimiter retains its declared capitalization exactly as it
appears in the prompt body, regardless of whether the segment would conventionally be title-
cased as a standalone noun or heading.)*

*(C-48 expected-count declaration: Expected `*Violation type:*` MUST NOT clauses qualifying
under C-45: 6 — one per multi-adjacent C-38-compliant precision site (sites 2, 3, 4, 5, 6, 7
from the PRECISION-SITE INVENTORY; sites 1 and 8 are single-adjacent and SHALL NOT carry
C-38 non-conflation directives). An executor SHALL verify that exactly 6 entries in the table
below correspond to `*Violation type:*` field MUST NOT clauses; if fewer than 6 are found,
at least one qualifying clause was omitted.)*

*(C-44 / C-45 / C-46 compliance note: all 7 embedded non-primary-location directives are
cited using the verbatim structural labels as they appear in the prompt body. Entry 8:
"TABLE A `Load-shape verdict` column" — verbatim column name from TABLE A header row. Entry
9: "TABLE B `Mechanism` column" — verbatim column name from TABLE B header row. Entry 10:
"TABLE C `Error code or signal` column" — verbatim column name from TABLE C header row.
Entry 11: "TABLE F `Setting or API parameter` column" — verbatim column name from TABLE F
header row. Entry 12: "PRECISION-SITE INVENTORY" — verbatim section header. Entry 13: "STEP 4
C-24 format requirement:" — verbatim bold sub-header including trailing colon. Entry 14: "STEP
4 C-13 compliance — Tier-ID threading:" — verbatim bold sub-header with lowercase c.
Entry 6: "Step 2H — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19)" —
verbatim bold block header with lowercase e and r in "enforcement reminder"; capital E/R would
fail C-46. No contextual derivations or paraphrases in entries 6-14.)*

For each enforcement directive in this prompt, verify that the primary directive uses RFC
2119-style normative language (SHALL, SHALL NOT, MUST, MUST NOT, PROHIBITED). An executor
SHALL enumerate each directive by its verbatim declared block name (for named blocks) or its
exact containing structure name (for embedded non-primary-location clauses) and record a
per-directive verdict.

| Directive block (verbatim declared name or containing structure) | Primary language used | C-40 verdict |
|-----------------------------------------------------------------|----------------------|-------------|
| REGISTRY GAP PROHIBITION — Failure 5 prevention (C-17) | PROHIBITED / SHALL | [PASS / FAIL] |
| Step 2A — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19) | SHALL NOT | [PASS / FAIL] |
| Step 2C — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19) | SHALL NOT | [PASS / FAIL] |
| Step 2E — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19) | SHALL NOT | [PASS / FAIL] |
| Step 2G — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19) | SHALL NOT | [PASS / FAIL] |
| Step 2H — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19) | SHALL NOT | [PASS / FAIL] |
| Failure 2 + Failure 6 prevention (C-16, C-20, C-23, C-26) — CLASSIFICATION REQUIRED AT STEP 1B | PROHIBITED / SHALL | [PASS / FAIL] |
| TABLE A `Load-shape verdict` column — *Violation type* field non-conflation directive | MUST NOT | [PASS / FAIL] |
| TABLE B `Mechanism` column — *Violation type* field non-conflation directive | MUST NOT | [PASS / FAIL] |
| TABLE C `Error code or signal` column — *Violation type* field non-conflation directive | MUST NOT | [PASS / FAIL] |
| TABLE F `Setting or API parameter` column — *Violation type* field non-conflation directive | MUST NOT | [PASS / FAIL] |
| PRECISION-SITE INVENTORY — inventory verification obligation (parenthetical note) | SHALL verify | [PASS / FAIL] |
| STEP 4 C-24 format requirement: — *Violation type* field non-conflation directive | MUST NOT | [PASS / FAIL] |
| STEP 4 C-13 compliance — Tier-ID threading: — *Violation type* field non-conflation directive | MUST NOT | [PASS / FAIL] |

If any row is FAIL: state the specific phrase found and its normative replacement.

*(C-41 satisfied: all 14 enforcement directives enumerated with individual per-directive
verdicts. C-42 satisfied: all 14 entries use verbatim declared names. C-46 satisfied: all
entries reproduce every character exactly, including lowercase e/r in "enforcement reminder"
at entry 6 and lowercase c in "C-13 compliance" at entry 14. C-47 NOT satisfied: interior-
segment title-case normalization is named as prohibited and characterized inline, but no wrong
→ right example pairs are provided — the criterion requires "examples showing the wrong → right
form" and a principle-only statement does not satisfy the exemplar requirement. C-48 satisfied:
expected count declared as 6; entries 8, 9, 10, 11, 13, 14 are the 6 qualifying `*Violation
type:*` MUST NOT clauses at multi-adjacent sites 2, 3, 4, 5, 6, 7.)*

---

## V-02 — Single Axis: Output Format (C-47 wrong-form-only example)

**Axis:** Output format — the STEP 4 C-41 preamble adds a C-47 instruction that names the
interior-segment title-case prohibition and provides examples of the prohibited forms.
The prohibited forms are named but the correct forms are not shown as the explicit right-hand
completion of a wrong → right pair. C-48 is implemented correctly (count = 6).

**Hypothesis:** C-47 requires "examples showing the wrong → right form." Showing the wrong
form alone ("MUST NOT cite 'Standing Enforcement Reminder'") without completing the pair with
the right form ("the correct citation is 'Standing enforcement reminder'") fails the exemplar
requirement — one direction of a required two-direction example is missing. Predicted: C-47
FAIL. Composite = ~109.5/110.

---

*(THE INERTIA PROBLEM: identical to V-01.)*

*(Role setup: identical to V-01.)*

*(PRECISION-SITE INVENTORY: identical to V-01 — eight sites, same hierarchy labels and
violation types, same verification obligation parenthetical.)*

*(STEP 1 — TIER REGISTRY: identical to V-01. All gates, phase conditions, Step 1A TABLE A,
Step 1B Failure 2 + Failure 6 prevention block: identical to V-01.)*

*(STEP 2 through STEP 3: identical to V-01 — all sections present with PHASE ENTRY/EXIT
conditions, all five Standing enforcement reminder blocks at Steps 2A, 2C, 2E, 2G, 2H, all
*Violation type* italic fields, all compliance failure conditions.)*

*(STEP 4 C-24 format requirement through C-14 compliance: identical to V-01.)*

**C-40 / C-41 compliance — Per-directive normative-register audit:**

*(C-43 discovery scope: identical to V-01. Total enforcement directives: 14.)*

*(C-47 citation instruction — interior-segment title-case prohibition: verbatim citation SHALL
retain the declared capitalization of every interior segment in multi-segment dash-delimited
block names. Interior-segment title-case normalization is PROHIBITED. An executor MUST NOT
cite "Step 2H — Standing Enforcement Reminder — REGISTRY GAP PROHIBITED (C-17, C-19)" for
the block whose declared header reads "Step 2H — Standing enforcement reminder — REGISTRY GAP
PROHIBITED (C-17, C-19)" — the capitalization of "Enforcement" and "Reminder" does not match
the declared label. Similarly, "REGISTRY GAP PROHIBITION — Failure 5 Prevention (C-17)" with
capital P is prohibited — the declared label reads "prevention" with lowercase p.)*

*(C-48 expected-count declaration: identical to V-01 — expected count 6, sites 2, 3, 4, 5, 6,
7.)*

*(C-44 / C-45 / C-46 compliance note: identical to V-01.)*

For each enforcement directive in this prompt, verify that the primary directive uses RFC
2119-style normative language. An executor SHALL enumerate each directive by its verbatim
declared block name or exact containing structure name and record a per-directive verdict.

| Directive block (verbatim declared name or containing structure) | Primary language used | C-40 verdict |
|-----------------------------------------------------------------|----------------------|-------------|
| REGISTRY GAP PROHIBITION — Failure 5 prevention (C-17) | PROHIBITED / SHALL | [PASS / FAIL] |
| Step 2A — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19) | SHALL NOT | [PASS / FAIL] |
| Step 2C — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19) | SHALL NOT | [PASS / FAIL] |
| Step 2E — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19) | SHALL NOT | [PASS / FAIL] |
| Step 2G — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19) | SHALL NOT | [PASS / FAIL] |
| Step 2H — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19) | SHALL NOT | [PASS / FAIL] |
| Failure 2 + Failure 6 prevention (C-16, C-20, C-23, C-26) — CLASSIFICATION REQUIRED AT STEP 1B | PROHIBITED / SHALL | [PASS / FAIL] |
| TABLE A `Load-shape verdict` column — *Violation type* field non-conflation directive | MUST NOT | [PASS / FAIL] |
| TABLE B `Mechanism` column — *Violation type* field non-conflation directive | MUST NOT | [PASS / FAIL] |
| TABLE C `Error code or signal` column — *Violation type* field non-conflation directive | MUST NOT | [PASS / FAIL] |
| TABLE F `Setting or API parameter` column — *Violation type* field non-conflation directive | MUST NOT | [PASS / FAIL] |
| PRECISION-SITE INVENTORY — inventory verification obligation (parenthetical note) | SHALL verify | [PASS / FAIL] |
| STEP 4 C-24 format requirement: — *Violation type* field non-conflation directive | MUST NOT | [PASS / FAIL] |
| STEP 4 C-13 compliance — Tier-ID threading: — *Violation type* field non-conflation directive | MUST NOT | [PASS / FAIL] |

If any row is FAIL: state the specific phrase found and its normative replacement.

*(C-41 satisfied: all 14 directives enumerated. C-42 satisfied: all verbatim. C-46 satisfied:
all character-exact. C-47 NOT satisfied: the C-47 instruction names the prohibited forms
("Standing Enforcement Reminder", "Failure 5 Prevention") but provides no corresponding
correct forms — the instruction shows only the wrong direction of a required wrong → right
pair. C-47 requires both forms shown together in each example; naming only the prohibited form
does not constitute a wrong → right example. C-48 satisfied: expected count 6; entries 8, 9,
10, 11, 13, 14 are the 6 qualifying clauses.)*

---

## V-03 — Single Axis: Lifecycle Emphasis (C-47 correct, C-48 absent)

**Axis:** Lifecycle emphasis — the STEP 4 C-41 preamble adds a fully correct C-47 instruction
with wrong → right example pairs for both "enforcement reminder" and "prevention" patterns.
The C-48 expected-count declaration is omitted entirely — no pre-declared count appears in the
C-41 preamble or anywhere in the audit block.

**Hypothesis:** C-48 requires the C-41 per-directive audit field to pre-declare the expected
count of `*Violation type:*` MUST NOT clauses qualifying under C-45. Without this count, a
reviewer cannot detect an omitted qualifying clause by count comparison — the gap is visible
only by re-scanning every `*Violation type:*` annotation. Predicted: C-48 FAIL. Composite =
~109.5/110.

---

*(THE INERTIA PROBLEM through STEP 3: identical to V-01.)*

*(STEP 4 C-24 format requirement through C-14 compliance: identical to V-01.)*

**C-40 / C-41 compliance — Per-directive normative-register audit:**

*(C-43 discovery scope: identical to V-01. Total enforcement directives: 14.)*

*(C-47 citation instruction — interior-segment title-case prohibition: verbatim citation SHALL
retain the declared capitalization of every interior segment in multi-segment dash-delimited
block names. Interior-segment title-case normalization is PROHIBITED. Wrong → right examples:
(1) "Step 2H — Standing Enforcement Reminder — REGISTRY GAP PROHIBITED (C-17, C-19)"
    → "Step 2H — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19)";
(2) "REGISTRY GAP PROHIBITION — Failure 5 Prevention (C-17)"
    → "REGISTRY GAP PROHIBITION — Failure 5 prevention (C-17)".
An executor MUST NOT capitalize any interior segment that appears in lowercase in the declared
block label.)*

*(C-44 / C-45 / C-46 compliance note: identical to V-01.)*

For each enforcement directive in this prompt, verify that the primary directive uses RFC
2119-style normative language. An executor SHALL enumerate each directive by its verbatim
declared block name or exact containing structure name and record a per-directive verdict.

| Directive block (verbatim declared name or containing structure) | Primary language used | C-40 verdict |
|-----------------------------------------------------------------|----------------------|-------------|
| REGISTRY GAP PROHIBITION — Failure 5 prevention (C-17) | PROHIBITED / SHALL | [PASS / FAIL] |
| Step 2A — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19) | SHALL NOT | [PASS / FAIL] |
| Step 2C — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19) | SHALL NOT | [PASS / FAIL] |
| Step 2E — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19) | SHALL NOT | [PASS / FAIL] |
| Step 2G — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19) | SHALL NOT | [PASS / FAIL] |
| Step 2H — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19) | SHALL NOT | [PASS / FAIL] |
| Failure 2 + Failure 6 prevention (C-16, C-20, C-23, C-26) — CLASSIFICATION REQUIRED AT STEP 1B | PROHIBITED / SHALL | [PASS / FAIL] |
| TABLE A `Load-shape verdict` column — *Violation type* field non-conflation directive | MUST NOT | [PASS / FAIL] |
| TABLE B `Mechanism` column — *Violation type* field non-conflation directive | MUST NOT | [PASS / FAIL] |
| TABLE C `Error code or signal` column — *Violation type* field non-conflation directive | MUST NOT | [PASS / FAIL] |
| TABLE F `Setting or API parameter` column — *Violation type* field non-conflation directive | MUST NOT | [PASS / FAIL] |
| PRECISION-SITE INVENTORY — inventory verification obligation (parenthetical note) | SHALL verify | [PASS / FAIL] |
| STEP 4 C-24 format requirement: — *Violation type* field non-conflation directive | MUST NOT | [PASS / FAIL] |
| STEP 4 C-13 compliance — Tier-ID threading: — *Violation type* field non-conflation directive | MUST NOT | [PASS / FAIL] |

If any row is FAIL: state the specific phrase found and its normative replacement.

*(C-41 satisfied: all 14 directives enumerated. C-42 satisfied: all verbatim. C-46 satisfied:
all character-exact. C-47 satisfied: wrong → right examples present for "enforcement reminder"
and "prevention" patterns — both the prohibited and correct forms are shown as explicit pairs.
C-48 NOT satisfied: no pre-declared expected count for `*Violation type:*` MUST NOT clauses
qualifying under C-45 appears in the audit preamble. The 6 qualifying clauses (entries 8, 9,
10, 11, 13, 14) are present in the table, but an omission from this set is undetectable by
count comparison without re-scanning every `*Violation type:*` annotation.)*

---

## V-04 — Single Axis: Role Sequence (C-47 correct, C-48 count = 5)

**Axis:** Role sequence — the STEP 4 C-41 preamble adds a fully correct C-47 instruction with
wrong → right example pairs. The C-48 expected-count declaration is present but declares the
count as 5, covering precision sites 2, 3, 4, 5, 6 only — site 7 (STEP 4 C-13 compliance —
Tier-ID threading:) is omitted from the enumeration count.

**Hypothesis:** The correct expected count is 6: sites 2, 3, 4, 5, 6, 7 are multi-adjacent
and each carry a `*Violation type:*` MUST NOT non-conflation directive qualifying under C-45.
Declaring 5 produces a count that would accept an audit table containing only entries 8, 9,
10, 11, 13 (omitting entry 14 for site 7) without triggering a discrepancy. The off-by-one
makes one qualifying clause permanently undetectable by count comparison. Predicted: C-48
FAIL. Composite = ~109.5/110.

---

*(THE INERTIA PROBLEM through STEP 3: identical to V-01.)*

*(STEP 4 C-24 format requirement through C-14 compliance: identical to V-01.)*

**C-40 / C-41 compliance — Per-directive normative-register audit:**

*(C-43 discovery scope: identical to V-01. Total enforcement directives: 14.)*

*(C-47 citation instruction — interior-segment title-case prohibition: identical to V-03 —
wrong → right examples for "enforcement reminder" and "prevention" patterns both present.)*

*(C-48 expected-count declaration: Expected `*Violation type:*` MUST NOT clauses qualifying
under C-45: 5 — one per multi-adjacent C-38-compliant precision site (sites 2, 3, 4, 5, 6
from the PRECISION-SITE INVENTORY). An executor SHALL verify that exactly 5 entries in the
table below correspond to `*Violation type:*` field MUST NOT clauses; if fewer than 5 are
found, at least one qualifying clause was omitted.)*

*(C-44 / C-45 / C-46 compliance note: identical to V-01.)*

For each enforcement directive in this prompt, verify that the primary directive uses RFC
2119-style normative language. An executor SHALL enumerate each directive by its verbatim
declared block name or exact containing structure name and record a per-directive verdict.

| Directive block (verbatim declared name or containing structure) | Primary language used | C-40 verdict |
|-----------------------------------------------------------------|----------------------|-------------|
| REGISTRY GAP PROHIBITION — Failure 5 prevention (C-17) | PROHIBITED / SHALL | [PASS / FAIL] |
| Step 2A — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19) | SHALL NOT | [PASS / FAIL] |
| Step 2C — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19) | SHALL NOT | [PASS / FAIL] |
| Step 2E — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19) | SHALL NOT | [PASS / FAIL] |
| Step 2G — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19) | SHALL NOT | [PASS / FAIL] |
| Step 2H — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19) | SHALL NOT | [PASS / FAIL] |
| Failure 2 + Failure 6 prevention (C-16, C-20, C-23, C-26) — CLASSIFICATION REQUIRED AT STEP 1B | PROHIBITED / SHALL | [PASS / FAIL] |
| TABLE A `Load-shape verdict` column — *Violation type* field non-conflation directive | MUST NOT | [PASS / FAIL] |
| TABLE B `Mechanism` column — *Violation type* field non-conflation directive | MUST NOT | [PASS / FAIL] |
| TABLE C `Error code or signal` column — *Violation type* field non-conflation directive | MUST NOT | [PASS / FAIL] |
| TABLE F `Setting or API parameter` column — *Violation type* field non-conflation directive | MUST NOT | [PASS / FAIL] |
| PRECISION-SITE INVENTORY — inventory verification obligation (parenthetical note) | SHALL verify | [PASS / FAIL] |
| STEP 4 C-24 format requirement: — *Violation type* field non-conflation directive | MUST NOT | [PASS / FAIL] |
| STEP 4 C-13 compliance — Tier-ID threading: — *Violation type* field non-conflation directive | MUST NOT | [PASS / FAIL] |

If any row is FAIL: state the specific phrase found and its normative replacement.

*(C-41 satisfied: all 14 directives enumerated. C-42 satisfied: all verbatim. C-46 satisfied:
all character-exact. C-47 satisfied: wrong → right examples present for both target patterns.
C-48 NOT satisfied: pre-declared count is 5, covering only sites 2, 3, 4, 5, 6. Site 7
(STEP 4 C-13 compliance — Tier-ID threading:) is a multi-adjacent C-38-compliant precision
site whose `*Violation type:*` MUST NOT clause qualifies under C-45 and is entry 14 in the
table — but is absent from the declared count. The correct expected count is 6. A reviewer
using count = 5 as the detection threshold would accept a table with entry 14 missing without
flagging a discrepancy.)*

---

## V-05 — All Combined (C-47 with wrong→right examples, C-48 count = 6)

**Axis:** All combined — the STEP 4 C-41 preamble adds both a fully correct C-47 instruction
(wrong → right example pairs for "enforcement reminder" and "prevention" patterns) and a
correct C-48 count declaration (count = 6, covering sites 2, 3, 4, 5, 6, 7). All 14 directive
entries use verbatim declared names. No regressions from R19 V-05.

**Hypothesis:** Both C-47 and C-48 are fully satisfied. C-47 is satisfied because both the
wrong form and the correct form are shown as explicit pairs for two concrete block names. C-48
is satisfied because the pre-declared count = 6 matches the number of multi-adjacent C-38-
compliant precision sites and equals the number of `*Violation type:*` MUST NOT entries
present in the table. All other criteria unchanged from R19 V-05. Predicted: composite
110/110.

---

*(THE INERTIA PROBLEM through STEP 3: identical to V-01.)*

*(STEP 4 C-24 format requirement through C-14 compliance: identical to V-01.)*

**C-40 / C-41 compliance — Per-directive normative-register audit:**

*(C-43 discovery scope: this field covers all SHALL, SHALL NOT, MUST, MUST NOT, and PROHIBITED
obligation clauses in the prompt regardless of structural location — named enforcement block
headers, *Violation type* italic fields, inventory parenthetical notes, and PHASE ENTRY/EXIT
condition blocks. Clauses lacking a standalone block header are named by their containing
structure. Total enforcement directives in this prompt: 14.)*

*(C-47 citation instruction — interior-segment title-case prohibition: verbatim citation SHALL
retain the declared capitalization of every interior segment in multi-segment dash-delimited
block names. Interior-segment title-case normalization is PROHIBITED. Wrong → right examples:
(1) "Step 2H — Standing Enforcement Reminder — REGISTRY GAP PROHIBITED (C-17, C-19)"
    → "Step 2H — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19)";
(2) "REGISTRY GAP PROHIBITION — Failure 5 Prevention (C-17)"
    → "REGISTRY GAP PROHIBITION — Failure 5 prevention (C-17)".
An executor MUST NOT capitalize any interior segment that appears in lowercase in the declared
block label.)*

*(C-48 expected-count declaration: Expected `*Violation type:*` MUST NOT clauses qualifying
under C-45: 6 — one per multi-adjacent C-38-compliant precision site (sites 2, 3, 4, 5, 6, 7
from the PRECISION-SITE INVENTORY; sites 1 and 8 are single-adjacent and SHALL NOT carry
C-38 non-conflation directives). An executor SHALL verify that exactly 6 entries in the table
below correspond to `*Violation type:*` field MUST NOT clauses; if fewer than 6 are found,
at least one qualifying clause was omitted.)*

*(C-44 / C-45 / C-46 compliance note: all 7 embedded non-primary-location directives are
cited using the verbatim structural labels as they appear in the prompt body. Entry 8:
"TABLE A `Load-shape verdict` column" — verbatim column name from TABLE A header row. Entry
9: "TABLE B `Mechanism` column" — verbatim column name from TABLE B header row. Entry 10:
"TABLE C `Error code or signal` column" — verbatim column name from TABLE C header row.
Entry 11: "TABLE F `Setting or API parameter` column" — verbatim column name from TABLE F
header row. Entry 12: "PRECISION-SITE INVENTORY" — verbatim section header. Entry 13: "STEP 4
C-24 format requirement:" — verbatim bold sub-header including trailing colon. Entry 14: "STEP
4 C-13 compliance — Tier-ID threading:" — verbatim bold sub-header with lowercase c.
Entry 6: "Step 2H — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19)" —
verbatim bold block header with lowercase e and r in "enforcement reminder"; capital E/R would
fail C-46. No contextual derivations or paraphrases in entries 6-14.)*

For each enforcement directive in this prompt, verify that the primary directive uses RFC
2119-style normative language (SHALL, SHALL NOT, MUST, MUST NOT, PROHIBITED). An executor
SHALL enumerate each directive by its verbatim declared block name (for named blocks) or its
exact containing structure name (for embedded non-primary-location clauses) and record a
per-directive verdict.

| Directive block (verbatim declared name or containing structure) | Primary language used | C-40 verdict |
|-----------------------------------------------------------------|----------------------|-------------|
| REGISTRY GAP PROHIBITION — Failure 5 prevention (C-17) | PROHIBITED / SHALL | [PASS / FAIL] |
| Step 2A — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19) | SHALL NOT | [PASS / FAIL] |
| Step 2C — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19) | SHALL NOT | [PASS / FAIL] |
| Step 2E — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19) | SHALL NOT | [PASS / FAIL] |
| Step 2G — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19) | SHALL NOT | [PASS / FAIL] |
| Step 2H — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19) | SHALL NOT | [PASS / FAIL] |
| Failure 2 + Failure 6 prevention (C-16, C-20, C-23, C-26) — CLASSIFICATION REQUIRED AT STEP 1B | PROHIBITED / SHALL | [PASS / FAIL] |
| TABLE A `Load-shape verdict` column — *Violation type* field non-conflation directive | MUST NOT | [PASS / FAIL] |
| TABLE B `Mechanism` column — *Violation type* field non-conflation directive | MUST NOT | [PASS / FAIL] |
| TABLE C `Error code or signal` column — *Violation type* field non-conflation directive | MUST NOT | [PASS / FAIL] |
| TABLE F `Setting or API parameter` column — *Violation type* field non-conflation directive | MUST NOT | [PASS / FAIL] |
| PRECISION-SITE INVENTORY — inventory verification obligation (parenthetical note) | SHALL verify | [PASS / FAIL] |
| STEP 4 C-24 format requirement: — *Violation type* field non-conflation directive | MUST NOT | [PASS / FAIL] |
| STEP 4 C-13 compliance — Tier-ID threading: — *Violation type* field non-conflation directive | MUST NOT | [PASS / FAIL] |

If any row is FAIL: state the specific phrase found and its normative replacement.

*(C-41 satisfied: all 14 enforcement directives enumerated with individual per-directive
verdicts. C-42 satisfied: all 14 entries use verbatim declared names — entries 1-7 are
primary-location named blocks; entries 8-14 are embedded directives cited by verbatim
structural labels. C-46 satisfied: all entries reproduce every character exactly, including
lowercase e/r in "enforcement reminder" at entry 6 and lowercase c in "C-13 compliance" at
entry 14 and lowercase p in "prevention" at entry 1. C-47 satisfied: wrong → right examples
provided for "enforcement reminder" (entry 6 test surface) and "prevention" (entry 1 test
surface) — both the prohibited capitalized form and the correct lowercase form are shown as
explicit pairs. C-48 satisfied: expected count declared as 6; entries 8, 9, 10, 11, 13, 14
are the 6 qualifying `*Violation type:*` MUST NOT clauses at multi-adjacent precision sites
2, 3, 4, 5, 6, 7 — count matches, no omission detectable.)*
