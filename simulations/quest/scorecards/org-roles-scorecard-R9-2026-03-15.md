---

## org-roles Round 9 Scorecard — Rubric v9

**Scoring formula:** `composite = (5/5 × 60) + (3/3 × 30) + (aspirational_pass/33 × 10)`
All five variates pass all essential and recommended criteria; the score differential is entirely in the aspirational component.

---

### Criteria Evaluation

#### C-01 through C-36 (baseline aspirational)

All five variates inherit the R8 V-01/V-03 foundation: C-09 through C-36 fully PASS (28 aspirational points). None of the R9 variations introduce regressions on baseline criteria — except V-05, addressed below.

---

### New Criteria (C-37 through C-41)

#### V-01 — Inertia Framing (R8 V-03 base + ANCHOR-CARD + phase-decomposed scan)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-37 | **PASS** | Phase 3 STOCK-ROLES explicitly designates inertia-advocate as "ANCHOR-CARD for this registry; Diagnosis Card written FIRST in Phase 5, YAML written FIRST; carries `anchor: true`; does NOT carry `orthogonality`." Phase 5 subsequent Diagnosis Cards include `orthogonality to ANCHOR-CARD` field per [FC-11]. Both (a) anchor designation with write-first ordering and (b) per-card orthogonality field present. |
| C-38 | **PARTIAL** | Scan has Phase 1 — Anchor-Orthogonality Check (lists verify questions + tests anchor-orthogonality combined), Phase 2 — Non-Anchor Pairwise Check, and Resolution statement — 3 named elements but only 2 labeled "Phase." C-38 PASS requires at least three named phases; enumeration is embedded in Phase 1 rather than a separate named phase. Exceeds PARTIAL condition (scan does decompose into named phases separating anchor from non-anchor pairwise), but falls short of strict "three named phases" PASS. |
| C-39 | **PASS** | Inherited from R8 V-03 base: INERTIA-GAP ANALYSIS sub-step in Phase 2 before expert naming, Gap Domains enumerated with Domain/Failure mode/Inertia resistance per gap. |
| C-40 | **PASS** | Inherited from R8 V-03 base: Phase 2 gate item 4 "Expert names derive from INERTIA-GAP ANALYSIS Domain vocabulary — no placeholder per [FC-1]" is the positive sourcing constraint. |
| C-41 | **PASS** | Inherited from R8 V-03 base: Diagnosis Card `inertia gap inherited` field citing "Gap N inertia resistance from Phase 2 INERTIA-GAP ANALYSIS — copied verbatim" references a named Gap Domain entry. |

**Aspirational:** 28 + 1 (C-37) + 0.5 (C-38) + 1 (C-39) + 1 (C-40) + 1 (C-41) = **32.5/33**
**Composite:** 60 + 30 + (32.5/33 × 10) = **99.85** GOLDEN

---

#### V-02 — Role Sequence (R8 V-03 base + GAP-{slug} identifiers + POSITIVE SOURCING)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-37 | **FAIL** | No ANCHOR-CARD designation in Phase 3. STOCK-ROLES lists inertia-advocate last as a standard stock role with no anchor label, no write-first ordering mandate. |
| C-38 | **FAIL** | Cross-card scan is flat: "For each pair of roles, confirm their primary_verify_questions address different facets." No anchor as reference axis; no named phase decomposition. |
| C-39 | **PASS** | INERTIA-GAP ANALYSIS with GAP-{slug} formal identifiers satisfies the named gap-enumeration sub-step requirement more firmly than R8 V-03. |
| C-40 | **PASS** | POSITIVE SOURCING statement per expert citing specific GAP-{slug} identifier and domain vocabulary term used in the name — this is the positive constraint required. |
| C-41 | **PASS** | Diagnosis Card `inertia gap inherited` cites "GAP-{slug}: [inertia resistance copied from INERTIA-GAP ANALYSIS]" by named identifier, not positional. |

