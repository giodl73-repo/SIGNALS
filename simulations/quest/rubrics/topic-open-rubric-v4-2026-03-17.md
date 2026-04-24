Reading the Round 3 scorecard to identify what's genuinely new versus already captured by C-11–C-17.

Three patterns from the scorecard:

1. **Anti-reconstruction directive** — V-01 and V-03 both add an explicit "copy this — do not reconstruct" prohibition alongside the template. C-16 requires the template to be field-complete; it doesn't require the skill to name the failure mode the template prevents. Providing a template is not the same as prohibiting the bypass that causes regression.

2. **Downstream tool citation for structural constraints** — V-02 and V-04 anchor path and field rules to specific tools: "because topic-status and topic-scanner glob for this specific path", "because topic-status parses all five for coverage computation." C-14 covers vocab+consequence; C-17 covers causal sequencing. Neither covers structural constraints (path, schema) annotated with an exact downstream tool dependency. This is distinct: the skill tells the model *which automation breaks* if the structure is wrong.

3. **Comparative failure framing** — V-03's C-17 evidence shows both paths explicitly: "If you write the table first, roles become post-hoc labels. If you write the rationale first, roles emerge from purpose." C-17 requires a causal reason; this goes further by contrasting compliant and non-compliant paths side by side. The contrast frame makes the consequence of the wrong path concrete rather than abstract.

Three new criteria: **C-18**, **C-19**, **C-20**. Scoring formula denominator goes from 9 to 12.

---

# Rubric: topic-open (v4)

**Skill**: Register a new topic, define its strategy, plan the signals needed for design commit.
**Outputs**: entry in `TOPICS.md` + `simulations/{topic}/strategy.md`

**v4 change**: Added C-18, C-19, C-20 from Round 3 excellence signals. C-18 closes the gap between providing a field-complete template (C-16) and preventing template bypass via an explicit anti-reconstruction directive. C-19 extends the causal annotation pattern (C-14, C-17) to structural constraints — path and schema rules accompanied by the specific downstream tool that depends on them. C-20 distinguishes comparative failure framing from causal framing — contrasting both paths explicitly rather than giving a reason for only the correct one. Aspirational denominator updated from 9 to 12.

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

C-09/C-10 carry over from v1. C-11 through C-15 added in v2. C-16 and C-17 added in v3. **C-18, C-19, and C-20 are new in v4.**

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-09 | Strategy defines an explicit commit gate | depth | Named COMMIT GATE section with exact item names |
| C-10 | Item names follow artifact naming convention | format | `{topic}-{signal}-{date}.md` pattern throughout |
| C-11 | Vocabulary constraint declared before instruction body | skill-design | Vocab rule in a standalone block preceding the instruction sequence — not buried inside column definitions |
| C-12 | Post-generation self-check phase present | skill-design | Checkbox list after output generation with at least one item per essential criterion |
| C-13 | Self-correction loop targets C-04 by name | skill-design | AMEND step asks a named question about priority drift (e.g., "Did any row use high/medium/low?") — not a generic review pass |
| C-14 | C-04 constraint framed with downstream consequence | skill-design | Vocab rule accompanied by failure consequence explanation ("Wrong vocabulary = silent breakage / most common mistake") — giving the model a reason to care, not just a rule to follow |
| C-15 | Prose rationale sequenced before signal table | skill-design | Skill instructs model to write prose rationale first, before constructing the signal table — so role differentiation (C-08) emerges from decision context rather than post-hoc count enforcement |
| C-16 | TOPICS.md row template is field-complete | skill-design | Skill includes a literal row template containing all three canonical fields: topic slug, short description, and `{YYYY-MM-DD}` date placeholder — not just instructions to "add a row"; the template itself encodes every required field |
| C-17 | Sequencing instruction is causal, not positional | skill-design | Skill explains *why* the prose rationale precedes the signal table (e.g., "so owner roles emerge from decision context rather than post-hoc count enforcement") — the instruction provides a reason, not just an order |
| **C-18** | **Template accompanied by anti-reconstruction directive** | **skill-design** | Skill explicitly prohibits reconstruction of the row template — e.g., "copy this — do not reconstruct" or equivalent. C-16 requires the template to exist and be field-complete; C-18 requires the skill to name the bypass failure mode and close it by direct prohibition |
| **C-19** | **Structural constraints cite downstream tool dependency** | **skill-design** | Path and/or field schema rules are accompanied by a named downstream tool that depends on them — e.g., "topic-status and topic-scanner glob for this specific path", "topic-status parses all five fields for coverage computation". A generic consequence ("it won't work") does not pass; the specific tool must be named |
| **C-20** | **Sequencing instruction uses comparative failure framing** | **skill-design** | Sequencing instruction contrasts both paths explicitly — what happens if the model follows the correct order *and* what happens if it doesn't — side by side. C-17 requires a causal reason for the correct path; C-20 requires the non-compliant path to also be described, making the consequence concrete through contrast rather than assertion |

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 12 * 10)
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

---

**Key design decisions in v4**:

- **C-18** closes the gap between template provision and template enforcement. Having a field-complete template (C-16) is necessary but not sufficient: the most common regression is a model that acknowledges the template and then reconstructs it from memory anyway. An explicit prohibition names that failure mode and removes the implicit permission to improvise.

- **C-19** extends the causal annotation pattern established by C-14 and C-17 to cover structural constraints. C-14 attaches a consequence to the vocabulary rule; C-17 attaches a reason to the sequencing order. C-19 applies the same discipline to path and schema rules — the skill cites the specific downstream tool that depends on them, giving the model a concrete entity to protect rather than an abstract rule to follow.

- **C-20** distinguishes comparative framing from causal framing. C-17 requires the skill to say *why* the correct path is correct; C-20 requires the skill to also describe what happens on the incorrect path — side by side. The contrast frame is a stronger persuasive structure: it makes the cost of the wrong choice as vivid as the benefit of the right one, reducing the gap between knowing the rule and acting on it under generation pressure.
