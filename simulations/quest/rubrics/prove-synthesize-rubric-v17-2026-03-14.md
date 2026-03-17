`prove-synthesize-rubric-v17-2026-03-14.md` written. Summary of what changed:

---

## v17 — Two new aspirational criteria from R16 excellence signals

**C-52 — Ceiling Declaration promoted to first named output section with inter-section citation** (extends C-42)

V-02 R16 is the source. The mandatory inline declaration (C-42) is upgraded to a dedicated named section — the first output slot, before Verdict and Confidence. Three conditions required simultaneously:
1. "Ceiling Declaration" (or equivalent) is the first named output section, containing the annotation-derived dimension values and ceiling
2. Q7 of the self-containment check maps to "Ceiling Declaration section" rather than to a synthesis reasoning section
3. The Confidence section explicitly cites "Ceiling Declaration section" by name as its ceiling authority

This closes the annotation-to-synthesis traceability chain: annotation inventory → named intersection inputs (C-48) → reproducible derivation (C-50) → dedicated output slot cited by the reasoning section.

**C-53 — Explicit dimensional independence statement in ceiling computation step** (extends C-48 + C-50)

V-04 R16 is the source. After the C-50 reproducibility claim and before the ceiling table, a stated constraint principle is added: inertia and evidence phase each independently constrain the ceiling; at a fixed phase level, an inertia-absent evidence base cannot exceed the inertia-absent ceiling column regardless of evidence volume. This forecloses the compensation-inference class that C-48 and C-50 leave open.

**Scoring impact:**

| Variation | R16 v16 | C-52 | C-53 | v17 |
|-----------|---------|------|------|-----|
| V-01 | 140.0 | FAIL | FAIL | 140.0 |
| V-02 | 140.0 | PASS | FAIL | **142.5** |
| V-03 | 140.0 | FAIL | FAIL | 140.0 |
| V-04 | 140.0 | FAIL | PASS | **142.5** |
| V-05 | 140.0 | FAIL | FAIL | 140.0 |

Max composite: **202.5** (53 criteria). Golden threshold unchanged at >= 90.
.

---

