# flow-throttle Variate — Round 7 (v7 Rubric)

**Date:** 2026-03-16
**Rubric:** v7 (C-01 through C-22, 5 essential / 3 recommended / 14 aspirational, max composite 160)
**Baseline:** QU5 golden (all 5 essential, all 3 recommended, C-09–C-19 aspirational = denominator 19)
**Rubric version change:** v6 → v7 adds C-20 (prose-restriction declaration), C-21 (cross-artifact
referential integrity), C-22 (typed-row risk taxonomy) from the V-02 "table-dominant" axis observation.

---

## Round 7 (v7) Purpose

The v7 rubric derives three new criteria from the V-02 axis observation: "Table-dominant format —
every analytical artifact is a numbered table; prose restricted to binding-tier causal reason, burst
narrative, and self-verification verdict notes."

V-02's output surfaced three structural signals not required by any v6 criterion:

- **C-20** — Explicitly declaring which prose contexts are permitted (not merely restricting prose)
  makes format deviations auditable. A restriction without a declaration is implicit; a declaration
  with a closed list is verifiable by inspection.

- **C-21** — Every derived table (UX catalog, mitigations, ranking) naming its upstream source
  artifact by identifier and stating its coverage obligation goes beyond C-17's single enumeration
  anchor at the consequence-phase entry. C-17 anchors the consequence phase entry; C-21 anchors
  every downstream artifact individually.

- **C-22** — A Type column with a per-type minimum-row guarantee makes category-level gaps
  detectable by type scan. C-09's count requirement (≥ 2 mitigations) can be satisfied by two rows
  of the same failure category; the typed-row taxonomy cannot.

**Variation axes:**
1. **C-20 axis** (V-01) — prose-restriction declaration only
2. **C-21 axis** (V-02) — cross-artifact referential integrity headers only
3. **C-22 axis** (V-03) — typed-row risk taxonomy only
4. **Combined C-20 + C-21** (V-04)
5. **Combined C-20 + C-21 + C-22** (V-05)

**Predicted v7 scores:**

| Variation | Axes | C-20 | C-21 | C-22 | Aspirational | Composite |
|-----------|------|------|------|------|--------------|-----------|
| V-01 | C-20 declaration only | PASS | FAIL | FAIL | 12/14 | ~152 |
| V-02 | C-21 referential integrity only | FAIL | PASS | FAIL | 12/14 | ~152 |
| V-03 | C-22 typed-row taxonomy only | FAIL | FAIL | PASS | 12/14 | ~152 |
| V-04 | C-20 + C-21 | PASS | PASS | FAIL | 13/14 | ~156 |
| V-05 | C-20 + C-21 + C-22 | PASS | PASS | PASS | 14/14 | 160 |

**Composite formula:**
```
Composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 14 * 70)
```

**Round 7 questions:**

Q1: Does a top-of-prompt prose-restriction declaration satisfy C-20 when some prose sections remain
(2D ranking, 2E cascade, 2F retry-after, 2G load shape) but are explicitly listed as permitted
contexts? Hypothesis: PASS — C-20 requires a closed list, not zero prose. An output that names
the permitted contexts and contains no prose outside them satisfies C-20. The risk: a judge may
require the declaration to appear as a self-contained labeled block, not embedded in the
meta-instruction paragraph.

Q2: Does adding a "Source: TABLE X. Coverage: one row per T-NN from TABLE X. No row may be
omitted." header line to each derived table satisfy C-21? Hypothesis: PASS — C-21's required
form is "a header line at each derived table stating its source artifact and coverage obligation."
The risk: tables that already partially state this in the phase entry condition (like TABLE C's
"One row per TABLE A Tier-ID. No tier SHALL be omitted.") may need the declaration on the table
itself, not just in the surrounding instruction text.

Q3: Does a five-column risk table (Risk-ID, Tier-ID, Risk description, Type, Severity) with a
stated minimum-coverage guarantee per type satisfy C-22? Hypothesis: PASS — C-22 requires (a)
a Type column with a named taxonomy, (b) a per-type minimum-row constraint stated in the prompt.
Both are present. The risk: if the model omits one type category from the output despite the
instruction, C-22 fails at scoring time regardless of the prompt form.

**Risk profiles:**
- V-01: Prose-restriction declaration may need to be a labeled block, not prose itself.
- V-02: The TABLE C phase entry condition already partially states coverage — whether that
  counts as C-21 or whether a header line ON the table is required is the scoring question.
- V-03: Model compliance risk — the model may list risks without populating the Type column
  uniformly, leaving one category absent.
- V-04: Interaction risk — prose-restriction declaration in a prompt that still has prose sections
  is self-referential. Declaration must list those sections explicitly.
- V-05: Maximum density; the C-22 risk table (TABLE E) inserts a new step between 2G and 2H,
  requiring TABLE F to reference TABLE E as its source — tests C-21 on a fresh artifact boundary.

---

## V-01 — Single Axis: C-20 Prose-Restriction Declaration

**Axis:** Add a formal, labeled prose-restriction declaration before the first table. The declaration
enumerates the complete and closed list of prose-permitted contexts. Prose outside these contexts
is a format violation detectable without full content review. All other elements stay at baseline.

**Hypothesis:** C-20 requires the declaration to appear before the first table and enumerate a
closed list. An output that contains this block and has no prose outside the declared contexts
satisfies C-20. The structural change is additive — one new labeled block inserted at the top.
C-21 and C-22 are not addressed; TABLE C's existing "One row per TABLE A Tier-ID" instruction
is not upgraded to a header line (C-21 test remains FAIL); no Type column exists in the mitigation
table (C-22 remains FAIL).

**v7 predicted scoring:**
- C-20: PASS — labeled declaration present before first table, closed list, contexts named
- C-21: FAIL — no upstream source identifier or coverage obligation header line on derived tables
- C-22: FAIL — no Type column in any table
- Composite: ~152/160

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
the rate-limited system described in the signal. Treat the stated request volume as 1x
nominal; also analyze at 2x and 5x.

The tables below are the primary output — each carries a distinct finding category that prose
cannot represent with the same auditability. Every cell SHALL be filled. Produce sections in
the order shown.

**PROSE-RESTRICTION DECLARATION (C-20) — This list is complete and closed:**
Prose is permitted only in the following four contexts. Prose appearing outside these contexts
is a format violation detectable by inspection without full content review.
1. `Load-shape verdict` mechanism explanation — one sentence per tier in TABLE A Step 1B.
2. Escape-route frame at Step 1B — naming the deferral temptation and the rejection mechanism.
3. UNIFORM/BURST narrative at Step 2G — one sentence per arrival pattern naming which tiers shift.
4. Self-verification verdict note at the closing audit — one sentence stating the pass/fail
   conclusion and, if FAIL, the criterion ID and gap.
