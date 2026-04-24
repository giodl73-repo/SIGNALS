# program-plan Rubric — v8

Evaluates a `program:plan` prompt against Signal's plugin contract and evidence-quality bar.
23 aspirational criteria, 4 essential, 3 recommended. Total max: **205 pts**.

---

## Essential Criteria (structural correctness — 60 pts)

### C-01 — Valid YAML Structure
- **Weight**: essential
- **Category**: correctness
- **Text**: The output is valid, parseable YAML with `program:` as the top-level key and
  `stages:` as a list of stage objects. Each stage has at minimum a `name:` field and a
  `skills:` list. A response that is prose only, a bulleted list, or syntactically invalid
  YAML fails this criterion immediately. A plan with a `program:` key but missing `stages:`
  also fails.
- **Pass condition**: The YAML is parseable and structurally complete: `program:` top-level key,
  `stages:` list, each stage has `name:` and `skills:`. Prose plans and bulleted-list plans fail.

### C-02 — Echo Stage Contract
- **Weight**: essential
- **Category**: correctness
- **Text**: The last stage in the `stages:` list has `name: echo`, `skills: []`, and
  `auto: true`. Any plan where echo has skills listed in it, echo is missing `auto: true`, or
  echo is absent entirely fails. The echo contract is a hard requirement from plugin design.
- **Pass condition**: The final stage is named `echo`, carries an empty `skills` list, and has
  `auto: true` set. Echo in any non-terminal position, echo with any skills listed, or echo
  missing `auto: true` all fail regardless of how well the rest of the plan scores.

### C-03 — Valid Signal Skill Names Only
- **Weight**: essential
- **Category**: correctness
- **Text**: Every entry in every `skills` list is a real, namespace-qualified skill from
  Signal's 9-namespace catalog: `scout`, `draft`, `review`, `flow`, `trace`, `prove`, `listen`,
  `program`, `topic`. Valid format: `namespace:skill` (e.g., `scout:feasibility`, `flow:lifecycle`,
  `prove:interview`). Invented skill names, unrecognized namespaces, plain English phrases,
  and namespace-only entries (e.g., `scout:` alone) all fail. A plan with even one invented
  skill name fails this criterion.
- **Pass condition**: Every `skills` entry in every stage is a real, namespace-qualified skill
  from Signal's catalog. No invented names, no namespace-only entries. The echo stage's empty
  `skills: []` is correct and does not fail this criterion.

### C-04 — Evidence-State Gates Only
- **Weight**: essential
- **Category**: correctness
- **Text**: Every non-echo stage has a `gate:` field whose value describes an artifact-presence
  or evidence-state condition: what must exist, what must be true of artifacts, what signals
  must be present -- not whether skills have been run or tasks have been completed. Execution-
  state gates (`"done"`, `"complete"`, `"skills executed"`, `"proceed to next stage"`) fail this
  criterion. Evidence-state gates (`"scout:feasibility artifact present"`, `"at least 2
  review:design signals with PASS"`, `"draft:spec reviewed and approved"`) pass. The distinction
  is verifiability by artifact inspection rather than execution history.
- **Pass condition**: All non-echo stage gates describe artifact-presence or evidence-state
  conditions. Every gate must be verifiable by examining artifacts, not by checking execution
  history. A single execution-state gate fails the criterion for the entire plan.

---

## Recommended Criteria (quality bar — 30 pts)

### C-05 — Namespace Dependency Order Respected
- **Weight**: recommended
- **Category**: quality
- **Text**: Skills are sequenced to respect Signal's namespace dependency layer: `scout` skills
  precede `draft` skills, `draft:spec` must exist before `review:*` skills, `review` signals
  must precede `flow`, `trace`, `prove`, and `listen` skills. A plan that places `review:design`
  in a stage before any `draft:spec` skill has run violates C-05, because design review requires
  a spec artifact to review. The dependency order is semantic: skills that consume artifacts
  must appear after stages that produce those artifacts.
- **Pass condition**: All namespace dependencies are respected in the stage sequence. Each skill
  that consumes an artifact appears in a stage after the skill that produces that artifact.
  Adjacent or out-of-order namespaces that have no dependency relationship are permitted.

### C-06 — Descriptive Stage Names
- **Weight**: recommended
- **Category**: quality
- **Text**: Stage `name:` values describe the intent or evidence goal of the stage, not the
  namespace of the skills they contain. Names like `"Scout the competitive landscape"`,
  `"Draft the feature spec"`, `"Review design for feasibility"` pass. Names like `"scout"`,
  `"draft"`, `"review"` fail -- they repeat the namespace label without describing what the
  stage is trying to learn or produce. The echo stage is exempt (its name is fixed by contract).
- **Pass condition**: Every non-echo stage has a `name:` value that describes the stage's
  evidence goal or intent. Namespace-only names, generic labels (`"stage 1"`, `"phase A"`),
  and one-word namespace repetitions fail.

### C-07 — Plan Identity Present
- **Weight**: recommended
- **Category**: quality
- **Text**: The plan is framed as a plan artifact -- a signal-gathering roadmap authored for
  a human decision-maker -- not as a list of executor instructions. This signal can appear as
  a `strategy:` field, a `purpose:` comment, a framing paragraph, or any element that positions
  the plan as "here is how we propose to gather evidence" rather than "here is what you must
  do." The distinction between plan-as-artifact and plan-as-executor-script is the core of
  Signal's philosophy. A plan with no framing beyond the YAML stages fails C-07.
- **Pass condition**: The output contains at least one element that frames the plan as a
  signal-gathering artifact for a decision-maker: a strategy field, a purpose comment, a framing
  paragraph, or equivalent. Pure skill lists with no framing fail.

---

## Aspirational Criteria (teaching quality — 115 pts)

### C-08 — Quantified Gate Thresholds
- **Weight**: aspirational
- **Category**: depth
- **Text**: At least one gate condition includes a quantified threshold: a numeric count of
  signals, a percentage of passing reviews, or a minimum artifact count. `"at least 2 scout
  signals present"`, `"3 of 5 review criteria pass"`, `"scout:feasibility artifact with >= 4
  of 6 dimensions covered"` are all quantified. `"sufficient scout signals"`, `"enough
  evidence"`, `"scout complete"` are not. Quantification makes the gate deterministic --
  a human or automated checker can evaluate it without judgment.
- **Pass condition**: At least one non-echo gate includes a numeric threshold or quantified
  condition. A plan with zero quantified gates fails even if all gates are evidence-state gates
  (C-04 compliance alone does not satisfy C-08).
- **Partial credit**: Not applicable -- either at least one quantified gate is present or it
  is not.

### C-09 — Deliberate Evidence Arc
- **Weight**: aspirational
- **Category**: depth
- **Text**: The stage sequence reflects a deliberate evidence arc -- typically breadth-first
  discovery followed by depth-of-design, then validation, synthesis, and integration -- not
  an arbitrary or alphabetical skill grouping. The arc should be visible from the stage names
  and skill selections alone, independent of any prose explanation. A plan that groups all
  scout skills together, all review skills together, and all flow skills together in namespace
  buckets rather than evidence-phase buckets fails C-09 even if the gates are correct.
- **Pass condition**: The stage sequence reflects a recognizable evidence-gathering arc with
  at least three distinct phases (e.g., discovery, design, validation) whose order reflects
  signal-gathering logic. Namespace-bucketed plans and arbitrary orderings fail.
