# flow-throttle Variate — Round 18

**Date:** 2026-03-16
**Rubric:** v18 (C-01–C-48, N_essential=5, N_recommended=3, N_aspirational=40)
**Max composite:** 290 | **Baseline ceiling:** R17 best (270/270 under v17, 270/290 under v18)

---

## State Analysis: What R17 Has vs. What R18 Must Add

**R17 coverage under v18 (assessed):**
- C-01 through C-44: all pass in all R17 variants (270/270 under v17).
- C-45: PASS in V-02 only. V-02's Table 1 signal distinction register has both "Confirms" and
  "Does NOT confirm" columns. V-01, V-03, V-04, V-05 express signal non-conflation in prose or
  per-signal role text — limitation inspection requires prose parsing, not column scan.
- C-46: PASS in V-05 only. V-05's role activation chain table appears at the prompt header
  before any role body, showing SIG-01 and SIG-02 as separate Handoff cells. V-01 through V-04
  embed the two-signal chain inside role bodies — a reader must enter Role 1.5 or the checkpoint
  to discover both signals.
- C-47: PASS in V-02 only. V-02's Table 2 is a typed bypass-attempt rejection table with named
  columns (Bypass attempt / Attempt type / Structural reason). V-01, V-03, V-04, V-05 defeat the
  bypass in prose or a named section — not a scannable register row.
- C-48: PASS in V-05 only. V-05's inertia-frame rejection field appears before the verification
  table with an explicit SHALL FILL instruction. V-01 through V-04 either embed bypass rejection
  in prose or in a section that does not gate the verification table — the table is reachable
  without filling a prerequisite field.

**R17 gaps by variant under v18:**

| Variant | C-45 | C-46 | C-47 | C-48 | Score under v18 |
|---------|------|------|------|------|----------------|
| V-01 | FAIL | FAIL | FAIL | FAIL | 270/290 |
| V-02 | PASS | FAIL | PASS | FAIL | 280/290 |
| V-03 | FAIL | FAIL | FAIL | FAIL | 270/290 |
| V-04 | FAIL | FAIL | FAIL | FAIL | 270/290 |
| V-05 | PASS | PASS | FAIL | PASS | 285/290 |

**R18 task:** All 5 variations must achieve 290/290. Every variant must carry C-45, C-46, C-47,
and C-48 simultaneously. Variation axes determine HOW each criterion is expressed — not WHETHER
it is present.

**Round 18 variation map:**

| Variation | Axes | C-45 mechanism | C-46 mechanism | C-47 mechanism | C-48 mechanism | Predicted |
|-----------|------|----------------|----------------|----------------|----------------|-----------|
| V-01 | Output format (single) | 5-column signal distinction register; "Does NOT confirm" column makes each signal's limit a cell value | Dense 4-role activation chain table at header before any section body | 3-column bypass-attempt rejection table (Attempt / Type / Structural reason) adjacent to signal distinction register | BYPASS GATE CONDITION fill field (two options) before count verification table; SHALL NOT proceed until filled | 290/290 |
| V-02 | Role sequence (single) | Signal distinction table in Role 1.5 with "Does NOT confirm" column; non-conflation statement references column by name | Role activation chain table at header; SIG-01 and SIG-02 as distinct Handoff cells before Role 1 body begins | Separate bypass-attempt rejection register (3 columns) in Role 1.5 inertia-frame section | INERTIA-FRAME REJECTION FIELD (two options) required before Role 1.5 verification table; field placement makes bypass rejection a structural gate | 290/290 |
| V-03 | Lifecycle emphasis (single) | Phase 0 signal specification table with "Does NOT confirm" column; limitation column appears at lifecycle phase entry | Lifecycle stage overview table at header; Phase column + Gate signal column shows SIG-01 and SIG-02 in distinct rows before any phase body | Phase 0.5 bypass defeat record — typed register (Attempt / Stage type / Gate reason) at lifecycle boundary | PHASE GATE FIELD (two options) that must be filled before Phase 1 count check opens; fills a named gate slot in the lifecycle sequence | 290/290 |
| V-04 | Phrasing register + inertia framing (combined) | SHALL-contract signal table; "DOES NOT CONFIRM" column header in caps; SHALL-NOT-treat statement references column header directly | SHALL-activation role sequence table at header; each Handoff cell includes SHALL-NOT-activate consequence | PROHIBITED FRAMING REGISTER — typed table; each row states SHALL NOT PROCEED and names the structural reason the bypass is prohibited | MANDATORY BYPASS DECLARATION — named fill field with two options; SHALL FILL before activation sequence opens; activation sequence cannot begin without field value | 290/290 |
| V-05 | Role sequence + output format + inertia framing (combined) | Signal distinction table in Role 1.5 with "Does NOT confirm" column; non-conflation statement quotes the "Does NOT confirm" cell value and directs column scan | Role activation chain table at header with Signal chain column; SIG-01 and SIG-02 appear as distinct cells in Handoff column; table is the first artifact before any role body | Named BYPASS DEFEAT REGISTER in Role 1.5 with 3 columns; bypass defeat recorded as auditable row; register is extensible by row for additional bypass variants | BYPASS REJECTION FIELD (two options) immediately before verification table; SHALL FILL instruction; verification table is presented as unreachable until field is filled | 290/290 |

---

## V-01

**Axis:** Output format (single-axis)

**Hypothesis:** A table-first format where every structural requirement — including C-45, C-46,
C-47, and C-48 — is expressed as a named, typed table or fill artifact makes all four new
criteria inspectable by column or row scan without prose parsing. The role activation chain
(C-46) is a typed 4-role table before any role body. The signal distinction register (C-45) is a
5-column table with "Does NOT confirm" as an explicit column header. The bypass rejection (C-47)
is a 3-column typed register adjacent to the signal distinction table. The bypass gate condition
(C-48) is a named fill field with two options that must be resolved before the count table is
reached — its placement makes the count table structurally unavailable until the field is filled.
Field 5 in Role 3 verifies all four criteria by table-citation evidence.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
the rate-limited system described in the signal. Treat the stated request volume as 1x nominal;
also analyze at 2x and 5x.

The tables below are the primary output — every cell SHALL be filled. Produce sections in the
order shown. This prompt uses a four-role activation sequence with named handoff signals.

**Role activation chain:**

| Role | Activation condition | Handoff signal | Responsibility |
|------|---------------------|----------------|----------------|
| Role 1 — FORMAT CONTRACT | None (runs first) | SIG-01: FORMAT CONTRACT COMPLETE | Precision-site inventory, format contract, annotation inventory |
| Role 1.5 — INVENTORY VERIFIER | SIG-01 present | SIG-02: INVENTORY VERIFIED or INVENTORY INCOMPLETE | Signal distinction table, bypass rejection register, bypass gate field, count verification |
| Role 2 — DOMAIN EXPERT | SIG-02 = INVENTORY VERIFIED | Step 2H closed | All analysis: Steps 1A through 2H |
| Role 3 — AUDIT | Step 2H closed | Audit complete | Compliance verification: Fields 1–5 |

An executor SHALL NOT activate a role until its activation condition is met. SIG-01 and SIG-02
are structurally distinct (see Role 1.5 signal distinction register). An executor SHALL NOT
treat SIG-01 as the activation condition for Role 2.

---

**ROLE 1 — FORMAT CONTRACT**

**Section A — Precision-site inventory**

