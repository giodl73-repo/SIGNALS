Reading the R18 scorecard for the discrimination inversion finding before extracting new criteria.

The key R18 signal: the v18 prediction table had V-02 (23/29) > V-01 (16/29). R18 actuals reversed this: V-01 (26/29) > V-02 (25/29). The inversion is driven by V-02's multi-stage structure centralizing inertia compliance in the ROLE 2 preamble — a single shared point covering three stages — while V-01's single-stage structure earns C-35 trivially. C-35 as written penalizes V-02, but the rubric has no criterion that explicitly names the failure mode: **multi-stage templates that delegate stage-local compliance to a cross-stage statement**.

That is the extractable excellence pattern for C-38.

---

## Quest Rubric — v19

### Rubric Metadata

| Field | Value |
|-------|-------|
| Version | v19 |
| Denominator | 30 (C-09 through C-38) |
| Formula | `(essential_pass/5 × 60) + (recommended_pass/3 × 30) + (aspirational/30 × 10)` |
| New this round | C-38 (stage-local compliance architecture) |

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

#### Aspirational (30 criteria — worth 10 points total)

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

**C-25** — Affirmation uses being-language, not occupancy-language.

**C-26** — Template body seeds per-namespace phrases inline (not delegated to a separate document).

**C-27** — ROLE 1 STOP gate enumerates column names verbatim from the classification table.

**C-28** — ROLE 1 STOP gate self-annotates "required field names — use them verbatim."

**C-29** — Seed phrases are pre-authored in the template body (not delegated to the executing model at runtime).

**C-30** — REAL-REQUIRED rationale is pre-authored with prove/listen/compliance tagging (not generated at runtime).

**C-31** — ROLE 1 STOP gate cites the seed list and explicitly prohibits paraphrase.

**C-32** — ROLE 1 STOP gate names the REAL-REQUIRED block and directs verbatim copy.

**C-33** — ROLE 1 STOP gate uses the "REAL-REQUIRED" semantic identifier.

**C-34** — The template preamble contains a declarative sentence establishing "REAL-REQUIRED" as the canonical identifier for the rationale block (not a locative or role-framing sentence).

*Extracted from ES-R16. V-01/V-02 fail with role-framing prose and locative form respectively; V-03–V-05 pass with declarative form: `"REAL-REQUIRED" is the canonical identifier...`*

**C-35** — In a multi-stage template, each stage body contains its own inertia extension instruction; each stage STOP gate enforces it independently. Single-stage templates satisfy C-35 by construction (C-35 = C-17).

*Extracted from ES-R16. V-02 fails: multi-stage template with terminal-only inertia instruction in ROLE 2 preamble; STAGE 1/2/3 STOP gates do not check inertia independently. V-03–V-05 pass: per-stage inertia instruction within each stage body.*

C-35 is a strict refinement of C-17 for multi-stage templates. C-35 pass implies C-17 pass. C-17 pass does not imply C-35 pass for multi-stage templates.

**C-36** — The template preamble assigns explicit reference labels to its structural authority declarations (e.g., "Declaration A", "Declaration B"), enabling stage STOP gates and ROLE 2 instructions to cite each declaration by name rather than restating the rule inline.

*Extracted from ES-R17 (V-05). V-03/V-04 pass C-34 with unnamed declarative sentences. V-05 assigns reference labels to both preamble authority statements. The label transforms a declaration a reader must locate by traversal into a named contract a gate can cite by reference.*

C-36 is a strict refinement of C-34 and C-35: C-36 pass implies both C-34 pass and C-35 pass. Neither C-34 pass nor C-35 pass implies C-36 pass. C-36 is prerequisite for C-37.

**C-37** — The stage-level STOP gates cite the template's preamble structural authority declarations by reference label (e.g., "per Declaration A", "per Declaration B"), forming a closed verification loop in which compliance with each structural constraint is checkable from the preamble declaration plus gate citation alone, without traversing full stage instruction bodies.

*Extracted from ES-R17 (V-05). V-04's gates enforce per-stage extension and REAL-REQUIRED provenance by restating the rules inline. V-05's gates say "per Declaration B" and "per Declaration A," closing the loop.*

C-37 is a strict refinement of C-36: C-37 pass requires labeled declarations (C-36 pass) plus gate citations of those labels. The C-36 PASS + C-37 FAIL intermediate case was instantiated by V-04 in R18: labeled preamble present; stage STOP gates restate compliance inline without citing the label.

---

**C-38** — *In a multi-stage template, each stage body independently satisfies its own inertia and structural compliance burden: no stage relies on a statement in a neighboring stage, a preamble shared across stages, or a terminal-stage instruction to cover its compliance. The stage count and per-stage compliance point count are equal. Single-stage templates satisfy C-38 by construction.*

