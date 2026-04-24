# flow-throttle Variate — Round 17

**Date:** 2026-03-16
**Rubric:** v17 (C-01–C-44, N_essential=5, N_recommended=3, N_aspirational=36)
**Max composite:** 270 | **Baseline ceiling:** R16 best (265/270 under v17)

---

## State Analysis: What R16 Has vs. What R17 Must Add

**R16 coverage under v17 (assessed):**
- C-01 through C-41: all pass (best R16 variant)
- C-42: PASS in all R16 variants — Field 5 in audit explicitly names the gate and verifies
  CLEARED status before Step 1A. Satisfies the "gate compliance is a first-class audit
  target" requirement.
- C-43: PASS in V-03 and V-05 only. Those variants have Role 1.5 producing a distinct
  INVENTORY VERIFIED signal separate from FORMAT CONTRACT COMPLETE. V-01, V-02, V-04 have
  only one signal (GATE STATUS = CLEARED or ACTIVATION STATUS = PROCEED), which conflates
  section-presence confirmation with count verification. The structural distinction "sections
  present" vs. "count verified" is not visible in those variants.
- C-44: PASS in V-05 only. The "looks complete" bypass is named and defeated with a
  structural proof only in V-05. V-01 through V-04 do not name the bypass failure mode or
  provide the structural proof that FORMAT CONTRACT COMPLETE is not equivalent to count
  completeness.

**R17 gaps by variant:**

| Variant | C-42 | C-43 | C-44 | Score under v17 |
|---------|------|------|------|----------------|
| V-01 | PASS | FAIL | FAIL | 260/270 |
| V-02 | PASS | FAIL | FAIL | 260/270 |
| V-03 | PASS | PASS | FAIL | 265/270 |
| V-04 | PASS | FAIL | FAIL | 260/270 |
| V-05 | PASS | PASS | PASS | 270/270 |

**R17 task:** All 5 variations must achieve 270/270. Variation axes determine HOW C-43 and
C-44 are expressed structurally — not WHETHER they are present. Every variation must carry
all three new criteria simultaneously.

**Round 17 variation map:**

| Variation | Axes | C-41 mechanism | C-43 mechanism | C-44 mechanism | Predicted composite |
|-----------|------|----------------|----------------|----------------|---------------------|
| V-01 | Lifecycle emphasis (single) | SIGNAL CHECKPOINT with two milestone records | Two-row milestone table: Signal 1 = section-presence, Signal 2 = count-complete | Bypass-failure note at checkpoint with lifecycle framing | 270/270 |
| V-02 | Output format (single) | PHASE 1 ACTIVATION SEQUENCE with signal distinction table + count table | Signal distinction table with "Confirms" and "Does NOT confirm" columns | Bypass-attempt rejection table naming "looks complete" as a row | 270/270 |
| V-03 | Role sequence (single) | Role 1.5 (INVENTORY VERIFIER) — distinct role, single responsibility | Two separate roles produce two signals; architectural separation | C-44 inertia-frame rejection as first content of Role 1.5 | 270/270 |
| V-04 | Phrasing register + lifecycle | TWO-SIGNAL MANDATORY GATEWAY with SHALL-separated signal declarations | Two explicit SHALL-NOT-conflate statements at gateway | PROHIBITED bypass clause naming "looks complete" failure mode | 270/270 |
| V-05 | Role sequence + output format + inertia framing | Role 1.5 + verification table + role activation chain | Signal distinction table (SIG-01/SIG-02) with Confirms column + role chain | Named failure mode + structural proof paragraph + rejection field | 270/270 |

---

## V-01

**Axis:** Lifecycle emphasis (single-axis)

**Hypothesis:** Adding a named two-signal lifecycle SIGNAL CHECKPOINT between FORMAT CONTRACT
COMPLETE and Role 2 — with explicit milestone records for each signal's distinct meaning —
satisfies C-43 without requiring a separate Role 1.5. The checkpoint labels Signal 1 as
section-presence and Signal 2 as count-completeness, making the structural distinction
visible as a milestone column value. A bypass-failure note at the checkpoint satisfies C-44.
Field 5 in the audit block explicitly verifies both signals and the CHECKPOINT STATUS field
were recorded before Step 1A, satisfying C-42.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
the rate-limited system described in the signal. Treat the stated request volume as 1x
nominal; also analyze at 2x and 5x.

This prompt uses a three-phase activation structure: **Role 1 (FORMAT CONTRACT)** produces
the precision inventory and annotation contract; the **SIGNAL CHECKPOINT** records two
distinct milestone signals and verifies the annotation inventory count before analysis opens;
**Role 2 (DOMAIN EXPERT)** runs only after both signals are confirmed. The tables below are
the primary output — every cell SHALL be filled. Produce sections in the order shown.

---

**ROLE 1 — FORMAT CONTRACT**

**Section A — Precision-site inventory**

