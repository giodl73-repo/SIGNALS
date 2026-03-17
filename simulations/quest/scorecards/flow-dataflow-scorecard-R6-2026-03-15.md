## flow-dataflow — Round 6 Scoring (Rubric v5)

---

### Axis Coverage Recap

| Axis | V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|------|
| Trigger IDs (NH-NN/LP-NN) | yes | no | no | no | yes |
| Stage-exit entity declaration | no | yes | no | no | yes |
| Boundary latency decomposed | no | no | yes | no | no |
| Verification index | no | no | no | yes | yes |
| Recovery audit table (C-18 structured) | 5-col | prose | prose | prose | 6-col |

---

### Essential Criteria (C-01–C-04)

All five variations fully structure their output around a 6-stage pipeline with explicit source → stage(s) → destination chains (C-01), a boundary table with an Error Handling column requiring a mechanism or explicit "no handling" flag (C-02), a named concrete loss point required at every stage (C-03), and per-stage input schema / transformation / output schema with `verified: no field added, removed, renamed, or retyped` for unchanged stages (C-04).

**All 5 variations: C-01 PASS · C-02 PASS · C-03 PASS · C-04 PASS**

---

### Recommended Criteria (C-05–C-07)

- **C-05 (latency per stage)** — every variation requires latency annotation as a mandatory stage item. PASS all.
- **C-06 (stale windows)** — every variation includes a stale accumulation section with both normal-operation and worst-case failure-mode staleness assessed separately, plus a mid-pipeline consumer staleness window. PASS all.
- **C-07 (domain framing)** — all variations pre-enumerate rich domain entity vocabularies: V-01 (ExpenseClaim, ReceiptImage, OCRReceiptRecord…), V-02 (PurchaseOrder, GoodsReceiptNote…), V-03 (SubledgerJournalEntry, ConsolidationLedger…), V-04 (CreditApplication, CreditBureauReport…), V-05 (UsageEvent, CDRRecord, RatedLineItem…). PASS all.

**All 5 variations: C-05 PASS · C-06 PASS · C-07 PASS**

---

### Aspirational Criteria (C-08–C-19)

#### C-08 — Recovery prescriptions

Every variation requires a paired recovery prescription for every NH annotation and every loss point, naming the specific mechanism, the protected entity, and an MS-NN step citation. Prose format for V-02/V-03/V-04 satisfies coverage (paired, specific, named). **PASS all**.

#### C-09 — Pattern trade-off analysis

All variations require a named alternative architecture with ≥2 trade-off dimensions, one of which must compare automated pipeline total against INCUMBENT TOTAL. **PASS all**.

#### C-10 — Pre-trace entity inventory

All variations pre-enumerate all in-scope entities in a dedicated inventory step (SECTION 1 / STEP 1 / DOMAIN CONTEXT) before any stage is traced. **PASS all**.

#### C-11 — Systematic boundary labeling

All boundary tables use B1→2 through B5→6 labels forming a complete inventory. V-01 and V-05 additionally require NH-NN annotations to reference these labels by name. **PASS all**.

#### C-12 — Verified-unchanged schema assertion

All variations require the exact phrase `verified: no field added, removed, renamed, or retyped` for any stage asserting schema identity. **PASS all**.

#### C-13 — Structural completeness enforcement

- V-01: Recovery Audit Table (SECTION 6) — blank row = visible C-08 gap; maps to C-02 (NH annotations) and C-03 (LP loss points). PASS.
- V-02: Boundary table — "all six columns required, blank cell = structural gap"; maps to C-02. PASS.
- V-03: 7-column boundary table with decomposed latency — blank cell = structural gap; maps to C-02. PASS.
- V-04: Boundary table + Verification Index — two independent structural surfaces. PASS.
- V-05: Boundary table + Recovery Audit Table + Verification Index — three surfaces. PASS.

**PASS all**.

#### C-14 — Incumbent baseline anchoring

All variations require MS-NN Step ID citations in recovery prescriptions, grounding fallback in the named pre-automation process (expense coordinator, AP clerk, controller, credit analyst, billing analyst) rather than generic "manual review." **PASS all**.

#### C-15 — Structured incumbent baseline table