All other analytical content SHALL be expressed in tables. If an executor finds itself writing
a sentence outside these four contexts, it SHALL stop and convert the content to a table row.

---

**STEP 1 — TIER REGISTRY**

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
  - *Violation type: vague label substituted for numeric value (e.g., "limited" in place of
    "1,200 req/min").*
  - Compliance failure condition: An entry using a vague label instead of a specific
    number-with-unit fails this column's precision requirement.
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

**Escape-route frame:** The temptation to defer is the "STATUS tracks volume thresholds"
framing — because TABLE A STATUS columns use OK/HIT/SAT to track volume thresholds,
load-shape classification appears out of scope for the registry and naturally belonging in
"LOAD SHAPE COMPARISON." This frame is self-defeating: load-shape classification requires
the registered `Limit` value available now at Step 1B, and Step 2G depends on per-tier
Load-shape verdicts to produce meaningful comparisons — deferring creates a circular
dependency where the downstream section that would receive shape classification is itself
dependent on the per-tier verdict the registry was supposed to supply. Step 1B exists
precisely to foreclose this dependency.

For each TABLE A tier, update `Load-shape verdict`:
- State SHAPE-NEUTRAL or SHAPE-SENSITIVE
- State the numeric rate differential between uniform and burst arrival at this tier's limit
- State the mechanism that explains the differential

  - *Violation type: deferred verdict token — the executor routes the SHAPE-NEUTRAL/
    SHAPE-SENSITIVE classification to Step 2G rather than recording it at Step 1B.*
  - Compliance failure condition: A Load-shape verdict entry left blank or deferred
    ("see Step 2G", "analyzed below") at the end of Step 1B fails the registration-time
    classification requirement and invalidates Step 2G's numeric comparison.

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
    "blocked" in place of "queue-fill").*
  - Compliance failure condition: A mechanism entry using a generic category label (blocked,
    throttled, slowed) rather than a specific named mechanism from the permitted set fails
    this column's precision requirement.

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
    identifier (e.g., "request fails" in place of "HTTP 429").*
  - Compliance failure condition: An `Error code or signal` entry using a plain description
    rather than a specific HTTP status code or platform signal identifier fails this column's
    precision requirement.

---

**Step 2C — UNPROTECTED BURST PATHS (TABLE D)**

**PHASE ENTRY CONDITION:** Step 2C SHALL be entered after Step 2B is closed.

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

For the 1x binding constraint tier: is Retry-After present and surfaced? If absent, the
failure mode SHALL be named precisely — retry storm (exponential backoff) vs. quota
exhaustion (circuit breaker).

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
    "add retry logic" instead of `connector.retryPolicy`).*
  - Compliance failure condition: A row naming a category of action rather than a specific
    parameter identifier fails this column's precision requirement.

---

**CLOSING AUDIT**

Confirm C-01 through C-08 compliance. For each criterion, state PASS or FAIL. If FAIL, name
the gap in one sentence. Self-verification verdict note (prose permitted here per the
Prose-Restriction Declaration): state whether all criteria pass or identify the failing
criterion and the gap.

---

## V-02 — Single Axis: C-21 Cross-Artifact Referential Integrity

**Axis:** Add an upstream source reference and coverage obligation as a header line on every
derived table. The header line names the source artifact by table identifier and states the
row-count or coverage constraint. Prose-restriction declaration (C-20) and typed-row taxonomy
(C-22) are not added.

**Hypothesis:** C-21's required form is "a header line at each derived table stating its source
artifact and coverage obligation." The golden baseline already states coverage requirements in
phase entry conditions (e.g., "One row per TABLE A Tier-ID. No tier SHALL be omitted.") but
these appear in instruction text around the table, not as a header line on the table itself.
The distinction matters for auditing: a header line is visible when viewing the table in
isolation; a surrounding instruction is not. C-21 closes the gap by requiring the constraint
to travel with the artifact it governs.

**v7 predicted scoring:**
- C-20: FAIL — no prose-restriction declaration block
- C-21: PASS — upstream source identifier + coverage obligation header on every derived table
- C-22: FAIL — no Type column in any risk/mitigation table
- Composite: ~152/160

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
the rate-limited system described in the signal. Treat the stated request volume as 1x
nominal; also analyze at 2x and 5x.

The tables below are the primary output — each carries a distinct finding category that prose
cannot represent with the same auditability. Every cell SHALL be filled. Produce sections in
the order shown.

---

**STEP 1 — TIER REGISTRY**

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

*[Primary artifact. All downstream tables derive from TABLE A. No downstream table may
reference a Tier-ID absent from TABLE A.]*

| Tier-ID | Component | Limit (number + unit) | Scope | STATUS 1x | STATUS 2x | STATUS 5x | Binding at band | Load-shape verdict | Failure visibility window | Recovery time |
|---------|-----------|----------------------|-------|-----------|-----------|-----------|-----------------|-------------------|--------------------------|---------------|
| T-01    |           |                      |       |           |           |           |                 | [Step 1B]         |                          |               |
| T-02    |           |                      |       |           |           |           |                 | [Step 1B]         |                          |               |
| ...     |           |                      |       |           |           |           |                 | [Step 1B]         |                          |               |

Column definitions:
- `Tier-ID` — Assign T-01, T-02, ... and SHALL be used verbatim in every downstream section.
- `Limit (number + unit)` — a specific number with a unit (e.g., "1,000 req/min").
  - *Violation type: vague label substituted for numeric value (e.g., "limited" in place of
    "1,200 req/min").*
  - Compliance failure condition: An entry using a vague label instead of a specific
    number-with-unit fails this column's precision requirement.
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

**Escape-route frame:** The temptation to defer is the "STATUS tracks volume thresholds"
framing — because TABLE A STATUS columns use OK/HIT/SAT to track volume thresholds,
load-shape classification appears out of scope for the registry and naturally belonging in
"LOAD SHAPE COMPARISON." This frame is self-defeating: load-shape classification requires
the registered `Limit` value available now at Step 1B, and Step 2G depends on per-tier
Load-shape verdicts to produce meaningful comparisons — deferring creates a circular
dependency where the downstream section that would receive shape classification is itself
dependent on the per-tier verdict the registry was supposed to supply. Step 1B exists
precisely to foreclose this dependency.

