## trace-migration Scoring — Round 14 (Rubric v12)

---

### Scoring Basis

The v12 rubric adds three aspirational criteria (C-37, C-38, C-39) at 5 pts each to a 230-pt base (C-01 through C-36). All five variations are constructed on the same base template; the only structural differences across variations are the presence or absence of the three new mechanisms. The base satisfies all prior 36 criteria.

**Point allocation:**
- C-01 through C-36: 230 pts (base — identical across all variations)
- C-37 (PROTOCOL COUNT MANIFEST): 5 pts
- C-38 (COST LEDGER table): 5 pts
- C-39 (Cross-Role Inertia Chain in Phase B): 5 pts
- **Total possible: 245 pts**

---

### Criterion-by-Criterion Evaluation

#### C-01 through C-36 — All Variations

All five variations inherit the same base template, which embeds:
- STEP REGISTRY with before/after state (C-01)
- DATA LOSS PATH binary field in every role section (C-02)
- CONSTRAINT TYPE REGISTRY with four mandatory rows, per-role four-binary-field checklist (C-03, C-28, C-29, C-32)
- DEFAULT presence check mandated in PARITY ENFORCEMENT BLOCK for ALL new NOT NULL columns (C-04)
- Phase B as the sole chronological execution artifact (C-05)
- Named gate fields, compound "(BINARY FIELD)" annotations, structural gate chaining (C-17, C-21, C-34)
- BOUNDARY PROTOCOL sections as named artifacts (C-35)
- STATUS QUO COST section preceding Q1 with three-part prose framing (C-36)
- CONSTRAINT TYPE REGISTRY at parse time (C-31)
- PARITY ENFORCEMENT BLOCK with pre-positioned checklist and explicit scoping-prohibition language (C-33)
- Remaining criteria (C-06 through C-16, C-18 through C-20, C-22 through C-27, C-30): satisfied by structural design

**Result: C-01 through C-36 = PASS in all five variations.**

---

#### C-37 — PROTOCOL COUNT MANIFEST Dual-Surface Verification

| V | Verdict | Evidence |
|---|---------|----------|
| V-01 | **PASS** | PROTOCOL COUNT MANIFEST table present at Phase B entry; pre-commits all six boundary names, gate names, and gate states before B1 begins. Header scan count (6 BOUNDARY PROTOCOL headers) and manifest row count (6 rows) form two independent verification surfaces. |
| V-02 | **FAIL** | No PROTOCOL COUNT MANIFEST. COST LEDGER is present (satisfies C-38) but provides no second surface for gate coverage. A boundary missing from Phase B headers would require reading phase interiors to detect. |
| V-03 | **FAIL** | No PROTOCOL COUNT MANIFEST. Cross-role B2 chain satisfies C-39 but introduces no manifest mechanism. Gate completeness verifiable only by header scan. |
| V-04 | **PASS** | PROTOCOL COUNT MANIFEST present at Phase B entry with all six rows. Same dual-surface structure as V-01. B2 uses single-role framing (fails C-39) but the manifest is fully present and pre-committed. |
| V-05 | **PASS** | PROTOCOL COUNT MANIFEST present with all six rows, identical structural placement as V-04. Operations-first ordering does not affect manifest presence. |

---

#### C-38 — Cost Ledger Table Machine-Countability

| V | Verdict | Evidence |
|---|---------|----------|
| V-01 | **FAIL** | STATUS QUO COST is labeled prose with three-part framing (satisfies C-36). Completeness requires reading to confirm all three parts are present — no row count is possible. |
| V-02 | **PASS** | STATUS QUO COST expressed as a three-row COST LEDGER table (one row per part: schema condition, dependent process, accumulation trajectory). A table with fewer than three filled rows would be a structural gap visible without reading cell contents. Completeness is machine-countable. |
| V-03 | **FAIL** | STATUS QUO COST is prose (same as V-01 axis). C-39 is satisfied by B2 content; C-38 is independently not present. |
| V-04 | **PASS** | COST LEDGER table with three rows, satisfying both C-36 (named pre-Q1 section) and C-38 (row-countable format). Additive with C-37's manifest — neither table format constrains the other. |
| V-05 | **PASS** | COST LEDGER table present, identical structure as V-04. Operations-first ordering makes row (a) — CURRENT SCHEMA CONDITION — an infrastructure-grounded condition, which sets up B2's cross-role chain but does not change the table's structural presence or row count. |

---

#### C-39 — Cross-Role Inertia Chain in Phase B