This section inventories every location in this prompt where a column definition carries a
violation-type annotation. An executor SHALL verify, at the SIGNAL CHECKPOINT, that every
listed site is present in Section C and that its annotation is placed at its anchor site.
Count: 7 precision sites across 5 tables.

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
- *Violation type: vague-label substitution — a vague label ("limited", "throttled")
  substituted for a specific number-with-unit.*
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
Record the specific HTTP status code or platform signal identifier (e.g., "HTTP 429",
"TL-0001").
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

**FORMAT CONTRACT COMPLETE** — Signal 1 of 2. This signal confirms that Role 1 Sections A,
B, and C are structurally present. It does NOT confirm that Section C annotation count equals
the declared count of 7. Count verification is performed at the SIGNAL CHECKPOINT.

---

**SIGNAL CHECKPOINT — Two-milestone activation record**

This checkpoint records two named signals. Role 2 SHALL NOT open until both signals are
confirmed at this checkpoint.

**Signal distinction — why two signals are required:**

FORMAT CONTRACT COMPLETE (Signal 1) confirms that Sections A, B, and C are present — it is
a *section-presence* signal. INVENTORY VERIFIED (Signal 2) confirms that Section C contains
the declared count of 7 annotations — it is a *count-completeness* signal. These signals are
structurally distinct: a Section C with 6 of 7 annotations satisfies Signal 1 (all sections
present) while failing Signal 2 (count below declared). Conflating the two signals converts
the count check into an unverified assertion detectable only after Role 2 produces output.

**Bypass-failure prohibition:**

The "looks complete" bypass failure mode: FORMAT CONTRACT COMPLETE has been stated and the
analysis tables are scaffolded, so Role 2 appears ready to activate. This bypass is
self-defeating. FORMAT CONTRACT COMPLETE is a section-presence signal only — it does not
verify that the annotation inventory is complete to its declared count. Skipping this
checkpoint converts the Section C count from a verifiable gate into an unverified assertion.
This checkpoint exists precisely because Signal 1 and Signal 2 are non-overlapping: Signal 1
is produced by Role 1 when sections are structurally present; Signal 2 is produced at this
checkpoint only after the count is verified. An executor SHALL complete both milestones before
Role 2 opens.

**Milestone 1 — Signal 1 record:**

| Milestone | Signal | Source | Confirms | Recorded? |
|-----------|--------|--------|----------|-----------|
| M-1 | FORMAT CONTRACT COMPLETE | Role 1 | Sections A, B, C structurally present | [Y/N] |

**Milestone 2 — Signal 2 activation (count verification):**

1. Count the Annot-ID rows in Section C above.
2. Compare to declared count: Section C declares 7 required annotations; expected row count = 7.
3. Apply outcome:
   - Row count = 7 → Record **INVENTORY VERIFIED** (Signal 2 confirmed). Both milestones
     complete — proceed to Role 2.
   - Row count < 7 → Record **INVENTORY INCOMPLETE** (Signal 2 withheld). The annotation
     inventory is incomplete. FORMAT CONTRACT COMPLETE was stated but count completeness is
     unverified. Return to Role 1, complete Section C to 7 rows, re-state FORMAT CONTRACT
     COMPLETE (re-record Milestone 1), then re-enter this checkpoint.

**CHECKPOINT STATUS:**
- Signal 1 (FORMAT CONTRACT COMPLETE): [ CONFIRMED / NOT YET ]
- Signal 2 (INVENTORY VERIFIED): [ CONFIRMED / WITHHELD ]
- Role 2 activation: [ OPEN — both signals confirmed / BLOCKED — return to Role 1 ]

An executor SHALL record all three fields before opening Role 2 / Step 1A.

---

**ROLE 2 — DOMAIN EXPERT**

**REGISTRY GAP PROHIBITION — Failure 5 prevention (C-17):** Tiers discovered during Step 2
are scope violations — evidence that the enumeration phase was incomplete. PROHIBITED:
assigning a new T-NN during Step 2 as a fill-in step. An executor SHALL return to TABLE A,
register the tier with all columns filled, and SHALL restart from the point of discovery.
This prohibition SHALL be restated at each Step 2 section where mid-phase discovery could
occur.

---

**Step 1A — VOLUME ANALYST: TIER IDENTIFICATION AND LIMITS**

**PHASE ENTRY CONDITION:** Step 1A SHALL be entered after CHECKPOINT STATUS Role 2 activation
= OPEN and the signal input has been read in full.

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
absent, name the failure mode precisely — retry storm (exponential backoff without Retry-After
guidance) vs. quota exhaustion (circuit breaker approach required).

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
non-placeholder `Load-shape verdict` assigned at Step 1B, not in Step 2G. State PASS or list
deferred rows.

**Field 4 — Annotation dropout (C-40):** Every Annot-01 through Annot-07 is present at its
anchor site. State PASS or list: Annot-ID | anchor site | status.