- **Partial credit**: Arc is present in stage-name hints or ordering rules but the prompt's
  top-level structure is flat, indexed, or otherwise does not enforce arc navigation.

### C-14 -- Deletion-Resistance Annotations on Structural Slots
- **Weight**: aspirational
- **Category**: depth
- **Text**: Every pre-positioned structural element -- particularly echo, but also any required
  section or slot -- carries explicit deletion-resistance annotations that create friction against
  omission or displacement. Deletion-resistance annotations are inline markers placed at the
  structural element itself: `# REQUIRED: ...`, `# DO NOT REMOVE`, `# DO NOT add skills here.
  DO NOT move echo before other stages.` These name what the element is and what violation looks
  like. Pre-positioning alone is insufficient: a model reading cursorily can skip or relocate an
  un-annotated pre-positioned element without encountering labeled resistance. Annotations
  convert structural placement from a suggestion into a visible constraint. Evidence from R2:
  V-03 earned C-11 PARTIAL specifically because echo was pre-positioned at template end but
  carried no `# REQUIRED` annotations -- a model filling the template without reading prose could
  still move or delete echo without structural friction. V-02 and V-04 achieved C-11 PASS via
  multi-annotation echo slots (`# REQUIRED: DO NOT add skills here. DO NOT move echo before
  other stages.`, `# REQUIRED: empty`, `# REQUIRED: must be present and true`).
- **Pass condition**: Every pre-positioned structural requirement in the output scaffold carries
  at least one explicit annotation at the element itself identifying it as required and naming
  the prohibited action. Echo with no annotations fails even if placed correctly in the template.
- **Partial credit**: Some structural slots carry deletion-resistance annotations but at least
  one required structural element (e.g., echo) is pre-positioned without annotation.

### C-10 -- Failure-Mode Contrast Pair
- **Weight**: aspirational
- **Category**: depth
- **Text**: The prompt includes at least one explicit BAD/GOOD or FAIL/PASS contrast pair
  targeting an essential criterion (C-01 through C-04). The contrast must show a wrong form
  alongside its correct replacement -- not just describe what is wrong, but show it in
  juxtaposition. A contrast pair targeting C-04 would show an execution-state gate (`# BAD:
  "done"`) alongside an evidence-state gate (`# GOOD: "scout:feasibility artifact present"`).
  This provides a model with a concrete reference for the wrong shape at the moment it is
  generating that field.
- **Pass condition**: At least one BAD/GOOD or FAIL/PASS contrast pair for an essential
  criterion is present in the output, with both the wrong form and the correct form shown.
  Contrast pairs that target only recommended or aspirational criteria do not satisfy C-10.
- **Partial credit**: Not applicable -- either at least one essential-criterion contrast pair
  is present or it is not.

### C-11 -- Structural Enforcement of Requirements
- **Weight**: aspirational
- **Category**: depth
- **Text**: At least one essential requirement (C-01 through C-04) is enforced structurally
  in the output scaffold, not just stated in prose rules. Structural enforcement means the
  scaffold itself makes the correct form the default and the wrong form requires active
  deviation. Examples: echo pre-positioned at the end of the YAML template (C-02 structural
  enforcement), namespace ordering enforced by zone section headers (C-05), `gate:` field
  pre-populated with an artifact-state placeholder (C-04). A prompt that only lists rules
  without embedding them in the scaffold relies entirely on the model reading and retaining
  prose rules -- structural enforcement provides a model that skims prose with a second path
  to compliance.
- **Pass condition**: At least one essential requirement is embedded structurally in the
  output scaffold -- not merely stated in prose. The scaffold must make compliance the path
  of least resistance for that requirement.
- **Partial credit**: Structural enforcement is present for some but not all essential
  criteria, or structural elements exist but are advisory (not default-state).

### C-12 -- Dual-Anchor Reinforcement
- **Weight**: aspirational
- **Category**: depth
- **Text**: Each essential criterion (C-01 through C-04) has at least two independent
  teaching anchors in the prompt -- two different mechanisms that each independently reinforce
  the requirement. Two anchors might be: a prose rule statement (anchor 1) plus a YAML template
  placeholder that embeds the requirement (anchor 2). Or: a prose rule (anchor 1) plus a BAD
  YAML block that shows the violation (anchor 2). The key property is independence: if a model
  misses one anchor, the other alone is sufficient to teach the criterion. A prompt with a
  single comprehensive prose section that covers C-01 through C-04 provides one anchor for each
  criterion regardless of length.
- **Pass condition**: All four essential criteria each have at least two independent anchors.
  At minimum: one structural/template anchor and one prose or error-artifact anchor per
  essential criterion.
- **Partial credit**: Dual anchoring covers at least 2 of the 4 essential criteria, but not all.

### C-13 -- Arc as Structural Spine
- **Weight**: aspirational
- **Category**: depth
- **Text**: The evidence arc (C-09) is expressed as the primary structural division of the
  prompt -- the top-level headers, zone delimiters, or section markers ARE the arc phases.
  This means that the arc is not described in a prose paragraph and then presented as a flat
  YAML template; the arc phases ARE the template structure. A prompt with `## Discovery Phase`,
  `## Design Phase`, `## Validation Phase` as major structural headers, each containing the
  corresponding YAML zone template, makes the arc impossible to miss because it IS the document
  structure. The distinction from C-09: C-09 asks whether the arc is present; C-13 asks whether
  the arc IS the structure.
- **Pass condition**: The evidence arc phases are the primary structural headers or zone
  delimiters of the prompt -- the document navigates arc phases as structural divisions, not as
  a flat YAML list with arc described in prose.
- **Partial credit**: Arc is present in stage-name hints or ordering rules but the prompt's
  top-level structure is flat, indexed, or otherwise does not enforce arc navigation.

### C-15 -- Plan-Level YAML Error Artifact
- **Weight**: aspirational
- **Category**: depth
- **Text**: The prompt includes a complete, multi-field YAML block explicitly labeled as a
  wrong example -- a full plan-level BAD YAML artifact showing structural failure across multiple
  fields -- not just a single inline gate comment. This provides a second anchor for C-01 (YAML
  structural validity) because inline gate-level `# BAD` comments target gate correctness (C-04),
  not structural correctness (C-01). Without a plan-level error block, C-01 has only one anchor
  (the template), and C-12 (dual-anchor) must be PARTIAL for that reason. A plan-level BAD YAML
  artifact shows what a wrong program structure looks like -- e.g., execution-state gates across
  all stages, missing `auto: true`, flat stage design -- as a complete parseable (but semantically
  wrong) YAML document. Evidence from R2: V-04's `# BAD: flat plan` YAML block with
  `gate: "all done"` across multiple stages was the sole R2 implementation achieving C-12 full
  PASS; it provided the second anchor for C-01 that all other variates (template-only or
  inline-comment only) lacked. V-01, V-02, and V-03 all received C-12 PARTIAL specifically
  because C-01 had only the template as its structural anchor.
- **Pass condition**: The prompt contains at least one complete YAML block -- not an inline
  comment and not a partial snippet -- explicitly labeled as a wrong example, showing plan-level
  structural failure or semantic anti-pattern across multiple fields. The block must be large
  enough (at least 2 stages with wrong gates, or structural key violations) to demonstrate
  plan-level error, not just field-level error.
