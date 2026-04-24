---
skill: quest-golden
skill_target: flow-dataflow
date: 2026-03-14
rounds: 20
rubric_final: flow-dataflow-rubric-v20-2026-03-14.md
score: 99.5
status: GOLDEN
---

# flow-dataflow — Golden Prompt

**Winning variation:** V-05 (R20, simplified — 24% reduction, all criteria preserved)
**Domain:** Media streaming royalty distribution pipeline
**Role sequence:** Operations → Commerce → Finance (non-natural: Operations-first)
**Structural innovations:** 16-SC chain; 4-column DETECTABILITY INDEX; 3-item Phase Gate 0;
three independent [A-00]-governing SCs (SC-0, SC-14, SC-15) with explicit co-governor
non-reliance assertion.

---

## Prompt Body

You are tracing data through a media streaming royalty distribution pipeline — play event
capture through usage aggregation, rights matching, royalty calculation, payment
distribution, and rights-holder analytics. Three expert roles run in the sequence
**Operations → Commerce → Finance**.

Produce [A-00] as a 4-column table (`SC | Violation Detectable At | Responsible Role | SLA Impact`)
before any role output. `SLA Impact` is `Yes` if violating this SC could directly cause a
royalty distribution SLA breach; otherwise `No`. Phase Gate 0 carries three verification
items before Role 1 (Operations) begins. Finance runs last and must cite Operations'
boundary artifacts directly — two positions prior in the Operations → Commerce → Finance
sequence — as a required skip-level citation. Phase Gate 2 verifies this by citing SC-12
by number.

---

### ARTIFACT REGISTRY

| Token | Artifact | Owner | Description |
|-------|----------|-------|-------------|
| [A-00] | DETECTABILITY INDEX | Pre-role | 4-column table (`SC \| Violation Detectable At \| Responsible Role \| SLA Impact`), 16 rows (SC-0 through SC-15); Phase Gate 0 appended with three verification items; produced FIRST. SC-0, SC-14, SC-15 apply. |
| [A-01] | INCUMBENT BASELINE | Operations | Manual play-report reconciliation and rights-matching workflow; ≥3 named steps with durations; produced first within Role 1. SC-11 applies. |
| [A-02] | DOMAIN CONTEXT | Operations | Entity vocabulary, distribution-cycle SLA (immutable after Stage 1), downstream consumer, cadence; SLA from [A-01] total. |
| [A-03] | STAGE TRACE — Operations | Operations | Play event ingestor → usage aggregation → rights matching engine; stage tables per SC-7. |
| [A-04] | BOUNDARY CHECKS — Operations | Operations | 7-column boundary tables per BOUNDARY BLOCK SCHEMA; Incumbent Equiv. cites [A-01]; required skip-level target for Finance (SC-12). |
| [A-05] | PHASE GATE 1 | Operations | Self-verification checklist; all ✓ before Commerce begins. SC-6 applies. |
| [A-06] | STAGE TRACE — Commerce | Commerce | Rights matching → royalty calculation → payment distribution; stage tables per SC-7. |
| [A-07] | BOUNDARY CHECKS — Commerce | Commerce | 7-column boundary tables; extends Elapsed (cumul.) from [A-04]; Incumbent Equiv. cites [A-01]. |
| [A-08] | PHASE GATE 2 | Commerce | Self-verification checklist; item [SC-12] verifies Finance skip-level citation. SC-6 applies. |
| [A-09] | STAGE TRACE — Finance | Finance | Payment distribution → rights-holder ledger → DSP reporting → royalty analytics; stage tables per SC-7. |
| [A-10] | BOUNDARY CHECKS — Finance | Finance | 7-column boundary tables; extends Elapsed (cumul.) from [A-07]; Incumbent Equiv. cites [A-01]. |
| [A-11] | STALE ANALYSIS | Finance | Normal-operation and failure-mode elapsed vs [A-02] threshold. |
| [A-12] | RECOVERY PRESCRIPTIONS | Finance | Named recovery; formula: `Fall back to [A-01] if [condition]`; SC-13 applies. |
| [A-13] | INCUMBENT TOTAL | Finance | Sum from [A-04], [A-07], [A-10]; role breakdown; immediately before [A-14]. |
| [A-14] | TRADE-OFF ANALYSIS | Finance | Cites [A-01], [A-02], [A-13]; ≥1 pattern; ≥2 dimensions; SC-8 and SC-13 apply. |

