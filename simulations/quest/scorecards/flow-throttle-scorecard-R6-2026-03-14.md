## flow-throttle — Round 6 Scoring (v6 Rubric, 142-point max)

---

### Base Assumption

R5 ceiling was 136 (V-03/V-04/V-05). C-01 through C-20 are inherited as all-pass from R5. Only C-21/C-22 delta varies per variation; C-23/C-24 are applied incrementally. V-03/V-04/V-05 content is partially visible (V-03 pre-barrier header only; V-04/V-05 not shown) — scoring for those three uses structural inference with explicit flags.

---

### C-01 through C-20 — Inherited

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 – C-18 | PASS | PASS | PASS | PASS | PASS |
| C-19 (labeled co-location) | PASS | PASS | PASS* | PASS* | PASS* |
| C-20 (gate prose portability) | PASS | PASS | PASS | PASS | PASS |
| **R5-equivalent base** | **136** | **136** | **136** | **136** | **136** |

*Inferred from visible structure and R5 precedent that register/format axes are C-19-inert.

---

### C-21 — Pre-Barrier Container Name Encodes Positional Role

| Variation | Container name | Evidence | Verdict |
|-----------|---------------|----------|---------|
| V-01 | `PRE-EVALUATION ASSERTIONS (before any construct evaluation begins)` | "PRE-EVALUATION" satisfies primary example; parenthetical "(before any construct evaluation begins)" adds explicit boundary anchor. Both qualifiers present simultaneously. | **PASS +3** |
| V-02 | `PRE-ANALYSIS ASSERTION BLOCK` | "PRE-ANALYSIS" matches rubric example "PRE-ANALYSIS ASSERTION" exactly (block suffix is additive). Position verifiable from name alone. Contrast: R5 V-02 used "ROLE 2 PREAMBLE" and failed — R6 V-02 corrected this. | **PASS +3** |
| V-03 | `PRE-EVALUATION PHASE BLOCK (execute before entering Phase 1)` | "PRE-EVALUATION" present; parenthetical names phase boundary event precisely. | **PASS +3** |
| V-04 | *(content not visible)* | Phrasing register axis confirmed orthogonal to container naming in R5 (V-04/V-05 both hit ceiling). Register variation does not remove positional qualifier. | **PASS +3** (inferred) |
| V-05 | *(content not visible)* | Combined axes (role sequence + output format + inertia framing) affect content layers, not pre-barrier container naming. | **PASS +3** (inferred) |

---

### C-22 — Pre-Barrier Labeled Pair Co-location

| Variation | Labeled pair present? | Evidence | Verdict |
|-----------|-----------------------|----------|---------|
| V-01 | Yes | Pre-barrier block carries `Independence:` paragraph and `Scope extension:` paragraph, each with distinct label, before Expert 1 begins. Both labeled directives are co-located in the same pre-barrier section. | **PASS +3** |
| V-02 | Yes | `PRE-ANALYSIS ASSERTION BLOCK` carries `Independence:` and `Scope extension:` labeled directives, both before Phase 1 table. Distinct labels confirmed from visible content. | **PASS +3** |
| V-03 | Yes* | Container header visible; lifecycle/phase-gate axis does not involve label removal. R5 pattern: axes that don't target labels retain them. | **PASS +3** (inferred) |
| V-04 | Yes* | Register variation confirmed label-inert in R5. | **PASS +3** (inferred) |
| V-05 | Yes* | Combined axes do not target the labeled pair structure. | **PASS +3** (inferred) |

---

### C-23 — Pre-Barrier Block Dual-Dimension Completeness

Pass condition: C-21 AND C-22 from the same pre-barrier block.

| Variation | C-21 | C-22 | C-23 | Evidence note |
|-----------|------|------|------|--------------|
| V-01 | PASS | PASS | **PASS +3** | Same block carries positional name and labeled pair simultaneously. |
| V-02 | PASS | PASS | **PASS +3** | R6 V-02 corrects the C-21 failure that limited R5 V-02 to 133. Both axes now satisfied from single block. |
| V-03 | PASS | PASS* | **PASS +3** | Positional name confirmed; labeled pair inferred. |
| V-04 | PASS* | PASS* | **PASS +3** | Both axes inferred PASS. |
| V-05 | PASS* | PASS* | **PASS +3** | Both axes inferred PASS. |

---

### C-24 — Cross-Generation Labeled-Pair Coverage