**Aspirational:** 28 + 0 (C-37) + 0 (C-38) + 1 (C-39) + 1 (C-40) + 1 (C-41) = **31/33**
**Composite:** 60 + 30 + (31/33 × 10) = **99.39** GOLDEN — no improvement over R8 V-03 ceiling

Note: V-02 strengthens C-40 and C-41 implementations, but both were already PASS in R8 V-03. The score is identical to R8 V-03 because the only new structural additions (GAP-{slug} naming, POSITIVE SOURCING) reinforce criteria that were already satisfied.

---

#### V-03 — Output Format (R8 V-03 base + YAML persistence of `orthogonality` + `inertia_gap_inherited`)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-37 | **FAIL** | V-03 adds an `orthogonality` field to Diagnosis Cards and YAML files (FC-11), but Phase 3 STOCK-ROLES carries no ANCHOR-CARD designation and no write-first ordering mandate. C-37 PASS requires both (a) ANCHOR-CARD designation with write-first ordering and (b) per-card orthogonality field. V-03 has (b) but not (a). The PARTIAL condition covers "ordering without per-card tracing" — the opposite situation. Without explicit ANCHOR-CARD designation, the FAIL condition applies. |
| C-38 | **FAIL** | Cross-card scan is flat (same as R8 V-03). No anchor phases. |
| C-39 | **PASS** | Unchanged from R8 V-03 base. |
| C-40 | **PASS** | Unchanged from R8 V-03 base. |
| C-41 | **PASS** | Diagnosis Cards have `inertia gap inherited` citing Gap Domain NAME per [FC-12]. YAML files additionally carry `inertia_gap_inherited` — but C-41 tests the Diagnosis Card, not YAML persistence. Still PASS. |

**Aspirational:** 28 + 0 (C-37) + 0 (C-38) + 1 (C-39) + 1 (C-40) + 1 (C-41) = **31/33**
**Composite:** 60 + 30 + (31/33 × 10) = **99.39** GOLDEN — no improvement over R8 V-03 ceiling

Note: V-03 tests whether YAML-level persistence of `orthogonality` and `inertia_gap_inherited` triggers any v9 criterion. It does not — C-37 requires explicit anchor designation (which V-03 omits), and no v9 criterion tests YAML-level field persistence independently of Diagnosis Card provenance. The axis hypothesis is falsified: YAML persistence alone is insufficient to advance the score.

---

#### V-04 — Combined (ANCHOR-CARD + named gaps + phase-decomposed scan + YAML persistence)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-37 | **PASS** | Phase 3 STOCK-ROLES lists inertia-advocate first as "ANCHOR-CARD for this registry; Diagnosis Card written FIRST in Phase 5; YAML written FIRST; carries `anchor: true`; does NOT carry `orthogonality` or `inertia_gap_inherited`." Phase 5 subsequent Diagnosis Cards require `orthogonality to ANCHOR-CARD` field. Both conditions met. |
| C-38 | **PARTIAL** | Same 2-phase scan structure as V-01: Phase 1 — Anchor-Orthogonality Check (combined enumeration + anchor testing) + Phase 2 — Non-Anchor Pairwise Check + "Record resolution before YAML writing begins." Three functional elements, only 2 labeled as phases. Same PARTIAL assessment as V-01. |
| C-39 | **PASS** | INERTIA-GAP ANALYSIS with formal GAP-{slug} identifiers before expert naming. Named sub-step with Gap Domain vocabulary. |
| C-40 | **PASS** | POSITIVE SOURCING statement per expert: "this name derives from GAP-{slug} Domain vocabulary: [specific term used]" — explicit positive constraint citing the named gap artifact. |
| C-41 | **PASS** | Diagnosis Card `inertia gap inherited` cites "GAP-{slug}: [inertia resistance copied verbatim]" — named GAP identifier, stronger provenance than R8 V-03's positional "Gap N." |

