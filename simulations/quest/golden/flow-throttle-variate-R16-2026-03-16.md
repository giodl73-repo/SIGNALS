# flow-throttle Variate — Round 16

**Date:** 2026-03-16
**Rubric:** v16 (C-01–C-41, N_essential=5, N_recommended=3, N_aspirational=33)
**Max composite:** 255 | **Baseline ceiling:** R15 best (250/255 under v16 — C-41 FAIL)

---

## State Analysis: What R15 Has vs. What R16 Must Add

**R15 coverage under v16 (assessed):**
- C-01 through C-40: all pass (best R15 variant)
- C-41: FAIL — R15 V-04's count check appears as a bullet item inside the Role 2
  PHASE 1 ENTRY CONDITION rather than as a structural gate. The count is declared (C-38
  PASS), the inventory is closed (C-39 PASS), the PROHIBITED clause is co-located in
  the inventory (C-40 PASS), but the count check does not block Phase 1 from opening —
  it is a verification note that an executor can read and proceed past without acting on.
  A count discrepancy is detectable only after Phase 1 produces output, not before.

**C-41 gap in R15:**

C-41 requires the annotation inventory count declared at Section C (satisfying C-38) to
be the activation condition for Role 2 / Phase 1, not a line item inside it. The
distinction: C-38 asks "is the count declared?"; C-41 asks "does a count discrepancy
prevent Phase 1 from opening?" An output passes C-38 when the inventory header states
"This section declares 7 required annotations." It passes C-41 only when the Role 2 entry
condition is structured so that confirming count = 7 is required before the body-construction
role runs — a count of 6 triggers a structural return to Role 1, not a note for the
executor to address after analysis.

**Round 16 variation map:**

| Variation | Axes | C-41 mechanism | Predicted composite |
|-----------|------|----------------|---------------------|
| V-01 | Lifecycle emphasis (single) | Standalone INVENTORY GATE phase — own header, CLEARED/BLOCKED outcomes | 255/255 |
| V-02 | Output format (single) | Count check as structured verification table with Expected/Actual/Verdict | 255/255 |
| V-03 | Role sequence (single) | Dedicated Role 1.5 (INVENTORY VERIFIER) with single-responsibility gate | 255/255 |
| V-04 | Phrasing register + lifecycle emphasis | SHALL-dominant gate block with SHALL NOT proceed at every decision point | 255/255 |
| V-05 | Role sequence + output format + inertia framing | Handoff table + gated checklist + named "looks complete" failure mode rejected | 255/255 |

---

## V-01

**Axis:** Lifecycle emphasis (single-axis)

**Hypothesis:** Expressing C-41 as a standalone named phase — "INVENTORY GATE" — positioned
between FORMAT CONTRACT COMPLETE and Role 2's opening, with its own section header, explicit
GATE CLEARED / GATE BLOCKED outcomes, and a restart procedure, creates stronger lifecycle
salience than a bullet item inside a Phase 1 entry condition. An executor cannot skip the
gate because it appears as a named section with an observable outcome state that must be
resolved before Role 2 is named.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
the rate-limited system described in the signal. Treat the stated request volume as 1x
nominal; also analyze at 2x and 5x.

This prompt uses a three-phase activation structure: **Role 1 (FORMAT CONTRACT)** produces the
precision inventory and annotation contract; the **INVENTORY GATE** verifies the contract is
complete before any body analysis begins; **Role 2 (DOMAIN EXPERT)** runs only after the
INVENTORY GATE reaches GATE CLEARED. The tables below are the primary output — every cell
SHALL be filled. Produce sections in the order shown.

---

**ROLE 1 — FORMAT CONTRACT**

**Section A — Precision-site inventory**

This section inventories every location in this prompt where a column definition carries a
violation-type annotation. An executor SHALL verify, at the INVENTORY GATE, that every listed
site is present in Section C and that its annotation is placed at its anchor site. Count: 7
precision sites across 5 tables.

| Site-ID | Table | Column | Violation type | C-27 hierarchy |
|---------|-------|--------|----------------|----------------|
| S-01 | TABLE A | `Limit (number + unit)` | vague-label substitution | primary |
| S-02 | TABLE A | `Binding?` | assertion-without-causal-reason | adjacent-1 (S-01/S-02/S-03 group) |
| S-03 | TABLE A | `Failure mode` | insufficient-categorical-diversity | adjacent-2 (S-01/S-02/S-03 group) |
| S-04 | TABLE B | `Mechanism` | generic-term substitution | primary |
| S-05 | TABLE C | `Error code or signal` | plain-description substitution | primary |
| S-06 | TABLE E | `Type` | category-absence-undetectable | primary |
| S-07 | TABLE F | `Setting or API parameter` | category-of-action substitution | primary |

Multi-adjacent sites S-01, S-02, S-03 share TABLE A. Non-conflation count: 3 violation types
at TABLE A precision sites. An executor SHALL NOT treat vague-label substitution,
assertion-without-causal-reason, and insufficient-categorical-diversity as variants of a
single "incomplete entry" failure. Each is a distinct violation with a distinct pass condition.

**Section B — Format contract**

**TABLE A — `Limit (number + unit)` (S-01, primary):**
A specific number with a unit is required (e.g., "1,000 req/min").
- *Violation type: vague-label substitution — a vague label ("limited", "throttled") substituted
  for a specific number-with-unit.*
- Compliance failure condition (C-27/S-01): An entry using a vague label instead of a
  number-with-unit fails this column.

**TABLE A — `Binding?` (S-02, adjacent-1):**
Y/N with a mechanism that explains why this tier is or is not binding at the relevant band.
- *Violation type: assertion-without-causal-reason — Binding? = Y with no mechanism stated.*
- Compliance failure condition (C-27/S-02): A Y entry without a named causal mechanism fails
  this column. Note: S-02 catches unsupported binary assertions; S-01 catches numeric
  imprecision; these are non-overlapping failure modes.

**TABLE A — `Failure mode` (S-03, adjacent-2):**
Name the observable failure type at saturation. At least two distinct values SHALL appear
across all TABLE A rows.
- *Violation type: insufficient-categorical-diversity — fewer than two distinct failure mode
  values across all TABLE A rows.*
- Compliance failure condition (C-27/S-03): A TABLE A where all `Failure mode` entries share
  the same value fails this column's diversity requirement. Note: S-03 catches categorical
  flattening; S-01 catches numeric imprecision; S-02 catches assertion gaps. Three distinct
  failure modes for three adjacent sites.

**TABLE B — `Mechanism` (S-04, primary):**
Name the specific throttle propagation mechanism from the permitted set: queue-fill,
connection-hold, retry-amplification, dependency-stall, timeout-cascade.
- *Violation type: generic-term substitution — "blocked", "throttled", or "slowed" in place
  of a named mechanism from the permitted set.*
