## corps-build — Quest Score, Round 13 (Rubric v11)

---

### Scoring Assumptions

All five variations are built on top of the R12 golden baseline. C-01 through C-36 carry forward as **PASS** across all variations — R12 already cleared the golden threshold on every prior criterion. The differentiating work in R13 is entirely on **C-37** and **C-38**, with V-03 and V-05 seeding future criteria (C-39, C-40) that are not scored by v11.

---

### Per-Variation Scorecards

#### V-01 — PATH-ISOLATION COP assignment (add COP-14)

| ID | Criterion | Score | Evidence Note |
|----|-----------|-------|---------------|
| C-01 | Role file completeness | PASS | Carries R12 baseline |
| C-02 | org-chart.md with ASCII hierarchy | PASS | Carries R12 baseline |
| C-03 | Inertia Advocate in every team | PASS | Carries R12 baseline |
| C-04 | org.yaml structural fidelity | PASS | Carries R12 baseline |
| C-05 | Role file typed fields present | PASS | Carries R12 baseline |
| C-06–C-08 | Recommended (×3) | PASS | Carries R12 baseline |
| C-09–C-36 | Aspirational (×28) | PASS | Carries R12 baseline |
| **C-37** | INVARIANTS-to-COP bidirectional pointer | **PASS** | Adds COP-14 (`PATH-ISOLATION-CHECK [team-slug]:`); `INVARIANT-PATH-ISOLATION` now carries concrete `cop: [COP-14]` identifier, completing the bidirectional map for all five invariants |
| **C-38** | Three-layer CO-EXTENSIVE DECLARATION | **PARTIAL** | Three layers are named but the positive `PROPERTY-COVERAGE-RULE` assertion ("adding a new property requires entries in all three") is absent; declaration is structurally present, coverage requirement is implied not stated |

**Essential PASS:** 5/5 ✓
**Composite:** 60 + 30 + 140 + 5.0 + 2.5 = **237.5 / 240**
**Golden threshold (201):** ✓

---

#### V-02 — PROPERTY-COVERAGE-RULE explicit assertion

| ID | Criterion | Score | Evidence Note |
|----|-----------|-------|---------------|
| C-01–C-05 | Essential (×5) | PASS | Carries R12 baseline |
| C-06–C-08 | Recommended (×3) | PASS | Carries R12 baseline |
| C-09–C-36 | Aspirational (×28) | PASS | Carries R12 baseline |
| **C-37** | INVARIANTS-to-COP bidirectional pointer | **PARTIAL** | `INVARIANT-PATH-ISOLATION` retains `cop: (implicit...)` — not a concrete COP-NN identifier; the rule about requiring COP pointers is now stated but the map itself is incomplete for PATH-ISOLATION |
| **C-38** | Three-layer CO-EXTENSIVE DECLARATION | **PASS** | Explicitly adds the `PROPERTY-COVERAGE-RULE` assertion ("adding a new property requires entries in all three layers"); all three layers named; positive obligation stated |

**Essential PASS:** 5/5 ✓
**Composite:** 60 + 30 + 140 + 2.5 + 5.0 = **237.5 / 240**
**Golden threshold (201):** ✓

---

#### V-03 — Phase `ENFORCES-INVARIANTS:` annotation

| ID | Criterion | Score | Evidence Note |
|----|-----------|-------|---------------|
| C-01–C-05 | Essential (×5) | PASS | Carries R12 baseline |
| C-06–C-08 | Recommended (×3) | PASS | Carries R12 baseline |
| C-09–C-36 | Aspirational (×28) | PASS | Carries R12 baseline |
| **C-37** | INVARIANTS-to-COP bidirectional pointer | **PARTIAL** | Phase-level `ENFORCES-INVARIANTS:` annotations are present but these are phase→invariant links, not the required INVARIANTS→COP and COP→invariant bidirectional pointer fields; C-37 requires `cop:` on INVARIANTS entries and `invariant:` on COP-NN items — neither is demonstrated by the phase-header pattern alone |
| **C-38** | Three-layer CO-EXTENSIVE DECLARATION | **PARTIAL** | Three-layer declaration is not extended to name the new phase-header enforcement mechanism; the phase-header pattern implicitly adds a fourth layer but the CO-EXTENSIVE DECLARATION is not updated to assert it; no `PROPERTY-COVERAGE-RULE` stated |

**Essential PASS:** 5/5 ✓
**Composite:** 60 + 30 + 140 + 2.5 + 2.5 = **235.0 / 240**
**Golden threshold (201):** ✓

*Seeds C-39 (Phase ENFORCES-INVARIANTS header) — not scored by v11.*

---

#### V-04 — V-01 + V-02 (COP-14 live-demonstrates the rule)

