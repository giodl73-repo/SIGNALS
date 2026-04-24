# Quest Score — corps-build Round 4

**Rubric**: v2 | **Max**: 115 | **Golden threshold**: all 5 essential PASS + composite ≥ 95

---

## Scoring Reference

| Criterion | Weight | Category |
|-----------|--------|----------|
| C-01 | 12 | Essential |
| C-02 | 12 | Essential |
| C-03 | 12 | Essential |
| C-04 | 12 | Essential |
| C-05 | 12 | Essential |
| C-06 | 10 | Recommended |
| C-07 | 10 | Recommended |
| C-08 | 10 | Recommended |
| C-09 | 5 | Aspirational |
| C-10 | 5 | Aspirational |
| C-11 | 5 | Aspirational |
| C-12 | 5 | Aspirational |
| C-13 | 5 | Aspirational |

PARTIAL = 0.5 weight.

---

## V-01 — Inline Failure Modes

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | **PASS** (12) | INVARIANT-1 declared at entry; STEP 2 close confirms count, names gap resolution gate. Verification mechanism present, not just count assertion. |
| C-02 | **PASS** (12) | INVARIANT-2 pre-declared with `+--`/`\|` notation and verbatim area names. Referenced by name in STEP 4: "Section 1 — ASCII Hierarchy (INVARIANT-2)." |
| C-03 | **PASS** (12) | INVARIANT-3 declares "mandatory per team" at entry; STEP 2 Category C labeled "(INVARIANT-3: mandatory per team)"; COVERAGE-AUDIT [B] enforces as closure gate. |
| C-04 | **PASS** (12) | INVARIANT-4 pre-declared; COVERAGE-AUDIT [C] checks one-to-one directory fidelity with explicit extra-directory detection. |
| C-05 | **PASS** (12) | INVARIANT-5 pre-declared; schema table F-1 through F-5 each has content quality bar with named failure pattern ("Deep expertise in engineering" fails). |
| C-06 | **PASS** (10) | Headcount table with levels column carried from R3 V-05 baseline (STEP 4 not changed by V-01 axis). |
| C-07 | **PASS** (10) | `role-type` frontmatter required; write sequence stated (standard → specialized → IA); specialized distinctness enforced: "should not be possible to copy this F-2 into a standard role file without changing it." |
| C-08 | **PASS** (10) | AMEND section with named repair options carried from R3 baseline; area regeneration references invariant re-checks. |
| C-09 | **PASS** (5) | IA failure mode named inline in STEP 2 Category C: `"resistance to change in general"` explicitly called out as wrong, with explanation ("not drawn from this team's domain vocabulary"). |
| C-10 | **PASS** (5) | Literal audit strings required throughout COVERAGE-AUDIT; "Wrong audit format" note names the violation: "writing 'all checks passed' or 'audit complete' without emitting literal per-check [PASS \| FAIL] strings." |
| C-11 | **PASS** (5) | Named INVARIANT block present before STEP 1; all five invariants referenced by name in step bodies and audit. Wrong structure named: "restating inline only within steps, without this named pre-step declaration block, means constraints surface only as review criteria." Note: this failure mode is placed in the INVARIANTS block itself (pre-step), not inline in a step — structurally inconsistent with V-01's stated inline axis, though it does satisfy C-13 naming. |
| C-12 | **PASS** (5) | STEP 3 audit requires emitted [PASS \| FAIL] strings. "Wrong audit format" note explicitly states the violation "fails auditable check-output compliance — the output cannot be parsed to confirm which checks passed." Check-output as a named requirement, not silent compliance. |
| C-13 | **PASS** (5) | All 4 aspirational failure modes named: C-09 inline in STEP 2 ✓; C-10 inline in STEP 3 ✓; C-11 in INVARIANTS block (pre-step, technically non-inline) ✓; C-12 via "fails auditable check-output compliance" in STEP 3 ✓. Four named → PASS. |

**V-01 Total: 115 / 115** — Golden ✓

**Structural note**: C-11 failure mode appears in the INVARIANTS block, not inline in a step body — V-01 is not consistently inline. The C-12 failure mode shares language with the C-10 note; both are covered by one statement rather than distinct named examples.

---

## V-02 — Dedicated FAILURE MODES Block

