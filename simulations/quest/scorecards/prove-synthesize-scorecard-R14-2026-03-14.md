## prove-synthesize — Round 14 Scorecard (v14 rubric)

**Date**: 2026-03-15
**Rubric**: v14 (max 187.5 pts; C-46 and C-47 added)
**Test variable**: C-46 + C-47 stability across role sequence, output format, phrasing register, and lifecycle framing axes

---

## Criterion Evaluation

### Criteria carried from v13 base (C-35 through C-45)

All five variations are built on the R13 V-04 full battery. Each check below applies to all 5 unless noted.

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-35 Concurrent execution + seamless output | PASS | PASS | PASS | PASS | PASS |
| C-36 Dual-exemplar adversarial gate | PASS | PASS | PASS | PASS | PASS |
| C-37 Slot-indexed self-containment check | PASS | PASS | PASS | PASS | PASS |
| C-38 Role-to-output closure attribution | PASS | PASS | PASS | PASS | PASS |
| C-39 Phase-gated confidence ceiling | PASS | PASS | PASS | PASS | PASS |
| C-40 Concurrent synthesis gate block | PASS | PASS | PASS* | PASS | PASS |
| C-41 Slot-indexed revision mandate | PASS | PASS | PASS | PASS | PASS |
| C-42 Ceiling declaration mandatory intermediate output | PASS | PASS | PASS | PASS | PASS |
| C-43 Gate block per-role dual exemplars | PASS | PASS | PASS | PASS | PASS |
| C-44 Per-signal annotated inventory w/ role classification | PASS | PASS | PASS | PASS | PASS |
| C-45 Two-dimensional ceiling table (phase × inertia) | PASS | PASS | PASS | PASS | PASS |

*V-03 names the section "Failure Mode Verification" rather than "Gate Block." C-40 is a structural criterion, not a naming criterion — the section is unified, post-role-definitions, per-role indexed with dual exemplars. PASS.

---

### C-46 — Annotation-to-ceiling derivation linkage (NEW v14)

**Pass condition**: C-44 PASS + explicit "derived not inferred" statement positioned in the ceiling computation step.

| Variation | C-44 prereq | Derivation statement in ceiling step? | Result |
|-----------|-------------|---------------------------------------|--------|
| V-01 | PASS | Line 55: "The ceiling computation in this step is derived from the per-signal annotation inventory, not inferred from a gestalt impression." Positioned in Phase 2: Ceiling Computation between Phase 1 annotation and cognitive roles. | **PASS** |
| V-02 | PASS | Line 168: Same verbatim statement. Positioned in Phase 2: Ceiling Computation, before roles and gate block. | **PASS** |
| V-03 | PASS | Line 282: "The ceiling value computed here is derived from the per-signal annotation inventory, not inferred from a gestalt impression of evidence quality. The annotation inventory is the computational source of the ceiling." Descriptive register; derivation claim and computational source attribution both present in the ceiling section. | **PASS** |
| V-04 | PASS | Line 391: "The ceiling computation in this step is derived from the per-signal annotation inventory, not inferred from a gestalt impression. The annotation inventory is the computational source of the ceiling; the ceiling is not asserted from an overall assessment of evidence quality — it is read from the intersection of the highest lifecycle phase present and the inertia coverage state, both of which are determined by the annotation inventory." Extends the base statement with explicit intersection mechanics naming both annotation-determined inputs. | **PASS** |
| V-05 | PASS | Line 502: "The ceiling computation in this step is derived from the per-signal annotation inventory, not inferred from a gestalt impression." Positioned in Phase 2: Ceiling Computation. | **PASS** |

**C-46 result: PASS across all 5 variations.** R13 discriminator (absence of derivation statement in V-01) is resolved in all R14 variations by explicit inclusion of the statement in the ceiling computation step.

---

### C-47 — Extended declaration coverage in slot-indexed self-containment check (NEW v14)

