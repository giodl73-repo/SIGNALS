# program-plan Rubric — v20

Evaluates a `program:plan` prompt against Signal's plugin contract and evidence-quality bar.
52 aspirational criteria, 4 essential, 3 recommended. Total max: **350 pts**.

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

## Aspirational Criteria (teaching quality — 235 pts)

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

### C-31 -- Complete BAD-YAML Cross-Criterion Coverage
- **Weight**: aspirational
- **Category**: depth
- **Text**: The plan-level BAD YAML block (C-15) contains at least one `# WRONG C-XX` tagged
  violation for each of the 7 criteria (C-01 through C-07) -- both essential (C-01 through C-04)
  and recommended (C-05 through C-07). C-16 requires at least one criterion-tagged error anywhere
  in the prompt; C-22 requires recommended-tier coverage across the full error artifact set; C-31
  requires the BAD PLAN block specifically to be a complete single-artifact criterion index --
  all 7 criteria each represented by at least one tagged wrong field within the single block.
  Without this, a model reading only the BAD PLAN block learns which shapes violate essential
  criteria but has no illustration of recommended-tier violations inside the concrete error
  example. When the BAD PLAN block carries all 7 criterion tags, it becomes a self-contained
  teaching index that covers every failure mode in one scannable artifact. Evidence from R8:
  V-03's BAD PLAN block carried 7 criterion-tagged violations spanning C-01 through C-07 -- the
  first variate to make the BAD PLAN block a complete criterion index rather than an
  essential-tier-only error sample.
- **Pass condition**: The plan-level BAD YAML block contains at least one `# WRONG C-XX` tag
  for each of C-01, C-02, C-03, C-04, C-05, C-06, and C-07. C-15 must also pass (the block
  must exist as a complete plan-level artifact). Criterion-tagged errors only in inline comments
  or only in the correction table do not satisfy C-31; the tags must appear within the BAD PLAN
  block itself. A block covering all 4 essential criteria but missing any recommended criterion
  satisfies C-16 and C-22 (if recommended errors appear elsewhere) but not C-31.
- **Partial credit**: Not applicable -- the BAD PLAN block either covers all 7 criteria with
  criterion tags or it does not. Partial coverage (e.g., 5 of 7) earns C-16 and possibly C-22
  but not C-31.

### C-32 -- Production Gate Field Correction Bridge
- **Weight**: aspirational
- **Category**: depth
- **Text**: When the three-field gate structure (C-28) is present, the production `gate:`
  sibling field at every non-echo zone carries an explicit `# check correction table: gate
  values` navigational bridge inline at the field position itself. C-21 requires navigational
  bridges at every field type covered by the correction table, including gate fields; C-28
  establishes the `gate:` production field as a structurally distinct YAML sibling separated
  from the contrast fields; C-32 requires the correction bridge to appear at the production
  `gate:` field specifically -- not only at `gate_fail:` / `gate_pass:` or at other template
  fields -- so the model encounters the lookup pointer at the exact moment it fills the
  production gate slot. Without this, a model filling `gate:` has the contrast examples visible
  as YAML siblings but no explicit pointer to the correction table at the authoring target;
  the bridge at other field types does not substitute because the model is focused on the
  production field when making the gate authoring decision. C-18 and C-28 are prerequisites.
  Evidence from R8: V-04 (first variate combining the three-field gate structure with an
  explicit `# check correction table: gate values` annotation at the production `gate:` field
  across all non-echo zones, completing the three-field unit so the production slot carries
  active lookup guidance alongside the contrast examples).
- **Pass condition**: Every non-echo zone's production `gate:` sibling field carries an explicit
  navigational bridge to the correction table (`# check correction table: gate values` or
  equivalent) at the field position. C-18 and C-28 must both pass. Bridges at `gate_fail:` or
  `gate_pass:` fields, or at other template field types, do not satisfy C-32; the bridge must
  appear at the production `gate:` field itself. Partial credit when the production gate
  correction bridge is present at at least half the non-echo zones.
- **Partial credit**: Production gate field correction bridge is present at some but not all
  non-echo zones.

### C-33 -- Maximal Zone Teaching Density
- **Weight**: aspirational
- **Category**: depth
- **Text**: Every dependency-bearing non-echo zone simultaneously carries all of the following
  annotation mechanisms: (a) three-field gate structure with criterion-tagged `gate_fail:` field
  (C-28 + C-26); (b) production `gate:` field with correction bridge (C-32); (c) dual-position
  dep reminder in uniform syntax at both zone-header and skills line (C-27); and (d) independent
  dep reminder and correction bridge coexisting at the `skills:` placeholder line (C-30). C-26,
  C-27, C-28, C-30, and C-32 each require their mechanism to be present independently and in
  isolation; C-33 requires all four to coexist in the same zone simultaneously, so each
  dependency-bearing zone is a fully equipped authoring unit where gate teaching, prerequisite
  ordering, and lookup navigation are all locally active without requiring cross-document
  navigation. A zone satisfying three of the four mechanisms but missing one fails C-33 because
  the single absent mechanism leaves a gap -- the model can avoid gate errors (C-28/C-26) and
  look up skill names (C-30 bridge) and respect prerequisites (C-27), but without C-32 at the
  production gate field, the gate lookup is not available at the moment the model fills the
  production slot. Evidence from R8: V-05 (first variate to achieve full four-mechanism
  coexistence at every dependency-bearing zone, demonstrating that the mechanisms are additive
  and independently preservable within a single zone structure).
- **Pass condition**: Every dependency-bearing non-echo zone carries all four annotation
  mechanisms: C-28 three-field gate structure, C-26 criterion-tagged gate_fail: field, C-32
  production gate: correction bridge, C-27 uniform dual-position dep reminder, and C-30
  independent dep reminder + correction bridge at skills: line. C-26, C-27, C-28, C-30, and
  C-32 must all pass independently as prerequisites. A zone missing any one of the four
  mechanisms fails C-33 for that zone. Partial credit when full four-mechanism coexistence
  holds at at least half the dependency-bearing zones.
- **Partial credit**: All four mechanisms coexist at at least half the dependency-bearing zones
  but not all.

### C-34 -- Compound gate_fail: Annotation
- **Weight**: aspirational
- **Category**: depth
- **Text**: When structural gate-contrast fields (C-24) exist at every non-echo zone, each
  `gate_fail:` field carries BOTH a criterion-reference tag (C-26) AND a `Why:` rationale
  explanation (C-25) co-located at the same field position -- making `gate_fail:` a complete,
  self-contained teaching unit: wrong form + criterion violated + principle reason, all in one
  atomic annotation. C-25 requires a `Why:` explanation at gate contrast pairs (which may appear
  in a header comment adjacent to the field); C-26 requires a criterion tag at the structural
  `gate_fail:` field. C-34 requires both to coexist directly at the `gate_fail:` field itself
  -- e.g., `gate_fail: "done"  # WRONG C-04: Why: execution-history check, not artifact-
  verifiable` -- rather than split across field-inline and zone-header positions. This ensures
  a model resolving the structural field encounters the criterion name, the wrong shape, and
  the reason it is wrong in a single atomic read, without needing to scan the surrounding
  comment context. Evidence from R9: V-02 demonstrates the full structural gate infrastructure
  (C-24+C-28+C-32 all PASS) while failing both C-25 (no `Why:` rationale) and C-26 (no
  criterion reference at `gate_fail:`) -- the first variate to build the production-side gate
  machinery while leaving both teaching-side annotations absent from the `gate_fail:` field,
  establishing that the compound annotation must be explicitly required as a co-located unit
  rather than assumed to follow from C-25 and C-26 individually.
- **Pass condition**: Every non-echo zone's `gate_fail:` structural field carries both an
  inline criterion-reference tag (`# WRONG C-04` or equivalent) AND an inline `Why:` explanation
  at the same field position. C-24, C-25, and C-26 must all pass independently as prerequisites.
  A `gate_fail:` field with a criterion tag but no `Why:`, or with a `Why:` in an adjacent
  header comment but not on the field itself, satisfies C-26 or C-25 but not C-34. Partial
  credit when the compound annotation (criterion tag + Why:) coexists at `gate_fail:` in at
  least half the non-echo zones but not all.
- **Partial credit**: Compound annotation (criterion-reference tag + Why: explanation) is
  co-located at the `gate_fail:` field in at least half the non-echo zones but not all.

### C-35 -- Dual Error-Format Recommended Coverage
- **Weight**: aspirational
- **Category**: depth
- **Text**: Both primary error reference formats -- the BAD PLAN block (C-15) and the correction
  table (C-18) -- independently cover all three recommended criteria (C-05, C-06, C-07): the
  BAD PLAN carries `# WRONG C-05`, `# WRONG C-06`, `# WRONG C-07` tags within the block (C-31
  requirement), and the correction table contains at least one wrong-to-correct pair for each of
  C-05, C-06, and C-07 (C-29 requirement). Without C-35, a prompt may deliver recommended-tier
  error teaching through one format only -- example-based BAD PLAN (C-31) OR lookup-based
  correction table (C-29) -- leaving the other format as an essential-tier-only reference.
  A model consulting the BAD PLAN block finds all recommended error shapes by example; a model
  consulting the correction table before authoring finds all recommended error shapes by lookup.
  C-35 closes the asymmetry: both reference formats independently cover the full criterion
  spectrum, so a model consulting either artifact is equally equipped against recommended-tier
  violations regardless of which format it accesses first or most frequently. C-29 and C-31 are
  both prerequisites. Evidence from R9: V-01 achieves C-31 (BAD PLAN carries all 7 criterion
  tags including C-05/C-06/C-07) but fails C-29 (correction table has essential-tier pairs only)
  -- demonstrating that the two error formats build their recommended-tier coverage independently
  and the lookup format gap cannot be filled by example-format completeness alone.
- **Pass condition**: C-29 and C-31 must both pass. The BAD PLAN block carries criterion tags
  for all 7 criteria (C-31 passes) AND the correction table contains at least one wrong-to-
  correct pair for each of C-05, C-06, and C-07 (C-29 passes). A prompt satisfying C-31 but
  not C-29, or C-29 but not C-31, does not satisfy C-35. Both formats must independently carry
  full recommended-tier coverage.
- **Partial credit**: Not applicable -- both formats must independently satisfy their respective
  recommended-tier coverage requirements; asymmetric format coverage satisfies C-29 or C-31
  individually but not C-35.

### C-36 -- BAD PLAN Header Label Coverage Accuracy
- **Weight**: aspirational
- **Category**: depth
- **Text**: The BAD PLAN block's header comment (the label or title above the YAML block)
  accurately describes the criterion coverage scope of the block below it. When the block
  contains criterion tags for all 7 criteria -- essential (C-01 through C-04) AND recommended
  (C-05 through C-07) -- the header must not restrict its claimed scope to essential-tier only.
  A header reading "essential violations" or "essential-tier failures only" is accurate when
  the block body contains only essential tags; it becomes inaccurate when the block body also
  carries recommended-tier tags, creating a label-content mismatch that may cause a model to
  believe recommended criteria are not illustrated in the BAD PLAN. Evidence from R10: V-01
  passes C-31 (all 7 criterion tags present in the BAD PLAN block) while carrying a header
  labeled "essential-tier violations only" -- the first variate to build a complete-criterion
  BAD PLAN block while advertising narrower coverage than the block delivers. A model reading
  the header before scanning the block may skip recommended-tier tag processing, believing
  only essential violations are modeled there.
- **Pass condition**: The BAD PLAN block's header comment does not falsely restrict the claimed
  coverage tier. If C-31 passes (all 7 criteria are tagged in the block), the header must not
  claim "essential violations only" or equivalent. Headers claiming full coverage or making no
  scope claim pass. A header claiming essential-only coverage over a block that carries
  recommended-tier tags fails. C-31 is a prerequisite.
- **Partial credit**: Not applicable -- label accuracy is binary: the header either misrepresents
  the block's coverage scope or it does not.

