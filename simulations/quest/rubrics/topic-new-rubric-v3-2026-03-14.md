Reading the three new patterns from the R2 scorecard:

1. **Pervasive consequence framing** — C-12 generalized: every enforced constraint should carry its downstream failure mode, not just priority vocabulary
2. **Stakeholder-risk-first sequencing** — opening with role/risk enumeration produces organically differentiated assignments and closes the loop to the rationale template
3. **Structural compression proof** — length-independence of the R1 patterns implies the underlying mechanism is structural enforcement, not prose elaboration

These become C-14, C-15, C-16.

---

# Rubric: topic-new — v3

**Skill**: `topic:new`
**Version**: v3
**Date**: 2026-03-14
**Promoted from**: v2 + R2 excellence signals

**Summary of criteria:**

- **5 Essential (C-01–C-05):** TOPICS.md entry exists, strategy at correct path, all 5 signal fields present, valid priority vocabulary, at least one essential signal
- **3 Recommended (C-06–C-08):** Multi-namespace coverage, narrative rationale, differentiated owner roles
- **8 Aspirational (C-09–C-16):** Explicit commit gate, artifact naming convention, checkbox-gate before transition, operational-consequence framing for invalid vocabulary, dedicated sections per aspiration, pervasive consequence framing across all constraints, stakeholder-risk-first opener, structural enforcement over prose elaboration

The hardest failure mode to catch is C-04 — models tend to substitute "high/medium/low" for the canonical essential/recommended/optional vocabulary. C-05 catches the degenerate case where everything is optional and there's no actual commit gate implied. **C-11–C-13 are structural excellence signals from R1**: they do not change whether a strategy is valid, but they predict whether the prompt will reliably produce valid strategies across diverse inputs. **C-14–C-16 are structural excellence signals from R2**: they represent the next tier — C-14 generalizes consequence framing beyond priority vocabulary, C-15 generates role differentiation organically rather than enforcing it as a checklist, and C-16 identifies when structure (not prose) is doing the enforcement work.

---

## Essential Criteria (60% of composite)

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-01 | TOPICS.md entry exists | artifact | `simulations/TOPICS.md` contains a row for the new topic with at least: topic name, status, and strategy path |
| C-02 | Strategy file at correct path | artifact | Strategy written to `simulations/{topic}/strategy.md` — not to a flat path, not inline in TOPICS.md |
| C-03 | All five signal fields present | correctness | Every signal row includes all five required fields: namespace, skill, item name, owner role, priority |
| C-04 | Priority values are valid | correctness | Every signal priority is one of: essential / recommended / optional — no other values present |
| C-05 | At least one essential signal planned | coverage | Strategy contains at least one signal marked essential — a topic with no essential signals has no defined commit gate |

---

## Recommended Criteria (30% of composite)

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-06 | Signal set spans multiple namespaces | coverage | Planned signals reference at least 2 distinct namespaces from: scout, draft, review, flow, trace, prove, listen, program, topic |
| C-07 | Strategy includes a narrative rationale | depth | Strategy file contains a prose section (>= 2 sentences) explaining why this topic needs investigation and what decision it informs |
| C-08 | Owner roles are differentiated | depth | At least 2 distinct owner roles appear across the planned signals (e.g., PM, engineer, designer, researcher) — signals should not all default to a single generic role |

---

