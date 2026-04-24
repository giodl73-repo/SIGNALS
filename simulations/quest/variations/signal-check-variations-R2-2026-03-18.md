Written to `simulations/quest/variations/signal-check-variations-R2-2026-03-18.md`.

---

## signal-check R2 — 5 Variations

**Axis matrix:**

| V | Label | Axis | Key move |
|---|-------|------|----------|
| V-01 | Explicit absence enforcement | Single: C-13 | Prohibition language at every dimension — "silence does not pass", "absence must be declared" |
| V-02 | Strict skill-format enforcement | Single: C-11 | `/namespace:skill` constraint declared in preamble, repeated at every action field |
| V-03 | Lifecycle emphasis shift | Single: depth inversion | CAUSAL GAP + SEQUENCE get multi-step procedures and examples; STALENESS + COHERENCE compressed to compact blocks |
| V-04 | Absence + skill format | Combination: C-13 + C-11 | Standing Rules block upfront with both constraints; reinforcing enforcement throughout |
| V-05 | Full v2 canonical stack | All three + R1 V-05 base | Preflight scaffold + CAUSAL GAP first + status tags + absence prohibition + skill format constraint + terminal guide |

**What's new vs. R1:** R1 tested status tags, CAUSAL GAP-first order, and coaching scaffold — and the R1 V-05 already achieved the structural ceiling for v1. R2 targets the three new v2 criteria (C-11, C-12, C-13) that R1 didn't have dedicated mechanisms for. V-01 tests C-13 solo (does prohibition alone close the silence failure mode?). V-02 tests C-11 solo (does an upfront format constraint propagate to inline references?). V-03 tests whether depth allocation affects pattern detection. V-04 and V-05 combine toward the v2 ceiling.

**Research questions:**
1. Does absence prohibition alone close C-13, or do structural slots (Basis field forcing "no artifact found") do the same work implicitly?
2. Does a preamble-level skill-format rule propagate to inline references, or do action fields still drift to bare names?
3. Does depth inversion improve C-09 cross-pattern detection without degrading C-06/C-07 on compressed dimensions?
 which looks like "the dimension was analyzed and found
  clear" rather than "no evidence was checked." V-01 adds a prohibition pattern to each dimension:
  "if no artifact covers this area, write the absence — do not leave the section blank or imply evidence
  exists." This is tested solo to see if prohibition alone is sufficient for C-13 compliance, or whether
  structural slots (like those in V-04/V-05) are also needed.

- **V-02 (strict skill-format enforcement):** C-11 requires that every skill reference in the output —
  not just in the MISSING SIGNAL GUIDE but in inline recommendations, action fields, and the readiness
  summary — uses the `/namespace:skill` format. R1 V-04/V-05 included the MISSING SIGNAL GUIDE with
  correct format examples, but did not explicitly prohibit bare skill names in other parts of the output.
  V-02 adds a format constraint at the preamble level and repeats it at the action field level in each
  section. This tests whether format compliance is achieved through constraint propagation or only at
  the terminal guide.

- **V-03 (lifecycle emphasis shift):** CAUSAL GAP and SEQUENCE are the hardest dimensions and most
  commonly open. STALENESS and COHERENCE are comparatively mechanical. V-03 allocates more instructional
  depth to the hard dimensions (longer criterion definitions, more explicit examples, more detailed
  step sequences) while compressing the mechanical ones to a single compact format block. This tests
  whether depth allocation affects cross-dimension pattern detection (C-09) and whether compressed
  sections still satisfy C-06/C-07 for the easy dimensions.

---

## V-01: Explicit absence enforcement (C-13 axis)

**Axis:** C-13 — every dimension where relevant evidence is absent must use explicit absence language.
Prohibition patterns added to each section: "If no artifact covers this, declare the absence — do not
leave the section blank, do not hedge, do not imply evidence exists."

**Hypothesis:** C-13 failures happen silently — a dimension that finds no evidence simply writes nothing,
which reads as "this dimension is clear" rather than "this dimension has no evidence to check." Adding
explicit prohibition language ("silence does not pass") at each section forces the model to distinguish
"checked and found nothing" from "found evidence and reported it." This is tested solo to determine
whether prohibition alone closes C-13 without requiring structural slots.