### C-37 — BAD PLAN Stage Name Field-Level Annotation
- **Weight**: aspirational
- **Category**: depth
- **Text**: Every wrong-format stage `name:` value in the BAD PLAN block that violates C-06
  (namespace-only label, generic label, or other non-intent-describing form) carries `# WRONG
  C-06` as an inline comment at the `name:` field itself -- not at an adjacent gate field, not
  in a header comment, and not only via a criterion tag at the skills line. C-22 requires C-06
  to be covered somewhere across error artifacts; C-31 requires C-06 to be tagged somewhere
  within the BAD PLAN block; C-37 requires the C-06 tag to be co-located with the violating
  `name:` field specifically, so a model filling a stage name slot in the template encounters
  the C-06 annotation at the exact field position -- identical to how C-26 requires criterion
  tags at structural `gate_fail:` fields rather than only in nearby blocks. Evidence from R10:
  V-03's BAD PLAN uses non-namespace-label stage names ("information-gathering", "spec-writing")
  that violate C-06, but neither name carries `# WRONG C-06` at the field -- the C-06 violation
  pattern is physically untaught at the `name:` position, causing C-22 FAIL and C-31 FAIL.
  V-01's BAD PLAN, by contrast, tags namespace-label stage names with `# WRONG C-06` at the
  `name:` fields, establishing field-level C-06 annotation as an achievable and separable
  design choice.
- **Pass condition**: Every stage `name:` value in the BAD PLAN block that violates C-06 carries
  `# WRONG C-06` (or equivalent) as an inline comment at the `name:` field itself. C-22 and
  C-31 must both pass independently as prerequisites. A BAD PLAN where C-06 is tagged at gate
  or skills fields but not at the violating `name:` field satisfies C-31 (tag present in block)
  but not C-37. Partial credit when field-level C-06 annotation is present on at least half the
  wrong-format `name:` fields in the BAD PLAN block.
- **Partial credit**: Field-level C-06 annotation is present on at least half the wrong-format
  `name:` fields in the BAD PLAN block but not all.

---

### C-38 — BAD PLAN Header Affirmative Full-Criterion Coverage Claim