For each TABLE A tier, update `Load-shape verdict`:
- State SHAPE-NEUTRAL or SHAPE-SENSITIVE
- State the numeric rate differential between uniform and burst arrival at this tier's limit
- State the mechanism that explains the differential

  - *Violation type: deferred verdict token — the executor routes the SHAPE-NEUTRAL/
    SHAPE-SENSITIVE classification to Step 2G rather than recording it at Step 1B.*
  - Compliance failure condition: A Load-shape verdict entry left blank or deferred
    ("see Step 2G", "analyzed below") at the end of Step 1B fails the registration-time
    classification requirement and invalidates Step 2G's numeric comparison.

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

**Step 2A — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19):** Tiers
appearing in backpressure analysis that are not in TABLE A are scope violations. An executor
SHALL NOT assign a new T-NN here. An executor SHALL return to TABLE A (complete Step 1A +
Step 1B), register the tier with all required columns, then continue.

*[TABLE B — Source: TABLE A. From (Tier-ID) SHALL reference a T-NN from TABLE A. Minimum
2 hops. No hop may reference a Tier-ID absent from TABLE A.]*

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
    "blocked" in place of "queue-fill").*
  - Compliance failure condition: A mechanism entry using a generic category label (blocked,
    throttled, slowed) rather than a specific named mechanism from the permitted set fails
    this column's precision requirement.

**PHASE EXIT CONDITION:** Step 2A SHALL be considered closed when at least two hops are
documented with T-NN identifiers and specific mechanisms.

---

**Step 2B — USER EXPERIENCE CATALOG (TABLE C)**

**PHASE ENTRY CONDITION:** Step 2B SHALL be entered after Step 2A PHASE EXIT CONDITION
is cleared.

*[TABLE C — Source: TABLE A. One row per T-NN from TABLE A. No tier may be omitted. No tier
absent from TABLE A may be added. Row count in TABLE C MUST equal row count in TABLE A.]*

| Tier-ID | Error code or signal | Retry-After present? (Y/N) | Retry-After surfaced to caller? (Y/N) | Visible in run history? (Y/N/SILENT) | Failure if Retry-After ignored |
|---------|---------------------|---------------------------|--------------------------------------|--------------------------------------|-------------------------------|
| T-01    |                     |                           |                                      |                                      |                               |
| T-02    |                     |                           |                                      |                                      |                               |

Column definitions:
- `Error code or signal` — Record the specific HTTP status code or platform-defined signal
  identifier returned at this throttle tier (e.g., "HTTP 429", "HTTP 503", "TL-0001").
  - *Violation type: plain description substituted for structured error code or signal
    identifier (e.g., "request fails" in place of "HTTP 429").*
  - Compliance failure condition: An `Error code or signal` entry using a plain description
    rather than a specific HTTP status code or platform signal identifier fails this column's
    precision requirement.

---

**Step 2C — UNPROTECTED BURST PATHS (TABLE D)**

**PHASE ENTRY CONDITION:** Step 2C SHALL be entered after Step 2B is closed.

**Step 2C — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19):** Tiers
referenced in burst path analysis that are not in TABLE A are scope violations. An executor
SHALL NOT assign a new T-NN here. An executor SHALL return to TABLE A.

*[TABLE D — Source: TABLE A. Tier-IDs involved SHALL reference T-NNs from TABLE A. At least
one row required. If no unprotected path exists, row 1 SHALL state the conclusion with at
least two named controls as evidence.]*

| Path-ID | Entry component | Gap reason (structural gap or named controls) | Tier-IDs involved | Consequence at burst volume |
|---------|----------------|-----------------------------------------------|-------------------|-----------------------------|
| P-01    |                |                                               |                   |                             |

---

**Step 2D — TIER RISK RANKING**

**PHASE ENTRY CONDITION:** Step 2D SHALL be entered after Step 2C is closed.

*[RANKING — Source: TABLE A. All TABLE A tiers SHALL appear. No tier may be omitted. No tier
absent from TABLE A may be ranked.]*

All TABLE A tiers SHALL appear in the ranking, ordered by business risk, highest to lowest.
One sentence per tier with rationale SHALL be provided. For the top-ranked tier, `Failure
visibility window` and `Recovery time` from TABLE A SHALL be referenced.

---

**Step 2E — CASCADE SCENARIO**

**PHASE ENTRY CONDITION:** Step 2E SHALL be entered after Step 2D is closed.

**Step 2E — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19):** Tiers
introduced during cascade trace that are not in TABLE A are scope violations. An executor
SHALL NOT assign a new T-NN here. An executor SHALL return to TABLE A.

*[CASCADE — Source: TABLE A. All tier references SHALL use T-NN identifiers from TABLE A.
Minimum three tiers. Each step SHALL be caused by the previous.]*

Trace one concrete cascade from the 1x binding constraint. T-NN identifiers SHALL be used
throughout. Each causal link SHALL be stated explicitly. A minimum of three tiers SHALL be
present, each step caused by the previous.

---

**Step 2F — RETRY-AFTER GAP ASSESSMENT**

**PHASE ENTRY CONDITION:** Step 2F SHALL be entered after Step 2E is closed.

*[RETRY-AFTER — Source: TABLE A and TABLE C. Binding-tier Tier-ID from TABLE A. Retry-After
status from TABLE C. Assessment references both artifacts.]*

For the 1x binding constraint tier: is Retry-After present and surfaced? If absent, the
failure mode SHALL be named precisely — retry storm (exponential backoff) vs. quota
exhaustion (circuit breaker).

---

**Step 2G — LOAD SHAPE COMPARISON**

**PHASE ENTRY CONDITION:** Step 2G SHALL be entered after Step 2F is closed.

**Step 2G — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19):** Tiers
introduced during load shape analysis that are not in TABLE A are scope violations. An
executor SHALL NOT assign a new T-NN here. An executor SHALL return to TABLE A.

*[LOAD SHAPE — Source: TABLE A. Load-shape verdicts from TABLE A Step 1B column. Tier
references SHALL use T-NNs from TABLE A. At least one numeric comparison where status
differs at identical total count.]*

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

*[TABLE F — Source: TABLE A. Component column SHALL reference T-NN or component name from
TABLE A. Minimum 2 rows. A mitigation row that names a category of action ("add retry logic")
requires further research before it can be applied. A row that names the exact parameter can
be applied immediately.]*

| MR-ID | Source | Gap type | Component | Setting or API parameter | Change | Expected outcome |
|-------|--------|----------|-----------|--------------------------|--------|-----------------|
| MR-01 |        |          |           |                          |        |                 |
| MR-02 |        |          |           |                          |        |                 |