This section inventories every location in this prompt where a column definition carries a
violation-type annotation. An executor SHALL verify, at Role 1.5, that every listed site is
present in Section C with its annotation at the anchor site. Count: 7 precision sites across
5 tables.

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
assertion-without-causal-reason, and insufficient-categorical-diversity as variants of a single
"incomplete entry" failure. Each is a distinct violation with a distinct pass condition.

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
  imprecision — non-overlapping failure modes.

**TABLE A — `Failure mode` (S-03, adjacent-2):**
Name the observable failure type at saturation. At least two distinct values SHALL appear
across all TABLE A rows.
- *Violation type: insufficient-categorical-diversity — fewer than two distinct failure mode
  values across all TABLE A rows.*
- Compliance failure condition (C-27/S-03): A TABLE A where all `Failure mode` entries share
  the same value fails this column's diversity requirement.

**TABLE B — `Mechanism` (S-04, primary):**
Name the specific throttle propagation mechanism from the permitted set: queue-fill,
connection-hold, retry-amplification, dependency-stall, timeout-cascade.
- *Violation type: generic-term substitution — "blocked", "throttled", or "slowed" in place of
  a named mechanism from the permitted set.*
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
Role 1.5 verifies this count before Role 2 activates.

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

**FORMAT CONTRACT COMPLETE** — SIG-01 produced. Role 1.5 activation condition satisfied.

---

**ROLE 1.5 — INVENTORY VERIFIER**

**Activation condition:** SIG-01 (FORMAT CONTRACT COMPLETE) present.

**Signal distinction register:**

| Signal ID | Signal name | Produced by | Confirms | Does NOT confirm |
|-----------|------------|-------------|----------|-----------------||
| SIG-01 | FORMAT CONTRACT COMPLETE | Role 1 | Sections A, B, C are structurally present | That Section C annotation count = declared count of 7 |
| SIG-02 | INVENTORY VERIFIED | Role 1.5 (this role) | Section C Annot-ID row count = declared count of 7 | That Sections A, B, C are structurally present (verified by SIG-01 only) |

An executor SHALL NOT treat SIG-01 as evidence that SIG-02 is satisfied. The "Does NOT
confirm" column value for SIG-01 makes this limitation a column-readable fact without requiring
prose parsing: SIG-01's "Does NOT confirm" cell states count non-verification explicitly.

**Bypass-attempt rejection register:**

| Bypass attempt | Attempt type | Structural reason for rejection |
|----------------|-------------|---------------------------------|
| Open Role 2 after SIG-01 (FORMAT CONTRACT COMPLETE) without completing the count verification table | "Looks complete" — SIG-01 stated, analysis tables scaffolded, prompt appears ready | SIG-01 confirms section presence only (see "Does NOT confirm" column above). A Section C with 6 of 7 annotations satisfies SIG-01 while failing SIG-02 — the discrepancy is detectable only after Role 2 produces output if the count table is skipped. Role 1.5 has single-responsibility for count verification; its handoff signal SIG-02 is the activation condition for Role 2. Bypassing Role 1.5 converts Section C count from a verifiable gate into an unverified assertion. |

**BYPASS GATE CONDITION — fill this field before proceeding to the count verification table
below. An executor SHALL NOT open the count verification table until this field is filled:**

[ BYPASS ATTEMPT IDENTIFIED AND REJECTED / NO BYPASS ATTEMPT DETECTED ]

**Count verification table:**

| Check | Expected | Actual | Verdict |
|-------|----------|--------|---------|
| SIG-01 (FORMAT CONTRACT COMPLETE) recorded in Role 1 | Present | [Y/N] | PROCEED if Y |
| Section C Annot-ID row count | 7 | [count rows] | PROCEED if actual = 7; RETURN TO ROLE 1 if < 7 |

**Outcome:**
- All rows PROCEED → state **INVENTORY VERIFIED** (SIG-02 produced). Role 2 activates.
- Any row RETURN TO ROLE 1 → state **INVENTORY INCOMPLETE** (SIG-02 withheld). Complete the
  gap. Re-state FORMAT CONTRACT COMPLETE (SIG-01 re-recorded). Re-enter Role 1.5 from the top.

**HANDOFF SIGNAL: [ INVENTORY VERIFIED / INVENTORY INCOMPLETE ]** — fill before Role 2.

---

**ROLE 2 — DOMAIN EXPERT**

**Activation condition:** SIG-02 = INVENTORY VERIFIED. An executor SHALL NOT open Step 1A if
Role 1.5 HANDOFF SIGNAL is not INVENTORY VERIFIED.

**REGISTRY GAP PROHIBITION — Failure 5 prevention (C-17):** Tiers discovered during Step 2
are scope violations — evidence that the enumeration phase was incomplete. PROHIBITED: assigning
a new T-NN during Step 2 as a fill-in step. An executor SHALL return to TABLE A, register the
tier with all columns filled, and SHALL restart from the point of discovery. This prohibition
SHALL be restated at each Step 2 section where mid-phase discovery could occur.

---

**Step 1A — VOLUME ANALYST: TIER IDENTIFICATION AND LIMITS**

**PHASE ENTRY CONDITION:** Step 1A SHALL be entered after SIG-02 = INVENTORY VERIFIED and the
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
referenced in burst path analysis not in TABLE A are scope violations. Return to TABLE A.

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
introduced during cascade trace not in TABLE A are scope violations. Return to TABLE A.

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
referenced in mitigation entries not in TABLE A are scope violations. Return to TABLE A.

| MR-ID | Source T-NN | Gap type | Component | Setting or API parameter | Change | Expected outcome |
|-------|-------------|----------|-----------|--------------------------|--------|-----------------|
| MR-01 |             |          |           |                          |        |                 |
| MR-02 |             |          |           |                          |        |                 |

---

**ROLE 3 — AUDIT**

**Audit block — compliance verification**

**Field 1 — Tier-ID threading (C-13):** Every T-NN from TABLE A appears verbatim in all
downstream sections (TABLE B `From`, TABLE C rows, TABLE D `Tier-IDs involved`, TABLE E
`Tier-ID`, Step 2E cascade trace, TABLE F `Source T-NN`). State PASS or list each discrepancy
as: T-NN | section | issue.

**Field 2 — REGISTRY GAP enforcement (C-17/C-19):** No new T-NN was assigned during Steps
2A–2H. State PASS or list violations as: step | T-NN introduced | impact.

**Field 3 — Load-shape classification at registration (C-16):** Every TABLE A row has a
non-placeholder `Load-shape verdict` assigned at Step 1B, not in Step 2G. State PASS or list
deferred rows.

**Field 4 — Annotation dropout (C-40):** Every Annot-01 through Annot-07 is present at its
anchor site. State PASS or list: Annot-ID | anchor site | status.

**Field 5 — Signal chain and v18 criteria compliance (C-41 + C-42 + C-45 + C-46 + C-47 + C-48):**
Verify each by citing evidence from the body:
(a) C-46: Role activation chain table is present at the prompt header before any role body
    begins — cite the table title and the two Handoff cells showing SIG-01 and SIG-02.
(b) C-45: Signal distinction register is present with a "Does NOT confirm" column — cite the
    SIG-01 "Does NOT confirm" cell value verbatim.
(c) C-47: Bypass-attempt rejection register contains at least one row with Bypass attempt,
    Attempt type, and Structural reason columns — cite the Attempt type cell value.
(d) C-48: BYPASS GATE CONDITION field was filled before the count verification table — cite
    the filled value.
