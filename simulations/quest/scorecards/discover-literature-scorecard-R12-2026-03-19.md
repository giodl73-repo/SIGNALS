## Round 12 Scorecard — discover-literature (v12 rubric)

---

### Pre-Scoring Analysis

All five variations share identical C-01..C-28 infrastructure (established through R11). The only differentiator is C-29. I verify each variation's Phase 1 and Phase 4 annotations against the three-element C-29 pass condition.

**C-29 pass condition checklist (must be present at BOTH boundaries):**
- (1) Sub-clause designation: names `C-27(a)` at Phase 1, `C-27(b)` at Phase 4 (or equivalent)
- (2) Self-declaring signal identification: names the specific field (e.g., "the `inertia_committed=[yes]` field is the self-declaring signal")
- (3) Embedded grep instruction: "Single-grep verifiable: grep for [token] and read [field] to confirm C-27(N) satisfied at this boundary"

---

### Per-Variation C-29 Element Audit

| Variation | Phase 1: Sub-clause | Phase 1: Signal ID | Phase 1: Grep | Phase 4: Sub-clause | Phase 4: Signal ID | Phase 4: Grep | C-29 |
|-----------|--------------------|--------------------|---------------|--------------------|--------------------|---------------|------|
| V-01 | `C-27(a)` ✓ | `inertia_committed=[yes]` ✓ | ABSENT ✗ | `C-27(b)` ✓ | `inertia_verified=[yes]` ✓ | ABSENT ✗ | **FAIL** |
| V-02 | `C-27 Phase-1 status` (not `(a)` notation) ✗ | `inertia_committed=[yes]` ✓ | Present ✓ | `C-27 Phase-4 status` ✗ | `inertia_verified=[yes]` ✓ | Present ✓ | **FAIL** |
| V-03 | `C-27(a)` ✓ | `inertia_committed=[yes]` ✓ | Present ✓ | Generic "C-27 compliance" ✗ | Implied only ✗ | ABSENT ✗ | **FAIL** |
| V-04 | Generic "C-27 compliance" ✗ | Implied only ✗ | ABSENT ✗ | `C-27(b)` ✓ | `inertia_verified=[yes]` ✓ | Present ✓ | **FAIL** |
| V-05 | `C-27(a)` ✓ | `inertia_committed=[yes]` ✓ | Present ✓ | `C-27(b)` ✓ | `inertia_verified=[yes]` ✓ | Present ✓ | **PASS** |

**V-02 sub-clause ruling:** The rubric gives `"C-27 Phase-1 status satisfied"` as the canonical C-28 example. However, C-29 pass condition requires `"explicitly names C-27(a) (or equivalent sub-clause label designating the Phase 1 dependency)"`. The phrase `"C-27 Phase-1 status"` is a C-28-level designator (phase-specific but not a formal sub-clause label). The C-29 design intent — making the grep instruction interpretable by linking it to a specific sub-clause identifier — requires `(a)`/`(b)` notation or equivalent formal sub-clause designator. `"Phase-1 status"` is a descriptor, not a sub-clause label. C-29 FAIL confirmed.

**V-03 Phase 4 ruling:** Phase 4 annotation reads `"C-28 PASS at Phase 4 boundary: C-27 compliance explicitly declared here -- inertia_verified=[yes] at this token makes the Phase 4 inertia verification verifiable from this token alone without cross-referencing Phase 1."` — no sub-clause designation, no explicit signal naming, no grep instruction. Pure C-28 level. C-29(b) FAIL.

**V-04 Phase 1 ruling:** Phase 1 annotation reads `"C-28 PASS at Phase 1 boundary: C-27 compliance explicitly declared here -- inertia_committed=[yes] at this token makes the Phase 1 inertia commitment verifiable from this token alone without cross-referencing Phase 4."` — no sub-clause designation, no explicit "self-declaring signal" naming, no grep instruction. Pure C-28 level. C-29(a) FAIL.

---

### Full Criterion Scores (All Variations)

**All five variations are identical on C-01..C-28.** The table below shows the shared base plus the C-29 delta.