```
You are running /signal-check for topic: {topic}.

This is a coaching check, not a gate. It surfaces what looks inconsistent so you
can decide what to address before committing. Nothing here blocks you from proceeding.

=== ARTIFACT INVENTORY ===

Use Glob to find all signal artifacts for {topic}:
  Pattern: simulations/**/*{topic}*.md

Build an inventory table:

  | # | Artifact path | Namespace | Signal type | Date |
  |---|--------------|-----------|-------------|------|

Artifact count: {N}

If no artifacts are found: write "No signal artifacts found for {topic}. Analysis
cannot proceed." and stop.

=== READINESS SUMMARY ===

[Write this section last -- place it first in the final artifact.]

2-4 sentences: overall signal health for {topic}, which dimensions are clear, which have
gaps, and whether signals support proceeding or recommend addressing a gap first.
Frame as advisory briefing, not a verdict.

=== DIMENSION ANALYSIS ===

Analyze all four dimensions using this structure per dimension:

  STATUS: OK | FLAG | OPEN
    OK = no issue identified
    FLAG = issue found, worth reviewing before committing
    OPEN = gap present, no artifact covers this area
  Basis: [artifact names and dates cited — "see above" does not pass; name them here]
  Finding: [specific observation — generic summary does not pass]
  Action: [required if STATUS is FLAG or OPEN; omit only if OK]

ABSENCE RULE (applies to every section below):
  If no artifact covers the question a dimension asks, you MUST write the absence explicitly.
  Do not leave the section blank. Do not write a vague finding that implies evidence was
  checked and found okay. The required form is: "No [evidence type] found — [dimension name]
  gap is open." Silence does not pass. An empty finding is indistinguishable from a missed
  check, not from a clean bill of health.

--- CAUSAL GAP ---

Does any artifact establish the mechanism linking {topic}'s feature to its claimed outcome?

Step 1: Name the claimed outcome for {topic}.
Step 2: Scan the inventory for any artifact that traces a causal chain from the feature to
that outcome. A causal chain is a sequence of observable steps — not a summary claim ("users
will benefit") and not a correlation.
Step 3: Produce one of two explicit statements:
  (a) "Mechanism evidence found: [artifact name, date] establishes [mechanism] by tracing [steps]."
  (b) "No mechanism evidence found. The causal gap is open."

Absence rule applied: if you find no mechanism evidence, you MUST write option (b). Do not
write a blank section or a hedge ("mechanism may be implied by the feasibility artifact").
Absence must be declared.

  STATUS: [OK / FLAG / OPEN]
  Basis: [artifacts checked for mechanism content; if none were found, write "no artifact
    addresses mechanism"]
  Finding: [(a) or (b) from above — the stated form is required]
  Action: [if FLAG or OPEN: name the skill using /namespace:skill format]

--- SEQUENCE ---

Did discovery happen before specification?

Compare dates of discovery-type artifacts (discover, scout, prove namespaces) to
specification-type artifacts (draft, topic namespaces). Name the artifacts and their dates.

  STATUS: [OK / FLAG / OPEN]
    OK = discovery dates precede specification dates
    FLAG = mixed or ambiguous order
    OPEN = no discovery artifacts exist

Absence rule applied: if no discovery artifacts exist, you MUST write "No discovery artifacts
found — ordering cannot be established." Do not write "SEQUENCE: OK" when no discovery
artifacts were checked. Do not assert an order without dating evidence.

  Basis: [artifact names and dates compared; if no discovery artifacts exist, write "no
    discovery artifacts found in inventory"]
  Finding: [what the dates show — or explicit absence declaration if no dates available]
  Action: [if FLAG or OPEN: name the discovery skill using /namespace:skill format]

--- STALENESS ---

Are signals recent enough to trust?

Name your staleness threshold before applying it:
  "For {topic}'s domain, signals older than [N] days are stale because [reason]."

Apply the threshold to each artifact in the inventory. Name which are within threshold
and which are past it.

  STATUS: [OK / FLAG / OPEN]

Absence rule applied: if the inventory contains no dated artifacts, you MUST write "No
dated artifacts found — staleness cannot be assessed." Do not write a threshold and then
apply it to an empty inventory without noting the absence.

  Basis: [artifacts checked against threshold, with their dates]
  Finding: [which are fresh, which are stale — by name; or explicit absence if no dates]
  Action: [if FLAG or OPEN: name the artifact to refresh and the skill using /namespace:skill]

--- COHERENCE ---

Do your signals agree with each other?

Find at least one pair of artifacts that address the same question. Name the agreement
or contradiction specifically. "Signals seem aligned" without named artifact pairs does
not pass this section.

  STATUS: [OK / FLAG / OPEN]
    OK = signals agree on shared questions
    FLAG = contradiction identified
    OPEN = only one artifact per question — no pair to compare

Absence rule applied: if the inventory contains only one artifact, you MUST write "Only one
artifact exists for {topic} — no pair available to assess coherence." Do not write "COHERENCE:
OK" when there was nothing to compare.

  Basis: [artifact pairs examined; if only one artifact exists, write "single artifact — no
    comparable pair available"]
  Finding: [named agreement or contradiction; or explicit absence of a comparable pair]
  Action: [if FLAG or OPEN: name what would resolve the contradiction or provide a second
    artifact, using /namespace:skill format for the skill]

=== CROSS-DIMENSION PATTERNS ===

Review the four STATUS values. If two or more dimensions share a common root cause, name it.
A shared root is more actionable than four independent issues.

Examples:
  - CAUSAL GAP OPEN + SEQUENCE OPEN: both may trace to a single missing phase — the team
    has not run any discovery. One root, two symptoms.
  - SEQUENCE FLAG + CAUSAL GAP OPEN: specification preceded discovery; the mechanism gap is
    likely downstream of the same premature commitment.

If a pattern exists: name it, name which dimensions it explains, name the single action
that would address the root.

If no shared root: "No cross-dimension pattern identified."

=== MISSING SIGNAL GUIDE ===

For every dimension with STATUS FLAG or OPEN, name the specific skill that would close it.
One line per gap. Format:

  [Dimension] gap: run /[namespace]:[skill] — produces [what it creates]

If no dimensions are FLAG or OPEN: "No missing signals — signal health is clear."

=== ARTIFACT ===

Write to simulations/signal/check/{topic}-check-{date}.md.

Frontmatter:
  topic: {topic}
  date: {date}
  causal_gap_status: ok | flag | open
  sequence_status: ok | flag | open
  staleness_status: ok | flag | open
  coherence_status: ok | flag | open
  staleness_threshold_named: true | false
  mechanism_evidence_found: true | false
  explicit_absences_declared: true | false
  cross_dimension_pattern: true | false
  artifact_count: {count}
  open_dimensions: [{list of FLAG or OPEN dimension names}]
```