- Compliance failure condition (C-27/S-04): A `Mechanism` entry using a generic term fails
  this column.

**TABLE C — `Error code or signal` (S-05, primary):**
Record the specific HTTP status code or platform signal identifier (e.g., "HTTP 429", "TL-0001").
- *Violation type: plain-description substitution — "request fails" in place of "HTTP 429".*
- Compliance failure condition (C-27/S-05): A plain description rather than a code or signal
  identifier fails this column.

**TABLE E — `Type` (S-06, primary):**
Classify by type: throughput-risk, visibility-risk, cascade-risk, recovery-risk. Every row
SHALL have a named type.
- *Violation type: category-absence-undetectable — a risk entry with no Type value, making
  category omission undetectable by column scan.*
- Compliance failure condition (C-27/S-06): A row with a blank or uncategorized `Type` entry
  fails this column.

**TABLE F — `Setting or API parameter` (S-07, primary):**
The exact configuration key, connector property, or API attribute name (e.g.,
`connector.retryPolicy`).
- *Violation type: category-of-action substitution — "add retry logic" in place of a named
  parameter identifier.*
- Compliance failure condition (C-27/S-07): A row naming a category of action rather than a
  specific parameter identifier fails this column.

**Section C — Annotation inventory**

This section declares **7 required annotations**. Count-scan verification: expected rows = 7.
A row count below 7 is a completeness gap detectable without reading annotation content.

| Annot-ID | Anchor site | Failure-mode label | Prohibited form (example) |
|----------|------------|-------------------|-----------------------------|
| Annot-01 | TABLE A — `Limit (number + unit)` | vague-label substitution | "limited" in place of "1,200 req/min" |
| Annot-02 | TABLE A — `Binding?` | assertion-without-causal-reason | Binding? = Y with no mechanism named |
| Annot-03 | TABLE A — `Failure mode` | insufficient-categorical-diversity | all rows: "timeout" |
| Annot-04 | TABLE B — `Mechanism` | generic-term substitution | "blocked" in place of "queue-fill" |
| Annot-05 | TABLE C — `Error code or signal` | plain-description substitution | "request fails" in place of "HTTP 429" |
| Annot-06 | TABLE E — `Type` | category-absence-undetectable | risk row with no Type value |
| Annot-07 | TABLE F — `Setting or API parameter` | category-of-action substitution | "add retry logic" in place of `connector.retryPolicy` |

This inventory is closed. An annotation not listed here does not exist as a contract
requirement. An annotation listed here that is absent from its anchor site in the body is a
FORMAT CONTRACT violation.

PROHIBITED: annotation dropout at any anchor site listed in this inventory — *prevents
handoff-boundary gap: an annotation absent from its anchor site is detectable only by full
body scan; this clause converts dropout into a contract violation identifiable by Annot-ID
lookup at this inventory without traversing the body. This PROHIBITED clause is physically
co-located inside the annotation inventory as required.*

**FORMAT CONTRACT COMPLETE**

---

**INVENTORY GATE — Phase 1 unlock procedure**

This is a standalone phase between FORMAT CONTRACT COMPLETE and Role 2. **Role 2 SHALL NOT
open until this gate reaches GATE CLEARED.**

**Gate procedure:**

1. Count the Annot-ID rows in Section C above.
2. Compare to declared count: Section C declares 7 required annotations; expected row count = 7.
3. Apply outcome:
   - Row count = 7 → **GATE CLEARED** — proceed to Role 2 / Phase 1.
   - Row count < 7 → **GATE BLOCKED** — the annotation inventory is incomplete. FORMAT
     CONTRACT COMPLETE was stated prematurely. Return to Role 1, complete Section C to 7
     rows, re-state FORMAT CONTRACT COMPLETE, then re-enter this gate.

**GATE STATUS: [ CLEARED / BLOCKED ]** — fill this field before opening Phase 1. An executor
SHALL NOT open Phase 1 until GATE STATUS = CLEARED is explicitly recorded.

---

**ROLE 2 — DOMAIN EXPERT**

**REGISTRY GAP PROHIBITION — Failure 5 prevention (C-17):** Tiers discovered during Step 2
are scope violations — evidence that the enumeration phase was incomplete. PROHIBITED: assigning
a new T-NN during Step 2 as a fill-in step. An executor SHALL return to TABLE A, register the
tier with all columns filled, and SHALL restart from the point of discovery. This prohibition
SHALL be restated at each Step 2 section where mid-phase discovery could occur.

---

**Step 1A — VOLUME ANALYST: TIER IDENTIFICATION AND LIMITS**

**PHASE ENTRY CONDITION:** Step 1A SHALL be entered after INVENTORY GATE = CLEARED and the
signal input has been read in full.

*(Volume analyst role: identify every rate-limiting component; record numeric limit, scope,
binding status with causal reason, failure mode, failure visibility window, and recovery time.
Leave `Load-shape verdict` as placeholder — assign at Step 1B.)*

**TABLE A — THROTTLE TIER INVENTORY**

| Tier-ID | Component | Limit (number + unit) | Scope | STATUS 1x | STATUS 2x | STATUS 5x | Binding? (Y/N + mechanism) | Failure mode | Load-shape verdict | Failure visibility window | Recovery time |
|---------|-----------|----------------------|-------|-----------|-----------|-----------|---------------------------|--------------|-------------------|--------------------------|---------------|
| T-01    |           |                      |       |           |           |           |                           |              | [Step 1B]         |                          |               |
| T-02    |           |                      |       |           |           |           |                           |              | [Step 1B]         |                          |               |
| ...     |           |                      |       |           |           |           |                           |              | [Step 1B]         |                          |               |

**STEP 1A GATE:** Closed when every T-NN row is populated (except `Load-shape verdict`),
`Limit` contains no vague labels, `Binding?` entries include causal mechanisms, and at least
two distinct `Failure mode` values appear across rows. An executor SHALL NOT open Step 1B
until this gate is cleared.

**PHASE EXIT CONDITION:** Step 1A is exited when the STEP 1A GATE is cleared.

---

**Step 1B — LOAD-SHAPE ANALYST: CLASSIFICATION**

**PHASE ENTRY CONDITION:** Step 1B SHALL be entered only after STEP 1A GATE is cleared.

**Failure 2 + Failure 6 prevention — CLASSIFICATION REQUIRED AT STEP 1B:** An executor SHALL
assign `Load-shape verdict` for every TABLE A tier at this step. PROHIBITED: leaving any
`Load-shape verdict` cell as placeholder or deferring classification to Step 2G.