`Setting or API parameter` — the exact configuration key, connector property, or API attribute
name SHALL be recorded here.

  - *Violation type: category of action substituted for named parameter identifier (e.g.,
    "add retry logic" instead of `connector.retryPolicy`).*
  - Compliance failure condition: A row naming a category of action rather than a specific
    parameter identifier fails this column's precision requirement.

---

## V-03 — Single Axis: C-22 Typed-Row Risk Taxonomy

**Axis:** Insert TABLE E (typed risk inventory) between Step 2G and Step 2H. TABLE E has a
Type column (Burst / Cascade / RetryAfter) with a per-type minimum-row guarantee stated in
the prompt. TABLE F (mitigations) derives from TABLE E and must have one row per TABLE E risk.
Prose-restriction declaration (C-20) and cross-artifact headers (C-21) are not added.

**Hypothesis:** C-22 requires (a) a Type column with a named taxonomy, (b) a per-type
minimum-row constraint stated in the prompt. A count-only requirement (≥ 2 mitigations) can
be satisfied by two rows of the same failure category; the typed-row taxonomy cannot. The
key test: does the model respect the per-type minimum guarantee, or does it satisfy the count
with homogeneous types? C-22 also requires that the mechanism making category absence
detectable — the type scan — be explicit in the prompt.

**v7 predicted scoring:**
- C-20: FAIL — no prose-restriction declaration block
- C-21: PARTIAL — TABLE F derives from TABLE E (new anchor), but other derived tables lack
  explicit upstream source header lines
- C-22: PASS — Type column with named taxonomy and per-type minimum-row constraint present
- Composite: ~153/160

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
the rate-limited system described in the signal. Treat the stated request volume as 1x
nominal; also analyze at 2x and 5x.

The tables below are the primary output — each carries a distinct finding category that prose
cannot represent with the same auditability. Every cell SHALL be filled. Produce sections in
the order shown.

---

**STEP 1 — TIER REGISTRY**

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
  - *Violation type: vague label substituted for numeric value (e.g., "limited" in place of
    "1,200 req/min").*
  - Compliance failure condition: An entry using a vague label instead of a specific
    number-with-unit fails this column's precision requirement.
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

**Escape-route frame:** The temptation to defer is the "STATUS tracks volume thresholds"
framing — because TABLE A STATUS columns use OK/HIT/SAT to track volume thresholds,
load-shape classification appears out of scope for the registry and naturally belonging in
"LOAD SHAPE COMPARISON." This frame is self-defeating: load-shape classification requires
the registered `Limit` value available now at Step 1B, and Step 2G depends on per-tier
Load-shape verdicts to produce meaningful comparisons — deferring creates a circular
dependency where the downstream section that would receive shape classification is itself
dependent on the per-tier verdict the registry was supposed to supply. Step 1B exists
precisely to foreclose this dependency.

For each TABLE A tier, update `Load-shape verdict`:
- State SHAPE-NEUTRAL or SHAPE-SENSITIVE
- State the numeric rate differential between uniform and burst arrival at this tier's limit
- State the mechanism that explains the differential

  - *Violation type: deferred verdict token — the executor routes the SHAPE-NEUTRAL/
    SHAPE-SENSITIVE classification to Step 2G rather than recording it at Step 1B.*
  - Compliance failure condition: A Load-shape verdict entry left blank or deferred
    ("see Step 2G", "analyzed below") at the end of Step 1B fails the registration-time
    classification requirement and invalidates Step 2G's numeric comparison.

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
    "blocked" in place of "queue-fill").*
  - Compliance failure condition: A mechanism entry using a generic category label (blocked,
    throttled, slowed) rather than a specific named mechanism from the permitted set fails
    this column's precision requirement.

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
    identifier (e.g., "request fails" in place of "HTTP 429").*
  - Compliance failure condition: An `Error code or signal` entry using a plain description
    rather than a specific HTTP status code or platform signal identifier fails this column's
    precision requirement.

---

**Step 2C — UNPROTECTED BURST PATHS (TABLE D)**

**PHASE ENTRY CONDITION:** Step 2C SHALL be entered after Step 2B is closed.

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

For the 1x binding constraint tier: is Retry-After present and surfaced? If absent, the
failure mode SHALL be named precisely — retry storm (exponential backoff) vs. quota
exhaustion (circuit breaker).

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

**Step 2G2 — RISK INVENTORY (TABLE E)**

**PHASE ENTRY CONDITION:** Step 2G2 SHALL be entered after Step 2G is closed.

**TYPED-ROW COVERAGE GUARANTEE (C-22):** TABLE E uses a Type column with a closed taxonomy:
Burst / Cascade / RetryAfter. The table SHALL contain at least one row of Type = Burst, at
least one row of Type = Cascade, and at least one row of Type = RetryAfter. A table with two
rows of the same Type while another Type is absent fails the minimum-coverage guarantee.
Category-level absence is detectable by type scan: an executor SHALL scan the Type column
after completing the table and confirm all three types are present before proceeding to Step
2H.

**TYPE SCAN GATE:** Before opening Step 2H, an executor SHALL confirm: (a) at least one Burst
row present; (b) at least one Cascade row present; (c) at least one RetryAfter row present.
If any type is absent, an executor SHALL add the missing row before proceeding.

| Risk-ID | Tier-ID | Risk description | Type | Severity (High/Med/Low) |
|---------|---------|-----------------|------|------------------------|
| R-01    |         |                 | Burst |                       |
| R-02    |         |                 | Cascade |                    |
| R-03    |         |                 | RetryAfter |                 |
| ...     |         |                 |      |                        |

- `Type` — MUST be exactly one of: Burst, Cascade, RetryAfter. No other values permitted.
- `Tier-ID` — SHALL reference a T-NN from TABLE A.

**PHASE EXIT CONDITION:** Step 2G2 is closed when the TYPE SCAN GATE is cleared.

---

**Step 2H — MITIGATION REGISTRY (TABLE F)**

**PHASE ENTRY CONDITION:** Step 2H SHALL be entered after Step 2G2 is closed.

**Step 2H — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19):** Tiers
referenced in mitigation entries that are not in TABLE A are scope violations. An executor
SHALL NOT assign a new T-NN here. An executor SHALL return to TABLE A (complete Step 1A +
Step 1B), register the tier with all required columns, then continue.

TABLE F derives from TABLE E. One row per Risk-ID from TABLE E. No risk may be omitted.
A mitigation row that names a category of action ("add retry logic") requires further research
before it can be applied. A row that names the exact parameter can be applied immediately.