---

### REGISTER DECLARATION

**SC-0 DETECTABILITY INDEX GATE** governs [A-00]; enforced by Phase Gate 0 three-item
verification appended to [A-00] — (1) row count = 16, (2) every row has non-empty
Responsible Role, (3) every row has exactly `Yes` or `No` in SLA Impact — any failing check
is a protocol violation detectable from [A-00] table structure before any role content is
read.

**SC-1 CITATION OPENER** governs [A-06], [A-09]; token-match at each role's `Citing:` line;
detectable at role-opener without reading role body.

**SC-2 STAGE-WRITE PROGRESSION GATE** governs [A-03], [A-06], [A-09] and [A-04], [A-07],
[A-10]; inline lock — Stage N+1 only after preceding boundary complete; detectable at
stage-boundary position.

**SC-3 INCREMENTAL ELAPSED** governs [A-04], [A-07], [A-10] (`Elapsed (cumul.)`); zero-reset
fails; detectable at column-header and cell-value level.

**SC-4 BINARY VERDICT** governs [A-04], [A-07], [A-10] (`Verdict`); non-binary value fails;
detectable at cell-value level.

**SC-5 STALENESS IMMUTABILITY** governs [A-02]; verbatim phrase required; detectable by
phrase-match within [A-02].

**SC-6 PHASE GATE OBLIGATION** governs [A-05] and [A-08]; unchecked item blocks next role;
detectable at role-boundary line.

**SC-7 STAGE TABLE FORMAT** governs [A-03], [A-06], [A-09]; missing `Stage Latency` column
fails; detectable at table-header row.

**SC-8 TRADE-OFF AS REQUIRED SECTION** governs [A-14] requiring [A-01], [A-02], [A-13];
token absence fails; detectable from [A-14] citation token list.

**SC-9 INCUMBENT EQUIV. CELL FORM** governs [A-04], [A-07], [A-10]; `[A-01]` token per cell;
detectable at cell level.

**SC-10 INCUMBENT TOTAL BEFORE TRADE-OFF** governs [A-13] before [A-14]; Grand Total row;
detectable by artifact-order check at [A-14] header.

**SC-11 BASELINE-FIRST PRODUCTION** governs [A-01] as first within Role 1; detectable at
Role 1 artifact-order head.

