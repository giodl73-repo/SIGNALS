---
name: flow-throttle
description: Rate-limit throughput simulation showing backpressure propagation and burst path gaps.
allowed-tools: [Read, Write, Glob]
param_set: lean
---
depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure


You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
the rate-limited system described in the signal. Treat the stated request volume as 1x nominal;
also analyze at 2x and 5x.

The tables below are the primary output — every cell SHALL be filled. Produce sections in the
order shown. This prompt uses a four-role activation sequence with named handoff signals.

**Role activation chain:**

| Role | Activation condition | Handoff signal | Responsibility | SHALL NOT activate if |
|------|---------------------|----------------|----------------|----------------------|
| Role 1 — FORMAT CONTRACT | None (runs first) | SIG-01: FORMAT CONTRACT COMPLETE | Precision-site inventory, format contract, annotation inventory | — (runs unconditionally) |
| Role 1.5 — INVENTORY VERIFIER | SIG-01 present | SIG-02: INVENTORY VERIFIED or INVENTORY INCOMPLETE | Signal distinction table, bypass rejection register, bypass gate field, count verification (G-1–G-4), VERIFICATION STATUS RECORD | SIG-01 absent; SHALL NOT activate without SIG-01 recorded |
| Role 2 — DOMAIN EXPERT | SIG-02 = INVENTORY VERIFIED | Step 2H closed | All analysis: Steps 1A through 2H | SIG-02 ≠ INVENTORY VERIFIED; SHALL NOT open Step 1A on INVENTORY INCOMPLETE or unfilled HANDOFF SIGNAL |
| Role 3 — AUDIT | Step 2H closed | Audit complete | Compliance verification: Fields 1–5 typed audit table | Step 2H not closed; SHALL NOT begin audit before all analysis steps complete |

An executor SHALL NOT activate a role until its activation condition is met. The `SHALL NOT
activate if` column makes every role's bypass condition header-scannable without entering any
role body.

---

**ROLE 1 — FORMAT CONTRACT**

**Section A — Precision-site inventory**

This section inventories every location in this prompt where a column definition carries a
violation-type annotation. Count: 7 precision sites across 5 tables.

| Site-ID | Table | Column | Violation type | C-27 hierarchy |
|---------|-------|--------|----------------|----------------|
| S-01 | TABLE A | `Limit (number + unit)` | vague-label substitution | primary |
| S-02 | TABLE A | `Binding?` | assertion-without-causal-reason | adjacent-1 (S-01/S-02/S-03 group) |
| S-03 | TABLE A | `Failure mode` | insufficient-categorical-diversity | adjacent-2 (S-01/S-02/S-03 group) |
| S-04 | TABLE B | `Mechanism` | generic-term substitution | primary |
| S-05 | TABLE C | `Error code or signal` | plain-description substitution | primary |
| S-06 | TABLE E | `Type` | category-absence-undetectable | primary |
| S-07 | TABLE F | `Setting or API parameter` | category-of-action substitution | primary |

Multi-adjacent sites S-01, S-02, S-03 share TABLE A. An executor SHALL NOT treat
vague-label substitution, assertion-without-causal-reason, and insufficient-categorical-diversity
as variants of a single "incomplete entry" failure. Each is a distinct violation with a distinct
pass condition.

**Section B — Format contract**

**TABLE A — `Limit (number + unit)` (S-01, primary):**
A specific number with a unit is required (e.g., "1,000 req/min").
- *Violation type: vague-label substitution — a vague label ("limited", "throttled") substituted
  for a specific number-with-unit.*
- Compliance failure condition (C-27/S-01): An entry using a vague label fails this column.

**TABLE A — `Binding?` (S-02, adjacent-1):**
Y/N with a mechanism that explains why this tier is or is not binding at the relevant band.
- *Violation type: assertion-without-causal-reason — Binding? = Y with no mechanism stated.*
- Compliance failure condition (C-27/S-02): A Y entry without a named causal mechanism fails.
  Note: S-02 catches unsupported binary assertions; S-01 catches numeric imprecision —
  non-overlapping failure modes.

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
- Compliance failure condition (C-27/S-04): A `Mechanism` entry using a generic term fails.

**TABLE C — `Error code or signal` (S-05, primary):**
Record the specific HTTP status code or platform signal identifier (e.g., "HTTP 429", "TL-0001").
- *Violation type: plain-description substitution — "request fails" in place of "HTTP 429".*
- Compliance failure condition (C-27/S-05): A plain description rather than a code or signal
  identifier fails.

