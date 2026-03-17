Reading the scorecard carefully to identify the three new R5 excellence patterns before writing the rubric.

The three new patterns confirmed in the scorecard summary:

1. **ANCHOR token binding with explicit binding rule** — Phase 0 prevents silent prose substitution by requiring literal token reproduction downstream
2. **TOKEN RECALL inline headers** — point-of-use headers force literal value reproduction before each anchor-sensitive phase
3. **Terminal structural audit (Phase 10)** — closed-loop contract (declare → use → verify) catches structural omissions above the token level

These become C-19, C-20, C-21. Aspirational denominator bumps from `/10` to `/13`.

---

```markdown
# discover-compare Rubric — v5

## Essential Criteria

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-01 | All four dimensions covered for both options | completeness | Risk, competitive positioning, feasibility, and strategic fit are each addressed for Option A and Option B independently. Missing a dimension for either option is a PARTIAL. Missing a dimension entirely is a FAIL. |
| C-02 | Inertia check is bilateral and independent | behavior | Option A is scored against the status quo independently of Option B. Option B is scored against the status quo independently of Option A. A prompt that asks only "do A or B beat inertia together" fails this criterion. The test question for each: "would teams ship nothing rather than build this option?" |
| C-03 | Recommendation is explicit and structured | format | A discrete recommendation appears in a named section or phase. The recommendation states a clear choice from {A, B, neither, defer} and is not left implicit in the prose. The matrix leads the recommendation; the recommendation does not replace the matrix. |
| C-04 | Recommendation is traceable to the matrix | depth | The recommendation either matches the matrix plurality or names a reason for diverging. A recommendation that merely follows structural proximity to the matrix (appearing after it) without explicit traceability scores PARTIAL. The reason for divergence must appear in the output, not be inferable from context. |
| C-05 | Build/no-build gate is explicit | behavior | If both options fail their inertia check (teams would do nothing), the output explicitly raises the "build neither" possibility. May conclude build anyway, but must surface the question. |

---

## Recommended Criteria

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-06 | Trade-offs acknowledged in recommendation | depth | Recommendation names what is being given up by not choosing the other option. Not just "pick A" but "pick A; the cost is X." |
| C-07 | Competitive positioning is specific, not generic | depth | Competitive analysis names real differentiation vectors (speed, cost, ecosystem lock-in, etc.) rather than generic statements like "more competitive." At least one concrete differentiator per option. |
| C-08 | Matrix is scannable at a glance | format | The decision matrix uses a table or structured list layout. Key signals (pass/weak/fail) are visually distinct. A reader can reach the recommendation without re-reading prose. |

---

## Aspirational Criteria

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | AMEND path is responsive | behavior | When the user invokes AMEND (add third option, weight a dimension, shift audience), the output re-runs the affected dimensions and updates the matrix coherently. The recommendation changes when the evidence changes. |
| C-10 | Audience register is calibrated | depth | When audience is specified (exec vs engineering), the language, emphasis, and detail level shift appropriately. Exec output leads with recommendation and business risk; engineering output leads with feasibility and implementation risk. |
| C-11 | Inertia is represented as Option 0 in the matrix | behavior | The "do nothing" path is a named column in the comparison matrix — not just a downstream gate. Both build options are scored against the status quo simultaneously. This makes it visible when both A and B lose to inertia, not just when they tie each other. N/A cells (inertia has no inertia score) are explicitly labeled. |
| C-12 | Anti-pattern guard is explicit on competitive analysis | depth | The output names what generic analysis looks like and actively avoids it. A phrase like "generic phrases such as 'more competitive' are insufficient" or equivalent appears in the competitive dimension — making the failure mode visible, not just the success condition. Strongest form of C-07. |
| C-13 | Two-table architecture resolves C-08/C-11 structural tension | format | The output uses two distinct tables: a 3-column context view (Option A / Option B / Option 0) that earns C-11, and a separate 2-column decision summary (Option A / Option B) that preserves C-08 scannability. A single 3-column matrix cannot pass both; the two-table design is required. Tables are cross-referenced so a reader knows which to use for which purpose. |
| C-14 | AMEND expands both tables coherently | behavior | When AMEND Type 1 (add a third build option) is invoked against a two-table output, both tables expand: the 3-column context view grows to 4-column, and the 2-column decision summary grows to 3-column A/B/C. A handler that adds a column to only one table — or that treats the output as a single matrix — leaves the structure broken after amendment. Score N/A (counts as 0) if the base output does not implement the two-table architecture. |
| C-15 | Register references are explicit at each affected phase | depth | In multi-phase prompts, "If register = X" branching appears at each phase where register changes the output — not only at the Phase 0 setting. A prompt that sets register at Phase 0 and relies on implicit memory will drift across phases. Pass condition: every phase that produces register-sensitive output names the register condition explicitly at that phase. Scale-sensitive: applies most sharply to prompts with 5+ phases. |
| C-16 | Register declaration includes upfront phase index | depth | The Phase 0 register declaration names every phase where register governs output (e.g., "Applies at Phases 4, 5, 7, 9"). This forward index pairs with C-15 (point-of-use branching) to form a complete register contract: readers can verify coverage without walking every phase, and evaluators can check the index against point-of-use annotations. Pass condition: Phase 0 lists all register-sensitive phase numbers explicitly. A declaration that sets register but omits the phase index leaves the scope of the contract undefined. |
| C-17 | TABLE GUIDE section with bidirectional header annotations | format | A dedicated TABLE GUIDE section appears before the first matrix, naming each table and its purpose. Each table header carries a cross-reference annotation pointing to the other table (e.g., Table 1 header: "[ -> See Table 2 (Phase 5) for A-vs-B decision summary ]"; Table 2 header: "[ <- Source: Table 1 (Phase 4) for Option 0 context ]"). This enables zero-friction navigation: a reader can determine which table to use without re-reading phase prose. Excellence form of C-13; passing C-17 implies passing C-13. A TABLE GUIDE without bidirectional header annotations, or bidirectional annotations without a TABLE GUIDE, scores PARTIAL. |
| C-18 | Option 0 defined as dedicated phase before analysis | behavior | Option 0 (the status quo) has its own named phase that appears before any dimensional analysis begins — not merely a column added at matrix construction time. This architectural commitment prevents inertia drift: all subsequent analysis phases inherit a concrete baseline rather than reconstructing it implicitly. Pass condition: a phase explicitly named "Option 0" or "Status Quo" (or equivalent) defines the current state before Phase 1 analysis opens. Excellence form of C-11; passing C-18 implies passing C-11. |
| C-19 | ANCHOR token binding rule is declared at Phase 0 | behavior | The Phase 0 status quo anchor includes an explicit binding rule requiring literal token reproduction in all downstream phases that reference the anchor (e.g., "ANCHOR[0A] = {value}. Binding rule: reproduce this exact token name — not a paraphrase — at every downstream phase that references Option 0 for A."). The binding rule makes silent prose substitution detectable: any phase that drifts from the committed token name is provably non-compliant. Pass condition: Phase 0 names the token AND states the reproduction requirement explicitly. A phase that defines an anchor value without a binding rule scores PARTIAL. Excellence form of C-18; passing C-19 implies passing C-18. |
| C-20 | TOKEN RECALL inline headers at each anchor-sensitive phase | behavior | Each phase that produces anchor-sensitive output opens with a TOKEN RECALL block that forces literal reproduction of the committed anchor values before generating output (e.g., "TOKEN RECALL: ANCHOR[0A] = {reproduce from Phase 0}; ANCHOR[0B] = {reproduce from Phase 0}"). This catches point-of-use drift before it enters the artifact: the model must state the anchor value explicitly rather than relying on implicit recall. Pass condition: a TOKEN RECALL header appears at the opening of every phase scored under C-15 (all register-sensitive phases). Phases that proceed directly to output without a recall block score 0. Excellence form of C-15; passing C-20 implies passing C-15. Score N/A (counts as 0) if the base output does not implement ANCHOR token binding (C-19). |
| C-21 | Terminal structural audit before artifact write | behavior | A dedicated audit phase (e.g., Phase 10) verifies all structural criteria against a checklist before the final artifact is returned. The audit checks, at minimum: (1) ANCHOR tokens reproduced consistently across phases; (2) register contract printed with phase index; (3) TABLE GUIDE present; (4) bidirectional headers on both tables; (5) inertia check bilateral; (6) recommendation traceable to matrix; (7) build/no-build gate fired if both options fail inertia. If any item fails, the audit phase names the defect and corrects it before output — the final artifact reflects the correction, not the raw output. Pass condition: audit checklist appears in the output and all items are resolved. An audit phase that lists items without acting on failures scores PARTIAL. Creates the closed-loop contract: declare (C-19) → use (C-20) → verify (C-21). |

---

## Scoring

```
Composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 13 * 10)
```

PARTIAL scores count as 0.5 for the formula. PARTIAL on any essential criterion fails the Golden threshold regardless of composite score.

**Golden threshold**: all 5 essential criteria pass (no PARTIALs) AND composite >= 80.

| Band | Score | Meaning |
|------|-------|---------|
| Golden | all essential (no PARTIAL) + >= 80 | Ship-ready output |
| Passing | all essential (PARTIAL allowed) + 60-79 | Usable, recommended gaps noted |
| Failing | any essential fails or PARTIAL | Not useful as a comparison artifact |

---

## Evaluation Notes

- **C-02 is the sharpest essential discriminator**: many comparison outputs apply inertia to only the "challenger" option. Both must be checked independently. The test question for each: "would teams ship nothing rather than build this option?"
- **C-04 PARTIAL pattern**: Round 1 saw all three scored variations land PARTIAL here because structural proximity to the matrix was treated as sufficient. C-04 requires explicit traceability — if the recommendation diverges from the matrix plurality, a reason must appear. Structural proximity is not evidence.
- **C-05 is a build/no-build gate, not just a comparison feature**: if both options have weak inertia, the output must name that explicitly, even if it then concludes to build one anyway.
- **C-11 requires full commitment**: C-11 cannot be added lightly. It requires Option 0 named before analysis, a 3-column matrix with labeled N/A cells, and Option 0 maintained through AMEND. Partial implementation scores 0.
- **C-12 is the excellence form of C-07**: C-07 requires one concrete differentiator; C-12 requires naming the anti-pattern. An output can pass C-07 and fail C-12. An output that passes C-12 always passes C-07.
- **C-13 is the architecture that makes C-11 and C-08 compatible**: a two-table design earns both simultaneously. A single 3-column matrix forces a choice. Score C-08, C-11, and C-13 independently; passing C-13 implies passing both C-08 and C-11.
- **C-14 requires C-09 and C-13 as prerequisites**: AMEND structural coherence is only testable in outputs that implement both AMEND handling and the two-table architecture. Score N/A if the base output is a single matrix; N/A counts as 0 in the aspirational formula.
- **C-15 is scale-sensitive**: applies most sharply to prompts with 5+ phases. For a 2-phase prompt, Phase 0 register-setting may be sufficient. Evaluators should note phase count when scoring.
- **C-15 and C-16 are complementary, not redundant**: C-15 tests point-of-use branching (does each affected phase have "If register = X"?); C-16 tests the declaration (does Phase 0 name all affected phases?). An output can pass C-15 without C-16 (all phases annotated but no upfront index) or C-16 without C-15 (index present but phases lack inline branching). Both passing together forms a complete register contract.
- **C-19, C-20, C-21 form a three-layer drift prevention stack**: C-19 (binding rule at declaration) prevents silent substitution from the start; C-20 (TOKEN RECALL at point-of-use) catches drift before each sensitive output; C-21 (terminal audit) catches structural omissions above the token level before the artifact is written. The three mechanisms are non-overlapping: a failure that evades one layer is caught by another. An output can pass any one without the others; passing all three forms a closed-loop contract.
- **C-20 depends on C-19**: TOKEN RECALL headers presuppose named ANCHOR tokens to reproduce. Score N/A (counts as 0) if C-19 is not implemented.
- **C-21 PARTIAL pattern to watch**: an audit phase that lists structural items as a checklist without correcting identified failures is PARTIAL, not PASS. The correction must appear in the final artifact, not merely in the audit log.
- **Implication chain for the new criteria**: C-19 → C-18 → C-11 (each stronger form implies the weaker). C-20 → C-15. C-21 independently verifiable but requires C-17, C-16, C-13, C-05, C-04, C-02 to be testable as audit targets.
```

