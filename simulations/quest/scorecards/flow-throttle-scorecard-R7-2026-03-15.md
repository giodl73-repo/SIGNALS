Now I have a complete picture of all five variations. Let me score them.

---

## flow-throttle — Round 7 Scorecard (v7 Rubric)

**Date:** 2026-03-16 | **Skill:** `flow:throttle` | **Rubric:** v7 (C-01–C-22, max 160)

---

### Scoring Formula

```
Composite = (essential_pass / 5 × 60)
          + (recommended_pass / 3 × 30)
          + (aspirational_pass / 14 × 70)
```

PARTIAL = 2.5 pts. All 5 variations inherit baseline: C-01–C-19 all PASS (11 aspirational).

---

### V-01 — C-20 Only: Prose-Restriction Declaration

**Structural additions:** `PROSE-RESTRICTION DECLARATION (C-20)` block at top, labeled, before TABLE A. Closed 4-item list (load-shape verdict, escape-route frame, UNIFORM/BURST narrative, self-verification note). Closing audit cross-references the declaration.

| Criterion | Verdict | Evidence |
|-----------|---------|---------|
| C-01 | PASS | Primary bottleneck with causal reason — TABLE A Binding at band + Load-shape verdict |
| C-02 | PASS | TABLE B minimum 2 hops with named mechanism |
| C-03 | PASS | TABLE A Tier-ID rows with Component + Scope |
| C-04 | PASS | TABLE C one row per TABLE A tier |
| C-05 | PASS | TABLE D unprotected burst paths |
| C-06 | PASS | TABLE C Retry-After columns + Step 2F assessment |
| C-07 | PASS | Step 2E cascade minimum 3 tiers |
| C-08 | PASS | TABLE A Limit (number + unit) column |
| C-09 | PASS | TABLE F MR-01, MR-02 with parameter names |
| C-10 | PASS | Load-shape verdict with numeric differential |
| C-11 | PASS | Tier-ID referential chain from TABLE A |
| C-12 | PASS | CLOSING AUDIT section |
| C-13 | PASS | Step 1A gate closed before Step 2; evidence base locked |
| C-14 | PASS | Binding at band N/A entries for non-binding tiers |
| C-15 | PASS | Step 1A → 1B → 2 phase sequence with role lock |
| C-16 | PASS | REGISTRY GAP PROHIBITION statements at each Step 2 section |
| C-17 | PASS | "One row per TABLE A Tier-ID. No tier SHALL be omitted." in phase entry conditions |
| C-18 | PASS | Escape-route frame names deferral temptation + rejection mechanism |
| C-19 | PASS | CLOSING AUDIT names C-01 through C-08 by category |
| **C-20** | **PASS** | Labeled block, closed 4-item list, positioned before TABLE A, closing audit back-references it |
| **C-21** | **FAIL** | No italic `*[TABLE X — Source: ...]` header lines on derived tables. Coverage obligations appear in PHASE ENTRY CONDITION prose, not as table-level headers that travel with the artifact. |
| **C-22** | **FAIL** | No Type column in any table; mitigation table has no failure-category taxonomy |

**Aspirational PASS:** 12/14 → 12 × 5 = 60 pts
**Composite: 60 + 30 + 60 = 150**

---

### V-02 — C-21 Only: Cross-Artifact Referential Integrity

**Structural additions:** Italic `*[TABLE X — Source: TABLE A. Coverage obligation...]*` header lines on every derived table: TABLE A (primary artifact declaration), TABLE B, TABLE C, TABLE D, RANKING, CASCADE, RETRY-AFTER, LOAD SHAPE, TABLE F.

| Criterion | Verdict | Evidence |
|-----------|---------|---------|
| C-01–C-19 | PASS | Same as V-01 baseline |
| **C-20** | **FAIL** | No prose-restriction declaration block. Prompt has no labeled closed-list of permitted prose contexts. |
| **C-21** | **PASS** | Every derived artifact has an italic header line naming source by identifier and stating row-count/coverage constraint. TABLE C: "One row per T-NN from TABLE A. No tier may be omitted. No tier absent from TABLE A may be added. Row count in TABLE C MUST equal row count in TABLE A." TABLE F: "Source: TABLE A. Component column SHALL reference T-NN or component name from TABLE A. Minimum 2 rows." Constraint travels with artifact, not just in surrounding text. |
| **C-22** | **FAIL** | No Type column; no failure-mode taxonomy |