(e) C-41 + C-42: SIG-02 (INVENTORY VERIFIED) was recorded as Role 1.5 HANDOFF SIGNAL before
    Step 1A opened — cite the HANDOFF SIGNAL value.
State PASS for each item or FAIL with the specific missing artifact.

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

---

## V-02

**Axis:** Role sequence (single-axis)

**Hypothesis:** A dedicated Role 1.5 architecture creates the cleanest structural separation for
all four new v18 criteria: (1) C-46 — the role activation chain at the header shows SIG-01 in
Role 1's Handoff cell and SIG-02 in Role 1.5's Handoff cell as structurally distinct entries,
making the two-signal design visible before any role body begins; (2) C-45 — Role 1.5's signal
distinction table gains a "Does NOT confirm" column, with the non-conflation statement
referencing the column by name; (3) C-47 — a separate bypass-attempt rejection register (3
columns) in Role 1.5's inertia-frame section records the bypass defeat as an auditable row
rather than prose; (4) C-48 — the INERTIA-FRAME REJECTION FIELD (two options) appears
immediately before the verification table, making bypass rejection a structural gate: the field
must be filled before the table opens. Field 5 in Role 3 verifies all four criteria by explicit
record-citation.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
the rate-limited system described in the signal. Treat the stated request volume as 1x nominal;
also analyze at 2x and 5x.

The tables below are the primary output — every cell SHALL be filled. Produce sections in the
order shown. This prompt uses a four-role sequence with explicit handoff signals.

**Role activation chain:**

| Role | Activation signal | Handoff signal | Responsibility |
|------|------------------|----------------|----------------|
| Role 1 — FORMAT CONTRACT | None (runs first) | SIG-01: FORMAT CONTRACT COMPLETE | Precision-site inventory (S-01–S-07), format contract, annotation inventory (7 annotations) |
| Role 1.5 — INVENTORY VERIFIER | SIG-01: FORMAT CONTRACT COMPLETE | SIG-02: INVENTORY VERIFIED or INVENTORY INCOMPLETE | Signal distinction table (C-45), bypass-attempt rejection register (C-47), inertia-frame rejection field (C-48), count verification |
| Role 2 — DOMAIN EXPERT | SIG-02: INVENTORY VERIFIED | Step 2H closed | Steps 1A through 2H — all analysis output |
| Role 3 — AUDIT | Step 2H closed | Audit complete | Fields 1–5 compliance verification |

An executor SHALL NOT activate a role until its named activation signal is present. An executor
seeing SIG-02 = INVENTORY INCOMPLETE SHALL return to Role 1 — Role 2 does not activate on
INVENTORY INCOMPLETE. An executor SHALL NOT treat SIG-01 as sufficient to activate Role 2.

---

**ROLE 1 — FORMAT CONTRACT**

**Section A — Precision-site inventory**

[Identical to V-01 Section A — 7-site table with Site-IDs S-01 through S-07, multi-adjacent
note for S-01/S-02/S-03 group (3 non-overlapping violation types), non-conflation count: 3.]

**Section B — Format contract**

[Identical to V-01 Section B — 7 column definitions for TABLE A `Limit`, TABLE A `Binding?`,
TABLE A `Failure mode`, TABLE B `Mechanism`, TABLE C `Error code or signal`, TABLE E `Type`,
TABLE F `Setting or API parameter`. Each definition includes `*Violation type:*` annotation
and compliance failure condition per C-27.]

**Section C — Annotation inventory**

This section declares **7 required annotations**. Role 1.5 verifies this count before Role 2
activates.

[Identical to V-01 Section C — 7-row table Annot-01 through Annot-07. PROHIBITED annotation
dropout clause physically co-located inside the inventory.]

**FORMAT CONTRACT COMPLETE** — SIG-01 produced. Role 1.5 activation signal issued.

---

**ROLE 1.5 — INVENTORY VERIFIER**

**Activation signal received:** SIG-01 (FORMAT CONTRACT COMPLETE)

**Signal distinction table:**

| Signal ID | Signal name | Produced by | Confirms | Does NOT confirm |
|-----------|------------|-------------|----------|-----------------||
| SIG-01 | FORMAT CONTRACT COMPLETE | Role 1 | Sections A, B, C are structurally present | That Section C annotation count = declared count of 7 |
| SIG-02 | INVENTORY VERIFIED | Role 1.5 (this role) | Section C Annot-ID row count = declared count of 7 | That Sections A, B, C are structurally present |

An executor SHALL NOT treat SIG-01 as evidence that SIG-02 is satisfied. The "Does NOT confirm"
column makes each signal's limitation column-readable: an executor can verify SIG-01's
limitation by scanning the "Does NOT confirm" cell without parsing surrounding prose. SIG-01
confirms section presence; only SIG-02 confirms count completeness.

**Inertia-frame rejection section:**

**Named failure mode:** "Looks complete / just start" — SIG-01 (FORMAT CONTRACT COMPLETE) has
been stated and analysis tables are scaffolded. Role 2 appears ready to activate.

**Bypass-attempt rejection register:**

| Bypass attempt | Attempt type | Structural reason for rejection |
|----------------|-------------|---------------------------------|
| Activate Role 2 on SIG-01 (FORMAT CONTRACT COMPLETE) without completing the inertia-frame rejection field and count verification table | "Looks complete" — SIG-01 stated, analysis tables scaffolded, prompt appears structurally ready | SIG-01 is a section-presence signal (see "Does NOT confirm" column above): it confirms Sections A, B, C exist but does NOT confirm that Section C contains the declared count of 7 annotations. A Section C with 6 of 7 annotations satisfies SIG-01 while failing SIG-02. The discrepancy is detectable only after Role 2 produces output. Role 1.5 has single-responsibility for count verification; its handoff signal SIG-02 is the sole activation condition for Role 2. Bypassing this role converts Section C count from a verifiable gate into an unverified assertion. |

**INERTIA-FRAME REJECTION FIELD — An executor SHALL fill this field before proceeding to the
verification table. The verification table is not available until this field is filled:**

[ BYPASS ATTEMPT IDENTIFIED AND REJECTED / NO BYPASS ATTEMPT DETECTED ]

**Verification table:**

| Check | Expected | Actual | Verdict |
|-------|----------|--------|---------|
| SIG-01 (FORMAT CONTRACT COMPLETE) recorded in Role 1 | Present | [Y/N] | PASS if Y |
| Section C Annot-ID row count | 7 | [count rows] | PASS if actual = 7; FAIL if actual < 7 |

**Outcome:**
- All PASS → state **INVENTORY VERIFIED** (SIG-02 produced) → Role 2 activates.
- Any FAIL → state **INVENTORY INCOMPLETE** (SIG-02 withheld) → return to Role 1. Correct the
  gap. Re-state FORMAT CONTRACT COMPLETE (SIG-01 re-issued). Re-enter Role 1.5 from the top.

**HANDOFF SIGNAL: [ INVENTORY VERIFIED / INVENTORY INCOMPLETE ]** — fill before Role 2.

---

**ROLE 2 — DOMAIN EXPERT**

**Activation signal required:** SIG-02 (INVENTORY VERIFIED, from Role 1.5). An executor SHALL
confirm HANDOFF SIGNAL = INVENTORY VERIFIED before opening Step 1A. An executor SHALL NOT open
Step 1A if HANDOFF SIGNAL = INVENTORY INCOMPLETE or if the HANDOFF SIGNAL field is unfilled.

