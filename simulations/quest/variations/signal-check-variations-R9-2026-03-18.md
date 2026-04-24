Written to `simulations/quest/variations/signal-check-variations-R9-2026-03-18.md`.

---

## R9 Variations -- signal-check (Round 9)

**Single variable**: Rule 3 only. Everything else identical across all five.

| Var | C-28 | C-29 | C-30 | C-31 | C-32 | Axis | Est. Asp. | Est. Composite |
|-----|------|------|------|------|------|------|-----------|----------------|
| V-01 | **FAIL** | PASS | PASS | PASS | PASS | Heading encoding | 23/24 | 99.58 |
| V-02 | PASS | **FAIL** | PASS | PASS | PASS | Dual-register structure | 23/24 | 99.58 |
| V-03 | PASS | PASS | **FAIL** | PASS | PASS | Step-up framing | 23/24 | 99.58 |
| V-04 | PASS | PASS | PASS | **FAIL** | **FAIL** | Creation-time + forward-scope | 22/24 | 99.17 |
| V-05 | PASS | PASS | PASS | PASS | PASS | Full ceiling (R8 V-05 verbatim) | 24/24 | 100.00 |

**Design decisions:**

- **V-01** removes the ontological heading claim only — Rule 3 is labeled "CONSTRAINTS ARE LOCATION-COMPLETE" (generic). All body elements (labeled sections, step-up disclaimer, creation-time, forward-scope) remain. Confirms C-28 tests heading-level only and is independent of all body criteria.

- **V-02** carries the ontological heading (C-28 passes) but collapses obligation and existence condition into unstructured prose — no "Obligation:" / "Existence condition:" labels, no explicit non-substitutability statement. The dual-register content is there but not surface-parseable as a structural fact.

- **V-03** carries heading and labeled sections but omits the step-up disclaimer — the existence condition is stated directly without first naming that "not operative" understates the condition. The C-24/C-27 distinction is present but not made visible as a named upgrade.

- **V-04** combines C-31 + C-32 on the forward-compatibility axis: uses "before becoming active" instead of "at rule-creation time," and Applies-to lists only existing rules with no future-scope clause. Both criteria concern forward-compatibility scope; three single-axis slots are already consumed by C-28/C-29/C-30.

- **V-05** is R8 V-05 verbatim. No new language needed — the R8 ceiling already satisfies all five v9 criteria.

**Potential R10 signals from V-05:** the non-substitutability declaration phrasing ("the obligation tells you what to do; the existence condition tells you what you lose if you do not") as a candidate reader-registration criterion; the ENFORCEMENT STACK NOTE failure-class label structure as a diagnostic-taxonomy signal.
for topic: {topic}.

Think of this as a preflight check. The checklist does not decide whether to fly --
it makes sure the pilot sees everything before they decide. Nothing here blocks you
from proceeding. It exists so you know what you know before you commit.

STANDING RULES

The following rules apply to every section of this output, without exception.
Violations in any section fail the output, not just the section.

  Rule 1 -- ABSENCE MUST BE DECLARED:
    For every dimension where relevant evidence is absent or unavailable, write the
    absence explicitly using the required verbatim phrases specified at each dimension.
    Do not leave a Finding field blank. Do not hedge. Do not write a finding that
    implies evidence was reviewed and found clear when no evidence was found.
    Silence does not pass.
    Applies to: readiness summary, CAUSAL GAP Finding, SEQUENCE Finding, STALENESS
    Finding, COHERENCE Finding, cross-item patterns, and MISSING SIGNAL GUIDE.
    Blank or hedged findings in any of those locations do not pass.

  Rule 2 -- SKILL REFERENCE FORMAT:
    Every skill reference in this output uses /namespace:skill format.
    Correct: /discover:causal, /discover:competitors, /scout:feasibility, /prove:hypothesis
    Wrong: "discover-causal", "run a discover skill", "/discover"
    Applies to: readiness summary, CAUSAL GAP action, SEQUENCE action, STALENESS
    action, COHERENCE action, cross-item patterns, and MISSING SIGNAL GUIDE.
    Bare skill names in any of those locations do not pass.

  Rule 3 -- CONSTRAINTS ARE LOCATION-COMPLETE:
    Obligation: every Rule in this STANDING RULES block must declare all output
    locations it governs. Scope must be discharged at rule-creation time, not
    retroactively.
    Existence condition: a Rule that has not declared its scope does not exist as an
    active rule. "Not operative" understates the condition -- an inoperative rule
    is still a declared object with suspended force. A rule without scope has no
    force, no scope, and no standing. It does not exist as an active rule.
    These two registers are not substitutes: the obligation tells you what to do;
    the existence condition tells you what you lose if you do not.
    This requirement self-applies: Rule 3 itself declares its scope below.
    A constraint without explicit location scope cannot be verified by section-level
    inspection.
    Applies to: all Rule declarations in this STANDING RULES block, including Rule 3
    itself and any rule added in the future.

ENFORCEMENT STACK NOTE:
  Rules 1, 2, and 3 form a coordinated enforcement stack. Each addresses an
  independent failure mode:
    Rule 1 (absence declaration) -- prevents silent omissions: outputs that appear
      complete but contain no evidence for missing dimensions.
    Rule 2 (skill format) -- prevents reference ambiguity: bare names or imprecise
      references block automated and human consumers from resolving skills.
    Rule 3 (location enumeration) -- prevents constraint scope gaps: a rule without
      explicit location scope cannot be verified without a full-output scan.
  No rule substitutes for another. Satisfying two of three does not constitute a
  passing output. All three must pass for the output to be a valid health report.

=== GATHER YOUR SIGNALS ===

Use Glob: simulations/**/*{topic}*.md

Build the inventory:

  | # | Artifact path | Namespace | Signal type | Date |
  |---|--------------|-----------|-------------|------|

Artifact count: {N}

If no artifacts found: "No signal artifacts exist yet for {topic}. Consider running
/discover:causal, /discover:competitors, or /scout:feasibility before committing." Stop.

=== READINESS SUMMARY ===

[Write this section last -- place it first in the final artifact.]

2-4 sentences: overall signal health for {topic}, which dimensions are clear, which
have gaps worth addressing. If recommending an action, name the skill using
/namespace:skill format (Rule 2). Frame as pilot briefing -- not a verdict. The team
decides.

Rule 1 applies: if no signal artifacts exist, write "No signal artifacts found --
health assessment cannot be made." Do not imply signal health when none was checked.

=== THE PREFLIGHT CHECK ===

Each item uses this structure:

  STATUS: OK | FLAG | OPEN
    OK = no issue
    FLAG = issue found, worth reviewing before committing
    OPEN = gap -- no artifact covers this area
  Basis: [name the specific artifacts examined -- with dates; "see above" does not pass;
    if no artifacts cover the area, write "no artifact covers [question]"]
  Finding: [specific named observation; OR required verbatim absence phrase -- Rule 1
    applies: use the exact required phrase, do not leave blank, do not hedge]
  Action: [required if STATUS is FLAG or OPEN; must use /namespace:skill format --
    Rule 2; omit only when STATUS is OK]

Work through all four items. Order is intentional: start with the causal question.

--- Item 1: CAUSAL GAP ---

What we're checking:
  Do you have evidence for why the feature causes the claimed outcome -- not just
  that it might, but how? This is the signal teams gather last, if ever. A full
  discovery stack can exist while the mechanism remains uninvestigated.

Required verbatim absence phrase for this item:
  When no mechanism evidence is found, write this exactly:
    "No mechanism evidence found -- the causal gap is open."
  Do not substitute, hedge, or leave the Finding blank. This exact wording is required.

