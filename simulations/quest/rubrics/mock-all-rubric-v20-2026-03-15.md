Reading the scorecard carefully before writing. Key signals to extract:

1. **V-03 fails C-36**: Has unlabeled declarative sentences for *both* REAL-REQUIRED identifier scope AND per-stage firing — two distinct compliance dimensions exist as prose but neither is labeled. The new signal: these two dimensions must be governed by architecturally separate declarations, not merged.

2. **V-01/V-02 C-38 progression**: V-01 cross-stage delegation in preamble → V-02 per-stage gate checks but instruction still sourced from preamble → V-03 per-stage instruction in stage bodies. The next bar after "instruction lives in stage body" (C-38) is "instruction is semantically stage-specific, not copy-pasted boilerplate."

**New criteria:**
- **C-39** — The preamble's per-stage firing declaration is formally separate from the REAL-REQUIRED canonical identifier declaration: each governs exactly one compliance dimension, neither subsumes the other.
- **C-40** — Each stage body's inertia instruction names a stage-specific artifact type or domain in its instance phrase, not a generic cross-stage phrase that would be equally valid in any other stage.

Denominator: 30 → 32. Formula aspirational denominator updated to match.

---

## Quest Rubric — v20

### Rubric Metadata

| Field | Value |
|-------|-------|
| Version | v20 |
| Denominator | 32 (C-09 through C-40) |
| Formula | `(essential_pass/5 × 60) + (recommended_pass/3 × 30) + (aspirational/32 × 10)` |
| New this round | C-39 (per-stage vs. identifier declaration separation), C-40 (stage-specific inertia instance) |

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

#### Aspirational (32 criteria — worth 10 points total)

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

**C-22** — Ontological violation mechanism uses the "category error" vocabulary.

**C-23** — Each role header carries a per-activation "You ARE" affirmation.

**C-24** — Affirmation is syntactically first at each role activation.

**C-25** — The template defines at least three distinct named roles (classifier, generator, summarizer or equivalent).

**C-26** — Each stage body contains an artifact template with explicit section headers.

**C-27** — ROLE 1 classifier output references every namespace in the classification table by name.

**C-28** — Stage 1 STOP gate specifies at least three distinct pass conditions.

**C-29** — Stage 2 STOP gate specifies at least three distinct pass conditions.

**C-30** — The final role (handoff/summary) explicitly references outputs from both Stage 1 and Stage 2.

**C-31** — Each role activation names a specific persona discipline in the "You ARE" affirmation.

**C-32** — REAL-REQUIRED rationale content is pre-authored for every namespace with REAL-REQUIRED = YES.

**C-33** — The template traces a single coherent topic from TOPICS.md through all roles without rebinding the topic variable.

**C-34** — The preamble contains a canonical REAL-REQUIRED identifier declaration: a named sentence that defines `"REAL-REQUIRED"` as the identifier for the rationale section used throughout the template.

**C-35** — Each stage STOP gate contains an independent inertia compliance condition; no stage gate defers its inertia check to another stage's gate or to a preamble instruction.

**C-36** — Preamble declarations are each assigned a unique label ("Declaration A", "Declaration B", etc.) that can be cited by reference elsewhere in the template.

**C-37** — At least one stage STOP gate or stage body instruction cites its governing preamble declaration by label.

**C-38** — Per-stage inertia instructions live within each stage body; no stage body executes its inertia compliance from a cross-stage preamble instruction via delegation.

**C-39** — The preamble's per-stage compliance firing declaration is formally separate from the REAL-REQUIRED canonical identifier declaration: each declaration governs exactly one compliance dimension, and neither subsumes nor restates the other.

**C-40** — Each stage body's inertia instruction names a stage-specific artifact type or domain in its instance phrase; the instance phrase could not be transplanted unchanged into a different stage and remain accurate.