- **Partial credit**: Not applicable -- either a plan-level YAML error block is present or it
  is not. Inline `# BAD: "done"` comments at gate positions do not count.

### C-16 -- Criterion-Referenced Error Tagging
- **Weight**: aspirational
- **Category**: depth
- **Text**: Error examples -- whether inline gate comments or a plan-level BAD YAML block -- are
  annotated with the specific criterion they violate: `# WRONG C-02: echo must have auto: true`,
  `# WRONG C-03: invented skill name`, `# WRONG C-04: execution-state gate`. Criterion-referenced
  tagging creates a direct semantic link from each wrong shape to the rubric criterion it
  violates, letting a model understand WHY the example is wrong, not just THAT it is wrong.
  Untagged BAD examples (C-10, C-15) show failure shape but leave the causal mapping implicit;
  tagged examples make the criterion-to-error index explicit at the point of failure. Evidence
  from R3: V-03's BAD PLAN YAML block annotated each wrong field with `# WRONG C-02`,
  `# WRONG C-03`, `# WRONG C-04`, enabling a model to cross-reference errors against requirements
  without global rule recall.
- **Pass condition**: At least one error example (inline or block) carries explicit criterion
  tags (e.g., `# WRONG C-02`, `# VIOLATES C-04`) at the wrong field or stage. Untagged contrast
  pairs (C-10) and untagged BAD YAML blocks (C-15) do not satisfy C-16. A single criterion-tagged
  wrong example satisfies the criterion regardless of how many other examples are untagged.
- **Partial credit**: Not applicable -- either at least one criterion-tagged error annotation
  is present or it is not.

### C-17 -- Per-Zone Gate Contrast
- **Weight**: aspirational
- **Category**: depth
- **Text**: Every arc zone (not just a dedicated contrast section) carries its own inline
  PASS/FAIL gate example, making gate correctness visible at each authoring decision point.
  C-10 requires at least one BAD/GOOD pair in the prompt; C-17 requires the contrast to be
  embedded per-zone so a model authoring stage N encounters the correct gate form immediately,
  without needing to navigate back to a central contrast section. Per-zone contrast removes
  the attention gap between the contrast section and the gate field being authored. Evidence
  from R3: V-01 embedded labeled `PASS:` / `FAIL:` gate examples at every arc zone header,
  producing consistent C-04 compliance across all stages -- a pattern not achievable by a
  single contrast pair whose lesson must be carried forward across the document.
- **Pass condition**: Every non-echo arc zone or stage section carries an inline gate example
  showing both a correct evidence-state gate (PASS) and an incorrect execution-state gate
  (FAIL) for that zone. A single central contrast section (C-10) with no per-zone repetition
  does not pass. Partial credit when per-zone contrast covers at least half the arc zones.
- **Partial credit**: Per-zone gate contrast is present for at least half the non-echo zones
  but not all.

### C-18 -- Wrong-to-Correct Correction Table
- **Weight**: aspirational
- **Category**: depth
- **Text**: The prompt includes a structured correction table mapping common error forms to
  their correct replacements -- wrong skill name to real skill name, execution gate to
  artifact gate, namespace-only stage name to intent label -- as a scannable lookup artifact
  distinct from inline contrast examples or a BAD YAML block. A correction table is consulted
  before generating rather than encountered during error; it enables active avoidance rather
  than passive pattern-matching from embedded examples. This complements C-10 (contrast pair)
  and C-15 (plan-level YAML error block) by providing a reference format rather than an
  illustration format. Evidence from R3: V-03 included a wrong-to-correct table mapping
  invented skill names to valid catalog entries and execution-state gate strings to their
  artifact-referencing equivalents, giving a model an explicit lookup before each field
  rather than relying on inference from scattered BAD/GOOD pairs.
- **Pass condition**: The prompt contains at least one table (markdown table, two-column list,
  or labeled mapping block) explicitly mapping wrong forms to correct forms for at least one
  essential criterion (C-01 through C-04). The table must cover at least 3 wrong-to-correct
  pairs to demonstrate coverage depth. A single inline `# BAD: X  # GOOD: Y` comment does not
  satisfy this criterion.
- **Partial credit**: Not applicable -- either a correction table with >= 3 pairs is present
  or it is not.

### C-19 -- Cross-Tier Error Coverage
- **Weight**: aspirational
- **Category**: depth
- **Text**: Error artifacts -- BAD YAML block (C-15), criterion-tagged errors (C-16), or
  correction table (C-18) -- cover errors from BOTH the essential tier (C-01 through C-04)
  AND at least one recommended criterion (C-05 through C-07). Essential-only error coverage
  teaches the model to avoid structural failures but leaves recommended errors (wrong stage
  names, out-of-order namespaces, missing plan identity) unconstrained at authoring time. Cross-
  tier coverage closes that gap by making the wrong shapes for recommended criteria equally
  visible. Evidence from R4: V-01's BAD PLAN block tagged `# WRONG C-05` (dependency order)
  and `# WRONG C-06` (stage name) alongside essential-tier tags, extending criterion-tagged
  error teaching from essentials to recommended criteria in a single artifact; V-03's correction
  table included 2 C-06 pairs (namespace-label stage names mapped to intent-label stage names)
  alongside 9 essential-tier pairs.
- **Pass condition**: At least one error artifact (BAD YAML block, criterion-tagged inline
  error, or correction table) contains at least one entry explicitly targeting a recommended
  criterion (C-05, C-06, or C-07) alongside essential-criterion entries. Essential-only coverage,
  however comprehensive, does not pass.
- **Partial credit**: Not applicable -- cross-tier coverage is either present in at least one
  artifact or it is not.

### C-20 -- Per-Zone Dependency Constraint Reminder
- **Weight**: aspirational
- **Category**: depth
- **Text**: Every arc zone that depends on artifacts from a prior zone carries an inline
  dependency constraint reminder at the skill-list authoring position -- not just gate contrast
  (C-17) but an explicit prerequisite statement naming the required prior artifact: `"review:*
  requires draft:spec artifact from prior stage"`, `"flow:* requires review:design artifact"`,
  `"listen:* requires at least one flow or trace signal"`. These reminders fire at the moment
  the model is choosing skills for that zone, preventing dependency-order violations (C-05) at
  source rather than after-the-fact. C-05 states the ordering rule; C-20 embeds a zone-local
  check that makes out-of-order skill placement feel wrong at the point of authoring. Evidence
  from R4: V-02 placed `review:* requires draft:spec` inline at the Design zone skill-selection
  point, converting a rules-section statement into a per-zone constraint visible at the exact
  moment it matters.
- **Pass condition**: Every non-echo arc zone whose skills depend on prior-zone artifacts carries
  an inline prerequisite statement at the skill-list position naming the required artifact or
  condition. A zone with no upstream dependencies (e.g., a pure scout discovery zone) is exempt.
  Stating the dependency ordering rule once in a rules section does not satisfy this criterion.
- **Partial credit**: Dependency constraint reminders are present for at least half the
  dependency-bearing zones but not all.