**REGISTRY GAP PROHIBITION — Failure 5 prevention (C-17):** Tiers discovered during Step 2
are scope violations. PROHIBITED: assigning a new T-NN during Step 2. Return to TABLE A,
register the tier, and restart from the point of discovery. This prohibition SHALL be restated
at each Step 2 section where mid-phase discovery could occur.

**Step 1A — VOLUME ANALYST: TIER IDENTIFICATION AND LIMITS**

**PHASE ENTRY CONDITION:** Step 1A SHALL be entered only after HANDOFF SIGNAL = INVENTORY
VERIFIED.

[TABLE A with all columns as V-01. `Load-shape verdict` placeholder for Step 1B. STEP 1A GATE
as V-01 — all T-NN rows populated, no vague `Limit` labels, `Binding?` with causal mechanisms,
at least 2 distinct `Failure mode` values.]

**Step 1B — LOAD-SHAPE ANALYST: CLASSIFICATION**

**PHASE ENTRY CONDITION:** Step 1B SHALL be entered only after STEP 1A GATE is cleared.

[Identical to V-01 Step 1B — CLASSIFICATION REQUIRED AT STEP 1B, deferral prohibition,
escape-route frame ("STATUS tracks volume thresholds" framing self-defeating explanation),
STEP 1B GATE requiring SHAPE-NEUTRAL or SHAPE-SENSITIVE with numeric differential and
mechanism for every row.]

**Steps 2A through 2H** — [Identical structure to V-01 Steps 2A–2H, including: Step 2A
REGISTRY GAP reminder + TABLE B (min 2 hops, permitted mechanism set); Step 2B TABLE C (one
row per Tier-ID); Step 2C TABLE D (at least one row, named controls if no gap); Step 2D
TABLE E (all tiers by risk, reference visibility + recovery for Rank 1); Step 2E cascade
scenario (min three tiers, explicit causal links); Step 2F Retry-After assessment (retry storm
vs. quota exhaustion); Step 2G load shape comparison (uniform vs. burst, at least one numeric
status difference at identical total count); Step 2H TABLE F mitigation registry. Each Step 2
section includes a standing REGISTRY GAP PROHIBITED reminder and phase entry condition.]

---

**ROLE 3 — AUDIT**

**Activation signal:** Step 2H closed

**Field 1 — Tier-ID threading (C-13):** [Identical to V-01 Field 1.]

**Field 2 — REGISTRY GAP enforcement (C-17/C-19):** [Identical to V-01 Field 2.]

**Field 3 — Load-shape classification at registration (C-16):** [Identical to V-01 Field 3.]

**Field 4 — Annotation dropout (C-40):** [Identical to V-01 Field 4.]

**Field 5 — Role 1.5 signal chain compliance (C-41 + C-42 + C-45 + C-46 + C-47 + C-48):**

An executor SHALL verify each item by citing explicit evidence from the body:

| Item | Criterion | Evidence required | Status |
|------|-----------|-------------------|--------|
| (a) | C-46 | Role activation chain table at prompt header shows SIG-01 in Role 1 Handoff cell and SIG-02 in Role 1.5 Handoff cell as distinct entries before any role body — cite the table and both Handoff cell values | PASS / FAIL |
| (b) | C-45 | Signal distinction table in Role 1.5 has a "Does NOT confirm" column — cite the SIG-01 "Does NOT confirm" cell value verbatim | PASS / FAIL |
| (c) | C-47 | Bypass-attempt rejection register in Role 1.5 contains at least one row with Bypass attempt, Attempt type, and Structural reason columns — cite the Attempt type cell value | PASS / FAIL |
| (d) | C-48 | INERTIA-FRAME REJECTION FIELD was filled before the verification table — cite the filled value | PASS / FAIL |
| (e) | C-41 + C-42 | HANDOFF SIGNAL = INVENTORY VERIFIED (SIG-02) recorded in Role 1.5 before Step 1A opened — cite the HANDOFF SIGNAL value | PASS / FAIL |

State overall PASS if all rows = PASS. State FAIL with the row identifying which item failed and
what evidence is absent. Gate compliance is verified by evidence in the body, not inferred from
output quality.

**Per-section compliance status (C-18):** [Identical to V-01 per-section table.]

---

## V-03

**Axis:** Lifecycle emphasis (single-axis)

**Hypothesis:** A lifecycle-stage framing treats C-45 through C-48 as named phases in the
output lifecycle rather than role-internal artifacts: the lifecycle stage overview table at the
header (C-46) shows SIG-01 and SIG-02 as distinct Gate signal entries in a Phase column
sequence, making the two-signal design visible as a lifecycle property before any phase body
begins. Phase 0's signal specification table (C-45) shows each signal's limitation as a "Does
NOT confirm" column value at the phase's entry point. Phase 0.5 is a dedicated bypass defeat
phase (C-47) — its output is a typed bypass defeat record with Attempt / Stage type / Gate
reason columns, making the defeat a lifecycle artifact rather than embedded prose. The PHASE
GATE FIELD (C-48) is a named gate slot in the lifecycle sequence that must be filled to clear
Phase 0.5 and allow Phase 1 (count check) to open. Field 5 verifies the full lifecycle gate
chain by phase citation.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
the rate-limited system described in the signal. Treat the stated request volume as 1x nominal;
also analyze at 2x and 5x.

The tables below are the primary output — every cell SHALL be filled. Produce sections in the
order shown. This prompt uses a lifecycle stage sequence with named gate signals.

**Lifecycle stage overview:**

| Phase | Stage name | Entry gate | Gate signal | Responsibility |
|-------|-----------|------------|-------------|----------------|
| Phase 0 | FORMAT CONTRACT | None | SIG-01: FORMAT CONTRACT COMPLETE | Precision-site inventory, format contract, annotation inventory |
| Phase 0.5 | BYPASS DEFEAT RECORD | SIG-01 present | See Phase 0.5 output | Signal specification (C-45), bypass defeat record (C-47), phase gate field (C-48) |
| Phase 1 | COUNT VERIFICATION | Phase 0.5 PHASE GATE FIELD filled | SIG-02: INVENTORY VERIFIED or INVENTORY INCOMPLETE | Section C annotation count check |
| Phase 2 | ANALYSIS | SIG-02 = INVENTORY VERIFIED | Step 2H closed | Steps 1A through 2H |
| Phase 3 | AUDIT | Step 2H closed | Audit complete | Compliance verification Fields 1–5 |

SIG-01 and SIG-02 are distinct gate signals — they appear in separate Phase rows. An executor
SHALL NOT treat SIG-01 as the entry gate for Phase 2. Phase 2 entry requires SIG-02 from
Phase 1.

---

**PHASE 0 — FORMAT CONTRACT**

**Section A — Precision-site inventory**

[Identical to V-01 Section A — 7-site table S-01 through S-07, multi-adjacent note for
S-01/S-02/S-03, non-conflation count: 3.]

**Section B — Format contract**

[Identical to V-01 Section B — 7 column definitions with `*Violation type:*` annotations and
compliance failure conditions per C-27.]

**Section C — Annotation inventory**

This section declares **7 required annotations**. Phase 1 verifies this count before Phase 2
opens.

[Identical to V-01 Section C — 7-row table Annot-01 through Annot-07. PROHIBITED annotation
dropout clause physically co-located inside the inventory.]

**FORMAT CONTRACT COMPLETE** — SIG-01 produced. Phase 0.5 entry gate satisfied.

---

**PHASE 0.5 — BYPASS DEFEAT RECORD**

