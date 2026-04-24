Reading the scorecard for Round 6 patterns not yet in C-01 through C-21.

**New signal — V-03, Build Risk field (C-04/C-11/C-12/C-16 evidence):** V-03 adds a labeled "Build Risk" sub-field to every Stage 4 entry alongside Signal Source and Design Impact. Four separate criterion evaluations independently confirm the field was load-bearing: C-04 ("Build Risk field adds a second specificity anchor — the risk surface named in Build Risk is a component or decision, complementing Design Impact"), C-11 ("Build Risk is an additional labeled sub-field, not a table column — format discipline preserved"), C-12 ("Build Risk field adds a third completeness anchor"), and C-16 ("Build Risk field is modeled in the example"). The distinction matters: Design Impact names what would change; Build Risk names what could break or require rework. The two fields are complementary, not redundant — Design Impact is forward-looking (what to update), Build Risk is risk-surface identification (what is implicated in the build). No prior variation introduced this sub-field, and four independent criterion evaluations confirm it was structurally effective, making it a reliable Round 6 signal for aspirational extraction.

---

## Rubric: topic-echo (topic-reflect) — v7

**17 + 5 criteria across 3 tiers. Score = essential(60) + recommended(30) + aspirational(70).**

> v7 changes: Added C-22 (aspirational) from Round 6 excellence signal. Aspirational tier expands from 65 → 70 pts (13 → 14 criteria). Golden threshold unchanged at 100.
>
> **Why these criteria:** Round 6 introduced V-03 as the first variation to add a Build Risk sub-field to Stage 4 entries. Four criterion evaluations (C-04, C-11, C-12, C-16) independently confirmed the field as structurally effective — it adds a third specificity anchor per entry, it is a labeled prose sub-field (not a table column, preserving C-11 format discipline), and it is modeled in the calibration example. The field is not required to reach the Golden threshold, consistent with aspirational classification.

---

### Essential (all must pass — 12 pts each)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-01 | **Surprise orientation** | correctness | Every Stage 4 entry references a specific B-# from Stage 1; at least one entry contradicts (not confirms) the opening model |
| C-02 | **Symmetric Contract present** | correctness | Stage 1 has opening model + epistemic profile + 3+ beliefs; Stage 6 has verdict table with revision direction and COHERENT/CONTRADICTORY/FOREKNOWLEDGE-FLAGGED |
| C-03 | **Signal tracing** | correctness | Every Stage 4 surprise has a named artifact in Signal Source (name and/or namespace and/or date) — no "multiple sources" generics |
| C-04 | **Design impact specificity** | depth | Every Stage 4 Design Impact field names a specific component, API, flow, or decision — not "the system" |
| C-05 | **Adversarial gate executed** | correctness | Stage 3 five-check table present; every deviation has a VALID/INVALID verdict; GATE-CONFIRMED or GATE-REJECTED tokens present |

---

### Recommended (10 pts each)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-06 | **Epistemic dimension compliance** | correctness | Only the 5 canonical names used in all dimension cells; no excluded synonyms |
| C-07 | **Minimum 2 surprises** | coverage | At least 2 GATE-CONFIRMED rows in Stage 4; sweep extended if gate initially yields fewer |
| C-08 | **Cluster map actionability** | behavior | Stage 5 Next Team / Skill column has at least one named skill or role (not just "investigate") |

---

