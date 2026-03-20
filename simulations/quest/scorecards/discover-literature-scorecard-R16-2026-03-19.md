Scorecard written to `simulations/quest/scorecards/discover-literature-scorecard-R16-2026-03-19.md`.

---

## R16 Score Results

**Top score: 215/215 (V-05)** | All essential: PASS

### Summary

All five variations are identical on C-01 through C-32. C-33 is the sole differentiator.

| V | Score | C-33 failure mode |
|---|-------|-------------------|
| V-05 | **215** | — full C-33 Compliance Declaration |
| V-04 | 210 | C-33(c) absent — both sub-clauses named but both-or-nothing not stated |
| V-02 | 210 | C-33(b) absent — C-32(a) only, C-32(b) inferrable not self-announcing |
| V-03 | 210 | C-33(a) absent — C-32(b) only, symmetric to V-02 |
| V-01 | 210 | C-33(a)+(b)+(c) absent — bare `C-32 PASS.` label |

### New Patterns

1. **C-33 requires all four elements** — (a) C-32(a) named, (b) C-32(b) named, (c) both-or-nothing stated explicitly, (d) C-32 PASS declared — as a labeled sub-section closing the C-30 block.

2. **Both-or-nothing must be declared, not just satisfied** — V-04 is the canonical failure: naming both sub-clauses without stating the constraint is informative but not structurally complete. Directly parallel to the V-04 R11 bare `C-28 PASS.` failure.

3. **The recursive self-announcing table completes**: C-33 is the block-level closing declaration, closing the operationalization-block axis (C-30/C-31/C-32/C-33) to match the inertia-integration axis (C-27/C-28/C-29/—).

```json
{"top_score": 215, "all_essential_pass": true, "new_patterns": ["C-33 Compliance Declaration requires all four elements — (a) C-32(a) named, (b) C-32(b) named, (c) both-or-nothing stated explicitly, (d) C-32 PASS declared — as a labeled sub-section within the C-30 block", "both-or-nothing must be declared, not just satisfied: listing both sub-clauses without stating the constraint leaves compliance inferrable but not self-announcing (V-04 failure pattern)", "the recursive block-level self-announcing pattern completes: each axis now has structural-fact -> self-declaring -> executable -> block-closing-declaration; C-33 is the terminal element of the operationalization-block axis"]}
```
d carries embedded grep instruction making C-31(a) placement citation procedurally executable in a single deterministic step.`

C-33(a) PASS: C-32(a) named by designator. C-33(b) FAIL: C-32(b) absent from closing. C-33(c) FAIL: no both-or-nothing confirmation. C-33(d) PASS. Both-or-nothing applies: CELL-SOURCE compliance is inferrable from the field itself but not self-announcing from the closing declaration.

**V-03 -- C-32(b) named only**

Closing text: `C-32 PASS: C-32(b) satisfied -- CELL-SOURCE field carries embedded grep instruction making C-31(b) cell-source confirmation procedurally executable in a single deterministic step.`

C-33(a) FAIL: C-32(a) absent. C-33(b) PASS: C-32(b) named. C-33(c) FAIL. C-33(d) PASS. Symmetric failure to V-02. Neither sub-clause can substitute for the other.

**V-04 -- Both sub-clauses named, no both-or-nothing**

Closing text: `C-32 PASS: C-32(a) satisfied -- PLACEMENT field carries embedded grep instruction...; C-32(b) satisfied -- CELL-SOURCE field carries embedded grep instruction...`

C-33(a) PASS. C-33(b) PASS. C-33(c) FAIL: both sub-clauses listed but the constraint that one-and-one fails is not stated. A reviewer cannot determine from the closing alone whether both fields being present was coincidental or structurally required. C-33(d) PASS.

**V-05 -- Full C-33 Compliance Declaration**

Closing includes `C-32 PASS:` with both C-32(a) and C-32(b) declared, `C-32 both-or-nothing confirmed` stated explicitly (one field operationalized and one self-declaring fails C-32; both fields must carry embedded grep instructions), and a labeled `C-33 Compliance Declaration` sub-section naming all four C-33 elements with per-element confirmations before declaring C-33 PASS.

All four elements present. A reviewer hitting the block's final element knows C-32 is satisfied without reading PLACEMENT and CELL-SOURCE individually. C-33 PASS.

---

### Full Score Table

| Criterion | Weight | Pts | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|--------|-----|------|------|------|------|------|
| C-01 through C-05 | essential | 60 | PASS | PASS | PASS | PASS | PASS |
| C-06 through C-08 | recommended | 30 | PASS | PASS | PASS | PASS | PASS |
| C-09 through C-32 | aspirational | 120 | PASS | PASS | PASS | PASS | PASS |
| **C-33** | aspirational | 5 | **FAIL** | **FAIL** | **FAIL** | **FAIL** | **PASS** |
| **TOTAL** | | | **210** | **210** | **210** | **210** | **215** |

**Ranking:** V-05 (215) > V-01 = V-02 = V-03 = V-04 (210).

---

### Key Structural Insight

**V-04 is the most instructive failure.** Both C-32(a) and C-32(b) are named by sub-clause designator -- the informational content is present. But C-33(c) requires the both-or-nothing constraint to be *explicitly stated*. Without that statement, a reviewer reading only the closing cannot determine whether both sub-clauses being present was incidental or architecturally required. The analogy holds: V-04 R16 fails C-33(c) in the same way V-04 R11 failed C-28 with a bare "C-28 PASS." -- informative in content, incomplete in structural self-declaration.

**The recursive self-announcing pattern completes:**

| Axis | Structural fact | Self-declaring | Executable | Block-level closing |
|------|----------------|----------------|------------|---------------------|
| Inertia integration | C-27 | C-28 | C-29 | -- |
| Operationalization block | C-30 | C-31 | C-32 | **C-33** |

C-33 closes the table: the block's final element makes C-32 compliance self-announcing at the block level, eliminating the need to read both labeled fields and infer compliance from their contents.

---

### Excellence Signals from V-05

1. **C-33 Compliance Declaration as a labeled sub-section** -- names all four C-33 elements individually with per-element "confirmed" annotations before declaring C-33 PASS. A reviewer scanning the block's closing encounters a single self-contained compliance proof.

2. **Both-or-nothing must be declared, not just satisfied** -- V-04 demonstrates that satisfying the structural constraint (both fields present) is not the same as declaring the constraint. C-33(c) requires the explicit statement "one field operationalized and one self-declaring fails C-32; both fields must carry embedded grep instructions."

3. **Dependency chain extension** -- V-05 explicitly extends the chain in the block closing: `C-14 + C-23 -> C-27 -> C-28 -> C-29 -> C-30 -> C-31 -> C-32 -> C-33 complete`. Each ceiling synthesis adds one link and makes the chain's terminal element scannable from the block's final position.

---

### Predictions vs. Actuals

| V | Predicted | Actual | Match |
|---|-----------|--------|-------|
| V-01 | FAIL 210/215 | FAIL 210/215 | YES |
| V-02 | FAIL 210/215 | FAIL 210/215 | YES |
| V-03 | FAIL 210/215 | FAIL 210/215 | YES |
| V-04 | FAIL 210/215 | FAIL 210/215 | YES |
| V-05 | PASS 215/215 | PASS 215/215 | YES |

All five predictions confirmed. 5/5.
