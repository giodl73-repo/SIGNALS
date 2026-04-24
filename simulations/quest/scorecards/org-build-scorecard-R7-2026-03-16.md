# Quest Score — org-build Round 7

**Rubric version**: v6 | **Denominator**: 16 aspirational | **Variations received**: V-01 only (V-02 through V-05 not provided)

---

## V-01 — Inertia-First Ordering

### Essential Criteria (5/5)

| ID | Verdict | Evidence |
|----|---------|----------|
| **C-01** | PASS | Artifact Generation section requires ASCII hierarchy with box/line diagram, explicitly forbids flat name list. |
| **C-02** | PASS | Phase T3 states MUST for all five fields (`orientation`, `lens`, `expertise`, `scope`, `collaborates_with`) in every role file. |
| **C-03** | PASS | Preamble: "The inertia-advocate role MUST appear in every execution regardless of depth, verdict, or input source." Unconditional. |
| **C-04** | PASS | "standard → 20–30 files. `--depth deep` → 50+ files. FORBIDDEN: falling below the lower bound." Both bounds and depth flag addressed. |
| **C-05** | PASS | Artifact Generation explicitly lists all five columns including `Decides` and `Escalates`; "Missing Decides or Escalates columns FAILS." |

**Essential: 5/5 → 60.0 pts**

---

### Recommended Criteria (3/3)

| ID | Verdict | Evidence |
|----|---------|----------|
| **C-06** | PASS | T2 phase: "Each area becomes a subdirectory under `.roles/`. MUST produce minimum 2 area subdirectories." |
| **C-07** | PASS | T2 table names ROB + Shiproom + Governance Forum (3 distinct rows). Charter requirement with all five fields including `Quorum` as N of M fraction is explicit. |
| **C-08** | PASS | Artifact Generation verdict block uses `{{T1-PRESSURE}}` and `{{T1-VERDICT}}` template slots; "Only one verdict. Both is an error. Neither is an error." |

**Recommended: 3/3 → 30.0 pts**

---

### Aspirational Criteria (14/16)

| ID | Verdict | Evidence |
|----|---------|----------|
| **C-09** | PASS | Row 1 = headcount threshold; Row 2 = "different trigger category (velocity, coupling, or governance signal)"; "Two headcount thresholds FAILS." |
| **C-10** | PASS | T4: "every 'Why It Applies Here' cell MUST open with `[element name] (cat-N) —` syntax." MUST enforced. |
| **C-11** | PASS | T3 input contract: "MUST read `T1-PRESSURE` from the T1 Record Block to select the IA scope template." IA scope template table is keyed to T1-PRESSURE. |
| **C-12** | PASS | T4 derivation block explicitly ties category selection to `T1-VERDICT`: two closed-set mappings, one per verdict path. "Category choices independent of structure FAIL." |
| **C-13** | PASS | "FORBIDDEN: writing both verdicts. FORBIDDEN: omitting both verdicts. Only one verdict. Both is an error. Neither is an error." Symmetric and explicit. |
| **C-14** | PASS | T1 gate declares T1-PRESSURE and T1-VERDICT; T2 input contract: "MUST read `T1-VERDICT` and `T1-PRESSURE` from the T1 Record Block." Named pair present. |
| **C-15** | PASS | "FORBIDDEN: writing both verdicts. FORBIDDEN: omitting both verdicts." Covers both-direction and neither-direction with symmetric FORBIDDEN framing. |
| **C-16** | PASS | T4: "Every Mitigation cell MUST contain a specific remediation action — not format guidance or column-structure instructions." Explicitly excludes format guidance from Mitigation cells. |
| **C-17** | PASS | T3: "paraphrase FAILS; apply verbatim." T3 Record Block field `T3-IA-SCOPE: [exact verbatim template text from table above]` locks verbatim requirement. |
| **C-18** | PASS | T4: CAN-OPERATE-FLAT "FORBIDDEN: `cat-1`, `cat-4`"; STRUCTURE-WARRANTED "FORBIDDEN: `cat-2`, `cat-3`." Both paths include an exclusion FORBIDDEN. |
| **C-19** | PASS | No advisory language ("should", "prefer", "typically", "consider") found in any constraint context. All cardinality, ordering, and field constraints use MUST or FORBIDDEN. Imperative "produce" and declarative "each area becomes" are instructions, not advisory constraints. |
| **C-20** | **FAIL** | T2, T3, T4 phases all declare input contracts with named variables. Artifact Generation consumes T1-PRESSURE, T1-VERDICT (via template slots) and T3-IA-SCOPE (via MUST) but carries no formal input contract block for T4 gate variables. T2-AREA-COUNT, T2-RHYTHM-ROWS, and T3-DEPTH are declared at gates but no downstream phase declares an input contract consuming them by name. Systematic coverage requirement not met. |
| **C-21** | **FAIL** | Follows from C-20 gap. Artifact Generation's template-slot references to T1 variables approach the threshold but T4-VERDICT-PATH, T4-REQUIRED-CATS, T4-FORBIDDEN-CATS, T4-AP-COUNT are not referenced by name in any consuming phase input contract, let alone under MUST/FORBIDDEN bindings. Constraint-completeness intersection (C-19 register ∩ C-20 coverage) fails at the Artifact Generation boundary. |
| **C-22** | PASS | Inertia verdict block template: `FLAT-CASE-PRESSURE: {{T1-PRESSURE}}` and `VERDICT: {{T1-VERDICT}}`. Named placeholder slots correspond directly to T1 gate variables. Reader who knows only T1 gate outputs can fill every slot without ambiguity. |
| **C-23** | PASS | Every phase boundary carries the ordering FORBIDDEN twice: once at end of producing phase ("FORBIDDEN: beginning Phase T{N+1} before the T{N} Record Block above is fully materialized") and once at start of consuming phase ("FORBIDDEN: beginning Phase T{N+1} without confirmed variables from the emitted record block"). Four phase boundaries, eight ordering guards total. |
| **C-24** | PASS | T1, T2, T3, T4 each emit a structured record block under `── T{N} GATE ──` framing with named typed variables. Blocks appear after phase work and before the next phase begins. Observable checkpoints at every gate. |