**Pass condition**: C-37 PASS + C-42 extended with at least one annotation-derived value + Q in self-containment check explicitly covering extended values with a named output slot.

| Variation | C-42 declaration | Q6 scope | Named slot | Result |
|-----------|-----------------|----------|-----------|--------|
| V-01 | Extended with Primary counts by phase AND inertia state | "What was the evidence phase coverage, the Primary signal counts by phase, the inertia coverage state, and what ceiling applied?" | → **Verdict/Confidence paragraph** (explicit parenthetical: "phase coverage, Primary counts by phase, and inertia state from the mandatory declaration must be traceable to the confidence score") | **PASS** |
| V-02 | Extended with Primary counts by phase AND inertia state | Same three-value scope as V-01 | → **Confidence section** (parenthetical: "phase coverage, Primary counts by phase, and inertia state from the mandatory declaration must be traceable to the confidence score in the Confidence section"). "Confidence section" is an explicitly defined, named output section — not "Verdict/Confidence paragraph" but a valid named slot. C-47 is a traceability criterion, not a slot-naming criterion. | **PASS** |
| V-03 | Extended with Primary counts by phase AND inertia state | "What was the evidence phase coverage, the Primary signal counts by phase, the inertia coverage state, and what ceiling was applied?" | → **Verdict/Confidence paragraph** (parenthetical: "phase coverage, Primary counts by phase, and inertia state from the mandatory declaration must be traceable to the confidence score") | **PASS** |
| V-04 | Extended with Primary counts by phase AND inertia state | Same three-value scope | → **Verdict/Confidence paragraph** (parenthetical explicitly enumerates: "all three annotation-derived dimension values — phase coverage, Primary counts by phase, inertia state — from the Phase 2 declaration must be traceable to the confidence score") | **PASS** |
| V-05 | Extended with Primary counts by phase AND inertia state | Same three-value scope | → **Verdict/Confidence section** (parenthetical: "phase coverage, Primary counts by phase, and inertia state from the mandatory declaration must be traceable to the confidence score in the Verdict/Confidence section") | **PASS** |

**C-47 result: PASS across all 5 variations.** The open question from the variation design (V-02 slot-name specificity) resolves as PASS — "Confidence section" is a named output slot satisfying the traceability requirement.

---

## Composite Score Computation

Base anchor: R13 V-04 calibrated at v14 = ~130.0 (full C-35–C-45 battery + C-46 + C-47).

All 5 R14 variations carry the full battery and earn both new criteria.

| Variation | Base (C-35–C-45) | C-46 delta | C-47 delta | v14 Composite |
|-----------|-----------------|------------|------------|---------------|
| V-01 ADVERSARY-first | 125.0 | +2.5 | +2.5 | **130.0** |
| V-02 6-section split | 125.0 | +2.5 | +2.5 | **130.0** |
| V-03 Descriptive register | 125.0 | +2.5 | +2.5 | **130.0** |
| V-04 ANALYST-first + lifecycle narrative | 125.0 | +2.5 | +2.5 | **130.0** |
| V-05 Inertia-primary + Adoption Conditions | 125.0 | +2.5 | +2.5 | **130.0** |

**Essential status**: C-11 / C-13 / C-30 — all-essential PASS (all variations inherit R13 V-04 essential passing status; no axis change touches the essential criteria).
**Golden threshold**: 130.0 >= 90 AND all essential PASS → **GOLDEN** (all 5).

---

## Variation Rankings

| Rank | Variation | Score | Distinguishing feature |
|------|-----------|-------|------------------------|
| T-1 | V-01 ADVERSARY-first | 130.0 | Role-sequence inversion stable; C-46/C-47 unaffected |
| T-1 | V-02 6-section split | 130.0 | Slot-name flexibility confirmed for C-47; "Confidence section" is a valid named slot |
| T-1 | V-03 Descriptive register | 130.0 | Register independence confirmed; derivation linkage and Q6 extension survive narrative framing |
| T-1 | V-04 ANALYST-first + lifecycle | 130.0 | **Most expansive C-46 statement**: names both annotation dimensions as computational inputs; most explicit Q6 enumeration ("all three annotation-derived dimension values") |
| T-1 | V-05 Inertia-primary + Adoption Conditions | 130.0 | **Structural innovation**: dedicated Adoption Conditions section creating an explicit inertia-scope traceability slot beyond current rubric scope |

