Reading the scorecard carefully before writing. The V-04 vs V-05 distinction is the primary excellence signal this round — both score 100.0 on C-39 and C-40, but V-05 carries a structurally stronger guarantee by pre-seeding example phrases rather than relying on model compliance with a domain-constraint instruction. That structural distinction maps directly to a new criterion.

---

## Quest Rubric — v21

### Rubric Metadata

| Field | Value |
|-------|-------|
| Version | v21 |
| Denominator | 33 (C-09 through C-41) |
| Formula | `(essential_pass/5 × 60) + (recommended_pass/3 × 30) + (aspirational/33 × 10)` |
| New this round | C-41 (pre-seeded example phrase per stage, not instruction-only domain constraint) |

---

### Criteria Tiers

#### Essential (5 criteria — worth 60 points)

**E-01** — The template opens with a TOPICS.md lookup and a tier state line before any role activates.

**E-02** — The template contains a classification table with the correct column headers.

**E-03** — The classification table contains exactly nine namespace rows.

**E-04** — The template's role activations proceed through sequential gated phases that cannot be skipped.

**E-05** — The template contains a REAL-REQUIRED block structure with at least one entry.

---

#### Recommended (3 criteria — worth 30 points)

**R-01** — Each namespace row uses the required MUST/DO NOT vocabulary in its per-namespace instruction.

**R-02** — The template contains an explicit body vocabulary compliance instruction.

**R-03** — Each stage STOP gate references a condition derived from the classification table.

---

#### Aspirational (33 criteria — worth 10 points total)

**C-09** — TOPICS.md lookup + tier state line present before any role activates.

**C-10** — Classification table column headers present and correctly named.

**C-11** — Nine namespace rows present in classification table.

**C-12** — Sequential gated phases present; phases cannot be skipped.

**C-13** — REAL-REQUIRED block structure present.

**C-14** — Per-namespace MUST/DO NOT use vocabulary present.

**C-15** — Body vocabulary compliance instruction present.

**C-16** — Stage STOP gate references classification-derived conditions.

**C-17** — Inertia extension instruction present.

**C-18** — Named phases with an ontological violation mechanism present.

**C-19** — Depth-anchored seed phrases present.

**C-20** — Body-grounding instruction present.

**C-21** — Inertia gap skeleton column pre-seeded in template body.

**C-22** — REAL-REQUIRED rationale section copied by canonical identifier, not by location heuristic.

**C-23** — Per-namespace inertia seed phrases are drawn from an authoritative list declared before ROLE 1.

**C-24** — Stage STOP gate for Stage 1 checks that every compliance-tagged namespace has a REAL-REQUIRED block.

**C-25** — Stage STOP gate for Stage 2 checks that every compliance-tagged namespace with REAL-REQUIRED = YES has been addressed.

**C-26** — Ontological identity framing names a specific category error (artifact output while in classifier role = ceased to be classifier).

**C-27** — Classification table column 8 (inertia gap skeleton) is pre-seeded with verbatim seed phrases from the authoritative list, not left blank.

**C-28** — Per-stage body vocabulary instruction names the vocabulary register for that stage (e.g., specification language / study-data framing / discovery-signal language).

**C-29** — Per-stage body vocabulary instruction names explicit DO NOT terms alongside the required register.

**C-30** — The inertia extension format string `-- specifically, {instance}` appears in each stage header.

**C-31** — The REAL-REQUIRED block carries a rationale section, not just a presence flag.

**C-32** — The template distinguishes compliance-tagged namespaces from non-compliance-tagged namespaces in the classification table.

**C-33** — Each namespace row's REAL-REQUIRED column is pre-populated (YES/NO/—) rather than left to the model to determine.

**C-34** — Preamble contains a canonical list of REAL-REQUIRED identifiers with their governing rationale, separate from the classification table.

**C-35** — Each stage body instruction names the specific artifact class that stage produces, not a generic cross-stage artifact label.

**C-36** — Both the REAL-REQUIRED identifier scope declaration and the per-stage firing declaration are present as explicit prose (unlabeled acceptable; presence required).

**C-37** — The REAL-REQUIRED identifier scope declaration names a canonical identifier and governs how the GENERATOR locates the rationale block.

**C-38** — The per-stage inertia firing instruction lives in the stage body, not solely in the preamble.

**C-39** — The preamble's per-stage firing declaration is formally separate from the REAL-REQUIRED canonical identifier declaration: each governs exactly one compliance dimension, neither subsumes the other.

*Diagnostic: Read Declaration A alone — does it contain per-stage firing language? Read Declaration B alone — does it contain REAL-REQUIRED identifier language? Either contamination = FAIL.*

**C-40** — Each stage body's inertia instruction names a stage-specific artifact type or domain in its instance phrase, not a generic cross-stage phrase that would be equally valid in any other stage.

*Diagnostic: Stage 1 instance must name HIGH-STRUCTURE domain (state transition / boundary contract / trigger condition / configuration key). Stage 2: EVIDENCE-HEAVY (study finding / empirical result / adoption measurement / hypothesis outcome). Stage 3: MIXED (market signal / design judgment / delivery milestone / coverage gap). Generic placeholder valid across all stages = FAIL.*

**C-41** — Each stage body's inertia instance placeholder carries a pre-seeded example phrase for that stage's domain, not merely a domain-constraint instruction. The example phrase is stage-specific (e.g., "the trigger condition that determines when {topic}'s state machine transitions from PENDING to ACTIVE under nominal load") so the model copies rather than infers the instance type.

*Diagnostic: Does each stage placeholder contain a concrete `e.g.`-style phrase that already instantiates the correct domain vocabulary? Instruction-only constraint with a bare `{domain instance for {topic}}` placeholder = FAIL. Pre-seeded phrase that the model can copy and adapt = PASS. Strongest form: placeholder embeds the example inline, not in a separate instruction block.*

---

### Scoring Reference

| Component | Max Points | Formula |
|-----------|-----------|---------|
| Essential | 60 | `(E_pass / 5) × 60` |
| Recommended | 30 | `(R_pass / 3) × 30` |
| Aspirational | 10 | `(A_pass / 33) × 10` |
| **Total** | **100** | sum |

**Perfect score:** 5E + 3R + 33A = 100.0

**C-41 structural note:** C-40 and C-41 form a progression — C-40 checks that the domain vocabulary is stage-specific; C-41 checks that the placeholder is pre-instantiated rather than instruction-governed. A template can pass C-40 by naming the correct domain in an instruction while still failing C-41 because it leaves inference to the model. V-04 (R20) exemplifies this: correct domain constraint, bare placeholder — C-40 PASS, C-41 FAIL. V-05 exemplifies the full bar: correct domain + pre-seeded phrase — both PASS.