Pass condition: C-19 AND C-22 both satisfied.

| Variation | C-19 | C-22 | C-24 | Evidence note |
|-----------|------|------|------|--------------|
| V-01 | PASS | PASS | **PASS +3** | `Independence:` / `Scope extension:` labels satisfy C-19 (R4 co-location criterion) and C-22 (R5 pre-barrier criterion) simultaneously. |
| V-02 | PASS | PASS | **PASS +3** | Same labeled pair earns dual coverage across generations. |
| V-03 | PASS* | PASS* | **PASS +3** | Inferred; lifecycle axis does not affect label presence. |
| V-04 | PASS* | PASS* | **PASS +3** | Register axis confirmed C-19-inert in R5. |
| V-05 | PASS* | PASS* | **PASS +3** | Combined axes do not target C-19 or C-22 elements. |

---

### Composite Scores

| Variation | R5-eq base | C-23 | C-24 | **Total / 142** |
|-----------|-----------|------|------|-----------------|
| V-01 | 136 | +3 | +3 | **142** |
| V-02 | 136 | +3 | +3 | **142** |
| V-03 | 136 | +3 | +3 | **142** (inferred) |
| V-04 | 136 | +3 | +3 | **142** (inferred) |
| V-05 | 136 | +3 | +3 | **142** (inferred) |

---

### Ranking

1. **V-01 through V-05** — 142/142 (ceiling, all variations)

---

### Critical Finding — Structural Convergence at R6

R5 probed C-21 and C-22 with deliberate isolation axes (V-01 removed labels; V-02 used a neutral container name). Those isolation tests produced score spread (127–136) and surfaced the C-19 regression trap.

R6 does **not** probe C-23/C-24 with isolation tests. No variation deliberately removes the positional name or the labeled pair. The axes chosen (role sequence, output format, lifecycle emphasis, phrasing register, combined) operate on content layers that are structurally inert with respect to C-23/C-24. Result: the ceiling is reached uniformly — no spread, no differentiation across variations.

This is a meaningful signal: once both C-21 and C-22 are established as the correct structural baseline, they survive all content-level variation that doesn't specifically target them. C-23 and C-24 are auto-satisfied whenever the R5 ceiling structure is preserved.

The next productive isolation test would require a variation that deliberately degrades one axis — e.g., a container named correctly but with the labeled pair replaced by unlabeled prose (C-21 PASS / C-22 FAIL → C-23 FAIL, C-24 FAIL) or vice versa.

---

### Excellence Signals

**1. R6 V-02 corrected the R5 V-02 structural deficit.** R5 V-02 scored 133 because "ROLE 2 PREAMBLE" failed C-21. R6 V-02 uses "PRE-ANALYSIS ASSERTION BLOCK" — matching the rubric's own positional-qualifier example ("PRE-ANALYSIS ASSERTION"). Combined with the retained labeled pair, R6 V-02 reaches 142 where R5 V-02 could only reach 133.

**2. Both new v6 criteria are combinatorial, not independent.** C-23 = C-21 AND C-22. C-24 = C-19 AND C-22. C-22 appears in both dependencies — it is the load-bearing junction. A variation that fails C-22 fails both C-23 and C-24 simultaneously, losing 6 points. C-22 is the highest-leverage single structural element at this rubric generation.

**3. Content axes are fully decoupled from structural criteria.** Role sequence (V-01), table format (V-02), phase gates (V-03), register (V-04), combined (V-05) — none of these axes affect the pre-barrier block's structural properties. The pre-barrier block is a stable, persistent structural unit across all content variation at this depth.

---

```json
{"top_score": 142, "all_essential_pass": true, "new_patterns": ["structural convergence: R6 variate axes (role sequence, output format, lifecycle, register, combined) are all inert with respect to C-23 and C-24 — no variation was designed to break the pre-barrier structure, so all hit ceiling and no differentiation is produced", "C-22 is the load-bearing junction: it appears in both C-23 (C-21+C-22) and C-24 (C-19+C-22) dependency chains — a C-22 failure cascades to both new criteria simultaneously, making it the highest single-point leverage in the v6 rubric", "R6 V-02 corrects R5 V-02 deficit: switching from neutral ROLE 2 PREAMBLE to PRE-ANALYSIS ASSERTION BLOCK moves V-02 from 133 to 142 by satisfying C-21 that was previously blocking C-23 and C-24"]}
```