---

## V-02: Strict skill-format enforcement (C-11 axis)

**Axis:** C-11 — every skill reference anywhere in the output must use `/namespace:skill` format.
A format constraint is stated at the preamble level and repeated in every section that produces
action fields. Bare skill names ("discover-causal") and vague prompts ("run the relevant skill")
are explicitly prohibited.

**Hypothesis:** C-11 fails because inline references (readiness summary, mid-section
recommendations) drift to bare names even when the MISSING SIGNAL GUIDE uses correct format.
The fix is not more examples — it is a constraint stated before analysis begins that is repeated
at every location where a skill reference might appear. This tests whether format compliance
is achieved through constraint propagation (state the rule early and repeat it) or only at
the terminal guide.

```
You are running /signal-check for topic: {topic}.

This is a coaching check, not a gate. It surfaces inconsistencies so you can decide what
to address before committing.

SKILL REFERENCE FORMAT (applies everywhere in this output):
  Every skill reference must use the format: /namespace:skill
  Examples: /discover:causal, /discover:competitors, /scout:feasibility
  Bare skill names (e.g., "discover-causal"), vague references ("run the relevant discover
  skill"), and namespace-only references ("run a /discover skill") do NOT pass.
  This constraint applies to the readiness summary, all action fields, the cross-dimension
  patterns section, and the MISSING SIGNAL GUIDE. No exceptions.

=== ARTIFACT INVENTORY ===

Use Glob to find all signal artifacts for {topic}:
  Pattern: simulations/**/*{topic}*.md

Build an inventory table:

  | # | Artifact path | Namespace | Signal type | Date |
  |---|--------------|-----------|-------------|------|

Artifact count: {N}

If no artifacts are found: "No signal artifacts found for {topic}. Consider running
/discover:causal, /discover:competitors, or other discover-namespace skills before committing."
Stop.

=== READINESS SUMMARY ===

[Write this section last — place it first in the final artifact.]

2-4 sentences: overall signal health posture for {topic}, which dimensions are clear, which
have gaps. If gaps exist, name the skill (using /namespace:skill format) that would close
each one. Frame as advisory briefing, not a verdict.

REMINDER: Any skill named in this summary must use /namespace:skill format.

=== DIMENSION ANALYSIS ===

Each dimension uses this structure:

  STATUS: OK | FLAG | OPEN
  Basis: [artifact names and dates — "see above" does not pass; name them here]
  Finding: [specific named observation]
  Action: [required if STATUS is FLAG or OPEN — must name a skill using /namespace:skill
    format; bare skill names do not pass]

--- CAUSAL GAP ---

Does any artifact establish the mechanism linking {topic}'s feature to its claimed outcome?

Step 1: Name the claimed outcome.
Step 2: Scan the inventory for mechanism evidence — a causal chain, not a correlation or
outcome summary.
Step 3: State explicitly:
  (a) "Mechanism evidence found: [artifact] establishes [chain] by [steps]."
  (b) "No mechanism evidence found. The causal gap is open."

  STATUS: [OK / FLAG / OPEN]
  Basis: [artifacts checked for mechanism content]
  Finding: [(a) or (b) — required; silence does not pass]
  Action: [if FLAG or OPEN: "Run /discover:causal to establish mechanism evidence."
    Must use /namespace:skill format — e.g., /discover:causal, not "discover-causal".]

--- SEQUENCE ---

Did discovery happen before specification?

Compare dates of discovery-type artifacts (discover, scout, prove namespaces) to
specification-type artifacts (draft, topic namespaces).

  STATUS: [OK / FLAG / OPEN]
  Basis: [artifact names and dates compared; if no discovery artifacts exist, state this]
  Finding: [what the dates show, or absence declaration if no discovery artifacts]
  Action: [if FLAG or OPEN: name the missing discovery skill using /namespace:skill format
    — e.g., /discover:competitors, /scout:feasibility]

--- STALENESS ---

Are signals recent enough to trust?

First, name your threshold:
  "For {topic}'s domain, signals older than [N] days are stale because [reason]."

Apply the threshold to each artifact.

  STATUS: [OK / FLAG / OPEN]
  Basis: [each artifact with its date, checked against threshold]
  Finding: [which are fresh, which are stale — by name]
  Action: [if FLAG or OPEN: name the artifact to refresh and the skill to run — using
    /namespace:skill format; e.g., /discover:competitors to refresh a stale competitive
    landscape signal]

--- COHERENCE ---

Do your signals agree with each other?

Find at least one pair of artifacts addressing the same question. State agreement or
contradiction specifically — "signals seem aligned" without named pairs does not pass.

  STATUS: [OK / FLAG / OPEN]
  Basis: [artifact pairs examined; or "single artifact — no pair available" if applicable]
  Finding: [named agreement or contradiction; or absence of a comparable pair]
  Action: [if FLAG or OPEN: name what would resolve the contradiction or provide a second
    artifact — using /namespace:skill format for the producing skill]

=== CROSS-DIMENSION PATTERNS ===

Review the four STATUS values. If two or more share a common root cause, name it.
If a shared root has a single action that would close multiple gaps, name that action —
using /namespace:skill format.

If no shared root: "No cross-dimension pattern identified."

=== MISSING SIGNAL GUIDE ===

For every dimension with STATUS FLAG or OPEN, name the skill that would close it.
All skill references must use /namespace:skill format. One line per gap:

  [Dimension] gap: run /[namespace]:[skill] — produces [what it creates]

REMINDER: Do not use bare skill names here. /discover:causal not "discover-causal".

If no dimensions are FLAG or OPEN: "No missing signals — signal health is clear."

=== ARTIFACT ===

Write to simulations/signal/check/{topic}-check-{date}.md.

Frontmatter:
  topic: {topic}
  date: {date}
  causal_gap_status: ok | flag | open
  sequence_status: ok | flag | open
  staleness_status: ok | flag | open
  coherence_status: ok | flag | open
  staleness_threshold_named: true | false
  mechanism_evidence_found: true | false
  cross_dimension_pattern: true | false
  skill_format_enforced: true
  artifact_count: {count}
  open_dimensions: [{list of FLAG or OPEN dimension names}]
```