| MR-ID | Risk-ID | Gap type | Component | Setting or API parameter | Change | Expected outcome |
|-------|---------|----------|-----------|--------------------------|--------|-----------------|
| MR-01 |         |          |           |                          |        |                 |
| MR-02 |         |          |           |                          |        |                 |
| MR-03 |         |          |           |                          |        |                 |

`Setting or API parameter` — the exact configuration key, connector property, or API attribute
name SHALL be recorded here.

  - *Violation type: category of action substituted for named parameter identifier (e.g.,
    "add retry logic" instead of `connector.retryPolicy`).*
  - Compliance failure condition: A row naming a category of action rather than a specific
    parameter identifier fails this column's precision requirement.

---

## V-04 — Combined: C-20 + C-21

**Axis:** Prose-restriction declaration (C-20) at the top of the prompt + upstream source
reference header lines on every derived table (C-21). Typed-row risk taxonomy (C-22) is not
added. This is the natural pairing: a closed prose list makes format violations auditable,
and cross-artifact headers make coverage drift auditable. Together they enforce two orthogonal
audit properties — format and lineage — without requiring the typed taxonomy.

**Hypothesis:** C-20 and C-21 address different failure modes and can be satisfied
independently. Together they form a two-gate format discipline: C-20 makes format type
auditable (prose vs. table); C-21 makes artifact coverage auditable (which source tiers
appear in each downstream table). An output can satisfy C-20 (no prose outside declared
contexts) while failing C-21 (derived tables drift from source), and vice versa. V-04 tests
whether both gates can be cleared simultaneously without requiring the typed taxonomy.

**v7 predicted scoring:**
- C-20: PASS — labeled declaration present before first table, closed list
- C-21: PASS — upstream source identifier + coverage obligation header on every derived table
- C-22: FAIL — no Type column in risk/mitigation tables
- Composite: ~156/160

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
the rate-limited system described in the signal. Treat the stated request volume as 1x
nominal; also analyze at 2x and 5x.

The tables below are the primary output — each carries a distinct finding category that prose
cannot represent with the same auditability. Every cell SHALL be filled. Produce sections in
the order shown.

**PROSE-RESTRICTION DECLARATION (C-20) — This list is complete and closed:**
Prose is permitted only in the following four contexts. Prose appearing outside these contexts
is a format violation detectable by inspection without full content review.
1. `Load-shape verdict` mechanism explanation — one sentence per tier in TABLE A Step 1B.
2. Escape-route frame at Step 1B — naming the deferral temptation and the rejection mechanism.
3. UNIFORM/BURST narrative at Step 2G — one sentence per arrival pattern naming which tiers shift.
4. Self-verification verdict note at the closing audit — one sentence stating the pass/fail
   conclusion and, if FAIL, the criterion ID and gap.
All other analytical content SHALL be expressed in tables. If an executor finds itself writing
a sentence outside these four contexts, it SHALL stop and convert the content to a table row.

---

**STEP 1 — TIER REGISTRY**

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

*[Primary artifact. All downstream tables derive from TABLE A. No downstream table may
reference a Tier-ID absent from TABLE A.]*

| Tier-ID | Component | Limit (number + unit) | Scope | STATUS 1x | STATUS 2x | STATUS 5x | Binding at band | Load-shape verdict | Failure visibility window | Recovery time |
|---------|-----------|----------------------|-------|-----------|-----------|-----------|-----------------|-------------------|--------------------------|---------------|
| T-01    |           |                      |       |           |           |           |                 | [Step 1B]         |                          |               |
| T-02    |           |                      |       |           |           |           |                 | [Step 1B]         |                          |               |
| ...     |           |                      |       |           |           |           |                 | [Step 1B]         |                          |               |

Column definitions:
- `Tier-ID` — Assign T-01, T-02, ... and SHALL be used verbatim in every downstream section.
- `Limit (number + unit)` — a specific number with a unit (e.g., "1,000 req/min").
  - *Violation type: vague label substituted for numeric value (e.g., "limited" in place of
    "1,200 req/min").*
  - Compliance failure condition: An entry using a vague label instead of a specific
    number-with-unit fails this column's precision requirement.
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

**Escape-route frame:** The temptation to defer is the "STATUS tracks volume thresholds"
framing — because TABLE A STATUS columns use OK/HIT/SAT to track volume thresholds,
load-shape classification appears out of scope for the registry and naturally belonging in
"LOAD SHAPE COMPARISON." This frame is self-defeating: load-shape classification requires
the registered `Limit` value available now at Step 1B, and Step 2G depends on per-tier
Load-shape verdicts to produce meaningful comparisons — deferring creates a circular
dependency where the downstream section that would receive shape classification is itself
dependent on the per-tier verdict the registry was supposed to supply. Step 1B exists
precisely to foreclose this dependency.

For each TABLE A tier, update `Load-shape verdict`:
- State SHAPE-NEUTRAL or SHAPE-SENSITIVE
- State the numeric rate differential between uniform and burst arrival at this tier's limit
- State the mechanism that explains the differential

  - *Violation type: deferred verdict token — the executor routes the SHAPE-NEUTRAL/
    SHAPE-SENSITIVE classification to Step 2G rather than recording it at Step 1B.*
  - Compliance failure condition: A Load-shape verdict entry left blank or deferred
    ("see Step 2G", "analyzed below") at the end of Step 1B fails the registration-time
    classification requirement and invalidates Step 2G's numeric comparison.

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

**Step 2A — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19):** Tiers
appearing in backpressure analysis that are not in TABLE A are scope violations. An executor
SHALL NOT assign a new T-NN here. An executor SHALL return to TABLE A (complete Step 1A +
Step 1B), register the tier with all required columns, then continue.

*[TABLE B — Source: TABLE A. From (Tier-ID) SHALL reference a T-NN from TABLE A. Minimum
2 hops. No hop may reference a Tier-ID absent from TABLE A.]*

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
    "blocked" in place of "queue-fill").*
  - Compliance failure condition: A mechanism entry using a generic category label (blocked,
    throttled, slowed) rather than a specific named mechanism from the permitted set fails
    this column's precision requirement.

**PHASE EXIT CONDITION:** Step 2A SHALL be considered closed when at least two hops are
documented with T-NN identifiers and specific mechanisms.

---

**Step 2B — USER EXPERIENCE CATALOG (TABLE C)**

**PHASE ENTRY CONDITION:** Step 2B SHALL be entered after Step 2A PHASE EXIT CONDITION
is cleared.

*[TABLE C — Source: TABLE A. One row per T-NN from TABLE A. No tier may be omitted. No tier
absent from TABLE A may be added. Row count in TABLE C MUST equal row count in TABLE A.]*

