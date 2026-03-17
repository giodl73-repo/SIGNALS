Written to `simulations/quest/golden/prove-topic-variate-R1-2026-03-15.md`.

---

## prove-topic R1 — Five Variations

---

### V-01 — Role Sequence: Scout-First, Hypothesis-Gated Entry

**Axis**: Role sequence — scout loading is a named STAGE 0 with an explicit gate (GATE S) before hypothesis formation. The hypothesis cannot be written until the scout record table is on file.

**Hypothesis**: Forcing scout load as an explicit pre-stage with a named gate increases C-02 grounding quality because the model commits to named findings before writing the claim, rather than referencing them retrospectively.

**What it looks like**: 6 sections (STAGE 0 through STAGE 5 + Campaign Completion Check). GATE S separates scout load from hypothesis formation. Scout anchor field is required in hypothesis frontmatter.

---

### V-02 — Output Format: Scorecard Rows + Tabular Artifact Manifest

**Axis**: Output format — the campaign opens with an Artifact Manifest table that the model fills row by row. Each stage must mark `[X]` and write a Verdict token before the next stage begins. Completion is visible as a filled table, not inferred from prose.

**Hypothesis**: Tabular stage gates reduce silent-skip failures (C-01/C-03) because omission is visible as a blank cell — structurally distinct from absent prose.

**What it looks like**: Manifest table at the top, each stage ends with an explicit "update row N" instruction and a Verdict token value, final check references the manifest.

---

### V-03 — Lifecycle Emphasis: Phase Transitions as First-Class Structure

**Axis**: Lifecycle emphasis — four named phase transitions (LOAD → HYPOTHESIZE → GATHER → SYNTHESIZE → DONE) replace five numbered stage headers. Each transition has an explicit forward condition that must be met before crossing. Stages are sub-units of phases.

**Hypothesis**: Named forward conditions on phase transitions reduce skip risk more than numbered stages because the model must satisfy a stated condition (not merely count sections) to advance.

**What it looks like**: Transition headers are the primary structure. GATHER contains three sub-stages (A/B/C) under one transition gate. Forward condition checkboxes appear at each transition, not throughout.

---

### V-04 — Combined: Conversational Register + Prominent Inertia Framing

**Axes**: Phrasing register (direct second-person imperative, brief headers) + inertia framing elevated to campaign level. "Name the status quo first" is the opening section. Every stage explicitly asks whether evidence tests against the status quo comparator.

**Hypothesis**: Campaign-level inertia framing reduces confidence inflation (C-09) more than synthesize-level framing because the status-quo comparator is named as the first act and referenced at every evidence stage, not introduced only at synthesis.

**What it looks like**: Opens with "Name the status quo first." Each stage has a status-quo check field. The ceiling table uses "No status-quo test / Status-quo tested" column headers instead of "Inertia absent/present." Stage closings are conversational ("Say 'Stage N done'").

---

### V-05 — Combined: Prose-Forward Format + Narrative Stage Chapters

**Axes**: Output format (prose-primary, no standalone checkbox lists or tables) + lifecycle emphasis (stages as narrative chapters, transitions via paragraph break). Embedded structure appears within paragraphs, not as cells or checkboxes.

**Hypothesis**: Prose-forward stages produce more coherent synthesis reasoning because running text requires the model to hold prior stage context continuously, whereas discrete table cells enable context fragmentation.

**What it looks like**: No checkbox gates. Each stage is a narrative chapter with prose instructions. Signal inventories are "prose-embedded enumerations." The ceiling derivation is written as a paragraph plus five inline ceiling values. Section format in synthesize is "prose paragraphs under named headers — no bullets, no standalone tables."

---

### Rubric Coverage Summary

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 all five execute | Stage 0-5 + completion check | Manifest 5-row structure | 3 sub-stages under GATHER gate | 5 numbered "Say done" confirmations | 5 named chapters + closing list |
| C-02 hypothesis grounded in scout | GATE S mandatory | Scout Load section before Stage 1 | LOAD→HYPOTHESIZE forward condition | "Load scout signals" then anchor field | Opening paragraph + anchor field |
| C-03 artifact per stage | Confirm + write after each | Manifest row [X] before advancing | Write + [X] at each sub-stage | "Say Stage N done" confirm | "confirming it exists" per stage |
| C-04 synthesis terminal + complete | STAGE 5 last, 7 sections | Row 5 fills last | SYNTHESIZE→DONE transition | Stage 5 is last "Campaign complete" | Closing lists 5 paths, synthesis last |
| C-05 topic prefix consistent | `{topic}-` in every path | Manifest paths all `{topic}-` | Named at opening | Named at opening | Named at opening |
| C-07 scout handoff explicit | Scout anchor field + slug | Scout record table | LOAD phase + anchor in HYPOTHESIZE | Scout anchor field | Opening summary paragraph |
| C-08 synthesis ready_for_topic_story | Handoff section + frontmatter | Row 5 verdict + Handoff section | Handoff section in SYNTHESIZE | Handoff section | Handoff section |
| C-09 thin evidence propagates | Stage 4 thin-signal check | Stage 4 thin-signal flag | Sub-stage C thin-signal paragraph | Stage 4 Warning + effect | Stage 4 explicit paragraph required |
