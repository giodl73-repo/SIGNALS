Written to `simulations/quest/golden/scout-size-variate-R15-2026-03-17.md`.

---

## Scout-Size Prompt Variations — R15

**Round**: 15 | **Rubric**: v15 (C-01–C-39, 31 aspirational) | **R14 champion**: V-05

### What R15 addresses

v15 formalized two criteria from R14 V-05 excellence signals:

| Criterion | What it requires | R14 gap |
|-----------|-----------------|---------|
| **C-38** | Phase 0 gate as formal table with STATUS + CLOSED-LABEL columns per precondition row | V-01–V-04 used prose or prose/table hybrid — CLOSED reason not co-located as schema column |
| **C-39** | Three-field WRONG block wrapped in `── DIAGNOSTIC PATTERN ──` named section header | V-01–V-04 embedded the block in CHECKPOINT/WRONG sections without a named diagnostic container |

R14 V-05 already satisfies both. R15 explores whether they propagate to simpler architectures, and pushes the champion toward C-40/C-41.

---

### Variation axes

| Var | Axis | Key structural changes from R14 counterpart |
|-----|------|---------------------------------------------|
| **V-01** | Inertia framing — single-phase, no role separation | Phase 0 prose → formal STATUS/CLOSED-LABEL table (C-38); WRONG block → `── DIAGNOSTIC PATTERN ──` section (C-39) |
| **V-02** | Phrasing register — second-person throughout, single-phase | Same C-38 + C-39 additions; all DIAGNOSTIC PATTERN fields in second-person observer stance ("your gap is derivable…") |
| **V-03** | Role sequence — two-phase full C-20 cluster | Phase 0 table upgrade (C-38); Phase 2 WRONG block wrapped in `── DIAGNOSTIC PATTERN ──` (C-39) |
| **V-04** | Lifecycle emphasis — expanded Phase 0 per-precondition sections retained | Gate-decision summary table RESULT column split into STATUS + CLOSED-LABEL (C-38); Phase 2 `── DIAGNOSTIC PATTERN ──` (C-39) |
| **V-05** | Output format + role sequence — champion evolution | Phase 0 in `── ENTRY GATE ──` delimiter; EVIDENCE column added to gate table beyond C-38 minimum **(C-40 candidate)**; REMEDIATION field added as fourth DIAGNOSTIC PATTERN entry **(C-41 candidate)** |

### Structural novelties in V-05 (C-40/C-41 candidates)

**C-40 candidate — EVIDENCE column**: Extends C-38's structural-encoding principle to the CLEAR verdict. C-38 requires CLOSED-LABEL co-located with the precondition row; C-40 would require an EVIDENCE field naming the specific artifact examined when producing CLEAR — making both outcomes verifiable at the schema level, not just the failure path.

**C-41 candidate — REMEDIATION field**: Closes the diagnostic loop opened by C-39's three-field block. C-39 + C-37 give the model class → detection → cause; C-41 adds correction → making the `── DIAGNOSTIC PATTERN ──` section a complete four-field diagnostic-remediation unit. The self-test query can reference the REMEDIATION directly ("apply the REMEDIATION above") rather than deriving a correction from the failure analysis.