**Escape-route frame:** The temptation to defer is the "STATUS tracks volume thresholds"
framing — because TABLE A STATUS columns use OK/HIT/SAT for volume thresholds, load-shape
classification appears out of scope for the registry and naturally belonging in "LOAD SHAPE
COMPARISON." This frame is self-defeating: load-shape classification requires the registered
`Limit` value available now at Step 1B, and Step 2G depends on per-tier Load-shape verdicts
to produce meaningful comparisons — deferring creates a circular dependency where the
downstream section that would receive shape classification is itself dependent on the per-tier
verdict the registry was supposed to supply. Step 1B exists precisely to foreclose this
dependency.

For each TABLE A tier, update `Load-shape verdict`:
- SHAPE-NEUTRAL or SHAPE-SENSITIVE
- Numeric rate differential between uniform and burst arrival at this tier's limit
- Mechanism explaining the differential

**STEP 1B GATE:** Closed when every TABLE A row has a `Load-shape verdict` containing a
SHAPE-NEUTRAL or SHAPE-SENSITIVE assignment, numeric differential, and mechanism. No
placeholder SHALL remain.

**PHASE EXIT CONDITION:** Step 1B is exited when the STEP 1B GATE is cleared. An executor
SHALL NOT begin Step 2 until this phase exit condition is met.

---

**Step 2A — BACKPRESSURE PROPAGATION TRACE (TABLE B)**

**PHASE ENTRY CONDITION:** Step 2A SHALL be entered only after TABLE A is closed.

**Step 2A — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19):** Tiers
appearing in backpressure analysis not in TABLE A are scope violations. An executor SHALL NOT
assign a new T-NN here. Return to TABLE A, register the tier, then continue.

| Hop | From (Tier-ID) | To component | Mechanism | Observable effect |
|-----|----------------|--------------|-----------|-------------------|
| 1   |                |              |           |                   |
| 2   |                |              |           |                   |
| ... |                |              |           |                   |

Minimum 2 hops. `From (Tier-ID)` SHALL reference a T-NN from TABLE A. `Mechanism` SHALL use
a value from the permitted set: queue-fill, connection-hold, retry-amplification,
dependency-stall, timeout-cascade.

---

**Step 2B — USER EXPERIENCE CATALOG (TABLE C)**

**PHASE ENTRY CONDITION:** Step 2B SHALL be entered after Step 2A is closed. One row per
TABLE A Tier-ID. No tier SHALL be omitted.

| Tier-ID | Error code or signal | Retry-After present? (Y/N) | Retry-After surfaced to caller? (Y/N) | Visible in run history? (Y/N/SILENT) | Failure if Retry-After ignored |
|---------|---------------------|---------------------------|--------------------------------------|--------------------------------------|-------------------------------|
| T-01    |                     |                           |                                      |                                      |                               |
| T-02    |                     |                           |                                      |                                      |                               |

---

**Step 2C — UNPROTECTED BURST PATHS (TABLE D)**

**PHASE ENTRY CONDITION:** Step 2C SHALL be entered after Step 2B is closed.

**Step 2C — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19):** Tiers
referenced in burst path analysis not in TABLE A are scope violations. An executor SHALL NOT
assign a new T-NN here. Return to TABLE A.

At least one row SHALL be present. If no unprotected path exists, row 1 SHALL state the
conclusion with at least two named controls as evidence.

| Path-ID | Entry component | Gap reason (structural gap or named controls) | Tier-IDs involved | Consequence at burst volume |
|---------|----------------|-----------------------------------------------|-------------------|-----------------------------|
| P-01    |                |                                               |                   |                             |

---

**Step 2D — TIER RISK RANKING (TABLE E)**

**PHASE ENTRY CONDITION:** Step 2D SHALL be entered after Step 2C is closed.

All TABLE A tiers SHALL appear, ordered by business risk (highest to lowest). One sentence per
tier with rationale. For the top-ranked tier, `Failure visibility window` and `Recovery time`
from TABLE A SHALL be referenced.

| Rank | Tier-ID | Type | Risk rationale |
|------|---------|------|----------------|
| 1    |         |      |                |
| 2    |         |      |                |
| ...  |         |      |                |

---

**Step 2E — CASCADE SCENARIO**

**PHASE ENTRY CONDITION:** Step 2E SHALL be entered after Step 2D is closed.

**Step 2E — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19):** Tiers
introduced during cascade trace not in TABLE A are scope violations. An executor SHALL NOT
assign a new T-NN here. Return to TABLE A.

Trace one concrete cascade from the 1x binding constraint. T-NN identifiers SHALL be used
throughout. Each causal link SHALL be stated explicitly. Minimum three tiers, each step caused
by the previous.

---

**Step 2F — RETRY-AFTER GAP ASSESSMENT**

**PHASE ENTRY CONDITION:** Step 2F SHALL be entered after Step 2E is closed.

For the 1x binding constraint tier: is Retry-After present and surfaced to the caller? If
absent, name the failure mode precisely — retry storm (exponential backoff without
Retry-After guidance) vs. quota exhaustion (circuit breaker approach required).

---

**Step 2G — LOAD SHAPE COMPARISON**

**PHASE ENTRY CONDITION:** Step 2G SHALL be entered after Step 2F is closed.

**Step 2G — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19):** Tiers
introduced during load shape analysis not in TABLE A are scope violations. Return to TABLE A.

Using TABLE A `Limit` values and `Load-shape verdict` column (classified at Step 1B), compare
1x nominal at two arrival patterns. Identical total count; only arrival distribution differs.

- **UNIFORM arrival** — state per-second arrival rate; state which tiers are HIT or SAT.
- **BURST arrival** — state burst fraction and peak per-second rate; state which tiers are
  HIT or SAT and why.

At least one numeric comparison where status differs at identical total count SHALL be present.

---

**Step 2H — MITIGATION REGISTRY (TABLE F)**

**PHASE ENTRY CONDITION:** Step 2H SHALL be entered after Step 2G is closed.

**Step 2H — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19):** Tiers
referenced in mitigation entries not in TABLE A are scope violations. An executor SHALL NOT
assign a new T-NN here. Return to TABLE A.

| MR-ID | Source T-NN | Gap type | Component | Setting or API parameter | Change | Expected outcome |
|-------|-------------|----------|-----------|--------------------------|--------|-----------------|
| MR-01 |             |          |           |                          |        |                 |
| MR-02 |             |          |           |                          |        |                 |

---

**ROLE 3 — AUDIT**

**Audit block — compliance verification**

**Field 1 — Tier-ID threading (C-13):** Every T-NN from TABLE A appears verbatim in all
downstream sections (TABLE B `From`, TABLE C rows, TABLE D `Tier-IDs involved`, TABLE E
`Tier-ID`, Step 2E cascade trace, TABLE F `Source T-NN`). State PASS or list each
discrepancy as: T-NN | section | issue.