**Field 5 — SIGNAL CHECKPOINT gate compliance (C-41 + C-42):** The SIGNAL CHECKPOINT was
completed before Step 1A opened. Both signals were explicitly recorded: Signal 1 (FORMAT
CONTRACT COMPLETE, section-presence) confirmed at Milestone 1, and Signal 2 (INVENTORY
VERIFIED, count-completeness) confirmed at Milestone 2. CHECKPOINT STATUS Role 2 activation
was explicitly set to OPEN before Step 1A began. State PASS or FAIL with explanation citing
which signal record is absent or which CHECKPOINT STATUS field was not set to OPEN. Gate
compliance is verified by evidence in the checkpoint, not inferred from body quality.

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

**Hypothesis:** Expressing the two-signal chain as a dedicated signal distinction table —
with "Confirms" and "Does NOT confirm" columns — makes the section-presence vs.
count-completeness distinction structurally visible as a column value rather than a prose
argument, satisfying C-43. A bypass-attempt rejection table names "looks complete" as a
typed failure mode and provides a structural reason for rejection, satisfying C-44. Field 5
uses a multi-row verification table requiring an explicit CLEARED evidence row per check,
satisfying C-42.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
the rate-limited system described in the signal. Treat the stated request volume as 1x
nominal; also analyze at 2x and 5x.

The tables below are the primary output — every cell SHALL be filled. Produce sections in
the order shown. This prompt has three structural stages: FORMAT CONTRACT (Role 1), PHASE 1
ACTIVATION SEQUENCE (two-signal count gate), and ANALYSIS (Role 2).

---

**ROLE 1 — FORMAT CONTRACT**

**Section A — Precision-site inventory**

[Identical to V-01 Section A — 7-site table with Site-IDs S-01 through S-07, multi-adjacent
note for S-01/S-02/S-03, and non-conflation count of 3 at TABLE A.]

**Section B — Format contract**

[Identical to V-01 Section B — 7 column definitions for TABLE A `Limit`, TABLE A `Binding?`,
TABLE A `Failure mode`, TABLE B `Mechanism`, TABLE C `Error code or signal`, TABLE E `Type`,
TABLE F `Setting or API parameter`. Each definition includes `*Violation type:*` annotation
and compliance failure condition per C-27.]

**Section C — Annotation inventory**

This section declares **7 required annotations**. The PHASE 1 ACTIVATION SEQUENCE verifies
this count before analysis begins.

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

**PHASE 1 ACTIVATION SEQUENCE**

Fill all tables in this section before opening any analysis section. Phase 1 SHALL NOT open
until ACTIVATION STATUS reads PROCEED.

**Table 1 — Signal distinction register:**

| Signal ID | Signal name | Produced by | Confirms | Does NOT confirm |
|-----------|------------|-------------|----------|-----------------|
| SIG-01 | FORMAT CONTRACT COMPLETE | Role 1 | Sections A, B, C are structurally present | That Section C annotation count = declared count of 7 |
| SIG-02 | INVENTORY VERIFIED | This activation sequence | Section C Annot-ID row count = declared count of 7 | — |

An executor SHALL NOT treat SIG-01 as evidence that SIG-02 is satisfied. "Sections present"
(SIG-01) and "count verified" (SIG-02) are non-overlapping guarantees confirmed by distinct
mechanisms.

**Table 2 — Bypass-attempt rejection register:**

| Bypass attempt | Attempt type | Structural reason for rejection |
|----------------|-------------|---------------------------------|
| Proceed to Role 2 after FORMAT CONTRACT COMPLETE without completing Table 3 count check | "Looks complete" — SIG-01 stated, tables scaffolded | SIG-01 (FORMAT CONTRACT COMPLETE) confirms section presence, not count completeness. SIG-02 requires an independent count verification. Skipping Table 3 leaves Section C count as an unverified assertion: a Section C with 6 of 7 annotations satisfies SIG-01 while failing SIG-02, and the discrepancy is detectable only after Role 2 produces output. |

**Table 3 — Count verification:**

| Check | Expected | Actual | Verdict |
|-------|----------|--------|---------|
| SIG-01 (FORMAT CONTRACT COMPLETE) recorded in Role 1 | Present | [Y/N] | PROCEED if Y |
| Section C Annot-ID row count | 7 | [count them] | PROCEED if actual = 7; RETURN TO ROLE 1 if actual < 7 |

**ACTIVATION STATUS:**
- All Table 3 rows → PROCEED: **INVENTORY VERIFIED** (SIG-02 confirmed). Record:
  ACTIVATION STATUS = PROCEED. Open Phase 1.
- Any Table 3 row → RETURN TO ROLE 1: SIG-02 withheld. Complete the indicated gap. Re-state
  FORMAT CONTRACT COMPLETE (re-confirm SIG-01). Re-fill Table 3 from the top.

**ACTIVATION STATUS: [ PROCEED / RETURN TO ROLE 1 ]** — This field SHALL be filled before
Step 1A begins.

---

**ROLE 2 — DOMAIN EXPERT**

**REGISTRY GAP PROHIBITION — Failure 5 prevention (C-17):** [Identical to V-01.]

**Step 1A — VOLUME ANALYST: TIER IDENTIFICATION AND LIMITS**

**PHASE ENTRY CONDITION:** Step 1A SHALL be entered only after ACTIVATION STATUS = PROCEED.