---

## V-03: Lifecycle emphasis shift (depth inversion axis)

**Axis:** Lifecycle emphasis — CAUSAL GAP and SEQUENCE receive expanded instructional depth
(multi-step procedures, explicit examples, more detailed output requirements). STALENESS and
COHERENCE are compressed to a compact single-block format. Space allocation reflects analytic
difficulty, not alphabetical or narrative order.

**Hypothesis:** CAUSAL GAP and SEQUENCE are harder to analyze correctly and more commonly
open. STALENESS and COHERENCE are comparatively mechanical (apply a threshold; compare artifact
pairs). Allocating more instructional depth to the hard dimensions should reduce C-04 silence
and C-02 date-assertion failures without degrading the mechanical dimensions — which have lower
failure rates and need less scaffolding. The secondary hypothesis is that more explicit CAUSAL GAP
instruction will improve cross-dimension pattern detection (C-09) because the analyst spends more
time with mechanism reasoning before reaching SEQUENCE.

```
You are running /signal-check for topic: {topic}.

This is a coaching check, not a gate. It surfaces inconsistencies so you can decide what
to address before committing. Nothing here produces a verdict that blocks you.

=== ARTIFACT INVENTORY ===

Use Glob to find all signal artifacts for {topic}:
  Pattern: simulations/**/*{topic}*.md

Inventory table:

  | # | Artifact path | Namespace | Signal type | Date |
  |---|--------------|-----------|-------------|------|

Artifact count: {N}

If no artifacts are found: "No signal artifacts found for {topic}." Stop.

=== READINESS SUMMARY ===

[Write last — position first in the output.]

2-4 sentences: overall signal health posture, which dimensions are clear or have gaps,
and whether signals support proceeding or one gap is worth addressing first.

=== DEEP ANALYSIS: CAUSAL GAP ===

This is the dimension teams most commonly skip. A full set of discovery artifacts can exist
while the causal mechanism remains unexamined. Work through this carefully before anything else.

**Step 1 — Name the outcome**

What is the claimed outcome for {topic}? State it explicitly:
  "The claimed outcome is: [outcome]."

If you cannot name the outcome from the artifact inventory, state: "The claimed outcome is
not named in any artifact — this is itself a gap."

**Step 2 — Define what mechanism evidence looks like**

Mechanism evidence is an artifact that traces a causal chain: a sequence of observable
intermediate steps from feature to outcome. It is not:
  - A correlation ("users who use X have better Y scores")
  - An outcome claim ("users will benefit from X")
  - A proxy metric ("adoption rate will increase")
  - An assumption about user behavior without observable chain

It is: "Feature X causes outcome Y because [step 1] → [step 2] → [step 3]."

**Step 3 — Check the inventory**

Scan every artifact. For each one, assess whether it contains mechanism evidence as defined
above. Be explicit about what you found and why it does or does not qualify.

**Step 4 — State your finding**

Choose one and write it verbatim:
  (a) "Mechanism evidence found: [artifact name, date] establishes [mechanism] by tracing
      [step 1] → [step 2] → [step 3]."
  (b) "No mechanism evidence found. The causal gap is open."

Silence does not pass. Hedging ("mechanism may be implied") does not pass.

  STATUS: OK | FLAG | OPEN
  Basis: [artifacts checked, with dates — name each one]
  Finding: [(a) or (b) verbatim]
  Action: [if FLAG or OPEN: "Run /discover:causal to gather mechanism evidence."]

=== DEEP ANALYSIS: SEQUENCE ===

The question is whether discovery preceded commitment. Commitment artifacts (specs, proposals,
topic registrations) tend to lock direction. Discovery artifacts (competitors, feasibility,
user research) should exist and be dated before commitment artifacts.

**Step 1 — Classify your inventory**

Sort each artifact into one of three categories:
  - Discovery: namespace is discover, scout, prove, research, listen
  - Commitment: namespace is draft, topic, program
  - Other: does not clearly belong to either

**Step 2 — Compare dates**

For each discovery artifact, note its date. For each commitment artifact, note its date.
Name the specific artifacts you are comparing.

**Step 3 — State the order the dates show**

One of three outcomes:
  (a) "Discovery precedes commitment: [discovery artifact, date] predates [commitment
      artifact, date]."
  (b) "Commitment precedes discovery: [commitment artifact, date] predates [discovery
      artifact, date]. Inversion flagged."
  (c) "No discovery artifacts exist. Ordering cannot be established."

Do not assert an order without citing dated artifacts.

  STATUS: OK | FLAG | OPEN
  Basis: [artifacts compared, with dates — name each one]
  Finding: [(a), (b), or (c) from above]
  Action: [if FLAG or OPEN: name the missing discovery signal and skill using /namespace:skill]

=== COMPACT ANALYSIS: STALENESS AND COHERENCE ===

These dimensions are more mechanical. Use the compact structure below for each.

--- STALENESS ---

Threshold: "For {topic}'s domain, signals older than [N] days are stale because [reason]."
(Name it; "recent enough" without a number does not pass.)

  STATUS: OK | FLAG | OPEN
  Basis: [artifacts checked, with dates]
  Finding: [which are fresh; which are past threshold — by name]
  Action: [if FLAG or OPEN: artifact to refresh + /namespace:skill to run]

--- COHERENCE ---

  STATUS: OK | FLAG | OPEN
  Basis: [artifact pairs examined; or "single artifact — no pair available"]
  Finding: ["[Artifact A, date] and [Artifact B, date] both say [X]" OR "[A] says [X],
    [B] says [Y] — contradiction on [question]" OR "No comparable pair exists for
    [question] — only one artifact covers it."]
  Action: [if FLAG or OPEN: what to run using /namespace:skill format]

=== CROSS-DIMENSION PATTERNS ===

Review all four STATUS values together. Given the depth of analysis above on CAUSAL GAP
and SEQUENCE, look especially for root connections between them.

Common pattern: SEQUENCE FLAG or OPEN + CAUSAL GAP OPEN often trace to the same root —
the team specified before running any discovery. One root, two symptoms.

If a pattern exists: name it, name which dimensions it explains, name the action that
addresses the shared root.

If no shared root: "No cross-dimension pattern identified."

=== MISSING SIGNAL GUIDE ===

For every dimension with STATUS FLAG or OPEN, one line per gap:

  [Dimension] gap: run /[namespace]:[skill] — produces [what it creates]

If all clear: "No missing signals — signal health is clear."

=== ARTIFACT ===

Write to simulations/signal/check/{topic}-check-{date}.md.

Frontmatter:
  topic: {topic}
  date: {date}
  causal_gap_status: ok | flag | open
  sequence_status: ok | flag | open
  staleness_status: ok | flag | open
  coherence_status: ok | flag | open
  staleness_threshold_named: true | false
  mechanism_evidence_found: true | false
  cross_dimension_pattern: true | false
  artifact_count: {count}
  open_dimensions: [{list of FLAG or OPEN dimension names}]
```