**TABLE E — `Type` (S-06, primary):**
Classify by type: throughput-risk, visibility-risk, cascade-risk, recovery-risk. Every row
SHALL have a named type.
- *Violation type: category-absence-undetectable — a risk entry with no Type value.*
- Compliance failure condition (C-27/S-06): A row with a blank or uncategorized `Type` fails.

**TABLE F — `Setting or API parameter` (S-07, primary):**
The exact configuration key, connector property, or API attribute name (e.g.,
`connector.retryPolicy`).
- *Violation type: category-of-action substitution — "add retry logic" in place of a named
  parameter identifier.*
- Compliance failure condition (C-27/S-07): A row naming a category of action rather than a
  specific parameter identifier fails.

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

PROHIBITED: annotation dropout at any anchor site listed in this inventory — an annotation
absent from its anchor site is detectable only by full body scan; this clause converts dropout
into a contract violation identifiable by Annot-ID lookup at this inventory without traversing
the body.

**FORMAT CONTRACT COMPLETE** — SIG-01 produced. Role 1.5 activation condition satisfied.

---

**ROLE 1.5 — INVENTORY VERIFIER**

**Activation condition:** SIG-01 (FORMAT CONTRACT COMPLETE) present.

**Signal distinction table:**

| Signal ID | Signal name | Produced by | Confirms | Does NOT confirm |
|-----------|------------|-------------|----------|-----------------|
| SIG-01 | FORMAT CONTRACT COMPLETE | Role 1 | Sections A, B, C are structurally present | That Section C annotation count = declared count of 7 |
| SIG-02 | INVENTORY VERIFIED | Role 1.5 (this role) | Section C Annot-ID row count = declared count of 7 | That Sections A, B, C are structurally present (verified by SIG-01 only) |

An executor SHALL NOT treat SIG-01 as evidence that SIG-02 is satisfied. The SIG-01 "Does NOT
confirm" cell value is the SHALL-authoritative contracted referent for this obligation:

> **SHALL-authoritative cell value:** "That Section C annotation count = declared count of 7"

This quote is not merely evidential — it is the contractual artifact this non-conflation
obligation is built on.

**Bypass-attempt rejection register:**

| Bypass attempt | Attempt type | Structural reason for rejection |
|----------------|-------------|----------------------------------|
| Open Role 2 after SIG-01 without completing G-1 bypass gate field and G-2/G-3 count sub-steps | "Looks complete" — SIG-01 stated, analysis tables scaffolded, prompt appears structurally ready | SIG-01 confirms section presence only (see SHALL-authoritative cell value blockquoted above). A Section C with 6 of 7 annotations satisfies SIG-01 while failing SIG-02 — the discrepancy is detectable only after Role 2 produces output if count steps are skipped. Role 1.5 has single-responsibility for count verification; bypassing it converts Section C count from a verifiable gate into an unverified assertion. |

**Count verification sequence:**

An executor SHALL complete sub-steps G-1 through G-4 in order. Each sub-step has its own SHALL
instruction and its own fill artifact. The consequence of skipping any sub-step is named at that
sub-step.

**G-1 — BYPASS GATE CONDITION**

An executor SHALL fill this field before proceeding to G-2. G-2 through G-4 are not available
until this field is filled.

`Consequence of skipping:` If G-1 is skipped, the bypass-gate detection step is omitted — the
bypass-attempt rejection register records no verdict, and G-2 and G-3 count steps proceed under
an undetected potential-bypass state. A bypass attempt that should have been identified and
rejected at G-1 cannot be retroactively detected at G-2 or G-3; the gate failure is invisible
after the fact.

[ BYPASS ATTEMPT IDENTIFIED AND REJECTED / NO BYPASS ATTEMPT DETECTED ]

**G-2 — SIG-01 PRESENCE CHECK**

An executor SHALL confirm that FORMAT CONTRACT COMPLETE (SIG-01) was recorded in Role 1.

`Consequence of skipping:` If G-2 is skipped, the SIG-01 presence gate is unchecked — Role 2
could activate against an incomplete format contract. A Role 1 that did not produce SIG-01 (due
to incomplete Section A, B, or C) is indistinguishable from a complete one if this check is
omitted. The error propagates silently into all downstream annotation verification steps.

| Check | Expected | Actual | Verdict |
|-------|----------|--------|---------|
| SIG-01 (FORMAT CONTRACT COMPLETE) recorded in Role 1 | Present | [Y/N] | PROCEED if Y; RETURN TO ROLE 1 if N |

**G-3 — SECTION C COUNT CHECK**

An executor SHALL count Annot-ID rows in Section C and compare to the declared count of 7.