| Tier-ID | Error code or signal | Retry-After present? (Y/N) | Retry-After surfaced to caller? (Y/N) | Visible in run history? (Y/N/SILENT) | Failure if Retry-After ignored |
|---------|---------------------|---------------------------|--------------------------------------|--------------------------------------|-------------------------------|
| T-01    |                     |                           |                                      |                                      |                               |
| T-02    |                     |                           |                                      |                                      |                               |

Column definitions:
- `Error code or signal` — Record the specific HTTP status code or platform-defined signal
  identifier returned at this throttle tier (e.g., "HTTP 429", "HTTP 503", "TL-0001").
  - *Violation type: plain description substituted for structured error code or signal
    identifier (e.g., "request fails" in place of "HTTP 429").*
  - Compliance failure condition: An `Error code or signal` entry using a plain description
    rather than a specific HTTP status code or platform signal identifier fails this column's
    precision requirement.

---

**Step 2C — UNPROTECTED BURST PATHS (TABLE D)**

**PHASE ENTRY CONDITION:** Step 2C SHALL be entered after Step 2B is closed.

**Step 2C — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19):** Tiers
referenced in burst path analysis that are not in TABLE A are scope violations. An executor
SHALL NOT assign a new T-NN here. An executor SHALL return to TABLE A.

*[TABLE D — Source: TABLE A. Tier-IDs involved SHALL reference T-NNs from TABLE A. At least
one row required.]*

| Path-ID | Entry component | Gap reason (structural gap or named controls) | Tier-IDs involved | Consequence at burst volume |
|---------|----------------|-----------------------------------------------|-------------------|-----------------------------|
| P-01    |                |                                               |                   |                             |

---

**Step 2D — TIER RISK RANKING**

**PHASE ENTRY CONDITION:** Step 2D SHALL be entered after Step 2C is closed.

*[RANKING — Source: TABLE A. All TABLE A tiers SHALL appear. No tier may be omitted. No tier
absent from TABLE A may be ranked.]*

All TABLE A tiers SHALL appear in the ranking, ordered by business risk, highest to lowest.
One sentence per tier with rationale SHALL be provided. For the top-ranked tier, `Failure
visibility window` and `Recovery time` from TABLE A SHALL be referenced.

---

**Step 2E — CASCADE SCENARIO**

**PHASE ENTRY CONDITION:** Step 2E SHALL be entered after Step 2D is closed.

**Step 2E — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19):** Tiers
introduced during cascade trace that are not in TABLE A are scope violations. An executor
SHALL NOT assign a new T-NN here. An executor SHALL return to TABLE A.

*[CASCADE — Source: TABLE A. All tier references SHALL use T-NN identifiers from TABLE A.
Minimum three tiers.]*

Trace one concrete cascade from the 1x binding constraint. T-NN identifiers SHALL be used
throughout. Each causal link SHALL be stated explicitly. A minimum of three tiers SHALL be
present, each step caused by the previous.

---

**Step 2F — RETRY-AFTER GAP ASSESSMENT**

**PHASE ENTRY CONDITION:** Step 2F SHALL be entered after Step 2E is closed.

*[RETRY-AFTER — Source: TABLE A and TABLE C. Binding-tier Tier-ID from TABLE A. Retry-After
status from TABLE C.]*

For the 1x binding constraint tier: is Retry-After present and surfaced? If absent, the
failure mode SHALL be named precisely — retry storm (exponential backoff) vs. quota
exhaustion (circuit breaker).

---

**Step 2G — LOAD SHAPE COMPARISON**

**PHASE ENTRY CONDITION:** Step 2G SHALL be entered after Step 2F is closed.

**Step 2G — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19):** Tiers
introduced during load shape analysis that are not in TABLE A are scope violations. An
executor SHALL NOT assign a new T-NN here. An executor SHALL return to TABLE A.

*[LOAD SHAPE — Source: TABLE A. Load-shape verdicts from TABLE A `Load-shape verdict` column
classified at Step 1B. Tier references SHALL use T-NNs from TABLE A.]*

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

*[TABLE F — Source: TABLE A. Component column SHALL reference T-NN or component name from
TABLE A. Minimum 2 rows. No component absent from TABLE A may appear.]*

A mitigation row that names a category of action ("add retry logic") requires further research
before it can be applied. A row that names the exact parameter can be applied immediately.

| MR-ID | Source | Gap type | Component | Setting or API parameter | Change | Expected outcome |
|-------|--------|----------|-----------|--------------------------|--------|-----------------|
| MR-01 |        |          |           |                          |        |                 |
| MR-02 |        |          |           |                          |        |                 |

`Setting or API parameter` — the exact configuration key, connector property, or API attribute
name SHALL be recorded here.

  - *Violation type: category of action substituted for named parameter identifier (e.g.,
    "add retry logic" instead of `connector.retryPolicy`).*
  - Compliance failure condition: A row naming a category of action rather than a specific
    parameter identifier fails this column's precision requirement.

---

**CLOSING AUDIT**

Confirm C-01 through C-08 compliance. For each criterion, state PASS or FAIL. If FAIL, name
the gap in one sentence. Self-verification verdict note (prose permitted here per the
Prose-Restriction Declaration): state whether all criteria pass or identify the failing
criterion and the gap.

---

## V-05 — Combined: C-20 + C-21 + C-22 (All Three New v7 Criteria)

**Axis:** All three new v7 criteria simultaneously. Prose-restriction declaration at the top
(C-20). Upstream source reference header lines on every derived table (C-21). Typed-row risk
taxonomy TABLE E inserted between 2G and 2H, with TABLE F deriving from TABLE E rather than
TABLE A directly (C-22). This combination maximally constrains the output: format is auditable
by declaration, lineage is auditable by table header, and risk category coverage is auditable
by type scan.

**Hypothesis:** C-20 + C-21 + C-22 form a coherent triad: C-20 constrains output format,
C-21 constrains artifact lineage, C-22 constrains failure-category coverage. No two of these
subsume the third. A count-only mitigation table can satisfy C-21 (one row per risk from
TABLE E) while failing C-22 (two rows of the same Type). A typed table can satisfy C-22
while failing C-21 (no source header on TABLE F). V-05 tests whether all three gates can be
held simultaneously. The structural interaction of interest: does the TABLE E insertion
require C-21's source reference on TABLE F to change from "Source: TABLE A" to "Source: TABLE
E", and does that change remain consistent with the registry gap prohibition?

**v7 predicted scoring:**
- C-20: PASS — labeled declaration present before first table, closed list
- C-21: PASS — upstream source identifier + coverage obligation header on every derived table,
  including TABLE F citing TABLE E as its source