---

## V-04: Absence enforcement + strict skill format (combination: C-13 + C-11)

**Axes combined:** V-01 (explicit absence prohibition) + V-02 (strict `/namespace:skill` format)

**Hypothesis:** C-13 and C-11 are independent structural properties that both degrade through
the same failure mode: local drift from stated constraints. Absence declarations drift to silence;
skill references drift to bare names. Combining the two constraints in a single variation tests
whether they reinforce each other (the discipline of stating explicit absence also tends to produce
properly-formatted skill references in the action field) or whether they require independent
enforcement to pass simultaneously. This combination should score well on all essentials, all
recommended, and C-11/C-12/C-13 without the full coaching-scaffold overhead of V-05.

```
You are running /signal-check for topic: {topic}.

Coaching check — not a gate. Surfaces inconsistencies so you can decide what to address
before committing. Advisory throughout.

STANDING RULES (apply to every section of this output):

  Rule 1 — Absence must be declared:
    For every dimension where relevant evidence is absent or unavailable, write the absence
    explicitly. Required form: "No [evidence type] found — [dimension] gap is open."
    Do not leave a section blank. Do not write a vague finding that implies evidence was
    checked. Silence does not pass.

  Rule 2 — Skill reference format:
    Every skill reference in this output uses /namespace:skill format.
    Correct: /discover:causal, /discover:competitors, /scout:feasibility
    Wrong: "discover-causal", "run the relevant discover skill", "/discover skill"
    This applies to the readiness summary, all action fields, cross-dimension patterns,
    and the MISSING SIGNAL GUIDE. No exceptions.

=== ARTIFACT INVENTORY ===

Use Glob: simulations/**/*{topic}*.md

Inventory table:

  | # | Artifact path | Namespace | Signal type | Date |
  |---|--------------|-----------|-------------|------|

Artifact count: {N}

If no artifacts found: "No signal artifacts found for {topic}. Run /discover:causal,
/discover:competitors, or other /discover namespace skills before committing." Stop.

=== READINESS SUMMARY ===

[Write last — position first in the output.]

2-4 sentences: signal health posture, which dimensions are clear, which have gaps.
Name any gap-closing skill using /namespace:skill format. Advisory framing — not a verdict.

=== DIMENSION ANALYSIS ===

Structure per dimension:

  STATUS: OK | FLAG | OPEN
  Basis: [artifact names and dates — "see above" does not pass; name them here]
  Finding: [specific named observation; OR explicit absence declaration if no evidence found]
  Action: [required if FLAG or OPEN; must use /namespace:skill format; omit only if OK]

--- CAUSAL GAP ---

Does any artifact establish the mechanism from {topic}'s feature to its claimed outcome?

Step 1: Name the claimed outcome.
Step 2: Check inventory for mechanism evidence — a causal chain of observable steps, not a
  correlation or outcome claim.
Step 3: State one of:
  (a) "Mechanism evidence found: [artifact, date] establishes [mechanism] by [steps]."
  (b) "No mechanism evidence found. The causal gap is open."

  STATUS: [OK / FLAG / OPEN]
  Basis: [artifacts checked; if none address mechanism, write "no artifact addresses
    mechanism — checked: {list artifacts}"]
  Finding: [(a) or (b) — required; absence rule: option (b) must be written when no
    mechanism evidence exists; blank finding does not pass]
  Action: [if FLAG or OPEN: "Run /discover:causal to establish mechanism evidence."
    Skill format rule: use /discover:causal, not "discover-causal".]

--- SEQUENCE ---

Did discovery happen before specification?

Compare dates: discovery-type artifacts (discover, scout, prove) vs. specification-type
(draft, topic). Name artifacts and dates.

  STATUS: [OK / FLAG / OPEN]
  Basis: [artifacts compared with dates; if no discovery artifacts: "no discovery artifacts
    in inventory — ordering cannot be established"]
  Finding: [what dates show; OR: "No discovery artifacts found — ordering cannot be
    established." Absence rule: if no discovery artifacts, this form is required.]
  Action: [if FLAG or OPEN: name missing signal using /namespace:skill format]

--- STALENESS ---

Are signals recent enough to trust?

Name threshold first: "For {topic}'s domain, signals older than [N] days are stale
because [reason]."

Apply to each artifact.

  STATUS: [OK / FLAG / OPEN]
  Basis: [each artifact with date; if no dated artifacts: "no dated artifacts — staleness
    cannot be assessed"]
  Finding: [which fresh, which stale — by name; OR: "No dated artifacts found — staleness
    cannot be assessed." Absence rule required if inventory has no dated artifacts.]
  Action: [if FLAG or OPEN: artifact to refresh + /namespace:skill to run]

--- COHERENCE ---

Do signals agree? Find at least one pair addressing the same question.

  STATUS: [OK / FLAG / OPEN]
  Basis: [pairs examined; if single artifact: "single artifact — no comparable pair
    available"]
  Finding: [named agreement or contradiction; OR: "Only one artifact exists — no pair
    available to assess coherence." Absence rule required when no pair exists.]
  Action: [if FLAG or OPEN: what resolves contradiction + /namespace:skill for second artifact]

=== CROSS-DIMENSION PATTERNS ===

Review all four STATUS values. If two or more share a common root, name it. Name the
single action that addresses the shared root — using /namespace:skill format.

If no shared root: "No cross-dimension pattern identified."

=== MISSING SIGNAL GUIDE ===

For every FLAG or OPEN dimension, one line per gap. All skill references must use
/namespace:skill format:

  [Dimension] gap: run /[namespace]:[skill] — produces [what it creates]

If all clear: "No missing signals."

=== ARTIFACT ===

Write to simulations/signal/check/{topic}-check-{date}.md.

Frontmatter:
  topic: {topic}
  date: {date}
  causal_gap_status: ok | flag | open
  sequence_status: ok | flag | open
  staleness_status: ok | flag | open
  coherence_status: ok | flag | open
  staleness_threshold_named: true | false
  mechanism_evidence_found: true | false
  explicit_absences_declared: true | false
  skill_format_enforced: true
  cross_dimension_pattern: true | false
  artifact_count: {count}
  open_dimensions: [{list of FLAG or OPEN dimension names}]
```

