## R15 Scorecard — discover-literature

**Scoring Framework (v15):** 5 essential (12 pts) + 3 recommended (10 pts) + 24 aspirational (5 pts) = **210 ceiling**

### Baseline: C-01 through C-31 — PASS across all five variations

All five variations carry the complete R14 V-05 baseline unchanged. C-01–C-31 are PASS uniformly.

---

### C-32 — The Differentiating Criterion

**Pass condition:** PLACEMENT field AND CELL-SOURCE field each carry an embedded grep instruction as field content. Both-or-nothing. Surrounding prose (even inside the block) does not satisfy C-32.

| Variation | C-32 | Evidence | Score |
|-----------|------|----------|-------|
| **V-05** | **PASS** | Both PLACEMENT and CELL-SOURCE embed grep instructions as field tail content; C-32(a)/(b) declared explicitly in closing; both-or-nothing confirmed | **210/210** |
| V-01 | FAIL | Neither field has a grep instruction — C-31 PASS (self-declaring) but C-32 FAIL (not executable) | 205/210 |
| V-02 | FAIL | PLACEMENT carries grep (C-32(a) PASS); CELL-SOURCE carries no grep (C-32(b) FAIL) — both-or-nothing | 205/210 |
| V-03 | FAIL | CELL-SOURCE carries grep (C-32(b) PASS); PLACEMENT carries no grep (C-32(a) FAIL) — symmetric to V-02 | 205/210 |
| V-04 | FAIL | Both grep instructions inside the block but after the C-31 PASS declaration, outside both labeled fields — in-block containment is insufficient; in-field embedding required | 205/210 |

**Ranking:** V-05 (210) > V-01 = V-02 = V-03 = V-04 (205).

---

### Key Structural Insight

**V-04 is the most instructive failure.** The grep instructions are inside the block — C-31(c)-level containment is met. But they are not inside their respective labeled fields. C-32's in-field embedding requirement is the field-level analog of C-31(c)'s in-block requirement: the structural logic recurses one level deeper. Being inside the block is necessary but not sufficient; each instruction must live inside the field it operationalizes.

**The both-or-nothing chain** — C-28 (both boundary annotations) → C-29 (all three elements at both boundaries) → C-31 (both PLACEMENT and CELL-SOURCE fields) → **C-32 (both fields carry grep instructions)** — each layer inherits the pattern from the one below.

---

```json
{"top_score": 210, "all_essential_pass": true, "new_patterns": ["Embed grep instruction as tail content of PLACEMENT field — field becomes self-verifying without leaving it; PLACEMENT grep inside the field is C-32(a)", "Embed grep instruction as tail content of CELL-SOURCE field — symmetric to C-32(a); CELL-SOURCE grep inside the field is C-32(b)", "C-32 closing declaration names both sub-clauses (a)/(b) explicitly and confirms both-or-nothing, completing the analogy table structural pattern on the operationalization-block axis", "In-field embedding is the field-level analog of C-31(c)'s in-block requirement: the structural-fact/self-declaring/executable-verification pattern recurses one level deeper"]}
```
ility | PASS | PASS | PASS | PASS | PASS | INERTIA SCENARIO:, INERTIA RISK:, THRESHOLD NOT MET:, RECOVERY NOTE:, TIER EMPTY:, PHASE N COMPLETE: all named |
| C-17 Contract-to-token binding | PASS | PASS | PASS | PASS | PASS | OBLIGATION A names RECOVERY NOTE: with schema; OBLIGATION B names TIER EMPTY: with schema |
| C-18 Multi-criterion token reuse | PASS | PASS | PASS | PASS | PASS | THRESHOLD NOT MET: annotated as covering C-09 + C-16; RECOVERY NOTE: covering C-12 + C-16 |
| C-19 Typed token schema block | PASS | PASS | PASS | PASS | PASS | Both OBLIGATION A and B use Token/Schema/Fields/Required when/Unacceptable format |
| C-20 Dual multi-criterion synthesis | PASS | PASS | PASS | PASS | PASS | Pair 1 (failure/recovery): C-09, C-12, C-16; Pair 2 (lifecycle): C-09, C-13, C-16; each independently C-20 |
| C-21 Symmetric dual-schema | PASS | PASS | PASS | PASS | PASS | Both obligations declare independent typed schema blocks with verbatim field name propagation |
| C-22 Unconditional lifecycle tokens | PASS | PASS | PASS | PASS | PASS | PHASE 2 COMPLETE: and PHASE 3 COMPLETE: both annotated as unconditional boundary tokens |
| C-23 Full-phase instrumentation | PASS | PASS | PASS | PASS | PASS | All four PHASE N COMPLETE: tokens present; each names boundary and confirms unconditional emission |
| C-24 Redundant dual-path | PASS | PASS | PASS | PASS | PASS | C-24 Independence Verification block present; remove-either-pair test; C-24 PASS declared |
| C-25 N-of-4 counter | PASS | PASS | PASS | PASS | PASS | Each PHASE token carries "Token N of 4 required for C-23 ... C-23 in progress at N/4" annotation |
| C-26 Named independence block | PASS | PASS | PASS | PASS | PASS | "C-24 Independence Verification" labeled section with (a)-(d) structural elements; C-24 PASS declared |
| C-27 Inertia status integration | PASS | PASS | PASS | PASS | PASS | PHASE 1 COMPLETE: carries `inertia_committed=[yes]`; PHASE 4 COMPLETE: carries `inertia_verified=[yes]` |
| C-28 Annotation explicitness | PASS | PASS | PASS | PASS | PASS | Phase 1: C-27(a) named, single-grep verifiable; Phase 4: C-27(b) named, additive design confirmed |
| C-29 Attestation operationalization | PASS | PASS | PASS | PASS | PASS | Sub-clause (a)/(b) designation, self-declaring signal ID, grep instruction at both boundaries |
| C-30 Named verification block | PASS | PASS | PASS | PASS | PASS | "C-29 Operationalization Verification" present; six cells confirmed; both grep instructions verbatim; C-29 PASS |
| C-31 Block placement citation | PASS | PASS | PASS | PASS | PASS | PLACEMENT and CELL-SOURCE labeled fields both present within the block; C-31(a)/(b)/(c) all satisfied |