**Aspirational PASS:** 12/14 → 60 pts
**Composite: 60 + 30 + 60 = 150**

---

### V-03 — C-22 Only: Typed-Row Risk Taxonomy

**Structural additions:** Step 2G2 inserts TABLE E (Risk Inventory) with Type column (Burst/Cascade/RetryAfter), TYPE SCAN GATE requiring explicit confirmation of all three types before Step 2H. TABLE F derives from TABLE E, stated in prose before the table.

| Criterion | Verdict | Evidence |
|-----------|---------|---------|
| C-01–C-19 | PASS | Same as baseline |
| **C-20** | **FAIL** | No labeled prose-restriction declaration |
| **C-21** | **PARTIAL** | TABLE F has an adjacent prose statement "TABLE F derives from TABLE E. One row per Risk-ID from TABLE E. No risk may be omitted." — this names the upstream source and states the coverage obligation, satisfying the semantic requirement. However, it is not formatted as a `*[TABLE F — Source: TABLE E...]*` header line that travels with the table; it appears as paragraph prose before the table. Other derived tables (TABLE B, TABLE C, TABLE D, etc.) have no source headers at all. Partial coverage of the C-21 form requirement. |
| **C-22** | **PASS** | TABLE E has Type column with closed taxonomy (Burst/Cascade/RetryAfter). TYPE SCAN GATE explicitly requires confirmation of all three types: "(a) at least one Burst row present; (b) at least one Cascade row present; (c) at least one RetryAfter row present." Pre-populated template rows demonstrate the expected types. Count requirement (≥2 mitigations via C-09) cannot satisfy C-22 because type scan detects homogeneous rows. |

**Aspirational PASS:** 11 PASS × 5 + 1 PARTIAL × 2.5 = 57.5 + 5 (C-22) = 62.5 pts
**Composite: 60 + 30 + 62.5 = 152.5 ≈ 153**

---

### V-04 — Combined: C-20 + C-21

**Structural additions:** C-20 declaration block at top (same as V-01) + C-21 italic header lines on every derived table (same as V-02). Closing audit back-references the declaration.

| Criterion | Verdict | Evidence |
|-----------|---------|---------|
| C-01–C-19 | PASS | Same as baseline |
| **C-20** | **PASS** | Labeled `PROSE-RESTRICTION DECLARATION (C-20)` block, closed 4-item list, before TABLE A. Closing audit references it: "prose permitted here per the Prose-Restriction Declaration." |
| **C-21** | **PASS** | Every derived table has `*[TABLE X — Source: TABLE A...]*` italic header line. TABLE C: "One row per T-NN from TABLE A. No tier may be omitted. No tier absent from TABLE A may be added. Row count in TABLE C MUST equal row count in TABLE A." TABLE F: "Source: TABLE A. Component column SHALL reference T-NN or component name from TABLE A. Minimum 2 rows. No component absent from TABLE A may appear." Full artifact-level lineage. |
| **C-22** | **FAIL** | No Type column; no failure-mode taxonomy in any table |

**Aspirational PASS:** 13/14 → 13 × 5 = 65 pts
**Composite: 60 + 30 + 65 = 155**

---

### V-05 — Combined: C-20 + C-21 + C-22 (All Three)

**Structural additions:** C-20 declaration (same) + C-21 headers on every table including NEW tables D2/E1/E2/E3/F (C-21 headers include failure-mode annotations) + C-22 TABLE E3 with TYPE SCAN GATE. Sections 2D (ranking), 2E (cascade), 2F (retry-after) promoted from prose to tables. TABLE F cites TABLE E3, not TABLE A, creating a transitive lineage chain.