**Field 2 — REGISTRY GAP enforcement (C-17/C-19):** No new T-NN was assigned during Steps
2A–2H. State PASS or list violations as: step | T-NN introduced | impact.

**Field 3 — Load-shape classification at registration (C-16):** Every TABLE A row has a
non-placeholder `Load-shape verdict` assigned at Step 1B, not in Step 2G. State PASS or
list deferred rows.

**Field 4 — Annotation dropout (C-40):** Every Annot-01 through Annot-07 is present at its
anchor site. State PASS or list: Annot-ID | anchor site | status.

**Field 5 — INVENTORY GATE compliance (C-41):** The INVENTORY GATE was reached before Phase 1
opened. GATE STATUS was explicitly set to CLEARED before Step 1A began. State PASS or FAIL
with explanation.

**Per-section compliance status (C-18):**

| Section | C-17/C-19 reminder present | C-16 (load-shape at reg.) | C-13 (T-NN threading) | Verdict |
|---------|---------------------------|--------------------------|----------------------|---------|
| Step 1A | N/A | gate-controlled | N/A | |
| Step 1B | N/A | assigned here | N/A | |
| Step 2A | Y/N | N/A | Y/N | |
| Step 2B | N/A | N/A | Y/N | |
| Step 2C | Y/N | N/A | Y/N | |
| Step 2D | N/A | N/A | Y/N | |
| Step 2E | Y/N | N/A | Y/N | |
| Step 2G | Y/N | N/A | Y/N | |
| Step 2H | Y/N | N/A | Y/N | |

FAIL entries (if any): Criterion-ID | Section | Failure description | Evidence

---

## V-02

**Axis:** Output format (single-axis)

**Hypothesis:** Expressing the C-41 gate as a structured verification table — with rows for
Check, Expected, Actual, and Verdict — makes the count comparison mechanically visible and
produces an observable output cell (Verdict row) that must be filled before Phase 1 opens.
A table-format gate cannot be "passed over" without the Verdict cell remaining blank, which
is itself a detectable compliance failure. The annotation inventory includes a `Gate-weight`
column that pre-identifies which rows contribute to the count, making the count derivation
auditable in the table itself.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
the rate-limited system described in the signal. Treat the stated request volume as 1x
nominal; also analyze at 2x and 5x.

The tables below are the primary output — every cell SHALL be filled. Produce sections in
the order shown. This prompt has three structural stages: FORMAT CONTRACT (Role 1), PHASE 1
ACTIVATION TABLE (count gate, C-41), and ANALYSIS (Role 2).

---

**ROLE 1 — FORMAT CONTRACT**

**Section A — Precision-site inventory**

Count: 7 precision sites. This inventory SHALL be cross-referenced at the PHASE 1 ACTIVATION
TABLE before analysis begins.

| Site-ID | Table | Column | Violation type | C-27 hierarchy |
|---------|-------|--------|----------------|----------------|
| S-01 | TABLE A | `Limit (number + unit)` | vague-label substitution | primary |
| S-02 | TABLE A | `Binding?` | assertion-without-causal-reason | adjacent-1 (S-01/S-02/S-03) |
| S-03 | TABLE A | `Failure mode` | insufficient-categorical-diversity | adjacent-2 (S-01/S-02/S-03) |
| S-04 | TABLE B | `Mechanism` | generic-term substitution | primary |
| S-05 | TABLE C | `Error code or signal` | plain-description substitution | primary |
| S-06 | TABLE E | `Type` | category-absence-undetectable | primary |
| S-07 | TABLE F | `Setting or API parameter` | category-of-action substitution | primary |

Multi-adjacent group S-01/S-02/S-03: 3 distinct violation types at TABLE A. Non-conflation
count: 3. An executor SHALL NOT treat these as a single "incomplete entry" failure mode.

**Section B — Format contract** (same column definitions and violation-type annotations as
V-01 Section B — all seven sites, each with `*Violation type:*` and compliance failure
condition. Omitted here for space; the format of each definition mirrors V-01 exactly.)

**Section C — Annotation inventory**

This section declares **7 required annotations**. The `Gate-weight` column identifies rows
that contribute to the Phase 1 activation count. A row count below 7 in Gate-weight=Y rows
is a completeness gap.

| Annot-ID | Anchor site | Failure-mode label | Prohibited form | Gate-weight |
|----------|------------|-------------------|--------------------|-------------|
| Annot-01 | TABLE A — `Limit (number + unit)` | vague-label substitution | "limited" for "1,200 req/min" | Y |
| Annot-02 | TABLE A — `Binding?` | assertion-without-causal-reason | Y with no mechanism | Y |
| Annot-03 | TABLE A — `Failure mode` | insufficient-categorical-diversity | all rows: "timeout" | Y |
| Annot-04 | TABLE B — `Mechanism` | generic-term substitution | "blocked" for "queue-fill" | Y |
| Annot-05 | TABLE C — `Error code or signal` | plain-description substitution | "fails" for "HTTP 429" | Y |
| Annot-06 | TABLE E — `Type` | category-absence-undetectable | row with no Type | Y |
| Annot-07 | TABLE F — `Setting or API parameter` | category-of-action substitution | "add retry" for `connector.retryPolicy` | Y |

This inventory is closed. An annotation not listed here does not exist as a contract
requirement. An annotation listed here absent from its anchor site is a FORMAT CONTRACT
violation.

PROHIBITED: annotation dropout at any anchor site in this inventory — *prevents
handoff-boundary gap: absence detectable only by full body scan; this clause converts dropout
to a contract violation identifiable by Annot-ID lookup. Co-located inside annotation
inventory per C-40 requirement.*

**FORMAT CONTRACT COMPLETE**

---

**PHASE 1 ACTIVATION TABLE**

Fill this table before opening any analysis section. Phase 1 SHALL NOT open until the Verdict
row reads PROCEED.

| Check | Expected | Actual | Verdict |
|-------|----------|--------|---------|
| Section C Gate-weight=Y row count | 7 | [count them] | PROCEED if actual=7; RETURN TO ROLE 1 if actual<7 |
| FORMAT CONTRACT COMPLETE stated | present | [Y/N] | PROCEED if Y |
| All Section C anchor sites populated | all 7 | [Y/N] | PROCEED if Y |

**Activation outcome:**
- All rows → PROCEED: open Phase 1.
- Any row → RETURN TO ROLE 1: Role 1 is incomplete. Complete the indicated gap, re-state
  FORMAT CONTRACT COMPLETE, re-fill this table from the top.

**ACTIVATION STATUS: [ PROCEED / RETURN TO ROLE 1 ]** — This field SHALL be filled before
Step 1A begins.