**Aspirational: 14/16 → 8.75 pts**

---

### Score Summary — V-01

| Component | Raw | Max | Points |
|-----------|-----|-----|--------|
| Essential | 5/5 | 60 | 60.00 |
| Recommended | 3/3 | 30 | 30.00 |
| Aspirational | 14/16 | 10 | 8.75 |
| **Composite** | | **100** | **98.75** |

---

## Excellence Signals

V-01 achieves the highest documented score for org-build by solving C-23 and C-24 structurally rather than procedurally. Two patterns are new at this score level:

**1. Double-fence ordering guard**
C-23 requires one ordering FORBIDDEN per phase boundary. V-01 emits two: one at the end of the producing phase (trailing FORBIDDEN under the record block) and one at the start of the consuming phase (input contract preamble). The redundancy is intentional — if a model skips the record block emit, the second fence fires at the consuming phase before any damage propagates. No prior variation has used this double-fence strategy.

**2. Structured record-block header format**
C-24 requires materialized record blocks. V-01 uses a consistent framing (`── T{N} GATE ──────────────────────────────────────`) that makes blocks visually scannable and creates a uniform auditing pattern. The header format allows a reader to locate all four gate checkpoints by scanning for `── T` alone. Prior variations emitted record blocks without a consistent framing convention.

**Existing patterns reinforced at ceiling**
- Bidirectional exclusion (C-15, C-18): FORBIDDEN covers both "both" and "neither" failure modes symmetrically.
- Verbatim-lock via record variable: T3 Record Block field `T3-IA-SCOPE` requires the exact template text, making paraphrase detectable at the checkpoint rather than only at artifact review time.
- Input contracts with MUST at every phase entry: each consuming phase opens with an explicit input contract before any work begins.

**Remaining gap (C-20/C-21)**
The Artifact Generation phase is the only phase without a formal input contract block. Adding a `**Input contract**:` section at the top of Artifact Generation that names T4-VERDICT-PATH, T4-REQUIRED-CATS, T4-FORBIDDEN-CATS, and T4-AP-COUNT under MUST would close both C-20 and C-21, pushing the composite to 100.

---

```json
{"top_score": 98.75, "all_essential_pass": true, "new_patterns": ["double-fence ordering guard: FORBIDDEN emitted at end of producing phase AND repeated at start of consuming phase", "structured record-block header format with consistent ── T{N} GATE ── framing enabling pattern-scan audit"]}
```