| Criterion | Weight | Pts | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|--------|-----|------|------|------|------|------|
| **ESSENTIAL** |
| C-01 Claims Extracted Before Search | 12 | 12 | PASS | PASS | PASS | PASS | PASS |
| C-02 Citation Table Present | 12 | 12 | PASS | PASS | PASS | PASS | PASS |
| C-03 Four-Tier Literature Map Built | 12 | 12 | PASS | PASS | PASS | PASS | PASS |
| C-04 Gap Analysis Recommendation Issued | 12 | 12 | PASS | PASS | PASS | PASS | PASS |
| C-05 Artifact Written with Required Frontmatter | 12 | 12 | PASS | PASS | PASS | PASS | PASS |
| **Essential subtotal** | | **60** | 60 | 60 | 60 | 60 | 60 |
| **RECOMMENDED** |
| C-06 Contrary Evidence Mapped to Claims | 10 | 10 | PASS | PASS | PASS | PASS | PASS |
| C-07 WebSearch Evidence Visible | 10 | 10 | PASS | PASS | PASS | PASS | PASS |
| C-08 High-Risk Claims Flagged | 10 | 10 | PASS | PASS | PASS | PASS | PASS |
| **Recommended subtotal** | | **30** | 30 | 30 | 30 | 30 | 30 |
| **ASPIRATIONAL** |
| C-09 Depth Mode Source Threshold Met | 5 | 5 | PASS | PASS | PASS | PASS | PASS |
| C-10 Methodological Precedent Chain | 5 | 5 | PASS | PASS | PASS | PASS | PASS |
| C-11 Interrogative Obligation Satisfied | 5 | 5 | PASS | PASS | PASS | PASS | PASS |
| C-12 Anti-Placeholder Recovery Executed | 5 | 5 | PASS | PASS | PASS | PASS | PASS |
| C-13 Empty-Tier Acknowledgment Present | 5 | 5 | PASS | PASS | PASS | PASS | PASS |
| C-14 Inertia Guard on PROCEED | 5 | 5 | PASS | PASS | PASS | PASS | PASS |
| C-15 Dual-Domain Obligation Preamble | 5 | 5 | PASS | PASS | PASS | PASS | PASS |
| C-16 Template-Label Checkability | 5 | 5 | PASS | PASS | PASS | PASS | PASS |
| C-17 Contract-to-Token Binding | 5 | 5 | PASS | PASS | PASS | PASS | PASS |
| C-18 Multi-Criterion Token Reuse | 5 | 5 | PASS | PASS | PASS | PASS | PASS |
| C-19 Typed Token Schema Block | 5 | 5 | PASS | PASS | PASS | PASS | PASS |
| C-20 Dual Multi-Criterion Token Synthesis | 5 | 5 | PASS | PASS | PASS | PASS | PASS |
| C-21 Symmetric Dual-Obligation Typed Schema | 5 | 5 | PASS | PASS | PASS | PASS | PASS |
| C-22 Unconditional Phase-Boundary Lifecycle Tokens | 5 | 5 | PASS | PASS | PASS | PASS | PASS |
| C-23 Full-Phase Lifecycle Instrumentation | 5 | 5 | PASS | PASS | PASS | PASS | PASS |
| C-24 Redundant Dual-Path Multi-Criterion Infrastructure | 5 | 5 | PASS | PASS | PASS | PASS | PASS |
| C-25 N-of-4 Progressive Counter Annotation | 5 | 5 | PASS | PASS | PASS | PASS | PASS |
| C-26 Named Independence Verification Block | 5 | 5 | PASS | PASS | PASS | PASS | PASS |
| C-27 Inertia Status Lifecycle Integration | 5 | 5 | PASS | PASS | PASS | PASS | PASS |
| C-28 Inertia Status Token Annotation Explicitness | 5 | 5 | PASS | PASS | PASS | PASS | PASS |
| **C-29 Attestation Operationalization** | 5 | 5 | **FAIL** | **FAIL** | **FAIL** | **FAIL** | **PASS** |
| **Aspirational subtotal** | | **105** | 100 | 100 | 100 | 100 | 105 |
| **TOTAL** | | **195** | **190** | **190** | **190** | **190** | **195** |

---

### C-28 Confirmation for All Variations

C-28 requires explicit C-27 compliance annotation at each boundary (self-declaring, independently verifiable). All five variations carry this — confirming C-29 is the only open question and all FAIL variations hold their C-28 base:

| Variation | Phase 1 C-28 annotation style | Phase 4 C-28 annotation style | C-28 |
|-----------|-------------------------------|-------------------------------|------|
| V-01 | Names C-27(a) + self-declaring signal. No grep. Explicitly "C-28 PASS" | Names C-27(b) + self-declaring signal. No grep. Explicitly "C-28 PASS" | PASS |
| V-02 | "C-27 Phase-1 status satisfied" (canonical C-28 example per rubric) + grep present | "C-27 Phase-4 status satisfied" + grep present | PASS |
| V-03 | Full C-28 annotation (sub-clause + signal) | "C-27 compliance explicitly declared" + "verifiable from this token alone" | PASS |
| V-04 | "C-27 compliance explicitly declared" + "verifiable from this token alone" | Full C-28 annotation (sub-clause + signal) | PASS |
| V-05 | Full C-28 + C-29 annotation | Full C-28 + C-29 annotation | PASS |

