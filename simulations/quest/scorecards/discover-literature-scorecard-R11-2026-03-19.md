## discover-literature — Round 11 Scorecard

### Rubric Version: v11 (ceiling: 190/190)

---

## Per-Variation Scoring

### Basis: C-01..C-27 Inherited from R10 V-05

All five variations share identical content for every criterion except C-28. The R10 V-05 base achieved ceiling on all 27 prior criteria. Abbreviated evidence for shared criteria; full detail on C-28 only.

---

### V-01 — C-28 Minimal Form (Both Tokens)

| Criterion | Result | Evidence |
|---|---|---|
| C-01 | PASS | Phase 1 extracts 3+ claims with counter-evidence notes before any search |
| C-02 | PASS | Citation table with all 7 required columns |
| C-03 | PASS | All four tier headings with TIER ENTRY/TIER EMPTY tokens |
| C-04 | PASS | Gap analysis with supported/unsupported counts + recommendation keyword |
| C-05 | PASS | Artifact path + frontmatter with all required fields |
| C-06 | PASS | CONTRARY entries reference claim numbers; Phase 5 names most dangerous |
| C-07 | PASS | Real WebSearch evidence visible in citation table |
| C-08 | PASS | HIGH RISK blocks present when needed; 0-risk case explicitly stated |
| C-09 | PASS | PHASE 2 COMPLETE: unconditional; threshold verifiable in every outcome |
| C-10 | PASS | METHODOLOGICAL tier chains to year-dated precedent entries |
| C-11 | PASS | PHASE 1 COMPLETE: carries evidence_type_mapped + counter-evidence-noted |
| C-12 | PASS | RECOVERY NOTE: token with field_name/title_fragment/outcome schema |
| C-13 | PASS | TIER EMPTY: three-field schema; PHASE 3 COMPLETE: tiers_empty_acknowledged field |
| C-14 | PASS | INERTIA SCENARIO: in Phase 1; INERTIA RISK: + verification in Phase 4 |
| C-15 | PASS | ENFORCEMENT CONTRACT covers both OBLIGATION A and B as non-optional |
| C-16 | PASS | All gates produce named tokens: INERTIA SCENARIO:, INERTIA RISK:, THRESHOLD NOT MET:, RECOVERY NOTE:, TIER EMPTY:, PHASE N COMPLETE: |
| C-17 | PASS | Contract names token format for both obligations |
| C-18 | PASS | THRESHOLD NOT MET: covers C-09+C-16 simultaneously |
| C-19 | PASS | OBLIGATION A typed schema: Token/Schema/Fields/Required when/Unacceptable |
| C-20 | PASS | Pair 1 (THRESHOLD NOT MET: + RECOVERY NOTE:) = C-09/C-12/C-16; Pair 2 (PHASE 2+3 COMPLETE:) = C-09/C-13/C-16 |
| C-21 | PASS | Both OBLIGATION A and OBLIGATION B use independent typed schema blocks |
| C-22 | PASS | PHASE 2 COMPLETE: and PHASE 3 COMPLETE: emit unconditionally |
| C-23 | PASS | All four phase boundaries: PHASE 1/2/3/4 COMPLETE: with phase-boundary annotations |
| C-24 | PASS | Two independent C-20-satisfying pairs; remove-either test confirms independence |
| C-25 | PASS | N-of-4 counter advances 1/4 → 2/4 → 3/4 → 4/4 across all four tokens |
| C-26 | PASS | "C-24 Independence Verification" block names both pairs, runs remove-either test, declares C-24 PASS |
| C-27 | PASS | PHASE 1 COMPLETE: carries `inertia_committed=[yes]`; PHASE 4 COMPLETE: carries `inertia_verified=[yes]` |
| **C-28** | **PASS** | Phase 1: "C-28 PASS at Phase 1 boundary: C-27 compliance explicitly declared here -- inertia_committed=[yes] at this token makes the Phase 1 inertia commitment verifiable from this token alone without cross-referencing Phase 4." Phase 4: "C-28 PASS at Phase 4 boundary: C-27 compliance explicitly declared here -- inertia_verified=[yes] at this token makes the Phase 4 inertia verification verifiable from this token alone without cross-referencing Phase 1." Both tokens carry explicit independence claims. C-28 PASS. |

**Essential PASS: 5/5. Score: 60 + 30 + 95 + 5 = 190/190**

---

### V-02 — C-28 Phase-1-Only Test

