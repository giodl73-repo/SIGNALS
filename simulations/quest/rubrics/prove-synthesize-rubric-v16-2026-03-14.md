Reading the R15 scorecard for excellence signals before writing v16.

Two patterns to extract:

1. **V-02's C-48 form** — the ceiling computation step goes beyond naming both intersection inputs (C-48) to add an explicit end-to-end reproducibility claim: *"Any reader who inspects the annotation inventory for these two values and reads the corresponding cell in the table below can independently derive the ceiling."* This is noted as "the most explicit form" and "exceeds the minimum C-48 bar" — a structural upgrade from mechanics-stated to reproducibility-guaranteed.

2. **Universal Q4 → section-name binding (all five variations)** — every variation's self-containment check Q4 explicitly names the dedicated inertia-scope section by its output section name (V-01: "Inertia Scope section", V-02: "Coverage Implications section", V-03: "Inertia Scope section", V-04: "Adoption Scope section", V-05: "Adoption Conditions section"). C-49 requires the section to exist as a named output slot; this pattern requires Q4 to reference it by name — bidirectional traceability. Absent in R14 (C-49 first appeared in V-05 R14, but Q4 naming was not a stated requirement).

These become **C-50** and **C-51**.

---

```markdown
# prove-synthesize-rubric-v16-2026-03-14.md

## prove-synthesize — Rubric v16

**Version**: v16 (2026-03-15)
**Predecessor**: v15 (2026-03-15)
**Golden threshold**: all essential PASS AND composite >= 90
**Max composite**: 197.5

---

## New in v16 — Two Aspirational Criteria from R15 Excellence Signals

| ID | Name | Extends | Pass Condition Summary |
|----|------|---------|------------------------|
| C-50 | Ceiling derivation end-to-end reproducibility claim | C-48 | When C-48 is PASS (both annotation-determined intersection inputs named in the ceiling computation step), the ceiling computation step goes further to include an explicit end-to-end reproducibility claim: a stated assertion that any reader who inspects the annotation inventory for the two named values and reads the corresponding intersection cell in the ceiling table can independently derive the ceiling. The claim must be stated as a direct consequence of the intersection mechanics — not merely implied by the presence of the derivation statement, not absorbed into the general "derived not inferred" language of C-46, and not present only in role definitions or preamble. C-48 requires the intersection inputs to be named; C-50 requires the reproducibility consequence to be stated. NOT: derivation statement names both inputs and identifies them as annotation-determined (C-48 PASS) without a stated reproducibility claim. NOT: reproducibility implied by the "any reader" form only present in exemplars rather than in the ceiling computation step itself. NOT: reproducibility language present in role definitions (e.g., ADVOCATE or ADVERSARY description blocks) but absent from the ceiling computation step — C-50 inherits C-48's positioning requirement. |
| C-51 | Self-containment Q4 explicit section-name binding | C-47 + C-49 | When the dedicated inertia-scope traceability section is present (C-49 PASS) and the slot-indexed self-containment check is present (C-47 PASS), Q4 of the self-containment check explicitly names the dedicated inertia-scope section by its output section name — the exact name as it appears in the synthesis output structure (e.g., "Inertia Scope section," "Coverage Implications section," "Adoption Conditions section," "Adoption Scope section," or equivalent). This creates bidirectional traceability: C-49 establishes that the section exists as a named output slot; C-51 establishes that Q4 references it by that name, closing the loop between the self-containment check and the dedicated section. The Q4 reference must name the section, not merely ask about inertia scope in the abstract. NOT: Q4 asks whether the inertia coverage state has been addressed in the synthesis without naming the dedicated section. NOT: dedicated section present (C-49 PASS) and Q4 present (C-47 PASS) but Q4 does not use the section name. NOT: section name appears in Q4 as a parenthetical example or rubric instruction rather than as the binding slot reference. |

---

## Scoring Delta

| | v9 | v10 | v11 | v12 | v13 | v14 | v15 | v16 |
|-|----|-----|-----|-----|-----|-----|-----|-----|
| Aspirational | 65.0 pts / 26 criteria | 75.0 pts / 30 criteria | 82.5 pts / 33 criteria | 87.5 pts / 35 criteria | 92.5 pts / 37 criteria | 97.5 pts / 39 criteria | 102.5 pts / 41 criteria | **107.5 pts / 43 criteria** |
| Max composite | 155.0 | 165.0 | 172.5 | 177.5 | 182.5 | 187.5 | 192.5 | **197.5** |
| Golden threshold | >= 90 | >= 90 | >= 90 | >= 90 | >= 90 | >= 90 | >= 90 | **>= 90 (unchanged)** |

---

## R15 Calibration Under v16

| Variation | v15 score (R15) | C-50 | C-51 | v16 score |
|-----------|----------------|------|------|-----------|
| V-01 ADVERSARY-first + Inertia Scope | 135.0 | FAIL | **PASS** | **137.5** |
| V-02 7-section split + Coverage Implications | 135.0 | **PASS** | **PASS** | **140.0** |
| V-03 Descriptive register + Inertia Scope | 135.0 | FAIL | **PASS** | **137.5** |
| V-04 ANALYST-first + Adoption Scope | 135.0 | FAIL | **PASS** | **137.5** |
| V-05 Inertia-primary + Adoption Conditions | 135.0 | FAIL | **PASS** | **137.5** |

**V-02 C-50 PASS**: C-48 prerequisite satisfied. The ceiling computation step carries the strongest intersection-mechanics statement across all five variations: *"The ceiling is read from the intersection of the highest evidence phase present and the inertia coverage state — both of which are determined by the annotation inventory."* This satisfies C-48. V-02 then adds an explicit end-to-end reproducibility claim: *"Any reader who inspects the annotation inventory for these two values and reads the corresponding cell in the table below can independently derive the ceiling."* Both inputs named, annotation-determination stated, and reproducibility consequence explicitly asserted. C-50 PASS.

**V-01 / V-03 / V-04 / V-05 C-50 FAIL**: All four have C-48 PASS (both annotation-determined intersection inputs named in the ceiling computation step). None carry an explicit reproducibility claim in the ceiling computation step. V-01: *"both determined by the annotation inventory"* — inputs named, annotation-determination stated, no reproducibility claim. V-03: SYNTHESIST and ADVERSARY exemplars state intersection mechanics with concrete values but no "any reader can independently derive" assertion. V-04: *"both derived directly from the annotation inventory"* — C-48 form, no reproducibility extension. V-05: *"both determined by the annotation inventory"* — C-48 form, no reproducibility extension. The C-50 discriminator is the stated reproducibility consequence; absent in all four.

**All five variations C-51 PASS**: C-49 PASS in all five (confirmed in R15 scorecard). C-47 PASS in all five (slot-indexed self-containment check with 6 questions). Q4 in each variation explicitly names the dedicated inertia-scope section by its output section name: V-01 Q4 → "Inertia Scope section"; V-02 Q4 → "Coverage Implications section"; V-03 Q4 → "Inertia Scope section"; V-04 Q4 → "Adoption Scope section"; V-05 Q4 → "Adoption Conditions section." All five create bidirectional traceability between Q4 and the dedicated section. C-51 is a universal PASS in R15 — the pattern was adopted uniformly when all five variations implemented C-49.

**C-51 retrospective on R14**: V-05 in R14 earned C-49 PASS (Adoption Conditions section present). The R14 scorecard does not record Q4 explicitly naming "Adoption Conditions section." C-51 cannot be confirmed PASS for R14 V-05 from available evidence. C-51 is therefore treated as first earned universally in R15 rather than retroactively in R14.

---

## C-50 Discriminator Detail

The R15 discriminator for C-50 is the presence of an explicit end-to-end reproducibility claim in the ceiling computation step — a stated assertion that any reader can independently verify the ceiling by performing the two-input annotation lookup and reading the intersection cell. V-02 earns C-50 because it extends the C-48 intersection-mechanics statement with a direct-address reproducibility guarantee: the claim is stated as an explicit consequence of the intersection mechanics, not implied. The remaining four variations satisfy C-48 (both inputs named, annotation-determined) but stop at the mechanics statement without asserting the reproducibility consequence. The criterion boundary is: intersection inputs named and identified as annotation-determined (C-48) vs. reproducibility of the derivation explicitly asserted as a consequence of those named inputs (C-50). C-50 does not require a specific phrasing form — the assertion that the derivation is independently reproducible from the annotation inventory is the discriminating element.

---

## C-51 Discriminator Detail

The R15 discriminator for C-51 is the explicit section-name reference in Q4 of the self-containment check — Q4 does not merely ask whether inertia scope has been addressed but names the exact output section where that address is expected to appear. All five R15 variations satisfy this: the Q4 question text binds to the dedicated section by name, creating a closed loop between the check and the output slot. This is structurally distinct from C-47 (which requires slot-indexed self-containment questions with slot-name references generally) and from C-49 (which requires the dedicated section to exist). C-51 captures the specific Q4 → section-name binding that ties these two structural elements together. The criterion reflects an architectural maturation: once a dedicated inertia-scope section exists (C-49), the self-containment check's Q4 should reference it by name rather than ask about inertia scope generically, ensuring that the check and the section remain synchronized if the section is renamed or relocated.

---

## Criteria Reference (all versions)

### Essential Criteria (carried from v1–v8; unchanged)

| ID | Name | Points | Type |
|----|------|--------|------|
| C-01 | Role-annotated signal table | 5.0 | Essential |
| C-02 | Per-signal verdict assignment | 5.0 | Essential |
| C-03 | Evidence summary per signal | 5.0 | Essential |
| C-04 | Synthesis verdict present | 5.0 | Essential |
| C-05 | Confidence level stated | 5.0 | Essential |
| C-06 | Risk or gap identification | 5.0 | Essential |
| C-07 | Recommendation present | 5.0 | Essential |
| C-08 | Structured output format | 5.0 | Essential |
| C-09 | Signal count stated | 5.0 | Essential |
| C-10 | Conflicting signal acknowledgment | 5.0 | Essential |
| C-11 | Lifecycle phase coverage stated | 5.0 | Essential |
| C-12 | Inertia state addressed | 5.0 | Essential |
| C-13 | Scope boundary stated | 5.0 | Essential |
| C-14 | No hallucinated signals | 5.0 | Essential |
| C-15 | No fabricated evidence | 5.0 | Essential |
| C-16 | Role separation maintained | 5.0 | Essential |
| C-17 | Output slots complete | 5.0 | Essential |
| C-18 | Annotation inventory present | 5.0 | Essential |
| C-19 | Phase-gated ceiling applied | 5.0 | Essential |

**Essential subtotal**: 95.0 pts / 19 criteria

---

### Aspirational Criteria (v1–v8 additions, C-20–C-34)

| ID | Name | Points | Type |
|----|------|--------|------|
| C-20 | Multi-role annotation present | 2.5 | Aspirational |
| C-21 | Per-signal role attribution | 2.5 | Aspirational |
| C-22 | Adversarial challenge present | 2.5 | Aspirational |
| C-23 | Synthesist integration present | 2.5 | Aspirational |
| C-24 | Advocate qualification present | 2.5 | Aspirational |
| C-25 | Ceiling value stated numerically | 2.5 | Aspirational |
| C-26 | Ceiling rationale stated | 2.5 | Aspirational |
| C-27 | Inertia coverage scope mapped | 2.5 | Aspirational |
| C-28 | Lifecycle phase distribution shown | 2.5 | Aspirational |
| C-29 | Conflicting roles reconciled | 2.5 | Aspirational |
| C-30 | Gap prioritization present | 2.5 | Aspirational |
| C-31 | Revision path stated | 2.5 | Aspirational |
| C-32 | Self-containment check present | 2.5 | Aspirational |
| C-33 | Output closure stated | 2.5 | Aspirational |
| C-34 | Role-to-output traceability present | 2.5 | Aspirational |

**v1–v8 aspirational subtotal**: 37.5 pts / 15 criteria

---

### Aspirational Criteria (v9–v16 additions, C-35–C-51)

| ID | Name | Points | Version Added | Extends |
|----|------|--------|---------------|---------|
| C-35 | Concurrent execution + seamless output | 2.5 | v9 | — |
| C-36 | Dual-exemplar adversarial gate | 2.5 | v9 | — |
| C-37 | Slot-indexed self-containment check | 2.5 | v9 | C-32 |
| C-38 | Role-to-output closure attribution | 2.5 | v9 | C-34 |
| C-39 | Phase-gated confidence ceiling | 2.5 | v10 | C-25/C-26 |
| C-40 | Concurrent synthesis gate block | 2.5 | v10 | C-35 |
| C-41 | Slot-indexed revision mandate | 2.5 | v10 | C-31/C-37 |
| C-42 | Ceiling declaration mandatory intermediate output | 2.5 | v11 | C-39 |
| C-43 | Gate block per-role dual exemplars | 2.5 | v11 | C-36/C-40 |
| C-44 | Per-signal annotated inventory | 2.5 | v12 | C-18/C-20 |
| C-45 | Two-dimensional ceiling table | 2.5 | v12 | C-39/C-44 |
| C-46 | Annotation-to-ceiling derivation linkage | 2.5 | v13 | C-44/C-45 |
| C-47 | Extended declaration coverage in self-containment check | 2.5 | v13 | C-37/C-42 |
| C-48 | Ceiling derivation intersection mechanics | 2.5 | v15 | C-46 |
| C-49 | Dedicated inertia-scope traceability section | 2.5 | v15 | C-45 |
| C-50 | Ceiling derivation end-to-end reproducibility claim | 2.5 | **v16** | C-48 |
| C-51 | Self-containment Q4 explicit section-name binding | 2.5 | **v16** | C-47 + C-49 |

**v9–v16 aspirational subtotal**: 42.5 pts / 17 criteria

---

### Full Scoring Summary

| Band | Criteria | Points |
|------|----------|--------|
| Essential (C-01–C-19) | 19 | 95.0 |
| Aspirational v1–v8 (C-20–C-34) | 15 | 37.5 |
| Aspirational v9–v16 (C-35–C-51) | 17 | 42.5 |
| **Total** | **51** | **197.5** |

**Golden threshold**: all 19 essential PASS AND composite >= 90

---

## Full Version History

| Version | Date | Δ Criteria | Max Composite | Key Addition |
|---------|------|------------|---------------|--------------|
| v1 | 2026-03-14 | baseline | — | Initial rubric |
| v9 | 2026-03-14 | +4 | 155.0 | Concurrent execution, dual-exemplar gate, slot-indexed check, closure attribution |
| v10 | 2026-03-14 | +4 | 165.0 | Phase-gated ceiling, concurrent gate block, slot-indexed revision mandate |
| v11 | 2026-03-14 | +3 | 172.5 | Ceiling declaration, per-role dual exemplars |
| v12 | 2026-03-14 | +2 | 177.5 | Per-signal annotated inventory, two-dimensional ceiling table |
| v13 | 2026-03-14 | +2 | 182.5 | Annotation-to-ceiling derivation linkage, extended declaration coverage in self-containment |
| v14 | 2026-03-14 | +2 | 187.5 | (see v14 release notes) |
| v15 | 2026-03-15 | +2 | 192.5 | Ceiling derivation intersection mechanics (C-48), dedicated inertia-scope traceability section (C-49) |
| **v16** | **2026-03-15** | **+2** | **197.5** | **Ceiling derivation end-to-end reproducibility claim (C-50), self-containment Q4 explicit section-name binding (C-51)** |
```