### C-21 -- Correction Table Scaffold Integration
- **Weight**: aspirational
- **Category**: depth
- **Text**: YAML template fields carry explicit navigational bridges to the correction table
  at the authoring moment -- `# check correction table`, `# see correction table: stage names`,
  `# see correction table: gates` -- placed inline at every field type the correction table
  covers: skill-list fields, gate fields, and stage-name fields. C-18 requires a correction
  table to exist; C-21 requires the template to actively route the model to that table at each
  decision point, ensuring the table is consulted during generation rather than read once before
  generation begins. Without scaffold integration, a correction table risks being read at
  document start and forgotten by the time the model reaches a specific field. With scaffold
  integration, every covered field is a pointer back to the lookup. Evidence from R4: V-03
  embedded `# check correction table` at skill list placeholders, gate placeholders, and stage
  name placeholders in the YAML template, creating bidirectional coupling between the scaffold
  and the correction reference -- the table pulls the model in at document level; the template
  pushes the model back to the table at field level.
- **Pass condition**: The YAML template carries `# check correction table` (or equivalent
  navigational annotations) inline at every field type covered by the correction table: skill
  lists, gates, and stage names. C-18 must also pass (a correction table must exist). Inline
  annotations without a correction table, or a correction table without inline template
  bridges, each fail C-21 alone. Partial credit when at least one field type carries a
  navigational bridge but not all field types covered by the table do.
- **Partial credit**: Navigational bridges to the correction table are present at some but
  not all covered field types in the YAML template.

### C-22 -- Complete Recommended-Tier Error Annotation
- **Weight**: aspirational
- **Category**: depth
- **Text**: Error artifacts cover ALL THREE recommended criteria (C-05, C-06, and C-07), not
  merely "at least one" as C-19 requires. C-19 opens cross-tier error coverage; C-22 closes
  it by requiring the full recommended tier to be represented, ensuring wrong shapes for
  dependency violations (C-05), generic stage names (C-06), and executor framing (C-07) are
  each explicitly visible at authoring time. Without complete coverage, a prompt may teach
  C-05 errors but leave C-06 and C-07 errors implicit, creating an asymmetric error surface.
  Evidence from R5: V-01 tagged `# WRONG C-05` (dependency order violation), `# WRONG C-06`
  (namespace-label stage name), and `# WRONG C-07` (executor framing) in the BAD PLAN block,
  achieving the first complete recommended-tier error annotation -- teaching the error shape
  for every recommended criterion, not just a representative sample.
- **Pass condition**: At least one error artifact (BAD YAML block, criterion-tagged inline
  errors, or correction table entries) contains entries explicitly targeting each of C-05,
  C-06, and C-07. Coverage of only one or two recommended criteria does not pass. All three
  must appear in the error artifact set.
- **Partial credit**: Not applicable -- complete coverage requires all three; partial
  recommended-tier coverage satisfies C-19 but not C-22.

### C-23 -- Dual-Position Zone Dependency Reminder
- **Weight**: aspirational
- **Category**: depth
- **Text**: Dependency constraint reminders appear at BOTH the zone-header position AND the
  `skills:` placeholder line within each dependency-bearing zone -- belt-and-suspenders within
  the zone itself. C-20 requires the reminder at the skill-list position; C-23 extends that
  to require the zone header to also carry the prerequisite statement, so a model scanning
  either at the zone boundary or at the skill-selection point encounters the constraint. Zone-
  header placement catches a model who reads ahead to the zone without reaching the skill list;
  skill-list placement catches a model who skips the header. Together they close both attention
  gaps within a single zone. Evidence from R5: V-01 failed C-20 because reminders appeared
  at zone headers only (e.g., `# review:* requires draft:spec -- this zone MUST precede the
  Validation phase`) but NOT at the `skills:` placeholder line. V-02 satisfied both positions
  by carrying PREREQUISITE comments at zone headers AND `# requires: ...` annotations at every
  `skills:` placeholder, demonstrating that dual-position placement achieves the maximum zone-
  local dependency constraint density.
- **Pass condition**: Every dependency-bearing zone carries an explicit prerequisite statement
  at both the zone-header position AND the `skills:` placeholder line. Zones with no upstream
  dependencies are exempt. Single-position placement (header only or skills only) satisfies
  C-20 but not C-23.
- **Partial credit**: Dual-position reminders are present for at least half the dependency-
  bearing zones but not all.

### C-24 -- Template-Field Gate Contrast
- **Weight**: aspirational
- **Category**: depth
- **Text**: Per-zone gate contrast pairs appear as labeled YAML template fields -- `FAIL gate:`
  and `PASS gate:` as actual keys in the template skeleton at each zone -- not merely as prose
  comments adjacent to or above the gate field. C-17 requires per-zone gate contrast to be
  inline; C-24 requires it to be structural, embedded in the YAML skeleton itself so the model
  must actively replace or resolve the contrast fields during generation. When contrast is in
  comment form, a model can produce the gate field without engaging with the contrast; when
  contrast is a template field, the model encounters it as part of the skeleton it is filling.
  This converts gate contrast from optional reading into a forced authoring decision at every
  zone. Evidence from R5: V-02 embedded labeled `FAIL gate: "..."` / `PASS gate: "..."` as
  actual fields in the template skeleton at all 5 non-echo zones, achieving C-17 PASS with
  the highest structural fidelity -- not just inline notes, but YAML keys the model must
  acknowledge during template completion.
- **Pass condition**: Every non-echo arc zone in the YAML template skeleton carries both a
  `FAIL gate:` field and a `PASS gate:` field (or equivalently labeled keys) as actual template
  entries, not as comment annotations. A template where gate contrast appears only in adjacent
  prose comments or zone-header comment blocks does not pass, even if per-zone contrast is
  present (C-17). Partial credit when template-field gate contrast covers at least half the
  non-echo zones.
- **Partial credit**: Template-field gate contrast is present in the skeleton at some but not
  all non-echo zones.

### C-25 -- Gate Contrast Rationale Annotation
- **Weight**: aspirational
- **Category**: depth
- **Text**: Per-zone gate contrast pairs (C-17) or structural gate fields (C-24) carry an
  explicit `Why:` explanation alongside each FAIL and PASS verdict -- stating why the FAIL form
  violates the criterion and why the PASS form satisfies it. C-17 requires the contrast pair
  to be present; C-25 requires the reasoning to be present at each pair, converting the contrast
  from a pattern-only example into a criterion-grounded teaching artifact. Without rationale, a
  model sees correct and incorrect shapes but must infer the criterion being taught; with
  rationale, the criterion basis is stated at the point of encounter. The "Why:" element also
  distinguishes shallow execution-state failures (`"done" is wrong`) from the criterion-level
  principle (`gates must be artifact-verifiable, not execution-history-dependent`). Evidence
  from R6: V-02's zone headers carried `# FAIL gate: "..." Why: ...` / `# PASS gate: "..." Why:
  ...` annotations at all five non-echo zones -- the first variate to include per-pair rationale
  alongside per-zone contrast, raising gate contrast from shape-teaching to principle-teaching.
- **Pass condition**: Every non-echo zone with gate contrast (C-17 or C-24) carries a `Why:`
  explanation for both the FAIL and PASS examples. A zone carrying FAIL/PASS examples without
  any rationale satisfies C-17 or C-24 but not C-25. Partial credit when rationale is present
  for at least half the non-echo zones.
- **Partial credit**: Gate contrast rationale is present for at least half the non-echo zones
  but not all.

### C-26 -- Criterion-Tagged Structural Gate Values
- **Weight**: aspirational
- **Category**: depth
- **Text**: When structural gate-contrast fields are used (C-24's `FAIL gate:` / `PASS gate:`
  or equivalent template keys), each `FAIL gate:` field carries an inline criterion-reference
  tag (`# WRONG C-04`) within the field value or as an adjacent same-line comment -- combining
  C-24's structural forcing with C-16's criterion-referencing at the exact field position. C-16
  requires criterion tags somewhere in error artifacts (typically a BAD block or correction
  table); C-24 requires structural gate-contrast fields; C-26 requires the criterion tag to be
  embedded AT the structural `FAIL gate:` field itself, not only in a separate BAD block. This
  ensures a model resolving the structural field encounters both the wrong shape AND the named
  criterion in a single atomic location -- no cross-document lookup required. Evidence from R6:
  V-03 embedded `# WRONG C-04` as an inline comment on the `gate_fail:` field at each non-echo
  zone, placing the criterion tag inside the structural skeleton rather than only in the BAD
  PLAN block, achieving criterion-to-structural-field linkage without requiring global document
  recall.