[TABLE A with all columns as V-01, including Binding? with causal mechanism, Failure mode
with diversity requirement, Load-shape verdict placeholder. STEP 1A GATE as V-01.]

**Step 1B — LOAD-SHAPE ANALYST: CLASSIFICATION**

[Identical to V-01 Step 1B — deferral prohibition, escape-route frame, STEP 1B GATE.]

**Steps 2A through 2H** — [Identical structure to V-01 Steps 2A–2H, including distributed
REGISTRY GAP reminders at 2A, 2C, 2E, 2G, 2H, phase entry/exit conditions, and all table
schemas with column definitions as V-01.]

---

**ROLE 3 — AUDIT**

**Audit block — compliance verification**

**Field 1 — Tier-ID threading (C-13):** [Identical to V-01.]

**Field 2 — REGISTRY GAP enforcement (C-17/C-19):** [Identical to V-01.]

**Field 3 — Load-shape classification at registration (C-16):** [Identical to V-01.]

**Field 4 — Annotation dropout (C-40):** [Identical to V-01.]

**Field 5 — PHASE 1 ACTIVATION SEQUENCE compliance (C-41 + C-42):**

| Verification check | Required | Evidence | Status |
|--------------------|----------|----------|--------|
| SIG-01 (FORMAT CONTRACT COMPLETE) recorded in Role 1 | Present | [cite location in body] | PASS / FAIL |
| Table 3 count check completed with Actual and Verdict filled | Filled | [cite Actual value and Verdict] | PASS / FAIL |
| ACTIVATION STATUS = PROCEED recorded before Step 1A | PROCEED | [cite location in body] | PASS / FAIL |
| SIG-02 (INVENTORY VERIFIED) confirmed before Step 1A | Confirmed | [cite Table 3 Verdict = PROCEED] | PASS / FAIL |

State overall PASS if all rows = PASS. State FAIL with the table row identifying which check
failed and what evidence is absent. Gate compliance is verified by evidence in the body, not
inferred from output quality.

**Per-section compliance status (C-18):** [Identical to V-01.]

---

## V-03

**Axis:** Role sequence (single-axis)

**Hypothesis:** A dedicated Role 1.5 (INVENTORY VERIFIER) creates the most architecturally
clean two-signal chain for C-43 — two separate roles produce two separate signals, making
the distinction between FORMAT CONTRACT COMPLETE (section-presence, Role 1) and INVENTORY
VERIFIED (count-completeness, Role 1.5) visible in the role structure itself rather than
in text. Opening Role 1.5 with the C-44 inertia-frame rejection as its first substantive
content makes the bypass-failure mode impossible to encounter without reading the rejection.
Field 5 explicitly verifies the Role 1.5 HANDOFF SIGNAL = INVENTORY VERIFIED was recorded
before Step 1A and requires that this signal — not FORMAT CONTRACT COMPLETE — is the Phase 1
activation condition, satisfying C-42.

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

[Identical to V-01 Section A — 7-site table with Site-IDs S-01 through S-07, multi-adjacent
note for S-01/S-02/S-03, and non-conflation count of 3.]

**Section B — Format contract**

[Identical to V-01 Section B — 7 column definitions, each with `*Violation type:*` annotation
and compliance failure condition per C-27.]

**Section C — Annotation inventory**

This section declares **7 required annotations**. Count-scan verification: expected rows = 7.
Role 1.5 verifies this count before Role 2 opens.

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

**FORMAT CONTRACT COMPLETE** — Role 1 handoff signal. This signal confirms section presence.
Role 1.5 activation condition is met.

---

**ROLE 1.5 — INVENTORY VERIFIER**

**Activation condition:** FORMAT CONTRACT COMPLETE has been stated by Role 1.
**Single responsibility:** Confirm that Section C annotation inventory row count equals the
declared count of 7 and produce INVENTORY VERIFIED. This role has no other responsibility
and produces no analysis output.

**Signal distinction — why Role 1.5 exists as a separate role:**

FORMAT CONTRACT COMPLETE (Role 1 handoff) confirms that Sections A, B, and C are
structurally present — it is a *section-presence* signal. INVENTORY VERIFIED (Role 1.5
handoff) confirms that Section C row count equals the declared count of 7 — it is a
*count-completeness* signal. These are distinct guarantees produced by distinct roles. A
Section C with 6 of 7 annotations satisfies FORMAT CONTRACT COMPLETE (sections present)
while failing INVENTORY VERIFIED (count below declared). Without Role 1.5, the count check
has no dedicated producer and a discrepancy is detectable only after Role 2 has generated
output. Role 1.5 exists to close this gap.

**Inertia-frame rejection — the "looks complete" bypass failure mode:**