All variations include a 4-column INCUMBENT BASELINE TABLE (Step ID | Manual Step | Actor | Duration) with ≥5 domain-specific steps and a declared INCUMBENT TOTAL. **PASS all**.

#### C-16 — Full recovery-to-baseline traceability

- V-01/V-05: Explicit "Step ID Cited (MS-NN)" column in recovery audit table — blank cell is a visible C-16 gap per row. V-05 additionally requires "Manual Step Cited (exact value from STEP 0, verbatim)." **PASS**.
- V-02/V-03/V-04: "Every recovery entry must carry an MS-NN citation" stated as a mandatory prose requirement. **PASS**.

**PASS all**.

#### C-17 — Entity-at-risk annotation per boundary

All variations include an "Entity at Risk" column in the boundary table requiring a named entity from the inventory. Enforcement quality varies but pass condition is met:

| Variation | C-17 Enforcement | Result |
|-----------|-----------------|--------|
| V-01 | Must be drawn from SECTION 1 inventory | PASS |
| V-02 | Must be drawn from preceding stage-exit declaration (strongest traceability) | PASS |
| V-03 | Must be drawn from SECTION 1 inventory | PASS |
| V-04 | Must be from SECTION 1 inventory + verification index cross-checks it | PASS |
| V-05 | Must be from preceding stage-exit declaration + verification index cross-checks | PASS (highest verifiability) |

**PASS all**.

#### C-18 — Structured recovery audit table

This is the decisive differentiator this round.

| Variation | Recovery Section Format | C-18 Result |
|-----------|------------------------|-------------|
| V-01 | 5-column audit table: Trigger ID \| Triggering Condition \| Recovery Mechanism \| Step ID Cited \| Manual Step Cited — every NH-NN and LP-NN must have a row; blank row = visible gap | **PASS** |
| V-02 | Prose recovery prescriptions — numbered entry format but no table structure | **FAIL** — "prose recovery section does not qualify" |
| V-03 | Prose recovery prescriptions — same structure as V-02 | **FAIL** |
| V-04 | Prose recovery prescriptions (Section 5) + verification index (Section 6, but index has "Recovery Refs" column not triggering condition / mechanism columns) | **FAIL** — index is a cross-reference table, not the recovery table; C-18 requires triggering condition + recovery mechanism + boundary reference as columns |
| V-05 | 6-column audit table: Trigger ID \| Triggering Condition \| Recovery Mechanism \| Named Entity Protected \| Step ID Cited \| Manual Step Cited — explicit C-18 instruction: "every NH-NN and LP-NN declared must have a row — a missing row is a structural C-18 gap" | **PASS** |

#### C-19 — Per-boundary latency annotation

All variations include a Boundary Latency column in the boundary table. V-03 exceeds the requirement with Transport Latency + Processing Overhead + Total Boundary Latency sub-columns, and SECTION 4 uses per-component addends. **PASS all**.

---

### Per-Variation Score

| Criterion | Tier | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|------|
| C-01 | Essential | PASS | PASS | PASS | PASS | PASS |
| C-02 | Essential | PASS | PASS | PASS | PASS | PASS |
| C-03 | Essential | PASS | PASS | PASS | PASS | PASS |
| C-04 | Essential | PASS | PASS | PASS | PASS | PASS |
| C-05 | Recommended | PASS | PASS | PASS | PASS | PASS |
| C-06 | Recommended | PASS | PASS | PASS | PASS | PASS |
| C-07 | Recommended | PASS | PASS | PASS | PASS | PASS |
| C-08 | Aspirational | PASS | PASS | PASS | PASS | PASS |
| C-09 | Aspirational | PASS | PASS | PASS | PASS | PASS |
| C-10 | Aspirational | PASS | PASS | PASS | PASS | PASS |
| C-11 | Aspirational | PASS | PASS | PASS | PASS | PASS |
| C-12 | Aspirational | PASS | PASS | PASS | PASS | PASS |
| C-13 | Aspirational | PASS | PASS | PASS | PASS | PASS |
| C-14 | Aspirational | PASS | PASS | PASS | PASS | PASS |
| C-15 | Aspirational | PASS | PASS | PASS | PASS | PASS |
| C-16 | Aspirational | PASS | PASS | PASS | PASS | PASS |
| C-17 | Aspirational | PASS | PASS | PASS | PASS | PASS |
| C-18 | Aspirational | **PASS** | **FAIL** | **FAIL** | **FAIL** | **PASS** |
| C-19 | Aspirational | PASS | PASS | PASS | PASS | PASS |
| **Aspirational pass** | | 12/12 | 11/12 | 11/12 | 11/12 | 12/12 |

