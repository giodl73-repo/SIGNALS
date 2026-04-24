# program-plan Rubric — v4

Evaluates a `program:plan` prompt against Signal's plugin contract and evidence-quality bar.
11 aspirational criteria, 4 essential, 3 recommended. Total max: **145 pts**.

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
  `trace:contract`). Invented namespaces, invented skill names within valid namespaces, and
  skills listed without namespace qualification all fail.
- **Pass condition**: Every skill reference resolves to a real Signal skill. A single invented
  name (e.g., `scout:analysis`, `build:deploy`) fails the entire criterion.

### C-04 — Evidence-State Gates (Not Execution State)
- **Weight**: essential
- **Category**: correctness
- **Text**: Every non-echo stage gate expresses evidence state -- what artifacts must exist or
  what conditions must be verifiably true -- not execution state. Evidence-state gates name
  artifacts by type (`scout-feasibility artifact present`), count signals (`>= 2 scout signals`),
  or describe a checkable condition (`no blocking feasibility concerns identified`).
  Execution-state gates describe what was done: `"done"`, `"complete"`, `"all skills run"`,
  `"proceed"`, `"stage complete"`, `"tasks finished"`. These fail because the next-phase owner
  cannot verify them.
- **Pass condition**: Every non-echo gate contains at least one artifact name, signal count, or
  verifiable evidence condition. A plan where even one gate consists solely of execution-state
  language fails.

---

## Recommended Criteria (improve output quality -- 30 pts)

### C-05 -- Namespace Dependency Order Respected
- **Weight**: recommended
- **Category**: correctness
- **Text**: Stages follow Signal's namespace dependency order. `scout` skills precede `draft`
  skills; `draft:spec` precedes `review:*`; `review:*` precedes `flow:*` and `trace:*`;
  `listen:*` and `topic:*` appear after simulation stages. The canonical ordering is:
  `scout -> draft -> review/prove -> flow/trace -> listen/topic -> echo`. A stage with `review:design`
  placed before any `draft:spec` stage violates this order because review requires a spec.
- **Pass condition**: No stage contains skills whose dependencies have not been produced by a
  prior stage. Minor exceptions (e.g., `prove:websearch` in a discovery stage) are acceptable
  where the stage scope makes the ordering intent clear.

### C-06 -- Descriptive Stage Names
- **Weight**: recommended
- **Category**: format
- **Text**: Stage names are human-readable phase labels describing team intent -- not namespace
  names reused as labels, not generic indices, not skill names. Passing: `discovery`,
  `market-scan`, `design`, `expert-review`, `simulation`, `feedback-preview`. Failing: `scout`,
  `draft`, `stage1`, `step-2`, `flow`.
- **Pass condition**: Every non-echo stage name would communicate phase intent to a stakeholder
  unfamiliar with Signal namespaces. Any stage named identically to a Signal namespace or using
  generic position indices fails.

### C-07 -- Plan-Not-Executor Identity Present
- **Weight**: recommended
- **Category**: behavior
- **Text**: The output makes clear the program is a plan, not an executor. This may appear as
  a YAML comment (`# this program is a plan, not an executor; skills run standalone`), in the
  `strategy` field framing the program as a decision-support artifact, or in a verification note
  accompanying the YAML. The plan does not describe stages as automatically running skills or
  present the program as a pipeline executor.
- **Pass condition**: At least one place in the output explicitly marks the program as a plan
  and not an automation layer, or the strategy field describes what decision the evidence
  informs. Plans that frame stages as execution steps or imply skills run automatically fail.

---

## Aspirational Criteria (raise the bar -- 55 pts)

### C-08 -- At Least One Quantified Gate
- **Weight**: aspirational
- **Category**: depth
- **Text**: At least one non-echo gate contains a numeric threshold that makes it
  machine-checkable in principle: `">= 2 scout signals present"`, `"0 P0 findings open"`,
  `">= 3 review artifacts"`, `"draft-spec and >= 1 feasibility signal archived"`. Quantified
  gates transform qualitative evidence conditions into verifiable pass/fail checks and signal
  the program was designed to be evaluated, not just read.
- **Pass condition**: At least one gate uses `>=`, `<=`, `=`, or an explicit count
  (`"0 blocking findings"`, `"at least 2 signals"`). Plans where all gates are qualitative
  only fail.

### C-09 -- Deliberate Evidence Arc
- **Weight**: aspirational
- **Category**: depth
- **Text**: The stage sequence forms a coherent investigation arc -- broad exploration first
  (scout, draft), focused validation and depth next (review, prove, flow, trace), synthesis
  last (listen, topic) -- rather than a flat skill accumulation or purely topological sort.
  The arc may be made visible via YAML layer-divider comments, stage name groupings that
  reflect the arc (e.g., `discovery` -> `design` -> `simulation` -> `feedback-preview`), or a
  `strategy` field describing the investigation trajectory. The structure shows the plan was
  shaped by a deliberate evidence strategy, not just namespace defaults.
- **Pass condition**: The plan has at least 3 substantive stages (plus echo) organized so that
  earlier stages build the foundation later stages require. The progression from breadth to
  depth to synthesis is visible in stage sequencing and stage naming. Plans that pack all skills
  into one stage or randomize namespace ordering fail.