- C-22: PASS — TABLE E has Type column, three required types, per-type minimum row guarantee
- Composite: 160/160

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
the rate-limited system described in the signal. Treat the stated request volume as 1x
nominal; also analyze at 2x and 5x.

The tables below are the primary output — each carries a distinct finding category that prose
cannot represent with the same auditability. Every cell SHALL be filled. Produce sections in
the order shown.

**PROSE-RESTRICTION DECLARATION (C-20) — This list is complete and closed:**
Prose is permitted only in the following four contexts. Prose appearing outside these contexts
is a format violation detectable by inspection without full content review.
1. `Load-shape verdict` mechanism explanation — one sentence per tier in TABLE A Step 1B.
2. Escape-route frame at Step 1B — naming the deferral temptation and the rejection mechanism.
3. UNIFORM/BURST narrative at Step 2G — one sentence per arrival pattern naming which tiers shift.
4. Self-verification verdict note at the closing audit — one sentence stating the pass/fail
   conclusion and, if FAIL, the criterion ID and gap.
All other analytical content SHALL be expressed in tables. If an executor finds itself writing
a sentence outside these four contexts, it SHALL stop and convert the content to a table row.

---

**STEP 1 — TIER REGISTRY**

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

*[Primary artifact. All downstream tables derive from TABLE A directly or transitively.
No downstream table may reference a Tier-ID absent from TABLE A.]*

| Tier-ID | Component | Limit (number + unit) | Scope | STATUS 1x | STATUS 2x | STATUS 5x | Binding at band | Load-shape verdict | Failure visibility window | Recovery time |
|---------|-----------|----------------------|-------|-----------|-----------|-----------|-----------------|-------------------|--------------------------|---------------|
| T-01    |           |                      |       |           |           |           |                 | [Step 1B]         |                          |               |
| T-02    |           |                      |       |           |           |           |                 | [Step 1B]         |                          |               |
| ...     |           |                      |       |           |           |           |                 | [Step 1B]         |                          |               |

Column definitions:
- `Tier-ID` — Assign T-01, T-02, ... and SHALL be used verbatim in every downstream section.
- `Limit (number + unit)` — a specific number with a unit (e.g., "1,000 req/min").
  - *Violation type: vague label substituted for numeric value (e.g., "limited" in place of
    "1,200 req/min").*
  - Compliance failure condition: An entry using a vague label instead of a specific
    number-with-unit fails this column's precision requirement.
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

**Escape-route frame:** The temptation to defer is the "STATUS tracks volume thresholds"
framing — because TABLE A STATUS columns use OK/HIT/SAT to track volume thresholds,
load-shape classification appears out of scope for the registry and naturally belonging in
"LOAD SHAPE COMPARISON." This frame is self-defeating: load-shape classification requires
the registered `Limit` value available now at Step 1B, and Step 2G depends on per-tier
Load-shape verdicts to produce meaningful comparisons — deferring creates a circular
dependency where the downstream section that would receive shape classification is itself
dependent on the per-tier verdict the registry was supposed to supply. Step 1B exists
precisely to foreclose this dependency.

For each TABLE A tier, update `Load-shape verdict`:
- State SHAPE-NEUTRAL or SHAPE-SENSITIVE
- State the numeric rate differential between uniform and burst arrival at this tier's limit
- State the mechanism that explains the differential

  - *Violation type: deferred verdict token — the executor routes the SHAPE-NEUTRAL/
    SHAPE-SENSITIVE classification to Step 2G rather than recording it at Step 1B.*
  - Compliance failure condition: A Load-shape verdict entry left blank or deferred
    ("see Step 2G", "analyzed below") at the end of Step 1B fails the registration-time
    classification requirement and invalidates Step 2G's numeric comparison.

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

**Step 2A — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19):** Tiers
appearing in backpressure analysis that are not in TABLE A are scope violations. An executor
SHALL NOT assign a new T-NN here. An executor SHALL return to TABLE A (complete Step 1A +
Step 1B), register the tier with all required columns, then continue.

*[TABLE B — Source: TABLE A. From (Tier-ID) SHALL reference a T-NN from TABLE A. Minimum
2 hops required. No hop may reference a Tier-ID absent from TABLE A. — Prevents scope creep
into the backpressure trace.]*

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
    "blocked" in place of "queue-fill").*
  - Compliance failure condition: A mechanism entry using a generic category label (blocked,
    throttled, slowed) rather than a specific named mechanism from the permitted set fails
    this column's precision requirement.

**PHASE EXIT CONDITION:** Step 2A SHALL be considered closed when at least two hops are
documented with T-NN identifiers and specific mechanisms.

---

**Step 2B — USER EXPERIENCE CATALOG (TABLE C)**

**PHASE ENTRY CONDITION:** Step 2B SHALL be entered after Step 2A PHASE EXIT CONDITION
is cleared.

*[TABLE C — Source: TABLE A. One row per T-NN from TABLE A. No tier may be omitted. No tier
absent from TABLE A may be added. Row count in TABLE C MUST equal row count in TABLE A.
— Prevents coverage elision in the UX artifact.]*

| Tier-ID | Error code or signal | Retry-After present? (Y/N) | Retry-After surfaced to caller? (Y/N) | Visible in run history? (Y/N/SILENT) | Failure if Retry-After ignored |
|---------|---------------------|---------------------------|--------------------------------------|--------------------------------------|-------------------------------|
| T-01    |                     |                           |                                      |                                      |                               |
| T-02    |                     |                           |                                      |                                      |                               |

Column definitions:
- `Error code or signal` — Record the specific HTTP status code or platform-defined signal
  identifier returned at this throttle tier (e.g., "HTTP 429", "HTTP 503", "TL-0001").
  - *Violation type: plain description substituted for structured error code or signal
    identifier (e.g., "request fails" in place of "HTTP 429").*
  - Compliance failure condition: An `Error code or signal` entry using a plain description
    rather than a specific HTTP status code or platform signal identifier fails this column's
    precision requirement.

---

**Step 2C — UNPROTECTED BURST PATHS (TABLE D)**

**PHASE ENTRY CONDITION:** Step 2C SHALL be entered after Step 2B is closed.

**Step 2C — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19):** Tiers
referenced in burst path analysis that are not in TABLE A are scope violations. An executor
SHALL NOT assign a new T-NN here. An executor SHALL return to TABLE A.