---

**ROLE 2 — DOMAIN EXPERT**

*(All Step 1A through Step 2H and Audit block sections are identical in structure to V-01.
PHASE ENTRY CONDITION for Step 1A references ACTIVATION STATUS = PROCEED instead of
INVENTORY GATE = CLEARED. Registry Gap Prohibition, escape-route frame, distributed
reminders at Steps 2A/2C/2E/2G/2H, and Audit block Field 5 reference the PHASE 1 ACTIVATION
TABLE rather than the INVENTORY GATE.)*

**REGISTRY GAP PROHIBITION — Failure 5 prevention (C-17):** [same as V-01]

**Step 1A — VOLUME ANALYST: TIER IDENTIFICATION AND LIMITS**

**PHASE ENTRY CONDITION:** Step 1A SHALL be entered only after PHASE 1 ACTIVATION TABLE
ACTIVATION STATUS = PROCEED.

[TABLE A, Steps 1B, 2A–2H, and Audit block as V-01 — identical structure, with ACTIVATION
STATUS replacing GATE STATUS in Field 5 of the Audit block.]

---

## V-03

**Axis:** Role sequence (single-axis)

**Hypothesis:** Elevating the annotation inventory count check to a named standalone role —
Role 1.5 (INVENTORY VERIFIER) — with its own activation condition, single responsibility,
and explicit handoff signal creates the clearest possible role-sequence gate for C-41. A
named role cannot be skipped without a visible structural gap in the role sequence. The
handoff from Role 1.5 to Role 2 uses an explicit HANDOFF SIGNAL that Role 2's entry condition
checks by name, creating a two-signal chain: FORMAT CONTRACT COMPLETE (Role 1 → Role 1.5)
and INVENTORY VERIFIED (Role 1.5 → Role 2).

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
the rate-limited system described in the signal. Treat the stated request volume as 1x
nominal; also analyze at 2x and 5x.

This prompt uses a four-role sequence: **Role 1 (FORMAT CONTRACT)** → **Role 1.5 (INVENTORY
VERIFIER)** → **Role 2 (DOMAIN EXPERT)** → **Role 3 (AUDIT)**. Each role activates only on
its predecessor's handoff signal. The tables below are the primary output — every cell SHALL
be filled. Produce sections in the order shown.

---

**ROLE 1 — FORMAT CONTRACT**

**Activation condition:** None — Role 1 runs first.
**Handoff signal:** FORMAT CONTRACT COMPLETE

**Section A — Precision-site inventory**

[Same 7-site table as V-01 Section A, including multi-adjacent note and non-conflation
count of 3 at TABLE A.]

**Section B — Format contract**

[Same 7 column definitions with violation types and compliance failure conditions as V-01
Section B.]

**Section C — Annotation inventory**

This section declares **7 required annotations**. Count-scan verification: expected rows = 7.
Role 1.5 verifies this count before Role 2 opens.

[Same 7-row annotation inventory table as V-01 Section C, with two-sentence closure and
PROHIBITED dropout clause co-located inside the inventory.]

**FORMAT CONTRACT COMPLETE** ← Role 1.5 activation signal

---

**ROLE 1.5 — INVENTORY VERIFIER**

**Activation condition:** FORMAT CONTRACT COMPLETE has been stated.
**Single responsibility:** Confirm that Section C annotation inventory row count equals the
declared count of 7. This role has no other responsibility and produces no analysis output.
**Handoff signal (conditional):**
- Count = 7 → state **INVENTORY VERIFIED** and yield to Role 2.
- Count < 7 → state **INVENTORY INCOMPLETE** and return to Role 1. Do not yield to Role 2
  until Role 1 corrects Section C and re-states FORMAT CONTRACT COMPLETE.

**Verification procedure:**

1. Count the Annot-ID rows in Section C.
2. Declared count: 7.
3. Actual count: [fill].
4. Outcome:
   - Actual = 7 → **INVENTORY VERIFIED** — Role 2 may activate.
   - Actual < 7 → **INVENTORY INCOMPLETE** — Section C has [7 - actual] missing rows.
     Return to Role 1. Complete Section C. Re-state FORMAT CONTRACT COMPLETE. Re-enter
     Role 1.5 from step 1.

**INVENTORY VERIFIED / INVENTORY INCOMPLETE:** [fill]

---

**ROLE 2 — DOMAIN EXPERT**

**Activation condition:** INVENTORY VERIFIED has been stated by Role 1.5.

An executor SHALL NOT open Step 1A until the Role 1.5 handoff signal is INVENTORY VERIFIED.
If INVENTORY INCOMPLETE was stated, Role 2 does not activate.

**REGISTRY GAP PROHIBITION — Failure 5 prevention (C-17):** [same as V-01]

**Step 1A — VOLUME ANALYST: TIER IDENTIFICATION AND LIMITS**

**PHASE ENTRY CONDITION:** Step 1A SHALL be entered only after Role 1.5 HANDOFF SIGNAL =
INVENTORY VERIFIED and the signal input has been read in full.

[TABLE A with all columns including Binding? with causal mechanism and Failure mode with
diversity requirement, as V-01. Load-shape verdict placeholder. STEP 1A GATE as V-01.]

**Step 1B — LOAD-SHAPE ANALYST: CLASSIFICATION**

[Identical to V-01 Step 1B — deferral prohibition, escape-route frame, STEP 1B GATE.]

**Step 2A through Step 2H** — [Identical structure to V-01 Steps 2A–2H, including distributed
REGISTRY GAP reminders at 2A, 2C, 2E, 2G, 2H, phase entry/exit conditions, and all tables.]

---

**ROLE 3 — AUDIT**

**Activation condition:** Step 2H is closed.

[Same audit block as V-01, with Field 5 checking that Role 1.5 HANDOFF SIGNAL = INVENTORY
VERIFIED appears before Step 1A, and per-section compliance table as V-01.]

---

## V-04

**Axes:** Phrasing register (primary) + Lifecycle emphasis (secondary)

**Hypothesis:** Maximizing SHALL/MUST/PROHIBITED density at the Phase 1 entry gate —
naming every decision point as a normative obligation — creates the strongest C-40 + C-41
joint coverage. The lifecycle emphasis axis compounds this: the PHASE 1 ENTRY CONDITION block
is a full named section (not a preamble note) with subsections for count declaration,
confirmation, and outcome. An executor encountering SHALL NOT at every branch point cannot
treat the count check as advisory.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
the rate-limited system described in the signal. Treat the stated request volume as 1x
nominal; also analyze at 2x and 5x.

The tables below are the primary output — every cell SHALL be filled. An executor SHALL
produce sections in the order shown. An executor SHALL NOT begin any analysis section before
all entry conditions for that section are met.

---