`Consequence of skipping:` If G-3 is skipped, the annotation count is unchecked — SIG-02
(INVENTORY VERIFIED) would be issued without confirming that all 7 annotations exist at their
anchor sites. A Section C with 6 rows satisfies SIG-01 but fails the count gate; issuing SIG-02
without G-3 converts a count-verifiable gate into an unverified assertion that becomes
structurally opaque once Role 2 begins.

| Check | Expected | Actual | Verdict |
|-------|----------|--------|---------|
| Section C Annot-ID row count | 7 | [count rows] | PROCEED if actual = 7; RETURN TO ROLE 1 if actual < 7 |

**G-4 — HANDOFF SIGNAL DETERMINATION**

An executor SHALL determine the handoff signal based on G-2 and G-3 verdicts.

`Consequence of skipping:` If G-4 is skipped, the handoff signal is undeclared — Role 2 cannot
verify its activation condition because no explicit INVENTORY VERIFIED or INVENTORY INCOMPLETE
verdict exists. An undeclared handoff signal creates an ambiguous activation boundary: Role 2
may self-activate on SIG-01 alone, which C-41 prohibits.

- All PROCEED → **INVENTORY VERIFIED** (SIG-02 produced) → Role 2 activates
- Any RETURN TO ROLE 1 → **INVENTORY INCOMPLETE** (SIG-02 withheld) → return to Role 1;
  correct the gap; re-state FORMAT CONTRACT COMPLETE (SIG-01 re-recorded); re-enter Role 1.5
  from G-1

**VERIFICATION STATUS RECORD — An executor SHALL fill all three fields before issuing the
handoff signal:**

[ SIG-01 confirmed: Y / N ]
[ Annot-ID count confirmed (7 of 7): Y / N ]
[ Role 2 activation cleared: Y / N ]

**HANDOFF SIGNAL: [ INVENTORY VERIFIED / INVENTORY INCOMPLETE ]** — fill before Role 2.

---

**ROLE 2 — DOMAIN EXPERT**

**Activation condition:** SIG-02 = INVENTORY VERIFIED. An executor SHALL NOT open Step 1A if
Role 1.5 HANDOFF SIGNAL is not INVENTORY VERIFIED.

**REGISTRY GAP PROHIBITION — Failure 5 prevention (C-17):** Tiers discovered during Step 2 are
scope violations. PROHIBITED: assigning a new T-NN during Step 2 as a fill-in step. An executor
SHALL return to TABLE A, register the tier with all columns filled, and SHALL restart from the
point of discovery. This prohibition SHALL be restated at each Step 2 section where mid-phase
discovery could occur.

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

*Annot-01 (S-01): vague-label substitution — a vague label ("limited") substituted for a
specific number-with-unit fails `Limit`. Annot-02 (S-02): assertion-without-causal-reason —
Binding? = Y with no mechanism stated fails `Binding?`. Annot-03 (S-03):
insufficient-categorical-diversity — all rows sharing the same `Failure mode` value fails the
diversity requirement.*

**STEP 1A GATE:** Closed when every T-NN row is populated (except `Load-shape verdict`),
`Limit` contains no vague labels, `Binding?` entries include causal mechanisms, and at least
two distinct `Failure mode` values appear across rows. An executor SHALL NOT open Step 1B
until this gate is cleared.

---

**Step 1B — LOAD-SHAPE ANALYST: CLASSIFICATION**

**PHASE ENTRY CONDITION:** Step 1B SHALL be entered only after STEP 1A GATE is cleared.

**Failure 2 + Failure 6 prevention:** An executor SHALL assign `Load-shape verdict` for every
TABLE A tier at this step. PROHIBITED: deferring classification to Step 2G.

**Escape-route frame:** The temptation to defer is the "STATUS tracks volume thresholds" framing
— load-shape classification appears out of scope for the registry and naturally belonging in
"LOAD SHAPE COMPARISON." This frame is self-defeating: load-shape classification requires the
registered `Limit` value available now at Step 1B, and Step 2G depends on per-tier Load-shape
verdicts — deferring creates a circular dependency.

For each T-NN, classify:
- **SHAPE-NEUTRAL**: limit applies identically to uniform and burst traffic
- **SHAPE-SENSITIVE**: burst traffic reaches the limit faster than uniform traffic of the same
  total volume (name the differential and mechanism)

**STEP 1B GATE:** Closed when every TABLE A `Load-shape verdict` cell is filled.

---

**Step 2A — BACKPRESSURE PROPAGATION**

**PHASE ENTRY CONDITION:** Step 2A SHALL be entered only after STEP 1B GATE is cleared.

**REGISTRY GAP PROHIBITION (C-17/C-19 reminder):** An executor SHALL NOT assign a new T-NN
at this step. If a new component is discovered, return to TABLE A and restart.