- **Pass condition**: Every non-echo zone's `FAIL gate:` structural field (or equivalent)
  carries an inline criterion-reference tag (`# WRONG C-04` or equivalent) at the field
  position. C-24 must also pass (structural gate-contrast fields must exist). Criterion tags
  only in a BAD block, with no tags at structural field positions, satisfy C-16 but not C-26.
  Partial credit when criterion-tagged structural gate fields cover at least half the non-echo
  zones.
- **Partial credit**: Criterion-tagged structural gate fields are present at some but not all
  non-echo zones.

### C-27 -- Uniform Dependency Reminder Syntax
- **Weight**: aspirational
- **Category**: depth
- **Text**: All dependency constraint reminders -- across every dependency-bearing zone and
  every position (zone-header and skills-line per C-23) -- use identical syntactic form:
  `# requires: <artifact> from Zone: <name> (C-05)` or a consistently applied equivalent
  pattern. Syntactic uniformity means the reminder is scannable as a machine-readable pattern;
  a model recognizes the `# requires:` prefix as a structured signal without needing to
  semantically parse varied natural-language phrasings. Inconsistent framing -- mixing
  `# requires: draft:spec`, `# this zone MUST follow...`, and `# dependency: review:*` across
  zones -- satisfies C-20's reminder-presence requirement but not C-27's uniformity requirement,
  because each reminder must be interpreted independently rather than recognized as an instance
  of a single pattern. C-23 requires dual-position placement; C-27 requires that the
  dual-position reminders share a single syntactic form across all zones and both positions.
  Evidence from R6: V-02's C-23 PASS evidence explicitly cited "in same format" across all
  four dependent zones at both positions -- `# requires: <artifact> from Zone: <name> (C-05)`
  used uniformly; V-01's C-23 FAIL was attributed specifically to "inconsistent framing" where
  zone headers used different phrasings from skills-line reminders.
- **Pass condition**: All dependency constraint reminders across all dependency-bearing zones
  and all positions share a single syntactic template. Minor substitution within a fixed
  template (replacing `<artifact>` or `<name>` with specific values) is permitted; restructuring
  the sentence form or omitting the criterion reference tag is not. C-23 must also pass.
  Partial credit when uniform syntax holds for at least half the dependency-bearing zones.
- **Partial credit**: Uniform reminder syntax holds across at least half the dependency-bearing
  zones but not all, or syntax is uniform at one position (e.g., skills-line only) but not both.

### C-28 -- Structural Gate Target Field Co-Location
- **Weight**: aspirational
- **Category**: depth
- **Text**: When structural gate-contrast fields are used (C-24's `gate_fail:` / `gate_pass:`
  or equivalent keys), the actual authoring-target `gate:` field appears as a named sibling
  YAML key at each zone -- alongside but distinct from the teaching-only contrast fields. Without
  the `gate:` target sibling, a model resolving the template cannot distinguish from YAML
  structure alone which field is the production output and which fields are teaching examples;
  it may populate `gate_fail:` or `gate_pass:` as the actual gate, or leave the real gate
  absent. When the `gate:` sibling is present, the schema explicitly separates the two roles:
  `gate_fail:` and `gate_pass:` are contrast-only; `gate:` is what the model must fill. C-24
  requires the contrast fields to exist as YAML keys; C-28 requires the production target to
  co-locate with them as a third key, converting a two-field contrast pair into a three-field
  teaching unit where output and examples are structurally distinguished. Evidence from R7:
  V-02 and V-03 both used `gate_fail:/gate_pass:/gate:` as actual YAML sibling keys at all 5
  non-echo zones -- the first variates to make the production gate field structurally explicit
  alongside the contrast pair rather than leaving it implicit or expecting the model to replace
  the contrast fields.
- **Pass condition**: Every non-echo zone in the YAML template carries an explicit `gate:` (or
  equivalently named target) field as a sibling alongside the contrast fields (`gate_fail:` /
  `gate_pass:` or equivalent). C-24 must also pass. A template where the contrast fields appear
  without a co-located production target satisfies C-24 but not C-28. Partial credit when the
  three-field structure is present at least half the non-echo zones.
- **Partial credit**: Gate target field is co-located with contrast fields at some but not all
  non-echo zones.

### C-29 -- Correction Table Recommended-Tier Pairs
- **Weight**: aspirational
- **Category**: depth
- **Text**: The correction table (C-18) includes at least one wrong-to-correct pair for each
  of the three recommended criteria (C-05, C-06, and C-07) individually, not just essential-tier
  pairs. C-22 requires error artifacts collectively to cover all three recommended criteria; C-29
  requires the correction table specifically to carry that recommended-tier coverage, so the
  reference-format lookup -- the artifact designed for pre-generation consultation -- covers the
  full criterion spectrum rather than only structural failures. A correction table containing
  only wrong skill names, execution gates, and YAML violations satisfies C-18 but not C-29;
  a table with rows for out-of-order namespace placement (C-05), namespace-label stage names
  (C-06), and executor-framing (C-07) alongside essential-tier rows satisfies both. The
  distinction from C-22: C-22 asks whether recommended-tier errors appear anywhere in the
  prompt's error artifacts; C-29 asks whether they appear specifically in the correction table's
  lookup format, enabling a model to look them up by criterion type before authoring. Evidence
  from R7: V-02's 13-row correction table included rows for C-05 (dep order wrong-to-correct),
  C-06 (namespace-label-to-intent-label stage name), and C-07 (executor-framing-to-plan-identity),
  extending the lookup reference from structural to quality failures.
- **Pass condition**: The correction table contains at least one wrong-to-correct pair explicitly
  targeting each of C-05, C-06, and C-07. C-18 must also pass. A table covering only essential-
  tier criteria, however comprehensive, does not satisfy C-29. All three recommended criteria
  must appear as table entries.
- **Partial credit**: Not applicable -- the correction table either covers all three recommended
  criteria individually or it does not.

