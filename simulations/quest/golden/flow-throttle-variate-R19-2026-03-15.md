# flow-throttle Variate — Round 19 (v18 rubric, C-01 through C-46)
**Date:** 2026-03-15
**Rubric:** v18 (C-01 through C-46, N_essential=5, N_recommended=3, N_aspirational=38)
**Baseline ceiling:** R18 V-05 (passes C-01 through C-46; composite 110/110)

---

## State Analysis: What R18 Established vs. What R19 Must Add

**R18 V-05 coverage under v18 (confirmed):**
- C-01 through C-44: all pass — composite 110/110
- C-45 satisfied: all `*Violation type:*` MUST NOT clauses at multi-adjacent sites are
  discovered (C-43 component); all containing-structure names use verbatim column headers,
  not step labels or table names alone (C-44 component).
- C-46 satisfied: all 12 citations (6 primary-location via C-42, 6 embedded via C-44)
  reproduce every character exactly, including the trailing colon in "STEP 4 C-24 format
  requirement:" and the lowercase c in "STEP 4 C-13 compliance — Tier-ID threading:".
- Total: 12 enforcement directives; 7 precision sites.

**R19 innovation — 8th precision site + 7th named enforcement block:**

R19 introduces two structural additions:

1. **TABLE C `Error code or signal` column** as the 8th precision site, inserted at document-
   order position 4 (between TABLE B `Mechanism` at site 3 and TABLE F `Setting or API
   parameter` at former site 4). This site is multi-adjacent — bordered by TABLE B `Mechanism`
   on the left (site 3) and TABLE F on the right (new site 5) — and carries a C-38-compliant
   MUST NOT non-conflation directive in its `*Violation type:*` field, making it
   C-43-discoverable under C-45. It adds a 10th embedded directive row to the C-41 audit table.

2. **Step 2H Standing enforcement reminder** as the 7th named enforcement block. This closes
   the gap in standing-reminder coverage: reminders exist at Steps 2A, 2C, 2E, and 2G but
   not at Step 2H (MITIGATION REGISTRY), where mid-phase tier discovery during mitigation
   analysis is possible. The verbatim declared block name —
   "Step 2H — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19)" —
   has a distinctive typography (lowercase "enforcement reminder") that makes it a C-46 test
   surface for primary-block citation errors.

**Site renumbering due to insertion at position 4:**

| Former site | New site | Definition |
|-------------|----------|-----------|
| 1 | 1 | TABLE A `Limit (number + unit)` — unchanged |
| 2 | 2 | TABLE A `Load-shape verdict` — unchanged |
| 3 | 3 | TABLE B `Mechanism` — right-neighbor reference updates |
| — | 4 | TABLE C `Error code or signal` — NEW |
| 4 | 5 | TABLE F `Setting or API parameter` — left-neighbor reference updates |
| 5 | 6 | STEP 4 C-24 format requirement: — both neighbor refs update |
| 6 | 7 | STEP 4 C-13 compliance — Tier-ID threading: — both neighbor refs update |
| 7 | 8 | STEP 4 C-19 compliance — distributed reminder audit: — left-neighbor ref updates; "Site 8 has one immediate neighbor" |

**Neighbor-reference changes in `*Violation type:*` fields:**

- **TABLE B `Mechanism`** (site 3): right neighbor changes from TABLE F (old site 4) to
  TABLE C `Error code or signal` (new site 4); violation-type contrast updated accordingly.
- **TABLE C `Error code or signal`** (site 4, new): left = TABLE B `Mechanism` (site 3);
  right = TABLE F `Setting or API parameter` (site 5); mechanism-taxonomy vs.
  structural-identifier-substitution vs. parameter-specificity three-way contrast.
- **TABLE F `Setting or API parameter`** (site 5): left neighbor changes from TABLE B
  `Mechanism` (old site 3) to TABLE C `Error code or signal` (new site 4); right neighbor
  site number updates from 5 to 6.
- **STEP 4 C-24 format requirement:** (site 6): left neighbor site updates from 4 to 5;
  right neighbor site updates from 6 to 7.
- **STEP 4 C-13 compliance — Tier-ID threading:** (site 7): left neighbor site updates from
  5 to 6; right neighbor site updates from 7 to 8.
