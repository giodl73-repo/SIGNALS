## New Excellence Patterns in Round 4

Two distinct patterns emerge from the scorecard:

**Pattern 1 — Field-Name Framing** (from C-06 differential)
V-02 gets PARTIAL on C-06 specifically because schema field names use discovery-register vocabulary ("Expected"/"Finding"). V-01, V-03, V-04, V-05 all pass because their field names encode correction vocabulary ("Inherited assumption," "What the next team would build wrong"). The mechanism: framing is won or lost at schema design time, before any rules fire. Discovery-register field names impose a ceiling on future-team framing — rules must work harder to achieve what correction-register vocabulary provides by default.
→ **C-17: Correction-Register Schema Design**

**Pattern 2 — Audit-Layer Enforcement** (from C-07 triple-enforcement in V-05)
V-05 uniquely achieves triple-enforcement because the portability audit creates a third layer: it names specific anti-pattern phrases and flags them as automatic rewrite triggers. Two-enforcement (field definition + rules) prohibits bad output; three-enforcement (+ audit scan) catches drift after the fact. The audit loop is structurally distinct from prohibition.
→ **C-18: Verification Audit Layer**

---

```markdown
# topic-echo-rubric-v5-2026-03-16.md

## Rubric: `topic-echo` — v5

**Skill**: `topic:echo`
**Version**: v5
**Date**: 2026-03-16
**Criteria count**: 18 (4 essential / 3 recommended / 11 aspirational)

**Formula**:
`(essential_pass/4 × 60) + (recommended_pass/3 × 30) + (aspirational_pass/11 × 10)`

PARTIAL = 0.5. Max composite = 100. Aspirational tier is a ceiling bonus,
not a score driver. Each full aspirational pass ≈ 0.91 pts.

**Band thresholds**: Gold ≥ 85 + all_essential_pass | Silver ≥ 70 +
all_essential_pass | Bronze ≥ 55 + all_essential_pass | Miss < 55 or any
essential FAIL

---

## Essential Criteria (60 pts — output fails without these)

### C-01 | Surprise Orientation
- **Weight**: essential
- **Category**: correctness
- **Text**: The output contains only genuine surprises — findings that
  contradict, reverse, or significantly complicate what was believed or
  designed before the signals arrived. Confirmations (findings that match
  prior expectations) are excluded from the surprise entries.
- **Pass condition**: Every entry in the output names something that was
  not predictable from pre-investigation design materials. An entry that
  restates what the spec already said fails. An entry framed as "this
  confirmed X" fails. PARTIAL if one entry is borderline but the
  remainder are genuine surprises.

### C-02 | Source Signal Tracing
- **Weight**: essential
- **Category**: correctness
- **Text**: Each surprise names the specific signal artifact or skill type
  that produced it. Vague attribution ("the research", "the signals",
  "investigation") is not acceptable. Tracing must be specific enough
  that a reviewer could locate the source artifact.
- **Pass condition**: Every surprise entry names a specific artifact (e.g.,
  `prove-interview-variate-R3`, `flow-resilience`) or skill type with
  enough precision to locate the source. "The signals" or "our research"
  fails. PARTIAL if one entry has weak attribution but the rest are
  specific.

### C-03 | Design Impact Assessment
- **Weight**: essential
- **Category**: depth
- **Text**: Each surprise states its consequence for design: what component,
  flow, constraint, or decision must change as a result. An entry that
  merely reports an interesting finding without naming what changes is
  incomplete.
- **Pass condition**: Every surprise entry contains a design impact clause
  that names a specific artifact, component, or decision. "This is
  interesting" or "worth noting" fails. PARTIAL if one entry has a weak
  impact clause but the rest are specific.

### C-04 | Named and Countable Surprises
- **Weight**: essential
- **Category**: format
- **Text**: Each surprise is a discrete, titled item. The output contains
  at least 2 surprises. A single observation is not a synthesis.
- **Pass condition**: Output has ≥ 2 surprises, each with a distinct name
  or title. An undifferentiated paragraph fails. PARTIAL if titles are
  present but two entries are substantially redundant.

---

## Recommended Criteria (30 pts — output is weak without these)

### C-05 | Surprise Diversity
- **Weight**: recommended
- **Category**: coverage
- **Text**: The output draws entries from at least 2 distinct signal
  namespaces. A synthesis built entirely from one signal type lacks the
  cross-namespace tension that makes an echo useful.
- **Pass condition**: ≥ 1 entry attributed to each of ≥ 2 distinct
  namespaces; schema explicitly requires multi-namespace sourcing.
  PARTIAL if a cross-signal requirement is present and structurally
  encourages multi-namespace reading, but no constraint enforces ≥ 2
  namespaces explicitly.

### C-06 | Future-Team Framing
- **Weight**: recommended
- **Category**: orientation
- **Text**: All schema field names, section labels, and output vocabulary
  are in the correction register — addressing what the next team inherits
  — rather than the discovery register — reporting what the current team
  found. Discovery-register vocabulary in field names imposes a ceiling
  on future-team framing that rules alone cannot lift.
- **Pass condition**: Zero discovery-register field names ("Expected",
  "Finding", "What we found", "Our result") in schema. All field labels
  encode future-team purpose. Vocabulary "we found" / "we learned" absent
  from schema structural elements. PARTIAL if output rules orient toward
  future-team purpose but schema field names retain discovery vocabulary,
  requiring extra rule enforcement to achieve framing.

### C-07 | Impact Specificity
- **Weight**: recommended
- **Category**: depth
- **Text**: The impact clause names a specific component, flow, or decision.
  Vague impact language is prohibited and enforcement is structural —
  prohibition stated in both field definition and in rules (double-
  enforcement).
- **Pass condition**: Impact clause field definition names specific
  artifact/component/decision; named prohibitions present ("worth noting",
  "bears watching", "has implications for design" each explicitly called
  out as failures); Rule enforcement cross-validates the field definition.
  PARTIAL if prohibition stated once (in field definition or in rules, not
  both).

---

## Aspirational Criteria (10 pts ceiling — signals of excellence)

### C-08 | Cross-Signal Synthesis
- **Weight**: aspirational
- **Category**: synthesis
- **Text**: At least one entry names two distinct signal sources and a
  named convergence gap — an insight that neither source alone could have
  surfaced.
- **Pass condition**: At least one entry states explicitly "Neither
  [signal A] nor [signal B] alone revealed this" and names the gap.
  PARTIAL if a cross-signal entry is present but the convergence gap is
  implied rather than named.

### C-09 | Counterfactual Awareness
- **Weight**: aspirational
- **Category**: depth
- **Text**: Each entry contains a clause naming the specific wrong outcome
  if this surprise is not incorporated — what the next team would build,
  decide, or assume incorrectly.
- **Pass condition**: Every entry has a named wrong-outcome clause
  ("without this, the next team would build [X] when [Y] is required").
  PARTIAL if C-15 passes — structural counterfactual induction shapes
  orientation toward wrong-outcome awareness pervasively, even without an
  explicit per-entry clause. FAIL if neither explicit clause nor structural
  induction is present.
- **Cross-reference**: C-15 PASS → C-09 PARTIAL (structural induction
  counts toward counterfactual awareness but cannot reach full pass
  without per-entry clause).

### C-10 | Epistemic Delta Tracing
- **Weight**: aspirational
- **Category**: depth
- **Text**: Each entry names the pre-investigation belief and the specific
  directional delta produced by the signals — not "we didn't know" but
  "we believed X; signals show Y."
- **Pass condition**: Entries include a field or clause stating the prior
  belief or implication of existing materials, and name the direction and
  nature of the shift. PARTIAL if prior belief is named but delta
  direction is unstated or magnitude is vague.

### C-11 | Non-Derivability Verification
- **Weight**: aspirational
- **Category**: correctness
- **Text**: The schema includes an explicit per-entry gate verifying that
  each surprise is not derivable from pre-signal materials by careful
  reading alone. Entries that fail the gate are excluded.
- **Pass condition**: Schema contains a named non-derivability gate (e.g.,
  "could a careful reader of the existing materials have predicted this
  without running signals?") applied per entry; exclusion rule stated
  for entries that fail. PARTIAL if non-derivability is mentioned in
  framing rules but no per-entry gate is applied.

### C-12 | Root-Cause Grouping
- **Weight**: aspirational
- **Category**: structure
- **Text**: Surprises are grouped or annotated by root-cause category —
  reflecting failure modes or knowledge gaps — rather than by topic.
- **Pass condition**: Grouping annotation present; categories reflect
  failure modes, not topic headings; non-derivability maintained within
  each category. PARTIAL if grouping is structurally encouraged but
  categories are topic-organized rather than failure-mode organized.

### C-13 | Signal Coverage Assessment
- **Weight**: aspirational
- **Category**: meta
- **Text**: Output includes a meta-assessment naming which namespace areas
  contributed entries, which are absent, and whether coverage is
  sufficient to claim echo completeness.
- **Pass condition**: Explicit meta-section names contributing signal
  types, identifies uncovered namespaces, and states a completeness
  judgment. PARTIAL if aggregate signal count or source list is provided
  but no completeness judgment is made.

### C-14 | Redundancy Elimination
- **Weight**: aspirational
- **Category**: correctness
- **Text**: No two entries name the same underlying correction. Degree-
  variants and paraphrases of the same correction are merged or excluded
  with rationale.
- **Pass condition**: Schema includes an explicit redundancy check; entries
  that are degree-variants of each other are merged or excluded with
  stated rationale. PARTIAL if entries are distinct but overlap is not
  explicitly checked and no rationale for near-duplicate inclusion is
  given.

### C-15 | Structural Counterfactual Induction
- **Weight**: aspirational
- **Category**: orientation
- **Added**: v4
- **Text**: The schema, role framing, or vocabulary structurally induces
  counterfactual thinking across all entries without requiring an explicit
  per-entry clause. The effect is pervasive — it shapes the entire
  orientation of the skill — not local to a single field.
- **Pass condition**: Role label, schema field names, or framing vocabulary
  collectively establish "what would the next team get wrong?" as the
  default lens, applied across all entries. Effect must be pervasive.
  PARTIAL if structural induction is present but confined to one schema
  section or role label only.
- **Cross-reference**: C-15 PASS → C-09 PARTIAL (structural induction
  is mechanically distinct from explicit per-entry clause; counts toward
  but cannot satisfy C-09 fully).

### C-16 | Misunderstanding-Category Synthesis
- **Weight**: aspirational
- **Category**: structure
- **Added**: v4
- **Text**: Surprises are grouped by category of misunderstanding — the
  type of blind spot in how the original design materials framed the
  problem — rather than by topic or root-cause alone. Misunderstanding-
  category grouping reveals the shape of the original team's ignorance,
  not merely a topic-organized list of gaps.
- **Pass condition**: Grouping categories reflect blind-spot types (e.g.,
  "scope assumption", "timing assumption", "actor assumption"); non-
  derivability constraint enforced within each category. PARTIAL if
  grouping is by misunderstanding category but non-derivability is not
  enforced; the grouping mechanism itself is an excellence signal even
  without full pass.

### C-17 | Correction-Register Schema Design
- **Weight**: aspirational
- **Category**: orientation
- **Added**: v5
- **Text**: Schema field names and structural labels are drawn from the
  correction register — encoding what the next team inherits — rather
  than the discovery register — encoding what the current team found.
  When field names use correction vocabulary, future-team framing is the
  default and requires no extra rule enforcement. When field names use
  discovery vocabulary, framing must be imposed through rules and may
  still fall short. The framing battle is won or lost at schema design
  time.
- **Pass condition**: Zero discovery-register field names ("Expected",
  "Finding", "What we found", "Our result", "Discovery") appear in schema
  structure. All field labels encode future-team purpose ("Inherited
  assumption", "What the next team would build wrong", "What the next
  team must decide before proceeding"). PARTIAL if schema uses correction
  vocabulary in most fields but retains one or more discovery-register
  labels. FAIL if schema field names are neutral or use discovery
  vocabulary throughout.
- **Cross-reference**: C-17 FAIL or PARTIAL → C-06 cannot exceed PARTIAL
  (discovery-register schema imposes a ceiling on future-team framing
  regardless of rule enforcement quality).

### C-18 | Verification Audit Layer
- **Weight**: aspirational
- **Category**: enforcement
- **Added**: v5
- **Text**: The skill includes an explicit audit or verification pass —
  structurally distinct from field definitions and prohibitions — that
  scans the draft output for named anti-pattern phrases and flags them
  as automatic rewrite triggers. This constitutes a third enforcement
  layer: field definition (layer 1) establishes the standard; named
  prohibitions in rules (layer 2) state what to exclude; audit scan
  (layer 3) catches drift that prohibitions miss and creates a self-
  correcting feedback loop. Two-enforcement prohibits bad output;
  three-enforcement catches it after the fact.
- **Pass condition**: Skill includes a named audit, portability-check, or
  verification-pass section that lists ≥ 3 specific anti-pattern phrases
  (e.g., "worth noting", "has implications for design", "signals
  indicated", "bears watching") and prescribes automatic rewrites when
  found; audit is applied to the full output, not scoped to a single
  field. PARTIAL if audit layer is present but names fewer than 3
  anti-pattern triggers or is scoped to one field only. FAIL if
  enforcement relies solely on field definitions and prohibitions with no
  verification pass.
```