The temptation to skip Role 1.5 and proceed directly to Role 2 is the "looks complete"
framing: FORMAT CONTRACT COMPLETE has been stated and the analysis tables are scaffolded, so
Role 2 appears ready to activate. This framing is self-defeating. FORMAT CONTRACT COMPLETE
is a *section-presence* signal — it confirms that Role 1 produced its sections, not that
Section C is complete to its declared count. Skipping Role 1.5 converts the Section C count
from a verifiable gate into an unverified assertion. A count discrepancy (e.g., 6 of 7
annotations present) is detectable only after Role 2 produces output, not before. Role 1.5
closes this gap by making count verification the activation condition for Role 2, not
section-presence alone. This proof is parallel to C-26 at Step 1B: just as Step 1B cannot be
deferred because Step 2G is structurally dependent on Load-shape verdicts that only Step 1B
produces, Role 2 cannot bypass Role 1.5 because Role 2's annotation contract depends on a
count-verified inventory that only Role 1.5 certifies.

**Verification procedure:**

1. Count the Annot-ID rows in Section C.
2. Declared count: 7.
3. Actual count: [fill].
4. Outcome:
   - Actual = 7 → state **INVENTORY VERIFIED** — Role 2 may activate.
   - Actual < 7 → state **INVENTORY INCOMPLETE** — Section C has [7 - actual] missing rows.
     Return to Role 1. Complete Section C. Re-state FORMAT CONTRACT COMPLETE. Re-enter Role
     1.5 from step 1.

**Role 1.5 HANDOFF SIGNAL: [ INVENTORY VERIFIED / INVENTORY INCOMPLETE ]** — fill before
Role 2.

---

**ROLE 2 — DOMAIN EXPERT**

**Activation condition:** Role 1.5 HANDOFF SIGNAL = INVENTORY VERIFIED.

An executor SHALL NOT open Step 1A until the Role 1.5 handoff signal is INVENTORY VERIFIED.
If INVENTORY INCOMPLETE was stated, Role 2 does not activate.

**REGISTRY GAP PROHIBITION — Failure 5 prevention (C-17):** Tiers discovered during Step 2
are scope violations. PROHIBITED: assigning a new T-NN during Step 2. An executor SHALL
return to TABLE A, register the tier with all columns filled, and SHALL restart from the
point of discovery. This prohibition SHALL be restated at each Step 2 section where
mid-phase discovery could occur.

---

**Step 1A — VOLUME ANALYST: TIER IDENTIFICATION AND LIMITS**

**PHASE ENTRY CONDITION:** Step 1A SHALL be entered only after Role 1.5 HANDOFF SIGNAL =
INVENTORY VERIFIED and the signal input has been read in full.

[TABLE A with all columns as V-01, Load-shape verdict placeholder, STEP 1A GATE as V-01.]

**Step 1B — LOAD-SHAPE ANALYST: CLASSIFICATION**

[Identical to V-01 Step 1B — deferral prohibition, escape-route frame, STEP 1B GATE.]

**Steps 2A through 2H** — [Identical structure to V-01 Steps 2A–2H, including distributed
REGISTRY GAP reminders at 2A, 2C, 2E, 2G, 2H, phase entry/exit conditions, and all table
schemas.]

---

**ROLE 3 — AUDIT**

**Activation condition:** Step 2H is closed.

**Audit block — compliance verification**

**Field 1 — Tier-ID threading (C-13):** [Identical to V-01.]

**Field 2 — REGISTRY GAP enforcement (C-17/C-19):** [Identical to V-01.]

**Field 3 — Load-shape classification at registration (C-16):** [Identical to V-01.]

**Field 4 — Annotation dropout (C-40):** [Identical to V-01.]

**Field 5 — Role 1.5 handoff signal compliance (C-41 + C-42):** Role 1.5 HANDOFF SIGNAL =
INVENTORY VERIFIED was explicitly recorded before Step 1A opened. The activation condition
for Role 2 is INVENTORY VERIFIED — not FORMAT CONTRACT COMPLETE. The presence of FORMAT
CONTRACT COMPLETE in Role 1 does not satisfy this field; only the Role 1.5 HANDOFF SIGNAL =
INVENTORY VERIFIED record satisfies the Phase 1 activation requirement. State PASS or FAIL.
If FAIL, identify whether (a) Role 1.5 HANDOFF SIGNAL field is absent or unfilled, (b) the
field reads INVENTORY INCOMPLETE rather than INVENTORY VERIFIED, or (c) Step 1A opened
without the Role 1.5 handoff signal appearing before it.

**Per-section compliance status (C-18):** [Identical to V-01.]

---

## V-04

**Axes:** Phrasing register (primary) + Lifecycle emphasis (secondary)

**Hypothesis:** Maximum SHALL/SHALL NOT density at a named TWO-SIGNAL MANDATORY GATEWAY —
with each signal named as a separate normative obligation in its own numbered step — satisfies
C-43 by making conflation a named violation: an executor encountering SHALL NOT conflate these
signals cannot treat them as equivalent. C-44's inertia frame appears as a PROHIBITED bypass
declaration with SHALL NOT at every decision point. C-42 is satisfied by a SHALL-verify audit
field that names each gateway step and requires citing explicit CLEARED evidence — not
inferring compliance from body quality.

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

An executor SHALL verify, at the TWO-SIGNAL MANDATORY GATEWAY, that every site listed here
has its annotation present at its anchor location. Count: 7 precision sites.