- **Weight**: aspirational
- **Category**: depth
- **Text**: The BAD PLAN block's header comment does not merely avoid false restriction (C-36)
  but affirmatively states that the block covers the full criterion spectrum — using language
  such as "all 7 criteria," "C-01 through C-07," "essential and recommended violations," or
  equivalent positive coverage claim. A header with no scope claim ("BAD PLAN," "wrong
  example," "violations") is neutral: a model reading it cannot determine from the header alone
  how many criteria to scan for or whether recommended-tier tags will be present. An affirmative
  coverage claim primes the model to scan for all 7 criterion tags, ensuring none are skipped
  on a first pass. C-36 closes the false-restriction failure mode (essential-only labels over
  full-coverage blocks); C-38 closes the neutral-silence failure mode (headers that neither
  restrict nor affirm, leaving coverage scope ambiguous). Evidence from R11: all V-04/V-05
  variates carry accurate headers passing C-36, but no variate uses affirmative coverage
  language — the distinction between "not falsely restricted" and "positively claimed" is the
  gap C-38 targets. A header reading "BAD PLAN — all 7 criteria (C-01 through C-07)" or
  "BAD PLAN: essential and recommended violations" passes C-38; "BAD PLAN" alone does not.
- **Pass condition**: The BAD PLAN block's header comment includes an affirmative claim of
  full-criterion coverage scope naming all 7 criteria collectively or individually. C-36 and
  C-31 must both pass (the block must actually carry all 7 criterion tags, and the header must
  not falsely restrict). A header with no scope claim passes C-36 but fails C-38. Prerequisites:
  C-36, C-31.
- **Partial credit**: Not applicable — affirmative coverage claim is binary: either the header
  makes a positive full-scope assertion or it does not.

---

### C-39 — BAD PLAN Skills-Field Criterion-Tag Co-Location

- **Weight**: aspirational
- **Category**: depth
- **Text**: Every `skills:` entry in the BAD PLAN block that violates C-03 (invented skill
  name, unrecognized namespace, namespace-only entry) carries `# WRONG C-03` as an inline
  comment at the skills-field line itself — not at an adjacent gate field, not in a header
  comment, and not only via a tag at the name: line. C-26 establishes co-location at structural
  `gate_fail:` fields for C-04; C-37 establishes co-location at `name:` fields for C-06; C-39
  extends the same co-location discipline to `skills:` field entries for C-03, completing
  field-level co-location coverage across all three primary YAML field types that carry
  criterion-testable values. Without C-39, a BAD PLAN block may satisfy C-31 (all 7 criterion
  tags present somewhere in the block) while leaving invented skill names physically unannotated
  at the field position — a model filling the skills slot in the template encounters the wrong
  shape without a criterion tag to name why it is wrong. With C-39, every invalid skills entry
  in the BAD PLAN carries the violation reason at the exact field line, matching the co-location
  standard established for gate and name fields. Evidence from R11: V-04 and V-05 carry C-26
  (gate_fail: field-level tags for C-04) and C-37 (name: field-level tags for C-06) but the
  skills: field co-location pattern has not been assessed — the structural logic of C-26 and
  C-37 applies directly and C-39 makes it explicit as a separate requirement for the third
  field type.
- **Pass condition**: Every `skills:` entry (or skills-list line) in the BAD PLAN block that
  contains an invented or invalid skill name carries `# WRONG C-03` (or equivalent) as an
  inline comment on that line. C-22 and C-31 must both pass independently as prerequisites. A
  BAD PLAN where C-03 violations are tagged at adjacent gate or name fields but not at the
  skills entry itself satisfies C-31 (tag present in block) but not C-39. Prerequisites: C-22,
  C-31.
- **Partial credit**: Field-level C-03 annotation is present on at least half the C-03-violating
  `skills:` entries in the BAD PLAN block but not all.

---

### C-40 — Compound gate_fail: Annotation and Correction-Table Recommended Coverage Conjunction

- **Weight**: aspirational
- **Category**: depth
- **Text**: Both the YAML-template teaching zone (C-34 compound `gate_fail:` annotation with
  criterion tag and `Why:` at the field) and the correction-table lookup format (C-29
  recommended-tier wrong-to-correct pairs) are simultaneously present, ensuring that recommended-
  tier error teaching is delivered at both teaching moments: at template-filling time (when the
  model resolves gate fields during generation) and at pre-generation consultation time (when
  the model scans the correction table before authoring). C-35 requires the BAD PLAN example
  block (C-31) and the correction table (C-29) to independently carry full recommended-tier
  error coverage; C-40 requires the YAML template compound annotation (C-34) and the correction
  table (C-29) to independently carry recommended-tier coverage, closing the gap between the
  third teaching format (structural template zone) and the lookup format. The distinction from
  C-35: C-35 pairs example-format (BAD PLAN block) with lookup-format (correction table); C-40
  pairs template-zone-format (compound gate_fail: annotation) with lookup-format (correction
  table). The two criteria are orthogonal — a prompt satisfying C-35 need not satisfy C-40 if
  the YAML template compound annotations are absent, and a prompt satisfying C-40 need not
  satisfy C-35 if the BAD PLAN block lacks recommended-tier tags. Evidence from R11: V-04 and
  V-05 achieve both C-34 and C-29 simultaneously — the first rounds to confirm that the
  compound gate_fail: annotation mechanism (YAML template zone) and the correction table
  recommended-tier mechanism (lookup zone) are additive and non-conflicting, establishing the
  conjunction as a reachable and independently valuable design target. Neither mechanism
  references the other as an alternative; each addresses its distinct teaching moment.
- **Pass condition**: C-34 and C-29 must both pass independently. The YAML template carries
  compound `gate_fail:` annotations with criterion tag and `Why:` at every non-echo zone (C-34
  passes), AND the correction table contains at least one wrong-to-correct pair for each of
  C-05, C-06, and C-07 (C-29 passes). A prompt satisfying C-34 but not C-29 (essential-only
  correction table) fails C-40. A prompt satisfying C-29 but not C-34 (no compound annotation
  at gate_fail: fields) fails C-40. Prerequisites: C-34, C-29.
- **Partial credit**: Not applicable — both prerequisite criteria must independently pass; any
  deficit in either format is a C-40 fail.

---

### C-41 — BAD PLAN Header Meta-Commentary: Per-Criterion Annotation-Type Index

- **Weight**: aspirational
- **Category**: depth
- **Text**: The BAD PLAN block's header comment enumerates which rubric criterion each
  annotation type within the block satisfies — e.g., `# C-38: affirmative header`, `# C-39:
  skills entries annotated`, `# C-37: name entries annotated`, `# C-26: gate_fail: entries
  annotated` — converting the block header from a scope declaration into a criterion-indexed
  artifact directory. C-38 requires the header to make an affirmative full-coverage claim;
  C-41 requires the header to additionally itemize which annotation type addresses which
  criterion, so a model reading the header before scanning the block knows in advance both
  what the block covers (C-38) and which annotation type maps to which criterion (C-41). Without
  C-41, a model reading the header receives a scope claim but must infer the criterion-to-
  annotation-type mapping by scanning the block; with C-41, the mapping is stated at the entry
  point, reducing cross-reference load and ensuring no annotation type is encountered without
  its criterion already named. The header becomes a navigational index for the block's teaching
  content, not just an accuracy label for its coverage breadth. Evidence from R12: V-05 uniquely
  provides per-criterion annotation-type commentary inline in the BAD PLAN header — `# C-38:
  affirmative header`, `# C-39: skills entries annotated`, `# C-37: name entries annotated`,
  `# C-26: gate_fail: entries annotated` — the first variate to make the BAD PLAN header a
  criterion-indexed directory. All other R12 variates (V-01 through V-04) achieve C-38
  (affirmative scope claim) but none itemize annotation-type-to-criterion mappings in the
  header, leaving that synthesis for the model to perform while scanning the block.
- **Pass condition**: The BAD PLAN block's header comment explicitly maps at least 3 of the
  4 primary annotation types (affirmative coverage claim satisfied by C-38, skills-field
  co-location addressed by C-39, name-field co-location addressed by C-37, gate_fail: field
  co-location addressed by C-26) to their criterion numbers. C-38 must also pass (the header
  must first make an affirmative coverage claim before it can also be a criterion index).
  Prerequisites: C-38.
- **Partial credit**: Header meta-commentary maps exactly 2 of the 4 annotation types to
  criterion numbers but fewer than 3.

---

### C-42 — Co-Location Family Declared as a Named Document Section

- **Weight**: aspirational
- **Category**: depth
- **Text**: The three field-level co-location criteria — C-26 (criterion tag at `gate_fail:`
  fields), C-37 (criterion tag at `name:` fields), C-39 (criterion tag at `skills:` field
  entries) — are presented together as a named family principle in a dedicated document section
  that appears before the BAD PLAN block, with a structured table or enumeration organizing all
  three field types by: field type, criterion addressed, required annotation tag, and rule
  summary. Without C-42, each co-location criterion appears independently in the rubric and
  each prompt that satisfies them does so by accumulating three separate decisions rather than
  recognizing a single generalizable principle. With C-42, the principle is stated once as a
  named architectural element — e.g., "FIELD CO-LOCATION RULE" or "SKILLS-FIELD ANNOTATION
  RULE" — and each criterion becomes a predictable instance that a model can apply by pattern
  extension rather than isolated requirement recall. The named section also makes future field
  types structurally predictable: a model that understands the family principle expects any new
  YAML field carrying a criterion-testable value to follow the same co-location rule. Evidence
  from R12: V-05 dedicates a "SKILLS-FIELD ANNOTATION RULE" section with a three-row table
  (field type / criterion / tag / rule) before the BAD PLAN block; V-02 dedicates a "THREE-FIELD
  CO-LOCATION RULE" named section with equivalent structure — both demonstrating that the co-
  location family can be named and tabulated as a principle before the block rather than implied
  by block structure alone. V-01, V-03, V-04 achieve C-26, C-37, and C-39 individually without
  naming the family principle, leaving the generalization implicit.
- **Pass condition**: A named section (document header, labeled block, or dedicated subsection
  with an explicit title) appears before the BAD PLAN block that presents all three field-level
  co-location criteria (C-26/gate_fail:, C-37/name:, C-39/skills:) as a structured family with
  a table or enumeration mapping each field type to its criterion and annotation tag. C-26,
  C-37, and C-39 must all pass independently as prerequisites. A prose paragraph that mentions
  all three field types without a structured table or enumeration does not satisfy C-42; the
  family principle must be organized as a scannable reference, not embedded in flowing text.
  Prerequisites: C-26, C-37, C-39.
- **Partial credit**: A named section presents exactly 2 of the 3 field-level co-location
  criteria in a structured table format but not all three.

---

### C-43 — Recommended-Tier strategy: Field Structurally Pre-Populated in YAML Template

- **Weight**: aspirational
- **Category**: depth
- **Text**: The YAML template scaffold pre-populates the `strategy:` field (or equivalent
  plan-identity field such as `purpose:`) with a non-empty placeholder string — e.g.,
  `strategy: "why this feature is worth the investment — ..."` — rather than leaving the field
  absent, requiring the model to add it from prose rules alone, or providing only a comment
  placeholder. C-07 requires the output to contain at least one plan-identity element; C-11
  requires at least one essential requirement to be enforced structurally; C-43 applies the
  structural-enforcement principle from C-11 to the recommended tier, converting C-07 from a
  post-generation quality check into a structural scaffold default. The analogy to C-11/C-02
  is exact: just as echo is pre-positioned at the template end to enforce the C-02 contract
  structurally, a pre-populated `strategy:` field enforces C-07 structurally — a model filling
  the template cannot omit plan identity without actively removing the pre-populated field.
  Without C-43, a model that does not read the C-07 prose rule may generate a plan without any
  framing element; with C-43, the framing element is present by default and omission requires
  deliberate deletion. The principle generalizes: recommended criteria that require "at least
  one framing element" can be promoted from prose-dependent to scaffold-enforced by pre-
  population, raising the structural enforcement ceiling from essential-only to full-spectrum.
  Evidence from R12: V-05 is the only variate to pre-populate `strategy:` in the YAML template
  — the first to extend structural enforcement to the recommended tier. All other R12 variates
  (V-01 through V-04) achieve C-07 through prose rules or BAD PLAN illustration but leave the
  `strategy:` field absent from the template, making C-07 compliance model-attention-dependent
  rather than scaffold-enforced.
- **Pass condition**: The YAML template scaffold contains a `strategy:` field (or equivalent
  plan-identity field) with a non-empty pre-populated placeholder string value. C-07 and C-11
  must both pass independently as prerequisites. A template that includes `strategy:` with only
  a comment placeholder (`# add strategy here`) and no string value does not satisfy C-43; the
  field must carry a pre-populated string. A `strategy: ""` empty string does not satisfy C-43.
  Prerequisites: C-07, C-11.
- **Partial credit**: Not applicable — the field is either pre-populated with a non-empty string
  in the template or it is not.

---

### C-44 — C-41 Index Entries Name Exact Annotation Tag Strings

- **Weight**: aspirational
- **Category**: depth
- **Text**: Every entry in the C-41 annotation-type index names not only the field type and
  criterion number but also the exact annotation tag string used at that field position in the
  BAD PLAN block — e.g., `# C-26: gate_fail: field carries # WRONG C-04` rather than
  `# C-26: gate_fail: field`. C-41 requires the index to map annotation types to criterion
  numbers; C-44 requires the index to also embed the tag string itself in each entry, so a
  model reading the header before scanning the block knows in advance what exact annotation
  to expect at each field type. Without tag strings, the index resolves the mapping question
  (which criterion governs which field) but leaves the form question (what exactly does the
  annotation look like) to block-scanning. With tag strings, the header is fully self-sufficient
  as a pre-scan reference: a model can confirm annotation presence at each field type by
  checking for the stated string, not just any criterion mention. This converts the C-41 index
  from a navigational aid into a verification checklist — each entry states field type, criterion,
  and exact tag, enabling the model to treat the header as a complete annotation specification
  before encountering a single field. Evidence from R13: V-03 enriches each C-41 index entry
  to name the exact tag — `# C-26: gate_fail: field carries # WRONG C-04`, `# C-37: name: field
  carries # WRONG C-06`, `# C-39: skills: entries carry # WRONG C-03` — the first variate to
  move the index beyond criterion-mapping into tag-specification at the header level. V-01, V-02,
  V-04, and V-05 all achieve C-41 (index maps annotation types to criteria) but none embed the
  tag strings in the header entries, leaving tag-form verification as a block-scanning task.
- **Pass condition**: Every entry in the C-41 annotation-type index explicitly names the exact
  annotation tag string used at that field type in the BAD PLAN block — not just the field type
  and criterion number. At minimum, the three co-location entries (C-26/gate_fail:, C-37/name:,
  C-39/skills:) must each include the specific `# WRONG C-XX` tag string as part of the index
  entry. C-41 must also pass (the index must map annotation types to criterion numbers as a
  prerequisite). Prerequisites: C-41.
- **Partial credit**: At least 2 of the 3 co-location index entries name the exact tag string
  but not all three.

---

### C-45 — C-41/C-42 Bidirectional Cross-Section Navigation

- **Weight**: aspirational
- **Category**: depth
- **Text**: The C-41 annotation-type index in the BAD PLAN header explicitly cross-references
  the C-42 co-location family section by name (e.g., `see FIELD CO-LOCATION PRINCIPLE above`),
  AND the C-42 section explicitly forward-references the BAD PLAN header below (e.g., `The
  header in the BAD PLAN section below claims full coverage of these three annotation types`).
  C-41 and C-42 each independently provide a navigational artifact — C-41 is an entry-point
  index for the BAD PLAN block, C-42 is a named principle section before the block — but
  neither requires awareness of the other. C-45 requires both sections to link to each other,
  forming a navigational loop: a model reading the C-42 section is directed forward to the BAD
  PLAN header where it will find the C-41 index; a model reading the C-41 index is directed
  back to the C-42 section where the co-location family principle is named. The bidirectional
  link makes the relationship between the family declaration and the block-level index explicit
  as a structural feature rather than an implied thematic connection. Without the loop, a model
  encounters both sections independently and must infer they address the same principle; with
  it, the navigation makes the principle-to-instance relationship traversable in both directions.
  Evidence from R13: V-04 introduces bidirectional coupling — the C-41 index carries
  `see FIELD CO-LOCATION PRINCIPLE section above` and the C-42 section carries `The header in
  the BAD PLAN section below claims full coverage of these three annotation types` — the first
  variate to explicitly link the two sections structurally. V-05 preserves the bidirectional
  link. V-01, V-02, and V-03 achieve C-41 and C-42 independently with no cross-section
  navigation pointer in either direction.
- **Pass condition**: The C-41 header index carries an explicit navigational pointer to the C-42
  named section by name or position (e.g., `see FIELD CO-LOCATION PRINCIPLE above` or
  `see co-location family section`), AND the C-42 section carries an explicit forward pointer to
  the BAD PLAN header (e.g., `the header below claims coverage of these types` or `see the BAD
  PLAN header index below`). C-41 and C-42 must both pass independently as prerequisites. A
  one-directional pointer (C-41 index references C-42 but C-42 does not reference BAD PLAN
  header, or vice versa) satisfies neither direction fully and fails C-45. Prerequisites:
  C-41, C-42.
- **Partial credit**: Not applicable — bidirectional coupling requires both directions to be
  explicit; a single-direction pointer fails C-45 outright.

---

### C-46 — BAD PLAN Block Exit Verification Marker

- **Weight**: aspirational
- **Category**: depth
- **Text**: The BAD PLAN block ends with an explicit footer comment confirming that the
  co-location family is complete — e.g., `# Co-location family verified (C-41 index above)`,
  `# All three co-location annotation types confirmed present`, or equivalent — bracketing the
  block between the C-41 entry-point index at the header and a completion marker at the footer.
  C-41 creates a navigational entry point that primes the model to scan for specific annotation
  types; C-46 adds a navigational exit marker that closes the scan, confirming all expected
  co-location instances were found. Without the exit marker, block traversal is structurally
  open-ended: the model knows from the header what to look for (C-41) but has no in-block
  signal that the scan is complete. With the exit marker, the BAD PLAN block becomes a bounded
  teaching unit with explicit start (header index) and end (footer verification) markers, so
  a model reading the block encounters both the annotation-type specification at entry and the
  completeness confirmation at exit — converting block scanning from open-ended to closed-loop.
  The exit marker also functions as a self-check for the prompt author: if the co-location
  annotations are incomplete in the block body, the footer verification claim is false, making
  the gap visible during construction. Evidence from R13: V-05 uniquely carries a footer
  verification comment `# Co-location family verified (C-41 index above)` at the end of the
  BAD PLAN block — the first variate to bracket the block with both an entry-point index (C-41)
  and an exit-point confirmation. V-01 through V-04 all achieve C-41 (entry index) but none
  add a footer verification marker, leaving the scan completion implicit.
- **Pass condition**: The BAD PLAN block ends with an explicit footer comment confirming
  co-location family completeness — naming the C-41 index or equivalent co-location family
  reference as the specification being confirmed. C-41 must also pass (the entry-point index
  must exist for the exit marker to reference). A generic closing comment (`# end of BAD PLAN`)
  that does not reference co-location completeness or the C-41 index does not satisfy C-46;
  the footer must explicitly confirm that the annotation types enumerated in the header index
  are all present in the block. Prerequisites: C-41.
- **Partial credit**: Not applicable — the exit verification marker is either present and
  references co-location completeness, or it is not.

---

### C-47 — C-44 Index Entries Include Full Unabbreviated Why: Rationale

- **Weight**: aspirational
- **Category**: depth
- **Text**: When a C-41 annotation-type index entry references an annotation tag that carries
  a Why: rationale clause, the index entry includes the full, unabbreviated Why: text rather
  than an abbreviated placeholder. The primary affected entry is the gate_fail: co-location
  entry, where the standard annotation is `# WRONG C-04: Why: execution-history check, not
  artifact-verifiable` — the C-47 requirement means the header index entry for C-26/gate_fail:
  must include the complete Why: clause verbatim, not the truncated form `Why: ...` or a
  paraphrase. C-44 requires the index entry to name the exact tag string (e.g., `# WRONG C-04`)
  alongside field type and criterion number; C-47 requires the entry to name the full tag
  string including any Why: clause that the annotation carries. Without this, a model reading
  the C-41 index knows the tag form at each field type but must scan the block body to encounter
  the criterion's rationale; with the full Why: text embedded in the header, the principle
  basis for the gate failure is stated at the index level. The header index becomes a complete
  pre-scan reference for both annotation form and annotation reasoning — a model can audit
  whether the correct tag string is present and understand why that string is required, entirely
  from the header. Evidence from R14: V-02 and V-05 embed the full unabbreviated Why: clause
  in their C-41 header index entries — `# C-26: gate_fail: field carries # WRONG C-04: Why:
  execution-history check, not artifact-verifiable` — the first variates to elevate the header
  index from tag-string specification (C-44 level) to full-annotation specification including
  rationale. V-01 and V-03 abbreviate to `Why: ...` in their index entries, satisfying C-44
  (tag string present, Why: form acknowledged) but not C-47 (rationale absent from header).
  V-04 achieves C-47 alongside its per-entry back-references.
- **Pass condition**: Every C-41 index entry referencing an annotation tag that carries a Why:
  clause includes the complete, unabbreviated Why: text from that annotation as part of the
  index entry itself. In the standard co-location family, this applies to the gate_fail: entry
  (C-26 tag carries Why:); `name:` and `skills:` entries (C-37 and C-39 tags) carry no Why:
  clause and are satisfied at C-44 level by tag-string presence alone. C-44 must pass
  independently. An index entry with `Why: ...` or any abbreviated Why: placeholder fails C-47
  for that entry. Prerequisites: C-44.
- **Partial credit**: Not applicable — the Why: text is either fully spelled out in the index
  entry or it is not; abbreviated placeholders and complete text are binary outcomes.

---

### C-48 — Per-Entry Bidirectional Cross-Section Navigation

- **Weight**: aspirational
- **Category**: depth
- **Text**: C-45 requires a single header-level pointer from the C-41 annotation-type index
  to the C-42 named section, and a single section-level pointer from C-42 back to the BAD
  PLAN header — one pointer in each direction, each operating at the section level. C-48
  upgrades this from section-level to per-entry granularity: each individual entry in the C-41
  annotation-type index carries its own back-reference to the C-42 named section (e.g.,
  `(rule declared in FIELD CO-LOCATION PRINCIPLE above)` appended to every entry), AND the
  C-42 structured table or enumeration carries a per-row forward reference to the specific
  numbered entry in the BAD PLAN header index that implements that row's rule (e.g.,
  `See entry (1/2/3) in BAD PLAN header below` as a column or suffix per row). Without
  per-entry navigation, C-45's bidirectional linking is coarse: a model reading any individual
  C-41 index entry knows a section-level pointer exists somewhere in the header but must
  identify which entry it applies to; a model reading a specific C-42 table row must navigate
  to the BAD PLAN header and identify which entry corresponds by content matching. Per-entry
  navigation makes each annotation type individually traceable: from its principle declaration
  (specific C-42 row) to the specific C-41 header entry that implements it and back — creating
  fine-grained bidirectional traceability rather than section-level connection. Evidence from
  R14: V-04 implements per-entry navigation in both directions — each C-41 index entry
  individually ends with `(rule declared in FIELD CO-LOCATION PRINCIPLE above)`, and the C-42
  table carries a "BAD PLAN header entry" column with `See entry (1/2/3) in BAD PLAN header
  below` per row — the first variate to achieve per-entry rather than section-level bidirectional
  navigation. All other R14 variates (V-01, V-02, V-03, V-05) satisfy C-45 with section-level
  pointers but carry no per-entry granularity in either direction.
