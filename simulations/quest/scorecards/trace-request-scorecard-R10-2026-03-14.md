# trace-request — Round 10 Scoring (Rubric v9)

> **Note:** Trace artifact is `placeholder` — no skill output submitted. Scoring is structural: each variation is evaluated on whether its prompt design operationalizes the rubric criteria. Criteria not touched by the variation axis are assumed PASS (baseline conformance from prior rounds).

---

## Rubric Reference (v9 criteria differentiating R10)

| Criterion | Tier | Points | What it tests |
|---|---|---|---|
| C-26 | Aspirational | 5 | Scope-gap Rem# three-way cross-link (Gap?=Y → Rem# → trace boundary) |
| C-27 | Aspirational | 5 | Vocabulary conformance gate (VT# identifiers + D=0 gate before Step 4) |
| C-01 thru C-25 | Ess/Rec/Asp | 180 | All prior criteria (baseline PASS assumed) |

---

## V-01 — Phrasing Register: C-26 Advisory

**Axis:** REQUIRED label removed from scope-gap Rem# cross-link; NOTE replaces mandate in Step 8b + Step 11.

| Criterion | Verdict | Evidence note |
|---|---|---|
| C-01 thru C-25 | PASS | No change to prior criteria; baseline holds |
| **C-26** | **FAIL** | NOTE replaces mandate — advisory wording does not satisfy "every Gap?=Y row wired to Rem# with exact scope string." No DISQUALIFIER triggers; criterion is structurally unenforced |
| **C-27** | **PASS** | Unchanged — VT# identifiers, per-term conformance table, D=0 gate all required |

**Composite:** 185 / 190
**All-essential PASS:** Yes (C-26 is aspirational)
**Rank:** T-2

---

## V-02 — Phrasing Register: C-27 Advisory

**Axis:** Step 3a conformance gate softened; D=0 gate and correction cycle not required.

| Criterion | Verdict | Evidence note |
|---|---|---|
| C-01 thru C-25 | PASS | No change to prior criteria; baseline holds |
| **C-26** | **PASS** | Unchanged — three-way cross-link still REQUIRED |
| **C-27** | **FAIL** | D=0 gate removed as hard requirement; correction cycle optional. C-02 PASS but C-27 FAIL — exactly the design decision note in v9: "precise declaration without a per-term check = C-02 PASS + C-27 FAIL" |

**Composite:** 185 / 190
**All-essential PASS:** Yes (C-27 is aspirational)
**Rank:** T-2

---

## V-03 — Lifecycle Emphasis: Coherence Spine

**Axis:** Step 8b adds REQUIRED explicit three-way coherence confirmation per Gap?=Y boundary before Step 9.

| Criterion | Verdict | Evidence note |
|---|---|---|
| C-01 thru C-25 | PASS | No regression; prior criteria unaffected |
| **C-26** | **PASS** | Three-way cross-link (Step 8a → Step 11 → Step 7/9) enforced by REQUIRED prose confirmation before advancing; coherence spine makes the link mandatory and sequenced |
| **C-27** | **PASS** | Unchanged — VT# + D=0 gate intact |

**Excellence signal ES-1 (V-03):** Prose-confirmation checkpoint at Step 8b acts as a progression gate — the trace cannot advance to Step 9 without explicitly verifying all three link arms for every Gap?=Y boundary. This is structurally stronger than a post-hoc cross-reference.

**Composite:** 190 / 190
**All-essential PASS:** Yes
**Rank:** T-1

---

## V-04 — Output Format: Coherence Table

**Axis:** New Step 8c — Scope String Coherence Table (Step3-Auth / Step8a-Invoked / Step11-Params / Match?) required before Step 9.

| Criterion | Verdict | Evidence note |
|---|---|---|
| C-01 thru C-25 | PASS | No regression; prior criteria unaffected |
| **C-26** | **PASS** | Coherence table provides a cell-verifiable backing structure — each cell independently testable; Match? column makes the cross-link binary and auditable |
| **C-27** | **PASS** | Unchanged — VT# + D=0 gate intact; VT# scope strings now also appear in Step 8c column headers, reinforcing the vocabulary binding |

**Excellence signal ES-2 (V-04):** Step 8c table columns (Step3-Auth / Step8a-Invoked / Step11-Params / Match?) decompose the ES-3 coherence claim into four independently auditable cells per boundary. A reviewer can verify Match? = Y without reading the full prose narrative — machine-verifiable structure.

**Composite:** 190 / 190
**All-essential PASS:** Yes
**Rank:** T-1

---

## V-05 — Combination: V-03 + V-04

**Axis:** Prose coherence confirmation in Step 8b (V-03) + backing Step 8c Match? table (V-04), both required.

| Criterion | Verdict | Evidence note |
|---|---|---|
| C-01 thru C-25 | PASS | No regression; prior criteria unaffected |
| **C-26** | **PASS** | Strongest evidence: prose confirmation AND table both required; if prose says "coherent" but Match? = N, the contradiction is itself a structural signal — two representations cannot both pass with divergent values |
| **C-27** | **PASS** | VT# scope strings must appear consistently in both Step 8b prose and Step 8c column values — dual-surface vocabulary binding |

**Excellence signal ES-3 (V-05 only):** Mismatch between inline prose confirmation and Step 8c Match? = N is a structural signal that neither representation alone could surface. V-05 is the first variation where coherence failure is detectable from format alone, without semantic reading of the prose.

**Composite:** 190 / 190
**All-essential PASS:** Yes
**Rank:** T-1 (structural depth edge over V-03/V-04 individually)

---

## Variation Ranking

| Rank | Variation | Score | C-26 | C-27 | Differentiator |
|---|---|---|---|---|---|
| T-1 | V-05 | 190/190 | PASS | PASS | Prose + table cross-validation; detectable mismatch |
| T-1 | V-03 | 190/190 | PASS | PASS | Progression gate at Step 8b |
| T-1 | V-04 | 190/190 | PASS | PASS | Cell-verifiable table structure |
| T-2 | V-01 | 185/190 | FAIL | PASS | C-26 unenforced (advisory only) |
| T-2 | V-02 | 185/190 | PASS | FAIL | C-27 unenforced (gate removed) |

---

## Excellence Signals (R10)

**ES-1:** Prose-confirmation checkpoint as a progression gate — sequenced enforcement prevents advance without explicit coherence verification per boundary.

**ES-2:** Scope String Coherence Table decomposes the cross-link into four independently auditable cells; Match? column makes the criterion machine-verifiable.

**ES-3 (V-05 only):** Dual-surface representation (prose + table) makes coherence failure detectable from structural mismatch alone — a pattern not surfaceable with either representation individually.

---

## C-28 Promotion Signal

R10 confirms both C-26 and C-27 load-bearing (V-01/V-02 regressions show 5-point loss each). V-03/V-04/V-05 all produce consistent ES-3 evidence for the VT# scope string propagation claim across Step 3 → Step 8a → Step 11. C-28 promotion conditions are met: two confirmed load-bearing criteria + multi-round ES-3 evidence from three independent structural expressions.

---

```json
{"top_score": 190, "all_essential_pass": true, "new_patterns": ["Prose-confirmation progression gate at Step 8b enforces three-way coherence per Gap?=Y boundary before Step 9 advance", "Scope String Coherence Table (Step3-Auth / Step8a-Invoked / Step11-Params / Match?) decomposes cross-link into four independently auditable cells per boundary", "Dual-surface representation (prose confirmation + Match? table) makes coherence failure detectable from structural mismatch alone — neither surface alone can surface the contradiction"]}
```
