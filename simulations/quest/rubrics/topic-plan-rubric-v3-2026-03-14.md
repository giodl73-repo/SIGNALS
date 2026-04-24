Written to `simulations/quest/rubrics/topic-plan-rubric-v3-2026-03-14.md`. Here is the complete v3 rubric:

---

# Rubric -- topic-plan (v3)

**Skill**: `topic:plan`
**Version**: v3 (promoted from v2 after Round 2 excellence signal extraction)
**Date**: 2026-03-14

---

## Summary

| Tier | Count | Points | Criteria |
|------|-------|--------|----------|
| Essential | 5 | 60 | Read strategy, read signals, identify delta, type proposals, confirm gate |
| Recommended | 3 | 30 | Evidence citations, before/after view, all three change types |
| Aspirational | 10 | 50 | Namespace gap detection, conflicting signal detection, typed confirmation verb, mandatory no-change rows, inline evidence brackets, anti-inventory warning, enumerated namespace audit, two-level traceability chain, explicit no-conflicts declaration, structured delta format |

**Total possible: 140 pts**

---

## Design Rationale

- **C-01/C-02** separated because fabricated signals and strategy-ignoring are independent failure modes.
- **C-03** is the core correctness gate: inventory != delta.
- **C-04** enforces the three-type mandate at output time.
- **C-05** is essential because auto-applying is destructive.
- **C-09/C-10** require reasoning beyond the immediate diff -- ceiling behaviors.
- **C-11--C-15** are prompt-engineering craft extracted from Round 1: they make the essential/recommended criteria *structurally self-enforcing* rather than merely instructed.
- **C-16** closes the gap in C-06: single-hop citation (proposal -> artifact) leaves the causal reasoning implicit; the two-level chain (proposal -> delta -> artifact) makes it auditable without re-reading the delta section.
- **C-17** is the null-case complement to C-10: C-10 handles the positive case (name conflicts); C-17 requires an explicit declaration when no conflicts exist -- parallel to C-12's no-change rows for proposals. Omitting the section is indistinguishable from skipping the audit.
- **C-18** is the structural complement to C-03/C-14: mandating "Strategy assumed [X] / Signal revealed [Y]" per finding makes the assumption-vs-signal distinction self-enforcing and makes fabricated deltas visible -- a fabrication has no "Strategy assumed" anchor it can honestly supply.

---

## Essential Criteria (60 pts total)

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-01 | **Reads strategy.md before proceeding** | essential | correctness | Output demonstrates that `simulations/{topic}/strategy.md` was read -- extracts at minimum: namespaces covered, planned skills, stated rationale, acknowledged gaps. Proposals without grounding in the current strategy fail. |
| C-02 | **Reads signal artifacts before proceeding** | essential | correctness | Output demonstrates that existing signal artifacts under `simulations/{topic}/` were read -- globs the directory, identifies artifacts by namespace/skill/date, uses their findings as input. Fabricated or assumed signal content fails. |
| C-03 | **Identifies delta, not inventory** | essential | correctness | Output explicitly names what signals revealed that the strategy did not anticipate -- not just what signals exist. A plain inventory without naming the gap fails. |
| C-04 | **Proposes typed changes** | essential | correctness | Each proposed change is typed as addition, removal, or re-prioritization. Untyped observations without actionable proposals fail. |
| C-05 | **Requires user confirmation before writing** | essential | behavior | Output presents proposals and waits for user approval before modifying `strategy.md`. Auto-applying or omitting the gate fails. |

---

## Recommended Criteria (30 pts total)

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-06 | **Cites signal evidence per change** | recommended | depth | Each proposed change is linked to at least one specific signal artifact that motivated it. |
| C-07 | **Before/after strategy summary** | recommended | format | Output shows a diff-style summary of how the strategy would change -- not just prose description. |
| C-08 | **Addresses all three change types** | recommended | coverage | Output considers additions *and* removals *and* re-prioritizations -- even if the conclusion is "no changes needed" in a category. |

---