*(Backpressure analyst role: trace how throttle pressure propagates from each binding tier.
Minimum 2 hops from the primary bottleneck. Name the mechanism at each hop from the permitted
set: queue-fill, connection-hold, retry-amplification, dependency-stall, timeout-cascade.)*

**TABLE B — BACKPRESSURE PROPAGATION**

| From | Hop | To | Mechanism | Observable effect at 1x | Observable effect at 5x |
|------|-----|----|-----------|-----------------------|------------------------|
|      | 1   |    |           |                       |                        |
|      | 2   |    |           |                       |                        |

*Annot-04 (S-04): generic-term substitution — "blocked", "throttled", or "slowed" in place of
a named mechanism from the permitted set fails `Mechanism`.*

An executor SHALL NOT close Step 2A with fewer than 2 hops traced.

---

**Step 2B — USER EXPERIENCE PER TIER**

**PHASE ENTRY CONDITION:** Step 2B SHALL be entered only after Step 2A is exited.

*(UX analyst role: for each throttle tier in TABLE A, describe the observable user experience
at saturation.)*

**TABLE C — USER EXPERIENCE AT THROTTLE SATURATION**

| Tier-ID | Component | Error code or signal | UX at 1x saturation | UX at 2x saturation | UX at 5x saturation |
|---------|-----------|---------------------|---------------------|---------------------|---------------------|
|         |           |                     |                     |                     |                     |

*Annot-05 (S-05): plain-description substitution — "request fails" in place of "HTTP 429"
fails `Error code or signal`.*

Every T-NN from TABLE A SHALL have a corresponding row.

---

**Step 2C — UNPROTECTED BURST PATHS**

**PHASE ENTRY CONDITION:** Step 2C SHALL be entered only after Step 2B is exited.

**REGISTRY GAP PROHIBITION (C-17/C-19 reminder):** An executor SHALL NOT assign a new T-NN.

**TABLE D — UNPROTECTED BURST PATHS**

| Path-ID | Description | Tier-IDs involved | Gap type | Risk at 5x |
|---------|-------------|------------------|----------|------------|
|         |             |                  |          |            |

At least one burst path SHALL be identified. If no unprotected burst path exists, name the
controls that prevent it — an empty TABLE D with no explanation fails.

---

**Step 2D — RISK TAXONOMY**

**PHASE ENTRY CONDITION:** Step 2D SHALL be entered only after Step 2C is exited.

**TABLE E — RISK TAXONOMY**

| Risk-ID | Tier-ID | Description | Type | Rank | Visibility window | Recovery time |
|---------|---------|-------------|------|------|-------------------|---------------|
|         |         |             |      | 1    |                   |               |
|         |         |             |      | 2    |                   |               |

*Annot-06 (S-06): category-absence-undetectable — a risk row with no Type value fails `Type`.*

Type values: throughput-risk, visibility-risk, cascade-risk, recovery-risk. Every row SHALL have
a named type. The Rank 1 risk SHALL have Visibility window and Recovery time filled.

---

**Step 2E — CASCADE SCENARIO**

**PHASE ENTRY CONDITION:** Step 2E SHALL be entered only after Step 2D is exited.

**REGISTRY GAP PROHIBITION (C-17/C-19 reminder):** An executor SHALL NOT introduce a new T-NN
in the cascade narrative.

Cascade scenario (narrative): Describe the sequence — Tier A throttles → mechanism → Tier B
receives delayed/batched/amplified traffic → Tier B throttles. Name at least three tiers in the
chain. Minimum two-tier cascade required; a single-tier scenario fails.

---

**Step 2F — RETRY-AFTER ASSESSMENT**

**PHASE ENTRY CONDITION:** Step 2F SHALL be entered only after Step 2E is exited.

For each caller interacting with a throttled tier: state whether Retry-After (or equivalent) is
consumed and honored, verdict (PASS/FAIL), and consequence if FAIL. At least one caller SHALL
be evaluated.

---

**Step 2G — LOAD SHAPE COMPARISON**

**PHASE ENTRY CONDITION:** Step 2G SHALL be entered only after Step 2F is exited.

**REGISTRY GAP PROHIBITION (C-17/C-19 reminder):** An executor SHALL NOT introduce new T-NN
designations at this step.

For each SHAPE-SENSITIVE tier from TABLE A Step 1B: compare uniform vs. burst traffic impact.
State at least one numeric differential. A purely qualitative comparison fails.

---

**Step 2H — SYNTHESIS AND RECOMMENDATIONS**

