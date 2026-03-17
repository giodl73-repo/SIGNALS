## trace-migration — Round 7 Scorecard (v7 rubric)

---

### Scoring Key

| Tier | Per-criterion | Max |
|------|--------------|-----|
| Essential (C-01–C-05) | 12 pts | 60 |
| Recommended (C-06–C-08) | 10 pts | 30 |
| Aspirational (C-09–C-27) | 5 pts | 95 |
| **Total** | | **185** |

PASS = full pts · PARTIAL = half pts · FAIL = 0  
**Golden** = all C-01–C-05 PASS AND composite ≥ 148 (80%)

---

### Essential Criteria (C-01–C-05)

| C | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|-----------|------|------|------|------|------|
| C-01 | Before/After State | PASS | PASS | PASS | PASS | PASS |
| C-02 | Data Loss Path | PASS | PASS | PASS | PASS | PASS |
| C-03 | Constraint Violation Analysis | PASS | **PARTIAL** | PASS | PASS | PASS |
| C-04 | Missing Default Value Detection | PASS | PASS | PASS | **PARTIAL** | PASS |
| C-05 | Chronological Step Ordering | PASS | PASS | PASS | PASS | PASS |
| **Essential /60** | | **60** | **54** | **60** | **54** | **60** |

**C-03 / V-02 — PARTIAL:** The scorecard template models only `NOT NULL RISK (BINARY FIELD)` as a structured constraint slot. FK, UNIQUE, and CHECK constraint violations have no dedicated field; they would fall into the free-form `MIGRATION DISRUPTION` field, which doesn't structurally require naming violating rows or the migration's response (fail/skip/backfill). A model reproducing the template faithfully would satisfy C-03 for NOT NULL but could silently omit FK/CHECK analysis.

**C-04 / V-04 — PARTIAL:** Q3 Finance explicitly asks for DEFAULT checks only on "financial columns." Q4 Operations covers constraint violation analysis (whether existing rows satisfy the constraint) but does not contain the word DEFAULT or require checking DEFAULT presence. A non-financial NOT NULL column added to an existing table (e.g., a `shipped_at TIMESTAMP NOT NULL` on an orders table) would not trigger a DEFAULT check from Q3, and Q4's constraint analysis would only surface it indirectly if existing rows fail — missing the pre-run DEFAULT-presence check C-04 requires.

---

### Recommended Criteria (C-06–C-08)

| C | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|-----------|------|------|------|------|------|
| C-06 | Performance Cliff Detection | PASS | PASS | PASS | PASS | PASS |
| C-07 | Rollback Viability Assessment | PASS | PASS | PASS | PASS | PASS |
| C-08 | Domain Expert Framing | PASS | PASS | PASS | PASS | PASS |
| **Recommended /30** | | **30** | **30** | **30** | **30** | **30** |

All five variations provide explicit performance cliff (table + row count + risk), rollback taxonomy (fixed vocabulary FULL DOWN MIGRATION / BACKUP ONLY / IRREVERSIBLE), and concrete domain objects with numeric thresholds.

---

### Aspirational Criteria (C-09–C-27)

| C | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|---|-----------|------|------|------|------|------|-------|
| C-09 | Zero-Downtime Viability | PASS | PASS | PASS | **PARTIAL** | PASS | V-04: Q2 scopes zero-downtime to Commerce tables; Q4 Operations omits it; a Finance or Operations DDL lock would not be caught in Phase A |
| C-10 | Idempotency Check | PASS | PASS | PASS | PASS | PASS | All have idempotency analysis with exact failure mode |
| C-11 | Locked Execution Sequence | PASS | PASS | PASS | PASS | PASS | Registry in first section; ≥2 downstream sections cite by step number |
| C-12 | Domain Section Pre-Positioned | PASS | PASS | PASS | PASS | PASS | Domain always before verify and recommendations |
| C-13 | Silence-is-Failure Enforcement | PASS | PASS | PASS | PASS | PASS | YES/NO/PARTIAL and fixed-taxonomy fields throughout |
| C-14 | Critical Field Type Annotation | PASS | PASS | PASS | PASS | PASS | `(BINARY FIELD)` at every definition site for data loss, NOT NULL risk, rollback |
| C-15 | Forward-Progress Gate | PASS | PASS | PASS | PASS | PASS | First gate in each output resolves OPEN/BLOCKED before downstream phase |
| C-16 | Two-Phase Analytical Decoupling | PASS | PASS | PASS | PASS | PASS | Phase A organized by concern/breach/role/lifecycle; Phase B canonical |
| C-17 | Gate Field Annotation Compound | PASS | PASS | PASS | PASS | PASS | `PARSE GATE (BINARY FIELD): ___ (OPEN / BLOCKED)` — C-14 + C-15 at same field |
| C-18 | Named Artifact Citation | PASS | PASS | PASS | PASS | PASS | Each cites distinct artifact: PARSE REGISTRY / STEP REGISTRY / FAILURE REGISTRY / Q1 / PARSE REGISTRY |
| C-19 | Per-Section Citation Repetition | PASS | PASS | PASS | PASS | PASS | Citation instruction appears in every analytical section, not only global preamble |
| C-20 | Domain Section Completion Constraint | PASS | PASS | PASS | PASS | PASS | V-01/V-03/V-05 have two-level C-20 (Phase A domain → B2; B2 → B3); V-02/V-04 have B2 → B3 only |
| C-21 | Complete Phase Gate Chain | PASS | PASS | PASS | PASS | PASS | Every phase transition has named binary gate and each phase header names its prerequisite |
| C-22 | Pre-Seeded Inline Domain Example | PASS | PASS | PASS | PASS | PASS | All have decimal(19,4)→decimal(10,2) worked example with $9,999,999.99 threshold |
| C-23 | Step Registry Phase Encapsulation | PASS | PASS | PASS | PASS | PASS | Registry enclosed in named phase with exit gate; first analytical section names gate |
| C-24 | Intra-Phase-B Gate Chain | PASS | PASS | PASS | PASS | PASS | V-01–V-04: B2→B3, B3→B4 (2 gates); V-05: B2→B3, B3→B4, B4→VERDICT (3 gates) |
| C-25 | Explicit Phase-B Canonical Claim | PASS | PASS | PASS | PASS | PASS | "C-05 is satisfied here, not by any Phase A section" verbatim in all five |
| **C-26** | **Terminal Output Gating** | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** | All five: `VERDICT *(requires RECOMMENDATIONS GATE = OPEN)*` |
| **C-27** | **Inertia-Contrast Framing** | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** | Three-part structure seeded in all five; V-04 has two distinct domain-role examples; V-05 has Phase A + distinct Phase B examples |
| **Aspirational /95** | | **95** | **95** | **95** | **92.5** | **95** |