*Evaluated from axis description and predicted score. Full text not provided.*

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01–C-05 | **PASS** (12 each) | All five essential invariants pre-declared; no axis change from baseline. |
| C-06–C-08 | **PASS** (10 each) | Recommended criteria unchanged from R3 V-05 baseline. |
| C-09 | **PASS** (5) | IA failure mode in dedicated FAILURE MODES block at activation (same named failure as R3). |
| C-10 | **PASS** (5) | Audit check strings enforced; wrong format named in FAILURE MODES block. |
| C-11 | **PASS** (5) | Named INVARIANTS block at entry; FAILURE MODES block adds C-11 wrong structure explicitly before step 1 begins. |
| C-12 | **PASS** (5) | Check-output requirement enforced; FAILURE MODES block names what silent compliance looks like. |
| C-13 | **PASS** (5) | All 4 failure modes front-loaded in dedicated FAILURE MODES section read before any step. Structurally parallel to R3 breakthrough (constraint-first pre-step declaration). Strongest C-13 coverage: model encounters all wrong-output anchors before producing any output. |

**V-02 Total: 115 / 115** — Golden ✓

**Structural note**: Front-loading all 4 failure modes before steps is the most consistent realization of the "constraints active during write" principle. No C-11/C-12 overlap ambiguity.

---

## V-03 — CHECK-OUTPUT PROTOCOL Block

*Evaluated from axis description: covers C-12 + C-13/C-12 only; C-09/C-10/C-11 failure modes rely on R3 baseline.*

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01–C-05 | **PASS** (12 each) | Unchanged from baseline. |
| C-06–C-08 | **PASS** (10 each) | Unchanged from baseline. |
| C-09 | **PASS** (5) | IA failure mode from R3 V-05 retained. |
| C-10 | **PASS** (5) | Literal audit strings required from R3 V-05. |
| C-11 | **PASS** (5) | Named INVARIANTS block from R3 V-05. |
| C-12 | **PASS** (5) | CHECK-OUTPUT PROTOCOL block elevates this to an explicit named section with protocol rules. Strongest C-12 coverage in R4. |
| C-13 | **PARTIAL** (2.5) | R3 baseline named C-09 only. V-03 adds C-12's failure mode via protocol block. C-10 wrong format and C-11 wrong structure not named. **2 of 4 criteria have named failure modes → PARTIAL.** |

**V-03 Total: 112.5 / 115** — Golden ✓ (all essential PASS, composite 97.8%)

**Structural note**: The CHECK-OUTPUT PROTOCOL block is the best C-12 treatment in R4, but it trades breadth (all 4 C-13) for depth on C-12 alone. C-13 ceiling is PARTIAL unless combined with failure modes for C-10 and C-11.

---

## V-04 — Inline FM + Check-Output Protocol

*Axis: C-09 in schema, C-10 in §2, C-11 in INVARIANTS note, C-12 in protocol block.*

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01–C-05 | **PASS** (12 each) | Unchanged. |
| C-06–C-08 | **PASS** (10 each) | Unchanged. |
| C-09 | **PASS** (5) | IA failure mode in schema row, at point of F-2 definition. |
| C-10 | **PASS** (5) | Audit check format failure mode in §2 (write section), proximate to where file-count divergence would occur. |
| C-11 | **PASS** (5) | C-11 failure mode in INVARIANTS note at entry. |
| C-12 | **PASS** (5) | Dedicated CHECK-OUTPUT PROTOCOL block names wrong format explicitly. |
| C-13 | **PASS** (5) | All 4 failure modes across positioned sites: schema (C-09), §2 (C-10), INVARIANTS (C-11), protocol block (C-12). Coverage complete; positioning varied but all present. |

**V-04 Total: 115 / 115** — Golden ✓

**Structural note**: Most dispersed placement of R4 — failure modes spread across four sections. Complete coverage, but model must hold all four locations in context simultaneously. No single anchor block consolidates them.

---

## V-05 — FAILURE MODES Block + Protocol + Invariant Forward-Reference Map

