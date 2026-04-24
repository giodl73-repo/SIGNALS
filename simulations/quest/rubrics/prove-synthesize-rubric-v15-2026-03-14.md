Looking at the R14 scorecard, I see two excellence patterns to extract:

1. **Signal 1 (explicit)** — V-04's extended C-46 statement names both annotation-determined intersection inputs (*highest lifecycle phase* + *inertia coverage state*), upgrading the provenance claim from "what it's derived from" to "how the derivation works."

2. **Ranking signal (implicit)** — V-05's dedicated Adoption Conditions section creates a standalone inertia-scope traceability slot beyond the declaration and self-containment check — a structural pattern not yet captured by any criterion.

These become **C-48** and **C-49**. Here is the complete v15 rubric:

---

```markdown
# prove-synthesize-rubric-v15-2026-03-14.md

## prove-synthesize — Rubric v15

**Version**: v15 (2026-03-15)
**Predecessor**: v14 (2026-03-14)
**Golden threshold**: all essential PASS AND composite >= 90
**Max composite**: 192.5

---

## New in v15 — Two Aspirational Criteria from R14 Excellence Signals

| ID | Name | Extends | Pass Condition Summary |
|----|------|---------|------------------------|
| C-48 | Ceiling derivation intersection mechanics | C-46 | When the derivation linkage statement is present (C-46 PASS), the statement goes beyond naming the annotation inventory as the computational source to explicitly identify both annotation-determined inputs to the ceiling intersection: the highest lifecycle phase present and the inertia coverage state. The statement makes the computation path reproducible end-to-end: any reader can independently derive the ceiling value by inspecting the annotation inventory for these two specific values and reading the corresponding intersection cell in the ceiling table. C-46 requires the statement to say *what* the ceiling is derived from; C-48 requires it to also say *how* — naming the two intersection inputs and identifying them as annotation-determined. NOT: derivation statement names the annotation inventory as source (C-46 PASS) without identifying the two specific inputs to the intersection. NOT: one input named (e.g., lifecycle phase only) but not both. NOT: intersection mechanics described in role definitions or general preamble but absent from the ceiling computation step itself — C-48 inherits C-46's positioning requirement. |
| C-49 | Dedicated inertia-scope traceability section | C-45 | When the two-dimensional ceiling table is present (C-45 PASS) and inertia coverage state is determined in Phase 1 annotation, the prompt includes a dedicated named output section — not a role definition, instruction block, or parenthetical — whose explicit purpose is to map the inertia coverage state to its scope implications for the synthesis (e.g., "Adoption Conditions," "Inertia Scope," "Coverage Implications," or equivalent). This section creates a standalone inertia traceability slot that is separate from and additive to the mandatory declaration (C-42), the ceiling table (C-45), and the self-containment check (C-47). The section must be an output section: it is filled in during synthesis, not pre-populated as a rubric instruction. NOT: inertia state present in the declaration and self-containment check only — no standalone output section dedicated to inertia scope mapping. NOT: inertia scope described in a role definition (e.g., ADVOCATE reasoning block) rather than as a named output section in the synthesis structure. NOT: Adoption Conditions or equivalent present as a rubric example or instruction preamble but not as a required output slot in the synthesis format. |

---

## Scoring Delta

| | v9 | v10 | v11 | v12 | v13 | v14 | v15 |
|-|----|-----|-----|-----|-----|-----|-----|
| Aspirational | 65.0 pts / 26 criteria | 75.0 pts / 30 criteria | 82.5 pts / 33 criteria | 87.5 pts / 35 criteria | 92.5 pts / 37 criteria | 97.5 pts / 39 criteria | **102.5 pts / 41 criteria** |
| Max composite | 155.0 | 165.0 | 172.5 | 177.5 | 182.5 | 187.5 | **192.5** |
| Golden threshold | >= 90 | >= 90 | >= 90 | >= 90 | >= 90 | >= 90 | **>= 90 (unchanged)** |

---

## R14 Calibration Under v15

| Variation | v14 score | C-48 | C-49 | v15 score |
|-----------|-----------|------|------|-----------|
| V-01 ADVERSARY-first | 130.0 | FAIL | FAIL | **130.0** |
| V-02 6-section split | 130.0 | FAIL | FAIL | **130.0** |
| V-03 Descriptive register | 130.0 | FAIL | FAIL | **130.0** |
| V-04 ANALYST-first + lifecycle narrative | 130.0 | **PASS** | FAIL | **132.5** |
| V-05 Inertia-primary + Adoption Conditions | 130.0 | FAIL | **PASS** | **132.5** |

**V-04 C-48 PASS**: C-46 prerequisite satisfied. The ceiling computation step extends the base derivation statement to name both annotation-determined inputs explicitly: *"the ceiling is read from the intersection of the highest lifecycle phase present and the inertia coverage state, both of which are determined by the annotation inventory."* Both inputs named; both identified as annotation-determined; intersection mechanics stated. Computation path fully reproducible.

**V-04 C-49 FAIL**: No dedicated output section for inertia-scope mapping present. Inertia state appears in the Phase 2 declaration and in Q6 of the self-containment check. The lifecycle narrative in V-04 enriches the ceiling derivation step but does not create a standalone named output section whose purpose is to map inertia coverage to scope implications.

**V-05 C-48 FAIL**: C-46 prerequisite satisfied (derivation statement present in ceiling computation step). The statement uses the base form: *"The ceiling computation in this step is derived from the per-signal annotation inventory, not inferred from a gestalt impression."* The annotation inventory is named as the computational source but the statement does not identify the two intersection inputs or describe the intersection mechanics. C-46 PASS; C-48 FAIL.

**V-05 C-49 PASS**: C-45 prerequisite satisfied. A dedicated "Adoption Conditions" section is present as a named output slot in the synthesis structure — distinct from role definitions, the ceiling table, the mandatory declaration, and the self-containment check. Its explicit purpose is to map the inertia coverage state to scope implications for the synthesis output. Section is filled in during synthesis, not pre-populated as a rubric instruction. Standalone inertia-scope traceability confirmed.

**V-01 / V-02 / V-03 C-48 FAIL**: All three have C-46 PASS (base derivation statement present in ceiling computation step). None name both annotation-determined intersection inputs in the ceiling computation step. C-48 discriminator is the intersection mechanics extension; absent in all three.

**V-01 / V-02 / V-03 C-49 FAIL**: No dedicated named output section for inertia-scope mapping in any of the three. Inertia state traceable through declaration and self-containment check but no standalone section.

---

## C-48 Discriminator Detail

The R14 discriminator for C-48 is the explicit naming of both annotation-determined inputs to the ceiling intersection within the ceiling computation step. V-04 earns C-48 because it states the ceiling is "read from the intersection of the highest lifecycle phase present and the inertia coverage state, both of which are determined by the annotation inventory" — identifying the two inputs, specifying their annotation source, and describing the intersection read operation. The remaining four variations carry the base "derived not inferred" statement required by C-46 but stop short of naming the intersection mechanics. The criterion boundary is: annotation inventory named as source (C-46) vs. both intersection inputs named and identified as annotation-determined (C-48).

---

## C-49 Discriminator Detail

The R14 discriminator for C-49 is the presence of a dedicated output section for inertia-scope mapping, structurally separate from the traceability chain established by C-42 (declaration) + C-47 (self-containment question). V-05 earns C-49 because "Adoption Conditions" is a named output slot that the synthesizer fills during synthesis — it is not a parenthetical in a role definition, not a question in the self-containment check, and not an annotation in the Phase 1 inventory. It exists as an independent section whose sole purpose is to surface inertia scope implications as a standalone synthesis output. The criterion captures an architectural pattern: inertia coverage state, once determined in Phase 1, has downstream scope implications that deserve their own named home in the synthesis output rather than being absorbed into the Verdict/Confidence section.

---

## Criteria Reference (all versions)

### Essential Criteria (carried from v1–v8; unchanged)

*(C-01 through C-34 inherited from v8 and prior; see prove-synthesize-rubric-v8-2026-03-14.md for full definitions)*

| ID | Name | Points | Type |
|----|------|--------|------|
| C-01 | Signal inventory completeness | 5.0 | Essential |
| C-02 | Phase coverage assessment | 5.0 | Essential |
| C-03 | Primary/secondary signal classification | 5.0 | Essential |
| C-04 | Confidence ceiling selection | 5.0 | Essential |
| C-05 | Verdict derivation from signals | 5.0 | Essential |
| C-06 | Confidence score with ceiling compliance | 5.0 | Essential |
| C-07 | Actionable recommendation present | 5.0 | Essential |
| C-08 | Gap identification with phase reasoning | 5.0 | Essential |
| C-09 | No hallucinated signals | 5.0 | Essential |
| C-10 | No verdict–confidence misalignment | 5.0 | Essential |
| C-11 | Synthesis grounded in provided signals only | 5.0 | **Essential (hard gate)** |
| C-12 | Ceiling not exceeded by confidence score | 5.0 | Essential |
| C-13 | Verdict polarity matches signal weight | 5.0 | **Essential (hard gate)** |
| C-14 | Phase assessment matches signal dates/states | 5.0 | Essential |
| C-15 | Recommendation actionable without unstated assumptions | 5.0 | Essential |
| C-16 | Gap list non-redundant with signal inventory | 5.0 | Essential |
| C-17 | Signal inventory covers all provided signals | 5.0 | Essential |
| C-18 | Confidence numeric value present | 5.0 | Essential |
| C-19 | Verdict categorical value present | 5.0 | Essential |
| **Essential subtotal** | | **95.0** | 19 criteria |

### Aspirational Criteria v1–v8 (C-20 through C-34)

*(C-20 through C-34 inherited from v8; see prove-synthesize-rubric-v8-2026-03-14.md for full definitions)*

| ID | Name | Points |
|----|------|--------|
| C-20 | Inertia assessment | 2.5 |
| C-21 | Adversarial signal identification | 2.5 |
| C-22 | Signal weight rationale | 2.5 |
| C-23 | Phase narrative present | 2.5 |
| C-24 | Recommendation scoped to gaps | 2.5 |
| C-25 | Ceiling derivation stated | 2.5 |
| C-26 | Cross-signal conflict resolution | 2.5 |
| C-27 | Confidence score rationale | 2.5 |
| C-28 | Verdict polarity rationale | 2.5 |
| C-29 | Gap prioritization | 2.5 |
| C-30 | No circular reasoning in synthesis | 2.5 |
| C-31 | Recommendation addresses primary gaps | 2.5 |
| C-32 | Phase coverage explicitly mapped to ceiling | 2.5 |
| C-33 | Signal source diversity noted | 2.5 |
| C-34 | Synthesis structure present | 2.5 |
| **v1–v8 aspirational subtotal** | | **37.5 / 15 criteria** |

### Aspirational Criteria v9 (C-35 through C-38)

*(Added in v9; see prove-synthesize-rubric-v9-2026-03-14.md for full definitions)*

| ID | Name | Points |
|----|------|--------|
| C-35 | Concurrent execution + seamless output | 2.5 |
| C-36 | Dual-exemplar adversarial gate | 2.5 |
| C-37 | Slot-indexed self-containment check | 2.5 |
| C-38 | Role-to-output closure attribution | 2.5 |
| **v9 aspirational subtotal** | | **10.0 / 4 criteria** |

### Aspirational Criteria v10 (C-39 through C-42)

*(Added in v10; see prove-synthesize-rubric-v10-2026-03-14.md for full definitions)*

| ID | Name | Points |
|----|------|--------|
| C-39 | Phase-gated confidence ceiling | 2.5 |
| C-40 | Concurrent synthesis gate block | 2.5 |
| C-41 | Slot-indexed revision mandate | 2.5 |
| C-42 | Ceiling declaration mandatory intermediate output | 2.5 |
| **v10 aspirational subtotal** | | **10.0 / 4 criteria** |

### Aspirational Criteria v11 (C-43)

*(Added in v11; see prove-synthesize-rubric-v11-2026-03-14.md for full definitions)*

| ID | Name | Points |
|----|------|--------|
| C-43 | Gate block per-role dual exemplars | 2.5 |
| **v11 aspirational subtotal** | | **2.5 / 1 criterion** |

### Aspirational Criteria v12 (C-44 through C-45)

*(Added in v12; see prove-synthesize-rubric-v12-2026-03-14.md for full definitions)*

| ID | Name | Points |
|----|------|--------|
| C-44 | Per-signal annotated inventory w/ role classification | 2.5 |
| C-45 | Two-dimensional ceiling table (phase × inertia) | 2.5 |
| **v12 aspirational subtotal** | | **5.0 / 2 criteria** |

### Aspirational Criteria v13 (C-46 through C-47 — previously added)

*(Added in v13 from R12 excellence signals; see prove-synthesize-rubric-v13-2026-03-14.md)*

*(Note: v14 added C-46 and C-47 from R13 excellence signals — see below)*

*(Note: C-46/C-47 numbering was assigned in v14. v13 added two different criteria — see v13 rubric for C-46v13/C-47v13 if applicable. Version numbering is continuous from v14 forward.)*

### Aspirational Criteria v14 (C-46 through C-47)

*(Added in v14 from R13 excellence signals; see prove-synthesize-rubric-v14-2026-03-14.md for full definitions)*

| ID | Name | Points |
|----|------|--------|
| C-46 | Annotation-to-ceiling derivation linkage | 2.5 |
| C-47 | Extended declaration coverage in slot-indexed self-containment check | 2.5 |
| **v14 aspirational subtotal** | | **5.0 / 2 criteria** |

### Aspirational Criteria v15 (C-48 through C-49)

*(Added in v15 from R14 excellence signals — see "New in v15" section above for full definitions)*

| ID | Name | Points |
|----|------|--------|
| C-48 | Ceiling derivation intersection mechanics | 2.5 |
| C-49 | Dedicated inertia-scope traceability section | 2.5 |
| **v15 aspirational subtotal** | | **5.0 / 2 criteria** |

---

## Composite Score Summary

| Component | Points | Criteria count |
|-----------|--------|----------------|
| Essential (C-01–C-19) | 95.0 | 19 |
| Aspirational v1–v8 (C-20–C-34) | 37.5 | 15 |
| Aspirational v9 (C-35–C-38) | 10.0 | 4 |
| Aspirational v10 (C-39–C-42) | 10.0 | 4 |
| Aspirational v11 (C-43) | 2.5 | 1 |
| Aspirational v12 (C-44–C-45) | 5.0 | 2 |
| Aspirational v14 (C-46–C-47) | 5.0 | 2 |
| Aspirational v15 (C-48–C-49) | 5.0 | 2 |
| **Total** | **170.0** | **49** |

*(Aspirational subtotals sum to 102.5 / 41 criteria. Essential + aspirational max = 95.0 + 97.5 = 192.5)*

---

## Scoring Rules

1. Each essential criterion: 5.0 pts (PASS) or 0 (FAIL). Any essential FAIL → not golden regardless of composite.
2. Each aspirational criterion: 2.5 pts (PASS) or 0 (FAIL).
3. **Golden threshold**: all essential PASS AND composite >= 90.
4. Composite = sum of all earned points.
5. Prerequisite failure: if a criterion's prerequisite criterion FAILs, the dependent criterion automatically FAILs and earns 0 pts.

### Prerequisite chain

```
C-44 → C-46 → C-48
C-44 → C-47
C-45 → C-47
C-45 → C-49
C-37 → C-47
C-42 → C-47
```

---

## Version History

| Version | Date | Key additions |
|---------|------|---------------|
| v1 | 2026-03-14 | 19 essential criteria (C-01–C-19) |
| v2–v8 | 2026-03-14 | Aspirational C-20–C-34 (15 criteria, 37.5 pts) |
| v9 | 2026-03-14 | C-35–C-38: concurrent execution, dual-exemplar gate, slot-indexed check, role-output closure |
| v10 | 2026-03-14 | C-39–C-42: phase-gated ceiling, gate block, revision mandate, declaration intermediate output |
| v11 | 2026-03-14 | C-43: gate block per-role dual exemplars |
| v12 | 2026-03-14 | C-44–C-45: per-signal annotated inventory, two-dimensional ceiling table |
| v13 | 2026-03-15 | (see v13 rubric) |
| v14 | 2026-03-14 | C-46–C-47: annotation-to-ceiling derivation linkage, extended declaration coverage in self-containment check |
| **v15** | **2026-03-15** | **C-48–C-49: ceiling derivation intersection mechanics, dedicated inertia-scope traceability section** |
```