---

### Composite Scores

| Variation | Essential | Recommended | Aspirational | **Total /185** | **%** | Golden |
|-----------|-----------|-------------|--------------|----------------|-------|--------|
| V-01 | 60 | 30 | 95 | **185** | 100% | YES |
| V-02 | 54 | 30 | 95 | **179** | 96.8% | NO (C-03 essential partial) |
| V-03 | 60 | 30 | 95 | **185** | 100% | YES |
| V-04 | 54 | 30 | 92.5 | **176.5** | 95.4% | NO (C-04 essential partial) |
| V-05 | 60 | 30 | 95 | **185** | 100% | YES |

---

### Ranking

| Rank | Variation | Score | Key differentiator |
|------|-----------|-------|--------------------|
| 1 (tie) | **V-01** | 185 | Inertia framing as organizational lens; double C-20 chain; all constraint types explicitly named |
| 1 (tie) | **V-03** | 185 | Adversarial register forces prior-state naming; double C-20 chain; all constraint types explicitly named |
| 1 (tie) | **V-05** | 185 | Dual-phase C-27 seeding (distinct examples at Phase A and Phase B); 5-gate Phase A lifecycle; 3 intra-Phase-B gates |
| 4 | V-02 | 179 | Scorecard field design leaves FK/UNIQUE/CHECK constraint analysis in free-form MIGRATION DISRUPTION — structural gap in C-03 |
| 5 | V-04 | 176.5 | DEFAULT check scoped to financial columns (Q3) misses non-financial NOT NULL columns; zero-downtime assessment Commerce-only in Phase A |

---

### Excellence Signals

**From V-01 and V-03** — the C-02/C-03/C-04 gap in V-02 and V-04 traces back to a structural principle: when an analytical phase uses a **free-form template field** (MIGRATION DISRUPTION) as the primary capture mechanism for constraint violations, the structural enforcement collapses to whatever the model decides to put there. V-01 and V-03 name all four constraint types (NOT NULL, UNIQUE, FK, CHECK) as explicit required analysis items within the phase instruction, making omission visible as a missing line in a list rather than a missing sentence in a paragraph.

**From V-05** — the dual-phase inertia seeding property: DOMAIN IMPACT Phase A seeds a Finance wire transfer example; DOMAIN SYNTHESIS Phase B seeds a **distinct** Commerce refund example. This forces Phase B synthesis to re-derive the inertia contrast at synthesis depth rather than inheriting Phase A's framing wholesale. It is the only variation where Phase B cannot satisfy C-27 by copying from Phase A. This is the structural basis of the predicted C-28 candidate.

**Unscored differentiator — C-28 candidate:** "Phase B domain synthesis must contain a pre-seeded inertia-contrast example that names a different business object than the Phase A domain example, requiring synthesis-level cause reasoning rather than Phase A inheritance." V-05 exclusive.

**Unscored differentiator — C-29 candidate:** "Phase A domain section header carries a forward-completion instruction naming Phase B's domain synthesis section as the downstream target, creating a two-level C-20 execution chain (Phase A domain → B2 → B3)." Present in V-01 and V-03 (DOMAIN BREACH and BUSINESS FAILURE INVESTIGATION both carry `POSITIONED BEFORE B2 DOMAIN SYNTHESIS`); absent in V-02 and V-04 (only B2 carries C-20); present in V-05 (DOMAIN IMPACT PHASE).

---

```json
{"top_score": 185, "all_essential_pass": true, "new_patterns": ["Dual-phase C-27 seeding: Phase B domain synthesis carries a pre-seeded inertia-contrast example naming a distinct business object from the Phase A domain example, preventing Phase B synthesis from satisfying C-27 by inheriting Phase A framing rather than deriving the inertia contrast at synthesis depth", "Phase A domain section completion constraint: the Phase A domain section header explicitly forward-names the Phase B domain synthesis section as its downstream completion target, creating a two-level C-20 execution chain (Phase A domain section must precede B2; B2 must precede B3) rather than a single-level chain anchored only at B2"]}
```
