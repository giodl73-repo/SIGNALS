Reading the Round 4 scorecard for patterns not yet captured by C-01 through C-17:

**New signal 1 — V-01, C-17 evidence:** V-01 didn't just name prohibited synonyms — it provided a full mapping table with canonical replacements ("Reliability→Correctness, Performance→Scalability…"). C-17 only requires naming 2+ prohibited synonyms; no criterion captures the complementary move of specifying what to use instead. A model that knows "Reliability is prohibited" still has to guess what replaces it; a model given "Reliability → Correctness" has a closed substitution loop.

**New signal 2 — V-02 structure:** V-02's distinguishing feature was explicit ENTER conditions and EXIT criteria per stage. Neither C-15 (top-level gate map) nor any other criterion captures per-stage verifiable contracts. C-15 gives the model a global orientation; per-stage ENTER/EXIT gives it a local self-check before each transition.

---

## Rubric: topic-echo (topic-reflect) — v5

**17 + 2 criteria across 3 tiers. Score = essential(60) + recommended(30) + aspirational(55).**

> v5 changes: Added C-18, C-19 (aspirational) from Round 4 excellence signals. Aspirational tier expands from 45 → 55 pts (9 → 11 criteria). Golden threshold unchanged at 100.
>
> **Why these criteria:** Round 4 produced four Golden scores — V-01 and V-03 at 125, V-02 at 120, V-04 combining formal register with worked calibration. Two patterns appeared in individual variations but not universally: a synonym-to-canonical replacement mapping (V-01 only, surfaced through C-17 evidence showing arrows to canonical targets) and a per-stage ENTER/EXIT lifecycle contract (V-02 only, structurally enforcing pre/post-conditions at each stage boundary). Both are above-floor quality: no variation required them to pass golden, but each closes a compliance gap that general prohibition language and top-level gate maps leave open.

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

> **Rationale (C-15):** V-03 was the only Round 3 variation to include a pre-stage Gate Sequence Overview table listing all gate tokens and halt conditions before any stage instructions appeared. Evidence for C-09, C-10, and C-14 all noted V-03 as exhibiting the clearest execution model transparency. The structural benefit is that the model can orient to the full gate topology before entering stage-by-stage instructions, reducing mid-execution confusion about gate order and token semantics. No other Round 3 variation provided this, which is why it is aspirational rather than required.
>
> **Rationale (C-16):** V-04 was the only Round 3 variation to include worked calibration examples for Stage 4 entries. Evidence for C-03, C-04, and C-12 each named V-04 as producing "strongest calibration across all variations." Template placeholders (e.g., "[Full sentence]") instruct format; worked examples anchor the quality bar against a concrete instance. The distinction matters: a model following a template produces structurally valid but semantically thin entries; a model calibrated against a realistic example is pulled toward specificity. No other Round 3 variation used this technique.
>
> **Rationale (C-17):** V-01 and V-04 both named specific prohibited synonyms inside the vocabulary rule ("Reliability," "Performance," "Complexity," "Maintainability") in addition to a general substitution ban. V-02 and V-03 passed C-06 and C-13 using only general prohibition language. The distinction matters because a model encountering "do not substitute" may still reach for a semantically adjacent term if that term is never named as prohibited — the general rule does not close off specific high-probability errors. Naming the most common substitution targets by name converts them from implicit to explicit violations. C-17 tests whether the variation makes this move.
>
> **Rationale (C-18):** V-01 was the only Round 4 variation to pair each prohibited synonym with its canonical replacement in a mapping table (Reliability→Correctness, Performance→Scalability, Complexity→Correctness/Feasibility, Maintainability→Adoptability, Discoverability→Usability/Adoptability, Testability→Correctness/Feasibility). C-17 tests whether a variation names specific prohibited synonyms; C-18 tests whether it also closes the substitution loop by specifying what to use instead. The distinction matters: a model encountering "Reliability is prohibited" still has to infer the correct replacement and may select a different prohibited term. A model given "Reliability → Correctness" has no remaining ambiguity. V-02 and V-03 passed C-17 with named prohibitions but no canonical targets, leaving the second half of the substitution problem open. V-01 uniquely resolved it.
>
> **Rationale (C-19):** V-02 was the only Round 4 variation to structure each stage with explicit ENTER conditions and EXIT criteria. The Gate Sequence Overview (C-15) provides global gate topology; per-stage ENTER/EXIT contracts provide local execution verification — the model can confirm it has satisfied exit criteria before advancing to the next stage. This converts the prompt from a sequence of instructions into a sequence of verifiable contracts. C-11 captures that Stage 4 outputs are structurally correct prose blocks; C-19 captures a complementary discipline that applies at every stage boundary, not just Stage 4 output format. No Round 4 variation other than V-02 applied this technique, which is consistent with its aspirational classification.

---

**Golden threshold:** all C-01 – C-05 pass AND composite >= 100 (requires all essential + all recommended + at least 2/11 aspirational).