- **STEP 4 C-19 compliance — distributed reminder audit:** (site 8): left neighbor site
  updates from 6 to 7; "Site 7 has one immediate neighbor" → "Site 8 has one immediate
  neighbor."

**C-19 audit step coverage update:**

The C-19 distributed-reminder audit previously covered 4 steps (2A, 2C, 2E, 2G). With the
Step 2H reminder added, it now covers 5 steps: 2A, 2C, 2E, 2G, 2H.

**Updated enforcement directive inventory for R19:**

Named blocks (7, was 6 in R18):
1. REGISTRY GAP PROHIBITION — Failure 5 prevention (C-17)
2. Step 2A — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19)
3. Step 2C — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19)
4. Step 2E — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19)
5. Step 2G — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19)
6. Step 2H — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19) ← NEW
7. Failure 2 + Failure 6 prevention (C-16, C-20, C-23, C-26) — CLASSIFICATION REQUIRED AT STEP 1B

Embedded directives (7, was 6 in R18):
8. TABLE A `Load-shape verdict` column — *Violation type* field non-conflation directive
9. TABLE B `Mechanism` column — *Violation type* field non-conflation directive
10. TABLE C `Error code or signal` column — *Violation type* field non-conflation directive ← NEW
11. TABLE F `Setting or API parameter` column — *Violation type* field non-conflation directive
12. PRECISION-SITE INVENTORY — inventory verification obligation (parenthetical note)
13. STEP 4 C-24 format requirement: — *Violation type* field non-conflation directive
14. STEP 4 C-13 compliance — Tier-ID threading: — *Violation type* field non-conflation directive

**Total enforcement directives in R19 V-05: 14** (7 named + 7 embedded)

**C-45/C-46 test surfaces in R19:**

| Test | Criterion | Description |
|------|-----------|-------------|
| Entry 6 capitalization | C-46 | "Step 2H — Standing enforcement reminder" has lowercase e and r; capital E/R fails C-46 (primary-block character mismatch, also C-42 FAIL) |
| Entry 1 capitalization | C-46 | "Failure 5 prevention" has lowercase p; capital P fails C-46 (primary-block character mismatch) |
| Entry 10 discovery | C-45 (C-43 component) | TABLE C `Error code or signal` MUST NOT is a C-43-discoverable directive per C-45; omitting it from C-41 fails C-43 + C-45 |
| Entry 10 container name | C-45 (C-44 component) | Container must be column header "TABLE C \`Error code or signal\` column"; step label "Step 2B error signal field" fails C-44 + C-45 |

---

## Round 19 Variation Map

| Var | Axes | C-45/C-46 mechanism | Predicted |
|-----|------|---------------------|-----------|
| V-01 | Phrasing register — Step 2H reminder added; entry 6 capitalizes "Enforcement Reminder" | "Step 2H — Standing Enforcement Reminder — REGISTRY GAP PROHIBITED (C-17, C-19)" | C-42 + C-46 FAIL (~109.44) |
| V-02 | Output format — Step 2H reminder added; entry 1 capitalizes "Prevention" | "REGISTRY GAP PROHIBITION — Failure 5 Prevention (C-17)" | C-42 + C-46 FAIL (~109.44) |
| V-03 | Lifecycle emphasis — TABLE C site added; entry 10 missing from C-41 | 14 directives in prompt; C-41 has only 13 rows; TABLE C `Error code or signal` absent | C-43 + C-45 FAIL (~109.44) |
| V-04 | Role sequence — TABLE C site added; entry 10 paraphrased | Entry 10 = "Step 2B error signal field — *Violation type* non-conflation directive" (step label, not column header) | C-44 + C-45 FAIL (~109.44) |
| V-05 | All combined — 8 sites, 14 directives, all verbatim | Entry 6 verbatim lowercase; entry 10 = "TABLE C \`Error code or signal\` column" verbatim | C-42 through C-46 PASS (110/110) |

**Single-axis questions:**

Q1 (V-01 vs R18 V-05): Does capitalizing "Enforcement Reminder" in the C-41 entry for the
new Step 2H primary block fail C-46? The verbatim declared block header is "**Step 2H —
Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19):**" with lowercase e
and r in "enforcement reminder." Citing "Step 2H — Standing Enforcement Reminder — REGISTRY
GAP PROHIBITED (C-17, C-19)" (capital E, R) fails C-46 because C-46 requires reproduction
of every character of the declared label exactly, including exact capitalization. It also
fails C-42 (verbatim primary-location block name). Predicted: C-42 FAIL + C-46 FAIL.
Composite = ~109.44/110.