---

## V-05: Full v2 canonical stack (C-11 + C-12 + C-13 + R1 V-05 base)

**Axes combined:** All three R2 axes + full R1 V-05 base (CAUSAL GAP first, status tags,
coaching scaffold, READINESS SUMMARY, CROSS-DIMENSION PATTERNS, MISSING SIGNAL GUIDE)

**Hypothesis:** All 13 criteria can be satisfied in a single output by combining the structural
features of R1 V-05 with the three new v2 enforcement mechanisms: (a) absence prohibition at
every dimension (C-13), (b) strict /namespace:skill format constraint declared upfront and
repeated at each action field (C-11), and (c) the terminal MISSING SIGNAL GUIDE from R1 V-05
already present for C-12. This is the v2 rubric-ceiling reference — every criterion has a
dedicated structural slot, and the two new constraint rules are embedded early enough to
propagate through the entire output.

```
You are running /signal-check for topic: {topic}.

Think of this as a preflight check. The checklist does not decide whether to fly — it makes
sure the pilot sees everything before they decide. Nothing here blocks you from proceeding.
It exists so you know what you know before you commit.

STANDING RULES (apply throughout this entire output, without exception):

  Rule 1 — Absence must be declared:
    For every dimension where relevant evidence is absent, write the absence explicitly.
    Required form: "No [evidence type] found — [dimension] gap is open."
    Blank findings are not acceptable. Hedged findings ("may be present elsewhere") are not
    acceptable. If evidence is absent, state it. Silence does not pass.

  Rule 2 — Skill reference format:
    Every skill reference in this output uses /namespace:skill format.
    Correct: /discover:causal, /discover:competitors, /scout:feasibility, /prove:hypothesis
    Wrong: "discover-causal", "run the discover skill", "a /discover skill"
    This applies to the readiness summary, all action fields, the cross-item patterns
    section, and the MISSING SIGNAL GUIDE. No bare names anywhere.

=== GATHER YOUR SIGNALS ===

Use Glob: simulations/**/*{topic}*.md

Build the inventory:

  | # | Artifact path | Namespace | Signal type | Date |
  |---|--------------|-----------|-------------|------|

Artifact count: {N}

If no artifacts found: "No signal artifacts exist yet for {topic}. Consider running
/discover:causal, /discover:competitors, or /scout:feasibility before committing." Stop.

=== READINESS SUMMARY ===

[Write this section last — place it first in the final artifact.]

2-4 sentences: overall signal health for {topic}, which dimensions are clear, which have
gaps worth addressing. If recommending an action, name the skill using /namespace:skill
format. Frame as pilot briefing — not a verdict. The team decides.

=== THE PREFLIGHT CHECK ===

Each item uses this structure:

  STATUS: OK | FLAG | OPEN
    OK = no issue
    FLAG = issue found, worth reviewing before committing
    OPEN = gap — no artifact covers this area
  Basis: [name the specific artifacts examined — with dates; "see above" does not pass;
    if no artifacts cover the area, write "no artifact covers [question]"]
  Finding: [specific named observation; OR explicit absence declaration when evidence is
    absent — Rule 1 applies here]
  Action: [required if STATUS is FLAG or OPEN; must use /namespace:skill format — Rule 2;
    omit only when OK]

Work through all four items. Order is intentional: start with the causal question.

--- Item 1: CAUSAL GAP ---

What we're checking:
  Do you have evidence for why the feature causes the claimed outcome — not just that it
  might, but how? This is the signal teams gather last, if ever. A full discovery stack
  can exist while the mechanism remains uninvestigated. Surfacing it before commitment
  is the point of this item.

What we found:

  Step 1: Name the claimed outcome for {topic}:
    "The claimed outcome is: [outcome]."
    If no artifact names the outcome: "The claimed outcome is not stated in any artifact —
    this is itself a gap."

  Step 2: Scan the inventory for mechanism evidence. A causal chain is a sequence of
  observable intermediate steps from feature to outcome. It is not:
    - A correlation or adoption metric
    - A summary claim ("users will benefit")
    - An assumption about behavior without traced steps
  It is: "Feature causes outcome because [step 1] → [step 2] → [step 3]."

  Step 3: State one of two forms — absence rule applies:
    (a) "Mechanism evidence found: [artifact, date] establishes [mechanism] by tracing
        [step 1] → [step 2] → [step 3]."
    (b) "No mechanism evidence found. The causal gap is open."
  Form (b) is required when no mechanism evidence exists. Silence does not pass.

  STATUS: [OK / FLAG / OPEN]
  Basis: [artifacts checked for mechanism content; if none: "no artifact addresses
    mechanism — inventory checked: {artifact names}"]
  Finding: [(a) or (b) from above — required]

What you can do:
  Action: [if FLAG or OPEN: "Run /discover:causal to establish mechanism evidence before
    committing." Use /namespace:skill format — Rule 2.]

--- Item 2: SEQUENCE ---

What we're checking:
  Did discovery happen before specification? Commitment tends to close off investigation.
  Specs written before discovery signals existed may reflect direction chosen before the
  team knew what they were committing to.

What we found:
  Classify each artifact as discovery (discover, scout, prove, research, listen namespaces)
  or commitment (draft, topic, program namespaces). Note the date of each.

  Compare the date ranges. State what they show:
    (a) "Discovery precedes commitment: [discovery artifact, date] predates [commitment
        artifact, date]."
    (b) "Commitment precedes discovery: [commitment artifact, date] predates [discovery
        artifact, date]. Inversion flagged."
    (c) "No discovery artifacts found. Ordering cannot be established." (Absence rule:
        this form is required when no discovery artifacts exist — do not write SEQUENCE OK
        when nothing was checked.)

  STATUS: [OK / FLAG / OPEN]
  Basis: [artifact names and dates compared; if no discovery artifacts: "no discovery
    artifacts in inventory"]
  Finding: [(a), (b), or (c) from above — form (c) required when no discovery exists]

What you can do:
  Action: [if FLAG or OPEN: name the missing discovery signal and skill — /namespace:skill
    format required — Rule 2]

--- Item 3: STALENESS ---

What we're checking:
  Are your signals fresh enough to act on? Domain velocity determines freshness. A fast-
  moving market makes a 30-day-old competitive signal unreliable. A stable enterprise cycle
  may sustain a 90-day-old signal. This item checks whether artifact dates fall within a
  defensible window for the decisions being made.

What we found:
  First, name your threshold:
    "For {topic}'s domain: signals older than [N] days are stale because [reason]."
  (Absence rule: if the inventory has no dated artifacts, write: "No dated artifacts found —
  staleness cannot be assessed." Do not apply a threshold to an empty set.)

  Apply threshold to each artifact. State which are within threshold and which are past it.

  STATUS: [OK / FLAG / OPEN]
  Basis: [each artifact with date, checked against threshold; or "no dated artifacts"]
  Finding: [fresh/stale breakdown by name; OR "No dated artifacts found — staleness
    cannot be assessed" — Rule 1 applies]

What you can do:
  Action: [if FLAG or OPEN: name the stale artifact, its age vs. threshold, and the
    skill to refresh it — /namespace:skill format required — Rule 2]

--- Item 4: COHERENCE ---

What we're checking:
  Do your signals tell a consistent story? When two signals address the same question,
  they should roughly agree — or the disagreement should be visible and deliberate. Hidden
  contradictions surface after commitment.

What we found:
  Find at least one pair of artifacts that address the same question. State what each says.
  Absence rule: if only one artifact exists, write: "Only one artifact exists for {topic} —
  no comparable pair available to assess coherence." Do not write COHERENCE OK when there
  was nothing to compare.

  Name a specific agreement or contradiction:
    Agreement: "[Artifact A, date] and [Artifact B, date] both say [X]."
    Contradiction: "[Artifact A, date] says [X]. [Artifact B, date] says [Y]. These
    disagree on [question]."
    No pair: "Only one artifact covers [question] — no pair available to cross-check."

  STATUS: [OK / FLAG / OPEN]
  Basis: [pairs examined; or "single artifact — no comparable pair"]
  Finding: [named agreement, contradiction, or absence — Rule 1 applies]

What you can do:
  Action: [if FLAG or OPEN: what resolves the contradiction or provides a second artifact,
    using /namespace:skill format — Rule 2]

=== CROSS-ITEM PATTERNS ===

Step back from the four items. Do two or more share a common root cause?

This matters because addressing a shared root closes multiple gaps with one action.
Look especially for:
  - CAUSAL GAP OPEN + SEQUENCE OPEN/FLAG: one missing phase — the team has not run
    discovery. One root, two symptoms. Action: /discover:causal addresses both.
  - SEQUENCE FLAG + CAUSAL GAP OPEN: spec preceded discovery; mechanism gap is downstream
    of the same premature commitment.
  - STALENESS FLAG + COHERENCE FLAG: stale signal is the source of the contradiction —
    one artifact reflects old conditions, one reflects current.

If a pattern exists: name it, name which items it explains, name the single action that
addresses the root — using /namespace:skill format (Rule 2).

If no shared root: "No cross-item pattern found."

=== MISSING SIGNAL GUIDE ===

For every item with STATUS FLAG or OPEN, one line per gap. All skill references use
/namespace:skill format (Rule 2 — no exceptions):

  [Dimension] gap: run /[namespace]:[skill] — produces [what it creates]

Examples:
  CAUSAL GAP open: run /discover:causal — produces mechanism evidence for the causal chain
  SEQUENCE open: run /discover:competitors — produces a dated discovery artifact to establish order
  STALENESS flag on competitors: run /discover:competitors — refreshes competitive landscape
  COHERENCE open: run /scout:feasibility — produces a second feasibility signal for comparison

If no items are FLAG or OPEN: "No missing signals — signal health is clear."

=== ARTIFACT ===

Write to simulations/signal/check/{topic}-check-{date}.md.

Frontmatter:
  topic: {topic}
  date: {date}
  causal_gap_status: ok | flag | open
  sequence_status: ok | flag | open
  staleness_status: ok | flag | open
  coherence_status: ok | flag | open
  staleness_threshold_named: true | false
  mechanism_evidence_found: true | false
  explicit_absences_declared: true | false
  skill_format_enforced: true
  cross_dimension_pattern: true | false
  missing_signals_by_skill: true | false
  artifact_count: {count}
  open_dimensions: [{list of FLAG or OPEN dimension names}]
```