**Entry gate:** SIG-01 (FORMAT CONTRACT COMPLETE) present.

**Signal specification table:**

| Signal ID | Signal name | Phase produced | Confirms | Does NOT confirm |
|-----------|------------|----------------|----------|-----------------||
| SIG-01 | FORMAT CONTRACT COMPLETE | Phase 0 | Sections A, B, C are structurally present | That Section C annotation count = declared count of 7 |
| SIG-02 | INVENTORY VERIFIED | Phase 1 (next phase) | Section C Annot-ID row count = declared count of 7 | That Sections A, B, C are structurally present |

An executor SHALL NOT treat SIG-01 as equivalent to SIG-02. The "Does NOT confirm" column
makes the limitation of each signal a phase-visible fact: SIG-01's "Does NOT confirm" cell
names count non-verification; SIG-02 must be independently produced at Phase 1.

**Bypass defeat record:**

| Bypass attempt | Stage type | Gate reason |
|----------------|-----------|-------------|
| Skip Phase 0.5 and Phase 1 and open Phase 2 directly after SIG-01 | "Looks complete" — SIG-01 stated, Phase 2 tables present, lifecycle appears ready to enter analysis | Phase 0.5 and Phase 1 are distinct lifecycle gates. SIG-01 is the Phase 0 output gate — it confirms that Phase 0's structural sections exist. SIG-02 is the Phase 1 output gate — it confirms that Section C count = declared count of 7. These are non-overlapping gates: SIG-01 can be produced while SIG-02 is withheld (a 6-of-7 Section C satisfies SIG-01 but fails Phase 1's count check). Phase 2 entry requires SIG-02, not SIG-01. Skipping Phase 0.5 and Phase 1 converts the count check from a gate condition into an unverified assumption. |

**PHASE GATE FIELD — This field is a required gate slot in the lifecycle sequence. Phase 1
(COUNT VERIFICATION) SHALL NOT open until this field is filled. An executor SHALL fill this
field before proceeding to Phase 1:**

[ BYPASS ATTEMPT IDENTIFIED AND REJECTED / NO BYPASS ATTEMPT DETECTED ]

**Phase 0.5 output:** Phase gate field filled. Phase 1 entry gate satisfied.

---

**PHASE 1 — COUNT VERIFICATION**

**Entry gate:** Phase 0.5 PHASE GATE FIELD filled.

| Lifecycle check | Expected | Actual | Verdict |
|-----------------|----------|--------|---------|
| SIG-01 (FORMAT CONTRACT COMPLETE) recorded in Phase 0 | Present | [Y/N] | CLEARED if Y |
| Section C Annot-ID row count | 7 | [count rows] | CLEARED if = 7; RETURN TO PHASE 0 if < 7 |

**Phase 1 outcome:**
- All CLEARED → state **INVENTORY VERIFIED** (SIG-02 produced). Phase 2 entry gate satisfied.
- Any RETURN TO PHASE 0 → state **INVENTORY INCOMPLETE** (SIG-02 withheld). Complete Section C
  to 7 rows. Re-state FORMAT CONTRACT COMPLETE (SIG-01 re-issued). Re-enter Phase 0.5 from the
  top. Re-enter Phase 1.

**PHASE 1 GATE STATUS:**
- SIG-02: [ INVENTORY VERIFIED / INVENTORY INCOMPLETE ]
- Phase 2 entry: [ OPEN — SIG-02 = INVENTORY VERIFIED / BLOCKED — return to Phase 0 ]

---

**PHASE 2 — ANALYSIS**

**Entry gate:** SIG-02 = INVENTORY VERIFIED. An executor SHALL NOT open Step 1A if Phase 1
GATE STATUS Phase 2 entry is not OPEN.

**REGISTRY GAP PROHIBITION — Failure 5 prevention (C-17):** Tiers discovered during Step 2 are
scope violations. PROHIBITED: assigning a new T-NN during Step 2. Return to TABLE A and restart
from the point of discovery. This prohibition SHALL be restated at each Step 2 section.

**Step 1A — VOLUME ANALYST: TIER IDENTIFICATION AND LIMITS**

**PHASE ENTRY CONDITION:** Step 1A SHALL be entered only after Phase 1 GATE STATUS = OPEN.

[TABLE A with all columns as V-01 including `Load-shape verdict` placeholder for Step 1B.
STEP 1A GATE as V-01.]

**Step 1B — LOAD-SHAPE ANALYST: CLASSIFICATION**

**PHASE ENTRY CONDITION:** Step 1B SHALL be entered only after STEP 1A GATE is cleared.

