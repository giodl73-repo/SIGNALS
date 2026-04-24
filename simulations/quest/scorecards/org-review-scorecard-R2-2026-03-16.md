# org-review Variations R14 / Quest Round 2 — Scoring (v11 rubric)

## Baseline Inherited from V-05 R13

All five variations inherit the complete V-05 R13 template, which confirmed PASS on C-01 through C-32 (210 pts) plus C-35 via §17 NULL HYPOTHESIS DIMENSION TABLE (+5 = 215 pts). The §17 block is present and pre-committed in the V-01 file (confirmed at lines 236–258). All base criteria reviewed below without re-deriving; only delta criteria (C-33, C-34) are contested.

---

## Per-Variation Scoring

### V-01 — Inline Applicability Tier in §15

**Delta criteria:**
- **C-33 (Lens Applicability Rating Pre-committed)**: PASS. §15 LENS COVERAGE TABLE gains a 4th "Artifact Applicability" column. Tier rules (HIGH/MEDIUM/LOW with outcome implications) are stated inside §15 itself — the table header acts as a pre-committed definition. Each row carries an artifact-specific rating before Status is assigned. Evidence: `| # | lens.verify Entry | Artifact Applicability | Status | Finding Reference |` + tier definitions printed inline.
- **C-34 (ADVISORY-GAP Domain Coverage Pre-committed)**: FAIL. No §10a domain gap-check protocol. No second sub-table in §5.5. The applicability ratings exist per-lens in §15 but nothing aggregates them domain-inward to flag uncovered artifact domains. C-31 active → C-34 not vacuous → FAIL.
- **C-35**: PASS (inherited §17).

| Criterion | Result | Pts |
|-----------|--------|-----|
| C-01–C-05 Essential | 5× PASS | 60 |
| C-06–C-08 Recommended | 3× PASS | 30 |
| C-09–C-32 Aspirational base | 24× PASS | 120 |
| C-33 | PASS (inline §15 column) | 5 |
| C-34 | FAIL (no domain gap-check) | 0 |
| C-35 | PASS (§17 inherited) | 5 |
| **Total** | | **220 / 225** |

---

### V-02 — ROLE MANIFEST Applicability Pre-Rating

**Delta criteria:**
- **C-33**: PASS. APPLICABILITY MATRIX in ROLE MANIFEST declares `Row ID | Role | lens.verify Entry | Artifact Domain Covered | Artifact Applicability | Basis for Rating` before any reviewer section runs. §15 cites matrix by row ID (`AM-0n: [tier]`). Rating is locked at manifest time — retroactive LOW assignment is structurally prevented. This is a stronger encoding than V-01.
- **C-34**: FAIL. V-02 is a single-axis variation. The APPLICABILITY MATRIX includes "Artifact Domain Covered" column but no domain-inward gap-check step follows; no §10a protocol; no §5.5 sub-table for ADVISORY-GAP domain classification. C-31 active → not vacuous → FAIL.
- **C-35**: PASS (inherited §17).

| Criterion | Result | Pts |
|-----------|--------|-----|
| C-01–C-05 Essential | 5× PASS | 60 |
| C-06–C-08 Recommended | 3× PASS | 30 |
| C-09–C-32 Aspirational base | 24× PASS | 120 |
| C-33 | PASS (MANIFEST pre-rating) | 5 |
| C-34 | FAIL (no domain gap-check) | 0 |
| C-35 | PASS (§17 inherited) | 5 |
| **Total** | | **220 / 225** |

---

### V-03 — §5.5 Domain Gap-Check Extension