---

## Expected scoring under v2 rubric

| V | E (60) | R (30) | A (10) | Est. composite | Gold? |
|---|--------|--------|--------|----------------|-------|
| V-01 | 60 (5/5) | 30 (3/3) | 6 (C-09+C-10+C-13) | 96 | YES |
| V-02 | 60 (5/5) | 30 (3/3) | 6 (C-09+C-10+C-11) | 96 | YES |
| V-03 | 60 (5/5) | 30 (3/3) | 4 (C-09+C-10) | 94 | YES |
| V-04 | 60 (5/5) | 30 (3/3) | 8 (C-09+C-10+C-11+C-13) | 98 | YES |
| V-05 | 60 (5/5) | 30 (3/3) | 10 (all 5) | 100 | YES |

**Research questions from this round:**

1. Does explicit absence prohibition (V-01) close C-13 independently of structural slots,
   or do structural slots (Basis field requiring "no artifact found" when empty) do the same
   work implicitly?
2. Does the skill-format constraint stated at the preamble level (V-02) propagate to inline
   references, or do action fields still produce bare names regardless of the upfront rule?
3. Does depth inversion in V-03 (expanded CAUSAL GAP + SEQUENCE, compressed STALENESS +
   COHERENCE) improve C-09 cross-pattern detection without degrading C-06/C-07 on the
   compressed dimensions?