### C-30 -- Dep-Reminder and Correction-Bridge Independence
- **Weight**: aspirational
- **Category**: depth
- **Text**: At skills-list positions in dependency-bearing zones that satisfy C-23 (dual-position
  dep reminders), a dependency constraint reminder (`# requires: <artifact> from Zone: <name>
  (C-05)`) and a correction-table navigational bridge (`# check correction table`) are each
  present independently -- neither annotation substitutes for the other. The two annotations
  serve orthogonal purposes: the dep reminder informs prerequisite ordering (which artifacts
  must exist before skills in this zone can be chosen); the correction-table bridge enables
  skill-name and gate-value lookup (whether chosen skills or gate strings are valid). A skills
  line carrying only a correction-table bridge satisfies C-21's navigational requirement but
  fails C-20/C-23's prerequisite-constraint requirement; the bridge tells the model to verify
  skill names but says nothing about whether this zone's skills can be placed here at all. A
  skills line carrying only a dep reminder satisfies C-20/C-23 but leaves the correction-table
  lookup absent at the most error-prone authoring position. C-30 requires both annotations to
  coexist at every dependent skills-list position, closing the conflation gap where one
  annotation type displaces the other. C-21 and C-23 are both prerequisites. Evidence from R7:
  V-02's Design zone skills line carried only `# check correction table: skill names` with no
  dep reminder, earning C-20 and C-23 PARTIAL for the Design zone; V-03 carried both a dep
  reminder and a correction-table bridge independently at all 4 dep zones' skills lines,
  demonstrating that the two annotations are additive, not alternative.
- **Pass condition**: Every dependency-bearing zone's `skills:` placeholder line carries both
  an explicit prerequisite statement (naming the required prior artifact) AND a correction-table
  navigational bridge. C-21 and C-23 must both pass. A skills line with only one of the two
  annotation types fails C-30 regardless of whether it satisfies C-21 or C-23 individually.
  Partial credit when both annotations coexist at at least half the dep-bearing skills positions.
- **Partial credit**: Both annotations coexist at at least half the dependency-bearing zones'
  skills-list positions but not all.

---

## Scoring Formula

| Tier | Weight | Criteria | Points each | Max |
|------|--------|----------|-------------|-----|
| Essential | 60 pts | C-01, C-02, C-03, C-04 | 15 | 60 |
| Recommended | 30 pts | C-05, C-06, C-07 | 10 | 30 |
| Aspirational | 115 pts | C-08 through C-30 (23 criteria) | 5 | 115 |

```
composite = (essential_pass/4 * 60)
          + (recommended_pass/3 * 30)
          + (aspirational_pass/23 * 115)
```

PASS = full points, PARTIAL = half points, FAIL = 0.

**Golden threshold**: all 4 essential criteria pass **and** composite >= 80.

---

## Scoring Worksheet

```
Essential:    C-01 [ ]  C-02 [ ]  C-03 [ ]  C-04 [ ]
              Pass count: ___ / 4  ->  ___ / 4 * 60 = ___ pts  (of 60)

Recommended:  C-05 [ ]  C-06 [ ]  C-07 [ ]
              Pass count: ___ / 3  ->  ___ / 3 * 30 = ___ pts  (of 30)

Aspirational: C-08 [ ]  C-09 [ ]  C-10 [ ]  C-11 [ ]
              C-12 [ ]  C-13 [ ]  C-14 [ ]  C-15 [ ]
              C-16 [ ]  C-17 [ ]  C-18 [ ]  C-19 [ ]
              C-20 [ ]  C-21 [ ]  C-22 [ ]  C-23 [ ]
              C-24 [ ]  C-25 [ ]  C-26 [ ]  C-27 [ ]
              C-28 [ ]  C-29 [ ]  C-30 [ ]
              Pass count: ___ / 23  ->  ___ / 23 * 115 = ___ pts  (of 115)

Composite score: ___ / 205
Golden: all essential pass AND composite >= 80  ->  [ ] YES  [ ] NO
```

---

## Failure Fast-Paths

The following conditions fail scoring regardless of composite score:

- Output contains no YAML at all (prose plan or bulleted list only)
- Echo stage is absent, not last, or has any skills listed in it
- Any stage contains an invented Signal skill name not in the 9-namespace catalog
- Every non-echo gate uses execution-state language only (`"done"`, `"complete"`, `"proceed"`)

---

## Scorer Notes

- **C-01**: Check YAML validity first. If unparseable, C-01 fails. Score remaining criteria
  as best-effort but note the failure.
- **C-02**: Echo is a hard contract. Missing `auto: true`, placing echo mid-plan, or listing
  any skills in echo are all hard fails regardless of otherwise valid structure.
- **C-03**: Authority for valid skill names is the plugin-plan.md catalog (9 namespaces, ~47
  skills). Skills listed without namespace prefix fail unless the plan establishes unambiguous
  context -- prefer `namespace:skill` form.
- **C-04**: The key test: can the next-phase owner verify the gate is satisfied by looking at
  artifacts, not by asking "did we run the skills?" Gates that describe running fail; gates
  that describe what must exist pass.
- **C-05**: Dependency ordering is assessed by namespace layer (`scout -> draft -> review/prove
  -> topic`), not alphabetically. A plan with `review:design` before any `draft:spec` fails
  C-05 because design review requires a spec artifact to review.
- **C-07**: The "plan not executor" signal can be subtle (a comment, a strategy field framing)
  -- it does not require an explicit disclaimer paragraph.
- **C-10**: The contrast must target one of C-01 through C-04. A BAD/GOOD pair for a
  recommended criterion (e.g., descriptive vs generic stage names) does not satisfy C-10.
- **C-11**: The distinction is structural vs stated. Ask: "If a model followed the prompt's
  scaffold without reading the rules section, would the output still satisfy this requirement?"
  If yes, C-11 passes for that requirement.
- **C-12**: Partial credit applies when dual-anchoring covers at least 2 of the 4 essential
  criteria. Full credit requires all 4 essential criteria to have dual anchoring.
- **C-13**: The test is whether the arc is navigable as structure, not just readable as text.
  If you removed all prose from the prompt and kept only headers and YAML skeleton, would the
  arc still be visible? If yes, C-13 passes.
- **C-14**: Check each pre-positioned structural element individually. Echo is the primary
  target. A `# REQUIRED: must be last` comment at the echo slot satisfies this for echo.
  Absence of any annotation on a pre-positioned element fails for that element.
- **C-15**: Inline `# BAD: "done"` comments within a YAML skeleton are C-10 evidence (gate
  contrast), not C-15. C-15 requires a complete YAML block -- multiple fields, multiple stages
  -- that is explicitly a wrong plan, not a wrong gate.
- **C-16**: The criterion tag must name a specific criterion (e.g., `C-02`, `C-04`), not just
  a generic label (`# WRONG`, `# BAD`). A tag without a criterion reference does not satisfy
  C-16. C-10 or C-15 elements that also carry criterion tags satisfy both C-10/C-15 and C-16.
- **C-17**: Per-zone contrast is assessed per non-echo zone. A zone carrying only PASS or only
  FAIL but not both does not satisfy per-zone contrast for that zone. Count zones with both
  PASS and FAIL examples; require >= 100% for full pass, >= 50% for partial.
- **C-18**: The correction table is scanned for covered criteria (C-01 through C-04) and pair
  count (>= 3 pairs). A table that maps only one criterion's errors fails. A table with fewer
  than 3 pairs fails. Criterion-tagged inline comments (C-16) and correction tables (C-18) are
  orthogonal -- C-16 can be satisfied without C-18 and vice versa.