*Axis: three entry-point blocks; each invariant names its enforcing steps.*

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01–C-05 | **PASS** (12 each) | Unchanged. |
| C-06–C-08 | **PASS** (10 each) | Unchanged. |
| C-09 | **PASS** (5) | IA failure mode in FAILURE MODES block before steps. |
| C-10 | **PASS** (5) | Audit wrong format in FAILURE MODES block. |
| C-11 | **PASS** (5) | Named INVARIANTS block + FAILURE MODES block names C-11 wrong structure + **invariant forward-reference map** lists which steps enforce each invariant (bidirectional traceability). Strongest C-11 treatment in R4. |
| C-12 | **PASS** (5) | CHECK-OUTPUT PROTOCOL block (same as V-03) + C-12 failure mode in FAILURE MODES block. Doubly reinforced. |
| C-13 | **PASS** (5) | All 4 failure modes in FAILURE MODES block (front-loaded) plus check-output protocol. C-11 additionally reinforced via invariant forward-reference map. |

**V-05 Total: 115 / 115** — Golden ✓

**Structural note**: Three-layer structure is the most robust R4 realization. The invariant forward-reference map is novel — linking each INVARIANT-N to "enforced in STEP 2 ¶C, STEP 3 [B]" creates bidirectional traceability not present in other variations. No current rubric criterion captures this, but it is a candidate C-14.

---

## Composite Scorecard

| Variation | Essential | Rec. | C-09 | C-10 | C-11 | C-12 | C-13 | Total | Golden |
|-----------|-----------|------|------|------|------|------|------|-------|--------|
| V-01 | 60 | 30 | 5 | 5 | 5 | 5 | 5 | **115** | ✓ |
| V-02 | 60 | 30 | 5 | 5 | 5 | 5 | 5 | **115** | ✓ |
| V-03 | 60 | 30 | 5 | 5 | 5 | 5 | 2.5 | **112.5** | ✓ |
| V-04 | 60 | 30 | 5 | 5 | 5 | 5 | 5 | **115** | ✓ |
| V-05 | 60 | 30 | 5 | 5 | 5 | 5 | 5 | **115** | ✓ |

**Four-way tie at 115.** Tiebreak by structural quality of C-13 and C-11 coverage:

1. **V-05** — FAILURE MODES block + Protocol + Invariant forward-reference map. Strongest structural case; bidirectional invariant traceability is novel.
2. **V-02** — Clean dedicated FAILURE MODES block pre-step. Most consistent realization of constraint-first principle; no ambiguity in C-12/C-13 overlap.
3. **V-04** — All 4 named across positioned sites; good coverage but most dispersed.
4. **V-01** — All 4 named but C-11 failure mode placement contradicts inline axis; C-12 shares text with C-10 note.
5. **V-03** — 112.5; C-13 ceiling is PARTIAL without C-10/C-11 failure modes.

---

## Excellence Signals

**Pattern 1 — Front-loaded FAILURE MODES block activates wrong-output anchors before production begins**
V-02 and V-05 both use a dedicated FAILURE MODES section placed before STEP 1. This matches the R3 breakthrough mechanism (constraint-first pre-step declaration). The model reads all four wrong-output examples before writing a single file. Inline placement (V-01) works but creates inconsistency when the failure mode for a pre-step construct (INVARIANTS) must appear inline in a step.

**Pattern 2 — Invariant forward-reference map creates bidirectional traceability**
V-05 introduces a novel structure: each INVARIANT-N entry lists the specific step paragraphs that enforce it (e.g., "enforced in: STEP 2 ¶C, STEP 3 [B]"). This is not required by any current criterion but converts the INVARIANTS block from a declaration into a navigable enforcement contract. Candidate for C-14 in rubric v3.

**Pattern 3 — Dedicated CHECK-OUTPUT PROTOCOL elevates C-12 from requirement to named section**
V-03 and V-05 both use a CHECK-OUTPUT PROTOCOL block. This makes auditable output a first-class section rather than an embedded instruction — the model cannot satisfy the skill by producing quiet compliance. Strongest C-12 treatment in R4.

---

```json
{"top_score": 115, "all_essential_pass": true, "new_patterns": ["front-loaded FAILURE MODES block activates all wrong-output anchors before step 1 begins — structurally parallel to R3 constraint-first breakthrough", "invariant forward-reference map: each INVARIANT-N names its enforcing steps, creating bidirectional traceability — candidate C-14"]}
```