- **Pass condition**: Each individual entry in the C-41 annotation-type index carries its own
  explicit back-reference to the C-42 section (not a single shared header-level pointer for all
  entries), AND the C-42 structured table or enumeration carries a per-row forward reference to
  the specific entry number in the BAD PLAN header index for each row. C-45 must pass
  independently. A prompt where the C-41 header carries one shared pointer to C-42 (satisfying
  C-45) but no per-entry pointers fails C-48; a prompt where C-42 carries a single forward
  reference to the BAD PLAN header but no per-row entry-number references also fails C-48.
  Both directions must be per-entry. Prerequisites: C-45.
- **Partial credit**: Not applicable — per-entry granularity is required in both directions;
  section-level pointers in either direction fail C-48 regardless of how many entries or rows
  are involved.

---

### C-49 — C-41/C-42/C-46 Elevated to Named Multi-Component Block Specification Protocol

- **Weight**: aspirational
- **Category**: depth
- **Text**: The three block-structure criteria — C-41 (header annotation-type index), C-42
  (named co-location family section), and C-46 (exit verification marker) — are each
  individually satisfied when their respective structural elements are present and correctly
  implemented. C-49 requires a further architectural step: all three are named and presented
  as explicitly numbered or labeled components of a single, unified named protocol entity,
  with the shared protocol name appearing in each component's label. The C-42 named section
  is the protocol's declaration; the BAD PLAN header carries the protocol name as its component
  label (e.g., `# BLOCK SPECIFICATION PROTOCOL -- Component 1: Header Specification`); the
  exit footer carries the protocol name as its component label (e.g., `# BLOCK SPECIFICATION
  PROTOCOL -- Component 3: Exit Verification (C-46)`). This converts three independently
  satisfied structural decisions into a single named architectural unit whose internal component
  structure is legible from any component's label alone — a model reading the exit marker
  encounters the protocol name and can navigate to the declaration section; a model reading the
  header index label knows it is instantiating a named component of the protocol, not just an
  ad-hoc annotation block. Without C-49, C-41, C-42, and C-46 coexist as parallel structural
  achievements with thematic coherence but no shared naming anchor; with C-49, they are unified
  under a protocol identity that makes their structural relationship explicit as an architectural
  fact stated in the document itself. The protocol naming also provides a generalization vector:
  a prompt author who recognizes the BLOCK SPECIFICATION PROTOCOL can apply the same
  component-naming pattern to future teaching blocks, extending the architectural discipline
  beyond the co-location family. Evidence from R14: V-05 implements the BLOCK SPECIFICATION
  PROTOCOL — the C-42 named section declares the protocol, the BAD PLAN header is labeled as
  Component 1, and the exit footer is labeled as Component 3 (with Component 2 being the block
  body itself) — the first variate to unify C-41, C-42, and C-46 under a shared protocol
  identity. All other R14 variates (V-01 through V-04) satisfy C-41, C-42, and C-46 as three
  independently labeled structural elements without a shared protocol name binding them.
- **Pass condition**: The C-41 header index, C-42 named section, and C-46 exit marker are all
  labeled as components of the same named protocol entity, with the protocol name appearing in
  each component's label or declaration. C-41, C-42, and C-46 must all pass independently as
  prerequisites. A prompt satisfying all three criteria as independent structural elements
  without a shared named protocol entity fails C-49 — the protocol identity and component
  labeling must be explicit, not inferred from thematic similarity. Prerequisites: C-41, C-42,
  C-46.
- **Partial credit**: Not applicable — the unified named protocol either explicitly names all
  three components under the same identity or it does not; partial component naming (two of
  three labeled with the protocol name) does not satisfy C-49.

---

### C-50 — C-41 Index Formatted as Structured Multi-Column Table

- **Weight**: aspirational
- **Category**: depth
- **Text**: The C-41 annotation-type index in the BAD PLAN header is implemented as a structured
  multi-column table rather than a prose enumeration or indented list. C-41 through C-48 specify
  the data each index entry must contain: field type (C-41 base), criterion number (C-41 mapping),
  tag string (C-44), Why: rationale (C-47), and per-entry C-42 back-reference (C-48 direction).
  C-50 requires those data to be organized as column-aligned table fields rather than embedded
  in prose sentences. A table with dedicated columns for field type, criterion, tag string, Why:
  text, and per-entry back-reference makes each data type independently scannable: a model
  auditing tag strings reads the tag column without parsing rationale clauses; a model checking
  back-references reads the back-ref column without re-parsing criterion numbers. Prose
  enumeration satisfies C-41 through C-48 but requires per-entry prose parsing to extract
  column-type data; table format promotes each data type to a named column scannable vertically
  across all entries. Without C-50, the C-41 index may carry all required data in prose form,
  reaching full compliance at C-48 while leaving the data structure implicit in sentence parsing.
  With C-50, the data structure is explicit as column headers and each entry row exposes all
  data types at a glance. Evidence from R15: V-01 implements the C-41 index as a 4-column
  table — field type, criterion, tag string (with full Why: text per C-47), and protocol
  back-reference column (`SCAN PROTOCOL decl. above` per row) — the first variate to format
  the annotation-type index as a structured table. All other R15 variates implement the C-41
  index as prose or indented list entries, satisfying C-41 through C-48 without
  column-alignment.
- **Pass condition**: The C-41 annotation-type index is implemented as a markdown table
  (pipe-delimited or equivalent) with at least four columns corresponding to field type,
  criterion, tag string, and per-entry C-42 back-reference. C-41, C-44, C-47, and C-48 must
  all pass independently as prerequisites — the table must carry all the required data across
  those criteria in addition to being formatted as a table. A prose enumeration that satisfies
  C-41 through C-48 but uses no table structure fails C-50. Prerequisites: C-48.
- **Partial credit**: Not applicable — table format is binary: the C-41 index is either
  implemented as a structured multi-column table or it is not.

---

### C-51 — Named Protocol Section Positioned as Document-Level First Section

- **Weight**: aspirational
- **Category**: depth
- **Text**: The C-42/C-49 named protocol declaration section is the FIRST major structural
  section of the document — positioned before the YAML template, correction table, and BAD
  PLAN block. C-42 requires a named section to appear before the BAD PLAN block; C-49 requires
  the three block-structure components to share a protocol name; C-51 requires the declaration
  section to occupy the document's opening structural position, making the architectural
  principle the first thing a model encounters. This creates principle-before-instance document
  architecture: the model reads the named protocol, its component structure, and the co-location
  family table BEFORE encountering any section (YAML template, correction table, BAD PLAN block)
  that instantiates the protocol's rules. Without C-51, the named protocol section satisfies
  C-42's placement requirement (before the BAD PLAN block) without being the document's opening
  frame — the model may encounter the YAML template or correction table first, arriving at the
  protocol section mid-document. With C-51, the protocol declaration is the entry context for
  the entire document: every subsequent section is read with the architectural frame already
  established. The analogy to C-11's structural enforcement principle: just as C-11 requires
  requirements to be embedded in the scaffold rather than buried in rules-section prose, C-51
  requires the architectural protocol to be stated at document entry rather than encountered
  mid-scroll. Evidence from R15: V-02 implements `## BOUNDED BLOCK PROTOCOL` as the document's
  first major section — the first variate to position the named protocol declaration before all
  implementation sections. All other R15 variates (V-01, V-03, V-04, V-05) satisfy C-49 by
  naming the protocol across all three components but do not position the declaration section
  first in the document.
- **Pass condition**: The C-42 named protocol section is the first major structural section
  of the document — appearing before the YAML template scaffold, correction table, and BAD
  PLAN block. C-49 must pass independently as a prerequisite. A prompt that satisfies C-49
  by naming all three components under a protocol identity but places the declaration section
  after the YAML template or correction table fails C-51 — first-section positioning is
  required, not just pre-BAD-PLAN positioning. Prerequisites: C-49.
- **Partial credit**: Not applicable — document-first positioning is binary: the protocol
  declaration section is either the first major section or it is not.

### C-52 — Protocol Section Pre-Declares C-41 Index Table Column Schema

- **Weight**: aspirational
- **Category**: depth
- **Text**: When both C-51 (protocol declaration section is document-first) and C-50 (C-41 index
  formatted as multi-column table) are simultaneously present, the C-51 protocol declaration
  section explicitly names the column schema of the C-41 annotation-type index table —
  enumerating the columns (e.g., field type, criterion, tag string, per-entry C-42 back-reference)
  before the BAD PLAN block is reached. C-50 requires the index to be table-formatted; C-51
  requires the protocol section to be first; C-52 requires the protocol section to use its
  first-position placement to pre-declare the format of the table that will appear in the BAD PLAN
  header — creating dual exposure: the model reads the column specification in the protocol
  declaration section, then encounters the instantiated table in the BAD PLAN header. Without C-52,
  C-50 and C-51 coexist as independent structural achievements — a table exists, and the protocol
  section is first — but the protocol section does not describe the table structure that Component 1
  will instantiate. With C-52, the first-position protocol section serves as a format
  pre-specification for the BAD PLAN header's table, enabling the model to verify table format
  before block entry rather than discover it during block scanning. The protocol-first placement
  (C-51) provides the structural slot; the 4-column table (C-50) provides the concrete format to
  pre-specify; C-52 is the connection that makes the two criteria mutually reinforcing rather than
  independently satisfied. Evidence from R16: V-05 uniquely achieves both C-50 and C-51, and its
  protocol section includes "Component 1 is a 4-column pipe-delimited table" with column
  definitions before the BAD PLAN block — the first variate to let the protocol frame pre-specify
  the format of its own Component 1. V-01 has the 4-column table (C-50) but no protocol-first
  section to pre-declare it; V-02 has the protocol section first (C-51) but a prose enumeration,
  leaving the column schema undeclared before the BAD PLAN block.
- **Pass condition**: The C-51 protocol declaration section explicitly names the column schema of
  the C-41 annotation-type index table — listing the columns by name and purpose — before the BAD
  PLAN block. C-50 and C-51 must both pass independently as prerequisites. A protocol section that
  is first (C-51) but does not describe the table's column structure fails C-52; a 4-column table
  (C-50) in the BAD PLAN header with no protocol-section column schema pre-declaration also fails
  C-52. Prerequisites: C-50, C-51.