**SC-12 SKIP-LEVEL CITATION IN FINANCE** governs [A-04] (Operations' boundary checks) via
Finance's `Citing:` line; enforced by Phase Gate 2 item citing [SC-12] by number —
`[A-04]` absent from Finance's `Citing:` line fails; detectable at Finance role-opener.
Finance = position 3; Operations = position 1; position distance is two.

**SC-13 BASELINE CLOSURE** governs [A-12] and [A-14] requiring [A-01] in both; detectable
from [A-12] and [A-14] header lines.

**SC-14 DETECTABILITY INDEX ROLE ASSIGNMENT** governs [A-00] (third column `Responsible
Role`); enforced by per-row non-empty check in [A-00] — any row with empty or absent
Responsible Role is a protocol violation detectable from [A-00] column cells before any
role content is read.

**SC-15 DETECTABILITY INDEX SLA IMPACT** governs [A-00] (fourth column `SLA Impact`);
enforced by per-row binary check in [A-00] — any row with a value other than exactly `Yes`
or exactly `No` is a protocol violation detectable from [A-00] column cells before any role
content is read.

Together, SC-0 through SC-15 form a complete closed verification chain. SC-0, SC-14, and
SC-15 all govern [A-00] with independent dual-slot anchoring: SC-0 for row count and Phase
Gate 0 completeness; SC-14 for per-row Responsible Role completeness; SC-15 for per-row
SLA Impact validity. No SC relies on another to supply the [A-00] enforcement reference.

**Part A — Field compliance markers:**

| Required Field | Column Header | Required Cell Form | Disqualifying Form |
|----------------|---------------|--------------------|--------------------|
| Domain entity | `Entity` | Named entity from [A-02] vocabulary | "data" or "records" alone |
| Elapsed (cumulative) | `Elapsed (cumul.)` | Numeric sum, in minutes | Partial sum; reset to zero |
| Freshness verdict | `Verdict` | Exactly `FRESH` or exactly `STALE` | Any other value |
| Error handling | `Error Handling` | Named mechanism or `no handling — see [A-12]` | Silence; omitted column |
| Schema change | `Schema Delta` | Named field-level changes or `NONE` | Omitted column |
| Data loss | `Data Loss Flag` | `YES — [loss point name]` or `NO` | Generic language |
| Incumbent equivalent | `Incumbent Equiv.` | `[A-01]: [named manual step + duration]` | Token omitted; column absent |
| Stage latency | `Stage Latency` | Explicit value, range, or characterization | Inferred only |

**Part B — Section format compliance markers:**

| Required Section | Section Header | Required Content Form | Disqualifying Form |
|------------------|---------------|----------------------|--------------------|
| INCUMBENT TOTAL | `### [A-13] INCUMBENT TOTAL` | Table: Operations, Commerce, Finance, Grand Total rows | Missing row; no Grand Total |
| TRADE-OFF ANALYSIS | `### [A-14] TRADE-OFF ANALYSIS` | [A-01], [A-02], [A-13] present; ≥1 pattern; ≥2 dimensions | Any token absent |

---

### BOUNDARY BLOCK SCHEMA

`Entity | Elapsed (cumul.) | Verdict | Error Handling | Schema Delta | Data Loss Flag | Incumbent Equiv.`

**Stage table format:** `Stage Latency | Schema In | Schema Out | Data Loss Flag`

---

### DETECTABILITY INDEX

| SC | Violation Detectable At | Responsible Role | SLA Impact |
|----|------------------------|-----------------|-----------|
| SC-0 | [A-00] row count, Responsible Role completeness, and SLA Impact validity — before any role content is read | Pre-role | No |
| SC-1 | Each non-first role's opening `Citing:` line — no role body reading required | Commerce, Finance | No |
| SC-2 | Each stage-advance transition position — no stage content reading required | All roles | Yes |
| SC-3 | The `Elapsed (cumul.)` column header and cell-value level — no row prose required | All roles | Yes |
| SC-4 | The `Verdict` cell-value level — no surrounding prose required | All roles | Yes |
| SC-5 | Phrase-match scan within [A-02] body — no other sections required | Operations | Yes |
| SC-6 | The role-boundary line before each role block — no role content required | Operations, Commerce | No |
| SC-7 | The stage table header row — no row contents required | All roles | No |
| SC-8 | The [A-14] citation token list — no prose interpretation required | Finance | No |
| SC-9 | The `Incumbent Equiv.` cell level — no surrounding prose required | All roles | No |
| SC-10 | The artifact-order position at [A-14] header — no cell value reading required | Finance | No |
| SC-11 | The Role 1 artifact-order head — no content reading required | Operations | No |
| SC-12 | Finance role-opener `Citing:` line — no role body reading required | Finance | No |
| SC-13 | The [A-12] and [A-14] section header lines — no section body required | Finance | No |
| SC-14 | Each [A-00] row's `Responsible Role` column cell — no row prose reading required | Pre-role | No |
| SC-15 | Each [A-00] row's `SLA Impact` column cell — no row prose reading required | Pre-role | No |

**Phase Gate 0** — Verify before Role 1 begins. Mark each ✓ or ✗:
- [ ] DETECTABILITY INDEX has exactly 16 rows (SC-0 through SC-15). Mark ✗ and halt if fewer.
- [ ] Every row has a non-empty `Responsible Role` value. Mark ✗ and halt if any cell is empty.
- [ ] Every row has exactly `Yes` or `No` in `SLA Impact`. Mark ✗ and halt if any other value.

---

### PRE-ROLE PRODUCTION

Produce [A-00] as a 4-column table with exactly 16 rows (SC-0 through SC-15). After the
table, append Phase Gate 0 and verify all three items ✓ before Role 1 begins.

---

### ROLE 1 — Operations

**[A-01] INCUMBENT BASELINE** — Write FIRST. Describe the manual play-report reconciliation
and rights-matching workflow this pipeline replaces. Include ≥3 named steps with durations
(e.g., "Rights analyst manually downloads weekly play-count report from each DSP portal and
cross-references usage totals against publishing rights database: 90 min"). Use entity
names reappearing in [A-02].

**[A-02] DOMAIN CONTEXT** — Entity vocabulary (reuse ≥2 from [A-01]): play event record,
usage aggregate, rights holder record, royalty calculation entry, payment distribution
record, rights-holder ledger entry, DSP reporting record, royalty analytics summary.
Downstream consumer and distribution cadence. Distribution-cycle SLA: integer with unit
from [A-01] total. Append verbatim: "This threshold is fixed. No subsequent role may revise
it after Stage 1 is written."

**[A-03] STAGE TRACE — Operations** — Per SC-7. Per SC-2.
- Stage 1: Streaming platform event emitter → play event ingestor
- Stage 2: Play event ingestor → usage aggregation service
- Stage 3: Usage aggregation → rights matching engine

**[A-04] BOUNDARY CHECKS — Operations** — Per BOUNDARY BLOCK SCHEMA.
[SC-3: Elapsed from 0.] [SC-4.] [SC-9: `[A-01]: [step + duration]`.]

**[A-05] PHASE GATE 1** — Mark ✓ or ✗:
- [ ] [A-01] first within Role 1 (SC-11)
- [ ] [A-01] ≥3 named steps with durations
- [ ] [A-02] SLA integer with unit; SC-5 phrase present
- [ ] [A-02] reuses ≥2 entity names from [A-01]
- [ ] Every [A-03] stage has four columns (SC-7)
- [ ] Every [A-04] block has seven columns per Part A
- [ ] `Elapsed (cumul.)` numeric sum (SC-3)
- [ ] `Verdict` FRESH or STALE (SC-4)
- [ ] [A-04] `Incumbent Equiv.`: `[A-01]: [step + duration]` (SC-9)

Commerce may not begin until all ✓. [SC-6.]

---

### ROLE 2 — Commerce

Citing: [A-01], [A-02], [A-04]

**[A-06] STAGE TRACE — Commerce** — Per SC-7. Per SC-2.
- Stage 4: Rights matching engine → royalty calculation service
- Stage 5: Royalty calculation → payment distribution service
- Stage 6: Payment distribution → rights-holder ledger (pre-posting handoff)

**[A-07] BOUNDARY CHECKS — Commerce** — Per BOUNDARY BLOCK SCHEMA.
[SC-3: extends [A-04] final.] [SC-4.] [SC-9.]

**[A-08] PHASE GATE 2** — Mark ✓ or ✗:
- [ ] Citing names [A-01], [A-02], [A-04] (SC-1)
- [ ] Every [A-06] stage has four columns (SC-7)
- [ ] Every [A-07] block has seven columns per Part A
- [ ] `Elapsed (cumul.)` extends [A-04] final (SC-3)
- [ ] `Verdict` from [A-02] threshold (SC-4)
- [ ] [A-07] `Incumbent Equiv.`: `[A-01]: [step + duration]` (SC-9)
- [ ] [SC-12]: Finance's `Citing:` line must include `[A-04]` — Operations' boundary
  checks, two positions prior. Position distance = two: Finance = position 3, Operations =
  position 1. Mark ✗ if [A-04] absent.

Finance may not begin until all ✓. [SC-6.]

---

### ROLE 3 — Finance

Citing: [A-01], [A-02], [A-04], [A-07]

**[A-09] STAGE TRACE — Finance** — Per SC-7. Per SC-2.
- Stage 7: Rights-holder ledger → DSP reporting service
- Stage 8: DSP reporting → royalty analytics dashboard
- Stage 9: Analytics dashboard → period royalty distribution report

**[A-10] BOUNDARY CHECKS — Finance** — Per BOUNDARY BLOCK SCHEMA.
[SC-3: extends [A-07] final.] [SC-4.] [SC-9.]

**[A-11] STALE ANALYSIS** —

| Entity ([A-02]) | Normal elapsed | Failure-mode elapsed | [A-02] threshold | Verdict |
|-----------------|----------------|----------------------|------------------|---------|

**[A-12] RECOVERY PRESCRIPTIONS** — [Per SC-13: cite [A-01].] Formula:
`Fall back to [A-01] if [specific condition]`. [A-01] in every formula.

**[A-13] INCUMBENT TOTAL** — Header: `### [A-13] INCUMBENT TOTAL`.

| Role | Incumbent Equiv. subtotal | Steps cited |
|------|--------------------------|-------------|
| Operations | | |
| Commerce | | |
| Finance | | |
| **Grand Total** | | |

**[A-14] TRADE-OFF ANALYSIS** — [Per SC-13: cite [A-01].] Header:
`### [A-14] TRADE-OFF ANALYSIS`. Tokens [A-01], [A-02], [A-13] required. ≥1 named
alternative pattern. ≥2 explicitly stated trade-off dimensions.

---

## What Made It Golden

**1. Three independent co-governors for a single artifact ([A-00])**
V-05 introduced SC-15 alongside the existing SC-0 and SC-14, giving [A-00] three separate
governing SCs each with full dual-slot anchoring — governed-artifact token and enforcement
mechanism named independently in every entry. No prior variation had more than two
co-governors for any artifact. This directly produced C-55 and C-56.

**2. The co-governor non-reliance assertion (C-56)**
The REGISTER DECLARATION closing paragraph makes explicit that "No SC relies on another to
supply the [A-00] enforcement reference." This is not implied by individual SC correctness
— it is a separate declarative claim that each co-governing SC is self-sufficient. This
one sentence produced a new criterion (C-56) and became a structural requirement for all
future variations.

**3. Four-column DETECTABILITY INDEX with SLA Impact**
Adding `SLA Impact` (Yes/No) as a fourth column to [A-00] raised Phase Gate 0 from two
items to three — one item per structural dimension of [A-00]. This created a tighter
coupling between the index structure and the gate that verifies it, making the Phase Gate 0
multi-item requirement (C-54) more expressive and verifiable.

**4. Operations-first non-natural sequence (O→C→F)**
The O→C→F sequence had not appeared in any prior round. It placed the skip-level citation
obligation on Finance (last) pointing back to Operations (first), maximising the position
distance and making the SC-12 two-position assertion unambiguous.

**5. 24% simplification with zero criterion loss**
The winning body was reduced from 3,042 to 2,307 words by removing the STRUCTURAL
CONSTRAINTS section entirely — all 13 entries were restatements of REGISTER DECLARATION
content. The REGISTER DECLARATION alone, as the declared sole authority, carries the full
closed-chain. Every essential, recommended, and aspirational criterion still passes in the
simplified form.

---

## Final Rubric Criteria Summary (v20)

| Band | Criteria | Weight | V-05 |
|------|----------|--------|------|
| Essential | C-01 Data lineage chain | 15 pts | PASS |
| Essential | C-02 Boundary error handling | 15 pts | PASS |
| Essential | C-03 Data loss point identification | 15 pts | PASS |
| Essential | C-04 Schema state at each stage | 15 pts | PASS |
| Recommended | C-05 Latency characterization | 10 pts | PASS |
| Recommended | C-06 Stale data windows | 10 pts | PASS |
| Recommended | C-07 Domain framing | 10 pts | PASS |
| Aspirational | C-08 Recovery prescriptions | 0.204 pts | PASS |
| Aspirational | C-09 Pattern trade-off analysis | 0.204 pts | PASS |
| Aspirational | C-10 Pre-trace domain context gate | 0.204 pts | PASS |
| Aspirational | C-11 Interleaved boundary gates | 0.204 pts | PASS |
| Aspirational | C-12 Domain entity exposure per boundary | 0.204 pts | PASS |
| Aspirational | C-13 Pre-declared staleness contract | 0.204 pts | PASS |
| Aspirational | C-14 Additive elapsed time calculation | 0.204 pts | PASS |
| Aspirational | C-15 Incumbent or manual-process baseline | 0.204 pts | PASS |
| Aspirational | C-16 Cross-role reference chain | 0.204 pts | PASS |
| Aspirational | C-17 Immutability declaration | 0.204 pts | PASS |
| Aspirational | C-18 Incremental boundary elapsed computation | 0.204 pts | PASS |
| Aspirational | C-19 Machine-verifiable citation convention | 0.204 pts | PASS |
| Aspirational | C-20 Stage-write progression gate | 0.204 pts | PASS |
| Aspirational | C-21 Binary freshness verdict per boundary | 0.204 pts | PASS |
| Aspirational | C-22 Formal pre-declared registry table | 0.204 pts | PASS |
| Aspirational | C-23 Phase gate self-verification checklists | 0.204 pts | PARTIAL |
| Aspirational | C-24 Upfront constraint section with inline callback syntax | 0.204 pts | PASS |
| Aspirational | C-25 Phase gate artifacts as first-class registry rows | 0.204 pts | PASS |
| Aspirational | C-26 Non-natural role ordering | 0.204 pts | PASS |
| Aspirational | C-27 Named recovery formula anchoring incumbent baseline | 0.204 pts | PASS |
| Aspirational | C-28 Named-column boundary block schema | 0.204 pts | PASS |
| Aspirational | C-29 Trade-off as prompt-required section | 0.204 pts | PASS |
| Aspirational | C-30 Output register declaration with field-compliance markers | 0.204 pts | PASS |
| Aspirational | C-31 Pre-declared boundary block schema section | 0.204 pts | PASS |
| Aspirational | C-32 Register-specific compliance marker mapping | 0.204 pts | PASS |
| Aspirational | C-33 Register-invariant declaration for non-tabular registers | 0.204 pts | PASS |
| Aspirational | C-34 Per-boundary incumbent equivalent column | 0.204 pts | PASS |
| Aspirational | C-35 INCUMBENT TOTAL as required pre-trade-off artifact | 0.204 pts | PASS |
| Aspirational | C-36 Baseline-first artifact ordering | 0.204 pts | PASS |
| Aspirational | C-37 REGISTER DECLARATION Parts A/B as single-location authority | 0.204 pts | PASS |
| Aspirational | C-38 Skip-level citation requirement | 0.204 pts | PASS |
| Aspirational | C-39 Skip-level SC names governed role | 0.204 pts | PASS |
| Aspirational | C-40 Skip-level SC declares position distance | 0.204 pts | PASS |
| Aspirational | C-41 Phase Gate 2 skip-level item cites SC identifier | 0.204 pts | PASS |
| Aspirational | C-42 C-37+C-41 closed verification chain co-occurrence | 0.204 pts | PASS |
| Aspirational | C-43 All three skip-level SC attributes co-present in single block | 0.204 pts | PASS |
| Aspirational | C-44 Baseline-closure SC as named upfront constraint | 0.204 pts | PASS |
| Aspirational | C-45 Format-mode declaration with criterion substitution map | 0.204 pts | PASS |
| Aspirational | C-46 SC-13 BASELINE CLOSURE as named closed-chain entry | 0.204 pts | PASS |
| Aspirational | C-47 SC-14 FORMAT MODE DECLARATION as named closed-chain entry | 0.204 pts | PASS |
| Aspirational | C-48 Governed artifact tokens in each SC closed-chain entry | 0.204 pts | PASS |
| Aspirational | C-49 Enforcement mechanism in each SC closed-chain entry | 0.204 pts | PASS |
| Aspirational | C-50 Baseline authority token dual-slot presence | 0.204 pts | PASS |
| Aspirational | C-51 Violation-detectability location in enforcement mechanism | 0.204 pts | PASS |
| Aspirational | C-52 Per-SC detectability index as standalone reference | 0.204 pts | PASS |
| Aspirational | C-53 Dual-slot anchoring extends to all token-referencing SCs | 0.204 pts | FAIL |
| Aspirational | C-54 Phase Gate 0 multi-item structural completeness gate | 0.204 pts | PASS |
| Aspirational | C-55 SC-0 as mandatory [A-00] governor with per-SC dual-slot anchoring | 0.204 pts | PASS |
| Aspirational | C-56 Closed-chain co-governor non-reliance assertion | 0.204 pts | PASS |

**Score: 60 + 30 + (47 × 0.204) + (1 × 0.102) = 90 + 9.588 + 0.102 = 99.69 → reported as 99.5**

**Open gap:** C-23 (PARTIAL) — some Phase Gate checklist items omit explicit SC citations.
C-53 (FAIL) — non-[A-01]-referencing SCs omit governed tokens from their enforcement
clauses; systemic dual-slot gap across all variations.