All criteria C-01..C-27: PASS (inherited from R10 V-05 base; Phase 4 C-27 cross-axis prose is present and complete).

| Criterion | Result | Evidence |
|---|---|---|
| C-27 | PASS | PHASE 1 COMPLETE: carries inertia_committed=[yes]; PHASE 4 COMPLETE: carries inertia_verified=[yes]; C-27 integration confirmed via both tokens |
| **C-28** | **FAIL** | Phase 1 token: carries "C-28 PASS at Phase 1 boundary: C-27 compliance explicitly declared here -- inertia_committed=[yes] at this token makes the Phase 1 inertia commitment verifiable from this token alone without cross-referencing Phase 4." ✓ Phase 4 token: carries C-27 cross-axis prose ("C-27 PASS: cross-axis integration complete -- PHASE 1 COMPLETE: carries inertia_committed=[yes]...") which names C-27 and confirms integration, but contains NO "C-28 PASS at Phase 4 boundary" declaration. A grep on the Phase 4 token finds no C-28 annotation -- compliance at the Phase 4 boundary is absent. C-28 requires both tokens to carry explicit attestations independently. One token is insufficient. |

**Essential PASS: 5/5. Score: 60 + 30 + 95 + 0 = 185/190**

---

### V-03 — C-28 Phase-4-Only Test

All criteria C-01..C-27: PASS (inherited from R10 V-05 base).

| Criterion | Result | Evidence |
|---|---|---|
| C-27 | PASS | PHASE 1 COMPLETE: carries inertia_committed=[yes]; PHASE 4 COMPLETE: carries inertia_verified=[yes] |
| **C-28** | **FAIL** | Phase 4 token: carries "C-28 PASS at Phase 4 boundary: C-27 compliance explicitly declared here -- inertia_verified=[yes] at this token makes the Phase 4 inertia verification verifiable from this token alone without cross-referencing Phase 1." ✓ Phase 1 token: carries "C-27 in progress: Phase 1 dependency satisfied, Phase 4 verification pending" prose which names C-27 and describes the partial state, but contains NO "C-28 PASS at Phase 1 boundary" declaration. A grep on the Phase 1 token finds no C-28 annotation -- compliance at the Phase 1 boundary is absent. Symmetric counterpart to V-02; together they confirm that C-28 requires both boundaries, not one. |

**Essential PASS: 5/5. Score: 60 + 30 + 95 + 0 = 185/190**

---

### V-04 — C-28 Label-Only (No Independence Prose)

All criteria C-01..C-27: PASS (inherited from R10 V-05 base).

| Criterion | Result | Evidence |
|---|---|---|
| C-27 | PASS | PHASE 1 COMPLETE: carries inertia_committed=[yes]; PHASE 4 COMPLETE: carries inertia_verified=[yes] |
| **C-28** | **FAIL** | Phase 1 token: "C-28 PASS." — bare label appended, no prose. Phase 4 token: "C-28 PASS." — bare label appended, no prose. **Assessment against pass condition**: C-28(a) requires the Phase 1 annotation to explicitly name C-27 compliance "stating that inertia commitment is observable from the lifecycle token layer." "C-28 PASS." does not state this — it labels the criterion met but does not articulate the observability claim. C-28(b) requires the Phase 4 annotation to "declare that both Phase 1 and Phase 4 status fields are present, and confirm the additive design property." "C-28 PASS." does neither. The rubric distinguishes V-01 from V-04 precisely because V-01 is "the minimal form that includes the independence claim" — the "verifiable from this token alone without cross-referencing" prose is the required independence articulation. Without it, C-28 compliance is not independently self-declaring at each token; a reader must already know what C-28 means to interpret the bare label. Annotation depth matters: FAIL. |

**Essential PASS: 5/5. Score: 60 + 30 + 95 + 0 = 185/190**

---

### V-05 — v11 Ceiling Synthesis (All 28 Criteria)

All criteria C-01..C-27: PASS (inherited from R10 V-05 base).