**ROLE 1 — FORMAT CONTRACT**

An executor SHALL complete Role 1 before any analysis section is entered.

**Section A — Precision-site inventory**

An executor SHALL verify, at the PHASE 1 ENTRY CONDITION, that every site listed here has
its annotation present at its anchor location. Count: 7 precision sites.

[Same 7-site table as V-01, with multi-adjacent note and non-conflation count.]

**Section B — Format contract**

An executor SHALL populate the following column definitions. Each definition SHALL include a
`*Violation type:*` annotation and a compliance failure condition. An executor SHALL NOT
omit either element at any precision site.

[Same 7 column definitions as V-01, with violation types and compliance failure conditions,
each using SHALL/PROHIBITED normative language in the failure condition text.]

**Section C — Annotation inventory**

This section SHALL declare the required annotation count before enumeration begins. **This
section declares 7 required annotations.** An executor verifying completeness SHALL count
rows; expected = 7. A count below 7 SHALL be treated as a completeness gap requiring Role 1
correction before Phase 1 opens.

| Annot-ID | Anchor site | Failure-mode label | Prohibited form (example) |
|----------|------------|-------------------|-----------------------------|
| Annot-01 | TABLE A — `Limit (number + unit)` | vague-label substitution | "limited" for "1,200 req/min" |
| Annot-02 | TABLE A — `Binding?` | assertion-without-causal-reason | Y with no mechanism |
| Annot-03 | TABLE A — `Failure mode` | insufficient-categorical-diversity | all rows: "timeout" |
| Annot-04 | TABLE B — `Mechanism` | generic-term substitution | "blocked" for "queue-fill" |
| Annot-05 | TABLE C — `Error code or signal` | plain-description substitution | "fails" for "HTTP 429" |
| Annot-06 | TABLE E — `Type` | category-absence-undetectable | row with no Type value |
| Annot-07 | TABLE F — `Setting or API parameter` | category-of-action substitution | "add retry" for `connector.retryPolicy` |

This inventory is closed. An annotation not listed here does not exist as a contract
requirement. An annotation listed here that is absent from its anchor site SHALL be treated
as a FORMAT CONTRACT violation requiring correction before handoff.

PROHIBITED: annotation dropout at any anchor site listed in this inventory — *prevents
handoff-boundary gap: an annotation absent from its anchor site is detectable only by full
body scan; this PROHIBITED clause, co-located inside the annotation inventory, converts
dropout into a contract violation identifiable by Annot-ID lookup.* An executor SHALL verify
each Annot-ID anchor site at handoff.

**FORMAT CONTRACT COMPLETE**

---

**PHASE 1 ENTRY CONDITION — MANDATORY GATE (C-41)**

An executor SHALL complete this section before opening Step 1A. An executor SHALL NOT open
Step 1A until this gate is cleared. This gate has three subsections; all three SHALL be
completed in order.

**Subsection 1 — Count declaration:**
Section C declares 7 required annotations. Expected row count at Section C = 7.

**Subsection 2 — Confirmation:**
An executor SHALL count the Annot-ID rows in Section C.
Actual Section C row count: [fill — required before proceeding].

**Subsection 3 — Outcome (SHALL NOT proceed until this subsection is resolved):**
- Actual count = 7: PHASE 1 ENTRY CONDITION CLEARED. An executor SHALL proceed to Step 1A.
- Actual count < 7: PHASE 1 ENTRY CONDITION BLOCKED. FORMAT CONTRACT COMPLETE was stated
  with an incomplete annotation inventory. An executor SHALL return to Role 1. An executor
  SHALL complete Section C to the declared count of 7. An executor SHALL re-state FORMAT
  CONTRACT COMPLETE. An executor SHALL re-enter this PHASE 1 ENTRY CONDITION from
  Subsection 1. An executor SHALL NOT proceed to Step 1A until Subsection 3 resolves to
  CLEARED.

**PHASE 1 ENTRY CONDITION STATUS: [ CLEARED / BLOCKED ]** — An executor SHALL fill this
field. An executor SHALL NOT open Step 1A if this field is BLOCKED or unfilled.

---

**ROLE 2 — DOMAIN EXPERT**

**REGISTRY GAP PROHIBITION — Failure 5 prevention (C-17):** Tiers discovered during Step 2
are scope violations. PROHIBITED: assigning a new T-NN during Step 2. An executor SHALL
return to TABLE A, register the tier with all columns filled, and SHALL restart from the
point of discovery. This prohibition SHALL be restated at each Step 2 section where
mid-phase discovery could occur.

**Step 1A — VOLUME ANALYST: TIER IDENTIFICATION AND LIMITS**

**PHASE ENTRY CONDITION:** Step 1A SHALL be entered only after PHASE 1 ENTRY CONDITION
STATUS = CLEARED (confirmed in the mandatory gate above).

[TABLE A, Step 1B with deferral prohibition + escape-route frame, Steps 2A–2H with distributed
REGISTRY GAP reminders, identical structure to V-01.]

**ROLE 3 — AUDIT**

[Audit block as V-01. Field 5 checks that PHASE 1 ENTRY CONDITION STATUS = CLEARED appears
before Step 1A. Per-section compliance table as V-01.]

---

## V-05

**Axes:** Role sequence (primary) + Output format (secondary) + Inertia framing (secondary)

**Hypothesis:** Three combined axes create the strongest C-41 gate:
(1) Role sequence — an explicit role-handoff table forces the reader to trace the activation
chain and makes a missing handoff signal structurally visible.
(2) Output format — all gates are structured tables that require a filled Verdict cell;
a blank cell is a visible compliance gap.
(3) Inertia framing — explicitly naming the "looks complete / just start" failure mode and
rejecting it with a structural proof (parallel to the C-26 circular-dependency proof at
Step 1B) converts the C-41 gate from a policy requirement into a logical necessity.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
the rate-limited system described in the signal. Treat the stated request volume as 1x
nominal; also analyze at 2x and 5x.

The tables below are the primary output — every cell SHALL be filled. Produce sections in
the order shown. This prompt uses a four-role sequence with explicit handoff signals.

**Role activation chain:**

| Role | Activation signal | Handoff signal | Responsibility |
|------|------------------|----------------|----------------|
| Role 1 — FORMAT CONTRACT | None (runs first) | FORMAT CONTRACT COMPLETE | Precision-site inventory, format contract, annotation inventory |
| Role 1.5 — INVENTORY VERIFIER | FORMAT CONTRACT COMPLETE | INVENTORY VERIFIED or INVENTORY INCOMPLETE | Count check: Section C row count = 7 |
| Role 2 — DOMAIN EXPERT | INVENTORY VERIFIED | Step 2H closed | All analysis (Steps 1A–2H) |
| Role 3 — AUDIT | Step 2H closed | Audit complete | Compliance verification |