[Identical 7-site table to V-01 Section A, with multi-adjacent note and non-conflation
count of 3.]

**Section B — Format contract**

An executor SHALL populate the following column definitions. Each definition SHALL include
a `*Violation type:*` annotation and a compliance failure condition. An executor SHALL NOT
omit either element at any precision site.

[Identical 7 column definitions to V-01 Section B — TABLE A `Limit`, TABLE A `Binding?`,
TABLE A `Failure mode`, TABLE B `Mechanism`, TABLE C `Error code or signal`, TABLE E `Type`,
TABLE F `Setting or API parameter`. Each with `*Violation type:*` and compliance failure
condition using normative language.]

**Section C — Annotation inventory**

This section SHALL declare the required annotation count before enumeration begins. **This
section declares 7 required annotations.** An executor verifying completeness SHALL count
rows; expected = 7. A count below 7 SHALL be treated as a completeness gap requiring Role 1
correction before Phase 1 opens.

| Annot-ID | Anchor site | Failure-mode label | Prohibited form (example) |
|----------|------------|-------------------|-----------------------------|
| Annot-01 | TABLE A — `Limit (number + unit)` | vague-label substitution | "limited" in place of "1,200 req/min" |
| Annot-02 | TABLE A — `Binding?` | assertion-without-causal-reason | Binding? = Y with no mechanism named |
| Annot-03 | TABLE A — `Failure mode` | insufficient-categorical-diversity | all rows: "timeout" |
| Annot-04 | TABLE B — `Mechanism` | generic-term substitution | "blocked" in place of "queue-fill" |
| Annot-05 | TABLE C — `Error code or signal` | plain-description substitution | "request fails" in place of "HTTP 429" |
| Annot-06 | TABLE E — `Type` | category-absence-undetectable | risk row with no Type value |
| Annot-07 | TABLE F — `Setting or API parameter` | category-of-action substitution | "add retry logic" in place of `connector.retryPolicy` |

This inventory is closed. An annotation not listed here SHALL NOT be treated as a contract
requirement. An annotation listed here that is absent from its anchor site SHALL be treated
as a FORMAT CONTRACT violation requiring correction before handoff.

PROHIBITED: annotation dropout at any anchor site listed in this inventory — *prevents
handoff-boundary gap: an annotation absent from its anchor site is detectable only by full
body scan; this PROHIBITED clause, co-located inside the annotation inventory, converts
dropout into a contract violation identifiable by Annot-ID lookup.* An executor SHALL verify
each Annot-ID anchor site at handoff.

**FORMAT CONTRACT COMPLETE** — Signal 1. An executor SHALL record this signal. An executor
SHALL NOT treat Signal 1 as evidence that Section C count is complete; Signal 1 confirms
section presence only.

---

**TWO-SIGNAL MANDATORY GATEWAY**

An executor SHALL complete this gateway before opening Step 1A. An executor SHALL NOT open
Step 1A until this gateway reaches CLEARED.

**Signal non-conflation requirement:**

This gateway requires two signals. An executor SHALL NOT conflate them:
1. **Signal 1 — FORMAT CONTRACT COMPLETE:** An executor SHALL confirm that Role 1 stated
   FORMAT CONTRACT COMPLETE. Signal 1 confirms that Sections A, B, and C are structurally
   present — it is a *section-presence* confirmation. An executor SHALL NOT treat Signal 1
   as evidence that Section C annotation count equals the declared count of 7.
2. **Signal 2 — INVENTORY VERIFIED:** An executor SHALL produce Signal 2 by completing the
   count verification procedure in this gateway. Signal 2 confirms that Section C row count
   = declared count of 7 — it is a *count-completeness* confirmation. An executor SHALL NOT
   activate Role 2 until Signal 2 is produced at this gateway.

**PROHIBITED — bypass via "looks complete" framing:** An executor encountering FORMAT
CONTRACT COMPLETE (Signal 1) SHALL NOT proceed directly to Role 2 on the basis that the
prompt appears complete or that the analysis scaffolding is in place. Signal 1 is a
section-presence signal; it does NOT guarantee Signal 2. A Section C with 6 of 7 annotations
stated FORMAT CONTRACT COMPLETE while Signal 2 would be withheld — the discrepancy is
detectable only after Role 2 produces output if Signal 2 is not verified. An executor SHALL
complete the count verification procedure before Role 2 activates.

**Count verification procedure:**

An executor SHALL execute the following steps in order. An executor SHALL NOT skip any step.

**Step G-1 — Signal 1 confirmation:**
An executor SHALL verify that FORMAT CONTRACT COMPLETE appears in Role 1.
Record: Signal 1 present = [Y/N]. An executor SHALL NOT proceed to Step G-2 if Signal 1
is absent.

**Step G-2 — Section C count:**
An executor SHALL count the Annot-ID rows in Section C.
Record: Actual count = [fill].

**Step G-3 — Count outcome (SHALL NOT proceed until resolved):**
- Actual count = 7: An executor SHALL record **INVENTORY VERIFIED** (Signal 2 produced).
  Proceed to Step G-4.
