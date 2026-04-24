Here is the complete v2 rubric:

---

# Rubric — topic-plan (v2)

**Skill**: `topic:plan`
**Version**: v2 (promoted from v1 after Round 1 excellence signal extraction)
**Date**: 2026-03-14

---

## Summary

| Tier | Count | Points | Criteria |
|------|-------|--------|----------|
| Essential | 5 | 60 | Read strategy, read signals, identify delta, type proposals, confirm gate |
| Recommended | 3 | 30 | Evidence citations, before/after view, all three change types |
| Aspirational | 7 | 35 | Namespace gap detection, conflicting signal detection, typed confirmation verb, mandatory no-change rows, inline evidence brackets, anti-inventory warning, enumerated namespace audit |

**Total possible: 125 pts**

---

## Design Rationale

- **C-01/C-02** separated because fabricated signals and strategy-ignoring are independent failure modes.
- **C-03** is the core correctness gate: inventory ≠ delta.
- **C-04** enforces the three-type mandate at output time.
- **C-05** is essential because auto-applying is destructive.
- **C-09/C-10** require reasoning beyond the immediate diff — ceiling behaviors.
- **C-11–C-15** are prompt-engineering craft extracted from Round 1: they make the essential/recommended criteria *structurally self-enforcing* rather than merely instructed.

---

## Essential Criteria (60 pts total)

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-01 | **Reads strategy.md before proceeding** | essential | correctness | Output demonstrates that `simulations/{topic}/strategy.md` was read — extracts at minimum: namespaces covered, planned skills, stated rationale, acknowledged gaps. Proposals without grounding in the current strategy fail. |
| C-02 | **Reads signal artifacts before proceeding** | essential | correctness | Output demonstrates that existing signal artifacts under `simulations/{topic}/` were read — globs the directory, identifies artifacts by namespace/skill/date, uses their findings as input. Fabricated or assumed signal content fails. |
| C-03 | **Identifies delta, not inventory** | essential | correctness | Output explicitly names what signals revealed that the strategy did not anticipate — not just what signals exist. A plain inventory without naming the gap fails. |
| C-04 | **Proposes typed changes** | essential | correctness | Each proposed change is typed as addition, removal, or re-prioritization. Untyped observations without actionable proposals fail. |
| C-05 | **Requires user confirmation before writing** | essential | behavior | Output presents proposals and waits for user approval before modifying `strategy.md`. Auto-applying or omitting the gate fails. |

---

## Recommended Criteria (30 pts total)

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-06 | **Cites signal evidence per change** | recommended | depth | Each proposed change is linked to at least one specific signal artifact that motivated it. |
| C-07 | **Before/after strategy summary** | recommended | format | Output shows a diff-style summary of how the strategy would change — not just prose description. |
| C-08 | **Addresses all three change types** | recommended | coverage | Output considers additions *and* removals *and* re-prioritizations — even if the conclusion is "no changes needed" in a category. |

---

## Aspirational Criteria (35 pts total)

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-09 | **Detects namespace coverage gaps** | aspirational | depth | Identifies which of the 9 namespaces have thin/missing coverage relative to the topic's current stage. Flat count without stage-relative framing is a partial pass. |
| C-10 | **Surfaces conflicting signals** | aspirational | depth | Names opposing signals and recommends how the revised strategy should handle the conflict. Silently ignored conflicts fail. |
| C-11 | **Uses a typed confirmation verb in the gate** | aspirational | behavior | The gate names a specific verb — e.g., "Reply 'apply' to confirm" — not a vague "let me know." A named verb closes the rationalization path for early application. |
| C-12 | **Requires explicit no-change rows per change type** | aspirational | coverage | Each of ADD / REMOVE / REPRIORITIZE gets an explicit row even when empty — e.g., "REMOVE: No changes." Omitting a category is a coverage failure mode; an explicit no-change declaration proves the type was considered. |
| C-13 | **Attaches inline evidence brackets in the before/after diff** | aspirational | format | Each changed item in the diff carries an inline bracket — e.g., `[+stakeholders: signal S3 showed missing exec alignment]`. Evidence in a separate section requires cross-referencing; inline brackets make confirmation frictionless. |
| C-14 | **Embeds anti-inventory warning at the delta step** | aspirational | correctness | At the delta step, output names the failure mode it is guarding against — e.g., "A plain inventory of signals is not the delta." Naming the anti-pattern at the point of execution makes the criterion self-enforcing. |
| C-15 | **Enumerates all 9 namespaces by name in the gap audit** | aspirational | coverage | The gap audit lists all 9 namespaces explicitly rather than using an open-ended "check for gaps" instruction. An enumerated list makes omission structurally visible; an unbounded instruction is easy to skip silently. |

---

## Scoring Formula

- **Essential** (C-01–C-05): 60 pts. Any essential failure caps score below passing.
- **Recommended** (C-06–C-08): 30 pts. 10 pts each.
- **Aspirational** (C-09–C-15): 35 pts. 5 pts each.
- **Composite**: `(essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/7 * 35)`
- **Golden threshold**: all essential pass + composite ≥ 80.

---

## Version History

| Version | Change |
|---------|--------|
| v1 | Initial — 5 essential, 3 recommended, 2 aspirational (100 pts total) |
| v2 | Added C-11–C-15 from Round 1 V-01 excellence signals; aspirational pool → 35 pts (125 pts total); composite formula updated |

---

**Key structural changes from v1:**

The 5 new aspirational criteria (C-11–C-15) operationalize a meta-principle from the Round 1 scorecard: the best variations don't just satisfy the rubric criteria, they *embed the criteria as guards within the prompt itself*. C-14 (anti-inventory warning) and C-15 (enumerated namespace list) are the most transferable — they apply to nearly any skill that has a "check for X" step.
tly names the failure mode it is guarding against — e.g., "A plain inventory of signals is not the delta." Naming the anti-pattern at the point of execution makes the criterion self-enforcing rather than just instructed. |
| C-15 | **Enumerates all 9 namespaces by name in the gap audit** | aspirational | coverage | The namespace gap audit lists all 9 namespaces explicitly (scout, draft, review, flow, trace, prove, listen, program, topic) rather than using an open-ended "check for gaps" instruction. An enumerated list makes omission structurally visible; an unbounded instruction is easy to skip silently. |

---

## Scoring Formula

- **Essential** (C-01–C-05): 60 pts total. All five must pass; any essential failure caps the score below passing regardless of recommended or aspirational performance.
- **Recommended** (C-06–C-08): 30 pts total. Each criterion contributes 10 pts equally.
- **Aspirational** (C-09–C-15): 35 pts total. Each criterion contributes 5 pts equally.
- **Composite**: `(essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/7 * 35)`
- **Golden threshold**: all essential pass + composite ≥ 80.

---

## Version History

| Version | Change |
|---------|--------|
| v1 | Initial rubric — 5 essential, 3 recommended, 2 aspirational (100 pts total) |
| v2 | Added C-11–C-15 from Round 1 excellence signals — 5 new aspirational criteria extracted from V-01 patterns; aspirational pool expanded to 35 pts (125 pts total); composite formula updated |
