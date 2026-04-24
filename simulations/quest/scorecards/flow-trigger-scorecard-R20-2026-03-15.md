## flow-trigger Round 20 — Scoring (Rubric v17)

---

### Scoring Framework

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 39 * 10)
```

PARTIAL = 0.5 credit. Max = 100.

**Essential (C-01–C-05):** All five variations carry a complete multi-phase protocol with explicit platform term contract, structured entry schema, firing order (EOR TABLE), anomaly verdicts, and scope gate. **5/5 PASS across all variations.**

**Recommended (C-06–C-08):** Circular analysis, conditional branch coverage, and anomaly remediation all structurally present in all variations. **3/3 PASS across all variations.**

**Aspirational baseline (C-09–C-38, 30 criteria):** Core structural properties — phase body completeness, denominator declaration, cascade depth budget, back-edge detection, terminal markers, CLOSURE CHECK counters, prohibition breach tokens, artifact manifest with role attribution, etc. — are identical across all five variations. **30/30 PASS baseline for all variations.**

---

### Per-Variation Scoring on Differentiating Criteria (C-39–C-47)

| Criterion | What it measures | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|-----------------|------|------|------|------|------|
| C-39 | INERTIA CONTRAST covers 7 mechanisms (incl. DUAL-TIME ATTRIBUTION CHAIN) | FAIL | FAIL | FAIL | PASS | PASS |
| C-40 | CLOSURE CHECK NOTE block uses code fence with machine-inspectable boundaries | PASS | PARTIAL | PASS | PASS | PASS |
| C-41 | (structural property — uniform across all) | PASS | PASS | PASS | PASS | PASS |
| C-42 | NOTE block baseline structure | PASS | PASS | PASS | PASS | PASS |
| C-43 | REMEDIATION SELF-SUFFICIENCY present as third extended bracket assertion | PASS | FAIL | PASS | PASS | PASS |
| C-44 | All 3 NOTE assertions carry extended bracket form (3/3) | PASS | PARTIAL | PASS | PASS | PASS |
| C-45 | ≥2 lifecycle phases carry both forward dependency + violation mode | PASS (2/6) | PASS (4/6) | PASS (6/6) | PASS (6/6) | PASS (6/6) |
| C-46 | ALL ordering-statement phases carry both components (PARTIAL ≥50%; FAIL <50%) | **FAIL** (33%) | **PARTIAL** (67%) | **PASS** (100%) | **PASS** (100%) | **PASS** (100%) |
| C-47 | Phase 0 registry rows ordered in execution sequence: DE above Auditor | **PASS** | **FAIL** | **FAIL** | **PASS** | **PASS** |

**Evidence notes:**

- **V-01 C-47 PASS:** Registry header `*(Row order: Domain Expert obligations first -- declaration-time artifact producers; Auditor obligations follow -- verification-time enforcers.)*` present; EOR TABLE and CASCADE DEPTH BUDGET rows appear above SCOPE GATE, EXCLUSION LOG, PROHIBITION CONTRACTS, ARTIFACT MANIFEST rows. C-46 FAIL: only Phases 0–1 carry the violation mode; Phases 2–5 state dependency only → 2/6 = 33% < 50% threshold.

- **V-02 C-47 FAIL:** `*(PHASE 0 OBLIGATION REGISTRY with standard Auditor-first row order: SCOPE GATE, EXCLUSION LOG, EOR TABLE, ...)*` — Auditor rows precede DE rows. C-46 PARTIAL: Phases 0–3 carry both (4/6 = 67%). C-40 PARTIAL: prose-delimited NOTE block, no fence. C-43 FAIL: REMEDIATION SELF-SUFFICIENCY bracket is `[must be maintained]` — bare, no rationale clause. C-44 PARTIAL: 2/3 extended.

- **V-03 C-46 PASS:** All six phases carry named violation mode in bold failure-mode label convention. Phase 6 carries a closing dependency directed at the final consumer. C-47 FAIL: `*(PHASE 0 OBLIGATION REGISTRY with standard Auditor-first row order)*`.

- **V-04:** C-47 PASS (registry header explicit, DE rows first) + C-46 PASS (Phases 0–5 all complete) + C-39 PASS (DUAL-TIME ATTRIBUTION CHAIN as 7th INERTIA CONTRAST mechanism; DERIVATION TEST covers all 7). C-44/C-43/C-40 PASS.

- **V-05:** All V-04 axes maintained. Adds Phase 6 closing dependency statement, full SHALL/MUST phrasing register throughout (no descriptive softening). Registry header identical to V-01/V-04. C-47+C-46 double-encoding: row positions enforce Phase 0 ordering invariant; phase forward-dependency paragraphs enforce lifecycle ordering invariant — each independently detectable.

---

### Aspirational Score Computation

| Variation | Baseline (C-09–C-38) | C-39 | C-40 | C-41/C-42 | C-43 | C-44 | C-45 | C-46 | C-47 | **Total asp** | **Asp score** |
|-----------|----------------------|------|------|-----------|------|------|------|------|------|--------------|--------------|
| V-01 | 30 | 0 | 1 | 2 | 1 | 1 | 1 | 0 | 1 | **37.0** | (37/39)×10 = **9.49** |
| V-02 | 30 | 0 | 0.5 | 2 | 0 | 0.5 | 1 | 0.5 | 0 | **34.5** | (34.5/39)×10 = **8.85** |
| V-03 | 30 | 0 | 1 | 2 | 1 | 1 | 1 | 1 | 0 | **37.0** | (37/39)×10 = **9.49** |
| V-04 | 30 | 1 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | **39.0** | (39/39)×10 = **10.00** |
| V-05 | 30 | 1 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | **39.0** | (39/39)×10 = **10.00** |

---

### Composite Scores

| Variation | Essential (60) | Recommended (30) | Aspirational (10) | **Composite** |
|-----------|---------------|-----------------|-------------------|--------------|
| V-01 | 60.0 | 30.0 | 9.49 | **99.49** |
| V-02 | 60.0 | 30.0 | 8.85 | **98.85** |
| V-03 | 60.0 | 30.0 | 9.49 | **99.49** |
| V-04 | 60.0 | 30.0 | 10.00 | **100.00** |
| V-05 | 60.0 | 30.0 | 10.00 | **100.00** |

**All 5 variations:** all essential pass ✓ | composite ≥ 80 ✓ → **Golden threshold met by all.**

---

### Ranking

| Rank | Variation | Score | Differentiator |
|------|-----------|-------|---------------|
| 1 | **V-05** | 100.00 | C-47+C-46+C-39+C-44+C-43 all PASS; Phase 6 closing dependency; full formal register |
| 1 | **V-04** | 100.00 | C-47+C-46+C-39+C-44+C-43 all PASS; DUAL-TIME ATTRIBUTION CHAIN as 7th INERTIA mechanism |
| 3 | **V-01** | 99.49 | C-47 PASS isolates role-sequence axis; C-46 FAIL (33% < threshold) |
| 3 | **V-03** | 99.49 | C-46 PASS isolates lifecycle-emphasis axis; C-47 FAIL (standard Auditor-first) |
| 5 | **V-02** | 98.85 | C-47 FAIL + C-43 FAIL + C-40 PARTIAL + C-44 PARTIAL; format degradation compounds |

V-01 and V-03 tie because each passes exactly one of C-46/C-47 while failing the other (net identical aspirational delta vs. baseline). V-02 falls furthest due to four separate aspirational degradations in a single variation.

---

### Excellence Signals from V-04/V-05

**1. Doubly-redundant execution-sequence encoding (C-47 × C-46 combined)**
V-05's hypothesis makes this explicit: the registry's row positions declare the Phase 0 artifact ordering invariant; the phase forward-dependency paragraphs declare the lifecycle ordering invariant. Any structural edit that reorders registry rows, removes a phase, or omits a violation mode from a forward-dependency paragraph is independently detectable from each axis — neither requires the other to surface the violation.

**2. Execution-sequence row ordering as a positional consistency contract (C-47)**
The `*(Row order: Domain Expert obligations first -- declaration-time artifact producers; Auditor obligations follow -- verification-time enforcers.)*` registry header converts table row position into a structural commitment: any row placing an Auditor obligation above a Domain Expert obligation on which it depends becomes a positional inconsistency verifiable by inspection alone, redundantly with the Activation Event column.

**3. DUAL-TIME ATTRIBUTION CHAIN as 7th INERTIA CONTRAST mechanism (C-39 path)**
Extending the INERTIA CONTRAST from 6 to 7 mechanisms — adding DUAL-TIME ATTRIBUTION CHAIN (declaration-time via ARTIFACT MANIFEST + detection-time via CLOSURE CHECK counters) — exposes the weaker alternative (declaration-time attribution only) and its failure mode (**anonymous detection-time attribution**) as derivable structural properties. A reader finds both layers required for remediation self-sufficiency without rubric access.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["doubly-redundant execution-sequence encoding: registry row positions (C-47) and phase forward-dependency paragraphs (C-46) independently enforce ordering invariants, making any structural edit detectable from either axis alone", "execution-sequence-aligned registry row ordering: Domain Expert rows above Auditor rows converts table position into a positional consistency contract redundant with the Activation Event column"]}
```