- Actual count < 7: An executor SHALL record **INVENTORY INCOMPLETE** (Signal 2 withheld).
  An executor SHALL return to Role 1. An executor SHALL complete Section C to 7 rows. An
  executor SHALL re-state FORMAT CONTRACT COMPLETE (Signal 1 re-recorded). An executor SHALL
  re-enter this gateway from Step G-1. An executor SHALL NOT proceed to Step G-4 or Step 1A.

**Step G-4 — Gateway status record:**

**GATEWAY STATUS:**
- Signal 1 (FORMAT CONTRACT COMPLETE): [ CONFIRMED / NOT YET ]
- Signal 2 (INVENTORY VERIFIED): [ CONFIRMED / WITHHELD ]
- Role 2 activation: [ CLEARED / BLOCKED ]

An executor SHALL fill all three fields. An executor SHALL NOT open Step 1A if Role 2
activation = BLOCKED or any field is unfilled.

---

**ROLE 2 — DOMAIN EXPERT**

An executor SHALL NOT enter Role 2 until GATEWAY STATUS Role 2 activation = CLEARED.

**REGISTRY GAP PROHIBITION — Failure 5 prevention (C-17):** Tiers discovered during Step 2
are scope violations. PROHIBITED: assigning a new T-NN during Step 2. An executor SHALL
return to TABLE A, register the tier, and SHALL restart from the point of discovery. This
prohibition SHALL be restated at each Step 2 section where mid-phase discovery could occur.

**Step 1A — VOLUME ANALYST: TIER IDENTIFICATION AND LIMITS**

**PHASE ENTRY CONDITION:** Step 1A SHALL be entered only after GATEWAY STATUS Role 2
activation = CLEARED. An executor SHALL NOT enter Step 1A if GATEWAY STATUS is BLOCKED or
unfilled.

[TABLE A with all columns as V-01. STEP 1A GATE as V-01. Step 1B with deferral prohibition
and escape-route frame as V-01. Steps 2A–2H with distributed REGISTRY GAP reminders and
phase entry/exit conditions as V-01. All table schemas identical to V-01.]

---

**ROLE 3 — AUDIT**

**Audit block — compliance verification**

**Field 1 — Tier-ID threading (C-13):** [Identical to V-01.]

**Field 2 — REGISTRY GAP enforcement (C-17/C-19):** [Identical to V-01.]

**Field 3 — Load-shape classification at registration (C-16):** [Identical to V-01.]

**Field 4 — Annotation dropout (C-40):** [Identical to V-01.]

**Field 5 — TWO-SIGNAL MANDATORY GATEWAY compliance (C-41 + C-42):** An executor SHALL
verify each of the following. An executor SHALL NOT infer gateway compliance from body
quality — explicit records from the gateway steps are required:
(a) Step G-1: Signal 1 (FORMAT CONTRACT COMPLETE) was confirmed — cite the Step G-1 record.
(b) Step G-2: Section C Actual count was filled — cite the recorded value.
(c) Step G-3: Signal 2 (INVENTORY VERIFIED) was produced — cite the Step G-3 record.
(d) Step G-4: GATEWAY STATUS Role 2 activation = CLEARED was explicitly recorded before
Step 1A — cite the GATEWAY STATUS field.
State PASS if all four are present. State FAIL with the specific step (G-1 through G-4)
where the required record is absent.

**Per-section compliance status (C-18):** [Identical to V-01.]

---

## V-05

**Axes:** Role sequence (primary) + Output format (secondary) + Inertia framing (secondary)

**Hypothesis:** Three combined axes produce the most structurally reinforced C-42 + C-43 +
C-44 coverage:
(1) Role sequence — a role activation chain table forces the reader to trace both handoff
signals; a missing signal entry is a visible structural gap in the chain.
(2) Output format — a signal distinction table with "Confirms" and "Does NOT confirm"
columns makes the section-presence vs. count-completeness distinction a column-readable fact;
Role 1.5's verification table requires a filled Verdict cell; blank cells are detectable
compliance gaps.
(3) Inertia framing — the "looks complete" bypass is named as a failure mode in a dedicated
section inside Role 1.5, defeated by a structural proof parallel to C-26, and requires an
explicit inertia-frame rejection field to be filled before the verification table runs.

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
| Role 1.5 — INVENTORY VERIFIER | FORMAT CONTRACT COMPLETE | INVENTORY VERIFIED or INVENTORY INCOMPLETE | Count check: Section C row count = 7; inertia-frame rejection |
| Role 2 — DOMAIN EXPERT | INVENTORY VERIFIED | Step 2H closed | All analysis (Steps 1A–2H) |
| Role 3 — AUDIT | Step 2H closed | Audit complete | Compliance verification |

An executor SHALL NOT activate a role until its activation signal is present. An executor
seeing INVENTORY INCOMPLETE in the Role 1.5 handoff column SHALL return to Role 1 — Role 2
does not activate on INVENTORY INCOMPLETE.

---

**ROLE 1 — FORMAT CONTRACT**