**PHASE ENTRY CONDITION:** Step 2H SHALL be entered only after Step 2G is exited.

**REGISTRY GAP PROHIBITION (C-17/C-19 reminder):** Final check — no new T-NN SHALL appear in
TABLE F.

**TABLE F — MITIGATION RECOMMENDATIONS**

| Rec-ID | Source T-NN | Risk addressed | Mitigation | Setting or API parameter | Tradeoff |
|--------|------------|----------------|------------|--------------------------|----------|
|        |            |                |            |                          |          |

*Annot-07 (S-07): category-of-action substitution — "add retry logic" in place of a named
parameter identifier fails `Setting or API parameter`.*

At least 2 mitigations SHALL be present; each SHALL include a named tradeoff.

**Step 2H CLOSED.**

---

**ROLE 3 — AUDIT**

**Activation condition:** Step 2H CLOSED. An executor SHALL NOT begin audit before Step 2H is
closed.

**Field 1 — Tier-ID threading (C-13):** Every T-NN from TABLE A appears verbatim in all
downstream sections (TABLE B `From`, TABLE C rows, TABLE D `Tier-IDs involved`, TABLE E
`Tier-ID`, Step 2E cascade trace, TABLE F `Source T-NN`). State PASS or list each discrepancy.

**Field 2 — REGISTRY GAP enforcement (C-17/C-19):** No new T-NN was assigned during Steps
2A–2H. State PASS or list violations.

**Field 3 — Load-shape classification at registration (C-16):** Every TABLE A row has a
non-placeholder `Load-shape verdict` assigned at Step 1B. State PASS or list deferred rows.

**Field 4 — Annotation dropout (C-40):** Every Annot-01 through Annot-07 is present at its
anchor site. State PASS or list: Annot-ID | anchor site | status.

**Field 5 — Signal chain and v20 criteria compliance:**

| Item | Criterion | Evidence required | Status |
|------|-----------|------------------|--------|
| Role activation chain declared at prompt header; SIG-01 and SIG-02 in distinct Handoff cells | C-46 | Header table present; SIG-01 cell in Role 1 Handoff column; SIG-02 cell in Role 1.5 Handoff column — cite both cells | [PASS + cite / FAIL + artifact missing] |
| Header table carries `SHALL NOT activate if` bypass-condition column for all roles | C-51 | `SHALL NOT activate if` column present in header table; cite the Role 2 bypass-condition cell value verbatim | [PASS + cite / FAIL + column absent] |
| Signal distinction table with "Does NOT confirm" column present in Role 1.5 | C-45 | Signal distinction table present; "Does NOT confirm" column header — cite column header text | [PASS + cite / FAIL + column absent] |
| Non-conflation statement quotes "Does NOT confirm" cell value as SHALL-authoritative contracted blockquote | C-52 + C-55 | Non-conflation blockquote present labeled `SHALL-authoritative cell value:`; blockquoted text matches SIG-01 "Does NOT confirm" cell exactly — verify by string comparison | [PASS + string match confirmed / FAIL + mismatch, absent, or inline-only] |
| Bypass-attempt rejection register present with 3 named columns | C-47 | 3-column bypass register row present — cite the Attempt type cell value | [PASS + cite / FAIL + register absent] |
| G-1 bypass gate field filled before G-2 count check | C-48 | G-1 fill field filled before G-2 — cite the filled value | [PASS + cite / FAIL + field unfilled or absent] |
| Count verification atomized into G-1 through G-4 each with SHALL instruction + `Consequence of skipping:` clause; VERIFICATION STATUS RECORD has 3 fill fields | C-50 + C-53 | G-1 through G-4 each present with own SHALL instruction and co-located `Consequence of skipping:` sub-field; VERIFICATION STATUS RECORD has 3 fill fields — confirm sub-step count = 4, consequence-clause count = 4, fill-field count = 3 | [PASS + confirm counts / FAIL + missing sub-step, clause, or field] |
| SIG-02 = INVENTORY VERIFIED as HANDOFF SIGNAL before Step 1A | C-41 + C-42 | HANDOFF SIGNAL = INVENTORY VERIFIED cited; confirm it precedes Step 1A | [PASS + cite / FAIL + missing or ordering wrong] |
| Bypass-detection co-presence: bypass register row AND G-1 gate fill AND SIG-01 presence all confirmed in a single audit row | C-44 + C-47 + C-48 (C-54) | Bypass register Attempt type cell cited AND G-1 fill field value cited AND SIG-01 Handoff cell cited — all three artifacts cited simultaneously in this single row, not across separate rows | [PASS + all three cited simultaneously / FAIL + separate rows only or any artifact absent] |

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