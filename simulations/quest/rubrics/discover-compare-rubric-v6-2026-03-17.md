Reading the scorecard carefully to identify the three new R6 excellence patterns before writing the rubric.

The three new patterns confirmed in the scorecard summary:

1. **Pre-artifact gate** — audit fires before artifact write; corrections don't require rewrite because the file doesn't exist yet (V-02 architectural distinction)
2. **Bilateral verdict sentences with independence constraint** — VERDICT A / VERDICT B as separate named output sentences each grounded only to its own ANCHOR token; audit verifies no cross-reference (V-03 pattern)
3. **Audit checklist items per TOKEN RECALL phase** — closes C-20/C-21 loop; each phase required to have TOKEN RECALL gains a corresponding audit checklist item, making completeness verifiable (pattern extracted from V-01/V-03/V-04 and named in the R6 summary)

These become C-22, C-23, C-24. Aspirational denominator bumps from `/13` to `/16`.

---

```markdown
# discover-compare Rubric — v6

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
| C-21 | Terminal structural audit before artifact write | behavior | A dedicated audit phase verifies all structural criteria against a checklist before the final artifact is returned. The audit checks, at minimum: (1) ANCHOR tokens reproduced consistently across phases; (2) register contract printed with phase index; (3) TABLE GUIDE present; (4) bidirectional headers on both tables; (5) inertia check bilateral; (6) recommendation traceable to matrix; (7) build/no-build gate fired if both options fail inertia. If any item fails, the audit phase names the defect and corrects it before output — the final artifact reflects the correction, not the raw output. Pass condition: audit checklist appears in the output and all items are resolved. An audit phase that lists items without acting on failures scores PARTIAL. Creates the closed-loop contract: declare (C-19) → use (C-20) → verify (C-21). |
| C-22 | Structural audit fires before artifact write (pre-artifact gate) | behavior | The structural audit phase is positioned before the artifact-write phase — not after — so that any correction determines what gets written rather than requiring a retroactive update to an already-written file. Pass condition: the audit phase explicitly states that the artifact will not be written until all checklist items pass (e.g., "Before writing the artifact in Phase N, self-verify each item below. If any item fails, correct it NOW — before proceeding to Phase N."). An audit that fires after the artifact is written cannot satisfy this criterion regardless of how corrections are applied. Excellence form of C-21; passing C-22 implies passing C-21. |
| C-23 | Bilateral inertia verdict sentences with independence constraint | behavior | The inertia gate produces two named, separate verdict sentences — VERDICT A and VERDICT B — each grounded only to its own ANCHOR token. The independence constraint is explicit: VERDICT A does not reference Option B; VERDICT B does not reference Option A. The audit verifies the independence constraint before artifact write. Pass condition: (1) both VERDICT A and VERDICT B appear as distinct labeled sentences; (2) each verdict names the specific mechanism driving inertia for that option alone; (3) the audit carries an item verifying cross-reference absence. A combined verdict ("both options face inertia") fails this criterion. Excellence form of C-02; passing C-23 implies passing C-02. Score N/A (counts as 0) if C-21 is not implemented. |
| C-24 | Audit checklist carries one item per required TOKEN RECALL phase | behavior | For each phase required to carry a TOKEN RECALL block under C-20, the C-21 (or C-22) audit checklist includes a corresponding item verifying that phase's recall block was present and reproduced the correct token values. This closes the C-20/C-21 loop: TOKEN RECALL completeness is verifiable from the audit output alone, without re-reading every phase. Pass condition: the number of TOKEN RECALL verification items in the audit checklist equals the number of recall-required phases declared in the C-16 phase index. An audit with fewer items than required phases scores PARTIAL. Score N/A (counts as 0) if C-20 or C-21 are not implemented. |

---

## Scoring

```
Composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 16 * 10)
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
- **C-22 vs C-21 architectural distinction**: C-21 (post-write audit) can still correct defects but requires a retroactive artifact update. C-22 (pre-artifact gate) eliminates the rewrite step — corrections happen before the file exists. Both score PASS for C-21; only the pre-gate position earns C-22.
- **C-23 strengthens C-02 observability**: bilateral inertia is required by C-02 structurally, but C-23 makes it an observable output trace. VERDICT A and VERDICT B are discrete tokens the audit can verify, not just a structural property the evaluator must infer.
- **C-24 closes the C-20/C-21 loop**: C-20 requires TOKEN RECALL at N phases; C-24 requires N corresponding audit items. Without C-24, C-21 can pass even when TOKEN RECALL coverage is incomplete — the audit simply doesn't check.
```