**Aspirational:** 28 + 1 (C-37) + 0.5 (C-38) + 1 (C-39) + 1 (C-40) + 1 (C-41) = **32.5/33**
**Composite:** 60 + 30 + (32.5/33 × 10) = **99.85** GOLDEN

---

#### V-05 — Combined Imperative Register (V-04 content, checklist format)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-37 | **PASS** | Step 6: "write the inertia-advocate Diagnosis Card FIRST — it is the ANCHOR-CARD." Subsequent cards include `Orthogonality to ANCHOR-CARD` field. YAML template includes `anchor: true` for inertia-advocate. Both conditions met. |
| C-38 | **PARTIAL** | Step 7 has Phase 1 — Anchor-Orthogonality and Phase 2 — Non-Anchor Pairwise — only 2 named phases. Revision embedded within Phase 2, no separate Resolution label. Same PARTIAL as V-01/V-04. |
| C-39 | **PASS** | Step 3: INERTIA-GAP ANALYSIS with GAP-{slug} identifiers produced before any expert named in Step 4. |
| C-40 | **PASS** | Step 4: POSITIVE SOURCING statement per expert required: "this name derives from GAP-{slug}: [specific term used in name]." |
| C-41 | **PASS** | Step 6 subsequent Diagnosis Cards: `Inertia gap inherited: "GAP-{slug}: [resistance verbatim]"`. Final checklist explicitly names C-41 criterion. |

**Regressions from V-04:**

| ID | V-04 | V-05 | Reason |
|----|------|------|--------|
| C-29 | PASS | **PARTIAL** | V-04 uses "CONTRACT VIOLATION (type 1)" and "CONTRACT VIOLATION (type 2)" in FC-10. V-05 replaces FC-N structure with "Commit 2 — Field identifiers" (which omits `collaborates_with` entirely from the commitment block) and uses checklist items "No PHANTOM names / No UNIVERSALIST listing" without violation/breach language. C-29 PASS requires the word "violation" or "breach" in the label. Both prohibitions present (C-08 PASS), but C-29 requires contract-violation framing. PARTIAL. |
| C-33 | PASS | **PARTIAL** | V-04 mirrors "CONTRACT VIOLATION (type 1/2)" labels in both the FC contract block and the YAML template's `collaborates_with` annotation. V-05's YAML template uses checklist items without CONTRACT VIOLATION labels. C-33 cannot PASS while C-29 is PARTIAL. Both prohibitions are mirrored (so not FAIL), but without violation framing → PARTIAL. |

**Aspirational:** 28 + 1 (C-37) + 0.5 (C-38) + 1 (C-39) + 1 (C-40) + 1 (C-41) − 0.5 (C-29 PARTIAL) − 0.5 (C-33 PARTIAL) = **31.5/33**
**Composite:** 60 + 30 + (31.5/33 × 10) = **99.55** GOLDEN

---

### Score Summary

| V | C-37 | C-38 | C-39 | C-40 | C-41 | C-29 | C-33 | Aspir. | Score | Band |
|---|------|------|------|------|------|------|------|--------|-------|------|
| V-01 | PASS | PARTIAL | PASS | PASS | PASS | PASS | PASS | 32.5/33 | **99.85** | GOLDEN |
| V-02 | FAIL | FAIL | PASS | PASS | PASS | PASS | PASS | 31.0/33 | **99.39** | GOLDEN |
| V-03 | FAIL | FAIL | PASS | PASS | PASS | PASS | PASS | 31.0/33 | **99.39** | GOLDEN |
| V-04 | PASS | PARTIAL | PASS | PASS | PASS | PASS | PASS | 32.5/33 | **99.85** | GOLDEN |
| V-05 | PASS | PARTIAL | PASS | PASS | PASS | PARTIAL | PARTIAL | 31.5/33 | **99.55** | GOLDEN |

**Rank:** V-01 = V-04 (99.85) › V-05 (99.55) › V-02 = V-03 (99.39)

---

### C-38 Frontier Analysis