| Criterion | Result | Evidence |
|---|---|---|
| C-27 | PASS | PHASE 1 COMPLETE: carries inertia_committed=[yes]; PHASE 4 COMPLETE: carries inertia_verified=[yes]; C-27 PASS: cross-axis integration declared complete |
| **C-28** | **PASS** | Phase 1: "C-28 attestation at Phase 1 boundary: this token independently declares that Phase 1 produced an inertia commitment -- the inertia_committed=[yes] field is the self-declaring signal; no cross-reference to Phase 4 is required to verify C-27(a) compliance here. Single-grep verifiable: grep for PHASE 1 COMPLETE: and read inertia_committed field to confirm C-27(a) satisfied at this boundary. C-28 PASS at Phase 1 boundary." Phase 4: "C-28 attestation at Phase 4 boundary: this token independently declares that Phase 4 discharged the inertia verification -- the inertia_verified=[yes] field is the self-declaring signal; no cross-reference to Phase 1 is required to verify C-27(b) compliance here. Single-grep verifiable: grep for PHASE 4 COMPLETE: and read inertia_verified field to confirm C-27(b) satisfied at this boundary. C-27 PASS: full cross-axis integration complete. C-28 PASS at Phase 4 boundary." Full clause-level naming (C-27(a)/C-27(b)), self-declaring signal identification, and embedded grep instruction. All C-28(a) and C-28(b) conditions met. PASS. |

**Essential PASS: 5/5. Score: 60 + 30 + 95 + 5 = 190/190**

---

## Summary Table

| Variation | C-28 | Score | Ceiling % |
|---|---|---|---|
| **V-01** (C-28 minimal, both tokens) | **PASS** | **190/190** | 100% |
| V-02 (Phase-1-only) | FAIL | 185/190 | 97.4% |
| V-03 (Phase-4-only) | FAIL | 185/190 | 97.4% |
| V-04 (label-only) | FAIL | 185/190 | 97.4% |
| **V-05** (ceiling synthesis) | **PASS** | **190/190** | 100% |

---

## Experimental Results

**V-02 and V-03 confirm: both tokens required.** The symmetric FAIL pair establishes that C-28 cannot be satisfied by annotating one boundary. The parallel with C-25 (N-of-4 counter required at every token) holds exactly.

**V-04 resolves the annotation depth question: FAIL.** The bare "C-28 PASS." label is explicit and not inferred from field presence — but the pass condition requires the annotation to *state* that inertia commitment is observable from the lifecycle token layer, and to confirm the additive design property. A label names the criterion but does not articulate its meaning at the boundary. V-01 becomes confirmed as the minimal ceiling candidate: the independence claim ("verifiable from this token alone without cross-referencing Phase N") is the required minimum articulation.

**V-05 excellence signals** — patterns that elevate it above V-01's minimal form:

1. **Clause-level C-27 specificity**: Naming C-27(a) at Phase 1 and C-27(b) at Phase 4 makes the annotation self-interpreting — a reviewer knows exactly which obligation each boundary satisfies without needing to read the rubric. V-01 says "C-27 compliance explicitly declared here"; V-05 says "C-27(a) compliance here, C-27(b) compliance there."

2. **Self-declaring signal identification**: "the inertia_committed=[yes] field is the self-declaring signal" explicitly names the observable field rather than leaving it implicit. The annotation becomes a pointer to the exact grep target.

3. **Embedded grep instruction**: "Single-grep verifiable: grep for PHASE N COMPLETE: and read [field] to confirm C-27([clause]) satisfied at this boundary" integrates the verification recipe directly into the token annotation. A reviewer has a complete verification workflow from a single token read.

---

## Excellence Signals

**Top patterns from V-05 not present in V-01 (minimal passer):**

- **Clause-level annotation**: Naming the specific C-27 sub-clause (a) or (b) at each boundary enables clause-level verification — a reviewer can confirm partial vs. complete C-27 satisfaction from a single token without knowing how many sub-clauses exist.
- **Self-declaring signal field identification**: Explicitly stating which field is the self-declaring signal removes ambiguity about which field value constitutes the compliance evidence.
- **Integrated grep instruction**: Embedding the grep command pattern in the annotation makes verification operational at read time, not retrospective at audit time.

---

```json
{"top_score": 190, "all_essential_pass": true, "new_patterns": ["Clause-level C-27 annotation: naming C-27(a) at Phase 1 and C-27(b) at Phase 4 makes each annotation self-interpreting without requiring rubric knowledge -- reviewer can confirm partial vs complete C-27 satisfaction from a single token", "Embedded grep instruction in annotation: 'Single-grep verifiable: grep for PHASE N COMPLETE: and read [field] to confirm C-27([clause]) satisfied at this boundary' integrates verification recipe directly into the token, making compliance operational at read time"]}
```