**Delta criteria:**
- **C-33**: FAIL. §15 LENS COVERAGE TABLE has no Artifact Applicability column. V-03 is a single-axis variation targeting C-34 only. C-31 active → C-33 not vacuous → FAIL.
- **C-34**: PASS. §10a DOMAIN COVERAGE GAP-CHECK PROTOCOL is pre-committed in the IMMUTABLE block. §5.5 gains a second sub-table: `| Artifact Domain | Reviewer(s) with HIGH Applicability | Coverage |`. Domains with no HIGH-applicability reviewer are classified ADVISORY-GAP and promoted to the ACTION ITEM REGISTER. The §5.5 section already sits after BRACKET CLOSING per §7. §10a defines its own role-level applicability framework (independent of C-33's per-lens ratings). C-34 pass condition requires pre-committed gap-check with ADVISORY-GAP promotion — both satisfied. Note: the vacuous condition for C-34 is "C-31 inactive OR no multi-domain artifact" — C-33 FAIL does **not** make C-34 vacuous per rubric scoring key.
- **C-35**: PASS (inherited §17).
- **C-25 (non-verdict section excluded from gate ledger)**: §5.5 is already listed under §6 EXCLUDED — the sub-table addition does not introduce a new verdict-emitting section. PASS preserved.

| Criterion | Result | Pts |
|-----------|--------|-----|
| C-01–C-05 Essential | 5× PASS | 60 |
| C-06–C-08 Recommended | 3× PASS | 30 |
| C-09–C-32 Aspirational base | 24× PASS | 120 |
| C-33 | FAIL (no §15 applicability column) | 0 |
| C-34 | PASS (§10a + §5.5 gap-check) | 5 |
| C-35 | PASS (§17 inherited) | 5 |
| **Total** | | **220 / 225** |

---

### V-04 — Combined: ROLE MANIFEST Applicability + §5.5 Domain Gap-Check

**Delta criteria:**
- **C-33**: PASS. V-02 encoding: ROLE MANIFEST APPLICABILITY MATRIX with `Artifact Domain Covered` column. §15 cites matrix by row ID. Applicability locked before any reviewer section executes.
- **C-34**: PASS. V-03 encoding: §10a + §5.5 domain gap-check. Crucially, the gap-check now references the APPLICABILITY MATRIX directly by domain — the "Artifact Domain Covered" column in the MANIFEST maps cleanly to the domain gap-check rows. This is the strongest form of C-34: HIGH-applicability determination is sourced from the pre-committed matrix rather than editorial judgment at §5.5 fill time.
- **C-35**: PASS (inherited §17).
- **Cross-section integrity**: MANIFEST → §15 (C-33) and MANIFEST → §5.5 (C-34) both source from the same matrix. Single source of truth prevents divergent applicability ratings at the two consumption points.

| Criterion | Result | Pts |
|-----------|--------|-----|
| C-01–C-05 Essential | 5× PASS | 60 |
| C-06–C-08 Recommended | 3× PASS | 30 |
| C-09–C-32 Aspirational base | 24× PASS | 120 |
| C-33 | PASS (MANIFEST pre-rating) | 5 |
| C-34 | PASS (§5.5 gap-check sourced from MANIFEST) | 5 |
| C-35 | PASS (§17 inherited) | 5 |
| **Total** | | **225 / 225** |

---

### V-05 — Full Integration (V-04 + Explicit Traceability Chain)

**Delta criteria:**
- **C-33**: PASS. Same V-02/V-04 mechanism. APPLICABILITY MATRIX in ROLE MANIFEST.
- **C-34**: PASS. Same V-03/V-04 mechanism. §10a + §5.5 sub-table referencing MANIFEST.
- **C-35**: PASS. §17 inherited and explicitly cited in the traceability chain documentation.
- **Additional structural quality**: Explicit chain `ROLE MANIFEST APPLICABILITY MATRIX → §15 LENS COVERAGE TABLE [C-33] → §5.5 DOMAIN COVERAGE GAP-CHECK [C-34]` printed in the preamble. This makes the information flow auditable without reading reviewer sections. Does not activate new rubric criteria (all 35 already PASS) but reduces the chance of a reviewer treating any step as optional. DISPOSITION_CONTRACT stays at §17 — no §18/§19 overhead.

| Criterion | Result | Pts |
|-----------|--------|-----|
| C-01–C-05 Essential | 5× PASS | 60 |
| C-06–C-08 Recommended | 3× PASS | 30 |
| C-09–C-32 Aspirational base | 24× PASS | 120 |
| C-33 | PASS (MANIFEST pre-rating, cited in chain) | 5 |
| C-34 | PASS (§5.5 gap-check, cited in chain) | 5 |
| C-35 | PASS (§17 inherited, cited in chain) | 5 |
| **Total** | | **225 / 225** |

---

## Composite Ranking

| Rank | Variation | C-33 | C-34 | C-35 | Score | Band |
|------|-----------|:----:|:----:|:----:|-------|------|
| **1** | **V-04** | PASS | PASS | PASS | **225 / 225** | Gold |
| **1** | **V-05** | PASS | PASS | PASS | **225 / 225** | Gold |
| 3 | V-01 | PASS | FAIL | PASS | 220 / 225 | Gold |
| 3 | V-02 | PASS | FAIL | PASS | 220 / 225 | Gold |
| 3 | V-03 | FAIL | PASS | PASS | 220 / 225 | Gold |

All five variations exceed the Gold threshold (190 pts) and all essential criteria PASS across all variations.

**V-04 vs V-05 tie-break (non-scoring)**: V-05 is structurally superior. The explicit traceability chain (`MANIFEST → §15 → §5.5`) makes cross-section applicability consistency auditable at a glance without reading reviewer narrative. V-05 is the recommended canonical form; V-04 achieves the same score with slightly weaker documentation of the information flow.

---

## Excellence Signals

Patterns from V-04 and V-05 that produce 225/225 vs. 220/225 in V-01/V-02/V-03:

**1. Combined axes are required** — No single-axis variation achieves 225/225. C-33 and C-34 require orthogonal structural additions (per-lens column + domain gap-check). V-01/V-02/V-03 each satisfy one; V-04/V-05 satisfy both. There is no minimum-effort path to 225.

**2. Front-loading applicability in ROLE MANIFEST** — V-02/V-04/V-05 lock applicability ratings before any reviewer section runs. V-01's inline approach (rates within §15 during fill) carries retroactive-assignment risk: a reviewer may assign LOW to avoid ADVISORY-OPEN-LENS entries. The MANIFEST pre-rating removes that editorial step.

**3. Single source of truth across C-33 and C-34** — V-04/V-05 source both §15 applicability ratings (C-33) and §5.5 domain gap-check (C-34) from the same APPLICABILITY MATRIX. This prevents divergent applicability ratings: the same role cannot be rated HIGH in §15 but absent from the domain gap-check, or vice versa.

**4. Embedding gap-check in existing §5.5** — V-03/V-04/V-05 extend §5.5 with a domain gap-check sub-table rather than adding §18/§19 as new IMMUTABLE contract sections (R13 approach). The DISPOSITION_CONTRACT stays at §17. Fewer contract sections means lower risk of an AI treating a section as optional; §5.5 is already present and required.

---

```json
{"top_score": 225, "all_essential_pass": true, "new_patterns": ["Front-loading applicability in ROLE MANIFEST before any reviewer section runs prevents retroactive LOW assignments and locks ratings as a pre-committed constraint", "Single source of truth: APPLICABILITY MATRIX in ROLE MANIFEST serves as input to both §15 LENS COVERAGE TABLE (C-33) and §5.5 domain gap-check (C-34), creating a forward-traceable chain with no divergence risk", "Embedding domain gap-check as §5.5 sub-table (§10a protocol) avoids new IMMUTABLE contract sections; DISPOSITION_CONTRACT stays at §17 with no §18/§19 overhead"]}
```