## Aspirational Criteria (10% of composite)

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-09 | Strategy defines a commit gate | depth | Strategy explicitly states the minimal signal set required before design commit rather than leaving the gate implicit |
| C-10 | Signal item names follow artifact naming convention | format | All item names follow the `{topic}-{signal}-{date}.md` pattern or are expressed as parameterized templates matching that convention |
| C-11 | Prompt includes checkbox-gate before phase transition | structure | Prompt contains a pre-transition checklist that forces coverage self-verification before the model proceeds to the next phase — eliminates silent criterion omissions |
| C-12 | Invalid vocabulary framed as operational consequence | framing | Prompt states the harm of invalid priority values in terms of downstream failure ("strategy cannot be used as a commit gate") rather than as a style preference or generic warning |
| C-13 | Each aspirational criterion has a dedicated section | structure | C-09 and C-10 each appear as their own named section or heading in the prompt template — not as inline reminders or parenthetical notes |
| C-14 | Consequence framing applied pervasively | framing | Every enforced constraint in the prompt (not just priority vocabulary) carries its downstream failure mode — each rule that can be violated states what breaks if it is |
| C-15 | Prompt opens with stakeholder-risk enumeration | structure | Prompt contains a WHO IS AT RISK or equivalent section that enumerates role categories and their risk exposure before signal planning begins — role differentiation emerges from the opener rather than being imposed by a late checklist |
| C-16 | Each criterion is enforced by a structural mechanism | structure | Every criterion (essential through aspirational) is enforced by a structural element — section header, checkbox, template field, or table column — not by prose instruction alone; this is the property that makes structural compression possible |

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 8 * 10)
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

---

## Changes from v2

### Three changes from v1 → v2 (carried forward)

1. **C-11, C-12, C-13 added** — extracted from R1 new_patterns. Prompt-structure criteria: assess whether the variation was engineered to prevent failure, not just whether the output happened to pass.
2. **Aspirational denominator bumped from 2 to 5** — full 10 points requires all three structural patterns.
3. **Excellence Signals section added** — records the R1 observations that motivated each new criterion.

### Three changes from v2 → v3

1. **C-14 added (pervasive consequence framing)** — R2 V-05 demonstrated that tying every enforced constraint to its failure mode, not just priority vocabulary, produced the most robust outputs across varied inputs. C-12 addressed one constraint; C-14 generalizes the pattern to the whole prompt.

2. **C-15 added (stakeholder-risk-first opener)** — R2 V-04 showed that enumerating role categories and their risk exposure *before* signal planning begins produces organically differentiated role assignments. This is architecturally superior to enforcing role differentiation as a late checklist (C-08): the opener generates the condition C-08 tests rather than correcting for its absence.

3. **C-16 added (structural enforcement over prose)** — R2 V-03 proved all 13 v2 criteria satisfiable in ~50 lines with zero degradation. The enabling property is that each criterion is enforced by a structural mechanism, not prose. C-16 names and tests that property directly, making length-independent compliance a first-class design target rather than a post-hoc observation.

4. **Aspirational denominator bumped from 5 to 8** — full 10 points now requires all eight aspirational criteria.

---

## Excellence Signals

### R1 signals → C-11, C-12, C-13

| Pattern | Criterion | Observation |
|---------|-----------|-------------|
| Checkbox-gate before phase transition | C-11 | Variations with pre-transition checklists had zero silent criterion omissions across all five signal fields |
| Operational-consequence framing | C-12 | Tying invalid vocabulary to "strategy cannot be used as a commit gate" was more reliable than generic WARNING labels; consequence framing persisted across varied inputs |
| Dedicated sections per aspiration | C-13 | Named section headings for C-09 and C-10 ensured structural presence regardless of prompt register or length |

### R2 signals → C-14, C-15, C-16

| Pattern | Criterion | Observation |
|---------|-----------|-------------|
| Pervasive consequence framing | C-14 | V-05 applied downstream-failure framing to every constraint, including the Naming Reference; robustness generalized beyond priority vocabulary — any rule that can be violated should state what breaks |
| Stakeholder-risk-first sequencing | C-15 | V-04's WHO IS AT RISK table enumerated four role categories before signal planning began; C-08 (role differentiation) was satisfied organically rather than correctively — the opener closed the loop to the rationale template |
| Structural compression proof | C-16 | V-03 satisfied all 13 v2 criteria in ~50 lines with no degradation, proving structure is the mechanism not word count; the enabling property is that every criterion has a structural enforcer (section, checkbox, field), making this testable as a first-class criterion |