- **C-19**: Scan all error artifacts (BAD YAML blocks, criterion-tagged inline errors, and
  correction table entries) for recommended-criterion coverage. A single C-05/C-06/C-07 entry
  in any artifact satisfies C-19, even if most entries target essential criteria. Ambiguous
  error entries not tagged to any criterion do not count toward C-19.
- **C-20**: Assess per dependency-bearing zone. Zones that only use upstream-independent skills
  (e.g., pure `scout:*` discovery) are exempt. For dependent zones, the reminder must be at
  the skill-list authoring position, not in a prior rules section. A zone-level header comment
  counts; a prose note before the template does not.
- **C-21**: C-18 is a prerequisite -- if no correction table is present, C-21 fails regardless
  of inline annotations. Check that navigational bridges appear at each field type covered in
  the table: if the table covers stage names, gate strings, and skill names, bridges must appear
  at all three field types in the template. A table with gate entries but no `# check correction
  table` at gate template fields fails C-21 for that field type. When C-24 structural gate
  fields are present, they may substitute for correction-table bridges at gate fields only if
  the structural field itself carries a criterion tag (C-26) -- structural presence alone does
  not excuse the navigational bridge absence.
- **C-22**: Scan all error artifacts for criterion tags. All three recommended criteria (C-05,
  C-06, C-07) must each appear at least once across the artifact set. C-22 subsumes C-19: a
  prompt satisfying C-22 necessarily satisfies C-19. Score C-22 and C-19 independently; partial
  recommended coverage (one or two of three) earns C-19 but not C-22.