Q2 (V-02 vs V-01): Does capitalizing "Prevention" in the C-41 entry for REGISTRY GAP
PROHIBITION fail C-46? The verbatim declared block header is "**REGISTRY GAP PROHIBITION —
Failure 5 prevention (C-17):**" with lowercase p. Citing "REGISTRY GAP PROHIBITION — Failure
5 Prevention (C-17)" fails C-46's character-exact requirement. Also fails C-42. Predicted:
C-42 FAIL + C-46 FAIL. Composite = ~109.44/110.

Q3 (V-03 vs V-01): Does adding TABLE C `Error code or signal` with a MUST NOT directive but
failing to enumerate it in C-41 fail C-45? Under C-45, `*Violation type:*` field MUST NOT
clauses at C-38-compliant multi-adjacent extension sites qualify as C-43-discoverable. TABLE C
site 4 is multi-adjacent (between sites 3 and 5) with a C-38 MUST NOT. Omitting it from C-41
fails the C-43 component of C-45. Predicted: C-43 FAIL + C-45 FAIL. Composite = ~109.44/110.

Q4 (V-04 vs V-03): Does discovering entry 10 (present in C-41) but citing it as "Step 2B
error signal field" instead of "TABLE C `Error code or signal` column" fail C-45? C-45
specifies that the verbatim containing-structure name for C-41 enumeration is the column
header, not a step label or positional description. "Step 2B error signal field" is a step-
label-plus-description derivation, not the verbatim column header. Also fails C-44. Predicted:
C-44 FAIL + C-45 FAIL. Composite = ~109.44/110.

Q5 (V-05): Do correct verbatim citations for all 14 directives — entry 6 as "Step 2H —
Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19)" (lowercase e/r), entry
10 as "TABLE C `Error code or signal` column — *Violation type* field non-conflation directive"
(verbatim column header) — satisfy C-42 through C-46 without regressions? Hypothesis: yes —
the lowercase-e/r declaration in the Step 2H block header and the verbatim column header for
TABLE C site 4 fully satisfy C-46 and C-45 respectively. No structural criteria affected.
Predicted: composite 110/110.

---

## V-01 — Single Axis: Phrasing Register (Step 2H Entry Capitalization Error)

**Axis:** Phrasing register — the prompt adds the Step 2H Standing enforcement reminder with
the correct verbatim declared block name; the PRECISION-SITE INVENTORY has 8 rows (including
TABLE C `Error code or signal` at site 4); all new structural content (TABLE C column
definitions, updated neighbor references) is present. The sole deviation: the C-41 audit
table entry 6 cites the Step 2H primary block as "Step 2H — Standing Enforcement Reminder —
REGISTRY GAP PROHIBITED (C-17, C-19)" (capital E in "Enforcement", capital R in "Reminder")
instead of the verbatim "Step 2H — Standing enforcement reminder — REGISTRY GAP PROHIBITED
(C-17, C-19)" (lowercase e, r). Entries 1-5 and 7-14 retain verbatim citations.

**Hypothesis:** The verbatim declared block header in the prompt body is "**Step 2H —
Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19):**" with lowercase e
and r. Citing "Step 2H — Standing Enforcement Reminder — REGISTRY GAP PROHIBITED (C-17,
C-19)" capitalizes two characters that appear lowercase in the declared label. C-46 requires
reproduction of every character of the declared label exactly, including exact capitalization;
C-42 requires citation by verbatim declared block name. Capital E/R makes the citation non-
verbatim on both counts. Predicted: C-42 FAIL + C-46 FAIL. Composite = ~109.44/110.

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
per-directive verdict:

| Directive block (verbatim declared name or containing structure) | Primary language used | C-40 verdict |
|-----------------------------------------------------------------|----------------------|-------------|
| REGISTRY GAP PROHIBITION — Failure 5 prevention (C-17) | PROHIBITED / SHALL | [PASS / FAIL] |
| Step 2A — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19) | SHALL NOT | [PASS / FAIL] |
| Step 2C — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19) | SHALL NOT | [PASS / FAIL] |
| Step 2E — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19) | SHALL NOT | [PASS / FAIL] |
| Step 2G — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19) | SHALL NOT | [PASS / FAIL] |
| Step 2H — Standing Enforcement Reminder — REGISTRY GAP PROHIBITED (C-17, C-19) | SHALL NOT | [PASS / FAIL] |
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
verdicts. C-42 NOT satisfied: entry 6 cites "Step 2H — Standing Enforcement Reminder —
REGISTRY GAP PROHIBITED (C-17, C-19)" with capital E and R — the verbatim declared block
header is "**Step 2H — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19):**"
with lowercase e and r; C-46 requires every character to match exactly, including
capitalization. C-42 FAIL + C-46 FAIL.)*

---

## V-02 — Single Axis: Output Format (REGISTRY GAP PROHIBITION Capitalization Error)

**Axis:** Output format — the prompt adds the Step 2H Standing enforcement reminder with the
correct verbatim block header (lowercase "enforcement reminder"); the PRECISION-SITE INVENTORY
has 8 rows; all new structural content is present. The sole deviation: the C-41 audit table
entry 1 cites the REGISTRY GAP PROHIBITION block as "REGISTRY GAP PROHIBITION — Failure 5
Prevention (C-17)" (capital P in "Prevention") instead of the verbatim "REGISTRY GAP
PROHIBITION — Failure 5 prevention (C-17)" (lowercase p). All other entries (2-14) retain
verbatim citations, including the corrected Step 2H entry ("Step 2H — Standing enforcement
reminder — REGISTRY GAP PROHIBITED (C-17, C-19)").

**Hypothesis:** The verbatim declared block header is "**REGISTRY GAP PROHIBITION — Failure 5
prevention (C-17):**" with lowercase p in "prevention." Citing "REGISTRY GAP PROHIBITION —
Failure 5 Prevention (C-17)" with capital P fails C-46's character-exact requirement and C-42's
verbatim primary-block name requirement. Predicted: C-42 FAIL + C-46 FAIL.
Composite = ~109.44/110.

---

*(THE INERTIA PROBLEM: identical to V-01.)*

*(Role setup: identical to V-01.)*

*(PRECISION-SITE INVENTORY: identical to V-01 — eight sites, same hierarchy labels and
violation types, same verification obligation parenthetical.)*

*(STEP 1 — TIER REGISTRY: identical to V-01. Block name "REGISTRY GAP PROHIBITION — Failure 5
prevention (C-17)" declared verbatim in prompt body; this is the label that entry 1 must cite.
All gates, phase conditions, and Step 1B Failure 2 + Failure 6 prevention block: identical to
V-01.)*

*(STEP 2 through STEP 3: identical to V-01 — all sections present with PHASE ENTRY/EXIT
conditions, all five Standing enforcement reminder blocks at Steps 2A, 2C, 2E, 2G, 2H, all
*Violation type* italic fields including TABLE B `Mechanism` updated right-neighbor reference
to TABLE C site 4, TABLE C `Error code or signal` column definitions, TABLE F updated left-
neighbor reference to TABLE C site 4.)*

*(STEP 4 through C-14 compliance: identical to V-01.)*

**C-40 / C-41 compliance — Per-directive normative-register audit:**

*(C-43 discovery scope: identical to V-01. Total enforcement directives: 14.)*

*(C-46 note: entry 1 introduces a capitalization error — "REGISTRY GAP PROHIBITION — Failure 5
Prevention (C-17)" uses capital P in "Prevention" where the verbatim declared block header
"**REGISTRY GAP PROHIBITION — Failure 5 prevention (C-17):**" uses lowercase p. C-46 requires
every character exact. Entry 6 corrected to verbatim "Step 2H — Standing enforcement reminder
— REGISTRY GAP PROHIBITED (C-17, C-19)" (lowercase e/r). Entries 2-5, 7-14 verbatim. C-42
FAIL + C-46 FAIL on entry 1.)*

| Directive block (verbatim declared name or containing structure) | Primary language used | C-40 verdict |
|-----------------------------------------------------------------|----------------------|-------------|
| REGISTRY GAP PROHIBITION — Failure 5 Prevention (C-17) | PROHIBITED / SHALL | [PASS / FAIL] |
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

*(C-41 satisfied: all 14 directives enumerated with per-directive verdicts. C-43 satisfied:
all 7 embedded directives discovered. C-44 satisfied: entries 8-14 use verbatim structural
labels. C-45 satisfied: TABLE C `Error code or signal` column entry 10 is present and uses
verbatim column header. C-42 NOT satisfied: entry 1 cites "REGISTRY GAP PROHIBITION — Failure
5 Prevention (C-17)" with capital P — verbatim declared label has lowercase p. C-46 NOT
satisfied: entry 1 fails character-exact reproduction. C-42 FAIL + C-46 FAIL.)*

---

## V-03 — Single Axis: Lifecycle Emphasis (TABLE C Site Added, Entry 10 Missing)

**Axis:** Lifecycle emphasis — the prompt adds TABLE C `Error code or signal` column
definitions (site 4) with a MUST NOT non-conflation directive; the PRECISION-SITE INVENTORY
has 8 rows; the Step 2H Standing enforcement reminder is present with verbatim block name;
all updated neighbor references are included. The sole deviation: the C-41 audit table has
only 13 rows — the entry for "TABLE C `Error code or signal` column — *Violation type* field
non-conflation directive" is missing. All other entries (1-9, 11-14) are present and verbatim.

**Hypothesis:** The TABLE C `Error code or signal` `*Violation type:*` field contains a MUST
NOT non-conflation clause; C-45 establishes that MUST NOT clauses at C-38-compliant multi-
adjacent extension sites qualify as C-43-discoverable. TABLE C site 4 is multi-adjacent
(bordered by TABLE B Mechanism at site 3 and TABLE F at site 5) and carries a C-38 MUST NOT.
Omitting entry 10 from the C-41 audit table fails the C-43 component of C-45 (discovery
criterion). Predicted: C-43 FAIL + C-45 FAIL. Composite = ~109.44/110.

---

*(THE INERTIA PROBLEM: identical to V-01.)*

*(Role setup: identical to V-01.)*

**PRECISION-SITE INVENTORY**

*(Required before any table is defined — C-33 + C-35 + C-37 + C-39. Identical to V-01 —
eight sites including TABLE C `Error code or signal` at site 4, same hierarchy labels,
violation types, and verification obligation parenthetical.)*

*(STEP 1 through STEP 3: identical to V-01 — all structural content including TABLE C column
definitions with MUST NOT non-conflation directive at site 4, updated neighbor references in
TABLE B `Mechanism` and TABLE F *Violation type* fields, Step 2H Standing enforcement reminder
present with verbatim lowercase header, C-19 distributed-reminder audit updated to cover 5
steps including Step 2H.)*

*(STEP 4 through C-14 compliance: identical to V-01.)*

**C-40 / C-41 compliance — Per-directive normative-register audit:**

*(C-43 discovery scope: this field covers all SHALL, SHALL NOT, MUST, MUST NOT, and PROHIBITED
obligation clauses in the prompt regardless of structural location — named enforcement block
headers, *Violation type* italic fields, inventory parenthetical notes, and PHASE ENTRY/EXIT
condition blocks. Clauses lacking a standalone block header are named by their containing
structure. Total enforcement directives in this prompt: 14.)*

*(C-45 / C-43 note: entry 10 is MISSING from the audit table below. The TABLE C `Error code
or signal` column `*Violation type:*` field contains a MUST NOT non-conflation clause; under
C-45, MUST NOT clauses at C-38-compliant multi-adjacent extension sites are C-43-discoverable
directives and MUST be enumerated in this audit. Site 4 is multi-adjacent (between sites 3
and 5) with a C-38 MUST NOT; the entry is absent. C-43 NOT satisfied; C-45 NOT satisfied.)*

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
| TABLE F `Setting or API parameter` column — *Violation type* field non-conflation directive | MUST NOT | [PASS / FAIL] |
| PRECISION-SITE INVENTORY — inventory verification obligation (parenthetical note) | SHALL verify | [PASS / FAIL] |
| STEP 4 C-24 format requirement: — *Violation type* field non-conflation directive | MUST NOT | [PASS / FAIL] |
| STEP 4 C-13 compliance — Tier-ID threading: — *Violation type* field non-conflation directive | MUST NOT | [PASS / FAIL] |

If any row is FAIL: state the specific phrase found and its normative replacement.

*(C-41 satisfied: all 13 enumerated directives receive per-directive verdicts. C-42 satisfied:
all 7 named blocks verbatim including "Step 2H — Standing enforcement reminder — REGISTRY GAP
PROHIBITED (C-17, C-19)" (lowercase e/r). C-43 NOT satisfied: the TABLE C `Error code or
signal` column MUST NOT non-conflation directive (directive 10 of 14) is absent — only 13 of
14 directives discovered. C-45 NOT satisfied: the C-43 discovery component of C-45 fails
because the MUST NOT clause at multi-adjacent site 4 is not enumerated. C-44 cannot be
assessed for the missing entry.)*

---

## V-04 — Single Axis: Role Sequence (TABLE C Site Added, Entry 10 Paraphrased)

**Axis:** Role sequence — the prompt adds TABLE C `Error code or signal` column definitions
(site 4) and Step 2H Standing enforcement reminder identically to V-03; the C-41 audit table
has 14 rows — entry 10 is present but uses a positional-contextual description "Step 2B error
signal field — *Violation type* non-conflation directive" rather than the verbatim column-
header label "TABLE C `Error code or signal` column — *Violation type* field non-conflation
directive." All other sections with 8-site changes are identical to V-03.

**Hypothesis:** Entry 10 is present (C-43 component of C-45 satisfied — all 14 directives
discovered), but the citation "Step 2B error signal field" is derived from the step name and
the column's functional role — it is not the verbatim column header label appearing in TABLE
C's header row. C-45 specifies the column header as the required containing-structure type;
"Step 2B error signal field" is a step-label-plus-description that does not match any
declared structural label in the prompt body. C-44 requires the verbatim structural label;
C-45 specifically requires the column header for this class of embedded directive. Predicted:
C-44 FAIL + C-45 FAIL. Composite = ~109.44/110.

---

*(THE INERTIA PROBLEM: identical to V-01.)*

*(Role setup: identical to V-01.)*

*(PRECISION-SITE INVENTORY: identical to V-03 — eight sites including TABLE C `Error code or
signal` at site 4, with all hierarchy labels and violation types.)*

*(STEP 1 through STEP 3: identical to V-03 — TABLE C column definitions with MUST NOT present,
updated neighbor references, Step 2H Standing enforcement reminder with verbatim lowercase
block name, 5-step C-19 audit.)*

*(STEP 4 through C-14 compliance: identical to V-03.)*

**C-40 / C-41 compliance — Per-directive normative-register audit:**

*(C-43 discovery scope: identical to V-03. Total enforcement directives in this prompt: 14.)*

*(C-44 / C-45 note: entries 8-9, 11-14 use verbatim structural labels. Entry 10 is present
(C-43 satisfied) but uses a positional descriptor: "Step 2B error signal field" is derived
from the step name (Step 2B) and the column's functional description — it does not appear as
a structural label anywhere in the prompt. The verbatim column header label is "Error code or
signal" and the containing-structure citation is "TABLE C `Error code or signal` column."
C-44 requires the exact containing-structure label from the prompt body; "Step 2B error signal
field" fails. C-45 additionally requires that the containing-structure name for Violation type
embedded directives at multi-adjacent sites be the column header, not a step label or positional
description. C-44 NOT satisfied + C-45 NOT satisfied: entry 10 non-verbatim by step-label
paraphrase.)*

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
| Step 2B error signal field — *Violation type* non-conflation directive | MUST NOT | [PASS / FAIL] |
| TABLE F `Setting or API parameter` column — *Violation type* field non-conflation directive | MUST NOT | [PASS / FAIL] |
| PRECISION-SITE INVENTORY — inventory verification obligation (parenthetical note) | SHALL verify | [PASS / FAIL] |
| STEP 4 C-24 format requirement: — *Violation type* field non-conflation directive | MUST NOT | [PASS / FAIL] |
| STEP 4 C-13 compliance — Tier-ID threading: — *Violation type* field non-conflation directive | MUST NOT | [PASS / FAIL] |

If any row is FAIL: state the specific phrase found and its normative replacement.

*(C-41 satisfied: all 14 enforcement directives enumerated with individual per-directive
verdicts. C-42 satisfied: all 7 named blocks verbatim. C-43 satisfied: all 7 non-primary
directives discovered — 14 total, 14 rows. C-44 NOT satisfied: entry 10 cites "Step 2B error
signal field" — a positional-contextual description not present as a structural label in the
prompt body; the verbatim TABLE C column header is `Error code or signal` and the correct
containing-structure citation is "TABLE C `Error code or signal` column." C-45 NOT satisfied:
the containing-structure name for this C-38-compliant multi-adjacent extension site (site 4)
uses a step label rather than the required column header form. C-44 FAIL + C-45 FAIL.)*

---

## V-05 — All Axes Combined (C-43 through C-46 Full Compliance, 8th Precision Site)

**Axis:** Full combination — 8th precision site (TABLE C `Error code or signal` column at
site 4) added with complete column definitions and MUST NOT non-conflation directive; Step 2H
Standing enforcement reminder added with verbatim lowercase block name; all neighbor
references in `*Violation type:*` fields updated to reflect renumbered sites (sites 1-8); C-41
audit table has 14 rows with all 7 embedded-directive entries citing verbatim column-header
structural labels from the prompt body, including entry 10 = "TABLE C `Error code or signal`
column — *Violation type* field non-conflation directive" and entry 6 = "Step 2H — Standing
enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19)" (lowercase e/r).

**Hypothesis:** All 7 embedded-directive entries cite verbatim structural labels. Entry 10
uses "TABLE C `Error code or signal` column" — the exact column header text from TABLE C's
header row, following the pattern established for entries 8, 9, and 11. Entry 6 uses the exact
declared block name "Step 2H — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17,
C-19)" with lowercase e and r as they appear in the block header. All neighbor references
updated for 8 sites. C-43 through C-46 all pass; composite 110/110.

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
condition blocks. Clauses lacking a standalone block header are named by their exact containing
structure. Total enforcement directives in this prompt: 14.)*

*(C-44 / C-45 / C-46 compliance note: all 7 embedded non-primary-location directives are
cited using the verbatim structural labels as they appear in the prompt body. Entry 8: "TABLE A
`Load-shape verdict` column" — verbatim column name from TABLE A header row. Entry 9: "TABLE B
`Mechanism` column" — verbatim column name from TABLE B header row. Entry 10: "TABLE C `Error
code or signal` column" — verbatim column name from TABLE C header row, matching the established
pattern for entries 8, 9, and 11. Entry 11: "TABLE F `Setting or API parameter` column" —
verbatim column name from TABLE F header row. Entry 12: "PRECISION-SITE INVENTORY" — verbatim
section header. Entry 13: "STEP 4 C-24 format requirement:" — verbatim bold sub-header
"**C-24 format requirement:**" as it appears in STEP 4, including trailing colon. Entry 14:
"STEP 4 C-13 compliance — Tier-ID threading:" — verbatim bold sub-header with lowercase c.
Entry 6: "Step 2H — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19)" —
verbatim bold block header "**Step 2H — Standing enforcement reminder — REGISTRY GAP
PROHIBITED (C-17, C-19):**" as it appears in Step 2H, with lowercase e and r in "enforcement
reminder." No contextual derivations or paraphrases in entries 6-14.)*

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

*(C-41 satisfied: all 14 enforcement directives enumerated by their declared or containing-
structure names with individual per-directive verdicts. C-42 satisfied: all 7 primary-location
directives cited by their verbatim declared block name exactly as they appear in the prompt
body — including "Step 2H — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17,
C-19)" with lowercase e and r. C-43 satisfied: all 7 non-primary-location directives
discovered — TABLE A, TABLE B, TABLE C, and TABLE F *Violation type* field non-conflation
directives, PRECISION-SITE INVENTORY parenthetical obligation, and both STEP 4 *Violation
type* field non-conflation directives. C-44 satisfied: all 7 embedded-directive entries cite
their containing structures using the verbatim structural labels from the prompt body —
"TABLE C `Error code or signal` column" is the exact column header text from TABLE C's header
row. C-45 satisfied: all `*Violation type:*` MUST NOT clauses at C-38-compliant multi-adjacent
sites (sites 2, 3, 4, 5, 6, 7) are discovered and cited using verbatim column headers, not
step labels or table names alone. C-46 satisfied: all 14 citations reproduce every character
of the declared label exactly, including lowercase "enforcement reminder" in entry 6 and
lowercase c in entry 14.)*