---

### C-32 -- C-31 Placement Citation Operationalization

This is the only criterion that differentiates the five variations.

**C-32 pass condition:** The PLACEMENT field and the CELL-SOURCE field within the C-30 named block each carry an embedded grep instruction as field content. Both-or-nothing: one field operationalized and one self-declaring fails C-32. Grep instructions appearing as surrounding prose outside both fields also fails C-32.

---

#### V-01 -- Control (R14 V-05 base, no C-32 additions)

The C-30 block's PLACEMENT and CELL-SOURCE fields contain:

> `PLACEMENT: This block appears after PHASE 4 COMPLETE: (emitted above) -- [...] C-31(a) satisfied: the Phase 4 lifecycle token is named explicitly as a labeled field within this block.`
>
> `CELL-SOURCE: All six cells below draw from already-emitted content -- [...] C-31(b) satisfied: cell-source provenance confirmed as a labeled field within this block.`

Neither field contains a grep instruction. Both are self-declaring at C-31 level. No embedded procedural instruction exists in either field.

**C-32: FAIL** -- Both C-32(a) and C-32(b) absent. The block is self-declaring (C-31 PASS) but not procedurally executable (C-32 FAIL). A reviewer must accept the declaration on faith; no single grep step confirms placement or cell-source independently.

**Score: 205/210**

---

#### V-02 -- PLACEMENT Grep Only (C-32(a) present, C-32(b) absent)

The PLACEMENT field carries an embedded grep instruction as tail content:

> `PLACEMENT: [...] C-31(a) satisfied: the Phase 4 lifecycle token is named explicitly as a labeled field within this block. Single-grep verifiable: grep for PHASE 4 COMPLETE: in output above -- block follows that token; C-31(a) placement confirmed. C-32(a) status: PLACEMENT field carries embedded grep instruction.`

The CELL-SOURCE field carries no grep instruction:

> `CELL-SOURCE: [...] C-31(b) satisfied: cell-source provenance confirmed as a labeled field within this block.`

C-32(a) PASS: PLACEMENT field embeds a grep instruction making placement verification a single deterministic step. C-32(b) absent: CELL-SOURCE is self-declaring only -- no grep instruction allows procedural confirmation of cell-source provenance.

**C-32: FAIL** -- C-32(a) PASS, C-32(b) absent. Both-or-nothing applies identically to C-29/C-31: one field operationalized and one self-declaring leaves cell-source verification executable in reading only, not in execution. Partial operationalization does not satisfy C-32.