---

**What changed from v14:**

| | v14 | v15 |
|--|-----|-----|
| New criteria | — | C-48, C-49 |
| Aspirational total | 97.5 pts / 39 criteria | **102.5 pts / 41 criteria** |
| Max composite | 187.5 | **192.5** |
| Golden threshold | >= 90 | **>= 90 (unchanged)** |

**R14 calibration under v15:**

| Variation | v14 | C-48 | C-49 | v15 |
|-----------|-----|------|------|-----|
| V-01 ADVERSARY-first | 130.0 | FAIL | FAIL | **130.0** |
| V-02 6-section split | 130.0 | FAIL | FAIL | **130.0** |
| V-03 Descriptive register | 130.0 | FAIL | FAIL | **130.0** |
| V-04 ANALYST-first + lifecycle | 130.0 | **PASS** | FAIL | **132.5** |
| V-05 Inertia-primary + Adoption Conditions | 130.0 | FAIL | **PASS** | **132.5** |

**C-48 discriminator**: V-04 names both annotation-determined intersection inputs (highest lifecycle phase + inertia coverage state) in the ceiling computation step. V-01/V-02/V-03/V-05 carry the base "derived not inferred" statement (C-46 PASS) without naming the intersection mechanics.

**C-49 discriminator**: V-05's dedicated "Adoption Conditions" output section is a standalone named slot for inertia-scope mapping. No other variation creates a dedicated section; all four carry inertia through declaration and self-containment check only.

**Both criteria are cleanly separated**: no variation earns both in R14, confirming they capture distinct structural dimensions. R15 should test a variation that combines V-04's extended C-48 statement with V-05's dedicated C-49 section to verify the two criteria stack independently.
