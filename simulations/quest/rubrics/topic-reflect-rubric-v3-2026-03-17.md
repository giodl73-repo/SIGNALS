## Rubric: topic-echo (topic-reflect) — v3

**14 criteria across 3 tiers. Score = essential(60) + recommended(30) + aspirational(30).**

> v3 changes: Added C-13 and C-14 (aspirational) from Round 2 excellence signals. Aspirational tier expands from 20 → 30 pts (4 → 6 criteria). Golden threshold raised to 100.
>
> **Why these criteria:** Round 2 produced a five-way tie at 102.5/110 — discrimination is exhausted at C-03/C-04/C-11/C-12, which now pass structurally for any prose-template variation. The two new criteria target the only remaining persistent failure modes: C-06 (PARTIAL across all 8 variations tested across two rounds) and C-10 (PARTIAL across all 8 variations tested across two rounds). Both failures are framing problems, not instruction problems — closed-list vocabulary and a dual-token gate are structural fixes.

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

> **Rationale (C-13):** C-06 has produced PARTIAL across all 8 variations tested in Rounds 1 and 2. Every variation listed the canonical names as guidance; none declared them as a closed vocabulary. A model following list-as-example framing may substitute "Reliability" for "Correctness" or "Performance" for "Scalability" without violating the instructions as written. A standalone closed-list rule with explicit prohibition changes the framing from example to constraint. C-13 tests whether the variation includes this structural language.
>
> **Rationale (C-14):** C-10 has produced PARTIAL across all 8 variations tested in Rounds 1 and 2. Every variation instructed "if FLAGGED, do not publish" — a production-level prohibition the model can honor or ignore with equal linguistic ease. No variation provided a stop-execution mechanism. A COMMIT-STAGE-3-CLEAN / COMMIT-STAGE-3-FLAGGED dual-token protocol forces the model to resolve the foreknowledge question as a named decision point before Stage 4 can proceed. C-14 tests whether the variation includes this gate token pair.

---

**Golden threshold:** all C-01 – C-05 pass AND composite >= 100 (requires all essential + all recommended + at least 2/6 aspirational).