### Composite Scores

```
composite = (essential_pass/4 × 60) + (recommended_pass/3 × 30) + (aspirational_pass/12 × 10)

V-01: (4/4 × 60) + (3/3 × 30) + (12/12 × 10) = 60 + 30 + 10.00 = 100
V-02: (4/4 × 60) + (3/3 × 30) + (11/12 × 10) = 60 + 30 +  9.17 =  99
V-03: (4/4 × 60) + (3/3 × 30) + (11/12 × 10) = 60 + 30 +  9.17 =  99
V-04: (4/4 × 60) + (3/3 × 30) + (11/12 × 10) = 60 + 30 +  9.17 =  99
V-05: (4/4 × 60) + (3/3 × 30) + (12/12 × 10) = 60 + 30 + 10.00 = 100
```

### Ranking

| Rank | Variation | Score | Notes |
|------|-----------|-------|-------|
| 1 | **V-05** | 100 | All axes combined — stage-exit entity + trigger IDs + 6-col recovery table + verification index with self-correction; broadest structural enforcement surface |
| 1 | **V-01** | 100 | Trigger IDs alone produce C-18 compliance; simpler structure but equally complete on rubric criteria |
| 3 | **V-04** | 99 | Verification index achieves C-17/C-19/C-16 co-visibility but recovery remains prose — C-18 gap; self-correction mandate is valuable but can't compensate |
| 3 | **V-02** | 99 | Stage-exit declaration improves C-17 traceability quality; C-18 gap from prose recovery |
| 3 | **V-03** | 99 | Latency decomposition adds structural depth to C-19 beyond rubric floor; C-18 gap from prose recovery |

V-05 is ranked first over V-01 despite equal rubric scores: it has the stage-exit entity declaration (prevents ad-hoc entity invention at boundary time), the 6-column recovery audit table with the verbatim Manual Step Cited column (tighter C-16 enforcement), and the verification index with self-correction mandate (co-visibility surface not present in V-01). V-01 achieves the same rubric score with a simpler structure — it is a viable golden if V-05's structural density proves to crowd out lineage prose.

---

### Excellence Signals from V-05

**1. Stage-exit entity forward declaration as C-17 chain anchor.** Each stage closes with "Entities exiting Stage N: [list from inventory]" before the downstream boundary annotation is written. The boundary's Entity at Risk column must choose from that declared set — not from the global inventory directly. This two-step constraint (inventory → stage-exit → boundary) prevents the entity quality degradation where an LLM names a plausible-sounding entity at boundary time that was never grounded in the stage's processing context.

**2. NH-NN/LP-NN pre-numbering makes C-18 row-completeness machine-verifiable.** Assigning identifiers at the point of declaration (not retrospectively during recovery table construction) creates citation targets. Every NH-NN and LP-NN declared is a recovery table row that either exists with the matching Trigger ID or is an unambiguous structural gap. This eliminates the paraphrase ambiguity problem where a recovery row's prose description may or may not address a specific NH annotation.

**3. Verification index self-correction mandate as a structural self-healing pattern.** The instruction "if any status reports a gap, correct it in the relevant upstream step before finalizing the index" combines a diagnostic surface (one row per boundary, all criteria co-visible) with a behavioral instruction that triggers backfill. This is the first enforcement pattern in the rubric series that asks the generator to self-audit and repair before declaring completion — operating as a protocol gate rather than a passive summary.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Stage-exit entity forward declaration as C-17 enforcement mechanism — declaring entities exiting each stage before the downstream boundary annotation constrains entity-at-risk selection to a traceable declared set, preventing ad-hoc entity invention at boundary annotation time", "Verification index self-correction mandate — requiring the generator to backfill upstream gaps discovered during post-trace index construction introduces a structural self-healing loop not captured by any existing rubric criterion"]}
```