All three combined variates (V-01, V-04, V-05) achieve C-38 PARTIAL but not PASS. The shared structure — Phase 1 (Anchor-Orthogonality combining enumeration + anchor-testing) and Phase 2 (Non-Anchor Pairwise) — exceeds the PARTIAL condition but does not satisfy the strict "at least three named phases" PASS condition. The missing element: a separately named enumeration phase (list all verify questions) prior to the anchor-orthogonality check. R8 V-02's four-step structure (Step 1 list, Step 2 anchor-ortho, Step 3 non-anchor pairwise, Step 4 revise) was the C-38 PASS reference. V-01/V-04/V-05's Phase 1 merges Steps 1+2 into one named phase, reducing the structure to 2 named phases plus a Resolution/revision step.

**C-38 full PASS requires:** a separately named enumeration step before the anchor-orthogonality check — "Step 1: list all primary verify questions from all completed cards" as its own labeled phase, then "Step 2: anchor-orthogonality check," then "Step 3: non-anchor pairwise check," then resolution. Round 10 should target this specifically.

---

### Excellence Signals from V-01 and V-04

**Signal 1 — Three-site ANCHOR-CARD propagation chain**
The inertia-advocate's anchor status is established at Phase 3 (STOCK-ROLES definition), enforced at Phase 5 (Diagnosis Card write-first mandate), and persisted to YAML (`anchor: true` field). Three independently checkable enforcement sites ensure the ordering constraint cannot be skipped at any stage of the pipeline.

**Signal 2 — Asymmetric field schema (anchor must-NOT constraint)**
The YAML schema explicitly states that the ANCHOR-CARD file carries `anchor: true` and must NOT carry `orthogonality`, while non-anchor files carry `orthogonality` and must NOT carry `anchor`. The negative constraint on the anchor side (absence of `orthogonality` from the anchor YAML) is as important as the positive constraint on non-anchor sides. This asymmetry makes the schema machine-checkable by downstream consumers.

**Signal 3 — Orthogonality verbatim copy mandate**
The `orthogonality to ANCHOR-CARD` value in the Diagnosis Card is explicitly marked "this value is copied verbatim to the YAML `orthogonality` field." This two-artifact provenance chain (Diagnosis Card → YAML) ensures the reasoning step and the persistent artifact carry identical content and are cross-verifiable.

**Signal 4 — Per-role PASS/FLAG records in Phase 1 scan**
V-01/V-04's scan requires "Record PASS or FLAG per non-anchor role before proceeding to Phase 2." The scan produces a per-role documented record, not just an undocumented internal check. This record is checkable before YAML writing begins and provides evidence for the revision step.

**Patterns not yet captured by any criterion (Round 10 candidates):**
- YAML-level anchor sentinel field (`anchor: true` as machine-readable anchor marker) — C-37 tests Diagnosis Card pipeline, not YAML output
- Separately named enumeration phase as prerequisite to anchor-orthogonality check — the gap in C-38 PARTIAL that blocks 100.00
- Per-role PASS/FLAG documentation in the cross-set scan (scan produces records, not just revisions)

---

```json
{"top_score": 99.85, "all_essential_pass": true, "new_patterns": ["three-site ANCHOR-CARD propagation chain: Phase 3 designation → Phase 5 write-first mandate → YAML anchor:true sentinel — three independently checkable enforcement sites", "asymmetric YAML field schema: ANCHOR-CARD carries anchor:true and must NOT carry orthogonality; non-anchor files carry orthogonality and must NOT carry anchor — absence constraint as load-bearing as presence constraint", "orthogonality verbatim-copy mandate: Diagnosis Card orthogonality-to-ANCHOR-CARD value explicitly marked for verbatim copy to YAML field, creating two-artifact provenance chain", "per-role PASS/FLAG records in Phase 1 scan: scan requires documented PASS or FLAG per non-anchor role before Phase 2 begins, making scan output a verifiable artifact rather than an undocumented check"]}
```