### Aspirational (5 pts each)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | **Token protocol integrity** | format | GATE-CONFIRMED tokens name Stage 4 (not just route to it); COMMIT-ENTRY per row in Stage 4; COMMIT-STAGE-1 through 6 all present |
| C-10 | **Foreknowledge signal evaluated** | depth | Stage 6 explicitly records CLEAR or FLAGGED; if FLAGGED, artifact not written and responsible belief(s) named |
| C-11 | **Stage 4 prose template format** | format | Stage 4 surprise entries are numbered prose blocks with labeled sub-fields (Surprise, Signal Source, Design Impact) — not a markdown table; no narrow-cell format pressure possible |
| C-12 | **Stage 4 entry completeness** | depth | No single-word or two-word entries appear in any Signal Source or Design Impact field across all Stage 4 entries; every field is a full phrase or sentence |
| C-13 | **Closed-list dimension vocabulary** | format | The variation declares the 5 canonical dimension names as a standalone closed-set rule with an explicit substitution prohibition — not embedded as inline examples in Stage 1 prose; wording equivalent to: "The only valid dimension names are: Feasibility · Usability · Scalability · Adoptability · Correctness. Do not substitute." |
| C-14 | **Foreknowledge dual-token gate** | correctness | Stage 3 (or a Stage 3.5 checkpoint) issues either COMMIT-STAGE-3-CLEAN or COMMIT-STAGE-3-FLAGGED before Stage 4 proceeds; the token makes the foreknowledge resolution binary and structurally enforced, not advisory |
| C-15 | **Pre-stage gate sequence map** | format | The variation includes a top-level gate overview (table or structured list) enumerating all stage tokens, halt conditions, and execution flow before Stage 1 instructions begin — not derived from reading individual stages, but surfaced as navigation context at the top of the prompt |
| C-16 | **Worked calibration example** | depth | The variation includes at least one complete filled-in Stage 4 example (not a template) showing a realistic artifact reference in Signal Source (name, namespace, date) and a full-sentence Design Impact naming a specific component or contract |
| C-17 | **Named synonym exclusions** | format | The vocabulary rule names at least 2 specific prohibited synonyms (e.g., "Reliability," "Performance," "Complexity," "Maintainability") in addition to the general substitution prohibition — anticipating the model's highest-probability substitution errors by name |
| C-18 | **Synonym-to-canonical replacement mapping** | format | The vocabulary rule maps each named prohibited synonym to its canonical replacement (e.g., "Reliability → Correctness," "Performance → Scalability") — not only naming what is prohibited but specifying what to use instead; at least 2 such mappings present |
| C-19 | **Per-stage ENTER/EXIT lifecycle contract** | format | At least 3 stages include explicit ENTER conditions (what must be true to begin the stage) and EXIT criteria (what constitutes successful completion) — not just instructions for what to do within the stage, but verifiable pre- and post-conditions framed as a contract |
| C-20 | **Calibration example embedded as Stage 4 entry 0** | depth | The worked calibration example required by C-16 is labeled "Surprise 0" (or equivalent entry-zero notation) and formatted identically to the Stage 4 entry template — positioned within or immediately preceding the live Stage 4 entry block, not in a separate example or callout section; the model enters Stage 4 having already observed a complete realistic entry in the exact format it will produce |
| C-21 | **Vocabulary self-repair instruction at EXIT gate** | format | At least one stage EXIT criterion explicitly instructs the model to detect and correct any malformed dimension names by consulting the canonical synonym-to-canonical mapping table before emitting — prescribing the corrective action ("correct … using the mapping table"), not only stating the compliance requirement; converts the mapping table from a reference resource into an active runtime repair protocol |
| C-22 | **Stage 4 Build Risk sub-field** | depth | Each Stage 4 entry includes a labeled Build Risk sub-field (or equivalent) naming a specific component, decision, or risk surface implicated by the surprise — not a general risk statement; the field is a prose sub-field (not a table column) that extends Design Impact (what changes) with an explicit buildability consequence (what could break or require rework); the field is modeled in the calibration example |