---

### Scores and Rankings

| Rank | Variation | Score | All Essential Pass | Golden Bar | C-29 |
|------|-----------|-------|-------------------|------------|------|
| 1 | **V-05** | **195/195** | YES | YES | PASS |
| 2 | V-01 | 190/195 | YES | YES | FAIL — missing grep at both boundaries |
| 2 | V-02 | 190/195 | YES | YES | FAIL — missing formal sub-clause notation at both boundaries |
| 2 | V-03 | 190/195 | YES | YES | FAIL — Phase 4 missing all three elements |
| 2 | V-04 | 190/195 | YES | YES | FAIL — Phase 1 missing all three elements |

**Prediction accuracy: 5/5.** All four FAIL variations confirmed at 190/195; V-05 confirmed at 195/195.

---

### Experiment Confirmations

| Experiment | Confirmed |
|------------|-----------|
| V-01: Grep instruction is the necessary C-29 operationalization act — sub-clause + signal without grep is richer C-28, not C-29 | CONFIRMED |
| V-02: Formal sub-clause notation (`(a)`/`(b)`) required; descriptive phase qualifier (`Phase-1 status`) is C-28-level designator | CONFIRMED |
| V-03: C-29 both-or-nothing (Phase 1 side) — full Phase 1 C-29 + Phase 4 C-28 only = FAIL | CONFIRMED |
| V-04: C-29 both-or-nothing (Phase 4 side) — full Phase 4 C-29 + Phase 1 C-28 only = FAIL | CONFIRMED |
| V-05: All three elements at both boundaries = 195/195 ceiling | CONFIRMED |

**C-29 both-or-nothing property confirmed** by V-03 and V-04 symmetrically, matching the C-28 both-or-nothing confirmation from R11 V-02/V-03. Each new criterion in the `C-27 -> C-28 -> C-29` chain inherits the boundary symmetry requirement from its predecessor.

---

### Excellence Signals (V-05)

**Signal 1 — Three-element indivisibility:** Sub-clause designation + self-declaring signal identification + grep instruction form an indivisible C-29 unit. Each serves the others: the sub-clause makes the grep instruction interpretable ("confirm C-27(a)" is phase-specific; "confirm C-27" is ambiguous); the signal identification names what the grep should read; the grep converts interpretation into execution. Removing any one element breaks the chain.

**Signal 2 — Both-or-nothing inheritance pattern:** C-29 inherits C-28's boundary symmetry requirement. Each new criterion added to the `C-27 -> C-28 -> C-29` dependency chain must satisfy the both-boundaries constraint established at C-28. This is a general design principle: annotation-layer criteria (C-28, C-29) are inherently symmetric — a boundary that isn't annotated is an observability gap, and partial annotation is the same as none.

**Signal 3 — Separate PASS declarations per criterion at each boundary:** V-05 declares `C-28 PASS at Phase 1 boundary` and `C-29 PASS at Phase 1 boundary` as distinct statements, then repeats at Phase 4. This makes each step in the `C-28 -> C-29` compliance ladder individually verifiable rather than merged into a single "everything passes here" block.

**Signal 4 — Complete dependency chain closure at final token:** V-05 Phase 4 ends with: `"C-29 fully satisfied at both Phase 1 and Phase 4 boundaries: C-29(a) confirmed at PHASE 1 COMPLETE:, C-29(b) confirmed here. Dependency chain C-14 + C-23 -> C-27 -> C-28 -> C-29 complete."` This closes the multi-criterion arc explicitly, making the entire compliance path verifiable from a single annotation point at the run's completion.

---

```json
{"top_score": 195, "all_essential_pass": true, "new_patterns": ["Three-element indivisibility: sub-clause designation + self-declaring signal ID + grep instruction form an indivisible C-29 unit — each element serves the others; removing any one breaks the operationalization chain", "Both-or-nothing inheritance: C-29 inherits C-28's boundary symmetry property — each criterion added to the annotation-layer dependency chain must satisfy both boundaries independently", "Separate per-criterion PASS declarations at each boundary: declaring C-28 PASS and C-29 PASS as distinct statements at each boundary makes each compliance step individually grep-verifiable rather than merged", "Dependency chain closure at final token: explicitly closing the full chain (C-14 + C-23 -> C-27 -> C-28 -> C-29 complete) at Phase 4 makes the entire compliance arc verifiable from the run's terminal annotation"]}
```
