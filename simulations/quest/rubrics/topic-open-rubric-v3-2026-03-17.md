Reading the scorecard carefully to identify what's genuinely new versus already captured by C-11–C-15.

Three patterns from the scorecard:

1. **Date regression** — all R2 variations dropped the `{YYYY-MM-DD}` field from the row template. C-01 tests for the field in *output*; what's missing is a skill-design criterion that the template itself is field-complete.

2. **Causal sequencing** — V-05 outperformed by saying *why* rationale precedes the table ("so owner roles emerge from decision context"), not just stating the order. C-15 tests *whether* rationale is first; it doesn't test *whether a reason is given*.

3. **Two-layer C-04 defense** — confirmed reliable, but the individual layers are already C-11 + C-13 + C-14. This is a validation of existing criteria, not a new one.

Two new criteria: **C-16** and **C-17**. Scoring formula denominator goes from 7 to 9.

---

# Rubric: topic-open (v3)

**Skill**: Register a new topic, define its strategy, plan the signals needed for design commit.
**Outputs**: entry in `TOPICS.md` + `simulations/{topic}/strategy.md`

**v3 change**: Added C-16 and C-17 from Round 2 excellence signals. C-16 addresses universal C-01 regression caused by incomplete row templates. C-17 distinguishes causal sequencing instructions from positional ones. Aspirational denominator updated from 7 to 9.

---

## Essential Criteria (60% of composite)

Must all pass. Without these the output is not useful.

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-01 | TOPICS.md entry exists | correctness | `simulations/TOPICS.md` contains a row for the new topic with at least: topic slug, short description, and start date |
| C-02 | Strategy file at correct path | correctness | Strategy written to `simulations/{topic}/strategy.md` — not to a flat path, not inline in TOPICS.md |
| C-03 | All five signal fields present | correctness | Every signal row contains all five required fields: namespace, skill, item name, owner role, priority — no field omitted or collapsed |
| C-04 | Priority vocabulary is valid | correctness | Every signal priority value is exactly one of: `essential` / `recommended` / `optional` — no substitutions (high/medium/low or other) |
| C-05 | At least one essential signal declared | coverage | Strategy contains at least one signal marked `essential` — a topic with no essential signals has no defined commit gate |

---

## Recommended Criteria (30% of composite)

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-06 | Signal set spans multiple namespaces | coverage | At least 2 distinct namespaces |
| C-07 | Strategy includes a prose rationale | depth | >= 2 sentences explaining why + what decision it informs |
| C-08 | Owner roles are differentiated | depth | At least 2 distinct owner roles |

---

## Aspirational Criteria (10% of composite)

C-09/C-10 carry over from v1. C-11 through C-15 added in v2. **C-16 and C-17 are new in v3.**

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-09 | Strategy defines an explicit commit gate | depth | Named COMMIT GATE section with exact item names |
| C-10 | Item names follow artifact naming convention | format | `{topic}-{signal}-{date}.md` pattern throughout |
| C-11 | Vocabulary constraint declared before instruction body | skill-design | Vocab rule in a standalone block preceding the instruction sequence — not buried inside column definitions |
| C-12 | Post-generation self-check phase present | skill-design | Checkbox list after output generation with at least one item per essential criterion |
| C-13 | Self-correction loop targets C-04 by name | skill-design | AMEND step asks a named question about priority drift (e.g., "Did any row use high/medium/low?") — not a generic review pass |
| C-14 | C-04 constraint framed with downstream consequence | skill-design | Vocab rule accompanied by failure consequence explanation ("Wrong vocabulary = silent breakage / most common mistake") — giving the model a reason to care, not just a rule to follow |
| C-15 | Prose rationale sequenced before signal table | skill-design | Skill instructs model to write prose rationale first, before constructing the signal table — so role differentiation (C-08) emerges from decision context rather than post-hoc count enforcement |
| **C-16** | **TOPICS.md row template is field-complete** | **skill-design** | Skill includes a literal row template containing all three canonical fields: topic slug, short description, and `{YYYY-MM-DD}` date placeholder — not just instructions to "add a row"; the template itself encodes every required field |
| **C-17** | **Sequencing instruction is causal, not positional** | **skill-design** | Skill explains *why* the prose rationale precedes the signal table (e.g., "so owner roles emerge from decision context rather than post-hoc count enforcement") — the instruction provides a reason, not just an order |

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 9 * 10)
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

---

**Key design decisions in v3**:

- **C-16** closes the most common regression path. C-01 tests whether the *output* contains a date; C-16 tests whether the *skill* makes date omission impossible by locking the template. All five R2 variations passed C-11–C-15 yet regressed on C-01 because they restated the row format from memory rather than carrying the canonical template. A field-complete literal template prevents this class of failure.

- **C-17** distinguishes reliable sequencing from lucky sequencing. C-15 passes when rationale appears before the table; C-17 additionally requires that the skill gave the model a causal reason for that order. R2 showed that "write rationale first" produces compliant output, but "write rationale first *so roles emerge from decision context*" produces rationale that is actually decision-grounded — the sequencing serves its purpose rather than just satisfying the check.