| V | Verdict | Evidence |
|---|---------|----------|
| V-01 | **FAIL** | B2 inertia-contrast example names Commerce consequence only. A different step is named relative to Phase A (satisfies C-30), but no cross-role causal chain links an Operations substrate failure to consequences in two distinct domain roles. |
| V-02 | **FAIL** | B2 names a single domain role's consequence. Same structural gap as V-01 — C-39 is a B2 content criterion, not a Phase A ordering or table-format criterion. COST LEDGER satisfies C-38 independently. |
| V-03 | **PASS** | B2 explicitly names an Operations substrate failure whose disruption produces named Commerce AND Finance downstream consequences in a single causal chain. Commerce-first Phase A ordering is confirmed irrelevant to C-39; the cross-role chain is a B2 content property. Removing either role's consequence would leave the other role's analysis incomplete — dependency evidence no single-role B2 can produce. |
| V-04 | **FAIL** | B2 seeds a new inertia-contrast example naming a single domain role's consequence (step distinct from Phase A, satisfies C-30). C-37 and C-38 both pass; neither table-format mechanism places any obligation on B2 cross-role content. |
| V-05 | **PASS** | B2 names an Operations substrate condition whose disruption cascades to named Commerce AND Finance consequences simultaneously. Operations-first role ordering in Phase A means Q1 establishes the infrastructure substrate, which Q2 and Q3 reframe as domain-role consequences — B2's cross-role chain is structurally motivated by the Q1 foundation. |

---

### Composite Scores

| V | C-01–C-36 | C-37 | C-38 | C-39 | Total | % |
|---|-----------|------|------|------|-------|---|
| V-01 | 230 | 5 | 0 | 0 | **235** | 95.9% |
| V-02 | 230 | 0 | 5 | 0 | **235** | 95.9% |
| V-03 | 230 | 0 | 0 | 5 | **235** | 95.9% |
| V-04 | 230 | 5 | 5 | 0 | **240** | 98.0% |
| V-05 | 230 | 5 | 5 | 5 | **245** | 100.0% |

---

### Ranking

| Rank | V | Score | Delta from Prior |
|------|---|-------|-----------------|
| 1 | **V-05** | 245/245 | — |
| 2 | **V-04** | 240/245 | −5 (C-39 absent) |
| 3 (tied) | **V-01** | 235/245 | −5 from V-04 (C-38 absent) |
| 3 (tied) | **V-02** | 235/245 | −5 from V-04 (C-37 absent) |
| 3 (tied) | **V-03** | 235/245 | −5 from V-04 (C-37 and C-38 absent, C-39 present) |

The V-01/V-02/V-03 tie at 235 confirms orthogonality: each new criterion contributes exactly 5 pts independent of the other two. V-04's gap from V-05 isolates C-39 as the single remaining differentiator — the two table-format mechanisms (manifest + ledger) are not sufficient for the top score without the cross-role B2 chain.

---

### Excellence Signals (V-05)

**E-01 — Operations-first ordering as structural motivation for cross-role B2.**
Placing Operations in Q1 forces the infrastructure substrate into the first per-role analysis slot. By the time Commerce (Q2) and Finance (Q3) are analyzed, the substrate condition is already established. B2's cross-role chain then names the Q1 substrate failure and shows both Q2 and Q3 consequences following from it — the ordering makes the dependency structurally visible rather than incidental.

**E-02 — Manifest as cross-document consistency check, not just a count.**
The PROTOCOL COUNT MANIFEST's value is not only the row count: it pre-commits boundary *names*, gate *names*, and gate *states* before any boundary is traversed inside Phase B. A boundary present in headers but absent from the manifest — or vice versa — is a cross-document inconsistency detectable at Phase B entry without reading any phase body. The two surfaces (header scan, manifest rows) are independently verifiable.

**E-03 — COST LEDGER elevates STATUS QUO COST from narrative to audit artifact.**
Three-part prose framing requires reading to confirm completeness. A three-row table with one row per part makes a missing part a visible gap — a row-count failure detectable without reading cell contents. This applies the same machine-countability principle that BOUNDARY PROTOCOL blocks apply to gate coverage (C-35) to the inertia baseline (C-36).

**E-04 — Cross-role B2 chain creates non-substitutable dependency evidence.**
A B2 example naming two roles' consequences in a single causal chain is not equivalent to two separate B2 examples each naming one role. The chain structure means the Operations substrate failure must hold for *both* downstream failures to follow simultaneously — removing one role's consequence leaves the other incomplete. No single-role B2, however specific, can produce this dependency evidence.

---

```json
{"top_score": 245, "all_essential_pass": true, "new_patterns": ["Operations-first role ordering makes cross-role B2 causal chain structurally motivated: Q1 substrate established before Q2/Q3 domain consequences, so B2 chain follows the Phase A dependency structure", "PROTOCOL COUNT MANIFEST creates cross-document consistency check at Phase B entry: boundary present in headers but absent from manifest is a detectable inconsistency without reading phase body interiors", "COST LEDGER table applies machine-countability to STATUS QUO COST completeness: three-part completeness verifiable by row count alone, not by reading prose to confirm all three parts are present"]}
```