| Criterion | Verdict | Evidence |
|-----------|---------|---------|
| C-01–C-19 | PASS | Same as baseline; cascade (TABLE E1), retry-after (TABLE E2), ranking (TABLE D2) promoted to tables further strengthen C-07, C-06, C-04 |
| **C-20** | **PASS** | Labeled declaration block, closed 4-item list. Prose sections (load-shape verdict, escape-route frame, UNIFORM/BURST narrative, self-verification note) are the only permitted contexts. Sections 2D/2E/2F promoted to tables, removing 3 former prose sections from outside the declared exception list — tightening compliance. |
| **C-21** | **PASS** | Every derived artifact has a `*[TABLE X — Source: ...]` italic header with failure-mode annotation: TABLE B "— Prevents scope creep into the backpressure trace", TABLE C "— Prevents coverage elision in the UX artifact", TABLE D "— Prevents burst analysis from introducing undeclared tiers", TABLE D2 "— Prevents ranking from silently dropping lower-risk tiers", TABLE E1/E2 with TABLE A sourcing, TABLE E3 "— Prevents mitigation drift by inserting a typed intermediary artifact", TABLE F "— Prevents mitigation coverage drift from the typed risk inventory." C-21 + C-18 are merged: header line states source *and* names the failure mode the constraint prevents. |
| **C-22** | **PASS** | TABLE E3 with Type column, closed Burst/Cascade/RetryAfter taxonomy, TYPE SCAN GATE with three explicit type-presence checks. Pre-populated template rows show one of each type. Transitive routing: TABLE F derives from TABLE E3 (not TABLE A), so TABLE F's row-count obligation propagates through the typed inventory — category-level gap in TABLE E3 produces a detectable gap in TABLE F. |

**Aspirational PASS:** 14/14 → 70 pts
**Composite: 60 + 30 + 70 = 160**

---

### Final Rankings

| Rank | Variation | Composite | C-20 | C-21 | C-22 | All Essential |
|------|-----------|-----------|------|------|------|---------------|
| 1 | **V-05** | **160/160** | PASS | PASS | PASS | YES |
| 2 | **V-04** | **155/160** | PASS | PASS | FAIL | YES |
| 3 | **V-03** | **153/160** | FAIL | PARTIAL | PASS | YES |
| 4 | **V-01** | **150/160** | PASS | FAIL | FAIL | YES |
| 4 | **V-02** | **150/160** | FAIL | PASS | FAIL | YES |

---

### Excellence Signals (V-05)

**1. Failure-mode annotation fused into table headers (C-18 × C-21 synthesis)**
V-05's header lines combine the C-21 lineage constraint with a C-18 failure-mode annotation: `*[TABLE C — Source: TABLE A. One row per T-NN... — Prevents coverage elision in the UX artifact.]*` Each header becomes self-explanatory — it states where data comes from AND why the constraint exists. A reader can verify compliance without reconstructing the analysis. This is the first variation to merge two previously independent criteria into a single header line.

**2. Transitive artifact lineage chain (TABLE A → TABLE E3 → TABLE F)**
Inserting TABLE E3 (typed risk inventory) as an intermediate artifact changes TABLE F's source reference from TABLE A to TABLE E3. C-21 now propagates transitively: a gap in TABLE A (missing tier) produces a gap in TABLE E3 (missing Tier-ID), which produces a gap in TABLE F (missing mitigation row). This multi-hop lineage check is architecturally cleaner than each table independently citing TABLE A — it follows the actual dependency structure of the analysis.

**3. Prose-section promotion collapses C-20 exception surface**
V-05 converts sections 2D (ranking), 2E (cascade), 2F (retry-after) from prose to tables (TABLE D2, TABLE E1, TABLE E2). This reduces the number of prose sections that need to be listed in the C-20 declaration, shrinking the exception surface from four items to one (load-shape verdict + escape-route frame, UNIFORM/BURST narrative, self-verification note). The declaration becomes more auditable because fewer permitted contexts mean fewer places to check for format violations.

**4. Pre-populated type rows enforce C-22 by template**
TABLE E3's template pre-populates `Type = Burst`, `Type = Cascade`, `Type = RetryAfter` in the first three rows. An executor filling in the table must override a default type assignment, not supply one from memory. This makes the TYPE SCAN GATE checkable from the template structure — category absence is visible before the table is even populated.

---

```json
{"top_score": 160, "all_essential_pass": true, "new_patterns": ["failure-mode annotation fused into table header lines — merges C-18 inertia framing with C-21 lineage constraint into a single self-explanatory header", "transitive artifact lineage chain — TABLE A → TABLE E3 → TABLE F propagates coverage gaps through the full cascade rather than each table independently citing TABLE A", "prose-section promotion narrows C-20 exception surface — converting 2D/2E/2F to tables reduces permitted-prose contexts, making the declaration more auditable"]}
```