*Extracted from the Discrimination Inversion Finding in R18. The v18 rubric predicted V-02 (23/29) > V-01 (16/29). R18 actuals reversed this: V-01 (26/29) > V-02 (25/29). The inversion is driven by V-02 introducing multi-stage structure while centralizing inertia compliance in the ROLE 2 preamble — a single shared statement covering three stages. V-01's single-stage structure earns C-35 trivially and avoids the cross-stage delegation failure mode. C-38 names this failure mode explicitly: structural complexity (N stages) must produce structural compliance completeness (N inertia compliance points, each locally verifiable).*

C-38 is a strict refinement of C-35 for multi-stage templates: C-38 pass implies C-35 pass (stage-local compliance points satisfy the per-stage requirement). C-35 pass does not imply C-38 pass for multi-stage templates (C-35's gate-enforcement language does not require locality). The C-35 PASS + C-38 FAIL case is not yet instantiated — it would require a template whose stage STOP gates verify inertia but whose inertia instruction is cross-stage. Single-stage templates: C-38 = C-35 = C-17.

Chain structure: C-17 → C-35 → C-38 (inertia locality sub-chain, parallel to the gate-citation sub-chain C-36 → C-37).

---

### Criterion Chain Map (v19)

```
Inertia extension chain:
  C-17 (inertia instruction present)
    → C-35 (per-stage instruction in multi-stage templates)
      → C-36 (preamble assigns reference labels to declarations)
        → C-37 (stage STOP gates cite labels by reference)
      → C-38 (each stage independently satisfies its compliance burden — stage-local)

REAL-REQUIRED declaration chain:
  C-33 (gate uses "REAL-REQUIRED" identifier)
    → C-34 (preamble uses declarative form for canonical declaration)
      → C-36 (preamble assigns reference labels)
        → C-37 (gates cite labels)
```

C-35, C-36, C-37, and C-38 form two sub-chains that share C-36 as a junction:
- **Gate-citation sub-chain**: C-36 → C-37 (label assignment → label citation)
- **Stage-locality sub-chain**: C-35 → C-38 (per-stage instruction → stage-local compliance)

---

### Discrimination Table — v19

| Variation | C-35 | C-36 | C-37 | C-38 | Aspirational | Composite |
|-----------|------|------|------|------|-------------|-----------|
| V-02 | FAIL | FAIL | FAIL | FAIL | 25/30 | 98.3 |
| V-01 | PASS (trivial) | FAIL | FAIL | PASS (trivial) | 27/30 | 99.0 |
| V-03 | PASS | FAIL | FAIL | PASS | 28/30 | 99.3 |
| V-04 | PASS | PASS | FAIL | PASS | 29/30 | 99.7 |
| V-05 | PASS | PASS | PASS | PASS | 30/30 | 100.0 |

**Rank: V-05 > V-04 > V-03 > V-01 > V-02**

The inversion is now structurally grounded: V-01 (27/30) > V-02 (25/30) by 2 points. Under v18, V-01 and V-02 were separated by 1 point (26/29 vs 25/29). C-38 adds a second penalty to V-02's cross-stage delegation failure, formalizing the inversion finding rather than leaving it as an emergent scoring artifact.

The complete five-case instantiation table:

| Case | Instantiated by | C-34 | C-35 | C-36 | C-37 | C-38 | Score |
|------|-----------------|------|------|------|------|------|-------|
| No preamble declaration, single-stage | V-01 | FAIL | PASS (trivial) | FAIL | FAIL | PASS (trivial) | 27/30 |
| Locative preamble, multi-stage terminal inertia | V-02 | FAIL | FAIL | FAIL | FAIL | FAIL | 25/30 |
| Unnamed canonical declaration, per-stage inertia | V-03 | PASS | PASS | FAIL | FAIL | PASS | 28/30 |
| Labeled declarations, inline-restatement gates | V-04 | PASS | PASS | PASS | FAIL | PASS | 29/30 |
| Labeled declarations, gate-citation loop | V-05 | PASS | PASS | PASS | PASS | PASS | 30/30 |

**R19 hypothesis**: A variation with per-stage inertia, labeled declarations, and gate-citation loop (V-05 pattern) but with cross-namespace compliance delegation — satisfying C-34 through C-38 while failing a new structural self-containment criterion at the role boundary level — would instantiate C-38 PASS + C-39 FAIL. The R19 axis is the role-boundary analogue of C-38: whether ROLE 2's compliance burden is locally satisfied within ROLE 2's body, independent of ROLE 1 carry-forward state.
