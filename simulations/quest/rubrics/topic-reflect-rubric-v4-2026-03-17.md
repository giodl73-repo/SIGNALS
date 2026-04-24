Reading the scorecard evidence across V-01 through V-04, three patterns emerged as distinct excellence signals not captured by any existing criterion:

1. **V-03**: Introduced a top-level "Gate Sequence Overview" table enumerating all gates, tokens, and halt conditions *before* Stage 1 — structural navigation that no other variation provided.
2. **V-04**: Included filled-in worked examples for Stage 4 entries (not just templates), which evidence for C-03, C-04, and C-12 all called "strongest calibration across all variations."
3. **V-01 + V-04**: Named specific prohibited synonyms ("Reliability," "Performance," "Complexity," "Maintainability") inside the vocabulary rule — not just "all other names prohibited" but explicit call-outs of the highest-probability substitution errors.

---

## Rubric: topic-echo (topic-reflect) — v4

**17 criteria across 3 tiers. Score = essential(60) + recommended(30) + aspirational(45).**

> v4 changes: Added C-15, C-16, C-17 (aspirational) from Round 3 excellence signals. Aspirational tier expands from 30 → 45 pts (6 → 9 criteria). Golden threshold unchanged at 100.
>
> **Why these criteria:** Round 3 produced four perfect 120/120 scores — discrimination is now exhausted at all 14 v3 criteria. Three new criteria target structural innovations that appeared in individual variations but not universally: a pre-stage gate map (V-03 only), worked calibration examples (V-04 only), and named synonym exclusions in the vocabulary rule (V-01 and V-04). All three represent above-floor quality — no variation required them to pass — but each measurably increases model compliance probability for the criteria they reinforce.

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

> **Rationale (C-15):** V-03 was the only Round 3 variation to include a pre-stage Gate Sequence Overview table listing all gate tokens and halt conditions before any stage instructions appeared. Evidence for C-09, C-10, and C-14 all noted V-03 as exhibiting the clearest execution model transparency. The structural benefit is that the model can orient to the full gate topology before entering stage-by-stage instructions, reducing mid-execution confusion about gate order and token semantics. No other Round 3 variation provided this, which is why it is aspirational rather than required.
>
> **Rationale (C-16):** V-04 was the only Round 3 variation to include worked calibration examples for Stage 4 entries. Evidence for C-03, C-04, and C-12 each named V-04 as producing "strongest calibration across all variations." Template placeholders (e.g., "[Full sentence]") instruct format; worked examples anchor the quality bar against a concrete instance. The distinction matters: a model following a template produces structurally valid but semantically thin entries; a model calibrated against a realistic example is pulled toward specificity. No other Round 3 variation used this technique.
>
> **Rationale (C-17):** V-01 and V-04 both named specific prohibited synonyms inside the vocabulary rule ("Reliability," "Performance," "Complexity," "Maintainability") in addition to a general substitution ban. V-02 and V-03 passed C-06 and C-13 using only general prohibition language. The distinction matters because a model encountering "do not substitute" may still reach for a semantically adjacent term if that term is never named as prohibited — the general rule does not close off specific high-probability errors. Naming the most common substitution targets by name converts them from implicit to explicit violations. C-17 tests whether the variation makes this move.

---

**Golden threshold:** all C-01 – C-05 pass AND composite >= 100 (requires all essential + all recommended + at least 2/9 aspirational).