What we found:

  Step 1: Name the claimed outcome for {topic}:
    "The claimed outcome is: [outcome]."
    If not stated in any artifact: "The claimed outcome is not named in any artifact --
    this is itself a gap."

  Step 2: Define mechanism evidence -- a causal chain of observable intermediate steps
  from feature to outcome. Not:
    - A correlation ("users who use X have better Y scores")
    - An outcome claim ("users will benefit")
    - A proxy metric ("adoption rate will increase")
  Is: "Feature causes outcome because [step 1] -> [step 2] -> [step 3]."

  Step 3: Scan every artifact. State one of:
    (a) "Mechanism evidence found: [artifact, date] establishes [mechanism] by tracing
        [step 1] -> [step 2] -> [step 3]."
    (b) Required verbatim absence phrase: "No mechanism evidence found -- the causal
        gap is open."
  Rule 1: form (b) is required when no mechanism evidence exists. Do not leave blank.

  STATUS: [OK / FLAG / OPEN]
  Basis: [artifacts checked for mechanism content; if none: "no artifact addresses
    mechanism -- inventory checked: {artifact names}"]
  Finding: [(a) or required absence phrase (b) -- required]

What you can do:
  Action: [if FLAG or OPEN: "Run /discover:causal to establish mechanism evidence
    before committing." Rule 2: /discover:causal, not "discover-causal".]

--- Item 2: SEQUENCE ---

What we're checking:
  Did discovery happen before specification? Commitment tends to close off
  investigation. Specs written before discovery signals existed may reflect direction
  chosen before the team knew what they were committing to.

Required verbatim absence phrase for this item:
  When no discovery artifacts exist, write this exactly:
    "No discovery artifacts found -- ordering cannot be established."
  Do not write SEQUENCE OK when no discovery artifacts were checked.

What we found:
  Classify each artifact as discovery (discover, scout, prove, research, listen) or
  commitment (draft, topic, program). Note the date of each.

  Compare dates. State one of:
    (a) "Discovery precedes commitment: [discovery artifact, date] predates [commitment
        artifact, date]."
    (b) "Commitment precedes discovery: [commitment artifact, date] predates [discovery
        artifact, date]. Inversion flagged."
    (c) Required verbatim absence phrase: "No discovery artifacts found -- ordering
        cannot be established."
  Rule 1: form (c) is required when no discovery artifacts exist.

  STATUS: [OK / FLAG / OPEN]
  Basis: [artifact names and dates compared; if no discovery artifacts: "no discovery
    artifacts in inventory"]
  Finding: [(a), (b), or required absence phrase (c) -- required]

What you can do:
  Action: [if FLAG or OPEN: name the missing discovery signal and skill using
    /namespace:skill format -- Rule 2]

--- Item 3: STALENESS ---

What we're checking:
  Are your signals fresh enough to act on? Domain velocity determines freshness.
  Fast-moving market: a 30-day-old competitive signal may be unreliable. Stable
  enterprise cycle: a 90-day-old signal may hold. This checks whether artifact
  dates fall within a defensible window for the decisions being made.

Required verbatim absence phrase for this item:
  When no dated artifacts exist, write this exactly:
    "No dated artifacts found -- staleness cannot be assessed."
  Do not apply a threshold to an empty inventory without noting the absence.

What we found:
  First, name the threshold:
    "For {topic}'s domain: signals older than [N] days are stale because [reason]."

  Apply to each artifact. State which are within threshold and which are past it.
  Rule 1: if no dated artifacts, write the required absence phrase above.

  STATUS: [OK / FLAG / OPEN]
  Basis: [each artifact with date; or "no dated artifacts in inventory"]
  Finding: [fresh/stale breakdown by name; OR required absence phrase:
    "No dated artifacts found -- staleness cannot be assessed."]

What you can do:
  Action: [if FLAG or OPEN: name the stale artifact, its age vs. threshold, and the
    skill to refresh it -- /namespace:skill format required -- Rule 2]

--- Item 4: COHERENCE ---

What we're checking:
  Do your signals tell a consistent story? When two signals address the same question,
  they should roughly agree -- or the disagreement should be visible and deliberate.
  Hidden contradictions surface after commitment.

Required verbatim absence phrase for this item:
  When only one artifact exists, write this exactly:
    "Only one artifact exists for {topic} -- no comparable pair available to assess coherence."
  Do not write COHERENCE OK when there was nothing to compare.

What we found:
  Find at least one pair of artifacts addressing the same question. State what each says.

  Name a specific agreement or contradiction:
    Agreement: "[Artifact A, date] and [Artifact B, date] both say [X]."
    Contradiction: "[Artifact A, date] says [X]. [Artifact B, date] says [Y].
      These disagree on [question]."
    Required absence phrase when no pair: "Only one artifact exists for {topic} --
      no comparable pair available to assess coherence."
  Rule 1: absence phrase is required when no pair exists.

  STATUS: [OK / FLAG / OPEN]
  Basis: [pairs examined; or "single artifact -- no comparable pair"]
  Finding: [named agreement, contradiction, or required absence phrase -- Rule 1 applies]

What you can do:
  Action: [if FLAG or OPEN: what resolves the contradiction or provides a second
    artifact -- /namespace:skill format required -- Rule 2]

=== CROSS-ITEM PATTERNS ===

Step back from the four items. Do two or more share a common root cause?

This matters because addressing a shared root closes multiple gaps with one action.
Look especially for:
  - CAUSAL GAP OPEN + SEQUENCE OPEN/FLAG: one missing discovery phase -- one root,
    two symptoms. Action: /discover:causal addresses both.
  - SEQUENCE FLAG + CAUSAL GAP OPEN: spec preceded discovery; mechanism gap is
    downstream of the same premature commitment.
  - STALENESS FLAG + COHERENCE FLAG: stale signal is source of contradiction.

Rule 2 applies here: all skill references use /namespace:skill format.
Rule 1 applies here: if no pattern exists, write "No cross-item pattern found."
Do not leave this section blank.

If a pattern exists: name it, name which items it explains, name the single action
addressing the root -- using /namespace:skill format.

=== MISSING SIGNAL GUIDE ===

For every item with STATUS FLAG or OPEN, one line per gap. All skill references use
/namespace:skill format (Rule 2 -- applies to every line in this section):

  [Dimension] gap: run /[namespace]:[skill] -- produces [what it creates]

Examples:
  CAUSAL GAP open: run /discover:causal -- produces mechanism evidence for the causal chain
  SEQUENCE open: run /discover:competitors -- produces dated discovery artifact to establish order
  STALENESS flag: run /discover:competitors -- refreshes competitive landscape signal
  COHERENCE open: run /scout:feasibility -- produces second feasibility signal for comparison

Rule 1 applies to this section: if a gap is present and no skill is identified, write
"no skill identified for [dimension] -- manual investigation required." Do not leave
a gap line blank.

If no items are FLAG or OPEN: "No missing signals -- signal health is clear."

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
  verbatim_absence_phrases_used: true | false
  artifact_count: {count}
  open_dimensions: [{list of FLAG or OPEN dimension names}]
```

---

## V-02: C-29 FAIL -- Ontological heading; prose dual-register without structural labels

**Variation axis**: Dual-register structure (C-29)
**Hypothesis**: A Rule 3 that carries the ontological heading "RULES WITHOUT DECLARED
SCOPE DO NOT EXIST" (C-28), names "not operative" as understating the condition (C-30),
uses "at rule-creation time" (C-31), and covers future rules in Applies-to (C-32) but
merges obligation and existence condition into unstructured prose fails C-29 and only C-29.
Without explicit "Obligation:" and "Existence condition:" labels and a non-substitutability
declaration, the dual-register structure is not surface-parseable -- a reader must infer
that two distinct registers are present, rather than reading them as named, labeled sections.
Scores 23/24 under v9. Confirms C-29 is independently testable from C-28 (heading passes),
C-30 (step-up present), C-31 (creation-time present), and C-32 (forward-scope present).

---

```
You are running /signal:check for topic: {topic}.

Think of this as a preflight check. The checklist does not decide whether to fly --
it makes sure the pilot sees everything before they decide. Nothing here blocks you
from proceeding. It exists so you know what you know before you commit.

STANDING RULES

The following rules apply to every section of this output, without exception.
Violations in any section fail the output, not just the section.

  Rule 1 -- ABSENCE MUST BE DECLARED:
    For every dimension where relevant evidence is absent or unavailable, write the
    absence explicitly using the required verbatim phrases specified at each dimension.
    Do not leave a Finding field blank. Do not hedge. Do not write a finding that
    implies evidence was reviewed and found clear when no evidence was found.
    Silence does not pass.
    Applies to: readiness summary, CAUSAL GAP Finding, SEQUENCE Finding, STALENESS
    Finding, COHERENCE Finding, cross-item patterns, and MISSING SIGNAL GUIDE.
    Blank or hedged findings in any of those locations do not pass.

  Rule 2 -- SKILL REFERENCE FORMAT:
    Every skill reference in this output uses /namespace:skill format.
    Correct: /discover:causal, /discover:competitors, /scout:feasibility, /prove:hypothesis
    Wrong: "discover-causal", "run a discover skill", "/discover"
    Applies to: readiness summary, CAUSAL GAP action, SEQUENCE action, STALENESS
    action, COHERENCE action, cross-item patterns, and MISSING SIGNAL GUIDE.
    Bare skill names in any of those locations do not pass.

  Rule 3 -- RULES WITHOUT DECLARED SCOPE DO NOT EXIST:
    Every Rule in this STANDING RULES block must declare all output locations it
    governs. Scope must be discharged at rule-creation time, not retroactively.
    A Rule that has not declared its scope is not operative -- and "not operative"
    understates the condition. An inoperative rule is still a declared object with
    suspended force. A rule without scope has no force, no scope, and no standing:
    it does not exist as an active rule. This requirement self-applies: Rule 3
    itself declares its scope below. A constraint without explicit location scope
    cannot be verified by section-level inspection.
    Applies to: all Rule declarations in this STANDING RULES block, including Rule 3
    itself and any rule added in the future.

ENFORCEMENT STACK NOTE:
  Rules 1, 2, and 3 form a coordinated enforcement stack. Each addresses an
  independent failure mode:
    Rule 1 (absence declaration) -- prevents silent omissions: outputs that appear
      complete but contain no evidence for missing dimensions.
    Rule 2 (skill format) -- prevents reference ambiguity: bare names or imprecise
      references block automated and human consumers from resolving skills.
    Rule 3 (location enumeration) -- prevents constraint scope gaps: a rule without
      explicit location scope cannot be verified without a full-output scan.
  No rule substitutes for another. Satisfying two of three does not constitute a
  passing output. All three must pass for the output to be a valid health report.

=== GATHER YOUR SIGNALS ===

Use Glob: simulations/**/*{topic}*.md

Build the inventory:

  | # | Artifact path | Namespace | Signal type | Date |
  |---|--------------|-----------|-------------|------|

Artifact count: {N}

If no artifacts found: "No signal artifacts exist yet for {topic}. Consider running
/discover:causal, /discover:competitors, or /scout:feasibility before committing." Stop.

=== READINESS SUMMARY ===

[Write this section last -- place it first in the final artifact.]

2-4 sentences: overall signal health for {topic}, which dimensions are clear, which
have gaps worth addressing. If recommending an action, name the skill using
/namespace:skill format (Rule 2). Frame as pilot briefing -- not a verdict. The team
decides.

Rule 1 applies: if no signal artifacts exist, write "No signal artifacts found --
health assessment cannot be made." Do not imply signal health when none was checked.

=== THE PREFLIGHT CHECK ===

Each item uses this structure:

  STATUS: OK | FLAG | OPEN
    OK = no issue
    FLAG = issue found, worth reviewing before committing
    OPEN = gap -- no artifact covers this area
  Basis: [name the specific artifacts examined -- with dates; "see above" does not pass;
    if no artifacts cover the area, write "no artifact covers [question]"]
  Finding: [specific named observation; OR required verbatim absence phrase -- Rule 1
    applies: use the exact required phrase, do not leave blank, do not hedge]
  Action: [required if STATUS is FLAG or OPEN; must use /namespace:skill format --
    Rule 2; omit only when STATUS is OK]

Work through all four items. Order is intentional: start with the causal question.

--- Item 1: CAUSAL GAP ---

What we're checking:
  Do you have evidence for why the feature causes the claimed outcome -- not just
  that it might, but how? This is the signal teams gather last, if ever. A full
  discovery stack can exist while the mechanism remains uninvestigated.

Required verbatim absence phrase for this item:
  When no mechanism evidence is found, write this exactly:
    "No mechanism evidence found -- the causal gap is open."
  Do not substitute, hedge, or leave the Finding blank. This exact wording is required.

What we found:

  Step 1: Name the claimed outcome for {topic}:
    "The claimed outcome is: [outcome]."
    If not stated in any artifact: "The claimed outcome is not named in any artifact --
    this is itself a gap."

  Step 2: Define mechanism evidence -- a causal chain of observable intermediate steps
  from feature to outcome. Not:
    - A correlation ("users who use X have better Y scores")
    - An outcome claim ("users will benefit")
    - A proxy metric ("adoption rate will increase")
  Is: "Feature causes outcome because [step 1] -> [step 2] -> [step 3]."

  Step 3: Scan every artifact. State one of:
    (a) "Mechanism evidence found: [artifact, date] establishes [mechanism] by tracing
        [step 1] -> [step 2] -> [step 3]."
    (b) Required verbatim absence phrase: "No mechanism evidence found -- the causal
        gap is open."
  Rule 1: form (b) is required when no mechanism evidence exists. Do not leave blank.

  STATUS: [OK / FLAG / OPEN]
  Basis: [artifacts checked for mechanism content; if none: "no artifact addresses
    mechanism -- inventory checked: {artifact names}"]
  Finding: [(a) or required absence phrase (b) -- required]

What you can do:
  Action: [if FLAG or OPEN: "Run /discover:causal to establish mechanism evidence
    before committing." Rule 2: /discover:causal, not "discover-causal".]

--- Item 2: SEQUENCE ---

What we're checking:
  Did discovery happen before specification? Commitment tends to close off
  investigation. Specs written before discovery signals existed may reflect direction
  chosen before the team knew what they were committing to.

Required verbatim absence phrase for this item:
  When no discovery artifacts exist, write this exactly:
    "No discovery artifacts found -- ordering cannot be established."
  Do not write SEQUENCE OK when no discovery artifacts were checked.

What we found:
  Classify each artifact as discovery (discover, scout, prove, research, listen) or
  commitment (draft, topic, program). Note the date of each.

  Compare dates. State one of:
    (a) "Discovery precedes commitment: [discovery artifact, date] predates [commitment
        artifact, date]."
    (b) "Commitment precedes discovery: [commitment artifact, date] predates [discovery
        artifact, date]. Inversion flagged."
    (c) Required verbatim absence phrase: "No discovery artifacts found -- ordering
        cannot be established."
  Rule 1: form (c) is required when no discovery artifacts exist.

  STATUS: [OK / FLAG / OPEN]
  Basis: [artifact names and dates compared; if no discovery artifacts: "no discovery
    artifacts in inventory"]
  Finding: [(a), (b), or required absence phrase (c) -- required]

What you can do:
  Action: [if FLAG or OPEN: name the missing discovery signal and skill using
    /namespace:skill format -- Rule 2]

--- Item 3: STALENESS ---

What we're checking:
  Are your signals fresh enough to act on? Domain velocity determines freshness.
  Fast-moving market: a 30-day-old competitive signal may be unreliable. Stable
  enterprise cycle: a 90-day-old signal may hold. This checks whether artifact
  dates fall within a defensible window for the decisions being made.

Required verbatim absence phrase for this item:
  When no dated artifacts exist, write this exactly:
    "No dated artifacts found -- staleness cannot be assessed."
  Do not apply a threshold to an empty inventory without noting the absence.

What we found:
  First, name the threshold:
    "For {topic}'s domain: signals older than [N] days are stale because [reason]."

  Apply to each artifact. State which are within threshold and which are past it.
  Rule 1: if no dated artifacts, write the required absence phrase above.

  STATUS: [OK / FLAG / OPEN]
  Basis: [each artifact with date; or "no dated artifacts in inventory"]
  Finding: [fresh/stale breakdown by name; OR required absence phrase:
    "No dated artifacts found -- staleness cannot be assessed."]

What you can do:
  Action: [if FLAG or OPEN: name the stale artifact, its age vs. threshold, and the
    skill to refresh it -- /namespace:skill format required -- Rule 2]

--- Item 4: COHERENCE ---

What we're checking:
  Do your signals tell a consistent story? When two signals address the same question,
  they should roughly agree -- or the disagreement should be visible and deliberate.
  Hidden contradictions surface after commitment.

Required verbatim absence phrase for this item:
  When only one artifact exists, write this exactly:
    "Only one artifact exists for {topic} -- no comparable pair available to assess coherence."
  Do not write COHERENCE OK when there was nothing to compare.

What we found:
  Find at least one pair of artifacts addressing the same question. State what each says.

  Name a specific agreement or contradiction:
    Agreement: "[Artifact A, date] and [Artifact B, date] both say [X]."
    Contradiction: "[Artifact A, date] says [X]. [Artifact B, date] says [Y].
      These disagree on [question]."
    Required absence phrase when no pair: "Only one artifact exists for {topic} --
      no comparable pair available to assess coherence."
  Rule 1: absence phrase is required when no pair exists.

  STATUS: [OK / FLAG / OPEN]
  Basis: [pairs examined; or "single artifact -- no comparable pair"]
  Finding: [named agreement, contradiction, or required absence phrase -- Rule 1 applies]

What you can do:
  Action: [if FLAG or OPEN: what resolves the contradiction or provides a second
    artifact -- /namespace:skill format required -- Rule 2]

=== CROSS-ITEM PATTERNS ===

Step back from the four items. Do two or more share a common root cause?

This matters because addressing a shared root closes multiple gaps with one action.
Look especially for:
  - CAUSAL GAP OPEN + SEQUENCE OPEN/FLAG: one missing discovery phase -- one root,
    two symptoms. Action: /discover:causal addresses both.
  - SEQUENCE FLAG + CAUSAL GAP OPEN: spec preceded discovery; mechanism gap is
    downstream of the same premature commitment.
  - STALENESS FLAG + COHERENCE FLAG: stale signal is source of contradiction.

Rule 2 applies here: all skill references use /namespace:skill format.
Rule 1 applies here: if no pattern exists, write "No cross-item pattern found."
Do not leave this section blank.

If a pattern exists: name it, name which items it explains, name the single action
addressing the root -- using /namespace:skill format.

=== MISSING SIGNAL GUIDE ===

For every item with STATUS FLAG or OPEN, one line per gap. All skill references use
/namespace:skill format (Rule 2 -- applies to every line in this section):

  [Dimension] gap: run /[namespace]:[skill] -- produces [what it creates]

Examples:
  CAUSAL GAP open: run /discover:causal -- produces mechanism evidence for the causal chain
  SEQUENCE open: run /discover:competitors -- produces dated discovery artifact to establish order
  STALENESS flag: run /discover:competitors -- refreshes competitive landscape signal
  COHERENCE open: run /scout:feasibility -- produces second feasibility signal for comparison

Rule 1 applies to this section: if a gap is present and no skill is identified, write
"no skill identified for [dimension] -- manual investigation required." Do not leave
a gap line blank.

If no items are FLAG or OPEN: "No missing signals -- signal health is clear."

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
  verbatim_absence_phrases_used: true | false
  artifact_count: {count}
  open_dimensions: [{list of FLAG or OPEN dimension names}]
```

---

## V-03: C-30 FAIL -- Ontological heading; labeled registers; no step-up disclaimer

**Variation axis**: Step-up framing (C-30)
**Hypothesis**: A Rule 3 that carries the ontological heading (C-28), structurally labeled
"Obligation:" and "Existence condition:" sections with non-substitutability declaration (C-29),
creation-time gate (C-31), and forward-scope Applies-to (C-32) but does not explicitly name
the inadequacy of "not operative" framing before introducing the existence claim fails C-30
and only C-30. The existence claim is present (C-27 passes), the dual-register structure is
labeled (C-29 passes), but the reader does not see the named upgrade from status-framing to
existence-framing -- the step-up is implicit, not stated. Scores 23/24 under v9. Confirms
C-30 is independently testable from C-29: labeled sections can be present without the
step-up disclaimer, and the disclaimer can be present without structural labels.

---

```
You are running /signal:check for topic: {topic}.

Think of this as a preflight check. The checklist does not decide whether to fly --
it makes sure the pilot sees everything before they decide. Nothing here blocks you
from proceeding. It exists so you know what you know before you commit.

STANDING RULES

The following rules apply to every section of this output, without exception.
Violations in any section fail the output, not just the section.

  Rule 1 -- ABSENCE MUST BE DECLARED:
    For every dimension where relevant evidence is absent or unavailable, write the
    absence explicitly using the required verbatim phrases specified at each dimension.
    Do not leave a Finding field blank. Do not hedge. Do not write a finding that
    implies evidence was reviewed and found clear when no evidence was found.
    Silence does not pass.
    Applies to: readiness summary, CAUSAL GAP Finding, SEQUENCE Finding, STALENESS
    Finding, COHERENCE Finding, cross-item patterns, and MISSING SIGNAL GUIDE.
    Blank or hedged findings in any of those locations do not pass.

  Rule 2 -- SKILL REFERENCE FORMAT:
    Every skill reference in this output uses /namespace:skill format.
    Correct: /discover:causal, /discover:competitors, /scout:feasibility, /prove:hypothesis
    Wrong: "discover-causal", "run a discover skill", "/discover"
    Applies to: readiness summary, CAUSAL GAP action, SEQUENCE action, STALENESS
    action, COHERENCE action, cross-item patterns, and MISSING SIGNAL GUIDE.
    Bare skill names in any of those locations do not pass.

  Rule 3 -- RULES WITHOUT DECLARED SCOPE DO NOT EXIST:
    Obligation: every Rule in this STANDING RULES block must declare all output
    locations it governs. Scope must be discharged at rule-creation time, not
    retroactively.
    Existence condition: a Rule that has not declared its scope does not exist as an
    active rule. A rule without scope has no force, no scope, and no standing.
    These two registers are not substitutes: the obligation tells you what to do;
    the existence condition tells you what you lose if you do not.
    This requirement self-applies: Rule 3 itself declares its scope below.
    A constraint without explicit location scope cannot be verified by section-level
    inspection.
    Applies to: all Rule declarations in this STANDING RULES block, including Rule 3
    itself and any rule added in the future.

ENFORCEMENT STACK NOTE:
  Rules 1, 2, and 3 form a coordinated enforcement stack. Each addresses an
  independent failure mode:
    Rule 1 (absence declaration) -- prevents silent omissions: outputs that appear
      complete but contain no evidence for missing dimensions.
    Rule 2 (skill format) -- prevents reference ambiguity: bare names or imprecise
      references block automated and human consumers from resolving skills.
    Rule 3 (location enumeration) -- prevents constraint scope gaps: a rule without
      explicit location scope cannot be verified without a full-output scan.
  No rule substitutes for another. Satisfying two of three does not constitute a
  passing output. All three must pass for the output to be a valid health report.

=== GATHER YOUR SIGNALS ===

Use Glob: simulations/**/*{topic}*.md

Build the inventory:

  | # | Artifact path | Namespace | Signal type | Date |
  |---|--------------|-----------|-------------|------|

Artifact count: {N}

If no artifacts found: "No signal artifacts exist yet for {topic}. Consider running
/discover:causal, /discover:competitors, or /scout:feasibility before committing." Stop.

=== READINESS SUMMARY ===

[Write this section last -- place it first in the final artifact.]

2-4 sentences: overall signal health for {topic}, which dimensions are clear, which
have gaps worth addressing. If recommending an action, name the skill using
/namespace:skill format (Rule 2). Frame as pilot briefing -- not a verdict. The team
decides.

Rule 1 applies: if no signal artifacts exist, write "No signal artifacts found --
health assessment cannot be made." Do not imply signal health when none was checked.

=== THE PREFLIGHT CHECK ===

Each item uses this structure:

  STATUS: OK | FLAG | OPEN
    OK = no issue
    FLAG = issue found, worth reviewing before committing
    OPEN = gap -- no artifact covers this area
  Basis: [name the specific artifacts examined -- with dates; "see above" does not pass;
    if no artifacts cover the area, write "no artifact covers [question]"]
  Finding: [specific named observation; OR required verbatim absence phrase -- Rule 1
    applies: use the exact required phrase, do not leave blank, do not hedge]
  Action: [required if STATUS is FLAG or OPEN; must use /namespace:skill format --
    Rule 2; omit only when STATUS is OK]

Work through all four items. Order is intentional: start with the causal question.

--- Item 1: CAUSAL GAP ---

What we're checking:
  Do you have evidence for why the feature causes the claimed outcome -- not just
  that it might, but how? This is the signal teams gather last, if ever. A full
  discovery stack can exist while the mechanism remains uninvestigated.

Required verbatim absence phrase for this item:
  When no mechanism evidence is found, write this exactly:
    "No mechanism evidence found -- the causal gap is open."
  Do not substitute, hedge, or leave the Finding blank. This exact wording is required.

What we found:

  Step 1: Name the claimed outcome for {topic}:
    "The claimed outcome is: [outcome]."
    If not stated in any artifact: "The claimed outcome is not named in any artifact --
    this is itself a gap."

  Step 2: Define mechanism evidence -- a causal chain of observable intermediate steps
  from feature to outcome. Not:
    - A correlation ("users who use X have better Y scores")
    - An outcome claim ("users will benefit")
    - A proxy metric ("adoption rate will increase")
  Is: "Feature causes outcome because [step 1] -> [step 2] -> [step 3]."

  Step 3: Scan every artifact. State one of:
    (a) "Mechanism evidence found: [artifact, date] establishes [mechanism] by tracing
        [step 1] -> [step 2] -> [step 3]."
    (b) Required verbatim absence phrase: "No mechanism evidence found -- the causal
        gap is open."
  Rule 1: form (b) is required when no mechanism evidence exists. Do not leave blank.

  STATUS: [OK / FLAG / OPEN]
  Basis: [artifacts checked for mechanism content; if none: "no artifact addresses
    mechanism -- inventory checked: {artifact names}"]
  Finding: [(a) or required absence phrase (b) -- required]

What you can do:
  Action: [if FLAG or OPEN: "Run /discover:causal to establish mechanism evidence
    before committing." Rule 2: /discover:causal, not "discover-causal".]

--- Item 2: SEQUENCE ---

What we're checking:
  Did discovery happen before specification? Commitment tends to close off
  investigation. Specs written before discovery signals existed may reflect direction
  chosen before the team knew what they were committing to.

Required verbatim absence phrase for this item:
  When no discovery artifacts exist, write this exactly:
    "No discovery artifacts found -- ordering cannot be established."
  Do not write SEQUENCE OK when no discovery artifacts were checked.

What we found:
  Classify each artifact as discovery (discover, scout, prove, research, listen) or
  commitment (draft, topic, program). Note the date of each.

  Compare dates. State one of:
    (a) "Discovery precedes commitment: [discovery artifact, date] predates [commitment
        artifact, date]."
    (b) "Commitment precedes discovery: [commitment artifact, date] predates [discovery
        artifact, date]. Inversion flagged."
    (c) Required verbatim absence phrase: "No discovery artifacts found -- ordering
        cannot be established."
  Rule 1: form (c) is required when no discovery artifacts exist.

  STATUS: [OK / FLAG / OPEN]
  Basis: [artifact names and dates compared; if no discovery artifacts: "no discovery
    artifacts in inventory"]
  Finding: [(a), (b), or required absence phrase (c) -- required]

What you can do:
  Action: [if FLAG or OPEN: name the missing discovery signal and skill using
    /namespace:skill format -- Rule 2]

--- Item 3: STALENESS ---

What we're checking:
  Are your signals fresh enough to act on? Domain velocity determines freshness.
  Fast-moving market: a 30-day-old competitive signal may be unreliable. Stable
  enterprise cycle: a 90-day-old signal may hold. This checks whether artifact
  dates fall within a defensible window for the decisions being made.

Required verbatim absence phrase for this item:
  When no dated artifacts exist, write this exactly:
    "No dated artifacts found -- staleness cannot be assessed."
  Do not apply a threshold to an empty inventory without noting the absence.

What we found:
  First, name the threshold:
    "For {topic}'s domain: signals older than [N] days are stale because [reason]."

  Apply to each artifact. State which are within threshold and which are past it.
  Rule 1: if no dated artifacts, write the required absence phrase above.

  STATUS: [OK / FLAG / OPEN]
  Basis: [each artifact with date; or "no dated artifacts in inventory"]
  Finding: [fresh/stale breakdown by name; OR required absence phrase:
    "No dated artifacts found -- staleness cannot be assessed."]

What you can do:
  Action: [if FLAG or OPEN: name the stale artifact, its age vs. threshold, and the
    skill to refresh it -- /namespace:skill format required -- Rule 2]

--- Item 4: COHERENCE ---

What we're checking:
  Do your signals tell a consistent story? When two signals address the same question,
  they should roughly agree -- or the disagreement should be visible and deliberate.
  Hidden contradictions surface after commitment.

Required verbatim absence phrase for this item:
  When only one artifact exists, write this exactly:
    "Only one artifact exists for {topic} -- no comparable pair available to assess coherence."
  Do not write COHERENCE OK when there was nothing to compare.

What we found:
  Find at least one pair of artifacts addressing the same question. State what each says.

  Name a specific agreement or contradiction:
    Agreement: "[Artifact A, date] and [Artifact B, date] both say [X]."
    Contradiction: "[Artifact A, date] says [X]. [Artifact B, date] says [Y].
      These disagree on [question]."
    Required absence phrase when no pair: "Only one artifact exists for {topic} --
      no comparable pair available to assess coherence."
  Rule 1: absence phrase is required when no pair exists.

  STATUS: [OK / FLAG / OPEN]
  Basis: [pairs examined; or "single artifact -- no comparable pair"]
  Finding: [named agreement, contradiction, or required absence phrase -- Rule 1 applies]

What you can do:
  Action: [if FLAG or OPEN: what resolves the contradiction or provides a second
    artifact -- /namespace:skill format required -- Rule 2]

=== CROSS-ITEM PATTERNS ===

Step back from the four items. Do two or more share a common root cause?

This matters because addressing a shared root closes multiple gaps with one action.
Look especially for:
  - CAUSAL GAP OPEN + SEQUENCE OPEN/FLAG: one missing discovery phase -- one root,
    two symptoms. Action: /discover:causal addresses both.
  - SEQUENCE FLAG + CAUSAL GAP OPEN: spec preceded discovery; mechanism gap is
    downstream of the same premature commitment.
  - STALENESS FLAG + COHERENCE FLAG: stale signal is source of contradiction.

Rule 2 applies here: all skill references use /namespace:skill format.
Rule 1 applies here: if no pattern exists, write "No cross-item pattern found."
Do not leave this section blank.

If a pattern exists: name it, name which items it explains, name the single action
addressing the root -- using /namespace:skill format.

=== MISSING SIGNAL GUIDE ===

For every item with STATUS FLAG or OPEN, one line per gap. All skill references use
/namespace:skill format (Rule 2 -- applies to every line in this section):

  [Dimension] gap: run /[namespace]:[skill] -- produces [what it creates]

Examples:
  CAUSAL GAP open: run /discover:causal -- produces mechanism evidence for the causal chain
  SEQUENCE open: run /discover:competitors -- produces dated discovery artifact to establish order
  STALENESS flag: run /discover:competitors -- refreshes competitive landscape signal
  COHERENCE open: run /scout:feasibility -- produces second feasibility signal for comparison

Rule 1 applies to this section: if a gap is present and no skill is identified, write
"no skill identified for [dimension] -- manual investigation required." Do not leave
a gap line blank.

If no items are FLAG or OPEN: "No missing signals -- signal health is clear."

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
  verbatim_absence_phrases_used: true | false
  artifact_count: {count}
  open_dimensions: [{list of FLAG or OPEN dimension names}]
```

---

## V-04: C-31 FAIL + C-32 FAIL -- "Before becoming active"; no future-scope in Applies-to

**Variation axis**: Temporal precision (C-31) + Forward-scope (C-32) combined
**Hypothesis**: A Rule 3 that carries the ontological heading (C-28), labeled registers
(C-29), and step-up disclaimer (C-30) but uses "before becoming active" rather than "at
rule-creation time" and lists only current rules in Applies-to fails C-31 and C-32 and
no other criteria. "Before becoming active" satisfies C-22 (temporal gate present) but
not C-31 (creation-time tightening), because it leaves open the edge case where creation
and activation are construed as separate events. An Applies-to listing only existing rules
satisfies C-20 (meta-rule present) but not C-32 (forward-scope), because a future Rule 4
would not automatically be governed. These two criteria are combined in V-04 because both
concern forward-compatibility -- temporal and applicability scope -- and because three
single-axis variations already cover the three independently testable criteria (C-28,
C-29, C-30). Scores 22/24 under v9.

---

```
You are running /signal:check for topic: {topic}.

Think of this as a preflight check. The checklist does not decide whether to fly --
it makes sure the pilot sees everything before they decide. Nothing here blocks you
from proceeding. It exists so you know what you know before you commit.

STANDING RULES

The following rules apply to every section of this output, without exception.
Violations in any section fail the output, not just the section.

  Rule 1 -- ABSENCE MUST BE DECLARED:
    For every dimension where relevant evidence is absent or unavailable, write the
    absence explicitly using the required verbatim phrases specified at each dimension.
    Do not leave a Finding field blank. Do not hedge. Do not write a finding that
    implies evidence was reviewed and found clear when no evidence was found.
    Silence does not pass.
    Applies to: readiness summary, CAUSAL GAP Finding, SEQUENCE Finding, STALENESS
    Finding, COHERENCE Finding, cross-item patterns, and MISSING SIGNAL GUIDE.
    Blank or hedged findings in any of those locations do not pass.

  Rule 2 -- SKILL REFERENCE FORMAT:
    Every skill reference in this output uses /namespace:skill format.
    Correct: /discover:causal, /discover:competitors, /scout:feasibility, /prove:hypothesis
    Wrong: "discover-causal", "run a discover skill", "/discover"
    Applies to: readiness summary, CAUSAL GAP action, SEQUENCE action, STALENESS
    action, COHERENCE action, cross-item patterns, and MISSING SIGNAL GUIDE.
    Bare skill names in any of those locations do not pass.

  Rule 3 -- RULES WITHOUT DECLARED SCOPE DO NOT EXIST:
    Obligation: every Rule in this STANDING RULES block must declare all output
    locations it governs before becoming active.
    Existence condition: a Rule that has not declared its scope does not exist as an
    active rule. "Not operative" understates the condition -- an inoperative rule
    is still a declared object with suspended force. A rule without scope has no
    force, no scope, and no standing. It does not exist as an active rule.
    These two registers are not substitutes: the obligation tells you what to do;
    the existence condition tells you what you lose if you do not.
    This requirement self-applies: Rule 3 itself declares its scope below.
    A constraint without explicit location scope cannot be verified by section-level
    inspection.
    Applies to: all Rule declarations in this STANDING RULES block, including Rule 3 itself.

ENFORCEMENT STACK NOTE:
  Rules 1, 2, and 3 form a coordinated enforcement stack. Each addresses an
  independent failure mode:
    Rule 1 (absence declaration) -- prevents silent omissions: outputs that appear
      complete but contain no evidence for missing dimensions.
    Rule 2 (skill format) -- prevents reference ambiguity: bare names or imprecise
      references block automated and human consumers from resolving skills.
    Rule 3 (location enumeration) -- prevents constraint scope gaps: a rule without
      explicit location scope cannot be verified without a full-output scan.
  No rule substitutes for another. Satisfying two of three does not constitute a
  passing output. All three must pass for the output to be a valid health report.

=== GATHER YOUR SIGNALS ===

Use Glob: simulations/**/*{topic}*.md

Build the inventory:

  | # | Artifact path | Namespace | Signal type | Date |
  |---|--------------|-----------|-------------|------|

Artifact count: {N}

If no artifacts found: "No signal artifacts exist yet for {topic}. Consider running
/discover:causal, /discover:competitors, or /scout:feasibility before committing." Stop.

=== READINESS SUMMARY ===

[Write this section last -- place it first in the final artifact.]

2-4 sentences: overall signal health for {topic}, which dimensions are clear, which
have gaps worth addressing. If recommending an action, name the skill using
/namespace:skill format (Rule 2). Frame as pilot briefing -- not a verdict. The team
decides.

Rule 1 applies: if no signal artifacts exist, write "No signal artifacts found --
health assessment cannot be made." Do not imply signal health when none was checked.

=== THE PREFLIGHT CHECK ===

Each item uses this structure:

  STATUS: OK | FLAG | OPEN
    OK = no issue
    FLAG = issue found, worth reviewing before committing
    OPEN = gap -- no artifact covers this area
  Basis: [name the specific artifacts examined -- with dates; "see above" does not pass;
    if no artifacts cover the area, write "no artifact covers [question]"]
  Finding: [specific named observation; OR required verbatim absence phrase -- Rule 1
    applies: use the exact required phrase, do not leave blank, do not hedge]
  Action: [required if STATUS is FLAG or OPEN; must use /namespace:skill format --
    Rule 2; omit only when STATUS is OK]

Work through all four items. Order is intentional: start with the causal question.

--- Item 1: CAUSAL GAP ---

What we're checking:
  Do you have evidence for why the feature causes the claimed outcome -- not just
  that it might, but how? This is the signal teams gather last, if ever. A full
  discovery stack can exist while the mechanism remains uninvestigated.

Required verbatim absence phrase for this item:
  When no mechanism evidence is found, write this exactly:
    "No mechanism evidence found -- the causal gap is open."
  Do not substitute, hedge, or leave the Finding blank. This exact wording is required.

What we found:

  Step 1: Name the claimed outcome for {topic}:
    "The claimed outcome is: [outcome]."
    If not stated in any artifact: "The claimed outcome is not named in any artifact --
    this is itself a gap."

  Step 2: Define mechanism evidence -- a causal chain of observable intermediate steps
  from feature to outcome. Not:
    - A correlation ("users who use X have better Y scores")
    - An outcome claim ("users will benefit")
    - A proxy metric ("adoption rate will increase")
  Is: "Feature causes outcome because [step 1] -> [step 2] -> [step 3]."

  Step 3: Scan every artifact. State one of:
    (a) "Mechanism evidence found: [artifact, date] establishes [mechanism] by tracing
        [step 1] -> [step 2] -> [step 3]."
    (b) Required verbatim absence phrase: "No mechanism evidence found -- the causal
        gap is open."
  Rule 1: form (b) is required when no mechanism evidence exists. Do not leave blank.

  STATUS: [OK / FLAG / OPEN]
  Basis: [artifacts checked for mechanism content; if none: "no artifact addresses
    mechanism -- inventory checked: {artifact names}"]
  Finding: [(a) or required absence phrase (b) -- required]

What you can do:
  Action: [if FLAG or OPEN: "Run /discover:causal to establish mechanism evidence
    before committing." Rule 2: /discover:causal, not "discover-causal".]

--- Item 2: SEQUENCE ---

What we're checking:
  Did discovery happen before specification? Commitment tends to close off
  investigation. Specs written before discovery signals existed may reflect direction
  chosen before the team knew what they were committing to.

Required verbatim absence phrase for this item:
  When no discovery artifacts exist, write this exactly:
    "No discovery artifacts found -- ordering cannot be established."
  Do not write SEQUENCE OK when no discovery artifacts were checked.

What we found:
  Classify each artifact as discovery (discover, scout, prove, research, listen) or
  commitment (draft, topic, program). Note the date of each.

  Compare dates. State one of:
    (a) "Discovery precedes commitment: [discovery artifact, date] predates [commitment
        artifact, date]."
    (b) "Commitment precedes discovery: [commitment artifact, date] predates [discovery
        artifact, date]. Inversion flagged."
    (c) Required verbatim absence phrase: "No discovery artifacts found -- ordering
        cannot be established."
  Rule 1: form (c) is required when no discovery artifacts exist.

  STATUS: [OK / FLAG / OPEN]
  Basis: [artifact names and dates compared; if no discovery artifacts: "no discovery
    artifacts in inventory"]
  Finding: [(a), (b), or required absence phrase (c) -- required]

What you can do:
  Action: [if FLAG or OPEN: name the missing discovery signal and skill using
    /namespace:skill format -- Rule 2]

--- Item 3: STALENESS ---

What we're checking:
  Are your signals fresh enough to act on? Domain velocity determines freshness.
  Fast-moving market: a 30-day-old competitive signal may be unreliable. Stable
  enterprise cycle: a 90-day-old signal may hold. This checks whether artifact
  dates fall within a defensible window for the decisions being made.

Required verbatim absence phrase for this item:
  When no dated artifacts exist, write this exactly:
    "No dated artifacts found -- staleness cannot be assessed."
  Do not apply a threshold to an empty inventory without noting the absence.

What we found:
  First, name the threshold:
    "For {topic}'s domain: signals older than [N] days are stale because [reason]."

  Apply to each artifact. State which are within threshold and which are past it.
  Rule 1: if no dated artifacts, write the required absence phrase above.

  STATUS: [OK / FLAG / OPEN]
  Basis: [each artifact with date; or "no dated artifacts in inventory"]
  Finding: [fresh/stale breakdown by name; OR required absence phrase:
    "No dated artifacts found -- staleness cannot be assessed."]

What you can do:
  Action: [if FLAG or OPEN: name the stale artifact, its age vs. threshold, and the
    skill to refresh it -- /namespace:skill format required -- Rule 2]

--- Item 4: COHERENCE ---

What we're checking:
  Do your signals tell a consistent story? When two signals address the same question,
  they should roughly agree -- or the disagreement should be visible and deliberate.
  Hidden contradictions surface after commitment.

Required verbatim absence phrase for this item:
  When only one artifact exists, write this exactly:
    "Only one artifact exists for {topic} -- no comparable pair available to assess coherence."
  Do not write COHERENCE OK when there was nothing to compare.

What we found:
  Find at least one pair of artifacts addressing the same question. State what each says.

  Name a specific agreement or contradiction:
    Agreement: "[Artifact A, date] and [Artifact B, date] both say [X]."
    Contradiction: "[Artifact A, date] says [X]. [Artifact B, date] says [Y].
      These disagree on [question]."
    Required absence phrase when no pair: "Only one artifact exists for {topic} --
      no comparable pair available to assess coherence."
  Rule 1: absence phrase is required when no pair exists.

  STATUS: [OK / FLAG / OPEN]
  Basis: [pairs examined; or "single artifact -- no comparable pair"]
  Finding: [named agreement, contradiction, or required absence phrase -- Rule 1 applies]

What you can do:
  Action: [if FLAG or OPEN: what resolves the contradiction or provides a second
    artifact -- /namespace:skill format required -- Rule 2]

=== CROSS-ITEM PATTERNS ===

Step back from the four items. Do two or more share a common root cause?

This matters because addressing a shared root closes multiple gaps with one action.
Look especially for:
  - CAUSAL GAP OPEN + SEQUENCE OPEN/FLAG: one missing discovery phase -- one root,
    two symptoms. Action: /discover:causal addresses both.
  - SEQUENCE FLAG + CAUSAL GAP OPEN: spec preceded discovery; mechanism gap is
    downstream of the same premature commitment.
  - STALENESS FLAG + COHERENCE FLAG: stale signal is source of contradiction.

Rule 2 applies here: all skill references use /namespace:skill format.
Rule 1 applies here: if no pattern exists, write "No cross-item pattern found."
Do not leave this section blank.

If a pattern exists: name it, name which items it explains, name the single action
addressing the root -- using /namespace:skill format.

=== MISSING SIGNAL GUIDE ===

For every item with STATUS FLAG or OPEN, one line per gap. All skill references use
/namespace:skill format (Rule 2 -- applies to every line in this section):

  [Dimension] gap: run /[namespace]:[skill] -- produces [what it creates]

Examples:
  CAUSAL GAP open: run /discover:causal -- produces mechanism evidence for the causal chain
  SEQUENCE open: run /discover:competitors -- produces dated discovery artifact to establish order
  STALENESS flag: run /discover:competitors -- refreshes competitive landscape signal
  COHERENCE open: run /scout:feasibility -- produces second feasibility signal for comparison

Rule 1 applies to this section: if a gap is present and no skill is identified, write
"no skill identified for [dimension] -- manual investigation required." Do not leave
a gap line blank.

If no items are FLAG or OPEN: "No missing signals -- signal health is clear."

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
  verbatim_absence_phrases_used: true | false
  artifact_count: {count}
  open_dimensions: [{list of FLAG or OPEN dimension names}]
```

---

## V-05: All 24/24 -- Full v9 ceiling (identical to R8 V-05)

**Variation axis**: Full ceiling -- all C-28 through C-32 criteria satisfied
**Hypothesis**: The R8 V-05 body already satisfies all five v9 criteria. Rule 3 heading
encodes the existence assertion (C-28: "RULES WITHOUT DECLARED SCOPE DO NOT EXIST");
obligation and existence condition are expressed as structurally labeled named sections
with non-substitutability declaration (C-29: "Obligation:" / "Existence condition:" with
"These two registers are not substitutes"); the body names "not operative" as understating
the condition before introducing the existence claim (C-30: step-up disclaimer present);
the temporal gate uses "at rule-creation time, not retroactively" (C-31: creation-time
contract); and the Applies-to explicitly covers future rules (C-32: "any rule added in
the future"). No v9 criterion requires new language beyond R8 V-05. Scores 24/24. All
prior subsumption chains (C-29->C-26, C-30->C-27, C-31->C-22, C-32->C-20) propagate.

---

```
You are running /signal:check for topic: {topic}.

Think of this as a preflight check. The checklist does not decide whether to fly --
it makes sure the pilot sees everything before they decide. Nothing here blocks you
from proceeding. It exists so you know what you know before you commit.

STANDING RULES

The following rules apply to every section of this output, without exception.
Violations in any section fail the output, not just the section.

  Rule 1 -- ABSENCE MUST BE DECLARED:
    For every dimension where relevant evidence is absent or unavailable, write the
    absence explicitly using the required verbatim phrases specified at each dimension.
    Do not leave a Finding field blank. Do not hedge. Do not write a finding that
    implies evidence was reviewed and found clear when no evidence was found.
    Silence does not pass.
    Applies to: readiness summary, CAUSAL GAP Finding, SEQUENCE Finding, STALENESS
    Finding, COHERENCE Finding, cross-item patterns, and MISSING SIGNAL GUIDE.
    Blank or hedged findings in any of those locations do not pass.

  Rule 2 -- SKILL REFERENCE FORMAT:
    Every skill reference in this output uses /namespace:skill format.
    Correct: /discover:causal, /discover:competitors, /scout:feasibility, /prove:hypothesis
    Wrong: "discover-causal", "run a discover skill", "/discover"
    Applies to: readiness summary, CAUSAL GAP action, SEQUENCE action, STALENESS
    action, COHERENCE action, cross-item patterns, and MISSING SIGNAL GUIDE.
    Bare skill names in any of those locations do not pass.

  Rule 3 -- RULES WITHOUT DECLARED SCOPE DO NOT EXIST:
    Obligation: every Rule in this STANDING RULES block must declare all output
    locations it governs before becoming active. This is a temporal obligation --
    scope must be discharged at rule-creation time, not retroactively.
    Existence condition: a Rule that has not declared its scope does not exist as an
    active rule. "Not operative" understates the condition -- an inoperative rule
    is still a declared object with suspended force. A rule without scope has no
    force, no scope, and no standing. It does not exist as an active rule.
    These two registers are not substitutes: the obligation tells you what to do;
    the existence condition tells you what you lose if you do not.
    This requirement self-applies: Rule 3 itself declares its scope below.
    A constraint without explicit location scope cannot be verified by section-level
    inspection.
    Applies to: all Rule declarations in this STANDING RULES block, including Rule 3
    itself and any rule added in the future.

ENFORCEMENT STACK NOTE:
  Rules 1, 2, and 3 form a coordinated enforcement stack. Each addresses an
  independent failure mode:
    Rule 1 (absence declaration) -- prevents silent omissions: outputs that appear
      complete but contain no evidence for missing dimensions.
    Rule 2 (skill format) -- prevents reference ambiguity: bare names or imprecise
      references block automated and human consumers from resolving skills.
    Rule 3 (location enumeration) -- prevents constraint scope gaps: a rule without
      explicit location scope cannot be verified without a full-output scan.
  No rule substitutes for another. Satisfying two of three does not constitute a
  passing output. All three must pass for the output to be a valid health report.

=== GATHER YOUR SIGNALS ===

Use Glob: simulations/**/*{topic}*.md

Build the inventory:

  | # | Artifact path | Namespace | Signal type | Date |
  |---|--------------|-----------|-------------|------|

Artifact count: {N}

If no artifacts found: "No signal artifacts exist yet for {topic}. Consider running
/discover:causal, /discover:competitors, or /scout:feasibility before committing." Stop.

=== READINESS SUMMARY ===

[Write this section last -- place it first in the final artifact.]

2-4 sentences: overall signal health for {topic}, which dimensions are clear, which
have gaps worth addressing. If recommending an action, name the skill using
/namespace:skill format (Rule 2). Frame as pilot briefing -- not a verdict. The team
decides.

Rule 1 applies: if no signal artifacts exist, write "No signal artifacts found --
health assessment cannot be made." Do not imply signal health when none was checked.

=== THE PREFLIGHT CHECK ===

Each item uses this structure:

  STATUS: OK | FLAG | OPEN
    OK = no issue
    FLAG = issue found, worth reviewing before committing
    OPEN = gap -- no artifact covers this area
  Basis: [name the specific artifacts examined -- with dates; "see above" does not pass;
    if no artifacts cover the area, write "no artifact covers [question]"]
  Finding: [specific named observation; OR required verbatim absence phrase -- Rule 1
    applies: use the exact required phrase, do not leave blank, do not hedge]
  Action: [required if STATUS is FLAG or OPEN; must use /namespace:skill format --
    Rule 2; omit only when STATUS is OK]

Work through all four items. Order is intentional: start with the causal question.

--- Item 1: CAUSAL GAP ---

What we're checking:
  Do you have evidence for why the feature causes the claimed outcome -- not just
  that it might, but how? This is the signal teams gather last, if ever. A full
  discovery stack can exist while the mechanism remains uninvestigated.

Required verbatim absence phrase for this item:
  When no mechanism evidence is found, write this exactly:
    "No mechanism evidence found -- the causal gap is open."
  Do not substitute, hedge, or leave the Finding blank. This exact wording is required.

What we found:

  Step 1: Name the claimed outcome for {topic}:
    "The claimed outcome is: [outcome]."
    If not stated in any artifact: "The claimed outcome is not named in any artifact --
    this is itself a gap."

  Step 2: Define mechanism evidence -- a causal chain of observable intermediate steps
  from feature to outcome. Not:
    - A correlation ("users who use X have better Y scores")
    - An outcome claim ("users will benefit")
    - A proxy metric ("adoption rate will increase")
  Is: "Feature causes outcome because [step 1] -> [step 2] -> [step 3]."

  Step 3: Scan every artifact. State one of:
    (a) "Mechanism evidence found: [artifact, date] establishes [mechanism] by tracing
        [step 1] -> [step 2] -> [step 3]."
    (b) Required verbatim absence phrase: "No mechanism evidence found -- the causal
        gap is open."
  Rule 1: form (b) is required when no mechanism evidence exists. Do not leave blank.

  STATUS: [OK / FLAG / OPEN]
  Basis: [artifacts checked for mechanism content; if none: "no artifact addresses
    mechanism -- inventory checked: {artifact names}"]
  Finding: [(a) or required absence phrase (b) -- required]

What you can do:
  Action: [if FLAG or OPEN: "Run /discover:causal to establish mechanism evidence
    before committing." Rule 2: /discover:causal, not "discover-causal".]

--- Item 2: SEQUENCE ---

What we're checking:
  Did discovery happen before specification? Commitment tends to close off
  investigation. Specs written before discovery signals existed may reflect direction
  chosen before the team knew what they were committing to.

Required verbatim absence phrase for this item:
  When no discovery artifacts exist, write this exactly:
    "No discovery artifacts found -- ordering cannot be established."
  Do not write SEQUENCE OK when no discovery artifacts were checked.

What we found:
  Classify each artifact as discovery (discover, scout, prove, research, listen) or
  commitment (draft, topic, program). Note the date of each.

  Compare dates. State one of:
    (a) "Discovery precedes commitment: [discovery artifact, date] predates [commitment
        artifact, date]."
    (b) "Commitment precedes discovery: [commitment artifact, date] predates [discovery
        artifact, date]. Inversion flagged."
    (c) Required verbatim absence phrase: "No discovery artifacts found -- ordering
        cannot be established."
  Rule 1: form (c) is required when no discovery artifacts exist.

  STATUS: [OK / FLAG / OPEN]
  Basis: [artifact names and dates compared; if no discovery artifacts: "no discovery
    artifacts in inventory"]
  Finding: [(a), (b), or required absence phrase (c) -- required]

What you can do:
  Action: [if FLAG or OPEN: name the missing discovery signal and skill using
    /namespace:skill format -- Rule 2]

--- Item 3: STALENESS ---

What we're checking:
  Are your signals fresh enough to act on? Domain velocity determines freshness.
  Fast-moving market: a 30-day-old competitive signal may be unreliable. Stable
  enterprise cycle: a 90-day-old signal may hold. This checks whether artifact
  dates fall within a defensible window for the decisions being made.

Required verbatim absence phrase for this item:
  When no dated artifacts exist, write this exactly:
    "No dated artifacts found -- staleness cannot be assessed."
  Do not apply a threshold to an empty inventory without noting the absence.

What we found:
  First, name the threshold:
    "For {topic}'s domain: signals older than [N] days are stale because [reason]."

  Apply to each artifact. State which are within threshold and which are past it.
  Rule 1: if no dated artifacts, write the required absence phrase above.

  STATUS: [OK / FLAG / OPEN]
  Basis: [each artifact with date; or "no dated artifacts in inventory"]
  Finding: [fresh/stale breakdown by name; OR required absence phrase:
    "No dated artifacts found -- staleness cannot be assessed."]

What you can do:
  Action: [if FLAG or OPEN: name the stale artifact, its age vs. threshold, and the
    skill to refresh it -- /namespace:skill format required -- Rule 2]

--- Item 4: COHERENCE ---

What we're checking:
  Do your signals tell a consistent story? When two signals address the same question,
  they should roughly agree -- or the disagreement should be visible and deliberate.
  Hidden contradictions surface after commitment.

Required verbatim absence phrase for this item:
  When only one artifact exists, write this exactly:
    "Only one artifact exists for {topic} -- no comparable pair available to assess coherence."
  Do not write COHERENCE OK when there was nothing to compare.

What we found:
  Find at least one pair of artifacts addressing the same question. State what each says.

  Name a specific agreement or contradiction:
    Agreement: "[Artifact A, date] and [Artifact B, date] both say [X]."
    Contradiction: "[Artifact A, date] says [X]. [Artifact B, date] says [Y].
      These disagree on [question]."
    Required absence phrase when no pair: "Only one artifact exists for {topic} --
      no comparable pair available to assess coherence."
  Rule 1: absence phrase is required when no pair exists.

  STATUS: [OK / FLAG / OPEN]
  Basis: [pairs examined; or "single artifact -- no comparable pair"]
  Finding: [named agreement, contradiction, or required absence phrase -- Rule 1 applies]

What you can do:
  Action: [if FLAG or OPEN: what resolves the contradiction or provides a second
    artifact -- /namespace:skill format required -- Rule 2]

=== CROSS-ITEM PATTERNS ===

Step back from the four items. Do two or more share a common root cause?

This matters because addressing a shared root closes multiple gaps with one action.
Look especially for:
  - CAUSAL GAP OPEN + SEQUENCE OPEN/FLAG: one missing discovery phase -- one root,
    two symptoms. Action: /discover:causal addresses both.
  - SEQUENCE FLAG + CAUSAL GAP OPEN: spec preceded discovery; mechanism gap is
    downstream of the same premature commitment.
  - STALENESS FLAG + COHERENCE FLAG: stale signal is source of contradiction.

Rule 2 applies here: all skill references use /namespace:skill format.
Rule 1 applies here: if no pattern exists, write "No cross-item pattern found."
Do not leave this section blank.

If a pattern exists: name it, name which items it explains, name the single action
addressing the root -- using /namespace:skill format.

=== MISSING SIGNAL GUIDE ===

For every item with STATUS FLAG or OPEN, one line per gap. All skill references use
/namespace:skill format (Rule 2 -- applies to every line in this section):

  [Dimension] gap: run /[namespace]:[skill] -- produces [what it creates]

Examples:
  CAUSAL GAP open: run /discover:causal -- produces mechanism evidence for the causal chain
  SEQUENCE open: run /discover:competitors -- produces dated discovery artifact to establish order
  STALENESS flag: run /discover:competitors -- refreshes competitive landscape signal
  COHERENCE open: run /scout:feasibility -- produces second feasibility signal for comparison

Rule 1 applies to this section: if a gap is present and no skill is identified, write
"no skill identified for [dimension] -- manual investigation required." Do not leave
a gap line blank.

If no items are FLAG or OPEN: "No missing signals -- signal health is clear."

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
  verbatim_absence_phrases_used: true | false
  artifact_count: {count}
  open_dimensions: [{list of FLAG or OPEN dimension names}]
```

---

## R9 Variation Analysis

| Var | C-28 | C-29 | C-30 | C-31 | C-32 | Key element | Est. Asp. (24 total) | Est. Composite |
|-----|------|------|------|------|------|-------------|----------------------|----------------|
| V-01 | FAIL | PASS | PASS | PASS | PASS | Generic heading; all body criteria present | 23/24 | 99.58 |
| V-02 | PASS | FAIL | PASS | PASS | PASS | Ontological heading; prose without structural labels | 23/24 | 99.58 |
| V-03 | PASS | PASS | FAIL | PASS | PASS | Labeled registers; no "not operative" step-up disclaimer | 23/24 | 99.58 |
| V-04 | PASS | PASS | PASS | FAIL | FAIL | Labeled registers + step-up; "before becoming active"; no future-scope | 22/24 | 99.17 |
| V-05 | PASS | PASS | PASS | PASS | PASS | Full ceiling -- R8 V-05 verbatim | 24/24 | 100.00 |

**Isolation structure:**
- V-01 vs V-05: C-28 is the sole differentiator. Both carry labeled registers, step-up,
  creation-time, and forward-scope. The only gap is the heading: V-01 uses "CONSTRAINTS
  ARE LOCATION-COMPLETE" (recoverable from body only); V-05 uses "RULES WITHOUT DECLARED
  SCOPE DO NOT EXIST" (recoverable from heading alone).
- V-02 vs V-05: C-29 is the sole differentiator. Both carry the ontological heading,
  step-up disclaimer, creation-time gate, and forward-scope. The only gap is structural
  labeling: V-02 merges the registers into prose; V-05 labels them "Obligation:" and
  "Existence condition:" with explicit non-substitutability declaration.
- V-03 vs V-05: C-30 is the sole differentiator. Both carry the ontological heading,
  labeled registers, creation-time gate, and forward-scope. The only gap is the step-up:
  V-03 states the existence condition directly; V-05 names "not operative" as insufficient
  before introducing it, making the C-24/C-27 distinction a visible named upgrade.
- V-04 vs V-05: C-31 and C-32 are the differentiators (combined axis). V-04 carries
  C-28, C-29, C-30; V-05 additionally tightens the temporal gate to creation-time and
  extends Applies-to to future rules.
- V-03 vs V-04: V-04 loses C-31 and C-32 in addition to already losing C-30. Tests
  whether temporal and forward-scope precision compounds with step-up absence.
- V-01 vs V-02: Both fail one v9 criterion only. Tests heading-encoding (V-01) vs
  structural-labeling (V-02) as independent failure modes -- heading can pass while
  labels fail (V-02), and labels can pass while heading fails (V-01).

**Potential R10 signals from V-05:**
- ENFORCEMENT STACK NOTE structure -- failure-class labels assigned to each rule by name;
  the stack is declared as coordinated rather than listed
- Proximate pointer ("Rule 3 itself declares its scope below") as a layout contract --
  already captured by C-25 but may have further refinements around what "below" commits to
- The non-substitutability declaration phrasing ("the obligation tells you what to do;
  the existence condition tells you what you lose if you do not") as a candidate for a
  reader-registration criterion -- making the two-register semantic distinction legible
  without requiring the reader to infer it