An executor SHALL NOT activate a role until its activation signal is present. An executor
seeing INVENTORY INCOMPLETE in the Role 1.5 column SHALL return to Role 1 — Role 2 does
not activate on INVENTORY INCOMPLETE.

---

**ROLE 1 — FORMAT CONTRACT**

**Section A — Precision-site inventory**

[Same 7-site table as V-01, with multi-adjacent note and non-conflation count.]

**Section B — Format contract**

[Same 7 column definitions as V-01 with all violation types, compliance failure conditions,
and non-conflation note at the S-01/S-02/S-03 group.]

**Section C — Annotation inventory**

This section declares **7 required annotations**. Role 1.5 verifies this count before Role 2
activates.

| Annot-ID | Anchor site | Failure-mode label | Prohibited form (example) |
|----------|------------|-------------------|-----------------------------|
| Annot-01 | TABLE A — `Limit (number + unit)` | vague-label substitution | "limited" for "1,200 req/min" |
| Annot-02 | TABLE A — `Binding?` | assertion-without-causal-reason | Y with no mechanism |
| Annot-03 | TABLE A — `Failure mode` | insufficient-categorical-diversity | all rows: "timeout" |
| Annot-04 | TABLE B — `Mechanism` | generic-term substitution | "blocked" for "queue-fill" |
| Annot-05 | TABLE C — `Error code or signal` | plain-description substitution | "fails" for "HTTP 429" |
| Annot-06 | TABLE E — `Type` | category-absence-undetectable | row with no Type value |
| Annot-07 | TABLE F — `Setting or API parameter` | category-of-action substitution | "add retry" for `connector.retryPolicy` |

This inventory is closed. An annotation not listed here does not exist as a contract
requirement. An annotation listed here absent from its anchor site is a FORMAT CONTRACT
violation.

PROHIBITED: annotation dropout at any anchor site listed in this inventory — *prevents
handoff-boundary gap: co-located here inside the annotation inventory per C-40 requirement.*

**FORMAT CONTRACT COMPLETE** ← Role 1.5 activation signal

---

**ROLE 1.5 — INVENTORY VERIFIER**

**Activation signal received:** FORMAT CONTRACT COMPLETE

**Inertia frame — the "looks complete" bypass failure mode:**

The temptation to skip Role 1.5 and proceed directly to Role 2 is the "looks complete"
framing — because FORMAT CONTRACT COMPLETE has been stated and the analysis tables are
scaffolded, activating Role 2 appears to miss no required steps. This frame is self-defeating:
FORMAT CONTRACT COMPLETE confirms that Role 1's *sections* are present — it does not verify
that the annotation inventory is *complete to its declared count*. Role 1.5 exists as a
structural gap between FORMAT CONTRACT COMPLETE and Role 2 activation precisely because a
partial Section C (e.g., 6 of 7 annotations) satisfies Role 1's section presence check
while failing the count declared in Section C's header. Skipping Role 1.5 converts the
Section C count from a verifiable gate into an unverified assertion — a discrepancy is
detectable only after Role 2 has produced output, not before. Role 1.5 closes this gap by
making count verification the activation condition for Role 2.

**Verification table:**

| Check | Expected | Actual | Verdict |
|-------|----------|--------|---------|
| Section C Annot-ID row count | 7 | [count] | PASS if actual=7; FAIL if actual<7 |
| FORMAT CONTRACT COMPLETE stated | present | [Y/N] | PASS if Y |

**Outcome:**
- All checks PASS → state **INVENTORY VERIFIED** → Role 2 activates.
- Any check FAIL → state **INVENTORY INCOMPLETE** → return to Role 1. Correct the gap.
  Re-state FORMAT CONTRACT COMPLETE. Re-enter Role 1.5 from the top.

**HANDOFF SIGNAL: [ INVENTORY VERIFIED / INVENTORY INCOMPLETE ]** — fill before Role 2.

---

**ROLE 2 — DOMAIN EXPERT**

**Activation signal required:** INVENTORY VERIFIED (from Role 1.5)

An executor SHALL confirm the Role 1.5 HANDOFF SIGNAL = INVENTORY VERIFIED before
opening Step 1A. An executor SHALL NOT open Step 1A if HANDOFF SIGNAL = INVENTORY
INCOMPLETE or if the HANDOFF SIGNAL field is unfilled.

**REGISTRY GAP PROHIBITION — Failure 5 prevention (C-17):** Tiers discovered during Step 2
are scope violations. PROHIBITED: assigning a new T-NN during Step 2. An executor SHALL
return to TABLE A, register the tier with all required columns, and SHALL restart from the
point of discovery. This prohibition SHALL be restated at each Step 2 section where
mid-phase discovery could occur.

---

**Step 1A — VOLUME ANALYST: TIER IDENTIFICATION AND LIMITS**

**PHASE ENTRY CONDITION:** Step 1A SHALL be entered only after Role 1.5 HANDOFF SIGNAL =
INVENTORY VERIFIED.

*(Volume analyst role: identify every rate-limiting component; record numeric limit, scope,
binding status with causal reason, failure mode, visibility window, and recovery time. Leave
`Load-shape verdict` as placeholder — assign at Step 1B.)*

**TABLE A — THROTTLE TIER INVENTORY**

| Tier-ID | Component | Limit (number + unit) | Scope | STATUS 1x | STATUS 2x | STATUS 5x | Binding? (Y/N + mechanism) | Failure mode | Load-shape verdict | Failure visibility window | Recovery time |
|---------|-----------|----------------------|-------|-----------|-----------|-----------|---------------------------|--------------|-------------------|--------------------------|---------------|
| T-01    |           |                      |       |           |           |           |                           |              | [Step 1B]         |                          |               |
| T-02    |           |                      |       |           |           |           |                           |              | [Step 1B]         |                          |               |
| ...     |           |                      |       |           |           |           |                           |              | [Step 1B]         |                          |               |

**STEP 1A GATE TABLE:**

| Gate check | Required | Status |
|------------|----------|--------|
| All T-NN rows populated (except Load-shape verdict) | Y | |
| No vague labels in `Limit` column | Y | |
| All `Binding?` entries include causal mechanism | Y | |
| At least 2 distinct `Failure mode` values | Y | |

Step 1B SHALL NOT open until all gate checks = Y.

---

**Step 1B — LOAD-SHAPE ANALYST: CLASSIFICATION**

**PHASE ENTRY CONDITION:** Step 1B SHALL be entered only after STEP 1A GATE TABLE is all-Y.

