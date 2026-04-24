```markdown
# Rubric: topic-open (v8)

**Skill**: Register a new topic, define its strategy, plan the signals needed for design commit.
**Outputs**: entry in `TOPICS.md` + `simulations/{topic}/strategy.md`

**v8 change**: C-31 through C-34 are promoted from Round 8 prospective signals, all confirmed
in the Round 9 base (R8 V-05 passes all four). C-31 requires Phase 5 AMEND blocks to use a
uniform `AMEND — {CONDITION NAME}` label format across all five essential criteria — no
free-form repair headers, no label variance. C-32 requires the Phase 2 GATE FAILURE block to
name exactly three things: the return phase, the repair action, and the re-run condition — "fix
and retry" does not satisfy. C-33 requires a Recovery Path column in every DEFAULTS row, making
repair paths discoverable at the point of default lookup rather than only in Phase 5. C-34 closes
a redundancy gap: DEFAULTS Recovery Path entries and Phase 5 AMEND blocks must carry independent,
non-overlapping repair procedures — the same repair instruction cannot appear in both surfaces.

C-35 through C-37 are new from Round 9 prospective signals (V-01, V-02, V-03 each pass exactly
one). C-35 extends C-32 to require exit gates at Phase 1, 3, and 4 in addition to Phase 2 — each
with a GATE FAILURE block giving return phase, repair action, and re-run condition — so gate
coverage is uniform across all four procedural phases, not concentrated at Phase 2. C-36 extends
C-12 to require Phase 5 to cover all eight criteria (C-01 through C-08, essential + recommended)
with `AMEND — {CONDITION NAME}` blocks — Phase 5 is a repair protocol for the full rubric, not
only the essential tier. C-37 adds a concrete example requirement: FIELD SCHEMA must contain a
filled-in example row using real (non-placeholder) values, and Phase 3 must follow the strategy
template with an example COMMIT GATE listing at least two exact item names — abstract templates
are accompanied by concrete anchors the model can pattern-match against.

Aspirational denominator updated from 22 to 29.

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

C-09/C-10 carry over from v1. C-11 through C-15 added in v2. C-16 and C-17 added in v3.
C-18, C-19, and C-20 added in v4. C-21, C-22, C-23, and C-24 added in v5. C-25, C-26,
and C-27 added in v6. C-28, C-29, and C-30 added in v7. C-31, C-32, C-33, and C-34
promoted from Round 8 prospective signals. **C-35, C-36, and C-37 are new in v8.**

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-09 | Strategy defines an explicit commit gate | depth | Named COMMIT GATE section with exact item names |
| C-10 | Item names follow artifact naming convention | format | `{topic}-{signal}-{date}.md` pattern throughout |
| C-11 | Vocabulary constraint declared before instruction body | skill-design | Vocab rule in a standalone block preceding the instruction sequence — not buried inside column definitions |
| C-12 | Post-generation self-check phase present | skill-design | Checkbox list after output generation with at least one item per essential criterion |
| C-13 | DEFAULTS table present | skill-design | Skill body contains a DEFAULTS table with a default value for every required field — gaps in user input have known fallback values rather than silent inference |
| C-14 | FIELD SCHEMA is explicit | skill-design | A labeled FIELD SCHEMA block defines each of the five required fields (name, allowed values or type, purpose) before the instruction body |
| C-15 | ROW TEMPLATE present | format | A ROW TEMPLATE block shows the exact TOPICS.md row format the model must produce — the template is not described in prose only |
| C-16 | Phase 1 prerequisite check present | skill-design | Phase 1 includes an explicit check for required inputs before generation begins; missing inputs trigger a named prompt-back rather than silent guessing |
| C-17 | Phase 2 GATE FAILURE block present | skill-design | The Phase 2 exit gate includes a GATE FAILURE block with explicit routing on failure — not just a pass/fail checklist with no repair path |
| C-18 | Phase 4 uses comparative framing | skill-design | Phase 4 ordering instructions use if-A / if-B framing to contrast the two paths (copy-from-defaults vs reconstruct) rather than listing both as undifferentiated steps |
| C-19 | Phase objectives are labeled | format | Each phase opens with a named purpose statement before its instruction body — the label is a brief noun phrase, not just "Phase N" |
| C-20 | Phase 2 gate covers all essential criteria | skill-design | Phase 2 gate has one check per essential criterion (C-01 through C-05) — no essential criterion is left without a gate item |
| C-21 | Gate items carry criterion codes | skill-design | Each Phase 2 gate item references the criterion it enforces via a code or semantic label (COV-NN, C-NN, or equivalent) — the enforcement link is explicit at the point of the check |
| C-22 | Each phase ends with explicit transition condition | skill-design | Each phase declares a named state that must be true before proceeding to the next phase — implicit "when done" transitions are not used |
| C-23 | Decision tables at three or more phases | skill-design | Structured decision tables present at Phase 2 and at least two other phases — not concentrated at a single phase |
| C-24 | Strategy template names all three sections | format | Phase 3 template explicitly labels the SIGNALS table section, the COMMIT GATE section, and the prose rationale section — all three are discoverable by name |
| C-25 | Gate and checklist items cite the enforcing tool | skill-design | Every exit gate item and Phase 5 checklist item names the tool that checks it — the enforcer is identified at the point of the check |
| C-26 | Ordering instructions carry inline comparative framing | skill-design | Every instruction that covers two distinct paths (copy vs reconstruct, append vs overwrite, etc.) carries its own if/if framing inline — the contrast is in the instruction body |
| C-27 | Labeled decision tables at every phase | skill-design | All five phases contain a labeled decision table — the label is visible before the table body, not only implied by context |
| C-28 | Decision table columns are uniform across all phases | skill-design | All decision tables in the skill share the same column schema (e.g., Path / Action / Consequence) — declared once in a DECISION TABLE SCHEMA block before Phase 1 and not varied per phase |
| C-29 | Tool citations specify the enforcement mechanism | skill-design | Every tool citation at a gate or checklist item names both the tool and what the tool checks (two-slot citation: tool name + enforcement contract) — the mechanism is stated, not just the enforcer |
| C-30 | Ordering instructions are self-contained | skill-design | Every ordering instruction carries its own comparative framing in the instruction body and does not delegate to "see Phase X Decision above" or any equivalent table reference |
| C-31 | Phase 5 AMEND labels are uniform | skill-design | All Phase 5 repair blocks for essential criteria use the format `AMEND — {CONDITION NAME}` — no free-form repair headers, no label format variation across criteria |
| C-32 | GATE FAILURE block is fully specified | skill-design | The Phase 2 GATE FAILURE block names exactly: the return phase, the repair action, and the re-run condition — all three elements present; "fix and retry" without routing does not pass |
| C-33 | DEFAULTS table includes Recovery Path column | skill-design | Every row in the DEFAULTS table contains a Recovery Path entry — repair paths are discoverable at the point of default lookup, not only through Phase 5 |
| C-34 | Recovery paths are non-overlapping | skill-design | DEFAULTS Recovery Path entries and Phase 5 AMEND blocks carry independent repair procedures — the same repair instruction does not appear on both surfaces; each addresses distinct failure modes |
| C-35 | Exit gates present at all procedural phases | skill-design | Phase 1 has a terminal exit gate; Phases 3 and 4 each have a return-to-repair gate; every gate includes a GATE FAILURE block naming return phase, repair action, and re-run condition — gate coverage is uniform across all four procedural phases, not concentrated at Phase 2 |
| C-36 | Phase 5 self-check covers essential and recommended criteria | skill-design | Phase 5 includes `AMEND — {CONDITION NAME}` blocks for all eight criteria (C-01 through C-08) — coverage is not limited to the five essential criteria; C-06, C-07, and C-08 each have a named AMEND block |
| C-37 | Schema and template definitions include concrete examples | skill-design | FIELD SCHEMA contains a filled-in example row with real (non-placeholder) values across all five fields; Phase 3 strategy template is followed by an example COMMIT GATE listing at least two exact item names in the `{topic}-{signal}-{date}.md` format — abstract templates are anchored by a concrete readable instance |
```