[Identical to V-01 Step 1B — lifecycle framing: "load-shape classification at registration is
a lifecycle property of Phase 2 Step 1B; deferring to Step 2G creates a cross-step circular
dependency that Phase 2's lifecycle cannot resolve." STEP 1B GATE as V-01.]

**Steps 2A through 2H** — [Identical structure to V-01 Steps 2A–2H with standing REGISTRY GAP
reminders and phase entry conditions at each step.]

---

**PHASE 3 — AUDIT**

**Entry gate:** Step 2H closed.

**Field 1 — Tier-ID threading (C-13):** [Identical to V-01 Field 1.]

**Field 2 — REGISTRY GAP enforcement (C-17/C-19):** [Identical to V-01 Field 2.]

**Field 3 — Load-shape classification at registration (C-16):** [Identical to V-01 Field 3.]

**Field 4 — Annotation dropout (C-40):** [Identical to V-01 Field 4.]

**Field 5 — Lifecycle gate chain compliance (C-41 + C-42 + C-45 + C-46 + C-47 + C-48):**

Verify each item by citing the phase and artifact from the body:

(a) C-46: Lifecycle stage overview table appears at the prompt header; SIG-01 and SIG-02 appear
    as distinct Gate signal entries in separate Phase rows before any phase body — cite the two
    rows.
(b) C-45: Signal specification table in Phase 0.5 has a "Does NOT confirm" column — cite the
    SIG-01 "Does NOT confirm" cell value verbatim.
(c) C-47: Bypass defeat record in Phase 0.5 contains at least one row with Bypass attempt,
    Stage type, and Gate reason columns — cite the Stage type cell value.
(d) C-48: PHASE GATE FIELD was filled before Phase 1 opened — cite the filled value.
(e) C-41 + C-42: Phase 1 GATE STATUS SIG-02 = INVENTORY VERIFIED was recorded before Step 1A
    opened — cite the Phase 1 GATE STATUS value.
State PASS for each item or FAIL with the specific phase and missing artifact.

**Per-section compliance status (C-18):** [Identical to V-01 per-section table with Phase 2
Step 1A through Step 2H rows.]

---

## V-04

**Axes:** Phrasing register (primary) + Inertia framing (secondary) — combined

**Hypothesis:** Combining formal SHALL-language phrasing with explicit inertia framing produces
the strongest enforcement register for all four v18 criteria. C-46: the SHALL-activation role
sequence table at the header states SHALL-NOT-activate consequences directly in the Handoff
signal cells, making the two-signal chain not just visible but carrying enforcement weight.
C-45: the SHALL-contract signal table uses "DOES NOT CONFIRM" as a capitalized column header,
and the non-conflation statement says "An executor SHALL NOT treat SIG-01 as evidence that SIG-02
is satisfied — the DOES NOT CONFIRM value for SIG-01 is the authoritative statement of this
limit." C-47: the PROHIBITED FRAMING REGISTER records each bypass defeat as a typed row with
a SHALL NOT PROCEED column, making the prohibition column-scannable. C-48: the MANDATORY BYPASS
DECLARATION is a named fill field with SHALL FILL instruction; the activation sequence cannot
begin until the field is filled, framed as an activation prerequisite rather than a section.
Every structural gate uses SHALL language, making compliance a contract obligation rather than
a recommendation.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
the rate-limited system described in the signal. Treat the stated request volume as 1x nominal;
also analyze at 2x and 5x.

The tables below are the primary output — every cell SHALL be filled. Produce sections in the
order shown. This prompt uses a four-role activation contract with SHALL-language handoff gates.

**Role activation contract:**

| Role | SHALL activate when | Handoff signal | SHALL NOT activate if |
|------|---------------------|----------------|----------------------|
| Role 1 — FORMAT CONTRACT | Immediately | SIG-01: FORMAT CONTRACT COMPLETE | N/A |
| Role 1.5 — INVENTORY VERIFIER | SIG-01 is present | SIG-02: INVENTORY VERIFIED or INVENTORY INCOMPLETE | SIG-01 is absent |
| Role 2 — DOMAIN EXPERT | SIG-02 = INVENTORY VERIFIED | Step 2H closed | SIG-02 is absent, INVENTORY INCOMPLETE, or MANDATORY BYPASS DECLARATION unfilled |
| Role 3 — AUDIT | Step 2H closed | Audit complete | Step 2H is not closed |

An executor SHALL treat this table as the authoritative activation contract. SIG-01 and SIG-02
are separate Handoff signal cells — they are structurally distinct and carry distinct SHALL NOT
activate conditions. An executor SHALL NOT treat SIG-01 as satisfying Role 2's activation
condition.

---

**ROLE 1 — FORMAT CONTRACT**

**Section A — Precision-site inventory**

[Identical to V-01 Section A — 7-site table S-01 through S-07 with multi-adjacent note and
non-conflation count of 3 at TABLE A.]

**Section B — Format contract**

[Identical to V-01 Section B — 7 column definitions with `*Violation type:*` annotations and
compliance failure conditions per C-27. Each definition SHALL be satisfied in the output body
or the column fails the compliance condition stated.]

**Section C — Annotation inventory**

This section declares **7 required annotations**. An executor SHALL NOT proceed past Role 1.5
until this count is verified.

[Identical to V-01 Section C — 7-row table Annot-01 through Annot-07. PROHIBITED annotation
dropout clause physically co-located inside the inventory.]

**FORMAT CONTRACT COMPLETE** — SIG-01 produced. Role 1.5 SHALL activate.

---

**ROLE 1.5 — INVENTORY VERIFIER**

**Activation condition satisfied:** SIG-01 (FORMAT CONTRACT COMPLETE) present.

**SHALL-contract signal table:**

| Signal ID | Signal name | Produced by | CONFIRMS | DOES NOT CONFIRM |
|-----------|------------|-------------|----------|-----------------|
| SIG-01 | FORMAT CONTRACT COMPLETE | Role 1 | Sections A, B, C are structurally present | That Section C annotation count = declared count of 7 |
| SIG-02 | INVENTORY VERIFIED | Role 1.5 | Section C Annot-ID row count = declared count of 7 | That Sections A, B, C are structurally present |

An executor SHALL NOT treat SIG-01 as evidence that SIG-02 is satisfied. The DOES NOT CONFIRM
value for SIG-01 is the authoritative statement of this limit: "That Section C annotation count
= declared count of 7" is what SIG-01 explicitly does not confirm, making this a column-readable
contract obligation rather than a prose qualification.

**PROHIBITED FRAMING REGISTER:**

| Prohibited framing | SHALL NOT proceed because | Structural enforcement |
|--------------------|--------------------------|----------------------|
| Activate Role 2 on SIG-01 (FORMAT CONTRACT COMPLETE) on the basis that the output appears complete or analysis scaffolding is in place | SIG-01 is a section-presence confirmation only (see DOES NOT CONFIRM column above). SIG-02 requires independent count verification. An executor SHALL NOT treat section presence as count confirmation — these are non-overlapping obligations | The DOES NOT CONFIRM column value for SIG-01 states the limit explicitly. A Section C with 6 of 7 annotations satisfies SIG-01 while failing SIG-02. The MANDATORY BYPASS DECLARATION below SHALL be filled before the verification table opens, enforcing that the executor has processed this prohibition before count verification begins |

**MANDATORY BYPASS DECLARATION — An executor SHALL fill this field. This field is an
activation prerequisite: the count verification sequence SHALL NOT open until this declaration
is filled:**

[ BYPASS ATTEMPT IDENTIFIED AND REJECTED / NO BYPASS ATTEMPT DETECTED ]

**Count verification sequence (opens only after MANDATORY BYPASS DECLARATION is filled):**

**Step G-1 — SIG-01 confirmation:**
An executor SHALL verify that FORMAT CONTRACT COMPLETE appears in Role 1.
Record: SIG-01 present = [Y/N]. An executor SHALL NOT proceed to Step G-2 if SIG-01 is absent.

**Step G-2 — Section C count:**
An executor SHALL count the Annot-ID rows in Section C.
Record: Actual count = [fill].

**Step G-3 — Count outcome:**
- Actual count = 7: An executor SHALL record **INVENTORY VERIFIED** (SIG-02 produced). Proceed
  to Step G-4.
- Actual count < 7: An executor SHALL record **INVENTORY INCOMPLETE** (SIG-02 withheld). Return
  to Role 1. Complete Section C to 7 rows. Re-state FORMAT CONTRACT COMPLETE (SIG-01
  re-issued). Re-enter Role 1.5 from the top. An executor SHALL NOT proceed to Step G-4.

**Step G-4 — Verification status record:**

**VERIFICATION STATUS:**
- SIG-01 (FORMAT CONTRACT COMPLETE): [ CONFIRMED / NOT YET ]
- SIG-02 (INVENTORY VERIFIED): [ CONFIRMED / WITHHELD ]
- Role 2 activation: [ CLEARED — both signals confirmed / BLOCKED — return to Role 1 ]

An executor SHALL fill all three fields. An executor SHALL NOT open Role 2 / Step 1A if Role 2
activation = BLOCKED or any field is unfilled.

---

**ROLE 2 — DOMAIN EXPERT**

**Activation condition:** Role 2 activation = CLEARED (from VERIFICATION STATUS Step G-4). An
executor SHALL confirm this field before opening Step 1A. An executor SHALL NOT open Step 1A
if VERIFICATION STATUS = BLOCKED or any VERIFICATION STATUS field is unfilled.

**REGISTRY GAP PROHIBITION — Failure 5 prevention (C-17):** Tiers discovered during Step 2 are
scope violations. PROHIBITED: assigning a new T-NN during Step 2. Return to TABLE A, register
the tier, and restart. This prohibition SHALL be restated at each Step 2 section.

**Step 1A — VOLUME ANALYST: TIER IDENTIFICATION AND LIMITS**

**PHASE ENTRY CONDITION:** Step 1A SHALL be entered only after VERIFICATION STATUS Role 2
activation = CLEARED.

[TABLE A with all columns as V-01. `Load-shape verdict` placeholder for Step 1B. STEP 1A GATE
as V-01 — all T-NN rows populated, no vague `Limit` labels, `Binding?` with causal mechanisms,
at least 2 distinct `Failure mode` values.]

**Step 1B — LOAD-SHAPE ANALYST: CLASSIFICATION**

**PHASE ENTRY CONDITION:** Step 1B SHALL be entered only after STEP 1A GATE is cleared.

[Identical to V-01 Step 1B — CLASSIFICATION REQUIRED AT STEP 1B with SHALL language, deferral
prohibition, escape-route frame, STEP 1B GATE. An executor SHALL assign SHAPE-NEUTRAL or
SHAPE-SENSITIVE for every row at this step — SHALL NOT defer to Step 2G.]

**Steps 2A through 2H** — [Identical structure to V-01 Steps 2A–2H. All reminders use SHALL
language. Standing REGISTRY GAP PROHIBITED reminder at each Step 2 section states: "An executor
SHALL NOT assign a new T-NN here. An executor SHALL return to TABLE A and SHALL restart from
the discovery point." Phase entry conditions use SHALL language.]

---

**ROLE 3 — AUDIT**

**Activation condition:** Step 2H closed.

**Field 1 — Tier-ID threading (C-13):** [Identical to V-01 Field 1 with SHALL language.]

**Field 2 — REGISTRY GAP enforcement (C-17/C-19):** [Identical to V-01 Field 2 with SHALL
language.]

**Field 3 — Load-shape classification at registration (C-16):** [Identical to V-01 Field 3
with SHALL language.]

**Field 4 — Annotation dropout (C-40):** [Identical to V-01 Field 4 with SHALL language.]

**Field 5 — SHALL-contract and v18 criteria compliance (C-41 + C-42 + C-45 + C-46 + C-47 + C-48):**

An executor SHALL verify each item by citing explicit evidence from the body:

| Item | Criterion | SHALL verify | Status |
|------|-----------|-------------|--------|
| (a) | C-46 | Role activation contract table at prompt header shows SIG-01 and SIG-02 as separate Handoff cells with distinct SHALL NOT activate conditions before any role body — cite the table and both Handoff cell values | PASS / FAIL |
| (b) | C-45 | SHALL-contract signal table has a "DOES NOT CONFIRM" column (capitalized) — cite the SIG-01 "DOES NOT CONFIRM" cell value verbatim | PASS / FAIL |
| (c) | C-47 | PROHIBITED FRAMING REGISTER contains at least one row with Prohibited framing, SHALL NOT proceed because, and Structural enforcement columns — cite the SHALL NOT proceed value | PASS / FAIL |
| (d) | C-48 | MANDATORY BYPASS DECLARATION was filled before the count verification sequence opened — cite the filled value | PASS / FAIL |
| (e) | C-41 + C-42 | VERIFICATION STATUS Role 2 activation = CLEARED was recorded before Step 1A opened — cite the VERIFICATION STATUS value | PASS / FAIL |

An executor SHALL state overall PASS if all items pass. An executor SHALL state FAIL with the
specific item and missing artifact. An executor SHALL NOT infer compliance from output quality.

**Per-section compliance status (C-18):** [Identical to V-01 per-section table.]

---

## V-05

**Axes:** Role sequence (primary) + Output format (secondary) + Inertia framing (secondary)

**Hypothesis:** Three combined axes produce maximum structural reinforcement for all four v18
criteria simultaneously:
(1) Role sequence — Role 1.5 architecture creates the cleanest two-signal separation; the role
    activation chain table at the header (C-46) makes this visible architecturally before any
    role body. The table uses a "Signal chain" column where SIG-01 appears in Role 1's cell and
    SIG-02 appears in Role 1.5's cell — distinct cells in a single column, scannable top-down.
(2) Output format — the signal distinction table in Role 1.5 (C-45) has a "Does NOT confirm"
    column whose cell value is quoted verbatim in the non-conflation statement, linking the
    prose requirement back to a column-scannable artifact. The BYPASS DEFEAT REGISTER (C-47) is
    a named, typed table in Role 1.5 whose rows are auditable without reading surrounding prose.
(3) Inertia framing — the BYPASS REJECTION FIELD (C-48) uses "BYPASS ATTEMPT IDENTIFIED AND
    REJECTED / NO BYPASS ATTEMPT DETECTED" as two options, requiring active disambiguation
    between detected and undetected bypasses. The field placement immediately above the
    verification table makes the verification table structurally unreachable until the field is
    filled.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
the rate-limited system described in the signal. Treat the stated request volume as 1x nominal;
also analyze at 2x and 5x.

The tables below are the primary output — every cell SHALL be filled. Produce sections in the
order shown. This prompt uses a four-role sequence with explicit handoff signals.

**Role activation chain:**

| Role | Activation signal | Signal chain | Responsibility |
|------|------------------|--------------|----------------|
| Role 1 — FORMAT CONTRACT | None (runs first) | SIG-01: FORMAT CONTRACT COMPLETE | Precision-site inventory (7 sites, S-01–S-07), format contract (7 column definitions), annotation inventory (7 annotations) |
| Role 1.5 — INVENTORY VERIFIER | FORMAT CONTRACT COMPLETE (SIG-01) | SIG-02: INVENTORY VERIFIED or INVENTORY INCOMPLETE | Signal distinction table with "Does NOT confirm" column (C-45), bypass defeat register (C-47), bypass rejection field (C-48), count verification table |
| Role 2 — DOMAIN EXPERT | INVENTORY VERIFIED (SIG-02) | Step 2H closed | Steps 1A–2H: tier inventory, load-shape classification, backpressure trace, UX catalog, burst paths, risk ranking, cascade scenario, Retry-After assessment, load shape comparison, mitigation registry |
| Role 3 — AUDIT | Step 2H closed | Audit complete | Fields 1–5 compliance verification, per-section status |

An executor SHALL NOT activate a role until its activation signal is present. SIG-01 and SIG-02
appear as separate cells in the Signal chain column — structurally distinct entries visible
before any role body begins. An executor SHALL NOT treat SIG-01 as the activation signal for
Role 2. An executor seeing INVENTORY INCOMPLETE in Role 1.5's Signal chain cell SHALL return
to Role 1 — Role 2 does not activate on INVENTORY INCOMPLETE.

---

**ROLE 1 — FORMAT CONTRACT**

**Section A — Precision-site inventory**

[Identical to V-01 Section A — 7-site table S-01 through S-07, multi-adjacent note for
S-01/S-02/S-03 group (3 non-overlapping violation types at TABLE A), non-conflation count: 3.]

**Section B — Format contract**

[Identical to V-01 Section B — 7 column definitions for TABLE A `Limit`, TABLE A `Binding?`,
TABLE A `Failure mode`, TABLE B `Mechanism`, TABLE C `Error code or signal`, TABLE E `Type`,
TABLE F `Setting or API parameter`. Each definition includes `*Violation type:*` annotation
at anchor site and compliance failure condition per C-27.]

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

**FORMAT CONTRACT COMPLETE** — SIG-01 produced. Role 1.5 activation signal issued.

---

**ROLE 1.5 — INVENTORY VERIFIER**

**Activation signal received:** FORMAT CONTRACT COMPLETE (SIG-01)

**Signal distinction table:**

| Signal ID | Signal name | Produced by | Confirms | Does NOT confirm |
|-----------|------------|-------------|----------|-----------------||
| SIG-01 | FORMAT CONTRACT COMPLETE | Role 1 | Sections A, B, C are structurally present | That Section C annotation count = declared count of 7 |
| SIG-02 | INVENTORY VERIFIED | Role 1.5 (this role) | Section C Annot-ID row count = declared count of 7 | That Sections A, B, C are structurally present |

An executor SHALL treat SIG-01 and SIG-02 as structurally distinct signals. The "Does NOT
confirm" column value for SIG-01 — "That Section C annotation count = declared count of 7" —
is the authoritative statement that SIG-01 does not cover count verification. An executor
SHALL NOT treat the presence of SIG-01 as evidence that SIG-02 is satisfied: the "Does NOT
confirm" value for SIG-01 names the exact gap that SIG-02 exists to close.

**Inertia-frame rejection — the "looks complete" bypass failure mode:**

**Named failure mode:** "Looks complete / just start" — SIG-01 (FORMAT CONTRACT COMPLETE) has
been stated and the analysis tables are scaffolded; Role 2 appears ready to activate.

**BYPASS DEFEAT REGISTER:**

| Bypass attempt | Attempt type | Structural reason for rejection |
|----------------|-------------|---------------------------------|
| Activate Role 2 on SIG-01 (FORMAT CONTRACT COMPLETE) on the basis that the prompt appears complete or analysis scaffolding is present | "Looks complete" — SIG-01 stated, tables scaffolded, Role 2 appears structurally ready | SIG-01 is a section-presence signal (see "Does NOT confirm" column: "That Section C annotation count = declared count of 7"). It confirms that Sections A, B, C exist but does NOT verify that Section C contains the declared count of 7 annotations. A Section C with 6 of 7 annotations satisfies SIG-01 while failing SIG-02 — the discrepancy is detectable only after Role 2 produces output if the count is not verified. Role 1.5 has single-responsibility for count verification; its handoff signal SIG-02 is the activation condition for Role 2 (see role activation chain table at header: Role 2 activation signal = INVENTORY VERIFIED, not FORMAT CONTRACT COMPLETE). Bypassing Role 1.5 converts Section C count from a verifiable gate into an unverified assertion. This proof parallels C-26 at Step 1B: just as Step 1B cannot be deferred because Step 2G depends on Load-shape verdicts that only Step 1B produces, Role 2 cannot bypass Role 1.5 because Role 2's annotation contract depends on count-verified inventory that only Role 1.5 certifies. |

**BYPASS REJECTION FIELD — An executor SHALL fill this field before proceeding to the
verification table. The verification table is presented below this field and is structurally
unavailable until this field is filled:**

[ BYPASS ATTEMPT IDENTIFIED AND REJECTED / NO BYPASS ATTEMPT DETECTED ]

**Verification table:**

| Check | Expected | Actual | Verdict |
|-------|----------|--------|---------|
| SIG-01 (FORMAT CONTRACT COMPLETE) recorded in Role 1 | Present | [Y/N] | PASS if Y |
| Section C Annot-ID row count | 7 | [count rows] | PASS if actual = 7; FAIL if actual < 7 |

**Outcome:**
- All PASS → state **INVENTORY VERIFIED** (SIG-02 produced) → Role 2 activates.
- Any FAIL → state **INVENTORY INCOMPLETE** (SIG-02 withheld) → return to Role 1. Correct the
  gap. Re-state FORMAT CONTRACT COMPLETE (SIG-01 re-issued). Re-enter Role 1.5 from the top.

**HANDOFF SIGNAL: [ INVENTORY VERIFIED / INVENTORY INCOMPLETE ]** — fill before Role 2.

---

**ROLE 2 — DOMAIN EXPERT**

**Activation signal required:** INVENTORY VERIFIED (SIG-02, from Role 1.5). An executor SHALL
confirm Role 1.5 HANDOFF SIGNAL = INVENTORY VERIFIED before opening Step 1A. An executor SHALL
NOT open Step 1A if HANDOFF SIGNAL = INVENTORY INCOMPLETE or if the HANDOFF SIGNAL field is
unfilled.

**REGISTRY GAP PROHIBITION — Failure 5 prevention (C-17):** Tiers discovered during Step 2
are scope violations. PROHIBITED: assigning a new T-NN during Step 2. An executor SHALL return
to TABLE A, register the tier with all required columns, and SHALL restart from the point of
discovery. This prohibition SHALL be restated at each Step 2 section where mid-phase discovery
could occur.

---

**Step 1A — VOLUME ANALYST: TIER IDENTIFICATION AND LIMITS**

**PHASE ENTRY CONDITION:** Step 1A SHALL be entered only after Role 1.5 HANDOFF SIGNAL =
INVENTORY VERIFIED.

*(Volume analyst role: identify every rate-limiting component; record numeric limit, scope,
binding status with causal reason, failure mode, failure visibility window, and recovery time.
Leave `Load-shape verdict` as placeholder — assign at Step 1B.)*

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
| At least 2 distinct `Failure mode` values across rows | Y | |

Step 1B SHALL NOT open until all gate checks = Y.

**PHASE EXIT CONDITION:** Step 1A is exited when STEP 1A GATE TABLE is all-Y.

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

Step 2A SHALL NOT open until all gate checks = Y.

---

**Step 2A — BACKPRESSURE PROPAGATION TRACE (TABLE B)**

**PHASE ENTRY CONDITION:** Step 2A SHALL be entered after STEP 1B GATE TABLE is all-Y.

**Step 2A — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19):** Tiers in
backpressure analysis not in TABLE A are scope violations. An executor SHALL NOT assign a new
T-NN here. Return to TABLE A.

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
| F-1 | C-13 tier-ID threading | Every T-NN appears verbatim in all downstream sections (TABLE B, TABLE C, TABLE D, TABLE E, Step 2E, TABLE F) | PASS / [list gaps] |
| F-2 | C-17/C-19 registry gap | No T-NN assigned outside TABLE A in Steps 2A–2H | PASS / [list violations] |
| F-3 | C-16 load-shape at registration | All Load-shape verdicts assigned at Step 1B, not Step 2G | PASS / [list deferrals] |
| F-4 | C-40 annotation dropout | Annot-01 through Annot-07 each present at anchor site | PASS / [list: Annot-ID | site | status] |
| F-5 | C-41 + C-42 + C-45 + C-46 + C-47 + C-48 | See sub-items (a)–(e) below | PASS / FAIL + identify missing artifact |

**Field 5 sub-items:**
(a) C-46: Role activation chain table at prompt header shows SIG-01 in Role 1's Signal chain
    cell and SIG-02 in Role 1.5's Signal chain cell as distinct column entries before any role
    body begins — cite the table and both Signal chain cell values.
(b) C-45: Signal distinction table in Role 1.5 has a "Does NOT confirm" column — cite the
    SIG-01 "Does NOT confirm" cell value verbatim and the non-conflation statement that quotes
    it.
(c) C-47: BYPASS DEFEAT REGISTER in Role 1.5 contains at least one row with Bypass attempt,
    Attempt type, and Structural reason columns — cite the Attempt type cell value.
(d) C-48: BYPASS REJECTION FIELD was filled before the verification table — cite the filled
    value and confirm that the verification table appears below the field in the prompt body.
(e) C-41 + C-42: Role 1.5 HANDOFF SIGNAL = INVENTORY VERIFIED (SIG-02) was explicitly recorded
    before Step 1A opened; SIG-01 appears in Role 1 as FORMAT CONTRACT COMPLETE and SIG-02
    appears in Role 1.5 as INVENTORY VERIFIED — they are structurally distinct records, not
    inferred from body quality. Cite both records.

State F-5 PASS if all five sub-items are satisfied. State FAIL with the specific sub-item and
missing artifact.

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