### C-10 -- Failure-Mode Contrast Pair
- **Weight**: aspirational
- **Category**: depth
- **Text**: The prompt includes at least one BAD/GOOD (or WRONG/CORRECT) example pair that
  makes a concrete essential failure mode visible at authoring time. Target failure modes:
  inertia gate (`"done"` vs artifact-naming gate), missing echo contract, invented skill name,
  or bad YAML structure. The contrast works by showing the failure as an output shape the model
  must not produce -- not by stating it as an abstract prohibition. Inline `# BAD` / `# GOOD`
  comments within a YAML skeleton count; a dedicated contrast section counts; a split column
  table counts. Evidence from R1: V-05 inertia contrast (BAD YAML gate vs GOOD gated YAML)
  produced the clearest C-04 pass of any variate; V-02 inline BAD/EXAMPLE comments produced
  reliable C-04 passes at lower scaffolding cost.
- **Pass condition**: At least one failure mode is illustrated with both a wrong example and
  its correction. A single prohibition rule without a counterexample does not pass. The contrast
  must be anchored to an essential criterion (C-01 through C-04).

### C-11 -- Structural Enforcement of Essential Requirement
- **Weight**: aspirational
- **Category**: depth
- **Text**: At least one essential requirement is enforced through document structure rather
  than prose rule alone. A structural enforcement is one where the wrong output is made
  difficult or impossible to produce within the scaffold the prompt provides -- not merely warned
  against. Examples: a YAML skeleton where the echo field appears with `# REQUIRED` at its
  exact position, making omission a deliberate deletion; lifecycle bands (Prove It / Design It
  / Simulate It / Listen Ahead) that embed namespace dependency order as section headers; a
  per-band skill catalog that makes only valid namespaced skills visible at the point of
  authoring. A rule that says "echo must be last" is not structural enforcement. A template
  that places echo last in the skeleton is. Evidence from R1: V-04's lifecycle bands converted
  C-05 from PARTIAL (V-01, V-02, V-03) to PASS by making namespace order a structural property
  of the output form; V-02's `# REQUIRED` echo annotation converted C-02 from a memorable rule
  into an unforgettable template slot.
- **Pass condition**: At least one essential requirement is embedded in the structural scaffold
  such that following the scaffold produces correct output without needing to remember the rule.
  Prose rules only, however clearly stated, do not pass this criterion.

### C-12 -- Dual-Anchor Reinforcement of Essential Criteria
- **Weight**: aspirational
- **Category**: depth
- **Text**: Each essential criterion (C-01 through C-04) is introduced through at least two
  independent mechanisms in the prompt -- such that the model would need to skip two separate
  locations to miss the requirement. Mechanisms include: opening rule statement, inline YAML
  comment at the relevant field, worked example, BAD/GOOD contrast, band framing, `# REQUIRED`
  annotation, strategy-field hint. Belt-and-suspenders redundancy prevents single-point-of-
  failure where the model misses a requirement by skipping a section. Evidence from R1: V-01
  (header + YAML comment dual reinforcement on C-07), V-04 (band framing + per-band YAML on
  C-02 and C-05), V-05 (opening paragraph + YAML comment on C-07; hard rules + GOOD example
  on C-02) all show this pattern raising scores on criteria that V-02 and V-03 only partially
  satisfied.
- **Pass condition**: Each of C-01, C-02, C-03, and C-04 can be independently derived from
  at least two non-overlapping locations in the prompt. A prompt that states all four rules
  once in a single rules section without structural or inline reinforcement does not pass.
  Partial credit (half points) applies when dual-anchoring covers at least 2 of the 4
  essential criteria.

### C-13 -- Arc as Structural Organizing Spine
- **Weight**: aspirational
- **Category**: depth
- **Text**: The evidence arc (breadth-first exploration -> focused validation -> synthesis) is
  the structural backbone of the prompt, not merely described in prose or a `strategy` field.
  The prompt's primary organizational structure -- question bank grouped by arc layer, lifecycle
  band section headers, top-level phase groupings -- directly corresponds to arc layers, so a
  model navigating the scaffold encounters the arc before reaching the skill lists. This goes
  beyond C-09 (arc visible in stage naming or strategy) to require the arc to be the axis the
  rest of the prompt is organized around. Evidence from R2: V-03's question bank grouped by
  arc layer (Discovery -> Design -> Validation -> Simulation -> Feedback) made the entire prompt
  structure an expression of the arc; V-04's lifecycle bands (Prove It / Design It / Simulate It
  / Listen Ahead) used the arc phases as first-class section dividers. V-01 and V-02 declared
  the arc in comments and step instructions but organized the prompt as flat numbered steps,
  earning C-09 PARTIAL.
- **Pass condition**: The arc layers correspond to first-class structural divisions (sections,
  bands, question clusters, template headers) that the rest of the prompt content hangs off.
  A model reaching the skill lists necessarily navigates through the arc structure. Arc declared
  in a note, comment, or strategy field while the prompt itself is flat or numerically indexed
  does not pass.
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

---

## Scoring Formula

| Tier | Weight | Criteria | Points each | Max |
|------|--------|----------|-------------|-----|
| Essential | 60 pts | C-01, C-02, C-03, C-04 | 15 | 60 |
| Recommended | 30 pts | C-05, C-06, C-07 | 10 | 30 |
| Aspirational | 55 pts | C-08 through C-18 (11 criteria) | 5 | 55 |

```
composite = (essential_pass/4 * 60)
          + (recommended_pass/3 * 30)
          + (aspirational_pass/11 * 55)
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
              C-16 [ ]  C-17 [ ]  C-18 [ ]
              Pass count: ___ / 11  ->  ___ / 11 * 55 = ___ pts  (of 55)

Composite score: ___ / 145
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
- **Failure fast-paths** cover the four most common failure modes from the variate scoring
  rounds: no YAML, bad echo, invented skills, all-execution gates.
- **Scoring total is 145** (not 130) because the aspirational tier expanded from 8 to 11
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