```markdown
# prove-synthesize-rubric-v17-2026-03-14.md

## prove-synthesize — Rubric v17

**Version**: v17 (2026-03-15)
**Predecessor**: v16 (2026-03-15)
**Golden threshold**: all essential PASS AND composite >= 90
**Max composite**: 202.5

---

## New in v17 — Two Aspirational Criteria from R16 Excellence Signals

| ID | Name | Extends | Pass Condition Summary |
|----|------|---------|------------------------|
| C-52 | Ceiling Declaration promoted to first named output section with inter-section citation | C-42 | The mandatory ceiling declaration (C-42) is promoted from an inline pre-synthesis statement to the first named output section in the synthesis output structure, placed before the Verdict section, the Confidence section, and all other synthesis reasoning sections. Three conditions must hold simultaneously: (1) a dedicated section named "Ceiling Declaration" (or equivalent) exists as the first named output slot and contains the annotation-derived dimension values (highest evidence phase and inertia coverage state) and the ceiling value; (2) Q7 of the self-containment check explicitly maps to this "Ceiling Declaration section" (or equivalent) rather than to a synthesis reasoning section such as "Confidence section"; (3) the Confidence section (or scoring section) contains an explicit inter-section citation to the Ceiling Declaration section — a stated constraint of the form "the score must not exceed the ceiling stated in the Ceiling Declaration section" or equivalent, binding the synthesis reasoning section to the annotation-derived values slot. All three conditions are required; satisfying one or two does not earn C-52. NOT: ceiling declaration present as an inline mandatory statement before synthesis reasoning (C-42 PASS form) but not as a named output section. NOT: named Ceiling Declaration section present but not placed before synthesis reasoning sections. NOT: Ceiling Declaration section present and Q7 mapping present, but Confidence section does not cite the Ceiling Declaration section by name. NOT: Confidence section references the ceiling value inline without citing a named output slot. C-52 inherits C-42's requirement that the annotation-derived values appear before synthesis reasoning begins; it adds the requirement that this positioning is formalized as a named first output slot with a closing citation from the Confidence section. |
| C-53 | Explicit dimensional independence statement in ceiling computation step | C-48 + C-50 | When C-48 is PASS (both annotation-determined intersection inputs named) and C-50 is PASS (reproducibility consequence explicitly stated), the ceiling computation step goes further to include an explicit dimensional independence statement — a stated principle that the inertia coverage dimension and the evidence phase dimension each independently constrain the ceiling, and that at a fixed evidence phase level an inertia-absent evidence base cannot exceed the inertia-absent ceiling column regardless of evidence volume. The statement must: (a) appear in the ceiling computation step (Phase 2, Confidence Ceiling section, or equivalent) after the C-50 reproducibility claim and before or alongside the ceiling table; (b) state independence as a principle, not merely note that both dimensions are present; (c) state the fixed-phase constraint explicitly — that evidence volume cannot compensate for an inertia gap at any fixed phase level. This forecloses a ceiling-violation inference class that C-48 and C-50 alone do not explicitly address: a reader who understands that both inputs are annotation-determined and that the derivation is reproducible might still infer that a sufficiently large or high-quality inertia-absent evidence base could outrun the inertia-absent ceiling column. C-53 explicitly forecloses that inference. NOT: independence implied by the ceiling table structure (rows x columns present) without a stated principle. NOT: general statement that "both dimensions matter" or "both are required" without stating they are independent constraints. NOT: statement that inertia affects the ceiling without stating the independence principle (that phase cannot compensate for inertia absence and vice versa). NOT: independence principle present in role definitions, preamble, or annotation instructions but absent from the ceiling computation step — C-53 inherits C-48's and C-50's positioning requirement. NOT: C-50 reproducibility claim present without the independence principle — C-53 requires both. |

---

## Scoring Delta

| | v9 | v10 | v11 | v12 | v13 | v14 | v15 | v16 | v17 |
|-|----|-----|-----|-----|-----|-----|-----|-----|-----|
| Aspirational | 65.0 pts / 26 criteria | 75.0 pts / 30 criteria | 82.5 pts / 33 criteria | 87.5 pts / 35 criteria | 92.5 pts / 37 criteria | 97.5 pts / 39 criteria | 102.5 pts / 41 criteria | 107.5 pts / 43 criteria | **112.5 pts / 45 criteria** |
| Max composite | 155.0 | 165.0 | 172.5 | 177.5 | 182.5 | 187.5 | 192.5 | 197.5 | **202.5** |
| Golden threshold | >= 90 | >= 90 | >= 90 | >= 90 | >= 90 | >= 90 | >= 90 | >= 90 | **>= 90 (unchanged)** |

---

## R16 Calibration Under v17

| Variation | v16 score (R16) | C-52 | C-53 | v17 score |
|-----------|----------------|------|------|-----------|
| V-01 ADVERSARY-ANALYST-SYNTHESIST + Adoption Boundaries | 140.0 | FAIL | FAIL | **140.0** |
| V-02 8-section + Ceiling Declaration + Coverage Horizon | 140.0 | **PASS** | FAIL | **142.5** |
| V-03 Lifecycle emphasis + Evidence Scope | 140.0 | FAIL | FAIL | **140.0** |
| V-04 ADVERSARY-first + inertia-primary + Inertia Reach | 140.0 | FAIL | **PASS** | **142.5** |
| V-05 Descriptive register + lifecycle + Scope Implications | 140.0 | FAIL | FAIL | **140.0** |

**V-02 C-52 PASS**: C-42 prerequisite satisfied. V-02 promotes the mandatory ceiling declaration to the first named output section ("**Ceiling Declaration**"), placed before Verdict, Confidence, and all reasoning sections. Three conditions confirmed: (1) "Ceiling Declaration" is the first named output slot, containing annotation-derived dimension values and ceiling value; (2) Q7 of the self-containment check maps to "Ceiling Declaration section" rather than "Confidence section"; (3) the Confidence section cites the Ceiling Declaration section: "The score must not exceed the ceiling stated in the Ceiling Declaration section." All three C-52 conditions satisfied. C-52 PASS.

**V-01 / V-03 / V-04 / V-05 C-52 FAIL**: All four carry the C-42 inline mandatory statement form (mandatory pre-synthesis declaration, positioned before synthesis reasoning begins). None promote the declaration to a dedicated first named output section. None carry an inter-section citation from the Confidence section to a named ceiling section. C-52 requires the named-section promotion plus inter-section citation; absent in all four.

**V-04 C-53 PASS**: C-48 and C-50 prerequisites satisfied. V-04 Phase 2 inserts a dimensional independence statement after the C-50 reproducibility claim and before the ceiling table: *"The inertia dimension and the evidence phase dimension each independently constrain confidence. At a fixed phase level, an inertia-absent evidence base cannot exceed the inertia-absent ceiling even if the evidence base is large."* Independence stated as a principle; fixed-phase constraint explicitly stated; inference foreclosure complete. C-53 PASS.

**V-01 / V-02 / V-03 / V-05 C-53 FAIL**: All four have C-48 PASS and C-50 PASS. None insert a dimensional independence statement as a stated principle in the ceiling computation step. V-01/V-02/V-03/V-05 state that both inputs are annotation-determined (C-48) and that the derivation is independently reproducible (C-50) but do not state that the two dimensions constrain independently or that evidence volume cannot compensate for inertia absence at a fixed phase level. The C-53 discriminator is the independence-as-principle statement; absent in all four.

---

## C-52 Discriminator Detail

The R16 discriminator for C-52 is the three-part structural upgrade from inline mandatory statement (C-42) to named first output section with inter-section citation. V-02 earns C-52 by satisfying all three conditions simultaneously: the annotation-derived dimension values occupy a dedicated output slot that is the first named section in the output structure; Q7 of the self-containment check references that slot by name; and the Confidence section cites that slot by name when stating the ceiling constraint. The effect is a closed annotation-to-synthesis traceability chain: the annotation inventory produces dimension values (C-44), those values are named in the ceiling computation step (C-48), the derivation is confirmed reproducible (C-50), and the annotation-derived values are now both a mandatory output slot (C-52 condition 1) and a cited anchor for the synthesis reasoning section (C-52 condition 3). The three C-52 conditions are individually achievable but collectively define the strongest annotation-to-synthesis traceability form: the ceiling is not only declared before synthesis reasoning but is structurally positioned as an authority that the synthesis reasoning section must cite. The failing condition for C-52 is carrying C-42 in its inline form — mandatory but not a named section, and not cited by the Confidence section.

---

## C-53 Discriminator Detail

The R16 discriminator for C-53 is the presence of an explicit dimensional independence statement in the ceiling computation step — a stated principle about the constraint semantics of the two ceiling dimensions, not merely a statement that both are present or annotation-determined. V-04 earns C-53 by extending the C-48 -> C-50 chain with a principle: the two dimensions constrain independently (not additively), and a large or high-quality inertia-absent evidence base cannot outrun the inertia-absent ceiling column at any fixed evidence phase level. This forecloses a reader inference that C-48 and C-50 alone leave open: knowing that both inputs are annotation-determined and that the derivation is reproducible does not tell the reader that inertia absence imposes a hard ceiling that evidence volume cannot compensate for. The C-53 discriminator is the stated independence principle and fixed-phase constraint; its absence in V-01/V-02/V-03/V-05 means that those variations leave the compensation inference open even with C-50 PASS. C-53 requires the principle to appear in the ceiling computation step (not in preamble, role definitions, or annotation instructions) and to state both the independence claim and its fixed-phase practical consequence.

---

## Criteria Reference (all versions)

### Essential Criteria (carried from v1-v8; unchanged)

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

### Aspirational Criteria (v1-v8 additions, C-20-C-34)

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

**v1-v8 aspirational subtotal**: 37.5 pts / 15 criteria

---

### Aspirational Criteria (v9-v17 additions, C-35-C-53)

| ID | Name | Points | Version Added | Extends |
|----|------|--------|---------------|---------|
| C-35 | Concurrent execution + seamless output | 2.5 | v9 | -- |
| C-36 | Dual-exemplar adversarial gate | 2.5 | v9 | -- |
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
| C-50 | Ceiling derivation end-to-end reproducibility claim | 2.5 | v16 | C-48 |
| C-51 | Self-containment Q4 explicit section-name binding | 2.5 | v16 | C-47 + C-49 |
| C-52 | Ceiling Declaration promoted to first named output section with inter-section citation | 2.5 | **v17** | C-42 |
| C-53 | Explicit dimensional independence statement in ceiling computation step | 2.5 | **v17** | C-48 + C-50 |

**v9-v17 aspirational subtotal**: 47.5 pts / 19 criteria

---

### Full Scoring Summary

| Band | Criteria | Points |
|------|----------|--------|
| Essential (C-01-C-19) | 19 | 95.0 |
| Aspirational v1-v8 (C-20-C-34) | 15 | 37.5 |
| Aspirational v9-v17 (C-35-C-53) | 19 | 47.5 |
| **Total** | **53** | **202.5** |

**Golden threshold**: all 19 essential PASS AND composite >= 90

---

## Full Version History

| Version | Date | Delta Criteria | Max Composite | Key Addition |
|---------|------|----------------|---------------|--------------|
| v1 | 2026-03-14 | baseline | -- | Initial rubric |
| v9 | 2026-03-14 | +4 | 155.0 | Concurrent execution, dual-exemplar gate, slot-indexed check, closure attribution |
| v10 | 2026-03-14 | +4 | 165.0 | Phase-gated ceiling, concurrent gate block, slot-indexed revision mandate |
| v11 | 2026-03-14 | +3 | 172.5 | Ceiling declaration, per-role dual exemplars |
| v12 | 2026-03-14 | +2 | 177.5 | Per-signal annotated inventory, two-dimensional ceiling table |
| v13 | 2026-03-14 | +2 | 182.5 | Annotation-to-ceiling derivation linkage, extended declaration coverage in self-containment |
| v14 | 2026-03-14 | +2 | 187.5 | (see v14 release notes) |
| v15 | 2026-03-15 | +2 | 192.5 | Ceiling derivation intersection mechanics (C-48), dedicated inertia-scope traceability section (C-49) |
| v16 | 2026-03-15 | +2 | 197.5 | Ceiling derivation end-to-end reproducibility claim (C-50), self-containment Q4 explicit section-name binding (C-51) |
| **v17** | **2026-03-15** | **+2** | **202.5** | **Ceiling Declaration promoted to first named output section with inter-section citation (C-52), explicit dimensional independence statement in ceiling computation step (C-53)** |
```