---

## Excellence Signals

**Signal 1 — Extended derivation mechanics in C-46 statement (V-04)**
V-04 goes beyond the minimum "derived not inferred" statement to name both annotation dimensions as computational inputs to the intersection: *"the ceiling is read from the intersection of the highest lifecycle phase present and the inertia coverage state, both of which are determined by the annotation inventory."* This upgrades C-46 from a provenance assertion to a reproducible computation path: a reader can independently follow the ceiling derivation by inspecting the annotation inventory for highest phase and inertia state, then reading the intersection cell. The minimum statement says *what* the ceiling is derived from; V-04's extended statement says *how* the derivation works.

**Signal 2 — Dedicated Adoption Conditions output section (V-05)**
V-05 adds a sixth section — **Adoption Conditions** — that explicitly separates adoption-scope analysis into three enumerated questions: (1) which segments/contexts inertia-present signals covered; (2) which they did not cover; (3) what specific inertia evidence type would fill each gap. This creates a dedicated traceability slot for inertia coverage scope that is currently subsumed within Counter-Evidence and Open Questions. The section converts inertia coverage scope from an implicit inference within the synthesis into an explicit structured output.

**Signal 3 — C-47 slot-name flexibility confirmed (V-02)**
V-02 confirms that C-47 is satisfied when the annotation-derived values map to a renamed slot ("Confidence section" in a 6-section format) rather than "Verdict/Confidence paragraph." The criterion requires named output slot with explicit traceability — not a specific slot name. This confirms C-47 is a structural traceability criterion, stable across output format reorganizations.

**Signal 4 — Full-battery stability confirmed across 4 axis dimensions (all 5)**
R14 serves as a stability confirmation round: C-46 and C-47 are confirmed stable across role sequence (ADVERSARY-first, ANALYST-first), output format (5-section, 6-section split, 6-section with Adoption Conditions), phrasing register (imperative, descriptive/narrative), and lifecycle framing (tabular phase labels, narrative lifecycle descriptions). No axis variation disrupted either new criterion when the machinery was explicitly included.

---

## v15 Candidate Criteria

**C-48 (candidate)** — Derivation mechanics enumeration in ceiling computation step (extends C-46)
V-04's extended derivation statement names both annotation-determined inputs to the intersection computation ("the highest lifecycle phase present and the inertia coverage state, both of which are determined by the annotation inventory"). This upgrades C-46 from derivation assertion to derivation path: the statement must name both dimensions as annotation-determined inputs, enabling independent re-derivation without trusting the synthesizer's assessment.

**C-49 (candidate)** — Inertia coverage scope section (extends C-45, C-42)
V-05's Adoption Conditions section creates an explicit output slot for inertia coverage scope: which segments/contexts the inertia-present signals covered, which they did not, and what specific evidence would fill each gap. This separates scope analysis from Counter-Evidence and Open Questions, creating end-to-end traceability: annotation inventory → ceiling → declaration → scope analysis section → named output slot.

---

```json
{"top_score": 130.0, "all_essential_pass": true, "new_patterns": ["V-04 extended derivation mechanics in ceiling computation step names both annotation-determined dimensions as inputs to the intersection computation, upgrading C-46 from provenance assertion to reproducible derivation path", "V-05 Adoption Conditions section creates a dedicated output slot for inertia coverage scope analysis — which segments inertia-present signals covered, which they did not, and what specific evidence fills each gap — separating scope analysis from Counter-Evidence and Open Questions"]}
```