**Section A — Precision-site inventory**

[Identical to V-01 Section A — 7-site table with Site-IDs S-01 through S-07, multi-adjacent
note for S-01/S-02/S-03, non-conflation count of 3.]

**Section B — Format contract**

[Identical to V-01 Section B — 7 column definitions, each with `*Violation type:*` annotation
and compliance failure condition per C-27.]

**Section C — Annotation inventory**

This section declares **7 required annotations**. Role 1.5 verifies this count before Role 2
activates.

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

**FORMAT CONTRACT COMPLETE** — Role 1.5 activation signal.

---

**ROLE 1.5 — INVENTORY VERIFIER**

**Activation signal received:** FORMAT CONTRACT COMPLETE

**Signal distinction table:**

| Signal ID | Signal name | Produced by | Confirms | Does NOT confirm |
|-----------|------------|-------------|----------|-----------------|
| SIG-01 | FORMAT CONTRACT COMPLETE | Role 1 | Sections A, B, C are structurally present | That Section C annotation count = declared count of 7 |
| SIG-02 | INVENTORY VERIFIED | Role 1.5 | Section C Annot-ID row count = declared count of 7 | — |

An executor SHALL treat SIG-01 and SIG-02 as structurally distinct. SIG-01 satisfies Role
1's section-presence requirement. SIG-02 satisfies the count-completeness requirement. An
executor SHALL NOT treat the presence of SIG-01 as evidence that SIG-02 is satisfied.

**Inertia-frame rejection — the "looks complete" bypass failure mode:**

**Named failure mode:** "Looks complete / just start" — SIG-01 (FORMAT CONTRACT COMPLETE)
has been stated and the analysis tables are scaffolded; Role 2 appears ready to activate.

**Structural proof of rejection:** This failure mode is self-defeating. SIG-01 is a
*section-presence* signal — it confirms that Role 1 produced Sections A, B, and C as
structural elements. SIG-01 does NOT verify that Section C contains the declared count of 7
annotations. A Section C with 6 of 7 annotations satisfies SIG-01 (sections present) while
failing the count declared in Section C's header. Role 1.5 exists precisely to close this
gap: it is the only role with single-responsibility for count verification, and its handoff
signal (SIG-02) is the activation condition for Role 2. Bypassing Role 1.5 converts the
Section C count from a verifiable gate into an unverified assertion — a count discrepancy is
detectable only after Role 2 has produced output, not before. This proof is parallel to C-26
at Step 1B: just as Step 1B cannot be deferred because Step 2G is structurally dependent on
Load-shape verdicts that only Step 1B produces, Role 2 cannot bypass Role 1.5 because Role
2's annotation contract depends on a count-verified inventory that only Role 1.5 certifies.

**Inertia-frame rejection field:** An executor SHALL fill this field before proceeding to the
verification table: [ BYPASS ATTEMPT IDENTIFIED AND REJECTED / NO BYPASS ATTEMPT DETECTED ]

**Verification table:**

| Check | Expected | Actual | Verdict |
|-------|----------|--------|---------|
| SIG-01 (FORMAT CONTRACT COMPLETE) recorded in Role 1 | Present | [Y/N] | PASS if Y |
| Section C Annot-ID row count | 7 | [count] | PASS if actual = 7; FAIL if actual < 7 |

**Outcome:**
- All checks PASS → state **INVENTORY VERIFIED** (SIG-02 produced) → Role 2 activates.
- Any check FAIL → state **INVENTORY INCOMPLETE** (SIG-02 withheld) → return to Role 1.
  Correct the gap. Re-state FORMAT CONTRACT COMPLETE (SIG-01 re-recorded). Re-enter Role 1.5
  from the top.

**HANDOFF SIGNAL: [ INVENTORY VERIFIED / INVENTORY INCOMPLETE ]** — fill before Role 2.

---

**ROLE 2 — DOMAIN EXPERT**

**Activation signal required:** INVENTORY VERIFIED (SIG-02, from Role 1.5)

An executor SHALL confirm the Role 1.5 HANDOFF SIGNAL = INVENTORY VERIFIED before opening
Step 1A. An executor SHALL NOT open Step 1A if HANDOFF SIGNAL = INVENTORY INCOMPLETE or if
the HANDOFF SIGNAL field is unfilled.

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
self-defeating: load-shape classification requires the registered `Limit` value available now
at Step 1B, and Step 2G depends on per-tier Load-shape verdicts to produce meaningful
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

**PHASE ENTRY CONDITION:** After Step 2C. All TABLE A tiers; ordered by business risk.

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
| F-5 | C-41 + C-42 gate compliance | Role 1.5 HANDOFF SIGNAL = INVENTORY VERIFIED (SIG-02) explicitly recorded before Step 1A; SIG-01 (FORMAT CONTRACT COMPLETE) and SIG-02 (INVENTORY VERIFIED) appear as structurally distinct entries — SIG-01 in Role 1, SIG-02 in Role 1.5; gate compliance verified by these records, not inferred from body quality | PASS / FAIL + identify which signal record is absent |

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
