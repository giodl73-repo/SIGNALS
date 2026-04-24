Here is the complete updated rubric:

---

# Rubric: topic-open (v2)

**Skill**: Register a new topic, define its strategy, plan the signals needed for design commit.
**Outputs**: entry in `TOPICS.md` + `simulations/{topic}/strategy.md`

**v2 change**: Added C-11 through C-15 from Round 1 excellence signals. Aspirational weight redistributed across 7 criteria (was 2). Scoring formula updated accordingly.

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

C-09/C-10 carry over from v1. **C-11 through C-15 are new in v2.**

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-09 | Strategy defines an explicit commit gate | depth | Named COMMIT GATE section with exact item names |
| C-10 | Item names follow artifact naming convention | format | `{topic}-{signal}-{date}.md` pattern throughout |
| **C-11** | **Vocabulary constraint declared before instruction body** | skill-design | Vocab rule in a standalone block preceding the instruction sequence — not buried inside column definitions |
| **C-12** | **Post-generation self-check phase present** | skill-design | Checkbox list after output generation with at least one item per essential criterion |
| **C-13** | **Self-correction loop targets C-04 by name** | skill-design | AMEND step asks a named question about priority drift (e.g., "Did any row use high/medium/low?") — not a generic review pass |
| **C-14** | **C-04 constraint framed with downstream consequence** | skill-design | Vocab rule accompanied by failure consequence explanation ("Wrong vocabulary = silent breakage / most common mistake") |
| **C-15** | **Prose rationale sequenced before signal table** | skill-design | Skill instructs model to write rationale first — so C-08 role differentiation emerges from decision context, not count enforcement |

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 7 * 10)
```

**Golden threshold**: all 5 essential pass AND composite >= 80.

---

**Key design decision in v2**: C-11 through C-15 evaluate the **skill prompt design**, not just its output. A skill variation can produce a passing output while still failing these criteria — meaning the result was achieved by luck of generation, not by design. This distinction matters for Round 2: the goal is prompts that produce reliable outputs, not prompts that got lucky once.
equence — e.g., "Wrong vocabulary = silent breakage / most common mistake" — giving the model a reason to care, not just a rule to follow |
| C-15 | Prose rationale sequenced before signal table | skill-design | The skill instructs the model to write the prose rationale section first, before constructing the signal table — so role differentiation (C-08) emerges from decision context rather than post-hoc count enforcement |

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 7 * 10)
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

---

## Criterion Notes

- **C-04** is the most common failure mode: models substitute `high/medium/low` for the canonical
  `essential/recommended/optional` vocabulary, making the strategy unusable as a commit gate.
- **C-05** catches the degenerate case where every signal is `optional` — no essential signal means
  no commit gate and the strategy provides no design readiness signal.
- **C-07** distinguishes a useful strategy from a pure mechanical table — the rationale is what
  connects the signal plan to an actual decision that needs to be made.
- **C-09** makes the implied gate explicit: a strategy that lists essential signals but never names
  the gate condition forces the consumer to infer it.
- **C-10** makes artifacts discoverable by `topic-scanner`; item names that don't follow the
  convention break glob-based coverage computation downstream.
- **C-11** addresses placement as a proxy for retention: Round 1 showed that vocabulary rules
  inside column definitions are more likely to drift in long outputs than rules in a standalone
  upfront block. Placement predicts retention.
- **C-12** and **C-13** together constitute a two-layer defense for C-04. C-12 catches drift at the
  output level via a structured checklist. C-13 tightens the check to the exact failure mode — a
  named question beats a generic review pass.
- **C-14** recognizes that consequence framing drives attention: "most common mistake / silent
  breakage" language raises model weighting on the C-04 rule more effectively than the rule alone.
  Attention follows stakes.
- **C-15** reflects that C-08 is most naturally satisfied when roles emerge from the decision
  context written before the table — prose-first sequencing makes differentiation implicit rather
  than count-enforced.
- **C-11 through C-15** evaluate the skill prompt design, not just its output. A skill variation
  can produce a passing output (all essential pass) while still failing these criteria — meaning
  the result was achieved by luck of generation, not by design.