*[TABLE D — Source: TABLE A. Tier-IDs involved SHALL reference T-NNs from TABLE A. At least
one row required. If no unprotected path exists, row 1 states conclusion with two named
controls. — Prevents burst analysis from introducing undeclared tiers.]*

| Path-ID | Entry component | Gap reason (structural gap or named controls) | Tier-IDs involved | Consequence at burst volume |
|---------|----------------|-----------------------------------------------|-------------------|-----------------------------|
| P-01    |                |                                               |                   |                             |

---

**Step 2D — TIER RISK RANKING (TABLE D2)**

**PHASE ENTRY CONDITION:** Step 2D SHALL be entered after Step 2C is closed.

*[TABLE D2 — Source: TABLE A. One row per T-NN from TABLE A. No tier may be omitted. No tier
absent from TABLE A may be ranked. Row count MUST equal TABLE A row count.
— Prevents ranking from silently dropping lower-risk tiers.]*

| Rank | Tier-ID | Business risk rationale | Failure visibility window (from TABLE A) | Recovery time (from TABLE A) |
|------|---------|------------------------|------------------------------------------|------------------------------|
| 1    |         |                        |                                          |                              |
| 2    |         |                        | N/A (top-rank only)                      | N/A (top-rank only)          |
| ...  |         |                        |                                          |                              |

For the top-ranked tier (Rank = 1), `Failure visibility window` and `Recovery time` SHALL be
copied verbatim from TABLE A.

---

**Step 2E — CASCADE SCENARIO (TABLE E1)**

**PHASE ENTRY CONDITION:** Step 2E SHALL be entered after Step 2D is closed.

**Step 2E — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19):** Tiers
introduced during cascade trace that are not in TABLE A are scope violations. An executor
SHALL NOT assign a new T-NN here. An executor SHALL return to TABLE A.

*[TABLE E1 — Source: TABLE A. Tier-ID column SHALL reference T-NNs from TABLE A. Minimum
3 cascade steps. Each step caused by the prior row.]*

| Step | Tier-ID | Event | Causal link to next step |
|------|---------|-------|--------------------------|
| 1    |         |       |                          |
| 2    |         |       |                          |
| 3    |         |       | (terminal step)          |

---

**Step 2F — RETRY-AFTER GAP ASSESSMENT (TABLE E2)**

**PHASE ENTRY CONDITION:** Step 2F SHALL be entered after Step 2E is closed.

*[TABLE E2 — Source: TABLE A (binding tier) and TABLE C (Retry-After column). One row per
binding tier identified in TABLE A.]*

| Tier-ID | Binding band | Retry-After present? | Retry-After surfaced? | If absent: failure mode |
|---------|-------------|---------------------|-----------------------|------------------------|
|         |             |                     |                       | retry storm / quota exhaustion |

`If absent: failure mode` — state exactly one: retry storm (exponential backoff) or quota
exhaustion (circuit breaker).

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

**Step 2G2 — RISK INVENTORY (TABLE E3)**

**PHASE ENTRY CONDITION:** Step 2G2 SHALL be entered after Step 2G is closed.

*[TABLE E3 — Source: TABLE A. Tier-ID column SHALL reference T-NNs from TABLE A. Minimum 3
rows required — one per Type. TABLE F (Step 2H) derives from TABLE E3, not TABLE A directly.
— Prevents mitigation drift by inserting a typed intermediary artifact.]*

**TYPED-ROW COVERAGE GUARANTEE (C-22):** TABLE E3 uses a Type column with a closed taxonomy:
Burst / Cascade / RetryAfter. The table SHALL contain at least one row of Type = Burst, at
least one row of Type = Cascade, and at least one row of Type = RetryAfter. A table that
satisfies a count requirement (e.g., two rows) using two rows of the same Type while omitting
a category fails the minimum-coverage guarantee. Category-level absence is detectable by type
scan — an executor SHALL scan the Type column after completing the table and confirm all three
types are present before proceeding to Step 2H.

**TYPE SCAN GATE:** Before opening Step 2H, an executor SHALL confirm: (a) at least one
Burst row present; (b) at least one Cascade row present; (c) at least one RetryAfter row
present. If any type is absent, an executor SHALL add the missing row before proceeding.

| Risk-ID | Tier-ID | Risk description | Type | Severity (High/Med/Low) |
|---------|---------|-----------------|------|------------------------|
| R-01    |         |                 | Burst |                       |
| R-02    |         |                 | Cascade |                    |
| R-03    |         |                 | RetryAfter |                 |
| ...     |         |                 |      |                        |

- `Type` — MUST be exactly one of: Burst, Cascade, RetryAfter. No other values permitted.
- `Tier-ID` — SHALL reference a T-NN from TABLE A.

**PHASE EXIT CONDITION:** Step 2G2 is closed when the TYPE SCAN GATE is cleared.

---

**Step 2H — MITIGATION REGISTRY (TABLE F)**

**PHASE ENTRY CONDITION:** Step 2H SHALL be entered after Step 2G2 is closed.

**Step 2H — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19):** Tiers
referenced in mitigation entries that are not in TABLE A are scope violations. An executor
SHALL NOT assign a new T-NN here. An executor SHALL return to TABLE A (complete Step 1A +
Step 1B), register the tier with all required columns, then continue.

*[TABLE F — Source: TABLE E3 (Risk Inventory). One row per Risk-ID from TABLE E3. No risk
may be omitted. No risk absent from TABLE E3 may be added. Row count in TABLE F MUST equal
row count in TABLE E3. — Prevents mitigation coverage drift from the typed risk inventory.]*

A mitigation row that names a category of action ("add retry logic") requires further research
before it can be applied. A row that names the exact parameter can be applied immediately.

| MR-ID | Risk-ID | Gap type | Component | Setting or API parameter | Change | Expected outcome |
|-------|---------|----------|-----------|--------------------------|--------|-----------------|
| MR-01 | R-01    |          |           |                          |        |                 |
| MR-02 | R-02    |          |           |                          |        |                 |
| MR-03 | R-03    |          |           |                          |        |                 |

`Setting or API parameter` — the exact configuration key, connector property, or API attribute
name SHALL be recorded here.

  - *Violation type: category of action substituted for named parameter identifier (e.g.,
    "add retry logic" instead of `connector.retryPolicy`).*
  - Compliance failure condition: A row naming a category of action rather than a specific
    parameter identifier fails this column's precision requirement.

---

**CLOSING AUDIT**

Confirm C-01 through C-08 compliance. For each criterion, state PASS or FAIL with evidence
location (table name + column or step). Self-verification verdict note (prose permitted here
per the Prose-Restriction Declaration): state whether all criteria pass or identify the
failing criterion and the gap.