**Score: 205/210**

---

#### V-03 -- CELL-SOURCE Grep Only (C-32(b) present, C-32(a) absent)

The PLACEMENT field carries no grep instruction:

> `PLACEMENT: [...] C-31(a) satisfied: the Phase 4 lifecycle token is named explicitly as a labeled field within this block.`

The CELL-SOURCE field carries an embedded grep instruction as tail content:

> `CELL-SOURCE: [...] C-31(b) satisfied: cell-source provenance confirmed as a labeled field within this block. Single-grep verifiable: grep for PHASE 1 COMPLETE: annotation (confirming cells (i)-(iii) draw from already-emitted PHASE 1 COMPLETE: content) and grep for PHASE 4 COMPLETE: annotation (confirming cells (iv)-(vi) draw from already-emitted PHASE 4 COMPLETE: content) in output above -- all six cells reference already-emitted content; C-31(b) cell-source confirmed. C-32(b) status: CELL-SOURCE field carries embedded grep instruction.`

C-32(b) PASS: CELL-SOURCE field embeds a grep instruction making cell-source confirmation procedurally executable. C-32(a) absent: PLACEMENT is self-declaring only -- no grep instruction allows mechanical confirmation that the block follows PHASE 4 COMPLETE:.

**C-32: FAIL** -- C-32(b) PASS, C-32(a) absent. Symmetric failure to V-02. Neither field substitutes for the other: placement verifiability and cell-source verifiability are independently required. A reviewer can execute cell-source confirmation but must accept placement on faith.

**Score: 205/210**

---

#### V-04 -- Both Grep Instructions as Surrounding Prose (not embedded in fields)

PLACEMENT and CELL-SOURCE fields are identical to V-01 (no grep in either field). After the C-31 PASS declaration at the block's close, a bracketed note is appended:

> `[C-32 operationalization note: Single-grep verifiable: grep for PHASE 4 COMPLETE: in output above -- block follows that token; C-31(a) placement confirmed. Single-grep verifiable: grep for PHASE 1 COMPLETE: annotation (confirming cells (i)-(iii) source) and PHASE 4 COMPLETE: annotation (confirming cells (iv)-(vi) source) in output above -- all six cells reference already-emitted content; C-31(b) cell-source confirmed.]`

Both grep instructions are present and both are inside the block. C-31(c)-level containment is satisfied. However, neither grep instruction is embedded within its respective labeled field -- the note is a structural appendage after the C-31 PASS declaration, outside both PLACEMENT and CELL-SOURCE field content.

**C-32: FAIL** -- C-32's in-field embedding requirement is the field-level analog of C-31(c)'s in-block requirement. Just as C-31(c) required PLACEMENT/CELL-SOURCE declarations to live inside the block rather than outside it, C-32 requires each grep instruction to live inside its respective field rather than outside it. A reviewer reading only the PLACEMENT field cannot locate the placement grep instruction within that field; a reviewer reading only the CELL-SOURCE field cannot locate the cell-source grep instruction within that field. Being inside the block is necessary but not sufficient: each instruction must be inside the field it operationalizes.

**Score: 205/210**

---

#### V-05 -- v15 Ceiling Synthesis (C-32 PASS)

Both PLACEMENT and CELL-SOURCE fields carry embedded grep instructions as tail content of their respective fields, before the block's six-cell audit. The PLACEMENT field:

> `PLACEMENT: [...] C-31(a) satisfied: the Phase 4 lifecycle token is named explicitly as a labeled field within this block. Single-grep verifiable: grep for PHASE 4 COMPLETE: in output above -- block follows that token; C-31(a) placement confirmed. C-32(a) satisfied: PLACEMENT field carries embedded grep instruction making C-31(a) placement citation procedurally executable in a single deterministic step.`

The CELL-SOURCE field:

> `CELL-SOURCE: [...] C-31(b) satisfied: cell-source provenance confirmed as a labeled field within this block. Single-grep verifiable: grep for PHASE 1 COMPLETE: annotation (confirming cells (i)-(iii) draw from already-emitted PHASE 1 COMPLETE: content) and grep for PHASE 4 COMPLETE: annotation (confirming cells (iv)-(vi) draw from already-emitted PHASE 4 COMPLETE: content) in output above -- all six cells reference already-emitted content; C-31(b) cell-source confirmed. C-32(b) satisfied: CELL-SOURCE field carries embedded grep instruction making C-31(b) cell-source confirmation procedurally executable in a single deterministic step.`