## Aspirational Criteria (50 pts total)

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-09 | **Detects namespace coverage gaps** | aspirational | depth | Identifies which of the 9 namespaces have thin/missing coverage relative to the topic's current stage. Flat count without stage-relative framing is a partial pass. |
| C-10 | **Surfaces conflicting signals** | aspirational | depth | Names opposing signals and recommends how the revised strategy should handle the conflict. Silently ignored conflicts fail. |
| C-11 | **Uses a typed confirmation verb in the gate** | aspirational | behavior | The gate names a specific verb -- e.g., "Reply 'apply' to confirm" -- not a vague "let me know." A named verb closes the rationalization path for early application. |
| C-12 | **Requires explicit no-change rows per change type** | aspirational | coverage | Each of ADD / REMOVE / REPRIORITIZE gets an explicit row even when empty -- e.g., "REMOVE: No changes." Omitting a category is a coverage failure mode; an explicit no-change declaration proves the type was considered. |
| C-13 | **Attaches inline evidence brackets in the before/after diff** | aspirational | format | Each changed item in the diff carries an inline bracket -- e.g., `[+stakeholders: signal S3 showed missing exec alignment]`. Evidence in a separate section requires cross-referencing; inline brackets make confirmation frictionless. |
| C-14 | **Embeds anti-inventory warning at the delta step** | aspirational | correctness | At the delta step, output names the failure mode it is guarding against -- e.g., "A plain inventory of signals is not the delta." Naming the anti-pattern at the point of execution makes the criterion self-enforcing. |
| C-15 | **Enumerates all 9 namespaces by name in the gap audit** | aspirational | coverage | The gap audit lists all 9 namespaces explicitly rather than using an open-ended "check for gaps" instruction. An enumerated list makes omission structurally visible; an unbounded instruction is easy to skip silently. |
| C-16 | **Establishes two-level traceability chain in proposals** | aspirational | depth | Each proposal links to both its motivating delta finding AND its source artifact (proposal -> delta -> artifact). Single-hop citation (proposal -> artifact only) leaves the causal reasoning implicit; the two-level chain makes the path auditable without re-reading the delta section. A table with separate "Delta Row" and "Evidence Artifact" columns is the reference implementation. |
| C-17 | **Declares absence explicitly at the conflict audit** | aspirational | coverage | If no conflicting signals are found, outputs a single explicit "No conflicts found" row or statement rather than omitting the conflict section. Omitting the section is indistinguishable from skipping the audit; an explicit null result proves the audit ran. Parallel to C-12's no-change rows for proposals -- absence must be declared, not silently omitted. |
| C-18 | **Mandates structured delta format per finding** | aspirational | correctness | The delta step requires each finding in the form "Strategy assumed [X] / Signal revealed [Y]" rather than free-form prose. The two-part format structurally enforces the assumption-vs-signal distinction. A fabricated delta is made visible because it has no "Strategy assumed" anchor it can honestly supply. A stop condition (one explicit row: "No strategy surprises found") is required when signals fully confirm the strategy. |

---

## Scoring Formula

- **Essential** (C-01--C-05): 60 pts. Any essential failure caps score below passing.
- **Recommended** (C-06--C-08): 30 pts. 10 pts each.
- **Aspirational** (C-09--C-18): 50 pts. 5 pts each.
- **Composite**: `(essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/10 * 50)`
- **Golden threshold**: all essential pass + composite >= 80.

---

## Version History

| Version | Change |
|---------|--------|
| v1 | Initial -- 5 essential, 3 recommended, 2 aspirational (100 pts total) |
| v2 | Added C-11--C-15 from Round 1 V-01 excellence signals; aspirational pool -> 35 pts (125 pts total); composite formula updated |
| v3 | Added C-16--C-18 from Round 2 V-02 excellence signals; aspirational pool -> 50 pts (140 pts total); composite formula updated |

---

**Key structural changes from v2:**

Three new aspirational criteria extracted from Round 2. All three address the *traceability and declaration* layer -- the gap between "the information is present somewhere" and "the information is structurally bound to the thing it explains":

- **C-16** (two-level chain): V-02 C-06 evidence showed proposal -> artifact is insufficient; the delta link must be explicit. Evidence that travels two hops (proposal -> delta -> artifact) is auditable; evidence that jumps directly to the artifact requires the reviewer to reconstruct the reasoning.
- **C-17** (explicit no-conflicts): V-02 C-10 evidence showed an explicit "No conflicts" row where none existed. The null case must be declared for the same reason C-12 requires explicit no-change rows -- omission is indistinguishable from skipping.
- **C-18** (structured delta format): Both V-01 and V-02 used "Strategy assumed [X] / Signal revealed [Y]" formatting. The format is not cosmetic -- it binds the claim to its falsifiability condition and adds a stop condition for the case where signals fully confirm the strategy.

---

**Three signals extracted, one meta-pattern behind them all:**

V-02 scored 125/125 in Round 2. The three new criteria capture *why* -- not by doing more, but by making the structure carry the enforcement load so the prompt doesn't have to instruct it repeatedly. C-16 makes traceability a chain property. C-17 makes the null case a first-class output. C-18 makes the delta format its own falsifiability test.