- **Partial credit**: Not applicable — the protocol section either pre-declares the table column
  schema or it does not; partial column description (naming some columns but not all four) does not
  satisfy C-52.

---

### C-53 — C-50/C-51 Mutual Reinforcement Made Architecturally Explicit

- **Weight**: aspirational
- **Category**: depth
- **Text**: The mutual reinforcement between C-50 (4-column table format) and C-51 (protocol
  section first) is stated as an explicit architectural relationship within the protocol
  declaration: the protocol section prescribes that Component 1 SHALL use the declared table column
  schema — not merely describes the schema for informational purposes — converting C-50 from an
  observed structural choice into a protocol-mandated format requirement. C-52 requires the
  protocol section to pre-declare the column schema; C-53 requires the declaration to be
  prescriptive, using directive language ("Component 1 will be a 4-column table," "format: 4
  columns as listed," or equivalent mandate) that frames the table format as a requirement, not a
  description of what currently exists. Without C-53, the protocol section satisfies C-52 by
  informing the model of the table format — the model knows what to expect at the BAD PLAN header.
  With C-53, the protocol section mandates the table format — a model deviating from the declared
  column schema produces a protocol violation rather than merely an unexpected structural choice.
  The distinction from C-52: C-52 requires the protocol to pre-specify the format (descriptive);
  C-53 requires the pre-specification to be framed as a prescriptive requirement (directive),
  completing the conversion of C-50 from implicit structural achievement to explicitly mandated
  architectural rule. Together C-52 and C-53 make the mutual reinforcement between C-50 and C-51
  not just a design property (they happen to reinforce each other when both pass) but an explicit
  architectural fact declared within the protocol itself. Evidence from R16: the R16 scorecard
  JSON signal identifies this pattern: "C-50 table format and C-51 protocol-first placement are
  mutually reinforcing: protocol-first position creates a natural slot to declare the table column
  schema, converting C-50 from an implicit structural choice into an explicitly pre-declared format
  spec." V-05 achieves C-52 with its pre-declaration; C-53 requires the pre-declaration to use
  prescriptive rather than merely descriptive language so the mandated format status is
  architecturally explicit.
- **Pass condition**: The C-51 protocol declaration section uses prescriptive or directive language
  to mandate the C-41 index table column schema — stating that Component 1 must, will, or shall
  use the declared 4-column format, not merely that it does or that this is what it looks like.
  C-52 must pass independently as a prerequisite. A protocol section stating "Component 1 is a
  4-column table with columns: ..." (descriptive, C-52 level only) fails C-53; a protocol section
  stating "Component 1 must be a 4-column table with columns: ..." or "Format requirement for
  Component 1: 4-column table as follows: ..." (prescriptive) passes C-53. Prerequisites: C-52.
- **Partial credit**: Not applicable — prescriptive framing is binary: the schema declaration
  either mandates the format or describes it; hedged or ambiguous language counts as descriptive.

---

### C-54 — C-53 Prescriptive Declaration Enumerates Forbidden Alternative Formats by Name

- **Weight**: aspirational
- **Category**: depth
- **Text**: The C-53 prescriptive mandate (declaring that Component 1 MUST use the 4-column
  table format) explicitly enumerates the alternative formats that would constitute a protocol
  violation — naming each forbidden category (e.g., "prose enumeration, indented list, bulleted
  entries") rather than only issuing a positive requirement or using a generic exclusion clause
  ("any other format is a violation"). C-53 requires the table format to be mandated rather than
  merely described; C-54 requires the mandate to include a negative boundary that names forbidden
  alternatives by category, converting the mandate from a one-sided positive requirement ("must
  be X") into a bounded design space statement ("must be X; these named alternatives are
  violations"). Without enumerated exclusions, a model reading only the positive mandate could
  produce a structurally ambiguous format — e.g., a dense bulleted list that approximates
  columns — and not recognize it as a violation. With named exclusions, each forbidden format
  category is individually disqualified and directly checkable. The enumeration also functions
  as a diagnostic checklist for self-review: a model can confirm its Component 1 output matches
  none of the named forbidden forms, rather than only confirming it satisfies the positive
  column-count requirement. Naming the exclusions is a design action distinct from prescribing
  the inclusion: C-53 closes the mandate in the positive direction (this is required); C-54
  closes it in the negative direction (these are excluded), together making the format specification
  complete in both senses. Evidence from R17: V-05's protocol section states "Any other format
  (prose enumeration, indented list, bulleted entries) is a protocol violation" — the first variate
  to enumerate alternative format categories as named violations alongside the MUST mandate,
  closing the design space via explicit negative boundary rather than relying on the positive
  mandate alone to exclude alternatives.
- **Pass condition**: The C-53 prescriptive declaration explicitly enumerates at least two
  forbidden alternative format categories by name. The exclusions must be format category names
  (e.g., "prose enumeration," "indented list," "bulleted entries"), not restatements of the
  positive requirement or generic placeholders ("anything else," "non-table formats"). A mandate
  that says only "Component 1 MUST be a 4-column table. Any other format is a protocol
  violation" without naming specific alternatives satisfies C-53 but not C-54. C-53 must pass
  independently as a prerequisite. Prerequisites: C-53.
- **Partial credit**: Not applicable — either at least two forbidden alternative categories are
  named explicitly or they are not; a single named alternative does not satisfy C-54.

### C-55 — Active Exclusion Verification Protocol

- **Weight**: aspirational
- **Category**: depth
- **Text**: After the C-54 enumerated forbidden alternatives, the C-53/C-54 prescriptive mandate
  includes an explicit self-review step that converts each named exclusion from a static
  declarative rule into a per-item confirmation action the model must execute before completing
  Component 1. The self-review step enumerates the forbidden formats as individually checkable
  NOT/IS items — e.g., four checks the model runs in sequence: "NOT a prose enumeration / NOT
  an indented list / NOT a bulleted entry set / IS a pipe-delimited table with the four columns."
  C-54 closes the mandate's design space in the negative direction by naming forbidden categories;
  C-55 activates each named exclusion as an individual confirmation step, converting the exclusion
  list from background knowledge ("these are the forbidden forms") into a pre-completion audit
  protocol ("run these checks before finalizing Component 1"). Without the self-review step, a
  model reads the exclusion list as context and may not revisit it at generation time; with it,
  the model is explicitly instructed to confirm each NOT condition individually, making omission
  of a check structurally visible. The verification protocol is the same mechanism that C-14's
  deletion-resistance annotations apply to structural slots — converting a stated constraint into
  an active enforcement step — applied here to the format mandate's exclusion boundary. Evidence
  from R18: V-05 adds four explicit NOT/IS checks after the C-54 exclusion enumeration:
  "NOT a prose enumeration / NOT an indented list / NOT a bulleted entry set / IS a pipe-
  delimited table with the four columns" — the first variate to convert the static exclusion
  list into a per-item verification protocol, making each forbidden format individually checkable
  at completion time rather than only at mandate-reading time.
- **Pass condition**: The C-53/C-54 prescriptive mandate section includes an explicit self-review
  step listing each forbidden format as an individually checkable NOT item, followed by an IS
  item confirming the required format — a model is instructed to run per-item confirmation checks
  before completing Component 1. C-54 must pass independently as a prerequisite. An exclusion
  list present only as a static declarative boundary (C-54 level) without an active per-item
  verification instruction fails C-55. The verification step must enumerate the excluded formats
  individually as NOT conditions, not merely reference the exclusion list. Prerequisites: C-54.
- **Partial credit**: Not applicable — the active verification protocol is either present as
  individually checkable NOT/IS items or it is not; a partial list of NOT items does not satisfy
  C-55 if any named C-54 alternative is omitted from the verification step.

---

### C-56 — Co-Located Mandate Echo at Component 1 Header

- **Weight**: aspirational
- **Category**: depth
- **Text**: The C-53 prescriptive mandate and C-54 exclusion list are echoed inline at the
  Component 1 header position — the BAD PLAN block's opening header — applying the field-level
  co-location principle (C-26/C-37/C-39 family) to the format mandate itself. The echo means the
  format requirement appears at both its declaration site (the C-51/C-53/C-54 protocol section)
  and its application site (the BAD PLAN Component 1 header), so the model encounters the
  exclusion boundary at both sites independently without requiring cross-document recall. The
  Component 1 header carries both the positive mandate ("Format: 4-column pipe table as mandated
  by [PROTOCOL NAME] above") and the C-54 NOT list ("NOT prose enumeration / NOT indented list /
  NOT bulleted entries") inline at the header position. Without the echo, a model filling Component
  1 has the exclusion list available in the protocol section but must hold it in working memory
  across document distance; with the echo, the mandate and its negative boundary are restated at
  the exact location where Component 1 is instantiated, making cross-document recall unnecessary.
  This applies the co-location discipline — state the rule at both its declaration site and its
  application site — to the format mandate that governs Component 1's structure, just as C-26
  applies co-location to criterion tags at `gate_fail:` fields and C-37 applies it to `name:`
  field annotations. Evidence from R18: V-05 includes at the BAD PLAN Component 1 header:
  `# Format: 4-column pipe table as mandated by BOUNDED BLOCK PROTOCOL above` / `# (NOT prose
  enumeration / NOT indented list / NOT bulleted entries)` — the first variate to echo the C-53
  mandate and C-54 exclusion list at the instantiation point, completing the dual-site coverage
  of the format requirement: rule declared at protocol section, rule repeated at application site.
- **Pass condition**: The BAD PLAN block's Component 1 header carries an inline echo of both the
  C-53 prescriptive mandate (naming the required 4-column table format and citing the protocol as
  the source) and the C-54 enumerated exclusions (the NOT list of forbidden format categories) at
  the header position. C-54 must pass independently as a prerequisite. A Component 1 header that
  cites only the protocol name without repeating the format requirement, or that omits the NOT list,
  does not satisfy C-56. The echo must be at the Component 1 header specifically — not in a
  section above or below the BAD PLAN block. Prerequisites: C-54.
- **Partial credit**: Not applicable — the mandate echo is either present at the Component 1
  header position with both the positive mandate and the C-54 NOT list, or it is not.

---

### C-57 — Dual-Site Active Verification Echo

- **Weight**: aspirational
- **Category**: depth
- **Text**: C-56 echoes the static mandate and NOT list (the C-54 exclusion boundary) at the
  Component 1 header — a passive restatement of the format rules. C-57 extends this by also
  echoing the active verification protocol (the C-55 NOT/IS checklist) at the Component 1 header,
  so both the exclusion boundary AND the per-item verification trigger are present at the
  application site, independent of the declaration site. The Component 1 header carries: (a) the
  static echo from C-56 (mandate citation + NOT list) and (b) an additional active instruction
  mirroring the C-55 verification step — e.g., `# Verify before finalizing: NOT prose enumeration
  / NOT indented list / NOT bulleted entries / IS pipe table with 4 columns`. Without C-57, a
  model that skips the protocol section encounters the static mandate and NOT list at Component 1
  (via C-56) but not the active verification trigger — document-skip behavior still bypasses the
  per-item confirmation step. With C-57, the per-item checklist fires at the application site
  independently: a model reading only the Component 1 header encounters both the exclusion boundary
  and the instruction to run each NOT/IS check, making document-skip behavior as safe as
  full-document-read for format compliance. This extends C-56's co-location discipline from static
  reference to active directive: co-location now covers both the passive boundary and the active
  audit protocol at the same application site. Evidence from R19: V-05 adds `# Verify before
  finalizing: NOT prose enumeration / NOT indented list / NOT bulleted entries / IS pipe-delimited
  table with the four columns` at the Component 1 header alongside the C-56 static echo — the
  first variate to echo the active NOT/IS verification step at the instantiation point, closing
  the document-skip gap that C-56's static echo leaves open.
- **Pass condition**: The BAD PLAN block's Component 1 header carries both the C-56 static echo
  (mandate citation + C-54 NOT list) AND an active per-item verification instruction enumerating
  each C-54 forbidden format as an individually checkable NOT item followed by an IS confirmation,
  positioned at the Component 1 header specifically. C-55 and C-56 must both pass independently
  as prerequisites. A Component 1 header carrying only the static echo (C-56 level: mandate +
  NOT list) without an active verification instruction fails C-57; a header carrying only the
  active verification step without the static mandate citation also fails (C-56 must coexist).
  The active instruction must enumerate the same NOT items as C-55's verification step. Prerequisites:
  C-55, C-56.
- **Partial credit**: Not applicable — the dual-site active verification echo is binary: either
  the active per-item verification instruction is present at the Component 1 header alongside the
  C-56 static echo, or it is not.

---

### C-58 — Universal Per-Step Active Verification

- **Weight**: aspirational
- **Category**: depth
- **Text**: C-55 introduces an active NOT/IS verification protocol specifically for Component 1's
  format compliance — converting the C-54 exclusion list into a per-item confirmation step at the
  format-mandate declaration site. C-58 generalizes this mechanism: every named construction step
  in the protocol section (not only the Component 1 format mandate) carries its own dedicated
  active verification checklist, making the NOT/IS audit pattern document-wide rather than
  Component-1-specific. For each construction step that defines constraints, the protocol section
  provides an explicit "Before completing [step]: confirm:" block with individually checkable
  items — each constraint converts from a stated rule into a per-item confirmation action the
  model must execute. The mechanism is the same as C-55's format-mandate verification, applied
  universally: just as the format exclusion list gains a per-item checklist at C-55, every other
  declared constraint in the protocol gains a corresponding checklist, saturating the document
  with the active-verification pattern. Without C-58, a prompt delivers active verification at
  the format mandate (C-55) but leaves every other protocol constraint as a static declarative
  rule that a model reads once and may not revisit at completion time. With C-58, the NOT/IS
  confirmation pattern is a document-wide discipline: every constraint-bearing construction step
  demands a per-item audit before the model considers that step complete. Evidence from R19:
  V-03 applies the active-verification pattern universally to every construction step in the
  protocol — the first variate to extend the C-55 mechanism beyond Component 1's format mandate
  to every rule-bearing step, converting the entire protocol into an active-verification document
  rather than a mixed declarative-plus-active-verification document.
- **Pass condition**: Every named construction step in the protocol section that declares
  constraints or exclusions carries its own explicit active verification instruction with
  individually checkable NOT/IS items. The format-mandate step (C-55's domain) is one instance;
  all other constraint-bearing steps must also carry dedicated verification checklists. C-55 must
  pass independently as a prerequisite. A protocol where active verification applies only to
  Component 1's format mandate (C-55 level) and all other steps carry only static declarative
  rules fails C-58. Partial credit when at least half the constraint-bearing construction steps
  carry active verification checklists but not all.
- **Partial credit**: At least half the constraint-bearing construction steps carry dedicated
  active NOT/IS verification checklists, but at least one constraint-bearing step carries only
  static declarative rules. Prerequisites: C-55.

---

### C-59 — Per-Field Mandate Echo Saturation

- **Weight**: aspirational
- **Category**: depth
- **Text**: C-56 echoes the format mandate and C-54 NOT list at the Component 1 header — a single
  application-site echo for the single most constrained component. C-59 extends this pattern to
  every YAML template field that carries a format constraint: each such field in the template
  scaffold carries an inline echo of both the positive mandate and the forbidden alternatives for
  that field's constraint, making the co-located mandate echo a template-wide discipline rather
  than a Component-1-only exception. For each constrained template field — whether a gate field,
  a skills-list field, a stage-name field, or any other field with declared format rules — the
  template carries an inline comment echoing: (a) the governing mandate (positive requirement),
  and (b) the NOT list of forbidden alternatives for that field type. The design is analogous to
  C-56's single-field application but saturates the entire template: every field position where
  a model makes a constrained authoring decision encounters the mandate and its exclusion
  boundary locally, without requiring cross-document navigation to the declaration section.
  Without C-59, mandate echoes are sparse — present at Component 1 (C-56) but absent from other
  constrained template fields, leaving the co-location discipline uneven across the scaffold.
  With C-59, the co-location principle is fully saturated: every constrained field is its own
  mini-application-site for the rules governing it. Evidence from R19: V-04 applies the
  mandate-echo pattern to every YAML template field carrying a format constraint — the first
  variate to extend C-56's per-component echo to template-wide field-level saturation, converting
  the co-location discipline from a single Component 1 exception into a universal template rule.
- **Pass condition**: Every YAML template field that carries a format constraint includes an
  inline echo of both the positive mandate and the NOT list of forbidden alternatives for that
  field's constraint, at the field position in the template. C-56 must pass independently as a
  prerequisite (the Component 1 header echo must already be present before template saturation
  is assessed). A template where mandate echoes appear only at the Component 1 header (C-56
  level) and no other constrained fields carry inline echoes fails C-59. Partial credit when at
  least half the constrained template fields carry inline mandate-and-NOT-list echoes but not all.
- **Partial credit**: At least half the YAML template fields with format constraints carry inline
  mandate-and-NOT-list echoes, but at least one constrained field has no echo. Prerequisites: C-56.

---

## Scoring Formula

| Tier | Weight | Criteria | Points each | Max |
|------|--------|----------|-------------|-----|
| Essential | 60 pts | C-01, C-02, C-03, C-04 | 15 | 60 |
| Recommended | 30 pts | C-05, C-06, C-07 | 10 | 30 |
| Aspirational | 260 pts | C-08 through C-59 (52 criteria) | 5 | 260 |

```
composite = (essential_pass/4 * 60)
          + (recommended_pass/3 * 30)
          + (aspirational_pass/52 * 260)
```

PASS = full points, PARTIAL = half points, FAIL = 0.

**Total max**: 60 + 30 + 260 = **350 pts**.

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
              C-28 [ ]  C-29 [ ]  C-30 [ ]  C-31 [ ]
              C-32 [ ]  C-33 [ ]  C-34 [ ]  C-35 [ ]
              C-36 [ ]  C-37 [ ]  C-38 [ ]  C-39 [ ]
              C-40 [ ]  C-41 [ ]  C-42 [ ]  C-43 [ ]
              C-44 [ ]  C-45 [ ]  C-46 [ ]  C-47 [ ]
              C-48 [ ]  C-49 [ ]  C-50 [ ]  C-51 [ ]
              C-52 [ ]  C-53 [ ]  C-54 [ ]  C-55 [ ]
              C-56 [ ]  C-57 [ ]  C-58 [ ]  C-59 [ ]
              Pass count: ___ / 52  ->  ___ / 52 * 260 = ___ pts  (of 260)

Composite score: ___ / 350
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
- **C-31**: C-15 is a prerequisite -- the BAD PLAN YAML block must exist. Scan the block for
  criterion tags. All seven criteria (C-01 through C-07) must each appear at least once as
  `# WRONG C-XX` within the block. Tags in inline gate comments outside the block, in the
  correction table, or in the scoring notes section do not count. The criterion must be tagged
  inside the BAD PLAN block itself. A block with all 4 essential tags but missing even one
  recommended tag fails C-31; satisfying C-16 and C-22 through other artifacts does not
  substitute for coverage within the BAD PLAN block.
- **C-32**: C-18 and C-28 are both prerequisites -- a correction table and the three-field gate
  structure must both be present. Assess per non-echo zone: does the production `gate:` sibling
  field carry a `# check correction table: gate values` annotation (or equivalent) at the field
  position? The correction bridge at `gate_fail:` / `gate_pass:` fields (which may exist via
  C-21) does not satisfy C-32. The bridge must appear on the production `gate:` key specifically.
  A zone with a correction bridge at the `skills:` placeholder but not at `gate:` passes C-21
  partial but not C-32. Partial credit when the production gate correction bridge is present at
  at least half the non-echo zones.
- **C-33**: C-26, C-27, C-28, C-30, and C-32 are all prerequisites. Assess per dependency-
  bearing zone: verify all four mechanisms coexist -- (a) `gate_fail:` has criterion tag (C-26),
  (b) production `gate:` has correction bridge (C-32), (c) zone header and skills: line both
  carry uniform dep reminder (C-27), (d) skills: line carries both dep reminder and correction
  bridge independently (C-30). A zone satisfying three of four fails C-33. Count dependency-
  bearing zones achieving all four; require >= 100% for full pass, >= 50% for partial. Echo and
  upstream-independent zones (no deps) are exempt from C-33 assessment.
- **C-34**: C-24, C-25, and C-26 are all prerequisites. Assess per non-echo zone's `gate_fail:`
  structural field. The compound annotation requirement means both the criterion tag AND the
  `Why:` explanation must appear at the field line itself -- not split between the field and an
  adjacent header comment. A `gate_fail:` field that carries `# WRONG C-04` (criterion tag
  present, satisfying C-26) but has `Why: execution-history check` only in a surrounding header
  comment satisfies C-26 but not C-34. The test: if you read only the `gate_fail:` line in
  isolation, does it carry both the criterion reference and the principle reason? If yes, C-34
  passes for that zone. Partial credit when compound annotation coexists at gate_fail: in at
  least half the non-echo zones.
- **C-35**: C-29 and C-31 are both prerequisites. Check each format independently. First,
  confirm C-31 passes (BAD PLAN block carries # WRONG C-05, # WRONG C-06, # WRONG C-07 tags).
  Second, confirm C-29 passes (correction table has at least one wrong-to-correct pair for each
  of C-05, C-06, C-07). C-35 passes only if both confirmations succeed. A prompt where the BAD
  PLAN has all 7 tags but the correction table has only essential-tier rows fails C-35 (and
  fails C-29). A prompt where the correction table has recommended-tier rows but the BAD PLAN
  only covers essential criteria fails C-35 (and fails C-31). There is no partial credit --
  the dual-format coverage either holds for both formats or it does not.
- **C-36**: C-31 is a prerequisite -- the BAD PLAN block must carry all 7 criterion tags before
  label accuracy is meaningful. Read the block's header comment (the label immediately above the
  YAML block, not a document-level section header). Check for scope-restricting language:
  "essential violations", "essential-tier failures only", "C-01 through C-04 violations", or
  any equivalent claim that excludes the recommended tier. If found, and C-31 passes (the block
  body actually does carry recommended-tier tags), the header label is inaccurate and C-36 fails.
  A header with no scope claim ("BAD PLAN", "wrong example", "violations") passes by default.
  A header explicitly claiming full coverage ("all-criterion violations", "C-01 through C-07")
  passes when C-31 also passes.
- **C-37**: C-22 and C-31 are both prerequisites. Locate every stage `name:` field in the BAD
  PLAN block that carries a C-06-violating value: namespace-only labels (`"scout"`, `"draft"`),
  generic labels (`"stage 1"`, `"phase A"`), or any name that does not describe evidence intent.
  Check whether each such `name:` field carries `# WRONG C-06` (or equivalent criterion tag) as
  an inline comment on the same line as the field. A criterion tag at the adjacent gate field,
  at the skills line, or in the zone header does not satisfy field-level annotation for that
  `name:` field. Partial credit when at least half the violating `name:` fields carry the
  criterion tag.
- **C-38**: C-36 and C-31 are both prerequisites. Read the BAD PLAN block header — the line
  immediately above the YAML block. Check not just for false restriction (C-36) but for
  affirmative coverage language: does the header contain a positive claim naming "all 7
  criteria," "C-01 through C-07," "essential and recommended," or equivalent? A header saying
  only "BAD PLAN" passes C-36 but fails C-38. A header saying "BAD PLAN — all 7 criteria"
  passes both. There is no partial credit; the affirmative claim is either present or absent.
- **C-39**: C-22 and C-31 are both prerequisites. Locate every `skills:` list entry in the BAD
  PLAN block that contains an invented or invalid skill name — any string not in Signal's 9-
  namespace catalog, any namespace-only entry (e.g., `scout:`), or any plain-English phrase
  (e.g., `"gather evidence"`). Check whether each such entry carries `# WRONG C-03` (or
  equivalent) as an inline comment on the same line. A criterion tag in the block header,
  adjacent to the gate field, or at the name: line does not satisfy field-level annotation for
  that skills entry. Partial credit when at least half the C-03-violating skills entries carry
  the field-level tag.
- **C-40**: C-34 and C-29 are both prerequisites. Confirm C-34 passes: every non-echo zone's
  `gate_fail:` structural field carries both `# WRONG C-04` and `Why:` at the field position.
  Then confirm C-29 passes: the correction table has at least one wrong-to-correct pair for
  each of C-05, C-06, and C-07. C-40 passes only if both confirmations succeed independently.
  A prompt with compound gate_fail: annotations but an essential-only correction table fails
  C-40 (C-29 fails). A prompt with recommended-tier correction table rows but missing compound
  annotations fails C-40 (C-34 fails). There is no partial credit.
- **C-41**: C-38 is a prerequisite. Read the BAD PLAN block header comment in full. Count the
  number of annotation types explicitly mapped to criterion numbers (affirmative header scope
  to C-38, skills-field co-location to C-39, name-field co-location to C-37, gate_fail: field
  co-location to C-26). A comment that says "see C-26, C-37, C-39, C-38" without naming what
  annotation type each criterion addresses does not satisfy C-41; the mapping must be from
  annotation type to criterion, not just a criterion list. Full pass: >= 3 annotation types
  mapped. Partial: exactly 2 mapped. Fail: fewer than 2 mapped or C-38 fails.
- **C-42**: C-26, C-37, and C-39 are all prerequisites. Locate any named section (a document
  header, a labeled block title, or a dedicated subsection with an explicit name) that appears
  before the BAD PLAN block and organizes field-level co-location criteria by field type. The
  section must present all three field types (gate_fail:, name:, skills:) with their criterion
  numbers and annotation tags in a structured format — table, enumeration, or labeled list with
  at least field, criterion, and tag columns or fields. A prose paragraph that mentions all
  three field types in running text without a structured table or enumeration does not satisfy
  C-42; the principle must be scannable as a reference. Partial credit when the named section
  covers exactly 2 of the 3 field types in structured format.
- **C-43**: C-07 and C-11 are both prerequisites. Locate the YAML template scaffold. Find the
  `strategy:` field (or equivalent plan-identity field). Check that it carries a non-empty
  pre-populated string value — not a comment, not an empty string, not a YAML null. The value
  must contain substantive placeholder text that frames the plan as a signal-gathering artifact.
  A `strategy: "..."` with only ellipsis does not satisfy C-43; a `strategy: "why this feature
  is worth the investment — ..."` with substantive framing does. There is no partial credit.
- **C-44**: C-41 is a prerequisite. Locate the C-41 annotation-type index in the BAD PLAN
  header. For each of the three co-location index entries (C-26/gate_fail:, C-37/name:,
  C-39/skills:), check whether the entry text includes the exact annotation tag string used at
  that field in the BAD PLAN block — e.g., `carries # WRONG C-04`, `carries # WRONG C-06`,
  `carries # WRONG C-03`. The tag string must appear as part of the index entry itself, not
  merely be inferable from the criterion number. A header that says `# C-26: gate_fail: field`
  satisfies C-41 (maps annotation type to criterion) but not C-44 (does not name the tag
  string). A header that says `# C-26: gate_fail: field carries # WRONG C-04` satisfies both.
  Full pass: all three co-location entries name their exact tag string. Partial: at least 2 of
  3 name their tag string.
- **C-45**: C-41 and C-42 are both prerequisites. First, locate the C-41 annotation-type
  index in the BAD PLAN header and check for an explicit reference to the C-42 named section
  by name or position (e.g., `see FIELD CO-LOCATION PRINCIPLE above`, `see co-location section`).
  Second, locate the C-42 named section and check for an explicit forward reference to the BAD
  PLAN header or the C-41 index (e.g., `the header below claims coverage`, `see BAD PLAN
  header index below`). Both directions must be present for C-45 to pass. A one-directional
  pointer -- only the C-41 header references C-42, or only C-42 references the BAD PLAN header
  -- fails C-45. There is no partial credit; bidirectionality is binary.
- **C-46**: C-41 is a prerequisite. Locate the final lines of the BAD PLAN YAML block (after
  the last stage in the block, not after the document-level BAD PLAN section). Check for an
  explicit footer comment that references co-location family completeness or the C-41 index.
  A footer that says `# end BAD PLAN` or `# --- end ---` without co-location language does not
  satisfy C-46. The comment must explicitly confirm that the annotation types enumerated in the
  header index are all present — e.g., `# Co-location family verified (C-41 index above)` or
  `# All three co-location field types annotated per C-41 index`. There is no partial credit;
  the exit marker is either present with co-location confirmation or it is not.
- **C-47**: C-44 is a prerequisite. Locate the gate_fail: entry in the C-41 annotation-type
  index (the entry for C-26). Read the Why: clause in that entry. Check whether it is fully
  spelled out (e.g., `Why: execution-history check, not artifact-verifiable`) or abbreviated
  (`Why: ...`, `Why: <reason>`, `Why: [explanation]`). Any abbreviated or placeholder form
  fails C-47 regardless of how precisely the tag string is specified (C-44 level). The full
  Why: text must match the actual annotation used at gate_fail: fields in the block body. Entries
  for C-37/name: and C-39/skills: carry no standard Why: clause and are not assessed under
  C-47. There is no partial credit.
- **C-48**: C-45 is a prerequisite. Read each individual C-41 index entry (not the header as
  a whole). Check whether each entry carries its own explicit back-reference to the C-42 section
  (e.g., `(rule declared in FIELD CO-LOCATION PRINCIPLE above)` appended to the entry text),
  as distinct from a single shared header-level pointer. Then locate the C-42 structured table
  or enumeration. Check whether each row carries a per-row forward reference to a specific
  numbered entry in the BAD PLAN header index (e.g., `See entry (1) in BAD PLAN header below`
  per row). Both directions must be per-entry; a single shared pointer in either direction fails
  C-48. There is no partial credit.
- **C-49**: C-41, C-42, and C-46 are all prerequisites. Read the label text of: (a) the C-41
  header index label, (b) the C-42 named section title, and (c) the C-46 exit footer comment.
  Check whether all three carry the same named protocol entity (e.g., all three reference
  "BLOCK SPECIFICATION PROTOCOL" or an equivalent shared protocol name). A prompt where C-41,
  C-42, and C-46 are each individually well-implemented but carry different names or no shared
  naming anchor fails C-49. The shared protocol name must appear explicitly in each component's
  label, not just be inferable from thematic coherence. There is no partial credit.
- **C-50**: C-48 is a prerequisite (per-entry bidirectional navigation must exist before table
  format is assessed). Locate the C-41 annotation-type index in the BAD PLAN header. Determine
  its format: is it a pipe-delimited markdown table with column headers, or is it a prose
  enumeration / indented list? A table must have at least four columns: field type, criterion,
  tag string (C-44 data), and per-entry C-42 back-reference (C-48 data). A Why: text column
  (C-47 data) is expected as a fifth column or merged into the tag-string column. Check that
  C-41, C-44, C-47, and C-48 all pass before awarding C-50 — a table that doesn't carry all
  required data types across those criteria fails both C-50 and its prerequisites. There is no
  partial credit; the format is either tabular or it is not.
- **C-51**: C-49 is a prerequisite — the named protocol must be established as a unified entity
  before its placement is assessed. Identify the C-42 named protocol declaration section. Then
  scan the document structure from the top: what is the first major structural section? If the
  protocol declaration section is not the first major section — if a YAML template section,
  correction table section, or any other content section precedes it — C-51 fails. A brief
  title header or introductory sentence before the protocol section does not count as a major
  section. The test: does the named protocol section appear before every implementation section
  in the document? There is no partial credit.
- **C-52**: C-50 and C-51 are both prerequisites. Locate the C-51 protocol declaration section.
  Scan it for explicit column schema language: does it name the four columns of the C-41 index
  table by purpose? All four columns must be named (field type, criterion, tag string, and
  per-entry back-reference — or equivalent purpose descriptions matching the actual table
  structure). A protocol section that merely states "Component 1 is a table" without naming
  columns fails C-52. A protocol section naming three of four columns partially describes the
  schema but does not satisfy C-52 — all columns the BAD PLAN header table actually uses must
  be named. There is no partial credit.
- **C-53**: C-52 is a prerequisite. Read the column schema declaration in the C-51 protocol
  section. Check whether it uses prescriptive/directive language — "must be," "will be,"
  "shall be," "is required to be," "format requirement: 4-column table" — or merely descriptive
  language — "is a 4-column table," "uses 4 columns," "the table has 4 columns." Descriptive
  language satisfies C-52 (schema named) but not C-53 (schema mandated). The test: does the
  declaration frame deviating from the schema as a protocol violation, or only as an
  inconsistency? Prescriptive framing converts deviation into violation; descriptive framing
  leaves deviation as a structural choice. There is no partial credit.
- **C-54**: C-53 is a prerequisite. Read the C-53 prescriptive declaration. After or alongside
  the MUST/SHALL mandate, look for explicit enumeration of forbidden alternatives: named format
  categories presented as violations (e.g., "prose enumeration, indented list, bulleted entries
  are protocol violations"). At least two named format categories must appear. A generic clause
  ("any other format is a violation," "non-table formats are prohibited") satisfies neither the
  enumeration requirement nor the named-category requirement — the alternatives must be
  identified by type. A single named alternative (e.g., "prose enumeration is a violation" with
  no other alternatives named) does not satisfy C-54. There is no partial credit.
- **C-55**: C-54 is a prerequisite. Locate the C-53/C-54 mandate section. After the positive
  mandate and the enumerated exclusions, look for an explicit multi-item self-review step that
  instructs the model to run per-item NOT/IS checks before completing Component 1. Each named
  C-54 exclusion category must appear as its own NOT item in the verification step; the IS item
  must confirm the required table format. The critical distinction from C-54: the C-54 exclusion
  list is a static declarative boundary (these formats are violations); the C-55 verification
  step is an active instructed check (run these items before completing Component 1). An
  exclusion list without an instructed verification step satisfies C-54 but not C-55. The
  self-review language must explicitly instruct the model to run the checks — e.g., "Before
  completing Component 1, confirm:" or "Self-review: check each item:" — not merely restate
  the exclusions in NOT form without an action instruction. There is no partial credit; every
  named C-54 exclusion must appear as a NOT item in the verification step.
- **C-56**: C-54 is a prerequisite. Locate the BAD PLAN block and identify the Component 1
  header (the comment or label immediately preceding the Component 1 table content). Read the
  header comment for two elements: (a) an explicit reference to the C-53 mandate, citing the
  protocol by name or citing the table format requirement ("Format: 4-column pipe table as
  mandated by [PROTOCOL NAME] above" or equivalent); and (b) an inline repetition of the C-54
  NOT list at the same header position ("NOT prose enumeration / NOT indented list / NOT bulleted
  entries" or equivalent format). Both elements must appear at the Component 1 header — a header
  carrying only the protocol name citation without the NOT list satisfies neither requirement;
  a header with only the NOT list without the protocol mandate citation also fails. The echo must
  be at the Component 1 header specifically, not in a surrounding section or block header. There
  is no partial credit.
- **C-57**: C-55 and C-56 are both prerequisites. Locate the Component 1 header. Confirm C-56
  passes first (static mandate citation + C-54 NOT list present). Then check for an additional
  active verification instruction at the same header position — a `# Verify before finalizing:`
  block or equivalent that enumerates each C-54 forbidden format as an individually checkable NOT
  item and ends with an IS confirmation. The active instruction must enumerate the same forbidden
  format categories as the C-55 verification step in the declaration section. A Component 1
  header carrying only the static echo (C-56 elements) without an active per-item instruction
  fails C-57. Confirm all four elements are at the Component 1 header: (a) mandate citation,
  (b) C-54 NOT list (static — C-56), (c) per-item NOT items (active — C-57), (d) IS confirmation
  item (active — C-57). There is no partial credit.
- **C-58**: C-55 is a prerequisite. Locate the protocol declaration section. Identify all
  constraint-bearing construction steps — steps that declare format requirements, exclusions, or
  behavioral rules. Count how many carry dedicated active verification checklists (explicit NOT/IS
  confirmation instructions distinct from the static rule text). The Component 1 format mandate
  is one step (C-55's domain); all other constraint-bearing steps must also have dedicated
  checklists for C-58 to pass fully. Full pass: every constraint-bearing step has an active
  verification checklist. Partial: at least half do but not all. Fail: only the Component 1 step
  has a checklist (C-55 level only). A prompt with one checklist (C-55) and all remaining steps
  as static declarations fails C-58.
- **C-59**: C-56 is a prerequisite. Locate the YAML template scaffold. Identify all template
  fields that carry format constraints (gates, skill entries, stage names, any field with
  declared format rules). For each constrained field, check whether the field position carries
  both (a) a positive mandate statement and (b) a NOT list of forbidden alternatives inline at
  the field. Fields with no format constraint are exempt. Full pass: every constrained template
  field carries both elements. Partial: at least half the constrained fields carry both elements
  but not all. Fail: mandate echoes appear only at the Component 1 header (C-56 level) with no
  additional template-field echoes. A template where only the Component 1 header carries the
  echo and all other constrained fields have only static annotations (C-21/C-26 level) fails C-59.

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
  other criteria are satisfied.
- **C-41 is aspirational** because header meta-commentary requires a second design layer at the
  header position — after C-38 establishes the affirmative coverage claim, C-41 adds the
  criterion-indexed directory that converts the header from a scope declaration into a navigation
  aid. The annotation-type-to-criterion mapping is implicit in the block; C-41 makes it explicit
  at the entry point, reducing model cross-reference load during block scanning.
- **C-42 is aspirational** because naming a family principle requires architectural awareness
  of the rubric's structural families, not just implementation of individual criteria. It is
  the first criterion that explicitly requires the prompt to present rubric structure as a named
  concept — converting three accumulated independent criteria into a single generalizable rule
  with a document home. Future field types that follow the co-location pattern become
  structurally predictable rather than requiring new standalone criteria.
- **C-43 is aspirational** because structural enforcement of recommended criteria is a design
  choice beyond what is required for correctness or quality. It demonstrates that the scaffold-
  first approach used for essential criteria (C-11) can extend to the recommended tier, raising
  the structural enforcement ceiling from essential-only to full-spectrum. A pre-populated
  `strategy:` field is the minimal viable extension: one field, one tier boundary crossed, one
  class of attention-dependent failure closed by default.
- **C-44 is aspirational** because embedding exact tag strings in the C-41 index requires a
  second design pass at the header — after the index maps annotation types to criteria (C-41),
  C-44 adds tag-form specification to each entry, converting the index from a navigational aid
  into a self-sufficient verification checklist. A model can confirm annotation compliance at
  each field type by checking for the exact stated string, eliminating the need to infer tag
  form from criterion context alone.
- **C-45 is aspirational** because bidirectional cross-section navigation requires both the
  C-41 index and the C-42 section to be designed with awareness of each other — each section
  must explicitly reference the other by name or position, creating a traversable structural
  loop. Without this mutual awareness, the two sections are parallel artifacts addressing the
  same principle independently; with it, they form a navigational unit where the principle
  declaration and the block-level index are linked in both directions.
- **C-46 is aspirational** because a BAD PLAN exit verification marker requires the prompt
  author to close the block explicitly, converting the block from an open scan into a bounded
  teaching unit. The exit marker also functions as a construction-time self-check: authoring
  the verification comment forces confirmation that the co-location annotations enumerated in
  the entry index are all present in the block body, catching omissions during construction
  rather than only at evaluation time.
- **C-47 is aspirational** because embedding the full unabbreviated Why: rationale in the
  C-41 header index requires the prompt designer to carry the criterion's explanatory principle
  all the way to the pre-scan level — not just the tag string form (C-44), but the semantic
  reason the tag exists. A header index entry with `Why: ...` teaches the index structure;
  a header index entry with `Why: execution-history check, not artifact-verifiable` teaches
  the principle. The distinction is the same as between C-10 (contrast pair present) and C-25
  (contrast pair with rationale): form without reason vs form with reason at the same location.
- **C-48 is aspirational** because per-entry bidirectional navigation requires structural
  awareness of the relationship between individual C-41 index entries and their corresponding
  C-42 principle rows — not just section-level awareness (C-45) but entry-level traceability.
  The design investment is higher: each entry in the index must carry its own back-reference,
  and each row in the C-42 table must carry a forward reference to its specific header entry.
  The payoff is fine-grained navigability: any annotation type can be traced from principle to
  instance and back without scanning neighboring entries.
- **C-49 is aspirational** because elevating C-41/C-42/C-46 to a named protocol requires the
  prompt designer to recognize that the three structural decisions share a common architectural
  identity — block header as entry spec, block body as teaching content, block footer as exit
  confirmation — and make that identity explicit through shared naming. Without C-49, the three
  criteria are achieved by accumulation; with C-49, they are unified by design intent. The
  named protocol also generalizes: a prompt designer who applies the BLOCK SPECIFICATION
  PROTOCOL to the co-location BAD PLAN block can apply the same pattern to any future teaching
  block that warrants header-spec + bounded-body + exit-confirmation structure.
- **C-50 is aspirational** because formatting the C-41 index as a table is a structural
  presentation decision beyond what C-41 through C-48 require. Those criteria specify the data
  each entry must contain; C-50 requires the container structure to be tabular, promoting each
  data type to an independently scannable column. The benefit is highest when entries carry
  multiple data types (field type + criterion + tag string + Why: + back-ref): a five-data-type
  prose sentence requires linear parsing while a five-column table row supports direct column
  access. The table format also makes the index a natural reference artifact — a model can
  return to the index during block scanning and look up specific columns without re-reading the
  full entry.
- **C-51 is aspirational** because positioning the named protocol section first requires a
  deliberate document architecture decision: the protocol is not discovered mid-document as a
  named organizing principle but is declared as the document's opening frame. This design choice
  inverts the typical prompt structure (rules-first, then template, then error artifacts) into
  principle-first architecture where the architectural model is declared before any section that
  instantiates it. The payoff is that every subsequent section is read with the protocol frame
  active — the model knows from document entry that the YAML template, correction table, and
  BAD PLAN block are protocol-instantiating components rather than independent teaching
  sections. C-51 is the document-level analog to C-11's scaffold-level structural enforcement:
  both move a requirement from mid-document discovery to up-front declaration.
- **C-52 is aspirational** because pre-declaring the column schema in the protocol section
  requires the first-position declaration (C-51) and the table format (C-50) to be designed as
  a coupled system rather than two independent structural choices. C-50 specifies that the index
  must be tabular; C-51 specifies that the protocol declaration must be first; C-52 requires
  the designer to recognize that first-position placement creates a natural slot to pre-specify
  what the table in Component 1 will look like. Without C-52, both criteria are satisfied
  independently without any connection between them; with C-52, the protocol section actively
  prepares the model for the table format it will encounter, converting dual exposure from an
  incidental design property into an explicit teaching mechanism.
- **C-53 is aspirational** because converting the schema pre-declaration from descriptive to
  prescriptive requires a further design decision: not just "here is what the table looks like"
  but "the table MUST look like this." The distinction matters for model behavior: a descriptive
  declaration informs; a prescriptive declaration constrains. When the column schema is mandated
  rather than described, deviating from it produces a protocol violation rather than a structural
  inconsistency — the framing change is small in text but significant in how a model interprets
  its compliance obligations. C-53 completes the conversion of C-50 from an observed pattern
  into an architecturally explicit requirement stated at the protocol level.
- **C-54 is aspirational** because enumerating forbidden alternatives requires the prompt
  designer to think not only about what the correct format IS but about what it ISN'T — a
  second-order design step that closes the design space in the negative direction. C-53 issues
  a positive mandate; C-54 adds named exclusions that make the mandate's boundary explicit
  rather than implicit. A model reading only "MUST be a 4-column table" must infer which other
  formats are excluded; a model reading "MUST be a 4-column table; prose enumeration, indented
  list, and bulleted entries are protocol violations" has the boundary directly stated. The
  negative enumeration is also a generalization of the co-location family's design philosophy:
  just as each co-location criterion names not only the correct annotation pattern but also
  what would violate it, C-54 names not only the correct format but what would violate it —
  applying the same explicit-boundary discipline to the table format requirement itself.
- **C-55 is aspirational** because converting the static exclusion list into an active
  per-item verification protocol requires the prompt designer to recognize that a declarative
  rule and an active confirmation step serve different compliance functions. C-54 closes the
  design space declaratively; C-55 converts each declared exclusion into a confirmation action
  the model must perform. The mechanism is the same as C-14's deletion-resistance annotations:
  C-14 converts structural slot pre-positioning from a suggestion into a labeled constraint;
  C-55 converts each format exclusion from background knowledge into a per-item check. The
  NOT/IS structure makes the verification protocol linear and exhaustive — each forbidden
  category gets its own line, ensuring none are skipped — and the IS item at the end confirms
  the positive requirement, bracketing the audit. A model that runs the four-item check before
  finalizing Component 1 cannot produce a prose enumeration or bulleted list and claim it
  satisfies the mandate without the check explicitly failing.
- **C-56 is aspirational** because echoing the mandate at the application site requires the
  prompt designer to apply the co-location discipline — state the rule at both its declaration
  site and its use site — to the format requirement itself. C-26 through C-39 apply co-location
  to annotation tags at YAML field positions; C-56 applies the same principle to the top-level
  format mandate that governs Component 1's structure. The design investment is distinct from
  C-55: C-55 converts the exclusion list into an active verification step at the declaration
  site; C-56 restates both the mandate and the exclusion list at the application site. Together
  they ensure the model encounters the format requirement at three independent locations: the
  mandate declaration (C-53), the active verification step (C-55), and the Component 1 header
  echo (C-56). Each location is sufficient alone to inform the format requirement; three
  independent exposures make non-compliance structurally improbable. C-57 adds a fourth
  exposure by also echoing the active verification trigger at the application site.
- **C-57 is aspirational** because extending C-56's co-location from static reference to active
  directive requires recognizing that two distinct mechanisms govern format compliance at the
  declaration site — the passive boundary (C-56's target) and the active verification trigger
  (C-55's target) — and that co-location should cover both, not just the static element. A model
  skipping the protocol section and reading only the Component 1 header encounters the exclusion
  boundary via C-56's static echo but not the per-item confirmation step unless C-57 is also
  present. C-57 closes the document-skip gap: the active audit protocol is available at both
  the declaration site (C-55) and the application site (C-57), making the verification step
  document-position-independent. The pattern generalizes the co-location family: co-locate not
  just the rule but also the enforcement action that activates the rule.
- **C-58 is aspirational** because universal per-step active verification requires the prompt
  designer to treat the C-55 active-verification mechanism not as a special exception for the
  format mandate but as a general document discipline applied to every constraint. The design
  investment is proportional to the number of constraint-bearing construction steps: each
  additional step requires its own NOT/IS checklist drafted at specificity level. Without C-58,
  the active-verification pattern is a local optimization at the format mandate; with C-58, it
  is a document-wide principle where every constraint is an audit step rather than a background
  fact. This raises the cognitive reliability ceiling for the entire protocol: a model following
  C-58-compliant instructions runs an active confirmation step at every constraint boundary, not
  only at the format mandate, making constraint-skipping behavior structurally difficult across
  the entire document.
- **C-59 is aspirational** because saturating every constrained YAML template field with a
  co-located mandate echo requires the prompt designer to extend C-56's Component-1 echo into a
  template-wide discipline, applying the same principle to every field position rather than a
  single high-stakes component. The design investment scales with template complexity: each
  constrained field requires both a mandate statement and a NOT list drafted at field-level
  specificity. The payoff is symmetric with the cost: a model authoring any constrained template
  field encounters the relevant mandate and exclusions locally, without needing to recall the
  governing rule from a remote declaration section. C-59 completes the co-location saturation
  that C-26/C-37/C-39 begin at annotation-tag level and C-56 establishes at component-header
  level, making the principle that rules belong at both declaration and application sites
  operative across the entire template surface.