- **C-23**: Assess per dependency-bearing zone. Both the zone-header position and the `skills:`
  placeholder must carry an explicit prerequisite statement. A zone-header-only reminder (like
  V-01's `# review:* requires draft:spec -- this zone MUST precede the Validation phase`)
  satisfies C-20 partial but not C-23. A zone with reminder only at `skills:` (no header
  mention) also fails C-23. Partial credit when dual-position coverage holds for at least half
  the dependency-bearing zones.
- **C-24**: C-24 requires contrast as actual YAML keys (`FAIL gate:` / `PASS gate:` as
  template fields), not as comment annotations. A zone where contrast appears only as
  `# FAIL: "done"` / `# PASS: "2 scout signals present"` adjacent to the gate field satisfies
  C-17 (inline per-zone contrast) but not C-24 (template-field contrast). The test: if you
  stripped all comments from the template, would the contrast still be visible as YAML
  structure? If yes, C-24 passes for that zone. Partial credit when template-field contrast
  covers at least half the non-echo zones.
- **C-25**: Assess per non-echo zone that has gate contrast (C-17 or C-24). A zone where
  contrast appears as `# FAIL: "done"` / `# PASS: "artifact present"` with no explanation
  satisfies C-17 or C-24 but not C-25. The "Why:" must explain the criterion basis -- why the
  FAIL form fails (e.g., execution-state vs artifact-state) -- not just restate the label.
  A `Why: this is wrong` gloss without criterion-level reasoning does not satisfy C-25.
  Partial credit when rationale is present for at least half the non-echo zones.
- **C-26**: C-24 is a prerequisite -- structural gate fields must exist for C-26 to apply.
  The criterion tag must appear at the structural field position itself (e.g., `gate_fail:
  "done"  # WRONG C-04`), not only in a separate BAD block. A prompt that has C-24 structural
  fields and C-16 tags in a BAD block satisfies both C-24 and C-16 but not C-26, because the
  tag is not co-located with the structural field. Partial credit when criterion-tagged
  structural gate fields cover at least half the non-echo zones.
- **C-27**: C-23 is a prerequisite -- dual-position placement must be established. Assess
  syntactic form by checking whether all reminders across all zones and positions use the same
  sentence structure and carry the criterion tag. Substitution of artifact names and zone names
  within a fixed template is allowed. A template that uses `# requires: X from Zone: Y (C-05)`
  uniformly but drops `(C-05)` in some positions fails C-27's uniformity requirement. Partial
  credit when uniform syntax holds across at least half the dependency-bearing zones, or when
  syntax is uniform at one position (skills-line or header) but not both.
- **C-28**: C-24 is a prerequisite -- structural contrast fields must exist. Assess per non-echo
  zone: does a `gate:` (or equivalently named production-target) key appear as a sibling
  alongside `gate_fail:` / `gate_pass:`? The production-target field may carry a placeholder
  value or an instruction comment; its presence as a YAML key is what matters. A zone with only
  `gate_fail:` and `gate_pass:` satisfies C-24 but not C-28. Partial credit when the three-
  field structure is present at at least half the non-echo zones.
- **C-29**: C-18 is a prerequisite -- a correction table must exist. Scan the correction table
  for rows targeting each of C-05, C-06, and C-07. Each criterion must have at least one entry
  (wrong-form to correct-form pair). A table that covers C-05 and C-06 but not C-07 fails C-29
  even if it satisfies C-22 (if C-07 appears in a BAD block but not the table). The test is
  specifically the correction table as a format, not the artifact set collectively.
- **C-30**: C-21 and C-23 are both prerequisites. Assess per dependency-bearing zone's `skills:`
  line. Both a dep reminder (`# requires: <artifact>`) and a correction-table bridge (`# check
  correction table`) must appear. The correction-table bridge for skill names does not satisfy
  the dep reminder requirement; a dep reminder does not satisfy the correction-table bridge
  requirement. They serve different purposes and must each be present independently. A skills
  line with only one type fails C-30 for that zone. Partial credit when both annotations coexist
  at at least half the dep-bearing zones.

---

## Design Decisions

- **C-01/C-02/C-03/C-04 are essential** because a plan failing any of them is structurally
  unusable -- bad YAML cannot be consumed, missing echo violates the plugin contract, invented
  skills reference nothing real, and execution-state gates destroy the only value the plan
  provides.
- **C-05 is recommended** (not essential) because namespace ordering is about quality of
  evidence sequencing -- a plan with scout/draft/review in correct order but flow/trace slightly
  misplaced is still useful.
- **C-06/C-07 are recommended** because descriptive names and explicit plan identity improve
  readability but do not break the plan's core function.
- **C-10 is aspirational** because failure-mode contrasts are a prompt engineering technique
  -- valuable for reliability but not required for a correct plan.
- **C-11 is aspirational** because structural enforcement requires more scaffold investment.
  Prose rules produce correct plans; structural enforcement makes them reliably correct without
  requiring careful reading.
- **C-12 is aspirational** because dual anchoring is a belt-and-suspenders technique. A
  well-attentive model passes all essentials from a single clear statement; dual anchoring
  provides robustness across inattentive or abbreviated generation.
- **C-13 is aspirational** because making the arc the structural spine -- not just stating it
  -- requires a prompt design decision that goes beyond ordering skills correctly. The arc must
  govern the document structure, not just the stage sequence.
- **C-14 is aspirational** because deletion-resistance annotations require deliberate placement
  work. Pre-positioning structural elements is C-11; annotating them against deletion is C-14.
  The two together achieve the highest structural reliability.
- **C-15 is aspirational** because a full BAD YAML plan block requires more construction effort
  than inline comments. It is the only technique that provides C-01 a second anchor, enabling
  C-12 full PASS. Without it, C-12 is structurally capped at PARTIAL regardless of how well
  C-02/C-03/C-04 are dual-anchored.
- **C-16 is aspirational** because criterion-referenced tagging requires the prompt author to
  know the rubric well enough to annotate each error with its criterion number. It is the
  highest-fidelity teaching technique: the model learns not just the wrong shape but which
  requirement the wrong shape violates.
- **C-17 is aspirational** because per-zone contrast requires repetition investment. A single
  contrast pair (C-10) is cheaper; per-zone contrast is more reliable because it eliminates
  the attention gap between the contrast section and the gate being authored.
- **C-18 is aspirational** because a correction table is a reference-format complement to
  illustration-format techniques (C-10, C-15, C-16). It enables active avoidance before
  generation rather than passive pattern-matching during generation.
- **C-19 is aspirational** because cross-tier error coverage requires the prompt author to
  identify wrong shapes for recommended criteria, not just essential ones. It extends the
  teaching surface of error artifacts from structural failures to quality failures, closing the
  coverage gap between essential-tier and recommended-tier criteria.
- **C-20 is aspirational** because per-zone dependency reminders require zone-local investment
  beyond what C-05 demands. C-05 teaches the rule; C-20 embeds the rule at each decision point,
  making dependency violations feel wrong locally rather than requiring the model to carry a
  global ordering rule across the entire document.
- **C-21 is aspirational** because scaffold integration of the correction table requires
  bidirectional coupling work: the table must be built (C-18) AND the template must route to
  it at each field type it covers. The combination creates an active consultation loop -- the
  table is not just present but actively consulted at generation time.
- **C-22 is aspirational** because complete recommended-tier error annotation requires the
  prompt author to identify wrong shapes for ALL three recommended criteria, not just a
  representative one. C-19 opens the cross-tier coverage gap; C-22 closes it. The incremental
  cost of tagging all three vs. one is low; the benefit is symmetric error coverage across the
  full recommended tier.
- **C-23 is aspirational** because dual-position dependency reminders require per-zone
  investment in both structural positions. C-20 installs the rule at the skill-selection point;
  C-23 adds the zone-boundary signal, closing the attention gap for models that scan zone
  headers before reading zone content. The R5 evidence shows that header-only placement (V-01)
  fails C-20 because the skills position is the authoritative decision point; dual-position
  placement (V-02) achieves maximum zone-local constraint density.
- **C-24 is aspirational** because template-field gate contrast requires the contrast to be
  structural, not merely annotative. C-17 requires per-zone contrast; C-24 requires that
  contrast to be embedded as YAML keys the model must actively engage with during template
  completion. This is the highest-fidelity gate-teaching technique: the model cannot produce
  the gate field without encountering the contrast as part of the skeleton it is resolving.
- **C-25 is aspirational** because gate contrast rationale requires the prompt author to
  articulate the criterion principle behind each FAIL/PASS verdict, not just exhibit the
  contrast shapes. C-17 and C-24 show what the right and wrong forms look like; C-25 explains
  WHY they are right or wrong, converting contrast from pattern-teaching to principle-teaching.
  The incremental cost is a `Why:` annotation per zone; the benefit is that a model failing to
  generalize from the example still encounters the criterion basis at the contrast point.
- **C-26 is aspirational** because criterion-tagged structural gate fields require the highest
  co-location fidelity: the criterion tag must be at the structural field itself, not in a
  nearby BAD block. C-16 requires criterion tags in error artifacts; C-24 requires structural
  gate fields; C-26 requires both to coincide at the field position. This is the most compact
  teaching form -- wrong shape, structural forcing, and criterion reference all in one atomic
  location -- requiring the most deliberate placement work.
- **C-27 is aspirational** because uniform dependency reminder syntax requires syntactic
  discipline across all zones and positions, not just semantic coverage. C-23 requires dual-
  position placement; C-27 requires that the dual-position reminders share a single parseable
  syntactic form. Inconsistent paraphrasing satisfies the presence requirement but creates a
  mixed-syntax pattern that each reminder must be parsed independently. Uniform syntax makes
  the reminder pattern scannable and machine-recognizable -- a structural property of the
  document, not just a content property.
- **C-28 is aspirational** because making the production gate target explicit as a YAML sibling
  requires deliberate schema design. C-24 requires contrast fields as YAML keys; C-28 requires
  the output slot to be equally explicit, so the three-field structure (`gate_fail:`,
  `gate_pass:`, `gate:`) separates pedagogical from production at the schema level rather than
  leaving the model to infer which field to fill. The increment from C-24 is one additional
  sibling key per zone; the benefit is unambiguous authoring guidance at the field level.
- **C-29 is aspirational** because correction tables are consulted as reference artifacts before
  generation, making their content selection high-stakes. C-22 requires recommended-tier error
  coverage anywhere in the prompt; C-29 requires it specifically in the lookup format, so the
  pre-generation reference tool covers quality failures (C-05/C-06/C-07) as well as structural
  ones. Without recommended-tier correction table rows, a model checking the table before
  authoring can avoid essential-tier errors but has no lookup defense against recommended-tier
  errors.
- **C-30 is aspirational** because dep-reminder/correction-bridge independence requires the
  prompt author to recognize that two distinct annotation obligations exist at every dependent
  skills line: prerequisite ordering (C-23) and lookup navigation (C-21). The R7 evidence shows
  they can be conflated -- a bridge substituting for a reminder -- because both appear at the
  same position. C-30 closes the conflation gap by requiring both to coexist, achieving maximum
  annotation density at the highest-risk authoring position in any dependent zone.
- **Failure fast-paths** cover the four most common failure modes from the variate scoring
  rounds: no YAML, bad echo, invented skills, all-execution gates.
- **Scoring total is 205** (not 190) because the aspirational tier expanded from 20 to 23
  criteria. The golden threshold (>= 80) is unchanged and achievable with essential + partial
  recommended even with zero aspirational points.

---

## Version History

| Version | Date | Change |
|---------|------|--------|
| v1 | 2026-03-15 | Initial rubric -- 4 essential, 3 recommended, 2 aspirational (total 100 pts) |
| v2 | 2026-03-15 | Added C-10/C-11/C-12 from R1 excellence signals; aspirational 2->5 criteria, 10->25 pts; total 115 pts |
| v3 | 2026-03-15 | Added C-13/C-14/C-15 from R2 excellence signals; aspirational 5->8 criteria, 25->40 pts; total 130 pts |
| v4 | 2026-03-16 | Added C-16/C-17/C-18 from R3 excellence signals; aspirational 8->11 criteria, 40->55 pts; total 145 pts |
| v5 | 2026-03-16 | Added C-19/C-20/C-21 from R4 excellence signals; aspirational 11->14 criteria, 55->70 pts; total 160 pts |
| v6 | 2026-03-16 | Added C-22/C-23/C-24 from R5 excellence signals; aspirational 14->17 criteria, 70->85 pts; total 175 pts |
| v7 | 2026-03-16 | Added C-25/C-26/C-27 from R6 excellence signals; aspirational 17->20 criteria, 85->100 pts; total 190 pts |
| v8 | 2026-03-16 | Added C-28/C-29/C-30 from R7 excellence signals; aspirational 20->23 criteria, 100->115 pts; total 205 pts |