The block closes with an explicit C-32 PASS declaration:

> `C-32 PASS: PLACEMENT field carries embedded grep instruction making C-31(a) placement citation procedurally executable -- C-32(a) satisfied; CELL-SOURCE field carries embedded grep instruction making C-31(b) cell-source confirmation procedurally executable -- C-32(b) satisfied; both grep instructions embedded within their respective labeled fields as field content, not as surrounding prose outside the fields -- C-32 both-or-nothing confirmed.`

C-32(a) PASS: PLACEMENT field content contains the grep instruction. C-32(b) PASS: CELL-SOURCE field content contains the grep instruction. Both-or-nothing confirmed with explicit sub-clause declaration. Dependency chain extended to C-32.

**C-32: PASS**

**Score: 210/210**

---

### Final Scores

| Variation | Score | C-32 | Delta from V-05 |
|-----------|-------|------|----------------|
| V-05 | **210/210** | PASS | -- |
| V-01 | 205/210 | FAIL | -5 (neither field has grep) |
| V-02 | 205/210 | FAIL | -5 (PLACEMENT grep only, CELL-SOURCE self-declaring) |
| V-03 | 205/210 | FAIL | -5 (CELL-SOURCE grep only, PLACEMENT self-declaring) |
| V-04 | 205/210 | FAIL | -5 (both grep in surrounding prose, not in fields) |

**Ranking:** V-05 (210) > V-01 = V-02 = V-03 = V-04 (205).

---

### Boundary Confirmations (R15)

| Variation | C-32 result | Confirmation |
|---|---|---|
| V-01 R15 | FAIL | Control baseline -- PLACEMENT/CELL-SOURCE present (C-31 PASS) but neither field carries a grep instruction; self-declaring without executable verification |
| V-02 R15 | FAIL | PLACEMENT grep present (C-32(a) PASS), CELL-SOURCE grep absent (C-32(b) FAIL); both-or-nothing property confirmed |
| V-03 R15 | FAIL | CELL-SOURCE grep present (C-32(b) PASS), PLACEMENT grep absent (C-32(a) FAIL); symmetric failure to V-02 confirmed |
| V-04 R15 | FAIL | Both grep instructions inside the block but outside both fields (post-C-31-PASS bracketed note); in-field embedding is the binding requirement, in-block containment is insufficient |

---

### Excellence Signals (V-05)

1. **In-field embedding as tail content** -- Each grep instruction is appended at the end of its respective labeled field, before the six-cell audit begins. A reviewer reading only the PLACEMENT field finds the placement verification procedure without leaving the field. Same for CELL-SOURCE. The grep instruction is inseparable from the declaration it operationalizes.

2. **Explicit C-32(a)/(b) sub-clause confirmation in the closing declaration** -- The closing statement names both sub-clauses explicitly, states both-or-nothing confirmed, and extends the dependency chain to C-32. This mirrors the C-29 and C-31 closing patterns at the same structural level.

3. **Analogy table completion** -- C-32 completes the structural-fact -> self-declaring -> executable-verification pattern on the operationalization-block axis (C-30/C-31/C-32), making it a clean analog of the inertia-integration axis (C-27/C-28/C-29). Both axes now have three layers. The in-field embedding requirement for C-32 is the field-level analog of C-31(c)'s in-block requirement: each level requires the verification artifact to live inside the structural element it verifies.

---

### C-32 Pattern Notes

**V-04 is the most instructive failure:** Both grep instructions are inside the block (clearing C-31(c)'s bar) but outside both labeled fields. This confirms C-32's in-field requirement is a strictly stronger constraint than C-31(c)'s in-block requirement. The structural logic recurses: just as C-31(c) required declarations to be inside the block rather than outside it, C-32 requires grep instructions to be inside their respective fields rather than outside them.

**The both-or-nothing chain:** C-28 required both Phase 1 and Phase 4 boundary annotations. C-29 required all three elements at both boundaries. C-31 required both PLACEMENT and CELL-SOURCE labeled fields. C-32 requires both fields to carry grep instructions. Each layer in the chain inherits both-or-nothing from the layer below it.