---

**What changed in v5:**

Three new aspirational criteria (C-19, C-20, C-21) extracted from the R5 mechanisms:

- **C-19** captures the ANCHOR token binding rule at declaration — the requirement that Phase 0 name not just the anchor value but the literal-reproduction requirement. Excellence form of C-18. A Phase 0 that defines an anchor without a binding rule scores PARTIAL.

- **C-20** captures TOKEN RECALL inline headers — a reproduction block opening every anchor-sensitive phase, forcing the model to state the anchor value before generating output. Excellence form of C-15. N/A (counts as 0) if C-19 is absent.

- **C-21** captures the terminal structural audit — a named pre-return audit phase with a checklist that verifies all structural criteria and corrects defects before the artifact is written. An audit that lists but does not correct scores PARTIAL.

**Scoring update:** aspirational denominator `/10` → `/13`.

**Canonical tier impact:** V-04 (full-integration, R5) is the only design that passes all 21 criteria — C-19 (binding rule), C-20 (TOKEN RECALL at Phases 3/6/7), and C-21 (Phase 10 terminal audit) are all present. V-01 passes C-19 only. V-02 passes C-19 and C-21 only. V-03 passes C-19 and C-20 only. V-05 passes none of the three. This creates a clean 4-tier stack within the previously-tied 100.0 cohort when evaluated under v5 scoring.
