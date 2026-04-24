---

# Variations -- program-plan (Round 1)

Five complete prompt body variations for `/program:plan`, targeting the v1 rubric (C-01 through C-09).

---

## V-01 -- Role Sequence axis

**Axis**: Role sequence -- map skills to roles before ordering stages
**Hypothesis**: Framing around *who does what* (PM/Architect/Dev/Lead) before namespace order produces more coherent phase groupings. Role-based handoff gates naturally produce artifact-referencing language (C-04, C-06) because gates become "what the next role needs to start."

**Prompt structure**: Step 1 maps skills to a role table. Step 2 groups into named phases by role. Step 3 writes evidence-state gates with at least one quantified. Step 4 adds echo. Output includes a gate rationale comment above each gate.

---

## V-02 -- Output Format axis

**Axis**: Output format -- annotated YAML skeleton with inline `# REQUIRED` / `# EXAMPLE` / `# BAD` markers
**Hypothesis**: Filling a skeleton eliminates structural errors (C-01, C-02). Inline BAD examples at the point of authoring make the execution-state gate failure concrete (C-04). The model can't forget the echo contract when it's embedded as `# REQUIRED` in the template.

**Prompt structure**: Hands the model a pre-structured YAML file with every required field annotated and every common failure shown inline. Rules section after the template. Output only the completed YAML.

---

## V-03 -- Phrasing Register axis

**Axis**: Phrasing register -- question-framing turns each stage into an evidence question
**Hypothesis**: Mapping each skill to a "question you're answering" produces gates that describe what-must-be-true rather than what-was-done (C-04, C-09), because every question has a built-in "how will we know it's answered?" answer.

**Prompt structure**: Canonical question catalog organized by phase (discovery / design / validation / simulation / research / feedback). Model selects questions, groups into stages, writes gates as "what evidence answers this question?" YAML comment above each gate marks the question it answers.

---

## V-04 -- Combined: Role Sequence + Lifecycle Emphasis

**Axis**: Role sequence x lifecycle emphasis -- four named bands (Prove It / Design It / Simulate It / Listen Ahead) with explicit role-handoff boundaries
**Hypothesis**: Named bands make the model reason about *why* phases transition, producing both better stage naming (C-06) and a deliberate evidence arc (C-09). Band-boundary gates read as handoff memos, naturally producing artifact-referencing language (C-04).

**Prompt structure**: Band diagram with owner/purpose/handoff-signal per band. Skills partitioned by band. Within-band stage creation (1--3 stages per band). Band-separator comments required in output YAML.

---

## V-05 -- Combined: Output Format + Inertia Framing

**Axis**: Output format x inertia framing -- show the BAD pattern before the GOOD template
**Hypothesis**: Contrasting an inertia plan (`all-skills` in one stage, `"all done"` gates) against a gated plan makes the model reason about what the gate *buys*, producing more specific artifact-referencing gates (C-04, C-07) and quantified gates (C-08).

**Prompt structure**: Opens with the ad-hoc failure pattern (full YAML, annotated with why it fails). Follows with the gated-plan pattern (full YAML, annotated with what makes each gate good). Then the template with a skill catalog table and a gate checklist.

---

Written to `simulations/quest/golden/program-plan-variate-R1-2026-03-15.md`.

**Coverage against v1 rubric**:

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 YAML structure | format skeleton | annotated template | end instruction | format skeleton | template + example |
| C-02 Echo contract | Step 4 explicit | `# REQUIRED` inline | closing section | `# required` comments | hard rules + example |
| C-03 Valid skill names | role table | per-namespace hints | per-question mapping | per-band catalog | explicit catalog table |
| C-04 Evidence-state gates | good/bad examples | `# EXAMPLE`/`# BAD` inline | "how will we know?" framing | handoff memo framing | BAD vs GOOD contrast |
| C-05 Namespace order | phase ordering | dependency rule comment | "keep questions in order" | band ordering | dependency rule explicit |
| C-06 Descriptive names | "not 'scout' or 'stage1'" | "descriptive label, not stage1" | names from question cluster | band-purpose naming guide | "not 'stage1' or 'scout'" |
| C-07 Plan-not-executor | header + YAML comment | header comment | implicit in question framing | header sentence | opening paragraph + YAML comment |
| C-08 Quantified gate | "At least one..." | `# HINT` with example | "Make at least one..." | "Make at least one..." | gate checklist item |
| C-09 Evidence arc | breadth-to-depth phases | namespace order rule | question sequence order | four bands breadth->depth | dependency rule + example |