| ID | Criterion | Score | Evidence Note |
|----|-----------|-------|---------------|
| C-01–C-05 | Essential (×5) | PASS | Carries R12 baseline |
| C-06–C-08 | Recommended (×3) | PASS | Carries R12 baseline |
| C-09–C-36 | Aspirational (×28) | PASS | Carries R12 baseline |
| **C-37** | INVARIANTS-to-COP bidirectional pointer | **PASS** | COP-14 (`PATH-ISOLATION-CHECK`) added; all five INVARIANTS entries now carry concrete `cop:` identifiers; all COP-NN items carry `invariant:` annotations; bidirectional map complete |
| **C-38** | Three-layer CO-EXTENSIVE DECLARATION | **PASS** | CO-EXTENSIVE DECLARATION names CATALOG + INVARIANTS + COP-NN and explicitly states `PROPERTY-COVERAGE-RULE`; COP-14 is the live demonstration that the rule functions — new property (PATH-ISOLATION) required a new COP entry |

**Essential PASS:** 5/5 ✓
**Composite:** 60 + 30 + 140 + 5.0 + 5.0 = **240 / 240**
**Golden threshold (201):** ✓

---

#### V-05 — V-01 + V-02 + V-03 + CROSS-REF `enforces-invariant:` annotations

| ID | Criterion | Score | Evidence Note |
|----|-----------|-------|---------------|
| C-01–C-05 | Essential (×5) | PASS | Carries R12 baseline |
| C-06–C-08 | Recommended (×3) | PASS | Carries R12 baseline |
| C-09–C-36 | Aspirational (×28) | PASS | Carries R12 baseline |
| **C-37** | INVARIANTS-to-COP bidirectional pointer | **PASS** | Full V-01 bidirectional map present; COP-14 completes the PATH-ISOLATION pointer; all invariant↔COP links bidirectional and named |
| **C-38** | Three-layer CO-EXTENSIVE DECLARATION | **PASS** | Full V-02 `PROPERTY-COVERAGE-RULE` present; additionally CROSS-REF rows carry `enforces-invariant:` annotations extending the attestation surface — declaration describes this as a fourth verification layer |

**Essential PASS:** 5/5 ✓
**Composite:** 60 + 30 + 140 + 5.0 + 5.0 = **240 / 240**
**Golden threshold (201):** ✓

*Seeds C-39 (Phase ENFORCES-INVARIANTS header) and C-40 (CROSS-REF invariant-linkage as fourth CO-EXTENSIVE layer) — not scored by v11.*

---

### Rankings

| Rank | Variation | Composite | C-37 | C-38 | Seeds |
|------|-----------|-----------|------|------|-------|
| 1 | **V-05** | 240 / 240 | PASS | PASS | C-39, C-40 |
| 2 | **V-04** | 240 / 240 | PASS | PASS | — |
| 3 | **V-01** | 237.5 / 240 | PASS | PARTIAL | — |
| 3 | **V-02** | 237.5 / 240 | PARTIAL | PASS | — |
| 5 | **V-03** | 235.0 / 240 | PARTIAL | PARTIAL | C-39 |

V-04 and V-05 tie on the v11 rubric at maximum score. V-05 ranks first because it seeds two new structural patterns that will become C-39 and C-40 in v12.

---

### Excellence Signals — V-05

**What V-05 did that V-04 did not:**

1. **Phase `ENFORCES-INVARIANTS:` header annotation** — each phase header declares which invariants it owns (`ENFORCES-INVARIANTS: NONE` for enforcement-free phases). This moves invariant residency from an implicit consequence of reading each phase to a named, scannable field on every phase boundary. A reviewer can audit invariant coverage without reading phase bodies.

2. **CROSS-REF `enforces-invariant:` row annotations** — BUILD-VERIFY CROSS-REF rows carry `enforces-invariant:` annotations naming the source invariant each cross-reference enforces. This makes CROSS-REF a fourth independent verification layer alongside CATALOG, INVARIANTS, and COP-NN — and enables V-05 to extend the CO-EXTENSIVE DECLARATION from three to four layers.

**Why these matter:** Prior rounds established the CATALOG → INVARIANTS → COP-NN traceability chain (C-37, C-38). V-05 extends coverage to the phase-execution and cross-verification planes. The structural logic is consistent: each time a new attestation surface emerges, it becomes auditable, named, and co-extensive with the others. V-04 demonstrates the rule with a new COP entry; V-05 propagates the rule to every attestation surface in the build, which is the deeper structural move.

---

```json
{"top_score": 240, "all_essential_pass": true, "new_patterns": ["Phase ENFORCES-INVARIANTS header annotation declares which invariants each phase owns, making per-phase invariant residency auditable at a glance without reading phase bodies", "BUILD-VERIFY CROSS-REF rows carry enforces-invariant annotations, extending CO-EXTENSIVE DECLARATION from three to four independent verification layers"]}
```