**Failure 2 + Failure 6 prevention — CLASSIFICATION REQUIRED AT STEP 1B:** An executor SHALL
assign `Load-shape verdict` for every TABLE A tier at this step. PROHIBITED: leaving any
`Load-shape verdict` as placeholder or deferring to Step 2G.

**Escape-route frame:** The temptation to defer is the "STATUS tracks volume thresholds"
framing — because TABLE A STATUS columns handle volume thresholds, load-shape classification
appears to belong naturally in the LOAD SHAPE COMPARISON section (Step 2G). This frame is
self-defeating: load-shape classification requires the registered `Limit` value available
now at Step 1B, and Step 2G depends on per-tier Load-shape verdicts to produce meaningful
comparisons — deferring creates a circular dependency. Step 1B closes this dependency.

For each TABLE A tier, update `Load-shape verdict`: SHAPE-NEUTRAL or SHAPE-SENSITIVE, with
numeric rate differential and mechanism.

**STEP 1B GATE TABLE:**

| Gate check | Required | Status |
|------------|----------|--------|
| Every TABLE A row has Load-shape verdict populated | Y | |
| Each verdict states SHAPE-NEUTRAL or SHAPE-SENSITIVE | Y | |
| Each verdict includes numeric differential | Y | |
| Each verdict names the mechanism | Y | |

Step 2 SHALL NOT open until all gate checks = Y.

---

**Step 2A — BACKPRESSURE PROPAGATION TRACE (TABLE B)**

**PHASE ENTRY CONDITION:** Step 2A SHALL be entered after STEP 1B GATE TABLE is all-Y.

**Step 2A — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19):** Tiers
in backpressure analysis not in TABLE A are scope violations. An executor SHALL NOT assign
a new T-NN here. Return to TABLE A.

| Hop | From (Tier-ID) | To component | Mechanism | Observable effect |
|-----|----------------|--------------|-----------|-------------------|
| 1   |                |              |           |                   |
| 2   |                |              |           |                   |
| ... |                |              |           |                   |

Minimum 2 hops. `Mechanism` from permitted set: queue-fill, connection-hold,
retry-amplification, dependency-stall, timeout-cascade.

---

**Step 2B — USER EXPERIENCE CATALOG (TABLE C)**

**PHASE ENTRY CONDITION:** After Step 2A. One row per TABLE A Tier-ID.

| Tier-ID | Error code or signal | Retry-After present? | Retry-After surfaced? | Visible in run history? | Failure if Retry-After ignored |
|---------|---------------------|---------------------|----------------------|------------------------|-------------------------------|
| T-01    |                     |                     |                      |                        |                               |
| T-02    |                     |                     |                      |                        |                               |

---

**Step 2C — UNPROTECTED BURST PATHS (TABLE D)**

**PHASE ENTRY CONDITION:** After Step 2B.

**Step 2C — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19):** Return
to TABLE A for any new tier. Do not assign a new T-NN here.

| Path-ID | Entry component | Gap reason | Tier-IDs involved | Consequence at burst |
|---------|----------------|------------|-------------------|-----------------------|
| P-01    |                |            |                   |                       |

---

**Step 2D — TIER RISK RANKING (TABLE E)**

**PHASE ENTRY CONDITION:** After Step 2C. All TABLE A tiers appear; ordered by business risk.

| Rank | Tier-ID | Type | Risk rationale |
|------|---------|------|----------------|
| 1    |         |      |                |
| 2    |         |      |                |

For Rank 1: reference `Failure visibility window` and `Recovery time` from TABLE A.

---

**Step 2E — CASCADE SCENARIO**

**PHASE ENTRY CONDITION:** After Step 2D.

**Step 2E — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19):** Return
to TABLE A for any new tier. Do not assign a new T-NN here.

Trace one concrete cascade from the 1x binding constraint. Use T-NN identifiers throughout.
Explicit causal links. Minimum three tiers.

---

**Step 2F — RETRY-AFTER GAP ASSESSMENT**

**PHASE ENTRY CONDITION:** After Step 2E.

For the 1x binding constraint tier: Retry-After present and surfaced? If absent, name the
failure mode: retry storm vs. quota exhaustion.

---

**Step 2G — LOAD SHAPE COMPARISON**

**PHASE ENTRY CONDITION:** After Step 2F.

**Step 2G — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19):** Return
to TABLE A for any new tier. Do not assign a new T-NN here.

Using TABLE A `Limit` values and `Load-shape verdict` (from Step 1B), compare 1x nominal at:
- **UNIFORM arrival** — per-second rate; which tiers HIT or SAT.
- **BURST arrival** — burst fraction, peak rate; which tiers HIT or SAT and why.

At least one numeric comparison with status differing at identical total count.

---

**Step 2H — MITIGATION REGISTRY (TABLE F)**

**PHASE ENTRY CONDITION:** After Step 2G.

**Step 2H — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19):** Return
to TABLE A for any new tier. Do not assign a new T-NN here.

| MR-ID | Source T-NN | Gap type | Component | Setting or API parameter | Change | Expected outcome |
|-------|-------------|----------|-----------|--------------------------|--------|-----------------|
| MR-01 |             |          |           |                          |        |                 |
| MR-02 |             |          |           |                          |        |                 |

---

**ROLE 3 — AUDIT**

**Activation signal:** Step 2H closed

**Audit compliance table:**

| Field | Criterion | Check | Status |
|-------|-----------|-------|--------|
| F-1 | C-13 tier-ID threading | Every T-NN appears verbatim in all downstream sections | PASS / [list gaps] |
| F-2 | C-17/C-19 registry gap | No T-NN assigned outside TABLE A | PASS / [list violations] |
| F-3 | C-16 load-shape at registration | All Load-shape verdicts in Step 1B, not Step 2G | PASS / [list deferrals] |
| F-4 | C-40 annotation dropout | Annot-01 through Annot-07 each present at anchor site | PASS / [list: Annot-ID \| site \| status] |
| F-5 | C-41 inventory gate | Role 1.5 HANDOFF SIGNAL = INVENTORY VERIFIED present before Step 1A | PASS / FAIL + explanation |

**Per-section compliance status (C-18):**

| Section | C-17/C-19 reminder | C-16 | C-13 | Verdict |
|---------|--------------------|------|------|---------|
| Step 1A | N/A | gate-controlled | N/A | |
| Step 1B | N/A | assigned here | N/A | |
| Step 2A | Y/N | N/A | Y/N | |
| Step 2B | N/A | N/A | Y/N | |
| Step 2C | Y/N | N/A | Y/N | |
| Step 2D | N/A | N/A | Y/N | |
| Step 2E | Y/N | N/A | Y/N | |
| Step 2G | Y/N | N/A | Y/N | |
| Step 2H | Y/N | N/A | Y/N | |

FAIL entries (if any): Criterion-ID | Section | Failure description | Evidence