> **Rationale (C-15):** V-03 was the only Round 3 variation to include a pre-stage Gate Sequence Overview table listing all gate tokens and halt conditions before any stage instructions appeared. Evidence for C-09, C-10, and C-14 all noted V-03 as exhibiting the clearest execution model transparency. The structural benefit is that the model can orient to the full gate topology before entering stage-by-stage instructions, reducing mid-execution confusion about gate order and token semantics. No other Round 3 variation provided this, which is why it is aspirational rather than required.
>
> **Rationale (C-16):** V-04 was the only Round 3 variation to include worked calibration examples for Stage 4 entries. Evidence for C-03, C-04, and C-12 each named V-04 as producing "strongest calibration across all variations." Template placeholders (e.g., "[Full sentence]") instruct format; worked examples anchor the quality bar against a concrete instance. The distinction matters: a model following a template produces structurally valid but semantically thin entries; a model calibrated against a realistic example is pulled toward specificity. No other Round 3 variation used this technique.
>
> **Rationale (C-17):** V-01 and V-04 both named specific prohibited synonyms inside the vocabulary rule ("Reliability," "Performance," "Complexity," "Maintainability") in addition to a general substitution ban. V-02 and V-03 passed C-06 and C-13 using only general prohibition language. The distinction matters because a model encountering "do not substitute" may still reach for a semantically adjacent term if that term is never named as prohibited — the general rule does not close off specific high-probability errors. Naming the most common substitution targets by name converts them from implicit to explicit violations. C-17 tests whether the variation makes this move.
>
> **Rationale (C-18):** V-01 was the only Round 4 variation to pair each prohibited synonym with its canonical replacement in a mapping table (Reliability→Correctness, Performance→Scalability, Complexity→Correctness/Feasibility, Maintainability→Adoptability, Discoverability→Usability/Adoptability, Testability→Correctness/Feasibility). C-17 tests whether a variation names specific prohibited synonyms; C-18 tests whether it also closes the substitution loop by specifying what to use instead. The distinction matters: a model encountering "Reliability is prohibited" still has to infer the correct replacement and may select a different prohibited term. A model given "Reliability → Correctness" has no remaining ambiguity. V-02 and V-03 passed C-17 with named prohibitions but no canonical targets, leaving the second half of the substitution problem open. V-01 uniquely resolved it.
>
> **Rationale (C-19):** V-02 was the only Round 4 variation to structure each stage with explicit ENTER conditions and EXIT criteria. The Gate Sequence Overview (C-15) provides global gate topology; per-stage ENTER/EXIT contracts provide local execution verification — the model can confirm it has satisfied exit criteria before advancing to the next stage. This converts the prompt from a sequence of instructions into a sequence of verifiable contracts. C-11 captures that Stage 4 outputs are structurally correct prose blocks; C-19 captures a complementary discipline that applies at every stage boundary, not just Stage 4 output format. No Round 4 variation other than V-02 applied this technique, which is consistent with its aspirational classification.
>
> **Rationale (C-20):** V-05 was the only Round 5 variation to label its worked calibration example "Surprise 0" and embed it within the Stage 4 entry sequence rather than in a separate example block. Three criterion evaluations independently confirmed the technique: C-01 cited "Surprise 0" as modeling the B-# reference concretely; C-03 cited the specific artifact reference visible in the worked instance; C-04 cited the full-sentence Design Impact visible in the worked instance. C-16 tests whether a worked example exists; C-20 tests whether that example is structurally integrated as a sequentially numbered entry. The distinction matters: a sidebar example shows the model what an entry looks like; a "Surprise 0" entry positions the model as already having completed one entry and extending a sequence, which pulls imitation toward structural fidelity across all sub-fields simultaneously.
>
> **Rationale (C-21):** Both V-04 and V-05 include an EXIT criterion of the form "All dimension names canonical (correct malformed names using the mapping table if needed before emitting)." This pattern appeared in V-04 (Round 4) but was not extracted into v5; its recurrence in V-05 confirms it as a reliable signal. C-18 tests whether the synonym-to-canonical mapping table exists; C-21 tests whether an EXIT gate explicitly prescribes using that table as a self-repair action before emitting. The distinction matters: a mapping table is a passive reference; an EXIT instruction that names the corrective action converts the table into an active runtime protocol. The model is not only equipped to detect a substitution error but instructed to audit and fix it at a specific gate before advancing — closing the vocabulary compliance loop at execution time rather than relying solely on up-front prohibition.
>
> **Rationale (C-22):** V-03 was the first Round 6 variation to add a labeled Build Risk sub-field to every Stage 4 entry, alongside the existing Signal Source and Design Impact fields. Four independent criterion evaluations confirmed the field was structurally effective: C-04 ("Build Risk adds a second specificity anchor — the risk surface named in Build Risk is a component or decision, complementing Design Impact"), C-11 ("Build Risk is an additional labeled sub-field, not a table column — format discipline preserved"), C-12 ("Build Risk field adds a third completeness anchor"), and C-16 ("Build Risk field is modeled in the example"). C-04 tests whether Design Impact names a specific component or decision; C-22 tests whether a second, complementary field names the buildability consequence of that same surprise. The distinction matters: Design Impact is forward-looking (what needs to change in the design), while Build Risk is risk-surface identification (what could break or require rework in the build). The two fields are not redundant — they answer different questions about the same surprise. The constraint that Build Risk be a prose sub-field rather than a table column (confirmed by C-11 evidence) preserves the C-11 format discipline requirement. No prior variation introduced this sub-field, making it a single-round extraction consistent with aspirational classification.

---

**Golden threshold:** all C-01 – C-05 pass AND composite >= 100 (requires all essential + all recommended + at least 2/14 aspirational).
